# Curva de aprendizaje de asesores comerciales con herramientas digitales de venta

*Node creado 2026-09-09 (skill `/seeker`) — v1.0.*

## 0. Encargo y alcance

Sustento académico para diseñar el sistema de medición de una herramienta digital
guía para asesores comerciales (lógica tipo AIDA: parámetros de producto, guiones,
técnicas de venta como referencia), **antes** de construir los indicadores del
prototipo. Cubre cinco capas: (1) modelo matemático de la curva de aprendizaje,
(2) modelos de evaluación de capacitación, (3) práctica deliberada, (4) time to
proficiency / onboarding comercial, (5) adopción de sales enablement tools. Para
cada fuente clave: hallazgo → cómo se traduce en un indicador medible del prototipo.

## 1. Veredicto inicial

Hay sustento académico sólido para las cinco capas, pero con una advertencia
estructural que debe gobernar el diseño de indicadores: **la literatura de curva de
aprendizaje (power law / exponencial) es sobre el individuo practicando una tarea
bien definida y repetible** (tiempo de reacción, geometría, digitación) — no sobre
"desempeño comercial" como constructo agregado. Aplicarla a un asesor requiere
descomponer el desempeño en **sub-tareas medibles y repetibles** (tiempo para
encontrar el parámetro correcto de un producto, tasa de objeciones resueltas por
guion, precisión en la recomendación) — no ajustar una curva directamente sobre
"ventas cerradas por mes", que está confundida con estacionalidad, territorio y
calidad de leads. Kirkpatrick es útil como **taxonomía de niveles de indicador**, no
como cadena causal probada — la evidencia empírica (Alliger & Janak, 1989) muestra
que los niveles no están significativamente correlacionados entre sí. La práctica
deliberada es el matiz más importante para un prototipo digital: **la cantidad de
uso de la herramienta (logs) es un proxy débil de competencia si la práctica no
tiene objetivo específico, feedback inmediato y dificultad ajustada** — esto es
precisamente lo que Macnamara et al. (2014) encuentran al mostrar que la práctica
deliberada explica <1% de la varianza de desempeño en "profesiones" (la categoría
más cercana a venta), muy por debajo de música/ajedrez/deportes.

## 2. Teoría de la curva de aprendizaje: ¿power law o exponencial?

**Newell & Rosenbloom (1985 [sic, cap. de 1981 en Anderson, ed.])** — *Mechanisms of
skill acquisition and the law of practice*, en Anderson, J.R. (ed.), *Cognitive
Skills and Their Acquisition*, Erlbaum — `(Newell & Rosenbloom, 1981 — ⚪ capítulo de
libro académico, sin arbitraje por pares tipo revista; canónico, citado >5.000 veces)`.
Formula la **power law of practice**: T = a·Pⁿ + c (el tiempo/error de ejecución de
una tarea decae como función potencia del número de intentos P), y propone el
**chunking** (agregación jerárquica de producciones en un sistema de producción,
construyendo sobre Miller 1956) como mecanismo cognitivo subyacente. Aplica a
tareas perceptuales y cognitivas de todo tipo (detección de blancos, pruebas
geométricas, solitario). **Traducción a indicador de prototipo:** graficar
`tiempo_tarea_i vs. n_intentos_tarea_i` (donde tarea_i es una sub-tarea acotada —
p. ej. "encontrar el parámetro correcto de cobertura para el perfil X del cliente")
y ajustar T = a·nᵇ; b (el exponente de aprendizaje) es el indicador comparable
entre asesores o entre versiones de la herramienta.

**Heathcote, Brown & Mewhort (2000)** — *The power law repealed: the case for an
exponential law of practice*, *Psychonomic Bulletin & Review*, 7(2), 185-207 —
`(Heathcote et al., 2000 — 🟢 peer-reviewed)`. Meta-análisis metodológico: ajustaron
funciones potencia y exponencial a **40 sets de datos (7.910 series de aprendizaje,
475 sujetos, 24 experimentos)**, comparando el ajuste sobre datos **individuales**
vs. **promediados**. Hallazgo clave: **la función exponencial ajusta mejor que la
potencia en el 100% de los sets de datos individuales**; el ajuste de la power law
que domina la literatura previa es un **artefacto del promediado entre sujetos**
(promediar curvas exponenciales con distinta tasa produce, matemáticamente, algo
que se parece más a una potencia). Proponen la función **APEX** (variante
exponencial con parámetro de práctica pre-experimental) como mejor candidata.
`(Heathcote et al., 2000 — ✅ diseño metanalítico explícito, N grande, réplica
across 24 experimentos — pero ⚠️ validez ecológica: todas las tareas de origen son
de laboratorio cognitivo, no desempeño laboral)`. **Traducción a indicador:**
**no promediar la curva entre asesores** para reportar "la curva de aprendizaje de
la herramienta" — eso reintroduce el artefacto de Heathcote et al. Ajustar la
curva **por asesor individual** (exponencial: T = a·e^(-λn) + c) y reportar la
distribución de λ (velocidad de aprendizaje) entre asesores, no una curva única
agregada.

**Contraevidencia/matiz buscado activamente (Paso 11):** se buscó si el debate
power-vs-exponencial se resolvió en contra de Heathcote et al. desde 2000 — no se
encontró una refutación directa, pero sí evidencia de que el patrón es más complejo
de lo binario: hay trabajo posterior (Piecewise power laws in individual learning
curves, PMC — no se pudo verificar autoría/año exactos en esta búsqueda) que sugiere
que curvas individuales pueden ser **potencias por tramos** (con puntos de quiebre,
p. ej. al automatizar una sub-habilidad) en vez de una sola función suave — lo cual
es compatible con la idea de "chunking" de Newell & Rosenbloom pero incompatible con
ajustar una sola curva continua de principio a fin. `(⚠️ fuente no verificada con
autoría exacta — no registrada en el ledger, mencionada solo como pista para
seguimiento futuro)`. **Implicación de diseño:** si la curva de un asesor muestra
un salto discontinuo (no una desaceleración suave), no es un error de medición —
puede ser el momento en que automatizó una sub-tarea (p. ej. dejó de necesitar
consultar el guion para una objeción común). Vale la pena instrumentar el prototipo
para detectar esos quiebres, no solo el exponente promedio.

## 3. Modelos de evaluación de capacitación: Kirkpatrick, Phillips y sus críticas

**Kirkpatrick (1959, serie de 4 artículos en *Journal of ASTD*; consolidado en
Kirkpatrick, D.L., 1994/1996, *Evaluating Training Programs: The Four Levels*)** —
`(Kirkpatrick — ⚪ libro/serie de práctica profesional, no arbitrado por pares;
extremadamente influyente pese a origen no académico)`. Cuatro niveles: **(1)
Reacción** (satisfacción del participante), **(2) Aprendizaje** (conocimiento/
habilidad adquirida, medible pre/post), **(3) Conducta** (transferencia al puesto de
trabajo — el asesor de verdad usa lo aprendido con clientes), **(4) Resultados**
(impacto de negocio — ventas, retención de cliente, ratio de conversión).
**Traducción a indicador por nivel, aplicado al prototipo:**
| Nivel | Qué mide | Indicador en el prototipo |
|---|---|---|
| 1. Reacción | Percepción del asesor sobre la herramienta | Encuesta corta post-sesión (NPS/CSAT de la herramienta) |
| 2. Aprendizaje | Conocimiento de producto/guion adquirido | Evaluación pre/post de conocimiento (quiz de parámetros de producto) |
| 3. Conducta | Uso real en interacción con cliente | Observación conductual tipo mystery shopper; logs de qué guion/parámetro consultó el asesor durante una llamada real |
| 4. Resultados | Impacto comercial | Tasa de conversión, ticket promedio, tiempo de cierre — controlando por territorio/leads |

**Alliger & Janak (1989)** — *Kirkpatrick's Levels of Training Criteria: Thirty Years
Later*, *Personnel Psychology*, 42(2), 331-342 — `(Alliger & Janak, 1989 — 🟢
peer-reviewed)`. Revisión crítica que identifica **tres supuestos tácitos** del
modelo que la evidencia no sostiene: que los niveles están en **orden ascendente de
información**, que están **causalmente encadenados**, y que están **positivamente
inter-correlacionados**. Su revisión de estudios empíricos **no encuentra evidencia
de que los niveles estén significativamente correlacionados entre sí** — es decir,
que un asesor reaccione bien (nivel 1) no predice que aprenda (nivel 2), y que
aprenda no predice que cambie su conducta (nivel 3). `(⚠️ validez de constructo del
modelo completo: la cadena causal 1→2→3→4 que la mayoría de la industria asume no
tiene respaldo empírico consistente)`. **Implicación de diseño crítica:** el
prototipo **no puede asumir que mejorar el nivel 2 (quiz de conocimiento) se
traduce en el nivel 3 (conducta real) o el nivel 4 (resultados)** — hay que medir
los cuatro niveles de forma independiente y validar la correlación entre ellos
específicamente para esta herramienta, no darla por sentada de la literatura.

**Bates (2004)** — *A critical analysis of evaluation practice: the Kirkpatrick
model and the principle of beneficence*, *Evaluation and Program Planning*, 27(3),
341-347 — `(Bates, 2004 — 🟢 peer-reviewed)`. Critica que el modelo, centrado en la
pregunta sumativa ("¿funcionó?"), **no responde la pregunta formativa** ("¿cómo
mejorar el diseño?"), limitando su utilidad para iterar el prototipo durante el
desarrollo — solo sirve para evaluarlo ya terminado.

**Reio, Rocco, Smith & Chang (2017)** — *A Critique of Kirkpatrick's Evaluation
Model*, *New Horizons in Adult Education & Human Resource Development*, 29(2),
35-53 — `(Reio et al., 2017 — 🟢 peer-reviewed)`. Síntesis de las críticas
acumuladas: falta de marco teórico explícito (no dice *por qué* la capacitación
produce cambio de conducta, solo que debería medirse), ambigüedad operacional de
cómo medir cada nivel, y sobre-simplicidad frente a la complejidad real del
aprendizaje adulto y organizacional.

**Phillips (ROI Methodology, Jack J. Phillips, desde 1990s; sintetizado en Phillips
& Phillips, *The Value of Learning*, 2007)** — `(Phillips — ⚪ metodología de
consultoría/práctica profesional, no arbitrada por pares)`. Añade un **Nivel 5:
ROI** — convierte el impacto de negocio del nivel 4 a valor monetario y lo compara
contra el costo del programa, **aislando** el efecto de la capacitación de otros
factores (cambios de mercado, liderazgo, estacionalidad) mediante métodos como
grupo de control, estimación de tendencia, o estimación del propio participante.
Crítica recurrente en la literatura de práctica profesional (no peer-reviewed, mera
señal de consenso de industria): aislar el efecto causal de la capacitación de
otros factores es metodológicamente difícil y costoso, y el valor práctico de
llegar al Nivel 5 es cuestionado cuando el Nivel 4 ya muestra la dirección del
efecto. **Traducción a indicador (aplicable solo si el prototipo llega a producción
con datos suficientes):** diseño cuasi-experimental (diferencias en diferencias
entre asesores con y sin acceso a la herramienta, o entre cohortes de adopción
escalonada) para poder aislar el efecto de la herramienta del ruido de mercado
antes de reportar cualquier cifra de "ROI".

## 4. Práctica deliberada: la calidad de la práctica, no solo la cantidad de uso

**Ericsson, Krampe & Tesch-Römer (1993)** — *The role of deliberate practice in the
acquisition of expert performance*, *Psychological Review*, 100(3), 363-406 —
`(Ericsson et al., 1993 — 🟢 peer-reviewed, uno de los papers más citados de
psicología del s. XX)`. Estudio de violinistas: las diferencias en desempeño de
elite se explican por la cantidad acumulada de **práctica deliberada** —
específicamente actividades diseñadas para mejorar el desempeño, con **objetivo
específico, feedback inmediato, y repetición con ajuste**, distinta de la simple
repetición o el juego libre. Definición operacional estricta: no cualquier "hora de
uso" cuenta como práctica deliberada. **Traducción a indicador clave para el
prototipo:** un log de "minutos usando la herramienta" **no es** un indicador de
práctica deliberada por sí solo. Para que lo sea, el prototipo debe instrumentar:
(a) si la sesión tenía un objetivo específico (p. ej. "practicar objeción de
precio"), (b) si hubo feedback inmediato y específico (no solo "correcto/
incorrecto"), y (c) si la dificultad se ajustó al nivel del asesor. Solo esas
sesiones cuentan para el indicador de "práctica deliberada acumulada"; el resto es
"exposición pasiva" y debe reportarse aparte.

**Macnamara, Hambrick & Oswald (2014)** — *Deliberate Practice and Performance in
Music, Games, Sports, Education, and Professions: A Meta-Analysis*, *Psychological
Science*, 25(8), 1608-1618 — `(Macnamara et al., 2014 — 🟢 peer-reviewed;
observacional/meta-analítico sobre estudios primarios en su mayoría correlacionales)`.
Meta-análisis que matiza fuertemente a Ericsson et al.: la práctica deliberada
explica **26% de la varianza en juegos, 21% en música, 18% en deportes, 4% en
educación, y menos de 1% en "profesiones"** (la categoría de dominio más análoga a
venta comercial). `(⚠️ validez de constructo en disputa: Ericsson respondió — ver
abajo — que Macnamara et al. usaron una definición mucho más amplia de "práctica
deliberada" que la original de 1993, incluyendo actividades como asistir a charlas
o estudiar solo, que no cumplen los criterios estrictos)`. **Implicación crítica
para el prototipo:** el dominio "profesiones" (ventas, gestión, tipeo) es
justamente donde el vínculo práctica→desempeño es **más débil y menos estudiado**
en la literatura — el prototipo no puede asumir por analogía con música/deportes
que más práctica en la herramienta necesariamente producirá mejoras de desempeño
proporcionales; hay que medirlo empíricamente para este caso específico, con
escepticismo activo.

**Contraevidencia/debate activo (Paso 11):** Ericsson (2016) respondió directamente
a Macnamara et al. defendiendo la definición original y cuestionando su método de
codificación; Macnamara & Hambrick (2020) replicaron señalando que los criterios
originales no han cambiado sustancialmente y el debate sigue sin resolverse en
consenso — se reporta la controversia como abierta, no se impone un bando.
`(Macnamara & Hambrick, 2020 y réplica en PMC8049893 — 🟢 peer-reviewed, controversia
activa)`.

## 5. Time to proficiency / time to productivity en onboarding comercial

**Bridge Group (reporte anual de benchmarks SaaS)** — `(⚪ reporte de industria, no
aplica revisión por pares — metodología de encuesta a empresas SaaS, no auditable
públicamente)`. Cifras de referencia repetidas en la industria: ramp time promedio
~3.2 meses hasta productividad plena; ejecutivos de cuenta enterprise tardan en
promedio 5.3 meses en cerrar su primer deal y 12-18 meses en alcanzar cuota de forma
consistente. `(🟠 D — cifra de consultora, sin acceso a metodología completa de
muestreo; útil como orden de magnitud de industria, no como dato duro)`.

**Brandon Hall Group (2023)** — onboarding estructurado reduce el time-to-productivity
en 30-50% frente a onboarding no estructurado — `(🟠 D — reporte de industria,
método no verificado en esta búsqueda)`. **Traducción a indicador:** definir
explícitamente qué evento marca "productividad plena" **antes** de medir (¿primer
deal cerrado? ¿cuota alcanzada dos meses consecutivos? ¿score de mystery shopper
sobre umbral?) — la literatura de industria usa definiciones distintas entre sí, lo
que hace los benchmarks no comparables entre organizaciones si no se fija el
criterio propio primero.

**Retención de conocimiento / forgetting curve — capa donde la búsqueda encontró un
problema de eco de cita (Paso 6) que hay que reportar explícitamente:** la cifra
"79% de empleados no puede recordar información crítica de entrenamiento después de
30 días — estudio longitudinal en *Human Resource Development Quarterly* (2023)"
**circula en múltiples blogs corporativos con el mismo fraseo casi idéntico, pero
no se pudo localizar el artículo real** en *HRDQ* que la respalde — es una cifra
sin fuente primaria verificable, un patrón típico de estadística fabricada o
mal-atribuida que se auto-replica en contenido de marketing (posiblemente generado
o parafraseado por IA). **No se registra como fuente en el ledger — se documenta
aquí como advertencia explícita: no usar esta cifra ni su atribución en el
prototipo ni en ningún material que cite este node.** Lo mismo aplica a la cifra
"90% olvidado en 30 días" atribuida sueltamente a Ebbinghaus sin cita verificable.

Lo que **sí** tiene respaldo académico real sobre retención y olvido:

**Murre & Dros (2015)** — *Replication and Analysis of Ebbinghaus' Forgetting
Curve*, *PLOS ONE*, 10(7) — `(Murre & Dros, 2015 — 🟢 peer-reviewed)`. Replican el
método de ahorros de Ebbinghaus (1885) sobre sílabas sin sentido con re-aprendizaje
a 20 min, 1h, 9h, 1 día, 2 días, 31 días — confirman la forma general de la curva
de olvido, con un salto ligero alrededor de las 24h (atribuido al sueño).
`(⚠️ validez ecológica muy baja para este caso de uso: es memoria de sílabas sin
sentido de UN sujeto, no conocimiento de producto/guion de venta de un asesor —
extrapolar la forma exacta de esta curva a conocimiento comercial complejo es una
sobre-extensión que la fuente original no sostiene)`.

**Cepeda, Pashler, Vul, Wixted & Rohrer (2006)** — *Distributed Practice in Verbal
Recall Tasks: A Review and Quantitative Synthesis*, *Psychological Bulletin*,
132(3), 354-380 — `(Cepeda et al., 2006 — 🟢 peer-reviewed; meta-análisis de 839
evaluaciones en 317 experimentos, 184 artículos)`. La práctica espaciada (spaced
repetition) mejora la retención final frente a la práctica masiva; el intervalo
óptimo entre repasos depende del intervalo de retención deseado (a mayor plazo que
se quiere recordar, mayor debe ser el espaciado entre repasos). **Traducción a
indicador:** medir retención de conocimiento de producto/guion a **30/60/90 días**
con evaluación (no solo autopercepción) es razonable como práctica de la industria,
pero el prototipo debería, además, **instrumentar refuerzo espaciado** (micro-quiz
recurrentes) dentro de la herramienta y medir si eso mejora la retención a 90 días
frente a un grupo que solo usó la herramienta sin refuerzo — eso convierte la
medición de retención en un experimento útil, no solo un reporte descriptivo.

## 6. Aplicación a herramientas digitales de venta (sales enablement)

**Agnihotri, Chaker, Dugan, Galvan & Nowlin (2023)** — *Sales technology research: a
review and future research agenda*, *Journal of Personal Selling & Sales
Management*, 43(4) — `(Agnihotri et al., 2023 — 🟢 peer-reviewed)`. Revisión de 50+
años de literatura de tecnología de ventas (1971-2023). Hallazgo relevante para el
prototipo: el campo tiene una **imagen fragmentada** sobre qué factores llevan de
adopción a uso efectivo — entrenamiento, presión del cliente y uso de pares
influyen en la adopción, pero **no es la cantidad de tecnología usada, sino cómo se
usa**, lo que predice el efecto sobre desempeño (converge con Macnamara et al. y
con la crítica a "hours of use" como proxy).

**Good, Hughes, Kirca & McGrath (2022)** — *A self-determination theory-based
meta-analysis on the differential effects of intrinsic and extrinsic motivation on
salesperson performance*, *Journal of the Academy of Marketing Science*, 50(3),
586-614 — `(Good et al., 2022 — 🟢 peer-reviewed; meta-análisis de 293 tamaños de
efecto, 127 estudios, N=77.560)`. La motivación intrínseca predice desempeño de
venta más fuerte que la extrínseca (r=.298 vs. r=.176), y ese patrón es **más
marcado en vendedores con mayor tenure/experiencia**. `(✅ N muy grande, meta-análisis
riguroso; ⚠️ el desempeño medido en los estudios primarios suele ser
autorreportado o de supervisor, no siempre objetivo)`. **Implicación de diseño:**
si el prototipo mide "adopción de la herramienta" como proxy de motivación/
compromiso del asesor, conviene distinguir uso motivado intrínsecamente (el asesor
la usa porque le sirve) de uso forzado por mandato — probablemente tengan efectos
distintos sobre la curva de aprendizaje real, replicando el patrón de este
meta-análisis.

**Mystery shopping como método de observación conductual (nivel 3 de Kirkpatrick):**
la literatura académica (van der Wiele, Hesselink & van Iwaarden, 2005, *Journal of
Retailing*, "Mystery shopping: A tool to develop insight into customer service
provision" y trabajo posterior en la misma revista sobre si el mystery shopping
predice satisfacción/ventas reales) — `(⚠️ trazabilidad exacta de autoría/año no
verificada con precisión suficiente en esta búsqueda para citar con confianza total;
tratar como pista, no como cita cerrada)` — muestra que el mystery shopping puede
ser confiable (alta consistencia inter-evaluador) si el instrumento está bien
diseñado, pero su validez de criterio (¿predice ventas/satisfacción real?) es
objeto de debate activo en la literatura — no asumir automáticamente que un buen
score de mystery shopper se traduce en mejor resultado comercial; validarlo para
este caso.

## 7. Contraevidencia buscada (Paso 11) — síntesis

Se buscó activamente evidencia que contradijera cada pieza central del sustento:

- **¿La power law está muerta?** No — el debate power-vs-exponencial sigue activo
  desde 2000 sin resolución consensuada citable en esta búsqueda; lo que sí está
  bien establecido es que **promediar entre sujetos infla artificialmente el ajuste
  de la power law** (Heathcote et al., 2000), lo cual es una advertencia de diseño,
  no una refutación total del modelo.
- **¿Kirkpatrick tiene evidencia causal real?** Se buscó específicamente evidencia a
  favor de la cadena causal 1→2→3→4 y **no se encontró** — al contrario, Alliger &
  Janak (1989) es la evidencia empírica clásica **en contra** de esa cadena.
- **¿La práctica deliberada aplica igual a "profesiones" que a música/deportes?**
  No — Macnamara et al. (2014) es en sí mismo el hallazgo de contraevidencia (<1% de
  varianza explicada en profesiones), y el debate Ericsson-vs-Macnamara sigue
  abierto y se reporta como tal, no resuelto a favor de un bando.
- **¿Hay evidencia de que el entrenamiento de ventas no funciona?** La búsqueda no
  encontró un meta-análisis específico de sales training con hallazgo nulo general,
  pero sí encontró la advertencia metodológica de que el sesgo de publicación a
  favor de resultados significativos probablemente **infla** la efectividad
  reportada del entrenamiento en la literatura existente — se reporta la ausencia
  de un hallazgo nulo claro sin asumir que eso significa "el entrenamiento
  funciona sin reservas".

## 8. Tabla resumen de rigurosidad

| Fuente | Tipo de evidencia | Revisión por pares | N | Validez | Confiabilidad | Peso para el diseño de indicadores |
|---|---|---|---|---|---|---|
| Newell & Rosenbloom, 1981 | Teórico/modelo computacional | ⚪ capítulo de libro | — | ✅ modelo canónico, dominio amplio | — | 🟢 Alto (marco conceptual base) |
| Heathcote et al., 2000 | Meta-metodológico (re-análisis) | 🟢 sí | 475 sujetos / 24 experimentos | ✅ alto rigor; ⚠️ validez ecológica (tareas de laboratorio) | ✅ replicado en 40 sets | 🟢 Alto (define cómo NO promediar la curva) |
| Alliger & Janak, 1989 | Revisión crítica empírica | 🟢 sí | múltiples estudios revisados | ✅ | — | 🟢 Alto (limita qué se puede asumir del modelo) |
| Bates, 2004 | Teórico/crítico | 🟢 sí | — | ✅ | — | 🟡 Medio (uso formativo, no indicador directo) |
| Reio et al., 2017 | Revisión crítica | 🟢 sí | — | ✅ | — | 🟡 Medio |
| Ericsson et al., 1993 | Observacional (comparación de grupos de expertise) | 🟢 sí | violinistas, N moderado | ⚠️ autorreporte retrospectivo de horas de práctica | — | 🟢 Alto (define qué cuenta como práctica deliberada) |
| Macnamara et al., 2014 | Meta-análisis | 🟢 sí | cientos de estudios primarios | ⚠️ definición de "práctica deliberada" en disputa | — | 🟢 Alto (matiza expectativas para "profesiones") |
| Cepeda et al., 2006 | Meta-análisis | 🟢 sí | 839 evaluaciones / 317 experimentos | ✅ | ✅ | 🟢 Alto (informa diseño de refuerzo espaciado) |
| Murre & Dros, 2015 | Experimental (replicación clásica) | 🟢 sí | N=1 (método de ahorros clásico) | ⚠️ validez ecológica baja para conocimiento comercial | ✅ replica Ebbinghaus 1885 | 🟡 Medio (forma general, no cifras exactas) |
| Agnihotri et al., 2023 | Revisión de literatura | 🟢 sí | 50+ años de literatura | ✅ | — | 🟢 Alto (matiza "cantidad de uso" como proxy) |
| Good et al., 2022 | Meta-análisis | 🟢 sí | 293 efectos / 127 estudios / N=77.560 | ✅ N grande; ⚠️ desempeño a veces autorreportado | ✅ | 🟡 Medio (contexto de motivación, no de curva directamente) |
| Bridge Group / Brandon Hall (benchmarks industria) | Reporte de industria | ⚪ no aplica | no auditable | ⚠️ definiciones de "ramp" no estandarizadas entre reportes | ⚠️ | 🟠 Bajo (orden de magnitud únicamente) |
| "79% HRDQ 2023" / "90% Ebbinghaus 30 días" | — | 🔴 no verificable — probable cifra fabricada/mal atribuida | — | ❌ | ❌ | 🔴 Descartada — no usar |

## 9. Limitaciones de la búsqueda

- No se accedió al texto completo de Newell & Rosenbloom (1981) ni de Ericsson et
  al. (1993) más allá de resúmenes y trabajo derivado — el detalle metodológico
  exacto (tamaños de muestra precisos, análisis estadístico completo) no se
  verificó línea por línea.
- La fuente sobre "piecewise power laws in individual learning curves" (PMC) se
  detectó pero no se pudo verificar autoría/año con confianza suficiente para
  citarla — queda como pista de seguimiento, no como fuente registrada.
- El artículo específico sobre validez/confiabilidad del mystery shopping
  (van der Wiele et al.) se detectó pero la autoría/año exactos no se verificaron
  con precisión total — mismo tratamiento: pista, no cita cerrada.
- No se encontró literatura peer-reviewed que aplique **directamente** la power
  law/exponential law de práctica a un contexto de venta consultiva o asesoría
  financiera — toda la evidencia de la sección 2 es de tareas de laboratorio
  cognitivo; la extrapolación a "curva de aprendizaje de un asesor" en la sección 1
  (veredicto) es una recomendación de diseño propia de este node, no un hallazgo
  replicado en el dominio de ventas.
- No se buscó literatura específica de e-learning/LMS para venta de seguros en
  Perú/LatAm — el foco fue la teoría general de curva de aprendizaje, evaluación de
  capacitación y sales enablement, no el contexto peruano de seguros (para eso,
  ver `[[seguros-comportamiento-mundo-peru]]` y `[[transicion-venta-fria-a-opt-in]]`).

## Conexiones

- [[transicion-venta-fria-a-opt-in]] — el asesor y su transición de venta fría a
  opt-in es el mismo actor cuya curva de aprendizaje mide este node.
- [[material-visual-venta-consultiva]] — el material que la herramienta guía usa
  como referencia (parámetros de producto, guiones) es lo que este node mide que el
  asesor aprenda a usar.
- [[proyecto-back-to-basics-ffvv-vida]] — el playbook del asesor y la Universidad
  Vida de este proyecto son el contexto organizacional donde una herramienta guía
  con curva de aprendizaje medible podría desplegarse.
- [[evaluacion-calidad-agentes-conversacionales-ia]] — si la herramienta guía tiene
  componente conversacional/IA, las escalas de calidad de ese node complementan la
  medición de nivel 3 (conducta) de Kirkpatrick.
