# Diagnóstico del Copiloto AI del asesor de Vida (RIMAC) — proyecto asociado a Back to Basics

> Node. Fuente de verdad de este tema: **estado, diagnóstico y decisiones del workstream del
> Copiloto AI** que usa el asesor de venta de productos de Vida. Es un proyecto **asociado a**
> Back to Basics, no una sección suya: `[[proyecto-back-to-basics-ffvv-vida]]` sigue siendo la
> fuente de verdad del modelo de venta; este node lo es de la herramienta.
> Capa de **estado interno**. La capa de **evidencia externa** sobre cómo almacenar el
> conocimiento vive en `[[arquitectura-conocimiento-agentes-copilot]]`.
>
> Fecha de elaboración: 2026-08-14 · Última actualización: 2026-08-20 · Versión: v2.3
> (v2.3: **§19 — entrevista con Radille, PO de AIDA.** La entrada de mayor valor del proyecto.
> ✅ **P4, P5, P13 y P14 RESUELTAS.** El objetivo declarado es **uno** —consolidar información y
> reducir tiempo de búsqueda—, no tres. ⭐⭐⭐ **El uso de AIDA está en la variable del asesor**:
> la inferencia de que la adopción no mide utilidad pasa a ser hecho. ⭐⭐⭐ **Es RAG puro** — el
> modelo no genera data, lee SharePoint y cita: el debate de reentrenar queda cerrado por la PO.
> ⭐⭐ **El feedback negativo ya está trazado a documentación desactualizada o incompleta** (capa A).
> ⭐⭐⭐ **Hay un canal barato ya abierto** (Jaime, mesas de los jueves) y 4 de los 6 arreglos caen
> ahí. ⛔ **No hay roadmap de AIDA**; los cambios entran por solicitud del negocio + captura de
> valor, y la capacidad ES presupuesto. ⛔⛔ **Contradicción abierta: la base vive en SharePoint**
> (Microsoft) aunque el motor sea Google — P15 se precisa. ⚠️ Los 5 subagentes del autorreporte
> **no fueron confirmados** por la PO. Abre P16 a P19.)
> (v2.2: **§18 — la reunión con la jefatura.** ⭐ **P9 RESUELTA: AIDA no corre sobre Copilot,
> corre sobre Google** — los límites numéricos de Copilot quedan **descartados**, no suspendidos.
> ⛔ **No hay sandbox de AIDA** (confirmado por el equipo de la herramienta): ninguna
> funcionalidad nueva se puede testear en AIDA, lo que convierte a los prototipos en el único
> banco de pruebas disponible. **El frente de entrenamiento queda deliberadamente fuera de la
> fase 1** por decisión de Alejo — §17 se reencuadra como expediente para cuando se decida, no
> como propuesta activa. Registra las **3 funciones declaradas de AIDA**, la **estrategia
> política de la presentación** (no confrontar a la PO: contrastar la herramienta contra su
> propia declaración), los **6 fixes** de la fase 1 y la **metodología de jueces por área**.)
> (v2.1: **§17 — la capacidad de entrenamiento y el bucle de casuística.** Behavioral Design
> **ya construyó 2 prototipos**, uno de práctica agéntica de objeciones sobre Copilot con
> puntaje, reporte a jefatura y retroalimentación a AIDA — la Fase 4 deja de ser *prototipar*
> y pasa a ser *evaluar lo que ya existe*. Aclara el proceso de captura de casuística (AIDA
> captura las mejores respuestas durante el entrenamiento) y marca sus **dos diferencias con
> el mecanismo validado de F-476** —práctica vs. conversación real, y puntaje propio vs.
> desenlace real— con el arreglo: **separar la captura de la etiqueta**. ⚠️ Advierte que el
> **reporte individual a jefatura puede invertir el signo** (F-495) y contaminar el corpus que
> se quiere construir. Acota la promesa del entrenamiento con F-496/F-497/F-498. Abre **P11**
> (cuál es el segundo prototipo) y **P12** (¿el prototipo reemplaza a Sales Coach?).)
> (v2.0: §16 fija la **estructura definitiva del Release 1 en tres etapas** —diagnóstico de la
> herramienta · intervención · testeo—, que manda sobre cualquier descripción anterior. Agrega la
> **velocidad** como segundo objetivo (y su medición en la Etapa 1), y nombra el "full con puntos de
> corte" como **serie temporal interrumpida**, con el hallazgo de que su serie de control ya existe
> gratis: los ramos que no reciben la intervención. Abre **P10** — "el modelo SHUNK", sin
> identificar.)
> (v1.9: §15 — integra el research *"La biblioteca de AIDA"* de Felipe y produce el **Release 1**
> (`_outputs/release-1-base-conocimiento-aida.md`). Aporta la cuantificación que faltaba, la
> respuesta con evidencia a reentrenar-vs-ordenar, y el argumento de que **ordenar el repositorio es
> lo que hace cumplible la regla que AIDA ya tiene** — tercera lectura de la prueba C8. Este node le
> aporta el hueco de su plan: la copia autoritativa está mal, así que el Release 1 abre resolviendo
> el catálogo.)
> (v1.8: §14 — **evaluación del Playbook del Asesor**, recibido de Alejo y persistido en
> `research/_fuentes_internas/`. Hallazgo central: **la fuente canónica contiene las
> contradicciones que debía resolver** — duplica Vida Contigo/VAG, omite VFP y usa el nombre
> desactualizado "Flexivida". Eso **corrige H3 de §11**: AIDA probablemente reproduce fielmente el
> playbook en vez de estar anclada a 2022 por su cuenta. Confirma P8 —el modelo no contiene
> parámetros de producto, los referencia— y de ahí sale una predicción falsable sobre B2-B4.
> Formato: 100.173 caracteres y 29 tablas, pero **partir por bloque resuelve el techo casi solo**.)
> (v1.7: §13 — **trabajo de campo con asesores**, a propuesta de Alejo. Dos correcciones de fondo:
> el campo **alimenta el banco de preguntas del protocolo, no lo sigue** (el banco actual es
> sintético, deducido de la matriz), y hay que preguntar por **incidentes concretos, no por
> opiniones** — F-488 (técnica del incidente crítico) sobre la base de F-257, que documenta ~39
> puntos de brecha entre percepción y desempeño real con herramientas de IA. Nombra además el hueco
> que ninguna telemetría cubre —**qué dejaron de preguntar**— y la deuda de credibilidad con
> asesores ya consultados dos veces.)
> (v1.6: §12 — **diseño de validación de los fixes**, a propuesta de Alejo. Separa **dos
> experimentos** que la propuesta unía: la re-corrida del banco de preguntas contra la base
> arreglada —que no necesita asesores y es la **compuerta**— y el piloto de desempeño con asesores.
> Aplica sin investigación nueva las estrategias de testeo que el repo ya tenía en
> `modelo-salud-ia-farmacias-peru` §4, con sus controversias declaradas. Estratificación por
> antigüedad **obligatoria**, y la sustitución por ChatGPT/Gemini como métrica conductual.)
> (v1.5: §11 — primera corrida de **auto-interrogación de AIDA**. Cinco hallazgos: AIDA es
> **multi-ramo, no de Vida** (1 de 5 subagentes); la arquitectura de ruteo que §8 recomendaba **ya
> existe**, así que falta medirla, no construirla; los productos que declara **no coinciden con el
> portafolio vigente** y apuntan a material de 2022; ⚠️ **`transfer_to_agent` es de Google ADK, no
> de Copilot Studio** — puede invalidar los límites técnicos asumidos (nueva P9, prioridad #1); y
> `SalesCoachAgent` contradice el mapa de frentes. Agrega la **capa D · Ruteo** a la taxonomía de
> §3. Instrumento en `_outputs/protocolo-interrogacion-aida-vida.md`.)
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

**P10 — ¿Qué es "el modelo SHUNK"?** Alejo lo nombra (2026-08-14) como el marco de la evaluación
con LLM de la Etapa 1, en dimensiones de "usabilidad, error, etc.". **No se pudo identificar y no se
aplicó por aproximación** — misma regla que evitó el error con "Shang"/Zheng en la referencia de
juez LLM. Candidatos buscados y descartados: **Shackel (1991)**, definición operacional canónica de
usabilidad (efectividad, aprendibilidad, flexibilidad, actitud), que no centra el error; y las
escalas de usabilidad de chatbots **BUS-11 / BUS-15 / CUQ**, de las cuales **CUQ sí tiene un factor
específico de manejo de errores** y ya está registrada como F-149. La Etapa 1 se construye mientras
tanto sobre los instrumentos ya verificados del proyecto.

**⭐ P9 (nueva, prioridad #1) — ¿Sobre qué framework corre AIDA realmente?** `transfer_to_agent`
apunta a Google ADK, no a Copilot Studio. Determina si los límites técnicos documentados aplican o
si esa parte del diagnóstico se rehace. **Solo se resuelve con TI o el equipo dueño.**

**P8 — ✅ RESUELTA (Alejo, 2026-08-14):** el modelo de venta es canónico para el conocimiento de
venta y **referencia** una fuente canónica de parámetros de producto, sin contenerla.

**P6 — ¿Los tres agentes comparten base de conocimiento o cada uno tiene la suya?** Decide si el
mapa de §8.1 describe la arquitectura actual o la contradice. Si comparten base, el problema de
recuperación es peor de lo estimado.

**P7 — ¿Quién es dueño de cada agente?** Si AIDA, el agente de suscripción y Sales Coach dependen de
equipos distintos, "una sola puerta de entrada" es un problema de gobierno antes que de tecnología.

**✅ P4 — RESUELTA (v2.3). Existe telemetría y ya se solicitó.** Los logs contienen **todas las
preguntas que le llegan a AIDA, cómo responde, y el feedback positivo/negativo**. Es exactamente el
corpus de fallas que §4 describía como fuente ideal. Ver §19.5.

**✅ P5 — RESUELTA (v2.3). Existe línea base y es sólida.** AIDA Sales está desplegada desde **mayo de
2025**; hay dashboards con cantidad de consultas, promedio diario, ratio de feedback y margen de
error. Volumen actual estable: **>30.000 consultas mensuales**, **3 a 3,5 consultas diarias** por
asesor. Más de un año de serie temporal. Ver §19.4.

**P11 — ¿Cuál es el segundo prototipo de Behavioral Design?** (abierta en v2.1) El brief dice "2
prototipos" y describe uno —la práctica agéntica de objeciones sobre Copilot—. Se asume que el otro
es el prototipo sobre Claude del Plan Piloto, **pero no está confirmado**. Si es un tercer artefacto,
hay un inventario incompleto de lo que el equipo ya construyó. Ver §17.1.

**P12 — ¿El prototipo de práctica reemplaza a Sales Coach, lo reemplaza en parte, o es un cuarto
agente?** (abierta en v2.1) Si AIDA adquiere capacidad de entrenamiento hay **dos agentes que
enseñan**. Las tres respuestas son defendibles; **no decidirlo no lo es** — por omisión quedan dos
agentes enseñando modelos de venta que nadie garantizó que coincidan. Ver §17.6.

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

## 11. Auto-interrogación de AIDA — primera corrida (v1.5)

**Frente de diagnóstico nuevo, abierto por Alejo:** preguntarle a la herramienta por sí misma. El
instrumento vive en `_outputs/protocolo-interrogacion-aida-vida.md`; aquí quedan los hallazgos.

⚠️ **Estatus epistémico de todo lo que sigue:** proviene de **un autorreporte de AIDA**, no de
inspección de configuración. Un modelo al que se le pregunta por su arquitectura produce una
narración plausible —leyendo su prompt de sistema, o reconstruyendo un patrón genérico— y **no
distingue entre ambas al responder**. Son hipótesis a triangular, **no documentación**.

**Lo que AIDA declara ser:** "AIDA FFVV", un Coordinador Principal con **cinco subagentes** —
`SaludAgent`, `VehicularAgent`, `VidaFinancieroAgent`, `GeneralOpsAgent`, `SalesCoachAgent` —, tres
lógicas (clasificación y enrutamiento; modo coach con contexto; reglas operativas estrictas que le
prohíben responder de memoria en temas técnicos) y una función, `transfer_to_agent`.

**Cinco hallazgos, dos de los cuales cambian el diagnóstico:**

**H1 · AIDA no es el copiloto del asesor de Vida: es multi-ramo.** Solo 1 de 5 subagentes es Vida.
⭐ Esto convierte **el error de ruteo entre ramos en candidato principal** de la queja "no da la
información adecuada": una respuesta correcta del ramo equivocado es, para el asesor,
indistinguible de un error de conocimiento. Y el presupuesto de recuperación (≤300 páginas, §3 del
node de arquitectura) se reparte entre cuatro dominios — Vida recibe una fracción.
**Corrección de encuadre:** este node venía tratando a AIDA como herramienta de Vida. No lo es. Es
una herramienta corporativa **que el asesor de Vida usa**.

**H2 · La arquitectura que §8 recomendaba ya existe.** Coordinador + subagentes por dominio con
fuentes separadas es exactamente el patrón de F-479/F-480. ⭐ **Cambia la conclusión de §8: el
arreglo no es construir el ruteo — el ruteo existe, y lo que falta es medir si acierta.**

**H3 · Los productos que AIDA nombra no coinciden con el portafolio vigente.** Declara "Flexivida,
Inversión Global, Renta Garantizada, UltraCash"; `[[matriz-productos-vida-rimac]]` (fichas vigentes
desde 01/01/2025) tiene **VFP, Plan Vida Flexible, Vida Contigo/Vida Ahorro Garantizado y Vida
Temporal Total**. ⭐ **"Flexivida" es el nombre del PPT de marzo 2022**, no el de la ficha vigente —
huella de que el conocimiento de Vida podría estar anclado a material de 2022. Los otros tres no
aparecen en Vida Individual, y tres productos vigentes no son nombrados.
Dos lecturas, ambas verificables con una pregunta (A3 del protocolo): **desfase de vigencia** o
**desalineación de alcance** (el agente cubre la línea *Vida e Inversiones*, no *Vida Individual
FFVV*). ⚠️ Descuento: AIDA dijo "productos **como**…" — son ejemplos, no catálogo.
> ⚠️ **CORRECCIÓN (v1.8, tras leer el Playbook — ver §14.1).** La lectura de "desfase de vigencia"
> era demasiado dura con AIDA. **El propio Playbook del Asesor, que es la fuente canónica, también
> dice "Flexivida"** — no "Plan Vida Flexible". Es más probable que **AIDA esté reproduciendo
> fielmente el playbook** que que esté anclada a un PPT de 2022 por su cuenta. El desfase existe,
> pero está **aguas arriba**, en la fuente. Mueve la culpa del agente al catálogo.

**H4 · `transfer_to_agent` es la función de delegación de Google ADK, no de Copilot Studio.**
⚠️ **Puede invalidar parte del trabajo previo.** Si AIDA no corre sobre Copilot Studio, **los
límites técnicos del node de arquitectura (36.000 caracteres, 7 MB/200 MB, tablas, PDF imagen) no
aplican** y esa parte del diagnóstico se rehace. Las otras dos lecturas: que el autorreporte esté
confabulado, o que sea una construcción mixta. **No se resuelve preguntándole otra vez a AIDA.**
👉 **Pasa a ser la pregunta técnica #1 del proyecto (P9), por encima del licenciamiento (P2).**

**H5 · `SalesCoachAgent` vive dentro de AIDA**, pero §2.1 lista Sales Coach como frente separado de
entrenamiento inicial. O son dos cosas homónimas, o el mapa de 6 frentes se corrige. Sin resolver.

### 11.1 Lo que esto agrega a la taxonomía de §3

Los hallazgos obligan a una capa que la taxonomía de tres no tenía:

| Capa | Qué falla | Cómo se ve | Cómo se confirma |
|---|---|---|---|
| **A · Conocimiento** | El dato no está o está mal | Inventa, no encuentra | Auditoría + RAGAS |
| **B · Instrucciones** | Tiene el dato, se comporta mal | Correcto pero inútil | Mismo dato, otra instrucción |
| **C · Plataforma** | Techos duros | Ignora documentos | Verificación técnica |
| **⭐ D · Ruteo** *(nueva)* | **Delega al agente equivocado** | **Respuesta correcta del ramo equivocado** — el asesor la lee como dato falso | Bloque C del protocolo: preguntas con términos que existen en varios ramos |

**Por qué importa que sea una capa aparte:** una falla de ruteo **se ve idéntica a una falla de
conocimiento** desde afuera, pero se arregla en un lugar completamente distinto — el clasificador,
no la base. Sin separarla, un proyecto de limpieza de contenido podría no mover la aguja en nada.

---

## 12. Diseño de validación de los fixes (v1.6)

**Propuesta de Alejo (2026-08-14):** una vez logrado el primer set de fixes —documentación en
formato adecuado, cuerpo de conocimiento unificado y no contradictorio del modelo de venta, más lo
que salga de la exploración— correr **un piloto que compare la performance de asesores con la
herramienta antigua y con la nueva.**

La propuesta es correcta en dirección. Lo que sigue son las decisiones de diseño que la hacen
interpretable — y una separación que conviene hacer antes de comprometer asesores.

⭐ **Nota de método:** esta sección **no requirió investigación nueva**. El repositorio ya tenía la
evidencia de estrategias de testeo levantada para un caso análogo (IA desplegada a profesionales en
Perú) en `[[modelo-salud-ia-farmacias-peru]]` §4 — E1 silent trial, E2 híbrido de Curran, E3
stepped-wedge —, con sus revisiones profundas y sus controversias ya documentadas. Se aplica tal
cual, incluidas las advertencias.

### 12.1 Son dos experimentos, no uno

Confundirlos es el error más caro disponible aquí, porque hace gastar el capital político de la
fuerza de venta en una prueba que podía haberse hecho sin ella.

| | **Experimento 1 · La herramienta** | **Experimento 2 · El asesor** |
|---|---|---|
| **Pregunta** | ¿Los fixes mejoraron las respuestas? | ¿La mejor herramienta cambia el desempeño? |
| **Necesita asesores** | **No** | Sí |
| **Duración** | Días | Semanas o meses |
| **Ruido** | Muy bajo — banco de preguntas fijo | Alto — estacionalidad, campañas, cartera, ánimo |
| **Qué aísla** | El efecto del fix, limpio | El efecto del fix **más** todo lo demás |
| **Costo** | Bajo | Alto, y consume goodwill de la FFVV |

**El Experimento 1 es la compuerta del 2.** Si la calidad de respuesta no se mueve en el mismo
banco de preguntas, **no hay nada que testear con asesores** — y se evita quemar la disposición de
la fuerza de venta en un piloto que nunca iba a mostrar nada.

### 12.2 Experimento 1 — la re-corrida (silent trial adaptado)

Es E1 de `[[modelo-salud-ia-farmacias-peru]]` §4 trasladado: medir el sistema **sin que su salida
influya en ninguna decisión real**.

- **Mismo banco de preguntas, mismo juez, misma rúbrica, misma calibración** que la línea base
  (`_outputs/protocolo-interrogacion-aida-vida.md`).
- **Comparación pareada pregunta por pregunta** (antes → después). Esto da **alta potencia
  estadística con pocos ítems**, porque cada pregunta es su propio control — no hay varianza entre
  sujetos que absorber.
- **Aísla el mecanismo:** como el banco está fijo, un cambio en el puntaje es atribuible al fix y no
  a variación de asesores o de mercado.
- ⚠️ **Advertencia heredada de la revisión profunda de F-56/F-57:** un silent trial **no es un
  casillero que se marca una vez** — vale mientras la población de uso no cambie. El caso citado
  ahí (un modelo que colapsó de AUC 0,90 a 0,50 por *distribution shift*) aplica: si después se
  amplía a otro ramo, otra región o cambia el mix de consultas, **hay que repetirlo**.

**Regla de decisión sugerida, a declarar antes de correrlo:** los fixes pasan si la exactitud (D1)
y la vigencia (D3) suben de forma clara **y** las fallas marcadas con riesgo regulatorio bajan a
cero. Sin eso, no se avanza al Experimento 2 — se itera el contenido.

### 12.3 Experimento 2 — cinco decisiones que hay que tomar antes

**1 · ¿Se pueden tener dos versiones a la vez?** Pregunta técnica, y es la primera. Si la base de
conocimiento es infraestructura compartida, **puede no ser posible que un grupo use la vieja y otro
la nueva simultáneamente**. Determina todo el diseño: si no se puede, el paralelo queda descartado
y hay que ir a escalonado o a antes/después. **Verificar con TI antes de diseñar nada más.**

**2 · Contaminación entre asesores.** Los asesores se hablan, se pasan capturas y se recomiendan
herramientas. Aleatorizar individuos dentro de una misma oficina **filtra**: el grupo control se
entera y, si puede, la usa. → **Aleatorizar por cluster** (equipo, oficina, territorio), no por
persona.

**3 · La conversión no sirve como desenlace primario.** Ya está declarado por el propio equipo en
el Plan Piloto: *el ciclo de venta de Vida excede el plazo del piloto; un movimiento en conversión
sería direccional, no concluyente*. Diseñar el piloto con conversión como métrica principal
garantiza un resultado nulo o ruidoso. Ver 12.5.

**4 · ⭐ Estratificar por antigüedad es obligatorio, no un análisis posterior.** Dos fuentes
independientes del propio repositorio convergen:
- **F-476** (QJE 2025): el efecto de un copiloto es **+34% en novatos y prácticamente nulo en
  expertos**. Un promedio mezcla dos poblaciones distintas.
- **F-55** (Cully et al. 2017, vía revisión profunda del node de salud): el caso de referencia de
  diseño híbrido que el proyecto ya cita tuvo **resultados desiguales entre subgrupos** — funcionó
  en uno y no en el otro.

**Implicación dura: un piloto sin estratificar puede reportar "sin efecto" cuando existe un efecto
grande en el grupo que más importa.** La estratificación va en el diseño y en el análisis
preespecificado, no se descubre después.

**5 · Efecto novedad.** Una herramienta nueva genera entusiasmo que se confunde con utilidad. El
Plan Piloto ya lo nombraba: interesa si el asesor *"sigue volviendo después de la novedad
inicial"*. → **Medir uso sostenido a partir de la semana 3**, no el pico inicial.

### 12.4 Qué diseño recomendar — y su controversia, declarada

**Recomendación: escalonado por clusters (stepped-wedge)** — los equipos pasan de la versión
antigua a la nueva en orden aleatorio hasta que todos la reciben.

Por qué encaja: resuelve la contaminación (el cluster entero cambia junto), no le niega
permanentemente la mejora a nadie —lo que importa cuando la herramienta vieja está reconocidamente
fallada—, y es compatible con un despliegue gradual, que es como esto va a ocurrir de todos modos.

⚠️ **Y ahora la advertencia que el repositorio ya tiene documentada, y que hay que declarar en el
protocolo en vez de omitirla:** el stepped-wedge **no es una elección libre de controversia**.
Hemming & Taljaard (F-58/F-59, revisión profunda 2026-08-12) sostienen que está en **mayor riesgo
de sesgo que un cluster-RCT paralelo** y que su supuesta ventaja ética **no es real**, porque la
implementación secuencial también cabe en un paralelo clásico; hay réplica académica activa. Además
**confunde por tiempo** — el control siempre se mide antes cronológicamente — y exige **ajuste por
tendencia temporal**, algo especialmente sensible en venta de seguros, donde hay estacionalidad y
campañas.

**Consecuencia práctica:** si se elige stepped-wedge, hay que **documentar explícitamente por qué se
prefiere sobre un paralelo** (como exige CONSORT), no presentarlo como la opción obviamente
superior. Si TI confirma que se pueden mantener dos instancias y hay suficientes equipos, **un
cluster-RCT paralelo es metodológicamente más limpio.**

### 12.5 Qué medir — tres niveles que no se mezclan

| Nivel | Métrica | Ventana |
|---|---|---|
| **1 · Herramienta** | Exactitud, vigencia, fidelidad y fallas con riesgo regulatorio, sobre el banco fijo | Inmediata (Exp. 1) |
| **2 · Conducta del asesor** | Tasa de uso sostenida (sem. 3+) · consultas resueltas sin escalar · conversaciones que respetan la secuencia del modelo (shadowing) · carga cognitiva autorreportada · **uso de ChatGPT/Gemini como sustituto** | 4-8 semanas |
| **3 · Comercial** | Propuestas enviadas y agendamiento como adelantados; conversión, prima y persistencia como rezagados | Fuera de ventana — **direccional, nunca concluyente** |

⭐ **La métrica más elegante del conjunto es la sustitución por IA externa.** Hoy está documentado
que los asesores usan ChatGPT y Gemini **para cubrir los huecos de AIDA**. Eso la convierte en un
indicador conductual, no declarativo, directamente derivado del diagnóstico: **si los fixes
funcionan, el uso de IA externa debería caer.** No requiere que el asesor evalúe nada — solo que se
le pregunte con qué frecuencia recurrió a una IA de afuera esta semana. Y tiene una lectura de
riesgo adicional que ya conviene al negocio: mide exposición de información por herramientas no
gobernadas.

### 12.6 Preregistrar antes de correr

Declarar **por escrito y antes de empezar**: hipótesis, desenlace primario, estratos (antigüedad
como mínimo), regla de decisión y análisis planeado.

No es formalismo académico: es la defensa contra el sesgo que este proyecto documentó seis veces en
otros contextos — **decidir después de ver los datos qué métrica contaba**. Y es coherente con el
criterio que el repositorio ya aplica al valorar evidencia externa: el único RCT preregistrado del
node de tendencias es también la evidencia que más peso recibe ahí.

### 12.7 Lo que este piloto no puede probar

- **No prueba que el modelo de venta funcione.** Prueba que la herramienta que lo vehicula mejoró.
  Son cosas distintas y confundirlas atribuiría al modelo un mérito o un fracaso de la herramienta.
- **No aísla cuál fix funcionó.** Los fixes van en paquete, así que el Experimento 2 responde
  "¿sirvió el paquete?", que es la pregunta correcta para decidir inversión. El **por qué** lo
  responde el Experimento 1, ítem por ítem.
- **No resuelve la contradicción aguas arriba** (§9). Si el modelo de venta no es efectivamente
  canónico para todos los frentes, la base volverá a divergir y el efecto medido se degradará con el
  tiempo. **El piloto mide el fix, no lo sostiene.**

---

## 13. Trabajo de campo con asesores (v1.7)

**Propuesta de Alejo (2026-08-14):** incorporar entrevistas y shadowing con asesores dentro de la
exploración, dado que quedan preguntas que solo ellos pueden responder.

Correcto, y con dos precisiones que cambian cuándo se hace y cómo se pregunta.

### 13.1 Criterio: reservar el campo para lo que nada más puede responder

El asesor es un recurso escaso y ya fue consultado dos veces (encuesta de 19, taller de 36). Todo lo
que pueda levantarse de telemetría o de la base **no debe preguntársele** — es el principio que el
propio Plan Piloto declara: *la carga de recolección es de la CoE, no del asesor*.

Seis cosas que **solo el campo entrega**:

1. **Qué le preguntan a ChatGPT/Gemini que no le preguntan a AIDA.** Es el mapa del hueco sin
   auditar un solo archivo.
2. ⭐ **Qué dejaron de preguntar.** El hallazgo más importante y el más invisible: después de
   suficientes malas respuestas, la gente deja de hacer categorías enteras de pregunta. **La
   telemetría tiene un problema de supervivencia — no puede mostrar una pregunta que nunca se
   hizo.** Ninguna métrica de logs detecta esto; solo se detecta preguntando.
3. **Qué hacen cuando sospechan que la respuesta está mal.** ¿Verifican? ¿Con quién? ¿La usan igual?
   Es conducta de rodeo, invisible en logs.
4. **En qué momento del flujo consultan y por qué ahí.** Los timestamps dan la hora, no la
   situación.
5. **Qué contradicciones han vivido en carne propia.** El asesor es el punto donde todas las
   instanciaciones del modelo se encuentran (§9) — **sabe dónde están las contradicciones porque las
   sufre.** Es la fuente más eficiente para F2b.
6. **La carga emocional.** El mandato del copiloto la nombra explícitamente (§1). No hay telemetría
   que la mida.

### 13.2 ⭐ Corrección de secuencia: el campo alimenta el protocolo, no lo sigue

**Esto corrige el instrumento tal como está hoy.** El banco de preguntas del Bloque B
(`_outputs/protocolo-interrogacion-aida-vida.md`) lo construí **deduciéndolo de la matriz de
productos** — son preguntas verificables, pero **sintéticas**: son las que *deberían* hacerse, no
las que los asesores *hacen*.

Un banco sintético mide lo que a nosotros nos parece importante. Un banco derivado del campo mide lo
que realmente rompe la venta. **El trabajo de campo va antes o en paralelo a la corrida del
protocolo, no después** — y su salida principal es el banco de preguntas real.

**Consecuencia práctica:** el Bloque B queda marcado como provisional. Después del campo se
reemplaza o se amplía con las 20-30 preguntas más frecuentes y más costosas que reporten los
asesores, conservando las de control (producto inexistente, duplicado de tres nombres, cifra con
riesgo regulatorio) porque esas sí tienen que ser diseñadas.

### 13.3 Cómo preguntar: incidentes, no opiniones

⚠️ **Preguntar "¿te ayuda AIDA?" produce una evaluación, y las evaluaciones autorreportadas de
herramientas de IA están sistemáticamente desalineadas de la conducta real.** El proyecto ya tiene
la evidencia dura de eso: **F-257** (METR) — desarrolladores fueron **19% más lentos** con IA
mientras estimaban ser **20% más rápidos**: una brecha de ~39 puntos entre percepción y desempeño.

La corrección es metodológica y tiene nombre: **técnica del incidente crítico** (Flanagan 1954,
**F-488**). Se pide **el último caso concreto en que ocurrió**, con contexto, conducta y
consecuencia. El asesor recuerda lo que pasó en vez de juzgar la herramienta, y eso esquiva la
brecha.

| ❌ En vez de preguntar | ✅ Preguntar |
|---|---|
| ¿AIDA te da buena información? | Cuéntame **la última vez** que le preguntaste algo y la respuesta no te sirvió. ¿Qué preguntaste? ¿Qué te dijo? ¿Qué hiciste después? |
| ¿Confías en AIDA? | ¿Cuándo fue **la última vez** que verificaste una respuesta suya por otro lado? ¿Con qué la verificaste? |
| ¿Usas ChatGPT? | ¿Cuál fue **lo último** que le preguntaste a ChatGPT o Gemini para el trabajo? ¿Por qué a esa y no a AIDA? |
| ¿Te falta información? | ¿Hay algo que **antes le preguntabas y ya no**? ¿Qué pasó? |
| ¿Encuentras información contradictoria? | Cuéntame **la última vez** que dos fuentes de RIMAC te dijeron cosas distintas. ¿Cuáles eran? ¿A cuál le hiciste caso? |

La última fila es doble: produce insumo para F2b **y** revela el criterio informal que el asesor usa
para arbitrar — que hoy es la única regla de resolución de contradicciones que existe.

### 13.4 A quién — el muestreo importa más que el número

De la encuesta ya se conoce la variación: AIDA usada "siempre" por 7/19, **"nunca" por 1/19**.

- ⭐ **El que no la usa nunca es la entrevista más informativa que existe.** Decidió que no valía la
  pena y puede decir exactamente por qué. Una sola conversación con esa persona probablemente rinde
  más que cinco con usuarios satisfechos.
- **Usuarios intensivos** (del grupo de 7): qué sí les funciona — hay que saber qué **no** romper.
- **Por antigüedad**, obligatorio: novatos vs. expertos usan la herramienta distinto y el efecto de
  un copiloto se concentra en los primeros (F-476). Sin este corte, el campo describe un asesor
  promedio que no existe.
- **Lima y provincias**: el Plan Piloto ya usaba esa proporción (6 Lima, 2 Arequipa, 2
  Cuzco/Trujillo) y provincia se cubría por videollamada.

**Volumen sugerido:** 8-12 entrevistas de incidente crítico (~45 min) + shadowing de 4-6 asesores.
Lo suficiente para saturar los modos de falla, no para estimar frecuencias — la frecuencia sale de
la telemetría y del protocolo, no del campo.

### 13.5 Shadowing: qué mirar

El diseño **ya existe** en el Plan Piloto y se reutiliza: shadowing por cobertura (todos al menos
una vez, provincia por videollamada), **bitácora post-conversación de 3 preguntas / 30 segundos por
WhatsApp**, y cierres de semana reflexivos de 10 minutos.

Qué observar específicamente para este diagnóstico, que la entrevista no da:

- **El momento exacto de la consulta** — ¿antes, durante o después de hablar con el cliente?
- **El salto entre herramientas** — la secuencia real: AIDA → Salesforce → WhatsApp → ChatGPT →
  material físico. Ahí está la carga que el copiloto debería absorber, y se ve, no se recuerda.
- **Qué hace con la respuesta** — ¿la copia, la reformula, la descarta, la verifica?
- **Cuánto tarda** en obtener algo usable, y cuántos intentos hace.
- **Qué no consulta** aunque le habría servido — visible solo en observación, y conecta con 13.1.2.

### 13.6 Dos riesgos que hay que gestionar

**1 · Ser observado cambia la conducta.** Un asesor acompañado va a usar AIDA más de lo habitual,
para verse alineado. **El shadowing sobreestima el uso.** Mitigación: triangular con telemetría,
decir explícitamente que no se evalúa a la persona sino a la herramienta, y no compartir los
registros individuales con jefaturas.

**2 · ⭐ Deuda de credibilidad — el riesgo relacional, y es el más serio.** Los asesores **ya
opinaron dos veces**: 19 respondieron una encuesta y 30 asistieron a un taller donde pidieron
mejoras concretas. Si se les vuelve a preguntar y no ven que lo anterior sirvió de algo, **el costo
no es que respondan mal: es que dejen de responder**, y eso cierra la única fuente de estas seis
preguntas.

**Obligación que se sigue de esto:** abrir cada entrevista contando **qué produjo lo que dijeron
antes** — que su queja sobre AIDA está documentada, que originó este proyecto, y qué se está
haciendo. No es cortesía: es la condición para que la segunda ronda tenga la misma calidad que la
primera.

---

## 14. Evaluación del Playbook del Asesor como fuente canónica (v1.8)

**Documento recibido de Alejo el 2026-08-14** (`research/_fuentes_internas/Playbook_del_Asesor.md`,
100.173 caracteres, 1.743 líneas). Es el **modelo de venta Vida** — la fuente canónica declarada en
§9.2. Primera evaluación real contra todo lo construido en este node.

**Veredicto en una línea:** el contenido es sólido y la estructura es mejor de lo esperado, pero
**el documento que debe resolver las contradicciones contiene contradicciones**, y no es consumible
por un agente en su forma actual.

### 14.1 ⭐ La contradicción está dentro de la fuente canónica

Contraste del portafolio del Bloque 2 contra `[[matriz-productos-vida-rimac]]` (derivada de fichas
comerciales **vigentes desde 01/01/2025**):

| Playbook (Bloque 2) | Matriz del repo | Estado |
|---|---|---|
| Temporal Total | Vida Temporal Total | ✅ Coincide |
| **Vida Contigo** | Vida Contigo = **VAG** = Vida Ahorro con Devolución — **un solo producto** | ⚠️ |
| **VAG** *(fila aparte, descripción distinta)* | ...es el mismo producto que Vida Contigo | 🔴 **El playbook lo trata como dos productos**, con descripciones que los diferencian ("un monto que también queda disponible" vs. "montos y plazos mayores") |
| **Flexivida** | Nombre vigente: **Plan Vida Flexible**; "Flexivida" es el nombre del **PPT de marzo 2022** | 🔴 Nombre desactualizado |
| VCD digital | "Pendiente — **no confirmado** como producto real distinto" | ⚠️ |
| Endosable digital | "Pendiente — **no confirmado**" | ⚠️ |
| *(ausente)* | **Vida Futuro Protegido (VFP)**, con 4 variantes (Plan 35/65, Plus 35/65) | 🔴 **Un producto vigente que el playbook no menciona** |

Dos hallazgos graves: **el playbook duplica un producto** (Vida Contigo / VAG) y **omite otro**
(VFP), que la matriz v1.2 confirma explícitamente como vigente.

⭐⭐ **Y esto obliga a corregir H3 de §11.** Ahí se interpretó que AIDA usara "Flexivida" como huella
de que su base estaba anclada a material de 2022. **Es más probable que AIDA esté reproduciendo
fielmente el playbook**, que usa ese mismo nombre. Es decir: **AIDA puede no estar equivocada — puede
estar siendo exacta respecto de una fuente que ya no lo es.**

Eso mueve el diagnóstico un eslabón aguas arriba y es exactamente lo que predecía §9: **la
inconsistencia del agente es la inconsistencia de la organización, reflejada.** Aquí queda
demostrado con nombres de producto concretos, no como hipótesis.

### 14.2 El playbook no contiene los datos que el asesor más consulta

Declarado por el propio documento: *"**Detalle técnico de cada producto (Pendiente)** — coberturas
exactas, exclusiones, tiempos de espera, edades de contratación, qué pasa si el cliente deja de
pagar, y montos/plazos mínimos y máximos… depende del equipo de Producto."*

✅ **Esto confirma P8**: el modelo es canónico para el **conocimiento de venta** y **referencia** una
fuente de producto sin contenerla. La lectura propuesta era correcta y ahora está confirmada por el
documento mismo.

⭐ **Pero produce una predicción falsable y valiosa.** Si la base de Vida de AIDA deriva del
playbook, **no tiene ningún dato de cobertura, exclusión ni carencia** — y las preguntas B2, B3 y B4
del protocolo (suma asegurada mínima de VFP, carencia de Enfermedades Graves, edad máxima de PEI)
**deberían fallar**.

**Los dos resultados posibles son ambos hallazgos:**
- **Si fallan** → confirma que el hueco es de contenido, no de recuperación. Se arregla trayendo la
  matriz de producto, no limpiando formatos.
- **Si AIDA las responde con seguridad** → está tomando datos de producto de **una fuente que no es
  el playbook y que nadie declaró**. Eso es una fuente no gobernada, y es más grave.

**Correr B2-B4 temprano.** Es la prueba más informativa por unidad de esfuerzo que hay disponible
hoy.

### 14.3 Formato: no consumible hoy, pero la conversión es barata

| Criterio (§4 del node de arquitectura) | Estado | Detalle |
|---|---|---|
| ≤36.000 caracteres por archivo | 🔴 **No** | **100.173** — 2,8× el techo |
| Sin tablas | 🔴 **No** | **29 tablas**, varias en el contenido más crítico |
| Estructura por encabezados | 🟢 **Sí** | Jerarquía limpia y profunda (bloques → H2 → H3 → H4/H5) |
| Un documento, un tema | 🟡 Parcial | 5 bloques temáticos bien separados, pero en un solo archivo |
| Sin imágenes | 🟢 **Sí** | Cero |
| Resumen al inicio | 🟡 Parcial | Tiene "Para empezar" y "Estado de esta versión" |
| Formato base | 🟢 **Óptimo** | Ya es markdown |

⭐ **La buena noticia, y es grande: partir por bloque resuelve el techo casi solo.**

| Archivo resultante | Caracteres | ¿Bajo 36k? |
|---|---|---|
| Portada + journey | 5.349 | ✅ |
| Bloque 1 · Quiénes somos | 13.701 | ✅ |
| **Bloque 2 · Qué vendes** | **5.396** | ✅ |
| Bloque 3 · Que te encuentren | 27.063 | ✅ |
| **Bloque 4 · La asesoría** | **34.390** | ⚠️ Al filo — **y crecerá** con lo pendiente. Partir en contacto / conversación / decisión |
| Bloque 5 · Después del sí | 3.838 | ✅ |
| Apéndice | **133** | 🔴 **Documento vacío** — bajo el umbral de indexación (~4 KB) |
| Índice de Confianza Profesional | 7.685 | ✅ (pero ver 14.5) |

**El trabajo real no es reescribir: es partir y des-tabular.** Mucho más barato de lo que el
diagnóstico inicial hacía temer, porque el documento ya nació en markdown y con jerarquía.

⚠️ **Dato incómodo de esa tabla: el Bloque 2 (Qué vendes) es el bloque sustantivo más pequeño —
5.396 caracteres, contra 27.063 de social selling.** El conocimiento de producto, que es lo que se
le pregunta a AIDA, es la parte más delgada del playbook. No es un problema de formato: es de
contenido faltante (14.2).

### 14.4 Las tablas están justo donde más duele

Las 29 tablas no están repartidas parejo. La **"Guía rápida: qué hay detrás de cada objeción"** —
tres columnas: lo que dice el cliente / qué puede haber detrás / estrategia sugerida — es
probablemente **el fragmento más valioso de todo el playbook**: manejo de objeciones es el tema más
pedido (42%) y el cierre el momento de mayor necesidad.

Es exactamente el contenido que un agente debe recuperar bien, **en el formato que peor sobrevive**:
aplanada, la relación entre la frase del cliente y su estrategia se pierde, y quedan tres listas
sueltas.

**Reescritura recomendada** — una entrada por objeción, con encabezado propio:

> `##### Objeción: "Está muy caro"`
> **Qué puede haber detrás:** no tiene puntos de referencia.
> **Estrategias:** Punto de referencia · Tu ingreso es tu mayor activo.
> **Cómo suena:** …

Así cada objeción se vuelve un fragmento autosuficiente y recuperable por sí mismo — que es
justamente lo que el asesor necesita en vivo.

### 14.5 El playbook es dos artefactos en uno

Contiene el **modelo de venta** (normativo, transversal, estable) y además contenido operativo de
otra naturaleza: el **Índice de Confianza Profesional** (autodiagnóstico personal), el **Apéndice
administrativo** (certificación, incentivos, esquema remunerativo) y buena parte del **social
selling** (cómo tomarse la foto, cómo vestirse, qué publicar).

Para un humano eso es útil y está bien reunido. **Para el agente es ruido que compite por el
presupuesto de recuperación** (§3 del node de arquitectura, ≤300 páginas).

Es el mismo principio de "dos artefactos, dos audiencias" que ya aplicaba al material visual —
ahora aplicado al documento canónico: **la derivación hacia la base del agente debe seleccionar, no
solo reformatear.** El autodiagnóstico y el apéndice no deberían entrar.

### 14.6 Ocho vacíos declarados — y uno depende de Alejo

El propio documento lista lo pendiente y de quién depende: detalle técnico de producto y glosario
(Producto), perfil de cliente objetivo (Estrategia de Clientes), gestión de referidos e indicadores
(por definir), certificación, incentivos y esquema remunerativo (por definir), y **estrategia de
contacto inicial CUA — "depende de Alejo"**.

⚠️ **La CUA sigue diciendo `_(Pendiente — Alejo)_` en el documento** (línea 898). Este node ya
advertía en Limitaciones que la "Resolución definitiva" de §6 de
`[[proyecto-back-to-basics-ffvv-vida]]` **no estaba verificada contra el documento fuente**. Queda
verificada: **el documento sigue sin la sección.** Es la tercera confirmación independiente del
mismo hueco (Plan Piloto, revisión directa del playbook, y ahora esta lectura).

**Estos ocho vacíos son el backlog de contenido del agente**, y hay que declararlos como tales: son
las preguntas que AIDA **no puede** responder bien hoy porque la respuesta no existe en ninguna
fuente canónica.

### 14.7 Lo que está bien y no hay que romper

- **El modelo de 4 pasos y el manejo de objeciones son contenido de calidad** — con procedimiento,
  ejemplo dialogado y estrategias codificadas (C.1 Referentes sociales, C.2 Punto de referencia,
  C.3 Proteger lo que ya tienes…). La codificación además ya es compatible con recuperación por
  fragmento.
- **28 fuentes citadas con DOI/enlace**, varias de primer nivel (*Journal of Applied Psychology*,
  *Psychological Science*, *Journal of Business Ethics*). Es un playbook con respaldo, poco común.
  ⚠️ Con una capa más débil que conviene marcar antes de citarla hacia afuera: BrightLocal, Forbes
  Finance Council, AdvisorRankings y Statista son del tipo que este proyecto trata con descuento.
  **Ninguna de las 28 está en el códice** — registrarlas es una tarea aparte, a decidir.
- **La lógica de match motivación ↔ perfil financiero → producto está clara y bien construida**, y
  es exactamente el núcleo generativo que §1.1 de Back to Basics describe.

### 14.8 Qué hacer con esto

1. **Resolver las tres discrepancias de producto (14.1)** con Producto: ¿VAG y Vida Contigo son uno
   o dos? ¿Flexivida o Plan Vida Flexible? ¿Dónde está VFP? **Es trabajo de días y desbloquea todo
   lo demás** — mientras el catálogo canónico esté mal, cualquier base derivada de él hereda el
   error.
2. **Correr B2-B4 del protocolo temprano** (14.2), porque distingue hueco de contenido de fuente no
   gobernada.
3. **Partir por bloque y des-tabular** (14.3, 14.4), empezando por el Bloque 4 — objeciones — que
   es el de mayor demanda.
4. **Definir qué NO entra a la base del agente** (14.5).
5. **Declarar los ocho vacíos como backlog de contenido** (14.6), y cerrar la CUA.

---

## 15. Integración del research de Felipe y el Release 1 (v1.9)

**Documento recibido de Alejo el 2026-08-14:** *"La biblioteca de AIDA"* (Felipe, practicante de
Behavioral Design), persistido en `research/_fuentes_internas/`. Research de mercado sobre por qué
el orden del repositorio decide la calidad del agente. **Es el trabajo externo de mayor calidad que
ha entrado a este proyecto.**

**Integración completa en `_outputs/release-1-base-conocimiento-aida.md`.** Aquí solo lo que cambia
este node.

**Lo que aporta y este node no tenía:**
- ⭐ **La cuantificación que el node de arquitectura declaraba inexistente** (F-490 a F-492) —
  corregido allí en su v1.2.
- ⭐ **La respuesta con evidencia a reentrenar-vs-ordenar** (F-492, EMNLP 2024): recuperar solo rinde
  **0,875** contra **0,504** de reentrenar; añadir reentrenamiento **restó**; y entrenar con hechos
  nuevos **aumenta linealmente la alucinación**.
- ⭐ **El mejor argumento del documento, que reinterpreta la prueba C8 del protocolo:** *AIDA ya
  tiene la regla correcta —no responder de memoria, delegar siempre—; el problema es que **hoy no se
  puede cumplir**, porque el especialista sale a buscar y encuentra contenido contradictorio, vacío o
  ilegible, y en ese vacío el modelo cae de vuelta en la memoria.* **Ordenar el repositorio no es el
  plan B: es lo que hace cumplible la regla que AIDA ya tiene.** Aparece así una **tercera lectura de
  C8** que este node no tenía: la regla puede estar **declarada, ser sincera y ser inejecutable** —
  una falla de **capa A disfrazada de capa B**. Se distingue con la prueba del fragmento pegado.
- **Taxonomía de láminas por tipo** (reescribir · describir con multimodal · excluir del índice ·
  recuperación visual), bastante más accionable que el "los PPT son malos" de §14.
- **Límites operativos de SharePoint** —hipervínculos internos que no se siguen, contenido cifrado
  que falla en silencio, quitar del índice es todo-o-nada— y el **riesgo de adopción** de §6 del
  Release 1.

**Convergencias independientes**, que valen como corroboración y no como eco —son dos trabajos
hechos por separado—: el **ruteo** como punto de falla propio (su paso 1 = **capa D** de §3), **una
sola copia autoritativa por tema** (= la fuente canónica de §9.2), y armar el **banco de control
temprano para tener la medición del antes** (= el Experimento 1 de §12).

⭐ **Lo que este node le aporta a él, y es el hueco de su plan:** su acción #2 —resolver
contradicciones dejando una sola copia autoritativa— **supone que la copia autoritativa es
correcta. §14 demuestra que no lo es**: el Playbook duplica Vida Contigo/VAG, omite VFP, usa
"Flexivida" y declara Pendiente el detalle técnico de producto. Dejar el playbook como copia única
**propagaría el error**. De ahí que el Release 1 abra con **R1.0 · resolver el catálogo**, que su
plan no contemplaba.

⚠️ **Advertencia de fuente (F-489):** su cifra ancla —79,5% → 24,2% por documentos contradictorios—
tiene un **problema de cita abierto**: el arXiv citado resuelve a otro paper y el mecanismo de ese
paper es **conflicto contexto-memoria**, no contradicción entre documentos del corpus. **El fenómeno
y la dirección se sostienen** por literatura adyacente; **la magnitud y la atribución hay que
reverificarlas antes de que entren a un comité.** El orden de prioridades del Release 1 **no cambia**
— se sostiene igual en F-490, F-491 y F-492, todas de venues arbitrados.

---

## 16. Estructura definitiva del Release 1 — tres etapas (v2.0)

**Definida por Alejo el 2026-08-14.** Es la estructura canónica del Release 1 y **manda sobre
cualquier descripción anterior de este node**. §12 (diseño de validación) y §13 (trabajo de campo)
siguen vigentes como el detalle metodológico de las etapas 1 y 3; lo que cambia es el encuadre.

**El Release 1 no es solo la intervención: empieza midiendo y termina comprobando.**

| Etapa | Qué es | Detalle metodológico |
|---|---|---|
| **1 · Diagnóstico de la herramienta** | Encuestas y shadowing con asesores → banco de preguntas reales → evaluación asistida con LLM (usabilidad, error, exactitud) → **medición de tiempo** | §13 (campo) + `_outputs/protocolo-interrogacion-aida-vida.md` Bloques A-D |
| **2 · Intervención en AIDA** | Rediseño de la base de conocimiento. **Objetivo declarado: menos errores y consulta más rápida** | `_outputs/release-1-base-conocimiento-aida.md` R1.0-R1.3 |
| **3 · Testeo** | Contra línea base, o A/B con la nueva solución | §12 |

### 16.1 Lo que la reestructuración agrega

**La velocidad como segundo objetivo declarado.** No requiere trabajo aparte —sale del mismo
movimiento: menos documentos compitiendo por la recuperación y archivos más cortos hacen que el
agente encuentre antes— pero **hay que cronometrarla en la Etapa 1**, o después no se puede
demostrar. Métrica: tiempo hasta obtener algo usable, y número de intentos. **La v1.0 del Release no
la tenía.**

### 16.2 El nombre correcto de "full con puntos de corte"

Alejo plantea la disyuntiva de la Etapa 3 así: *si es posible aislar a AIDA para un grupo de
asesores, o si se debe hacer un full con puntos de corte.* Lo segundo tiene nombre y literatura
propia: **serie temporal interrumpida** (*interrupted time series*), el diseño cuasi-experimental
más fuerte disponible cuando no se puede aleatorizar.

**Tres caminos, según lo que permita la plataforma** — y la pregunta técnica de si se pueden
sostener dos versiones a la vez **va a TI antes que cualquier otra cosa**:

| Si… | Diseño | Nota |
|---|---|---|
| Se pueden dos versiones en paralelo | **A/B por clusters** (equipos, nunca personas) | El más limpio. Aleatorizar personas dentro de una oficina filtra: se pasan capturas |
| Se puede por tandas | **Escalonado** (stepped-wedge) | Requiere ajuste por tendencia temporal, y no está libre de debate metodológico (§12.4) |
| Es todo o nada | **Serie temporal interrumpida** | Necesita **varios puntos de medición antes y después**, no dos fotos |

⭐ **Y la debilidad clásica de la serie temporal interrumpida ya está resuelta por el alcance que
elegimos.** Su problema es que algo más pudo cambiar en el mismo periodo (campaña, estacionalidad).
La solución estándar es agregar una serie de comparación — y **aquí ya la tenemos: el Release 1 se
acota a Vida, así que Salud y Vehicular siguen con la base vieja.** Funcionan como serie de control
natural, sin montar nada. Si Vida mejora y los otros ramos no, el efecto es de la intervención. Es
la variante **comparativa** del diseño, que es la que la literatura recomienda, y **no cuesta
esfuerzo adicional**.

### 16.3 Dos condiciones que se arrastran de §12 y no son negociables

- **Estratificar por antigüedad desde el diseño** — el efecto se concentra en novatos (F-476); sin
  el corte, un efecto real puede leerse como nulo.
- **La conversión no es desenlace primario** — el ciclo de venta de Vida excede la ventana.

---

## 17. La capacidad de entrenamiento y el bucle de casuística (v2.1)

Aporte de Alejo, 2026-08-18. Tres piezas de información que **cambian el estado de la Fase 4**: deja
de ser "prototipar capacidades" y pasa a ser "**ya hay prototipos; falta la evidencia sobre ellos**".

> ⚠️ **Reencuadre (v2.2, 2026-08-19).** En la reunión con la jefatura, **Alejo sacó deliberadamente
> el frente de entrenamiento de la fase 1** — por dos razones que dijo explícitamente: requiere otro
> nivel de desarrollo, y **"la literatura no sostiene que el asesor tenga que entrenar a través de
> AIDA"**, siendo una idea que vino de la propuesta de la herramienta, no de la necesidad levantada.
>
> ⭐ **Esa cautela ahora tiene respaldo citable: F-496** — en profesiones, la práctica deliberada
> explica **menos del 1% de la varianza de desempeño**, la categoría más débil de las cinco medidas.
> Lo que dijo por criterio, la evidencia lo sostiene.
>
> **Entonces este §17 no es una propuesta activa: es el expediente** de lo que hay que tener resuelto
> el día que se decida entrar — y sobre todo, de los dos errores que serían caros de cometer
> (§17.3 la etiqueta, §17.4 el reporte a jefatura). El orden correcto lo fijó la propia reunión:
> **primero el diagnóstico de uso y potencial, después la decisión de desarrollar.**

### 17.1 Lo que se sabe ahora

1. **Entrenar habilidades de venta con AIDA** es una de las capacidades que el equipo quiere probar.
2. **El proceso de captura de casuística se aclara:** AIDA **captura las mejores respuestas durante
   el entrenamiento con AIDA**. La práctica no es solo práctica — es el mecanismo de adquisición.
3. **Behavioral Design ya construyó 2 prototipos.** Uno es una **funcionalidad agéntica de práctica
   sobre Copilot**: el asesor practicaba con **casos ficticios de objeciones**, recibía consejos y
   **era puntuado**; más la capacidad de **guardar los puntajes**, **reportar resultados a la
   jefatura**, y **retroalimentar las capacidades de AIDA**.

⚠️ **Supuesto declarado:** el brief dice "2 prototipos" y describe uno. Se asume que el segundo es el
**prototipo sobre Claude del Plan Piloto** ya documentado en §0 — pero **no está confirmado**, y si
es un tercer artefacto distinto, hay que inventariarlo. **Pregunta P11.**

### 17.2 Por qué la aclaración del proceso es el aporte más valioso, y a la vez el más frágil

**Lo valioso.** El problema de la casuística de los mejores asesores nunca fue *quererla* — fue
**adquirirla**. Ese conocimiento no está escrito, y pedirle a alguien que lo escriba falla dos veces:
no lo hace, y si lo hace escribe la versión declarada, no la que ejecuta. **La práctica lo produce
como subproducto de una actividad que el asesor tiene su propia razón para hacer.** Eso resuelve la
adquisición sin pedirle trabajo extra a nadie. Es la mejor idea del bloque.

**Lo frágil.** El mecanismo validado no funciona exactamente así. Vale la pena poner la comparación
al lado, porque las dos diferencias no son de detalle — deciden si el efecto se reproduce:

| | Brynjolfsson, Li & Raymond (2025) — F-476 | La propuesta |
|---|---|---|
| **Qué se capturó** | Conversaciones **reales con clientes** | Respuestas de **práctica** sobre casos ficticios |
| **Cómo se definió "la mejor"** | Por el **desenlace**: el caso se resolvió. Las conversaciones se **sobreponderaron según el desempeño real** del agente | Por el **puntaje que AIDA misma asigna** contra una rúbrica |

De ahí salen dos riesgos distintos:

**Riesgo 1 · La práctica no es la conducta.** Lo que un asesor dice cuando lo están puntuando es lo
que **cree** que es la respuesta correcta, no necesariamente lo que hace frente al cliente. El corpus
resultante es de práctica **declarada**. No es fatal —sigue siendo mejor que nada, y sigue siendo lo
que hoy no existe— pero hay que nombrarlo, porque cambia lo que se puede prometer.

**Riesgo 2 · El bucle cerrado, y este sí es serio.** Si AIDA puntúa, AIDA selecciona las respuestas
mejor puntuadas, y AIDA después enseña ese corpus, entonces **nada externo corrige nunca la rúbrica**.
La rúbrica pasa a ser la definición operativa de "vender bien" y deriva libre de si efectivamente
vende. Es el mismo problema de fondo que el proyecto ya diagnosticó en la base de conocimiento
—una fuente que se valida a sí misma— reproducido un nivel más arriba.

### 17.3 El arreglo: separar la captura de la etiqueta

⭐ **No hay que renunciar a la idea. Hay que anclar el bucle a una señal de afuera.**

- **La captura sigue igual** — durante la práctica, que es lo barato y lo que funciona.
- **La etiqueta viene de afuera:** qué respuestas entran al corpus canónico se decide por el
  **desempeño real** del asesor (conversión, persistencia de la póliza), **no por su puntaje de
  práctica**. Se sobreponderan las respuestas de quien vende bien de verdad, que es exactamente lo
  que hizo F-476.
- **Y no cuesta trabajo extra:** esa señal de desenlace **ya hay que levantarla** para la Etapa 3 del
  Release 1. Es el mismo dato, usado dos veces.

Beneficio secundario: si la casuística de los mejores-por-resultado rinde distinto que la de los
mejores-por-rúbrica, **eso mismo es un hallazgo** — dice si la rúbrica está midiendo lo que importa.

### 17.4 El reporte a la jefatura puede invertir el signo de todo lo demás

Esta es la pieza más barata de implementar y la más fácil de equivocar, porque **parece una función
gratis**. No lo es.

- **Kluger & DeNisi (1996)** — 607 tamaños de efecto, 23.663 observaciones. El feedback mejora el
  desempeño en promedio (d = 0,41), pero **más de un tercio de las intervenciones de feedback lo
  empeoró**. El moderador es **hacia dónde dirige la atención**: el feedback sobre **la tarea** ayuda;
  el feedback sobre **la persona** perjudica. Un puntaje que llega a tu jefe es, por construcción,
  feedback sobre la persona (F-495).
- **Y hay un efecto de segundo orden propio de este diseño:** si el puntaje es evaluativo, el asesor
  deja de usar la práctica para fallar barato y empieza a usarla para puntuar bien. **Eso contamina
  justamente el corpus que se quiere construir** — se capturan actuaciones para la jefatura, no
  mejores respuestas. **Las dos funcionalidades se atacan entre sí.**

**Recomendación — es decisión de diseño, no técnica:**

| Destinatario | Qué ve | Por qué |
|---|---|---|
| **El asesor** | Su puntaje, su progreso, todo | Feedback de tarea, es el que funciona |
| **La jefatura** | **Agregado y por tema, no por persona** — "en tu equipo la objeción de precio es la debilidad" | Accionable para el jefe sin convertir la práctica en examen |
| **Individual a jefatura** | Solo si se decide después, declarado, y **con el corpus ya construido** | Evita contaminar la captura en el momento en que más importa |

Si el negocio igual quiere reporte individual —decisión legítima—, entonces como mínimo **conservar
un modo de práctica que no puntúe ni reporte**, para que siga existiendo un lugar donde fallar.

### 17.5 Qué esperar de la capacidad de entrenamiento, honestamente

Tres resultados verificados que acotan la promesa:

- **La práctica simulada funciona tan bien como practicar con una persona real** — meta-análisis de
  27 ECAs, 1.480 participantes: sin diferencia significativa en habilidades de comunicación,
  razonamiento ni desempeño global (F-497). ⭐ **Léase bien: el valor no es que enseñe mejor. Es la
  disponibilidad y el costo** — se practica un martes a las 11 de la noche sin agendar a nadie. Ese
  es el argumento correcto, y es suficientemente bueno.
- **La simulación gana mucho contra no hacer nada y poco contra otra instrucción activa** — efectos
  grandes vs. ninguna intervención, pero de 0,30 a 0,66 contra otros métodos (F-498). Si hoy ya hay
  role-play con el jefe, el delta es modesto; si no hay nada, es grande.
- ⚠️ **Y el techo incómodo:** en la meta-analítica de práctica deliberada, **las profesiones son la
  categoría donde la práctica explica menos varianza de desempeño: por debajo del 1%** — contra 26%
  en juegos, 21% en música, 18% en deportes (F-496). **No se puede vender el entrenamiento como la
  palanca de productividad.** Lo que sí sostiene la evidencia es el otro lado: **la práctica como
  mecanismo de captura de casuística** (§17.2), que es un argumento de conocimiento, no de
  aprendizaje.

### 17.6 La colisión con Sales Coach, que nadie ha nombrado todavía

Sales Coach es el **frente 5** del mapa de §2.1: entrenamiento en fases iniciales. **Si AIDA adquiere
capacidad de entrenamiento, hay dos agentes que enseñan** — y dos agentes que enseñan sin una fuente
común es exactamente la falla que este proyecto está diagnosticando en los documentos, reproducida un
nivel más arriba.

§8.1 ya había resuelto la forma —Sales Coach **detrás de la puerta, como modo separado**, apoyado en
Sitzmann 2011 (F-219) sobre el valor de un espacio de práctica seguro y distinto de la conversación
real. **Lo nuevo es que ese "modo separado" ya existe: es el prototipo.** Entonces la pregunta deja
de ser arquitectónica y pasa a ser de propiedad:

**P12 — ¿El prototipo de práctica es el reemplazo de Sales Coach, su reemplazo parcial, o un cuarto
agente?** Las tres son respuestas defendibles; **la que no es defendible es no decidirlo**, porque el
resultado por omisión son dos agentes enseñando modelos de venta que nadie garantizó que coincidan.

### 17.7 Consecuencia para el plan

La Fase 4 se reformula: **ya no es "prototipar capacidades", es "evaluar los prototipos que ya
existen y decidir cuáles se promueven"** — más barato y más rápido de lo que estaba escrito. Y el
orden correcto no es construir más, es:

1. **Inventariar los 2 prototipos** (P11) — qué hace cada uno, sobre qué corre, quién lo tiene.
2. **Decidir la señal de etiqueta** antes de capturar nada (§17.3), porque un corpus construido con
   la etiqueta equivocada hay que rehacerlo entero.
3. **Decidir el destinatario del puntaje** antes de la primera corrida (§17.4), por la misma razón.
4. **Resolver P12** antes de que existan dos agentes que enseñan.

⚠️ **Y una dependencia que no cambia:** todo esto se apoya en que AIDA responda bien. Un agente que
entrena sobre una base contradictoria enseña la contradicción, y la enseña con más eficacia que un
documento. **El Release 1 sigue yendo primero.**

---

## 18. La reunión con la jefatura y el encuadre de la presentación (v2.2)

Conversación de Alejo con Mili (jefatura), agosto 2026. **Es la fuente más informativa que ha
entrado a este node**: resuelve la pregunta técnica que estaba bloqueando el diagnóstico, impone una
restricción que cambia el diseño de validación, y fija el encuadre político del primer entregable.

### 18.1 ⭐ P9 RESUELTA — AIDA no corre sobre Copilot, corre sobre Google

Declarado en la reunión: *"suponíamos que como era de Copilot, incluso su capacidad de inferencia era
poca, pero **sí sabemos que ahora es de Google**"*.

**Esto confirma la señal de la auto-interrogación** (§11, H4): AIDA declaró `transfer_to_agent`, que
es de **Google ADK**, no de Copilot Studio. La contradicción no era un error de la herramienta — era
el dato correcto.

**Consecuencias, y son varias:**

| Qué cambia | Antes | Ahora |
|---|---|---|
| Límites numéricos de Copilot (7 MB / 200 MB, 36.000 caracteres/archivo, ≤300 págs.) | Suspendidos hasta confirmar | ⛔ **Descartados** — no aplican. `[[arquitectura-conocimiento-agentes-copilot]]` §3 queda acotado a su título |
| Las **reglas de redacción y formato** (F-490 a F-492, F-469 a F-475) | Vigentes | ✅ **Siguen vigentes** — son propiedades de la recuperación, no del fabricante |
| Capacidad de inferencia esperada | Baja (supuesto) | **Desconocida y probablemente mayor** — hay que medirla, no suponerla |
| Argumento con este auditorio | Neutro | ⭐ **Favorable**: la organización ya evalúa mover toda la ofimática a Google (análisis a cargo de Miguel Portugal, tentativo, no cerrado). El trabajo sobre AIDA **rema a favor** de esa dirección, no en contra |

⚠️ **Y una advertencia de método que la reunión deja explícita:** el supuesto "es Copilot, luego
infiere poco" estuvo condicionando el diagnóstico. **Ya no se supone: se mide.** Es exactamente lo
que justifica el bloque de auditoría con LLM.

### 18.2 ⛔ No hay sandbox de AIDA — la restricción que más cambia el plan

Confirmado por el equipo de la herramienta y ratificado por la jefatura: **no existe espacio de
sandboxing.** No se puede crear una funcionalidad y dársela a 10 asesores.

**Qué sobrevive y qué no:**

| Diseño | Estado |
|---|---|
| A/B de **funcionalidad nueva** dentro de AIDA | ⛔ **Imposible.** No hay forma de aislar un grupo |
| Serie temporal interrumpida sobre la **base de conocimiento** | ✅ **Sigue en pie** — la intervención es de contenido, no de código, y los otros ramos siguen siendo la serie de comparación |
| Testeo de funcionalidades **en los prototipos** | ✅ **Es la única vía** |

⭐ **Esto convierte la propuesta de "el prototipo como banco de prototipado" en la única opción
disponible, no en una preferencia de diseño.** Y hay antecedente presupuestal: para Back to Basics
ya hubo disposición a invertir en un prototipo para probar una funcionalidad.

### 18.3 Las tres funciones declaradas de AIDA, y el estado real de cada una

Levantadas de **dos fuentes que no obligan a confrontar a nadie**: la documentación de RIMAC sobre el
proyecto AIDA, y **lo que la propia herramienta responde cuando se le pregunta para qué sirve**.

| # | Función declarada | Estado según el diagnóstico |
|---|---|---|
| 1 | **Centralizar el conocimiento y los recursos del asesor** | ⛔ **Muy poco.** El conocimiento sigue viviendo en el cartapacio, en la capa y en el onboarding. En recursos, **Sales Coach: cero** |
| 2 | **Dar soporte comercial** | 🟡 **Parcial.** Se le dieron lógicas para construir mensajes recomendados a partir de una base de conocimiento — la función existe, la calidad del insumo es el problema |
| 3 | **Consultar información oficial y actualizada de producto** | 🟡 **Arquitectura sí, contenido no.** Existe la consulta a un SharePoint, pero la información no está seteada de la manera correcta |

**Hipótesis de la jefatura, y vale la pena retenerla:** AIDA **nació para la función 2**, y las otras
dos se le agregaron después. El argumento es de coherencia de diseño — si las tres hubieran sido la
premisa, la orquestación sería otra. ⚠️ Es hipótesis, no dato; **P13**.

⚠️ **Riesgo epistémico de usar la auto-descripción de AIDA como línea base.** Es elegante
políticamente y §11 ya lo advirtió: **es autorreporte**. Si AIDA describe mal su propio propósito, la
brecha se mide contra una promesa alucinada. **Mitigación: la documentación manda, la auto-descripción
corrobora.** Y si divergen, esa divergencia **es un hallazgo gratis** —la herramienta no sabe para
qué es— y sigue sin confrontar a nadie.

### 18.4 El encuadre político del entregable (definido por la jefatura)

**Regla dura: no confrontar a la PO de AIDA.** No se va a preguntar "para qué sirve AIDA" para
después contrastar esa respuesta con los hechos. **Se contrasta la herramienta contra su propia
declaración documentada.**

**Estructura acordada:**

1. **De dónde venimos** — del trabajo de estrategia de Vida (Back to Basics); en el camino
   aparecieron oportunidades que afectan **transversalmente** a la fuerza de ventas.
2. **Esto dice la documentación y esto dice la herramienta de sí misma** (la promesa).
3. **Esto es lo que encontramos que hace** (auditoría) **y esto es lo que el asesor hace con ella**
   (campo).
4. **¿Cómo cerramos estas brechas?** — pregunta abierta, no lista de exigencias.
5. **Backlog de quick fixes: de respaldo**, no de contenido principal. Sale cuando la conversación
   gira hacia soluciones.

**El pedido no es "arreglen esto".** Es **feedback + co-crear una matriz de priorización**: el equipo
trae la voz del asesor; los dueños de la capacidad traen la factibilidad. Encuadre declarado:
**responsabilidad colectiva**.

- **Auditorio:** Emanuel, Will y Miguel Portugal. La jefatura la lleva después a comité y
  posiblemente a Giselle.
- **Formato:** **presentación pequeña**, explícitamente no extensa.
- **Fuera del alcance de esta conversación:** las **integraciones con Salesforce**. Will las declaró
  viables (un front en AIDA con métricas de Salesforce, y registro desde ahí), pero **cruzan a otro
  dueño** — la puerta se abre recién después de consultarlo. Se mapea, no se propone.

### 18.5 Los seis fixes de la fase 1, como los enumeró Alejo

Todos son **fixes mínimos**: cambios de lógica y de carga de documentos. **No requieren inversión —
requieren capacidad.**

| # | Fix | Correspondencia en el Release 1 |
|---|---|---|
| 1 | Cargar el **catálogo de productos** con gobierno de actualización comprometido por Productos | **R1.0**, el bloqueante |
| 2 | Cargar el **modelo de venta** (Playbook) partido en secciones, sin las partes gráficas | **R1.2** |
| 3 | **Sacar del índice** lo que no debe responder y ordenar los documentos | **R1.1** |
| 4 | **Láminas → cuadros** | **R1.3** |
| 5 | **Evaluar la consistencia** de las respuestas | **R1.4** + §18.6 |
| 6 | **Que la pantalla no aparezca en blanco** — guía de uso y recuperación de desertores | La pieza de reintroducción de §6 del Release 1 |

⭐ **La correspondencia es casi exacta con lo que el Release 1 ya tenía.** Eso es corroboración
independiente del alcance: se llegó a la misma lista por dos caminos.

**Y el punto de gobernanza que la jefatura marcó como condición, no como deseo:** *"si le vamos a dar
un Excel, puede terminar pasando lo mismo... necesitamos que **Productos se comprometa** a tener por
lo menos un flujo de actualización"*. Sin eso, **la promesa de información actualizada no tiene
sentido**. Es la misma conclusión de §10 y de "lo que el Release 1 no arregla".

### 18.6 ⭐ Metodología de jueces por área — un patrón oro que el proyecto no tenía

Propuesta nueva de la reunión: preguntarle a **Experiencia, Negocio y Marketing** qué *debería*
responder AIDA ante una pregunta dada, y usar eso como referencia contra la respuesta real.

**Por qué es un aporte y no una variante:** el protocolo actual usa **la matriz de producto** como
patrón oro, y eso solo sirve para la capa de **dato de producto**. Esto abre patrón oro para la capa
de **mensaje** —cómo hablarle al cliente—, que no tenía ninguno.

**Y tiene un segundo efecto que vale más que el primero:** si las tres áreas responden distinto, **la
inconsistencia no es de AIDA — es de la organización**, y queda medida. Es exactamente la tesis de §9
(*el copiloto no puede resolver la contradicción aguas arriba, solo ocultarla*), convertida en
instrumento. **Se incorpora al protocolo como Bloque E.**

### 18.7 Los tres artefactos de exploración, y el cuarto que cambió de dueño

| Artefacto | Qué hace |
|---|---|
| **Auditoría de la herramienta** | Estresarla, evaluar la calidad de sus respuestas con método estructurado (Bloque D + Bloque E) |
| **Reporte del asesor** | Encuesta + **shadowing** (~3 asesores, unas horas) — con foco en **cómo y para qué usan las herramientas de afuera**, que es lo que hoy no se ve |
| **Reporte de fallos técnicos** | Tiempos, inconsistencias. Simple y hoy inexistente |
| ~~Qué debería y qué no debería ser AIDA~~ | ⭐ **Cambió de dueño:** la jefatura definió que **no sale del diagnóstico** — lo tienen que declarar los **dueños de la capacidad**. Deja de ser entregable y pasa a ser **la pregunta que se lleva a la reunión** |

**Herramienta de campo:** **Wiser** (vía Dani) para las encuestas, incluida su modalidad
cuantitativa. ⚠️ **Restricción operativa:** los asesores tienen la IA bloqueada en la computadora —
**responden desde el teléfono**.

### 18.8 Datos de campo que la reunión agrega o precisa

- ⭐ **La mayoría de asesores usa AIDA y a la vez declara que no le es útil.** La lectura de Alejo:
  el uso está **movido por una métrica de uso, no por utilidad percibida**. **Consecuencia directa
  para este auditorio: cualquier número de adopción que se esté reportando hacia arriba no es señal
  de valor.** Es el hallazgo más filoso de la reunión y merece existir solo.
- **Conducta compensatoria confirmada por los propios asesores:** usan **ChatGPT y Gemini** por fuera
  para "qué respondo en este caso", "cómo manejo esta objeción".
- **La mejora más pedida es la consistencia de las respuestas.**
- **La capacidad peor calificada es el manejo de objeciones** — y ahí se refiere a **los recursos que
  se le dan al asesor**, no a AIDA. **Solo 6 asesores** consideran que reciben información suficiente
  para manejarlas.
- **Donde los asesores ven la mayor oportunidad de mejora es en AIDA.** ⭐ Dato de adopción
  favorable: no la dieron por perdida.

### 18.9 Preguntas nuevas

**P13 — ¿AIDA nació para "soporte comercial" y el resto se le agregó?** (hipótesis de la jefatura,
§18.3). Cambia si el diagnóstico mide una promesa real o una promesa retrospectiva.

**P14 — ¿Cuál es el objetivo declarado de AIDA según sus dueños?** Qué se espera que haga y **qué se
espera que NO haga**. La jefatura la marcó como **la pregunta a llevar a la reunión**, no a inferir.

**P15 — ¿Qué implica exactamente "es de Google"?** ¿Gemini Enterprise, Agentspace, ADK a medida? De
eso dependen los límites reales de archivo, la capacidad de inferencia y qué se puede pedir. **Miguel
Portugal es el interlocutor natural.**

---

## 19. Entrevista con la PO de AIDA — objetivos, alcance y gobierno (v2.3)

Reunión del equipo (Alejo, Melissa, Felipe) con **Radille, PO de las funcionalidades de AIDA
asociadas a la FFVV**, agosto 2026.

⭐ **Es la entrada de mayor valor que ha recibido el proyecto.** Resuelve cinco preguntas abiertas,
**confirma tres hipótesis centrales del diagnóstico desde la propia dueña de la capacidad**, revela
un canal de intervención barato que ya está abierto, y abre una contradicción técnica que hay que
resolver antes de decidir arquitectura.

⭐ **Nota de encuadre:** todo lo que sigue es **declaración de la PO**, no inspección. Pero a
diferencia del autorreporte de AIDA (§11), aquí la fuente es **la persona responsable de la
capacidad**, y varias de sus afirmaciones son verificables contra los logs que ya se solicitaron.

### 19.1 Qué es AIDA, según su PO

**Nace de una iniciativa estratégica del año pasado con dos frentes**, y de ahí salen **dos versiones
distintas**:

| | **AIDA Service** | **AIDA Sales** |
|---|---|---|
| **Para** | Central de Consultas | **Plaza de ventas (FFVV)**, BI Pro, equipo del Hub, piloto del canal BIF |
| **Qué hace** | Procedimientos, para el asesor atendiendo al cliente en línea. Consulta por DNI del cliente | Información de producto abocada a la venta |
| **Arquitectura** | ✅ **La misma en ambas** | ✅ La misma |
| **Base de conocimiento** | Independiente | Independiente |
| **¿Conversan entre sí?** | ⛔ **No.** Cada base es independiente | ⛔ No |

⚠️ **Y acá aparece una discrepancia con §11 que hay que declarar.** La auto-interrogación devolvió
**cinco subagentes por ramo** (`SaludAgent`, `VehicularAgent`, `VidaFinancieroAgent`,
`GeneralOpsAgent`, `SalesCoachAgent`). **La PO no describe esa segmentación** — describe **dos
productos separados por caso de uso** (Service / Sales), y dentro de Sales, distintos canales.

Las dos descripciones **no se contradicen necesariamente** —AIDA Sales podría tener subagentes por
ramo adentro— pero **tampoco se confirman**. ⭐ **Esto refuerza la advertencia epistémica de §11: el
autorreporte de un modelo sobre su propia arquitectura no es documentación.** H1, H2 y H5 quedan
**sin confirmar por la PO**, y hay que resolverlos contra el diagrama de arquitectura, no contra
AIDA. **P16.**

### 19.2 ✅ P14 RESUELTA — el objetivo declarado, en palabras de la PO

Melissa lo formuló y Radille lo confirmó textualmente:

> *"¿Podríamos decir que fue para un tema de **consolidación de información** para el asesor y
> justamente **reducir tiempos de búsqueda**?"*
> — **"Ese fue el objetivo."**

**Y las funcionalidades declaradas de AIDA Sales son tres, concretas:**

1. **Genera speeches de venta personalizados**
2. **Genera cuadros comparativos entre planes**
3. **Comparte los brochures** cargados en la base, para que el asesor no los busque en distintos lugares

⭐⭐ **Esto corrige el encuadre del proyecto, y también corrige a P13.** El repo venía trabajando con
**tres funciones declaradas** de igual jerarquía —centralizar conocimiento · dar soporte comercial ·
consultar información de producto—, levantadas de documentación y de la auto-descripción.

**La PO dice que hay un objetivo, no tres:** *consolidar información y reducir el tiempo de búsqueda*.
Las otras dos son **funcionalidades construidas al servicio de ese objetivo**, no fines en sí mismas.

⭐ **Consecuencia para la lectura de la brecha:** la función que el diagnóstico marcaba como "sin
avance" —centralizar el conocimiento y los recursos— **no era una de tres promesas. Era la promesa.**
La brecha es más seria de lo que estaba presentada, y a la vez **más fácil de conversar**, porque
ataca exactamente lo que la capacidad se propuso hacer.

⚠️ **P13 queda resuelta al revés de como se planteó.** La hipótesis de la jefatura era que AIDA nació
para *soporte comercial* y lo demás se le agregó. **No: nació para consolidación.** El soporte
comercial es una funcionalidad encima.

### 19.3 ⭐⭐⭐ Cómo se mide el éxito — y la confirmación del hallazgo más filoso

**Los dashboards de seguimiento miden:**
- Cantidad de consultas de los asesores
- Promedio de consultas diarias
- **Ratio de feedback positivo / negativo**
- Margen de error de las respuestas
- Actividad

Alejo preguntó directo: *"¿Entonces el objetivo es la métrica de adopción?"*
Radille: **"Sí, la cantidad de consultas, el promedio de consultas diarias y la actividad."**

⭐⭐⭐ **Y la pieza que faltaba, que Melissa desenterró con la pregunta correcta:**

> *"¿Hubo algún tipo de incentivos, o se metió dentro de los indicadores de los asesores para
> incentivar ese uso?"*
> — **"Están en su business, en su variable."**

**El uso de AIDA está dentro de la retribución variable del asesor.**

⭐⭐⭐ **Esto convierte en hecho lo que §18.8 tenía como inferencia.** El diagnóstico había deducido
—de la coexistencia de "la usa" y "no me sirve"— que el uso no lo movía la utilidad. **Ahora está
confirmado por la dueña de la capacidad: el uso está incentivado directamente y el criterio de éxito
declarado es la métrica de adopción.**

**Consecuencia, y hay que decirla con cuidado porque es delicada:** la cifra de adopción **no puede
leerse como señal de valor**, no porque nadie haya hecho trampa, sino **por construcción del
indicador**. Un asesor que consulta AIDA porque está en su variable produce el mismo número que uno
que la consulta porque le sirve. **El indicador no distingue, y no fue diseñado para distinguir.**

⭐ **La lectura constructiva, y es la que va a la presentación:** no es que la medición esté mal
hecha. Es que **mide adopción, y adopción no es utilidad** — y hoy no existe ningún indicador que
mida lo segundo. Ese es el hueco, y llenarlo es barato.

### 19.4 Línea base real — ✅ P5 RESUELTA

| Dato | Valor |
|---|---|
| **Despliegue de AIDA Sales** | **Mayo de 2025** — lleva más de un año en producción |
| Trayectoria | Crecimiento sostenido desde mayo hasta cierre de año |
| **Estado actual** | **Volumen estable** |
| **Volumen** | **>30.000 consultas mensuales** |
| **Promedio por asesor** | **3 a 3,5 consultas diarias** |

⭐ **Existe línea base y es sólida.** El diagnóstico no arranca de cero: hay más de un año de serie
temporal, que es exactamente lo que necesita el diseño de serie temporal interrumpida (§16.2).

### 19.5 ✅✅ P4 RESUELTA — los logs existen, son accesibles y ya se pidieron

Radille confirmó que hay **logs**, y precisó qué contienen:

> *"No es la conversación de Radille con AIDA. Es **todas las preguntas que le llegan a AIDA, cómo
> responde, y si le pusieron feedback positivo o negativo**."*

⭐⭐⭐ **Eso es exactamente el corpus de fallas que §4 declaraba como fuente ideal y no sabía si
existía.** Tiene los tres campos que el formato necesita —pregunta · respuesta · señal de calidad— con
volumen real y sin sesgo de recuerdo.

**Alejo ya los solicitó por correo.**

⭐ **Consecuencia para el plan de campo:** la opción 3 de la jerarquía de §4 —pedirle a un grupo de
asesores que registre durante una semana las consultas no resueltas— **queda descartada por
innecesaria**. Se ahorra tiempo de asesor, que era el recurso más caro y el que carga la deuda de
credibilidad de §13.6.

⚠️ **Lo que los logs no dan, y el campo sigue teniendo que dar:** las seis cosas de §13.1 — sobre
todo **qué dejaron de preguntar**, que es invisible en cualquier telemetría por definición.

### 19.6 ⭐⭐⭐ La arquitectura: es RAG puro, y la PO cierra el debate de reentrenar

Alejo preguntó si el modelo fue entrenado con la información. La respuesta es inequívoca:

> *"El modelo lee la documentación de SharePoint. **El modelo no genera data, extrae.** El modelo no
> genera ningún tipo de información. Lo que hace es **interpretar la base de conocimientos**,
> identificar qué se está consultando y sobre esa información responde. Inclusive **en la respuesta te
> pone los documentos de referencia** sobre los cuales se basó."*

Y Alejo lo formuló de vuelta, que es como quedó cerrado:

> *"Entonces, dependiendo de la calidad de la información que tenga el negocio actualizada, el modelo
> va a poder razonar mejor."*

⭐⭐⭐ **Esto es la validación más fuerte posible de la tesis del Release 1, y no viene del CoE — viene
de la dueña de la capacidad.**

| Lo que el proyecto venía argumentando con evidencia externa | Lo que la PO declara |
|---|---|
| Reentrenar casi no mueve la aguja; darle el documento correcto al responder es el mejor resultado y el más barato (F-490, F-492) | **No hay nada que reentrenar. El modelo no genera información, la extrae** |
| Ordenar el repositorio no es el plan B, es lo que vuelve cumplible la regla que AIDA ya tiene | **La calidad de la respuesta es función directa de la calidad del SharePoint** |
| El diseño debe mostrar fragmento y fuente, no solo el enlace | **AIDA ya cita los documentos de referencia** en cada respuesta |

⭐ **La discusión "¿arreglamos la base o reentrenamos el modelo?" queda cerrada. No era una
disyuntiva.**

### 19.7 ⛔⛔ La contradicción técnica: SharePoint vs. Google

**La PO dice, dos veces y sin ambigüedad, que la base de conocimiento vive en SharePoint** —
"ambas son SharePoint", "es un SharePoint que tiene una estructura de carpetas".

**SharePoint es Microsoft.** Y la reunión con la jefatura (§18.1) estableció que **AIDA corre sobre
Google**.

**Las dos afirmaciones pueden ser compatibles, y la lectura más probable las reconcilia:**

| Capa | Probable | Estado |
|---|---|---|
| **Motor / modelo** | Google | Declarado por la jefatura |
| **Repositorio documental** | **SharePoint (Microsoft)** | ✅ Declarado por la PO, dos veces |

Un motor de Google indexando un repositorio SharePoint es una arquitectura común y perfectamente
viable. **Pero no está confirmado**, y hay dos consecuencias que obligan a resolverlo:

1. ⚠️ **Algunos límites de SharePoint podrían sí aplicar** —umbral de indexación, tratamiento de
   formatos, permisos— aunque los de **Copilot Studio** sigan descartados. **No reabrir los números de
   Copilot; sí verificar los del repositorio.**
2. ⚠️ **La decisión de arquitectura de la Fase 5 depende de saber qué habla con qué.**

⭐ **P15 se precisa:** ya no es solo *"¿qué servicio de Google?"* sino **"¿qué servicio de Google
indexa un SharePoint de Microsoft, y con qué límites?"** Interlocutores: Miguel Portugal y el equipo
técnico de Radille. **Existe un diagrama de arquitectura** — pedirlo explícitamente.

### 19.8 ⭐⭐ El gobierno de la base: dónde está exactamente el hueco

> *"Es un SharePoint que tiene una estructura de carpetas."*
> *"**Cada ramo vela porque sus características estén bien.**"*
> *"Internamente **no** [hay un analista asignado]... **cómo se organicen** [es de cada ramo]."*

⭐⭐ **Esto identifica el hueco de gobernanza con precisión, y de forma no acusatoria.**

La responsabilidad **está asignada** —cada ramo responde por su carpeta— pero **sin rol declarado, sin
cadencia, sin criterio de calidad y sin nadie que verifique.** Cada ramo se organiza como puede.

⭐ **Y ese es exactamente el mecanismo por el que se llega a un catálogo con duplicados, versiones de
2022 conviviendo con vigentes, y archivos vacíos.** No hay nadie haciendo mal su trabajo. **El trabajo
no está definido.**

**Consecuencia directa para el Release 1:** la condición de gobernanza de §11.3 del dossier —que
Productos se comprometa a un flujo de actualización— **no es un pedido extraordinario. Es completar
algo que la arquitectura ya asume que existe.**

### 19.9 ⭐⭐ La calidad se mide con feedback — y el feedback ya apunta a la capa A

> *"Los asesores tienen que darle feedback positivo o negativo a cada [respuesta]."*
> *"**En los últimos meses, cualquier feedback negativo estaba más en relación a alguna documentación
> que no estaba actualizada o alguna documentación que no estaba completa.**"*

⭐⭐⭐ **La PO confirma el diagnóstico central del proyecto, con sus propios datos.**

El feedback negativo de AIDA **ya está trazado a documentación desactualizada o incompleta** — es
decir, **capa A (conocimiento)**, que era la hipótesis principal y la que el proyecto se proponía
falsar.

⭐ **Valor para la presentación:** la brecha deja de ser una interpretación del CoE. **Es lo que el
propio sistema de feedback de AIDA viene registrando.** No hay que convencer a nadie de que el
problema es el contenido — el instrumento de la capacidad ya lo dice.

⚠️ **Lo que esto no cierra:** la proporción. Saber que el feedback negativo "está más en relación a"
documentación no dice **cuánto** del total es capa A y cuánto es B, C o D. **Eso sale de los logs**, y
es la primera pregunta a hacerles.

### 19.10 ✅ Confirmación en población propia del efecto por antigüedad

Melissa preguntó si habían analizado quiénes usan más la herramienta:

> *"La tendencia es que **los que tienen mayor uso son asesores nuevos**, y los que tienen menos uso
> son **asesores ya antiguos o más expertos**."*

⭐⭐ **Esto confirma F-476 en la población de RIMAC.** Brynjolfsson, Li & Raymond midieron +34% en
novatos y efecto mínimo en expertos. El patrón de uso de AIDA reproduce esa distribución.

⭐ **Y ahorra trabajo:** §5.1 proponía *"reanalizar la encuesta cortando por antigüedad, es trabajo de
una tarde"*. **La PO ya tiene el dato y confirma el patrón.** Lo que queda es cuantificarlo contra los
logs.

⚠️ **Precisión importante:** esto confirma el patrón de **uso**, no el de **efecto**. Que los novatos
la usen más no prueba que les rinda más — aunque es consistente con que así sea. **La estratificación
por antigüedad en el diseño de validación (§16.3) sigue siendo obligatoria.**

### 19.11 ⛔⛔⛔ No hay roadmap de AIDA — y el proceso real de cambio

**Declarado sin rodeos:**

> *"**No hay ahorita un roadmap de mejora de AIDA.** Bajo la nueva estructura del modelo operativo,
> **el negocio es quien tiene que gatillar las solicitudes** de cualquier cambio o mejora nueva. Si
> pasa algo con AIDA, alguna incidencia, se soluciona. Pero si son cosas nuevas o cambios, tienen que
> entrar por este [proceso]."*

**El proceso formal de solicitud, en cuatro pasos:**

| # | Paso | Detalle |
|---|---|---|
| 1 | **El negocio genera una solicitud** | No el CoE, no TI. **El negocio** |
| 2 | **Acompañada de una captura de valor** | *"No llega a ser un business case, es algo más sencillo, pero el objetivo es que cualquier solución genere una captura: puede ser en plata, puede ser en KPIs"* |
| 3 | **Evaluación por "metodología de fricción de la demanda"** | ⚠️ Metodología no detallada — **P17** |
| 4 | **En base a eso se desarrolla la capacidad** | |

⭐⭐ **Y el cuello de botella real, que el proyecto tenía mal caracterizado:**

> *"En la mayoría de casos hay un tema de presupuesto, porque necesita perfiles que no tenemos. Los
> recursos son **staffeables**: están en el equipo de IA pero **no son recursos asignados al BAU**. Si
> vienes con una iniciativa y necesitas uno de ellos, **tienes la plata, lo pagas y te lo llevas**."*

⚠️ **Corrección al Release 1.** El proyecto venía afirmando que los seis arreglos *"no necesitan
inversión, solo capacidad"*. **Eso es impreciso: en esta organización, capacidad ES presupuesto** —
los recursos del equipo de IA son staffeables y los paga el negocio que los solicita.

### 19.12 ⭐⭐⭐ El camino barato, declarado por la propia PO — y ya está abierto

Radille lo dijo sin que se lo preguntaran, cerrando la reunión:

> *"Lo más sencillo es **agregar base de conocimiento**. Es un poco lo que estamos haciendo con Jaime,
> que sale de **las mesas de trabajo de los jueves**: todo lo que están actualizando del manual, de los
> catálogos de beneficios, todo eso se está **centralizando a través de AIDA**. Eso es lo más sencillo:
> **cargar nueva base de conocimientos es lo más sencillo**."*

⭐⭐⭐ **Esto es lo más accionable de toda la entrevista, y cambia la táctica del Release 1.**

Hay **dos caminos**, con costos radicalmente distintos, y la PO acaba de decir cuál es cuál:

| Camino | Qué incluye | Costo | Proceso |
|---|---|---|---|
| ⭐ **Carga de base de conocimiento** | Documentos nuevos, corregidos o reformateados en el SharePoint | **El más sencillo.** Sin presupuesto ni staffing | **Ya existe un canal abierto y funcionando** (Jaime, mesas de los jueves) |
| **Cambio de capacidad** | Funcionalidad nueva, cambios de lógica, interfaz | Requiere presupuesto y recursos staffeables | Solicitud del negocio + captura de valor + fricción de la demanda |

**Ahora se puede clasificar cada uno de los seis arreglos de §18.5 contra esa división:**

| # | Arreglo | Camino |
|---|---|---|
| 1 | Cerrar el catálogo de producto | ⭐ **Carga de base** — barato, canal abierto |
| 2 | Cargar el modelo de venta (Playbook partido y des-tabulado) | ⭐ **Carga de base** — barato, canal abierto |
| 3 | Sacar del índice lo que no debe responder | ⭐ **Carga de base** (bajas) — barato |
| 4 | Convertir láminas en cuadros | ⭐ **Carga de base** — barato |
| 5 | Evaluar la consistencia de las respuestas | 🟡 **Mixto** — el banco de control lo corre el CoE; instrumentarlo dentro de AIDA sí es capacidad |
| 6 | Que la pantalla no arranque en blanco | 🔴 **Capacidad** — requiere solicitud, captura de valor y presupuesto |

⭐⭐ **Cuatro de los seis arreglos —y son los que sostienen la promesa del Release 1— caen del lado
barato, por un canal que ya está operando.** No hay que crear un proceso: hay que **sumarse a las
mesas de los jueves**.

⭐ **Y el arreglo 6 —la pantalla en blanco— es el que necesita el business case.** Que es justamente
donde el proyecto tiene el argumento más fuerte: es la pieza que decide si la mejora **llega** a los
asesores que ya la abandonaron (§20 del dossier).

### 19.13 Contexto político

- ⚠️ **El equipo de Radille depende de Giselle**, y Radille identificó a **Giselle como quien originó
  el pedido de la reunión**. La misma persona a quien la jefatura pensaba escalar el tema. Conviene
  tenerlo presente antes de mover piezas.
- Radille preguntó explícitamente si el interés va por *"factibilidades técnicas o lo que ya hayamos
  hecho"* o por *"un wish de lo que pueda querer el asesor"*. ⭐ **La respuesta honesta es que va por
  lo segundo, y conviene decirlo así** — encaja con el encuadre de responsabilidad compartida y evita
  que la conversación se lea como auditoría.
- **Existe un diagrama de arquitectura.** Radille lo mencionó con reticencia (*"no me queda claro cuál
  sería la [utilidad]"*). **Acceso no confirmado** — pedirlo con propósito explícito.

### 19.14 Preguntas nuevas y estado actualizado

**P16 — ¿AIDA Sales tiene subagentes por ramo adentro?** La auto-interrogación declaró cinco; la PO
describe segmentación por caso de uso y canal. Se resuelve con el diagrama, no preguntándole a AIDA.

**P17 — ¿Qué es la "metodología de fricción de la demanda"?** Es el filtro por el que pasa cualquier
solicitud. **Conocerla es saber cómo se escribe una solicitud que pasa.**

**P18 — ¿Qué proporción del feedback negativo es capa A?** La PO dice que "está más en relación a"
documentación desactualizada o incompleta. **Los logs deberían permitir cuantificarlo**, y es la
primera pregunta que hay que hacerles.

**P19 — ¿Cómo se entra a las mesas de trabajo de los jueves?** Es el canal barato ya abierto (§19.12).
**Probablemente la pregunta operativa más rentable del proyecto.**

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
