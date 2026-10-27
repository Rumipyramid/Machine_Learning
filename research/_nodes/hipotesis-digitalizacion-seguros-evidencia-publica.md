# Hipótesis de digitalización en seguros: qué responde la evidencia pública y qué exige dato interno

> Documento de investigación. Fuente persistente y versionada en el repositorio.
> Fecha de elaboración: 2026-10-27 · Última actualización: 2026-10-27 · Versión: v1.0
> Origen: `/trinidad` (pista empírica/teórica y pista de negocio; la social no se corrió, ver §8) pedida por el usuario para
> hacer "doble clic" en `digitalizacion-seguros-mercados-emergentes`: qué más se puede investigar para sus puntos abiertos y
> cuáles de las hipótesis de un estudio interno se pueden responder con fuentes públicas.
> Fuentes registradas en `research/fuentes/codice.md` (F-1007 a F-1029); reutiliza F-877, F-884, F-888, F-936, F-1003,
> F-851, F-852, F-923.
> 🔒 **Las hipótesis vienen de un estudio interno que no se versiona** (repositorio público). Aquí están **reformuladas en
> términos genéricos, sin cifras, módulos ni identificadores del estudio**. La correspondencia con las del estudio vive fuera
> del repositorio.

---

## 0. Conclusión

**Con fuentes públicas no se puede cerrar ninguna de las hipótesis sobre recurrencia y fidelidad digital; se puede
afinarlas, decidir cuáles no vale la pena buscar afuera y diseñar cómo probarlas con dato propio.** La razón es una sola: casi
toda la evidencia pública sobre "el cliente digital se queda más" es una correlación medida por quien vende la tecnología,
y el único experimento aleatorizado hallado sobre un caso parecido (programas de bienestar) muestra que **quien participa ya
era distinto antes de participar** (F-1028).

Cuatro ideas, de más a menos sólida:

1. **Sí hay un argumento estructural que la evidencia pública sostiene bien:** los seguros tienen pocos contactos naturales
   por año y la actividad la fija el producto (un seguro de vida casi no genera siniestros; el de autos, unos seis por cada
   cien asegurados al año). Es difícil que una app cambie eso por sí sola (F-1020, F-1018).
2. **Fidelidad:** hay correlación consistente entre uso digital y menos bajas (F-1007, F-1027), un caso con signo favorable
   y mejor diseñado (F-1012) y **ninguna prueba causal independiente** de que el app reduzca la caducidad. La banca tampoco
   la tiene (F-1010).
3. **Bancaseguros:** los pocos datos públicos apuntan a que **pesa más el producto que el canal** (F-1016), pero son de la
   India y de 2014. En Perú no se halló ni la participación del canal ni la persistencia.
4. **Techo digital, activación, familiar cubierto y a quién acude el cliente:** la evidencia pública no responde; requieren
   dato interno (§4).

Qué hacer: usar lo público para **calibrar expectativas y fijar el diseño de prueba**, y reservar el dato interno para lo
causal. §6 trae los diseños.

---

## 1. Qué se pidió y qué no es este documento

- **Se pidió:** averiguar, para cada hipótesis, si la evidencia pública (insurtech, banca, seguros en el mundo, LATAM, Perú)
  puede responderla, parcialmente o no.
- **Es un triaje de hipótesis más un mapa de evidencia, no una prueba de ellas.** Una hipótesis "con evidencia a favor" en el
  estudio interno no se confirma ni se refuta aquí.
- **Todo se leyó por resúmenes de búsqueda o notas de prensa.** Ningún informe se abrió completo. Mucha evidencia viene de
  proveedores que venden lo que miden.
- **No se halló ninguna fuente peruana** sobre canal, persistencia ni activación digital. Perú aparece solo con contexto
  previo del node de digitalización.

Cada hipótesis recibe uno de tres veredictos sobre **qué tanto la evidencia pública puede responderla**:

- 🟢 **Lo público orienta con claridad** (no la cierra; apoya o contradice la dirección).
- 🟡 **Lo público da contexto y método, no respuesta.**
- 🔴 **Solo con dato interno.**

---

## 2. Hipótesis reformuladas y triaje

| # | Hipótesis (genérica) | Veredicto | Qué se halló | Dato interno que falta |
|---|---|---|---|---|
| HD1 | La proporción digital actual es una meta, no un techo calculado; las carteras grandes sin digitalizar pueden no tener nada que ofrecerles | 🔴 | Referencias externas de adopción, no un techo de una cartera concreta | Composición de la cartera y qué ofrecer a cada segmento |
| HD2 | El cliente digital se queda más (y la comparación mezcla dos poblaciones: el cliente antiguo y el nuevo) | 🟡 | Correlación a favor; sesgo de selección documentado; un caso con signo favorable | Cohortes separadas, antes/después de la adopción |
| HD3 | Cada producto tiene su propio momento de activación, o la activación es transversal | 🔴 | Nada en seguros; guías de fintech de proveedores | Embudo de activación por producto y momento |
| HD4 | El familiar cubierto también aporta valor (los familiares digitalizados se dan de baja menos) | 🟡 | Agrupar productos sí asocia con más retención; "familiar" no se halló | Corte por cobertura de dependientes |
| HD5 | Hace falta una llave de entrada por cartera; en algunas basta con el siniestro | 🟡 | El siniestro pesa en la intención de renovar | Qué evento activa a qué cartera |
| HD6 | El canal de venta se puede mover, pero no todos por igual | 🟡 | Cifras de proveedores; sin retención | Potencial por canal y retención por canal |
| HD7 | En bancaseguros, estar en la app no cambia nada: el cliente se va por el producto, no por el canal | 🟡 | Dato indio antiguo a favor de "pesa el producto"; sin dato peruano | Persistencia por producto y canal; ligado al crédito |
| HD8 | Lo que determina la actividad es el producto, no el canal; la gente casi no interactúa con la propuesta de valor | 🟢 | Frecuencia de contacto y de siniestro estructuralmente baja | Medir actividad digital por producto |
| HD9 | A quién acude el cliente del banco depende del producto | 🔴 | Solo señales de banca (producto ancla) | Ruta de contacto por producto |
| HD10 | Cada ramo está en un nivel de madurez digital distinto (distinguir "aquí no funciona" de "aquí no se intentó") | 🟡 | Oferta por ramo; sin adopción por ramo en LATAM ni Perú | Madurez por ramo con datos de la cartera |

**Dos de las hipótesis se pueden afinar solo con lo hallado:** HD8 gana apoyo estructural, y HD2 se reformula en términos
de selección (§6).

---

## 3. Dónde se halló evidencia, por lente

`—` = se buscó y no se halló. Los IDs F-n remiten al ledger.

| | Insurtech | Banca | Seguros en el mundo | LATAM | Perú |
|---|---|---|---|---|---|
| **HD1 Techo** | — | — | F-1009, F-1023 | F-1029 (solo oferta) | — |
| **HD2 Más fiel** | F-1026 | F-1010, F-1011, F-1014 | F-1007, F-1008, F-1012, F-1027, F-1028 | — | — |
| **HD3 Activación** | F-1025 (fintech, proveedores) | F-1025 | — | — | — |
| **HD4 Familiar** | — | — | F-1018, F-1019 | — | — |
| **HD5 Siniestro** | — | — | F-1021, F-1022 | — | — |
| **HD6 Canal de venta** | — | — | F-1023, F-1024 | — | F-884 (SOAT ~90% digital) |
| **HD7 Bancaseguros** | — | F-1015 | F-1016, F-1017 | F-1017, F-1029 | F-877 (desgravamen opcional) |
| **HD8 Producto** | — | F-1020 (200 contactos al año en banca) | F-1020, F-1016, F-1018 | — | — |
| **HD9 A quién acude** | — | F-1015 | — | — | — |
| **HD10 Por ramo** | — | — | F-1009, F-1023 | F-1029, F-1003 | F-888, F-936 |

**Lectura.** Perú queda vacío de evidencia específica en casi todas las filas: lo digital peruano hallado es oferta y
cobertura de pagos, no conducta de retención. LATAM tiene oferta y crecimiento, no retención. La banca ofrece ideas de
método, no resultados causales.

---

## 4. Hipótesis por hipótesis

### HD1 — Techo digital 🔴

- **Qué dice lo público.** Los líderes digitales del seguro en EE.UU. logran que hasta 61% (auto) y 54% (hogar) de los clientes
  inicien una venta por canales digitales (F-1023, Bain, medido sobre quién inicia, no sobre quién completa ni retiene). El uso
  de la app del plan de salud es 38% entre asegurados comerciales y 20% en Medicare Advantage (F-1009). Sirven de **referencia
  externa**, no de techo: son países, ramos y poblaciones distintas.
- **Por qué no se responde afuera.** Un techo es una propiedad de una cartera concreta (edad, conectividad, qué se les ofrece).
  La parte "puede que no haya nada que ofrecerles" es una pregunta de producto, no de adopción.
- **Qué probar adentro.** Segmentar la cartera sin digitalizar por motivo (no puede, no quiere, no se le ofreció) y probar una
  oferta mínima en una muestra.
- **Para Perú.** El contexto previo (informalidad, billeteras, F-879, F-936) sugiere que el techo está ligado a quién cobra
  y paga en digital, no solo a la tecnología.

### HD2 — El cliente digital se queda más 🟡

- **A favor (correlación).** Asegurados de 21 aseguradoras con portal cancelan menos que los que no lo usan (F-1007, de un
  proveedor); un asegurador de autos europeo tiene **menos abandono entre clientes captados por comparador** (3% menos según
  el resumen original; 6% según una página posterior, F-1012); Vitality reporta tasas de caducidad de 3,5% a 6,9% en su base
  y AIA Australia 40% menos caducidad entre inscritos (F-1027, de la propia empresa, mezclado con su modelo de precios). En
  banca, clientes digitalmente activos compran más productos y cuestan menos (F-1014).
- **Contra o matiz.** Una encuesta sudafricana halla correlación **negativa** entre confianza digital e intención de
  quedarse (F-1010), y los estudios de banca móvil son sobre todo transversales (F-1010).
- **El problema central es la selección.** En el experimento de Illinois (F-1028) los que aceptaron el programa ya gastaban
  menos y tenían mejores hábitos **antes** de entrar; el programa no cambió el gasto en el primer año. Traslado (inferencia
  mía): quien baja la app puede ser quien ya iba a quedarse.
- **Qué probar adentro.** Separar poblaciones (cliente antiguo y nuevo no se suman) y comparar solo clientes parecidos antes
  de adoptar, con diferencias en diferencias (§6.1).
- **Lo que no se halló:** ninguna estimación causal independiente de app a caducidad, ni en seguros ni en banca (F-1010);
  el único diseño causal hallado en banca es un extracto sin resultados verificados (F-1011).

### HD3 — Activación: por producto o transversal 🔴

- **Lo público no toca seguros.** Las guías de fintech dicen que se optimiza para los primeros 30 días y que completar el alta
  predice poco la retención frente al primer beneficio real, pero son de proveedores y sus benchmarks se contradicen entre sí
  (73% frente a 10-15% frente a 2,6% de retención a 30 días, F-1025). **No sirven como vara.**
- **Pista de método.** La tasa de activación se define como quienes completan una acción clave sobre quienes empezaron el
  alta; ahí está lo medible.
- **Qué probar adentro.** Definir por producto cuál es "el primer beneficio" (cobrar un siniestro, usar el seguro de salud,
  consultar un saldo) y medir el embudo.

### HD4 — El familiar cubierto aporta valor 🟡

- **Lo hallado es sobre agrupar productos, no personas:** retención de 95% con auto y hogar juntos frente a 85% sin agrupar
  (F-1018, correlación); **el seguro de vida no aportó a la retención en ese agrupamiento**; en planes de salud, la rotación
  mensual es 3,4% en individuales y 2,1% en de grupo (F-1019), que es el sustituto más cercano a "plan familiar" y no
  separa dependientes.
- **Cuidado con el traslado.** "Más personas en la póliza" puede reflejar que la póliza está atada a un empleador o a un
  crédito, no que cada persona aporte valor.
- **Qué probar adentro.** Comparar retención por número de personas cubiertas, controlando por cómo se contrató.

### HD5 — La llave de entrada por cartera 🟡

- **El siniestro es el momento de mayor influencia reportada:** buena experiencia de siniestro y buen servicio son los
  principales motores de retención en EE.UU. (F-1022); en 2010, entre los siniestrados muy satisfechos 71% "definitivamente
  renovaría" frente a 53% en los poco satisfechos. Capgemini halla que la mitad de los asegurados de vida está decepcionada y
  que 23% se queja de no poder hacer cambios por autoservicio (F-1021).
- **Límite.** Son intenciones declaradas y datos antiguos; no demuestran que el siniestro sea la mejor "llave" para activar.
  Que la gran mayoría nunca tenga siniestro (F-1020) deja fuera a casi todo el cliente.
- **Qué probar adentro.** Qué evento (alta, renovación, siniestro, consulta) activa a cada cartera, y cuál predice mejor que
  el cliente se quede.

### HD6 — El canal de venta se mueve, pero no igual 🟡

- Para autos, los proveedores de seguro embebido en concesionarias afirman que Deloitte proyecta 20% de las compras de seguro
  de autos en concesionaria a 2030 y que 35% de los clientes está interesado (F-1024); son cifras de vendedores de la
  tecnología. **No se halló retención de pólizas vendidas en concesionaria.**
- Lo único medido sobre canal digital es la **iniciación de la venta** (F-1023).
- **Qué probar adentro.** Retención por canal de origen con producto constante (§6.1).

### HD7 — En bancaseguros, el producto pesa más que el canal 🟡

- **A favor de "el producto":** en la India, la persistencia fue 65,4% con alta participación de bancaseguros y 60,2% con alta
  de agencia, y el regulador atribuyó el peor desempeño de los corredores corporativos no bancarios a malas ventas; el seguro
  temporal tuvo la mayor caducidad y las pensiones la menor (F-1016). Son datos de hace más de diez años.
- **Lo que sugiere el diseño del producto (inferencia).** Los seguros de vida ligados a crédito crecieron mucho en LATAM
  (F-1017); si el seguro termina con el crédito, la baja no es una decisión de canal. **No se halló dato de retención tras el
  pago del crédito.**
- **Perú:** no se halló participación del canal ni persistencia. Fuente primaria pendiente: estadísticas de primas por canal
  de la SBS y de APESEG. El cambio que hizo opcional el desgravamen en 2025 (F-877) podría servir como experimento natural
  (§6.1).

### HD8 — Lo que determina la actividad es el producto 🟢

- **Es la hipótesis con mejor apoyo público (estructural).** Un asegurador típico recibe unas dos o tres solicitudes de información
  por cliente al año; los siniestros son seis por cien asegurados-año en autos y menos de uno por cien en vida (F-1020). Un
  informe de 2007 halló que 71% de los clientes rara vez o nunca interactuaba con su distribuidor, frente a más de 200
  interacciones anuales en banca.
- **Límite.** Son datos de 2007 y de un análisis de una consultora. Que el producto fije la frecuencia no implica que un
  diseño no pueda crear ocasiones de uso; lo que muestra es que **hay que traer el valor, no solo la app**.
- **Qué probar adentro.** Actividad digital por producto con canal constante, y lo inverso (§6.1).

### HD9 — A quién acude el cliente depende del producto 🔴

- Solo hay señales de banca: quienes no tienen una tarjeta principal tienen más probabilidad de irse (17% frente a 7% en 12
  meses; F-1015, de un proveedor de pagos). Sugiere que el **producto ancla la relación**. No hay nada equivalente en seguros.
- **Qué probar adentro.** Ruta de contacto (quién llama a quién, y por qué) por tipo de producto.

### HD10 — Madurez digital distinta por ramo 🟡

- La oferta digital por ramo se conoce (movilidad concentra 39% de las insurtech de Centroamérica y el Caribe, y vida y salud
  31%; F-1029); lo que no se conoce es la **adopción por ramo** en LATAM ni en Perú. En Perú hay indicios de contexto (SOAT ~90%
  digital, F-884; Yape con seguro de salud, F-888).
- **La distinción "no funciona" frente a "no se intentó"** es clave y no se resuelve con fuentes públicas: exige saber qué se
  ofreció en cada ramo.

---

## 5. Recurrencia: cómo la capitalizan otros y en qué indicador aterrizan

La pregunta es qué valor de negocio se le atribuye a que el cliente vuelva a interactuar y cómo se mide. Lo hallado:

| Actor | Dónde aterriza el valor | Indicador | Fuente | Cómo leerlo |
|---|---|---|---|---|
| Lemonade | Costo de adquirir frente a prima recurrente | US$1 de marketing por más de US$2 de prima en vigor (2020); valor de vida del cliente sobre su costo | F-1026 | Autodeclarado por la empresa |
| Discovery Vitality | Menos caducidad entre inscritos | Tasa de caducidad de Vitality 3,5% (2018-19), 4,0% y 6,9% | F-1027 | Cifra de la empresa; sin comparación causal |
| AIA Australia | Menos caducidad | 40% menos entre inscritos | F-1027 | Mezclado con su modelo de precios |
| Banca (McKinsey) | Más productos por cliente y menor costo de servir | 1,6 productos frente a 0,5 en 12 meses | F-1014 | Correlación en Asia; 2017 |
| Banca (Visa y RFi) | Producto ancla | 17% frente a 7% de probabilidad de irse | F-1015 | Proveedor de pagos |
| Banca (BCG) | Alerta temprana | Menos ingresos a la app, menor volumen de pagos | F-1015 | Recomendación, no medición |
| Capgemini (vida) | Experiencia | +38% de NPS, −11% de razón de gastos y +6% de crecimiento de ingresos de los mejores frente al resto | F-1021 | Cifras de la consultora; no causal |
| J.D. Power (hogar y auto) | Agrupar productos | Retención de 95% frente a 85% | F-1018 | Correlación |

**Lectura.** Los indicadores donde se aterriza son cuatro: **caducidad o persistencia, productos por cliente, costo de servir
y prima en vigor por costo de adquisición**. **Ninguna cifra separa el efecto de la recurrencia de la selección de clientes**;
por eso "la vara que hoy no tenemos" no se encuentra afuera: se construye adentro con una cuenta que sume el cambio en
retención por margen, el cambio en ventas cruzadas y el cambio en costo de servir (inferencia mía, a validar con las áreas
financiera y actuarial). La decisión de si la recurrencia vale la inversión es del negocio, no de la investigación.

---

## 6. Cómo probarlo con dato propio (propuestas de diseño; razonamiento mío)

### 6.1 Principios

1. **Separar poblaciones.** El cliente antiguo y el que se activa al contratar son grupos distintos; sumarlos en un solo
   número mezcla dos fenómenos.
2. **Comparar parecidos.** Emparejar adoptantes y no adoptantes en las características previas (edad, producto, antigüedad,
   prima, historial de siniestros) y, si la adopción ocurre en momentos distintos, usar diferencias en diferencias
   escalonadas (el diseño de F-1011, no verificado).
3. **Producto constante, canal variable; y al revés.** Es la forma de separar HD7 y HD8: misma póliza por distintos canales, y
   mismo canal con distintos productos.
4. **Supervivencia, no solo tasa.** Medir cuánto tarda en caducar, con la activación como variable que cambia en el tiempo, y
   separar caducidad, siniestro y vencimiento del contrato.
5. **Experimentos naturales.** Fecha de lanzamiento de una app, campañas por cohorte, cambios regulatorios (desgravamen
   opcional, F-877).
6. **Probar la mejor versión del mecanismo, no solo una correlación.** Un nudge de activación aleatorizado por cartera
   (el único tipo de evidencia que cierra la discusión de selección, F-1028).

### 6.2 Qué hipótesis admite cada diseño

| Hipótesis | Diseño preferente | Qué la refutaría |
|---|---|---|
| HD1 | Segmentación de la cartera sin digitalizar y oferta mínima en muestra | Que, ofreciéndoles algo, la activación siga cerca de cero |
| HD2 | Emparejamiento y diferencias en diferencias | Que el efecto desaparezca al comparar parecidos |
| HD3 | Embudo y supervivencia con activación variable | Que la activación no cambie con el producto |
| HD4 | Retención por personas cubiertas, controlando cómo se contrató | Que el efecto desaparezca al controlar por canal y empleador |
| HD5 | Comparar eventos que activan por cartera | Que el siniestro no prediga permanencia |
| HD6 | Retención por canal de origen con producto constante | Que el canal no cambie la retención |
| HD7 | Producto constante y canal variable; experimento natural del desgravamen | Que el canal explique la baja más que el producto |
| HD8 | Canal constante y producto variable | Que el canal explique la actividad más que el producto |
| HD9 | Rutas de contacto por producto | Que todos los productos usen la misma ruta |
| HD10 | Madurez por ramo con registro de qué se ofreció | Que "no se intentó" explique la baja adopción |

---

## 7. Qué más se puede investigar afuera (siguiente barrido)

En orden de valor, pensado para no repetir lo que ya está en los nodes:

1. **Fuente primaria para Perú:** estadísticas de la SBS sobre primas por canal y persistencia por producto, y reportes de
   APESEG. No se alcanzaron en esta corrida.
2. **Evidencia causal en banca digital:** localizar el estudio de diferencias en diferencias de un banco español (F-1011) y
   buscar otros con lanzamiento escalonado de app; en seguros, estudios de lanzamiento de portal o app con cohorte de control.
3. **Ping An y otros grandes del seguro digital:** ventas cruzadas por cliente y retención (no se halló en esta corrida).
4. **Dependientes y familia:** estudios sobre retención por número de personas cubiertas (salud y vida).
5. **Persistencia tras el crédito en seguros ligados a crédito** en Brasil, Chile y Colombia (superintendencias y aseguradoras).
6. **Experimentos de activación en seguros** (no en fintech de proveedores): qué momento del alta mueve el primer uso.
7. **Lo cualitativo:** qué dicen asegurados peruanos de su relación con el seguro después de contratar (el node de foresight
   ya cubre la percepción de IA, no la de recurrencia).

---

## 8. Limitaciones

- **Lectura por resúmenes.** Ningún informe se abrió completo.
- **Predominan proveedores y consultoras**, con incentivo para mostrar que lo digital retiene (F-1007, F-1008, F-1024, F-1025).
- **Datos antiguos** en varias piezas (frecuencia de contacto de 2007; persistencia india de 2014; satisfacción con
  siniestro de 2010 y 2014).
- **Cero fuente peruana** sobre canal y persistencia.
- **Pista social no corrida.** Las hipótesis son sobre conducta que se mide en datos, no sobre discurso; la percepción
  social de la IA ya está en el node de foresight. Es una decisión mía; si se prefiere, se puede correr.
- **F-1011** es un extracto sin título ni autoría verificados; se usa solo como pista de método.
- **El experimento de Illinois** es de programas de bienestar laboral, no de seguros: el traslado a la selección en apps
  es una analogía, no un resultado.
- **Se omiten adrede las cifras del estudio interno** (repositorio público): no se contrastaron aquí con la evidencia
  externa, solo se reformularon sus preguntas.

---

## Conexiones

- [[digitalizacion-seguros-mercados-emergentes|Digitalización en seguros en mercados emergentes]] — node raíz del que
  se hace doble clic (definiciones basales de fidelidad y alto valor, §5b).
- [[foresight-experiencia-futura-seguros-digitalizacion|Foresight: la experiencia futura de los seguros y la digitalización]] —
  qué experiencias futuras hacen más o menos relevante medir recurrencia.
- [[economia-conductual-seguros-literatura|Economía conductual de los seguros]] — inercia, selección y confianza que
  condicionan fidelidad y activación.
- [[venta-vida-digital-hibrida-latam|Venta de vida digital vs. híbrida en LATAM]] — canal digital, híbrido y bancaseguros
  en la región.
- [[lealtad-gamificacion-recompensas-retail|Gamificación, recompensas y lealtad en retail]] — por qué no apostar por
  recurrencia inducida sin prueba causal.
