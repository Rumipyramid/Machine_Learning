# Release 1 · La base de conocimiento de AIDA (Vida)

**Propuesta de alcance ejecutable.** v2.2 · 2026-08-18

> **v2.2 (2026-08-18) — la Fase 4 cambia de naturaleza.** Behavioral Design **ya construyó 2
> prototipos**, uno de práctica agéntica de objeciones sobre Copilot (con puntaje, reporte a
> jefatura y retroalimentación a AIDA). La Fase 4 deja de ser *prototipar capacidades* y pasa a ser
> **evaluar los prototipos que existen**. Incorpora el proceso aclarado de captura de casuística
> (AIDA captura las mejores respuestas durante el entrenamiento), sus **dos diferencias con el
> mecanismo validado** y el arreglo (**separar la captura de la etiqueta**), la advertencia sobre el
> **reporte individual a jefatura** (F-495) y la acotación honesta de lo que el entrenamiento puede
> prometer (F-496, F-497, F-498). Detalle completo en el node §17.

> **v2.1 (2026-08-18) — trazabilidad y horizonte.** Cuatro cambios pedidos por Alejo, aplicados
> aquí y en la versión presentable (artifact `0bb009a6`): (1) **citación (Autor, año) en línea** de
> toda afirmación que venga de fuente primaria o secundaria; (2) **§9 Insumos** — lista completa de
> lo que sostiene el documento, separando internos de externos y declarando lo que quedó fuera;
> (3) **§5.1 Las fases siguientes** — incluida la **Fase 4 de prototipado**, que responde la
> pregunta que el Release 1 no responde (*qué más debería hacer AIDA*) y le da un rol al prototipo
> Claude en vez de dejarlo compitiendo con AIDA; (4) **§5 reformulado**: cada ítem diferido ahora
> declara **por qué no ahora y adónde va**, en vez de ser una lista de descartes sin destino.

> ⭐ **v2.0 — reestructurado en tres etapas** (definición de Alejo, 2026-08-14). El Release 1 no es
> solo la intervención: **empieza midiendo y termina comprobando.**
>
> | | Etapa | Qué incluye |
> |---|---|---|
> | **1** | **Diagnóstico de la herramienta** | Encuestas y shadowing con asesores → banco de preguntas reales → evaluación asistida con LLM (usabilidad, error, exactitud) → **medición de tiempo**, que la v1.0 no tenía |
> | **2** | **Intervención en AIDA** | Los entregables R1.0 a R1.3 de abajo. Objetivo declarado: **menos errores y consulta más rápida** |
> | **3** | **Testeo** | Prueba 1 contra línea base (sin asesores, es la compuerta) → Prueba 2 con asesores: A/B por equipos, escalonado, o **serie temporal interrumpida** según lo que permita la plataforma |
>
> **Dos cosas que la reestructuración agrega:**
> - **La velocidad como segundo objetivo.** No requiere trabajo aparte —sale del mismo movimiento:
>   menos documentos compitiendo y archivos más cortos hacen que el agente encuentre antes— pero
>   **hay que cronometrarla en la Etapa 1**, o después no se puede demostrar.
> - **El nombre correcto del "full con puntos de corte": serie temporal interrumpida.** Es el diseño
>   cuasi-experimental más fuerte disponible cuando no se puede aleatorizar. Requiere **varios puntos
>   de medición antes y después**, no dos fotos. ⭐ Y su debilidad —que algo más pudo cambiar en el
>   mismo periodo— **se resuelve con algo que ya tenemos**: como el Release 1 se acota a Vida, Salud
>   y Vehicular siguen con la base vieja y funcionan como **serie de comparación natural**. Si Vida
>   mejora y los otros ramos no, el efecto es de la intervención. Es la variante *comparativa* del
>   diseño, y no cuesta montar nada.
>
> ⚠️ **Pendiente de confirmar — "el modelo SHUNK".** Alejo lo nombra como el marco de la evaluación
> con LLM (usabilidad, error). **No se pudo identificar** y no se aplica por aproximación — misma
> regla que evitó el error con "Shang"/Zheng. Candidatos encontrados y descartados por no encajar:
> **Shackel (1991)**, definición operacional canónica de usabilidad (efectividad, aprendibilidad,
> flexibilidad, actitud) — no centra el error; y **BUS-11 / BUS-15 / CUQ**, escalas de usabilidad de
> chatbots, de las cuales **CUQ sí tiene un factor específico de manejo de errores** y ya está en el
> códice como F-149. **La Etapa 1 se construye mientras tanto sobre los instrumentos ya verificados
> del proyecto**, y el marco de Shunk se incorpora en cuanto se confirme cuál es.

Integra el research *"La biblioteca de AIDA"* (Felipe, Behavioral Design,
`research/_fuentes_internas/La_biblioteca_de_AIDA_Felipe.docx`) con el diagnóstico del proyecto
(`_nodes/diagnostico-copiloto-ai-asesor-vida-rimac.md` v1.8), la evidencia de arquitectura
(`_nodes/arquitectura-conocimiento-agentes-copilot.md` v1.1) y la matriz de producto
(`_nodes/matriz-productos-vida-rimac.md` v1.2).

---

## 0. La promesa del Release 1, en una frase

**Que cuando un asesor de Vida le pregunte a AIDA algo de producto o de venta, la respuesta sea
correcta, vigente y citable — o que AIDA diga que no lo sabe.**

No es "que AIDA funcione bien". Es un alcance acotado y verificable: **un dominio (Vida), un cuerpo
canónico, y una medición del antes y el después.**

---

## 1. Por qué esto es lo primero, y no una etapa preparatoria

El research de Felipe cierra con evidencia una pregunta de presupuesto que este proyecto iba a
enfrentar igual: *si AIDA aprendió de una base desordenada, ¿alcanza con arreglar la base o hay que
reentrenarla?*

La respuesta está medida (**F-492**, EMNLP 2024): sobre conocimiento fuera del entrenamiento, el
modelo base rinde 0,481; **reentrenado 0,504 —prácticamente nada, y en otro modelo empeoró—**;
reentrenado *más* documento al responder 0,830; y **solo darle el documento al responder: 0,875, el
mejor resultado y el más barato.** Añadir reentrenamiento restó. Un segundo paper agrega que
entrenar con hechos nuevos **aumenta linealmente la tendencia a inventar**.

⭐ **Y el argumento más elegante del research de Felipe, que este proyecto no tenía:**

> AIDA **ya tiene la regla correcta** — su lógica le prohíbe responder de memoria en temas técnicos
> y la obliga a delegar al especialista. Esa es exactamente la mitigación que recomienda la
> literatura. **El problema no es la regla: es que hoy no se puede cumplir**, porque cuando el
> especialista sale a buscar encuentra contenido contradictorio, vacío o ilegible — y en ese vacío
> el modelo cae de vuelta en la memoria.
>
> **Ordenar el repositorio no es el plan B. Es lo que hace cumplible la regla que AIDA ya tiene.**

Esto además **reinterpreta la prueba C8 del protocolo**. Ahí se planteaba que si AIDA responde de
memoria pese a su regla, es falla de capa B (instrucciones). Hay una tercera lectura mejor: **la
regla está declarada y es sincera, pero es inejecutable** — una falla de capa A disfrazada de capa
B. Se distingue con la prueba del fragmento pegado.

---

## 2. Lo que el research de Felipe agrega, y lo que el diagnóstico le agrega a él

**Convergen de forma independiente** en el mecanismo (bibliotecario, no experto), en el ruteo como
punto de falla propio, en "una sola copia autoritativa por tema", y en armar el banco de control
**temprano, para tener la medición del antes**. Eso es corroboración real, no eco: son dos trabajos
hechos por separado.

### 2.1 Lo que Felipe aporta y el diagnóstico no tenía

⭐ **La cuantificación que el node de arquitectura declaraba inexistente.** Ese node decía
textualmente: *"no hay un estudio con muestra que cuantifique cuánto mejora la exactitud al
reformatear una base corporativa"*. **Ya no aplica** — ver F-490 a F-492:

| Palanca | Efecto medido | Rigor |
|---|---|---|
| Conversión estructurada vs. extracción plana | 86,2% → **94,1%**; en preguntas con tablas, **33 puntos** de brecha | 🔵 revista arbitrada, 1.706 páginas |
| Calidad de conversión | Recuperación 63,5 → **44,8** con conversor mediocre | 🟢 ICCV 2025, 8.561 documentos |
| Presentaciones vs. texto | Brecha de **26 puntos** vs. 6 — **3 a 6× peor** | 🟢 ACL/ICLR/AAAI |
| Un solo documento distractor | **−25%** de precisión; con 18, 56,4% → 23,5% | 🔵 SIGIR 2024 **+ reproducción 2026** |
| Crecer el corpus sin separar por dominio | 75% → **menos de 40%** | 🟡 preprint |

Y tres cosas más: el **techo** de las presentaciones (28% de acierto de los modelos donde un humano
llega a 89%, y el cuello de botella es *entender* la lámina, no encontrarla); la **taxonomía de
láminas por tipo** con tratamiento distinto para cada una, que es mucho más accionable que el
"los PPT son malos" del diagnóstico; y **en qué NO gastar** — troceado semántico avanzado,
solapamiento del 20%, defaults de herramienta y grafos de conocimiento.

⚠️ **Nota de reconciliación:** ese último punto **choca en parte** con el node de arquitectura, que
recoge de la documentación de Microsoft un default de 512 tokens con 25% de solapamiento (F-471) y
dos preprints a favor del troceado consciente de la estructura (F-474/F-475). Se reconcilian así:
**troceado por estructura ≠ troceado semántico avanzado** (el primero usa los encabezados que ya
existen; el segundo calcula puntos de corte y es lo que no rinde), y **un default de fabricante no
es un óptimo**. La regla operativa que sobrevive a ambos: **partir por encabezado y no invertir en
solapamiento.**

### 2.2 Lo que el diagnóstico le agrega a Felipe — y es el hueco de su plan

Su acción #2 es *"resolver las contradicciones dejando una sola copia autoritativa"*. Correcto. Pero
supone que la copia autoritativa es correcta.

⭐ **No lo es.** La lectura del Playbook del Asesor (§14 del node) contra la matriz de producto
encontró que **la fuente canónica contiene las contradicciones**:

- **duplica un producto** — Vida Contigo y VAG figuran como dos filas con descripciones distintas,
  siendo el mismo producto;
- **omite otro** — Vida Futuro Protegido no aparece;
- **usa un nombre desactualizado** — "Flexivida" es el nombre del PPT de 2022, no de la ficha
  vigente;
- y **declara Pendiente el detalle técnico de producto** — coberturas, exclusiones, carencias y
  edades no están en ninguna parte del playbook.

**Consecuencia dura para el plan: "dejar una sola copia autoritativa" propagaría el error si la
copia elegida es el playbook tal como está hoy.** Por eso el Release 1 abre con una acción que el
research no tenía.

---

## 3. Alcance del Release 1 — cinco entregables

Ordenados por dependencia. Los tres primeros no requieren decisión técnica, presupuesto ni
negociación con otras áreas: **la ventaja que Felipe identifica correctamente es que el contenido lo
controla el propio equipo.**

### R1.0 · Resolver el catálogo de Vida ⚠️ bloqueante

**Qué:** cerrar con Producto las tres discrepancias de §2.2 y publicar **una matriz de producto
única y fechada** como fuente canónica de parámetros.

**Por qué va primero:** todo lo demás deriva de aquí. Mientras el catálogo esté mal, cada documento
que se derive de él hereda el error, y la limpieza produce una base ordenada **y equivocada**.

**Insumo listo:** `matriz-productos-vida-rimac.md` ya existe con trazabilidad de fuente y nivel de
confianza por dato — hay que promoverla, no construirla.

**Esfuerzo:** días. **Depende de:** Producto.

### R1.1 · Sacar del índice lo que no debe responder

**Qué:** vacíos, plantillas, portadas, láminas de marca y versiones antiguas.

**Por qué:** es la acción de impacto alto que **no depende de nadie más**, y cada distractor
eliminado devuelve precisión de forma directa y medible (F-491: un distractor, −25%).

⚠️ **Detalle operativo de SharePoint** que el research aporta: sacar un sitio del índice es **todo o
nada** y afecta también a la búsqueda general de la empresa. Existe *descubrimiento restringido de
contenido*, que saca contenido de las respuestas del agente **sin quitarle el acceso a nadie** — esa
es la herramienta correcta. En sitios grandes puede tardar más de una semana en aplicarse:
**empezarlo temprano.**

**Esfuerzo:** bajo. **Depende de:** nadie.

### R1.2 · Cargar el cuerpo canónico de Vida, derivado y no copiado

**Qué:** el modelo de venta y el catálogo, convertidos a la forma que el agente puede consumir.

- **Partir el Playbook por bloque.** Ya medido: todos los bloques quedan bajo el techo de 36.000
  caracteres salvo el Bloque 4 (34.390, al filo y crecerá), que se parte en contacto / conversación
  / decisión.
- **Des-tabular**, empezando por la **guía de objeciones** — una entrada por objeción con encabezado
  propio, para que cada una sea un fragmento autosuficiente. Es el contenido más consultado (42% lo
  pide) en el formato que peor viaja (33 puntos de brecha en preguntas con tabla, F-490).
- **Excluir lo que no es conocimiento de venta:** Índice de Confianza Profesional, apéndice
  administrativo (133 caracteres — documento vacío), y el detalle de social selling operativo.
  **Derivar es seleccionar, no solo reformatear.**
- **Etiquetar** cada archivo con ramo, producto, vigencia, dueño y estado.

**Esfuerzo:** medio, y **menor de lo que parece**: el playbook ya es markdown, con jerarquía limpia
y sin imágenes. El trabajo es partir y des-tabular, no reescribir.

### R1.3 · Reescribir los cuadros comparativos que más se consultan

**Qué:** los veinte o treinta cuadros de planes, tarifas y coberturas que hoy viven como láminas de
diseño, convertidos a texto canónico y citable.

**Por qué acotado así:** la pregunta que ordena el trabajo **no es "qué láminas hay" sino "qué
láminas se consultan"**. Reescribir esos veinte rinde más que montar recuperación visual sobre todo
el repositorio, y cuesta una fracción.

**Esfuerzo:** medio. **Depende de:** el inventario (§4).

### R1.4 · Banco de control y medición antes/después

**Qué:** conjunto fijo de preguntas de Vida con respuesta conocida, **incluyendo preguntas que AIDA
debe rechazar**, corrido antes y después de cada cambio.

**Ya existe el instrumento:** `_outputs/protocolo-interrogacion-aida-vida.md` (v0.4), con el Bloque D
de auditoría asistida por Claude y su calibración humana obligatoria.

⚠️ **Corre ANTES de tocar nada.** Es la única forma de convertir "ordenamos el SharePoint" en "la
precisión pasó de X a Y" — y como observa Felipe, **no existe ningún estudio publicado que aísle el
retorno de ordenar una base corporativa**, así que medir el propio antes/después genera un dato que
hoy no existe públicamente.

**Esfuerzo:** bajo. **Depende de:** nadie.

---

## 4. El entregable cero: el inventario

Antes de R1.1 hace falta saber qué hay: **cuántos documentos por ramo, cuántos vacíos, cuántas
presentaciones con cuadros comparativos, y qué temas concentran las consultas reales.**

No es un estudio: es una corrida sobre el SharePoint más el histórico de preguntas a AIDA. Felipe
señala además una herramienta de Microsoft probablemente sin usar — **evaluación de gestión de
contenido**, un diagnóstico automático del estado del repositorio re-ejecutable cada 30 días.

⭐ **Y el atajo más barato para saber qué se consulta**, del §13 del node: preguntarle a los asesores
**qué le preguntan a ChatGPT que no le preguntan a AIDA.** Es el mapa del hueco sin auditar un solo
archivo.

---

## 5. Qué no entra ahora, y adónde va

> ⭐ **v2.1 — reformulado (2026-08-18).** La versión anterior era una lista de descartes sin destino:
> mezclaba "se hace después" con "es otro problema" con "lo hace otro equipo", y quien la leía no
> podía distinguirlos. **Cada ítem diferido ahora declara dos cosas: por qué no ahora, y dónde entra.**
> Nada de esto se descarta — se ordena.

| Qué | Por qué no ahora | Dónde entra |
|---|---|---|
| Describir las láminas para que el agente las lea | Recupera los diagramas sin rehacerlos, pero R1.3 cubre lo más consultado a menor costo | **Fase 3** (motor) |
| Reordenador + cita forzada con fragmento textual | Es la técnica con mejor costo-beneficio, pero **no es contenido: es cambio técnico**, y depende del equipo de plataforma | **Fase 3** (motor) |
| Partir y etiquetar el resto del repositorio | El Release 1 se acota a Vida a propósito, para tener un control natural en los otros ramos | **Fase 2** (extensión) |
| Recuperación visual de página | La opción más cara, y **rinde menos en español que en inglés** | **Fase 3**, y solo si la Fase 1 muestra que la falla es visual |
| **El ruteo entre ramos** | Es diseño del coordinador, no contenido — **capa D** del diagnóstico. Felipe también lo deja fuera de alcance | **Fase 5** (arquitectura de agentes) |
| **El agente coach de ventas** | Es el único que necesita el contexto de otro agente, y ese patrón es el más frágil de la literatura | **Fase 5** (arquitectura de agentes) |
| **El front: qué mostrarle al asesor** | No es que sea menor — es que es **rediseño de producto**, no limpieza de base. Confundirlos hunde los dos | Pieza mínima **ya en el Release 1** (ver §6); el rediseño completo, **Fase 4** |
| **Capacidades nuevas de la herramienta** | Todavía no sabemos cuáles valen la pena; construirlas antes de saberlo es el error caro | **Fase 4** (prototipado) |

---

## 5.1 Las fases siguientes

El Release 1 arregla el cuerpo de conocimiento de Vida. Lo que sigue no es una lista de deseos: cada
fase **depende de que la anterior haya dejado una medición**.

### Fase 2 · Extender a los demás ramos

Salud y Vehicular con el método ya probado en Vida. **Requisito de entrada:** que la Etapa 3 del
Release 1 haya mostrado mejora medida en Vida. Si no la mostró, extender el método es propagar algo
que no sabemos que funciona.

⚠️ **Costo de la Fase 2:** al extender, **se pierde la serie de comparación natural**. Por eso la
medición de Vida tiene que quedar cerrada antes, no en paralelo.

### Fase 3 · Mejorar el motor

Las técnicas de recuperación que el Release 1 deja fuera por ser cambio técnico: reordenador, cita
forzada con fragmento textual, descripción de láminas. **Requisito de entrada:** el diagnóstico de
la Etapa 1 tiene que haber mostrado que la falla que queda es de recuperación y no de contenido —
son fallas distintas y se arreglan distinto (capas A vs. C de la taxonomía).

### Fase 4 · Entrenamiento, casuística y los prototipos que ya existen

> ⭐ **Reformulada el 2026-08-18.** Esta fase estaba escrita como "prototipar capacidades antes de
> construirlas". **Ya no aplica en esos términos: Behavioral Design ya construyó 2 prototipos.** La
> fase deja de ser *construir prototipos* y pasa a ser **evaluar los que hay y decidir cuáles se
> promueven** — más barato y más rápido de lo que estaba planteado.

**Qué existe hoy.** Uno de los prototipos es una **funcionalidad agéntica de práctica sobre Copilot**:
el asesor practica con **casos ficticios de objeciones**, recibe consejos y **es puntuado**; más la
capacidad de guardar los puntajes, **reportarlos a la jefatura** y **retroalimentar a AIDA**.

⚠️ **P11 abierta:** el brief dice "2 prototipos" y describe uno. Se asume que el segundo es el
prototipo sobre Claude del Plan Piloto, **sin confirmar**.

**Las tres capacidades candidatas, y cómo se relacionan:**

| Capacidad | Por qué es candidata | Estado |
|---|---|---|
| **Entrenar habilidades de venta** | Interés declarado del equipo; y es **el mecanismo de captura** de la casuística | **Prototipo construido** |
| **Casuística de los mejores asesores, recuperable por situación** | El conocimiento que gana ventas vive en conversaciones, no en documentos — por eso ninguna base lo tiene | Se **produce** desde la práctica |
| **Registro asistido** | El asesor registra en Salesforce lo que ya le contó a AIDA. La duplicación más visible de los seis frentes | Sin prototipar |

⭐ **El proceso, aclarado: AIDA captura las mejores respuestas durante el entrenamiento con AIDA.**
Eso resuelve el problema real, que nunca fue *querer* la casuística sino **adquirirla** — pedirle a
alguien que la escriba falla dos veces: no lo hace, y si lo hace escribe la versión declarada. La
práctica la produce como subproducto de algo que el asesor ya tiene razón para hacer.

**Pero el mecanismo validado no funciona exactamente así, y las diferencias deciden si el efecto se
reproduce** (F-476):

| | Brynjolfsson, Li & Raymond (2025) | La propuesta |
|---|---|---|
| Qué se capturó | Conversaciones **reales con clientes** | Respuestas de **práctica** |
| Cómo se definió "la mejor" | Por el **desenlace**, sobreponderando a los agentes con mejor desempeño real | Por el **puntaje que AIDA misma asigna** |

⭐ **El arreglo, y no cuesta trabajo extra: separar la captura de la etiqueta.** La captura sigue en
la práctica; **qué entra al corpus canónico lo decide el desempeño real** (conversión, persistencia),
no el puntaje de práctica. Sin eso, AIDA puntúa, selecciona lo que ella puntuó y enseña el resultado
— un bucle que nada externo corrige. Y la señal de desenlace **ya hay que levantarla para la Etapa 3**.

⚠️ **El reporte individual a la jefatura puede invertir el signo de todo lo demás.** Kluger & DeNisi
(1996) — 607 tamaños de efecto: el feedback mejora en promedio (d = 0,41) pero **más de un tercio de
las intervenciones lo empeoró**, y el moderador es si dirige la atención a la tarea o a la persona
(F-495). Un puntaje que llega al jefe es lo segundo. Peor: si el puntaje es evaluativo, el asesor
practica para puntuar bien — **y eso contamina justamente el corpus que se quiere construir**. Las
dos funcionalidades se atacan entre sí. **Recomendación:** al asesor su puntaje completo; a la
jefatura **agregado y por tema, no por persona**.

**Qué esperar, honestamente** — tres resultados que acotan la promesa:

- La práctica simulada rinde **igual que practicar con una persona real** (27 ECAs, 1.480
  participantes, F-497). **El valor es la disponibilidad y el costo, no la superioridad pedagógica.**
- Contra ninguna instrucción el efecto es grande; contra instrucción activa cae a 0,30-0,66 (F-498).
  Si ya hay role-play con la jefatura, el delta es modesto.
- ⚠️ **En profesiones, la práctica deliberada explica menos del 1% de la varianza de desempeño** —la
  categoría más débil de las cinco medidas (F-496). **No se puede vender el entrenamiento como la
  palanca de productividad.** Lo que sí sostiene la evidencia es la **captura de casuística**.

⚠️ **Y una colisión que hay que decidir, no dejar que ocurra: Sales Coach ya entrena.** Si AIDA
entrena, hay **dos agentes que enseñan** — la misma falla que se está diagnosticando en los
documentos, un nivel más arriba. **P12.**

### Fase 5 · La arquitectura de agentes

El ruteo entre ramos y la relación entre los tres agentes desplegados (AIDA, suscripción, Sales
Coach). **Requisito de entrada bloqueante:** confirmar sobre qué framework corre AIDA realmente
(P9 — `transfer_to_agent` apunta a Google ADK, no a Copilot Studio). Sin eso, cualquier decisión de
arquitectura se toma sobre un supuesto no verificado.

### En paralelo · Que la mejora llegue a quien ya se fue

No espera a ninguna fase, porque **el asesor que abandonó AIDA no va a volver a comprobar si
mejoró** (ver §6). Es la pieza mínima de reintroducción, y corre junto con la Etapa 2.

---

## 6. El riesgo que puede anular el Release 1 entero

Felipe cierra su documento con el punto más incómodo, y hay que subirlo aquí porque **afecta la
decisión de alcance, no solo la comunicación**:

> Llegar a AIDA no es el problema — los asesores saben dónde está. **Lo que hay al llegar es una
> pantalla en blanco:** ningún botón, ningún caso de uso, ningún ejemplo, nada que le diga al asesor
> qué puede pedirle.

Y el mecanismo por el que eso puede anular todo el trabajo:

- **El asesor que ya dejó de usar AIDA no va a volver a comprobar si mejoró.** Está documentado
  desde 2015: tras ver fallar a una herramienta automatizada, la gente la abandona **incluso cuando
  pasa a ser mejor que la alternativa**, y no la reevalúa por su cuenta.
- El meta-análisis de adopción (88 estudios) da la jerarquía correcta: la **utilidad percibida**
  predice el uso más (r = 0,59) que la facilidad de uso (r = 0,43) — la calidad **sí** es la palanca
  mayor. Pero la facilidad de uso también predice la utilidad percibida (r = 0,49): **la pantalla en
  blanco no compite con la calidad, la oculta.** El asesor no puede percibir que AIDA mejoró si
  nunca llega a formular la pregunta que se lo mostraría.
- El caso más parecido documentado —ensayo del gobierno australiano con Copilot, más de 2.000
  personas con acceso garantizado— tuvo **86% que quería seguir usándolo y solo un tercio usándolo a
  diario**, con dos barreras declaradas que no eran de acceso: **no saber cómo pedir** e
  **identificar casos de uso relevantes**.

⭐ **Consecuencia para el alcance:** el Release 1 necesita **una pieza mínima de reintroducción** —
aunque sea tres ejemplos de qué preguntarle y un aviso de que cambió. No es el rediseño del front,
que es conversación aparte. Es lo mínimo para que la mejora **llegue a quien ya se fue**, que es
justamente la población que se quiere recuperar.

---

## 7. Lo que el Release 1 NO arregla — decirlo antes, no después

- **La invención residual no desaparece.** Herramientas comerciales con recuperación sobre
  documentos oficiales **y citas reales** siguen inventando entre **17% y 33%**, y el modo de falla
  dominante es **citar un documento auténtico y afirmar falsamente que dice lo que no dice**
  (F-493). Y hay un agravante: **mostrar citas sube la confianza del usuario incluso cuando las
  citas son falsas.** De ahí el criterio de diseño: no basta con el enlace — **fragmento textual y
  fecha de vigencia visibles**, y medir si la cita *sustenta* la respuesta, no si existe. El banco de
  control no es un entregable de proyecto: es permanente.
- **El ruteo entre ramos sigue igual.** AIDA es multi-ramo y una pregunta ambigua puede seguir yendo
  al especialista equivocado — y eso se ve, desde el asesor, idéntico a un dato falso.
- **No resuelve el gobierno de la actualización.** Si nada impide que mañana se suba un PPT nuevo
  sin dueño ni fecha, la base se vuelve a ensuciar. El Release 1 debe dejar **dueño y cadencia
  declarados** o tiene fecha de vencimiento.
- **No prueba que el modelo de venta funcione.** Prueba que la herramienta que lo vehicula mejoró.

---

## 8. Advertencia de fuente, para proteger la propuesta

⚠️ **La cifra ancla del research —"la precisión cae 79,5% → 24,2% con documentos contradictorios"—
tiene un problema de cita abierto** (F-489). El arXiv 2506.06485 resuelve a un paper distinto del
título citado, y su mecanismo es **conflicto contexto-memoria**, no contradicción entre documentos
del corpus, que es lo que el argumento necesita.

**El fenómeno se sostiene** — hay literatura independiente y adyacente que lo respalda, y la
dirección no está en duda. **Lo que hay que reverificar es la magnitud y su atribución antes de que
esa cifra entre a un comité**, porque es exactamente el tipo de número que se pide rastrear. Las
demás cifras del research provienen de venues arbitrados verificables (ICCV, ACL, ICLR, AAAI, SIGIR,
EMNLP, NeurIPS) y no tienen este problema.

Esto no debilita la propuesta: **el orden de prioridades no cambia**, porque se sostiene igual en
F-490, F-491 y F-492, todas verificables.

---

## 9. Insumos — qué sostiene este documento

> Añadido en v2.1 (2026-08-18) a pedido de Alejo, junto con la citación **(Autor, año)** en línea de
> toda afirmación que venga de una fuente. **Criterio:** si una afirmación no tiene fuente rastreable,
> o se marca como criterio propio del proyecto, o no entra.

### 9.1 Primarios — internos de RIMAC

| # | Insumo | Nota |
|---|---|---|
| 1 | **Playbook del Asesor** (RIMAC, versión 2026-08-14) — modelo de venta Vida, 5 bloques | Fuente canónica declarada. ⚠️ Contiene **8 pendientes** y las discrepancias de catálogo evaluadas en el diagnóstico §14 |
| 2 | **Matriz de productos Vida RIMAC**, derivada de fichas comerciales vigentes desde 2025-01-01 | Patrón oro para calificar exactitud (Bloque B del protocolo) |
| 3 | **Encuesta a 19 asesores** (CoE, 2026) | Uso de herramientas, satisfacción, temas más pedidos, uso compensatorio de IA externa |
| 4 | **Taller de Manejo de Objeciones** (36 invitados / 30 asistentes, 2026) | Drivers de valor y mejoras pedidas |
| 5 | **Auto-interrogación de AIDA** (2026-08-14) | ⚠️ **Autorreporte**: hipótesis a triangular con IT, no documentación de arquitectura |
| 6 | **Plan Piloto · Modelo de Experiencia de Venta Vida** (CoE Diseño Estratégico, julio 2026) | ⚠️ Estado histórico — el plan cambió; sus indicadores miden el **prototipo Claude**, no AIDA |
| 7 | **Mapa sistémico AS IS y diagnóstico Dx1-Dx3** (CoE Experience Design, 2026) | Origen del mapa de 6 frentes; reancla el diagnóstico a **Dx2** |
| 8 | **«La biblioteca de AIDA»** — research de Behavioral Design (Felipe, agosto 2026) | Aporta la cuantificación de formatos y la comparación reentrenar-vs-recuperar. ⚠️ Su cifra ancla (79,5%→24,2%) tiene problema de cita abierto (F-489) y **no se usa** |

### 9.2 Secundarios — evidencia externa, por rigor

| # | Fuente | ID |
|---|---|---|
| 1 | **Brynjolfsson, Li & Raymond (2025)**, «Generative AI at Work», *QJE* 140(2) — 5.179 agentes, despliegue escalonado | F-464 |
| 2 | **Franke & Park (2006)**, meta-análisis de venta adaptativa, *JMR* 43(4) — 155 muestras, >31.000 vendedores | F-477 |
| 3 | **Dietvorst, Simmons & Massey (2015)**, «Algorithm Aversion», *JEP: General* 144(1), 114-126 | F-494 |
| 4 | **Ovadia et al. (2024)** · **Gekhman et al. (2024)**, *EMNLP* — fine-tuning vs. recuperación | F-490, F-491 |
| 5 | **Zheng et al. (2023)**, MT-Bench, *NeurIPS* · **Liu et al. (2023)**, G-Eval, *EMNLP* | F-159, F-158 |
| 6 | **Magesh et al. (2025)**, *J. Empirical Legal Studies* (Stanford RegLab) · **Ding et al. (2025)**, *AAAI* | F-493 |
| 7 | **Flanagan (1954)**, «The Critical Incident Technique», *Psychological Bulletin* 51(4) | F-485 |
| 8 | **King & He (2006)**, meta-análisis de TAM, *Information & Management* 44(1) — 88 estudios. ⚠️ **Los coeficientes específicos (r=,59 / r=,43 / r=,49) provienen del research interno; verifiqué el paper y su muestra, no esos coeficientes** | F-492 |
| 9 | **Lopez Bernal, Cummins & Gasparrini (2018)**, *IJE* 47(6) · **Hemming & Taljaard (2020)**, *IJE* | F-487, F-486 |
| 10 | **OHR-Bench** (ICCV 2025) · **REAL-MM-RAG** (IBM, ACL 2025) · **ColPali** (ICLR 2025) · *Applied Sciences* (2026) · **«The Power of Noise»** (SIGIR 2024) + reproducción (SIGIR 2026) | F-469 a F-475 |
| 11 | **Microsoft Learn** (2026) — SharePoint para Copilot, índice semántico, límites de fuentes, orquestación. ⚠️ **Documentación de fabricante**; reverificar antes de decidir arquitectura | F-479, F-480 |
| 12 | **METR (2025)** — impacto de IA en desarrolladores experimentados. ⚠️ Preprint | F-488 |
| 13 | **Kluger & DeNisi (1996)**, *Psychological Bulletin* 119(2), 254-284 — 607 tamaños de efecto / 23.663 observaciones; **más de un tercio de las intervenciones de feedback empeoró el desempeño** | F-495 |
| 14 | **Macnamara, Hambrick & Oswald (2014)**, *Psychological Science* 25(8) — 88 estudios; **profesiones <1% de varianza explicada**. ⚠️ Controversia académica activa sobre la magnitud | F-496 |
| 15 | **JMIR (2024)** 26:e56195 — 27 ECAs / 1.480 participantes, metodología Cochrane · **Cook et al. (2011)**, *JAMA* 306(9) y su revisión comparativa (2012). ⚠️ Dominio salud: dirección transferible, magnitud a validar | F-497, F-498 |
| 16 | **«Judging the Judges»** (2026) · **T2-RAGBench** (2026) · **«When More Documents Hurt RAG»** (2026) · **Microsoft ISE** (2024). ⚠️ Preprints y documentación técnica: **usar la dirección, no la magnitud** | F-482, F-476 |

### 9.3 Lo que quedó deliberadamente fuera

Cuatro familias de cifras que circulan en este mercado **no entraron** por no tener fuente primaria
rastreable — y quedan registradas como trampas para que no reaparezcan en un deck:

| Cifra | Por qué no entra | ID |
|---|---|---|
| Adopción de metodologías de venta | Las cifras disponibles vienen de vendors de *sales enablement* | F-481 |
| Aceleración por configuradores de producto | 12 de 12 fuentes son del proveedor que vende el configurador | F-483 |
| Retorno de gestión de datos maestros (MDM) | El mecanismo es real, pero la cifra es de vendor y la tasa de fracaso de implementación es alta | F-484 |
| «79,5% → 24,2%» por documentos contradictorios | El arXiv citado resuelve a otro paper, con otro mecanismo | F-489 |
