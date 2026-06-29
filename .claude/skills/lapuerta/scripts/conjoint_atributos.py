#!/usr/bin/env python3
"""
conjoint_atributos.py — Importancia relativa de atributos de un seguro (estilo conjoint)
para la población sintética de `lapuerta`.

Qué hace
--------
El generador modela rasgos y conductas (confianza, WTP, canal, NSE…), pero NO trae
una variable directa de "qué atributo valora más" cada persona. Este script la deriva:
a cada usuario sintético le asigna pesos de utilidad sobre los atributos de un seguro,
en función de sus rasgos, y reporta la IMPORTANCIA RELATIVA (% de la decisión) por
atributo — a nivel global y por segmento. Es la lectura "conjoint" de la población.

Atributos evaluados
-------------------
  precio              precio accesible / relación valor-precio
  transparencia       información clara, sin letra chica (entender qué cubre)
  asesoria            acompañamiento humano (un asesor que guíe, no que venda)
  cobertura           amplitud de la cobertura
  respaldo_siniestro  que pague rápido y sin trabas cuando toca usarlo
  marca               reputación / marca conocida

Direcciones de los pesos (de dónde salen)
-----------------------------------------
Replican la evidencia ya codificada en el modelo y la investigación base (SBS/APESEG):
- Sensibilidad al PRECIO ↑ con NSE bajo, sesgo del presente alto, WTP bajo, educación baja.
- TRANSPARENCIA ↑ con desconfianza y baja educación financiera (la causa #1 de desconfianza
  es la falta de información).
- ASESORÍA ↑ con preferencia por broker, mayor edad y baja educación financiera; ↓ en Gen Z
  y canal directo/digital (el broker casi duplica la confianza plena en el modelo).
- COBERTURA ↑ con NSE alto, WTP alto y confianza plena.
- RESPALDO en el siniestro ↑ con NSE alto, ser ya asegurado y alta exposición sísmica.
- MARCA ↑ con desconfianza (buscan respaldo de marca conocida) y NSE alto.

ADVERTENCIA: los pesos son `supuesto` (ilustrativos, calibrados a las DIRECCIONES de la
evidencia), no part-worths estimados de un conjoint real. Para un ranking definitivo se
necesita un ejercicio de elección discreta con datos primarios. Útil para priorizar
hipótesis, no como medida final.

Uso
---
  python conjoint_atributos.py --n 12000 --seed 42
  python conjoint_atributos.py --n 12000 --by nse
  python conjoint_atributos.py --by generacion

Solo librería estándar + el generador del mismo directorio.
"""
from __future__ import annotations

import argparse
import importlib.util
import os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("synthgen", os.path.join(HERE, "generate_synthetic_users.py"))
synthgen = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(synthgen)

ATTRIBUTES = ["precio", "transparencia", "asesoria", "cobertura", "respaldo_siniestro", "marca"]

LABELS = {
    "precio": "Precio accesible / valor-precio",
    "transparencia": "Transparencia e información clara",
    "asesoria": "Asesoría / acompañamiento humano",
    "cobertura": "Amplitud de cobertura",
    "respaldo_siniestro": "Respaldo en el siniestro (pago ágil)",
    "marca": "Marca / reputación",
}

# pesos base (antes de modificadores por rasgo)
BASE = {
    "precio": 1.0, "transparencia": 0.9, "asesoria": 0.7,
    "cobertura": 0.8, "respaldo_siniestro": 0.85, "marca": 0.6,
}


def attribute_weights(u: dict) -> dict:
    """Pesos de utilidad por atributo para un usuario, normalizados a 100%."""
    w = dict(BASE)
    nse = u["nse"]
    edu = u["educacion_financiera"]
    conf = u["confianza_aseguradora"]
    wtp = float(u["wtp_ratio"])

    # PRECIO — sensibilidad al precio
    w["precio"] += {"A": -0.4, "B": -0.2, "C": 0.1, "D": 0.4, "E": 0.6}[nse]
    w["precio"] += {"alto": 0.3, "medio": 0.0, "bajo": -0.2}[u["sesgo_presente"]]
    w["precio"] += {"baja": 0.2, "media": 0.0, "alta": -0.2}[edu]
    if wtp < 0.7:
        w["precio"] += 0.3

    # TRANSPARENCIA / información
    w["transparencia"] += {"desconfia": 0.5, "neutral": 0.1, "confia_plena": -0.1}[conf]
    w["transparencia"] += {"baja": 0.3, "media": 0.0, "alta": -0.1}[edu]

    # ASESORÍA / acompañamiento
    w["asesoria"] += {"broker_corredor": 0.5, "bancaseguros": 0.1,
                      "directo_digital": -0.3, "ninguno": 0.0}[u["canal_preferido"]]
    w["asesoria"] += {"Gen_Z_18_27": -0.3, "Millennial_28_43": -0.1,
                      "Gen_X_44_59": 0.1, "Boomer_60_mas": 0.3}[u["generacion"]]
    w["asesoria"] += {"baja": 0.2, "media": 0.0, "alta": -0.1}[edu]

    # COBERTURA
    w["cobertura"] += {"A": 0.4, "B": 0.3, "C": 0.0, "D": -0.2, "E": -0.3}[nse]
    w["cobertura"] += {"confia_plena": 0.2, "neutral": 0.0, "desconfia": -0.1}[conf]
    if wtp > 1.0:
        w["cobertura"] += 0.3

    # RESPALDO en el siniestro
    w["respaldo_siniestro"] += {"A": 0.3, "B": 0.2, "C": 0.0, "D": -0.1, "E": -0.1}[nse]
    w["respaldo_siniestro"] += {"alta": 0.15, "media": 0.0, "baja": -0.05}[u["exposicion_riesgo_sismico"]]
    if u["tenencia_seguro"] != "ninguno":
        w["respaldo_siniestro"] += 0.2

    # MARCA / reputación
    w["marca"] += {"desconfia": 0.3, "neutral": 0.0, "confia_plena": 0.1}[conf]
    w["marca"] += {"A": 0.2, "B": 0.15, "C": 0.0, "D": -0.1, "E": -0.1}[nse]

    w = {k: max(0.05, v) for k, v in w.items()}  # piso para evitar negativos
    s = sum(w.values()) or 1.0
    return {k: 100.0 * v / s for k, v in w.items()}


def aggregate(users: list[dict]) -> dict:
    acc = defaultdict(float)
    for u in users:
        for a, v in attribute_weights(u).items():
            acc[a] += v
    n = len(users) or 1
    return {a: acc[a] / n for a in ATTRIBUTES}


def print_ranking(title: str, imp: dict, n: int) -> None:
    print(f"\n{title}  (n={n})")
    for a, v in sorted(imp.items(), key=lambda kv: -kv[1]):
        bar = "█" * int(round(v / 2))
        print(f"  {LABELS[a]:38} {v:5.1f}%  {bar}")


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Importancia de atributos de seguro (estilo conjoint).")
    p.add_argument("--n", type=int, default=12000)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--by", choices=["nse", "generacion", "region", "canal_preferido"],
                   help="desglosar el ranking por esta dimensión")
    args = p.parse_args(argv)

    import random
    rng = random.Random(args.seed)
    schema = synthgen.load_schema()
    users = [synthgen.generate_user(rng, schema, i) for i in range(args.n)]

    print("IMPORTANCIA RELATIVA DE ATRIBUTOS DE UN SEGURO (estilo conjoint)")
    print("Pesos = supuesto calibrado a las direcciones de la evidencia; no part-worths reales.")
    print_ranking("== GLOBAL ==", aggregate(users), len(users))

    if args.by:
        groups = defaultdict(list)
        for u in users:
            groups[u[args.by]].append(u)
        print(f"\n──────── Desglose por {args.by} ────────")
        for lvl in sorted(groups):
            print_ranking(f"[{args.by} = {lvl}]", aggregate(groups[lvl]), len(groups[lvl]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
