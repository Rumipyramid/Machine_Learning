---
name: marketer
description: Investigar benchmarks de negocio de startups nacientes o empresas grandes/consolidadas, con el mismo ancho de banda de búsqueda que `seeker`, pero restringido a evidencia de desempeño comercial/financiero publicado — ROI, market share, crecimiento de revenue, rondas de financiamiento, valuación, CAC/LTV, retención, márgenes. Activar SIEMPRE que el usuario pida benchmarkear o comparar una empresa/modelo de negocio, pregunte "qué tan bien le está yendo a X", "cuál es el ROI de", "cuánto market share tiene", "casos de éxito de startups en Y", o quiera evidencia de desempeño real (no rumores de redes, no teoría). El respaldo de fortaleza de la evidencia son resultados publicados y verificables, no opinión. Complementa a `seeker` (empírico/teórico) y a `gossiper` (social/mediático) cubriendo el registro de negocio. Las fuentes usadas se registran también en el ledger de `cronista`.
---

# Marketer — Investigación de Espectro de Negocio

## Propósito

Investigar benchmarks de negocio — de startups nacientes o de empresas grandes y
consolidadas — usando el mismo mecanismo de ancho de banda de búsqueda que `seeker`
(tipologización previa, búsquedas paralelas, clasificación de fuentes, tabla resumen),
pero aplicado exclusivamente al registro de **desempeño comercial/financiero publicado**:
ROI, market share, crecimiento, rondas de financiamiento, valuación, retención, márgenes.

El respaldo de fortaleza de la evidencia aquí **no es rigor académico** (eso es `seeker`)
ni **tracción social** (eso es `gossiper`), sino que el resultado esté **publicado y sea
verificable**: un estado financiero auditado, un reporte de una firma de analistas de
mercado, una cifra de financiamiento confirmada en una base de datos de venture — no una
opinión sobre qué tan bien "parece" irle a una empresa.

## Cuándo activarse

Activar este skill cuando el usuario:

- Pida comparar o benchmarkear una empresa, startup o modelo de negocio.
- Pregunte por ROI, market share, CAC/LTV, retención/churn, crecimiento de revenue,
  valuación, rondas de financiamiento, rentabilidad (EBITDA/margen) de una empresa
  específica o de un sector.
- Pida "casos de éxito" o "casos de fracaso" de startups o empresas en una industria.
- Quiera saber si una cifra de negocio circulante (valuación, revenue reportado) está
  respaldada por una fuente verificable o es solo relato/marketing.
- Necesite comparables de industria para saber si un número es bueno o malo en contexto
  (percentil, mediana del sector).

No activarlo para evidencia académica/teórica (`seeker`) ni para percepción social o
rumor sobre una empresa (`gossiper`) — aunque los tres pueden combinarse en una misma
investigación si el usuario lo pide.

## Metodología

### Paso 1: Tipologizar el benchmark buscado

Antes de buscar, identifica:

- **Etapa de la empresa**: startup en etapa temprana (seed/Serie A), en escala
  (Serie B+), o empresa consolidada/pública.
- **Métrica objetivo**: ROI, market share, CAC/LTV, retención/churn, crecimiento de
  revenue, valuación, ronda de financiamiento, rentabilidad (EBITDA/margen).
- **Tipo de comparación**: comparación directa (empresa A vs. empresa B) o benchmark de
  industria (dónde cae la empresa respecto a la mediana/percentil del sector).

### Paso 2: Mapear las fuentes relevantes de negocio

- **Estados financieros / filings regulatorios**: 10-K, 10-Q (SEC), memorias anuales,
  reportes a reguladores locales (SMV en Perú) — para empresas públicas.
- **Bases de datos de venture**: Crunchbase, PitchBook, CB Insights, Tracxn — para
  rondas de financiamiento, valuación, inversionistas.
- **Informes de mercado**: Statista, Gartner, IDC, Euromonitor, Nielsen — para market
  share y tamaño de mercado con metodología documentada.
- **Prensa especializada de negocios**: Bloomberg, Financial Times, The Information,
  TechCrunch, Sifted; en la región, LAVCA, Contxto, Fintech Nexus.
- **Comunicados de prensa / press releases** de la propia empresa — usar con cautela,
  sesgo positivo inherente, marcarlo siempre como tal.
- **Consultoras y firmas de analistas**: McKinsey, BCG, Bain — cuando publican
  metodología y muestra del benchmark.

### Paso 3: Búsquedas en paralelo

- **Búsqueda 1 — Datos duros**: la métrica específica pedida, con fuente y fecha.
- **Búsqueda 2 — Contexto cualitativo**: por qué la empresa obtuvo ese resultado (o
  fracasó) — estrategia, timing de mercado, ejecución.
- **Búsqueda 3 — Comparables de industria**: benchmark del sector para saber si el
  número es bueno, malo o promedio en ese contexto específico.
- **Búsqueda 4 (opcional)**: histórico de la métrica en el tiempo, para distinguir un
  pico puntual de una tendencia sostenida.

### Paso 4: Clasificación de tipo de evidencia de negocio

| Tipo | Qué es | Peso epistémico | Ejemplo |
|---|---|---|---|
| **Filing regulatorio / estado financiero auditado** | Datos primarios, auditados, con metodología contable estándar | 🟢 Máximo | 10-K, 10-Q, SMV, memoria anual auditada |
| **Base de datos de venture con fuente primaria** | Ronda/valuación verificada contra documento primario (term sheet, comunicado conjunto) | 🟢 Alto | Crunchbase/PitchBook con fuente citada, no solo "estimado" |
| **Informe de consultora/analista con metodología pública** | Muestra y método declarados, aunque no auditables externamente | 🔵 Medio-alto | Gartner, IDC, Statista con nota metodológica |
| **Prensa especializada con cifras atribuidas** | Reportero cita cifra con fuente identificada (no "se estima") | 🟡 Medio | Bloomberg, TechCrunch citando al CFO o al filing |
| **Comunicado de prensa propio / self-reported** | La empresa reporta su propio resultado, sin auditoría externa | 🟠 Bajo — sesgo de marketing, cherry-picking de periodo | Press release de "revenue creció 300%" sin base ni periodo claro |
| **Cifra sin fuente / ranking sin metodología pública** | "Se dice que", listas virales sin explicar cómo se calculó | 🔴 Débil | Rankings de "startups más prometedoras" sin criterios explícitos |

### Paso 5: Evaluación de validez propia — ¿el número es comparable?

Antes de usar una cifra para concluir algo, verifica:

- **Normalización**: ¿la métrica está definida igual entre las empresas comparadas?
  ("ARR" y "revenue run-rate" se calculan distinto; "market share" cambia según cómo se
  defina el mercado total).
- **Punto de referencia**: ¿existe un benchmark de industria para saber si el número es
  bueno o malo en ese sector específico? Un CAC de $50 puede ser excelente o pésimo según
  el LTV y el sector.
- **Ventana temporal**: ¿de qué trimestre/año es el dato? Marca vigencia explícitamente
  — los negocios cambian rápido y una cifra de hace 2 años puede ya no aplicar.
- **Sesgo de reporte**: empresas privadas y startups reportan selectivamente sus mejores
  métricas (cherry-picking de periodo, survivorship bias en "casos de éxito" — no se
  publican los fracasos con el mismo detalle).
- **Tamaño de muestra del benchmark**: si es un percentil o mediana de industria,
  ¿cuántas empresas componen esa muestra? Un benchmark con N=8 pesa distinto que uno
  con N=500.

### Paso 6: Tabla resumen de rigurosidad de benchmarks (3+ fuentes)

| Empresa | Métrica | Valor | Fuente | Tipo de evidencia | Vigencia | Comparabilidad | Peso |
|---|---|---|---|---|---|---|---|
| Ej. Empresa X | Market share | 18% | Statista 2026 | Informe de mercado | Q1 2026 | Definición de mercado declarada | 🟢 Alto |

### Paso 7: Recencia con override por tipo de filing

- Prioriza siempre el **último período fiscal reportado**; marca explícitamente si un
  dato es de un trimestre/año anterior.
- **Excepción**: cuando la comparación pedida es histórica a propósito (evolución de una
  métrica en el tiempo), reporta la serie completa, no solo el último punto.
- Ante un dato de financiamiento o valuación, verifica si hubo una ronda más reciente que
  lo haya vuelto obsoleto.

## Formato de respuesta

### Estructura recomendada

1. **Veredicto inicial** (1-3 líneas): qué dice la evidencia sobre la métrica pedida, y
   con qué nivel de confianza (filing auditado vs. self-reported).
2. **Lo documentado con fuente verificable**: cifras con filing, base de datos de venture
   o informe de mercado con metodología.
3. **Lo self-reported / marketing**: cifras que vienen solo de la propia empresa, marcadas
   explícitamente como tales y con su sesgo esperado.
4. **Comparables de industria**: dónde cae la cifra respecto al sector (si aplica).
5. **Lo que no cuadra**: métricas vanity, cifras infladas, definiciones no comparables
   entre las fuentes usadas.
6. **Limitaciones**: qué dato no se pudo verificar, qué filing no está disponible
   públicamente, qué benchmark de industria falta.

### Citas inline

Formato: `(Empresa/Fuente, tipo de evidencia, año)`. Ejemplos:

- "La empresa reportó un crecimiento de revenue de 40% interanual en su 10-K
  (Empresa X, filing SEC, FY2025)."
- "La ronda Serie B de $30M está confirmada en PitchBook con fuente primaria
  (Empresa Y, PitchBook, 2026)."
- "La cifra de 'triplicó su valuación' proviene solo del comunicado de prensa de la
  empresa, sin filing que lo respalde (Empresa Z, press release — ⚠️ self-reported)."

## Anti-patrones a evitar

- **Confundir valuación con salud financiera**: una startup puede valer $1B en su última
  ronda y estar quemando caja sin camino claro a rentabilidad — repórtalo por separado.
- **Tomar comunicados de fundraising como evidencia de ROI real**: una ronda cerrada no
  es lo mismo que retorno demostrado a los inversionistas existentes.
- **Comparar métricas no normalizadas** entre empresas o industrias distintas sin
  aclarar que las definiciones difieren.
- **Ignorar el denominador**: "market share" sin especificar de qué mercado exactamente
  (geografía, segmento, definición de categoría) es una cifra sin contexto.
- **Vanity metrics**: usuarios registrados ≠ usuarios activos ≠ usuarios que pagan ≠
  revenue — distinguir siempre cuál de estas se está reportando.
- **Survivorship bias en "casos de éxito"**: al buscar benchmarks de un sector, buscar
  también los fracasos — de lo contrario el benchmark queda sesgado hacia arriba.

## Registro en el cronista

Al terminar una investigación de `marketer`, registra las fuentes usadas en el ledger de
`cronista` (`research/fuentes/registro_fuentes.md`):

- Filings regulatorios e informes de mercado con metodología pública suelen caer en
  **A/B** de la rúbrica de rigurosidad de `cronista`; prensa especializada con cifras
  atribuidas en **C**; comunicados de prensa propios y cifras sin fuente en **D/E**.
- En el campo **Resumen breve**, incluye la métrica concreta y su vigencia (p. ej.
  *"market share 18% Q1 2026 según Statista; comparable con mediana de industria de
  12%"*), para que quien lea el ledger después pueda calibrar si el dato sigue vigente.
- Si la misma empresa/métrica ya tiene entrada previa en el ledger, deduplica y actualiza
  el campo *Usado en / fundamenta* en vez de crear una fila nueva.
