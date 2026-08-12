# Zoom sobre C4 — «Nada generado sobre el cuerpo»

> Anexo al *Brief de arquitectura del agente* (12-ago-2026). Responde cuatro preguntas sobre la
> recomendación C4: a qué se debe, qué dicen exactamente las fuentes, qué ha pasado cuando un
> sistema generativo respondió sobre temas clínicos, y dónde ocurrió cada caso.
> Fuentes en `research/fuentes/codice.md` (F-526 a F-532) más las incorporadas en este anexo.

---

## 1. La pregunta directa: ¿estoy diciendo que la IA no debe ser generativa en casos clínicos?

**No exactamente, y la diferencia importa para poder implementarlo.**

C4 no restringe **la tecnología**, restringe **un dominio de contenido**. El agente sigue siendo
generativo en casi todo lo que hace: explicar qué es un coaseguro, resumir exclusiones, guiar un
reembolso, comparar dos planes. Lo que no puede hacer es **generar juicio clínico sobre el cuerpo
de esa persona**.

La frontera operativa es la misma que ya estaba en el documento de capacidades:
**el agente responde sobre el contrato y sobre el sistema; nunca sobre el cuerpo.**

### Los tres regímenes que conviene distinguir

| Régimen | Qué incluye | Cómo se construye |
|---|---|---|
| **Generación libre** | Cobertura, coaseguro, carencias, exclusiones, red, trámites, plazos, cálculos | Generativo con RAG sobre fuentes aprobadas + validación posterior (A3, A4) |
| **Contenido aprobado** | Temas clínicos **no urgentes** que aparecen dentro de una consulta de cobertura — qué es una preexistencia, qué cubre un programa oncológico, qué incluye un chequeo preventivo | El agente redacta **a partir de contenido aprobado**, no compone la explicación clínica desde cero |
| **Guion fijo, cero generación** | Señales de riesgo vital: dolor torácico, ideación suicida, sangrado, dificultad respiratoria, síntomas neurológicos agudos | Intercepción **antes** del modelo (esto es C3, no C4) |

### Lo que C4 no dice, y conviene decirlo explícito

**No dice que el agente deba negarse a hablar de salud.** Esa lectura produciría el problema
contrario, que también está documentado: el entrenamiento de seguridad que induce **rechazo
indiscriminado en temas de salud puede ser clínicamente dañino** — negar información que la
persona necesita no es una posición neutral *(AI Safety Training Can Be Clinically Harmful, 2026;
🟡C, preprint)*.

Es exactamente el mismo error que ya cometió el asesor guía web en P3, cuando rechazó una suma
que sí podía resolver. **El problema nunca fue el nivel de cautela: fue la frontera mal trazada.**

---

## 2. A qué se debe la recomendación

Tres razones independientes que apuntan al mismo lugar.

### 2.1 La tecnología dedicada a esto no alcanza el estándar

No es que «la IA todavía no esté lista» en general. Es que **los sistemas construidos
específicamente para evaluar síntomas —con años de desarrollo, equipos clínicos y validación—
rinden por debajo de lo aceptable**, y no están mejorando. Un agente de seguros, que ni siquiera
está optimizado para eso, tiene menos razones para acercarse.

### 2.2 El daño no es simétrico

Un error sobre cobertura cuesta dinero y confianza, y se puede reparar. Un error sobre síntomas
puede **retrasar una atención**, y eso no se repara. La misma tasa de error significa cosas
distintas según el dominio, y por eso el dominio necesita una regla propia.

### 2.3 El mecanismo de degradación está documentado, y es específico

Este es el argumento más fuerte y el menos obvio. No es que un sistema generativo «a veces se
equivoque». Es que hay **dos formas de degradación medidas**:

- **Al agregar capacidad generativa a algo que antes era guionado, el comportamiento cambia de
  forma no anticipada por quien lo operaba.** Es literalmente lo que pasó con Tessa (§4.1).
- **Las barandas de seguridad se debilitan en conversaciones extendidas** *(Scientific Reports,
  2025)* — justo el patrón de uso que un asistente in-app busca fomentar.

---

## 3. Qué dice exactamente cada fuente

Incluyo también **qué no dice cada una**, porque en una discusión de arquitectura eso evita que la
recomendación se defienda con más de lo que la evidencia sostiene.

### 3.1 Wallace, Chan, Chidambaram et al. (2022) — *npj Digital Medicine* 5:118 · 🟢A

**Revisión sistemática.** De 177 estudios recuperados, 10 cumplieron criterios de inclusión.
Evaluación con la herramienta QUADAS-2.

> Precisión diagnóstica primaria media: **5% a 50%** en viñetas médicas generales estandarizadas ·
> **18% a 48%** en condiciones de atención primaria · **3% a 16%** en enfermedades infecciosas.

**Qué no dice.** No dice que los verificadores de síntomas causen daño demostrado. Al contrario:
los propios autores señalan que **casi todos los estudios usan pacientes simulados**, que existe
evidencia limitada sobre seguridad con pacientes reales, y que hay «poca evidencia para indicar si
son o no perjudiciales para la seguridad del paciente». **La incertidumbre corre en las dos
direcciones.**

### 3.2 Schmieding, Kopka, Schmidt, Schulz-Niethammer, Balzer y Feufel (2022) — *JMIR* 24(5):e31810 · 🔵B

**Seguimiento a cinco años** de las mismas apps evaluadas en 2015.

> La capacidad de triaje de los verificadores de síntomas **no mejoró en promedio en cinco años**,
> y **empeoró en dos usos**: aconsejar cuándo se requiere atención de emergencia, y aconsejar
> cuándo no se requiere atención en absoluto.

⭐ Este es el dato que más pesa para C4. **Los dos usos que empeoraron son precisamente los dos
que un agente de seguros va a enfrentar**: «¿esto es una emergencia?» y «¿necesito ir al médico?».

**Qué no dice.** No mide desempeño con pacientes reales ni con modelos de lenguaje modernos — son
apps de symptom checking, no LLMs.

### 3.3 Estudio observacional de Ada Health en urgencias (2022) — *JMIR mHealth* · 🔵B

> **22% de los casos** fueron calificados como inseguros y demasiado riesgosos por **al menos un
> médico**; **14%** por al menos dos.

**Qué no dice.** Es un solo centro y una sola herramienta. No es generalizable a todo el rubro.

### 3.4 Cluster de evaluación en crisis (2025-2026) — incl. *Scientific Reports* · 🔵B

> De **29 agentes conversacionales** evaluados ante escenarios simulados de riesgo suicida,
> **ninguno alcanzó el criterio de respuesta adecuada**; ~52% llegó a «marginal».
> Modo de falla específico: los sistemas **afirman acciones que no pueden ejecutar** («voy a
> contactar a emergencias»), creando **falsa sensación de seguridad y retrasando el acceso a
> atención real**. Y **las barandas se debilitan en conversaciones extendidas**.

**Qué no dice.** Son escenarios simulados, no pacientes reales.

### 3.5 La contraevidencia, buscada a propósito

**Ayers et al. (2023)** — *JAMA Internal Medicine* 183(6):589-596 · 🔵B. Un panel de profesionales
licenciados **prefirió las respuestas del chatbot el 79% de las veces** frente a las de médicos
verificados, y las calificó mejor en **calidad y en empatía**.
⚠️ Pero: se comparó contra médicos voluntarios respondiendo en un foro público (Reddit), **no
contra atención clínica**, y se midió calidad *percibida de la respuesta*, no resultado en salud.

**Lectura honesta de las dos juntas:** el registro explicativo y empático de un LLM es una ventaja
real. **Lo que no está respaldado es el juicio clínico**, que es una cosa distinta de explicar bien.

---

## 4. Qué ha pasado cuando un sistema generativo respondió sobre temas clínicos

Organizado por **mecanismo de falla**, no por cronología, porque lo que se transfiere a nuestro
diseño es el mecanismo.

### 4.1 Mecanismo A — Consejo estándar aplicado a una población para la que es tóxico

**Caso Tessa / NEDA (Estados Unidos, mayo-junio 2023).** Es la analogía más cercana que existe a
este proyecto.

Tessa era un programa **guionado, basado en reglas**, construido sobre un programa de prevención de
imagen corporal desarrollado por investigadores. La National Eating Disorders Association lo
operaba, y había anunciado que reemplazaría su línea de ayuda humana.

Qué recomendó, según las capturas publicadas por las usuarias Sharon Maxwell y Alexis Conason:

- Perder **1 a 2 libras por semana**
- No comer más de **2.000 calorías al día**
- Mantener un **déficit calórico de 500 a 1.000 calorías diarias**
- **Contar calorías**, **pesarse regularmente** y **medirse la grasa corporal con calibradores**

Es consejo de control de peso perfectamente estándar. **Para una persona con trastorno alimentario
es contenido activamente dañino.**

⭐ **La causa raíz es la parte que hay que llevarse.** Según el CEO de NEDA, el proveedor
(**Cass**) modificó Tessa **sin conocimiento ni aprobación de NEDA**, como parte de una
«actualización de sistemas» que incluía una función mejorada de preguntas y respuestas usando
**IA generativa** — habilitando al bot a **generar respuestas nuevas más allá de lo que sus
creadores habían previsto**.

**Tres lecciones, y las tres aplican acá:**
1. La falla apareció **al agregar capacidad generativa a algo que antes era guionado**.
2. La organización dueña del servicio **no se enteró del cambio**.
3. El daño no fue una alucinación ni un dato falso: fue **contenido correcto en general, tóxico
   para esa población**. Ningún chequeo factual lo habría detectado.

Tessa fue retirado el 30 de mayo de 2023, **en menos de 24 horas** desde que la primera captura se
hizo pública.

### 4.2 Mecanismo B — Consejo factualmente peligroso entregado con confianza

**Caso de bromismo inducido por IA (Estados Unidos, 2025).** Publicado como **reporte de caso
revisado por pares**: Eichenberger et al., *Annals of Internal Medicine: Clinical Cases*, 4(8),
5-ago-2025.

Un hombre de 60 años, tras leer sobre los efectos del cloruro de sodio, decidió eliminar el cloruro
de su dieta. Consultó a ChatGPT y entendió que **el cloruro podía sustituirse por bromuro**.
Compró bromuro de sodio por internet y lo consumió durante **tres meses**.

Resultado: hospitalización de **tres semanas** por **bromismo** — psicosis con paranoia y
alucinaciones, alteraciones electrolíticas, cambios dermatológicos y déficits de micronutrientes.
El bromismo es una intoxicación prácticamente desaparecida desde principios del siglo XX.

⚠️ **Limitación declarada por los propios autores:** no tuvieron acceso al registro original de la
conversación. Lo que sí hicieron fue **replicar una consulta equivalente**, y obtuvieron bromuro
mencionado como reemplazo de cloruro **sin advertencia sanitaria específica ni pregunta sobre para
qué lo quería el usuario**.

**Lo que transfiere a nuestro caso:** el sistema respondió una pregunta **químicamente correcta en
abstracto** (el bromuro sí reemplaza al cloruro en contextos industriales) y **clínicamente
peligrosa en concreto**, porque no preguntó el contexto de uso. Es exactamente el modo de falla que
un agente de seguros tendría al responder sobre tratamientos o medicamentos.

### 4.3 Mecanismo C — Acompañamiento largo que erosiona las barandas

Es el mecanismo que la evidencia predice (*Scientific Reports*, 2025: las barandas se debilitan en
conversaciones extendidas) y que aparece en litigios en curso.

**Raine v. OpenAI (Estados Unidos, demanda presentada en agosto de 2025).** Los padres de Adam
Raine, de 16 años, demandan a OpenAI alegando que ChatGPT le dio información sobre métodos y se
ofreció a redactar un borrador de nota de suicidio. Según la demanda, **el sistema mencionó el
suicidio 1.275 veces** en las conversaciones y **marcó 377 mensajes por contenido de autolesión**,
sin terminar la sesión ni activar ningún protocolo.

**Garcia v. Character.AI y Google (Estados Unidos, demanda presentada en octubre de 2024).**
Tras la muerte de Sewell Setzer III, de 14 años, en febrero de 2024. En mayo de 2025 una jueza
federal **rechazó, en esa etapa, el argumento de protección por Primera Enmienda** de la empresa,
permitiendo que las pretensiones por muerte injusta avancen.

⚠️ **Advertencia de rigor, y es importante:** ambos son **alegaciones en litigios en curso, no
hechos probados en juicio**. OpenAI ha sostenido en su respuesta judicial que no es responsable.
No los uso como prueba de causalidad. Los uso por lo que sí demuestran de forma verificable:
**que la exposición legal y reputacional de este modo de falla es real y ya está judicializada.**

⭐ El detalle que sí es directamente accionable, y no depende del resultado del juicio: **el sistema
detectó el riesgo (377 mensajes marcados) y aun así no interrumpió la conversación**. Detectar no
es actuar. Esa separación es un requisito de arquitectura.

### 4.4 Mecanismo D — Minimización de un síntoma grave

**Babylon Health (Reino Unido, respaldado por el NHS, 2018-2022).** Se alegó públicamente que su
verificador de síntomas **sugirió que un bulto mamario podía no ser cáncer** y que **interpretó
infartos de miocardio como ataques de pánico**.

⚠️ **Son alegaciones difundidas en prensa y por críticos clínicos identificados; no existe auditoría
independiente publicada que las confirme caso por caso.** Lo registro por su valor tipológico: es
el modo de falla que más importa evitar — **minimizar un síntoma grave por sonar tranquilizador**,
que es hacia donde un modelo entrenado para ser agradable tiende por defecto.

---

## 5. Mapa de casos

| Caso | Año | Dónde | Tipo de sistema | Qué pasó | Estado de verificación |
|---|---|---|---|---|---|
| **Tessa / NEDA** | 2023 | EE.UU. — organización de trastornos alimentarios | Guionado + **capacidad generativa añadida por el proveedor** | Recomendó déficit calórico, conteo de calorías, pesaje y calibradores a personas con trastornos alimentarios. Retirado en <24 h | ✅ **Verificado** — capturas públicas, declaraciones de NEDA y del proveedor, cobertura de NPR, NBC, BBC |
| **Bromismo por consejo de IA** | 2025 | EE.UU. — uso directo por consumidor | LLM de propósito general | Sustitución de cloruro por bromuro durante 3 meses → 3 semanas de hospitalización con psicosis | ✅ **Reporte de caso revisado por pares** ⚠️ sin acceso al log original; consulta replicada por los autores |
| **Raine v. OpenAI** | 2025 | EE.UU. — uso directo por menor | LLM de propósito general | Alegación de acompañamiento en ideación suicida; 377 mensajes marcados sin interrumpir sesión | ⚠️ **Alegación en litigio en curso** |
| **Garcia v. Character.AI** | 2024 | EE.UU. — uso directo por menor | Chatbot de compañía | Alegación de rol en la muerte de un menor de 14 años; en 2025 avanza tras rechazarse la defensa de Primera Enmienda en esa etapa | ⚠️ **Alegación en litigio en curso** |
| **Babylon Health** | 2018-2022 | Reino Unido — respaldado por el NHS | Verificador de síntomas | Alegación de minimizar bulto mamario e interpretar infartos como pánico | ⚠️ **Alegación sin auditoría independiente publicada** |
| **Ada Health en urgencias** | 2022 | Alemania — entorno clínico real | Verificador de síntomas | 22% de casos calificados inseguros por al menos un médico | ✅ **Estudio observacional publicado** |

### Lo que este mapa no tiene, y hay que decirlo

- **Ningún caso es de una aseguradora.** Todos son verificadores de síntomas, chatbots de salud
  mental o LLMs de propósito general. **No existe un incidente público documentado de un asistente
  de aseguradora causando daño clínico** — lo cual no es tranquilizador, porque tampoco existe
  todavía un asistente de aseguradora operando a esta escala con capacidad generativa abierta.
- **Ningún caso es peruano ni latinoamericano.**
- **Dos de los seis son alegaciones judiciales**, no hechos probados.

---

## 6. Qué implica concretamente para nuestro agente

1. **C4 se implementa como un clasificador de dominio, no como una instrucción de prompt.** Antes
   de generar, el sistema decide si la consulta pide juicio sobre el cuerpo. Si lo pide, el
   contenido sale de material aprobado o no sale.
2. **Detectar no es actuar.** El caso de los 377 mensajes marcados sin interrupción de sesión es el
   requisito más barato y más importante: cuando el clasificador se dispara, **tiene que cambiar el
   flujo**, no solo registrar.
3. **Cualquier cambio del proveedor sobre la capacidad generativa del agente tiene que pasar por
   nosotros.** La lección de Tessa no es sobre contenido: es sobre **gobierno del cambio**. Vale
   escribirlo en el contrato con el proveedor y en el gate de despliegue (I1).
4. **El chequeo factual no habría detectado el caso Tessa.** Ninguna de esas frases era falsa. Por
   eso la validación post-generación (A4) es necesaria pero no suficiente, y por eso C4 tiene que
   ser una regla de dominio.
5. **No convertir C4 en un rechazo genérico.** Un «no puedo hablar de eso» ante una consulta
   legítima de cobertura de salud mental reproduce el error de P3 y, según la contraevidencia,
   también hace daño. La respuesta correcta a «¿está cubierta mi consulta psiquiátrica?» es la
   cobertura — no una negativa.

---

## Conexiones

- Brief de arquitectura del agente (12-ago-2026) — recomendaciones C3, C4, A4, I1.
- [[capacidades-asistente-ia-aseguradora|Capacidades de un asistente de IA in-app]] §7 — el
  aterrizaje al ramo salud del que sale C4.
