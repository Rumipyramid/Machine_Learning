# Escalamiento a humano en flujos de bot: ¿el usuario estresado atraviesa las opciones hasta llegar a una persona?

> Documento de investigación. Fuente persistente y versionada en el repositorio.
> Fecha de elaboración: 2026-08-19 · Versión: v1.0
> Origen: `/seeker` — investigación de espectro amplio (empírico + teórico/crítico)

---

## 0. Veredicto inicial

**Parcialmente cierto, y la parte que se cree mejor sustentada es justo la que no está
medida.** El atajo al humano existe, está cuantificado y hasta está legislado. La
preferencia por un humano sí se desplaza con la carga emocional del problema. Pero
"**ignorando las opciones**" —la idea de que el estrés produce una especie de ceguera al
menú— **no tiene medición directa en la literatura de servicio**, y el mecanismo
psicológico que se suele invocar para explicarla (estrés → conducta habitual) **falló dos
replicaciones exactas preregistradas** (F-476).

La explicación que sí aguanta la evidencia disponible es menos dramática y más útil:
no es ceguera, es **un guion aprendido**. Veinte años de menús telefónicos enseñaron que
el valor esperado de leer las opciones es bajo, y el usuario ejecuta el atajo que ya
conoce. El estrés no ciega: **acelera el abandono de una vía que ya se descontaba como
mala**.

---

## 1. El claim tiene tres proposiciones, no una

| # | Proposición | Tipo | Estado |
|---|---|---|---|
| **P1** | Quien quiere un humano intenta saltarse el flujo del bot | empírico-cuantitativo | ✅ **Documentado** |
| **P2** | El estrés/enojo desplaza la preferencia hacia el humano | empírico-causal | ✅ **Documentado, pero condicional** |
| **P3** | Lo hace **ignorando las opciones** (no las procesa) | empírico-causal (cognitivo) | ⚠️ **No medido; mecanismo canónico refutado** |

⚠️ Nótese además que la formulación original une con "o" dos condiciones muy distintas:
"si está estresado **o** busca ayuda humana". La segunda rama es **casi tautológica**
(quien busca un humano, busca un humano). El contenido empírico real del claim está en la
primera rama y en P3.

---

## 2. Lo que sí está documentado

### 2.1 El atajo existe y está cuantificado (P1)

- **70%** de quienes llaman a empresas han intentado **marcar cero** para saltarse el menú,
  y **72%** termina "siempre o frecuentemente" hablando con un humano después de encontrar
  un IVR; **88%** prefiere de entrada un agente en vivo (Clutch, 2019 — F-471; encuesta
  N=501 EE.UU.).
- **Solo 14%** de los problemas de servicio se resuelven **completamente** en autoservicio,
  aun cuando **73%** de los clientes pasan por autoservicio en algún punto de su journey; e
  incluso entre problemas que el propio cliente califica de "muy simples", solo **36%** se
  resuelve ahí (Gartner, 2024 — F-472; encuesta N=5.728, dic-2023).
- El patrón **antecede a los chatbots**: el 57% de quienes llaman ya intentaron resolverlo
  solos en la web antes (Dixon, Toman & DeLisi, 2013 — F-491), y el catálogo canónico de
  fallas de autoservicio (Meuter et al., 2000 — F-490, 800+ incidentes críticos) ya
  documentaba el mismo desenlace.

### 2.2 La emoción sí desplaza la preferencia hacia el humano (P2)

- **El hallazgo más fuerte y más directo**: cuando el cliente entra **enojado** a una
  interacción con chatbot, antropomorfizar el bot (nombre, avatar, "yo siento…") **daña**
  la satisfacción, la evaluación de la empresa y la intención de compra — efecto que **no
  aparece** en clientes no enojados (Crolic, Thomaz, Hadi & Stephen, 2022 — F-469; datos de
  campo de una telco internacional + 4 experimentos, *Journal of Marketing*). El mecanismo
  propuesto es de **expectativas**: el bot humanizado promete una eficacia que no cumple, y
  el enojado ya llega con expectativas infladas.
- La aversión al algoritmo es **dependiente de la tarea**: se rechaza más en tareas
  percibidas como **subjetivas** que objetivas (Castelo, Bos & Lehmann, 2019 — F-481), y en
  salud opera la **negligencia de unicidad** — el temor a que la IA no contemple lo que mi
  caso tiene de particular (Longoni, Bonezzi & Morewedge, 2019 — F-482).
- En manejo de **reclamos**, los consumidores prefieren agente humano incluso después de
  que el chatbot resolvió bien; y prefieren un traspaso **temprano e iniciado por el
  usuario** antes que uno tardío disparado por la frustración (Chacon &
  Martínez-Troncoso, 2026 — F-486; 4 estudios preregistrados).
- El rasgo **necesidad de interacción humana** modera la relación: cuanto más alta, más
  pesa el trato humano del canal (Sheehan, Jin & Gottlieb, 2020 — F-499). Es un rasgo
  **estable de la persona**, no un estado emocional del momento — matiz que el claim borra.
- Ante una falla del bot, las estrategias de afrontamiento documentadas incluyen
  explícitamente la **búsqueda de apoyo expresivo** junto con afrontamiento activo,
  aceptación y retiro (Information Technology & People, 2024 — F-488; 23 entrevistas), y la
  secuencia frustración→agresión hacia la marca está descrita cualitativamente (Ozuem et
  al., 2024 — F-487; 47 entrevistas en 4 países).

### 2.3 Escalar tarde cuesta caro (el corolario operativo)

En un experimento de campo aleatorizado en Taobao/Alibaba, la intervención humana
**preserva la calidad en escalamientos técnicos** pero es **mucho menos efectiva en
escalamientos emocionales**: +40,8% de duración del chat, +6 puntos porcentuales de
reintento y **−0,928 puntos** en la calificación del cliente, porque la intervención llega
**después** de que la frustración se acumuló (Wang, Zhu, Feng, Lu & Jia, 2026 — F-470;
⚠️ preprint, sin revisión por pares).

⭐ **Esto es lo más accionable de toda la investigación**: la pregunta de diseño no es *si*
el usuario va a llegar al humano, sino *en qué punto de su curva de frustración* llega.

### 2.4 Corroboración regulatoria (conducta tan extendida que se legisla)

- **Perú — OSIPTEL (2023)**: los asesores virtuales (telefónicos o web) **deben estar
  configurados para transferir al usuario a un asesor humano en cualquier etapa** de la
  atención. Vigente desde el **1-abr-2023** para móvil, fija, internet y TV paga (F-473).
- **España — Ley 10/2025 de Servicios de Atención a la Clientela**: prohíbe basar la
  atención **exclusivamente** en bots; si el cliente lo pide, el traspaso a persona debe ser
  inmediato y efectivo. En vigor desde 28-dic-2025, con adaptación hasta 28-dic-2026 (F-474).

⚠️ Ojo con la inferencia: la regulación prueba que el **problema** es masivo y políticamente
visible, **no** prueba el mecanismo cognitivo de P3.

### 2.5 El dato peruano

- Neo Consulting (Perú, N=270): el chatbot es apenas el **4.º canal** de atención más usado
  (**18%**), detrás de llamada telefónica (**59%**) y WhatsApp (**54%**) — F-494. ⚠️ Cifra
  de consultora, conocida solo por cobertura secundaria; registrada con descuento.
- El regulador peruano legisló el traspaso obligatorio a humano (F-473), lo que sitúa a
  Perú **antes** que España en este punto específico.

---

## 3. Lo que es interpretación o teoría (y de quién es)

Cuatro marcos explican el fenómeno mejor que la intuición de "el estrés lo ciega", y
conviene atribuirlos en vez de presentarlos como consenso:

- **Suchman (1987), *Plans and Situated Actions*** (F-478). La tesis canónica del campo: la
  máquina asume que el usuario ejecuta **un plan**; el usuario, en realidad, actúa
  **situadamente** y trae el plan a colación según las circunstancias. El menú no falla
  porque el usuario esté nervioso, falla porque **el modelo de interacción de la máquina es
  falso de origen**. Es el argumento más fuerte disponible para P3 — y es teórico, no
  empírico.
- **De Certeau (1980), *La invención de lo cotidiano*** (F-479). El "marcar cero" es
  literalmente una **táctica** en su sentido técnico: el débil no puede rediseñar el
  sistema (eso sería *estrategia*), solo puede **desviarlo desde adentro**. Explica por qué
  el atajo se transmite socialmente como un truco, no como un uso previsto.
- **Reeves & Nass (1996), CASA / *The Media Equation*** (F-492). La gente aplica reglas
  sociales a las máquinas de forma automática. Es el marco que hace inteligible por qué
  humanizar un bot **empeora** las cosas con un cliente enojado (F-469): activa expectativas
  sociales que el bot no puede honrar.
- **Easterbrook (1959), hipótesis de utilización de claves** (F-477). Alto arousal → se
  estrecha el rango de claves atendidas ("visión de túnel" atencional). Es el respaldo
  teórico clásico de P3 — **pero es de 1959, de laboratorio, y no se ha probado en flujos
  conversacionales de servicio**. Citarlo como si demostrara P3 sería sobre-extender el
  dominio de la teoría.

---

## 4. Lo que no cuadra

### 4.1 "Ignorando las opciones" no está medido

Ninguna fuente localizada mide la cadena causal completa **estrés → no procesa el menú →
atraviesa el flujo**. Lo que sí hay:

- Métricas de industria (*zero-out rate*, *opt-out rate*) que **cuentan el resultado**, no
  el estado mental que lo produce.
- El límite de memoria de trabajo en menús hablados (3-4 opciones antes de que el usuario
  deje de retenerlas) es una **restricción estructural del canal**, presente con o sin
  estrés.
- Análisis de conversaciones reales (Martijn, van Hooijdonk, Hoeken & Kunneman, 2026 —
  F-489; 200 conversaciones de un chatbot de transporte público neerlandés) muestran que el
  redireccionamiento a humano se concentra en peticiones **transaccionales**, no en
  usuarios alterados. El predictor observado es **el tipo de tarea**, no la emoción.
- Cuando se les pregunta directamente, los usuarios **prefieren** que el bot ofrezca
  opciones y explicaciones ante una ruptura, porque son accionables (Ashktorab, Jain,
  Liao & Weisz, 2019, CHI — F-493). Es decir: en el agregado **no rechazan las
  opciones**; lo que rechazan son opciones que no llevan a ningún lado.

### 4.2 El mecanismo psicológico más citado no replicó

El puente teórico habitual —el estrés desplaza la conducta de dirigida-a-meta a
**habitual** (Schwabe & Wolf, 2009, *J. Neuroscience* — F-475)— **no sobrevivió a dos
replicaciones exactas preregistradas** (Smeets, Ashton, Roelands & Quaedflieg, 2023,
*Neurobiology of Stress* — F-476): pese a inducción de estrés exitosa (subjetiva y
fisiológica), ni el grupo con estrés ni el control mostraron el patrón esperado. Hay
además un estudio posterior en *PLOS One* con la misma conclusión negativa.

⚠️ **Consecuencia práctica: no usar "el estrés vuelve la conducta automática" como
afirmación fuerza en un deck o en un documento de diseño de este proyecto.**

### 4.3 "Estresado" no implica "quiere humano" — hay contraevidencia sólida

| Evidencia | Qué contradice |
|---|---|
| Lucas, Gratch, King & Morency (2014) — F-483: creer que se habla con una máquina **reduce** el miedo a autorrevelarse | El estrés puede empujar **hacia** el bot, no hacia el humano |
| Jin et al. (2025), *Journal of Consumer Psychology* — F-500: >6.000 participantes; en compras **vergonzosas**, >80% prefiere un chatbot **claramente no humano**; la disposición cae a medida que el agente parece más humano | Contradice directamente "a mayor carga emocional, más humano" |
| Ayers et al. (2023), *JAMA Internal Medicine* — F-484: respuestas de chatbot calificadas como empáticas 9,8× más frecuentemente que las de médicos (195 intercambios de r/AskDocs) | El humano no es automáticamente superior en el registro emocional |
| Han, Yin & Zhang (2026), *MIS Quarterly* — F-485: la **empatía explícita** del bot dispara **reactancia psicológica** y baja la competencia percibida | Lo que el usuario rechaza es la **postura emocional** del bot, no su condición de bot |

⭐ La lectura conjunta de F-483, F-500 y F-485 es específica y contraintuitiva: en varios
contextos cargados de emoción **el usuario quiere una máquina que se comporte como
máquina** — no un humano, y menos aún un bot fingiendo empatía.

### 4.4 La segunda rama del claim es tautológica

"Si busca ayuda humana… llega a un humano" no es una hipótesis falsable. La pregunta
interesante que sí lo es: **¿cuántos turnos tolera antes de pedirlo, y qué gatilla el
pedido?** Sobre eso no se encontró un dato duro publicado: la literatura describe **qué
señales** anteceden al escalamiento (repetición, reformulación, sentimiento negativo —
Sandbank et al., 2018, NAACL — F-497) pero no un umbral cuantificado de turnos.

---

## 5. Eco de cita y huérfanos (auditoría de las cifras que circulan)

Aplicando el chequeo de eco del skill y la regla **C22** de
`tendencias-diseno-innovacion`:

- 🔁 **Una sola fuente con muchos altavoces**: "70% marca cero", "65% dice *agente*", "72%
  termina hablando con un humano" y "88% prefiere agente en vivo" **son todas de la misma
  encuesta** (Clutch 2019, N=501 — F-471). Las decenas de blogs que las repiten **no son
  confirmación independiente**. Además es **de 2019 y de EE.UU.**: pre-LLM.
- 🕳️ **Huérfano de cita**: la afirmación muy repetida de que "Forrester encontró que
  transferir antes del pico de frustración eleva la satisfacción" **no remonta a ningún
  informe de Forrester localizable** — su rastro termina en un blog de proveedor (F-495).
  Misma anatomía que el caso F-444 del node de tendencias. **No usar.**
- ⚔️ **Tensión no resuelta que hay que reportar como tal**: los proveedores de chatbots
  publican *containment rates* de **70-90%** (F-496, 🔴E, con conflicto de interés
  evidente), mientras Gartner mide **14%** de resolución completa en autoservicio con N=5.728
  (F-472). No miden exactamente lo mismo —"contenido en el bot" ≠ "problema resuelto"— y
  esa diferencia de definición **es** el hallazgo: un usuario "contenido" puede ser un
  usuario que se rindió.
- 📎 El dato de Gartner llegó a esta investigación vía un artículo de práctica de
  *California Management Review* (Burden, Dukatz, Ramesh & Converso, 2026 — F-498),
  firmado por autores de una consultora que vende justamente estos sistemas. Se rastreó
  hasta la nota de prensa original de Gartner antes de usarlo; el artículo aporta además
  el término útil de **"chatbot loop"** para el bucle sin salida.

---

## 6. De dónde viene el claim

La intuición es correcta en su observación y equivocada en su explicación, y su origen es
rastreable: en **2005** Paul English (cofundador de Kayak) publicó el **"IVR Cheat
Sheet"**, lista de códigos para saltarse los menús telefónicos, que en 2006 se convirtió
en **gethuman.com** y superó el millón de visitantes (F-480). English denunciaba
explícitamente el **default de la industria**: obligar al que llama a agotar todas las
opciones automáticas antes de dejarlo llegar a una persona.

Es decir: **el atajo se volvió conocimiento público hace veinte años**. Lo que hoy se
observa como "conducta del usuario estresado" es, en buena medida, **un guion cultural
aprendido y transmitido** — la *táctica* de De Certeau, ya institucionalizada. El estrés
probablemente **acelera** su ejecución; la evidencia disponible no sostiene que la
**cause**.

---

## 7. Contraevidencia buscada a propósito (Paso 11)

Se buscaron activamente: (a) réplicas fallidas del mecanismo de estrés (**encontradas** —
F-476); (b) evidencia de que los usuarios **prefieren** el bot bajo carga emocional
(**encontrada** — F-483, F-500, F-484); (c) evidencia de que la mayoría **no** escala
(**encontrada pero contaminada** por conflicto de interés — F-496 vs. F-472); (d) críticas
al relato "los clientes odian los chatbots" (**encontradas**: las preferencias son
dependientes de contexto, tarea y generación, no universales).

---

## 8. Tabla resumen de rigurosidad

| Fuente | Tipo de evidencia | Revisión por pares | N | Validez | Confiabilidad | Peso para el claim |
|---|---|---|---|---|---|---|
| Crolic et al., 2022 (F-469) | Datos de campo + 4 experimentos | 🟢 *J. of Marketing* | campo telco + exp. | ✅ interna alta (experimental) | ✅ multi-método | 🟢 **Alto** (P2) |
| Wang et al., 2026 (F-470) | RCT de campo | 🔴 **preprint arXiv** | plataforma Taobao | ✅ ecológica alta | ⚠️ sin arbitraje | 🟡 Medio-alto (corolario) |
| Chacon & Martínez-Troncoso, 2026 (F-486) | 4 estudios preregistrados (DCE) | 🟢 *J. of Consumer Behaviour* | 4 muestras | ✅ preregistro | ✅ multi-estudio | 🟢 Alto (P2) |
| Castelo et al., 2019 (F-481) · Longoni et al., 2019 (F-482) | Experimentos | 🟢 JMR / JCR | multi-estudio | ✅ | ✅ | 🟢 Alto (P2, mecanismo) |
| Jin et al., 2025 (F-500) | Experimentos | 🟢 *J. of Consumer Psychology* | >6.000 | ✅ | ✅ | 🟢 **Alto (contraevidencia)** |
| Lucas et al., 2014 (F-483) | Experimento | 🟢 *Computers in Human Behavior* | laboratorio | ⚠️ externa (lab) | ✅ replicado en línea | 🟡 Medio (contraevidencia) |
| Han et al., 2026 (F-485) | 3 experimentos (incl. LLM en vivo) | 🟢 *MIS Quarterly* | 3 estudios | ✅ | ✅ | 🟢 Alto (contraevidencia matizada) |
| Ayers et al., 2023 (F-484) | Comparación con evaluadores ciegos | 🟢 *JAMA Intern Med* | 195 intercambios | ⚠️ **ecológica baja**: foro público, no consulta real; jueces = profesionales, no pacientes | ✅ triplicado | 🟡 Medio (contraevidencia) |
| Schwabe & Wolf, 2009 (F-475) | Experimento | 🟢 *J. Neuroscience* | pequeño | ❌ **no replicó** | ❌ | 🔴 **Bajo — no usar** |
| Smeets et al., 2023 (F-476) | 2 replicaciones exactas preregistradas | 🟢 *Neurobiology of Stress* | 2 muestras | ✅ preregistro | ✅ | 🟢 Alto (refuta mecanismo) |
| Martijn et al., 2026 (F-489) | Análisis de conversaciones reales | 🟢 *Int. J. of HCI* | 200 conversaciones | ⚠️ un solo chatbot/dominio | ✅ codificación sistemática | 🟡 Medio (P3) |
| Gartner, 2024 (F-472) | Encuesta de industria | ⚪ no aplica | 5.728 | ⚠️ método no auditable | ⚠️ | 🟡 Medio (P1) |
| Clutch, 2019 (F-471) | Encuesta de industria | ⚪ no aplica | 501 | ⚠️ autorreporte retrospectivo, EE.UU., **pre-LLM** | ⚠️ **origen de eco de cita** | 🟡 Medio (P1) |
| OSIPTEL 2023 (F-473) · Ley 10/2025 ES (F-474) | Norma regulatoria | ⚪ no aplica | — | ✅ hecho verificable | ✅ | 🔵 Alto como corroboración, nulo como mecanismo |
| Vendors de containment (F-496) · "Forrester" vía blog (F-495) | Marketing / huérfano | ⚪ | — | ❌ | ❌ | 🔴 **No usar como afirmación fuerza** |

**Balance de arbitraje**: de 13 fuentes empíricas/académicas clave, **11 pasaron revisión
por pares**, 1 es preprint (F-470) y 1 es encuesta de industria sin arbitraje aplicable.

---

## 9. Qué implica para este proyecto

1. **No prometer que el bot "detecta" al usuario estresado y por eso lo escala.** La
   evidencia sostiene lo contrario del reflejo habitual: humanizar y empatizar con el
   usuario alterado **empeora** los resultados (F-469, F-485). El bot debe volverse **más
   máquina y más rápido para salir**, no más cálido.
2. **La salida a humano debe ser visible desde el turno 1, no un premio por agotar el
   flujo.** Chacon (F-486) muestra que el traspaso **temprano e iniciado por el usuario**
   se prefiere al tardío; Alibaba (F-470) cuantifica el costo de llegar tarde. En Perú,
   además, **es obligatorio por norma de OSIPTEL** (F-473).
3. **Medir el pedido de humano como señal de diseño, no como fracaso.** Un *opt-out rate*
   alto en un paso concreto dice que el menú no coincide con las intenciones reales de ese
   paso.
4. **Cuidado con el KPI de *containment*.** Si se optimiza contra F-496 (70-90%) en vez de
   contra la resolución real (F-472: 14%), se estará premiando al bot por **retener**
   usuarios que en realidad se rindieron.
5. **Enlace con el modelo `lapuerta`**: la variable relevante para simular esta conducta no
   es "estrés" (no medible ni validado) sino algo del tipo *experiencia previa con canales
   automatizados* + `confianza` + `acceso_digital`. **No se propone todavía como variable
   nueva** — se deja anotado para `/cerrajero`.

---

## 10. Limitaciones de la búsqueda

- ⚠️ **El proxy de red del entorno bloqueó el acceso a texto completo** en ScienceDirect,
  Wiley, Springer, Taylor & Francis, arXiv, PMC/NCBI, Emerald, ORA-Oxford, NN/g, Clutch y
  otros. Todo lo anterior se construyó con **resúmenes de editorial, portales
  universitarios, notas de prensa institucionales y resultados de búsqueda**, no con
  lectura del texto completo. Los tamaños de efecto puntuales (especialmente los de F-470)
  **no pudieron verificarse contra el paper**.
- No se localizó ningún estudio que mida directamente **estrés → procesamiento del menú →
  escalamiento** en un flujo conversacional real. Es un hueco genuino de la literatura, no
  solo de esta búsqueda.
- No se halló **dato peruano primario** sobre tasas de escalamiento a humano; F-494 es
  consultora, conocida solo por cobertura secundaria.
- No se buscó el registro social (`/gossip`) ni el de negocio (`/marketer`): con
  `/trinidad` este tema daría más, sobre todo en el registro social, donde el "truco para
  llegar a un humano" circula intensamente.

---

## Conexiones

- [[evaluacion-calidad-agentes-conversacionales-ia|Evaluación de calidad de agentes
  conversacionales de IA]] — este node aporta **qué conducta medir** (pedido de humano,
  opt-out por paso, momento del escalamiento en la curva de frustración) y una advertencia
  fuerte sobre el KPI de *containment*; ese node aporta **con qué instrumentos** medirlo
  (BUS-11, CUQ, PARADISE, métricas RAG).
- [[modelo-salud-ia-farmacias-peru|Modelo de triage con IA + farmacias + atención humana
  (Perú)]] — el diseño del flujo `/trinidad` + `/seeker` de triage asume un paso a atención
  humana; este node aporta la evidencia de **cuándo** debe ofrecerse (temprano, visible) y
  la contraevidencia de que humanizar el bot en momentos de angustia puede ser
  contraproducente (F-469, F-485), además de la obligación regulatoria peruana (F-473).
- [[seguros-comportamiento-mundo-peru|Comportamiento, percepción y mercado global de
  seguros (Mundo vs. Perú)]] — el ~48% de desconfianza documentado ahí es el suelo sobre el
  que ocurre esta conducta: un canal automatizado que no deja salir refuerza exactamente la
  causa #1 de desconfianza (falta de información/atención).
