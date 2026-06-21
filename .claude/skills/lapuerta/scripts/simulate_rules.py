#!/usr/bin/env python3
"""Motor de respuestas POR REGLAS para usuarios sintéticos de seguros (Perú).

Hace preguntas predeterminadas a una población generada y devuelve la distribución
de respuestas (y, opcionalmente, el desglose por segmento). Las reglas combinan los
rasgos de cada persona (confianza, NSE, sesgo del presente, educación, canal…) con
direcciones tomadas de los datos.

Solo usa la librería estándar + el generador del mismo skill.

Ejemplos:
  python scripts/simulate_rules.py --question confianza --n 1000 --seed 42
  python scripts/simulate_rules.py --question contratar --n 1000 --by nse
  python scripts/simulate_rules.py --question marca --brand "RIMAC" --filter nse=A --n 800
  python scripts/simulate_rules.py --list        # ver preguntas disponibles
"""
from __future__ import annotations

import argparse
import collections
import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("synthgen", os.path.join(HERE, "generate_synthetic_users.py"))
synthgen = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(synthgen)


# ---- Definición de preguntas (label, categorías, función de respuesta, favorable) ----
def _q_confianza(u, brand=None):
    return u["confianza_aseguradora"]


def _q_contratar(u, brand=None):
    if u["tenencia_seguro"] == "voluntario":
        return "si"
    s = 0.0
    s += {"confia_plena": 2, "neutral": 0, "desconfia": -1.5}[u["confianza_aseguradora"]]
    s += {"A": 1.5, "B": 1.5, "C": 0.3, "D": -0.5, "E": -1}[u["nse"]]
    s += {"alto": -1.2, "medio": -0.3, "bajo": 0.5}[u["sesgo_presente"]]
    s += {"alta": 0.8, "media": 0.2, "baja": -0.4}[u["educacion_financiera"]]
    if s >= 1.5:
        return "si"
    if s >= -0.6:
        return "condiciones"
    return "no"


def _q_tenencia(u, brand=None):
    return u["tenencia_seguro"]


def _q_marca(u, brand=None):
    s = 0.0
    s += {"confia_plena": 2, "neutral": 0, "desconfia": -2}[u["confianza_aseguradora"]]
    s += {"voluntario": 1, "solo_obligatorio": 0, "ninguno": -0.5}[u["tenencia_seguro"]]
    s += {"broker_corredor": 1, "bancaseguros": 0.7, "directo_digital": -0.3, "ninguno": -0.5}[u["canal_preferido"]]
    if s >= 1.5:
        return "positiva"
    if s >= -0.6:
        return "neutral"
    return "critica"


def _q_datos_ia(u, brand=None):
    return u["apertura_datos_ia"]


QUESTIONS = {
    "confianza": {
        "label": "¿Confías en las aseguradoras?",
        "cats": [("confia_plena", "Confío"), ("neutral", "Neutral"), ("desconfia", "Desconfío")],
        "answer": _q_confianza, "favorable": "confia_plena",
    },
    "contratar": {
        "label": "¿Contratarías un seguro hoy?",
        "cats": [("si", "Sí"), ("condiciones", "Sí, con condiciones"), ("no", "No")],
        "answer": _q_contratar, "favorable": "si",
    },
    "tenencia": {
        "label": "¿Tienes algún seguro actualmente?",
        "cats": [("voluntario", "Seguro voluntario"), ("solo_obligatorio", "Solo obligatorio"), ("ninguno", "Ninguno")],
        "answer": _q_tenencia, "favorable": "voluntario",
    },
    "marca": {
        "label": "¿Qué piensas de {brand}?", "needs_brand": True,
        "cats": [("positiva", "Positiva"), ("neutral", "Neutral / evalúa"), ("critica", "Crítica")],
        "answer": _q_marca, "favorable": "positiva",
    },
    "datos_ia": {
        "label": "¿Compartirías tus datos con una aseguradora que use IA?",
        "cats": [("alta", "Sí, sin problema"), ("media", "Con reservas"), ("baja", "No")],
        "answer": _q_datos_ia, "favorable": "alta",
    },
}

DIM_FIELDS = ["nse", "generacion", "region", "canal_preferido", "educacion_financiera", "sesgo_presente"]


def sample(n, seed, filters):
    import random
    rng = random.Random(int(seed)); schema = synthgen.load_schema()
    out, i, guard = [], 0, 0
    while len(out) < n and guard < 5_000_000:
        u = synthgen.generate_user(rng, schema, i); i += 1; guard += 1
        if all(u.get(k) == v for k, v in filters.items()):
            out.append(u)
    return out


def tally(users, q, brand):
    counts = collections.Counter(q["answer"](u, brand) for u in users)
    n = len(users) or 1
    return [(key, label, counts.get(key, 0), round(100 * counts.get(key, 0) / n, 1)) for key, label in q["cats"]]


def main(argv=None):
    p = argparse.ArgumentParser(description="Simula respuestas por reglas de usuarios sintéticos de seguros.")
    p.add_argument("--question", help="id de la pregunta (ver --list)")
    p.add_argument("--brand", default="la marca", help="marca para la pregunta 'marca'")
    p.add_argument("--n", type=int, default=1000)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--by", choices=DIM_FIELDS, help="desglosar por esta dimensión")
    p.add_argument("--filter", action="append", default=[], metavar="campo=valor",
                   help="filtrar segmento (repetible), p. ej. --filter nse=A")
    p.add_argument("--list", action="store_true", help="listar preguntas")
    args = p.parse_args(argv)

    if args.list or not args.question:
        print("Preguntas disponibles:")
        for k, q in QUESTIONS.items():
            print(f"  {k:10} → {q['label']}")
        return 0

    q = QUESTIONS[args.question]
    filters = dict(f.split("=", 1) for f in args.filter)
    users = sample(args.n, args.seed, filters)
    label = q["label"].replace("{brand}", args.brand)
    fdesc = (" · " + ", ".join(f"{k}={v}" for k, v in filters.items())) if filters else ""
    print(f"Pregunta: {label}")
    print(f"Muestra: {len(users)} usuarios (semilla {args.seed}){fdesc}\n")
    if not users:
        print("Ningún usuario cumple esos filtros."); return 0

    print("Distribución:")
    for _, lbl, cnt, pct in tally(users, q, args.brand):
        bar = "█" * int(pct / 2)
        print(f"  {lbl:22} {pct:5.1f}%  {bar}")

    if args.by:
        print(f"\nDesglose por {args.by} (% '{dict(q['cats'])[q['favorable']]}'):")
        groups = collections.defaultdict(list)
        for u in users:
            groups[u[args.by]].append(u)
        for lvl in sorted(groups):
            sub = groups[lvl]
            fav = sum(1 for u in sub if q["answer"](u, args.brand) == q["favorable"])
            print(f"  {lvl:22} {round(100*fav/len(sub),1):5.1f}%  (n={len(sub)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
