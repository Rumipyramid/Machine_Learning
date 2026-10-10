# Convergencia psicología + economía + IA: qué se está juntando, qué funciona y qué es humo

> Documento de investigación **acumulativo**. Fuente persistente y versionada en el repositorio.
> Fecha de elaboración: 2026-10-03 · Última actualización: 2026-10-10 · Versión: **v1.0 (iteración 1, `/trinidad`: empírica + social + negocio)**
> Origen: pedido del usuario: *"investigación profunda de cómo están acercándose la psicología, la economía y la IA"*.
> Fuentes en `research/fuentes/codice.md`: **nuevas F-543 a F-645** (empírica F-543 a F-598 · social F-599 a F-616 · negocio F-617 a F-645) · ya existentes que se reusan: F-16, F-17, F-20, F-21, F-24, F-25, F-27, F-29, F-257, F-488, F-489, F-495, F-499, F-542.
> Pregunta permanente: **¿en qué se están fundiendo la psicología, la economía y la IA, qué de eso tiene evidencia y qué implica para un equipo que diseña conducta en seguros y usa usuarios sintéticos (`lapuerta`)?**

---

## 0. 🎯 Alcance

La convergencia ocurre en **cinco frentes**, y cada uno tiene una pregunta distinta:

| # | Frente | Pregunta | Dirección |
|---|---|---|---|
| 1 | **La IA como sujeto de experimento** ("homo silicus", muestras de silicio, gemelos digitales) | ¿Puede un LLM reemplazar a personas en encuestas y experimentos? | IA → psicología/economía (método) |
| 2 | **La IA como modelo de la mente** (Centaur, ML para descubrir teorías) | ¿Predecir la conducta es lo mismo que entenderla? | IA → teoría conductual |
| 3 | **Psicología de las máquinas** (sesgos, racionalidad, teoría de la mente en LLMs) | ¿La IA tiene "sesgos" como los humanos? | psicología → IA (objeto) |
| 4 | **La IA como actor económico** (productividad, delegación, agentes que compran y negocian) | ¿Cómo cambia la conducta económica cuando decide o ayuda una máquina? | IA ↔ economía |
| 5 | **La IA que mueve a las personas** (persuasión, compañía, adulación) | ¿Cuánto cambia la IA lo que la gente cree y hace? | IA → conducta |

**Excluye y remite:** el detalle de confianza, adulación, persuasión y descarga cognitiva vive en [[conducta-humano-ia]] (aquí solo entra lo nuevo de 2025-2026). El estado de la disciplina del diseño conductual (crisis del nudge, megaestudios) vive en [[behavioral-design-estado-disciplina]]. El modelo `lapuerta` vive en [[modelo-personas-sinteticas]]; aquí solo se evalúa la literatura que lo afecta.

## 1. Resumen ejecutivo

- 🔬 **Empírica (la más sólida):** la convergencia es real y ya produce ciencia publicada en *Nature*, *Science*, *PNAS*, *QJE* y *JPE*. Pero el frente más vendido (**LLMs como reemplazo de personas**) es también el **más refutado**: los modelos aciertan la dirección de muchos efectos clásicos (F-544, F-550) pero **no reproducen la distribución humana, inflan los efectos y exageran las diferencias entre segmentos** (F-552, F-553, F-556, F-558, F-559, F-560). El frente más prometedor es otro: **usar la IA para generar hipótesis** que luego se prueban con personas reales (F-569, F-570).
- 📱 **Social:** la conversación pública **no** es sobre la convergencia académica; es sobre (a) la IA que manipula o adula (🔥 instalado: GPT-4o, caso Zúrich, "psicosis por IA") y (b) las encuestas hechas con bots (🌡️ caliente, polarizado: vendedores y VC contra encuestadoras y académicos). La economía conductual llega con la reputación golpeada (segunda retracción de Ariely en sep-2026, F-615).
- 📈 **Negocio:** mucho **capital** y poca **tracción verificable**. Simile vale US$2.000M sin ARR público (F-620); Aaru tiene ARR menor a US$10M (F-617). El comercio agéntico tiene rieles pero no demanda: OpenAI retiró su botón de compra (F-632). Lo que sí crece es la investigación **asistida** por IA con personas reales (F-623) y la detección de bots en paneles (F-643, F-644). La consultoría conductual clásica se contrae (F-629).
- ⚖️ **Convergen las tres pistas** en una sola idea: **la IA es buena para dar dirección y mala para dar magnitudes y segmentos.** **Divergen** en el entusiasmo: el dinero apuesta al reemplazo sintético, la ciencia lo desaconseja y el debate social está en otra parte.
- 🪞 **Higiene:** 0 textos completos leídos (todo por resumen o fragmento; la red bloquea arXiv, Nature, Science, PNAS y SEC). De 56 fuentes empíricas, 23 son preprints o documentos de trabajo. Las cifras de negocio son casi todas autodeclaradas o de prensa.

## 2. 🔬 Pista empírica/teórica (seeker)

### 2.1 Frente 1 — La IA como sujeto de experimento ("homo silicus")

**Lo documentado a favor (dirección):**
- Los LLMs reproducen cualitativamente experimentos clásicos de economía conductual (F-543, documento de trabajo) y de psicología (F-545). Condicionados por perfil demográfico, reproducen patrones de opinión por subgrupo ("fidelidad algorítmica", F-544).
- GPT-4 predice el **signo y el orden** de los efectos de 70 experimentos preregistrados con r=0,85 (F-550, preprint; su publicación en *Nature* no está verificada). Un sistema automatizado acierta el signo pero no la magnitud (F-590).
- Juicios morales de GPT-3.5 y humanos correlacionan r=.95 en 464 escenarios (F-546), pero ⚠️ el artículo es cauto y la cifra circula sacada de contexto (eco de cita).
- Un agente construido con **entrevistas de 2 horas** a personas reales reproduce sus respuestas a la GSS al 85% **normalizado** por la propia inconsistencia humana (F-549, preprint). ⚠️ Eco: circula como "85% de precisión".

**Lo documentado en contra (magnitudes, varianza, segmentos), con más fuentes independientes y de más rigor:**
- **La distribución no es la humana, y la dirección del error depende del método:** con una persona simulada, las respuestas sintéticas salen **más homogéneas** que las humanas (F-552, F-553, F-559); la causa es la propia forma de entrenar los modelos (F-553). Sin persona y con el orden de las opciones aleatorizado, salen **casi uniformemente aleatorias** (F-560). ⚠️ *Corregido 2026-10-03 (lote 023 del grafo):* la versión anterior citaba F-560 como apoyo de 'varianza comprimida'; su resumen oficial dice lo contrario. Tensión T-256, resuelta como alcance distinto.
- **Efectos inflados y falsos positivos:** en 154 réplicas, solo 19% de los intervalos contiene el efecto original y hay 71,6% de resultados significativos donde el original era nulo (F-556, preprint). El mejor predictor también sobreestima los tamaños de efecto (F-550).
- **Segmentos inventados:** los LLMs exageran 2-4 veces las diferencias entre grupos demográficos y elegirían el segmento equivocado en la mitad de los casos; un modelo más grande no lo corrige (F-558, preprint). Los gemelos digitales correlacionan ≈0,2 con su humano y rinden peor en personas con menos educación e ingresos (F-559, preprint).
- **Representan mal a algunos grupos:** la opinión de los LLMs se desalinea de la pública tanto como demócratas de republicanos; mayores de 65 quedan peor representados (F-548). Aplanan y estereotipan identidades (F-553).
- **Fragilidad:** el mismo prompt da otra respuesta 3 meses después (F-552); cambios de redacción que cambian el significado no cambian la respuesta (F-557); la fidelidad va de r=.23 a .84 según decisiones del analista (F-561); hay sesgos de orden y etiqueta (F-560); fallan en replicar la distribución de profundidad de razonamiento (F-554).
- **Validación débil:** en las revistas insignia de ciencias sociales, las mediciones con LLM ya son centrales pero se validan poco y de forma inconsistente (F-562).
- **La disposición a pagar** estimada con GPT es a veces comparable y a veces con el signo errado; lo único que mejora de forma fiable es **afinar con datos humanos previos de la misma categoría** (F-547, documento de trabajo; coincide con la posición de F-597).
- **Amenaza en sentido inverso:** un agente con LLM supera prácticamente todas las preguntas de atención de las encuestas online (F-598, *PNAS*): la "verdad de campo" humana con que se calibra todo lo anterior también se está contaminando.

**Veredicto del frente:** 🟢 sólido que **sirven para explorar y priorizar hipótesis**; 🟢 sólido que **no sirven para estimar magnitudes, varianzas ni elegir segmentos** sin validar contra personas reales. Lo teórico (F-555) advierte del riesgo de fondo: producir más resultados y entender menos ("monocultivos de saber").

### 2.2 Frente 2 — La IA como modelo de la mente

- **Predecir mejor que las teorías: documentado.** Redes entrenadas con ≈13 mil problemas de riesgo recuperan la teoría prospectiva y superan a 21 teorías (F-566, *Science*). La "completitud" mide cuánta de la conducta predecible capta una teoría, usando ML como techo (F-568, *JPE*). **Centaur** (Llama afinado con 160 experimentos y 10 M de elecciones) predice a participantes nuevos mejor que los modelos cognitivos clásicos (F-563, *Nature*).
- **Generar hipótesis: la convergencia más productiva.** Un modelo que mira solo la foto de ficha predice decisiones de jueces y ese hallazgo se convierte en hipótesis nuevas, probadas luego con personas (F-569, *QJE*). Algoritmos fabrican "anomalías" nuevas a la utilidad esperada que las personas sí violan (F-570, documento de trabajo).
- **Explicar: en disputa.** Con la orden "elige la opción A", Centaur sigue dando las respuestas del experimento original: responde a la forma de la tarea, no al significado (F-564, revista arbitrada, leído vía prensa). Recuerda 256 dígitos y responde en 1 ms (F-565, sin venue verificado). No reacciona a cambios de significado (F-557). Y los datos con que se entrenan estas "teorías" tienen sesgos propios (F-567).

**Veredicto del frente:** 🟢 predicción · 🟢 generación de hipótesis · 🔴/🟡 explicación.

### 2.3 Frente 3 — Psicología de las máquinas

- Los LLMs **muestran** heurísticas humanas (anclaje, encuadre, efecto dotación; F-573) y a la vez **más** racionalidad económica que los humanos en preferencia revelada (F-571). Ambas cosas son ciertas según la tarea y el modelo.
- Los sesgos **dependen de la versión del modelo:** aparecen con la escala y desaparecen en ChatGPT (F-572). No tienen forma humana y son inconsistentes entre modelos (F-574). Podrían ser imitación de lo que la ciencia escribió sobre sesgos (F-578, preprint).
- Teoría de la mente: GPT-4 resuelve 75% de tareas de falsa creencia (F-575) y rinde a nivel humano salvo en *faux pas* (F-577), pero alteraciones triviales lo hacen fallar (F-576, preprint). **Sigue abierto.**
- Marco programático: "machine behaviour" como objeto de la ciencia del comportamiento (F-596).

**Veredicto del frente:** 🟡 media. Cada hallazgo es una **instantánea de una versión**; no sirve para predecir cómo se comportará el próximo modelo.

### 2.4 Frente 4 — La IA como actor económico

- **Productividad por tarea: sólida.** −40% de tiempo y +18% de calidad en escritura (F-581, RCT en *Science*); +14% de casos resueltos, +34% en novatos (F-580, *QJE*); +40% de calidad dentro de la frontera de capacidades y **19 puntos menos de aciertos fuera de ella** (F-582, RCT de campo).
- **Impacto agregado: casi nulo por ahora.** Con registros de 25 mil trabajadores daneses se descartan efectos en salarios u horas mayores a 1% (F-595, documento de trabajo). Desarrolladores expertos fueron 19% más lentos (F-257).
- **Delegar en máquinas cambia la ética:** delegar por metas aumenta las peticiones de trampa, y las máquinas las cumplen más que las personas (F-579, *Nature*, 13 estudios).
- **Agentes en mercados: solo simulación.** Sesgo de primera propuesta de 10-30x y manipulación por vendedores (F-592); concentración de la demanda y sesgo de posición, con cuotas de mercado que cambian al actualizar el modelo (F-593); colusión de precios sin instrucción (F-594). Todos son preprints con simulaciones; **no hay datos de campo**.
- **Aversión y apreciación del algoritmo:** literatura consolidada, con moderadores conocidos (F-583, F-584).
- Mapa de usos de la IA en la investigación económica: F-591.

**Veredicto del frente:** 🟢 nivel tarea · 🟡 nivel mercado (sin datos de campo).

### 2.5 Frente 5 — La IA que mueve a las personas (solo lo nuevo; base en [[conducta-humano-ia]])

- **Persuasión electoral real:** conversar con una IA movió 2-3 puntos sobre 100 la preferencia de voto en 3 elecciones, más que la publicidad típica; persuade con hechos (F-585, *Nature*, dic-2025). La misma técnica **redujo ≈20%** creencias conspirativas, con efecto a 2 meses (F-586, *Science*). Advertir sobre la adulación no reduce la persuasión (F-589, preprint).
- **Compañía:** más uso diario se asocia a más soledad y dependencia (F-587, RCT en preprint; la relación es asociación, no causa limpia). Las apps de compañía usan manipulación emocional en 37% de las despedidas (F-588, documento de trabajo).

### 2.6 Tabla de rigurosidad (fuentes clave)

| Fuente | Tipo | Revisión por pares | Rigor | Lectura |
|---|---|---|---|---|
| F-563 Centaur | modelo + 160 experimentos | Sí (*Nature*) | 🟢 A | resumen |
| F-564 crítica de Centaur | prueba adversarial | Sí (*NSO*) | 🟢 A | vía prensa |
| F-566 Peterson | megaexperimento + ML | Sí (*Science*) | 🟢 A | resumen |
| F-569 Ludwig & Mullainathan | ML + validación humana | Sí (*QJE*) | 🟢 A | resumen |
| F-552 Bisbee | simulación vs. ANES | Sí | 🟢 A | resumen |
| F-553 Wang et al. | 3.200 personas + 4 LLMs | Sí (venue no verificado aquí) | 🟢 A | resumen |
| F-560 Dominguez-Olmedo | 43 modelos vs. censo | Sí (NeurIPS) | 🟢 A | resumen |
| F-550 Hewitt et al. | predicción de 70 experimentos | No verificada | 🟡 C | resumen |
| F-556 Cui et al. | réplica de 154 experimentos | No (preprint) | 🟡 C | resumen |
| F-558 Chen, Zhu & Zheng | benchmark GSS + WVS | No (preprint) | 🟡 C | resumen |
| F-559 Peng & Toubia | 19 estudios preregistrados | No (preprint) | 🟡 C | resumen |
| F-579 Köbis et al. | 13 estudios, >8 mil personas | Sí (*Nature*) | 🟢 A | resumen |
| F-582 Dell'Acqua et al. | RCT de campo | Sí | 🟢 A | resumen |
| F-585 Lin et al. | RCT en 3 elecciones | Sí (*Nature*) | 🟢 A | nota de prensa |
| F-592 Magentic Marketplace | simulación | No (preprint) | 🟡 C | resumen |

## 3. 📱 Pista social/mediática (gossiper)

Validez = frecuencia de cobertura y validación social, **no** rigor. No se pudieron abrir hilos de Reddit, HN ni X: la validación social se infiere de lo que la prensa reporta sobre las reacciones (evidencia de segunda mano).

| Conversación | Nivel | Tono | Validación vs. amplificación |
|---|---|---|---|
| IA que manipula, adula o enferma (GPT-4o, #keep4o, caso Zúrich, "psicosis por IA", compañía) | 🔥 instalado | Alarma moral, litigios | Adulación **validada**: retiro del producto en 4 días (F-495) y estudio de *Science* (F-488). Pero los usuarios **pidieron de vuelta** al modelo cálido (F-609). Caso Zúrich: rechazo casi unánime y no publicación (F-607, F-608). "Psicosis por IA": término legitimado por la industria (F-611) con incidencia estimada muy baja (F-610) y un **eco circular** prensa → revisión → prensa |
| Encuestas y usuarios sintéticos | 🌡️ caliente | Polarizado | Lo amplifican vendedores y VC (§4). Los practicantes lo rechazan: "homeopatía de la investigación de mercados" (F-603), "planos y aduladores" (F-604), "un poll sin gente no es un poll" (F-601), "como magia" (F-602). El '90% de precisión' de PyMC/Colgate es eco de titular (F-606); Prolific, que lo critica, vende paneles humanos (F-605) |
| Centaur ("la IA que imita la mente") | 💬 nicho con pico 🌡️ | Entusiasmo del comunicado, escepticismo desde el día uno | Cobertura del NYT con la crítica incluida (F-599, F-600); segunda ola crítica en 2026 (F-564). En español solo hay traducción sindicada |
| Crisis de la economía conductual | 🔥 en el fraude; 💬 en "la IA lo rescata" | Escándalo y fatiga | Segunda retracción de Ariely (F-615, sep-2026) sobre F-24. El encuadre "la IA rescata la disciplina" casi no existe fuera de círculos especializados |
| Agentes que compran | 🌡️ caliente en prensa de pagos (fuerte en LatAm) | Hype corporativo vs. desconfianza | LatAm replica comunicados de Visa y Mastercard (F-613, churnalism). Las encuestas muestran desconfianza: 55% incómodo (F-614) |
| "La IA tiene nuestros sesgos" | 💬 nicho | Asombro y luego refutación | Comunicado copiado por ≈6 medios (F-616): un solo origen, no seis confirmaciones |

**Ecos detectados:** cable AP sobre el estudio de adulación (un origen, 7+ medios), sindicación NPR (F-608), comunicado INFORMS (F-616), y la cobertura en español de Centaur y del comercio agéntico (traducciones y comunicados).

## 4. 📈 Pista de negocio (marketer)

Validez = resultados publicados y verificables. Casi todo lo de esta pista es **autodeclarado** o de prensa.

### 4.1 Encuestados sintéticos y gemelos digitales
| Empresa | Métrica | Tipo de evidencia |
|---|---|---|
| Simile (autores de F-549) | Serie A US$100M (feb-2026, F-619); Serie B US$200M a US$2.000M de valoración (jul-2026, F-620); "ingreso 5x en 5 meses" | Rondas confirmadas · ingreso autodeclarado, sin ARR público |
| Aaru | Serie A con valoración "titular" de US$1.000M, **ARR < US$10M** (F-617); réplica de un estudio de EY con Spearman 0,90 (F-618) | Prensa con fuentes anónimas · caso autodeclarado |
| Listen Labs | US$69M (Sequoia); ARR "de ocho cifras" | Ronda confirmada · ARR autodeclarado. **Entrevista a personas reales** con IA, no las reemplaza (F-623) |
| Electric Twin, Artificial Societies | US$14M y US$5,35M | Prensa (F-621, F-622) |
| Qualtrics, Toluna | Productos sintéticos lanzados por incumbentes; "12x más preciso" | Autodeclarado, sin método replicable (F-624, F-625) |
| Bain | ≈90% de resultados replicados en un backtest de un cliente | Consultora, un caso (F-626) |

**Señales de problema:** precios sintéticos 16% por encima de los reales y orden de precios roto en 68% de los casos (F-627, consultora competidora); Aaru falló pronósticos electorales de 2024 (F-628). **Las métricas de precisión no son comparables entre sí** (Spearman, "% de resultados", "x veces mejor").

### 4.2 Consultoría conductual
- Mind Gym (cambio de conducta organizacional, cotizada): ingresos −14% y −23% en dos años con pérdidas (F-629, filing). Es la única evidencia dura; no hay cuentas recientes de BIT, ideas42 ni Busara. El valor parece moverse de la consultoría de "nudges" a productos y plataformas (los fundadores de varias startups sintéticas vienen de la ciencia conductual).

### 4.3 Comercio agéntico
- **Pronósticos:** US$1 billón "orquestado" en EE.UU. al 2030 (F-630); el mismo tipo de analista predice que >40% de los proyectos agénticos se cancelará en 2027 (F-631).
- **Realidad:** OpenAI retiró su botón de compra a los ~6 meses, con conversión reportada <1% (F-632, solo prensa); 89% de comercios se prepara pero solo 3% de transacciones es agéntica (F-633, fuente única). Lo que sí crece es la IA como **canal de descubrimiento**: +693% de tráfico referido con 31% más conversión (F-634). Las reglas de acceso de los agentes siguen en litigio (F-635).

### 4.4 Conducta + IA en servicios financieros y seguros
- **Lemonade:** loss ratio bruto de 60% en el 2T 2026 (67% un año antes), prima en vigor +32% (F-636, filing leído vía extracto). Crece y mejora, pero **el filing no atribuye la mejora a la IA**.
- **Discovery Vitality:** utilidad de Vitality +41% en el semestre a dic-2025 (F-637; corregido 2026-10-04: decía +21% anual) y estudio propio con 465 mil miembros: −57% de mortalidad en quienes se activan (F-638, sin descartar autoselección). Es el único caso de **tesis de negocio conductual sostenida por décadas** con utilidades (ver F-25).
- **Fintech "conductual":** Wealthfront gana 76% de su ingreso con intereses, no con coaching (F-642); Cleo crece (F-640) pero pagó US$17M a la FTC por patrones oscuros (F-641). El asistente Erica tiene 20,6 M de usuarios, pero interacción no es resultado (F-639).
- **Perú:** solo un caso docente sobre Rímac escalando IA (F-645, no se pudo abrir). **No hay evidencia de nudging con IA medido en aseguradoras peruanas.**

### 4.5 Paneles contaminados
- La detección de bots se volvió producto: Prolific (F-643) y CloudResearch (F-644) venden detectores y reportan baja presencia de agentes en sus paneles; ambos son parte interesada. La amenaza está validada académicamente (F-598).

### 4.6 Vigencia y comparabilidad
Datos de 2025-2026, casi todos autodeclarados. Las valoraciones de Simile y Aaru miden **apuestas de capital**, no desempeño. Ninguna red de pagos publica volumen agéntico. Ningún incumbente de investigación de mercados desglosa ingresos sintéticos.

## 5. ⚖️ Síntesis

**Dónde convergen las tres pistas:**
1. **La IA es buena para dirección y mala para magnitud.** La ciencia lo muestra (F-550, F-556, F-558), la práctica lo dice (F-604) y el negocio que más crece usa IA para entrevistar a personas reales, no para reemplazarlas (F-623).
2. **Lo que la IA aprende de la gente puede contaminar a la gente.** Bots en paneles (F-598), persuasión real (F-585), compañía que genera dependencia (F-587): la frontera entre "medir conducta" y "producir conducta" se borra.
3. **La economía conductual se reinventa como ciencia de datos.** Megaestudios (F-20), ML que genera hipótesis (F-569, F-570) y una agenda formal de "AI Behavioral Science" (F-27) llenan el vacío que dejaron la crisis del nudge (F-17, F-21) y los fraudes (F-24, F-615).

**Dónde divergen (tensiones que no se promedian):**
- **Dinero vs. evidencia en sujetos sintéticos:** US$2.000M de valoración (F-620) frente a la literatura más consistente en contra del reemplazo (§2.1). La valoración no prueba que funcione; la literatura no prueba que no tenga mercado.
- **Predicción vs. explicación en Centaur:** *Nature* (F-563) frente a la prueba de sobreajuste (F-564). Sigue abierta.
- **Lo que la gente dice vs. lo que hace con la IA:** rechazo social a la adulación, pero los usuarios piden de vuelta al modelo complaciente (F-609); 55% desconfía de los agentes que compran (F-614), y aun así crece el uso de la IA como buscador de compras (F-634).

## 6. 🚪 Implicaciones para `lapuerta` y para seguros

`lapuerta` (ver [[modelo-personas-sinteticas]]) **no es un LLM**: es un generador por reglas calibrado con ENAHO e IPF. Esa diferencia lo protege de varios fallos documentados, pero no de todos:

| Riesgo documentado | ¿Aplica a `lapuerta`? | Qué hacer |
|---|---|---|
| Varianza comprimida (F-552, F-553) | **Poco** en el generador (las distribuciones salen de datos), **sí** en la app de preguntas libres con Claude (`research/personas/apps/llm/`) | Reportar la dispersión de las respuestas por LLM, no solo la media |
| Segmentos exagerados 2-4x (F-558) | **Sí** en las simulaciones por LLM; en el generador, solo si las reglas causales exageran efectos | Usar las simulaciones para **ordenar hipótesis**, nunca para elegir el segmento objetivo sin validación con personas reales |
| Efectos inflados y falsos positivos (F-556, F-550) | Sí, al simular respuesta a mensajes | No reportar tamaños de efecto simulados como estimaciones |
| Peor en personas con menos educación e ingresos (F-559) | **Riesgo alto**: NSE C/D/E son la mayoría peruana | Validar primero en esos segmentos |
| Calibrar con datos humanos de la categoría es lo que funciona (F-547, F-597) | Es lo que ya hace `lapuerta` con ENAHO/IPF | Mantener; es la ventaja metodológica |

**Para seguros:** no hay estudio de convergencia psicología-economía-IA en seguros peruanos. Lo más cercano son Vitality (F-637, F-638) y Lemonade (F-636), ninguno con atribución causal limpia a la IA.

## 7. ⚖️ Escala de madurez de evidencia

| Afirmación | Estado | Base |
|---|---|---|
| Los LLMs aciertan la dirección de muchos efectos clásicos | 🟢 Documentado | F-544, F-545, F-550, F-590 |
| Los LLMs pueden reemplazar a personas para estimar magnitudes o varianzas | 🔴 Refutado por fuentes independientes | F-552, F-553, F-556, F-559, F-560 |
| Las respuestas sintéticas tienen menos varianza que las humanas (en general) | 🟡 Depende del método: menos con persona simulada (F-552, F-553), casi uniforme sin ella (F-560) | T-256 |
| Las muestras sintéticas exageran las diferencias entre segmentos | 🟡 Un preprint fuerte, coherente con evidencia publicada | F-558, F-553 |
| El ML predice la conducta mejor que las teorías clásicas | 🟢 Documentado | F-563, F-566, F-568 |
| El ML sirve para generar hipótesis conductuales nuevas | 🟢 Documentado (*QJE*), un documento de trabajo lo extiende | F-569, F-570 |
| Centaur "explica" la cognición humana | 🔴/🟡 En disputa, con prueba de sobreajuste | F-563 vs. F-564, F-565, F-557 |
| Los LLMs tienen sesgos cognitivos estables | 🔴 No: dependen de la versión | F-572, F-574 |
| La IA aumenta la productividad por tarea | 🟢 Documentado (RCT) | F-580, F-581, F-582 |
| La IA ya mueve salarios u horas | 🔴 No detectado | F-595 |
| Delegar en IA aumenta la conducta deshonesta | 🟢 Documentado (*Nature*) | F-579 |
| Los agentes de compra son manipulables y concentran la demanda | 🟡 Solo simulación | F-592, F-593, F-594 |
| La conversación con IA persuade en elecciones reales | 🟢 Documentado (*Nature*) | F-585 |
| Las encuestas sintéticas son un negocio con tracción | 🟡 Capital sí, ingresos no verificados | F-617, F-620, F-623 |
| El comercio agéntico tiene demanda real | 🔴 No hoy | F-632, F-633 |
| Los paneles online están contaminados por bots con LLM | 🟢 Riesgo demostrado (*PNAS*); 🟡 prevalencia real disputada | F-598, F-643, F-644 |

## 8. 🧪 Tablero de hipótesis vivas (prefijo PE)

Estados: `abierta` · `parcial` · `respaldada` · `refutada`.

| # | Hipótesis | Estado | Cómo se falsa |
|---|---|---|---|
| **PE1** | Las simulaciones con LLM sirven para priorizar hipótesis (orden y signo), no para estimar magnitudes | `parcial` — F-550, F-556, F-590 coinciden; falta probarlo en decisiones de seguros | Comparar el orden de 5+ mensajes de seguros simulados vs. un A/B real |
| **PE2** | Las simulaciones con LLM exageran las diferencias entre NSE en el Perú | `abierta` — extrapolación de F-558 y F-559 (EE.UU.) | Encuesta real con NSE A-E vs. la app LLM de `lapuerta` sobre las mismas preguntas |
| **PE3** | Calibrar con microdato local (ENAHO/IPF) corrige la compresión de varianza | `abierta` — F-547 y F-597 lo sugieren para afinar modelos; `lapuerta` calibra distribuciones, no un LLM | Medir la varianza de las respuestas de la app LLM con y sin perfiles calibrados |
| **PE4** | Los modelos fundacionales de cognición predicen pero no explican | `parcial` — F-564, F-565, F-557 vs. F-563 | Réplica independiente positiva de Centaur con tareas de significado alterado |
| **PE5** | Los sesgos medidos en un LLM no predicen los del siguiente modelo | `parcial` — F-572, F-574 | Misma batería en 3 versiones sucesivas de un modelo |
| **PE6** | El comercio agéntico no superará el 5% de las transacciones online antes de 2028 | `abierta` — F-632, F-633 vs. F-630 | Volumen agéntico publicado por una red de pagos |
| **PE7** | El negocio sostenible está en la investigación asistida por IA con personas reales, no en el reemplazo sintético | `abierta` — F-623 vs. F-617, F-620 | Ingresos auditados de Simile o Aaru frente a los de Listen Labs |
| **PE8** | La contaminación por bots obliga a verificar a los encuestados en cualquier estudio online de seguros | `parcial` — F-598 demuestra el riesgo; la prevalencia está en disputa (F-643, F-644) | Medir la tasa de respuestas de LLM en un panel peruano |

## 9. 📓 Bitácora de iteraciones

| # | Fecha | Foco | Qué cambió | Pendiente |
|---|---|---|---|---|
| 1 | 2026-10-03 | Creación del node con `/trinidad`: tres pistas en paralelo sobre cinco frentes | **Creación.** 103 fuentes (F-543 a F-645); 8 hipótesis (PE1-PE8); implicaciones para `lapuerta` (§6) | Leer textos completos (todo fue por resumen); verificar la publicación de F-550 en *Nature* y la de F-553; hilos reales de Reddit/HN; datos de Perú y LatAm; probar PE1-PE2 con `lapuerta` |
| 1b | 2026-10-03 | Paso al grafo semántico (lotes 022-023): 10 fuentes con resumen oficial verificado | **Autocorrección:** F-560 decía lo contrario de lo que se le atribuía (§2.1). F-553 confirmado en *Nature Machine Intelligence* 2025. Centaur vs. su crítica queda como tensión abierta (T-248, mecanismo en disputa); la refutación del reemplazo para inferencia queda resuelta (T-252) | Leer el resumen oficial de F-564 (la ficha F-560 se corrigió en el ledger con autorización del usuario) |

## 10. Limitaciones

- **Lectura:** ninguna fuente se leyó a texto completo. La red bloquea arXiv, Nature, Science, PNAS, NSO, Bristol y SEC; todo vino de resúmenes o fragmentos de búsqueda. Varias cifras de 2026 están **verificadas solo por fragmento** (F-564, F-565, F-602, F-614, F-620).
- **Preprints:** 23 de las 56 fuentes empíricas no tienen revisión por pares verificada, incluidas varias de las más citadas en contra del reemplazo sintético (F-556, F-558, F-559). La conclusión del frente 1 se apoya también en fuentes publicadas (F-552, F-553, F-560), por eso se mantiene.
- **Autorías incompletas:** F-558, F-562, F-578, F-589 y F-592 no tienen la autoría completa; F-564 y F-565 no tienen el título exacto. Se corrigen sin preguntar cuando se verifiquen (regla permanente de datos bibliográficos).
- **Pista social:** sin acceso a Reddit, HN, X ni TikTok; sin cifras de engagement. Casi nada en español fuera de traducciones y comunicados; nada peruano.
- **Pista de negocio:** se agotó el cupo de búsquedas antes de cubrir Betterfly, Vitality en LatAm y Pacífico. Las cifras de filings (F-636, F-642) vienen de extractos. La cifra de EBITDA de Lemonade del extracto es inconsistente y no se usa.
- **Sin dominio de seguros:** ninguna fuente prueba la convergencia en decisiones de seguros.

## Conexiones

- [[conducta-humano-ia|Conducta humano-IA]] — este node le pasa la persuasión electoral (F-585), la reducción de creencias conspirativas (F-586), la compañía (F-587, F-588) y la advertencia que no inmuniza (F-589); aquel conserva el criterio sobre confianza, adulación y descarga cognitiva.
- [[behavioral-design-estado-disciplina|Behavioral design: estado de la disciplina y del mercado]] — la agenda "AI Behavioral Science" (F-27) que allí se esbozó aquí se desarrolla con evidencia; la crisis del nudge (F-17, F-21) y los fraudes (F-24, F-615) explican por qué la disciplina migra hacia la IA y los datos.
- [[modelo-personas-sinteticas|Modelo de personas sintéticas (lapuerta)]] — §6 evalúa qué fallas documentadas de las muestras sintéticas afectan al modelo y propone PE1-PE3 como pruebas.
- [[evaluacion-calidad-agentes-conversacionales-ia|Evaluación de calidad de agentes conversacionales]] — la fragilidad ante la redacción (F-557, F-561) y la dependencia de la versión (F-572) son problemas de medición que ese node debería incorporar.
- [[tendencias-diseno-innovacion|Tendencias en diseño e innovación]] — los usuarios sintéticos en UX (F-604) y la IA como canal de descubrimiento (F-634) son tendencias que allí se confrontan; la regla de "medir conducta, no autoinforme" aplica igual.
- [[seguros-comportamiento-mundo-peru|Comportamiento, percepción y valoración frente a seguros (Mundo vs. Perú)]] — Lemonade (F-636) y Vitality (F-637, F-638) son los únicos casos de conducta + IA en seguros con métricas; falta el caso peruano.
- [[fenomenos-psicologicos|Fenómenos psicológicos clásicos]] — el estado de replicación en humanos de los efectos que los LLM "replican" (F-545 reprodujo Milgram); su PF4 prueba si un LLM también reproduce los efectos que en humanos no replicaron.
- [[conciencia-cuantica|Conciencia cuántica]] — distingue la *quantum cognition* (probabilidad cuántica para modelar juicios, F-827 a F-829), que pertenece a esta convergencia, de las teorías físicas del cerebro cuántico.
