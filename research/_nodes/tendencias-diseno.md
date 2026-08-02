# Tendencias en diseño: qué tiene impacto real y qué es propuesta

> Documento de investigación **acumulativo**. Fuente persistente y versionada en el repositorio.
> Fecha de elaboración: 2026-07-26 · Última actualización: 2026-08-02 · Versión: v3.0 (iteración 3)
> Origen: `/trinidad` — investigación de 360° (empírica + social + negocio)
> Pregunta permanente: **¿qué tendencias de diseño tienen impacto tangible demostrado y
> cuáles son propuestas innovadoras todavía sin respaldo?**
> Fuentes registradas en `research/fuentes/codice.md` (F-237 a F-328 · iter. 2: F-380 a F-398 ·
> iter. 3: F-399 a F-429).
>
> **Lo último (iteración 3, 2026-08-02) — la iteración en que el node se auditó a sí mismo.**
> El hallazgo que la iteración 2 celebró como su mejor aporte —el **impuesto de verificación**
> que reconciliaba la divergencia ⚔️ de productividad con IA— **no resiste su propio chequeo de
> eco de cita**: la cifra ancla (4,3 min senior vs. 1,2 min junior) no tiene fuente primaria
> rastreable y muere en un blog sin arbitraje que dice "in a recent study…" sin nombrar nada
> (F-404). Es la **sexta cadena de eco** del node y la primera que estaba *adentro*. **H19 se
> degrada.** En paralelo: **H20 se confirma con margen** (13/13 = 100% de las cifras atribuidas
> en el corpus hispanohablante vienen de emisores anglosajones interesados — y tres de ellas se
> atribuyen a un Gartner que nunca las publicó), **H5, H10, H11 y H15 pasan a `parcial`**, y el
> **desmentido oficial de MercadoLibre** vuelve contestado el caso testigo con el que la
> iteración 2 refutó H17. Ver §11.

## 🔁 Cómo se usa y se enriquece este node

Este node **no se reescribe en cada iteración: se confronta**. Es la memoria larga del proyecto
sobre diseño, y su valor está en acumular criterio, no en acumular titulares. Cada corrida
recurrente de `/trinidad` sobre tendencias de diseño debe:

1. **Confrontar el tablero de hipótesis (§6)** antes que buscar novedad. Una hipótesis que se
   confirma o se refuta vale más que una tendencia nueva: cambiar el estado de una fila de §6 es
   el entregable principal de cada iteración.
2. **Clasificar todo hallazgo nuevo en la escala de madurez de evidencia (§5)** — 🟢 documentado /
   🟡 plausible mal probado / 🔴 hype / ⚔️ evidencia en conflicto. Ninguna tendencia entra al node
   sin nivel asignado.
3. **Anotar la bitácora (§8)** con qué se buscó, qué cambió de estado y qué quedó pendiente, para
   que la siguiente iteración no repita el barrido.
4. **Destilar en §7 (criterio e intuición)** solo lo que sobrevivió a dos o más iteraciones. §7 es
   lo que se puede usar sin volver a consultar la evidencia; todo lo demás sigue siendo provisional.
5. **Descontar por estacionalidad y por incentivo del emisor** (ver §7, reglas C4 y C5) antes de
   leer cualquier pico de conversación como cambio estructural.
6. **Auditar hacia adentro, no solo hacia afuera** *(añadido en la iteración 3, ver C20)*. Antes de
   cerrar la corrida, tomar **el hallazgo más satisfactorio de la iteración anterior** —típicamente
   el que cerró una contradicción abierta— y rastrear su fuente primaria con el mismo rigor con que
   se desmontan las cifras ajenas. La iteración 3 encontró así que el "impuesto de verificación" que
   la iteración 2 celebró **no existe como evidencia rastreable**. Un node que solo audita hacia
   afuera acumula sus propios ecos de cita.

---

## 1. Resumen ejecutivo

- 🔬 **Empírica**: la afirmación "el diseño produce impacto de negocio tangible" es *probablemente
  cierta pero está mal probada*. La evidencia sólida existe (econometría de firmas, experimentación
  online) y dice algo mucho más modesto que la retórica de la industria: el efecto del diseño es
  **real, pequeño, acumulativo y mediado**. Las cifras estrella (McKinsey +32%/+56%, "$1 → $100")
  son correlacionales, no auditables y con conflicto de interés estructural.
- 📱 **Social**: el eje dominante del gremio es **IA × identidad profesional**, con dos subtramas
  🔥: la ansiedad laboral y el rechazo al "AI slop". Pero el volumen de la ansiedad **no está
  respaldado por la evidencia de causalidad**, y hay actores con incentivo económico directo en
  sostener el pánico — **en los dos bandos**: también quien la desmiente vive de la audiencia
  (iter. 3, H11). ⬆️ *Iter. 3*: el eje **se normaliza** — la conversación pasó de "¿nos va a
  reemplazar?" a "así se trabaja ahora" (Figma Config 2026), y el propio ciclo del "diseño ha
  muerto" empieza a generar su anticuerpo desde adentro.
- 📈 **Negocio**: hay que separar tres mercados que la conversación confunde. Las **herramientas**
  crecen fuerte con datos auditados (Figma +46% YoY) pero el mercado de capitales las castiga por
  riesgo de disrupción de IA (Figma cotiza bajo su precio de IPO). Las **consultoras de diseño**
  están en crisis estructural documentada (IDEO −67% de revenue, Veryday cerrada, R/GA vendida a
  PE, Song absorbida). El **ROI del diseño** es el eslabón más débil de los tres.
- ⚖️ **Convergencia central de las tres pistas**: *el diseño importa, pero no por las razones ni en
  la magnitud que la industria del diseño afirma.* Lo que resiste escrutinio es el **mecanismo**
  (reducir fricción, error, retrabajo y riesgo regulatorio), no el **multiplicador**. Y la ansiedad
  del gremio, medida contra los datos, es desproporcionada respecto de la evidencia causal
  disponible.
- ⚔️ **Divergencia que este node no resuelve**: la evidencia sobre si la IA acelera o frena el
  trabajo está en conflicto directo (METR: −19% de productividad con IA en devs expertos; estudio
  de design-system-aware AI: −46% a −69% de time-to-delivery). ⚠️ **La iteración 2 creyó haberla
  reconciliado y la iteración 3 revirtió esa conclusión**: el mecanismo del *impuesto de
  verificación* perdió su cifra ancla por falta de fuente primaria. **Vuelve a estar sin resolver.**
  Ver §11.2 y §6/H19.
- 🪞 **Regla de higiene que este node aprendió sobre sí mismo (iter. 3)**: el hallazgo con más
  riesgo de entrar sin verificar no es el espectacular — es **el que cierra una contradicción
  propia**. Ver C20 y H24.

---

## 2. 🔬 Pista empírica/teórica (seeker)

**Veredicto:** la evidencia realmente sólida del valor del diseño es más antigua, más modesta y
mucho menos citada que la evidencia que la industria promueve. La frontera de 2026 —generative UI,
agentic UX— es hoy propuesta sin respaldo independiente, y hay 20 años de literatura previa que
predice que fallará en aprendibilidad.

### 2.1 Lo documentado

- **Capacidad de diseño ↔ desempeño de firma: asociación real, medida con datos objetivos.** El
  estudio canónico (Hertenstein, Platt & Veryzer, 2005 — F-237, peer-reviewed, 93 firmas) encuentra
  mejor ROA/ROS/crecimiento en firmas con diseño industrial efectivo. ⚠️ La variable independiente
  es una *percepción experta*, contaminable por halo. La réplica moderna es mucho mejor: panel GLS
  sobre **1.659 firmas públicas estadounidenses, 1980-2015**, con capacidad de diseño
  operacionalizada objetivamente vía inventores presentes a la vez en patentes de diseño y de
  utilidad (F-238, 2025, peer-reviewed) — confirma efecto directo **y** efecto moderador que
  amplifica el retorno de la innovación. **Es la mejor evidencia disponible del vínculo
  diseño→negocio.** Sigue siendo observacional.
- **Design thinking: efecto real pero *mediado*, no directo.** El efecto sobre el desempeño del
  proyecto está **totalmente mediado por empoderamiento psicológico** (Roth et al., 2020 — F-239):
  el design thinking funciona en parte como práctica de motivación de equipo, no como método
  superior de resolución de problemas. La revisión posterior confirma que los mecanismos causales
  siguen sin establecerse (Mayer et al., 2025 — F-240).
- **La mayoría de los cambios de diseño no mejoran las métricas.** El dato más incómodo y mejor
  sostenido del reporte: en Microsoft solo **~1/3** de los experimentos bien diseñados logró mejorar
  su métrica objetivo; en Bing, Google Ads, Netflix y Airbnb las tasas de fracaso reportadas van del
  **85% al 90%** (Kohavi & Thomke, 2017 — F-262). Es evidencia causal (miles de A/B tests
  aleatorizados) y contradice de frente la narrativa de multiplicadores: el valor se **acumula en
  mejoras de 0,1-0,2%**, no llega en un rediseño transformador.
- **Dark patterns: efecto causal grande, medido experimentalmente.** Aceptación de un plan dudoso:
  **11,3% (control) → 25,8% con dark patterns leves → 41,9% con agresivos** (~4x) en experimento
  aleatorizado con muestra ponderada por censo, N=1.773 (Luguri & Strahilevitz, 2021 — F-241). Los
  agresivos generan backlash; los leves no. **La evidencia más fuerte del "poder del diseño" es
  sobre su capacidad de daño, no de valor** — un hecho que la industria del diseño rara vez cita.
  La susceptibilidad es transversal: los proxies clásicos de vulnerabilidad (ingreso, edad)
  explican poco (F-251).
- **Claridad > ornamento.** La correlación estética-usabilidad percibida **cae de r=0,79 a r=0,34
  al controlar por fluidez de procesamiento** (Preßler et al., 2023 — F-249): buena parte del
  "efecto estética" es en realidad *facilidad de procesamiento*, no belleza. El caso Liquid Glass
  de Apple lo valida en el mundo real (F-272): pérdida de contraste y jerarquía degradada, caída de
  calificaciones de accesibilidad, y corrección posterior por la propia Apple.
- **Accesibilidad dejó de ser argumento de ROI y pasó a ser obligación con sanción**: el European
  Accessibility Act es exigible desde el **28 de junio de 2025**, con primeras demandas en Francia
  en noviembre de 2025 (F-265).

### 2.2 Interfaces con IA: confianza, explicabilidad y adaptación

Es aquí donde el desfase entre discurso y evidencia es mayor, y donde hay hallazgos accionables
contraintuitivos:

- **Explicabilidad → confianza: correlación significativa pero *moderada*.** Meta-análisis PRISMA
  de **90 estudios** (Atf & Lewis, 2025 — F-242): los propios autores concluyen que la
  explicabilidad **no es el factor único ni predominante** de la confianza. Refuta la premisa
  implícita de casi todo el discurso de "capas de transparencia de IA" de los reportes de tendencias.
- **Explicaciones ≠ mejor decisión conjunta.** Las explicaciones **no** produjeron desempeño
  complementario humano-IA: subieron la precisión cuando la IA acertaba y la bajaron cuando erraba
  — firma diagnóstica de **sobre-confianza**, no de calibración (Bansal et al., 2021 — F-244). La
  teoría explicativa: las explicaciones solo sirven **en la medida en que permiten verificar** la
  corrección de la predicción, y en la mayoría de contextos no lo permiten (Fok & Weld, 2024 —
  F-243).
- **Pero la sobre-confianza es estratégica, no inevitable.** Las explicaciones **sí** reducen
  sobre-confianza y mejoran precisión **solo en tareas difíciles**; en tareas fáciles o medias no
  hay diferencia frente a mostrar solo la predicción (Vasconcelos et al., 2023 — 5 estudios, N=731 —
  F-246). Las *cognitive forcing functions* también reducen sobre-confianza, con costo en
  satisfacción y carga percibida (Buçinca et al., 2021 — F-245).
- **⭐ Síntesis accionable**: añadir "explicabilidad" genérica **no calibra la confianza**. Lo que
  la calibra es (a) hacer **verificable** la salida, (b) introducir **fricción deliberada donde la
  tarea es difícil**, (c) **no ponerla donde la tarea es fácil**.
- **La adaptación automática de interfaces ya fue probada y perdió, hace 20 años.** Menús
  **estáticos** significativamente más rápidos que los **adaptativos**; los **adaptables** (control
  del usuario) superaron a los adaptativos (control del sistema); y la alta precisión de adaptación
  **reduce la conciencia del usuario sobre el conjunto completo de funciones**, dañando la
  aprendibilidad (Findlater & McGrenere, 2004/2010 — F-247). La adaptación lenta ayuda; la rápida
  perjudica.
- **Este es el mayor punto ciego del discurso 2026**: "la interfaz se genera de nuevo para cada
  usuario en cada turno" es la versión extrema de la adaptación rápida controlada por el sistema
  que la literatura ya identificó como perjudicial.
- **Más personalización no es mejor**: bajo saliencia de privacidad, la personalización con datos
  personales **no supera al mensaje genérico** y es peor que la contextual moderada (F-253);
  evidencia de campo confirma que el consejo de IA personalizado puede reducir la compra por
  intrusividad percibida (F-254). Relevante directamente para seguros.

### 2.3 Design systems

- La cifra estrella (**"47% más rápido"**) viene de un estudio con **N=8 desarrolladores de la
  propia agencia que vende design systems**, sin cegamiento y **con efecto de orden no controlado**
  (todos hicieron primero la versión desde cero, así que el aprendizaje de la tarea infla el
  beneficio atribuido al design system) — Sparkbox, 2022 (F-269). Es generador de hipótesis, no
  evidencia de efecto.
- La evidencia más reciente y mejor diseñada es un **preprint sin revisión por pares**: experimento
  controlado en una gran empresa brasileña, **49 desarrolladores profesionales**, 3 stacks, 3
  condiciones; reporta −46,7% a −69,4% de time-to-delivery con IA alineada al design system, y
  **menor variabilidad de desempeño** (F-259). *El hallazgo de reducción de variabilidad es más
  creíble y más interesante que el de velocidad.*
- **Contrapeso**: la industria reporta lo contrario de lo que promociona — la satisfacción con el
  buy-in **cayó de 42% a 32% interanual** y Gartner ubica a los design systems deslizándose al
  valle de la desilusión (zeroheight, 2025 — F-270). **La promesa de eficiencia coexiste con una
  crisis documentada de adopción y mantenimiento.**

### 2.4 Registro teórico/crítico

No aporta evidencia empírica, pero cambia cómo se lee todo lo anterior:

- **Post-Norman: el propio Norman se auto-refuta parcialmente.** En *Design for a Better World*
  (2023 — F-274) argumenta que el human-centered design es **insuficiente y potencialmente dañino**:
  optimiza el problema inmediato de un individuo mientras ignora efectos sistémicos, y ha servido
  para **monetizar consumidores**. Tesis atribuible a Norman, no consenso.
- **Crítica ontológica/decolonial**: el diseño es constitutivamente *world-making* — no resuelve
  problemas dentro de un mundo dado, fabrica el mundo en el que los problemas aparecen (Escobar,
  2018 — F-275); y reproduce desigualdad estructural salvo que sea liderado por comunidades
  marginadas (Costanza-Chock, 2020 — F-276). ⚠️ **Se buscó específicamente fricción interna entre
  ambos marcos (2024-2026) y no se encontró** — se tratan como complementarios. Esa ausencia de
  contraste es un dato: es un campo teórico con poca fricción interna, lo que debilita su valor
  probatorio.
- **Diseño y capitalismo de plataforma**: el capitalismo depende materialmente del trabajo del
  diseño gráfico, y —el punto más filoso— **las estrategias anticonsumistas (social design,
  speculative design) son sistemáticamente reapropiadas para servir al crecimiento** (Pater, 2021 —
  F-277; Fry, 2020 — F-278).
- **Aplicación del marco a la propia literatura de "valor del diseño"**: la producción de evidencia
  sobre el valor del diseño es **ella misma un producto con función comercial**. No es un argumento
  *ad hominem*: es una hipótesis sobre por qué la industria produce estudios correlacionales con
  cifras grandes y no experimentos con cifras pequeñas. **Los experimentos con cifras pequeñas
  (Kohavi) los produce quien no vende diseño.**
- **Anti-patrones: único punto donde teoría y evidencia convergen.** La crítica teórica ("el diseño
  es instrumento de captura de atención y consentimiento") tiene respaldo experimental duro (F-241)
  y respaldo regulatorio (FTC, CMA, Comisión Europea).

### 2.5 Chequeo de eco de cita — seis cadenas que colapsan en una sola fuente (o en ninguna)

Esto es un hallazgo en sí mismo y debe sobrevivir a todas las iteraciones:

1. **"+32% de crecimiento / +56% de retorno al accionista"** — decenas de altavoces (Fast Company,
   Wallpaper*, AMA, blogs de agencia) → **todos citan McKinsey (2018)**, un único reporte sin
   significancia estadística publicada, sin referencias y sin análisis de sesgo de muestreo (F-266).
   Es **una** pieza de evidencia con ~30 megáfonos.
2. **"$1 invertido en UX devuelve $100"** — la cadena termina en un reporte de Forrester (2016)
   **tras un muro de pago de ~US$1.495**, que prácticamente ningún citante ha leído (F-268). Hay
   indicios fuertes de **conflación de tres claims distintos**, incluida la **curva de costo de
   cambio de Boehm** (corregir un error tarde cuesta ~100x) — que **no es un ROI de inversión en UX
   en absoluto**. El "100x de UX" es, con alta probabilidad, un error de transcripción de una regla
   de ingeniería de software.
3. **"47% más rápido con design system"** → Sparkbox (2022), N=8 (F-269). Una fuente, muchos
   megáfonos.
4. **"671% de ROI de design systems según Forrester"** → **no existe estudio primario rastreable**
   (F-327). Lo que sí existe es un Forrester TEI **comisionado y pagado por InVision** con 475% de
   ROI sobre una organización compuesta de 4 entrevistas (F-328). Registrado explícitamente como 🔴 E
   para que no vuelva a entrar al proyecto por otra vía.
5. **"135% de ROI de un design system"** *(detectada en la iteración 2)* — la cifra que reemplazó al
   671% en la circulación de 2026 **no es un resultado medido: es una calculadora**. Sale de un
   artículo de Smashing Magazine (2022 — F-397) que *modela* US$646.000 invertidos → US$1.517.400 de
   ahorro estimado a 5 años. Y los insumos del modelo son a su vez cifras autorreportadas por la
   industria (Klüver 2019, Ray 2018, Slack 2019). **Es un modelo alimentado con ecos.** Mismo defecto
   estructural que el +35,26% de Baymard (F-311): nadie ejecutó y midió.
   ⚠️ *Corregido en la iteración 3:* el patrón no es que la industria **cambie** de cifra — es que
   **no cambia nada**. El 135% no reemplazó al 671%: los dos siguen circulando, cada uno en su
   nicho, junto al McKinsey de 2018 y al "$1 → $100" de Forrester. Ver §11.5 y H22 reformulada.
6. **"4,3 min de verificación por sugerencia para seniors vs. 1,2 para juniors"** *(detectada en la
   iteración 3 — **y la primera cadena que estaba dentro de este node**)*. Es la cifra ancla del
   **impuesto de verificación** que la iteración 2 adoptó como el mecanismo que reconciliaba la
   divergencia ⚔️ de productividad con IA. Rastreo: la frase se repite casi palabra por palabra en
   Sonar, Faros AI, Augment Code, Entrepreneur y mariothomas.com, y el punto más profundo alcanzable
   es un artículo de **DZone** (F-404) que dice literalmente *"in a recent study of 250 developers
   across five organizations…"* **sin nombrar autor, institución ni enlazar el estudio**. No existe
   paper, preprint ni informe con ese N y esas cifras. El preprint que el node citaba como mecanismo
   (F-388) es de **autor único** y es **síntesis de cifras de terceros, no experimento propio**.
   ⭐ *La regla que sale de aquí (C20) es la más incómoda del node:* **el chequeo de eco de cita hay
   que aplicarlo también hacia adentro, y con más fuerza cuanto más satisfactorio sea el hallazgo.**
   La cifra entró sin resistencia porque *resolvía* una tensión que el node arrastraba desde la
   iteración 1 — exactamente la condición en que baja la guardia.

*Nota simétrica de honestidad: el dato de Kohavi también se repite mucho y proviene esencialmente de
una organización (Microsoft ExP), aunque las cifras análogas de Google/Bing/Netflix/Airbnb vienen de
reportes separados.*

---

## 3. 📱 Pista social/mediática (gossiper)

**Nivel general:** 🔥 muy alta y sostenida en el eje **IA × identidad profesional del diseñador**.
Casi todo lo demás (estética, herramientas, design systems) se discute como subtrama de ese eje.

*Tabla actualizada en la iteración 3 (2026-08-02); la columna de cambio registra el movimiento.*

| Tendencia | Instalación | Tono dominante | Δ iter. 3 |
|---|---|---|---|
| **IA normalizada como herramienta por defecto (Figma Config 2026)** | 🔥 | **Pragmático, no defensivo**: "así se trabaja ahora" | ⬆️ **eje nuevo** — F-412 |
| Ansiedad IA / empleo / "el fin del UX designer" | 🔥 | Ansioso, pero con **fatiga del propio ciclo**: varias piezas de 2026 ya lo llaman "el truco de engagement más viejo del mundo" | ↔️ caliente, con anticuerpo propio — F-415 |
| "AI slop" / *sameness* estética | 🔥 | Indignado; **reconfirmado como empuje de vendors** (Pinterest+Canva+Adobe decretan la fatiga de la estética que ellos venden) | ↔️ segunda camada — F-411 |
| Confusión del rol / "nadie sabe qué es un diseñador" | 🌡️ | Exasperado, muy validado por experiencia propia | ↔️ |
| Compresión del rol vía IA en mercados emergentes | 🌡️ | **Contencioso** — MercadoLibre **niega** la atribución a IA; se suma Livspace (India, ~1.000 despidos) | ⬇️ de conducta limpia a **caso disputado** — F-419, F-416 |
| Desacople discurso-mercado del propio vendor | 🌡️ | Cínico, incipiente | ⬆️ **nuevo** |
| Anti-design / neo-brutalismo / lo-fi | 🌡️ | Entusiasta, pero **empujado por vendors** | ↔️ |
| Design systems como gobernanza de IA | 🌡️ | Técnico, pragmático, poco dramático | ↔️ |
| Vibe coding para diseñadores | 🌡️ | Ambivalente: FOMO + escepticismo | ↔️ |
| Retorno táctil/analógico (riso, zines, print) | 💬 | Cálido, sin conflicto — **pero con conducta real** | ↔️ |
| Liquid Glass de Apple | 🧊 (fue 🌡️, fue 🔥) | Apagado; sin actividad nueva | ⬇️ ciclo cerrado |
| Service design | 🧊 | Prácticamente ausente | ↔️ (cerrado como `parcial` en iter. 2) |

### 3.1 La ansiedad gremial: no es "reemplazo", es pérdida de definición

El registro dominante **no** es "la IA reemplaza diseñadores" en abstracto. Es más específico y más
amargo: **el rol perdió definición y el mercado de entrada se cerró.**

- El dato ancla del gremio es un empate a tres bandas casi perfecto: **36% dice que el campo mejoró,
  35% que empeoró, 29% sin cambio** — y simultáneamente **89% dice trabajar más rápido** (Figma /
  NewtonX, n=906 — F-280). Esa combinación de *mejora instrumental + malestar existencial* es la
  firma emocional de 2026: **la gente no está peor en su día a día, está peor en su expectativa de
  futuro.** NN/g confirma la división, no el pánico: 47% ve "algún valor" en la IA, 20% no está
  impresionado (F-281).
- La queja mejor validada desde la experiencia personal es sobre **contratación, no reemplazo**: un
  aviso de "Product Designer" pide hoy estrategia, front-end, research y "mentalidad de builder" en
  una persona (F-301). Y hay una ironía perfecta documentada: hiring managers desbordados por
  **portafolios generados con IA que se ven todos iguales** — la IA no les quitó el trabajo a los
  diseñadores, **les rompió el mecanismo de selección**.
- El daño percibido se concentra en **junior**; senior y generalistas estratégicos se recuperan.
- **Estacionalidad, no tendencia**: el ciclo "el diseño ha muerto" es estructuralmente recurrente y
  repica con cada lanzamiento de modelo (el pico de 2026 lo detonó ChatGPT Images 2.0 el 21 de
  abril) — F-296, F-300. **Antes de leer un pico como cambio estructural, verificar contra el
  calendario de releases.**

### 3.2 Liquid Glass: el caso más limpio de backlash exitoso

Cadena rastreada: WWDC 2025 → iOS 26 (sept-2025) → burla masiva por legibilidad y contraste, con
post viral ancla en X (F-289) → Apple introduce control "Tinted" en iOS 26.1 (F-291) → iOS 27
(jun-2026) suma **slider de transparencia** (F-292).

⭐ **Hallazgo metodológico que vale para todas las iteraciones: la validación más fuerte de toda
esta investigación no es un comentario, es una conducta corporativa.** Apple envió un control de
transparencia. Eso valida el backlash con más peso que cualquier cantidad de likes.

Contramatiz que se pierde si uno solo cuenta volumen: **hubo backlash contra el backlash**. En X se
dijo que la versión atenuada "se ve mucho más barata"; en Reddit se aplaudió por accesibilidad. **Hay
dos públicos con intereses estéticamente opuestos y ambos se sienten traicionados por la solución de
compromiso.**

### 3.3 AI slop: rebelión genuina, captura corporativa

El vocabulario está totalmente instalado (degradados morados, sans gruesas, blobs, esquinas
redondeadas apiladas, sombras suaves en todo) — la comunidad desarrolló **taxonomía propia**, señal
fuerte de instalación. Cadena: manifiesto **Slopless** de un creador individual (F-286) → newsletters
de diseño (F-287) → **Landor le pone nombre corporativo: "Anti-AI Crafting"** (F-288). Ese salto de
capa es el indicador de instalación más significativo, más que cualquier conteo de menciones.

⚠️ **Dos alertas que deben conservarse:**
- **La cuenta clave tiene incentivo comercial y publica las dos narrativas opuestas** — firma
  "Designers will OWN 2026-2030" y a la vez lidera el movimiento contra el slop; vende cursos.
  Su incentivo está alineado con mantener al gremio en estado de urgencia, **en cualquier dirección**.
- **Las dos grandes narrativas estéticas "anti-IA" de 2026 están promovidas por empresas de
  herramientas de IA y por agencias globales de branding.** Canva vende generación con IA y a la vez
  decreta el año de la imperfección humana (F-295). **Es una tendencia industria-hacia-abajo
  disfrazada de rebelión comunitaria-hacia-arriba.**

### 3.4 Validación genuina vs. mera amplificación

- **Validación** (experiencia propia o conducta observable): Apple enviando el control de
  transparencia; usuarios del foro oficial de Figma criticando Figma Make con especificidad técnica
  (F-293); reviews que fijan el techo real de las herramientas ("Lovable te lleva como máximo al 70%,
  no es production-ready" — F-294); hiring managers reportando el problema de portafolios
  indistinguibles; **inscripciones pagadas** a talleres de riso/zines; adopción medible de design
  tokens (84%, desde 56%) y de shadcn/ui (>75.000 estrellas en GitHub) — F-298.
- **Mera amplificación**: "Designers are cooked" / "UX is dead" con lápidas generadas por IA en
  LinkedIn — volumen enorme, aporte informativo nulo, **cero testimonios de primera mano de despidos
  atribuibles a IA**. Y las listicles de "tendencias 2026" de Wix, Figma, Adobe, Envato: contenido
  de marketing de fabricantes de herramientas, no sentimiento de comunidad (F-279).
- **Churnalism detectado**: el reporte "Imperfect by Design" de Canva es **una sola pieza con al
  menos seis vitrinas** (Businesswire → financialcontent, MSN, campaignbrief, LBBOnline, lotiva…)
  con el mismo texto y las mismas cifras. **Cuenta como 1 pieza de cobertura, no 6.**
  ⚠️ *Advertencia operativa para futuras iteraciones: el término "design trends 2026" está capturado
  por diseño de interiores (1stDibs y similares) y contamina las búsquedas.*

### 3.5 Búsqueda adversarial: el backlash que sí apareció

1. **Contra "la IA se lleva los empleos de diseño" — el desmentido más fuerte.** Sí hay 87.714
   recortes *atribuidos* a IA en 5 meses de 2026 (F-283). Pero **Gallup encontró que 62% de los
   despedidos eran NO usuarios de IA, y solo 1% citó IA o automatización como razón principal**
   (F-282); el economista jefe de Glassdoor señala *scapegoating*: "una empresa puede decir que la
   IA es la razón, pero eso no significa que lo sea". Se reporta además que 55% de esos empleadores
   se arrepintió. **La atribución a IA es narrativa corporativa conveniente, no causalidad
   demostrada.**
2. **Contra el propio movimiento anti-slop.** Un análisis de **25 millones de comentarios** concluye
   que las acusaciones de "AI slop" funcionan crecientemente como **forma emergente de gatekeeping
   social** más que como identificación real de contenido IA — y ese aumento **no** forma parte de un
   alza general de hostilidad online (F-284). Es la contraevidencia más incómoda para el gremio:
   **parte de la indignación estética es defensa de estatus profesional.**
3. **Contra la estética anti-diseño.** Un estudio de usabilidad separó brutalismo disciplinado de
   anti-diseño caótico y encontró que la versión caótica llegó a tasas de éxito de tarea de
   **8-10%** en páginas con mucha información (F-297). **La tendencia que el gremio celebra como
   rebelión destruye la usabilidad cuando se aplica sin disciplina** — y esto circula en el registro
   técnico, casi no en el social.
4. **Contra las figuras de autoridad.** Jakob Nielsen provocó rechazo amplio, sostenido y en
   publicaciones independientes al declarar que la IA "invalidará completamente el proceso manual de
   diseño UX" (F-299).

### 3.6 Hallazgo negativo: el silencio del service design

Se buscó activamente conversación social sobre service design y **prácticamente no existe** (las
búsquedas se contaminan con layoffs de ServiceNow). Lo poco cuantificable: 459 contratos citando
"Service Design" en Inglaterra en 6 meses (1,45% del total) — F-302. **Lectura: silencio social no
equivale a decadencia, pero sí significa que el service design no está participando de la
conversación identitaria del gremio. No hay ansiedad porque no hay tribuna.**

---

## 4. 📈 Pista de negocio (marketer)

**Veredicto: hay tres mercados distintos que la conversación sobre "tendencias de diseño" confunde
en uno solo.** Confianza alta en (1) y (2) — filings SEC y transacciones confirmadas; baja-media en
(3).

### 4.1 Herramientas de diseño: crecen, pero el mercado descuenta obsolescencia

| Empresa | Métrica | Valor | Corte | Evidencia |
|---|---|---|---|---|
| **Figma** | Revenue Q1'26 | **$333,4M, +46% YoY** (acelerando desde +40%) | 31-mar-2026 | 8-K SEC (F-303) |
| Figma | Net Dollar Retention | **139%** (⚠️ definición no estándar) | 31-mar-2026 | 8-K SEC (F-303) |
| Figma | Revenue FY2025 | ~**$1,05B, +41%** | FY2025 | 8-K SEC (F-304) |
| Figma | Precio de la acción | ~**−49% YTD, ~−83/87% desde el pico, bajo el precio de IPO ($33)** | jul-2026 | Prensa (F-326) |
| **Adobe** | Revenue Q2 FY26 | **$6,62B, +13% YoY** (récord); suscripción 97% | may-2026 | 10-Q SEC (F-306) |
| Adobe | ARR total | **$27,10B, +12,5%** — incluye ~$480M **inorgánicos** (Semrush) | may-2026 | 10-Q SEC (F-306) |
| **Canva** | ARR | ~**$4B**; valuación $42B (secundario); **IPO postergada a 2027** | 2025-26 | Auto-reportado (F-323, F-324) |
| **Lovable** | ARR | ~**$400-500M**; ronda **en conversaciones** a $12-13,2B (no cerrada) | 2026 | Auto-reportado (F-320, F-321) |

⚠️ **El desacople es el hallazgo, no el crecimiento.** Figma crece *acelerando* y su acción cotiza
**bajo el precio de IPO**. Causas concurrentes documentadas: vencimiento del lock-up (27-ene-2026),
lanzamiento de **Claude Design de Anthropic el 17-abr-2026** con caída inmediata de 6-7,7% (F-318), y
recortes en cadena de precio objetivo. **El mercado no está descontando desempeño: está descontando
obsolescencia por IA.** El propio S-1 de Figma declara ese riesgo (F-305).

⚠️ **Degradación del reporting bajo presión**: Adobe **fusionó Digital Media, Digital Experience y
Publishing en un solo segmento reportable** desde Q1 FY2026 — la pregunta "cómo va Digital Media" ya
no es respondible con datos públicos. Webflow **dejó de publicar ARR** (último dato duro: $200M de
2023) e hizo layoffs en mayo 2026 (F-322).

### 4.2 Consultoras de diseño: crisis estructural documentada

Cuatro señales convergentes, no anecdóticas:

- **IDEO**: revenue cayó a **<$100M desde ~$300M cuatro años antes** (~−67%), tras recortar 32% de
  la plantilla en 2023 (F-316, F-317). El propio CEO dice que la centralidad en el cliente "ya es
  *table stakes*". ⚠️ Discrepancia abierta: ZoomInfo estima $238,4M — se privilegia Fortune
  (reportería con cifra atribuida) sobre un estimador algorítmico sin metodología.
- **Veryday**: McKinsey **cerró** el estudio que había adquirido en 2016.
- **R/GA**: IPG la **vendió a private equity** con **términos no revelados** — señal en sí misma
  (F-307).
- **Accenture Song**: reestructurada y luego **absorbida** dentro de otra línea de negocio (F-325).

**No se encontró ninguna consultora de diseño con evidencia publicada de crecimiento en 2025-2026.
Esa ausencia, tras buscarla, es evidencia.**

### 4.3 ROI del diseño: el eslabón más débil

| Cifra | Metodología real | Veredicto |
|---|---|---|
| McKinsey +32 pp / +56 pp (F-266) | 300 empresas, correlacional, **sin significancia publicada, sin citas, sin análisis de sesgo de muestreo**; 8 años sin replicar | 🔴 No usar como afirmación fuerza |
| "671% ROI de Forrester" (F-327) | **No existe estudio primario rastreable** | 🔴 Eco de cita puro |
| DMI Design Value Index +211% (F-267) | Selección **retrospectiva** de empresas ya reconocidas como design-centric | 🔴 Look-ahead bias + sesgo de supervivencia |
| Sparkbox −47% (F-269) | N=8, misma agencia, efecto de orden no controlado | 🟡 Honesta pero no generalizable |
| Baymard +35,26% de conversión (F-311) | **Potencial modelado, no lift medido** — nadie ejecutó las 32 mejoras y midió | 🟡 Se cita como si fuera resultado observado |

⭐ **No se encontró ni un solo caso donde una empresa pública atribuya un lift de conversión a un
rediseño en un documento auditado (10-K/10-Q). Esa ausencia es en sí un hallazgo.**

### 4.4 Mercado laboral: la divergencia emisor-vs-oficial

- **BLS** (organismo oficial): diseñadores gráficos **+2% 2024-2034** (más lento que el promedio),
  con mención explícita de que las herramientas de IA pueden reducir la contratación de freelancers
  (F-308). En contraste, web developers y digital designers **+7%** (F-309). **El estancamiento no
  es del "diseño": es del diseño gráfico.**
- **UXPA 2024**: 35% de organizaciones **redujeron** staff de UX — mismo porcentaje que las que lo
  aumentaron (F-313). ⚠️ **No hay edición 2025 ni 2026**: el mejor dato laboral del gremio tiene
  ~2 años. El benchmark de tamaño de equipo de NN/g (ratio 1:5:50) tiene **6 años y es pre-IA
  generativa** (F-312).
- **Las encuestas optimistas las publican empresas que le venden a ese mismo público**: Figma (82%
  de hiring managers dice que la necesidad se mantuvo o aumentó) y Adobe (46% percibe más
  oportunidades) — F-280, F-314. **Conflicto de interés del emisor, declarado.**

---

## 5. ⚖️ Síntesis: escala de madurez de evidencia

Esta tabla es el **entregable operativo** del node. Cada iteración la actualiza.

| Tendencia | Estado | Base |
|---|---|---|
| **Dark patterns mueven conducta económica** | 🟢 Documentado (causal) | F-241, F-251 |
| **Accesibilidad como obligación legal (UE)** | 🟢 Documentado (normativo) | F-265 |
| **Capacidad de diseño ↔ desempeño de firma** | 🟢 Documentado (asociación, no causalidad) | F-237, F-238 |
| **Claridad/fluidez > ornamento** | 🟢 Documentado | F-249, F-272 |
| **La mayoría de rediseños no mueve la métrica** | 🟢 Documentado (causal, A/B a escala) | F-262 |
| **Crisis del modelo consultora de diseño** | 🟢 Documentado (4 señales convergentes) | F-307, F-316, F-317, F-325 |
| **Explicabilidad de IA aumenta confianza** | 🟡 Parcial — sobrevendido (efecto moderado) | F-242 |
| **Design systems aceleran el desarrollo** | 🟡 Plausible, mal probado | F-259, F-269, F-270 |
| **Explicaciones mejoran la decisión humano-IA** | 🔴 Contradicho en su forma general | F-243, F-244, F-246 |
| **ROI del diseño 100:1 / MDI +32%/+56% / 671% / 135%** | 🔴 Hype (eco de cita — 5 cadenas) | F-266, F-268, F-327, **F-397** |
| **Generative UI: *gusta más* que el texto plano** | 🟢 Documentado (preferencia declarada, sesión única) ⬆️ *iter. 2* | **F-380, F-381** |
| **Generative UI: *funciona mejor*** | 🔴 Contradicho en los atributos de soporte ⬆️ *iter. 2* | **F-382, F-384** + F-247 |
| **Generative UI / interfaces generadas por LLM (como paradigma)** | 🔴 Propuesta sin respaldo independiente | F-247, F-256, F-258, F-260, **F-383, F-385, F-386** |
| **Service design tiene base de evidencia institucional** | 🟡 Existe pero es pre-IA y sin outcomes de largo plazo ⬆️ *iter. 2* | **F-387, F-395** |
| **El ciclo identitario del gremio llega desfasado a LatAm** | 🔴 Refutado (llega simultáneo, con conducta corporativa local) ⬆️ *iter. 2* | **F-389, F-391, F-392** |
| **Agentic UX** | 🔴 Hype declarado por sus propios autores | F-261 |
| **Spatial computing como tendencia de diseño** | 🔴 Hype (~5% de diseñadores construye para ello) | F-279 |
| **Personalización con IA a escala** | 🔴 Contradicho / condicional (efecto backfire) | F-253, F-254 |
| **La IA acelera el trabajo de diseño/producto** | ⚔️ **Evidencia en conflicto directo** — ⬆️ *iter. 3: la reconciliación de la iter. 2 se cae, vuelve a estar sin resolver* | F-257 vs. F-259 (ahora peer-reviewed, SBES 2026) |
| **El *impuesto de verificación* explica esa divergencia** | 🟡 **Degradado** *(iter. 3)* — el fenómeno cualitativo tiene respaldo (F-406), la **cifra ancla no tiene fuente primaria** (F-404) y la relación con la seniority no es monótona (F-407) | ~~F-388~~ → F-404, F-406, F-407 |
| **La IA está causando el desempleo de diseñadores** | ⚔️ Atribución declarada ≠ causalidad — ⬆️ *iter. 3: ahora también en español (MercadoLibre niega la atribución)* | F-282 vs. F-283, **F-419** |
| **Mejora percibida > mejora objetiva al usar IA** | 🟢 Documentado (causal, peer-reviewed) **pero de magnitud modesta** ⬆️ *iter. 3* — la brecha existe (~4 pts de auto-estimación sobre ~3 pts de mejora real) y **no llega a los ≥20 pp** que el node predecía | **F-401**, F-402 |
| **Rediseño expresivo mejora fluidez Y estética a la vez** | 🟢 Documentado (experimental, CHI 2026) ⬆️ *iter. 3* — complica la dicotomía "claridad *contra* ornamento" | **F-403** |
| **El corpus hispanohablante de tendencias cita evidencia local** | 🔴 **Refutado** *(iter. 3)* — 13/13 cifras atribuidas son de emisores anglosajones interesados; 15/20 piezas no citan **ninguna** fuente | **F-408 a F-411**, F-418 |
| **"Gartner dice que el 60% de las tareas de diseño…"** | 🔴 Hype — **autoridad prestada**: no existe reporte de Gartner con esas cifras | **F-408 vs. F-418** |

### Convergencias entre las tres pistas

1. **La retórica de la industria del diseño no resiste a sus propias fuentes.** La pista empírica
   desarma el ROI por metodología; la de negocio lo desarma por trazabilidad (no hay estudio
   primario); la social muestra que el discurso lo sostienen actores con incentivo comercial. **Tres
   caminos independientes, misma conclusión.**
2. **El valor defendible del diseño es el mecanismo, no el multiplicador.** Reducir fricción, error,
   retrabajo y riesgo regulatorio — todo ello medible y auditable — resiste; los multiplicadores no.
3. **La IA cambió el trabajo del diseño antes que su evidencia.** Las tres pistas coinciden en que
   la adopción va muy por delante de la validación: el gremio ya trabaja con IA (89% dice ser más
   rápido), el mercado ya la valoriza (o la castiga), y la literatura todavía no puede decir si
   funciona.

### Divergencias que este node NO resuelve

- **⚔️ Productividad con IA**: METR (RCT, devs expertos, **−19% de velocidad real** mientras estimaban
  ser 20% más rápidos) vs. preprint DS-aware AI (**−46% a −69% de time-to-delivery**). Explicación
  plausible de la diferencia: METR midió tareas en repos maduros que los devs conocían a fondo; el
  otro midió construcción de componentes nuevos con un design system.
  ⬆️ **Iteración 2 — la divergencia deja de ser un misterio y pasa a ser una variable moderadora.**
  La hipótesis que la iteración 1 formuló a mano ahora tiene nombre y cifras: el **impuesto de
  verificación** (*verification tax*) — ~4,3 min por sugerencia para seniors vs. ~1,2 min para
  juniors, que **escala con la madurez del código base y puede exceder el ahorro de generación**
  (F-388). Los dos estudios no se contradicen: **miden puntos opuestos de la misma curva.** ⚠️ El
  mecanismo viene de un preprint sin revisión por pares — es la mejor explicación disponible, no un
  hecho establecido. **Reclasificada de "sin resolver" a "reconciliada por mecanismo, pendiente de
  confirmación independiente"** (ver H19).
- **⚔️ Percepción gremial vs. dato oficial**: Figma/Adobe (encuestas de emisor interesado) reportan
  demanda estable o creciente; BLS proyecta +2% a diez años para diseño gráfico.
- **⚔️ Estética anti-IA**: alta validación social, evidencia de usabilidad negativa (8-10% de éxito
  de tarea en anti-diseño caótico), y promoción por parte de los propios vendors de IA.

---

## 6. 🧪 Tablero de hipótesis vivas

**Este es el corazón iterativo del node.** Cada corrida debe intentar mover al menos una fila.
Estados: `abierta` · `respaldada` · `refutada` · `parcial`.

| # | Hipótesis | Estado | Cómo se falsa |
|---|---|---|---|
| **H1** | Un índice de empresas "design-centric" definido **ex ante** tendrá exceso de retorno sobre el S&P **indistinguible de cero** (el +211% del DVI es look-ahead bias + supervivencia) | `abierta` — predicción del node: el exceso se reduce >70% | Replicación prospectiva del DVI con criterios congelados en t₀ |
| **H2** | El reporte de Forrester (2016) **no contiene** la afirmación "$1 → $100" en la forma en que circula | `abierta` | Compra y lectura del reporte (~US$1.495) |
| **H3** | En tarea repetida a lo largo de ≥5 sesiones, la **generative UI** dará **peor** tiempo de tarea y **peor** aprendibilidad que una UI estática equivalente, aunque gane en preferencia declarada en la sesión 1 | ⬆️ **`parcial`** *(iter. 2)* — **la mitad de la predicción está confirmada y la otra mitad sigue sin medirse.** Confirmado: gana en preferencia de sesión única (hasta 72%, F-381; F-380). Confirmado indirectamente: falla justo en prevención de errores, eficiencia de uso, recuperación y ayuda (F-382), y **produce interfaces distintas ante el mismo prompt incluso en ejecuciones repetidas de la misma herramienta** (F-384) — la inconsistencia que destruiría la aprendibilidad ya está medida. Sigue abierto: **nadie ha corrido el estudio longitudinal** | Estudio longitudinal independiente entre-sujetos. ⚠️ **Tras 3 iteraciones sigue sin existir.** Lo más cercano hallado en la iter. 3 no califica: F-399 compara condiciones en horizonte corto, F-400 (DIS 2025, N=37) es formativo/cualitativo. Tres barridos independientes con términos distintos y cero resultados **ya no es azar de búsqueda: es una propiedad del campo** (C7) |
| **H4** | Añadir explicación ("¿por qué veo esto?") **no** mejora precisión ni calibración en decisiones de **baja** dificultad; **sí** en alta | `parcial` — respaldada por F-246 en laboratorio, sin replicar en dominio aplicado | RCT con dificultad manipulada en recomendación de producto financiero/seguros |
| **H5** | En cualquier estudio que mida **a la vez** desempeño objetivo y percibido, la mejora subjetiva **excederá** a la objetiva en ≥20 pp | ⬆️ **`parcial`** *(iter. 3)* — **apareció por fin el estudio del tipo exacto que pedía, y la dirección se confirma pero la magnitud no.** F-401 (*Computers in Human Behavior*, peer-reviewed, Study 1 + réplica, N=452): desempeño objetivo +3 pts, auto-estimación +4 pts → brecha real de ~1 pt, **muy por debajo del umbral de ≥20 pp**. F-402 replica el diseño (objetivo+percibido+EEG) en código. **La hipótesis acierta en el signo y falla en la escala** — y eso le quita buena parte de su valor destructivo | Meta-análisis de estudios que reporten ambas medidas. ⚠️ **Reformular el umbral**: ≥20 pp era una apuesta, no una predicción fundada; el dato dice que la brecha honesta es de un solo dígito |
| **H6** | El efecto de un design system sobre el tiempo de desarrollo será **<20%** (no 47%, no 69%) con contrabalanceo de orden, N≥40 y devs externos a la organización que mantiene el sistema | `abierta` — **tres iteraciones buscando replicación independiente, cero resultados.** Novedad de la iter. 3: F-259 **dejó de ser preprint** (aceptado en SBES 2026, venue arbitrado) — sube el rigor del estudio pero **no su generalizabilidad**: misma muestra, misma empresa. ⭐ *El campo institucionaliza el mismo estudio en vez de replicarlo* — y sigue publicando calculadoras (F-425 usa el 135% de 2022 como cifra vigente en 2026) | Replicación independiente de Sparkbox con diseño corregido |
| **H7** | En un A/B real, las variantes que aumentan **fluidez** (contraste, jerarquía, menos elementos) superarán a las que aumentan atractivo estético sin aumentar fluidez | `abierta` — **y la iter. 3 sugiere que está mal planteada.** F-403 (CHI 2026, N=48, Material 3 vs. Material 3 Expressive) encuentra fijación 33% más rápida, tarea 20% más rápida **y** mejores calificaciones: fluidez y estética **subieron juntas**. En sistemas maduros no suelen ser un trade-off. **Reformulación propuesta para la iter. 4: no "¿cuál gana?" sino "¿en qué condiciones se sacrifica una por la otra?"** (el caso conocido sigue siendo Liquid Glass, F-272) | Experimento de campo que manipule las dos variables de forma independiente |
| **H8** | En Perú, donde la causa #1 de desconfianza en seguros es la falta de información, la exposición a patterns de *hidden information* predecirá desconfianza en aseguradoras **con más fuerza que las variables demográficas** | `abierta` — **el puente más directo con el resto del proyecto** | Experimento sobre muestra peruana replicando Luguri & Strahilevitz |
| **H9** | **Brecha actitud-conducta en diseñadores**: el discurso público es anti-IA/anti-slop pero la adopción declarada es altísima (89% trabaja más rápido) | `abierta` — **estructuralmente el mismo fenómeno que `disposicion_compartir_datos_pricing` en `lapuerta`** | Medir si la indignación estética predice o no comportamiento de uso |
| **H10** | La ansiedad gremial es un fenómeno de **seniority**, no de gremio: el daño está concentrado en juniors pero se enuncia en nombre de "los diseñadores" | ⬆️ **`parcial`** *(iter. 3)* — **primera evidencia segmentada en tres iteraciones**, cualitativa pero en plataforma con identidad corporativa verificada (Blind, F-414): seniors describen el mercado como *"pésimo si eres junior o recién graduado; si eres senior o superior, no es ideal pero está cerca de lo normal"*. Consistente con F-280/F-301, ahora con testimonio por nivel en vez de encuesta agregada | Encuesta segmentada por años de experiencia **con N reportado** — sigue sin existir |
| **H11** | **El doom tiene modelo de negocio**: la proporción de amplificadores del discurso "la IA mata al diseño" con incentivo comercial directo (cursos, bootcamps, portafolios) es alta; si lo es, el volumen social debe descontarse fuertemente | ⬆️ **`parcial`** *(iter. 3)* — auditoría de n≈8 piezas: **~60-70% tiene incentivo comercial identificable** en el formato o el publisher (bootcamp, Substack de pago, YouTube monetizado, agencia de contenido) — proporción aproximada, muestra de conveniencia, declarada como tal. ⭐ **Ampliación que no estaba en la hipótesis: el discurso que *corrige* el pánico también tiene modelo de negocio.** Varias piezas que dicen "dejen de decir que el diseño murió" son newsletters o bootcamps que necesitan tráfico (F-415). **El descuento por incentivo aplica a los dos bandos, no solo al alarmista** | Censo (no muestra) de los principales amplificadores con clasificación de su modelo de ingresos |
| **H12** | El backlash estético es **señalización de estatus profesional**, no preferencia de usuario | `parcial` — respaldada por F-284 (gatekeeping) y F-297 (usabilidad) | Testear si la "autenticidad imperfecta" mejora alguna métrica de usuario |
| **H13** | **Desacople valuación/desempeño**: si Figma reporta ≥40% de crecimiento en Q2 2026 y la acción **no** recupera sobre $33, el mercado descuenta disrupción por IA, no ejecución | `abierta` — **se resuelve el 5-ago-2026, tres días después de esta corrida.** Estado al corte: FIG cerró en **US$24,30 el 31-jul**, precio objetivo promedio **cayó de ~$40 (mar) a $31-33 (fin de jul)** ⚠️ con dispersión real entre compiladores, y **apareció la primera recomendación de venta** entre 16 casas (antes 0) — F-421. **Guidance oficial de Q2: $348-350M, ~40% YoY** (F-420), lo que deja la condición de falsación perfectamente limpia | Reporte Q2 2026 de Figma (5-ago) + evolución del precio a 90 días. **Es la única hipótesis del tablero con fecha de vencimiento** |
| **H14** | **El ARR de vibe coding no retiene**: si Lovable cierra a $12-13,2B, su ARR a 12 meses crecerá <50% (vs. 150%+ histórico), revelando la cohorte de churn | `abierta` — **la ronda sigue sin cerrar** al 2-ago-2026 (F-426). ARR autorreportado ~$400M (feb) → ~$500M (jun) con 146 empleados. ⭐ **Lo más informativo es una conducta, no una cifra: preguntada de forma directa, Lovable se negó a compartir su churn y su split mensual/anual** (F-427). Barclays estima tráfico **−40% desde el pico** y valuación implícita de **$1,8B** — 3x a 7x por debajo de la narrativa de ronda | Comparar ARR jul-2026 vs. jul-2027; se resuelve de inmediato si publican NRR con desglose de cohortes |
| **H15** | **La consultora de diseño pura no vuelve**: ninguna de las cuatro publicará crecimiento de dos dígitos en 2026-2027; la recuperación, si ocurre, será como implementadoras de IA | ⬆️ **`parcial`** *(iter. 3)* — **primer contraejemplo en tres iteraciones: R/GA reporta +30% H2'25 vs. H1'25 y +25% YoY en Q1 2026** (F-422). ⚠️ Tres descuentos: es **autorreportado** (privada, sin filing), R/GA **nunca fue consultora de diseño puro** (es agencia digital/publicitaria), y la propia nota enmarca el giro como **pivote a IA y consolidación** — es decir, **cae dentro de la cláusula de escape que la hipótesis ya preveía**. La predicción central sigue sin refutarse: IDEO sin cifra auditada, Veryday cerrada, y **Accenture no reporta Song como segmento** (F-428), lo que vuelve la pregunta estructuralmente no respondible | Reporte de revenue **auditado** de una consultora de diseño pura, o adquisición a múltiplo alto |
| **H16** | **El estándar de reporting se degrada donde hay presión de IA**: si Figma deja de reportar NDR o paid customers en algún trimestre 2026-2027, se refuerza | `parcial` — ya ocurrió con Adobe (fusión de segmentos), Webflow (dejó de publicar ARR, y suma **un segundo layoff del ~20% en may-2026**) y ahora **Accenture, que no reporta Song como segmento SEC** (F-428). ⚠️ **En Figma todavía no**: el Q1'26 reportó NDR (139%) y todos los tramos de paid customers. El reporte del 5-ago es la próxima prueba | Trimestre a trimestre |
| **H17** | **Desfase geográfico**: el ciclo identitario del gremio llega a Perú/LatAm desfasado, atenuado, o el mercado local ni siquiera participa de esa conversación | ⬇️ **`refutada`** *(iter. 2)* — **no hay desfase.** Brasil adopta IA **por encima** del mundo anglosajón (94% vs. 89%, N=823 — F-389); MercadoLibre ejecutó la compresión del rol en LatAm con **119 desvinculaciones de UX** integrando diseño y contenido (F-391); el vocabulario anti-slop circula en español en medios masivos (F-390). El ciclo es **simultáneo**, no diferido | Refutada. Ver H20, que es lo que quedó vivo del barrido |
| **H18** | **El silencio del service design** es señal de madurez (absorbido en operaciones), no de irrelevancia | ⬆️ **`parcial`** *(iter. 2)* — **la mitad favorable**: existe base de evidencia institucional (revisión oficial del gobierno británico, F-387), infraestructura viva (SDN, conferencia global, Touchpoint — F-395) y **comunidad activa en Perú desde 2017** (F-394). **La mitad adversa**: una figura interna de la disciplina describe una "**crisis de la práctica**" por no haber sabido demostrar valor (F-393), y **no hay métricas públicas de membresía** para medirlo. *Silencio social ≠ irrelevancia — pero tampoco es prueba de madurez* | Métricas de membresía SDN, o presupuesto/plantilla de service design en organizaciones grandes |

### Hipótesis abiertas en la iteración 2

| # | Hipótesis | Estado | Cómo se falsa |
|---|---|---|---|
| **H19** | **El impuesto de verificación es la variable moderadora**: el efecto de la IA sobre la velocidad de entrega será **negativo en código base maduro y positivo en construcción nueva**, y el punto de cruce dependerá de la seniority, no de la calidad del modelo | ⬇️ **`abierta` con alerta** *(iter. 3 — degradada desde "reconciliada por mecanismo")*. **Su cifra ancla no existe como evidencia rastreable**: 4,3/1,2 min muere en un blog sin arbitraje que cita "un estudio reciente" sin nombrarlo (F-404, sexta cadena de eco), y F-388 resultó ser **síntesis de autor único, no experimento**. Lo que **sí** queda en pie: el fenómeno cualitativo de desplazamiento de esfuerzo hacia verificación, con telemetría independiente (F-406: +98% de PRs, **+91% de tiempo de revisión**). Lo que **se rompe**: la relación monótona con la seniority (F-407, N=400 revisores / 11.429 revisiones: la aprobación **sube +14,5 pp** con la exposición acumulada — más experiencia → *menos* escrutinio). ⚠️ **No confundir con F-405**, un paper teórico homónimo sin relación | Un experimento que manipule **madurez del código base** como factor y mida seniority como moderador. **Tras 3 iteraciones no existe ninguno**: todo lo disponible es yuxtaposición narrativa post-hoc de estudios distintos |
| **H20** | **La conducta es local, el discurso es importado**: LatAm/España **generan evidencia y decisiones propias** pero **consumen el marco interpretativo traducido del inglés** — se re-emite el 89% de Figma sin el descuento por interés del emisor que la propia fuente exige. Predicción: **>70%** de las cifras citadas en piezas hispanohablantes de tendencias 2026 serán de emisores anglosajones con interés comercial | ⬆️ **`respaldada`** *(iter. 3)* — **auditoría sistemática: 13/13 cifras atribuidas (100%) provienen de emisores anglosajones con interés comercial directo** (Gartner, Forrester, Baymard, Google, Designer Fund, Adobe, Canva, Pinterest). **Cero** de las ~20 piezas citó un estudio con muestra propia en español o portugués. La predicción de >70% quedó corta. ⚠️ Muestra de conveniencia (N≈20), válida para el corpus auditado, no generalizable sin sesgo de indexación | Repetir la auditoría con muestreo sistemático y N mayor. Se refutaría si una réplica encuentra <70% |
| **H21** | **Brecha de gobernanza, no de adopción**: en mercados emergentes el problema real no es que los diseñadores no usen IA sino que la usan **sin marco corporativo** — 60% en cuentas personales, 14% con capacitación de la empresa (F-389). Si es así, la intervención de mayor retorno es **gobernanza, no capacitación en herramientas** | `abierta` — **tercera iteración consecutiva en blanco para el dato peruano.** Lo más cercano hallado: EY (70% de grandes empresas peruanas subirá presupuesto de IA, n=250 directivos) mide adopción organizacional, no *shadow AI*; España aporta brecha de confianza 68% empleados vs. 92% ejecutivos, pero en fuerza laboral general (F-417). ⭐ **La ausencia tras tres barridos con términos distintos ya es el hallazgo**: no se puede distinguir "el estudio no existe" de "existe tras un muro que el proxy no cruza" | **Dejar de barrer genéricamente.** Requiere fuente primaria: contacto con una asociación de diseño peruana, o que el propio proyecto corra la encuesta interna en Rimac |
| **H22** | **El ROI del diseño se cita por rotación, no por evidencia**: cuando una cifra estrella se desmonta públicamente, la industria **la sustituye por otra** en vez de dejar de citar cifras (671% → 135%) | 🔄 **Reformulada** *(iter. 3)* — **la predicción literal no se cumplió, y lo que se encontró es peor.** No apareció una cifra nueva: **las cinco ya desmontadas siguen todas vivas y circulando en paralelo**, cada una en su nicho — "$1→$100" descrito en 2026 como "el benchmark estándar" (F-423), McKinsey 2018 (y en un caso **mal fechado como "McKinsey 2026"**), DVI con sus dos cifras históricas conflacionadas (228% y 211%, sin edición nueva desde 2016), y el 135% de la calculadora de 2022 vendido como método vigente (F-425). **Ningún divulgador retiró ninguna cifra tras ser cuestionada.** ⚠️ La rotación 671%→135% fue un evento de *años*: cuatro días entre corridas no dan margen para observarla | **Reformulación para la iter. 4:** el enunciado correcto no es "la industria rota la cifra" sino "**la industria no corrige: acumula**". Se falsa comparando **semestre a semestre** (no corrida a corrida) si alguna cifra desmontada pierde circulación medible |

### Hipótesis abiertas en la iteración 3

| # | Hipótesis | Estado | Cómo se falsa |
|---|---|---|---|
| **H23** | **Autoridad prestada**: en el contenido de tendencias de diseño, una fracción no trivial de las cifras atribuidas a una autoridad nombrada (Gartner, Forrester, NN/g) **no existe en ningún reporte rastreable de ese emisor**. No es sesgo del emisor: es atribución fabricada o mal transcrita | `abierta` — caso testigo fuerte: tres cifras ("60% de tareas de diseño con IA", "80%", "68%") atribuidas a Gartner en una misma pieza (F-408); la búsqueda del reporte primario **no encontró ninguno** (F-418). Sí existen predicciones reales de Gartner con "60%", pero sobre temas distintos. ⭐ **Es un fallo de un orden peor que C4**: contra el emisor interesado sirve descontar; contra el emisor que nunca lo dijo, descontar no alcanza — hay que verificar que la afirmación exista | Tomar N cifras atribuidas a autoridades nombradas e intentar rastrear cada una hasta el reporte primario. Se refuta si la tasa de no-rastreables es marginal |
| **H24** | **El hallazgo satisfactorio no se audita**: los errores de este node se concentrarán en los hallazgos que **resuelven** una tensión que el node ya arrastraba, no en los que la contradicen. Un mecanismo que reconcilia una divergencia entra con menos escrutinio que una cifra que la agrava | `abierta` — **fundada en el propio error de la iteración 2**: el impuesto de verificación se adoptó sin rastrear su fuente primaria precisamente porque *cerraba* la divergencia ⚔️ abierta desde la iteración 1. Ninguna de las cifras que el node desmontó de otros (671%, 135%, McKinsey) tuvo ese trato. Predicción para la iter. 4: **si algo se cae, será otro hallazgo reconciliador, no una refutación** | Revisar, en cada iteración, si los hallazgos que se cayeron eran mayoritariamente reconciliadores. Se refuta si los errores se distribuyen por igual entre hallazgos que confirman y que contradicen |
| **H25** | **El corpus hispanohablante de tendencias no cita nada**: más del 70% de las piezas en español/portugués sobre tendencias de diseño **no cita ninguna fuente verificable** — ni local ni anglosajona. El problema no es solo importar el marco: es la ausencia total de aparato de evidencia | `abierta` — observado **15/20 (75%)** en la auditoría de la iter. 3: la mayoría afirma tendencias ("el minimalismo sigue ganando fuerza", "la tipografía audaz rompe normas") **sin ninguna cita**. Es distinto en naturaleza de H20 (que describe *qué* se cita cuando se cita) y probablemente más determinante del nivel de la conversación regional | Muestreo sistemático con N mayor. Se refuta si una réplica encuentra que la mayoría de las piezas sí ancla sus afirmaciones |
| **H26** | **El escrutinio decae con la exposición, no crece con la seniority**: frente a salidas de IA, lo que predice el nivel de verificación no es la antigüedad del profesional sino **cuántas salidas de IA ya revisó** — y la relación es negativa (habituación), no positiva | `abierta` — respaldo inicial en F-407 (400 revisores, 11.429 revisiones: aprobación **+14,5 pp** a través de deciles de exposición). Está en tensión con la narrativa lineal "los seniors verifican más" que sostenía H19. ⭐ **Si se sostiene, invierte el diseño de cualquier control de calidad sobre trabajo asistido por IA**: el riesgo no está en el novato que no sabe revisar, sino en el veterano que ya se acostumbró | Medir tasa de detección de error contra exposición acumulada, controlando por seniority. Se refuta si la seniority predice mejor que la exposición |

---

## 7. 🧭 Criterio e intuición acumulada

Reglas de decisión destiladas de la evidencia. **Se usan sin volver a consultar las fuentes.**
Una regla solo asciende aquí cuando sobrevivió al menos a una búsqueda adversarial explícita.

**Sobre cómo argumentar el valor del diseño**

- **C1 — Argumentar por mecanismo, nunca por multiplicador.** "Este cambio reduce N pasos, M errores
  y X horas de retrabajo" resiste a un CFO. "El diseño devuelve 100x" no sobrevive a la primera
  pregunta por la metodología. Cualquier deck que use McKinsey +32%/+56%, el "$1 → $100" o el "671%"
  como afirmación fuerza está construido sobre arena y **es vulnerable en la sala**.
- **C2 — Prometer acumulación, no transformación.** La distribución real de efectos del diseño es de
  cola larga con moda cero: ~2/3 de los cambios bien diseñados **no** mueven su métrica objetivo. La
  promesa honesta y defendible es *iterar y medir*, no *rediseñar y despegar*.
- **C3 — Cuando una cifra sea espectacular, rastrear la fuente primaria antes de usarla.** Las
  cuatro cifras más citadas del valor del diseño colapsan cada una en una única fuente no auditable
  —y una de ellas (671%) en ninguna. La regla operativa: *si no puedo leer el estudio primario, no
  entra a un entregable.*

**Sobre cómo leer tendencias**

- **C4 — Descontar por incentivo del emisor, siempre.** Los reportes de tendencias los publican
  quienes venden las herramientas de la tendencia; las encuestas laborales optimistas las publican
  quienes le venden a ese público; el movimiento anti-slop lo lidera quien vende cursos. No los
  descarta — obliga a preguntar **quién gana si creo esto**.
- **C5 — Distinguir pico de tendencia.** El pánico gremial es **estacional**: repica con cada
  lanzamiento de modelo. Verificar todo pico contra el calendario de releases antes de leerlo como
  cambio estructural.
- **C6 — Contar conducta, no volumen.** La mejor evidencia social de esta investigación no fue un
  hilo viral: fue **Apple enviando un slider de transparencia** y **gente pagando por talleres de
  riso**. Conducta observable > cantidad de likes. Y una nota publicada en seis medios con el mismo
  texto es **una** pieza de cobertura, no seis.
- **C7 — El hallazgo negativo es un hallazgo.** "No existe ningún caso de rediseño con métricas en
  un documento auditado", "no hay consultora de diseño con crecimiento publicado", "el service design
  no aparece en la conversación": las tres se obtuvieron buscando y no encontrando, y las tres son
  informativas.

**Sobre diseñar con IA**

- **C8 — La explicabilidad genérica no calibra la confianza; la verificabilidad sí.** Poner "¿por
  qué veo esto?" en todos lados aumenta la confianza *con independencia de la calidad de la
  explicación* — es decir, produce sobre-confianza. Lo que funciona: hacer la salida **verificable**,
  poner **fricción deliberada donde la tarea es difícil**, y **no ponerla donde es fácil**.
- **C9 — Sospechar de la interfaz que se reconfigura sola.** Hay 20 años de evidencia de que la
  adaptación rápida controlada por el sistema pierde frente a lo estático, y de que **adaptable**
  (control del usuario) le gana a **adaptativo** (control del sistema). La generative UI es la
  versión extrema de lo que ya falló. Consistencia y aprendibilidad son el costo oculto.
- **C10 — Más personalización no es mejor cuando la privacidad está saliente.** La personalización
  con datos personales puede rendir **peor** que el mensaje genérico si el usuario está atento a la
  privacidad. Directamente relevante para seguros, donde el dato es sensible por definición.
- **C11 — Desconfiar de toda métrica de productividad autorreportada.** Existe un RCT donde
  desarrolladores expertos fueron **19% más lentos** con IA creyendo ser 20% más rápidos: una brecha
  percepción-realidad de ~39 puntos. **Cualquier "somos X% más rápidos con IA" sin medición objetiva
  debe leerse como sentimiento, no como dato.**

**Sobre estética**

- **C12 — Claridad antes que ornamento, con evidencia.** El "efecto estética-usabilidad" se reduce a
  menos de la mitad al controlar por fluidez de procesamiento: buena parte de lo que se atribuye a la
  belleza es en realidad **facilidad de procesamiento**. Liquid Glass es la demostración de que ni la
  organización con más recursos de diseño del mundo es inmune.
- **C13 — El anti-diseño sin disciplina destruye la usabilidad.** Brutalismo con grilla clara ≠
  anti-diseño caótico; el segundo llegó a 8-10% de éxito de tarea en páginas densas de información.

**Sobre cómo leer la evidencia de una tecnología nueva** *(ascendidas en la iteración 2)*

- **C15 — Preguntar siempre qué se midió: preferencia, desempeño o consecuencia.** Toda la evidencia
  favorable a la generative UI mide **preferencia declarada en sesión única, contra una línea base
  débil** (texto plano) y producida por quien vende la tecnología; toda la evidencia desfavorable
  mide **atributos de soporte** (prevención de errores, recuperación, ayuda, eficiencia) y
  **consistencia**. No se contradicen: miden cosas distintas. La pregunta operativa ante cualquier
  claim de una tecnología de diseño es *¿esto es un dato de gusto, de desempeño o de consecuencia?*
  — y el discurso casi siempre presenta el primero como si fuera el tercero.
- **C16 — La curva antes que el signo.** Ante "¿la IA acelera el trabajo?", la respuesta correcta no
  es sí ni no: es *¿en qué punto de la curva está este equipo?* Un piloto que mida el promedio de
  mundos distintos medirá cero y concluirá mal. Diseñar el piloto **segmentando por madurez del
  sistema y por perfil**, no agregando.
  ⚠️ **Corregida en la iteración 3.** La regla sobrevive; **las cifras con que se ilustraba, no**.
  El "4,3 min senior vs. 1,2 junior" no tiene fuente rastreable (F-404) y la relación con la
  seniority resultó **no monótona**: con exposición acumulada el escrutinio *baja*, no sube (F-407,
  H26). Lo que queda firme es el desplazamiento de esfuerzo de generación a verificación (+91% de
  tiempo de revisión, F-406). **Usar la regla para diseñar el piloto; no usar los números para
  prometer su resultado.**
- **C17 — El campo no corrige: acumula.** *(Reformulada en la iteración 3.)* La iteración 2 creyó que
  cuando una cifra estrella se desmonta, la industria **rota** a otra. Es peor que eso: **no rota,
  suma**. El 671%, el 135%, el McKinsey de 2018 y el "$1→$100" de Forrester siguen los cuatro vivos
  y circulando en paralelo en 2026, cada uno en su nicho, y ninguno de sus divulgadores retiró nada
  tras el cuestionamiento. Consecuencia operativa: **no esperes que una refutación reduzca la
  circulación de una cifra**; la única defensa que funciona es local y previa — **exigir el diseño
  del estudio antes de dejarla entrar**: ¿alguien ejecutó el cambio y midió el resultado, o alguien
  estimó el ahorro?

**Sobre geografía y contexto local** *(ascendida en la iteración 2)*

- **C18 — En LatAm, la conducta es local y el marco es importado; usar el primero, descontar el
  segundo.** Se creyó que el ciclo identitario del gremio llegaría desfasado a la región y **no es
  así**: la adopción de IA en Brasil supera a la anglosajona y la compresión del rol de diseño ya se
  ejecutó en la empresa más valiosa de la región. Pero el *relato* que circula en español y
  portugués es traducción, y arrastra sin filtro las cifras de emisores interesados. Regla operativa
  para cualquier entregable regional: **buscar el dato de conducta local** (decisiones corporativas,
  estudios con muestra propia) y **no citar la cifra anglosajona sin su descuento por emisor** (C4).
  ⚠️ *Provisional: ascendida con una sola iteración de respaldo.*

**Sobre cómo se cita la evidencia** *(ascendidas en la iteración 3)*

- **C19 — Antes de descontar al emisor, verificar que el emisor lo haya dicho.** C4 enseña a
  preguntar *quién gana si creo esto*. La iteración 3 encontró un fallo de un orden peor: cifras
  atribuidas a **Gartner que Gartner nunca publicó** — tres en una sola pieza (F-408 vs. F-418).
  Contra el emisor interesado sirve descontar; contra la **autoridad prestada** descontar no alcanza,
  porque no hay nada que descontar. Regla operativa: cuando una cifra viene con el nombre de una
  autoridad pegado y **sin enlace al reporte**, el paso 1 no es evaluarla — es **buscar si existe**.
  Si el emisor citado no la publicó, la cifra no es débil: es inventada.
  ⚠️ *Provisional: ascendida con una sola iteración de respaldo (H23).*
- **C20 — El chequeo de eco de cita se aplica también hacia adentro, y sobre todo cuando el hallazgo
  te conviene.** Este node desmontó cinco cadenas de eco ajenas y luego **adoptó una propia sin
  rastrearla** (el impuesto de verificación, §2.5 n.º 6). No fue descuido: entró sin resistencia
  porque *resolvía* una divergencia que el node arrastraba desde la iteración 1. **La condición de
  riesgo no es el hallazgo espectacular, es el hallazgo que cierra una herida abierta.** Regla:
  cuando un mecanismo reconcilie una contradicción propia, tratarlo con **más** escrutinio que a la
  cifra que vino a reemplazar, no con menos (H24).
  ⚠️ *Provisional: ascendida con una sola iteración de respaldo.*
- **C21 — La conducta también se disputa: verificar la atribución, no solo el hecho.** C6 dice contar
  conducta, no volumen — y sigue en pie. Pero la iteración 3 muestra su límite: el caso testigo más
  limpio del node (MercadoLibre desvinculando UX "por IA") tiene **desmentido oficial de la propia
  empresa** — "reorganización interna", "menos del 0,09% de la plantilla" (F-419) — mientras
  ex-empleados sostienen lo contrario. **El despido ocurrió** (hecho); **la causa está en disputa**
  (atribución), y es la atribución la que hace el argumento. Es el mismo *scapegoating* que Gallup
  documentó en inglés (F-282), ahora en español. Regla: separar siempre **el evento** de **su
  explicación**, y no dejar que un dato de conducta pase a afirmación fuerza si la causa la declara
  una parte interesada — en cualquiera de las dos direcciones.
  ⚠️ *Provisional: ascendida con una sola iteración de respaldo.*

**Sobre el poder del diseño**

- **C14 — La evidencia causal más fuerte del poder del diseño es sobre su capacidad de daño.** Los
  dark patterns casi cuadruplican la aceptación de un plan dudoso, en experimento aleatorizado con
  muestra representativa, y afectan a todos los grupos —los proxies clásicos de vulnerabilidad
  explican poco. Es el único punto donde la crítica teórica al diseño está empíricamente confirmada.
  **Leído en positivo: el diseño mueve conducta de verdad; lo que está mal probado es que la mueva
  hacia el valor.**

---

## 8. 📓 Bitácora de iteraciones

| # | Fecha | Foco de la corrida | Qué cambió | Pendiente que hereda la siguiente |
|---|---|---|---|---|
| 1 | 2026-07-26 | Barrido fundacional de 360°: impacto tangible vs. propuesta innovadora, en producto/UX, IA, design systems, servicio y visual | **Creación del node.** 92 fuentes registradas (F-237 a F-328). Escala de madurez (§5) y 14 reglas de criterio (§7) establecidas. Tablero abierto con 18 hipótesis | (a) **H13 es falsable el 5-ago-2026** — Figma reporta Q2; (b) barrido en **español/portugués** (H17), todo lo hallado es anglosajón; (c) **service design** merece pasada propia (H18); (d) leer los preprints de generative UI de primera mano (el proxy bloqueó arXiv); (e) buscar si apareció **replicación independiente** del efecto design systems (H6) |
| 2 | 2026-07-29 | **Confrontación**, no novedad: los 5 pendientes heredados (H17 español/portugués · H18 service design · H6 replicación · H3 generative UI · H13 Figma) | **4 hipótesis movidas.** ⬇️ **H17 `refutada`** (no hay desfase geográfico). ⬆️ **H3 `parcial`** (preferencia confirmada; desempeño de soporte y consistencia refutados; longitudinal sigue sin existir). ⬆️ **H18 `parcial`** (base institucional sí, madurez no probada, crisis declarada desde adentro). **H6 sigue abierta** pero suma la **5.ª cadena de eco** (135% modelado, F-397). **Divergencia ⚔️ de productividad reconciliada por mecanismo** (impuesto de verificación, F-388). 19 fuentes nuevas (F-380 a F-398), 4 hipótesis nuevas (H19-H22), 4 reglas nuevas (C15-C18) | (a) **H13 se resuelve el 5-ago-2026** — leer el reporte Q2 de Figma y el precio a 90 días; (b) **H22 se pone a prueba sola**: registrar qué cifra ocupa el lugar del "ROI del diseño" en la iteración 3; (c) **H21 (shadow AI / gobernanza) es la más accionable para Rimac** — no se buscó dato peruano equivalente al brasileño; (d) sigue sin leerse **ningún texto completo** (proxy 403 en arXiv, ACM, MDPI, gov.uk, IBPAD): las 19 fuentes nuevas están soportadas en abstracts y snippets; (e) **H20** (conducta local vs. marco importado) requiere una auditoría sistemática de piezas hispanohablantes |
| 3 | 2026-08-02 | **Auditoría, incluida la del propio node**: los 5 pendientes heredados (H13 Figma · H22 rotación de la cifra · H21 shadow AI peruano · H20 auditoría hispanohablante · lectura de texto completo) + confrontación de H3, H5, H6, H7 | **6 hipótesis movidas y una autocorrección estructural.** ⬇️ **H19 degradada**: la cifra ancla del *impuesto de verificación* (4,3/1,2 min) **no tiene fuente primaria rastreable** — sexta cadena de eco del node y **la primera propia** (F-404); F-388 resultó síntesis de autor único, no experimento. ⬆️ **H20 `respaldada`** con 13/13 (100%) vs. el >70% predicho. ⬆️ **H5 `parcial`** (F-401, peer-reviewed, N=452: la brecha existe pero es de ~1 pt, no ≥20 pp — la hipótesis acierta el signo y falla la escala). ⬆️ **H10 y H11 `parcial`**. ⬆️ **H15 `parcial`** (R/GA +25% YoY, primer contraejemplo en 3 iteraciones, pero dentro de la cláusula de escape). 🔄 **H22 reformulada**: la industria no rota cifras, **las acumula**. ⚠️ **Desmentido oficial de MercadoLibre** vuelve contestado el caso testigo de la iter. 2. 31 fuentes nuevas (F-399 a F-429), 4 hipótesis nuevas (H23-H26), 3 reglas nuevas (C19-C21) y **2 reglas corregidas** (C16, C17) | (a) **H13 se resuelve el 5-ago-2026**: leer el reporte Q2 de Figma contra el guidance de $348-350M (~40%) y el precio a 90 días — **es la única hipótesis con fecha de vencimiento y ya venció**; (b) **H21: dejar de barrer genéricamente** — tres iteraciones en blanco; requiere fuente primaria (asociación de diseño peruana o encuesta interna de Rimac); (c) **H24 se pone a prueba sola**: registrar si lo que se cae en la iter. 4 es otra vez un hallazgo *reconciliador*; (d) **H7 necesita reformulación** antes de seguir buscando (F-403 muestra fluidez y estética subiendo juntas); (e) el proxy 403 es **estructural, no mala suerte** — tercera iteración sin leer un solo texto completo: **asumirlo en el diseño de la corrida** en vez de declararlo como limitación cada vez |

---

## 9. Limitaciones de la iteración 1

- **Bloqueos de red que condicionan la confianza de varias fuentes.** El proxy devolvió 403 en
  `arxiv.org`, `mckinsey.com`, `nngroup.com`, `sec.gov`, `bls.gov`, `reddit.com`, `x.com` y
  `news.ycombinator.com`. Consecuencias concretas: **no se leyó línea por línea ningún filing de
  Figma/Adobe** (las cifras marcadas A se recuperaron indirectamente con URL primaria verificada, y
  **deben revalidarse contra EDGAR antes de publicarse**); **no se leyeron los preprints de
  generative UI en su texto completo**; y en la pista social **no se pudieron contar upvotes ni leer
  hilos de primera mano** — es decir, el eje de *validación social*, que es justamente lo que
  distingue a esa pista de un resumen de prensa, quedó medido con menor confianza que el eje de
  frecuencia.
- **Autoría no verificada** en tres fuentes (F-238 y dos preprints de 2026): citadas por título y
  URL, sin inventar nombres.
- **Sesgo geográfico**: todo lo hallado es anglosajón. No se cubrió literatura ni conversación en
  español/portugués — crítico dado el contexto peruano del proyecto (H17).
- **Diseño de servicio es el subcampo con menor densidad de evidencia** de los cinco revisados: en
  salud, menos de la mitad de los estudios de codiseño evalúa outcomes, y socialmente es 🧊.
- **No se accedió a bases indexadas** (Scopus, Web of Science, ACM DL completo) ni a bases de venture
  (PitchBook, Crunchbase).
- **Asimetría de vigencia en la pista de negocio**: el dato operativo de Figma es al 31-mar-2026,
  ~4 meses más viejo que el dato de precio de su acción.

---

## 10. 🔁 Iteración 2 (2026-07-29) — confrontación de las hipótesis heredadas

Corrida de `/trinidad` con mandato explícito de **confrontar antes que buscar novedad**. Los cinco
pendientes que dejó la iteración 1 se atacaron uno por uno. Las tres pistas se mantienen separadas.

**Resumen de la corrida en una frase por pista:**

- 🔬 **Empírica**: la evidencia de generative UI **por fin llegó**, y dice exactamente lo que la
  teoría de 2004 predecía — gusta en la primera sesión y falla en todo lo que sostiene el uso
  repetido.
- 📱 **Social**: la hipótesis del desfase latinoamericano **era falsa**, y su refutación vino de
  conducta corporativa, no de conversación.
- 📈 **Negocio**: el ROI del diseño **no se corrigió, se recicló** — cayó el 671% y ocupó su lugar
  un 135% igual de modelado.

### 10.1 🔬 Generative UI: la evidencia llegó y se partió en dos mitades limpias

La iteración 1 clasificó la generative UI como 🔴 *propuesta sin respaldo independiente* y lo fundó
en literatura de hace 20 años (Findlater & McGrenere, F-247). En estos meses aparecieron **siete
piezas nuevas**, y el resultado no es que la clasificación estuviera mal: es que ahora se puede
partir el claim en dos, y cada mitad tiene un veredicto distinto.

**Mitad que gana — "gusta más":**

- El paper insignia (F-380, Leviathan/Valevski, Google) muestra preferencia humana abrumadora frente
  a la salida markdown de un LLM. ⚠️ Tres descuentos que el titular no lleva: es **preprint sin
  revisión por pares**, la línea base es **texto plano** (un rival deliberadamente débil), y **sus
  propios autores admiten que los resultados son peores que los de expertos humanos**, "al menos
  comparables en el 50% de los casos". Un 50% de empate contra un humano se está comunicando como
  una victoria.
- La versión peer-reviewed existe y es más seria: hasta **72% de preferencia** sobre interfaces
  conversacionales en tareas densas en información (F-381, Findings of ACL 2026). Sigue siendo
  **preferencia declarada en sesión única**.

**Mitad que pierde — "funciona mejor":**

- **138 pantallas** generadas por Figma, Banani y Stitch, evaluadas contra las 10 heurísticas de
  Nielsen (F-382, CHI 2026): baja tasa de soporte justo en **H5 prevención de errores, H7 eficiencia
  de uso, H9 recuperación de errores y H10 ayuda/documentación**. Es decir, **falla precisamente en
  los atributos que solo importan cuando el usuario vuelve** — y brilla en los que se juzgan de un
  vistazo. Esa es la firma exacta de un artefacto optimizado para la primera impresión.
- Una revisión sistemática (F-384) mide el defecto de base: **prompts idénticos producen interfaces
  sustancialmente distintas, incluso entre ejecuciones repetidas de la misma herramienta**. La
  inconsistencia **no es inmadurez del modelo: es una propiedad del paradigma**.
- La comunidad HCI produjo contrapeso publicado, no solo tuits: un position paper explícito
  *Against Generative UI* (F-383), el traslado del marco de deuda técnica oculta a las interfaces
  maleables (F-385), y un reencuadre útil de Microsoft Research (F-386): con generative UI **el
  objeto de usabilidad deja de ser la interfaz y pasa a ser el generador**.

⭐ **Lo que esto le hace a H3.** La hipótesis predecía: *gana en preferencia en la sesión 1, pierde
en tiempo de tarea y aprendibilidad a lo largo de ≥5 sesiones.* La primera mitad está **confirmada**.
La segunda no está confirmada — pero sus dos precondiciones causales (inconsistencia entre
ejecuciones, ausencia de andamiaje de error y ayuda) **ya están medidas**. H3 pasa a `parcial`.

⚠️ **Y el hallazgo negativo que vale tanto como los positivos:** tras dos iteraciones buscándolo,
**sigue sin existir un solo estudio longitudinal independiente de generative UI**. Toda la evidencia
favorable la producen los fabricantes y mide una sola sesión. Los autores de F-382 lo declaran ellos
mismos como limitación. **Un paradigma se está adoptando con evidencia que, por construcción, no
puede detectar su modo de falla principal.**

### 10.2 🔬📱 Service design: no está en silencio, está en otra tribuna — y en crisis según los suyos

La iteración 1 registró un hallazgo negativo (🧊: el service design no aparece en la conversación
social) y lo dejó como H18 con una lectura optimista: *silencio = madurez*. La pasada propia
encuentra las dos mitades, y la optimista **no gana**.

**A favor de "existe y está institucionalizado":**

- El gobierno británico comisionó y publicó una **revisión de evidencia sobre diseño público**
  (PDER, F-387): tres revisiones de literatura por un equipo académico interdisciplinario más un
  banco de casos, con evidencia sobre outcomes (efectividad, innovación, eficiencia) y sobre
  barreras institucionales (liderazgo, capacidad, financiamiento, oportunidad de iterar). ⚠️ Con un
  detalle que la vuelve menos útil de lo que parece: **se redactó entre sept-2023 y mar-2024 y se
  publicó en jul-2025** — su corpus es **anterior a la IA generativa**.
- La infraestructura sigue viva: SDN (2004), conferencia global 2026, y una edición de *Touchpoint*
  titulada precisamente "From AI to Synthetic Services" (F-395).
- **Y hay tribuna local**: existe una comunidad de service design en **Lima desde junio de 2017**,
  activa en 2026 con su Jam de 48 horas (dentro del Global Service Jam simultáneo en 85 ciudades) y
  sesiones periódicas (F-394). Directamente relevante para el proyecto: **el service design en Perú
  no hay que fundarlo, hay que encontrarlo.**

**En contra de "es madurez":**

- Búsqueda adversarial explícita: una figura reconocida *dentro* de la disciplina describe el campo
  en "una verdadera **crisis de la práctica**" (F-393), atribuida a que las organizaciones
  invirtieron en diseño durante el crecimiento **sin posicionar los equipos ni demostrar valor**, y
  a que el design thinking no cumplió su promesa. Es el mismo diagnóstico que la pista de negocio de
  la iteración 1 encontró en las consultoras (IDEO −67%, Veryday cerrada, R/GA a PE).
- **No existen métricas públicas de membresía de SDN** ni de presupuesto de service design en
  organizaciones. Se buscaron y no aparecieron: H18 **no se puede cerrar con dato duro en ninguna
  dirección**.

⭐ **Veredicto honesto:** *silencio social ≠ irrelevancia* queda **respaldado**. *Silencio social =
madurez* queda **sin respaldo, y con contraevidencia interna**. La lectura que sobrevive es la
tercera: el service design tiene instituciones, evidencia y comunidad, pero **no tiene un relato con
el que participar de la conversación identitaria del gremio** — y por eso es invisible justo en el
momento en que el gremio decide quién es. H18 → `parcial`.

### 10.3 📈 Design systems y productividad: una cifra reciclada y un mecanismo que reconcilia

**Lo que no apareció (y se buscó):** ninguna replicación independiente del efecto de un design
system sobre el tiempo de desarrollo. **H6 sigue abierta tras dos iteraciones de búsqueda.**

**Lo que sí apareció:**

- **Quinta cadena de eco de cita.** El "**135% de ROI**" que circula en 2026 no es un estudio: es una
  **calculadora** publicada en 2022 (F-397) que modela US$646.000 → US$1.517.400 de ahorro estimado
  a cinco años, alimentada con cifras autorreportadas por la industria. Nadie ejecutó y midió.
  ⭐ **El patrón importa más que la cifra**: cuando el 671% se desmontó, la industria **no dejó de
  citar cifras — cambió de cifra**. De ahí sale H22 y la regla C17.
- **Dato de supervivencia**, que es más informativo que cualquier ROI: la satisfacción con el buy-in
  cae de 42% a 32% interanual y **solo ~40% de los design systems sigue activo pasados 18 meses**
  (F-396). ⚠️ Fuente con interés del emisor directo (vende la herramienta) — lo que hace *más*
  creíble el dato negativo, no menos.
- ⭐ **El hallazgo más valioso de la corrida para el resto del proyecto: el impuesto de
  verificación.** La iteración 1 dejó abierta la divergencia ⚔️ entre METR (−19% de velocidad real
  en devs expertos) y el preprint de IA alineada a design system (−46/−69% de time-to-delivery), y
  aventuró a mano que la diferencia estaba en la madurez del código base. Ahora eso tiene nombre y
  cifras (F-388): **~4,3 minutos de verificación por sugerencia para un senior vs. ~1,2 para un
  junior, escalando con la madurez del código base hasta exceder el ahorro de generación**; juniors
  ganan 30-40% pero con atrofia de habilidad. **Los dos estudios no se contradicen: miden extremos
  opuestos de la misma curva.** ⚠️ Preprint sin revisión por pares — es la mejor explicación
  disponible, no un hecho establecido (H19).

### 10.4 📱 El barrido en español y portugués: H17 refutada, y lo que quedó vale más

La iteración 1 declaró su sesgo anglosajón como limitación crítica y apostó a H17: *el ciclo
identitario del gremio llega a LatAm desfasado, atenuado, o el mercado local ni participa.*
**Es falso en las tres formas.**

- **Adopción: LatAm va por delante, no por detrás.** El estudio brasileño (F-389, Môre + IBPAD,
  **N=823 profesionales**, nov-2025) reporta **94% de adopción de IA** entre diseñadores brasileños
  y 66% de uso diario — **por encima del 89% anglosajón** (F-280). Es, además, **la única evidencia
  local con muestra propia** hallada en toda la corrida.
- **Conducta: la compresión del rol ya se ejecutó en la región.** MercadoLibre —la empresa
  latinoamericana más valiosa en bolsa— desvinculó **119 personas del área de UX** (32 en Argentina)
  en una reestructuración que **integra explícitamente los roles de diseño y contenido** apoyándose
  en IA; los perfiles más golpeados fueron **UX writers y especialistas de contenido** (F-391).
  ⭐ Aplicando C6 (contar conducta, no volumen): esto pesa más que todo el discurso anglosajón sobre
  "el fin del UX designer" junto, porque **es una decisión corporativa fechada y documentada, no una
  queja de LinkedIn**.
  ⚠️ **Corregido en la iteración 3 — leer junto con §11.6 y C21.** MercadoLibre **desmintió
  oficialmente** la atribución a IA: declaró que fue una "reorganización interna para integrar
  Diseño y Contenido" y que representó "menos del 0,09% de su plantilla de más de 125.000
  empleados" (F-419), mientras ex-empleados sostienen que parte de su trabajo era entrenar los
  sistemas que los reemplazaron. **El despido es un hecho; la causa está en disputa.** Deja de ser
  "conducta corporativa limpia" y pasa a ser **caso contestado**, con el mismo descuento por
  *scapegoating* que la iteración 1 aplicó al mercado anglosajón (F-282). **La refutación de H17 se
  sostiene igual**, pero sobre otras patas: el estudio brasileño con muestra propia (F-389) y ahora
  también Livspace en India (F-416). La ironía es que la iteración 1 registró que el daño se concentraba en
  juniors; aquí el rol eliminado es **una especialización entera**.
- **Discurso: existe, y es traducción.** El vocabulario anti-slop, la "fatiga visual post-IA" y el
  neo-brutalismo circulan en medios masivos en español (F-390), y el debate identitario tiene sus
  propios podcasts en español. Pero el material **cita cifras anglosajonas de emisores interesados**
  —el 89% de Figma reaparece en prensa argentina y en escuelas españolas— **sin el descuento que la
  propia fuente exige** (C4).

⭐ **Lo que quedó vivo es mejor que la hipótesis refutada.** La distinción útil no es *anglosajón vs.
LatAm* sino **conducta local vs. marco importado** (H20): la región **genera datos y decisiones
propias** y **consume interpretación traducida**. Y de ahí sale el hallazgo más accionable para el
proyecto: en Brasil, **60% de los diseñadores usa IA en cuentas personales sin lineamiento
corporativo y solo 14% recibió capacitación de la empresa** (F-389). **El problema no es adopción,
es gobernanza** (H21) — lo cual, en un negocio asegurador donde el dato del cliente es sensible por
definición, no es un detalle de RRHH.

⚠️ **Nota de honestidad sobre este barrido:** el dato duro local es **brasileño y argentino**. Para
**Perú** solo se hallaron portales de empleo y una comunidad de service design (F-394): **no se
encontró ningún estudio peruano con muestra propia** sobre diseñadores e IA. El sesgo geográfico se
redujo, no se eliminó.

### 10.5 📈 Figma antes del 5 de agosto: H13 sigue en pie y se resuelve en una semana

Al 13-jul-2026 FIG cotizaba ~**US$23,57**, con rango de 52 semanas de **US$16,60 a US$142,92** —
**~−83/−84% desde el pico y todavía bajo el precio de IPO (US$33)** — mientras el consenso de
analistas apunta a US$30,56 a 12 meses, con 5 compras y **0 ventas** (F-398). El desacople que la
iteración 1 identificó **se mantiene intacto**: 46% de crecimiento interanual y NDR de 139% (el más
alto en más de dos años) conviviendo con una acción por debajo de su precio de salida.

**H13 se resuelve el 5 de agosto de 2026** (reporte Q2) y en los 90 días siguientes. La condición
está fijada de antemano: *si Figma reporta ≥40% de crecimiento y la acción no recupera sobre US$33,
el mercado descuenta disrupción por IA, no ejecución.* La iteración 3 debe leerlo y cerrarla.

### 10.6 Limitaciones de la iteración 2

- ⚠️ **Ninguna de las 19 fuentes nuevas se leyó en texto completo.** El proxy devolvió **403 en
  todos los intentos de lectura directa**: arXiv, ACM Digital Library, MDPI, gov.uk, IBPAD, Xataka.
  Todo el §10 está construido sobre **abstracts y snippets de búsqueda**. Consecuencias concretas:
  no se verificaron tamaños de muestra ni métodos línea por línea; **las cifras del PDER, del estudio
  brasileño y de la revisión sistemática de consistencia deben revalidarse antes de publicarse en un
  entregable**. Es la misma limitación de la iteración 1 y **no mejoró**: asumirla como estructural
  del entorno, no como mala suerte.
- **Autoría no verificada** en 6 de las 19 fuentes nuevas (F-381 a F-386, F-388): citadas por título,
  venue y URL, sin inventar nombres.
- **El barrido hispanohablante no alcanzó a Perú con dato propio** (ver §10.4).
- **H18 quedó sin dato duro**: no hay métricas públicas de membresía ni de presupuesto de service
  design. Se buscaron.
- **La pista social sigue midiéndose por frecuencia y no por validación**: sin acceso a X ni Reddit,
  no se pudieron contar reacciones ni leer hilos de primera mano. La compensación deliberada de esta
  iteración fue **apoyarse en conducta observable** (despidos de MercadoLibre, eventos con fecha de
  Service Design Lima, control de transparencia de Apple en la iteración 1) en vez de en volumen —
  lo cual es más sólido, pero mide otra cosa.
- **H16 (degradación del reporting) no se pudo avanzar** en esta corrida.

---

## 11. 🔁 Iteración 3 (2026-08-02) — la iteración en que el node se auditó a sí mismo

Corrida de `/trinidad` con el mismo mandato de **confrontar antes que buscar novedad**. Las tres
pistas se mantienen separadas. La corrida terminó siendo, sobre todo, un ejercicio de honestidad
hacia adentro: el mejor hallazgo de la iteración anterior no sobrevivió a la regla que el propio
node aplica a los demás.

**Resumen de la corrida en una frase por pista:**

- 🔬 **Empírica**: el mecanismo que la iteración 2 celebró **no tiene fuente** — y las dos ausencias
  que el node arrastra (longitudinal de generative UI, replicación de design systems) llegaron a su
  tercera confirmación consecutiva.
- 📱 **Social**: la sospecha sobre el corpus hispanohablante era correcta y **se quedó corta** — no
  solo cita lo anglosajón interesado, cita autoridades que no dijeron lo que se les atribuye.
- 📈 **Negocio**: el ROI del diseño **no rota, acumula** — las cinco cifras desmontadas siguen vivas
  en paralelo, ninguna retirada; y H13 llega a su fecha de vencimiento con la condición más limpia
  que ha tenido.

### 11.1 🔬 Tercera ausencia consecutiva: H3 y H6

**Generative UI (H3).** Tres búsquedas dirigidas ("longitudinal", "multi-session", "between-subjects
≥5 sesiones") y ningún estudio que califique. Lo más cercano: F-399, que compara cuatro condiciones
en horizonte corto (no repite tarea con la misma persona), y F-400 (ACM DIS 2025, N=37, journaling
de una semana), que es **formativo y cualitativo** — produce datos ricos sobre cómo los
profesionales usan la herramienta, pero **no compara generative UI contra UI estática en tiempo de
tarea ni en aprendibilidad**, que es lo único que movería la hipótesis.

**Design systems (H6).** Ninguna replicación independiente, por tercera vez. Lo que sí cambió es el
estatus del estudio existente: **F-259 dejó de ser preprint y fue aceptado en SBES 2026** (venue con
arbitraje por pares de la SBC). Sube el rigor del estudio; **no sube su generalizabilidad** — misma
muestra, misma empresa, sin devs externos. ⭐ *El campo institucionaliza el mismo estudio en vez de
replicarlo*, mientras sigue publicando calculadoras: F-425 usa el 135% de 2022 como método vigente
para "medir el ROI de un design system en 2026".

⚠️ **Lo que estas dos ausencias ya son.** Tres barridos independientes, con términos distintos, en
tres momentos distintos, y cero resultados en ambos casos. Eso deja de ser azar de búsqueda y pasa a
ser una **propiedad del campo**: se están adoptando dos paradigmas (interfaces generadas, design
systems como palanca de productividad) con una base de evidencia que, por construcción, no puede
detectar su modo de falla principal. Aplicando C7, la ausencia es el hallazgo — y a la tercera, es
un hallazgo sólido.

### 11.2 🔬⚠️ El impuesto de verificación: el node se desmonta a sí mismo

**Este es el hallazgo central de la iteración 3, y es una corrección.**

La iteración 2 cerró celebrando que la divergencia ⚔️ de productividad con IA —METR (−19% de
velocidad real en devs expertos) vs. preprint DS-aware (−46/−69% de time-to-delivery)— por fin tenía
un mecanismo reconciliador con nombre y cifras: el **impuesto de verificación**, ~4,3 min por
sugerencia para seniors vs. ~1,2 para juniors, escalando con la madurez del código base.

**Esa cifra no tiene fuente primaria rastreable.** El rastreo la encuentra repetida casi palabra por
palabra en Sonar, Faros AI, Augment Code, Entrepreneur y mariothomas.com; el punto más profundo
alcanzable es un artículo de **DZone** (F-404) que dice literalmente *"in a recent study of 250
developers across five organizations…"* **sin nombrar autor, institución ni enlazar el estudio**. No
existe paper, preprint ni informe con ese N y esas cifras. Y el preprint que el node citaba como
mecanismo (F-388) resultó ser de **autor único** y de naturaleza **sintética** — un marco teórico
que cita cifras de terceros, **no un experimento propio con muestra declarada**.

⭐ **Por qué importa más que la cifra.** Es la **sexta cadena de eco de cita** del node (§2.5) y la
primera que estaba *adentro*. Las cinco anteriores eran ajenas: el node las cazó aplicando C3 y C17.
Esta entró sin resistencia, y la razón es específica y generalizable: **cerraba una herida abierta**.
Resolvía una contradicción que el node arrastraba desde la iteración 1, y esa condición —no lo
espectacular de la cifra— es lo que bajó la guardia. De ahí sale **C20** y la hipótesis **H24**, que
predice que los próximos errores del node volverán a concentrarse en hallazgos reconciliadores.

**Qué queda en pie y qué se cae.**

| Afirmación | Estado tras la iteración 3 |
|---|---|
| La IA desplaza esfuerzo de generación hacia verificación | ✅ **Se sostiene** — telemetría independiente con N grande: **+98% de PRs y +91% de tiempo de revisión** (F-406) |
| La magnitud es 4,3 min (senior) vs. 1,2 min (junior) | ❌ **Se cae** — sin fuente primaria (F-404) |
| El impuesto crece monótonamente con la seniority | ❌ **Se rompe** — F-407 (400 revisores, 11.429 revisiones): la aprobación **sube +14,5 pp** a través de deciles de exposición; **más experiencia acumulada → menos escrutinio**, no más |
| Existe un experimento que manipule madurez del código base como factor | ❌ **No existe** — todo lo disponible es yuxtaposición narrativa post-hoc de estudios distintos |

⚠️ **Alerta de blindaje.** Existe un preprint riguroso titulado *The Verification Tax: Fundamental
Limits of AI Auditing in the Rare-Error Regime* (F-405), que es un **paper teórico-estadístico sobre
límites de auditoría de calibración de modelos** y **no tiene ninguna relación** con tiempos de
revisión de código. Se registra explícitamente porque una búsqueda futura por "verification tax"
lo devolverá y **podría prestarle su autoridad a una cifra que no la tiene** — que es exactamente el
mecanismo de C19.

De la inversión del signo (más exposición → menos escrutinio) sale **H26**, que si se sostiene
cambia el diseño de cualquier control de calidad sobre trabajo asistido por IA: **el riesgo no está
en el novato que no sabe revisar, sino en el veterano que ya se acostumbró.**

### 11.3 🔬 H5: llegó el estudio que pedía, y la hipótesis acierta el signo pero falla la escala

H5 predecía que en cualquier estudio que midiera **a la vez** desempeño objetivo y percibido, la
mejora subjetiva excedería a la objetiva en **≥20 pp**. Era "la hipótesis de mayor valor
destructivo" del node.

Apareció el estudio del tipo exacto que pedía, y es la mejor fuente nueva de esta iteración:
**F-401** (*Computers in Human Behavior*, vol. 175, peer-reviewed, Study 1 + réplica interna,
**N=452**). Con asistencia de IA, el desempeño objetivo en razonamiento lógico sube **~3 puntos**
sobre la norma poblacional y la auto-estimación sube **~4 puntos**. **La brecha existe y va en la
dirección predicha, pero es de un solo dígito — no de ≥20 pp.** Hallazgo adicional notable: el
efecto Dunning-Kruger **desaparece** con uso de IA — la herramienta nivela el desempeño real sin
corregir la sobreestimación.

**F-402** replica el diseño ideal (objetivo + percibido + fisiológico: rúbrica, NASA-TLX, EEG,
eye-tracking, EDA, HRV) en dominio de código, multisitio: con IA, razón θ/α de EEG más baja y
parpadeo más alto, consistente con **menor compromiso cognitivo al delegar**.

⭐ **Lo honesto es decir que el node se pasó de rosca.** El umbral de ≥20 pp era una apuesta, no una
predicción fundada, y venía de la brecha de ~39 puntos del RCT de METR (C11) — un caso extremo
tratado como si fuera el caso típico. **C11 sigue en pie** (desconfiar del autorreporte de
productividad), pero su magnitud debe leerse como techo, no como norma. H5 pasa a `parcial` con el
umbral marcado para reformulación. Sigue sin existir la medición en el dominio propio: **ningún
estudio mide objetivo y percibido en design systems o madurez de diseño**.

### 11.4 🔬 H7: la dicotomía puede estar mal planteada

**F-403** (CHI 2026, peer-reviewed, N=48, 10 apps, Material 3 vs. Material 3 Expressive) encuentra
fijación visual correcta **33% más rápida**, tarea **20% más rápida** **y** calificaciones más
positivas. Es decir: el rediseño mejoró **fluidez y estética a la vez**.

No es el experimento que H7 pide (aislar las dos variables), pero es informativo de otro modo:
sugiere que en sistemas de diseño maduros **fluidez y atractivo no suelen ser un trade-off**. La
formulación "fluidez *contra* ornamento" describe bien un caso de falla conocido (Liquid Glass,
F-272, donde el ornamento se comió el contraste) y mal el caso general. **C12 no se toca** —la
evidencia de que buena parte del "efecto estética" es fluidez de procesamiento sigue firme (F-249)—
pero **H7 necesita reformularse antes de seguir buscándola**: la pregunta útil no es *¿cuál gana?*
sino *¿en qué condiciones se sacrifica una por la otra?*

### 11.5 📱 La auditoría hispanohablante: H20 al 100%, y algo peor que el sesgo del emisor

La iteración 2 dejó H20 como su hipótesis más prometedora: *la conducta es local, el marco es
importado*, con la predicción de que **>70%** de las cifras citadas en piezas hispanohablantes de
tendencias 2026 vendrían de emisores anglosajones con interés comercial.

**Auditoría de ~20 piezas en español y portugués. Resultado: 13/13 cifras con atribución (100%)
provienen de emisores anglosajones con interés comercial directo** — Gartner, Forrester, Baymard,
Google, Designer Fund, Adobe, Canva, Pinterest. **Cero** piezas citaron un estudio, encuesta o dato
con muestra propia en español o portugués. **H20 pasa a `respaldada`, con la predicción superada.**

| Cifra citada | Emisor atribuido | Interés comercial | Nota |
|---|---|---|---|
| "+60% de tareas de diseño con IA para 2026" | Gartner | vende investigación | ⚠️ **no rastreable** (F-418) |
| "+80% de productos con IA generativa en la capa de interfaz" | Gartner | ídem | ⚠️ **no rastreable** |
| "68% de empresas con design systems asistidos por IA" | Gartner | ídem | ⚠️ **no rastreable** |
| "$1 en UX devuelve $100" | Forrester | reporte tras paywall | ya desmontada en iter. 1 (F-268) |
| "~70% de abandono de carrito por usabilidad" | Baymard | vende informes por suscripción | — |
| Adopción de IA 54% (2025) → 91% (2026) | Designer Fund (VC) | tesis de inversión | F-410 |
| Claude 78% vs. ChatGPT 65% entre diseñadores | Designer Fund | ídem | F-410 |
| "Cansancio de la perfección IA" como tendencia | Pinterest, Canva, Adobe | venden generación con IA | F-411 |
| "+30% de búsquedas de texturas realistas" | Canva | sobre su propia base | no auditable |

⭐ **Y el hallazgo que no estaba en la hipótesis: tres de esas cifras se atribuyen a un Gartner que
nunca las publicó.** La búsqueda del reporte primario (F-418) encontró predicciones reales de
Gartner con "60%", pero sobre **temas distintos** (abandono de proyectos de IA, equipos de
ingeniería más pequeños, adopción de agentes) — **ninguna sobre tareas de diseño**. Esto es un fallo
de un orden peor que el sesgo del emisor: contra el emisor interesado sirve descontar (C4); contra
la **autoridad prestada** descontar no alcanza, porque no hay nada que descontar. De ahí salen
**C19** y **H23**.

⚠️ **Matiz honesto que corrige el titular hacia abajo.** De las ~20 piezas, **solo 5 anclan sus
afirmaciones a alguna cifra con fuente nombrada**. Las otras **15 (75%) no citan absolutamente
nada** — ni bueno ni malo: afirman tendencias ("el minimalismo sigue ganando fuerza", "la tipografía
audaz rompe normas") sin ningún aparato de evidencia. **El problema del corpus regional no es solo
importar el marco: es que tres cuartas partes no fingen siquiera tener una fuente.** De ahí sale
**H25**, que probablemente determina más el nivel de la conversación regional que H20 misma.

### 11.6 📱 El eje se normaliza — y el caso testigo se disputa

**Lo que cambió en el eje dominante.** La iteración 2 encontró el gremio en modo ansioso-defensivo.
La iteración 3 encuentra el mismo eje 🔥 pero con dos movimientos:

1. **Normalización institucional.** Figma Config 2026 (23-25 jun, +8.000 asistentes) integró la IA
   como *default*, no como amenaza: **Figma Make** (con Claude), **Figma Motion**, 20+ herramientas
   de imagen (F-412). El registro pasó de *"¿nos va a reemplazar?"* a *"así se trabaja ahora"*. Es
   un eje nuevo en la tabla de §3.
2. **Anticuerpo del propio ciclo.** El discurso "el diseño ha muerto" sigue caliente, pero **ya
   genera su propia refutación desde adentro**: múltiples piezas de 2026 lo llaman "el truco de
   engagement más viejo del mundo" y documentan que se repite cada pocos años (F-415). La
   iteración 1 estableció que el ciclo es **estacional** (C5); la iteración 3 muestra que **la
   comunidad lo nombra activamente como manipulación retórica**, no solo que se repita.

**Y la corrección adversarial más importante de la pista social: MercadoLibre desmintió.** La
iteración 2 usó los 119 despidos de UX como **el ejemplo más limpio de C6** ("contar conducta, no
volumen") para refutar H17. La búsqueda adversarial de esta iteración encontró el desmentido
oficial: la empresa declara que fue una "**reorganización interna para integrar Diseño y
Contenido**" y que representó "**menos del 0,09% de su plantilla** de más de 125.000 empleados"
(F-419); ex-empleados sostienen que parte de su trabajo era entrenar los sistemas que los
reemplazaron.

⭐ **El despido es un hecho; la causa está en disputa — y era la causa la que hacía el argumento.**
Es el mismo patrón de *scapegoating* que Gallup documentó en el mercado anglosajón (F-282), ahora en
español y en la dirección opuesta: allá las empresas **atribuían** despidos a la IA para justificarse,
aquí la empresa **niega** la atribución para no cargar con el costo reputacional. En ambos casos la
declaración corporativa está interesada. De ahí sale **C21**.

**La refutación de H17 se sostiene igual**, pero sobre otras patas: el estudio brasileño con muestra
propia (F-389, N=823) y ahora también **Livspace en India** (~1.000 despidos, ~12% de la plantilla,
funciones de diseño incluidas — F-416), que amplía el patrón de compresión del rol a un tercer
mercado emergente. ⚠️ Con una ironía que refuerza H20: **la conducta es india, la cobertura es solo
en inglés.**

### 11.7 📱 Seniority, y el negocio de los dos bandos

**H10 pasa a `parcial`** con la primera evidencia segmentada por seniority en tres iteraciones. No es
cuantitativa, pero viene de una plataforma con **verificación de identidad corporativa** (Blind,
F-414), lo que la hace más creíble que un hilo anónimo: seniors describen el mercado como *"pésimo
si eres junior o recién graduado; si eres senior o superior, no es ideal pero está cerca de lo
normal"*. Consistente con F-280/F-301, ahora con testimonio por nivel en vez de encuesta agregada.
Sigue sin existir la encuesta segmentada por años de experiencia **con N reportado**.

**H11 pasa a `parcial`, y se amplía.** Auditoría de n≈8 piezas del ciclo "UX is dead": **~60-70%
tiene incentivo comercial identificable** en el formato o el publisher — bootcamp, Substack de pago,
YouTube monetizado, agencia de contenido (F-415). Proporción aproximada sobre muestra de
conveniencia, declarada como tal.

⭐ **Lo que no estaba en la hipótesis: el discurso que *corrige* el pánico también tiene modelo de
negocio.** Varias de las piezas que dicen "dejen de decir que el diseño murió" son ellas mismas
newsletters o bootcamps que necesitan tráfico. **El descuento por incentivo (C4) aplica a los dos
bandos, no solo al alarmista** — y eso significa que el volumen del debate identitario, en cualquier
dirección, es una medida pobre del estado real del oficio.

**H9 sigue `abierta`.** No apareció medición nueva específica de diseñadores. Sí un patrón análogo en
población general española que refuerza el mecanismo: **49% rechaza o expresa preocupación** por la
IA a inicios de 2026 mientras **82% ya la usa** para trabajar mejor (F-417). Es analogía de refuerzo,
no confirmación: mide otra población.

**H21 sigue `abierta`, y por tercera vez en blanco.** No existe (o no es alcanzable) un estudio
peruano ni hispanoamericano con muestra propia sobre *shadow AI* en diseño/producto. Lo más cercano:
EY reporta que 70% de grandes empresas peruanas subirá presupuesto de IA (n=250 directivos) — pero
eso mide **adopción organizacional, no uso sin lineamiento**. ⭐ **Recomendación operativa: dejar de
barrer genéricamente.** Tres iteraciones con términos distintos y cero resultados no distinguen "no
existe" de "existe tras un muro que el proxy no cruza". Para moverla hace falta una fuente primaria
distinta: contacto con una asociación de diseño peruana, o que el propio proyecto corra la medición
interna. **Sigue siendo la hipótesis más accionable para el contexto Rimac** — un negocio asegurador
donde el dato del cliente es sensible por definición no puede tener 60% de uso de IA en cuentas
personales sin saberlo.

### 11.8 📈 Figma en la víspera: H13 llega a su fecha con la condición más limpia que ha tenido

**H13 se resuelve el 5 de agosto de 2026** — tres días después de esta corrida. Estado al corte:

| Dato | Valor | Corte |
|---|---|---|
| Precio de cierre FIG | **US$24,30** (bajo el IPO de $33) | 31-jul-2026 (viernes) |
| Precio objetivo promedio | **~$40 (mar) → $31-33 (fin de jul)** ⚠️ dispersión real entre compiladores ($30,56 / $32,67 / $36,11) | jul-2026 |
| Recomendaciones | **Primera venta** entre 16 casas (antes 0 ventas) | 19-jul-2026 |
| Guidance oficial Q2'26 | **$348-350M, ~40% YoY** | dado en el call de Q1 |
| Paid customers Q1'26 | ~690.000, **+54% YoY** | 31-mar-2026 |

⭐ **Con el guidance oficial en la mano la prueba queda perfectamente limpia**: *si el reporte del
5-ago cumple o supera $348-350M (~40% de crecimiento) y la acción aun así no recupera sobre US$33,
el mercado descuenta disrupción por IA, no ejecución.* La iteración 4 debe leerlo y cerrarla — es la
única hipótesis del tablero con fecha de vencimiento, y ya venció.

**Señal nueva y más fuerte que en la iteración 2**: la aparición de la primera recomendación de venta
y la caída sostenida del precio objetivo indican que el consenso se está moviendo de "comprar con
cautela" a un reparto más poblado de *holds*. Movimiento en ambas direcciones: BofA reinstauró Buy
$30 (tesis: "la IA es más *tailwind* que *headwind*"), **RBC cortó a $22** tras Config 2026
cuestionando el margen operativo no-GAAP guiado de solo **~9% por gasto en cómputo de IA** — es
decir, el escepticismo ya no es solo sobre la demanda, es sobre **la economía unitaria de responder
con IA** (F-421).

⭐ **Y el evento corporativo que le da cuerpo al descuento**: el CPO de Anthropic **renunció a la
junta de Figma el 16-abr-2026**, el mismo día en que trascendió que el siguiente modelo incluiría
herramientas de diseño competidoras; al día siguiente se lanzó **Claude Design**, con **+1M de
usuarios en su primera semana** (F-429). La caída de 6-7,7% que el node ya tenía registrada (F-318)
tiene detrás un hecho fechado y divulgado a la SEC, no solo un sentimiento de mercado.

**H16 sigue `parcial`, sin movimiento nuevo en Figma**: el Q1'26 reportó NDR (139%) y todos los
tramos de paid customers. Pero la tendencia gana un tercer caso fuera de Figma: **Accenture no
reporta Song como segmento SEC** (F-428), lo que vuelve "¿Song crece?" **estructuralmente no
respondible con datos públicos** — el mismo mecanismo que la fusión de segmentos de Adobe. Y Webflow
sumó un **segundo layoff (~20% de la plantilla, may-2026)** sin publicar ARR desde 2023.

### 11.9 📈 El ROI del diseño no rota: acumula. Y H15 recibe su primer contraejemplo

**H22 predecía que esta iteración encontraría una cifra nueva ocupando el lugar del "ROI del
diseño". No la encontró — y lo que encontró es peor.** Las cinco cifras ya desmontadas **siguen
todas vivas, circulando en paralelo**, cada una en su nicho de contenido, sin corrección alguna:

- **"$1 → $100" de Forrester (2016, tras paywall)**: descrito textualmente en 2026 como **"el
  benchmark estándar para justificar presupuestos de diseño"** (F-423).
- **Nueva capa de conflación**: el "83% de aumento de conversión por 10% de inversión en UX"
  atribuido a Nielsen y el "$1 ahorra $10 en desarrollo y $100 en mantenimiento" atribuido a
  Clare-Marie Karat — **ambas de origen anterior al año 2000**, recirculando sin fecha en contenido
  de 2026 (F-424). **Confirma la sospecha de la iteración 1**: el "100x de UX" conflaciona una regla
  de ingeniería de software con un ROI de inversión en diseño.
- **McKinsey +32/+56 pp (2018)**: sigue siendo la cifra, y en al menos un caso aparece **mal fechada
  como "McKinsey 2026"** — la cadena de eco no se corrige, **empeora en precisión**.
- **DMI Design Value Index**: circulan **228% y 211% mezclados como si fueran el mismo estudio**
  (son ediciones distintas, 2013 y 2016); **no existe edición posterior a 2016**. Diez años citando
  un índice que dejó de publicarse.
- **135% de design systems**: la calculadora de 2022 (F-397) sigue siendo la cifra que un vendor usa
  para "medir el ROI de un design system en 2026" (F-425).

⭐ **Ningún divulgador retiró ninguna cifra tras el cuestionamiento.** Eso reformula H22 y corrige
**C17**: la hipótesis de la *rotación* era demasiado generosa con el campo — suponía que responde a
la refutación cambiando de argumento. **No responde en absoluto: acumula.** (Nota metodológica
honesta: la rotación 671%→135% fue un evento de *años*; cuatro días entre corridas no dan margen
temporal para observar una nueva. La reformulación propone medir **semestre a semestre**.)

**H15 pasa a `parcial` con su primer contraejemplo en tres iteraciones**: **R/GA reporta +30% H2'25
vs. H1'25 y +25% YoY en Q1 2026** (F-422) — el único crecimiento de doble dígito hallado en el
universo de consultoras/agencias de diseño desde que existe el node. ⚠️ Con tres descuentos que lo
dejan **dentro de la cláusula de escape que la propia hipótesis preveía**: es autorreportado (empresa
privada, sin filing auditable), R/GA **nunca fue consultora de diseño puro** (agencia
digital/publicitaria con práctica de diseño), y la propia nota enmarca el giro como **pivote a IA y
consolidación**, no como recuperación del modelo. La predicción central sigue sin refutarse: **tras
tres iteraciones no ha aparecido ninguna consultora de diseño pura con crecimiento auditado**.

**H14 sigue `abierta`, con la evidencia adversarial más fuerte de la corrida.** La ronda de Lovable a
$13,2B **seguía sin cerrar** al 2-ago-2026 (F-426); el ARR autorreportado subió de ~$400M a ~$500M
con 146 empleados. Pero lo más informativo es una **conducta, no una cifra**: preguntada de forma
directa, **Lovable se negó a compartir su tasa de churn y su split mensual/anual** (F-427). No es que
el dato no exista — la empresa decidió no publicarlo. Barclays estima **tráfico −40% desde el pico** y
una valuación implícita de **$1,8B**, entre 3x y 7x por debajo de la narrativa de ronda. La compañía
sostiene NDR >100%, y un analista independiente señala la falla que el node ya anticipó: **NDR >100%
es compatible con churn masivo si los que quedan gastan mucho más.**

### 11.10 Limitaciones de la iteración 3

- ⚠️ **Tercera iteración consecutiva sin leer un solo texto completo.** El proxy devolvió **403 en
  todos los intentos** de lectura directa, en las tres pistas: arXiv, ACM DL, ScienceDirect,
  gartner.com, sec.gov, x.com, reddit.com y la mayoría de los sitios hispanohablantes auditados.
  Todo el §11 está construido sobre **abstracts y snippets de búsqueda**. ⭐ **Conclusión operativa
  que la iteración 4 debe asumir: esto es estructural del entorno, no mala suerte.** Deja de tener
  sentido declararlo como limitación cada corrida; hay que **diseñar el barrido asumiéndolo** —
  priorizar hallazgos negativos y rastreos de cadena de cita (que sí funcionan con snippets) sobre
  verificaciones de método que exigen el PDF.
- **Autoría no verificada** en F-399, F-400 y F-404 (DZone no declara autor). Las cifras de F-420,
  F-421 y F-428 se recuperaron **indirectamente vía prensa financiera**, no leyendo el filing:
  **revalidar contra EDGAR antes de publicarlas en un entregable**, igual que en las iteraciones 1
  y 2.
- **No se confirmó contra el programa oficial** que SBES 2026 haya aceptado y publicado el estudio de
  design systems (F-259): la evidencia es un resumen de búsqueda, no el *proceedings*.
- **Muestra de conveniencia en las dos auditorías clave**: H20 (N≈20 piezas, 13 cifras) y H11 (n≈8
  amplificadores) se recogieron por búsqueda, no por muestreo sistemático. El 100% y el ~60-70% son
  válidos **para el corpus auditado**, no generalizables sin sesgo de qué indexa el buscador.
- **No se pudo cerrar el rastreo de la cifra 4,3/1,2 min hasta el fondo absoluto**: sin leer el PDF
  de F-388 y el de DZone en texto completo, no se puede descartar que ambos compartan una fuente
  común más arriba en la cadena. Se reporta el límite alcanzable, no se cierra la pregunta — pero el
  límite alcanzable ya es suficiente para no usar la cifra.
- **H21 sigue sin resolverse por ausencia, no por negación** — tercera vez.
- **La pista social sigue midiéndose por frecuencia y no por validación**: sin acceso a X ni Reddit
  no se pudieron contar reacciones. La compensación deliberada de esta iteración fue apoyarse en
  **conducta observable** (Config 2026, despidos de Livspace, la negativa de Lovable a publicar
  churn) y en **plataformas con identidad verificada** (Blind) en vez de en volumen.

---

## Conexiones

- [[behavioral-design-estado-disciplina|Behavioral design: estado de la disciplina y del mercado]] —
  node hermano y precedente metodológico directo: allí la crisis del nudge por sesgo de publicación,
  aquí la crisis del ROI del diseño por eco de cita. **El mismo patrón en dos disciplinas vecinas:
  una industria que sobrevendió su efecto promedio y ahora se defiende mejor por mecanismo que por
  multiplicador.**
- [[material-visual-venta-consultiva|Material visual en la venta consultiva]] — la regla C12
  (fluidez > ornamento) y la hipótesis H7 son directamente aplicables a los flyers y ayudas visuales
  de ese node; y su evidencia sobre *choice overload* e *icon arrays* es el caso aplicado de lo que
  aquí se sostiene en general.
- [[evaluacion-calidad-agentes-conversacionales-ia|Evaluación de calidad de agentes conversacionales
  de IA]] — las reglas C8 y C11 (verificabilidad > explicabilidad; desconfiar del autorreporte) son
  criterios de diseño que ese node debería incorporar a su instrumentación de medición.
  ⬆️ *Iteración 2*: **C15 es la advertencia más directa para ese node** — la evidencia de generative
  UI muestra que un artefacto de IA puede ganar en **preferencia declarada** mientras falla en
  prevención de errores, recuperación y ayuda (F-382). Cualquier instrumento que mida satisfacción
  de un agente conversacional **sin medir recuperación de error mide la mitad optimista del
  fenómeno**.
- [[seguros-comportamiento-mundo-peru|Comportamiento, percepción y valoración frente a seguros
  (Mundo vs. Perú)]] — H8 conecta los dark patterns con la causa #1 de desconfianza en seguros en
  Perú (falta de información), que es un hallazgo central de ese node.
- [[modelo-personas-sinteticas|Modelo de personas sintéticas (lapuerta)]] — H9 (brecha
  actitud-conducta en diseñadores) es estructuralmente el mismo fenómeno que la variable
  `disposicion_compartir_datos_pricing` del modelo: desconfianza abstracta declarada ≠ conducta real.
- [[proyecto-back-to-basics-ffvv-vida|Proyecto Back to Basics — FFVV Vida Individual]] — C1 y C2
  (argumentar por mecanismo, prometer acumulación) aplican a cómo se sustenta el valor del rediseño
  de la experiencia de venta ante el VP.
  ⬆️ *Iteración 2*: **C16 cambia cómo debería diseñarse el Plan Piloto de validación**. Si el
  impuesto de verificación es real (F-388), un piloto que promedie perfiles y niveles de madurez
  medirá cero; hay que **segmentar por seniority del asesor y por madurez del proceso** que se
  interviene. Y **existe una comunidad de service design en Lima desde 2017** (F-394) — interlocutor
  local para el frente de Service Design del proyecto, no hay que construirlo de cero.
  ⚠️ *Iteración 3 — corrección que ese proyecto debe recoger*: **la recomendación de segmentar el
  piloto sigue en pie; las cifras con que se justificaba, no.** El "4,3 min vs. 1,2 min" no tiene
  fuente rastreable (F-404) y la relación con la seniority resultó no monótona (F-407). Si el Plan
  Piloto cita esa cifra en un documento para el VP, **es vulnerable en la sala** — exactamente el
  riesgo que C1 describe. Segmentar sí; prometer la magnitud, no.

⬆️ **Conexiones nuevas de la iteración 3:**

- [[behavioral-design-estado-disciplina|Behavioral design: estado de la disciplina y del mercado]] —
  **C20 es transferible directamente a ese node**. Allí la crisis del nudge se documentó como sesgo
  de publicación *ajeno*; aquí este node descubrió que había adoptado sin rastrear un mecanismo
  propio porque le cerraba una contradicción. **La pregunta que C20 obliga a hacerle a cualquier
  node del proyecto: ¿cuál es mi hallazgo más satisfactorio, y lo verifiqué con el mismo rigor con
  que desmonté los ajenos?**
- [[evaluacion-calidad-agentes-conversacionales-ia|Evaluación de calidad de agentes conversacionales
  de IA]] — **H26 es una advertencia de instrumentación para ese node**. Si el escrutinio humano
  sobre salidas de IA **decae con la exposición acumulada** (F-407: +14,5 pp de aprobación a través
  de deciles de exposición), entonces cualquier esquema de evaluación con revisores humanos
  recurrentes **se degrada con el tiempo por construcción**, y una caída en la tasa de defectos
  detectados puede significar "el modelo mejoró" o "el revisor se acostumbró" — dos cosas opuestas
  que el instrumento no distingue si no rota revisores o no siembra casos de control.
- [[modelo-personas-sinteticas|Modelo de personas sintéticas (lapuerta)]] — **C19 (autoridad
  prestada) es un criterio de admisión para la calibración del modelo.** El generador se parametriza
  con cifras de terceros; la iteración 3 muestra que en el corpus de tendencias el **100%** de las
  cifras atribuidas venía de emisores interesados y que **tres de ellas se atribuían a una
  institución que nunca las publicó**. Antes de que una cifra externa entre al esquema, verificar
  que **el emisor citado la haya publicado**, no solo que la cifra suene plausible.
