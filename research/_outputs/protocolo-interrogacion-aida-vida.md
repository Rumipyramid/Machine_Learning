# Protocolo de interrogación de AIDA — ramo Vida

**Instrumento de diagnóstico.** Versión 0.1 · 2026-08-14
Construido sobre `_nodes/diagnostico-copiloto-ai-asesor-vida-rimac.md` (v1.4),
`_nodes/evaluacion-calidad-agentes-conversacionales-ia.md` (v1.0),
`_nodes/arquitectura-conocimiento-agentes-copilot.md` (v1.1) y
`_nodes/matriz-productos-vida-rimac.md` (v1.2, **fuente de verdad para calificar exactitud**).

> ⚠️ **Slot pendiente — "modelo de Shang".** Alejo pidió construir esto usando el modelo de Shang.
> **No se pudo identificar con certeza cuál es**, y el proyecto no permite citar por aproximación
> (ver reglas de eco de cita). Se buscó y no aparece en el códice ni como framework establecido de
> evaluación de chatbots. Los dos candidatos encontrados están al final (§6). **Las dimensiones de
> §3 son provisionales y están construidas sobre instrumentos ya verificados del repo; se
> reemplazan o se reordenan en cuanto se confirme el modelo.**

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

## 6. El slot de Shang — los dos candidatos encontrados

Ninguno se aplicó, porque ninguno es claramente "el modelo de Shang" para evaluar respuestas:

1. **Shang & Seddon (2000/2002)** — *A Comprehensive Framework for Classifying the Benefits of ERP
   Systems* / *Assessing and managing the benefits of enterprise systems* (Information Systems
   Journal 12(4):271-299). Cinco dimensiones de beneficio: **operacional, gerencial, estratégico,
   infraestructura TI y organizacional.** Es el "modelo de Shang" más conocido en sistemas
   empresariales, peer-reviewed y sólido — pero clasifica **beneficios de un sistema**, no calidad
   de respuestas. Encajaría muy bien para evaluar **qué valor entrega AIDA**, como bloque aparte.
2. **Otro Shang no identificado** — la búsqueda de "Shang" + evaluación de chatbots no devuelve un
   framework establecido con ese nombre.

**Tercera posibilidad a descartar:** que "Shang" sea una transcripción de otro apellido.

👉 **Confirmar con Alejo antes de la v0.2.** Si es Shang & Seddon, se agrega como **Bloque D** —
evaluación de beneficio en cinco dimensiones— sin tocar los Bloques A-C, que miden otra cosa.

---

## 7. Hoja de registro

Una fila por pregunta ejecutada:

`id · fecha · sesión · pregunta · respuesta literal · agente al que delegó · ramo de la respuesta ·
D1 · D2 · D3 · D4 · D5 · D6 · ¿riesgo regulatorio? · capa (A/B/C/ruteo) · fuente donde vivía la
respuesta correcta · nota`

**Mínimo para línea base:** las 12 de B + las 8 de C + A1-A10 = **30 filas**. C7 se ejecuta 3 veces.
Con eso hay corpus para F1 y una línea base repetible tras cada cambio.
