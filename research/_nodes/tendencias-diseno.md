# Tendencias en diseño: qué tiene impacto real y qué es propuesta

> Documento de investigación **acumulativo**. Fuente persistente y versionada en el repositorio.
> Fecha de elaboración: 2026-07-26 · Última actualización: 2026-07-29 · Versión: v2.0 (iteración 2)
> Origen: `/trinidad` — investigación de 360° (empírica + social + negocio)
> Pregunta permanente: **¿qué tendencias de diseño tienen impacto tangible demostrado y
> cuáles son propuestas innovadoras todavía sin respaldo?**
> Fuentes registradas en `research/fuentes/codice.md` (F-237 a F-328 · iteración 2: F-380 a F-398).
>
> **Lo último (iteración 2, 2026-07-29):** cuatro hipótesis se movieron. **H17 refutada**
> (el ciclo identitario del gremio *no* llega desfasado a LatAm: MercadoLibre despidió 119
> personas de UX integrando diseño y contenido con IA, y Brasil adopta IA **más** que el
> mundo anglosajón, 94% vs. 89%). **H3 y H18 pasan a `parcial`**. **H6 gana una quinta
> cadena de eco de cita** (el "135% de ROI" de design systems es una calculadora, no un
> estudio). Y apareció el **mecanismo que reconcilia** la divergencia ⚔️ de productividad
> con IA: el *impuesto de verificación*. Ver §10.

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
  sostener el pánico.
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
  trabajo está en conflicto directo (METR: −19% de productividad con IA en devs expertos; preprint
  de design-system-aware AI: −46% a −69% de time-to-delivery). Ver §6/H5.

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

### 2.5 Chequeo de eco de cita — tres cadenas que colapsan en una sola fuente

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
   ⭐ *Patrón que ya es regla:* cada vez que una cifra estrella del ROI del diseño se desmonta,
   **la industria no deja de citar cifras: cambia de cifra.** 671% → 135%. La cadena de eco no es un
   accidente de una fuente, es la forma en que este mercado produce su evidencia.

*Nota simétrica de honestidad: el dato de Kohavi también se repite mucho y proviene esencialmente de
una organización (Microsoft ExP), aunque las cifras análogas de Google/Bing/Netflix/Airbnb vienen de
reportes separados.*

---

## 3. 📱 Pista social/mediática (gossiper)

**Nivel general:** 🔥 muy alta y sostenida en el eje **IA × identidad profesional del diseñador**.
Casi todo lo demás (estética, herramientas, design systems) se discute como subtrama de ese eje.

| Tendencia | Instalación | Tono dominante |
|---|---|---|
| Ansiedad IA / empleo / "el fin del UX designer" | 🔥 | Ansioso-defensivo, con contraataque activo |
| "AI slop" / *sameness* estética | 🔥 | Indignado, con movimiento organizado (Slopless) |
| Liquid Glass de Apple | 🌡️ (fue 🔥) | Ya resuelto, tono de "ganamos" |
| Confusión del rol / "nadie sabe qué es un diseñador" | 🌡️ | Exasperado, muy validado por experiencia propia |
| Anti-design / neo-brutalismo / lo-fi | 🌡️ | Entusiasta, pero **empujado por vendors** |
| Design systems como gobernanza de IA | 🌡️ | Técnico, pragmático, poco dramático |
| Vibe coding para diseñadores | 🌡️ | Ambivalente: FOMO + escepticismo |
| Retorno táctil/analógico (riso, zines, print) | 💬 | Cálido, sin conflicto — **pero con conducta real** |
| Service design | 🧊 | Prácticamente ausente |

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
| **La IA acelera el trabajo de diseño/producto** | ⚔️ **Evidencia en conflicto directo** | F-257 vs. F-259 |
| **La IA está causando el desempleo de diseñadores** | ⚔️ Atribución declarada ≠ causalidad | F-282 vs. F-283 |

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
| **H3** | En tarea repetida a lo largo de ≥5 sesiones, la **generative UI** dará **peor** tiempo de tarea y **peor** aprendibilidad que una UI estática equivalente, aunque gane en preferencia declarada en la sesión 1 | ⬆️ **`parcial`** *(iter. 2)* — **la mitad de la predicción está confirmada y la otra mitad sigue sin medirse.** Confirmado: gana en preferencia de sesión única (hasta 72%, F-381; F-380). Confirmado indirectamente: falla justo en prevención de errores, eficiencia de uso, recuperación y ayuda (F-382), y **produce interfaces distintas ante el mismo prompt incluso en ejecuciones repetidas de la misma herramienta** (F-384) — la inconsistencia que destruiría la aprendibilidad ya está medida. Sigue abierto: **nadie ha corrido el estudio longitudinal** | Estudio longitudinal independiente entre-sujetos. ⚠️ Tras 2 iteraciones **sigue sin existir** — y esa ausencia, buscándola, ya es un hallazgo (C7) |
| **H4** | Añadir explicación ("¿por qué veo esto?") **no** mejora precisión ni calibración en decisiones de **baja** dificultad; **sí** en alta | `parcial` — respaldada por F-246 en laboratorio, sin replicar en dominio aplicado | RCT con dificultad manipulada en recomendación de producto financiero/seguros |
| **H5** | En cualquier estudio que mida **a la vez** desempeño objetivo y percibido, la mejora subjetiva **excederá** a la objetiva en ≥20 pp | `abierta` — **la hipótesis de mayor valor destructivo**: si se sostiene, invalida casi todo reporte de industria sobre design systems, IA y madurez de diseño | Meta-análisis de estudios que reporten ambas medidas |
| **H6** | El efecto de un design system sobre el tiempo de desarrollo será **<20%** (no 47%, no 69%) con contrabalanceo de orden, N≥40 y devs externos a la organización que mantiene el sistema | `abierta` — **se buscó replicación independiente en la iter. 2 y no existe**; lo que sí apareció es una quinta cadena de eco (135% modelado, F-397) y evidencia de que **solo ~40% de los sistemas sigue activo pasados 18 meses** (F-396). El campo produce calculadoras de ROI, no experimentos | Replicación independiente de Sparkbox con diseño corregido |
| **H7** | En un A/B real, las variantes que aumentan **fluidez** (contraste, jerarquía, menos elementos) superarán a las que aumentan atractivo estético sin aumentar fluidez | `abierta` — **aplicable directamente al contexto Rimac/seguros** | Experimento de campo |
| **H8** | En Perú, donde la causa #1 de desconfianza en seguros es la falta de información, la exposición a patterns de *hidden information* predecirá desconfianza en aseguradoras **con más fuerza que las variables demográficas** | `abierta` — **el puente más directo con el resto del proyecto** | Experimento sobre muestra peruana replicando Luguri & Strahilevitz |
| **H9** | **Brecha actitud-conducta en diseñadores**: el discurso público es anti-IA/anti-slop pero la adopción declarada es altísima (89% trabaja más rápido) | `abierta` — **estructuralmente el mismo fenómeno que `disposicion_compartir_datos_pricing` en `lapuerta`** | Medir si la indignación estética predice o no comportamiento de uso |
| **H10** | La ansiedad gremial es un fenómeno de **seniority**, no de gremio: el daño está concentrado en juniors pero se enuncia en nombre de "los diseñadores" | `abierta` — no se pudo segmentar por seniority | Datos de empleo o encuesta segmentada por años de experiencia |
| **H11** | **El doom tiene modelo de negocio**: la proporción de amplificadores del discurso "la IA mata al diseño" con incentivo comercial directo (cursos, bootcamps, portafolios) es alta; si lo es, el volumen social debe descontarse fuertemente | `abierta` — caso testigo identificado (F-286) | Auditar los N amplificadores principales y clasificar su modelo de ingresos |
| **H12** | El backlash estético es **señalización de estatus profesional**, no preferencia de usuario | `parcial` — respaldada por F-284 (gatekeeping) y F-297 (usabilidad) | Testear si la "autenticidad imperfecta" mejora alguna métrica de usuario |
| **H13** | **Desacople valuación/desempeño**: si Figma reporta ≥40% de crecimiento en Q2 2026 y la acción **no** recupera sobre $33, el mercado descuenta disrupción por IA, no ejecución | `abierta` — **falsable el 5-ago-2026** (fecha de reporte) y en los 90 días siguientes | Reporte Q2 2026 de Figma + evolución del precio |
| **H14** | **El ARR de vibe coding no retiene**: si Lovable cierra a $12-13,2B, su ARR a 12 meses crecerá <50% (vs. 150%+ histórico), revelando la cohorte de churn | `abierta` | Comparar ARR jul-2026 vs. jul-2027; se resuelve de inmediato si publican NRR |
| **H15** | **La consultora de diseño pura no vuelve**: ninguna de las cuatro publicará crecimiento de dos dígitos en 2026-2027; la recuperación, si ocurre, será como implementadoras de IA | `abierta` | Cualquier reporte de revenue o adquisición a múltiplo alto |
| **H16** | **El estándar de reporting se degrada donde hay presión de IA**: si Figma deja de reportar NDR o paid customers en algún trimestre 2026-2027, se refuerza | `parcial` — ya ocurrió con Adobe (fusión de segmentos) y Webflow (dejó de publicar ARR) | Trimestre a trimestre |
| **H17** | **Desfase geográfico**: el ciclo identitario del gremio llega a Perú/LatAm desfasado, atenuado, o el mercado local ni siquiera participa de esa conversación | ⬇️ **`refutada`** *(iter. 2)* — **no hay desfase.** Brasil adopta IA **por encima** del mundo anglosajón (94% vs. 89%, N=823 — F-389); MercadoLibre ejecutó la compresión del rol en LatAm con **119 desvinculaciones de UX** integrando diseño y contenido (F-391); el vocabulario anti-slop circula en español en medios masivos (F-390). El ciclo es **simultáneo**, no diferido | Refutada. Ver H20, que es lo que quedó vivo del barrido |
| **H18** | **El silencio del service design** es señal de madurez (absorbido en operaciones), no de irrelevancia | ⬆️ **`parcial`** *(iter. 2)* — **la mitad favorable**: existe base de evidencia institucional (revisión oficial del gobierno británico, F-387), infraestructura viva (SDN, conferencia global, Touchpoint — F-395) y **comunidad activa en Perú desde 2017** (F-394). **La mitad adversa**: una figura interna de la disciplina describe una "**crisis de la práctica**" por no haber sabido demostrar valor (F-393), y **no hay métricas públicas de membresía** para medirlo. *Silencio social ≠ irrelevancia — pero tampoco es prueba de madurez* | Métricas de membresía SDN, o presupuesto/plantilla de service design en organizaciones grandes |

### Hipótesis abiertas en la iteración 2

| # | Hipótesis | Estado | Cómo se falsa |
|---|---|---|---|
| **H19** | **El impuesto de verificación es la variable moderadora**: el efecto de la IA sobre la velocidad de entrega será **negativo en código base maduro y positivo en construcción nueva**, y el punto de cruce dependerá de la seniority, no de la calidad del modelo | `abierta` — mecanismo propuesto por un preprint (F-388); si se sostiene, **el debate "¿la IA acelera o no?" está mal planteado** y la pregunta correcta es *¿en qué punto de la curva estoy?* | Un experimento que manipule **madurez del código base** como factor y mida seniority como moderador. Se refuta si el efecto es del mismo signo en ambas condiciones |
| **H20** | **La conducta es local, el discurso es importado**: LatAm/España **generan evidencia y decisiones propias** (estudio brasileño N=823, despidos de UX en MercadoLibre) pero **consumen el marco interpretativo traducido del inglés** — se re-emite el 89% de Figma sin el descuento por interés del emisor que la propia fuente exige | `abierta` — **lo que quedó vivo tras refutar H17, y probablemente más útil que ella**. Predicción: >70% de las cifras citadas en piezas hispanohablantes de tendencias 2026 serán de emisores anglosajones con interés comercial | Auditar N piezas en español/portugués y clasificar el origen y el interés del emisor de cada cifra que citan |
| **H21** | **Brecha de gobernanza, no de adopción**: en mercados emergentes el problema real no es que los diseñadores no usen IA sino que la usan **sin marco corporativo** — 60% en cuentas personales, 14% con capacitación de la empresa (F-389). Si es así, la intervención de mayor retorno es **gobernanza, no capacitación en herramientas** | `abierta` — **directamente accionable en el contexto Rimac**; conecta con el riesgo de dato sensible del negocio asegurador | Replicar la medición de *shadow AI* en una organización peruana; se refuta si la adopción sin lineamientos es marginal |
| **H22** | **El ROI del diseño se cita por rotación, no por evidencia**: cuando una cifra estrella se desmonta públicamente, la industria **la sustituye por otra igual de trazable-a-una-fuente** en vez de dejar de citar cifras (671% → 135%) | `abierta` — patrón observado en 2 iteraciones consecutivas; predicción: **la iteración 3 encontrará una cifra nueva y distinta** ocupando el mismo lugar retórico | Registrar en cada iteración qué cifra ocupa el lugar de "el ROI del diseño". Se refuta si la cifra dominante se mantiene estable o si desaparece sin reemplazo |

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
  es sí ni no: es *¿en qué punto de la curva está este equipo?* Construcción nueva y perfiles junior
  ganan; código base maduro y perfiles senior pagan un **impuesto de verificación** que puede
  superar el ahorro. Un piloto que mida el promedio de ambos mundos medirá cero y concluirá mal.
  Diseñar el piloto **segmentando por madurez del sistema y por seniority**, no agregando.
- **C17 — Cuando desmontes una cifra estrella, prepárate para la siguiente.** Este campo no responde
  a la refutación dejando de citar cifras: **rota la cifra**. El 671% cayó y lo reemplazó el 135% —
  igual de modelado, igual de no medido. La defensa no es tumbar la cifra del día, es **exigir el
  diseño del estudio**: ¿alguien ejecutó el cambio y midió el resultado, o alguien estimó el ahorro?
  ⚠️ *Provisional: ascendida con una sola iteración de respaldo; se confirma o cae en la iteración 3
  (H22).*

**Sobre geografía y contexto local** *(ascendida en la iteración 2)*

- **C18 — En LatAm, la conducta es local y el marco es importado; usar el primero, descontar el
  segundo.** Se creyó que el ciclo identitario del gremio llegaría desfasado a la región y **no es
  así**: la adopción de IA en Brasil supera a la anglosajona y la compresión del rol de diseño ya se
  ejecutó en la empresa más valiosa de la región. Pero el *relato* que circula en español y
  portugués es traducción, y arrastra sin filtro las cifras de emisores interesados. Regla operativa
  para cualquier entregable regional: **buscar el dato de conducta local** (decisiones corporativas,
  estudios con muestra propia) y **no citar la cifra anglosajona sin su descuento por emisor** (C4).
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
  queja de LinkedIn**. La ironía es que la iteración 1 registró que el daño se concentraba en
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
