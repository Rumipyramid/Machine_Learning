#!/usr/bin/env python3
"""Genera la matriz de status de proyectos Behavioral Design (RIMAC) en Excel.

Fuente: Excel de trabajo del equipo + Roadmap Q3-2026 (Chapter SD1).
Actualizado al 2026-06-22. El PDF del roadmap tenía el texto distorsionado;
los campos inciertos van marcados «(por confirmar)» (ver hoja "Leyenda y notas").
Uso: python reportes/generar_matriz_status.py
Salida: reportes/Status_Proyectos_Behavioral_Design.xlsx
"""
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.formatting.rule import DataBarRule
from openpyxl.utils import get_column_letter

COLUMNS = [
    "Clave", "Épica", "Iniciativa", "Prioridad", "Objetivo del proyecto",
    "Intervención de diseño de conducta", "Estado (Jira)", "Status (detalle)",
    "% Avance", "Equipo que requiere el servicio", "Stakeholder",
    "Equipo Behavioral Design", "Fichas", "Fecha de entrega", "Riesgos",
    "Impacto esperado",
]

NEGOCIO = "Priorizada por negocio"
CAPACIDAD = "Capacidades equipo BD"
BACKLOG = "Backlog (Chapter SD1)"

ROWS = [
    # ----- Iniciativas existentes (actualizadas con el Roadmap Q3-2026) -----
    ["Q-1", "Guías resumidas (Pólizas simples)", "Guías resumidas — 4 nuevos productos AMI", NEGOCIO,
     "Promover el entendimiento y uso eficiente de los seguros de salud",
     "Rediseño de la información del producto para hacerla clara y comprensible (ataca la barrera de «falta de información»).",
     "In Progress", "Diseño 1/4; roadmap reajustado −6 semanas; presentación del entregable 30/6; + flyers de venta (1×producto + comparativo)", 0.40,
     "AMI – Salud (Producto)", "Estrella Damian, Soiky Bardales", "Stef, Felipe, Alejandro", 8, "30/06 (presentación)",
     "Cambio en el roadmap (de 1 guía a 4 productos); reajuste −6 semanas",
     "↓ ~25–30% casos NPS «no recibí información» (est.); ataca la palanca #1 de desconfianza en Perú"],

    ["Q-2", "Renovación AMI", "Batería de soluciones para la renovación AMI", NEGOCIO,
     "Reducir el churn y reclamos por cambios en la renovación",
     "Comunicación proactiva que reduce incertidumbre y fricción ante el cambio (speeches de primer contacto + carta de renovación).",
     "In Review", "Guía de comunicación con escenarios y speeches: entregada; feedback y ajustes finales. Carta de renovación: Oncológicos BBVA (diseño acotado implementado)", 0.90,
     "AMI – Renovación / Salud", "Estrella Damian, Soiky Bardales", "Alejandro", 2, "30 de junio",
     "La carta por sí sola no cubre la necesidad del usuario",
     "+3–5 pp retención sobre base industria ~84% y ↓ reclamos (est.); depende de desbloquear las 3 soluciones on hold"],

    ["Q-3", "Guías resumidas (Pólizas simples)", "Guías resumidas — EPS (Top 4 cuentas + Multiempresa)", NEGOCIO,
     "Promover el entendimiento y uso eficiente de los seguros de salud",
     "Misma palanca de claridad/comprensión aplicada a cuentas clave.",
     "In Review", "Top 4 cuentas: 2/4 entregadas, 2/4 en revisión; Multiempresa: entregada; ajustes del entregable y presentación final", 0.80,
     "EPS – Salud Corporativa", "Kevin Crisanto, María Alejandra Valcarcel", "Stef, Felipe, Alejandro", 3, "Julio 2026",
     "Producto pide no comunicar algunos servicios valorados por el usuario",
     "Renovación de cuentas TOP EPS (incl. Antapacay) + ↓ «no recibí información» en corporativo; alto valor por cuenta"],

    ["Q-4", "Evolution+: Cobranzas", "Optimización de Cobranzas B2B", NEGOCIO,
     "Promover la captura de datos para conciliación de facturas proveedores",
     "Rediseño del flujo de captura de datos (Evolution+) para facilitar/incentivar que los proveedores entreguen la información de conciliación.",
     "In Progress", "12 entrevistas brokers/clientes B2B (entendimiento E2E del pago, pains de confirmación) → bajada/análisis → diseño de la nueva experiencia y pilotos → ejecutar piloto y definir experiencia final", 0.20,
     "Cobranzas / Finanzas", "Rosemary Moyano", "Stef", 4, "Q3 2026",
     "Track de diseño aprobado sin explorar la problemática",
     "Liberación de S/600k provisionados"],

    ["Q-5", "Back to Basics FFVV Vida Individual", "Mensajes de primer contacto", NEGOCIO,
     "Promover el agendamiento de citas comerciales",
     "Mensajes de primer contacto (copys/secuencia) que enmarcan la propuesta y reducen la fricción para agendar una cita comercial.",
     "In Progress", "Estrategia de primer contacto alineado a CUA (en definición → desbloqueándose); speeches de primer contacto", 0.30,
     "FFVV Vida Individual", "Diana Riofrío, Jaime Huerta", "Alejandro", 1, "Julio 2026",
     "Estrategia de contacto bajo contexto CUA en definición (antes bloqueado)",
     "+20–30% agendamiento de citas en primer contacto (est.)"],

    ["Q-6", "Loyalty", "Programa de lealtad — Piloto/MVP", NEGOCIO,
     "Diseñar un programa de lealtad del ecosistema que asegure la permanencia de los asegurados",
     "Diseño del programa de lealtad (mecánica de recompensas/beneficios) para reforzar la permanencia y el comportamiento de continuidad del asegurado.",
     "In Progress", "Piloto/MVP: definición de operativa, niveles de beneficios y clientes participantes (Meli) → envío de solicitud + push de participantes (Meli) → inicio y soporte del piloto (Alejandro)", 0.60,
     "Loyalty / Ecosistema RIMAC", "Denisse Galvez, Lucía Ramos, Jorge Sarmiento", "Meli, Alejandro", 2, "Q3 2026 (piloto 24/08–08/09)",
     "—",
     "Permanencia base RIMAC (1,250 MM clientes); benchmark loyalty +20–25% retención y +40% cross-sell (est.)"],

    ["Q-7", "Back to Basics FFVV Vida Individual", "Universidad Vida", NEGOCIO,
     "Acelerar la curva de aprendizaje de asesores nuevos / mejorar ratio de conversión",
     "Programa de formación «Universidad Vida» para asesores nuevos: acelera la curva de aprendizaje con práctica estructurada.",
     "Diseñado", "Asistencia a onboarding de FFVV actual; contenido listo, falta diseño instruccional (Learning)", 0.40,
     "FFVV Vida Individual", "Diana Riofrío, Jaime Huerta", "Melissa, Alejandro", 4, "Julio 2026",
     "Capacidad limitada del equipo de learning",
     "−25–40% tiempo de ramp-up de asesores jr + mejor conversión y NPS Venta (est.)"],

    ["Q-8", "Back to Basics FFVV Vida Individual", "Copiloto del Asesor: AIDA — Bot trainer + reportería", NEGOCIO,
     "Promover el aprendizaje y capacitación de asesores y dar visibilidad de expertise a jefaturas FFVV",
     "Agente entrenador (bot) de práctica de casos con puntaje de efectividad y alertas por falta de principios básicos de experiencia (CX); práctica deliberada con feedback y visibilidad a jefaturas.",
     "In Review", "Prototipo diseñado y validada usabilidad y valoración de usuarios; en track de Back to Basics | Venta Vida", 0.80,
     "FFVV Vida Individual", "Diana Riofrío, Jaime Huerta", "Felipe, Melissa", 6, "—",
     "AIDA no cumple el task; entra a comité de priorización; 3 herramientas en paralelo",
     "+efectividad del asesor (medible vía el puntaje del bot) y consistencia CX; práctica con feedback acelera ramp "
     "(−25–40%, est.); jefaturas hacen coaching dirigido. Ahorro proyectado S/1.8M (cifra del board, base por documentar)"],

    ["Q-9", "Back to Basics FFVV Vida Individual", "Kit de Social Selling", NEGOCIO,
     "Promover la generación de leads y agendamientos para FFVV",
     "Estrategia y contenido del Social Selling (contenido + herramientas de huella digital) para que la FFVV genere leads y agendamientos.",
     "In Progress", "Estrategia y contenido del Social Selling; en track de Back to Basics | Venta Vida", 0.40,
     "FFVV Vida Individual", "Diana Riofrío, Jaime Huerta", "Melissa", 3, "Julio 2026",
     "Recursos limitados de contenido + falta de incentivos + falta de monitoreo",
     "+leads/agendamientos FFVV; social selling 15–25% conversión lead→cita, CPL −30–50% (est.)"],

    ["Q-10", "Bienestar 360", "Bienestar 360", NEGOCIO,
     "Piloto con colaboradores Rimac para construir hábitos saludables sostenibles",
     "Programa de hábitos saludables (piloto Bienestar 360) para construir y sostener hábitos de bienestar en colaboradores.",
     "Done", "Implementado y en mantenimiento; cierre de playbook del programa + acompañamiento a la fase de mantenimiento", 1.00,
     "Bienestar / Estar Bien", "Erika Echegaray, Belem Rodríguez; Solange Soto, Rosa Díaz", "Stef", 3,
     "Setiembre 2026 (solo acompañamiento)",
     "Presupuesto y recursos limitados para la siguiente versión",
     "+3 ptos Wellby · CSAT 4.6/5 · NPS 78"],

    ["Q-11", "Modelo de entendimiento y uso eficiente de seguros", "Arquitectura BD", CAPACIDAD,
     "Definir framework de trabajo para ecosistema de entendimiento y uso eficiente de seguros",
     "Arquitectura del conocimiento",
     "In Progress", "Framework de trabajo terminado; falta alinear con los distintos frentes involucrados. En roadmap Q3: Backlog (Arquitectura BD)", 0.80,
     "Chapter BD", "—", "Todos", "—", "—",
     "—",
     "Framework para potenciar el entendimiento y uso eficiente de seguros"],

    ["Q-12", "Sistema de generación de usuarios sintéticos", "Arquitectura BD", CAPACIDAD,
     "Crear recurso de exploración para conocimiento esencial de seguros y comportamiento con los seguros en Perú",
     "Creación de herramienta de testeo",
     "Diseñado", "Terminado, por validar. En roadmap Q3: Backlog (Arquitectura BD)", 0.90,
     "Chapter BD", "—", "Todos", "—", "—",
     "—",
     "Agilidad en el testeo de preguntas ya exploradas sobre conducta con seguros"],

    ["Q-13", "Modelo de cambio de hábitos", "Arquitectura BD", CAPACIDAD,
     "Definir framework de trabajo para ecosistema de entendimiento y uso eficiente de seguros",
     "Arquitectura del conocimiento",
     "Done", "Terminado y validado. En roadmap Q3: Backlog (Arquitectura BD)", 1.00,
     "Chapter BD", "—", "Todos", "—", "—",
     "—",
     "Framework para trabajo de iniciativas relacionadas al cambio de hábitos"],

    ["Q-14", "Skill para desk research con rigurosidad científica", "Arquitectura BD", CAPACIDAD,
     "Potenciar el desk research con parámetros de búsqueda con rigurosidad metodológica y creación de repositorio de conocimiento",
     "Creación de herramienta de research",
     "Diseñado", "Terminado, por validar. En roadmap Q3: Backlog (Arquitectura BD)", 0.90,
     "Chapter BD", "—", "Todos", "—", "—",
     "—",
     "Agilidad y calidad de los entregables de investigación de escritorio"],

    # ----- Iniciativas nuevas del Roadmap Q3-2026 (Chapter SD1) -----
    ["Q-15", "Nuevo seguro AMI", "Nuevos planes AMI + Seguro PT/P", NEGOCIO,
     "Lanzar nuevos planes AMI con materiales de venta y capacitación a la FFVV",
     "Entrega de guías resumidas, carta de bienvenida, speech de venta y flyers; capacitación FFVV; lineamientos de experiencia de venta y siniestros (Seguro PT/P).",
     "In Progress", "Entrega 1ª guía (plan vital, maquetado de agencia), carta de bienvenida, speech de venta (Speech Analytics), flyer; apoyo en nombres de planes (Marketing); capacitación FFVV; seguimiento a lanzamiento. Seguro PT/P: lineamientos de experiencia (por confirmar)", 0.30,
     "AMI – Salud (Producto)", "(por confirmar)", "(por confirmar)", "—", "Q3 2026",
     "—", "—"],

    ["Q-16", "Salud integral", "MBI – Vivo (piloto)", NEGOCIO,
     "Pilotear MBI – Vivo con un segmento definido con Salud / Estar Bien",
     "Diseño y aterrizaje de un piloto (propuesta, presupuesto, producción y lanzamiento).",
     "In Progress", "Presentación y revisión de la propuesta del piloto; retomar conversaciones con stakeholders (Salud / Estar Bien) para definir el segmento; definición de presupuesto; aterrizaje y aprobación; producción y lanzamiento del piloto", 0.20,
     "Salud / Estar Bien", "(por confirmar)", "(por confirmar)", "—", "Q3 2026",
     "—", "—"],

    ["Q-17", "Evolution+: Reservas Vida", "Negociación y liberación de reservas vida", NEGOCIO,
     "Liberar reservas de vida mediante una nueva experiencia de gestión",
     "Diseño de la experiencia vista cliente E2E (4 fases) + piloto + co-diseño del escalamiento.",
     "In Progress", "Diseño de la experiencia E2E en 4 fases; implementación del piloto; co-diseñar el escalamiento con el equipo de proceso; adecuar a gestión externa (Rimac empresa tercera); seguimiento al despliegue", 0.20,
     "Finanzas / Vida", "(por confirmar)", "(por confirmar)", "—", "Q3 2026",
     "—", "—"],

    ["Q-18", "Evolution+: AMI continuidad", "Optimización de venta nueva AMI con continuidad", NEGOCIO,
     "Optimizar la venta nueva AMI con continuidad",
     "Piloto de venta por el hub + actualización de viabilidad financiera + definición de escalamiento.",
     "In Progress", "Implementación del piloto para venta por el hub; actualización de la viabilidad financiera (caída en venta vs costo potencial de atención); definición de escalamiento a otros frentes (brokers, online y VIP)", 0.20,
     "AMI – Salud / Comercial", "(por confirmar)", "(por confirmar)", "—", "Q3 2026",
     "—", "—"],

    ["Q-19", "Comunicaciones Loyalty", "Diseño de piezas y journeys de comunicación", NEGOCIO,
     "Soportar Loyalty/Renovación con piezas y journeys de comunicación",
     "Diseño de piezas y journeys (Angio Hogar/Vida, Protección Múltiple, Venta Hospitalaria, Renovación, Cobranza transversal).",
     "In Progress", "Diseño de piezas y journeys: Angio Hogar Total, Seguro Reciclar (journey), Protección Múltiple / Venta Hospitalaria, Renovación / WhatsApp, Cobranza transversal (imagen Royal)", 0.30,
     "Loyalty / Comunicaciones", "(por confirmar)", "(por confirmar)", "—", "Q3 2026",
     "—", "—"],

    ["Q-20", "Loyalty Empresas", "Modelo de relacionamiento empresas + Propuesta de valor", NEGOCIO,
     "Definir el modelo de relacionamiento y la propuesta de valor para empresas",
     "Talleres de ideación + benchmark + modelos de relacionamiento (directo, brokers, corporativo) + propuesta de valor.",
     "In Progress", "Taller de ideación (30/06 presencial Lima · 02/07 virtual provincia); modelos de relacionamiento empresas directo / brokers / corporativo (benchmark, análisis, entregable y presentación final); potenciar storytelling de la propuesta de valor (con Marketing)", 0.30,
     "Loyalty / Empresas", "(por confirmar)", "(por confirmar)", "—", "Q3 2026",
     "—", "—"],

    ["Q-21", "Renovación", "RIMAC Wrap (tangibilización pre-renovación)", BACKLOG,
     "Tangibilizar el valor antes de la renovación",
     "Toque de tangibilización pre-renovación (RIMAC Wrap).",
     "Backlog", "Backlog del Chapter SD1 (sin sprint asignado)", 0.0,
     "Renovación", "(por confirmar)", "(por confirmar)", "—", "—",
     "—", "—"],

    ["Q-22", "Renovación", "Recordatorio multicanal (SMS/WhatsApp/Push)", BACKLOG,
     "Reforzar la renovación con recordatorios multicanal",
     "Toques adicionales de recordatorio multicanal (SMS, WhatsApp y Push Notifications).",
     "Backlog", "Backlog del Chapter SD1 (sin sprint asignado)", 0.0,
     "Renovación", "(por confirmar)", "(por confirmar)", "—", "—",
     "—", "—"],

    ["Q-23", "Venta", "Sistema de incentivos orientados a la experiencia", BACKLOG,
     "Orientar los incentivos de asesores hacia la experiencia",
     "Diseño de un sistema de incentivos para asesores orientado a la experiencia (Back to Basics).",
     "Backlog", "Backlog del Chapter SD1 (sin sprint asignado)", 0.0,
     "Venta", "(por confirmar)", "(por confirmar)", "—", "—",
     "—", "—"],

    ["Q-24", "Nuevo Modelo de Ventas", "Convenios y Financieros — nuevo modelo de venta", BACKLOG,
     "Definir un nuevo modelo de venta para Convenios y Financieros",
     "Nuevo modelo de venta para Convenios y Financieros.",
     "Backlog", "Backlog del Chapter SD1. Convenios (sponsor Diana Riofrío y Patricia Romero); Financieros (sponsor Claro Gomez y Patricia Romero)", 0.0,
     "Venta / Convenios y Financieros", "Diana Riofrío, Patricia Romero (Convenios); Claro Gomez, Patricia Romero (Financieros)", "(por confirmar)", "—", "—",
     "—", "—"],

    ["Q-25", "Vida Individual", "Experiencia Postventa", BACKLOG,
     "Mejorar la experiencia postventa de Vida Individual",
     "Rediseño de la experiencia postventa.",
     "Backlog", "Backlog del Chapter SD1 (sponsor Diana Riofrío)", 0.0,
     "Vida Individual / Posventa", "Diana Riofrío", "(por confirmar)", "—", "—",
     "—", "—"],

    ["Q-26", "Ahorro Salud", "Derivación eficiente MER", BACKLOG,
     "Hacer más eficiente la derivación (MER) en Ahorro Salud",
     "Rediseño de la derivación eficiente MER.",
     "Backlog", "Backlog del Chapter SD1 (sin sprint asignado)", 0.0,
     "Ahorro Salud", "(por confirmar)", "(por confirmar)", "—", "—",
     "—", "—"],
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
    "Backlog": PatternFill("solid", fgColor="D9D9D9"),
}

COL_ESTADO = 7
COL_AVANCE = 9
COL_FICHAS = 13

WIDTHS = [7, 30, 28, 20, 38, 44, 14, 38, 10, 22, 26, 20, 8, 20, 30, 44]
WRAP_COLS = {2, 3, 4, 5, 6, 8, 10, 11, 12, 15, 16}

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
ws["A2"] = ("Roadmap Q3-2026 (Chapter SD1) · Fecha de corte: 2026-06-22 · "
            "26 iniciativas (14 previas + 12 nuevas del roadmap)")
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
ws.freeze_panes = f"D{first_data}"

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
ws2.column_dimensions["B"].width = 96
ws2["A1"] = "Leyenda y notas metodológicas"
ws2["A1"].font = TITLE_FONT
notas = [
    ("Fuente / corte", "2026-06-22. Actualizado con el Roadmap Q3-2026 (Chapter SD1). El PDF del roadmap tenía "
                       "el texto distorsionado; los campos inciertos van marcados «(por confirmar)»."),
    ("Conflictos detectados", "Q-3: el Excel previo decía «5 clientes / Done»; el roadmap dice «Top 4 cuentas "
                  "(2/4 entregadas, 2/4 en revisión) + Multiempresa entregada» → quedó In Review. "
                  "Q-5: estaba «To Do (Block)»; el roadmap muestra «Estrategia de primer contacto alineado a CUA» "
                  "activa → pasó a In Progress (desbloqueándose). Confirmar ambos."),
    ("Iniciativas nuevas (Q-15–Q-26)", "Del roadmap Q3 Chapter SD1: Nuevo seguro AMI, MBI-Vivo, Evolution+ "
                  "Reservas Vida, Evolution+ AMI continuidad, Comunicaciones Loyalty, Modelo de relacionamiento "
                  "empresas, RIMAC Wrap, Recordatorio multicanal, Sistema de incentivos, Nuevo modelo de ventas "
                  "Convenios/Financieros, Vida Individual Postventa, Derivación eficiente MER. Owners y fichas por asignar."),
    ("Prioridad", "«Priorizada por negocio» · «Capacidades equipo BD» (Q-11–Q-14) · «Backlog (Chapter SD1)» "
                  "para iniciativas nuevas sin sprint asignado."),
    ("Objetivo del proyecto", "El para qué de negocio de la iniciativa (resultado buscado)."),
    ("Intervención de diseño de conducta", "La solución/artefacto de behavioral design que se diseña: la palanca "
                  "conductual concreta (guía, mensaje, programa, bot, kit, framework, etc.)."),
    ("% Avance", "Avance por iniciativa según el equipo / roadmap. Iniciativas nuevas: estimación inicial (por confirmar)."),
    ("Equipo que requiere el servicio", "Área cliente del servicio de BD. «Chapter BD» = trabajo interno (capacidades)."),
    ("Stakeholder", "Del board original / roadmap. Las nuevas iniciativas tienen stakeholder «(por confirmar)» salvo "
                    "Convenios/Financieros (Diana Riofrío, Patricia Romero, Claro Gomez) y Postventa (Diana Riofrío)."),
    ("Equipo Behavioral Design", "Behavioral designers asignados. Loyalty (Q-6): Meli + Alejandro (según roadmap)."),
    ("Fichas", "Capacidad por iniciativa (regla 8/2). PENDIENTE: Stef acumula 11 fichas (Q-1,Q-3,Q-4,Q-10) → supera "
               "el máximo de 10; Alejandro en 9 (sobreasignado). Las iniciativas nuevas (Q-15–Q-26) están sin fichas asignadas."),
    ("(est.) en Impacto", "Estimación basada en benchmarks + investigación interna; no cifra comprometida por RIMAC."),
    ("Cifras duras", "Q-4 (S/600k), Q-8 (S/1.8M) y Q-10 (Wellby/CSAT/NPS) provienen del board original."),
    ("Estados (colores)", "Verde = Done · Azul = In Review · Lila = Diseñado · Amarillo = In Progress · "
                          "Rojo = To Do (Block) · Gris = Backlog."),
]
for i, (k, v) in enumerate(notas, start=3):
    ws2.cell(row=i, column=1, value=k).font = Font(bold=True, color=NAVY)
    ws2.cell(row=i, column=1).alignment = Alignment(vertical="top", wrap_text=True)
    c = ws2.cell(row=i, column=2, value=v)
    c.alignment = Alignment(wrap_text=True, vertical="top")
    ws2.row_dimensions[i].height = 48

OUT = Path(__file__).resolve().parent / "Status_Proyectos_Behavioral_Design.xlsx"
wb.save(OUT)
print("Generado:", OUT, "| filas:", len(ROWS), "| columnas:", len(COLUMNS))
