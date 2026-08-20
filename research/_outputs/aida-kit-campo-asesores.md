# Kit de campo — capturar la conducta del asesor de aquí al miércoles

**Instrumento listo para enviar.** v1.0 · 2026-08-20
Complementa `_outputs/aida-roadmap-evaluacion.md`, que cubre la auditoría de la herramienta.
Esto cubre **la otra mitad: qué hace el asesor**, con AIDA y con las herramientas de afuera.

---

## La recomendación, en una línea

**Prioriza lo que no le cuesta tiempo al asesor, y captura en el momento en vez de preguntar
después.** En cinco días no da para etnografía; sí da para tres cosas que rinden más de lo que
parecen.

| # | Método | Costo para el asesor | Rendimiento | ¿Entra esta semana? |
|---|---|---|---|---|
| **1** | **Los logs de AIDA** | **Cero** | ⭐⭐⭐ El mayor volumen de conducta real disponible | ✅ **Prioridad absoluta** |
| **2** | **Bitácora diaria por WhatsApp + capturas** | 30 seg/día | ⭐⭐⭐ Conducta en el momento, no recordada | ✅ **Sí** |
| **3** | **4 entrevistas de incidente crítico** | 40 min, una vez | ⭐⭐ Alto si el muestreo es el correcto | ✅ **Sí, solo cuatro** |
| **4** | **Encuesta corta en Wiser** | 3 min | ⭐ Da magnitudes, no conducta | 🟡 Solo si sobra tiempo |
| **5** | **Shadowing clásico** | 2-3 h | ⭐⭐ Alto, pero no cabe | ⛔ **Deferir a después del miércoles** |

⭐ **Deferir el shadowing no es una concesión, es mejor secuencia:** después del miércoles vas a saber
qué le importa a los dueños de la capacidad, y el shadowing se puede apuntar en vez de barrer.

---

## 1 · Los logs — lo primero, y no requiere goodwill de nadie

Ya los pediste. **Insiste el jueves temprano.** Cubren **>30.000 consultas mensuales** y más de un año
de historia: ningún método de campo se acerca a ese volumen, y no le cuesta un minuto a ningún asesor.

**Qué pedirle a los logs, en orden:**

1. **Las 50 preguntas más frecuentes.** ⭐ Es el banco real que reemplaza al sintético.
2. **Las preguntas con feedback negativo**, agrupadas por tema. Es el corpus de fallas, servido.
3. **Distribución por hora del día.** Dice si consultan **preparando** o **en vivo** con el cliente.
4. **Turnos por consulta y reformulaciones.** Cuántas vueltas necesita una respuesta usable.
5. **Consultas sin cierre** — abandono.
6. ⭐⭐ **Series por categoría a lo largo del tiempo.** *¿Hay algún tipo de pregunta que se hacía en
   los primeros meses y ya casi no aparece?*

> **Sobre el punto 6.** La telemetría no puede mostrar una pregunta que **nunca** se hizo — eso solo
> sale preguntando. **Pero sí puede mostrar una categoría que se apagó.** Si las preguntas de
> cobertura cayeron 70% desde marzo, eso es abandono selectivo y está en los datos que ya existen.
> **Es el análisis más barato con mayor probabilidad de dar un hallazgo de portada.**

---

## 2 · Bitácora diaria por WhatsApp — el mejor rendimiento por costo

**Por qué esta y no una entrevista:** las evaluaciones retrospectivas de herramientas de IA están
sistemáticamente desalineadas de la conducta real — el caso mejor documentado tiene a los usuarios
**19% más lentos** mientras estimaban ser **20% más rápidos** (F-488). **Preguntar el martes qué pasó
la semana pasada produce una opinión. Preguntar hoy qué pasó hoy produce un dato.**

⭐ **Y encaja con una restricción que ya conocemos: los asesores tienen la IA bloqueada en la
computadora, así que su uso de ChatGPT y Gemini pasa por el teléfono.** WhatsApp los encuentra
exactamente donde ocurre la conducta que queremos ver.

**A quién:** 6-8 asesores. **Cuándo:** jueves a lunes, un mensaje al final del día.

### Mensaje de apertura *(enviar el jueves)*

> Hola [nombre]. Te escribo porque estamos trabajando en mejorar AIDA, y **el proyecto salió de lo que
> ustedes respondieron en la encuesta**: lo que dijeron sobre la herramienta está documentado y es lo
> que abrió esta conversación con el equipo que la maneja.
>
> Para eso necesito entender cómo la usan de verdad, no cómo debería usarse. Te voy a escribir estos
> días **una sola vez al día, tres preguntas, 30 segundos**. Podés contestar con audio si es más
> rápido.
>
> Dos cosas importantes: **no estamos evaluando a nadie**, estamos evaluando la herramienta. Y **nada
> de lo que me digas individualmente va a jefatura.**

⚠️ **El primer párrafo no es cortesía: es la condición para que la segunda ronda tenga la calidad de
la primera.** Ya opinaron dos veces. Si vuelven a opinar sin ver que la anterior sirvió de algo, el
costo no es que respondan mal — es que dejen de responder.

### Las tres preguntas diarias

> 1. ¿Le preguntaste algo a AIDA hoy? ¿Qué le preguntaste? *(si no, poné "nada")*
> 2. ¿Usaste ChatGPT o Gemini para algo del trabajo? ¿Para qué, y en qué momento del día?
> 3. ¿Hubo algo que necesitabas y no encontraste en ningún lado?

### ⭐ Y el pedido que vale más que las tres preguntas juntas

> **Si AIDA te respondió algo que no te sirvió, mandame captura.** No hace falta que expliques nada,
> con la foto basta.

**Por qué es lo mejor del kit:**
- **Cero fricción** — es más rápido que escribir.
- **Trae el artefacto completo**: la pregunta, la respuesta y **las fuentes que citó** — que es
  exactamente el formato del corpus de fallas.
- ⭐ **Es el banco real de preguntas** que el protocolo dice que debe reemplazar al sintético.
- **No depende de que el asesor sepa explicar qué estuvo mal.**

⚠️ **Sobre la pregunta 2, y es delicado:** enmarcarla siempre como *"queremos saber qué resuelven por
fuera porque eso nos dice qué le falta a AIDA"*, **nunca como si fuera un control de cumplimiento.**
Si se lee como *"estamos viendo si usan herramientas no autorizadas"*, dejan de reportarlo y se pierde
la señal más rica que hay.

---

## 3 · Cuatro entrevistas de incidente crítico

**Cuatro, no ocho.** El muestreo importa más que el número, y con cuatro bien elegidos se saturan los
modos de falla.

| # | A quién | Por qué esa persona |
|---|---|---|
| **1** | ⭐⭐ **El que declaró usarla "nunca"** (1/19) | **La entrevista más informativa que existe.** Decidió que no valía la pena y puede decir exactamente por qué. Rinde más que cinco con usuarios satisfechos |
| **2** | **Un usuario intensivo** (de los 7 que la usan siempre) | Hay que saber **qué no romper** |
| **3** | **Un asesor nuevo** (<6 meses) | Donde se concentra el efecto de un copiloto (+34%, F-476) |
| **4** | **Un asesor experto** | El contraste que hace visible el patrón |

**40 minutos cada una. Agendarlas el jueves para viernes y lunes.**

### Cómo preguntar: incidentes, no opiniones

| ❌ No preguntar | ✅ Preguntar |
|---|---|
| ¿AIDA te da buena información? | Contame **la última vez** que le preguntaste algo y la respuesta no te sirvió. ¿Qué preguntaste? ¿Qué te dijo? ¿Qué hiciste después? |
| ¿Confías en AIDA? | ¿Cuándo fue **la última vez** que verificaste una respuesta suya por otro lado? ¿Con qué la verificaste y cuánto te tomó? |
| ¿Usás ChatGPT? | ¿Cuál fue **lo último** que le preguntaste a ChatGPT o Gemini para el trabajo? ¿Por qué a esa y no a AIDA? |
| ¿Te falta información? | ⭐ ¿Hay algo que **antes le preguntabas a AIDA y ya no**? ¿Qué pasó? |
| ¿Encontrás información contradictoria? | Contame **la última vez** que dos fuentes de RIMAC te dijeron cosas distintas. ¿Cuáles eran? ¿A cuál le hiciste caso? |

⭐ **Dos preguntas nuevas que conviene sumar esta vez:**

> **A.** Cuando usás ChatGPT o Gemini, **¿es antes de hablar con el cliente, durante, o después?**
>
> **B.** Los nueve segundos que tarda AIDA en responder, **¿qué hacés mientras esperás?**

**Por qué A:** si es **durante**, el cuadro es mucho más urgente — significa que hay un modelo
genérico, sin la estrategia de RIMAC, hablándole al cliente en tiempo real por interpósita persona.

**Por qué B:** a nueve segundos ya estamos en el borde del umbral donde la gente cambia de tarea
(F-503). **Si contestan "me voy a otra cosa", eso explica la fuga sin necesidad de invocar la
calidad** — y es un arreglo distinto y más barato.

---

## 4 · Wiser — solo si sobra tiempo, y para magnitudes

Una encuesta da **frecuencias**, no conducta. Sirve para poner número a lo que las entrevistas
describen, no para reemplazarlas. **Máximo 8 preguntas, 3 minutos, pensada para el teléfono.**

> 1. Esta semana, ¿cuántas veces le preguntaste algo a AIDA? *(0 · 1-2 · 3-5 · más de 5)*
> 2. Esta semana, ¿cuántas veces usaste ChatGPT o Gemini para algo del trabajo? *(mismo rango)*
> 3. ⭐ Cuando AIDA te responde algo de producto, ¿lo verificás antes de usarlo con un cliente?
>    *(siempre · casi siempre · a veces · casi nunca · nunca)*
> 4. Si verificás, ¿con qué? *(cartapacio · un colega · el jefe · SharePoint · ChatGPT/Gemini · otro)*
> 5. ¿Hay algo que antes le preguntabas a AIDA y ya no? *(sí/no + abierta)*
> 6. ¿Para qué usás ChatGPT o Gemini? *(múltiple: objeciones · explicar un producto · redactar ·
>    resumir · otra)*
> 7. ¿Qué te haría usar AIDA más de lo que la usás hoy? *(abierta)*
> 8. Antigüedad en la posición *(menos de 6 meses · 6-12 · 1-3 años · más de 3)*

⭐ **La pregunta 3 es la más importante de la encuesta.** Es el proxy de la métrica que decide si el
objetivo declarado se cumple: si todos verifican siempre, **el tiempo de búsqueda no bajó ni cuando
AIDA acierta.**

⚠️ **La 8 no es demográfica de relleno: es el corte obligatorio.** Sin antigüedad, los resultados
describen a un asesor promedio que no existe.

---

## Calendario

| Día | Qué |
|---|---|
| **Jueves** | 🔴 Insistir por los logs · mandar el mensaje de apertura a los 6-8 · agendar las 4 entrevistas · primera bitácora en la noche |
| **Viernes** | Bitácora · 2 entrevistas · lanzar Wiser si Dani lo tiene listo |
| **Sábado** | Bitácora *(un solo mensaje, no molesta)* |
| **Domingo** | ⛔ Nada. **No escribir.** |
| **Lunes** | Bitácora final · 2 entrevistas · cerrar Wiser · analizar los logs |
| **Martes** | ⛔ Nada de campo. Consolidar y armar el deck |

⚠️ **El sábado sí y el domingo no.** Un mensaje el sábado de alguien que sabe que estás trabajando es
tolerable; el domingo quema goodwill y el dato de un día no lo compensa.

---

## Los dos riesgos, y cómo se gestionan

**1 · Ser observado cambia la conducta.** Cualquier asesor que sabe que lo estás mirando va a usar
AIDA más de lo habitual. **La bitácora sobreestima el uso.** Mitigación: triangular siempre contra los
logs, que no tienen ese sesgo, y **nunca compartir registros individuales con jefaturas** — decirlo
explícitamente al abrir.

**2 · ⭐ La deuda de credibilidad, que es el riesgo serio.** Los asesores **ya opinaron dos veces**: 19
en la encuesta, 30 en el taller donde pidieron mejoras concretas. **Si se les pregunta una tercera vez
sin que vean qué produjo lo anterior, el costo no es que respondan mal: es que dejen de responder.**

**Obligación que se sigue:** abrir cada contacto contando **qué produjo lo que dijeron antes**. Está
en el mensaje de apertura de §2 y en la primera línea de cada entrevista. **No es cortesía — es la
condición de que exista una tercera ronda.**

---

## Qué vas a tener el martes, y qué no

| ✅ Vas a tener | ⛔ No vas a tener |
|---|---|
| Las preguntas reales, con volumen y frecuencia *(logs)* | Observación directa del flujo de trabajo |
| Capturas de fallas reales, con sus citas | Cronometraje del ciclo completo con cliente real |
| Uso declarado de ChatGPT/Gemini, con momento y propósito | Línea base sin AIDA |
| Tasa de verificación declarada *(el proxy de T6)* | El salto entre herramientas, visto |
| Cuatro relatos de incidente con contexto y consecuencia | Frecuencias con potencia estadística |
| ⭐ Posible evidencia de **categorías de pregunta que se apagaron** | |

⭐ **Alcanza para el miércoles.** Lo que se pide ese día no es un estudio: es mostrar la brecha entre
lo que AIDA declara hacer y lo que el asesor hace con ella. **Para eso, tres capturas y un relato bien
elegido pesan más que una tabla de frecuencias.**

---

## Conexiones

- `[[aida-roadmap-evaluacion]]` — la otra mitad del trabajo: la auditoría de la herramienta.
- `[[diagnostico-copiloto-ai-asesor-vida-rimac]]` §13 — el diseño completo de trabajo de campo, del
  que este kit es la versión comprimida a cinco días.
- `[[aida-banco-preguntas-corrida]]` — el banco sintético que las capturas de §2 deben reemplazar.
