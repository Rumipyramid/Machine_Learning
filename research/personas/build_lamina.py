#!/usr/bin/env python3
"""Genera la lamina (infografia PNG) que explica el sistema de usuarios
sinteticos de seguros y como se trabaja su validez interna.

Salida: research/personas/lamina_sistema_usuarios_sinteticos.png
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# Paleta
AZUL   = "#1f3b73"
AZUL2  = "#2e5aac"
CYAN   = "#1aa3a3"
VERDE  = "#2e8b57"
NARANJA= "#d9822b"
ROJO   = "#b23a48"
GRIS   = "#43474e"
FONDO  = "#f4f6fa"
BLANCO = "#ffffff"

fig, ax = plt.subplots(figsize=(16, 10), dpi=140)
fig.patch.set_facecolor(BLANCO)
ax.set_xlim(0, 160); ax.set_ylim(0, 100); ax.axis("off")


def box(x, y, w, h, text, fc, tc="white", fs=10.5, weight="normal", ec=None, align="center"):
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.4,rounding_size=2.2",
                       linewidth=1.2, facecolor=fc, edgecolor=ec or fc, zorder=2)
    ax.add_patch(p)
    ha = {"center": "center", "left": "left"}[align]
    tx = x + w / 2 if align == "center" else x + 2.5
    ax.text(tx, y + h / 2, text, ha=ha, va="center", color=tc,
            fontsize=fs, fontweight=weight, zorder=3, linespacing=1.35)


def arrow(x1, y1, x2, y2, color=GRIS):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>",
                 mutation_scale=18, linewidth=2.0, color=color, zorder=1))


# ---------- Titulo ----------
box(4, 90.5, 152, 8, "", AZUL, ec=AZUL)
ax.text(8, 94.5, "Sistema de Usuarios Sintéticos de Seguros — Perú",
        ha="left", va="center", color="white", fontsize=20, fontweight="bold")
ax.text(152, 94.5, "Cómo funciona  ·  cómo se trabaja su validez interna",
        ha="right", va="center", color="#cdd8f0", fontsize=12, style="italic")

# ---------- Seccion A: pipeline ----------
ax.text(8, 86.5, "① CÓMO FUNCIONA  (pipeline de generación)", ha="left",
        va="center", color=AZUL, fontsize=13.5, fontweight="bold")

pipe = [
    ("Investigación\n\nFuentes reales:\nSBS · APESEG · APEIM\nOECD · McKinsey · EY", AZUL2),
    ("Matriz de variables\n\nMarginales +\ncondicionales +\nmodelos derivados\n→ schema JSON", CYAN),
    ("Generador\n\nMuestreo Monte Carlo\n(stdlib) · semilla\n→ reproducible", VERDE),
    ("Usuarios sintéticos\n\nCSV con 12 atributos\npor persona", NARANJA),
    ("Simulación de\nrespuestas\n\nRole-play coherente\ncon cada perfil", AZUL),
]
w, h, gap, y0 = 27, 17, 4.0, 66
x = 6
centers = []
for txt, col in pipe:
    box(x, y0, w, h, txt, col, fs=9.5)
    centers.append((x, x + w))
    x += w + gap
for i in range(len(pipe) - 1):
    arrow(centers[i][1] + 0.3, y0 + h / 2, centers[i + 1][0] - 0.3, y0 + h / 2)

# Tira de variables
ax.text(8, 62.5, "12 variables por usuario:", ha="left", va="center",
        color=GRIS, fontsize=10, fontweight="bold")
ax.text(8, 60.0,
        "generación · NSE · región · educación financiera · sesgo del presente · canal  |  "
        "exposición sísmica · apertura a datos/IA  |  confianza · tenencia · seguro de desastres · WTP",
        ha="left", va="center", color=GRIS, fontsize=9.2)

# ---------- Seccion B: validez interna ----------
ax.text(8, 54.5, "② CÓMO SE TRABAJA LA VALIDEZ INTERNA", ha="left",
        va="center", color=ROJO, fontsize=13.5, fontweight="bold")

cw, ch, cgap = 36, 30, 4.5
cy = 22
cx = 6
cards = [
    (CYAN, "A · Anclaje en datos",
     "Cada variable marca su origen:\n"
     "• 'dato'  → fuente citada\n"
     "• 'supuesto' → estimación\n   ilustrativa, ajustable\n\n"
     "Trazabilidad total al doc\nde investigación."),
    (VERDE, "B · Calibración + validación",
     "Re-muestreo n=5000 y se\ncomparan marginales contra\nobjetivos reales:\n\n"
     "• any-seguro  0.43 vs 0.40\n• desconfía   0.45 vs 0.48\n"
     "• desastres   0.029 vs 0.033\n• WTP medio   ~0.77"),
    (AZUL2, "C · Grafo de dependencias",
     "Validez de constructo vía\nrelaciones condicionales:\n\n"
     "región → exposición sísmica\ngeneración → apertura datos\n"
     "canal(broker) → ↑ confianza\nNSE+edu+sesgo → tenencia\ntenencia → WTP"),
    (NARANJA, "D · Reproducibilidad",
     "• Semilla fija → mismos\n   usuarios siempre\n"
     "• Código stdlib auditable\n• Schema JSON versionado\n"
     "• Cada muestra se commitea\n   al repo (PR)"),
]
for col, title, body in cards:
    box(cx, cy, cw, ch, "", BLANCO, ec=col)
    box(cx, cy + ch - 6, cw, 6, title, col, fs=11, weight="bold")
    ax.text(cx + 2.5, cy + (ch - 6) / 2, body, ha="left", va="center",
            color=GRIS, fontsize=9.2, linespacing=1.45)
    cx += cw + cgap

# ---------- Banda inferior: amenazas a la validez ----------
box(6, 4, 148, 13, "", "#fbeae5", ec=ROJO)
ax.text(10, 13.2, "⚠  Amenazas a la validez / límites de interpretación", ha="left",
        va="center", color=ROJO, fontsize=11.5, fontweight="bold")
ax.text(10, 8.0,
        "Varias marginales son supuestos a recalibrar con micro-datos (ENAHO, encuestas SBS).  ·  "
        "Fuentes urbano-céntricas (2023–25).  ·  Validez INTERNA (coherencia con marginales) ≠ validez "
        "EXTERNA / causal.\nLos datos sintéticos NO representan personas reales: aptos para prototipado, "
        "pruebas de pipeline y simulación; no para inferencia causal ni evidencia de mercado.",
        ha="left", va="center", color=GRIS, fontsize=9.3, linespacing=1.4)

ax.text(152, 1.6, "research/personas/  ·  2026-06-21", ha="right", va="center",
        color="#9aa0aa", fontsize=8)

plt.tight_layout(pad=0.5)
out = "research/personas/lamina_sistema_usuarios_sinteticos.png"
plt.savefig(out, facecolor=BLANCO, bbox_inches="tight")
print("Guardado:", out)
