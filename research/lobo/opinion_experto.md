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
- **Evidencia:** F-16, F-17, F-18, F-20, F-21 (todas 🟢A)
- **Confianza:** Alta
- **Actualizado:** 2026-07-21

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
  inbound/opt-in, nunca llamada en frío.** *Parcialmente instinto, parcialmente
  ledger-backed*: en mercados de baja confianza institucional la intermediación
  humana suele convertir mejor que el canal digital directo, pero el riesgo
  regulatorio de tesis 8 hace que cualquier variante de contacto saliente no
  consentido sea hoy una apuesta con S/2M+ de multa potencial y precedente
  directo contra un competidor. La jugada válida es bróker como canal de
  confianza que el cliente busca (referidos, punto de venta), no como fuerza de
  prospección saliente.
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

## ⚠️ Riesgos

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
</content>
