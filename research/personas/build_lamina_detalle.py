#!/usr/bin/env python3
"""Lamina v3 (detallada) del sistema de usuarios sinteticos de seguros.

Diseno de una pagina con: pipeline detallado, pilares de validez interna, dos
graficos de evidencia (validacion modelo vs. realidad; anclas reales de mercado)
y referencias al pie.

Salida: research/personas/lamina_sistema_usuarios_sinteticos_detalle.png
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle

AZUL  = "#1f3b73"; AZUL2 = "#2e5aac"; CYAN = "#138a8a"; VERDE = "#2e8b57"
NARANJA = "#cf7a1f"; ROJO = "#b23a48"; GRIS = "#2f333a"; GRISL = "#5a5f68"
BLANCO = "#ffffff"; LINEA = "#dfe3ea"

W, H = 200.0, 140.0
fig = plt.figure(figsize=(22, 15), dpi=150)
fig.patch.set_facecolor(BLANCO)
bg = fig.add_axes([0, 0, 1, 1]); bg.set_xlim(0, W); bg.set_ylim(0, H); bg.axis("off")


def rbox(x, y, w, h, fc, ec=None, lw=1.6):
    bg.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.5,rounding_size=2.2",
                 linewidth=lw, facecolor=fc, edgecolor=ec or fc, zorder=2))


def arrow(x1, y1, x2, y2, c=GRISL):
    bg.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>",
                 mutation_scale=22, linewidth=2.4, color=c, zorder=1))


def inset(x0, y0, x1, y1):
    return fig.add_axes([x0 / W, y0 / H, (x1 - x0) / W, (y1 - y0) / H])


# ---------- Titulo ----------
rbox(3, 128, 194, 9.5, AZUL, ec=AZUL)
bg.text(8, 134.6, "Sistema de Usuarios Sintéticos de Seguros — Perú",
        ha="left", va="center", color="white", fontsize=25, fontweight="bold")
bg.text(8, 130.4, "Cómo se construye, por qué es confiable, y la evidencia que lo respalda",
        ha="left", va="center", color="#cdd8f0", fontsize=14, style="italic")
bg.text(196, 132.5, "claude-opus-4-8\n+ generador calibrado", ha="right", va="center",
        color="#9fb2db", fontsize=10, linespacing=1.3)

# ---------- Pipeline ----------
bg.text(5, 124.5, "① CÓMO SE CONSTRUYE  ·  del dato real a la persona sintética",
        ha="left", va="center", color=AZUL, fontsize=14.5, fontweight="bold")
steps = [
    (AZUL2, "1", "Investigación", "Datos reales del mercado:\npenetración, confianza,\ntenencia y barreras\n(fuentes oficiales)."),
    (CYAN, "2", "Parámetros (matriz)", "12 variables con\ndistribuciones de\nprobabilidad; cada una\nmarcada dato/supuesto."),
    (VERDE, "3", "Generador", "Monte Carlo: 'lanza dados'\nsegún las distribuciones.\nSemilla fija →\nreproducible."),
    (NARANJA, "4", "Personas sintéticas", "Cada una con 12 rasgos\ncoherentes (NSE, sesgo,\ncanal, confianza,\ntenencia, WTP…)."),
    (AZUL, "5", "Simulación", "Se les pregunta; responden\nsegún su perfil (reglas o\nClaude). Salida: gráficos\ne insights."),
]
w, h, y0 = 35.5, 21, 99
gap = (194 - 5 * w) / 4
x = 3; centers = []
for col, num, title, body in steps:
    rbox(x, y0, w, h, col, ec=col)
    bg.add_patch(Circle((x + w / 2, y0 + h - 4.6), 3.1, facecolor="white", edgecolor=col, lw=2, zorder=3))
    bg.text(x + w / 2, y0 + h - 4.7, num, ha="center", va="center", color=col, fontsize=15, fontweight="bold", zorder=4)
    bg.text(x + w / 2, y0 + h - 9.8, title, ha="center", va="center", color="white", fontsize=12.5, fontweight="bold")
    bg.text(x + w / 2, y0 + 6.2, body, ha="center", va="center", color="white", fontsize=10.3, linespacing=1.4)
    centers.append((x, x + w)); x += w + gap
for i in range(4):
    arrow(centers[i][1] + 0.4, y0 + h / 2, centers[i + 1][0] - 0.4, y0 + h / 2)

# ---------- Banda media: validez (izq) + grafico validacion (der) ----------
# Izquierda: pilares de validez
rbox(3, 50, 101, 44, "#eef3fb", ec=VERDE, lw=2)
rbox(3, 87.5, 101, 6.5, VERDE, ec=VERDE)
bg.text(53.5, 90.7, "② ¿POR QUÉ ES CONFIABLE? — validez interna", ha="center", va="center",
        color="white", fontsize=14, fontweight="bold")
pillars = [
    ("A · Anclaje en datos", "Cada variable se marca como dato (fuente citada) o supuesto\n(estimación ajustable). Trazabilidad total."),
    ("B · Validación empírica", "Re-muestreo de n=5 000: las marginales del modelo reproducen\nlas reales (ver gráfico →)."),
    ("C · Dependencias causales", "región→exposición · generación→apertura · canal(broker)→confianza\n· NSE+educación+sesgo→tenencia→WTP."),
    ("D · Reproducibilidad", "Semilla fija = mismas personas; código auditable (stdlib);\nesquema y datasets versionados en el repo."),
]
py = 82
for head, body in pillars:
    bg.text(7, py, head, ha="left", va="center", color=GRIS, fontsize=12, fontweight="bold")
    bg.text(7, py - 4.0, body, ha="left", va="center", color=GRISL, fontsize=10, linespacing=1.35)
    py -= 9.4

# Derecha: grafico de validacion (evidencia fuerte)
rbox(108, 50, 89, 44, BLANCO, ec=VERDE, lw=2)
bg.text(152.5, 90.7, "Evidencia: el modelo reproduce la realidad", ha="center", va="center",
        color=VERDE, fontsize=13, fontweight="bold")
bg.text(152.5, 87.2, "marginales simuladas (n=5 000)  vs.  datos reales", ha="center", va="center",
        color=GRISL, fontsize=9.5, style="italic")
axv = inset(120, 56, 192, 83)
cats = ["Tiene\nseguro", "Desconfía", "Seguro\ndesastres"]
modelo = [43, 45, 2.9]; real = [40, 48, 3.3]
xs = range(len(cats)); bw = 0.38
axv.bar([i - bw / 2 for i in xs], modelo, bw, label="Modelo", color=AZUL2)
axv.bar([i + bw / 2 for i in xs], real, bw, label="Real (dato)", color=NARANJA)
for i in xs:
    axv.text(i - bw / 2, modelo[i] + 1.2, f"{modelo[i]}%", ha="center", fontsize=8.5, color=AZUL2, fontweight="bold")
    axv.text(i + bw / 2, real[i] + 1.2, f"{real[i]}%", ha="center", fontsize=8.5, color=NARANJA, fontweight="bold")
axv.set_xticks(list(xs)); axv.set_xticklabels(cats, fontsize=9)
axv.set_ylim(0, 56); axv.set_ylabel("% de la población", fontsize=9)
axv.legend(fontsize=8.5, loc="upper right", frameon=False)
axv.spines[["top", "right"]].set_visible(False)
axv.tick_params(labelsize=8.5)
axv.set_axisbelow(True); axv.grid(axis="y", color=LINEA, lw=0.8)

# ---------- Banda baja: grafico anclas (izq) + variables/limites (der) ----------
rbox(3, 9, 89, 38, BLANCO, ec=CYAN, lw=2)
bg.text(47.5, 43.7, "Anclas reales que calibran el modelo", ha="center", va="center",
        color=CYAN, fontsize=13, fontweight="bold")
axa = inset(13, 14, 86, 38)
labels = ["Perú", "LatAm", "Chile"]
vals = [2.08, 3.2, 4.6]; cols = [ROJO, GRISL, VERDE]
axa.barh(range(len(labels)), vals, color=cols, height=0.62)
for i, v in enumerate(vals):
    axa.text(v + 0.08, i, f"{v}%", va="center", fontsize=9, fontweight="bold", color=GRIS)
axa.set_yticks(range(len(labels))); axa.set_yticklabels(labels, fontsize=9.5)
axa.invert_yaxis(); axa.set_xlim(0, 5.4)
axa.set_xlabel("Penetración de seguros (% del PBI)", fontsize=9)
axa.spines[["top", "right"]].set_visible(False); axa.tick_params(labelsize=8.5)
axa.set_axisbelow(True); axa.grid(axis="x", color=LINEA, lw=0.8)
bg.text(47.5, 10.6, "Perú está muy por debajo de la región → alta brecha y oportunidad.",
        ha="center", va="center", color=GRISL, fontsize=9, style="italic")

# Derecha: variables + limites
rbox(96, 9, 101, 38, "#fbf4ec", ec=NARANJA, lw=2)
bg.text(146.5, 43.7, "Las 12 variables  ·  y qué no olvidar", ha="center", va="center",
        color=NARANJA, fontsize=13, fontweight="bold")
bg.text(100, 38.5,
        "generación · NSE · región · educación financiera · sesgo del presente · canal\n"
        "exposición sísmica · apertura a datos/IA · confianza · tenencia · seguro de\n"
        "desastres · disposición a pagar (WTP)",
        ha="left", va="top", color=GRIS, fontsize=10, linespacing=1.5)
bg.text(100, 25.5, "⚠  Límites de interpretación", ha="left", va="center", color=ROJO,
        fontsize=11, fontweight="bold")
bg.text(100, 21.5,
        "• Son personas inventadas, no reales.\n"
        "• Varios supuestos deben recalibrarse con micro-datos locales (ENAHO).\n"
        "• Validez INTERNA (coherencia) ≠ validez EXTERNA / causal.\n"
        "• Útil para prototipar y explorar hipótesis; no sustituye una encuesta.",
        ha="left", va="top", color=GRISL, fontsize=9.6, linespacing=1.45)

# ---------- Referencias (pequeñas) ----------
bg.text(5, 5.4, "Fuentes:", ha="left", va="center", color=GRIS, fontsize=8.5, fontweight="bold")
bg.text(5, 3.1,
        "SBS — Estudio de conocimiento y percepción de la demanda de seguros (2023) · APESEG (penetración, seguro de desastres) · "
        "APEIM (segmentación NSE) · MAPFRE Economics — Mercado asegurador LatAm 2024 · OECD Global Insurance Market Trends 2025 · "
        "McKinsey / EY / Bain / Accenture / Swiss Re (confianza y comportamiento) · literatura de economía conductual (sesgo del presente, WTP).",
        ha="left", va="center", color=GRISL, fontsize=7.6)
bg.text(196, 4.2, "Elaboración: 2026-06-21 · research/personas/", ha="right", va="center",
        color="#9aa0aa", fontsize=8)

plt.savefig("research/personas/lamina_sistema_usuarios_sinteticos_detalle.png",
            facecolor=BLANCO, bbox_inches="tight")
print("OK")
