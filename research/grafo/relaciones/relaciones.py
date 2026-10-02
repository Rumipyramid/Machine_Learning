#!/usr/bin/env python3
"""Grafo semántico incremental del códice (solo stdlib).

  next [-n 5] [--mejorar]  siguiente lote sin procesar (prioriza cerebro de diseño); --mejorar = ya procesadas solo a nivel ficha
  add lote.json      valida y agrega un lote (entidades + relaciones con evidencia) y registra el barrido
  check              valida todo el almacén
  render             escribe RELACIONES.md, relaciones.json y relaciones.html

Reglas: vocabulario cerrado (vocabulario.json); toda relación lleva fuente F-n del ledger, un `apoyo`
(paráfrasis o cita ≤300 car.), el nivel de `lectura` y la `fuerza` de la afirmación. Nunca se marca
'procesada' una fuente sin al menos una relación o una nota explícita de por qué no aporta.
"""
import json, re, sys, datetime as dt
from collections import Counter, defaultdict
from pathlib import Path

H = Path(__file__).resolve().parent
RES = H.parent.parent
V = json.loads((H / "vocabulario.json").read_text())
F_TRI, F_ENT, F_EST = H / "triples.jsonl", H / "entidades.json", H / "estado.json"
RIG = {"🟢": "A", "🔵": "B", "🟡": "C", "🟠": "D", "🔴": "E"}


def ledger():
    sys.path.insert(0, str(H.parent))
    import build_grafo as bg
    rows, full = bg.parse_ledger((RES / "fuentes/codice.md").read_text()), {}
    for l in (RES / "fuentes/codice.md").read_text().splitlines():
        m = re.match(r"\| F-(\d+) \|", l)
        if m:
            full[int(m.group(1))] = l
    dn = (RES / "_nodes/tendencias-diseno-innovacion.md").read_text()
    return rows, full, bg.explicit_cites(dn)


def load():
    tri = [json.loads(l) for l in F_TRI.read_text().splitlines() if l] if F_TRI.exists() else []
    ent = json.loads(F_ENT.read_text()) if F_ENT.exists() else {}
    est = json.loads(F_EST.read_text()) if F_EST.exists() else {"barridos": [], "discrepancias": []}
    return tri, ent, est


def procesadas(est):
    return {int(f[2:]) for b in est["barridos"] for f in b["f_ids"]}


def cmd_next(n, mejorar=False):
    rows, full, dcit = ledger()
    tri, _, est = load()
    done = procesadas(est)
    if mejorar:  # fuentes cuyas relaciones son todas lectura=ficha: candidatas a lectura profunda
        lec = defaultdict(set)
        for t in tri: lec[t["f"]].add(t["lectura"])
        done = {int(f[2:]) for f, l in lec.items() if l != {"ficha"}} | (done - {int(f[2:]) for f in lec})
    order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
    pend = [f for f in rows if f not in done]
    pend.sort(key=lambda f: (f not in dcit, order.get(rows[f]["rigor"], 9), f))
    print(f"pendientes: {len(pend)} de {len(rows)} (procesadas {len(done)}). Orden: cerebro de diseño → rigor A→E → ID.\n")
    for f in pend[:n]:
        print(full[f][:1600], "\n")


def cmd_add(path):
    rows, _, _ = ledger()
    tri, ent, est = load()
    lote = json.loads(Path(path).read_text())
    errs = []
    nuevas = {e["id"]: e for e in lote.get("entidades", [])}
    for i, e in nuevas.items():
        if not re.fullmatch(r"[a-z0-9_]+", i): errs.append(f"id de entidad inválido: {i}")
        if e.get("tipo") not in V["tipos_entidad"]: errs.append(f"{i}: tipo '{e.get('tipo')}' fuera del vocabulario")
        if not e.get("nombre"): errs.append(f"{i}: sin nombre")
    known = set(ent) | set(nuevas)
    fids = {int(f[2:]) for f in lote["f_ids"]}
    seen = {(t["s"], t["p"], t["o"], t["f"]) for t in tri}
    out, covered = [], set()
    for t in lote.get("triples", []):
        k = (t["s"], t["p"], t["o"], t["f"])
        if t["p"] not in V["relaciones"]: errs.append(f"relación fuera del vocabulario: {t['p']}")
        for x in (t["s"], t["o"]):
            if x not in known: errs.append(f"entidad desconocida: {x}")
        if not re.fullmatch(r"F-\d+", t["f"]) or int(t["f"][2:]) not in rows: errs.append(f"fuente inexistente: {t['f']}")
        elif int(t["f"][2:]) not in fids: errs.append(f"{t['f']} no está en f_ids del lote")
        if not 10 <= len(t.get("apoyo", "")) <= 300: errs.append(f"apoyo vacío o >300 car. en {k}")
        if t.get("lectura") not in V["lectura"]: errs.append(f"lectura inválida en {k}")
        if t.get("fuerza") not in V["fuerza"]: errs.append(f"fuerza inválida en {k}")
        if k in seen: errs.append(f"duplicada: {k}")
        seen.add(k); covered.add(t["f"])
        out.append(t)
    sin_aporte = {n["f"] for n in lote.get("sin_aporte", [])}
    for f in lote["f_ids"]:
        if f not in covered and f not in sin_aporte:
            errs.append(f"{f} sin relaciones y sin nota en `sin_aporte`")
    if errs:
        print("LOTE RECHAZADO:\n- " + "\n- ".join(errs)); sys.exit(1)
    base = len(tri)
    with F_TRI.open("a") as fh:
        for i, t in enumerate(out, 1):
            t = {"id": f"T-{base+i}", **t, "fecha": lote["fecha"]}
            fh.write(json.dumps(t, ensure_ascii=False) + "\n")
    ent.update(nuevas)
    F_ENT.write_text(json.dumps(ent, ensure_ascii=False, indent=1, sort_keys=True))
    est["barridos"].append({"fecha": lote["fecha"], "f_ids": lote["f_ids"], "triples": len(out),
                            "sin_aporte": lote.get("sin_aporte", []), "notas": lote.get("notas", "")})
    est["discrepancias"] += [{"fecha": lote["fecha"], **d} for d in lote.get("discrepancias", [])]
    F_EST.write_text(json.dumps(est, ensure_ascii=False, indent=1))
    print(f"ok: +{len(out)} relaciones, +{len(nuevas)} entidades, {len(lote['f_ids'])} fuentes registradas")


def cmd_check():
    tri, ent, est = load()
    rows, _, _ = ledger()
    p = 0
    used = {x for t in tri for x in (t["s"], t["o"])}
    for t in tri:
        if t["p"] not in V["relaciones"] or t["s"] not in ent or t["o"] not in ent:
            print("✗", t["id"], "referencia inválida"); p += 1
    for e in set(ent) - used: print("⚠ entidad sin relaciones:", e); p += 1
    print("sin problemas" if not p else f"{p} problemas")


def clase(p): return V["relaciones"][p]["clase"]


def cmd_render():
    tri, ent, est = load()
    rows, _, dcit = ledger()
    done = procesadas(est)
    today = dt.date.today().isoformat()
    byent = defaultdict(set)
    for t in tri:
        byent[t["s"]].add(t["f"]); byent[t["o"]].add(t["f"])
    deg = Counter()
    for t in tri: deg[t["s"]] += 1; deg[t["o"]] += 1
    rig = Counter(rows[f]["rigor"] for f in done if f in rows)
    tot = Counter(r["rigor"] for r in rows.values())
    des_done = len(done & dcit)
    L = [f"# 🧬 Grafo semántico del códice — RELACIONES\n\n*Generado {today} por `relaciones.py render`. No editar a mano. "
         "Cada relación vive en `triples.jsonl` con fuente F-n, apoyo, nivel de lectura y fuerza.*\n",
         "> **Transparencia:** una relación aquí es lo que *una fuente dice*, no un hecho. `lectura=ficha` significa que solo se leyó "
         "el resumen del ledger; `abstract` que se leyó el resumen real de la fuente; `completa`, el texto íntegro. "
         "Un cruce entre fuentes es una *coincidencia de entidades*, no una prueba de que las fuentes sean compatibles.\n",
         "## 1. Cobertura\n", "| | |\n|---|---|",
         f"| Fuentes procesadas | **{len(done)} de {len(rows)}** ({100*len(done)/len(rows):.1f}%) |",
         f"| …del cerebro de diseño (citadas en el node) | {des_done} de {len(dcit & set(rows))} |",
         "| …por rigor | " + " · ".join(f"{k} {rig[k]}/{tot[k]}" for k in "ABCDE") + " |",
         f"| Barridos | {len(est['barridos'])} |", f"| Entidades | {len(ent)} |", f"| Relaciones | {len(tri)} |"]
    lec = Counter(t["lectura"] for t in tri); fz = Counter(t["fuerza"] for t in tri)
    L.append("| Nivel de lectura | " + " · ".join(f"{k} {v}" for k, v in lec.most_common()) + " |")
    L.append("| Fuerza de las afirmaciones | " + " · ".join(f"{k} {v}" for k, v in fz.most_common()) + " |\n")
    pr = Counter(t["p"] for t in tri)
    L += ["## 2. Relaciones por tipo\n", "| Relación | Clase | n |\n|---|---|---|"] + [f"| `{p}` | {clase(p)} | {n} |" for p, n in pr.most_common()]
    L += ["", "## 3. Convergencias: entidades sostenidas por ≥2 fuentes\n"]
    conv = sorted(((e, s) for e, s in byent.items() if len(s) >= 2), key=lambda x: -len(x[1]))
    L += ["| Entidad | Fuentes |\n|---|---|"] + [f"| {ent[e]['nombre']} | {', '.join(sorted(s, key=lambda x: int(x[2:])))} |" for e, s in conv] if conv else ["*(ninguna aún)*"]
    L += ["", "## 4. Tensiones declaradas (`contradice` / `refuta`)\n"]
    ten = [t for t in tri if t["p"] in ("contradice", "refuta")]
    L += [f"- **{ent[t['s']]['nombre']}** —{t['p']}→ **{ent[t['o']]['nombre']}** ({t['f']}, {t['fuerza']}): {t['apoyo']}" for t in ten] or ["*(ninguna aún)*"]
    L += ["", "## 5. Hubs (entidades más conectadas)\n", "| Entidad | Tipo | Grado | Fuentes |\n|---|---|---|---|"]
    L += [f"| {ent[e]['nombre']} | {ent[e]['tipo']} | {d} | {len(byent[e])} |" for e, d in deg.most_common(10)]
    L += ["", "## 6. Discrepancias halladas contra el ledger (para `cronista`; no se corrigen aquí)\n"]
    L += [f"- **{d['f']}** ({d['fecha']}): {d['detalle']}" for d in est["discrepancias"]] or ["*(ninguna)*"]
    L += ["", "## 7. Registro de barridos\n", "| Fecha | Fuentes | Relaciones | Sin aporte | Notas |\n|---|---|---|---|---|"]
    L += [f"| {b['fecha']} | {', '.join(b['f_ids'])} | {b['triples']} | {', '.join(x['f'] for x in b['sin_aporte']) or '–'} | {b['notas'][:200]} |" for b in est["barridos"]]
    L += ["", "---\n*Visor: `relaciones.html` · datos: `relaciones.json` · siguiente lote: `python research/grafo/relaciones/relaciones.py next`*"]
    (H / "RELACIONES.md").write_text("\n".join(L) + "\n")
    data = {"entidades": [{"id": k, **v, "grado": deg[k], "fuentes": sorted(byent[k])} for k, v in ent.items()],
            "relaciones": [{**t, "clase": clase(t["p"])} for t in tri], "generado": today,
            "cobertura": {"procesadas": len(done), "total": len(rows)}}
    (H / "relaciones.json").write_text(json.dumps(data, ensure_ascii=False, indent=1))
    (H / "relaciones.html").write_text((H / "relaciones.template.html").read_text().replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False)))
    print(f"ok: {len(done)} fuentes, {len(ent)} entidades, {len(tri)} relaciones")


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] not in ("next", "add", "check", "render"): print(__doc__); sys.exit(1)
    if a[0] == "next": cmd_next(int(a[a.index("-n") + 1]) if "-n" in a else 5, "--mejorar" in a)
    elif a[0] == "add": cmd_add(a[1])
    elif a[0] == "check": cmd_check()
    else: cmd_render()
