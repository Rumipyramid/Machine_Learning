#!/usr/bin/env python3
"""Orquestador de /edipo2: corre los tres oráculos y emite un solo bloque.

Ejecuta en una sola pasada:
  1. tirada de I Ching (método de milenrama por defecto)
  2. cielo del momento para Lima (o la ubicación indicada)
  3. tirada de tarot de Marsella en clave junguiana

Uso:
  python tirada.py                                  # markdown consolidado
  python tirada.py --json                           # JSON consolidado
  python tirada.py --pregunta "¿sigo en Rimac?"     # sella la pregunta en la consulta
  python tirada.py --tarot cruz --iching monedas
  python tirada.py --fecha 2026-07-28 --hora 21:00
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timedelta, timezone

import astro
import iching
import tarot


def sello(pregunta: str | None, dt_local: datetime, datos: dict) -> dict:
    crudo = json.dumps(datos, ensure_ascii=False, sort_keys=True) + (pregunta or "")
    return {
        "pregunta": pregunta or "(consulta espontánea: sin pregunta explícita)",
        "momento_local": dt_local.strftime("%Y-%m-%d %H:%M"),
        "huella": hashlib.sha256(crudo.encode("utf-8")).hexdigest()[:12],
        "nota": "La huella identifica esta tirada: dos consultas distintas nunca comparten sello.",
    }


def consultar(pregunta: str | None = None, metodo_iching: str = "yarrow",
              tipo_tarot: str = "tres", invertidas: bool = False,
              dt_local: datetime | None = None, tz: float = -5.0,
              lat: float = -12.0464, lon: float = -77.0428,
              seed: int | None = None, baraja: str = "marsella") -> dict:
    if dt_local is None:
        dt_local = datetime.now(timezone.utc).replace(tzinfo=None) + timedelta(hours=tz)
    ich = iching.tirada(metodo_iching, seed)
    cielo = astro.carta(dt_local, tz, lat, lon)
    tar = tarot.tirada(tipo_tarot, False, invertidas, seed, baraja)
    datos = {"iching": ich, "cielo": cielo, "tarot": tar}
    return {"sello": sello(pregunta, dt_local, datos), **datos}


def a_markdown(c: dict) -> str:
    s = c["sello"]
    partes = [
        "# Consulta /edipo2",
        "",
        f"**Pregunta:** {s['pregunta']}",
        f"**Momento:** {s['momento_local']} (hora de Lima) · **sello:** `{s['huella']}`",
        "",
        "---",
        "",
        iching.a_markdown(c["iching"]),
        "",
        "---",
        "",
        astro.a_markdown(c["cielo"]),
        "",
        "---",
        "",
        tarot.a_markdown(c["tarot"]),
    ]
    return "\n".join(partes)


def main() -> None:
    ap = argparse.ArgumentParser(description="Orquestador de oráculos de /edipo2")
    ap.add_argument("--pregunta", default=None)
    ap.add_argument("--iching", choices=("yarrow", "monedas"), default="yarrow")
    ap.add_argument("--tarot", choices=("una", "tres", "cruz", "arbol"), default="tres")
    ap.add_argument("--invertidas", action="store_true")
    ap.add_argument("--baraja", choices=("marsella", "waite"), default="marsella",
                    help="sistema de significados del tarot")
    ap.add_argument("--fecha", help="AAAA-MM-DD (hora local)")
    ap.add_argument("--hora", help="HH:MM (hora local)")
    ap.add_argument("--lat", type=float, default=-12.0464)
    ap.add_argument("--lon", type=float, default=-77.0428)
    ap.add_argument("--tz", type=float, default=-5.0)
    ap.add_argument("--seed", type=int, default=None, help="solo para pruebas reproducibles")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    dt = datetime.now(timezone.utc).replace(tzinfo=None) + timedelta(hours=a.tz)
    if a.fecha:
        y, mo, d = (int(x) for x in a.fecha.split("-"))
        dt = dt.replace(year=y, month=mo, day=d)
    if a.hora:
        h, mi = (int(x) for x in a.hora.split(":"))
        dt = dt.replace(hour=h, minute=mi, second=0, microsecond=0)

    c = consultar(a.pregunta, a.iching, a.tarot, a.invertidas, dt, a.tz, a.lat, a.lon,
                  a.seed, a.baraja)
    print(json.dumps(c, ensure_ascii=False, indent=2) if a.json else a_markdown(c))


if __name__ == "__main__":
    main()
