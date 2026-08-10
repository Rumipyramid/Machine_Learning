# Revisión del modelo de trabajo de diseño

### Contraste de la sesión de construcción metodológica contra la evidencia acumulada de diseño e innovación

> Documento para el equipo de diseño. Fecha: 2026-08-10.
> Base: `research/_nodes/tendencias-diseno-innovacion.md` (v4.0 — 31 hipótesis, 22 reglas
> destiladas, evidencia F-237 a F-468) y `research/_nodes/metodologias-diseno-sistemas-complejos.md`
> (v1.0 — F-469 a F-482). Las fuentes citadas como `F-n` están en `research/fuentes/codice.md`
> con su nivel de rigurosidad (🟢A a 🔴E).

---

## Cómo leer este documento

Esto no es una evaluación del equipo. Es un contraste entre lo que se discutió en la sesión y lo
que la evidencia publicada dice sobre problemas del mismo tipo — con la ventaja injusta de poder
consultar 230 fuentes en frío mientras ustedes construían en vivo con una hora de reloj.

Casi todo lo que aparece aquí como riesgo **no es un error del equipo: es un modo de falla
documentado del campo entero**. Varios de esos modos de falla ya fueron nombrados en la propia
sesión, sin el vocabulario que los conecta con la literatura. Esa es, de hecho, la parte más útil
de este documento: darle nombre a lo que ustedes ya vieron.

Está organizado en cinco partes: **lo que ya está bien resuelto** · **lo que ya descubrieron pero
no tiene nombre** · **riesgos** · **oportunidades** · **sugerencias**.

---

## 1. Lo que ya está bien resuelto

Vale empezar por acá porque es lo que no hay que tocar en la siguiente iteración.

**El DoR como compuerta, no como formulario.** Definir qué tiene que existir antes de que una
quest entre a ejecución es la decisión de mayor apalancamiento de toda la sesión. La mayoría de
los modelos de trabajo de diseño se rompen justamente ahí: aceptan pedidos sin criterio de
entrada y después negocian alcance bajo presión de fecha.

**La regla de no duplicar ejecución.** Que dos roles no ejecuten lo mismo suena obvio y casi nunca
está escrito. Escribirlo evita la discusión política caso por caso.

**La ambición del to-be por macro-journey.** Es la pieza que le da al modelo una unidad de análisis
más grande que el ticket. Sin eso, un modelo de trabajo de diseño degenera en cola de pedidos.

**Evitar el XL porque rompe el balance de capacidad.** Es una decisión correcta desde la operación
— y tiene un costo que conviene mirar de frente (§4, R2). Correcta no quiere decir gratis.

**La honestidad del diagnóstico en la propia sesión.** "En Rimac la mayoría de problemas son en
realidad sistémicos" y "cada año es como construir un Rimac Frankenstein" son dos observaciones
que la literatura tarda un paper entero en fundamentar. Ya están dichas. El trabajo pendiente no
es descubrirlas, es que el modelo las tome en serio.

---

## 2. Lo que el equipo ya descubrió, pero todavía no tiene nombre

Cuatro conceptos con literatura detrás que corresponden uno a uno con cosas que se dijeron en la
sesión. Ponerles nombre no es cosmético: un problema con nombre se puede priorizar, medir y
defender en una reunión de portafolio. Uno sin nombre se vuelve a discutir cada trimestre.

### 2.1 Complicado ≠ complejo

La metáfora de la "fábrica digital" describe con precisión un sistema **complicado**: la relación
causa-efecto es cognoscible, un experto puede analizarla, y la solución se diseña y se impone. En
un sistema **complejo**, las interacciones son no lineales y —en la formulación de la extensión de
Cynefin a gestión de proyectos (F-473, 🔵B)— *"las soluciones surgen de las circunstancias en vez
de imponerse"*.

| | Complicado | Complejo |
|---|---|---|
| Causa-efecto | Cognoscible con análisis | No cognoscible por adelantado |
| Quién resuelve | Expertos que definen el proceso | Nadie por adelantado |
| Cómo aparece la solución | Se diseña y se impone | **Emerge** |

La sesión sostiene las dos cosas a la vez: la metáfora es de fábrica, el diagnóstico es de sistema.
No es contradicción — es que hay dos tipos de trabajo mezclados en el mismo modelo, y solo uno de
ellos se organiza bien como línea de producción.

⚠️ **Con una advertencia sobre el propio marco:** Cynefin no tiene prueba científica de validez y
la asignación de dominio es subjetiva — equipos distintos clasifican la misma situación en dominios
distintos (F-472, 🟠D). Sirve como **lenguaje común**, no como criterio de decisión. Úsenlo para
entenderse, no para dirimir.

### 2.2 Failure demand

El ejemplo del IVR —las llamadas al contact center suben porque una locución vieja confunde a los
clientes— tiene nombre técnico: **failure demand**, la demanda que existe *solo porque el sistema
falló antes* (F-474, 🔵B). Rellamadas, reclamos, retrabajos, escalamientos.

Es, de todo lo revisado en las dos investigaciones, **el único indicador contable que el campo
produjo**. Separar demanda de valor de demanda de falla convierte una discusión metodológica en un
número. Y en una operación con contact center y gestión de renovaciones **es instrumentable con lo
que ya existe** — no requiere ninguna capacidad nueva.

### 2.3 Backstage

*"Se flea en un canal y Dios sabrá quién se lleva después el seguimiento."* Eso es una descripción
de backstage sin dueño.

Birgit Mager, autoridad académica del service design (F-476, 🟡C): *"No puedes cambiar el
frontstage si no impactas el backstage"* — y **la mayoría de las iniciativas de innovación fracasan
al escalar porque el backstage nunca se rediseñó**. Es la distinción operativa entre design thinking
(diseña la experiencia) y service design (diseña la experiencia **y el sistema de entrega que la
produce**).

La consecuencia práctica: cuando un piloto funciona con 10 personas y no escala, la hipótesis por
defecto no debería ser "el diseño estaba mal" sino "el backstage nunca se tocó".

### 2.4 Suboptimización

*"Viene el pedido de un área y tú solo trabajas con esa área."* La crítica de Jackson al Vanguard
Method (F-475, 🔵B) describe exactamente el riesgo: al definir el sistema desde un solo punto de
vista, **se mejora la parte y se empeora el todo**. Se mejora la experiencia de un área y se
empeora la economía del conjunto.

"Rimac Frankenstein" es el nombre coloquial del resultado acumulado de muchas optimizaciones
locales correctas.

---

## 3. Una precisión de alcance antes de seguir

Para que el resto del documento se lea bien, conviene dejar escrito qué se está considerando
dentro del alcance de behavioral design en este análisis.

**El objeto de trabajo es la arquitectura de la decisión**: dónde ocurre la elección, con qué
opciones, en qué orden, con qué opción por defecto, con qué fricción, con qué información
disponible en el momento exacto de decidir, y con qué costo de revertir. La pieza de comunicación
es *una* de las variables de esa arquitectura, no su perímetro.

Esto importa para el modelo de trabajo por una razón concreta: **el nivel al que se escribe el rol
en el documento es el nivel al que va a ser convocado durante el año siguiente**. Un rol descrito
por sus entregables visibles se recibe como servicio de ejecución al final del proceso; un rol
descrito por su objeto de decisión se convoca al momento de definir el journey. La diferencia no
se negocia después: se fija cuando se escribe el modelo.

---

## 4. Riesgos

Ordenados por qué tan caro sale descubrirlos tarde.

### R1 · Medir entrega en una disciplina donde la mayoría de lo bien hecho no mueve su métrica

La distribución real de efectos del diseño es de cola larga con moda cero: **~2/3 de los cambios
bien diseñados no mueven su métrica objetivo** (evidencia causal, A/B a escala, F-262 — regla **C2**
del node de tendencias).

Un modelo de trabajo que cuenta quests entregadas y capacidad consumida va a reportar producción
estable mientras el impacto varía enormemente y sin registro. En el mejor escenario el equipo hace
un trabajo excelente y no puede probarlo. En el peor, se hace un año entero de trabajo dentro del
tercio que no movió nada, con todos los indicadores del modelo en verde.

> Hay un precedente interno exacto de este modo de falla: los modelos de churn del negocio predicen
> **quién** se va a ir con muy buena performance, pero no registran **por qué** — el 59% de
> cancelación voluntaria queda sin causa medida. Un modelo de trabajo que registra **cuánto** se
> entregó sin registrar **si sirvió** es el mismo agujero, un nivel más arriba.

### R2 · El modelo excluye estructuralmente el tipo de evidencia más fuerte

En la sesión se nombró un experimento longitudinal que podría correr tres años. En la misma sesión
se decidió evitar el XL porque rompe el balance de capacidad. Las dos cosas son razonables por
separado y juntas producen un sesgo estructural: **lo que no cabe en un ciclo no entra al
portafolio.**

Esto pesa más de lo que parece. La pieza de evidencia más sólida de todo el node de tendencias —el
RCT preregistrado de UBI/telemática en seguros, N=1.449 (F-442)— es exactamente del tipo que este
modelo no puede alojar. Y en tres barridos independientes buscando el estudio longitudinal
equivalente en diseño de interfaces, no existe (regla **C7**): nadie lo corrió. Ese es el hueco.

El riesgo no es que falte un proyecto grande. Es que el equipo quede permanentemente del lado débil
de la evidencia por una decisión de capacidad que nunca se tomó como decisión sobre evidencia.

### R3 · Suboptimización por diseño de entrada

Si el trabajo entra por pedido de área y se ejecuta con esa área, el modelo **no tiene ningún punto
donde alguien pregunte qué le pasa al resto del sistema** (F-475). Cada quest puede estar bien
resuelta y el agregado empeorar.

Es el riesgo más caro de la lista porque es invisible desde adentro: se manifiesta a nivel de
portafolio, no de quest, y ningún indicador de quest lo va a mostrar.

### R4 · El vacío de implementación y evaluación

El hallazgo de mayor rigor de toda la investigación de metodologías (F-469, 🟢A — revisión de
alcance de 49 estudios sobre 50 años de Soft Systems Methodology en salud): la metodología más
establecida del campo se usó sobre todo para **entender el problema y proponer mejoras**, y **mucho
menos para implementarlas y evaluarlas**.

Medio siglo de aplicación documentada, y casi nunca llega a la fase donde podría demostrarse que
funcionó. Un modelo de trabajo cuyo producto principal es un to-be por macro-journey está a un paso
de heredar exactamente ese patrón: mapas excelentes, ninguna medición de si el mapa cambió algo.

### R5 · La fragmentación del end-to-end quedó abierta

El punto más fuerte que se levantó en la sesión y el único que no se resolvió: *"si había un valor
en tener el end to end era que el mismo rol entendía y se empapaba del problema."*

Al partir el journey por especialidad se gana claridad de responsabilidad y se pierde el rol que
carga el problema completo en la cabeza. Y hay una consecuencia concreta: **el backstage tiende a
quedarse sin dueño**, porque no es de nadie en particular y aparece entre dos especialidades.

Este riesgo no tiene respaldo empírico fuerte en las fuentes revisadas — lo pongo porque el
argumento es bueno y quedó sin contestar, no porque la literatura lo confirme.

### R6 · El mejor punto de la sesión llegó con dos minutos de reloj

*"Estamos atacando el problema por el detalle… falta atacarlo por el otro lado, que es cómo vamos a
priorizar."*

La evidencia de negocio apunta en la misma dirección: solo 30% de los programas de transformación
cumple plazo, presupuesto y alcance, y el predictor que reporta la literatura **no es la metodología
de diseño — es la gobernanza y la consistencia del liderazgo** (F-482). La observación que más
duele: *"el proceso empieza gradualmente a llenar vacíos que el liderazgo debería atender — los
planes detallados compensan prioridades poco claras, los foros de gobernanza sustituyen la toma de
decisiones, las métricas reemplazan conversaciones significativas."*

⚠️ **Con la salvedad de rigor que corresponde:** esa evidencia es de consultoras (🟡C) con posible
eco de cita entre firmas, mientras que R4 se apoya en una revisión sistemática (🟢A). No pesan
igual. Lo honesto es decir que la evidencia fuerte muestra el vacío de evaluación, y la evidencia
débil sugiere dónde está la causa.

Pero el riesgo operativo es concreto y no depende del rigor de la fuente: **un modelo de trabajo
muy bien especificado sobre un criterio de priorización no resuelto va a ejecutar impecablemente lo
que no había que hacer.**

---

## 5. Oportunidades

### O1 · Hay un hueco público que este equipo está a poca distancia de llenar

Tres barridos independientes, con términos distintos, buscando lo mismo: **no existe ningún caso
público de rediseño con métricas de resultado en un documento auditado**. Ni de consultoras, ni de
in-house, ni de casos premiados. La ausencia dejó de ser azar de búsqueda y pasó a ser una
propiedad del campo (regla **C7**).

Traducido: si este equipo elige **un** rediseño, define el indicador antes de empezar, lo mide
después y publica el resultado —incluso si el resultado es que no movió nada— tiene algo que
prácticamente nadie tiene. La barrera no es de capacidad. Es de decisión.

### O2 · Hay un número disponible mañana

Failure demand en el journey de renovación o en el contact center (§2.2). No requiere metodología
nueva, ni herramienta nueva, ni presupuesto. Requiere clasificar la demanda que ya se registra.

Es la conversión más barata que existe de "el diseño aporta valor" a un número que un CFO puede
leer, y encaja exactamente con la regla **C1**: *argumentar por mecanismo, nunca por multiplicador*
— "este cambio elimina N rellamadas al mes" resiste una pregunta; "el diseño devuelve 100x" no.

### O3 · El backstage como criterio de entrada convierte un riesgo en una regla de una línea

Si el DoR ya existe como compuerta, agregarle el backstage no cuesta rediseñar el modelo: cuesta un
campo. Y ataca directamente el modo de falla predecible del escalamiento (F-476).

### O4 · El momento de escribir el rol es este y no se repite

Un modelo de trabajo se escribe una vez y se hereda durante años. Es la única ventana barata para
fijar el alcance de behavioral design en arquitectura de la decisión (§3) en vez de dejarlo
emerger de la costumbre de los pedidos. Después se negocia caso por caso, con mucho más esfuerzo y
peores resultados.

### O5 · Un vocabulario de cuatro palabras baja el costo de todas las discusiones siguientes

Complicado/complejo · backstage · failure demand · suboptimización. Cuatro términos con literatura
detrás que le dan al equipo forma de nombrar problemas que hoy se re-explican desde cero en cada
reunión.

### O6 · Las reglas de argumentación aplican hacia adentro también

**C1** (mecanismo, no multiplicador) y **C11** (desconfiar de toda métrica de productividad
autorreportada — existe un RCT donde desarrolladores expertos fueron 19% *más lentos* con IA
creyendo ser 20% más rápidos, una brecha percepción-realidad de ~39 puntos) no son solo para
presentaciones a negocio. Aplican a cómo el propio modelo reporte su rendimiento. Si el modelo se
evalúa por percepción del equipo sobre su propia velocidad, C11 dice qué tan confiable es ese dato.

---

## 6. Sugerencias

Ordenadas por relación impacto/costo. Las tres primeras se pueden decidir en la siguiente sesión.

### Inmediatas — no cambian el modelo, lo completan

**S1 · Un campo obligatorio en el DoR: "¿cómo sabremos si sirvió?"**
Indicador definido *antes* de empezar, con su valor base. Es la palanca más barata de todo este
documento y ataca R1 y R4 a la vez. La recomendación de fondo de la investigación de metodologías
es literalmente esta: dado que las tres pistas de evidencia convergen en que el vacío está en la
implementación y la medición, **la decisión de mayor impacto no es qué método adoptar, sino
comprometerse por adelantado a medir el resultado** — cualquiera de los métodos funciona mejor con
esa disciplina que el mejor de ellos sin ella.

**S2 · Un campo de backstage en el to-be.** Qué proceso, sistema o rol de trastienda tiene que
cambiar para que este frontstage funcione. Si la respuesta es "ninguno", que quede escrito — y que
se revise, porque suele ser falso.

**S3 · Una línea anti-suboptimización en el DoR.** Toda quest que entre por pedido de un área
declara qué otra área absorbe el costo del cambio. No hace falta resolverlo en la compuerta; hace
falta que alguien lo haya escrito una vez.

### Sobre el diseño del modelo

**S4 · Un carril fuera de la economía de capacidad.** Reservar una fracción explícita (10-15% es un
punto de partida razonable, no un número con evidencia) para trabajo que no cabe en un ciclo:
experimentos largos, instrumentación, medición posterior de cosas ya entregadas. Sin esto, R2 no se
resuelve — porque el problema no es la voluntad, es que la economía de fichas expulsa
automáticamente lo que no cierra en el período.

**S5 · Un "dueño del problema" nominal por macro-journey, aunque la ejecución se reparta.** Responde
a R5 sin volver al end-to-end por rol. Alguien que carga el problema completo y a quien le
pertenece el backstage por defecto. Es un rol de continuidad, no de ejecución.

**S6 · Escribir el alcance de behavioral design por su objeto de decisión, no por sus entregables.**
Ver §3. Una frase en el documento del modelo.

**S7 · Adoptar el vocabulario de §2 en el documento del modelo.** Cuatro definiciones, media página.

### Sobre gobernanza — la que no es del equipo pero le toca pedir

**S8 · Una sesión dedicada al criterio de priorización de portafolio, antes de seguir afinando el
método.** Es exactamente lo que se dijo al final con dos minutos de reloj (R6), y la evidencia de
negocio dice que es donde está el predictor. Poner esa sesión primero es barato; descubrir en
diciembre que se ejecutó bien el portafolio equivocado, no.

**S9 · Elegir un caso y auditarlo de punta a punta para publicarlo.** Un rediseño, un indicador
definido antes, una medición después, el resultado escrito sea cual sea. Es O1. Es la única
sugerencia de esta lista que además construye reputación externa para el equipo.

---

## 7. Lo que este documento no resuelve

Por honestidad sobre los límites de lo que se puede afirmar acá:

- **No dice qué metodología adoptar.** La conclusión de la investigación de metodologías es que la
  pregunta está mal planteada: no hay una mejor, hay un criterio de selección según el tipo de
  problema. La tabla de selección completa está en `metodologias-diseno-sistemas-complejos.md` §4.
- **No resuelve R5.** El argumento sobre la pérdida del end-to-end quedó sin contestar en la
  sesión y no encontré evidencia que lo confirme ni lo refute. S5 es una mitigación, no una
  respuesta.
- **La evidencia de gobernanza (R6) es toda 🟡C.** Ninguna cifra de tasa de éxito de
  transformación viene de una fuente auditable independiente. Está marcada como tal en el texto.
- **No evalúa a las personas ni la calidad del trabajo del equipo.** No tengo base para eso y no es
  lo que se contrastó.

---

## Conexiones

- [[tendencias-diseno-innovacion|Tendencias en diseño e innovación]] — origen de las reglas C1, C2,
  C7, C11 y de la evidencia sobre distribución de efectos y ausencia de casos auditados.
- [[metodologias-diseno-sistemas-complejos|Metodologías de diseño para sistemas complejos]] —
  origen de complicado/complejo, backstage, failure demand, suboptimización y del hallazgo del
  vacío de evaluación.
