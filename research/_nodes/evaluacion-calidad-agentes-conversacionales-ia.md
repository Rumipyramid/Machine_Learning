# Evaluación de calidad de agentes conversacionales de IA (chatbots)

> Documento de investigación. Fuente persistente y versionada en el repositorio.
> Fecha de elaboración: 2026-07-15 · Versión: v1.0
> Origen: `/seeker` — investigación de espectro amplio (empírico + teórico)

---

## 0. Veredicto inicial

Sí existen escalas y frameworks establecidos — no uno solo, sino **tres familias
distintas** que miden cosas distintas y no deberían mezclarse en un puntaje único:
(1) escalas de usabilidad centradas en la percepción del usuario, con décadas de
validación psicométrica; (2) métricas técnicas automatizadas para modelos de lenguaje/RAG,
mucho más recientes (2023-2025); y (3) frameworks específicos de banca/seguros, escasos y
de rigor desigual. Todas son aplicables al caso del agente de RIMAC, y de hecho conviene
usar más de una a la vez porque miden ejes distintos del mismo problema.

---

## 1. Los tres ejes que no hay que mezclar

Antes de elegir una escala, conviene separar **qué se está midiendo realmente**, porque un
chatbot puede fallar en un eje sin fallar en los otros:

1. **Éxito de tarea (task success)** — ¿resolvió lo que el usuario necesitaba? Métrica
   operativa: resolution rate.
2. **Percepción/satisfacción del usuario** — ¿la experiencia se sintió bien, clara,
   confiable? Se mide con cuestionarios de autorreporte validados.
3. **Corrección objetiva de la respuesta** — ¿la información que dio es fiel a la fuente
   real (no inventó datos de producto)? Se mide con métricas técnicas automatizadas sobre
   las respuestas mismas, no con encuestas a usuarios.

Un chatbot puede completar la tarea (eje 1) con una experiencia percibida como mala (eje 2)
precisamente porque cometió errores de exactitud puntuales (eje 3) — los tres ejes hay que
medirlos por separado para diagnosticar dónde está el problema real, no promediarlos en un
solo número.

---

## 2. Familia 1 — Escalas de usabilidad centradas en el usuario

| Escala | Qué mide | Rigor | Nota |
|---|---|---|---|
| **PARADISE** (Walker et al., 1997 — F-147) | Satisfacción = función ponderada de éxito de tarea menos costo de interacción (duración, turnos, errores) | 🟢 A — canónico, ACL Anthology | Separa explícitamente "¿logró su objetivo?" de "¿qué tan costoso fue?" |
| **SASSI** (Hone & Graham, 2000 — F-148) | 6 factores de autorreporte, incluye precisión percibida y velocidad | 🟢 A — _Natural Language Engineering_ | Diseñado originalmente para sistemas de voz, pero ampliamente extendido a chatbots de texto |
| **CUQ** — Chatbot Usability Questionnaire (Ulster University — F-149) | 16 ítems, 0-100 (comparable a SUS), 4 factores: personalidad, UX, **manejo de errores**, onboarding | 🔴 tesis original no arbitrada / 🟢 validación 2023 sí arbitrada (Springer) | **La más directamente aplicable al caso de RIMAC** — tiene un factor específico de manejo de errores |
| **BUS-11** (re-examinado 2024 — F-150) | 11 ítems, validado específicamente para chatbots de atención al cliente/CRM | 🟢 A — _Personal and Ubiquitous Computing_ (Springer) | Caso de uso más parecido al de RIMAC: chatbot comercial de cara al cliente, no de propósito general |

**Cómo se usan:** son cuestionarios que se administran a usuarios reales después de
interactuar con el agente — miden percepción, no corrección objetiva de las respuestas.

---

## 3. Familia 2 — Métricas técnicas para modelos de lenguaje / RAG

Distinto de las escalas de arriba: no son cuestionarios a personas, son **métricas
automatizadas calculadas sobre las respuestas mismas** del modelo, típicamente con otro LLM
como evaluador ("LLM-as-judge").

- **RAGAS** (F-151, ⚠️ visto vía documentación técnica de terceros, no el paper original) —
  el estándar de facto actual para sistemas RAG (agentes que responden basándose en
  documentos/base de conocimiento, como probablemente hace el agente de RIMAC sobre
  información de productos):
  - *Faithfulness*: ¿la respuesta es fiel a la fuente recuperada? Se calcula extrayendo
    afirmaciones discretas de la respuesta y verificando cada una contra el contexto — así
    se detecta alucinación de forma granular, no binaria.
  - *Answer relevancy*: ¿la respuesta contesta lo que se preguntó?
  - *Context precision/recall*: ¿el sistema recuperó la información correcta antes de
    responder?
- **LLM-as-judge con rúbrica** — usar un modelo para puntuar respuestas contra criterios
  explícitos. Tiene sesgos documentados (verbosity bias: preferir respuestas más largas;
  position bias: preferir la primera opción en comparaciones) que se mitigan con prompting
  estructurado y rúbricas explícitas, no eliminándolos por completo.

**Limitación importante:** esta familia es de 2023-2025, mucho menos madura que las
escalas de usabilidad (que tienen 25+ años de validación). No hay todavía un consenso tan
sólido como el de PARADISE/SASSI — es una capa de ingeniería en evolución activa, no una
escala psicométrica estabilizada.

### 3.1 Instrumentos que puntúan la respuesta individual directamente

RAGAS (arriba) mide fidelidad a una fuente — pero no es lo único que existe cuando la
pregunta es "¿cómo califico *esta* respuesta puntual del agente?". Hay tres instrumentos
de referencia diseñados exactamente para eso, con más historial de validación que RAGAS:

- **G-Eval** (Liu et al., 2023 — F-156, peer-reviewed EMNLP): el evaluador (un LLM) razona
  paso a paso contra criterios explícitos y asigna un puntaje 1-5 por dimensión (coherencia,
  consistencia, fluidez, relevancia) a **cada respuesta individual**. Es hoy el método de
  LLM-as-judge con mejor correlación documentada con juicio humano entre los comparados en
  su paper original.
- **MQM** (F-157) — ⚠️ **corregido tras pregunta del usuario**: MQM en su forma real es
  específico de calidad de traducción; sus 7 dimensiones (Terminology, Locale Conventions,
  etc.) no mapean a una respuesta conversacional. No es una escala que "también sirva" para
  un chatbot. Lo que sí es real y aplicable es su **método**: anotar cada error por
  categoría y severidad (neutral/menor/mayor/crítico) en vez de un puntaje holístico único
  — un enfoque que investigación reciente ha usado como inspiración para construir marcos
  *nuevos* en otros dominios (código, salud, salidas de LLM en general), no MQM aplicado
  literalmente. Para RIMAC, esto significa **construir una taxonomía de errores propia**
  (ej. error factual de póliza = crítico, error de tono = menor) con la misma lógica de
  severidad ponderada — no adoptar MQM como si fuera un estándar ya hecho para este caso.
- **FED / USR** (Mehri & Eskenazi, 2020 — F-158, peer-reviewed ACL): esquemas de anotación
  turno por turno con dimensiones explícitas, incluida **"Correct"** como una dimensión
  separada de "Fluent" o "Appropriate" — diseñados originalmente para anotación humana,
  hoy replicables también con un LLM como evaluador.

**Diferencia clave con la Familia 1 (usabilidad):** estos tres puntúan **la respuesta**,
no la experiencia agregada del usuario con toda la conversación — son el instrumento
correcto si lo que se quiere es una nota por interacción/respuesta, no una encuesta de
satisfacción post-conversación.

### 3.2 Banco de preguntas estandarizadas + juez LLM (lo que preguntó el usuario)

Sí existe, y tiene nombre: **MT-Bench** (Zheng et al., 2023 — F-159, peer-reviewed
NeurIPS, ampliamente adoptado). La metodología es exactamente la que se preguntó: un
**banco fijo de preguntas** (MT-Bench usa 80, multi-turno, agrupadas por categoría de
habilidad) evaluado por un **LLM juez** que puntúa cada respuesta contra una rúbrica.

**Lo que el propio paper obliga a decir con honestidad, porque lo mide él mismo:** un LLM
juez tiene sesgos documentados — de **posición** (favorece la primera opción en una
comparación), de **verbosidad** (favorece respuestas más largas aunque no sean mejores), y
de **auto-favorecimiento** (tiende a puntuar mejor respuestas parecidas a las que él mismo
generaría). El paper propone mitigarlos con rúbricas explícitas y aleatorizando el orden —
no eliminarlos, mitigarlos. Aplicado a este proyecto: si yo actúo como juez, debo puntuar
contra criterios explícitos y verificables (la taxonomía de severidad de §5, con ejemplos
concretos de "qué cuenta como crítico"), no con un juicio abierto de "¿esto suena bien?" —
así el sesgo de verbosidad/estilo pesa menos.

**Cómo se vería aplicado a RIMAC:** un banco de 15-20 preguntas estandarizadas, cubriendo
los 3 productos Vida ya trabajados en este proyecto (Garantizado, con Devolución,
Flexible) más objeciones comunes y casos límite, cada una con una **respuesta de
referencia** (la respuesta correcta, verificada por alguien de producto) — y luego
comparar la respuesta real del agente contra esa referencia, puntuando con la taxonomía de
severidad de §5. Esto no reemplaza el diagnóstico con muestra real de la Fase 1 (§5) — lo
complementa: la muestra real te dice qué está fallando *en la práctica*; el banco
estandarizado te permite repetir la misma prueba exacta cada vez que cambie el agente, para
saber si una corrección realmente funcionó.

---

## 4. Familia 3 — Frameworks específicos de banca/seguros

- **Howard, Sumbriu & Jonathan (2025) — F-152**, "Unified Framework for Evaluating Chatbot
  Efficiency in Banking and Insurance Industries": el más específico en contenido (combina
  precisión de respuesta + tiempo + calidad de PLN + satisfacción, con métricas
  sectoriales: cumplimiento regulatorio, precisión de recomendación de pólizas, eficiencia
  de reclamos) — pero **su editorial no se pudo verificar como indexada en Scopus/WoS/DOAJ**.
  Se reporta con esa salvedad explícita: contenido plausible, rigor de la revista no
  confirmado.
- **Taylor & Francis, 2024 — F-153** y **MDPI Electronics, 2025 — F-154**: ambos
  peer-reviewed y específicos del sector seguros, pero centrados en *aceptación/adopción*
  del chatbot por parte del asegurado, no en calidad de respuesta per se — complementan,
  no reemplazan, las escalas de la Familia 1-2.

### Tabla resumen de rigurosidad

| Fuente | Tipo de evidencia | Revisión por pares | Peso para el caso RIMAC |
|---|---|---|---|
| PARADISE (F-147) | Framework teórico + validación empírica | 🟢 Sí | 🟡 Medio — marco conceptual, no una escala lista para aplicar directo |
| SASSI (F-148) | Escala psicométrica validada | 🟢 Sí | 🟡 Medio — diseñada para voz, adaptable a texto |
| CUQ (F-149) | Escala psicométrica, N=26 en validación | 🔴 tesis / 🟢 validación posterior | 🟢 Alto — factor de manejo de errores directamente relevante |
| BUS-11 (F-150) | Escala psicométrica re-validada | 🟢 Sí | 🟢 Alto — validada para chatbots de atención al cliente |
| RAGAS (F-151) | Métrica técnica automatizada | ⚠️ No verificado en esta búsqueda | 🟢 Alto — mide directamente alucinación/fidelidad |
| Framework banca-seguros (F-152) | Revisión de literatura + síntesis | ⚠️ No verificable | 🟡 Medio — contenido específico, rigor incierto |

---

## 5. Aplicación recomendada para el caso de RIMAC — plan en 3 fases

No conviene elegir un instrumento pesado (RAGAS, encuesta CUQ) antes de saber **qué tipo de
error** es el que ya se observó — eso es barato de averiguar y evita instrumentar de más.

### Fase 1 — Diagnóstico manual, barato, primero

- Reunir una muestra de **20-30 conversaciones reales** del agente (referencia de tamaño:
  la validación de CUQ usó N=26 — suficiente para un primer diagnóstico, no para
  generalizar con rigor estadístico).
- Que **al menos 2 personas** revisen la muestra de forma independiente (no una sola, para
  poder detectar si hay desacuerdo — un desacuerdo alto entre revisores es señal de que el
  criterio no está claro, no solo de que el agente falla) y clasifiquen cada respuesta con
  errores según esta taxonomía de severidad (adaptada de la lógica de MQM — no MQM en sí,
  ver §3.1):

| Severidad | Peso | Qué es | Ejemplo en un agente de seguros |
|---|---|---|---|
| 🔴 Crítico | 25 | Riesgo regulatorio, legal o de decisión de compra equivocada | Dice mal una condición de cobertura, un plazo, un monto, o afirma algo que contradice el condicionado real |
| 🟠 Mayor | 5 | Rompe la tarea, aunque no sea un dato falso | No entiende la pregunta y no lo reconoce; da una respuesta genérica que no resuelve nada; se queda "trabado" en un loop |
| 🟡 Menor | 1 | No impide resolver la tarea, pero se nota | Tono desalineado, respuesta demasiado larga/corta, formato inconsistente |
| ⚪ Neutral | 0 | Válido, sin problema | — |

- Quien revisa debe **conocer la respuesta correcta** (idealmente alguien de producto/FFVV,
  no un revisor sin contexto de seguros) — sin eso no se puede distinguir un error crítico
  de uno menor con confianza.

**Este paso ya responde lo esencial:** si la mayoría de lo encontrado es 🔴/🟠, el problema
es de exactitud/capacidad — ahí es donde escalar con RAGAS tiene sentido. Si es
mayormente 🟡, el problema es más de percepción/tono — ahí CUQ/BUS-11 rinde más.

### Fase 2 — Escalar el eje que resultó dominante en la Fase 1

- **Si domina 🔴/🟠 (exactitud/capacidad):** correr **RAGAS** sobre un volumen mayor de
  conversaciones (requiere acceso a los documentos/base de conocimiento que el agente usa
  como fuente) para automatizar la detección de alucinación a escala, en vez de seguir
  revisando todo a mano.
- **Si domina 🟡 (percepción/tono):** aplicar **CUQ o BUS-11** como encuesta a usuarios
  reales tras interactuar con el agente — CUQ en particular aísla un factor específico de
  "manejo de errores".
- Es común que ambos ejes aparezcan a la vez — no son excluyentes, pero conviene
  invertir primero donde pesó más en la Fase 1, no en los dos por igual desde el día uno.

### Fase 3 — Monitoreo continuo, no una auditoría única

- **Resolution rate** como métrica operativa continua, con el techo esperado ajustado a la
  baja por tratarse de un sector complejo (seguros) — no comparar contra el 80%+ que se
  reporta como "best-in-class" para chatbots de propósito general (§4, F-155).
- Repetir la Fase 1 (muestreo + taxonomía de severidad) de forma periódica sobre una
  muestra nueva, no solo una vez — un agente puede degradarse silenciosamente si cambia el
  contenido fuente o el modelo subyacente sin que nadie lo note hasta la próxima auditoría.

---

## 6. Limitaciones

- ~~No se accedió al paper original de RAGAS~~ — corregido: se verificó el paper primario
  (EACL 2024) al preparar enlaces para el usuario.
- **Corrección registrada (2026-07-15):** la primera versión de este node presentó MQM
  como un framework "extendido a evaluación de LLMs", lo cual sobreextendía su alcance real
  — MQM es específico de traducción; lo aplicable a chatbots es su método de severidad
  ponderada, no el framework en sí. Corregido en §3.1 tras pregunta directa del usuario.
  Se deja esta nota como registro del error y la corrección, no solo el texto ya arreglado.
- El framework más específico al caso de uso (F-152) tiene rigor editorial no verificable —
  se usa su contenido con esa salvedad explícita, no como fuente A.
- No existe un estándar único, obligatorio o universalmente adoptado por la industria de
  seguros específicamente — lo que existe es una combinación de escalas de HCI generales +
  frameworks técnicos de LLM en evolución activa + literatura sectorial todavía escasa.
- No se investigó qué agente/proveedor tecnológico usa específicamente RIMAC en su sitio —
  esta investigación es sobre los marcos de evaluación disponibles, no un diagnóstico del
  agente real.

---

## Conexiones

- [[metodologias-diseno-sistemas-complejos|Metodologías de diseño para sistemas complejos]] — ese node identifica que el vacío del campo está en la evaluación, no en el diagnóstico; este node aporta instrumentos concretos de medición para cerrarlo.
- [[seguros-comportamiento-mundo-peru|Comportamiento, percepción y valoración frente a
  seguros (Mundo vs. Perú)]] — una mala experiencia con el agente de IA alimenta
  directamente el problema de desconfianza (~48%) ya documentado en ese node; medir y
  corregir errores del agente es una palanca concreta sobre ese número.
- [[tendencias-diseno-innovacion|Tendencias en diseño e innovación: qué tiene impacto real y qué es propuesta]] — sus
  reglas C8 y C11 son criterios de diseño que este node debería incorporar a su instrumentación:
  la explicabilidad genérica **no** calibra la confianza (produce sobre-confianza; lo que la calibra
  es la verificabilidad de la salida), y toda métrica de productividad autorreportada debe
  descontarse frente a la medición objetiva.
