#!/usr/bin/env python3
"""
enaho_loader.py — Carga, cruza y resume microdatos de ENAHO (INEI) para sembrar
la generacion de usuarios sinteticos de `lapuerta`.

Objetivo
--------
ENAHO se descarga por modulos (CSV) desde https://proyectos.inei.gob.pe/microdatos/.
Este script:
  1) lee uno o varios modulos en CSV,
  2) los cruza por la llave de hogar/persona (conglome+vivienda+hogar[+codperso]),
  3) aplica el FACTOR DE EXPANSION (pesos muestrales; sin esto las cifras se sesgan),
  4) recodifica los codigos crudos de ENAHO a las categorias de `lapuerta`
     (region, educacion, nse-proxy, situacion_laboral-proxy, tenencia_vivienda),
  5) exporta una TABLA CONJUNTA ponderada (CSV) + marginales (JSON) listas para
     sembrar un IPF/copula en el generador (mejora #1 de la revision de literatura).

Formatos: usa solo la libreria estandar y consume CSV (descarga directa de INEI).
Si en el futuro instalan pandas+pyreadstat, hay un gancho opcional para .dta/.sav.

Modulos ENAHO relevantes (referencia)
-------------------------------------
  Modulo 100  Caracteristicas de la Vivienda   -> tenencia_vivienda (p105a)
  Modulo 200  Miembros del Hogar               -> dependientes / composicion
  Modulo 300  Educacion                        -> nivel educativo (p301a)
  Modulo 500  Empleo e Ingresos                -> situacion_laboral (ocu500, p507, ...)
  Sumaria     Agregados de gasto/ingreso       -> nse-proxy (gasto per capita)

Llaves: conglome + vivienda + hogar  (hogar); + codperso (persona).
Factor: por defecto `factor07` (anual). El modulo 500 suele traer `fac500a`.
Geografia: `dominio` (1-8) -> macro-region; `estrato` -> urbano/rural.

Uso
---
  # Resumen ponderado de un modulo ya recodificado
  python enaho_loader.py --modulo300 enaho2024_mod300.csv --dim region --dim educacion

  # Cruce hogar (vivienda + sumaria) -> tabla conjunta region x nse_proxy x tenencia
  python enaho_loader.py --modulo100 mod100.csv --sumaria sumaria.csv \
         --dim region --dim nse_proxy --dim tenencia_vivienda \
         --out-joint joint.csv --out-marginales marginales.json

ADVERTENCIA: nse_proxy (quintiles de gasto per capita) NO es APEIM; es una
aproximacion. situacion_laboral usa una regla simplificada de formalidad; refinar
con p507/contrato/planilla segun el diccionario del anio.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from collections import defaultdict

# --------------------------------------------------------------------------- #
# Lectura de CSV de ENAHO
# --------------------------------------------------------------------------- #
# Los CSV del INEI suelen venir en latin-1 y con nombres de columna en minuscula
# o mayuscula. Normalizamos las claves a minuscula.

def read_csv_module(path: str) -> list[dict]:
    """Lee un modulo CSV de ENAHO; normaliza nombres de columna a minuscula."""
    encodings = ("utf-8-sig", "latin-1")
    last_err = None
    for enc in encodings:
        try:
            with open(path, "r", encoding=enc, newline="") as f:
                # autodeteccion simple de delimitador (INEI usa , o ;)
                sample = f.read(4096)
                f.seek(0)
                delim = ";" if sample.count(";") > sample.count(",") else ","
                reader = csv.DictReader(f, delimiter=delim)
                rows = []
                for r in reader:
                    rows.append({(k or "").strip().lower(): (v.strip() if isinstance(v, str) else v)
                                 for k, v in r.items()})
                return rows
        except UnicodeDecodeError as e:
            last_err = e
    raise last_err  # type: ignore


HOGAR_KEYS = ("conglome", "vivienda", "hogar")
PERSONA_KEYS = HOGAR_KEYS + ("codperso",)


def _key(row: dict, keys) -> tuple:
    return tuple(str(row.get(k, "")).strip() for k in keys)


def merge_modules(base: list[dict], other: list[dict], keys=HOGAR_KEYS,
                  suffix: str = "") -> list[dict]:
    """Une `other` sobre `base` por las llaves dadas (left join)."""
    index = {}
    for r in other:
        index[_key(r, keys)] = r
    merged = []
    for r in base:
        o = index.get(_key(r, keys), {})
        m = dict(r)
        for k, v in o.items():
            if k in keys:
                continue
            m[(k + suffix) if (suffix and k in m) else k] = v
        merged.append(m)
    return merged


# --------------------------------------------------------------------------- #
# Factor de expansion
# --------------------------------------------------------------------------- #

def get_factor(row: dict, factor_cols=("factor07", "fac500a", "factora07", "factorpob")) -> float:
    for c in factor_cols:
        v = row.get(c)
        if v not in (None, "", "."):
            try:
                return float(str(v).replace(",", "."))
            except ValueError:
                continue
    return 1.0  # sin factor: conteo simple (avisar al usuario)


# --------------------------------------------------------------------------- #
# Recodificaciones ENAHO -> categorias lapuerta
# --------------------------------------------------------------------------- #
# Cada funcion devuelve la categoria de lapuerta o None si falta el dato.

def recode_region(row: dict) -> str | None:
    """`dominio` (1-8) -> macro-region de lapuerta.
    1 Costa Norte, 2 Costa Centro, 3 Costa Sur, 4 Sierra Norte,
    5 Sierra Centro, 6 Sierra Sur, 7 Selva, 8 Lima Metropolitana."""
    d = row.get("dominio")
    try:
        d = int(float(d))
    except (TypeError, ValueError):
        return None
    if d == 8:
        return "Lima_Metropolitana"
    if d in (1, 2, 3):
        return "Resto_Costa"
    if d in (4, 5, 6):
        return "Sierra"
    if d == 7:
        return "Selva"
    return None


def recode_area(row: dict) -> str | None:
    """`estrato` 1-5 -> urbano; 6-8 -> rural (centros poblados pequenos/rural)."""
    e = row.get("estrato")
    try:
        e = int(float(e))
    except (TypeError, ValueError):
        return None
    return "urbano" if e <= 5 else "rural"


def recode_generacion(row: dict) -> str | None:
    """`p208a` (edad en años) -> cohorte generacional (solo adultos 18+).
    Gen Z 18-27, Millennial 28-43, Gen X 44-59, Boomer 60+."""
    a = row.get("p208a")
    try:
        a = int(float(a))
    except (TypeError, ValueError):
        return None
    if a < 18:
        return None
    if a <= 27:
        return "Gen_Z_18_27"
    if a <= 43:
        return "Millennial_28_43"
    if a <= 59:
        return "Gen_X_44_59"
    return "Boomer_60_mas"


def recode_educacion(row: dict) -> str | None:
    """`p301a` (nivel educativo) -> proxy de educacion_financiera baja/media/alta.
    1 sin nivel, 2 inicial, 3 primaria incompleta, 4 primaria completa,
    5 secundaria incompleta, 6 secundaria completa, 7 sup. no univ. incompleta,
    8 sup. no univ. completa, 9 sup. univ. incompleta, 10 sup. univ. completa,
    11 postgrado. (Proxy: a mayor nivel, mayor educacion financiera.)"""
    v = row.get("p301a")
    try:
        n = int(float(v))
    except (TypeError, ValueError):
        return None
    if n <= 4:
        return "baja"
    if n <= 8:
        return "media"
    return "alta"


def recode_tenencia_vivienda(row: dict) -> str | None:
    """`p105a` (tenencia de la vivienda) -> categorias de tenencia.
    1 alquilada, 2 propia (pagando), 3 propia (totalmente pagada),
    4 propia por invasion, 5 cedida por otro hogar/institucion, 6 otra."""
    v = row.get("p105a")
    try:
        n = int(float(v))
    except (TypeError, ValueError):
        return None
    if n in (2, 3):
        return "propietario_formal"
    if n == 4:
        return "propietario_informal"
    if n == 1:
        return "alquila"
    if n in (5, 6):
        return "cedida"
    return None


def recode_situacion_laboral(row: dict) -> str | None:
    """Proxy simplificado con el modulo 500.
    ocu500: 1 ocupado, 2 desocupado abierto, 3 desocupado oculto, 4 inactivo.
    Formalidad (proxy): p507 (categoria ocupacional) + tenencia de contrato.
      - empleado/obrero con contrato o en planilla -> formal_dependiente
      - independiente / trabajador del hogar -> independiente_microemprendedor
      - resto de ocupados sin contrato -> informal
    NOTA: refinar con el diccionario del anio (p511a contrato, planilla, RUC)."""
    ocu = row.get("ocu500")
    try:
        ocu = int(float(ocu))
    except (TypeError, ValueError):
        return None
    if ocu != 1:
        return None  # solo poblacion ocupada para este eje
    p507 = row.get("p507")
    try:
        cat = int(float(p507))
    except (TypeError, ValueError):
        cat = None
    # p507: 1 empleador, 2 independiente, 3 empleado, 4 obrero,
    #       5 trab. del hogar, 6 trab. familiar no remunerado, 7 otro
    tiene_contrato = str(row.get("p511a", "")).strip() in ("1", "2", "3", "4")
    if cat in (3, 4) and tiene_contrato:
        return "formal_dependiente"
    if cat in (1, 2):
        return "independiente_microemprendedor"
    return "informal"


# --- nse_proxy: quintiles ponderados de gasto per capita (Sumaria) ----------

def compute_nse_proxy(rows: list[dict],
                      gasto_col: str = "gashog2d",
                      miembros_col: str = "mieperho",
                      factor_cols=("factor07",)) -> dict:
    """Asigna nse_proxy (A..E) por quintiles ponderados de gasto per capita.
    Devuelve {hogar_key: 'A'|'B'|'C'|'D'|'E'} (A = quintil mas alto)."""
    vals = []
    for r in rows:
        try:
            g = float(str(r.get(gasto_col, "")).replace(",", "."))
            m = float(str(r.get(miembros_col, "")).replace(",", "."))
            if m <= 0:
                continue
            pc = g / m
        except (TypeError, ValueError):
            continue
        w = get_factor(r, factor_cols)
        vals.append((pc, w, _key(r, HOGAR_KEYS)))
    if not vals:
        return {}
    vals.sort(key=lambda t: t[0])
    total_w = sum(w for _, w, _ in vals)
    # cortes en 20/40/60/80% de la poblacion ponderada
    cutpoints = [0.2, 0.4, 0.6, 0.8]
    labels_low_to_high = ["E", "D", "C", "B", "A"]
    out = {}
    cum = 0.0
    ci = 0
    for pc, w, k in vals:
        cum += w
        frac = cum / total_w
        while ci < len(cutpoints) and frac > cutpoints[ci]:
            ci += 1
        out[k] = labels_low_to_high[ci]
    return out


# Mapa de recodificadores por dimension de lapuerta
RECODERS = {
    "region": recode_region,
    "area": recode_area,
    "generacion": recode_generacion,
    "educacion": recode_educacion,
    "tenencia_vivienda": recode_tenencia_vivienda,
    "situacion_laboral": recode_situacion_laboral,
}


# --------------------------------------------------------------------------- #
# Crosstab ponderado y exportacion
# --------------------------------------------------------------------------- #

def weighted_crosstab(rows: list[dict], dims: list[str],
                      nse_map: dict | None = None,
                      factor_cols=("factor07",)) -> dict:
    """Tabla conjunta ponderada sobre `dims`. Devuelve {tupla_categorias: peso}."""
    table = defaultdict(float)
    for r in rows:
        key = []
        ok = True
        for d in dims:
            if d == "nse_proxy":
                cat = nse_map.get(_key(r, HOGAR_KEYS)) if nse_map else None
            elif d in RECODERS:
                cat = RECODERS[d](r)
            else:  # columna ya recodificada presente en la fila
                cat = r.get(d) or None
            if cat is None:
                ok = False
                break
            key.append(cat)
        if not ok:
            continue
        table[tuple(key)] += get_factor(r, factor_cols)
    return dict(table)


def normalize_marginales(table: dict, dims: list[str]) -> dict:
    """Marginales 1-D normalizadas por dimension (formato listo para el schema)."""
    out = {d: defaultdict(float) for d in dims}
    total = sum(table.values()) or 1.0
    for key, w in table.items():
        for d, cat in zip(dims, key):
            out[d][cat] += w
    return {d: {c: round(v / total, 4) for c, v in sorted(cats.items())}
            for d, cats in out.items()}


def export_joint_csv(table: dict, dims: list[str], path: str) -> None:
    total = sum(table.values()) or 1.0
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(list(dims) + ["peso_expandido", "proporcion"])
        for key, weight in sorted(table.items(), key=lambda kv: -kv[1]):
            w.writerow(list(key) + [round(weight, 2), round(weight / total, 6)])


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #

def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Carga/cruza microdatos ENAHO para sembrar lapuerta.")
    p.add_argument("--modulo100", help="CSV Modulo 100 (vivienda)")
    p.add_argument("--modulo200", help="CSV Modulo 200 (miembros del hogar)")
    p.add_argument("--modulo300", help="CSV Modulo 300 (educacion)")
    p.add_argument("--modulo500", help="CSV Modulo 500 (empleo)")
    p.add_argument("--sumaria", help="CSV Sumaria (agregados de gasto)")
    p.add_argument("--dim", action="append", default=[], dest="dims",
                   help="dimension de la tabla (repetible): region, area, educacion, "
                        "nse_proxy, tenencia_vivienda, situacion_laboral")
    p.add_argument("--factor", default="factor07", help="columna de factor de expansion")
    p.add_argument("--out-joint", help="ruta CSV de la tabla conjunta")
    p.add_argument("--out-marginales", help="ruta JSON de marginales normalizadas")
    args = p.parse_args(argv)

    if not args.dims:
        p.error("indica al menos una --dim")
    factor_cols = (args.factor, "factor07", "fac500a", "factora07")

    # Base = primer modulo disponible (preferimos persona si hay 300/500)
    base = None
    base_keys = HOGAR_KEYS
    loaded = {}
    for name, path in [("m100", args.modulo100), ("m200", args.modulo200),
                       ("m300", args.modulo300), ("m500", args.modulo500),
                       ("sum", args.sumaria)]:
        if path:
            if not os.path.exists(path):
                p.error(f"no existe el archivo: {path}")
            loaded[name] = read_csv_module(path)
            print(f"[ok] {name}: {len(loaded[name])} filas <- {path}", file=sys.stderr)

    if not loaded:
        p.error("provee al menos un modulo CSV")

    # Eleccion de base: persona-level si hay 300/500; si no, hogar-level
    if "m300" in loaded:
        base, base_keys = loaded["m300"], PERSONA_KEYS
    elif "m500" in loaded:
        base, base_keys = loaded["m500"], PERSONA_KEYS
    elif "m100" in loaded:
        base, base_keys = loaded["m100"], HOGAR_KEYS
    else:
        base = next(iter(loaded.values()))

    # Cruces hogar-level sobre la base
    for name in ("m100", "m500", "sum"):
        if name in loaded and loaded[name] is not base:
            base = merge_modules(base, loaded[name], keys=HOGAR_KEYS)

    # nse_proxy desde sumaria si se pide
    nse_map = None
    if "nse_proxy" in args.dims:
        if "sum" not in loaded:
            p.error("nse_proxy requiere --sumaria")
        nse_map = compute_nse_proxy(loaded["sum"], factor_cols=factor_cols)
        print(f"[ok] nse_proxy asignado a {len(nse_map)} hogares (quintiles ponderados)",
              file=sys.stderr)

    table = weighted_crosstab(base, args.dims, nse_map=nse_map, factor_cols=factor_cols)
    if not table:
        print("[!] tabla vacia: revisa nombres de columnas/recodificacion vs diccionario del anio.",
              file=sys.stderr)
        return 1

    marg = normalize_marginales(table, args.dims)
    print("\n== Marginales ponderadas ==", file=sys.stderr)
    print(json.dumps(marg, ensure_ascii=False, indent=2))

    if args.out_joint:
        export_joint_csv(table, args.dims, args.out_joint)
        print(f"[ok] tabla conjunta -> {args.out_joint}", file=sys.stderr)
    if args.out_marginales:
        with open(args.out_marginales, "w", encoding="utf-8") as f:
            json.dump(marg, f, ensure_ascii=False, indent=2)
        print(f"[ok] marginales -> {args.out_marginales}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
