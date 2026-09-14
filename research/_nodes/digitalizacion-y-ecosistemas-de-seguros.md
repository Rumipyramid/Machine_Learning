# Digitalización de seguros y ecosistemas de seguros — estado del arte + bench 2026

*Node de investigación · creado 2026-09-14 · v1.0*
*Investigación: `/seeker` (registro empírico + teórico/crítico) + bench de negocio 2026.*
*Fuentes: F-469 a F-505 del ledger de `cronista` (`research/fuentes/codice.md`).*

---

## 0. Veredicto

**Las "mejores prácticas" de digitalización de seguros que circulan como consenso están mucho
peor respaldadas que su nivel de circulación.** Hay evidencia académica sólida de que digitalizar
**sí** mueve la eficiencia técnica — pero en forma de **curva en U**, no de escalera: el tramo
inicial *destruye* productividad antes de crearla (F-472). Y hay evidencia de industria de que,
agregando 20 años, el sector **subió el gasto en TI sin mejorar sus ratios de costo** (F-486).

Sobre **ecosistemas**, el veredicto es más duro: la teoría que los sostiene es sólida y canónica
(F-470), pero la **evidencia de que las aseguradoras los ejecuten bien es escasa, mayormente
cualitativa o de consultora, y la cifra más citada en contra (`<5% de aseguradoras son ecosystem
masters`) resulta ser un artefacto de definición, no una medición de desempeño** (F-488). El
único caso longitudinal académico disponible es un N=1 cualitativo (F-475).

En 2026 el dinero ya no discute esto: **el 99,1% del capital insurtech del 2T-2026 fue a
compañías de IA** (F-491) y el mercado público premia rentabilidad de suscripción, no crecimiento
digital (F-494 vs. F-495).

> **Regla operativa que sale de este node:** al defender una inversión de digitalización, no cites
> la tasa de fracaso del 70% (no existe, F-477), ni cifras de STP de proveedores (F-504), ni
> proyecciones de *embedded insurance* (las casas de research difieren 2x **para el mismo año**,
> F-503). Lo que sí resiste escrutinio está en §4.

---

## 1. Registro empírico: qué está efectivamente documentado

### 1.1 El efecto de digitalizar no es lineal — es una curva en U

El hallazgo con mejor diseño disponible: sobre **76 aseguradoras chinas, 2011-2020**, la relación
entre índice de transformación digital y **productividad total de factores es en forma de U**
(F-472 — 🟢 peer-reviewed, *The Geneva Papers on Risk and Insurance*). Es decir: **a niveles bajos
de digitalización la PTF primero cae**, y solo después de superar un umbral empieza a subir.

Esto no es un detalle técnico. Reencuadra por completo la conversación de negocio:

- Un programa de digitalización medido a 12-18 meses puede mostrar **deterioro real de
  productividad y aun así estar en la trayectoria correcta**.
- Simétricamente, **un programa que se detiene a mitad de la U termina peor que si no hubiera
  empezado** — el costo se incurrió, el beneficio está del otro lado del umbral.
- Ninguna de las "mejores prácticas" de consultora que revisé incorpora esta forma funcional.
  Todas presentan el retorno como monótono creciente.

⚠️ **Calibración:** muestra 100% china, panel de aseguradoras cotizadas o grandes. **Validez
externa hacia Perú: baja-media.** El mecanismo (costo de absorción antes del beneficio) es
plausiblemente universal; el umbral numérico no es trasladable.

Converge con esto, por otro camino metodológico: sobre **88 aseguradoras chinas, 2012-2023**, con
SBM-DEA para medir eficiencia técnica y una batería inusualmente seria de identificación causal
(efectos fijos + variable instrumental + diferencias-en-diferencias + *double machine learning*),
la aplicación de tecnología de *big data* **sí eleva significativamente la eficiencia técnica**
(F-473 — 🟢 peer-reviewed, *Finance Research Letters*). Es la mejor evidencia causal del node a
favor de digitalizar.

Y en solvencia, sobre **39 aseguradoras chinas 2016-2023** con efectos fijos + PSM, la innovación
insurtech muestra efecto positivo (F-474 — 🟢 peer-reviewed, revista de menor tier).

> **Sesgo de corpus que hay que declarar:** las tres fuentes con identificación causal seria del
> estado del arte son **de China**. No encontré equivalente peer-reviewed con panel europeo,
> estadounidense ni latinoamericano. Eso no invalida el hallazgo — lo hace **provisional y
> geográficamente concentrado**, exactamente el tipo de sesgo que este proyecto ya documentó en
> otro dominio (ver `tendencias-diseno-innovacion.md`).

### 1.2 La contraevidencia agregada: la paradoja de productividad del seguro

Contra lo anterior juega un dato de industria, no académico, pero difícil de esquivar: entre
**2012 y 2017 el gasto en TI como porcentaje del costo operativo subió 24% en P&C y 12% en vida,
y los ratios de costo globales no mejoraron** (F-486 — 🟡 C, McKinsey). La misma casa reporta que,
a escala global, **las primas crecieron ~4,9% anual desde 2005 hasta ~US$8,3 billones en 2025,
pero la utilidad antes de impuestos creció solo ~4,3%: veinte años sin mejora de rentabilidad ni
de eficiencia** (F-485).

McKinsey señala además que **los esfuerzos de contención de costos vía canales digitales u
outsourcing "a menudo resultaron inefectivos"** para mejorar el desempeño global (F-486). Esto es
notable porque proviene de una firma cuyo negocio es vender transformación: **es contraevidencia
emitida por una parte interesada en la dirección contraria**, lo que le sube el peso.

**Cómo se reconcilian §1.1 y §1.2:** no se contradicen. La curva en U predice exactamente esto —
un sector en el que la mayoría de los actores está en el tramo descendente o cerca del mínimo
arroja, agregado, "gasto arriba, eficiencia plana". La lectura honesta no es "digitalizar no
sirve" ni "digitalizar sirve", sino **"la mediana del sector no ha cruzado el umbral"**.

### 1.3 Dónde sí aparece señal de desempeño (y por qué hay que descontarla)

La cifra más atractiva del año: las aseguradoras con analítica más sofisticada habrían logrado
**combined ratio 6 puntos porcentuales menor y crecimiento de primas 3 pp mayor** entre 2022 y
2024 frente a los adoptantes lentos (F-489 — 🟡 C, encuesta WTW 2026).

⚠️ **Calibración — esta cifra no debe usarse como afirmación fuerza causal:**
- Es **correlacional y transversal**, con autoclasificación del nivel de sofisticación analítica.
- Tiene **causalidad reversa evidente**: las aseguradoras con mejor combined ratio tienen más
  margen para invertir en analítica. El sentido de la flecha no está identificado.
- El proveedor de la encuesta **vende servicios de analítica**.
- No es auditable: método y muestra no están completamente publicados.

Úsala como *señal direccional consistente con F-473*, nunca como "6 puntos de combined ratio".

En la misma línea, Grant Thornton (950 ejecutivos de seguros, 2026): **52% reporta crecimiento de
ingresos atribuido a IA y 62% mejores insights de decisión — pero 44% reporta que problemas de
gobernanza o cumplimiento contribuyeron al fracaso o bajo desempeño de proyectos de IA** (F-490).
Ese 44% es, para efectos prácticos, el hallazgo más accionable de toda la encuesta: **el cuello de
botella declarado ya no es el modelo, es la gobernanza**.

### 1.4 Incumbentes vs. entrantes: usan la misma tecnología para cosas distintas

Hallazgo cualitativo pero robusto y repetido: **los entrantes usan IA, big data y digital para
construir servicios nuevos** (features de producto, valor y experiencia del cliente), mientras que
**las aseguradoras establecidas usan la tecnología defensivamente**: mejorar servicios existentes
y canales de distribución existentes (F-476 — 🟢 peer-reviewed).

Esta es la diferencia estructural que más importa para una aseguradora tradicional: **el mismo
presupuesto de tecnología produce resultados distintos según si financia el negocio que ya existe
o uno que todavía no existe.** Y conecta con la curva en U: digitalizar defensivamente es
precisamente la forma de **quedarse en el tramo descendente** — se paga el costo de absorción sin
cambiar el modelo que justificaría el beneficio.

### 1.5 Cuánta digitalización hay realmente (línea base regulatoria)

EIOPA, sobre el sector europeo: **~50% de las aseguradoras de no-vida y ~24% de las de vida usan
IA** en operaciones (F-478 — 🔵 B, supervisor con metodología documentada). Su encuesta en curso
sobre IA generativa arroja adopción rápida **concentrada en back-office**: resumen de documentos,
herramientas internas, asistencia de código (F-479).

Dato incómodo para el relato dominante: **la adopción real de GenAI está en el back-office, no en
la experiencia del cliente ni en la suscripción**, que es donde se promete el valor.

---

## 2. Ecosistemas de seguros: teoría sólida, evidencia floja

### 2.1 La teoría canónica (y qué exige de verdad)

La referencia obligada es Jacobides, Cennamo & Gawer (2018), *Towards a Theory of Ecosystems*,
*Strategic Management Journal* (F-470 — 🟢 peer-reviewed, canónica). Su tesis central: **la
modularidad es lo que permite que un ecosistema exista** — hace posible que organizaciones
distintas e interdependientes coordinen **sin jerarquía ni contratos completos**, mediante
complementariedades no genéricas.

Consecuencia que casi todo el material de industria omite: **si tu producto y tus procesos no son
modulares, no tienes un ecosistema, tienes un conjunto de convenios comerciales.** La modularidad
no es un "enabler técnico" opcional; en esta teoría es la **condición de existencia**.

El propio Jacobides es de los críticos más duros del hype: señala que hay "más confusión que
claridad" y "demasiadas definiciones", que **"los ecosistemas tienden a ser mucho menos abiertos
de lo que se anuncian"**, y usa el fracaso de **GE Predix** como caso: quiso ser todo para todos,
olvidando que un ecosistema necesita **propuesta de valor clara para el cliente final Y para el
complementador**, y gestionó mal los incentivos de estos últimos (F-505 — 🟠 D, entrevista).

### 2.2 La tasa de fracaso: qué dice realmente el estudio de BCG

La cifra que circula como "85% de los ecosistemas fracasan" proviene de Pidun, Reeves & Schüssler
(BCG, 2019): **menos del 15% de los ecosistemas de negocio son sostenibles en el largo plazo**, y
del análisis de **110 ecosistemas fracasados** en varias industrias, **más de un tercio de los
fracasos se explica por el modelo de gobernanza** (F-487 — 🟡 C).

⚠️ **Chequeo de eco de cita:** el "85%" que circula es **la inversa aritmética del <15%**, no una
cifra publicada. Y la muestra de 110 es **una muestra de fracasos** (seleccionada por el
resultado), no una muestra aleatoria de ecosistemas de la que se derive una tasa. **La afirmación
defendible es "más de un tercio de los fracasos observados fue por gobernanza", no "85% fracasa".**

### 2.3 El artefacto definicional de Accenture (importante)

La otra cifra omnipresente: **menos del 5% de las aseguradoras son "ecosystem masters"**, segunda
peor industria entre doce analizadas (F-488 — 🟡 C, 106 ejecutivos de seguros dentro de 1.250
líderes de negocio).

Al rastrear la definición, resulta que "ecosystem master" se define como la empresa que **(a)
aspira a disrumpir su industria vía ecosistemas, (b) planea liderar tantos ecosistemas como sea
posible, y (c) apunta a ≥5% de crecimiento vía ecosistemas**.

**Los tres criterios son de intención declarada, no de desempeño.** El "<5%" no mide que las
aseguradoras ejecuten mal los ecosistemas: mide que **pocas aseguradoras declaran una ambición
maximalista** — que es, plausiblemente, una postura sensata dada la evidencia de §2.2. Citar este
dato como prueba de incapacidad del sector es una **sobreinterpretación del instrumento**.

(En la misma encuesta, 84% de los ejecutivos de seguros dice que los ecosistemas son importantes
para su estrategia y 54% busca activamente oportunidades — es decir, el problema declarado no es
desinterés.)

### 2.4 El único estudio académico longitudinal de un ecosistema de seguros

Oruganti (2025), *Information Systems and e-Business Management* (F-475 — 🟢 peer-reviewed,
**cualitativo longitudinal, N=1**): sigue a una aseguradora de vida implementando una estrategia
de transformación digital *top-down* y creando un **ecosistema de seguros basado en recompensas**.

Sus tres acciones que definen la formación del ecosistema:
1. **Cambios en los elementos del modelo de negocio** (no en el canal — en el modelo).
2. **Identificar y alinear socios del ecosistema** a esos cambios estratégicos.
3. **Cambiar los modelos operativo y de gobernanza** en consecuencia.

Habilitadores: **enfoque modular del servicio de seguros** y capacidad de **combinar y recombinar
(*mix-and-match*) el paquete de servicios complementarios y recompensas**, distinguiendo
complementadores **centrales** de **periféricos**.

⚠️ N=1, cualitativo, sin grupo de comparación y sin outcome financiero reportado. **Sirve para
generar hipótesis sobre la secuencia correcta, no para estimar retorno.** Nótese que confirma
independientemente el requisito de modularidad de F-470.

### 2.5 Ping An: el caso testigo, con su matiz

Ping An es el ejemplar citado universalmente. Sus cifras de 1S-2026 (F-493 — 🟡 C, reporte de
compañía, no auditado independientemente):

- **RMB 88.700 millones** de primas de salud, incluidos >RMB 43.000 millones de seguro médico (+4,9% i.a.).
- **18,3 millones de clientes de Ping An Life (38,5%) usaron servicios de salud y senior care**,
  incluido el **71% de los recién incorporados**.
- **Prima de primer año por póliza 1,5x mayor** en clientes de *health care* y **5,2x mayor** en
  clientes de *home-based senior care*; +4 pp en tasa de *upsell*.
- Ping An Good Doctor: **90 millones de usuarios activos mensuales**; la unidad de salud y
  tecnología reportó utilidad de RMB 379,5 millones (+366,1% i.a.).

⚠️ **Lo que estas cifras no prueban:** el "5,2x" es una **comparación entre clientes que eligieron
usar servicios de senior care y los que no** — es autoselección pura. Los clientes que contratan
cuidado domiciliario para adultos mayores son, casi por construcción, más ricos y más
comprometidos. **No es el efecto causal del ecosistema; es el perfil de quien lo usa.** Es la
misma trampa metodológica que este proyecto ya documentó en Vitality/Discovery
(`mecanismos-seguros-salud.md`).

Lo que sí es defendible de Ping An: **la cobertura** (38,5% de la base, 71% de los nuevos) es un
dato de penetración real, no autoseleccionado por outcome, y es un orden de magnitud que ninguna
aseguradora occidental reporta.

---

## 3. La capa teórica que cambia la interpretación de todo lo anterior

Buscar solo en el registro empírico deja fuera la discusión que **cambia qué cuenta como "mejor
práctica"**.

### 3.1 Del pool al perfil (Cevolini & Esposito, 2020)

*From pool to profile: Social consequences of algorithmic prediction in insurance*, *Big Data &
Society* (F-471 — 🟢 peer-reviewed, teórico/sociológico, canónico del debate).

Tesis: **para el seguro, la incertidumbre compartida es un recurso, no un defecto.** El seguro
existe porque nadie sabe a quién le va a tocar. Si la predicción algorítmica permite conocer la
exposición individual, **el precio deja de referirse a un pool y pasa a referirse a un perfil** —
y con eso se erosiona el principio mismo de mutualización sobre el que el producto está
construido. Los autores advierten que el razonamiento de *pay-as-you-drive / pay-how-you-drive*
puede **contradecir el significado fundamental del seguro**, produciendo nuevas formas de
discriminación y exclusión de cobertura.

**Por qué esto importa para "mejores prácticas" y no es filosofía decorativa:**
la personalización extrema —que todo el material de industria presenta como el fin último de la
digitalización— **no es una mejora incremental del mismo producto: es un cambio de producto.**
Llevada al límite, el seguro deja de vender transferencia de riesgo mutualizado y pasa a vender
un servicio de precio individualizado, que es un negocio distinto, con distinta base de
legitimidad social y distinta exposición regulatoria (§6.5).

Eling & Lehmann (2018) llegan al mismo lugar desde la economía del seguro: entre las tres áreas de
cambio sobre la **asegurabilidad** identifican el efecto de "información nueva y más abundante
sobre la asimetría de información y el *risk pooling*" (F-469 — 🟢 peer-reviewed, revisión de 84
papers y estudios de industria, *Geneva Papers*). Su marco de cuatro tareas de la industria
—mejorar la experiencia del cliente, mejorar procesos, ofrecer productos nuevos y prepararse para
competir con otras industrias— sigue siendo **la mejor taxonomía disponible** para ordenar un
programa de digitalización, ocho años después.

### 3.2 La consecuencia práctica

Quien construye un ecosistema de datos alrededor de la póliza está, quiéralo o no, empujando la
frontera pool→perfil. La evidencia de consumidor de 2026 (§6.7) sugiere que **el público percibe
esa frontera y reacciona**: la confianza en el uso de IA por parte de aseguradoras **cayó de 46% a
40% en un año**, mientras la confianza en el manejo de datos personales se mantiene en 71%
(F-492). La gente no desconfía de que le guarden los datos; desconfía de **qué decisión se toma
con ellos**.

---

## 4. Mejores prácticas, ordenadas por fuerza de respaldo

| # | Práctica | Respaldo | Nivel de evidencia |
|---|---|---|---|
| 1 | **Modularizar producto y servicio antes de buscar socios** — sin modularidad no hay ecosistema, hay convenios | F-470 (canónica), F-475 (caso) | 🟢 Teórico canónico + caso confirmatorio |
| 2 | **Diseñar la gobernanza del ecosistema antes del lanzamiento** — es la causa #1 de fracaso observada | F-487 (>1/3 de 110 fracasos), F-490 (44% de fracasos de IA por gobernanza/compliance) | 🟡 Industria, pero dos fuentes independientes convergen |
| 3 | **Presupuestar el valle de la U**: esperar deterioro de productividad antes de la mejora, y no cortar el programa ahí | F-472 | 🟢 Peer-reviewed, panel; ⚠️ China |
| 4 | **Que la tecnología financie modelo nuevo, no defensa del canal existente** | F-476, F-486 | 🟢 + 🟡 convergentes |
| 5 | **Empezar por datos y analítica de suscripción/siniestros, no por la capa de experiencia** | F-473 (causal), F-489 (correlacional) | 🟢 causal + 🟡 direccional |
| 6 | **Gobernanza de IA con testeo cuantitativo de discriminación, por diseño** — ya es obligación legal en varias jurisdicciones | F-479, F-480, F-481 | 🔵 Regulatorio (obligatorio, no opcional) |
| 7 | **Modelo híbrido digital-con-humano como default, no digital puro** | F-492 (solo 15% quiere 100% autoservicio; 87% valora el agente humano) | 🟡 Encuesta; converge con `futuro-asesores-seguros-venta-digital.md` |
| 8 | **Medir cobertura del ecosistema (penetración en la base), no solo el diferencial de los usuarios** — evita autoselección | F-493 leído críticamente | 🟠 Inferencia metodológica propia |
| 9 | **Tratar el diseño de claims del producto embebido como parte del producto** — la facilidad de compra sin facilidad de siniestro es el patrón de daño ya identificado por el regulador británico | F-483 | 🔵 Supervisor |

---

## 5. Lo que NO hay que citar (cifras contaminadas)

### 5.1 "El 70% de las transformaciones digitales fracasa" — **no existe**

Rastreo de la cadena: el número viene de **Hammer & Champy (1993)**, *Reengineering the
Corporation*, donde escriben que entre 50% y 70% de los esfuerzos de reingeniería no lograron
resultados, **calificándolo ellos mismos de "estimación no científica"**; para 1995 Hammer lo
estaba retractando, escribiendo que no hay tasa de fracaso inherente a la reingeniería. Mark
Hughes rastreó la narrativa del "70% del cambio fracasa" a través de cinco fuentes publicadas
distintas **y no encontró evidencia empírica detrás de ninguna**. La variante moderna (70% +
"US$900.000 millones perdidos") rastrea a **una columna de Forbes de 2018 firmada por un ejecutivo
de software**, no a un estudio (F-477).

**Es un huérfano de cita**, exactamente el defecto que `tendencias-diseno-innovacion.md` tipificó
como regla C22. El sustituto legítimo, si se necesita una cifra: **~48% de los proyectos cumple o
supera sus objetivos** (Gartner, vía la misma trazabilidad — 🟠 D, verificar antes de usar).

### 5.2 Las cifras de STP y automatización de siniestros de proveedores

Circulan como "benchmarks": *claims* de 72 horas a menos de 5 minutos; ajustadores que pasan de
10-15 a 50+ casos diarios; 70-90% de STP en siniestros de baja complejidad; "hasta 70% de ahorro
de costos"; un caso de 51 segundos (F-504 — 🔴 E).

**Todas provienen de blogs de proveedores que venden exactamente eso**, sin muestra, sin línea
base, sin identificación de la aseguradora y sin auditoría. No son benchmarks: son material de
venta. **No usar en un caso de negocio interno.** Lo mismo aplica a la afirmación de que la IA
agéntica produce "3 a 5 puntos de mejora en loss ratio".

### 5.3 Las proyecciones de mercado de *embedded insurance*

Para **el mismo año 2026**, las casas de research publican: **US$138.080 millones**, **US$176.350
millones** y **US$188.500 millones**. Al horizonte 2033-2035: US$1,24 billones, US$1,46 billones y
US$2,07 billones (F-503 — 🔴 E como conjunto).

**Una dispersión de ~1,4x en el año base y de >1,6x en el terminal, para el mismo objeto, es
señal de que la categoría no está definida de forma comparable entre metodologías.** Citar
cualquiera de estas cifras como "el tamaño del mercado" es citar una definición propietaria, no
un hecho. La cifra de McKinsey para Asia (~US$170.000 millones de no-vida embebido hacia 2030,
F-485) tiene el mismo problema, con mejor reputación de emisor.

---

## 6. BENCH 2026 — qué está pasando de verdad este año

### 6.1 El capital: la IA se comió el insurtech

Gallagher Re, **2T-2026** (F-491 — 🟡 C, la serie de referencia del sector):

| Métrica | 2T-2026 | Lectura |
|---|---|---|
| Financiamiento total | **US$2.440 M** | Máximo desde 2T-2022 |
| Número de operaciones | **107** | Máximo desde 1T-2024 |
| **Share a compañías de IA** | **99,1%** (US$2.420 M en 95 deals) | Venía de 95,2% en 1T-2026 |
| Rondas >US$5 M | **100% a compañías de IA** | Sin excepciones |
| Deals ≥US$100 M | US$1.670 M (**68,4%** del total) | Mejor trimestre de mega-rondas desde 4T-2021 |
| **Etapa temprana** | **−51,8% t/t** (US$548,5 M → US$264,2 M) | ⚠️ La señal contraria |
| Inversiones de (re)aseguradoras | 27 (vs. 32 en 1T) | Corporativo enfriándose |

**La lectura correcta no es "el insurtech volvió".** Es que **el capital se concentró
brutalmente**: récord de cuatro años en total, con el *pipeline* de etapa temprana partido a la
mitad en un trimestre. Eso es un sector financiando **infraestructura de IA para aseguradoras
existentes**, no retadores nuevos. Coincide con la lectura de que el insurtech pasó de disrupción
a infraestructura.

### 6.2 Las públicas: la divergencia que define el año

| Compañía | Resultado 2026 | Lectura |
|---|---|---|
| **Hippo** | Utilidad neta **US$10 M** en 2T-2026, ingresos +23,4% a US$145 M, **combined ratio 95,8%** (−4 pp), **quinto trimestre rentable consecutivo** (F-494) | El caso que sí cerró |
| **Lemonade** | 2T-2026: ingresos **US$294,4 M (+79%)**, *net loss ratio* 62-61%, **pérdida neta ~US$43 M**; primer trimestre de EBITDA ajustado positivo aún prometido para 4T-2026 (F-495) | Crece rápido, todavía no cierra |
| **Root** | Vuelve a pérdida estrecha (**US$5,4 M**) tras un año con utilidad (F-495) | Rentabilidad no consolidada |

**Lo que el mercado premió en 2026 es rentabilidad de suscripción, no crecimiento digital.** Hippo
—el libro más pequeño y diversificado— es el que capitaliza; Lemonade, con 79% de crecimiento de
ingresos, sigue en pérdida. Es la contraevidencia más limpia contra la tesis de que digitalizar la
distribución resuelve la economía del seguro.

### 6.3 El mercado público se reabrió (y con matices)

- **Ethos** (software de venta de seguro de vida) salió a Nasdaq (ticker **LIFE**) en enero de
  2026: ~**US$200 M** levantados a **US$19/acción**, pero **cerró su primer día en US$16,85
  (−11%)**. Fundamentales reales: **~US$278 M de ingresos y ~US$46,6 M de utilidad neta en los
  9 meses a septiembre de 2025**, rentable desde mediados de 2023 y creciendo >50% i.a. (F-496).
- **Accelerant** debutó en NYSE (ARX) con valuación de **US$6.400 M**, **+36% en el debut**,
  US$724 M levantados (F-497).
- Aspen, American Integrity, Ategrity y Slide también listaron y cotizan sobre su precio de salida.

**Matiz que importa:** Ethos es rentable y aun así abrió bajo el precio de colocación. El apetito
volvió, pero **con descuento** — y para el proyecto es relevante que Ethos ya estaba registrado en
`futuro-asesores-seguros-venta-digital.md` como el caso más sólido de venta digital de vida, con
el matiz de que **interviene un humano en los casos ambiguos**. Ese matiz sigue en pie tras el IPO.

### 6.4 La infraestructura embebida se consolidó y se financia con deuda

- **Cover Genius**: **US$100 M** de Vista Credit Partners (julio 2026), valuación **US$1.900 M**.
- **Qover**: **US$12 M** de crecimiento (CIBC Innovation Banking); **3x de crecimiento de ingresos
  hasta US$173 M de GWP** en cuatro años.
- **bolttech**: **US$640 M** acumulados; Serie C de US$147 M a valuación de **US$2.100 M** (F-498).

Señal estructural: **Cover Genius levantó capital de crédito, no equity de riesgo.** Una categoría
que se financia con deuda es una categoría con flujos predecibles — es decir, **dejó de ser
apuesta y pasó a ser negocio**, con los múltiplos que eso implica.

### 6.5 IA agéntica: producción real, pero con el foco donde nadie lo promociona

- **AIG** desplegó el asistente de suscripción con IA generativa construido con **Anthropic y
  Palantir** — el despliegue en producción más citado de 2026 (F-501).
- **RIMAC** (Perú) lanzó su **"Agentic Web"**: el sitio público deja de ser vitrina informativa y
  pasa a interpretar intención, adaptar la experiencia en tiempo real y guiar conversacionalmente.
  Incluye **el primer agente conversacional de IA generativa del sector asegurador local**.
  Liderado por Ximena Labarthe (Growth Manager de Venta Digital). Resultados reportados: **+10% de
  leads en un mes, 39% de tasa de conversión de leads y +43% de crecimiento de venta 100%
  digital** (F-500).
  ⚠️ **Cifras autorreportadas vía prensa, sin línea base ni ventana de medición publicadas.** Un
  mes no distingue efecto del lanzamiento de estacionalidad o de campaña concurrente. Es una
  señal, no una medición.
- **LATAM**: ya operan **18 insurtechs especializadas en IA agéntica** en la región (F-499).
- Pero EIOPA encuentra que la adopción real de GenAI se concentra en **back-office** (F-479), y
  Grant Thornton que **44% de los proyectos de IA falló o rindió por debajo por gobernanza o
  cumplimiento** (F-490).

### 6.6 Regulación: 2026 es el año en que la gobernanza de IA dejó de ser opcional

| Jurisdicción | Qué cambia | Fecha |
|---|---|---|
| **UE — AI Act** | La IA usada para **evaluación de riesgo y pricing en vida y salud** queda clasificada **alto riesgo**; la mayor parte del reglamento aplica desde **agosto de 2026** (F-480) | ago-2026 |
| **UE — EIOPA** | Opinión sobre **gobernanza y gestión de riesgo de IA** dirigida a supervisores nacionales: gobernanza de datos, registro, equidad, ciberseguridad, **explicabilidad y supervisión humana** (F-479) | vigente |
| **UE — FiDA** | *Open finance*: en trílogos, **adopción esperada hacia mediados de 2026**, obligaciones por fases desde 2027. Cubre **no-vida**; **excluye vida y salud** por riesgo de exclusión financiera (F-482) | 2026-2027 |
| **EE.UU. — Colorado SB21-169** | Obliga a **probar cuantitativamente** que el uso de datos externos (ECDIS), algoritmos y modelos predictivos no produce discriminación injusta. Vida desde 2023-2024; **extensión a auto y salud con plazo de cumplimiento en julio de 2026** (F-481) | jul-2026 |
| **Reino Unido — FCA** | *Value measures* y escrutinio sobre productos embebidos: baja frecuencia de siniestros, baja interacción del cliente y **alto volumen de quejas**; la causa raíz principal de las quejas es **servicio y entrega del siniestro** (F-483) | vigente |

**Síntesis:** el reglamento de Colorado convierte en obligación legal lo que la §3.1 planteaba
como problema conceptual. **La frontera pool→perfil ya no es un debate académico: es un requisito
de prueba cuantitativa.** Para cualquier aseguradora que opere modelos de pricing con datos
externos, la capacidad de *demostrar* ausencia de discriminación por clase protegida pasó de
"buena práctica" a condición de licencia.

### 6.7 El consumidor se movió en dirección contraria al hype

Encuestas de 2026 (F-492 — 🟡 C/🟠 D; ver advertencia de trazabilidad abajo):

- **La confianza en que las aseguradoras usen IA responsablemente cayó de 46% (2025) a 40% (2026)**.
- Solo **43%** confía en que la IA se use en su beneficio, contra **71%** que confía en el manejo
  responsable de sus datos personales.
- **87%** dice que tener un agente humano sigue siendo importante.
- Solo **15%** quiere una experiencia 100% digital de autoservicio; **48%** prefiere *digital-first
  con opción de hablar con alguien*.
- **61%** es más propenso a elegir un agente que **use IA** para dar servicio más rápido y personalizado.

**La lectura no es "el consumidor rechaza la IA".** Es que **acepta la IA como herramienta del
asesor y la rechaza como sustituto del asesor** — y que la confianza cae justo mientras la
adopción sube. Esto refuerza, desde el registro del consumidor, la práctica #7 de §4 y converge
con lo ya documentado en `futuro-asesores-seguros-venta-digital.md` y
`venta-vida-digital-hibrida-latam.md`.

⚠️ **Trazabilidad incompleta:** no pude verificar patrocinador, tamaño de muestra ni metodología
de estas encuestas (bloqueo de egreso del entorno). Trátense como señal direccional.

### 6.8 LATAM y Perú

- **Ecosistema regional**: **576 insurtechs activas en América Latina, +14% i.a.** (el mayor
  crecimiento desde 2023); **US$90 millones** captados en el 1S-2026, tercer semestre de mayor
  inversión desde la pandemia. La categoría que más crece es **soluciones para agentes y
  corredores tradicionales: +36% anual** (F-499).
  → **El capital regional está apostando a equipar al intermediario, no a eliminarlo.** Es el
  contrapunto local más fuerte a la tesis de desintermediación.
- **Perú**: sector asegurador en **S/ 71.150 millones** a junio 2025 (+5,1% i.a.), con proyección
  de crecimiento del producto de **2,9% para 2026**; **bancaseguros concentra el 64,19% de los
  asegurados**; primas de microseguros de **S/ 65,9 millones** contra siniestros por S/ 25,7
  millones (F-484).
  → Un mercado donde **dos de cada tres asegurados llegan por el banco** es, estructuralmente, un
  mercado ya **embebido** — el debate peruano no es si adoptar distribución embebida, sino
  **quién orquesta la que ya existe.**
- **RIMAC**: ver §6.5.

### 6.9 Consolidación

Corebridge Financial y Equitable Holdings anunciaron fusión por **~US$22.000 millones** (marzo
2026); Baldwin adquirió Cobbs Allen (US$1.410 M); Enstar adquirió Accident Fund Holdings
(US$1.590 M); Howden compró Atlantic Group (>US$500 M). En plataformas core, **Majesco se emparejó
con Akur8 y Vitech** para fusionar core, inteligencia de pricing e IA; Guidewire, Duck Creek, EIS,
Sapiens y Socotra enfrentan una vara competitiva más alta por capacidades end-to-end con hoja de
ruta de IA (F-502 — 🟠 D).

---

## 7. Contraevidencia buscada a propósito

Siguiendo el Paso 11 de `/seeker`, se buscaron explícitamente refutaciones. Lo encontrado:

1. ✅ **Contra "digitalizar mejora el desempeño"**: la paradoja de productividad del sector (F-486)
   y la forma en U (F-472). **Encontrada y es fuerte.**
2. ✅ **Contra "el modelo digital puro gana"**: Lemonade crece 79% y pierde US$43 M mientras Hippo
   capitaliza con el libro más pequeño (F-494, F-495); Ethos abre −11% pese a ser rentable (F-496).
   **Encontrada.**
3. ✅ **Contra "los ecosistemas son el futuro del seguro"**: <15% sostenibles (F-487), gobernanza
   como causa dominante de fracaso, GE Predix como caso (F-505). **Encontrada.**
4. ✅ **Contra las cifras que sostienen el discurso**: el 70% es huérfano de cita (F-477); las
   proyecciones de embedded difieren 1,4x para el mismo año (F-503); el "<5% ecosystem masters" es
   artefacto definicional (F-488). **Encontrada, y es el hallazgo más útil del ejercicio.**
5. ✅ **Contra "el consumidor quiere autoservicio"**: 15% lo quiere; la confianza en IA cayó 6 pp en
   un año (F-492). **Encontrada.**
6. ❌ **No encontrada**: evidencia pública de que una gran aseguradora europea haya **cerrado o
   castigado contablemente** una venture digital greenfield en 2025-2026. Se buscó activamente
   (Allianz, AXA, Generali) y **no apareció**; lo que aparece son salidas de portafolio
   estratégicas (Allianz-Bajaj) y resultados sólidos. **Ausencia de evidencia, no evidencia de
   ausencia**: estos castigos suelen no desglosarse en el reporte.
7. ❌ **No encontrada**: ningún estudio con identificación causal seria **fuera de China**.

---

## 8. Tabla resumen de rigurosidad

| Fuente | Tipo de evidencia | Peer review | N / muestra | Validez | Peso para el claim |
|---|---|---|---|---|---|
| F-472 — TFP curva en U | Panel econométrico | 🟢 Sí (*Geneva Papers*) | 76 aseguradoras, 2011-2020 | ⚠️ Externa baja (solo China) | 🟢 **Alto** |
| F-473 — Big data y eficiencia técnica | Panel + IV + DiD + double ML | 🟢 Sí (*Finance Research Letters*) | 88 aseguradoras, 2012-2023 | ✅ Interna alta / ⚠️ externa | 🟢 **Alto** |
| F-469 — Eling & Lehmann | Revisión sistemática + marco | 🟢 Sí (*Geneva Papers*) | 84 papers y estudios | ✅ Marco, no estimación | 🟢 **Alto (taxonómico)** |
| F-470 — Jacobides et al. | Teórico canónico | 🟢 Sí (*SMJ*) | n/a | ✅ Canónica | 🟢 **Alto (teórico)** |
| F-471 — Cevolini & Esposito | Teórico/sociológico | 🟢 Sí (*Big Data & Society*) | n/a | ✅ Canónica del debate | 🟢 **Alto (teórico)** |
| F-474 — InsurTech y solvencia | Panel FE + PSM | 🟢 Sí (tier menor) | 39 aseguradoras | ⚠️ | 🟡 Medio |
| F-475 — Ecosistema de vida | Caso cualitativo longitudinal | 🟢 Sí | **N=1** | ⚠️ Sin generalización | 🟡 Medio (genera hipótesis) |
| F-476 — Incumbentes vs. entrantes | Comparativo cualitativo | 🟢 Sí | n.d. | ⚠️ | 🟡 Medio |
| F-478/F-479 — EIOPA | Encuesta supervisora | ⚪ n/a | Sector europeo | ✅ Obligatoria, censal | 🔵 **Alto (oficial)** |
| F-481 — Colorado SB21-169 | Norma + reglamento | ⚪ n/a | n/a | ✅ Hecho jurídico | 🔵 **Alto** |
| F-487 — BCG ecosistemas | Análisis de casos | ⚪ n/a | **110 fracasos** (muestra sesgada por outcome) | ⚠️ No da tasa poblacional | 🟡 Medio |
| F-488 — Accenture | Encuesta de intención | ⚪ n/a | 106 ejecutivos de seguros / 1.250 | ❌ **Constructo: mide intención, no desempeño** | 🔴 **Bajo — no citar como capacidad** |
| F-489 — WTW analytics | Encuesta correlacional | ⚪ n/a | n.d. | ❌ Causalidad reversa evidente | 🟡 Direccional |
| F-490 — Grant Thornton | Encuesta | ⚪ n/a | 950 ejecutivos | ⚠️ Autorreporte | 🟡 Medio |
| F-491 — Gallagher Re | Serie de transacciones | ⚪ n/a | 107 deals | ✅ Hechos de mercado | 🟡 **Alto para el hecho** |
| F-492 — Encuestas de consumidor | Encuesta | ⚪ n/a | ⚠️ **no verificado** | ⚠️ Actitud declarada | 🟠 Direccional |
| F-493 — Ping An | Reporte de compañía | ⚪ n/a | Base propia | ❌ **Autoselección en el 5,2x** | 🟡 Medio (cobertura) / 🔴 Bajo (efecto) |
| F-477 — "70% fracasa" | **Huérfano de cita** | ❌ | **Ninguna** | ❌ | 🔴 **No usar** |
| F-503 — Proyecciones embedded | Research propietario | ⚪ n/a | Definiciones incompatibles | ❌ Dispersión 1,4x mismo año | 🔴 **No usar** |
| F-504 — Cifras de STP de proveedores | Material de venta | ❌ | Ninguna declarada | ❌ | 🔴 **No usar** |

**Portafolio:** 8 fuentes académicas peer-reviewed (3 con identificación causal, todas de China),
5 oficiales/regulatorias, ~12 de industria y ~10 de prensa/negocio para el bench. **Tres cifras
identificadas como contaminadas y marcadas como no citables.**

---

## 9. Limitaciones de esta búsqueda

1. ⚠️ **El entorno bloqueó el acceso directo a prácticamente todos los dominios primarios**
   (Springer, Wiley, SagePub, PMC/NCBI, BCG, Swiss Re, Geneva Association, EIOPA, IMD, Yahoo
   Finance, prensa peruana). **La evidencia se reconstruyó vía búsqueda dirigida y no por lectura
   del texto completo.** Concretamente: no leí el paper de la curva en U, ni el de Cevolini &
   Esposito, ni el informe de BCG, ni el reporte de EIOPA en su versión original. Todo lo
   reportado aquí proviene de resúmenes de búsqueda verificados por convergencia entre consultas
   independientes, no de la fuente primaria. **Descuéntese la confianza en consecuencia**, y trátese
   cualquier cifra exacta de §1-§2 como pendiente de verificación en el texto original.
2. **No se localizó el umbral numérico de la curva en U** (F-472) — el hallazgo cualitativo (hay
   un mínimo) está; el punto de inflexión, no.
3. **Geneva Association, *Digital Platform Ecosystems in Insurance* (2024)** es la fuente que más
   habría aportado a §2 y **no se pudo leer**. Queda como tarea pendiente.
4. **No hay evidencia peruana propia sobre digitalización de seguros**: lo de Perú es mercado
   agregado (F-484) y un caso de compañía autorreportado (F-500). **No existe, hasta donde
   alcanzó esta búsqueda, ningún estudio con método sobre digitalización de seguros en Perú.**
5. **Sesgo geográfico del corpus causal**: 3 de 3 estudios con identificación causal seria son de
   China. No se encontró réplica occidental ni latinoamericana.
6. **No se hizo *snowballing* hacia adelante** sobre Jacobides et al. (2018) ni sobre Cevolini &
   Esposito (2020) por el bloqueo a Scholar/Semantic Scholar. No sé si sus tesis fueron matizadas
   o refutadas después.

---

## 10. Conexiones

- [[seguros-comportamiento-mundo-peru|Comportamiento y mercado de seguros (Mundo vs. Perú)]] —
  este node aporta el lado de **oferta y tecnología** a la penetración y desconfianza que aquel
  documenta desde la demanda. La caída de confianza en IA (§6.7) es continua con la desconfianza
  estructural del asegurado peruano.
- [[futuro-asesores-seguros-venta-digital|¿Desaparecerán los asesores de seguros?]] — §6.7 y §6.8
  refuerzan su tesis: el 15% que quiere autoservicio puro y el +36% anual de insurtechs que
  **equipan** al corredor latinoamericano son evidencia nueva a favor del modelo híbrido.
  El IPO de Ethos (§6.3) actualiza su §3.7.
- [[venta-vida-digital-hibrida-latam|Venta de vida digital vs. híbrida en LATAM]] — el bench
  regional de §6.8 (576 insurtechs, US$90 M, IA agéntica) es su actualización 2026.
- [[tendencias-diseno-innovacion|Tendencias en diseño e innovación]] — §5 de este node es un caso
  de libro de sus reglas **C22 (huérfano de cita)** y de eco de cita: el "70% fracasa" y el "85%
  de ecosistemas fracasa" tienen la misma anatomía que las cifras que aquel node desmontó.
- [[mecanismos-seguros-salud|Mecanismos de seguros de salud]] — la autoselección del "5,2x" de
  Ping An (§2.5) es el mismo defecto metodológico ya documentado allí para Vitality/Discovery.
- [[behavioral-design-estado-disciplina|Behavioral design como disciplina]] — la frontera
  pool→perfil (§3.1) es la versión aseguradora de su discusión i-frame/s-frame.
- [[modelo-personas-sinteticas|Modelo de personas sintéticas (`lapuerta`)]] — §6.7 aporta
  marginales candidatas para recalibrar `apertura_datos_ia` y
  `disposicion_compartir_datos_pricing`: la confianza cayó de 46% a 40% en 12 meses.
