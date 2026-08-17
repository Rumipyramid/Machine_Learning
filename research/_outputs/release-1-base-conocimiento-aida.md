# Release 1 · La base de conocimiento de AIDA (Vida)

**Propuesta de alcance ejecutable.** v2.0 · 2026-08-14

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

## 5. Qué va a fases siguientes

| Diferido | Por qué no en el Release 1 |
|---|---|
| Descripción multimodal de láminas | Recupera diagramas sin rehacerlos, pero R1.3 cubre lo más consultado a menor costo |
| Reordenador + cita forzada con fragmento textual | Mejor relación costo-beneficio de las técnicas, pero **es cambio técnico**: necesita al equipo de la plataforma |
| Partir y etiquetar el resto del repositorio | El Release 1 se acota a Vida; el resto se hace con el método ya probado |
| Recuperación visual de página | La opción más cara, y **rinde menos en español que en inglés** |
| **El ruteo entre ramos** | Es diseño del coordinador, no contenido. Felipe lo identifica como fuera de alcance y coincide con la **capa D** del diagnóstico |
| **El agente coach de ventas** | Es el único que necesita contexto de otro agente, y la literatura marca ese patrón como el más frágil. Revisar aparte |
| **El front: qué mostrarle al asesor** | Ver §6 — es el riesgo más subestimado de todo esto |

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
