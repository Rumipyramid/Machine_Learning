"""Genera mu-corpus.json para la página "Pregúntale a Mu" (research/grafo/preguntar/index.html).

Solo stdlib. Parte los nodes de research/_nodes/ por secciones (## / ###) en fragmentos de hasta ~1.800
caracteres, toma cada fila del ledger (research/fuentes/codice.md) como una ficha F-n, y agrega el estado del
panel (salida de research/grafo/mu.py). La página busca en estos fragmentos y se los pasa a Claude.

Uso: python research/grafo/preguntar/build_corpus.py
"""
import json, re, subprocess, sys, datetime as dt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
NODES = ROOT / "research" / "_nodes"
LEDGER = ROOT / "research" / "fuentes" / "codice.md"
OUT = Path(__file__).resolve().parent / "mu-corpus.json"
MAX = 1800


def node_title(text, stem):
    m = re.search(r"^# (.+)$", text, re.M)
    return m.group(1).strip() if m else stem


def split_node(stem, text):
    title = node_title(text, stem)
    parts, head, buf = [], title, []
    for line in text.splitlines():
        m = re.match(r"^(#{2,3}) (.+)$", line)
        if m:
            if buf:
                parts.append((head, "\n".join(buf).strip()))
            head, buf = m.group(2).strip(), []
        else:
            buf.append(line)
    if buf:
        parts.append((head, "\n".join(buf).strip()))
    chunks = []
    for head, body in parts:
        if not body:
            continue
        while body:
            if len(body) <= MAX:
                piece, body = body, ""
            else:
                cut = body.rfind("\n", 0, MAX)
                cut = cut if cut > MAX // 2 else MAX
                piece, body = body[:cut], body[cut:].lstrip()
            chunks.append({"k": "node", "node": stem, "titulo": title, "seccion": head, "texto": piece})
    return chunks


def ledger_rows():
    rows = []
    for line in LEDGER.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| F-"):
            continue
        c = [x.strip() for x in line.strip().strip("|").split(" | ")]
        if len(c) < 9:
            continue
        rows.append({"k": "fuente", "id": c[0], "autor": c[1], "anio": c[2], "titulo": c[3], "rigor": c[4],
                     "resumen": c[5], "uso": c[6], "url": c[7], "registrado": c[8]})
    return rows


def estado():
    try:
        out = subprocess.run([sys.executable, str(ROOT / "research" / "grafo" / "mu.py")], capture_output=True,
                             text=True, cwd=ROOT, timeout=120).stdout
    except Exception:
        return {}
    lines = [l for l in out.splitlines() if l and not l.startswith("panel:")]
    return {"lineas": lines}


def main():
    chunks = []
    for p in sorted(NODES.glob("*.md")):
        chunks += split_node(p.stem, p.read_text(encoding="utf-8"))
    fuentes = ledger_rows()
    data = {"generado": dt.date.today().isoformat(), "estado": estado(), "nodes": chunks, "fuentes": fuentes}
    OUT.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"ok: {len(chunks)} fragmentos de {len(list(NODES.glob('*.md')))} nodes, {len(fuentes)} fuentes, "
          f"{OUT.stat().st_size // 1024} KB → {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
