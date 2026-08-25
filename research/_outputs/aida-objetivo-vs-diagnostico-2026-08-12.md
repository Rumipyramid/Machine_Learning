# AIDA frente a su objetivo

### Qué se propuso lograr, qué muestra el diagnóstico, y qué falta para poder responder la pregunta

> Fecha: 2026-08-12 · CoE de Diseño de Experiencia
> Construido sobre `research/_nodes/aida-copiloto-asesor-rimac.md` (v1.0).
> Evidencia: encuesta a asesores (n=19), análisis auditado de 2.697 consultas de 274 asesores
> (17-18 de agosto de 2026) y el plan de exploratorio cualitativo. Fuentes F-537 a F-541.

---

## 0. El veredicto en cinco líneas

**AIDA se creó para reducir el tiempo de gestión del asesor y, por esa vía, mejorar la conversión.
El diagnóstico no permite afirmar que haya cumplido ninguno de los dos — y en los dos casos por
razones distintas.**

- **Tiempo de gestión:** no se midió el antes, así que no hay contra qué comparar. Y el
  comportamiento que sí se observa no se parece a un ahorro de tiempo: se parece a una **inversión**
  de tiempo. El uso dominante son sesiones de estudio de **35 minutos**.
- **Conversión:** AIDA **falla precisamente en los dos momentos donde se cierra una venta** —cuánto
  cuesta y cómo se emite— y para lo que más impactaría el cierre, la mitad de los asesores ya la
  reemplazó por ChatGPT.
- **Y hay una tercera cosa, que es la más importante:** AIDA sí funciona muy bien, pero **para algo
  distinto de lo que se le pidió**. Eso no es un fracaso: es una decisión pendiente.

---

## 1. El objetivo declarado, y qué habría que medir para darlo por cumplido

| Objetivo | Tipo | Qué habría que medir | ¿Se midió? |
|---|---|---|---|
| **Reducir el tiempo de gestión del asesor** | Directo | Tiempo por tarea antes vs. después, en las mismas tareas | ❌ No hay línea base |
| **Mejorar la conversión** | Indirecto, vía el anterior | Tasa de conversión con y sin AIDA, controlando por asesor y por producto | ❌ No, y el ciclo de venta de Vida excede el plazo del piloto |

⚠️ **Los dos objetivos comparten un problema de origen: ninguno tiene línea base.** No existe una
medición de cuánto tardaba un asesor en resolver una duda de producto antes de AIDA, ni cuánto tarda
ahora. Sin ese antes, ninguna cifra del diagnóstico puede leerse como mejora ni como deterioro.

**Esto no es un defecto del análisis de logs** —que hace bien lo que se propuso hacer— **es un hueco
de diseño del proyecto.** Conviene decirlo antes de que alguien pida "el número de ahorro de
tiempo": ese número no existe y hoy no se puede construir hacia atrás.

---

## 2. Objetivo 1 · Reducir el tiempo de gestión

### 2.1 El uso real es inversión de tiempo, no ahorro

El comportamiento característico de AIDA no es la consulta rápida. Es sentarse a estudiar.

| | |
|---|---|
| Sesiones de 10 o más turnos | **80** |
| Asesores que las hicieron | 62 |
| Consultas que representan | 1.327 — **el 49% de todo el tráfico** |
| **Duración mediana** | **35 minutos** |
| Tiempo agregado dedicado a esas sesiones | del orden de **47 horas en dos días** |

*Estimación conservadora: 80 sesiones × 35 min de mediana. Como la distribución es asimétrica, el
total real es probablemente mayor.*

⭐ **Casi la mitad del uso de AIDA son personas dedicándole media hora seguida a prepararse. Eso no
es reducción de tiempo de gestión — es tiempo de preparación que antes no aparecía en ningún lado.**

**Y hay que ser justo con dos lecturas posibles, porque el dato no distingue entre ellas:**

- **Lectura optimista:** esas 35 minutos reemplazan a algo que antes tomaba más — buscar en PDFs,
  preguntarle al supervisor, esperar respuesta de producto. Sería ahorro real, invisible en el log.
- **Lectura pesimista:** esas 35 minutos son tiempo *nuevo*, que antes no se dedicaba porque el
  asesor simplemente no se preparaba con ese nivel de detalle.

**No tenemos cómo distinguirlas con los datos actuales.** Y la diferencia entre ambas es
exactamente la diferencia entre haber cumplido el objetivo y haberlo cambiado sin decirlo.

### 2.2 El costo de verificación es invisible en el log, y va en contra del objetivo

Un log registra la consulta. **No registra lo que el asesor hace después de recibir una respuesta
que no le convence.**

En Vida, la falla general es **6,0%** — unas **91 respuestas fallidas** sobre 1.522 consultas de
producto. Y en los dos temas críticos, **21 fallas sobre 165 consultas** de precio y contratación.
Cada una de esas fallas no es tiempo neutro:

> **Una respuesta errada cuesta la consulta, más la verificación por otro canal, más —si llegó
> hasta el cliente— la corrección.** Es tiempo negativo, no tiempo cero.

Que esto preocupa internamente ya está reconocido: la guía del exploratorio cualitativo incluye,
textual, la pregunta *"¿cuándo fue la última vez que verificaste una respuesta suya por otro lado?
¿Con qué la verificaste y cuánto te tomó?"*. **Esa pregunta existe porque alguien sospecha que el
costo de verificación es real, y hoy no está medido por ningún lado.**

### 2.3 Sobre la latencia, sin inflarla

La guía de entrevistas menciona que AIDA tarda **nueve segundos** en responder. Vale hacer la
cuenta antes de que alguien la use como argumento:

- Agregado: 2.697 consultas × 9 s ≈ **6,7 horas** de espera en dos días, repartidas entre 274
  asesores. Son **≈44 segundos por asesor por día**.
- **En agregado es despreciable.** No es un problema de eficiencia.

⚠️ **Pero sí es un problema donde el objetivo original lo pone.** Si AIDA se usa —como declara el
Plan Piloto— **en vivo durante la conversación real con el cliente**, nueve segundos de silencio
frente a alguien que espera una respuesta es un problema de experiencia, no de minutos. La cifra
agregada no lo captura y no hay que usarla para negarlo ni para dramatizarlo.

### 2.4 Veredicto sobre el objetivo 1

> **No se puede afirmar que AIDA haya reducido el tiempo de gestión, ni que lo haya aumentado.**
> No hay línea base. El único patrón observable —sesiones de 35 minutos— es compatible tanto con
> ahorro como con inversión adicional, y el costo de verificación de las fallas no está medido.

---

## 3. Objetivo 2 · Mejorar la conversión

### 3.1 AIDA falla precisamente en los dos momentos donde se cierra una venta

De ocho temas de producto en Vida, solo dos quedan claramente peor que el promedio de 6,0%:

| Tema | Consultas | Fallas | Rango 95% |
|---|---|---|---|
| **Precio, prima y montos** | 121 | 15 | **7,7 – 19,4%** |
| **Contratación y emisión** | 44 | 6 | **6,4 – 26,7%** |
| *(referencia)* Rentabilidad, retiros e inversión | 290 | 9 | 1,6 – 5,8% |

⭐ **No es casualidad ni mala suerte: son los dos únicos temas que no dependen de la ficha del
producto sino de las reglas de operación del negocio** — scoring, autonomías comerciales, tarifas
por edad y suma asegurada, sobreprimas, requisitos de suscripción.

Y son, exactamente, **cotizar y emitir**: las dos actividades que consumen tiempo de gestión y las
dos que están más cerca de la conversión. Las preguntas que no pudo responder no son exóticas:

> *"¿Cuál es la prima mínima de Vida Contigo?"*
> *"¿Cuál es el monto mínimo para incrementar la suma asegurada en Vida Ahorro Garantizado?"*
> *"¿La condromalasia genera sobreprima en un seguro de vida Temporal Total?"*
> *"¿Cuál es el procedimiento para solicitar un cambio de suma asegurada?"*

**La causa está medida y no es el modelo.** De 6.165 citas en respuestas de Vida: **77% son fichas
y brochures, 9,6% condiciones generales, y solo 3,4% reglas de operación**. Los dos temas que
fallan son exactamente los que no tienen documentos cargados.

### 3.2 Para lo que más impactaría la conversión, ya la reemplazaron

Los asesores señalan desde tres preguntas independientes de la encuesta que su mayor carencia está
en **objeciones y cierre** — 68% dice que las herramientas ayudan poco, 42% pide objeciones como
capacitación prioritaria, 42% señala el cierre como el momento con menos apoyo.

Y el log muestra qué pasó cuando se lo pidieron a AIDA:

| Tipo de pedido | Asesores | Preguntaron 1 sola vez | Falla | Bloqueo del filtro |
|---|---|---|---|---|
| Producto | 267 | 18% | 6,7% | 0,6% |
| *"Escríbeme una pieza"* | 85 | 32% | 4,7% | 3,0% |
| **"Enséñame a vender"** | **50** | **66%** | **8,9%** | **4,4%** |

⭐ **Cincuenta asesores le pidieron a AIDA que les enseñara a vender. Treinta y tres no volvieron a
intentarlo.**

Y **53% de los encuestados menciona ChatGPT, Gemini o Copilot por iniciativa propia**, con la IA
bloqueada en la computadora — sacan el teléfono en medio de la jornada. Nadie preguntó por IA
externa: salió solo, en una pregunta abierta.

> **En el punto donde el objetivo de conversión se juega, AIDA no está compitiendo contra el statu
> quo. Está compitiendo contra ChatGPT, y está perdiendo.**

### 3.3 Y aunque funcionara, hoy no sería atribuible

El propio Plan Piloto declara los indicadores comerciales fuera de alcance: **el ciclo de venta de
Vida excede el plazo del piloto**, de modo que un movimiento en conversión sería direccional, no
concluyente.

Es decir: **el objetivo indirecto no es medible con el diseño actual**, independientemente de que
AIDA funcione bien o mal.

### 3.4 Veredicto sobre el objetivo 2

> **No hay evidencia de que AIDA haya mejorado la conversión, y el diseño actual no permite
> obtenerla.** Lo que sí se puede afirmar es más incómodo: **falla de forma medible en los dos
> momentos donde se cierra una venta, y en el tercero —objeciones y cierre— ya fue sustituida.**

---

## 4. La divergencia entre el objetivo y el uso, que puede ser buena noticia

Hasta acá el informe suena a fracaso. No lo es, y sería un error presentarlo así.

| | Lo que se buscaba | Lo que ocurre |
|---|---|---|
| **Momento de uso** | Durante la gestión, para acelerarla | **Antes**, para prepararse |
| **Uso dominante** | Apoyo transaccional y comercial | **84% consultas de producto** |
| **Comportamiento** | Consulta rápida | **Sesión de estudio de 35 min** |
| **Dónde funciona** | En el cierre | **En el estudio del producto** |

**Y donde ocurre, funciona bien:**

- **97% de los asesores** (267 de 274) hizo al menos una consulta de producto.
- **86% vuelve** después de la primera consulta.
- Dentro de las sesiones de estudio la falla es **5,8%**, *mejor* que el promedio.
- ⭐ **Ningún asesor menciona la información de producto como una necesidad insatisfecha.** Es el
  uso más grande de la herramienta y nadie se queja de él — porque funciona. Un silencio que
  confirma vale más que una cifra.

> **AIDA es un buen producto de capacitación y consulta técnica que se especificó como herramienta
> de productividad comercial.**

**La decisión que esto abre para dirección no es "arreglar o matar". Son dos caminos legítimos:**

1. **Reapuntar el objetivo** a lo que ya funciona: reconocer a AIDA como herramienta de estudio y
   consulta de producto, y medirla como tal (cobertura de producto, tiempo hasta encontrar el dato,
   fallas por producto). Es el camino barato y el que tiene evidencia a favor.
2. **Sostener el objetivo original** y aceptar que exige un trabajo que hoy no está hecho: cargar
   las reglas de operación, y rediseñar por completo el modo comercial.

**No son excluyentes, pero sí son secuenciales:** el camino 2 no puede empezar antes de que exista
la documentación del camino 1.

---

## 5. Lo que habría que hacer para poder responder la pregunta

Ordenado por relación valor/esfuerzo.

**1 · Cargar las reglas de operación de precio y emisión.** Es la única acción del listado que
ataca directamente los dos objetivos a la vez: reduce el tiempo perdido en verificar y cierra la
falla en los dos momentos de la venta. **Y no requiere tocar el modelo** — es carga documental.
El caso de rentabilidad lo demuestra: es el único tema claramente mejor que el promedio, y la razón
es que **consulta una herramienta con datos vivos en vez de un documento**.

**2 · Medir el costo de verificación.** Cuántas veces el asesor va a otra fuente después de una
respuesta de AIDA, y cuánto le toma. Es la variable que decide si AIDA ahorra o cuesta tiempo, y
hoy es invisible. La pregunta ya está en la guía del exploratorio: hay que ejecutarla.

**3 · Construir la línea base que falta, aunque sea hacia adelante.** Cronometrar un conjunto
acotado de tareas frecuentes (encontrar la carencia de un producto, calcular una prima mínima,
resolver una objeción) con y sin AIDA, en una muestra chica. No da causalidad, pero da la
comparación que hoy no existe.

**4 · Segmentar el uso por desempeño comercial del asesor.** La data ya existe —274 asesores
identificados— y la literatura de copilotos de venta dice que las ganancias **no se reparten
parejo**: siguen una U invertida, donde el tramo medio gana más, los de abajo sufren sobrecarga de
información y los de arriba muestran aversión (Luo, Qin, Fang y Qu, 2021, *Journal of Marketing*,
experimentos de campo aleatorizados). **Hoy el promedio está tapando tres comportamientos
distintos.**

**5 · Reducir el modo comercial en vez de enriquecerlo.** Las respuestas comerciales de AIDA son de
**483 palabras contra 188 de producto**. Ante el 66% de abandono, el instinto es mejorar y ampliar
la respuesta. **El experimento de campo dice lo contrario:** al restringir el nivel de feedback del
coach, el desempeño de los agentes de menor rendimiento mejoró significativamente. Es la
recomendación más barata y la más contraintuitiva del informe.

**6 · Confirmar qué es `coach_mode` con el equipo técnico.** El 43% de los pedidos comerciales se
procesa por el camino equivocado, y ahí la falla se multiplica por cuatro. Es una inferencia
razonable pero **no confirmada**, y si es correcta es un arreglo de bajo costo con efecto directo
sobre el objetivo de conversión.

---

## 6. Lo que este informe no puede afirmar

- **No dice que AIDA no reduzca el tiempo de gestión.** Dice que **no se midió** y que el patrón
  observable es ambiguo. La ausencia de evidencia no es evidencia de ausencia.
- **No dice que AIDA empeore la conversión.** Dice que falla en los momentos donde la conversión se
  juega, y que no existe la medición que permitiría atribuir un efecto en ninguna dirección.
- **Dos días de datos**, lunes 17 y martes 18 de agosto. Sin cierre de mes ni campaña — justo los
  momentos donde la presión comercial, y por lo tanto el uso comercial, sería mayor.
- **La encuesta es n=19 sobre 200+**, autoseleccionada.
- **Las tasas de falla son un piso.** El detector solo captura fallas totales, no **parciales** —
  respuestas que contestan algo pero no lo que se preguntó. El problema real es igual o mayor,
  nunca menor.
- **No hay contrafactual.** No sabemos qué tan bien resolvería el asesor la misma consulta sin
  AIDA, ni qué tan bien la resuelve ChatGPT — que es la comparación que los asesores ya hacen todos
  los días con su celular.

---

*Documento interno · CoE de Diseño de Experiencia, RIMAC. Cifras agregadas, sin identidad de
asesores ni de clientes.*
