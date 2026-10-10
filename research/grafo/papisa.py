#!/usr/bin/env python3
"""El libro y el velo de la Papisa: lo que el cerebro sabe y una respuesta calló (solo stdlib).

Herramienta determinista de la mente "La Papisa" (`.claude/skills/mentes/`). No interpreta: dada una pregunta (y
las fuentes que citó la respuesta ya dada), separa lo que el cerebro tiene y no se usó de lo que el cerebro no sabe.

  1. EL LIBRO   fuentes relevantes del ledger que la respuesta NO citó (rigor A-B primero)
  2. LO VIVO    hipótesis de los tableros sobre el tema que siguen abiertas o parciales
  3. EL VELO    contradicciones abiertas del grafo · fuentes relevantes leídas solo en resumen o no procesadas
                en el grafo semántico · temas del backlog de Mu sin cobertura

Uso:  python research/grafo/papisa.py --tema "palabras clave" [--cito F-16,F-244] [--top 8] [--json]
Lee research/fuentes/codice.md, research/_nodes/, research/grafo/relaciones/ y research/garaje/backlog_temas.md.
"""
import argparse, json, re, sys, unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "preguntar"))
import build_corpus as bc  # noqa: E402  (reutiliza los parsers del índice de "Pregúntale a Mu")

BACKLOG = HERE.parent / "garaje" / "backlog_temas.md"
VACIAS = set("para por con sin una uno unos unas los las del que como cual cuando donde este esta estos estas ese esa eso hay muy mas pero porque sobre entre desde hasta tiene tienen son fue han hoy todo toda todos todas cada sus nos les the and for with from that this".split())
ORDEN = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}


def norm(s):
    s = unicodedata.normalize("NFD", str(s).lower())
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


CORTAS = {"ia", "ai", "ux", "ubi", "sbs", "pbi", "llm", "nse"}


def raices(s):
    return {t[:6] for t in re.split(r"[^a-z0-9ñ]+", norm(s)) if (len(t) > 3 and t not in VACIAS) or t in CORTAS}


def puntaje(claves, *textos):
    """0 si el texto no cubre al menos la mitad de las claves (mínimo 2); si las cubre, claves halladas + bono por título."""
    if not claves:
        return 0
    hall = claves & raices(" ".join(textos))
    if len(hall) < min(2, len(claves)) or len(hall) < len(claves) / 2:
        return 0
    return len(hall) + 0.5 * len(claves & raices(textos[0]))


def libro(tema, cito=(), top=8):
    claves = raices(tema)
    fuentes = bc.ledger_rows()
    tens, _ = bc.grafo(fuentes)
    cito = set(cito)
    rel = []
    for f in fuentes:
        p = puntaje(claves, f["titulo"], f["resumen"])
        if p > 0:
            rel.append((p, f))
    rel.sort(key=lambda x: (-x[0], ORDEN.get(x[1]["rig"], 9), -(x[1]["y"] or 0)))
    no_citadas = [f for _, f in rel if f["id"] not in cito]
    fuertes = [f for f in no_citadas if f["rig"] in ("A", "B")]
    ficha = lambda f: {"id": f["id"], "rigor": f["rig"], "anio": f["anio"], "autor": f["autor"][:60],
                       "titulo": f["titulo"][:140], "lectura": "a fondo" if f["deep"] else "solo resumen" if f["sem"] else "fuera del grafo"}

    hips = [h for h in bc.hipotesis() if h["estado"] in ("abierta", "parcial", "otra")
            and puntaje(claves, h["texto"], h["detalle"]) > 0]
    hips.sort(key=lambda h: -puntaje(claves, h["texto"], h["detalle"]))

    abiertas = [t for t in tens if t["abierta"] and puntaje(claves, t["s"] + " " + t["o"], t["apoyo"]) > 0]
    veladas = [f for _, f in rel if not f["deep"]]

    backlog = []
    if BACKLOG.exists():
        for l in BACKLOG.read_text(encoding="utf-8").splitlines():
            c = [x.strip() for x in l.strip().strip("|").split("|")]
            if len(c) == 6 and c[1].isdigit() and (int(c[2]) > 0 or int(c[3]) > 0):
                backlog.append({"tema": c[0], "consultas": int(c[1]), "sin": int(c[2]), "parcial": int(c[3]),
                                "toca": bool(claves & raices(c[0]))})
    backlog.sort(key=lambda b: (not b["toca"], -b["sin"], -b["parcial"]))

    return {"tema": tema, "citadas": sorted(cito),
            "libro": [ficha(f) for f in (fuertes or no_citadas)[:top]],
            "vivo": [{"id": h["id"], "estado": h["estado"], "texto": h["texto"][:220], "prueba": h["prueba"][:200]} for h in hips[:top]],
            "velo": {"disputas": [{"f": t["f"], "s": t["s"], "p": t["p"], "o": t["o"], "estado": t["estado"],
                                   "nota": (t["nota"] or t["apoyo"])[:220]} for t in abiertas[:top]],
                     "a_medias": [ficha(f) for f in veladas[:top]],
                     "backlog": backlog[:top]},
            "totales": {"relevantes": len(rel), "no_citadas": len(no_citadas), "no_citadas_AB": len(fuertes),
                        "hipotesis_vivas": len(hips), "disputas": len(abiertas), "a_medias": len(veladas)}}


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--tema", required=True, help="palabras clave de la pregunta")
    ap.add_argument("--cito", default="", help="fuentes que la respuesta ya citó, p. ej. F-16,F-244")
    ap.add_argument("--top", type=int, default=8)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    cito = re.findall(r"F-\d+", a.cito.upper())
    L = libro(a.tema, cito, a.top)
    if a.json:
        print(json.dumps(L, ensure_ascii=False, indent=1)); return
    T = L["totales"]
    print(f"# El libro y el velo de la Papisa — tema: {a.tema}\n")
    print(f"> {T['relevantes']} fuentes del ledger tocan el tema; la respuesta citó {len(cito)}. Candidatos, no juicios.\n")
    print(f"## 1. El libro — lo que el cerebro sabe y no se usó ({T['no_citadas']} no citadas, {T['no_citadas_AB']} de rigor A-B)")
    for f in L["libro"]:
        print(f"- {f['id']} ({f['rigor']}, {f['anio']}) {f['autor']} — {f['titulo']} · lectura: {f['lectura']}")
    print(f"\n## 2. Lo vivo — hipótesis abiertas o parciales ({T['hipotesis_vivas']})")
    for h in L["vivo"]:
        print(f"- {h['id']} [{h['estado']}] {h['texto']}" + (f"\n  prueba pendiente: {h['prueba']}" if h["prueba"] else ""))
    print(f"\n## 3. El velo — lo que el cerebro no sabe todavía")
    print(f"### Disputas abiertas en el grafo ({T['disputas']})")
    for t in L["velo"]["disputas"]:
        print(f"- {t['f']}: \"{t['s']}\" {t['p']} \"{t['o']}\" — {t['estado']}. {t['nota']}")
    print(f"### Fuentes relevantes leídas solo en resumen o fuera del grafo ({T['a_medias']})")
    for f in L["velo"]["a_medias"]:
        print(f"- {f['id']} ({f['rigor']}) {f['titulo']} · {f['lectura']}")
    print("### Backlog de Mu con huecos (✗ sin cobertura · ~ parcial)")
    for b in L["velo"]["backlog"]:
        print(f"- {b['tema']} · ✗ {b['sin']} · ~ {b['parcial']}{' · toca este tema' if b['toca'] else ''}")
    if not T["relevantes"]:
        print("\n_El libro está en blanco para este tema: el cerebro no lo tiene. Ese silencio es la lectura._")


if __name__ == "__main__":
    main()
