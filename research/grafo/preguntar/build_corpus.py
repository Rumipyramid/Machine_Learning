"""Genera mu-corpus.json para la página "Pregúntale a Mu" (research/grafo/preguntar/index.html).

Solo stdlib. Parte los nodes de research/_nodes/ por secciones (## / ###) en fragmentos de hasta ~1.800
caracteres, toma cada fila del ledger (research/fuentes/codice.md) como una ficha F-n anotada con rigor, año y
lectura en el grafo, y agrega contradicciones del grafo con su estado, los tableros de hipótesis, los umbrales del
Chacal (chacal_rubrica.json) y el estado del panel (salida de research/grafo/mu.py). La página busca en estos fragmentos y se los pasa a Claude.

Uso: python research/grafo/preguntar/build_corpus.py
"""
import json, re, subprocess, sys, datetime as dt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REL = ROOT / "research" / "grafo" / "relaciones"
RUBRICA = ROOT / "research" / "grafo" / "chacal_rubrica.json"
# Mismo criterio que research/grafo/chacal.py: estos estados de resolución NO cuentan como resueltos
ABIERTAS = {"en_disputa", "sin_verificar", "mecanismo_en_disputa"}
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


def year(s):
    ys = [int(y) for y in re.findall(r"(?<!\d)(19\d\d|20\d\d)(?!\d)", s or "")]
    return max(ys) if ys else None


def rigor(s):
    m = re.search(r"\b([A-E])\b", s or "")
    return m.group(1) if m else "?"


def grafo(fuentes):
    """Anota cada ficha con lo que el grafo sabe de ella y devuelve contradicciones y discrepancias."""
    tri = [json.loads(l) for l in (REL / "triples.jsonl").read_text(encoding="utf-8").splitlines() if l]
    ent = json.loads((REL / "entidades.json").read_text(encoding="utf-8"))
    est = json.loads((REL / "estado.json").read_text(encoding="utf-8"))
    sem = {f for b in est["barridos"] for f in b["f_ids"]}
    lec = {}
    for t in tri:
        lec.setdefault(t["f"], set()).add(t["lectura"])
    res = {r["triple"]: r for r in est.get("resoluciones", [])}
    nombre = lambda i: ent.get(i, {}).get("nombre", i)
    tens = []
    for t in tri:
        if t["p"] not in ("contradice", "refuta"):
            continue
        r = res.get(t["id"], {})
        e = r.get("estado", "sin_resolver")
        tens.append({"id": t["id"], "f": t["f"], "s": nombre(t["s"]), "p": t["p"], "o": nombre(t["o"]),
                     "apoyo": t["apoyo"], "estado": e, "nota": r.get("nota", ""),
                     "abierta": e == "sin_resolver" or e in ABIERTAS})
    for f in fuentes:
        f["rig"] = rigor(f["rigor"])
        f["y"] = year(f["anio"])
        f["sem"] = f["id"] in sem
        f["deep"] = bool(lec.get(f["id"], {"ficha"}) - {"ficha"})
    disc = [{"f": d["f"], "detalle": d["detalle"]} for d in est["discrepancias"] if d.get("estado") != "cerrada"]
    return tens, disc


def hipotesis():
    """Filas de los tableros de hipótesis (H del node de diseño, HC del node de conducta humano-IA)."""
    out = []
    for stem in ("tendencias-diseno-innovacion", "conducta-humano-ia"):
        text = (NODES / f"{stem}.md").read_text(encoding="utf-8")
        for l in text.splitlines():
            m = re.match(r"\|\s*\*\*(HC?\d+)\*\*\s*\|(.*?)\|(.*?)\|(.*?)\|", l)
            if not m:
                continue
            st = m.group(3)
            pos = {k: st[:140].find(k) for k in ("refutada", "respaldada", "parcial", "abierta") if k in st[:140]}
            out.append({"id": m.group(1), "node": stem, "texto": re.sub(r"\*\*", "", m.group(2)).strip(),
                        "estado": min(pos, key=pos.get) if pos else "otra",
                        "detalle": re.sub(r"\*\*", "", st).strip()[:900],
                        "prueba": re.sub(r"\*\*", "", m.group(4)).strip()[:300]})
    return out


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
    tens, disc = grafo(fuentes)
    rub = json.loads(RUBRICA.read_text(encoding="utf-8"))["dimensiones"]
    data = {"generado": dt.date.today().isoformat(), "estado": estado(), "nodes": chunks, "fuentes": fuentes,
            "tensiones": tens, "discrepancias": disc, "hipotesis": hipotesis(),
            "rubrica": {k: {"def": v["def"], "verde": v["verde"], "amarillo": v["amarillo"]} for k, v in rub.items()}}
    OUT.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"ok: {len(chunks)} fragmentos de {len(list(NODES.glob('*.md')))} nodes, {len(fuentes)} fuentes, "
          f"{len(tens)} contradicciones ({sum(t['abierta'] for t in tens)} abiertas), {len(data['hipotesis'])} hipótesis, "
          f"{OUT.stat().st_size // 1024} KB → {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
