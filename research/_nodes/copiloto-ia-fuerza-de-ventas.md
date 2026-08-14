# ¿Un copiloto de IA potencia a la fuerza de ventas? Evidencia de 360°

> Documento de investigación. Fuente persistente y versionada en el repositorio.
> Fecha de elaboración: 2026-08-14 · Versión: v1.0
> Origen: `/trinidad` — investigación de 360° (empírica + social + negocio)
> Pregunta original: ¿hay evidencia de que un copiloto de IA potencia a la fuerza de ventas?
> Fuentes registradas en `research/fuentes/codice.md` (F-469 a F-493).

---

## 0. Resumen ejecutivo (TL;DR)

**Veredicto corto: sí, hay evidencia causal real — pero el efecto no es una propiedad de la
herramienta, es una función de tres condiciones, y fuera de ellas el copiloto puede restar.**

La mejor evidencia disponible **no** dice "el copiloto sube las ventas X%". Dice algo más
específico y más útil: el copiloto rinde en proporción a **qué tan mala era la práctica que
sustituye**, rinde distinto **según el nivel del vendedor**, y rinde solo mientras se mantenga
**detrás** del vendedor y no delante del cliente.

- **Pista empírica/teórica:** la más fuerte de las tres. Existe un experimento aleatorizado
  publicado en un journal top **con agentes de venta reales** (Luo et al. 2021, *Journal of
  Marketing*, N=429 agentes de una fintech, F-469): el coach de IA supera al humano en forma de
  **U invertida** — los agentes de rango **medio** ganan más; los de abajo se ahogan en
  **sobrecarga de información** y los de arriba muestran **aversión a la IA**. El mismo paper
  prueba las dos soluciones: **restringir el nivel de feedback** y, sobre todo, **ensamblar IA +
  coach humano**, que superó a cualquiera de los dos por separado. Convergente con el RCT de
  referencia en soporte al cliente (+14% promedio, **+34% en los novatos**, F-470) y con el
  hallazgo incómodo de la frontera irregular: fuera de la zona de competencia del modelo, el
  usuario de IA rinde **19 puntos porcentuales peor** que quien no la usa (F-471).
- **Pista social/mediática:** instalada pero **dividida**, no entusiasta — y con una divisoria
  nítida: el copiloto que *asiste* al vendedor tiene mejor recepción que el agente que *actúa* en
  su nombre. Sentimiento medido sobre herramientas de IA de ventas: **22% positivo / 46%
  mixto-condicional / 32% negativo** (F-477); **83% de una audiencia de líderes de ventas declara
  no haber logrado que los AI SDR funcionen** (F-478); LinkedIn cambió su algoritmo en mayo 2026
  para **suprimir** el "AI slop" (F-479); y las tasas de respuesta en frío caen mientras sube la
  adopción de IA en outreach (F-480). En seguros: los agentes están **curiosos pero todavía no
  confían** — solo 6% de principales de agencia usa IA (F-481).
- **Pista de negocio:** abundante en cifras y **estructuralmente sesgada al alza**. Los números
  grandes (+35% win rate, 468% ROI, 83% vs. 66% de crecimiento) vienen todos de vendors midiendo
  su propio producto, sin aleatorización y sin controlar autoselección (F-482, F-483, F-484). La
  contraevidencia buscada a propósito es dura: **95% de los pilotos de GenAI sin retorno medible
  en P&L** (F-490), **50-70% de churn anual** en herramientas de IA de ventas, y una brecha de
  88% que "adoptó" contra 24% que la tiene embebida en el workflow de ingresos (F-491).
- **Convergencia:** las tres pistas señalan la misma variable moderadora — **dónde se coloca el
  copiloto respecto del cliente**. Asistir al vendedor: respaldado. Reemplazar la conversación:
  penalizado en las tres.
- **Divergencia real, no promediada:** ⚔️ **cuando la evidencia sube de rigor, el efecto baja de
  magnitud.** Vendors sin aleatorización: +26% a +35%. Estudios con asignación aleatoria: **+7% a
  +14%**, con casos documentados de **efecto cero y de efecto negativo**. No se promedian: se
  reporta la brecha, porque la brecha *es* el hallazgo.

---

## 1. 🔬 Pista empírica/teórica

### 1.1 La fuente central: el único RCT publicado sobre coaching de IA a agentes de venta

**Luo, Qin, Fang & Qu (2021), _Journal of Marketing_ 85(2):14-32 (F-469, 🟢A)** es la evidencia
más directa que existe sobre la pregunta. Serie de experimentos de campo **aleatorizados** en
empresas fintech; el Experimento 1 asignó al azar **429 agentes de venta** a entrenamiento en el
puesto con **coach de IA** o **coach humano**.

**Hallazgo principal — el beneficio incremental de la IA tiene forma de U invertida:**

| Segmento de agente | Ganancia incremental de IA vs. coach humano | Por qué |
|---|---|---|
| **Rango bajo** | Limitada | **Sobrecarga de información**: el problema más severo del grupo. La IA les da más feedback del que pueden procesar. |
| **Rango medio** | **La mayor de las tres** | Tienen base suficiente para procesar el feedback y margen suficiente para mejorar. |
| **Rango alto** | Limitada | **Aversión a la IA**: la resistencia más fuerte de los tres grupos frente a un coach humano. |

**Y el mismo paper prueba las dos soluciones, que es lo que lo hace accionable:**

- **Experimento 2:** rediseñar el coach de IA **restringiendo el nivel de feedback** → mejora
  significativa del desempeño de los agentes de rango bajo. El problema no era el modelo, era el
  **caudal**.
- **Experimento 3:** el **ensamblaje IA + coach humano superó a la IA sola y al humano solo.**
  Combina las "habilidades de dato duro" de la IA con las "habilidades interpersonales blandas"
  del manager, y resuelve simultáneamente los dos problemas (sobrecarga abajo, aversión arriba).

> ⭐ **Este es el resultado más importante de todo el node**: la configuración con mejor respaldo
> causal no es "copiloto" ni "coach humano", es **copiloto + humano**, con el caudal de feedback
> calibrado al nivel del vendedor.

### 1.2 El efecto se concentra en los menos hábiles — y hay aprendizaje que persiste

**Brynjolfsson, Li & Raymond (2025), _Quarterly Journal of Economics_ 140(2):889 (F-470, 🟢A)** —
5.179 agentes de soporte, despliegue escalonado de un asistente conversacional basado en GPT:

- **+14% de productividad promedio** (casos resueltos por hora).
- **+34% en novatos y trabajadores de baja habilidad**; efecto **mínimo** en los más
  experimentados, con **pequeñas caídas de calidad** en los de mayor habilidad.
- Efectos secundarios relevantes y poco citados: **mejora el sentimiento del cliente**, **aumenta
  la retención de empleados**, y produce **aprendizaje duradero** (los agentes mejoran incluso sin
  la IA; la adherencia a las recomendaciones sube con el tiempo).
- Mecanismo declarado: la IA **disemina las mejores prácticas de los trabajadores más capaces** y
  acelera el descenso por la curva de experiencia.

⚠️ **Es soporte al cliente, no venta.** La transferencia es razonable (conversación asistida en
tiempo real, misma clase de tarea) pero no es evidencia directa de venta.

### 1.3 El hallazgo incómodo: fuera de su frontera, el copiloto degrada el desempeño

**Dell'Acqua et al. (2025), _Organization Science_ (F-471, 🟢A)** — 758 consultores de BCG (7% de
su fuerza de contribuidores individuales), 18 tareas realistas:

- **Dentro** de la frontera de capacidad del modelo: +12.2% de tareas completadas, **25.1% más
  rápido**, **+40% de calidad** evaluada por humanos.
- **Fuera** de la frontera: los consultores con IA rindieron **19 puntos porcentuales peor**.
  Precisión: **84.5% sin IA → 70.6% con IA → 60% con IA + curso de prompt engineering.**

> ⭐ El curso de prompting **empeoró** el resultado: dio más confianza para usar la IA justo donde
> no correspondía. Esto tiene una implicación directa para cualquier despliegue: **entrenar en
> "cómo usar el copiloto" sin delimitar dónde NO usarlo es contraproducente.**

**Y el usuario no detecta la degradación.** El RCT de METR (F-475, 🔵B) con 16 desarrolladores
experimentados y 246 tareas encontró que fueron **19% más lentos** con IA mientras estimaban haber
sido **20% más rápidos**. La brecha percepción-realidad es de ~39 puntos y va en la dirección
equivocada.

> ⚠️ **Consecuencia metodológica dura: la satisfacción declarada del vendedor con el copiloto no
> es un indicador válido de que el copiloto funcione.** Ninguna encuesta de adopción puede
> detectar este fallo.

### 1.4 El límite que separa "copiloto" de "IA frente al cliente"

**Luo, Tong, Fang & Qu (2019), _Marketing Science_ 38(6):937-947 (F-472, 🟢A)** — experimento de
campo con **6.255 clientes de una empresa de servicios financieros**, llamadas salientes de
renovación de préstamos, aleatorizando **cuándo (o si) el chatbot revelaba ser IA**:

| Condición | Tasa de cierre | Duración de llamada |
|---|---|---|
| Chatbot **sin revelar** | **23.7%** | — |
| Agente humano competente | 25.1% | ~64 seg |
| Agente humano novato | 4.9% | — |
| Chatbot **revelado al inicio** | **4.8%** (**−79.7%**) | **~10 seg** |

El chatbot no revelado era **4x más efectivo que los novatos** y estadísticamente comparable a los
humanos competentes. Revelar que era IA antes de la conversación **destruyó el 79.7% del
desempeño**. Mecanismo: percepción de **menor conocimiento y menor empatía** — subjetiva, no
objetiva (la competencia real del bot no cambió). Mitigable con **revelación tardía** y con
experiencia previa del cliente con IA.

> ⭐ **Este es el dato más duro del corpus para el diseño del producto, y está en servicios
> financieros por teléfono** — casi exactamente el contexto de venta de seguros de vida. Dice que
> el valor se captura poniendo la IA **detrás** del asesor. Delante del cliente, y declarada, el
> costo de confianza es catastrófico. Y ocultarla no es una opción viable: es exactamente el
> mecanismo que dispara el backlash documentado en `futuro-asesores-seguros-venta-digital` §2.

### 1.5 El efecto depende de qué tan mala era la práctica previa (el rango 0%–16.3%)

**Fang, Yuan, Zhang, Donati & Sarvary (2025), arXiv 2510.12049 (F-473, 🔵B, preprint)** —
experimentos de campo aleatorizados a gran escala en una plataforma de retail transfronterizo,
millones de usuarios y productos, **7 workflows** de negocio, 6 meses (2023-2024):

- Efecto sobre ventas: **de 0% a 16.3%**, "dependiendo de la contribución marginal de la GenAI
  **respecto de las prácticas existentes de la empresa**".
- Mecanismo: opera vía **mayor tasa de conversión**, no vía ticket más grande.
- Heterogeneidad: vendedores **más pequeños y nuevos**, y consumidores **menos experimentados**,
  obtienen ganancias desproporcionadamente mayores.

> ⭐ **La lectura correcta del "0%" no es que la IA falle: es que en los workflows donde la
> empresa ya tenía una buena práctica, no había nada que ganar.** El copiloto no crea desempeño —
> sustituye la ausencia de un buen proceso. Es la misma forma del hallazgo de Luo (§1.1: los top
> ganan poco) y de Brynjolfsson (§1.2: los expertos ganan poco), ahora a nivel de *proceso* en vez
> de a nivel de *persona*.

### 1.6 El "humano en el loop" no rescata todos los fallos por igual

**Experimento de campo aleatorizado en Alibaba/Taobao (2026, arXiv 2605.14830, F-474, 🔵B)** — 647
trabajadores de servicio al cliente, 680.676 chats: la IA agéntica **redujo la duración** de los
chats pero **bajó sustancialmente las calificaciones** en los chats elegibles para IA. Y el
hallazgo clave: la supervisión humana **preserva la calidad en escalamientos técnicos**, pero es
**mucho menos efectiva en escalamientos emocionales** — si el cliente ya se frustró o
desconfió durante la interacción con IA, meter un humano después **no repara el daño** (peores
calificaciones y más recontactos).

> Converge con lo que este proyecto ya documentaba desde negocio: quien empieza digital y termina
> escalando a un humano reporta una experiencia **peor**, no neutral (NPS −11 puntos, Bain, F-183
> en [[futuro-asesores-seguros-venta-digital]] §3.2). Dos evidencias independientes, mismo
> patrón: **el rescate humano tardío no es una red de seguridad confiable.**

### 1.7 Capa teórica: la respuesta del cliente cambia según la etapa de venta

**Adam, Roethke & Benlian (2023), _Information Systems Research_ 34(3):1148-1168 (F-476, 🟢A)** —
las respuestas del cliente a agentes automatizados vs. humanos **no son estables a lo largo del
proceso de venta**: cambian conforme el cliente avanza de etapa, con mecanismos distintos en cada
transición. Implicación de diseño: la asignación humano/IA debería decidirse **por etapa del
journey**, no en bloque para todo el proceso.

### Tabla de rigurosidad (pista empírica)

| Fuente | Tipo | Rigor | Aporte |
|---|---|---|---|
| Luo, Qin, Fang & Qu 2021 (F-469) | 3 experimentos de campo aleatorizados, N=429 agentes de venta, *J. of Marketing* | 🟢 A | **U invertida** por nivel + las dos soluciones (restringir feedback; ensamblar IA+humano) |
| Brynjolfsson, Li & Raymond 2025 (F-470) | Despliegue escalonado, N=5.179 agentes, *QJE* | 🟢 A | +14% promedio, **+34% novatos**, +retención, aprendizaje duradero |
| Dell'Acqua et al. 2025 (F-471) | Experimento de campo, N=758 consultores, *Organization Science* | 🟢 A | +40% calidad dentro de la frontera; **−19 pp fuera** |
| Luo, Tong, Fang & Qu 2019 (F-472) | Experimento de campo, N=6.255 clientes, servicios financieros, *Marketing Science* | 🟢 A | Revelar la IA al cliente **−79.7%** de cierre |
| Adam, Roethke & Benlian 2023 (F-476) | Experimental, *Information Systems Research* | 🟢 A | La respuesta del cliente cambia **por etapa de venta** |
| Fang et al. 2025 (F-473) | RCT a gran escala, 7 workflows | 🔵 B (preprint) | Efecto **0% a 16.3%** según la práctica previa |
| Alibaba/Taobao 2026 (F-474) | RCT de campo, N=647 trabajadores | 🔵 B (preprint) | El humano en el loop **no rescata escalamientos emocionales** |
| METR 2025 (F-475) | RCT, N=16 devs, 246 tareas | 🔵 B (N pequeño, sin peer review) | **19% más lentos creyéndose 20% más rápidos** |

---

## 2. 📱 Pista social/mediática

**Nivel de instalación social: 🔥 alto en volumen, 🌡️ tibio en tono.** El tema circula muchísimo,
pero el sentimiento dominante **no es entusiasmo: es condicionalidad**.

### 2.1 La divisoria social: copiloto que asiste ≠ agente que actúa

Es la señal social más consistente encontrada. Un análisis de menciones sobre herramientas de IA
para ventas (F-477, 🟠D) codifica el sentimiento agregado en **22% positivo / 46% mixto o
condicional / 32% negativo** — con las herramientas de tipo **AI SDR** (que actúan en nombre del
vendedor) como las más polarizantes (una de ellas, 18% positivo contra 48% negativo), y las que se
posicionan explícitamente como "capa de aceleración del workflow, no reemplazo" con mejor
recepción. La misma fuente resume que **los copilotos van algo mejor que los AI SDR**.

**Queja dominante, repetida y específica:** personalización superficial (nombre + empresa),
mensajes que "suenan a robot", ausencia de la empatía que construye confianza.

### 2.2 Conducta observable, no opinión: la plataforma legisló contra el "AI slop"

El 20 de mayo de 2026 LinkedIn anunció cambios de algoritmo dirigidos a contenido, comentarios y
automatización de baja calidad generados con IA: no se borran, se **suprimen** más allá de la red
inmediata del autor (F-479, 🟠D). Que la plataforma donde vive el social selling B2B haya
convertido el rechazo al output de IA en **política de producto** es una señal social mucho más
fuerte que cualquier encuesta de opinión — es conducta institucional, no declaración.

### 2.3 La contraparte del comprador: la efectividad del outreach con IA está cayendo

Múltiples mediciones independientes del sector convergen (F-480, 🟠D): las tasas de respuesta a
correo en frío bajaron de ~8.5% (2019) a ~7% (2023), ~5% (2025) y **3-5% entrando a 2026**; otra
serie reporta 6.8% (2023) → **3.4% (inicios 2026)**. Y las actitudes declaradas acompañan:
**~61% dice poder identificar outreach escrito por IA** y **47% de profesionales B2B dice que
respondería *menos* si cree que el email fue generado por IA**.

⚠️ Descuento obligado: **todas estas cifras las publican vendors del propio sector** (plataformas
de outreach, herramientas de email), que tienen incentivo en ambas direcciones. Se registran por
la **convergencia direccional** entre fuentes con incentivos distintos, no por el valor puntual.

> Nótese que esto **no** contradice a Luo 2019 (§1.4) — lo complementa. Aquel muestra que un bot
> *no revelado* rinde como un humano competente; este muestra que cuando el mercado entero
> aprende a detectar el output de IA, la ventaja se erosiona sola. La detectabilidad es el factor
> que se degrada con la adopción masiva.

### 2.4 Lo que sí se sabe de agentes de seguros específicamente

**2024 Agent-Customer Connection Study (F-481, 🟡C)** — 1.133 líderes y equipos de agencias
independientes + 1.110 consumidores:

- Solo **6% de los principales de agencia usa IA hoy**; 36% espera adoptarla en 5 años.
- Sentimiento **partido casi por la mitad** entre "oportunidad" (~25%) y "amenaza" (~27%), con el
  resto neutral o sin opinión.
- Síntesis de los propios autores: los agentes están **"curiosos, pero todavía no confían"** en la
  tecnología.
- Lo que los agentes **quieren** dejar de hacer (tareas administrativas, atención de servicio de
  clientes existentes) coincide exactamente con lo que un copiloto puede absorber — y lo que
  quieren hacer más (prospectar, cross-sell, cotizar) es lo que quedaría liberado.

> ⭐ Esa última coincidencia es la mejor noticia social del node: **el caso de uso que la evidencia
> empírica respalda (absorber carga administrativa detrás del asesor) es exactamente el que los
> propios asesores piden.** No hay que convencerlos de ese caso de uso; hay que no darles el otro.

### 2.5 Lo que no se pudo verificar (declarado explícitamente)

- **No se accedió a conversación primaria de vendedores.** El proxy de red del entorno bloqueó
  Reddit, varios substacks de práctica del gremio y la mayoría de los foros. Todo lo social de
  esta sección viene de **agregadores que reportan sobre lo social**, no de los hilos originales.
  Es exactamente la misma limitación que ya declaró [[futuro-asesores-seguros-venta-digital]] §2
  al buscar debate genuino entre asesores.
- **El "83% no ha logrado que los AI SDR funcionen" (F-478, 🟠D) es una encuesta de audiencia de
  un medio del sector**, no una muestra probabilística. Se registra por la magnitud y por venir de
  una audiencia de líderes de ventas (no de escépticos de la IA), pero no es una estimación
  poblacional.

---

## 3. 📈 Pista de negocio

### 3.1 Las cifras grandes — y por qué todas comparten el mismo defecto

| Fuente | Cifra publicada | Método | Defecto estructural |
|---|---|---|---|
| **Gong Labs** (F-482, 🟠D) | **+35% win rate** (Smart Trackers), **+26%** (Ask Anything) | >1M de oportunidades, **1.418 organizaciones** | **El vendor mide su propio producto** y compara *dentro* de su base: los equipos que activan las funciones de IA plausiblemente ya eran los mejores equipos. **Autoselección no controlada.** La propia empresa aclara que el estudio "está aislado a usuarios de Gong". |
| **Forrester TEI, comisionado por Microsoft** (F-483, 🟠D) | **468% ROI** (alto) / 282% (medio) / **125%** (bajo) | 13 entrevistas en 6 organizaciones + encuesta a 222 empresas | Es un estudio **"New Technology: *Projected*"** — modelado, **no medido**. Comisionado por el proveedor. El rango 125%-468% *es* la admisión de incertidumbre. |
| **Salesforce State of Sales 2026** (F-484, 🟠D) | **83% de equipos con IA reportó crecimiento** vs. **66% sin IA**; 3.7x más probable cumplir cuota | n>4.000 profesionales de ventas | **Autorreporte + correlación pura + conflicto de interés directo** (Salesforce vende Agentforce). No controla tamaño, sector, madurez ni presupuesto: las empresas que crecen son las que pueden comprar IA. |
| **McKinsey** (F-486, 🟠D) | Revenue uplift **3-15%**, ROI de ventas **+10-20%** | No publicada | Mismo defecto que este proyecto ya documentó dos veces en el mismo emisor (F-266, F-439): cifra sin muestra, sin significancia y sin auditoría. |

> ⭐ **Regla de lectura para todo este bloque:** ninguna de estas cifras es aleatorizada. Puestas
> junto a las de §1 (que sí lo son), el contraste es el hallazgo: **+26% a +35% sin control**
> contra **+7% a +14% con asignación aleatoria** — y con casos de efecto cero y negativo.

### 3.2 Adopción real y casos con nombre propio

- **Agentforce (Salesforce)**: ARR superó **US$500M en Q3 FY26**, **+330% interanual**, 9.500
  deals pagados desde el lanzamiento — la rampa de ARR más rápida de un producto en los 26 años
  de la empresa (F-485, 🟡C). Mide **venta del producto**, no desempeño del producto.
- **Morgan Stanley** (F-487, 🟡C): **98% de los equipos de asesores** usa a diario el AI Assistant;
  eficiencia de recuperación documental de **20% → 80%**; la herramienta de resumen de reuniones
  (Debrief) se extendió a móvil y Salesforce. Es el caso más cercano a "copiloto para fuerza de
  venta consultiva de servicios financieros" con adopción verificada a escala. ⚠️ **Adopción no es
  desempeño**: no hay cifra pública de efecto sobre ventas ni contrafactual.
- **Ping An** (F-489, 🟡C): RMB **30.442 millones** de ventas atribuidas a IA en Q1 2026, con
  primas de primer año de vida/salud +45.5%. ⚠️ La **atribución** "impulsado por IA" la hace la
  propia empresa, sin metodología de contrafactual publicada.
- **Seguros, lo más específico encontrado** (F-488, 🟠D): aseguradora nacional de EE.UU. con
  ~**1.500 agentes de primera línea**, con coaching asistido por IA y "next best actions":
  **+7% de conversión de venta**, −5% de AHT, ~6 horas/semana recuperadas por manager, y
  efectividad de coaching en el programa bilingüe de ~51% a >80% en un trimestre. Case study del
  proveedor, sin grupo de control — pero **el +7% es notable por ser el único número de esta pista
  que cae dentro del rango que producen los estudios aleatorizados**, en vez de multiplicarlo.
- **Copiloto de recuperación de información en llamada de seguros** (F-493, 🟡C): sistema
  demostrado sobre un escenario de seguros con 50 productos en 10 categorías — 2.8 segundos de
  respuesta media, **14x más rápido que la búsqueda manual en CRM**, ~5.7 minutos ahorrados en una
  llamada con 10 preguntas del cliente. Mide **latencia de la herramienta**, no conversión.

### 3.3 Contraevidencia buscada a propósito (paso obligatorio)

- **MIT Project NANDA, "The GenAI Divide" (2025, F-490, 🟡C):** pese a US$30-40 mil millones de
  inversión empresarial, **95% de los pilotos de GenAI no produce retorno medible en P&L**; solo
  **5% de las herramientas de IA a medida llega a producción**. Base: 52 entrevistas ejecutivas,
  153 encuestas, 300 despliegues públicos. ⚠️ **Muestra chica y no probabilística** — la cifra
  "95%" se viralizó sin ese matiz. **Diagnóstico de los propios autores: el problema no es la
  calidad del modelo ni la regulación, es el enfoque de implementación.**
- **Churn y adopción hueca (F-491, 🟠D):** **50-70% de churn anual** en herramientas de IA de
  ventas; **88% de los equipos declara haber adoptado IA pero solo 24% la tiene embebida en
  workflows de ingresos**; y en el caso del copiloto horizontal más grande del mercado, **<4.5%
  de los clientes comerciales paga por él y solo 20-30% de esos lo usa semanalmente.**
- **AI SDR vs. humano (F-492, 🔴E):** circula ampliamente que los meetings agendados por IA
  convierten a oportunidad **15% vs. 25%** de los humanos. ⚠️ **Se rastrea a un vendor del propio
  espacio y se cita en cadena entre blogs de vendors sin estudio localizable.** Se registra como
  **cifra de circulación, no como dato** — mismo tratamiento que este proyecto le dio a los
  huérfanos de cita en [[tendencias-diseno-innovacion]] (regla C22).
- **Caso de campo con segmentación por valor (F-478, 🟠D):** una empresa SaaS Serie B reestructuró
  su equipo de 10 SDR alrededor de agentes de IA durante seis meses. Los meetings originados por
  IA con **ACV < US$25K** convirtieron a tasa similar a los humanos; los de **ACV > US$50K
  cerraron a tasa materialmente menor**. Anécdota de un caso, sin auditoría — pero converge
  exactamente con la variable moderadora de complejidad ya documentada en
  [[futuro-asesores-seguros-venta-digital]].

---

## 4. ⚖️ Síntesis

### 4.1 Dónde convergen las tres pistas

**Convergencia 1 — el copiloto rinde en proporción a lo mala que era la práctica previa.**
Empírica: efecto de 0% a 16.3% según la contribución marginal sobre la práctica existente (§1.5);
+34% en novatos contra ~0% en expertos (§1.2); ganancia máxima en el rango medio, no en el alto
(§1.1). Negocio: el único caso de seguros con número creíble reporta +7%, y el salto grande está
en la efectividad de coaching (51%→80%), es decir en el proceso que estaba peor (§3.2). Social:
la queja no es "la IA es mala", es "no aporta nada por encima de lo que ya hacía bien" (§2.1).

**Convergencia 2 — el valor está detrás del vendedor, no delante del cliente.** Empírica: revelar
la IA al cliente cuesta 79.7% del cierre en servicios financieros (§1.4), y el rescate humano
tardío no repara escalamientos emocionales (§1.6). Social: el copiloto que asiste se recibe mejor
que el agente que actúa; la plataforma suprime el output automatizado; el comprador declara que
respondería menos si detecta IA (§2.1-2.3). Negocio: donde hay números creíbles, el copiloto
asiste al humano (Morgan Stanley, la aseguradora de 1.500 agentes); donde reemplaza al humano de
frente, aparecen los 15% vs. 25% y el 83% que no logró hacerlo funcionar (§3.3).

**Convergencia 3 — el problema es de implementación, no de modelo.** Es la conclusión explícita de
los tres registros: MIT lo dice literalmente ("no es calidad del modelo ni regulación, es el
enfoque"); Luo lo demuestra experimentalmente (el mismo modelo, con el feedback restringido,
pasa de no funcionar a funcionar); y el gremio lo dice a su manera (el 88%/24% de adopción
declarada contra embebida).

### 4.2 Dónde divergen — y no se promedia

⚔️ **Divergencia 1: la magnitud del efecto es inversamente proporcional al rigor con que se mide.**
Sin aleatorización (vendors): +26% a +35% de win rate, 125%-468% de ROI. Con asignación aleatoria:
+7% a +14%, con **casos documentados de cero y de negativo**. No se resuelve promediando: la
respuesta honesta a "¿cuánto sube?" es **"entre nada y +14%, según tres condiciones", no "+35%"**.

⚔️ **Divergencia 2: "adoptado", "funcionando" y "rentable" son tres cosas distintas y las tres
pistas miden distintas.** 87% de organizaciones usa IA (negocio) · 83% no logró que los AI SDR
funcionen (social) · 95% de pilotos sin retorno en P&L (contraevidencia). No se contradicen: la
brecha entre **88% que adoptó** y **24% que la tiene embebida en el workflow de ingresos** es la
explicación más económica de las tres cifras a la vez.

⚔️ **Divergencia 3: el copiloto puede empeorar el desempeño sin que nadie lo note.** −19 pp fuera
de la frontera (§1.3) y 19% más lento creyéndose 20% más rápido (§1.3). Esta es la única
divergencia que no está entre pistas sino **entre la medición y la percepción**, y es la más
peligrosa operativamente porque invalida el instrumento con que la mayoría de las empresas evalúa
sus pilotos.

### 4.3 Respuesta directa a la pregunta

**Sí, hay evidencia — de nivel A, aleatorizada, con agentes de venta reales — de que un copiloto
de IA potencia a la fuerza de ventas. Pero la evidencia respalda una configuración específica, no
la idea general:**

1. **IA + coach humano ensamblados**, no IA sola (Luo Exp. 3 — la configuración que ganó).
2. **Caudal de feedback restringido** y calibrado al nivel del vendedor (Luo Exp. 2).
3. **Segmentado por nivel**: el mayor retorno está en el **medio** de la distribución (Luo Exp. 1)
   o en los **menos hábiles** cuando la tarea es de ejecución más que de juicio (Brynjolfsson).
4. **Con la frontera delimitada explícitamente**: dónde NO usarlo importa más que dónde sí
   (Dell'Acqua).
5. **Detrás del asesor, nunca declarado frente al cliente** en el momento de venta (Luo 2019).
6. **Medido contra un contrafactual**, no por satisfacción declarada (METR).

---

## 5. Implicaciones para el proyecto (AIDA / Espacio Digital del Asesor)

Este node no es abstracto para este proyecto: [[proyecto-back-to-basics-ffvv-vida]] ya tiene un
copiloto del asesor (AIDA) como palanca central, y ya documenta un defecto específico.

1. **El defecto conocido es exactamente el fallo que la evidencia predice como más costoso.** La
   **inconsistencia de respuestas del copiloto** — señalada de forma independiente por la encuesta
   a 19 asesores *y* por el Taller de Manejo de Objeciones — es la manifestación operativa del
   hallazgo de §1.3: fuera de su frontera de competencia, el copiloto **resta**. No es un bug de
   pulido: es la condición bajo la cual el signo del efecto se invierte. Su prioridad en el
   backlog (ítem 1, corto plazo) está bien puesta, y ahora tiene respaldo causal externo.
2. **La arquitectura de Back to Basics ya es la que ganó el experimento.** Copiloto + formación +
   mentoría *es* el "ensamblaje IA + coach humano" que superó a ambos por separado (Luo Exp. 3).
   Esto convierte una decisión de diseño en una apuesta respaldada — y desaconseja explícitamente
   la tentación de "centralizar todo en el copiloto" sin el componente humano.
3. **"Centralizar funciones en el copiloto" (ítem 1 del backlog) necesita un límite explícito.**
   El Hallazgo 1 del mapa (sobrecarga del asesor) y el mecanismo de Luo (sobrecarga de información
   en los agentes de rango bajo) son **el mismo problema**. Centralizar sin restringir el caudal
   reproduce el fallo del Experimento 1; restringir el caudal es lo que lo arregló en el
   Experimento 2. Menos feedback, mejor dirigido, no más funciones.
4. **El Plan Piloto (10 asesores) tiene un riesgo de diseño que la evidencia hace evitable.** Si
   el efecto tiene forma de U invertida, **medir el promedio de 10 asesores puede dar cero aunque
   el copiloto funcione muy bien en el segmento medio**. Con N=10 hay que **estratificar por nivel
   de desempeño previo** al asignar y al leer resultados, o el piloto arriesga concluir "no
   funciona" sobre un efecto real.
5. **El indicador de éxito no puede ser satisfacción del asesor.** El taller obtuvo NPS 96.67 y
   99.33% de satisfacción — y aun así los asesores reportaron el defecto de consistencia. METR
   (§1.3) muestra que la percepción de productividad puede ir en dirección opuesta a la
   productividad medida. Se necesita un **indicador de desempeño con comparación**, no una
   encuesta de percepción.
6. **La línea roja está clara y coincide con lo que el proyecto ya decidió.** Copiloto detrás del
   asesor: respaldado por las tres pistas. IA conversando con el cliente en el momento de venta de
   Vida: penalizada con −79.7% de cierre en el contexto empírico más parecido que existe. La
   señal local de RIMAC de "asesor web con IA generativa que duplicó conversión" (autorreportada,
   🟠D, ver [[proyecto-back-to-basics-ffvv-vida]] §2) **no alcanza para cruzar esa línea** —
   es exactamente el tipo de cifra que §3.1 de este node muestra que se desinfla al medirse bien.

---

## 6. Limitaciones

- **No existe ningún RCT publicado de copiloto de IA en venta de seguros.** Lo más cercano es
  fintech con agentes de venta telefónica (F-469) y servicios financieros con renovación de
  préstamos por teléfono (F-472). La transferencia al ramo asegurador es razonable —producto
  financiero complejo, venta asistida, canal telefónico— **pero es transferencia, no evidencia
  directa**.
- **Ningún dato peruano ni latinoamericano de calidad.** Toda la evidencia es de EE.UU., China y
  Europa. La única señal local previa del proyecto es autorreportada (🟠D).
- **No se leyó ningún PDF primario en esta sesión.** El proxy de red del entorno bloqueó ~12
  dominios (arxiv, SSRN, SagePub, ama.org, dl.acm.org, Reddit, varios substacks, eurekalert,
  techxplore, udel, agentforthefuture). Los papers 🟢A se reconstruyeron por **búsqueda dirigida
  con múltiples fuentes secundarias convergentes**; diseños, muestras y direcciones de efecto son
  consistentes entre ellas, pero **las magnitudes puntuales del efecto de Luo 2021 (cuánto exactamente
  mejora el agente de rango medio) no se pudieron capturar** — solo la forma de la relación.
  Misma limitación y mismo procedimiento que la revisión profunda de 2026-08-12 en
  [[modelo-salud-ia-farmacias-peru]].
- **La pista social carece de acceso a conversación primaria** (§2.5): todo viene de agregadores.
- **F-473 y F-474 son preprints** no confirmados como peer-reviewed; se registran 🔵B por diseño
  experimental sólido y escala, no por validación de pares.
- **Sesgo de publicación no evaluado.** Los estudios que encuentran efectos nulos de copilotos de
  IA en ventas tienen menos probabilidad de publicarse; el corpus 🟢A disponible es pequeño (5
  papers) y no permite un análisis de embudo.
- **No se investigó el ángulo de costo.** Todo este node habla de efecto sobre desempeño; ninguna
  fuente aleatorizada reporta el costo por asesor de operar el copiloto, que es la otra mitad de
  cualquier decisión de ROI.

---

## Conexiones

- [[futuro-asesores-seguros-venta-digital|¿Desaparecerán los asesores de seguros?]] — aquel node
  establece **que** conviene invertir en el asesor en vez de reemplazarlo en producto complejo;
  este responde **cómo** hacerlo con evidencia causal, y aporta el dato más duro sobre por qué la
  IA no debe ponerse frente al cliente (Luo 2019, −79.7%). Comparten la misma variable moderadora
  (complejidad) y el mismo hallazgo sobre el rescate humano tardío (Bain NPS −11 / Alibaba
  escalamientos emocionales).
- [[proyecto-back-to-basics-ffvv-vida|Proyecto Back to Basics — FFVV Vida Individual]] — caso real
  donde AIDA/Espacio Digital del Asesor es la aplicación directa de este node; §5 traduce la
  evidencia a seis implicaciones concretas sobre el defecto de consistencia, el backlog y el
  diseño del Plan Piloto.
- [[material-visual-venta-consultiva|Material visual en la venta consultiva]] — misma familia de
  intervención (herramientas que asisten al asesor en la conversación compleja, en vez de
  reemplazarla); este node aporta la evidencia experimental de que el caudal de la ayuda importa
  tanto como su contenido.
- [[evaluacion-calidad-agentes-conversacionales-ia|Evaluación de calidad de agentes
  conversacionales de IA]] — provee los instrumentos para medir la **consistencia** del copiloto,
  que §5 identifica como el defecto de mayor prioridad; complemento metodológico directo.
- [[behavioral-design-estado-disciplina|Estado del behavioral design como disciplina]] — la
  divergencia rigor↔magnitud de §4.2 es el mismo "voltage drop" que aquel node documenta para
  intervenciones conductuales (DellaVigna & Linos, F-21): efectos grandes en papers, chicos a
  escala.
- [[tendencias-diseno-innovacion|Tendencias en diseño e innovación]] — §3.1 y F-492 aplican sus
  reglas de criterio sobre eco de cita, huérfanos de cita y descuento por incentivo del emisor.
