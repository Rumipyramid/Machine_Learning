# CLAUDE.md — Codex de conocimiento del proyecto

Este archivo lo carga Claude Code automáticamente al iniciar cualquier sesión sobre este
repositorio. Funciona como "bóveda/codex" persistente del proyecto.

## Repositorio
- **Proyecto:** Machine_Learning (`Rumipyramid/Machine_Learning`)
- Contenido principal: `Proyecto_ML_1.ipynb`, carpeta `Self driving car`.

## Base de conocimiento (codex)

### 📌 Seguros — comportamiento y percepción (Mundo vs. Perú)
Investigación recopilada el 2026-06-21 con fuentes de OECD, McKinsey, EY, Bain, Accenture,
Swiss Re, MAPFRE, APESEG, SBS Perú y literatura de economía conductual.

- **Documento principal:** `research/seguros_comportamiento_mundo_peru.md`
- **Datos clave:** penetración Perú ~2.08% del PBI (vs. 3.2% LatAm); confianza plena ~23-25%
  y ~48% desconfía (causa #1: falta de información); ~4/10 tiene seguro; SOAT conocido por 94%;
  solo ~3.3% de hogares con seguro de desastres; brecha de protección global ~US$1.8 billones.

### 📌 Usuarios sintéticos de seguros (Perú)
Matriz de variables + distribuciones para generar perfiles sintéticos calibrados a los datos.

- **Matriz legible:** `research/personas/matriz_usuarios_sinteticos.md`
- **Esquema (machine-readable):** `research/personas/synthetic_user_schema.json`
- **Generador:** `research/personas/generate_synthetic_users.py` (solo stdlib)
  - Uso: `python research/personas/generate_synthetic_users.py --n 1000 --out usuarios.csv --seed 42`
- **Dataset de ejemplo:** `research/personas/usuarios_sinteticos_ejemplo.csv`
- Variables: generación, NSE, región, educación financiera, sesgo del presente, canal,
  exposición sísmica, apertura a datos/IA, confianza, tenencia de seguro, seguro de desastres,
  WTP ratio.
- Marginales validadas: any-insurance ≈ 0.43, desconfía ≈ 0.45, desastres ≈ 0.03.

### 📌 Skill: `lapuerta` (usuarios sintéticos de seguros)
Generador + simulador de usuarios sintéticos empaquetado como **skill compartible** (autocontenido).

- **Invocación:** `/lapuerta`
- **Ubicación:** `.claude/skills/lapuerta/`
- **Contenido:** `SKILL.md` (es) + `SKILL.en.md` (en) + `scripts/generate_synthetic_users.py`
  + `scripts/simulate_rules.py` + `scripts/synthetic_user_schema.json`
  + `references/matriz_usuarios_sinteticos.md`.
- **Uso:** generar/consultar perfiles sintéticos de asegurados peruanos y simular respuestas
  (por reglas o con LLM). Para compartir, copiar la carpeta a `.claude/skills/` (proyecto)
  o `~/.claude/skills/` (personal).

### 📌 Reportes quincenales (fortalecimiento del modelo)
Investigación recurrente (cada ~15 días) que busca evidencia nueva y propone cómo incorporar
variables al modelo `lapuerta`.

- **Automatización:** GitHub Action `.github/workflows/fortalecimiento-modelo.yml` (cron días 1 y 16)
  ejecuta `research/updates/generate_report.py` (API de Claude + búsqueda web) y commitea el reporte.
- **Requisitos:** secreto `ANTHROPIC_API_KEY` en el repo + Actions habilitado. El `schedule` solo
  corre desde la rama por defecto (mergear allí para activarlo); se puede probar con "Run workflow".
- **Índice de reportes (auto-actualizado):**
<!-- LAPUERTA_REPORTS_START -->
- 2026-06-21 — `research/updates/2026-06-21_fortalecimiento_modelo.md`
<!-- LAPUERTA_REPORTS_END -->

## Convenciones
- Documentación de investigación → carpeta `research/`.
- Activos de personas sintéticas → `research/personas/`.
- Skills del proyecto → `.claude/skills/`.
- Reportes quincenales → `research/updates/` (indexados arriba).
