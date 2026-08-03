# RIMAC ya sabe quién se va a ir. El problema es que no sabe por qué.

> Explicación en lenguaje simple del análisis técnico de churn (fuga de clientes) y
> renovación de RIMAC, con la opinión de negocio de **El Lobo** y la validación externa de
> **`/trinidad`** (investigación que cruza evidencia académica, de negocio y social).
> Pensado para leerse sin conocimiento previo de analítica de datos.
> Basado en: `research/_nodes/modelo-churn-renovacion-rimac.md` (v1.0) y
> `research/lobo/opinion_experto.md` (tesis 21) del proyecto `Rumipyramid/Machine_Learning`.
> 2026-07-30.

---

## La idea central, en una frase

RIMAC construyó modelos que **predicen con muchísima precisión qué clientes están por
irse** — mejor que el promedio de lo que logran otras empresas del sector, según lo que
encontramos comparando con estudios publicados. Pero **nadie en la empresa sabe todavía por
qué se van** la mayoría de esos clientes. Es como tener un radar excelente que avisa "va a
llover en tu zona el jueves" — pero sin saber si va a llover por una tormenta, por el mar o
por el deshielo. Sin esa segunda pieza de información, es difícil decidir si conviene llevar
paraguas, cerrar ventanas o simplemente cancelar el paseo.

---

## 1. ¿Qué son estos modelos, en términos simples?

RIMAC construyó, con su equipo interno de IA, un conjunto de "calculadoras de riesgo" que
revisan la información de cada cliente (cuánto paga, hace cuánto es cliente, qué productos
tiene, cómo se le contactó, etc.) y le asignan una nota: **¿qué tan probable es que este
cliente se vaya en los próximos meses?**

Hay dos familias de estos modelos:

- **Modelos de "fuga" (Churn):** miran a todos los clientes de RIMAC (1.8 millones) y
  predicen quién va a cancelar su póliza — separando dos motivos distintos: porque **dejó
  de pagar** (morosidad) o porque **decidió activamente cancelar** (pedido del cliente).
- **Modelos de "renovación":** miran solo a los clientes que están por renovar su póliza de
  auto (VEH) o de salud (AMI) y predicen dos cosas para cada uno: **¿va a seguir siendo
  cliente los próximos 12 meses?** y **¿va a tener un accidente/atención médica costosa en
  ese periodo?**

### ¿Qué tan buenos son estos modelos?

Aquí está el primer hallazgo importante, y es una **buena noticia poco reconocida
internamente**: si RIMAC solo mirara a los 3 de cada 10 clientes más riesgosos de su base
(el 26-36% con la nota más alta), ya estaría encontrando a **9 de cada 10 clientes que
realmente se van a ir** (79-91% del total, según el modelo).

Comparamos esto contra lo que dice la literatura especializada sobre modelos parecidos en
otras empresas de seguros: normalmente, para atrapar 9 de cada 10 casos hace falta mirar a
la **mitad** de la base de clientes, no a un tercio. Es decir, **los modelos de RIMAC son
notablemente más eficientes que el estándar de la industria** — necesitan revisar mucha
menos gente para encontrar casi a los mismos "sospechosos".

**🐺 El Lobo dice:** *"La capacidad técnica ya no es el problema. RIMAC construyó un buen
radar. El problema es que el radar te dice 'este cliente se va' pero no te dice 'porque
subieron el precio', 'porque tuvo mal servicio' o 'porque otra aseguradora le ofreció
algo mejor' — y sin esa segunda pieza, cualquier campaña para retenerlo es un tiro a
ciegas."*

---

## 2. El hallazgo más importante: la mayoría se va por decisión propia, no por falta de pago

Cuando un cliente cancela su seguro, hay dos motivos posibles:

- **Dejó de pagar** (morosidad): 4 de cada 10 casos (41%).
- **Pidió cancelar activamente** (decisión propia): **6 de cada 10 casos (59%)**.

La mayoría de los clientes que se van, **se van porque quieren irse**, no porque no puedan
pagar. Y aquí está el vacío más grande de todo el análisis: **ningún documento de RIMAC
registra por qué deciden irse.** ¿Es el precio? ¿Un mal servicio? ¿Una oferta de la
competencia? Hoy, nadie lo sabe con certeza.

Buscamos si esto es normal en la industria de seguros, o si es algo raro de RIMAC. **No es
raro — es una tendencia mundial que está creciendo:** en Estados Unidos, cerca de 3 de cada
10 asegurados cambiaron de compañía en 2025, sobre todo por el aumento acumulado de precios.
Y algo todavía más revelador: **6 de cada 10 clientes cambiarían de aseguradora por mejor
atención, no por un precio más bajo** — incluso entre los que dicen estar "satisfechos", 3
de cada 10 están pensando en irse. Es decir: el fenómeno que ve RIMAC (la gente se va por
decisión propia, no solo por no poder pagar) es parte de algo mucho más grande que está
pasando en todo el sector asegurador.

**🐺 El Lobo dice:** *"Esto no es un problema de RIMAC solamente — es la ola que está
pegando en todo el sector. Pero eso no es excusa para no medirlo. Al contrario: si es una
ola que crece, medir la causa raíz hoy es más urgente, no menos."*

---

## 3. Un mismo modelo, dos ramos de negocio, un resultado sorprendente

RIMAC construyó estos modelos por separado para **autos (VEH)** y para **salud individual
(AMI)**. Al comparar los dos, encontramos un patrón que **ningún documento de RIMAC había
señalado** — lo calculamos cruzando sus propias tablas.

### En autos (VEH): todo funciona como se esperaría

Los clientes que el modelo predice que se van a ir pronto, y los que van a tener un choque o
accidente, son en su mayoría **grupos distintos de personas**. Un cliente que probablemente
no va a renovar su seguro no es, por esa sola razón, más o menos propenso a chocar. Tiene
sentido: manejar bien o mal un auto no tiene mucho que ver con si uno decide seguir pagando
el seguro.

### En salud (AMI): el patrón se invierte

Aquí pasa algo distinto: **los clientes que el modelo predice que se van a ir (baja
persistencia) son, a la vez, los que más van a usar el seguro (más atenciones médicas)**. Y
al revés: los clientes más fieles son los que menos lo usan.

Esto tiene sentido si se piensa un momento: **un seguro de salud se usa todo el tiempo**
(consultas, chequeos, tratamientos), no solo cuando pasa algo grave como en un auto. Alguien
que está usando mucho su seguro de salud en este momento —quizás porque está en tratamiento
de algo— es también alguien más sensible al precio o a las condiciones cuando llega el
momento de renovar.

Buscamos en estudios académicos de seguros de salud si este patrón ya se conoce, y **sí** —
hay investigación seria (2026) que documenta que, en seguros de salud, la gente que decide no
renovar suele tener un historial de uso distinto de la que sí se queda. Es exactamente el
tipo de fenómeno que RIMAC está viendo. **Con una salvedad importante:** los estudios miden
esto mirando hacia atrás (gente que ya se fue), mientras que el modelo de RIMAC lo predice
hacia adelante (gente que todavía no decidió). Se parece mucho, pero no es exactamente lo
mismo — así que lo tratamos como "muy probable, no 100% confirmado".

**Lo que no se sabe todavía, y que cambiaría la jugada:** ¿el cliente usa mucho el seguro y
por eso decide irse (por el costo)? ¿O tiene un accidente/atención costosa y eso lo empuja a
irse (por una mala experiencia con el reclamo)? Son dos películas distintas con el mismo
final, y **RIMAC hoy no tiene forma de saber cuál es la correcta** con la información
disponible.

**🐺 El Lobo dice:** *"Este es el hallazgo que más me interesa de todo el análisis. Si el
cliente se va porque el seguro le sale caro justo cuando más lo necesita, la jugada es hablar
de precio y valor. Si se va porque tuvo una mala experiencia cobrando un reclamo, la jugada
es arreglar el proceso de atención de siniestros. Son dos soluciones completamente distintas,
y hoy RIMAC no sabe cuál de las dos aplica."*

---

## 4. Lo que cuesta cada ramo, en plata

| | Autos (VEH) | Salud (AMI) |
|---|---|---|
| Clientes en riesgo de no renovar | 5,500 | 4,100 (menos clientes, pero...) |
| % que sí renueva | 82 de cada 100 | 88 de cada 100 |
| Plata que se pierde porque el cliente no dura los 12 meses | ~$470,000 | **~$1,180,000** |
| Plata que se pierde por siniestros/atenciones caras | ~$1,000,000 | **~$1,540,000** |

**Aunque hay menos clientes de salud en riesgo que de auto, las pérdidas de salud son mucho
más grandes** — más del doble en el caso de la no-renovación. Esto confirma que, aunque el
ramo de autos tiene más volumen, **el ramo de salud es donde se está quemando más plata por
cliente**.

---

## 5. Cosas que encontramos en los documentos que hay que arreglar (no son errores del
modelo, son errores de cómo se armó la presentación)

Al revisar los archivos originales de RIMAC, encontramos varios detalles que conviene
corregir antes de compartir estos documentos fuera del equipo que los hizo:

- **Una lámina de la presentación de salud dice "auto" por error** (quedó mal copiada de la
  presentación de autos).
- **Hay una tabla con un campo que quedó vacío** (el ingreso promedio de los clientes de
  auto, en un segmento) — sin esa cifra, ese modelo específico no se puede usar todavía para
  decidir a quién contactar.
- **Dos números que deberían ser distintos aparecen exactamente iguales** en dos segmentos
  distintos de riesgo en salud — puede ser correcto, o puede ser un error de copiado. Hay que
  confirmarlo contra el archivo original antes de usarlos.
- **Una misma palabra ("% Efectividad") significa cosas distintas en cada uno de los dos
  documentos** — en uno mide "cuánto del problema total resuelvo mirando aquí", en el otro
  mide "qué tan seguro estoy de acertar con este grupo". Si alguien compara los dos
  documentos sin saber esto, va a leer mal los números.
- **4 láminas de la presentación de renovación están ocultas** — no se ven si alguien
  proyecta la presentación, aunque sí forman parte del modelo que se usa.

Ninguna de estas cosas invalida el trabajo — son detalles de "limpieza" antes de que el
documento circule más ampliamente.

---

## 6. ¿Qué tan seguros podemos estar de que "gestionar" a estos clientes realmente funciona?

Un punto importante que hay que tener claro: **todo lo que se midió hasta ahora es qué tan
bien el modelo habría acertado en el pasado** — no qué pasa cuando RIMAC efectivamente le
escribe, llama o le hace una oferta a un cliente en riesgo. Es la diferencia entre "el
pronóstico del tiempo acertó ayer" y "el paraguas que compramos realmente nos mantuvo
secos". Ambas cosas son importantes, pero son preguntas distintas.

RIMAC ya tiene planeado un **piloto** (una prueba real, a menor escala, para confirmar si
gestionar a estos clientes efectivamente reduce cuántos se van) — pero todavía no tiene
fecha. Es el paso que falta para pasar de "sabemos identificar a quién le puede pasar esto"
a "sabemos que hacer algo al respecto funciona".

---

## 7. Qué haría El Lobo — oportunidades y riesgos, en plata y en simple

### 💰 Oportunidades

1. **Preguntarle al cliente por qué se va, no solo predecir que se va.** Algo tan simple
   como una encuesta corta al momento de cancelar (2-3 preguntas) ya empezaría a cerrar el
   vacío más grande de todo este análisis.
2. **No tratar a todos los que se van a ir de la misma forma.** El que deja de pagar necesita
   ayuda para pagar (recordatorios, más formas de pago, flexibilidad de fecha). El que
   cancela por decisión propia necesita que le resuelvan el motivo real — un descuento
   genérico puede no servir si el problema es otro.
3. **En salud, diseñar una oferta específica para el grupo "usa mucho el seguro y está por
   irse".** Es el grupo que más plata puede hacer perder dos veces (se va, y mientras se
   queda, cuesta caro) — y hoy no existe una jugada pensada específicamente para él.
4. **Aprovechar que RIMAC ya sabe *cuándo* actuar.** Los modelos ya calculan con precisión la
   ventana de tiempo antes de que el cliente se vaya (2 a 4 meses de anticipación, según el
   modelo) — coincide con lo que dicen estudios externos sobre cuándo la gente realmente
   decide cancelar. Ese "cuándo" ya está resuelto; hay que usarlo mejor.

### ⚠️ Riesgos

1. **Confundir "el modelo es bueno para predecir" con "ya sabemos que funciona intervenir".**
   Todavía no hay una prueba real de que contactar a estos clientes efectivamente los
   retenga — eso recién se sabrá con el piloto.
2. **Comparar los dos documentos (Churn y Renovación) sin saber que una misma palabra
   significa cosas distintas en cada uno** — riesgo de que alguien tome una decisión basada
   en una lectura cruzada equivocada.
3. **Corregir los detalles de las láminas antes de que el documento circule más** — ninguno
   es grave, pero juntos le restan seriedad al trabajo si alguien de fuera del equipo los
   nota primero.

---

## 8. En una sola idea, para llevarse

RIMAC no necesita mejorar su capacidad de **predecir** quién se va — ya lo hace mejor que el
promedio del mercado. Necesita invertir en entender el **por qué**, y en probar si actuar
sobre esa predicción realmente cambia el resultado. El radar ya funciona; falta el
meteorólogo que explique qué tipo de lluvia viene, y falta comprobar que el paraguas
efectivamente nos mantiene secos.

---

*Este resumen simplifica, sin cambiar el sentido, el análisis técnico completo disponible en
`research/_outputs/analisis-churn-renovacion-rimac-2026-07-30.md` (con todas las tablas de
datos y el detalle lámina por lámina) y en `research/_nodes/modelo-churn-renovacion-rimac.md`
(v1.0). La validación externa está registrada como F-388 a F-392 en
`research/fuentes/codice.md`, y la opinión de negocio completa en
`research/lobo/opinion_experto.md` (tesis 21).*
