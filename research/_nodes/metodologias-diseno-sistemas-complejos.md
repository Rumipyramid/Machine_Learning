# Metodologías de diseño para sistemas complejos

> Documento de investigación. Fuente persistente y versionada en el repositorio.
> Fecha de elaboración: 2026-08-05 · Versión: v1.0
> Origen: investigación de 360° (pista empírica/teórica + social/mediática + de negocio)
> Pregunta original: ¿cuáles son las mejores metodologías de diseño para sistemas complejos?
> Fuentes registradas en `research/fuentes/codice.md` (F-469 a F-482).

---

## 0. Resumen ejecutivo (TL;DR)

**Veredicto corto: la pregunta "¿cuál es la mejor metodología?" está mal planteada, y la
evidencia lo muestra desde tres direcciones distintas.**

- **Pista empírica:** la metodología más establecida para sistemas complejos (Soft Systems
  Methodology, 50 años de uso) tiene una revisión de alcance de 49 estudios en salud que
  encuentra algo demoledor: se usa mayormente para **entender el problema y proponer mejoras,
  y mucho menos para implementarlas y evaluarlas** (F-469, 🟢A). Casi nunca llega a la fase
  donde se podría medir si funcionó. El marco más popular para *clasificar* complejidad
  (Cynefin) **no tiene prueba científica de validez** y su asignación de dominio es subjetiva
  (F-472).
- **Pista social:** la crítica más dura al design thinking viene de dentro del campo — un
  socio de **IDEO**, la firma que lo popularizó, lo llama "teatro de la innovación" cuando se
  usa sin estrategia ni seguimiento de impacto (F-477). El gremio advierte contra confundir
  **"fluidez en frameworks" con "fluidez en diseño"** (F-478).
- **Pista de negocio:** el dato que descoloca. Solo 30% de los programas de transformación
  cumple plazo, presupuesto y alcance, y esa tasa lleva años estancada. Pero el predictor que
  reporta la literatura de consultoría **no es la metodología de diseño** — es la gobernanza y
  la consistencia del liderazgo (F-482).

**Convergencia de las tres pistas:** el cuello de botella no está en elegir el marco correcto.
Está en **llegar a la implementación y medir**. Las tres pistas, con criterios de validez
distintos, apuntan al mismo lugar.

---

## 1. 🔬 Pista empírica/teórica

### 1.1 La distinción que sí cambia el método: complicado ≠ complejo

Es la única parte de esta investigación donde la teoría es clara y operativa. Un sistema
**complicado** y uno **complejo** no difieren en tamaño ni en dificultad, sino en la relación
causa-efecto:

| | Complicado | Complejo |
|---|---|---|
| Causa-efecto | Cognoscible con análisis | No cognoscible por adelantado |
| Diferencia real | Solo **cuánto tiempo y energía** cuesta descubrir la estructura | Interacciones no lineales: cambios menores producen consecuencias desproporcionadas |
| Quién resuelve | Expertos que analizan y definen el proceso | Nadie por adelantado |
| Cómo aparece la solución | Se diseña y se impone | **Emerge de las circunstancias** |

La formulación precisa viene de la extensión de Cynefin a gestión de proyectos (F-473, 🔵B):
en el dominio complejo *"las soluciones surgen de las circunstancias en vez de imponerse"*.

**Por qué importa para el método.** Si esa frase es correcta, en un sistema complejo **no se
diseña la solución — se diseñan las condiciones para que aparezca**. Eso descalifica de entrada
cualquier método que prometa llegar a la respuesta correcta mediante análisis suficiente, y
explica por qué las metodologías serias de este campo se parecen más a protocolos de
aprendizaje que a procesos de diseño.

**Contraevidencia sobre el propio marco:** Cynefin se publicó como herramienta de decisión
gerencial y hoy se usa como heurística de enseñanza, pero **la prueba científica de su validez
está pendiente**, la evidencia empírica en contextos corporativos es limitada, y **la
asignación de dominio es subjetiva** — equipos distintos clasifican la misma situación en
dominios distintos (F-472, 🟠D). Es útil como **lenguaje común**, no como criterio de decisión.

### 1.2 El hallazgo más importante: las metodologías no llegan a la evaluación

Una revisión de alcance de 49 estudios sobre 50 años de uso de **Soft Systems Methodology** en
salud (F-469, 🟢A — la fuente de mayor rigor de esta investigación) encuentra tres cosas:

1. El uso es **inconsistente**: se aparta de la visión original de Checkland, aplica
   herramientas distintas e involucra stakeholders de forma idiosincrática.
2. Se usó sobre todo para **entender la situación problemática y sugerir mejoras**.
3. **Mucho menos para implementar y evaluar esas mejoras.**

Ese tercer punto es el hallazgo central de toda esta investigación. La metodología más
establecida del campo, con medio siglo de aplicación documentada, **casi nunca llega a la fase
donde podría demostrarse que funciona**.

**Matiz que evita una lectura injusta:** SSM declara explícitamente que sus modelos
conceptuales son **herramientas para facilitar el debate, no hipótesis falsables** (Checkland,
F-470, 🔵B). Eso es una decisión de diseño del método, no un defecto oculto — pero implica que
**exigirle evidencia de efectividad con el estándar de las ciencias empíricas es una categoría
equivocada**. Hay que saberlo antes de pedirle pruebas que por construcción no puede dar.

### 1.3 Lo que sí tiene evidencia (con salvedades)

| Metodología | Evidencia encontrada | Rigor |
|---|---|---|
| Dinámica de sistemas basada en comunidad | Revisión sistemática sobre intervenciones de prevención (F-480) | 🟢 A |
| Pensamiento sistémico en salud | Correlación con competencias de seguridad del paciente; revisión de alcance de 19 estudios en 15 países (F-479) | 🔵 B |
| Viable System Model (Beer) | 25 casos revisados, incluyendo empresa global de software de 9.000 empleados (F-481) | 🟡 C |
| Wardley mapping | Casos en proyectos de gobierno del Reino Unido y manufactura de pequeña escala (F-481) | 🟡 C |
| Vanguard Method (Seddon) | Aplicado en 11 países; número especial de revista arbitrada (F-474) | 🔵 B |

**Advertencia sobre la fila de pensamiento sistémico en salud:** son estudios **transversales
correlacionales**, varios con autorreporte de percepción. Miden asociación, no efecto causal de
una intervención metodológica. No confundir "los enfermeros con más pensamiento sistémico
reportan mejores competencias" con "entrenar pensamiento sistémico mejora la seguridad".

### 1.4 Contraevidencia buscada a propósito

**Crítica al Vanguard Method (Jackson, F-475, 🔵B).** Al definir el sistema **desde el cliente
del servicio**, permite rediseñar subsistemas sin atender los sistemas macro hasta que estos
aparecen como restricción — lo que puede producir **suboptimización del sistema mayor**. Un
servicio se vuelve excelente a costa del conjunto.

Es la crítica más relevante para un equipo que rediseña journeys dentro de una organización
grande: **se puede mejorar la experiencia de venta y empeorar la economía del negocio**, y el
método no lo advertiría.

---

## 2. 📱 Pista social/mediática

**Nivel de instalación social: 🔥 alto — con la particularidad de que la crítica más fuerte
viene de dentro.**

No es una controversia de terceros: son los propios practicantes de élite del campo los que
critican.

- **Natasha Jen (socia de Pentagram), F-477:** el design thinking se volvió *"un culto que cree
  ingenuamente que puede crear cambio en sistemas grandes vía un método reductivo"*. Reducir la
  resolución creativa de problemas a cinco pasos **hace parecer fácil lo que no lo es**.
- **Michael Hendrix (socio de IDEO), F-477:** reconoce el uso superficial del método como
  **"teatro de la innovación"** — sin historia ni estrategia que las una y sin seguimiento de
  impacto, las iniciativas terminan **creando apariencia en vez de sustancia**.

**Que la crítica venga de IDEO es lo que le da peso.** No es un detractor externo: es la firma
que popularizó el método señalando cómo se degrada en la práctica.

- **Sentimiento del gremio (F-478, 🟠D):** a medida que se multiplicaron las certificaciones,
  algunos equipos **aprendieron rituales sin desarrollar las habilidades duras** de
  investigación, síntesis y criterio. La advertencia recurrente: no confundir **"fluidez en
  frameworks" con "fluidez en diseño"**.

**Conclusión de esta pista:** la crítica social no dice que estos métodos no sirvan. Dice que
**se volvieron performativos** — que la ejecución visible del ritual (talleres, post-its,
mapas) reemplazó al trabajo difícil que el ritual debía ordenar.

---

## 3. 📈 Pista de negocio

### 3.1 El dato que reordena la pregunta

| Métrica | Valor |
|---|---|
| Programas tecnológicos grandes que cumplen plazo, presupuesto y alcance | **30%** |
| Tasa de éxito de transformaciones (estancada hace años) | **30-35%** |
| Mejora de éxito con modelos de gobernanza fuertes | **+38%** |
| Mejora de velocidad de entrega con gobernanza fuerte | **+25%** |

Fuente: BCG / McKinsey vía cobertura de consultoría (F-482, 🟡C — encuestas propias no
auditables, posible eco de cita entre firmas).

**Lo relevante no son las cifras exactas — es qué variable aparece como predictor.** La propia
literatura de consultoría concluye que el fracaso *"rara vez es un fallo de diseño: los planes
suelen ser buenos, los marcos suelen ser sólidos, la gente suele ser capaz"*. Es fallo de
**alineamiento, propiedad y consistencia de liderazgo**.

Y una observación que vale más que las cifras: *"el proceso empieza gradualmente a llenar
vacíos que el liderazgo debería atender — los planes detallados compensan prioridades poco
claras, los foros de gobernanza sustituyen la toma de decisiones, las métricas reemplazan
conversaciones significativas"*. **Es exactamente el mecanismo del "teatro de la innovación" de
la pista social, visto desde el lado del negocio.**

### 3.2 Por qué los pilotos no escalan — la explicación operativa

El aporte más accionable de esta pista viene del service design (F-476, 🟡C, citando a Birgit
Mager, autoridad académica del campo):

> *"No puedes cambiar el frontstage si no impactas el backstage."*
> **La mayoría de las iniciativas de innovación fracasan al escalar porque el backstage nunca
> se rediseñó.**

De ahí la distinción operativa entre dos cosas que suelen confundirse:

| | Qué diseña |
|---|---|
| **Design thinking** | La experiencia del usuario (frontstage) |
| **Service design** | La experiencia **y el sistema de entrega que la produce** (backstage) |

El **service blueprint** es el único método que mapea en un solo diagrama las acciones del
cliente, las del empleado de cara al cliente, los procesos de trastienda y los sistemas de
soporte. Es la herramienta que fuerza a mirar lo que no se ve.

### 3.3 Failure demand: el único indicador contable del campo

El Vanguard Method aporta un concepto que, a diferencia de casi todo lo demás en esta
investigación, **se puede contar**: **"failure demand"** — la demanda que existe *solo porque
el sistema falló antes* (rellamadas, reclamos, retrabajos, escalamientos) (F-474, 🔵B).

Separar demanda de valor de demanda de falla convierte una discusión metodológica en una
medición. Para una operación con centro de contacto, es directamente instrumentable.

---

## 4. ⚖️ Síntesis

**Convergencia (las tres pistas, con criterios distintos, dicen lo mismo):** el problema no es
la elección de metodología. Es que **el trabajo se detiene antes de la implementación y la
medición**. La pista empírica lo muestra en 49 estudios de SSM que diagnostican pero no
evalúan; la social lo llama teatro de la innovación; la de negocio lo mide como una tasa de
éxito estancada en 30% donde el predictor es gobernanza, no método.

**Divergencia real, no forzada:** la pista de negocio sugiere que la gobernanza importa más que
el método, pero esa evidencia es de consultoras (🟡C) con posible eco de cita entre firmas —
mientras que la crítica metodológica de la pista empírica se apoya en una revisión sistemática
(🟢A). **No se pueden pesar en la misma balanza.** Lo honesto es decir que la evidencia fuerte
muestra un vacío de evaluación, y la evidencia débil sugiere dónde estaría la causa.

**Respuesta directa a la pregunta original.** No hay una "mejor metodología". Hay un criterio
de selección según qué se necesita hacer:

| Si el problema es… | Sirve | Por qué |
|---|---|---|
| Clasificar en qué terreno estás antes de elegir método | Cynefin, como **lenguaje común** | Útil para alinear al equipo; ⚠️ no como criterio de decisión — la asignación de dominio es subjetiva y sin validación |
| Actores que no coinciden en cuál es el problema | Soft Systems Methodology | Está diseñado exactamente para eso; ⚠️ tiene que llegar a implementación o se queda en diagnóstico |
| Un piloto que funciona pero no escala | **Service blueprint** | Es el único que obliga a rediseñar el backstage, que es donde muere el escalamiento |
| Medir cuánto del trabajo es desperdicio del propio sistema | **Failure demand** (Vanguard) | El único indicador contable del campo |
| Entender si la organización puede sostener el cambio | Viable System Model | Diagnóstico estructural, no de experiencia |
| Decidir qué construir propio y qué comprar | Wardley mapping | Posiciona componentes por madurez evolutiva |

**La recomendación de fondo:** dado que las tres pistas convergen en que el vacío está en la
implementación y la medición, **la decisión de mayor impacto no es qué método adoptar, sino
comprometerse por adelantado a medir el resultado del rediseño** — con un indicador definido
antes de empezar. Cualquiera de los métodos de arriba funciona mejor con esa disciplina que el
mejor de ellos sin ella.

---

## 5. Aplicación al contexto del equipo

El equipo trabaja en sistemas socio-técnicos con muchos actores (rediseño de experiencia de
venta, modelos de atención en salud, sistemas de research ops), no en productos digitales
aislados. Cuatro implicaciones directas:

1. **El riesgo de suboptimización es real y aplica hoy.** La crítica de Jackson al Vanguard
   Method (F-475) describe exactamente el riesgo de rediseñar un journey de venta o de
   renovación sin tocar la estructura que lo condiciona: **se mejora la experiencia y se
   empeora la economía**. Vale hacerlo explícito como riesgo en cualquier rediseño de journey.
2. **El backstage es el punto de falla predecible al escalar.** Si un piloto de rediseño de
   venta o de atención funciona en 10 asesores y no escala, la hipótesis por defecto —según
   F-476— es que **el backstage nunca se rediseñó**, no que el frontstage estuviera mal.
3. **Failure demand es instrumentable ya.** En una operación con centro de contacto y gestión
   de renovaciones, separar demanda de valor de demanda de falla es medible con lo que ya
   existe, y convierte una discusión de método en un número.
4. **La disciplina de medición que el campo no tiene, este equipo sí puede tener.** El hallazgo
   de F-469 —que las metodologías rara vez llegan a evaluar— es precisamente el vacío que un
   sistema de research ops con trazabilidad de evidencia y ciclos de validación está diseñado
   para cerrar. Es una ventaja disponible, no una aspiración.

---

## 6. Limitaciones

- **La pista de negocio es toda 🟡C.** Ninguna cifra de tasa de éxito de transformación viene
  de un estudio auditado; son encuestas propias de consultoras con posible eco de cita entre
  firmas. Tratar como dirección, no como benchmark.
- **La evidencia de efectividad de pensamiento sistémico es correlacional** (F-479), en varios
  casos con autorreporte de percepción. No hay ensayos controlados que midan si adoptar una
  metodología de sistemas mejora resultados frente a no adoptarla.
- **Sesgo de parte en las fuentes de metodologías específicas.** El número especial sobre
  Vanguard (F-474) es mayormente de practicantes del propio método; los casos de VSM y Wardley
  provienen de quienes los aplican. Se declara, no se descarta.
- **No se encontró comparación directa entre metodologías.** Ningún estudio compara SSM vs.
  service design vs. VSM sobre el mismo problema. La tabla de selección de §4 es **razonamiento
  sobre para qué fue diseñada cada una**, no evidencia comparativa.
- **F-472 (crítica a Cynefin) es agregada**, sin una fuente primaria única verificada en esta
  sesión — la crítica de falta de validación es consistente y ampliamente repetida, pero
  convendría rastrear el trabajo original antes de citarla como afirmación fuerte.
- **No se investigaron** Theory U, design for policy, MBSE ni safe-to-fail probes con la misma
  profundidad; quedaron fuera del alcance de esta ronda.

---

## Conexiones

- [[behavioral-design-estado-disciplina|Estado del behavioral design como disciplina]] — ese
  node documenta el mismo patrón en la disciplina hermana: marcos populares cuyo efecto
  promedio se desploma al corregir sesgo de publicación. La lección se repite aquí: **adopción
  no es evidencia**.
- [[modelo-salud-ia-farmacias-peru|Modelo de triage con IA + farmacias]] — caso vivo de sistema
  socio-técnico complejo del proyecto, donde aplica directamente el criterio de §5 (backstage,
  failure demand, riesgo de suboptimización).
- [[evaluacion-calidad-agentes-conversacionales-ia|Evaluación de calidad de agentes de IA]] —
  complementa el vacío que este node identifica: cómo medir, que es exactamente donde las
  metodologías de sistemas se quedan cortas.
