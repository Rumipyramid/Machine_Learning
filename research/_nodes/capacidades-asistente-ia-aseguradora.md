# Capacidades de un asistente de IA in-app para una aseguradora multi-ramo

> Documento de investigación. Fuente persistente y versionada en el repositorio.
> Fecha de elaboración: 2026-08-12 · Versión: v1.0
> Origen: investigación de 360° (`/trinidad` — pista empírica/teórica + social/mediática + de negocio)
> Pregunta original: ¿qué capacidades debe tener un asistente de IA que vive dentro de la app de
> una aseguradora multi-ramo, con objetivos de MAU, cross-sell y autoatención?
> Fuentes registradas en `research/fuentes/codice.md` (F-511 a F-525).
> Insumos internos contrastados: evaluación propia del agente web (20 preguntas, MT-Bench /
> LLM-as-judge con grounding) y propuesta preliminar de capacidades del equipo de Product Design del CoE.

---

## 0. Resumen ejecutivo

**Las tres pistas convergen en un punto que la propuesta del equipo no cubre: el problema
principal de un agente de seguros no es lo que sabe, es dónde están sus bordes** — qué debe
responder, qué debe rechazar, cuándo debe entregar la conversación a un humano, y qué obliga
legalmente a la empresa.

- **🔬 Empírica:** los LLMs **reconocen la ambigüedad pero rara vez preguntan** (sesgo de
  sub-clarificación, F-511); los regímenes que penalizan la abstención **fuerzan estadísticamente
  la alucinación** (F-512); el razonamiento numérico **colapsa de 95,6% a ~0%** al pasar de
  búsqueda simple a cálculo multivariado (F-514); y la mejor regla de escalamiento que existe no
  es por complejidad sino **por de quién fue la culpa** (F-515, 🟢A).
- **📱 Social:** el techo lo puso un tribunal — **la empresa responde por lo que dice su chatbot**
  (F-518). El regulador financiero estadounidense ya documentó el mapa de fallas con 98 millones
  de usuarios (F-519). Y lo que enfurece a la gente **no es que sea un bot: es quedarse sin salida**
  (F-521).
- **📈 Negocio:** el caso más grande del mundo (Erica, 3.000M de interacciones) mueve engagement
  con un mecanismo específico —**50-60% de sus interacciones son proactivas**, F-522— y el caso
  más publicitado de autoatención **se revirtió** porque las métricas de volumen enmascararon el
  deterioro de calidad (Klarna, F-523).

**⚔️ Divergencia que no se resuelve: los tres objetivos de negocio compiten entre sí.** La
autoatención empuja a cerrar conversaciones rápido; el MAU empuja a abrirlas; el cross-sell
empuja a extenderlas comercialmente. Klarna es el caso documentado de optimizar uno y perder
los otros dos.

**⚠️ Y el hallazgo que cambia el encuadre de todo el ejercicio:** la evaluación se hizo sobre un
agente **web y anónimo**; el agente propuesto es **in-app y autenticado**. Ese cambio de contexto
**agrava de categoría la mayoría de los hallazgos**, no los alivia. Ver §4.0 — es lo primero que
debería discutir el equipo.

---

## 1. 🔬 Pista empírica/teórica

### 1.1 Ambigüedad: el equipo tiene razón, y le falta la mitad del problema

El bloque 3 de la propuesta (desambiguación, memoria de sesión, multi-intención, corrección a
media conversación, terminología coloquial) está **bien fundado y bien observado**. La literatura
lo respalda y agrega un dato que lo hace más urgente: existe un **sesgo consistente de
sub-clarificación** — los modelos **reconocen** que la consulta es ambigua y aun así **prefieren
responder prematuramente**, y el sesgo **empeora conforme avanza el diálogo** (F-511, 🔵B,
hallazgo replicado en ≥4 trabajos independientes).

⚠️ **Pero hay un matiz que la propuesta no contempla y que puede invertir el resultado:
preguntar no es gratis.** El trabajo *"Clarification Is Not Enough"* muestra que el cuello de
botella se **desplaza** a responder bien después de la aclaración. Un agente que pregunta mucho
y responde mal después es **peor** que uno que responde directo: agrega turnos, agrega esfuerzo
y no agrega resolución. Y el esfuerzo es justamente lo que predice deslealtad (§4.3).

**Regla operativa que se desprende:** desambiguar solo cuando la respuesta cambia según la
respuesta del usuario. Si las tres pólizas del cliente tienen el mismo copago, no preguntar cuál
— responder.

### 1.2 La frontera de conocimiento: el hallazgo que explica los dos errores del agente actual

Los regímenes de entrenamiento y las evaluaciones binarias que **penalizan la abstención fuerzan
estadísticamente la alucinación**: el modelo aprende que adivinar rinde más que decir "no sé"
(F-512, 🔵B). La contramedida documentada no es pedirle cautela en el prompt: es **diseñar la
rúbrica de evaluación para que dé crédito a la abstención calibrada**.

⭐ **Leído contra la evaluación propia, esto explica de una sola vez los dos errores que parecían
opuestos:**

| Hallazgo de la evaluación | Dirección del error |
|---|---|
| P3 — rechaza una aritmética que sí puede resolver con los datos dados | **Sobre-abstención** |
| P4, P6, P7, P9, P10 — omite cifras y plazos públicos y verificables (5 de 20) | **Sub-utilidad por precaución** |
| P19 — ofrece cotizar un producto marcado como solo-renovaciones | **Sobre-confianza** |

No es un agente "demasiado cauto" ni "demasiado suelto". Es un agente **cuya frontera de
conocimiento no está definida**, y por eso falla en ambas direcciones a la vez.

La única referencia hallada del dominio exacto (F-513, 🟡C — preprint de industria, sin
reproducción independiente) resuelve esto arquitectónicamente descomponiendo el RAG de seguros en
cuatro tareas separadas, y la primera es la relevante: **"Knowledge Boundary ID" — entrenar el
rechazo como una tarea propia**, no como una instrucción de sistema. Las otras tres: selección
de conocimiento, destilación factual y **auto-verificación post-generación**.

### 1.3 Razonamiento numérico: no es una capacidad del modelo, es una herramienta conectada

El bloque 1 de la propuesta (cálculos de cobertura, saldo, temporales, consistencia de moneda)
identifica correctamente el problema. La evidencia dice **cómo** resolverlo, y no es pidiéndoselo
al modelo:

- **FAITH: los modelos de frontera pasan de 95,6% de acierto en búsqueda simple a prácticamente
  0% en cálculos multivariados** (F-514, 🔵B).
- El grueso del error está en **identificar mal la magnitud**, y **un error aritmético temprano se
  propaga por toda la cadena de razonamiento**.
- Consenso operativo: sin herramienta externa **no se puede garantizar corrección numérica**; los
  sistemas comerciales delegan el cálculo a llamadas de herramienta.

⭐ **Traducción para el equipo:** "razonamiento numérico" no debería redactarse como una
habilidad esperada del agente sino como un **requisito de arquitectura**: deducible, coaseguro,
saldo de suma asegurada, días a vencimiento y edad se calculan en una función determinista, y el
modelo solo redacta el resultado. La consistencia de moneda que el equipo pide es un chequeo de
esa función, no una instrucción de estilo.

### 1.4 Falla, reparación y escalamiento: lo que falta entero en la propuesta

Ninguno de los cuatro bloques cubre qué pasa **cuando el agente falla o cuando el caso no es
suyo**. Es la ausencia más grande, y es donde está la mejor evidencia disponible.

**F-515 (🟢A — *Journal of Consumer Behaviour*, con análisis de mediación)** aporta tres
resultados y uno de ellos es una regla de enrutamiento directamente implementable:

1. La **competencia percibida** sube 0,28 desviaciones estándar tras adoptar IA y **media el 45%**
   del efecto total sobre recuperación de confianza.
2. El soporte informativo por IA es **37% menos efectivo cuando el cliente expresa emoción
   negativa intensa**.
3. ⭐ **Los clientes prefieren IA cuando la falla fue suya, y prefieren humano cuando la falla fue
   de la empresa.**

**El criterio de escalamiento, entonces, no es la complejidad del caso — es de quién fue la culpa
y cuánta carga emocional trae el cliente.** Un rechazo de siniestro, una prima cobrada de más o
un reembolso demorado son fallas de la empresa: van a humano aunque el agente "sepa" la respuesta.

Complementos (F-516, 🔵B — experimentos de laboratorio, muestras de conveniencia): la falla de
chatbot escala vía **frustración → agresión hacia la marca**, no solo hacia el canal; **expresar
gratitud funcionó mejor que disculparse**; y un dato que conviene tener presente antes de
sobreinvertir: **los consumidores prefieren un humano para resolver reclamos incluso después de
que un chatbot resolvió su caso con éxito**.

### 1.5 Venta asistida por IA: la contraevidencia más fuerte del expediente

**F-517 (🟢A — *Marketing Science*, experimento de campo aleatorizado a gran escala en una fintech
real)** es la mejor fuente de esta investigación sobre el objetivo comercial, y va en contra:

> **Divulgar que el interlocutor es una IA antes de la conversación redujo las compras en ~79,7%.**
> Los chatbots no divulgados fueron tan efectivos como vendedores humanos experimentados y
> **cuatro veces más efectivos que los novatos**. El mecanismo medido: la divulgación activa
> percepción de **menor conocimiento y menor empatía**.

⚠️ **La lectura correcta no es la fácil.** La conclusión **no** es "no divulgar" — divulgar es
exigible y ocultarlo es la ruta directa al escenario de F-518. Las conclusiones defendibles son
dos:

1. **El cross-sell asistido por IA divulgada arranca con una penalización estructural**, y hay que
   compensarla con **utilidad demostrada**, no con persuasión.
2. **Cualquier proyección de cross-sell calcada de un benchmark de venta humana está inflada.**

El propio paper reporta la mitigación: la penalización **se reduce** al divulgar *después* de la
interacción útil, y con clientes de experiencia previa. Es decir: **primero resolver, después
ofrecer** — que es también lo que la práctica de conversational commerce recomienda por otras
razones.

---

## 2. 📱 Pista social/mediática

**Nivel de instalación social: 🔥 alto y estable.** El malestar con chatbots de atención en banca
y seguros no es un pico: lleva años, cruzó a regulación y cruzó a tribunales.

### 2.1 El techo legal — *Moffatt v. Air Canada*

Air Canada argumentó que **no era responsable de lo que dijo su chatbot**, tratándolo como una
entidad separada. El tribunal lo rechazó: el chatbot **es parte del sitio de la empresa, y la
empresa responde por toda la información que publica**, sea estática o conversacional (F-518, 🔵B
— decisión primaria, aunque de cuantía menor y sin efecto de precedente fuera de su jurisdicción).

⭐ **Para una aseguradora peruana la implicación es más severa que para una aerolínea**, porque lo
que el agente afirme sobre **cobertura, carencias, plazos, exclusiones y preexistencias** es
materia de contrato y de protección al consumidor. **Todo lo que el agente afirme, lo afirmó la
empresa.**

Esto reencuadra el pedido de "trazabilidad" del bloque 4: el equipo lo planteó como una ayuda
para que el usuario verifique. Es también, y sobre todo, **el registro de qué se le prometió a
quién**.

### 2.2 El mapa de fallas ya lo escribió un regulador

El *issue spotlight* del CFPB (F-519, 🔵B — regulador con acceso a su propia base de reclamos)
documenta con **98 millones de usuarios** de chatbots bancarios en 2022 exactamente los modos de
falla que importan acá:

- La efectividad **cae a medida que la pregunta se complejiza**.
- Los chatbots reconocen disputas **solo por palabras o sintaxis específicas**.
- Los consumidores quedan atrapados en **bucles repetitivos de jerga inútil**.
- Clientes mayores o cuya lengua principal no es la del canal **quedan sin salida a un humano**.
- Efecto neto: **erosión de la confianza en la institución**, no solo en el canal.

El sentimiento público agregado (F-521, 🟠D — anecdotario, sin muestra) es consistente y se
resume en una frase: **lo que enfurece no es que sea un bot, es quedarse sin salida.** La demanda
expresada es siempre la misma — ruta rápida a un humano, y que el bot **reconozca cuándo está
frustrando** y transfiera solo.

### 2.3 Riesgo adversarial

El caso del concesionario Chevrolet cuyo chatbot fue inducido a "vender" una camioneta en US$1
como "oferta legalmente vinculante" (F-520, 🟠D — incidente viral) completa el cuadro desde el
otro lado: **no solo el error propio del agente obliga a la empresa, también el error inducido
por el usuario.** En un agente con capacidad comercial y con cliente autenticado, esto deja de
ser anécdota.

---

## 3. 📈 Pista de negocio

### 3.1 Erica (Bank of America) — el caso más grande, y su mecanismo real

**3.000 millones de interacciones** acumuladas · **~50 millones de clientes** · **más de 58
millones de interacciones al mes** · **18,7 millones de horas** de conversación (F-522, 🟠D —
autorreporte corporativo sin auditoría).

⭐ **El dato que casi nadie cita y que es el único mecanismo documentado de MAU: entre 50% y 60%
de las interacciones son *proactivas*** — el asistente sugiere algo y el cliente entra a partir de
esa sugerencia. Más de **1.700 millones de insights proactivos personalizados** entregados.

⚠️ El "98% encuentra lo que necesita" es autorreportado, con definición propia y sin metodología
publicada. **No usarlo como benchmark.**

### 3.2 Klarna — la contraevidencia central, y su mecanismo de falla

En 2024: el asistente hacía el trabajo de **700 agentes** y atendía **dos tercios de las
consultas**. En 2025: **reversión y recontratación de humanos** tras caer la satisfacción
(F-523, 🟡C — la reversión y las citas del CEO tienen cobertura independiente; **las cifras
originales de 2024 nunca fueron auditadas**).

Cita del CEO: *"nos enfocamos demasiado en eficiencia y costo… el resultado fue menor calidad, y
eso no es sostenible."*

⭐ **El mecanismo de falla es lo que hay que llevarse, no la anécdota: las métricas agregadas de
volumen en las que la IA rendía bien enmascararon el deterioro de calidad en tipos específicos de
interacción.** Es literalmente el riesgo de gobernar el agente por *deflection rate*.

### 3.3 Lemonade — el techo real de automatización en seguros

**96% de los primeros avisos de siniestro** se toman sin humano, pero **solo 55% de los siniestros
se resuelven de punta a punta automáticamente** (F-524, 🟠D — cifras de la empresa reproducidas
por blogs de proveedores con interés comercial).

⭐ **La brecha entre 96% y 55% es el hallazgo:** capturar es fácil, **resolver** es donde entra el
humano. Y esto en la aseguradora más automatizada del mundo, con productos deliberadamente
simples (hogar, inquilino, mascota) — no salud, no EPS, no multi-ramo con preexistencias y
carencias. **Cualquier meta de autoatención en un ramo complejo debe partir por debajo de ese 55%.**

---

## 4. ⚖️ Síntesis y contraste con la propuesta del equipo

### 4.0 Lo primero: el cambio de web a app agrava los hallazgos, no los alivia

La evaluación se hizo sobre un agente **web y anónimo**. El agente propuesto es **in-app y
autenticado**. Dos consecuencias que conviene discutir antes que cualquier lista de capacidades:

**(a) El hedge "depende de tu plan" deja de ser aceptable.** En la web, ante un usuario anónimo,
responder *"la cobertura depende del plan que hayas contratado, revísalo en tu póliza"* es
correcto. **Dentro de la app, con el cliente autenticado, el agente sabe cuál es el plan.** Los
cinco hallazgos de omisión (P4, P6, P7, P9, P10) pasan de *hedge defendible* a **evasión
injustificada**.

**(b) "Ve a la app y haz X" se vuelve absurdo.** La respuesta más frecuente del agente evaluado es
una ruta de navegación hacia la app. Dicha **por** la app, esa respuesta es la definición de
esfuerzo innecesario — y el cambio de canal y el contacto repetido son los dos mayores generadores
de esfuerzo documentados (F-525). **Dentro de la app, informar cómo hacer algo debe ser reemplazado
por hacerlo.**

### 4.1 Los cuatro bloques de la propuesta, evaluados

| Bloque de la propuesta | Veredicto | Evidencia | Qué corregir o agregar |
|---|---|---|---|
| **1. Razonamiento numérico** | ✅ Problema bien identificado, **solución mal ubicada** | 🔵B (F-514) | No es capacidad del modelo: es **herramienta determinista**. 95,6% → ~0% al pasar a cálculo multivariado. Redactarlo como requisito de arquitectura |
| **2. Estructuración y presentación** | ✅ Correcto y bien observado | 🟡C-🔵B (F-525) | Agregar el criterio que lo justifica: **cada turno extra y cada cambio de canal es esfuerzo medible**. La priorización ante 200 prestadores no es estética, es reducción de esfuerzo |
| **3. Ambigüedad y contexto** | ✅ El bloque mejor construido | 🔵B (F-511) | Agregar el límite: **preguntar no es gratis**. Desambiguar solo cuando la respuesta cambia. Y el post-clarification answering es el cuello de botella real |
| **4. Precisión y confiabilidad** | ⚠️ **Correcto pero incompleto en una dirección** | 🔵B (F-512) · 🔵B (F-518) | Está escrito solo contra la alucinación. **El agente evaluado falla igual de seguido por omisión y por rechazo injustificado.** Necesita ser bidireccional. Y la trazabilidad es también **registro de obligación legal** |

### 4.2 Lo que falta: cuatro capacidades sin bloque

**A · Frontera de conocimiento bidireccional** — 🔵B (F-512, F-513)
La propuesta dice qué no inventar. No dice **qué el agente está obligado a responder**. Hace falta
la lista explícita de lo que sí puede afirmar (sumas aseguradas por plan, carencias, plazo de
inclusión de recién nacido, exclusiones estándar, cálculo de copago/coaseguro) y tratar la
omisión de esos datos **como una falla, no como prudencia**.

**B · Escalamiento y reparación** — 🟢A (F-515), 🔵B (F-516, F-519)
Ausente por completo, y es lo que más enfurece a los usuarios. La regla que la evidencia respalda:
**escalar por culpa y por carga emocional, no por complejidad.** Falla de la empresa → humano.
Emoción negativa intensa → humano (la IA rinde 37% menos ahí). Y ruta a humano siempre visible,
nunca escondida detrás de intentos del bot.

**C · Proactividad** — 🟠D (F-522)
Ausente. La propuesta es **enteramente reactiva**: cada capacidad descrita asume que el usuario
pregunta primero. **Si el objetivo es MAU, un asistente reactivo no puede entregarlo** — el único
mecanismo documentado de engagement en el caso más grande del mundo es que **50-60% de las
interacciones las inicia el asistente**. ⚠️ Evidencia débil (autorreporte corporativo), pero es la
única que hay y es direccionalmente clara.

**D · Capacidad de ejecutar, no solo de explicar** — 🟡C (F-525), 🟠D (F-524)
Ausente. Autoatención no es explicar bien cómo hacer un trámite: es **completarlo**. Reembolso,
inclusión de dependiente, descarga de póliza, actualización de datos, pago. Lemonade muestra dónde
está el techo (96% captura vs. 55% resolución) y muestra que **la diferencia entre ambos es
exactamente lo que separa un asistente informativo de uno que hace autoatención de verdad**.

### 4.3 Los tres objetivos, con la fuerza de evidencia que realmente tienen

| Objetivo | Fuerza de evidencia | Qué la sostiene | Qué la limita |
|---|---|---|---|
| **Autoatención** | 🔵 **Moderada** — el mejor sustentado de los tres | Erica a escala masiva (F-522); Lemonade 55% end-to-end (F-524); el marco de esfuerzo (F-525) | ⚠️ El 55% es en los productos **más simples que existen**. En salud/EPS con preexistencias y carencias, el techo es **más bajo**. Y Klarna revirtió (F-523) |
| **MAU** | 🟠 **Débil e indirecta** | Un solo mecanismo documentado: **proactividad** (F-522) | Ninguna evidencia causal de que un asistente suba MAU. Las cifras de Erica son autorreportadas, no auditadas, y **volumen de interacciones ≠ usuarios activos** |
| **Cross-sell** | 🔴 **La más débil, y con contraevidencia 🟢A en contra** | Nada verificable en seguros | **F-517: divulgar la IA redujo compras ~79,7%** en experimento de campo. Sumado al hallazgo propio de que el agente no cruza el puente ante señal implícita |

⭐ **La tensión que hay que nombrar y no resolver artificialmente: los tres objetivos compiten.**
La autoatención empuja a **cerrar** conversaciones rápido. El MAU empuja a **abrirlas**. El
cross-sell empuja a **extenderlas comercialmente**. Un agente optimizado para *deflection* baja el
MAU; uno optimizado para engagement sube el costo por interacción; uno optimizado para cross-sell
erosiona la confianza que sostiene a los otros dos. **Klarna es el caso documentado de optimizar
uno y perder los otros.**

**Recomendación de secuencia, no de simultaneidad:** autoatención primero (es lo mejor sustentado
y construye la competencia percibida que F-515 identifica como mediadora del 45% de la confianza);
proactividad después (es el mecanismo de MAU); cross-sell último y **solo sobre conversaciones ya
resueltas** — que es además la mitigación que el propio F-517 reporta.

---

## 5. Recomendaciones priorizadas

1. **Definir la lista blanca de afirmaciones autorizadas** — qué cifras, plazos y reglas puede
   decir el agente sin derivar. Ataca los 5 hallazgos de omisión y es prerrequisito de todo lo
   demás. Con el cliente autenticado, esta lista es mucho más ancha que en la web.
2. **Sacar todo cálculo del modelo y ponerlo en función determinista.** Deducible, coaseguro,
   saldo, días a vencimiento, edad. Resuelve P3 y previene el modo de falla de F-514.
3. **Escribir la política de escalamiento por culpa y emoción**, no por complejidad. Ruta a humano
   siempre visible.
4. **Sustituir "cómo hacer X en la app" por "hacer X"** en los trámites de mayor volumen. Es la
   única definición de autoatención que sobrevive dentro de la app.
5. **Diseñar la evaluación continua antes que las capacidades** — con la abstención puntuando a
   favor (F-512) y con métricas segmentadas por tipo de interacción, no agregadas por volumen
   (la lección de Klarna).
6. **Tratar el cross-sell como puente post-resolución**, nunca como interrupción; y ajustar a la
   baja toda proyección comercial calcada de benchmarks de venta humana.
7. **Registrar qué se le prometió a quién.** Consecuencia directa de F-518.

---

## 6. Limitaciones

- **No se halló ninguna evidencia causal** de que un asistente in-app aumente MAU o cross-sell en
  seguros. Todo lo de negocio es autorreporte corporativo (🟠D) o cobertura de prensa (🟡C).
- **Cero evidencia peruana o latinoamericana** sobre asistentes de IA en seguros. Ni casos, ni
  benchmarks, ni percepción local medida.
- **La pista social se apoya en anecdotario y en un regulador extranjero.** El CFPB es sólido pero
  es EE.UU.; no se buscó posición de SBS o INDECOPI sobre agentes conversacionales, y eso queda
  como pendiente relevante para una aseguradora peruana.
- **F-513 es un preprint de industria sin reproducción independiente** — es la única referencia del
  dominio exacto y hay que tratarla como hipótesis arquitectónica, no como práctica validada.
- **La cifra ancla del marco de esfuerzo (F-525) tiene sospecha de eco de cita:** circula desde
  2010 sin dataset público. Se usa el mecanismo, no el multiplicador (regla C3).

---

## Conexiones

- [[evaluacion-calidad-agentes-conversacionales-ia|Evaluación de calidad de agentes conversacionales de IA]]
  — este node aporta el **qué debe saber hacer** el agente; aquel aporta el **cómo medirlo**
  (MT-Bench, LLM-as-judge, escalas de usabilidad). La recomendación 5 vive en la intersección.
- [[modelo-salud-ia-farmacias-peru|Modelo de triage IA + farmacias + atención humana]] — comparte
  el problema de dónde poner el límite entre lo que resuelve la IA y lo que requiere humano, en el
  mismo mercado y con el mismo tipo de cliente.
- [[tendencias-diseno-innovacion|Tendencias en diseño e innovación]] — **C8 aplica directamente**
  (la explicabilidad genérica no calibra la confianza; la verificabilidad sí), y **C2 obliga a
  desinflar** cualquier promesa de impacto del agente antes de llevarla a comité.
- [[seguros-comportamiento-mundo-peru|Comportamiento y percepción de seguros (Mundo vs. Perú)]] —
  el ~48% de desconfianza hacia las aseguradoras en Perú, con la falta de información como causa
  #1, es el contexto en el que este agente va a operar: la omisión de datos no es neutral, alimenta
  la causa declarada de la desconfianza.
