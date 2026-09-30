# Comportamiento de compra en redes sociales (social commerce): Mundo → LATAM → Perú, con zoom en seguros

> Documento de investigación. Fuente persistente y versionada en el repositorio.
> Fecha de elaboración: 2026-09-30 · Versión: v1.0
> Origen: `/trinidad` (pistas `seeker` + `gossiper` + `marketer` en paralelo)
> Pregunta original: ¿cómo evoluciona el comportamiento de compra en redes sociales? Datos del
> mundo con foco en LATAM y Perú (cuánto tiempo se pasa en redes evaluando productos, cuánto
> convierte cada plataforma). Luego, zoom en la compra de **seguros** a través de redes (LATAM y
> Perú).
> Fuentes registradas en `research/fuentes/codice.md` (**F-469 a F-513**), más las reutilizadas
> F-118, F-232 y F-374.
> Output derivado: `_outputs/informe-experto-social-commerce-seguros-2026-09-30.md`.

⚠️ **Nota de acceso.** El proxy de red del entorno bloqueó la lectura directa de casi todas las
fuentes primarias de este tema (datareportal.com, gwi.com, gestion.pe, infobae.com, sbs.gob.pe,
apeseg.org.pe, limra.com, loma.org, undp.org, pacifico.com.pe, opinionbox.com, AMVO). Las cifras
se reconstruyeron por **búsqueda dirigida** (fragmentos indexados de la fuente o de su cobertura
en prensa). Cada fila del códice lo declara; ninguna cifra se inventó ni se completó de memoria.
Cuando una cifra no se pudo recuperar (p. ej. los **minutos diarios en redes del Perú** en
Digital 2026), queda como hueco explícito, no como estimación.

---

## 0. Resumen ejecutivo (TL;DR)

1. **Las redes ya son el principal lugar de descubrimiento, pero no el principal lugar de cierre.**
   En Perú, 61,3% de los usuarios digitales dice que decide compras tras ver contenido en línea
   (F-477) y 57% de los compradores online ya compró alguna vez por redes (F-475). Pero el cierre
   sigue concentrado en **WhatsApp** (81% seguirá pidiendo por WhatsApp aun sin pago integrado,
   F-476) y en e-commerce/marketplace, no en tiendas dentro de la red. **TikTok Shop no opera
   oficialmente en Perú** (F-486).
2. **El tiempo en redes tocó techo en 2022 y baja en el mundo (−10%, a 2h21m/día), pero LATAM
   sigue ~1 hora por encima del promedio (3h20m+)** (F-470, F-471). Lo que crece ya no es el
   tiempo sino **la intención comercial de ese tiempo**.
3. **"Cuánto tiempo pasan evaluando productos en redes" no lo mide ninguna fuente pública.** Lo que
   sí existe: cuánta gente investiga productos en redes (31% en Facebook en 6 países de LATAM
   incl. Perú, F-479; 48% de la Gen Z global vs. 21% de boomers, F-480).
4. **Las tasas de conversión "por plataforma" que circulan (TikTok 4,7% · Instagram 2,1% ·
   Facebook 1,8%) son huérfanas de cita** (F-490): no aparecen en ninguna fuente primaria. Lo
   auditable es más modesto: leads en Meta convierten 7,72% en promedio y 5,98% en finanzas y
   seguros (F-491, EE.UU., lead ≠ venta).
5. **Seguros: las redes funcionan como vitrina y educación, no como punto de venta.** Más de dos
   tercios de los latinoamericanos empieza a buscar un seguro de vida en línea, pero la mayoría no
   lo compra por ahí (F-498); más de 60% quiere un recorrido **híbrido** (F-499). Lo que sí cierra
   por un canal digital en Perú son los productos **simples y baratos** (SOAT, microseguros, salud
   de S/9,90 en Yape: F-508, F-510). En la pista social, el tema está dominado por el **fraude**
   (SOAT falso por Facebook, falso seguro de vida por WhatsApp: F-504 a F-506).

**Convergencia/divergencia de las tres pistas:** convergen en que la red **abre** la compra y el
chat o el humano la **cierra**. Divergen en la magnitud: la pista social amplifica la idea de que
"las redes deciden 6 de cada 10 compras" (una sola encuesta repetida por ≥6 medios); la pista
empírica aclara que eso mide **intención declarada** y que la **confianza en el vendedor** es lo que
convierte la intención en compra (F-494); la pista de negocio muestra que, incluso en EE.UU., la
compra dentro de la red es ~7% del e-commerce (F-489).

---

## 1. Tipologización (Paso 1 de `/trinidad`)

| Arista | Pista | ¿Aplica? |
|---|---|---|
| ¿Cuánto tiempo y atención se dedica a redes, y cuánto de eso es evaluación de productos? ¿Qué mecanismos (confianza, reseñas, live) convierten? | 🔬 empírica/teórica | Sí: la parte académica es fuerte sobre **mecanismos** y débil sobre **LATAM/Perú** |
| ¿Qué se dice en redes y prensa sobre comprar por redes? ¿Qué narrativa domina en seguros? | 📱 social/mediática | Sí: la cobertura de prensa es abundante; Reddit y TikTok no se pudieron medir (ver §6) |
| ¿Cuánto factura el social commerce, qué plataformas ganan y con qué conversión? ¿Quién vende seguros por redes? | 📈 negocio | Sí: datos gremiales (CAPECE, AMVO, CCCE), benchmarks de pauta y casos de aseguradoras |

---

## 2. 🔬 Pista empírica/teórica (criterio de `seeker`: rigor metodológico)

**Veredicto:** 🟡 **Parcialmente sustentado.** Está bien documentado que la **confianza** (sobre
todo en el vendedor) es el mediador principal entre la exposición en redes y la intención de
compra, y que el **live commerce** aumenta ventas en marketplaces. **No** hay evidencia académica
revisada por pares que mida el **tiempo de evaluación de productos en redes** ni la **conversión
real por plataforma** en LATAM o Perú. Casi toda la evidencia mide *intención* declarada, no
compra observada.

### 2.1 Lo documentado

- **La confianza es el motor, y pesa más la confianza en el vendedor que en la plataforma.**
  Un meta-análisis de 19 estudios encuentra un efecto medio grande de la confianza sobre la
  intención de compra en social commerce (r ≈ 0,55); el efecto es mayor cuando el objeto de la
  confianza es el vendedor (Wang et al., 2022, **F-494**).
- **Qué construye esa confianza:** cantidad y calidad de reseñas, información simétrica del
  producto y **rapidez de respuesta** del vendedor. La percepción de precio justo modera el paso
  de confianza a intención (ECRA, 2024, **F-495**). ⭐ La rapidez de respuesta es la variable que
  conecta directamente con WhatsApp como canal de cierre.
- **El live commerce vende, por dos vías distintas:** una informativa (reduce la incertidumbre
  sobre el producto) y otra relacional (fortalece el vínculo con el cliente); ambas elevan las
  ventas (POM, 2025, **F-496**).
- **En LATAM, reputación y ventas van juntas de forma consistente** en e-commerce (datos de
  Mercado Libre, J. Internet Commerce 2021, **F-497**). Es la única pieza revisada por pares de la
  región encontrada; es de e-commerce, no de redes.

### 2.2 Tiempo de atención: el techo de 2022

- Global: **2h21m/día** en redes a inicios de 2026 (DataReportal, **F-470**), casi **10% por
  debajo del pico de 2022**, con la mayor caída entre adolescentes y veinteañeros (FT sobre panel
  GWI de 250.000 adultos en 50+ países, **F-471**).
- LATAM sigue muy por encima: **Brasil 3h32m, Colombia 3h22m, México ~3h20-3h30m** (**F-470**,
  vía agregadores secundarios).
- En LATAM el tiempo en línea cayó **34 minutos desde 2021**, y cerca de un tercio espera reducir
  su actividad digital (Bain, vía Americas MI, **F-472**, 🟠 D).
- **Perú:** 28,3 millones de identidades en redes (**81,6%** de la población) y 99,5% de los
  internautas usa al menos una red (**F-469**). ⚠️ **El dato de minutos diarios del Perú de
  Digital 2026 no se pudo recuperar** (datareportal.com bloqueado). El último dato oficial
  disponible es de 2022: **3h22m/día en internet**, con redes como la actividad más citada (70%)
  (Concortv, **F-473**).

### 2.3 Tiempo *evaluando productos*: el hueco

No se encontró ninguna fuente, académica o comercial, que mida **minutos dedicados a evaluar
productos** dentro de redes, ni en el mundo ni en LATAM. Lo que existe son **proxies de
amplitud** (qué porcentaje investiga en redes), no de **profundidad** (cuánto tiempo):

| Proxy | Dato | Fuente |
|---|---|---|
| Usa Facebook para investigar productos antes de comprar (6 países LATAM incl. Perú) | 31% · YouTube 28,7% · Instagram 23,4% | F-479 (🟡 C, N=1.800) |
| Usa redes para investigar marcas/productos (global) | Gen Z 48% vs. boomers 21% | F-480 (🟡 C) |
| Investiga productos en Instagram (Brasil) | 72% | F-483 (🟡 C, N=2.055) |
| Leyó recomendaciones de otros consumidores en redes (Perú) | 60,7% | F-477 (🟡 C) |

### 2.4 Lectura teórica/interpretativa

- **De "embudo" a "bucle".** La literatura de confianza (F-494, F-495) y la de live commerce
  (F-496) coinciden en que la red no reemplaza la evaluación: la **comprime**. La información del
  producto, la prueba social (reseñas) y la conversación con el vendedor ocurren en el mismo
  espacio y casi al mismo tiempo. Por eso el "tiempo evaluando" es difícil de medir: ya no es una
  etapa separada del resto.
- **Intención ≠ compra.** Todos los estudios A de esta pista miden **intención de compra**
  declarada. En el proyecto ya está documentado que la brecha entre actitud y conducta es
  estructural (ver [[seguros-comportamiento-mundo-peru]] y la variable
  `disposicion_compartir_datos_pricing` del modelo `lapuerta`). Aplica aquí con más fuerza.

### 2.5 Tabla de rigurosidad

| Fuente | Tipo | Peer review | Muestra | Rigurosidad |
|---|---|---|---|---|
| Wang et al. 2022 (F-494) | Meta-análisis | ✅ SAGE Open | 19 estudios, 20 efectos | 🟢 A (k chico; solo intención) |
| ECRA 2024 (F-495) | Encuesta + SEM | ✅ | no recuperada | 🟢 A |
| POM 2025 (F-496) | Datos observacionales de marketplace | ✅ | no recuperada | 🟢 A |
| J. Internet Commerce 2021 (F-497) | Datos de reputación-ventas en LATAM | ✅ | Mercado Libre | 🟢 A |
| FT/GWI (F-471) | Panel comercial | ❌ | 250.000 personas, 50+ países | 🟡 C |
| DataReportal (F-469, F-470) | Compilación de herramientas de pauta y paneles | ❌ | agregado | 🟡 C |

**Contraevidencia buscada a propósito:** (a) la caída del tiempo en redes desde 2022 (F-471,
F-472) contradice la narrativa de "cada vez más tiempo en redes"; (b) ningún estudio A mide
compra real en redes en LATAM, y el único regional (F-497) es de marketplace. El veredicto se
mantiene en 🟡.

---

## 3. 📱 Pista social/mediática (criterio de `gossiper`: frecuencia y validación social)

**Nivel de instalación:** 🔥 **Instalado** para "las redes deciden lo que compramos" ·
🌡️ **Tibio** para "comprar por TikTok" en Perú · 🔥 **Instalado** para el **fraude** en seguros
comprados por redes/WhatsApp.

### 3.1 La narrativa dominante y su eco

- **"6 de cada 10 peruanos decide qué comprar por redes"** aparece en Gestión, Trome, Correo,
  Revista Economía, Infobae y mas-ventas (2025-2026). ⚠️ **Todas remiten a la misma encuesta de
  Kantar Ibope Media** (F-477, F-478 como variante de Infobae). Es un **eco de cita**: 1 fuente
  y ≥6 medios. El volumen mide amplificación, no validación.
- Mismo patrón en la región: "65% compra por influencia de redes" en México (Kueski) y "51,2% de
  compradores digitales usa redes para comprar" vs. **30% que compra por redes** según AMVO
  (F-481, F-482). La diferencia no es una contradicción: son **definiciones distintas** (influye
  / usa / compra). La prensa las presenta como si midieran lo mismo.

### 3.2 La contranarrativa: "desinfluencia" y desconfianza

- **Solo 7% de los usuarios de redes en Perú confía en los grandes influencers**, y 5% en
  creadores pequeños; los amigos y la familia (28%) y las reseñas de quienes ya probaron el
  producto (23%) son las fuentes más creíbles (Ipsos Perú, **F-478**). 19% dice haber comprado
  por recomendación de un creador.
- **Los reclamos ligados a ventas por redes se triplicaron entre 2019 y 2024**, y 58,1% señala las
  redes como el canal donde es más difícil reclamar (Indecopi, **F-507**). Indecopi respondió con
  obligaciones nuevas de libro de reclamaciones para quienes venden por Instagram, Facebook y
  TikTok.

### 3.3 Seguros en la conversación social

- **La conversación sobre seguros en redes, en Perú y la región, es sobre todo de fraude:**
  SOAT falso vendido por Facebook a motociclistas (Perú, **F-504**); alertas del regulador
  colombiano y de SURA, que declara explícitamente que **WhatsApp no es canal autorizado** para
  el SOAT (**F-505**); EsSalud alertando de estafadores que cobran un "falso seguro de vida y
  sepelio" por WhatsApp a deudos identificados **en publicaciones de redes** (**F-506**).
- A eso se suma el antecedente de contacto no consentido (BBVA/Rimac ante Indecopi, **F-118**,
  ver [[transicion-venta-fria-a-opt-in]]).
- **TikTok:** hay contenido de asesores de seguros ("mejor vendedor de seguros", "publicidad de
  seguros") y aseguradoras españolas con campañas de creadores (Mapfre, Verti, Mutua, **F-511**),
  pero **no se pudo medir volumen ni tono** (TikTok no es indexable desde este entorno).
- **Reddit:** ❄️ sin cobertura encontrada en español para "comprar seguro por redes" en Perú o
  México. Lo declaro como ausencia de señal, no como señal de ausencia.

### 3.4 Validación vs. amplificación

| Afirmación social | Amplificación | Validación (reacción de personas reales) |
|---|---|---|
| "Las redes deciden 6/10 compras" | Alta (≥6 medios, 1 fuente) | No medible: no hay hilos con reacción |
| "No confío en influencers" | Media (prensa, Ipsos) | Coherente con la narrativa de "desinfluencia" 2025 |
| "Cuidado con seguros por WhatsApp/Facebook" | Alta (reguladores, aseguradoras, EsSalud, prensa de 2+ países) | Alta: alertas institucionales repetidas = el problema es real y recurrente |

---

## 4. 📈 Pista de negocio (criterio de `marketer`: resultados publicados y verificables)

### 4.1 Tamaño y peso real del social commerce

| Métrica | Dato | Tipo de evidencia | Fuente |
|---|---|---|---|
| Social commerce EE.UU. 2025 → 2026 | US$87,0 mil M (+21,5%) → US$101,0 mil M; ~7,2% del e-commerce | 🟡 C (modelo de analista) | F-489 |
| Pronóstico de Accenture (2022) para 2025 | US$1,2 billones globales | 🟡 C, **pronóstico a contrastar** | F-488 |
| Social commerce LATAM 2025 | **US$14,6 mil M** *o* **US$172,4 mil M** según el reporte de la misma editorial | 🟠 D, **no usar** (diferencia de ~12 veces) | F-487 |
| E-commerce Perú | US$15.600 M en 2024 (+21,2%, 5,5% del PBI); US$8.700 M en 1S2025 (+18%) | 🟡 C (gremio) | F-474 |
| E-commerce México | MX$941 mil M en 2025 (+19,2%); 77,2 M de compradores; **3 de cada 10 compra por redes** | 🟡 C (gremio) | F-481 |
| E-commerce Colombia | COP 145,4 billones en 2025 (+11,1%); 684,6 M de transacciones; 2 de cada 5 descubre marcas en redes | 🟡 C (gremio) | F-484 |
| Brasil | 73% de usuarios de Instagram compró algo descubierto ahí; 69% compró por un anuncio en redes | 🟡 C (N=2.055) | F-483 |

⚠️ **Lectura de negocio:** el mercado LATAM de social commerce **no tiene hoy una cifra de tamaño
confiable**. Los números gremiales por país (CAPECE, AMVO, CCCE) sí son comparables entre sí como
e-commerce total, pero **ninguno separa con precisión la compra que se cierra dentro de la red**.

### 4.2 Plataformas: quién gana en LATAM y cómo

- **TikTok Shop** entró a México (feb-2025) y a Brasil (may-2025). En Brasil el GMV mensual pasó
  de US$1 M a US$25,7 M en 3 meses y a **US$46,1 M en agosto 2025**. La mezcla en Brasil: ~50%
  vitrina/marketplace, 25,7% video corto, 23,4% live. En México el live de marca pesa ~70%
  (Momentum Works, **F-485**). ⚠️ El arranque de México estuvo acompañado de subsidios reportados
  de US$2-3 mil M: **crecimiento comprado, todavía no probado como orgánico**.
- **Perú:** TikTok Shop **no está disponible oficialmente** a inicios de 2026 (**F-486**); lo que
  existe es TikTok como vitrina + cierre por WhatsApp o web.
- **WhatsApp es el riel de cierre de la región.** 8 de cada 10 brasileños prefiere hablar con
  empresas por mensajes (BCG+Meta, **F-493**); 81% de usuarios de smartphone en Perú seguirá
  pidiendo por WhatsApp aun sin pago integrado (Ipsos, **F-476**). Los anuncios *click-to-WhatsApp*
  reportan +94% de conversión y −92% de costo por lead, y Movistar México triplicó sus ventas
  mensuales, pero **ambos datos son de estudios comisionados por Meta** (**F-492**, 🟠 D).

### 4.3 Conversión por plataforma: lo auditable vs. lo que circula

| Cifra | ¿De dónde sale? | Veredicto |
|---|---|---|
| TikTok Shop 4,7% · Instagram 2,1% · Facebook 1,8% · live "hasta 30%" | Blogs SEO de 2026 que se citan entre sí | 🔴 **Huérfana de cita** (F-490) — no usar |
| Leads en Meta: 7,72% promedio; **finanzas y seguros 5,98%**, CPL US$38,09, CPC US$4,57 | Base de clientes de WordStream/LocalIQ (EE.UU.) | 🟡 C (F-491): real pero es **lead**, no venta, y es EE.UU. |
| CTWA +94% conversión | Forrester comisionado por Meta | 🟠 D (F-492) |
| "Corredores que usan WhatsApp convierten 45% más" (Brasil) | Blogs de software para corredores | 🔴 Huérfana (F-512) |

**Conclusión de negocio:** no existe una tasa de conversión pública, auditable y comparable **por
plataforma** para LATAM o Perú. Cualquier cifra así en una presentación debe tratarse como
supuesto y validarse con datos propios (§7 del output).

---

## 5. 🔎 Zoom: compra de seguros en redes (LATAM y Perú)

### 5.1 🔬 Empírica

- **Latinoamérica busca online y compra con persona.** Más de dos tercios de los consumidores de
  vida en 6 países (incl. Perú) **empieza su búsqueda en línea**, pero la mayoría de esas pólizas
  **no se compra por canales digitales** (McKinsey & LIMRA, 2022, **F-498**). Más de 60% quiere
  un recorrido **híbrido**, mezclando autoservicio y asistencia en cada paso (McKinsey, Informe
  Global de Seguros 2025 – LATAM, **F-499**).
- **Referencia EE.UU. (no transferible sin ajuste):** ~6 de cada 10 personas usa redes para
  informarse sobre productos financieros y de seguros (LIMRA/Life Happens, **F-232**); 78% de la
  Gen Z y los millennials usa redes en relación con productos financieros, pero sobre todo para
  **educarse**, con desconfianza explícita hacia el contenido (LOMA 2025, **F-500**, ⚠️ la parte
  cualitativa tiene N=33).
- **Brecha de oferta:** 59% de los menores de 40 quiere relacionarse digitalmente y directo con
  su aseguradora; solo 31% de las aseguradoras lo permite (Capgemini, **F-502**).
- ⚠️ **Cifra a no usar:** "72% investiga aseguradoras en redes antes de contactar a un agente
  (J.D. Power 2025)" circula en blogs de marketing de seguros, pero **no aparece** en el
  comunicado del estudio de J.D. Power que cita (**F-501**, huérfana de cita).
- **Evidencia académica específica de "comprar seguros en redes" en LATAM:** ❌ **no encontrada.**
  Los estudios revisados por pares disponibles son de intención de compra en Asia/Medio Oriente.

### 5.2 📱 Social

Ver §3.3: en seguros, la señal social más fuerte en Perú y la región es el **fraude y la
suplantación por redes/WhatsApp**. Esto es un **impuesto de confianza** que pagan todas las
aseguradoras formales cada vez que proponen cerrar por esos canales. Se suma a una desconfianza
de base de **~48%** hacia las aseguradoras en Perú (ver [[seguros-comportamiento-mundo-peru]]).

### 5.3 📈 Negocio

- **Marco regulatorio peruano:** la SBS permite comercializar seguros **a distancia**,
  incluyendo **redes sociales y comparadores**, siempre que la información sea veraz, completa y
  se entregue póliza o certificado (Res. SBS 277-2021, **F-503**). **La venta por redes es legal
  en Perú.** El límite está en el **consentimiento** para contactar (Ley 32323, **F-118**).
- **Lo que sí cierra en digital en Perú es lo simple y barato:**
  - SOAT digital desde S/32, pagado con Yape y **entregado por WhatsApp** (Interseguro, **F-510**).
  - "Seguro Salud Yape" (Pacífico × Yape) desde **S/9,90/mes** dentro de una billetera de ~17 M
    de usuarios; la alianza reporta más de 1 M de clientes con productos simples (**F-508**, 🟠 D
    por venir de un publirreportaje). El diagnóstico del PNUD (2026) registra un arranque más
    modesto del seguro de salud en Yape (~2.100 pólizas en su corte) y ~6 M de asegurados en
    microseguros en el país (**F-509**).
  - Rimac usa WhatsApp para **postventa** (aviso de siniestro con fotos), no como canal principal
    de venta de vida (**F-513**).
- **Insurtech LATAM se mueve hacia embedded/B2B2C** (536 insurtechs; Brasil 214, México 139,
  Chile 100, Colombia 67; financiamiento más selectivo) (**F-374**). Globalmente, TikTok ya
  integra seguros para comercios **dentro de TikTok Shop** (con ERGO NEXT, **F-511**): el seguro
  embebido en la red llega primero por el lado **del vendedor**, no del consumidor.
- **Benchmark de pauta:** los leads de finanzas y seguros en Meta cuestan US$38 y convierten 5,98%
  a lead (EE.UU., **F-491**). No hay benchmark público equivalente para Perú.

### 5.4 Síntesis del zoom

| | Producto simple (SOAT, microseguro, salud básica) | Producto complejo (vida, ahorro, salud integral) |
|---|---|---|
| Rol de la red | Vitrina + cierre en 1-2 pasos | Descubrimiento + educación + generación de lead |
| Canal de cierre | Billetera (Yape) / web / WhatsApp con entrega del documento | Asesor humano (presencial o por video), con WhatsApp como continuidad |
| Barrera principal | **Fraude/suplantación** (¿esto es real?) | **Confianza en el vendedor** + complejidad |
| Evidencia | Negocio (F-508, F-510); social (F-504 a F-506) | Empírica regional (F-498, F-499) + negocio ([[venta-vida-digital-hibrida-latam]]) |

---

## 6. ⚖️ Síntesis de las tres pistas

**Convergen (señal fuerte):**
1. La red **abre** la compra y otra cosa la **cierra**: el chat (WhatsApp), la billetera o el
   humano. Lo dicen la teoría de la confianza (F-494, F-495), los datos regionales de seguros
   (F-498, F-499) y los datos de negocio (F-476, F-486, F-510).
2. **La confianza en *quién vende* pesa más que el alcance de *quién recomienda*.** Lo dice el
   meta-análisis (F-494: confianza en el vendedor > otros objetos) y lo dice la calle (F-478: 7%
   confía en grandes influencers; 28% en amigos y familia).

**Divergen (tensión sin resolver):**
1. **Magnitud:** la prensa dice "las redes deciden 6 de cada 10 compras" (intención declarada,
   F-477); el negocio dice que la compra *dentro de la red* es ~7% del e-commerce incluso en
   EE.UU. (F-489). Ambas pueden ser ciertas a la vez: la red **influye mucho y transacciona poco**.
2. **Tiempo:** la industria vende "más tiempo en redes = más oportunidad"; la evidencia de panel
   muestra que el tiempo **baja** desde 2022 (F-471), aunque LATAM siga alto.
3. **WhatsApp:** el negocio lo muestra como el canal de mejor conversión de la región (F-492,
   F-493); la pista social lo muestra como el canal preferido de los estafadores de seguros
   (F-505, F-506). **El canal con más potencial de cierre es también el que carga más desconfianza.**

---

## 7. Limitaciones

- **Acceso:** la mayoría de las fuentes primarias estuvo bloqueada por el proxy (ver nota
  inicial). Varias cifras vienen de fragmentos indexados; el riesgo de error de transcripción es
  mayor que en un node con lectura directa. Caso detectado: una nota de prensa atribuye a CAPECE
  "15,6 millones de peruanos que compran en línea", **el mismo número** que los US$15.600 M de
  ventas 2024; puede ser un error de transcripción y **no se usa** en este node.
- **Minutos diarios del Perú en redes (Digital 2026):** no recuperados.
- **Tiempo evaluando productos:** no medido por ninguna fuente pública (§2.3).
- **Conversión por plataforma en LATAM/Perú:** no existe una cifra pública auditable (§4.3).
- **Pista social:** TikTok y Reddit no se pudieron medir en volumen ni tono; la pista social quedó
  apoyada en prensa y alertas institucionales.
- **Seguros:** sin evidencia académica regional sobre compra en redes; la evidencia de EE.UU.
  (F-232, F-500) no se transfiere sin ajuste por la desconfianza estructural peruana.

---

## Conexiones

- [[seguros-comportamiento-mundo-peru|Comportamiento, percepción y mercado de seguros (Mundo vs. Perú)]]
  — de ahí sale la desconfianza de base (~48%) que funciona como "impuesto de confianza" sobre la
  venta por redes; este node agrega el canal (redes/WhatsApp) a ese diagnóstico.
- [[transicion-venta-fria-a-opt-in|Transición de venta fría a opt-in]] — el anuncio que lleva a
  WhatsApp (*click-to-WhatsApp*) es la táctica puente *opt-in* más directa: el cliente inicia la
  conversación, lo que resuelve el problema de consentimiento (F-118).
- [[futuro-asesores-seguros-venta-digital|¿Desaparecerán los asesores de seguros?]] — este node
  confirma su tesis desde el canal social: la red genera la demanda y el asesor la cierra; el
  asesor-creador de contenido es la versión social de "digital potencia al intermediario".
- [[venta-vida-digital-hibrida-latam|Venta de vida en LATAM: digital vs. híbrido]] — evidencia de
  negocio complementaria: el híbrido gana en la región; aquí se ve el primer tramo (descubrimiento
  en redes) de ese recorrido híbrido.
- [[material-visual-venta-consultiva|Material visual en la venta consultiva]] — el contenido
  visual (foto/video del producto) es la actividad #1 en redes en Perú (51,4%, F-477); los
  principios de reducción de incertidumbre de ese node aplican al contenido de redes.
- [[tendencias-diseno-innovacion|Tendencias en diseño e innovación]] — la regla C22 (**huérfano de
  cita**) de ese node aplica aquí literalmente: las tasas de conversión por plataforma (F-490) y el
  "72% de J.D. Power" (F-501) son casos del mismo defecto.
