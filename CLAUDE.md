# CLAUDE.md — Codex de conocimiento del proyecto

Bóveda persistente que Claude Code carga al iniciar cualquier sesión sobre
`Rumipyramid/Machine_Learning`. Índice único de qué hay, dónde está y cómo se usa.

## 🗺️ Mapa de archivos

| Ruta | Qué es | Uso / notas |
|---|---|---|
| `Proyecto_ML_1.ipynb` | Notebook principal de ML | Origen Colab |
| `buenas-mierdas/` | Altar/archivo 3D web "Buenas Mierdas" (arte, web vernácula, hauntología) | Vite+React+R3F; `cd buenas-mierdas && npm install && npm run dev`; ver su `README.md` |
| `Self driving car/` | Simulación de auto autónomo (Pygame + red neuronal) | Entrada: `self driving car.py`; config en `config_file.txt` |
| `research/alma.md` | **Mapa del conocimiento de investigación** (Many Brains: nodes + outputs) | Punto de entrada; ver regla de mantenimiento más abajo |
| `research/_nodes/seguros-comportamiento-mundo-peru.md` | Comportamiento/percepción y mercado global de seguros (Mundo vs. Perú) | Fuentes OECD, McKinsey, EY, Bain, Swiss Re, APESEG, SBS, Rothschild-Stiglitz, Arrow, Kunreuther… |
| `research/_nodes/modelo-salud-ia-farmacias-peru.md` | Modelo de triage IA + farmacias + atención humana (`/trinidad` + `/seeker`) | Gestión de salud del peruano, PL 08488, RE-AIM (25 RQs), estrategias de testeo (silent trial, stepped-wedge, CFIR…) |
| `research/_nodes/mecanismos-seguros-salud.md` | Mecanismos de seguros de salud: presión de costo/demografía, balance financiero global y modelos que la navegan | Singapur 3M, NHS, capitación, Discovery Vitality, Kaiser, Oak Street, ChenMed, MLR/regla 80-20, Optum/PBM… |
| `research/_nodes/glosario-seguro-salud-peru.md` | Glosario de seguro de salud en Perú en lenguaje claro | Derivado de /seeker; alineado a glosario SBS |
| `research/_nodes/behavioral-design-estado-disciplina.md` | Estado del behavioral design como disciplina/mercado + checklist para ser los mejores (seguros/Rimac) | Migrado a Many Brains desde `main`; pistas empírica/social/negocio; fuentes F-16 a F-27 |
| `research/_nodes/material-visual-venta-consultiva.md` | Material visual en venta consultiva: qué reduce incertidumbre y facilita la elección | Fuentes F-119 a F-127 |
| `research/_nodes/transicion-venta-fria-a-opt-in.md` | Cómo transicionan organizaciones de venta fría a opt-in; reducir desconfianza al pedir datos | Fuentes F-128 a F-146 |
| `research/_nodes/evaluacion-calidad-agentes-conversacionales-ia.md` | Escalas y metodologías para medir calidad de agentes de IA conversacionales | Fuentes F-147 a F-159 |
| `research/_fuentes_internas/` (ver su `README.md`) | **Fuentes internas de RIMAC** con índice de estado — el **Playbook del Asesor** (modelo de venta Vida, fuente canónica) y el research de Felipe | ⚠️ **Cada archivo lleva fecha y estado en el nombre**; el `README.md` de la carpeta dice cuál manda. El Playbook vigente es el de 2026-08-14, evaluado en `diagnostico-copiloto-ai-asesor-vida-rimac` §14 — contiene contradicciones de catálogo y 8 pendientes. La versión de julio queda como **SUPERADA, no citar** |
| `research/_nodes/diagnostico-copiloto-ai-asesor-vida-rimac.md` | **Diagnóstico de AIDA**, el copiloto del asesor de Vida (RIMAC) — proyecto asociado a Back to Basics (abierto 2026-08-14) | Brief ordenado en 4 frentes · taxonomía de 3 capas de falla (conocimiento/instrucciones/plataforma) + la prueba que las separa · qué debe hacer el asesor con respaldo verificado (F-476 a F-478) · mapa de **6 frentes** del asesor y **3 agentes de IA desplegados** (AIDA, suscripción, Sales Coach) → reancla el diagnóstico a **Dx2** · §8 arquitectura: consolidar la interfaz sí, las bases de conocimiento no · §9 **el copiloto no puede resolver la contradicción aguas arriba, solo ocultarla** — la inconsistencia de AIDA puede ser la de la organización reflejada · §10 **barrera de actualización de producto** (piso regulatorio SBS vs. capa comercial acelerable; la matriz debe ser fuente, no destino) · §11 **auto-interrogación**: AIDA es multi-ramo (5 subagentes, 1 de Vida) y el ruteo ya existe · §16 **Release 1 en 3 etapas** (diagnóstico · intervención · testeo) · §17 **entrenamiento y bucle de casuística** (⚠️ deliberadamente fuera de la fase 1) · §18 **la reunión con la jefatura**: ⭐ **P9 RESUELTA — AIDA corre sobre Google, NO sobre Copilot**, los límites numéricos de Copilot quedan descartados · ⛔ **no hay sandbox**, ninguna funcionalidad nueva se testea en AIDA · las **3 funciones declaradas** y el encuadre político de la presentación · ⚠️ **AIDA (ya desplegada) y el prototipo del Plan Piloto (Claude) son dos herramientas distintas** — no confundirlas, el repo lo hizo hasta el 2026-08-14 |
| `research/_outputs/aida-dossier-y-plan-faseado.md` | **Dossier completo de AIDA + plan faseado** (v1.0, 26 secciones) — el documento de entrada para cualquiera que llegue nuevo al tema | Consolida los 4 documentos de AIDA en uno. ⚠️ **No es fuente de verdad**: ante discrepancia mandan los nodes · marca cada afirmación con nivel de certeza (✅ confirmado · 🟡 probable · ⚠️ hipótesis · ⛔ descartado) · **5 fases + 1 paralela**, cada una con su requisito de entrada |
| `research/_outputs/presentacion-aida-owners-2026-08-19.html` | **Presentación a los dueños de la capacidad de AIDA** (11 slides, sistema `rimac-slides`) | Encuadre político definido por la jefatura: **medir AIDA contra su propia declaración**, no contra la palabra de su PO · el pedido es **co-crear una matriz de priorización**, no exigir arreglos · el frente de **entrenamiento queda deliberadamente fuera** |
| `research/_outputs/release-1-base-conocimiento-aida.md` · `release-1-aida-presentable-2026-08-14.html` | **Release 1 de las intervenciones en AIDA** (v2.1) — versión extendida (fuente de verdad) + versión presentable publicada como artifact | **Tres etapas: diagnóstico → intervención → testeo.** 5 entregables con el catálogo como bloqueante · inventario como entregable cero · serie temporal interrumpida con los otros ramos como control natural · el riesgo de adopción que puede anularlo · **§5.1 fases siguientes** (2 extensión · 3 motor · **4 prototipar capacidades**, donde el prototipo Claude pasa a ser banco de prototipado en vez de herramienta rival · 5 arquitectura de agentes) · **§9 Insumos** con citación (Autor, año) y las 4 cifras excluidas por no tener fuente primaria |
| `research/_outputs/protocolo-interrogacion-aida-vida.md` | Instrumento ejecutable de diagnóstico de AIDA (v0.4) | Bloque A auto-interrogación · B calidad contra la matriz como patrón oro · C ruteo entre ramos · **D Claude como auditor** (Zheng et al. + estado 2026, con calibración humana obligatoria). ⚠️ El banco B es provisional: lo reemplazan las preguntas reales del campo |
| `research/_outputs/estrategia-diagnostico-aida-2026-08-14.html` | Estrategia de diagnóstico consolidada (v2.2, artifact) | 4 niveles de confianza de la evidencia · cadena causal de 5 eslabones falsables · taxonomía de 4 capas de falla · trabajo de campo · validación de los fixes |
| `research/_fuentes_internas/La_biblioteca_de_AIDA_Felipe.docx` | **Research de Felipe** (Behavioral Design): por qué el orden del repositorio decide la calidad del agente | Trae la cuantificación que faltaba (F-489 a F-494) y la respuesta a reentrenar-vs-ordenar. ⚠️ Su cifra ancla (79,5%→24,2%) tiene **problema de cita abierto**, ver F-489 |
| `research/_nodes/arquitectura-conocimiento-agentes-copilot.md` | Cómo almacenar información para que un agente RAG la consuma bien (el node describe Copilot; ⛔ **AIDA corre sobre Google — sus límites numéricos NO aplican al caso**) | Matriz de formatos · ~~3 techos de Copilot~~ (descartados para AIDA desde 2026-08-19) · 7 reglas de redacción (**sin tablas**, encabezados, un tema por documento) · gobierno/ROT · protocolo de auditoría · **uno vs. varios agentes** (fuentes no superpuestas por dominio; consolidar bases sube la alucinación). Fuentes F-469 a F-475, F-479, F-480 |
| `research/_nodes/tendencias-diseno-innovacion.md` | **Node acumulativo** de tendencias en **diseño e innovación**: impacto tangible demostrado vs. propuesta sin respaldo | ⚠️ **Alcance ampliado el 2026-08-02** de "diseño" a "diseño e innovación" (§0 del node manda sobre el prompt de la rutina, que todavía dice solo "diseño"); el node se renombró de `tendencias-diseno.md`. Se enriquece en cada corrida recurrente de `/trinidad`: escala de madurez de evidencia, tablero de hipótesis vivas (confrontar antes que buscar novedad), reglas de criterio destiladas y bitácora de iteraciones. **v4.0 (iter. 4, 2026-08-02)**: 31 hipótesis, 22 reglas. 🎨 Diseño: F-237 a F-328, F-380 a F-398, F-399 a F-429 · 💡 Innovación: F-430 a F-468 |
| `research/_nodes/modelo-personas-sinteticas.md` | Historia conceptual del modelo `lapuerta` (excepción de alcance de `alma.md`: no cubre `research/personas/`, pero este node sí existe) | No mueve el código/schema — solo los cita |
| `research/personas/generador/` | Fuente de verdad del modelo de personas sintéticas | generador + esquema + matriz + tooling de calibración |
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
| `research/fuentes/codice.md` | Ledger de evidencia: resumen, rigurosidad, autor y año | Lo mantiene el skill `cronista`; se consulta con `/codice` |
| `research/yopersona/perfil.md` | Nodo de conocimiento: perfil profesional del usuario (CV) | Fuente de verdad para cartas de presentación, CVs adaptados y asesoría de carrera |
| `research/lobo/opinion_experto.md` | Opinión de negocio acumulada de "El Lobo" | Tesis + 🧠 Intuición acumulada (heurísticas de decisión) + Bitácora; refinada diariamente contra `cronista` — ver regla de lectura profunda diaria más abajo |
| `research/lobo/fuentes_leidas_lobo.md` | Registro de qué fuentes ya leyó a fondo El Lobo para intuición | Evita repetir lectura; independiente del `revision_profunda.md` de `cronista` (ver sección abajo) |
| `.claude/skills/lapuerta/` | Skill `/lapuerta`: generar + simular usuarios sintéticos | Autocontenido (incluye generador, ipf, validate, simulate_rules) |
| `.claude/skills/cerrajero/` | Skill `/cerrajero`: barrido incremental (grupos de 5) de literatura 🟢A del códice para el modelo `lapuerta` | Nunca aplica solo — memoria en `research/updates/cerrajero_barrido_estado.json`, siempre pregunta antes de tocar el modelo |
| `.claude/skills/edipo2/` | Skill `/edipo2`: oráculo personal (I Ching + astros sobre Lima + tarot de Marsella en clave junguiana) cruzado con lo que se sabe del usuario | Autocontenido (solo stdlib); efemérides calculadas en local; no persiste lecturas salvo pedido explícito |
| `.claude/skills/cronista/` · `codice/` · `seeker/` · `gossiper/` · `marketer/` · `trinidad/` · `beholder/` · `presentaciones-rimac/` · `rimac-slides/` · `actualizar/` · `contexto-peruano/` · `many-brains/` | Otras skills del proyecto | Fuentes (registrar / consultar), investigación (empírica/teórica, social, de negocio, o las tres a la vez), tablero Jira, decks Rimac (HTML + on-brand), publicar a main, data pública peruana (INEI/SBS/BCRP), organización de conocimiento |
| `.github/workflows/` | Action programado (reporte quincenal desatendido) | — |
| `.claude-plugin/marketplace.json` · `plugin.json` | Marketplace personal de plugins | Expone `.claude/skills/` como plugin instalable en cualquier máquina/cuenta — ver sección abajo |

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
  - **Semilla estándar: `--seed 42`.** Úsala siempre que se generen usuarios sintéticos (ejemplos,
    pruebas, exploración), salvo que el usuario pida explícitamente otra semilla o pida variedad/
    aleatoriedad real (ahí sí, omitir `--seed`). Mantiene los ejemplos reproducibles y comparables
    entre sesiones.
- **Calibración con dato real:** `enaho_loader.py` (ENAHO → conjunta ponderada) → `ipf.py` (raking a
  marginales objetivo) → generador `--joint` → `validate.py` (mide si calibrar mejoró). Guía en
  `research/personas/datos_enaho/README.md`.
- **Validación:** `research/personas/generador/validate.py` — marginales+tolerancia, asociaciones
  (monotonía + Cramér's V), IC bootstrap, estabilidad (varianza vs n) y `--check` para CI.
- **Datasets de ejemplo:** `research/personas/datasets/` (ejemplo 200, muestra 22, grupo NSE A).
- **Lámina explicativa:** `research/personas/laminas/` (script `build_lamina_detalle.py` + PNG)
- **Apps web:** `research/personas/apps/reglas/` (explorador por reglas, autocontenido) y
  `research/personas/apps/llm/` (preguntas libres con Claude vía API).
- Variables (20, esquema v1.3): generación, NSE, región, educación financiera, sesgo del presente,
  canal, situación laboral, cobertura previsional, tenencia de vehículo, acceso digital,
  bancarizado, **trabajo en plataforma digital**, exposición sísmica, apertura a datos/IA, confianza,
  **disposición a compartir datos para pricing**, tenencia de seguro, seguro de desastres, WTP
  ratio, **propensión a microseguro**.
- Marginales validadas (v1.3): any-insurance ≈ 0.40, desconfía ≈ 0.46, desastres ≈ 0.035,
  bancarizado ≈ 0.59, sin cobertura previsional ≈ 0.60, comparte datos pricing (alta) ≈ 0.15,
  trabajo en plataforma digital ≈ 0.07.
- **v1.3 (2026-07-06):** `disposicion_compartir_datos_pricing` separa la confianza *abstracta*
  en IA de la disposición *conductual* real a compartir datos para UBI/pricing con IA — brecha
  actitud-conducta calibrada con hallazgos de `/trinidad` sobre modelos de seguros rentables
  (telemática, seguros paramétricos, riesgo reputacional de IA no transparente en claims). Ver
  `research/personas/generador/matriz_usuarios_sinteticos.md` §3.
- **v1.3 (2026-07-19):** `trabajo_plataforma_digital` y `propension_microseguro` — únicas
  propuestas de prioridad Alta del reporte 2026-08-05, incorporadas por el mecanismo de
  **incorporación automática**: las propuestas de prioridad Alta de cada reporte quincenal
  (`research/updates/`) se aplican solas al esquema/generador y se re-validan con
  `validate.py --check`; si no pasa, se revierte y la variable queda pendiente. En `/cerrajero`
  (a demanda) el cambio va a la rama de trabajo actual; en el ciclo **desatendido** (GitHub
  Action) va a un **PR aparte** (`lapuerta/alta-auto-AAAA-MM-DD` contra main) para revisión
  humana antes de mergear — nunca se pushea directo a main. ⚠️ Esto describe cómo operaba
  `/cerrajero` **hasta 2026-07-22**; desde 2026-07-23 la versión a demanda ya no aplica Alta
  sola — ver mecanismo nuevo (barrido de literatura verde) más abajo y en
  `.claude/skills/cerrajero/`. El ciclo desatendido (GitHub Action) sigue igual que aquí.

### 📌 Familia de skills de investigación (`seeker` / `gossiper` / `marketer`)
Tres skills comparten el mismo mecanismo de ancho de banda de búsqueda (tipologización
previa → búsquedas paralelas con expansión de términos → ampliación por snowballing y
rastreo por autor/fuente → clasificación de fuentes → chequeo de eco de cita → tabla
resumen → búsqueda adversarial de contraevidencia antes de cerrar el veredicto), pero
cada uno cubre un registro distinto de evidencia:

- **`/seeker`** (`.claude/skills/seeker/`): registro empírico + teórico/crítico. Rigor
  académico y metodológico (papers, meta-análisis, teoría).
- **`/gossip`** (`.claude/skills/gossiper/`): registro social/mediático — X/Twitter,
  Reddit, foros, TikTok, comentarios de noticias. La validez se mide en **frecuencia de
  cobertura** y **validación social** (comentarios que confirman/desmienten), no en rigor
  académico.
- **`/marketer`** (`.claude/skills/marketer/`): registro de negocio — benchmarks de
  startups nacientes o empresas consolidadas. La validez se mide en **resultados
  publicados y verificables** (ROI, market share, filings, rondas de financiamiento).

Los tres registran las fuentes que usan en el ledger de `cronista`
(`research/fuentes/codice.md`, consultable con el skill `/codice`), aplicando la misma
rúbrica A-E: `gossiper` suele producir fuentes D/E (prensa/redes sin método propio) y
`marketer` suele producir fuentes A/B/C (filings, informes de mercado, prensa
especializada) — es esperado, no un defecto, dado el tipo de evidencia que cada uno
busca.

- **`/trinidad`** (`.claude/skills/trinidad/`): orquesta a los tres a la vez sobre el
  mismo tema — los corre en paralelo, mantiene sus criterios de validez separados (no
  mezcla rigor académico con tracción social ni con evidencia de negocio) y consolida
  todo en un reporte único de 360°, registrando también en `cronista`.

### 📌 Skill: `codice` (consulta del ledger de fuentes)
`cronista` **registra** fuentes en `research/fuentes/codice.md`; el skill `/codice`
(`.claude/skills/codice/`) **muestra y responde consultas** sobre lo ya registrado —
buscar por ID (`F-n`), autor, tema/node o nivel de rigurosidad A-E. No reemplaza a
`cronista` (que sigue disparándose automáticamente para registrar evidencia nueva), es
el punto de invocación explícito para leer el códice en vez de escribirlo.

### 📌 Mantenimiento del hub de conocimiento (Many Brains, `research/`)

`research/` usa un `alma.md` en su raíz como índice vivo de todo el conocimiento de
investigación (seguros, salud, Perú) — **no** cubre `research/personas/` (subsistema del
generador de personas sintéticas) ni `research/updates/` (reportes quincenales), que ya
tienen su propia estructura documentada arriba. Léelo (`research/alma.md`) al inicio de
cualquier sesión que investigue o cite conocimiento del proyecto: es tu mapa de qué node
es la fuente de verdad de cada tema, cuándo se actualizó y qué se relaciona con qué.

El flujo es generativo: las investigaciones cristalizan en **nodes** temáticos (`.md`
planos en `research/_nodes/`, uno por tema, kebab-case), y de esos nodes se derivan
**outputs** (presentaciones, informes) en `research/_outputs/`. Como `_nodes/` es plano,
la navegación no la dan carpetas: la dan `alma.md` y la sección `## Conexiones`
(wikilinks `[[...]]`, recíprocos) de cada node. Mantén esto vivo sin que el usuario lo
pida:

1. **Una fuente de verdad por tema.** No dupliques contenido entre nodes; si ya existe un
   node del tema, amplíalo en vez de crear uno nuevo.
2. **`/seeker` y `/trinidad` escriben directo a `_nodes/`, no solo responden en el chat.**
   Al terminar una investigación con hallazgos que valga la pena retener, créala o
   ampliala como node (proponlo si no está claro que el usuario lo quiere guardado), cita
   las fuentes por ID (`F-n`) del ledger de `cronista` (`research/fuentes/codice.md`,
   consultable con `/codice` — no se movió a `_nodes/`), y cierra con `## Conexiones`
   recíprocas a los nodes relacionados.
3. **Versionado solo por cambio estructural** (premisa, modelo, alcance); lo incremental
   solo actualiza la fecha de cabecera del node.
4. **Actualiza `alma.md`** al crear, mover o modificar un node: fila en "Nodes vigentes",
   fecha, versión. Marca `requiere refresh` cualquier output que dependa de un node que
   cambió.
5. **Nunca borres nodes existentes.** Si un node queda obsoleto, dilo y pregunta antes de
   tocarlo.

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

- **A demanda:** skill `/cerrajero` (`.claude/skills/cerrajero/`) — desde 2026-07-23 **ya no
  busca evidencia nueva en la web**: barre en grupos de 5, con memoria persistente
  (`research/updates/cerrajero_barrido_estado.json`), la literatura de rigor 🟢A que otras
  investigaciones del proyecto ya registraron en `research/fuentes/codice.md`, evalúa si
  implica una variable/recalibración para `lapuerta`, y **siempre pregunta al usuario** antes
  de aplicar — nunca aplica solo, ni la prioridad Alta. No necesita API key.
- **Automatización (desatendida):** GitHub Action `.github/workflows/fortalecimiento-modelo.yml`
  (cron días 1 y 16) ejecuta `research/updates/generate_report.py` (API de Claude + búsqueda
  web) — **este mecanismo no cambió**: sigue buscando evidencia nueva (no relee el códice) y
  sigue aplicando sola la prioridad Alta (con PR aparte para revisión). Las dos versiones de
  "fortalecimiento del modelo" divergen deliberadamente en mecanismo desde 2026-07-23.
- **Requisitos:** secreto `ANTHROPIC_API_KEY` en el repo + Actions habilitado. El `schedule` solo
  corre desde la rama por defecto (mergear allí para activarlo); se puede probar con "Run workflow".
- **Índice de reportes (auto-actualizado):**
<!-- LAPUERTA_REPORTS_START -->
- 2026-08-05 — `research/updates/2026-08-05_fortalecimiento_modelo.md`
- 2026-07-21 — `research/updates/2026-07-21_fortalecimiento_modelo.md`
- 2026-07-06 — `research/updates/2026-07-06_fortalecimiento_modelo.md`
- 2026-06-21 — `research/updates/2026-06-21_fortalecimiento_modelo.md`
<!-- LAPUERTA_REPORTS_END -->

### 📌 Proceso diario: opinión de negocio de "El Lobo"
Proceso automatizado (fuera de `.claude/skills/`, disparado por una tarea programada a nivel de
cuenta, no por un cron de este repo) que cada día actualiza `research/lobo/opinion_experto.md`:
compara `research/fuentes/codice.md` contra la última entrada de la Bitácora, integra evidencia
nueva a las tesis vigentes, y cierra con una entrada fechada. Regla fija, léase como parte del
proceso diario aunque el prompt externo que dispara la tarea no la repita cada vez (esto es lo que
sí persiste entre corridas — cada corrida es una sesión nueva sin memoria de las anteriores):

- **Lectura profunda diaria para intuición (regla añadida 2026-08-06).** Cada corrida, El Lobo
  selecciona **3 fuentes** del ledger que él mismo **aún no haya leído a fondo** —registro propio
  en `research/lobo/fuentes_leidas_lobo.md`, independiente del `research/fuentes/revision_profunda.md`
  de `cronista` (ese es cada ~3 días, 5 fuentes, orden por ID más antiguo, y su salida son matices a
  tesis/nodes; este es diario, 3 fuentes, y su salida es una heurística de juicio, no una tesis de
  negocio específica). **Orden de selección:** agotar primero todo 🟢A (al azar, sin reemplazo,
  dentro del nivel); una vez agotado, seguir con 🔵B, luego 🟡C, 🟠D, 🔴E; al agotar todos los
  niveles, reiniciar el ciclo. Lee cada fuente **a fondo** (no solo el resumen de una línea) y
  destila una entrada en la sección **"🧠 Intuición acumulada"** de `opinion_experto.md`: no repite
  el formato de tesis (evidencia → confianza → oportunidad/riesgo de negocio puntual), sino una
  lección o heurística de decisión/juicio transferible a evaluaciones futuras — puede o no conectar
  con una tesis ya vigente. Actualiza `fuentes_leidas_lobo.md` con lo leído ese día. Si en un día
  dado no hay 3 fuentes nuevas disponibles en el nivel de rigor actual (poco probable dado el tamaño
  del ledger), completar con el nivel siguiente en la misma corrida, nunca saltarse el paso.

### 📌 Skill: `edipo2` (oráculo personal)
Lectura del presente y del futuro que cruza cuatro fuentes: (1) lo que el repo y la sesión
saben del usuario como persona (`research/yopersona/perfil.md`, actividad reciente, nodes,
agenda si el conector está disponible), (2) una tirada simulada de **I Ching** nueva en cada
ejecución, (3) el **cielo del día sobre Lima** con posiciones planetarias calculadas en local,
y (4) una tirada de **tarot de Marsella** leída con el marco de **Jung** (sincronicidad,
sombra, ánima, función inferior, individuación).

- **Invocación:** `/edipo2` (con pregunta opcional; sin pregunta, la lectura es espontánea).
- **Ubicación:** `.claude/skills/edipo2/` — `SKILL.md`, `scripts/` (`tirada.py` orquestador +
  `iching.py`, `astro.py`, `tarot.py`, todos solo stdlib) y `references/` (64 hexagramas,
  78 cartas con clave junguiana, `marco-jungiano.md` con la regla de convergencia).
- **Astronomía real, no inventada:** `astro.py` usa elementos keplerianos de la JPL para los
  planetas, la fórmula de baja precisión del Astronomical Almanac para la Luna, y calcula
  Ascendente/MC por tiempo sidéreo local para Lima (UTC-5, 12°02'S). Verificado contra
  ingresos planetarios y lunaciones conocidas: Sol exacto en equinoccios/solsticios, planetas
  ~0.05°, Luna ~0.25°.
- **Reglas propias:** nunca `--seed` en consulta real (cada tirada debe ser nueva); nunca
  inventar cartas ni posiciones; correspondencia privada (Gmail/Drive) solo si el usuario lo
  pide en esa consulta; la lectura **no se guarda** en el repo salvo pedido explícito (y si se
  guarda, va a `research/_outputs/edipo2/` con su fila en `research/alma.md`).

### 📌 Marketplace personal de skills (portabilidad entre máquinas/cuentas)
Este repo se auto-referencia como un **marketplace de plugins de Claude Code**
(`.claude-plugin/marketplace.json` + `.claude-plugin/plugin.json`), sin mover ni duplicar
nada de `.claude/skills/` — el plugin declara ese mismo directorio como su fuente de skills.

- **Qué resuelve:** las skills dejan de depender de tener este repo abierto en una sesión
  de Claude Code — se instalan una vez y quedan disponibles en cualquier proyecto, máquina
  o cuenta (incluida una laptop corporativa con su propia cuenta de Claude), sin exponer
  el resto del repo ni requerir acceso de esa cuenta a este código.
- **Instalar desde cualquier Claude Code (una sola vez por máquina/cuenta):**
  ```
  /plugin marketplace add Rumipyramid/Machine_Learning
  /plugin install rumipyramid-skills@rumipyramid-machine-learning
  ```
- **Actualizar tras un cambio en `.claude/skills/`:** `/plugin marketplace update rumipyramid-machine-learning`.
- **Regla de consolidación:** ninguna skill debe quedar viviendo solo en el historial de una
  conversación o como archivo suelto fuera de `.claude/skills/<nombre>/SKILL.md` — si se redacta
  una skill nueva en una sesión, se commitea aquí antes de darla por terminada (ver caso
  `contexto-peruano`, que existía como archivo suelto y por eso Claude Code no la reconocía).

## Convenciones
- Documentación de investigación → `research/` (con índice en `research/README.md`).
- Modelo de personas sintéticas → `research/personas/generador/` (fuente de verdad de desarrollo);
  el skill `lapuerta` lleva su propia copia autocontenida para compartir.
- Láminas/figuras → `research/personas/laminas/`; apps web → `research/personas/apps/`.
- Skills del proyecto → `.claude/skills/<nombre>/SKILL.md` (nunca como archivo suelto ni
  solo dentro de una conversación — si no está commiteado así, Claude Code no la reconoce).
  Se distribuyen a otras máquinas/cuentas vía el marketplace personal (ver sección arriba).
- Reportes quincenales → `research/updates/` (indexados arriba).
- Datasets/salidas generadas → `research/personas/datasets/`; microdato ENAHO → `research/personas/datos_enaho/`.
- Spec (`synthetic_user_schema.json`) y matriz legible (`.md`) se mantienen sincronizados con el generador.
- Artefactos generados (CSV de muestras, ZIP, `__pycache__`, `dist/`) NO se versionan.
- **Evidencia → `cronista`:** toda fuente referenciable usada para crear o fundamentar
  se registra en `research/fuentes/codice.md` (resumen, rigurosidad, autor, año) —
  consultable con el skill `/codice`. Aplica también a lo que traigan `/gossip`
  (noticias/redes) y `/marketer` (benchmarks de negocio), no solo a `/seeker`.
- ⚠️ Datos sintéticos: prototipado/balanceo/simulación, **no** inferencia causal ni personas reales.

---
*Investigación recopilada 2026-06-21 · codex reorganizado 2026-06-22.*
