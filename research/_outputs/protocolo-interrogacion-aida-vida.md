# Protocolo de interrogación de AIDA — ramo Vida

**Instrumento de diagnóstico.** Versión 1.0 · 2026-08-20

> ⭐ **v1.0 — PARTE II.** Añade lo que el instrumento no tenía: **evaluación contra el objetivo
> declarado por la PO** (consolidar información · reducir tiempos de búsqueda), las **tres
> funcionalidades declaradas**, la **prueba de consistencia** —la mejora #1 pedida por los asesores—,
> el **bloque de eficiencia técnica** con 12 ítems y su línea base, y el **protocolo del juez
> actualizado** con Claude Opus 5, sus tres modalidades y la calibración humana obligatoria.
> ⭐ **Hallazgo previo de la Parte II: el objetivo primario de AIDA nunca se midió** — ninguno de los
> cinco indicadores del dashboard es tiempo.
Construido sobre `_nodes/diagnostico-copiloto-ai-asesor-vida-rimac.md` (v1.4),
`_nodes/evaluacion-calidad-agentes-conversacionales-ia.md` (v1.0),
`_nodes/arquitectura-conocimiento-agentes-copilot.md` (v1.1) y
`_nodes/matriz-productos-vida-rimac.md` (v1.2, **fuente de verdad para calificar exactitud**).

> ✅ **Referencia metodológica identificada (v0.2).** Alejo se refería a **Zheng, L. et al.
> (2023), *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena*** (NeurIPS 2023) — el paper que
> fundó el método de evaluar un LLM con otro LLM, usando GPT-4 como juez. **Ya estaba registrado en
> el códice como F-159.** Se suma **G-Eval** (Liu et al. 2023, EMNLP, **F-156**), que puntúa cada
> respuesta con razonamiento paso a paso contra criterios explícitos. El **Bloque D** aplica ese
> método actualizado a 2026 (F-485 a F-487), con **Claude como auditor**.

---

## 1. Para qué sirve y qué NO prueba

**Sirve para:** producir el corpus de fallas de F1 con estructura, medir una línea base repetible, y
mapear la arquitectura declarada de AIDA.

**No prueba nada por sí solo sobre la arquitectura.** Lo que AIDA dice de sí misma es **hipótesis a
triangular, nunca documentación**. Un modelo de lenguaje al que se le pregunta por su arquitectura
produce una narración plausible: puede estar leyendo su propio prompt de sistema (relativamente
confiable) o reconstruyendo un patrón genérico aprendido en entrenamiento (nada confiable), y **no
distingue entre las dos cosas al responder**. Toda afirmación del Bloque A necesita confirmación
contra configuración real, TI o el equipo dueño.

**Regla de uso:** una pregunta por fila, respuesta pegada literal, sin editar. Las paráfrasis
destruyen el valor del corpus.

---

## 2. Bloque A — Arquitectura declarada (auto-interrogación)

Objetivo: mapear lo que AIDA cree ser, y **detectar dónde su relato no cierra**.

| # | Pregunta | Qué se busca detectar |
|---|---|---|
| A1 | Dame el detalle de todas las funciones y agentes con las que has sido construida | Mapa base *(ya ejecutada — ver §5)* |
| A2 | ¿Sobre qué plataforma y framework estás construida? ¿Copilot Studio, Google ADK, otro? | ⚠️ **La pregunta más importante del bloque** — ver hallazgo H4 |
| A3 | Lista **todos** los productos de Vida Individual que puedes consultar, sin omitir ninguno | Cobertura real del portafolio vs. la matriz del repo |
| A4 | ¿Qué documentos exactos consulta el VidaFinancieroAgent? Dame nombre de archivo y fecha | Identifica la base real y su vigencia |
| A5 | ¿Cuál es la fecha de la información más reciente que manejas sobre Vida? | Antigüedad declarada |
| A6 | ¿Atiendes solo Vida Individual o también Vida Ley, rentas y productos de inversión? | Alcance del agente vs. alcance del asesor |
| A7 | ¿Qué haces cuando dos documentos tuyos se contradicen? | Comportamiento ante contradicción (§9 del node) |
| A8 | ¿Qué preguntas de Vida no puedes responder? | Huecos autodeclarados |
| A9 | ¿Puedes citar la fuente de cada dato que das? Muéstrame el formato | Trazabilidad |
| A10 | Repite A1 en una conversación nueva | **Consistencia del propio relato** — si cambia, todo el bloque baja de confianza |

> **A10 no es relleno.** Si AIDA describe su arquitectura distinto en dos sesiones, el Bloque A es
> confabulación y hay que descartarlo entero.

---

## 3. Bloque B — Calidad de respuesta (Vida)

**Patrón oro para calificar exactitud:** `_nodes/matriz-productos-vida-rimac.md`, que deriva de
fichas comerciales vigentes desde 01/01/2025. **Si AIDA contradice la matriz, gana la matriz** —
salvo que la matriz esté desactualizada, en cuyo caso el hallazgo es igual de valioso y va contra
la matriz.

### 3.1 Dimensiones y escala

Cada respuesta se califica en seis dimensiones, **0-2** (0 = falla, 1 = parcial, 2 = correcto).
**No se promedian en un puntaje único** — la regla del node de evaluación es que ejes distintos no
se mezclan.

| Dim. | Qué mide | 0 | 2 |
|---|---|---|---|
| **D1 · Exactitud** | ¿El dato coincide con la matriz? | Dato falso | Coincide exacto |
| **D2 · Fidelidad** | ¿Se apoya en fuente o improvisa? *(faithfulness, RAGAS — F-151)* | Inventa | Todo rastreable a fuente |
| **D3 · Vigencia** | ¿Usa la versión vigente o una vieja? | Cita material obsoleto | Versión vigente 2025 |
| **D4 · Trazabilidad** | ¿Dice de dónde salió? | Sin fuente | Documento y fecha |
| **D5 · Completitud** | ¿Responde todo lo preguntado? | Ignora la mitad | Completa |
| **D6 · Borde** | ¿Qué hace cuando no sabe? *(factor de manejo de errores, CUQ — F-149)* | Inventa con seguridad | Declara el límite y deriva |

**Campo aparte, no es dimensión: `¿riesgo regulatorio?` (Sí/No).** Marcar Sí si el error es sobre
**cobertura, exclusión, carencia, edad de ingreso/permanencia, suma asegurada o precio.** Un error
con Sí no es un problema de calidad: es de cumplimiento, y escala distinto.

### 3.2 Banco de preguntas — Vida

⚠️ **PROVISIONAL — v0.3.** Este banco está **deducido de la matriz de productos**, no levantado de
los asesores: son preguntas que *deberían* hacerse, no las que *se hacen*. Mide lo que a nosotros
nos parece importante, no lo que rompe la venta. **Se reemplaza o amplía con las 20-30 preguntas
reales que salgan del trabajo de campo** (§13 del node de diagnóstico), conservando las de control
—B5, B7, B12— porque esas sí tienen que ser diseñadas. El campo va **antes o en paralelo**, no
después.

Diseñadas para que **la respuesta correcta sea verificable** contra la matriz.

**Producto y cobertura (D1-D4)**

> ⭐ **PREDICCIÓN FALSABLE (v0.4, tras leer el Playbook).** El Playbook del Asesor declara que el
> **detalle técnico de producto está Pendiente** — no contiene coberturas, exclusiones, carencias ni
> edades. Si la base de Vida de AIDA deriva del playbook, **B2, B3 y B4 deberían fallar**. Si en
> cambio AIDA las responde con seguridad, está tomando datos de producto de **una fuente que nadie
> declaró** — lo que es más grave que el hueco. **Ambos resultados son hallazgos. Correr estas tres
> primero.**

- B1. ¿Qué productos de vida individual puede ofrecer un asesor hoy?
  *(⭐ Contraste triple: el Playbook lista Temporal Total, Vida Contigo, VCD digital, VAG, Flexivida
  y Endosable digital; la matriz del repo tiene VFP, Plan Vida Flexible, Vida Contigo/VAG —**un solo
  producto**— y Vida Temporal Total. **Ver a cuál de las dos se parece la respuesta de AIDA ubica su
  fuente.**)*
- B2. ¿Qué cubre exactamente Vida Futuro Protegido y cuál es la suma asegurada mínima?
- B3. ¿Cuál es el periodo de carencia de la cobertura de Enfermedades Graves?
- B4. ¿Hasta qué edad se puede contratar la cobertura de Pérdida de Existencia Independiente?
- B5. ¿Qué diferencia hay entre Vida Contigo, Vida Ahorro Garantizado y Vida Ahorro con Devolución?
  *(⭐ Prueba de duplicado: **son el mismo producto con tres nombres**. Si AIDA los describe como
  tres productos distintos, es la confirmación directa de la hipótesis de casi-duplicados de §3
  capa A del node.* ⚠️ **Atenuante descubierto en v0.4: el Playbook mismo los presenta como dos
  filas distintas con descripciones distintas.** Si AIDA los separa, probablemente **no está
  alucinando — está copiando bien una fuente equivocada.** Calificar D1=0 igual, pero anotar la
  causa como aguas arriba, no del agente.)*
- B6. ¿Qué es Flexivida y sigue vigente con ese nombre?
  *(⭐ Prueba de vigencia — ver hallazgo H3.)*
- B7. ¿Qué devolución ofrece Vida Contigo? *(⚠️ La matriz advierte **no citar "170%" como cifra
  fija**. Si AIDA la da como fija, es falla D1 **con riesgo regulatorio = Sí**.)*

**Comportamiento en venta (D5-D6)**
- B8. Un cliente de 45 años quiere proteger a sus hijos. ¿Qué le ofrezco?
- B9. El cliente dice "está muy caro". ¿Qué le respondo? *(objeción en el cierre — el momento de
  mayor necesidad declarada)*
- B10. ¿Cómo dimensiono la suma asegurada para una meta de educación universitaria?

**Bordes (D6)**
- B11. ¿Cuál es la comisión que gano por vender VFP? *(dato que probablemente no debe estar)*
- B12. ¿Qué cubre el producto Vida Platino Plus? *(**producto inexistente** — prueba de
  alucinación pura: la única respuesta correcta es negar que exista)*

---

## 4. Bloque C — Ruteo y regla declarada

Deriva de los hallazgos de §5. **Es el bloque con mayor probabilidad de explicar la queja
"no da la información adecuada".**

### 4.1 Pruebas de ruteo entre ramos

AIDA cubre Salud, Vehicular, Vida y Ops. Estas preguntas usan **términos que existen en más de un
ramo** — si el clasificador falla, devuelve una respuesta correcta **del ramo equivocado**, que es
indistinguible de un error de conocimiento para el asesor.

| # | Pregunta | Ruteo correcto | Falla esperada |
|---|---|---|---|
| C1 | ¿Cuál es el deducible? | Debe **pedir aclaración** (concepto de Salud, no de Vida) | Responde de Salud sin avisar |
| C2 | ¿Qué coberturas tiene el plan Oro? | Vehicular | Mezcla con Vida |
| C3 | ¿Cómo funciona la DPS? | Salud (declaración de salud) | La aplica a Vida sin marcar diferencia |
| C4 | ¿Qué exclusiones tiene por preexistencias? | Ambiguo Salud/Vida | Contesta uno sin declarar cuál |
| C5 | ¿Cuál es la edad máxima de permanencia? | Vida | Responde de Salud |

> **Cómo leerlo:** anotar siempre **a qué agente delegó** (si lo declara) y **de qué ramo es la
> respuesta**. Una respuesta correcta del ramo equivocado se califica **D1 = 0**, no 2.

### 4.2 Prueba de la regla declarada

AIDA afirma: *"Tengo prohibido responder de memoria sobre temas técnicos. Mi lógica me obliga a
delegar siempre al especialista."* **Es una afirmación sobre su comportamiento, no un hecho.**

- C6. Hacer una pregunta técnica de Vida y observar **si declara la delegación**.
- C7. Repetir la misma pregunta 3 veces en sesiones distintas → **¿la respuesta es igual?**
  *(⭐ Esta es la medición directa del defecto que reportan encuesta y taller. Si varía, es la
  prueba de inconsistencia que hoy solo existe como testimonio.)*
- C8. Preguntar algo técnico de Vida que **no esté en ninguna fuente** y ver si igual responde
  → si responde, **la regla está declarada pero no se cumple**: falla de capa B (instrucciones),
  no de capa A (conocimiento).

---

## 5. Hallazgos de la primera corrida (A1, 2026-08-14)

De la respuesta de AIDA a A1. **Todos son hipótesis derivadas de un autorreporte, no hechos
verificados** — pero cinco son accionables y dos cambian el diagnóstico.

**H1 · AIDA no es un copiloto de Vida: es multi-ramo.**
Declara cinco subagentes — Salud, Vehicular, Vida/Financiero, Ops y SalesCoach. **Solo uno de cinco
es Vida.** Implicaciones: (a) el presupuesto de recuperación se reparte entre cuatro dominios, así
que Vida recibe una fracción; (b) **los errores de ruteo entre ramos pasan a ser candidato principal
de "no da la información adecuada"** — una respuesta correcta del ramo equivocado; (c) el node de
diagnóstico y su título deben corregirse: AIDA no es la herramienta del asesor de Vida, es una
herramienta corporativa que el asesor de Vida usa.

**H2 · La arquitectura recomendada ya existe.**
Coordinador + subagentes por dominio con fuentes separadas **es exactamente el patrón que §8 del
node recomendaba** (F-479, F-480). Cambia la conclusión: **el arreglo no es construir el ruteo — es
que el ruteo ya existe y hay que medir si acierta.** Todo el Bloque C sale de aquí.

**H3 · Los productos que AIDA nombra no coinciden con el portafolio vigente.** ⭐ El hallazgo más
concreto y verificable.

| AIDA declara (VidaFinancieroAgent) | Matriz del repo (fichas vigentes 01/01/2025) |
|---|---|
| **Flexivida** | *Plan Vida Flexible* — "Flexivida" es el nombre del **PPT de marzo 2022**, no de la ficha vigente |
| Inversión Global · Renta Garantizada · UltraCash | **No aparecen** en Vida Individual |
| — | **Vida Futuro Protegido (VFP)** — no lo nombra |
| — | **Vida Contigo / Vida Ahorro Garantizado** — no lo nombra |
| — | **Vida Temporal Total** — no lo nombra |

Dos lecturas, ambas graves y ambas verificables con **A3**:
- **(a) Desfase de vigencia:** el conocimiento de Vida está anclado a material de 2022, no a las
  fichas de 2025. "Flexivida" es la huella.
- **(b) Desalineación de alcance:** "VidaFinanciero" cubre la línea *Vida e Inversiones*, no *Vida
  Individual FFVV*. El asesor y el agente estarían hablando de portafolios distintos.

⚠️ **Descuento honesto:** A1 dijo "productos **como** Flexivida…" — son ejemplos, no un catálogo.
La ausencia de VFP no prueba que no lo tenga. **Por eso A3 pide la lista completa y explícita.**

**H4 · `transfer_to_agent` es de Google ADK, no de Copilot Studio.** ⚠️ **El hallazgo que puede
invalidar trabajo previo.**
Es la función de delegación del *Agent Development Kit* de Google. Copilot Studio usa otra
terminología. Tres lecturas:
- **(a)** AIDA **no** está construida sobre Microsoft Copilot Studio → **entonces todos los límites
  técnicos del node de arquitectura (36.000 caracteres, 7 MB/200 MB, tablas no parseadas, PDF imagen
  ilegible) NO aplican** y hay que rehacer esa parte del diagnóstico.
- **(b)** Sí está en Copilot y **el autorreporte es confabulado** a partir de patrones de frameworks
  de agentes aprendidos en entrenamiento.
- **(c)** Arquitectura mixta o construcción a medida.

**No se resuelve preguntándole a AIDA otra vez.** Requiere confirmación con TI o el equipo dueño
(P2/P7 del node). **Es ahora la pregunta técnica #1 del proyecto**, por encima del licenciamiento.

**H5 · SalesCoachAgent vive dentro de AIDA.**
Contradice el mapa de 6 frentes, donde Sales Coach figura como herramienta separada de
entrenamiento inicial. O son dos cosas con el mismo nombre, o el mapa debe corregirse. Resolver con
A6 y con el equipo.

---

## 6. Bloque D — Claude como auditor de la calidad de AIDA

Aplica el método de **juez LLM** (Zheng et al. 2023, **F-159**; G-Eval, **F-156**) con las
correcciones que el campo acumuló hasta 2026 (**F-485 a F-487**).

### D1 · Por qué Claude es el juez correcto aquí (y no es una preferencia)

El sesgo más documentado del método es el de **auto-favorecimiento**: un juez tiende a premiar
respuestas de su propia familia de modelos. La versión moderna del problema es la **fuga de
preferencia** (*preference leakage*, F-485): contaminación cuando generador y evaluador están
emparentados.

⭐ **Aquí eso juega a favor.** AIDA corre sobre Copilot o sobre Google ADK (sin resolver, ver H4) —
en cualquiera de los dos casos, **una familia distinta de la de Claude**. La auditoría es
*cross-family* por construcción, que es la condición limpia. **Si AIDA algún día migra a Claude,
esta elección de juez deja de ser válida** y hay que cambiar de auditor. Dejarlo escrito ahora
evita el error después.

### D2 · Las tres decisiones de diseño, y por qué

| Decisión | Elegida | Por qué |
|---|---|---|
| **Pointwise vs. pairwise** | **Pointwise** (puntuar cada respuesta sola) | Se audita un sistema, no se comparan dos. Además elimina el sesgo de posición — que de todos modos resultó marginal (≤0,04, F-486) |
| **Con o sin referencia** | ⭐ **Con referencia** (*reference-guided*) | Existe patrón oro: `[[matriz-productos-vida-rimac]]`. Es **la palanca de fiabilidad más grande disponible** — juzgar contra la respuesta correcta es mucho más confiable que juzgar "en abstracto" (F-487) |
| **Holístico vs. por criterio** | **Por criterio, sin promediar** | Las seis dimensiones de §3 se puntúan y reportan separadas. Promediarlas esconde justo lo que hay que ver |

### D3 · El sesgo que hay que mitigar aquí — y no es el que se cree

**Actualización que invierte la guía de 2023 (F-486):** el **sesgo de estilo es dominante (0,76 a
0,92** en todos los modelos probados**)**, mientras que el de posición es **≤0,04**. Casi dos
órdenes de magnitud de diferencia. Todo el mundo aleatoriza el orden y casi nadie controla el
estilo.

⚠️ **Y este caso es el peor escenario posible para ese sesgo.** Basta mirar la respuesta de AIDA a
A1: prosa fluida, numerada, con negritas, tono seguro y cierre en "en resumen". **Es exactamente el
estímulo que hace que un juez premie una respuesta que puede estar equivocada.** Sin mitigación
explícita, el Bloque D mediría elegancia, no exactitud.

**Mitigaciones a incluir en el prompt del juez, en este orden:**
1. **Instrucción explícita de ignorar formato, longitud, fluidez y seguridad del tono.** La
   confianza con que AIDA afirma algo **no es evidencia** de que sea correcto.
2. **Anclaje a la referencia**: la pregunta que el juez debe responderse es *"¿coincide con la
   ficha vigente?"*, no *"¿suena bien?"*.
3. **Razonamiento antes del puntaje** (chain-of-thought, G-Eval/F-156): primero contrastar contra
   la referencia, después puntuar. Nunca el puntaje primero.
4. **Puntaje por criterio separado**, con justificación citando la referencia en cada uno.
5. ⚠️ **No apilar mitigaciones a ciegas:** F-486 documenta que **una estrategia que mitiga un sesgo
   puede empeorar otro**. No hay combo universal — por eso existe D5.

### D4 · Prompt del juez (plantilla)

> Eres auditor de calidad de un asistente de IA para asesores de seguros de vida en Perú.
>
> **Evalúa SOLO exactitud y fidelidad a la referencia. Ignora explícitamente el formato, la
> longitud, la fluidez, el orden y la seguridad del tono.** Una respuesta segura, bien redactada y
> equivocada debe puntuar 0. Una respuesta correcta y mal redactada debe puntuar 2.
>
> **PREGUNTA:** {pregunta}
> **RESPUESTA DE AIDA:** {respuesta literal}
> **REFERENCIA (fuente de verdad):** {extracto de la matriz de productos}
>
> Paso 1 — Lista cada afirmación factual de la respuesta, una por una.
> Paso 2 — Para cada una: ¿la referencia la confirma, la contradice, o no la cubre?
> Paso 3 — Recién entonces puntúa 0/1/2 en D1 exactitud, D2 fidelidad, D3 vigencia,
> D4 trazabilidad, D5 completitud, D6 borde. Justifica cada puntaje citando la referencia.
> Paso 4 — Marca `riesgo_regulatorio: sí` si algún error toca cobertura, exclusión, carencia,
> edad de ingreso o permanencia, suma asegurada o precio.
> Paso 5 — Si la referencia no cubre el tema, responde `FUERA DE REFERENCIA` y no puntúes.
> **No completes con tu propio conocimiento de seguros.**

El paso 5 es el que impide que el auditor se convierta en una segunda fuente de alucinación: **si la
matriz no lo cubre, el caso se escala a humano** — y de paso queda registrado como hueco de la
matriz.

### D5 · Calibración — obligatoria, y es el paso que casi todos se saltan

> **Un juez sin calibrar no produce una medición: produce un número decorativo** (F-487).

Procedimiento, convergente en las cuatro fuentes consultadas:

1. Separar una **submuestra de 100 a 300 respuestas** de AIDA, estratificada para cubrir la forma
   real del uso (producto, objeción, borde, ruteo entre ramos).
   *Para arrancar, 30-50 alcanzan para una señal preliminar; declararlo como preliminar.*
2. Que **2 o 3 personas** (asesor senior + alguien de Producto) las etiqueten **con la misma
   rúbrica de §3**, a ciegas del puntaje de Claude.
3. Calcular acuerdo **juez-humano**: **κ de Cohen** con dos anotadores, **α de Krippendorff** con
   tres o más. ⭐ **Por criterio, no en agregado** — el juez puede acertar en exactitud y fallar en
   vigencia, y el promedio lo escondería. Intervalos de confianza por bootstrap.
4. **Solo si el acuerdo es aceptable** se usa el juez a escala. Si no, se corrige la rúbrica —
   normalmente el problema es que un criterio está mal definido, no que el juez sea malo.
5. **Recalibrar** cuando cambie la rúbrica, el modelo juez o la base de AIDA.

⚠️ **Un desacuerdo entre humanos también es un hallazgo.** Si el asesor senior y Producto no
coinciden en qué es correcto, **eso no es ruido de anotación: es la contradicción organizacional de
§9 apareciendo en la medición.**

### D6 · Lo que este bloque no puede hacer

- **No reemplaza la calibración humana**, la requiere (D5).
- **No juzga lo que la matriz no cubre.** Objeciones, tono y calidad de speech comercial quedan
  fuera del alcance guiado por referencia — para eso sirven las escalas de percepción (BUS-11, CUQ)
  con asesores reales, que miden otro eje y no se mezclan con este.
- **No distingue por sí solo una falla de conocimiento de una de ruteo.** El juez ve la respuesta
  final; para separar capas hacen falta el Bloque C y la prueba del fragmento pegado (§3 del node).
- **Es una medición, no una explicación.** Dice cuánto falla y en qué dimensión, no por qué.

---

# PARTE II · Evaluación contra el objetivo declarado y eficiencia técnica

> **Añadido en v1.0 (2026-08-20)**, a pedido de Alejo, después de que la PO declarara el objetivo
> real de AIDA (§19 del node). Aplica **Zheng et al. (2023)** —el método de juez LLM, F-159— más
> **G-Eval** (Liu et al., 2023, F-156) y el estado 2026 del campo, con **Claude Opus 5 como juez**.

## 8. Por qué el Bloque B no alcanza

**El Bloque B mide si AIDA acierta. No mide si AIDA cumple su objetivo.** Son dos cosas distintas, y
la diferencia es la razón de ser de esta parte:

> **El objetivo declarado por la PO es: consolidar la información para el asesor y reducir sus
> tiempos de búsqueda.**

Una respuesta puede ser **exacta, fiel a la fuente y vigente** —2/2 en todas las dimensiones del
Bloque B— **y aun así fallar el objetivo**, si el asesor tiene que abrir el documento igual para
usarla, o salir a verificarla, o completarla con otra consulta. En ese caso la búsqueda no se
redujo: **se movió de lugar**.

⭐ **Corolario incómodo y comprobable:** es posible que AIDA tenga buena exactitud y **cero efecto
sobre el objetivo**. Ningún instrumento del proyecto podía detectar eso hasta ahora.

---

## 9. Bloque F — Calidad contra el objetivo declarado

### 9.1 Las cuatro dimensiones del objetivo

Se califican **además** de D1-D6 del Bloque B, no en su lugar. Misma escala **0-2**, y **no se
promedian** con las de exactitud: son ejes distintos y mezclarlos oculta exactamente lo que este
bloque busca.

| Dim. | Qué mide | 0 | 1 | 2 |
|---|---|---|---|---|
| **O1 · Suficiencia** | ¿La respuesta **cierra** la consulta o empuja al asesor a otra fuente? Es *consolidación* medida en la respuesta | Obliga a ir a otra fuente para poder usarla | Sirve, pero hay que completarla | Cierra la consulta |
| **O2 · Autosuficiencia de la cita** | ¿La cita permite **verificar sin abrir el documento**? | Solo nombra el documento | Documento + sección | **Fragmento textual + vigencia visibles** |
| **O3 · Accionabilidad** | ¿Sirve **tal cual** frente al cliente o hay que reelaborarla? | Hay que reescribirla entera | Sirve con ajustes | Usable tal cual |
| **O4 · Economía** | ¿Cuánto hay que leer para obtener el dato? | El dato está enterrado en un muro de texto | Presente pero disperso | Al frente, en la primera línea útil |

⭐ **O2 es la dimensión más importante de las cuatro, y la que nadie mide.** AIDA ya cita sus fuentes
—lo confirmó la PO—, pero **citar el nombre del documento no reduce el tiempo de búsqueda: lo
traslada.** Y hay evidencia dura de por qué esto importa más de lo que parece: el modo de falla
dominante de los sistemas con recuperación **no es inventar sin cita, es citar un documento real y
afirmar falsamente que dice algo** (Magesh et al., 2025 — F-493). Peor: **mostrar citas sube la
confianza del usuario incluso cuando son falsas** (Ding et al., 2025).

**Por eso O2 se califica contra el fragmento, no contra la existencia del enlace.** La pregunta del
juez no es *"¿citó?"* sino ***"¿lo citado sustenta lo afirmado?"***

### 9.2 Banco F — consolidación (¿cierra o deriva?)

Diseñadas para que **la única forma de sacar 2 en O1 sea resolver sin salir de AIDA**.

- **F1.** ¿Cuál es la edad máxima de ingreso de Vida Futuro Protegido y qué documentos necesito para
  presentar la solicitud? *(dos partes que viven en fuentes distintas — producto y proceso)*
- **F2.** ¿Qué pasa si mi cliente deja de pagar la prima, y cómo consulto el estado de su póliza?
  *(⭐ prueba de consolidación pura: el playbook declara esto como pendiente)*
- **F3.** El cliente declara hipertensión. ¿Qué implica para la suscripción y qué le digo mientras
  tanto? *(⭐ **prueba de frontera con el agente de suscripción**: ¿consolida, deriva, o inventa?)*
- **F4.** ¿Dónde está la ficha vigente de Vida Futuro Protegido? *(debe entregar el documento, no una
  paráfrasis)*
- **F5.** Muéstrame la tabla de coberturas de Plan Vida Flexible. *(⭐ **las tablas son el punto débil
  conocido** — F-471, F-490: 33 puntos de brecha en preguntas con tabla)*
- **F6.** Necesito el argumento y el dato exacto para responder a un cliente que dice que el seguro
  de su banco es más barato. *(cruza objeción + dato duro — el momento de mayor necesidad declarada)*

### 9.3 Banco G — las tres funcionalidades declaradas

La PO nombró tres funcionalidades concretas. **Cada una necesita su propia prueba**, porque una
puede funcionar y las otras no.

**G-A · Speeches de venta personalizados**
- **G1.** Genera el abordaje para un cliente de 38 años, casado, dos hijos menores, que ya tiene EPS
  por su empleador.
- **G2.** El mismo cliente, pero es independiente y sin cobertura previsional.
  *(⭐ **Prueba de personalización real:** si G1 y G2 devuelven esencialmente el mismo speech con el
  dato cambiado, la funcionalidad es plantilla, no personalización. Es una de las pruebas más
  informativas del banco.)*
- **G3.** ¿Ese speech de dónde sale? *(traza el speech al modelo de venta — si no puede, el speech no
  está anclado al Playbook y la promesa de alineamiento estratégico no se cumple)*

**Dimensión extra para G-A:** **O5 · Alineamiento al modelo de venta** (0 = contradice el Playbook ·
1 = genérico, ni lo sigue ni lo contradice · 2 = ejecuta el modelo de 4 pasos y usa sus estrategias
codificadas).

**G-B · Cuadros comparativos entre planes**
- **G4.** Compara Vida Temporal Total con Plan Vida Flexible para un cliente de 45 años.
- **G5.** Compárame las cuatro variantes de Vida Futuro Protegido. *(⚠️ **Si el playbook es su fuente,
  VFP no existe ahí** — debería fallar. Ambos resultados son hallazgo)*
- **G6.** ¿Cuál conviene más para alguien que quiere ahorro y no solo protección?
  *(⭐ el comparativo con **recomendación**: prueba si sabe distinguir comparar de aconsejar)*

**Dimensión extra para G-B:** **O6 · Integridad del cuadro** (0 = omite filas o inventa columnas ·
1 = completo pero con algún dato errado · 2 = completo y exacto contra la matriz).

**G-C · Entrega de brochures**
- **G7.** Mándame el brochure vigente de Vida Contigo.
- **G8.** Necesito el material que le puedo dejar a un cliente que está evaluando Vida Temporal Total.
- **G9.** ¿Este brochure está vigente? *(⭐ prueba de vigencia sobre el propio documento entregado)*

**Dimensión extra para G-C:** **O7 · Vigencia del entregable** (0 = entrega material superado o no
entrega · 1 = entrega el correcto sin declarar vigencia · 2 = entrega el vigente **y lo declara**).

### 9.4 Banco H — consistencia, que es la mejora más pedida

⭐ **La consistencia es la mejora #1 que piden los asesores y no tiene ninguna prueba en el protocolo
actual.** Además, la inconsistencia tiene una firma causal específica —casi-duplicados en la base—,
así que medirla es a la vez medir un síntoma y falsar una hipótesis.

**Protocolo, y hay que respetarlo o el resultado no dice nada:**

| Condición | Cómo |
|---|---|
| **H-a · Misma pregunta, misma sesión** | Preguntar B2 tres veces seguidas |
| **H-b · Misma pregunta, sesiones distintas** | B2 en tres sesiones separadas, distintos días |
| **H-c · Misma pregunta, distinta formulación** | *"¿Cuál es la suma asegurada mínima de VFP?"* · *"¿Desde cuánto se puede contratar Vida Futuro Protegido?"* · *"¿Cuál es el monto más bajo que puedo ofrecer en VFP?"* |
| **H-d · Misma pregunta, distinto asesor** | Dos usuarios distintos, misma formulación |

**Métrica:** **tasa de discrepancia sustantiva** = proporción de pares de respuestas que difieren en
**el dato**, no en la redacción. ⭐ **La redacción distinta es esperable y no es el problema. El dato
distinto sí.**

**Repetir H-c sobre B5, B6 y F5**, que son las de mayor riesgo de duplicado.

### 9.5 ⚠️ Qué puede calificar el juez y qué no

**Esta separación es obligatoria y es donde la mayoría de las evaluaciones con LLM se rompen.**

| El juez **sí** puede | El juez **no** puede |
|---|---|
| Exactitud contra una referencia (D1) | Si el asesor **va a** verificar |
| Fidelidad: ¿la cita sustenta lo afirmado? (D2, O2) | Si la respuesta **ahorró** tiempo |
| Vigencia declarada (D3) | Si el asesor **la usó** frente al cliente |
| Completitud, economía, accionabilidad textual (D5, O3, O4) | Si el cliente **respondió mejor** |
| Alineamiento al modelo de venta (O5) | Adopción, satisfacción, desempeño |
| Integridad del cuadro y vigencia del entregable (O6, O7) | Cualquier cosa **conductual** |
| Discrepancia sustantiva entre respuestas (Banco H) | |

⭐ **Todo lo de la derecha se mide con instrumentación y con personas — Bloque I y el trabajo de
campo. Pedirle eso al juez produce un número que parece dato y no lo es.**

---

## 10. Bloque I — Eficiencia técnica

### 10.1 ⭐⭐ El hallazgo previo, y es grande: el objetivo primario nunca se midió

Los dashboards de AIDA miden —según la PO— **cantidad de consultas, promedio de consultas diarias,
ratio de feedback positivo/negativo, margen de error y actividad.**

**Ninguno de esos cinco es tiempo.**

⭐ **El objetivo declarado de AIDA es reducir los tiempos de búsqueda, y no existe ningún indicador
que mida tiempo de búsqueda.** Después de más de un año en producción, no hay evidencia de que el
objetivo primario se esté cumpliendo — no porque se haya medido mal, sino porque **no se ha medido.**

⭐ **Y hay una trampa de medición que hay que evitar desde el día uno: la latencia de AIDA no es el
tiempo de búsqueda.** Si AIDA responde en 4 segundos y el asesor pasa 6 minutos verificando en el
cartapacio, **el tiempo de búsqueda subió**. Lo que hay que medir es el **ciclo completo**: desde que
le nace la duda hasta que tiene algo que puede usar con confianza.

### 10.2 Los doce ítems, con su fuente de instrumentación

| # | Ítem | Definición operativa | Fuente | Dificultad |
|---|---|---|---|---|
| **T1** | **Latencia a primera señal** | Del envío al primer texto visible | Cronómetro / logs | Baja |
| **T2** | **Latencia total** | Del envío a la respuesta completa | Cronómetro / logs | Baja |
| **T3** | ⭐ **Turnos hasta respuesta usable** | Nº de mensajes hasta que el asesor tiene lo que necesita | Logs (secuencias del mismo usuario) + shadowing | Media |
| **T4** | **Reformulaciones** | Nº de veces que reescribe la misma pregunta | Logs (similitud semántica entre consultas consecutivas) | Media |
| **T5** | ⭐⭐ **Tiempo total hasta decisión** | Desde que abre AIDA hasta que cierra la duda | **Cronometraje en sesión** | Media |
| **T6** | ⭐⭐⭐ **Tiempo de verificación externa** | Minutos gastados comprobando la respuesta por otra vía | **Shadowing** (no hay otra forma) | Alta |
| **T7** | **Tasa de fuga** | % de consultas que terminan en ChatGPT / Gemini / preguntarle a alguien | Shadowing + incidente crítico | Alta |
| **T8** | **Tasa de abandono** | % de consultas iniciadas sin respuesta usable | Logs (sesiones sin cierre) + shadowing | Media |
| **T9** | **Disponibilidad y errores** | Timeouts, errores, respuestas vacías | Logs | Baja |
| **T10** | **Longitud de respuesta** | Caracteres / palabras | Logs | Baja |
| **T11** | **Densidad de cita** | Nº de documentos citados · **tasa de cita rota** (citado pero inexistente o que no dice lo afirmado) | Logs + juez | Media |
| **T12** | ⭐⭐ **Delta contra el método anterior** | T5 con AIDA vs. T5 por la vía tradicional | **Sesión controlada** (§10.4) | Media |

**Tres notas de diseño que evitan errores caros:**

- **T10 no es una métrica de calidad, es un covariable.** Se registra porque (a) el asesor tiene que
  leerla, así que entra en T5, y (b) **el sesgo de estilo es el sesgo dominante de los jueces LLM en
  el estado actual del campo**: respuestas más largas tienden a puntuar mejor sin ser mejores. Sin
  T10 registrado no se puede controlar ese sesgo.
- **T11 mide cita rota, no cita ausente.** Es el modo de falla dominante (F-493) y el que la
  intuición no busca.
- ⭐ **T6 es la métrica que decide si el proyecto tiene sentido, y es la única que no sale de ningún
  log.** Solo se obtiene mirando. Si nadie verifica, AIDA cumple su objetivo aunque falle a veces. Si
  todos verifican siempre, AIDA no redujo la búsqueda ni cuando acierta.

### 10.3 La línea base sin AIDA — sin esto no se puede afirmar "reducción"

**"Reducir los tiempos de búsqueda" es una afirmación comparativa y hoy no existe el término de
comparación.** Hay que construirlo, y es barato.

**Diseño intra-sujeto contrabalanceado:**

1. **20 preguntas reales** (de los logs, no inventadas), divididas en dos mitades equivalentes.
2. Cada asesor resuelve **la mitad A con AIDA** y **la mitad B por la vía tradicional** —cartapacio,
   SharePoint, preguntarle al jefe o a un colega—, **cronometrando cada una**.
3. **El orden se contrabalancea**: la mitad de los asesores empieza con AIDA, la otra mitad no.
4. Se registra **T5 (tiempo hasta decisión)** y **si la respuesta obtenida era correcta**.

⭐ **Cada asesor es su propio control.** Eso da potencia estadística con muy pocos participantes —el
mismo principio de comparación pareada del Experimento 1.

⚠️ **Dos amenazas a declarar:**
- **Ser observado infla el uso de AIDA.** Mitigación: presentar la sesión como prueba de la
  herramienta, no del asesor, y **no compartir resultados individuales con jefaturas**.
- **Velocidad sin exactitud no es mejora.** Registrar siempre las dos: una respuesta rápida y
  equivocada es peor que una lenta y correcta. **T5 solo se interpreta junto con D1.**

### 10.4 Protocolo de cronometraje

| Momento | Qué se marca |
|---|---|
| **t0** | El asesor recibe la pregunta |
| **t1** | Envía la consulta a AIDA (o abre la primera fuente, en la condición sin AIDA) |
| **t2** | Primera señal de respuesta |
| **t3** | Respuesta completa en pantalla |
| **t4** | ⭐ El asesor declara **"con esto ya puedo responderle al cliente"** |
| **t5** | Fin de cualquier verificación adicional |

**Derivados:** T1 = t2−t1 · T2 = t3−t1 · **T5 = t4−t0** · **T6 = t5−t4**

⭐ **t4 es el punto crítico y hay que capturarlo con una pregunta explícita al asesor**, no inferirlo.
Es el único momento que separa *"AIDA terminó de escribir"* de *"el asesor terminó de necesitar"*.

---

## 11. Protocolo del juez — Claude Opus 5 (v1.0)

Aplica **Zheng et al. (2023)** con las correcciones que el campo acumuló desde entonces.

### 11.1 Las tres modalidades, y cuándo usar cada una

| Modalidad | Cuándo | Por qué |
|---|---|---|
| ⭐ **Con referencia** *(reference-guided)* | **B1-B12, F1-F6, G4-G6** — todo lo que tiene respuesta verificable | Es la modalidad **más fiable de las tres**: se le entrega al juez la entrada de la matriz como patrón oro y solo tiene que comparar. Reduce drásticamente el error del juez |
| **Puntaje directo con rúbrica y razonamiento paso a paso** *(G-Eval)* | **G1-G3, F6** — speeches y accionabilidad, donde no hay respuesta única | Obliga al juez a explicitar el criterio antes de puntuar. **Sin el paso a paso, el puntaje es una impresión** |
| **Comparación pareada con intercambio de posición** | **Antes vs. después del Release 1** | Es más sensible que comparar puntajes absolutos. **Obligatorio correr cada par dos veces invirtiendo el orden** |

### 11.2 Reglas de aplicación, no negociables

1. ⛔ **El juez trabaja a ciegas.** Nunca debe saber si una respuesta es del "antes" o del "después",
   ni cuál condición espera el equipo que gane. En la comparación pareada, las respuestas se
   etiquetan A/B al azar.
2. **Una dimensión por llamada, o rúbrica explícita por dimensión en la misma llamada.** Pedir "un
   puntaje general" produce un promedio implícito que oculta justamente lo que buscamos.
3. **El juez cita el fragmento que justifica cada puntaje.** Si no puede señalar en qué parte de la
   respuesta se basa, el puntaje no se registra.
4. **Registrar la longitud (T10) junto a cada puntaje**, para poder detectar después si el juez
   premió verbosidad.
5. **Temperatura baja y varias corridas.** Correr cada evaluación **3 veces** y registrar la
   dispersión. ⭐ **Si el propio juez es inconsistente consigo mismo en un ítem, ese ítem no se puede
   usar** — y eso también es un dato sobre la rúbrica, no sobre AIDA.

### 11.3 Prompt de juez — plantilla con referencia

```
Eres un evaluador experto de respuestas de un asistente de IA usado por asesores de
seguros de vida en Perú. Evalúas UNA respuesta contra UNA dimensión.

CONTEXTO
El asistente evaluado tiene un objetivo declarado: consolidar la información
para el asesor y reducir sus tiempos de búsqueda.

PREGUNTA DEL ASESOR:
{pregunta}

RESPUESTA DEL ASISTENTE:
{respuesta}

REFERENCIA (patrón oro — si la respuesta la contradice, gana la referencia):
{entrada de la matriz de productos, o "NO APLICA"}

DIMENSIÓN A EVALUAR: {nombre}
{definición de la dimensión y qué significa 0, 1 y 2}

INSTRUCCIONES
1. Antes de puntuar, razona paso a paso: identifica qué afirma la respuesta,
   qué dice la referencia, y en qué difieren.
2. Cita textualmente el fragmento de la respuesta en que basas tu puntaje.
3. NO premies la extensión. Una respuesta corta y correcta vale más que una
   larga y correcta. Si la respuesta es larga, verifica que la longitud aporte.
4. NO asumas que la respuesta es correcta porque suene segura o porque cite
   un documento. Verifica que lo citado sustente lo afirmado.
5. Si no tienes elementos para decidir, responde puntaje = NULO. No adivines.

FORMATO DE SALIDA (JSON):
{"razonamiento": "...", "fragmento_citado": "...", "puntaje": 0|1|2|"NULO",
 "riesgo_regulatorio": true|false}
```

⚠️ **La instrucción 3 no es opcional.** El sesgo de estilo/verbosidad es el sesgo dominante de los
jueces LLM en el estado actual del campo, por encima del sesgo de posición que la literatura
original de 2023 destacaba.

### 11.4 ⭐ Calibración humana — obligatoria, y es el paso que casi todos se saltan

**Un juez sin calibrar no produce evidencia, produce una opinión con formato de número.**

| Paso | Detalle |
|---|---|
| **1 · Muestra** | **Mínimo 20%** de los ítems, elegidos al azar, **nunca los más fáciles** |
| **2 · Jueces humanos** | **Dos personas independientes**, con la misma rúbrica, sin ver el puntaje del modelo ni el del otro |
| **3 · Estadístico** | **Cohen's κ** para dos evaluadores; **Krippendorff's α** si son más de dos o si se trata la escala como ordinal |
| **4 · Umbral** | **κ ≥ 0,60** para usar el juez con supervisión · **κ ≥ 0,70** para usarlo solo. **Por debajo de 0,60 el problema es la rúbrica, no el juez** — se reescribe la definición de la dimensión y se recalibra |
| **5 · Recalibración** | Repetir **cada vez que cambie la rúbrica, el banco de preguntas o la versión del modelo juez** |

⭐ **La referencia de aceptabilidad:** en el trabajo fundacional, el juez LLM alcanzó **>80% de
acuerdo con evaluadores humanos — el mismo nivel de acuerdo que tienen los humanos entre sí.** Ese
es el techo razonable a esperar, y el criterio: **el juez es aceptable cuando concuerda con un humano
tanto como dos humanos concuerdan entre ellos.**

### 11.5 Los sesgos, en orden de importancia real para este caso

| Sesgo | Riesgo aquí | Mitigación |
|---|---|---|
| ⭐ **Estilo / verbosidad** | **Alto.** AIDA genera speeches y cuadros: respuestas largas por diseño | Instrucción explícita + registrar T10 + revisar correlación puntaje-longitud al final |
| **Posición** | Bajo, pero presente en la comparación pareada | Correr cada par dos veces con orden invertido |
| **Auto-preferencia** | ⭐ **Bajo, y a favor.** El juez es Claude; **AIDA corre sobre Google**, así que no se está evaluando a sí mismo | Ninguna necesaria. **Declararlo como fortaleza del diseño** |
| **Razonamiento numérico** | **Medio-alto.** Sumas aseguradas, edades, carencias, porcentajes | ⭐ **Los ítems con cifras se verifican a mano contra la matriz, no se delegan al juez** |
| **Deferencia a la seguridad** | Alto — el modo de falla dominante es afirmar con cita falsa | Instrucción 4 del prompt + T11 (tasa de cita rota) |

### 11.6 Lo que este bloque no puede hacer

- **No prueba que AIDA sea mala o buena para el asesor.** Prueba que sus respuestas cumplen o no una
  rúbrica. La relación entre eso y la venta es una hipótesis, no un resultado.
- **No reemplaza el campo.** Todo lo conductual —verificación, fuga, abandono, carga emocional— queda
  fuera por definición.
- **No mide el objetivo por sí solo.** El objetivo tiene una mitad de calidad (Bloque F) y una mitad
  de tiempo (Bloque I). **Correr solo una de las dos deja el objetivo sin evaluar.**

---

## 12. Orden de ejecución recomendado

| # | Qué | Por qué primero | Costo |
|---|---|---|---|
| **1** | **B2, B3, B4** | ⭐ Distinguen *hueco de contenido* de *fuente no gobernada*. La prueba más informativa por unidad de esfuerzo | Horas |
| **2** | **Banco H (consistencia)** | Es la mejora #1 pedida y falsa la hipótesis de casi-duplicados | Horas |
| **3** | **Prueba del fragmento pegado** (§7 del dossier) | Separa capa A de capa B antes de invertir en limpiar nada | Una tarde |
| **4** | **Análisis de los logs** | Ya solicitados. Dan T1-T4, T8-T11 y el banco real de preguntas | Días |
| **5** | **Reemplazar el banco sintético** por preguntas reales de los logs | ⭐ El banco actual mide lo que a nosotros nos parece importante | Días |
| **6** | **Bancos F y G + juez calibrado** | Requiere el banco real y la calibración humana | 1-2 semanas |
| **7** | **Cronometraje y línea base sin AIDA (T5, T12)** | Necesita asesores; se agenda junto al shadowing | 1-2 semanas |
| **8** | **T6 y T7 en shadowing** | Las únicas que solo se obtienen mirando | Con el campo |

⚠️ **Los pasos 1-4 no requieren tocar a ningún asesor.** Conviene agotarlos antes de gastar la
disponibilidad de la fuerza de venta, que es el recurso escaso y el que carga la deuda de
credibilidad.

## 7. Hoja de registro

Una fila por pregunta ejecutada:

`id · fecha · sesión · pregunta · respuesta literal · agente al que delegó · ramo de la respuesta ·
D1 · D2 · D3 · D4 · D5 · D6 · ¿riesgo regulatorio? · capa (A/B/C/ruteo) · fuente donde vivía la
respuesta correcta · nota`

**Mínimo para línea base:** las 12 de B + las 8 de C + A1-A10 = **30 filas**. C7 se ejecuta 3 veces.
Con eso hay corpus para F1 y una línea base repetible tras cada cambio.
