#!/usr/bin/env python3
"""
validate.py — Harness de validacion del generador de usuarios sinteticos (lapuerta).

No puedes mejorar lo que no puedes medir. Este script mide la calidad del generador
en los tres ejes que importan:

  1) MARGINALES vs OBJETIVO (con tolerancia)   -> validez de calibracion + golden test
  2) ASOCIACIONES por pares (direccion/fuerza) -> validez de la estructura interna
  3) INTERVALOS bootstrap                       -> confiabilidad (incertidumbre)
  4) ESTABILIDAD (varianza vs n)                -> confiabilidad (n minimo por segmento)

Uso:
  python validate.py                      # reporte completo (n grande)
  python validate.py --n 20000 --seed 7
  python validate.py --check              # solo pass/fail; exit code 1 si algo falla (CI)
  python validate.py --stability          # incluye la curva varianza vs n (mas lento)
  python validate.py --joint fitted.csv   # validar sembrando desde una conjunta IPF/ENAHO

Solo libreria estandar + el generador del mismo directorio.
"""
from __future__ import annotations

import argparse
import importlib.util
import math
import os
import random
import statistics
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("synthgen", os.path.join(HERE, "generate_synthetic_users.py"))
synthgen = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(synthgen)


# --------------------------------------------------------------------------- #
# Generacion de poblacion (con o sin semilla conjunta)
# --------------------------------------------------------------------------- #

def gen_population(n: int, seed: int, joint_path: str | None = None) -> list[dict]:
    rng = random.Random(seed)
    schema = synthgen.load_schema()
    sampler = None
    if joint_path:
        _, sampler = synthgen.load_joint_sampler(joint_path)
    return [synthgen.generate_user(rng, schema, i,
                                   base_override=sampler(rng) if sampler else None)
            for i in range(n)]


def rate(U: list[dict], pred) -> float:
    return sum(1 for u in U if pred(u)) / (len(U) or 1)


# --------------------------------------------------------------------------- #
# 1) Marginales vs objetivo (con tolerancia)
# --------------------------------------------------------------------------- #
# (objetivo, tolerancia_abs, predicado). Objetivos anclados en SBS/APESEG/BCRP
# (ver research/seguros_comportamiento_mundo_peru.md y el schema).

TARGETS = {
    "any_insurance (tiene seguro)": (0.40, 0.04, lambda u: u["tenencia_seguro"] != "ninguno"),
    "desconfia":                    (0.48, 0.05, lambda u: u["confianza_aseguradora"] == "desconfia"),
    "seguro_desastres":             (0.033, 0.015, lambda u: u["seguro_desastres_naturales"]),
    "bancarizado":                  (0.59, 0.05, lambda u: u["bancarizado"]),
    "sin cobertura previsional":    (0.60, 0.07, lambda u: u["cobertura_previsional"] == "ninguna"),
}


def report_marginales(U: list[dict]) -> bool:
    print("── 1. MARGINALES vs OBJETIVO " + "─" * 40)
    print(f"{'indicador':32} {'modelo':>8} {'objetivo':>9} {'tol':>6}  estado")
    all_ok = True
    for name, (target, tol, pred) in TARGETS.items():
        val = rate(U, pred)
        ok = abs(val - target) <= tol
        all_ok &= ok
        print(f"{name:32} {val:8.3f} {target:9.3f} {tol:6.3f}  {'OK' if ok else 'FUERA'}")
    print(f"  → {'TODAS dentro de tolerancia' if all_ok else 'HAY MARGINALES FUERA DE RANGO'}\n")
    return all_ok


# --------------------------------------------------------------------------- #
# 2) Asociaciones por pares (validez de la estructura interna)
# --------------------------------------------------------------------------- #

def cond_rate_by(U, dim, pred):
    """Tasa de `pred` por nivel de `dim`."""
    g = defaultdict(list)
    for u in U:
        g[u[dim]].append(u)
    return {lvl: rate(sub, pred) for lvl, sub in g.items()}


def is_monotonic(rates: dict, order: list, decreasing=True, slack=0.01) -> bool:
    """Verifica monotonia a lo largo de `order` (permite pequeño ruido `slack`)."""
    seq = [rates[k] for k in order if k in rates]
    for a, b in zip(seq, seq[1:]):
        if decreasing and b > a + slack:
            return False
        if not decreasing and b < a - slack:
            return False
    return True


def cramers_v(U, a, b) -> float:
    """Cramér's V entre dos variables categoricas (0=independencia, 1=asociacion total)."""
    rows = sorted({u[a] for u in U}); cols = sorted({u[b] for u in U})
    ri = {v: i for i, v in enumerate(rows)}; ci = {v: i for i, v in enumerate(cols)}
    table = [[0] * len(cols) for _ in rows]
    for u in U:
        table[ri[u[a]]][ci[u[b]]] += 1
    n = len(U)
    rt = [sum(r) for r in table]; ct = [sum(c) for c in zip(*table)]
    chi2 = 0.0
    for i in range(len(rows)):
        for j in range(len(cols)):
            exp = rt[i] * ct[j] / n if n else 0
            if exp > 0:
                chi2 += (table[i][j] - exp) ** 2 / exp
    k = min(len(rows), len(cols))
    return math.sqrt(chi2 / (n * (k - 1))) if n and k > 1 else 0.0


def report_asociaciones(U: list[dict]) -> bool:
    print("── 2. ASOCIACIONES (estructura que DEBE cumplirse por diseño) " + "─" * 7)
    ok_all = True

    checks = [
        ("Tenencia ↑ con NSE (A→E decrec.)", "nse", ["A", "B", "C", "D", "E"], True,
         lambda u: u["tenencia_seguro"] != "ninguno"),
        ("Tenencia ↓ con sesgo presente (bajo→alto decrec.)", "sesgo_presente", ["bajo", "medio", "alto"], True,
         lambda u: u["tenencia_seguro"] != "ninguno"),
        ("Tenencia ↑ con educación (alta→baja decrec.)", "educacion_financiera", ["alta", "media", "baja"], True,
         lambda u: u["tenencia_seguro"] != "ninguno"),
        ("Desastres ↑ con exposición (alta→baja decrec.)", "exposicion_riesgo_sismico", ["alta", "media", "baja"], True,
         lambda u: u["seguro_desastres_naturales"]),
    ]
    for desc, dim, order, dec, pred in checks:
        rates = cond_rate_by(U, dim, pred)
        ok = is_monotonic(rates, order, decreasing=dec)
        ok_all &= ok
        seq = "  ".join(f"{k}={rates.get(k,0):.2f}" for k in order)
        print(f"  [{'OK' if ok else '!!'}] {desc}\n         {seq}")

    # broker eleva confianza: P(desconfia|broker) < P(desconfia|global)
    p_broker = rate([u for u in U if u["canal_preferido"] == "broker_corredor"],
                    lambda u: u["confianza_aseguradora"] == "desconfia")
    p_global = rate(U, lambda u: u["confianza_aseguradora"] == "desconfia")
    ok = p_broker < p_global
    ok_all &= ok
    print(f"  [{'OK' if ok else '!!'}] Broker reduce desconfianza: broker={p_broker:.2f} < global={p_global:.2f}")

    # WTP asegurado > no asegurado
    wtp_a = statistics.mean([u["wtp_ratio"] for u in U if u["tenencia_seguro"] != "ninguno"] or [0])
    wtp_n = statistics.mean([u["wtp_ratio"] for u in U if u["tenencia_seguro"] == "ninguno"] or [0])
    ok = wtp_a > wtp_n
    ok_all &= ok
    print(f"  [{'OK' if ok else '!!'}] WTP asegurado > no asegurado: {wtp_a:.2f} > {wtp_n:.2f}")

    # fuerza de asociacion (informativo)
    print(f"\n  Fuerza de asociación (Cramér's V):")
    print(f"    NSE × tenencia_seguro      = {cramers_v(U, 'nse', 'tenencia_seguro'):.3f}")
    print(f"    región × exposición_sísmica = {cramers_v(U, 'region', 'exposicion_riesgo_sismico'):.3f}")
    print(f"  → {'estructura coherente' if ok_all else 'REVISAR: alguna relación no se cumple'}\n")
    return ok_all


# --------------------------------------------------------------------------- #
# 3) Intervalos bootstrap (confiabilidad)
# --------------------------------------------------------------------------- #

def bootstrap_ci(flags01: list[int], B: int = 1000, seed: int = 0, alpha: float = 0.05):
    """IC percentil para una proporción a partir de indicadores 0/1."""
    rng = random.Random(seed)
    n = len(flags01)
    if n == 0:
        return (0.0, 0.0)
    means = []
    for _ in range(B):
        s = sum(flags01[rng.randrange(n)] for _ in range(n))
        means.append(s / n)
    means.sort()
    lo = means[int((alpha / 2) * B)]
    hi = means[min(B - 1, int((1 - alpha / 2) * B))]
    return (lo, hi)


def report_bootstrap(U: list[dict], B: int = 1000, seed: int = 0) -> None:
    print(f"── 3. INTERVALOS BOOTSTRAP (B={B}, IC 95%) " + "─" * 26)
    for name, (_, _, pred) in TARGETS.items():
        flags = [1 if pred(u) else 0 for u in U]
        est = sum(flags) / (len(flags) or 1)
        lo, hi = bootstrap_ci(flags, B=B, seed=seed)
        print(f"  {name:32} {est:6.3f}  IC95% [{lo:.3f}, {hi:.3f}]  (±{(hi-lo)/2:.3f})")
    print()


# --------------------------------------------------------------------------- #
# 4) Estabilidad (varianza vs n)
# --------------------------------------------------------------------------- #

def report_stability(ns=(100, 500, 1000, 5000), reps: int = 30, joint=None) -> None:
    print(f"── 4. ESTABILIDAD (any-insurance · {reps} semillas por n) " + "─" * 13)
    print(f"{'n':>7} {'media':>8} {'desv.est':>9} {'rango (min–max)':>22}")
    for n in ns:
        vals = []
        for r in range(reps):
            U = gen_population(n, seed=1000 + r, joint_path=joint)
            vals.append(rate(U, lambda u: u["tenencia_seguro"] != "ninguno"))
        sd = statistics.pstdev(vals)
        print(f"{n:7d} {statistics.mean(vals):8.3f} {sd:9.3f}   {min(vals):.3f}–{max(vals):.3f}")
    print("  → a mayor n, menor desviación. Usa esto para fijar el n mínimo por segmento.\n")


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #

def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Harness de validación del generador de usuarios sintéticos.")
    p.add_argument("--n", type=int, default=20000, help="tamaño de la muestra de validación")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--bootstrap", type=int, default=1000, help="réplicas bootstrap (0 = omitir)")
    p.add_argument("--stability", action="store_true", help="incluir curva varianza vs n (más lento)")
    p.add_argument("--joint", default=None, help="sembrar variables base desde una conjunta IPF/ENAHO")
    p.add_argument("--check", action="store_true",
                   help="modo CI: solo pass/fail de marginales+asociaciones; exit 1 si falla")
    args = p.parse_args(argv)

    U = gen_population(args.n, args.seed, joint_path=args.joint)
    seed_note = f" · joint={args.joint}" if args.joint else ""
    print(f"\nVALIDACIÓN · n={len(U)} · semilla={args.seed}{seed_note}\n")

    ok_marg = report_marginales(U)
    ok_assoc = report_asociaciones(U)

    if args.check:
        ok = ok_marg and ok_assoc
        print(f"RESULTADO: {'PASS ✓' if ok else 'FAIL ✗'}")
        return 0 if ok else 1

    if args.bootstrap:
        report_bootstrap(U, B=args.bootstrap, seed=args.seed)
    if args.stability:
        report_stability(joint=args.joint)

    print("Listo. (usa --check para CI, --stability para la curva varianza vs n)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
