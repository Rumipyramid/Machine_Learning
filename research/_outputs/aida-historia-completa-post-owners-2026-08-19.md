# AIDA — la historia completa

### Lo que la presentación dejó abierto, lo que respondió la owner, y lo que el diagnóstico terminado confirma

> Fecha: 2026-08-19 · CoE de Diseño Estratégico
> **Complementa** la presentación *«AIDA frente a su propia promesa»* (owners, 19-ago-2026), que se
> construyó **antes** de cerrar el diagnóstico.
> **Insumos nuevos:** conversación con Radiye (owner actual de AIDA) y el análisis auditado de
> 2.697 consultas de 274 asesores.
> Base de conocimiento: `research/_nodes/aida-copiloto-asesor-rimac.md` · fuentes F-537 a F-541.

---

## 0. Qué cambió desde la presentación

La presentación se armó con una **lectura preliminar** y cerraba pidiendo tres cosas. Desde
entonces pasaron dos cosas: **el diagnóstico se completó** y **la owner respondió**.

**El titular es bueno y conviene decirlo primero:** ninguna de las dos novedades desmiente el
relato. Lo **precisa**, lo **hace más defendible** y —en dos puntos— **lo mejora**.

| | Estado en la presentación | Estado hoy |
|---|---|---|
| El objetivo declarado de AIDA | *"Lo pedimos, no lo teníamos"* | ✅ **Confirmado en primera persona por la owner** |
| Por qué conviven "la uso" y "no me sirve" | Inferencia del equipo | ✅ **Explicado: el uso está en los objetivos del asesor** |
| La causa raíz documental | Hipótesis del CoE | ✅ **La owner llegó a lo mismo por otro camino** |
| Sobre qué corre AIDA | *"Necesitamos saberlo"* | ⚠️ **Sigue abierto, y apareció una inconsistencia** |
| Compromiso de actualización de Producto | *"Es la condición que no podemos resolver"* | ⚠️ **Confirmado como no resuelto — y sabemos por qué** |
| Los seis arreglos | Sin eje de factibilidad | ✅ **Tenemos la mitad del eje** |

---

## 1. El objetivo declarado, en palabras de la owner

Era el pedido 01 de la última lámina. Está respondido, textual:

> **Melissa:** *"¿Podríamos decir que fue para un tema de consolidación de información para el
> asesor y justamente reducir en tiempos de búsqueda?"*
> **Radiye:** *"Ese fue el objetivo."*

**AIDA nace como parte de una iniciativa estratégica de IA del año pasado**, con dos frentes:
Central de Consultas (→ *AIDA Service*) y la fuerza de ventas (→ *AIDA Sales*). Comparten
arquitectura; **lo que difiere es la base de conocimiento**, y las dos bases —ambas en
SharePoint— **son independientes y no conversan entre sí**. *AIDA Sales* está en producción
**desde mayo de 2025**.

### ⭐ El objetivo real es más angosto que la vara que usamos, y eso mejora la conversación

La presentación midió a AIDA contra **tres funciones declaradas**. La owner declara **una sola**:
consolidar información y reducir tiempo de búsqueda. El soporte comercial aparece en su
descripción, pero **como funcionalidad construida, no como objetivo medido**:

> *"También tiene funcionalidades como genera switches de venta personalizados, genera cuadros
> comparativos entre planes."*

**Por qué esto es una buena noticia y no una corrección incómoda:**

1. **La función 3 (consultar producto) es el objetivo central, y ahí el diagnóstico es más duro,
   no más blando.** Si el propósito declarado es que el asesor encuentre rápido la información
   correcta, entonces fallar 7,7–19,4% en precio y 6,4–26,7% en contratación **es fallar en el
   objetivo, no en un extra**.
2. **La función 2 (soporte comercial) deja de ser un incumplimiento y pasa a ser algo peor de
   diagnosticar y más fácil de conversar: una capacidad que se construyó sin criterio de éxito.**
   Nadie definió qué debía lograr, así que nadie podía notar que el 66% de quienes le pidieron que
   les enseñara a vender no volvió a intentarlo.
3. **La función 1 (centralizar) sí estaba mal calificada en la presentación.** Ver §5.

**Ajuste de relato sugerido:** en vez de *"AIDA declara tres funciones y esas tres son la vara"*,
decir **"AIDA tiene un objetivo declarado y dos capacidades construidas sin criterio de éxito"**.
Es más preciso, más justo con el equipo que la construyó, y deja el foco donde el diagnóstico
pega más fuerte.

---

## 2. ⭐ La paradoja de la lámina 5 tiene explicación, y es mejor que la inferencia

La presentación decía: *"Las dos cosas solo conviven si el uso no lo está moviendo la utilidad. Lo
mueve la métrica de uso."* Era una inferencia razonable. **Ahora hay algo más fuerte.**

**Primero: la owner confirma que lo que se mide es adopción, no utilidad.**

> **Felipe:** *"Entonces el objetivo es la métrica de adopción."*
> **Radiye:** *"Sí, la cantidad de consulta, la cantidad de consultas diarias, el promedio de
> consultas diarias y la actividad."*

Los dashboards de seguimiento reportan: **cantidad de consultas, ratio de feedback positivo/negativo
y margen de error**. Nada mide si el asesor resolvió lo que vino a resolver, ni cuánto tiempo se
ahorró — que era el objetivo.

**Segundo, y es el hallazgo más importante de toda la conversación:**

> **Melissa:** *"¿Hubo algún tipo de incentivos, o no se metió dentro de los indicadores de los
> asesores para incentivar ese uso?"*
> **Radiye:** *"Están en su business, en su val."*

⭐⭐ **El uso de AIDA está dentro de los objetivos de valoración del asesor.**

**Esto cierra el argumento de la lámina 5 sin necesidad de inferir nada.** "La uso" y "no me sirve"
conviven porque **usarla es parte de lo que al asesor se le mide**. La métrica de adopción no es
neutral: está atada a un incentivo.

**Y obliga a un ajuste honesto de nuestro propio diagnóstico.** Las cifras de adopción del análisis
de logs —**274 asesores, 86% de retorno, 97% de uso de producto**— **no son adopción voluntaria
pura**. Parte de ese volumen es cumplimiento de meta.

⚠️ **Ojo con el alcance de esta advertencia, porque es fácil pasarse:** contamina las cifras de
**adopción**, no las de **calidad**. Una respuesta fallida es fallida haya sido la consulta
voluntaria u obligada. Los cuatro hallazgos del diagnóstico se sostienen enteros. Lo que hay que
dejar de decir es *"los asesores adoptaron AIDA"* como señal de valor.

⭐ **Y hay un matiz que juega a favor y conviene no perder:** el patrón de **sesiones de estudio de
35 minutos de mediana, que son el 49% del tráfico**, es muy difícil de explicar por incentivo. Nadie
cumple una meta de uso con media hora de consultas encadenadas sobre el mismo producto. **Ese uso
parece genuino**, y es justamente donde AIDA funciona mejor (5,8% de falla, mejor que el promedio).

---

## 3. El diagnóstico terminado confirma la lectura preliminar, y le pone número

La presentación cerraba la lámina de brechas con *"Lectura preliminar. Se cierra con los resultados
de la auditoría estructurada."* Ya cerró: **2.697 consultas reales de 274 asesores**, con las cifras
re-derivadas desde un único script y verificadas una por una.

| Lo que decía la presentación | Lo que el diagnóstico confirma |
|---|---|
| *"El problema no es la función [comercial], es el material del que los construye"* | 428 consultas comerciales · **66% de los que pidieron "enséñame a vender" no volvieron** · falla 8,9% y bloqueo del filtro 7× mayor que en producto |
| *"La arquitectura está; lo que no está es el contenido en la forma que puede leer"* | De 6.165 citas: **77% folletos y fichas · 9,6% condiciones generales · 3,4% reglas de operación** |
| *"Los asesores ya resolvieron por fuera"* | **53%** menciona ChatGPT/Gemini **por iniciativa propia**, con la IA bloqueada en la computadora |

**Y agrega dos cosas que la presentación no podía tener:**

**⭐ Dónde falla, exactamente.** De ocho temas de producto en Vida, solo dos quedan claramente peor
que el promedio de 6,0%: **precio (7,7–19,4%)** y **contratación y emisión (6,4–26,7%)**. Son los
dos únicos que **no dependen de la ficha del producto sino de las reglas de operación del negocio**
— y son, exactamente, cotizar y emitir.

**⭐ La prueba limpia de que el problema no es el modelo.** *Rentabilidad* es el único tema
claramente **mejor** que el promedio (1,6–5,8%), y la razón es que **no sale de un documento: sale
de una herramienta conectada con valores reales de portafolio**. Cuando AIDA tiene un dato vivo,
acierta. Es el argumento de la lámina 7 —*"el problema está en la biblioteca de la que lee"*—
demostrado con datos propios, adentro.

---

## 4. ⭐ La causa raíz ya es compartida: no hay que convencer a nadie

Esto cambia el tono de la conversación con el equipo de AIDA, y para bien.

> **Radiye:** *"Principalmente ya en los últimos meses cualquier feedback negativo estaba más en
> relación a alguna documentación que no estaba actualizada o alguna documentación que no estaba
> completa."*

Y sobre cómo funciona el modelo:

> *"El modelo no genera ningún tipo de información. El modelo lo que hace es interpreta la base de
> conocimientos, identifica qué es lo que se está consultando y sobre esa información responde."*

**La owner llegó al mismo diagnóstico que nosotros, por un camino completamente distinto** —ella
desde el feedback de los asesores, nosotros desde el conteo de 6.165 citas documentales. **Dos
métodos independientes, la misma causa raíz.**

**Consecuencia para la presentación:** la lámina 7 (*"el problema no está en el modelo, está en la
biblioteca"*) **no necesita defenderse: ya es consenso**. Conviene presentarla como acuerdo, no como
hallazgo. El desacuerdo, si aparece, no va a estar en el qué — va a estar en el quién y el cuándo.

---

## 5. Una corrección que nos toca hacer: la función 1 no está "sin avance"

La presentación calificó *"Centralizar el conocimiento y los recursos del asesor"* como **Sin
avance**. La transcripción muestra que eso ya no es exacto:

> **Radiye:** *"Es un poco lo que estamos haciendo con Jaime, que sale de las mesas de trabajo de
> los jueves… todo lo que están actualizando del manual, de los catálogos de beneficios, todo eso
> se está centralizando a través de AIDA."*

**Hay un flujo de centralización activo**, con cadencia semanal y un interlocutor con nombre.
Corresponde actualizar ese estado a **Parcial / en curso**, y —mejor aún— **presentarlo como el
punto de apoyo del plan en vez de como una falla**: la vía por la que entran los seis arreglos de
contenido ya existe y ya está funcionando.

⚠️ Lo que sí sigue siendo cierto de esa lámina: **Sales Coach no está integrado de ninguna forma**,
y el conocimiento sigue viviendo también en el cartapacio y en el onboarding.

---

## 6. ⭐ El problema no es dificultad: es ownership sin nombre propio

Era el pedido 03 de la última lámina —*"un compromiso de actualización desde Producto"*— y la
respuesta confirma que sigue sin resolverse, pero **explica por qué**.

> **Felipe:** *"¿Quién tiene el ownership de cada carpeta?"*
> **Radiye:** *"Cada ramo vela porque sus características estén bien."*
> **Melissa:** *"¿Hay como un analista que se encarga de velar por la información?"*
> **Radiye:** *"Claro, internamente no… tipo, tengo el software macro, pero claro, internamente
> cómo se organicen."*

Y al mismo tiempo:

> *"Lo más sencillo es agregar base de conocimiento. Cargar nueva base de conocimientos es lo más
> sencillo."*

⭐ **Poner las dos frases juntas es el argumento más fuerte que tenemos para la sesión:**

> **Arreglar el contenido es lo técnicamente más fácil que se puede hacer con AIDA. Lleva sin
> hacerse quince meses. La razón no es la dificultad — es que la responsabilidad está repartida
> entre ramos y no asignada a nadie en particular.**

Eso convierte el pedido 03 de *"queremos un compromiso"* —que suena a buena voluntad— en algo
concreto y verificable: **un dueño nominal por ramo, con fecha de vigencia por documento**. Es
exactamente el arreglo 01 de la lámina 8 (*"una sola versión vigente por producto, con dueño y
fecha"*), y ahora tiene la evidencia de por qué es el bloqueante.

---

## 7. ⭐ Los seis arreglos ya tienen la mitad del eje horizontal

La lámina 9 decía: *"Nosotros llegamos con el eje vertical… lo que no tenemos es el eje horizontal.
Cuánto cuesta cada arreglo, qué se puede tocar y en qué orden, solo lo saben ustedes."*

**Radiye dio parte de esa información en la conversación**, y separa los seis en dos rutas muy
distintas:

**Ruta corta — contenido.** Entra por el flujo que ya existe (mesas de los jueves, con Jaime). La
owner lo llama textualmente *"lo más sencillo"*. **Sin presupuesto, sin desarrollo.**

| # | Arreglo | Por qué es ruta corta |
|---|---|---|
| 01 | Cerrar el catálogo de producto | Es carga y limpieza de base de conocimiento |
| 02 | Cargar el modelo de venta | Ídem — el Playbook seccionado |
| 03 | Sacar del índice lo que no debe responder | Ídem — eliminación de documentos |
| 04 | Convertir las láminas en cuadros | Ídem — reemplazo de material |

**Ruta larga — producto.** Requiere **solicitud del negocio con captura de valor**, evaluada por una
*metodología de fricción de la demanda*, y **presupuesto para recursos "estafiables"** — personas del
equipo de IA que no están asignadas al BAU y que el negocio tiene que pagar.

| # | Arreglo | Por qué es ruta larga |
|---|---|---|
| 05 | Evaluar la consistencia de las respuestas | Es instrumentación nueva, no contenido |
| 06 | Que la pantalla no arranque en blanco | Es cambio de interfaz/lógica del producto |

⚠️ **Y el dato duro que hay que llevar a la sesión:** *"no hay ahorita un roadmap de mejora de
AIDA"*. Las mejoras no están planificadas; se gatillan una por una desde el negocio.

⭐ **Implicación para la matriz de la lámina 9: los seis no se priorizan juntos.** Cuatro se pueden
empezar esta semana por un canal que ya funciona. Dos necesitan que alguien del negocio levante una
solicitud con captura de valor. **Mezclarlos en una sola matriz haría que los cuatro fáciles
esperen a los dos difíciles** — que es exactamente lo que hay que evitar.

---

## 8. A quién hay que hablarle: el interlocutor cambió

> **Radiye:** *"Eso lo podrían ver más directamente con el negocio, porque bajo la nueva estructura
> del modelo operativo… el negocio es el que tiene que gatillar las solicitudes de cualquier cambio,
> mejora nueva."*
> *"La que hizo el pedido fue Giselle… nosotros somos el equipo de Giselle."*

**El equipo de AIDA opera el sistema; no decide qué se construye.** Para los arreglos 05 y 06, la
conversación no termina en esta mesa: **necesita un patrocinador del negocio dispuesto a levantar la
solicitud y a financiar los recursos.**

**Lo que conviene salir a buscar de esta sesión, entonces, son dos cosas distintas:**
1. Del equipo de AIDA → **ejecución de los cuatro arreglos de contenido** por el canal que ya existe.
2. Del negocio → **un dueño de la solicitud** para los dos que requieren desarrollo.

---

## 9. Lo que sigue abierto

**⚠️ Sobre qué corre AIDA — y una inconsistencia que hay que resolver.** Era el pedido 02 y no está
cerrado. La presentación afirma *"confirmamos que no corre sobre Copilot sino sobre Google"*, pero
la owner describe **las dos bases de conocimiento en SharePoint** (Microsoft). Un stack mixto es
perfectamente posible, pero **la afirmación de la lámina 10 no está confirmada por esta
conversación** y conviene no sostenerla hasta ver el diagrama de arquitectura, que existe y no se
compartió.

**El denominador de adopción, que quizá ya tenemos.** Radiye reporta **más de 30.000 consultas
mensuales** y un promedio diario *"entre 3 y 3,5"*. Si eso último es **por asesor por día**, el
denominador estaría alrededor de **400 asesores activos** — y cerraría una de las preguntas abiertas
del diagnóstico. **Hay que confirmarlo antes de usarlo.**

⭐ **Lo que sí valida esa cifra: nuestra ventana de dos días es representativa en volumen.** 30.000
mensuales sobre ~22 días hábiles dan ≈1.364 consultas diarias; nosotros observamos **1.348 por
día**. Casi idénticas. Eso no valida la *composición* (siguen faltando cierre de mes y campaña),
pero sí el caudal — y era una de las limitaciones que declarábamos.

**El alcance de AIDA Sales es más ancho que Vida.** La owner precisa que sirve a *"la plaza de
ventas, ahora BI Pro, también el equipo del Hub y un piloto del canal BIF"*. **Los 274 asesores del
análisis no son 274 asesores de Vida.** Los hallazgos H2 y H3 sí están restringidos a Vida y no se
ven afectados; los de adopción (H1, H4) hay que leerlos como transversales.

**La curva por antigüedad, y sus dos lecturas.**

> **Radiye:** *"La tendencia es que los que tienen mayor uso son asesores nuevos, y los que tienen
> menos uso son asesores ya antiguos o más experimentados."*

Esto responde parcialmente una pregunta que el diagnóstico dejó abierta, y **coincide con la
literatura de copilotos — pero de dos maneras que significan cosas opuestas:**

- **Lectura A (buena):** los nuevos usan más **porque les sirve más**. Es lo que encuentra
  Brynjolfsson et al. (2025, *QJE*, 5.172 agentes): las ganancias se concentran en los menos
  experimentados.
- **Lectura B (mala):** los antiguos usan menos **porque la desestiman**. Es la *aversión a la IA*
  de los agentes top que documenta Luo et al. (2021, *Journal of Marketing*, experimentos de campo).

⚠️ **Y la diferencia importa mucho: si los asesores antiguos son los que más venden, AIDA no está
tocando a quienes mueven el número.** Distinguir entre A y B requiere cruzar uso con **desempeño
comercial**, no solo con antigüedad. La data existe.

**Y una advertencia que sale de la misma literatura:** las respuestas comerciales de AIDA son de
**483 palabras contra 188 de las de producto**. Ante el 66% de abandono, el instinto es enriquecer
la respuesta de coaching. El experimento de Luo et al. muestra lo contrario: **al restringir el
nivel de feedback, el desempeño mejoró**. Hay que dar menos, no más.

---

## 10. La historia completa, en una página

**1 · AIDA tiene un objetivo declarado, y lo confirmó su owner:** consolidar la información del
asesor y reducir su tiempo de búsqueda. Está en producción desde mayo de 2025, con más de 30.000
consultas mensuales.

**2 · Ese objetivo nunca se midió.** Lo que los dashboards reportan es adopción —consultas diarias,
actividad, ratio de feedback— y **el uso está dentro de los objetivos de valoración del asesor**.
No existe línea base de tiempo de búsqueda, así que no hay contra qué comparar.

**3 · Por eso "la uso" y "no me sirve" conviven sin contradicción.** Y por eso cualquier número de
adopción que hoy se reporte hacia arriba **no es una señal de valor**.

**4 · El diagnóstico muestra dónde falla, y no es al azar.** De ocho temas de producto en Vida,
solo dos quedan claramente peor: **precio y contratación** — los dos únicos que no dependen de la
ficha del producto sino de las reglas de operación. Son, exactamente, cotizar y emitir.

**5 · La causa está medida, y ya es consenso.** El 77% de lo que AIDA cita son folletos y fichas;
solo el 3,4% son reglas de operación. La owner llegó a la misma conclusión desde el feedback de los
asesores. **No hay que convencer a nadie del diagnóstico.**

**6 · Y hay una prueba interna de que el problema no es el modelo:** rentabilidad es el único tema
donde AIDA está claramente mejor que el promedio, y es el único que **consulta una herramienta con
datos vivos en vez de un documento**.

**7 · Para lo que los asesores más piden —objeciones y cierre— ya se fueron.** 53% usa ChatGPT o
Gemini por su cuenta, con la IA bloqueada en la computadora. Y de los 50 que le pidieron a AIDA que
les enseñara a vender, **33 no volvieron a intentarlo**.

**8 · Lo que falta hacer es lo técnicamente más fácil, y lleva quince meses sin hacerse.** Cargar
contenido es —palabras de la owner— *"lo más sencillo"*. No se hizo porque **la responsabilidad
está repartida entre ramos y no asignada a nadie con nombre**.

**9 · Cuatro de los seis arreglos se pueden empezar ya**, por un canal de centralización que ya
existe y funciona. Los otros dos necesitan que **el negocio** levante una solicitud con captura de
valor y financie los recursos — porque **no hay roadmap de mejora de AIDA**.

> ### En una frase
> **AIDA cumple bien el objetivo que nadie le midió, falla en el que nadie documentó, y lo que le
> falta es lo más barato de arreglar — solo que no tiene dueño.**

---

*Documento interno · CoE de Diseño de Experiencia, RIMAC. Las citas de la conversación con la owner
provienen de una transcripción automática y conservan su sentido, no necesariamente su literalidad
palabra por palabra.*
