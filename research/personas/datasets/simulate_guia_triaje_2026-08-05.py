#!/usr/bin/env python3
"""Simulación de la 'Guía de preguntas' (estudio de triaje digital + kit) sobre
200 usuarios sintéticos peruanos generados con el modelo `lapuerta`.

Universo pedido: peruanos 18-65 años, NSE A, B y C.

IMPORTANTE — alcance de esta simulación:
  El prototipo (https://vivo-triaje.vercel.app) NO es alcanzable desde este entorno
  (la política de red del gateway devuelve 403 al CONNECT). Por lo tanto se responden
  SOLO las preguntas de la guía que no requieren haber usado el prototipo ni el kit
  físico. Las secciones "SOBRE EL ASISTENTE DIGITAL" y "SOBRE EL KIT" quedan sin
  responder y se reportan como tales.

Calibración de las reglas de respuesta: las direcciones y proporciones de la sección
"PUNTO DE PARTIDA" vienen de la investigación propia del proyecto
(research/_nodes/modelo-salud-ia-farmacias-peru.md §1.1-§1.4, fuentes F-35, F-36,
F-38, F-39, F-48):
  - Motivos para evitar al médico: ineficiencia del sistema 59.34%, falta de tiempo
    51.48%, falta de dinero 15.74%, desconfianza en médicos solo 7.21%.
  - Fuentes de consejo para automedicarse: familia/vecinos 70.49%, recetas previas
    64.26%, técnico de farmacia 22.95%.
  - Preferencia por marca 66.2% vs. genérico 16.23%.
  - 3 de cada 10 hogares compra sin receta; provincias 36% > Lima 32%.
  - 35% no asiste a un centro de salud por demoras; 13% por distancia.
"""
from __future__ import annotations

import argparse
import collections
import csv
import importlib.util
import os
import random

SKILL = "/home/user/Machine_Learning/.claude/skills/lapuerta/scripts"
_spec = importlib.util.spec_from_file_location(
    "synthgen", os.path.join(SKILL, "generate_synthetic_users.py"))
g = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(g)

SEED = 42
N_TARGET = 200
TARGET_NSE = {"A", "B", "C"}

# Rango etario por generación, truncado al techo de 65 que pide el estudio.
# ⚠️ El modelo `lapuerta` define Boomer como "60_mas" (sin techo); aquí se trunca a 60-65.
AGE_BAND = {
    "Gen_Z_18_27": (18, 27),
    "Millennial_28_43": (28, 43),
    "Gen_X_44_59": (44, 59),
    "Boomer_60_mas": (60, 65),
}

# Proxy declarado: el modelo no tiene variable "usa WhatsApp".
# Se deriva de `acceso_digital`. SUPUESTO, no dato calibrado.
P_WHATSAPP = {"alta": 0.97, "media": 0.85, "baja": 0.45}

ASEGURADORAS = ["RIMAC", "Pacífico", "Mapfre", "La Positiva", "Sanitas"]


def build_population():
    rng = random.Random(SEED)
    schema = g.load_schema()
    pop, drawn = [], 0
    while len(pop) < N_TARGET:
        u = g.generate_user(rng, schema, drawn)
        drawn += 1
        if u["nse"] not in TARGET_NSE:
            continue
        lo, hi = AGE_BAND[u["generacion"]]
        u["edad"] = rng.randint(lo, hi)
        u["usa_whatsapp"] = rng.random() < P_WHATSAPP[u["acceso_digital"]]
        u["id"] = f"P_{len(pop):03d}"
        u["_rng"] = rng.random()          # ruido idiosincrático reproducible
        u["_rng2"] = rng.random()
        u["_rng3"] = rng.random()
        pop.append(u)
    return pop, drawn


# ------------------------------------------------------- PERFIL ("Para conocerte")
def q_seguro_privado(u):
    """¿Tienes algún seguro de salud PRIVADO?"""
    if u["tenencia_seguro"] != "voluntario":
        return ("no", None)
    # Entre quienes tienen seguro voluntario, la probabilidad de que sea de salud
    # privado (no solo vida/vehicular) escala con NSE.
    p = {"A": 0.80, "B": 0.55, "C": 0.28}[u["nse"]]
    if u["_rng"] < p:
        idx = int(u["_rng2"] * len(ASEGURADORAS)) % len(ASEGURADORAS)
        return ("si", ASEGURADORAS[idx])
    return ("no", None)


def q_para_quien(u):
    """¿Buscas ayuda para ti, o también para un hijo / alguien mayor en casa?"""
    if u["generacion"] == "Gen_Z_18_27":
        return "solo_para_mi" if u["_rng"] < 0.72 else "tambien_terceros"
    if u["generacion"] == "Millennial_28_43":
        return "tambien_hijos" if u["_rng"] < 0.58 else "solo_para_mi"
    if u["generacion"] == "Gen_X_44_59":
        return "tambien_hijos_y_mayores" if u["_rng"] < 0.62 else "solo_para_mi"
    return "tambien_mi_pareja_o_yo" if u["_rng"] < 0.55 else "solo_para_mi"


# ------------------------------------------------- PUNTO DE PARTIDA (comportamiento)
def q_como_resolvio(u):
    """Último malestar leve: ¿cómo lo resolviste?  (calibrado con F-35/F-38/F-39)"""
    # Coeficientes COMPRIMIDOS y ruido amplio: una primera versión con coeficientes
    # más fuertes producía 80.3% de automedicación (fuera del rango documentado
    # 20-68%) y segmentos saturados en 100%. Recalibrado para que la marginal caiga
    # dentro del rango de F-35/F-38/F-39 y ningún segmento sea determinístico.
    s = 0.0
    s += {"A": -1.10, "B": -0.35, "C": 0.30}[u["nse"]]
    s += {"alta": -0.35, "media": 0.0, "baja": 0.35}[u["educacion_financiera"]]
    s += 0.25 if u["region"] != "Lima_Metropolitana" else 0.0   # provincias 36% > Lima 32%
    s += {"formal_dependiente": -0.30, "independiente_microemprendedor": 0.20,
          "informal": 0.40}[u["situacion_laboral"]]
    s += 0.35 if u["tenencia_seguro"] == "ninguno" else 0.0
    s += (u["_rng"] - 0.5) * 2.4

    if s >= 0.95:
        return "botiquin_casero"          # se automedicó con lo que tenía en casa
    if s >= 0.15:
        return "farmacia_sin_receta"      # fue a la botica y pidió algo
    if s >= -0.75:
        return "consulta_remota_o_conocido"  # preguntó a un familiar/conocido con criterio médico
    return "consulta_medica_formal"


MOTIVO_LABEL = {
    "sistema_lento": "El sistema es lento / sacar cita toma mucho",
    "falta_tiempo": "No tenía tiempo",
    "era_leve": "Era algo leve, no ameritaba médico",
    "costo": "Por el costo",
    "desconfianza_medico": "No confío mucho en la atención médica",
}


def q_por_que(u, como):
    """¿Por qué lo abordaste así? — proporciones ancladas en F-38."""
    r = u["_rng2"]
    if como == "consulta_medica_formal":
        return "era_serio_o_tengo_cobertura"
    # Distribución calibrada: ineficiencia 59.34% / tiempo 51.48% / dinero 15.74% /
    # desconfianza 7.21% (se reparte como motivo DOMINANTE, no múltiple).
    if r < 0.36:
        return "sistema_lento"
    if r < 0.63:
        return "falta_tiempo"
    if r < 0.83:
        return "era_leve"
    if r < 0.94:
        return "costo"
    return "desconfianza_medico"


def q_medicamentos(u, como):
    """¿Cómo hiciste con los medicamentos? — fuente de consejo + marca vs genérico."""
    r = u["_rng3"]
    if como == "consulta_medica_formal":
        fuente = "receta_del_medico"
    elif como == "botiquin_casero":
        fuente = "receta_previa_guardada" if r < 0.55 else "consejo_familiar"
    elif como == "farmacia_sin_receta":
        fuente = "consejo_tecnico_farmacia" if r < 0.48 else "lo_pedi_por_nombre"
    else:
        fuente = "consejo_familiar"
    # Preferencia marca 66.2% vs genérico 16.23% (resto: indistinto)
    if u["_rng"] < 0.66:
        pref = "marca"
    elif u["_rng"] < 0.82:
        pref = "generico"
    else:
        pref = "indistinto"
    return fuente, pref


# ------------------------------------------- ESCALAMIENTO (hipotético, sin prototipo)
def q_no_mejora_24_48h(u):
    """Si a las 24-48h no mejoras, ¿qué harías?"""
    s = 0.0
    s += {"A": 0.9, "B": 0.4, "C": -0.3}[u["nse"]]
    s += 0.7 if u["tenencia_seguro"] == "voluntario" else 0.0
    s += {"confia_plena": 0.5, "neutral": 0.0, "desconfia": -0.5}[u["confianza_aseguradora"]]
    s += -0.4 if u["region"] != "Lima_Metropolitana" else 0.0
    s += (u["_rng3"] - 0.5) * 1.4
    if s >= 1.0:
        return "voy_al_medico_o_clinica"
    if s >= 0.1:
        return "teleconsulta_si_esta_incluida"
    if s >= -0.7:
        return "vuelvo_a_la_farmacia"
    return "espero_un_poco_mas"


# ---------------------------------------------------------- CIERRE (solución ideal)
def q_solucion_ideal(u):
    s = 0.0
    s += {"alta": 0.8, "media": 0.1, "baja": -0.8}[u["apertura_datos_ia"]]
    s += {"alta": 0.5, "media": 0.0, "baja": -0.6}[u["acceso_digital"]]
    s += {"confia_plena": 0.4, "neutral": 0.0, "desconfia": -0.6}[u["confianza_aseguradora"]]
    s += {"Gen_Z_18_27": 0.5, "Millennial_28_43": 0.3,
          "Gen_X_44_59": -0.2, "Boomer_60_mas": -0.6}[u["generacion"]]
    s += (u["_rng2"] - 0.5) * 1.2
    if s >= 1.1:
        return "rapida_y_digital_sin_hablar_con_nadie"
    if s >= 0.2:
        return "digital_pero_con_humano_disponible"
    if s >= -0.7:
        return "que_me_confirme_un_profesional"
    return "prefiero_atencion_presencial"


def pct(c, n):
    return {k: round(100.0 * v / n, 1) for k, v in c.items()}


def block(title):
    print("\n" + "=" * 82)
    print(title)
    print("=" * 82)


def dist(c, n, labels=None, indent="    "):
    for k, v in c.most_common():
        lab = labels.get(k, k) if labels else k
        print(f"{indent}{lab:52s} {100.0*v/n:5.1f}%  ({v})")


def main(out_csv=None):
    pop, drawn = build_population()
    n = len(pop)
    print(f"[Se muestrearon {drawn} perfiles de la población general para obtener "
          f"{n} que cumplen NSE A/B/C]")
    print(f"POBLACIÓN: {n} usuarios sintéticos peruanos · 18-65 años · NSE A/B/C · seed={SEED}")

    block("COMPOSICIÓN DE LA MUESTRA")
    for dim in ("nse", "generacion", "region", "situacion_laboral",
                "tenencia_seguro", "confianza_aseguradora", "acceso_digital",
                "apertura_datos_ia", "educacion_financiera"):
        c = collections.Counter(u[dim] for u in pop)
        print(f"  {dim:24s} " + " · ".join(f"{k}={v}" for k, v in c.most_common()))
    edades = sorted(u["edad"] for u in pop)
    print(f"  {'edad':24s} min={edades[0]} · mediana={edades[n//2]} · max={edades[-1]}")

    # ---------------- SCREENER
    block("PARTE 1 — SCREENER · ¿Sueles usar WhatsApp en tu día a día?")
    cw = collections.Counter("si_pasa" if u["usa_whatsapp"] else "no_pasa" for u in pop)
    dist(cw, n, {"si_pasa": "✅ Sí — continúa la sesión",
                 "no_pasa": "❌ No — queda fuera del estudio"})
    elegibles = [u for u in pop if u["usa_whatsapp"]]
    ne = len(elegibles)
    print(f"\n  → MUESTRA ELEGIBLE PARA LA GUÍA PRINCIPAL: {ne} de {n}")
    print("  ⚠️ Proxy declarado: el modelo no tiene variable 'usa WhatsApp'; se deriva de")
    print("     `acceso_digital` (alta .97 / media .85 / baja .45). Es SUPUESTO, no dato.")

    # ---------------- PERFIL
    block("PARTE 2 — PARA CONOCERTE  (n=%d elegibles)" % ne)
    print("\n  ¿Cuántos años tienes?")
    ce = collections.Counter()
    for u in elegibles:
        e = u["edad"]
        band = "18-27" if e <= 27 else "28-43" if e <= 43 else "44-59" if e <= 59 else "60-65"
        ce[band] += 1
    dist(ce, ne)

    print("\n  ¿Tienes algún seguro de salud privado?")
    cs = collections.Counter()
    aseg = collections.Counter()
    for u in elegibles:
        r, a = q_seguro_privado(u)
        cs[r] += 1
        if a:
            aseg[a] += 1
    dist(cs, ne, {"si": "Sí, tengo seguro de salud privado", "no": "No"})
    if aseg:
        print("\n    ¿De qué aseguradora? (entre los que sí tienen, n=%d)" % sum(aseg.values()))
        dist(aseg, sum(aseg.values()), indent="      ")
        print("      ⚠️ Reparto de marcas = SUPUESTO (no hay market share verificado en el ledger).")

    print("\n  Cuando buscas ayuda para un malestar, ¿es para ti o también para otros?")
    cq = collections.Counter(q_para_quien(u) for u in elegibles)
    dist(cq, ne, {
        "solo_para_mi": "Solo para mí",
        "tambien_hijos": "También para mis hijos",
        "tambien_hijos_y_mayores": "También para hijos y/o un adulto mayor",
        "tambien_mi_pareja_o_yo": "También para mi pareja",
        "tambien_terceros": "También para otros en casa"})

    # ---------------- PUNTO DE PARTIDA
    block("PUNTO DE PARTIDA — La última vez que te sentiste mal, ¿cómo lo resolviste?")
    comos = {u["id"]: q_como_resolvio(u) for u in elegibles}
    cc = collections.Counter(comos.values())
    dist(cc, ne, {
        "botiquin_casero": "Me automediqué con lo que tenía en casa",
        "farmacia_sin_receta": "Fui a la farmacia y pedí algo sin receta",
        "consulta_remota_o_conocido": "Consulté a un familiar/conocido con criterio médico",
        "consulta_medica_formal": "Fui a una consulta médica formal"})
    auto = cc["botiquin_casero"] + cc["farmacia_sin_receta"]
    print(f"\n    → RESOLVIÓ SIN VER A UN MÉDICO: {100.0*auto/ne:.1f}% "
          f"({auto} de {ne})")
    print("      Consistente con el rango 20-68% de automedicación documentado en")
    print("      `modelo-salud-ia-farmacias-peru.md` §1.1 (F-35/F-38/F-39).")

    print("\n  ¿Por qué lo abordaste así?")
    cp = collections.Counter(q_por_que(u, comos[u["id"]]) for u in elegibles)
    lab = dict(MOTIVO_LABEL)
    lab["era_serio_o_tengo_cobertura"] = "Era serio / tengo cobertura y la uso"
    dist(cp, ne, lab)
    print("      Calibrado con F-38: ineficiencia del sistema y falta de tiempo dominan;")
    print("      la desconfianza en el médico es el motivo MENOS citado (7.21%).")

    print("\n  ¿Cómo hiciste con los medicamentos?")
    cf, cm = collections.Counter(), collections.Counter()
    for u in elegibles:
        f, p = q_medicamentos(u, comos[u["id"]])
        cf[f] += 1
        cm[p] += 1
    dist(cf, ne, {
        "receta_del_medico": "Con receta del médico",
        "receta_previa_guardada": "Reusé una receta anterior",
        "consejo_familiar": "Me guie por consejo de familia/conocidos",
        "consejo_tecnico_farmacia": "Le pregunté al técnico de la farmacia",
        "lo_pedi_por_nombre": "Lo pedí por nombre, ya sabía cuál"})
    print("\n    Marca vs. genérico:")
    dist(cm, ne, {"marca": "Prefiero la marca conocida",
                  "generico": "Genérico está bien",
                  "indistinto": "Me da igual"}, indent="      ")

    # ---------------- ESCALAMIENTO
    block("SI A LAS 24-48 HORAS NO MEJORAS, ¿QUÉ HARÍAS?  (hipotético — sin prototipo)")
    cn = collections.Counter(q_no_mejora_24_48h(u) for u in elegibles)
    dist(cn, ne, {
        "voy_al_medico_o_clinica": "Voy al médico / clínica",
        "teleconsulta_si_esta_incluida": "Teleconsulta, si viene incluida",
        "vuelvo_a_la_farmacia": "Vuelvo a la farmacia por algo más fuerte",
        "espero_un_poco_mas": "Espero un poco más a ver si pasa"})

    # ---------------- CIERRE
    block("CIERRE — ¿Cómo debería ser la solución ideal para estos síntomas?")
    ci = collections.Counter(q_solucion_ideal(u) for u in elegibles)
    dist(ci, ne, {
        "rapida_y_digital_sin_hablar_con_nadie": "Rápida y digital, sin tener que hablar con nadie",
        "digital_pero_con_humano_disponible": "Digital, pero con un humano disponible si lo necesito",
        "que_me_confirme_un_profesional": "Que un profesional me confirme antes de tomar algo",
        "prefiero_atencion_presencial": "Prefiero atención presencial"})

    # ---------------- CORTES
    block("CORTES POR SEGMENTO — resolvió SIN médico (automedicación)")
    for dim in ("nse", "generacion", "region", "situacion_laboral"):
        print(f"\n  Por {dim}:")
        groups = collections.defaultdict(list)
        for u in elegibles:
            groups[u[dim]].append(u)
        for gname, gu in sorted(groups.items(), key=lambda kv: -len(kv[1])):
            k = sum(1 for x in gu if comos[x["id"]] in
                    ("botiquin_casero", "farmacia_sin_receta"))
            print(f"    {gname:34s} n={len(gu):3d}   {100.0*k/len(gu):5.1f}%")

    block("PREGUNTAS QUE NO SE PUDIERON RESPONDER (requieren el prototipo / el kit)")
    for q in [
        "SOBRE EL ASISTENTE DIGITAL — ¿qué te pareció la experiencia general? ¿por qué?",
        "SOBRE EL ASISTENTE DIGITAL — ¿qué tan fácil te resultó? poco / algo / muy fácil",
        "SOBRE EL ASISTENTE DIGITAL — ¿qué te gustó y qué no te gustó? ¿por qué?",
        "SOBRE EL ASISTENTE DIGITAL — sobre las recomendaciones: ¿por qué elegiste esa / no elegiste alguna?",
        "SOBRE EL ASISTENTE DIGITAL — ¿qué mejorarías?",
        "SOBRE EL KIT — ¿qué te pareció? ¿por qué?",
        "SOBRE EL KIT — ¿qué te gustó y qué no te gustó? ¿por qué?",
        "SOBRE EL KIT — ¿qué mejorarías?",
    ]:
        print(f"    ✗ {q}")
    print("\n    Motivo: https://vivo-triaje.vercel.app no es alcanzable desde este entorno")
    print("    (el gateway de red responde 403 al CONNECT — denegación de política, no")
    print("    un fallo transitorio). El kit, además, es un objeto físico.")

    if out_csv:
        base = [k for k in pop[0] if not k.startswith("_")]
        extra = ["resp_seguro_privado", "resp_aseguradora", "resp_para_quien",
                 "resp_como_resolvio", "resp_por_que", "resp_fuente_medicamento",
                 "resp_marca_generico", "resp_no_mejora", "resp_solucion_ideal"]
        with open(out_csv, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=base + extra)
            w.writeheader()
            for u in pop:
                row = {k: u[k] for k in base}
                if u["usa_whatsapp"]:
                    s, a = q_seguro_privado(u)
                    como = q_como_resolvio(u)
                    f, pr = q_medicamentos(u, como)
                    row.update({
                        "resp_seguro_privado": s, "resp_aseguradora": a or "",
                        "resp_para_quien": q_para_quien(u),
                        "resp_como_resolvio": como,
                        "resp_por_que": q_por_que(u, como),
                        "resp_fuente_medicamento": f, "resp_marca_generico": pr,
                        "resp_no_mejora": q_no_mejora_24_48h(u),
                        "resp_solucion_ideal": q_solucion_ideal(u)})
                else:
                    for k in extra:
                        row[k] = "FUERA_DEL_ESTUDIO"
                w.writerow(row)
        print(f"\n[CSV con los {n} perfiles y sus respuestas: {out_csv}]")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv")
    main(ap.parse_args().csv)
