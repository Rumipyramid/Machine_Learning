# Tendencias en diseño: qué tiene impacto real y qué es propuesta

> Documento de investigación **acumulativo**. Fuente persistente y versionada en el repositorio.
> Fecha de elaboración: 2026-07-26 · Última actualización: 2026-07-27 · Versión: v1.1
> Origen: `/trinidad` — investigación de 360° (empírica + social + negocio)
> Pregunta permanente: **¿qué tendencias de diseño tienen impacto tangible demostrado y
> cuáles son propuestas innovadoras todavía sin respaldo?**
> Fuentes registradas en `research/fuentes/codice.md` (F-237 a F-328 · iteración 2: F-329 a F-391).
> Iteraciones: 2 (ver bitácora §8).

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
  de design-system-aware AI: −46% a −69% de time-to-delivery). Ver §6/H5. ⚠️ **La iteración 2
  desarmó esta divergencia: el preprint no medía design systems. Ver §1.bis.**

---

## 1.bis ⚠️ Correcciones a la iteración 1 (introducidas en la iteración 2)

**Este bloque es obligatorio y permanente.** Un node acumulativo que solo agrega y nunca se corrige
deja de ser memoria y se vuelve sedimento. Cada iteración que encuentre un error de la anterior lo
escribe aquí, con nombre y apellido.

- 🔴 **CORRECCIÓN 1 — El preprint de "design-system-aware AI" no medía design systems.** La
  iteración 1 registró su −46,7% a −69,4% de *time-to-delivery* como evidencia sobre design systems
  y lo puso en conflicto directo con el RCT de METR. **Es un error de atribución de brazo
  experimental.** El estudio (arXiv:2607.13156, Zup Innovation, 49 devs, entre-sujetos) tiene *tres*
  brazos —Manual (n=7) · Design System (n=21) · IA asistida contextualizada con el DS (n=21)— y
  **la reducción reportada corresponde al brazo de IA, no al brazo design-system-solo** (F-335). El
  contraste que resolvería H6 —Design-System vs. Manual— **no se pudo obtener**. Consecuencias: (a)
  la divergencia ⚔️ "la IA acelera o frena" **deja de sostenerse por esta vía** — METR midió devs
  expertos en repos maduros que conocían a fondo, Zup midió construcción de componentes nuevos con
  un baseline de 7 personas; no son comparables y ninguno refuta al otro; (b) el "efecto design
  systems" pierde su única fuente aparentemente moderna.
- 🔴 **CORRECCIÓN 2 — "IDEO −67% de revenue" no es un dato documentado.** La iteración 1 lo listó
  entre las cuatro señales convergentes de la crisis de las consultoras. La cifra (US$300M → US$100M)
  proviene de **un ex-empleado no identificado**, citado por prensa en **octubre de 2023**; IDEO es
  privada y **no presenta filings**. Rigurosidad real: **🔴 D/E, no B** (F-388). Lleva ~2,75 años
  reciclándose sin verificación — el mismo patrón de eco de cita que este node persigue en otros,
  aparecido dentro del propio node. **Lo que sí está documentado de IDEO** es el recorte del **32% de
  la plantilla** (oct-2023, confirmado por la empresa) y el cierre de las oficinas de Múnich y Tokio.
  La tesis de la crisis **sobrevive** apoyada en las otras señales, pero con un eslabón menos y
  reformulada (ver §6/H15).
- 🟡 **CORRECCIÓN 3 — "Veryday cerrada" es impreciso.** Veryday fue **adquirida por McKinsey en 2016**
  y absorbida en McKinsey Design. Consistente con la tesis de absorción, no con quiebra. La palabra
  "cerrada" sobrestimaba la señal.
- 🟡 **PRECISIÓN 4 — Posible doble registro de una misma encuesta.** La iteración 1 registró como
  F-280 una encuesta de Figma/NewtonX con **n=906** diseñadores. La iteración 2 encontró la misma
  cifra de N atribuida a otro emisor ("Designer Fund, *AI in Design 2026*", 906 diseñadores, 60+
  países). **Puede ser la misma encuesta circulando con dos atribuciones, o dos encuestas distintas
  con N idéntico por coincidencia.** No se resolvió. Hasta que se resuelva, **no contar ambas como
  confirmaciones independientes** (F-362).

---

## 1.ter Resumen ejecutivo de la iteración 2

La corrida 2 fue a cerrar los cinco pendientes de la corrida 1 y volvió con un resultado mejor que
el buscado en tres de ellos, porque **la respuesta estaba en otra disciplina o en otro idioma**:

- 🔬 **H6 se resuelve, pero desde la ingeniería de software.** Un design system *es* software reuse
  con otro nombre, y esa literatura lleva **30 años de datos industriales sin poder establecer el
  efecto de productividad** (3 de 11 estudios, y solo en una métrica inflada por construcción),
  mientras **sí** establece consistentemente el efecto de **calidad y densidad de defectos**.
- 📱 **H17 no era "desfase", era desplazamiento de eje.** El mismo shock tecnológico produce **crisis
  de identidad** donde el gremio está desagremiado (anglosajón) y **acción colectiva regulatoria**
  donde hay federaciones y sindicatos vivos (España, Argentina) o tradición de análisis de clase
  (Brasil). Es un hallazgo más fuerte que el retraso temporal, que también existe (~19 meses) pero
  es secundario.
- 📈 **H18 se responde con un tercer estado.** Ni madurez ni irrelevancia: el service design **nunca
  construyó su aparato de evaluación de outcomes**, y su caída *sí* está cuantificada mientras su
  supuesta absorción in-house solo está anecdotada.
- ⚖️ **La convergencia nueva de las tres pistas es sobre la inmedibilidad.** La empírica encuentra
  que la métrica dominante del sector sube por construcción; la social, que la frecuencia aparente
  en español está inflada por SEO educativo; la de negocio, que el diseño ya no es una línea
  contable separable en ningún lado (ni en contratos públicos, ni en informes de mercado LatAm, ni
  en el P&L de las consultoras absorbidas). **Tres formas independientes del mismo problema: el
  diseño se volvió estructuralmente difícil de contar, y la inmedibilidad no es lo mismo que la
  salud.**
- 🔴 **Y una advertencia sobre el propio node**: dos cifras que la iteración 1 dio por buenas eran
  eco de cita o atribución errónea (§1.bis). El node encontró en sí mismo el defecto que diagnostica
  en la industria. **Eso valida el mecanismo iterativo, no lo invalida** — pero obliga a tratar toda
  cifra de fuente única como provisional hasta que una iteración posterior la ataque.

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

*Nota simétrica de honestidad: el dato de Kohavi también se repite mucho y proviene esencialmente de
una organización (Microsoft ExP), aunque las cifras análogas de Google/Bing/Netflix/Airbnb vienen de
reportes separados.*

### 2.6 ⭐ Design systems = software reuse: la disciplina vecina ya lo midió y no lo encontró (iter. 2)

**El hallazgo más importante de la iteración 2 en esta pista.** La pregunta "¿un design system
acelera el desarrollo?" no es nueva ni propia del diseño: es **exactamente** la pregunta que la
ingeniería de software se hace desde los años 90 bajo el nombre de *software reuse* / *component-based
development*. Y esa literatura, con datos industriales reales y treinta años de acumulación,
**no logró establecer el efecto de productividad**:

- **La revisión canónica** (Mohagheghi & Conradi, 2007, *Empirical Software Engineering* — F-329,
  peer-reviewed, 11 estudios industriales 1994-2005): reuso sistemático → **menor densidad de
  defectos en 5 estudios** y menor esfuerzo de corrección en 3, pero **ganancias significativas de
  productividad en solo 3 de 11**.
- ⭐ **El artefacto métrico que lo explica todo — y que este node adopta como regla.** Esa misma
  revisión distingue **"apparent productivity"** (tamaño total del software ÷ esfuerzo total) de
  **"actual productivity"** (tamaño del código *nuevo* ÷ esfuerzo total). **Los 3 estudios con
  ganancias las reportan en la primera** — una métrica que **sube mecánicamente con el reuso por
  construcción**: cuenta el código reutilizado en el numerador sin cargar en el denominador el
  esfuerzo de haberlo creado. **Toda medición de design systems de la forma "componentes entregados ÷
  horas" está midiendo apparent productivity, y por tanto no puede falsar la hipótesis que dice
  demostrar.**
- **El estudio diseñado para medirlo obtuvo signos contradictorios** según qué métrica se usara
  (Frakes & Succi, 2001, *Journal of Systems and Software* — F-331).
- **La revisión sistemática reciente** (*Information and Software Technology*, 2024 — F-330;
  ⚠️ autoría no verificada, no se inventaron nombres): **87% de los estudios primarios es de calidad
  baja (20%) o moderada (67%)**; la síntesis del campo se hace por *vote-counting*, no meta-análisis;
  y documenta **costos** de productividad en reuso *verbatim* y ad hoc. Frase que retrata al campo:
  muchos desarrolladores que practican reuso **afirman beneficios sin demostrarlos formalmente**.
- **Contraevidencia buscada activamente y encontrada**: Basili, Briand & Melo (1996, *CACM* — F-332)
  sí halló mayor productividad — pero en 8 sistemas de <15 KSLOC, sin aleatorización, hace 30 años,
  con el mismo problema de operacionalización.

**Reevaluación del 47% de Sparkbox (F-333).** Se recuperó el diseño exacto y es **peor que "falta de
contrabalanceo"**: 8 desarrolladores construyeron el mismo formulario de contacto desde cero y
**después lo reconstruyeron con Carbon** (mediana 4,2 h → 2,0 h). Es **orden fijo con repetición de
la tarea idéntica**: el segundo build del mismo formulario es más rápido con cualquier herramienta,
por aprendizaje de la tarea y de los requisitos. El 47% **confunde efecto-herramienta con
efecto-repetición y no es separable con ese diseño**.

🔴 **Eco de cita nuevo, con agravante de autoridad falsa (F-334).** Blogs de 2025-2026 atribuyen **a
Nielsen Norman Group** que "organizaciones con design systems maduros reportan 47% de ciclos más
rápidos y 34% de reducción de deuda técnica de diseño", junto a "ROI anual de 300-600%". El 47%
**coincide exactamente con la cifra de Sparkbox (N=8)**, y una búsqueda restringida a `nngroup.com`
**no encuentra la cifra en ningún artículo de NN/g**. Es una fuente D adquiriendo el megáfono de una
autoridad que nunca la publicó. *(La no-aparición en búsqueda de dominio restringido es evidencia de
ausencia, no prueba definitiva.)*

⭐ **El vacío que es en sí mismo un dato.** Se buscaron explícitamente RCTs de bibliotecas de
componentes con devs y tiempo de tarea. Lo que devuelve ese espacio de búsqueda en 2024-2026 son
**RCTs de IA** (Google con 96 ingenieros y asignación aleatoria; GitHub Copilot; el propio preprint
de Zup): **el campo tiene ahora capacidad y voluntad metodológica de correr experimentos aleatorizados
sobre herramientas de desarrollo — y los está corriendo sobre IA, no sobre design systems.**

> **Conclusión operativa:** el argumento honesto de un design system es **consistencia y densidad de
> defectos** (5 estudios convergentes), **no velocidad**. Quien defienda un design system por
> velocidad está usando el único eje que treinta años de datos industriales no pudieron sostener.

### 2.7 Interfaces adaptativas: la variable que reorganiza H3 (iter. 2)

La literatura **no** dice "la adaptación automática degrada el desempeño". Dice algo más filoso, y
la distinción es la síntesis propia de esta iteración:

| Qué adapta el sistema | Estabilidad espacial | Resultado |
|---|---|---|
| Frecuencia de uso → **reubica ítems** (menús dinámicos/adaptativos) | ❌ rota | **Degrada.** Usuarios más lentos y 81% prefiere estático (F-340); o prefieren el adaptable pero **rinden peor con el adaptativo** (F-341) |
| Predicción → **guía la atención sin mover nada** (*ephemeral adaptation*, fade-in gradual) | ✅ preservada | **Mejora**: más rápido que estático con precisión alta, **sin costo** con precisión baja (F-344, N=48, CHI) |
| Rasgo **estable** del usuario (capacidad motora) → genera la UI una vez (SUPPLE / ability-based) | ✅ preservada tras generar | **26% más rápido y 73% más preciso** que las interfaces del fabricante (F-345) |

**El predictor del éxito no es "adaptar o no adaptar": es (a) si la adaptación destruye la
consistencia espacial y (b) si adapta a un rasgo estable o a una predicción móvil de intención.**

La generative UI de 2025-2026 está, por construcción, **en la peor celda**: regenera el layout
completo en cada turno, y una revisión sistemática documenta que **prompts idénticos producen UIs
sustancialmente distintas entre herramientas e incluso entre ejecuciones repetidas de la misma
herramienta** (F-338). La línea de trabajo que intenta corregir esto —generar UI que **cumpla** un
design system, vía *context engineering*— está apenas en abstracts extendidos de CHI 2026 (F-339): es
la intersección H3×H6 y todavía no tiene resultados de desempeño. Y su métrica de éxito declarada es
**preferencia en sesión única / preferencia
de raters** — hasta 72% de preferencia humana en un preprint (F-336), comparabilidad con expertos en
~50% de casos en otro (F-337) — exactamente la métrica que la literatura de menús adaptativos
demostró que **se disocia del desempeño**.

⚠️ **Honestidad sobre esta inferencia:** que los preprints no midan aprendibilidad longitudinal es
una inferencia sobre el **vocabulario de evaluación reportado**, no lectura del método: el proxy
bloqueó arXiv por segunda iteración consecutiva y **no se leyó ningún preprint de primera mano**.

### 2.8 ⭐ El patrón transversal: juicio subjetivo ≠ desempeño objetivo (iter. 2)

Lo que en la iteración 1 eran hallazgos sueltos, en la 2 se revela como **una familia coherente**, y
con una pieza nueva peer-reviewed que la cierra por el lado neurofisiológico:

- **METR (iter. 1)**: devs expertos **19% más lentos** con IA creyendo ser **20% más rápidos**.
- **Preßler et al. 2023 (iter. 1)**: la correlación estética-usabilidad **cae de r=0,79 a r=0,34** al
  controlar por fluidez de procesamiento.
- **Findlater & McGrenere 2004 (F-341)**: los usuarios **prefieren** el menú con el que rinden peor.
- ⭐ **Gaspar-Figueiredo et al., 2026, *Journal of Systems and Software* 231 (F-342)** — peer-reviewed,
  **usa EEG como medida objetiva de carga cognitiva** contra preferencia declarada: **los menús mejor
  puntuados en atracción registraron ALTA carga cognitiva**, y algunos usuarios prefieren interfaces
  que **no** mejoran su desempeño. *(Replicación interna del mismo grupo, N=40, en F-343 — no es
  replicación independiente.)*
- **Schlamann et al. 2026 (F-346)**: detecta que las condiciones estéticas definidas *a posteriori*
  están confundidas por la **usabilidad experimentada** — la misma familia de confusión que la fluidez.

> Esto asciende a **regla de criterio del node** (ver §7, C15).

### 2.9 Estética → desempeño objetivo: un meta-análisis nuevo, y por qué no cierra el caso (iter. 2)

⭐ **Schlamann, M., Nestler, S. & Thielsch, M. T. (2026), "Attractive Things Do Work Better: A
Meta-Analysis on Visual Aesthetics and User Performance", *International Journal of Human-Computer
Interaction* (F-346)** — 🟢 A: peer-reviewed, **preregistrado**, **31 estudios · 234 effect sizes ·
18.794 participantes**. Resultado: **efecto pequeño-a-medio de la estética sobre el desempeño
objetivo, g = 0,29**, con alta heterogeneidad no explicada; moderadores significativos: dispositivo
de interacción y manipulación tipográfica. "No hay evidencia de que el diseño atractivo perjudique
fundamentalmente el desempeño."

**Esto no contradice a Preßler: mide otro constructo.** El node debe separar de aquí en adelante:

| Constructo | Qué mide | Hallazgo |
|---|---|---|
| Estética → **usabilidad percibida** | juicio del usuario | Inflado; cae de r=0,79 a r=0,34 al controlar fluidez (iter. 1) |
| Estética → **desempeño objetivo** | velocidad, precisión, eficiencia | Efecto **real pero pequeño**: g=0,29 (F-346) |

⚔️ **Alerta que debe conservarse.** El mismo grupo publicó en 2019 un meta-análisis previo con
**g=0,12** (25 estudios, N=3.025 — F-347) en el que **los propios autores declararon posible sesgo de
publicación**. **El efecto se duplicó** al ampliar la base, y **Thielsch es autor senior de ambos**:
no son dos confirmaciones independientes, son **una línea de investigación**. El preregistro y el
N=18.794 pesan a favor; la no-independencia y la duplicación del estimador pesan en contra. **No se
pudo verificar si el paper de 2026 reporta análisis de sesgo de publicación** (Taylor & Francis y
Zenodo bloqueados) — **es el primer objetivo de la iteración 3.**

### 2.10 Diseño de servicios: el tercer estado (iter. 2, H18)

La respuesta a "¿madurez o irrelevancia?" es **ninguna de las dos**: el campo **produjo proceso y no
midió resultado**.

- ⭐ **Revisión sistemática de codiseño en multimorbilidad** (*BMC Medicine*, 2024 — F-348):
  **14.376 reportes cribados → 13 elegibles → solo 2 reportaron outcomes de salud y bienestar** (un
  ECA n=134 y una cohorte controlada n=1.933), y **solo 4 de 17 outcomes favorecieron a la
  intervención codiseñada** frente al control.
- **Overview de revisiones** (*Implementation Science*, 2024 — F-349): el codiseño *"appears to be
  ethically the right thing to do"* pero **"una evaluación rigurosa de su proceso e impacto falta
  frecuentemente"**. Que en 2024 el aporte de una revisión general sea **proponer un marco de
  evaluación** indica que el campo no tenía uno.
- **Lo que sí se absorbió en operaciones** es lo más formalizable y lo menos ligado a la identidad
  disciplinar del diseño: **service blueprinting** (con antecedentes validados: orientación al
  mercado, clima de servicio y formalidad del proceso) y la **service-dominant logic**. **Se fue el
  método, no la disciplina.**
- ⚔️ **Conflicto de incentivos a registrar:** que el campo declare el codiseño como *"lo éticamente
  correcto"* hace socialmente costoso publicar un nulo. Hay sospecha razonable de sesgo de
  publicación **y** de un incentivo a no medir. No se pudo testear (haría falta funnel plot).

### 2.11 ⭐ La tradición latinoamericana del diseño (iter. 2, H17 académica)

Existe, tiene linaje continuo y verificable, y **dice algo que la conversación anglosajona ignora** —
pero hay que ser preciso sobre qué tipo de cosa es.

**El hallazgo genealógico:** un artículo en *AI & Society* (Springer, 2022, número especial
*Cybernetics in Latin America* — F-350) sostiene que **Gui Bonsiepe formuló el concepto de *interfaz*
aplicado al diseño en la revista INTEC n.º 2, Santiago de Chile, 1972**, dirigiendo el Departamento
de Diseño Industrial del INTEC-CORFO bajo Allende e incorporando conceptos cibernéticos a las
disciplinas proyectuales. Su grupo **reconstruyó la opsroom del proyecto CYBERSYN** (1972-73). Si la
tesis es correcta, la genealogía estándar del concepto central del campo (Engelbart → Xerox PARC →
ACM SIGCHI) **tiene una rama latinoamericana, cibernética y socialista, que no se cita**.
⚠️ **Advertencia de eco de cita: la tesis la sostiene un artículo, en un número especial temático, y
su autor —a quien no se pudo identificar— parece estar detrás de los trabajos relacionados sobre
CYBERSYN. Puede ser una sola voz con varios altavoces. Se registra como tesis publicada en revista
arbitrada, pendiente de verificación independiente.**

**El cuerpo teórico:** Ulm → Maldonado → **Bonsiepe** (*Diseño Industrial: Tecnología y Dependencia*
1978, *Diseño de la Periferia* 1985, *Del Objeto a la Interfase* 1995 — F-351) → **colonialidad do
fazer** (Brasil — F-353) → **Escobar**, *Designs for the Pluriverse* / *Autonomía y diseño* (F-352).
Tesis compartida: **el diseño periférico no es diseño del centro con menos presupuesto, sino otra
práctica con otra función económica y otros criterios de éxito.**

⭐ **Por qué esto importa para este node en particular:** la tesis de la *colonialidad del hacer*
sostiene que la hegemonía del Norte no es solo sobre los procesos productivos sino **sobre el
pensamiento que constituye la investigación en diseño**. Aplicado reflexivamente: **"¿cuál es el ROI
del diseño?" ya es una pregunta situada, no una pregunta neutra.** Es el correctivo más fuerte que
este node ha recibido a su propio marco.

⚠️ **Advertencia dura y necesaria:** esta tradición es **casi enteramente teórico-crítica y no produce
evidencia empírica de efectos** (rúbrica ⚪/C, no A). **Sería un error meterla como "evidencia a favor
del valor del diseño". Es evidencia de que la pregunta por el valor está formulada desde un lugar.**

Estado de la disciplina en la región: la investigación en diseño **"comienza a afianzarse"** en
América Latina mientras en Europa/EE.UU. está consolidada (F-354); y la WIPO registra que **"en muchos
países en desarrollo el enorme potencial económico e innovador del diseño pasa desapercibido"**, con
la observación —directamente convergente con la iteración 1, pero a escala macro— de que **el diseño,
a diferencia de la innovación, no está bien integrado en la política pública porque su impacto es
difícil de medir** (F-355).

### 2.12 Vacío operativo: dark patterns fuera de poblaciones WEIRD (iter. 2)

Búsqueda adversarial con **resultado negativo bien definido**: **no existe réplica transcultural a
gran escala de dark patterns en población latinoamericana** (F-356). Lo que hay es infraestructura
previa —el campo ya reconoce que su muestra es WEIRD, y hay trabajo en la Universidad de São Paulo
sobre arquitectura de elección en el marco de protección de datos— pero no resultados.

> **Consecuencia directa para este proyecto:** la magnitud del efecto de dark patterns en usuarios
> peruanos (H8) es hoy una **extrapolación desde muestra estadounidense, no un dato**. Eso no
> invalida usar el mecanismo como criterio de diseño; sí invalida citar el "casi 4x" como si aplicara
> a Perú.

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

### 3.7 ⭐ El barrido en español y portugués: no hay desfase, hay desplazamiento de eje (iter. 2)

**Este es el hallazgo que reformula H17.** La conversación en ES/PT existe y es intensa, pero **no
corre por el mismo eje** que la anglosajona.

**(a) La frecuencia bruta engaña — y el mecanismo es nuevo.** La primera página de resultados en
español para "¿la IA reemplazará a los diseñadores?" está dominada por **universidades, bootcamps y
academias** (Anáhuac, UCAL, Cibertec, Continental, ISIL, Corriente Alterna, UXER, Neoland, Ironhack,
SHIFTA/Elisava, CEI, Barreira, ESI Valladolid…) respondiendo **una pregunta de captación de alumnos**
(F-361). ⭐ **Es el equivalente estructural del churnalism, en versión SEO: ~20 piezas que "cubren el
tema" son una sola pieza de marketing con veinte vitrinas.** Descontado eso, la conversación *de
gremio* genuina en ES/PT es **notablemente más delgada** que la anglosajona.

**(b) Sí hay retraso —~19 meses— pero entró por la puerta equivocada.** "AI slop" se acuña en inglés
en **mayo 2024**, es palabra del año en **dic-2025**, y recién entonces entra al español vía Emol
(16-dic-2025), Infobae (20-dic-2025) y Fast Company México (30-ene-2026) — F-360. **No importó desde
la indignación del gremio de diseño, sino desde una noticia de diccionario.** Entró como curiosidad
léxica, no como bandera de identidad profesional, y eso explica el tono. El mismo patrón de
importación se repite con los otros artefactos del debate: encuestas anglosajonas reempaquetadas al
español y al portugués, y el especial identitario *"El diseñador ha muerto"* de Gràffica (ES) **está
vocalizado por Neville Brody y Peter Hall** — voces anglosajonas importadas a un medio español
(F-364). **El debate identitario en ES/PT es mayoritariamente derivativo.**

**(c) El tono es otro, y hay fórmula memética.** Donde el anglosajón dice *"¿sigo siendo diseñador?"*
(angustia de identidad), el hispano-lusófono dice **"esto va a separar a los buenos de los malos, y
yo estoy del lado bueno"** (disciplina de gremio). La fórmula aparece casi palabra por palabra en los
dos idiomas —señal de meme, no de coincidencia—: *"la IA no va a reemplazar a los diseñadores **pero
sí va a dejar en evidencia a algunos**"* (PE), *"não vai substituir web designers **mas vai expor os
ruins**"* (BR), *"está **separando quem pensa de quem só executa**"* (BR), *"va a **dividirlos en dos
grupos muy diferentes**"* (MX) — F-363. **Es una postura de distinción, no de duelo.** Corolario: el
rechazo estético tipo "AI slop" **casi no existe como afecto propio en ES/PT**; cuando aparece es
reportaje *sobre* el fenómeno anglosajón.

**(d) ⭐ Y hay dos agendas propias que la conversación anglosajona no tiene.**

**D1 — Derechos de autor, regulación y acción colectiva organizada: 🔥 el registro más caliente en
español.** No es opinión suelta en redes: es **infraestructura gremial produciendo documentos**.
- **Manifiesto READ** (Red Española de Asociaciones de Diseño), v1.0 jul-2025, presentado el
  19-sep-2025; elaborado por su Grupo de Buenas Prácticas durante 2024-2025; publicado en castellano,
  euskera, gallego, valenciano/catalán e inglés; respaldado por **UGT (sindicato)**, federaciones
  UNESCO y OdiseIA. **Es el primer manifiesto del sector asociativo del diseño español sobre IA — de
  diseño específicamente, no de ilustración** (F-357).
- **Manifiesto multi-federación** (Alianza Audiovisual, ADE, ACE Traductores, FADIP, Unión de
  Correctores): exige autorización previa, remuneración, **retirada del mercado de "modelos
  ilegales"** e indemnización; recogido en iniciativa parlamentaria (F-358).
- 🇦🇷 **Asociación Argentina de Actores**: campaña con Ricardo Darín y otros, lema *"Mi imagen, mis
  expresiones y mi voz son mis herramientas de trabajo"* (F-359).

**D2 — La IA como *pretexto patronal*: 🌡️ marco brasileño sin equivalente anglosajón.** Es
analíticamente el más interesante porque es una **contranarrativa de causalidad**: sostiene que *las
empresas usan la IA como excusa para no admitir sus problemas financieros*, y que *"si el mercado
convence a devs y designers de que una máquina puede reemplazarlos mañana, esos trabajadores aceptan
hacer el trabajo de tres, dejan de exigir mejores condiciones y no se sindicalizan por miedo"*
(F-365). Converge con cobertura de prensa de negocios brasileña sobre empresas usando la IA como
"desculpa para demitir" (F-366).

> ⭐ **Por qué esto es más fuerte que "hay desfase": el mismo shock tecnológico produce crisis de
> identidad donde el gremio es individualista y está desagremiado, y acción colectiva regulatoria
> donde hay federaciones y sindicatos vivos o tradición de análisis de clase. La variable moderadora
> no es la latitud ni el idioma: es la existencia de infraestructura gremial.**

**Perú es el mercado que menos participa de cualquiera de los dos ejes.** No se encontró conversación
peruana propia sobre IA e identidad del diseñador: hay contenido institucional de captación, prensa
suave, y una infraestructura de **tarifas** gremial pre-IA (tarifarios de diseño Lima) que **no
aparece ligada a la IA**. No se halló colegio ni asociación peruana emitiendo posición sobre IA —
contraste marcado con España y Argentina. ⚠️ **Salvedad metodológica que no debe perderse: la
ausencia puede ser real o límite del instrumento** — en Perú mucha conversación gremial vive en
grupos cerrados de WhatsApp/Facebook, no indexables. **La conclusión honesta es "no es públicamente
indexable", no "no existe".**

### 3.8 H11 se refuta y se invierte en el registro ES/PT (iter. 2)

Auditoría con denominador declarado: **N = 38 amplificadores hispano/lusófonos** (definición
reproducible: todo actor que aparece orgánicamente al buscar la pregunta canónica en ES/PT).
**27 de 38 (71%) tienen incentivo comercial directo identificable** — 15 escuelas/bootcamps,
3 curso+mentoría, 5 agencias, 3 SaaS.

🔴 **Pero el conteo, solo, miente.** Al cruzar *incentivo × qué dice cada uno*, la hipótesis se
invierte: **los 27 con incentivo comercial no venden doom, venden el antídoto.** Su género es
uniformemente tranquilizador-reskilling: el titular hace la pregunta ansiosa y el cuerpo la desactiva
("no, pero tienes que actualizarte — con nosotros"). **El doom es el gancho, no la tesis.**

Y **los que sí hacen alarma genuina no tienen nada que vender**: READ, FADIP, UGT, la Asociación
Argentina de Actores, colectivos activistas, una newsletter laboral brasileña cuyo incentivo es
*inverso* (quiere sindicalización, no clientes). Los tres individuos más citados del nicho son
**empleados a sueldo** sin curso que ofrecer, y una bolsa de empleo de diseño —cuyo incentivo es
explícitamente **anti-doom**— publica un número titulado *"¿será que el diseño murió?"*.

> **Corrección práctica que reemplaza a H11 en este registro: no hay que descontar el volumen social
> por interés comercial, hay que descontarlo por SEO educativo.** Es un sesgo distinto: **infla la
> frecuencia aparente, no la alarma.** ⚠️ Esto vale para ES/PT; **no se extiende al registro
> anglosajón**, donde la iteración 1 encontró otra estructura y el ecosistema de cohortes y
> newsletters pagas es mucho más denso.

### 3.9 Service design: silencio social, vida institucional (iter. 2)

Sigue 🧊 como conversación en los tres idiomas — nadie está peleando por esto en redes en ningún
idioma. **Pero la pista era correcta: vive en el sector público** (F-367): SDN Brazil chapter (2011),
Service Design Day Brasil 2026, gov.br Design System 4.0; **Laboratorio de Gobierno de Chile
contratando un consultor en Diseño de Servicios Digitales**; laboratorios de innovación pública en
Argentina y España; LAIB, ELIP 2026, Laboratorio GovTech LATAM del BID Lab.

⭐ **Y hay un hook peruano vigente, que es lo más accionable de esta pista para el proyecto:**
- **Decreto Supremo 090-2026-PCM** — modifica el Reglamento del Sistema Administrativo de
  Modernización de la Gestión Pública para **incorporar formalmente la innovación pública** como eje,
  promoviendo el diseño e implementación de soluciones para mejorar la calidad de los servicios al
  ciudadano (F-368).
- **2ª edición del Concurso Nacional de Buenas Prácticas en Calidad de Servicios 2026** de la PCM,
  con ejes de mejora continua, innovación pública y gobierno abierto (F-369).
- **Service Design Jam Lima 2026**; formación de Fundación NovaGob en Perú sobre diseño de servicios
  públicos centrado en las personas.

> **Reformulación:** el service design no está muerto ni silencioso — está **desacoplado del
> discurso**. Cero temperatura social, base institucional creciente. Para un proyecto que trabaja
> seguros y salud en Perú, **el decreto y el concurso son la superficie de contacto, no la
> conversación de redes.**

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

### 4.5 ⭐ Service design: la caída está cuantificada, la absorción solo anecdotada (iter. 2, H18)

**La única serie temporal cuantificada que se encontró** (ITJobsWatch, agregador de avisos IT del
Reino Unido con metodología pública — F-370):

| Métrica "Service Designer" (UK) | Valor | Corte |
|---|---|---|
| Vacantes de **contrato**, 6 meses | **210 (2023) → 96 (2024) → 83 (2025)** ≈ **−60% en dos años** | abr-2023 / abr-2024 / abr-2025 |
| Vacantes **permanentes**, 6 meses | **28** (0,051% de todos los avisos permanentes IT del UK) | a 30-may-2025 |
| Mediana salarial | **£55.000, −15,03% YoY** (desde £64.732) | a 30-may-2025 |
| Mediana excluyendo Londres | **£50.000, −31,03% YoY** | a 30-may-2025 |

⚠️ **Comparabilidad y vigencia, sin adornos:** cubre **solo avisos de IT en Reino Unido** (mucho
service design vive fuera de esa taxonomía); **N=28** hace que la variación salarial sea ruido, no
señal; y **el dato más reciente tiene 14 meses** — no se sabe si la caída continuó o se estabilizó en
2026, porque el sitio quedó bloqueado.

**Destrucción documentada de capacidad pública (EE.UU.):** **18F fue eliminado íntegramente el
1-mar-2025** —~90-100 investigadores, diseñadores y product managers notificados a medianoche— por
instrucción de DOGE a la GSA; el email interno calificó al equipo de *"non-critical"*; 18F facturaba
**US$250/hora** a otras agencias y dejó "decenas de millones" en proyectos inconclusos (F-371).
**Es el dato más duro que existe de destrucción de capacidad pública de service design.**

**Continuidad documentada (Reino Unido):** contrato GDS de **£19M** a Made Tech (abr-2026, vía CCS
RM6100 — F-372); **£2,5M** a ThoughtWorks para GOV.UK Publishing Service desde abr-2025 (notice
oficial de Contracts Finder — F-373); el framework RM1043.9 sigue nombrando explícitamente
*"user-centred design services"* entre lo comprable.
⚠️ **Pero ojo con el denominador: ninguno de esos es un contrato *de service design*.** Son contratos
de entrega de IT donde el diseño va **empaquetado dentro**. Eso es exactamente lo que predice la
tesis de absorción — **y también lo que hace imposible medir el gasto público en service design como
línea separada.** No se encontró ninguna licitación 2026 cuyo objeto sea service design en sí.

**¿Migró in-house?** Solo hay **prueba de existencia, no de volumen**: vacantes 2026 de *Head of
Service Design* en NatWest (dentro del Design Executive Leadership Team), *Principal Service Designer*
en Valley Bank, service designer en Golden 1 Credit Union, y un IT Specialist de UX/Service Design en
el ADB (F-374). **No se encontró ni un solo dato de headcount de equipos de diseño in-house en bancos,
aseguradoras o telcos** — los outlooks sectoriales hablan de headcount total y de contratación en IA
y **nunca desagregan diseño**. Señal adyacente mala: **caída de ~50% en contratación entre las 30
mayores aseguradoras de NA y Europa desde 2022**.

> **Veredicto honesto:** *"absorbido" está mejor sostenido que "muerto"* — el rol no desapareció, se
> disolvió dentro de roles de producto/entrega y de contratos de IT donde ya no es una línea contable
> separable. **Pero los dos lados de la ecuación se miden con instrumentos de calidad radicalmente
> distinta** (la caída, con una serie; la absorción, con avisos sueltos), así que **el neto no es
> calculable**. Y eso deja a la disciplina estructuralmente inmedible: **la inmedibilidad no es lo
> mismo que la salud.**

### 4.6 Figma: el baseline queda fijado antes del 5-ago-2026 (iter. 2, H13/H16)

**El reporte Q2 2026 es el miércoles 5-ago-2026** (anuncio de la propia compañía ~15-jul-2026 —
F-376). **Hoy es 27-jul-2026: aún no ocurrió, y este node no especula sobre su resultado.** Lo que sí
queda registrado es el punto de partida, para que la iteración 3 pueda falsar H13 limpiamente:

| Dato | Valor | Fecha exacta |
|---|---|---|
| **Guía Q2 2026** | US$348-350M, **~40% YoY** en el punto medio (**+4,4% QoQ**) | dada el 14-may-2026 |
| **Guía FY2026** | US$1,422-1,428B, **~35% YoY**, +US$55M sobre la guía previa | 14-may-2026 |
| Precio FIG | **US$21,12** | 25-jul-2026 |
| Precio de IPO | US$33,00 | 31-jul-2025 |
| Market cap | ~US$11,2-11,5B (**−80% desde el debut**) | jul-2026 |
| Máx./mín. 52 semanas | US$142,92 / US$16,60 | 12 meses a jul-2026 |
| Consenso | PT US$30,40; **6 buy, 0 sell** | jul-2026 |

📌 **Observación que la iteración 1 no tenía y que arma la falsación: la guía de Q2 (40%) está por
debajo del crecimiento real de Q1 (46%). Figma está guiando a desaceleración por su propia boca.**
La prueba limpia del 5-ago es: ¿bate y reacelera, o confirma el 40%?

**Q1 2026 fue el mejor trimestre que ha publicado** (F-375): revenue **US$333,4M, +46% YoY** (consenso
US$313,2M); **NDR 139%**, la más alta en 2+ años; clientes >US$10k ARR **15.218, +37% YoY**; margen
bruto 82%; FCF **US$89M, 27% de margen**. **P/S forward implícito: ~7,9x.** Es decir: **el mercado
paga ~8 veces ventas por un negocio que crece 35-40% con 82% de margen bruto.** Eso no es un múltiplo
de castigo por *desempeño*; es un **descuento por riesgo terminal**.

**Señales de problema buscadas activamente (no aparecieron solas):** short interest de **15,4M
acciones (~US$900M, ~35% del float)**, máximo post-IPO; **insiders vendieron 5.504.322 acciones
(~US$208,9M) en tres meses**, incluidas 3.029.063 del CEO; lock-up vencido el 27-ene-2026 con tramos
escalonados a lo largo de 2026 (F-377). **Contrapeso:** BofA reinició cobertura con Buy y PT US$30
(7-jul-2026).

> **H13 se reformula con lo aprendido: el descuento no es por desempeño operativo, es (a) mecánico
> —lock-up y venta de insiders— y (b) por riesgo terminal de que la IA generativa comprima la capa de
> diseño. El mercado no está diciendo "el diseño no rinde"; está diciendo "el diseño puede dejar de
> ser una capa con dueño".**

### 4.7 ⭐ H16 se invierte: las métricas narrativas se retiran cuando dejan de halagar (iter. 2)

Sí existe retirada de métricas — **pero no en las herramientas de diseño, sino en la consultoría**:

- ⭐ **Accenture**: la CEO anunció en el call del **18-jun-2026** que **ese sería el último trimestre**
  en que reporta por separado bookings y revenue de *advanced AI*, razón declarada: "es tan omnipresente
  que ya no tiene sentido aislarla". **Ocurre exactamente cuando los bookings caen −3% en moneda local
  y Managed Services −15% YoY**, con recorte de guía FY y ~11.000 despidos en 2026 tras ~22.000 en
  2025 (F-378, F-383).
- **Adobe**: su ARR de US$27,1B **incluye ~US$480M de ARR adquirido de Semrush** (abr-2026) — la meta
  del FY26 está **inorgánicamente inflada**; además **difirió el aumento anual de precios de Creative
  Cloud** y reconoce presión sobre el ARR en el segundo semestre. **El CFO se fue el 15-jun-2026**,
  cuatro días después del reporte, con la sucesión del CEO ya en calendario (F-379).
- **Figma, en cambio, no dejó de reportar nada** — publicó más granularidad y mejores números.

> **El patrón que emerge no es "el estándar de reporting se degrada". Es: las métricas narrativas se
> retiran cuando dejan de halagar; las métricas de producto sobreviven mientras halaguen. La
> retirada de una métrica es, en sí misma, una señal legible.**

⚠️ Comparabilidad: el NDR de Figma se calcula **solo sobre clientes con >US$10k de ARR** (estrechamiento
preexistente, no nuevo) — su 139% **no es comparable** con un NDR de base completa. Y el ARR de Adobe
**dejó de ser comparable consigo mismo** al absorber Semrush sin desagregar la contribución.

### 4.8 Lovable: la desaceleración se deriva de sus propios anuncios (iter. 2, H14)

Toda la escalera de ARR es autorreportada, pero **la desaceleración se deduce aritméticamente de dos
anuncios de la propia empresa — y va contra su interés, lo que la hace mucho más creíble que
cualquier cifra positiva que publiquen** (F-380):

| Hito ARR | Cuándo | Meses desde el anterior |
|---|---|---|
| US$100M | mes 8 | — |
| US$200M | mes 12 | +4 |
| US$300M | mes 14 | +2 |
| **US$400M** | feb-2026 | **+1** |
| **US$500M** (run-rate) | 9-jun-2026 | **+4** |

> **ARR neto nuevo por mes: ~US$100M/mes → ~US$25M/mes. Una desaceleración de ~4x.**

**Señales de retención — todas indirectas, ninguna directa** (F-381): Lovable **se negó a compartir su
tasa de churn** cuando se le preguntó directamente; su co-fundador afirma NDR "por encima de 100%",
métrica **engañosa por construcción** (el NDR solo mide a los que se quedan: con 50% de churn y el
resto gastando 2x, se ve espectacular mientras el negocio es una puerta giratoria); **el CEO de un
competidor admitió públicamente que "la tasa de churn de todos es realmente alta"** en toda la
categoría; y el primer reporte de usuarios de Lovable —explícitamente **no auditado**— reporta que
**60,5% de los usuarios todavía no gana dinero** (F-382), un indicador adelantado de churn. Presión
estructural adicional: Lovable **paga inferencia por llamada**, así que cada app construida tiene COGS
real.

📌 **Eco de cita desmontado:** la ronda en conversaciones de ~US$300M @ US$13,2B aparece en seis medios
que **citan todos el mismo anuncio**. Es **1 fuente primaria con 6 altavoces**, no triangulación.

> **H14 queda `parcial`: la desaceleración está respaldada, la falta de retención no.** Ningún actor
> de la categoría publica churn ni NRR — **no es que no se encontrara, es que no se publica**. Hay
> cuatro señales indirectas convergentes y **cero mediciones directas**. **La ausencia sistemática del
> dato, cuando todos los demás se publican con entusiasmo, es en sí misma informativa — pero no es
> una conclusión.**

### 4.9 Consultoras: se liquida la estructura de propiedad, no evidentemente la demanda (iter. 2, H15)

| Empresa | Qué pasó | Fecha |
|---|---|---|
| **R/GA** | IPG la vende a **Truelink Capital** (private equity); management coinvierte | mar-2025 · US$200-300M |
| **Huge** | IPG la vende a **AEA Investors**, fusionada con Hero Digital | dic-2024 |
| **IPG** | **Omnicom completa su adquisición** (US$13B) | 26-nov-2025 |
| **Accenture Song** | Absorbida en "Reinvention Services" — **pero sigue comprando agencias** (Whalar, jun-2026) | 2026 · ~US$20B revenue FY25, +8% |
| **frog** | **Sigue viva** como marca de Capgemini Invent; creció de ~500 a **~2.200 personas** absorbiendo cinco firmas | vigente abr-2026 |

**Contraevidencia buscada a propósito y encontrada** (F-384, F-385): **frog no encogió, se
cuadruplicó**; Accenture Song **sigue comprando agencias en 2026** — si la demanda de diseño estuviera
muerta, no se compraría; y Veryday fue **adquirida por McKinsey**, no cerrada (§1.bis).

📌 Circula un revenue de ~US$544M para R/GA (fuente 🔴 E, sin fecha). Si fuera direccionalmente
correcto, US$200-300M implicaría **~0,4-0,55x revenue** — múltiplo de liquidación para un negocio de
servicios, donde lo normal es 1-2x. **No verificable; indicativo, no establecido.**

> **H15 se reformula: lo que se liquida es la consultora de diseño como P&L autónomo, que migra a
> roll-ups de private equity o a P&L integrados de consultoría/tech. NO está demostrado que el revenue
> del diseño se desplome.** Song (~US$20B), frog (~2.200) y Designit (~1.7K) están **grandes e
> intactos como unidades absorbidas**. Los fracasos documentados son **de estructura y propiedad**,
> no evidentemente de demanda. **Y el único número del lado de la demanda que la iteración 1 daba por
> bueno era una cita anónima (§1.bis, corrección 2).**

### 4.10 ⭐ La arista peruana verificable — y la que no lo es (iter. 2, H17-negocio)

**Lo verificable, con grado de filing:** **Credicorp (NYSE: BAP)** presenta 6-K ante la SEC — es, con
diferencia, el dato de experiencia digital latinoamericana con mayor rigor disponible (F-386, Q1 2026):

| Métrica | Valor |
|---|---|
| Revenue de **Yape** | **+101% YoY** |
| Utilidad operativa de Yape | ~S/205M (~US$59M) = **6,9% de la utilidad pre-impuestos del grupo** |
| Yape como % del fee income del grupo | **17%** (desde 12%) |
| Revenue por MAU | **+65% YoY** a ~S/10,3 |
| Utilidad neta del grupo · ROE | S/2.063M, +16,1% YoY · **21,1%** |

⚠️ **Dos advertencias que valen tanto como el dato.** **(1) Esto NO es ROI del diseño.** Es el
desempeño de un producto digital / modelo de negocio; atribuirlo a "diseño" sería **exactamente el
error de atribución que este node existe para evitar**. Lo que demuestra es que **existe una
experiencia digital peruana con resultados de negocio auditables** — el sustrato, no la causa.
**(2) 🚩 Bandera de calidad de datos:** al menos una fuente secundaria transcribió **"S/10,3" como
"PLN10,3"** (zlotys polacos). **Las cifras latinoamericanas se corrompen en la cadena secundaria en
inglés: para LatAm, ir al filing o no usar el dato.**

🔴 **Lo NO verificable, y hay que decirlo:** circula que **el NPS de Rimac subió de 20 a 53** en dos
años (y de 18 a 70 en vehiculares). **No se pudo trazar a ninguna fuente primaria**; los candidatos
revisados no contienen la cifra. **Tratar como NO VERIFICADA** hasta rastrear el origen (F-387). Lo
que sí está documentado de Rimac son **casos de cliente de proveedores tecnológicos** (🟠 D, el
proveedor tiene interés): modernización de core con reducción de tiempos de procesamiento de hasta 80%
y productividad +80%, ~3 millones de clientes; nueva modernización cloud anunciada el **20-jul-2026**;
y la adjudicación de **SISCO VIII** (vigencia ene-2025 a dic-2026) — F-389.

**El mercado de diseño en LatAm, sencillamente, no está medido.** Las cifras de outsourcing regional
que circulan **se contradicen entre sí** (US$126,3B a 2030 vs. US$320B a 2030 para el mismo mercado,
ambas en blogs de vendors citando informes que no se identifican — F-390) y, sobre todo, **ninguna
desagrega diseño/UX: va empaquetado dentro de "IT services"**. Lo único con textura es una encuesta
de comunidad (N=651) que reporta **hasta 8x de dispersión salarial en el mismo puesto** (F-391) — que
por sí sola es señal de **un mercado sin estándar de precios**, consistente con una disciplina cuyo
valor no está establecido.

---

## 5. ⚖️ Síntesis: escala de madurez de evidencia

Esta tabla es el **entregable operativo** del node. Cada iteración la actualiza.
La columna **Δ** marca lo que cambió en la iteración 2.

| Tendencia | Estado | Δ iter. 2 | Base |
|---|---|---|---|
| **Dark patterns mueven conducta económica** | 🟢 Documentado (causal) — ⚠️ **solo en muestra WEIRD** | ⚠️ acotado | F-241, F-251, F-356 |
| **Accesibilidad como obligación legal (UE)** | 🟢 Documentado (normativo) | = | F-265 |
| **Capacidad de diseño ↔ desempeño de firma** | 🟢 Documentado (asociación, no causalidad) | = | F-237, F-238 |
| **Claridad/fluidez > ornamento** (usabilidad **percibida**) | 🟢 Documentado | = | F-249, F-272 |
| **Estética → desempeño OBJETIVO** *(constructo distinto del anterior)* | 🟢 Documentado, **efecto pequeño (g=0,29)** — ⚠️ sin réplica independiente | 🆕 | F-346, F-347 |
| **La mayoría de rediseños no mueve la métrica** | 🟢 Documentado (causal, A/B a escala) | = | F-262 |
| **Reuso/design systems → menor densidad de defectos** | 🟢 Documentado (5 estudios industriales) | 🆕 | F-329 |
| **Disociación juicio subjetivo ≠ desempeño objetivo** | 🟢 Documentado (patrón transversal, ahora con EEG) | 🆕 ⭐ | F-342, F-341, F-346 + METR |
| **Codiseño/service design mejora outcomes** | 🟢 **Documentado el DÉFICIT**: 2 de 14.376 reportes midieron outcomes; 4/17 favorables | 🆕 ⭐ | F-348, F-349 |
| **Caída de la demanda de service design (UK)** | 🟢 Documentado (serie: −60% de contratos 2023-2025) | 🆕 | F-370, F-371 |
| **Adaptación que PRESERVA la estabilidad espacial** *(ephemeral, ability-based)* | 🟢 Documentado que **mejora** el desempeño | 🆕 ⭐ | F-344, F-345 |
| **Adaptación que ROMPE la estabilidad espacial** *(menús dinámicos)* | 🔴 Documentado que **degrada** | 🆕 | F-340, F-341 |
| **Explicabilidad de IA aumenta confianza** | 🟡 Parcial — sobrevendido (efecto moderado) | = | F-242 |
| **Design systems aceleran el desarrollo** | 🔴 **DEGRADADO**: 30 años de software reuse sin establecer el efecto; la métrica dominante sube por construcción | ⬇️ ⭐ | F-329, F-330, F-331, F-333, F-335 |
| **Explicaciones mejoran la decisión humano-IA** | 🔴 Contradicho en su forma general | = | F-243, F-244, F-246 |
| **ROI del diseño 100:1 / MDI +32%/+56% / 671% / "47% según NN/g"** | 🔴 Hype (eco de cita) — **+1 caso nuevo con autoridad falsa** | ⬆️ | F-266, F-268, F-327, F-334 |
| **Generative UI / interfaces generadas por LLM** | 🔴 Propuesta sin respaldo independiente — **y en la peor celda de la taxonomía de adaptación** | ⬇️ | F-247, F-256, F-336, F-337, F-338 |
| **Agentic UX** | 🔴 Hype declarado por sus propios autores | = | F-261 |
| **Spatial computing como tendencia de diseño** | 🔴 Hype (~5% de diseñadores construye para ello) | = | F-279 |
| **Personalización con IA a escala** | 🔴 Contradicho / condicional (efecto backfire) | = | F-253, F-254 |
| **Crisis del modelo consultora de diseño** | 🟡 **REFORMULADO**: se liquida la **propiedad** (P&L autónomo → PE / absorción), no está demostrada la caída de demanda | ⬇️ | F-384, F-385, F-388 · ⚠️ ver §1.bis |
| **La IA acelera el trabajo de diseño/producto** | 🟡 **Ya no es ⚔️**: el preprint no medía lo que se creía; queda **un solo RCT** (METR, −19%) y evidencia de que la percepción excede al desempeño | ⬇️ ⭐ | F-257 · ⚠️ ver §1.bis |
| **La IA está causando el desempleo de diseñadores** | ⚔️ Atribución declarada ≠ causalidad — **+ hipótesis rival: "IA como pretexto patronal"** | ⬆️ | F-282 vs. F-283 vs. F-365 |
| **Tradición latinoamericana del diseño como marco alternativo** | 🟡 Documentada como tradición · 🔴 sin evidencia empírica de efectos · ⚠️ tesis de la interfaz-1972 = fuente única | 🆕 ⭐ | F-350, F-351, F-352, F-353 |
| **El mercado de diseño en LatAm tiene tamaño conocido** | 🔴 **No medido**: cifras contradictorias y ninguna desagrega diseño | 🆕 | F-390, F-388 |

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
4. ⭐ **(iter. 2) El diseño se volvió estructuralmente difícil de contar — y las tres pistas lo
   encuentran por caminos independientes.** La **empírica**: la métrica dominante del sector
   (*apparent productivity*) **sube por construcción con el reuso**, así que no puede falsar lo que
   dice demostrar. La **social**: la frecuencia aparente en español está inflada por **SEO
   educativo**, no por conversación real. La **de negocio**: el diseño **ya no es una línea contable
   separable** en ningún lado — ni en los contratos públicos (va empaquetado en entrega de IT), ni
   en los informes de mercado LatAm (va dentro de "IT services"), ni en el P&L de las consultoras
   absorbidas. **La inmedibilidad no es lo mismo que la salud, y tampoco es lo mismo que la
   enfermedad: es la condición que impide decidir entre ambas.**
5. ⭐ **(iter. 2) La retirada o el silencio de una métrica es información.** Accenture deja de
   reportar su métrica-estandarte de IA justo cuando deja de halagarla; Lovable se niega a publicar
   churn mientras publica todo lo demás; el service design no tiene una sola licitación con su nombre
   en el objeto. **Los tres son el mismo gesto en tres registros: donde el dato existiría y no
   aparece, la ausencia es el hallazgo.**

### Divergencias que este node NO resuelve

- ~~**⚔️ Productividad con IA**~~ → **(iter. 2) RESUELTA COMO FALSO CONFLICTO.** El preprint de
  "design-system-aware AI" no medía design systems y su brazo de comparación tiene n=7; no es
  comparable con METR (devs expertos en repos maduros que conocían a fondo). **Ninguno refuta al
  otro.** Ver §1.bis. Lo que queda en pie es **un solo RCT** con desempeño objetivo (METR, −19%) y
  una familia creciente de evidencia de que **la percepción de mejora excede a la mejora real**.
- **⚔️ Percepción gremial vs. dato oficial**: Figma/Adobe (encuestas de emisor interesado) reportan
  demanda estable o creciente; BLS proyecta +2% a diez años para diseño gráfico.
- **⚔️ Estética anti-IA**: alta validación social, evidencia de usabilidad negativa (8-10% de éxito
  de tarea en anti-diseño caótico), y promoción por parte de los propios vendors de IA.
- 🆕 **⚔️ (iter. 2) Estética → desempeño objetivo: ¿g=0,12 o g=0,29?** El estimador **se duplicó**
  entre el meta-análisis de 2019 y el de 2026, **con el mismo autor senior** y con sospecha de sesgo
  de publicación declarada por los propios autores en la versión previa. No son dos confirmaciones
  independientes. **Sin resolver hasta ver el análisis de sesgo del suplemento.**
- 🆕 **⚔️ (iter. 2) ¿Qué causa la ansiedad del gremio?** La lectura anglosajona la atribuye a la
  capacidad técnica de la IA; el marco brasileño sostiene que la causa es **el uso gerencial de la IA
  como amenaza disciplinaria** ("la IA como pretexto patronal"). Son dos causalidades distintas con
  consecuencias prácticas opuestas. **Contrastable, y sin contrastar.**
- 🆕 **⚔️ (iter. 2) Service design: ¿absorbido o desmantelado?** La caída está medida con una serie
  (−60% de contratos UK); la absorción in-house solo con avisos sueltos. **Instrumentos de calidad
  radicalmente distinta a cada lado de la ecuación: el neto no es calculable.**

---

## 6. 🧪 Tablero de hipótesis vivas

**Este es el corazón iterativo del node.** Cada corrida debe intentar mover al menos una fila.
Estados: `abierta` · `respaldada` · `refutada` · `parcial`.

| # | Hipótesis | Estado | Cómo se falsa |
|---|---|---|---|
| **H1** | Un índice de empresas "design-centric" definido **ex ante** tendrá exceso de retorno sobre el S&P **indistinguible de cero** (el +211% del DVI es look-ahead bias + supervivencia) | `abierta` — predicción del node: el exceso se reduce >70% | Replicación prospectiva del DVI con criterios congelados en t₀ |
| **H2** | El reporte de Forrester (2016) **no contiene** la afirmación "$1 → $100" en la forma en que circula | `abierta` | Compra y lectura del reporte (~US$1.495) |
| **H3** | ~~En tarea repetida (≥5 sesiones) la generative UI dará peor tiempo y aprendibilidad que una UI estática~~ → **REFORMULADA (iter. 2)**: la degradación no la causa "adaptar", la causa **romper la estabilidad espacial** y adaptar a una **predicción móvil de intención** en vez de a un **rasgo estable**. La generative UI degradará **porque regenera el layout**, no porque se adapte | `parcial` — respaldada la premisa (los preprints miden preferencia en sesión única, no aprendibilidad) y **refutada la formulación gruesa**: *ephemeral adaptation* y *ability-based design* **mejoran** el desempeño (F-344, F-345) | Estudio longitudinal que compare las tres celdas de la taxonomía de §2.7, no dos condiciones |
| **H4** | Añadir explicación ("¿por qué veo esto?") **no** mejora precisión ni calibración en decisiones de **baja** dificultad; **sí** en alta | `parcial` — respaldada por F-246 en laboratorio, sin replicar en dominio aplicado | RCT con dificultad manipulada en recomendación de producto financiero/seguros |
| **H5** | En cualquier estudio que mida **a la vez** desempeño objetivo y percibido, la mejora subjetiva **excederá** a la objetiva en ≥20 pp | `abierta` — **la hipótesis de mayor valor destructivo**: si se sostiene, invalida casi todo reporte de industria sobre design systems, IA y madurez de diseño | Meta-análisis de estudios que reporten ambas medidas |
| **H6** | El efecto de un design system sobre el tiempo de desarrollo será **<20%** (no 47%, no 69%) con contrabalanceo de orden, N≥40 y devs externos a la organización que mantiene el sistema | ⭐ **`respaldada` en dirección (iter. 2), por vía indirecta.** El estudio que la falsaría **no existe** — ni en design systems ni, tras 30 años, en software reuse. Pero tres vías independientes la sostienen: 3/11 estudios con ganancia y solo en *apparent productivity* (métrica inflada por construcción); signos contradictorios en el estudio diseñado para medirlo; y 87% de estudios primarios de calidad baja/moderada con **costos** de productividad documentados. El 47% de Sparkbox es N=8 con **orden fijo y tarea repetida idéntica** | **Reformulada:** ya no "¿cuál es el efecto?" sino **"¿por qué una industria que ahora sí corre RCTs no ha corrido ninguno sobre design systems, y por qué su métrica dominante es la que ya se sabe inflada?"** |
| **H6b** | 🆕 El brazo **Design-System-solo vs. Manual** del preprint de Zup (arXiv:2607.13156) mostrará un efecto **muy inferior** al −46/−69% que se atribuyó erróneamente a los design systems | `abierta` — **es el número que resolvería H6 empíricamente**; no se pudo obtener (arXiv bloqueado dos iteraciones seguidas) | Leer el preprint de primera mano |
| **H7** | En un A/B real, las variantes que aumentan **fluidez** (contraste, jerarquía, menos elementos) superarán a las que aumentan atractivo estético sin aumentar fluidez | `abierta` — **aplicable directamente al contexto Rimac/seguros** | Experimento de campo |
| **H8** | En Perú, donde la causa #1 de desconfianza en seguros es la falta de información, la exposición a patterns de *hidden information* predecirá desconfianza en aseguradoras **con más fuerza que las variables demográficas** | `abierta` — **el puente más directo con el resto del proyecto**. ⚠️ **(iter. 2) Se confirmó que NO existe réplica de dark patterns en población latinoamericana** (F-356): el "casi 4x" es hoy **extrapolación desde muestra estadounidense**, no un dato aplicable a Perú | Experimento sobre muestra peruana replicando Luguri & Strahilevitz |
| **H9** | **Brecha actitud-conducta en diseñadores**: el discurso público es anti-IA/anti-slop pero la adopción declarada es altísima (89% trabaja más rápido) | `abierta` — **estructuralmente el mismo fenómeno que `disposicion_compartir_datos_pricing` en `lapuerta`** | Medir si la indignación estética predice o no comportamiento de uso |
| **H10** | La ansiedad gremial es un fenómeno de **seniority**, no de gremio: el daño está concentrado en juniors pero se enuncia en nombre de "los diseñadores" | `abierta` — no se pudo segmentar por seniority | Datos de empleo o encuesta segmentada por años de experiencia |
| **H11** | **El doom tiene modelo de negocio**: la proporción de amplificadores del discurso "la IA mata al diseño" con incentivo comercial directo es alta; si lo es, el volumen social debe descontarse fuertemente | ⭐ **`refutada` e INVERTIDA en ES/PT (iter. 2)** · **`abierta` en anglosajón.** Auditados N=38: **71% tiene incentivo comercial — pero no vende doom, vende el antídoto** (tranquilizador-reskilling; el doom es el gancho, no la tesis). Los que sí alarman son **sindicatos y federaciones sin nada que vender**. **La corrección correcta no es descontar por interés comercial sino por SEO educativo** — que infla la *frecuencia aparente*, no la *alarma* | Repetir la auditoría con denominador por **audiencia** (no por visibilidad en buscador) y en el eje anglosajón |
| **H12** | El backlash estético es **señalización de estatus profesional**, no preferencia de usuario | `parcial` — respaldada por F-284 (gatekeeping) y F-297 (usabilidad) | Testear si la "autenticidad imperfecta" mejora alguna métrica de usuario |
| **H13** | **Desacople valuación/desempeño**: si Figma reporta ≥40% de crecimiento en Q2 2026 y la acción **no** recupera sobre $33, el mercado descuenta disrupción por IA, no ejecución | ⭐ **`respaldada` y reformulada (iter. 2)**: la divergencia se agudizó (Q1 +46% YoY, NDR 139%, FCF 27% · acción a **US$21,12 el 25-jul-2026**, 64% del precio de IPO, −80% de market cap desde el debut, P/S forward ~7,9x). **El descuento no es por desempeño: es mecánico (lock-up + venta de insiders, ~35% del float en corto) y por riesgo terminal.** El mercado no dice "el diseño no rinde", dice **"el diseño puede dejar de ser una capa con dueño"**. 📌 **Figma guía a 40% cuando su Q1 real fue 46%: guía a desaceleración por su propia boca** | **Falsable el 5-ago-2026.** Baseline fijado en §4.6 |
| **H14** | **El ARR de vibe coding no retiene**: si Lovable cierra a $12-13,2B, su ARR a 12 meses crecerá <50% (vs. 150%+ histórico), revelando la cohorte de churn | **`parcial` (iter. 2)**: **desaceleración respaldada** y derivada aritméticamente de los propios anuncios de la empresa (**ARR neto nuevo de ~US$100M/mes a ~US$25M/mes, −4x**) — evidencia contra el interés del emisor. **Retención `abierta`: nadie en la categoría publica churn ni NRR.** Cuatro señales indirectas convergentes, cero mediciones directas | Comparar ARR jul-2026 vs. jul-2027; se resuelve de inmediato si publican NRR |
| **H15** | ~~**La consultora de diseño pura no vuelve**~~ → **REFORMULADA (iter. 2)**: lo que se liquida es **la consultora de diseño como P&L autónomo** (migra a roll-ups de private equity o a P&L integrados de consultoría/tech), **no está demostrada una caída de la demanda** | **`parcial`** — contraevidencia real: **frog no encogió, se cuadruplicó** (~500 → ~2.200); Accenture Song **sigue comprando agencias en 2026**; Veryday fue **adquirida**, no cerrada. Y **el único número del lado de la demanda que la iter. 1 daba por bueno (IDEO −67%) era una cita anónima** (§1.bis) | Un reporte de revenue verificable de cualquier consultora de diseño — que **estructuralmente no existirá**: ninguna presenta filings |
| **H16** | **El estándar de reporting se degrada donde hay presión de IA**: si Figma deja de reportar NDR o paid customers en algún trimestre 2026-2027, se refuerza | ⭐ **`parcial` y con el patrón INVERTIDO (iter. 2)**: la retirada ocurrió **en la consultoría, no en las herramientas** — Accenture dejó de reportar su métrica-estandarte de IA el **18-jun-2026**, justo cuando bookings −3% y Managed Services −15%; Adobe rellenó su ARR con Semrush. **Figma reportó más granularidad y mejores números.** Regla que emerge: **las métricas narrativas se retiran cuando dejan de halagar; las de producto sobreviven mientras halaguen** | Trimestre a trimestre |
| **H17** | ~~**Desfase geográfico**~~ → ⭐ **REFORMULADA (iter. 2): no hay desfase, hay DESPLAZAMIENTO DE EJE.** El mismo shock produce **crisis de identidad** donde el gremio está desagremiado y **acción colectiva regulatoria** donde hay federaciones/sindicatos vivos o tradición de análisis de clase. **La variable moderadora no es la latitud ni el idioma: es la existencia de infraestructura gremial** | **`parcial`**: retraso real (~19 meses en "AI slop", que entró al español **por una noticia de diccionario**, no por indignación de diseño); tono **pragmático-meritocrático**, no existencial; **dos agendas propias sin equivalente anglosajón** (derechos/regulación 🔥 en España; "IA como pretexto patronal" 🌡️ en Brasil). **Perú es el que menos participa** — con la salvedad de que su conversación gremial no es públicamente indexable | Comparar la presencia de federaciones/sindicatos de diseño activos con el eje dominante del discurso, país por país |
| **H18** | ~~**El silencio del service design es madurez, no irrelevancia**~~ → ⭐ **REFORMULADA (iter. 2): es un TERCER ESTADO — el campo produjo proceso y nunca construyó el aparato de evaluación de outcomes** | **`respaldada` la lectura pesimista**: 14.376 reportes cribados → 13 elegibles → **2 midieron outcomes** → **4 de 17 favorables**; y las propias revisiones declaran que "una evaluación rigurosa falta frecuentemente". **Caída cuantificada** (−60% de contratos UK 2023-2025; 18F eliminado) vs. **absorción solo anecdotada** → **neto no calculable**. Lo que sí se absorbió en operaciones (blueprinting, S-D logic) es **el método, no la disciplina** | Leer el *Service Design Salary(+) Report 2026* (1.000+ profesionales, 100+ países) — mejor instrumento primario existente |
| **H19** | 🆕 **La disociación juicio-desempeño es un fenómeno general de la interacción con sistemas adaptativos, no un accidente de cada estudio**: en cualquier diseño que mida ambas cosas, la preferencia declarada **no predecirá** el desempeño objetivo, y en varios casos irá en sentido contrario | **`respaldada` (iter. 2)** — cinco piezas independientes ya convergen: METR, Preßler, Findlater & McGrenere, **Gaspar-Figueiredo 2026 con EEG** (lo preferido registra **mayor** carga cognitiva) y el confusor de usabilidad experimentada de Schlamann 2026. **Es la generalización de H5** | Un estudio que mida ambas y encuentre correlación positiva fuerte la debilitaría |
| **H20** | 🆕 **La ansiedad del gremio la causa el uso gerencial de la IA como amenaza disciplinaria, no su capacidad técnica** (hipótesis rival brasileña) | `abierta` — **ataca directamente el hueco de causalidad que la iter. 1 dejó abierto** y tiene consecuencias prácticas opuestas a la lectura estándar | Correlacionar anuncios de despidos "por IA" con desempeño financiero previo de la empresa; buscar admisiones de ejecutivos |
| **H21** | 🆕 **El meta-análisis de estética 2026 (g=0,29) no sobrevivirá a un análisis de sesgo de publicación**: el estimador se duplicó respecto de 2019 (g=0,12), con el mismo autor senior y con sesgo ya declarado como sospecha por los propios autores | `abierta` — **primer objetivo de la iteración 3** | Leer el suplemento en Zenodo: funnel plot y análisis de sensibilidad |
| **H22** | 🆕 **La cifra "NPS de Rimac 20→53" no tiene fuente primaria** y es un caso de eco de cita del mismo tipo que el ROI 100:1 | `abierta` — **directamente relevante para el proyecto**: es una cifra que circula internamente | Rastrear el origen; si aparece en un caso de cliente de vendor, degradarla a 🟠 D |
| **H23** | 🆕 **La ausencia sistemática de una métrica es predictiva**: en cualquier categoría donde todos los actores publiquen métricas de crecimiento y **ninguno** publique retención, la retención será mala | `abierta` — sugerida por vibe coding (cero churn publicado en toda la categoría) y por el service design (cero licitaciones con su nombre en el objeto) | Comparar categorías con y sin publicación de retención contra su supervivencia a 3 años |

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

**Sobre el poder del diseño**

- **C14 — La evidencia causal más fuerte del poder del diseño es sobre su capacidad de daño.** Los
  dark patterns casi cuadruplican la aceptación de un plan dudoso, en experimento aleatorizado con
  muestra representativa, y afectan a todos los grupos —los proxies clásicos de vulnerabilidad
  explican poco. Es el único punto donde la crítica teórica al diseño está empíricamente confirmada.
  **Leído en positivo: el diseño mueve conducta de verdad; lo que está mal probado es que la mueva
  hacia el valor.** ⚠️ **(iter. 2) Con el acotamiento de que no hay réplica en población
  latinoamericana: el "casi 4x" no se puede citar como si aplicara a Perú.**

**Reglas destiladas en la iteración 2** *(las cuatro primeras sobrevivieron a dos corridas: la
iteración 1 las había encontrado como casos sueltos y la 2 les dio mecanismo)*

- ⭐ **C15 — La preferencia declarada no predice el desempeño, y a veces lo contradice.** Cinco
  piezas independientes convergen: devs 19% más lentos creyéndose 20% más rápidos; usuarios que
  prefieren el menú con el que rinden peor; **interfaces mejor puntuadas en atracción con MAYOR carga
  cognitiva medida por EEG**; el efecto estético que se desploma al controlar por fluidez; y la
  usabilidad experimentada confundiendo el juicio estético. **Ninguna decisión de diseño debe
  fundarse solo en preferencia declarada, tests de concepto incluidos.** *(Generaliza C11.)*
- ⭐ **C16 — Antes de creer una métrica de productividad, pregunta si sube por construcción.**
  *Apparent productivity* (output total ÷ esfuerzo) **crece mecánicamente con el reuso**, porque
  cuenta en el numerador lo que no cuenta en el denominador. **Toda métrica de forma "componentes
  entregados ÷ horas", "features por sprint" o "líneas por dev" es de esta familia y no puede falsar
  la hipótesis que dice demostrar.** Exige la versión que cuenta solo lo nuevo.
- ⭐ **C17 — Cuando una disciplina no encuentra su efecto, busca si la disciplina vecina ya lo midió.**
  Treinta años de *software reuse* contestaron la pregunta de los design systems mejor que toda la
  literatura de diseño. **Antes de declarar "no hay evidencia", verifica que no exista con otro
  nombre en otro campo.**
- ⭐ **C18 — La ausencia de un dato que debería existir es un dato.** Nadie en vibe coding publica
  churn mientras todos publican ARR; Accenture retira su métrica de IA justo cuando deja de
  halagarla; no hay una sola licitación pública con "service design" en el objeto. **Donde el dato
  existiría y no aparece, la ausencia es el hallazgo — pero es una señal, no una conclusión: "no
  encontré" nunca equivale a "no existe".**
- **C19 — Distingue *frecuencia aparente* de *conversación real*, y en español descuenta el SEO
  educativo.** Veinte piezas que "cubren el tema" pueden ser una sola pieza de marketing con veinte
  vitrinas. Es el equivalente estructural del churnalism, y en el corpus hispanohablante **domina la
  primera página de resultados**. *(Complementa C4 y C5: descontar por estacionalidad, por incentivo
  del emisor **y por SEO**.)*
- **C20 — Al leer un estudio, verifica a qué brazo pertenece el efecto antes de citarlo.** El error
  más caro de la iteración 1 no fue creer una cifra falsa: fue atribuir una cifra real **al brazo
  experimental equivocado** (§1.bis). En diseños de 3+ brazos, "el estudio encontró −46%" no significa
  nada sin decir *entre qué y qué*.
- **C21 — Dos meta-análisis con el mismo autor senior no son dos confirmaciones.** Son una línea de
  investigación. Si además el estimador se duplica entre uno y otro, y la versión previa declaraba
  sospecha de sesgo de publicación, **el segundo no cierra el caso: lo reabre.**
- **C22 — Adaptar no es el problema; romper la estabilidad espacial sí.** Adaptar a un **rasgo estable
  del usuario** preservando posiciones mejora el desempeño (26% más rápido, 73% más preciso); guiar la
  atención sin mover nada también. **Reubicar según una predicción móvil de intención degrada.** Es la
  pregunta que hay que hacerle a cualquier propuesta de "interfaz que se adapta al usuario".
- **C23 — Para datos latinoamericanos, ir al documento primario o no usar el dato.** Las cifras de la
  región se corrompen en la cadena secundaria en inglés (se documentó un "S/10,3" transcrito como
  "PLN10,3"). Y ningún informe de mercado desagrega diseño: va empaquetado dentro de "IT services".
- **C24 — La pregunta "¿cuál es el ROI del diseño?" es una pregunta situada, no neutra.** La tradición
  latinoamericana (Bonsiepe, colonialidad do fazer, Escobar) sostiene que la hegemonía del Norte opera
  también **sobre el pensamiento que constituye la investigación en diseño**. No es evidencia a favor
  del valor del diseño — **es un correctivo al marco desde el que este node formula sus hipótesis, y
  hay que sostenerlo sin convertirlo en coartada para no medir.**

---

## 8. 📓 Bitácora de iteraciones

| # | Fecha | Foco de la corrida | Qué cambió | Pendiente que hereda la siguiente |
|---|---|---|---|---|
| 1 | 2026-07-26 | Barrido fundacional de 360°: impacto tangible vs. propuesta innovadora, en producto/UX, IA, design systems, servicio y visual | **Creación del node.** 92 fuentes registradas (F-237 a F-328). Escala de madurez (§5) y 14 reglas de criterio (§7) establecidas. Tablero abierto con 18 hipótesis | (a) **H13 es falsable el 5-ago-2026** — Figma reporta Q2; (b) barrido en **español/portugués** (H17), todo lo hallado es anglosajón; (c) **service design** merece pasada propia (H18); (d) leer los preprints de generative UI de primera mano (el proxy bloqueó arXiv); (e) buscar si apareció **replicación independiente** del efecto design systems (H6) |
| 2 | 2026-07-27 | Cierre de los cinco pendientes de la iteración 1: H17 (barrido ES/PT), H18 (service design), H6 (replicación design systems), preprints de generative UI, H11 (incentivo de los amplificadores) | **Se movieron 9 hipótesis y se corrigió el propio node.** 63 fuentes nuevas (F-329 a F-391). ⭐ **H6 respaldada por vía indirecta** desde la literatura de *software reuse* (§2.6) — con el artefacto de *apparent productivity* como hallazgo central. ⭐ **H17 reformulada de "desfase" a "desplazamiento de eje"** (§3.7). ⭐ **H18 respondida con un tercer estado** (§2.10, §4.5). **H11 refutada e invertida** en ES/PT (§3.8). **H3 reformulada** alrededor de la estabilidad espacial (§2.7). **H13, H15 y H16 reformuladas** (§4.6-4.9). **H5 generalizada a H19** con evidencia de EEG (§2.8). 4 hipótesis nuevas (H20-H23) + H6b. **10 reglas de criterio nuevas (C15-C24)** y **§1.bis: dos correcciones de hecho a la iteración 1** (el preprint de Zup no medía design systems; "IDEO −67%" es una cita anónima) | (a) **H13 se falsa el 5-ago-2026** — Figma reporta Q2 con guía de 40% frente a un Q1 real de 46%; baseline fijado en §4.6; (b) **leer el suplemento de Zenodo del meta-análisis de estética** (H21) — es el primer objetivo; (c) leer el ***Service Design Salary(+) Report 2026***, mejor instrumento primario para H18; (d) obtener el **brazo Design-System-solo vs. Manual** del preprint de Zup (H6b); (e) **la pista social quedó sin medir su eje de validación social** (cero upvotes/comentarios leídos) — probar mirrors de Reddit y la **pista audiovisual en español** (TikTok/YouTube), sin explorar; (f) rastrear el **origen del NPS de Rimac 20→53** (H22); (g) revalidar Figma y Credicorp **contra EDGAR** — pendiente por segunda iteración consecutiva |

---

## 9. Limitaciones

### 9.bis Limitaciones de la iteración 2

- 🔴 **El bloqueo de red dejó de ser un accidente y pasó a ser una condición estructural del node.**
  En la iteración 2 el proxy devolvió **403 en el CONNECT** (política de egress, no bot-blocking ni
  fallo transitorio) para **todos** los dominios académicos y financieros relevantes: `arxiv.org`,
  `semanticscholar.org`, `sciencedirect.com`, `link.springer.com`, `dl.acm.org`, `tandfonline.com`,
  `scielo.org`, `redalyc.org`, `openalex.org`, `crossref.org`, `scholar.google.com`,
  `researchgate.net`, `pmc.ncbi.nlm.nih.gov`, `sec.gov`, `wikipedia.org`, y en la pista social además
  `reddit.com`, `medium.com`, `substack.com` y varios medios en español. **Consecuencia
  epistemológica que hay que propagar a toda lectura de este node: en la iteración 2 no se leyó de
  primera mano ni un solo paper, preprint ni filing.** Todo pasó por el resumidor de búsqueda.
- ⚠️ **Autoría no verificada en ~8 fuentes** (la SLR de reuso 2024, el artículo de *AI & Society* sobre
  Bonsiepe, las dos revisiones de codiseño, la SLR de MDPI, el preprint de Zup y la lista completa de
  coautores de dos papers). **No se inventó ningún nombre**; donde el node atribuye autoría es porque
  el nombre apareció asociado al título en al menos dos resultados independientes.
- 🔴 **La pista social quedó con su eje distintivo sin medir.** Cero upvotes, comentarios, vistas o
  shares contados de primera mano. **Todo lo que el node dice sobre "tono" en ES/PT viene de titulares
  y snippets, no de leer respuestas de personas reales.** El eje de *validación social* —lo único que
  distingue a esa pista de un resumen de prensa— quedó, por segunda iteración, medido con confianza
  baja. **La pista audiovisual en español (TikTok/YouTube/Instagram), que es donde probablemente vive
  la validación social real en LatAm, está prácticamente sin explorar.**
- ⚠️ **El muestreo de la auditoría de H11 es por visibilidad en buscador, no por audiencia** — lo que
  sesga precisamente hacia quien invierte en SEO. Que ese sesgo *sea* el hallazgo no lo vuelve un
  muestreo representativo de los mayores amplificadores.
- ⚠️ **Los dos lados de H18 se midieron con instrumentos incomparables**: la caída con una serie
  temporal de un agregador; la absorción in-house con avisos de empleo sueltos. **Y el dato de la
  serie tiene 14 meses de antigüedad** (corte may-2025) porque el sitio quedó bloqueado: no se sabe
  qué pasó en 2026.
- ⚠️ **Cobertura geográfica todavía parcial:** la pista ES/PT cubrió España, Brasil, México,
  Argentina, Chile y Perú, pero **no** Colombia ni Centroamérica con profundidad, y **no** se accedió
  a las comunidades cerradas (WhatsApp/Facebook) donde vive buena parte de la conversación gremial
  peruana. **La ausencia de conversación peruana debe leerse como "no públicamente indexable", no como
  "no existe".**
- ⚠️ **Sin acceso a bases indexadas** (Scopus, Web of Science, ACM DL completo) ni de venture
  (PitchBook, Crunchbase), igual que en la iteración 1.

### 9.ter Limitaciones de la iteración 1

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
- [[seguros-comportamiento-mundo-peru|Comportamiento, percepción y valoración frente a seguros
  (Mundo vs. Perú)]] — H8 conecta los dark patterns con la causa #1 de desconfianza en seguros en
  Perú (falta de información), que es un hallazgo central de ese node.
- [[modelo-personas-sinteticas|Modelo de personas sintéticas (lapuerta)]] — H9 (brecha
  actitud-conducta en diseñadores) es estructuralmente el mismo fenómeno que la variable
  `disposicion_compartir_datos_pricing` del modelo: desconfianza abstracta declarada ≠ conducta real.
- [[proyecto-back-to-basics-ffvv-vida|Proyecto Back to Basics — FFVV Vida Individual]] — C1 y C2
  (argumentar por mecanismo, prometer acumulación) aplican a cómo se sustenta el valor del rediseño
  de la experiencia de venta ante el VP. **(iter. 2)** C15 se le suma como restricción dura: los
  tests de concepto con asesores miden preferencia declarada, que **no predice** desempeño.
- **(iter. 2)** [[modelo-salud-ia-farmacias-peru|Modelo de triage IA + farmacias + atención humana]] —
  el hallazgo de §3.9 es directamente operativo para ese node: el **Decreto Supremo 090-2026-PCM**
  incorpora formalmente la innovación pública al Sistema de Modernización de la Gestión Pública, y el
  Concurso Nacional de Buenas Prácticas en Calidad de Servicios 2026 de la PCM es una vía de entrada
  institucional. **Y §2.10 es la advertencia que lo acompaña: el codiseño en salud tiene un déficit
  documentado de evaluación de outcomes (2 de 14.376 reportes), así que ese node debe medir
  resultados, no proceso — que es exactamente lo que su marco RE-AIM ya exige.**
