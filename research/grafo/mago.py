#!/usr/bin/env python3
"""La mesa del Mago: candidatos a conexiones ocultas del segundo cerebro (solo stdlib).

Herramienta determinista de la mente "El Mago" (`.claude/skills/mentes/`). No interpreta:
pone sobre la mesa lo que el grafo permite ver y que ningún node declara todavía, para
que el Mago lo contraste con los hechos (ledger F-n) o lo marque como intuición.

Lee (sin escribir nada):
  research/grafo/grafo.json                 nodes, fuentes F-n (rigor), citas y wikilinks
  research/grafo/relaciones/triples.jsonl   relaciones semánticas s-p-o por fuente
  research/grafo/relaciones/entidades.json  nombres legibles de las entidades

Cuatro bandejas:
  1. PUENTES     pares de nodes que se apoyan en las mismas fuentes y no se enlazan entre sí
  2. ENTIDADES   conceptos que aparecen en fuentes de ≥2 nodes no enlazados
  3. TENSIONES   relaciones `contradice`/`refuta` y efectos opuestos (aumenta vs reduce)
                 sobre el mismo par de conceptos, según fuentes distintas
  4. CADENAS     A→B (fuente 1) + B→C (fuente 2): eslabón inferido, nunca afirmado por nadie

Uso:  python research/grafo/mago.py [--tema "palabras clave"] [--top 8] [--json]
Regenerar antes el grafo si cambiaron nodes o ledger: python research/grafo/build_grafo.py
"""
import argparse, itertools, json, unicodedata
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
REL = HERE / "relaciones"
PESO = {"A": 3.0, "B": 2.0, "C": 1.0, "D": 0.5, "E": 0.5}
EFECTO = {"aumenta": +1, "reduce": -1}
TENSION = {"contradice", "refuta"}
ENCADENA = {"aumenta", "reduce", "media", "modera", "asocia_con"}


def norm(s):
    s = unicodedata.normalize("NFD", str(s).lower())
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def cargar():
    g = json.loads((HERE / "grafo.json").read_text(encoding="utf-8"))
    nodes = {n["id"] for n in g["nodes"] if n["type"] == "node"}
    fuentes = {n["id"]: n for n in g["nodes"] if n["type"] == "fuente"}
    cita = defaultdict(set)      # F-n -> nodes que la citan
    enlace = set()               # pares de nodes con wikilink (sin dirección)
    for e in g["edges"]:
        if e["k"] == "cita" and e["s"] in nodes:
            cita[e["t"]].add(e["s"])
        elif e["k"] == "wikilink":
            enlace.add(frozenset((e["s"], e["t"])))
    triples = [json.loads(l) for l in (REL / "triples.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    ent = json.loads((REL / "entidades.json").read_text(encoding="utf-8"))
    return nodes, fuentes, cita, enlace, triples, ent


def rigor(fuentes, f):
    return fuentes.get(f, {}).get("rigor", "?")


def etiqueta(fuentes, fs):
    return ", ".join(f"{f}({rigor(fuentes, f)})" for f in sorted(fs, key=lambda x: int(x[2:])))


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--tema", default="", help="palabras clave para filtrar la mesa (sin tildes da igual)")
    ap.add_argument("--top", type=int, default=8)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    nodes, fuentes, cita, enlace, triples, ent = cargar()
    nombre = lambda i: ent.get(i, {}).get("nombre", i)
    claves = [t for t in norm(a.tema).split() if len(t) >= 4]

    def toca(*textos):
        if not claves:
            return True
        blob = norm(" ".join(textos))
        return any(k in blob for k in claves)

    def titulo(f):
        return fuentes.get(f, {}).get("titulo", "")

    # 1. PUENTES: nodes que comparten fuentes y no se enlazan
    comp = defaultdict(set)
    for f, ns in cita.items():
        for x, y in itertools.combinations(sorted(ns), 2):
            comp[(x, y)].add(f)
    puentes = []
    for (x, y), fs in comp.items():
        if frozenset((x, y)) in enlace or len(fs) < 2:
            continue
        if not toca(x, y, *(titulo(f) for f in fs)):
            continue
        puentes.append({"a": x, "b": y, "fuentes": sorted(fs), "peso": sum(PESO.get(rigor(fuentes, f), 0) for f in fs)})
    puentes.sort(key=lambda p: (-p["peso"], p["a"]))

    # 2. ENTIDADES puente: un concepto vive en fuentes de nodes que no se hablan
    ent_f = defaultdict(set)
    for t in triples:
        ent_f[t["s"]].add(t["f"]); ent_f[t["o"]].add(t["f"])
    entidades = []
    for e, fs in ent_f.items():
        ns = set().union(*(cita.get(f, set()) for f in fs))
        if len(ns) < 2:
            continue
        sueltos = [p for p in itertools.combinations(sorted(ns), 2) if frozenset(p) not in enlace]
        if not sueltos or not toca(nombre(e), *ns):
            continue
        entidades.append({"entidad": nombre(e), "nodes": sorted(ns), "pares_sin_enlace": len(sueltos),
                          "fuentes": sorted(fs, key=lambda x: int(x[2:]))})
    entidades.sort(key=lambda d: (-d["pares_sin_enlace"], -len(d["fuentes"])))

    # 3. TENSIONES: contradicciones declaradas + efectos opuestos entre fuentes distintas
    tensiones = []
    for t in triples:
        if t["p"] in TENSION and toca(nombre(t["s"]), nombre(t["o"]), t.get("apoyo", "")):
            tensiones.append({"tipo": t["p"], "s": nombre(t["s"]), "o": nombre(t["o"]), "fuentes": [t["f"]],
                              "lectura": t.get("lectura"), "apoyo": t.get("apoyo", "")[:220]})
    por_par = defaultdict(list)
    for t in triples:
        if t["p"] in EFECTO:
            por_par[(t["s"], t["o"])].append(t)
    for (s, o), ts in por_par.items():
        signos = {EFECTO[t["p"]] for t in ts}
        if signos == {1, -1} and len({t["f"] for t in ts}) > 1 and toca(nombre(s), nombre(o)):
            up = sorted({t["f"] for t in ts if t["p"] == "aumenta"}); dn = sorted({t["f"] for t in ts if t["p"] == "reduce"})
            tensiones.append({"tipo": "efecto_opuesto", "s": nombre(s), "o": nombre(o), "fuentes": up + dn,
                              "lectura": None, "apoyo": f"aumenta según {', '.join(up)}; reduce según {', '.join(dn)}"})
    tensiones.sort(key=lambda d: (d["tipo"] != "efecto_opuesto", -sum(PESO.get(rigor(fuentes, f), 0) for f in d["fuentes"])))

    # 4. CADENAS: A→B y B→C de fuentes distintas, sin que ninguna fuente diga A→C
    sale = defaultdict(list)
    directo = {(t["s"], t["o"]) for t in triples}
    for t in triples:
        if t["p"] in ENCADENA:
            sale[t["s"]].append(t)
    cadenas, vistos = [], set()
    for t1 in triples:
        if t1["p"] not in ENCADENA:
            continue
        for t2 in sale.get(t1["o"], []):
            if t2["f"] == t1["f"] or t2["o"] == t1["s"] or (t1["s"], t2["o"]) in directo:
                continue
            clave = (t1["s"], t1["o"], t2["o"])
            if clave in vistos or not toca(nombre(t1["s"]), nombre(t1["o"]), nombre(t2["o"])):
                continue
            vistos.add(clave)
            ns = cita.get(t1["f"], set()) | cita.get(t2["f"], set())
            peso = PESO.get(rigor(fuentes, t1["f"]), 0) + PESO.get(rigor(fuentes, t2["f"]), 0)
            cruza = len(cita.get(t1["f"], set()) ^ cita.get(t2["f"], set())) > 0
            debiles = (t1["p"] == "asocia_con") + (t2["p"] == "asocia_con")  # asociación pura: eslabón más flojo
            cadenas.append({"a": nombre(t1["s"]), "p1": t1["p"], "b": nombre(t1["o"]), "p2": t2["p"], "c": nombre(t2["o"]),
                            "fuentes": [t1["f"], t2["f"]], "cruza_nodes": cruza, "nodes": sorted(ns),
                            "peso": peso + (1 if cruza else 0) - 1.5 * debiles})
    cadenas.sort(key=lambda d: -d["peso"])

    mesa = {"tema": a.tema, "puentes": puentes[:a.top], "entidades": entidades[:a.top],
            "tensiones": tensiones[:a.top], "cadenas": cadenas[:a.top],
            "totales": {"puentes": len(puentes), "entidades": len(entidades), "tensiones": len(tensiones), "cadenas": len(cadenas)}}
    if a.json:
        print(json.dumps(mesa, ensure_ascii=False, indent=1)); return

    T = mesa["totales"]
    print(f"# La mesa del Mago{' — tema: ' + a.tema if a.tema else ''}\n")
    print("> Candidatos, no hallazgos. Cada uno debe pasar la prueba de realidad (ledger F-n) o declararse intuición.\n")
    print(f"## 1. Puentes no declarados ({T['puentes']}) — nodes que se apoyan en las mismas fuentes y no se enlazan")
    for p in mesa["puentes"]:
        print(f"- [[{p['a']}]] ⟷ [[{p['b']}]] · peso {p['peso']:.1f} · {etiqueta(fuentes, p['fuentes'])}")
    print(f"\n## 2. Entidades puente ({T['entidades']}) — un concepto que vive en nodes que no se hablan")
    for d in mesa["entidades"]:
        print(f"- **{d['entidad']}** · {', '.join(d['nodes'])} · {etiqueta(fuentes, d['fuentes'][:8])}")
    print(f"\n## 3. Tensiones ({T['tensiones']}) — donde las fuentes chocan")
    for d in mesa["tensiones"]:
        lect = f" · lectura={d['lectura']}" if d["lectura"] else ""
        print(f"- `{d['tipo']}` **{d['s']}** → **{d['o']}** · {etiqueta(fuentes, d['fuentes'])}{lect}\n  {d['apoyo']}")
    print(f"\n## 4. Cadenas inferidas ({T['cadenas']}) — eslabón que ninguna fuente afirma")
    for d in mesa["cadenas"]:
        x = " · cruza nodes" if d["cruza_nodes"] else ""
        print(f"- {d['a']} —{d['p1']}→ {d['b']} —{d['p2']}→ {d['c']} · {etiqueta(fuentes, d['fuentes'])}{x}")
    if not any(T.values()):
        print("\n_Mesa vacía para este tema: el cerebro no tiene material que conectar. Dilo así; no lo rellenes._")


if __name__ == "__main__":
    main()
