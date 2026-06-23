#!/usr/bin/env python3
"""Registra un cambio del Beholder y mantiene solo los últimos 15 días.

Repositorio de historial: agrega una entrada, purga las de más de 15 días y
regenera la vista legible CAMBIOS.md. Solo stdlib.

Uso:
  python reportes/historial/registrar_cambio.py --autor "Nombre" --clave Q-7 \
      --campo "Estado" --antes "Diseñado" --despues "In Review" --tipo normal
  # cambio de fecha (controlado):
  python reportes/historial/registrar_cambio.py --autor "Meli" --clave Q-6 \
      --campo "Fecha de entrega" --antes "Julio 2026" --despues "Agosto 2026" \
      --tipo fecha --estado pendiente
  # al aprobar una fecha:  ... --tipo fecha --estado aprobada
  # solo purgar/regenerar:
  python reportes/historial/registrar_cambio.py --solo-purgar
"""
import argparse
import csv
import datetime as dt
from pathlib import Path

DIR = Path(__file__).resolve().parent
CSV_PATH = DIR / "CAMBIOS.csv"
MD_PATH = DIR / "CAMBIOS.md"
RETENCION_DIAS = 15
CAMPOS = ["timestamp", "autor", "clave", "campo", "antes", "despues", "tipo", "estado"]


def cargar():
    if not CSV_PATH.exists():
        return []
    with CSV_PATH.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def guardar(rows):
    with CSV_PATH.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS)
        w.writeheader()
        w.writerows(rows)


def purgar(rows):
    corte = dt.datetime.now() - dt.timedelta(days=RETENCION_DIAS)
    out = []
    for r in rows:
        try:
            ts = dt.datetime.fromisoformat(r["timestamp"])
        except Exception:
            continue
        if ts >= corte:
            out.append(r)
    return out


def render(rows):
    rows_sorted = sorted(rows, key=lambda r: r["timestamp"], reverse=True)
    ahora = dt.datetime.now().isoformat(timespec="seconds")
    lines = [
        "# 🕝 Historial de cambios del Beholder — últimos 15 días",
        "",
        "> Generado por `registrar_cambio.py`. **No editar a mano.** El historial completo siempre "
        "queda en el git log.",
        f"> Retención: {RETENCION_DIAS} días · Última actualización: {ahora} · Cambios vigentes: {len(rows_sorted)}",
        "",
        "| Fecha/hora | Autor | Quest | Campo | Antes | Después | Tipo | Estado |",
        "|---|---|---|---|---|---|---|---|",
    ]
    if not rows_sorted:
        lines.append("| — | — | — | — | — | — | — | (sin cambios en los últimos 15 días) |")
    for r in rows_sorted:
        lines.append(
            "| {timestamp} | {autor} | {clave} | {campo} | {antes} | {despues} | {tipo} | {estado} |".format(**r)
        )
    MD_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description="Registra un cambio del Beholder (retención 15 días).")
    ap.add_argument("--autor")
    ap.add_argument("--clave")
    ap.add_argument("--campo")
    ap.add_argument("--antes", default="")
    ap.add_argument("--despues", default="")
    ap.add_argument("--tipo", choices=["normal", "fecha"], default="normal")
    ap.add_argument("--estado", default="aplicado")
    ap.add_argument("--solo-purgar", action="store_true")
    a = ap.parse_args()

    rows = cargar()
    if not a.solo_purgar:
        if not (a.autor and a.clave and a.campo):
            ap.error("Para registrar necesitas --autor, --clave y --campo (o usa --solo-purgar).")
        rows.append({
            "timestamp": dt.datetime.now().isoformat(timespec="seconds"),
            "autor": a.autor, "clave": a.clave, "campo": a.campo,
            "antes": a.antes, "despues": a.despues, "tipo": a.tipo, "estado": a.estado,
        })
    rows = purgar(rows)
    guardar(rows)
    render(rows)
    print(f"Historial actualizado: {len(rows)} cambio(s) en los últimos {RETENCION_DIAS} días.")


if __name__ == "__main__":
    main()
