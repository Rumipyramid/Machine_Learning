# CLAUDE.md — Codex de conocimiento del proyecto

Este archivo lo carga Claude Code automáticamente al iniciar cualquier sesión sobre este
repositorio. Funciona como "bóveda/codex" persistente del proyecto.

## Repositorio
- **Proyecto:** Machine_Learning (`Rumipyramid/Machine_Learning`)
- Contenido principal: `Proyecto_ML_1.ipynb`, carpeta `Self driving car`.

## Mapa de la bóveda
```
README.md                      ← entrada / mapa del repo
CLAUDE.md                      ← este códice
research/
  README.md                    ← índice de investigación
  seguros_comportamiento_mundo_peru.md
  personas/
    generador/                 ← generador, esquema, matriz, dataset de ejemplo
    laminas/                   ← lámina explicativa (script + PNG)
    apps/reglas/               ← explorador web por reglas (autocontenido)
    apps/llm/                  ← app de preguntas libres con Claude (API)
  updates/                     ← reportes quincenales + generador del reporte
.claude/skills/
  lapuerta/                    ← skill compartible (generar + simular)
  cerrajero/                   ← skill: actualización quincenal a demanda
.github/workflows/             ← Action programado (reporte quincenal)
```

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

- **Matriz legible:** `research/personas/generador/matriz_usuarios_sinteticos.md`
- **Esquema (machine-readable):** `research/personas/generador/synthetic_user_schema.json`
- **Generador:** `research/personas/generador/generate_synthetic_users.py` (solo stdlib)
  - Uso: `python research/personas/generador/generate_synthetic_users.py --n 1000 --out usuarios.csv --seed 42`
- **Dataset de ejemplo:** `research/personas/generador/usuarios_sinteticos_ejemplo.csv`
- **Lámina explicativa:** `research/personas/laminas/` (script `build_lamina_detalle.py` + PNG)
- **Apps web:** `research/personas/apps/reglas/` (explorador por reglas, autocontenido) y
  `research/personas/apps/llm/` (preguntas libres con Claude vía API).
- Variables (17, esquema v1.2): generación, NSE, región, educación financiera, sesgo del presente,
  canal, **situación laboral, cobertura previsional, tenencia de vehículo, acceso digital,
  bancarizado**, exposición sísmica, apertura a datos/IA, confianza, tenencia de seguro,
  seguro de desastres, WTP ratio.
- Marginales validadas (v1.2): any-insurance ≈ 0.40, desconfía ≈ 0.46, desastres ≈ 0.035,
  bancarizado ≈ 0.59, sin cobertura previsional ≈ 0.60.

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

- **A demanda:** skill `/cerrajero` (`.claude/skills/cerrajero/`) ejecuta la actualización en la
  sesión (Claude investiga con búsqueda web, redacta, indexa y commitea). No necesita API key.
- **Automatización (desatendida):** GitHub Action `.github/workflows/fortalecimiento-modelo.yml`
  (cron días 1 y 16) ejecuta `research/updates/generate_report.py` (API de Claude + búsqueda web).
- **Requisitos:** secreto `ANTHROPIC_API_KEY` en el repo + Actions habilitado. El `schedule` solo
  corre desde la rama por defecto (mergear allí para activarlo); se puede probar con "Run workflow".
- **Índice de reportes (auto-actualizado):**
<!-- LAPUERTA_REPORTS_START -->
- 2026-08-05 — `research/updates/2026-08-05_fortalecimiento_modelo.md`
- 2026-07-21 — `research/updates/2026-07-21_fortalecimiento_modelo.md`
- 2026-07-06 — `research/updates/2026-07-06_fortalecimiento_modelo.md`
- 2026-06-21 — `research/updates/2026-06-21_fortalecimiento_modelo.md`
<!-- LAPUERTA_REPORTS_END -->

## Convenciones
- Documentación de investigación → `research/` (con índice en `research/README.md`).
- Modelo de personas sintéticas → `research/personas/generador/` (fuente de verdad de desarrollo);
  el skill `lapuerta` lleva su propia copia autocontenida para compartir.
- Láminas/figuras → `research/personas/laminas/`; apps web → `research/personas/apps/`.
- Skills del proyecto → `.claude/skills/`.
- Reportes quincenales → `research/updates/` (indexados arriba).
- Artefactos generados (CSV de muestras, ZIP, `__pycache__`, `dist/`) NO se versionan.
