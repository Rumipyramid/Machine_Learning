# Foresight: la experiencia futura de los seguros y la digitalización — preguntas profundas y radar de señales

> Documento de investigación. Fuente persistente y versionada en el repositorio.
> Fecha de elaboración: 2026-10-27 · Última actualización: 2026-10-27 · Versión: v1.2 (v1.2 suma §12: mapa de tendencias globales y de LATAM por pregunta abierta, §12.6 con cifras de la SBS y regulación peruana de 2026, §12.7 sobre finanzas abiertas y §12.8 sobre seguros en Yape; v1.1 sumó §11: cuatro señales nuevas y actualización de la 14)
> Origen: `/trinidad` (empírica/teórica + social + negocio) pedida por el usuario para reconstruir el radar de señales que se
> retiró de `digitalizacion-seguros-mercados-emergentes` (§9.4). Pregunta de partida: *¿cuál es la experiencia futura de los
> seguros y la digitalización?* y, detrás de ella, *¿cuáles son las preguntas más profundas?*
> Fuentes registradas en `research/fuentes/codice.md` (F-981 a F-1006); reutiliza F-961 a F-965 (marco y señales de Perú),
> F-1099 a F-1117 (§12), F-442, F-851, F-852, F-869, F-875, F-877, F-879, F-881, F-884, F-888, F-901, F-905, F-913, F-923, F-928, F-929, F-934, F-936.
> Solo fuentes públicas. Ningún material confidencial de clientes o empleadores se usó en este node.

---

## 0. Qué es y qué no es este documento

- **Es un radar armado con búsquedas, no un ejercicio de prospectiva.** El método de Godet (F-961) exige taller con expertos,
  análisis estructural, juego de actores y escenarios. Aquí solo hay una lectura de evidencia pública. Lo que sigue son
  **hipótesis ordenadas para llevar a un taller**, no pronósticos.
- **Todo se leyó por resúmenes de búsqueda o notas de prensa.** Ningún informe se abrió completo. Muchas cifras vienen de
  proveedores o aseguradoras que venden lo que miden.
- **La pista social es la más débil**: no se pudo llegar a Reddit ni a X. Lo que hay es percepción medida por encuestas de
  proveedores, demandas judiciales y guías de uso (ver §2.2).
- **Las "preguntas profundas" (§1) son construcción mía**, no un hallazgo. Se derivan de dónde chocan las fuentes; otra lectura
  podría armar otras. Están marcadas como tales.

---

## 1. Resumen ejecutivo

**Conclusión.** La experiencia futura de los seguros no se decide por cuánta tecnología se use, sino por quién responde
cuando el cliente más necesita que la promesa se cumpla. Lo digital ya cambió cómo se cotiza, se paga y se avisa. Lo que
sigue sin probarse es la parte que más pesa: que el pago llegue, rápido y sin pelea, cuando ocurre el daño.

Cuatro ideas, de más a menos sólida:

1. **Lo que el cliente delega hoy es lo de apoyo, no lo que compromete.** En una encuesta de proveedor en EE.UU. (F-982), el
   51% acepta alertas de clima severo y el 46% que la IA genere una cotización; solo el 22% acepta que presente un reclamo por
   él y el 16% que cancele o renueve una póliza. Es la mejor señal conductual disponible, pero es de un solo país y de un
   proveedor.
2. **Las aseguradoras ya venden dentro de asistentes de IA, pero cierran la compra en su propio sitio.** Liberty Mutual,
   Aviva, Tuio e Insurify cotizan en ChatGPT; no se halló una compra de punta a punta dentro del chat (F-981). La conversación
   captura la atención; la responsabilidad contractual sigue en la aseguradora.
3. **El precio individual y la mancomunación (el reparto del riesgo entre todos) se tensionan más cuanto más datos hay.** La
   teoría lo plantea con fuerza (F-990, F-992), la regulación europea ya trata la IA de precios en vida y salud como de alto
   riesgo (F-986), y hay un contrapunto que dice que la ruptura es menos nueva de lo que parece (F-994). Está abierto.
4. **En Perú la pregunta previa es si se digitaliza el seguro o solo su cobro.** Con 70,7% de empleo informal (F-879), 67% de
   adultos con cuenta o billetera (F-936) y solo 19% con algún respaldo asegurador entre quienes perdieron ingresos (F-1006),
   el techo no es la tecnología sino que haya algo asegurable, cobrable y creíble.

Las tres pistas **convergen** en que lo conversacional y lo automático avanzan por el lado de la cotización y el aviso. **Divergen**
en que el negocio celebra la IA (99,1% del financiamiento insurtech, F-901; riesgo n.º 2 en el barómetro de Allianz, F-989)
mientras la confianza del cliente en la IA cae (46% a 40%, F-983) aunque el apoyo declarado sube (F-982). No se resuelve:
miden cosas distintas.

---

## 1.1 La pregunta madre y las preguntas profundas

**Pregunta madre (construcción mía):** *¿Qué significa sentirse protegido en una vida medida, automatizada y asistida por IA, y
quién responde por esa promesa?*

Cada pregunta profunda es un punto donde las fuentes chocan. Se indica la fuente que la sostiene y qué haría falta para
responderla.

| # | Pregunta profunda | Por qué es profunda | Qué la sostiene | Qué haría falta para responderla |
|---|---|---|---|---|
| P1 | **Promesa y prueba:** ¿qué hace creíble un seguro que se compra en segundos y se paga (o no) en semanas? | Lo digital acelera la venta, no el siniestro. La confianza en el producto sube cuando el cliente cobra (F-852) y la demanda cae si el pago no llega o se duda de él (F-851). | F-851, F-852, F-999 (la velocidad de pago es característica de producto), F-875 (sanciones en Perú por plazos y rechazos) | Medir tiempo y tasa de pago real por canal; experimento de pago visible antes de renovar |
| P2 | **Solidaridad vs. personalización:** ¿cuánto precio individual tolera un sistema que existe para repartir riesgo? | Más datos permiten cobrar a cada quien su riesgo y, a la vez, deshacen el reparto. Quien carga con el riesgo "peor" puede quedar fuera. | F-990, F-991, F-992, F-993; contrapunto F-994; regulación F-986 | Estudios de efecto sobre bienestar (la Geneva Association dice que están "lejos de ser obvios", F-991); reglas peruanas (no verificadas, F-1005) |
| P3 | **Agencia y delegación:** ¿hasta dónde dejará la persona que un agente decida por ella? | La comodidad cae al pasar de asistir a decidir (F-982). Un agente que renueva o cancela por la persona cambia quién es el "cliente". | F-982, F-983, F-995 (más transacciones automatizadas, apoyo humano en momentos críticos) | Estudio conductual (no declarado) de delegación en renovación; qué pasa cuando el agente se equivoca |
| P4 | **Ex post vs. ex ante:** ¿el seguro seguirá siendo pagar después del daño o pasará a evitarlo? | Si la aseguradora previene, su relación con el cliente es continua y cambia el modelo. | F-996 (de transferir riesgo a mitigarlo), F-442 (RCT: el seguro por uso cambia conducta), F-1000, F-1001 (cifras de proveedores) | Evidencia independiente de persistencia; quién paga el sensor y quién se queda con el ahorro |
| P5 | **Asegurabilidad:** ¿qué riesgos dejarán de poder asegurarse a un precio razonable? | Clima, ciber e IA presionan el límite de lo asegurable. Si el seguro se retira, la digitalización no tiene qué entregar. | F-987, F-988, F-989 | Series de retiradas y exclusiones por zona; en Perú, datos del Niño Costero (ver `fenomeno-el-nino-impacto-personas`) |
| P6 | **Dónde vive la relación:** ¿con la aseguradora, el banco, la billetera o el asistente de IA? | Quien posee la relación decide qué se renueva y quién guarda los datos. | F-981, F-936, F-888, F-998 (embebido, estimaciones incomparables), F-965 (finanzas abiertas) | Renovación y siniestros dentro de billeteras (no solo venta); texto de la norma de finanzas abiertas |
| P7 | **Qué queda humano:** ¿qué momentos exigen una persona? | La IA asiste, pero el apoyo humano sigue siendo necesario en momentos críticos según prospectiva de una aseguradora (F-995), y la mitad desconfía de que la IA decida reclamos (F-982). | F-982, F-984 (demandas por denegaciones automatizadas, sin sentencia), F-995 | Prueba comparada de siniestro con y sin humano en el momento de la decisión |
| P8 | **Perú:** ¿se digitaliza el seguro o solo su cobro? | La mayor parte de lo digital peruano hallado está en vender, cobrar y avisar; poco en proteger a quien hoy no tiene respaldo. | F-879, F-936, F-888, F-884, F-1006, F-913 | Mapa de qué fracción de pólizas se renueva y se reclama digitalmente (§8 del node de digitalización) |

**Cómo se relacionan.** P1 es la raíz: si la promesa no es creíble, P3, P6 y P7 no cambian nada (nadie delega ni integra algo
en lo que no confía). P2 y P5 son los dos extremos del mismo problema (quién queda dentro del sistema). P4 es la salida
optimista de P1 y P5. P8 aterriza todo en un país donde el punto de partida es distinto.

---

## 2. Las tres pistas, separadas

### 2.1 🔬 Pista empírica y teórica

Criterio de validez: arbitraje, método, replicación. Aquí la evidencia directa sobre el futuro es escasa por definición;
lo que hay son piezas que fundamentan las preguntas.

| Fuente | Qué aporta | Rigor |
|---|---|---|
| Godet y colaboradores (F-961); Hiltunen (F-962) | Método: variables clave, juego de actores, escenarios; una señal tiene visibilidad, difusión e interpretación | 🟡 C / 🟢 A (por resúmenes) |
| Eling y Lehmann, 2018 (F-923) | Revisión de 84 artículos: la digitalización afecta la cadena de valor y los criterios de asegurabilidad | 🟢 A |
| Iversen y Rehm, 2022 (F-990) | Más datos polarizan preferencias y fragmentan pools de seguro social en grupos más pequeños y menos redistributivos | 🔵 B (leído por introducción) |
| Geneva Association, 2015 (F-991); Steiner, 2018 (F-992) | Mayor diferenciación de primas; efectos de bienestar poco claros; riesgo de grupos "no asegurables" | 🔵 B |
| Insurance Business y Crooked Timber (F-993) | Distinción mutualista (precio por riesgo individual) vs. solidario (ignora el riesgo); riesgo de clasificación | 🟠 D (opinión) |
| MetaTOC (F-994) | Contrapunto: la individualización del riesgo es anterior al big data | 🟡 C (solo abstract) |
| RCT de seguro por uso, 2026 (F-442) | Único estudio causal hallado de prevención por seguro: cambia la conducta de manejo | 🟢 A |
| Karlan et al., 2014 (F-851); Cole, Giné y Vickery, 2017 (F-852) | Pagos recibidos y de la red mejoran la confianza y la demanda | 🟢 A (agricultura, Ghana e India) |

**Lo documentado.** El pago real genera confianza (F-851, F-852) y el seguro por uso cambia conducta (F-442). **Lo
teórico.** Más datos erosionan la mancomunación (F-990, F-992) con un contrapunto (F-994). **Lo que falta.** No hay evidencia
causal independiente de que un agente de IA mejore o empeore la experiencia de siniestro, ni de qué pasa con la solidaridad
en seguros de vida y salud en un mercado como el peruano.

### 2.2 📱 Pista social y de percepción (la más débil)

Criterio de validez: frecuencia de cobertura y validación social. **No se alcanzó Reddit ni X**; lo que sigue es percepción
medida (encuestas de proveedores) y conflicto público (demandas).

- **Apoyo y confianza se mueven en direcciones distintas.** En EE.UU., el 39% cree buena idea que su aseguradora use IA
  (20% en 2025) y el 84% usa herramientas de IA al menos a veces (F-982). En otra encuesta, la confianza en la IA de las
  aseguradoras bajó de 46% a 40% y el 85% quiere que avisen cuando la usan (F-983). Ambas son de proveedores y no son
  comparables entre sí.
- **El conflicto público está en la decisión automática del reclamo.** Familias de asegurados demandaron a UnitedHealth por un
  algoritmo que habría negado cuidados, y hay una demanda contra Cigna por negar reclamos sin revisión médica; las empresas lo
  niegan y no se halló sentencia (F-984).
- **La ciudadanía ya usa chatbots contra la aseguradora.** Hay guías para redactar apelaciones con IA, con la advertencia de
  que el chatbot puede inventar cláusulas; un dato citado dice que cerca de 1 de cada 5 reclamos dentro de red fue negado en
  HealthCare.gov en 2024 y menos del 1% de los negados se apeló (F-985, 🔴 E, de segunda mano).
- **Precedente de riesgo reputacional por prometer IA en el siniestro:** el caso Lemonade de 2021 (F-869).

**Nivel de instalación social: 🌡️ (tema presente en prensa y en demandas, sin evidencia de debate masivo hallada).** En Perú
no se halló discusión social sobre IA en seguros.

### 2.3 📈 Pista de negocio

Criterio de validez: resultados publicados y verificables. **Casi todo es de proveedores, consultoras o aseguradoras que
describen su propio futuro**; se lee como promesa, no como resultado.

| Tema | Lo hallado | Fuente | Cómo leerlo |
|---|---|---|---|
| Distribución en asistentes de IA | Tuio, Aviva, Liberty Mutual, Insurify, Nsure cotizan en ChatGPT; Insurify reporta +151% de tráfico y +212% de ingresos desde ChatGPT en seis meses; la compra se cierra en el sitio de la aseguradora | F-981 | Cifras propias; un informe citado dice que el canal "sigue sin probarse" |
| IA en la industria | 99,1% del financiamiento insurtech va a IA; solo 4% escaló IA generativa a toda la organización; pilotos de agentes en 74% de aseguradoras grandes | F-901, F-928, F-929 | Mucho piloto, poca escala; definiciones de "escala" distintas |
| Prospectiva de las propias firmas | MAPFRE: cuatro escenarios a 2035; McKinsey: siniestros hacia 2030 con más mitigación y servicio proactivo; EY: nueve tipos de cliente; PwC: los silos impiden la experiencia centrada en el cliente | F-995, F-996, F-997 | Documentos de consultoras y aseguradoras leídos por resumen |
| Seguro embebido | Estimaciones a 2030 desde más de US$70.000 M (EE.UU., Conning) hasta US$270.000 M de primas brutas (Asia, McKinsey) | F-998 | **No comparables**: cada una mide algo distinto |
| Paramétrico | US$3.480 M a US$19.200 M en 2025; la velocidad de pago es característica de producto; Aon: US$260.000 M de pérdidas económicas en 2025, la mitad sin asegurar | F-999 | Rango enorme; los aseguradores no publican datos paramétricos específicos |
| Seguro por uso y prevención | 14,4% de pólizas con telemática; sensores de fuga reducirían entre 39% y 96% la frecuencia según el estudio | F-1000, F-1001 | Estudios apoyados por proveedores; el RCT independiente es F-442 |
| Fracasos | wefox pasó de US$3.000 M de valuación a rescate de €170 M | F-1002 | La pila completa digital no garantiza viabilidad |
| LATAM | 576 insurtechs; inversión de US$199 M en 2025 (+117%); la región pasa de distribuir a habilitar tecnología (más de 51%) | F-1003 | Informe patrocinado; cifras de Celent de segunda mano |
| Infraestructura pública | India: Bima Sugam, Bima Vistaar y Bima Vahak, con retrasos | F-1004, F-905 | Prensa; el modelo "como UPI para seguros" es una apuesta de Estado |
| Riesgos que asegurar | Ciber, n.º 1 por quinto año (42%); IA sube del puesto 10 al 2 | F-989 | Encuesta de una aseguradora a expertos |

**Señal de problema.** La estimación del tamaño del mercado de lo "nuevo" (embebido, paramétrico, uso) varía de 5 a 10 veces
entre firmas (F-998, F-999). Nadie mide lo mismo, y eso es en sí una señal de que el mercado aún no existe de forma
medible.

### 2.4 ⚖️ Regulación y contexto (se separa porque no es ninguna de las tres pistas)

- **Europa:** la IA para evaluar riesgo y fijar precios en seguros de vida y salud de personas es de alto riesgo bajo el
  Reglamento de IA de la UE, según EIOPA (F-986). EIOPA también advierte que en zonas de alto riesgo el seguro puede dejar de
  estar disponible y que las primas de propiedad podrían duplicarse en una década según una asociación alemana (F-987).
- **Perú, IA:** el reglamento de la ley de IA (DS 115-2025-PCM) rige desde el 22 de enero de 2026, clasifica sistemas en
  prohibidos, de alto riesgo y aceptables, y no trae sanciones propias de IA (F-1005). **No se verificó qué usos en seguros
  son de alto riesgo.**
- **Perú, conducta:** las sanciones se concentran en plazos y rechazos del siniestro y en reglas por edad (F-875, F-484); el
  desgravamen dejó de ser automático (F-877).
- **Perú, pagos y datos:** la Ley 32413 permite pagar sueldos en billetera (F-964); la SBS y el BCRP preparan finanzas abiertas
  e iniciadores de pago, con fechas que las fuentes no concilian y sin confirmar si alcanzan a seguros (F-965).
- **Contexto peruano:** 70,7% de empleo informal (F-879); 67% de adultos con cuenta o billetera (F-936); confianza
  institucional 45% (F-881); 14% confía en las aseguradoras según una encuesta de Ipsos citada, que no concilia con el 23-25%
  del node previo (F-934); 31% perdió ingresos y solo 19% tenía respaldo asegurador (F-1006).

---

## 3. ⚖️ Síntesis: dónde convergen, dónde divergen y qué cambia para la pregunta

**Convergen** (las tres pistas, en distinto tono):
- Lo conversacional y lo automático avanzan primero por el lado de **cotizar, avisar y cobrar**, no por el de decidir ni
  pagar el siniestro (F-981, F-982, F-995, F-996).
- **El siniestro es donde se juega la confianza**: la teoría (F-852), la percepción (F-982, F-984) y la regulación peruana
  (F-875, F-484) apuntan al mismo punto.

**Divergen** (no se resuelve):
- **Negocio vs. percepción:** el dinero va a la IA (F-901) y el barómetro de riesgos la ubica entre los dos mayores (F-989),
  pero la confianza del cliente cae (F-983). Posible lectura: la industria compra eficiencia mientras el cliente exige
  transparencia. Es una inferencia, no un hallazgo.
- **Apoyo vs. confianza:** F-982 sube y F-983 baja. Miden preguntas distintas (apoyo a la idea vs. confianza en el uso), con
  muestras y proveedores distintos.
- **Individualización vs. mancomunación:** la teoría plantea una amenaza (F-990, F-992); la regulación europea reacciona
  (F-986); otros dicen que la ruptura es aparente (F-994).
- **Prevención:** hay RCT independiente de que el seguro por uso cambia conducta (F-442), pero las cifras de sensores son de
  proveedores (F-1001) y no hay evidencia independiente de persistencia.

**Lo que esto implica para la pregunta.** Es más defendible hablar de **varias experiencias futuras en tensión** que de una:
la conversacional (donde se decide y se cotiza), la invisible (embebida y automática), la preventiva (el seguro que evita
el daño) y la paramétrica (pago inmediato por un índice). Ninguna elimina el problema de P1.

---

## 4. Experiencias futuras candidatas (hipótesis, no pronósticos)

Cada una con señal a favor, contraseñal y qué la hace falsable.

| Experiencia | Señal a favor | Contraseñal | Cómo se refutaría |
|---|---|---|---|
| **Conversacional:** cotizar y comparar hablando con un asistente | Cuatro aseguradoras y un marketplace ya cotizan dentro de ChatGPT (F-981); 84% usa IA al menos a veces (F-982) | La compra sigue cerrándose fuera del chat (F-981); el canal "sigue sin probarse"; 85% quiere aviso del uso de IA (F-983) | Si en 12-24 meses no aparece una contratación completa dentro del asistente, o si la conversión es menor que en web |
| **Invisible / embebida:** el seguro viene dentro de otra compra o app | Estimaciones de US$70.000-270.000 M (F-998); Yape vende seguro de salud (F-888) | Las estimaciones no son comparables; ~0,18% de la base de Yape como meta de afiliados (F-888); no se conoce renovación | Si la renovación de seguros dentro de billeteras es baja frente a canal directo |
| **Preventiva / proactiva:** la aseguradora evita el daño | RCT de seguro por uso (F-442); McKinsey (F-996); sensores (F-1001) | Evidencia de proveedores; sin dato de persistencia; ¿quién paga el dispositivo? | Si el efecto se desvanece tras el programa o los créditos de prima no compensan el costo |
| **Pago inmediato / paramétrico:** el índice dispara el pago | Valor de la velocidad (F-999); Niño Costero 2026-27 como caso (ver node del Niño) | Riesgo de base (el índice no coincide con la pérdida real); mercado sin datos públicos | Si los pagos paramétricos no llegan realmente más rápido ni se perciben como justos |
| **Infraestructura pública / red compartida:** una plataforma común (tipo "UPI de seguros") | Bima Trinity en India (F-1004, F-905) | Retrasos; es apuesta de un Estado con otras condiciones | Si la plataforma no logra interoperar con aseguradoras privadas |
| **Personalización con tensión de solidaridad:** precio y producto a la medida | Más datos, más diferenciación (F-991); EY: cobertura y servicio a medida (F-997) | Alto riesgo regulatorio en Europa (F-986); riesgo de grupos "no asegurables" (F-992) | Si los reguladores limitan los datos o el mercado castiga a quien segmenta |

---

## 5. Radar de señales

Tipos: **tendencia pesada** (casi segura) · **germen de cambio** (señal débil ya visible) · **incertidumbre crítica** (puede
ir en dos direcciones) · **comodín** (poco probable, gran impacto). Confianza = qué tan sólida es la evidencia, no la
probabilidad del evento.

| # | Señal | Evidencia | Tipo | Pregunta profunda | Indicador a vigilar | Confianza | Pista |
|---|---|---|---|---|---|---|---|
| 1 | **Seguros cotizados en asistentes de IA** | Liberty Mutual, Aviva, Tuio, Insurify; la compra se cierra en el sitio (F-981) | Germen de cambio | P3, P6 | Primera contratación completa dentro del asistente; conversión frente a web | Media-baja: cifras propias | 📈 |
| 2 | **Gradiente de comodidad con la IA** | 51% alertas, 46% cotización, 22% presentar reclamo, 16% cancelar/renovar (F-982) | Tendencia pesada (dirección) | P3, P7 | Misma encuesta repetida; estudio conductual de delegación | Media: un país, un proveedor | 📱 |
| 3 | **Caída de la confianza en la IA de las aseguradoras** | 46% a 40%; 85% quiere aviso (F-983) | Incertidumbre crítica | P1, P3 | Reclamos por decisiones automatizadas; exigencias de transparencia | Baja-media | 📱 |
| 4 | **Decisión automática del reclamo en tribunales** | Demandas contra UnitedHealth y Cigna (F-984) | Germen de cambio | P7, P1 | Sentencias y acuerdos | Baja: sin resolución | 📱 |
| 5 | **Reglas de IA para precios** | Alto riesgo en vida y salud en la UE (F-986); DS 115-2025-PCM en Perú sin detalle de seguros (F-1005) | Germen de cambio | P2 | Texto de las normas peruanas; copia del enfoque europeo | Media (UE) / baja (Perú) | ⚖️ |
| 6 | **Retirada del seguro en zonas de riesgo climático** | EIOPA, Aviva, Allianz (F-987, F-988) | Tendencia pesada | P5 | Retiradas y exclusiones; primas de propiedad | Media: discurso y prensa | ⚖️ |
| 7 | **Ciber e IA como riesgos asegurables y a asegurar** | Ciber n.º 1, IA n.º 2 (F-989) | Tendencia pesada | P5 | Barómetro anual; límites y exclusiones en pólizas ciber | Media | 📈 |
| 8 | **Prevención conectada** | RCT (F-442); sensores y telemática (F-1000, F-1001) | Germen de cambio | P4 | Persistencia del efecto; quién paga el dispositivo | Media (RCT) / baja (sensores) | 🔬 / 📈 |
| 9 | **Pago paramétrico rápido** | Velocidad como producto; mercado mal medido (F-999) | Germen de cambio | P1, P4 | Días reales de pago; reclamos por riesgo de base | Baja | 📈 |
| 10 | **Fracaso de la pila completa** | wefox (F-1002); Lemonade (F-869, F-509) | Incertidumbre crítica | P6 | Cierres y rescates de insurtech | Media | 📈 |
| 11 | **Infraestructura pública de seguros** | Bima Trinity (F-1004, F-905) | Germen de cambio | P6, P8 | Adopción y entregas en la India; ¿algo parecido en LATAM? | Baja | 📈 |
| 12 | **Insurtech de LATAM pasa a habilitadora** | 576 insurtechs, más de 51% habilitadores (F-1003) | Tendencia pesada | P6 | Rondas, consolidación 2026 | Media-baja | 📈 |
| 13 | **Sueldo en billetera** | Ley 32413; DS 011-2026-EF (F-964) | Germen de cambio | P6, P8 | Proporción de trabajadores pagados por billetera; fiscalización | Media: la norma existe, la adopción no se conoce | ⚖️ |
| 14 | **Finanzas abiertas e iniciadores de pago** | SBS y BCRP: fechas que no concilian (2028 o 2029); no se sabe si incluye seguros (F-965) | Germen / incertidumbre | P6 | Texto del alcance; participación de aseguradoras | Baja | ⚖️ |
| 15 | **Billetera como centro financiero** | 67% con cuenta o billetera; Yape ~16 M; Pacífico vende dentro (F-936, F-888) | Incertidumbre crítica | P6 | Seguros **renovados** y reclamados en billeteras; quién guarda los datos | Media | 🏛️ |
| 16 | **Envejecimiento y urbanización** | ~40 M de peruanos y esperanza de vida de 83 años en 2050 (F-963) | Tendencia pesada | P8 | Proyecciones del INEI (no obtenidas) | Media-alta | 🏛️ |
| 17 | **Supervisión de conducta en el siniestro** | Sanciones por plazos y rechazos; desgravamen opcional (F-875, F-484, F-877) | Tendencia pesada | P1 | Sanciones; reclamos | Media-alta | ⚖️ |
| 18 | **Informalidad persistente** | 70,7% en 2025; rural 94,8% (F-879) | Tendencia pesada | P8 | Informalidad; cobertura por billeteras | Alta | 🏛️ |
| 19 | **Pérdida de ingreso sin respaldo** | 31% perdió ingresos y 19% tenía respaldo (F-1006) | Tendencia pesada | P8 | Lo mismo en otras encuestas | Media | 🏛️ |
| 20 | **Confianza en aseguradoras** | 14% (Ipsos citado) vs. ~23-25% del node previo; confianza institucional 45% (F-934, F-881) | Incertidumbre crítica | P1 | Medición propia | Baja: no concilian | 🏛️ |
| 21 | **Trabajadores de plataformas sin cobertura** | Sin oferta vigente hallada (F-913) | Germen débil | P8 | Normas sobre repartidores; oferta de plataformas | Baja | 🏛️ |
| 22 | **Pérdida masiva de confianza en un canal** (falla de una billetera, estafas con pólizas falsas, como el SOAT de 2022) | Caso puntual (F-884) | Comodín | P1 | Incidentes de fraude | Baja: sin evidencia directa | 🏛️ |
| 23 | **Clima: Niño Costero 2026-27** | Ver `fenomeno-el-nino-impacto-personas` | Tendencia pesada / comodín | P5, P4 | ENFEN; siniestros por desastre | Media | 🏛️ |

**Variables clave candidatas** (a validar con análisis estructural, no con este node): credibilidad del pago del siniestro ·
quién posee la relación con el cliente · costo de servir por canal · regulación de conducta y de IA · apertura de datos ·
formalización del ingreso · conectividad · uso de IA en siniestros · exposición climática · envejecimiento · tecnología de
pagos · poder de los canales (bancos, billeteras, corredores, asistentes de IA).

---

## 6. Escenarios exploratorios a 2035 (hipótesis, sin probabilidades)

Dos incertidumbres críticas sostienen el cuadro. **No son las únicas posibles**; salen de las preguntas P1 y P6.

| | **Promesa de pago poco creíble** | **Promesa de pago creíble** |
|---|---|---|
| **El asistente, la billetera o el banco posee la relación** | *Seguro como accesorio barato:* micropólizas dentro de apps y asistentes; poca renovación y poca reclamación; la aseguradora es proveedora invisible | *Seguro como función de la plataforma:* el cliente confía y renueva dentro de la app; la aseguradora compite por ser la elegida en el menú del asistente |
| **La aseguradora o el corredor posee la relación** | *Híbrido defensivo:* el corredor y el papel siguen siendo el ancla; lo digital queda en cotizar y pagar | *Relación directa con datos abiertos:* la aseguradora gestiona el ciclo completo con consentimiento, y la prevención hace parte del producto |

**Relación con MAPFRE (F-995).** Sus cuatro escenarios (del "muro" que frena el avance digital a la "utopía" de acceso
universal a sistemas personalizados) varían principalmente el **grado de avance tecnológico y de acceso**. El cuadro de arriba
varía **quién posee la relación y qué tan creíble es el pago**. No se mapean uno a uno; sirven como contraste. No se pudo
abrir el informe, solo notas de prensa.

**Qué cambia para las tres definiciones basales** (ver `digitalizacion-seguros-mercados-emergentes` §5b):
- En el escenario de accesorio, la fidelidad (renovar por elección) sería escasa y el cliente de alto valor se definiría casi
  solo por costo de servir.
- En el de función de la plataforma, el cliente digitalmente sano depende del canal ajeno y la fiabilidad pasa a ser del socio.
- En el de relación directa, el cliente de alto valor incluye el valor de los datos que consiente compartir y el ahorro por
  prevención.

---

## 7. Implicaciones para Perú (hipótesis para validar)

1. **Probar P1 antes que innovar en la interfaz.** Si el pago no es creíble, una experiencia conversacional o embebida
   captura venta pero no renovación. Medir tiempo y tasa de pago por canal es la señal de mayor valor y menor costo.
2. **Mirar renovación y siniestro en billeteras, no solo ventas.** La meta de Yape/Pacífico (30.000 afiliados en el primer
   año, ~0,18% de la base, F-888) dice que vender es lo fácil.
3. **Preguntarse a quién protege lo digital.** Con informalidad de 70,7% y solo 19% con respaldo ante pérdida de ingresos,
   el gran hueco es el seguro de ingresos y de salud para independientes; no se halló oferta digital vigente para
   trabajadores de plataformas (F-913). Es una pregunta de producto, no de tecnología.
4. **Prepararse para la regulación de IA y datos sin esperar.** El texto peruano no se verificó, pero la dirección europea
   (alto riesgo en precios de vida y salud, F-986) y las sanciones locales por plazos y rechazos (F-875) sugieren que la
   transparencia de las decisiones automatizadas va a pesar.
5. **Cuidar el sesgo de supervivencia.** Casi todas las cifras de negocio son de quien vende. Antes de decidir, pedir
   evidencia independiente.

---

## 8. Hipótesis vivas (para confrontar, no para confirmar)

| # | Hipótesis | Qué la respalda hoy | Qué la refutaría |
|---|---|---|---|
| FH1 | La confianza en el pago del siniestro condiciona la renovación más que la experiencia de compra | Karlan y Cole (F-851, F-852) en agricultura; resto es inferencia | Un experimento en Perú que muestre renovación alta sin pago creíble |
| FH2 | La delegación al agente se queda en lo de apoyo mientras no haya un historial de aciertos | Gradiente de comodidad (F-982) | Aumento sostenido de comodidad en renovación o reclamo autónomo |
| FH3 | El asistente de IA será canal de captación, no de contratación, al menos 2-3 años | F-981 | Contratación completa dentro del asistente con conversión comparable |
| FH4 | Más datos reducen la mancomunación en vida y salud antes que en otros ramos | F-990, F-986 (por qué la UE lo trata como alto riesgo) | Regulación o mercado que mantengan precios comunes sin pérdida de clientes |
| FH5 | La prevención conectada solo escala si alguien distinto al cliente paga el dispositivo | Créditos de prima pequeños (3-8%, F-1001), vendedores de dispositivos | Adopción alta con pago del propio cliente y efecto persistente |
| FH6 | En Perú, lo digital llega primero a quien ya está bancarizado, no a quien carece de respaldo | F-879, F-936, F-1006 | Oferta digital con adopción alta entre informales |

---

## 9. Limitaciones y pendientes

**Limitaciones**
- Lectura por resúmenes; ningún informe se abrió completo. McKinsey, MAPFRE, EY, PwC y Celent se leyeron por prensa.
- **Pista social débil** (sin Reddit ni X; encuestas de proveedores).
- **Cifras de proveedores** (Insurity, Smart Communications, Insurify, LexisNexis/Flo, Mordor, Lockton): no independientes.
- **EE.UU. y Europa dominan** la evidencia sobre IA y percepción; en Perú no se halló encuesta equivalente.
- **Fechas de finanzas abiertas discrepan** entre fuentes (F-965); el contenido de la norma de IA en seguros no se verificó
  (F-1005).
- **No es un ejercicio Godet real**: sin taller, sin análisis estructural ni juego de actores. Las 23 señales y las 6
  experiencias son lectura mía.

**Pendientes (en orden de valor)**
1. Taller con expertos de la aseguradora y de fuera para validar y priorizar las variables clave.
2. Análisis estructural (influencia y dependencia) y juego de actores (aseguradoras, bancos, billeteras, reguladores,
   corredores, asistentes de IA); escenarios con ejes o SMIC.
3. Leer el texto de la norma de IA (DS 115-2025-PCM) y la hoja de ruta de finanzas abiertas para saber si alcanzan a seguros.
4. Obtener las proyecciones de población del INEI.
5. Una medición propia de confianza y de tiempo de pago por canal en Perú.
6. Revisar el radar cada trimestre con las rutinas de `/trinidad`.

---

## 10. Ledger usado

Fuentes nuevas: **F-981 a F-1006** (empírica/teórica F-990 a F-994 · percepción/social F-982 a F-985 · negocio F-981 y F-989,
F-995 a F-1004 · regulación F-986, F-987, F-1005 · contexto F-1006 · prensa F-988). Reutiliza F-961 a F-965, F-442, F-509,
F-851, F-852, F-869, F-875, F-877, F-879, F-881, F-884, F-888, F-901, F-905, F-913, F-923, F-928, F-929, F-934, F-936.
Todas están en `research/fuentes/codice.md`.

---

## 11. Actualización v1.1 (2026-10-27): nuevas señales tras revisar fuentes aportadas

*Origen: nueve fuentes aportadas por la persona usuaria, clasificadas en `digitalizacion-seguros-mercados-emergentes` §12. Todo se leyó por resumen de búsqueda.*

**Qué cambia en una línea:** la señal 14 (finanzas abiertas) pasó de "norma futura" a "proyecto en consulta pública", y se suman cuatro señales (24 a 27). El radar queda en **27 señales**.

| # | Señal | Evidencia | Tipo | Pregunta profunda | Indicador a vigilar | Confianza | Pista |
|---|---|---|---|---|---|---|---|
| 14 (actualiza) | **Finanzas abiertas en Perú: consulta pública** | La SBS autorizó el 2-oct-2026 la consulta del proyecto de Reglamento General (Res. 02433-2026; 18 días) y después de los Títulos V a VII (Res. 02519-2026) (F-1064). Un reportaje que cita el boletín de un bufete dice que contempla a las aseguradoras (F-1063, F-1062) | Germen de cambio | P6 | Texto final; mención expresa de seguros; calendario de entrada; en Chile el plazo se movió de jul-2026 a jul-2027 (F-1050) | Media-baja: el alcance a seguros **no se verificó en la norma** | ⚖️ |
| 24 | **Financiamiento insurtech concentrado en vida y salud** | Life & Care: 26% de las insurtechs y 76% del financiamiento del 1S 2026; movilidad: 211 empresas y 9%; ticket medio de US$8,2 M (F-1068) | Germen de cambio | P6, P7 | Reparto por segmento en el 2S 2026 y 2027 | Media-baja: informe patrocinado por una aseguradora | 📈 |
| 25 | **Aseguradoras tradicionales compran distribuidores digitales** | En jul-2026 MAPFRE anunció que adquiriría 38,9% de Tuio, que ya cotizaba en ChatGPT (F-1068, F-981) | Germen de cambio | P6 | Otras compras o alianzas de aseguradoras con distribuidores de IA | Media: nota de MAPFRE, parte interesada | 📈 |
| 26 | **Brecha de protección frente a catástrofes en LATAM** | 81,0% en 2015-2024: solo 19% de US$100.000 M de pérdidas aseguradas; Asia 82,8%, Norteamérica 43,2% (F-1069) | Tendencia pesada | P5 | Informe de MAPFRE Economics y Swiss Re cada año | Media: parte interesada con datos de reaseguradora | 💼 |
| 27 | **Adopción de IA por aseguradoras mexicanas** | Entre 15% y 20% usa IA, sobre todo en fraude, suscripción y atención (AMIS, vía LexLatin; F-1063) | Germen de cambio | P3, P7 | Encuesta de AMIS repetida; reglas de IA en México (hoy sin ley general) | Baja: gremio, de segunda mano | ⚖️ |

**Reglas de lectura.**
- La señal 25 une dos piezas del foresight: la distribución dentro de asistentes de IA (señal 1) y la estrategia de una aseguradora tradicional. No se halló que Tuio venda dentro de ChatGPT con resultados; solo que cotiza.
- La señal 26 refuerza P5 (asegurabilidad) con un dato latinoamericano; antes solo había Europa (F-987).
- **No cambia la conclusión de §1:** la credibilidad del pago sigue siendo la pregunta de fondo.

**Pendiente actualizado.** El pendiente 3 de §9 (leer el texto de finanzas abiertas) avanzó: el proyecto existe y está en consulta, pero **falta abrir el texto y buscar la mención de seguros**.

---

## 12. Actualización v1.2 (2026-10-27): tendencias globales y de LATAM, ordenadas por las preguntas abiertas de un documento de estrategia

*Origen: la persona usuaria pidió las **tendencias globales y latinoamericanas** en seguros, insurtech y digitalización, tomando como punto de partida un documento interno de estrategia que cuestiona varias cosas. Ese documento **no se copia ni se resume aquí** (repositorio público); solo se reformulan, en términos genéricos, las **preguntas** que abre, y se busca qué dicen las fuentes públicas sobre cada una. Todo se leyó por resumen de búsqueda; la pista social no se corrió.*

### 12.1 Respuesta corta

**Las tendencias globales más repetidas tienen más promesa que resultado medido.** Siete, de más a menos respaldadas por datos:

1. **Costos médicos de dos dígitos y persistentes:** 10,3% global proyectado para 2026, 14,0% en Asia-Pacífico y **11,9% en América Latina** (desde 10,5%), la mayor aceleración; 55% de las aseguradoras de salud espera que se mantenga más de tres años (F-1102).
2. **La IA pasa de asistente a agente, pero casi no escala:** solo 22% de las aseguradoras la llevó a producción a escala, aunque 66% de la plantilla ya usa herramientas de IA; el cuello de botella sería confianza y gobierno, no tecnología (F-1103; coincide con F-928 y F-929).
3. **El capital se concentra en la IA:** 95% del financiamiento insurtech del 1T 2026 y 99,1% del 2T fue a empresas de IA (F-1065, F-901).
4. **De pagar a prevenir:** es el discurso dominante (F-1103, F-996), pero la prueba causal es mínima: un experimento de seguro por uso (F-442) y un programa digital de diabetes cuyo ahorro desaparece al segundo año (F-1108).
5. **Embebido y plataformas toman la relación con el cliente:** las estimaciones de mercado varían de 5 a 10 veces según la firma (F-998); aseguradoras y comparadores ya cotizan en asistentes de IA, y la compra se cierra en su propio sitio (F-981).
6. **Más riesgo que no se deja asegurar:** ciber es el riesgo n.º 1 de las empresas y la IA el n.º 2 (F-989); las aseguradoras se retiran de zonas de alto riesgo climático (F-987, F-988).
7. **Regulación de la IA y de los datos:** en Europa, la IA que fija precios en vida y salud es de alto riesgo (F-986).

**En América Latina y Perú**, de más a menos respaldadas:

1. **Costo médico y brecha de protección:** 11,9% de tendencia médica (F-1102) y 81,0% de brecha de protección frente a catástrofes (F-1069).
2. **Ecosistema insurtech que madura y se concentra:** 576 empresas, mortalidad anual de 6,9% (de 12,7% en 2024), 76% del financiamiento a vida y salud con 26% de las empresas (F-1068). Informe patrocinado por una aseguradora.
3. **Distribución todavía intermediada:** agentes y corredores aportan 60-65% de las primas en la región (F-375), ~50% en México (F-1072); en Perú hay plataformas para corredores, sin cifra de participación reciente (F-1107).
4. **Compra digital en productos simples y obligatorios, con fraude:** ~90% de los SOAT peruanos son digitales (F-884) y el SOAT en línea acumula miles de reportes de fraude en Colombia (F-1047).
5. **Regulación en movimiento:** proyecto de finanzas abiertas de la SBS en consulta pública (F-1064; alcance a seguros sin verificar), sandbox ampliado (F-1106), reglamento de IA vigente (F-1005); en Chile el calendario de finanzas abiertas se mueve a 2027 (F-1050).
6. **IA con datos contradictorios:** 43% de aseguradoras latinoamericanas con IA generativa en producción (Celent, de segunda mano, F-1003) frente a 15%-20% de aseguradoras mexicanas que usan IA (AMIS, F-1063).
7. **Mercado lento:** en Perú, primas del 1S 2026 con solo +1,1% (F-506) y siniestralidad retenida del sistema de 39,3% (2025) a 40,6% (1T 2026) (F-1105).

### 12.2 Las preguntas abiertas y lo que dicen las fuentes

Solidez: 🟢 con causalidad · 🔵 institucional o con método · 🟡 encuesta o estudio de consultora · 🟠 prensa, proveedor o cifra propia.

| # | Pregunta que abre el documento | Tendencia global | América Latina y Perú | Solidez | Qué sigue abierto |
|---|---|---|---|---|---|
| 1 | **¿Con qué se mide lo digital: venta y uso, o resultado?** | Los estudios que miden resultado relacionan madurez digital con rentabilidad relativa, sin causalidad (F-1099, F-1101); la compra digital sube (47% de pólizas nuevas de auto y hogar en EE.UU.) mientras baja la satisfacción y solo 11% usa un chatbot (F-1094) | No hay medición pública local | 🟡 | Efecto causal de lo digital en el ratio combinado |
| 2 | **¿Dónde está el dinero: siniestralidad o costo de servir?** | Propiedad y accidentes de EE.UU. 2024: siniestros 71,0% y gastos 25,2% de la prima (F-1091); las aseguradoras esperan mejorar la siniestralidad 3 a 8 puntos y ahorrar 10% a 20% en otras partes (F-1100) | Siniestralidad retenida del sistema peruano 39,3% (2025) y 40,6% (1T 2026) (F-1105); en salud, la tendencia médica de 11,9% (F-1102) | 🟡 / 🟠 | Peso de gastos y siniestros por ramo en Perú (no público por ramo) |
| 3 | **¿La autogestión resuelve o termina en llamada?** | Brecha entre lo que se ofrece y lo que se quiere: 59% de menores de 40 quiere relación digital directa y 31% de aseguradoras la ofrece (F-1096); el uso de chatbots es bajo (F-1094) | Siniestros por WhatsApp con IA en Brasil, sin resultados (F-893); SOAT vendido por una cuenta verificada de WhatsApp en Colombia (F-1047) | 🟡 | Tasa de resolución sin humano (no se publica) |
| 4 | **¿Una sola relación con el cliente (un perfil, una entrada)?** | Ping An: 2,94 contratos por cliente y 99% de retención en quienes tienen tres o más categorías (selección) (F-1092); agrupar productos se asocia a más retención (F-1018) | Billeteras con seguros (Yape, Mercado Pago, OXXO: F-888, F-1051 a F-1053), sin resultados; finanzas abiertas en consulta en Perú (F-1064) | 🟠 | Si la vista única causa mejor retención o solo la refleja |
| 5 | **¿Prevenir en lugar de indemnizar?** | Es el discurso de 2026 (F-1103, F-996); un RCT de seguro por uso cambia la conducta (F-442); un programa digital de diabetes ahorra en el año 1 y no en el 2 (F-1108); en Discovery, 30% menos siniestros de auto entre los 'avanzados y comprometidos', con selección (F-1093) | Interés alto en prevención en Brasil (97%) (F-1095); parámetrico para el Niño Costero (ver `fenomeno-el-nino-impacto-personas`) | 🟢 un RCT; 🟠 el resto | Evidencia causal de prevención en salud y vehículos; quién paga el dispositivo |
| 6 | **¿La IA como motor de decisión (suscripción, precio, siniestros)? ¿Depende del dato?** | 22% escaló la IA y 66% de la plantilla la usa (F-1103); IA generativa a escala en 4% (F-928) y 7% (F-929); IA de precios en vida y salud, de alto riesgo en la UE (F-986); la confianza del cliente baja a 40% (F-983) | 43% (Celent, dudoso) frente a 15%-20% (AMIS) de uso de IA (F-1003, F-1063); decreto peruano de IA vigente, sin detalle para seguros (F-1005) | 🟡 / 🟠 | Calidad y unificación del dato como cuello de botella: sin evidencia pública local |
| 7 | **¿El corredor como principal usuario de lo digital?** | Las agencias más digitales crecen más rápido, con selección (F-1097) | Agentes y corredores, 60-65% regional (F-375), ~50% en México (F-1072); plataformas para corredores en Perú, la mayoría de 2022 (F-1107) | 🟡 / 🟠 | Participación del corredor en Perú 2025-2026 (no hallada) |
| 8 | **¿Qué se vende en digital y qué no, según el ramo?** | Auto y hogar: 47% digital en EE.UU. (F-1094); vida: 59% frente a 31% de oferta (F-1096) | SOAT ~90% digital (F-884), producto obligatorio y de precio regulado; el financiamiento va a vida y salud (F-1068) | 🟡 / 🟠 | Participación digital por ramo en Perú |
| 9 | **¿Qué pasa con los costos médicos?** | 10,3% global; Asia-Pacífico 14,0%; Norteamérica 9,2%; Europa 8,2% (F-1102) | **11,9% en América Latina**, excluyendo Argentina, desde 10,5% (F-1102) | 🟡 | Impulsores para LATAM y siniestralidad de salud en Perú |
| 10 | **¿Entran terceros con seguro embebido?** | Estimaciones incomparables (F-998); cotización en asistentes de IA (F-981); embebido europeo de US$49.000 M a 2030, sin verificar (F-1104); MAPFRE toma 38,9% de Tuio (F-1068) | Mercado Pago y OXXO lanzan micropólizas sin resultados públicos (F-1052, F-1053); Fitch lo ve como requisito para competir (F-1065) | 🟠 | Pólizas, renovación y siniestros de lo embebido en LATAM: ninguno público |
| 11 | **¿Qué regulan el dato y la IA, y se puede cruzar datos para tarificar?** | Alto riesgo para precios de vida y salud en la UE (F-986) | Peru: finanzas abiertas en consulta (F-1064), sandbox ampliado (F-1106), decreto de IA (F-1005); Chile: finanzas abiertas a 2027 (F-1050); México: sin ley general de IA (F-1063) | 🔵 / 🟠 | Si las finanzas abiertas del Perú alcanzan a seguros (no verificado) |
| 12 | **¿Qué riesgos y qué ciclo presionan?** | Ciber n.º 1 e IA n.º 2 (F-989); retirada de zonas climáticas (F-987); mercado blando en líneas comerciales (F-1065) | Brecha de protección de 81,0% (F-1069); mercado peruano lento en 2026 (F-506) | 🟡 / 🔵 | Impacto del Niño Costero 2026-27 en siniestros |

### 12.3 Lectura (inferencias mías)

1. **Las preguntas 1, 4 y 6 no se pueden responder con fuentes públicas.** Las tendencias globales dicen hacia dónde va la industria, no si una decisión local rinde. Se responden con dato propio y con diseños que separen la selección.
2. **Donde hay cifra sólida es en el entorno:** costos médicos, brecha de protección y estructura de costos de otros mercados. Es lo que sirve para dimensionar.
3. **Casi todas las tendencias de oferta (IA, embebido, prevención) vienen de proveedores o de las propias aseguradoras.** Las de demanda (lo que quiere el cliente) vienen de encuestas de consultoras en mercados maduros.
4. **Perú tiene pocos datos públicos locales por ramo:** primas y siniestralidad por ramo, participación de corredores y del canal digital no se hallaron.

### 12.4 Discrepancias de las fuentes que conviene conocer

- **Primas del sistema peruano:** las cifras de prensa no coinciden porque miden cosas distintas. Al 1S 2026, las **primas** (que descuentan el ajuste por reservas técnicas) crecieron +1,1% hasta S/ 9.451 M, y las **primas netas** crecieron +8% hasta S/ 12.385 M (SBS, vía Gestión; F-1105). La diferencia es el ajuste por reservas, que pesa más en aseguradoras con rentas vitalicias. Aun así, hay que ver la definición antes de comparar con S/ 19.915 M de 2024 o S/ 24.520 M anualizadas a marzo de 2026. Es una explicación de la prensa; no la verifiqué en las tablas de la SBS.
- **Resolución SBS 01747-2026 (corregido el 2026-10-27):** es el **Reglamento de Banking as a Service (BaaS)**, no un reglamento general de productos digitales innovadores ni solo de apertura de cuentas y créditos. Su lista de servicios incluye también **bancaseguros** (F-1111). Las dos descripciones de prensa que había leído eran parciales.
- **Adopción de IA en LATAM:** 43% (Celent, de segunda mano) frente a 15%-20% en México (AMIS) no se concilian: miden países, definiciones y fechas distintos.

### 12.5 Límites y pendientes

**Límites.** Todo se leyó por resumen o extracto. Las encuestas son de proveedores y consultoras. No se corrió la pista social. Las normas peruanas no se abrieron; se leyeron a través de análisis jurídicos y de un boletín de abogados.

**Pendientes.**

1. Estadísticas de la SBS por ramo y por compañía: primas, siniestralidad y gastos (solo hay totales del sistema).
2. Participación de los corredores y del canal digital en las primas peruanas.
3. Texto completo del reglamento BaaS y de la norma de finanzas abiertas: ¿puede una aseguradora ser proveedora o receptora, o solo entra por bancaseguros? (el calendario general ya está en §12.7)
4. Desglose de impulsores del costo médico para LATAM en el informe de WTW.
5. Verificar Celent frente a AMIS sobre uso de IA.
6. Abrir el PDF de Moody's Local (abril de 2026): la cifra de primas totales de 2025 no se localizó en los extractos.
7. Leer en la norma original si el reglamento de la Ley 31814 trata la tarificación de seguros como IA de alto riesgo.

### 12.6 Actualización SBS y regulación peruana (2026-10-27)

**Fuentes.** Boletín de Pérez-Llorca del tercer trimestre de 2026 (sección de Perú y carta inicial; F-1110), reglamento BaaS (F-1111) e informe de Moody's Local (F-1112). El boletín es de un estudio de abogados que resume normas para sus clientes (🟡 C); lo usé para saber qué normas existen y qué dicen en lo grueso, no para citarlas.

**El mercado en cifras (medidas distintas, no mezclar):**

| Medida | Cifra | Fuente | Nota |
|---|---|---|---|
| Primas, 1S 2026 (descuentan reservas) | S/ 9.451 M, +1,1% | SBS vía Gestión (F-1105) | Mide menos que las primas netas |
| Primas netas, 1S 2026 | S/ 12.385 M, +8% | SBS vía Gestión (F-1105) | |
| Utilidad neta conjunta, 1S 2026 | S/ 1.391 M, +7,5% | SBS vía Gestión (F-1105) | 7 de 17 empresas a la baja y una con pérdidas |
| Primas netas anualizadas, mar-2026 | S/ 24.520 M, +8,8% | APESEG vía Gestión (F-1105) | |
| Siniestralidad retenida | 39,30% a fines de 2025 (42,19% en 2024); 40,6% al 1T 2026 | Moody's Local (F-1112); APESEG (F-1105) | Moody's espera peor siniestralidad en 2026 por un posible Niño |
| Resultado técnico 2025 | −13,64% | Moody's Local (F-1112) | Más comisiones, gastos técnicos y siniestros |
| Crecimiento esperado 2026 | 8%-9% | Moody's Local (F-1112) | Proyección, no dato |
| Penetración y densidad | ~2% del PBI; ~US$ 203 por habitante | Moody's Local vía Gestión | |

**Lectura (inferencia mía).** Las primas netas crecen, pero lo que queda después de reservas, comisiones y siniestros se aprieta (resultado técnico de 2025 en −13,64%). Ese es el contexto en que se decide cuánto invertir en digitalizar. Esto es coherente con la pregunta 2 de §12.2 (¿dónde está el dinero?), pero con totales del sistema no se puede decir qué ramo o qué empresa lo explica.

**Normas peruanas de 2026 que tocan lo digital** (según el boletín; sin abrir los textos):

| Norma | Qué hace | Por qué importa a la experiencia digital | Estado |
|---|---|---|---|
| Res. SBS 01747-2026 (BaaS) | Una plataforma no financiera se alía con un banco o caja para ofrecer cuentas, créditos, tarjetas y bancaseguros; el banco o caja sigue respondiendo ante el cliente | Es la vía por la que el seguro podría venderse dentro de apps ajenas, con el banco o caja como responsable (pregunta 10, *embebido*) | Vigente 180 días después de su publicación (hacia fines de dic-2026, cálculo mío) |
| Res. SBS 1029 y 1923-2026 (infracciones) | El deber de asesorar abarca oferta, suscripción, ejecución, reclamo y cobro; la intermediación a distancia debe informar del producto y del derecho de arrepentimiento; el rechazo de cobertura se comunica con su sustento | Lo digital queda bajo supervisión de conducta en todo el ciclo, no solo en la venta | Vigentes |
| Res. SBS 2260-2026 (paramétricos) | Reglamento de seguros paramétricos solo para riesgos climáticos y de la naturaleza; aviso de activación en 2 días y pago en 10 días calendario; sin deducibles ni coaseguro | Primer marco para pago automático por umbral, pero **el público inicial no es el minorista** (organismos públicos, corporativos, grandes empresas) | Vigente |
| Proyecto de ley de delegación (28-ago) | Activación paramétrica de compensaciones del FOGASA y base legal para consultar identidad en RENIEC | La verificación de identidad en línea es un cuello de botella de la contratación digital | **Solo proyecto**, sin aprobar |
| Res. SBS 2133-2026 (autorización de empresas) | Tres modalidades de autorización, precalificación y menos plazos | Probablemente baja la barrera de entrada: la SBS autorizó a Nacional de Seguros como la aseguradora n.º 18 (Res. 1317-2026) | Vigente |
| Proyecto de gestión actuarial (Res. 1771-2026) | Calidad de datos, actuario designado, backtesting y juicio experto regulado | Los modelos de tarificación y de datos alternativos tendrían que ser documentados y auditables (pregunta 11) | **Solo consulta pública** |
| Reglamento de la Ley 31814 (IA, set-2025) | Marco general de IA con niveles de riesgo, usos prohibidos y de alto riesgo | Regula la IA en general; el boletín **no dice** si cubre la tarificación de seguros | Vigente |

**En la región (según el boletín):** la UE trata como alto riesgo la IA de tarificación en seguros de vida y salud de personas; Colombia tiene la política CONPES 4144 y un proyecto de ley inspirado en el reglamento europeo; México regula con la Circular Única de la CNSF y la ley de protección de datos, sin ley general de IA. **Inferencia mía:** Perú y la UE tienen norma aplicable hoy; Colombia y México todavía no.

**Qué cambia para las preguntas abiertas.**

1. *¿Quién tiene la relación?* (pregunta 4) El BaaS abre una vía legal para que la relación la tenga una plataforma ajena, pero con el banco o caja como responsable. Si una aseguradora puede ser proveedora o solo entra por bancaseguros, no se sabe.
2. *¿Qué se vende digital?* (pregunta 8) Los paramétricos entran por empresas, no por personas: el seguro paramétrico minorista que se discute por el Niño no tiene aún reglamento propio.
3. *Regulación de datos e IA* (pregunta 11) Hay norma general de IA vigente y un borrador actuarial que exige calidad de datos; falta saber cómo se aplican a la tarificación.

**Casos de INDECOPI que muestran por dónde se disputa lo digital** (sobre decisiones de primera instancia, resumidas por el boletín): una aseguradora alegó que el cliente eligió una cobertura por su canal de comercio electrónico y que le avisó del cambio por correo un día después del siniestro; la comisión no encontró pruebas de la negativa de cobertura y declaró prescrita la modificación unilateral, pero dejó la vía judicial abierta. Es un solo caso; indica que la **prueba de lo que el cliente vio y aceptó en un canal digital** es un tema de litigio, no que sea frecuente.

### 12.7 Finanzas abiertas (open banking y open insurance): qué hay (2026-10-27)

**En corto.** La banca abierta va primero en todos lados y el seguro abierto va detrás. Brasil es el único caso con open insurance funcionando y no hay cifras públicas de beneficio para el consumidor. En Perú, los seguros entrarían hacia 2029; antes llegan el reglamento BaaS (fines de 2026) y la banca abierta (2028). Es lo que alcancé a leer en extractos y notas de prensa; las fechas discrepan entre fuentes.

| País | Estado | ¿Entran los seguros? | Fuente |
|---|---|---|---|
| **Brasil** | Open Insurance en operación desde la Resolución CNSP 425/2021, supervisado por la Susep; la Res. Susep 61/2025 afina el modelo; el grupo de trabajo se prorrogó un año (2026) con foco en simplificar el consentimiento | **Sí, ya** (obligatorio al inicio para las aseguradoras más grandes) | F-1115 |
| **Colombia** | Decreto 368 de 2026: finanzas abiertas obligatorias para las entidades vigiladas; el cronograma de estandarización se ampliaría 6 meses (según un solo boletín de bufete) | **Sí, por decreto**; su hoja de ruta se fija en el cronograma de la SFC | F-1114 |
| **Chile** | NCG 514 de 2024; la entrada prevista para jul-2026 se propone mover a jul-2027 | Sin calendario para aseguradoras | F-1050 |
| **México** | Ley Fintech de 2018; reglas de datos abiertos pendientes | No se halló norma para seguros | búsqueda sin fuente registrada |
| **Perú** | Hoja de ruta de la SBS (feb-2026) en cuatro fases: regulación y estándares 2026-2027, banca abierta 2027-2029, finanzas abiertas desde 2029; consulta del reglamento general en curso (octubre-noviembre de 2026) | **Después de la banca**: seguros, pensiones, cooperativas y fintechs "desde 2029", sin lista de aseguradoras | F-1113 |

**Qué muestran las tendencias (inferencias mías).**

1. **El seguro abierto llega tarde y sin prueba de beneficio.** El único indicador público de Brasil son las llamadas técnicas a las APIs (de 8,4 M a 15,2 M entre 2023 y 2024). Eso mide uso técnico, no consentimientos ni mejores ofertas. El propio comité del sistema pide convertir los datos compartidos en servicios útiles para el consumidor (F-1115).
2. **El consentimiento es un problema de diseño de conducta.** Que Brasil priorice "simplificar el trayecto de consentimiento" indica fricción. No encontré tasas de consentimiento en seguros. Es una hipótesis para probar, no un hallazgo.
3. **Para una aseguradora peruana, lo primero que cambia no es el open finance.** Orden probable: (a) reglamento BaaS, vigente hacia fines de 2026, que permite vender bancaseguros dentro de apps ajenas (F-1111); (b) banca abierta desde 2028, que le da a los bancos datos transaccionales del cliente (F-1113); (c) seguros abiertos hacia 2029, si se cumple el calendario. La obligación para las aseguradoras llega al final. Es una lectura del calendario, y el calendario puede moverse.
4. **Quien tenga los datos bancarios tendrá ventaja para ofrecer seguros.** Es plausible, no probado: con consentimiento, un banco o una billetera podría ajustar la oferta a ingresos y gastos. Las aseguradoras sin banco no verían esos datos hasta el seguro abierto.
5. **Colombia es el caso regional más cercano de obligación para aseguradoras y corredores.** Su cronograma, aún por publicar, mostrará cómo se implementa en seguros.

**Pendiente de verificar.** El texto de los lineamientos y del reglamento (qué datos de seguros y cuándo); si las fechas de comentarios son las de la SBS o las de la prensa; el Decreto 1489 de Colombia (solo hay un boletín); consentimientos reales del Open Insurance de Brasil.

### 12.8 Seguros que se venden por Yape: qué cambia y qué todavía no se sabe (2026-10-27)

**En corto.** Cambia la distribución y quién tiene la relación con el cliente. Todavía no se sabe si cambia la economía del seguro: no hay cifras públicas de ventas por Yape, renovación ni siniestralidad.

**Lo observado (dato).**

- **Qué se vende.** En la app hay seguros de vida (S/ 5,99 al mes por S/ 10.000), de salud (S/ 9,90 con teleconsultas y S/ 500 por hospitalización), de robo del celular (desde S/ 4,90), de fraude en cuentas Yape y BCP (S/ 4,99 por hasta S/ 3.500), SOAT y uno para emprendedores. La aseguradora es Pacífico. Los precios vienen de notas de 2024-2025 y pueden haber cambiado (F-1116).
- **Quién es el dueño.** Yape, el BCP y Pacífico pertenecen al mismo grupo (Credicorp). Los reportes de Credicorp incluyen *insurtech* dentro de una cartera de innovación que pesó 8,1% de los ingresos ajustados por riesgo en el 4T25 (F-529).
- **Escala del canal.** Entre 15,9 M y 17 M de usuarios activos según la fuente y la fecha; Credicorp reporta 16,4 M y un ingreso por usuario de S/ 10,3 (+65%), sin decir cuánto viene de seguros (F-1117, F-936).
- **Resultados de seguros.** Un publirreportaje dice que la alianza llegó a más de un millón de clientes de Pacífico, sin separar por producto ni año. La meta de salud era de 30.000 afiliados en el primer año, cerca de 0,18% de los usuarios (F-888). El resultado de suscripción de seguros de Credicorp cayó 9,1% en el 2T26 por líneas comerciales, autos y vida, no por Yape (F-1117).

**Lo que cambia (inferencias mías, ordenadas de más a menos firmes).**

1. **El costo de llegar al cliente baja casi a cero.** El seguro se ofrece en una pantalla que el usuario ya abre cada día, con precios de microproducto. Es inferencia desde la oferta; no conozco el costo real de adquisición.
2. **La relación queda en la billetera, que es del mismo grupo.** Esto encaja con el escenario *seguro como accesorio barato* del 2×2 de §6: la billetera posee la relación y la confianza en el pago del siniestro es baja. No hallé aseguradoras competidoras vendiendo dentro de Yape ni si hay exclusividad; solo no las encontré. Tampoco encontré seguros de otras aseguradoras en Plin o en billeteras de otros bancos.
3. **El producto se diseña alrededor de un riesgo cotidiano.** Celular robado, fraude en la propia cuenta, una atención médica por teléfono. Son riesgos que la persona ve ese mismo día, no seguros de vida o salud completos. Es un cambio de producto, no solo de canal.
4. **El cobro se mueve a la billetera.** Pacífico ya cobra pólizas por Yape, y la Ley 32413 (sueldo en billetera) acerca el cobro al día de pago (F-964). Es una hipótesis de cobranza que no probé con datos de morosidad.
5. **La regulación pesa más sobre quien vende en la app.** La SBS amplió el deber de asesorar a toda la vida del contrato, y la venta a distancia debe informar del producto y del derecho de arrepentimiento (F-1110). Con el BaaS, el banco o caja responde ante el cliente aunque la plataforma lo venda (F-1111).

**Lo que probablemente no cambia (hipótesis).** Que la persona confíe en que le pagarán el siniestro, y que renueve. No encontré ningún estudio independiente de renovación o siniestralidad de seguros embebidos en billeteras; solo blogs de proveedores con cifras propias. En otros países hay escala de pólizas (GCash tiene 51,4 M de pólizas con 76% de clases D y E, cifra de la empresa; F-896) pero tampoco publican renovación ni siniestralidad.

**Cómo leer la cifra "más de un millón de clientes".** Es un conteo acumulado, sin período, producto ni pago. Un cliente con una póliza de S/ 4,90 que no se renueva cuenta igual. Eso no dice cuántas pólizas siguen vigentes, cuántos eran nuevos en seguros ni cuánta prima se cobra.

**Qué mediría para saber si cambia el juego** (con datos propios, no públicos):

| Pregunta | Indicador | Por qué |
|---|---|---|
| ¿Llega a gente nueva? | Parte de compradores sin seguro previo | Distingue inclusión de canibalización |
| ¿Se queda? | Persistencia al mes 13 frente al mismo producto por otro canal | La venta es un momento; la renovación es la relación |
| ¿Cumple la promesa? | Siniestros reclamados, pagados y tiempo de pago | La confianza se juega en el pago |
| ¿Es por el canal o por quien compra? | Prueba con grupo que no ve la oferta (aleatorio) | Sin eso, compra y persistencia se confunden con quién elige comprar |
| ¿Cuánto cuesta? | Costo de adquisición, comisión a la plataforma y gasto de servicio por póliza | El precio de S/ 4,90 solo funciona con costos mínimos |

**Límites de esta sección.** Todo se leyó por páginas comerciales, publirreportajes y resúmenes de resultados. No se corrió la pista social (qué dicen los usuarios de Yape sobre estos seguros). No se verificó exclusividad ni cuántas pólizas siguen vigentes.

## Conexiones

- [[digitalizacion-seguros-mercados-emergentes|Digitalización en seguros en mercados emergentes]] — de dónde viene este radar
  (§9.4 retirado); aquí están las tres definiciones basales y el mapa de lo digitalizado.
- [[economia-conductual-seguros-literatura|Economía conductual de los seguros]] — la base conductual de P1 y P3
  (confianza, elección, asesoría).
- [[seguros-comportamiento-mundo-peru|Seguros: comportamiento y mercado, Mundo vs. Perú]] — contexto de confianza y penetración.
- [[conducta-humano-ia|Conducta humano-IA]] — confianza, sobre-confianza y delegación (P3, P7).
- [[fenomeno-el-nino-impacto-personas|Fenómeno El Niño: impacto en las personas]] — clima y seguro paramétrico (P4, P5).
- [[mecanismos-seguros-salud|Mecanismos de seguros de salud]] — solidaridad y personalización en salud (P2).
- [[futuro-asesores-seguros-venta-digital|Futuro de los asesores de seguros y venta digital]] — qué queda humano (P7).
- [[venta-vida-digital-hibrida-latam|Venta de vida digital vs. híbrida en LATAM]] — comparación con LATAM (P6).
- [[modelo-personas-sinteticas|Modelo de personas sintéticas `lapuerta`]] — segmentos para simular escenarios.
- [[hipotesis-digitalizacion-seguros-evidencia-publica|Hipótesis de digitalización en seguros: evidencia pública y dato interno]] — cómo medir hoy la recurrencia que algunas de estas experiencias futuras darían por supuesta.
