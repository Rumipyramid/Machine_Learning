# CLAUDE.md — Codex de conocimiento del proyecto

Bóveda persistente que Claude Code carga al iniciar cualquier sesión sobre
`Rumipyramid/Machine_Learning`. Índice único de qué hay, dónde está y cómo se usa.

## 🗺️ Mapa de archivos

| Ruta | Qué es | Uso / notas |
|---|---|---|
| `Proyecto_ML_1.ipynb` | Notebook principal de ML | Origen Colab |
| `Self driving car/` | Simulación de auto autónomo (Pygame + red neuronal) | Entrada: `self driving car.py`; config en `config_file.txt` |
| `research/seguros_comportamiento_mundo_peru.md` | Investigación base: comportamiento/percepción de seguros (Mundo vs. Perú) | Fuentes OECD, McKinsey, EY, Bain, Swiss Re, APESEG, SBS… |
| `research/glosario_seguro_salud_peru.md` | Glosario de seguro de salud en Perú en lenguaje claro | Derivado de /seeker; alineado a glosario SBS |
| `research/personas/generador/` | Fuente de verdad del modelo de personas sintéticas | generador + esquema + matriz + tooling de calibración |
| `research/personas/generador/COMO_FUNCIONA_LA_PUERTA.md` | Guía explicativa: mecánica interna, validez y confiabilidad | Documento de referencia del sistema |
| `research/personas/generador/synthetic_user_schema.json` | Esquema machine-readable (v1.2, 17 variables) | Lo consume el generador |
| `research/personas/generador/matriz_usuarios_sinteticos.md` | Matriz legible: variables, distribuciones, grafo causal, arquetipos | Deriva de la investigación base |
| `research/personas/generador/generate_synthetic_users.py` | Generador de perfiles (solo stdlib) | `python … --n 1000 --out usuarios.csv --seed 42` · `--joint` siembra desde ENAHO/IPF |
| `research/personas/generador/enaho_loader.py` | Carga/cruza microdato ENAHO → tabla conjunta ponderada | Aplica factor de expansión; recodifica a categorías del modelo |
| `research/personas/generador/ipf.py` | Iterative Proportional Fitting (raking) | Ajusta la semilla ENAHO a marginales objetivo conservando asociación |
| `research/personas/generador/validate.py` | Harness de validación | Marginales+tolerancia, asociaciones, IC bootstrap, estabilidad; `--check` para CI |
| `research/personas/datos_enaho/` | Microdato ENAHO (guía + carpeta de trabajo) | CSV/ZIP gitignored (pesados, regenerables); ver su `README.md` |
| `research/personas/datasets/` | Datasets de ejemplo del generador | ejemplo (200), muestra 22, grupo NSE A |
| `research/personas/laminas/` | Lámina explicativa del sistema (script + PNG) | — |
| `research/personas/apps/reglas/` · `apps/llm/` | Apps web: explorador por reglas (autocontenido) y preguntas libres con Claude (API) | — |
| `research/updates/` | Reportes quincenales de fortalecimiento del modelo | Indexados en este códice (bloque gestionado) |
| `research/fuentes/registro_fuentes.md` | Ledger de evidencia: resumen, rigurosidad, autor y año | Lo mantiene el skill `cronista` |
| `.claude/skills/lapuerta/` | Skill `/lapuerta`: generar + simular usuarios sintéticos | Autocontenido (incluye generador, ipf, validate, simulate_rules) |
| `.claude/skills/cerrajero/` | Skill `/cerrajero`: actualización quincenal a demanda | Investiga, redacta reporte, indexa y commitea |
| `.claude/skills/cronista/` · `seeker/` · `beholder/` · `presentaciones-rimac/` · `actualizar/` | Otras skills del proyecto | Fuentes, investigación, tablero Jira, decks Rimac, publicar a main |
| `.github/workflows/` | Actions: reporte quincenal desatendido + **golden test** del modelo en push/PR | `validar-modelo.yml` corre `validate.py --check` |

## Base de conocimiento (codex)

## 📊 Datos clave — seguros (Perú vs. Mundo)

- **Penetración:** Perú ~**2.08%** del PBI · LatAm 3.2% · Chile 4.6%. CAGR ~12% (2026-2031).
- **Confianza:** plena ~**23-25%**; ~**48% desconfía** (causa #1: falta de información).
  Global cross-industria ~39%. El **broker eleva la confianza** (intermediación).
- **Tenencia:** ~**4/10** tiene/tuvo seguro en 2 años. SOAT conocido por **94%**.
- **Desastres naturales:** solo ~**3.3% de hogares** asegurados, en país altamente sísmico.
- **Brecha de protección global:** ~**US$1.8 billones**; 60% de pérdidas por catástrofe (2024) sin asegurar.
- **Barreras:** precio, desconfianza, baja educación financiera, **sesgos** (present bias, inercia).

## 🧑‍🤝‍🧑 Personas sintéticas — parámetros del generador

- **Matriz legible:** `research/personas/generador/matriz_usuarios_sinteticos.md`
- **Esquema (machine-readable):** `research/personas/generador/synthetic_user_schema.json`
- **Generador:** `research/personas/generador/generate_synthetic_users.py` (solo stdlib)
  - Uso: `python research/personas/generador/generate_synthetic_users.py --n 1000 --out usuarios.csv --seed 42`
  - `--joint fitted.csv` siembra las variables base desde una conjunta ENAHO/IPF (preserva correlaciones).
- **Calibración con dato real:** `enaho_loader.py` (ENAHO → conjunta ponderada) → `ipf.py` (raking a
  marginales objetivo) → generador `--joint` → `validate.py` (mide si calibrar mejoró). Guía en
  `research/personas/datos_enaho/README.md`.
- **Validación:** `research/personas/generador/validate.py` — marginales+tolerancia, asociaciones
  (monotonía + Cramér's V), IC bootstrap, estabilidad (varianza vs n) y `--check` para CI.
- **Datasets de ejemplo:** `research/personas/datasets/` (ejemplo 200, muestra 22, grupo NSE A).
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
- Datasets/salidas generadas → `research/personas/datasets/`; microdato ENAHO → `research/personas/datos_enaho/`.
- Spec (`synthetic_user_schema.json`) y matriz legible (`.md`) se mantienen sincronizados con el generador.
- Artefactos generados (CSV de muestras, ZIP, `__pycache__`, `dist/`) NO se versionan.
- **Evidencia → `cronista`:** toda fuente referenciable usada para crear o fundamentar
  se registra en `research/fuentes/registro_fuentes.md` (resumen, rigurosidad, autor, año).
- ⚠️ Datos sintéticos: prototipado/balanceo/simulación, **no** inferencia causal ni personas reales.

---
*Investigación recopilada 2026-06-21 · codex reorganizado 2026-06-22.*
