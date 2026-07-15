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

## 5. Aplicación recomendada para el caso de RIMAC

Dado que "tiene errores en la experiencia" es una descripción general, sin especificar si
el error es de exactitud (inventa datos de producto), de manejo de fallos (no sabe qué
decir cuando no entiende), o de tono/percepción:

1. **CUQ o BUS-11** administrado a una muestra de usuarios reales tras interactuar con el
   agente — mide percepción y aísla específicamente el factor de manejo de errores (CUQ).
2. **RAGAS o LLM-as-judge con rúbrica** sobre una muestra de transcripciones reales — mide
   si las respuestas fueron objetivamente fieles a la información de producto de RIMAC, no
   solo si "se sintieron bien". Esto es lo único de las tres familias que puede confirmar o
   descartar alucinación como causa raíz.
3. **Resolution rate** como métrica operativa continua, con el techo esperado ajustado a la
   baja por tratarse de un sector complejo (seguros) — no comparar contra el 80%+ que se
   reporta como "best-in-class" para chatbots de propósito general.

Sin acceso directo al agente de RIMAC para inspeccionar transcripciones reales, no es
posible determinar aquí cuál de los tres ejes (§1) es la causa del problema reportado — es
el paso que sigue antes de elegir la escala definitiva.

---

## 6. Limitaciones

- No se accedió al paper original de RAGAS (arXiv/EACL) — se documentó vía descripciones
  técnicas de terceros (Langfuse, Confident AI). Verificar el paper primario antes de citar
  las métricas con más precisión técnica.
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

- [[seguros-comportamiento-mundo-peru|Comportamiento, percepción y valoración frente a
  seguros (Mundo vs. Perú)]] — una mala experiencia con el agente de IA alimenta
  directamente el problema de desconfianza (~48%) ya documentado en ese node; medir y
  corregir errores del agente es una palanca concreta sobre ese número.
