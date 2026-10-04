#!/usr/bin/env python3
"""Instrumento de impacto de Mu (solo stdlib). Escribe research/grafo/impacto.json, que lee el panel /mu (nivel N7).

Junta dos orígenes:
  1. La base del artefacto "Pregúntale a Mu" exportada con ArtifactData (`list` con `out_dir`):
     <dir>/consultas/<id>.json y <dir>/usos/<id>.json.
  2. research/grafo/impacto_manual.jsonl: decisiones fuera del artefacto (una por línea, JSON con
     fecha, decision, donde, node, fuentes, evidencia).

Uso: python research/grafo/impacto.py [--db DIR]
Sin --db conserva la última foto de la base guardada en impacto.json y solo recalcula lo manual.
No guarda ids de personas en el repo: solo las cuenta.
"""
import json, sys, datetime as dt
from collections import Counter
from pathlib import Path

H = Path(__file__).resolve().parent
OUT = H / "impacto.json"
MAN = H / "impacto_manual.jsonl"


def docs(d):
    out = []
    for p in sorted(d.glob("*.json")) if d.exists() else []:
        j = json.loads(p.read_text(encoding="utf-8"))
        out.append(j.get("data", j) if isinstance(j, dict) else j)
    return out


prev = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
base = prev.get("base", {})
if "--db" in sys.argv:
    d = Path(sys.argv[sys.argv.index("--db") + 1])
    cons, usos = docs(d / "consultas"), docs(d / "usos")
    val = Counter(u.get("valor") for u in usos)
    base = {
        "foto": dt.date.today().isoformat(),
        "consultas": len(cons),
        "personas": len({c.get("quien") for c in cons if c.get("quien")}),
        "dias_activos": len({str(c.get("at", ""))[:10] for c in cons if c.get("at")}),
        "valoradas": len(usos),
        "decision": val["decision"], "util": val["util"], "no_util": val["no_util"],
        "nodes_consultados": dict(Counter(c.get("node") or "(ninguno)" for c in cons).most_common()),
        "decisiones": [{"fecha": str(u.get("at", ""))[:10], "decision": u.get("decision", ""), "donde": u.get("donde", ""),
                        "node": u.get("node", ""), "fuentes": u.get("fuentes", []), "origen": "artefacto"}
                       for u in sorted(usos, key=lambda u: str(u.get("at", ""))) if u.get("valor") == "decision"],
    }

man = [json.loads(l) for l in MAN.read_text(encoding="utf-8").splitlines() if l.strip()] if MAN.exists() else []
decs = base.get("decisiones", []) + [{**m, "origen": "manual"} for m in man]
valoradas = base.get("valoradas", 0)
utiles = base.get("decision", 0) + base.get("util", 0)
res = {
    "_nota": "Generado por impacto.py. Decisiones autodeclaradas: prueban uso, no que la decisión fuera buena.",
    "generado": dt.date.today().isoformat(),
    "base": base,
    "manuales": len(man),
    "metricas": {
        "consultas_reales": base.get("consultas", 0),
        "personas": base.get("personas", 0),
        "valoradas": valoradas,
        "util_pct": round(100 * utiles / valoradas) if valoradas else 0,
        "decisiones": len(decs),
    },
    "decisiones": decs,
}
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
m = res["metricas"]
print(f"impacto: {m['consultas_reales']} consultas · {m['personas']} personas · {m['valoradas']} valoradas · "
      f"{m['util_pct']}% útiles · {m['decisiones']} decisiones ({len(man)} manuales) · foto de la base: {base.get('foto', 'nunca')}")
