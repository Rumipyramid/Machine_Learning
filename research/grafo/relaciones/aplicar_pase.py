#!/usr/bin/env python3
"""Aplica un pase de lectura profunda (pase_NNN.json) en su sitio sobre triples.jsonl.

Cada relación confirmada contra el resumen oficial pasa de lectura 'ficha' a 'abstract' con el apoyo reescrito.
Las contradichas no se tocan: se registran como discrepancias abiertas en estado.json para revisión humana
(corregir el ledger requiere autorización del usuario). Solo stdlib.

Uso: python research/grafo/relaciones/aplicar_pase.py pase_NNN.json [--dry]
"""
import json, sys
from pathlib import Path

H = Path(__file__).resolve().parent
F_TRI, F_EST = H / "triples.jsonl", H / "estado.json"


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    dry = "--dry" in args
    p = Path(args[0]) if Path(args[0]).is_absolute() else H / args[0]
    pase = json.loads(p.read_text(encoding="utf-8"))
    tri = [json.loads(l) for l in F_TRI.read_text(encoding="utf-8").splitlines() if l]
    by = {t["id"]: t for t in tri}
    upd = pase.get("actualizaciones_en_su_sitio", {})
    ok, omit = 0, []
    for tid, apoyo in upd.items():
        t = by.get(tid)
        if not t or not apoyo.strip():
            omit.append(tid)
            continue
        t["apoyo"] = apoyo.strip()[:300]
        if t["lectura"] == "ficha":
            t["lectura"] = "abstract"
        t["fecha"] = pase.get("fecha", t.get("fecha"))
        ok += 1
    contra = [c for c in pase.get("contradichas_por_el_resumen", []) if c.get("triple") in by]
    print(f"{p.name}: {ok} relaciones actualizadas · {len(omit)} omitidas {omit[:5]} · {len(contra)} contradichas")
    if dry:
        return
    F_TRI.write_text("".join(json.dumps(t, ensure_ascii=False) + "\n" for t in tri), encoding="utf-8")
    est = json.loads(F_EST.read_text(encoding="utf-8"))
    for c in contra:
        est.setdefault("discrepancias", []).append({
            "f": c.get("f") or by[c["triple"]]["f"], "triple": c["triple"], "estado": "abierta",
            "detalle": f"El resumen oficial contradice la relación {c['triple']}: {c.get('nota', '')}"[:600],
            "fecha": pase.get("fecha", "")})
    est.setdefault("pases", []).append({"archivo": p.name, "fecha": pase.get("fecha", ""), "actualizadas": ok,
                                        "contradichas": len(contra), "fuentes": pase.get("fuentes", [])})
    F_EST.write_text(json.dumps(est, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
