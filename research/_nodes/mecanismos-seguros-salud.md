# Mecanismos de seguros de salud: presión actual y modelos que la navegan

> Node. Fuente de verdad de este tema. Rescata 3 investigaciones `/seeker`/`/trinidad` que
> originalmente solo vivían en el chat (2026-07-10). Fuentes indexadas en
> `fuentes/codice.md` (F-86 a F-116, F-193 a F-207, F-469 a F-521).
>
> Fecha de elaboración: 2026-07-10 · Última actualización: 2026-09-03 · Versión: **v2.2**
> (v1.1 amplía con §2: balance financiero global/rentabilidad de la categoría; v1.2 amplía
> con §2.6: contraste regional Europa/Asia/Perú-Latam)

### §0 — Ampliación de alcance (2026-09-02, v2.0)

⚠️ **El alcance de este node se amplió** de "mecanismos de aseguramiento y modelos que navegan la
presión de costo" a **la pregunta de eficiencia completa**: qué reduce efectivamente el gasto
médico —dentro y fuera de lo clínico— y qué modelos de negocio de salud logran a la vez
rentabilidad y mejora de salud. Se conservan §1-§5 sin cambios de numeración (el ledger cita §2.4,
§3 y §4) y se agregan cuatro capítulos nuevos:

- **§6** — Intervenciones **no médicas** (cuidado, hábitos, determinantes sociales): ¿reducen el
  gasto a lo largo del tiempo?
- **§7** — Palancas **clínicas** de costo-eficiencia del gasto en tratamiento, ordenadas por
  magnitud del efecto verificado.
- **§8** — Matriz de modelos de negocio por **rentabilidad verificada × mejora de salud
  demostrada**, y el correctivo del ciclo 2025-2026.
- **§9** — Síntesis v2.0: seis reglas transversales y su lectura para el caso peruano.
- **§10** *(v2.1, 2026-09-03)* — **Cuidado integral, modelo de Porter y autoatención digital**:
  corrige el §6 separando *programa añadido* (sin retorno probado) de *rediseño del modelo de
  atención con cambio de riesgo* (con retorno probado), evalúa la base de evidencia del modelo de
  Porter, y ordena el arsenal del asegurador por efecto verificado sobre siniestralidad. Añade
  las reglas 7, 8 y 9.
- **§11** *(v2.2, 2026-09-03)* — **Glosario operativo**: definición corta de cada estrategia de
  §1-§10 con tres columnas — impacto en salud, impacto en negocio y nivel de evidencia — más los
  cinco conceptos que explican los fracasos. No introduce fuentes nuevas: destila el node.

**Regla de lectura**: donde §8 y §2/§3/§4 hablen del mismo actor (Kaiser, Discovery, Oak Street),
**§8 manda** — incorpora datos financieros más recientes y, en el caso de Oak Street, el desenlace
del caso que §4 había dejado abierto.

---

## 1. ¿Está "roto" el modelo de mancomunación de riesgo?

**Pregunta original**: ¿es correcto decir que el modelo por el que la gente sana subsidia a la
gente enferma está roto, porque ahora la gente vive más, se siniestra más y busca atención con
más frecuencia?

**Veredicto**: parcialmente correcto, pero sobre-simplificado en dos puntos.

- **"La gente vive más" — cierto**: esperanza de vida global de 46 años (1950) a >70 (2023); 65+
  pasará de 524M (2010) a ~1,500M (2050) (F-86, ⚠️ agregador no verificado contra WHO/UN directo).
- **"Se siniestra más" — cierto, con matiz causal**: envejecimiento se asocia a más enfermedad
  crónica/multimorbilidad (F-87, 🟢 peer-reviewed). Costo médico global sube 9.5%→10%→10.3%
  (2024-2026). **Pero el driver #1 no es el envejecimiento**: es nueva tecnología médica (74% de
  aseguradoras la citan), seguido de deterioro de sistemas públicos (52%) y farmacéutica (49%)
  (F-88, reporte de industria WTW).
- **"Busca atención al respecto" — cierto, pero NO es nuevo**: es el **riesgo moral** (moral
  hazard) formalizado por **Pauly (1968)** — buscar más atención al estar asegurado es conducta
  económica racional (responde al precio marginal), no "mala fe". Es una propiedad estructural
  del seguro desde su diseño teórico, no un fenómeno reciente causado por la longevidad (F-89, 🟢
  peer-reviewed, AER, paper fundacional del campo).
- **"El modelo está roto" — documentado, pero condicional, no universal**: existen casos reales
  de colapso por selección adversa ("espiral de la muerte"): un bloque individual de 1981 con
  primas escaladas a ~7x hacia 2009 (F-90, 🟢 peer-reviewed); Nueva York, tras *community rating*
  sin mandato, redujo su mercado individual a 17,000 asegurados hacia 2013 (casi colapso total);
  Blue Cross/Blue Shield mostró evidencia temprana similar (F-91, 🟢 peer-reviewed); Harvard 1995
  (sanos migraron al plan barato, encareciendo el generoso hasta volverlo insostenible).
  **Pero no ocurre automáticamente por demografía** — ocurre específicamente con *community
  rating sin mandato ni ajuste de riesgo*. Donde existen mandatos + ajuste de riesgo (ACA), el
  pool se ha sostenido (F-92, 🟢 peer-reviewed).

**Tensión activa que sí valida la intuición del "roto"**: hay literatura académica documentando
cómo el self-tracking/telemetría empuja a la industria hacia pricing personalizado que reduce la
subsidización cruzada (F-94, 🟢 peer-reviewed) — el mercado está respondiendo a la presión
alejándose de la solidaridad pura, no porque colapsó de golpe sino porque se está rediseñando.
Conecta directamente con `disposicion_compartir_datos_pricing` en el modelo `lapuerta`
(ver [[modelo-salud-ia-farmacias-peru|Modelo de triage IA + farmacias]]).

---

## 2. Balance financiero global: ¿es rentable la categoría de seguros de salud?

**Pregunta original**: ¿cuál es el balance de los seguros de salud en el mundo? ¿la
categoría está siendo rentable?

**Veredicto**: sí es rentable, pero con un margen de utilidad de suscripción
estructuralmente delgado y bajo compresión — y la mayor parte de la utilidad real del
sector hoy no viene de asegurar, viene de negocios adyacentes verticalmente integrados
(farmacia/PBM). "Rentable" y "con márgenes de suscripción altos" son dos afirmaciones
distintas; la evidencia solo respalda la primera.

### 2.1 El dato agregado más reciente: rentable, pero con margen fino

La industria de seguros de salud de EE.UU. (el mercado que concentra ~80% de las primas
de salud privadas del mundo, F-196, 🟠D) reportó una ganancia de suscripción de USD 8,900
millones en el primer semestre de 2025 — un margen de utilidad de apenas **1.8%** sobre
ingresos (NAIC, F-193, 🔵B, regulador oficial). No es una categoría en pérdida agregada,
pero tampoco es un negocio de márgenes altos: 1.8% es un margen fino para cualquier
industria.

### 2.2 La tendencia es de compresión, no de expansión

El medical loss ratio (proporción de la prima que se destina a pagar atención médica,
ver §2.3) superó el **87%** en años recientes, y los márgenes de suscripción cayeron a un
mínimo de 7 años (**2%**) en 2022, por el retorno de procedimientos médicos post-pandemia
y el alza de costos unitarios (KFF, F-194, 🔵B). Esto confirma, con cifra agregada, la
misma presión de costo que documenta §1: el costo médico global sube consistentemente
(9.5%→10%→10.3%, F-88), y ese costo se traduce directamente en menos margen para el
asegurador, no solo en primas más altas para el asegurado.

### 2.3 Por qué el margen es delgado: está limitado por regulación, no solo por competencia

En EE.UU., la regla del **80/20** de la ACA (el "medical loss ratio" o MLR) obliga
legalmente a los aseguradores a destinar al menos 80% (pólizas individuales/grupo
pequeño) u 85% (grupo grande) de cada prima a atención médica o mejora de calidad — el
resto (administración + utilidad) no puede superar 15-20% de la prima, y si lo supera,
el excedente se devuelve como reembolso a los asegurados (entre 2012-2023 se devolvieron
USD 11,800 millones en reembolsos por este motivo — HealthCare.gov/Commonwealth Fund,
F-197, 🔵B). **Esto es un techo de utilidad puesto por diseño regulatorio**, no solo el
resultado de competencia de mercado — un dato importante para no asumir que un margen
delgado significa automáticamente una industria en crisis: en parte es una industria
regulada explícitamente para que no gane más de cierto umbral sobre la prima pura.

### 2.4 Dónde está la rentabilidad real: no en asegurar, en la integración vertical

Si el margen de suscripción está topado por regulación, ¿dónde gana dinero el sector?
La evidencia más directa (un filing regulatorio primario, no una estimación de prensa)
lo muestra con un solo número: en el segundo trimestre de 2026, la unidad de gestión de
beneficios farmacéuticos (PBM) del asegurador más grande de EE.UU. —Optum Rx, de
UnitedHealth Group— reportó **USD 38,300 millones en ingresos y USD 1,500 millones en
utilidad operativa en un solo trimestre** (UnitedHealth Group, SEC Form 8-K, F-198, 🟢A)
— y su principal cliente es la propia aseguradora del mismo grupo. No es un caso aislado:
tres empresas (CVS Caremark, Cigna Express Scripts, UnitedHealth Optum Rx) procesan el
**80% de los reclamos de recetas** en EE.UU., y las tres están integradas verticalmente
con una aseguradora grande (Drug Channels, F-199, 🟡C). El propio sector reconoce que el
modelo tradicional de utilidad del PBM (ganar por la diferencia entre lo que cobra al
plan y lo que paga a la farmacia — "spread pricing") atraía crítica suficiente como para
que Optum Rx anunciara en 2026 un cambio a tarifa fija por miembro, independiente del
precio de lista del fabricante (Bloomberg, F-200, 🟡C).

**Lectura para el proyecto**: la pregunta "¿es rentable el seguro de salud?" tiene una
respuesta distinta según qué parte del negocio se mida. El *seguro puro* (prima menos
reclamos) es rentable pero con margen fino y regulado. El *negocio adyacente
verticalmente integrado* (farmacia, gestión de beneficios, y en otros mercados also
provisión directa — ver Kaiser Permanente en §3) es donde se concentra la utilidad real
hoy en los actores más grandes.

### 2.5 El reto de costo más agudo y actual: medicamentos especializados (GLP-1)

Dentro de "sube el costo médico" (§1), el driver más agudo en 2026 tiene nombre propio:
el gasto en farmacia es el componente de costo médico de más rápido crecimiento del año
(+14.8% interanual), impulsado principalmente por medicamentos GLP-1 para pérdida de
peso/diabetes (MedCity News, F-201, 🟠D). 43% de los planes de salud rankean el manejo de
costos de medicamentos especializados como su objetivo número uno para 2026, y algunos
empleadores vieron los GLP-1 saltar de ser su gasto farmacéutico #32 a ser el #1 en un
solo año (Mercer, F-202, 🟡C, encuesta propia a empleadores). Es un ejemplo concreto y
actual de "nueva tecnología médica" — la causa #1 de presión de costo que ya identificaba
§1 (F-88) — no una categoría nueva de reto, sino la manifestación más reciente y aguda de
la misma causa.

### 2.6 Fuera de EE.UU.: ¿el mismo patrón de margen delgado?

La limitación declarada en la v1.1 de este node (ver Limitaciones) era que todo el dato
financiero agregado de §2.1-§2.5 era estadounidense. Una ronda adicional de `/trinidad`
buscó específicamente el contraste regional — Europa, Asia y Perú/Latinoamérica — y
encuentra que **el patrón de EE.UU. (margen delgado, regulado por ley) no se repite igual
en mercados sin un techo regulatorio equivalente a la regla 80/20**.

- **Europa — rentabilidad sólida y creciente.** El segmento Vida y Salud de Allianz (el
  mayor grupo asegurador europeo) tuvo una utilidad operativa récord de EUR 9,000 millones
  en el año completo 2025, y EUR 2,400 millones solo en el primer trimestre de 2026
  (+11.1% interanual) — impulsada por un mejor resultado del propio servicio de seguros, no
  por inversión financiera (F-203, 🔵B). Bupa Group reportó una utilidad subyacente de GBP
  1,009 millones para 2025 (+16% a tipo de cambio constante), impulsada por el crecimiento
  de primas en seguro de salud individual/corporativo e IPMI (F-204, 🟠D). Ninguno de los
  dos mercados europeos de estos casos tiene un equivalente estricto de la regla 80/20
  estadounidense — consistente con la hipótesis de §2.3 de que el margen delgado de EE.UU.
  es en buena parte un techo regulatorio, no solo el resultado de la competencia.
- **Asia — crecimiento fuerte, con la misma sombra de selección adversa que EE.UU.** Niva
  Bupa (India) reportó un salto de utilidad de 67% en el trimestre cerrado en marzo de 2026
  (F-205, 🟠D). El mercado de seguros de salud de China se proyecta de USD 150,628M (2025) a
  USD 254,657M (2033), aunque el segmento público —no el privado— sigue siendo el mayor
  (78.31% del total, F-206, 🟡C). Pero el crecimiento de primas de salud comercial en China
  se desaceleró de forma marcada: 8.2% en 2024 vs. un CAGR de 20.5% en 2016-2019, con el
  Swiss Re Institute atribuyéndolo en parte a un **riesgo creciente de selección adversa**
  (F-207, 🔵B) — el mismo mecanismo teórico de §1, ahora con evidencia de mercado real fuera
  de EE.UU.
- **Perú/Latinoamérica — hueco de dato confirmado, no relleno.** Se buscó explícitamente
  rentabilidad/balance financiero agregado del mercado de EPS peruano y de seguros de salud
  privados en Latinoamérica. No se encontró ninguna fuente con datos de margen o utilidad
  agregada del sector (ni de SUSALUD ni de asociaciones gremiales) — solo aparecieron sitios
  de comparación de precios al consumidor, sin dato financiero agregado utilizable como
  fuente. Se declara la ausencia de resultado en el texto del node en vez de forzar una
  entrada débil en el ledger de `cronista` (mismo criterio que la "pista social sin
  cobertura" en [[material-visual-venta-consultiva|Material visual en venta consultiva]]).
  **Sigue siendo una pregunta abierta del proyecto.**

**Lectura conjunta con §2.1-§2.5**: el hallazgo central no cambia — el margen delgado
documentado en EE.UU. es en gran parte una consecuencia de su propio diseño regulatorio
(regla 80/20), no una propiedad universal del ramo de seguros de salud. Fuera de ese marco
regulatorio específico, la categoría muestra rentabilidad sólida y en expansión en Europa y
Asia, con el mismo riesgo estructural de selección adversa (§1) apareciendo en China según
crece el mercado privado.

### Tabla de rigurosidad (balance financiero)

| Fuente | Tipo | Rigor | Nota |
|---|---|---|---|
| NAIC, 2025 Mid-Year Results (F-193) | Regulador oficial, datos agregados | 🔵 B | Margen de utilidad agregado: 1.8% |
| KFF, Health Insurer Financial Performance (F-194) | Organización de políticas de salud | 🔵 B | MLR >87%, margen mínimo de 7 años en 2022 |
| Oliver Wyman, Q1 2025 (F-195) | Consultora actuarial | 🟡 C | Dato trimestral de MLR de grandes públicas |
| Risk & Insurance (F-196) | Prensa especializada | 🟠 D | Crecimiento global desacelerando a 0.5% en 2026 |
| HealthCare.gov / Commonwealth Fund, regla 80/20 (F-197) | Regulación oficial + análisis de fundación | 🔵 B | Techo de utilidad puesto por diseño regulatorio |
| UnitedHealth Group, filing SEC Q2 2026 (F-198) | Filing regulatorio primario | 🟢 A | Optum Rx: USD 1,500M de utilidad operativa en un trimestre |
| Drug Channels (F-199) | Analista especializado | 🟡 C | 3 PBMs = 80% de reclamos, integrados verticalmente |
| Bloomberg, Optum Rx (F-200) | Prensa financiera | 🟡 C | Cambio de modelo de utilidad del PBM más grande |
| MedCity News, GLP-1 (F-201) | Prensa de negocio de salud | 🟠 D | Farmacia +14.8% interanual, el driver más agudo |
| Mercer, GLP-1 2026 (F-202) | Consultora de beneficios | 🟡 C | 43% de planes priorizan manejo de costo especializado |
| Allianz SE, comunicado de resultados (F-203) | Filing/comunicado oficial de empresa pública | 🔵 B | Vida y Salud: EUR 9,000M utilidad operativa FY2025 |
| Health & Protection, Bupa Group (F-204) | Prensa especializada | 🟠 D | GBP 1,009M utilidad subyacente 2025, +16% |
| Insurance Business Asia, Niva Bupa (F-205) | Prensa especializada | 🟠 D | +67% utilidad trimestral (India) |
| Grand View Research, China (F-206) | Firma de investigación de mercado | 🟡 C | Mercado USD 150,628M (2025) → USD 254,657M (2033) |
| Swiss Re Institute, China (F-207) | Instituto de investigación de reaseguradora | 🔵 B | Crecimiento de primas desacelera 20.5%→8.2%, selección adversa |

---

## 3. Modelos que navegan bien esta presión

**Principio de diseño que se repite en toda la evidencia**: los modelos **híbridos** (mancomunación
para riesgo catastrófico + mecanismos individuales para riesgo rutinario/moral hazard) superan
tanto a la solidaridad pura como al pricing puramente individualizado.

### Mecanismos con evidencia real

| Mecanismo | Qué resuelve | Evidencia | Peso |
|---|---|---|---|
| Ajuste de riesgo (Países Bajos, competencia gestionada) | Selección adversa | "Uno de los mejores modelos en práctica" pero aún no neutraliza del todo los incentivos de selección (F-96, 🟡) | Medio |
| Mejora continua del ajuste (grupos de costo por diagnóstico, multimorbilidad) | Precisión del ajuste | Campo activo de mejora, no solución estática (F-97, 🟢 peer-reviewed) | Alto |
| Capitación / value-based care (ACOs) | Riesgo moral del proveedor | Reduce costos sin reducir calidad (⚠️ F-98, fuente no verificada con precisión) | Medio (con reserva) |
| Ajuste de riesgo de la ACA | Espiral de la muerte | Comprime diferencias de loss ratio entre aseguradoras, "funcionando como se pretendía" (F-103, 🟡 análisis profesional) | Medio |
| Sistema 3M de Singapur (Medisave+Medishield+Medifund) | Moral hazard + catástrofe + equidad | Cobertura universal combinando ahorro individual (85%) + seguro catastrófico + red focalizada (~10%) (F-102, 🔵 B) | Alto |
| Incentivos conductuales/wellness | Prevención | **Evidencia mixta**: "modesta y a menudo de corta duración" (F-100, 🟢 peer-reviewed independiente) — ver tensión abajo | Medio |

**⚠️ Tensión declarada**: Vitality (la empresa) publicó su propio estudio afirmando resultados
fuertes y sostenidos (F-99, 🔴 autopublicado, conflicto de interés directo) — la ciencia
independiente es más cautelosa (F-100). No se promedia: se presentan en tensión.

### Casos de negocio con resultados publicados

- **Discovery Vitality** (Sudáfrica/global): utilidad operativa de Discovery Insure **+34%**
  (a R546M), atribuida explícitamente al programa Vitality Drive; ROE normalizado 15.4%
  (desde 13.5%) (F-104, 🔵 B, resultados oficiales). Prueba financiera real del mecanismo — aunque
  la atribución causal (¿selección de sanos o cambio de conducta real?) no está resuelta por la
  propia empresa.
- **Kaiser Permanente**: modelo integrado (capitación + provisión en una organización), top 5-10%
  nacional en HEDIS desde 2014 (F-105, 🔵 B). **No es inmune**: en 2025 enfrentó costos crecientes
  igual que el resto del sector — supera a sus pares bajo la misma presión, no la elimina.
- **Oscar Health**: loss ratio médico mejoró de 75.4% (Q1 2025) a 70.5% (Q1 2026) tras "un año de
  reset" con pricing disciplinado (F-106, 🔵 B, filing SEC). Eco directo del caso Babylon Health: la
  tecnología/disrupción sin disciplina actuarial no basta.

---

## 4. La capa de atención primaria específicamente

**Pregunta original**: dentro de la arquitectura de capas (ahorro/rutina, seguro catastrófico, red
de seguridad), ¿existen modelos que cubran bien la atención primaria?

### Mecanismos

| Modelo | Evidencia | Peso |
|---|---|---|
| **Direct Primary Care (DPC)**: cuota mensual fija (USD 50-150) directa al médico | Teóricamente sólido, visitas 30-60min vs. 12-15 tradicional; **poca evidencia peer-reviewed de beneficios, ningún estudio longitudinal** (F-107, F-108, 🟢) | Medio — teoría fuerte, evidencia delgada |
| **Gatekeeping + capitación (China, piloto)** | Consultas primarias **+55.3%**, visitas hospitalarias **-23.9%**, sin aumento de gasto (F-109, 🟢 cuasi-experimental — diseño fuerte) | Alto |
| **Gatekeeping — revisión general** | Reduce especialistas/gasto, **pero con diagnóstico tardío documentado, particularmente cáncer** (F-110, 🟢 revisión sistemática) | Medio — beneficio real con riesgo real |
| **Capitación NHS (UK)** | Modelo híbrido (capitación ajustada por necesidad + bono por desempeño + FFS para extras) en uso real a escala nacional (F-111, 🟢) | Alto |
| **Singapur — policlínicas + CHAS** | ⚠️ Incluso Singapur (el mejor caso de riesgo catastrófico, §3) lucha aquí: su reforma "Healthier SG" tuvo **éxito limitado** — subsidios insuficientes para cambiar práctica de proveedores establecidos (F-112, 🔵 B) | Medio |

**⚠️ Problema estructural del modelo más simple (DPC)**: excluye a quien no puede pagar la
membresía — exactamente lo opuesto de lo que necesita un sistema como el peruano, donde
automedicarse por falta de tiempo/dinero ya es el patrón dominante (ver
[[modelo-salud-ia-farmacias-peru|Modelo de triage IA + farmacias]] §1). Un DPC puro empeoraría el
problema que se busca resolver, salvo que se combine con subsidio (CHAS) o se integre en un
sistema capitado más amplio (NHS).

### Casos de negocio

- **Oak Street Health → CVS, USD 10.6B** (2023): validación estratégica fuerte del modelo de
  atención primaria basada en valor para Medicare. **Pero** (filing SEC oficial): operaba con
  pérdidas, esperando perder >USD 200M en 2023, sin rentabilidad hasta 2025 al menos (F-113,
  F-114). Validación de mercado ≠ rentabilidad actual — confirmado por análisis académico (F-115,
  🟢 peer-reviewed).
- **ChenMed**: 22% menos incidencia de stroke en pacientes >1 año inscritos; mejor desempeño que
  fee-for-service en tamizaje/HbA1c/estatinas; NPS de pacientes 80-90 (⚠️ muy por encima del NPS
  promedio de aseguradoras de 23-35, ver [[seguros-comportamiento-mundo-peru|Comportamiento y
  mercado global de seguros]] §7.2). **Fuente autopublicada, conflicto de interés** (F-116, 🔴,
  mismo patrón que Vitality).

---

## 5. Síntesis transversal (§1-§4)

**Convergencia**: la capitación/valor-por-resultado gana en las capas investigadas
(aseguradoras generales §3, atención primaria específicamente §4) — no es casualidad, es un
principio de diseño transversal. Conecta directamente con §2.4: Kaiser Permanente (§3) es
en esencia el mismo principio de integración vertical que hace rentable a Optum —
capitación + provisión propia en una sola organización, en vez de negocio de seguro puro
separado del negocio de atención/farmacia.

**Divergencia/tensión que no se resuelve artificialmente**: el entusiasmo de negocio (Discovery,
ChenMed) es sistemáticamente más optimista que la evidencia académica independiente sobre el
mismo mecanismo — plausible que el efecto financiero venga más de **selección** (sanos se
autoseleccionan hacia estos productos) que de **cambio de conducta real** a gran escala.

**Para el proyecto**: el PL 08488 peruano (farmacéutico paga con stock del SIS, no membresía
privada) ya está, sin saberlo, más cerca del modelo Singapur/NHS que del modelo DPC
estadounidense — buena señal para el diseño de
[[modelo-salud-ia-farmacias-peru|el modelo de triage IA + farmacias]].

---

## 6. ¿Reduce el gasto médico lo que ocurre *fuera* del consultorio?

> **Pregunta original (2026-09-02)**: ¿existe evidencia de que los planes de cuidado, el cambio de
> hábitos o las intervenciones en otras áreas del bienestar —más allá de lo médico— reduzcan el
> gasto médico o la siniestralidad de las personas a lo largo del tiempo?

**Veredicto corto**: sí existe evidencia, pero es **mucho más débil, más selectiva y más
contradictoria** de lo que asume la industria. Las tres intervenciones más vendidas comercialmente
(wellness corporativo, gestión de casos de alto costo, apps de manejo de crónicos) **fallaron sus
pruebas aleatorizadas**. Las que sí funcionan comparten tres rasgos: focalización por riesgo,
intervención estructurada y **evaluador independiente del vendedor**.

### 6.0 La premisa que ordena todo el capítulo

Antes de mirar caso por caso, hay un resultado que fija el marco: revisando **599 estudios de
costo-efectividad**, menos de ~20% de las medidas preventivas estudiadas **ahorra dinero**, y la
distribución de razones costo-efectividad de la prevención es **estadísticamente similar a la del
tratamiento** (F-483, 🟢A, NEJM). La conclusión correcta no es "la prevención no sirve": es que
**costo-efectivo ≠ ahorrador**. La mayoría de la prevención *compra salud a un precio razonable*,
no gratis. Cualquier caso de negocio que prometa ahorro neto tiene que justificar por qué su
intervención está en ese ~20% — y casi ninguno lo hace.

### 6.1 Wellness corporativo: el caso mejor financiado y peor sustentado

Es el ejemplo más limpio de una cifra que se institucionalizó antes de probarse.

- **La cifra fundacional**: "**US$3,27 de ahorro médico por cada dólar invertido**" (más US$2,73 en
  ausentismo), de un meta-análisis de 2010 (F-472). Los propios autores advirtieron que los
  estudios agregados **carecían de grupo de control robusto**.
- **La refutación, hecha por los mismos autores**: dos RCT grandes e independientes.
  - **Illinois Workplace Wellness Study** (N=4.834, F-469, 🟢A, *QJE*): el programa aumentó de
    forma persistente el **tamizaje**, pero **sin efecto causal significativo en gasto médico
    total**, conductas, productividad ni autorreporte. ⭐ Y explica el espejismo: **en el año
    previo a la intervención** los participantes ya gastaban menos y eran más sanos que los no
    participantes. Lo que los estudios observacionales leen como ahorro es, en buena medida,
    **autoselección de sanos**.
  - **BJ's Wholesale Club** (>32.000 empleados, F-470, 🟢A, *JAMA*): mejoras significativas en
    **conductas autorreportadas** (ejercicio, manejo de peso) y **ninguna** en medidas clínicas,
    gasto, utilización ni ausentismo a 18 meses.
  - **Seguimiento a 3 años** del mismo ensayo (F-471, 🟢A, *Health Affairs*): tampoco aparecen
    efectos. ⭐ Esto **cierra la salida habitual** de la industria ("la prevención necesita
    horizonte largo").
- **El cierre metodológico**: aplicando corrección de sesgo de publicación a la literatura previa,
  el efecto medio corregido es **negativo y no significativo** (p=0,14), y el IC 99% de los RCT
  **excluye** la estimación de 2010 (F-469).

> **Lo que sí produce el wellness**: participación, tamizaje y conducta autorreportada. Eso puede
> tener valor de marca, de retención o de relación — pero **no es un caso de negocio de reducción
> de siniestralidad**, y presentarlo como tal es insostenible frente a esta evidencia.

### 6.2 Gestión de casos y coordinación de cuidados: el mismo nulo, dos décadas seguidas

- **Medicare Coordinated Care Demonstration** (15 programas con asignación aleatoria, F-474, 🟢A,
  *JAMA* 2009): solo **2 de 15** redujeron hospitalizaciones y **ninguno generó ahorro neto** una
  vez contadas las cuotas de gestión.
- **Camden Coalition "hotspotting"** (F-473, 🟢A, *NEJM* 2020), el programa insignia de manejo de
  superutilizadores: readmisión a 180 días de **62,3% (tratamiento) vs. 61,7% (control)**. Sin
  efecto. ⭐ El aporte más útil no es el resultado sino el mecanismo del error: los programas
  dirigidos a pacientes de altísimo gasto exhiben **regresión a la media muy fuerte**, así que un
  análisis antes-después casi siempre "encuentra" un ahorro que el RCT no confirma.
- **El matiz que rescata algo**: un reanálisis posterior del experimento de Medicare halló que
  **4 de 11** programas sí redujeron hospitalizaciones **8-33%** en el subgrupo de **alto riesgo de
  hospitalización inmediata** (F-474). La variable que decide no es el programa, es **a quién se
  aplica**.

### 6.3 Determinantes sociales (comida, vivienda, transporte): la mejor evidencia del lado no médico — y su trampa

Es aquí donde aparecen los números positivos más grandes, y también el hallazgo más incómodo del
barrido.

| Evidencia | Diseño | Resultado |
|---|---|---|
| Comidas médicamente adaptadas, Massachusetts (F-475, 🟢A ⚠️ observacional) | Emparejado, base de reclamos de todos los pagadores, 807 receptores | **−16,4% de gasto médico mensual** (US$3.838 vs. US$4.591), menos hospitalizaciones y admisiones a casa de reposo |
| Programa intensivo de comida como medicina (F-476, 🟢A, **RCT**) | Aleatorizado, ~500 pacientes con diabetes no controlada e inseguridad alimentaria | **Sin efecto significativo en HbA1c**; sí aumentó el uso de servicios preventivos |
| Revisión de ROI de intervenciones sociales (F-478, 🟢A) | Revisión con método de ROI declarado | **+85% de ROI promedio** en inseguridad alimentaria (rango 1% a 287%, un caso en −31%); **+50%** en vivienda (5% a 224%, un caso en −38%) |
| *Healthy Opportunities Pilots*, Carolina del Norte (F-477, 🔵B) | Serie temporal interrumpida comparativa, Medicaid estatal, 2022-2024 | **US$85-164 de ahorro por beneficiario/mes** (la cifra varía entre el análisis académico y el comunicado oficial), menos urgencias y hospitalizaciones |

**⚠️ La tensión que no se resuelve promediando** (misma regla que §3 aplica a Vitality): el mismo
mecanismo —comida como medicina— da **efecto fuerte en diseño observacional (F-475)** y **nulo en
diseño aleatorizado (F-476)**. La diferencia está en el método, no en la intervención. Quien cite
solo el 16% está citando el diseño más débil de los dos.

**⭐ Y el hallazgo más importante de todo este capítulo no es un resultado clínico**: el programa de
Carolina del Norte **demostró ahorro y aun así fue desfinanciado**. La legislatura no renovó
fondos después del 1-jul-2025 y el programa se suspendió (F-477). Es la demostración empírica del
**problema del bolsillo equivocado**: quien paga la intervención (el presupuesto estatal, el
empleador, la aseguradora de este año) **no es quien captura el ahorro** (el sistema hospitalario,
la aseguradora del año siguiente, la sociedad a 10 años). En un mercado con rotación anual de
afiliados, **demostrar ahorro no basta para que el ahorro se pague**.

### 6.4 Lo que sí funciona: incentivos focalizados y programas estructurados por riesgo

Dos contraejemplos sólidos impiden concluir que "nada del lado conductual sirve":

- **Incentivos financieros para dejar de fumar** (F-479, 🟢A, RCT N=2.538, *NEJM*): abstinencia
  sostenida a 6 meses de **9,4%-16,0% vs. 6,0%** con cuidado usual, con superioridad de los
  esquemas de recompensa sostenida a 12 meses. ⭐ Y un hallazgo de diseño conductual directamente
  aplicable: los esquemas de **recompensa** tuvieron **90,0% de aceptación** frente a **13,7%** de
  los de **depósito**, aunque los de depósito eran más efectivos *entre quienes los aceptaban* —
  **efectividad y aceptación se optimizan en direcciones opuestas**.
- **NHS Diabetes Prevention Programme** (F-481, 🟢A, evaluación independiente DIPLOMA): incidencia
  de diabetes tipo 2 **menor donde el programa operaba** (**IRR 0,938; IC95% 0,905-0,972**) y
  evaluado como **altamente probable de ser costo-efectivo**. Es el único programa nacional de
  cambio de hábitos con evidencia positiva e independiente encontrado en este barrido.

**La diferencia con §6.1 no es "prevención sí / prevención no"**, es: **población focalizada por
riesgo medido** (prediabetes confirmada, fumadores activos) + **intervención estructurada con
protocolo** + **evaluación por un tercero que no vende el programa**. Cuando faltan los tres, el
resultado es el nulo del wellness.

### 6.5 La versión digital del mismo error

La evaluación independiente más dura del barrido: las herramientas digitales de manejo de diabetes
producen reducciones de HbA1c **mínimas (0,23-0,60%) y no sostenidas**, sin mejora en peso,
presión ni colesterol, y **aumentan el gasto neto a 3 años** (+US$2.002 comercial, +US$1.011
Medicare, +US$723 Medicaid) — en una categoría que acumula **US$58 mil millones** en inversión y
M&A (F-482, 🔵B, PHTI). ⚠️ Los proveedores evaluados disputaron públicamente el análisis; se
registra la disputa, no se promedia con el hallazgo.

### Regla destilada del §6

> **El ahorro atribuido a intervenciones no médicas casi siempre se evapora cuando el diseño pasa
> de observacional a aleatorizado.** Antes de creer una cifra de ROI de bienestar, preguntar tres
> cosas: (1) ¿hubo grupo de control asignado al azar? (2) ¿quién midió — el vendedor o un tercero?
> (3) ¿los participantes ya eran distintos *antes* de entrar? Si las tres no tienen buena
> respuesta, la cifra mide selección, no efecto.

---

## 7. Desde lo médico: cómo se hace más costo-eficiente el gasto en tratamiento

> **Pregunta original (2026-09-02)**: desde lo médico, ¿cómo podemos hacer más costo-eficiente el
> gasto en tratamientos? ¿qué evidencias o ejemplos exitosos hay?

**Veredicto corto, y es contraintuitivo**: las reducciones de costo mejor probadas **no vienen de
cambiar lo que se le hace al paciente, sino de cambiar el precio que se paga, el lugar donde se
hace y quién lo hace**. Las palancas de precio/sitio producen efectos de dos dígitos; las de
modelo de pago, de un dígito bajo; las de cambiar la conducta clínica, las más difíciles de todas.

### 7.1 Precio y sitio de atención — la palanca de mayor efecto probado

- **Reference pricing (CalPERS)** — el mecanismo mejor documentado de todo el barrido (F-484, 🟢A).
  El comprador fija un precio de referencia (US$30.000 para reemplazo de rodilla/cadera; US$1.500
  colonoscopía; US$2.000 cataratas; US$6.000 artroscopia) y el afiliado paga la diferencia si
  elige un proveedor por encima. Resultado: **los proveedores caros bajaron sus precios 34%**, con
  ahorros de US$2,8M (articular), US$1,3M (cataratas), US$2,3M (artroscopia) y US$7M
  (colonoscopía), **sin evidencia de daño clínico**. La razón por la que funciona: el precio de un
  mismo procedimiento variaba **hasta 5x entre hospitales sin relación con la calidad**.
- **Traslado de sitio de atención** (infusión y especializados del hospital al consultorio,
  centro ambulatorio o domicilio): ahorros reportados de **US$16.000 a US$37.000 por paciente/año**
  y 40-60% en infusión domiciliaria, con dos tercios de los planes ya operando programas de este
  tipo (F-489). ⚠️ **Registrado con descuento explícito**: las cifras provienen de actores con
  interés comercial directo (aseguradora/PBM y proveedores de infusión), sin evaluación
  independiente localizada. El mecanismo es coherente con F-484; la magnitud, no verificada.
- **Biosimilares y genéricos** — el ahorro estructuralmente mayor de la farmacia, y **el caso más
  claro de un ahorro bloqueado por el modelo de negocio de quien debería aplicarlo**: los
  biosimilares de adalimumab tienen precios **5% a 87% menores** y hasta **US$6.000 millones** de
  ahorro potencial, **no realizado** — la cuota de mercado se mantuvo bajo 2% en el primer período.
  La razón alegada es de incentivos: el cambio implicaría una caída estimada de **84% en la
  utilidad del PBM** sobre esa molécula, y las farmacias especializadas que dispensan la marca
  **comparten dueño con los PBM** (F-490). ⭐ Conecta directo con §2.4: **la integración vertical
  que hace rentable al sector es la misma que frena su mecanismo de ahorro mejor probado.**

### 7.2 Modelos de pago: efecto real, magnitud de un dígito bajo

- **Pago por episodio (bundled payments)** — evaluación con **aleatorización a nivel de área
  metropolitana** por diseño del propio programa CJR de Medicare (F-485, 🟢A, *NEJM*): **US$812 de
  ahorro por episodio (−3,1%)**, vía **menos enfermería especializada post-alta**, **sin aumento
  de complicaciones**.
- **ACOs / Medicare Shared Savings Program**, año 2024 (F-486, 🔵B, CMS): **US$2.400 millones de
  ahorro neto**, el mayor desde el inicio del programa, con **75% de 476 ACOs** ganando pagos por
  desempeño. ⚠️ Contra el gasto asignado de 10,3 millones de beneficiarios, eso es del orden de
  **1-2%**.

> **Lectura conjunta**: los cambios de modelo de pago funcionan de verdad, y su efecto honesto es
> **1-3%**, no los dos dígitos que promete la narrativa del *value-based care*. Es una mejora
> estructural sostenida, no un salto.

### 7.3 Dejar de hacer lo que no sirve (low-value care)

Las intervenciones basadas en **Choosing Wisely** sí cambian la práctica, pero solo cuando son
**multicomponente y dirigidas al clínico**; la sola difusión de recomendaciones no basta y los
servicios de bajo valor siguen siendo prevalentes una década después, con certeza de la evidencia
calificada como **baja a muy baja** en varios análisis (F-487, 🟢A). ⭐ Lección operativa:
**de-implementar es más difícil que implementar** — no ocurre por información, ocurre por rediseño
del flujo de trabajo y de los incentivos.

### 7.4 Cambiar el lugar: hospital en casa

Menor **mortalidad intrahospitalaria** y menor uso de urgencias a 30 días, estancia más corta y
**costo total menor** (19-30% según Johns Hopkins; CMS halla menor gasto post-alta en más de la
mitad de los 25 principales MS-DRG) (F-488). ⚠️ La readmisión a 30 días **no mejora de forma
consistente**, y el modelo depende de un **waiver regulatorio renovable**: su riesgo principal no
es clínico, es de política de pago.

### 7.5 Cambiar quién hace la tarea — la palanca más transferible al Perú

- **Kaiser Permanente Norte de California, hipertensión** (F-480, 🟢A): control de **44% a 90% en
  13 años**, mientras la media nacional pasaba de 55,4% a 64,1%. Los componentes son
  **organizativos, no motivacionales**: registro de hipertensos, métricas compartidas, guía única,
  **visitas de toma de presión con asistente médico (sin médico)** y **combinación en una sola
  píldora**. ⭐ Es el mejor caso documentado de que la mejora clínica a escala llega por **rediseño
  de proceso**, no por educar al paciente.
- **Agentes comunitarios de salud (CHW) en países de ingreso bajo y medio** (F-505, 🟢A,
  revisiones sistemáticas con mayoría de ensayos aleatorizados por conglomerados): mejoras en
  reducción de presión arterial, vinculación al cuidado y adherencia, con costo-efectividad
  generalmente favorable — en **Argentina**, ICER de **US$3.299 por AVAC** (US$26 por mmHg de
  reducción sistólica). ⚠️ Los autores advierten que la heterogeneidad de contextos impide una
  conclusión única fuerte.

### 7.6 Diseño de beneficio y el frente caro del momento

- **Value-Based Insurance Design (V-BID)** (F-492, 🟢A): bajar o eliminar el copago de
  medicamentos de alto valor **mejora la adherencia de forma inmediata y sostenida** (+2,8% en
  estatinas, mantenido en años siguientes) y **compensa la caída de adherencia** al migrar a
  planes con deducible, **sin aumentar el gasto total del plan**. ⚠️ Promesa correcta: mejora
  adherencia sin costo extra; **solo en algunos casos** reduce el gasto médico total.
- **GLP-1** — F-483 ocurriendo en tiempo real (F-491, 🔵B/🟡C): el costo de farmacia por
  miembro/mes pasó de **US$4,34 (2022) a más de US$27 (1T 2025)**; ampliar cobertura sube la prima
  del empleador **6% a ~14% anual**; solo **37% de los empleadores autofinanciados** la ofrecen
  para obesidad y **1 de cada 7 que la ofrece considera retirarla**. Todos los estudios coinciden:
  **al precio comercial actual aumentan el gasto total de corto plazo**, aunque reduzcan el costo
  médico del usuario (~US$560/año). **Efectivo, plausiblemente costo-efectivo, no ahorrador.**

### Tabla ordenada por magnitud del efecto verificado

| Palanca | Efecto medido | Calidad del diseño | Nota |
|---|---|---|---|
| Reference pricing (F-484) | **−34% en el precio del proveedor** | 🟢 Alta — programa real, datos del comprador | El efecto más grande y mejor probado |
| Biosimilares (F-490) | **−5% a −87% de precio**, hasta US$6.000M | 🟡 Media — dato de industria | ⚠️ Ahorro **no realizado** por conflicto de incentivos del PBM |
| Sitio de atención (F-489) | US$16.000-37.000/paciente/año | 🟠 Baja — fuente interesada | Mecanismo plausible, magnitud no verificada |
| Hospital en casa (F-488) | −19% a −30% de costo + menor mortalidad | 🔵/🟢 Sólida | Depende de waiver regulatorio |
| Rediseño de proceso clínico (F-480) | Control de HTA 44%→90% | 🟢 Alta | Efecto clínico enorme; ahorro no aislado |
| CHW en recursos limitados (F-505) | ICER US$3.299/AVAC | 🟢 Alta | Costo-efectivo, no necesariamente ahorrador |
| Pago por episodio (F-485) | **−3,1%** (US$812/episodio) | 🟢 Alta — aleatorizado por área | Sin daño clínico |
| ACOs / MSSP (F-486) | **~1-2%** neto | 🔵 Sólida — regulador | Ahorro real y sostenido, pero pequeño |
| V-BID (F-492) | +adherencia, gasto total neutro | 🟢 Alta | No prometer ahorro |
| Choosing Wisely / de-implementación (F-487) | Variable, certeza baja | 🟢 Alta (revisiones) ⚠️ evidencia primaria débil | Solo funciona multicomponente |
| GLP-1 al precio actual (F-491) | **+6% a +14% de prima** | 🔵 Sólida | Aumenta gasto de corto plazo |

---

## 8. ¿Qué modelos ganan dinero, cuáles mejoran la salud, y cuáles ambas cosas?

> **Preguntas originales (2026-09-02)**: ¿qué modelos de negocio de salud —servicios o seguros— son
> los más exitosos financieramente en el mundo? ¿cuáles mejoran realmente la salud de sus
> asegurados o pacientes? ¿cuáles ambas?

La matriz cruza **rentabilidad verificada** (filings, resultados oficiales) contra **mejora de
salud demostrada** (evidencia independiente, no autorreportada). El criterio de "demostrada" es
deliberadamente duro: un caso solo entra si la evidencia clínica **no proviene exclusivamente de
quien vende el modelo**.

### 8.1 Ganan dinero y hay evidencia de salud (el cuadrante escaso)

| Modelo | Prueba financiera | Prueba de salud | Descuento obligatorio |
|---|---|---|---|
| **Kaiser Permanente** (integrado: asegura y atiende) | Ingresos US$127.700M, utilidad operativa US$1.400M = **margen 1,1%**, neto US$9.300M (F-496) | Top 5-10% nacional en HEDIS desde 2014 (F-105); control de hipertensión 44%→90% con evidencia peer-reviewed (F-480) | ⭐ **El sistema con mejor evidencia clínica sostenida opera con ~1% de margen**: es viable, no lucrativo |
| **Narayana Health** (India, alto volumen / bajo costo) | Ingresos ₹78.960M (+44%), **EBITDA 21,7%**, utilidad ₹8.105M (F-498) — margen que ninguna aseguradora de EE.UU. o Europa alcanza | 16.500+ cirugías cardíacas/año; mortalidad a 30 días post-alta 3,2%→0,9% (F-498) | ⚠️ Los datos clínicos son **autorreportados en presentación a inversionistas**, no peer-reviewed; y el +44% sugiere efecto de consolidación |
| **Aravind Eye Care** (India, subsidio cruzado) | Autosostenible sin donación para su operación núcleo; utilización de recursos 80% vs. ~25% del referente global (F-499) | **70% de servicios gratis o subsidiados sin segmentar la calidad clínica** — la diferencia entre pagante y no pagante está en el lente y la comodidad, no en el procedimiento (F-499) | 🟡 Sin estados financieros auditados públicos; cifras de costo unitario de épocas distintas |
| **Hospital en casa** (modelo de entrega, no empresa) | −19% a −30% de costo (F-488) | Menor mortalidad intrahospitalaria y menos urgencias (F-488) | Depende de un waiver regulatorio renovable |

### 8.2 Ganan mucho dinero, sin evidencia de que mejoren la salud

| Modelo | Prueba financiera | Estado de la evidencia de salud |
|---|---|---|
| **PBM / integración vertical de farmacia** (Optum Rx y pares) | **US$1.500M de utilidad operativa en un trimestre** sobre US$38.300M de ingresos (F-198, filing SEC); 3 PBMs procesan 80% de las recetas de EE.UU. (F-199) | **Ninguna**. Y hay evidencia de lo contrario: sus incentivos **bloquean** la adopción de biosimilares que ahorrarían hasta US$6.000M (F-490) |
| **Medicare Advantage** | El motor de crecimiento del sector durante una década | ⭐ **US$84.000 millones de sobrepago en 2025** (~20% más que Medicare tradicional): **US$40.000M por intensidad de codificación** y **US$44.000M por selección favorable** (F-493, MedPAC). En calidad, MA muestra más prevención y menos hospitalizaciones, pero **sin ventaja consistente en mortalidad, readmisiones, experiencia ni disparidades** (F-494) → **calidad equivalente, no superior** |
| **Manejo digital de crónicos** (categoría) | US$58 mil millones en inversión y M&A (F-482) | **Negativa**: HbA1c mínima y no sostenida, y **aumenta el gasto neto a 3 años** (F-482) |
| **Discovery / Vitality** (caso intermedio) | Utilidad operativa normalizada de Vitality **+70% a R3.205M** (FY jun-2025) y **+41% a R2.120M** (semestre a dic-2025); 10,4M de vidas fuera de China (F-497) | ⚠️ **La atribución sigue sin resolverse** (misma advertencia que §3): la evidencia independiente sobre incentivos de bienestar es "modesta y a menudo de corta duración" (F-100), mientras la empresa reporta resultados fuertes (F-99). Crecer y ganar con un programa de conducta **no prueba** que el programa cambie la conducta |

### 8.3 Mejoran la salud y no logran ganar dinero (todavía)

| Modelo | Prueba de salud | Realidad financiera |
|---|---|---|
| **Atención primaria capitada para adultos mayores** (Oak Street, ChenMed, CareMore) | CareMore: **42% menos admisiones** y amputaciones en diabéticos 60% menores (F-504); ChenMed: 22% menos incidencia de stroke (F-116) ⚠️ ambos **sin control por selección** | ⭐ **CVS registró un deterioro de plusvalía de US$5.700 millones** sobre su unidad de entrega de atención y anunció cierre de sedes de Oak Street (F-502) — la confirmación auditada de la advertencia que el node ya hacía en §4 |
| **Servicios sociales pagados por el sistema de salud** | Menos urgencias y hospitalizaciones, US$85-164 de ahorro por beneficiario/mes (F-477) | **Desfinanciado y suspendido** en jul-2025 pese a haber demostrado ahorro (F-477) |
| **Insurtechs de salud** | — | Trayectorias opuestas con el mismo modelo: **Bright Health salió del negocio asegurador**; **Clover** alcanzó EBITDA ajustado positivo en 2025 y guía a su primera utilidad neta GAAP en 2026; **Devoted** sigue con pérdidas (F-503) |

### 8.4 El correctivo temporal: ni siquiera el ganador estructural gana siempre

La v1.1-v1.2 de este node concluyó que el sector es rentable con margen fino y que la utilidad real
está en los negocios adyacentes integrados (§2). El ciclo 2025 **confirma la segunda mitad y pone
a prueba la primera**: UnitedHealth Group registró ingresos récord de **US$447.600 millones** pero
utilidad de **US$12.100M (bajando desde US$14.400M)**, con **MLR anual de 89,1% y 92,4% en el 4T**
—el más alto en ocho años— y la utilidad operativa de **UnitedHealthcare, el negocio asegurador,
cayendo ~40%** (de US$15.600M a US$9.400M). Su guía 2026 asume **3,2% de margen operativo** y la
**pérdida de 1,3-1,4 millones de afiliados de Medicare Advantage** por salir de mercados no
rentables (F-495).

⭐ **Lectura estructural**: el negocio de *seguro puro* se comprimió mientras el grupo siguió siendo
rentable. Es exactamente la tesis de §2.4, ahora demostrada con el ciclo a la baja.

### 8.5 La prueba latinoamericana de la integración vertical, y sale mixta

Si el hallazgo global es "integrar verticalmente es donde está la utilidad", el caso más grande de
la región lo matiza: **Hapvida NotreDame Intermédica** (Brasil) cerró 2025 con sinistralidade caja
acumulada de **75,3%**, pero descompuesta revela **72,0% en la operación original Hapvida**
(Norte/Nordeste, verticalizada de larga data) contra **78,4% en NotreDame** (Sur/Sudeste), nivel
**cercano al de competidores sin verticalización relevante** (F-501). ⭐ Es decir: **la ventaja de
la verticalización no se reprodujo al trasplantarla** a otra región y otra base de clientes. La
respuesta de la empresa fue la mayor inversión de su historia (R$2.000 millones para 10 hospitales
propios hacia 2026). **Referencia obligada para cualquier tesis de "hacer un Kaiser" en
Latinoamérica.**

El contraste asiático apunta a un uso distinto de lo mismo: **Ping An Good Doctor** reportó
ingresos de RMB 5.470M (+13,7%) y utilidad atribuible de RMB 379,5M (+366,1%), con ~12 millones de
usuarios anuales de su "AI Doctor" y el modelo **"IA + médico humano"** cubriendo al 100% de los
clientes minoristas del grupo (F-500). ⚠️ Pero la utilidad propia (~US$52M) es pequeña frente al
grupo: **el valor declarado del servicio médico es habilitar la venta de seguros** (la prima de
primer año por póliza de clientes de salud subió 1,5x). Es integración vertical usada como
**herramienta de distribución**, no como centro de utilidad.

---

## 9. Síntesis v2.0: seis reglas que ordenan las cuatro preguntas

1. **Costo-efectivo ≠ ahorrador.** Menos del ~20% de las medidas preventivas ahorra dinero
   (F-483). La mayoría compra salud a precio razonable. Un caso de negocio de prevención que
   promete ahorro neto debe demostrar por qué está en ese 20%.
2. **El ahorro no médico se evapora al aleatorizar.** Wellness corporativo (F-469 a F-472),
   hotspotting (F-473), coordinación de cuidados (F-474) y comida como medicina (F-475 vs. F-476)
   dan resultados fuertes en diseño observacional y nulos en RCT. El mecanismo del espejismo tiene
   nombre: **autoselección de sanos** y **regresión a la media**.
3. **Lo que sí funciona del lado conductual comparte tres rasgos**: focalización por riesgo medido,
   intervención estructurada y **evaluador independiente del vendedor** (F-479, F-481, F-505). Sin
   los tres, el resultado esperable es el nulo.
4. **La costo-eficiencia médica probada viene del precio, del sitio y de quién hace la tarea — no
   de cambiar al paciente.** Reference pricing baja precios 34% (F-484); los biosimilares tienen
   87% de diferencia de precio (F-490); mover el sitio de atención mueve decenas de miles de
   dólares (F-489); sacar la toma de presión del médico llevó el control de hipertensión de 44% a
   90% (F-480). Los cambios de modelo de pago son reales pero de **1-3%** (F-485, F-486).
5. **La rentabilidad máxima del sector y la mejora de salud están, hoy, en cuadrantes distintos.**
   Lo más rentable —PBM integrado (F-198), Medicare Advantage (F-493)— no tiene evidencia de
   mejorar la salud, y en el caso del PBM **bloquea activamente** un ahorro probado (F-490). Lo
   que mejor mejora la salud —Kaiser (F-496), atención primaria capitada (F-502, F-504)— opera al
   1% de margen o directamente pierde dinero. **El cuadrante de "ambas" existe pero es escaso**, y
   sus mejores casos están fuera de EE.UU. y Europa: **Narayana y Aravind** (F-498, F-499).
6. **⭐ Demostrar ahorro no basta: hay que capturarlo.** El programa de Carolina del Norte demostró
   ahorro y fue desfinanciado (F-477); los biosimilares tienen el ahorro probado y no se adoptan
   (F-490); Oak Street mejora resultados y generó un deterioro de US$5.700M (F-502). **El problema
   del bolsillo equivocado —quien paga la intervención no es quien captura el ahorro— explica más
   fracasos que la falta de eficacia clínica.** Con rotación anual de afiliados, la prevención
   financia a la aseguradora del año siguiente.

### 9.1 Qué significa esto para el proyecto (Perú)

- **Para el diseño del modelo de triage IA + farmacias** (ver
  [[modelo-salud-ia-farmacias-peru|ese node]]): la evidencia más transferible no es la del wellness
  digital —que fracasó su evaluación independiente (F-482)— sino la de **task-shifting**: KPNC
  (F-480) y CHW en países de ingreso bajo y medio (F-505, ICER US$3.299/AVAC en Argentina). El
  mecanismo probado es **sacar la tarea rutinaria del médico y estandarizarla**, que es
  precisamente la lógica del PL 08488.
- **Para cualquier caso de negocio de prevención dirigido a una aseguradora peruana**: la pregunta
  que decide no es "¿mejora la salud?" sino **"¿quién captura el ahorro y en qué plazo?"** (regla
  6). Un programa cuyo retorno aparece al año 5 no es financiable por un contrato que se repacta
  cada año.
- **⚠️ El hueco de dato peruano sigue abierto, ahora doblemente verificado.** APESEG reporta ~S/
  9.500 millones en siniestros del sector durante 2025 y una densidad de ~US$203 de prima per
  cápita (F-506), pero **no existe cifra pública de siniestralidad ni de margen del ramo salud/EPS
  peruano** — ni en SUSALUD, ni en APESEG, ni en gremios. Es la segunda búsqueda dedicada que
  confirma la ausencia (la primera, en la v1.2, §2.6). Se declara el hallazgo negativo en vez de
  forzar una fuente débil.

---

## 10. Cuidado integral, modelo de Porter y autoatención digital: ¿dónde está el retorno?

> **Preguntas originales (2026-09-03)**: siendo una aseguradora, ¿apostar por un programa de cuidado
> integral no trae retorno, no hay evidencia? ¿Qué pasa con el modelo de Porter? ¿La atención y
> autoatención digital muestra evidencia de impacto en salud y negocio a largo plazo? ¿Qué sí
> muestra impacto en salud, siniestralidad y negocio asegurador?

### 10.0 La corrección al §6: la pregunta estaba mal planteada

El §6 concluyó que el ahorro de las intervenciones no médicas se evapora al aleatorizar. Eso **no
es lo mismo** que decir que el cuidado integral no rinde. La lectura correcta de toda la evidencia
reunida es más precisa y más útil:

> **Lo que no tiene retorno probado es el *programa añadido*** —un beneficio de bienestar, un
> coaching, una app, un equipo de gestión de casos que se cuelga encima de un seguro que sigue
> operando igual—. **Lo que sí tiene retorno probado es el *rediseño del modelo de atención*
> acompañado de un cambio en quién asume el riesgo.** No es la misma apuesta, y la evidencia las
> separa con claridad.

Los cuatro fracasos del §6 (wellness, hotspotting, coordinación de cuidados, comida como medicina)
comparten una anatomía: **programa superpuesto, población no estratificada, sin cambio en el
contrato de riesgo**. Los éxitos de este §10 comparten la opuesta.

### 10.1 El modelo de Porter (VBHC): diagnóstico sólido, implementación sin ROI demostrado

**Qué prueba tiene el modelo como tal**: notablemente poca, y hay que decirlo con precisión porque
es un marco que se cita como si estuviera probado. Las revisiones de alcance de su implementación
encuentran tres cosas (F-507, 🟢A):

1. **"La agenda de valor articula la meta y el contenido, pero no da ninguna estrategia de
   implementación"** — es un marco de gestión, no una intervención con tamaño de efecto.
2. **Sesgo de publicación positivo declarado por los propios revisores**: la literatura tiende a
   reportar solo casos exitosos, lo que impidió capturar los intentos fallidos reales.
3. Los estudios miden **indicadores de proceso**, no resultados clínicos finales, mortalidad ni
   PROMs.

⭐ Conclusión honesta: **el modelo de Porter no ha sido falsado, pero tampoco probado.** No existe
para "implementar VBHC" una cifra comparable al −34% del reference pricing (F-484) o al −3,1% del
pago por episodio (F-485). Quien lo proponga como caso de negocio con retorno cuantificado está
extrapolando.

**El caso de éxito canónico y lo que realmente demuestra.** Martini-Klinik (Hamburgo) mide
sistemáticamente incontinencia, disfunción eréctil, irritación intestinal y complicaciones, y
**supera de forma consistente el promedio nacional alemán** (F-509). Pero el mecanismo que la
evidencia sostiene no es "adoptó VBHC": es **concentración de volumen en una sola patología +
medición sistemática de resultados + retroalimentación al cirujano + técnica quirúrgica propia**.
⭐ Es el mismo mecanismo de rediseño de proceso que llevó el control de hipertensión de KPNC de 44%
a 90% (F-480) — no una transformación de gestión corporativa.

**El fracaso canónico, y el contraste que lo explica.** En **Karolinska**, la implementación fue
**liderada por consultores (BCG, contrato de 4 años)**, comunicada como algo nuevo con argumentos
tomados directamente de Porter y Teisberg; la evaluación interna del directorio registró
facturación de consultores, conflictos de interés y **VBHC estancado**. En **Uppsala**, el mismo
modelo se lideró internamente y la consultora estuvo involucrada **4 meses** (F-508, 🟢A, tesis
doctoral del Karolinska Institutet). El hallazgo transferible: las organizaciones que fracasaron
**nunca definieron conceptualmente qué era VBHC** y terminaron etiquetando como tal prácticas de
gestión sin relación con la agenda de valor.

> **Veredicto sobre Porter**: su diagnóstico —medir resultados que importan al paciente por unidad
> de costo a lo largo del ciclo completo de atención, y organizar la atención en unidades
> integradas por condición— es **conceptualmente sólido y coherente con toda la evidencia dura de
> este node**. Pero es **infraestructura, no programa**: habilita las palancas que sí tienen
> efecto medido (concentrar volumen, medir y retroalimentar, integrar el ciclo), no las
> reemplaza. Presupuestarlo como "transformación VBHC" con ROI proyectado es exactamente lo que
> falló en Karolinska.

### 10.2 Cuidado integral: sí hay retorno, y la condición es contractual, no clínica

| Caso | Diseño | Resultado | Qué lo hace funcionar |
|---|---|---|---|
| **Gesundes Kinzigtal** (Alemania) (F-510, 🟢A) | Poblacional con **grupo de control** (~32.000 miembros vs. 13 regiones comparables y ~300.000 asegurados AOK); único sistema poblacional alemán con evaluación externa rigurosa | Reducción del costo comparativo de la región desde el inicio del programa; modelo Triple Aim | ⭐ **Contrato de ahorro compartido de base poblacional**: el operador cobra una parte del ahorro que genera contra el gasto esperado. **La estructura del contrato resuelve el problema del bolsillo equivocado** |
| **Nuka System of Care** (Alaska) (F-511, 🟡C) | Autorreportado, sin control | Urgencias −40 a −50%, admisiones −53%, días de hospitalización −36%, especialidad −65%; percentil 75-90 en HEDIS; 2 premios Baldrige | Acceso el mismo día, equipos con relación continua, **propiedad comunitaria del sistema**. ⚠️ Magnitud no verificable: es antes-después, justo el diseño contra el que advierte F-473 |
| **Modelo Alzira / Ribera Salud** (España) (F-520, 🟢A) | Concesión capitada a 15 años por ~250.000 habitantes, incluida la construcción | Costo per cápita ~25% menor según sus defensores; ⚠️ la literatura documenta **la brecha entre la retórica de éxito y la realidad financiera** | ⭐ **Terminó revertido a provisión pública en abril de 2018**: el riesgo dominante de un contrato integral a 15 años no es actuarial, es de **continuidad institucional** (mismo patrón que F-477) |

**Y la evidencia que dice qué piezas producen el efecto** (F-519, 🟢A, meta-análisis + revisión de
186 revisiones sistemáticas): el resultado no lo produce "el programa integral" como bloque, sino
componentes identificables — **liderazgo del médico de atención primaria**, **atención
especializada liderada por enfermería dentro de la atención primaria** con vínculo formal al nivel
secundario, **soporte al automanejo**, **estratificación de riesgo** y **coordinación entre
servicios**.

⭐ Ese conjunto de piezas es exactamente el que explica KPNC (F-480), Kinzigtal (F-510) y Nuka
(F-511) — y **el que faltaba** en los programas de coordinación de cuidados que fracasaron
(F-473, F-474). La diferencia entre el éxito y el nulo no fue el entusiasmo ni el presupuesto:
fue la estratificación de riesgo y quién lideraba.

### 10.3 Atención y autoatención digital: la línea divisoria más útil de todo el node

La mejor evidencia disponible es la serie de evaluaciones del **Peterson Health Technology
Institute**, porque es el **mismo evaluador independiente con el mismo método** aplicado a
categorías distintas — lo que descarta que el marco esté sesgado contra lo digital:

| Categoría | Efecto clínico | Efecto económico |
|---|---|---|
| Manejo digital de **diabetes** (F-482) | HbA1c −0,23 a −0,60%, **no sostenida**; nada en peso, presión ni colesterol | **Aumenta el gasto neto a 3 años** (+US$2.002 comercial) |
| Digital de **hipertensión — manejo de medicación** (F-512) | **Baja la presión de forma significativa** | Sube el gasto en el corto plazo y **recupera el costo con ahorro neto de largo plazo** por menor riesgo cardiovascular |
| Digital de **hipertensión — cambio de conducta** (Teladoc, Omada, DarioHealth, Hello Heart, Lark) (F-512) | **Poco o ningún efecto** sobre presión sistólica vs. cuidado usual | Sube el gasto, sin compensación |
| Virtual **musculoesquelético** (F-513) | **Mejora dolor y estado funcional** | — |

> **⭐ La línea divisoria no es digital vs. presencial. Es si la herramienta cierra el ciclo con una
> decisión clínica o solo entrega retroalimentación al paciente.** Lo que ajusta la terapia
> funciona; lo que informa, motiva y acompaña, no.

La evidencia aleatorizada lo confirma desde el otro lado: en **TASMINH4** (F-515, 🟢A, ECA en 142
consultorios del Reino Unido), el automonitoreo de presión —con o sin telemonitoreo— **usado por
el médico para titular la medicación** produce presión significativamente menor que la titulación
guiada por lecturas de consultorio. El paciente mide, pero **el efecto viene de que el dato entra
en una decisión de prescripción**.

**Sobre el largo plazo, que es lo que se preguntó**: no existe evidencia de impacto sostenido en
siniestralidad de la autoatención digital genérica. Lo que sí hay:

- **Telesalud**: ahorra por **sustitución de visita y costo de traslado**, no por menor morbilidad
  — y solo si sustituye en vez de sumarse (el hallazgo central del taskforce es que **sustituyó y
  no aumentó el número total de visitas**) (F-517). ⭐ Es una palanca de **eficiencia operativa,
  no de siniestralidad de largo plazo**. Y casi toda su evidencia es del período COVID, con el
  efecto de la pandemia confundido con el de la tecnología.
- **El registro de negocio es peor que el clínico**: Teladoc acumula **US$14.200 millones en
  deterioros de plusvalía** al cierre de 2024 y una **pérdida neta de US$1.000 millones ese año**
  (F-514, filing SEC) — la empresa que compró Livongo por ~US$18.500M, la adquisición insignia de
  la tesis "digital + crónicos = ahorro", la misma que F-482 no halló respaldada.

### 10.4 Entonces, ¿qué sí mueve la siniestralidad? El arsenal ordenado

Esta es la respuesta directa a la tercera pregunta. Ordenado por **efecto verificado**, con la
columna que la industria suele omitir: **quién captura el ahorro y en cuánto tiempo**.

| Palanca | Efecto medido | Evidencia | Quién captura | Horizonte |
|---|---|---|---|---|
| **Diseño de red** (red limitada / niveles) | Quienes migran gastan **~40% menos**; US$761/afiliado; primas **−16%** con red angosta doble | 🟢 A — cuasi-experimento con incentivo exógeno (F-516) | **El asegurador, de inmediato** | Inmediato |
| **Reference pricing** | Proveedores caros bajan precio **−34%** | 🟢 A (F-484) | El comprador/asegurador | 1-2 años |
| **Sitio de atención** | US$16-37 mil por paciente/año | 🟠 D — fuente interesada (F-489) | El pagador | Inmediato |
| **Biosimilares/genéricos** | −5% a −87% de precio | 🟡 C (F-490) | ⚠️ Hoy lo captura el PBM, **que por eso lo frena** | Inmediato |
| **Centros de excelencia + segunda opinión** | Mecanismo: la cirugía que no se hace | 🟠 D — autorreportado (F-521) | El pagador | 1-2 años |
| **Manejo de medicación (incl. digital con titulación)** | Baja presión; recupera costo con ahorro neto | 🔵 B / 🟢 A (F-512, F-515, F-480) | El pagador **si retiene al afiliado** | 3-10 años |
| **Cuidado integral con riesgo compartido y estratificación** | Costo comparativo menor con grupo de control | 🟢 A (F-510); componentes en F-519 | ⭐ **Solo si el contrato lo asigna** | 3-5 años |
| **Pago por episodio / capitación** | −3,1% por episodio; ACOs ~1-2% | 🟢 A / 🔵 B (F-485, F-486) | El pagador | 1-3 años |
| **Autorización previa / gestión de utilización** | Reduce utilización | 🟢 A ⚠️ **con daño documentado** (F-518) | El asegurador | Inmediato |
| Wellness genérico, coaching digital, gestión de casos sin estratificar | **Sin efecto** en gasto | 🟢 A — RCT (F-469 a F-474, F-482) | — | — |

**⚠️ La advertencia sobre la palanca más tentadora.** La autorización previa **sí baja
utilización**, pero la revisión sistemática de sus efectos adversos documenta **exacerbación de
enfermedad, hospitalización prevenible, estancia prolongada y menor supervivencia libre de
enfermedad**; la auditoría oficial del OIG halló que **13% de las denegaciones revisadas de
Medicare Advantage sí cumplían las reglas de cobertura** y que **80,7% de las denegaciones
apeladas se revirtieron**; y al menos un estudio encuentra que **el costo administrativo superó
el ahorro** (F-518). Es la palanca que traslada el costo al paciente y al prestador — y hoy es el
principal foco regulatorio y reputacional del sector.

### 10.5 Tres reglas nuevas (7, 8 y 9), que se suman a las seis del §9

7. **El retorno no está en el programa: está en el contrato.** El mismo cuidado integral rinde en
   Kinzigtal (ahorro compartido de base poblacional, F-510) y no rinde como programa superpuesto
   (F-473, F-474). Antes de diseñar el programa, definir **quién asume el riesgo, quién cobra el
   ahorro y en qué plazo**. Si el afiliado rota anualmente, el retorno de un programa a 5 años lo
   cobra otro.
8. **Digital que decide vs. digital que informa.** La herramienta que **cierra el ciclo con una
   decisión clínica** (titular medicación) mejora salud y recupera su costo (F-512, F-515); la que
   entrega retroalimentación, coaching o autogestión al paciente **no muestra efecto y aumenta el
   gasto** (F-482, F-512). Es la pregunta de diseño número uno de cualquier producto digital de
   salud.
9. **Medir resultados es condición necesaria, no suficiente — y es infraestructura, no programa.**
   El modelo de Porter no tiene ROI demostrado (F-507) y su fracaso mejor documentado fue una
   transformación liderada por consultores (F-508); su éxito canónico es, en el fondo, volumen
   concentrado más medición sistemática con retroalimentación (F-509). Medir habilita las palancas
   que sí funcionan; no las sustituye.

### 10.6 Lectura para una aseguradora peruana

- **Sí apostar** por rediseño de red y de precio (F-516, F-484): es el efecto más grande, el más
  rápido y el que la propia aseguradora captura — y en un mercado con dispersión de precios sin
  relación con calidad, es donde más margen hay.
- **Sí apostar** por cuidado integral **solo si se puede estructurar el riesgo**: capitación,
  ahorro compartido o integración vertical con estratificación por riesgo y liderazgo de atención
  primaria (F-510, F-519). Sin eso, es gasto añadido.
- **Sí apostar** por lo digital **que toca la decisión clínica** — triage que deriva, herramientas
  que ajustan terapia, automonitoreo que alimenta una prescripción (F-512, F-515). Es exactamente
  la lógica del modelo de triage IA + farmacias de este proyecto: el valor no está en la app, está
  en que **cambia qué se hace después**.
- **No apostar** por wellness genérico, coaching digital de conducta ni gestión de casos sin
  estratificación de riesgo: cinco RCT independientes dicen que no mueve el gasto (F-469 a F-474,
  F-482).
- **⚠️ Y no usar la autorización previa como palanca principal**: baja utilización, tiene daño
  clínico documentado y es hoy el mayor riesgo regulatorio y reputacional del ramo (F-518) — un
  riesgo que en el mercado peruano, con ~48% de desconfianza declarada
  (ver [[seguros-comportamiento-mundo-peru|Comportamiento y mercado global de seguros]]), es más
  caro que en el mercado donde se documentó.

---

## 11. Glosario operativo: qué es cada estrategia, qué mueve y con qué respaldo

> Añadido el 2026-09-03 (v2.2). Definición corta de cada mecanismo mencionado en §1-§10, con su
> impacto verificado en **salud**, su impacto en **negocio** (siniestralidad/margen) y el **nivel de
> evidencia** que respalda ese efecto. No introduce fuentes nuevas: destila §1-§10.

**Escala de evidencia** (evalúa la fuerza del diseño que sostiene el efecto, no la reputación de la
fuente): 🟢 **Alta** = ECA o cuasi-experimento con control · 🔵 **Sólida** = evaluación oficial o
independiente con método público, frecuentemente modelada · 🟡 **Media** = observacional, estudio de
caso o teoría con evidencia delgada · 🟠 **Baja** = autorreportado o emisor con interés comercial ·
⚪ **Sin evidencia** localizada. En las columnas de impacto, **⛔ marca efecto nulo demostrado**
(distinto de "sin evidencia": aquí se midió bien y no hubo efecto).

### 11.1 Cómo se paga — contrato y asignación de riesgo

| Estrategia | Definición corta | Impacto en salud | Impacto en negocio | Evidencia |
|---|---|---|---|---|
| **Mancomunación de riesgo** | Juntar primas para que los sanos financien a los enfermos en un mismo periodo | Indirecto: habilita acceso | Es el modelo base; colapsa por selección adversa si no hay mandato ni ajuste | 🟢 Teoría fundacional + colapsos documentados (F-90, F-91) |
| **Ajuste de riesgo** | Redistribuir dinero entre aseguradoras según lo enfermo de su cartera | Indirecto: quita el incentivo a descremar | Comprime diferencias de loss ratio y sostiene el pool | 🟡→🟢 Funciona "como se pretendía", sin neutralizar del todo (F-96, F-103) |
| **Capitación** | Monto fijo por persona por periodo, esté sana o enferma | Mixto: mejora prevención, arriesga subprovisión | Transfiere el riesgo al prestador y hace predecible el costo | 🟢 Con gatekeeping: primaria +55,3%, hospital −23,9% (F-109) |
| **Pago por episodio (bundle)** | Un solo precio por todo el tratamiento de una condición | Neutro: sin aumento de complicaciones | **−3,1%** (US$812 por episodio) | 🟢 Aleatorizado por área metropolitana (F-485) |
| **ACO / ahorro compartido** | Si el gasto de la población queda bajo la meta, el prestador cobra parte del ahorro | Calidad mantenida | **~1-2% neto**; en Kinzigtal, costo comparativo menor | 🔵 CMS (F-486) · 🟢 con grupo de control (F-510) |
| **Regla 80/20 (MLR)** | Obliga a destinar ≥80-85% de la prima a atención médica | ⚪ Ninguno directo | Techo legal de utilidad; US$11.800M devueltos 2012-2023 | 🔵 Regulación con datos oficiales (F-197) |
| **Sistema 3M (Singapur)** | Ahorro individual obligatorio + seguro catastrófico + red de subsidio | Cobertura universal sostenida | Contiene riesgo moral sin renunciar a equidad | 🔵 (F-102) ⚠️ su propia reforma de primaria tuvo éxito limitado (F-112) |
| **Concesión capitada (Alzira)** | Un privado opera toda la atención de un territorio por pago per cápita a 15 años | ⚪ Sin evidencia independiente concluyente | ~25% menos costo per cápita **según la parte interesada**; revertido a lo público en 2018 | 🟡 Disputada; brecha documentada entre retórica y realidad financiera (F-520) |
| **Subsidio cruzado (Aravind)** | El que paga financia al que no, con la misma calidad clínica para ambos | Alta: 70% gratis/subsidiado sin segmentar el procedimiento | Autosostenible sin donación; utilización de recursos 80% vs. ~25% global | 🟡 Casos académicos, sin estados auditados públicos (F-499) |
| **Integración vertical** | El asegurador es también dueño de clínicas, farmacia o gestión de beneficios | ⚪ Sin evidencia de mejora (excepción: Kaiser) | ⭐ **Donde está la utilidad real del sector** | 🟢 Filings para el efecto financiero (F-198) ⚠️ no se trasplantó en Brasil (F-501) |
| **PBM** | Intermediario que administra el beneficio de farmacia y gana en el diferencial | ⚪ Ninguno · ⚠️ **negativo indirecto**: frena biosimilares | Máxima rentabilidad del sector (US$1.500M operativos en un trimestre) | 🟢 Filing SEC (F-198) · 🟡 para el bloqueo del ahorro (F-490) |
| **Medicare Advantage** | Plan privado que recibe un pago ajustado por riesgo para cubrir a un beneficiario de Medicare | Calidad **equivalente**, no superior: más prevención, sin ventaja en mortalidad ni readmisiones | Motor de crecimiento; **US$84.000M de sobrepago (2025)**: US$40.000M por codificación + US$44.000M por selección favorable | 🟢 Revisión sistemática (F-494) · 🔵 MedPAC (F-493) |

### 11.2 Cómo se compra — palancas de precio, red y acceso

| Estrategia | Definición corta | Impacto en salud | Impacto en negocio | Evidencia |
|---|---|---|---|---|
| **Reference pricing** | El plan fija un precio tope; si el afiliado elige más caro, paga la diferencia | Neutro: sin daño clínico detectado | ⭐ **−34% en el precio del proveedor** | 🟢 Programa real con datos del comprador (F-484) |
| **Red limitada / por niveles** | Cubrir solo a un subconjunto de prestadores, o cobrar menos por los baratos | Neutro clínicamente ⚠️ el costo se paga en acceso y satisfacción | ⭐ **−40% de gasto en quienes migran**; primas **−16%** | 🟢 Cuasi-experimento con incentivo exógeno (F-516) |
| **Site of care** | Mover el mismo procedimiento del hospital al consultorio, ambulatorio o domicilio | Neutro si la selección de paciente es correcta | US$16.000-37.000 por paciente/año | 🟠 Cifras de emisor con interés comercial directo (F-489) |
| **Centros de excelencia + segunda opinión** | Concentrar cirugía compleja en pocos centros expertos, con segunda opinión obligatoria | Positivo: evita la cirugía innecesaria | Ahorro por procedimiento evitado (~US$30.000 en el caso testigo) | 🟠 Autorreportado por el empleador (F-521) |
| **Biosimilares / genéricos** | Sustituir la marca por su equivalente al vencer la patente | Neutro: equivalencia terapéutica | −5% a −87% de precio ⚠️ **ahorro no realizado** si lo captura el PBM | 🟡 Dato de industria (F-490) |
| **Autorización previa** | Exigir permiso del asegurador antes de un servicio o fármaco caro | ⚠️ **Negativo documentado**: exacerbación, hospitalización prevenible, menor supervivencia libre de enfermedad | Baja utilización, pero un estudio halla **costo administrativo > ahorro**; 80,7% de denegaciones apeladas se revierten | 🟢 Revisión sistemática de daños + auditoría OIG (F-518) |
| **V-BID** | Bajar el copago de lo que sí sirve, en vez de subirlo a todo por parejo | Positivo: +2,8% de adherencia, sostenido | **Neutro en gasto total** — no prometer ahorro | 🟢 Cuasi-experimental con series largas (F-492) |
| **Gatekeeping** | Pasar obligatoriamente por primaria antes del especialista | ⚠️ **Mixto**: menos especialista, pero diagnóstico tardío documentado (cáncer) | Reduce gasto en especialista y hospital | 🟢 Revisión sistemática (F-110) + cuasi-experimento (F-109) |
| **Direct Primary Care** | Cuota mensual fija directo al médico de cabecera, sin seguro de por medio | Teoría fuerte, **evidencia delgada**; sin estudios longitudinales | ⚠️ Excluye a quien no puede pagar la membresía | 🟡 Poca evidencia peer-reviewed (F-107, F-108) |

### 11.3 Cómo se atiende — entrega clínica

| Estrategia | Definición corta | Impacto en salud | Impacto en negocio | Evidencia |
|---|---|---|---|---|
| **VBHC / modelo de Porter** | Organizar la atención por condición y medir resultados que importan al paciente por unidad de costo | ⚪ **Sin estimación de efecto** | ⚪ **Sin ROI demostrado** | 🟡 Revisiones con sesgo de publicación positivo declarado + fracaso documentado en Karolinska (F-507, F-508) |
| **IPU (unidad integrada de práctica)** | Equipo multidisciplinario dedicado a una sola condición, responsable del ciclo completo | Positivo en el caso de alto volumen: supera el promedio nacional en PROMs | No aislado del efecto de volumen | 🟢 PROMs publicados ⚠️ sin control por selección de pacientes (F-509) |
| **PROMs** | Resultados reportados por el propio paciente (dolor, continencia, función) | Habilitante: no interviene por sí solo | Indirecto: hace comparable la calidad y permite contratar por resultado | 🟡 Es infraestructura de medición, no intervención (F-507, F-509) |
| **Cuidado integral (integrated care)** | Coordinar primaria, especialidad, hospital y social como un circuito único | Positivo **cuando tiene los componentes**; ⛔ nulo como programa superpuesto | Rinde **solo si el contrato asigna el riesgo y el ahorro** | 🟢 Meta-análisis de componentes (F-519) + Kinzigtal (F-510) vs. ⛔ nulos (F-473, F-474) |
| **Chronic Care Model** | La versión operativa para crónicos: registro, guía única, equipo, automanejo, seguimiento proactivo | Positivo en control de la enfermedad | Ahorro condicionado a estratificación | 🟢 Revisión de 186 revisiones sistemáticas (F-519) |
| **Estratificación de riesgo** | Clasificar la población por riesgo real para intervenir solo a quien lo justifica | ⭐ **Es la variable que separa lo que funciona de lo que no** | Convierte un programa nulo en uno con efecto (8-33% menos hospitalizaciones en alto riesgo) | 🟢 Reanálisis de programas aleatorizados (F-474) + NHS DPP (F-481) |
| **Task-shifting** | Pasar la tarea rutinaria del médico a enfermería o técnico, estandarizada por protocolo | ⭐ **Efecto grande**: control de hipertensión 44%→90% | Ahorro no aislado, pero libera el recurso más caro | 🟢 Cohorte poblacional con comparador nacional (F-480) |
| **CHW (agente comunitario)** | Persona de la comunidad, con formación corta, que hace seguimiento y adherencia en terreno | Positivo: presión arterial, vinculación al cuidado, adherencia | **Costo-efectivo, no ahorrador**: ICER US$3.299/AVAC | 🟢 Revisiones de ensayos por conglomerados (F-505) |
| **De-implementación / Choosing Wisely** | Dejar de hacer lo que la evidencia dice que no aporta | Positivo: evita el daño del servicio inútil | Ahorro variable; **solo funciona multicomponente y dirigido al clínico** | 🟢 Revisiones sistemáticas ⚠️ certeza de la evidencia primaria baja a muy baja (F-487) |
| **Hospital en casa** | Atención de nivel hospitalario agudo entregada en el domicilio | ⭐ **Menor mortalidad intrahospitalaria** y menos urgencias ⚠️ readmisión mixta | **−19% a −30%** de costo | 🔵/🟢 Informe regulatorio + meta-análisis de ECAs (F-488) |
| **Triage** | Clasificar la urgencia y derivar al nivel correcto antes de que el paciente elija solo | Depende de la **seguridad** del algoritmo, no de su precisión | Potencial de evitar el nivel de atención equivocado | 🟡 Precisión ≠ outcome; ver [[modelo-salud-ia-farmacias-peru]] |

### 11.4 Lo no médico y lo digital

| Estrategia | Definición corta | Impacto en salud | Impacto en negocio | Evidencia |
|---|---|---|---|---|
| **Wellness corporativo** | Programa de bienestar del empleador: tamizajes, retos, charlas | Solo **conducta autorreportada**; nada clínico | ⛔ **Nulo en gasto médico**, también a 3 años | 🟢 Dos RCT grandes + seguimiento (F-469, F-470, F-471) |
| **Shared-value insurance (Vitality)** | Premiar con descuentos la conducta saludable medida y compartir el ahorro | ⚠️ **Atribución sin resolver**: la evidencia independiente es más cauta que la empresa | ⭐ **Probado**: utilidad operativa +70% (FY2025) | 🔵 Resultados oficiales para negocio · 🟡 en tensión para salud (F-497 vs. F-100) |
| **Hotspotting** | Detectar al puñado de pacientes que concentra el gasto y ponerles un equipo intensivo | ⛔ Sin efecto (readmisión 62,3% vs. 61,7%) | ⛔ Nulo | 🟢 RCT (F-473) |
| **Gestión de casos / coordinación** | Un gestor que agenda, acompaña y conecta servicios para pacientes complejos | Mejora **solo en el subgrupo de alto riesgo inmediato** | ⛔ **Ningún ahorro neto** con las cuotas de gestión contadas | 🟢 15 programas con asignación aleatoria (F-474) |
| **Determinantes sociales / comida como medicina** | Pagar con dinero de salud lo que no es salud: alimento, vivienda, transporte | ⚠️ **Mixto**: −16,4% de gasto en observacional, ⛔ nulo en HbA1c en el RCT | ROI 85% (comida) y 50% (vivienda), **con casos negativos en el rango**; ⚠️ desfinanciado pese a demostrar ahorro | 🟢 Revisión de ROI + RCT + evaluación estatal (F-475 a F-478) |
| **Incentivos financieros conductuales** | Pagar por lograr una conducta. *Recompensa*: 90% de aceptación · *Depósito*: más efectivo, 13,7% de aceptación | ⭐ Positivo: abstinencia 16,0% vs. 6,0% | No medido en gasto médico | 🟢 RCT N=2.538 (F-479) |
| **Programa estructurado de prevención (DPP)** | Currículo de 12 meses de dieta y actividad para **prediabetes confirmada**, no para toda la población | ⭐ Positivo: menor incidencia de diabetes (IRR 0,938) | **Costo-efectivo, no necesariamente ahorrador** | 🟢 Evaluación independiente comisionada (F-481) |
| **Automanejo / autoatención** | Que el paciente gestione su condición crónica: medir, ajustar, decidir cuándo consultar | Depende de si **conecta con una decisión clínica** | ⚪ Sin evidencia de impacto de largo plazo en siniestralidad | 🟡 (F-519 como componente; F-515 en su versión conectada) |
| **Automonitoreo + autotitulación** | El paciente mide en casa y ese dato ajusta su dosis | ⭐ Positivo: presión significativamente menor | Costo-efectivo | 🟢 ECA en 142 consultorios (F-515) |
| **Digital de "manejo de medicación"** | Herramienta cuyo output **cambia la prescripción** | ✅ Baja la presión de forma significativa | Sube el gasto a corto plazo y **lo recupera con ahorro neto de largo plazo** | 🔵 Evaluador independiente, efecto económico **modelado** a 10 años (F-512) |
| **Digital de "cambio de conducta"** | App que informa, motiva o da coaching sin tocar la terapia | ⛔ Poco o ningún efecto (presión, HbA1c no sostenida) | ⚠️ **Aumenta el gasto neto** (+US$2.002 a 3 años en diabetes) | 🔵 Tres evaluaciones del mismo evaluador (F-482, F-512) |
| **Telesalud** | Consulta remota que sustituye a la presencial | Acceso, **no morbilidad** | Ahorra por sustitución de visita y traslado, no por enfermar menos | 🟢/🔵 ⚠️ evidencia dominada por el período COVID (F-517) |

### 11.5 Los cinco conceptos que explican los fracasos

No son estrategias sino **diagnósticos**: por eso no llevan columnas de impacto.

| Concepto | Definición corta | Por qué importa |
|---|---|---|
| **Selección adversa** | Se aseguran los más enfermos, sube la prima, se van los sanos, sube más | Destruye pools reales ("espiral de la muerte"), no es teoría (F-90, F-91) |
| **Selección favorable** | Captas gente más sana de lo que su puntaje de riesgo indica | US$44.000M de sobrepago anual en MA **sin gestionar nada** (F-493) |
| **Riesgo moral** | Al estar asegurado consumes más, porque el precio marginal que ves no es el real | Es conducta económica racional, no mala fe — propiedad estructural del seguro (F-89) |
| **Regresión a la media** | El paciente carísimo de este año gasta menos el próximo por sí solo | El programa se lleva el crédito: por eso los estudios antes-después "encuentran" ahorro que el RCT no confirma (F-473) |
| **Bolsillo equivocado** | Quien paga la intervención no es quien cobra el ahorro (otro presupuesto, otro año, otra aseguradora) | ⭐ Explica más fracasos que la falta de eficacia clínica (F-477, F-490, F-502) |

## Limitaciones generales

- Ninguna evidencia de precisión/efectividad citada aquí fue validada en población peruana
  específicamente.
- La pista social se evaluó explícitamente en las 3 investigaciones y se omitió las 3 veces —
  sin resultados de búsqueda en foros/RRSS para estos temas técnico-institucionales.
- La fuente F-98 (revisión sistemática de ACOs) no se pudo verificar con autor/journal exacto —
  tratar con reserva.
- **(§2, v1.1)** Todos los datos financieros agregados de §2.1-§2.5 (márgenes, MLR, regla
  80/20) son de EE.UU. — el único con datos públicos agregados y auditables encontrados en
  esa ronda. Se usaba como proxy del "balance global" solo porque concentra ~80% de las
  primas de salud privadas del mundo (F-196, 🟠D, dato no verificado con rigor A/B).
  **(Parcialmente resuelto en v1.2, §2.6)**: se sumó contraste de Europa y Asia (rentable y
  en expansión, sin el mismo techo regulatorio) — pero Perú/Latinoamérica **sigue sin dato
  agregado de rentabilidad** pese a búsqueda dedicada; hueco confirmado, no cerrado.
- **(§2, v1.1)** La cifra de Optum Rx (F-198) es de un solo trimestre y de un solo actor,
  aunque sea el más grande — no se puede generalizar sin más datos que "todo PBM integrado
  es igual de rentable"; se reporta como el caso mejor documentado (filing primario), no
  como promedio de la industria.
- **(§2.6, v1.2)** Los casos europeos y asiáticos (F-203 a F-207) son, igual que Optum
  Rx, actores individuales (o un país, en el caso de China) en un trimestre/año dado — no
  se puede generalizar a "toda Europa/Asia es rentable en salud" sin más muestra, se
  reportan como evidencia direccional consistente, no como promedio regional verificado.

- **(§6-§9, v2.0)** **Sesgo geográfico persistente y agravado**: casi toda la evidencia
  aleatorizada del §6 y del §7 es estadounidense o británica (RCT de wellness, hotspotting,
  comida como medicina, CJR, MSSP, NHS DPP). Las dos excepciones deliberadas son los CHW en
  países de ingreso bajo y medio (F-505) y los casos de India (F-498, F-499). **Ninguna
  evidencia de §6-§8 fue validada en población peruana.**
- **(§6, v2.0)** Los resultados nulos de wellness (F-469 a F-471) provienen de **dos poblaciones
  de empleados formales estadounidenses**. No permiten concluir sobre poblaciones sin cobertura
  previsional ni sobre intervenciones dirigidas a riesgo ya diagnosticado — de hecho, el NHS DPP
  (F-481), que sí focaliza por riesgo medido, **da resultado positivo**.
- **(§7.1, v2.0)** Las cifras de traslado de sitio de atención (F-489) provienen exclusivamente
  de actores con interés comercial directo. Se reportan por su mecanismo, **no como magnitud
  verificada**; falta una evaluación independiente.
- **(§8, v2.0)** Los datos clínicos de Narayana Health (F-498), CareMore (F-504) y ChenMed
  (F-116) son **autorreportados o comparados contra promedio nacional sin control por
  selección**. El cuadrante "gana dinero y mejora la salud" es real, pero su evidencia clínica es
  sistemáticamente más débil que su evidencia financiera — el patrón inverso al del sector
  académico.
- **(§8.4, v2.0)** Las cifras de UnitedHealth (F-495) fueron recuperadas de comunicados de
  resultados vía prensa financiera, **no leídas línea por línea del 10-K**.
- **(§9.1, v2.0)** El hueco de dato peruano (margen y siniestralidad del ramo salud/EPS) **sigue
  abierto tras una segunda búsqueda dedicada** (F-506). Se declara la ausencia; no se rellena
  con proxies.

- **(§10, v2.1)** El modelo de Porter **no tiene estimación de efecto** comparable a las palancas
  del §7. Lo que este node afirma es que su base de evidencia de implementación es débil y con
  sesgo de publicación positivo declarado (F-507) — **no** que el marco sea incorrecto. Esa
  distinción debe conservarse al citarlo.
- **(§10.2, v2.1)** Las cifras de Nuka (F-511) son **autorreportadas y sin grupo de control**;
  las de Alzira (F-520) provienen de una parte interesada y están en disputa política explícita.
  Solo **Kinzigtal** (F-510) tiene diseño con grupo de control — y sus propios evaluadores
  advierten que no está establecido cuánto del ahorro es ganancia real de salud poblacional.
- **(§10.3, v2.1)** La evidencia de costo de telesalud (F-517) es mayoritariamente del período
  COVID, con el efecto de la pandemia confundido con el de la tecnología. Las evaluaciones de
  PHTI (F-482, F-512, F-513) son la mejor serie independiente disponible, pero **modelan** el
  efecto económico de largo plazo en vez de observarlo.
- **(§10.4, v2.1)** El efecto de red limitada (F-516) proviene de **empleados públicos de
  Massachusetts en 2012**. Su magnitud no es trasladable a un mercado con estructura de oferta
  distinta; el mecanismo (precio + cantidad) sí.

## Conexiones

- [[modelo-salud-ia-farmacias-peru|Modelo de triage IA + farmacias (Perú)]] — este node aporta el
  marco de mecanismos globales; ese node aplica el diseño concreto al caso peruano (PL 08488,
  automedicación, InkaFarma/Mifarma).
- [[seguros-comportamiento-mundo-peru|Comportamiento y mercado global de seguros]] — §7 de ese
  node (mercado global por ramo) es el punto de partida cuantitativo de este; el NPS de ChenMed
  (§4 aquí) se compara contra el NPS de aseguradoras documentado ahí (§7.2).
- [[glosario-seguro-salud-peru|Glosario de seguro de salud en Perú]] — vocabulario base.
- [[behavioral-design-estado-disciplina|Behavioral design: estado de la disciplina y del
  mercado]] — Discovery Vitality aparece en ambos: ahí como caso de referencia de
  behavioral design aplicado a seguros, aquí como mecanismo que navega presión de costo.
- [[futuro-asesores-seguros-venta-digital|¿Desaparecerán los asesores de seguros?]] — los
  casos de Babylon Health y el "reset" de Oscar Health (§3 aquí) son la misma advertencia
  a nivel de suscripción/operación que ese node documenta a nivel de distribución: apostar
  por tecnología sin disciplina humana de por medio tiende a salir caro.
- [[behavioral-design-estado-disciplina|Behavioral design: estado de la disciplina y del
  mercado]] — **(v2.0)** el §6 de este node es la contraparte de evidencia dura de ese: los RCT
  de wellness (F-469 a F-472) y el nulo replicado del cambio de hábitos delimitan **hasta dónde
  llega el behavioral design cuando la métrica es gasto médico y no conversión**. El
  contraejemplo positivo (incentivos para dejar de fumar, F-479) y su hallazgo de que
  recompensa y depósito optimizan en direcciones opuestas es material directo para ese node.
- [[tendencias-diseno-innovacion|Tendencias en diseño e innovación]] — **(v2.0)** F-472 (el
  "US$3,27 por dólar" del wellness) es un caso de manual de las reglas de ese node: una cifra
  que se institucionalizó globalmente antes de ser probada y que **sus propios autores
  refutaron después** sin que dejara de circular. Y F-482 (manejo digital de crónicos, US$58 mil
  millones invertidos con resultado negativo) es el equivalente en salud de sus casos de
  divergencia entre inversión y desempeño.
