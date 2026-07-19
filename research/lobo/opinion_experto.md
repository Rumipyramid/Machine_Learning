# 🐺 El Lobo — Opinión de negocio acumulada

> No vengo a resumir papers. Vengo a decir dónde hay plata, dónde se quema plata,
> y qué jugada haría yo con lo que el `cronista` ya verificó. Cada tesis carga su
> evidencia (F-n del ledger `research/fuentes/registro_fuentes.md`) y un nivel de
> confianza que sube o baja según la rigurosidad de lo que la sostiene. Lo que no
> tiene fuente en el ledger va marcado como **instinto** — razonado desde
> principios de negocio, no dato verificado.
>
> Creado: 2026-07-12.

## 🎯 Tesis vigentes

### 1. La divulgación ("explicar mejor") es una palanca de conversión débil — no de crecimiento
Dos fuentes A independientes (RCT de campo con ~124k usuarios reales + síntesis
académica canónica) muestran lo mismo: mejorar la comprensión del consumidor casi
nunca cambia su conducta de compra. Un glosario, una guía o un "explicador" suben
el conocimiento, no la conversión. Si el negocio mide éxito de un glosario en
ventas, está midiendo la métrica equivocada.
- **Evidencia:** F-9 (🟢A, RCT N≈124,000), F-10 (🟢A, síntesis canónica)
- **Confianza:** Alta
- **Actualizado:** 2026-07-12

### 2. El coaseguro variable es el cuello de botella de comprensión #1 en seguros de salud
Dos estudios (uno con dos encuestas representativas EE.UU., otro con encuesta
nacional del regulador de salud) coinciden: el coaseguro es el término peor
entendido, y quien tiene un plan con coaseguro/tarifas variables subestima sus
costos reales por un margen mucho mayor que quien tiene deducible fijo. Esto no es
un problema de comunicación — es un problema de diseño de producto.
- **Evidencia:** F-6 (🟢A, Loewenstein et al. 2013), F-7 (🔵B, KFF 2017)
- **Confianza:** Alta
- **Actualizado:** 2026-07-12

### 3. El problema de comprensión es estructural, no generacional — no lo resuelve "educar a los jóvenes"
Solo ~1 de cada 4 adultos Gen Z en EE.UU. puede definir deducible o copago. Cruzado
con la tesis 1 y 2, el patrón es consistente: ni la generación más "nativa digital"
entiende los términos base, y aunque los entendiera, eso no predice que compre.
Cualquier estrategia que apueste a "la próxima generación va a entender mejor" no
tiene sustento.
- **Evidencia:** F-8 (🟡C, NAIC 2024 — nota de asociación, método no detallado)
- **Confianza:** Media (una sola fuente C; consistente con F-6/F-7 pero no del
  mismo rigor). **Tope explícito** (mismo criterio aplicado a tesis 4 el
  2026-07-13): no sube a Alta por consistencia narrativa con F-6/F-7 — solo
  sube si aparece un F-n con rigurosidad B o mejor que confirme el patrón
  generacional, idealmente con dato peruano/latinoamericano en vez de EE.UU.
- **Actualizado:** 2026-07-17

### 4. La brecha de aseguramiento sísmico en Perú es una categoría de producto casi vacía
Solo ~3.3% de los hogares peruanos tiene seguro contra sismos/desastres en un país
de altísima exposición sísmica. El dato circula vía prensa citando a APESEG (el
gremio del sector — incentivo a dramatizar la brecha para pedir regulación
favorable), no vía fuente primaria auditada directamente.
- **Evidencia:** F-5 (🟠D, Infobae vía APESEG)
- **Confianza:** Media — la dirección del hallazgo (brecha enorme) es creíble y
  consistente con la baja penetración general del mercado peruano, pero el número
  exacto no está verificado en fuente primaria. Antes de dimensionar un caso de
  negocio con el 3.3%, pedir el dato directo de APESEG/SBS. **Tope explícito:**
  esta tesis se sostiene en una única fuente D — no sube a Alta por consistencia
  narrativa; solo sube si aparece un F-n con rigurosidad B o mejor que confirme el
  número directamente desde APESEG/SBS.
- **Actualizado:** 2026-07-13

### 5. ESG como diferenciador de marca: aplica al consumidor global premium, no está probado en Perú
Bain reporta que ~80% de consumidores globales quiere criterios ESG integrados en
sus seguros. Es una encuesta propia de consultora (no auditable) y de alcance
global — extrapolarla al consumidor peruano medio (con problemas de tenencia
básica, no de diferenciación ESG) es **instinto**, no dato.
- **Evidencia:** F-4 (🟡C, Bain & Company 2023, alcance global)
- **Confianza:** Baja para el mercado peruano específicamente
- **Actualizado:** 2026-07-12

### 6. La era del "nudge de catálogo" terminó — testear en la propia población es el estándar, no copiar el tamaño de efecto de un paper
El meta-análisis fundacional pro-nudge (447 experimentos) fue revertido por un
re-análisis bayesiano que corrige sesgo de publicación: ajustado, no queda
evidencia de un efecto promedio del nudging. Con datos reales a escala (123+ RCTs
administrativos, >20M personas) el efecto que sobrevive ronda ~1.4 puntos
porcentuales, muy por debajo del ~8.7pp que reportan los papers académicos — un
"voltage drop" de ~6x entre laboratorio y despliegue real. Un meta-análisis de
segundo orden matiza esto: hay impacto, pero es menor y muy heterogéneo por
dominio/técnica, no un cero absoluto. Esto extiende la tesis 1: no solo la
divulgación es una palanca débil — el nudge genérico importado de un paper también
lo es, salvo que se valide en la propia base de usuarios.
- **Evidencia:** F-16 (🟢A, meta-análisis original), F-17 (🟢A, re-análisis que lo
  revierte), F-18 (🟢A, matiza: efecto real pero heterogéneo), F-20 (🟢A, megastudy
  como metodología correcta: testear muchas variantes a la vez, en casa), F-21
  (🟢A, voltage drop cuantificado). Contrapeso a mirar con cautela: F-26 (🟡C,
  McKinsey reporta +10% retención en nudge units corporativas) es un caso de
  consultora, no auditable — no pesa contra la evidencia A de arriba.
- **Confianza:** Alta
- **Actualizado:** 2026-07-12

### 7. El diseño de producto embebido (s-frame) gana sobre el nudge cosmético (i-frame)
El campo se desvió priorizando soluciones a nivel individual (recordatorios,
defaults, copy) sobre el rediseño estructural del producto. El caso con outcome
telemático real (no autoreportado) lo prueba: seguros por uso (UBI) redujeron
velocidad 11-13%, frenadas bruscas 16-21% y aceleraciones agresivas 16-25% —
conducta cambiada por el diseño del producto (pricing dinámico + feedback), no por
un mensaje. Es la misma lógica de la tesis 2: la palanca de mayor ROI es rediseñar
el producto (coaseguro fijo, pricing por uso), no explicarlo mejor.
- **Evidencia:** F-19 (🟢A, marco teórico i-frame/s-frame, canónico), F-23 (🟢A,
  RCT de campo nacional con outcome telemático objetivo)
- **Confianza:** Alta
- **Actualizado:** 2026-07-12

## 💰 Oportunidades

- **Producto paramétrico de bajo costo contra sismos.** Categoría con ~96.7% de
  hogares sin cobertura (tesis 4) en un país donde SOAT —un seguro obligatorio de
  bajo entendimiento y alto conocimiento (94%, F-1)— ya probó que la distribución
  masiva funciona cuando el producto es simple y el precio es bajo. Jugada:
  bundling o cross-sell sobre la base de SOAT, no venta desde cero.
- **Rediseñar el producto, no el glosario.** Si el coaseguro variable es el
  problema (tesis 2) y la divulgación no cambia conducta (tesis 1), la jugada de
  mayor ROI es lanzar variantes con deducible fijo y simuladores de costo en el
  punto de venta — no otro explicador. Esto convierte un hallazgo académico en
  ventaja de producto frente a competidores que siguen invirtiendo en "educar".
- **Distribución por bróker/intermediario para superar desconfianza.** *Instinto,
  no ledger-backed todavía*: en mercados de baja confianza institucional, la
  intermediación humana suele convertir mejor que el canal digital directo. Vale
  la pena que `seeker` o `marketer` busquen evidencia dura (tasa de conversión
  bróker vs. digital en Perú) antes de apostarle presupuesto.
- **Pricing dinámico por uso (UBI) como producto, no como campaña de nudge.**
  Tesis 7 lo prueba con outcome real: telemática + feedback + precio variable
  cambia la conducta de manejo de forma medible. Jugada: extender la lógica UBI
  más allá de auto (salud, hogar) donde exista dato de uso, en vez de invertir en
  otra campaña de comunicación sobre manejo seguro.
- **Posicionar `lapuerta` en la frontera de "AI Behavioral Science".** La agenda
  formal del subcampo (agentes sintéticos, simulación conductual con IA) recién se
  está formando, con autores de primer nivel detrás (F-27, aunque todavía
  preprint sin peer review). `lapuerta` ya hace exactamente eso. *Instinto, no
  ledger-backed como oportunidad de negocio*: hay ventana para posicionar el
  trabajo como caso aplicado temprano antes de que el subcampo se sature — vale
  que `seeker` monitoree este preprint hacia su publicación final.

## ⚠️ Riesgos

- **Quemar presupuesto de marketing en "educación financiera" esperando ventas.**
  Es el error más respaldado por evidencia del ledger (tesis 1, dos fuentes A). Si
  el objetivo real es conversión, ese presupuesto rinde más en simplificación de
  producto o en el canal de bróker.
- **Lanzar producto Gen Z con coaseguro variable pensando que "ya van a entender".**
  Tesis 2 + 3 combinadas: ni el consumidor promedio ni el más joven entienden el
  coaseguro. Ese diseño produce fricción, quejas y probable lapse/churn temprano.
- **Dimensionar un caso de negocio de seguros de desastres con el 3.3% sin
  verificar la fuente primaria.** Es un número de gremio (APESEG) vía prensa (D),
  no auditado. Usarlo para levantar capital o justificar inversión sin
  confirmación directa es un riesgo de credibilidad si el número no resiste
  escrutinio.
- **F-15 sigue marcada "NO USAR" en el ledger** (cifra de UnitedHealth sin método
  verificable, ~9% entiende términos básicos). Cuidado con que se cuele en algún
  deck o caso de negocio — no tiene respaldo.
- **Dimensionar el ROI de un nudge con el tamaño de efecto de un paper académico.**
  Tesis 6: el "voltage drop" es ~6x (1.4pp de campo vs 8.7pp de laboratorio).
  Cualquier caso de negocio de una nudge unit interna debe presupuestar con el
  número de campo, no con el del paper que lo inspiró — si no, el forecast de
  retorno queda sobreestimado desde el día uno.
- **Confiar en estudios de "honestidad"/nudges éticos sin verificar su
  integridad.** El escándalo Ariely/Gino (F-24) mostró fabricación de datos en
  investigación de honestidad ampliamente citada por la industria de seguros
  (declaraciones juradas, formularios de siniestros, firma-al-inicio vs.
  firma-al-final). Antes de citar un estudio de honestidad conductual para
  diseñar un formulario o proceso antifraude, verificar que no sea parte del
  corpus retractado — es un riesgo de credibilidad tan serio como F-15.
- **Tratar los resultados de Vitality (F-25) como evidencia dura.** Es dato
  autoreportado corporativo sin auditoría externa (🟠D) — misma categoría de
  fragilidad que F-15/F-5. Útil como benchmark direccional de "shared-value
  insurance" (76% menor mortalidad en miembros engaged, +15% en manejo), pero no
  como input numérico de un caso de negocio.
- **La tenencia de seguros de vida en EE.UU. cayó de 63% (2011) a 51% (2024)**
  pese a que las intervenciones de comprensión sí mejoran el journey de compra
  puntual (F-22, 🟡C). Refuerza la tesis 1 en la dirección más incómoda: mejorar
  el entendimiento en el punto de venta no basta para sostener ni crecer la
  categoría a nivel agregado.
- **La cartera de tesis lleva 4 revisiones diarias seguidas sin insumo nuevo.**
  *Instinto, no ledger-backed*: ninguna tesis está siendo puesta a prueba por
  evidencia activa ahora mismo — este archivo es un snapshot con fecha de
  vencimiento implícita, no una fuente viva. Si se va a apalancar una decisión
  de negocio grande (pricing, entrada a categoría, pitch a inversionista) sobre
  tesis 3 o 4 —las dos más frágiles del set—, correr `/seeker` o `/marketer`
  antes de usarlas, no asumir que "nadie las refutó" equivale a "siguen firmes".
- **Esperar pasivamente a que aparezca evidencia nueva ya no es gratis — pero
  seguir pidiendo `/seeker`/`/marketer` cada día tampoco lo es.** *Instinto*: con
  siete días seguidos sin corridas de `/seeker`, `/gossip`, `/marketer` ni
  `/trinidad` desde el 2026-07-12, insistir a diario en encargar esas búsquedas
  sin que nadie las ejecute es una jugada que ya rindió lo que tenía que rendir
  (dejar la brecha visible) y ahora solo repite la misma nota. El checkpoint
  natural más cercano ya está en el propio códice: el reporte quincenal
  automatizado de `cerrajero`/GitHub Action tiene su próxima corrida programada
  para **2026-07-21** (ver índice en `CLAUDE.md`) — es el punto donde
  razonablemente puede entrar evidencia nueva sin depender de que alguien
  encargue manualmente `/seeker` sobre Gen Z peruano (tesis 3) o el dato primario
  APESEG/SBS (tesis 4). Hasta esa fecha, tesis 3 y 4 siguen **congeladas en
  Media** y esta bitácora puede dejar de repetir la misma llamada a la acción a
  diario — el siguiente chequeo con sustancia real es el 21, no mañana.

## 📔 Bitácora

- **2026-07-12** — Primera creación de la opinión. Revisé las 15 fuentes del
  ledger (`registro_fuentes.md`, F-1 a F-15). Construí 5 tesis iniciales: (1)
  la divulgación no convierte, (2) el coaseguro es el cuello de botella de
  comprensión, (3) el problema es estructural/no generacional, (4) la brecha
  sísmica peruana es una categoría casi vacía, (5) ESG es palanca global, no
  probada en Perú. Marqué 3 oportunidades y 4 riesgos, incluyendo la advertencia
  de no usar F-15. Sin entradas previas contra las cuales comparar — este es el
  punto de partida.
- **2026-07-12** — El ledger creció de F-15 a F-27 (investigación `/trinidad`
  sobre behavioral design, volcada en `research/behavioral_design_360.md`).
  Novedad sustancial: la "crisis del nudge" (F-16/F-17/F-18/F-21) — el
  meta-análisis fundacional pro-nudge fue revertido por un re-análisis que
  corrige sesgo de publicación, y el "voltage drop" de campo vs. laboratorio es
  ~6x. Sumé tesis 6 (nudge de catálogo ya no es apuesta segura) y tesis 7
  (diseño de producto embebido/s-frame gana sobre nudge cosmético, con el caso
  UBI de F-19/F-23). Agregué 2 oportunidades (UBI como producto extensible,
  posicionar `lapuerta` en la frontera de "AI behavioral science" vía F-27) y 4
  riesgos (sobreestimar ROI de nudge con cifra de paper, citar estudios de
  honestidad sin chequear el corpus retractado de Ariely/Gino en F-24, tratar
  Vitality/F-25 como dato duro, y la caída de tenencia de vida en EE.UU. pese a
  mejor comprensión en F-22 — refuerza tesis 1). Ninguna tesis 1-5 cambió de
  confianza; la evidencia nueva no las contradice, las extiende.
- **2026-07-13** — Sin cambios sustanciales: el ledger sigue en F-1 a F-27, sin
  fuentes nuevas desde la entrada anterior. Revisé las 7 tesis contra la rúbrica
  de rigurosidad; ninguna cambia de nivel de confianza. Único matiz aplicado:
  hice explícito en la tesis 4 (brecha sísmica) que su confianza Media tiene un
  tope duro por depender de una sola fuente D (F-5, prensa vía APESEG) — no debe
  subir a Alta por mera consistencia narrativa con la baja penetración general,
  solo por una fuente B o mejor que confirme el dato directo del gremio/regulador.
  Las tesis 6 y 7 (crisis del nudge, s-frame > i-frame) siguen siendo las más
  accionables y mejor blindadas (evidencia A múltiple y convergente); tesis 3 y 4
  siguen siendo las más frágiles (una sola fuente C/D cada una) y son las
  candidatas naturales para la próxima ronda de `/seeker` o `/marketer`.
- **2026-07-14** — Sin cambios sustanciales: el ledger permanece en F-1 a F-27,
  sin fuentes nuevas registradas desde la revisión anterior. Repasé las 7 tesis
  contra la rúbrica de rigurosidad; ninguna cambia de nivel de confianza — el
  conjunto de evidencia que las sostiene no varió. Confirmo que tesis 3 (Gen Z,
  una sola fuente 🟡C) y tesis 4 (brecha sísmica, una sola fuente 🟠D con tope
  explícito) siguen siendo las más frágiles: tesis 3 necesita una segunda fuente
  independiente que confirme el patrón generacional fuera de EE.UU. (idealmente
  Perú), y tesis 4 necesita el dato directo de APESEG/SBS en vez de la cifra vía
  prensa. Ninguna otra tesis, oportunidad o riesgo requiere matiz hoy; las 7
  tesis, 5 oportunidades y 7 riesgos vigentes siguen representando bien la
  evidencia disponible en el ledger.
- **2026-07-15** — Sin cambios sustanciales: tercer día consecutivo con el
  ledger fijo en F-1 a F-27 — no hay corrida nueva de `/seeker`, `/gossip`,
  `/marketer` ni `/trinidad` desde el 2026-07-12. Repasé las 7 tesis, 5
  oportunidades y 7 riesgos contra la rúbrica; ninguna cambia de nivel de
  confianza. La racha de "sin novedad" en sí misma es una señal para el
  negocio, no solo un no-evento: tesis 3 y 4 llevan ya tres revisiones seguidas
  marcadas como las más frágiles del set sin que nadie haya cerrado el hueco
  (segunda fuente generacional fuera de EE.UU. para tesis 3; dato primario
  APESEG/SBS para tesis 4). Instinto: si ningún otro skill va a levantar esa
  evidencia pronto, más vale bajar la prioridad de cualquier caso de negocio
  que dependa hoy del 3.3% de tesis 4 y tratarlo explícitamente como
  provisional, en vez de dejarlo languidecer en confianza "Media" indefinida.
  No se tocó ninguna cifra ni fuente — es una nota de gestión de la cartera de
  tesis, no un cambio de evidencia.
- **2026-07-16** — Sin cambios sustanciales: cuarto día consecutivo con el
  ledger fijo en F-1 a F-27 — sin corridas nuevas de `/seeker`, `/gossip`,
  `/marketer` ni `/trinidad` desde el 2026-07-12. Repasé las 7 tesis, 5
  oportunidades y 7 riesgos contra la rúbrica; ninguna cambia de nivel de
  confianza. Convertí la observación de ayer sobre la racha de "sin novedad"
  en un riesgo explícito de la cartera (nuevo bullet en ⚠️ Riesgos, marcado
  instinto): esta opinión es un snapshot con vencimiento implícito, y las
  tesis 3 (Gen Z, una sola fuente 🟡C) y 4 (brecha sísmica, una sola fuente
  🟠D con tope explícito) no deben tratarse como validadas por el mero hecho
  de que nadie las refutó en cuatro días — si alguna va a sostener una
  decisión grande de negocio, corresponde correr `/seeker` o `/marketer`
  antes de usarla tal cual está. No se tocó ninguna cifra ni fuente.
- **2026-07-17** — Sin cambios sustanciales: quinto día consecutivo con el
  ledger fijo en F-1 a F-27 — sin corridas nuevas de `/seeker`, `/gossip`,
  `/marketer` ni `/trinidad` desde el 2026-07-12. Repasé las 7 tesis, 5
  oportunidades y 7 riesgos contra la rúbrica; ninguna cambia de nivel de
  confianza. Único matiz aplicado hoy: extendí a la tesis 3 (Gen Z) el mismo
  tope explícito que ya tenía la tesis 4 (brecha sísmica) desde el
  2026-07-13 — ambas son las tesis más frágiles del set (una sola fuente
  🟡C/🟠D cada una) y ninguna debe subir de confianza por mera consistencia
  narrativa con otras tesis; solo sube con una fuente B o mejor que confirme
  el hallazgo de forma directa. No se sumó ningún riesgo nuevo: la racha de
  estancamiento del ledger (ya señalada como riesgo el 2026-07-16) sigue
  siendo la observación de portafolio más relevante — cinco días sin
  evidencia nueva es la señal en sí misma, no solo la ausencia de una.
- **2026-07-18** — Sin cambios sustanciales: sexto día consecutivo con el
  ledger fijo en F-1 a F-27 — sin corridas nuevas de `/seeker`, `/gossip`,
  `/marketer` ni `/trinidad` desde el 2026-07-12. Repasé las 7 tesis, 5
  oportunidades y 7 riesgos contra la rúbrica; ninguna cambia de nivel de
  confianza. Cambié el tono del riesgo de estancamiento: ya no es solo una
  observación de portafolio, es una llamada a la acción concreta — encargar
  `/seeker` sobre comprensión de seguros en Gen Z/millennials peruanos (cierra
  tesis 3) y el dato primario de APESEG/SBS sobre penetración sísmica (cierra
  tesis 4), en vez de seguir revisando el mismo ledger esperando que cambie
  solo. Formalicé que tesis 3 y 4 quedan **congeladas en Media** hasta que
  llegue esa evidencia — no suben por antigüedad ni por repetición de la
  revisión diaria. Bitácora dentro de la ventana de ~30 días; no hubo entradas
  que podar.
- **2026-07-19** — Sin cambios sustanciales: séptimo día consecutivo con el
  ledger fijo en F-1 a F-27 — sin corridas nuevas de `/seeker`, `/gossip`,
  `/marketer` ni `/trinidad` desde el 2026-07-12. Repasé las 7 tesis, 5
  oportunidades y 7 riesgos contra la rúbrica; ninguna cambia de nivel de
  confianza. Único matiz aplicado: reformulé el riesgo de estancamiento — pedir
  `/seeker`/`/marketer` cada día sin que nadie los ejecute ya no aporta señal
  nueva, así que fijé un checkpoint concreto en vez de repetir el llamado a
  diario: el códice (`CLAUDE.md`) ya tiene programada la próxima corrida del
  reporte quincenal automatizado (`cerrajero`) para **2026-07-21**, que es donde
  razonablemente puede entrar evidencia fresca sobre el sector. Tesis 3 y 4
  siguen **congeladas en Media** hasta esa fecha; esta bitácora no repetirá la
  misma advertencia de "sin novedad" cada 24h si el 21 tampoco trae nada — a
  partir de entonces corresponde una evaluación distinta (por ejemplo, si
  siguen sin cerrarse, degradarlas fuera de "tesis vigentes" en vez de
  mantenerlas indefinidamente en Media). Bitácora dentro de la ventana de ~30
  días; no hubo entradas que podar.
