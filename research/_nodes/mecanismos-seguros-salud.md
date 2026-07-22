# Mecanismos de seguros de salud: presión actual y modelos que la navegan

> Node. Fuente de verdad de este tema. Rescata 3 investigaciones `/seeker`/`/trinidad` que
> originalmente solo vivían en el chat (2026-07-10). Fuentes indexadas en
> `fuentes/codice.md` (F-86 a F-116, F-193 a F-207).
>
> Fecha de elaboración: 2026-07-10 · Última actualización: 2026-07-22 · Versión: v1.2
> (v1.1 amplía con §2: balance financiero global/rentabilidad de la categoría; v1.2 amplía
> con §2.6: contraste regional Europa/Asia/Perú-Latam — corrida adicional de `/trinidad`)

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

## 5. Síntesis transversal (las 4 secciones)

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
