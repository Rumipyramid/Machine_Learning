#!/usr/bin/env python3
"""Genera la matriz de status de proyectos Behavioral Design (RIMAC) en Excel.

Fuente de datos: Excel de trabajo del equipo (Status_Proyectos_Behavioral_Design_1)
+ board original. Sincronizado al 2026-06-22.
Uso: python reportes/generar_matriz_status.py
Salida: reportes/Status_Proyectos_Behavioral_Design.xlsx
"""
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.formatting.rule import DataBarRule
from openpyxl.utils import get_column_letter

# ----------------------------------------------------------------------------
# Datos. Cada fila = una iniciativa (quest), en el orden de columnas de COLUMNS.
# Sincronizado con el Excel de trabajo del equipo (typos corregidos y el impacto
# truncado de Q-11 completado; ver hoja "Leyenda y notas").
# ----------------------------------------------------------------------------
COLUMNS = [
    "Clave", "Épica", "Iniciativa", "Prioridad", "Objetivo del proyecto",
    "Intervención de diseño de conducta", "Estado (Jira)", "Status (detalle)",
    "% Avance", "Equipo que requiere el servicio", "Stakeholder",
    "Equipo Behavioral Design", "Fichas", "Fecha de entrega", "Riesgos",
    "Impacto esperado",
]

NEGOCIO = "Priorizada por negocio"
CAPACIDAD = "Capacidades equipo BD"

ROWS = [
    ["Q-1", "Guías resumidas (Pólizas simples)", "Guías resumidas — 4 nuevos productos AMI", NEGOCIO,
     "Promover el entendimiento y uso eficiente de los seguros de salud",
     "Rediseño de la información del producto para hacerla clara y comprensible (ataca la barrera de «falta de información»).",
     "In Progress", "WIP - 1 producto en agencia", 0.40,
     "AMI – Salud (Producto)", "Estrella Damian, Soiky Bardales", "Stef, Felipe, Alejandro", 8, "30 de junio",
     "Cambio en el roadmap (de 1 guía a 4 productos)",
     "↓ ~25–30% casos NPS «no recibí información» (est.); ataca la palanca #1 de desconfianza en Perú"],

    ["Q-2", "Renovación AMI", "Batería de soluciones para la renovación AMI", NEGOCIO,
     "Reducir el churn y reclamos por cambios en la renovación",
     "Comunicación proactiva que reduce incertidumbre y fricción ante el cambio.",
     "Diseñado", "Carta de renovación implementada; 3 soluciones diseñadas on hold", 1.00,
     "AMI – Renovación / Salud", "Estrella Damian, Soiky Bardales", "Alejandro", 2, "30 de junio",
     "La carta por sí sola no cubre la necesidad del usuario",
     "+3–5 pp retención sobre base industria ~84% y ↓ reclamos (est.); depende de desbloquear las 3 soluciones on hold"],

    ["Q-3", "Guías resumidas (Pólizas simples)", "Guías resumidas — 5 clientes TOP EPS", NEGOCIO,
     "Promover el entendimiento y uso eficiente de los seguros de salud",
     "Misma palanca de claridad/comprensión aplicada a cuentas clave.",
     "Done", "1 implementada, 4 entregadas", 1.00,
     "EPS – Salud Corporativa", "Kevin Crisanto, María Alejandra Valcarcel", "Stef, Felipe, Alejandro", 3, "Julio 2026",
     "Producto pide no comunicar algunos servicios valorados por el usuario",
     "Renovación de cuentas TOP EPS (incl. Antapacay) + ↓ «no recibí información» en corporativo; alto valor por cuenta"],

    ["Q-4", "Evolution+: Cobranzas", "Captura de datos para conciliación de facturas de proveedores", NEGOCIO,
     "Promover la captura de datos para conciliación de facturas proveedores",
     "Rediseño del flujo de captura de datos (Evolution+) para facilitar/incentivar que los proveedores entreguen la información de conciliación.",
     "In Progress", "En fase de research", 0.20,
     "Cobranzas / Finanzas", "Rosemary Moyano", "Stef", 4, "30 de junio",
     "Track de diseño aprobado sin explorar la problemática",
     "Liberación de S/600k provisionados"],

    ["Q-5", "Back to Basics FFVV Vida Individual", "Mensajes de primer contacto", NEGOCIO,
     "Promover el agendamiento de citas comerciales",
     "Mensajes de primer contacto (copys/secuencia) que enmarcan la propuesta y reducen la fricción para agendar una cita comercial.",
     "To Do (Block)", "Block", 0.10,
     "FFVV Vida Individual", "Diana Riofrío, Jaime Huerta", "Alejandro", 1, "Julio 2026",
     "No existe estrategia definida de contacto bajo contexto CUA (bloqueado)",
     "+20–30% agendamiento de citas en primer contacto (est., potencial — bloqueado por estrategia CUA)"],

    ["Q-6", "Loyalty", "Programa de lealtad (MVP/piloto)", NEGOCIO,
     "Diseñar un programa de lealtad del ecosistema que asegure la permanencia de los asegurados",
     "Diseño del programa de lealtad (mecánica de recompensas/beneficios) para reforzar la permanencia y el comportamiento de continuidad del asegurado.",
     "In Progress", "Diseñando y viabilizando la propuesta MVP/piloto (3–6 meses)", 0.60,
     "Loyalty / Ecosistema RIMAC", "Denisse Galvez, Lucía Ramos, Jorge Sarmiento", "Alejandro", 2, "Julio 2026",
     "—",
     "Permanencia base RIMAC (1,250 MM clientes); benchmark loyalty +20–25% retención y +40% cross-sell (est.)"],

    ["Q-7", "Back to Basics FFVV Vida Individual", "Universidad Vida", NEGOCIO,
     "Acelerar la curva de aprendizaje de asesores nuevos / mejorar ratio de conversión",
     "Programa de formación «Universidad Vida» para asesores nuevos: acelera la curva de aprendizaje con práctica estructurada.",
     "Diseñado", "Contenido listo, falta diseño instruccional (Learning)", 0.40,
     "FFVV Vida Individual", "Diana Riofrío, Jaime Huerta", "Melissa, Alejandro", 4, "Julio 2026",
     "Capacidad limitada del equipo de learning",
     "−25–40% tiempo de ramp-up de asesores jr + mejor conversión y NPS Venta (est.)"],

    ["Q-8", "Back to Basics FFVV Vida Individual", "Skill AIDA Bot Trainer + reportería", NEGOCIO,
     "Promover el aprendizaje y capacitación de asesores y dar visibilidad de expertise a jefaturas FFVV",
     "Agente entrenador (bot) de práctica de casos con puntaje de efectividad y alertas por falta de principios básicos de experiencia (CX); práctica deliberada con feedback y visibilidad a jefaturas.",
     "In Review", "Prototipo diseñado y validada usabilidad y valoración de usuarios", 0.80,
     "FFVV Vida Individual", "Diana Riofrío, Jaime Huerta", "Felipe, Melissa", 6, "—",
     "AIDA no cumple el task; entra a comité de priorización; 3 herramientas en paralelo",
     "+efectividad del asesor (medible vía el puntaje del bot) y consistencia CX; práctica con feedback acelera ramp "
     "(−25–40%, est.); jefaturas hacen coaching dirigido. Ahorro proyectado S/1.8M (cifra del board, base por documentar)"],

    ["Q-9", "Back to Basics FFVV Vida Individual", "Kit de Social Selling", NEGOCIO,
     "Promover la generación de leads y agendamientos para FFVV",
     "Kit de social selling (contenido + herramientas de huella digital) para que la FFVV genere leads y agendamientos.",
     "In Progress", "WIP", 0.40,
     "FFVV Vida Individual", "Diana Riofrío, Jaime Huerta", "Melissa", 3, "Julio 2026",
     "Recursos limitados de contenido + falta de incentivos + falta de monitoreo",
     "+leads/agendamientos FFVV; social selling 15–25% conversión lead→cita, CPL −30–50% (est.)"],

    ["Q-10", "Bienestar 360", "Bienestar 360", NEGOCIO,
     "Piloto con colaboradores Rimac para construir hábitos saludables sostenibles",
     "Programa de hábitos saludables (piloto Bienestar 360) para construir y sostener hábitos de bienestar en colaboradores.",
     "Done", "Implementado y en mantenimiento", 1.00,
     "Bienestar / Estar Bien", "Erika Echegaray, Belem Rodríguez; Solange Soto, Rosa Díaz", "Stef", 3,
     "Setiembre 2026 (solo acompañamiento)",
     "Presupuesto y recursos limitados para la siguiente versión",
     "+3 ptos Wellby · CSAT 4.6/5 · NPS 78"],

    # --- Iniciativas de capacidades del equipo BD (Chapter BD) ---
    ["Q-11", "Modelo de entendimiento y uso eficiente de seguros", "Arquitectura BD", CAPACIDAD,
     "Definir framework de trabajo para ecosistema de entendimiento y uso eficiente de seguros",
     "Arquitectura del conocimiento",
     "In Progress", "Terminado el framework de trabajo; falta alinear con los distintos frentes involucrados", 0.80,
     "Chapter BD", "—", "Todos", "—", "—",
     "—",
     "Framework para potenciar el entendimiento y uso eficiente de seguros"],

    ["Q-12", "Sistema de generación de usuarios sintéticos", "Arquitectura BD", CAPACIDAD,
     "Crear recurso de exploración para conocimiento esencial de seguros y comportamiento con los seguros en Perú",
     "Creación de herramienta de testeo",
     "Diseñado", "Terminado, por validar", 0.90,
     "Chapter BD", "—", "Todos", "—", "—",
     "—",
     "Agilidad en el testeo de preguntas ya exploradas sobre conducta con seguros"],

    ["Q-13", "Modelo de cambio de hábitos", "Arquitectura BD", CAPACIDAD,
     "Definir framework de trabajo para ecosistema de entendimiento y uso eficiente de seguros",
     "Arquitectura del conocimiento",
     "Done", "Terminado y validado", 1.00,
     "Chapter BD", "—", "Todos", "—", "—",
     "—",
     "Framework para trabajo de iniciativas relacionadas al cambio de hábitos"],

    ["Q-14", "Skill para desk research con rigurosidad científica", "Arquitectura BD", CAPACIDAD,
     "Potenciar el desk research con parámetros de búsqueda con rigurosidad metodológica y creación de repositorio de conocimiento",
     "Creación de herramienta de research",
     "Diseñado", "Terminado, por validar", 0.90,
     "Chapter BD", "—", "Todos", "—", "—",
     "—",
     "Agilidad y calidad de los entregables de investigación de escritorio"],
]

# ----------------------------------------------------------------------------
# Estilos
# ----------------------------------------------------------------------------
NAVY = "1F3864"
HEADER_FILL = PatternFill("solid", fgColor=NAVY)
HEADER_FONT = Font(bold=True, color="FFFFFF", size=11)
TITLE_FONT = Font(bold=True, color=NAVY, size=15)
THIN = Side(style="thin", color="BFBFBF")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
WRAP_TOP = Alignment(wrap_text=True, vertical="top")
CENTER = Alignment(horizontal="center", vertical="center", wrap_text=True)

ESTADO_FILL = {
    "Done": PatternFill("solid", fgColor="C6EFCE"),
    "In Review": PatternFill("solid", fgColor="BDD7EE"),
    "Diseñado": PatternFill("solid", fgColor="E4DFEC"),
    "In Progress": PatternFill("solid", fgColor="FFF2CC"),
    "To Do (Block)": PatternFill("solid", fgColor="FFC7CE"),
}

# Índices de columna (1-based) con uso especial
COL_ESTADO = 7
COL_AVANCE = 9
COL_FICHAS = 13

WIDTHS = [7, 30, 26, 18, 38, 44, 14, 32, 10, 22, 24, 20, 8, 20, 34, 46]
WRAP_COLS = {2, 3, 4, 5, 6, 8, 10, 11, 12, 15, 16}  # columnas (1-based) con texto largo

# ----------------------------------------------------------------------------
# Construcción
# ----------------------------------------------------------------------------
wb = Workbook()
ws = wb.active
ws.title = "Status Proyectos"

last_col = get_column_letter(len(COLUMNS))
ws.merge_cells(f"A1:{last_col}1")
ws["A1"] = "Matriz de Status — Behavioral Design (RIMAC)"
ws["A1"].font = TITLE_FONT
ws.merge_cells(f"A2:{last_col}2")
ws["A2"] = "Cierre Q2 2026 · Fecha de corte: 2026-06-22 · 14 iniciativas (10 de negocio + 4 de capacidades del equipo BD)"
ws["A2"].font = Font(italic=True, color="595959", size=10)
ws.row_dimensions[1].height = 22

HEADER_ROW = 4
for c, name in enumerate(COLUMNS, start=1):
    cell = ws.cell(row=HEADER_ROW, column=c, value=name)
    cell.fill = HEADER_FILL
    cell.font = HEADER_FONT
    cell.alignment = CENTER
    cell.border = BORDER
ws.row_dimensions[HEADER_ROW].height = 32

for r, row in enumerate(ROWS, start=HEADER_ROW + 1):
    for c, value in enumerate(row, start=1):
        cell = ws.cell(row=r, column=c, value=value)
        cell.border = BORDER
        cell.alignment = WRAP_TOP if c in WRAP_COLS else Alignment(vertical="top")
        if c == COL_ESTADO:
            cell.alignment = CENTER
            cell.fill = ESTADO_FILL.get(value, PatternFill())
            cell.font = Font(bold=True, size=10)
        if c == COL_AVANCE:
            cell.number_format = "0%"
            cell.alignment = CENTER
        if c == COL_FICHAS:
            cell.alignment = CENTER

for c, w in enumerate(WIDTHS, start=1):
    ws.column_dimensions[get_column_letter(c)].width = w

first_data = HEADER_ROW + 1
last_data = HEADER_ROW + len(ROWS)
ws.auto_filter.ref = f"A{HEADER_ROW}:{last_col}{last_data}"
ws.freeze_panes = f"D{first_data}"  # congela Clave · Épica · Iniciativa

avance_letter = get_column_letter(COL_AVANCE)
ws.conditional_formatting.add(
    f"{avance_letter}{first_data}:{avance_letter}{last_data}",
    DataBarRule(start_type="num", start_value=0, end_type="num", end_value=1,
                color="4472C4", showValue=True),
)

# ----------------------------------------------------------------------------
# Hoja de leyenda y notas
# ----------------------------------------------------------------------------
ws2 = wb.create_sheet("Leyenda y notas")
ws2.column_dimensions["A"].width = 34
ws2.column_dimensions["B"].width = 94
ws2["A1"] = "Leyenda y notas metodológicas"
ws2["A1"].font = TITLE_FONT
notas = [
    ("Fecha de corte", "2026-06-22. Sincronizado con el Excel de trabajo del equipo."),
    ("Prioridad", "«Priorizada por negocio» = demanda de un área cliente · «Capacidades equipo BD» = "
                  "proyectos internos de arquitectura/herramientas del Chapter BD (Q-11 a Q-14)."),
    ("Objetivo del proyecto", "El para qué de negocio de la iniciativa (resultado buscado)."),
    ("Intervención de diseño de conducta", "La solución/artefacto de behavioral design que se diseña e "
                  "implementa: la palanca conductual concreta (guía, mensaje, programa, bot, kit, framework, etc.)."),
    ("% Avance", "Avance por iniciativa según el equipo (Excel de trabajo)."),
    ("Equipo que requiere el servicio", "Área cliente del servicio de Behavioral Design. «Chapter BD» = "
                  "trabajo interno del equipo (capacidades)."),
    ("Stakeholder", "Tomado del board original. Las iniciativas de capacidades BD no tienen stakeholder externo (—)."),
    ("Equipo Behavioral Design", "Behavioral designers asignados. «Todos» en las iniciativas de capacidades BD."),
    ("Fichas", "Capacidad por iniciativa (regla 8/2). CAPACIDAD: con Q-10 asignado a Stef, Stef acumula 11 "
               "fichas (Q-1, Q-3, Q-4, Q-10) → supera el máximo de 10; Alejandro queda en 9 (sobreasignado). "
               "Revisar reasignación. Q-11 a Q-14 las trabaja «Todos» sin fichas asignadas."),
    ("(est.) en Impacto", "Estimación basada en benchmarks de industria + investigación interna del repo, "
                          "no cifra comprometida por RIMAC."),
    ("Cifras duras", "Q-4 (S/600k), Q-8 (S/1.8M) y Q-10 (Wellby/CSAT/NPS) provienen del board original."),
    ("Correcciones aplicadas", "Typos del Excel de trabajo: «escencial»→«esencial», «Aglidad»→«Agilidad», "
                  "«cmabio»→«cambio», «cinetífica»→«científica». Impacto de Q-11 estaba truncado («…uso efic») "
                  "y se completó a «…uso eficiente de seguros»."),
    ("Estados (colores)", "Verde = Done · Azul = In Review · Lila = Diseñado · Amarillo = In Progress · "
                          "Rojo = To Do (Block)."),
]
for i, (k, v) in enumerate(notas, start=3):
    ws2.cell(row=i, column=1, value=k).font = Font(bold=True, color=NAVY)
    ws2.cell(row=i, column=1).alignment = Alignment(vertical="top", wrap_text=True)
    c = ws2.cell(row=i, column=2, value=v)
    c.alignment = Alignment(wrap_text=True, vertical="top")
    ws2.row_dimensions[i].height = 46

OUT = Path(__file__).resolve().parent / "Status_Proyectos_Behavioral_Design.xlsx"
wb.save(OUT)
print("Generado:", OUT, "| filas:", len(ROWS), "| columnas:", len(COLUMNS))
