#!/usr/bin/env python3
"""Genera el reporte quincenal de fortalecimiento del modelo `lapuerta`.

Usa la API de Claude (claude-opus-4-8) con la herramienta de búsqueda web para
investigar datos/evidencia recientes y proponer cómo incorporar nuevas variables
al modelo de usuarios sintéticos de seguros (Perú). Escribe el reporte en
`research/updates/AAAA-MM-DD_fortalecimiento_modelo.md` y lo indexa en el códice
(`CLAUDE.md`).

Pensado para correr dentro de un GitHub Action (cron). Requiere ANTHROPIC_API_KEY.

Uso:
  python research/updates/generate_report.py            # genera (llama a la API)
  python research/updates/generate_report.py --dry-run  # arma el prompt sin llamar
"""
from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import sys

MODEL = "claude-opus-4-8"
ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
UPDATES_DIR = os.path.join(ROOT, "research", "updates")
CODEX = os.path.join(ROOT, "CLAUDE.md")
START = "<!-- LAPUERTA_REPORTS_START -->"
END = "<!-- LAPUERTA_REPORTS_END -->"

VARIABLES_ACTUALES = (
    "generacion, nse, region, educacion_financiera, sesgo_presente, canal_preferido, "
    "exposicion_riesgo_sismico, apertura_datos_ia, confianza_aseguradora, tenencia_seguro, "
    "seguro_desastres_naturales, wtp_ratio"
)
YA_PROPUESTAS = (
    "acceso_digital, situacion_laboral, bancarizado, experiencia_siniestro, "
    "conciencia_riesgo_climatico, cobertura_salud_publica, influencia_social"
)

SYSTEM = """\
Eres analista de investigación del modelo de usuarios sintéticos de seguros del Perú
("lapuerta"). Tu trabajo quincenal: buscar datos y evidencia RECIENTES (últimos ~6 meses)
que permitan fortalecer el modelo, y proponer cómo incorporarlos como variables.

Usa la herramienta de búsqueda web para encontrar fuentes verificables (INEI, BCRP, SBS,
APESEG, APEIM, MAPFRE, OECD, prensa especializada, literatura). Prioriza cifras concretas
con su fuente. No inventes datos; si no encuentras evidencia nueva fuerte para algo, dilo.

Entrega SOLO un reporte en Markdown en español, con esta estructura exacta:
1. Encabezado con fecha y "Próxima revisión" (+15 días).
2. Resumen ejecutivo (3-6 viñetas con la evidencia más fuerte y su cifra).
3. Tabla: variable candidata | evidencia/dato | fuente | cómo incorporarla | prioridad | origen(dato/supuesto).
4. Detalle por variable (definición, evidencia, incorporación: distribución/dependencias/efecto).
5. Cambios propuestos al esquema (snippets JSON ilustrativos) + nota de re-validación.
6. Fuentes (lista de URLs).
Marca cada propuesta como `dato` (anclado en fuente) o `supuesto`. Evita repetir variables
que ya existen o ya fueron propuestas; busca ángulos NUEVOS o recalibraciones con cifras frescas.
"""


def build_user_prompt(today: str, nxt: str) -> str:
    return f"""\
Fecha de hoy: {today}. Próxima revisión: {nxt}.

Variables YA en el modelo: {VARIABLES_ACTUALES}.
Variables YA propuestas en reportes previos (no repetir salvo recalibración con cifra nueva):
{YA_PROPUESTAS}.

Marginales objetivo actuales (no romper): tiene seguro ≈ 0.40, desconfía ≈ 0.48,
seguro de desastres ≈ 0.033.

Investiga evidencia reciente sobre comportamiento, percepción y demanda de seguros en Perú
(y LatAm como referencia) y produce el reporte en Markdown según la estructura indicada.
Cierra con la línea: "*Generado por el ciclo quincenal de fortalecimiento del modelo `lapuerta`.*"
"""


def call_claude(system: str, user: str) -> str:
    import anthropic

    client = anthropic.Anthropic()
    web_search = {"type": "web_search_20260209", "name": "web_search", "max_uses": 8}
    messages = [{"role": "user", "content": user}]
    for _ in range(6):  # tolera varios pause_turn del bucle de búsqueda server-side
        resp = client.messages.create(
            model=MODEL,
            max_tokens=8000,
            thinking={"type": "adaptive"},
            output_config={"effort": "medium"},
            system=system,
            tools=[web_search],
            messages=messages,
        )
        if resp.stop_reason == "refusal":
            raise RuntimeError("El modelo rechazó la solicitud.")
        if resp.stop_reason == "pause_turn":
            messages.append({"role": "assistant", "content": resp.content})
            continue
        break
    text = "".join(b.text for b in resp.content if getattr(b, "type", None) == "text")
    if not text.strip():
        raise RuntimeError("Respuesta vacía del modelo.")
    return text.strip()


def update_codex(date_str: str, rel_path: str) -> None:
    if not os.path.exists(CODEX):
        return
    with open(CODEX, "r", encoding="utf-8") as f:
        content = f.read()
    entry = f"- {date_str} — `{rel_path}`"
    if START in content and END in content:
        if entry in content:
            return
        content = content.replace(START, f"{START}\n{entry}", 1)
    else:  # crear la sección si no existe
        block = (
            "\n### 📌 Reportes quincenales (fortalecimiento del modelo)\n"
            f"Índice de reportes (auto-actualizado):\n{START}\n{entry}\n{END}\n"
        )
        content = content.rstrip() + "\n" + block
    with open(CODEX, "w", encoding="utf-8") as f:
        f.write(content)


def main(argv=None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args(argv)

    today = dt.date.today()
    nxt = today + dt.timedelta(days=15)
    today_s, nxt_s = today.isoformat(), nxt.isoformat()
    system, user = SYSTEM, build_user_prompt(today_s, nxt_s)

    if args.dry_run:
        print(f"[dry-run] modelo={MODEL}")
        print(f"[dry-run] system chars={len(system)}  user chars={len(user)}")
        print(f"[dry-run] escribiría research/updates/{today_s}_fortalecimiento_modelo.md")
        return 0

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERROR: falta ANTHROPIC_API_KEY", file=sys.stderr)
        return 2

    report = call_claude(system, user)
    os.makedirs(UPDATES_DIR, exist_ok=True)
    fname = f"{today_s}_fortalecimiento_modelo.md"
    out = os.path.join(UPDATES_DIR, fname)
    with open(out, "w", encoding="utf-8") as f:
        f.write(report + "\n")
    update_codex(today_s, f"research/updates/{fname}")
    print(f"OK → {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
