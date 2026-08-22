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
CALENDARIO = os.path.join(BASE, "calendario.csv")
PATRIMONIO = os.path.join(BASE, "patrimonio.csv")
DEUDA = os.path.join(BASE, "deuda.csv")

TIPOS = ("ingreso", "fijo", "variable", "deuda")

# Categorías que un presupuesto completo debería tener registradas. Si un mes no
# las tiene, el resumen las marca como HUECO — no como cero. La diferencia
# importa: un cero dice "no gasté", un hueco dice "no sé cuánto gasté".
CATEGORIAS_BASE = ("alimentacion", "transporte", "servicios", "comunicaciones")

# Categoria reservada: identifica la cuota de la tarjeta dentro del servicio de
# deuda. El resto de las filas `tipo=deuda` (adelantos, cuotas sin intereses) se
# tratan como pagos fijos que NO amortizan la tarjeta. Sin esta marca no se puede
# proyectar con una cuota distinta de la registrada.
CATEGORIA_TC = "tarjeta_credito"

# Categoria reservada: bolsa provisional para el gasto de vida mientras las
# categorias base no esten medidas. Cubre el hueco en el balance sin fingir que
# el dato existe — el resumen sigue avisando que falta el desglose.
CATEGORIA_RESERVA = "reserva_vida"

# Categoria reservada: dinero que entra al mes desde un activo propio (retiro de
# ahorros, venta de algo). Financia el mes pero NO es ingreso: si entra al
# denominador, los ratios mienten — un mes malo se ve sano por haber vaciado la
# cuenta de ahorros.
CATEGORIA_AHORRO = "ahorro"

# Plata que entra al mes pero no es ingreso: la propia (retiro de ahorros) y la
# ajena (un prestamo recibido). Ambas financian el mes; ninguna es capacidad de
# pago, asi que las dos quedan fuera del denominador de los ratios.
CATEGORIA_PRESTAMO = "prestamo_recibido"
CATEGORIAS_NO_INGRESO = (CATEGORIA_AHORRO, CATEGORIA_PRESTAMO)


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


def leer_calendario() -> dict:
    """Eventos de ingreso/egreso irregulares ya conocidos, indexados por mes."""
    if not os.path.exists(CALENDARIO):
        return {}
    cal = {}
    with open(CALENDARIO, newline="", encoding="utf-8") as fh:
        for i, fila in enumerate(csv.DictReader(fh), start=2):
            if not (fila.get("concepto") or "").strip():
                continue
            try:
                monto = float(fila["monto"])
            except (KeyError, TypeError, ValueError):
                sys.exit(f"{CALENDARIO}:{i} monto invalido para '{fila.get('concepto')}'")
            cal.setdefault(fila["mes"].strip(), []).append({
                "concepto": fila["concepto"].strip(),
                "monto": monto,
                "estado": (fila.get("estado") or "").strip(),
            })
    return cal


def meses_desde(mes: str, n: int) -> list[str]:
    y, m = (int(x) for x in mes.split("-"))
    out = []
    for _ in range(n):
        out.append(f"{y:04d}-{m:02d}")
        m += 1
        if m > 12:
            m, y = 1, y + 1
    return out


def leer_patrimonio(tc: float) -> list[dict]:
    """Activos, convertidos a soles al tipo de cambio dado."""
    if not os.path.exists(PATRIMONIO):
        return []
    filas = []
    with open(PATRIMONIO, newline="", encoding="utf-8") as fh:
        for i, f in enumerate(csv.DictReader(fh), start=2):
            if not (f.get("activo") or "").strip():
                continue
            try:
                monto = float(f["monto"])
            except (KeyError, TypeError, ValueError):
                sys.exit(f"{PATRIMONIO}:{i} monto invalido para '{f.get('activo')}'")
            moneda = (f.get("moneda") or "PEN").strip().upper()
            filas.append({
                "activo": f["activo"].strip(),
                "categoria": (f.get("categoria") or "").strip(),
                "moneda": moneda,
                "monto": monto,
                "pen": monto * tc if moneda == "USD" else monto,
                "costo": float(f["costo"]) if (f.get("costo") or "").strip() else None,
                "liquidez": (f.get("liquidez") or "baja").strip(),
                "confianza": (f.get("confianza_valuacion") or "").strip(),
                "nota": (f.get("nota") or "").strip(),
            })
    return filas


def leer_pasivos() -> list[dict]:
    """Saldo de inicio del mes mas reciente registrado en deuda.csv."""
    if not os.path.exists(DEUDA):
        return []
    por_acreedor = {}
    with open(DEUDA, newline="", encoding="utf-8") as fh:
        for f in csv.DictReader(fh):
            if not (f.get("instrumento") or "").strip():
                continue
            crudo = (f.get("saldo_inicial") or "").strip()
            tcea = (f.get("tcea") or "").strip()
            por_acreedor[f["instrumento"].strip()] = {
                "instrumento": f["instrumento"].strip(),
                "saldo": float(crudo) if crudo else None,
                "tcea": float(tcea) if tcea else None,
                "estado": (f.get("estado") or "vigente").strip(),
                "nota": (f.get("nota") or "").strip(),
            }
    return list(por_acreedor.values())


# ------------------------------------------------------------------ resumen

def calcular_resumen(mes: str) -> dict:
    filas = leer_mes(mes)

    por_tipo = {t: [f for f in filas if f["tipo"] == t] for t in TIPOS}
    total = {t: sum(f["monto"] for f in por_tipo[t]) for t in TIPOS}

    ingresos = total["ingreso"]
    desahorro = sum(f["monto"] for f in por_tipo["ingreso"]
                    if f["categoria"] in CATEGORIAS_NO_INGRESO)
    ingresos_propios = ingresos - desahorro
    fijos = -total["fijo"]          # se guardan negativos, aqui como magnitud
    variables = -total["variable"]
    deuda = -total["deuda"]

    balance = ingresos - fijos - variables - deuda
    # Lo que queda para pagar deuda una vez cubierta la vida corriente.
    capacidad_pago = ingresos - fijos - variables

    deudas = por_tipo["deuda"]
    cuota_tc = -sum(f["monto"] for f in deudas if f["categoria"] == CATEGORIA_TC)
    otros_deuda = -sum(f["monto"] for f in deudas if f["categoria"] != CATEGORIA_TC)
    if deudas and cuota_tc == 0:
        print(f"AVISO: ningun movimiento de deuda tiene categoria '{CATEGORIA_TC}'.\n"
              f"       La proyeccion tratara los {soles(otros_deuda)} de servicio de deuda\n"
              f"       como pagos que no amortizan la tarjeta.", file=sys.stderr)

    categorias_presentes = {f["categoria"] for f in filas}
    huecos = [c for c in CATEGORIAS_BASE if c not in categorias_presentes]
    reserva = -sum(f["monto"] for f in filas if f["categoria"] == CATEGORIA_RESERVA)
    estimados = [f for f in filas if (f.get("estado") or "").strip() == "estimado"]

    return {
        "mes": mes,
        "movimientos": filas,
        "por_tipo": por_tipo,
        "ingresos": ingresos,
        "fijos": fijos,
        "variables": variables,
        "servicio_deuda": deuda,
        "cuota_tc": cuota_tc,
        "otros_deuda": otros_deuda,
        "balance": balance,
        "capacidad_pago": capacidad_pago,
        "desahorro": desahorro,
        "ingresos_propios": ingresos_propios,
        "ratio_deuda_ingreso": (deuda / ingresos_propios) if ingresos_propios else 0.0,
        "ratio_fijos_ingreso": (fijos / ingresos_propios) if ingresos_propios else 0.0,
        "huecos": huecos,
        "reserva_vida": reserva,
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

    if r["desahorro"]:
        print(f"  De ese balance, {soles(r['desahorro'])} no son ingresos: son ahorros")
        print(f"  propios o plata prestada. El mes cuadra, pero no con lo que ganas.\n")

    print("INDICADORES")
    print(f"  Capacidad de pago (segun registrado) {soles(r['capacidad_pago'], 8)}")
    print(f"  Servicio de deuda comprometido       {soles(r['servicio_deuda'], 8)}")
    brecha = r["capacidad_pago"] - r["servicio_deuda"]
    print(f"  Brecha (capacidad - servicio)        {soles(brecha, 8)}")
    print(f"  Servicio de deuda / ingresos         {r['ratio_deuda_ingreso']:>7.0%}   (sano: < 30%)")
    if r["desahorro"]:
        print(f"  (ratios sobre ingresos propios de {soles(r['ingresos_propios'])}, sin contar")
        print(f"   ahorros ni prestamos)")
    print(f"  Fijos / ingresos                     {r['ratio_fijos_ingreso']:>7.0%}   (sano: < 50%)")

    if r["huecos"] or r["estimados"]:
        print(f"\n{'!' * 62}")
        if r["huecos"] and r["reserva_vida"]:
            print(f"GASTO DE VIDA SIN DESGLOSAR — cubierto provisionalmente con una")
            print(f"reserva estimada de {soles(r['reserva_vida'])}. Sin medir:")
            for c in r["huecos"]:
                print(f"  - {c}")
            print("  El balance cuadra, pero con un supuesto. Mide el gasto real y")
            print("  reemplaza la reserva por las categorias con su monto.")
        elif r["huecos"]:
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

def proyectar(r: dict, saldo_tc: float, cuota: float, tcea: float, meses: int,
              variables: float | None = None, otros_deuda_hasta: str | None = None,
              destino_extra: str = "deuda") -> list[dict]:
    """
    Proyecta mes a mes desde el mes base de `r`, aplicando el calendario de
    ingresos irregulares (CTS, gratificacion) en el mes que corresponde.

    Modela lo que pasa de verdad cuando el mes no alcanza: la cuota se paga
    igual, pero el faltante vuelve a la tarjeta.
    """
    cal = leer_calendario()
    i = tasa_mensual(tcea)
    var = r["variables"] if variables is None else variables
    otros_deuda = r["otros_deuda"]   # adelanto y cuotas sin intereses: no son la TC

    filas = []
    saldo, caja = saldo_tc, 0.0

    for mes in meses_desde(r["mes"], meses):
        eventos = cal.get(mes, [])
        extra = sum(e["monto"] for e in eventos)
        paga_otros = otros_deuda if (otros_deuda_hasta is None or mes <= otros_deuda_hasta) else 0.0

        disponible = r["ingresos"] + extra - r["fijos"] - var - paga_otros

        interes = saldo * i
        bruto = saldo + interes
        deseado = cuota + (extra if destino_extra == "deuda" else 0.0)
        pago = min(deseado, bruto)
        faltante = max(0.0, pago - disponible)     # lo que no alcanza vuelve a la TC
        saldo = bruto - pago + faltante
        caja += disponible - pago + faltante

        filas.append({
            "mes": mes, "extra": extra, "eventos": [e["concepto"] for e in eventos],
            "otros_deuda": paga_otros, "disponible": disponible, "interes": interes,
            "pago": pago, "faltante": faltante, "saldo": saldo, "caja": caja,
        })
    return filas


def imprimir_proyeccion(filas: list[dict], r: dict, tcea: float, var: float,
                        destino_extra: str) -> None:
    print(f"\n{'=' * 78}")
    print(f"  PROYECCION desde {r['mes']} — TCEA {tcea:.0f}% · "
          f"gasto variable asumido {soles(var)}/mes")
    print(f"  Ingreso extraordinario (CTS, gratificacion) -> {destino_extra.upper()}")
    print(f"{'=' * 78}\n")
    print(f"  {'Mes':>8}  {'Extra':>9}  {'Disponible':>11}  {'Pago TC':>10}"
          f"  {'A la TC':>9}  {'Saldo TC':>10}  {'Caja':>10}")
    print(f"  {'-' * 8}  {'-' * 9}  {'-' * 11}  {'-' * 10}  {'-' * 9}  {'-' * 10}  {'-' * 10}")

    libre = None
    for f in filas:
        extra_s = soles(f["extra"], 9) if f["extra"] else " " * 9
        falt_s = soles(f["faltante"], 9) if f["faltante"] > 0.5 else " " * 9
        print(f"  {f['mes']:>8}  {extra_s}  {soles(f['disponible'], 11)}"
              f"  {soles(f['pago'], 10)}  {falt_s}  {soles(f['saldo'], 10)}"
              f"  {soles(f['caja'], 10)}")
        if libre is None and f["saldo"] <= 0.5:
            libre = f["mes"]
        if f["eventos"]:
            print(f"  {'':>8}  ({', '.join(f['eventos'])})")

    print()
    if libre:
        print(f"  Tarjeta en cero: {libre}")
    else:
        print(f"  La tarjeta NO se cancela en el horizonte proyectado "
              f"(saldo final {soles(filas[-1]['saldo'])})")
    print(f"  Caja acumulada al cierre: {soles(filas[-1]['caja'])}")
    meses_falt = [f['mes'] for f in filas if f['faltante'] > 0.5]
    if meses_falt:
        print(f"  Meses en que la cuota no alcanza y vuelve a la tarjeta: "
              f"{', '.join(meses_falt)}")
    print()


# ------------------------------------------------------------------ reparto

def imprimir_reparto(r: dict, reserva: float, minimo: float = 0.0) -> None:
    """
    Reparto del sueldo el dia de pago: que sale si o si, cuanto se aparta para
    vivir, y recien con lo que queda se define la cuota de la tarjeta.

    El orden importa. Definir la cuota primero y vivir con lo que sobre es como
    se termina financiando la comida con la tarjeta.
    """
    ingresos = [f for f in r["movimientos"] if f["tipo"] == "ingreso"
                and f["categoria"] not in CATEGORIAS_NO_INGRESO]
    fijos = [f for f in r["movimientos"] if f["tipo"] == "fijo"]
    otros_deuda = [f for f in r["movimientos"]
                   if f["tipo"] == "deuda" and f["categoria"] != CATEGORIA_TC]
    cuota_reg = r["cuota_tc"]

    print(f"\n{'=' * 64}")
    print(f"  REPARTO DEL SUELDO — {r['mes']}")
    print(f"{'=' * 64}\n")

    print("1. ENTRA")
    for f in ingresos:
        print(f"     {f['concepto']:<30} {soles(f['monto'], 10)}")
    print(f"     {'':<30} {soles(r['ingresos_propios'], 10)}\n")

    print("2. SALE SI O SI (no negociable)")
    for f in sorted(fijos + otros_deuda, key=lambda x: x["monto"]):
        print(f"     {f['concepto']:<30} {soles(-f['monto'], 10)}")
    no_negociable = r["fijos"] + r["otros_deuda"]
    print(f"     {'':<30} {soles(no_negociable, 10)}\n")

    disponible = r["ingresos_propios"] - no_negociable
    print(f"   Disponible                       {soles(disponible, 10)}\n")

    print(f"3. SE APARTA PARA VIVIR           {soles(reserva, 10)}")
    print("   (comida, transporte, servicios, celular — hasta el proximo sueldo)\n")

    sostenible = disponible - reserva
    # El minimo del estado de cuenta es un piso contractual: si la cuota
    # sostenible cae por debajo, no hay eleccion — manda el minimo y lo que
    # falta tiene que salir de otro lado.
    cuota = max(sostenible, minimo)
    hueco = max(0.0, minimo - sostenible)

    print(f"{'-' * 64}")
    print(f"  4. A LA TARJETA                  {soles(cuota, 10)}"
          f"{'   <- pago minimo' if hueco else ''}")
    print(f"{'-' * 64}\n")

    if sostenible < 0:
        print(f"  ALERTA: no alcanza. Faltan {soles(-sostenible)} solo para cubrir lo")
        print("  no negociable mas la reserva de vida, antes de la tarjeta.\n")
    elif hueco:
        print(f"  El minimo ({soles(minimo)}) es mayor que lo que aguanta el mes")
        print(f"  ({soles(sostenible)}). No es elegible: hay que pagarlo igual, y")
        print(f"  quedan {soles(disponible - minimo)} para vivir.\n")
        print(f"  HUECO DEL MES: {soles(hueco)}")
        print("  Tiene que salir de algun lado. Compara las fuentes por su efecto")
        print("  NETO al final del horizonte —contando el activo que consumes, no")
        print("  solo la caja que queda— y deja la tarjeta para el final: cargar el")
        print("  hueco al plastico lo mantiene devengando hasta que canceles, no un")
        print("  mes, y pierde el periodo de gracia por ser consumo sobre saldo.\n")
    else:
        if cuota_reg and abs(cuota - cuota_reg) > 1:
            dif = cuota_reg - cuota
            print(f"  La cuota registrada es {soles(cuota_reg)}: {soles(abs(dif))} "
                  f"{'mas' if dif > 0 else 'menos'} de lo que")
            print(f"  aguanta el mes. Pagar de mas no acelera nada — esa diferencia")
            print(f"  vuelve a la tarjeta como consumo y encima pierde el periodo")
            print(f"  de gracia. Paga {soles(cuota)}.\n")
        if not minimo:
            print("  Verifica el pago minimo de tu estado de cuenta: si es mayor que")
            print("  este monto, ese es el piso y hay que recortar por otro lado.\n")


# --------------------------------------------------------------- patrimonio

ORDEN_LIQUIDEZ = ("inmediata", "dias", "baja")


def imprimir_patrimonio(tc: float, tcea: float, colchon: float) -> None:
    activos = leer_patrimonio(tc)
    pasivos = leer_pasivos()

    print(f"\n{'=' * 70}")
    print(f"  PATRIMONIO — tipo de cambio asumido S/ {tc:.2f} por USD")
    print(f"{'=' * 70}\n")

    print("ACTIVOS")
    total_activos = 0.0
    por_liq = {}
    for niv in ORDEN_LIQUIDEZ:
        grupo = [a for a in activos if a["liquidez"] == niv]
        if not grupo:
            continue
        sub = sum(a["pen"] for a in grupo)
        por_liq[niv] = sub
        total_activos += sub
        print(f"  {niv}")
        for a in grupo:
            og = f"  (US$ {a['monto']:,.0f})" if a["moneda"] == "USD" else ""
            if a["costo"] is not None and abs(a["costo"] - a["pen"]) > 0.5:
                og += f"  (costo {soles(a['costo'])})"
            duda = "  ~valuacion incierta" if a["confianza"] == "baja" else ""
            print(f"    {a['activo']:<26} {soles(a['pen'], 10)}{og}{duda}")
        print(f"    {'':<26} {soles(sub, 10)}  <- subtotal\n")
    print(f"  {'TOTAL ACTIVOS':<28} {soles(total_activos, 10)}\n")

    print("PASIVOS")
    total_pasivos = 0.0
    for q in pasivos:
        tasa = "  tasa ?" if q["tcea"] is None else f"  {q['tcea']:.0f}%"
        if q["estado"] == "cancelado":
            print(f"    {q['instrumento']:<26} {'cancelado':>10}{tasa}")
        elif q["saldo"] is None:
            print(f"    {q['instrumento']:<26} {'por confirmar':>10}{tasa}")
        else:
            total_pasivos += q["saldo"]
            print(f"    {q['instrumento']:<26} {soles(q['saldo'], 10)}{tasa}")
    print(f"    {'':<26} {soles(total_pasivos, 10)}  <- registrado\n")

    # Orden de ataque: siempre de la tasa mas cara a la mas barata. Una deuda a
    # 0% nunca se adelanta mientras exista una cara — adelantarla es regalar el
    # unico financiamiento gratis que se tiene.
    vivos = [q for q in pasivos if q["estado"] != "cancelado"]
    caras = sorted(vivos, key=lambda q: -(1e9 if q["tcea"] is None else q["tcea"]))
    if len(caras) > 1:
        print("  Orden de ataque (de la tasa mas cara a la mas barata):")
        for n, q in enumerate(caras, 1):
            t = "sin confirmar — asumir alta" if q["tcea"] is None else f"{q['tcea']:.0f}%"
            extra = "   <- solo el minimo, nunca adelantar" if q["tcea"] == 0 else ""
            print(f"    {n}. {q['instrumento']:<24} {t}{extra}")
        print()

    neto = total_activos - total_pasivos
    print(f"{'-' * 70}")
    print(f"  PATRIMONIO NETO             {soles(neto, 10)}")
    if any(p["saldo"] is None for p in pasivos if p["estado"] != "cancelado"):
        print("  (es un techo: hay pasivos sin confirmar — el neto real es menor)")
    print(f"{'-' * 70}\n")

    # --- tasa valla: que tiene que rendir un activo para justificar tenerlo ---
    liquido = por_liq.get("inmediata", 0.0) + por_liq.get("dias", 0.0)
    aplicable = max(0.0, liquido - colchon)
    i = tasa_mensual(tcea)
    print("TASA VALLA (que tiene que rendir un activo para valer la pena)")
    print(f"  Tu deuda cuesta {tcea:.0f}% anual ({i * 100:.2f}% mensual). Cualquier activo que")
    print(f"  rinda menos que eso te cuesta plata mientras la deuda exista.\n")
    print(f"  Liquido o casi liquido (dias)      {soles(liquido, 10)}")
    if colchon:
        print(f"  Reservado como colchon             {soles(colchon, 10)}")
    print(f"  Aplicable a la tarjeta hoy         {soles(aplicable, 10)}")
    print(f"  Lo que cuesta NO aplicarlo         {soles(aplicable * i, 10)} / mes\n")


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

    p_pro = sub.add_parser("proyeccion",
                           help="Proyecta N meses aplicando calendario.csv")
    p_pro.add_argument("--mes", required=True, help="Mes base cuya estructura se repite")
    p_pro.add_argument("--saldo", type=float, required=True, help="Saldo TC inicial")
    p_pro.add_argument("--cuota", type=float, required=True)
    p_pro.add_argument("--tcea", type=float, default=60.0)
    p_pro.add_argument("--meses", type=int, default=12)
    p_pro.add_argument("--variables", type=float, default=None,
                       help="Gasto variable mensual asumido (llena el hueco del presupuesto)")
    p_pro.add_argument("--otros-deuda-hasta", default=None, metavar="AAAA-MM",
                       help="Ultimo mes en que se paga el otro servicio de deuda (adelanto)")
    p_pro.add_argument("--extraordinario", choices=["deuda", "caja"], default="deuda",
                       help="Destino de CTS/gratificacion (default: deuda)")
    p_pro.add_argument("--json", action="store_true")

    p_rep = sub.add_parser("reparto",
                           help="Como repartir el sueldo el dia de pago")
    p_rep.add_argument("--mes", required=True)
    p_rep.add_argument("--reserva", type=float, required=True,
                       help="Cuanto se aparta para vivir hasta el proximo sueldo")
    p_rep.add_argument("--minimo", type=float, default=0.0,
                       help="Pago minimo de la tarjeta segun el estado de cuenta (es un piso)")

    p_pat = sub.add_parser("patrimonio", help="Activos, pasivos y patrimonio neto")
    p_pat.add_argument("--tc", type=float, default=3.75,
                       help="Tipo de cambio USD->PEN (default 3.75; verificar en BCRP)")
    p_pat.add_argument("--tcea", type=float, default=60.0,
                       help="TCEA de la deuda, para calcular la tasa valla")
    p_pat.add_argument("--colchon", type=float, default=0.0,
                       help="Monto liquido que se reserva como fondo de emergencia")

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

    elif a.cmd == "reparto":
        imprimir_reparto(calcular_resumen(a.mes), a.reserva, a.minimo)

    elif a.cmd == "patrimonio":
        imprimir_patrimonio(a.tc, a.tcea, a.colchon)

    elif a.cmd == "proyeccion":
        r = calcular_resumen(a.mes)
        var = r["variables"] if a.variables is None else a.variables
        filas = proyectar(r, a.saldo, a.cuota, a.tcea, a.meses, a.variables,
                          a.otros_deuda_hasta, a.extraordinario)
        if a.json:
            print(json.dumps(filas, ensure_ascii=False, indent=2))
        else:
            imprimir_proyeccion(filas, r, a.tcea, var, a.extraordinario)


if __name__ == "__main__":
    main()
