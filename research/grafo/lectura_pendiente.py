#!/usr/bin/env python3
"""Lista priorizada de fuentes que conviene leer en texto completo.

Prioriza las fuentes que sostienen reglas e hipótesis y que el cerebro solo conoce
por su ficha, por un resumen o por terceros. Solo stdlib; solo lee.

Uso: python research/grafo/lectura_pendiente.py [--top 40]
Salida: research/fuentes/lectura_pendiente.md
"""
import argparse, json, re, sys
from collections import Counter
from pathlib import Path

H = Path(__file__).resolve().parent
RES = H.parent
sys.path.insert(0, str(H))
import build_grafo as bg  # noqa: E402

NIVEL = {"ficha": 0, "abstract": 1, "completa": 2}
TXT = {0: "solo ficha", 1: "resumen oficial", 2: "texto completo"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=40)
    a = ap.parse_args()
    ledger = bg.parse_ledger((RES / "fuentes/codice.md").read_text(encoding="utf-8"))
    raw = {}
    for l in (RES / "fuentes/codice.md").read_text(encoding="utf-8").splitlines():
        m = re.match(r"\| F-(\d+) \|", l)
        if m:
            raw[int(m.group(1))] = l
    nodes = {p.stem: p.read_text(encoding="utf-8") for p in (RES / "_nodes").glob("*.md")}
    cnt = Counter(f for t in nodes.values() for f in bg.explicit_cites(t))
    # citas dentro de filas de hipótesis (| **H1** |…) y de reglas (párrafos de §7 del nodo de diseño)
    hyp = Counter()
    for t in nodes.values():
        for l in t.splitlines():
            if re.match(r"\|\s*\*\*(?:HC?|PE|PF|CQ)\d+\*\*", l):
                hyp.update(bg.explicit_cites(l))
    d = nodes.get(bg.DESIGN, "")
    m = re.search(r"^## 7\..*?(?=^## 8\.)", d, re.S | re.M)
    reg = Counter(bg.explicit_cites(m.group(0))) if m else Counter()
    best = {}
    for l in (H / "relaciones/triples.jsonl").read_text().splitlines():
        if l:
            t = json.loads(l)
            k = int(t["f"][2:]); best[k] = max(best.get(k, 0), NIVEL.get(t["lectura"], 0))
    filas = []
    for f, r in ledger.items():
        b = best.get(f, 0)
        if b == 2:
            continue
        linea = raw.get(f, "")
        dudas = []
        if "no verificad" in linea:
            dudas.append("datos no verificados")
        if re.search(r"fuentes? secundaria|vía [A-Z]|resumen de la BPS", linea):
            dudas.append("leída por terceros")
        peso = 3 * reg[f] + 2 * hyp[f] + min(cnt[f], 5) + (2 if r["rigor"] in "AB" else 0) + (2 - b) + 2 * len(dudas)
        if reg[f] or hyp[f] or dudas:
            filas.append((peso, f, r, b, dudas))
    filas.sort(key=lambda x: (-x[0], x[1]))
    out = ["# Lectura pendiente en texto completo",
           "",
           "> Generado por `research/grafo/lectura_pendiente.py` (determinista; no editar a mano).",
           "> Fuentes que sostienen reglas o hipótesis del cerebro, o cuyos datos no se pudieron verificar, y que hasta hoy",
           "> solo se conocen por su ficha, por un resumen o por terceros. Leerlas completas es lo que más sube la solidez de Mu.",
           "",
           "**Cómo resolverlas:** (1) habilitar en la red del entorno los dominios de las editoriales (ver `research/fuentes/textos/README.md`),",
           "o (2) dejar el PDF o el texto en `research/fuentes/textos/F-n.pdf` (o `.txt`). En la siguiente sesión se lee, se corrige",
           "la ficha si hace falta (con autorización si cambia una cifra) y sus relaciones del grafo pasan a `lectura: completa`.",
           "",
           f"Total candidatas: {len(filas)} · se muestran {min(a.top, len(filas))}.",
           "",
           "| Prioridad | Fuente | Rigor | Hoy se conoce por | Sostiene | Dudas | Enlace |",
           "|---|---|---|---|---|---|---|"]
    for peso, f, r, b, dudas in filas[: a.top]:
        sost = ", ".join(x for x in (f"{reg[f]} regla(s)" if reg[f] else "", f"{hyp[f]} hipótesis" if hyp[f] else "",
                                     f"{cnt[f]} nodo(s)") if x)
        tit = f"{r.get('autor', '')[:40]} ({r.get('anio', '')})"
        cols = [x.strip() for x in raw.get(f, "").split("|")]
        url = cols[8] if len(cols) > 8 else ""
        out.append(f"| {peso} | F-{f} — {tit} | {r['rigor']} | {TXT[b]} | {sost} | {'; '.join(dudas) or '—'} | {url} |")
    (RES / "fuentes/lectura_pendiente.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"ok: {len(filas)} candidatas → research/fuentes/lectura_pendiente.md")


if __name__ == "__main__":
    main()
