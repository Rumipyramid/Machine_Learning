#!/usr/bin/env python3
"""Genera la matriz de status de proyectos Behavioral Design (RIMAC) en Excel.

Fuente de datos: TABLERO_BEHOLDER.md + board original (Behavioral_Design.pdf).
Uso: python reportes/generar_matriz_status.py
Salida: reportes/Status_Proyectos_Behavioral_Design.xlsx
"""
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.formatting.rule import DataBarRule
from openpyxl.utils import get_column_letter

# ----------------------------------------------------------------------------
# Datos. Cada fila = una iniciativa (quest). % avance y "equipo que requiere el
# servicio" son estimación/inferencia (ver hoja "Leyenda y notas").
# ----------------------------------------------------------------------------
COLUMNS = [
    "Clave", "Épica", "Iniciativa", "Objetivo", "Estado (Jira)",
    "Status (detalle)", "% Avance", "Equipo que requiere el servicio",
    "Stakeholder", "Equipo Behavioral Design", "Fichas", "Fecha de cierre",
    "Riesgos", "Impacto esperado",
]

ROWS = [
    ["Q-1", "Guías resumidas (Pólizas simples)",
     "Guías resumidas — 4 nuevos productos AMI",
     "Promover el entendimiento y uso eficiente de los seguros de salud",
     "In Progress", "WIP - Documento de primer producto en agencia", 0.40,
     "AMI – Salud (Producto)", "Estrella Damian, Soiky Bardales",
     "Stef, Felipe, Alejandro", 8, "30 de junio",
     "Cambio en el roadmap (de 1 guía a 4 productos)",
     "↓ ~25–30% casos NPS «no recibí información» (est.); ataca la palanca #1 de desconfianza en Perú"],

    ["Q-2", "Renovación AMI",
     "Batería de soluciones para la renovación AMI",
     "Reducir el churn y reclamos por cambios en la renovación",
     "In Progress", "Carta de renovación implementada; 3 soluciones diseñadas on hold", 0.40,
     "AMI – Renovación / Salud", "Estrella Damian, Soiky Bardales",
     "Alejandro", 2, "30 de junio",
     "La carta por sí sola no cubre la necesidad del usuario",
     "+3–5 pp retención sobre base industria ~84% y ↓ reclamos (est.); depende de desbloquear las 3 soluciones on hold"],

    ["Q-3", "Guías resumidas (Pólizas simples)",
     "Guías resumidas — 5 clientes TOP EPS",
     "Promover el entendimiento y uso eficiente de los seguros de salud",
     "Done", "Implementado", 1.00,
     "EPS – Salud Corporativa", "Kevin Crisanto, María Alejandra Valcarcel",
     "Stef, Felipe, Alejandro", 3, "Julio 2026",
     "Producto pide no comunicar algunos servicios valorados por el usuario",
     "Renovación de cuentas TOP EPS (incl. Antapacay) + ↓ «no recibí información» en corporativo; alto valor por cuenta"],

    ["Q-4", "Evolution+: Cobranzas",
     "Captura de datos para conciliación de facturas de proveedores",
     "Promover la captura de datos para conciliación de facturas proveedores",
     "In Progress", "En fase de research", 0.20,
     "Cobranzas / Finanzas", "Rosemary Moyano",
     "Stef", 4, "30 de junio",
     "Track de diseño aprobado sin explorar la problemática",
     "Liberación de S/600k provisionados"],

    ["Q-5", "Back to Basics FFVV Vida Individual",
     "Mensajes de primer contacto",
     "Promover el agendamiento de citas comerciales",
     "To Do (Block)", "Block", 0.10,
     "FFVV Vida Individual", "Diana Riofrío, Jaime Huerta",
     "Alejandro", 1, "Julio 2026",
     "No existe estrategia definida de contacto bajo contexto CUA (bloqueado)",
     "+20–30% agendamiento de citas en primer contacto (est., potencial — bloqueado por estrategia CUA)"],

    ["Q-6", "Loyalty",
     "Programa de lealtad (MVP/piloto)",
     "Diseñar un programa de lealtad del ecosistema que asegure la permanencia de los asegurados",
     "In Progress", "Diseñando y viabilizando la propuesta MVP/piloto (3–6 meses)", 0.30,
     "Loyalty / Ecosistema RIMAC", "Denisse Galvez, Lucía Ramos, Jorge Sarmiento",
     "Alejandro", 2, "—",
     "—",
     "Permanencia base RIMAC (1,250 MM clientes); benchmark loyalty +20–25% retención y +40% cross-sell (est.)"],

    ["Q-7", "Back to Basics FFVV Vida Individual",
     "Universidad Vida",
     "Acelerar la curva de aprendizaje de asesores nuevos / mejorar ratio de conversión",
     "In Progress", "WIP", 0.40,
     "FFVV Vida Individual", "Diana Riofrío, Jaime Huerta",
     "Melissa, Alejandro", 4, "Julio 2026",
     "Capacidad limitada del equipo de learning",
     "−25–40% tiempo de ramp-up de asesores jr + mejor conversión y NPS Venta (est.)"],

    ["Q-8", "Back to Basics FFVV Vida Individual",
     "Skill AIDA Bot Trainer + reportería",
     "Promover el aprendizaje y capacitación de asesores y dar visibilidad de expertise a jefaturas FFVV. "
     "Agente con el que el asesor practica casos; genera puntaje de efectividad y alertas por falta de "
     "principios básicos de experiencia (CX), visibles a jefaturas FFVV.",
     "In Review", "Prototipo diseñado y validada usabilidad y valoración de usuarios", 0.80,
     "FFVV Vida Individual", "Diana Riofrío, Jaime Huerta",
     "Felipe, Melissa", 6, "—",
     "AIDA no cumple el task; entra a comité de priorización; 3 herramientas en paralelo",
     "+efectividad del asesor (medible vía el puntaje del bot) y consistencia CX; práctica con feedback acelera ramp "
     "(−25–40%, est.); jefaturas hacen coaching dirigido. Ahorro proyectado S/1.8M (cifra del board, base por documentar)"],

    ["Q-9", "Back to Basics FFVV Vida Individual",
     "Kit de Social Selling",
     "Promover la generación de leads y agendamientos para FFVV",
     "In Progress", "WIP", 0.40,
     "FFVV Vida Individual", "Diana Riofrío, Jaime Huerta",
     "Melissa", 3, "Julio 2026",
     "Recursos limitados de contenido + falta de incentivos + falta de monitoreo",
     "+leads/agendamientos FFVV; social selling 15–25% conversión lead→cita, CPL −30–50% (est.)"],

    ["Q-10", "Bienestar 360",
     "Bienestar 360",
     "Piloto con colaboradores Rimac para construir hábitos saludables sostenibles",
     "Done", "Mantenimiento", 1.00,
     "Bienestar / Estar Bien", "Erika Echegaray, Belem Rodríguez; Solange Soto, Rosa Díaz",
     "— (Equipo Bienestar / Estar Bien)", "—", "Setiembre 2026 (solo acompañamiento)",
     "Presupuesto y recursos limitados para la siguiente versión",
     "+3 ptos Wellby · CSAT 4.6/5 · NPS 78"],
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
    "In Progress": PatternFill("solid", fgColor="FFF2CC"),
    "To Do (Block)": PatternFill("solid", fgColor="FFC7CE"),
}

WIDTHS = [7, 30, 30, 40, 14, 34, 10, 26, 28, 24, 8, 22, 40, 52]
WRAP_COLS = {2, 3, 4, 6, 8, 9, 10, 13, 14}  # 1-based columns to wrap

# ----------------------------------------------------------------------------
# Construcción
# ----------------------------------------------------------------------------
wb = Workbook()
ws = wb.active
ws.title = "Status Proyectos"

# Título
last_col = get_column_letter(len(COLUMNS))
ws.merge_cells(f"A1:{last_col}1")
ws["A1"] = "Matriz de Status — Behavioral Design (RIMAC)"
ws["A1"].font = TITLE_FONT
ws.merge_cells(f"A2:{last_col}2")
ws["A2"] = "Cierre Q2 2026 · Fecha de corte: 2026-06-22 · 6 épicas · 10 iniciativas"
ws["A2"].font = Font(italic=True, color="595959", size=10)
ws.row_dimensions[1].height = 22

HEADER_ROW = 4
for c, name in enumerate(COLUMNS, start=1):
    cell = ws.cell(row=HEADER_ROW, column=c, value=name)
    cell.fill = HEADER_FILL
    cell.font = HEADER_FONT
    cell.alignment = CENTER
    cell.border = BORDER
ws.row_dimensions[HEADER_ROW].height = 30

for r, row in enumerate(ROWS, start=HEADER_ROW + 1):
    for c, value in enumerate(row, start=1):
        cell = ws.cell(row=r, column=c, value=value)
        cell.border = BORDER
        cell.alignment = WRAP_TOP if c in WRAP_COLS else Alignment(vertical="top")
        if c == 5:  # Estado
            cell.alignment = CENTER
            cell.fill = ESTADO_FILL.get(value, PatternFill())
            cell.font = Font(bold=True, size=10)
        if c == 7:  # % Avance
            cell.number_format = "0%"
            cell.alignment = CENTER
        if c == 11:  # Fichas
            cell.alignment = CENTER

# Anchos de columna
for c, w in enumerate(WIDTHS, start=1):
    ws.column_dimensions[get_column_letter(c)].width = w

# Filtro + panel congelado
first_data = HEADER_ROW + 1
last_data = HEADER_ROW + len(ROWS)
ws.auto_filter.ref = f"A{HEADER_ROW}:{last_col}{last_data}"
ws.freeze_panes = f"C{first_data}"

# Barras de datos en % Avance (columna G)
ws.conditional_formatting.add(
    f"G{first_data}:G{last_data}",
    DataBarRule(start_type="num", start_value=0, end_type="num", end_value=1,
                color="4472C4", showValue=True),
)

# ----------------------------------------------------------------------------
# Hoja de leyenda y notas
# ----------------------------------------------------------------------------
ws2 = wb.create_sheet("Leyenda y notas")
ws2.column_dimensions["A"].width = 30
ws2.column_dimensions["B"].width = 90
ws2["A1"] = "Leyenda y notas metodológicas"
ws2["A1"].font = TITLE_FONT
notas = [
    ("Fecha de corte", "2026-06-22"),
    ("% Avance", "Estimación derivada del estado/status de cada iniciativa (no es un % reportado por el "
                  "equipo). Done/Mantenimiento = 100%; In Review = 80%; In Progress = 20–40% según detalle; "
                  "Block = 10%. Ajustar con el avance real de cada líder."),
    ("Equipo que requiere el servicio", "Campo inferido a partir del stakeholder y la iniciativa "
                  "(área de negocio cliente del servicio de Behavioral Design). Confirmar con el equipo."),
    ("Stakeholder", "Tomado del board original (Behavioral_Design.pdf)."),
    ("Equipo Behavioral Design", "Behavioral designers asignados (assignees)."),
    ("Fichas", "Capacidad asignada (8 de 10 fichas comprometibles por persona). Distribución propuesta, "
               "pendiente de confirmación. Alerta de capacidad: Alejandro 9/8 (🔴 sobreasignado)."),
    ("(est.) en Impacto", "Estimación basada en benchmarks de industria + investigación interna del repo, "
                          "no cifra comprometida por RIMAC."),
    ("Cifras duras", "Q-4 (S/600k), Q-8 (S/1.8M) y Q-10 (Wellby/CSAT/NPS) provienen del board original."),
    ("Estados (colores)", "Verde = Done · Azul = In Review · Amarillo = In Progress · Rojo = To Do (Block)."),
]
for i, (k, v) in enumerate(notas, start=3):
    ws2.cell(row=i, column=1, value=k).font = Font(bold=True, color=NAVY)
    ws2.cell(row=i, column=1).alignment = Alignment(vertical="top")
    c = ws2.cell(row=i, column=2, value=v)
    c.alignment = Alignment(wrap_text=True, vertical="top")
    ws2.row_dimensions[i].height = 42

OUT = Path(__file__).resolve().parent / "Status_Proyectos_Behavioral_Design.xlsx"
wb.save(OUT)
print("Generado:", OUT)
