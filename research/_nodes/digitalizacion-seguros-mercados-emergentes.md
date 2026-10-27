# Digitalización en seguros en mercados emergentes: qué se digitaliza, para qué, qué conducta cambia y qué definir para Perú

> Documento de investigación. Fuente persistente y versionada en el repositorio.
> Fecha de elaboración: 2026-10-26 · Última actualización: 2026-10-27 · Versión: v1.6 (v1.6 suma §13: para qué digitalizan y qué buscan; v1.5 sumó §12: clasificación de fuentes aportadas por el usuario; v1.4 sumó §11: casos de México, Colombia, Chile y Argentina; v1.3 sumó §10: qué más explica la digitalización además de las cuatro variables de §2; v1.1 sumó §8: estado de la digitalización por etapa, insurtech y láminas de banca de México; v1.2 sumó §9: defaults, pago y automatización; el resto de la literatura conductual de seguros vive en `economia-conductual-seguros-literatura`)
> Origen: `/trinidad` — investigación de 360° (empírica + social + negocio)
> Pregunta original: cómo y para qué se digitalizan las aseguradoras, qué intervenciones conductuales se
> aplicaron y sobre quiénes, dónde hay oportunidades de diseño en mercados emergentes, qué se aprende de otras
> industrias y con qué criterios definir al cliente digitalmente sano, la fidelidad y el cliente de alto valor
> en una aseguradora peruana.
> Fuentes registradas en `research/fuentes/codice.md` (F-847 a F-968; §10: F-1030 a F-1043; §11: F-1044 a F-1060; §12: F-1061 a F-1072; §13: F-1085 a F-1098). Reutiliza fuentes previas del ledger
> (F-372 a F-377, F-509, F-362 a F-366, F-442, F-807) citadas por ID.

---

## 0. Cómo leer este documento (límites del método)

- **Todo se leyó por resúmenes de búsqueda.** Ningún artículo se abrió completo. Los tamaños de efecto salen
  de resúmenes (abstracts) y fichas. Los hosts de McKinsey, PNUD, Swiss Re, GSMA y Repairer Driven News
  devolvieron bloqueo de red (403 o fallo de resolución); no se rodearon.
- **Pista social débil.** La herramienta de búsqueda no devolvió hilos de X, Reddit ni TikTok sobre seguros en
  LATAM. Lo que aquí figura como "percepción" son encuestas de consumidores, prensa y sanciones. No se
  presenta como validación social.
- **Sesgo de supervivencia.** Casi todos los casos de escala (GCash, Grab, Pula, Tigo, ZhongAn, PB Fintech,
  Azos) son empresas que siguen operando y que publican sus propias cifras. Los cierres (Betterfly) y las
  ventas de unidades (Bestow) aparecen poco en la prensa.
- **Marcas de evidencia.** Cada hallazgo indica: nivel (RCT, cuasi-experimento, observacional, caso de
  negocio, reporte de industria, opinión), quién lo reporta (propia empresa = PR, o tercero) y el ID del ledger.

---

## 1. Resumen ejecutivo

1. **Lo que cambia la conducta con causalidad demostrada es el diseño del contrato, no el canal.** Cobrar la
   prima al cosechar, y no por adelantado, sube la adopción de **5% a 72%**; poder pagar **un mes después** suma 21
   puntos (Casaburi y Willis, 2018; F-847). En Kenia, India, Ghana y China la barrera es la desconfianza y la
   liquidez; el precio explica menos (F-848 a F-852). Haber visto pagar un siniestro, propio o ajeno, sube la
   demanda (F-851, F-852).
2. **No existe un experimento independiente que evalúe app, WhatsApp o chatbot de seguros.** Todo lo "digital de
   canal" que se halló es PR, caso de negocio o encuesta de proveedor (F-865, F-867, F-889, F-893, F-894).
3. **Hipótesis de edad: matizada.** La edad mueve la preferencia por el contacto humano (59% de baby boomers lo
   prefiere, F-865), pero la evidencia que la contradice es del mismo tamaño: la edad no predijo la compra
   online al controlar ingreso, educación y habilidad (F-860), y entre los jóvenes también hay abandono (26% de
   la Gen Z evitó reclamar por frustración digital, F-865). Pesan más el momento (siniestro), la confianza y la
   liquidez. Confianza media-baja: no hay estudio peruano.
4. **En Perú lo digital ya ganó donde el producto es obligatorio y verificable** (SOAT ~90% digital, según el
   gremio, F-884). Donde es voluntario no hay dato público de conversión. Las sanciones se concentran en el
   siniestro (plazos, condiciones, reglas por edad; F-875), y desde setiembre de 2025 el desgravamen es
   opcional salvo hipotecario (F-877): desaparece el "default" que alimentaba el canal bancario.
5. **Qué hacer primero:** (a) piloto de cobro alineado al ingreso por billetera, con grupo de control; (b)
   convertir el primer siniestro en el momento de verdad, con plazo visible; (c) definir al cliente digital
   sano por **resolución autónoma del evento**, con un indicador del "silencio" (quien abandona y no reclama);
   (d) decidir a quién empujar a digital con **valor esperado de migración probado con control**, nunca por
   edad (Indecopi ya multó a Mapfre con 50 UIT por excluir a mayores de 85, F-875).
6. **Lo que no se sabe:** no hay benchmark público de contención, resolución al primer contacto ni
   procesamiento directo (F-907); no hay evidencia latinoamericana de que digitalizar reduzca la caducidad
   (la fuga menor de Tigo es autorreportada, F-898); no hay encuesta sobre a quién culpa el cliente de un
   siniestro por bancaseguros.

### Las tres pistas por separado

- **🔬 Empírica/teórica (sólida en demanda y confianza, vacía en canal digital).** RCT y cuasi-experimentos
  convergen en liquidez, confianza y pago visible. Las revisiones sobre edad confirman un vacío de
  investigación (F-859).
- **📱 Percepción/social (débil).** Encuestas de proveedores en EE.UU. y un caso viral antiguo (Lemonade,
  2021). Sin redes sociales latinoamericanas recuperables. Instalación social: 🧊 en LATAM; 🌡️ solo para
  "IA en el momento del siniestro" (Lemonade).
- **💼 Negocio (rica pero autorreportada).** Escala de pólizas (GCash, Grab), crecimiento (PB Fintech,
  ZhongAn) y rentabilidad aún no alcanzada en el caso insignia (Lemonade, pérdida neta de US$43 M en el 2T
  2026; F-509). Sin retención ni siniestralidad publicadas para los embebidos.
- **⚖️ Convergencia:** las tres señalan la confianza y el momento del siniestro como el punto de decisión, y el
  modelo híbrido como patrón estable (Bain, Swiss Re, McKinsey; F-864, F-885, F-887). **Divergencia:**
  el negocio celebra velocidad de IA en el siniestro (Rímac "48 horas a 1 minuto", F-889; Lemonade 5% de gasto
  de reclamos, F-904) mientras la evidencia empírica y regulatoria ubica en el siniestro la mayor fricción y
  los castigos (F-875, F-876). No se resuelve: ninguna fuente mide si la velocidad mejora la confianza.

---

## 2. Veredicto de la hipótesis de edad: MATIZADA

**Hipótesis evaluada:** la edad (jóvenes digitalizables, mayores no) es el criterio principal para decidir
quién se digitaliza y por qué canal.

**Veredicto:** matizada, con inclinación a no sostenida como criterio principal. **Confianza media-baja:**
las fuentes sobre edad son de EE.UU. o genéricas de compra online, no de seguros en Perú.

| | Evidencia | Tipo / calidad |
|---|---|---|
| **A favor** | 59% de baby boomers y 39% de la generación X prefiere hablar con una persona antes que un proceso totalmente digital; solo 7% y 14% quiere autoservicio total (F-865) | Encuesta de proveedor, EE.UU.; muestra no verificada |
| **A favor** | En adultos mayores de Lima, la **facilidad percibida** es lo que más se asocia con adoptar Yape; evitan tareas que los hagan sentir vulnerables (F-862) | Tesis; método no visto |
| **A favor** | El node previo reporta que la Gen Z es más abierta a compartir datos (38% más positiva que los boomers) y confía más en la IA (87% frente a 75%) (`seguros-comportamiento-mundo-peru` §1.3) | Encuesta global de consultora |
| **En contra** | Con ingreso, educación, innovación y habilidad en internet en el modelo, **edad y género no influyeron** en la intención de compra online de seniores (F-860, n=154, no es seguros) | Tesis |
| **En contra** | Lo que predice comprar online es la **edad subjetiva** (cuán joven se siente) y la percepción de riesgo, no los años (F-861, n=244, 50+) | Estudio transversal, no es seguros |
| **En contra** | Los jóvenes también abandonan lo digital: 26% de la Gen Z y 21% de los millennials evitó reclamar por la frustración del proceso; 28% de la Gen Z cambió de aseguradora (F-865). Los millennials reportan 85% de satisfacción con lo digital, pero se interpreta como expectativa más alta (F-866) | Encuestas de proveedores, EE.UU. |
| **En contra** | La revisión de 44 estudios sobre envejecimiento y compra de seguros concluye que **los efectos matizados de la edad están poco estudiados** (F-859) | Revisión de alcance |
| **Confusor en Perú** | La informalidad laboral llega a **84,8% entre 14 y 24 años** y a 94,8% en zona rural (F-879): en Perú la edad se mezcla con ingreso irregular y falta de cuenta. Quien parece "joven digital" puede ser informal sin historial | Estadística oficial vía prensa |

**Variables que explican mejor (hipótesis, no hallazgos):** el momento (comprar frente a siniestrarse: Swiss
Re, F-885), la confianza en la contraparte (F-849, F-850), la liquidez e irregularidad del ingreso (F-847), la
complejidad del producto y la habilidad percibida (F-861, F-862). **§10 amplía esta lista** con
habilitadores y entorno.

---

## 3. Casos conductuales y estratégicos

Leyenda: **Nivel** = RCT · cuasi-experimento · observacional · caso de negocio · reporte de industria ·
opinión. **Quién reporta** = tercero o PR (propia empresa).

### 3.1 Seguros y microseguros

*Para México, Colombia, Chile y Argentina, ver §11.*

| Caso | País / industria | Qué digitalizó | Población objetivo | Intervención / estrategia | Mecanismo conductual | Resultado y duración | Nivel · fuente |
|---|---|---|---|---|---|---|---|
| Casaburi y Willis | Kenia · seguro agrícola | Cobranza (no es digital; es diseño del contrato) | ~80.000 cañeros de un comprador | Prima descontada al cosechar; opción de pagar un mes después | Liquidez, sesgo al presente, riesgo de contraparte | **72% vs. 5%** de adopción; **+21 pp** pagando un mes después; mayor efecto en los más pobres. Duración: una campaña (no se verificó seguimiento) | RCT · tercero (AER) · F-847 |
| Cole et al. | India · seguro de lluvia | Venta | Hogares rurales | Ofertas aleatorias de precio y condiciones | Confianza, liquidez, saliencia | **5-10%** de adopción; sensible a precio pero no basta bajarlo | RCT · tercero · F-848 |
| Dercon, Gunning, Zeitlin | Kenia · salud | Venta | Cafeteros/té | Variación aleatoria de prima + medición de confianza en lab | Confianza limitada | Quien confía poco responde más a rebajas; pérdida por baja confianza **>31% de la prima** | RCT · tercero · F-849 |
| Cai et al. | China · seguro de cerdas | Venta | Familias criadoras | Incentivos al funcionario que inscribe | Confianza institucional | El seguro sube la producción y el efecto **persiste**; la desconfianza frena la inscripción pese al subsidio | RCT · tercero (REStat) · F-850 |
| Karlan et al. | Ghana · seguro índice | Venta y pago | Agricultores | Subsidios y pagos aleatorios | Prueba social y pago observado | Más inversión y riesgo productivo; **demanda sube con pagos propios y de la red social** | RCT · tercero (QJE) · F-851 |
| Cole, Giné, Vickery | India · seguro de lluvia | Pago | Agricultores | Pagos recibidos | Pago como señal de confianza | Los pagos **mejoran la confianza** y cambian decisiones productivas | RCT · tercero (RFS) · F-852 |
| Gaurav, Cole, Tobacman | India · seguro de lluvia | Marketing | 600 agricultores | Capacitación financiera + 6 tratamientos de marketing | Comprensión, garantía | Capacitación sube adopción pero **no es costo-efectiva**; garantía de devolución **~US$43,62 por póliza extra**; solo 1 de 6 tratamientos significativo | RCT · tercero (JMR) · F-853 |
| Tigo con BIMA | Ghana y Senegal · telecom | Venta y cobro (saldo de recarga) | Clientes prepago | Seguro gratuito atado al uso (freemium) | Regalo, inercia, costo hundido de conversión | Empresa: **55% pasa al pago**, menos fuga; ~1 M de clientes y 93% sin otro seguro (CGAP). Senegal: 13% de la base | Caso de negocio · **PR/industria**; sin evaluación independiente · F-898, F-899 |
| GCash GInsure | Filipinas · billetera | Venta embebida | Usuarios de la billetera | Micropólizas en la app | Baja fricción, precio mínimo | 14,6 M usuarios y 51,4 M pólizas (1T 2025); >20 M (4T 2025); **76% de clase D/E, 75% fuera de Manila**. Sin renovación ni siniestralidad | Caso de negocio · **PR** · F-896 |
| Grab Financial | Sudeste Asiático · plataforma | Venta embebida | Usuarios de viajes | *Ride Cover* de S$0,30 al reservar | Compra en el momento del riesgo | >100 M pólizas acumuladas (c. 2021). Sin retención ni primas | Caso de negocio · **PR** · F-897 |
| Pula | África · paramétrico | Pago automático y venta embebida | Pequeños agricultores | Cobertura incluida en insumos, crédito o programas | Cero acción del cliente; sin reclamo | Cifras propias (1,1 M agricultores en 2019; 3,4 M hogares). **Riesgo de base**: el umbral no siempre coincide con la pérdida y erosiona confianza (opinión) | Caso de negocio · **PR** + opinión · F-900 |
| ReachUHC | Ghana · seguro de salud | Renovación | 342.818 afiliados | Recordatorio por teléfono / renovación automática por dinero móvil | Olvido, procrastinación | Línea base: **~50% renueva tarde o no renueva**; razones: olvido 19,8%, falta de tiempo 17,9%, procrastinación 15,6%. **Sin resultados aún** | Protocolo de RCT · F-856 |
| Seguro Salud Yape | Perú · salud | Venta y servicio (teleconsulta) | ~17 M de usuarios Yape | S/9,90 al mes en la app | Baja fricción, precio simbólico | Meta: **30.000 afiliados en el primer año** (≈0,18% de la base). Sin cifra real | Caso de negocio · **PR/publirreportaje** · F-888 |
| SOAT digital | Perú · obligatorio | Venta | Dueños de vehículos | Emisión en línea con registro automático | Obligación + verificabilidad + precio menor | **~90% de emisiones digitales** (gremio). Sin dato 2025-2026 | Reporte de industria · gremio · F-884 |
| Rímac | Perú · vehicular | Siniestro y venta | Asegurados | Chatbot de IA; rediseño web | Velocidad percibida | Análisis de siniestro **~48 h → ~1 min**; **+43% ventas digitales**, 39% conversión de lead. Sin fecha, sin base | Caso de negocio · **PR** · F-889 |
| Mapfre Brasil | Brasil · auto y agro | Siniestro por WhatsApp | Distribuidores, luego clientes | IA por audio o texto | Canal habitual | Lanzamiento 2025-2026. **Sin resultados** | Caso de negocio · PR · F-893 |
| Lemonade | EE.UU. · todo digital | Venta, pago, siniestro | Mercado masivo | IA y app | Velocidad y transparencia | 2T 2026: 3,31 M clientes, **retención anual en dólares 85%**, gasto de reclamos 5% frente a ~9% de la industria; **pérdida neta US$43 M**; 2021: polémica por prometer lectura de "microexpresiones" | Caso de negocio · empresa cotizada + prensa · F-509, F-904, F-869 |
| ZhongAn | China · ecosistemas | Todo | Usuarios de plataformas | Seguros dentro de ecosistemas de terceros | Contexto de compra | 1S 2025: **salud +38,3%** (15,2 M asegurados); **finanzas del consumidor −10,6%**; estilo de vida digital −1,4% | Caso de negocio · empresa cotizada · F-902 |
| PB Fintech (Policybazaar) | India · marketplace | Venta y renovación | Compradores online | Plataforma de comparación | Comparación, comisiones | 4T año fiscal 2026: primas colocadas +46%, utilidad +54%; **riesgo por posible recorte de comisiones** | Caso de negocio · prensa sobre resultados · F-903 |
| Azos | Brasil · vida | Suscripción digital | Corredores | Tecnología distribuida por >9.000 corredores | Confianza del intermediario | Facturación duplicada dos años seguidos (ver `venta-vida-digital-hibrida-latam`) | Caso de negocio · F-377 |
| Betterfly | Chile y LATAM · bienestar corporativo | B2B2C | Empleados | Suscripción pagada por la empresa | — | **Cerró operaciones en 5 de 8 países (2025)**; fracaso documentado | Prensa · F-372, F-373 |

**Fracasos y señales de alerta documentados:** Betterfly (F-372); Bestow vendió su aseguradora D2C (F-366);
Lemonade sin utilidad neta a 11 años de fundada (F-509); varios medios registran desplome de valuaciones de
insurtechs (Root, Metromile), pero esa cifra no pasó por el ledger. El 99,1% del financiamiento insurtech del 2T
2026 va a empresas de IA y el de etapa temprana cae 51,8% (F-901).

### 3.2 Qué se digitaliza, para qué y con qué resultado medido

| Proceso | Canal dominante hallado | Objetivo declarado | Resultado realmente medido (y por quién) |
|---|---|---|---|
| **Venta** | App, web, comparadores, billetera/plataforma (embebido) | Inclusión y penetración | Escala de pólizas (GCash, Grab) y crecimiento de primas (PB Fintech): **PR**. Sin evidencia independiente de que amplíe cobertura en quien antes no tenía |
| **Onboarding** | Formularios en app/WhatsApp | Menor fricción | **Sin datos de abandono en seguros de LATAM.** La cifra de 60% de abandono circula en un ebook de proveedor (F-873, 🔴 E) |
| **Cobranza** | Billetera, dinero móvil, descuento al cosechar | Menor caducidad | Pago diferido: RCT (F-847). Cuotas pequeñas por dinero móvil: opinión de encuestados (F-910) |
| **Siniestro** | App, WhatsApp, chatbot, IA | Menor costo y mayor velocidad | Costo de reclamos 5% (Lemonade, PR, F-904); tiempo 48 h → 1 min (Rímac, PR, F-889). Satisfacción **mayor cuando el reclamo se gestiona digital de punta a punta**, pero solo 31-36% recibe actualizaciones por app (J.D. Power, F-868) |
| **Renovación** | Recordatorio, autopago | Persistencia | Protocolo ReachUHC sin resultados (F-856); persistencia al mes 13 de 65-70% en India solo en blog de proveedor (F-909) |
| **Servicio** | Chatbot, app | Menos llamadas | Quien usó chatbot puntúa **+132 puntos**, pero solo **11%** lo usó (F-867). Sin tasa de contención pública (F-907) |

**Objetivo declarado frente a resultado medido.** El discurso es inclusión y penetración; lo que se mide y
publica es volumen de pólizas, velocidad y costo de reclamos. La penetración peruana sigue en ~2% del PBI
(`seguros-comportamiento-mundo-peru` §3.9) y el sistema creció solo +1,1% en el 1S 2026 (F-506): no hay señal
de que la digitalización haya movido el agregado, aunque tampoco hay un estudio que lo pruebe.

**Sobre la premisa de "no buscar un heavy user".** Plausible, pero **sin respaldo de tercero**: solo blogs de
proveedores dicen que se interactúa ~2 veces al año (F-914), y esos mismos proveedores sostienen lo contrario
(que más interacción mejora persistencia). Tensión abierta, no resuelta.

---

## 4. Matriz intervención × segmento

Símbolos: ✅ efecto causal medido en un segmento análogo · 🟡 señal (PR, observacional o encuesta) · ❌ costoso
o sin efecto · ⬜ sin evidencia hallada. **Casi todas las celdas de segmentos urbanos y digitales están
vacías**: la evidencia causal es agrícola y rural, y se transfiere por analogía.

| Intervención | Rural / agro informal | Informal urbano con billetera | Formal bancarizado y digital | Mayor / poca habilidad digital | Cliente de banco (bancaseguros) | En siniestro |
|---|---|---|---|---|---|---|
| **Cobro alineado al ingreso / pago diferido** | ✅ F-847 (contrato agrícola) | ⬜ hipótesis; encuestados apoyan cuotas pequeñas (F-910) | ⬜ | ⬜ | ⬜ | — |
| **Aval de una figura de confianza** (corredor, institución local) | 🟡 la confianza es la barrera medida (F-849, F-850); el efecto del aval no se verificó | ⬜ | ⬜ | 🟡 | 🟡 la confianza en el corredor sube (node previo §3.3) | — |
| **Pagar un siniestro y que se vea** | ✅ F-851, F-852 | ⬜ | ⬜ | ⬜ | ⬜ | 🟡 el servicio y el siniestro son los motores de retención (F-868) |
| **Recordatorio y renovación automática** | ⬜ | 🟡 protocolo sin resultados (F-856) | ⬜ | ⬜ | 🟡 el default existía, hoy limitado (F-877) | — |
| **Seguro embebido en billetera o plataforma** | 🟡 Pula (F-900) | 🟡 GCash 76% D/E (PR, F-896) | 🟡 Nubank, Mercado Libre (sin cifras, F-911) | ⬜ | — | — |
| **Autoservicio / chatbot de siniestro** | ⬜ | ⬜ | 🟡 F-867, F-904 | ❌ 59% boomers prefiere humano (F-865) | — | 🟡 mixto: mayor satisfacción en digital pero 26-28% evita reclamar por frustración (F-865, F-868) |
| **WhatsApp conversacional** | ⬜ | 🟡 hábito: 97-98% en banca de Brasil y México (F-872); casos de proveedor (F-894) | 🟡 | ⬜ | — | 🟡 sin resultados (F-893) |
| **Capacitación financiera** | ✅ sube adopción, **no costo-efectiva** (F-853) | ⬜ | ⬜ | ⬜ | ⬜ | — |
| **Garantía de devolución** | ❌ US$43,62 por póliza extra (F-853) | ⬜ | ⬜ | ⬜ | ⬜ | — |
| **Freemium atado a telecom** | 🟡 Tigo (PR, F-898) | 🟡 | ⬜ | ⬜ | — | — |
| **Híbrido asistido (humano + herramienta digital)** | 🟡 Pula, Azos (F-377, F-900) | ⬜ | 🟡 clientes multicanal dan el mayor NPS (F-864) | 🟡 F-865 | 🟡 corredores 60-65% (F-887, ambiguo) | 🟡 F-885 |

---

## 5. Mapa de oportunidades priorizado (Perú)

Impacto esperado = cuánto movería adopción, retención o confianza según la evidencia; Facilidad = qué tan rápido
se puede probar en una aseguradora peruana. **La prioridad combina ambos; no es una predicción.**

| Prioridad | Oportunidad | Impacto | Facilidad | Evidencia que la sostiene | Transferibilidad |
|---|---|---|---|---|---|
| 1 | **O1. Cobro alineado al flujo de ingreso por billetera** (cuotas por cobro de Yape/Plin; primer cobro diferido 30 días) | Alto | Media (reglas de cobertura durante el diferimiento; riesgo de crédito) | RCT en agro (F-847) | Con adaptación: Perú no tiene un comprador único que descuente; el análogo urbano es hipótesis |
| 2 | **O2. El primer siniestro como producto** (plazo comprometido y visible, seguimiento proactivo) | Alto | Media | Pagos que suben confianza y demanda (F-851, F-852); motor de retención (F-868); castigos regulatorios (F-875, F-876) | Transferible |
| 3 | **O3. Renovación consciente con recordatorio y autopago con consentimiento** | Medio-alto | Alta | Línea base ~50% tarde o nunca (F-856); resultados pendientes; riesgo de consumo si el default no es transparente | Con adaptación: probar con control |
| 4 | **O4. Medir antes de forzar** (línea base de resolución autónoma, abandono y "silencio") | Medio (habilita todo) | Alta | Sin benchmarks públicos (F-907) | Interno |
| 5 | **O5. Híbrido asistido** (corredor, asesor o familiar con herramienta digital) para vida, salud y mayores | Alto en vida/salud | Media-alta (ya hay trabajo en Back to Basics) | F-864, F-885, F-377 | Transferible |
| 6 | **O6. Responsable único visible en bancaseguros** y consentimiento explícito tras el fin del default de desgravamen | Medio | Media | Reguladores y jueces cargan al banco (F-874); Res. 00890-2025 (F-877). Falta encuesta de percepción propia | Con adaptación |
| 7 | **O7. Micropólizas por evento en billeteras y plataformas** (viaje, accidente, entrega) con medición de renovación | Medio | Media-alta (Pacífico ya vende viaje desde S/3, F-888) | Escala de PR (F-896, F-897) sin retención | Con adaptación: exigir cohortes |
| 8 | **O8. WhatsApp primero para reportar siniestro, con humano en el circuito** | Medio | Alta | Casos sin resultados (F-893, F-894) | Con adaptación: piloto medido |
| 9 | **O9. Cobertura paramétrica anticipatoria (Niño Costero)** | Potencialmente alto | Baja (regulación y riesgo de base, F-900) | Ver `fenomeno-el-nino-impacto-personas` | Con adaptación |
| 10 | **O10. Protección para trabajadores de plataformas e independientes** | Medio-alto | Baja-media | Vacío de cobertura 2019 (F-913); sin oferta vigente hallada | Por validar |

**Qué no hacer con la evidencia actual:** forzar digital por edad (riesgo Indecopi, F-875); usar capacitación
financiera o garantía de devolución como palanca principal (F-853); gamificar sin evidencia en seguros (solo un
experimento fuerte en todo el rubro, F-807, de un centro comercial asiático; ver `lealtad-gamificacion-recompensas-retail`).

### 5b. Criterios para las tres definiciones basales (Perú)

**Advertencia:** no hay umbrales públicos que copiar. Los valores objetivo salen de la línea base interna y de
pruebas con grupo de control. Las fórmulas y la selección de métricas son una construcción de este documento
(inferencia), apoyada en la evidencia citada.

**1. Cliente digitalmente sano.** Definición propuesta: *resuelve por sí mismo, sin fricción y sin perder
confianza, el evento que lo trajo, y vuelve al canal digital en el siguiente evento.*

| Capa | Métricas candidatas | Respaldo / límite |
|---|---|---|
| Acceso (necesaria, no suficiente) | Activó el canal en los primeros 30-90 días; contacto verificado (WhatsApp o correo) | "Un inicio de sesión solo prueba que entró, no que resolvió" (F-907, proveedores) |
| Resolución | Tasa de resolución autónoma **por tipo de evento** (cobro, constancia, aviso de siniestro, seguimiento); completitud sin recontacto a 7 y 30 días; tiempo a resolución; esfuerzo del cliente | Sin benchmark público de contención ni resolución al primer contacto (F-907). Solo "pocos aseguradores superan la mediana en adopción y contención a la vez" (J.D. Power; medianas no publicadas) |
| Confianza y retorno | Reuso digital en el siguiente evento; **llamadas tras uso digital** (desviación real = no vuelve a llamar) | La cifra de 40% frente a 92% de retorno es de segunda mano y de proveedor (F-914) |
| Silencio (guardarraíl) | Reclamos no presentados tras abandono digital; caducidad posterior a un trámite abandonado | 26-28% evitó reclamar por frustración digital (F-865, EE.UU.) |
| Equidad | Todo desglosado por rural/urbano, con/sin cuenta, edad, tipo de evento; salida a humano siempre disponible | Informalidad 70,7%, rural 94,8%; internet en hogar rural 23,4% (F-878, F-879) |

**No usar:** cantidad de descargas, usuarios activos mensuales ni "usuario intensivo" como éxito de un producto
de pocos toques. Un cliente que casi no entra y resuelve todo sin llamar es el caso sano.

**2. Fidelidad.** Principio: separar **retención por inercia** (default, banco, cobro automático) de
**retención por elección**. En un mercado de baja confianza, la renovación sola no la distingue.

| Señal de fidelidad | Por qué importa | Respaldo / límite |
|---|---|---|
| Renovación **después de un siniestro** (pagado, rechazado o sin siniestro), comparada | Es el momento que construye o destruye la confianza | Pago recibido sube la renovación y la confianza (F-851, F-852, F-858); servicio y siniestro como motor (F-868) |
| Recompra voluntaria cuando cambiar de aseguradora no cuesta nada (p. ej. SOAT en línea) | Aísla la elección de la inercia | Hipótesis de diseño; sin fuente |
| Reclamar en lugar de callar | La fidelidad sana incluye confianza para usar el seguro | F-865 |
| Compra adicional **sin empuje comercial** | El cross-sell empujado mide al vendedor | Hipótesis |
| Recomendación (NPS) | Los promotores valen ~7 veces un detractor en EE.UU. (Bain, c. 2014) | F-864; antiguo, sin dato peruano |
| Persistencia al mes 13 y 25 | Estándar actuarial | Sin benchmark peruano; el 65-70% de India es de blog de proveedor (F-909) |

**¿Digitalizar reduce la caducidad?** No hay evidencia latinoamericana. Lo hallado: caída de fuga en Tigo
(autorreportada, F-898), retención anual de 85% en Lemonade (sin contrafactual, F-904), olvido y
procrastinación como causas de no renovar (F-856), baja comprensión como causa de caducidad (F-857, F-858).
**La hipótesis de que la permanencia depende de la longevidad del producto** (vida de 15 años frente a SOAT de
1 año) **no se probó en ninguna fuente**. Se puede probar con cohortes por producto y con un grupo de control sin
recordatorios.

**3. Cliente de alto valor.** Valor ≠ prima alta. En Perú, Mapfre tuvo ratio combinado de 102,4% en el 1T 2026 y
la utilidad de Rímac cayó 40% en el 2T (`seguros-comportamiento-mundo-peru` §3.9): un cliente que paga mucho en
un ramo con pérdida técnica no es de alto valor.

- **Valor del cliente:** `LTV_i = Σ_t [ prima_it × (1 − siniestralidad esperada_it − gastos_it) × P(permanece_t) ] − CAC_i − costo de servir_i`
- **Valor esperado de migrar a digital:** `VEM_i = (costo de servir humano − costo de servir digital) × permanencia esperada_i − costo del incentivo − P(pérdida inducida por forzar) × LTV_i`
- **Regla:** empujar donde `VEM_i > 0` **y** el evento esperado es rutinario; mantener humano donde el evento
  esperado es grave, emocional o complejo (vida, salud, siniestro severo; Bain, Swiss Re, F-864, F-885).
- **Cómo estimar la parte causal:** prueba con grupo de control que separe a los *persuadibles* (migran por el
  incentivo), los *migrarían igual* y los *se molestan* (modelo de uplift). Sin esto, el incentivo se paga a quien
  igual migraba.
- **Variables:** ramo y rentabilidad técnica, riesgo (siniestralidad esperada), severidad esperada del evento,
  permanencia esperada por producto, CAC y costo de servir por canal, elasticidad al canal, potencial de
  compra adicional, datos de contacto disponibles.
- **Restricciones:** Indecopi sancionó reglas por edad y la responsabilidad solidaria con el ajustador (F-875);
  la SBS endurece plazos y sustento de rechazos (F-484 en el node previo).

### 5c. Mapa de la oferta local y techo de oportunidad

**Barrido de la oferta (por ficha y prensa; no es auditoría de experiencia).**

| Actor | Lo hallado | Evidencia | Falta |
|---|---|---|---|
| **Pacífico** | App *Mi Espacio Pacífico* con seguimiento de siniestro; Seguro Salud Yape (teleconsulta, S/9,90); pago de seguros por Yape; viaje desde S/3 (abr-2026); sanción solidaria con ajustador | F-888, F-890, F-875 | Afiliados reales, conversión, vehicular y vida digital |
| **Rímac** | Chatbot de siniestros vehiculares (48 h → 1 min); +43% de ventas digitales vehicular; reclamos 2023 en SOAT y vehicular | F-889, F-876 | Funciones de la app; porcentaje del total; fecha |
| **Mapfre Perú** | Módulos en tiendas EFE; asistente de IA para asesores de Cajas Municipales; descuentos online | F-891 | App propia verificable; la hallada es de Paraguay |
| **La Positiva** | App: siniestros leves y no leves, pedir asesor de servicio, seguir al ajustador, tarjetas electrónicas, pago de recibos | F-890 | Ventas digitales |
| **Interseguro / Interbank** | Canal bancario +18,9% (2025); IA generativa propia; venta directa masiva incluido SOAT; Plin +45% | F-892 | Seguros vendidos por la app o Plin |
| **Bancos (BBVA, Scotiabank, BCP)** | Solo la norma: desgravamen opcional y endoso sin costo | F-877 | Funciones digitales de seguros |

**Por ramo.** *SOAT:* ~90% digital (F-884). *Salud:* Yape-Pacífico (F-888). *Vehicular:* Rímac y La Positiva
(F-889, F-890). *Vida, riesgos generales y empresas:* no se halló evidencia digital peruana en esta ronda; ver
`proyecto-back-to-basics-ffvv-vida`. *Microseguros:* el diagnóstico del PNUD de marzo de 2026 existe, pero no
se pudo abrir (F-882); línea base antigua: 0,58% del mercado en 2016 (F-883).

**Techo real: no es un número.** Son tres filtros.

| Filtro | Dato | Fuente |
|---|---|---|
| **Acceso** | 59% de adultos con cuenta; 42% con dinero móvil; telefonía móvil en 95,7% de hogares; internet en hogar 60,1% (rural 23,4%); 89,2% de usuarios se conecta por celular | F-878, F-880 |
| **Capacidad de pago e ingreso** | Empleo informal 70,7% (rural 94,8%; 14-24 años 84,8%) | F-879 |
| **Confianza** | Confianza plena en aseguradoras ~23-25%, ~48% desconfía (node previo); confianza institucional 45%, empresas 57% (F-881) | F-881 |

El techo digital depende además de la cartera propia. **Hipótesis a verificar con datos internos** (no
probadas): (1) proporción de la cartera con WhatsApp o correo verificado; (2) pólizas cuyo vínculo con el
cliente lo tiene un banco o corredor; (3) grupos donde asegurado y pagador no coinciden; (4) clientes sin cuenta
o en zona rural; (5) SOAT comprado sin identificar al asegurado; (6) mayores; (7) siniestrados con severidad
alta. Cada una reduce lo "gestionable" por canal digital y se mide con la base propia.

**Bancaseguros: ¿a quién culpa el cliente?** No se halló encuesta que lo mida. Lo que sí hay es normativo:
reguladores y jueces hacen responsable al banco cuando falla su rol (F-874). Una encuesta de McKinsey citada
por la búsqueda (25.000 entrevistados, 7 países) indicaría mayor confianza en el banco como marca para líneas
personales; no se abrió. **Contradicción a vigilar:** el 60-65% de corredores y agentes que F-375 usa como dato
regional podría ser el dato de México (F-887).

---

### 5d. Señales: hacia dónde va el sector (nuevos territorios)

| Señal | Qué se sabe | Madurez de la evidencia |
|---|---|---|
| **IA absorbe el capital** | 99,1% del financiamiento insurtech del 2T 2026 (US$2.440 M); etapa temprana −51,8%; la mayoría de despliegues es IA **asistiva**, no autónoma (F-901) | Reporte de industria |
| **Nuevos riesgos** | Responsabilidad por IA (HSB, Corgi), ciber en pymes (solo 5-20% con póliza), exclusiones ISO por IA (F-912) | Prensa; datos escasos de siniestralidad |
| **Embebido y ecosistemas** | GCash, Grab, Nubank, Mercado Libre (F-896, F-897, F-911); ZhongAn: salud crece 38% mientras finanzas del consumidor cae 10,6% (F-902) | PR; dependencia del ecosistema |
| **Salud como puerta** | ZhongAn salud; Yape teleconsulta (F-902, F-888) | PR |
| **Paramétrico** | Pula; riesgo de base (F-900) | PR y opinión |
| **Infraestructura pública digital** | Bima Sugam en India, con fechas contradictorias (F-905) | Prensa |
| **Digitalización ≠ compra digital** | Índice de Swiss Re sube en >80% de países, pero la compra de punta a punta la frenan confianza, asesoría y complejidad (F-885) | Reporte de reaseguradora |
| **Consolidación** | 45 fusiones y adquisiciones de corredores en Brasil (2021-2023, F-887) | Consultora |

---


### 5e. Cross-industry y transferibilidad

| Hallazgo | Industria | Condiciones que lo hicieron funcionar | ¿Existen en Perú o LATAM? | Qué adaptar | Transferibilidad |
|---|---|---|---|---|---|
| M-Shwari: 34% toma el préstamo; −6,3 pp de recorte de gasto ante shocks; no sube ahorro ni activos (F-854, cuasi-experimento) | Fintech sobre dinero móvil | Dinero móvil masivo (M-Pesa), scoring sin historial | Parcial: 42% con dinero móvil, 5% pidió crédito digital (F-880) | Interoperabilidad Yape/Plin; protección al consumidor | **Con adaptación** |
| SMS: adherencia OR 1,49 en ingreso bajo y medio; en África mejoran citas (OR 2,03) pero no adherencia (F-855) | Salud | Acciones puntuales con costo bajo | Sí (celular casi universal) | Usar para **acciones puntuales** (renovar, subir un documento), no para conductas sostenidas | **Con adaptación** |
| Asesoría por voz agrícola: +US$100/año, +8,6% y +28% de rendimiento; <US$10 por agricultor; ensayo de seguimiento en Kenia sin efecto (F-863, PR de la organización) | Agtech | Línea de voz, contenido local | Parcial: rural con internet 23,4% (F-878) | Voz o WhatsApp para asesoría de seguro agrícola; probar costo-efectividad | **Con adaptación** (evidencia mixta) |
| Freemium atado a recarga: 55% pasa a pago; menos fuga (F-898, PR) | Telecom | Operador dueño de la relación y del cobro | No verificado en Perú | Alianza con telecom; medir renovación real | **Con adaptación** |
| Pago por uso con bloqueo de dispositivo: repago ~mediados de 90% (F-908, PR) | Energía/PAYG | Se puede apagar el activo si no se paga | No aplica a un seguro | Suspender cobertura por atraso chico choca con protección al consumidor y daña confianza | **No transferible** (sin evidencia causal y con riesgo) |
| Gamificación: un solo experimento fuerte; efecto se mantuvo tras retirar la gamificación y el cupón se desvaneció (F-807) | Retail | Centro comercial asiático | Sin evidencia causal en LATAM (node `lealtad-gamificacion-recompensas-retail`) | Probar solo en seguros con control | **Con adaptación** (muy baja certeza) |
| Seguro embebido en súper-app (GCash, Grab) (F-896, F-897, PR) | Plataformas | Base de decenas de millones de usuarios activos | Sí: Yape ~17 M (F-888) | Medir renovación; precio de entrada bajo | **Con adaptación** |

**Industrias análogas no cubiertas:** educación, servicios públicos, microfinanzas peruanas y retail de la
región: pendiente.

---


---

## 6. Lagunas de información

1. **Ningún RCT independiente de canal digital en seguros** (app, WhatsApp, chatbot, embebido): todo es PR.
2. **Tasa de abandono de onboarding de seguros en LATAM:** no existe cifra verificable (F-873 es de proveedor).
3. **Digitalización → caducidad en LATAM:** no se halló; lo existente es autorreportado.
4. **Percepción de responsabilidad en bancaseguros** (banco o aseguradora): sin encuesta.
5. **Benchmarks de contención, resolución al primer contacto y procesamiento directo:** no públicos.
6. **Persistencia en Perú** (mes 13): sin dato; la cifra de India es de blog de proveedor.
7. **Resultados reales de embebidos** (retención, siniestralidad, primas): ninguno publica, incluido Yape-Pacífico.
8. **Funciones de las apps de Rímac y Mapfre Perú:** no halladas; falta una **auditoría de experiencia**
   (cliente incógnito) para completar la comparación.
9. **Vida e inversión "sin spam"** (pregunta del macro): sin evidencia suficiente en esta ronda; ver
   `futuro-asesores-seguros-venta-digital` y `behavioral-design-estado-disciplina`.
10. **Documentos clave no abiertos** por bloqueo: diagnóstico del PNUD sobre microseguros (F-882), informe de
    McKinsey, sigma de Swiss Re, informes de GSMA. Se leyeron por resumen.
11. **No cubiertas:** educación, servicios públicos y retail latinoamericano como industrias análogas; recordatorios
    de ahorro (Karlan et al., hallazgo no leído); India y Sudeste Asiático en profundidad; fate de BIMA/Millicom.
12. **Pista social latinoamericana:** sin hilos de X, Reddit ni TikTok.
13. **Efectos de aval por figura de confianza** en seguros: no verificados en esta ronda.

### Contradicciones entre fuentes (no resueltas)

- **Participación de corredores:** 60-65% como dato regional (F-375) frente a posible dato de México (F-887).
- **Pagos digitales en Perú:** 52% (Trivelli) frente a ~59% (BCRP) sin poder verificar (F-880).
- **Cobertura de microseguros 2022:** 294 M frente a 331 M según la nota (F-886).
- **Lemonade:** "nunca dejamos que la IA rechace reclamos" frente a documentos de IPO que decían que el bot
  manejaba algunos reclamos sin intervención humana, y a la aclaración de que los chequeos automáticos no son
  IA (F-869).
- **SMS:** efecto positivo en adherencia en meta-análisis de ingreso bajo y medio (OR 1,49) frente a ningún
  efecto en adherencia en SMS unidireccional en África (RR 1,10), aunque sí en asistencia a citas (F-855).
- **Engagement:** "no buscar heavy user" frente a la tesis de proveedores de que más interacción mejora
  persistencia (F-914).
- **Jóvenes:** 28% de la Gen Z cambió de aseguradora por mala experiencia digital (F-865) frente a 81% de
  satisfacción digital de la Gen Z en auto (F-866); miden cosas distintas.
- **Tigo/BIMA:** fuga menor y conversión de 55% (GSMA, autorreportado) frente a una lectura de "éxito en
  inclusión" (CGAP) sin medir fuga; ninguna es independiente (F-898, F-899).

---

## 7. Ledger de fuentes (F-847 a F-968)

Resumen, rigurosidad completa y URL de cada fuente: `research/fuentes/codice.md`. 🔬 empírica · 📱 percepción/social · ⚖️ regulación · 🏛️ contexto Perú · 💼 negocio. Fuentes reutilizadas del ledger previo: F-362 a F-366, F-372 a F-377, F-442, F-485, F-509, F-807 y, en §9, F-221, F-357, F-615, F-724 (node de fenómenos psicológicos y de tendencias). F-917, F-919 y F-920 vienen de las láminas del usuario y **no están verificadas**.

| ID | Pista | Autor | Año | Título | Rigor |
|---|---|---|---|---|---|
| F-847 | 🔬 | Casaburi, L. & Willis, J. | 2018 | Time versus State in Insurance: Experimental Evidence from Contract Farming in Kenya (American Economic Review) | 🟢 A |
| F-848 | 🔬 | Cole, S.; Giné, X.; Tobacman, J.; Topalova, P.; Townsend, R. & Vickery, J. | 2013 | Barriers to Household Risk Management: Evidence from India (AEJ: Applied Economics 5(1):104-135; antes FRBNY Staff Report 373) | 🟢 A |
| F-849 | 🔬 | Dercon, S.; Gunning, J. W. & Zeitlin, A. | s.f. (working paper; año no verificado) | The Demand for Insurance under Limited Trust: Evidence from a Field Experiment in Kenya (Blavatnik School of Government, Oxford) | 🔵 B |
| F-850 | 🔬 | Cai, H.; Chen, Y.; Fang, H. & Zhou, L.-A. | 2015 | The Effect of Microinsurance on Economic Activities: Evidence from a Randomized Field Experiment (Review of Economics and Statistics 97(2):287-300; antes NBER WP 15396) | 🟢 A |
| F-851 | 🔬 | Karlan, D.; Osei, R.; Osei-Akoto, I. & Udry, C. | 2014 | Agricultural Decisions after Relaxing Credit and Risk Constraints (Quarterly Journal of Economics) | 🟢 A |
| F-852 | 🔬 | Cole, S.; Giné, X. & Vickery, J. | 2017 | How Does Risk Management Influence Production Decisions? Evidence from a Field Experiment (Review of Financial Studies; DOI 10.1093/rfs/hhw080) | 🟢 A |
| F-853 | 🔬 | Gaurav, S.; Cole, S. & Tobacman, J. | 2011 | Marketing Complex Financial Products in Emerging Markets: Evidence from Rainfall Insurance in India (Journal of Marketing Research 48:S150-S162) | 🟢 A |
| F-854 | 🔬 | Bharadwaj, P.; Jack, W. & Suri, T. | 2021 (NBER WP 25604, 2019) | Fintech and Household Resilience to Shocks: Evidence from Digital Loans in Kenya (Journal of Development Economics, año según resumen de búsqueda) | 🟢 A |
| F-855 | 🔬 | Revisiones sistemáticas de SMS en salud (autoría y URL exacta no verificadas por la búsqueda) | s.f. | Network meta-analysis de 85 ECA de SMS y adherencia (n=16.271) y revisión de SMS unidireccional en África | 🔵 B |
| F-856 | 🔬 | Equipo ReachUHC (Kumasi, Ghana) | 2025 | ReachUHC: protocolo de un ECA de recordatorios por teléfono y renovación automática para aumentar la renovación del seguro de salud (Trials) | 🔵 B |
| F-857 | 🔬 | CEPR (autores no verificados) | s.f. | Documento de discusión CEPR DP12242 sobre renovación de un programa de microseguro de salud en India | 🔵 B |
| F-858 | 🔬 | Kirchner, E. & Musshoff, O. | 2022 (según resumen de búsqueda) | Entendimiento, satisfacción y renovación en seguro índice de clima en Mali (ponencia, Agricultural Economics Society) | 🟡 C |
| F-859 | 🔬 | Revisiones sobre envejecimiento e intención de compra de seguros (autoría no verificada) | 2024 y 2026 | A scoping review of the impact of ageing on individual consumers' insurance purchase intentions (PMC11414486) y The Impact of Societal Ageing on Individual Consumers' Insurance Purchase Intentions: A Review and Research Agenda (PMC12837219) | 🔵 B |
| F-860 | 🔬 | Pires, R. | s.f. | Intenção de compra online nos seniores portugueses (tesis, ISCTE-IUL) | 🟡 C |
| F-861 | 🔬 | Revista Upravlenets (autoría no verificada) | 2024 | Estudio de consumidores de 50+ años sobre edad subjetiva y compras en internet (Rusia, n=244) | 🟡 C |
| F-862 | 🔬 | Tesis PUCP (autoría no verificada) | s.f. | Uso de billeteras digitales en la generación de adultos mayores de Lima Metropolitana | 🟡 C |
| F-863 | 🔬 | Precision Agriculture for Development (PAD) | 2017 | PAD 2017 annual report | 🟡 C |
| F-864 |  | Bain & Company | c. 2014 (investigación 2013-2014; fuera de la ventana de 5 años, valor fundacional) | Customer loyalty and the 'digical' transformation in P&C and life insurance / Best's Review: Want more loyal customers? | 🟡 C |
| F-865 | 📱 | Insurity (encuesta de proveedor, vía Business Wire y Repairer Driven News) | 2025 | Digital Experience Index 2025 | 🟡 C |
| F-866 | 📱 | Insurance.com (vía Yahoo / Stacker) | 2026 | 2026 insurance satisfaction survey: How Gen Z, Millennials, Gen X and Boomers compare | 🟡 C |
| F-867 | 📱 | J.D. Power | 2026 | 2026 U.S. Insurance Digital Experience Study (11.553 evaluaciones, ene-mar 2026) | 🟡 C |
| F-868 | 📱 | J.D. Power | 2025 | U.S. Claims Digital Experience Study / Auto Claims Satisfaction Study 2025 | 🟡 C |
| F-869 | 📱 | The Register (y réplicas en medios) | 2021 | Lemonade: la aseguradora que presume su IA se mete en problemas por ella | 🟠 D |
| F-870 | 📱 | Dimension Labs (análisis de proveedor) | s.f. | Lemonade Insurance Analysis (4.567 reseñas de tiendas de apps, Trustpilot y BBB) | 🔴 E |
| F-871 | 📱 | Chubb (encuesta global 2023 y estudio regional presentado en dic-2025) | 2023-2025 | Estudio Chubb: confianza en aseguradoras digitales y compras online en América Latina | 🟡 C |
| F-872 | 📱 | Infobip / Frost & Sullivan (vía TI Inside) | 2022 | Brasil supera a EE.UU. en adopción de asistentes virtuales y chatbots en bancos y fintechs | 🟡 C |
| F-873 | 📱 | Sovos (ebook de proveedor) | 2024 | El onboarding digital seguro y sin fricciones | 🔴 E |
| F-874 | ⚖️ | Superintendencia Financiera de Colombia (vía BU Abogados) y fallos argentinos (Marval, 2003; Diario Judicial, 2026) | 2003-2026 | Sanción a un banco por la custodia de declaraciones de asegurabilidad en seguros de vida grupo ligados a créditos; responsabilidad del banco tomador de una póliza colectiva | 🟠 D |
| F-875 | ⚖️ | Indecopi (vía Andina, Peru Retail y Gestión) | 2025-2026 | Sanciones a aseguradoras: Interseguro (S/122.889,50 por plazo vencido en un reclamo SOAT; Res. 2362-2025/SPC), Mapfre (50 UIT por excluir a mayores de 85 años de seguros de viaje), Protecta, Rímac (Lambayeque) y Pacífico + RTS (responsabilidad solidaria con el ajustador; Res. 3228-2025/SPC); estadística 2019-2022 | 🟠 D |
| F-876 | 📱 | Rímac Seguros | 2023 | Reporte de Reclamos 2023 (web) | 🟡 C |
| F-877 | ⚖️ | SBS (Resolución N° 00890-2025, vía Expreso y Andina) | 2025 | El seguro de desgravamen pasa a ser opcional en tarjetas de crédito y préstamos personales; obligatorio solo en hipotecarios (vigente desde el 9-sep-2025) | 🟠 D |
| F-878 | 🏛️ | INEI (Boletín TIC, 4T 2025; cifras preliminares, vía resumen de búsqueda) | 2025 | Las tecnologías de información y comunicación en los hogares, oct-dic 2025 | 🔵 B |
| F-879 | 🏛️ | INEI / EPEN (vía Infomercado, Expreso y Gestión) | 2025-2026 | Empleo informal en el Perú | 🟡 C |
| F-880 | 🏛️ | Banco Mundial Global Findex (edición 2025, datos 2024), vía Carolina Trivelli (IEP) en Gestión y BCRP (Reporte de Estabilidad y Pagos, set-2025) | 2025 | Inclusión financiera y pagos digitales en el Perú | 🔵 B |
| F-881 | 🏛️ | Edelman Trust Barometer 2026, informe Perú | 2026 | 2026 Edelman Trust Barometer — Peru Report | 🟡 C |
| F-882 | 🏛️ | PNUD / Iniciativa de Seguros y Financiamiento de Riesgos (IRFF) | 2026 | Diagnóstico de microseguros en el Perú (24-mar-2026) | 🔵 B |
| F-883 | 🏛️ | Repositorio PUCP (documento académico; autoría no verificada) | s.f. (datos de 2016) | Microseguros en el Perú: evolución, situación actual y comparación con otros países | 🟡 C |
| F-884 | 🏛️ | APESEG (vía Andina y Revista Economía) | 2023 (cifra sin fecha clara en una de las notas) | Nueve de cada diez SOAT emitidos son digitales | 🟠 D |
| F-885 | 💼 | Swiss Re Institute | 2026 (y sigma 2023) | sigma insights 06/2026: Scaling in a digital economy — trust is key | 🔵 B |
| F-886 | 💼 | Microinsurance Network | 2025 | The Landscape of Microinsurance 2024 | 🔵 B |
| F-887 | 💼 | McKinsey & Company | 2025 | Pursuing insurance growth in Latin America (artículo web del Global Insurance Report 2025) | 🟡 C |
| F-888 | 💼 | Pacífico y Yape (publirreportajes en Correo y Trome; descubre.vc) | 2025-2026 | Lanzamiento del Seguro Salud Yape (desde S/9,90 al mes) y otras notas de Pacífico (seguros de viaje desde S/3, abr-2026; pago de seguros por Yape) | 🟠 D |
| F-889 | 💼 | Infomercado (nota sobre Rímac) y estudio de caso web | s.f. (sin fecha en el resumen) | Rímac Seguros: IA reduce a un minuto el análisis de siniestros; +43% en ventas 100% digitales tras rediseñar la web de seguro vehicular | 🟠 D |
| F-890 | 💼 | La Positiva y Pacífico (fichas de la App Store y documento de Pacífico) | 2024-2026 | Apps La Positiva Seguros y Mi Espacio Pacífico | 🟠 D |
| F-891 | 💼 | Peru Retail y publicaciones de Mapfre Perú | 2024-2026 | Mapfre Perú: módulos de venta en tiendas EFE (Decesos, Necesidad Futura, Hogar); asistente de IA "A Tu Lado Mapfre" para asesores de Cajas Municipales; campaña MAPFRE WOW | 🟠 D |
| F-892 | 💼 | Interseguro (Memoria Anual 2025) e Intercorp Financial Services (resultados 1S 2026, vía Forbes Perú y Gestión) | 2025-2026 | Interseguro: canal bancario +18,9% en 2025 y arquitecturas propias de IA generativa; IFS: Plin +45% en transacciones mensuales | 🔵 B |
| F-893 | 💼 | CQCS, Baguete y Legismap (prensa de seguros de Brasil) | 2025-2026 | Mapfre Brasil: apertura de siniestros de auto por WhatsApp con IA por audio o texto (sep-2025) y de seguro agro por chatbot (ene-2026) | 🟠 D |
| F-894 | 💼 | Blip (caso de proveedor) | 2024 | Caso de una aseguradora mexicana de autos con WhatsApp (PDF de proveedor) | 🔴 E |
| F-895 | 💼 | CIO.com (premio CIO 100) | s.f. | Zurich galardonada en finanzas y seguros: chatbot de WhatsApp que baja el trámite de siniestros | 🟠 D |
| F-896 | 💼 | GCash / Mynt (comunicados, vía Fintech News Philippines y AAP) | 2025 | GCash GInsure: seguro embebido en la billetera | 🟠 D |
| F-897 | 💼 | Vulcan Post (sobre Grab Financial) | c. 2021 | Grab Financial sold over 100 million insurance policies | 🟠 D |
| F-898 | 💼 | GSMA (Mobile for Development) | 2014 y posterior | Promising Starts in Mobile Microinsurance / A look at mobile insurance: from past to present | 🟡 C |
| F-899 | 💼 | CGAP | s.f. | Can Phones Drive Insurance Markets? Initial Results From Ghana | 🟡 C |
| F-900 | 💼 | Pula (cifras de la empresa vía MicroSave y prensa de startups) y Business Daily Africa (opinión) | 2023-2026 | Pula: seguro paramétrico agrícola y ganadero embebido en programas existentes | 🟠 D |
| F-901 | 💼 | Gallagher Re (Global InsurTech Report Q2 2026, vía Reinsurance News, Insurance Business y Risk & Insurance) | 2026 | Global InsurTech Report Q2 2026 | 🟡 C |
| F-902 | 💼 | ZhongAn Online (resultados 2025 y 1S 2025, vía HKEX, Reinsurance News y Quartr) | 2025-2026 | ZhongAn Online P&C: resultados 2025 | 🔵 B |
| F-903 | 💼 | Inc42, Quartr y HDFC Securities (sobre PB Fintech) | 2026 | PB Fintech (Policybazaar): resultados del 4T del año fiscal 2026 | 🟡 C |
| F-904 | 💼 | Coverager, MarketBeat e Insurance Journal (sobre la carta a accionistas de Lemonade 2T 2026; complementa F-509) | 2026 | Lemonade reports Q2 2026 results | 🟡 C |
| F-905 | 💼 | Outlook Money, Business Standard y otros (sobre IRDAI) | 2024-2026 | Bima Sugam: mercado digital de seguros de la India | 🟠 D |
| F-906 | 💼 | Datos Insights (antes Aite-Novarica) | 2021 y 2023 | Self-Service and Digital Payment Rates in Insurance (70 CIO en 2021; 57 en 2023) | 🟡 C |
| F-907 | 💼 | EasySend y Xemplar Insights (marcos de KPI de proveedores) | 2024-2025 | KPIs de experiencia del cliente en seguros / adopción digital | 🔴 E |
| F-908 | 💼 | Business Daily Africa, TechCabal y estudio de caso de Harvard (sobre M-KOPA) | 2024-2025 | M-KOPA: pago por uso, repago y recuperación | 🟠 D |
| F-909 | 💼 | Credgenics (blog de proveedor) | s.f. | Persistencia y caducidad en seguros de vida en India | 🔴 E |
| F-910 | 💼 | Universidad de Makerere (tesis) | s.f. | Factores que influyen en la caducidad de pólizas en Uganda | 🟠 D |
| F-911 | 💼 | FinTech Global (Mercado Libre) y Tecnoblog (Nubank) | c. 2023-2026 | Mercado Libre Seguros (5 M de clientes) y Nubank con Chubb | 🟠 D |
| F-912 | 💼 | Insurance Business, Intelligent Insurer y Swiss Re (vía prensa) | 2026 | Responsabilidad por IA y ciber para pymes como nuevo territorio | 🟡 C |
| F-913 | 💼 | Gestión y Andina (notas sobre repartidores de delivery) | 2019-2021 | Repartidores de delivery: qué derechos tienen y qué les depara el futuro | 🟠 D |
| F-914 | 💼 | 8x8, AWS, Stripe y CleverTap (blogs y casos de proveedores) | 2025-2026 | Insurance customer engagement: cómo mejorar retención, crecimiento y experiencia digital | 🔴 E |
| F-915 | 🔬 | Buell, R. W. & Norton, M. I. | 2011 | The Labor Illusion: How Operational Transparency Increases Perceived Value (Management Science 57(9):1564-1579) | 🟢 A |
| F-916 | 🔬 | Nienaber, A.-M.; Hofeditz, M. & Searle, R. H. (según resumen de búsqueda; título exacto no verificado) | 2014 | Meta-análisis de confianza organizacional en el sector de servicios financieros (International Journal of Bank Marketing) | 🟢 A |
| F-917 | 🔬 | De Oliveira Santini, F.; Eberle, L.; Ladeira, W. J.; Milan, G. S.; Graciola, A. P. & Sampaio, C. H. | 2023 | Trust in the financial services context: a meta-analysis (International Journal of Bank Marketing 41(7):1693-1714; DOI 10.1108/ijbm-06-2022-0248) | 🟡 C |
| F-918 | 🔬 | Greene, C. & Stavins, J. | 2020 | Consumer Payment Choice for Bill Payments (Federal Reserve Bank of Boston, Working Paper 20-9) | 🔵 B |
| F-919 | 🔬 | Kosse, A. | 2021 | An empirical analysis of bill payment choices (Bank of Canada, Staff Working Paper 2021-23) | 🟡 C |
| F-920 | 📱 | Fiserv (citada en lámina del usuario) | 2023 | Números que hablan (Edición México) | 🟡 C |
| F-921 | 🔬 | Ericson, K. M. | 2014 | Consumer Inertia and Firm Pricing in the Medicare Part D Prescription Drug Insurance Exchange (American Economic Journal: Economic Policy 6(1):38-64; NBER WP 18359, 2012) | 🟢 A |
| F-922 | 🔬 | Experimento en Uganda (autoría no verificada), Mobarak y Rosenzweig (India) y otros | s.f. | Redes informales de riesgo y demanda de seguro formal: experimento en Uganda rural; seguro de lluvia en jatis de India | 🔵 B |
| F-923 | 🔬 | Eling, M. & Lehmann, M. (y Eling, Nuessle & Staubli, 2022) | 2018 | The impact of digitalization on the insurance value chain and the insurability of risks (Geneva Papers on Risk and Insurance 43(3):359-396); The effect of AI on the insurance industry (2022) | 🟢 A |
| F-924 | 💼 | McKinsey & Company | 2025 | The UK insurtech landscape: strong, shifting, collaborative | 🟡 C |
| F-925 | 💼 | NTT DATA (vía Kapronasia) | 2025 | Insurtech Global Outlook Report 2025 | 🟠 D |
| F-926 | 💼 | Capgemini y Efma (vía Insurance Business) | 2018-2019 | Informe mundial de insurtech: colaboración entre aseguradoras e insurtechs | 🟡 C |
| F-927 | 💼 | Gen Re | 2025 | 2025 U.S. Individual Life Next Gen Underwriting Survey | 🟡 C |
| F-928 | 💼 | Bain & Company (vía Insurance Business) | 2025 | Claims Maturity Assessment 2025 (81 aseguradoras P&C) | 🟡 C |
| F-929 | 💼 | BCG, Wavestone y Datos Insights (vía eMarketer y prensa) | 2025-2026 | Aseguradoras e IA: pilotos frente a escala | 🟡 C |
| F-930 | 💼 | Adacta (encuesta europea 2025), Insurance Global Operations (200 aseguradoras de EE.UU.) y Datos Insights (STP 2019) | 2019-2025 | Modernización de sistemas centrales de seguros y procesamiento directo | 🟡 C |
| F-931 | 📱 | J.D. Power (dic-2025; vía Business Wire y Repairer Driven News) | 2025 | 2025 U.S. Claims Digital Experience Study (complementa F-868) | 🟡 C |
| F-932 | 🏛️ | Gestión (publirreportaje de Insurance Day 2023, organizado por APESEG) | 2023 | Insurance Day 2023: tendencias que marcarán las estrategias empresariales del sector asegurador | 🟠 D |
| F-933 | 💼 | Forbes Perú (sobre Interseguro) | 2022 | Interseguro proyecta crecimiento de doble dígito en 2022 y mayores ventas en su canal digital | 🟠 D |
| F-934 | 🏛️ | Gestión (nota de junio de 2023), con una encuesta de Ipsos y un blog de Sovos | 2023 | Aseguradoras simplifican contratos y aceleran respuesta digital a siniestros | 🟠 D |
| F-935 | ⚖️ | SBS (Resolución 1121-2017, modificada por la 277-2021; vía ProActivo y El Peruano) | 2017-2021 | Reglamento de Comercialización de Productos de Seguros | 🟠 D |
| F-936 | 🏛️ | SBS, Paysafe, Peru Retail, Infomercado y Mercado Negro | 2025-2026 | Billeteras digitales en el Perú: usuarios y frecuencia | 🟠 D |
| F-937 | 💼 | Swiss Re Institute | 2023 | sigma 5/2023: The economics of digitalisation in insurance | 🔵 B |
| F-938 | 🔬 | Sakaguchi, H.; Stewart, N.; Gathergood, J.; Adams, P.; Guttman-Kenney, B.; Hayes, L. & Hunt, S. | 2022 | Default Effects of Credit Card Minimum Payments (Journal of Marketing Research 59(4):775-796; DOI 10.1177/00222437211070589) | 🟢 A |
| F-939 | 🔬 | Keys, B. J. & Wang, J. | 2019 (versión final no verificada; documento de trabajo desde 2014; Journal of Financial Economics según listados) | Perverse Nudges: Minimum Payments and Debt Paydown in Consumer Credit Cards | 🔵 B |
| F-940 | 🔬 | Guttman-Kenney, B.; Leary, J. & Stewart, N. (según la lámina; autoría exacta no verificada) | 2018 | Weighing anchor on credit card debt (FCA, Occasional Paper 43) | 🔵 B |
| F-941 | 🔬 | Medina, P. C. | 2021 | Side Effects of Nudging: Evidence from a Randomized Intervention in the Credit Card Market (Review of Financial Studies 34(5):2580-2607) | 🟢 A |
| F-942 | 🔬 | Agarwal, S.; Chomsisengphet, S.; Mahoney, N. & Stroebel, J. | 2015 | Regulating Consumer Financial Products: Evidence from Credit Cards (Quarterly Journal of Economics 130(1):111-164) | 🟢 A |
| F-943 | 🔬 | Soll, J. B.; Keeney, R. L. & Larrick, R. P. | 2013 (la lámina dice 2012) | Consumer Misunderstanding of Credit Card Use, Payments, and Debt: Causes and Solutions (Journal of Public Policy & Marketing 32(1):66-81) | 🟢 A |
| F-944 | 🔬 | Gathergood, J.; Mahoney, N.; Stewart, N. & Weber, J. | 2019 | How Do Individuals Repay Their Debt? The Balance-Matching Heuristic (American Economic Review 109(3):844-875) | 🟢 A |
| F-945 | 🔬 | Reshadi, F. & Fitzgerald, M. P. | 2023 | The pain of payment: A review and research agenda (Psychology & Marketing 40(5):1672-1688; DOI 10.1002/mar.21825) | 🟢 A |
| F-946 | 🔬 | Jachimowicz, J. M.; Duncan, S.; Weber, E. U. & Johnson, E. J. | 2019 | When and why defaults influence decisions: a meta-analysis of default effects (Behavioural Public Policy 3(2):159-186) | 🟢 A |
| F-947 | 🔬 | Barsky, R. B.; Juster, F. T.; Kimball, M. S. & Shapiro, M. D. | 1997 | Preference Parameters and Behavioral Heterogeneity: An Experimental Approach in the Health and Retirement Study (Quarterly Journal of Economics 112(2):537-579; NBER WP 5213) | 🟢 A |
| F-948 | 🔬 | Gächter, S.; Johnson, E. J. & Herrmann, A. | 2022 (revista no verificada) | Individual-level loss aversion in riskless and risky choices | 🔵 B |
| F-949 | 🔬 | Yechiam (2022) y Quentin & De Langhe (2021) (vía resultados de búsqueda; revistas no verificadas) | 2021-2022 | Críticas a la aversión a la pérdida (replicación con apuestas pequeñas y no invarianza de medida) | 🟡 C |
| F-950 | 🔬 | Mani, A.; Mullainathan, S.; Shafir, E. & Zhao, J. (más dos réplicas pequeñas) | 2013 (Science) | Poverty impedes cognitive function y réplicas con resultado nulo (Bogotá, n=417; pescadores de Tanzania, tesis) | 🟢 A |
| F-951 | 🔬 | Handel, B. R. | 2013 | Adverse Selection and Inertia in Health Insurance Markets: When Nudging Hurts (American Economic Review) | 🟢 A |
| F-952 | 🔬 | Abaluck, J. & Gruber, J. (y la disputa de Ketcham et al., 2012) | 2011 | Choice Inconsistencies among the Elderly: Evidence from Plan Choice in the Medicare Part D Program (American Economic Review) | 🟢 A |
| F-953 | 🔬 | Bhargava, S.; Loewenstein, G. & Sydnor, J. | 2017 (versión publicada no verificada; NBER WP 21160, 2015) | Choose to Lose: Health Plan Choices from a Menu with Dominated Option (Quarterly Journal of Economics) | 🟢 A |
| F-954 | 🔬 | Sydnor, J. | 2010 | (Over)insuring Modest Risks (American Economic Journal: Applied Economics) | 🟢 A |
| F-955 | 🔬 | Gottlieb, D. & Smetters, K. | 2021 (NBER WP 18601, 2012, "Narrow Framing and Life Insurance") | Lapse-Based Insurance (American Economic Review) | 🟢 A |
| F-956 | 💼 | LIMRA y SOA (vía MarketFacts) | 2020 | Life and Disability Lapse Behavior | 🟡 C |
| F-957 | 🔬 | PNAS (estudio sobre frecuencia de pago de ingresos; autoría no verificada) | c. 2022 | Frecuencia de pago de ingresos (salario, beneficios, lotería) y presupuesto (PNAS, artículo 2205877119) | 🔵 B |
| F-958 | 🔬 | FCA (Financial Conduct Authority, Reino Unido) | 2015 | Occasional Paper 12: Encouraging consumers to act at renewal — evidence from field trials in the home and motor insurance markets | 🔵 B |
| F-959 | ⚖️ | FCA y resúmenes de HFW, Clifford Chance y RTE (Banco Central de Irlanda) | 2022-2025 | Prohibición del *price walking* en seguros de hogar y auto (vigente desde enero de 2022) y su evaluación | 🟠 D |
| F-960 | 🔬 | Data Colada, PNAS (retractación) y Kristal et al. (2020) | 2012-2021 | Retractación de "Signing at the beginning makes ethics salient" (Shu, Mazar, Gino, Ariely y Bazerman, PNAS 2012) | 🔵 B |
| F-961 | 🔬 | Godet, M. (con Monti, Meunier y Roubelat) | 2000 (4.ª edición; primera versión de 1991) | La caja de herramientas de la prospectiva estratégica (Cuadernos de LIPS n.º 5) | 🟡 C |
| F-962 | 🔬 | Hiltunen, E. (y Ansoff, vía fuentes secundarias) | 2008 (Ansoff: años 1970, fecha exacta no verificada) | The future sign and its three dimensions (Futures) y definición de señal débil | 🟢 A |
| F-963 | 🏛️ | CEPLAN (vía Andina y su informe de 2022) | 2022-2026 | Perú 2050: Tendencias globales y regionales; fichas del Observatorio Nacional de Prospectiva | 🔵 B |
| F-964 | ⚖️ | Peru Retail, La República, Caretas y Buk (sobre la Ley 32413 y el DS 011-2026-EF) | 2025-2026 | Pago de sueldos, CTS, gratificaciones y pensiones por billeteras digitales | 🟠 D |
| F-965 | ⚖️ | El Peruano, Diario Bitcoin y Fiskil (sobre la SBS y el BCRP) | 2026 | Hoja de ruta de finanzas abiertas y reglamento de iniciadores de pago | 🟠 D |
| F-966 | 🔬 | Deque, Digital.gov y otros (sobre estudios de Nielsen Norman Group) | 2014-2025 | Los *placeholders* en campos de formulario son perjudiciales | 🟠 D |
| F-967 | 🏛️ | Banxico y Publimetro (México); Minsait Payments vía Infomercado (Perú) | 2022-2024 | Domiciliación (cobro automático) en México y preferencia de medio de pago en Perú | 🟠 D |
| F-968 | 💼 | Advanced Hindsight (caso de Irrational Labs) | 2018 | Aligning automatic payments with income (Beneficial State Bank) | 🟠 D |

---

## 8. Adenda v1.1 (2026-10-26): estado de la digitalización, insurtech y líneas de las láminas de banca

*Origen: pedido del usuario de ir "un paso más": (1) qué está digitalizado y qué no en seguros (mundo, LATAM, Perú), (2) cómo se relacionan digitalización, seguros e insurtech, y (3) trasladar a seguros la línea de investigación de cinco láminas de una presentación de banca en México. Los fragmentos sobre BanCoppel llegan después y no están integrados.*

### 8.1 Las láminas como líneas de investigación para seguros

Las láminas son del usuario. Lo que sigue separa lo que se pudo verificar de lo que no. **Cada traducción a seguros es hipótesis, no hallazgo.**

| Lámina | Qué afirma | Verificación | Traducción a seguros (hipótesis) | Cómo probarla |
|---|---|---|---|---|
| **Uso general de servicios financieros en México** (sin fuente visible) | 32% de adultos sin producto formal, 24% con uno, 28% con 2-3, 11% con 4-5, 5% con 6 o más; más de 90% de las transferencias en efectivo; ante imprevistos, primero la red de familiares y amigos | No verificable: la lámina no cita fuente. En Perú: 59% con cuenta (Findex 2024, F-880) y 67% con cuenta o billetera (SBS, fin de 2025, F-936) | El seguro cae en la categoría "resiliencia", donde compite con la red informal. La evidencia sobre si la red desplaza al seguro es **mixta**: sí en Uganda; en India depende del riesgo de base (F-922) | Preguntar a quién recurre el cliente ante un evento (familia, ahorro, crédito, seguro) antes de diseñar el canal |
| **¿Cómo es la relación con la banca móvil?** (Fiserv, 2023) | 90% opera por banca móvil, 68% muy satisfecho; se usa para saldo (83%) y transferencias (82%), poco para reportar robos (20%) e invertir (12%); fallas de acceso, de transacción y alertas tardías | **No verificada** (F-920): proveedor, método desconocido, es banca | Mismo patrón esperable en seguros: digital en tareas rutinarias y de bajo riesgo; poco en eventos de alto riesgo. Peru: SOAT ~90% digital frente a vida sin evidencia digital (§8.2) | Medir qué hace el cliente en la app (consultar póliza, constancia, pago) y qué no (siniestro, cambio de cobertura); ranking de tareas |
| **Transparencia operacional** (Buell y Norton, 2011) | Mostrar el proceso hace preferir servicios con más espera; la lámina da 62% vs. 42% (30 s) y 63% vs. 23% (60 s) | **Existe y el efecto central se confirma** (5 experimentos, F-915). Las cifras de la lámina **no se verificaron**. Esperas de 10-60 segundos en viajes y citas, no en trámites de días | Aplicable al siniestro y a la emisión: mostrar "qué se está revisando" en vez de "en proceso". La velocidad extrema ("1 minuto", F-889) y la transparencia son estrategias distintas y nadie las comparó en seguros. Evidencia indirecta: solo 22% de las aseguradoras da actualizaciones adecuadas y la satisfacción es mayor con actualizaciones por app (F-931) | A/B en el seguimiento del siniestro: pasos visibles frente a estado genérico; medir llamadas por estado, percepción de valor y confianza |
| **Confianza, un factor clave** (meta-análisis) | Más confianza en el banco sube compromiso, lealtad, intención de compra y costos de cambio; palancas: comunicación oportuna, influencia social, facilidad de uso, utilidad, satisfacción, competencia, seguridad, privacidad y aseguramiento estructural | **El paper citado (De Oliveira Santini et al., 2023) no apareció en la búsqueda** (F-917). Sí se verificó otro meta-análisis (93 estudios, F-916): el **entorno regulatorio** pesa más en servicios financieros que en otras industrias | En seguros se suma un antecedente que el marco bancario no destaca: **el pago del siniestro** (F-851, F-852). La regulación como "aseguramiento estructural" se vuelve comunicable (SBS, Indecopi) | Medir los antecedentes de la lámina como moderadores de renovación y reclamo; comparar el peso del pago del siniestro |
| **¿Hay usuarios propensos a automatizar?** (Greene y Stavins, 2020; Kosse, 2021) | El nivel socioeconómico condiciona programar pagos; de ahí hipótesis de dolor de pago y aversión a la pérdida | Greene y Stavins verificado (F-918): pagan en automático quienes tienen más ingreso y gasto en facturas, **sin efecto de saliencia**; Kosse **no verificado** (F-919). El salto a dolor de pago y aversión a la pérdida **no está en el resumen** | Autopago y renovación automática diferenciados por segmento. **Riesgo:** la inercia tiene efectos persistentes y las aseguradoras suben precio a los antiguos (~10% más, Ericson 2014, F-921). En Perú el default del desgravamen ya se eliminó (F-877) | Mensajes diferenciados por ingreso; consentimiento explícito; vigilar precio a renovantes; resultados de ReachUHC pendientes (F-856) |

**Cambio a la definición de cliente digitalmente sano (§5b).** Se agrega una capa de **fiabilidad**: tasa de fallas de acceso, de transacción y de notificaciones. La lámina de banca móvil las lista como los problemas dominantes (F-920, no verificada) y en seguros solo 22% de las veces se dan actualizaciones adecuadas (F-931). Un cliente no puede ser "sano digital" si el canal le falla.

### 8.2 Qué está digitalizado y qué no

**Cómo leerlo.** 🟢 digitalizado a escala con alguna cifra · 🟡 parcial o solo anuncios · 🔴 poco o nada · ⬜ sin dato hallado. La columna "Lectura" es inferencia mía. **No se halló participación de venta digital sobre primas para Brasil, Colombia ni México; en Perú solo cifras sueltas de gremio y publirreportaje.**

| Etapa | Mundo | LATAM | Perú | Lectura |
|---|---|---|---|---|
| **Buscar y cotizar** | Las herramientas de comparación casi duplican la probabilidad de considerar comprar (EE.UU., F-867) | ⬜ | 67% prefiere lo digital para buscar y cotizar, no para comprar (publirreportaje, 2023, F-932) | 🟢 como consulta |
| **Comprar un producto simple** | ~47% de las compras en EE.UU. son digitales (F-867) | ⬜ por país | SOAT ~90% digital (gremio, F-884); Interseguro ~70% de su SOAT (2022, F-933); **pero solo 21% de las pólizas online (2023, F-932)**: no concilian | 🟢 en SOAT, 🟡 en el resto |
| **Comprar un producto complejo** (vida, salud, empresas) | Confianza, asesoría y complejidad frenan la compra digital de punta a punta (F-885); Corea: lo online en vida cayó 33,6% en una década (`futuro-asesores-seguros-venta-digital`) | Bancaseguros domina vida en Brasil; corredores/agentes 80-85% de no vida (F-887) | Sin evidencia digital de vida | 🔴 humano o híbrido |
| **Suscripción** | EE.UU. vida: 59% de solicitudes califica a suscripción acelerada (F-927); en líneas complejas el procesamiento directo es bajo (2019, F-930) | Azos: suscripción digital que se distribuye por corredores (F-377) | ⬜ | 🟡 (🟢 en vida simple, EE.UU.) |
| **Emisión y póliza electrónica** | ⬜ | ⬜ | Venta a distancia regulada; documentos dentro de 15 días; pólizas de una hoja; "el regulador a veces prefiere el papel" (F-934, F-935) | 🟡 |
| **Cobranza** | ⬜ | ⬜ | **Infraestructura sí:** 67% de adultos con cuenta o billetera, Yape ~16 M (F-936); Pacífico cobra seguros por Yape (F-888). **Porcentaje de primas cobradas digitalmente: sin dato** | 🟢 la infraestructura; ⬜ su uso en seguros |
| **Servicio y autogestión** | Satisfacción en servicio 695/1000 (−4); solo 11% usa chatbot (F-867) | ⬜ | Apps de La Positiva y Pacífico; uso desconocido (F-890) | 🟡 |
| **Aviso de siniestro** | Lemonade: la detección de choque por app acelera el primer aviso (F-904) | Mapfre Brasil por WhatsApp con IA (F-893); caso de proveedor en México (F-894) | Chatbot de Rímac (F-889); app de La Positiva (F-890) | 🟡 anuncios sin resultados |
| **Seguimiento y decisión del siniestro** | Actualizaciones adecuadas **solo 22% de las veces** (F-931); **4% escaló IA generativa en siniestros y 27% busca transformarlos por completo** (F-928) | ⬜ | Reclamos y sanciones se concentran en plazos y rechazos (F-875, F-876) | 🔴 el punto menos digitalizado y más sensible |
| **Renovación** | La inercia tiene efectos persistentes (F-921) | ⬜ | ⬜ | ⬜ |
| **Sistemas centrales** | 42% califica su sistema con C o menos y 63% tiene el mismo hace 11 años o más (EE.UU.); 51,8% de decisores europeos está modernizando (F-930) | ⬜ | ⬜ | 🔴 cuello de botella estructural (sin dato local) |

**Patrón (inferencia):** lo digital está **en los bordes** (buscar, comprar algo simple, pagar) y lo manual **en el medio** (suscripción compleja, decisión y seguimiento del siniestro, sistemas centrales). Es el mismo patrón que la lámina de banca móvil (mucho en saldo y transferencias, poco en inversión y reportes). Y es coherente con Swiss Re: más digitalización no implica compra digital de punta a punta (F-885).

**Por ramo en Perú.** SOAT 🟢 · Salud 🟡 (Seguro Salud Yape con teleconsulta, F-888) · Vehicular 🟡 (Rímac, La Positiva) · Vida 🔴/⬜ (sin evidencia digital; ver `proyecto-back-to-basics-ffvv-vida`) · Hogar y robo ⬜ (las multas de Indecopi son por peritaje y condiciones, no por canal, F-485) · Riesgos generales y empresas ⬜ · Microseguros ⬜ (diagnóstico del PNUD sin abrir, F-882) · Agrario ⬜.

**Dos distinciones útiles.** (1) Que Perú tenga rieles de pago digitales (Yape, Plin) **no** significa que el seguro esté digitalizado: la infraestructura es de la banca. (2) Un anuncio de producto digital no es uso: casi ningún actor publica cuántos clientes lo usan.

**Contradicciones nuevas, sin resolver.**
- **Venta digital en Perú:** 21% de las pólizas online (F-932) frente a SOAT 90% y 70% (F-884, F-933). Pueden medir cosas distintas (pólizas frente a emisiones, años distintos), pero no concilian.
- **Confianza en aseguradoras:** 14% (Ipsos 2023, F-934) frente a ~23-25% del node previo.
- **Cuentas y billeteras:** 59% (Findex 2024, F-880) frente a 67% (SBS, fin de 2025, F-936): años y definiciones distintos.
- **Plin:** 4 M (Peru Retail) frente a 8 M (Infomercado) de usuarios (F-936).

### 8.3 Digitalización, seguros e insurtech

- **Marco teórico.** La digitalización toca toda la cadena de valor y además cambia lo que es asegurable: mejora la experiencia, simplifica procesos, habilita productos nuevos y expone a competidores de otras industrias; la información adicional cambia la asimetría y el pooling, y la conectividad aumenta la interdependencia de riesgos (Eling y Lehmann, 2018, F-923). Esto conecta con la selección adversa del node de comportamiento.
- **Quién la hace.** La evidencia, débil y en parte de otros países, apunta a que la digitalización es sobre todo un proyecto de las aseguradoras tradicionales con insurtechs como **habilitadores**:
  - En el Reino Unido, ~75% de las insurtechs son habilitadores y solo 9% del financiamiento de 2024 fue a entidades aseguradoras (75% en 2021) (F-924).
  - Las insurtechs de pila completa luchan con costos de adquisición y poco historial de suscripción (F-925, informe leído por blog).
  - ~96% de las aseguradoras tradicionales se declaraba abierta a colaborar (2018-2019, dato antiguo, F-926).
  - El caso insignia de pila completa, Lemonade, sigue con pérdida neta (F-509); Azos crece distribuyendo por corredores (F-377).
- **Tamaño regional.** 576 insurtechs en LATAM y US$90 M en el 1S 2026 (F-374) frente a US$2.440 M globales en el 2T 2026, con 99,1% a IA (F-901). La región es un jugador pequeño del capital de riesgo.
- **Digitalizar no es penetrar.** Perú sigue en ~2% del PBI y el sistema creció +1,1% en el 1S 2026 (F-506). Ninguna fuente prueba que la digitalización haya movido la penetración.
- **Pendiente:** no se buscó el ecosistema insurtech peruano (qué actores, qué casos). Y falta el rol del **banco como canal digital**, que es justo lo que ilustran las láminas de banca (ver §8.4).

### 8.4 Pendientes y supuestos

1. **Fragmentos de BanCoppel.** No los he visto. Una búsqueda sobre BanCoppel solo devolvió su app y el modelo "phygital" en tiendas Coppel; **nada sobre seguros ni sobre "señales"** (sin registrar en el ledger). **Supuesto por confirmar:** por "señales" entiendo comportamiento observable del cliente usado para decidir a quién ofrecer qué y cuándo. Si es otra cosa (por ejemplo, señales de mercado o de scoring), se reorienta.
2. **Verificar** F-917 (confianza), F-919 (Kosse) y F-920 (Fiserv) con los resúmenes oficiales.
3. **Porcentaje de primas por canal** de Brasil (SUSEP, CNseg), México (AMIS, CNSF), Colombia (Fasecolda) y Perú (SBS, APESEG): hay que abrirlos directo; los hosts relevantes estaban bloqueados o la búsqueda no los trajo.
4. **Auditoría de experiencia** (cliente incógnito) de las apps peruanas.

---

## 9. Adenda v1.2 (2026-10-26): defaults, pago y automatización

*Origen: cinco láminas más de banca (defaults y pago mínimo, pagos automáticos, incertidumbre y aversión a la pérdida, malentendidos en el pago, dolor del pago) y varios links; el usuario pidió ir más allá de la banca hacia seguros. Las señales de cambio (foresight) **no se incorporan aquí**: el usuario las tratará en un acápite propio. Es un campo exploratorio: salvo donde se cita evidencia, lo que sigue son hipótesis.*

### 9.1 Verificación de las cinco láminas

| Lámina | Lo que afirma | Lo que se encontró | Veredicto |
|---|---|---|---|
| **Defaults y pago mínimo** | La gente se ancla en el mínimo y deja de ahorrar 19,8% en intereses; la información adicional es ineficaz; ocultar el mínimo y mostrar el saldo sube el pago medio 26,74% | Sakaguchi et al. (F-938) existe. En la versión publicada, el pago automático al mínimo explica **~8% de todo el interés pagado** (12% en un borrador de 2018); proponen ocultar el mínimo y dirigir la atención al saldo total. Keys y Wang (F-939): pagos bimodales, 29% cerca del mínimo, **menos de 1%** adopta un pago alternativo sugerido. Agarwal et al. (F-942): el aviso de ahorro movió 0,5 pp sin cambiar el pago total. Un resumen sobre el documento de la FCA (F-940) dice que el mínimo funciona **más como meta que como ancla**. Navarro-Martinez (2011): no apareció | **Dirección confirmada. Las cifras 19,8% y 26,74% no se verificaron.** Matiz: "ancla" frente a "meta" |
| **Pagos automáticos** | Reducen 12% los pagos no hechos a tiempo; el experimento de Irrational Labs da +14%; alinear con la nómina lleva las faltas a ~0; en automático muchos eligen el mínimo y el total pagado cae 75% | Sakaguchi (F-938): quien automatiza al mínimo **paga más interés del que evita en mora**. Irrational Labs (F-968): resumen cualitativo, mejora inscripción y repago; sin cifras. Baugh (2017): no apareció. ⚠️ El 8% y el 12% de Sakaguchi son **porcentajes del interés pagado**, no de usuarios morosos: la lámina puede haber confundido el 12% | **Mecanismo confirmado (ahorra mora, cuesta interés). Cifras 12%, 14% y 75% sin verificar** |
| **Incertidumbre y aversión a la pérdida** | La aversión a la pérdida es mayor con menor ingreso; por eso los de rentas bajas automatizan menos | Barsky et al. (F-947) mide tolerancia al riesgo y la liga a no tener seguro, pero explica poco y **no muestra que el menor ingreso implique más aversión**. Gächter et al. (F-948): la aversión a la pérdida **sube con la edad, el ingreso y la riqueza**. El node de fenómenos psicológicos la reporta mayor en mayores y menor en quien conoce el producto (F-724). Críticas de replicación en apuestas pequeñas (F-949) | **No sostenida como está escrita.** La hipótesis final (los de menor ingreso automatizan menos por querer control) puede ser cierta por otras vías (§9.2: liquidez y desfase de ingreso) |
| **Malentendidos en el pago** | El *payment-interest bias* surge de la numeracia y de la información desglosada; además se olvida pagar o no se puede | Soll, Keeney y Larrick (F-943; es de **2013**, no 2012): se subestima el tiempo de pago y los menos numerados fijan pagos muy bajos; el estado de cuenta rediseñado por la ley CARD redujo los sesgos. El nombre *payment-interest bias* no apareció. Gathergood et al. (F-944, no está en la lámina): se reparte el pago por saldo y no por tasa, aun con más en juego | **Confirmada en lo central.** Lusardi y Tufano (2009) no se verificó |
| **El dolor del pago** | Con ingreso de 8.000, 400 duelen más que con 20.000; la automatización reduce el dolor pero también la atención a los pagos | Reshadi y Fitzgerald (F-945) existe: dolor **inmediato o anticipado**, con cualquier recurso que dé seguridad; "tacaños" lo sienten más. **El ejemplo del ingreso y el efecto de la automatización no se verificaron** | **Concepto confirmado; las dos afirmaciones concretas, sin verificar** |

**Links adicionales.** Buell y Norton (F-915): verificado. El meta-análisis de confianza del enlace de Emerald es F-917: sigue sin abrirse. El estudio de Treo y arXiv 1803.05032: **no los pude abrir** (la búsqueda no los halló y el acceso directo a esos sitios falla); si me dices el título, los busco por nombre. El artículo de NN/g sobre *placeholders* (F-966): solo por resúmenes secundarios. JSTOR 2951245: no lo abrí; no confirmo que sea Barsky.

### 9.2 Qué agrega la literatura para seguros: pago, renovación y caducidad

*Esta sección cubre solo el tramo de pago y mantenimiento. El resto del ciclo (considerar, elegir, creer, asesoría, selección) está en [[economia-conductual-seguros-literatura|Economía conductual de los seguros: qué dice la literatura]].*

| Tema | Hallazgo | Evidencia | Qué significa para seguros |
|---|---|---|---|
| **Defaults** | Efecto medio d = 0,68 (58 estudios) con **mucha variación**, algunos nulos y dos negativos (F-946). El node de tendencias ya registra que el *opt-out* no superó al *opt-in* en un enrolamiento (F-357) | Meta-análisis | No hay "default universal". Hay que probarlo en cada decisión |
| **Inercia y precio** | Los defectos iniciales persisten y los planes antiguos pagaban ~10% más (F-921). Quitar la inercia puede **empeorar** el mercado: Handel duplica la pérdida por selección adversa (F-951). La prohibición británica del *price walking* (2022) proyectó £3.700-4.200 M de ahorro; su evaluación de 2025 halla menores precios en auto y nada en hogar, con franquicias obligatorias más altas en auto (F-959) | Observacional y regulatorio; evaluación vía resúmenes | La renovación automática sin vigilancia es un riesgo de conducta, y un "nudge" bien intencionado puede dañar al conjunto |
| **Caducidad: olvido frente a liquidez** | En una aseguradora, **el olvido explica 37,8% de las caducidades recientes y la liquidez inesperada 15,4%** (F-955) | Encuesta + modelo, AER | El autopago ataca la causa mayor, pero solo en ese contexto. **No hay dato peruano** |
| **Automatizar tiene un costo de atención** | Quien automatiza al mínimo paga más interés (F-938). Los recordatorios bajaron la mora 14% pero subieron 9% los sobregiros, **5% más caro en conjunto para quien ya usaba sobregiros** (F-941) | RCT y datos transaccionales | La fricción se mueve: quien tiene ingreso irregular puede pasar de caducar por olvido a quedarse sin fondos el día del cobro |
| **Información** | Un aviso de ahorro movió 0,5 pp y no cambió el pago total (F-942); menos de 1% adopta el pago sugerido (F-939). **Pero** en seguros de hogar, poner la **prima del año anterior** en el aviso de renovación subió 11-18% los que cambian o negocian; en auto no hubo efecto; avisos simplificados, folletos y recordatorios casi no movieron nada (F-958) | Experimentos de campo | La información que **compara con un punto de referencia propio** puede mover; la que solo explica, casi no. Coincide con "explicar más no basta" (F-6, F-9) |
| **Anclas y menús** | Se eligen deducibles bajos con primas muy superiores al valor esperado (F-954); los mayores subponderan costos de bolsillo frente a la prima (F-952); con una opción dominada muchos eligen peor (F-953) | Observacional, AER y QJE | El deducible y la suma asegurada son anclas; el menú importa más que la explicación |
| **Frecuencia de pago** | Más frecuencia se asocia a más caducidad (¿efecto recordatorio?) pero es observacional (F-956); **72% de quien elige cobro mensual lo hace para presupuestar** (F-957, no es seguros) | Industria + PNAS | Tensión sin resolver: lo mensual ayuda a presupuestar y puede aumentar la caducidad |
| **Pobreza y atención** | El efecto "la escasez resta capacidad cognitiva" tiene dos réplicas pequeñas sin efecto (F-950) | Original arbitrado + réplicas débiles | No sostener decisiones de diseño sobre "ancho de banda" como hecho firme |
| **Honestidad al declarar** | "Firmar al inicio" se apoyaba en un estudio con una aseguradora de autos cuyos **datos estaban fabricados**; se retractó y no replicó (F-960; ver F-615) | Retractación | No usar esa táctica como "probada" en declaraciones de siniestro o de millaje |
| **Reparto de pagos** | La gente reparte por saldo y no por tasa, aunque el error cueste más (F-944) | 1,4 M de personas | Con varias obligaciones (créditos, seguros), el pago de la prima puede quedar en el último lugar **sin que sea desinterés** |

**Tres lecciones.**
1. **Automatizar lo que se olvida, no lo que exige atención.** El autopago resuelve el olvido, pero tiene trampas conocidas (el mínimo, el desfase de liquidez) (F-938, F-941).
2. **La información útil compara con algo propio.** Lo genérico casi no mueve; la prima del año anterior sí, al menos en hogar (F-958).
3. **Un nudge puede mover el daño de lugar.** Medina (F-941) y Handel (F-951) lo muestran en dos niveles distintos: en la persona y en el mercado.

### 9.3 Diseño del pago de primas: hipótesis para probar

Son hipótesis de diseño, no resultados. El análogo del "pago mínimo" en seguros no es el interés sino la **cobertura**: pagar menos o tarde no genera deuda, genera suspensión.

| # | Hipótesis | Apoyo | Cómo probarla | Riesgo |
|---|---|---|---|---|
| **DP1** | **Antes de diseñar, medir por qué caducan en Perú:** olvido, falta de liquidez, desinterés o insatisfacción | F-955 (37,8% frente a 15,4% en otro contexto) | Encuesta a recién caducados + clasificación de cobros fallidos | Que el autopago se invierta sobre una causa que no es la mayor |
| **DP2** | **Cobrar cuando entra el ingreso, no en una fecha fija** (sueldo en billetera o entrada de dinero) | F-847 (pago al cosechar), F-968, F-964 | A/B con grupo de control en billetera | Sobregiros o cobros fallidos (F-941); informales sin día fijo |
| **DP3** | **Autopago con "latido":** aviso previo al cobro, revisión periódica y comparación con el precio anterior | F-958, F-921, F-959, F-945 (atención) | A/B de renovación con y sin comparación | Consentimiento y fiscalización por Indecopi |
| **DP4** | **Mostrar la consecuencia en cobertura** ("tu cobertura se suspende el [fecha]") al pagar menos o tarde | Adaptación de la lámina; F-945 (dolor anticipado) | A/B de texto en el pago | El encuadre de pérdida es "replicado con matices" y varía por persona (F-221, F-724) |
| **DP5** | **Frecuencia de pago:** mensual con recordatorio frente a anual | F-956, F-957 | Cohortes por frecuencia con emparejamiento | Observacional: no separa causa |
| **DP6** | **Formularios de pago con etiqueta visible** y la opción "otra cantidad" sin texto que desaparece | F-966 (solo secundaria) | Prueba de usabilidad | Evidencia débil |
| **DP7** | **Menús de deducible y cobertura sin opciones dominadas** y con default explícito | F-952, F-953, F-954 | Experimento de arquitectura de elección | Manipulación si se usa el señuelo a propósito (node de fenómenos psicológicos) |

**Cambio a las definiciones basales (§5b).** En **fidelidad**, la caducidad por olvido no es deslealtad: hay que **clasificar la causa de cada caducidad** antes de leer "caducó" como "no era fiel". En **cliente digitalmente sano**, el autopago no es un éxito por sí mismo: cuenta si el cliente conserva atención sobre lo que paga (revisión periódica, sin sobrecobros).

### 9.4 Pendientes de esta adenda

1. **Abrir** el estudio de Treo, arXiv 1803.05032 y el artículo de NN/g (necesito el título o que me lo pegues).
2. **Verificar** F-917 y F-919 (láminas) y las cifras de las láminas 6-10 contra los papers.
3. **Medir en Perú** lo que la literatura sugiere y no tiene dato local: causa de caducidad (DP1), cobro automático de primas, proporción de cobro por billetera.

---

## 10. Adenda v1.3 (2026-10-27): qué más explica la digitalización, además de las cuatro variables

### 10.1 Respuesta corta

**Sí hay más, y conviene reordenarlas.** Las cuatro variables de §2 (momento, confianza, liquidez e irregularidad del
ingreso, complejidad y habilidad percibida) describen sobre todo **la disposición de la persona**: si quiere y le
conviene. Dejan fuera dos grupos:

- **Los habilitadores:** si **puede** (tener dispositivo, conexión, habilidades, un medio de pago digital y poder
  identificarse).
- **El entorno:** si el sistema se lo **facilita** (la gente cercana, la regulación, cómo le llega el producto y la
  calidad de lo digital que se le ofrece).

Con eso la lista pasa de 4 a 17 candidatas (las 4 originales más 13 nuevas, algunas de las cuales refinan una original) en tres familias (§10.3). **Ninguna evidencia de las que siguen modela estas
variables juntas para seguros en Perú:** son candidatas, no hallazgos, y "explican mejor" sigue sin comprobarse (§2 ya lo
marcaba como hipótesis).

### 10.2 Qué tan sólidas son las cuatro originales

Antes de sumar, conviene decir que las cuatro no tienen el mismo respaldo:

| Variable original | Respaldo | Fuente | Lectura |
|---|---|---|---|
| **O1 · Confianza en la contraparte** | 🟢 Fuerte | RCT de campo en Kenia y China (F-849, F-850); una encuesta independiente en Jordania la halla como el factor de mayor peso (β = 0,52; F-1030) | La mejor sostenida |
| **O2 · Liquidez e irregularidad del ingreso** | 🟢 Fuerte, pero agrícola | RCT en Kenia (F-847) | Causal, en cañeros; el traslado a asalariados e informales urbanos es hipótesis |
| **O3 · Momento (comprar frente a siniestrarse)** | 🟡 Moderado | Swiss Re (F-885): la digitalización sube, pero la compra de punta a punta la frenan confianza, asesoría y complejidad | Informe de reaseguradora; no causal |
| **O4 · Complejidad y habilidad percibida** | 🟡 Débil | Un estudio ruso de 244 personas de 50+ y una tesis de Lima (F-861, F-862) | No son de seguros; muestras pequeñas |

### 10.3 Las variables que se suman, por familia

Tres familias (**puede, quiere, le llega**) y 17 variables: las cuatro originales (O1 a O4) y trece nuevas (N1 a N13);
N2, N5, N6 y N8 refinan o separan una original. Es una organización mía, no un modelo validado.

**Familia 1 · Puede (habilitadores)**

| # | Variable | Qué evidencia hay | Dato peruano | Apoyo |
|---|---|---|---|---|
| N1 | **Dispositivo y conexión** (incluye brecha de género) | Estudios con datos de Findex hallan que tener celular y conexión son los mayores impulsores de adopción fintech (F-1033). GSMA: un celular básico cuesta 24% del ingreso mensual de una mujer frente a 12% del de un hombre, y las mujeres son 14% menos propensas a usar internet móvil en países de ingreso bajo y medio (F-1034) | 95,7% de hogares con celular (rural 88,1%); 60,1% con internet en el hogar (rural 23,4%); 82,0% de la población usa internet, 89,2% desde el celular (4T 2025; F-1035) | 🟡 |
| N2 | **Habilidades digitales y financieras** (distinto de la habilidad *percibida* de O4) | Una revisión con metaanálisis en África subsahariana halla que facilidad y utilidad percibidas son los mayores predictores de adopción de fintech móvil (F-1032); GSMA cita las habilidades como segunda barrera (F-1034). **Educar no basta:** en microseguros la educación al cliente subió el conocimiento pero no la demanda (F-1037) | El BCRP encuentra menor adopción de medios digitales entre quienes tienen menos instrucción (F-1041) | 🟡 |
| N3 | **Medio de pago digital y uso del efectivo** | El cobro alineado al ingreso es lo que mejor funcionó (F-847); en Perú condiciona la cobranza digital (DP2 de §9.3) | Cuentas: 59% (2024) y dinero móvil 42% (F-880); 14% usó solo efectivo en el mes; en los niveles D y E predomina el efectivo (65%) (F-1041; fuentes discrepantes en el nivel) | 🟡 |
| N4 | **Identificación y verificación (KYC)** | En países de ingreso bajo, 26% de los adultos sin cuenta cita no tener documentación (Findex 2017); las mujeres pobres tienen ~30% menos probabilidad de tener documento (F-1036). Un resumen de MicroSave dice que quien no pasa el KYC queda fuera de seguros y pensiones (F-1036) | No hallado. **Hipótesis mía:** en Perú el documento de identidad probablemente no sea el límite; la fricción de verificar en el alta sí puede serlo (cifras de abandono de 40-68% vienen de guías de proveedores, F-1025 de `hipotesis-digitalizacion-seguros-evidencia-publica`) | 🟠 |

**Familia 2 · Quiere (disposición)** (O1 confianza, O2 liquidez, O3 momento, O4 complejidad ya están aquí)

| # | Variable | Qué evidencia hay | Dato peruano | Apoyo |
|---|---|---|---|---|
| N5 | **Utilidad y facilidad percibidas** | Metaanálisis en África subsahariana (F-1032). En un estudio de seguros en Jordania de 346 personas, una vez que entran confianza y actitud, el esfuerzo esperado no tiene efecto directo (preprint, F-1031) | No hallado | 🟡 |
| N6 | **Riesgo percibido (fraude y datos)** | En Jordania el riesgo percibido resta (β = −0,18; F-1030). **El efecto de la preocupación por la privacidad no está establecido:** en un preprint el signo se invierte al corregir endogeneidad (F-1031) | 67% teme el fraude y 66% el robo de datos bancarios al comprar en línea (Ipsos, 2023); 39% se siente seguro en plataformas financieras en línea (Kaspersky, 2024). **No son de seguros** (F-1039) | 🟡 |
| N7 | **Propuesta de valor percibida y sustitutos informales** | Una revisión de ~30 estudios (OIT, 2013) lista cinco determinantes de la demanda: comprensión, propuesta de valor, liquidez, confianza y **otros mecanismos para enfrentar el riesgo** (F-1037). Las redes informales pueden desplazar o complementar al seguro (F-922) | De los peruanos que perdieron ingresos, 19% tenía respaldo asegurador (F-1006); 48% desconfía por no entender su póliza (Datum, vía prensa; F-1039) | 🟡 |
| N8 | **Preferencia por un contacto humano** (refina "confianza" y "complejidad") | Accenture: 58% confía en un asesor presencial para un reclamo frente a 12% en un servicio automatizado (año no verificado); J.D. Power 2016: solo 7% prefiere un canal digital para reportar el siniestro (F-1040); Insurity 2025: 59% de los *baby boomers* prefiere hablar con una persona (F-865) | Entre quienes no compran en línea, 55% quiere ver el producto antes (Kantar); casi la mitad prefiere lo presencial al comprar seguros (BCG, vía prensa) (F-1039) | 🟡 |

**Dos confianzas distintas (inferencia mía).** O1 mezcla la confianza **en la aseguradora** (que pagará) y la confianza **en el canal** (que no
habrá fraude ni error). N6 y N8 son la segunda; F-849 y F-850 son la primera. Conviene medirlas por separado.

**Familia 3 · Le llega (entorno y oferta)**

| # | Variable | Qué evidencia hay | Dato peruano | Apoyo |
|---|---|---|---|---|
| N9 | **Gente cercana (redes e influencia social)** | En China, un amigo tratado equivale a una rebaja de 13% en la prima, por difusión de conocimiento (F-978). En Pakistán, los hogares de una misma red renuevan de forma parecida, y eso puede amplificar la selección adversa; en Tanzania, la responsabilidad conjunta genera el incentivo de no asegurarse y apoyarse en los pares (F-1038). En modelos de intención de seguros en Jordania, la influencia social aparece débil (F-1031) | No hallado | 🟡 |
| N10 | **Regulación y protección percibida** | En Jordania la protección regulatoria sube la intención (β = 0,12) y la confianza: actúa en parte **a través de la confianza** (F-1030) | Reglamento de IA vigente desde enero de 2026 (F-1005); sanciones por plazos y rechazos (F-875, F-484); desgravamen opcional (F-877). Que esto sea una señal de confianza para el cliente es **inferencia mía** | 🟡 |
| N11 | **Cómo llega el producto** (obligatorio, embebido o elegido) | El SOAT, obligatorio, se emite ~90% digital (F-884); **eso no prueba adopción voluntaria** (inferencia). Los defectos cambian cómo se decide (§9.1). Un titular patrocinado dice que 43% compraría un seguro integrado a otra compra (solo el titular, F-1043) | Idem | 🟠 |
| N12 | **Calidad de la oferta digital** | La revisión de África subsahariana señala que **el lado de la oferta está poco estudiado** (F-1032). En EE.UU. la satisfacción con webs y apps de seguros bajó, muchos no encuentran lo que buscan y muchos ignoran los asistentes virtuales (F-1009); entre 21% y 28% evitó reclamar por la frustración del proceso (F-865) | No hallado | 🟡 |
| N13 | **Intermediario como puerta** (agente o corredor con herramienta digital) | En mercados emergentes agentes y corredores siguen dominando; hay plataformas con más de 30.000 agentes de punto de venta (India), **sin resultados medidos** de efecto en contratación o renovación (F-1042) | Corredores 60-65% (ambiguo; F-887) | 🟠 |

### 10.4 Cómo se ordenan por etapa (inferencia mía)

Las familias pesan distinto según la etapa; coincide con el mapa de §8.2:

| Etapa | Pregunta | Familia y variables dominantes (hipótesis) |
|---|---|---|
| Entrar a lo digital | ¿Puede? | Habilitadores (N1 a N4) |
| Contratar | ¿Quiere y confía? | Disposición: confianza (O1), utilidad (N5), riesgo percibido (N6), valor (N7), complejidad (O4) y momento de compra (O3) |
| Usar y reclamar | ¿Cumplen y me atienden? | Momento de siniestro (O3), contacto humano (N8), calidad de la oferta (N12) |
| Renovar | ¿Se queda? | Liquidez y cobro (O2, N3), cómo llegó el producto (N11), gente cercana (N9), experiencia del pago del siniestro (O1) |

### 10.5 Qué cambia para el diseño y la medición

1. **Separar "no puede" de "no quiere" y de "no le llegó bien".** El mismo "no digital" tiene causas distintas, y cada una
   pide una respuesta distinta (conexión, confianza o rediseño de la interfaz). Es la misma distinción entre "no funciona"
   y "no se intentó" de `hipotesis-digitalizacion-seguros-evidencia-publica`.
2. **Lo que `lapuerta` ya modela y lo que no.** Ya tiene acceso digital, bancarizado, educación financiera, confianza,
   canal, apertura a datos e IA y disposición a compartir datos. **No tiene** preferencia por contacto humano, uso de efectivo
   frente a medio digital, cómo llegó el producto, calidad percibida de la oferta digital ni influencia de la red. Es solo una
   propuesta: cualquier cambio al modelo pasa por `/cerrajero`, que pregunta antes de aplicarlo.
3. **Perú no tiene un estudio que mida estas variables juntas para seguros.** Solo hay datos por variable (conexión,
   cuentas, medios de pago, miedo al fraude) y casi ninguno es de seguros.

### 10.6 Límites y pendientes

**Límites.** Todo se leyó por resúmenes. Los estudios de Jordania y de Bangladesh son encuestas transversales y de
conveniencia, y el de África subsahariana trata fintech móvil, no seguros. No se halló revisión sistemática de adopción de
*insurtech*. Las cifras del INEI son preliminares en algunos informes. Las cifras de prensa peruana (Ipsos, Kaspersky,
Kantar, Datum, BCG) no se contrastaron con sus originales.

**Pendientes (en orden de valor).**

1. Tablas peruanas de Findex 2025 por edad, ingreso y género, con los motivos de no tener cuenta.
2. Cortes de la ENAHO sobre motivos de no uso de internet y uso por edad y nivel socioeconómico.
3. Contrastar las cifras de Datum y BCG con sus informes.
4. Buscar una revisión sistemática de adopción de seguros digitales y modelos para América Latina.
5. Abrir el informe completo de GSMA (solo se leyó el comunicado).
6. Si la aseguradora tiene dato, probar las 17 variables juntas en un modelo explicativo de adopción y renovación.

---

## 11. Adenda v1.4 (2026-10-27): casos conductuales y estratégicos en México, Colombia, Chile y Argentina

*Origen: pedido del usuario de ver qué casos hay en estos cuatro países para la lógica de §3. Se buscó con la metodología de `/trinidad` (pista empírica/teórica y pista de negocio; la social no se corrió). Todo se leyó por resúmenes de búsqueda y notas de prensa; muchas notas no traen fecha.*

### 11.1 Respuesta corta

- **Hay casos estratégicos, casi ninguno conductual medido.** No se halló **ni un experimento de campo sobre seguros** en estos cuatro países. Lo más cercano está en países vecinos: un experimento aleatorizado de seguro de salud para trabajadores informales en Nicaragua (inscripción de solo 20%), un experimento de laboratorio sobre empujones en Bolivia y un experimento de conducta con seguro de rendimiento por área en Perú (F-1060).
- **Los casos mejor documentados son de regulación y de diseño del sistema, no de plataformas.** En Chile, la licitación de seguros ligados a créditos hipotecarios (2012). En Argentina, el botón de baja obligatorio (2025). En Colombia, una brecha entre renovación deseada y efectiva, y el fraude en el SOAT que se compra en línea. En México, la venta telefónica con cargo a tarjeta.
- **De las plataformas (Mercado Pago, OXXO, Nequi, Falabella) no hay resultados públicos:** ni pólizas por país, ni renovación, ni retención. Solo anuncios de producto y precio.
- **Lo más útil para tus hipótesis:** Colombia dice que la gente **quiere renovar más de lo que renueva** (70,2% frente a 39,1%), y Argentina cambió por ley qué tan fácil es **irse**, lo que cambia qué significa medir fidelidad.

### 11.2 Casos por país

Mismo esquema que §3.1, resumido. **Nivel** = encuesta oficial · regulación · caso de negocio · observacional. "Mecanismo" es inferencia mía salvo que se indique. Sin resultado medido = sin cifra pública de pólizas, renovación o retención.

**México**

| Caso | Qué digitalizó o diseñó | Intervención | Mecanismo (inferencia) | Resultado y quién reporta | Nivel · fuente |
|---|---|---|---|---|---|
| Mercado Pago con Cardif y con Chubb | Venta embebida en la billetera | Seguro contra robo de **$41 al mes** desde la app; seguro para pymes desde **$55 al mes** (oct-2026) | Baja fricción y precio mínimo en el sitio donde ya paga | **Sin resultados.** Una cifra de 83% de negocios sin seguro es de una fuente secundaria | Caso de negocio · PR · F-1052 |
| OXXO con GNP | Venta en un punto de pago cotidiano | Microseguros de cáncer y primer infarto a **$99 y $149**, tarjeta que se activa por llamada | Compra donde ya se paga en efectivo | **Sin resultados**; fecha del anuncio no clara | Caso de negocio · prensa · F-1053 |
| Compartamos con Mapfre | Distribución por una institución de microfinanzas | Vida incluida en los créditos para mujeres y cobertura voluntaria adicional; la aseguradora se queda con la prima y paga la distribución | Confianza en la institución que ya presta; producto ligado al crédito | Más de **2 millones de asegurados** y ~40% del microseguro de vida (2011, informe del propio banco); sin datos de renovación | Caso de negocio · PR + estudio de Milliman · F-1055 |
| Venta telefónica con cargo a tarjeta | Venta por llamada | Seguros que se cobran a la tarjeta de crédito | Fricción de salida: cuesta cancelar (inferencia) | Condusef advierte contra comprar seguros por teléfono y dice que cancelar por teléfono **no se ha logrado**; las quejas de aseguradoras son por **negativa de pago, cancelaciones sin respuesta y demoras** | Regulador · prensa sin fecha · F-1054 |
| Guros | Seguro de auto digital | Insurtech levantó US$5,8 M; 7 de cada 10 autos sin seguro (AMIS, vía nota) | — | **Sin resultados** | Caso de negocio · prensa · F-1056 |

**Colombia**

| Caso | Qué digitalizó o diseñó | Intervención | Mecanismo (inferencia) | Resultado y quién reporta | Nivel · fuente |
|---|---|---|---|---|---|
| Primer estudio de demanda de seguros (Superfinanciera, Banca de las Oportunidades y Fasecolda) | No es digital: mide demanda de hogares | Encuesta nacional | **Brecha entre intención y conducta** | **Renovación efectiva 39,1%; deseada 70,2%**; 90,3% de los hogares tiene algún esquema de protección, pero solo 30,3% obtuvo un seguro de forma voluntaria; 86,8% de los hogares con servicios adicionales no los usa | Encuesta oficial · F-1045 |
| SOAT que se compra en línea | Venta digital de un seguro obligatorio | Compra por web y WhatsApp; el precio está regulado | Confianza **en el canal** y precio como señal (si hay "descuento", es estafa) | **2.870 reportes de posible fraude** (2022-2025); Fasecolda: **5.267 casos en 2023** (4.742 en 2022); en oct-2026 un tribunal ordenó a la Superfinanciera un plan de canales digitales seguros en seis meses; AXA Colpatria vende el SOAT por una cuenta verificada de WhatsApp | Litigio y regulación · prensa · F-1047 |
| Interacciones digitales | Atención y servicio | Respuestas inmediatas | — | Las interacciones digitales entre aseguradoras y clientes crecieron **más de 30% en dos años** (Fasecolda, vía prensa); producción del 1T 2026 de $14,8 billones (+4,5%) | Gremio · prensa · F-1048 |
| Seguro agropecuario paramétrico | Pago por índice | Seguro con cofinanciación nacional | Pago rápido y verificable | El ramo pagó más de **$81.000 millones en 2024** a más de **98.000 productores**; penetración de **~5% del área cultivada** | Gremio · prensa · F-1046 |

**Chile**

| Caso | Qué digitalizó o diseñó | Intervención | Mecanismo (inferencia) | Resultado y quién reporta | Nivel · fuente |
|---|---|---|---|---|---|
| Licitación de seguros ligados a créditos hipotecarios (Ley 20.552, 2012) | No es digital: rediseña quién compra | El **banco licita** el seguro de desgravamen e incendio cada año entre aseguradoras, en vez de imponer una a cada cliente | La decisión pasa del individuo a un comprador institucional que compara precios | En las 37 licitaciones de jul-dic 2012, el precio bajó **59,53% en promedio** (según la SVS de entonces; cifra de segunda mano); la CMF califica el balance de positivo; en 2021 se prohibió exigir corredor en las bases y que corredores que asesoran al banco ofrezcan | Regulación · cuasi-experimento natural, sin análisis causal formal · F-1049 |
| Ecosistema insurtech | Nuevos entrantes | 112 insurtechs (+26%) | — | Tercer ecosistema de la región; Betterfly cerró en cinco de ocho países (§3.1) | Informe patrocinado · F-1044 |
| Finanzas abiertas | Datos con consentimiento | NCG 514 (jul-2024); entrada prevista para jul-2026, con propuesta de extender a **jul-2027** | — | **No se halló calendario para aseguradoras**; fuentes discrepan en el plazo | Regulación · prensa · F-1050 |

**Argentina**

| Caso | Qué digitalizó o diseñó | Intervención | Mecanismo (inferencia) | Resultado y quién reporta | Nivel · fuente |
|---|---|---|---|---|---|
| Botón de baja obligatorio (Res. SSN 435/2025) | Venta y gestión en línea | Quien vende pólizas por canales electrónicos debe mostrar un **botón visible para pedir la baja**, en el sitio y en las apps (desde el 21-ago-2025); desde 2022 hay un Registro de Canales Digitales | **Reducir la fricción de salida** | **Sin resultados todavía** | Regulación · estudio jurídico · F-1057 |
| Inflación y suma asegurada | Actualización del valor | Algunas aseguradoras pasaron de actualizar semestralmente a hacerlo trimestral o mensual | Ilusión monetaria; el valor asegurado se queda atrás | Dilema entre subir cuotas y captar clientes; aumenta el infraseguro; **sin dato de caducidad** | Prensa · F-1058 |
| Mercado Pago | Venta embebida con servicio | Vida y accidentes con teleconsulta y reintegro de 50% en medicamentos desde **$2.822 al mes** | Servicio inmediato junto a la cobertura | 80% destaca la rapidez (autodeclarado); 11 millones de clientes con pólizas en la región (sin desglose por país) | Caso de negocio · PR · F-1051 |
| Paramétrico agrícola | Pago por índice | Pólizas para sequía de maíz y soja | Pago rápido | Pólizas **duplicadas en un año** (nota sin fecha) | Prensa · F-1059 |

### 11.3 Qué se aprende (inferencias mías)

1. **La mejor evidencia sobre cambio de conducta viene de reglas, no de apps.** Chile cambió quién decide y el precio bajó; Argentina cambió qué tan fácil es salir; Colombia mide la brecha entre lo que se quiere y lo que se hace. Ninguno es un experimento aleatorizado, pero todos tienen un antes y un después o una medición oficial.
2. **La brecha entre intención y conducta en la renovación es el dato más fuerte de la región.** Colombia: se quiere renovar 70,2% y se renueva 39,1%. Es compatible con la lectura de §9.2 (caducidad por olvido o falta de liquidez) y con la idea de que **la digitalización se mide en renovación, no en venta**. El estudio no es digital ni dice por qué.
3. **La confianza en el canal es una variable aparte (N6, §10).** El SOAT colombiano es obligatorio y de precio regulado, y aun así el canal en línea acumula miles de reportes de fraude. Digitalizar un producto con demanda segura no elimina la desconfianza en el canal.
4. **Chile y Perú tomaron caminos opuestos con el mismo producto.** Chile convirtió el seguro de desgravamen en una licitación institucional; Perú lo hizo opcional y portable (F-877). Son dos teorías distintas de dónde está el fallo: en quién compra o en que sea obligatorio. No se halló comparación de resultados entre ambos.
5. **Facilitar la salida cambia el significado de "fidelidad".** Con botón de baja (Argentina) la retención que queda es más informativa que con un seguro difícil de cancelar (México por teléfono, F-1054). Para las definiciones de fidelidad de §5b, conviene registrar si la salida es fácil o difícil en cada canal.
6. **Lo embebido en la región tiene anuncios, no resultados.** Mercado Pago, OXXO y las demás no publican pólizas, renovación ni siniestros por país; solo hay una cifra regional de Mercado Libre.

### 11.4 Qué no se halló, por país

| Pregunta | México | Colombia | Chile | Argentina |
|---|---|---|---|---|
| Participación del canal digital en las primas | No hallado | No hallado (solo interacciones, +30%) | No hallado | No hallado (bancos >40% de las ventas, 2023, dato de una empresa) |
| Renovación o retención de un producto embebido | No hallado | No hallado | No hallado | No hallado |
| Experimento de campo en seguros | No hallado | No hallado | No hallado | No hallado |
| Dato oficial de seguros digitales | No hallado | Estudio de demanda; interacciones | Licitación (no digital) | Resoluciones de la SSN |

La mezcla de canales de la región cambió poco: agentes y corredores aportan 60-65% de las primas (McKinsey 2025, vía F-1057; coincide con F-375).

### 11.5 Límites y pendientes

**Límites.** Todo es resumen de búsqueda o prensa; muchas notas no traen fecha (OXXO, Condusef, paramétrico en Argentina); las cifras de la SVS (59,53%) y de Colombia (renovación) vienen de resultados sin abrir el documento original; el informe de la ONU sobre insurtech en América Latina y el Caribe (nov-2025) no se leyó.

**Pendientes (en orden de valor).**

1. Estadísticas oficiales por canal y persistencia: AMIS y CNSF (México), Fasecolda y Superfinanciera (Colombia), CMF (Chile) y SSN (Argentina).
2. Abrir el estudio de demanda de Colombia: fecha, método y si distingue el canal digital.
3. Abrir los documentos de la CMF y de la UC sobre la licitación chilena para verificar el efecto en precios y comisiones.
4. Abrir el brief de Milliman sobre microseguro de vida en México (resultados sobre gastos funerarios y renovación).
5. Seguir el efecto de la Res. SSN 435/2025 sobre las bajas.
6. Buscar casos de seguro embebido con resultado (Nequi, Falabella, Mach, Ualá) en informes anuales o comunicados de resultados.

---

## 12. Adenda v1.5 (2026-10-27): fuentes aportadas por el usuario, con clasificación y confiabilidad

*Origen: la persona usuaria compartió nueve enlaces y pidió clasificarlos (`/trinidad`), revisar que fueran confiables y ubicarlos donde correspondan.*

### 12.1 Respuesta corta

- **Ningún enlace se pudo abrir directamente:** la red de este entorno bloquea esos sitios (error 403 o de DNS) y no se intentó evadirlo. Cada fuente se leyó por **búsqueda dirigida a su sitio**, es decir, por resumen. El PDF de Deloitte se leyó completo después, con la copia que subió la persona usuaria (§12.5). Dos piezas (el PDF de Pérez-Llorca y el número 495 de la revista de la Universidad de Lima) **siguen sin leerse**; de ellas solo se conoce lo que dicen sus fichas.
- **Confiables como evidencia hay pocas.** Con reserva por ser parte interesada: el informe climático de MAPFRE Economics (F-1069). Con rigor académico y no de seguros: el artículo de la Universidad de Lima (F-1066). Los demás son consultoras, bufetes, corredoras o aseguradoras que describen su mercado (🟡 C), prensa o consultoras que se describen a sí mismas (🟠 D) y dos que **conviene descartar** como evidencia (🔴 E).
- **Dos de las nueve se repiten a otras:** el reportaje de LexLatin resume el boletín de Pérez-Llorca, y la nota de MAPFRE repite el informe de Digital Insurance LATAM que ya estaba en el ledger (F-1003, F-1044). Cuentan como **una** fuente cada par, no como dos.
- **Lo más útil que dejaron:** que el proyecto de reglamento de finanzas abiertas de la SBS ya está en consulta pública (F-1064), y que el financiamiento insurtech de la región se concentra en vida y salud (F-1068).

### 12.2 Clasificación

Pista: 🔬 empírica/teórica · 📱 social · 💼 negocio · ⚖️ regulación. Rigor: 🟢 A · 🔵 B · 🟡 C · 🟠 D · 🔴 E.

| # | Fuente (enlace dado) | Qué es | Pista | Rigor | ¿Se leyó? | Qué aporta | Dónde se usa |
|---|---|---|---|---|---|---|---|
| 1 | Deloitte, folleto *Seguros Latinoamérica* (2025) | Consultora | 💼 | 🟡 C | **Sí, completo** (PDF subido por la persona usuaria) | Cifras de penetración, de participación en primas y de canales de México; datos de Chile; **pero casi todo es de segunda mano y no mide retención** (ver §12.5) | §12.5 (F-1072; F-1061 queda como las páginas hermanas) |
| 2 | Pérez-Llorca, *Actualidad Iberoamericana de Seguros* 3T 2026 | Bufete, boletín | ⚖️ | 🟡 C | **PDF no**; solo la ficha | Cubre Colombia, España, México, Portugal y, **desde esta edición, Perú** (13-oct-2026) | Foresight §11 (F-1062) |
| 3 | LexLatin, reportaje de seguros, finanzas abiertas e IA | Medio jurídico (eco de la anterior) | ⚖️ | 🟠 D | Por resumen | La SBS contempla aseguradoras en finanzas abiertas; **AMIS: 15% a 20% de las aseguradoras mexicanas usa IA**; México sin ley general de IA; oportunidades en paramétricos, ciber y billeteras | Foresight §11 (F-1063) |
| 4 | Gallagher Perú, 5 tendencias del mercado en LATAM 2026 | Corredora y reaseguradora | 💼 | 🟡 C | Por resumen | Mercado blando, regulación, cambio, clima; **insurtech abre nichos como Perú** (una frase); 95% del financiamiento insurtech del 1T 2026 fue a IA. Casi todo es de líneas comerciales | Foresight §11 (F-1065) |
| 5 | Universidad de Lima, revista *Desafíos* (número 495) | Revista académica | 🔬 | 🔵 B | **El número no**; se halló un artículo de otro número | Más uso de tecnología sube la probabilidad de inclusión financiera; la informalidad la baja. Autoría con vínculos con bancos y retail | §10 N1 y N3 (F-1066) |
| 6 | BeWay, etiqueta *seguros* | Consultora conductual | 🔬 práctica | 🟠 D | Etiqueta **no**; solo un artículo hallado | Caso con 'aceptación de más de 30%' autodeclarado y sin línea base; cumbre con casos de Coppel y BBVA, sin detalle de seguros | `economia-conductual-seguros-literatura` §7 (F-1067) |
| 7 | MAPFRE, financiación insurtech 1S 2026 | Aseguradora patrocinadora (eco de F-1003 y F-1044) | 💼 | 🟡 C | Por resumen | **Life & Care: 26% de las insurtechs y 76% del financiamiento**; 576 insurtechs (+14%); Brasil 217, México 150, Chile 112, Argentina 110; MAPFRE compra 38,9% de Tuio | §11 y foresight §11 (F-1068) |
| 8 | Research and Markets, *Global Insurtech Market 2020 to 2025* | Informe de pago de 2020 | 💼 | 🔴 E | Por resumen de Business Wire | Pronóstico de US$10,14 mil M a 2025 con TCAC de 10,8%; otras casas dan 36% a 43% | **Se descarta** (F-1070) |
| 9 | MPM Software, tendencias 2026 | Proveedor de software, blog | 💼 | 🔴 E | Por resumen | Seis tendencias; 'seguro invisible' en 2027; reducción de 40% del costo de emisión (cifra propia). La brecha de 81% coincide con MAPFRE Economics | **No se usa como evidencia** (F-1071) |
| 10 | Artículo subido después: Enríquez, Alvarado y Romero, *Aplicación de la economía conductual en el mercado de los seguros* (*Desafíos* n.º 8, 2025) | Revista universitaria | 🔬 | 🟡 C | **Sí, completo** (documento subido por la persona usuaria) | Revisión narrativa con series de la SBS; **varias citas con cifras no coinciden con sus fuentes**; revela experimentos agrícolas en el Perú | `economia-conductual-seguros-literatura` §8 (F-1073 a F-1078) |

Además, al verificar los datos se sumaron dos fuentes que no estaban en la lista: el **proyecto de reglamento de finanzas abiertas de la SBS** (Res. 02433-2026 y 02519-2026, F-1064, 🔵 B) y el **informe climático de MAPFRE Economics** (F-1069, 🔵 B).

### 12.3 Qué cambia en los nodes

1. **Finanzas abiertas en Perú ya está en consulta pública.** La SBS puso en consulta el proyecto del Reglamento General el 2-oct-2026 (18 días de plazo) y después los Títulos V a VII (F-1064). LexLatin, que cita el boletín de un bufete, dice que contempla a las aseguradoras; **el texto no se abrió, así que el alcance a seguros sigue sin verificar.** Esto actualiza el cronograma de F-965 (reglamento general a inicios de 2027) y la pendiente de §8.4.
2. **El financiamiento insurtech se concentra en vida y salud.** Con 26% de las empresas, Life & Care recibió 76% del dinero del 1S 2026; movilidad, con 211 empresas, 9% (F-1068). Es consistente con la lectura de §8.3 de que vida y salud lideran, pero es un informe patrocinado por una aseguradora.
3. **Brecha de protección frente a catástrofes de 81,0% en LATAM** (promedio 2015-2024; MAPFRE Economics con datos de Swiss Re, F-1069). Sirve a la pregunta de asegurabilidad del foresight.
4. **IA en aseguradoras mexicanas: 15% a 20% (AMIS, vía LexLatin).** Dato de gremio de segunda mano; no verificado.
5. **Parte interesada:** MAPFRE patrocina el informe sobre el ecosistema insurtech, produce el estudio climático y compra una parte de Tuio (que aparece en el foresight como una de las aseguradoras que cotiza en ChatGPT, F-981). Sus cifras se leen como del sector que describe.

### 12.4 Límites y pendientes

**Límites.** Todo se leyó por resumen de búsqueda, salvo el PDF de Deloitte (§12.5). El PDF de Pérez-Llorca y el número 495 de la revista no se abrieron. De BeWay no se abrió la etiqueta que se indicó. Las fechas de varias páginas de MPM y de Gallagher no son consistentes.

**Pendientes.**

1. Si la persona usuaria sube también el PDF de Pérez-Llorca (es público), se puede leer a fondo y reclasificar; el de Deloitte ya se leyó (§12.5).
2. **Probablemente resuelto:** el artículo que la persona usuaria subió después es del n.º 8 de *Desafíos* (jul-dic 2025) y parece ser el que buscaba; falta confirmar que ese número sea el 495 del enlace.
3. Abrir el texto del proyecto de finanzas abiertas de la SBS en `sbs.gob.pe` y buscar la mención de seguros.
4. Verificar con AMIS el dato de 15% a 20% de aseguradoras que usan IA.

### 12.5 Lo que dice el folleto de Deloitte (leído completo) y qué tan firme es

**Qué es.** Un folleto de 11 páginas de Monitor Deloitte México (Deloitte S-LATAM, 2025). Es un **punto de vista**, no una investigación: no declara método, muestra ni fechas de campo. Argumenta que la digitalización es una necesidad estratégica en cuatro frentes: oferta (del seguro a la medida al embebido), canales, modelos de negocio y eficiencia operativa.

**Conclusión sobre su solidez.** Sirve como **mapa de lo que la industria dice**, no como evidencia de efecto. Casi todo está sostenido en 16 referencias secundarias: prensa del sector, notas de prensa de empresas, blogs de proveedores, y solo tres fuentes institucionales (OCDE, FIDES y la CNSF vía Hacienda de México).

**Datos útiles, con su fuente real (F-1072):**

| Dato | Fuente real que cita | Cómo leerlo |
|---|---|---|
| Penetración por país (% del PIB): Chile 4,5; Brasil 3,3; Colombia 3,3; Uruguay 2,9; México 2,7; **Perú 2,6**; Ecuador 2,4; Argentina 2,0; promedio OCDE 8,8 | OCDE (2024) | Institucional. **Perú aparece con 2,6%, mientras la SBS da 2,06%**: definiciones distintas, no se concilian aquí |
| Participación en primas de la región: Brasil 41,93%; México 22,96%; Argentina 10,43%; Chile 7,86%; Colombia 6%; **Perú 4,8%** | FIDES (2023) | Institucional. El texto dice que los cinco mayores suman 85%, y las cifras de la gráfica suman ~89% |
| México, canales: agentes ~50% de las primas, bancaseguros 17%, *retailers* 18%, venta directa 10% | CNSF vía Hacienda (2024) | Institucional. **No confirma el 60-65% de agentes y corredores de McKinsey para la región (F-375)**: son definiciones y alcances distintos |
| Primas de la región +17,1% en 2023, hasta US$203.354 M | Latino Insurance (prensa del sector) | Secundaria |
| Penetración de ~3% frente a 7% mundial | Un blog de un proveedor (MPM) | **Débil: el 7% mundial no viene de Swiss Re ni de la OCDE sino de un blog comercial** (el mismo que se descartó en F-1071) |
| Más de 500 insurtechs; tipo más frecuente (31% en la gráfica): propiedad, accidentes y corredor multilínea | Digital Insurance LATAM (2025) | Informe patrocinado; ya está en F-1003 y F-1044 |
| Chile: 92% de las aseguradoras trabaja con al menos dos insurtechs; digitalización total de procesos de 18% (+50% en 2024); cerca de un tercio con más de 80% de flujos parcialmente digitalizados | InsurteChile (2024) | Gremio de insurtechs y aseguradoras chilenas: parte interesada. Mide procesos, no clientes |
| Embebido: 4,5 M de clientes activos y más de US$200 M en primas, comisiones y otros ingresos | Nota de prensa de MetLife (no nombrada en el texto) | **Autodeclarado**, mezcla primas con comisiones |
| 57% de las aseguradoras del mundo usa IA para detectar fraude | Latino Insurance (2025) | Secundaria |

**Lo que afirma sin respaldo (importante para tus hipótesis):**
- **"Pagar un siniestro de auto al instante hace al cliente más propenso a renovar o ampliar la póliza."** No trae cita ni medición. Es justo la hipótesis de la promesa y la prueba (P1 del foresight, FH1) que sigue sin probarse.
- **"La IA predice la propensión a cancelar de cada cliente y activa campañas de retención."** Sin cita ni resultados. Es una práctica declarada, no un efecto medido.
- **La conclusión dice que los casos muestran 'mejora en la retención de clientes'.** En el documento no hay ninguna medición de retención; los casos son anónimos o de notas de prensa.
- **Un caso mexicano de vida personalizada por app y WhatsApp**, sin nombre de empresa y con un blog como referencia (Truora). No se puede usar como caso.

**Lo que no está en el folleto:** nada específico de Perú más allá de su penetración y participación en primas y de que la SBS automatiza la captura de datos; nada de renovación, caducidad, activación ni de comportamiento del cliente. **No contesta ninguna de las hipótesis de §2 ni de §10.**

**Dónde se aprovecha:** como referencia de contexto (§8.3 y §11), para verificar la participación de agentes en México (F-1072 frente a F-375) y como lista de afirmaciones de la industria que conviene probar con dato propio (`hipotesis-digitalizacion-seguros-evidencia-publica`).

## 13. Adenda v1.6 (2026-10-27): para qué digitalizan las aseguradoras y qué buscan

*Origen: la persona usuaria preguntó **para qué digitalizan y qué se busca al hacerlo**, antes de entrar a la estrategia. Partió de un documento interno (no versionado: repositorio público); de él solo se usaron las **fuentes públicas de referencia**, que se verificaron aquí. `/trinidad` con pista empírica/teórica y pista de negocio; **la pista social no se corrió.***

### 13.1 Respuesta corta

**Las aseguradoras digitalizan para siete cosas, que no pesan lo mismo ni se miden igual:** vender más, gastar menos en servir y operar, pagar menos siniestros, retener y profundizar la relación, dar al cliente lo que pide, crear productos y mercados nuevos, y defenderse de nuevos competidores. La literatura académica las agrupa en cuatro tareas: mejorar la experiencia, simplificar procesos, lanzar productos nuevos y prepararse para competidores de otras industrias (Eling y Lehmann, 2018; F-923).

Lo que sostiene el resto de la sección:

1. **Lo que las empresas declaran** es eficiencia y experiencia del cliente: en una encuesta a 43 ejecutivos, 60% marcó eficiencia operativa y 58% experiencia del cliente (F-1085); en otra, 59% espera de la IA, sobre todo, eficiencia (F-1086). Son encuestas de proveedores.
2. **Lo que miden y publican** es volumen, velocidad, costo y uso (ventas digitales, tiempo de respuesta, usuarios activos). **Casi nunca publican el efecto sobre el resultado técnico** (siniestralidad y gastos).
3. **Lo que está probado con causalidad independiente es muy poco:** un experimento aleatorizado de seguro por uso que cambió la conducta de manejo (F-442). El resto son correlaciones con selección (F-1099, F-1101, F-1097) o cifras de las propias empresas (F-1092, F-1093).
4. **La tensión de fondo (inferencia mía):** en seguros de propiedad y accidentes de EE.UU., los siniestros pesan casi tres veces lo que los gastos (71,0% frente a 25,2% de la prima en 2024; F-1091), pero la digitalización se ha usado más en venta y servicio. El siniestro es el bolsillo grande y más difícil de mover; los gastos son el chico y más controlable. La literatura pública no dice cuál rinde más.
5. **No hay evidencia independiente de que "más uso" (MAU, tráfico) mejore el resultado.** En EE.UU., la compra digital sube (47% de las pólizas nuevas de auto y hogar) mientras la satisfacción con esa compra baja (523, −12 puntos) y solo 11% usa un chatbot (F-1094).

### 13.2 Los siete objetivos: qué buscan, qué hay y qué tan sólido es

| # | Objetivo | Qué buscan | Qué se encontró | Solidez |
|---|---|---|---|---|
| 1 | **Vender más y mejor** | Captar en digital, sobre todo en productos simples; vender por comparador, billetera o plataforma | 47% de las pólizas nuevas de auto y hogar en EE.UU. ya se compran en digital (F-1094); en Perú, ~90% de los SOAT se emiten digitales, un seguro obligatorio y de precio regulado (F-884). **No se halló que lo digital haya movido la penetración agregada** (§3.2) | 🟡 adopción medida; efecto total no |
| 2 | **Gastar menos en servir y operar** | Autogestión, automatización, menos llamadas, procesos más cortos | Los autoservicios fallan y terminan en llamada (cifra de 31% en auto en EE.UU. no confirmada, F-1095); solo 11% usa un chatbot (F-1094); ventaja de 6 puntos del ratio combinado en los sindicatos más avanzados de Lloyd's, con selección (F-1101); proveedores prometen −40% de costo de emisión (F-1071) | 🟠 correlación o cifra de proveedor |
| 3 | **Pagar menos siniestros** | Prevención, detección de fraude, selección y precio más fino, control del siniestro | **Un RCT:** el seguro por uso cambia la conducta de manejo (F-442). Sensores de fuga con cifras de proveedores (F-1001). 57% de las aseguradoras del mundo usa IA contra el fraude (F-1072, de segunda mano). Discovery: 30% menos siniestros entre conductores 'avanzados y comprometidos', con selección (F-1093) | 🟢 un RCT; 🟠 el resto |
| 4 | **Retener y profundizar** | Más productos por cliente, menos caducidad, relación continua | Ping An: 2,94 contratos por cliente y 99% de retención entre quienes tienen tres o más categorías (F-1092): **selección**, quien compra mucho ya era leal. Agrupar auto y hogar: retención de 95% frente a 85% (F-1018). Sin prueba causal de que la app retenga (§0 de `hipotesis-digitalizacion-seguros-evidencia-publica`) | 🟠 correlación |
| 5 | **Dar lo que el cliente pide** | Experiencia sin fricción, relación digital directa, atención asistida | 59% de los menores de 40 quiere relación digital directa y solo 31% de las aseguradoras la ofrece; 67% quiere digital con un asesor dedicado y 16% lo recibe (F-1096). Interés en prevención muy alto en Brasil (97%) (F-1095). **La satisfacción con lo digital cae** (F-1094, F-1009) | 🟡 encuestas |
| 6 | **Crear productos y mercados nuevos** | Embebido, paramétrico, microseguro, inclusión | Estimaciones de mercado que no concilian (F-998, F-999); casos de escala con cifras propias (GCash, Grab; §3.1); RCT de demanda en agricultura (F-847, F-849) | 🟠 PR; 🟢 solo los RCT agrícolas |
| 7 | **Defenderse y habilitar** | Modelo operativo digital como requisito para competir; datos para la IA | Fitch: será un requisito para competir en LATAM (Fitch vía prensa); 74% lo ve como prioridad (F-1085); 99,1% del financiamiento insurtech del 2T 2026 fue a IA (F-901) | 🟡 opinión de analistas |

### 13.3 Declarado, medido y probado

| Objetivo | Lo que declaran | Lo que miden | ¿Está probado el efecto? |
|---|---|---|---|
| Vender más | Inclusión y penetración | Pólizas y primas digitales | No: no se mide el efecto en el total |
| Gastar menos | Eficiencia | Tiempo, costo por trámite, uso de autoservicio | No de forma independiente; sí cifras de empresas |
| Pagar menos siniestros | Prevención, fraude | Cuando se mide, siniestros de quienes participan | **Parcial:** un RCT de seguro por uso; el resto, con selección |
| Retener | Fidelidad | Caducidad y contratos por cliente de quienes usan la app | No: la selección no se separa |
| Dar lo pedido | Experiencia | Satisfacción y NPS | Correlación; la satisfacción digital baja |
| Productos nuevos | Penetración y acceso | Pólizas vendidas | Solo en RCT agrícolas |
| Defensa | Supervivencia | Inversión y lanzamientos | No aplica |

**Lectura (inferencia mía):** hay una brecha entre el 'para qué' declarado y lo que se mide. Casi todo lo que se mide es de **actividad** (uso, velocidad, volumen) y casi nada es de **resultado** (siniestralidad, ratio combinado, retención causal). Que no se mida no prueba que no funcione, pero **impide saber qué objetivo rinde más**.

### 13.4 'Se asocia con más creación de valor': qué significa, cómo se mide y qué no prueba

**Conclusión.** Esa frase describe una **correlación entre el nivel de digitalización de una aseguradora y su rentabilidad relativa**, no una prueba de que digitalizar cause mayor rentabilidad. Hay dos estudios que la sostienen y ambos tienen el mismo límite: las aseguradoras que ya ganan más pueden invertir antes y más en lo digital.

**Estudio 1: ACORD, Digital Maturity Study (F-1099).**

- **Quién:** ACORD, un gremio de estándares de datos del sector, que **vende** el estudio. El PDF que circula con el sello de Swiss Re es la edición de 2022 (julio de 2023). Las de 2025 y 2026 evalúan **210** aseguradoras de vida, propiedad y accidentes y reaseguro.
- **Cómo mide la madurez digital:** ocho capacidades (plataformas de clientes, analítica de datos, infraestructura, operaciones, automatización, inversión, modelos de negocio y cultura), evaluadas **en relación con las demás aseguradoras**. Las ordena en cinco niveles.
- **Qué es el 'valor':** un **beneficio relativo indexado**: la rentabilidad de cada aseguradora frente a la del promedio del estudio, con el promedio fijado cerca de 100. No es un monto ni un ratio combinado.
- **Qué halló (edición 2026):** solo el nivel superior (~7%, 'competidores digitales') superó el promedio, con **135,7 frente a 102,5**; los otros cuatro niveles quedaron por debajo del promedio. En ediciones anteriores los dos niveles superiores solían superarlo. Un resumen de 2025 añade que solo una cuarta parte había digitalizado de verdad la cadena de valor.
- **Qué hacen distinto los líderes (según el estudio):** parten del objetivo de negocio y planifican a más largo plazo que el siguiente punto de solución.

**Estudio 2: WTW sobre Lloyd's (F-1101).** 49 sindicatos (~85% del mercado) se clasificaron **ellos mismos** por su avance digital. El ratio combinado operativo agregado de 2022 fue **89%** en el grupo más avanzado, **93%** en el intermedio y **95%** en el menos avanzado: una ventaja de **6 puntos** del ratio combinado, no de 6%. Es un solo año y una sola plaza (el mercado de Londres, de seguros comerciales y especializados).

**Un tercer dato, de metas y no de resultados (F-1100):** Swiss Re Institute reporta que las aseguradoras se proponen mejorar la siniestralidad entre **3 y 8 puntos porcentuales** y ahorrar **10% a 20%** en otras partes de la cadena con la transformación digital. Son lo que **esperan**, no lo que lograron.

**Por qué no prueba que lo digital cause el valor:**

1. **Causalidad inversa.** En un estudio de 23 aseguradoras sauditas, la rentabilidad y la solvencia **predicen** la adopción de insurtech (F-1088). Las que ganan más pueden pagar más tecnología.
2. **Medición relativa.** Si el índice es relativo a los pares, el promedio siempre es 100: que unas suban implica que otras bajen, sin que cambie el resultado agregado del sector.
3. **Autoclasificación y métrica propia.** WTW clasificó a los sindicatos por su autoevaluación; ACORD usa su índice y su métrica de beneficio, que **no son auditables desde afuera**.
4. **Otros factores.** Las aseguradoras mejor gestionadas pueden tener a la vez mejor tecnología y mejor suscripción, sin que lo uno cause lo otro.
5. **Quién publica.** ACORD vende el estudio, WTW vende asesoría de transformación y Swiss Re es reaseguradora de las que digitalizan: todos tienen interés en que el resultado sea positivo.
6. **Plazo y sectores.** Un año en Lloyd's y comparaciones entre grandes aseguradoras no dicen nada de aseguradoras medianas de mercados emergentes.

**Qué sí dice (inferencia mía):** las aseguradoras más digitalizadas **no parecen ir peor**, y el nivel superior sí se separa del promedio. Es una señal para investigar con diseños que separen la selección (emparejamiento y diferencias en diferencias, §6 de `hipotesis-digitalizacion-seguros-evidencia-publica`), no una cifra para prometer.

**Otros hallazgos sobre el efecto en el resultado:**

- Un panel dinámico ucraniano sobre digitalización y desempeño financiero existe, pero **solo se vio su resumen** (F-1088).
- La literatura académica sobre insurtech se concentra en la tecnología (IA y blockchain) más que en el efecto económico (F-1090) y ofrece modelos de cómo se crea valor sin medirlo (F-1089).
- Las agencias más digitales crecen 70% más rápido (EE.UU., encuesta patrocinada por aseguradoras de 2022), pero con selección (F-1097).
- **Prevención:** un programa digital de prevención de diabetes redujo el gasto de salud US$1.169 por participante en el primer año frente a un grupo emparejado, pero **ya no fue significativo al segundo año** y es observacional y ligado a un proveedor (F-1108). No se halló un experimento aleatorizado de una aseguradora con costos de siniestros como resultado.

### 13.5 Qué busca el cliente frente a lo que buscan las aseguradoras

| Lo que busca la aseguradora | Lo que dice buscar el cliente | Distancia |
|---|---|---|
| Eficiencia en servir | Digital para lo simple y humano para lo complejo (§12; F-1096) | El autoservicio que falla se vuelve llamada |
| Vender en digital | Poder comparar precios y coberturas (F-1094) | Hoy sube la compra y baja la satisfacción |
| Pagar menos siniestros | Servicios de prevención: interés alto, sobre todo en Brasil (F-1095) | El uso actual es mucho menor que el interés (cifra no confirmada) |
| Retener | Relación digital directa, con asesor dedicado (F-1096) | 59% frente a 31%; 67% frente a 16% |

**Cautela:** son encuestas de mercados maduros (EE.UU., Europa, 14 a 18 países) de consultoras. **No hay medición equivalente para Perú.**

### 13.6 El benchmark público verificado

Las fuentes públicas citadas en el documento de la persona usuaria se revisaron en esta sesión (por resumen). ✔ confirmado · ✗ no confirmado.

| Dato citado | Fuente | Verificación |
|---|---|---|
| 47% de las pólizas nuevas de auto y hogar se compran en digital; satisfacción de 523 (−12); 11% usó un chatbot; 11.553 evaluaciones | J.D. Power 2026 | ✔ (la caída de 12 puntos de segunda mano) |
| Con herramientas de comparación, la compra pasa de 21% a 39% | J.D. Power 2026 | ✗ la prensa habla de **consideración** que casi se duplica; no se confirmó la cifra de compra |
| Encuesta de 28.765 consumidores en 14 países; interés en prevención | Bain 2023 | ✔ (Brasil 97%, Japón 81%) |
| Interés de 60% a 80% y uso actual de 2% a 4%; 31% de fallas del autoservicio | Bain 2023 | ✗ no se confirmaron |
| 59% frente a 31%; muestra de 6.176 menores de 40 años | Capgemini y LIMRA | ✔ (además 67% frente a 16%) |
| 77% espera recomendaciones basadas en datos frente a 16% | Capgemini y LIMRA | ✗ no se confirmó el 77% |
| Agencias con mayor madurez digital crecen 70% más rápido | Agent for the Future | ✔ pero es el estudio de **2022**, de agentes de EE.UU. patrocinado por aseguradoras (el de 2021 daba 60%) |
| Discovery: 30% menos siniestros de auto entre los mejor calificados | Shared Value Africa | ✔ 'avanzados y comprometidos': 30% menos frecuencia y 34% menos severidad, con selección |
| Discovery: hospitalizaciones 10% menos, estancias 25% más cortas, siniestros de vida 45% menores, caídas de póliza 67% menores | Shared Value Africa | ✗ no se vieron esas cifras |
| Ping An: 251 millones de clientes y 2,94 contratos por cliente | Resultados de 2025 | ✔ |
| Ping An: prima de primer año 1,5 veces mayor en clientes de servicios de salud | Resultados de 2025 | ✗ no se halló (sí 99% de retención en 3 o más categorías y 1,7 veces más contratos a los 5 años) |
| McKinsey 2020 (mercado alemán): 84% usa pasos digitales y 55% no se imaginaba comprar en línea | McKinsey | ✗ no se verificó en esta sesión |

**Qué implica:** las cifras de J.D. Power, Bain, Capgemini y Ping An son verificables en lo central, pero **varias de las más llamativas no se pudieron confirmar**. Conviene citar solo lo ✔ y abrir la fuente de lo ✗ antes de usarlo en un entregable.

### 13.7 Qué falta para responder del todo

1. **Dimensionar los dos bolsillos en Perú.** Con las estadísticas de la SBS, el peso de los gastos y de los siniestros por ramo y por compañía. Hoy solo hay el dato de EE.UU. (F-1091). Es la pieza que permite decir cuánto vale cada objetivo.
2. **Un estudio que mida el efecto de lo digital en el ratio combinado**, con diseño que separe selección (emparejamiento, diferencias en diferencias; §6 de `hipotesis-digitalizacion-seguros-evidencia-publica`).
3. **Leer el panel dinámico ucraniano** y buscar paneles en *Journal of Risk and Insurance* y *Geneva Papers* (F-1088).
4. **Medir lo que quiere el cliente peruano** (prevención, relación directa), no extrapolarlo de encuestas globales.
5. **La pista social** no se corrió: falta ver qué se discute públicamente sobre para qué digitalizan las aseguradoras y qué reclaman los clientes.

### 13.8 Límites

Todo se leyó por resumen de búsqueda. Las encuestas son de proveedores o consultoras. Los datos de costos son de EE.UU. y de propiedad y accidentes. El documento interno de la persona usuaria **no se copió ni se resume aquí** (repositorio público); solo se usó su lista de fuentes públicas.

---

---

## Conexiones

- [[seguros-comportamiento-mundo-peru|Comportamiento, percepción y valoración frente a seguros (Mundo vs. Perú)]] —
  base de penetración, confianza y tenencia; este node usa sus cifras y marca una ambigüedad en la participación
  de corredores (F-375 frente a F-887).
- [[futuro-asesores-seguros-venta-digital|¿Desaparecerán los asesores de seguros?]] — mismo patrón híbrido a nivel
  global; aquí se extiende a mercados emergentes y a conducta.
- [[venta-vida-digital-hibrida-latam|Venta de vida digital vs. híbrida en LATAM]] — Azos, Betterfly y bancaseguros
  de Brasil; este node añade evidencia causal de demanda y las definiciones basales.
- [[transicion-venta-fria-a-opt-in|Transición de venta fría a opt-in]] — confianza al pedir datos; relevante para
  el consentimiento en renovación automática.
- [[behavioral-design-estado-disciplina|Estado del behavioral design]] — crisis del nudge y megaestudios; este node
  confirma que los efectos grandes en seguros vienen de rediseñar el contrato, no de empujones.
- [[lealtad-gamificacion-recompensas-retail|Gamificación, recompensas y lealtad en retail]] — por qué no apostar a
  gamificación en seguros sin prueba.
- [[fenomeno-el-nino-impacto-personas|Fenómeno El Niño: impacto en las personas]] — oportunidad paramétrica (O9).
- [[evaluacion-calidad-agentes-conversacionales-ia|Evaluación de calidad de agentes conversacionales]] — métricas
  para medir un chatbot de siniestros.
- [[modelo-personas-sinteticas|Modelo de personas sintéticas `lapuerta`]] — segmentos de la matriz (§4) se pueden
  simular con sus variables (informalidad, bancarización, acceso digital, confianza).
- [[fenomenos-psicologicos|Fenómenos psicológicos clásicos]] — estado de replicación de la aversión a la pérdida y del anclaje que usan las láminas de pago (§9.1); ahí está F-724 (mayor en mayores).
- [[economia-conductual-seguros-literatura|Economía conductual de los seguros: qué dice la literatura]] — el resto del ciclo de decisión (demanda, elección, confianza, asesoría, selección, ahorro) que aquí no se cubre.
- [[foresight-experiencia-futura-seguros-digitalizacion|Foresight: la experiencia futura de los seguros y la digitalización]] — radar de 23 señales, preguntas profundas y escenarios a 2035 (reemplaza al radar que se retiró de este node).
- [[hipotesis-digitalizacion-seguros-evidencia-publica|Hipótesis de digitalización en seguros: evidencia pública y dato interno]] — doble clic sobre fidelidad, activación, bancaseguros y recurrencia: qué se puede responder afuera y qué no.
- [[economia-plateada-seguros-peru-latam|Economía plateada y seguros en Perú y LATAM]] — personas mayores: demografía, acceso digital, oferta de rentas y salud, hipótesis SE1-SE6.
