# 🐺 El Lobo — Opinión de negocio acumulada

> No vengo a resumir papers. Vengo a decir dónde hay plata, dónde se quema plata,
> y qué jugada haría yo con lo que el `cronista` ya verificó. Cada tesis carga su
> evidencia (F-n del ledger `research/fuentes/codice.md`) y un nivel de
> confianza que sube o baja según la rigurosidad de lo que la sostiene. Lo que no
> tiene fuente en el ledger va marcado como **instinto** — razonado desde
> principios de negocio, no dato verificado.
>
> Creado: 2026-07-12.

## 🎯 Tesis vigentes

### 1. La divulgación ("explicar mejor") es una palanca de conversión débil — no de crecimiento
Dos fuentes A independientes (RCT de campo con ~124k usuarios reales + síntesis
académica canónica) muestran lo mismo: mejorar la comprensión del consumidor casi
nunca cambia su conducta de compra. Un glosario, una guía o un "explicador" suben
el conocimiento, no la conversión. Un estudio oficial de la Comisión Europea
específico del ramo seguros confirma el mismo patrón dentro del sector: no basta
con dar más información, tiene que estar bien estructurada — la estructura
importa más que el volumen de divulgación.
**[Revisión profunda 2026-07-21]** Leer F-9 y F-10 completos (no solo el
resumen) agrega el *mecanismo*, no solo el resultado. En el RCT real de F-9,
cambiarse de producto tomaba ~15 minutos y la ganancia promedio rondaba
~US$190/año — y aun así casi nadie cambió. La causa que identifican los
autores es la **creencia pesimista** del consumidor sobre si la alternativa
vale el esfuerzo, no la complejidad de la información. F-10 añade la razón
estructural de por qué el sector sigue invirtiendo aquí pese a la evidencia: la
gente **recorta información en vez de acumularla** al decidir, y "divulgar
mejor" es la palanca regulatoria más fácil de accionar para un legislador, no
la que más funciona — riesgo directo para cualquier enfoque tipo "glosario
oficial" (SBS incluida) que se apoye solo en explicar mejor.
- **Evidencia:** F-9 (🟢A, RCT N≈124,000), F-10 (🟢A, síntesis canónica), F-124
  (🔵B, Comisión Europea, específico de seguros)
- **Confianza:** Alta
- **Actualizado:** 2026-07-21

### 2. El coaseguro variable es el cuello de botella de comprensión #1 en seguros de salud
Dos estudios (uno con dos encuestas representativas EE.UU., otro con encuesta
nacional del regulador de salud) coinciden: el coaseguro es el término peor
entendido, y quien tiene un plan con coaseguro/tarifas variables subestima sus
costos reales por un margen mucho mayor que quien tiene deducible fijo. Esto no es
un problema de comunicación — es un problema de diseño de producto.
**[Revisión profunda 2026-07-21]** La segunda encuesta del propio estudio F-6
(no solo la primera, ya citada) separa dos cosas que se suelen mezclar: la
evidencia de que la gente **entendería mejor** un plan simplificado
(todo-copago, sin coaseguro) es sólida — pero la evidencia de que ese plan
simplificado **les atraería más o cambiaría su elección real** es bastante más
débil. Comprensión y preferencia no son lo mismo: un cliente puede entender
perfectamente el coaseguro y aun así preferirlo, por ejemplo por una prima más
baja. **Tope explícito:** esta tesis sostiene el diagnóstico de comprensión con
confianza Alta; el salto a "por tanto simplificar el producto aumenta ventas"
hereda el tope de la tesis 1 y necesita su propia validación de elección real.
- **Evidencia:** F-6 (🟢A, Loewenstein et al. 2013), F-7 (🔵B, KFF 2017)
- **Confianza:** Alta en el diagnóstico de comprensión; el paso a "simplificar
  vende más" no está probado por esta fuente y hereda el tope de tesis 1.
- **Actualizado:** 2026-07-21

### 3. El problema de comprensión es estructural, no generacional — no lo resuelve "educar a los jóvenes"
Solo ~1 de cada 4 adultos Gen Z en EE.UU. puede definir deducible o copago. Ningún
`F-n` nuevo desde el 2026-07-12 toca este patrón generacional.
- **Evidencia:** F-8 (🟡C, NAIC 2024 — nota de asociación, método no detallado)
- **Confianza:** Media. **Tope explícito:** no sube a Alta por consistencia
  narrativa — solo sube si aparece un F-n con rigurosidad B o mejor que confirme
  el patrón generacional, idealmente con dato peruano/latinoamericano.
- **Actualizado:** 2026-07-17

### 4. La brecha de aseguramiento sísmico en Perú es una categoría de producto casi vacía — y hoy tiene ruta de producto concreta
Solo ~3.3% de los hogares peruanos tiene seguro contra sismos/desastres (dato aún
vía prensa/APESEG, no primario). Lo nuevo: el mercado de seguros **paramétricos**
—el vehículo natural para llenar este vacío— pasó de tesis abstracta a categoría
con tracción real: proyectado de ~USD 21B (2026) a ~USD 39B (2030), y ya existe
marco académico publicado sobre cómo diseñar el trigger para minimizar riesgo de
base. La oportunidad ya no depende solo de que el 3.3% sea exacto — depende de que
la categoría "producto paramétrico" tiene demanda de capital y diseño técnico
maduro detrás, mundialmente.
**[Nota 2026-07-21 — instinto, no fuente nueva]** La revisión profunda de hoy
sobre F-3 (tesis 14: miopía + narrow framing) da una lectura de por qué el
3.3% es tan bajo, no solo cuánto: un hogar que asegura su auto pero no su
casa contra sismo no está siendo irracional respecto al sismo específicamente
— está evaluando cada póliza aislada (narrow framing) en vez de ver que ambas
exposiciones son parte del mismo portafolio de riesgo. Esto es razonamiento
desde tesis 14, no un dato nuevo del ledger: implica que el mensaje de venta
del paramétrico sísmico debería anclarse explícitamente al seguro que el
cliente ya tiene (auto, SOAT), no venderse como categoría nueva aislada — pero
esto no está probado con un experimento de conversión real, es hipótesis de
producto derivada, no verificada.
- **Evidencia:** F-5 (🟠D, Infobae vía APESEG — número de brecha sin cambio),
  F-163 (🟡C, SOA, tamaño de mercado paramétrico), F-164 (🟢A, diseño óptimo de
  trigger); conexión con F-3 (🟢A, tesis 14) es razonamiento propio, no cita
  directa del paper sobre seguros de desastre.
- **Confianza:** Media en el número exacto de brecha (sin cambio, mismo tope que
  antes); **Alta** en que "paramétrico sísmico" es la jugada de producto correcta
  independientemente del número exacto — la ventana de mercado/capital ya no es
  instinto, tiene evidencia A+C detrás. La lectura de mensaje anclado a
  narrow framing es **instinto**, no probada.
- **Actualizado:** 2026-07-21

### 5. ESG como diferenciador de marca: aplica al consumidor global premium, no está probado en Perú
Bain reporta que ~80% de consumidores globales quiere criterios ESG integrados en
sus seguros. Es una encuesta propia de consultora (no auditable) y de alcance
global — extrapolarla al consumidor peruano medio es **instinto**, no dato.
- **Evidencia:** F-4 (🟡C, Bain & Company 2023, alcance global)
- **Confianza:** Baja para el mercado peruano específicamente
- **Actualizado:** 2026-07-12

### 6. La era del "nudge de catálogo" terminó — testear en la propia población es el estándar, no copiar el tamaño de efecto de un paper
El meta-análisis fundacional pro-nudge (447 experimentos) fue revertido por un
re-análisis bayesiano que corrige sesgo de publicación: ajustado, no queda
evidencia de un efecto promedio del nudging. Con datos reales a escala el efecto
que sobrevive ronda ~1.4pp, muy por debajo del ~8.7pp de los papers académicos —
un "voltage drop" de ~6x entre laboratorio y despliegue real.
**[Revisión profunda 2026-07-21]** Dentro del propio dataset de Mertens et al.
(F-16: 447 efectos/212 estudios, corregido después a 455/214 sin cambiar la
conclusión sustantiva), el ranking por técnica no era parejo: **default/
esfuerzo** tuvo el efecto más grande específicamente en los dominios de
**salud y finanzas** —los dos más relevantes para un asegurador— mientras que
**incentivos** domina en educación y políticas públicas. Esto no contradice
que "murió el efecto promedio" (F-17 sigue en pie); pero si hay que elegir qué
técnica testear primero en la propia población —que es justo lo que pide esta
tesis— el ranking direccional del propio dataset dice "empieza por defaults",
no por mensajes/priming. No es garantía, es prior razonable para priorizar el
primer experimento.
**[Revisión profunda 2026-07-22]** Leí a fondo las 5 fuentes 🟢A que sostienen esta tesis
(F-17 a F-21 — antes solo tenían el resumen de una línea del ledger). Tres hallazgos
nuevos, ninguno cambia la dirección de la tesis, pero la profundizan:
1. **"No hay efecto promedio" no es solo el veredicto de Maier — es el mismo resultado
   por tres caminos metodológicos independientes.** F-17 (RoBMA sobre el propio dataset
   de Mertens) ya lo decía; F-18 (Hu et al. 2025) lo repite a escala mucho mayor —14
   meta-análisis, 1,638 estudios, ~30M de participantes— y el efecto agregado cae de
   d=0.27 a **d=0.004** tras corregir sesgo de publicación; F-21 (DellaVigna & Linos)
   llega ahí por una ruta totalmente distinta (RCTs reales de unidades de gobierno vs.
   RCTs publicados en journals) y encuentra que el sesgo de publicación + bajo poder
   estadístico académico **alcanzan para explicar toda la brecha** de ~6x ("voltage
   drop"), no una supuesta diferencia laboratorio-vs-mundo-real. **Caveat que templa la
   contundencia:** Hu et al. reportan que la mayoría de los 14 meta-análisis que agregan
   tiene calidad metodológica baja o crítica (AMSTAR-2, por falta de pre-registro y de
   evaluación de riesgo de sesgo) — el corpus que sostiene "no hay efecto" es él mismo de
   calidad mediocre. Es la mejor estimación disponible hoy, no un caso cerrado con
   evidencia impecable.
2. **F-20 (Milkman) en detalle da una receta de diseño, no solo un método a copiar.** El
   megastudy real fue 54 programas de 4 semanas sobre 61,293 miembros reales de gimnasio;
   45% de las intervenciones subió asistencia 9-27%, y la que más funcionó no fue un
   recordatorio genérico sino un microincentivo (~US$0.09) dirigido específicamente al
   **momento de recaída** (faltar a una sesión programada y volver a la siguiente). Prior
   accionable para el primer experimento propio: diseñar el nudge alrededor del momento de
   lapso, no de la adherencia general.
3. **F-19 (Chater & Loewenstein) da un mecanismo de negocio, no solo académico, para por
   qué el i-frame domina.** Documentan que BP acuñó "huella de carbono" en 2004
   específicamente para reencuadrar el cambio climático como responsabilidad individual
   mientras cabildeaba contra la regulación sistémica que sí reduciría emisiones — su
   lectura es que firmas de sectores diversos "promueven el i-frame mientras cabildean sin
   descanso por políticas s-frame que favorecen sus propios intereses". Conexión directa
   con tesis 1: apostar solo por "educación financiera" o "glosarios" sin rediseñar el
   producto no es solo una jugada de ROI débil (tesis 1) — corre el riesgo de leerse como
   el mismo patrón de desvío de responsabilidad que describe este caso, si no se acompaña
   de cambios reales de producto.
- **Evidencia:** F-16, F-17, F-18, F-19, F-20, F-21 (todas 🟢A)
- **Confianza:** Alta — ahora sostenida por tres metodologías independientes que convergen
  en la misma conclusión, con el caveat explícito de que el corpus agregado más reciente
  (Hu et al.) es de calidad mediocre.
- **Actualizado:** 2026-07-22

### 7. El diseño de producto embebido (s-frame) gana sobre el nudge cosmético (i-frame) — pero la telemática tiene techo de confianza incluso donde funciona
El caso UBI (seguro por uso) con outcome telemático real —no autoreportado—
prueba que rediseñar el producto (pricing dinámico + feedback) cambia conducta de
manejo medible: velocidad -11-13%, frenadas bruscas -16-21%. Matiz nuevo: incluso
en un mercado maduro y con marco regulatorio claro (UK), la adopción real es baja
y la desconfianza persiste — solo ~12% usa telemática hoy, 73% no la usa, y solo
32% se siente cómodo con que el asegurador recolecte ese dato. El producto
funciona; la barrera no es de diseño, es de confianza en el punto de entrada.
- **Evidencia:** F-19 (🟢A, marco i-frame/s-frame), F-23 (🟢A, RCT de campo
  telemático), F-166/F-167 (🟠D, techo de adopción/confianza en UK)
- **Confianza:** Alta en que el producto funciona donde se adopta; Media en la
  velocidad de adopción masiva sin trabajar antes la confianza de entrada.
- **Actualizado:** 2026-07-20

### 8. El riesgo regulatorio por contacto comercial no consentido en seguros peruanos ya no es teórico — es expediente activo, y ya tocó al sector
INDECOPI fiscaliza con IA más de 7 millones de audios de llamadas comerciales al
año y ya sancionó 26 empresas en 2025 por S/2.6M. Lo que cambia el cálculo de
riesgo: **Pacífico Seguros** está bajo investigación directa (50,000 audios de su
call center Impulsa365 analizados) y BBVA fue sancionado dos veces, la segunda
tras pedir explícitamente ser excluido de la base de datos — la corrección
regulatoria ya alcanzó a un competidor directo del ramo seguros, no es un riesgo
de otro sector que "podría" llegar a seguros.
- **Evidencia:** F-70 (🔵B, INDECOPI, escala de fiscalización), F-117 (🔵B,
  Pacífico Seguros bajo investigación), F-118 (🔵B, caso BBVA + texto legal),
  F-138 (🔵B, segunda sanción BBVA)
- **Confianza:** Alta
- **Actualizado:** 2026-07-20

### 9. El modelo farmacia-frente-primario + triage IA + derivación tiene tracción estatal y de infraestructura real en Perú, no es apuesta especulativa
Tres señales independientes convergen: (a) el Congreso tiene en debate el PL
08488 para incorporar farmacias privadas como puntos de atención primaria; (b)
MINSA ya aprobó el Plan Nacional de Telesalud 2026 con red de >2,000
establecimientos y >3M atenciones remotas registradas; (c) la infraestructura de
delivery de farmacia ya opera a escala nacional (InkaFarma+Mifarma, 2,245
locales, 18% de boticas del país). Y el comportamiento real del usuario ya apunta
hacia ahí: la automedicación en Perú **no** nace principalmente de desconfianza
en el médico (solo 7.2% la cita como razón) sino de ineficiencia del sistema
formal (59%) y falta de tiempo (51%) — el frente de farmacia no compite contra la
confianza del paciente, compite contra la lentitud del Estado.
- **Evidencia:** F-38 (🟠D, razones de automedicación), F-47 (🟠D, PL 08488),
  F-48 (🔵B, Plan Nacional de Telesalud MINSA), F-49 (🟠D, escala de InkaFarma/Mifarma)
- **Confianza:** Alta en la oportunidad de mercado/distribución; el riesgo de
  ejecución técnica del triage IA es un problema aparte (ver tesis 10).
- **Actualizado:** 2026-07-20

### 10. El punto de fracaso más probable de un triage con IA no es la tecnología — es sobreclamar precisión clínica sin validación formal
Babylon Health colapsó de USD 4.2B de valuación a bancarrota exactamente por
esto: el Lancet no encontró evidencia convincente de que su triage superara a
médicos humanos en ningún escenario realista. En el mundo real, los
symptom-checkers de IA en producción rondan ~45% de precisión diagnóstica sin
mejora en 3 años de uso — muy por debajo de lo que sugiere el marketing típico
del sector. La literatura ya tiene el playbook para evitarlo: correr el modelo en
"silent trial"/shadow mode 60-90 días (sin influir en la atención real, sin
necesitar consentimiento) antes de producción, y separar explícitamente
validación técnica de validación clínica (la que casi siempre se salta).
- **Evidencia:** F-50 (🟢A/vía prensa especializada, caso Babylon), F-43 (🟢A,
  precisión real 45%), F-56/F-57 (🟢A, protocolo de silent trial), F-62 (🔵B,
  marco FDA SaMD)
- **Confianza:** Alta
- **Actualizado:** 2026-07-20

### 11. El ciclo de rentabilidad del seguro global está en su mejor momento en 25 años — no es momento de jugar defensivo
Combined ratio P&C de EE.UU. en 91.9% con la mayor ganancia de suscripción en 25
años; reaseguro (Munich Re, Swiss Re, Hannover Re, Scor) con ROE conjunto récord
de 19.6%. Converge con tesis 4: la ventana para lanzar el producto paramétrico
sísmico no solo tiene demanda sin cubrir del lado del consumidor peruano, tiene
ciclo de capital reasegurador favorable del lado de la oferta, al mismo tiempo.
- **Evidencia:** F-160 (🟠D, combined ratio 25-year high), F-32/F-33/F-34 (🔵B/🔵B/🟠D,
  récords de ROE en reaseguro), F-163/F-164 (ver tesis 4)
- **Confianza:** Media-Alta — converge desde múltiples jugadores independientes,
  pero ninguna fuente A pura mide directamente "ciclo favorable = buen momento
  de lanzamiento", es lectura de negocio sobre datos financieros oficiales.
- **Actualizado:** 2026-07-20

### 12. "Menos opciones convierte más" es folklore de UX, no un efecto confiable — la palanca real es estructurar la comparación, no podar el catálogo
El meta-análisis que agrega 50 estudios de choice overload da un efecto promedio
prácticamente cero; el estudio clásico de las mermeladas que originó la narrativa
no replica de forma consistente. Lo que sí tiene evidencia sólida y específica
del ramo seguros: las ayudas de decisión visuales (icon arrays, formato de
frecuencia "3 de 100" en vez de porcentaje) mejoran comprensión de riesgo en
segmentos de baja numeracidad — exactamente el segmento peruano de baja
educación financiera que ya modela `lapuerta`.
- **Evidencia:** F-119 (🟢A, meta-análisis ~efecto cero), F-121 (🟢A, el
  estudio original no replica bien), F-122 (🟢A, decision aids mejoran
  conocimiento/reducen conflicto decisional), F-123 (🟢A, icon arrays en baja
  numeracidad), F-124 (🔵B, seguros específicamente)
- **Confianza:** Alta
- **Actualizado:** 2026-07-20

### 13. La divulgación progresiva de datos convierte mejor — y funciona incluso sin cambiar la actitud real del cliente hacia su privacidad
Dos estudios A recientes confirman el mecanismo exacto: secuenciar los campos de
un formulario de menos a más sensibles (y repartirlos en varias pantallas)
aumenta cuánto divulga la persona; pedir datos repetidamente aumenta la
divulgación con el tiempo **sin que cambie la preocupación real de privacidad**
— funciona aunque no debería. El antecedente más fuerte de divulgación real no es
la explicación legal sino la confianza situacional en la marca (paradoja de la
privacidad: la intención declarada de proteger datos no predice la conducta
real). Jugada directa para el onboarding de `disposicion_compartir_datos_pricing`
(variable ya calibrada en `lapuerta` v1.3) y para cualquier flujo de
consentimiento de telemática/UBI: pedir en pasos progresivos anclados a marca de
confianza, no en un formulario legal único.
- **Evidencia:** F-142 (🟢A, secuenciar campos aumenta divulgación), F-143 (🟢A,
  repetición aumenta divulgación sin cambiar actitud), F-144 (🟢A, paradoja de la
  privacidad, canónico), F-141 (🟢A, foot-in-the-door original)
- **Confianza:** Alta en el mecanismo; **riesgo ético explícito** — el mismo
  mecanismo que convierte mejor puede leerse como manipulador si se abusa, no es
  carta libre para maximizar divulgación sin límite.
- **Actualizado:** 2026-07-20

### 14. La subaseguración tiene dos mecanismos conductuales específicos y accionables — miopía y narrow framing — que la educación financiera genérica no ataca
Un survey académico de 2021 (revisado a fondo el 2026-07-21) descompone
"sesgos" —la palabra genérica que usan `CLAUDE.md` y `lapuerta`— en mecanismos
concretos: **miopía** (cortoplacismo que subestima riesgos futuros) y **narrow
framing** (evaluar cada decisión de seguro de forma aislada, sin ver el
portafolio de riesgo total — por eso alguien asegura su auto y no su salud sin
sentir contradicción, aunque ambas son la misma exposición al riesgo
agregado). La mitigación que propone la literatura no es "más educación
financiera" sino alfabetización **específicamente sobre los sesgos** — un
contenido distinto al glosario de términos (tesis 1/2) o a la educación
financiera genérica que ya intenta la SBS.
- **Evidencia:** F-3 (🟢A, Pitthan & De Witte 2021 — nota: el ledger tenía mal
  atribuida la autoría a "Platteau", corregido en esta revisión)
- **Confianza:** Media — es un survey teórico sin RCT propio que mida si
  "alfabetización en sesgos" cambia la tenencia real de seguros en Perú; el
  mecanismo es plausible y coherente con tesis 1 (educar no basta si no ataca
  la creencia/marco correcto), pero falta el dato de intervención.
- **Actualizado:** 2026-07-21

### 15. Una cifra headline de retorno en % no es solo una elección de diseño — es un ancla persuasiva y un patrón ya fiscalizado en Perú al mismo tiempo
Un número inicial grande y prominente ("170% de devolución") sesga el juicio de valor
del consumidor incluso cuando el número es poco relevante — efecto de anclaje robusto,
no específico de seguros pero bien establecido. El mismo patrón (cifra grande + condición
real en letra chica) es justo el que un marco regulatorio de referencia (NAIC, EE.UU.)
prohíbe expresar como porcentaje —exige monto—; no es norma peruana, pero marca la
categoría de riesgo. En Perú, Indecopi fiscaliza publicidad financiera engañosa de forma
activa y ya sancionó a una entidad financiera comparable (BBVA, 2025) por una promesa
publicitaria que no se cumplía en la práctica — el riesgo de fiscalización no es
hipotético. Información "a confirmar" (montos/plazos sin cerrar) visible en piezas que
llegan al cliente reduce de forma medible tanto la confianza en la fuente como la
disposición a comprar: no es un detalle de producción pendiente, es una fuga de
conversión y un riesgo regulatorio a la vez, con el mismo origen.
- **Evidencia:** F-175 (🟢A, efecto de anclaje), F-172 (🔵B, modelo NAIC, EE.UU. — no
  aplicable directo en Perú), F-173 (🔵B, lineamientos Indecopi, sí aplicable), F-174
  (🟠D, caso BBVA vía prensa sobre resolución oficial), F-176 (🟢A, info incompleta →
  menos confianza y disposición a comprar), F-177 (🟠D, cifra direccional de abandono)
- **Confianza:** Alta en que el patrón (cifra % headline + condición chica + dato "a
  confirmar" visible) es simultáneamente el de mayor poder persuasivo y el de mayor
  riesgo regulatorio-reputacional. Media en si Indecopi sancionaría específicamente el
  caso "% vs. monto" — F-173 no se investigó al mismo nivel de detalle que F-172 (que es
  de EE.UU.); no tratar como bloqueante legal cierto en Perú sin verificación adicional
  del marco peruano en ese punto específico.
- **Actualizado:** 2026-07-21

### 16. El asesor de seguros no desaparece con la venta digital — se redistribuye por complejidad de producto, y el reclamo (no la venta) es donde lo 100%-digital falla más
Investigación 360° (`/trinidad`) sobre si la tecnología elimina al intermediario da un
veredicto convergente en las tres pistas: no. El marco causal canónico (Cummins &
Doherty 2006) explica que el agente/broker es un "market maker" que mitiga asimetría de
información y selección adversa — un problema estructural que la tecnología automatiza
parcialmente, no elimina. Dos estudios empíricos confirman que la complejidad del
producto y la confianza (no "cuán digital es la sociedad") predicen si alguien compra
sin humano. La evidencia de negocio es la que más pesa aquí, y es incómoda para el
discurso "todo se automatiza": en Corea del Sur (mercado altamente digitalizado) el
canal 100% online de seguros de vida **cayó 33.6% en una década**; en China, pese a
20x de crecimiento insurtech, agentes+bancaseguros retienen >90% de las primas de vida;
Lemonade —el caso insignia de "seguro 100% digital"— sigue sin ser rentable 12 años
después de fundado; y el mercado global de corretaje está **creciendo** (USD 336B→695B
proyectado a 2033), no encogiendo. El punto de falla más agudo de lo digital-only no es
la venta, es el reclamo: 33-39% de reclamos 100% digitales fallan y requieren rescate
humano, y quien escala de digital a humano reporta una experiencia **peor** (NPS -11)
que cualquiera de los dos canales bien ejecutados solos. Señal social que refuerza esto
sin buscarla: el backlash viral de diciembre 2024 contra UnitedHealthcare (62,000
reacciones en un post, 57,000 de risa) fue rabia específica contra la negación
automatizada de reclamos de salud — el público no celebra que una IA decida sin criterio
humano en el momento de mayor impacto.
- **Evidencia:** F-180 (🟢A, marco causal), F-191 (🔵B, confianza+complejidad), F-192
  (⚠️ no verificado, tratar con cautela), F-181 a F-186, F-189, F-190 (🟡C/🟠D, datos de
  negocio convergentes de 3 mercados independientes), F-183 (🟡C, falla de reclamos
  digitales), F-187/F-188 (🟠D, señal social)
- **Confianza:** Alta en la dirección (el intermediario se redistribuye por complejidad,
  no desaparece); Media en la magnitud exacta de cualquier cifra puntual — casi toda la
  evidencia de negocio es C/D, ninguna supera B. Ningún dato es específico de Perú; la
  transferencia se apoya en que el patrón (confianza sube con broker) ya está
  documentado localmente en tesis previas de este mismo ledger.
- **Actualizado:** 2026-07-23

### 17. La rentabilidad real del seguro de salud no viene de suscribir riesgo — viene de integrarse verticalmente con farmacia/PBM, y el costo especializado (GLP-1) es hoy el driver más agudo
Datos oficiales de EE.UU. (mercado que concentra ~80% de las primas de salud privadas
del mundo) muestran un margen de suscripción de apenas 1.8% (H1 2025) y un medical loss
ratio >87% con mínimo de 7 años en 2022 — parte de esto es diseño regulatorio a
propósito (la regla 80/20 obliga a devolver el excedente como reembolso; se devolvieron
USD 11,800M entre 2012-2023), no solo competencia de mercado. Pero el dato que cambia el
análisis es otro: en el mismo trimestre, la unidad de farmacia (PBM) del asegurador más
grande de EE.UU. —Optum Rx, cuyo principal cliente es su propia aseguradora hermana—
generó USD 1,500M de utilidad operativa sobre USD 38,300M de ingresos, con un filing
regulatorio primario (no estimación de prensa) como fuente. No es un caso aislado: 3
PBMs procesan el 80% de los reclamos de recetas en EE.UU. y las 3 están integradas
verticalmente con una aseguradora grande. **Lectura de negocio:** "rentable" y "con
margen de suscripción alto" son dos afirmaciones distintas — la utilidad real del sector
hoy vive en el negocio adyacente integrado (farmacia), no en el seguro puro. Esto
refuerza directamente la tesis 9 (farmacia-frente-primario en Perú): no es solo una
oportunidad de distribución/acceso, es el mismo mecanismo estructural por el que el
asegurador más grande del mundo genera utilidad real hoy. Dentro de la presión de costo
médico general, el driver más agudo y actual tiene nombre propio: gasto en farmacia
+14.8% interanual en 2026, impulsado por GLP-1 (pérdida de peso/diabetes) — 43% de
planes de salud lo rankean como prioridad #1 de manejo de costo.
- **Evidencia:** F-193 (🔵B, margen 1.8%), F-194 (🔵B, MLR >87%), F-197 (🔵B, techo
  regulatorio 80/20), F-198 (🟢A, filing SEC primario, utilidad de Optum Rx), F-199
  (🟡C, concentración de PBMs), F-200 (🟡C, cambio de modelo de utilidad del PBM), F-201
  (🟠D, GLP-1 +14.8%), F-202 (🟡C, GLP-1 como prioridad #1)
- **Confianza:** Alta en el patrón de EE.UU. (sostenido por un filing primario, no solo
  prensa/consultora); la extrapolación a que el mismo mecanismo aplicaría en Perú es
  **instinto** — no hay dato peruano de márgenes de aseguradora de salud vs. margen de
  farmacia en este ledger todavía.
- **Actualizado:** 2026-07-23

### 18. El playbook de venta de RIMAC mezclaba una técnica real de persuasión conductual con una heurística de ventas sin base científica, vendidas como si fueran del mismo tipo
Auditoría dedicada (2026-07-24, a pedido del usuario) del Bloque 4 del Playbook del Asesor —
manejo de objeciones, 9 "sesgos cognitivos" (C.1-C.9) nombrados sin una sola cita— para el
proyecto `_nodes/proyecto-back-to-basics-ffvv-vida.md`. Primera pasada (mismo día) trabajó solo
sobre el resumen del proyecto, que no traía la numeración C.n exacta; segunda pasada, ya sobre el
documento real `Playbook_del_asesor.md`, corrigió la numeración y sumó la novena técnica que
faltaba (C.4, sesgo del presente). Resultado final: 8 de las 9 sí tienen origen académico sólido
y verificable (prueba social, anclaje, dotación, sesgo del presente, aversión a la pérdida,
dilución de responsabilidad, encuadre, facilidad cognitiva), con papers fundacionales de
Kahneman, Tversky, Thaler, Cialdini y el propio ledger del proyecto (F-3) detrás. La novena —C.7,
"regla del 10x"— **no es un sesgo cognitivo**: es una heurística de fijación de metas de un libro
de ventas motivacional (Grant Cardone, 2011), sin metodología ni evidencia empírica propia, y sin
relación real con cómo el Playbook la usa ("poner el precio en contexto"). Mezclarla con las
otras ocho en la misma lista le da una autoridad que no tiene — no es un error trivial de
formato, es presentar una opinión de negocio como si fuera ciencia conductual verificada,
exactamente el tipo de vulnerabilidad que ya señalaba la **tesis 6** (no confiar en catálogo sin
verificar origen) y un caso concreto, no hipotético, de por qué auditar cada "sesgo" antes de
enseñarlo a un asesor. Un matiz adicional en "dilución de responsabilidad" (C.6): el paper
original (Darley & Latané 1968) describe por qué la gente *no actúa* frente a una emergencia
cuando hay testigos — aplicarlo a "manejo de objeciones" en una venta 1-a-1 es una transferencia
de dominio que la literatura no valida directamente; la cita es real, el encaje con el uso que le
da el Playbook no lo es todavía. Las 8 citas ya se insertaron directamente en el documento real
del Playbook (no solo en el ledger), con la corrección de C.7 marcada como nota, no como
eliminación unilateral — la decisión de retirar o renombrar esa técnica queda para el equipo.
- **Evidencia:** F-220, F-221, F-222, F-223, F-224, F-225, F-228 (🟢A, fuentes fundacionales de
  cada sesgo real); F-3 (🟢A, ya en el ledger, ahora también sostiene C.4); F-226 (🟢A, cita real
  con encaje de dominio cuestionable); F-227 (🔴E, confirma que "regla del 10x" no es ciencia
  conductual)
- **Confianza:** Alta en que 8 de 9 técnicas tienen base académica sólida y en que la técnica #9
  está mal categorizada; Media en el encaje específico de "dilución de responsabilidad" al
  contexto de objeciones de venta 1-a-1 (cita real, transferencia de dominio no verificada).
- **Actualizado:** 2026-07-24

### 19. Perfilar por motivación, no por demografía, ya no es solo elegancia de diseño — y puede ser el punto ciego estructural de `lapuerta`
Un paper específico de servicios financieros (no marketing genérico) encuentra que la
segmentación demográfica estándar (edad, ingreso, ocupación) explica poco de la conducta
real de compra, preferencia de marca o adopción de canal/tecnología en este sector. La
Teoría de la Autodeterminación —una de las teorías de motivación humana más replicadas en
psicología— da el marco de por qué: la conducta sostenida conecta con necesidades
psicológicas (autonomía, competencia, relación) y metas personales, no con una categoría
externa asignada. Esto no es una curiosidad académica: es evidencia convergente A+A de que
"perfilar por el por qué del cliente" (protección / crecimiento / meta / rentabilizar) le
gana estructuralmente a perfilar por edad/NSE/ocupación en este sector específico.
**Instinto conectado, no dato nuevo:** `lapuerta` construye sus personas sintéticas
mayormente sobre variables demográficas (NSE, generación, región, educación financiera,
exposición sísmica) — ninguna variable del esquema v1.3 captura directamente la
*motivación* del cliente frente al seguro. Si el hallazgo de F-229 se extiende más allá de
vida individual (no verificado, es el escenario donde se encontró la evidencia), el modelo
puede estar optimizando la variable de segmentación equivocada para lo que de verdad
predice conducta. No es una recomendación de cambio inmediato al esquema — es una hipótesis
de brecha para poner sobre la mesa en la próxima revisión de variables (`/cerrajero`).
- **Evidencia:** F-229 (🟢A, Piercy/Campbell/Heinrich 2011, específico de servicios
  financieros), F-230 (🟢A, Deci & Ryan 2000, marco teórico canónico)
- **Confianza:** Alta en el patrón general (empírico sectorial + teoría robusta convergen);
  Media en que aplique tal cual fuera de vida individual — es extrapolación razonada, no
  verificada, y la conexión con el esquema de `lapuerta` es instinto explícito.
- **Actualizado:** 2026-07-25

### 20. En vida individual, el freno más caro no es la incomprensión del producto — es un precio percibido 7-12x inflado, y solo saliencia+calculadora (no lenguaje simple solo) lo revierte
Una encuesta de gremio (LIMRA/Life Happens) encuentra que 72% sobreestima el costo de una
póliza term life básica, solo 25% acierta el precio real, y los adultos jóvenes y sanos
—el segmento de menor riesgo real, el que menos debería sobreestimar— la sobreestiman de 7
a 12 veces. Esto es un problema distinto al de tesis 1/2 (comprensión de términos): no es
que el cliente no entienda "coaseguro", es que tiene un número equivocado en la cabeza
antes de que empiece la conversación de venta. Dos RCT declarados (SOA/RGA 2024) muestran
qué sí mueve esa aguja: FAQs + resúmenes + íconos de saliencia mejoraron comprensión 21%;
combinar lenguaje simple con una **calculadora de precio personalizada** llegó a 28% — y
el lenguaje simplificado por sí solo, sin más, no bastó. La jugada no es "explicar mejor
el producto" (palanca ya débil según tesis 1), es corregir un número concreto y mal
calculado, con una herramienta, no con un texto.
- **Evidencia:** F-231 (🔵B, dos RCT declarados N=2,001/2,005, revisión por pares no
  verificada por ser informe de instituto, no revista arbitrada), F-232 (🟡C, encuesta de
  gremio, N no verificado en esta búsqueda por bloqueo de acceso a la fuente primaria)
- **Confianza:** Media-Alta — el mecanismo (saliencia+calculadora > lenguaje solo) tiene
  respaldo B; la magnitud exacta de sobreestimación (7-12x) es C, cifra de gremio sin
  verificación independiente en esta pasada.
- **Actualizado:** 2026-07-25

### 21. RIMAC ya tiene el "quién" de la fuga con precisión de clase mundial — el vacío de valor real está en el "por qué" de la cancelación voluntaria, no en el modelo
Análisis de dos decks internos (Modelo de Churn — Visión Cliente, abril 2026; Matriz de
Renovación AMI y VEH, ene-feb 2026) más validación externa (`/trinidad`, 2026-07-30) sobre
el nivel de sofisticación real de esa capacidad. Los 7 modelos (3 de Churn + 4 de
Renovación) capturan 79-91% del evento con solo 26-36% de la base — un benchmark académico
publicado reciente (revista arbitrada) reporta lift de ~1.9-3.01x en el decil superior
como el estándar/mejor-caso de la literatura, con 50% de la base necesaria para el mismo
~90% de captura. RIMAC necesita casi la mitad de esa base para el mismo resultado, y el
score "Muy Alto" de Morosidad tiene lift x11.6 — muy por encima del x3.01 publicado como
mejor caso. **Esto no es una comparación controlada perfecta (datasets distintos), pero la
brecha es demasiado grande para ser ruido:** la capacidad técnica de detección ya no es el
cuello de botella de esta operación. El hallazgo de mayor valor de negocio no es técnico:
la cancelación **voluntaria** (pedido del cliente, APC, 59% del total) supera a la
**involuntaria** (morosidad, 41%), y es consistente con una tendencia de industria mucho
más amplia y reciente —no una anomalía del dato de RIMAC— documentada externamente: ~29% de
asegurados en EE.UU. cambiaron de aseguradora en 2025 por presión de precio acumulada, y
60% cambiaría por mejor personalización/experiencia, no por precio más bajo. **Ningún
documento interno reporta la causa raíz de ese 59%** (precio, servicio, competencia) — es
el vacío de mayor valor de negocio de todo el cruce: RIMAC tiene el "quién" con precisión,
no el "por qué". Segundo hallazgo, más especulativo: la matriz AMI muestra un patrón
inverso al de VEH — baja persistencia predicha se asocia a *más* siniestralidad relativa en
AMI (ratio 1.30) y a *menos* en VEH (ratio 0.68), algo que ningún documento fuente señala.
La literatura de selección adversa dinámica en seguros de salud (revista especializada en
economía del seguro, 2026) da el marco teórico más cercano —quienes lapsan tienen una
experiencia de siniestros distinta de quienes permanecen— pero el dato de RIMAC es
*predictivo* (dos scores sobre clientes que aún no decidieron), no retrospectivo, así que
la analogía no se puede confirmar 1:1: se reporta como divergencia señalada, no como
hallazgo cerrado. Tercer hallazgo, de gobernanza de datos, no de negocio: "% Efectividad"
significa cosas opuestas en cada uno de los dos decks (recall en Churn, precisión en
Renovación), hay 4 láminas con contenido incompleto (placeholders sin llenar) ocultas en
vez de corregidas, y al menos 3 inconsistencias puntuales (etiqueta cruzada VEH/AMI, campo
vacío, valores idénticos entre segmentos que deberían diferir) — nada que invalide los
modelos, pero si alguien en el equipo compara ambos decks asumiendo que los términos
significan lo mismo, va a leer mal los números.
- **Evidencia:** F-388 (🟢A, benchmark de lift de churn), F-389 (🟡C, cancelación voluntaria
  como tendencia de industria), F-390 (🟢A, selección adversa dinámica en salud — divergencia
  señalada, no confirmación directa), F-391 (🔵B, mismo mecanismo en cuidado a largo plazo),
  F-392 (🟡C, ventana de decisión 30-90 días — tratar con cautela)
- **Confianza:** Alta en que la capacidad técnica de RIMAC está por encima del benchmark
  publicado y en que el vacío real es la causa raíz de la cancelación voluntaria, no el
  modelo; Media en la lectura de selección adversa dinámica para el patrón AMI/VEH — es el
  marco teórico más cercano encontrado, no una confirmación causal con el dato disponible.
- **Actualizado:** 2026-07-30

## 💰 Oportunidades

- **Producto paramétrico de bajo costo contra sismos.** Categoría con ~96.7% de
  hogares sin cobertura (tesis 4), y ahora con mercado global creciendo a
  ~USD 39B para 2030 y marco de diseño técnico ya publicado (tesis 4/11). SOAT
  ya probó que la distribución masiva funciona con producto simple y precio
  bajo. Jugada: bundling o cross-sell sobre la base de SOAT, con diseño de
  trigger validado académicamente, en un ciclo de reaseguro favorable — la
  ventana de oferta y demanda coinciden hoy.
- **Rediseñar el producto, no el glosario.** Si el coaseguro variable es el
  problema (tesis 2) y la divulgación no cambia conducta (tesis 1), la jugada de
  mayor ROI es lanzar variantes con deducible fijo y simuladores de costo en el
  punto de venta.
- **Farmacia + triage IA + derivación como frente primario de salud.** Tracción
  estatal (PL 08488, Plan Nacional de Telesalud) e infraestructura de delivery ya
  a escala (tesis 9) hacen esta una apuesta con demanda y canal ya validados —
  no hay que crear el hábito de ir a la farmacia, ya existe. **Condición dura:**
  el triage IA solo se lanza después de un silent trial de 60-90 días (tesis
  10); saltarse ese paso es repetir el error de Babylon con capital propio.
- **Material comparativo visual estructurado, no reducción de catálogo.** Tesis
  12: invertir en icon arrays y estructura "good-better-best" en el punto de
  venta consultiva, no en podar opciones de producto — la evidencia dice que la
  fricción es de comparación, no de cantidad.
- **Divulgación progresiva para el onboarding de pricing por datos/telemática.**
  Tesis 13: pedir consentimiento de UBI/pricing IA en pasos ligados a marca de
  confianza, campo por campo, en vez de un formulario legal único — convierte
  mejor sin depender de cambiar la actitud del cliente hacia la privacidad.
- **Distribución por intermediario humano de confianza — pero estrictamente
  inbound/opt-in, nunca llamada en frío.** Ya no es solo instinto: tesis 16 le da
  respaldo A/B convergente en tres mercados de alta digitalización (Corea, China,
  caso Lemonade) de que el intermediario no desaparece en productos complejos —
  se redistribuye hacia ellos. El riesgo regulatorio de tesis 8 sigue vigente:
  cualquier variante de contacto saliente no consentido es una apuesta con S/2M+
  de multa potencial y precedente directo contra un competidor. La jugada válida
  es bróker como canal de confianza que el cliente busca (referidos, punto de
  venta), no como fuerza de prospección saliente.
- **Invertir en herramientas para el asesor humano en el momento del reclamo, no
  en digitalizar el reclamo completo.** Tesis 16: 33-39% de reclamos 100%
  digitales fallan y requieren rescate humano, y el que escala tarde reporta peor
  experiencia (NPS -11) que un canal humano directo. La jugada de mayor ROI en
  siniestros complejos es un flujo híbrido bien diseñado desde el inicio, no un
  "self-service" que empuja al cliente frustrado a escalar tarde.
- **Integración vertical seguro + farmacia como motor de utilidad real, no solo
  de acceso/distribución.** Tesis 17 eleva la oportunidad de tesis 9
  (farmacia-frente-primario en Perú): en el mercado que mejor se documenta hoy
  (EE.UU.), la utilidad real del sector de salud vive en el negocio de farmacia
  integrado (PBM), no en el margen de suscripción (delgado por diseño
  regulatorio). Un modelo peruano que combine aseguramiento + farmacia bajo un
  mismo techo no es solo un canal de distribución más barato — replica el
  mecanismo por el que el asegurador de salud más grande del mundo genera
  utilidad real hoy. **Instinto, no probado en Perú:** el dato es de EE.UU.; no
  hay cifra local de margen de farmacia vs. margen de aseguradora todavía.
- **Estrategia explícita de costo de medicamentos especializados (GLP-1 y
  análogos), no solo "contener costo médico" en genérico.** Tesis 17: es el
  driver de costo más agudo y actual documentado, con saltos de #32 a #1 en el
  gasto farmacéutico de un empleador en un solo año — cualquier diseño de
  producto de salud/farmacia en el modelo debería presupuestar este rubro
  específico, no tratarlo como "inflación médica" genérica.
- **Pricing dinámico por uso (UBI) como producto, no como campaña de nudge.**
  Tesis 7 lo prueba con outcome real, pero extenderlo (salud, hogar) debe
  presupuestar una curva de adopción lenta por el techo de confianza documentado
  incluso en mercados maduros — no asumir adopción masiva rápida.
- **Posicionar `lapuerta` en la frontera de "AI Behavioral Science".** La agenda
  formal del subcampo recién se está formando (F-27, preprint). *Instinto*: vale
  la pena posicionar el trabajo como caso aplicado temprano antes de que el
  subcampo se sature.
- **Programa de alfabetización conductual específica (miopía, narrow framing),
  no educación financiera genérica.** Tesis 14: complemento —no sustituto— de
  rediseñar el producto (tesis 1/2/12); ataca el marco mental que hace que la
  gente no vea sus decisiones de seguro como parte de un mismo portafolio de
  riesgo.
- **Rediseñar cifras headline de retorno como monto, no como porcentaje, y
  nunca mostrar datos "a confirmar" en piezas cliente-facing.** Tesis 15: el
  mismo cambio de diseño reduce a la vez el riesgo regulatorio-reputacional y
  la fuga de conversión por desconfianza — no son dos arreglos distintos, es
  uno solo con doble retorno.
- **Calculadora de precio real en el punto de entrada de vida individual, no
  al final del funnel.** Tesis 20: ataca directamente la sobreestimación de
  7-12x que bloquea la conversación antes de que empiece — acompañada de FAQ
  con íconos/resúmenes de saliencia, no de lenguaje simplificado solo (F-231
  ya muestra que eso no basta).
- **Abrir el copy de vida individual con la pregunta que el cliente ya hace en
  abierto ("¿vale la pena?"), no con definiciones técnicas.** Señal social
  débil (🔴E, tesis 20) pero coherente con el patrón cuantificado del precio
  percibido — empezar el glosario/FAQ por ahí, dejar el vocabulario técnico
  (prima, endoso, coaseguro) como segunda capa, igual que ya se decidió para
  el glosario de salud.
- **Perfilar campañas y bundling de vida individual por motivación (proteger /
  crecer / meta / rentabilizar), no por edad/NSE/ocupación.** Tesis 19: ya no
  es solo intuición de producto — tiene respaldo empírico específico del
  sector financiero (F-229) y marco psicológico robusto (F-230) de que la
  motivación predice mejor la conducta que la categoría demográfica asignada.
- **Instrumentar la causa raíz del 59% de cancelación voluntaria (APC), no solo el score.**
  Tesis 21: RIMAC ya identifica *quién* va a cancelar con precisión por encima del
  benchmark de industria — el ROI marginal más alto ya no está en mejorar el modelo, está en
  capturar *por qué* decide irse (precio, servicio, competencia) con una encuesta de salida
  o modelo de causa raíz, para poder diseñar tratamientos distintos en vez de una sola
  gestión de retención genérica sobre un evento que mezcla al menos tres causas distintas.
- **Diseñar oferta específica para el cuadrante "alta siniestralidad + baja persistencia" en
  AMI, antes de que el cliente decida irse.** Tesis 21: si el patrón de selección adversa
  dinámica aplica (marco teórico, no confirmado con el dato disponible), ese cuadrante es
  el de mayor pérdida potencial doble — se va Y cuesta caro mientras se queda — y es
  exactamente el segmento que la matriz Persistencia × Siniestralidad ya aísla, sin que
  ningún documento interno proponga todavía una jugada específica para él.

## ⚠️ Riesgos

- **Vender "educación financiera"/glosario como la solución, sin rediseñar el producto,
  puede leerse como desvío de responsabilidad — no solo como ROI débil.** Tesis 6
  (revisión profunda 2026-07-22, F-19): el caso documentado de BP acuñando "huella de
  carbono" en 2004 para reencuadrar el cambio climático como problema individual mientras
  cabildeaba contra regulación sistémica es el precedente nombrado de esta dinámica.
  Riesgo reputacional, no solo de conversión: cualquier campaña de "educamos al
  consumidor" sin acompañarla de cambios reales de producto (deducible fijo en vez de
  coaseguro, tesis 2; icon arrays, tesis 12) corre el riesgo de leerse —o de funcionar—
  como desvío de responsabilidad hacia el cliente.
- **Contacto comercial no consentido, con precedente ya dentro del sector
  seguros.** Tesis 8: Pacífico Seguros bajo investigación directa, BBVA
  sancionado dos veces, INDECOPI escaneando millones de audios con IA. Cualquier
  call center o campaña saliente sin consentimiento explícito y verificable hoy
  arriesga multa de hasta 450 UIT y una orden de cese que borra bases de datos
  completas, incluidas las de terceros (agencias, referidos).
- **Lanzar un triage con IA sin shadow-mode previo.** Tesis 10: el precedente
  Babylon Health (USD 4.2B → bancarrota) y la precisión real de ~45% de los
  symptom-checkers en producción hacen que cualquier lanzamiento sin 60-90 días
  de silent trial sea apostar capital contra un patrón de fracaso ya documentado.
- **Tratar el modelo de atención primaria basada en valor (capitación,
  farmacia-como-frente-primario) como camino rápido a rentabilidad.** Los casos
  internacionales que mejor navegan la presión de costo (Singapur, NHS, Kaiser,
  Oak Street, ChenMed) son arquitecturas sólidas a largo plazo, pero
  financieramente lentas: Oak Street operaba con pérdidas >USD 200M/año al
  momento de ser adquirida por USD 10.6B, y hasta Kaiser —líder de la categoría—
  enfrentó presión de costos crecientes en 2025. Dimensionar la oportunidad de
  tesis 9 con expectativa de rentabilidad de corto plazo es un error de
  proyección, no de estrategia.
- **Sobreclamar capacidad de IA en comunicación pública (claims, pricing,
  antifraude).** Lemonade tuvo que retractarse públicamente tras presumir en
  redes que su IA analiza señales faciales para detectar fraude — la reacción
  viral por "fisonomía" sigue citándose como caso de cautela cinco años después.
  Mismo patrón que el riesgo ya señalado sobre Vitality (F-25): dato de negocio
  autopublicado o comunicación pública sobre IA en seguros necesita revisión de
  riesgo reputacional antes de salir, no solo revisión legal.
- **Medir el agente conversacional de IA con la métrica equivocada.** Si el
  agente de RIMAC se evalúa solo por tasa de resolución o satisfacción
  autorreportada, no se está midiendo si **alucina coberturas o pólizas que no
  existen** — el estándar de la industria para eso es distinto (RAGAS mide
  fidelidad al contexto recuperado verificando cada afirmación por separado;
  G-Eval/MT-Bench puntúan la respuesta individual, no la experiencia agregada).
  Es un riesgo silencioso: un agente puede "sonar bien" en una encuesta de
  satisfacción y seguir inventando datos de producto.
- **Quemar presupuesto de marketing en "educación financiera" esperando ventas.**
  Tesis 1, ahora con respaldo adicional específico de seguros (F-124). Si el
  objetivo real es conversión, ese presupuesto rinde más en simplificación de
  producto o en material comparativo estructurado (tesis 12).
- **Lanzar producto Gen Z con coaseguro variable pensando que "ya van a entender".**
  Tesis 2 + 3 combinadas.
- **Dimensionar un caso de negocio de seguros de desastres con el 3.3% sin
  verificar la fuente primaria.** Sigue siendo un número de gremio vía prensa, no
  auditado — aunque la jugada de producto (paramétrico) ya no depende solo de
  ese número exacto (tesis 4).
- **F-15 sigue marcada "NO USAR" en el ledger** (cifra de UnitedHealth sin método
  verificable). Cuidado con que se cuele en algún deck o caso de negocio.
- **Dimensionar el ROI de un nudge con el tamaño de efecto de un paper
  académico.** Tesis 6: "voltage drop" de ~6x entre campo y laboratorio.
- **Confiar en estudios de "honestidad"/nudges éticos sin verificar su
  integridad.** El escándalo Ariely/Gino (F-24) mostró fabricación de datos en
  investigación ampliamente citada por la industria de seguros — verificar que
  no sea parte del corpus retractado antes de citarlo para diseñar un formulario
  o proceso antifraude.
- **Usar la divulgación progresiva de datos (tesis 13) sin límite ético.** El
  mismo mecanismo que aumenta conversión de datos funciona "aunque no debería" —
  usarlo para maximizar divulgación sin que el cliente entienda realmente qué
  autorizó es un riesgo reputacional y regulatorio (LPDP exige consentimiento
  informado e inequívoco), no solo una táctica de UX.
- **La tenencia de seguros de vida en EE.UU. cayó de 63% (2011) a 51% (2024)**
  pese a que las intervenciones de comprensión sí mejoran el journey de compra
  puntual. Refuerza tesis 1 en la dirección más incómoda.
- **Publicidad con cifra de retorno garantizado en % como elemento dominante,
  y datos "a confirmar" visibles en piezas que llegan al cliente.** Tesis 15:
  patrón ya sancionado por Indecopi en un caso comparable (BBVA, 2025); no es
  solo un riesgo de conversión (ancla + desconfianza), es un riesgo de multa y
  orden de cese sobre material que ya está circulando o por circular.
- **Apostar por "reemplazar al asesor" en productos complejos (vida, salud,
  siniestros) en vez de darle mejores herramientas.** Tesis 16: en los dos
  mercados más digitalizados investigados (Corea, China) el canal humano no
  perdió terreno en el segmento de mayor valor — perderlo sería repetir un error
  ya documentado, no una apuesta original.
- **Lanzar un flujo de reclamos 100% digital sin ruta de escalamiento humano bien
  diseñada.** Tesis 16: 33-39% de reclamos digitales fallan igual, y escalar
  tarde/mal genera peor experiencia (NPS -11) que atender el reclamo con un
  humano desde el inicio — el "self-service primero, humano de rescate" mal
  ejecutado es la peor de las tres opciones, no la más barata.
- **Dimensionar el modelo de farmacia-frente-primario (tesis 9) solo como
  ahorro/acceso, sin ver la integración vertical como motor de utilidad
  propio.** Tesis 17: en EE.UU. la utilidad real del sector de salud está en el
  negocio de farmacia integrado (PBM), no en el margen de suscripción — dato de
  filing primario (Optum Rx), no de prensa. Extrapolar el mecanismo exacto a
  Perú sin dato local es instinto, pero ignorarlo por completo en el diseño del
  modelo sería descartar la señal más fuerte (🟢A) que entró al ledger esta
  semana sobre dónde está la plata en salud.
- **Corrección de proceso, no de evidencia:** el ledger de fuentes se renombró
  de `registro_fuentes.md` a `codice.md` el 2026-07-19; las revisiones diarias
  del 2026-07-13 al 2026-07-19 leyeron una ruta que había quedado congelada en
  F-27 y reportaron "sin novedad" siete días seguidos — mientras tanto, entre el
  2026-07-06 y el 2026-07-19 ya se habían registrado 144 fuentes nuevas (F-28 a
  F-171) vía `/trinidad` y `/seeker` que nunca llegaron a esta opinión. La
  lectura de hoy (2026-07-20) contra `codice.md` es la que corrigió esto. Tesis
  3 y 4 seguían correctamente congeladas en Media (no había evidencia
  generacional/sísmica nueva específica), pero el resto de la cartera estaba
  desactualizada sin que la bitácora lo supiera. Vigilar que futuras revisiones
  lean siempre la ruta vigente indicada en `CLAUDE.md`, no una ruta fija
  hardcodeada.
- **Enseñar "regla del 10x" a la fuerza de venta como si fuera un sesgo cognitivo con la misma
  autoridad que anclaje o aversión a la pérdida.** Tesis 18: es una heurística de metas de un
  libro motivacional, no ciencia conductual — si se corrige el Bloque 4 del Playbook agregando
  citas a las otras 7 técnicas sin corregir esta, el efecto neto es darle a una idea sin evidencia
  el mismo peso visual que a las que sí la tienen, un riesgo de credibilidad silencioso si algún
  día alguien en Legal/Compliance o el propio VP pide la fuente de cada "sesgo".
- **Optimizar el glosario/calculadora de vida individual solo para bajar el precio percibido, sin
  explicar bien la declaración de salud.** Tesis 20: la distinción legal entre dolo/culpa grave
  (puede anular la póliza o negar el siniestro) y omisión involuntaria de algo leve (típicamente
  solo ajusta la prima) es real y consecuente — omitirla del material orientado a conversión deja
  al cliente firmando sin entender un riesgo concreto de negación de reclamo, exactamente el
  momento de mayor fricción reputacional (siniestro), no un tecnicismo legal menor. Nota de
  proceso: la aplicación exacta al marco normativo peruano no está verificada — usar como
  lenguaje orientativo, no como texto legal validado por Legal/Cumplimiento.
- **Asumir que el esquema de segmentación de `lapuerta` (mayormente demográfico: NSE, generación,
  región) captura lo que de verdad predice conducta de seguros.** Tesis 19: la evidencia
  específica de servicios financieros dice que la demografía explica poco frente a la motivación
  subyacente. Instinto, no diagnóstico confirmado sobre el propio modelo — pero ignorarlo sin
  evaluarlo en la próxima revisión de variables sería descartar la señal más directa que ha
  entrado al ledger sobre el propio diseño de segmentación de `lapuerta`.
- **Comparar los dos decks de churn/renovación de RIMAC asumiendo que sus términos significan lo
  mismo.** Tesis 21: "% Efectividad" es recall en el deck de Churn y precisión en el de
  Renovación — mismo nombre, definición opuesta. Sumado a 4 láminas ocultas con contenido
  incompleto (placeholders sin llenar) y al menos 3 inconsistencias puntuales detectadas
  (etiqueta cruzada VEH/AMI, campo vacío, valores idénticos entre segmentos que deberían
  diferir), el riesgo no es que el modelo esté mal — es que alguien tome una decisión de negocio
  citando el número equivocado por leer ambos documentos como si compartieran vocabulario.
- **Confundir "el modelo concentra bien el evento" con "la gestión ya reduce el churn real."**
  Tesis 21: tanto el deck de Churn como el de Renovación validan con backtest fuera de tiempo —
  miden qué tan bien habría funcionado el score en el pasado, no el efecto de una intervención
  real ya desplegada. Dimensionar el ROI del piloto (próximo hito, sin fecha en el deck de
  Renovación) con el mismo nivel de confianza que el score de concentración sería repetir, en
  analítica de retención, el mismo error que tesis 6 ya señaló para el nudge: tamaño de efecto
  de laboratorio/backtest no es tamaño de efecto de campo.

## 📔 Bitácora

- **2026-07-12** — Primera creación de la opinión. Revisé las 15 fuentes del
  ledger (F-1 a F-15). Construí 5 tesis iniciales: (1) la divulgación no
  convierte, (2) el coaseguro es el cuello de botella de comprensión, (3) el
  problema es estructural/no generacional, (4) la brecha sísmica peruana es una
  categoría casi vacía, (5) ESG es palanca global, no probada en Perú. Marqué 3
  oportunidades y 4 riesgos, incluyendo la advertencia de no usar F-15.
- **2026-07-12** — El ledger creció a F-27 (`/trinidad` sobre behavioral
  design). Sumé tesis 6 (crisis del nudge) y tesis 7 (s-frame > i-frame, caso
  UBI). Agregué 2 oportunidades y 4 riesgos nuevos (ROI de nudge sobreestimado,
  corpus retractado Ariely/Gino, Vitality como dato autopublicado, caída de
  tenencia de vida en EE.UU.).
- **2026-07-13 a 2026-07-19** — Siete revisiones diarias consecutivas
  reportaron "sin cambios sustanciales" contra `registro_fuentes.md`, fijo en
  F-1 a F-27. Único ajuste real en esa ventana: se puso tope explícito de
  confianza a tesis 3 y 4 (no suben por consistencia narrativa, solo por fuente
  B+ directa) y se fijó un checkpoint para el 2026-07-21 (próxima corrida de
  `cerrajero`). *Nota de la revisión de hoy:* esta racha de "sin novedad" fue en
  parte un artefacto de ruta de archivo (ver entrada 2026-07-20) — el ledger
  real sí creció durante esta ventana, solo que bajo un nombre de archivo
  distinto (`codice.md`, vigente desde el 2026-07-19).
- **2026-07-20** — Cambio sustancial: leí el ledger vigente (`codice.md`, ahora
  con 171 fuentes) y encontré 144 fuentes nuevas (F-28 a F-171) nunca antes
  incorporadas a esta opinión, producto de `/trinidad`/`/seeker` entre el
  2026-07-06 y el 2026-07-19 (salud/farmacias/PL 08488, mecanismos de seguros de
  salud, material visual de venta consultiva, transición venta fría→opt-in,
  evaluación de agentes conversacionales de IA, y datos de rentabilidad/mercado
  global de seguros). Sumé 6 tesis nuevas (8-13): riesgo regulatorio de contacto
  no consentido ya activo contra Pacífico Seguros y BBVA; oportunidad de
  farmacia+triage IA validada por señal estatal e infraestructura real; riesgo
  de sobreclamar precisión clínica de IA (caso Babylon); ciclo de rentabilidad
  del seguro global en máximo de 25 años; choice overload como folklore de UX
  (la palanca real es estructurar, no podar catálogo); y divulgación progresiva
  de datos como mecanismo de conversión que funciona incluso sin cambiar la
  actitud real del cliente hacia su privacidad. Actualicé tesis 4 (paramétrico
  ahora con mercado/diseño técnico real detrás, no solo instinto) y tesis 7
  (UBI funciona pero con techo de confianza documentado). Reescribí
  Oportunidades y Riesgos para reflejar todo esto, incluyendo un riesgo de
  proceso: la racha de "sin cambios" de la semana pasada fue en parte un
  artefacto de que se leía una ruta de archivo congelada, no evidencia real de
  estancamiento del ledger.
- **2026-07-21** — Primera corrida de la rutina de **revisión profunda** (cada
  ~3 días, lee 5 fuentes del ledger a fondo en vez de solo su resumen de una
  línea). Revisadas F-3, F-6, F-9, F-10 y F-16 (las 5 fuentes 🟢A de ID más
  antiguo, ninguna tenía revisión profunda previa — ver
  `research/fuentes/revision_profunda.md`). Encontré y corregí un error de
  atribución en el ledger (F-3 decía "Platteau", son Pitthan & De Witte). Sumé
  tesis 14 (miopía/narrow framing como mecanismos específicos de subaseguración,
  distintos de "sesgos" en genérico). Agregué matiz de mecanismo (no solo
  resultado) a tesis 1 (creencia pesimista + recorte de información como causa
  de por qué la divulgación no convierte), a tesis 2 (comprensión ≠ preferencia,
  tope heredado de tesis 1) y a tesis 6 (el ranking por técnica/dominio dentro
  del propio meta-análisis de Mertens favorece probar defaults primero en
  salud/finanzas). Ningún cambio de confianza hacia abajo esta vez — las 5
  lecturas profundizaron el mecanismo sin contradecir el resumen previo.
  Enriquecí en paralelo 3 nodes de Many Brains (`seguros-comportamiento-mundo-peru.md`,
  `glosario-seguro-salud-peru.md`, `behavioral-design-estado-disciplina.md`) con
  las mismas citas, sin mover ni reestructurar nada.
- **2026-07-21 (proceso diario)** — Corrida separada del proceso diario de
  refinamiento (distinto de la revisión profunda de más arriba, que corrió antes
  hoy mismo vía `cronista`). Comparé `codice.md` contra la última entrada de la
  bitácora: el ledger sigue tope en F-171, sin fuentes nuevas desde la revisión
  profunda de esta mañana — **sin cambios sustanciales** en evidencia. Sí agregué
  un matiz a tesis 4 (seguro paramétrico sísmico): conecté el mecanismo de
  narrow framing de la tesis 14 recién creada con la brecha de aseguramiento
  sísmico — un hogar que asegura su auto pero no su casa contra sismo no
  necesariamente desconfía del producto, puede estar evaluando cada póliza de
  forma aislada en vez de como un mismo portafolio de riesgo. Marcado
  explícitamente como **instinto** (razonamiento propio conectando dos tesis ya
  existentes), no como dato nuevo — ningún nivel de confianza numérico cambió
  por esto. Ninguna otra tesis, oportunidad o riesgo requirió ajuste.
- **2026-07-21 (segunda corrida del día)** — El ledger creció de F-171 a F-179
  entre la corrida anterior de hoy y esta: `/trinidad` revisó un artefacto
  concreto (flyers "Vida Ahorro") y registró 8 fuentes nuevas sobre publicidad
  de retorno garantizado — efecto de anclaje de cifras prominentes (F-175, A),
  un modelo regulatorio de referencia que restringe expresar retorno como %
  (F-172, B, EE.UU.), el marco peruano de Indecopi sobre publicidad engañosa
  (F-173, B) y un caso real de sanción a una entidad financiera comparable
  (F-174, BBVA 2025, D), más evidencia de que información incompleta visible
  al cliente reduce confianza y disposición a comprar (F-176 A, F-177 D) y de
  que contenido emocional e informativo son complementarios, no sustitutos
  (F-178 A, F-179 D). Sumé tesis 15 (cifra headline en % = ancla persuasiva +
  riesgo regulatorio simultáneo, mismo origen) y una oportunidad/riesgo
  espejados. Confianza fijada en Alta para el patrón de riesgo, Media para si
  Indecopi sancionaría específicamente el caso "% vs. monto" — el marco
  peruano no se investigó al mismo nivel de detalle que el modelo de EE.UU.
  citado como categoría de riesgo. Ninguna tesis previa (1-14) requirió
  ajuste de confianza. *Limpieza de proceso:* removí una etiqueta `</content>`
  suelta al final del archivo, remanente de una operación de escritura
  anterior — no era contenido de El Lobo.
- **2026-07-22** — Corrida diaria de refinamiento. Leí `codice.md` completo:
  sigue tope en F-179, sin fuentes nuevas desde la segunda corrida de ayer
  (2026-07-21) — **sin cambios sustanciales** en evidencia. Repasé las 15
  tesis contra ese mismo tope y ninguna quedó desalineada con el ledger
  vigente; tampoco encontré una conexión razonable nueva entre tesis que
  valiera la pena marcar como instinto sin forzarla — prefiero no sumar un
  matiz artificial un día después de que la revisión de ayer ya conectó lo
  disponible (tesis 4↔14 sobre narrow framing, tesis 15 sobre anclaje +
  riesgo regulatorio). Próximo salto de tesis/confianza queda condicionado a
  que `/trinidad`, `/seeker`, `/gossip` o `/marketer` registren fuentes
  nuevas en el ledger, o a que la próxima revisión profunda (rutina de
  `cronista`, cada ~3 días) encuentre un matiz de mecanismo al leer una
  fuente ya citada a fondo.
- **2026-07-22 (revisión profunda)** — Segunda corrida de la rutina de revisión
  profunda (cada ~3 días). Las 5 fuentes 🟢A de ID más antiguo sin lectura profunda
  previa eran F-17 a F-21 — el mismo cluster que ya sostenía tesis 6 (crisis del
  nudge), todas con solo el resumen de una línea del ledger hasta hoy — ver
  `research/fuentes/revision_profunda.md`. Nota de acceso: los URLs directos
  (PNAS, Wiley, SSRN, Nature, NBER) devolvieron 403 en esta sesión — el proxy de
  red del entorno bloquea todo tráfico saliente directo, confirmado con curl
  crudo, no es un bloqueo específico de estas fuentes — así que la lectura
  profunda se hizo vía múltiples búsquedas dirigidas que devolvieron contenido
  sustancial de cada paper (cifras exactas, metodología, citas textuales), no
  solo el resumen que ya tenía el ledger. Profundicé tesis 6 con tres hallazgos:
  (1) tres metodologías independientes (RoBMA de Maier, meta-meta-análisis de Hu
  et al. a ~30M de participantes con caída de d=0.27 a d=0.004, y la
  descomposición de DellaVigna & Linos que atribuye toda la brecha "voltage
  drop" a sesgo de publicación) convergen en que el efecto promedio del nudge
  publicado estaba inflado por sesgo de publicación, no por una brecha
  laboratorio-vs-mundo-real — con el caveat de que el corpus de Hu et al. es en
  su mayoría de calidad AMSTAR-2 baja/crítica; (2) el megastudy de Milkman en
  detalle (54 programas, 61,293 personas) da una receta de diseño concreta: el
  nudge que más funcionó apuntó al momento de recaída, no a la adherencia
  general; (3) Chater & Loewenstein documentan que BP acuñó "huella de carbono"
  en 2004 para reencuadrar el cambio climático como responsabilidad individual
  mientras cabildeaba contra regulación sistémica — mecanismo de negocio, no
  solo académico, para el sesgo hacia el i-frame, que conecté como riesgo nuevo
  (no solo de ROI sino reputacional) a la práctica de vender solo "educación
  financiera" sin rediseñar producto. Ningún cambio de confianza hacia abajo;
  tesis 6 se mantiene en Alta, ahora con base metodológica más amplia. Enriquecí
  en paralelo el node `_nodes/behavioral-design-estado-disciplina.md` (pista
  empírica y tabla de rigurosidad) con las mismas citas, sin mover ni
  reestructurar nada.
- **2026-07-23** — Corrida diaria de refinamiento. El ledger creció de F-179 a
  F-202 desde la última corrida (2026-07-22): una investigación `/trinidad`
  completa sobre el futuro de los asesores de seguros frente a la venta 100%
  digital (F-180 a F-192, node nuevo `_nodes/futuro-asesores-seguros-venta-digital.md`)
  y una ampliación del node `mecanismos-seguros-salud.md` con datos de balance
  financiero/rentabilidad de seguros de salud en EE.UU. (F-193 a F-202) —
  **cambio sustancial**. Sumé tesis 16 (el asesor no desaparece con lo digital,
  se redistribuye por complejidad de producto; el reclamo, no la venta, es
  donde falla lo 100%-digital) y tesis 17 (la utilidad real del seguro de salud
  vive en la integración vertical con farmacia/PBM, no en el margen de
  suscripción — dato sostenido por un filing SEC primario, 🟢A). Tesis 17
  refuerza directamente a tesis 9 (farmacia-frente-primario en Perú): ya no es
  solo oportunidad de acceso/distribución, es el mismo mecanismo de utilidad
  del asegurador de salud más grande del mundo — marcado explícitamente como
  instinto en la extrapolación a Perú, porque no hay dato local de margen de
  farmacia vs. margen de aseguradora en el ledger todavía. Añadí 4
  oportunidades y 3 riesgos nuevos reflejando ambas tesis (herramientas para el
  asesor en el momento del reclamo en vez de digitalizarlo por completo;
  integración farmacia+seguro como motor de utilidad; estrategia explícita de
  costo de medicamentos especializados/GLP-1). Ninguna tesis previa (1-15)
  requirió ajuste de confianza — el ledger nuevo no las tocó.
- **2026-07-24** — Corrida a pedido explícito del usuario: "revisa todo el conocimiento sobre la
  venta de seguros de vida en RIMAC y analízalo con el lobo para reforzar los argumentos". Audité
  el Bloque 4 del Playbook del Asesor (`_nodes/proyecto-back-to-basics-ffvv-vida.md` §5,
  Hallazgo 2) — 9 "sesgos cognitivos" (C.1-C.9) sin una sola cita en el documento original.
  Primera pasada trabajó solo sobre el resumen del proyecto (sin numeración C.n exacta); al pedir
  el usuario aplicar los cambios, releí el documento real `Playbook_del_asesor.md` y corregí la
  numeración + encontré una novena técnica (C.4, sesgo del presente) que la primera pasada no
  había cubierto. Resultado final: 8 de 9 sí tienen respaldo fundacional real (Kahneman, Tversky,
  Thaler, Cialdini, y F-3 ya existente para sesgo del presente), la novena (C.7, "regla del 10x")
  resultó ser una heurística de metas de un libro de ventas motivacional (Cardone 2011), no
  ciencia conductual — mal categorizada junto a las demás. Sumé tesis 18 con este hallazgo, un
  riesgo nuevo (enseñar la regla del 10x con la misma autoridad que un sesgo real), y F-220 a
  F-228 al ledger (8 fuentes nuevas + reutilización de F-3 ya existente: 6 fundacionales de
  sesgos reales, 1 cita real con encaje de dominio cuestionable, 1 fuente que confirma que algo
  NO es ciencia conductual, y Sweller 1988 para fortalecer Dx3 del Modelo de Experiencia de Venta
  Vida con base académica explícita). Inserté las 8 citas directamente en el documento real del
  Playbook (no solo en el ledger) y envié la versión corregida al usuario. Ninguna tesis previa
  (1-17) requirió ajuste de
  confianza — es evidencia nueva sobre un documento del proyecto, no sobre el ledger externo
  existente.
- **2026-07-24 (proceso diario)** — Corrida automática diaria de refinamiento, separada de la
  auditoría a pedido del usuario que ya corrió hoy mismo (entrada anterior). Confirmé que
  `codice.md` sigue tope en F-228 — verifiqué la secuencia completa F-1 a F-228 sin huecos, sin
  fuente nueva registrada desde la corrida anterior de hoy — **sin cambios sustanciales** en
  evidencia. Repasé las 18 tesis contra ese mismo tope: ninguna quedó desalineada con el ledger
  vigente. No forcé ninguna conexión nueva entre tesis solo por completar el paso — la corrida de
  hoy ya conectó lo disponible (tesis 18 sobre el Playbook). Próximo salto de tesis/confianza
  queda condicionado a que `/trinidad`, `/seeker`, `/gossip`, `/marketer` o `cronista` registren
  fuentes nuevas en el ledger.
- **2026-07-25** — Corrida diaria de refinamiento. El ledger creció de F-228 a F-235 desde la
  última corrida (2026-07-24): una investigación `/trinidad` sobre el glosario de seguro de vida
  en lenguaje sencillo y el perfilamiento por motivación (nodes nuevos
  `_nodes/glosario-seguro-vida-peru.md` y `_nodes/matriz-productos-vida-rimac.md`, ampliación de
  `_nodes/proyecto-back-to-basics-ffvv-vida.md`) — **cambio sustancial**. Sumé tesis 19
  (perfilar por motivación, no por demografía, tiene ahora respaldo A+A específico de servicios
  financieros — y puede exponer un punto ciego estructural en el propio esquema de `lapuerta`,
  construido mayormente sobre variables demográficas) y tesis 20 (en vida individual, el freno
  más caro no es la incomprensión del producto sino un precio percibido 7-12x inflado; solo
  saliencia+calculadora lo revierte, no lenguaje simple solo). Añadí 3 oportunidades (calculadora
  de precio en el punto de entrada, abrir el copy con "¿vale la pena?" en vez de tecnicismos,
  perfilar campañas por motivación) y 2 riesgos nuevos (glosario/calculadora que omite la
  distinción legal dolo/culpa grave vs. omisión en declaración de salud; el propio esquema de
  `lapuerta` sin evaluar frente a la señal de que la demografía predice poco en este sector).
  Ninguna tesis previa (1-18) requirió ajuste de confianza — el ledger nuevo no las tocó
  directamente, aunque tesis 19 se conecta con instinto explícito al diseño de `lapuerta` sin
  tocar su esquema todavía. Mantuve la bitácora sin podar — con 14 días de historial
  (2026-07-12 a hoy) sigue dentro de la ventana de ~30 días indicada.
- **2026-07-26** — Corrida diaria de refinamiento. Confirmé `main` actualizado (fast-forward
  78584ad→b74f2a1) y leí `codice.md` completo: sigue tope en F-235, sin fuente nueva registrada
  desde la corrida de ayer (2026-07-25) — **sin cambios sustanciales** en evidencia. Repasé las 20
  tesis contra ese mismo tope: ninguna quedó desalineada con el ledger vigente. No forcé ninguna
  conexión nueva entre tesis solo por completar el paso — tesis 19 y 20 (las más recientes) ya
  quedaron conectadas con el resto de la cartera en la corrida de ayer. Próximo salto de
  tesis/confianza queda condicionado a que `/trinidad`, `/seeker`, `/gossip`, `/marketer` o
  `cronista` registren fuentes nuevas en el ledger. Bitácora con 15 días de historial
  (2026-07-12 a hoy), dentro de la ventana de ~30 días — sin podar todavía.
- **2026-07-30** — Corrida a pedido explícito del usuario: "usa trinidad y el lobo para
  analizar" un documento nuevo (`Analisis_Detallado_Churn_Renovacion.md`, análisis detallado de
  2 decks internos de RIMAC sobre modelos de churn y matriz de renovación AMI/VEH), persistido
  en `research/_fuentes_internas/`. Corrí `/trinidad` para validar externamente 4 preguntas
  concretas del documento (benchmark de concentración/lift de churn, cancelación voluntaria vs.
  morosidad como patrón de industria, selección adversa dinámica para el patrón inverso
  persistencia-siniestralidad AMI/VEH, y ventanas de gestión anticipada) — registré F-388 a
  F-392 en el ledger y creé el node `_nodes/modelo-churn-renovacion-rimac.md` (v1.0) con el
  detalle completo. Sumé tesis 21: RIMAC ya tiene capacidad de detección de churn por encima del
  benchmark académico publicado (lift x11.6 en el score top de Morosidad vs. x3.01 reportado
  como mejor caso en la literatura) — el vacío de mayor valor de negocio no es el modelo, es que
  ningún documento interno reporta la causa raíz del 59% de cancelación voluntaria (APC), pese a
  que esa proporción (voluntaria > involuntaria) es consistente con una tendencia de industria
  más amplia, no una anomalía local. Señalé como divergencia explícita (no forzada) que el marco
  teórico más cercano para el patrón AMI/VEH (selección adversa dinámica) no se puede confirmar
  1:1 porque el dato de RIMAC es predictivo, no retrospectivo. Añadí 2 oportunidades
  (instrumentar causa raíz de APC; oferta para el cuadrante alta-siniestralidad/baja-persistencia
  en AMI) y 2 riesgos (comparar ambos decks asumiendo vocabulario compartido — "% Efectividad"
  significa cosas opuestas en cada uno; confundir buena concentración de backtest con evidencia
  de que la gestión real reduce el churn, mismo error de tesis 6 aplicado a retención). Ninguna
  tesis previa (1-20) requirió ajuste de confianza — es evidencia nueva sobre un documento del
  proyecto, no sobre el ledger externo existente. Bitácora con 18 días de historial
  (2026-07-12 a hoy), dentro de la ventana de ~30 días — sin podar todavía.
