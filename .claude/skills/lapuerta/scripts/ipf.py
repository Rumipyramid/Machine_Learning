#!/usr/bin/env python3
"""
ipf.py — Iterative Proportional Fitting (raking) para sembrar el generador de
`lapuerta` con la estructura de dependencia real de ENAHO.

Idea (mejora #1 de la revision de literatura)
----------------------------------------------
Hoy el generador muestrea variables base (nse, region, educacion, ...) de sus
marginales de forma INDEPENDIENTE -> no garantiza las correlaciones reales.
IPF toma una TABLA CONJUNTA de referencia (la semilla que produce enaho_loader.py)
y la reescala iterativamente hasta que sus marginales coincidan con las marginales
objetivo, CONSERVANDO la asociacion (odds-ratios) de la semilla.

  semilla (ENAHO joint.csv)  +  marginales objetivo (schema/encuesta)
        ──IPF──▶  tabla conjunta ajustada  ──▶  muestreador reproducible

Referencias: Deming & Stephan (1940); raking de encuestas; alternativa al copula
(SynC) cuando si hay una tabla conjunta de referencia.

Limitaciones honestas
---------------------
- IPF NO puede crear celdas que no existan en la semilla (ceros estructurales):
  si una combinacion no aparece en ENAHO, tendra probabilidad 0 en la salida.
- Solo ajusta las dimensiones para las que se den marginales objetivo; el resto
  de la estructura conjunta se mantiene tal como en la semilla.

Solo libreria estandar.

Uso
---
  # Ajustar la semilla de ENAHO a las marginales objetivo del esquema
  python ipf.py --joint joint.csv --targets targets.json \
      --out-fitted fitted.csv

  # Ajustar y ademas muestrear 1000 perfiles base reproducibles
  python ipf.py --joint joint.csv --targets targets.json \
      --out-fitted fitted.csv --sample 1000 --seed 42 --out-sample base.csv

Formato de --joint  : CSV de enaho_loader.py (columnas de dimension + 'peso_expandido').
Formato de --targets: JSON {dimension: {categoria: probabilidad, ...}, ...}.
                      Puede cubrir solo algunas dimensiones.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import random
import sys
from collections import defaultdict


# --------------------------------------------------------------------------- #
# Carga
# --------------------------------------------------------------------------- #

def load_joint(path: str, weight_col: str = "peso_expandido"):
    """Lee el CSV de tabla conjunta. Devuelve (dims, {tupla: peso})."""
    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
        # dims = todas las columnas menos las de peso/proporcion
        ignore = {weight_col, "proporcion"}
        dim_idx = [i for i, c in enumerate(header) if c not in ignore]
        try:
            w_idx = header.index(weight_col)
        except ValueError:
            raise SystemExit(f"[!] no encuentro la columna de peso '{weight_col}' en {path}")
        dims = [header[i] for i in dim_idx]
        table = defaultdict(float)
        for row in reader:
            if not row:
                continue
            key = tuple(row[i] for i in dim_idx)
            try:
                table[key] += float(row[w_idx])
            except ValueError:
                continue
    return dims, dict(table)


def load_targets(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        targets = json.load(f)
    # normalizar cada dimension a suma 1
    out = {}
    for dim, cats in targets.items():
        s = sum(cats.values())
        if s <= 0:
            continue
        out[dim] = {c: v / s for c, v in cats.items()}
    return out


# --------------------------------------------------------------------------- #
# IPF
# --------------------------------------------------------------------------- #

def _marginal(table: dict, dims: list[str], dim: str) -> dict:
    j = dims.index(dim)
    m = defaultdict(float)
    for key, w in table.items():
        m[key[j]] += w
    return dict(m)


def ipf(table: dict, dims: list[str], targets: dict,
        max_iter: int = 200, tol: float = 1e-8, verbose: bool = True):
    """Ajusta `table` a las marginales `targets`. Devuelve (tabla_ajustada, diag)."""
    table = {k: float(v) for k, v in table.items()}
    fit_dims = [d for d in dims if d in targets]
    if not fit_dims:
        raise SystemExit("[!] ninguna dimension de --targets coincide con --joint")

    # avisar de categorias objetivo ausentes en la semilla (ceros estructurales)
    for d in fit_dims:
        present = set(_marginal(table, dims, d))
        missing = [c for c in targets[d] if targets[d][c] > 0 and c not in present]
        if missing and verbose:
            print(f"[!] '{d}': categorias en objetivo ausentes en la semilla "
                  f"(quedaran en 0): {missing}", file=sys.stderr)

    history = []
    max_err = float("inf")
    for it in range(1, max_iter + 1):
        # --- una pasada completa: ajustar cada dimension a su marginal objetivo ---
        for d in fit_dims:
            j = dims.index(d)
            cur = _marginal(table, dims, d)
            cur_total = sum(cur.values()) or 1.0
            for key in list(table):
                cat = key[j]
                cur_cat = cur.get(cat, 0.0)
                if cur_cat <= 0:
                    continue
                tgt = targets[d].get(cat, 0.0) * cur_total  # masa objetivo de la categoria
                table[key] *= tgt / cur_cat
        # --- error medido al FINAL de la pasada, sobre TODAS las dims ajustadas ---
        max_err = 0.0
        for d in fit_dims:
            newm = _marginal(table, dims, d)
            new_total = sum(newm.values()) or 1.0
            for cat, tprob in targets[d].items():
                max_err = max(max_err, abs(newm.get(cat, 0.0) / new_total - tprob))
        history.append(max_err)
        if max_err < tol:
            break
    diag = {"iteraciones": it, "error_max_final": max_err,
            "convergio": max_err < tol, "dims_ajustadas": fit_dims}
    if verbose:
        print(f"[ok] IPF: {it} iter · error_max={max_err:.2e} · "
              f"{'convergio' if diag['convergio'] else 'no convergio'}", file=sys.stderr)
    return table, diag


# --------------------------------------------------------------------------- #
# Validacion, exportacion y muestreo
# --------------------------------------------------------------------------- #

def marginales_normalizadas(table: dict, dims: list[str]) -> dict:
    total = sum(table.values()) or 1.0
    out = {}
    for d in dims:
        m = _marginal(table, dims, d)
        out[d] = {c: round(w / total, 4) for c, w in sorted(m.items())}
    return out


def export_fitted(table: dict, dims: list[str], path: str) -> None:
    total = sum(table.values()) or 1.0
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(list(dims) + ["peso", "proporcion"])
        for key, weight in sorted(table.items(), key=lambda kv: -kv[1]):
            w.writerow(list(key) + [round(weight, 6), round(weight / total, 8)])


def sample_base(table: dict, dims: list[str], n: int, seed: int | None) -> list[dict]:
    """Muestrea n perfiles base (solo las dims de la tabla) de la conjunta ajustada."""
    rng = random.Random(seed)
    keys = list(table.keys())
    weights = [table[k] for k in keys]
    chosen = rng.choices(keys, weights=weights, k=n)
    return [dict(zip(dims, key)) for key in chosen]


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #

def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="IPF: ajusta una tabla conjunta a marginales objetivo.")
    p.add_argument("--joint", required=True, help="CSV de tabla conjunta (enaho_loader.py)")
    p.add_argument("--targets", required=True, help="JSON {dim: {cat: prob}}")
    p.add_argument("--weight-col", default="peso_expandido", help="columna de peso en --joint")
    p.add_argument("--max-iter", type=int, default=200)
    p.add_argument("--tol", type=float, default=1e-8)
    p.add_argument("--out-fitted", help="CSV de salida con la tabla ajustada")
    p.add_argument("--sample", type=int, help="muestrea N perfiles base de la conjunta ajustada")
    p.add_argument("--seed", type=int, default=None, help="semilla de muestreo (reproducibilidad)")
    p.add_argument("--out-sample", help="CSV de salida de la muestra base")
    args = p.parse_args(argv)

    for path in (args.joint, args.targets):
        if not os.path.exists(path):
            p.error(f"no existe el archivo: {path}")

    dims, table = load_joint(args.joint, weight_col=args.weight_col)
    targets = load_targets(args.targets)
    print(f"[ok] semilla: {len(table)} celdas · dims={dims}", file=sys.stderr)

    antes = marginales_normalizadas(table, dims)
    fitted, diag = ipf(table, dims, targets, max_iter=args.max_iter, tol=args.tol)
    despues = marginales_normalizadas(fitted, dims)

    print("\n== Marginales (dim ajustada): objetivo | antes -> despues ==", file=sys.stderr)
    for d in diag["dims_ajustadas"]:
        for cat, tprob in sorted(targets[d].items()):
            print(f"  {d}={cat}: obj={tprob:.3f} | {antes[d].get(cat,0):.3f} -> "
                  f"{despues[d].get(cat,0):.3f}", file=sys.stderr)

    if args.out_fitted:
        export_fitted(fitted, dims, args.out_fitted)
        print(f"[ok] tabla ajustada -> {args.out_fitted}", file=sys.stderr)

    if args.sample:
        muestra = sample_base(fitted, dims, args.sample, args.seed)
        if args.out_sample:
            with open(args.out_sample, "w", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=dims)
                w.writeheader()
                w.writerows(muestra)
            print(f"[ok] muestra base ({len(muestra)}) -> {args.out_sample}", file=sys.stderr)
        else:
            w = csv.DictWriter(sys.stdout, fieldnames=dims)
            w.writeheader()
            w.writerows(muestra)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
