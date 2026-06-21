#!/usr/bin/env python3
"""Lamina v4 (detallada, paleta rojo pastel con degrade) del sistema de
usuarios sinteticos de seguros.

Incluye: pipeline, validez interna + grafico de validacion, glosario (semilla /
marginales simuladas), las 12 variables explicadas, grafico de anclas reales,
limites y referencias. Lienzo alto para evitar solapamientos.

Salida: research/personas/lamina_sistema_usuarios_sinteticos_detalle.png
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle

# --- Paleta: rojo pastel con degrade ---
RED_DEEP = "#8e2b3a"            # encabezados fuertes
RED_GRAD = ["#eda0a0", "#e38585", "#d96b6b", "#cc5050", "#b23a48"]  # claro -> oscuro
RED_LT   = "#fdeeee"           # fondos suaves
RED_LT2  = "#fbe4e4"
RED_MED  = "#d96363"
RED_DK   = "#a83232"
GRIS  = "#3b2f2f"; GRISL = "#7c6c6c"; LINEA = "#efd9d9"; BLANCO = "#ffffff"

W, H = 200.0, 176.0
fig = plt.figure(figsize=(22, 19.4), dpi=140)
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
rbox(3, 165, 194, 9, RED_DEEP, ec=RED_DEEP)
bg.text(8, 171.4, "Sistema de Usuarios Sintéticos de Seguros — Perú",
        ha="left", va="center", color="white", fontsize=25, fontweight="bold")
bg.text(8, 167.3, "Cómo se construye · por qué es confiable · qué significa cada parámetro",
        ha="left", va="center", color="#f3d6da", fontsize=14, style="italic")
bg.text(196, 169.2, "claude-opus-4-8  +  generador calibrado", ha="right", va="center",
        color="#e7b9c0", fontsize=10)

# ---------- ① Pipeline ----------
bg.text(5, 161.5, "① CÓMO SE CONSTRUYE  ·  del dato real a la persona sintética",
        ha="left", va="center", color=RED_DEEP, fontsize=14.5, fontweight="bold")
steps = [
    ("1", "Investigación", "Datos reales del mercado:\npenetración, confianza,\ntenencia y barreras."),
    ("2", "Parámetros (matriz)", "12 variables con\ndistribuciones; cada una\nmarcada dato/supuesto."),
    ("3", "Generador", "Monte Carlo: 'lanza dados'\nsegún las distribuciones.\nSemilla fija → reproducible."),
    ("4", "Personas sintéticas", "Cada una con 12 rasgos\ncoherentes (NSE, sesgo,\ncanal, confianza, WTP…)."),
    ("5", "Simulación", "Se les pregunta; responden\nsegún su perfil. Salida:\ngráficos e insights."),
]
w, h, y0 = 35.5, 21, 138
gap = (194 - 5 * w) / 4
x = 3; centers = []
for (num, title, body), col in zip(steps, RED_GRAD):
    rbox(x, y0, w, h, col, ec=col)
    bg.add_patch(Circle((x + w / 2, y0 + h - 4.6), 3.1, facecolor="white", edgecolor=col, lw=2, zorder=3))
    bg.text(x + w / 2, y0 + h - 4.7, num, ha="center", va="center", color=col, fontsize=15, fontweight="bold", zorder=4)
    bg.text(x + w / 2, y0 + h - 9.8, title, ha="center", va="center", color="white", fontsize=12.5, fontweight="bold")
    bg.text(x + w / 2, y0 + 6.0, body, ha="center", va="center", color="white", fontsize=10.2, linespacing=1.4)
    centers.append((x, x + w)); x += w + gap
for i in range(4):
    arrow(centers[i][1] + 0.4, y0 + h / 2, centers[i + 1][0] - 0.4, y0 + h / 2)

# ---------- Glosario: semilla + marginales ----------
bg.text(5, 134.6, "GLOSARIO  ·  dos conceptos clave", ha="left", va="center",
        color=RED_DK, fontsize=12.5, fontweight="bold")
gloss = [
    (3, "¿Qué es la “semilla”?",
     "Un número que fija el azar del generador. Con la misma semilla\n"
     "salen exactamente las mismas personas: hace el experimento\n"
     "reproducible y auditable. Cambiarla = una muestra nueva."),
    (101, "¿Qué son las “marginales simuladas”?",
     "La proporción de cada categoría en la muestra generada (p. ej.\n"
     "% que desconfía). 'Marginal' = el total de una variable sin\n"
     "cruzarla con otras. Las comparamos con las reales para validar."),
]
for gx, head, body in gloss:
    rbox(gx, 116, 96, 16, RED_LT2, ec=RED_MED, lw=1.6)
    bg.text(gx + 5, 129.6, head, ha="left", va="center", color=RED_DEEP, fontsize=12, fontweight="bold")
    bg.text(gx + 5, 123.0, body, ha="left", va="center", color=GRIS, fontsize=9.6, linespacing=1.4)

# ---------- ② Validez (izq) + grafico validacion (der) ----------
bg.text(5, 112.5, "② ¿POR QUÉ ES CONFIABLE? — validez interna", ha="left", va="center",
        color=RED_DEEP, fontsize=14.5, fontweight="bold")
rbox(3, 81, 101, 28, RED_LT, ec=RED_MED, lw=1.8)
pillars = [
    ("A · Anclaje en datos", "Cada variable se marca dato (fuente) o supuesto (ajustable)."),
    ("B · Validación empírica", "Re-muestreo n=5 000: las marginales ≈ las reales (gráfico →)."),
    ("C · Dependencias causales", "región→exposición · canal(broker)→confianza · NSE+sesgo→tenencia."),
    ("D · Reproducibilidad", "Semilla fija + código auditable + esquema versionado en el repo."),
]
py = 105
for head, body in pillars:
    bg.text(7, py, head, ha="left", va="center", color=RED_DK, fontsize=11.5, fontweight="bold")
    bg.text(7, py - 3.3, body, ha="left", va="center", color=GRISL, fontsize=9.4, linespacing=1.3)
    py -= 6.6

rbox(108, 81, 89, 28, BLANCO, ec=RED_MED, lw=1.8)
bg.text(152.5, 106.2, "Evidencia: el modelo reproduce la realidad", ha="center", va="center",
        color=RED_DK, fontsize=12.5, fontweight="bold")
axv = inset(120, 84.5, 192, 102.5)
cats = ["Tiene\nseguro", "Desconfía", "Seguro\ndesastres"]
modelo = [43, 45, 2.9]; real = [40, 48, 3.3]
xs = range(len(cats)); bw = 0.38
axv.bar([i - bw / 2 for i in xs], modelo, bw, label="Modelo", color=RED_GRAD[0])
axv.bar([i + bw / 2 for i in xs], real, bw, label="Real (dato)", color=RED_DK)
for i in xs:
    axv.text(i - bw / 2, modelo[i] + 1.2, f"{modelo[i]}%", ha="center", fontsize=8, color=GRIS, fontweight="bold")
    axv.text(i + bw / 2, real[i] + 1.2, f"{real[i]}%", ha="center", fontsize=8, color=RED_DK, fontweight="bold")
axv.set_xticks(list(xs)); axv.set_xticklabels(cats, fontsize=8.5)
axv.set_ylim(0, 56); axv.set_ylabel("% de la población", fontsize=8.5)
axv.legend(fontsize=8, loc="upper right", frameon=False)
axv.spines[["top", "right"]].set_visible(False); axv.tick_params(labelsize=8)
axv.set_axisbelow(True); axv.grid(axis="y", color=LINEA, lw=0.8)

# ---------- ③ Las 12 variables explicadas ----------
bg.text(5, 78.0, "③ LAS 12 VARIABLES (qué significa cada una)", ha="left", va="center",
        color=RED_DEEP, fontsize=14.5, fontweight="bold")
rbox(3, 39, 194, 36, RED_LT, ec=RED_MED, lw=1.8)
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
    ("WTP (disposición a pagar)", "Cuánto pagaría como fracción\ndel precio justo del riesgo."),
]
col_x = [8, 72, 136]
row_y = [71, 62, 53, 44]
for idx, (name, desc) in enumerate(variables):
    cx = col_x[idx % 3]; ry = row_y[idx // 3]
    bg.text(cx, ry, f"{idx+1}. {name}", ha="left", va="center", color=RED_DK, fontsize=10.5, fontweight="bold")
    bg.text(cx, ry - 3.1, desc, ha="left", va="top", color=GRISL, fontsize=9.0, linespacing=1.3)

# ---------- Anclas reales (izq) + limites (der) ----------
rbox(3, 8, 89, 28, BLANCO, ec=RED_MED, lw=1.8)
bg.text(47.5, 33.4, "Anclas reales que calibran el modelo", ha="center", va="center",
        color=RED_DK, fontsize=12.5, fontweight="bold")
axa = inset(13, 13, 86, 29.5)
labels = ["Perú", "LatAm", "Chile"]; vals = [2.08, 3.2, 4.6]
axa.barh(range(3), vals, color=[RED_GRAD[0], RED_GRAD[2], RED_DK], height=0.6)
for i, v in enumerate(vals):
    axa.text(v + 0.08, i, f"{v}%", va="center", fontsize=9, fontweight="bold", color=GRIS)
axa.set_yticks(range(3)); axa.set_yticklabels(labels, fontsize=9)
axa.invert_yaxis(); axa.set_xlim(0, 5.4)
axa.set_xlabel("Penetración de seguros (% del PBI)", fontsize=8.5)
axa.spines[["top", "right"]].set_visible(False); axa.tick_params(labelsize=8)
axa.set_axisbelow(True); axa.grid(axis="x", color=LINEA, lw=0.8)
bg.text(47.5, 9.6, "Perú está muy por debajo de la región → alta brecha y oportunidad.",
        ha="center", va="center", color=GRISL, fontsize=8.8, style="italic")

rbox(96, 8, 101, 28, RED_LT2, ec=RED_DK, lw=1.8)
bg.text(101, 33.4, "⚠  Qué no olvidar (límites)", ha="left", va="center",
        color=RED_DK, fontsize=12.5, fontweight="bold")
bg.text(101, 29.0,
        "• Son personas inventadas, no reales.\n"
        "• Varios supuestos deben recalibrarse con micro-datos (ENAHO).\n"
        "• Validez INTERNA (coherencia) ≠ validez EXTERNA / causal.\n"
        "• Útil para prototipar e indagar hipótesis; no sustituye una encuesta.",
        ha="left", va="top", color=GRIS, fontsize=9.6, linespacing=1.5)

# ---------- Referencias (pequeñas) ----------
bg.text(5, 5.2, "Fuentes:", ha="left", va="center", color=GRIS, fontsize=8.5, fontweight="bold")
bg.text(5, 3.0,
        "SBS — Estudio de conocimiento y percepción de la demanda de seguros (2023) · APESEG · APEIM (NSE) · "
        "MAPFRE Economics — Mercado asegurador LatAm 2024 · OECD Global Insurance Market Trends 2025 · "
        "McKinsey / EY / Bain / Accenture / Swiss Re · economía conductual (sesgo del presente, WTP).",
        ha="left", va="center", color=GRISL, fontsize=7.5)
bg.text(196, 4.0, "Elaboración: 2026-06-21 · research/personas/", ha="right", va="center",
        color="#b39aa0", fontsize=8)

plt.savefig("research/personas/lamina_sistema_usuarios_sinteticos_detalle.png",
            facecolor=BLANCO, bbox_inches="tight")
print("OK")
