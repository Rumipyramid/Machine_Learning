# Mecanismos de seguros de salud: presión actual y modelos que la navegan

> Node. Fuente de verdad de este tema. Rescata 3 investigaciones `/seeker`/`/trinidad` que
> originalmente solo vivían en el chat (2026-07-10). Fuentes indexadas en
> `fuentes/codice.md` (F-86 a F-116).
>
> Fecha de elaboración: 2026-07-10 · Última actualización: 2026-07-10 · Versión: v1.0

---

## 1. ¿Está "roto" el modelo de mancomunación de riesgo?

**Pregunta original**: ¿es correcto decir que el modelo por el que la gente sana subsidia a la
gente enferma está roto, porque ahora la gente vive más, se siniestra más y busca atención con
más frecuencia?

**Veredicto**: parcialmente correcto, pero sobre-simplificado en dos puntos.

- **"La gente vive más" — cierto**: esperanza de vida global de 46 años (1950) a >70 (2023); 65+
  pasará de 524M (2010) a ~1,500M (2050) (F-86, ⚠️ agregador no verificado contra WHO/UN directo).
- **"Se siniestra más" — cierto, con matiz causal**: envejecimiento se asocia a más enfermedad
  crónica/multimorbilidad (F-87, 🟢 peer-reviewed). Costo médico global sube 9.5%→10%→10.3%
  (2024-2026). **Pero el driver #1 no es el envejecimiento**: es nueva tecnología médica (74% de
  aseguradoras la citan), seguido de deterioro de sistemas públicos (52%) y farmacéutica (49%)
  (F-88, reporte de industria WTW).
- **"Busca atención al respecto" — cierto, pero NO es nuevo**: es el **riesgo moral** (moral
  hazard) formalizado por **Pauly (1968)** — buscar más atención al estar asegurado es conducta
  económica racional (responde al precio marginal), no "mala fe". Es una propiedad estructural
  del seguro desde su diseño teórico, no un fenómeno reciente causado por la longevidad (F-89, 🟢
  peer-reviewed, AER, paper fundacional del campo).
- **"El modelo está roto" — documentado, pero condicional, no universal**: existen casos reales
  de colapso por selección adversa ("espiral de la muerte"): un bloque individual de 1981 con
  primas escaladas a ~7x hacia 2009 (F-90, 🟢 peer-reviewed); Nueva York, tras *community rating*
  sin mandato, redujo su mercado individual a 17,000 asegurados hacia 2013 (casi colapso total);
  Blue Cross/Blue Shield mostró evidencia temprana similar (F-91, 🟢 peer-reviewed); Harvard 1995
  (sanos migraron al plan barato, encareciendo el generoso hasta volverlo insostenible).
  **Pero no ocurre automáticamente por demografía** — ocurre específicamente con *community
  rating sin mandato ni ajuste de riesgo*. Donde existen mandatos + ajuste de riesgo (ACA), el
  pool se ha sostenido (F-92, 🟢 peer-reviewed).

**Tensión activa que sí valida la intuición del "roto"**: hay literatura académica documentando
cómo el self-tracking/telemetría empuja a la industria hacia pricing personalizado que reduce la
subsidización cruzada (F-94, 🟢 peer-reviewed) — el mercado está respondiendo a la presión
alejándose de la solidaridad pura, no porque colapsó de golpe sino porque se está rediseñando.
Conecta directamente con `disposicion_compartir_datos_pricing` en el modelo `lapuerta`
(ver [[modelo-salud-ia-farmacias-peru|Modelo de triage IA + farmacias]]).

---

## 2. Modelos que navegan bien esta presión

**Principio de diseño que se repite en toda la evidencia**: los modelos **híbridos** (mancomunación
para riesgo catastrófico + mecanismos individuales para riesgo rutinario/moral hazard) superan
tanto a la solidaridad pura como al pricing puramente individualizado.

### Mecanismos con evidencia real

| Mecanismo | Qué resuelve | Evidencia | Peso |
|---|---|---|---|
| Ajuste de riesgo (Países Bajos, competencia gestionada) | Selección adversa | "Uno de los mejores modelos en práctica" pero aún no neutraliza del todo los incentivos de selección (F-96, 🟡) | Medio |
| Mejora continua del ajuste (grupos de costo por diagnóstico, multimorbilidad) | Precisión del ajuste | Campo activo de mejora, no solución estática (F-97, 🟢 peer-reviewed) | Alto |
| Capitación / value-based care (ACOs) | Riesgo moral del proveedor | Reduce costos sin reducir calidad (⚠️ F-98, fuente no verificada con precisión) | Medio (con reserva) |
| Ajuste de riesgo de la ACA | Espiral de la muerte | Comprime diferencias de loss ratio entre aseguradoras, "funcionando como se pretendía" (F-103, 🟡 análisis profesional) | Medio |
| Sistema 3M de Singapur (Medisave+Medishield+Medifund) | Moral hazard + catástrofe + equidad | Cobertura universal combinando ahorro individual (85%) + seguro catastrófico + red focalizada (~10%) (F-102, 🔵 B) | Alto |
| Incentivos conductuales/wellness | Prevención | **Evidencia mixta**: "modesta y a menudo de corta duración" (F-100, 🟢 peer-reviewed independiente) — ver tensión abajo | Medio |

**⚠️ Tensión declarada**: Vitality (la empresa) publicó su propio estudio afirmando resultados
fuertes y sostenidos (F-99, 🔴 autopublicado, conflicto de interés directo) — la ciencia
independiente es más cautelosa (F-100). No se promedia: se presentan en tensión.

### Casos de negocio con resultados publicados

- **Discovery Vitality** (Sudáfrica/global): utilidad operativa de Discovery Insure **+34%**
  (a R546M), atribuida explícitamente al programa Vitality Drive; ROE normalizado 15.4%
  (desde 13.5%) (F-104, 🔵 B, resultados oficiales). Prueba financiera real del mecanismo — aunque
  la atribución causal (¿selección de sanos o cambio de conducta real?) no está resuelta por la
  propia empresa.
- **Kaiser Permanente**: modelo integrado (capitación + provisión en una organización), top 5-10%
  nacional en HEDIS desde 2014 (F-105, 🔵 B). **No es inmune**: en 2025 enfrentó costos crecientes
  igual que el resto del sector — supera a sus pares bajo la misma presión, no la elimina.
- **Oscar Health**: loss ratio médico mejoró de 75.4% (Q1 2025) a 70.5% (Q1 2026) tras "un año de
  reset" con pricing disciplinado (F-106, 🔵 B, filing SEC). Eco directo del caso Babylon Health: la
  tecnología/disrupción sin disciplina actuarial no basta.

---

## 3. La capa de atención primaria específicamente

**Pregunta original**: dentro de la arquitectura de capas (ahorro/rutina, seguro catastrófico, red
de seguridad), ¿existen modelos que cubran bien la atención primaria?

### Mecanismos

| Modelo | Evidencia | Peso |
|---|---|---|
| **Direct Primary Care (DPC)**: cuota mensual fija (USD 50-150) directa al médico | Teóricamente sólido, visitas 30-60min vs. 12-15 tradicional; **poca evidencia peer-reviewed de beneficios, ningún estudio longitudinal** (F-107, F-108, 🟢) | Medio — teoría fuerte, evidencia delgada |
| **Gatekeeping + capitación (China, piloto)** | Consultas primarias **+55.3%**, visitas hospitalarias **-23.9%**, sin aumento de gasto (F-109, 🟢 cuasi-experimental — diseño fuerte) | Alto |
| **Gatekeeping — revisión general** | Reduce especialistas/gasto, **pero con diagnóstico tardío documentado, particularmente cáncer** (F-110, 🟢 revisión sistemática) | Medio — beneficio real con riesgo real |
| **Capitación NHS (UK)** | Modelo híbrido (capitación ajustada por necesidad + bono por desempeño + FFS para extras) en uso real a escala nacional (F-111, 🟢) | Alto |
| **Singapur — policlínicas + CHAS** | ⚠️ Incluso Singapur (el mejor caso de riesgo catastrófico, §2) lucha aquí: su reforma "Healthier SG" tuvo **éxito limitado** — subsidios insuficientes para cambiar práctica de proveedores establecidos (F-112, 🔵 B) | Medio |

**⚠️ Problema estructural del modelo más simple (DPC)**: excluye a quien no puede pagar la
membresía — exactamente lo opuesto de lo que necesita un sistema como el peruano, donde
automedicarse por falta de tiempo/dinero ya es el patrón dominante (ver
[[modelo-salud-ia-farmacias-peru|Modelo de triage IA + farmacias]] §1). Un DPC puro empeoraría el
problema que se busca resolver, salvo que se combine con subsidio (CHAS) o se integre en un
sistema capitado más amplio (NHS).

### Casos de negocio

- **Oak Street Health → CVS, USD 10.6B** (2023): validación estratégica fuerte del modelo de
  atención primaria basada en valor para Medicare. **Pero** (filing SEC oficial): operaba con
  pérdidas, esperando perder >USD 200M en 2023, sin rentabilidad hasta 2025 al menos (F-113,
  F-114). Validación de mercado ≠ rentabilidad actual — confirmado por análisis académico (F-115,
  🟢 peer-reviewed).
- **ChenMed**: 22% menos incidencia de stroke en pacientes >1 año inscritos; mejor desempeño que
  fee-for-service en tamizaje/HbA1c/estatinas; NPS de pacientes 80-90 (⚠️ muy por encima del NPS
  promedio de aseguradoras de 23-35, ver [[seguros-comportamiento-mundo-peru|Comportamiento y
  mercado global de seguros]] §7.2). **Fuente autopublicada, conflicto de interés** (F-116, 🔴,
  mismo patrón que Vitality).

---

## 4. Síntesis transversal (las 3 secciones)

**Convergencia**: la capitación/valor-por-resultado gana en las tres capas investigadas
(aseguradoras generales §2, atención primaria específicamente §3) — no es casualidad, es un
principio de diseño transversal.

**Divergencia/tensión que no se resuelve artificialmente**: el entusiasmo de negocio (Discovery,
ChenMed) es sistemáticamente más optimista que la evidencia académica independiente sobre el
mismo mecanismo — plausible que el efecto financiero venga más de **selección** (sanos se
autoseleccionan hacia estos productos) que de **cambio de conducta real** a gran escala.

**Para el proyecto**: el PL 08488 peruano (farmacéutico paga con stock del SIS, no membresía
privada) ya está, sin saberlo, más cerca del modelo Singapur/NHS que del modelo DPC
estadounidense — buena señal para el diseño de
[[modelo-salud-ia-farmacias-peru|el modelo de triage IA + farmacias]].

## Limitaciones generales

- Ninguna evidencia de precisión/efectividad citada aquí fue validada en población peruana
  específicamente.
- La pista social se evaluó explícitamente en las 3 investigaciones y se omitió las 3 veces —
  sin resultados de búsqueda en foros/RRSS para estos temas técnico-institucionales.
- La fuente F-98 (revisión sistemática de ACOs) no se pudo verificar con autor/journal exacto —
  tratar con reserva.

## Conexiones

- [[modelo-salud-ia-farmacias-peru|Modelo de triage IA + farmacias (Perú)]] — este node aporta el
  marco de mecanismos globales; ese node aplica el diseño concreto al caso peruano (PL 08488,
  automedicación, InkaFarma/Mifarma).
- [[seguros-comportamiento-mundo-peru|Comportamiento y mercado global de seguros]] — §7 de ese
  node (mercado global por ramo) es el punto de partida cuantitativo de este; el NPS de ChenMed
  (§3 aquí) se compara contra el NPS de aseguradoras documentado ahí (§7.2).
- [[glosario-seguro-salud-peru|Glosario de seguro de salud en Perú]] — vocabulario base.
- [[behavioral-design-estado-disciplina|Behavioral design: estado de la disciplina y del
  mercado]] — Discovery Vitality aparece en ambos: ahí como caso de referencia de
  behavioral design aplicado a seguros, aquí como mecanismo que navega presión de costo.
