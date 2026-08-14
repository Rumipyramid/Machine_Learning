# Diagnóstico del Copiloto AI del asesor de Vida (RIMAC) — proyecto asociado a Back to Basics

> Node. Fuente de verdad de este tema: **estado, diagnóstico y decisiones del workstream del
> Copiloto AI** que usa el asesor de venta de productos de Vida. Es un proyecto **asociado a**
> Back to Basics, no una sección suya: `[[proyecto-back-to-basics-ffvv-vida]]` sigue siendo la
> fuente de verdad del modelo de venta; este node lo es de la herramienta.
> Capa de **estado interno**. La capa de **evidencia externa** sobre cómo almacenar el
> conocimiento vive en `[[arquitectura-conocimiento-agentes-copilot]]`.
>
> Fecha de elaboración: 2026-08-14 · Última actualización: 2026-08-14 · Versión: v1.1
> (v1.1, mismo día, confirmado por Alejo: **se resuelve la ambigüedad de plataforma que v1.0
> declaraba bloqueante**. La herramienta diagnosticada es **AIDA**, construida con **Microsoft
> Copilot** y **ya desplegada en producción** para la fuerza de ventas. El prototipo sobre Claude
> es otra cosa —el del Plan Piloto, cuyo diseño además cambió—. Cambio estructural: fija el objeto
> del diagnóstico, activa con fuerza plena los límites técnicos de Copilot, y obliga a corregir una
> fuente de insumos que v1.0 había asignado mal — ver §4.)
> Origen: brief en borrador del usuario (Alejandro Rojas) el 2026-08-14, ordenado a pedido
> explícito ("todo lo que te voy diciendo por ahora es emborrador, ayúdame a ordenarlo").
> Fuentes nuevas: F-476 a F-478. Fuentes heredadas: el diagnóstico interno ya documentado en
> `proyecto-back-to-basics-ffvv-vida.md` (encuesta a 19 asesores, Taller de Manejo de Objeciones,
> backlog de 5 frentes) y los instrumentos de `evaluacion-calidad-agentes-conversacionales-ia.md`.

---

## 0. Encuadre — qué es este proyecto y qué no

**Objeto del diagnóstico: AIDA** — el copiloto de IA del asesor de Vida, **construido con
Microsoft Copilot** y **ya desplegado en producción** para la fuerza de ventas (confirmado por
Alejo, 2026-08-14).

⚠️ **No confundir con el prototipo sobre Claude** del Plan Piloto (§8 de
`[[proyecto-back-to-basics-ffvv-vida]]`), que es una herramienta distinta, creada para validar el
modelo de venta, y cuyo diseño cambió. Este node **no** diagnostica ese prototipo. La confusión
entre ambos estuvo documentada como hecho en el repositorio hasta el 2026-08-14 — ver la
corrección v1.5 de ese node.

**Es:** un diagnóstico de una herramienta **ya en producción**, con fallas reportadas por sus
usuarios, cuya base de conocimiento se sospecha causa principal. El entregable inmediato es
**documentación del problema**, no una solución construida.

**No es:** el diseño de un copiloto nuevo. Ni la validación del modelo de venta (eso es el Plan
Piloto, §8 del node de Back to Basics).

**Regla metodológica heredada del proyecto marco, que aplica de lleno aquí:** *toda exploración
del sistema es obligatoria antes de diseñar*. Traducido a este caso: **no se rediseña la base de
conocimiento antes de haber inventariado la actual y separado las capas de falla** (§3).

---

## 1. El brief, ordenado

Lo que se dijo en borrador, reordenado en cuatro frentes de trabajo con dependencias explícitas.
Esta es la estructura propuesta; los tres primeros frentes se pueden trabajar en paralelo, el
cuarto depende de los tres.

| # | Frente | Pregunta que responde | Entregable | Estado |
|---|---|---|---|---|
| **F1** | **Documentar las fallas del output** | ¿Qué falla exactamente, con qué frecuencia, y de qué tipo es cada falla? | Corpus de fallas clasificado + línea base medida | 🔴 No iniciado — hoy la evidencia es cualitativa y de segunda mano |
| **F2** | **Auditar la base de conocimiento** | ¿Qué hay realmente en la base, y cuánto de eso el agente ni siquiera puede leer? | Inventario por formato/peso/vigencia + lista de inconsumibles | 🔴 No iniciado — el protocolo está listo (§6 del node de arquitectura) |
| **F3** | **Definir la forma correcta de almacenar** | ¿Cómo debe estructurarse la información para que el agente la consuma? | ✅ **Resuelto con evidencia** | 🟢 `[[arquitectura-conocimiento-agentes-copilot]]` |
| **F4** | **Mapear qué debe hacer el asesor** | ¿Qué conductas están verificadas contra desempeño real, y cuáles debe soportar el copiloto? | Mapa de capacidades priorizado por evidencia | 🟡 Marco de priorización resuelto (§5); falta cruzarlo con el journey real |

**Problemática declarada, textual:** el copiloto "tiene fallas graves en el output" y "se alimenta
de una base de conocimientos desordenada, cargada con PPT, PDF, imágenes, documentos vacíos de
diferentes formatos y Words".

**Plataforma: confirmada.** AIDA está construida con **Microsoft Copilot** y desplegada en
producción. ⭐ Esto **activa con fuerza plena** todos los límites técnicos de
`[[arquitectura-conocimiento-agentes-copilot]]` — ya no son "principios que se transfieren", son
**los techos exactos bajo los que AIDA opera hoy**: tablas no parseadas, 36.000 caracteres por
archivo, ≤300 páginas totales, PDF escaneado ilegible, imagen sin alt-text invisible, y el techo de
7 MB o 200 MB según licencia.

**Expectativa declarada:** "que ayude al asesor durante su gestión de venta."

---

## 2. Lo que ya sabíamos antes de este brief

Esto **no parte de cero.** El repositorio ya tenía evidencia primaria del problema, levantada por
el propio equipo y documentada en `[[proyecto-back-to-basics-ffvv-vida]]`. Sirve como línea base
cualitativa y, sobre todo, como **corroboración independiente**: el brief de hoy coincide con lo
que los asesores dijeron por su cuenta hace semanas.

- **Uso real (encuesta a 19 asesores):** AIDA se usa "siempre" en **7/19 (36,8%)**, muy por debajo
  de Salesforce (84,2%) y WhatsApp (73,7%). Solo 1/19 declaró no usarla nunca — o sea, **el
  problema no es rechazo, es uso intermitente**: la abren y no siempre les sirve.
- **Queja textual de los asesores:** *"no da la información adecuada"*, *"no contesta bien casi
  nunca"* — empatada como herramienta a mejorar (4/19).
- **Corroboración desde otro instrumento:** el Taller de Manejo de Objeciones (NPS 96,67, 30
  asistentes) reportó como mejora pedida la **"consistencia del copiloto de IA"** — mismo defecto,
  levantado en un contexto distinto, por un método distinto.
- **Conducta compensatoria documentada:** los asesores usan **ChatGPT/Gemini por su cuenta** para
  cubrir los huecos de AIDA y del cotizador. ⭐ Este es el dato más importante de los cinco:
  significa que **la demanda de asistencia conversacional está validada** — el asesor ya decidió
  que quiere una IA que le ayude, y cuando la propia no responde, **se va a una de afuera**. El
  problema no es de adopción de la categoría; es de calidad del producto. (Y tiene una implicación
  de riesgo que este node debe nombrar: información de cliente y de producto saliendo por
  herramientas no gobernadas.)
- **Ya estaba priorizado:** el backlog de Back to Basics tiene como frente #1 de corto plazo
  *"resolver la consistencia de respuestas del copiloto de IA"*, con la instrucción de
  **centralizar funciones en el copiloto en vez de sumar herramientas sueltas**, cuidando no
  sobresaturar al asesor.

**Lectura:** tres instrumentos independientes (encuesta, taller, brief de hoy) convergen en el
mismo defecto — **inconsistencia**, no ausencia de información. Eso es una pista causal fuerte, y
apunta a un mecanismo concreto: ver §3, capa A.

⭐ **Hallazgo agregado en v1.1 — el asesor tiene (o iba a tener) dos IA en paralelo.** Al separar
AIDA del prototipo del piloto aparece algo que ningún documento del proyecto había hecho explícito:
AIDA **ya está desplegada** en la fuerza de ventas, y el prototipo sobre Claude sería **una segunda
herramienta de IA** para el mismo asesor. Eso:

- **contradice la premisa de diseño del Plan Piloto** — *"el asesor interactúa con una sola
  herramienta"* (§8 de Back to Basics) — que describe el mundo del piloto, no el del campo;
- **contradice el propio lineamiento del backlog** de *"centralizar funciones en el copiloto en vez
  de sumar herramientas sueltas, cuidando no sobresaturar al asesor"*;
- **cae de lleno en Dx3** (alta carga cognitiva y emocional del asesor), que es justamente el
  diagnóstico que el proyecto dice estar atacando.

No se sigue de esto que el prototipo sobre Claude esté mal planteado — se sigue que **la relación
entre las dos herramientas es una decisión de diseño pendiente y no declarada**: ¿el prototipo
reemplaza a AIDA, la alimenta, se fusiona con ella, o convive? Conviene resolverlo explícitamente
antes de que el campo lo resuelva por su cuenta (que es lo que ya pasó con ChatGPT/Gemini).
⚠️ El rediseño del piloto anunciado por Alejo el 2026-08-14 puede haber cambiado esto — pendiente
de recibir la actualización.

---

## 3. La taxonomía que hay que aplicar antes de arreglar nada

**Este es el aporte central del node y el mayor riesgo del proyecto si se salta.**

"Fallas graves en el output" no es un diagnóstico: es un síntoma que puede venir de tres capas
distintas, que se arreglan con equipos, presupuestos y plazos distintos. Atribuir todo a la base
de conocimiento es la hipótesis más plausible **y no está verificada todavía**.

| Capa | Qué falla | Cómo se ve en el output | Cómo se confirma | Quién lo arregla |
|---|---|---|---|---|
| **A · Conocimiento** (recuperación) | El dato correcto no está, no es legible, está duplicado o desactualizado | Inventa datos de producto · da información de otro producto · dice "no tengo esa información" sobre algo que sí está · **responde distinto a la misma pregunta en dos momentos** | Auditoría de base (§6 del node de arquitectura) + *context precision/recall* de RAGAS | Contenido / Producto |
| **B · Instrucciones** (comportamiento) | El agente tiene el dato pero se comporta mal: tono, longitud, no sigue el modelo de venta, no pregunta antes de recomendar | Responde correcto pero inútil · da precio cuando debía redirigir con una pregunta · rompe la secuencia del modelo de venta | Mismo dato, distinta instrucción → ¿cambia la respuesta? Si cambia, es capa B | Diseño / CoE |
| **C · Plataforma** (límites del producto) | Techos duros: tamaño, formatos, licencia, ventana de contexto | Ignora documentos completos · trunca · no cita | Verificación de licencia y límites (F-469, F-470, F-471) | TI / Arquitectura |

### La prueba que separa la capa A de la capa B, y cuesta una tarde

Tomar 20 preguntas reales de asesores. Para cada una, **pegar manualmente el fragmento correcto de
la fuente** en el prompt y volver a preguntar.

- Si con el fragmento pegado **responde bien** → la información existe y el problema es que **no
  la encuentra**: es **capa A**, y se arregla con contenido.
- Si con el fragmento pegado **sigue respondiendo mal** → es **capa B**, y ninguna limpieza de la
  base lo va a resolver.

⭐ **El síntoma de "inconsistencia" (la misma pregunta contestada distinto en dos momentos) tiene
una firma causal muy específica: apunta a duplicados o casi-duplicados en la base** — versiones
distintas del mismo documento, de las que cada consulta recupera una. Es la hipótesis principal a
falsar en F2, y es consistente con una base cargada por acumulación a lo largo del tiempo.

---

## 4. Cómo documentar las fallas (F1) sin producir un anecdotario

El riesgo de F1 es terminar con una lista de quejas sin estructura, que no permita priorizar ni
medir mejora. El repositorio **ya tiene el instrumento**:
`[[evaluacion-calidad-agentes-conversacionales-ia]]`, cuyo aporte central aplica exactamente aquí
— **hay tres ejes que no deben mezclarse en un puntaje único**:

1. **Éxito de tarea** — ¿resolvió lo que el asesor necesitaba?
2. **Percepción del asesor** — ¿se sintió útil, claro, confiable? (escalas validadas: **BUS-11** es
   la más cercana al caso, chatbot comercial; **CUQ** tiene un factor específico de *manejo de
   errores*)
3. **Corrección objetiva** — ¿lo que dijo es fiel a la fuente real? (**RAGAS**: *faithfulness* para
   alucinación, *context precision/recall* para calidad de recuperación — F-151)

El eje 3 es el que responde "¿tiene fallas graves?" con un número defendible ante un comité, y el
que distingue **capa A de capa B** de §3.

**Formato propuesto para el corpus de fallas** — una fila por falla observada:

`pregunta del asesor · respuesta del agente · respuesta correcta · fuente donde vivía la respuesta ·
capa (A/B/C) · severidad · ¿es de producto regulado?`

Dos campos merecen justificación: **"fuente donde vivía la respuesta"** es lo que convierte el
corpus en un mapa de huecos de la base — sin él, la lista no dice qué arreglar. Y **"¿es de
producto regulado?"** separa la falla cosmética de la falla con riesgo: un error sobre coberturas,
exclusiones o precio dicho a un cliente no es un problema de calidad, es un problema de
cumplimiento.

**⚠️ Corrección de v1.1 — de dónde salen las preguntas reales.** La v1.0 de este node decía que el
indicador del Plan Piloto (*"consultas sin respuesta satisfactoria y temas más consultados"*, §8 de
Back to Basics) **era** el corpus de F1 y solo había que ir a buscarlo. **Eso era incorrecto**: ese
indicador mide **el prototipo sobre Claude**, no AIDA. Sirve para el prototipo; no dice nada sobre
la herramienta desplegada.

Para AIDA, las fuentes de preguntas reales son otras, en este orden de preferencia:

1. **Telemetría propia de AIDA** — logs de conversación de la herramienta en producción. Es la
   fuente ideal: volumen real, sin sesgo de recuerdo, y permite medir frecuencia además de tipo.
   **Verificar primero si existe y si es accesible** (ver P4 en §6); en muchos despliegues de
   Copilot la analítica está disponible pero nadie la ha mirado.
2. **Las 19 respuestas de la encuesta ya levantada** — contienen quejas textuales pero no los pares
   pregunta/respuesta que el corpus necesita. Sirven para *tipificar* las fallas, no para medirlas.
3. **Levantamiento dirigido con asesores** — pedir a un grupo pequeño que registre, durante una
   semana, las consultas que AIDA no resolvió. Es lo más caro en tiempo de asesor: usarlo solo si 1
   no existe, y respetando el principio de que la carga de recolección es de la CoE.
4. **Las conversaciones que los asesores están teniendo con ChatGPT/Gemini** (§2) son, en la
   práctica, **el registro de lo que AIDA no les resolvió**. Es la fuente más rica y la más difícil
   de obtener por la vía formal — pero como diagnóstico cualitativo, preguntarle a un asesor "¿qué
   le preguntas a ChatGPT que no le preguntas a AIDA?" es probablemente la pregunta más eficiente
   de todo este proyecto.

---

## 5. Qué debe hacer el asesor — y qué de eso está verificado

Aquí la pregunta del brief era: qué elementos, verificados, impactan de verdad en productividad y
venta. La respuesta tiene dos hallazgos independientes que apuntan en la misma dirección.

### 5.1 El copiloto no rinde igual para todos — y la diferencia es enorme

La mejor evidencia causal disponible (**F-476**, Brynjolfsson, Li & Raymond, *QJE* 2025, 🟢A,
5.179 agentes, despliegue escalonado, desempeño objetivo) sobre un asistente conversacional de IA
en trabajo de conversación asistida:

- **+14% de productividad en promedio** (casos resueltos por hora)
- **+34% en trabajadores novatos y de baja calificación**
- **impacto mínimo en los experimentados y altamente calificados**
- mecanismo declarado: **la IA difunde las mejores prácticas de los trabajadores más capaces**
- efectos secundarios: mejora el sentimiento del cliente y **la retención de empleados**

**Tres implicaciones directas para este proyecto:**

1. **El copiloto se diseña para el asesor nuevo, no para el asesor promedio.** El promedio de +14%
   es un artefacto estadístico de dos poblaciones distintas; diseñar contra el promedio es diseñar
   contra nadie.
2. **La adopción actual hay que releerla por antigüedad.** El "AIDA 7/19 siempre" es un promedio
   que probablemente esconde el mismo patrón. **Reanalizar la encuesta cortando por antigüedad es
   trabajo de una tarde sobre datos ya levantados** — y si el patrón aparece, cambia a quién se le
   pregunta y para quién se construye. (El piloto tiene 4 de 10 asesores con 6 meses de antigüedad:
   la muestra para verlo ya existe.)
3. **El mecanismo dice qué cargar en la base:** si el efecto viene de *difundir las mejores
   prácticas de los mejores*, entonces el activo más valioso no es el catálogo de producto — es
   **cómo resuelven los mejores asesores las conversaciones difíciles**. Eso hoy no está escrito en
   ninguna parte.

⚠️ **Descuento honesto:** el estudio es de soporte al cliente, no de venta consultiva de vida. La
transferencia es plausible por similitud de tarea (conversación asistida sobre una base de
conocimiento), **no demostrada**. Tratar la dirección como sólida y la magnitud como hipótesis.

### 5.2 Qué conducta del asesor está verificada contra desempeño real

**F-477** (Franke & Park, *JMR* 2006, 🟢A, meta-análisis de 155 muestras y **>31.000 vendedores**)
hace una distinción que es exactamente lo que el brief pedía — separar lo verificado de lo que solo
se siente bien:

| Constructo | Autorreportado | Evaluado por el jefe | **Objetivo** |
|---|---|---|---|
| **Venta adaptativa** (cambiar la conducta durante la interacción según lo que el cliente muestra) | ✅ sube | ✅ sube | ✅ **sube** |
| **Orientación al cliente** (disposición general a poner al cliente primero) | ✅ sube | — | ❌ **no** |

⭐ **La asimetría es el hallazgo: la conducta situacional se paga en desempeño real; la actitud
declarada solo se paga en la autopercepción del vendedor.** Además, la dirección causal probada va
**adaptación → orientación al cliente** (adaptarse construye la orientación, no al revés), lo que
invierte el orden de muchos programas de formación comercial: no se entrena la actitud esperando
que produzca conducta, se entrena la conducta.

Vigencia verificada: el constructo sigue vivo y en expansión, con revisiones integradoras
publicadas en 2025 (**F-478**) — no es un hallazgo de 2006 que el campo haya abandonado. ⚠️ De
F-478 **no usar cifras de efecto**: no se accedió al texto completo.

### 5.3 La convergencia que ordena la prioridad

Tres fuentes independientes —evidencia externa, la encuesta interna y el taller— apuntan al mismo
punto del journey:

- **La evidencia** dice que lo que se paga es la **adaptación en vivo** (F-477).
- **Los asesores** dicen que lo que más necesitan es **manejo de objeciones** (42%, el tema más
  pedido) y que el momento de mayor necesidad es **el cierre** (~40%).
- **El taller** confirma que lo que valoran es **casuística real** + práctica con feedback.

Manejo de objeciones en el cierre **es** venta adaptativa: es el momento donde el asesor tiene que
leer una señal del cliente y cambiar de camino en tiempo real.

**De ahí sale el criterio de priorización del copiloto**, que es la respuesta al frente F4:

| Prioridad | Capacidad | Por qué |
|---|---|---|
| **1** | Apoyo a la **adaptación en vivo**: qué responder ante esta objeción, con este cliente, en este momento | Único constructo con efecto verificado sobre desempeño **objetivo** (F-477) + es lo que los asesores piden (42%) + es el momento declarado de mayor necesidad (cierre) |
| **2** | **Casuística real** de los mejores asesores, recuperable por situación | Es el mecanismo por el que la IA produce el efecto (F-476: difunde las mejores prácticas) + driver de valor #1 del taller |
| **3** | **Datos duros de producto** (coberturas, exclusiones, precios), exactos y trazables | Condición de no-daño: es donde una falla es riesgo de cumplimiento, no molestia. Pero **no es el diferencial** — la encuesta dice que el asesor **no pide más información de producto** |
| **4** | Contenido de actitud, valores, identidad de marca | Efecto verificado solo sobre desempeño **autorreportado** (F-477). No cargarlo como prioridad de la base |

⚠️ **Nota de disciplina, coherente con las reglas del proyecto sobre cadenas de eco de cita:** este
mercado está saturado de cifras tipo *"los vendedores pierden el 30% de su tiempo buscando
información"* o *"la IA aumenta las ventas un X%"*, casi siempre emitidas por proveedores de
herramientas de sales enablement y sin fuente primaria rastreable. **No incorporar ninguna de esas
cifras al proyecto sin rastrear el origen** — es exactamente la falla que
`[[tendencias-diseno-innovacion]]` documentó seis veces (reglas C19-C22).

---

## 6. Preguntas abiertas — lo que hay que confirmar antes de avanzar

**✅ P1 — Plataforma: RESUELTA (2026-08-14, confirmado por Alejo).** AIDA es la herramienta
**creada con Microsoft Copilot y ya desplegada** para la fuerza de ventas; el prototipo sobre Claude
es el del Plan Piloto, una herramienta distinta cuyo diseño además cambió. **Era la lectura (a) de
las tres que v1.0 planteaba** — es decir, hay dos herramientas de IA, y eso es en sí mismo un
hallazgo de diagnóstico (ver §2). Consecuencia práctica: **todos los límites técnicos de
`[[arquitectura-conocimiento-agentes-copilot]]` aplican a AIDA con fuerza plena**, no como
principios transferidos.

**P2 — Licenciamiento (ahora es la pregunta técnica #1).** ¿El agente opera con licencia de Microsoft 365 Copilot en el mismo tenant?
Es la diferencia entre poder usar archivos de 200 MB o solo de **menos de 7 MB** (F-470). Un deck
comercial con imágenes supera 7 MB con facilidad — si la respuesta es "sin licencia en el tenant",
buena parte de la base podría estar fuera de alcance por esta sola razón.

**P3 — ¿Dónde vive la base?** SharePoint, Teams, carpeta de red, cargada directamente en el agente.
Determina qué reglas de gobierno de §5 del node de arquitectura son aplicables.

**P4 — ¿Quién es el dueño de la base hoy?** Si nadie la gobierna, el problema **volverá** aunque se
limpie una vez. Es la diferencia entre un arreglo y una solución.

**P5 — ¿Existe medición previa?** ¿Hay logs de conversaciones, tasa de uso, consultas sin respuesta?
El Plan Piloto declaraba que **el tracking del prototipo no existía todavía** al 24/07 — confirmar
si se habilitó, porque de eso depende si F1 se levanta de datos o de entrevistas.

---

## 7. Plan de trabajo propuesto

Secuencia sugerida. F2 primero porque es barato, rápido y **puede explicar el problema completo
antes de gastar en lo demás**.

| Paso | Qué | Depende de | Salida |
|---|---|---|---|
| ~~**0**~~ | ~~Resolver P1 (plataforma)~~ | — | ✅ **Resuelto 2026-08-14: AIDA = Copilot, desplegada** |
| **0b** | Resolver **P2 (licencia)** y **P3 (dónde vive la base)** | — | Define si aplica el techo de 7 MB o el de 200 MB |
| **1** | **F2 · Inventario de la base** — protocolo de 7 pasos (§6 del node de arquitectura) | P2, P3 | Cuánto de la base es inconsumible, duplicado o vacío |
| **2** | **F1 · Corpus de fallas** — 20-30 casos reales, clasificados por capa A/B/C | Telemetría de AIDA o levantamiento dirigido (§4, P5) | Línea base medible + mapa de huecos |
| **3** | **Prueba A/B de capa** (§3) — pegar el fragmento correcto y volver a preguntar | Paso 2 | Veredicto: ¿es conocimiento o es comportamiento? |
| **4** | Reanálisis de la encuesta **cortando por antigüedad** | Datos ya levantados | Confirma o refuta la tesis de segmentación de §5.1 |
| **5** | Piloto de reescritura sobre **un** dominio acotado (p. ej. objeciones de cierre) | Pasos 1-3 | Prueba de que reformatear mueve la aguja, antes de reescribir todo |
| **6** | Mapa de capacidades del copiloto priorizado | Pasos 3-5 | Respuesta a F4 |

**Principio de diseño recomendado, heredado del Plan Piloto:** *la carga de recolección es de la
CoE, no del asesor.* Todo lo que se pueda levantar de logs, que no se le pregunte al asesor.

**Por qué el paso 5 antes de reescribir todo:** no existe evidencia cuantificada de cuánto mejora
la exactitud al reformatear una base corporativa (§7 del node de arquitectura). Un dominio acotado
con medición antes/después **produce la cifra propia** en vez de importar una de un proveedor — y
es exactamente la disciplina que el proyecto ya aplica (tesis 6 del Lobo: no copiar tamaño de
efecto de catálogo, testear en la propia población).

---

## Limitaciones

- **Este node ordena un brief en borrador, no un diagnóstico ejecutado.** F1 y F2 no están
  iniciados: todo lo que dice sobre las causas es **hipótesis priorizada por evidencia**, no
  hallazgo verificado. La hipótesis principal —que la inconsistencia viene de duplicados y de
  formatos ilegibles— es plausible y coherente con tres instrumentos, y **sigue sin verificarse**.
- **No se ha visto la base de conocimiento ni el agente.** Todo el diagnóstico técnico es
  deductivo, a partir de los formatos que el usuario enumeró y de la documentación de la
  plataforma.
- ~~La ambigüedad de plataforma (P1) no está resuelta.~~ **Resuelta el 2026-08-14** (AIDA =
  Microsoft Copilot, desplegada). Queda en pie **P2**: sin saber el licenciamiento, no se sabe si el
  techo de archivo aplicable es de 7 MB o de 200 MB — una diferencia de casi 30× que puede cambiar
  sola el veredicto del inventario.
- **El Plan Piloto (§8 de Back to Basics) cambió** y la actualización no se ha recibido. Todo lo que
  este node dice sobre el piloto y sobre la relación entre AIDA y el prototipo describe el diseño de
  julio 2026, no el vigente.
- Los datos internos citados en §2 provienen de `proyecto-back-to-basics-ffvv-vida.md`, que a su vez
  los toma de documentos internos que **no viven en este repositorio**.
- F-476 es de soporte al cliente, no de venta consultiva de vida: dirección sólida, magnitud a
  validar en población propia.

---

## Conexiones

- [[arquitectura-conocimiento-agentes-copilot]] — la evidencia externa que responde el frente F3:
  cómo debe almacenarse la información. Este node la consume; ese node la sostiene.
- [[proyecto-back-to-basics-ffvv-vida]] — el proyecto marco al que este está asociado. De ahí vienen
  la encuesta a 19 asesores, el Taller de Manejo de Objeciones, el backlog que ya priorizaba la
  consistencia del copiloto, y el Plan Piloto cuyo indicador de "consultas sin respuesta
  satisfactoria" es insumo directo de F1.
- [[evaluacion-calidad-agentes-conversacionales-ia]] — el instrumento de medición de F1: los tres
  ejes que no hay que mezclar, BUS-11/CUQ para percepción y RAGAS para corrección objetiva.
- [[futuro-asesores-seguros-venta-digital]] — el marco de por qué invertir en potenciar al asesor
  humano en vez de reemplazarlo; este copiloto es una instancia concreta de esa tesis.
- [[matriz-productos-vida-rimac]] — el catálogo de productos que la base de conocimiento debe
  representar correctamente; su trazabilidad de fuentes y niveles de confianza es directamente
  reutilizable como criterio de vigencia para la capa 3 de §5.3.
- [[material-visual-venta-consultiva]] — por qué el material visual sí importa para el **cliente**,
  aunque sea ilegible para el **agente**: dos artefactos, dos audiencias.
