#!/usr/bin/env python3
"""Genera la lamina (infografia PNG) que explica, en lenguaje sencillo, el
sistema de usuarios sinteticos de seguros y por que el modelo es confiable.

Salida: research/personas/lamina_sistema_usuarios_sinteticos.png
Formato grande y legible (lienzo amplio, tipografias grandes).
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle

# Paleta
AZUL   = "#1f3b73"
AZUL2  = "#2e5aac"
CYAN   = "#138a8a"
VERDE  = "#2e8b57"
NARANJA= "#cf7a1f"
ROJO   = "#b23a48"
GRIS   = "#2f333a"
GRISL  = "#5a5f68"
BLANCO = "#ffffff"

fig, ax = plt.subplots(figsize=(22, 15), dpi=150)
fig.patch.set_facecolor(BLANCO)
ax.set_xlim(0, 200); ax.set_ylim(0, 134); ax.axis("off")


def rbox(x, y, w, h, fc, ec=None, lw=1.6):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.5,rounding_size=2.5",
                 linewidth=lw, facecolor=fc, edgecolor=ec or fc, zorder=2))


def arrow(x1, y1, x2, y2, color=GRISL):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>",
                 mutation_scale=30, linewidth=3.2, color=color, zorder=1))


# ---------- Titulo ----------
rbox(3, 121, 194, 11, AZUL, ec=AZUL)
ax.text(100, 128.4, "¿Cómo creamos personas “de mentira” que se comportan como peruanos reales?",
        ha="center", va="center", color="white", fontsize=27, fontweight="bold")
ax.text(100, 123.4, "Un sistema que inventa miles de perfiles para estudiar qué piensa la gente sobre los seguros",
        ha="center", va="center", color="#cdd8f0", fontsize=16, style="italic")

# ---------- Paso a paso ----------
ax.text(6, 116, "Cómo lo hacemos, paso a paso", ha="left", va="center",
        color=AZUL, fontsize=20, fontweight="bold")

steps = [
    (AZUL2,  "1", "Leemos estudios reales", "Qué piensan los peruanos\nde los seguros, según\nfuentes oficiales (SBS,\nAPESEG)."),
    (CYAN,   "2", "Anotamos las proporciones", "Como una receta de cocina:\ncuántos confían, cuántos\ntienen seguro, etc."),
    (VERDE,  "3", "La compu “lanza los dados”", "Siguiendo esa receta\ncrea miles de personas\ninventadas."),
    (NARANJA,"4", "12 rasgos por persona", "Edad, ingresos, si confía,\nsi tiene seguro,\ndónde vive…"),
    (AZUL,   "5", "Les hacemos preguntas", "Y cada una responde\nsegún su forma de ser."),
]
w, h, y0 = 35.0, 23, 87
gap = (194 - 5 * w) / 4
x = 3
cx_list = []
for col, num, title, body in steps:
    rbox(x, y0, w, h, col, ec=col)
    ax.add_patch(Circle((x + w / 2, y0 + h - 4.8), 3.4, facecolor="white", edgecolor=col, lw=2, zorder=3))
    ax.text(x + w / 2, y0 + h - 4.9, num, ha="center", va="center", color=col, fontsize=17, fontweight="bold", zorder=4)
    ax.text(x + w / 2, y0 + h - 10.5, title, ha="center", va="center", color="white", fontsize=12.5, fontweight="bold")
    ax.text(x + w / 2, y0 + 6.2, body, ha="center", va="center", color="white", fontsize=12, linespacing=1.4)
    cx_list.append((x, x + w))
    x += w + gap
for i in range(len(steps) - 1):
    arrow(cx_list[i][1] + 0.5, y0 + h / 2, cx_list[i + 1][0] - 0.5, y0 + h / 2)

# ---------- Bloque grande: por que es confiable ----------
LX, LW = 3, 118
rbox(LX, 6, LW, 76, "#eef3fb", ec=VERDE, lw=2.2)
rbox(LX, 74.5, LW, 7.5, VERDE, ec=VERDE)
ax.text(LX + LW / 2, 78.3, "¿Por qué es confiable este modelo?", ha="center", va="center",
        color="white", fontsize=20, fontweight="bold")

points = [
    ("No inventamos los números.",
     "Salen de estudios oficiales del Perú (SBS, APESEG, APEIM)."),
    ("Lo comprobamos con una prueba.",
     "Si creamos 5,000 personas, el grupo que desconfía sale casi\nigual al real: 45% en el modelo vs 48% medido en encuestas."),
    ("Respeta la lógica de la vida real.",
     "Alguien con más ingresos y educación tiende más a tener\nseguro… tal como pasa de verdad."),
    ("Cualquiera puede repetirlo.",
     "Con la misma “semilla” salen las mismas personas: es\ntransparente y el código se puede revisar."),
]
py = 67
for i, (head, body) in enumerate(points, 1):
    ax.add_patch(Circle((LX + 8, py), 3.4, facecolor=VERDE, edgecolor=VERDE, zorder=3))
    ax.text(LX + 8, py - 0.1, str(i), ha="center", va="center", color="white", fontsize=16, fontweight="bold", zorder=4)
    ax.text(LX + 14, py + 1.6, head, ha="left", va="center", color=GRIS, fontsize=15.5, fontweight="bold")
    ax.text(LX + 14, py - 3.0, body, ha="left", va="center", color=GRISL, fontsize=13, linespacing=1.4)
    py -= 15.5

# ---------- Columna derecha: analogia + advertencia ----------
RX, RW = 125, 72

rbox(RX, 47, RW, 35, "#e9f5f4", ec=CYAN, lw=2.2)
rbox(RX, 74.5, RW, 7.5, CYAN, ec=CYAN)
ax.text(RX + RW / 2, 78.3, "En palabras simples", ha="center", va="center",
        color="white", fontsize=18, fontweight="bold")
ax.text(RX + 4, 60, "Es como un videojuego que crea\npersonajes: cada uno es inventado,\n"
        "pero todos siguen las mismas reglas\nque vemos en los peruanos reales.\n\n"
        "Así podemos “entrevistar” a miles\nsin hacer una encuesta gigante.",
        ha="left", va="center", color=GRIS, fontsize=13.5, linespacing=1.5)

rbox(RX, 6, RW, 36, "#fbeae5", ec=ROJO, lw=2.2)
rbox(RX, 34.5, RW, 7.5, ROJO, ec=ROJO)
ax.text(RX + RW / 2, 38.3, "Qué NO hay que olvidar", ha="center", va="center",
        color="white", fontsize=18, fontweight="bold")
ax.text(RX + 4, 20.5,
        "•  Son personas inventadas, no reales.\n"
        "•  Sirven para practicar ideas, probar\n    preguntas y hacer prototipos.\n"
        "•  NO reemplazan una encuesta real\n    ni prueban qué causa qué.\n"
        "•  Algunos datos son estimaciones que\n    conviene afinar con cifras locales.",
        ha="left", va="center", color=GRIS, fontsize=13.5, linespacing=1.5)

ax.text(197, 2.5, "research/personas/  ·  2026-06-21", ha="right", va="center",
        color="#9aa0aa", fontsize=11)

plt.tight_layout(pad=0.6)
out = "research/personas/lamina_sistema_usuarios_sinteticos.png"
plt.savefig(out, facecolor=BLANCO, bbox_inches="tight")
print("Guardado:", out)
