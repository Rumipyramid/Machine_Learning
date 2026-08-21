#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
finanzas.py — Calculadora de finanzas personales del repo (solo stdlib).

Lee los CSV de `finanzas/movimientos/` y responde tres preguntas:

  1. ¿Cómo cierra el mes?            -> `resumen`
  2. ¿Cuánto cuesta realmente la deuda y cuándo se acaba?  -> `deuda`
  3. ¿Qué pasa si este mes se repite? -> `proyeccion`

Uso:
    python finanzas.py resumen --mes 2026-08
    python finanzas.py deuda --saldo 10000 --cuota 3000 --tcea 0 40 60 90
    python finanzas.py proyeccion --mes 2026-08 --meses 12 --tcea 60
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
MOV_DIR = os.path.join(BASE, "movimientos")

TIPOS = ("ingreso", "fijo", "variable", "deuda")

# Categorías que un presupuesto completo debería tener registradas. Si un mes no
# las tiene, el resumen las marca como HUECO — no como cero. La diferencia
# importa: un cero dice "no gasté", un hueco dice "no sé cuánto gasté".
CATEGORIAS_BASE = ("alimentacion", "transporte", "servicios", "comunicaciones")


# ---------------------------------------------------------------- utilidades

def soles(x: float, ancho: int = 0) -> str:
    """Formatea un monto en soles. Peru usa coma para miles."""
    s = f"S/ {x:,.0f}"
    return s.rjust(ancho) if ancho else s


def tasa_mensual(tcea_pct: float) -> float:
    """Convierte una TCEA (% anual efectiva) a tasa efectiva mensual."""
    return (1.0 + tcea_pct / 100.0) ** (1.0 / 12.0) - 1.0


def leer_mes(mes: str) -> list[dict]:
    ruta = os.path.join(MOV_DIR, f"{mes}.csv")
    if not os.path.exists(ruta):
        disponibles = sorted(
            f[:-4] for f in os.listdir(MOV_DIR) if f.endswith(".csv")
        ) if os.path.isdir(MOV_DIR) else []
        sys.exit(
            f"No existe {ruta}\n"
            f"Meses registrados: {', '.join(disponibles) or '(ninguno)'}"
        )
    filas = []
    with open(ruta, newline="", encoding="utf-8") as fh:
        for i, fila in enumerate(csv.DictReader(fh), start=2):
            if not (fila.get("concepto") or "").strip():
                continue
            tipo = (fila.get("tipo") or "").strip()
            if tipo not in TIPOS:
                sys.exit(f"{ruta}:{i} tipo invalido '{tipo}' (esperado: {'/'.join(TIPOS)})")
            try:
                fila["monto"] = float(fila["monto"])
            except (KeyError, TypeError, ValueError):
                sys.exit(f"{ruta}:{i} monto invalido para '{fila.get('concepto')}'")
            fila["tipo"] = tipo
            fila["categoria"] = (fila.get("categoria") or "").strip()
            filas.append(fila)
    return filas


# ------------------------------------------------------------------ resumen

def calcular_resumen(mes: str) -> dict:
    filas = leer_mes(mes)

    por_tipo = {t: [f for f in filas if f["tipo"] == t] for t in TIPOS}
    total = {t: sum(f["monto"] for f in por_tipo[t]) for t in TIPOS}

    ingresos = total["ingreso"]
    fijos = -total["fijo"]          # se guardan negativos, aqui como magnitud
    variables = -total["variable"]
    deuda = -total["deuda"]

    balance = ingresos - fijos - variables - deuda
    # Lo que queda para pagar deuda una vez cubierta la vida corriente.
    capacidad_pago = ingresos - fijos - variables

    categorias_presentes = {f["categoria"] for f in filas}
    huecos = [c for c in CATEGORIAS_BASE if c not in categorias_presentes]
    estimados = [f for f in filas if (f.get("estado") or "").strip() == "estimado"]

    return {
        "mes": mes,
        "movimientos": filas,
        "por_tipo": por_tipo,
        "ingresos": ingresos,
        "fijos": fijos,
        "variables": variables,
        "servicio_deuda": deuda,
        "balance": balance,
        "capacidad_pago": capacidad_pago,
        "ratio_deuda_ingreso": (deuda / ingresos) if ingresos else 0.0,
        "ratio_fijos_ingreso": (fijos / ingresos) if ingresos else 0.0,
        "huecos": huecos,
        "estimados": [f["concepto"] for f in estimados],
    }


def imprimir_resumen(r: dict) -> None:
    print(f"\n{'=' * 62}")
    print(f"  RESUMEN {r['mes']}")
    print(f"{'=' * 62}\n")

    for tipo, etiqueta in (
        ("ingreso", "INGRESOS"),
        ("fijo", "GASTOS FIJOS"),
        ("variable", "GASTOS VARIABLES"),
        ("deuda", "SERVICIO DE DEUDA"),
    ):
        filas = r["por_tipo"][tipo]
        subtotal = sum(f["monto"] for f in filas)
        print(f"{etiqueta}")
        if not filas:
            print("  (sin movimientos registrados)")
        for f in sorted(filas, key=lambda x: -abs(x["monto"])):
            marca = " ~" if (f.get("estado") or "").strip() == "estimado" else "  "
            print(f" {marca} {f['concepto']:<28} {soles(f['monto'], 12)}")
        print(f"    {'':<28} {soles(subtotal, 12)}  <- subtotal\n")

    print(f"{'-' * 62}")
    print(f"  Balance del mes            {soles(r['balance'], 12)}")
    print(f"{'-' * 62}\n")

    print("INDICADORES")
    print(f"  Capacidad de pago (segun registrado) {soles(r['capacidad_pago'], 8)}")
    print(f"  Servicio de deuda comprometido       {soles(r['servicio_deuda'], 8)}")
    brecha = r["capacidad_pago"] - r["servicio_deuda"]
    print(f"  Brecha (capacidad - servicio)        {soles(brecha, 8)}")
    print(f"  Servicio de deuda / ingresos         {r['ratio_deuda_ingreso']:>7.0%}   (sano: < 30%)")
    print(f"  Fijos / ingresos                     {r['ratio_fijos_ingreso']:>7.0%}   (sano: < 50%)")

    if r["huecos"] or r["estimados"]:
        print(f"\n{'!' * 62}")
        if r["huecos"]:
            print("HUECOS DEL PRESUPUESTO — categorias sin ningun movimiento:")
            for c in r["huecos"]:
                print(f"  - {c}")
            print("  El balance de arriba NO las incluye: el deficit real es mayor.")
        if r["estimados"]:
            print(f"Montos estimados (no confirmados): {', '.join(r['estimados'])}")
        print(f"{'!' * 62}")
    print()


# -------------------------------------------------------------------- deuda

def amortizar(saldo: float, cuota: float, tcea_pct: float,
              extra_mensual: float = 0.0, max_meses: int = 600) -> dict:
    """
    Amortiza `saldo` con `cuota` fija a la `tcea_pct` dada.

    Orden dentro del mes: se devengan intereses, se carga el consumo nuevo del
    mes (`extra_mensual` — p.ej. el deficit del presupuesto que termina
    pagandose con la tarjeta) y recien entonces se aplica la cuota.

    Devuelve {'meses', 'total_pagado', 'intereses', 'filas'}, o
    {'perpetua': True, 'motivo': ...} si el saldo deja de bajar.
    """
    i = tasa_mensual(tcea_pct)
    filas = []
    total_pagado = 0.0
    total_interes = 0.0
    mes = 0

    while saldo > 0.005 and mes < max_meses:
        interes = saldo * i
        bruto = saldo + interes + extra_mensual
        pago = min(cuota, bruto)
        nuevo_saldo = bruto - pago

        # Sin progreso: el saldo no baja. Distinguimos los dos motivos porque
        # exigen decisiones distintas (renegociar tasa vs. cerrar el deficit).
        if nuevo_saldo >= saldo - 1e-9 and nuevo_saldo > 0.005:
            motivo = ("la cuota no cubre ni los intereses: la deuda crece sola"
                      if cuota <= interes else
                      "la cuota cubre los intereses pero no el consumo nuevo: "
                      "el saldo se estanca y nunca se cancela")
            return {"perpetua": True, "motivo": motivo, "meses": None,
                    "filas": filas}

        mes += 1
        saldo = nuevo_saldo
        total_pagado += pago
        total_interes += interes
        filas.append({"mes": mes, "interes": interes, "consumo": extra_mensual,
                      "pago": pago, "saldo": saldo})

    if saldo > 0.005:
        return {"perpetua": True, "meses": None, "filas": filas,
                "motivo": f"no se cancela en {max_meses} meses"}

    return {
        "perpetua": False,
        "meses": mes,
        "total_pagado": total_pagado,
        "intereses": total_interes,
        "filas": filas,
    }


def escenarios_deuda(saldo: float, cuota: float, tceas: list[float],
                     extra_mensual: float = 0.0) -> list[dict]:
    out = []
    for t in tceas:
        r = amortizar(saldo, cuota, t, extra_mensual)
        out.append({
            "tcea": t,
            "meses": r["meses"],
            "total_pagado": None if r["perpetua"] else r["total_pagado"],
            "intereses": None if r["perpetua"] else r["intereses"],
            "perpetua": r["perpetua"],
            "motivo": r.get("motivo"),
        })
    return out


def imprimir_deuda(saldo: float, cuota: float, esc: list[dict],
                   extra_mensual: float) -> None:
    print(f"\n{'=' * 62}")
    print(f"  DEUDA — saldo {soles(saldo)} · cuota {soles(cuota)}/mes")
    if extra_mensual:
        print(f"  + {soles(extra_mensual)}/mes de consumo nuevo cargado a la deuda")
    print(f"{'=' * 62}\n")
    print(f"  {'TCEA':>6}  {'Meses':>6}  {'Total pagado':>14}  {'Intereses':>12}")
    print(f"  {'-' * 6}  {'-' * 6}  {'-' * 14}  {'-' * 12}")
    for e in esc:
        if e["perpetua"]:
            print(f"  {e['tcea']:>5.0f}%  {'nunca':>6}  {e['motivo']}")
        else:
            print(f"  {e['tcea']:>5.0f}%  {e['meses']:>6}  {soles(e['total_pagado'], 14)}"
                  f"  {soles(e['intereses'], 12)}")
    print("\n  La TCEA real esta en tu estado de cuenta. Registrala en deuda.csv:")
    print("  la diferencia entre 40% y 90% es plata, no un detalle.\n")


# --------------------------------------------------------------- proyeccion

def imprimir_proyeccion(r: dict, saldo: float, cuota: float, tcea: float,
                        meses: int) -> None:
    """
    Proyecta repitiendo la estructura del mes. Si el mes cierra en negativo,
    ese deficit se carga a la tarjeta — que es lo que pasa en la practica.
    """
    extra = -min(0.0, r["balance"])
    i = tasa_mensual(tcea)

    print(f"\n{'=' * 62}")
    print(f"  PROYECCION — {meses} meses repitiendo la estructura de {r['mes']}")
    print(f"  TCEA {tcea:.0f}% · balance mensual {soles(r['balance'])}")
    if extra:
        print(f"  El deficit de {soles(extra)}/mes se carga a la tarjeta")
    print(f"{'=' * 62}\n")
    print(f"  {'Mes':>4}  {'Interes':>10}  {'Consumo':>10}  {'Pago':>10}  {'Saldo TC':>12}")
    print(f"  {'-' * 4}  {'-' * 10}  {'-' * 10}  {'-' * 10}  {'-' * 12}")

    s = saldo
    for m in range(1, meses + 1):
        interes = s * i
        bruto = s + interes + extra
        pago = min(cuota, bruto)
        s = bruto - pago
        print(f"  {m:>4}  {soles(interes, 10)}  {soles(extra, 10)}"
              f"  {soles(pago, 10)}  {soles(s, 12)}")
    print()


# --------------------------------------------------------------------- main

def main() -> None:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    p_res = sub.add_parser("resumen", help="Cierre del mes")
    p_res.add_argument("--mes", required=True, help="AAAA-MM, p.ej. 2026-08")
    p_res.add_argument("--json", action="store_true")

    p_deu = sub.add_parser("deuda", help="Escenarios de pago de la deuda")
    p_deu.add_argument("--saldo", type=float, required=True)
    p_deu.add_argument("--cuota", type=float, required=True)
    p_deu.add_argument("--tcea", type=float, nargs="+", default=[0, 40, 60, 90],
                       help="Una o varias TCEA en %% (default: 0 40 60 90)")
    p_deu.add_argument("--consumo-nuevo", type=float, default=0.0,
                       help="Gasto mensual que se sigue cargando a la deuda")
    p_deu.add_argument("--json", action="store_true")

    p_pro = sub.add_parser("proyeccion", help="Repetir el mes N veces")
    p_pro.add_argument("--mes", required=True)
    p_pro.add_argument("--saldo", type=float, required=True)
    p_pro.add_argument("--cuota", type=float, required=True)
    p_pro.add_argument("--tcea", type=float, default=60.0)
    p_pro.add_argument("--meses", type=int, default=12)

    a = p.parse_args()

    if a.cmd == "resumen":
        r = calcular_resumen(a.mes)
        if a.json:
            r.pop("movimientos"); r.pop("por_tipo")
            print(json.dumps(r, ensure_ascii=False, indent=2))
        else:
            imprimir_resumen(r)

    elif a.cmd == "deuda":
        esc = escenarios_deuda(a.saldo, a.cuota, a.tcea, a.consumo_nuevo)
        if a.json:
            print(json.dumps(esc, ensure_ascii=False, indent=2))
        else:
            imprimir_deuda(a.saldo, a.cuota, esc, a.consumo_nuevo)

    elif a.cmd == "proyeccion":
        r = calcular_resumen(a.mes)
        imprimir_proyeccion(r, a.saldo, a.cuota, a.tcea, a.meses)


if __name__ == "__main__":
    main()
