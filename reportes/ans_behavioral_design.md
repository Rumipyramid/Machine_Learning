# 📏 ANS Behavioral Design — propuesta de tallaje por entregable

**Fecha:** 2026-07-10 · **Origen:** revisión del `ANS_ServiceBehavioral_Design.xlsx` de Milagros
(sección Behavioral Design), complementada con `/trinidad` (evidencia académica + debate de
prácticos + benchmarks de negocio sobre cómo entallar trabajo creativo/variable) · **Estado:**
propuesta para revisión del equipo.

---

## 0. /trinidad — qué dice la evidencia sobre entallar trabajo creativo

**Resumen ejecutivo:** las tres pistas **convergen** en un mismo punto, poco intuitivo pero
consistente: **estimar en unidades de tiempo precisas es la parte débil**; **fijar un presupuesto
de esfuerzo y calibrarlo con datos propios** es la parte fuerte. Eso es exactamente lo que ya hace
la economía de monedas del Beholder — este apartado la respalda con evidencia, no la reemplaza.

### 🔬 Pista empírica/teórica
La estimación humana de duración de tareas está sesgada de forma sistemática y predecible: el
**planning fallacy** (Kahneman & Tversky, 1979 — 🟢 fundacional) muestra que la gente subestima
tiempos porque planea desde una "vista interna" (los detalles de *esta* tarea) en vez de una
"vista externa" (cómo le fue a tareas parecidas en el pasado). El remedio documentado es el
**reference-class forecasting**: construir la estimación desde la distribución de casos
similares ya ejecutados, no desde el razonamiento sobre el caso particular (Kahneman & Tversky,
1979; síntesis en Flyvbjerg, 2013 🟢 — *Delusions of Success*). Traducido al equipo: la tabla de
tallas de la sección 3.1 solo es confiable si se calibra contra **los propios entregables
pasados del equipo** (lo que ya hace `beholder_tools.py retro`), no contra un supuesto teórico
de cuánto "debería" tardar algo.

### 💬 Pista social/mediática (debate de prácticos)
No hay un rumor viral que rastrear aquí, pero sí un **debate activo y de larga data** en
comunidades de práctica (foros de Agile, Scrum.org, Atlassian Community, blogs técnicos) conocido
como el movimiento **#NoEstimates**: la postura crítica argumenta que estimar en puntos/horas es
"trabajo sobre el trabajo" que genera sobrecarga cognitiva y hay que cuestionarlo o abolirlo,
mientras la postura defensora sostiene que el valor real de estimar no es el número sino **la
conversación** que produce alineamiento entre el equipo (Scrum.org, 2024; Atlassian Community,
2024 — 🟡 debate de prácticos, no evidencia controlada). El consenso reportado es que "no hay una
respuesta correcta única: el contexto decide" — que es justo la posición que toma esta propuesta:
tallas ligeras para conversación y kickoff, sin pretender que predicen el calendario con
precisión.

### 📈 Pista de negocio
Basecamp formalizó esta misma tensión en **Shape Up** con el concepto de **appetite**: *"un
appetite es completamente distinto de un estimado. Los estimados empiezan con un diseño y
terminan en un número; los appetites empiezan con un número y terminan en un diseño"* — se fija
cuánto tiempo se **quiere** gastar (presupuesto fijo), y el alcance se recorta para caber en ese
presupuesto, en vez de estimar cuánto "tomaría" un alcance ya fijado (Basecamp, *Shape Up*,
cap. 3 — 🟡 metodología propietaria, ampliamente adoptada). Por el lado de agencias de diseño
externas, la industria ya resolvió esta misma pregunta con dos modelos: **day rate** (tiempo de
un perfil senior, para trabajo de alcance variable) y **retainer** (capacidad reservada
recurrente, para relación continua) — casi exactamente el mismo par que "quest tallado" vs.
"bolsa de soporte" de esta propuesta (Creativepool, 2026; ManyPixels, 2026 — 🟡 prensa/guías de
industria, sin auditoría independiente).

### ⚖️ Síntesis y qué cambia en la propuesta
Las tres pistas apuntan a la misma arquitectura: **presupuesto fijo + calibración empírica +
recorte de alcance**, no estimación granular por etapa. Dos ajustes concretos a partir de esta
evidencia:
1. **La tabla 3.1 se declara explícitamente como "appetite", no como estimado** — un número de
   días que el equipo *decide* invertir en una talla, no una predicción de cuánto "tomará". Si
   el trabajo no cabe en el appetite, se recorta alcance (menos touchpoints, menos variantes),
   no se negocia más tiempo por default.
2. **El valor de tallar en kickoff es la conversación, no el número** — por eso el driver 3.2 se
   hace en 3 preguntas rápidas *con la persona que ejecuta presente*, nunca por Milagros o el
   comité solos desde afuera.

### Limitaciones de esta investigación
No se encontró literatura específica sobre tallaje de **diseño conductual** (behavioral design)
como disciplina propia — la evidencia se apoya en investigación general de estimación en trabajo
de conocimiento/creativo (software, diseño de servicio, gestión de proyectos), que es el
contexto más cercano disponible. La pista social no encontró comunidades específicas de
DesignOps discutiendo este problema (sí de ingeniería de software); se declara esa pista más
débil de las tres, no se fuerza.

---

## 1. Qué conservamos del modelo de Milagros (funciona bien)

1. **Separar proyecto de soporte** — días para trabajo de proyecto, horas para soporte. Correcto.
2. **Las categorías de soporte** (desbloqueos, nuevos escenarios, QA conductual, deuda
   conductual) describen bien el trabajo invisible del rol. Se conservan casi intactas.
3. **Feedback + VB como tiempo explícito** — reconocer que el loop con stakeholders consume
   días es un acierto político y operativo.
4. **Ejemplos de talla** — calibrar con casos concretos evita la inflación de tallas.

## 2. Dónde el modelo no calza con el rol real (y por qué no tomarlo como base)

| # | Supuesto del modelo de Milagros | Realidad del equipo BD (evidencia del tablero) |
|---|---|---|
| 1 | Toda iniciativa recorre un **pipeline lineal de 7 etapas** (research → … → playbook) | El trabajo real es **heterogéneo por entregable**: guías resumidas, playbooks, mesas legales, plantillas de contacto, modelos de competencias, despliegues, consultorías. Pocas iniciativas del Q3 recorren el pipeline completo; tallarlas por etapa obliga a forzar el trabajo dentro de un molde que no le corresponde. |
| 2 | La talla escala **todas las etapas por el mismo delta** (M=+3d, L=+7d, XL=+14d uniforme) | La complejidad no vive en todas las etapas por igual: un journey grande infla research y diagnóstico, no el diseño del experimento. El delta uniforme sobre-tara unas etapas y sub-tara otras. |
| 3 | **Factor = 1/%asignación** (50% ⇒ ×2 días, lineal) | Nadie del equipo está al 100% en una iniciativa: corren 4–8 frentes simultáneos (libro de monedas). La multitarea no escala lineal — el cambio de contexto tiene costo propio documentado (Rubinstein, Meyer & Evans, 2001 ⚪ ref. canónica). El factor lineal **subestima** sistemáticamente los plazos y el ANS nacería incumplible. |
| 4 | El reloj del ANS **corre continuo** | La historia del propio tablero muestra que la fricción dominante es **externa**: agencia (−6 semanas en guías AMI), mesa Legal/CUA (gate de Q-9), comité de herramientas (gate de AIDA), feedback de Producto. Un ANS que no pausa el reloj en gates externos se incumple por causas que BD no controla — y eso es medición injusta y pérdida política. |
| 5 | Un solo perfil, sin niveles | El equipo tiene expertise registrada (Senior / semi senior / junior, `beholder.config.md`): la misma talla no toma los mismos días para todos, y el pairing en entregables críticos es política del equipo. |
| 6 | ANS en **días** desconectado de la capacidad | El equipo ya gobierna capacidad en **monedas** (esfuerzo Q3, ≤8 simultáneas, validador automático). Dos sistemas de medida no conciliados = promesas contradictorias garantizadas. |

## 3. Propuesta: ANS modular por entregable, anclado a la economía de monedas

### Principio rector
**Se talla el entregable, no la etapa — y la talla es un appetite, no un estimado** (ver
sección 0): un presupuesto de días que el equipo decide invertir, calibrado contra su propio
historial, no una predicción derivada de descomponer el trabajo en pasos. Si el entregable no
cabe en la talla, se recorta alcance antes que se negocia más tiempo.

### 3.1 Catálogo de entregables BD con appetite por talla

> **Las categorías son cajones por función, no por artefacto.** Cada una responde a "¿qué
> trabajo hace este entregable?", de modo que lo que el equipo haga a futuro cae en un cajón
> existente sin rediseñar la tabla. Ejemplos actuales *(en cursiva)* y futuros (en lista) por
> categoría:
>
> 1. **🔍 Evidencia y diagnóstico** — producir conocimiento sobre la conducta. *Desk research,
>    bench frío/caliente, behavioral journey, diagnóstico de barreras.* Futuro: análisis de
>    data conductual, entrevistas/observación en campo, matriz de sesgos de un journey.
> 2. **📣 Comunicación conductual** — piezas y mensajes que mueven entendimiento o acción, para
>    **cualquier audiencia** (cliente o asesor). *Guías resumidas, flyers, cartas, plantillas
>    de mensaje para asesores, guías de comunicación con speeches, journeys de comunicación.*
>    Futuro: campañas de recordatorios con framing, copy de notificaciones/push, cartas de
>    renovación, scripts de bots.
> 3. **🎛️ Arquitectura de intervención** — rediseñar el contexto de decisión en un flujo,
>    producto o servicio. *Estrategia de primer contacto, batería de soluciones de renovación.*
>    Futuro: defaults y reordenamiento de opciones, rediseño de momentos de decisión (checkout,
>    renovación), sistemas de incentivos, arquitectura de decisión de un producto digital.
> 4. **🧪 Validación y experimentación** — probar antes de escalar. *Sacrificial concepts, test
>    de concepto Vivo Pack.* Futuro: pilotos en campo, experimentos A/B con tracking, series de
>    experimentación sobre un journey.
> 5. **📚 Sistemas y frameworks** — codificar conocimiento reutilizable del equipo o del negocio.
>    *Playbook de ventas, playbook B360, modelo de competencias, modelo de cambio de hábitos.*
>    Futuro: bibliotecas de intervenciones probadas, guidelines conductuales para otros equipos,
>    frameworks por línea de negocio.
> 6. **🚀 Adopción y despliegue** — instalar el cambio en la organización. *Despliegue FFVV
>    stock, despliegue Universidad Vida.* Futuro: capacitaciones, campañas de adopción con
>    campeones, seguimiento post-implementación.
>
> **Regla de encaje:** si un quest combina dos funciones (p. ej. research + framework), se
> talla cada función por separado y se suman — no se infla una sola categoría.
>
> Días = **días hábiles efectivos de trabajo BD al 100% en esa tarea** (no calendario).
> Conversión a monedas: **1 🪙 ≈ 1.5 días efectivos** (calibrada con la retro del tablero:
> ratio medio actual 0.72 🪙/día; se recalibra cada trimestre con `beholder_tools.py retro`).

| Categoría (función) | S | M | L | XL |
|---|---|---|---|---|
| **🔍 Evidencia y diagnóstico** | Desk research acotado · 2d · 1🪙 | Bench + síntesis con hipótesis · 4d · 3🪙 | Research con entrevistas/observación · 8d · 5🪙 | Diagnóstico E2E con data + campo · 12d+ · 8🪙+ |
| **📣 Comunicación conductual** | Ajuste de pieza/copy sobre plantilla existente · 1–2d · 1🪙 | Pieza o set nuevo para 1 canal/producto, con validación · 3–4d · 2–3🪙 | Familia de piezas o journey multicanal (o con gate legal) · 6–8d · 4–5🪙 | Ecosistema de comunicación E2E · 12d+ · 8🪙+ |
| **🎛️ Arquitectura de intervención** | Micro-fricción o default en un paso · 1–2d · 1🪙 | Intervención en un momento de decisión · 4d · 3🪙 | Estrategia conductual de un flujo completo · 8d · 5–6🪙 | Programa conductual E2E / arquitectura de un producto · 15d+ · 10🪙+ |
| **🧪 Validación y experimentación** | Test guerrilla / sacrificial concepts · 3d · 2🪙 | Test moderado con artefactos · 5d · 3–4🪙 | Experimento A/B con tracking · 10d · 6–7🪙 | Programa de experimentación (serie) · 15d+ · 10🪙+ |
| **📚 Sistemas y frameworks** | Ajuste de sección de un playbook/modelo · 1–2d · 1🪙 | Bloque nuevo o framework adaptado · 5d · 3–4🪙 | Playbook/modelo completo con validación · 10d · 6–7🪙 | Sistema con evaluación + gobernanza · 15d+ · 10🪙+ |
| **🚀 Adopción y despliegue** | Sesión de capacitación con material listo · 1–2d · 1🪙 | 1 cohorte con materiales listos · 4d · 3🪙 | Multi-cohorte con campeones y refuerzos · 8d · 5–6🪙 | Organización completa con medición de adopción · 12d+ · 8🪙+ |
| **🤝 Consultoría a otros equipos** — *agente AI App, Home* | Se gestiona como **soporte por horas** (ver 3.3), no como proyecto: sesión 0.5–1h · revisión 2–4h · co-diseño puntual 1–2d | | | |

### 3.2 Drivers de tallado (cómo decidir la talla sin discutir 20 minutos)
La talla se determina con **3 preguntas**, no por "tamaño del journey":

1. **Novedad:** ¿reusa un patrón/plantilla del equipo o se diseña de cero? (reuso → baja 1 talla)
2. **Superficie:** ¿cuántos touchpoints/variantes/productos toca? (1 → S/M · varios → L · familia/canal completo → XL)
3. **Validación requerida:** ¿cuántos aprobadores/gates externos tiene? (0–1 → mantiene talla ·
   2+ gates (legal, médico, comité) → sube 1 talla **o** se declara el gate por separado, ver 3.4)

Regla de honestidad: si dos drivers apuntan a tallas distintas, gana la mayor. Las tallas no se
negocian a la baja en la reunión de kickoff — se recalibran con datos en la retro trimestral.

### 3.3 Soporte: bolsa mensual conectada a la reserva de overhead
Se conservan las 4 categorías y horas de Milagros (desbloqueos 0.5–3h · nuevos escenarios 1–6h ·
QA conductual 0.5–4h · deuda conductual 2–8h), con una regla de encaje: **el soporte se paga de
la reserva de overhead** que la economía del equipo ya aparta (las 2 monedas no comprometidas de
cada persona ≈ 3 días/trimestre ≈ **~8 horas/mes por persona**). Si el soporte de un mes excede
la bolsa, deja de ser soporte: se convierte en quest con talla propia en el tablero. Esto evita
el patrón clásico de "muerte por soporte" invisible.

### 3.4 Los dos relojes (la regla más importante del ANS)
- **Reloj BD (el que se promete):** días hábiles efectivos desde kickoff **con insumos
  completos**. Es el único reloj sobre el que el equipo firma ANS.
- **Lead time (el que se reporta):** días calendario reales, incluyendo esperas.
- El reloj BD **se pausa** cuando: (1) el feedback de stakeholder tarda >48h; (2) hay gate
  externo (comité, Legal/CUA, validación médica, agencia); (3) vacaciones (capacidad 0, regla 5
  de la config).
- **Cada entrega reporta ambos números.** La brecha entre reloj BD y lead time hace **visible y
  cuantificable la fricción externa** — deja de ser una excusa y se vuelve un dato para Milagros
  y el comité. (Ej. real: guías AMI — trabajo BD de días, lead time +6 semanas por agencia.)

### 3.5 Ajuste por expertise y pairing (config del Beholder)
- **Junior** en un tipo de entregable que no ha hecho antes: talla efectiva ×1.3 **o** pairing
  con senior (recomendado en entregables L/XL y en todo lo crítico — regla ya vigente).
- **Senior review** en entregables con gate externo: +0.5 día fijo (evita retrabajos del gate).
- El tablero de progreso (Universidad Vida interna del propio equipo, cuando exista) permitirá
  bajar el ×1.3 con evidencia.

### 3.6 Integración con el Beholder (un solo sistema, no dos)
| Pieza | Cómo encaja |
|---|---|
| Tallas de quest | La talla del entregable fija sus monedas → el libro mayor y el validador (≤8 simultáneas) ya gobiernan si cabe en el calendario. |
| Prioridad del comité | Prioridad **Alta** de Milagros compra **SLA de inicio** (kickoff ≤5 días hábiles desde la solicitud con insumos), no solo de entrega. |
| Dependencias 🔗 | Los gates externos del reloj (3.4) se registran como dependencias; un gate vencido dispara ⚠️/🚨 según el protocolo de códigos. |
| Retro trimestral | `beholder_tools.py retro` compara monedas vs. días reales por entrega → recalibra la tabla 3.1 cada trimestre con datos, no con negociación. |
| Digest semanal | Reporta cumplimiento de reloj BD vs. lead time por entrega — el dato político clave para el comité. |

## 4. Qué proponerle a Milagros (resumen ejecutivo)
1. **Mantener su estructura para Service Design** si a ese rol le calza el pipeline — no es
   nuestra pelea.
2. Para Behavioral Design, **tallar por entregable** (tabla 3.1) con los 3 drivers (3.2), como
   **appetite calibrado con datos propios**, no como estimado por etapa (evidencia: sección 0).
3. **Dos relojes**: BD firma ANS sobre días efectivos; el lead time se reporta aparte y
   cuantifica la fricción externa (esto también la ayuda a ella a defender al equipo en comité).
4. Soporte con **bolsa mensual de ~8h/persona** conectada a la reserva de overhead; excedente se
   vuelve proyecto tallado.
5. Recalibración **trimestral con datos** (retro), no renegociación por reunión — es la misma
   lógica de reference-class forecasting que respalda el appetite en la sección 0.

## 5. Fuentes citadas (/trinidad)
- Kahneman, D. & Tversky, A. (1979) — origen del *planning fallacy*; ver también
  [Wikipedia: Planning fallacy](https://en.wikipedia.org/wiki/Planning_fallacy) y
  [The Decision Lab](https://thedecisionlab.com/biases/planning-fallacy) 🟢
- Flyvbjerg, B. (2013) — [*Delusions of Success* (comentario a Lovallo & Kahneman)](https://arxiv.org/pdf/1305.0741) — reference-class forecasting como remedio 🟢
- [PMI — Planning Fallacy: Causes and Solutions](https://www.pmi.org/learning/library/planning-fallacy-causes-solutions-project-expectations-6374) 🔵
- Basecamp — [*Shape Up*, cap. 3, "Set Boundaries"](https://basecamp.com/shapeup/1.2-chapter-03) — concepto de *appetite* 🟡
- [Scrum.org — No Estimates and is it Advisable for a Scrum Team to Adopt it?](https://www.scrum.org/resources/blog/no-estimates-and-it-advisable-scrum-team-adopt-it) 🟡
- [Atlassian Community — Best Practice for Estimation in Agile Teams](https://community.atlassian.com/forums/Jira-questions/Best-Practice-for-Estimation-in-Agile-Teams-Story-Points-vs/qaq-p/3100530) 🟡
- [Creativepool — Agency Pricing Models Explained](https://creativepool.com/magazine/workshop/agency-pricing-models-explained-retainers-vs-day-rates-vs-project-based-pricing) · [ManyPixels — Design Agency Pricing 2026](https://www.manypixels.co/blog/get-a-designer/design-agency-pricing) 🟡

Registradas en `research/fuentes/registro_fuentes.md` (F-30 a F-33).
