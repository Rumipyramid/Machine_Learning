#!/usr/bin/env python3
"""
Generador de usuarios sinteticos - consumidores de seguros (Peru).

Muestrea perfiles a partir de la matriz de variables y modelos derivados
definidos en synthetic_user_schema.json (calibrados con datos de SBS 2023,
APESEG, APEIM y literatura conductual; ver
research/seguros_comportamiento_mundo_peru.md).

Uso:
    python generate_synthetic_users.py --n 1000 --out usuarios.csv --seed 42
    python generate_synthetic_users.py --n 5            # imprime en consola

Solo usa la libreria estandar (random, json, csv, argparse, math).
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import os
import random
import sys

SCHEMA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "synthetic_user_schema.json")


def load_schema(path: str = SCHEMA_PATH) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def weighted_choice(rng: random.Random, dist: dict) -> str:
    """Elige una clave segun el peso (probabilidad) asociado."""
    keys = list(dist.keys())
    weights = list(dist.values())
    return rng.choices(keys, weights=weights, k=1)[0]


def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + math.exp(-x))


def sample_confianza(rng: random.Random, schema: dict, canal: str) -> str:
    model = schema["modelos_derivados"]["confianza_aseguradora"]
    base = dict(model["marginal_objetivo"])
    if canal == "broker_corredor":
        base["confia_plena"] += 0.15
        base["desconfia"] = max(0.01, base["desconfia"] - 0.15)
    elif canal == "directo_digital":
        base["confia_plena"] = max(0.01, base["confia_plena"] - 0.03)
        base["desconfia"] += 0.03
    return weighted_choice(rng, base)


def sample_situacion_laboral(rng: random.Random, schema: dict, nse: str) -> str:
    return weighted_choice(rng, schema["variables"]["situacion_laboral"]["tabla"][nse])


def sample_tenencia_vehiculo(rng: random.Random, schema: dict, region: str) -> str:
    return weighted_choice(rng, schema["variables"]["tenencia_vehiculo"]["tabla"][region])


def sample_acceso_digital(rng: random.Random, schema: dict, region: str, nse: str, generacion: str) -> str:
    s = schema["variables"]["acceso_digital"]["score"]
    score = s["intercepto"] + s["region"][region] + s["nse"][nse] + s["generacion"][generacion]
    if score >= s["umbral_alta"]:
        return "alta"
    if score >= s["umbral_media"]:
        return "media"
    return "baja"


def sample_bancarizado(rng: random.Random, schema: dict, nse: str, region: str, acceso: str) -> bool:
    s = schema["variables"]["bancarizado"]["score"]
    score = s["intercepto"] + s["nse"][nse] + s["region"][region] + s["acceso_digital"][acceso]
    return rng.random() < sigmoid(score)


def sample_tenencia(rng: random.Random, schema: dict, nse: str, edu: str, sesgo: str,
                    confianza: str, situacion: str, bancarizado: bool, vehiculo: str) -> str:
    d = schema["modelos_derivados"]["tenencia_seguro"]["drivers"]
    score = (d["intercepto"]
             + d["nse"][nse]
             + d["educacion_financiera"][edu]
             + d["sesgo_presente"][sesgo]
             + d["confianza_aseguradora"][confianza]
             + d["situacion_laboral"][situacion]
             + d["bancarizado"]["true" if bancarizado else "false"]
             + d["tenencia_vehiculo"][vehiculo])
    p_any = sigmoid(score)
    if rng.random() >= p_any:
        return "ninguno"
    # De los que tienen seguro: mas obligatorio en NSE bajo; formal y auto inclinan a obligatorio.
    sp = schema["modelos_derivados"]["tenencia_seguro"]["split_voluntario"]
    p_voluntario = sp["p_voluntario_por_nse"][nse]
    if situacion == "formal_dependiente":
        p_voluntario *= sp["factor_formal_dependiente"]
    if vehiculo == "auto":
        p_voluntario *= sp["factor_auto"]
    return "voluntario" if rng.random() < p_voluntario else "solo_obligatorio"


def sample_desastres(rng: random.Random, schema: dict, nse: str,
                     exposicion: str, tenencia: str) -> bool:
    base = schema["modelos_derivados"]["seguro_desastres_naturales"]["marginal_objetivo"]
    mult = 1.0
    mult *= {"A": 4.0, "B": 2.5, "C": 1.0, "D": 0.4, "E": 0.2}[nse]
    mult *= {"alta": 1.4, "media": 1.0, "baja": 0.6}[exposicion]
    mult *= {"voluntario": 3.0, "solo_obligatorio": 0.8, "ninguno": 0.1}[tenencia]
    p = min(0.95, base * mult)
    return rng.random() < p


def sample_wtp(rng: random.Random, schema: dict, tenencia: str) -> float:
    dist = schema["modelos_derivados"]["wtp_ratio"]["distribucion"]
    params = dist["asegurado"] if tenencia != "ninguno" else dist["no_asegurado"]
    val = rng.gauss(params["media"], params["sd"])
    return round(max(0.0, val), 3)


def generate_user(rng: random.Random, schema: dict, idx: int) -> dict:
    v = schema["variables"]
    generacion = weighted_choice(rng, v["generacion"]["categorias"])
    nse = weighted_choice(rng, v["nse"]["categorias"])
    region = weighted_choice(rng, v["region"]["categorias"])
    edu = weighted_choice(rng, v["educacion_financiera"]["categorias"])
    sesgo = weighted_choice(rng, v["sesgo_presente"]["categorias"])
    canal = weighted_choice(rng, v["canal_preferido"]["categorias"])
    exposicion = weighted_choice(rng, v["exposicion_riesgo_sismico"]["tabla"][region])
    apertura = weighted_choice(rng, v["apertura_datos_ia"]["tabla"][generacion])
    situacion = sample_situacion_laboral(rng, schema, nse)
    vehiculo = sample_tenencia_vehiculo(rng, schema, region)
    acceso = sample_acceso_digital(rng, schema, region, nse, generacion)
    bancarizado = sample_bancarizado(rng, schema, nse, region, acceso)

    confianza = sample_confianza(rng, schema, canal)
    tenencia = sample_tenencia(rng, schema, nse, edu, sesgo, confianza, situacion, bancarizado, vehiculo)
    desastres = sample_desastres(rng, schema, nse, exposicion, tenencia)
    wtp = sample_wtp(rng, schema, tenencia)

    return {
        "id": f"user_{idx:06d}",
        "generacion": generacion,
        "nse": nse,
        "region": region,
        "educacion_financiera": edu,
        "sesgo_presente": sesgo,
        "canal_preferido": canal,
        "situacion_laboral": situacion,
        "tenencia_vehiculo": vehiculo,
        "acceso_digital": acceso,
        "bancarizado": bancarizado,
        "exposicion_riesgo_sismico": exposicion,
        "apertura_datos_ia": apertura,
        "confianza_aseguradora": confianza,
        "tenencia_seguro": tenencia,
        "seguro_desastres_naturales": desastres,
        "wtp_ratio": wtp,
    }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Genera usuarios sinteticos de seguros (Peru).")
    parser.add_argument("--n", type=int, default=10, help="numero de usuarios a generar")
    parser.add_argument("--out", type=str, default=None, help="ruta de salida CSV (opcional)")
    parser.add_argument("--seed", type=int, default=None, help="semilla para reproducibilidad")
    parser.add_argument("--schema", type=str, default=SCHEMA_PATH, help="ruta del schema JSON")
    args = parser.parse_args(argv)

    rng = random.Random(args.seed)
    schema = load_schema(args.schema)
    users = [generate_user(rng, schema, i) for i in range(args.n)]
    fields = list(users[0].keys())

    if args.out:
        with open(args.out, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows(users)
        print(f"Generados {len(users)} usuarios -> {args.out}")
    else:
        writer = csv.DictWriter(sys.stdout, fieldnames=fields)
        writer.writeheader()
        writer.writerows(users)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
