#!/usr/bin/env python3
"""Examen fijo de calidad de Mu.

Dos pasos, para medir si un cambio mejora o empeora las respuestas:

  1. recuperar  — corre la página real de "Pregúntale a Mu" sin conexión (recuperar.cjs) y mide si para cada
                  pregunta recupera el nodo esperado y alguna de sus fuentes clave. Guarda el prompt exacto
                  que Mu enviaría a Claude en examen/prompts/Qnn.txt (no se versiona).
  2. calificar  — recibe las respuestas (JSON {"Q01": "texto", …}, producidas por Claude con esos prompts) y
                  califica cada una: ideas obligatorias presentes, afirmaciones prohibidas, códigos F-n
                  inventados, fuentes clave citadas y nivel de respaldo de la balanza del Criterio.

Uso:
  python research/grafo/examen/examen.py recuperar
  python research/grafo/examen/examen.py calificar --respuestas respuestas.json [--etiqueta texto]

Cada corrida agrega una línea a examen/historial.jsonl y reescribe examen/RESULTADOS.md. Solo stdlib + node.
"""
import argparse, datetime as dt, json, re, subprocess, sys, unicodedata
from pathlib import Path

H = Path(__file__).resolve().parent
GRAFO = H.parent
PREG = H / "preguntas.json"
HIST = H / "historial.jsonl"
NIVELES = {"firme": 3, "parcial": 2, "solo_heuristica": 1, "sin_base": 0}


def norm(s):
    s = unicodedata.normalize("NFD", s.lower())
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def cargar():
    return json.loads(PREG.read_text(encoding="utf-8"))["preguntas"]


def node_bin():
    for b in ("node", "/opt/node22/bin/node"):
        try:
            subprocess.run([b, "--version"], capture_output=True, check=True)
            return b
        except Exception:
            pass
    sys.exit("no se encontró node")


def recuperar(a):
    qs = cargar()
    out = H / "prompts" / "recuperacion.json"
    out.parent.mkdir(exist_ok=True)
    subprocess.run([node_bin(), str(H / "recuperar.cjs"), str(PREG), str(out)], check=True)
    res = {r["id"]: r for r in json.loads(out.read_text())["resultados"]}
    filas, ok_n, ok_f, tot_f = [], 0, 0, 0
    for q in qs:
        r = res.get(q["id"], {})
        (H / "prompts" / f"{q['id']}.txt").write_text(r.get("prompt", ""), encoding="utf-8")
        aceptables = q["nodo"] if isinstance(q["nodo"], list) else [q["nodo"]]
        nodo_ok = q["nodo"] is None or any(n in r.get("nodos", []) for n in aceptables)
        fu = set(q["fuentes"])
        f_ok = (not fu) or bool(fu & set(r.get("fuentes", [])))
        ok_n += nodo_ok
        if fu:
            tot_f += 1
            ok_f += f_ok
        filas.append({"id": q["id"], "nodo_ok": nodo_ok, "fuentes_ok": f_ok if fu else None,
                      "nodos": r.get("nodos", [])[:3], "fuentes_clave_recuperadas": sorted(fu & set(r.get("fuentes", [])))})
    resumen = {"nodo_correcto_pct": round(100 * ok_n / len(qs)), "fuente_clave_pct": round(100 * ok_f / tot_f) if tot_f else None}
    registrar("recuperacion", a.etiqueta, resumen, filas)
    print(json.dumps(resumen, ensure_ascii=False))
    for f in filas:
        if not f["nodo_ok"] or f["fuentes_ok"] is False:
            print(" ✗", f["id"], "nodos:", ", ".join(f["nodos"]), "· fuentes clave:", f["fuentes_clave_recuperadas"] or "ninguna")


def criterio(q, texto):
    tmp = H / "prompts" / "_resp.txt"
    tmp.parent.mkdir(exist_ok=True)
    tmp.write_text(texto, encoding="utf-8")
    p = subprocess.run([sys.executable, str(GRAFO / "criterio.py"), "--pregunta", q, "--respuesta", str(tmp), "--json"],
                       capture_output=True, text=True)
    try:
        return json.loads(p.stdout)
    except Exception:
        return {}


def calificar(a):
    qs = cargar()
    resp = json.loads(Path(a.respuestas).read_text(encoding="utf-8"))
    filas = []
    for q in qs:
        t = resp.get(q["id"])
        if t is None:
            filas.append({"id": q["id"], "falta": True})
            continue
        n = norm(t)
        debe = [bool(re.search(norm(x), n)) for x in q["debe"]]
        prohibidas = [x for x in q["no_debe"] if re.search(norm(x), n)]
        c = criterio(q["pregunta"], t)
        cit = c.get("citadas", {})
        inv = cit.get("inventadas", [])
        val = set(cit.get("validas", []))
        clave = sorted(set(q["fuentes"]) & val)
        ideas = sum(debe) / len(debe) if debe else 1
        # Puntaje 0-100: ideas 50 · sin prohibidas 20 · sin inventadas 15 · fuente clave citada 15
        pts = 50 * ideas + (20 if not prohibidas else 0) + (15 if not inv else 0) + \
            (15 if (clave or not q["fuentes"]) else 0)
        filas.append({"id": q["id"], "puntaje": round(pts), "ideas": f"{sum(debe)}/{len(debe)}",
                      "ideas_faltantes": [x for x, ok in zip(q["debe"], debe) if not ok], "prohibidas": prohibidas,
                      "inventadas": inv, "fuentes_clave_citadas": clave, "respaldo": c.get("nivel", "?"),
                      "relevancia": c.get("relevancia", {}).get("global", "?")})
    hechas = [f for f in filas if not f.get("falta")]
    resumen = {"preguntas": len(hechas), "puntaje_medio": round(sum(f["puntaje"] for f in hechas) / len(hechas)) if hechas else 0,
               "con_inventadas": sum(1 for f in hechas if f["inventadas"]),
               "con_prohibidas": sum(1 for f in hechas if f["prohibidas"]),
               "respaldo_firme": sum(1 for f in hechas if f["respaldo"] == "firme")}
    registrar("respuestas", a.etiqueta, resumen, filas)
    print(json.dumps(resumen, ensure_ascii=False))
    for f in hechas:
        if f["puntaje"] < 70:
            print(f" ✗ {f['id']} {f['puntaje']} · faltan: {f['ideas_faltantes']} · prohibidas: {f['prohibidas']} · inventadas: {f['inventadas']}")


def registrar(tipo, etiqueta, resumen, filas):
    reg = {"fecha": dt.date.today().isoformat(), "tipo": tipo, "etiqueta": etiqueta or "", "resumen": resumen, "detalle": filas}
    with HIST.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(reg, ensure_ascii=False) + "\n")
    informe()


def informe():
    regs = [json.loads(l) for l in HIST.read_text(encoding="utf-8").splitlines() if l] if HIST.exists() else []
    L = ["# Examen de calidad de Mu — resultados", "",
         "> Generado por `research/grafo/examen/examen.py` (no editar a mano). Preguntas en `preguntas.json`.",
         "> Recuperación = si Mu encuentra el nodo y las fuentes correctas. Respuestas = si lo que responde contiene las ideas",
         "> clave, evita afirmaciones prohibidas, no inventa códigos de fuente y cita fuentes clave (0-100).",
         "", "## Historial", "", "| Fecha | Tipo | Etiqueta | Resultado |", "|---|---|---|---|"]
    for r in regs:
        s = r["resumen"]
        txt = (f"nodo correcto {s['nodo_correcto_pct']}% · fuente clave {s['fuente_clave_pct']}%" if r["tipo"] == "recuperacion"
               else f"puntaje medio {s['puntaje_medio']} · {s['con_inventadas']} con fuentes inventadas · "
                    f"{s['con_prohibidas']} con afirmaciones prohibidas · {s['respaldo_firme']} con respaldo firme")
        L.append(f"| {r['fecha']} | {r['tipo']} | {r['etiqueta']} | {txt} |")
    for tipo in ("recuperacion", "respuestas"):
        ult = next((r for r in reversed(regs) if r["tipo"] == tipo), None)
        if not ult:
            continue
        L += ["", f"## Última corrida de {tipo} ({ult['fecha']})", ""]
        if tipo == "recuperacion":
            L += ["| Pregunta | Nodo correcto | Fuente clave | Nodos recuperados |", "|---|---|---|---|"]
            for f in ult["detalle"]:
                fk = "—" if f["fuentes_ok"] is None else ("sí" if f["fuentes_ok"] else "no")
                L.append(f"| {f['id']} | {'sí' if f['nodo_ok'] else 'no'} | {fk} | {', '.join(f['nodos'])} |")
        else:
            L += ["| Pregunta | Puntaje | Ideas | Respaldo | Problemas |", "|---|---|---|---|---|"]
            for f in ult["detalle"]:
                if f.get("falta"):
                    L.append(f"| {f['id']} | — | — | — | sin respuesta |")
                    continue
                prob = "; ".join(x for x in (
                    ("faltan: " + ", ".join(f["ideas_faltantes"])) if f["ideas_faltantes"] else "",
                    ("prohibidas: " + ", ".join(f["prohibidas"])) if f["prohibidas"] else "",
                    ("inventadas: " + ", ".join(f["inventadas"])) if f["inventadas"] else "") if x) or "—"
                L.append(f"| {f['id']} | {f['puntaje']} | {f['ideas']} | {f['respaldo']} | {prob.replace('|', '/')} |")
    (H / "RESULTADOS.md").write_text("\n".join(L) + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("recuperar"); r.add_argument("--etiqueta")
    c = sub.add_parser("calificar"); c.add_argument("--respuestas", required=True); c.add_argument("--etiqueta")
    a = ap.parse_args()
    recuperar(a) if a.cmd == "recuperar" else calificar(a)


if __name__ == "__main__":
    main()
