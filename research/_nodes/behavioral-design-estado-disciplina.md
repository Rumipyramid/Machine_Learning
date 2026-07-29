# Behavioral design: estado de la disciplina y del mercado

> Documento de investigación. Fuente persistente y versionada en el repositorio.
> Fecha de elaboración: 2026-07-12 · Última actualización: 2026-07-22 · Versión: v1.1
> (migrado desde `research/behavioral_design_360.md` a Many Brains, sin cambios de fondo)
> Origen: `/trinidad` — investigación de 360° (empírica + social + negocio)
> Pregunta: **¿cómo le va al behavioral design como disciplina y mercado, y qué se
> necesita para ser los mejores — aplicado a seguros (Rimac)?**
> Fuentes registradas en `research/fuentes/codice.md` (F-16 a F-27).

## Resumen ejecutivo

- 🔬 **Empírica**: el "nudge promedio" está en crisis (tras corregir sesgo de publicación,
  la evidencia del efecto promedio se debilita mucho), pero la disciplina no murió — se
  reconvirtió: megastudies, personalización, diseño estructural (s-frame) y ahora IA.
- 📱 **Social**: la conversación pública sobre el campo está dominada por dos narrativas:
  el escándalo de fraude (Ariely/Gino) y el giro a IA. Es una conversación intra-profesional
  (🌡️ circulando), no un tema viral masivo.
- 📈 **Negocio**: la demanda crece y se consolida (big consultoras comprando boutiques
  conductuales; Vitality operando en 40+ mercados; aseguradoras montando unidades propias).
  El mercado paga por esto aunque la academia discuta el efecto promedio.
- ⚖️ **Convergencia clave**: las tres pistas apuntan a lo mismo — el valor ya no está en
  "aplicar nudges de catálogo", sino en **experimentar en propio contexto, medir en KPIs de
  negocio, diseñar a nivel de producto (no solo de mensaje) e integrar IA**. Esa es la
  definición operativa de "ser los mejores" en 2026.

---

## 🔬 Pista empírica/teórica (seeker)

**Veredicto:** el behavioral design es real pero sus efectos promedio fueron sobrevendidos;
la frontera actual es heterogeneidad + personalización + intervención estructural. Quien
siga vendiendo "el nudge universal" está una década atrás.

### Lo documentado

- **La crisis del efecto promedio.** El meta-análisis fundacional de 447 experimentos
  reportó que el nudging funciona en general (Mertens et al., 2022 — meta-análisis, PNAS).
  La re-análisis con corrección bayesiana de sesgo de publicación concluyó que **no queda
  evidencia de un efecto promedio** una vez corregido el sesgo (Maier et al., 2022 — PNAS,
  RoBMA; ⚠️ el debate metodológico sigue abierto). Un meta-análisis de segundo orden más
  reciente matiza: hay impacto, pero menor y muy heterogéneo por dominio y técnica
  (Hu, 2025 — Journal of Behavioral Decision Making).
- **[Revisión profunda 2026-07-22, F-17/F-18/F-21] Tres métodos independientes convergen
  en el mismo resultado — y por la misma razón.** Maier et al. re-analizaron el propio
  dataset de Mertens (447→455 efectos) con **RoBMA** (robust Bayesian meta-analysis,
  model-averaging de selection models + PET-PEESE): tras la corrección, no queda evidencia
  bayesiana de un efecto promedio positivo — la severidad del sesgo de publicación en la
  literatura de nudge es tal que se lo "traga" entero. Hu et al. (2025) repiten el
  ejercicio a una escala mucho mayor: 13 artículos / 14 meta-análisis, 1,638 estudios
  primarios, ~30 millones de participantes — el efecto agregado cae de **d=0.27 (IC95%
  [0.16, 0.38])** antes de corregir sesgo de publicación a **d=0.004** después de
  corregirlo, prácticamente cero. DellaVigna & Linos (F-21, más abajo) llegan al mismo
  punto por una vía totalmente distinta —no reanalizan meta-análisis, comparan RCTs reales
  de unidades de gobierno contra RCTs publicados en journals— y encuentran que el sesgo de
  publicación y el bajo poder estadístico de los estudios académicos **alcanzan para
  explicar toda la diferencia** entre ambas muestras; que un académico participe en el
  diseño no explica la brecha por sí solo. Tres metodologías independientes (Bayesiano,
  meta-meta-análisis, comparación campo-vs-publicado) aterrizan en la misma conclusión por
  razones distintas: **el efecto promedio del nudge en la literatura publicada estaba
  inflado por sesgo de publicación, no por una brecha real laboratorio-vs-mundo-real.**
  Caveat de Hu et al. que templa la contundencia: la mayoría de los 14 meta-análisis que
  agregan tiene calidad metodológica **baja o críticamente baja** por AMSTAR-2 (falta de
  pre-registro, ausencia de evaluación de riesgo de sesgo en los meta-análisis originales)
  — el corpus que sostiene esta conclusión es él mismo de calidad mediocre; es la mejor
  estimación disponible hoy, no un caso cerrado con evidencia impecable.
- **La granularidad importa más que el promedio (F-16, revisión profunda
  2026-07-21).** Dentro del propio meta-análisis original de Mertens et al.
  (447 efectos/212 estudios — corregido después a 455/214 sin cambiar la
  conclusión sustantiva), el ranking por técnica no era parejo: las
  intervenciones de **default/esfuerzo** tuvieron el efecto más grande
  específicamente en los dominios de **salud y finanzas** — los dos más
  relevantes para un asegurador — mientras que **incentivos** domina en
  educación y políticas públicas. Esto no contradice que el efecto promedio
  agregado no sea robusto a sesgo de publicación (Maier et al., abajo); pero si
  hay que elegir qué técnica testear primero en la propia población, el ranking
  direccional del propio dataset (defaults > incentivos > mensajero/afecto >
  saliencia > priming > ego/compromiso/normas) es un prior razonable, no una
  garantía.
- **Efectos reales a escala son chicos pero rentables.** Los RCTs de unidades de nudging
  gubernamentales a escala (123+ RCTs, >20 millones de personas) muestran efectos mucho
  menores que los de papers académicos — del orden de ~1.4 puntos porcentuales vs ~8.7 en
  la literatura publicada (DellaVigna & Linos, 2022 — Econometrica; ampliamente replicado
  como referencia del "voltage drop"). Chicos, pero a costo casi nulo por persona: el ROI
  puede seguir siendo alto si el denominador es grande. **[Revisión profunda 2026-07-22,
  F-21]** Lo que explica la brecha, según los propios autores: no es que el nudge funcione
  peor "en el mundo real" per se — es que el sesgo de publicación y el bajo poder
  estadístico de los estudios académicos alcanzan para explicar toda la diferencia de ~6x;
  el canal de entrega (en persona vs. carta, reflejo de restricciones institucionales) sí
  explica parte de la variación restante. La heterogeneidad entre tipos de nudge es
  sustancial —algunos efectos son nulos o incluso negativos aun a escala—; los *defaults*
  embebidos en un entorno de elección sensible a normas sociales son los que mejor
  persisten al escalar, más que los mensajes o recordatorios genéricos.
- **Megastudies y heterogeneidad.** El enfoque de megastudy (decenas de brazos, cientos de
  miles de personas, un outcome objetivo común) es hoy el estándar para saber *qué* funciona
  *dónde* (Milkman et al., 2021 — Nature, megastudy de ejercicio con 54 arms/61,293 personas;
  megastudies de vacunación con N=689,693). La investigación 2024-2025 se concentra en
  **cuándo la heterogeneidad es accionable para personalizar** (arXiv 2411.16552, 2024 —
  ⚠️ preprint). **[Revisión profunda 2026-07-22, F-20]** El megastudy de ejercicio en
  detalle: 30 científicos de 15 universidades, 54 programas digitales de 4 semanas cada
  uno, corridos sobre 61,293 miembros reales de una cadena de gimnasios de EE.UU. (24 Hour
  Fitness) — outcome objetivo (asistencia real registrada, no autorreportada). 45% de las
  intervenciones subió las visitas semanales entre 9-27%; la que más funcionó no fue el
  recordatorio genérico sino un microincentivo dirigido al **momento de recaída**:
  bonificar con puntos (~US$0.09) específicamente a quien había faltado a una sesión
  programada y volvía a la siguiente. Costo de despliegue a escala: ~US$0.75 por persona
  por mes — coherente con la lectura de "efectos chicos pero de costo casi nulo" de
  DellaVigna & Linos. Lección de diseño: apuntar el nudge al momento de lapso/recaída, no
  a la adherencia general.
- **Evidencia específica en seguros.** RCTs de RGA/SOA (N≈2,001 y 2,005) muestran que
  intervenciones de comprensión (video vs texto, simplificación) mejoran el journey de
  compra de vida (RGA/SOA, 2024-2025 — C, industria con método declarado). Un experimento
  de campo nacional de seguros basados en uso (UBI) redujo exceso de velocidad 11-13%,
  frenadas bruscas 16-21% y aceleraciones 16-25% (Accident Analysis & Prevention, 2025 —
  RCT de campo). Ambos casos son **diseño del producto/feedback loop**, no solo mensajes.
  **[Revisión profunda 2026-07-29, F-23]** Lectura completa del experimento UBI: es un RCT
  preregistrado (NCT06101251), N=1,449 conductores reclutados a nivel nacional, con 6
  semanas de línea base y 12 semanas de intervención en 4 brazos (control / feedback
  estándar / meta asignada / meta elegida, con incentivo de US$100). Dato que el resumen de
  una línea no traía: las mejoras de conducta **se sostuvieron durante un período de
  seguimiento posterior al fin de la intervención** — no es solo efecto Hawthorne mientras
  el conductor sabe que lo miden. Matiz que acota el caso: lo validado es un mecanismo de
  **feedback + microincentivo** ("UBI simulado"), no necesariamente el pricing dinámico real
  de una prima — conviene no generalizar automáticamente de uno a otro al citar este caso
  como ejemplo de "producto embebido".
- **El giro teórico i-frame → s-frame.** La crítica más influyente de la década: el campo
  se desvió al enfocarse en soluciones individuales (i-frame) para problemas con causas
  sistémicas (s-frame); los mejores resultados vienen de cambiar la estructura — defaults
  de producto, pricing, arquitectura del sistema — no la "psicología del usuario"
  (Chater & Loewenstein, 2022 — Behavioral and Brain Sciences; cf. Sunstein y BIT, que
  responden que ambos marcos son complementarios). **[Revisión profunda 2026-07-22, F-19]**
  El mecanismo que proponen no es solo "moda académica" sino incentivo de actor:
  documentan que BP acuñó el término "huella de carbono" en 2004 dentro de una campaña
  ("Beyond Petroleum") diseñada específicamente para reencuadrar el cambio climático como
  un problema de conducta individual — mientras la empresa seguía cabildeando activamente
  contra la regulación sistémica (s-frame) que de verdad reduciría emisiones. Su lectura
  general, citada textual: "firmas de un amplio rango de sectores encuentran que pueden
  promover sus propios intereses promoviendo el i-frame mientras cabildean sin descanso
  por políticas s-frame que favorecen esos mismos intereses" — el i-frame no solo distrae
  por default, puede ser una estrategia activa de desvío de responsabilidad. Relevancia
  directa para seguros: cualquier apuesta de la industria en "educación financiera" o
  "glosarios" sin acompañarla de rediseño real de producto corre el riesgo de leerse —o de
  funcionar— exactamente así, aunque no sea la intención declarada.
- **La crisis de integridad.** Los dos investigadores más famosos del campo aplicado
  (Ariely, Gino) enfrentan evidencia sustancial de fabricación de datos justamente en los
  estudios de honestidad usados por la industria de seguros (firma arriba del formulario);
  Harvard halló misconduct en Gino en 2023, y el caso sigue produciendo literatura
  (Bazerman, 2025 — *Inside an Academic Scandal*; Science, 2023-2025). Implicación
  práctica: **no construir sobre hallazgos de celebrity science sin verificar replicación**.
- **La frontera IA.** Emergió un subcampo formal de "AI Behavioral Science" (Jackson et al.,
  2025 — SSRN/arXiv, ⚠️ preprint con autores top: Camerer, Mullainathan, Brynjolfsson…), y
  la simulación de comportamiento humano con LLMs (usuarios sintéticos) ya muestra
  ganancias medibles de fidelidad cuando se afina con datos reales y trazas de razonamiento
  (arXiv 2503.20749, 2025 — ⚠️ preprint; la literatura advierte no confiar en agentes
  generativos sin benchmark de realismo empírico, arXiv 2506.21974).

### Tabla de rigurosidad (fuentes clave)

| Fuente | Tipo | N | Validez | Peso para la pregunta |
|---|---|---|---|---|
| Mertens et al., 2022 | Meta-análisis | 447 estudios | ⚠️ sesgo de publicación demostrado | 🟡 Medio |
| Maier et al., 2022 | Re-análisis bayesiano | (mismos datos) | ✅ método robusto; debate abierto | 🟢 Alto |
| Hu et al., 2025 | Meta-meta-análisis | 14 meta-análisis / 1,638 estudios / ~30M | ⚠️ calidad AMSTAR-2 baja/crítica en la mayoría del corpus agregado | 🟢 Alto en escala, 🟡 Medio en calidad del corpus |
| DellaVigna & Linos, 2022 | RCTs a escala | >20M personas | ✅ outcomes administrativos reales | 🟢 Alto |
| Milkman et al., 2021 | Megastudy | 54 arms / 61,293 personas | ✅ outcome objetivo | 🟢 Alto |
| Chater & Loewenstein, 2022 | Teórico | — | (marco, no dato) | 🟢 Alto como brújula |
| RGA/SOA, 2024-25 | RCT industria | ~2k × 2 | ⚠️ industria, no auditado | 🟡 Medio |
| UBI field experiment, 2025 | RCT de campo | nacional | ✅ conducta observada (telemática) | 🟢 Alto |
| arXiv LLM sim., 2025 | Preprint | — | ⚠️ sin peer review | 🟡 Medio |

---

## 📱 Pista social/mediática (gossiper)

**Nivel de instalación:** 🌡️ **Circulando** — el behavioral design no es tema viral masivo;
la conversación es intra-profesional (LinkedIn, newsletters, prensa científica) y gira
alrededor de dos narrativas. *(Juicio de instalación, separado del juicio de verdad.)*

1. **"El campo tiene un problema de credibilidad"**: el escándalo Ariely/Gino tuvo cobertura
   sostenida en medios establecidos (NPR Planet Money, Science, Freakonomics/Dubner) entre
   2023 y 2025, con validación mayoritaria (las acusaciones se confirmaron con
   investigaciones institucionales, no se desmintieron). Para el público profesional, "la
   firma arriba del formulario" pasó de caso estrella a chiste interno — y era *el* caso
   estrella de behavioral design en seguros.
2. **"El campo se está volviendo IA"**: eventos LSE, workshops académicos (AIBS 2025/2026)
   y contenido profesional apuntan a que la conversación de futuro del gremio es
   IA + comportamiento (agentes sintéticos, personalización algorítmica), no nudges clásicos.

**Validación vs. amplificación:** la narrativa de crisis está validada (retractions,
sanciones); la narrativa de "IA reemplaza al behavioral scientist" es mayormente
amplificación especulativa por ahora.

**Limitación importante:** no se pudo acceder directamente a X/Reddit/TikTok desde este
entorno; esta pista se apoya en prensa científica y contenido profesional indexado. El
sentimiento de foros de nicho queda sin medir — es la pista más débil del reporte.

---

## 📈 Pista de negocio (marketer)

**Veredicto:** la demanda comercial de behavioral design crece y se institucionaliza,
divergiendo de la crisis académica. La evidencia de mejor calidad viene del modelo
seguros + comportamiento (shared value), no de consultoría genérica.

### Lo documentado con fuente

- **Consolidación del mercado**: Nesta adquirió el Behavioural Insights Team (2021); a lo
  largo de 2024-2025 Deloitte, Oliver Wyman, Aon, KPMG, BCG, IBM, PwC y McKinsey adquirieron
  o se asociaron con firmas de economía conductual (informes de mercado — 🟠 metodología no
  auditable). El mercado amplio de consultoría económica: ~US$38B en 2025, CAGR ~5%
  (intelmarketresearch — 🟠). La lectura direccional es clara: **la capacidad conductual se
  volvió línea de servicio estándar de las big firms**, ya no diferencial por sí sola.
- **El caso de referencia en seguros — Vitality/Discovery**: modelo shared-value
  fundado en economía conductual, hoy en 40+ mercados y 40M miembros; reporta que miembros
  altamente engaged tienen 76% menor mortalidad y que conductores mejoran 15% tras un mes
  de Vitalitydrive (Vitality Group, 2025 — ⚠️ **self-reported**, sin auditoría externa;
  aún así, es el benchmark que toda aseguradora conductual persigue y ~la mitad del valor
  económico acumulado se atribuye a cambio de comportamiento según su propio reporte).
- **Unidades conductuales corporativas**: McKinsey documenta nudge units privadas con
  impactos tipo +10% retención y reducción de fraude, y define el estándar operativo:
  traducir conducta a valor medible vía A/B testing permanente (McKinsey — 🟡 C, consultora).
- **El anti-caso — Lemonade**: contrató a Ariely como Chief Behavioral Officer (2015-2020)
  y construyó marketing sobre el "honesty pledge"; el hallazgo detrás resultó fabricado.
  Lección de negocio: el behavioral design como *storytelling* es frágil; como *sistema de
  experimentación* es defendible.
- **Contexto local**: Rimac ya opera un CoE de Behavioral & Service Design y desplegó un
  asesor web con IA generativa que —según prensa local— duplicó conversión (Business
  Empresarial, 2025 — 🟠 D, self-reported). El BID y la agenda regional de inclusión
  financiera piden explícitamente educación/diseño financiero basado en economía del
  comportamiento para mercados como Perú (BID/CEMLA — 🔵 B).

### Vigencia y comparabilidad

Las cifras de Vitality y Rimac son self-reported y no normalizadas (no hay definición
común de "mejora del conductor" ni de "conversión"); sirven como dirección, no como
benchmark duro. El dato duro comparable del sector es el de DellaVigna & Linos (efectos
chicos, ROI alto por costo marginal ~0) — útil para fijar expectativas con stakeholders.

---

## ⚖️ Síntesis — qué significa "ser los mejores" en behavioral design (seguros, 2026)

**Dónde convergen las tres pistas** (señal fuerte):

1. **El nudge de catálogo murió; el experimento propio manda.** Academia (voltage drop,
   heterogeneidad), mercado (McKinsey: A/B como estándar) y el benchmark Vitality
   (feedback loops de producto) coinciden: el valor está en medir en tu población, no en
   copiar efectos publicados. *Para Rimac: cada intervención conductual debería nacer con
   grupo de control y KPI de negocio pre-declarado.*
2. **Del mensaje al producto (i-frame → s-frame).** Los casos con resultados grandes y
   sostenidos (Vitality, UBI telemático) cambian la estructura del producto — pricing
   dinámico, defaults, recompensas — no solo el copy del email. *La ventaja competitiva
   está en diseño conductual embebido en el producto asegurador.*
3. **IA + usuarios sintéticos es la frontera reconocida del campo.** Tanto la agenda
   académica (AI Behavioral Science) como la práctica apuntan ahí. El modelo `lapuerta`
   de este repo (personas sintéticas calibradas con ENAHO/IPF + validación) está
   exactamente en esa frontera: pocos equipos en la región tienen simulación de
   consumidores calibrada con microdato nacional. *Es el activo diferencial a escalar:
   usarlo para pre-testear intervenciones antes del A/B real reduce el costo del punto 1.*
4. **La integridad es ahora un activo comercial.** Post Ariely/Gino, poder decir "nuestros
   efectos vienen de nuestros propios RCTs, con datos verificables" diferencia frente a
   consultoras que venden hallazgos de segunda mano.

**Dónde divergen** (tensión real, no resolverla artificialmente):

- La pista de negocio crece mientras la pista empírica cuestiona el efecto promedio. El
  mercado está pagando, en parte, por una promesa más grande que la evidencia. Eso es un
  **riesgo** (corrección de expectativas) y una **oportunidad**: los equipos que fijan
  expectativas honestas (efectos de 1-3 pp a costo marginal bajo, compuestos en el tiempo)
  y las cumplen, sobreviven a la corrección; los que venden magia, no.

**Checklist operativo para "ser los mejores"** (derivado de las tres pistas):

- [ ] Toda intervención con control + KPI de negocio pre-declarado (no post-hoc).
- [ ] Portafolio balanceado: 70% mejoras s-frame de producto / 30% optimización de mensajes.
- [ ] Pipeline: hipótesis → simulación con `lapuerta` → megastudy/A-B en campo → escalar solo lo que replica.
- [ ] Expectativas caladas con DellaVigna & Linos (efectos chicos × población grande = ROI).
- [ ] Cero dependencia de hallazgos no replicados (auditar el catálogo de sesgos que se usa hoy).
- [ ] Medir heterogeneidad siempre (qué segmento responde), no solo el efecto promedio.

## Limitaciones

- **Pista social**: sin acceso directo a X/Reddit/TikTok; queda sin medir el sentimiento
  de comunidades de nicho. Es la pista más débil.
- **Vitality/Rimac**: cifras self-reported sin auditoría externa; usarlas como dirección.
- **Mercado**: no existe un market-size confiable específico de "behavioral design"
  (los informes disponibles tienen metodología opaca); se reportó solo la señal de
  consolidación, que sí es verificable operación por operación.
- No se accedió a bases de venture (PitchBook/Crunchbase) para dimensionar funding de
  boutiques conductuales.

---

## Conexiones

- [[seguros-comportamiento-mundo-peru|Comportamiento, percepción y valoración frente a
  seguros (Mundo vs. Perú)]] — el caso Vitality y la brecha de confianza en seguros que
  describe ese node son parte de la evidencia de negocio de este.
- [[mecanismos-seguros-salud|Mecanismos de seguros de salud]] — Discovery Vitality aparece
  en ambos nodes desde ángulos distintos: ahí como mecanismo que navega presión de costo,
  aquí como caso de referencia de behavioral design aplicado a seguros.
- [[material-visual-venta-consultiva|Material visual en la venta consultiva]] — aplica
  varios de los mismos principios (experimentar en la propia población, diseño a nivel de
  producto no solo de mensaje) al problema específico de explicar un producto de seguros.
- [[modelo-personas-sinteticas|Modelo de personas sintéticas (lapuerta)]] — el activo concreto
  que posiciona al proyecto en la frontera de "AI Behavioral Science" que este node identifica.
- [[proyecto-back-to-basics-ffvv-vida|Proyecto Back to Basics — FFVV Vida Individual]] — aplica
  la asimetría i-frame/s-frame de este node a un caso real: el Playbook del Asesor de RIMAC es
  casi enteramente i-frame (guiones, manejo de objeciones), mientras los nodos rojos del mapa
  sistémico del proyecto (perfilamiento, monitoreo de calidad) — el rediseño s-frame pendiente —
  siguen sin resolverse.
- [[tendencias-diseno|Tendencias en diseño: qué tiene impacto real y qué es propuesta]] — node
  hermano: el mismo patrón que este node documenta en behavioral design (efecto promedio
  sobrevendido, corregido por sesgo de publicación) aparece allí en el diseño (ROI sobrevendido,
  desarmado por eco de cita). Ambos concluyen lo mismo: la disciplina se defiende mejor por
  **mecanismo** que por **multiplicador**.
