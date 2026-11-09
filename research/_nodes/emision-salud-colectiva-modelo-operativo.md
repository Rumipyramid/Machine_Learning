# Emisión eficiente en seguros de salud colectivos — desk research para el modelo operativo To Be (RIMAC)

> **Versión:** v1.0 · **Fecha:** 2026-11-09 · **Encargo:** equipo de investigación de RIMAC que define el modelo
> operativo futuro de emisión de salud colectiva (EPS y Asistencia Médica Colectiva, AMC).
> **Fuentes:** F-847 a F-905 del ledger (`research/fuentes/codice.md`).
> **Complementa, no reemplaza:** las 20 entrevistas Jobs to be Done (12 empresas, 8 brokers). Nada de lo que sigue
> anticipa lo que necesitan los clientes peruanos.

## Cómo leer este documento

- **Método y su límite principal.** Se hicieron ~45 búsquedas en inglés, español y portugués. El proxy de red del
  entorno bloqueó la lectura directa de las páginas (pwc.com, insurancenewsnet.com, fineos.com, datos-insights.com,
  interseguro.pe, entre otras). **Todo se leyó por resumen de búsqueda**, no por texto completo. Por eso varias cifras
  quedan marcadas "a verificar" y ninguna norma peruana se citó por artículo leído.
- **Nivel de evidencia (escala del encargo).** **A** medición independiente, auditada o regulatoria. **B** dato de la
  propia empresa en documento público con cifras. **C** estimación de consultora o analista. **D** marketing sin
  método. En el ledger, la misma fuente lleva además la rúbrica A-E de `cronista`; no son la misma escala.
- **Perspectiva de eficiencia.** **A** aseguradora · **E** empresa cliente · **B** broker. Cuando una práctica solo
  tiene evidencia desde A, se marca ⚠️*solo A*.
- **Tipo de afirmación.** 📊 dato observado · 🧠 inferencia del analista · ❓ hipótesis.

---

## 1. Resumen ejecutivo

1. **Nadie publica una tasa verificable de emisión sin intervención manual (STP) en colectivos.** Ni aseguradoras
   (MetLife, Unum, Sun Life, Guardian), ni consultoras, ni reguladores. Las cifras que circulan son de proveedores de
   software y casos únicos (F-860). Cualquier meta de STP para el To Be tendrá que construir su propia línea base.
   *Confianza alta (en la ausencia) · A.*
2. **El cuello de botella está en los datos del grupo, no en el acto de emitir.** Censo, altas, bajas y
   elegibilidad concentran los errores. Hay un dato regulatorio: en el lanzamiento de HealthCare.gov (EE.UU., 2013)
   ~25% de los archivos de inscripción llegaba con errores y bajó a ~10% (F-849). Una encuesta pagada por un
   proveedor reporta que 42% de los trabajadores afectados por errores en sus beneficios recibió facturas
   inexactas (F-850). La industria creó estándares de intercambio (LIMRA LDEx, 2020-2022), pero ninguna aseguradora
   los exige (F-847, F-848). *Confianza media-alta · A, E, B.*
3. **La personalización se resuelve con límites por segmento, no con un producto por cliente.** En pymes, los
   referentes venden planes estandarizados y reparten el riesgo en un fondo común: Brasil lo exige por norma para
   contratos de hasta 29 vidas (F-867); Alice vende planes PME de 1 a 29 vidas (F-868); Pacífico ofrece un plan
   pyme contratable desde una persona (F-895). En corporativos sigue habiendo negociación y tarifa por experiencia
   (F-863). No hay medición independiente de lo que se gana o pierde al estandarizar. *Confianza media · A
   (y E por simplicidad, sin medir).*
4. **La automatización de cotización avanza por umbral de tamaño del grupo.** SulAmérica pasó a cotizar en sistema,
   sin análisis técnico, los grupos de 100 a 199 vidas (2022), y su plataforma para brokers cierra contratos de
   hasta 99 vidas en minutos (F-865). Bradesco Saúde digitalizó cotización y emisión PME y espera ahorrar hasta
   6 días (F-866). Los grupos grandes y complejos siguen siendo manuales. Ningún referente publicó el resultado
   medido. *Confianza media en la práctica, baja en el resultado · A, B.*
5. **La integración con los sistemas del cliente pesa en la elección de aseguradora, según lo que dicen
   empleadores y brokers.** 59% de los empleadores elegiría una aseguradora integrada a su plataforma de
   beneficios aunque cueste más (LIMRA-EY, 2021; F-854). 59% de los brokers pone la tecnología como el primer factor
   para recomendar aseguradora, a la par de la solidez financiera (57%) (Wellfleet-EIS, 2021; F-852). Es
   preferencia declarada, en EE.UU., y con patrocinio interesado. La evidencia contraria existe: la comisión y el
   producto siguen pesando (F-853, F-880). *Confianza media-baja · E, B.*
6. **La práctica emergente es conectar aseguradora y sistema de nómina por API, pero con personas detrás.**
   Rippling firmó en 2026 conexiones directas con Guardian, MetLife, Unum y Sun Life para no reconciliar datos a
   mano (F-873). Gusto mantiene un equipo humano que empuja planes nuevos, renovaciones y cambios de aseguradora
   (F-876). 🧠 En Perú existe un análogo que nadie parece explotar: la planilla electrónica (T-Registro) ya registra
   la afiliación a EPS de cada trabajador (F-888). *Confianza media en la práctica; la oportunidad peruana es
   inferencia.*
7. **La regulación peruana parece habilitar más de lo que frena, con dos puntos de cuidado.** La SBS reconoce la
   póliza y el certificado electrónicos (F-883), la firma electrónica tiene base legal (F-893) y, según el reglamento
   de registro, solo los productos personales, obligatorios y masivos requieren aprobación previa (F-885).
   Los puntos de cuidado: los datos de salud son sensibles y el nuevo reglamento de protección de datos (vigente
   desde marzo de 2025) sube las exigencias (F-891, F-892); y las EPS responden a SUSALUD además de la SBS (F-889).
   ⚠️ Esto requiere validación legal: no se leyó el texto vigente de ninguna norma. *Confianza media · A, E.*
8. **Automatizar el núcleo es caro y falla seguido.** Solo 40% de las implementaciones de cotizadores
   configurables (CPQ) en empresas B2B "funcionan del todo" (F-878). Un proveedor reconoce que muchos sistemas de
   administración de pólizas de grupo no cumplieron lo prometido (F-881). En la región, Betterfly —que vendía vida
   de grupo en Perú con Interseguro— cerró su operación peruana en 2025 (F-871, F-904). *Confianza media · A.*

**Hallazgo transversal sobre traslado de trabajo.** Varias "eficiencias" de la aseguradora mueven trabajo al
cliente o al broker. La facturación autoadministrada (*self-bill*) deja la conciliación a la empresa (F-900). Los
portales donde el broker teclea los datos del grupo trasladan la digitación al broker; un proveedor lo describe como
la queja típica de los brokers en EE.UU. (F-861, F-875). En RIMAC, donde el broker opera la plataforma, este es el
riesgo a vigilar en el To Be.

---

## 2. Desarrollo por pregunta

### P1. Modelo de producto y personalización

**Práctica 1.1 — Fábrica de producto configurable.** Un motor de reglas guarda coberturas, deducibles, topes y
tarifas como piezas reutilizables. Un plan "nuevo" es una combinación de piezas ya aprobadas, no un desarrollo.

- *Quién:* proveedores de *core* (Duck Creek, EIS, Pega) y sus clientes. EIS describe el caso del negocio de
  accidentes y salud de AIG Canadá: reglas configurables y tarificación automática para salir de procesos manuales
  (F-856). Pega reporta que CareFirst (EE.UU.) lanza productos 50% más rápido (F-859).
- *Resultado:* 📊 solo afirmaciones de proveedor (D). Duck Creek dice que cambia precios en horas y lanza
  productos en semanas (F-857). Un dato de analista (Novarica, citado por Vitech): los productos de grupo tardan ~2
  meses más en salir al mercado que los individuales (F-858; C). ⚠️*solo A*.
- *Prerrequisitos:* catálogo de coberturas normalizado, notas técnicas por pieza, gobierno de quién puede crear
  piezas nuevas.
- *Contraevidencia:* los casos de éxito los publica quien vende el software. Ver P10.
- *Hipótesis:* no dice nada sobre H2-H12.

**Práctica 1.2 — Estandarizar a las pymes y repartir su riesgo en un fondo común.**

- *Quién y cómo:* 📊 En Brasil la norma de la ANS (RN 309/2012) agrupa los contratos empresariales de hasta 29
  vidas y les aplica un mismo índice de reajuste (F-867; A). Alice vende planes PME de 1 a 29 vidas, con propuestas
  válidas 75 días y un mínimo de 3 vidas en adhesión obligatoria (F-868; B). En Perú, Pacífico EPS ofrecía en 2014
  un plan colectivo para empresas de menos de 100 trabajadores cuyos gastos se agrupaban con los de empresas
  similares (nota de Gestión de 2014, sin ficha propia; D, dato antiguo), y hoy promociona un plan pyme desde una persona con solicitud en línea
  (F-895; B). En EE.UU., los estados que estandarizaron planes pyme fijaron niveles de valor actuarial y dejaron a las
  aseguradoras libertad en la red (F-905; C).
- *Qué se gana y qué se pierde:* 📊 Un gestor de planes canadiense sostiene que la estandarización resta
  flexibilidad al patrocinador (F-901; D). En beneficios no médicos de EE.UU., muy pocas aseguradoras ofrecen
  diseños a medida a grupos chicos (F-901; C, 2010). 🧠 Lo que se gana es predecibilidad de tarifa y emisión sin
  diseño; lo que se pierde es margen de negociación del broker.
- *Perspectiva:* A, y E por simplicidad de elección (sin medir).
- *Aplicabilidad en Perú:* 🧠 alta para AMC pyme. Para EPS, el plan mínimo y el crédito de EsSalud fijan un piso
  común (F-887), lo que ya estandariza parte del producto.
- *Hipótesis:* puede atenuar H2 en pymes (menos suscripción manual), sin evidencia directa.

**Práctica 1.3 — Corporativo: negociación acotada y tarifa por experiencia.** El estándar actuarial mezcla la
siniestralidad propia del grupo con una tarifa manual según su credibilidad: a mayor tamaño, más pesa la experiencia
propia (F-863; A metodológica, SOA 2015). Las guías de estudio sitúan el corte en ~50 vidas (tarifa manual) y ~500
(experiencia plena), con variaciones (F-863; D en los cortes). 🧠 Esto da un criterio objetivo para decidir qué
grupos pueden cotizarse por tabla sin intervención y cuáles no.

### P2. Cotización y suscripción de grupos

**Práctica 2.1 — Cotización automática bajo un umbral de vidas.**

- *Quién:* 📊 SulAmérica (Brasil, 2022): la cotización de salud empresarial para 100-199 vidas pasó a generarse en
  el sistema, sin análisis técnico previo; su plataforma "Acelera" permite al broker contratar hasta 99 vidas en
  minutos (F-865; B/D, anuncio sin resultado medido). Bradesco Saúde (2022): cotización y emisión PME 100%
  digitales, con ahorro esperado de hasta 6 días (F-866; D, expectativa). Sami (Brasil): contratación de empresas
  "en minutos", y desde 2023 venta por brokers con comisiones rediseñadas (F-869; D).
- *Perspectiva:* A y B (tiempo de respuesta al broker). E, indirecta.
- *Prerrequisitos:* tabla de tarifas por edad/región, reglas de elegibilidad, censo estructurado.
- *Qué sigue siendo manual:* grupos sobre el umbral, diseños fuera de catálogo, grupos con siniestralidad propia
  creíble (F-863). Analistas de seguros comerciales reportan el mismo patrón: STP alta en negocios chicos, baja en
  grandes y especializados, porque se venden vía brokers con negociación (F-864; C).
- *Hipótesis:* coherente con H2 (los tiempos de respuesta son el dolor que estos referentes atacan). No la confirma
  para Perú.

**Práctica 2.2 — Extracción automática del censo y del pliego (RFP).** El dolor de suscripción más citado es
convertir planillas y documentos del cliente en datos estructurados (F-861; D). Ushur reporta que Equitable bajó el
tiempo de propuesta de 5 días a 5 minutos y automatizó ~85% de las solicitudes (F-860; D, caso único del proveedor).
Milliman vende guías de suscripción pyme por puntos de débito que habilitan reglas automáticas (F-862; C).
⚠️*solo A*. *Contraevidencia:* ningún dato independiente; el "de días a horas" es frase de marketing (F-860).

### P3. Emisión y STP

- **Sin evidencia encontrada de una tasa de STP en emisión colectiva.** Se buscó en presentaciones a inversionistas
  (MetLife, Unum, Sun Life), en analistas (Celent, Datos Insights, Novarica) y en prensa sectorial. Lo más cercano:
  una página de terceros atribuye a MetLife una baja del ratio de gastos de beneficios de grupo de 22,1% (2019) a
  ~19,5% (2023), en parte por STP en **siniestros** rutinarios, no en emisión (F-882; D, a verificar en el 10-K).
- **Dónde se rompe el STP (evidencia indirecta).** 📊 En grupos grandes y diseños negociados (F-864). En la
  conversión de censos (F-861). En la falta de estándar de intercambio: cada aseguradora implementa el archivo 834
  a su manera (F-851; D). 🧠 La emisión en sí es el paso más automatizable; lo que la frena es lo que llega antes
  (datos incompletos) y lo que viene después (altas y bajas).
- *Hipótesis:* coherente con H2 en emisión, sin dato peruano.

### P4. Intercambio de datos de colaboradores

**Práctica 4.1 — Estándar de archivo o API común.** 📊 LIMRA publicó en 2020 sus estándares LDEx para beneficios no
médicos, agregó API en 2021 y salud en 2022. Lo diseñaron 51 empresas; las aseguradoras del comité suman 90% del
mercado no médico de EE.UU. (F-847; B). En 2022, 98% del comité planeaba implementarlo, pero las aseguradoras aún
no lo exigían (F-848; C/D). El archivo ANSI 834 sigue siendo la norma de facto en salud (F-875).

**Práctica 4.2 — Conectores entre aseguradora y plataformas de nómina/beneficios.** 📊 Noyo e Ideon ofrecen una sola
integración hacia muchas aseguradoras; Guardian y Sun Life firmaron con ellas en 2020-2022 (F-874; D, sin
resultados). Employee Navigator dice conectar con 500+ aseguradoras, nóminas y administradores, con 65.000
empleadores y 2.500 brokers (F-875; D). Rippling lanzó en 2026 conexiones directas, co-construidas con cada
aseguradora, con migración de 12 meses para clientes existentes (F-873; D).

**Evidencia sobre errores y facturación.** 📊 HealthCare.gov 2013: ~25% de archivos 834 con errores, luego ~10%;
errores típicos: inscripciones duplicadas, parentesco mal codificado, archivos ilegibles, bajas sin alta previa
(F-849; A reportado por prensa; antiguo pero canónico). Encuesta Harris pagada por Noyo (2022): ~2 de 5 trabajadores
con beneficios sufrió errores; 42% facturas inexactas, 41% problemas de acceso, 37% demoras de cobertura (F-850; C,
patrocinio interesado, muestra no confirmada). Los desfases nacen de que las elecciones son continuas y los archivos
viajan semanal o mensualmente (F-851; D).

- *Perspectiva:* A, E (facturación), B.
- *Aplicabilidad en Perú:* 🧠 **media-alta, con un atajo local.** El T-Registro de SUNAT registra la afiliación a
  EPS y alimenta la PLAME (F-888; A). Un dato que el empleador ya declara al Estado podría ser la fuente de altas y
  bajas, si la empresa lo autoriza. ⚠️ Una guía de SUNAT indica que los datos de cobertura EPS no se descargan a la
  PLAME (F-888): verificar qué campos existen antes de diseñar sobre esto.
- *Hipótesis:* **apoya H6** (fuera de Perú). Apoya débilmente **H7**: los brokers de EE.UU. sostienen procesos con
  hojas de cálculo (F-861, F-875; D). No hay evidencia sobre WhatsApp.

### P5. Rol del intermediario

**Práctica 5.1 — Portal del broker con cotizador y contratación.** SulAmérica (Acelera) y Bradesco (Portal de
Negocios, rediseñado con feedback de brokers) (F-865, F-866). AVLA lanzó en Perú en 2022 una plataforma para más de
1.000 corredores (F-903; D). Sami rediseñó comisiones al abrir el canal broker (F-869).

**Práctica 5.2 — Integración vía API o agregador para agencias grandes.** 📊 En P&C, una encuesta de Celent (2021)
encontró que ~3/4 de los encuestados tenía o planeaba integraciones API con los sistemas de gestión de agencias
(F-879; C). Estudios más antiguos (Novarica 2009-2011) mostraban que los agentes usaban más los portales de la
aseguradora que la integración con su propio sistema; los ejecutivos de cuenta preferían portales y los dueños,
su sistema (F-879; C, antiguo). Las aseguradoras no integran agencia por agencia, por eso las chicas dependen de
agregadores (F-879; D).

**¿La experiencia operativa decide a qué aseguradora lleva el broker sus cuentas?**

| Señal | Qué dice | Nivel | Dirección |
|---|---|---|---|
| Wellfleet-EIS 2021, brokers de beneficios voluntarios EE.UU. | Tecnología 59%, solidez financiera 57%, proceso de siniestros 36% como factores para recomendar; 93% llama "muy importante" la experiencia digital; los principales dolores con aseguradoras son de TI, incluidos errores de facturación (48%) | C, patrocinio interesado (vendedor de software + aseguradora) | Apoya H9 |
| LIMRA, productores (ramo no confirmado) | Más de 90% pondera ajuste al cliente, facilidad para hacer negocios y solidez; la comisión queda en 67% | C, fecha no verificada | Apoya H9 |
| LIMRA-EY 2021, empleadores EE.UU. | 59% elegiría aseguradora integrada aunque cueste más; casi la mitad cambiaría si no está integrada; 44% no está satisfecho con la tecnología de su aseguradora | C | Apoya H9 (desde E) |
| LIMRA, productores de vida individual | Portafolio de productos 57% vs. facilidad para hacer negocios 40% | C | **Contradice** H9 (otro ramo) |
| Cummins & Doherty 2006, *Journal of Risk and Insurance* | La comisión estructura la colocación; las comisiones contingentes alinean incentivos aseguradora-broker; ~4-5% del ingreso del broker | A (arbitrado; financiado por gremio asegurador; canónico) | Matiza H9: la comisión es palanca estructural |

🧠 **Lectura:** la evidencia de H9 es toda **preferencia declarada** en encuesta. No se encontró ningún estudio de
preferencia revelada (qué aseguradora eligió de verdad el broker, controlando por tarifa y comisión). La hipótesis
contraria no queda descartada. **H12:** apoyo débil y de otro ramo (F-879). **H8:** en EE.UU. el broker implementa y
opera la plataforma de beneficios por el empleador (F-875; D); señal coherente, no prueba.

### P6. Autoservicio y visibilidad para la empresa

- 📊 **Hay disponibilidad, no adopción.** Kaiser, CoverGo, The Hartford y otros ofrecen portales para que el
  empleador dé altas, bajas y cambios (resultados de búsqueda sin cifras de uso). McKinsey encontró que dos tercios
  de las personas prefiere informarse sola y ~90% usaría un proceso digital guiado; solo 3 de 12 aseguradoras
  invertía más de 10% de su presupuesto de TI en experiencia digital (F-855; C, ~2016, antiguo).
- **Sin evidencia encontrada de tasas de adopción real** de autoservicio del empleador en colectivos. Se buscó
  "employer portal adoption", "HR administrator digital usage" y similares.
- 🧠 Alan (Francia) es el referente más visible de autoservicio total: 1 millón de miembros y 37.000 empresas
  (2026), con la automatización para clientes empresa como prioridad declarada (F-870; B). No publica cifras de uso
  ni de costo por miembro.
- *Hipótesis:* no dice nada sobre H8.

### P7. Renovación

- 📊 **Perú:** las condiciones mínimas aprobadas por la SBS en varios productos exigen avisar por escrito con 45
  días de anticipación los cambios de la renovación, y dan al contratante al menos 30 días para rechazarlos; la
  renovación automática está permitida con ese aviso (en Colombia esas cláusulas se consideran abusivas) (F-886; A en
  la norma, B en la comparación). No se confirmó que el plazo aplique igual a todos los seguros de grupo.
- 📊 **Brasil:** el fondo común de pymes recibe un índice único de reajuste (F-867): renovación sin negociación caso
  por caso. Alice informó 11,2% de reajuste empresarial en 2025 (F-868; B).
- 📊 **EE.UU.:** la mayoría de las renovaciones de grupo cae en el cuarto trimestre y se recomienda empezar ~4 meses
  antes (D). En 2026, más de un tercio de 3.717 organizaciones vio alzas de 10% o más en su última renovación
  (Gallagher; F-899; C).
- **Sin evidencia encontrada** de resultados medidos de renovación automatizada o anticipada en colectivos.
- 🧠 La regla de 45 días fija un calendario mínimo que obliga a tener la tarifa de renovación lista ~2 meses antes.
  Es un candidato natural a automatizar (cálculo y envío del aviso), y es fuente de confianza para el cliente.
- *Hipótesis:* coherente con H2 en renovación (alzas grandes generan negociación), sin dato peruano.

### P8. Facturación y cobranza

- 📊 **Lista vs. autoadministrada.** En la factura de lista (*list bill*) la aseguradora detalla cada asegurado; en
  la autoadministrada (*self-bill*) el empleador reporta solo totales (F-900; B). Las aseguradoras suelen recomendar
  la de lista porque permite conciliar (F-900). Kaiser rediseñó sus reportes de discrepancias para clientes
  autofacturados (F-900; B).
- 📊 **El costo de conciliar.** Un boletín de RR.HH. reporta que comparar la factura contra el registro propio puede
  tomar semanas cada mes (F-900; D). Diferencias de céntimos por descuento se acumulan en saldos (F-900; A, acta de
  un ente público de Massachusetts).
- 📊 **Perú, dato que cambia el peso del error.** El empleador con EPS descuenta como crédito el 25% de sus aportes a
  EsSalud, con tope en el monto de la factura de la EPS y en 10% de la UIT por trabajador cubierto (F-888; D, foro
  contable que cita el art. 16 de la Ley 26790). 🧠 Un error en la factura de la EPS no es solo un reproceso: puede
  afectar el crédito tributario de la empresa. Esto sube el valor de la exactitud para E.
- *Hallazgo de traslado:* la factura autoadministrada mejora A y traslada la conciliación a E.
- *Hipótesis:* **apoya H6** (fuera de Perú) y da un mecanismo peruano plausible para que el dolor sea agudo.

### P9. Coaseguro (prioridad baja)

- 📊 La Ley del Contrato de Seguro (Ley 29946) tiene un artículo sobre coaseguro (art. 89) y la SBS tiene un
  reglamento de contratación y gestión de reaseguros y coaseguros (F-902; A). No se pudo leer su texto.
- 📊 En Colombia, la Corte Suprema (2024) indicó que los efectos del coaseguro interno entre aseguradoras no son
  oponibles al asegurado (F-902; C).
- **Sin evidencia encontrada** de prácticas operativas para coordinar la emisión entre dos aseguradoras.

### P10. Modelo operativo y transición

- **Sin evidencia encontrada** de estructuras de equipos de emisión (roles, métricas, gobierno del producto) en
  aseguradoras de colectivos. Se buscó "group benefits implementation team", "new case setup" y equivalentes.
- 📊 **Lo más cercano.** Gusto mantiene un equipo de "operaciones de grupo" entre las aseguradoras y su atención al
  cliente para empujar planes nuevos, renovaciones y cambios (F-876; D, avisos de empleo): aun la plataforma más
  digital necesita personas en la emisión.
- 📊 **Fracasos y reversión.** Solo 40% de las implementaciones de CPQ funciona del todo; el éxito depende de alcance
  claro, integración y preparación de la organización (F-878; C, 200 ejecutivos). Un proveedor admite que muchos
  sistemas de administración de grupo adaptados de otros ramos no cumplieron y que seguir puede costar más (F-881;
  D). Benefitfocus terminó vendida a Voya en 2023 por ~US$570 millones (búsqueda; sin ficha propia); Ease dejó de
  aceptar grupos nuevos en 2025 y migró a sus brokers a Employee Navigator (F-875; D). Betterfly despidió al 30% en
  2023 y cerró Perú y otros cuatro países en 2025 (F-871; D).
- 🧠 La consolidación de plataformas de beneficios en EE.UU. sugiere que el negocio de "conectar" es difícil de
  sostener solo; las aseguradoras que lo hacen bien terminan co-construyendo con plataformas grandes (F-873).

### P11. Marco regulatorio y condiciones habilitantes

**Perú.**

| Tema | Qué se encontró | Nivel | Efecto probable |
|---|---|---|---|
| Quién regula | SUSALUD regula, autoriza y registra a las IAFAS; a las empresas de seguros les aplica un régimen propio (art. 9 del DL 1158) y la SBS mantiene su supervisión (F-889). Las EPS nacen de la Ley 26790 (1997), cubren la capa simple y EsSalud la compleja (F-887) | A / D | 🧠 EPS: doble ventanilla (SUSALUD + SBS). AMC: SBS como eje. ⚠️ No se confirmó quién aprueba los planes EPS |
| Registro de productos | Reglamento de registro de modelos de pólizas y notas técnicas (Res. SBS 7044-2013): aprobación previa solo para seguros personales, obligatorios y masivos; los demás, revisión posterior; en pólizas negociadas, póliza y nota técnica deben estar a disposición de la SBS (F-885) | A (vía resúmenes) | 🧠 Habilita una fábrica de producto con piezas registradas. ⚠️ Confirmar si un colectivo de salud negociado cae en "revisión posterior" |
| Póliza electrónica | El reglamento de conducta de mercado (Res. SBS 4143-2019) define la póliza electrónica e incluye el certificado electrónico (F-883). La norma de 2013 exigía consentimiento del contratante para el envío electrónico (F-884; posiblemente superada) | A | Habilita despacho digital de póliza y certificados |
| Firma | Ley 27269 de firmas y certificados digitales y su reglamento (F-893) | A | Habilita contratación remota |
| Renovación | Aviso de 45 días en condiciones mínimas aprobadas (F-886) | A | Fija calendario; fuente de confianza |
| Datos personales | Nuevo reglamento (DS 016-2024-JUS), vigente desde fines de marzo de 2025: oficial de datos personales, gestión de incidentes, portabilidad, responsabilidad proactiva (F-891). La autoridad sostiene que el empleador es responsable de los datos de salud de seguridad laboral y quien hace los exámenes es encargado (F-892) | A (vía estudios jurídicos) | Fricción y confianza a la vez. 🧠 Integrar planilla y aseguradora exige definir roles responsable/encargado y consentimiento |
| Corredores de salud | SUSALUD lleva un registro de corredores de aseguramiento en salud (Res. 124-2021-SUSALUD/S) y prepublicó lineamientos de cláusulas generales de contratos de aseguramiento (F-890) | A | Afecta el rol del broker en EPS |
| Planilla electrónica | T-Registro registra afiliación a EPS; la PLAME se arma desde el T-Registro (F-888) | A | 🧠 Fuente potencial de altas y bajas |

**Contraste Latam.**

- **Chile:** solo se pueden comercializar textos incorporados al Depósito de Pólizas de la CMF (F-896; A). Hay
  oferta digital de seguro complementario de salud para pymes desde 5 empleados (Zurich, 2025; F-897; D).
- **México:** los contratos de adhesión deben registrarse ante la CNSF; los celebrados sin registro son anulables a
  pedido del contratante (LISF arts. 200-201; F-898; A vía extracto).
- **Brasil:** fondo común obligatorio para pymes de hasta 29 vidas (F-867). Open Insurance (SUSEP) avanza con
  prórrogas: la fase 3 para seguros de personas se movió a junio de 2025 y en 2025 se abrió una revisión de normas
  (F-872; A vía estudio jurídico). Permite que corredoras se acrediten para iniciar órdenes del cliente.
- **Colombia:** sin evidencia específica de emisión colectiva; solo el dato de que la renovación automática se
  considera abusiva (F-886) y la jurisprudencia de coaseguro (F-902).
- 🧠 Perú, con revisión posterior para productos no masivos, parece tener un régimen de registro más liviano que el
  depósito previo chileno o el registro obligatorio mexicano. A verificar con el texto vigente.

**Analogías fuera de seguros (equivalencia explícita).**

- *Onboarding corporativo en banca ↔ suscripción + emisión de un grupo nuevo.* Ambos exigen reunir documentos de la
  empresa, validarlos con reglas y aprobar excepciones. Fenergo (2023, 1.100 ejecutivos): la revisión de un cliente
  corporativo toma 95 días en promedio y cuesta ~US$2.600; 48% de los bancos perdió clientes por onboarding lento
  (F-877; C, patrocinio interesado). 🧠 El paralelo sugiere que la lentitud de alta de un cliente empresa tiene costo
  comercial medible.
- *CPQ B2B ↔ cotización de planes con reglas.* Reduce el tiempo de solicitud a cotización 27%, pero solo 40% de las
  implementaciones funciona del todo (F-878; C).
- *Plataformas de nómina ↔ fuente de altas y bajas.* Rippling y Gusto (F-873, F-876); en Perú, el T-Registro (F-888).

---

## 3. Tabla consolidada

| Práctica | Etapa | Referente | Resultado reportado | Persp. | Nivel | Aplicabilidad en Perú |
|---|---|---|---|---|---|---|
| Fábrica de producto con piezas reutilizables | Producto / emisión | AIG Canadá (EIS), CareFirst (Pega), Duck Creek | Lanzamientos más rápidos; CareFirst 50% | A | D | **Media:** el registro SBS por revisión posterior lo facilitaría; exige notas técnicas por pieza |
| Plan pyme estandarizado con riesgo en fondo común | Producto / cotización / renovación | ANS RN 309 (BR), Alice, Pacífico | Reajuste único; contratación desde 1 vida | A, E | A (norma) / B | **Alta** en AMC pyme; en EPS el plan mínimo ya estandariza |
| Tarifa por experiencia según credibilidad | Suscripción | SOA (método) | Criterio objetivo de cuándo cotizar por tabla | A | A (metodológica) | **Alta:** define el umbral del STP |
| Cotización automática bajo umbral de vidas | Cotización | SulAmérica, Bradesco Saúde, Sami | 100-199 vidas sin análisis técnico; hasta −6 días (esperado) | A, B | B/D | **Alta** si el broker obtiene tarifa en el acto |
| Extracción automática de censo y RFP | Suscripción | Equitable (Ushur), Majesco | 5 días → 5 min (caso único) | A | D | **Media:** depende de la calidad de las planillas que llegan |
| Estándar común de datos de altas/bajas | Endosos | LIMRA LDEx, ANSI 834 | Estándar creado; adopción voluntaria | A, E, B | B/C | **Media-baja:** no hay estándar local; el T-Registro es el candidato |
| Conexión aseguradora–nómina por API | Endosos / emisión | Rippling + Guardian/MetLife/Unum/Sun Life; Noyo; Ideon | Sin resultados publicados | A, E | D | **Media:** existen Buk y otras nóminas locales; sin evidencia de conexión con aseguradoras |
| Portal del broker con cotizador y contratación | Cotización / emisión | SulAmérica Acelera, Bradesco, AVLA Iglu (PE) | Contratación en minutos (anuncio) | B | D | **Alta** para corredores persona natural; riesgo de trasladar digitación |
| Integración vía API o agregador para agencias | Cotización / endosos | Celent (P&C) | ~3/4 con API desplegada o planeada | B | C | **Media** para agencias grandes |
| Portal de autoservicio del empleador | Postventa | Kaiser, CoverGo, Alan | Sin datos de adopción | E | D | **Desconocida:** validar en campo |
| Aviso de renovación con plazo fijo | Renovación | SBS (45 días) | Plazo normado | E, B | A | **Alta:** ya obligatorio; automatizable |
| Factura de lista con detalle por asegurado | Cobranza | Standard, Kaiser | Permite conciliar; self-bill traslada trabajo a E | A, E | B | **Alta:** el crédito EPS hace crítica la exactitud |
| Equipo humano de "operaciones de grupo" junto a la plataforma | Modelo operativo | Gusto | Señal de que la emisión no es 100% automática | A | D | **Alta** como principio de diseño |

---

## 4. Vacíos

| Vacío | Qué se buscó | Qué fuente haría falta |
|---|---|---|
| Tasa de STP en emisión colectiva | Investor days, analistas, prensa | Benchmark de Celent/Datos Insights pagado, o línea base propia de RIMAC (process mining del flujo actual) |
| Adopción real de autoservicio del empleador | "employer portal adoption" y variantes | Datos de uso de portales de aseguradoras; métricas propias |
| Preferencia revelada del broker (no declarada) | Estudios de colocación vs. experiencia operativa | Datos SBS de primas por corredor y aseguradora cruzados con cambios de plataforma; estudio académico |
| Errores de altas/bajas en Perú | SUSALUD, SBS, APESEG | Reclamos SUSALUD/Indecopi por facturación EPS; datos internos de notas de crédito |
| Participación de corredores en salud colectiva peruana | SBS, APECOSE | Estadística SBS de intermediación por ramo |
| Afiliados EPS por empresa (2025-2026) | SUSALUD | Boletín estadístico de IAFAS EPS de SUSALUD (el dato de 2,9% de la población, F-894, no tiene fecha confirmada) |
| Quién aprueba planes EPS y qué tan rápido | SUSALUD, SBS | Texto vigente de la normativa EPS; consulta legal |
| Estructura de equipos de emisión eficientes | Roles, métricas, gobierno | Entrevistas con pares de la región (SulAmérica, Sura), casos de consultoras |
| Prácticas de coaseguro operativo | SBS, Ley 29946 | Texto del art. 89 y del reglamento SBS; práctica de mercado |
| Colombia y México en salud colectiva | SFC, CNSF, FASECOLDA, AMIS | Normas de registro y estudios gremiales |
| Texto completo de todas las fuentes | — | Repetir la lectura en un entorno sin bloqueo de red; varias cifras quedan "a verificar" |

---

## 5. Preguntas para el campo

Para saber si cada práctica responde a un dolor real o a una necesidad interna de la aseguradora:

1. **Producto estandarizado (P1):** ¿Qué parte del plan negociado le importa de verdad a la empresa y qué parte negocia
   el broker por costumbre? ¿Aceptaría un plan de catálogo si la tarifa sale en el acto?
2. **Cotización inmediata (P2):** ¿Cuánto tiempo espera hoy una cotización? ¿Qué pierde la empresa o el broker
   mientras espera (una oferta de otra aseguradora, una fecha de inicio)?
3. **Censo (P2/P4):** ¿En qué formato entrega la empresa la lista de trabajadores? ¿Cuántas veces se la devuelven
   por errores?
4. **Altas y bajas (P4):** ¿Quién avisa un alta, por qué canal y cuánto tarda en reflejarse? ¿La empresa estaría
   dispuesta a que la aseguradora lea los datos de su planilla (T-Registro o su sistema de nómina)? ¿Qué le daría
   miedo?
5. **Facturación (P8):** ¿Cuántas horas al mes dedica la empresa a conciliar la factura? ¿Alguna vez un error afectó
   su crédito EPS?
6. **Broker y aseguradora (P5, H9):** Cuéntame la última vez que llevaste una cuenta a otra aseguradora. ¿Qué la
   decidió? ¿Qué tendría que fallar en la operación para que te vayas aunque la tarifa sea mejor?
7. **Broker persona natural vs. agencia (H12):** ¿Usas el portal de la aseguradora o tu propio sistema? ¿Qué
   tecleas dos veces?
8. **Visibilidad (H8):** ¿La empresa sabe en qué estado está su trámite sin preguntarle al broker? ¿Quiere saberlo?
9. **Autoservicio (P6):** ¿Qué haría la empresa sola si pudiera, y qué prefiere seguir delegando al broker?
10. **Renovación (P7):** ¿Con cuánta anticipación llega hoy la propuesta de renovación? ¿Qué información falta para
    decidir?
11. **Herramientas paralelas (H7):** ¿Qué hojas de cálculo, correos o chats de WhatsApp existen solo para seguir el
    trámite? ¿Quién los mantiene?

---

## 6. Relación con las hipótesis del estudio de campo

| Hipótesis | Qué dice la evidencia secundaria | Veredicto |
|---|---|---|
| H2 (dolores en suscripción, emisión, renovación) | Los referentes atacan tiempos de cotización y emisión (F-865, F-866) y la intake del censo (F-861); alzas de renovación grandes (F-899) | Apoya parcialmente, fuera de Perú |
| H6 (altas/bajas → reprocesos en facturación) | Errores de inscripción y facturas inexactas (F-849, F-850); conciliación costosa (F-900); crédito EPS amplifica el error (F-888) | Apoya, fuera de Perú; mecanismo peruano plausible |
| H7 (Excel, correo, WhatsApp) | Brokers de EE.UU. con hojas de cálculo (F-861, F-875; D) | Apoyo débil; nada sobre WhatsApp |
| H8 (la empresa ve poco en cuentas intermediadas) | En EE.UU. el broker implementa la plataforma por el empleador (F-875) | No dice casi nada |
| H9 (el broker evalúa el esfuerzo operativo) | Preferencia declarada a favor (F-852, F-853, F-854); comisión y producto pesan (F-853, F-880) | Mixta; sin preferencia revelada |
| H12 (persona natural depende de la plataforma; agencias piden integración) | Agencias chicas dependen de portales o agregadores; adopción de API en P&C (F-879) | Apoyo débil, otro ramo |

---

## 7. Fuentes consolidadas

Tipo: P = primaria, S = secundaria. Independencia: I = independiente, C = con interés comercial.

| ID | Organización / autor | Título | Año | URL | Tipo | Indep. | Nivel |
|---|---|---|---|---|---|---|---|
| F-847 | LIMRA | Enhancements to Data Exchange Standards (all employee benefits) | 2022 | https://www.limra.com/en/newsroom/news-releases/2022/limras-newest-enhancements-to-data-exchange-standards-allow-for-enrollment-in-all-employee-benefits-plans/ | P | C (gremio) | B |
| F-848 | LIMRA | LDEx battle card | 2022 | https://www.limra.com/siteassets/about/sales-repository/product/ldex/ldex-battle-card.pdf | P | C | C |
| F-849 | CMS vía The New Republic / Benton | Obamacare 834 error rate falls from 25% to 10% | 2013 | https://newrepublic.com/article/115837/obamacare-834-error-rate-falls-25-percent-10-percent | S | I | A (dato regulatorio vía prensa; antiguo) |
| F-850 | The Harris Poll para Noyo | Consumer impact of bad data in employee benefits | 2022 | https://prnewswire.com/news-releases/harris-poll-reveals-consumer-impact-of-bad-data-in-employee-benefits-301820336.html | P | C | C |
| F-851 | Impakter | Why keeping carriers in sync with enrollment data is harder than it looks | 2026 | https://impakter.com/why-keeping-carriers-in-sync-with-enrollment-data-is-harder-than-it-looks/ | S | ? | D |
| F-852 | Wellfleet & EIS | Workplace Benefits Broker Survey | 2021 | https://businesswire.com/news/home/20211117005427/en/Wellfleet-and-EIS-Survey-Finds-Workplace-Benefits-Brokers-Demanding-Better-Technology | P | C | C |
| F-853 | LIMRA vía InsuranceNewsNet | It's Not All About Comp Anymore | s.f. | https://insurancenewsnet.com/innarticle/It%E2%80%99s-Not-All-About-Comp-Anymore-LIMRA-a-471119 | S | C (gremio) | C |
| F-854 | LIMRA & EY | Workplace benefits technology study | 2021 | https://www.limra.com/en/research/workplace-benefits/workplace-benefits-technology/ | P | C (gremio) | C |
| F-855 | McKinsey & Company | The future of group life insurance in the US | ~2016 | https://www.mckinsey.com/industries/financial-services/our-insights/the-future-of-group-life-insurance-in-the-us | P | C | C (antiguo) |
| F-856 | EIS Group | AIG Canada A&H core insurance case study | s.f. | https://www.casestudies.com/company/eis-group/case-study/aig-canada-ah-deploys-eis-core-insurance-software-for-its-group-benefits-business | P | C | D |
| F-857 | Duck Creek | How leading insurers launch new products faster | s.f. | https://www.duckcreek.com/resource/blog/how-leading-insurers-launch-new-products-faster/ | P | C | D |
| F-858 | Vitech (cita Novarica) | Group insurers' need for speed to market | 2024 | https://www.vitechinc.com/wp-content/uploads/2024/05/INSIGHT-Group-Insurers-Need-for-Speed-to-Market.pdf | S | C | C |
| F-859 | Pegasystems | CareFirst BlueCross BlueShield case study | s.f. | https://www.casestudies.com/company/pegasystems/case-study/carefirst-bluecross-blueshield-customer-case-study | P | C | D |
| F-860 | Ushur | AI automation for group benefits quoting and RFP intake | 2025 | https://ushur.ai/newsroom/ushur-unveils-ai-powered-automation-solutions-for-group-benefits-quoting-and-rfp-intake | P | C | D |
| F-861 | Majesco | Intelligent underwriting for group, voluntary and worksite | s.f. | https://majesco.com/blog/intelligent-underwriting-strategic-business-value-for-group-voluntary-benefits-and-worksite-insurers | P | C | D |
| F-862 | Milliman | Small Group Medical Underwriting Guidelines | s.f. | https://id.milliman.com/-/media/products/sgmugs/sgmugs.ashx | P | C | C |
| F-863 | Society of Actuaries | A practical approach to assigning credibility for group medical insurance pricing | 2015 | https://www.soa.org/globalassets/assets/Files/Research/research-2015-practical-approach-assigning-credibility-group-medical.pdf | P | I | A (metodológica) |
| F-864 | Capco (cita Novarica) | Commercial insurance transformation / insurance trends | 2025-26 | https://www.capco.com/intelligence/capco-intelligence/finding-success-across-the-insurance-value-chain | S | C | C |
| F-865 | SulAmérica vía Revista Apólice | Novidades para planos empresariais de saúde e odonto | 2022 | https://www.revistaapolice.com.br/2022/03/sulamerica-traz-novidade-para-planos-empresariais-de-saude-e-odonto/ | S | C | B/D |
| F-866 | Bradesco Saúde vía Revista Apólice | Bradesco simplifica contratação de seguro saúde com tecnologia | 2022 | https://revistaapolice.com.br/2022/02/bradesco-simplifica-contratacao-de-seguro-saude-com-tecnologia/ | S | C | D |
| F-867 | ANS (Brasil) | RN 309/2012 — agrupamento de contratos (pool de risco) | 2012-13 | https://www.gov.br/ans/pt-br/arquivos/acesso-a-informacao/participacao-da-sociedade/http-answeb-producao-administrator-9c990ba54f978eb173ed9241dfce1a20/10/ap10_nt2013_propostas_reajustes_planos_coletivos.pdf | P | I | A |
| F-868 | Alice | Manual do corretor (abr. y dic. 2025) | 2025 | https://alice.com.br/blog/wp-content/uploads/2024/03/manual-do-corretor-alice-dezembro-de-2025.pdf | P | C | B |
| F-869 | Sami vía Revista Apólice / Brazil Journal | Sami aposta em canal de corretores | 2020-23 | https://revistaapolice.com.br/2023/06/sami-capta-r-90m-e-aposta-em-novo-canal-de-vendas-via-corretores/ | S | C | D |
| F-870 | Alan | Press room / carta a accionistas 2025 | 2025-26 | https://alan.com/en/about/press-room | P | C | B |
| F-871 | Forbes Perú / Forbes Chile | Betterfly cierra operaciones en Perú y otros cuatro países | 2023, 2025 | https://forbes.pe/negocios/2025-03-17/betterfly-cerro-sus-operaciones-en-peru-y-otros-cuatro-paises-como-parte-de-su-reorganizacion | S | I | D |
| F-872 | Demarest / Legismap | Susep publica novos prazos do Open Insurance; retrospectiva 2025 | 2024-25 | https://www.demarest.com.br/susep-publica-novos-prazos-e-regras-para-a-implementacao-do-open-insurance-e-a-participacao-das-sociedades-processadoras-de-ordem-do-cliente/ | S | I | A (norma vía estudio jurídico) |
| F-873 | Rippling / Guardian / Sun Life | Direct carrier integrations (Preferred Carrier Program) | 2026 | https://www.businesswire.com/news/home/20260716427534/en/ | P | C | D |
| F-874 | Noyo, Ideon, Guardian, Sun Life | Anuncios de alianzas de conectividad | 2020-22 | https://www.businesswire.com/news/home/20220727005367/en/Sun-Life-and-Ideon-Partner-to-Make-Benefits-Enrollment-Faster-and-Easier-for-Employers-Employees-and-Brokers | P | C | D |
| F-875 | Employee Navigator / Warner Pacific | Integraciones 2025; transición desde Ease | 2025 | https://www.warnerpacific.com/news/employee-navigator-ease-integration-updates | P | C | D |
| F-876 | Gusto | Avisos de empleo: Group Operations Fulfillment | 2025-26 | https://www.builtinchicago.org/job/group-operations-fulfillment-benefit-services/9387314 | P | C | D (señal) |
| F-877 | Fenergo | KYC / onboarding de clientes corporativos | 2023 | https://resources.fenergo.com/newsroom/arduous-client-onboarding-and-kyc-costing-banks-millions | P | C | C |
| F-878 | Simon-Kucher | Unlocking growth through pricing and quoting automation | s.f. | https://www.simon-kucher.com/en/insights/unlocking-growth-through-pricing-and-quoting-automation | P | C | C |
| F-879 | Novarica / Celent vía Insurance Journal | Portales vs. sistemas de agencia; API | 2009-21 | https://www.insurancejournal.com/news/national/2021/10/05/635341.htm | S | C | C |
| F-880 | Cummins, J. D. & Doherty, N. A. | The Economics of Insurance Intermediaries (*J. Risk Insur.* 73(3)) | 2006 | https://ideas.repec.org/a/bla/jrinsu/v73y2006i3p359-396.html | P | I (financiado por gremio) | A (canónico) |
| F-881 | FINEOS | Group benefits policy admin systems not living up to expectations | 2023 | https://www.fineos.com/2023/05/10/policy-administration-systems-for-group-benefits-not-living-up-to-expectations-stay-the-course-or-change-direction/ | P | C | D |
| F-882 | PitchGrade (terceros) | MetLife: group benefits and AI | s.f. | https://pitchgrade.com/research/metlife-ai-margin-pressure | S | ? | D (verificar en 10-K) |
| F-883 | SBS | Res. SBS N° 4143-2019, Reglamento de Gestión de Conducta de Mercado | 2019 | https://www.interseguro.pe/wp-content/uploads/2021/06/Reg.-de-Gestión-de-Conducta-de-Mercado_Res.-SBS-N°-4143-2019.pdf | P | I | A |
| F-884 | SBS | Res. SBS N° 3201-2013, Reglamento para el uso de pólizas electrónicas | 2013 | https://www.mapfre.com.pe/media/reglamento-para-el-uso-de-polizas-electronicas-sbs-3201.pdf | P | I | A (posiblemente superada) |
| F-885 | SBS | Res. SBS N° 7044-2013, Registro de modelos de pólizas y notas técnicas (citada en Res. 04208-2024 y 01050-2026) | 2013 | https://imagescdn.rimac.com/blt7bb7bb15f3a9d714/6788124619a7e33c030b3af2/RESOLUCIÓN_SBS_N_04208_-_2024_-_SBS-PRI.pdf | P | I | A |
| F-886 | SBS (condiciones mínimas) / Fundación MAPFRE | Aviso de 45 días en renovación; comparativa Perú-Colombia | varios | https://documentacion.fundacionmapfre.org/documentacion/es/media/group/1075225.do | P/S | I | A / B |
| F-887 | Trámites Perú (sobre Ley 26790) | EPS vs EsSalud; planes EPS | s.f. | https://tramitesperu.com/comparadores/eps-vs-essalud/ | S | ? | D |
| F-888 | SUNAT / Noticiero Contable | T-Registro y PLAME; crédito EPS | 2023-24 | https://orientacion.sunat.gob.pe/sites/default/files/inline-files/PDF%20de%20T-Registro%20y%20PLAME.pdf | P/S | I | A / D |
| F-889 | SUSALUD | Política regulatoria de SUSALUD | s.f. | https://cdn.www.gob.pe/uploads/document/file/1909409/POLITICA%20REGULATORIA%20DE%20SUSALUD.pdf.pdf | P | I | A |
| F-890 | SUSALUD | Res. 124-2021-SUSALUD/S (corredores); proyecto de lineamientos de cláusulas generales | 2021 | https://cdn.www.gob.pe/uploads/document/file/2648018/Res-124-2021-SUP.pdf.pdf | P | I | A |
| F-891 | Garrigues / CMS / El Peruano | Nuevo reglamento de la Ley de Protección de Datos Personales (DS 016-2024-JUS) | 2024-25 | https://www.garrigues.com/es_ES/noticia/peru-publica-nuevo-reglamento-ley-proteccion-datos-personales | S | I | A (norma vía estudio jurídico) |
| F-892 | ANPD (MINJUSDH) vía LP Derecho | Opinión Consultiva 013-2021-JUS/DGTAIPD | 2021 | https://lpderecho.pe/empleador-informacion-examenes-medicos-trabajadores-opinion-consultiva-013-2021-jus-dgtaipd | P | I | A |
| F-893 | Congreso / PCM | Ley 27269 y DS 052-2008-PCM | 2000, 2008 | https://appddpadigital.agn.gob.pe/ddpa/wp-content/uploads/2024/12/Ley-N°27269.pdf | P | I | A |
| F-894 | ComexPerú (datos SUSALUD) | Policy brief EsSalud | s.f. | https://comex-assets.s3.amazonaws.com/comex-assets/web/posts/20652/Policy_brief_EsSalud_.pdf | S | I (gremio) | C |
| F-895 | Pacífico Seguros | Seguro Pyme Salud Base (folleto) | 2026 | https://www.pacifico.com.pe/documents/28730/191105486/Flyer+-+Seguro+Pyme+Salud+Base+-+Feb26.pdf/4fd0a3eb-8e05-788c-5979-30f9731df155 | P | C | B |
| F-896 | CMF Chile | Depósito de Pólizas | s.f. | https://www.cmfchile.cl/portal/principal/623/w4-article-14649.html | P | I | A |
| F-897 | Chócale | Zurich lanza seguro complementario de vida y salud para pymes desde 5 empleados | 2025 | https://chocale.cl/2025/05/zurich-lanza-seguro-complementario-de-vida-y-salud-para-pymes-desde-5-empleados/ | S | ? | D |
| F-898 | Congreso de la Unión (México) | LISF arts. 200-201 (extracto) | — | https://www.stewart.com/content/dam/stewart/Microsites/mexico/pdfs/transcipcion-de-diposiciones-legales-citadas.pdf | P | I | A (vía extracto) |
| F-899 | Gallagher vía Insurance Business | Benefits data moves to center of broker renewal talks | 2026 | https://www.insurancebusinessmag.com/us/news/benefits/benefits-data-moves-to-center-of-broker-renewal-talks-591058.aspx | S | C | C |
| F-900 | Standard Insurance; Kaiser; Net@Work; GIC Massachusetts | List bill vs self-admin; reportes de discrepancias | varios | https://www.standard.com/eforms/19015.pdf | P/S | C/I | B / D |
| F-901 | SOA (The Independent Consultant) / Benefits Canada | Personalización y estandarización de planes de grupo | 2010; s.f. | https://www.soa.org/4934a4/globalassets/assets/library/newsletters/the-independent-consultant/2010/august/ind-2010-iss31-lambert.pdf | S | I | C / D |
| F-902 | Congreso (Ley 29946); SBS; Pérez-Llorca / Asuntos Legales (CO) | Coaseguro: art. 89; reglamento de reaseguros y coaseguros; jurisprudencia colombiana | 2012; 2024 | https://www.perezllorca.com/es-co/actualidad/boletin/coaseguro-en-colombia-concepto-aplicacion-y-jurisprudencia-reciente/ | P/S | I | A / C |
| F-903 | Infomercado | AVLA lanza Iglu, plataforma digital para corredores | 2022 | https://infomercado.pe/avla-lanza-iglu-la-nueva-plataforma-digital-para-corredores-de-seguros-280422-gb/ | S | ? | D |
| F-904 | SBS vía Interseguro | Res. SBS 02107-2022, aprobación Vida Grupo Betterfly | 2022 | https://www.interseguro.pe/Documentos/vida-grupo-betterfly/RESOLUCI%C3%93N%20SBS%20N%2002107-2022%20-%20Aprobaci%C3%B3n%20Vida%20Grupo%20Betterfly.pdf | P | I | A |
| F-905 | Rockefeller Institute of Government | Product standardization in small group markets | s.f. | https://policyarchive.org/download/22077 | P | I | C |

---

## Conexiones

- [[mecanismos-seguros-salud]] — por qué la presión de costo médico explica las alzas de renovación y el interés en
  estandarizar (contexto financiero de P7).
- [[glosario-seguro-salud-peru]] — términos de EPS, EsSalud, capa simple y crédito EPS en lenguaje claro.
- [[futuro-asesores-seguros-venta-digital]] — el rol del intermediario frente a la automatización (P5, H9, H12).
- [[seguros-comportamiento-mundo-peru]] — confianza del cliente peruano y efecto del broker sobre la confianza
  (marco de H8 y H9).
- [[tendencias-diseno-innovacion]] — regla de criterio sobre cifras de proveedores interesados y cadenas de eco:
  aplica a casi toda la evidencia D de este node.
