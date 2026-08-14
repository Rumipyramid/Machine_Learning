# Diagnóstico del Copiloto AI del asesor de Vida (RIMAC) — proyecto asociado a Back to Basics

> Node. Fuente de verdad de este tema: **estado, diagnóstico y decisiones del workstream del
> Copiloto AI** que usa el asesor de venta de productos de Vida. Es un proyecto **asociado a**
> Back to Basics, no una sección suya: `[[proyecto-back-to-basics-ffvv-vida]]` sigue siendo la
> fuente de verdad del modelo de venta; este node lo es de la herramienta.
> Capa de **estado interno**. La capa de **evidencia externa** sobre cómo almacenar el
> conocimiento vive en `[[arquitectura-conocimiento-agentes-copilot]]`.
>
> Fecha de elaboración: 2026-08-14 · Última actualización: 2026-08-14 · Versión: v1.4
> (v1.4: corrige §9.2 — **el modelo de venta ES la fuente canónica** y las contradicciones se
> resuelven ahí, lo que convierte la base de AIDA en una **derivación del modelo** en vez de una
> carpeta a ordenar; y agrega §10, la barrera sistémica de actualización de producto: el retraso
> tiene un componente regulatorio irreducible (SBS, F-482) y uno comercial que no lo es, hoy
> acoplados; la dirección de traducción propuesta está invertida; y la evidencia de aceleración es
> **12/12 de proveedores** (F-483), con una sola fuente independiente que además reporta alta tasa
> de fracaso de implementación (F-484).)
> (v1.3: precisa el **mandato del copiloto** —centralizar y reducir carga cognitiva/emocional— y
> agrega §9, el hallazgo mayor hasta ahora: **el copiloto no puede resolver la contradicción aguas
> arriba, solo ocultarla**, por lo que la inconsistencia reportada de AIDA puede ser la
> inconsistencia de la organización reflejada. Corrige además la lectura estrecha de "multimodal"
> que hizo v1.2 — ver §8. v1.2: mapa de 6 frentes y 3 agentes desplegados, reancla a Dx2, §8 de
> arquitectura.)
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

**Expectativa declarada (v1.0):** "que ayude al asesor durante su gestión de venta."

**Mandato precisado (v1.3, Alejo 2026-08-14) — vale la pena citarlo entero porque nombra la causa,
no solo la función:** el copiloto debe **centralizar y facilitar el trabajo del asesor, reduciendo
su carga cognitiva y emocional**, hoy alta por dos demandas concretas:

1. **registrar en distintas plataformas**, y
2. **leer información física y virtual que a veces puede ser contradictoria.**

⚠️ La segunda causa no es un problema de la herramienta y **no se resuelve dentro de ella** — ver §9.
Es el hallazgo más importante de esta versión del node.

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

### 2.1 El mapa real de frentes del asesor (agregado en v1.2, declarado por Alejo 2026-08-14)

El asesor no opera contra una herramienta ni contra dos. Opera hoy contra **seis frentes**:

| # | Frente | Naturaleza | ¿Es un agente de IA? |
|---|---|---|---|
| 1 | **Salesforce** | Sistema de **registro** (CRM) — obligación operativa, no ayuda | No |
| 2 | **AIDA** | Superficie de **conocimiento/conversación**, en producción | ✅ Sí (Microsoft Copilot) |
| 3 | **Material físico** | Artefacto para el **cliente**, no para el asesor | No |
| 4 | **Agente de suscripción** | Apoyo en el proceso de **suscripción/underwriting** | ✅ Sí |
| 5 | **Sales Coach** | **Entrenamiento** en fases iniciales | ✅ Sí |
| 6 | **Feedback de jefatura** | Canal **humano**, relacional | No |

⭐ **Hallazgo (corrige y amplía el de v1.1): no son dos IA en paralelo, son tres agentes ya
desplegados** —AIDA, suscripción y Sales Coach— más el prototipo del piloto como cuarto candidato.
La v1.1 de este node subestimó el problema porque solo conocía dos.

**Esto reancla el diagnóstico.** v1.1 lo ataba a Dx3 (carga cognitiva del asesor). Con el mapa
completo, el frente principal es **Dx2** — *los elementos del sistema no siempre conversan entre sí,
y el usuario recibe información inconsistente durante su compra*. Tres agentes con bases de
conocimiento distintas, sin contrato de consistencia entre ellos, **son literalmente el mecanismo
que Dx2 describe.** Dx3 sigue aplicando, pero como consecuencia, no como causa raíz.

**Dos distinciones que hay que hacer antes de decidir qué consolidar** — porque "seis frentes" no
son seis cosas del mismo tipo:

- **Frentes 3 y 6 no compiten con el copiloto: lo complementan.** El material físico tiene otra
  audiencia (el cliente — ver `[[material-visual-venta-consultiva]]`), y el feedback de jefatura es
  un vínculo humano cuyo valor no es informacional. **Absorberlos sería un error de diseño**, no un
  avance de consolidación.
- **El frente 1 es de otra especie.** Salesforce es el **sistema de registro**: tiene obligaciones
  de dato, trazabilidad y reportería que no son "una función front". Lo que puede consolidarse es
  **la interacción** con Salesforce (que el copiloto registre por el asesor), no el sistema.

La pregunta de qué hacer con los frentes 2, 4 y 5 —los tres agentes— es de arquitectura y tiene
respuesta con evidencia: ver §8.

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

**P6 — ¿Los tres agentes comparten base de conocimiento o cada uno tiene la suya?** Decide si el
mapa de §8.1 describe la arquitectura actual o la contradice. Si comparten base, el problema de
recuperación es peor de lo estimado.

**P7 — ¿Quién es dueño de cada agente?** Si AIDA, el agente de suscripción y Sales Coach dependen de
equipos distintos, "una sola puerta de entrada" es un problema de gobierno antes que de tecnología.

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

## 8. ¿Debe el copiloto concentrar todos los frentes? (agregado en v1.2)

**El lineamiento declarado** (Alejo, 2026-08-14, derivado del diagnóstico sistémico de la FFVV): el
modelo de ventas debe funcionar de forma **multimodal, desplegado en distintos frentes**, pero el
copiloto **debería concentrar todas o la mayoría de las funciones front** del asesor.

Leído literal, eso parece contradictorio (desplegar en varios frentes *y* concentrar en uno) y
además choca con el techo de ≤300 páginas de `[[arquitectura-conocimiento-agentes-copilot]]`. No es
contradictorio: es que **se están mezclando tres capas que hay que decidir por separado.**

> ⚠️ **Corrección de v1.3 a mi propia lectura de v1.2.** La v1.2 de este node interpretó
> "multimodal" como *"el modelo está presente en todas las superficies del asesor"*. **Es más
> estrecho que lo que el lineamiento dice.** Multimodal significa que el modelo de venta es
> **transversal al ecosistema de ventas** y se instancia en frentes institucionales distintos, la
> mayoría de los cuales **no son superficies del asesor**: el modelo por competencias de selección y
> entrenamiento, el diseño de pautas publicitarias, el copiloto, y los sistemas del canal. Ver §1.1
> de `[[proyecto-back-to-basics-ffvv-vida]]`, donde queda documentado el modelo mismo.

| Capa | Pregunta | Respuesta con evidencia |
|---|---|---|
| **Distribución del modelo** | ¿Dónde vive el modelo de venta? | **Multimodal y transversal** — se instancia en 4 frentes institucionales con dueños distintos (talento, marketing, tecnología, canal). **El copiloto es uno de ellos, no su casa.** |
| **Interfaz del asesor** | ¿A cuántos lugares tiene que ir el asesor? | **Uno** — consolidar. Es lo que ataca Dx3 y lo que pide el lineamiento. |
| **Recuperación** | ¿Cuántas bases de conocimiento hay detrás? | **Varias, separadas por dominio.** ⚠️ **Consolidarlas empeora el problema.** |

**Consecuencia de la primera fila, que conviene tener explícita:** el copiloto es un **consumidor**
del modelo, no su dueño. Sus criterios de éxito (carga reducida, respuestas correctas) **no son** los
del modelo (adopción consistente en los cuatro frentes). Confundirlos hace que el copiloto cargue
con culpas del modelo, y que problemas del copiloto se lean como fracaso del modelo.

### 8.1 Por qué consolidar las bases sería un error

Es el punto donde la intuición de consolidación falla, y la evidencia es consistente en dos frentes
independientes:

- **El fabricante (F-479):** cada subagente debe tener **fuentes de conocimiento distintas y no
  superpuestas**; si dos buscan en la misma base, uno encuentra primero y el otro no aporta nada.
  Recomienda agentes separados cuando hay **dominio de expertise propio**, **reglas de gobierno o
  control de acceso distintas**, o reutilización como servicio.
- **Evidencia externa (F-480, preprint):** centralizar todo en un solo sistema RAG **agranda el
  espacio de recuperación y aumenta la evidencia irrelevante**; la señal-ruido cae cuando las bases
  no están separadas por dominio. Particionar por dominio y rutear **reduce el ruido y la
  interferencia entre temas**, con **mayor exactitud y menor alucinación** que el agente único.

⭐ **Aplicado a RIMAC, esto invierte la conclusión intuitiva:** los tres agentes (venta, suscripción,
entrenamiento) **cumplen casi uno a uno los criterios de Microsoft para estar separados** —
dominios de expertise distintos, y la suscripción con reglas de gobierno claramente distintas. **Es
probable que estén bien separados en la capa de conocimiento.** El problema no es que sean tres: es
que **el asesor tiene que saber cuál es cuál y entrar a cada uno por su cuenta.**

### 8.2 La forma que sí satisface el lineamiento

**Una puerta de entrada, varios dominios detrás.** El asesor le habla a un solo copiloto; el
copiloto rutea a la base correcta según lo que le pregunten. Es un patrón soportado explícitamente
por Copilot Studio (orquestación multi-agente, F-479), no un desarrollo a medida.

Eso satisface las tres capas a la vez: el modelo se despliega multimodal, el asesor ve una sola
superficie, y cada dominio conserva su espacio de recuperación limpio.

**Qué se consolida y qué no:**

| Frente | Decisión | Por qué |
|---|---|---|
| AIDA (venta) | **Es la puerta** | Ya es la superficie conversacional en producción |
| Agente de suscripción | **Detrás de la puerta**, base separada | Dominio y gobierno distintos (F-479) — mezclarlo sube el riesgo donde el error es más caro |
| Sales Coach | **Detrás de la puerta**, modo separado | Práctica y producción son modos distintos; ver 8.3 |
| Salesforce | **Se consolida la interacción, no el sistema** | Que el copiloto registre por el asesor; el CRM sigue siendo el sistema de registro |
| Material físico | **No se absorbe** | Otra audiencia: el cliente |
| Feedback de jefatura | **No se absorbe** | Su valor no es informacional |

### 8.3 Dos advertencias de secuencia

**1. La puerta única sobre bases rotas empeora el diagnóstico, no lo mejora.** Si se pone un
orquestador delante de tres agentes cuya calidad de conocimiento no se ha auditado, el asesor deja
de saber **cuál** falló — y el equipo pierde la señal que hoy sí tiene ("AIDA no contesta bien").
**F2 (auditoría de la base) va antes que cualquier consolidación de interfaz**, no después.

**2. El entrenamiento no sobrevive al contacto con una herramienta rota.** Hoy el asesor nuevo se
entrena en Sales Coach y luego trabaja en AIDA. Pero la mejor evidencia causal disponible (F-476)
dice que **el mayor efecto de un copiloto se da precisamente en los novatos (+34%)** — es decir, la
herramienta de la que más depende un asesor nuevo es **la de producción**, no la de entrenamiento.
Si AIDA falla, el asesor nuevo aprende un modelo en Sales Coach que después no puede ejecutar.
**Arreglar AIDA es precondición para que el valor de Sales Coach se materialice**, y probablemente
la intervención de mayor retorno de todo el mapa. (No se sigue de esto que Sales Coach deba
fusionarse con AIDA: la literatura de simulación en adultos —Sitzmann 2011, F-219— sostiene el valor
de un espacio de práctica seguro y separado de la conversación real con cliente.)

### 8.4 Lo que falta para cerrar esta sección

- **No se ha visto ninguno de los tres agentes.** Todo §8 es diseño deducido de la descripción de
  los frentes, no de una inspección.
- **No se sabe si los tres comparten base de conocimiento o tienen la suya.** Es la pregunta que
  decide si §8.1 describe la situación actual o la contradice — **P6**, ver §6.
- **No se sabe quién es dueño de cada agente** (¿el mismo equipo? ¿TI, Producto, Academia?).
  Determina si "una puerta de entrada" es un problema técnico o uno organizacional. **P7.**

---

## 9. La contradicción aguas arriba: lo que el copiloto no puede resolver (agregado en v1.3)

**El mandato del copiloto incluye una tarea que ningún copiloto puede cumplir.** Se le pide reducir
la carga de "leer información que a veces puede ser contradictoria". Pero:

> **Un sistema de recuperación no arbitra contradicciones. Recupera fragmentos y responde con lo que
> recuperó.** Frente a dos fuentes que se contradicen, no dice "hay dos versiones" — **toma una y
> responde con seguridad**, y puede tomar la otra en la consulta siguiente.

Es decir: el copiloto **no elimina la contradicción, la oculta** — y la convierte en algo peor,
porque el asesor pierde incluso la señal de que había dos versiones. Cuando leía dos documentos
contradictorios, al menos *veía* el conflicto.

⭐ **Esto reencuadra el defecto principal reportado.** Los asesores dicen que AIDA es **inconsistente**
("no contesta bien casi nunca", "consistencia del copiloto de IA"). Hasta v1.2 este node trataba la
inconsistencia como hipótesis de **duplicados en la base** (§3, capa A). Sigue siendo plausible, pero
ahora hay una hipótesis hermana **más profunda y con confirmación independiente del propio equipo**:

> **La inconsistencia de AIDA puede ser la inconsistencia de la organización, reflejada.**
> Si el modelo de venta se instancia en cuatro frentes sin fuente canónica (§1.1 de
> `[[proyecto-back-to-basics-ffvv-vida]]`), las versiones divergen; la base del copiloto hereda esa
> divergencia; y el agente la devuelve como respuestas que cambian.

La confirmación no viene de un análisis: viene de que **Alejo describe la contradicción como un
hecho ya observado en el material que el asesor lee hoy**, antes y fuera del copiloto.

### 9.1 Qué cambia esto en el plan

**Limpiar formatos es necesario y no es suficiente.** F2 (auditoría) detecta duplicados por
similitud; **no detecta contradicciones semánticas** entre documentos que se ven distintos y dicen
cosas incompatibles. Hay que agregar un paso:

| Paso | Qué | Por qué es distinto de F2 |
|---|---|---|
| **F2b · Detección de contradicciones** | Sobre los temas de mayor consulta (objeciones de cierre, coberturas, precios), contrastar **qué dice cada frente**: playbook, material físico, base de AIDA, pauta publicitaria, sistemas del canal | F2 pregunta *"¿es legible?"*; F2b pregunta *"¿dicen lo mismo?"*. Un documento puede ser perfectamente legible y perfectamente contradictorio |

**Cómo hacerlo barato:** no hace falta auditar todo. Tomar **los 10 temas más consultados** (que
salen del corpus de F1) y, para cada uno, poner lado a lado lo que dice cada frente. Donde haya
discrepancia, esa es una contradicción que el copiloto está reflejando hoy.

### 9.2 Quién resuelve la contradicción (corregido en v1.4 por Alejo)

> ⚠️ **Corrección a la v1.3 de este node.** La v1.3 planteaba que "si no hay fuente canónica, el
> copiloto no debería ser el primer arreglo" y proponía que el agente respondiera *"esto no está
> resuelto"*. **El planteamiento estaba mal encuadrado: daba por buscar una fuente canónica que ya
> está declarada.**

**El modelo de venta es la fuente canónica.** Es el único material y cuerpo de conocimiento de
consulta para todos los frentes multimodales (Alejo, 2026-08-14). **Las contradicciones se resuelven
en el modelo**, no en cada frente ni dentro del copiloto.

Eso convierte una discusión de gobierno abierta en **una regla operativa cerrada**, con tres
consecuencias inmediatas:

1. **La base de conocimiento de AIDA no debe ser una carpeta de documentos: debe ser una derivación
   del modelo.** Esto reencuadra F2 y F3 — el trabajo no es "ordenar la carpeta", es **reemplazar la
   carpeta por una derivación**. Ordenar una carpeta que no deriva del modelo produce una base
   limpia y aun así divergente.
2. **Toda contradicción detectada es un defecto contra el modelo**, no una decisión del equipo del
   copiloto. Se escala, se resuelve en el modelo, y **todos los frentes re-derivan**. Que el equipo
   del copiloto resuelva por su cuenta cuál versión es la buena es precisamente cómo se generó la
   divergencia.
3. **Todo lo que el copiloto necesite y no esté en el modelo es un hueco del modelo**, no un hueco
   de la base. El copiloto deja de ser un consumidor pasivo y pasa a ser **el mejor detector de
   huecos que el modelo puede tener**, porque recibe las preguntas reales de los asesores.

⭐ **El bucle que esto cierra.** El modelo ya es generativo hacia producto: cuando ninguna oferta
hace match con una motivación real, **emite un requerimiento de producto** (§1.1 de
`[[proyecto-back-to-basics-ffvv-vida]]`). Con esta regla, el modelo se vuelve generativo también
hacia el conocimiento: **cuando el copiloto no puede responder o encuentra una contradicción, emite
un requerimiento de contenido contra el modelo.** Mismo mecanismo, otra salida. Y le da al indicador
"consultas sin respuesta satisfactoria" un destino claro: **es el backlog del modelo.**

**Lo que sí sobrevive de la v1.3** como comportamiento de la herramienta (capa B, §3): mientras una
contradicción está en cola de resolución, **es preferible que el agente declare que el punto no está
resuelto a que elija en silencio una de dos versiones.** Ya no como sustituto del gobierno —que
existe— sino como **comportamiento de degradación honesta** mientras el modelo resuelve.

⚠️ **Matiz a confirmar (P8).** El modelo es canónico para el **conocimiento de venta** (cómo vender,
qué decir, cuándo). Los **parámetros de producto** (coberturas, exclusiones, precios) son un dominio
distinto, con otro dueño y otra cadencia — y con piso regulatorio (§10). La lectura de este node es
que el modelo **referencia** una fuente canónica de producto en vez de contenerla, lo que además es
consistente con la regla de dominios no superpuestos de §8. **Confirmar con Alejo.**

---

## 10. Barrera sistémica: la cadena de suministro de conocimiento de producto (v1.4)

**Declarada por Alejo (2026-08-14):** el negocio **no tiene forma de actualizar ágilmente la
información de productos** — cambios, bajas, altas. Hipótesis propuesta por él: un sistema que
traduzca documentos ejecutivos en una **matriz de productos con parámetros claros**.

Pregunta que hizo, textual: *¿existe alguna forma comprobada de agilizar esto?* Respuesta honesta en
tres partes.

### 10.1 Parte del retraso es irreducible — y conviene medirlo antes de atacarlo

En Perú los modelos de póliza están sujetos al **Registro de la SBS** (Res. SBS N° 7044-2013,
**F-482**). Modificar documentación registrada tiene plazos y condiciones normados, obliga a
identificar claramente las cláusulas modificadas, y **el modelo modificado recién se vuelve
obligatorio 30 días calendario después de notificada la Resolución**.

⭐ **Pero eso aplica a la capa contractual, no a la comercial.** El retraso que se vive tiene **dos
componentes con pisos totalmente distintos:**

| Capa | Qué es | Piso | ¿Acelerable? |
|---|---|---|---|
| **Contractual/registrada** | Condiciones, cláusulas, el modelo de póliza | **Regulatorio (SBS)** | ❌ No — es el costo de operar en el mercado |
| **Comercial/explicativa** | Cómo se explica, a qué motivación sirve, qué objeciones aparece, cómo se dimensiona | **Ninguno** | ✅ Sí — horas, no meses |

**El diagnóstico probable no es "el negocio es lento": es que las dos capas están acopladas** porque
viven en el mismo documento ejecutivo. La capa comercial hereda la cadencia regulatoria de la
contractual sin necesitarla. **Desacoplarlas es la palanca, y no requiere permiso de nadie.**

**Primera medición sugerida, barata:** tomar los 3 últimos cambios de producto y cronometrar dónde
se fue el tiempo — aprobación regulatoria vs. traducción interna a materiales. Si el grueso está en
la traducción interna, el problema es de proceso propio y se resuelve solo.

### 10.2 La dirección de la traducción está invertida

La hipótesis propuesta —*traducir documentos ejecutivos a una matriz*— **automatiza el síntoma**.
Mientras se siga autorando en PPT/PDF y luego traduciendo, hay un **desfase permanente** y la matriz
está desactualizada por diseño: cada cambio nace en el documento y llega tarde a la matriz.

La práctica establecida invierte el flujo:

> **La matriz es la fuente; los documentos ejecutivos se generan desde ella.** Se autora una vez en
> forma estructurada y se publica a N canales (autoría estructurada / publicación de fuente única).

Es exactamente la regla de **"una fuente canónica, N instanciaciones"** de §1.1 de
`[[proyecto-back-to-basics-ffvv-vida]]`, aplicada al dato de producto. Y encaja con §8: el modelo de
venta es canónico para el conocimiento de venta; la matriz de producto lo es para los parámetros.

⭐ **RIMAC ya tiene un prototipo de esto en este repositorio:**
`[[matriz-productos-vida-rimac]]` — catálogo de productos con coberturas, add-ons, **trazabilidad de
fuentes y niveles de confianza**. Se construyó a mano para otro fin, pero **es la especificación de
la matriz que se necesita**, incluida la parte que los proveedores no traen de fábrica: decir de
dónde salió cada dato y cuánto se confía en él. No hay que diseñarla desde cero — hay que decidir si
se promueve a fuente canónica, con dueño y cadencia.

### 10.3 Qué está comprobado y qué no

⚠️ **Advertencia de evidencia (F-483), y es fuerte:** se buscó específicamente evidencia de
aceleración y **12 de 12 fuentes encontradas en dos búsquedas independientes eran proveedores** que
venden la solución que la cifra justifica. Las cifras que circulan —"de 12-18 meses a 4-8 semanas",
"de 8-16 semanas a 20 minutos"— **no tienen estudio, muestra ni método**. **No usarlas en ningún
material de RIMAC.**

**Lo que sí está establecido:**

- **La práctica existe y es madura.** Los configuradores de producto ("product factory") son una
  categoría real usada por aseguradoras reales; la autoría estructurada de fuente única es
  disciplina de décadas (DITA es estándar OASIS). El **mecanismo** —parametrizar el producto y
  versionarlo con fecha de vigencia, en vez de describirlo en prosa— es sólido, y tiene un beneficio
  colateral relevante en seguros: permite **reconstruir qué condiciones aplicaban a una póliza
  emitida hace años**, en vez de aplicarle la configuración de hoy.
- **Evidencia independiente, la única encontrada (F-484):** la calidad del dato maestro de producto
  **sí impacta significativamente el desempeño del proceso** (peer-reviewed, aunque en dominio
  logístico, no seguros). Beneficios donde funciona: menor esfuerzo de reconciliación, mejor
  auditabilidad, mayor alineación regulatoria.
- ⚠️ **Y la contraevidencia, que hay que decir en la misma frase:** el análisis empírico de estas
  implementaciones encuentra **adopción heterogénea, capacidades fragmentadas y gobierno solo
  parcialmente formalizado** (F-484). Es decir: **la mayoría de las implementaciones no logran lo que
  la categoría promete.** El riesgo dominante de este frente no es elegir mal la herramienta — es
  comprar plataforma y no cambiar el proceso de autoría.

**Recomendación que se sigue de lo anterior:** no empezar por plataforma. Empezar por **un dominio
acotado** —los productos de Vida Individual, que ya están mapeados— con la matriz existente
promovida a fuente, un dueño nombrado, una cadencia declarada, y **medición propia antes/después**
del tiempo de actualización. Es la misma disciplina que el proyecto ya aplica: no importar tamaños
de efecto de catálogo, medir en la propia población.

### 10.4 Por qué esto es del copiloto y no solo del negocio

Si la matriz existe y es canónica, **la base de conocimiento de AIDA deja de ser un problema
recurrente**: se deriva de la matriz y se regenera con cada cambio, en vez de volver a ensuciarse
cada vez que alguien sube un PPT nuevo. Sin eso, cualquier limpieza que haga F2 **tiene fecha de
vencimiento** — la carpeta se vuelve a desordenar porque nada impide que se desordene.

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
