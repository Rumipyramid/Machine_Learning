# Protocolo de interrogación de AIDA — ramo Vida

**Instrumento de diagnóstico.** Versión 0.2 · 2026-08-14
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

Diseñadas para que **la respuesta correcta sea verificable** contra la matriz.

**Producto y cobertura (D1-D4)**
- B1. ¿Qué productos de vida individual puede ofrecer un asesor hoy?
- B2. ¿Qué cubre exactamente Vida Futuro Protegido y cuál es la suma asegurada mínima?
- B3. ¿Cuál es el periodo de carencia de la cobertura de Enfermedades Graves?
- B4. ¿Hasta qué edad se puede contratar la cobertura de Pérdida de Existencia Independiente?
- B5. ¿Qué diferencia hay entre Vida Contigo, Vida Ahorro Garantizado y Vida Ahorro con Devolución?
  *(⭐ Prueba de duplicado: **son el mismo producto con tres nombres**. Si AIDA los describe como
  tres productos distintos, es la confirmación directa de la hipótesis de casi-duplicados de §3
  capa A del node.)*
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

## 7. Hoja de registro

Una fila por pregunta ejecutada:

`id · fecha · sesión · pregunta · respuesta literal · agente al que delegó · ramo de la respuesta ·
D1 · D2 · D3 · D4 · D5 · D6 · ¿riesgo regulatorio? · capa (A/B/C/ruteo) · fuente donde vivía la
respuesta correcta · nota`

**Mínimo para línea base:** las 12 de B + las 8 de C + A1-A10 = **30 filas**. C7 se ejecuta 3 veces.
Con eso hay corpus para F1 y una línea base repetible tras cada cambio.
