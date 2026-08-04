# IVR y Voicebots en seguros: origen, rol, desempeño y oportunidades

> Documento de investigación. Fuente persistente y versionada en el repositorio.
> Fecha de elaboración: 2026-07-30 · Versión: v1.0
> Origen: `/trinidad` — investigación de 360° (empírica + social + negocio)
> Pregunta original: ¿cómo nacieron las herramientas IVR/Voicebots, cuál es su rol en las
> empresas de seguros, cómo performan, y cuáles son las oportunidades?
> Fuentes registradas en `research/fuentes/codice.md` (F-393 a F-401).

---

## 0. Resumen ejecutivo (TL;DR)

**Veredicto corto: el IVR/voicebot resuelve bien lo rutinario y barato, y repite —en el
canal de voz— el mismo patrón de riesgo que este proyecto ya documentó para lo 100% digital
en general: falla más en el momento de mayor carga emocional o complejidad (reclamo,
cobertura, negación), no en la consulta simple.** Las tres pistas convergen en esto, aunque
con matices propios de cada una.

- **Pista empírica/teórica:** sólida en el mecanismo de confianza, débil en comparación
  directa voicebot-vs-humano en seguros. Tres papers peer-reviewed convergentes muestran que
  la confianza en un asistente de voz depende del antropomorfismo (voz, entonación,
  personalidad percibida) — la forma, no solo el contenido de la respuesta, es un driver
  causal de si el cliente confía lo suficiente como para dar información sensible o aceptar
  una recomendación.
- **Pista social/mediática:** señal real de fricción, no viral pero consistente — existe una
  cultura extendida de "frases secretas" para forzar el escalamiento a un humano, y una
  categoría de queja específica ("el bot no puede ni terminar su propia despedida") sobre
  voicebots de seguros que fallan antes incluso de que el cliente sea contratante.
- **Pista de negocio:** la más fuerte en volumen de evidencia, la más débil en
  independencia — casi toda la cifra de ROI/containment viene de vendors con interés directo
  en vender la tecnología (mismo patrón de riesgo de eco de cita ya señalado en otras
  investigaciones de este proyecto). Contraevidencia buscada a propósito y encontrada: riesgo
  regulatorio de E&O (un bot dando consejo de cobertura es actividad con licencia), fraude por
  clonación de voz (vector que no existe en texto), y el hecho de que las propias
  aseguradoras grandes (AIG, WR Berkley, Great American) están pidiendo exclusiones de póliza
  para no cubrir responsabilidad derivada de sus propios sistemas de IA.
- **Convergencia con nodes previos del proyecto:** el patrón "falla más en el momento de
  mayor carga, no en la venta/consulta simple" ya está documentado para lo digital en general
  ([[futuro-asesores-seguros-venta-digital]] §3.2) y ahora se repite específicamente en voz.

---

## 1. 🔬 Pista empírica/teórica — origen técnico y mecanismo de confianza

### 1.1 De menús de tonos a IA conversacional: 90 años de evolución, no una novedad

El linaje del IVR es más largo de lo que sugiere el marketing de "voicebots con IA": el
primer intento de síntesis de voz mecánica fue el **Voder** de Bell Labs (Homer Dudley,
años 1930), operado manualmente con un pedal. Los primeros sistemas IVR comerciales
aparecen en los **años 60-70**, y el estándar de menús de tonos DTMF ("presione 1 para...")
se masifica recién en los **90** (AT&T, Nortel). La transición a **voicebots
conversacionales** con reconocimiento de intención vía LLM —donde el cliente puede decir lo
que necesita en lenguaje natural en vez de navegar un árbol de opciones— ocurre recién en
los **2020s** (F-393, 🟡C). Es una evolución de 90+ años en pasos discretos, no un salto
repentino.

### 1.2 El mecanismo de confianza: la voz misma, no solo el contenido

Tres papers peer-reviewed convergen en un mismo mecanismo causal, cada uno desde un ángulo
distinto:

- **Journal of Service Management (Emerald, 2024/2025, F-396, 🟢A):** las características
  paralingüísticas del asistente de voz (entonación, velocidad del habla) generan
  **atracción parasocial**, que a su vez impulsa el antropomorfismo percibido y la
  confianza — la entonación aumenta la atracción específicamente cuando la velocidad del
  habla es alta.
- **ScienceDirect (2023, F-397, 🟢A):** el antropomorfismo (presencia social, voz humana,
  amabilidad percibida) incrementa la **seguridad percibida**, que predice directamente la
  aceptación de transaccionar por voz.
- **SAGE Journals — Fakhimi, Garry & Biggemann (2023, F-398, 🟢A):** las características
  antropomórficas (auditivas, inteligencia cognitiva percibida, manerismos) afectan
  directamente el *engagement* y la confianza del consumidor durante el encuentro de
  servicio.

**Lectura conjunta:** la forma en que suena un voicebot —no solo si responde correctamente—
es un driver causal de si el cliente confía lo suficiente como para dar información
sensible (número de póliza, datos de salud, datos de pago) o aceptar una recomendación de
cobertura. Para un asegurador, esto implica que invertir solo en la precisión del motor de
IA sin invertir en el diseño de la voz/personalidad es optimizar la mitad del problema.

### 1.3 Limitación explícita de esta pista

**No se encontró comparación empírica directa y peer-reviewed de voicebot-vs-humano
específicamente en seguros** (tasa de éxito de tarea, confianza, satisfacción) en esta ronda
de búsqueda — la literatura disponible es sobre asistentes de voz en general (compras,
servicios), aplicada aquí por relevancia de dominio, no por evidencia directa del sector
asegurador.

---

## 2. 📱 Pista social/mediática — fricción real, no viral

**Nivel de instalación social: 💬 moderado — señal consistente, no un pico de controversia.**

No se encontró un evento viral específico sobre voicebots de seguros, pero sí una **cultura
extendida y ya asentada** de resistencia al canal automatizado de voz en general:

- Existe una práctica difundida de **"frases secretas"** (repetir "agente", "representante",
  o incluso maldecir deliberadamente) para forzar el escalamiento desde un IVR/voicebot hacia
  un humano — cobertura de prensa de consumo (Fox News) documenta esto como un fenómeno
  conocido, no un caso aislado (F-395, 🟠D).
- En un foro de nicho de la propia industria de seguros (agentes, no consumidores finales),
  se describe la experiencia con un voicebot de una aseguradora como "un bot que ni siquiera
  puede terminar su propia despedida" — la queja no es sobre precisión de contenido, es sobre
  la mecánica básica de la conversación fallando (F-395, 🟠D).
- Se menciona, sin fuente primaria verificable, el término interno de industria **"Frustration
  AI"** — sistemas diseñados deliberadamente para agotar al cliente hasta que cuelgue. Se
  registra como señal cualitativa encontrada en la búsqueda, explícitamente no confirmada como
  hecho — pero es coherente con la queja recurrente de que los IVR tradicionales son "baratos,
  predecibles y frustrantes para cualquier cosa no trivial".

**Conclusión de esta pista:** no hay una controversia viral que analizar, pero sí una base de
resentimiento social ya instalada y normalizada hacia el canal de voz automatizado — el
listón de tolerancia del usuario hacia un voicebot que falla es más bajo, no más alto, que
hacia un chat que falla, precisamente porque el usuario ya llega con una expectativa negativa
formada por décadas de IVR tradicional.

---

## 3. 📈 Pista de negocio — ROI real pero mayormente autorreportado, con riesgos serios encontrados a propósito

### 3.1 Lo que reportan los proveedores (tratar con cautela — eco de cita entre vendors)

Múltiples proveedores de la misma categoría de producto (Perspective AI, Retell AI, Quiq,
Strada, AnyReach, entre otros) convergen en cifras similares — **alto riesgo de que sea una
sola narrativa de industria repetida, no confirmaciones independientes** (F-394, 🟠D):

| Métrica | Cifra reportada |
|---|---|
| Containment rate en consultas rutinarias (líneas personales) | ~50% |
| Reducción de tiempo de gestión de llamada | 40-60% |
| Mejora en resolución al primer contacto | 25-35% |
| Mejora en CSAT | 15-25% |
| Reducción de costo de call center (caso IBM) | 40% |
| ROI a 3 años (caso Google Contact Center AI) | 331% |

**Matiz importante que sí aparece documentado, y que vale más que cualquier cifra puntual:**
el "containment rate" moderno mide si la IA **resolvió** la consulta a satisfacción del
cliente — a diferencia del antiguo "deflection rate" del IVR tradicional, que solo medía si
la llamada *no llegó* a un humano, sin verificar si el problema real se resolvió. Es un
cambio de métrica honesto que reconoce, implícitamente, que el IVR clásico optimizaba la
métrica equivocada.

**Dónde concentran valor los proveedores que sí especifican caso de uso (no genérico):**
cobertura fuera de horario (un First Notice of Loss capturado a las 2am no se pierde frente a
un competidor), absorción de picos de demanda (eventos climáticos, ventanas de renovación), y
liberar tiempo de agentes licenciados de lecturas de estado repetitivas — no reemplazo de la
conversación compleja, sino descarga del trabajo repetitivo alrededor de ella.

### 3.2 Contraevidencia buscada a propósito (Paso 10 de `marketer`)

Tres hallazgos de riesgo real, específicos del canal de voz, que la narrativa de ROI de los
vendors no menciona:

1. **Riesgo de E&O (errores y omisiones) — el más específico del sector seguros:** las
   conversaciones de cobertura son actividad con licencia regulatoria. Un bot improvisando
   precios o recomendaciones de cobertura es, en palabras de un especialista en riesgo de
   seguros, "un reclamo de E&O calentándose" (F-400, 🟠D). Es un riesgo legal que un chatbot
   de texto comparte, pero que en voz —donde la conversación es menos estructurada y más
   fácil de improvisar fuera de guion— es más agudo.
2. **Fraude por clonación de voz:** tecnología de voz sintética puede recrear una voz de
   forma realista y superar pruebas simples de autenticación biométrica por voz — un vector
   de fraude que **no existe en canales de texto** y que crece en paralelo a la adopción de
   voicebots (F-400, 🟠D).
3. **Las propias aseguradoras no confían en su responsabilidad por IA:** AIG, WR Berkley y
   Great American buscaron aprobación regulatoria para exclusiones de póliza que les permitan
   **negar cobertura de reclamos vinculados al uso de sus propios sistemas de IA** (chatbots
   y agentes incluidos) (F-401, 🟡C). Es una señal de meta-riesgo fuerte: si las aseguradoras
   grandes están pidiendo no ser responsables por lo que hace su propia IA, es una señal de
   que el riesgo regulatorio/legal de este canal es tomado en serio dentro del sector, no solo
   un temor externo de analistas.

### 3.3 Contexto sectorial de riesgo de confianza en IA (no específico de voicebots, pero mismo patrón)

84% de aseguradoras de salud en EE.UU. usa IA para autorizaciones previas; la tasa de
negación inicial de reclamos llegó a 15% en 2026, con rechazos por "validación clínica"
activada por IA subiendo 9% desde 2022; una demanda colectiva alega que negaciones de cuidado
por IA de UnitedHealth contribuyeron a muertes de pacientes (F-399, 🟠D). No es evidencia
directa de voicebots, pero es el mismo patrón de riesgo de confianza en IA de seguros que ya
documenta este proyecto (ver tesis 10 de El Lobo, caso Babylon Health) — el canal cambia, el
riesgo de fondo (sobreclamar capacidad de la IA sin validación suficiente) es el mismo.

---

## 4. ⚖️ Síntesis

**Convergencia real entre las tres pistas:** el patrón de este proyecto sobre lo 100%
digital en seguros —funciona bien en lo simple y rutinario, falla más en el momento de mayor
carga (reclamo, cobertura, negación)— se repite en voz, con un matiz propio del canal: la
**confianza en un voicebot depende de cómo suena, no solo de si responde bien** (pista
empírica), el usuario ya llega desconfiado por décadas de IVR tradicional (pista social), y
el riesgo legal/regulatorio de que un bot de voz improvise consejo de cobertura es tomado en
serio incluso por las propias aseguradoras grandes (pista de negocio).

**Divergencia real, no forzada:** la pista de negocio reporta ROI y containment rate
altos —pero casi toda esa evidencia es autorreportada por vendors con interés directo, el
mismo patrón de riesgo epistémico que este proyecto ya señaló en otras investigaciones de
negocio (LATAM, Bowtie). La pista social y la contraevidencia de negocio (E&O, fraude de voz,
exclusiones de póliza) pintan un cuadro más cauto que el que sugiere el marketing del sector.

**Implicación para el proyecto:** el voicebot/IVR con IA es una herramienta real de
eficiencia operativa —sobre todo para lo repetitivo, fuera de horario, y de alto volumen—
pero no es una vía segura para dar consejo de cobertura o manejar el momento del reclamo sin
supervisión humana, ni un sustituto de resolver la confianza del cliente en el canal.
Conecta directamente con el hallazgo ya documentado en
[[futuro-asesores-seguros-venta-digital]] (§3.2, Bain): los reclamos 100% digitales fallan
33-39% del tiempo y quien escala tarde reporta peor experiencia — un voicebot mal diseñado en
el momento del reclamo puede ser, literalmente, el "self-service primero, humano de rescate
tardío" que ese node ya identifica como la peor de las combinaciones posibles.

---

## 5. Limitaciones

- **La pista de negocio es mayormente autorreportada por vendors** — ninguna fuente de esta
  investigación supera C en la rúbrica de rigurosidad para las cifras de ROI/containment;
  tratar como dirección de industria, no como benchmark auditado.
- **No se encontró comparación empírica directa voicebot-vs-humano específica de seguros** —
  la evidencia de confianza/antropomorfismo es de asistentes de voz en general, aplicada por
  relevancia de dominio.
- **La pista social no tiene un caso viral específico de seguros** que analizar en
  profundidad — la señal es de fricción de fondo, consistente pero no un evento puntual.
- **No se investigó el mercado peruano específicamente** — ni el uso de voicebots por
  aseguradoras peruanas, ni percepción social local del canal telefónico automatizado.
- **F-393 (evolución histórica del IVR) mezcla fuentes de vendor con un artículo de revista
  de perfil no verificado** — tratar la cronología como dirección razonable, no como hecho
  académico certificado en cada fecha puntual.

---

## Conexiones

- [[futuro-asesores-seguros-venta-digital|¿Desaparecerán los asesores de seguros?]] — este
  node confirma en el canal de voz el mismo patrón que ese node documenta en general: lo
  digital falla más en el momento de mayor carga (reclamo), no en la consulta simple.
- [[modelo-churn-renovacion-rimac|Modelo de Churn y Matriz de Renovación de RIMAC]] — ese
  node identifica que RIMAC ya tiene ventanas de gestión anticipada bien diseñadas (2-4 meses
  antes de la fuga/renovación) pero no la causa raíz de la cancelación voluntaria; un
  voicebot mal diseñado en esa ventana de contacto podría generar la fricción exacta que
  aumenta, en vez de reducir, esa cancelación.
- `research/lobo/opinion_experto.md` — tesis nueva traduce estos hallazgos a oportunidades y
  riesgos de negocio concretos para RIMAC.
