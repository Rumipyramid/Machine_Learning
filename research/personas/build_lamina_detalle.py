#!/usr/bin/env python3
"""Lamina v6 (rojo pastel) del sistema de usuarios sinteticos de seguros.

Cambios v6:
- Seccion ④ ampliada: ademas del flujo perfil->logica->respuesta, panel
  "Cada atribucion viene de una fuente" (que dato/fuente respalda cada regla).
- Pilares de ② con interlineado corregido (sin solapamientos).
- Grafico de anclas sin choque eje/nota.
- Lienzo mas alto; diagramacion y tamanos revisados para lectura.

Salida: research/personas/lamina_sistema_usuarios_sinteticos_detalle.png
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle

RED_DEEP = "#8e2b3a"
RED_GRAD = ["#eda0a0", "#e38585", "#d96b6b", "#cc5050", "#b23a48"]
RED_LT = "#fdeeee"; RED_LT2 = "#fbe4e4"; RED_MED = "#d96363"; RED_DK = "#a83232"
GRIS = "#3b2f2f"; GRISL = "#7c6c6c"; LINEA = "#efd9d9"; BLANCO = "#ffffff"

W, H = 200.0, 212.0
fig = plt.figure(figsize=(22, 23.32), dpi=140)
fig.patch.set_facecolor(BLANCO)
bg = fig.add_axes([0, 0, 1, 1]); bg.set_xlim(0, W); bg.set_ylim(0, H); bg.axis("off")


def rbox(x, y, w, h, fc, ec=None, lw=1.6):
    bg.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.5,rounding_size=2.0",
                 linewidth=lw, facecolor=fc, edgecolor=ec or fc, zorder=2))


def arrow(x1, y1, x2, y2, c=RED_MED):
    bg.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>",
                 mutation_scale=20, linewidth=2.4, color=c, zorder=1))


def inset(x0, y0, x1, y1):
    return fig.add_axes([x0 / W, y0 / H, (x1 - x0) / W, (y1 - y0) / H])


# ---------- Titulo ----------
rbox(3, 201, 194, 9, RED_DEEP, ec=RED_DEEP)
bg.text(8, 207.4, "Sistema de Usuarios Sintéticos de Seguros — Perú",
        ha="left", va="center", color="white", fontsize=25, fontweight="bold")
bg.text(8, 203.3, "Cómo se construye · cómo responden · de dónde sale cada respuesta · por qué es confiable",
        ha="left", va="center", color="#f3d6da", fontsize=13.5, style="italic")

# ---------- ① Pipeline ----------
bg.text(5, 198.0, "① CÓMO SE CONSTRUYE  ·  del dato real a la persona sintética",
        ha="left", va="center", color=RED_DEEP, fontsize=14.5, fontweight="bold")
steps = [
    ("1", "Investigación", "Datos reales del mercado:\npenetración, confianza,\ntenencia y barreras."),
    ("2", "Parámetros (matriz)", "12 variables con sus\nproporciones; cada una\nmarcada dato/supuesto."),
    ("3", "Generador", "La compu 'lanza dados'.\nLa 'semilla' fija el azar:\nmisma semilla → mismas\npersonas."),
    ("4", "Personas sintéticas", "Cada una con 12 rasgos\ncoherentes (NSE, sesgo,\ncanal, confianza, WTP…)."),
    ("5", "Simulación", "Se les pregunta y\nresponden según su\nperfil → ver sección ④."),
]
w, h, y0 = 35.5, 22, 174
gap = (194 - 5 * w) / 4
x = 3; centers = []
for (num, title, body), col in zip(steps, RED_GRAD):
    rbox(x, y0, w, h, col, ec=col)
    bg.add_patch(Circle((x + w / 2, y0 + h - 4.8), 3.1, facecolor="white", edgecolor=col, lw=2, zorder=3))
    bg.text(x + w / 2, y0 + h - 4.9, num, ha="center", va="center", color=col, fontsize=15, fontweight="bold", zorder=4)
    bg.text(x + w / 2, y0 + h - 10.0, title, ha="center", va="center", color="white", fontsize=12.5, fontweight="bold")
    bg.text(x + w / 2, y0 + 5.8, body, ha="center", va="center", color="white", fontsize=10.0, linespacing=1.4)
    centers.append((x, x + w)); x += w + gap
for i in range(4):
    arrow(centers[i][1] + 0.4, y0 + h / 2, centers[i + 1][0] - 0.4, y0 + h / 2)

# ---------- ④ ¿Cómo responde cada usuario? + de dónde sale la lógica ----------
bg.text(5, 171.0, "④ ¿CÓMO RESPONDE CADA USUARIO?  ·  de los rasgos (y su fuente) a la respuesta",
        ha="left", va="center", color=RED_DEEP, fontsize=14.5, fontweight="bold")
rbox(3, 126, 194, 43, RED_LT, ec=RED_MED, lw=1.8)
bg.text(8, 163.8, "Tomamos el perfil de cada persona y construimos su respuesta de dos formas:",
        ha="left", va="center", color=GRIS, fontsize=11)
# flujo
flow = [(10, 58, RED_GRAD[0], "Perfil de la\npersona (12 rasgos)"),
        (76, 124, RED_GRAD[2], "Lógica de respuesta\n(regla  o  IA)"),
        (142, 190, RED_GRAD[4], "Respuesta +\nsentimiento")]
for x0, x1, col, txt in flow:
    rbox(x0, 154, x1 - x0, 7, col, ec=col)
    bg.text((x0 + x1) / 2, 157.5, txt, ha="center", va="center", color="white", fontsize=10.5, fontweight="bold", linespacing=1.2)
arrow(59, 157.5, 75, 157.5); arrow(125, 157.5, 141, 157.5)
# columna izquierda: motores + ejemplo
bg.text(8, 149.0, "● Por reglas:", ha="left", va="center", color=RED_DK, fontsize=10.5, fontweight="bold")
bg.text(31, 149.0, "cada rasgo suma o resta y decide la postura.", ha="left", va="center", color=GRIS, fontsize=10)
bg.text(8, 144.6, "● Con Claude (IA):", ha="left", va="center", color=RED_DK, fontsize=10.5, fontweight="bold")
bg.text(39, 144.6, "se pone en los zapatos de la persona y responde.", ha="left", va="center", color=GRIS, fontsize=10)
rbox(7, 129, 100, 12, BLANCO, ec=RED_MED, lw=1.4)
bg.text(11, 137.2, "Ejemplo", ha="left", va="center", color=RED_DK, fontsize=10, fontweight="bold")
bg.text(11, 133.2, "NSE bajo · desconfía · sesgo alto · sin seguro →", ha="left", va="center", color=GRIS, fontsize=9.4)
bg.text(11, 130.6, "“No me fío, y no me alcanza.”  (Desfavorable)", ha="left", va="center", color=GRIS, fontsize=9.4, style="italic")
# columna derecha: de dónde sale la lógica (fuente de cada atribución)
rbox(110, 128, 84, 21, RED_LT2, ec=RED_DK, lw=1.6)
bg.text(114, 146.0, "Cada atribución viene de una fuente", ha="left", va="center",
        color=RED_DEEP, fontsize=10.5, fontweight="bold")
attrib = [
    "Confianza (confía/desconfía)  →  SBS 2023",
    "Tenencia y penetración  →  APESEG",
    "Segmentos NSE (A–E)  →  APEIM",
    "Sesgo del presente · WTP  →  econ. conductual",
    "Penetración macro (% PBI)  →  MAPFRE / OECD",
]
ay = 142.3
for line in attrib:
    bg.text(114, ay, "• " + line, ha="left", va="center", color=GRIS, fontsize=9.2)
    ay -= 3.0

# ---------- ② ¿Por qué es confiable? (simple) + grafico ----------
bg.text(5, 123.0, "② ¿POR QUÉ ES CONFIABLE?  ·  en palabras simples", ha="left", va="center",
        color=RED_DEEP, fontsize=14.5, fontweight="bold")
rbox(3, 90, 101, 31, RED_LT, ec=RED_MED, lw=1.8)
pillars = [
    ("No inventamos los números", "Vienen de estudios reales del Perú\n(SBS, APESEG)."),
    ("Lo comprobamos", "Creamos miles de personas y revisamos\nque se parezcan a la gente real (gráfico →)."),
    ("Respeta la lógica de la vida", "Más ingresos y educación → más seguro,\nigual que en la realidad."),
    ("Cualquiera puede repetirlo", "Con la misma 'semilla' (número que fija\nel azar) salen las mismas personas."),
]
py = 117.5
for head, body in pillars:
    bg.text(7, py, "✓ " + head, ha="left", va="center", color=RED_DK, fontsize=11.5, fontweight="bold")
    bg.text(10, py - 3.0, body, ha="left", va="top", color=GRISL, fontsize=9.3, linespacing=1.3)
    py -= 7.0

rbox(108, 90, 89, 31, BLANCO, ec=RED_MED, lw=1.8)
bg.text(152.5, 117.6, "Evidencia: el modelo se parece a la realidad", ha="center", va="center",
        color=RED_DK, fontsize=12.5, fontweight="bold")
bg.text(152.5, 114.4, "% de personas en cada grupo:  modelo  vs.  estudios reales",
        ha="center", va="center", color=GRISL, fontsize=8.8, style="italic")
axv = inset(120, 92, 192, 110)
cats = ["Tiene\nseguro", "Desconfía", "Seguro\ndesastres"]
modelo = [43, 45, 2.9]; real = [40, 48, 3.3]
xs = range(len(cats)); bw = 0.38
axv.bar([i - bw / 2 for i in xs], modelo, bw, label="Modelo", color=RED_GRAD[0])
axv.bar([i + bw / 2 for i in xs], real, bw, label="Realidad", color=RED_DK)
for i in xs:
    axv.text(i - bw / 2, modelo[i] + 1.2, f"{modelo[i]}%", ha="center", fontsize=8, color=GRIS, fontweight="bold")
    axv.text(i + bw / 2, real[i] + 1.2, f"{real[i]}%", ha="center", fontsize=8, color=RED_DK, fontweight="bold")
axv.set_xticks(list(xs)); axv.set_xticklabels(cats, fontsize=8.5)
axv.set_ylim(0, 56); axv.set_ylabel("% de personas", fontsize=8.5)
axv.legend(fontsize=8.5, loc="upper right", frameon=False)
axv.spines[["top", "right"]].set_visible(False); axv.tick_params(labelsize=8)
axv.set_axisbelow(True); axv.grid(axis="y", color=LINEA, lw=0.8)

# ---------- ③ Las 12 variables explicadas ----------
bg.text(5, 87.0, "③ LAS 12 VARIABLES (qué significa cada una)", ha="left", va="center",
        color=RED_DEEP, fontsize=14.5, fontweight="bold")
rbox(3, 47, 194, 38, RED_LT, ec=RED_MED, lw=1.8)
variables = [
    ("Generación", "Cohorte de edad (Gen Z→Boomer);\nmarca actitudes y canal."),
    ("NSE", "Nivel socioeconómico (A alto→E bajo);\nprincipal driver de tenencia."),
    ("Región", "Lima, Costa, Sierra o Selva;\ndefine la exposición sísmica."),
    ("Educación financiera", "Cuánto entiende de seguros\n(baja / media / alta)."),
    ("Sesgo del presente", "Tendencia a postergar la decisión;\nfrena la compra."),
    ("Canal preferido", "Cómo contrataría: directo/digital,\nbancaseguros, broker o ninguno."),
    ("Exposición sísmica", "Riesgo de sismo según su región\n(alta / media / baja)."),
    ("Apertura a datos/IA", "Disposición a compartir datos y\nconfiar en IA (mayor en jóvenes)."),
    ("Confianza", "Confía, es neutral o desconfía\nde las aseguradoras."),
    ("Tenencia de seguro", "Voluntario, solo obligatorio\n(SOAT/Vida Ley) o ninguno."),
    ("Seguro de desastres", "Si tiene cobertura ante sismos\n(sí / no)."),
    ("WTP (cuánto pagaría)", "Cuánto pagaría comparado con\nel precio justo del riesgo."),
]
col_x = [8, 72, 136]; row_y = [80, 71, 62, 53]
for idx, (name, desc) in enumerate(variables):
    cx = col_x[idx % 3]; ry = row_y[idx // 3]
    bg.text(cx, ry, f"{idx+1}. {name}", ha="left", va="center", color=RED_DK, fontsize=10.5, fontweight="bold")
    bg.text(cx, ry - 3.0, desc, ha="left", va="top", color=GRISL, fontsize=9.0, linespacing=1.3)

# ---------- Anclas reales (izq) + limites (der) ----------
rbox(3, 14, 89, 28, BLANCO, ec=RED_MED, lw=1.8)
bg.text(47.5, 39.4, "Anclas reales que calibran el modelo", ha="center", va="center",
        color=RED_DK, fontsize=12.5, fontweight="bold")
bg.text(47.5, 36.0, "Perú está muy por debajo de la región.", ha="center", va="center",
        color=GRISL, fontsize=8.8, style="italic")
axa = inset(13, 18, 86, 34)
labels = ["Perú", "LatAm", "Chile"]; vals = [2.08, 3.2, 4.6]
axa.barh(range(3), vals, color=[RED_GRAD[0], RED_GRAD[2], RED_DK], height=0.6)
for i, v in enumerate(vals):
    axa.text(v + 0.08, i, f"{v}%", va="center", fontsize=9, fontweight="bold", color=GRIS)
axa.set_yticks(range(3)); axa.set_yticklabels(labels, fontsize=9)
axa.invert_yaxis(); axa.set_xlim(0, 5.4)
axa.set_xlabel("Penetración de seguros (% del PBI)", fontsize=8.5)
axa.spines[["top", "right"]].set_visible(False); axa.tick_params(labelsize=8)
axa.set_axisbelow(True); axa.grid(axis="x", color=LINEA, lw=0.8)

rbox(96, 14, 101, 28, RED_LT2, ec=RED_DK, lw=1.8)
bg.text(101, 39.4, "⚠  Qué no olvidar", ha="left", va="center", color=RED_DK, fontsize=12.5, fontweight="bold")
bg.text(101, 35.0,
        "• Son personas inventadas, no reales.\n"
        "• Sirven para practicar ideas y probar preguntas.\n"
        "• No reemplazan una encuesta real ni prueban qué causa qué.\n"
        "• Algunos datos son estimaciones a afinar con cifras locales.",
        ha="left", va="top", color=GRIS, fontsize=9.6, linespacing=1.5)

# ---------- Referencias ----------
bg.text(5, 8.0, "Fuentes:", ha="left", va="center", color=GRIS, fontsize=8.5, fontweight="bold")
bg.text(5, 5.6,
        "SBS — Estudio de conocimiento y percepción de la demanda de seguros (2023) · APESEG · APEIM (NSE) · "
        "MAPFRE Economics — Mercado asegurador LatAm 2024 · OECD Global Insurance Market Trends 2025 · "
        "McKinsey / EY / Bain / Accenture / Swiss Re · economía conductual (sesgo del presente, WTP).",
        ha="left", va="center", color=GRISL, fontsize=7.5)
bg.text(196, 6.8, "Elaboración: 2026-06-21 · research/personas/", ha="right", va="center",
        color="#b39aa0", fontsize=8)

plt.savefig("research/personas/lamina_sistema_usuarios_sinteticos_detalle.png",
            facecolor=BLANCO, bbox_inches="tight")
print("OK")
