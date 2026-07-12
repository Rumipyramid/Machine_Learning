# Behavioral Design — Investigación 360° (trinidad)

> Reporte consolidado `/trinidad` · 2026-07-12
> Pregunta: **¿cómo le va al behavioral design como disciplina y mercado, y qué se
> necesita para ser los mejores — aplicado a seguros (Rimac)?**
> Pistas: 🔬 empírica/teórica (`seeker`) · 📱 social/mediática (`gossiper`) · 📈 negocio (`marketer`).
> Fuentes registradas en `research/fuentes/registro_fuentes.md` (F-16 a F-27).

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
- **Efectos reales a escala son chicos pero rentables.** Los RCTs de unidades de nudging
  gubernamentales a escala (123+ RCTs, >20 millones de personas) muestran efectos mucho
  menores que los de papers académicos — del orden de ~1.4 puntos porcentuales vs ~8.7 en
  la literatura publicada (DellaVigna & Linos, 2022 — Econometrica; ampliamente replicado
  como referencia del "voltage drop"). Chicos, pero a costo casi nulo por persona: el ROI
  puede seguir siendo alto si el denominador es grande.
- **Megastudies y heterogeneidad.** El enfoque de megastudy (decenas de brazos, cientos de
  miles de personas, un outcome objetivo común) es hoy el estándar para saber *qué* funciona
  *dónde* (Milkman et al., 2021 — Nature, megastudy de ejercicio con 61 arms/60k personas;
  megastudies de vacunación con N=689,693). La investigación 2024-2025 se concentra en
  **cuándo la heterogeneidad es accionable para personalizar** (arXiv 2411.16552, 2024 —
  ⚠️ preprint).
- **Evidencia específica en seguros.** RCTs de RGA/SOA (N≈2,001 y 2,005) muestran que
  intervenciones de comprensión (video vs texto, simplificación) mejoran el journey de
  compra de vida (RGA/SOA, 2024-2025 — C, industria con método declarado). Un experimento
  de campo nacional de seguros basados en uso (UBI) redujo exceso de velocidad 11-13%,
  frenadas bruscas 16-21% y aceleraciones 16-25% (Accident Analysis & Prevention, 2025 —
  RCT de campo). Ambos casos son **diseño del producto/feedback loop**, no solo mensajes.
- **El giro teórico i-frame → s-frame.** La crítica más influyente de la década: el campo
  se desvió al enfocarse en soluciones individuales (i-frame) para problemas con causas
  sistémicas (s-frame); los mejores resultados vienen de cambiar la estructura — defaults
  de producto, pricing, arquitectura del sistema — no la "psicología del usuario"
  (Chater & Loewenstein, 2022 — Behavioral and Brain Sciences; cf. Sunstein y BIT, que
  responden que ambos marcos son complementarios).
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
| DellaVigna & Linos, 2022 | RCTs a escala | >20M personas | ✅ outcomes administrativos reales | 🟢 Alto |
| Milkman et al., 2021 | Megastudy | 61 arms / ~60k | ✅ outcome objetivo | 🟢 Alto |
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
