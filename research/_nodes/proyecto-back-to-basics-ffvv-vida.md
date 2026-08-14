# Proyecto Back to Basics — FFVV Vida Individual (RIMAC): conocimiento construido

> Node. Fuente de verdad de este tema: consolida el conocimiento interno del proyecto (modelo de
> experiencia de venta, mapa sistémico, estrategias de contacto, playbook del asesor, y su cruce
> contra la evidencia ya vetada del proyecto). Complementa, no reemplaza, a los nodes de
> investigación externa que ya se aplican a este mismo proyecto (ver Conexiones) — este node es
> la capa de **estado y decisiones internas de RIMAC**, esos otros son la capa de **evidencia
> externa**.
>
> Fecha de elaboración: 2026-07-23 · Última actualización: 2026-08-14 · Versión: v1.6
> (v1.0: mapa sistémico + estrategias de contacto + playbook + su cruce con evidencia/Lobo.
> v1.1 antepone el marco que faltaba — el "Modelo de Experiencia de Venta Vida" presentado al VP,
> con el diagnóstico Dx1-Dx3 ya formalizado — cambio estructural, no incremental, porque reordena
> cómo se debe narrar todo lo demás: liderar con el sistema, no con las iniciativas.
> v1.2 suma el Plan Piloto de validación del modelo — §8 — y corrige la descripción de AIDA: no es
> un simulador de práctica previo a un uso en producción ("AIDA Skill Trainer"), es ya la única
> herramienta que el asesor usa en conversación real con el cliente, ver nota en §2 — cambio
> estructural porque corrige cómo se describe una pieza del modelo mismo, no solo agrega
> información nueva. ⚠️ **Esta corrección de v1.2 era ella misma incorrecta en su parte central —
> ver v1.5.**
> v1.3 (2026-07-25, confirmado por Alejo) cierra la ambigüedad de fondo del workstream de
> contacto: **el lineamiento ya no es "5 estrategias en escalera con estados mixtos" — es
> categórico: solo aparecen en el playbook estrategias que parten de consentimiento ya existente.**
> Estrategias 2 y 3 pasan de "pendientes" a cerradas por diseño (§3); §6 se actualiza con la
> resolución real aplicada directamente al documento de la sesión, corrigiendo un bug que ya se
> había detectado y creído resuelto antes (ver Resolución definitiva); el "80% de volumen sin
> CUA" deja de tratarse como problema a resolver con una estrategia nueva y pasa a tratarse como
> compensado por calidad de conversación, no por cantidad de contactos — cambio estructural
> porque redefine qué cuenta como estrategia válida, no solo actualiza un estado.)
> **v1.6 (2026-08-14, formulado con Alejo) — se declara qué clase de objeto es el Modelo de Venta.**
> Nueva §1.1: no es un guion ni una metodología comercial, es un **modelo de referencia transversal**
> (normativo, transversal y **generativo** — cuando no hay producto que haga match con una motivación
> real, emite un requerimiento de producto). Se documentan por primera vez **los cuatro frentes donde
> se instancia** (competencias/selección y entrenamiento, pautas publicitarias, copiloto, sistemas
> del canal), la regla de **una fuente canónica, N instanciaciones**, y por qué su ausencia produce
> la información contradictoria que agota al asesor — Dx2 como causa, Dx3 como síntoma. Cambio
> estructural: fija la naturaleza del artefacto central del proyecto y su alcance institucional, que
> excede a la FFVV.
>
> **v1.5 (2026-08-14, confirmado por Alejo) — desconflación de AIDA y el prototipo del piloto.**
> Cambio estructural: corrige qué **es** una de las piezas centrales del modelo, y la corrección
> anterior (v1.2) era ella misma errónea. Este node venía describiendo **una sola** herramienta de
> IA del asesor; son **dos**:
> - **AIDA** — construida con **Microsoft Copilot**, **ya desplegada en producción** para la fuerza
>   de ventas. Es la herramienta que mide la encuesta de §5 y la que sufre los problemas de base de
>   conocimiento y de output que ahora se diagnostican en
>   `[[diagnostico-copiloto-ai-asesor-vida-rimac]]`.
> - **El prototipo del Plan Piloto (§8)** — construido sobre **Claude**, creado para validar el
>   modelo de venta. **Su diseño de julio cambió**; actualización pendiente de recibir, por lo que
>   todo §8 debe leerse como estado histórico, no vigente.
>
> Origen del error: el documento del Plan Piloto habla de "el agente"; v1.2 leyó ese "agente" como
> AIDA y lo propagó a §2 y §8. Correcciones aplicadas en ambas secciones, marcadas en línea.
> ⭐ **Hallazgo que se desprende de la desconflación** (no es solo higiene documental): la premisa
> de diseño del Plan Piloto —"el asesor interactúa con una sola herramienta"— no describe el campo
> real, donde AIDA ya está desplegada. Ver §2.
> Fuentes: documento interno "Conocimiento construido — Proyecto FFVV Vida Individual (RIMAC)"
> (consolidado al 2026-07-21, v1.0 de este node) + su continuación (consolidado al 2026-07-23) +
> imagen del mapa AS IS 2026 compartida en la sesión (no persistida como archivo en el repo — ver
> Limitaciones) + documento interno "Plan Piloto · Modelo de Experiencia de Venta Vida" (CoE
> Diseño Estratégico, v1, julio 2026, subido a la sesión 2026-07-24 — ver §8) + lineamiento
> definitivo de CUA comunicado directamente por el usuario (Alejo) el 2026-07-25 — ver §3 y §6.
> **Actualización 2026-07-24 (sin bump de versión, incremental):** análisis con el Lobo
> (`research/lobo/opinion_experto.md`) para cerrar el hueco de citas del Bloque 4 (§5, Hallazgo 2)
> y fortalecer Dx3 (§1) — suma F-220 a F-228 al ledger de `cronista`, únicas fuentes externas
> nuevas que introduce este node hasta ahora. **Actualización 2026-07-25 (sin bump de versión,
> incremental):** corrige la fuente de C.6 en la tabla de §5 (Davis 1976, F-236, reemplaza a
> Darley & Latané 1968, F-226, cuyo encaje cuestionable ya advertía esta misma tabla) y aplica el
> renombrado ya recomendado de C.7 ("Poner el precio en perspectiva (anclaje aplicado)", cita
> ahora Tversky & Kahneman 1974, F-220, en vez de la "regla del 10x") — ambos a pedido del
> usuario, aplicados directamente al Playbook de la sesión también. **Actualización 2026-07-26
> (sin bump de versión, incremental):** el lineamiento de CUA de §3 pasa de "vigente — no
> definitivo" a definitivo/resuelto; se agrega la precisión de que ninguna base de datos armada a
> partir de referidos sin consentimiento es legal (riesgo penal, incluso un solo número); y se
> documenta el mecanismo concreto de la Estrategia 4 — tarjeta del asesor con código QR al
> formulario de consentimiento — que resuelve "Gestión de referidos" en el Playbook de la sesión
> (Bloque 5, antes `(Pendiente)`).
> **v1.4 (2026-07-27)** incorpora el deck "Back to Basics — low-fi" (17 láminas, presentación para
> Milagros, persistido en `research/_outputs/back-to-basics-presentacion-lowfi-2026-07-27.html`):
> formaliza el origen del pedido y la regla metodológica del equipo ("toda exploración del sistema
> es obligatoria antes de diseñar"), suma 4 hallazgos previos de investigación (Research CoE
> 2023-2025) nunca antes documentados en este node, reencuadra el mapa sistémico con una
> terminología de "9 frentes" (ver nota de reconciliación en §2) y 4 hallazgos operativos nuevos que
> se anclan a Dx1-Dx3, agrega evidencia externa nueva (McKinsey, F-359/F-360; trayectoria de loss
> ratio de Lemonade, F-361), suma datos primarios de diagnóstico (encuesta a 19 asesores + resultados
> del Taller de Manejo de Objeciones) nunca antes cuantificados en este node, introduce "Universidad
> Vida" como programa de onboarding, un backlog estructurado de 5 frentes (incluye un mecanismo
> nuevo — alertas de CRM como default seguro — complementario al de la tarjeta QR de §3), la
> bifurcación estratégica Espejo (otros canales de Vida) vs. Transformación (ramo **AMI**, no
> mencionado antes en este node), y la lista de entregables del equipo — que revela a **Felipe**
> como colaborador no listado en el §0 Equipo hasta ahora. Cambio estructural: agrega alcance
> (AMI), evidencia nueva y un miembro de equipo no documentado — no es solo actualización de estado.

---

## 0. Equipo del proyecto

**(Agregado 2026-07-24, confirmado por el usuario)** Back to Basics — Venta Vida Individual ha
sido trabajado por **Alejandro Rojas** y **Melissa Ramírez** (ambos Behavioral Designers) y
**César Cordero** (Service Design). Nota de trazabilidad: §3 de este node lista además a
"Melissa (Consentimiento/CUA)" como stakeholder del workstream de estrategias de contacto — no
se asume que sea la misma persona que Melissa Ramírez sin confirmación explícita; se documentan
ambas referencias tal como aparecen en las fuentes originales.

**(Agregado 2026-07-27, vía deck "Back to Basics — low-fi", lámina 17 "Entregables del equipo";
rol confirmado por el usuario el mismo día): aparece un cuarto colaborador, Felipe, practicante
de Behavioral Design**, con autoría o co-autoría en: prototipo de agente para entrenamiento de
asesores (con Melissa), diseño del prototipo funcional del front agéntico, y capacidad del agente
de entrenamiento para generar reportería de resultados (además de la encuesta pre-post, con
Alejandro). César Cordero es de un equipo distinto (Service Design) — no hay superposición ni
reemplazo entre ambos; simplemente no aparece en esta lámina de entregables puntual.

## 1. Modelo de Experiencia de Venta Vida (deck presentado al VP)

Presentación "Modelo de Experiencia de Venta Vida" (actualizado mayo 2026, CoE Experience
Design), mostrada al VP de los canales de venta Vida y Financieros. Es el documento marco que
engloba el workstream de estrategias de contacto FFVV (§3) y el playbook del asesor (§4) dentro
de una narrativa más amplia de experiencia de venta — todo lo que sigue en este node vive dentro
de este marco, no al lado de él.

**Feedback del VP y su implicación operativa — la lección más importante de esta sección:**
reacción positiva, con interés particular en el mapeo sistémico del ecosistema (mapa de
nodos/conexiones + diagnóstico Dx1-Dx3, ver §2). **En futuras presentaciones a este VP o
audiencias similares de dirección de canal, liderar con el mapa del ecosistema y el diagnóstico
sistémico antes de mostrar iniciativas o palancas puntuales — abrir con "iniciativas aisladas" se
percibe como parche, no como sistema.** Esto aplica directamente a cualquier deck que este
proyecto produzca de aquí en adelante (ver output relacionado en Conexiones).

**Statement Vida Individual:** "Redefinimos tu seguro de vida para que vivas tranquilo hoy y
mañana... conectándote con un ecosistema de bienestar que cuida tu vida desde el primer día."
Misión: promover y guiar en el bienestar financiero e integral.

**3 Pilares de la Propuesta de Valor:**
1. Protección que habilita bienestar (el seguro activa un ecosistema de servicios).
2. Enfoque en motivaciones (producto/beneficios/experiencia según el "por qué" del cliente, no un
   perfil estándar).
3. Crece y se adapta contigo (se adapta a hitos de vida: matrimonio, hijo, casa, cambio de
   trabajo, separación).

**4 Principios transversales:** Claridad y simplicidad; Asesoría especializada (disponible en
venta, hitos de vida, gestión del producto — no solo siniestro); Confianza (validación de pares,
testimonios, transparencia de letra chica); Sin fricciones (autogestión para lo común,
escalamiento humano para lo complejo).

**4 Motivaciones de personas (Vida Individual):** Proteger a los míos; Hacer crecer mi dinero;
Llegar a una meta específica; Rentabilizar lo que ya pago. **(Fortalecido 2026-07-24):** perfilar
por motivación en vez de por perfil demográfico estándar tiene respaldo en literatura —
Piercy, Campbell & Heinrich 2011 (F-229, 🟢A, específico de servicios financieros) encuentra que
la segmentación demográfica explica poco de la conducta real de compra/preferencia de marca en
este sector; la Teoría de la Autodeterminación (Deci & Ryan 2000, F-230, 🟢A) da el marco
psicológico general de por qué la motivación subyacente predice mejor la conducta que una
categoría externa asignada.

**Diagnóstico sistémico formalizado (Dx1-Dx3)** — numeración oficial ya validada por el VP, que
acompaña al mapa del ecosistema (mismo mapa AS IS 2026 de §2). **Cualquier hallazgo nuevo del
proyecto debe anclarse a uno de estos tres, en vez de crear otra taxonomía:**
- **Dx1** — Las lógicas de negocio de Cliente (comprar lo que necesita/conviene), Aseguradora
  (vender y retener más) y Vendedor de seguros (ganar la mayor comisión posible) no siempre
  conversan → genera fracturas en la experiencia del usuario.
- **Dx2** — Los elementos del sistema no siempre conversan entre sí → el usuario recibe
  información inconsistente durante su compra. (Es el diagnóstico que sostiene directamente el
  mapa del ecosistema de §2.)
- **Dx3** — El asesor tiene alta carga cognitiva y emocional que le deja poca capacidad para
  gestionar con calidad → el usuario experimenta una venta acelerada y fracturada. **(Fortalecido
  2026-07-24):** la Teoría de Carga Cognitiva (Sweller 1988, F-228, 🟢A) da a este diagnóstico
  base académica explícita — la capacidad de procesamiento consciente es limitada, y tareas con
  muchos elementos que gestionar a la vez degradan el desempeño incluso en expertos. Antes era
  solo diagnóstico interno; ahora tiene respaldo de la literatura de ciencia cognitiva.

**Iniciativas aisladas ya existentes** (evidencia de que hoy se soluciona en piezas sueltas, no
como sistema — el contraste que justifica todo el proyecto): Póliza simple, Welcome Pack,
Material de capacitación del asesor, Consultas post-venta, Pauta de RRSS, Speech de asesor, PDP.

**Visión de solución:** "De ofrecerte lo que tenemos, a construir lo que necesitas."
Diferenciación por cómo se vende, no solo por lo que se vende. Para el asesor: dar solo las
herramientas más eficientes, liberando capacidad cognitiva/emocional (ataca Dx3 directamente).
Para el prospecto: ir a su ritmo, información coherente en su propio lenguaje (ataca Dx2). La
tecnología potencia al asesor, no lo reemplaza — coherente con
[[futuro-asesores-seguros-venta-digital|¿Desaparecerán los asesores de seguros?]]; el ciclo del
asesor y el journey del cliente se diseñan como un mismo sistema.

**Mesa Back to Basics FFVV — Experiencia To Be** (preliminar, sujeta a priorización con Producto,
Estrategia de Clientes y Canal — ver §7):
- Journey cliente (5 momentos, mismo journey que el playbook de §4): Awareness/consideración →
  Primer contacto → Explicación del producto → Aceptación → Postventa/medición.
- Journey asesor (nuevo, no estaba en el playbook): Talento → Perfilamiento y gestión → Cierre de
  venta → Postventa.
- Palancas propuestas (16, sin priorizar aún): secuencia de perfilamiento centrada en motivación,
  simulación de escenarios y productos, plataforma única de inteligencia de leads, data
  centralizada de performance de venta, alertas automatizadas de churn, selección predictiva de
  talento, formación en venta consultiva con estándar único, línea de carrera y formación
  continua, sistema de incentivos/comisiones/penalidades, copiloto del asesor, suscripción
  inteligente, ecosistema no cliente, awareness alineada con estrategia, herramientas de social
  selling para asesor, IA conversacional para el cliente, enrutamiento inteligente
  asesor-cliente, handoff sin quiebre.
  **Candidatas directas para resolver los nodos rojos del mapa** (§2: "Sistemas para
  perfilamiento y gestión de ventas", "Monitoreo de calidad"): plataforma única de inteligencia
  de leads, copiloto del asesor, alertas automatizadas de churn.

**Origen del pedido (agregado 2026-07-27, vía deck "Back to Basics — low-fi", lámina 03):**
RIMAC había despriorizado varios proyectos estratégicos, pero la necesidad de negocio no se
detuvo — llegó un pedido puntual (speeches para distintos momentos del journey del asesor). El
equipo de behavioral design aplicó su regla de trabajo (ver siguiente párrafo) antes de
responder al pedido literal, y encontró que la misma CoE venía produciendo diseños no
articulados entre sí — de ahí nace la decisión de unificar los frentes de Venta Vida bajo
"Back to Basics", en vez de simplemente entregar los speeches pedidos.

**Regla metodológica del equipo (agregado 2026-07-27):** "todo pedido recibe, obligatoriamente,
una exploración del sistema en el que está inscrito el problema — antes de diseñar ninguna
solución." No se diseña una pieza suelta (un speech, una plantilla) sin entender el ecosistema
completo que la rodea; el resultado típico de esa exploración es un mapa del ecosistema (§2). Es
la razón formal, ya articulada como regla de equipo y no solo como práctica implícita, de por qué
este proyecto existe como frente unificado y trae diagnóstico propio en vez de piezas sueltas.

**Hallazgos previos de investigación — Research CoE 2023-2025 (agregado 2026-07-27, vía deck
low-fi, lámina 04):** cuatro hallazgos de investigaciones internas anteriores a este proyecto,
que ya apuntaban a la misma dirección antes de la exploración sistémica de 2026:
1. **El asesor es "la cara" de RIMAC** — una buena experiencia con el asesor se traduce en
   recomendación; una mala experiencia genera rechazo hacia RIMAC como marca, no solo hacia esa
   persona.
2. **Los brokers ganan la confianza que RIMAC no gana directamente** — se les percibe como más
   confiables y transparentes que RIMAC al ofrecer sus propios productos.
3. **La venta agresiva genera rechazo** — usuarios reportan ser abordados con mensajes invasivos
   y confusos.
4. **El problema es sistémico, no solo del asesor** — el asesor es el primer frente de cara al
   usuario, pero hay una lógica sistémica detrás que impacta la experiencia del cliente durante
   la venta. Es el precedente directo, previo a 2026, de lo que Dx1-Dx3 formaliza más arriba en
   esta misma sección.

**Evidencia externa adicional para "potenciar al asesor, no digitalizar" (agregado 2026-07-27,
vía deck low-fi, lámina 08) — complementa el benchmark de Corea/China/Lemonade ya citado en §2:**
McKinsey (2023, F-359, 🔵B): *"Insurers cannot sacrifice the human touch in CX — especially for
life customers, who rank agents as the most trusted source for learning about insurance
products."* En Asia-Pacífico el mix de canales de vida sigue dominado por agencias (~40%) y
partnerships (~35%) — el contacto cara a cara sigue siendo la forma dominante aunque ~80% de las
ventas ya están habilitadas por tecnología digital (McKinsey, F-360, 🔵B): lo digital potencia al
agente, no lo reemplaza. Contraejemplo citado en el mismo deck: Lemonade (IA sin agentes, IPO
2020) mantuvo un loss ratio de 166% (2017) → 86% (2019) → ~90% (2021-22) (F-361, 🟠D, fuente
original no verificada — complementa a F-189/F-29, ya en el ledger, con datos más recientes)
— digitalizar sin potenciar el juicio humano no resolvió la economía del seguro.

**Diagnóstico interno — encuesta a 19 asesores y Taller de Manejo de Objeciones (agregado
2026-07-27, vía deck low-fi, láminas 09-12):** primeros datos primarios cuantificados de este
proyecto sobre uso y valoración de herramientas por parte de los propios asesores.

- **Uso de herramientas ("siempre", de 19 asesores):** Salesforce 16/19 (84.2%, nunca 0/19) ·
  WhatsApp 14/19 (73.7%, nunca 0/19) · Email 11/19 (57.9%, nunca 0/19) · Excel 10/19 (52.6%,
  nunca 1/19) · **AIDA 7/19 (36.8%, nunca 1/19)** · CartaPlan 1/19 (5.3%, nunca 7/19).
- **Satisfacción general con la ayuda que reciben:** 8.05/10 en promedio — pero el promedio no
  cuenta toda la historia: comprensión de producto 8/19 bastante · 8/19 regular · 3/19 poco;
  **manejo de objeciones/persuasión, la peor calificada: 6/19 bastante · 9/19 regular · 4/19
  poco.**
- **Hallazgo accionable central:** manejo de objeciones es el tema más pedido (42%, 8/19) y el
  cierre es el momento con más necesidad de apoyo (~40%) — el asesor no pide más información de
  producto, pide ayuda para manejar la conversación justo antes de cerrar. Herramientas a
  mejorar, empatadas a 4/19 cada una: **AIDA** ("no da la información adecuada", "no contesta
  bien casi nunca" — mismo defecto de consistencia que reporta el taller, ver abajo), recursos
  visuales (piden brochures digitales listos), cotizador (piden usarlo sin autorización previa).
  Otros hallazgos: falla de onboarding citada explícitamente ("no enseñan bien a usar
  Salesforce... aprendemos en marcha"); uso informal de ChatGPT/Gemini para compensar huecos de
  AIDA y del cotizador.
- **Taller de Manejo de Objeciones (piloto, 36 invitados):** 99.33% satisfacción con el
  contenido · 98.67% desempeño del speaker · **NPS de 96.67** · 83.33% de asistencia (30 de 36).
  Drivers de valor: casuística real (principal), copiloto de IA (probablemente el mismo
  simulador de práctica deliberada co-diseñado por el equipo — ver AIDA Skill Trainer en §2),
  metodología práctica con feedback. Mejoras pedidas: más diversidad de casos, **consistencia del
  copiloto de IA — mismo defecto que AIDA reporta la encuesta**, logística.
- **Lectura conjunta:** el dolor de encuesta y taller (tema: manejo de objeciones; momento: el
  cierre; mecanismo: simulación con IA + feedback) es la expresión más concreta del Hallazgo 1
  del mapa (sobrecarga del asesor, ver nota de reconciliación en §2) — pero el diagnóstico
  completo pide algo más amplio que solo entrenamiento, porque si las lógicas colisionan
  (Hallazgo 2) y el cliente hereda esa inconsistencia (Hallazgo 3), la respuesta tiene que ser
  más de una pieza. Tres apuestas mejor respaldadas, base de la Fase 1 ya construida (ver más
  abajo): (1) contenido y herramientas que hablen el mismo idioma, (2) corregir las fallas del
  copiloto — mismo defecto en encuesta y taller, (3) evolucionar el entrenamiento con IA.

**Qué se construyó — Fase 1 (agregado 2026-07-27, vía deck low-fi, lámina 13; consolida y nombra
lo que §3, §4 y §6 de este node ya documentaban por partes):** Modelo de Venta de 5 bloques
(Quiénes somos · Qué vendes · Que te encuentren · La asesoría, 4 pasos · Después del sí, mismos
bloques que el Playbook de §4) · Perfilamiento por motivaciones (dos mecánicas: meta — costo de
lo que el cliente quiere lograr — y protección — ingreso que la familia perdería) · Agente
(cuerpo de conocimiento para entrenamiento: modelo de venta, portafolio, manejo de objeciones e
identidad RIMAC, con speeches por origen de lead) · Toolkit de social selling (Nivel 1: foto,
historia, perfiles, firma; Nivel 2: redes completas, banco de contenido) · Playbook y materiales
(storytelling de asesoría + materiales simplificados: flyer, brochure, cartaplan) · Estrategia de
contacto (validada con Legal/Cumplimiento/CUA — ver §3; plantillas WhatsApp y correo) ·
**Universidad Vida** (programa nuevo, no mencionado antes en este node: onboarding con práctica
espaciada desde el día 1 — ver también "Despliegue" más abajo).

**Backlog estructurado de siguientes pasos (agregado 2026-07-27, vía deck low-fi, láminas 15-16
— más específico y accionable que las "16 palancas sin priorizar" ya documentadas arriba):**
1. **Consulta (corto plazo):** resolver la consistencia de respuestas del copiloto de IA — mismo
   defecto que señalan la encuesta y el taller. Centralizar funciones en el copiloto en vez de
   sumar herramientas sueltas, cuidando no sobresaturar al asesor (Hallazgo 1 del mapa).
2. **Entrenamiento (mediano plazo):** de onboarding puntual a programa de crecimiento continuo
   (competencias + práctica espaciada); la IA pasa de piloto a herramienta de uso diario (requiere
   alcance ampliado con GenAI).
3. **Alertas de CRM — mecanismo nuevo, complementario a la tarjeta QR de §3:** un "default
   seguro" en Salesforce que avisa o condiciona el contacto al consentimiento registrado —
   protege sin depender de que el asesor lo recuerde. No sustituye el mecanismo de autorregistro
   de la Estrategia 4 (§3); opera un nivel más abajo, como salvaguarda técnica dentro del CRM.
4. **Programa de referidos:** contacto por referido en vez de en frío, apoyado en consentimiento
   implícito + prueba social + reciprocidad — falta definir el incentivo al cliente que refiere
   (ver también la "Novedades abiertas" de §3 sobre pago YAPE/Plin, pendiente de Legal).
5. **Seguimiento e incentivos:** diseñar un sistema de seguimiento del aprendizaje y del
   cumplimiento de lineamientos RIMAC, atado a un sistema de incentivos y crecimiento — responde
   directamente a los nodos rojos de "incentivos por calidad/experiencia" y "monitoreo de
   calidad" del mapa (§2).

**Despliegue post-piloto (agregado 2026-07-27):** dos frentes en paralelo — la fuerza de venta
actual (por defaults y campeones) y **Universidad Vida** (por cohortes). La decisión de
implementación en AIDA sale del piloto de §8, no es un paso aparte.

**Espejo vs. Transformación — bifurcación estratégica (agregado 2026-07-27, vía deck low-fi,
lámina 16):** el proyecto ya distingue explícitamente dos caminos de escalamiento con riesgo y
esfuerzo distintos, más allá de las "16 palancas sin priorizar" ya documentadas:
- **Espejo → otros canales de Vida (riesgo/esfuerzo bajo):** mismo producto, mismo cliente, mismo
  modelo — solo cambia el canal de entrega. Se replica sin cambios: venta consultiva,
  storytelling, estrategia de contacto, perfilamiento por motivaciones. Se ajusta: el canal, el
  ritmo de seguimiento, el tono si aplica. No requiere repetir la exploración obligatoria del
  sistema (ver regla metodológica arriba).
- **Transformación → ramo AMI (riesgo/esfuerzo mayor) — alcance nuevo, no mencionado antes en
  este node.** Producto distinto, otras motivaciones, otro ciclo de venta y otras objeciones. Se
  hereda la metodología completa, la formación con práctica espaciada, la validación por piloto.
  Se transforma (no se reusa): arquitectura de decisión, manejo de objeciones, y el perfilamiento
  por motivaciones se recalibra. **Exige repetir la exploración obligatoria del sistema para AMI
  antes de construir nada** — no hay diagnóstico sistémico de AMI todavía en este repositorio.
  *(Nota: el deck fuente no expande la sigla "AMI" — verificar con el equipo antes de usarla en
  materiales externos sin definirla.)*

**Entregables del equipo de behavioral design (agregado 2026-07-27, vía deck low-fi, lámina 17
— primer inventario consolidado con autoría por persona):** (1) Diagnóstico sistémico de la
Venta Vida (Alejandro); (2) Piloto de capacitación en manejo de objeciones — diseño de la
capacitación (Melissa), guía digital para manejo de objeciones (Alejandro y Melissa), resumen
físico de la guía (Alejandro), prototipo de agente para entrenamiento de asesores (Felipe y
Melissa); (3) Estrategia y mensajes de primer contacto — sacrificial concepts para validación
con legal y cumplimiento (Alejandro), plantillas de mensaje para WhatsApp/email (Alejandro); (4)
Playbook para el asesor — estrategia de social selling (Melissa), consolidado de contenido y
diseño del manual (Melissa); (5) Materiales de venta — flyers de venta (Alejandro), tarjeta de
presentación del asesor (Melissa — ver la maqueta con mecanismo QR construida en sesión, sección
de flyers/tarjeta de este proyecto); (6) Diseño del piloto — prototipo funcional del front
agéntico (Felipe); (7) Herramientas de medición — encuesta pre-post de asesores (Alejandro y
Felipe), matriz para mystery shoppers con rúbricas de experiencia (Alejandro y Melissa),
capacidad del agente de entrenamiento para generar reportería (Felipe).

---

### 1.1 Qué tipo de objeto es el Modelo de Venta (agregado 2026-08-14, formulado con Alejo)

Sección agregada porque el proyecto venía llamándolo "modelo de venta" sin declarar **qué clase de
artefacto es**, y esa imprecisión tiene consecuencias prácticas: determina quién lo mantiene, cómo
se despliega y contra qué se mide.

**No es un guion de venta, ni una metodología comercial, ni un playbook.** Es un **modelo de
referencia transversal del ecosistema de venta**: un cuerpo normativo sobre **cómo debe venderse el
seguro de vida** —no solo cómo debe vender *este* asesor— que **ningún frente posee y todos
instancian**.

Tiene tres propiedades que conviene nombrar por separado:

1. **Normativo.** Prescribe cómo *debe* venderse; no describe cómo se vende hoy. Es lo opuesto al
   mapa AS IS de §2, y por eso ambos son necesarios: el mapa dice dónde está el sistema, el modelo
   dice hacia dónde debe moverse.
2. **Transversal.** No vive en un frente. Vive en varios a la vez, y **su dueño no es ninguno de
   ellos** (ni la CoE, ni la academia, ni marketing, ni el copiloto).
3. **Generativo** — la propiedad más distintiva y la menos documentada hasta ahora. La lógica
   central es un **match entre motivaciones de la persona y productos ofrecidos**; cuando **no hay
   producto que haga match con una motivación real**, el modelo **no descarta al cliente: emite un
   requerimiento de producto**. Es decir, el modelo es también un **canal de entrada al desarrollo
   de producto**, no solo un instrumento de venta. Un modelo de venta que produce requerimientos de
   producto es una pieza de estrategia, no de capacitación.

**Contenido del modelo, en cuatro capas:** (a) una **lógica de match** motivación ↔ producto;
(b) una **secuencia** — en qué momento del recorrido se comunica qué; (c) un **cuerpo de
conocimiento** — qué decir y cómo; (d) un **bucle de producto** — qué falta en el portafolio.

Respaldo de la lógica central, ya en el ledger: la segmentación demográfica explica poco de la
conducta real en servicios financieros (Piercy, Campbell & Heinrich 2011, **F-229**, 🟢A), y la
Teoría de la Autodeterminación explica por qué la motivación subyacente predice mejor que una
categoría externa asignada (Deci & Ryan 2000, **F-230**, 🟢A).

#### Los frentes donde el modelo se instancia

"Multimodal" en este proyecto significa esto, y **no** significa "el modelo está en todas las
pantallas del asesor":

| Frente | En qué se convierte el modelo ahí | Dueño típico |
|---|---|---|
| **Modelo por competencias** (selección y entrenamiento) | Criterios de contratación + currículo de formación | Talento / Academia |
| **Pautas publicitarias** | Promesa, segmentación del mensaje, oferta comunicada | Marketing |
| **Copiloto (AIDA)** | Base de conocimiento + comportamiento del agente | Tecnología / CoE |
| **Sistemas del canal** | Campos, estados, validaciones y reglas del flujo | TI / Canal |

⭐ **La relación correcta entre el modelo y cada frente es de instanciación, no de copia.** Cada
frente **traduce** el modelo a su propio idioma. Y de ahí sale el requisito arquitectónico que el
proyecto todavía no tiene declarado:

> **Una fuente canónica, N instanciaciones.** Debe existir **un** lugar donde el modelo es
> verdadero, y cada frente deriva de él. Sin eso, cada frente escribe su propia versión y las
> versiones divergen con el tiempo.

**Por qué esto no es una formalidad:** el asesor es el punto donde todas las instanciaciones se
encuentran. Si divergen, **el asesor es quien recibe la contradicción** — lo que Alejo describe como
"información física y virtual que a veces hasta puede ser contradictoria". Eso es **Dx2 en su forma
más pura** (los elementos del sistema no conversan entre sí), y **Dx3 es cómo se siente** (carga
cognitiva y emocional). La contradicción que agota al asesor no es un problema de documentación: es
el modo de falla predecible de un modelo transversal sin fuente canónica.

⚠️ **Trampa a evitar al defender este modelo ante un comité (F-481):** el mercado de sales
enablement está lleno de cifras del tipo "+12% de win rate con adopción >75%" o "+10% de revenue por
cada 10% de adopción", **todas de proveedores y sin fuente primaria rastreable**. No incorporarlas.
El concepto que sí importa —que existe una **brecha entre proceso documentado y proceso
adoptado**— el proyecto **ya lo mide con instrumento propio**: el indicador 6 del Plan Piloto
(brecha comprensión → aplicación).


## 2. Mapa sistémico AS IS 2026 (diagnóstico de ecosistema)

Mapa de nodos y conexiones del ecosistema de venta de seguros de vida de RIMAC, con tres
dimensiones por nodo — estado (verde/amarillo/rojo), tipo de influencia (directa +, inversa −,
habilitadora O) y estado de la influencia (continua/discontinua). Es el mapa referenciado en Dx2
del deck al VP (§1) — existe también como diagrama visual (ver Limitaciones sobre su
disponibilidad en el repo).

**Origen del ejercicio (confirmado por el usuario, 2026-07-24):** este mapeo sistémico no nace
de cero en 2026 — viene de una línea que arranca en **2024**, cuando se consolidó una
intervención en la fuerza de ventas de **telemarketing**, hecha por un equipo llamado **Digital
Engagement**. Back to Basics (Vida Individual, FFVV presencial) extiende esa misma lógica de
diagnóstico sistémico a un canal distinto, no la inventa — vale la pena nombrar este precedente
en cualquier presentación al VP o a Milagros como evidencia de que el enfoque ya tiene una
trayectoria dentro de RIMAC, no es un experimento aislado del CoE.

**Insumos del diagnóstico (confirmados por el usuario, 2026-07-24):**
- Shadowing con asesores; entrevistas con asesores; entrevistas/reuniones con stakeholders
  (Legal, Cumplimiento, CUA, FFVV); entrevistas con otras áreas que manejan frentes de venta;
  análisis de procesos.
- **Desk research y benchmark — específicamente sobre cuál es la mejor forma de llevar la venta
  en productos de vida** (no benchmarking genérico de estrategias de contacto). De este
  benchmark salen dos definiciones de diseño clave:
  - **Por qué el modelo es híbrido, con el asesor como parte no negociable de la gestión**: se
    apoya en el mismo cuerpo de evidencia de
    [[futuro-asesores-seguros-venta-digital|¿Desaparecerán los asesores de seguros?]] — el
    marco causal de por qué el intermediario persiste (Cummins & Doherty 2006, mitiga asimetría
    de información y selección adversa) y el benchmark de negocio de mercados de alta
    digitalización que **no** reemplazaron al asesor humano: Corea del Sur (canal 100% online de
    vida retrocedió 33.6% en una década), China (agentes + bancaseguros retienen >90% de las
    primas de vida pese a 20x de crecimiento insurtech), y el caso Lemonade (100% digital, sigue
    sin ser rentable 12 años después de fundado). El mercado global de corretaje además está
    **creciendo** (USD 336B→695B proyectado a 2033), no encogiendo — evidencia de negocio, no
    solo intuición, de que "vender vida sin asesor" no es el modelo que gana.
  - **Cómo surge la propuesta del copiloto del asesor (AIDA)**: si el benchmark descarta
    reemplazar al asesor, la pregunta de diseño pasa de "¿automatizamos la venta?" a "¿cómo
    potenciamos al asesor sin sumarle más carga?" (conecta directo con Dx3). RIMAC ya tenía una
    señal propia a favor de esa dirección — un asesor web con IA generativa que, según prensa
    local, duplicó conversión (Business Empresarial 2025, autorreportado, 🟠D) — y la literatura
    de simulación de entrenamiento en adultos (Sitzmann 2011, F-219, 🟢A) da la base para que el
    copiloto empiece como herramienta de *práctica* (AIDA Skill Trainer) antes que como
    herramienta de *producción* en vivo — reduce el riesgo de lanzar algo sin validar, coherente
    con la tesis 10 del Lobo (no sobreclamar precisión de IA sin validación, caso Babylon
    Health). **Corrección (2026-07-24, vía Plan Piloto — ver §8):** esa secuencia
    "práctica antes que producción" no es lo que terminó construyéndose. El Plan Piloto describe
    al agente como **"la única herramienta" del asesor**, usada en vivo durante la conversación
    real con el cliente ("el agente vive dentro de Claude", con "los dos modos" sin detallar aún
    cuáles son) — el playbook deja de ser un documento que el asesor consulta y pasa a ser la base
    de conocimiento que alimenta al agente. No hay evidencia en el Plan Piloto de una fase previa
    de solo-práctica; el riesgo que motivaba empezar por ahí (lanzar sin validar) sigue vigente,
    pero ahora se gestiona distinto — vía el propio piloto de 10 asesores (§8), no vía una etapa
    de simulador aislada.
    > ⚠️ **CORRECCIÓN DE LA CORRECCIÓN (2026-08-14, confirmada por Alejo).** El párrafo de arriba
    > decía "el Plan Piloto describe **a AIDA** como la única herramienta"; **decía mal**. Ese
    > "agente que vive dentro de Claude" es el **prototipo del piloto**, no AIDA. Son dos
    > herramientas distintas y hay que mantenerlas separadas en todo material de este proyecto:
    > - **AIDA** — creada con **Copilot**, **ya desplegada** para la fuerza de ventas. Es la que
    >   reporta la encuesta de §5 (7/19 la usa siempre; "no da la información adecuada") y la que
    >   se diagnostica en `[[diagnostico-copiloto-ai-asesor-vida-rimac]]`.
    > - **El prototipo del piloto** — construido sobre **Claude**, para validar el modelo de venta.
    >   Su diseño de julio cambió; actualización pendiente.
    >
    > ⭐ **Consecuencia que este node debe registrar como hallazgo, no como nota al pie:** la
    > premisa de diseño del Plan Piloto —*"el asesor interactúa con una sola herramienta"*— **no
    > describe la realidad de campo**. El asesor ya tiene AIDA desplegada; el prototipo del piloto
    > sería una segunda IA en paralelo. Eso pertenece de lleno al Dx3 (carga cognitiva del asesor)
    > y al lineamiento del backlog de "centralizar funciones en el copiloto en vez de sumar
    > herramientas sueltas" — que hoy el propio proyecto estaría contradiciendo sin haberlo hecho
    > explícito.
    > ⚠️ Queda **sin confirmar** si el "AIDA Skill Trainer" mencionado arriba es la misma AIDA
    > desplegada, una función suya, o un tercer artefacto. No asumirlo en ninguna dirección.
- **Auditoría de materiales existentes** (confirmado por el usuario, 2026-07-24): material
  recibido de **Learning** (contenido de formación existente), de **Marketing** (piezas y
  campañas), material que **los propios asesores** habían construido por su cuenta, y material
  bajado desde canales como el **Cartaplan**. Esto es evidencia operativa directa de por qué
  "Cartaplan/Manuales" aparece verde en el mapa (§2) pero "cartillas simplificadas" aparece
  amarillo — existe material, pero de origen disperso y sin curaduría única.

**Clusters del ecosistema:** Producto (Coberturas, Beneficios, Precio, Experiencia); Unidad de
Negocio e Inteligencia Comercial (nodo articulador central); Marketing (Benchmark, Speeches,
Cartillas); Palancas de Venta (Promociones, KPIs de performance y de experiencia); Espacio
Digital del Asesor (sistemas de perfilamiento, feedback con datos, Agente AI copiloto, canales de
soporte); Espacio Físico del Asesor (ambientación, Cartaplan); Seguimiento (monitoreo de
calidad); Formación (capacitaciones, supervisión/mentoría); Incentivos (salario, performance,
calidad/experiencia, permanencia cliente y asesor); Personalidad del Asesor (habilidades,
capacidades cognitivas, creencias/motivación); Selección (evaluaciones de entrada, rotación).

**Nodos críticos (🔴 rojo):** monitoreo de calidad, KPIs de experiencia (NPS EJO Venta),
sistemas de perfilamiento y gestión de ventas, benchmark, rotación de personal, incentivos por
calidad/experiencia, incentivos por permanencia del asesor.

**Nodos con potencial de mejora (🟡 amarillo):** KPIs de performance, precio,
supervisión/mentoría, capacitaciones, salario y beneficios, incentivos por performance, feedback
al asesor, canales de soporte, cartillas simplificadas, habilidades comerciales, capacidades
cognitivas, incentivos por permanencia del cliente.

**Nodos activados (🟢 verde):** coberturas, beneficios, experiencia, marketing, speeches,
promociones, Unidad de Negocio e Inteligencia Comercial, Agente AI copiloto (nodo emergente),
Cartaplan, ambientación funcional, creencias y motivación, evaluaciones de entrada.

**Enfoque metodológico:** diagnóstico basado en evidencia, sin soluciones todavía (Sección 1 del
documento maestro: hallazgos con evidencia; Sección 2: ejes de trabajo con evidencia). Se
mantiene coherencia entre el mapa visual y el documento diagnóstico, y entre ambos y Dx1-Dx3 (§1).

**Nota de reconciliación de terminología (2026-07-27, vía deck "Back to Basics — low-fi", lámina
06):** el deck presenta el mismo mapa agrupado en **"9 frentes"** — Producto, Palancas de venta,
Formación, Selección, Incentivos, Personalidad del Asesor, Seguimiento, Espacio Digital, Espacio
Físico — una simplificación de los 11 clusters listados arriba (no incluye "Unidad de Negocio e
Inteligencia Comercial" ni "Marketing" como frentes separados). No está confirmado si es una
consolidación deliberada o una simplificación de la lámina para audiencia ejecutiva — tratar
"9 frentes" como el lenguaje de presentación y los 11 clusters de arriba como el detalle
completo, hasta que se confirme cuál es la fuente de verdad vigente. El deck aclara además el
alcance de intervención: **Back to Basics interviene en Personalidad del Asesor, Formación, y
parte de Palancas de venta y Espacio Digital/Físico** — no en los 9 frentes completos.

**Cuatro hallazgos operativos del mapa (2026-07-27, vía el mismo deck, lámina 07) — reformulan
Dx1-Dx3 (§1) en términos más concretos, no los reemplazan:**
1. **Sobrecarga del asesor** — "Habilidades comerciales" y "Capacidades cognitivas" son los
   nodos con más conexiones entrantes de todo el mapa: onboarding, incentivos, monitoreo,
   materiales, IA, todo desemboca en el asesor en el momento de la venta. Versión operativa de
   Dx3.
2. **Lógicas que colisionan** — cada frente opera con su propia lógica sin coordinarse con las
   demás (incentivos, selección, formación, control); el mapa no muestra ningún nodo que las
   concilie — el único punto de encuentro es, otra vez, el asesor. Versión operativa de Dx1/Dx2.
3. **Experiencia desarticulada de cara al cliente** — sin estrategia unificada, cada asesor
   vende "a su manera"; el cliente hereda cualquier inconsistencia no resuelta antes. Consecuencia
   directa de Dx2.
4. **La queja es sobre el trato, no el consentimiento** — cuando el cliente se queja, rara vez es
   por consentimiento formal: es porque se sintió acosado o maltratado en el contacto. Precisión
   importante para el workstream de §3: riesgo legal (CUA) y experiencia del cliente son
   problemas relacionados pero **distintos** — resolver CUA no resuelve automáticamente la
   percepción de trato.

---

## 3. Estrategias de contacto FFVV (DS 016-2024-JUS)

Workstream paralelo al mapa: reemplazar la prospección en frío de la FFVV (Vida Individual) por
una escalera de 5 estrategias de contacto conformes con el Art. 26 de DS 016-2024-JUS.
Documento de referencia interno: `documento_maestro_estrategias_FFVV_v2.md` (no vive en este
repo).

> ### ⚠️ Lineamiento definitivo (2026-07-25, confirmado por Alejo — sustituye el estado "en
> escalera" de abajo)
>
> **Hoy solo pueden aparecer en el playbook estrategias que parten de consentimiento comercial
> ya existente. No va a haber ninguna estrategia para contactar a alguien que no tiene ese
> consentimiento — ni como excepción, ni como variante "diluida" de contacto en frío.** Esto no
> es una postura diplomática para la mesa con Legal/Cumplimiento (como se documentaba antes en
> esta sección) — es la regla de diseño que rige de aquí en adelante, y cierra por decisión
> propia (no solo por falta de validación de Compliance) a cualquier estrategia que dependiera de
> escribir primero para conseguir el consentimiento.
>
> **Lo que esto implica en la práctica:** el playbook del asesor solo puede documentar dos
> caminos — contactar directo a quien ya tiene CUA vigente, o esperar a que alguien sin CUA
> consienta por su cuenta (vía referente) antes de que el asesor le escriba. Ver el detalle
> aplicado en §6 (Resolución definitiva).
>
> **Actualización 2026-07-26 (confirmada por Alejo): el lineamiento pasa de "vigente — no
> definitivo" a definitivo, resuelto.** No hay contacto sin CUA, punto — ya no se presenta como
> un estado provisional sujeto a validación de Compliance.
>
> **Precisión legal agregada en esta misma actualización: ninguna base de datos armada a partir
> de referidos es legal — conlleva riesgo penal.** "Base de datos" incluye el caso más simple y
> más frecuente en la práctica: que un referente le pase al asesor el número de un familiar o
> amigo sin que esa persona haya dado su consentimiento — un solo número ya cuenta, no hace falta
> una lista. Esto cierra una ambigüedad que la Estrategia 4 dejaba abierta en la práctica (¿qué
> hace el asesor si el cliente simplemente le dicta un número?): la respuesta es que ese número no
> se recibe ni se guarda bajo ninguna circunstancia — ver el mecanismo concreto abajo.
>
> **Mecanismo concreto de la Estrategia 4, agregado en esta actualización: tarjeta del asesor con
> código QR.** El "enlace único" de la Estrategia 4 se implementa como una tarjeta (física o
> digital) con un código QR que apunta al formulario de toma de consentimiento — el cliente se la
> comparte a quien quiera recomendar, esa persona escanea el QR y decide por su cuenta si deja sus
> datos. El asesor no ve ni recibe ningún número hasta que eso ocurre. Aplicado directamente en el
> Playbook de la sesión, sección "Gestión de referidos" (Bloque 5) — antes marcada `(Pendiente)`.

**Estado de validación (histórico al 2026-07-20, mantenido por trazabilidad — ver el lineamiento
definitivo arriba, que reemplaza este estado):**
- Estrategia 1 (sondeo encubierto): cerrada/descartada.
- Estrategia 2 (gancho suave) y Estrategia 3 (solo-consentimiento): **cerradas (2026-07-25) —
  no por falta de validación de Compliance, sino porque por definición ambas requieren que el
  asesor escriba primero para obtener el consentimiento, lo cual el lineamiento definitivo ya no
  permite.** Antes figuraban como "pendientes, sin validación de CUA".
- **Estrategia 4 (autorregistro mediado por referente): única validada explícitamente por
  CUA — y ahora, con el lineamiento definitivo, la única vía para prospectos sin CUA, punto.**
  Principio no negociable: "RIMAC nunca escribe a un número que no se haya autorregistrado."
- Estrategia 5 (sorteo): válida como pauta/canal no dirigido (la persona se autoselecciona y
  consiente antes de cualquier contacto — compatible con el lineamiento definitivo); cerrada en
  su versión dirigida por el asesor.
- Estrategia 6 (segmentación por CUA vigente, documentada en la conversación de CUA pero no
  detallada antes en este node): lógica correcta y compatible con el lineamiento — no es una vía
  para contactar sin consentimiento, es una forma de saber quién ya lo dio antes de escribir —
  pero bloqueada en la práctica por un problema circular: verificar CUA suele requerir el DNI,
  dato que normalmente solo se obtiene después de haber contactado.

**Stakeholders:** Alejandro (Behavioral Design/CoE Experiencia, autor), Patricia (FFVV), Melissa
(Consentimiento/CUA), Dayana (Legal), Karen y María Alejandra (Compliance — validación final
pendiente sobre lo que quede vivo de la escalera, ahora reducida a Estrategias 4, 5 no dirigida y
6), Milagros (validó sorteo digital con Legal), Lorena (FFVV, a incluir en próxima sesión con
Compliance).

**Novedades abiertas:**
- Incentivo a referentes (pago solo al referente, vía YAPE/Plin) — CUA abrió la posibilidad,
  pendiente confirmación de Legal.
- FFVV propuso 4 cambios a reglas de Salesforce (bloquear contacto sin CUA, marcar contacto
  reciente, marcar negativa de contacto, marcar reclamos) — sin evaluación de factibilidad de
  Tecnología aún.
- **Tensión de mayor magnitud del proyecto, reencuadrada (2026-07-25):** ~80% del volumen de
  venta de FFVV dependía de prospección en frío sin CUA ni referido. Con el lineamiento
  definitivo, esto **deja de ser un problema que se resuelve encontrando una sexta estrategia de
  contacto** — no la va a haber. Pasa a ser un problema que se compensa distinto: con la calidad
  de las conversaciones que sí se pueden tener (modelo de 4 pasos, manejo de objeciones,
  postventa — todo lo que sí vive en el playbook), no con más volumen de contacto. Ver la
  "Oportunidad: Compensar el impacto de CUA" en la presentación del proyecto, y la nota que se
  agregó al propio playbook en §6.

**Conexión con el mapa sistémico:** la Estrategia 4 y la falta de trazabilidad del canal FFVV son
consistentes con los nodos críticos ya identificados en rojo en §2: "Sistemas para perfilamiento
y gestión de ventas" y "Monitoreo de calidad" — y con Dx2 (§1): el usuario recibe información
inconsistente porque los elementos del sistema no conversan entre sí.

**Conexión con el riesgo legal ya documentado en el proyecto** (ver
[[transicion-venta-fria-a-opt-in|Transición de venta fría a opt-in]] y tesis 8 de
`research/lobo/opinion_experto.md`): Pacífico Seguros —competidor directo— ya está bajo
investigación de INDECOPI por el mismo patrón (call center tercerizado sin autorización, F-117);
BBVA fue sancionado dos veces (F-118, F-138). El 80% de volumen sin cobertura de ninguna de las 5
estrategias es, en términos de esa evidencia externa, la exposición legal activa más grande del
proyecto — no un detalle operativo.

---

## 4. Playbook del Asesor (VF)

Documento de referencia interno: `Playbook_del_asesor - VF.md`, RIMAC Seguros 2026, Vida
Individual. Es el manual dirigido al asesor de venta (distinto del documento de estrategias de
contacto de §3, que es el paper legal/behavioral para la mesa con Legal/Compliance/CUA; ambos son
parte del mismo workstream FFVV, bajo el marco del Modelo de Experiencia de Venta Vida de §1).

**Estructura:** 5 bloques sobre un journey de cliente de 5 momentos (Awareness/consideración →
Primer contacto → Explicación del producto → Aceptación → Postventa/Medición) — el mismo journey
usado en la visión To Be de la Mesa Back to Basics FFVV (§1).
- Bloque 1: quiénes somos / cultura RIMAC.
- Bloque 2: rol del asesor.
- Bloque 3: generando awareness — social selling, identidad digital (WhatsApp/Google/
  LinkedIn/Instagram).
- Bloque 4: la conversación — venta consultiva de 4 pasos (motivación → dimensionamiento →
  perfil financiero → propuesta) + manejo de objeciones con 9 estrategias C.1-C.9 basadas en
  sesgos cognitivos.
- Bloque 5: postventa — toques Mes 1/6/9, renovación Mes 12.
- Apéndice: Índice de Confianza Profesional (autoevaluación del asesor).

**Secciones marcadas "Pendiente" en el documento original:**
- "Estrategia de contacto inicial — CUA" (Bloque 3) — dependía directamente del workstream de §3
  (**resuelto de verdad el 2026-07-25**, ver §6 "Resolución definitiva" — la resolución anterior
  del 2026-07-20 no estaba realmente aplicada, esta sí).
- Banco de recursos de marketing para repostear (Bloque 3).
- FAQ de coberturas específicas, exclusiones, qué pasa si el cliente deja de pagar (Bloque 4).
- **Flyers de venta (Bloque 4, agregado 2026-07-26):** formato definido — 1 JPG por producto real
  (VFP, Plan Vida Flexible, Vida Contigo, Vida Temporal Total) + 1 JPG comparativo para compartir
  pantalla en conversación (no para chat). VCD digital/Endosable digital quedan sin flyer hasta
  que se confirmen como producto real (ver [[matriz-productos-vida-rimac|Matriz de productos Vida
  RIMAC]] §1). Pendiente que el usuario adjunte los 5 JPG.
- Gestión de referidos e indicadores de negocio (Bloque 5).
- Certificación e incentivos, esquema remunerativo (Apéndice).
- Meta de reviews en Google (15 reviews, 4.8+) — por validar.

**Conexión con el mapa sistémico:** el playbook es evidencia operativa de varios nodos ya
mapeados en §2 — Cartaplan/Manuales (verde); Capacitaciones y Habilidades comerciales (amarillo,
con contenido tangible de venta consultiva y manejo de objeciones); el vacío de "Sistemas para
perfilamiento y gestión de ventas" (rojo) se refleja en que el modelo de 4 pasos vive solo en
este documento, sin integración con Salesforce.

---

## 5. Playbook vs. evidencia (cruce con `seeker` y tesis del Lobo)

Revisión cruzada (2026-07-20) del Playbook contra el skill `seeker` (rigor evidencial) y
`research/lobo/opinion_experto.md` (tesis de negocio, ledger de fuentes `F-n`). Esta sección es
el puente directo entre el conocimiento interno del proyecto (§1-4) y la evidencia externa que ya
sostiene el resto de este hub.

**Hallazgo 1 — asimetría i-frame/s-frame.** El playbook es casi enteramente i-frame (marca
personal, guiones, manejo de objeciones). La **tesis 6** del Lobo (confianza Alta — F-16 a F-21,
todas 🟢A) y la **tesis 7** (confianza Alta — F-19, F-23) sostienen que el diseño de
producto/sistema (s-frame) supera al nudge cosmético individual. Ver también
[[behavioral-design-estado-disciplina|Behavioral design: estado de la disciplina]] §⚖️ Síntesis,
punto 2 ("Del mensaje al producto"). La única pieza s-frame real del proyecto es el ecosistema
Estar Bien (Pilar 2, no detallado en el conocimiento consolidado). El resto —incluidos Bloques 3
y 4 del playbook— optimiza al asesor, no al sistema, mientras los nodos rojos del mapa AS IS
(§2) siguen sin resolverse estructuralmente. **Esto es, en el lenguaje oficial de §1, una
manifestación directa de Dx3** (el asesor recibe herramientas i-frame que le piden más de él, no
menos carga) **sin haber resuelto Dx1/Dx2 primero** — las palancas s-frame propuestas en la Mesa
Back to Basics (§1: plataforma de leads, copiloto, alertas de churn) son la respuesta pendiente.

**Hallazgo 2 — hueco de citas en Bloque 4 (✅ cerrado 2026-07-24, con una corrección).** Bloque 3
(imagen/presencia digital) estaba bien citado con literatura nivel A, aunque son estudios de
laboratorio con validez ecológica limitada para conversión real. Bloque 4 (manejo de objeciones
C.1-C.9, donde se juega el cierre de venta) no citaba ninguna fuente para ninguno de los 9 sesgos
que nombraba. Revisión dedicada (2026-07-24, análisis con el Lobo, esta vez sobre el documento
real `Playbook_del_asesor.md` — la primera pasada había trabajado solo con el resumen, que no
traía la numeración C.n exacta) encontró la cita académica fundacional para 8 de los 9 y una
corrección importante para el noveno:

| Estrategia C. | Nombre en el Playbook | Sesgo/técnica | Fuente académica | Nota |
|---|---|---|---|---|
| C.1 | Referentes sociales | Prueba social | Cialdini & Goldstein 2004 (F-224, 🟢A) | Sistematiza el trabajo de Cialdini (*Influence*, 1984) |
| C.2 | Punto de referencia | Anclaje | Tversky & Kahneman 1974 (F-220, 🟢A) | Complementa a F-175 (aplicación 2022 a precio) |
| C.3 | Proteger lo que ya tienes | Dotación (endowment) | Kahneman, Knetsch & Thaler 1990 (F-223, 🟢A) | — |
| C.4 | El costo de esperar | Sesgo del presente | Pitthan & De Witte 2021 (F-3, 🟢A) | Mismo paper que ya sostiene `sesgo_presente` en el modelo `lapuerta` — identifica miopía y narrow framing como mecanismos específicos |
| C.5 | Lo que está en riesgo | Aversión a la pérdida | Kahneman & Tversky 1979 (F-221, 🟢A) | Prospect Theory, base del Nobel 2002 |
| C.6 | Cuando la decisión se posterga | Decisión conjunta / difusión de responsabilidad entre quienes deciden | **Corregida 2026-07-25:** Davis 1976 (F-236, 🟢A) — reemplaza a Darley & Latané 1968 (F-226, 🟢A, conservada por trazabilidad) | La fuente original (emergencias con testigos) tenía encaje no verificado con objeciones de venta 1-a-1, tal como ya advertía esta misma fila; Davis (1976, *Decision Making Within the Household*) sí describe directamente el fenómeno de la objeción — una decisión de compra compartida en pareja/familia, no una emergencia. Corrección a pedido del usuario. |
| C.7 | **Renombrada 2026-07-25:** "Poner el precio en perspectiva (anclaje aplicado)" (antes "Poner el precio en contexto") | Anclaje | Tversky & Kahneman 1974 (F-220, 🟢A) — mismo mecanismo que C.2 | **Aplicado el cambio recomendado el 2026-07-24:** ya no cita "la regla del 10x" (Cardone 2011, F-227, 🔴E — no era un sesgo cognitivo, quedó registrada en el ledger solo como hallazgo de la corrección); la técnica se cita ahora con su mecanismo real (anclaje, mismo que C.2/C.8), sin cambiar el contenido del ✗/✓ ni los tips. |
| C.8 | Tu ingreso es tu mayor activo | Encuadre (framing) | Tversky & Kahneman 1981 (F-222, 🟢A) | Mismo mecanismo que C.5, aplicado a redacción de la oferta |
| C.9 | Números claros | Facilidad cognitiva | Alter & Oppenheimer 2009 (F-225, 🟢A) | Base académica de un término popularizado por Kahneman (2011) |

Sigue siendo lo inverso de cómo debería repartirse el rigor visible en el documento original (la
sección de menor validez ecológica tenía más cita que la sección donde se decide si la venta se
cierra) — pero el respaldo evidencial ya existe y ya se insertó directamente en el documento
`Playbook_del_asesor.md` (2026-07-24, ver nota de aplicación abajo). El pendiente de §7 ("agregar
respaldo evidencial a C.1-C.9") queda **resuelto**, con la corrección de C.7 aplicada como nota
en el documento (no se retiró la sección — se marcó para decisión del equipo).

**Hallazgo 3 — tensión con tesis 1 y 6 del Lobo.** La **tesis 1** (divulgación/comprensión es
palanca de conversión débil, confianza Alta — F-9 RCT N≈124k, F-10, F-124 específico de seguros)
tensiona con el supuesto implícito de que "hablar claro" mueve el cierre — la evidencia dice que
mejora comprensión/retención, no conversión (F-22, RGA/SOA). La **tesis 6** (testear en la propia
población, no importar de catálogo) aplica directo a reglas del Bloque 3 (foto, vestimenta,
mimetismo postural): son prescripciones importadas de papers sin validación en la fuerza de venta
real de RIMAC.

**Lo que sí se sostiene:** el modelo de 4 pasos de venta consultiva ataca bien el cuello de
botella #1 en comprensión de seguros — coaseguro/retorno variable (F-6, F-7 — ver **tesis 2** del
Lobo) — resolviéndolo en el punto de venta, no solo con más divulgación genérica. Es la parte del
playbook mejor alineada con la evidencia dura del ledger.

**Implicación para cualquier propuesta de intervención sistémica derivada de este proyecto:** no
recomendar solo más entrenamiento/guiones de asesor (i-frame) sin señalar que la evidencia de
mayor ROI apunta a rediseño de producto/sistema (s-frame) — coherente con los nodos rojos del
mapa AS IS 2026 (§2) y con las palancas s-frame ya propuestas en la Mesa Back to Basics (§1).

---

## 6. Bloque 4 vs. estado real de CUA — descalce y resolución

Revisión (2026-07-20) del Bloque 4 · "Momento 2 · Primer contacto" del playbook contra el estado
real de validación CUA documentado en §3.

**Hallazgo 1.** El speech "referido" original tenía al asesor escribiendo directo al referido
usando información de segunda mano ("[Referente] me comentó que..."). Esa es la mecánica de la
Estrategia 2 (no validada) — Legal (Dayana) advirtió que "no es riesgo cero, RIMAC sigue
iniciando el contacto" — y viola el principio no negociable de la Estrategia 4.

**Hallazgo 2.** Faltaba el speech de la única estrategia validada: en el flujo real de la
Estrategia 4, el referente envía el mensaje de Fase 1 por su propio WhatsApp; el asesor solo
contacta después del autorregistro y consentimiento vía formulario (Fase 3). Ese script no
existía — era el hueco más importante del playbook.

**Hallazgo 3.** El speech "en frío" no calzaba con ninguna estrategia de la escalera (ni las
pendientes): sin referente, formulario ni vínculo previo. Era el de mayor riesgo real, pero
recibía la misma advertencia genérica que "contexto previo" (de menor riesgo) — sin
diferenciación de severidad.

**Resuelto (2026-07-20):** se reescribió "Speech de primer contacto" (Bloque 4) en
`Playbook_del_asesor - VF (v3 rutas de contacto CUA).md` (documento interno). Se retiraron el
speech "en frío" y el "referido" original (con nota de trazabilidad). Quedaron dos rutas:
- **Ruta 1 · Contacto a través de referentes** (Estrategia 4, con Fases 1/2/3 explícitas,
  incluye el script de Fase 3 antes faltante).
- **Ruta 2 · Mensajes para clientes con CUA** (nueva — contactos con consentimiento ya
  registrado por cualquier canal legítimo: cliente existente, sorteo/pauta no dirigida
  Estrategia 5, u otro canal que Legal valide).

También se actualizaron los dos placeholders de Bloque 3 que apuntaban a esta sección
("Estrategia de contacto inicial — CUA" y la nota de WhatsApp) para que dejen de decir
"pendiente" y apunten a las rutas nuevas.

**Nota de coherencia con la evidencia externa:** este rediseño (dos rutas explícitas, ninguna en
frío) es exactamente lo que la evidencia externa de
[[transicion-venta-fria-a-opt-in|Transición de venta fría a opt-in]] recomienda — no existe caso
documentado de transición frío→opt-in sin abandonar por completo el contacto sin consentimiento
previo; intentar mantener una versión "diluida" del contacto en frío (como hacía el speech
retirado) es el mismo patrón de riesgo que ese node señala en el caso del Do Not Call Registry
(empresas que migraron la táctica en vez de cambiar el modelo de fondo).

**Resolución definitiva (2026-07-25, aplicada directamente por Alejo al documento de la
sesión).** La "resolución" de 2026-07-20 de arriba resultó, tras verificación directa contra
`Playbook_del_asesor.md` el 2026-07-24, **no estar realmente aplicada** — el placeholder
"Pendiente" seguía en el documento en uso, y el Plan Piloto (§8) corroboró el mismo vacío de
forma independiente (ver Limitaciones). El 2026-07-25 se cerró de verdad, con el lineamiento
definitivo de §3 aplicado directamente al documento de la sesión (no a un archivo `v3` aparte que
después no se usó):

- **"Estrategia de contacto inicial — CUA" (Bloque 3) ya no dice "Pendiente".** Contiene la regla
  completa, marcada explícitamente como "vigente — no definitivo": Ruta 1 (CON CUA, 3 orígenes
  cerrados) y Ruta 2 (SIN CUA → único camino es el autorregistro mediado por referente, contacto
  solo después de que la persona consiente por su cuenta).
- **El bug recurrente del Hallazgo 1 volvió a aparecer y se corrigió otra vez.** Al incorporar
  contenido de una versión distinta del playbook (`Playbook_del_asesor__VF_2.md`, 2026-07-25) se
  trajo, sin querer, la misma mecánica que el Hallazgo 1 ya había señalado el 2026-07-20: el
  speech "cliente llega referido" hacía que el asesor escribiera directo a la persona referida con
  información de segunda mano. Se corrigió en el momento, alineándolo con la Ruta 2 (el asesor
  contacta solo después de que el referido ya se autorregistró y consintió). **Lección para este
  proyecto:** este error no es un despiste puntual — es el patrón de riesgo más fácil de
  reintroducir sin querer cada vez que se combina contenido de distintas versiones del playbook;
  cualquier fusión futura de material debe revisar explícitamente los speechs de primer contacto
  contra la Ruta 2 antes de aceptarlos.
- **El "80% de volumen sin CUA" deja de tratarse como pendiente de resolver con una estrategia
  nueva** (ver §3, reencuadre 2026-07-25) — el propio Bloque 3 del playbook ahora dice
  explícitamente que el documento mismo (mejor conversación, no más contactos) es la forma en
  que se compensa ese impacto.

Esto **sustituye** la resolución de 2026-07-20 como estado verificado — no como un evento
adicional. La brecha "lo que el proyecto dice que está resuelto" vs. "lo que el documento real
dice" que motivó la Limitación de abajo queda cerrada para esta sección específica, aunque el
documento aplicado (`Playbook_del_asesor.md`) sigue sin vivir en este repositorio.

---

## 7. Pendientes activos (al 2026-07-23)

- ~~Validación final de Compliance (Karen, María Alejandra) sobre Estrategias 2 y 3~~ — **ya no
  aplica (2026-07-25)**: Estrategias 2 y 3 quedaron cerradas por decisión de diseño (lineamiento
  definitivo, §3), no por falta de validación de Compliance. Lo que sí sigue pendiente de
  Compliance es la validación de lo que quedó vivo: Estrategia 4, Estrategia 5 no dirigida y
  Estrategia 6.
- Confirmación de Legal sobre incentivo a referentes (pago vía YAPE/Plin).
- Evaluación de factibilidad de Tecnología para los 4 cambios propuestos a reglas de Salesforce.
- **El 80% del volumen de venta que dependía de prospección en frío sin CUA ni referido sigue sin
  cobertura de contacto — pero con el lineamiento definitivo (§3), esto ya no se trata como un
  pendiente a resolver con una sexta estrategia.** Queda como pendiente de negocio real (cuánto
  volumen se pierde, cómo se compensa con retención/referidos/conversión), no como pendiente de
  diseño de estrategia de contacto.
- ~~Bloque 4 del playbook: agregar respaldo evidencial a las 9 estrategias de manejo de
  objeciones (C.1-C.9)~~ — **resuelto (2026-07-24)**, ver Hallazgo 2 de §5: citas insertadas
  directamente en `Playbook_del_asesor.md`. ~~Queda pendiente que el equipo confirme si retirar o
  renombrar C.7~~ — **resuelto (2026-07-25):** el usuario confirmó renombrarla ("Poner el precio
  en perspectiva (anclaje aplicado)"), aplicado directamente en el playbook y en la tabla de §5.
  También se corrigió la fuente de C.6 (Davis 1976 reemplaza a Darley & Latané 1968).
- Secciones aún "Pendiente" del playbook: banco de recursos de marketing, FAQ de
  coberturas/exclusiones, gestión de referidos e indicadores (Bloque 5), certificación e
  incentivos (Apéndice), meta de reviews en Google.
- Conectar el "Índice de Confianza Profesional" con datos reales de conversión para que deje de
  ser un nudge de catálogo (coherente con **tesis 6** del Lobo: no copiar tamaño de efecto de
  catálogo, testear en la propia población).
- **(nuevo, 2026-07-23)** Visión To Be de la Mesa Back to Basics FFVV (§1: journeys + 16
  palancas) está preliminar — pendiente de priorización con Producto, Estrategia de Clientes y
  Canal. No tratar las 16 palancas como roadmap comprometido todavía.
- **(nuevo, 2026-07-23)** En próximos materiales para el VP o audiencias de dirección de canal:
  liderar con el mapa sistémico y Dx1-Dx3 (§1-§2) antes de mostrar iniciativas puntuales — regla
  de narrativa ya aprendida, no repetir el error de abrir con piezas sueltas.

---

## 8. Plan Piloto de validación del modelo (10 asesores, agosto 2026)

Documento interno "Plan Piloto · Modelo de Experiencia de Venta Vida" (CoE Diseño Estratégico,
v1, julio 2026 — no vive en este repositorio). Es el diseño de validación de campo del modelo
descrito en §1, antes de decidir su implementación en AIDA.

**Objetivo general:** validar la recepción del modelo en un grupo de asesores en operación —
si lo comprenden, lo aplican y lo incorporan a su forma de trabajar a través del agente — y qué
le falta al modelo para sostenerse cuando se implemente. **No es un experimento comercial**: en
dos semanas no se espera (ni se busca) movimiento en tasa de cierre.

**Objetivos específicos**, en dos ejes:
- Eje 1 · El modelo — OE1 Comprensión (día 1: ¿el asesor interioriza el modelo como recorrido, no
  como colección de técnicas?), OE2 Aplicación (campo: ¿respeta la secuencia — motivación antes
  que producto, dimensiona un número, cierra pidiendo un siguiente paso?), OE3 Suficiencia del
  contenido (¿qué le pide el asesor al agente que hoy no está resuelto?).
- Eje 2 · El agente — OE4 Adopción (¿cómo se integra a la rutina real, y sigue volviendo después
  de la novedad inicial?).

**Tres premisas de diseño:** (1) el asesor interactúa con una sola herramienta, el agente — el
playbook es la base de conocimiento que lo alimenta, no una superficie de uso paralela; (2) dos
fases con lógicas distintas — transferencia (día 1) y puesta en acción (dos semanas) — para
diagnosticar *dónde* está el problema, no solo constatar que existe; (3) no es experimento
comercial, ver arriba.

**Muestra — 10 asesores**, compuesta por antigüedad, territorio y forma de originar demanda (no
para comparar rendimiento, sino para detectar si el modelo asume condiciones que no todos
tienen): 4 de 6 meses de antigüedad, 4 de 2-3 años, 2 con rasgo diferencial (asesor diamante,
generador de contenido en redes); 6 Lima, 2 Arequipa, 2 Cuzco/Trujillo; orígenes de demanda
mixtos (pauta digital, contenido propio, cartera propia, flujo estándar).

**Desarrollo:**
- **Día 1 — sesión de transferencia (90 min):** estructura del playbook (10 min); *la asesoría*
  (el modelo de 4 pasos, 25 min — el bloque con más tiempo asignado, "es el corazón"); *social
  selling en acción* (25 min, se hace ahí mismo con acompañamiento de la CoE: foto profesional,
  historia profesional en 3 partes, perfiles y firma — no queda como tarea, porque "si sale como
  tarea para después, no se hace"); el agente (15 min, cómo se usa, los dos modos, entrega de
  accesos); ejercicio de comprensión (15 min, mide OE1).
- **Ejercicio de comprensión — 4 casos**, aplicados el día 1 y el día de cierre (mismos casos,
  para leer el delta): Caso A (primer contacto en frío — revela si evita mencionar
  producto/precio en el primer mensaje), Caso B (el cliente salta al precio — revela si redirige
  con una pregunta en vez de dar un precio suelto o negarse en seco), Caso C (dimensionar una
  meta — ej. universidad de una hija — el número sale del costo de la meta), Caso D (dimensionar
  protección — el número sale de lo que la familia dejaría de percibir, no de una meta con precio
  conocido). C y D exigen razonamientos distintos a propósito: un asesor puede resolver bien uno
  y fallar en el otro, y ese contraste ya es un hallazgo sobre qué reforzar.
- **Dos semanas de campo:** agenda del piloto (inicial + viva, declarada por el asesor, columna
  vertebral de qué observar); shadowing continuo por cobertura (todo asesor al menos una vez,
  provincia por videollamada); bitácora post-conversación (3 preguntas, 30 seg, por WhatsApp);
  cierres de semana (10 min, reflexivos, los viernes ×2). **Principio de diseño explícito: la
  carga de recolección es de la CoE, no del asesor** — todo lo que se pueda levantar sin
  preguntarle, se levanta sin preguntarle.
- **Cierre:** consolidación de hallazgos, sesión con líderes de venta, priorización de vacíos de
  contenido, decisión sobre implementación en AIDA.

**Indicadores (6):** comprensión inicial y su delta al cierre; cobertura de uso (tasa, no conteo
— en cuántas de sus interacciones reales usó el agente); conversaciones que respetan la
secuencia del modelo (shadowing); momento de uso respecto de la interacción (antes/durante/
después); consultas sin respuesta satisfactoria y temas más consultados (insumo directo para la
v2 del contenido); **brecha comprensión → aplicación** (cruce comprendió×aplicó — distingue si un
fallo en campo es "brecha de activación" [comprendió pero no aplica: problema de agente/
acompañamiento/contexto] de "brecha de transferencia" [no comprendió: problema de cómo se enseña
el modelo] — sin esta medición, cualquier falla en campo se leería como "no les gustó el modelo",
sin decir qué arreglar).

**Alcance y limitaciones declaradas por el propio documento:**
- Fuera de alcance: Bloque 5 (postventa, opera en hitos de mes 1/6/9) e indicadores comerciales
  (el ciclo de venta de Vida excede el plazo del piloto — un movimiento en conversión sería
  direccional, no concluyente).
- Dependencia técnica: el tracking del prototipo no existe todavía (hay que habilitarlo antes del
  24/07); el acceso de los 10 asesores al agente requiere asiento activo en el Team/Enterprise de
  Claude de RIMAC (a confirmar antes del 24/07).
  > ⚠️ **CORRECCIÓN (2026-08-14, confirmada por Alejo — ver v1.5 en la cabecera).** Esta viñeta
  > decía antes que este hecho técnico "confirma que AIDA es un prototipo construido sobre
  > Claude". **Es falso, y era una conflación de dos herramientas distintas.** El agente del Plan
  > Piloto —el que requiere asiento en el Team/Enterprise de Claude— es un **prototipo construido
  > sobre Claude**, hecho para este piloto. **AIDA es otra cosa: la herramienta creada con
  > Copilot que ya está desplegada en producción para la fuerza de ventas.** El documento del
  > Plan Piloto habla de "el agente" y este node leyó "el agente" como AIDA; no lo es.
  > ⚠️ **Además, el Plan Piloto de esta sección cambió** (avisado por Alejo el 2026-08-14,
  > actualización pendiente de recibir): tratar todo el §8 como **descripción histórica del
  > diseño de julio 2026**, no como el plan vigente.
- **Vacíos de contenido conocidos, declarados explícitamente por el propio Plan Piloto: "La
  Estrategia de Contacto Inicial (CUA) sigue pendiente."** Esto **corrobora de forma
  independiente** el hallazgo de la revisión directa del playbook real (línea 131,
  `_(Pendiente — Alejo)_` — ver Limitaciones de este node): la brecha entre "lo que la
  documentación interna del proyecto da por resuelto" (§6 de este node) y "lo que está escrito en
  el documento fuente" no es una lectura desactualizada de una sola revisión — el equipo que
  escribió el Plan Piloto, trabajando en paralelo, llegó a la misma conclusión sin que se le
  señalara. **Tratar la resolución descrita en §6 como no verificada hasta confirmar contra el
  documento fuente actual.**

**Hitos comprometidos:** envío de playbook y artefactos + selección de asesores (vie 24/07, CoE/
Producto y Líderes de Venta); revisión de playbook y artefactos (mar 04/08, Líderes de Venta y
Producto); inicio de piloto (vie 07/08, CoE).

**Conexión con §1 y §2:** este piloto es la validación de campo del modelo cuyo diseño se
describe en §1 (statement, pilares, motivaciones, journey) y de la hipótesis de copiloto descrita
en §2 — sus resultados (indicador 6 en particular) son el insumo directo para decidir si las 16
palancas de la Mesa Back to Basics (§1) pasan de preliminares a priorizadas.

---

## Limitaciones

- Este node consolida documentos internos de RIMAC (no públicos, subidos directamente a la
  sesión en dos entregas: 2026-07-21 y 2026-07-23) — no es investigación con fuentes externas
  nuevas; las citas `F-n` que aparecen aquí ya estaban registradas en `research/fuentes/codice.md`
  antes de este node.
- Los documentos de referencia citados (`documento_maestro_estrategias_FFVV_v2.md`,
  `Playbook_del_asesor - VF.md` y su v3, el deck "Modelo de Experiencia de Venta Vida", "Plan
  Piloto · Modelo de Experiencia de Venta Vida" de §8) **no viven en este repositorio** — este
  node resume su contenido relevante, no los reemplaza como fuente primaria interna.
- **La resolución descrita en §6 (Bloque 4 vs. CUA) no estaba verificada contra el documento
  fuente actual — actualizado (2026-07-25): la "Resolución definitiva" de §6 sí se aplicó
  directamente al documento de la sesión** (verificado porque se hizo en esta misma sesión, no
  por revisión posterior). **Actualizado (2026-07-26): `Playbook_del_asesor.md` ya vive en este
  repositorio** — el usuario lo adjuntó y quedó persistido en
  `research/_fuentes_internas/Playbook_del_asesor.md` (v1.0 · jun 2026 · borrador interno,
  contenido verificado contra este node el mismo día: coincide con el estado que §3/§6 ya
  documentaban — 2 rutas de contacto CUA, sin speech "en frío"). Esto cierra la limitación de
  fondo que motivó esta nota: el archivo deja de depender de sobrevivir solo en el estado de una
  sesión externa y ya puede versionarse y auditarse como el resto de este repo. Si se genera una
  versión más nueva del Playbook fuera de esta sesión, hay que volver a subirla aquí para que este
  node y el archivo persistido no diverjan otra vez.
- **El mapa AS IS 2026 (§2) existe como diagrama visual** (compartido en la sesión el
  2026-07-24) pero no se pudo persistir el archivo de imagen en este repo — este node solo
  guarda su lectura textual (clusters, semáforo de nodos). Si se necesita el diagrama en sí para
  un output (p. ej. una lámina de presentación), debe volver a compartirse en la sesión donde se
  construya ese output.
- El 80% de volumen sin cobertura legal (§3, §7) es la tensión central no resuelta del proyecto a
  la fecha de consolidación (2026-07-23) — cualquier lectura de este node debe tratarlo como
  pregunta abierta activa, no como riesgo ya mitigado.
- La Visión To Be y sus 16 palancas (§1) son preliminares y no priorizadas — no citarlas como
  compromiso de roadmap en materiales externos al proyecto.

---

## Conexiones

- [[diagnostico-copiloto-ai-asesor-vida-rimac|Diagnóstico del Copiloto AI del asesor de Vida]] —
  proyecto **asociado** a este (no una sección suya, abierto 2026-08-14): diagnostica la herramienta
  de IA que usa el asesor, cuyo defecto de consistencia ya aparecía aquí por triplicado (encuesta a
  19 asesores: "no da la información adecuada"; Taller de Manejo de Objeciones: "consistencia del
  copiloto de IA"; backlog de corto plazo, frente #1). Ese node hereda de aquí los datos primarios y
  el Plan Piloto (§8), cuyo indicador de "consultas sin respuesta satisfactoria" es su insumo
  directo. ⚠️ **Resolvió una ambigüedad que este node tenía mal documentada:** aquí AIDA se
  describía como prototipo **sobre Claude**; es falso — AIDA es la herramienta de **Copilot ya
  desplegada**, y el prototipo sobre Claude es el del Plan Piloto. Ver la corrección v1.5 en la
  cabecera y las notas en línea de §2 y §8.
- [[matriz-productos-vida-rimac|Matriz de productos Vida RIMAC — catálogo y coberturas]] —
  catálogo de qué cubre y cuánto cuesta cada producto real (VFP, Plan Vida Flexible, Vida
  Contigo, Vida Temporal Total); insumo directo del Bloque 4 del Playbook del Asesor (§4 de ese
  node, "venta consultiva de 4 pasos" — motivación → dimensionamiento → perfil financiero →
  propuesta) y del ejercicio de dimensionamiento del Plan Piloto (§8 de ese node, Casos C y D) —
  incluye el caveat de no citar "170%" de devolución como cifra fija, relevante para cualquier
  material de este proyecto que mencione Vida Contigo. VCD digital y Endosable digital, que
  aparecen en el Playbook del Asesor, quedan pendientes — no confirmados como producto real
  distinto (§1 de ese node).
- [[glosario-seguro-vida-peru|Glosario de seguro de vida en lenguaje claro]] — investigación
  `/trinidad` (2026-07-24) que completó la sección "Preguntas frecuentes de producto" del
  Playbook del Asesor (Bloque 4, Momento 4) con un glosario de cliente; hallazgo clave: la
  barrera real no es vocabulario técnico sino precio percibido y desconfianza de fondo.
- [[transicion-venta-fria-a-opt-in|Transición de venta fría a venta opt-in]] — evidencia externa
  que sostiene el diseño de las 5 estrategias de §3 y la resolución del Bloque 4 en §6; ese node
  documenta que ninguna transición real evita contracción de volumen, directamente relevante al
  pendiente del 80% en §7.
- [[behavioral-design-estado-disciplina|Behavioral design: estado de la disciplina]] — sostiene
  el Hallazgo 1 de §5 (i-frame vs. s-frame) y la evaluación de por qué el playbook necesita
  rediseño de producto, no solo más guion — conecta directo con Dx3 (§1).
- [[material-visual-venta-consultiva|Material visual en la venta consultiva]] — aplica
  directamente al Bloque 4 (materiales que acompañan la conversación de venta) y a la brecha de
  citas señalada en el Hallazgo 2 de §5.
- [[futuro-asesores-seguros-venta-digital|¿Desaparecerán los asesores de seguros?]] — sostiene
  por qué invertir en el asesor (Formación §4, Espacio Digital del Asesor §2) es la apuesta
  correcta para Vida Individual, un producto complejo — y por qué la Visión de solución de §1
  ("la tecnología potencia al asesor, no lo reemplaza") tiene respaldo externo, no es solo
  postura interna.
- `research/lobo/opinion_experto.md` (subsistema fuera del alcance de `alma.md`, ver `CLAUDE.md`)
  — tesis 1, 2, 6, 7, 8 y 16 sostienen directamente los hallazgos de §5 y §6; este node es, en la
  práctica, la aplicación operativa de esas tesis a un proyecto real de RIMAC.
- `research/_outputs/back-to-basics-presentacion-milagros-2026-07-23.md` — output construido
  sobre una versión más resumida de este mismo proyecto (el documento "Back to Basics" de alto
  nivel, previo a que se sumara el marco de §1); este node es la capa de detalle y de marco
  narrativo (Dx1-Dx3, statement, pilares) que ese output no cubría todavía.
- `research/_outputs/back-to-basics-presentacion-lowfi-2026-07-27.html` — deck de 17 láminas
  (low-fi, para Milagros), persistido tal cual el 2026-07-27; es la fuente de la mayoría de las
  adiciones de esta versión v1.4 del node (origen del pedido, regla metodológica, hallazgos
  previos, encuesta a 19 asesores, Taller de Manejo de Objeciones, Universidad Vida, backlog
  estructurado, Espejo/Transformación-AMI, entregables del equipo). Más reciente y más completo
  que el output de 2026-07-23 citado arriba — ver también sus dos láminas explícitamente nuevas
  (04 y 17, "añadidas a pedido, no están en el reporte original" según su propio endnote).
- [[tendencias-diseno-innovacion|Tendencias en diseño e innovación: qué tiene impacto real y qué es propuesta]] — sus
  reglas C1 y C2 (argumentar por **mecanismo**, no por multiplicador; prometer **acumulación**, no
  transformación) aplican directamente a cómo se sustenta ante el VP el valor del rediseño de la
  experiencia de venta.
