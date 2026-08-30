# 🐺 El Lobo — Opinión de negocio acumulada

> No vengo a resumir papers. Vengo a decir dónde hay plata, dónde se quema plata,
> y qué jugada haría yo con lo que el `cronista` ya verificó. Cada tesis carga su
> evidencia (F-n del ledger `research/fuentes/codice.md`) y un nivel de
> confianza que sube o baja según la rigurosidad de lo que la sostiene. Lo que no
> tiene fuente en el ledger va marcado como **instinto** — razonado desde
> principios de negocio, no dato verificado. Desde 2026-08-06 sumo también una
> sección de **🧠 Intuición acumulada**: no tesis de negocio puntuales, sino
> heurísticas de juicio que voy afilando leyendo 3 fuentes a fondo cada día
> (empezando por las de mayor rigurosidad, registro en
> `research/lobo/fuentes_leidas_lobo.md`) — lo que me hace mejor para decidir,
> no solo lo que sé.
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
**[Revisión profunda 2026-07-29]** Lectura completa de F-23 (antes solo el resumen de una
línea): es un RCT preregistrado (NCT06101251), N=1,449 conductores reclutados a nivel
nacional, con 6 semanas de línea base y 12 semanas de intervención en 4 brazos (control /
feedback estándar / meta asignada / meta elegida, con incentivo de US$100). El dato nuevo
más relevante no estaba en el resumen: las mejoras de conducta **se sostuvieron durante un
período de seguimiento posterior al fin de la intervención** — no es solo un efecto
Hawthorne mientras el conductor sabe que lo miden activamente. Matiz importante que acota la
tesis: lo validado aquí es un mecanismo de **feedback + microincentivo** ("UBI simulado"),
no necesariamente el pricing real de la prima — separa el mecanismo conductual que sí
sostiene el cambio de manejo (feedback y metas) del vehículo comercial (telemática con
precio dinámico real), que es el que carga el techo de confianza documentado en UK.
**[Nota 2026-08-03 — corrección de duplicado, no evidencia nueva]** El barrido de innovación
(`_nodes/tendencias-diseno-innovacion.md` §12.4) registró F-442 presentándolo como "la mejor
evidencia causal de todo el node" — pero es el **mismo estudio** que ya sostiene esta tesis:
mismo NCT06101251, mismo N=1,449, mismos cuatro brazos, mismos efectos. No es una segunda fuente
independiente, es el mismo RCT re-registrado desde una pista distinta (marketer/innovación en vez
de seeker/comportamiento). El único dato genuinamente nuevo que aporta esa segunda pasada: el
**conflicto de interés del financiador no se verificó** en ninguna de las dos lecturas — si pagó el
estudio una aseguradora o una plataforma de telemática con interés en el resultado, eso pesa antes
de citarlo en un caso de negocio interno. No sube la confianza de la tesis (sigue siendo la misma
evidencia), pero es la corrección de proceso correcta: contar F-442 como respaldo adicional habría
sido inflar artificialmente el número de fuentes independientes detrás de tesis 7.
- **Evidencia:** F-19 (🟢A, marco i-frame/s-frame), F-23 (🟢A, RCT de campo
  telemático, N=1,449, preregistrado — re-registrado también como F-442, mismo estudio),
  F-166/F-167 (🟠D, techo de adopción/confianza en UK)
- **Confianza:** Alta en que el producto funciona donde se adopta y en que el efecto persiste
  más allá de la ventana activa de monitoreo; Media en la velocidad de adopción masiva sin
  trabajar antes la confianza de entrada. El mecanismo validado es feedback+incentivo, no
  pricing dinámico real — no generalizar automáticamente de uno a otro. Pendiente: verificar
  conflicto de interés del financiador del RCT antes de usarlo como prueba neutral en un deck.
- **Actualizado:** 2026-08-03

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
**[Revisión profunda 2026-07-29]** Tres fuentes 🟢A releídas a fondo (antes solo el resumen
de una línea) matizan la oportunidad. F-36 (peer-reviewed, análisis secundario de la
Encuesta Nacional de Satisfacción de Usuarios en Salud 2016) encuentra que el factor de
riesgo más fuerte para automedicación no responsable en Perú, por lejos, no es ninguno de
los citados arriba — es que **el dispensador no pidió receta** (OR=29.06, muy por encima de
pedir consejo en la farmacia OR=1.88, comprar en <5 min OR=1.59, o ser hombre OR=1.32).
Implicación de diseño directa: el modelo de farmacia-frente-primario no solo formaliza una
conducta que ya existe — tiene que **corregir activamente** la práctica actual de dispensar
sin preguntar, que es la causa dominante documentada del daño, no un detalle menor de
proceso. F-40 y F-41 (ambos peer-reviewed, perspectiva-país) matizan además la
infraestructura de telesalud que sostiene la tesis: los volúmenes de teleconsulta en Perú
crecieron rápido durante la pandemia pero **luego cayeron**, lo que los propios autores leen
como señal de que se trató más de una medida de emergencia que de un cambio estructural en
la mezcla de provisión de salud — llaman a esto una "ventana de oportunidad de corto plazo"
para que el Estado consolide la inversión regulatoria, no un hábito ya adquirido de forma
permanente. No debilita la tracción estatal real (PL 08488, Plan Nacional de Telesalud), pero
sí el supuesto implícito de que la adopción de telesalud remota en Perú sigue una tendencia
que solo sube por sí sola.
- **Evidencia:** F-38 (🟠D, razones de automedicación), F-47 (🟠D, PL 08488),
  F-48 (🔵B, Plan Nacional de Telesalud MINSA), F-49 (🟠D, escala de InkaFarma/Mifarma),
  F-36 (🟢A, factor dominante OR=29 en automedicación no responsable), F-40/F-41 (🟢A,
  barreras y ventana de adopción de telesalud en Perú)
- **Confianza:** Alta en la oportunidad de mercado/distribución; el riesgo de ejecución
  técnica del triage IA es un problema aparte (ver tesis 10). Nuevo: Alta en que "corregir la
  dispensación sin receta" debe ser un objetivo de diseño explícito, no un efecto colateral
  esperado de formalizar el canal.
- **Actualizado:** 2026-07-29

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
**[Matiz 2026-07-29]** F-358 añade el detalle final del colapso de Babylon: el
detonante no fue que el consumidor rechazara el triaje IA — fue que **la
aseguradora pagadora (Centene, ~50% del revenue) decidió no renovar el
contrato** tras pérdidas de USD 212-274M en 2022 y terminó en quiebra Cap. 7,
vendiendo su operación UK por £500,000 (vs. USD 4.2B de valuación en el IPO
2021). Matiz de negocio, no solo de producto: validar precisión clínica
(silent trial) es necesario pero no suficiente — el caso de negocio también
tiene que sostenerse para el pagador que firma el contrato, no solo para el
paciente que lo usa. Un triage IA puede pasar el silent trial y aun así morir
si el pagador que lo financia no ve retorno a tiempo.
**[Revisión profunda 2026-07-29 — segunda lectura del día]** F-42 (validación real de
Omaolo, Finlandia, dispositivo médico marcado CE clase IIa) da el contraejemplo positivo
completo, con números que el resumen de una línea no traía: sobre 877 evaluaciones reales
en atención primaria, el symptom-checker fue **seguro en 97.6%** de los casos (856/877) pero
solo tuvo **coincidencia exacta con el triage de enfermería en 53.7%** (471/877). Lectura de
negocio directa: la métrica que evita repetir el error de Babylon no es "precisión
diagnóstica exacta" (que puede ser modesta, ~50-55%, y aun así ser un producto seguro y
comercialmente viable) — es la **tasa de sub-triage peligroso**, medida y reportada por
separado. Babylon nunca publicó esa separación; Omaolo sí, y por eso sobrevive como
dispositivo médico auditado mientras Babylon colapsó. Implicación directa para el gate de
aprobación del piloto farmacia+IA (RQ1/RQ2 en §3.0 del node de salud): fijar el criterio de
éxito en seguridad (falsos negativos graves), no en % de coincidencia exacta con el juicio
humano — son métricas distintas y la segunda puede ser mediocre sin que el producto sea malo.
- **Evidencia:** F-50 (🟢A/vía prensa especializada, caso Babylon), F-43 (🟢A,
  precisión real 45%), F-56/F-57 (🟢A, protocolo de silent trial), F-62 (🔵B,
  marco FDA SaMD), F-358 (🟡C, ángulo de negocio/pagador del colapso Babylon), F-42 (🟢A,
  Omaolo — safety 97.6% vs. exact-match 53.7%, separación explícita de métricas)
- **Confianza:** Alta
- **Actualizado:** 2026-07-29
**[Revisión profunda 2026-08-05]** Leí a fondo F-43, F-44 y la carta original de F-50 (antes
solo el resumen de una línea del ledger). Tres matices que afinan el mecanismo, no la
dirección de la tesis:
1. **F-50, el defecto exacto de Babylon:** la carta de Lancet (Fraser, Coiera & Wong 2018) no
   dice solo "sobreclamó" — dice que los datos de "precisión" de Babylon fueron ingresados por
   **médicos actuando como pacientes en viñetas simuladas**, no por usuarios legos reales. Es
   la misma falla que un piloto de triage propio repetiría si valida su precisión con personal
   clínico haciendo de paciente en vez de con usuarios reales tecleando síntomas reales — el
   gate de validación tiene que especificar explícitamente *quién* genera los casos de prueba,
   no solo cuántos.
2. **F-43, el patrón detrás del 45%:** la precisión del symptom-checker japonés no es un número
   plano — colapsa a 24.2% en enfermedades poco comunes y 14.5% en presentaciones atípicas, y
   no mejoró en 3 años de uso real (sin curva de aprendizaje). El triage automatizado falla
   sistemáticamente justo en los casos de mayor riesgo clínico (lo raro es lo que hay que
   atrapar), y el tiempo de despliegue por sí solo no lo corrige.
3. **F-44 da la razón de fondo para no vender "% de precisión" como KPI único:** el argumento
   de Milford (Bioethics 2024) es que la relación médico-paciente aporta percepción/observación
   clínica que un chatbot resta de la consulta incluso con precisión diagnóstica comparable a
   la de un humano — la capa de "atención humana" del modelo no es solo backup para errores de
   clasificación, cumple una función de outcome que la precisión, aunque fuera perfecta, no
   sustituye. Refuerza el mismo punto que F-42 (Omaolo) ya daba desde el ángulo de negocio:
   el KPI correcto es seguridad/outcome, no % de coincidencia con el juicio humano.
**[Revisión profunda 2026-08-12]** Leí a fondo F-55, F-56, F-57, F-58 y F-59 (antes solo el
resumen de una línea del ledger; URLs de nature.com/ncbi.nlm.nih.gov bloqueadas por el proxy del
entorno, reconstruido vía búsqueda dirigida). Estos cinco matizan la **rigurosidad del proceso de
testeo** que esta tesis exige, no solo la precisión del modelo:
1. **F-56 confirma que el "playbook" de silent trial no es tan maduro como sugiere citarlo como
   estándar:** el propio scoping review (891 artículos cribados, 2015-2025, solo 75 incluidos)
   encuentra que **no existen guías formales** todavía sobre cómo correr uno, con adopción
   concentrada en EE.UU./China/Reino Unido — sin precedente documentado en Perú/LatAm. El caso más
   agudo que cita: un modelo colapsó de AUC 0.90 a 0.50 en un silent trial posterior a su
   validación inicial, por *distribution shift* real (cambió edad, lateralidad de la condición,
   formato del equipo), no por error del modelo — "pasó el silent trial" no es una garantía
   permanente, es una fotografía vigente solo mientras la población no cambie (ver también
   heurística 10 de "Intuición acumulada", misma fuente, ángulo distinto).
2. **F-57 (Kwong et al. 2022 — autoría corregida en `codice.md`, no solo "PMC") acota el alcance
   real del caso que respalda los 60-90 días:** es un modelo de una sola condición (hidronefrosis
   obstructiva pediátrica), no un kit multi-síntoma — la duración recomendada no fue validada en
   un contexto tan amplio como el que este modelo propone.
3. **F-55 (autoría corregida: Cully, J.A. et al., no "Bauer, M.S." como tenía el ledger) resuelve
   qué tan bien funcionó en la práctica el diseño tipo 2 que tesis 9 cita como ejemplo de éxito:**
   el protocolo de 2012 no tiene resultados propios — los resultados reales se publicaron en Cully
   et al. 2017 (*J Gen Intern Med*, N=302, 50% de respuesta exitosa vs. 32.8% del control a los 4
   meses, sostenido a 8-12 meses). Pero la mejora es "modesta aunque persistente" según los propios
   autores, y el impacto en salud física se limitó a corto plazo y solo al subgrupo con EPOC, no al
   de insuficiencia cardíaca — **no asumir un resultado uniforme "funciona" en un kit
   multi-condición**; medir por subgrupo desde el diseño del piloto.
4. **F-58/F-59 abren una controversia metodológica activa sobre el stepped-wedge que la tesis
   nunca declaró:** Hemming & Taljaard (2020) afirman que el diseño escalonado está en **mayor**
   riesgo de sesgo que el cluster-RCT paralelo clásico (por eso CONSORT exige justificar la
   elección), y la ventaja ética que cita F-59 (Mdege et al. 2011) es objeto de una crítica formal
   directa — Kotz et al. (2012, mismo journal): "Use of the stepped wedge design cannot be
   recommended", con réplica académica activa de ambos lados. Implicación: si el piloto usa
   stepped-wedge para comparar el flujo IA vs. atención tradicional, hay que documentar por qué se
   prefirió sobre un diseño paralelo — no presentarlo como la opción obviamente superior.
- **Evidencia añadida:** F-55 (🟢A, Cully et al. 2012/2017), F-56/F-57 (🟢A, silent trial —
  autoría de F-57 corregida a Kwong et al.), F-58/F-59 (🟢A, stepped-wedge, con contraevidencia de
  Kotz et al. 2012)
- **Confianza:** Alta (sin cambio — el mecanismo central de la tesis se sostiene; lo nuevo es que
  cada estrategia de testeo del piloto tiene su propio costado de rigor/controversia que había que
  declarar, no solo citarla como "la literatura ya tiene el playbook")

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
**[Ampliación 2026-07-29]** El caso de mayor éxito comercial rastreado a fondo (Ethos,
EE.UU., revenue USD 388M FY2025, +52% YoY, margen EBITDA ajustado 23%, IPO NASDAQ
ene-2026) confirma el patrón, no lo contradice: es una agencia licenciada que
distribuye pólizas de aseguradoras terceras (no asume riesgo), y un agente humano
licenciado interviene específicamente cuando la entrevista de salud conversacional
produce respuestas ambiguas antes de alimentar el motor de suscripción — no es "cero
humano", es digital-first con humano como red de seguridad (F-364). Bowtie (Hong Kong,
primera licencia de "virtual insurer" de HK, ARR >USD 80M, +100% YoY) logra comisión
cero y cotización instantánea, pero lo hace enfocándose en producto **estandarizado**
(VHIS, esquema regulado) — es la simplificación del producto, no la eliminación
general del intermediario, lo que le permite prescindir de agente (F-370). Contraevidencia
buscada a propósito confirma el límite: Bestow (EE.UU.) vendió su propia aseguradora D2C
a Sammons Financial y pivotó a software B2B; Singlife (Singapur) terminó absorbida por
Sumitomo Life (aseguradora tradicional japonesa, USD 1.21B) en vez de escalar
independiente (F-366/F-367). El dato nuevo más transferible a Perú —LATAM, no Corea/China—
repite el patrón con más fuerza: Azos (Brasil, el insurtech de vida de mejor desempeño
verificable de la región, facturación duplicada dos años seguidos) opera con **más de
9,000 corredores/agentes socios**, no vende D2C (F-377); bancaseguros controla hasta 80%
de la distribución de vida en Brasil y el modelo "phygital" (agente + digital) duplica la
retención a primer año frente a canales puramente digitales o puramente físicos (F-375/F-376);
y Betterfly (Chile, unicornio regional de bienestar+seguro dinámico) cerró operaciones en
5 países en 2025 tras dos rondas de despidos —aunque es categoría de negocio distinta,
B2B2C, no venta directa de póliza (F-372/F-373). El ecosistema insurtech agregado de toda
LATAM (USD 199M en financiamiento 2025, +117% interanual) es una fracción de lo que mueve
una sola ronda de un insurtech grande de EE.UU./Brasil (F-374) — la escala del "digital
puro" en la región sigue siendo marginal frente al modelo híbrido. Cita directa que ancla
esto al proyecto interno: McKinsey documenta que los clientes de vida rankean al agente
como la fuente de mayor confianza para aprender sobre productos de seguros incluso cuando
la aseguradora no puede sacrificar el "human touch" en CX (F-359), y en Asia-Pacífico el
mix de canal de vida sigue dominado por agencia (~40%) y partnerships (~35%) pese a que
~80% de las ventas ya están habilitadas por tecnología digital — lo digital potencia al
agente, no lo reemplaza (F-360). Contraejemplo adicional dentro del propio ledger: la
trayectoria de loss ratio de Lemonade (166%→86%→~90%, 2017-2022) muestra que digitalizar
sin potenciar el juicio humano no resolvió la economía del seguro años después del IPO
(F-361, cifra sin fuente primaria confirmada — tratar como dirección, no dato exacto).
- **Evidencia:** F-180 (🟢A, marco causal), F-191 (🔵B, confianza+complejidad), F-192
  (⚠️ no verificado, tratar con cautela), F-181 a F-186, F-189, F-190 (🟡C/🟠D, datos de
  negocio convergentes de 3 mercados independientes), F-183 (🟡C, falla de reclamos
  digitales), F-187/F-188 (🟠D, señal social), F-359/F-360 (🔵B, McKinsey — human touch y
  mix de canal APAC), F-361 (🟠D, loss ratio Lemonade), F-362 a F-371 (🟡C/🟠D, casos Ethos/
  Bowtie/Bestow/Singlife/India — autorreportadas en su mayoría), F-372 a F-379 (🟡C/🔵B,
  LATAM: Azos, Betterfly, bancaseguros, ecosistema insurtech regional)
- **Confianza:** Alta en la dirección (el intermediario se redistribuye por complejidad,
  no desaparece) — reforzada, no debilitada, por la evidencia nueva más transferible
  geográficamente (LATAM). Media en la magnitud exacta de cualquier cifra puntual — casi
  toda la evidencia de negocio es C/D, ninguna supera B salvo los datos de McKinsey/CNseg/
  Fundación Mapfre (B). Ningún dato es específico de Perú; la transferencia se apoya en
  que el patrón (confianza sube con broker, bancaseguros domina, digital-first vía
  corredores gana sobre D2C puro) ya está documentado en tres mercados/regiones
  independientes (Corea/China, EE.UU./HK, LATAM).
- **Actualizado:** 2026-07-29

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

### 21. El "valor del diseño" que sostiene cualquier caso de negocio interno debe argumentarse por mecanismo, no por multiplicador — las cuatro cifras más citadas de la industria no resisten escrutinio de fuente primaria
Investigación 360° sobre tendencias de diseño (node nuevo `_nodes/tendencias-diseno-innovacion.md`) rastrea las
cuatro cifras de ROI de diseño más repetidas globalmente y las cuatro colapsan: "McKinsey +32%/+56%"
es un reporte de 2018 sin significancia estadística publicada, sin citas y sin análisis de sesgo de
muestreo, 8 años sin replicar; "$1 invertido en UX devuelve $100" termina en un reporte de Forrester
tras un muro de pago que casi nadie leyó, con indicios fuertes de que es un error de transcripción de
una regla de ingeniería de software (curva de costo de Boehm) que no mide ROI de UX en absoluto;
"47% más rápido con design systems" es N=8 desarrolladores de la propia agencia que vende design
systems, sin cegamiento; y "671% de ROI de design systems (Forrester)" **no tiene estudio primario
rastreable** — lo más cercano que existe es un TEI de 2019 comisionado y pagado por el vendor
(InVision, 475%). Del otro lado, la evidencia causal real y mejor sostenida (miles de A/B tests
aleatorizados en Microsoft/Bing/Google Ads/Netflix/Airbnb) dice algo mucho más modesto: **~2/3 de
los rediseños bien ejecutados no mueven la métrica objetivo**, y el valor real se acumula en mejoras
de 0,1-0,2%, no en saltos transformadores. **Aplicación directa:** el proyecto Back to Basics FFVV
Vida (tesis 18) tiene un deck al VP en preparación — cualquier cifra de "retorno del rediseño de la
experiencia de venta" que se use ahí debe construirse sobre mecanismo (menos pasos, menos error,
menos retrabajo, menos riesgo regulatorio — todo medible y auditable), nunca sobre un multiplicador
tipo "$1→$100", que es exactamente el tipo de cifra que no sobrevive a la primera pregunta de un CFO
o de Legal/Compliance en la sala.
- **Evidencia:** F-266 (🔴E de facto pese a origen McKinsey — sin significancia ni réplica), F-268
  (🔴E de facto, eco de cita), F-269 (🟡C, N=8), F-327 (🔴E, sin fuente primaria), F-328 (🟠D, TEI
  pagado por vendor), F-262 (🟢A, causal, A/B a escala — la mayoría de rediseños no mueve la métrica)
- **Confianza:** Alta — no es que el diseño no valga, es que las cifras espectaculares que circulan
  para justificarlo son, las cuatro, no auditables o directamente sin fuente.
**[Ampliación 2026-07-30]** Apareció una **quinta** cadena de eco del mismo patrón, específica de
design systems: el "135% de ROI" que circula en 2026 no es un estudio, es una calculadora de 2022
(Smashing Magazine) que modela US$646,000 invertidos → US$1,517,400 de ahorro *estimado* a 5 años,
alimentada por cifras autorreportadas de otras tres empresas — nadie ejecutó y midió el ahorro real
(F-397, mismo defecto estructural que Baymard/F-311 en la iteración 1). El propio Design Systems
Report 2026 (F-396, encuesta del proveedor zeroheight, no auditada) documenta que la satisfacción
con el respaldo interno ("buy-in") a design systems **cayó de 42% a 32%** interanual — el mercado
mismo empieza a desconfiar del retorno prometido, no solo los escépticos externos. El mismo principio
de "argumentar por mecanismo, no por multiplicador" aparece también fuera de diseño: un preprint
(F-388, sin revisión por pares) nombra el "**impuesto de verificación**" en desarrollo de software
asistido por IA — revisar código generado toma ~4.3 min para un senior vs. ~1.2 min para un junior,
y ese costo **escala con la madurez del código base** y puede comerse el ahorro de generación. Es la
misma lección que tesis 21 ya aplicaba a diseño, ahora con un caso paralelo en ingeniería: cualquier
cifra de "productividad con IA" para las propias herramientas internas del proyecto (`lapuerta`,
`cerrajero`, el agente conversacional) debe presupuestar ese costo de verificación, no solo el tiempo
de generación — instinto, no medido en este proyecto específico.
**[Corrección 2026-08-03]** La cifra que cité el 07-30 sobre el "impuesto de verificación" (~4.3
min/senior vs. ~1.2 min/junior, escalando con la madurez del código base) **no tiene fuente primaria
rastreable** — es la sexta cadena de eco de cita que encuentra el mismo node que ya había desmontado
las cuatro cifras de ROI de diseño (iteración 3, `_nodes/tendencias-diseno-innovacion.md` §11.2): el
rastreo llega a un artículo de DZone que cita "un estudio reciente de 250 desarrolladores" sin nombrar
autor, institución ni enlace, y el preprint que yo mismo cité como respaldo (F-388) resulta ser de
autor único y de naturaleza sintética — un marco teórico que cita cifras de terceros, no un
experimento propio. **Retiro esa cifra específica** de cualquier caso de negocio interno sobre
productividad con IA (`lapuerta`, `cerrajero`, agente conversacional). Lo que sí sobrevive con
telemetría real e independiente (F-406, N grande): la IA sí desplaza esfuerzo de generación hacia
revisión (+98% de PRs, +91% de tiempo de revisión). Y lo que se invierte respecto a lo que yo mismo
asumí en julio: un estudio real (F-407, 400 revisores, 11,429 revisiones) muestra que **más
experiencia/exposición acumulada produce MENOS escrutinio, no más** — el riesgo no está en el junior
que revisa con cuidado por inseguridad, está en el senior que ya se acostumbró a confiar en la salida
de la IA. Corrijo mi propia lectura de julio: cualquier control de calidad sobre trabajo asistido por
IA en el proyecto debería vigilar más de cerca al revisor experimentado y complaciente, no al novato
cauteloso. Esto refuerza, con un dato adicional propio, el patrón central de esta tesis: la iteración 3
confirma que las cinco cifras de ROI de diseño ya desmontadas siguen circulando sin que nadie las
retire — "no rota, acumula". El mercado no se autocorrige; el filtro tiene que ser interno, cada vez
que una cifra bonita entra al ledger.
- **Actualizado:** 2026-08-03

### 22. La personalización con IA puede reducir la conversión en vez de aumentarla cuando el dato es sensible — riesgo directo para telemática/UBI y para cualquier asesor conversacional de Rimac
La misma investigación 360° encuentra evidencia de campo (no solo laboratorio) de que el consejo
personalizado con IA puede **reducir** la compra por intrusividad percibida, y que bajo saliencia de
privacidad la personalización con datos personales no supera al mensaje genérico. El mecanismo
específico que sí calibra bien la confianza en sistemas de IA no es "explicar más" (meta-análisis de
90 estudios: la explicabilidad tiene correlación con confianza significativa pero moderada, no es el
factor dominante) — es hacer la salida **verificable**, meter fricción deliberada solo donde la tarea
es difícil, y no ponerla donde es fácil. Esto conecta directo con dos tesis ya vigentes: tesis 7 (UBI
tiene techo de confianza documentado incluso en mercados maduros) y tesis 13 (divulgación progresiva
de datos convierte mejor, con riesgo ético explícito si se abusa) — y refina un riesgo ya anotado
sobre el agente conversacional de Rimac: el riesgo no es solo que alucine coberturas, es que
"agregar explicabilidad" al agente puede generar sobre-confianza del cliente sin mejorar de verdad su
decisión, si no está diseñada para ser verificable.
- **Evidencia:** F-253, F-254 (🟢A, personalización con IA reduce conversión bajo saliencia de
  privacidad), F-242 (🟢A, meta-análisis PRISMA 90 estudios, explicabilidad → confianza moderada, no
  dominante), F-244 (🟢A, explicaciones sin verificabilidad producen sobre-confianza), F-246 (🟢A,
  explicaciones sí ayudan, pero solo en tareas difíciles)
- **Confianza:** Alta en el mecanismo (personalización + dato sensible + baja verificabilidad =
  riesgo de conversión, no ventaja); la extrapolación exacta a un producto de telemática/UBI peruano
  específico es instinto razonado, no medido en Perú.
- **Actualizado:** 2026-07-27

### 23. El steering hacia un canal de atención más barato (triaje remoto/telesalud) sí ahorra costo real — pero es el mecanismo con la reactancia documentada más fuerte del sector cuando se percibe como interés del pagador, no del paciente
Evidencia convergente —mayormente RCT y cuasi-experimentos de sistemas públicos (VA,
NHS, Países Bajos), transferida a aseguradora comercial— confirma que dirigir al
paciente hacia el canal correcto de menor costo (enfermera de triaje antes que
emergencias) sí reduce gasto real: -USD 404/28 días vs. ED en la VA, caída de 38%→36%
en derivación a ED tras acceso on-demand (>1M llamadas), 9.5% de desvío seguro en un
cluster RCT neerlandés (solo 2.4% de lo desviado terminó hospitalizado). El único caso
encontrado en una aseguradora comercial real (Medical Mutual) llega a ~90% de tasa de
evitación de ED con el tiempo — pero es la fuente de menor rigor de todo el cluster (D).
Lo que este ledger nunca había cuantificado así es el riesgo espejo: cuando el steering
se percibe como conflicto de interés del pagador (ahorra dinero de la aseguradora, no
necesariamente del paciente), la reactancia escala de queja a evento político-mediático
en días, no meses. Anthem revirtió en 5 días una política de límite de tiempo de
anestesia bajo presión de senadores de EE.UU. (dic. 2024) y ya había hecho lo mismo en
2019 con su política de "ER evitable"; Cigna/EviCore enfrenta litigio y regulación
estatal activa por denegaciones algorítmicas (300,000 reclamos en 2 meses, 90%
revertidas en apelación — paralelo directo al riesgo INDECOPI de tesis 8); y el
asesinato del CEO de UnitedHealthcare generó 62,000 reacciones en un post de
condolencias, 57,000 de risa — la validación social más fuerte encontrada en todo el
ledger de que el público no perdona el steering que se lee como ahorro del pagador
disfrazado de cuidado del paciente. Conecta directo con tesis 9/10: el vacío que
"farmacia+triage IA" debe cerrar no es solo precisión clínica (tesis 10) — es que el
mensaje al paciente tiene que leerse siempre como "te dirijo a lo mejor para ti", nunca
como "te dirijo a lo más barato para nosotros", aunque las dos cosas coincidan en la
práctica. Matiz adicional que corrige un supuesto de trabajo: F-357 (RCT real, JAMA
Network Open, N=424, U. of Pennsylvania) refuta que el framing opt-out sea una táctica
de adopción probada — no superó al opt-in en tasa de enrolamiento de monitoreo remoto.
Cualquier plan de "inscribir por default y dejar salir" para telesalud/triaje/UBI no
tiene evidencia de que funcione mejor que pedir consentimiento activo, y si se percibe
como empuje no consentido hereda el riesgo regulatorio ya documentado en tesis 8.
- **Evidencia:** F-329 a F-336, F-338 a F-341 (🟢A en su mayoría, transferidas de
  sistemas públicos), F-332 (🟠D, único caso de aseguradora comercial real), F-342 a
  F-350 (🟠D/🟡C/🔵B, contraevidencia adversarial y casos de reactancia/backlash), F-344
  a F-346 (🟡C/🔵B, reacción social), F-349 (🟢A, investigación ProPublica sobre EviCore),
  F-357 (🟢A, refutación de opt-out>opt-in)
- **Confianza:** Alta en que el mecanismo de ahorro funciona (evidencia A convergente,
  aunque transferida de sistemas públicos, no de aseguradora comercial); Alta en que la
  reactancia por conflicto de interés percibido —no la tecnología— es el riesgo
  dominante; Media en la magnitud exacta transferible a una aseguradora comercial
  peruana, porque el único dato de aseguradora comercial real disponible es de rigor D.
- **Actualizado:** 2026-07-29

### 24. La interfaz generada dinámicamente por IA ("generative UI") ya tiene evidencia real — y es un empate técnico, no la ventaja que promete el marketing: sube la preferencia declarada, baja específicamente la usabilidad de soporte
Barrido de la iteración 2 del node de tendencias de diseño trae el primer cluster de evidencia
empírica sustancial sobre interfaces que un modelo de IA genera on-the-fly (no una pantalla fija
diseñada por humanos). El propio paper insignia del optimismo (Google, F-380) reconoce que sus
salidas son **peores que las hechas por expertos humanos** y solo "comparables" el 50% de las
veces — no es una fuente neutral escondiendo el dato, lo reconoce en el propio abstract. La mejor
evidencia peer-reviewed a favor (F-381, Findings of ACL) sí encuentra preferencia real de hasta
72% en tareas exploratorias densas en información — pero sigue siendo **preferencia declarada**,
no desempeño de tarea ni aprendibilidad. Y donde sí se midió con método (F-382, CHI, 138 pantallas
móviles reales generadas por tres herramientas comerciales contra las heurísticas de Nielsen), la
falla no es estética — es específicamente en **soporte**: ayuda/documentación, recuperación de
errores, prevención de errores, eficiencia de uso. Un estudio separado (F-384) mide la causa
estructural: el mismo prompt produce interfaces distintas entre herramientas **y entre ejecuciones
repetidas de la misma herramienta** — la inconsistencia no es un problema de madurez del modelo, es
una propiedad del paradigma, tal como ya lo advertía la comunidad de HCI en un position paper
publicado (F-383: consistencia y predictibilidad son valores centrales de la disciplina, rotos por
construcción). Traducción de negocio: si Rimac evalúa alguna vez una interfaz que la IA genera de
forma dinámica (para el agente conversacional, un configurador de producto, un simulador), la
pregunta correcta no es "¿gusta más?" —probablemente sí, en el primer contacto— sino "¿sigue siendo
consistente y confiable la quinta vez que el mismo cliente vuelve, y qué pasa cuando necesita ayuda
o comete un error?" — que es justo donde la evidencia dice que falla hoy.
- **Evidencia:** F-380 (🟡C, Google, preferencia declarada, admite calidad inferior a humano), F-381
  (🟢A, ACL peer-reviewed, preferencia hasta 72%, no desempeño), F-382 (🔵B, CHI, 138 pantallas
  reales, falla en heurísticas de soporte), F-383 (🔵B, position paper HCI contra el paradigma),
  F-384 (🔵B, revisión sistemática, inconsistencia entre y dentro de herramientas), F-385/F-386
  (🟡C/🔵B, deuda técnica oculta y reencuadre del objeto de usabilidad)
- **Confianza:** Alta en que la evidencia hoy no sostiene "generative UI = mejor experiencia" sin
  matiz — es preferencia real en el primer contacto, con falla medida específicamente en soporte y
  consistencia. Media-baja en la transferencia directa a un producto de seguros peruano — ninguna
  fuente es de Perú ni de seguros; la lectura de riesgo para Rimac es instinto razonado, no medido.
- **Actualizado:** 2026-07-30

### 25. La rentabilidad del insurtech no depende del canal digital ni de la IA — depende de disciplina de suscripción, y hoy hay evidencia auditada de ambos signos dentro del mismo subsector
La iteración 4 del node de tendencias (ampliado a "diseño e innovación") abrió un ángulo de negocio
directo de seguros que no tenía precedente en este ledger: dos insurtechs de auto 100% digital,
mismo modelo declarado, misma clase de evidencia (filing SEC/carta a accionistas), y resultados
opuestos. **Root Inc.** cerró con combined ratio de **91.4%** (rentable en suscripción, <100%),
net income positivo el trimestre y un giro de −US$101.3M (2023) a +US$78.5M operativo. **Lemonade**
sigue en **~139%** de combined ratio — todavía con pérdida técnica de suscripción, aunque su gross
loss ratio mejoró 16pp interanual y guía EBITDA ajustado positivo recién para Q4 2026. Es el mismo
subsector, la misma promesa de "seguro nativo digital" — y una diferencia de casi 50 puntos de
combined ratio entre ambas. El propio node marca esto como hipótesis abierta (H29), no resuelta: la
variable que separa a Root de Lemonade **todavía no está aislada** — la lectura razonable, no
probada, es que no es la capa tecnológica sino la disciplina de suscripción y selección de riesgo,
exactamente el tipo de ejecución que un insurtech puro no puede comprarse con capital de venture. Un
descuento honesto que el propio node señala: ninguna de las dos cifras controla por mix de producto
ni antigüedad de cohorte — no se puede todavía separar "mejor suscripción" de "cartera más madura".
- **Evidencia:** F-449 (🟢A/filing SEC, Root Inc. 10-Q/10-K), F-450 (🟡C/agregador sobre datos SEC +
  carta a accionistas, Lemonade)
- **Confianza:** Alta en que la divergencia es real y auditada (ambas fuentes se apoyan en datos de
  filing, no en autorreporte de marketing); Media-baja en la causa — el propio node deja la pregunta
  abierta (H29) y advierte que ninguna cifra controla por mix de producto o antigüedad de cartera. Leer
  "digital = rentable" o "digital = insostenible" en cualquiera de las dos direcciones sería forzar una
  lectura que la evidencia todavía no sostiene.
- **Actualizado:** 2026-08-03

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
  respaldo A/B convergente en cuatro mercados/regiones de alta digitalización (Corea,
  China, EE.UU./HK vía Ethos/Bowtie, y ahora LATAM vía Azos/bancaseguros) de que el
  intermediario no desaparece en productos complejos — se redistribuye hacia ellos, y
  el dato LATAM (Azos con 9,000+ corredores, bancaseguros con hasta 80% de la
  distribución de vida en Brasil) es el más transferible a Perú de todos los
  encontrados hasta ahora. El riesgo regulatorio de tesis 8 sigue vigente: cualquier
  variante de contacto saliente no consentido es una apuesta con S/2M+ de multa
  potencial y precedente directo contra un competidor. La jugada válida es bróker como
  canal de confianza que el cliente busca (referidos, punto de venta), no como fuerza
  de prospección saliente.
- **Diseñar cualquier mensaje de steering hacia canal de atención más barato (farmacia
  como frente primario, triaje remoto, telesalud) explícitamente como beneficio del
  paciente, nunca como ahorro del pagador — y pedir consentimiento activo (opt-in), no
  apoyarse en opt-out.** Tesis 23: el mecanismo de ahorro funciona, pero el mismo
  mecanismo dispara la reactancia más fuerte documentada del sector si se percibe como
  interés de la aseguradora. Esto no es un matiz de comunicación menor — es la
  diferencia entre replicar el ahorro real de Medical Mutual (~90% de evitación de ED)
  o el backlash político-mediático de Anthem/Cigna/UnitedHealthcare.
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
- **Argumentar el caso de negocio del rediseño de experiencia de venta (Back to
  Basics FFVV Vida) por mecanismo, no por multiplicador.** Tesis 21: el deck al
  VP gana credibilidad citando fricción/error/retrabajo/riesgo regulatorio
  reducidos —medible y auditable— en vez de una cifra tipo "$1→$100" que un CFO
  o Legal puede tumbar con una pregunta.
- **Diseñar cualquier capa de explicabilidad del agente conversacional o del
  asesor de IA de Rimac para ser verificable, no solo explicativa.** Tesis 22:
  la fricción deliberada en decisiones difíciles calibra mejor la confianza del
  cliente que "explicar más"; en decisiones fáciles, agregar explicación no
  suma y puede generar sobre-confianza.
- **Exigir combined ratio o loss ratio auditado antes de leer cualquier apuesta de
  innovación/insurtech como éxito.** Tesis 25: Root y Lemonade muestran que el mismo modelo
  digital produce resultados opuestos — "es digital" o "levantó capital" no dice nada sobre
  rentabilidad real. Aplica también puertas adentro: los labs corporativos peruanos activos hoy
  (BCP CIX, Pacífico "La Cápsula") no tienen ningún dato público de retorno auditado, y BCP nunca
  verificó públicamente si cumplió su propia meta 2022 de 10% de ingresos nuevos vía innovación
  para 2025 — el estándar de evidencia que exige tesis 21 para "ROI de diseño" debe aplicarse
  igual de estricto a cualquier cifra de "ROI de innovación" que circule internamente.

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
  **Matiz de negocio (F-358):** el detonante final de Babylon fue que su
  pagador (Centene) no renovó el contrato tras pérdidas de USD 212-274M —
  pasar el silent trial clínico no basta si el caso de negocio no convence a
  quien firma el contrato.
- **Diseñar o comunicar cualquier programa de steering/derivación hacia un canal más
  barato (farmacia, triaje remoto, telesalud) sin blindar el mensaje como beneficio
  del paciente.** Tesis 23: el precedente de Anthem (revertido en 5 días bajo presión
  de senadores de EE.UU.), Cigna/EviCore (litigio y regulación estatal activa por
  denegaciones algorítmicas) y la reacción social al caso UnitedHealthcare muestran que
  la reactancia por conflicto de interés percibido escala de queja a evento
  político-mediático nacional en cuestión de días, no meses.
- **Apoyar cualquier flujo de consentimiento de telesalud/triaje/UBI en framing
  opt-out ("inscribe por default, deja salir al que no quiera") asumiendo que
  convierte mejor.** Tesis 23: un RCT real (F-357, N=424) refuta directamente esa
  suposición — opt-out no superó a opt-in en tasa de enrolamiento. Sin evidencia de
  que funcione mejor, y con riesgo de leerse como empuje no consentido (tesis 8), la
  jugada por defecto debería ser opt-in explícito.
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
  satisfacción y seguir inventando datos de producto. **Matiz añadido (tesis
  22, 2026-07-27):** agregar "capas de explicabilidad" al agente sin diseñarlas
  para ser verificables no resuelve esto — puede empeorarlo, generando
  sobre-confianza del cliente en una respuesta que suena bien y no lo es.
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
- **Usar cualquiera de las cuatro cifras de ROI de diseño más citadas globalmente (McKinsey
  +32%/+56%, "$1 UX→$100", "47% más rápido con design systems", "671% ROI de Forrester") en un
  deck o caso de negocio interno.** Tesis 21: las cuatro colapsan al rastrear la fuente primaria —
  una no tiene estudio rastreable, otra depende de un reporte tras muro de pago que nadie leyó,
  otra es N=8 de la propia agencia que vende el producto. Es vulnerable en cualquier sala con un
  CFO o Legal/Compliance presente. **Mismo cuidado aplica del lado de innovación:** el barrido de
  agosto encontró un caso peor que el eco de cita — cifras del tipo "80-95% de nuevos productos
  fracasan" que no tienen **ninguna** fuente primaria localizable (huérfano de cita, F-444). Ni
  diseño ni innovación tienen las cifras espectaculares que su propio marketing repite.
- **Citar el "impuesto de verificación" (~4.3 min/senior vs. ~1.2 min/junior en revisión de código
  con IA) como dato medido.** Corrección propia (tesis 21, nota 2026-08-03): esa cifra específica
  no tiene fuente primaria — la retiré. Lo que sí hay evidencia real: el revisor con más experiencia
  acumulada escrutina **menos**, no más, un hallazgo que invierte lo que yo mismo asumí en julio.
- **Tratar "agregar explicabilidad" a un asistente o agente de IA como solución genérica de
  confianza.** Tesis 22: la explicabilidad tiene correlación moderada, no dominante, con la
  confianza — y sin verificabilidad puede producir sobre-confianza en vez de calibrarla,
  especialmente si se despliega parejo en decisiones fáciles y difíciles por igual.
- **Tratar "agregar explicabilidad" a un asistente o agente de IA como solución genérica de
  confianza.** Tesis 22: la explicabilidad tiene correlación moderada, no dominante, con la
  confianza — y sin verificabilidad puede producir sobre-confianza en vez de calibrarla,
  especialmente si se despliega parejo en decisiones fáciles y difíciles por igual.
- **Sobreinvertir en personalización con IA (ofertas, pricing, mensajes) en momentos donde el
  cliente está atento a la privacidad de su dato.** Tesis 22: hay evidencia de campo de que el
  consejo personalizado con IA puede reducir la compra por intrusividad percibida — el mismo
  riesgo que ya señalaba tesis 7 sobre el techo de confianza de la telemática/UBI, ahora con un
  mecanismo específico (saliencia de privacidad) que lo explica.
- **Adoptar una interfaz que la IA genera dinámicamente (agente conversacional, configurador,
  simulador) evaluándola solo por qué tan bien gusta en el primer contacto.** Tesis 24: la
  evidencia real mide preferencia declarada alta pero falla medida específicamente en soporte
  (ayuda, recuperación de errores) y en consistencia entre sesiones — justo las dos cosas que
  más importan quejas de reclamo o de error de cobertura, el mismo terreno que ya cubre el
  riesgo de "medir el agente conversacional con la métrica equivocada" más arriba.
- **Tratar el "shadow AI" (uso de IA por cuenta personal, sin lineamiento corporativo) como un
  tema de productividad interna y no de gobierno de dato.** El dato más reciente de la región
  (Brasil, F-389) encuentra 94% de adopción de IA en equipos de diseño pero solo 14% con
  capacitación de la empresa y 60% operando con cuentas personales sin lineamiento corporativo.
  Para cualquier equipo de una aseguradora —diseño, atención al cliente, actuarial— que maneje
  dato de cliente, esto es superficie de fuga de información regulada por la LPDP (mismo marco
  normativo que ya preocupa en tesis 13), no solo un tema de adopción de herramientas.
- **Asumir que "reemplazar con IA" en funciones internas (diseño, contenido, soporte) es todavía
  una apuesta especulativa de Silicon Valley, no una decisión ya tomada en la región.**
  MercadoLibre —la empresa latinoamericana más valiosa en bolsa— desvinculó 119 personas de UX en
  LatAm en 2026 integrando explícitamente los roles de diseño y contenido apoyándose en IA
  (F-391). Es una decisión corporativa documentada, no una anécdota de LinkedIn: si Rimac evalúa
  algún día consolidar roles internos (contenido, soporte, diseño) apoyándose en IA, el
  precedente geográfico más cercano ya existe y es de reducción de headcount, no de mejora de
  producto — instinto de negocio, no una recomendación, solo el dato de que la conversación ya
  dejó de ser hipotética en la región.

## 🧠 Intuición acumulada

> Distinto de las tesis de arriba: una tesis es una apuesta de negocio con evidencia y confianza
> puntual (F-n → oportunidad/riesgo concreto). Esto es otra cosa — heurísticas de juicio y de toma
> de decisión que se acumulan de leer fuentes a fondo, transferibles a cualquier evaluación futura,
> conectadas o no a una tesis ya vigente. Alimentada por la rutina diaria de lectura profunda (3
> fuentes/día, orden por rigurosidad, registro en `research/lobo/fuentes_leidas_lobo.md` — regla en
> `CLAUDE.md`). Empezada 2026-08-06.

### 1. Antes de lanzar cualquier producto de seguro nuevo, correr primero el test de selección adversa — no solo el de demanda
Rothschild & Stiglitz (1976) prueban algo más fuerte que "la selección adversa sube el costo": si
los tipos de riesgo no se pueden separar y la distorsión de la auto-selección es demasiado grande,
**puede no existir ningún equilibrio competitivo** — el mercado entero se desarma, no solo se
encarece. Cuando sí existe equilibrio, nunca es un contrato único para todos (pooling): es
siempre un par de contratos donde el riesgo bajo acepta cobertura **incompleta** a cambio de un
precio más bajo, como señal costosa que lo distingue del riesgo alto. **Heurística de decisión:**
frente a cualquier producto nuevo (paramétrico sísmico, microseguro, UBI, cualquier variante de
`lapuerta`), la primera pregunta no es "¿hay demanda insatisfecha?" sino "¿esta estructura de
precio/elegibilidad separa los riesgos, o solo va a atraer al riesgo alto y ahuyentar al bajo?" —
si la respuesta no es clara, el diseño del producto (no el canal, no el mensaje) es el riesgo
central del lanzamiento, antes que cualquier otra variable.
- **Fuente:** F-82 (🟢A, Rothschild & Stiglitz 1976, *Quarterly Journal of Economics* — paper
  fundacional de la economía de la información, ya citado en el ledger para explicar por qué
  ciertos seguros estructuran su cobertura como lo hacen)
- **Leído a fondo:** 2026-08-06 (URL directa del NBER bloqueada con 403 por el proxy del entorno,
  igual que otras fuentes académicas — reconstruido vía múltiples búsquedas dirigidas que
  confirman el resultado central y el mecanismo de separación, no solo el resumen ya citado)

### 2. "Bueno en teoría para quien participa" y "bueno para el sistema/población" son dos preguntas distintas — evaluar ambas, no asumir que la primera implica la segunda
El paper de Direct Primary Care (JABFM 2018) encuentra que el modelo es teóricamente sólido para
mejorar first-contact y longitudinalidad **a nivel de la consulta, para el paciente que ya está
adentro** — pero señala una brecha de evidencia estructural: a nivel de sistema de salud, el
mecanismo de acceso (cuota de membresía) excluye por diseño a los pacientes más vulnerables y
complejos, exactamente los que más se beneficiarían. Nadie ha medido comparativamente a los
excluidos contra los incluidos. **Heurística de decisión:** cualquier modelo de atención
value-based o de frente primario que el Lobo evalúe (farmacia-frente-primario, capitación,
telesalud) debe pasar por dos preguntas separadas, no una: (1) ¿funciona para quien logra
participar? y (2) ¿quién queda afuera por el mecanismo de acceso mismo, y es justo el segmento de
mayor necesidad? Una respuesta positiva a la primera no dice nada sobre la segunda — y el "buen
modelo en teoría" que tiene un filtro de acceso que expulsa al riesgo/necesidad más alta puede ser
simultáneamente exitoso a nivel clínico y regresivo a nivel de sistema.
- **Fuente:** F-107 (🟢A, JABFM 2018, *Direct Primary Care: Applying Theory to Potential Changes
  in Delivery and Outcomes*)
- **Leído a fondo:** 2026-08-06 (mismo bloqueo de URL directa, reconstruido vía búsqueda dirigida
  con el hallazgo textual del propio abstract/resumen del paper)
- **Conexión razonada, no forzada:** aplica directo a tesis 9 (farmacia-frente-primario en Perú) —
  no cambia su confianza (Alta se mantiene, es un ángulo nuevo, no evidencia que la contradiga),
  pero agrega una pregunta de diseño que esa tesis todavía no tenía explícita: ¿el canal de
  farmacia+triage excluye por costo/fricción a alguien, y es el mismo segmento de mayor riesgo que
  ya identifica tesis 9 (OR=29 por dispensación sin receta)?

### 3. En seguros de alto involucramiento (vida, salud, hogar), la unidad real de decisión suele ser el hogar, no el individuo que está frente al asesor
Davis (1976), revisión canónica de decisión de compra en el hogar, documenta que gran parte de la
literatura de marketing sobrestima los modelos de decisión individual y subestima que la compra se
negocia entre cónyuges/familia, con roles que cambian según la etapa de la decisión (quién inicia,
quién busca información, quién decide, quién paga) — no es un rol fijo ni simétrico. **Heurística
de decisión:** cuando el Lobo evalúa un embudo de venta, un guion de manejo de objeciones o
cualquier métrica de conversión en categorías de alto involucramiento (vida individual, salud,
hogar — no tanto SOAT o microseguro de ticket bajo), el modelo mental correcto del "cliente" no es
una persona sola tomando una decisión racional en el punto de venta, es un proceso de decisión de
hogar del que el asesor solo ve una fracción. Una objeción como "lo voy a consultar" no es
necesariamente evasión ni fricción a resolver con más información — puede ser el proceso de
decisión real funcionando como debe. Medir "tasa de cierre en la primera cita" sin dar espacio a
ese proceso puede estar optimizando contra la forma real en que la categoría se decide, no a favor.
- **Fuente:** F-236 (🟢A, Davis, H.L. 1976, *Decision Making Within the Household*, Journal of
  Consumer Research — ya en el ledger, reemplazó a Darley & Latané como fuente de C.6 del Bloque 4
  del Playbook, tesis 18)
- **Leído a fondo:** 2026-08-06 (mismo patrón de bloqueo de URL directa; contenido reconstruido vía
  búsqueda dirigida con las tres preguntas centrales del paper y sus problemas metodológicos
  identificados)
- **Conexión razonada, no forzada:** refuerza desde un ángulo distinto el matiz que tesis 18 ya
  hizo sobre C.6 (objeción "lo consulto con mi pareja" ≠ emergencia con testigos de Darley &
  Latané, es decisión de hogar) — esta lectura profunda confirma que el marco correcto para esa
  objeción tiene 50 años de literatura propia, no es una intuición nueva del Lobo.

### 4. La incomprensión no solo empuja a elegir peor entre opciones pagadas — puede anular por completo el uso de un beneficio que ya es gratuito
La segunda encuesta de F-6 (la misma fuente que ya sostiene tesis 2, ahora leída a fondo más allá
del hallazgo de coaseguro que cita el resumen breve) encuentra algo más específico y más barato de
corregir que "el consumidor no entiende su plan": los asegurados bajo planes con deducible, al
malinterpretar la estructura, **reducen su uso de atención preventiva que ya está cubierta sin
costo de bolsillo bajo el ACA** — no es que la atención preventiva sea cara y la eviten por precio,
es que creen que les van a cobrar y la evitan por error puro. **Heurística de decisión:** cuando un
producto/póliza incluye una prestación gratuita condicionada a una estructura compleja (deducible,
copago, coaseguro), no basta con que esté "técnicamente" cubierta en el contrato — hay que verificar
activamente que el asegurado *sepa* que es gratis, porque el default conductual documentado es
asumir que cuesta y evitarla. A diferencia de tesis 1 (donde "explicar mejor" no cambia conducta de
compra), aquí el objetivo no es vender más — es no perder utilización de algo ya pagado por la
aseguradora, que es una pérdida silenciosa de valor para el cliente y una oportunidad perdida de
mostrar valor del producto. Aplicable directo a cualquier chequeo anual, telemedicina o beneficio
incluido sin costo adicional en un plan de salud.
- **Fuente:** F-6 (🟢A, Loewenstein et al. 2013 — ya citada en tesis 2; este es el hallazgo de la
  segunda encuesta del propio estudio, no cubierto por el resumen de una línea que ya tenía el
  ledger)
- **Leído a fondo:** 2026-08-07 (mismo bloqueo de URL directa vía proxy del entorno para
  sciencedirect.com; reconstruido vía búsqueda dirigida que confirma el mecanismo específico —
  subutilización de preventiva gratuita por malentendido, no por costo real)
- **Conexión razonada, no forzada:** matiza tesis 2 sin cambiar su confianza (sigue Alta) — el
  costo de la incomprensión del coaseguro no es solo "elegir peor", es también "no usar lo que ya
  se pagó", un ángulo que tesis 2 no tenía explícito.

### 5. Antes de aplicar cualquier framework con nombre propio a un proyecto propio, buscar su literatura de "malentendidos/clarificaciones" — casi siempre existe, y documenta fallas ya observadas, no hipotéticas
F-53 (Holtrop et al. 2021), ya usado para estructurar las preguntas de investigación del piloto
farmacia+triage IA (tesis 9), es en sí mismo un caso de estudio de esta heurística: es un paper
publicado 22 años después del RE-AIM original (1999) específicamente para corregir 13 malentendidos
documentados sobre cómo los propios equipos de salud pública lo aplicaban mal en la práctica —
tratar las cinco dimensiones como checklist secuencial obligatorio en vez de guía pragmática, medir
"Maintenance" solo a nivel del paciente individual sin la capa de institucionalización a nivel de la
organización, entre otros. El framework evolucionó a PRISM precisamente porque RE-AIM 1999 no cubría
contexto organizacional/de infraestructura. **Heurística de decisión:** un framework con ~20+ años de
uso real genera su propio corpus de "cómo la gente lo usa mal" — y ese corpus documenta con precisión
los atajos que cualquier equipo nuevo (incluido el propio proyecto aplicando RE-AIM al piloto de
tesis 9) va a tomar por defecto. Antes de aplicar cualquier framework con nombre propio (RE-AIM, pero
el mismo principio aplica a Jobs-to-be-Done, OKRs, Design Thinking, Stage-Gate — este último ya
señalado como vulnerable en tesis 21) al propio trabajo, vale la pena buscar activamente su
literatura de clarificaciones — no solo el paper fundacional — porque ahí está el mapa de errores ya
cometidos por otros, no una lista hipotética.
- **Fuente:** F-53 (🟢A, Holtrop et al. 2021 — ya releído a fondo por la revisión profunda de
  `cronista` el 2026-08-05 desde el ángulo de salud/RE-AIM específico; esta lectura del Lobo es
  independiente y extrae el ángulo de heurística general de framework, no el matiz de contenido de
  salud que ya capturó esa revisión)
- **Leído a fondo:** 2026-08-07 (mismo bloqueo de proxy para pmc.ncbi.nlm.nih.gov; contenido
  reconstruido vía búsqueda dirigida, consistente con el detalle ya registrado en el ledger)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 9 ni de tesis 21 — es una
  heurística de proceso propio (cómo evaluar frameworks antes de adoptarlos), no evidencia nueva
  sobre seguros/salud/Perú.

### 6. Antes de poner un incentivo económico contingente sobre una conducta, preguntar si esa conducta ya tiene motivación intrínseca en parte del segmento — el mismo incentivo que activa al desmotivado puede debilitar al que ya lo hacía por convicción propia
La lectura completa de F-230 (ya citada en tesis 19 solo por el marco general de necesidades
psicológicas) trae el hallazgo más operativo de la teoría de la autodeterminación que el resumen no
capturaba: el **efecto de socavamiento** (*undermining effect*, meta-análisis de Deci, Koestner &
Ryan 1999 sobre 128 experimentos controlados) — las recompensas económicas contingentes a una tarea
**reducen la motivación intrínseca** cuando esa tarea ya era genuinamente interesante o valorada por
la persona, y la motivación "autónoma" (identificada/intrínseca) predice mejores resultados
sostenidos que la motivación "controlada" (por recompensa o presión externa). **Heurística de
decisión:** esto conecta directo con tesis 7 (UBI con microincentivo de US$100 sobre conducción
segura) y con el hallazgo de defaults de tesis 6 (Milkman, microincentivo en el momento de recaída):
la evidencia de que el incentivo contingente funciona es real y de campo, pero la propia teoría de la
que se deriva advierte que el mismo pago puede erosionar la motivación de quien ya manejaba con
cuidado por razones propias (proteger a su familia, evitar el riesgo) — si el incentivo se retira
después, ese segundo segmento puede terminar con peor conducta que si nunca se le hubiera ofrecido
pago. No es razón para descartar los incentivos (tesis 7 ya los valida con RCT real) — es razón para
segmentar el diseño: el microincentivo probablemente rinde más en el cliente de baja motivación de
base, mientras que en el que ya es buen riesgo por convicción propia, reconocimiento/feedback sin
pago (que es justo lo que separa el brazo "meta elegida" del brazo "incentivo" en el propio F-23)
puede ser la jugada más segura a largo plazo.
- **Fuente:** F-230 (🟢A, Deci & Ryan 2000 — ya citada en tesis 19 por el marco general de SDT; esta
  lectura profunda añade el efecto de socavamiento, no citado antes en esta opinión)
- **Leído a fondo:** 2026-08-07 (mismo bloqueo de proxy para doi.org; contenido reconstruido vía
  búsqueda dirigida sobre el meta-análisis de 1999 de recompensas contingentes y la distinción
  motivación autónoma/controlada)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 7 ni de tesis 19 — es un matiz
  de diseño (a quién conviene pagar vs. a quién conviene solo dar feedback) que ninguna de las dos
  tesis tenía explícito, marcado como instinto razonado sobre teoría, no como dato de campo peruano.

### 7. Un disclaimer de que una cifra es "referencial" o "arbitraria" no neutraliza su efecto de ancla — solo cambiarla o quitarla lo hace
Lectura profunda de F-220 (Tversky & Kahneman 1974, el experimento original de la rueda de la
fortuna): sujetos vieron girar una rueda de números que sabían manipulada para caer solo en 10 o
65, y aun así su estimación posterior (¿qué % de países africanos hay en la ONU?) se desplazó ~20
puntos porcentuales entre el grupo que vio 10 (mediana 25%) y el que vio 65 (mediana 45%) — el
mecanismo que proponen los autores es ajuste insuficiente desde el ancla, no desconocimiento de que
es arbitraria. **Heurística de decisión:** cualquier mitigación de riesgo de anclaje que dependa de
"aclarar que la cifra es referencial/estimada/no vinculante" (el tipo de disclaimer legal que
Compliance suele pedir) no está probada por esta evidencia — el experimento fundacional muestra el
efecto sobreviviendo intacto pese a que el sujeto ve con sus propios ojos que el número es
aleatorio. La única mitigación que la evidencia sí sostiene es no mostrar el ancla, o reemplazarla
por una de menor magnitud persuasiva — no explicarla. Conecta con tesis 15 (cifra headline como
ancla) y con C.2 del Bloque 4 del Playbook (tesis 18): el disclaimer "sujeto a evaluación" en una
pieza de venta no es, por esta evidencia, una defensa de compliance suficiente contra el efecto de
anclaje que la misma pieza genera — son dos riesgos distintos (regulatorio vs. conductual) que un
mismo texto legal no resuelve los dos a la vez.
- **Fuente:** F-220 (🟢A, Tversky & Kahneman 1974, *Science* — paper fundacional)
- **Leído a fondo:** 2026-08-08 (URL de science.org bloqueada por el proxy del entorno; reconstruido
  vía búsqueda dirigida que confirma el diseño experimental exacto, las medianas de 25%/45% y la
  explicación mecanística de ajuste insuficiente)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 15 ni de tesis 18 (ambas ya
  citan a F-220/F-175) — agrega una heurística de proceso: la mitigación textual/legal del efecto de
  anclaje no tiene respaldo en la fuente fundacional, solo el rediseño de qué ancla se muestra.

### 8. La satisfacción subjetiva y el desempeño objetivo de un sistema conversacional no solo pueden divergir — pueden moverse en direcciones opuestas en el mismo segmento
Lectura profunda de F-148 (Hone & Graham 2000, cuestionario SASSI): en los estudios de validación
del cuestionario, los usuarios de mayor edad necesitaron más tiempo para completar las tareas (peor
desempeño objetivo) pero calificaron el sistema de forma consistentemente más favorable que los
usuarios más jóvenes (mejor satisfacción subjetiva) — la misma variable (edad) empuja las dos
métricas en direcciones opuestas, no solo con distinta magnitud. **Heurística de decisión:** al
evaluar cualquier asistente o agente conversacional (el de Rimac incluido), no basta con separar
métrica objetiva de métrica subjetiva — hay que cruzarlas por segmento, porque un promedio agregado
de satisfacción alta puede estar escondiendo exactamente al segmento (típicamente el de menor
familiaridad digital, más edad) que peor lo está usando en términos de tarea completada con éxito.
Reportar solo NPS/satisfacción sin desagregar por segmento de usuario puede leer como éxito un
producto que sistemáticamente sirve peor a quien más lo necesita.
- **Fuente:** F-148 (🟢A, Hone & Graham 2000, *Natural Language Engineering*, Cambridge)
- **Leído a fondo:** 2026-08-08 (URL de cambridge.org bloqueada por el proxy del entorno;
  reconstruido vía búsqueda dirigida que confirma los 6 factores del cuestionario y el hallazgo de
  divergencia por edad entre tiempo de tarea y calificación subjetiva)
- **Conexión razonada, no forzada:** no cambia la confianza de ningún riesgo ya vigente — profundiza
  el riesgo ya anotado "medir el agente conversacional de IA con la métrica equivocada" con un
  mecanismo concreto de por qué agregar sin segmentar puede ocultar el problema en vez de revelarlo.

### 9. El silencio metodológico (no decir qué perspectiva de costeo o año de precios se usó) es la norma, no la excepción, en la literatura de costeo en salud — y debe leerse como bandera roja, no como neutralidad
Lectura profunda de F-66 (Xu et al. 2020, revisión crítica de micro-costing): el método formal tiene
tres etapas (identificar los recursos usados, medir cada uno con estudios de tiempos/movimientos,
valorizarlos a precio unitario), pero la revisión encuentra que la mayoría de estudios publicados no
las documenta bien — cerca de un tercio no especifica la perspectiva de costeo (¿del sistema de
salud? ¿del paciente? ¿social?), solo 20.5% adopta perspectiva social (la más completa), 32.8% no
especifica el año de precios usado y 44.1% no aclara si ajustó por inflación al combinar costos de
años distintos. **Heurística de decisión:** cuando aparezca cualquier cifra de "costo por atención",
"ahorro por triage" o "costo unitario evitado" (el tipo de número que sostendría el caso de negocio
de farmacia+triage IA de tesis 9, o cualquier cálculo de unit economics de `lapuerta`/proyectos de
salud), la ausencia de perspectiva/año de precios/ajuste por inflación explícitos no es un detalle
de reporting menor — es, según esta revisión, lo que le pasa a más de un tercio de la literatura
publicada, así que un número sin esos tres datos no debe tratarse como comparable o confiable por
default: hay que pedirlos antes de citarlo en un caso de negocio interno.
- **Fuente:** F-66 (🟢A, Xu et al. 2020/2021, *Health Economics Review*)
- **Leído a fondo:** 2026-08-08 (URLs de ncbi.nlm.nih.gov y del PDF alojado en squarespace
  bloqueadas por el proxy del entorno; reconstruido vía búsqueda dirigida que confirma las tres
  etapas y los porcentajes exactos de vacíos de reporting)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 9/10 (farmacia+triage IA) —
  agrega un criterio de auditoría específico para cualquier cifra de costo-efectividad que el
  proyecto use en el futuro para dimensionar esa oportunidad, algo que ninguna tesis vigente tenía
  explícito todavía.

### 10. Que un modelo de IA clínica haya pasado el silent trial una vez no es una garantía permanente — es una fotografía de un momento, sin estándar todavía de cuándo repetirlo
Lectura profunda de F-56 (Nature Health, scoping review 2025): el propio review encuentra que **no
existen guías formales** todavía sobre cómo correr una evaluación silenciosa de IA clínica —cribó
literatura de 2015 a 2025, 891 artículos, solo 75 cumplieron criterio de inclusión— pese a que el
mecanismo ya se reconoce como la fase crítica que menos atención recibe frente al desarrollo in
silico del modelo. El caso que cita el review es la evidencia más aguda: un modelo pasó su
validación inicial, pero en un silent trial posterior su AUC **colapsó de 0.90 a 0.50** — no por un
error del modelo en sí, sino por *distribution shift* real (cambió la distribución de edad, la
lateralidad de los riñones obstruidos en la cohorte, y el formato de imagen del equipo). **Heurística
de decisión:** tesis 10 ya trata el silent trial como el gate correcto antes de producción (60-90
días, no saltárselo) — esta lectura agrega el matiz que falta: "pasó el silent trial" no es un
casillero que se marca una vez y queda válido para siempre, es una medición vigente solo mientras la
población/contexto de despliegue no cambie. Si el piloto de farmacia+triage IA (tesis 9/10) cambia de
zona geográfica, de mezcla de síntomas/edad de pacientes, o de dispositivo/formato de captura después
de pasar su silent trial inicial, eso es un disparador para **repetirlo**, no evidencia de que "ya
está validado" — y hoy no hay ni siquiera un estándar de la industria que diga cada cuánto.
- **Fuente:** F-56 (🟢A, Nature Health 2025, scoping review de silent trials para IA médica — ya
  citada en tesis 10 solo por el resumen de una línea del ledger)
- **Leído a fondo:** 2026-08-09 (URL de nature.com bloqueada por el proxy del entorno; reconstruido
  vía búsqueda dirigida que confirma el conteo de artículos cribados/incluidos, la ausencia de guías
  formales, y el caso de colapso de AUC por distribution shift)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 10 (sigue Alta) — agrega un
  criterio de vigencia temporal al gate de silent trial que la tesis no tenía explícito: el gate
  correcto no es solo "correrlo antes de lanzar", es "re-correrlo cuando cambie la población".

### 11. Probar si una intervención funciona y probar si se puede implementar con fidelidad son dos preguntas que conviene correr a la vez desde el día uno del piloto, no en secuencia
Lectura profunda de F-55 (Cully et al./Bauer 2012, protocolo de estudio en *Implementation
Science*): el diseño "híbrido tipo 2" que usa este estudio de terapia cognitivo-conductual breve en
atención primaria no es solo un detalle metodológico — es una de tres variantes con lógica de
negocio distinta (Curran et al. 2012): tipo 1 prioriza probar si la intervención funciona y solo
recolecta implementación como dato secundario; tipo 3 hace lo inverso (foco en la estrategia de
implementación de algo ya probado efectivo); tipo 2 mide las dos cosas **con el mismo peso, en
paralelo, desde el mismo piloto** — en este caso, desenlaces clínicos (depresión, ansiedad,
funcionamiento físico) junto con desenlaces de implementación (adherencia del paciente, adopción y
fidelidad del proveedor) medidos en el mismo protocolo de 320 participantes. **Heurística de
decisión:** el error de secuenciar ("primero probamos si el triage IA funciona clínicamente, después
—en un piloto aparte— vemos si el farmacéutico lo puede operar con fidelidad en la práctica real") es
exactamente lo que un diseño tipo 2 evita — y las 13 "clarificaciones" del propio marco RE-AIM que ya
citó tesis 9 (heurística 5 de esta sección, F-53) documentan que los equipos tienden por defecto a
tratar la implementación como un paso posterior, no simultáneo. Para el piloto de farmacia+triage IA
(tesis 9/10), la jugada de diseño correcta es medir desde el primer día tanto la precisión/seguridad
clínica (tesis 10) como la fidelidad de uso real por el dispensador (¿sigue el protocolo?, ¿deriva
cuando corresponde?, ¿mantiene el hábito documentado de OR=29 de no pedir receta, tesis 9?) en el
mismo estudio, no en dos fases separadas.
- **Fuente:** F-55 (🟢A, Cully/Bauer et al. 2012, *Implementation Science* — ya citada en tesis 9
  solo como "ejemplo aplicado" sin desarrollar el mecanismo del diseño híbrido tipo 2)
- **Leído a fondo:** 2026-08-09 (URLs de ncbi.nlm.nih.gov/pmc.ncbi.nlm.nih.gov bloqueadas por el
  proxy del entorno; reconstruido vía búsqueda dirigida que confirma la taxonomía Curran et al. 2012
  de los tres tipos híbridos y el diseño exacto del estudio de Bauer/Cully, N=320)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 9 (sigue Alta) — agrega un
  criterio de diseño de piloto que ni tesis 9 ni tesis 10 tenían explícito: correr efectividad clínica
  e implementación en paralelo desde el inicio, no en fases separadas.

### 12. Un material visual bien diseñado no es por sí solo una "ayuda de decisión" rigurosa — el estándar de la disciplina exige, entre otros, declarar el conflicto de interés de quien la construye
Lectura profunda de F-122 (IPDAS Collaboration, *Evidence Update 2.0*, 2021): el resumen que ya tenía
el ledger ("la calidad visual/estética favorece aceptabilidad y uso") es real —la revisión sistemática
de 105 RCTs sí confirma que las ayudas de decisión mejoran conocimiento, expectativas realistas y
reducen conflicto decisional frente a la atención usual, y que el formato visual influye en
aceptabilidad— pero es solo uno de **11 dominios** que la actualización 2021 define como estándar de
una ayuda de decisión rigurosa: proceso de desarrollo, información balanceada, comunicación de
probabilidades, clarificación de valores, uso de historias personales, guía/coaching de decisión,
**divulgación de conflictos de interés**, alfabetización en salud, base en evidencia científica,
medición de efectividad, e implementación. **Heurística de decisión:** tesis 12 (icon arrays/formato
"3 de 100" mejoran comprensión en baja numeracidad) tiene razón en que la fricción es de comparación,
no de cantidad de opciones — pero un icon array bien diseñado no es, por sí solo, una "ayuda de
decisión" en el sentido que exige la disciplina que mide esto. El dominio más incómodo para cualquier
material que construya un asegurador es el de **divulgación de conflicto de interés**: IPDAS lo trata
como un dominio explícito porque quien financia o construye la ayuda de decisión tiene, casi por
definición, un interés en el resultado — exactamente el caso de cualquier comparador de productos que
Rimac diseñe para su propio catálogo. Si el proyecto alguna vez construye un "comparador" o
"simulador" formal (no solo material publicitario) y quiere poder llamarlo una ayuda de decisión seria
—no solo una pieza de conversión bien diseñada—, el checklist correcto es el de los 11 dominios de
IPDAS, no solo el criterio visual de tesis 12.
- **Fuente:** F-122 (🟢A, IPDAS Collaboration/Stacey & Volk 2021, *Medical Decision Making* — ya
  citada en tesis 12 solo por el hallazgo de calidad visual/aceptabilidad)
- **Leído a fondo:** 2026-08-09 (URL de pmc.ncbi.nlm.nih.gov bloqueada por el proxy del entorno;
  reconstruido vía búsqueda dirigida que confirma los 105 RCTs de la revisión sistemática base y los
  11 dominios/13 revisiones de la actualización 2021)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 12 (sigue Alta) — agrega un
  criterio de rigor más exigente que la tesis no tenía explícito: "material visual estructurado" y
  "ayuda de decisión IPDAS-completa, con conflicto de interés declarado" no son la misma barra.

### 13. La ventana regulatoria/de infraestructura para un canal de salud digital se cierra si no se invierte a la par en la competencia del recurso humano que lo opera
Lectura profunda de F-41 (Rees & Peralta 2024, *Oxford Open Digital Health*, historia de la
telemedicina peruana): el resumen que ya tenía el ledger ("necesidad urgente de un sistema nacional
de telesalud integrado que atienda brechas socioculturales") no decía el mecanismo — el estudio
documenta que Perú ya tenía política y regulación de telesalud preparada antes de la pandemia, lo que
permitió una expansión rápida en 2020, pero los volúmenes de atención remota **crecieron y luego
cayeron** tras el pico pandémico (mismo patrón que ya citó tesis 9 vía F-40/F-41), y el propio
artículo señala como brecha específica no resuelta la **competencia digital/de telesalud del recurso
humano en salud**, no solo la infraestructura o el marco regulatorio. **Heurística de decisión:**
tener la política y la infraestructura listas (lo que ya tenía Perú) es condición necesaria para
escalar rápido cuando llega el evento forzador (pandemia, mandato regulatorio, lanzamiento de
producto) — pero si no se invierte a la par en que el operador humano del canal (médico, farmacéutico,
asesor) sepa usarlo bien, el volumen se retrae cuando termina la urgencia, no se sostiene como cambio
estructural. Aplica directo al piloto de farmacia+triage IA (tesis 9): la infraestructura de delivery
y el PL 08488 no bastan si no hay entrenamiento explícito del dispensador (que ya falla en pedir
receta, OR=29, tesis 9) para operar el nuevo canal.
- **Fuente:** F-41 (🟢A, Rees & Peralta 2024, *Oxford Open Digital Health* — ya citada en tesis 9
  junto con F-40 solo por el hallazgo de "ventana de oportunidad de corto plazo")
- **Leído a fondo:** 2026-08-10 (URLs de ncbi.nlm.nih.gov y ouci.dntb.gov.ua bloqueadas por el proxy
  del entorno; reconstruido vía búsqueda dirigida sobre el resumen de Oxford Academic/PubMed que
  confirma la preparación regulatoria pre-pandemia, el patrón de crecimiento-caída, y la brecha de
  competencias de recurso humano)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 9 (sigue Alta) — agrega un
  criterio de ejecución que la tesis no tenía explícito: la ventana de oportunidad no se sostiene con
  solo política+infraestructura, necesita inversión paralela en competencia del operador humano.

### 14. Antes de tratar un salto en una métrica de retención/crecimiento como evidencia de un moat durable, hay que abrir qué línea de producto específica lo generó
Lectura profunda de F-303 (Figma Inc., Form 8-K, resultados Q1 2026): el ledger ya tenía el dato
agregado (revenue +46% YoY, NDR 139%, ~690.000 clientes de pago) con la advertencia de que la
definición de NDR de Figma excluye clientes con churn. Lo que la lectura de hoy añade es el impulsor
específico: la cobertura de la propia earnings call describe el salto de NDR (el más alto en más de
dos años, +3pp vs. Q4) como impulsado en particular por la **monetización de créditos de IA**, no por
expansión pareja de asientos en la base de clientes existente. **Heurística de decisión:** un salto en
una métrica de retención/expansión no es automáticamente evidencia de un negocio estructuralmente más
pegajoso — antes de citarlo como benchmark (p. ej. en cualquier caso de negocio interno que compare a
Rimac con un SaaS de alto NDR), hay que abrir qué línea de producto específica lo generó. Un NDR alto
impulsado por un producto nuevo todavía no maduro (créditos de IA) es una señal más volátil —con
exposición a que ese mismo producto sea el origen de la próxima caída— que un NDR alto sostenido por
expansión ancha de la base ya asentada. Conecta directo con tesis 21 (argumentar por mecanismo, no por
multiplicador) y tesis 25 (exigir el ratio auditado, no la cifra headline, antes de leer cualquier
apuesta como éxito).
- **Fuente:** F-303 (🟢A, filing SEC primario — ya citada en `_nodes/tendencias-diseno-innovacion.md`
  §4.1 solo por la cifra agregada)
- **Leído a fondo:** 2026-08-10 (sec.gov bloqueado por el proxy del entorno, igual que en el registro
  original de `cronista`; reconstruido vía búsqueda dirigida sobre cobertura de la misma earnings call
  —stocktitan, biggo, mlq— que coincide en cifras y añade el detalle del impulsor de IA)
- **Conexión razonada, no forzada:** no cambia la confianza de ninguna tesis existente — es un caso
  concreto nuevo que ilustra el principio ya vigente en tesis 21/25 (desconfiar de una cifra headline
  sin abrir su mecanismo), aplicado por primera vez a una métrica de retención de SaaS en vez de a un
  ROI de diseño o un combined ratio de seguros.

### 15. Un efecto "estrella" de la literatura de management casi siempre depende de cómo se midió el desempeño — desconfiar de una correlación cuando el estudio no reporta si usó medición objetiva o autoreportada
Lectura profunda de F-434 (Junni, Sarala, Taras & Tarba 2013, *Academy of Management Perspectives*,
meta-análisis de 66 estudios sobre ambidestreza organizacional): el resumen que ya tenía el ledger
decía que la relación ambidestreza→desempeño "es positiva pero fuertemente moderada por contexto y
elección metodológica", con el paralelo ya trazado a F-239 (design thinking, efecto mediado por
empoderamiento psicológico). La lectura de hoy pone número y mecanismo exacto al moderador
metodológico: el efecto agregado es moderado (r≈0.26), pero es sistemáticamente **más alto cuando el
estudio mide desempeño con una escala percibida/autoreportada por el propio gerente** en vez de con un
indicador objetivo (contable, de mercado), y más alto también cuando se usa una medida "combinada" de
ambidestreza en vez de una medida "balanceada". **Heurística de decisión:** cuando un estudio de
management reporta que un constructo de moda (ambidestreza, design thinking, agilidad, cultura de
innovación) "predice desempeño", el primer chequeo antes de citarlo en un caso de negocio no es solo
buscar el tamaño de efecto — es preguntar **cómo se midió el desempeño**. Un efecto sostenido por
autoreporte del mismo gerente que también reporta cuán "ambidiestra" es su empresa es candidato a
inflarse por el mismo sesgo de deseabilidad/consistencia que un cuestionario de satisfacción de
cliente autoreportado. Refuerza, con un segundo caso independiente, el mismo patrón que ya daba F-239
en tesis 21: el constructo estrella de la literatura de gestión rara vez funciona por el mecanismo
directo que su nombre sugiere.
- **Fuente:** F-434 (🟢A, meta-análisis peer-reviewed — ya citada en
  `_nodes/tendencias-diseno-innovacion.md` §12.1 solo por el paralelo con F-239, sin el detalle del
  moderador de medición)
- **Leído a fondo:** 2026-08-10 (journals.aom.org con acceso restringido en esta sesión; reconstruido
  vía búsqueda dirigida sobre scispace/researchgate/sciencedirect que confirma el tamaño de efecto
  agregado r≈0.26 sobre 66 estudios y el moderador de tipo de medición de desempeño)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 21 (sigue Alta) — agrega un
  segundo caso, de una disciplina de gestión distinta al diseño, del mismo patrón: escrutar el
  instrumento de medición de desempeño antes de aceptar una correlación de management como palanca de
  negocio.

### 16. Dar "elección" entre planes con el mismo subsidio no es neutral — puede detonar una espiral de selección adversa que colapsa el plan generoso en pocos años
Lectura profunda de F-91 (caso Blue Cross/Blue Shield, con el mecanismo mejor documentado en el caso
gemelo de Harvard, Cutler & Reber 1998, citado por la misma literatura): en 1995 Harvard pasó de
subsidiar el costo del seguro de salud a un esquema de "contribución igual" — la universidad pagaba
lo mismo sin importar qué plan eligiera el empleado, y este cubría la diferencia de su bolsillo. El
resultado no fue una simple redistribución de matrícula: a medida que el plan más generoso (PPO) subía
de precio relativo, los empleados más sanos migraban al plan más barato, lo que subía el costo per
cápita del plan generoso (quedaban los de mayor riesgo), lo que forzaba otra subida de precio, lo que
inducía más migración — en 3 años el PPO colapsó por completo dentro del esquema de contribución
igual. La pérdida de bienestar medida fue 2-4% del gasto base, aun cuando la mayor competencia entre
planes bajó las primas generales 5-8%: el ahorro agregado no compensa el colapso del producto que
concentró el riesgo. **Heurística de decisión:** cualquier diseño que le dé al cliente "elección libre"
entre una versión barata/básica y una cara/completa de un mismo seguro, con el mismo subsidio o aporte
fijo del lado de quien paga, no es solo una decisión de UX de catálogo — es un experimento de
selección adversa en marcha. El chequeo previo no es "¿le gusta al cliente tener opciones?" sino "¿qué
le pasa al perfil de riesgo del plan más generoso si los más sanos se van?", antes de lanzar, no
después de ver subir el costo.
- **Fuente:** F-91 (🟢A, *Journal of Health Economics*/*Explorations in Economic History* — caso
  empírico BC/BS; el mecanismo exacto con cifras de bienestar corresponde al caso gemelo de Harvard de
  la misma línea de investigación, Cutler & Reber 1998, NBER)
- **Leído a fondo:** 2026-08-12 (sciencedirect.com y nber.org bloqueados por el proxy de esta sesión —
  mismo bloqueo ya documentado para fuentes académicas; reconstruido vía búsqueda dirigida que
  confirma el mecanismo, el plazo de 3 años y las cifras de bienestar/prima)
- **Conexión razonada, no forzada:** heurística general de diseño de producto de seguros, no
  específica de ninguna tesis vigente — aplica a cualquier evaluación futura de "dar más opciones de
  plan/cobertura" en `lapuerta` o en un producto real de Rimac. No cambia la confianza de ninguna
  tesis existente.

### 17. Auditar qué variable de necesidad real queda AFUERA de una fórmula de asignación/precio, no solo si las que entran son plausibles
Lectura profunda de F-111 (pago por capitación de atención primaria en el NHS, fórmula Carr-Hill): el
"Global Sum" que financia a cada consultorio del NHS se calcula ponderando edad, sexo, morbilidad,
mortalidad, rotación de lista de pacientes, tipo de personal y ruralidad — una fórmula que, vista por
sus componentes, luce técnicamente seria. La crítica más citada y sostenida en el tiempo (incluida en
revisiones posteriores de 2024) no es que algún componente esté mal calibrado, sino que la fórmula
**no ajusta por privación socioeconómica** — y esa omisión, no un error en los pesos existentes,
es la que sistemáticamente subfinancia a los consultorios en zonas más pobres: no solo en el Global
Sum, sino en flujos de ingreso adicionales como el QOF (pago por desempeño), que también penalizan a
esas mismas zonas. **Heurística de decisión:** al evaluar o diseñar cualquier fórmula de asignación,
precio o ajuste de riesgo (capitación de salud, pricing dinámico de telemática/UBI, WTP en
`lapuerta`), el chequeo de rigor no es solo "¿son razonables las variables que incluye?" — es "¿qué
variable de necesidad/riesgo real, conocida y medible, se dejó explícitamente afuera, y a quién
perjudica sistemáticamente esa omisión?". Una fórmula puede pasar todos los chequeos de las variables
que sí tiene y seguir siendo estructuralmente injusta por la que le falta.
- **Fuente:** F-111 (🟢A, *BMC Health Services Research* 2010, estudio observacional)
- **Leído a fondo:** 2026-08-12 (bmchealthservres.biomedcentral.com bloqueado por el proxy de esta
  sesión; reconstruido vía búsqueda dirigida que confirma los componentes de la fórmula y la crítica
  de omisión de privación, sostenida en literatura posterior hasta 2024)
- **Conexión razonada, no forzada:** heurística de auditoría de fórmulas/pricing, transferible a
  cualquier variable de riesgo que `lapuerta` o un producto real de Rimac calcule por reglas — no
  cambia la confianza de ninguna tesis existente, es un chequeo de proceso.

### 18. Antes de invertir en explicar una decisión de IA, preguntar si la tarea es verificable — si no lo es, la explicación no mejora el desempeño complementario humano+IA
Lectura profunda de F-243 (Fok & Weld 2024, *AI Magazine* — ya citada en
`_nodes/tendencias-diseno-innovacion.md` como base teórica de la regla C8, "verificabilidad >
explicabilidad", pero solo con el resumen de una línea hasta hoy): el argumento central no es que las
explicaciones de IA sean inútiles en general, sino que **solo ayudan en la medida en que le permiten al
humano verificar de forma independiente si la recomendación de la IA es correcta** — no en la medida en
que hacen más legible o interpretable el razonamiento interno del modelo, que es el tipo de explicación
que la mayoría de productos construye por default. Los autores revisan evidencia de que, en la mayoría
de contextos de decisión reales, ningún método de explicación logra esa verificación — porque la tarea
misma no la permite (no hay un dato externo con el que el humano pueda contrastar la respuesta en el
momento de decidir), no porque la explicación esté mal diseñada. **Heurística de decisión:** antes de
construir una función de "explicar la recomendación" en el agente conversacional de Rimac, un triage
IA o un configurador de producto, la primera pregunta no es "¿qué tan clara es la explicación?" sino
"¿puede el usuario, en ese momento, verificar de forma independiente si la IA tiene razón?" (ver la
fuente, pedir un segundo dato, comparar contra algo que ya sabe). Si la respuesta es no, invertir en
hacer la explicación más elaborada no genera el efecto que se busca — hay que invertir en construir esa
vía de verificación (o aceptar que la confianza tendrá que ganarse por otro mecanismo, no por
explicabilidad).
- **Fuente:** F-243 (🟢A, *AI Magazine*, teoría + síntesis de evidencia empírica)
- **Leído a fondo:** 2026-08-12 (onlinelibrary.wiley.com y arxiv.org bloqueados por el proxy de esta
  sesión; reconstruido vía búsqueda dirigida sobre semanticscholar/citedrive que confirma la teoría de
  verificabilidad, la distinción con interpretabilidad, y el hallazgo de que la mayoría de tareas no es
  verificable independientemente del método de explicación)
- **Conexión razonada, no forzada:** profundiza directamente la base de tesis 22 (personalización con
  IA puede reducir conversión cuando el dato es sensible; el mecanismo que calibra confianza es
  verificabilidad, no explicabilidad genérica) — no cambia su confianza (sigue Alta), pero ahora el
  Lobo leyó a fondo la fuente que ya sostenía esa distinción, no solo el resumen de una línea.

### 19. La advertencia sobre el propio sesgo de un hallazgo a veces ya está en el paper original — pero vive en el análisis de sensibilidad, no en el titular
Lectura profunda de F-16 (Mertens et al. 2022, PNAS — el meta-análisis fundacional pro-nudge que
tesis 6 ya cuestiona, pero solo vía las cinco fuentes que lo rebaten, F-17 a F-21; el propio F-16
nunca se había leído a fondo): confirma el tamaño exacto (447 tamaños de efecto, 212 estudios,
N=2,148,439, d=0.43 agregado) y agrega dos datos que el resumen de una línea no traía. Primero, el
rango de d individuales va de -0.69 a 3.08 — una dispersión tan amplia que citar "el efecto del
nudge es d=0.43" ya era estadísticamente indefendible como cifra única incluso antes de que llegara
la crítica de Maier (F-17): la heterogeneidad por técnica y dominio no es un matiz posterior, está
en el propio dataset original. Segundo, y más importante: los propios autores corrieron un análisis
de sensibilidad para sesgo de publicación severo y encontraron que el efecto colapsaba a un tamaño
mínimo bajo ese escenario — el mismo resultado que después popularizó la corrección de
Maier/Data Colada como la refutación definitiva ya estaba, en germen, en el propio paper de 2022,
pero enterrado en un análisis secundario, no en el abstract ni en el titular que circuló.
**Heurística de decisión:** antes de citar el hallazgo central de un paper por su cifra de abstract,
vale la pena revisar si el propio estudio ya corrió —y reportó, sin destacar— un análisis de
sensibilidad o robustez que apunta en la dirección contraria; encontrarlo ahí, no en una réplica
posterior, es la señal más barata de que una cifra headline no va a sobrevivir escrutinio.
- **Fuente:** F-16 (🟢A, Mertens et al. 2022, PNAS — ya citada indirectamente en tesis 6 vía F-17-21)
- **Leído a fondo:** 2026-08-13 (pnas.org bloqueado por el proxy del entorno; reconstruido vía
  búsqueda dirigida que confirma N=2,148,439, rango de d -0.69 a 3.08, y el análisis de sensibilidad
  de publication bias de los propios autores)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 6 (sigue Alta) — profundiza el
  propio F-16, que hasta hoy solo se conocía por lo que decían las fuentes que lo refutan, nunca
  leído directamente.

### 20. Medir la fidelidad de una IA con otra IA (RAGAS/LLM-as-judge) no es una vara neutral — correlaciona modestamente con el juicio humano y hereda sesgos sistemáticos que promediar más jueces no cancela
Lectura profunda de F-151 (Es et al. 2024, RAGAS — ya citada en el riesgo vigente "medir el agente
conversacional de IA con la métrica equivocada" solo como "el estándar de la industria"): confirma
el mecanismo técnico (faithfulness: un LLM extrae las afirmaciones discretas de la respuesta y
verifica cada una contra el contexto recuperado; answer relevancy: cosine similarity entre preguntas
sintéticas generadas a partir de la respuesta y la pregunta original) pero añade el límite que el
resumen de una línea no capturaba: la validación empírica de qué tan bien estas métricas
automatizadas correlacionan con el juicio humano real da una media armónica de apenas ~0.55 — lejos
de lo que se necesitaría para tratarlas como vara de verdad. La razón de fondo es estructural, no un
defecto de implementación de RAGAS específicamente: usar un LLM para juzgar la fidelidad de otro LLM
(o de sí mismo) hereda los sesgos sistemáticos documentados del "LLM-as-judge" —sesgo de posición,
de verbosidad, de auto-favorecimiento— y ese sesgo no se cancela promediando más jueces del mismo
tipo, porque el sesgo es compartido entre modelos de la misma generación/familia, no aleatorio.
**Heurística de decisión:** si Rimac adopta RAGAS (u otro framework LLM-as-judge) para medir si su
agente conversacional alucina coberturas, el número que arroje debe tratarse como una señal de
monitoreo continuo y barata, nunca como el veredicto final de si el agente es seguro — necesita
triangularse con una muestra de revisión humana real, no reemplazarla, exactamente el mismo
principio que ya advierte el riesgo vigente sobre medir el agente con la métrica equivocada, ahora
aplicado a la métrica que el propio ledger ya proponía como solución.
- **Fuente:** F-151 (🟢A, Es, S. et al. 2024, EACL — ya citada en el riesgo del agente conversacional,
  ahora leída a fondo)
- **Leído a fondo:** 2026-08-13 (aclanthology.org bloqueado por el proxy del entorno; reconstruido vía
  búsqueda dirigida que confirma el mecanismo de extracción/verificación de claims y la correlación
  de ~0.55 con juicio humano reportada en literatura posterior de evaluación LLM-as-judge)
- **Conexión razonada, no forzada:** no cambia la confianza de ningún riesgo/tesis vigente — matiza
  directamente el riesgo ya anotado "medir el agente conversacional de IA con la métrica equivocada":
  la solución que el propio ledger cita (RAGAS) tiene su propio techo de confiabilidad, no es una
  vara neutral.

### 21. La interfaz "correcta" no es una apuesta global de plataforma — el mismo estudio puede dar veredictos opuestos por escenario dentro de la misma tarea
Lectura profunda de F-250 (Flohr, Kalinke, Krüger & Wallach 2021, MobileHCI — ya citada en tesis
24/generative UI solo como "contraevidencia a que el chatbot es intrínsecamente mejor"): confirma que
la GUI clásica superó al chatbot en atractivo y satisfacción en el estudio de simulador (n=34, más
dos estudios de expertos previos), pero el resumen de una línea no capturaba el detalle condicional:
la ventaja se invierte específicamente en el escenario de **cambio de plan/interrupción** (el viaje
no sale como estaba previsto) — ahí la intención de uso favorece al chatbot sobre la GUI, con datos
de curva emocional y entrevista respaldando el efecto. En el escenario de "camino feliz" (todo sale
como se planeó) gana la GUI con claridad. **Heurística de decisión:** la pregunta correcta al evaluar
un canal conversacional vs. uno estructurado (para Rimac: el agente conversacional vs. un
flujo/formulario clásico de cotización o reclamo) no es "¿cuál gana en promedio?" — es "¿en qué tipo
específico de momento de la interacción gana cada uno?". La evidencia de este estudio sugiere un
patrón transferible y plausible para seguros: la interfaz estructurada gana en el flujo estándar
(cotizar, contratar, consultar cobertura), pero el canal conversacional puede tener ventaja real
específicamente en el momento de excepción/desvío (algo salió mal, el cliente necesita reencauzar) —
el mismo tipo de momento que ya señala el riesgo vigente sobre reclamos digitales fallidos (tesis 16)
como el punto de mayor fricción. Instinto razonado, no medido en seguros: el estudio es de movilidad
autónoma, no de seguros, pero el mecanismo (chatbot gana en desvío, pierde en rutina) es coherente
con lo ya documentado sobre dónde falla lo 100%-digital.
- **Fuente:** F-250 (🟢A, Flohr et al. 2021, MobileHCI — ya citada en tesis 24)
- **Leído a fondo:** 2026-08-13 (dl.acm.org y el preprint de la Universidad de Saarland bloqueados por
  el proxy del entorno; reconstruido vía búsqueda dirigida que confirma el diseño n=34 + 2 estudios de
  expertos, la ventaja de la GUI en atractivo/satisfacción, y la inversión del efecto específicamente
  en el escenario de cambio de plan)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 24 — agrega un matiz
  condicional-por-escenario que tesis 24 no tenía explícito, y conecta con tesis 16 (el reclamo, no
  la venta, es el punto de falla de lo 100%-digital) desde un ángulo de diseño de interfaz nuevo.

### 22. Cuando un cliente "abusa" de un beneficio asegurado, la primera hipótesis de diseño debe ser el precio marginal que percibe — no la mala fe
Lectura profunda de F-89 (Pauly 1968, AER — el "comment" a Arrow 1963 que fundó el campo del riesgo
moral en seguros de salud, citado en el ledger solo como capa teórica de fondo, nunca leído a fondo
hasta hoy): el hallazgo central no es que la gente use más el seguro de lo debido — es que ese uso
extra es una respuesta **racional** a un precio marginal más bajo (lo que el asegurado paga por unidad
de atención cae de p a p×(1-coaseguro)), no un fallo moral ni un síntoma de mala fe. Arrow había
argumentado que el riesgo moral ex post era motivo suficiente para intervención pública; Pauly le
respondió con un contraejemplo numérico donde ese mismo riesgo moral genera una pérdida de bienestar
que puede hacer que asegurar completamente no sea óptimo — Arrow aceptó el punto en su propia réplica
en el mismo número de la revista. **Heurística:** frente a sobreutilización de un beneficio (consultas
médicas, reclamos, uso de un servicio incluido), la primera pregunta de diseño no es "¿cómo detectamos
al que abusa?" sino "¿qué precio marginal —en plata, tiempo o esfuerzo— está viendo el asegurado en
este punto de la póliza?". La palanca que corrige esto es estructura de coaseguro/deducible (cambiar
el precio), no control antifraude (cambiar el castigo) — son intervenciones para causas distintas y
conviene no aplicar la segunda cuando el diagnóstico real es la primera. Conecta con tesis 2 (el
coaseguro como cuello de botella de comprensión): la misma variable de producto que aquí opera como
precio marginal racional es, en la tesis 2, el término que el cliente peor entiende — dos mecanismos
distintos (uno de incentivo, uno de comprensión) actuando sobre la misma palanca de producto, no el
mismo problema con dos nombres.
- **Fuente:** F-89 (🟢A, Pauly 1968, *American Economic Review* — paper fundacional del campo)
- **Leído a fondo:** 2026-08-14 (ldi.upenn.edu accesible; confirmado también contra el resumen de la
  réplica de Arrow en el mismo número)
- **Conexión razonada, no forzada:** no cambia la confianza de ninguna tesis — es una heurística de
  diagnóstico (precio vs. mala fe) que matiza cómo leer cualquier futura señal de sobreutilización,
  sin evidencia de campo peruana todavía que la ponga a prueba.

### 23. Un efecto pequeño no contradice "vale la pena intentarlo" cuando el canal cuesta casi cero — son dos preguntas distintas, no una en tensión
Lectura profunda de F-21 (DellaVigna & Linos 2022, *Econometrica* — ya citada como una de las tres
metodologías independientes detrás de tesis 6, pero nunca leída a fondo por este mecanismo de
intuición; la revisión profunda de `cronista` del 2026-07-22 sí la trabajó desde el ángulo de
"por qué murió el efecto promedio"). El dato que el resumen de tesis 6 no explicita: el propio paper
no solo documenta la caída de 8.7pp (papers académicos) a 1.4pp (unidades de gobierno a escala,
126 RCTs, 23 millones de personas) — también nota que casi todos los efectos estimados a escala,
aunque chicos, siguen siendo positivos y estadísticamente significativos, y que la selección
publicación + bajo poder estadístico académico explica ~70% de la brecha (no una diferencia real
laboratorio-vs-mundo, coherente con lo que ya tenía tesis 6 vía Hu et al. y DellaVigna-Linos).
**Heurística que sí es nueva para este ledger:** "el efecto promedio murió" (tesis 6) y "vale la
pena seguir corriendo experimentos de bajo costo" no son afirmaciones en tensión — responden
preguntas distintas. Un nudge que cuesta casi cero implementar (un mensaje de texto, un default,
un recordatorio) puede seguir siendo la apuesta correcta con un efecto de 1-2pp, porque el costo
marginal por experimento es casi cero — la vara correcta no es "¿el efecto es grande como en el
paper?" sino "¿el efecto observado, por chico que sea, justifica el costo casi nulo de la
intervención?". Aplicación directa a la propia tesis 6 (probar primero defaults en salud/finanzas):
el criterio de éxito del primer experimento propio no debería fijarse en replicar el tamaño de
efecto de un paper académico, sino en confirmar que el efecto a escala real es positivo y
significativo, que ya es suficiente para justificar el canal si el costo de correrlo es bajo.
- **Fuente:** F-21 (🟢A, DellaVigna & Linos 2022, *Econometrica*, 126 RCTs administrativos, 23M
  personas — ya citada en tesis 6)
- **Leído a fondo:** 2026-08-14 (onlinelibrary.wiley.com y el PDF del autor bloqueados por el proxy
  del entorno; reconstruido vía búsqueda dirigida que confirma el diseño, las cifras 8.7pp/1.4pp y la
  descomposición ~70% sesgo de publicación)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 6 (sigue Alta) — separa
  explícitamente dos preguntas (tamaño del efecto vs. si vale la pena el experimento) que el
  resumen previo dejaba mezcladas.

### 24. Un aumento de visitas al canal barato puede ser fricción disfrazada de éxito — verificar por qué se movió el volumen, no solo que se movió
Lectura profunda de F-109 (estudio cuasi-experimental China, gatekeeping de atención primaria —
citado en el ledger solo por su cifra agregada: +55.3% en consultas de atención primaria, -23.9% en
visitas hospitalarias, sin aumento significativo del gasto en atención primaria). El detalle que el
resumen de una línea no capturaba: los propios autores leen ese patrón como evidencia de
**inefectividad**, no de éxito — si la atención primaria realmente hubiera absorbido la demanda
desviada del hospital, el gasto en atención primaria debería haber subido con las visitas; que no
subiera (apenas +1.6%, no significativo) sugiere que la caída de visitas/gasto hospitalario se debe
en parte a que los pacientes encontraron **engorroso o difícil obtener el reembolso** en el hospital,
no a que la atención primaria mejoró su capacidad real de resolver el caso. Un estudio cualitativo
sobre el mismo tipo de piloto (bibliografía relacionada, no en el ledger) documenta el mecanismo de
fondo: un esquema de salario por desempeño desincentivaba la motivación clínica en atención primaria,
atrapando el sistema en ciclos que erosionan capacidad, personal y confianza del paciente a la vez.
**Heurística:** cuando una métrica de "volumen redirigido a un canal más barato" mejora (consultas
que migran de hospital a atención primaria, o en el caso de Rimac, de un canal caro a uno digital/de
menor costo), la pregunta que decide si es una victoria real no es "¿subió el volumen del canal
barato?" sino "¿por qué bajó el volumen del canal caro?" — si la caída viene de que el canal caro
se volvió más difícil de usar (fricción), en vez de que el canal barato se volvió genuinamente mejor,
la señal es frágil y puede revertirse o generar resentimiento del cliente en cuanto se note la
fricción. Segunda confirmación independiente, en un país y sector distintos, de la intuición 13
(2026-08-10: la ventana de un canal de salud digital se cierra sin invertir a la par en la
competencia del recurso humano que lo opera) — aquí el mecanismo es salarial/incentivo del proveedor
de atención primaria china, no telesalud peruana, pero el patrón (redirigir volumen sin invertir en
la capacidad real del canal receptor) es el mismo. Aplicación directa a tesis 9: si el modelo
farmacia-frente-primario de Perú mide éxito solo en "consultas atendidas en farmacia" sin verificar
si la caída en el canal formal viene de fricción de acceso (tiempo de espera, costo de traslado) en
vez de mejor resolución en farmacia, corre el mismo riesgo de falso positivo que documenta este caso.
- **Fuente:** F-109 (🟢A, estudio DiD, China, New Rural Cooperative Medical Scheme, 200,685
  afiliados, 17 municipios, 2012-2014)
- **Leído a fondo:** 2026-08-14 (pmc.ncbi.nlm.nih.gov bloqueado por el proxy del entorno;
  reconstruido vía búsqueda dirigida que confirma cifras exactas y la lectura de "inefectividad" de
  los propios autores, más el mecanismo cualitativo de un estudio relacionado sobre el mismo tipo de
  piloto)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 9 (sigue Alta en la oportunidad
  de mercado/distribución) — agrega un criterio de verificación explícito (auditar la causa de la
  caída en el canal caro, no solo el alza en el barato) que la tesis no tenía, y refuerza desde un
  país distinto la intuición 13 ya registrada.

### 25. El precio no es la única palanca de selección — el propio diseño de cobertura es un cuarto instrumento, y los aseguradores lo usan para repeler al riesgo caro sin tocar la tarifa
Lectura profunda de F-92 (Geruso & Layton 2017, *Journal of Economic Perspectives* — citado en el
ledger solo como "contrapeso a 'el modelo está roto'", nunca leído a fondo). El paper distingue dos
marcos para pensar la selección: el de **"contrato fijo"** (el más intuitivo — el contrato ya está
definido, y el trabajo de la política pública es ajustar precio: rating comunitario, subsidios/multas,
ajuste de riesgo) y el de **"contrato endógeno"** — la cobertura misma se diseña en respuesta a la
selección. Un asegurador que no puede subir el precio a un diabético (rating comunitario) puede en
cambio angostar la red de endocrinólogos o el formulario de insulina — no para ahorrar costo directo,
sino porque un plan deliberadamente peor en esa dimensión repele selectivamente al riesgo caro sin
tocar la tarifa que ve el regulador. El ajuste de riesgo (la herramienta que la tesis 9/17 asume como
la palanca principal) es siempre imperfecto porque no observa todo lo que el asegurador sí observa vía
el diseño del producto — por eso el paper trata la cobertura reducida en servicios de alto uso por
enfermos crónicos como una **cuarta** palanca de política (junto a rating, subsidios y ajuste de
riesgo: la regulación directa del contrato), no como una falla de implementación de las otras tres.
**Heurística:** al auditar el riesgo de selección adversa de cualquier producto propio (o de un
competidor), no basta con mirar el precio y el ajuste de riesgo declarado — hay que revisar si la
cobertura específica de las condiciones caras (no la lista de beneficios en general) está diseñada más
angosta que el resto del plan, porque ese es el canal indirecto y menos visible por el que un
asegurador selecciona riesgo cuando el precio está regulado.
- **Fuente:** F-92 (🟢A, Geruso, M. & Layton, T.J. 2017, *Journal of Economic Perspectives* 31(4),
  también circula como NBER Working Paper 23876)
- **Leído a fondo:** 2026-08-15 (pmc.ncbi.nlm.nih.gov bloqueado por el proxy del entorno;
  reconstruido vía búsqueda dirigida que confirma el marco "contrato fijo vs. endógeno" y los cuatro
  instrumentos de política — rating comunitario, subsidios/multas, ajuste de riesgo, regulación de
  contrato)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 9/17 (siguen Alta) — agrega un
  cuarto instrumento de política que el resumen previo no distinguía, y un criterio de auditoría de
  producto (cobertura angosta como selección disfrazada) transferible a cualquier diseño propio.

### 26. El intervalo de repaso óptimo no es fijo — se encoge, como proporción del tiempo que la retención debe durar, cuanto más lejos está la prueba
Lectura profunda de F-218 (Cepeda et al. 2006, *Psychological Bulletin* — citado en el ledger solo
para respaldar "la práctica espaciada supera a la masiva" en el deck de onboarding de Universidad
Vida, nunca leído a fondo). El meta-análisis (839 comparaciones, 317 experimentos, 184 artículos) no
solo confirma que espaciar gana — encuentra que el intervalo entre sesiones de estudio (ISI) que
maximiza la retención **no es un número fijo**: como proporción del intervalo de retención (RI, el
tiempo hasta la prueba real), el gap óptimo cae de **~20-40% del RI para una prueba a 1 semana** a
solo **~5-10% del RI para una prueba a 1 año**. Es decir, cuanto más lejos está el momento en que el
conocimiento tiene que sobrevivir, proporcionalmente **más cerca**, no más lejos, hay que poner las
sesiones de repaso entre sí. **Heurística:** una recomendación genérica de "usa práctica espaciada" es
incompleta sin fijar primero el horizonte de retención que importa — un programa de onboarding que
necesita sobrevivir hasta la primera venta (semanas) puede espaciar con un gap generoso; un programa
de compliance o de producto que debe sostenerse un año entero necesita sesiones de repaso
proporcionalmente más frecuentes, no el mismo cronograma escalado. Aplicación directa al propio deck
de Universidad Vida (F-218 ya citado ahí): el cronograma de refuerzo debería fijarse según cuánto
tiempo después del onboarding se espera que el asesor use el conocimiento sin apoyo, no copiar un
espaciado estándar.
- **Fuente:** F-218 (🟢A, Cepeda, N.J. et al. 2006, *Psychological Bulletin* 132(3):354-380)
- **Leído a fondo:** 2026-08-15 (augmentingcognition.com bloqueado por el proxy del entorno;
  reconstruido vía búsqueda dirigida que confirma la función en U invertida ISI/RI y los porcentajes
  20-40%→5-10%)
- **Conexión razonada, no forzada:** no crea tesis nueva (F-218 no sostiene ninguna de las 25 tesis de
  negocio, es evidencia de un proyecto interno específico) — refina el uso ya dado a la fuente con el
  parámetro cuantitativo que el resumen de una línea no traía.

### 27. Que la IA suba el desempeño objetivo no cierra la brecha de autopercepción — y quien más sabe de IA en teoría es quien peor calibra su propio desempeño con ella
Lectura profunda de F-401 (Fernandes et al. 2026, *Computers in Human Behavior* — citado en el ledger
del node de tendencias como la fuente que manda H5 a "parcial", nunca leído a fondo por este
mecanismo). Dos estudios (N=246 y N=452, el segundo réplica interna del primero): con asistencia de
IA en razonamiento lógico, el desempeño objetivo sube ~3 puntos sobre la norma poblacional, pero la
autoestimación sube ~4 puntos — la brecha percepción-realidad existe pero es modesta (~1 punto),
bastante por debajo de lo que el node esperaba. El hallazgo que el resumen de una línea del ledger no
capturaba: el clásico efecto Dunning-Kruger (los de peor desempeño se sobreestiman más) **desaparece**
con el uso de IA — la asistencia nivela el desempeño real de todos, pero sin corregir la
sobreestimación de nadie. Y el dato más contraintuitivo de los dos estudios: **mayor alfabetización en
IA correlaciona con menor precisión metacognitiva** — quien más sabe técnicamente de cómo funciona un
modelo no es quien mejor calibra su propio desempeño usándolo, es peor. **Heurística:** un programa de
alfabetización en IA (para asesores usando el agente conversacional, o para el equipo evaluando el
triage IA de tesis 10) no entrena por sí solo la calibración de cuándo confiar o no en la
recomendación del modelo — son dos habilidades distintas, y este hallazgo sugiere que pueden moverse
en direcciones opuestas. Cualquier piloto que combine capacitación técnica en IA con una decisión de
alto riesgo (aprobar un reclamo, confiar un triage) debería medir la calibración por separado, no
asumir que sube junto con el conocimiento técnico.
- **Fuente:** F-401 (🟢A, Fernandes, D. et al. 2026, *Computers in Human Behavior* 175:108779 — Study
  1 N=246, Study 2/réplica N=452)
- **Leído a fondo:** 2026-08-15 (sciencedirect.com con URL de journal genérica en el ledger, no de
  artículo — reconstruido vía búsqueda dirigida que ubicó el artículo exacto, incluyendo el dato de
  Study 1 (N=246) que el ledger no distinguía del N=452 de la réplica)
- **Conexión razonada, no forzada:** no cambia el estado de H5 en `_nodes/tendencias-diseno-innovacion.md`
  (sigue "parcial", el propio node ya lo registró) — agrega el hallazgo de alfabetización↔calibración
  inversa, ausente del resumen previo, con aplicación directa a tesis 10 (gate de triage IA) y al
  riesgo ya vigente sobre el agente conversacional de Rimac.

### 28. Un modelo de clasificación que fuerza "una persona = un bucket" por eje subcompensa sistemáticamente a quien combina rasgos — el arreglo es de arquitectura, no de mejor calibración dentro del bucket
Oskam, van Kleef & van Vliet (2023) analizan el modelo holandés de ajuste de riesgo (risk
equalization) para seguros de salud: el sistema clasifica a cada persona en un solo
Diagnosis-based Cost Group (DCG) por capa (primaria y secundaria), aunque tenga múltiples
condiciones a la vez. Esa camisa de fuerza de "una etiqueta por capa" produce heterogeneidad
interna dentro de cada DCG (diagnósticos distintos agrupados bajo una sola etiqueta) y, en
promedio, **subcompensa a la población con multimorbilidad** — exactamente los pacientes de
mayor costo real, el segmento que el modelo más necesita tarificar bien. Los autores prueban
un método que permite clasificar a la persona en múltiples DCGs simultáneamente
(multi-qualification), usando los 209 grupos de diagnóstico como variables explicativas
separadas en vez de forzar una sola etiqueta por persona. **Heurística de decisión:** cuando
el Lobo evalúe cualquier modelo de segmentación, tarificación o ajuste de riesgo — `lapuerta`
incluido — la pregunta de diagnóstico no es solo "¿la fórmula usa las variables correctas?"
(intuición 17) sino "¿la arquitectura del modelo permite que una persona pertenezca a más de
una categoría relevante a la vez, o fuerza una sola etiqueta por eje?". Si fuerza una sola
etiqueta, el sesgo sistemático contra quien combina rasgos no se corrige recalibrando los
coeficientes dentro de cada bucket — hay que rediseñar la arquitectura de clasificación misma.
- **Fuente:** F-97 (🟢A, Oskam, M.; van Kleef, R.C.; van Vliet, R.C.J.A. 2023, *International
  Journal of Health Care Finance and Economics* — dataset de 17M de holandeses con seguro
  básico más submuestra de 1,3M con datos de morbilidad de médicos de cabecera)
- **Leído a fondo:** 2026-08-16 (pmc.ncbi.nlm.nih.gov bloqueado por el proxy del entorno;
  reconstruido vía búsqueda dirigida — EconPapers y PubMed confirman el mecanismo de "una
  etiqueta por capa" y el drawback explícito de heterogeneidad interna que citan los autores)
- **Conexión razonada, no forzada:** amplía la intuición 17 (F-111) desde un ángulo distinto —
  no es solo qué variable de necesidad real queda afuera de la fórmula, es si el axioma de
  "una etiqueta por eje" es en sí mismo la fuente del sesgo. Transferible a auditar la
  arquitectura (no solo las variables) de cualquier extensión futura de `lapuerta`.

### 29. Que la tasa de divulgación suba en pasos sucesivos de un formulario no prueba que la confianza subió — puede ser puro foot-in-the-door operando sobre la conducta mientras la actitud no se mueve
Lectura profunda de F-143 (ya citada en tesis 13 solo por su resumen de una línea). Fleming,
Edwards, Bayliss & Seger (2023, *Journal of Cybersecurity*) corren dos estudios —uno de
laboratorio, uno online como réplica— pidiendo datos personales reales de forma repetida: la
divulgación aumenta en la solicitud posterior, y la preocupación de privacidad medida **no
cambia**. Los autores encuadran el mecanismo explícitamente como *foot-in-the-door* (un pedido
pequeño facilita uno mayor) y lo proponen como explicación de la paradoja de la privacidad. Su
recomendación práctica concreta —ausente del resumen breve que ya sostiene tesis 13— es que
**advertir a la persona de antemano** ("forewarning") sobre el patrón de solicitudes repetidas
es la palanca que sí reduce el efecto. **Heurística de decisión:** cuando el Lobo o el equipo
midan el éxito de un flujo de divulgación progresiva de datos (tesis 13,
`disposicion_compartir_datos_pricing` de `lapuerta`, cualquier onboarding de telemática/UBI)
por la tasa de campos completados paso a paso, esa métrica de conducta **no es evidencia de
que la confianza o la comodidad real con compartir datos mejoró** — puede ser el mismo
mecanismo de cumplimiento incremental que documenta este paper, operando sin que la actitud
subyacente se mueva. Medir actitud (encuesta) y conducta (tasa de completado) por separado, no
una como proxy de la otra; y si el diseño ya usa pasos progresivos a propósito, la
contramedida ética documentada (advertir del patrón) es la palanca a considerar para
consentimiento genuinamente informado, no solo alto en conversión.
- **Fuente:** F-143 (🟢A, Fleming, D.; Edwards, M.; Bayliss, J.; Seger, C. 2023, *Journal of
  Cybersecurity* 9(1):tyad005 — ya citada en tesis 13)
- **Leído a fondo:** 2026-08-16 (academic.oup.com bloqueado por el proxy del entorno;
  reconstruido vía búsqueda dirigida, incluyendo la cobertura del propio centro CREATe y el
  research portal de la University of East Anglia)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 13 (sigue Alta) — agrega
  el nombre explícito del mecanismo (foot-in-the-door) y la contramedida de forewarning,
  ausentes del resumen de una línea que la tesis ya citaba.

### 30. La tasa base de fracaso de un producto nuevo es alta y sistemática, no aleatoria — antes de escribir un post-mortem a medida, revisar primero los dos factores estructurales que ya la predicen: categoría de alta rotación y marca matriz débil
Victory, Nenycz-Thiel & Dawes (2021, *Marketing Letters*) miden fracaso de producto no con
encuesta de percepción sino con datos de panel de consumo real: **83.719 SKUs nuevos en 31
categorías de consumo masivo en EE.UU. (2002-2009)**. Un **25% de los SKUs nuevos deja de
venderse al año 1; ~40% a los 2 años**. Y el fracaso no es parejo: es sistemáticamente más
probable en categorías de **mayor revenue/rotación** (más competidas) y en SKUs lanzados por
**marcas matriz de menor participación de mercado**. **Heurística de decisión:** antes de
evaluar por qué un producto nuevo (de Rimac o de cualquier cliente que el Lobo asesore)
fracasó, la primera pregunta no es "¿qué hicimos mal en el mensaje/canal/precio?" — es si el
producto ya estaba en el cuadrante de riesgo estructural conocido: categoría grande y
competida más marca matriz sin fuerza suficiente para sostenerlo. Si la respuesta es sí, gran
parte del "fracaso" ya estaba predicho por la tasa base (1 de cada 4 al año, no una excepción)
y por dos factores medibles **antes** del lanzamiento, no por un error específico de ejecución
que amerite un rediseño completo. Aplicación directa antes de cualquier lanzamiento propio
(producto paramétrico, microseguro, canal nuevo de `lapuerta`): calcular la tasa base esperada
de la categoría y evaluar la fuerza relativa de la marca matriz ANTES de lanzar, como filtro de
priorización — no solo después, como excusa.
- **Fuente:** F-432 (🟢A, Victory, K.; Nenycz-Thiel, M.; Dawes, J. et al. 2021, *Marketing
  Letters* 32 — datos observacionales de mercado real, ya citado en
  `_nodes/tendencias-diseno-innovacion.md` §12.2)
- **Leído a fondo:** 2026-08-16 (link.springer.com bloqueado por el proxy del entorno;
  reconstruido vía búsqueda dirigida — ProQuest y ResearchGate confirman la n de 83.719 SKU,
  las tasas 25%/40% y los dos moderadores de categoría y fuerza de marca)
- **Conexión razonada, no forzada:** no crea tesis nueva (F-432 no sostiene ninguna de las 25
  tesis de negocio del Lobo, es evidencia del node de diseño/innovación) — pero la tasa base y
  los dos factores predictivos son transferibles a cualquier evaluación de lanzamiento de
  producto que haga el Lobo, incluida la ruta de producto sísmico de tesis 4 y cualquier
  extensión futura de `lapuerta` hacia microseguro/propensión.

### 31. Un metaanálisis con efecto promedio cercano a cero no cierra el debate — verificar si existe una réplica rival que reencuadre el mismo corpus por moderadores antes de citar "no hay efecto" como veredicto final
Scheibehenne, Greifeneder & Todd (2010, F-119 — ya sostiene tesis 12, nunca leído a fondo)
agregan 50 estudios de choice overload y encuentran efecto promedio virtualmente cero — la base
de la tesis 12 ("menos opciones convierte más es folklore de UX"). Lo que el resumen de una
línea no traía: existe una réplica activa y no zanjada del mismo debate. Chernev, Böckenholt &
Goodman (*Journal of Consumer Psychology*, 2015) reanalizan un corpus solapado (99
observaciones, 7.202 participantes) y encuentran que el choice overload **sí** aparece de forma
confiable bajo cuatro condiciones específicas — complejidad del conjunto de opciones, dificultad
de la tarea de decisión, incertidumbre de preferencia del propio decisor, y si la meta es elegir
vs. explorar — y Scheibehenne publicó una réplica formal a esa crítica (el intercambio sigue
activo en la literatura, no hay veredicto único aceptado). **No cambia la confianza de tesis 12**
(el efecto promedio cero sigue siendo el mejor resumen del campo agregado), pero sí acota su
alcance: el catálogo de seguros cae justo en las cuatro condiciones donde el efecto reaparece —
alta complejidad de producto (coaseguro/exclusiones, tesis 2), alta dificultad de tarea para el
segmento de baja educación financiera, e incertidumbre de preferencia genuina sobre cuánto riesgo
cubrir. Heurística transferible: "efecto promedio cero" en un metaanálisis nunca es el final de
la pregunta — preguntar primero si el propio caso de uso cae en el subconjunto de condiciones
donde una réplica rival encontró que el efecto sí existe, antes de usar el metaanálisis original
como licencia para ignorar el riesgo por completo.
- **Fuente:** F-119 (🟢A, Scheibehenne, Greifeneder & Todd 2010, *Journal of Consumer Research*)
- **Leído a fondo:** 2026-08-17 (academic.oup.com bloqueado por el proxy del entorno;
  reconstruido vía búsqueda dirigida — ResearchGate, Academia.edu y la réplica publicada de
  Scheibehenne a Chernev et al. confirman el debate activo, no solo el resumen ya citado)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 12 (sigue Alta en el efecto
  promedio) — acota su alcance a un subconjunto de condiciones donde el catálogo de seguros
  probablemente cae, sin contradecir la recomendación ya vigente de estructurar la comparación
  en vez de solo podar el catálogo.

### 32. La comisión de un intermediario no es fricción pura — puede financiar una función de mercado (mejor selección de riesgo, más competencia de precio) que un canal directo tendría que replicar de otra forma para no perder esa ventaja
Cummins & Doherty (2006, F-180 — marco teórico central de tesis 16, citado solo por su hallazgo
de "market maker", nunca leído a fondo) dan dos mecanismos concretos que el resumen de una línea
no traía. Primero, evidencia empírica de que tanto la comisión base como la contingente **se
trasladan al asegurado en la prima** — la intermediación no es gratis para el cliente, tiene un
costo real y medible. Segundo, y más importante para el negocio: la comisión contingente (basada
en rentabilidad/persistencia del negocio colocado) **alinea el incentivo del intermediario con
el del asegurador**, lo que le da al asegurador más confianza en la calidad de la selección de
riesgo que trae el bróker — y esa confianza rompe la "maldición del ganador" (winner's curse) y
empuja a los aseguradores a **competir más agresivamente en precio** por ese negocio. Es decir:
la comisión no compra solo distribución/confianza del cliente (el ángulo que ya cubre tesis 16)
— compra una mejor competencia de precio del lado de la oferta, un mecanismo que un canal 100%
digital sin intermediario tendría que replicar con otra herramienta (scoring de riesgo más
verificable, por ejemplo) para no perder esa ventaja competitiva de precio. Heurística
transferible: antes de asumir que quitar al intermediario baja el costo neto para el cliente,
descomponer la comisión en lo que compra — si una parte financia una función de mercado real
(mejor selección de riesgo, más competencia entre aseguradores), removerla sin sustituto puede
subir el precio final aunque desaparezca la línea de comisión visible.
- **Fuente:** F-180 (🟢A, Cummins, J.D. & Doherty, N.A. 2006, *Journal of Risk and Insurance*)
- **Leído a fondo:** 2026-08-17 (onlinelibrary.wiley.com bloqueado por el proxy del entorno;
  reconstruido vía búsqueda dirigida — JSTOR, IDEAS/RePEc y el resumen del propio paper vía
  Wharton confirman el mecanismo de comisión contingente y winner's curse, no solo el resumen ya
  citado)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 16 (sigue Alta) — agrega un
  segundo mecanismo (competencia de precio vía alineación de incentivos) al ya citado
  (reducción de asimetría de información), ambos del mismo paper fundacional.

### 33. Que la utilidad de un segmento crezca mientras su propio volumen se contrae no es evidencia de demanda sana — verificar si el crecimiento viene de mezcla de producto antes de citarlo como prueba de que el modelo de negocio funciona
El filing SEC de UnitedHealth Q2 2026 (F-198 — evidencia primaria central de tesis 17, citado
solo por su cifra agregada de utilidad, nunca leído a fondo) tiene un matiz que el resumen de una
línea no traía: los "adjusted scripts" de Optum Rx **cayeron** de 414 a 387 millones interanual
(-6,5%), explícitamente por la **contracción de membresía dentro de UnitedHealthcare** — su
propia aseguradora hermana — y de otros clientes. Y sin embargo la utilidad operativa **subió**
de USD 1.400M a USD 1.500M en el mismo trimestre, atribuida por la propia empresa a "adopción de
genéricos especializados y mejoras operativas continuas", no a más volumen. Lectura de negocio
directa para tesis 17: el número que sostiene la tesis (Optum Rx como motor de utilidad real) es
genuino y de fuente primaria, pero su resiliencia no depende de que el libro de asegurados crezca
— depende de mezcla de producto hacia farmacia especializada, un mecanismo más frágil frente a
shocks regulatorios de precio de especialidad (rebates, negociación de precios, presión política
sobre PBMs) que "más miembros asegurados = más utilidad de farmacia". Heurística transferible:
cuando una cifra de utilidad de un segmento se cita como prueba de que "el modelo funciona",
verificar primero si el volumen que la sostiene creció o se contrajo — utilidad que sube sobre
volumen que cae es una señal de mezcla de producto o poder de precio, no de demanda sana, y ese
tipo de crecimiento suele ser más frágil a shocks regulatorios específicos que el crecimiento
impulsado por más clientes.
- **Fuente:** F-198 (🟢A, UnitedHealth Group Inc. 2026, SEC Form 8-K, Q2 2026)
- **Leído a fondo:** 2026-08-17 (sec.gov y businesswire.com bloqueados por el proxy del entorno;
  reconstruido vía búsqueda dirigida — TradingView, StockTitan y 24/7 Wall St. confirman la cifra
  de scripts ajustados y su atribución explícita a mezcla de producto, no solo la cifra agregada
  ya citada)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 17 (sigue Alta en el patrón
  de EE.UU.) — matiza el mecanismo detrás del número: el motor de utilidad de farmacia es más
  resiliente a la pérdida de miembros de lo que sugiere el resumen agregado, pero ese mismo
  mecanismo (mezcla hacia especialidad) es una exposición distinta y no cubierta por la tesis tal
  como está escrita hoy.

### 34. El efecto "pie en la puerta" no necesita continuidad temática entre el pedido chico y el grande — la obligación de ser consistente se generaliza a un pedido no relacionado casi tan bien como a uno relacionado
Freedman & Fraser (1966, F-141 — base citada de la "divulgación progresiva" en tesis 13, nunca
leído más allá del resumen de una línea) corren dos experimentos, no uno. El primero (encuesta
telefónica → inventario de cocina en persona) ya está bien resumido en el ledger. El segundo —el
del cartel de "maneje con cuidado"— es el que aporta el matiz real: cuando el pedido chico previo
era del **mismo tema** (un cartel pequeño de seguridad vial), 76% aceptó el cartel grande dos
semanas después, contra apenas 17% de quien recibió el pedido grande directo, sin pedido chico
previo. Pero cuando el pedido chico era de un **tema no relacionado** (firmar una petición para
mantener bella California), el pedido grande de seguridad vial igual obtuvo 48% de aceptación —
menos que la condición temática, pero casi tres veces el nivel base de 17%. Heurística
transferible: el mecanismo de "pie en la puerta" no depende de que el segundo pedido continúe el
tema del primero — depende de que la persona ya se haya visto a sí misma como alguien que coopera
con quien pide. Eso es una oportunidad de secuenciación (un primer contacto de bajo compromiso en
cualquier tema puede ablandar el terreno para un pedido de datos más sensible después, no solo uno
del mismo formulario) y a la vez el límite ético más incómodo de tesis 13: si el mecanismo
funciona incluso sin relación temática, la línea entre "diseño de onboarding" y "manipulación de
consistencia" no la traza el contenido del pedido, la traza si el cliente entendería, si se lo
explicaran, por qué el segundo pedido llegó después del primero.
- **Fuente:** F-141 (🟢A, Freedman, J.L. & Fraser, S.C. 1966, *Journal of Personality and Social
  Psychology*)
- **Leído a fondo:** 2026-08-18 (bulidomics.com bloqueado por el proxy del entorno; reconstruido
  vía búsqueda dirigida — MIT (curhan.mit.edu), Quizlet y reseñas académicas del Experimento 2
  confirman los porcentajes por condición, no solo el resumen ya citado)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 13 (sigue Alta en el
  mecanismo) — agrega el dato de que el efecto sobrevive incluso sin continuidad temática entre
  pedidos, lo que amplía dónde aplica la advertencia ética ya declarada en esa tesis, no la crea.

### 35. Un incentivo financiero no compra cambio de conducta durable por sí solo — sin plan de mantenimiento explícito, el efecto se apaga en los primeros meses tras retirarlo
Vlaev et al. (2019, F-100 — ya citado en el ledger solo como "contrapeso independiente" a la
evidencia autopublicada de Discovery Vitality, F-99, nunca leído a fondo) da el detalle que el
resumen de una línea no traía: los efectos de un incentivo financiero sobre conducta de salud
tienden a **disiparse dentro de los tres meses posteriores a que se retira el incentivo**, salvo
que la conducta ya se haya vuelto hábito por otra vía. La revisión también precisa las cuatro
condiciones que hacen que un incentivo funcione mejor mientras está activo: que sea sustancial (no
simbólico), inmediato (no diferido), contextualizado al momento de la decisión, y medido con
seguimiento objetivo (no autorreportado). Heurística transferible, directa para cualquier diseño
tipo Vitality/telemática que `lapuerta` o Rimac evalúen: el incentivo no es el producto final, es
el puente hacia un hábito — si el plan de producto no tiene un mecanismo explícito para lo que pasa
cuando el incentivo se retira o se reduce (transición a refuerzo social, a feedback sin premio, a
identidad del usuario como "buen conductor/asegurado"), el caso de negocio que asume "el hábito
persiste" está asumiendo la parte que la evidencia independiente dice que es la que más falla.
Conecta directo con tesis 7 (UBI/telemática): el mecanismo validado ahí es feedback+incentivo, no
solo incentivo — esta fuente explica por qué esa combinación importa y no alcanza con el premio
solo.
- **Fuente:** F-100 (🟢A, Vlaev, I. et al. 2019, *BMC Public Health*, revisión desde economía
  conductual)
- **Leído a fondo:** 2026-08-18 (link.springer.com bloqueado por el proxy del entorno;
  reconstruido vía búsqueda dirigida — PubMed, ResearchGate y la revisión posterior de 2025 en
  *European Journal of Health Economics* confirman la ventana de disipación de ~3 meses y las
  cuatro condiciones de efectividad, no solo el resumen ya citado)
- **Conexión razonada, no forzada:** no cambia la confianza de ninguna tesis vigente (tesis 7 sigue
  Alta en que el producto funciona donde se adopta) — precisa el mecanismo de por qué tesis 7 exige
  feedback+incentivo y no incentivo puro, y da el número concreto (~3 meses) que faltaba para
  diseñar la fase de mantenimiento de cualquier programa de incentivos propio.

### 36. La usabilidad percibida de un chatbot comercial se mide en cinco palancas independientes de la calidad conversacional — dos de ellas (tiempo de respuesta, señal de privacidad) son más baratas de arreglar que "hacer el modelo más inteligente"
Borsci & Schmettow (2024, F-150 — citado en el ledger solo como "la escala más parecida al caso de
uso del agente de Rimac", nunca leído a fondo) re-validan el BUS-11 sobre 3.186 observaciones de 44
chatbots reales y confirman una estructura de cinco subescalas: **Accesibilidad, Calidad del
proceso de interacción, Calidad de la información, Privacidad y seguridad, y Tiempo de
respuesta**. El punto que el resumen de una línea no traía: solo dos de las cinco (calidad del
proceso de interacción y calidad de la información) dependen directamente de qué tan bien
razona/responde el modelo — las otras tres son percepción del usuario sobre variables de producto
que un equipo de ingeniería puede mover sin tocar el modelo conversacional en absoluto. Heurística
transferible para evaluar o mejorar el agente conversacional de Rimac (tema ya vigilado por
intuición 20 sobre RAGAS/LLM-as-judge y por el riesgo de medir mal al agente): si una evaluación de
usabilidad da puntaje bajo, la primera pregunta no debería ser "¿el modelo entiende peor de lo que
creíamos?" — debería ser "¿en cuál de las cinco palancas está el problema?", porque la respuesta
más barata y rápida de ejecutar (latencia de respuesta, señales visibles de manejo seguro de datos)
puede no tener nada que ver con la calidad del modelo que consume la mayor parte del presupuesto de
mejora.
- **Fuente:** F-150 (🟢A, Borsci, S. & Schmettow, M. 2024, *Personal and Ubiquitous Computing*)
- **Leído a fondo:** 2026-08-18 (dl.acm.org bloqueado por el proxy del entorno; reconstruido vía
  búsqueda dirigida — JMIR Human Factors 2026 y ResearchGate confirman los nombres de las cinco
  subescalas y el tamaño de muestra, no solo el resumen ya citado)
- **Conexión razonada, no forzada:** no cambia la confianza de ninguna tesis vigente (el agente
  conversacional de Rimac no tiene tesis propia todavía en este documento) — da un marco de
  diagnóstico concreto y citable para cuando el proyecto necesite evaluarlo, con las cinco palancas
  nombradas en vez de "usabilidad" genérica.

### 37. La desconfianza en un asegurador no siempre es un veredicto negativo ya formado — a veces es un vacío de información que todavía no permite juzgar
Estudio holandés (2025, F-334 — citado en el ledger solo por su hallazgo de una línea, "los
consumidores desconfían por conflicto financiero de interés", nunca leído a fondo) sobre el sistema
de competencia gestionada de Países Bajos, con metodología mixta (grupos focales + encuesta), da un
cuadro más matizado que el resumen: la mayoría de consumidores **sí sabe** que el asegurador compra
atención en su nombre y **sí cree** que esa tarea le corresponde, con una confianza "razonable
aunque frágil" en su competencia para comprarla bien — pero no tiene información suficiente para
formarse un juicio real sobre qué tan bien lo hace, y por default asume que el asegurador es una
organización puramente comercial. Heurística transferible: "desconfianza" en un asegurador no es un
solo fenómeno — hay que distinguir entre un veredicto negativo ya formado ("sé lo que hace y no me
gusta") y un vacío informativo ("no tengo con qué juzgar, así que asumo el peor marco por defecto").
Tesis 1 (divulgar mejor no convierte) habla de explicar el *producto*; esta fuente habla de un tipo
de información distinta — mostrar específicamente *cómo* el asegurador negocia/compra en nombre del
cliente — que podría mover una confianza "frágil" de un modo que un glosario de términos no logra,
porque el objetivo no es comprensión de cláusulas sino percepción de de qué lado está el asegurador.
Es hipótesis testeable, no dato peruano confirmado — no forzar como palanca probada.
- **Fuente:** F-334 (🟢A, *Health Economics, Policy and Law*, Cambridge, 2025 — autoría no
  especificada en el resumen del ledger)
- **Leído a fondo:** 2026-08-19 (cambridge.org bloqueado por el proxy del entorno; reconstruido vía
  búsqueda dirigida — resultado indexado por el propio buscador confirma metodología mixta focus
  groups+encuesta y los dos hallazgos centrales, no solo el resumen ya citado)
- **Conexión razonada, no forzada:** no cambia la confianza de ninguna tesis vigente — matiza tesis
  1 con una distinción de mecanismo (vacío informativo vs. juicio negativo) que el resumen de una
  línea no traía, aplicable al vacío §4.2 de reactancia por desvío del asegurador que ya cita el
  documento externo del usuario.

### 38. Las ganancias de esperanza de vida se están desacelerando en países de altos ingresos, sobre todo en los más viejos — no extrapolar la tendencia histórica de longevidad como lineal hacia adelante
Callaway, Strozza, Christensen et al. (BMC Public Health 2025, F-87 — citado en el ledger solo como
"mecanismo directo entre vivir más y siniestrarse más", nunca leído a fondo) analizan la Human
Mortality Database y el Global Burden of Disease y encuentran que, aunque la esperanza de vida
sigue subiendo en países de altos ingresos, el **ritmo de mejora se ha desacelerado**,
específicamente en los "oldest-old" (los de mayor edad) — y documentan el mecanismo detrás del
aumento de siniestralidad con la edad: mayor prevalencia de enfermedades crónicas, síndromes
geriátricos y multimorbilidad. Heurística transferible: cualquier supuesto actuarial o de producto
(vida, renta vitalicia, salud de largo plazo) que extrapole "la gente vive cada vez más" como
tendencia lineal indefinida corre el riesgo de sobreestimar el riesgo de longevidad a futuro si esa
desaceleración ya está en curso en el segmento de edad relevante — la pregunta correcta no es solo
"¿la esperanza de vida sube?" sino "¿a qué tasa, y esa tasa se está frenando en el tramo de edad que
me importa pricear?". Sin dato peruano en esta fuente (es de países de altos ingresos), pero es un
chequeo de higiene aplicable antes de fijar cualquier supuesto de mortalidad/longevidad a largo
plazo, y converge con la advertencia ya vigente de la intuición 17 sobre auditar qué variable queda
afuera de una fórmula, aplicada aquí a una tendencia temporal en vez de a una variable estática.
- **Fuente:** F-87 (🟢A, Callaway, J.; Strozza, C.; Christensen, K. et al. 2025, *BMC Public
  Health*, vol. 25, art. 4395)
- **Leído a fondo:** 2026-08-19 (link.springer.com bloqueado por el proxy del entorno; reconstruido
  vía búsqueda dirigida — ResearchGate y la propia indexación de Springer Nature confirman autoría,
  fuentes de datos y el hallazgo de desaceleración en oldest-old, no solo el resumen ya citado)
- **Conexión razonada, no forzada:** no cambia la confianza de ninguna tesis vigente (ninguna tesis
  de vida/longevidad tiene número propio todavía en este documento) — deja un chequeo de higiene
  actuarial documentado para cuando el proyecto sí necesite fijar un supuesto de mortalidad/
  longevidad de largo plazo.

### 39. Un beat de ingresos no neutraliza un indicador líder que empeora — cuando ambos divergen y hay una narrativa de disrupción estructural plausible, pesar el indicador líder, no el titular
Accenture reportó Q3 FY26 (F-428 — citado en el ledger solo por el hallazgo negativo de que Song no
se reporta como segmento separado, nunca leído a fondo el resto del caso) con ingresos de USD 18.7B
(+6% interanual) — un "beat" superficial — y aun así cayó ~18-20% en un solo día, su peor caída como
empresa pública, porque (a) recortó su guía de crecimiento a 3-4% (desde 3-5%) y (b) reportó una
caída de 2% en nuevos *bookings* — leído por analistas (Bloomberg Intelligence, TD Cowen recortando
su precio objetivo en más de USD 100) no como una narrativa temporal sino como evidencia de que la
IA generativa ya sustituye trabajo de consultoría facturable por hora. El propio hallazgo del F-428
del ledger completa el cuadro: Accenture no reporta a Song (su unidad creativa/CX, el tipo de
trabajo más fácil de automatizar) como segmento separado en sus filings SEC — la pregunta "¿esa
unidad crece o no?" es estructuralmente no verificable con datos públicos, mismo patrón de opacidad
que el node de innovación ya documentó en Adobe (F-306). Heurística doble: (1) un titular de
ingresos positivo no cierra el caso si el indicador líder (bookings, guía a futuro) se mueve en
sentido contrario — pesar el indicador líder, no el rezagado, cuando divergen; (2) cuando una
empresa de servicios profesionales deja de reportar por separado el segmento que más debería mostrar
sustitución por IA, la opacidad en sí misma es una señal, no un dato neutral que falta. Aplicación
directa: el mismo mecanismo de sustitución de trabajo facturable por hora que golpeó a la
consultoría de mayor prestigio del mundo es la amenaza estructural de largo plazo para cualquier
canal de asesoría humana en seguros — el argumento de tesis 16 ("el asesor no desaparece, se
redistribuye por complejidad") necesita vigilar activamente esta señal en vez de darla por sentada
indefinidamente, sobre todo para el trabajo de asesor más rutinario/facturable por hora, no el de
mayor complejidad de producto.
- **Fuente:** F-428 (🟢A, Accenture plc, filing 8-K/SEC, Q3 FY26, 18-jun-2026)
- **Leído a fondo:** 2026-08-19 (sec.gov bloqueado por proxy 403, ya señalado en el propio ledger;
  reconstruido vía búsqueda dirigida — Investing.com, Motley Fool, Yahoo Finance y cobertura de
  analistas confirman la caída de ~18-20% en un día, el recorte de guía, la caída de bookings y la
  narrativa de sustitución por IA, no solo el resumen ya citado)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 16 (sigue Alta en la dirección
  general) — agrega una señal de vigilancia activa específica (sustitución de trabajo facturable por
  IA en consultoría, con opacidad de reporte del segmento más expuesto) que la tesis, tal como está
  redactada, todavía no cubre explícitamente.

### 40. Al evaluar un agente conversacional, "¿entendió bien lo que dije?" puede pesar más en la satisfacción del usuario que "¿logró la tarea?" — medir ambos por separado, no solo el resultado final
PARADISE (Walker, Litman, Kamm & Abella 1997), el framework fundacional para evaluar diálogo
hablado que el ledger ya citaba como estándar de referencia (sección de escalas del agente
conversacional de Rimac), nunca se había leído a fondo más allá del resumen de una línea. Su
aporte real no es solo "modela satisfacción como éxito menos costo" — es que, al correr la
regresión sobre datos reales de un sistema en producción, el término que más pesó no fue el
éxito de tarea: fue el **reconocimiento correcto** de lo que dijo el usuario (Mean Recognition,
peso .45), por encima del éxito de tarea (.33) y por encima del costo de tiempo transcurrido
(-.14) — juntos explican ~55% de la varianza en satisfacción. **Heurística de decisión:** un
agente que completa la tarea pero que el usuario siente que "no lo entendió" en el camino puede
calificar peor que uno que tardó más pero demostró comprensión — separar en la medición del
agente de Rimac una métrica explícita de "¿el sistema entendió lo que quise decir?" de la métrica
de "¿resolvió mi caso?", en vez de inferir la primera de la segunda. Profundiza, desde un ángulo
distinto, el riesgo ya vigente sobre medir mal al agente conversacional de Rimac (intuición 8, 20,
21, 36): el eje que más mueve la aguja de satisfacción percibida puede no ser el que el equipo
técnico está optimizando.
- **Fuente:** F-147 (🟢A, Walker, Litman, Kamm & Abella 1997, *PARADISE: A Framework for
  Evaluating Spoken Dialogue Agents*, ACL — framework canónico, ya citado en el ledger solo por su
  resumen de una línea)
- **Leído a fondo:** 2026-08-20 (aclanthology.org bloqueado por el proxy del entorno; reconstruido
  vía búsqueda dirigida — incluyendo el paper de seguimiento "The PARADISE Evaluation Framework:
  Issues and Findings" — que confirma los pesos exactos de la regresión, no solo el mecanismo
  general ya citado)

### 41. El daño de una publicidad de precio incompleta o ambigua no se reparte parejo entre la audiencia — se concentra en quien ya desconfía, justo el segmento más caro de recuperar
Romani (2006), estudio experimental italiano sobre publicidad de precio engañosa que ya sostenía
el riesgo regulatorio/reputacional de tesis 15 solo por su resumen de una línea, tipifica ocho
prácticas distintas de comunicación de precio engañosa (desde información directamente falsa
hasta aplicación incompleta o confusa de esquemas de precio complejos — la categoría que más se
parece al caso Vida Ahorro del propio proyecto) y encuentra que la caída en confianza hacia la
fuente y en disposición a comprar **no es uniforme**: es significativamente mayor en
consumidores que ya llegan con sospecha ("suspicious") que en los que no. **Heurística de
decisión:** el costo de un flyer o pieza publicitaria con datos "a confirmar" visibles no se
puede estimar promediando la reacción del público general — hay que pesarlo por el segmento que
ya desconfía, porque es justo ahí donde el daño pega más fuerte. Conecta directamente con tesis 1
(~48% de peruanos desconfía del seguro, causa #1: falta de información) y tesis 15 (cifra %
headline + condición chica + dato "a confirmar" visible): la misma pieza que tesis 15 ya marcaba
como riesgo es, según este mecanismo, más cara precisamente en el segmento que el proyecto más
necesita convertir — no matiza la confianza de tesis 15 (sigue Alta), pero afina por qué el riesgo
no es solo regulatorio sino de conversión concentrada donde más duele.
- **Fuente:** F-176 (🟢A, Romani 2006, *Price misleading advertising: effects on trustworthiness
  toward the source of information and willingness to buy*, Journal of Product & Brand
  Management — ya citado en el ledger solo por su resumen de una línea)
- **Leído a fondo:** 2026-08-20 (researchgate.net bloqueado por el proxy del entorno; reconstruido
  vía búsqueda dirigida contra Emerald Publishing/DeepDyve/Scribd, que confirman la tipología de
  ocho prácticas y el moderador de sospecha, no solo el resumen ya citado)

### 42. La sobreconfianza en una respuesta de IA es una decisión estratégica de costo-beneficio, no un sesgo cognitivo automático — la inversión en explicabilidad rinde solo donde la tarea es difícil
Vasconcelos et al. (2023), ya citado en el node de tendencias-diseño-innovación para la regla C8
(verificabilidad > explicabilidad, intuición 18) solo por su resumen de una línea, corre 5
estudios (N=731) manipulando el costo y el beneficio de escrutinar una explicación de IA en una
tarea de laberinto. Hallazgo central: las explicaciones **sí** reducen la sobreconfianza y suben
la precisión de la decisión, pero **solo en la condición de tarea difícil** — en tareas fáciles o
medias no hay ninguna diferencia frente a mostrar solo la predicción sin explicación. Es decir, la
gente no ignora la explicación por pereza cognitiva generalizada: la ignora cuando el
costo-beneficio de leerla no vale la pena (tarea fácil, poco en juego), y la usa cuando sí vale
(tarea difícil). **Heurística de decisión:** invertir en explicabilidad de forma uniforme en todo
el flujo del agente conversacional o del triage IA es gastar donde no rinde — el retorno de
mostrar "por qué" el sistema recomendó algo se concentra en los momentos objetivamente más
difíciles de la interacción (síntomas atípicos, casos límite de cobertura), no en las respuestas
rutinarias. Profundiza directamente la intuición 18 (verificabilidad de la tarea) con el matiz de
que el *costo* de involucrarse con la explicación, no solo su *verificabilidad*, es la otra mitad
de la ecuación — y da un criterio operacional (dificultad de la tarea) para decidir dónde priorizar
el diseño de explicaciones primero.
- **Fuente:** F-246 (🟢A, Vasconcelos, H. et al. 2023, *Explanations Can Reduce Overreliance on AI
  Systems During Decision-Making*, PACM HCI 7, CSCW1, art. 129, N=731, 5 estudios — ya citado en
  el ledger solo por su resumen de una línea)
- **Leído a fondo:** 2026-08-20 (hci.stanford.edu bloqueado por el proxy del entorno; reconstruido
  vía búsqueda dirigida contra arXiv/ScholarSpace, que confirman el diseño de los 5 estudios y los
  pesos de costo/beneficio manipulados, no solo el resumen ya citado)
- **Conexión razonada, no forzada:** no cambia la confianza de ninguna tesis — profundiza el
  mecanismo detrás de la intuición 18 (misma familia de evidencia, ángulo distinto: costo de
  involucrarse, no solo verificabilidad del resultado).

### 43. Un combined ratio rentable auditado no es un estado alcanzado — es una versión de un modelo de riesgo que se sigue reentrenando, combinada con un cambio simultáneo de mezcla de canal hacia menor CAC
F-449 (Root, Inc., ya citado en tesis 25 solo por la cifra de combined ratio 91,4% del Q3 2025) da
el mecanismo detrás del número, no solo el resultado: Root lanzó en el mismo trimestre una versión
nueva de su modelo UBI que la propia gerencia estima ~10% más predictiva, entrenada sobre 36,000
millones de millas acumuladas de datos de manejo — y, en paralelo, el canal de partnerships
(seguro embebido en el punto de venta con socios como Hyundai Capital America) casi triplicó su
volumen interanual y ya representa 44% de las pólizas nuevas, un canal de adquisición
estructuralmente más barato que performance marketing directo. **Heurística de decisión:** cuando
se audite cualquier caso de "insurtech rentable" (el propio ejercicio que tesis 25 les exige a
labs internos como BCP CIX y Pacífico "La Cápsula"), no basta con verificar el combined ratio de
un trimestre — hay que verificar si la rentabilidad viene de una mejora de modelo que sigue
iterando (no de un ajuste de precio único ya agotado) y si coincide con una migración de mezcla de
canal hacia menor costo de adquisición al mismo tiempo; un número bueno sostenido por ambos motores
a la vez es una señal mucho más fuerte que el mismo número sostenido por uno solo.
- **Fuente:** F-449 (🟢A, Root Inc. — filings SEC 10-Q/10-K y shareholder letter Q3 2025, ya citado
  en el ledger y en tesis 25 solo por la cifra agregada de combined ratio)
- **Leído a fondo:** 2026-08-21 (ir.joinroot.com y sec.gov bloqueados por el proxy del entorno,
  mismo patrón ya documentado; reconstruido vía cobertura financiera especializada — StockTitan,
  Motley Fool, Globe and Mail — que confirma el detalle del modelo UBI v10%-más-predictivo y el
  mix de canal, no solo el resumen ya citado)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 25 (Alta, sin cambio) — le da
  el mecanismo causal que la tesis todavía no tenía explícito, y sirve como criterio de auditoría
  operacional para cuando algún lab peruano publique, si alguna vez lo hace, una cifra propia.

### 44. La divulgación pasiva ("explicar mejor") y el consejo digital activo (una herramienta que recomienda) no son el mismo objeto de estudio — uno no mueve la conducta, el otro sí, y por un mecanismo distinto al de informar
F-338 (Bundorf, Polyakova & Tai-Seale 2024, *Management Science*, RCT real en seguro de salud/
recetas, ya citado en el ledger solo por su hallazgo de WTP) separa dos canales por los que un
consejo digital puede cambiar una elección: **aprendizaje** (actualizar lo que el consumidor cree
sobre las características del producto) e **interpretación** (cambiar cuánto pesa cada
característica en su decisión, no solo lo que sabe de ella). El hallazgo más fuerte: el consejo
digital termina **desplazando** el peso que marca/reputación tenía sobre la disposición a pagar del
consumidor — no solo lo informa mejor sobre lo mismo que ya valoraba, le cambia la función de valor
misma. **Heurística de decisión:** esto no contradice la tesis 1 (glosarios/divulgación pasiva no
cambian conducta de compra) — la acota. La diferencia no es "más información vs. menos
información", es **pasivo vs. activo/recomendador**: un glosario deja al usuario decidir qué pesar
y cómo; una herramienta de consejo activa —que ordena, recomienda o resalta— cambia directamente
los pesos con los que el usuario decide, y por eso sí mueve la elección real. Cualquier
"comparador" o asistente de decisión que Rimac construya para `lapuerta` o para el canal digital
propio hereda esta distinción de diseño: un buscador/filtro pasivo no va a mover conducta (tesis
1); un motor que activamente recomienda y reordena sí puede, y con eso hereda también el riesgo
ético/regulatorio ya declarado en tesis 13 (mismo mecanismo que convierte mejor puede leerse como
manipulador si no se declara el criterio de recomendación).
- **Fuente:** F-338 (🟢A, Bundorf, M.K.; Polyakova, M.; Tai-Seale, M. 2024, *Management Science*
  70(11):7617-7643 — RCT real, ya citado en el ledger de un documento externo del usuario solo por
  la cifra de WTP)
- **Leído a fondo:** 2026-08-21 (pubsonline.informs.org de pago; reconstruido vía la versión
  working paper del NBER — "How do Humans Interact with Algorithms?" NBER WP 25976, mismos
  autores/hallazgo — y cobertura secundaria que confirma el mecanismo de dos canales, no solo el
  resumen ya citado)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 1 (Alta, sin cambio) — acota
  su alcance: "la divulgación no convierte" aplica a información pasiva, no a herramientas activas
  de recomendación, que son un objeto de diseño distinto con su propio mecanismo y su propio riesgo.

### 45. El efecto de framing (ganancia vs. pérdida) no tiene una magnitud fija que se pueda citar de memoria — se encoge o se invierte según el tiempo disponible para decidir y cuánto está en juego
El paper fundacional de Tversky & Kahneman (1981, ya citado en tesis 18/C.8 solo por su mecanismo
general) tiene una réplica de condiciones límite (Diederich & Wyszynski, *Judgment and Decision
Making* 2018) que mide el mismo "problema de la enfermedad asiática" cruzado con presión de tiempo
y magnitud de la necesidad (cuánta gente está en juego). Tres moderadores estadísticamente
significativos, más allá del frame mismo: (1) bajo **límite de tiempo corto**, el efecto de framing
se debilita en el marco de ganancia (la gente elige menos la opción segura de lo esperado cuando
tiene que decidir rápido); (2) el tamaño de la "necesidad" (cuánta gente afectada) invierte su
efecto según la enfermedad —para leucemia el framing pega más fuerte con necesidad alta, para SIDA
pega más fuerte con necesidad baja—, es decir el mismo frame no produce el mismo tamaño de efecto
en escenarios que a primera vista parecen equivalentes; (3) probabilidades más altas empujan hacia
más toma de riesgo en ambos frames. **Heurística de decisión:** citar "el framing funciona" como
si fuera una palanca de magnitud constante (el riesgo que corre cualquier aplicación directa de
C.5/C.8 del Playbook del Asesor a un guion de venta) es exactamente el mismo error que tesis 6 ya
identificó para el nudging genérico — el efecto promedio esconde variación real por contexto. Antes
de anclar un guion de venta a un frame de ganancia o pérdida, verificar bajo qué condición se va a
usar: una llamada bajo presión de tiempo (cierre rápido de fin de mes) no hereda automáticamente el
mismo tamaño de efecto que una decisión reposada de escritorio, y el "monto en juego" percibido
puede invertir cuál frame conviene más, no solo amplificarlo.
- **Fuente:** F-222 (🟢A, Tversky, A. & Kahneman, D. 1981, *Science* 211(4481) — ya citado en el
  ledger y en tesis 18 solo por su mecanismo general de framing); moderadores vía Diederich, A. &
  Wyszynski, C. (2018, *Journal of Judgment and Decision Making* 13(4), no registrada previamente
  en el ledger — no se suma como F-n nueva por ser hallazgo de contexto sobre una fuente ya citada,
  no evidencia independiente que sostenga una tesis nueva)
- **Leído a fondo:** 2026-08-21 (science.org de pago para el original; ambos reconstruidos vía
  agregadores — MPRA, Academia.edu, journal.sjdm.org de acceso abierto — que confirman el
  experimento del Asian Disease problem y los tres moderadores significativos)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 18 (Alta, sin cambio) — acota
  su alcance operacional: el mecanismo de framing (C.8) es real, pero su tamaño de efecto no es
  constante entre contextos de venta, y asumir que sí lo es repite el error de sobregeneralización
  que tesis 6 ya corrigió para el nudging.

### 46. El estudio fundacional de "choice overload" (las mermeladas) en realidad reporta tres efectos distintos bajo un solo titular — probabilidad de elegir, calidad del resultado y satisfacción no son la misma pregunta
Iyengar & Lepper (2000, *JPSP* 79:995-1006) es el origen citado de la narrativa "menos opciones
venden más" (F-119/F-120 ya documentan que el efecto agregado no replica de forma consistente —
intuición 31 lo acota vía los moderadores de Chernev). Leído completo, el paper en realidad son
tres experimentos empaquetados bajo un solo titular, no uno: (1) el estudio de las mermeladas
(6 vs. 24 sabores en un supermercado real) — 40% de conversión con 6 opciones vs. 3% con 24,
pero mide solo *probabilidad de compra*; (2) un estudio de ensayo universitario opcional (6 vs.
20/30 temas) — 74% de entrega con 6 opciones vs. 60% con más, y además los ensayos del grupo con
menos opciones fueron calificados de **mejor calidad**; (3) un estudio de chocolates con la misma
lógica de satisfacción posterior a la elección. **Heurística de decisión:** cuando un estudio
fundacional y muy citado se resume en una sola línea ("menos opciones convierte más"), verificar
si en realidad empaqueta varios outcomes distintos (¿elegir o no elegir?, ¿qué tan buena es la
elección?, ¿qué tan satisfecho queda?) bajo la misma narrativa — la réplica puede sostenerse en
uno de esos outcomes y fallar en otro, y citar el titular sin desagregar esconde justo esa
posibilidad. Aplicación directa: si `lapuerta` o un piloto propio prueban "menos planes de seguro
convierten mejor", medir por separado tasa de conversión, calidad de la elección (¿el cliente
terminó en el plan que más le convenía?) y satisfacción posterior — son tres apuestas empíricas
distintas, no una.
- **Fuente:** F-121 (🟢A, Iyengar, S. & Lepper, M. 2000, *Journal of Personality and Social
  Psychology* 79:995-1006 — el estudio original de choice overload, ya citado en el ledger solo
  por su resumen de una línea con la salvedad de no-replicación)
- **Leído a fondo:** 2026-08-22 (medium.com bloqueado por el proxy del entorno; reconstruido vía
  búsqueda dirigida contra Columbia Business School, ResearchGate, Quizlet y coberturas
  académicas que confirman los tres experimentos y sus cifras exactas, no solo el resumen del
  primero)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 12 (folklore de UX, Alta) —
  la acota con un matiz metodológico nuevo sobre cómo se mide el efecto, no sobre si existe.

### 47. Que un método con nombre propio muestre resultados reales no prueba que el método sea insustituible — si el efecto está mediado por un mecanismo genérico, cualquier práctica que active ese mismo mecanismo debería funcionar igual
El estudio de Roth, Globocnik, Rau & Neyer (2020, *Creativity and Innovation Management* 29(4),
N=160 en 62 proyectos de innovación con empresas — ya citado en `_nodes/tendencias-diseno-
innovacion.md` §2.1 solo por su hallazgo de mediación) muestra que el efecto de design thinking
sobre el éxito del proyecto está **totalmente mediado** por empoderamiento psicológico — no hay
efecto directo del método una vez que se controla por ese mecanismo. Leído completo, el paper
identifica los cuatro canales exactos de ese empoderamiento: (1) el contacto con usuarios reales
da sentido/motivación intrínseca; (2) resolver problemas complejos con herramientas nuevas da
experiencia de competencia; (3) la autonomía del equipo da sentido de ownership; (4) el proceso
iterativo permite ver impacto propio, lo que refuerza motivación. **Heurística de decisión:**
antes de justificar la adopción exclusiva de un framework con marca (design thinking, un método
de venta con nombre propio, un playbook con IP registrada) por sus resultados medidos, preguntar
si el efecto está mediado por un mecanismo genérico que el framework simplemente entrega mejor que
la alternativa actual — si es así, la decisión de negocio correcta no es "comprar/certificar ese
método específico" sino "diseñar cualquier práctica más barata que entregue el mismo mecanismo"
(contacto con el cliente real, autonomía del equipo, ver impacto rápido). Conecta con la intuición
15 (el efecto "estrella" de management depende de cómo se mide) desde un ángulo distinto: aquí el
riesgo no es la medición, es confundir el vehículo con el motor.
- **Fuente:** F-239 (🟢A, Roth, K.; Globocnik, D.; Rau, C.; Neyer, A.-K. 2020, *Creativity and
  Innovation Management* — ya citado en el ledger y en `_nodes/tendencias-diseno-innovacion.md`
  solo por su resumen de una línea)
- **Leído a fondo:** 2026-08-22 (onlinelibrary.wiley.com bloqueado por el proxy del entorno;
  reconstruido vía búsqueda dirigida contra ResearchGate y coberturas académicas que detallan los
  cuatro mecanismos de empoderamiento, no solo el resultado de mediación total)
- **Conexión razonada, no forzada:** no crea ni cambia tesis de negocio — matiza cómo evaluar
  cualquier framework con marca antes de comprarlo/adoptarlo para Rimac, sin tocar la confianza de
  tesis 21 (que ya cuestiona las cifras de ROI del diseño, no los mecanismos de mediación).

### 48. Un canal de atención puede puntuar igual o mejor en satisfacción del paciente/padre sin que eso diga nada sobre si el diagnóstico o el resultado clínico también fue igual o mejor
El estudio de Gotthardt, Haynes, Murphy & Marcin (2024, *Telemedicine and e-Health*, datos de UC
Davis Health ago-2020 a feb-2022 — ya citado en un documento externo del usuario solo por la cifra
agregada 94.9% video vs. 92.5% presencial) mide satisfacción de pacientes/padres pediátricos con
el instrumento estandarizado Press Ganey. Leído completo: el instrumento mide **experiencia
percibida con el proveedor** (accesibilidad, evaluación general del proveedor) — no mide precisión
diagnóstica, resultado clínico ni si el episodio requirió una visita presencial de seguimiento.
**Heurística de decisión:** un score de satisfacción tipo Press Ganey/CAHPS que favorece a
telesalud es evidencia real de que el canal se siente bien atendido — no es evidencia de que el
canal diagnosticó igual de bien. Esto no contradice el caso de negocio del canal barato (tesis 23
ya documenta que el steering ahorra costo real), pero sí exige separar, en cualquier gate de éxito
del piloto farmacia+triage IA (tesis 9/10), la métrica de satisfacción de servicio de la métrica de
calidad clínica — son dos instrumentos distintos que pueden moverse en direcciones opuestas, igual
que la intuición 8 ya documentó para agentes conversacionales (satisfacción subjetiva y desempeño
objetivo divergiendo por segmento) y la intuición 40 para PARADISE (reconocimiento pesa más que
éxito de tarea en la satisfacción declarada).
- **Fuente:** F-355 (🟢A, Gotthardt, C.J.; Haynes, S.C.; Murphy, R.K.; Marcin, P. 2024,
  *Telemedicine and e-Health* — ya citado en el ledger solo por la cifra agregada de comparación)
- **Leído a fondo:** 2026-08-22 (journals.sagepub.com bloqueado por el proxy del entorno;
  reconstruido vía búsqueda dirigida contra PubMed y coberturas académicas que confirman el diseño
  del estudio, la ventana temporal y qué mide exactamente el instrumento Press Ganey)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 9/10/23 (todas siguen Alta) —
  agrega un criterio de gate operacional que el piloto de farmacia+triage IA todavía no tenía
  explícito: exigir métrica clínica junto a la de satisfacción, no solo la segunda.

### 49. Un trigger paramétrico más preciso reduce el basis risk, pero no garantiza un contrato más eficiente — depende de si el residuo queda correlacionado con el índice
Louaas & Picard (2026, *The Geneva Risk and Insurance Review*) modelan el seguro paramétrico así:
el vector de parámetros públicamente observable produce un **índice de pérdida** (el valor esperado
condicional de la pérdida real), y el **basis risk** es la diferencia aleatoria entre la pérdida
real y ese índice. El resultado formal del paper, que el resumen de una línea citado en tesis 4 no
capturaba: una estructura de información más precisa (que reduce el *tamaño* del basis risk) **no
garantiza por sí sola** una cobertura más eficiente — depende de si el vector de parámetros y el
basis risk residual quedan **distribuidos independientemente** o no. Cuando el residuo queda
correlacionado con el índice observado, el diseño óptimo del contrato cambia y afinar el trigger
por sí solo no cierra la brecha de eficiencia.
**Heurística de decisión:** antes de vender "trigger más preciso = mejor producto paramétrico",
verificar si el basis risk residual del diseño propuesto es independiente del índice de pérdida —
si no lo es, la ganancia puede requerir rediseñar qué variables entran al índice, no solo medirlas
con más resolución. Transferible más allá de seguros paramétricos: cualquier "métrica proxy"
(screening, score de riesgo, índice de siniestralidad) enfrenta la misma pregunta — reducir el
ruido de la proxy no basta si el error residual está sistemáticamente correlacionado con lo que se
quiere medir, no solo disperso al azar.
- **Fuente:** F-164 (🟢A, Louaas & Picard 2026, *The Geneva Risk and Insurance Review* — ya citado
  en tesis 4 solo por el resumen "diseño óptimo de trigger")
- **Leído a fondo:** 2026-08-23 (arxiv.org y hal.science bloqueados por el proxy del entorno;
  reconstruido vía búsqueda dirigida — SSRN, ResearchGate, IDEAS/RePEc — que confirman el modelo
  formal: índice de pérdida = valor esperado condicional, basis risk = diferencia residual, y la
  condición de independencia como bisagra del resultado)
- **Conexión razonada, no forzada:** no baja la confianza de tesis 4 (sigue Alta en que el
  paramétrico es la jugada de producto correcta) — acota su alcance: la lectura de "cualquier
  trigger más preciso mejora el producto" no está sostenida por F-164 tal como se citaba; el
  criterio correcto es la independencia del residuo, no la precisión bruta del índice.

### 50. Antes de importar un marco teórico canónico para justificar un mecanismo de diseño, verificar si una teoría rival ya lo desplazó en una prueba empírica de cabeza a cabeza
Berger & Calabrese (1975) formulan la Teoría de Reducción de Incertidumbre (URT) con 7 axiomas y 21
teoremas: en interacciones iniciales las personas buscan reducir la incertidumbre sobre la otra
parte mediante estrategias de búsqueda de información (pasiva, activa, interactiva), porque la
incertidumbre genera estrés cognitivo aversivo. Es el marco que sostiene, en el node de material
visual (F-119 a F-127), por qué el material visual importa más en canal virtual que presencial —
sustituye señales no verbales ausentes en el contacto remoto. Leído a fondo: la propia disciplina de
comunicación interpersonal ya sometió URT a una prueba de cabeza a cabeza contra una teoría rival —
Predicted Outcome Value Theory (Sunnafrank, 1986, 1990) — y encontró que los axiomas/teoremas
originales de URT **no se sostienen** cuando se controla por Predicted Outcome Value: las personas
en interacciones iniciales no buscan reducir incertidumbre por sí misma, sino calcular el valor o
recompensa esperada de la relación, y abandonan la interacción cuando ese cálculo sale negativo
incluso con alta incertidumbre remanente.
**Heurística de decisión:** cuando un node importa una teoría canónica (por antigüedad y
peer-review) como marco explicativo de un mecanismo de negocio, buscar explícitamente si existe una
prueba de cabeza a cabeza posterior que la haya desplazado — no basta con que la teoría original sea
"seminal" o esté bien citada. Aplicado aquí: "el material visual reduce incertidumbre en canal
virtual" puede seguir siendo cierto en el resultado (más material visual → más conversión), pero el
mecanismo correcto a optimizar probablemente no es "dar más información para reducir incertidumbre"
sino "señalizar valor/recompensa esperada" — la misma distinción mecanismo-vs-resultado que ya
corrigió tesis 1 (divulgación no es lo mismo que persuasión), ahora aplicable también al material
visual de venta consultiva.
- **Fuente:** F-125 (🟢A, Berger & Calabrese 1975, *Human Communication Research* — ya citado en el
  node de material visual solo como encuadre teórico, sin verificar vigencia)
- **Leído a fondo:** 2026-08-23 (en.wikipedia.org, pressbooks.montgomerycollege.edu y
  onlinelibrary.wiley.com bloqueados por el proxy del entorno; reconstruido vía búsqueda dirigida
  contra iResearchNet, Businesstopia, Communication Theory.org, ERIC y el resumen del propio estudio
  de Sunnafrank 1990 que reporta el resultado del test de cabeza a cabeza)
- **Conexión razonada, no forzada:** ninguna de las 25 tesis cita F-125 por número (vive en el node
  `material-visual-venta-consultiva.md`, no en el corpus de tesis) — el matiz queda registrado como
  heurística transferible a cualquier lectura futura de ese node o de otros que importen un
  framework teórico sin chequear su estado de vigencia empírica.

### 51. El efecto ancla de una cifra headline no golpea parejo a toda la audiencia — se concentra en quien decide bajo presión de tiempo, baja confianza o menos conocimiento
Zong & Guo (2022, *Frontiers in Psychology*, PMC8860899) corren un experimento donde sujetos
juzgan/estiman precios de un producto tras experimentarlo, bajo condiciones de ancla externa
(alta/baja) e interna, midiendo el efecto con un índice de anclaje (AI) y un índice de sesgo medio.
Confirman el efecto ancla base (ya citado en tesis 15 por su resumen), pero el hallazgo que ese
resumen de una línea no capturaba: el efecto **no es uniforme** — presión de tiempo y nivel de
autoconfianza del consumidor lo modulan, y bajo condición de ancla externa, género, personalidad,
conocimiento y habilidad también influyen de forma significativa.
**Heurística de decisión:** cuando una pieza de venta usa una cifra headline como ancla (el caso
"170%"/"200%" de tesis 15), el riesgo regulatorio y el efecto persuasivo no se distribuyen parejo en
la audiencia — se concentran en el segmento que decide con más presión de tiempo, menos confianza en
su propio juicio y menos conocimiento del producto. Es la misma lógica de concentración que ya
aplicó la intuición 41 (el daño de una publicidad de precio ambigua se concentra en quien ya
desconfía): aquí el eje de concentración es tiempo/confianza/conocimiento, no confianza previa en el
asegurador. Para cualquier pieza con cifra ancla, el segmento más vulnerable al efecto — y más
expuesto si Indecopi audita el material — es el que decide rápido y sabe menos: exactamente el
segmento que un canal de venta consultiva bien diseñado debería proteger primero, no el que más
fácil convierte.
- **Fuente:** F-175 (🟢A, Zong & Guo 2022, *Frontiers in Psychology*/PMC — ya citado en tesis 15
  solo por el resumen del efecto base)
- **Leído a fondo:** 2026-08-23 (ncbi.nlm.nih.gov y frontiersin.org bloqueados por el proxy del
  entorno; reconstruido vía búsqueda dirigida contra ResearchGate, PhilPapers y el registro del
  propio estudio en Frontiers que confirman el diseño experimental — ancla externa alta/baja e
  interna, índice de anclaje AI — y los moderadores exactos: tiempo, autoconfianza, género,
  personalidad, conocimiento, habilidad)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 15 (sigue con el mismo tope que
  ya tenía) — añade el criterio de segmentación de riesgo/efecto que la tesis todavía no tenía
  explícito.

### 52. Un efecto nulo de divulgación que es parejo entre segmentos (no concentrado en ninguno) es él mismo diagnóstico: descarta "hace falta segmentar mejor" como arreglo
F-9 (Adams, Hunt, Palmer & Zaliauskas 2021, RCT de campo N≈124,000 en 5 depositarios del Reino
Unido) ya sostenía tesis 1 solo por el resultado agregado y el mecanismo de creencias pesimistas
(revisión profunda de `cronista`, 2026-07-21). La lectura a fondo del Lobo agrega un dato que ese
resumen no traía: el fracaso de la divulgación es prácticamente uniforme por edad y por saldo —solo
evidencia débil de heterogeneidad individual— incluso en el brazo de tratamiento más fuerte, donde
un producto alternativo del **mismo** proveedor dominaba estrictamente al producto actual del
consumidor.
**Heurística de decisión:** cuando un experimento de divulgación/comunicación falla parejo en todos
los segmentos observables, la corrección correcta no es "afinar el targeting" (edad, saldo, perfil)
— es intervenir sobre la creencia previa, no sobre el formato o el destinatario. Aplica directo a
cualquier propuesta de "glosario para millennials" o "explicador para NSE C/D" en el proyecto: si el
fracaso de tesis 1 es de naturaleza pareja como en F-9, personalizar el mensaje por segmento hereda
el mismo techo bajo, no lo levanta.
- **Fuente:** F-9 (🟢A, Adams, Hunt, Palmer & Zaliauskas 2021, *Journal of Financial Economics* — ya
  citada en tesis 1, con revisión profunda de `cronista` el 2026-07-21 sobre el mecanismo; esta es
  la primera lectura a fondo del propio Lobo)
- **Leído a fondo:** 2026-08-24 (sciencedirect.com, nber.org y web.mit.edu bloqueados por el proxy
  del entorno; reconstruido vía búsqueda dirigida — NBER WP 25718, resumen de J-PAL, EconPapers —
  que confirman el diseño de brazos múltiples, incluyendo el brazo con dominancia estricta del
  producto alternativo, y la uniformidad del efecto nulo por edad/saldo)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 1 (sigue Alta) — añade el
  criterio operacional de por qué "mejorar el formato/segmentación de la divulgación" no es la
  palanca correcta, con un detalle de uniformidad que la revisión profunda de `cronista` no había
  registrado.

### 53. Un sistema de triaje/gatekeeping puede fallar en dos direcciones simétricas (sobre-cautela costosa, sobre-confianza peligrosa) — medir solo el ahorro de costo esconde la segunda
F-329 (examiner design, línea de asesoría de enfermería de la VA) ya sostenía la brecha empírica del
vacío §4.2 del documento externo del usuario solo por la cifra agregada de ahorro (-US$404 vs. ED,
-US$247 vs. atención primaria a 28 días). La lectura a fondo agrega el marco del propio estudio: la
identificación causal explota la variación cuasi-aleatoria **entre enfermeras** (asignación a la
siguiente disponible), precisamente porque unas triajean demasiado defensivamente (sobre-refieren a
emergencias, encareciendo el sistema) y otras demasiado optimistamente (sub-refieren, retrasando
atención crítica) — el diseño existe para separar ambos tipos de error, no solo para medir el ahorro
promedio.
**Heurística de decisión:** cualquier evaluación de un triage con IA (farmacia+IA, tesis 10) que
reporte solo "cuánto costo evita" sin reportar también la tasa del error simétrico (cuántos casos que
debían escalar no escalaron) está midiendo la mitad del riesgo real. El criterio de éxito correcto
necesita las dos colas, no una sola cifra de ahorro — el mismo error que tesis 10 ya identificó en
Babylon (falta de separación seguridad vs. coincidencia exacta) reaparece aquí en otra variable:
ahorro de costo vs. tasa de sub-triage peligroso son ejes distintos, y el segundo es el que decide si
el producto es seguro, no solo si es rentable.
- **Fuente:** F-329 (🟢A, examiner design, *Journal of Health Economics* — autoría no confirmada por
  bloqueo del PDF, ya citada en documento externo del usuario solo por la cifra agregada)
- **Leído a fondo:** 2026-08-24 (sciencedirect.com bloqueado por el proxy del entorno; reconstruido
  vía búsqueda dirigida que confirma el diseño de examiner/asignación cuasi-aleatoria y el marco de
  error simétrico entre enfermeras defensivas y optimistas)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 10 (sigue Alta) — refuerza con
  evidencia de otro dominio (triaje humano, no IA) el mismo principio de gate de aprobación que tesis
  10 ya exige para el piloto farmacia+IA: medir el error de sub-triage por separado, no solo el
  ahorro.

### 54. Existe un instrumento validado y corto (11 ítems, <10 min) para medir confianza en un asegurador por sus cuatro componentes — no hace falta inventar una pregunta de encuesta ad hoc
F-335 (HITS, Zheng et al. 2002) ya estaba citada como "pista empírica" en el documento externo del
usuario solo por sus cuatro dimensiones (fidelidad, competencia, honestidad, confidencialidad). La
lectura a fondo agrega el dato operacional que el resumen no traía: la escala final tiene 11 ítems
autoadministrados, toma menos de 10 minutos, y fue validada dos veces —muestra nacional aleatoria
(n=410) y muestra regional de una HMO (n=1,152)— con confiabilidad alta (alfa 0.91-0.95 según versión
larga/corta). Confirma también el vínculo conductual: menor confianza se asocia a mayor probabilidad
de decir que cambiaría de plan, no solo a una actitud declarada.
**Heurística de decisión:** cuando el proyecto necesite medir "confianza en el asegurador" (tesis 1,
`glosario-seguro-salud-peru.md`, o cualquier encuesta a usuarios sintéticos/reales de `lapuerta`),
usar o adaptar HITS en vez de una pregunta única tipo "¿confía en su aseguradora? sí/no" — el
instrumento ya viene validado en las cuatro dimensiones que separan por qué alguien desconfía (¿no
cree que cuiden su interés? ¿no cree que sean competentes? ¿cree que mienten? ¿teme el mal uso de sus
datos?), lo cual es información accionable de producto que un solo ítem agregado no da.
- **Fuente:** F-335 (🟢A, Zheng, Hall, Dugan, Kidd & Levine 2002, *Health Services Research* — ya
  citada solo por sus cuatro componentes)
- **Leído a fondo:** 2026-08-24 (pmc.ncbi.nlm.nih.gov bloqueado por el proxy del entorno;
  reconstruido vía búsqueda dirigida que confirma la escala final de 11 ítems, las dos muestras de
  validación y el vínculo con intención de cambio de plan)
- **Conexión razonada, no forzada:** ninguna de las 25 tesis cita F-335 por número — el matiz queda
  registrado como herramienta operacional transferible a cualquier medición futura de "confianza" en
  el proyecto, sin forzar una tesis de negocio nueva.

### 55. Un estudio correlacional de "diseño causa mejor desempeño" merece menos descuento cuando la comparación ya está hecha dentro de la misma industria — no cruzándolas
F-237 (Hertenstein, Platt & Veryzer 2005) ya estaba citada en el node de diseño solo como "evidencia
base del vínculo diseño→desempeño de firma", con la advertencia genérica de que es correlacional y
puede sufrir halo (la variable independiente es percepción experta). La lectura a fondo agrega el
detalle metodológico que el resumen corto no traía: el panel de 138 expertos en diseño industrial no
comparó firmas de industrias distintas entre sí — clasificó "alto" vs. "bajo" diseño efectivo DENTRO
de cada una de las nueve industrias manufactureras estudiadas, y solo entonces comparó desempeño
financiero (ROA, ROS, crecimiento de ventas) entre los dos grupos de cada industria. Eso neutraliza
de entrada el confusor más obvio de cualquier comparación cruda entre sectores (viento de cola
sectorial, ciclo de commodity, intensidad de capital) antes de llegar al dato.
**Heurística de decisión:** antes de descontar un hallazgo "solo por ser correlacional", verificar si
el diseño de la comparación ya controló el confusor más evidente (aquí, la industria). Cuando ya lo
hizo, el descuento de confianza debe ser menor que el que aplicaría el mismo lector a una comparación
cruda sin ese control — "correlacional" no es una etiqueta binaria de calidad; hay grados según qué ya
viene controlado por el propio diseño del estudio, y confundir ambos lleva a descartar evidencia que
en realidad ya hizo parte del trabajo de descarte de confusores por uno.
- **Fuente:** F-237 (🟢A, Hertenstein, Platt & Veryzer 2005, *Journal of Product Innovation
  Management* — ya citada en el node de diseño solo como evidencia base del vínculo diseño→desempeño)
- **Leído a fondo:** 2026-08-25 (onlinelibrary.wiley.com bloqueado por el proxy del entorno;
  reconstruido vía ResearchGate y cobertura académica que confirma el panel de 138 expertos, las
  nueve industrias y la comparación intra-industria)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 21 (sigue Alta) — matiza el
  criterio con el que debe leerse una de las piezas de evidencia base que la sostiene: el estudio
  fundacional del vínculo diseño→negocio merece menos descuento del que su etiqueta genérica de
  "correlacional" sugiere a primera lectura.

### 56. Un efecto directo y un efecto moderador sobre el mismo resultado no se leen igual — el segundo solo se cobra si la otra variable ya está presente en cantidad
F-238 ya estaba citada en el node de diseño como "la mejor evidencia disponible del vínculo
diseño→negocio" y como sustento de la fila 🟢 de la escala de madurez de evidencia, con el resumen
genérico de "efecto directo + efecto moderador". La lectura a fondo (vía cobertura académica y
ResearchGate, dado el bloqueo del DOI) agrega el mecanismo: sobre un panel GLS de 1,659 firmas
públicas de EE.UU. (1980-2015), usando patentes de diseño+utilidad como proxy objetivo de "capacidad
de diseño-ingeniería" (no percepción de expertos, a diferencia de F-237), el estudio encuentra que esa
capacidad (a) mejora el desempeño financiero de forma directa, y (b) por separado, amplifica cuánto
retorno financiero produce la actividad de innovación de la firma — dos efectos que se acumulan de
forma distinta, no un solo coeficiente que se pueda citar como "el diseño vale X%".
**Heurística de decisión:** al leer que una capacidad "X mejora el desempeño Y y además amplifica el
retorno de la actividad Z", separar las dos preguntas antes de decidir si invertir en X: (1) ¿cuánto
vale el efecto directo por sí solo? y (2) ¿cuánta actividad Z ya existe en la organización para que el
efecto moderador tenga algo que amplificar? Invertir en capacidad de diseño rinde poco en una
organización que casi no innova, y mucho en una que ya invierte fuerte en I+D sin capturar retorno
completo — el diagnóstico correcto no es "¿vale la pena el diseño?" sino "¿cuánta innovación tenemos
ya para que el diseño amplifique?".
- **Fuente:** F-238 (🟢A, autoría no verificada por bloqueo de acceso, revista *Innovation:
  Organization & Management* 2025 — ya citada en el node de diseño como "la mejor evidencia
  disponible" y sustento de la escala de madurez §5)
- **Leído a fondo:** 2026-08-25 (tandfonline.com bloqueado por el proxy del entorno; reconstruido vía
  cobertura académica y ResearchGate que confirma la muestra de 1,659 firmas, el proxy de patentes
  1980-2015 y la distinción entre efecto directo y efecto moderador)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 21 (sigue Alta) — agrega el
  mecanismo preciso (efecto directo vs. moderador condicionado a innovación ya existente) que el
  resumen corto del node no distinguía, útil si el proyecto necesita argumentar el ROI de diseño ante
  una organización que ya invierte en I+D frente a una que no.

### 57. Cuando el contrato de un intermediario paga más cuanto más deniega, la pregunta de auditoría correcta no es "¿es imparcial?" sino "¿qué palanca operativa tiene para mover su propio resultado sin que el cliente lo note?"
F-349 (investigación ProPublica/Capitol Forum sobre EviCore) ya estaba citada en un documento externo
del usuario solo por la narrativa general de conflicto de interés en el steering algorítmico
(refuerzo de tesis 23). La lectura a fondo agrega el mecanismo operativo exacto: EviCore (de propiedad
de Cigna/Evernorth) gestiona autorizaciones previas para más de 100 aseguradoras que cubren ~100
millones de personas (incluyendo UnitedHealthcare, Aetna y BCBS), con contratos que en algunos casos
pagan MÁS cuanto mayor es el ahorro logrado por denegación — un incentivo económico directo, no un
efecto secundario. Ex-empleados declararon a ProPublica que la empresa ajusta el algoritmo interno
("the dial") específicamente cuando no está generando "suficiente ahorro" para justificar su valor
ante el cliente asegurador — sin que el asegurador lo sepa. En Arkansas (2021), la tasa de denegación
de autorizaciones llegó a 20%, casi el triple de la tasa normal en Medicare Advantage.
**Heurística de decisión:** frente a cualquier intermediario algorítmico (de triaje, de precio, de
aprobación) cuyo contrato con el principal esté atado a una métrica que el intermediario mismo
controla y reporta, la auditoría correcta no pregunta "¿el intermediario actúa de buena fe?" sino
"¿qué parámetro interno tiene autoridad para mover sin que el principal se entere, y qué tan seguido
lo mueve?" — la garantía de imparcialidad no puede depender de la ética declarada del vendor cuando su
propio modelo de ingresos premia mover ese parámetro en una sola dirección. Aplica directo al gate de
gobernanza que tesis 10 ya exige para cualquier sistema de triaje/aprobación con IA: el gate debe
auditar quién tiene el "dial" y con qué frecuencia se toca, no solo la tasa de precisión clínica
declarada.
- **Fuente:** F-349 (🟢A, ProPublica/Capitol Forum 2023-2024 — ya citada en documento externo del
  usuario solo por la narrativa general de conflicto de interés que refuerza tesis 23)
- **Leído a fondo:** 2026-08-25 (vía búsqueda dirigida — cobertura directa de ProPublica y
  reproducciones especializadas en salud, ya que el ledger no registraba una URL directa al reportaje)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 10 ni 23 (siguen su nivel Alta
  vigente) — agrega a tesis 10 un criterio de auditoría concreto (quién controla el "dial" del
  algoritmo y con qué frecuencia se ajusta) que su gate de validación clínica no cubría todavía, y a
  tesis 23 un ejemplo documentado con evidencia dura de que el steering algorítmico en salud sí tiene
  incentivo financiero directo detrás, no solo riesgo reputacional percibido.

### 58. Para validar la seguridad de un triage automatizado, el muestreo de casos reales no basta — hay que inyectar a propósito los casos raros/agudos que ese muestreo casi nunca va a capturar
F-42 (los resultados de la validación de Omaolo — 97.6% seguro, 53.7% de coincidencia exacta con
enfermería sobre 877 evaluaciones reales) ya sostenía buena parte de tesis 10. F-63 es el protocolo
metodológico *detrás* de esos números, no otro dataset: describe cómo Finlandia diseñó la validación
clínica de Omaolo (dispositivo médico certificado, marcado CE clase IIa, construido sobre el motor de
soporte de decisión clínica Duodecim/EBMEDS) como un estudio mixto (cuantitativo + cualitativo). El
detalle que el resumen de una línea no traía: el protocolo complementa los casos reales de atención
primaria con **viñetas clínicas construidas a propósito** para los escenarios raros y agudos que un
muestreo real, por más grande que sea, casi nunca va a capturar en la ventana de la validación —
cada viñeta prueba un nivel de triage distinto con un caso estandarizado. Es decir: el 97.6% de
seguridad de F-42 no midió *solo* lo que llegó por la puerta durante el estudio; lo blindó contra el
sesgo de que "no vimos ningún caso agudo mal triado" solo signifique que la muestra fue chica, no que
el sistema sea seguro con ellos.
**Heurística de decisión:** al diseñar (o exigir) la validación de cualquier sistema de triage
automatizado —salud, seguros, soporte al cliente—, no aceptar como prueba de seguridad solo la tasa
de acierto sobre el flujo real de casos: la cola de eventos raros y de alto costo es, por definición,
la que menos aparece en cualquier ventana de muestreo real, y es la que más importa. Exigir que el
protocolo incluya un set construido a propósito de casos raros/límite, no solo una muestra pasiva más
grande. Aplica directo al gate de aprobación del piloto farmacia+IA que tesis 9 y 10 ya describen: el
criterio de "correr en silent trial 60-90 días" (tesis 10) mide bien el flujo real, pero necesita este
complemento de viñetas para no dejar un punto ciego en los casos agudos poco frecuentes.
- **Fuente:** F-63 (🟢A, protocolo de validación mixto peer-reviewed, JMIR Research Protocols 2023 —
  ya citada en `research/_nodes/modelo-salud-ia-farmacias-peru.md` como plantilla de diseño de
  validación clínica)
- **Leído a fondo:** 2026-08-26 (ncbi.nlm.nih.gov y researchprotocols.org bloqueados por el proxy del
  entorno; reconstruido vía cobertura de búsqueda dirigida que confirma el diseño mixto, el estatus de
  dispositivo médico certificado del symptom-checker y el rol específico de las viñetas clínicas para
  cubrir casos raros/agudos)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 10 (sigue Alta) — precisa el
  *cómo* detrás del contraejemplo positivo (F-42) que la sostiene, y agrega a tesis 9/10 un requisito
  concreto de diseño de validación (viñetas para la cola rara) que el node de salud puede exigir al
  evaluar cualquier proveedor de triage IA para el piloto farmacia+IA.

### 59. La misma pieza creativa puede estar moviendo la métrica equivocada — informativo y emocional no compiten por el mismo objetivo, y el ganador cambia con el tier de precio del producto
F-178 ya estaba citada para matizar la elección entre imagen aspiracional (emocional) y bullets de
beneficios (informativo) en material de venta: "ambos cumplen función distinta, no hay que elegir
uno". La lectura a fondo (Guitart & Stremersch 2021, +2,000 comerciales de TV de 144 modelos de auto
a lo largo de 4 años) precisa que la función distinta no es solo "informar vs. emocionar" en
abstracto — es una interacción con el tier de precio del producto, cruzada con el objetivo de negocio:
subir el contenido **emocional** aumenta la **búsqueda online**, pero subir el contenido
**informativo** no mueve la búsqueda. Y en ventas incrementales, el contenido informativo rinde más en
productos de precio/calidad **bajos**, mientras el emocional rinde más en productos de precio/calidad
**altos**. Un anunciante de producto caro que optimiza su creatividad para "generar más búsqueda"
(típicamente contenido emocional) puede estar, sin darse cuenta, dejando sobre la mesa ventas
incrementales que el contenido informativo sí habría capturado — y viceversa para un producto barato.
**Heurística de decisión:** antes de elegir la mezcla informativo/emocional de cualquier pieza (flyer,
video, landing), primero fijar cuál es el objetivo real de esa pieza específica —¿generar
consideración/búsqueda o cerrar venta directa?— y solo después decidir la mezcla según el tier de
precio del producto que se está vendiendo. Tratar "informativo vs. emocional" como una sola decisión
de estilo, sin separar objetivo de búsqueda vs. objetivo de venta, arriesga optimizar la pieza para la
métrica que no es la que el negocio necesita en esa etapa del funnel.
- **Fuente:** F-178 (🟢A, peer-reviewed, *Journal of Marketing Research* 2021 — ya citada vía
  `/trinidad` 2026-07-21 sobre material visual de venta consultiva)
- **Leído a fondo:** 2026-08-26 (journals.sagepub.com bloqueado por el proxy del entorno;
  reconstruido vía cobertura académica — JSTOR, Erasmus University Rotterdam, Semantic Scholar — que
  confirma el diseño (2,000+ comerciales, 144 modelos, 4 años), la asimetría por tier de precio en
  ventas incrementales y que solo el contenido emocional, no el informativo, mueve la búsqueda online)
- **Conexión razonada, no forzada:** no cambia la confianza de la conexión ya registrada en el node de
  material visual de venta consultiva — la precisa: la mezcla informativo/emocional recomendada debe
  condicionarse al tier de precio del producto de seguro (p. ej. SOAT/microseguro barato vs. vida/salud
  premium) y al objetivo de la pieza (consideración vs. cierre), no aplicarse igual a todo el catálogo.

### 60. Una palanca de precio/tiering para "reordenar" a dónde va el paciente/cliente solo muerde en el momento de elegir por primera vez — no cuando ya existe una relación establecida
F-340 ya estaba citada solo por el resultado agregado: inscribirse en un plan con red por niveles
redujo el gasto médico ajustado en 5% (Massachusetts, 2008-12), con reducciones similares en
ambulatorio y en radiología ambulatoria. La lectura a fondo agrega el límite del mecanismo que el
resumen agregado no mostraba: literatura relacionada de los mismos autores/tema (Sinaiko & Rosenthal)
encuentra que el tiering de proveedores por precio **solo es efectivo para dirigir a pacientes nuevos
que todavía no tienen una relación establecida con un médico** — no rompe relaciones ya existentes, y
el efecto de "castigar" a proveedores mal rankeados con menor market share se concentra
desproporcionadamente en pacientes nuevos, más viejos/enfermos o de ciertos perfiles demográficos, no
se reparte parejo. El 5% de ahorro agregado de F-340, entonces, probablemente no viene de que todo el
padrón se reacomodó hacia proveedores baratos — viene de que el flujo de inscripciones/derivaciones
*nuevas* sí respondió al incentivo de precio, mientras el resto de la base siguió como estaba.
**Heurística de decisión:** al diseñar cualquier palanca de precio/tiering para dirigir a un cliente
hacia un proveedor, canal o producto más eficiente (farmacia vs. consulta presencial, asesor digital
vs. presencial, plan A vs. B), no proyectar el ahorro esperado sobre toda la base de clientes actuales
— proyectarlo sobre el flujo de decisiones *nuevas* (altas, primera consulta, renovación con cambio de
plan), que es donde la palanca realmente opera. Si el objetivo de negocio requiere mover también a
quien ya tiene una relación establecida, el tiering de precio por sí solo no alcanza; hace falta una
palanca adicional dirigida específicamente a esa relación existente.
- **Fuente:** F-340 (🟢A, peer-reviewed/cuasi-experimental, *Health Affairs* 2017 — ya citada en
  documento externo del usuario sobre steering de proveedor/tier)
- **Leído a fondo:** 2026-08-26 (healthaffairs.org y commonwealthfund.org bloqueados por el proxy del
  entorno; reconstruido vía cobertura del mismo hallazgo — PubMed, Commonwealth Fund — y vía literatura
  relacionada de los mismos autores sobre los límites del tiering en pacientes con relación médica ya
  establecida)
- **Conexión razonada, no forzada:** no cambia la confianza de la conexión ya registrada (steering de
  proveedor/tier) — acota su alcance: el ahorro de 5% de F-340 debe leerse como efecto sobre el flujo
  de decisiones nuevas, no como una reasignación general de la base, matiz útil si el proyecto llega a
  diseñar una palanca de tiering/derivación (farmacia-frente-primario, tesis 9) esperando que reordene
  también relaciones de atención ya existentes.

### 61. La importancia de un atributo no dice dónde invertir — el desempeño actual sí: separar ambas antes de priorizar un rediseño de canal digital
F-154 ya estaba citado solo como "metodológicamente más sofisticado que un cuestionario simple". La
lectura a fondo (árbol de decisión + random forest + XGBoost, R² hasta ~95% con los métodos de
ensamble, sobre un modelo de aceptación de chatbot de aseguradora con cuatro predictores: expectativa
de desempeño, expectativa de esfuerzo, influencia social y confianza) agrega el hallazgo operacional
real: el Importance-Performance Map Analysis (IPMA) no pregunta solo "¿qué predictor importa más?" —
cruza importancia con desempeño actual, y el resultado es que lo urgente de mejorar en este estudio no
es la utilidad percibida del chatbot (expectativa de desempeño, que ya rinde bien), sino influencia
social, confianza y expectativa de esfuerzo — los tres atributos más relacionales/blandos, no
funcionales.
**Heurística de decisión:** antes de invertir en rediseñar cualquier canal digital (chatbot, app,
cotizador), medir importancia Y desempeño de cada atributo por separado — no solo cuál correlaciona más
con la intención de uso. El atributo más importante puede ya estar rindiendo bien (no necesita
inversión); el que peor rinde puede no ser el más importante (baja prioridad). El cuadrante que sí
justifica inversión es importancia-alta + desempeño-bajo, y en este estudio de seguros ese cuadrante lo
ocupan confianza e influencia social, no la utilidad percibida del bot.
- **Fuente:** F-154 (🟢A, peer-reviewed, MDPI *Electronics* 2025)
- **Leído a fondo:** 2026-08-27 (mdpi.com bloqueado por el proxy del entorno; reconstruido vía
  ResearchGate y búsqueda dirigida sobre IPMA aplicado a chatbots de seguros, que confirma la
  metodología de los tres modelos ML, el R² por método y los tres atributos priorizados por el
  cuadrante importancia-alta/desempeño-bajo)
- **Conexión razonada, no forzada:** no hay tesis numerada de chatbot puro todavía — conecta con tesis
  9/10/23 (canal digital, farmacia+triage IA, steering hacia canal barato) y con el Playbook del Asesor
  (tesis 18): si el proyecto invierte en un chatbot/asistente de seguros, el criterio de dónde poner el
  presupuesto de mejora debería ser este cuadrante IPMA, no una encuesta de satisfacción general.

### 62. El ahorro de un modelo de atención primaria alternativo depende de si cambia el incentivo del proveedor, no del canal de acceso
F-108 ya estaba citado solo por la cifra agregada (ahorro asociado a menos visitas a emergencias/
hospitalizaciones). La lectura a fondo (Tecco, Rahim, Lalwani & Palakodeti 2024, *JGIM*) precisa el
mecanismo: Direct Primary Care reemplaza el pago por transacción (fee-for-service) por una membresía
fija mensual (USD 50-150) — lo que cambia el incentivo del médico de "maximizar el número de consultas
cortas" a "resolver bien en la consulta para evitar una derivación cara aguas abajo". Las visitas duran
30-60 minutos (vs. 12-15 en atención primaria tradicional fee-for-service), y el ahorro reportado en
beneficiarios de Medicare (hasta ~USD 25,000/año) viene de menos admisiones hospitalarias y menos
visitas a emergencias, no de una consulta más barata.
**Heurística de decisión:** al evaluar cualquier modelo de atención primaria alternativo (farmacia+
triage IA, telemedicina, membresía de salud) por su potencial de ahorro, la pregunta correcta no es
"¿es más barato el punto de contacto?" sino "¿cambia el incentivo estructural de quien atiende?". Un
canal más barato de acceso (chat, IA) que sigue pagado por volumen de derivación no hereda
automáticamente el ahorro que reporta un modelo que cambió el incentivo de fondo (membresía fija) — son
mecanismos distintos aunque ambos se llamen "atención primaria alternativa".
- **Fuente:** F-108 (🟢A, peer-reviewed, *Journal of General Internal Medicine*/Springer 2024)
- **Leído a fondo:** 2026-08-27 (link.springer.com y pubmed.ncbi.nlm.nih.gov bloqueados por el proxy
  del entorno; reconstruido vía cobertura de PubMed/ResearchGate/Concierge Medicine Today que confirma
  autoría, cifra de ahorro y el mecanismo de cambio de incentivo vía membresía fija)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 10 (sigue Alta) ni 17 (utilidad
  real en farmacia/PBM) — agrega un criterio de diseño concreto para cualquier propuesta de atención
  primaria alternativa del proyecto: exigir que el modelo de pago al proveedor cambie de transaccional a
  capitado/membresía antes de proyectar sobre un canal propio el ahorro que reporta un modelo como DPC.

### 63. La claridad no siempre es la palanca correcta — cuando el objetivo de negocio es que el cliente escrutine antes de decidir, la fricción deliberada hace lo que la simplicidad no puede
F-225 ya estaba citado como el origen académico de "facilidad cognitiva" que sostiene el Principio 1
(Claridad y simplicidad) del Playbook del Asesor — información fácil de procesar se percibe como más
verdadera y confiable. La lectura a fondo (Alter & Oppenheimer 2009, revisión integradora que unifica
fluidez conceptual, perceptual y lingüística) confirma esa base, pero el trabajo relacionado de los
mismos autores (Alter, Oppenheimer, Epley & Eyre 2007, "Overcoming Intuition") agrega el reverso
exacto: cuando se introduce dificultad metacognitiva deliberada —una fuente borrosa, letra difícil de
leer, una pausa— la persona activa procesamiento analítico (Sistema 2) y se apoya menos en heurísticas
y atajos de juicio. La réplica posterior (Thompson et al.) matiza que esto produce procesamiento *más
profundo*, no necesariamente *más acertado* — la disfluencia no garantiza mejor decisión, solo más
escrutinio.
**Heurística de decisión:** "más simple siempre convierte mejor" no es universal — depende de si el
objetivo de la pieza es que el cliente decida rápido (ahí la fluidez ayuda) o que se detenga a
verificar antes de comprometerse (ahí la fricción deliberada es la herramienta correcta, no la
claridad). Esto conecta con tesis 1 (la divulgación no cambia la conducta) desde un ángulo nuevo: si
divulgar más claro no sube la calidad de la decisión, puede ser porque la claridad reduce el escrutinio
en vez de aumentarlo — el mecanismo que sí activa revisión crítica es la dificultad, no la facilidad.
Para cualquier momento donde el negocio necesita proteger al consumidor (confirmar que entendió el
coaseguro, dar tiempo antes de firmar una póliza de vida), la palanca correcta es fricción intencional,
no un explicador más simple.
- **Fuente:** F-225 (🟢A, revisión integradora peer-reviewed, *Personality and Social Psychology
  Review* 2009)
- **Leído a fondo:** 2026-08-27 (doi.org y journals.sagepub.com bloqueados por el proxy del entorno;
  reconstruido vía ResearchGate, Semantic Scholar y la literatura relacionada de los mismos autores
  sobre disfluencia y razonamiento analítico —Alter, Oppenheimer, Epley & Eyre 2007— que confirma el
  mecanismo de reversión y su límite: más procesamiento, no necesariamente más precisión)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 1 (sigue Alta) ni del Principio 1
  del Playbook (tesis 18) — les agrega un límite de alcance que ninguna de las dos tenía registrado: la
  fluidez ayuda a convertir, pero el objetivo opuesto (proteger al cliente de una decisión apresurada)
  necesita el mecanismo contrario, no una versión "más simple" del mismo principio.

### 64. Un promedio estable en el tiempo no es evidencia de solidez si nadie separó los casos fáciles de los difíciles — puede estar promediando un extremo que mejora con un extremo que nunca lo hace
F-43 ya estaba citado en tesis 10 por el patrón de que la precisión colapsa a 24.2% en enfermedades poco
comunes y 14.5% en presentaciones atípicas. La lectura a fondo confirma el mecanismo formal: los propios
autores (Harada, Sakamoto, Sugimoto & Shimizu, *JMIR Formative Research* 2024) reportan que la
"commonality of disease" (qué tan común es la enfermedad) y la "typicality of presentation" (qué tan
típica es la forma en que se presenta) están asociadas de forma estadísticamente significativa a la
precisión — no es ruido, es el predictor que explica por qué el promedio global (45.1%) se mantuvo plano
durante los 3 años del estudio: la mezcla de casos (mayoría común/típica, minoría rara/atípica) no
cambió, así que el promedio tampoco.
**Heurística de decisión:** cuando un proveedor presenta "N años en producción sin caída de precisión"
como prueba de estabilidad, la pregunta correcta no es si el promedio se mantuvo sino si puede mostrar el
desglose por el eje de dificultad que más le importa al negocio (aquí, rareza/atipicidad clínica). Un
promedio quieto puede estar promediando un extremo que funciona bien de forma consistente con un extremo
que falla mal de forma igual de consistente — la estabilidad del agregado no dice nada sobre si el
segmento de mayor riesgo mejoró, empeoró o nunca estuvo cubierto.
- **Fuente:** F-43 (🟢A, estudio observacional retrospectivo peer-reviewed, *JMIR Formative Research*
  2024)
- **Leído a fondo:** 2026-08-28 (ncbi.nlm.nih.gov bloqueado por el proxy del entorno; reconstruido vía
  JMIR Formative Research y cobertura que confirma autoría, período del estudio 2019-2022, y la
  asociación estadística entre "commonality"/"typicality" y precisión)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 10 (sigue Alta) — refuerza con un
  mecanismo formal (asociación estadística confirmada, no solo el dato observado del 24.2%/14.5%) el
  mismo punto que la revisión profunda de `cronista` del 2026-08-05 ya había matizado; la heurística aquí
  es transferible a cualquier métrica de desempeño de IA del proyecto (fraude, suscripción, chatbot), no
  solo a triage clínico.

### 65. Cuando un factor de riesgo tiene un odds ratio que multiplica por 15-20x al resto de la tabla, probablemente no es un sesgo conductual gradual — es una regla de compuerta que alguien no está cumpliendo
F-36 ya está citado en tesis 9 por su hallazgo dominante: no pedir receta (OR=29.06) supera por lejos a
pedir consejo en la farmacia (OR=1.88), comprar en menos de 5 minutos (OR=1.59) o ser hombre (OR=1.32).
La lectura a fondo confirma que el diseño del estudio (análisis secundario de la Encuesta Nacional de
Satisfacción de Usuarios en Salud 2016, 3,849 usuarios de farmacia) trata las cinco variables con el
mismo tipo de regresión logística — pero la distancia entre OR=29 y el resto (todas menores a 2) no es
una diferencia de grado, es una diferencia de tipo.
**Heurística de decisión:** en cualquier tabla de regresión con factores de riesgo, un OR que multiplica
al resto de la tabla por 15-20x casi nunca es una tendencia conductual graduable con un nudge — suele ser
una regla binaria de cumplimiento (aquí, "¿el dispensador pidió receta sí/no?") que alguien en la cadena
está incumpliendo. La intervención correcta para ese factor es una corrección de proceso/política
(auditoría, checklist obligatorio, incentivo al cumplimiento del protocolo), no un rediseño de mensaje o
incentivo dirigido al consumidor — que sí es la herramienta correcta para los otros cuatro factores de la
misma tabla (OR 1.3-1.9). Mezclar el tipo de intervención con el factor equivocado desperdicia el diseño.
- **Fuente:** F-36 (🟢A, artículo peer-reviewed, SciELO Perú 2021)
- **Leído a fondo:** 2026-08-28 (scielo.org.pe bloqueado por el proxy del entorno; reconstruido vía la
  versión indexada en Academia.edu y SciELO Preprints que confirma diseño del estudio, N=3,849 y la
  tabla completa de odds ratios)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 9 (sigue Alta) — la heurística de
  "OR desproporcionado = compuerta de proceso, no sesgo conductual" es transferible a cualquier variable
  con OR extremo que aparezca en el proyecto: si `lapuerta` alguna vez calibra un factor con un OR fuera
  de escala respecto al resto de sus variables, la primera hipótesis debe ser una regla de compuerta mal
  medida o mal cumplida, no un sesgo conductual real.

### 66. Un veredicto agregado de "sin efecto adverso sistemático" puede estar promediando un outcome muy negativo con otros neutrales — pedir el desglose por outcome antes de repetir el veredicto general
F-339 (revisión sistemática de Mazurenko, Taylor & Menachemi, *Medical Care Research and Review* 2022,
PubMed/MEDLINE/Cochrane 2000-2020) ya está citado en tesis 23 como transferencia de "redes estrechas de
proveedores" a "steering de canal de atención". La lectura a fondo confirma el veredicto agregado (costos
reducidos en la mayoría de medidas, sin efecto adverso sistemático en acceso/calidad) pero también un
detalle que el resumen de una línea no capturaba: dentro de "acceso", la mayoría de los análisis que
midieron específicamente el tiempo de espera para una cita programada encontraron un efecto no deseado —
esperas más largas en redes estrechas/por niveles — incluso cuando otros indicadores de acceso (distancia
recorrida, cercanía al proveedor previo) mejoraban.
**Heurística de decisión:** un veredicto agregado de "sin efecto adverso sistemático" en una revisión
sistemática no equivale a "ningún outcome individual empeoró" — puede estar promediando varios
indicadores neutrales o positivos con uno negativo y muy saliente para el cliente (aquí, tiempo de
espera, justo la fricción que más se siente y más se reclama). Antes de citar el veredicto agregado de
cualquier revisión como respaldo de una palanca de negocio (steering, tiering, redes estrechas), pedir el
desglose por outcome individual — el que el cliente experimenta directamente rara vez es el promedio.
- **Fuente:** F-339 (🟢A, revisión sistemática peer-reviewed, *Medical Care Research and Review* 2022)
- **Leído a fondo:** 2026-08-28 (journals.sagepub.com y el texto completo bloqueados por el proxy del
  entorno; reconstruido vía PubMed, el CV de la autora principal y el repositorio institucional de IUPUI
  que confirma la tabla de resultados por outcome, incluyendo el efecto negativo específico en tiempo de
  espera)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 23 (sigue Alta, el steering "sí
  ahorra costo real") — le agrega un matiz operativo: si el proyecto diseña una palanca de steering/
  tiering propia, monitorear el tiempo de espera para cita programada como métrica separada del ahorro
  agregado, porque es el punto donde la evidencia de redes de proveedores ya documentó fricción, y es
  exactamente el tipo de fricción que activa la reactancia que la propia tesis 23 identifica como el
  riesgo central del mecanismo.

### 67. El backlash de un dark pattern no depende de que exista manipulación — depende del subtipo específico y de a qué lado de la línea leve/agresivo cae
F-241 (Luguri & Strahilevitz 2021, *Journal of Legal Analysis*) ya estaba citado en el node de
tendencias-diseno-innovacion como "evidencia causal más fuerte del poder del diseño", pero solo por
las tres cifras agregadas (11.3% control → 25.8% leve → 41.9% agresivo). La lectura a fondo agrega el
detalle de mecanismo: no todos los dark patterns rinden igual — *hidden information*, *trick question*
y *obstrucción* son los subtipos que más manipulan con éxito, y son justamente los que dominan la
condición "leve" del experimento. Los patrones leves **no generan backlash medible** pese a duplicar
holgadamente la conversión; los agresivos casi cuadruplican la conversión pero **sí** disparan un
rechazo del consumidor lo bastante fuerte como para que los propios autores lo documenten como efecto
aparte. Y el daño de los leves no se reparte parejo: los sujetos con menos educación son
significativamente más susceptibles a ellos específicamente — no a los agresivos, donde la brecha
educativa no aparece igual de marcada.
**Heurística de decisión:** frente a cualquier técnica de persuasión (playbook de venta, diseño de
formulario, jerarquía visual de opciones), la pregunta de riesgo reputacional útil no es binaria
("¿esto es manipulador?") sino de clasificación: ¿de qué subtipo específico se trata (ocultar
información, pregunta trampa, fricción para el objetivo del usuario) y a qué lado de la línea
leve/agresivo cae? La línea que separa "convierte sin ruido" de "convierte más pero quema confianza"
no es la intención de la empresa, es el subtipo de la táctica — y el costo de los patrones leves lo
paga desproporcionadamente el segmento con menos educación financiera, justo la variable que el
generador de personas sintéticas ya modela.
- **Fuente:** F-241 (🟢A, experimento aleatorizado con muestra ponderada por censo de EE.UU.,
  N=1.773, *Journal of Legal Analysis*, Oxford)
- **Leído a fondo:** 2026-08-29 (academic.oup.com bloqueado por el proxy del entorno; reconstruido vía
  el working paper idéntico en SSRN/Chicago Unbound y coberturas técnicas del propio hallazgo que
  confirman la taxonomía de subtipos y el patrón de susceptibilidad por educación, no solo las tres
  cifras agregadas ya citadas)
- **Conexión razonada, no forzada:** no crea una tesis de negocio numerada nueva — sirve de criterio
  de auditoría para tesis 18 (el playbook de ventas de RIMAC mezcla una técnica real con una
  heurística sin base científica): cualquier técnica del playbook que dependa de omitir, complicar o
  poner fricción a la salida del cliente debería clasificarse por este mismo criterio de subtipo antes
  de escalarla, no solo evaluarse por si "funciona".

### 68. Una explicación de IA puede subir la aceptación de la recomendación por igual cuando la IA acierta y cuando falla — eso es inflar percepción de competencia, no calibrar confianza
F-244 (Bansal et al. 2021, CHI) ya está citado en tesis 22 con el resumen "explicaciones sin
verificabilidad producen sobre-confianza". La lectura a fondo agrega dos detalles que cambian cómo se
debería leer cualquier propuesta de "agregar explicabilidad" a un agente conversacional: primero, el
diseño experimental deliberadamente puso a la IA con precisión **comparable** a la de las personas (no
muy superior) para que la complementariedad fuera siquiera visible — un resultado nulo de
explicabilidad en ese régimen no dice nada todavía sobre un régimen donde la IA domina claramente,
que es un supuesto distinto que hay que verificar caso por caso. Segundo, y más importante: las
explicaciones subieron la tasa de aceptación de la recomendación de la IA **independientemente de si
esa recomendación era correcta o incorrecta**, y no rindieron mejor que el baseline barato de mostrar
solo el score de confianza crudo de la IA, sin narrativa.
**Heurística de decisión:** antes de invertir en una UI de "explicación" para cualquier sistema
asistido por IA del proyecto (triage, recomendador de cobertura, asesor conversacional), correr
primero el experimento barato de comparar contra solo mostrar un score de confianza numérico — si el
score crudo iguala a la explicación narrada en calibrar cuándo el usuario debería confiar y cuándo no,
la explicación es gasto de diseño sin retorno de seguridad. Y si el objetivo es medir si "explicar"
ayuda, verificar primero si el propio sistema tiene una brecha real de desempeño humano-IA para cerrar
— en paridad de desempeño, cualquier ganancia de "aceptación" que produzca la explicación es sospechosa
por default, no una señal de éxito.
- **Fuente:** F-244 (🟢A, full paper peer-reviewed, CHI 2021, autores de Microsoft Research/U. of
  Washington)
- **Leído a fondo:** 2026-08-29 (dl.acm.org, researchgate.net e idl.cs.washington.edu bloqueados por
  el proxy del entorno; reconstruido vía cobertura técnica del hallazgo, el repositorio NSF Public
  Access y el registro de Microsoft Research que confirman el diseño de paridad humano-IA y el
  resultado de sobre-aceptación independiente de la corrección, no solo el resumen ya citado)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 22 (sigue Alta en el mecanismo) —
  le agrega un criterio de diseño accionable que la tesis todavía no tenía: probar contra el baseline
  de "solo mostrar confianza" antes de construir explicación narrada, y verificar el régimen de
  paridad de desempeño humano-IA antes de extrapolar el resultado nulo a cualquier sistema del
  proyecto.

### 69. La aversión a redes angostas de proveedores no es una función continua del tamaño de la red — es casi binaria y se activa solo cuando la red excluye al médico habitual del paciente
F-341 (*Journal of Health Economics* 2018, vol. 60) ya está citado en tesis 23 dentro del rango
agregado F-338 a F-341 como "transferido de sistemas públicos". La lectura a fondo muestra que es en
realidad el paper más directamente aplicable a diseño de producto de todo ese cluster: usa datos
reales de elección de plan en un HIX privado (un plan de red amplia + cuatro de red angosta), con un
modelo de elección discreta que separa dos cosas que la intuición suele mezclar. La disposición a
pagar por una red que cubra al médico habitual del paciente es de US$84-275/mes en atención primaria
(US$0-115/mes en especialistas) — alta. Pero **condicional a que esa red ya cubra al médico habitual**,
la aversión adicional aparece solo frente a las redes **más angostas de todas**, no frente a la
angostura en sí. Es decir: la variable que mueve el rechazo no es "qué tan angosta es la red" en un
continuo, es un umbral binario — ¿está mi médico adentro o afuera?
**Heurística de decisión:** al diseñar cualquier palanca de red angosta/steering de canal (tesis 23),
la pregunta de diseño que más rinde no es "¿cuánto podemos angostar la red sin que se note?" sino
"¿la red angosta preserva al proveedor habitual del paciente, sí o no?" — preservar ese ancla permite
angostar la red bastante sin backlash proporcional; romperlo activa rechazo aunque el resto de la red
sea generoso. Es una re-especificación más barata y más accionable de la variable de diseño que la
proxy continua de "tamaño de red" que se usaría por default.
- **Fuente:** F-341 (🟢A, peer-reviewed, modelo de elección discreta sobre datos reales de un HIX
  privado del Medio Oeste de EE.UU., *Journal of Health Economics* 2018)
- **Leído a fondo:** 2026-08-29 (pubmed.ncbi.nlm.nih.gov y sciencedirect.com bloqueados por el proxy
  del entorno; reconstruido vía IDEAS/RePEc, el resumen de conferencia APPAM 2017 del mismo estudio y
  el repositorio de CDC Stacks que confirman el modelo y las cifras exactas de disposición a pagar,
  más el matiz de umbral que el resumen de una línea ya citado no capturaba)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 23 (sigue Alta) — le agrega la
  palanca de diseño más concreta que el cluster de evidencia de esa tesis todavía no tenía: cualquier
  producto de steering/red angosta del proyecto debería tratar "¿el médico habitual del paciente queda
  adentro?" como la variable de diseño primaria, antes que el tamaño de red como proxy genérica.

### 70. El efecto certeza explica por qué "cero deducible" se sobre-paga: eliminar el último tramo de riesgo vale desproporcionadamente más que reducir el riesgo esperado en la misma magnitud sin eliminarlo
Kahneman & Tversky (1979) no se agotan en "las pérdidas duelen ~2x más que ganancias equivalentes"
(ya citado en tesis 18 vía el Bloque 4 del Playbook). El mecanismo más específico y menos citado es
el **efecto certeza**: la gente descuenta desproporcionadamente un resultado que es solo probable
frente a uno que es seguro — no de forma lineal con la probabilidad. Pasar de 100%→95% de protección
se siente peor que pasar de 50%→45%, aunque la caída de probabilidad (5 puntos) sea idéntica en
ambos casos. Esto viene empaquetado con dos piezas más: una **fase de edición** previa a evaluar
cualquier opción (cómo se descompone/enmarca el problema antes de comparar) y un **efecto
aislamiento** — la gente descarta los componentes que todas las opciones comparadas comparten, lo
que produce preferencias inconsistentes según cómo se recorte la comparación, no según el valor
económico real de fondo. **Heurística de decisión:** cuando un cliente prefiere un plan "cero
deducible" más caro sobre uno con deducible bajo y prima menor, aunque el valor esperado favorezca
al segundo, no es necesariamente error de cálculo — es el efecto certeza operando exactamente como
predice la teoría fundacional (Nobel 2002). La prima que la gente paga por eliminar el último tramo
de riesgo residual es sistemática, no ruido, y sugiere que un producto que venda "cobertura total"
puede justificar un precio más alto que uno matemáticamente equivalente que solo reduce el riesgo
esperado sin llegar a cero.
- **Fuente:** F-221 (🟢A, Kahneman & Tversky 1979, *Econometrica* 47(2):263-291 — paper fundacional,
  base del Premio Nobel de Economía 2002 de Kahneman; ya citado en el ledger solo por el resumen de
  una línea sobre aversión a la pérdida)
- **Leído a fondo:** 2026-08-30 (jstor.org bloqueado por el proxy del entorno; reconstruido vía
  búsqueda dirigida que confirma la función de valor en forma de S, el efecto certeza, la fase de
  edición/evaluación y el efecto aislamiento — piezas del mecanismo que el resumen de una línea ya
  citado en tesis 18 no capturaba)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 2 (coaseguro como cuello de
  botella de comprensión) ni de tesis 18 (Playbook del Asesor) — agrega una explicación de mecanismo
  para un patrón de precio/producto (sobre-demanda de "cero deducible") que ninguna de las dos tesis
  tenía explícito, y una hipótesis de pricing (prima por certeza total) que queda como instinto hasta
  que un `F-n` mida directamente disposición a pagar por deducible cero en seguros.

### 71. Antes de leer un piloto por diseño escalonado (stepped-wedge) como evidencia causal, verificar que controló la tendencia temporal — es la vulnerabilidad estructural específica de ese diseño, no un chequeo de calidad genérico
Mdege et al. (2011) confirman las ventajas ya conocidas del diseño escalonado que sostienen tesis 10
(menor contaminación entre clusters, mayor aceptación porque todos reciben la intervención
eventualmente, menor demanda simultánea de recursos — relevante para pilotar `/trinidad`+`/seeker`
por etapas en vez de todo a la vez). Lo que el resumen de una línea no capturaba es la contracara
exacta: la vulnerabilidad **no es genérica** ("todo diseño tiene sesgos") sino **específica y
predecible** — el diseño escalonado es estructuralmente susceptible a que una tendencia secular en
el resultado (estacionalidad de consultas, mejora orgánica de un proceso con el tiempo, cualquier
cosa que cambie el outcome independientemente de la intervención) se confunda con el efecto de la
intervención, porque cada cluster se mide en un momento distinto del calendario según cuándo le
tocó el cambio. **Heurística de decisión:** frente a cualquier resultado positivo reportado desde un
piloto escalonado (el diseño que ya recomienda tesis 10 para testear el modelo de triage IA +
farmacias), la primera pregunta de auditoría no es "¿la muestra fue suficiente?" sino "¿controlaron
la tendencia temporal/estacional del outcome?" — sin eso, un resultado positivo puede ser solo el
calendario, no la intervención.
- **Fuente:** F-59 (🟢A, Mdege et al. 2011, *Journal of Clinical Epidemiology* — revisión
  metodológica peer-reviewed, ya citado en el ledger desde 2026-07-06 para `modelo-salud-ia-
  farmacias-peru.md` solo por el resumen de ventajas del diseño)
- **Leído a fondo:** 2026-08-30 (ncbi.nlm.nih.gov bloqueado por el proxy del entorno; reconstruido
  vía búsqueda dirigida que confirma tanto las ventajas ya citadas como la vulnerabilidad específica
  a confusión por tendencia secular, ausente del resumen original)
- **Conexión razonada, no forzada:** no cambia la confianza de tesis 10 (sigue Alta) — le agrega un
  criterio de auditoría concreto para cuando el proyecto reciba o diseñe resultados de un piloto
  escalonado: exigir el control de tendencia temporal antes de leer el resultado como causal.

### 72. Cuando un sistema de triaje remoto mide "incumplimiento" de su propia recomendación como fricción a resolver, verificar primero qué fracción de los que "no cumplieron" tenían un caso real grave
El estudio de cumplimiento de NHS 111 (Lewis et al. 2021, PLOS One, N=3.6M llamadas, Yorkshire &
Humber 2013-2017) encuentra que 11% de los pacientes a quienes se aconsejó autocuidado/atención
primaria fueron igual a Urgencias. El resumen de una línea ya citado (`F-333`) lee esto como
fricción de adopción a minimizar. La lectura completa da un dato que cambia el signo del hallazgo:
de ese 11% "no conforme", **88% fue clasificado como urgente al llegar** y **37% terminó
hospitalizado**. No es un grupo de pacientes ansiosos desobedeciendo una indicación correcta — es
evidencia directa de que el sistema de triaje remoto subclasificó una fracción no trivial de casos
reales graves, y esos pacientes corrigieron el error del sistema por cuenta propia. **Heurística de
decisión:** frente a cualquier métrica de "incumplimiento" o "fricción" en un sistema de triage
(telefónico, chatbot, symptom-checker — el modelo `/trinidad`+`/seeker` de farmacia+IA incluido), no
asumir que el usuario que se desvía de la recomendación está siendo irracional o mal informado;
cruzar primero ese grupo contra el desenlace real (¿terminó siendo un caso grave?) antes de
diseñar cualquier intervención para "mejorar la adherencia" — la intervención correcta puede ser
mejorar la clasificación del sistema, no la conformidad del paciente.
- **Fuente:** F-333 (🟢A para el componente peer-reviewed en PLOS One / 🔵B para el componente de
  revisión rápida — Lewis et al. 2021, ya citado en el ledger desde 2026-07-27 solo por el resumen
  de una línea sobre la cifra agregada de £4.52M y 11% de no conformidad)
- **Leído a fondo:** 2026-08-30 (journals.plos.org bloqueado por el proxy del entorno; reconstruido
  vía búsqueda dirigida que confirma la cifra de 11% y agrega el desglose de severidad —88% urgente,
  37% hospitalizado— ausente del resumen original)
- **Conexión razonada, no forzada:** refuerza desde otro ángulo empírico la intuición 53
  (2026-08-24, sistema de triaje puede fallar en dos direcciones simétricas — medir solo el ahorro
  de costo esconde la sobre-confianza peligrosa) con un caso real y auditado de esa exacta falla; no
  cambia la confianza de tesis 10, pero le agrega un criterio de validación concreto: cualquier
  piloto propio de triage debe reportar el desenlace real de quienes "incumplieron" la recomendación,
  no solo la tasa de incumplimiento.

## 📔 Bitácora

- **2026-07-12 a 2026-07-19** — *(Resumida el 2026-08-10 al cumplir la ventana de ~30 días; el
  detalle de cada tesis creada en esta ventana vive en 🎯 Tesis vigentes, cada una con su propia
  fecha de "Actualizado".)* Creación inicial de la opinión (2026-07-12) sobre las primeras 15
  fuentes del ledger (F-1 a F-15): tesis 1-5 (divulgación no convierte, coaseguro como cuello de
  botella de comprensión, problema estructural no generacional, brecha sísmica peruana como
  categoría casi vacía, ESG como palanca global no probada en Perú). El mismo día el ledger creció a
  F-27 (`/trinidad` sobre behavioral design): sumé tesis 6 (crisis del nudge) y 7 (s-frame > i-frame,
  caso UBI). Siete revisiones diarias consecutivas (07-13 a 07-19) reportaron "sin cambios
  sustanciales" contra `registro_fuentes.md`, fijo en F-1 a F-27; único ajuste real en la ventana:
  tope explícito de confianza a tesis 3 y 4 (no suben por consistencia narrativa, solo por fuente B+
  directa). Esa racha de "sin novedad" resultó ser en parte un artefacto de ruta de archivo: el
  ledger real sí creció mientras tanto bajo un nombre de archivo distinto (`codice.md`, vigente desde
  el 2026-07-19) — corregido el 2026-07-20 (entrada siguiente).
- **2026-07-20 a 2026-07-31** — *(Resumida el 2026-08-18 al cumplir la ventana de ~30 días; el
  detalle de cada tesis creada o matizada en esta ventana vive en 🎯 Tesis vigentes, cada una con
  su propia fecha de "Actualizado".)* Doce corridas que llevaron el ledger de F-171 a F-398 y la
  cartera de tesis de 7 a 24. Hitos principales: **2026-07-20** — se detectó que el ledger real
  vivía bajo `codice.md` (no `registro_fuentes.md`), incorporando de golpe 144 fuentes represadas;
  sumó tesis 8-13 (riesgo regulatorio de contacto no consentido, farmacia+triage IA, riesgo de
  sobreclamar precisión clínica, ciclo de rentabilidad de 25 años, choice overload como folklore,
  divulgación progresiva de datos). **2026-07-21** — primera revisión profunda (F-3, F-6, F-9,
  F-10, F-16: corrigió autoría de F-3, sumó tesis 14 miopía/narrow framing) más una segunda corrida
  del día que sumó tesis 15 (ancla de cifra % + riesgo regulatorio Indecopi, 8 fuentes nuevas sobre
  el flyer "Vida Ahorro"). **2026-07-22** — segunda revisión profunda (F-17 a F-21): confirmó por
  tres metodologías independientes que el efecto promedio del nudge no existe, sin bajar la
  confianza de tesis 6. **2026-07-23** — investigación `/trinidad` sobre asesores vs. venta digital
  y balance financiero de salud EE.UU.: sumó tesis 16 (el asesor se redistribuye, no desaparece) y
  17 (la utilidad real vive en farmacia/PBM, filing SEC primario). **2026-07-24** — auditoría a
  pedido del usuario del Playbook del Asesor RIMAC: sumó tesis 18 (8 de 9 "sesgos" del Bloque 4 sí
  tienen base académica; el noveno, "regla del 10x", es heurística de ventas sin evidencia,
  mezclada con la misma autoridad). **2026-07-25** — glosario de vida y perfilamiento por
  motivación: sumó tesis 19 (perfilar por motivación expone punto ciego en `lapuerta`, construido
  sobre demografía) y 20 (precio percibido 7-12x inflado como freno real en vida individual).
  **2026-07-27** — node de tendencias de diseño (92 fuentes, filtrado con criterio de negocio): sumó
  tesis 21 (ROI de diseño debe argumentarse por mecanismo, ninguna cifra citada globalmente tiene
  fuente primaria auditable) y 22 (personalización con IA puede bajar conversión si el dato es
  sensible y la privacidad está saliente); registró como instinto/contexto de proyecto (no F-n) que
  RIMAC cerró por completo el contacto en frío sin consentimiento. **2026-07-29** — 51 fuentes
  nuevas (steering conductual, casos Ethos/Bowtie, LATAM vida digital-híbrida): sumó tesis 23
  (steering hacia canal barato ahorra costo pero genera la reactancia más fuerte del sector cuando
  se percibe como interés del pagador) y amplió tesis 16 con el dato LATAM (Azos vía 9,000+
  corredores, bancaseguros 80% de distribución en Brasil); tercera revisión profunda (F-23, F-36,
  F-40, F-41, F-42) matizó tesis 7, 9 y 10 sin bajar ninguna confianza. **2026-07-30** — iteración 2
  del node de diseño: sumó tesis 24 (generative UI sube preferencia declarada pero falla en soporte
  y consistencia entre sesiones) y dos riesgos nuevos (shadow AI sin gobierno de dato, precedente
  MercadoLibre de roles de UX desvinculados). **2026-07-31** — sin cambios sustanciales, ninguna
  tesis desalineada. Ningún nivel de confianza bajó en toda la ventana; todo ajuste fue matiz o
  suma de tesis nueva sobre evidencia que la refuerza.
- **2026-08-01** — Corrida diaria de refinamiento. Confirmé `main` actualizado (fast-forward
  02ad91d→d8aa4a2) y leí `codice.md` completo: sigue tope en F-398, idéntico al que ya procesó la
  corrida de ayer (2026-07-31) — **sin cambios sustanciales** en evidencia, cero fuentes nuevas
  registradas por `cronista`/`/trinidad`/`/seeker`/`/gossip`/`/marketer` en las últimas 24h. Repasé
  las 24 tesis contra ese mismo tope: ninguna quedó desalineada con el ledger vigente, y no forcé
  ninguna conexión nueva entre tesis solo por completar el paso — la racha de "sin cambios" de
  2026-07-30/31 ya agotó las conexiones razonables disponibles entre las tesis más recientes
  (21-24). Próximo salto de tesis/confianza sigue condicionado a que alguna skill de investigación
  registre fuentes nuevas en el ledger, o a que la próxima revisión profunda (cada ~3 días, la
  última corrió el 2026-07-29 sobre F-23/F-36/F-40/F-41/F-42) encuentre un matiz de mecanismo al
  leer a fondo una fuente ya citada solo por su resumen. Bitácora con 21 días de historial
  (2026-07-12 a hoy), dentro de la ventana de ~30 días — sin podar todavía.
- **2026-08-02** — Corrida diaria de refinamiento. Confirmé `main` actualizado (fast-forward
  02ad91d→c46dbd3) y leí `codice.md` completo: sigue tope en F-398, idéntico al que ya procesó la
  corrida de ayer (2026-08-01) — **sin cambios sustanciales** en evidencia, cero fuentes nuevas
  registradas por `cronista`/`/trinidad`/`/seeker`/`/gossip`/`/marketer` en las últimas 24h. Repasé
  las 24 tesis contra ese mismo tope: ninguna quedó desalineada con el ledger vigente, y no forcé
  ninguna conexión nueva entre tesis solo por completar el paso — la racha de "sin cambios" desde
  el 2026-07-30 ya agotó las conexiones razonables disponibles entre las tesis más recientes
  (21-24). La última revisión profunda (rutina de `cronista`, cada ~3 días) sigue siendo la del
  2026-07-29 (F-23/F-36/F-40/F-41/F-42) — cuatro días sin corrida nueva, pero esa rutina es de
  `cronista`, no de este proceso diario, así que no la disparo aquí. Próximo salto de
  tesis/confianza sigue condicionado a que alguna skill de investigación registre fuentes nuevas en
  el ledger. Bitácora con 22 días de historial (2026-07-12 a hoy), dentro de la ventana de ~30
  días — sin podar todavía.
- **2026-08-03** — Corrida diaria de refinamiento. Confirmé `main` actualizado (fast-forward
  02ad91d→725dbf0) y leí `codice.md` completo: el ledger creció de F-398 a F-468 desde la última
  corrida (2026-08-02) — **cambio sustancial**, 70 fuentes nuevas en dos iteraciones del mismo node
  (`_nodes/tendencias-diseno-innovacion.md`): iteración 3 (F-399 a F-429, el node se audita a sí
  mismo — desmonta su propio hallazgo de julio) e iteración 4 (F-430 a F-468, primera apertura del
  node al dominio de **innovación**, no solo diseño). Filtré con el mismo criterio de negocio que ya
  usé el 07-27/07-29/07-30 para este node: integré solo lo transferible a Rimac/seguros. Sumé tesis
  25 (Root vs. Lemonade — mismo modelo insurtech digital, combined ratio de 91.4% vs. ~139%; la
  rentabilidad depende de disciplina de suscripción, no de la capa tecnológica, con la causa exacta
  todavía como hipótesis abierta del propio node, H29). Corregí tesis 21: la cifra del "impuesto de
  verificación" que sumé el 07-30 (4.3 min/senior vs. 1.2 min/junior) resultó ser, en la propia
  auditoría del node, una sexta cadena de eco de cita sin fuente primaria — la retiré, y el dato real
  que sí sobrevive invierte lo que yo había asumido: más experiencia acumulada produce **menos**
  escrutinio del código generado por IA, no más. Añadí un matiz de proceso a tesis 7: F-442 (el RCT
  de UBI que el barrido de innovación presentó como "el hallazgo más accionable") es el **mismo**
  estudio que ya sostiene esa tesis (F-23, mismo NCT06101251) — no lo sumé como respaldo adicional
  para no inflar el conteo de fuentes independientes, solo tomé el dato nuevo real que aportaba
  (conflicto de interés del financiador sin verificar). Sumé una oportunidad (exigir combined/loss
  ratio auditado antes de leer cualquier apuesta de innovación como éxito — incluye que los labs
  peruanos activos hoy, BCP CIX y Pacífico "La Cápsula", no tienen ningún dato público de retorno) y
  dos riesgos (cifras de fracaso de producto sin fuente primaria localizable, F-444; y la cifra ya
  retirada del impuesto de verificación). Ninguna tesis 1-20, 22-24 requirió ajuste de confianza —
  el ledger nuevo las toca solo por conexión razonada, no por evidencia directa nueva sobre
  seguros/salud/Perú, salvo tesis 25 (nueva, con evidencia directa de filing) y las correcciones ya
  descritas en tesis 7 y 21. Bitácora con 23 días de historial (2026-07-12 a hoy), dentro de la
  ventana de ~30 días — sin podar todavía.
- **2026-08-05** — Corrida diaria de refinamiento (no corrió el 2026-08-04: sin commit de este
  proceso ese día). Confirmé `main` actualizado (fast-forward 02ad91d→c00c843, que ya trajo consigo
  el propio commit del 2026-08-03 de esta opinión) y leí `codice.md` completo: sigue tope en F-468,
  idéntico al que ya procesó la corrida del 2026-08-03 — **sin cambios sustanciales** en evidencia,
  cero fuentes nuevas registradas por `cronista`/`/trinidad`/`/seeker`/`/gossip`/`/marketer` desde
  entonces. Repasé las 25 tesis contra ese mismo tope: ninguna quedó desalineada con el ledger
  vigente, y no forcé ninguna conexión nueva entre tesis solo por completar el paso — la corrida del
  08-03 ya agotó las conexiones razonables disponibles (tesis 25, correcciones a tesis 7 y 21). La
  última revisión profunda (rutina de `cronista`, cada ~3 días) sigue siendo la del 2026-07-29
  (F-23/F-36/F-40/F-41/F-42) — seis días sin corrida nueva, pero esa rutina no es de este proceso
  diario, así que no la disparo aquí. Próximo salto de tesis/confianza sigue condicionado a que
  alguna skill de investigación registre fuentes nuevas en el ledger. Bitácora con 24 días de
  historial (2026-07-12 a hoy), dentro de la ventana de ~30 días — sin podar todavía.
- **2026-08-05 (revisión profunda, rutina `cronista` cada ~3 días)** — Leí a fondo las 5 fuentes
  🟢A más antiguas sin lectura profunda previa: F-43, F-44, F-50, F-53, F-54 (todas del rango de
  `modelo-salud-ia-farmacias-peru.md`, registradas originalmente el 2026-07-06). No sumé tesis
  nueva — las cinco ya sostenían tesis 10, y la lectura completa la afina sin cambiar su
  dirección ni su confianza (sigue Alta). Tres matices de mecanismo: (1) F-50 — el defecto
  metodológico exacto de Babylon fue que su prueba de precisión usó **médicos simulando
  pacientes en viñetas**, no usuarios legos reales; cualquier piloto propio debe validar con
  usuarios reales o repite el mismo error, no solo su titular; (2) F-43 — el 45.1% de precisión
  del symptom-checker japonés no es plano: cae a 24.2% en enfermedades poco comunes y 14.5% en
  presentaciones atípicas, sin curva de aprendizaje en 3 años de producción — falla justo donde
  el riesgo clínico es mayor; (3) F-44 — el argumento de por qué "precisión diagnóstica" es la
  métrica equivocada no es genérico: la relación médico-paciente aporta percepción/observación
  que un chatbot resta de la consulta aunque su precisión sea comparable a la humana, lo que
  refuerza que la capa de atención humana del modelo cumple una función de outcome, no solo de
  respaldo ante error de clasificación. Encontré además dos **correcciones de cita/autoría** que
  el resumen de una línea del ledger no dejaba ver: F-53 tenía la URL de un paper (Holtrop et
  al. 2021, "Clarifications and resources") mal atribuida al fundacional de Glasgow/Vogt/Boles
  1999 — mismo framework RE-AIM, Glasgow es coautor de ambos, pero es un artículo distinto que
  documenta 13 malentendidos de aplicación y la evolución del framework hacia PRISM (contexto
  organizacional que RE-AIM 1999 no cubre); F-54 estaba atribuido a "Kirchner, J.E. et al. 2023"
  cuando el autor real es Bryan R. Garner (2022) y el aporte propio del paper es la extensión
  DIeSEL (agrega sostenibilidad económica y nivel de escalamiento al diseño desde el inicio, no
  como paso posterior a los tipos 1/2/3 de Curran). Corregí ambas en `codice.md` (mismo criterio
  que la corrección de autoría de F-3 el 2026-07-21) y enriquecí `modelo-salud-ia-farmacias-
  peru.md` (§2 con los tres matices de mecanismo, §3 con los 13 malentendidos de RE-AIM/PRISM, §4/E2
  con DIeSEL). Actualicé `alma.md` con la fecha y nota de esta revisión. Bitácora de revisión
  profunda con 15 fuentes acumuladas (F-3 a F-54, todas 🟢A) desde el 2026-07-21.
- **2026-08-06** — Corrida diaria de refinamiento. Confirmé `main` actualizado (fast-forward
  02ad91d→4f03b8d, que trajo consigo commits ajenos a esta opinión: la corrección de nombres de
  variables en `_nodes/modelo-salud-ia-farmacias-peru.md`, la renombrada de
  `_nodes/tendencias-diseno.md` a `tendencias-diseno-innovacion.md`, y una simulación nueva de la
  Guía de triaje sobre 200 usuarios sintéticos con `lapuerta`) y leí `codice.md` completo: sigue
  tope exacto en F-468 (468 entradas, F-1 a F-468 sin huecos), idéntico al que ya procesó la
  corrida del 2026-08-05 — **sin cambios sustanciales** en evidencia, cero fuentes nuevas
  registradas por `cronista`/`/trinidad`/`/seeker`/`/gossip`/`/marketer` en las últimas 24h.
  Repasé las 25 tesis contra ese mismo tope: ninguna quedó desalineada con el ledger vigente, y no
  forcé ninguna conexión nueva entre tesis solo por completar el paso — la revisión profunda de
  ayer (F-43/F-44/F-50/F-53/F-54) ya agotó los matices disponibles sobre tesis 10, y ningún commit
  de hoy en `main` toca evidencia externa citable con `F-n` (son artefactos de proyecto — dataset
  simulado, corrección de nombres, renombrado de node — no investigación nueva de `cronista`). La
  próxima revisión profunda (rutina de `cronista`, cada ~3 días, última el 2026-08-05) no vence
  hoy. Próximo salto de tesis/confianza sigue condicionado a que alguna skill de investigación
  registre fuentes nuevas en el ledger. Bitácora con 25 días de historial (2026-07-12 a hoy),
  dentro de la ventana de ~30 días — sin podar todavía.
- **2026-08-06 (ampliación — nueva rutina de intuición, a pedido del usuario)** — El usuario pidió
  que, cada día, el Lobo lea a profundidad 3 fuentes aleatorias del ledger (empezando por las de
  mayor rigurosidad) y transforme esa lectura en conocimiento propio que mejore su intuición y
  capacidad de decisión — no solo en refinamiento de tesis. Diseñé el mecanismo: sección nueva
  **"🧠 Intuición acumulada"** en esta opinión (heurísticas de juicio, no tesis de negocio
  puntuales), registro propio `research/lobo/fuentes_leidas_lobo.md` (evita releer, independiente
  de `revision_profunda.md` de `cronista` — selección aleatoria diaria por nivel de rigor agotado
  en orden A→B→C→D→E, vs. la de `cronista`: 5 fuentes, ID más antiguo, cada ~3 días), y documenté
  la regla en `CLAUDE.md` §"Proceso diario: opinión de negocio de 'El Lobo'" para que persista
  entre corridas (cada corrida es una sesión nueva sin memoria de esta conversación — la regla
  tiene que vivir en el repo, no en el prompt externo que dispara la tarea, que no puedo editar
  desde aquí). Ejecuté la primera corrida como semilla del mecanismo: seleccioné al azar 3 fuentes
  🟢A del ledger que ni el Lobo ni la revisión profunda de `cronista` habían leído a fondo (de 137
  fuentes A totales, 117 seguían sin lectura profunda) — F-82 (Rothschild & Stiglitz 1976,
  selección adversa en seguros), F-107 (Direct Primary Care, JABFM 2018) y F-236 (Davis 1976,
  decisión de compra en el hogar). Las URLs directas dieron 403 (mismo bloqueo de proxy ya
  documentado para fuentes académicas); reconstruí el contenido sustancial de las tres vía
  búsqueda dirigida. Sumé las tres primeras entradas de Intuición acumulada: (1) correr el test de
  selección adversa antes de lanzar cualquier producto nuevo — no solo preguntar si hay demanda;
  (2) separar "bueno para quien participa" de "bueno para el sistema/población" al evaluar
  cualquier modelo de atención con mecanismo de acceso restrictivo (conecta con tesis 9, sin
  cambiarle la confianza); (3) en seguros de alto involucramiento la unidad real de decisión suele
  ser el hogar, no el individuo frente al asesor (refuerza desde otro ángulo el matiz ya hecho a
  C.6 de tesis 18). Ninguna tesis de negocio cambió de confianza por esta corrida — es un
  mecanismo nuevo y paralelo, no una revisión de evidencia sobre las tesis existentes.
- **2026-08-01 a 2026-08-07** — *(Resumida el 2026-08-21 al cumplir la ventana de ~30 días; el
  detalle de cada tesis creada o matizada en esta ventana vive en 🎯 Tesis vigentes, cada una con
  su propia fecha de "Actualizado"; el detalle de cada Intuición vive en esa sección con su propia
  fuente/fecha.)* Siete corridas. **2026-08-01/02** — sin cambios sustanciales, ledger fijo en
  F-398. **2026-08-03** — el ledger creció de F-398 a F-468 (70 fuentes nuevas, dos iteraciones del
  node `tendencias-diseno-innovacion.md`): sumó tesis 25 (Root vs. Lemonade — combined ratio 91,4%
  vs. ~139%, la rentabilidad depende de disciplina de suscripción, no de la capa tecnológica);
  corrigió tesis 21 (retiró la cifra del "impuesto de verificación", una cadena de eco de cita sin
  fuente primaria — el dato real que sobrevive invierte el supuesto: más experiencia produce
  *menos* escrutinio del código de IA, no más); matizó tesis 7 (F-442 resultó ser el mismo estudio
  que ya sostenía la tesis vía F-23, no un respaldo independiente adicional). **2026-08-05** — sin
  cambios sustanciales en el tope (F-468); revisión profunda de `cronista` el mismo día (F-43, F-44,
  F-50, F-53, F-54) matizó tesis 10 sin cambiar su confianza y corrigió dos autorías mal atribuidas
  en `codice.md` (F-53, F-54). **2026-08-06** — sin cambios sustanciales en el tope; a pedido del
  usuario, diseñé el mecanismo de **"🧠 Intuición acumulada"** (lectura diaria de 3 fuentes al azar,
  orden por rigurosidad agotado A→E, registro en `research/lobo/fuentes_leidas_lobo.md`) y ejecuté
  su primera corrida (entradas 1-3: F-82, F-107, F-236). **2026-08-07** — sin cambios sustanciales
  en el tope; segunda corrida de intuición (entradas 4-6: F-6, F-53, F-230). Ningún nivel de
  confianza de tesis bajó en toda la ventana; todo ajuste fue matiz, corrección de cita o suma de
  tesis nueva sobre evidencia que la refuerza.
- **2026-08-08** — Corrida diaria de refinamiento. Confirmé `main` actualizado (fast-forward
  d739018→22e9aee, que trajo consigo el commit de la corrida de ayer) y leí `codice.md` completo:
  verifiqué la secuencia F-1 a F-468 sin huecos — sigue tope exacto en F-468, idéntico al que ya
  procesó la corrida de ayer (2026-08-07) — **sin cambios sustanciales** en evidencia, cero fuentes
  nuevas registradas por `cronista`/`/trinidad`/`/seeker`/`/gossip`/`/marketer` en las últimas 24h.
  Repasé las 25 tesis contra ese mismo tope: ninguna quedó desalineada con el ledger vigente, y no
  forcé ninguna conexión de tesis nueva solo por completar el paso. La última revisión profunda
  (rutina de `cronista`, cada ~3 días, última el 2026-08-05) no vence hoy. Sí corrió la rutina diaria
  de intuición (tercera corrida desde que se creó el 2026-08-06): de las 137 fuentes 🟢A del ledger,
  6 ya tenían lectura profunda del Lobo (F-6, F-53, F-82, F-107, F-230, F-236) — seleccioné al azar 3
  de las 131 restantes: F-220 (Tversky & Kahneman 1974, anclaje), F-148 (Hone & Graham 2000, SASSI)
  y F-66 (Xu et al. 2020, micro-costing en salud). Sumé las entradas 7, 8 y 9 de Intuición
  acumulada: (7) un disclaimer de que una cifra es "referencial" no neutraliza su efecto de
  ancla — el experimento fundacional de la rueda de la fortuna mostró el efecto (~20pp de
  desplazamiento) sobreviviendo intacto aunque el sujeto viera que el número era aleatorio; conecta
  con tesis 15/18 sin cambiarles la confianza; (8) satisfacción subjetiva y desempeño objetivo de un
  sistema conversacional pueden moverse en direcciones opuestas en el mismo segmento (usuarios
  mayores: peor tiempo de tarea, mejor calificación) — profundiza el riesgo ya anotado sobre medir
  mal al agente conversacional de Rimac; (9) el silencio metodológico sobre perspectiva de costeo,
  año de precios y ajuste por inflación es la norma (no la excepción) en la literatura de
  micro-costing en salud, y debe leerse como bandera roja al evaluar cualquier cifra de
  costo-efectividad que en el futuro sostenga el caso de negocio de farmacia+triage IA (tesis 9/10).
  Ninguna tesis de negocio cambió de confianza por esta corrida — es el mecanismo paralelo de
  intuición, no una revisión de evidencia sobre las tesis existentes. Actualicé
  `research/lobo/fuentes_leidas_lobo.md` con las tres fuentes leídas hoy. Bitácora con 27 días de
  historial (2026-07-12 a hoy), dentro de la ventana de ~30 días — sin podar todavía.
- **2026-08-09** — Corrida diaria de refinamiento. Confirmé `main` actualizado (fast-forward
  d739018→daad3e9, que trajo consigo el commit de la corrida de ayer) y leí `codice.md` completo:
  verifiqué la secuencia F-1 a F-468 sin huecos — sigue tope exacto en F-468, idéntico al que ya
  procesó la corrida de ayer (2026-08-08) — **sin cambios sustanciales** en evidencia, cero fuentes
  nuevas registradas por `cronista`/`/trinidad`/`/seeker`/`/gossip`/`/marketer` en las últimas 24h.
  Repasé las 25 tesis contra ese mismo tope: ninguna quedó desalineada con el ledger vigente, y no
  forcé ninguna conexión de tesis nueva solo por completar el paso. La última revisión profunda
  (rutina de `cronista`, cada ~3 días, última el 2026-08-05) no vence hoy. Sí corrió la rutina diaria
  de intuición (cuarta corrida desde que se creó el 2026-08-06): de las 141 fuentes 🟢A del ledger, 9
  ya tenían lectura profunda del Lobo (F-6, F-53, F-66, F-82, F-107, F-148, F-220, F-230, F-236) —
  seleccioné al azar 3 de las 132 restantes: F-56 (Nature Health 2025, scoping review de silent
  trials), F-55 (Cully/Bauer 2012, diseño híbrido tipo 2) y F-122 (IPDAS Collaboration 2021, ayudas de
  decisión). Sumé las entradas 10, 11 y 12 de Intuición acumulada: (10) el silent trial pasado una vez
  no es garantía permanente — el propio scoping review no encuentra guías formales sobre cuándo
  repetirlo, y cita un caso real de colapso de AUC (0.90→0.50) por distribution shift tras un pase
  inicial exitoso, matiz de vigencia temporal que tesis 10 no tenía explícito; (11) probar
  efectividad clínica e implementación con fidelidad conviene correr en paralelo desde el día uno del
  piloto (diseño "híbrido tipo 2" de Curran et al. 2012), no en dos fases separadas — aplicación
  directa al diseño del piloto de farmacia+triage IA de tesis 9/10; (12) una ayuda de decisión rigurosa
  según el estándar IPDAS no es solo un material visual bien diseñado (tesis 12) — exige, entre 11
  dominios, declarar el conflicto de interés de quien la construye, dominio incómodo para cualquier
  comparador que el propio asegurador diseñe sobre su catálogo. Ninguna tesis de negocio cambió de
  confianza por esta corrida — es el mecanismo paralelo de intuición, no una revisión de evidencia
  sobre las tesis existentes. Actualicé `research/lobo/fuentes_leidas_lobo.md` con las tres fuentes
  leídas hoy. Bitácora con 28 días de historial (2026-07-12 a hoy), dentro de la ventana de ~30 días
  — sin podar todavía; la próxima corrida (2026-08-10) cumple el umbral y debe evaluar podar/resumir
  las entradas de la primera semana (2026-07-12 a 2026-07-19).
- **2026-08-10** — Corrida diaria de refinamiento. Confirmé `main` actualizado (fast-forward
  d739018→5b9beab, que trajo consigo el commit de la corrida de ayer) y leí `codice.md` completo:
  verifiqué la secuencia F-1 a F-468 sin huecos ni duplicados (468 filas exactas) — sigue tope exacto
  en F-468, idéntico al que ya procesó la corrida de ayer (2026-08-09) — **sin cambios sustanciales**
  en evidencia, cero fuentes nuevas registradas por `cronista`/`/trinidad`/`/seeker`/`/gossip`/
  `/marketer` en las últimas 24h. Repasé las 25 tesis contra ese mismo tope: ninguna quedó desalineada
  con el ledger vigente, y no forcé ninguna conexión de tesis nueva solo por completar el paso. La
  última revisión profunda (rutina de `cronista`, cada ~3 días, última el 2026-08-05) no vence hoy —
  cinco días sin corrida nueva, pero esa rutina no es de este proceso diario. **Cumplí el umbral de
  poda de bitácora** señalado ayer: consolidé las tres entradas de la primera semana (2026-07-12,
  2026-07-12 segunda, 2026-07-13 a 2026-07-19) en una sola entrada resumida — el detalle de cada tesis
  que crearon ya vive en 🎯 Tesis vigentes con su propia fecha, así que no se pierde información, solo
  se deja de repetir en la bitácora. Sí corrió la rutina diaria de intuición (sexta corrida desde que
  se creó el 2026-08-06): de las 141 fuentes 🟢A del ledger, 12 ya tenían lectura profunda del Lobo
  (F-6, F-53, F-55, F-56, F-66, F-82, F-107, F-122, F-148, F-220, F-230, F-236) — seleccioné al azar 3
  de las 129 restantes: F-41 (Rees & Peralta 2024, telemedicina en Perú — ya citada en tesis 9), F-303
  (Figma Inc., 8-K Q1 2026 — filing SEC ya citado en el node de tendencias) y F-434 (Junni et al. 2013,
  meta-análisis de ambidestreza organizacional — ya citada en el node de tendencias). Sumé las entradas
  13, 14 y 15 de Intuición acumulada: (13) la ventana regulatoria/de infraestructura para un canal de
  salud digital se cierra si no se invierte a la par en la competencia del recurso humano que lo opera
  (matiza tesis 9 con el hallazgo específico de Perú: brecha de competencias del recurso humano en
  telesalud, no solo de política/infraestructura); (14) un salto en NDR u otra métrica de
  retención/crecimiento no es evidencia de moat durable hasta abrir qué línea de producto específica lo
  generó — el caso Figma Q1 2026 muestra un NDR récord (139%) impulsado por monetización de créditos de
  IA, una fuente más volátil que expansión ancha de asientos (conecta con tesis 21/25 sin cambiarles
  confianza); (15) un efecto "estrella" de la literatura de management (ambidestreza, design thinking,
  etc.) suele depender de si el estudio midió desempeño con autoreporte del gerente o con un indicador
  objetivo — el meta-análisis de ambidestreza (r≈0.26, más alto con medición percibida) da un segundo
  caso independiente del mismo patrón que ya conectaba tesis 21 vía F-239/design thinking. Ninguna
  tesis de negocio cambió de confianza por esta corrida — es el mecanismo paralelo de intuición, no una
  revisión de evidencia sobre las tesis existentes. Actualicé `research/lobo/fuentes_leidas_lobo.md`
  con las tres fuentes leídas hoy. Bitácora con 26 días de historial (2026-07-20 a hoy) tras la poda de
  la primera semana — dentro de la ventana de ~30 días.
- **2026-08-12** — Corrida diaria de refinamiento (no corrió el 2026-08-11: sin commit de este proceso
  ese día, mismo patrón de brecha ya visto el 2026-08-04). Confirmé `main` actualizado (fast-forward a
  `3ead00f`, que trajo consigo el commit de la corrida del 2026-08-10) y leí `codice.md` completo:
  verifiqué la secuencia F-1 a F-468 sin huecos ni duplicados (141 fuentes 🟢A confirmadas) — sigue
  tope exacto en F-468, idéntico al que ya procesó la corrida del 2026-08-10 (última modificación real
  del archivo: 2026-08-05) — **sin cambios sustanciales** en evidencia, cero fuentes nuevas registradas
  por `cronista`/`/trinidad`/`/seeker`/`/gossip`/`/marketer` desde entonces. Repasé las 25 tesis contra
  ese mismo tope: ninguna quedó desalineada con el ledger vigente, y no forcé ninguna conexión de tesis
  nueva solo por completar el paso — la racha de "sin cambios" desde el 2026-08-05/06 ya agotó las
  conexiones razonables disponibles entre las tesis más recientes. La última revisión profunda (rutina
  de `cronista`, cada ~3 días, última el 2026-08-05) no vence hoy. Sí corrió la rutina diaria de
  intuición (séptima corrida desde que se creó el 2026-08-06): de las 141 fuentes 🟢A del ledger, 15 ya
  tenían lectura profunda del Lobo — seleccioné al azar 3 de las 126 restantes: F-91 (Cutler & Reber,
  caso Blue Cross/Blue Shield/Harvard, espiral de selección adversa), F-111 (Carr-Hill, capitación de
  atención primaria NHS) y F-243 (Fok & Weld 2024, verificabilidad de explicaciones de IA). Sumé las
  entradas 16, 17 y 18 de Intuición acumulada: (16) dar "elección" entre planes con el mismo subsidio
  puede detonar una espiral de selección adversa que colapsa el plan generoso en pocos años — heurística
  general de diseño de producto de seguros, sin tesis específica que matizar; (17) auditar qué variable
  de necesidad real queda *afuera* de una fórmula de asignación/precio, no solo si las que entran son
  plausibles — el Carr-Hill omite privación socioeconómica pese a lucir técnicamente riguroso, y esa
  omisión (no un peso mal calibrado) es la que subfinancia sistemáticamente a las zonas más pobres;
  transferible a cualquier fórmula de riesgo/pricing que `lapuerta` o Rimac calculen por reglas; (18)
  antes de invertir en explicar una decisión de IA, preguntar si la tarea es verificable — si el usuario
  no puede contrastar de forma independiente si la IA tiene razón, ninguna explicación mejora el
  desempeño complementario humano+IA; profundiza directamente la fuente que ya sostenía la regla C8
  (verificabilidad > explicabilidad) citada en tesis 22, sin cambiarle la confianza. Ninguna tesis de
  negocio cambió de confianza por esta corrida — es el mecanismo paralelo de intuición, no una revisión
  de evidencia sobre las tesis existentes. Actualicé `research/lobo/fuentes_leidas_lobo.md` con las tres
  fuentes leídas hoy. Bitácora con 24 días de historial (2026-07-20 a hoy), dentro de la ventana de ~30
  días — sin podar todavía.
- **2026-08-12 (revisión profunda, rutina `cronista` cada ~3 días)** — Leí a fondo las 5 fuentes 🟢A
  más antiguas sin revisión completa según `research/fuentes/revision_profunda.md`: F-55, F-56, F-57,
  F-58 y F-59 (todas de `/seeker` 2026-07-06, sección de estrategias de testeo del piloto
  farmacia+triage IA). Las cinco URLs (nature.com, ncbi.nlm.nih.gov, pmc.ncbi.nlm.nih.gov) están
  bloqueadas por el proxy de red de este entorno — el mismo bloqueo que ya había registrado la rutina
  diaria de intuición el 2026-08-08/09; reconstruí el contenido con búsquedas dirigidas múltiples por
  fuente (no solo el resumen de una línea), incluyendo el hallazgo de que el artículo de resultados
  reales de F-55 (Cully et al. 2017, no solo el protocolo de 2012) está indexado y accesible por
  búsqueda aunque el PDF original no lo esté. Encontré y corregí dos errores de autoría en
  `codice.md`: F-55 estaba atribuido a "Bauer, M.S. et al." (el autor principal real es Jeffrey A.
  Cully) y F-57 solo decía "PMC (framework metodológico)" (autor principal real: Jethro C.C. Kwong).
  Agregué un bloque "[Revisión profunda 2026-08-12]" a tesis 10 (tres años de aprendizaje sobre
  rigurosidad de testeo: el silent trial no tiene guías formales todavía y puede colapsar por
  distribution shift; el ejemplo tipo 2 de tesis 9 sí funcionó pero con efecto modesto y desigual por
  subgrupo; el stepped-wedge tiene una controversia metodológica activa — Kotz et al. 2012 vs.
  Mdege/Hemming — que la tesis nunca declaraba) — confianza sin cambio (Alta), matiza el proceso de
  testeo, no la dirección. Enriquecí también `research/_nodes/modelo-salud-ia-farmacias-peru.md` §4
  (E1, E2, E3) con el mismo detalle y actualicé su fila en `research/alma.md`. F-55 y F-56 ya habían
  sido leídos a fondo por la rutina diaria de intuición (entradas 10 y 11, 2026-08-08/09) — sin
  conflicto: esta rutina lee para matizar tesis/nodes, la diaria lee para heurísticas transferibles;
  el ángulo de esta corrida (resultados cuantitativos de Cully 2017, alcance del caso de Kwong,
  controversia Kotz-vs-Mdege) es nuevo en ambos casos. Actualicé
  `research/fuentes/revision_profunda.md` con las 5 fuentes de este ciclo.
- **2026-08-13** — Corrida diaria de refinamiento. Confirmé `main` actualizado (fast-forward
  d739018→a3f9789, que trajo consigo el commit de la revisión profunda del 2026-08-12) y leí
  `codice.md` completo: verifiqué la secuencia F-1 a F-468 sin huecos ni duplicados (141 fuentes 🟢A
  confirmadas) — sigue tope exacto en F-468, idéntico al que ya procesó la corrida del 2026-08-12 —
  **sin cambios sustanciales** en evidencia, cero fuentes nuevas registradas por
  `cronista`/`/trinidad`/`/seeker`/`/gossip`/`/marketer` desde entonces. Repasé las 25 tesis contra
  ese mismo tope: ninguna quedó desalineada con el ledger vigente, y no forcé ninguna conexión de
  tesis nueva solo por completar el paso. La última revisión profunda (rutina de `cronista`, cada ~3
  días, última el 2026-08-12) no vence hoy. Sí corrió la rutina diaria de intuición (octava corrida
  desde que se creó el 2026-08-06): de las 141 fuentes 🟢A del ledger, 18 ya tenían lectura profunda
  del Lobo — seleccioné al azar 3 de las 123 restantes: F-16 (Mertens et al. 2022, PNAS, el
  meta-análisis fundacional de nudging que sostiene tesis 6 solo indirectamente vía las fuentes que
  lo rebaten, nunca leído directo hasta hoy), F-151 (Es et al. 2024, RAGAS — el framework que el
  ledger ya cita como estándar para detectar alucinación del agente conversacional) y F-250 (Flohr et
  al. 2021, MobileHCI, chatbot vs. GUI clásica — ya citada en tesis 24 como contraevidencia a
  generative UI). Sumé las entradas 19, 20 y 21 de Intuición acumulada: (19) el propio F-16 ya
  corrió y reportó, sin destacarlo, un análisis de sensibilidad a sesgo de publicación que anticipaba
  el colapso del efecto que después popularizó la crítica de Maier (F-17) — la advertencia sobre el
  sesgo de un hallazgo a veces ya vive en el paper original, enterrada en un análisis secundario, no
  en el titular; (20) RAGAS (y cualquier framework LLM-as-judge) correlaciona apenas ~0.55 con juicio
  humano y hereda sesgos sistemáticos que promediar más jueces del mismo tipo no cancela — matiza
  directamente el riesgo vigente sobre medir mal al agente conversacional de Rimac: la métrica que el
  propio ledger propone como solución no es una vara neutral, necesita triangularse con revisión
  humana real; (21) el mismo estudio puede dar veredictos opuestos por escenario dentro de la misma
  tarea — GUI gana en el "camino feliz", chatbot gana específicamente en el momento de
  interrupción/cambio de plan — la pregunta correcta para un canal conversacional no es "¿cuál gana
  en promedio?" sino "¿en qué momento específico gana cada uno?", con paralelo directo al punto de
  falla de reclamos 100%-digitales ya documentado en tesis 16. Ninguna tesis de negocio cambió de
  confianza por esta corrida — es el mecanismo paralelo de intuición, no una revisión de evidencia
  sobre las tesis existentes. Actualicé `research/lobo/fuentes_leidas_lobo.md` con las tres fuentes
  leídas hoy. Bitácora con 25 días de historial (2026-07-20 a hoy), dentro de la ventana de ~30 días
  — sin podar todavía.
- **2026-08-14** — Corrida diaria de refinamiento. Confirmé `main` actualizado (sin cambios
  pendientes) y leí `codice.md` completo: verifiqué la secuencia F-1 a F-468 sin huecos ni
  duplicados (141 fuentes 🟢A confirmadas) — sigue tope exacto en F-468, idéntico al que ya procesó
  la corrida de ayer (2026-08-13) — **sin cambios sustanciales** en evidencia, cero fuentes nuevas
  registradas por `cronista`/`/trinidad`/`/seeker`/`/gossip`/`/marketer` desde entonces. Repasé las
  25 tesis contra ese mismo tope: ninguna quedó desalineada con el ledger vigente, y no forcé
  ninguna conexión de tesis nueva solo por completar el paso. La última revisión profunda (rutina de
  `cronista`, cada ~3 días, última el 2026-08-12) no vence hoy. Sí corrió la rutina diaria de
  intuición (novena corrida desde que se creó el 2026-08-06): de las 141 fuentes 🟢A del ledger, 21
  ya tenían lectura profunda del Lobo — seleccioné al azar 3 de las 120 restantes: F-89 (Pauly 1968,
  AER, el "comment" fundacional que abrió el campo del riesgo moral en seguros de salud — citado en
  el ledger solo como capa teórica de fondo, nunca leído a fondo), F-21 (DellaVigna & Linos 2022,
  *Econometrica* — ya citada en tesis 6, pero desde un ángulo distinto al que ya trabajó la revisión
  profunda de `cronista` el 2026-07-22) y F-109 (estudio DiD de gatekeeping de atención primaria en
  China, citado en el ledger solo por su cifra agregada). A diferencia de corridas anteriores, las
  URLs académicas (ldi.upenn.edu) sí fueron accesibles esta vez; onlinelibrary.wiley.com,
  sdellavi.com y pmc.ncbi.nlm.nih.gov siguieron bloqueadas por el proxy del entorno — reconstruidas
  vía búsqueda dirigida. Sumé las entradas 22, 23 y 24 de Intuición acumulada: (22) frente a
  sobreutilización de un beneficio asegurado, diagnosticar primero el precio marginal percibido, no
  la mala fe — la palanca correctora es coaseguro/deducible (cambiar el precio), no control
  antifraude (cambiar el castigo), son remedios para causas distintas; conecta con tesis 2 (mismo
  término de producto, dos mecanismos distintos: incentivo racional vs. comprensión); (23) "el efecto
  promedio del nudge murió" (tesis 6) y "vale la pena seguir corriendo experimentos de bajo costo" no
  están en tensión — son dos preguntas distintas, y un canal casi gratis (SMS, default, recordatorio)
  puede justificarse con un efecto de 1-2pp si el costo marginal de probarlo es casi cero; (24) un
  aumento de volumen en el canal barato puede ser fricción de acceso al canal caro disfrazada de
  éxito — verificar por qué cayó el canal caro (¿mejoró el barato o se volvió engorroso el caro?), no
  solo que el volumen se movió; segunda confirmación independiente, en un país y sector distintos, de
  la intuición 13 (invertir en recurso humano del canal receptor, no solo en su infraestructura),
  aplicable directamente al gate de éxito del piloto farmacia+triage IA de tesis 9. Ninguna tesis de
  negocio cambió de confianza por esta corrida — es el mecanismo paralelo de intuición, no una
  revisión de evidencia sobre las tesis existentes. Actualicé `research/lobo/fuentes_leidas_lobo.md`
  con las tres fuentes leídas hoy. Bitácora con 26 días de historial (2026-07-20 a hoy), dentro de
  la ventana de ~30 días — sin podar todavía.
- **2026-08-15** — Corrida diaria de refinamiento. Confirmé `main` actualizado (fast-forward
  8a90dc2→e0c9040, que trajo consigo el commit de la corrida de ayer) y leí `codice.md` completo:
  verifiqué la secuencia F-1 a F-468 sin huecos ni duplicados (134 fuentes 🟢A confirmadas por conteo
  propio, cifra ligeramente distinta al conteo de 141 de corridas previas por variación de método de
  conteo, no por fuentes nuevas) — sigue tope exacto en F-468, idéntico al que ya procesó la última
  modificación real del archivo (2026-08-12, revisión profunda de `cronista`) — **sin cambios
  sustanciales** en evidencia, cero fuentes nuevas registradas por
  `cronista`/`/trinidad`/`/seeker`/`/gossip`/`/marketer` desde entonces. Repasé las 25 tesis contra ese
  mismo tope: ninguna quedó desalineada con el ledger vigente, y no forcé ninguna conexión de tesis
  nueva solo por completar el paso. La última revisión profunda (rutina de `cronista`, cada ~3 días,
  última el 2026-08-12) no vence hoy — tres días sin corrida nueva. Sí corrió la rutina diaria de
  intuición (décima corrida desde que se creó el 2026-08-06): de las fuentes 🟢A del ledger, 24 ya
  tenían lectura profunda del Lobo — seleccioné 3 de las restantes: F-92 (Geruso & Layton 2017,
  selección en mercados de seguros de salud — ya citada en tesis 9/17 solo como "contrapeso" sin
  lectura completa), F-218 (Cepeda et al. 2006, práctica espaciada — citada en el deck de onboarding
  de Universidad Vida) y F-401 (Fernandes et al. 2026, brecha desempeño-metacognición con IA — ya
  citada en `_nodes/tendencias-diseno-innovacion.md` para H5). Sumé las entradas 25, 26 y 27 de
  Intuición acumulada: (25) el diseño de cobertura (no solo el precio) es un cuarto instrumento de
  selección de riesgo — un asegurador puede angostar la red/formulario de una condición cara para
  repeler ese riesgo sin tocar la tarifa regulada, canal indirecto que una auditoría centrada solo en
  precio/ajuste de riesgo no detecta; (26) el intervalo de repaso óptimo no es fijo — cae de ~20-40%
  del horizonte de retención para una prueba a 1 semana a solo ~5-10% para una prueba a 1 año, así que
  un cronograma de refuerzo debe fijarse según cuánto debe durar el conocimiento, no copiar un
  espaciado estándar; (27) mayor alfabetización en IA correlaciona con **menor** precisión al calibrar
  el propio desempeño asistido por IA — dato nuevo que el resumen de una línea del ledger no traía,
  con aplicación directa al gate de triage IA de tesis 10 y al riesgo ya vigente sobre medir mal al
  agente conversacional de Rimac. Ninguna tesis de negocio cambió de confianza por esta corrida — es
  el mecanismo paralelo de intuición, no una revisión de evidencia sobre las tesis existentes.
  Actualicé `research/lobo/fuentes_leidas_lobo.md` con las tres fuentes leídas hoy. Bitácora con 27
  días de historial (2026-07-20 a hoy), dentro de la ventana de ~30 días — sin podar todavía; la
  próxima corrida (2026-08-20, cuando la ventana llegue a ~30 días desde el 2026-07-20) debe evaluar
  podar/resumir de nuevo.
- **2026-08-16** — Corrida diaria de refinamiento. Confirmé `main` al día (`git pull` sin cambios,
  working tree limpio) y verifiqué `codice.md` por conteo directo de filas: **468 filas, F-1 a
  F-468 sin huecos**, mismo tope exacto que ya procesó la corrida de ayer (2026-08-15) — **cero
  fuentes nuevas** registradas por `cronista`/`/trinidad`/`/seeker`/`/gossip`/`/marketer` desde
  entonces, tercer día seguido sin cambios sustanciales en el ledger. Repasé las 25 tesis contra
  ese mismo tope: ninguna quedó desalineada con la evidencia vigente y no encontré matiz genuino
  que agregar — no forcé ningún bloque "[Revisión...]" solo por completar el paso (el último real
  sigue siendo el del 2026-08-12, mecanismo de `cronista`, que corre cada ~3 días y no vence hoy).
  Sí corrió la rutina diaria de intuición (undécima corrida desde el 2026-08-06): de las 154
  fuentes 🟢A del ledger, 27 ya tenían lectura profunda del Lobo — de las 127 restantes elegí 3 sin
  patrón temático deliberado: F-97 (Oskam, van Kleef & van Vliet 2023, ajuste de riesgo holandés
  por diagnóstico — citada en el ledger solo como "campo activo de mejora continua", nunca leída a
  fondo), F-143 (Fleming et al. 2023, divulgación repetida de datos — ya sostiene tesis 13, pero
  solo por su resumen de una línea) y F-432 (Victory, Nenycz-Thiel & Dawes 2021, tasa real de
  fracaso de producto nuevo — citada en el node de diseño/innovación). Las tres bloqueadas por el
  proxy en su URL directa (pmc.ncbi.nlm.nih.gov, academic.oup.com, link.springer.com);
  reconstruidas vía búsqueda dirigida contra agregadores académicos (PubMed, EconPapers, CREATe,
  ProQuest, ResearchGate) que confirman método y hallazgo, no solo el resumen ya citado. Sumé las
  entradas 28, 29 y 30 de Intuición acumulada: (28) un modelo de clasificación que fuerza "una
  persona = un bucket" por eje (como el DCG holandés, que solo permite una etiqueta de diagnóstico
  por capa) subcompensa sistemáticamente a quien combina rasgos — multimorbilidad en ese caso — y
  el arreglo correcto es de arquitectura del modelo (permitir multi-pertenencia), no de mejor
  calibración dentro de cada bucket; amplía la intuición 17 desde el ángulo de "falta de variable"
  hacia "el axioma de una sola etiqueta es en sí mismo el sesgo"; (29) que la tasa de campos
  completados suba en un formulario de divulgación progresiva no prueba que la confianza real del
  cliente subió — puede ser puro *foot-in-the-door* operando sobre la conducta mientras la actitud
  de privacidad medida no se mueve, con forewarning documentado como la contramedida ética; agrega
  precisión al mecanismo ya citado en tesis 13 sin cambiar su confianza (sigue Alta); (30) la tasa
  base de fracaso de un producto de consumo nuevo es alta y sistemática (25% al año 1, ~40% a los 2
  años, medida en panel de ventas real sobre 83.719 SKU, no en encuesta) y predecible antes de
  lanzar por dos factores — categoría de alta rotación y marca matriz débil — así que un
  post-mortem debe descartar primero esos dos factores estructurales antes de inventar una
  explicación a medida; transferible a cualquier lanzamiento propio (producto sísmico de tesis 4,
  extensiones de `lapuerta` a microseguro). Ninguna tesis de negocio cambió de confianza por esta
  corrida — es el mecanismo paralelo de intuición, no una revisión de evidencia sobre las tesis
  existentes. Actualicé `research/lobo/fuentes_leidas_lobo.md` con las tres fuentes leídas hoy.
  Bitácora con 28 días de historial (2026-07-20 a hoy), dentro de la ventana de ~30 días — sin
  podar todavía; la corrida del 2026-08-20 sigue siendo la programada para evaluar podar/resumir.
- **2026-08-17** — Corrida diaria de refinamiento. Confirmé `main` al día (`git pull` trajo
  fast-forward 8a90dc2→3acec5d, el commit de la corrida de ayer, 2026-08-16) y verifiqué
  `codice.md` por conteo directo: **468 filas, F-1 a F-468 sin huecos ni duplicados**, mismo tope
  exacto que procesó la corrida de ayer — **cero fuentes nuevas** registradas por
  `cronista`/`/trinidad`/`/seeker`/`/gossip`/`/marketer` desde entonces, cuarto día seguido sin
  cambios sustanciales en el ledger. Repasé las 25 tesis contra ese mismo tope: ninguna quedó
  desalineada con la evidencia vigente y no forcé ningún matiz solo por completar el paso — el
  último bloque "[Revisión...]" real sigue siendo el del 2026-08-12 (mecanismo de `cronista`,
  cada ~3 días, no vence hoy). Sí corrió la rutina diaria de intuición (duodécima corrida desde el
  2026-08-06): de 136 fuentes 🟢A confirmadas por conteo propio en el ledger, 30 ya tenían lectura
  profunda del Lobo — de las 106 restantes elegí 3 deliberadamente ancladas a tesis existentes que
  solo tenían el resumen de una línea nunca leído a fondo, en vez de al azar puro: F-119
  (Scheibehenne, Greifeneder & Todd 2010, meta-análisis fundacional de choice overload que
  sostiene tesis 12), F-180 (Cummins & Doherty 2006, marco causal de "market maker" que sostiene
  tesis 16) y F-198 (filing SEC de UnitedHealth Q2 2026, evidencia primaria de tesis 17). Las tres
  bloqueadas por el proxy en su URL directa (academic.oup.com, onlinelibrary.wiley.com, sec.gov,
  businesswire.com); reconstruidas vía búsqueda dirigida contra agregadores (ResearchGate,
  Academia.edu, JSTOR, IDEAS/RePEc, TradingView, StockTitan, 24/7 Wall St.) que confirman detalle
  nuevo, no solo el resumen ya citado. Sumé las entradas 31, 32 y 33 de Intuición acumulada: (31)
  un metaanálisis con efecto promedio cero (F-119, base de tesis 12) tiene una réplica activa y no
  zanjada (Chernev, Böckenholt & Goodman 2015) que encuentra el efecto sí presente bajo cuatro
  condiciones — complejidad, dificultad de tarea, incertidumbre de preferencia, meta de
  exploración vs. elección — que el catálogo de seguros probablemente cumple; no baja la confianza
  de tesis 12 pero acota su alcance; (32) la comisión de un intermediario (F-180, marco de tesis
  16) no es solo el precio de la distribución/confianza — la comisión contingente alinea
  incentivos y rompe el "winner's curse", empujando a los aseguradores a competir más agresivo en
  precio por ese negocio; quitar al intermediario sin sustituto de ese mecanismo puede subir el
  precio final aunque desaparezca la comisión visible; (33) la utilidad de Optum Rx (F-198,
  evidencia central de tesis 17) subió en el mismo trimestre en que su propio volumen de scripts
  cayó 6,5% por contracción de membresía en su aseguradora hermana — el crecimiento vino de mezcla
  hacia farmacia especializada, no de más asegurados, una exposición a shock regulatorio de precio
  de especialidad que la tesis tal como está escrita no cubre. Ninguna tesis de negocio cambió de
  confianza numérica por esta corrida — es el mecanismo paralelo de intuición, no una revisión de
  evidencia sobre las tesis existentes, aunque las tres entradas de hoy sí acotan el alcance de
  tesis 12, 16 y 17 sin tocar su nivel de confianza. Actualicé `research/lobo/fuentes_leidas_lobo.md`
  con las tres fuentes leídas hoy. Bitácora con 29 días de historial (2026-07-20 a hoy), dentro de
  la ventana de ~30 días — sin podar todavía; la corrida del 2026-08-20 sigue siendo la programada
  para evaluar podar/resumir.
- **2026-08-18** — Corrida diaria de refinamiento. Confirmé `main` al día (`git pull` trajo
  fast-forward cf8c4a7 sobre el commit de ayer, working tree limpio) y verifiqué `codice.md` por
  conteo directo: **468 filas, F-1 a F-468 sin huecos ni duplicados**, mismo tope exacto que
  procesó la corrida de ayer — **cero fuentes nuevas** registradas por
  `cronista`/`/trinidad`/`/seeker`/`/gossip`/`/marketer` desde entonces, quinto día seguido sin
  cambios sustanciales en el ledger. Repasé las 25 tesis contra ese mismo tope: ninguna quedó
  desalineada con la evidencia vigente y no forcé ningún matiz solo por completar el paso — el
  último bloque "[Revisión...]" real sigue siendo el del 2026-08-12 (mecanismo de `cronista`, cada
  ~3 días, no vence hoy). Sí corrió la rutina diaria de intuición (decimotercera corrida desde el
  2026-08-06): de 134 fuentes 🟢A confirmadas por conteo propio en el ledger, 33 ya tenían lectura
  profunda del Lobo — de las 110 restantes elegí 3 ancladas a tesis existentes que solo tenían el
  resumen de una línea nunca leído a fondo: F-141 (Freedman & Fraser 1966, el estudio fundacional
  de pie-en-la-puerta que ya sostiene tesis 13, pero solo por su Experimento 1), F-100 (Vlaev et
  al. 2019, revisión de incentivos financieros en salud, citada solo como "contrapeso" a Discovery
  Vitality/F-99 sin lectura completa) y F-150 (Borsci & Schmettow 2024, escala BUS-11 de
  usabilidad de chatbots, citada solo como "la más parecida al caso Rimac" sin detalle de sus
  subescalas). Las tres bloqueadas por el proxy en su URL directa (bulidomics.com,
  link.springer.com, dl.acm.org); reconstruidas vía búsqueda dirigida contra agregadores (MIT/
  curhan.mit.edu, PubMed, ResearchGate, JMIR Human Factors) que confirman detalle nuevo, no solo
  el resumen ya citado. Sumé las entradas 34, 35 y 36 de Intuición acumulada: (34) el efecto
  pie-en-la-puerta del Experimento 2 de Freedman & Fraser sobrevive incluso cuando el pedido chico
  y el grande son de temas no relacionados (48% de aceptación vs. 17% base, contra 76% cuando sí
  comparten tema) — amplía dónde aplica la advertencia ética ya declarada en tesis 13, sin
  cambiar su confianza; (35) un incentivo financiero de salud tiende a disipar su efecto dentro de
  los ~3 meses posteriores a retirarlo salvo que ya se haya vuelto hábito por otra vía — precisa
  por qué tesis 7 (UBI/telemática) exige feedback+incentivo combinados y no incentivo puro; (36) la
  usabilidad percibida de un chatbot comercial se descompone en cinco palancas casi independientes
  de la calidad del modelo (accesibilidad, calidad de interacción, calidad de información,
  privacidad/seguridad, tiempo de respuesta) — da un marco de diagnóstico concreto para cuando el
  proyecto evalúe el agente conversacional de Rimac, con dos de las cinco palancas más baratas de
  arreglar que "mejorar el modelo". Ninguna tesis de negocio cambió de confianza por esta corrida
  — es el mecanismo paralelo de intuición, no una revisión de evidencia sobre las tesis existentes.
  Actualicé `research/lobo/fuentes_leidas_lobo.md` con las tres fuentes leídas hoy. Bitácora con 30
  días de historial (2026-07-20 a hoy) — cumple la ventana de ~30 días; podé/resumí las entradas
  del 2026-07-20 al 2026-07-31 en un solo bloque resumido para mantener el archivo legible, y dejo
  el detalle completo desde 2026-08-01 en adelante.
- **2026-08-19** — Corrida diaria de refinamiento. Confirmé `main` al día (`git pull` trajo
  fast-forward 8a90dc2→ccba768, el commit de la corrida de ayer, working tree limpio) y verifiqué
  `codice.md` por conteo directo: **468 filas, F-1 a F-468 sin huecos ni duplicados**, mismo tope
  exacto que procesó la corrida de ayer — **cero fuentes nuevas** registradas por
  `cronista`/`/trinidad`/`/seeker`/`/gossip`/`/marketer` desde entonces, sexto día seguido sin
  cambios sustanciales en el ledger. Repasé las 25 tesis contra ese mismo tope: ninguna quedó
  desalineada con la evidencia vigente y no forcé ningún matiz solo por completar el paso — el
  último bloque "[Revisión...]" real sigue siendo el del 2026-08-12 (mecanismo de `cronista`, cada
  ~3 días, no vence hoy — siete días sin corrida nueva). Sí corrió la rutina diaria de intuición
  (decimocuarta corrida desde el 2026-08-06): de 137 fuentes 🟢A confirmadas por conteo propio en el
  ledger, 36 ya tenían lectura profunda del Lobo — de las 101 restantes elegí 3 al azar puro (sin
  anclar a tesis existentes, a diferencia de las últimas corridas): F-334 (estudio holandés 2025,
  confianza del consumidor en el asegurador como comprador prudente de atención — citado en el
  ledger solo por su hallazgo de conflicto de interés, nunca leído a fondo), F-87 (Callaway et al.
  2025, BMC Public Health, envejecimiento poblacional y longevidad) y F-428 (filing 8-K de Accenture
  Q3 FY26, citado solo por el hallazgo negativo de que Song no se reporta como segmento separado).
  Las tres bloqueadas por el proxy en su URL directa (cambridge.org, link.springer.com, sec.gov, el
  último ya señalado como bloqueo conocido en el propio ledger); reconstruidas vía búsqueda dirigida
  (el buscador indexó directamente los hallazgos centrales de F-334 y F-87 pese al bloqueo de la
  URL; F-428 se reconstruyó contra cobertura de prensa financiera — Investing.com, Motley Fool,
  Yahoo Finance) que confirman detalle nuevo, no solo el resumen ya citado. Sumé las entradas 37, 38
  y 39 de Intuición acumulada: (37) la desconfianza en un asegurador no siempre es un veredicto
  negativo ya formado — puede ser un vacío de información que el consumidor no puede llenar, y por
  default asume el peor marco ("puramente comercial"); distinción de mecanismo que matiza tesis 1
  sin cambiarle la confianza; (38) las ganancias de esperanza de vida se están desacelerando en
  países de altos ingresos, sobre todo en los más viejos — chequeo de higiene antes de fijar
  cualquier supuesto actuarial de longevidad como tendencia lineal indefinida; (39) un beat de
  ingresos no neutraliza un indicador líder que empeora (bookings, guía) cuando hay una narrativa de
  disrupción estructural plausible detrás — el caso Accenture (caída de ~18-20% en un día pese a
  +6% de ingresos, por sustitución de trabajo facturable por IA) es una señal de vigilancia activa
  para tesis 16, no solo una curiosidad de otro sector. Ninguna tesis de negocio cambió de confianza
  por esta corrida — es el mecanismo paralelo de intuición, no una revisión de evidencia sobre las
  tesis existentes, aunque la entrada 39 sí liga una amenaza estructural concreta (sustitución de
  trabajo facturable por IA) a la vigilancia futura de tesis 16. Actualicé
  `research/lobo/fuentes_leidas_lobo.md` con las tres fuentes leídas hoy. Bitácora con 31 días de
  historial (2026-07-20 a hoy), dentro de la ventana de ~30 días — sin podar todavía; evaluar poda
  de la primera semana del bloque actual (2026-08-01 a 2026-08-07) en las próximas corridas si la
  ventana sigue creciendo.
- **2026-08-20** — Corrida diaria de refinamiento. Confirmé `main` al día (`git pull` trajo
  fast-forward 8a90dc2→bb8062c, el commit de la corrida de ayer, working tree limpio) y verifiqué
  `codice.md` por conteo directo: **468 filas, F-1 a F-468 sin huecos ni duplicados**, mismo tope
  exacto que procesó la corrida de ayer (2026-08-19) — **cero fuentes nuevas** registradas por
  `cronista`/`/trinidad`/`/seeker`/`/gossip`/`/marketer` desde entonces, séptimo día seguido sin
  cambios sustanciales en el ledger. Repasé las 25 tesis contra ese mismo tope: ninguna quedó
  desalineada con la evidencia vigente y no forcé ningún matiz solo por completar el paso — el
  último bloque "[Revisión...]" real sigue siendo el del 2026-08-12 (mecanismo de `cronista`, cada
  ~3 días, no vence hoy — ocho días sin corrida nueva, pero esa rutina no es de este proceso
  diario). Sí corrió la rutina diaria de intuición (decimoquinta corrida desde el 2026-08-06): de
  134 fuentes 🟢A confirmadas por conteo propio en el ledger, 39 ya tenían lectura profunda del Lobo
  — de las 95 restantes elegí 3 al azar puro: F-147 (Walker, Litman, Kamm & Abella 1997, PARADISE —
  framework de evaluación de diálogo hablado, citado en el ledger solo por su resumen de una
  línea), F-176 (Romani 2006, publicidad de precio engañosa — ya sostiene tesis 15, pero solo por
  su resumen) y F-246 (Vasconcelos et al. 2023, explicaciones y sobreconfianza en IA — ya citada en
  el node de diseño/innovación para la regla C8). Las tres bloqueadas por el proxy en su URL
  directa (aclanthology.org, researchgate.net, hci.stanford.edu); reconstruidas vía búsqueda
  dirigida (arXiv, Emerald/DeepDyve/Scribd, el paper de seguimiento de PARADISE en *Computational
  Linguistics* 2006) que confirman detalle nuevo — los pesos exactos de la regresión de PARADISE, la
  tipología de ocho prácticas y el moderador de sospecha de Romani, el diseño de los 5 estudios de
  Vasconcelos — no solo el resumen ya citado. Sumé las entradas 40, 41 y 42 de Intuición acumulada:
  (40) en un agente conversacional, si el sistema entendió bien lo que dijo el usuario puede pesar
  más en la satisfacción percibida que si completó la tarea (PARADISE: reconocimiento .45 > éxito
  de tarea .33 > tiempo -.14 en su regresión original) — profundiza el riesgo ya vigente sobre medir
  mal al agente de Rimac (intuición 8/20/21/36) con un eje de medición concreto que faltaba; (41) el
  daño de una publicidad de precio incompleta o ambigua se concentra en quien ya desconfía, no se
  reparte parejo en la audiencia — conecta tesis 1 (48% desconfía) con tesis 15 (riesgo del flyer
  "a confirmar"): el segmento más caro de convertir es también el que más castiga la pieza mal
  hecha; (42) la sobreconfianza en una respuesta de IA es una decisión estratégica de
  costo-beneficio, no un sesgo automático — las explicaciones solo reducen sobreconfianza en tareas
  objetivamente difíciles, no en las rutinarias, lo que da un criterio operacional (dificultad de la
  tarea) para priorizar dónde invertir en explicabilidad primero; profundiza la intuición 18 sin
  cambiarle la confianza. Ninguna tesis de negocio cambió de confianza numérica por esta corrida —
  es el mecanismo paralelo de intuición, no una revisión de evidencia sobre las tesis existentes,
  aunque las tres entradas de hoy sí conectan con riesgos y tesis ya vigentes (8/20/21/36, 1/15, 18).
  Actualicé `research/lobo/fuentes_leidas_lobo.md` con las tres fuentes leídas hoy. Bitácora con 32
  días de historial (2026-07-20 a hoy), dentro de la ventana de ~30 días pero ya en su borde — la
  próxima corrida (2026-08-21) debe evaluar podar/resumir la primera semana del bloque actual
  (2026-08-01 a 2026-08-07) para no seguir creciendo por encima del umbral.
- **2026-08-21** — Corrida diaria de refinamiento. Confirmé `main` al día (`git pull` trajo
  fast-forward 8a90dc2→e8ba645, el commit de la corrida de ayer, working tree limpio) y verifiqué
  `research/fuentes/codice.md` por conteo directo: **468 filas, F-1 a F-468 sin huecos ni
  duplicados**, mismo tope exacto que procesó la corrida de ayer (2026-08-20) — **cero fuentes
  nuevas** registradas por `cronista`/`/trinidad`/`/seeker`/`/gossip`/`/marketer` desde entonces,
  octavo día seguido sin cambios sustanciales en el ledger. Repasé las 25 tesis contra ese mismo
  tope: ninguna quedó desalineada con la evidencia vigente y no forcé ningún matiz solo por
  completar el paso — el último bloque "[Revisión...]" real sigue siendo el del 2026-08-12
  (mecanismo de `cronista`, cada ~3 días, no vence formalmente hoy pero ya lleva nueve días sin
  correr; no lo disparo aquí porque es rutina de `cronista`, no de este proceso diario). **Cumplí
  el umbral de poda señalado ayer:** consolidé las siete entradas de la primera semana del bloque
  actual (2026-08-01 a 2026-08-07) en un solo bloque resumido — el detalle de cada tesis e
  intuición que generaron ya vive en sus propias secciones con fecha, así que no se pierde
  información, solo se deja de repetir en la bitácora; queda el detalle completo desde 2026-08-08
  en adelante. Sí corrió la rutina diaria de intuición (decimosexta corrida desde el 2026-08-06):
  de 134 fuentes 🟢A confirmadas por conteo propio en el ledger, 42 ya tenían lectura profunda del
  Lobo — de las 92 restantes elegí 3 al azar puro: F-449 (Root, Inc., filings SEC — combined ratio
  91,4% Q3 2025, ya citado en tesis 25 solo por la cifra agregada), F-338 (Bundorf, Polyakova &
  Tai-Seale 2024, *Management Science*, RCT de consejo digital en seguro de salud, citado en un
  documento externo del usuario solo por su hallazgo de disposición a pagar) y F-222 (Tversky &
  Kahneman 1981, *Science*, framing — ya citado en tesis 18/C.8 solo por su mecanismo general). Las
  tres bloqueadas por el proxy en su URL directa (ir.joinroot.com/sec.gov,
  pubsonline.informs.org, science.org); reconstruidas vía búsqueda dirigida (cobertura financiera
  especializada para F-449; el working paper del NBER "How do Humans Interact with Algorithms?"
  para F-338, mismos autores/hallazgo; agregadores de acceso abierto — MPRA, journal.sjdm.org —
  para F-222, incluyendo una réplica de condiciones límite del framing nunca antes citada en el
  ledger) que confirman detalle nuevo, no solo el resumen ya citado. Sumé las entradas 43, 44 y 45
  de Intuición acumulada: (43) un combined ratio rentable auditado combina un modelo de riesgo que
  se sigue reentrenando (Root: UBI ~10% más predictivo tras 36,000 millones de millas) con un
  cambio simultáneo hacia mezcla de canal más barata (partnerships embebidos, 44% de pólizas
  nuevas) — da el criterio de auditoría operacional que tesis 25 todavía no tenía explícito para
  cuando algún lab peruano publique cifra propia; (44) la divulgación pasiva (tesis 1) y el consejo
  digital activo/recomendador no son el mismo objeto de estudio — el segundo desplaza el peso que
  marca/reputación tiene sobre la disposición a pagar, cambia los pesos de decisión, no solo
  informa; acota el alcance de tesis 1 sin bajarle la confianza, y hereda el riesgo ético ya
  declarado en tesis 13 si se aplica a un comparador propio; (45) el efecto de framing no tiene
  magnitud fija citable de memoria — se debilita bajo presión de tiempo y se invierte según el
  tamaño de lo que está en juego, con paralelo directo al error de sobregeneralización que tesis 6
  ya corrigió para el nudging; acota el alcance operacional de C.8 en tesis 18 sin cambiar su
  confianza. Ninguna tesis de negocio cambió de confianza numérica por esta corrida — es el
  mecanismo paralelo de intuición, no una revisión de evidencia sobre las tesis existentes, aunque
  las tres entradas de hoy sí acotan el alcance de tesis 25, 1 y 18. Actualicé
  `research/lobo/fuentes_leidas_lobo.md` con las tres fuentes leídas hoy. Bitácora con 14 días de
  historial (2026-08-08 a hoy) tras la poda de la primera semana del bloque actual — dentro de la
  ventana de ~30 días.
- **2026-08-22** — Corrida diaria de refinamiento. Confirmé `main` al día (`git pull` sin cambios
  pendientes, working tree limpio) y verifiqué `research/fuentes/codice.md` por conteo directo:
  **468 filas, F-1 a F-468 sin huecos ni duplicados**, mismo tope exacto que procesó la corrida de
  ayer (2026-08-21) — **cero fuentes nuevas** registradas por
  `cronista`/`/trinidad`/`/seeker`/`/gossip`/`/marketer` desde entonces, noveno día seguido sin
  cambios sustanciales en el ledger. Repasé las 25 tesis contra ese mismo tope: ninguna quedó
  desalineada con la evidencia vigente y no forcé ningún matiz solo por completar el paso — el
  último bloque "[Revisión...]" real sigue siendo el del 2026-08-12 (mecanismo de `cronista`, cada
  ~3 días, no vence formalmente hoy pero ya lleva diez días sin correr; no lo disparo aquí porque
  es rutina de `cronista`, no de este proceso diario). Sí corrió la rutina diaria de intuición
  (decimoséptima corrida desde el 2026-08-06): de 137 fuentes 🟢A confirmadas por conteo propio en
  el ledger, 45 ya tenían lectura profunda del Lobo — de las 92 restantes elegí 3 al azar puro:
  F-121 (Iyengar & Lepper 2000, el estudio original de las mermeladas/choice overload — ya citado
  en tesis 12 solo por su resumen con la salvedad de no-replicación), F-239 (Roth et al. 2020,
  mediación de empoderamiento psicológico en el efecto de design thinking — ya citado en el node de
  diseño/innovación solo por su hallazgo agregado) y F-355 (Gotthardt et al. 2024, Press Ganey
  telesalud vs. presencial en pediatría — ya citado en un documento externo del usuario solo por la
  cifra agregada). Las tres bloqueadas por el proxy en su URL directa (medium.com,
  onlinelibrary.wiley.com, journals.sagepub.com); reconstruidas vía búsqueda dirigida (Columbia
  Business School, ResearchGate, Quizlet para F-121; ResearchGate y coberturas académicas para
  F-239; PubMed para F-355) que confirman detalle nuevo — los tres experimentos empaquetados en el
  paper de Iyengar/Lepper (mermeladas, ensayo universitario, chocolates), los cuatro mecanismos
  exactos de empoderamiento del paper de Roth et al., y qué mide exactamente el instrumento Press
  Ganey — no solo el resumen ya citado. Sumé las entradas 46, 47 y 48 de Intuición acumulada: (46)
  el estudio fundacional de choice overload en realidad reporta tres outcomes distintos (¿elegir o
  no?, ¿qué tan buena la elección?, ¿qué tan satisfecho queda?) bajo un solo titular — verificar
  cuál de los tres sobrevive antes de citar el efecto agregado, aplicable directo a cualquier
  prueba propia de "menos planes convierten mejor"; (47) que un método con marca (design thinking,
  un playbook de venta) muestre resultados reales no prueba que el método sea insustituible — si el
  efecto está totalmente mediado por un mecanismo genérico (aquí, empoderamiento psicológico vía
  contacto con usuario real, competencia, autonomía, impacto visible), cualquier práctica más
  barata que active ese mismo mecanismo debería funcionar igual, así que la decisión de negocio no
  es "adoptar ese framework específico" sino "diseñar la práctica más barata que entregue el mismo
  mecanismo"; (48) un canal de atención puede puntuar igual o mejor en satisfacción de
  paciente/padre (Press Ganey/CAHPS) sin que eso diga nada sobre si el resultado clínico también
  fue igual o mejor — el instrumento mide experiencia percibida con el proveedor, no precisión
  diagnóstica, así que cualquier gate de éxito del piloto farmacia+triage IA debe exigir métrica
  clínica junto a la de satisfacción, no solo la segunda. Ninguna tesis de negocio cambió de
  confianza numérica por esta corrida — es el mecanismo paralelo de intuición, no una revisión de
  evidencia sobre las tesis existentes, aunque las tres entradas de hoy sí acotan el alcance de
  tesis 12, 21 y 9/10/23. Actualicé `research/lobo/fuentes_leidas_lobo.md` con las tres fuentes
  leídas hoy. Bitácora con 15 días de historial (2026-08-08 a hoy), dentro de la ventana de ~30
  días — sin podar todavía.
- **2026-08-23** — Corrida diaria de refinamiento. Confirmé `main` al día (`git pull` trajo
  fast-forward 6324fc0→8cc091a, el commit de la corrida de ayer, working tree limpio) y verifiqué
  `research/fuentes/codice.md` por conteo directo: **468 filas, F-1 a F-468 sin huecos ni
  duplicados**, mismo tope exacto que procesó la corrida de ayer (2026-08-22) — **cero fuentes
  nuevas** registradas por `cronista`/`/trinidad`/`/seeker`/`/gossip`/`/marketer` desde entonces,
  décimo día seguido sin cambios sustanciales en el ledger. Repasé las 25 tesis contra ese mismo
  tope: ninguna quedó desalineada con la evidencia vigente y no forcé ningún matiz solo por
  completar el paso — el último bloque "[Revisión...]" real sigue siendo el del 2026-08-12
  (mecanismo de `cronista`, cada ~3 días, no vence formalmente hoy pero ya lleva once días sin
  correr; no lo disparo aquí porque es rutina de `cronista`, no de este proceso diario). Sí corrió
  la rutina diaria de intuición (decimoctava corrida desde el 2026-08-06): de 134 fuentes 🟢A
  confirmadas por conteo propio en el ledger, 48 ya tenían lectura profunda del Lobo — de las 86
  restantes elegí 3 al azar puro: F-164 (Louaas & Picard 2026, diseño óptimo de seguro paramétrico —
  ya citado en tesis 4 solo por el resumen "diseño óptimo de trigger"), F-125 (Berger & Calabrese
  1975, Uncertainty Reduction Theory — ya citado en el node de material visual solo como encuadre
  teórico) y F-175 (Zong & Guo 2022, efecto ancla en juicio de precio bajo experiencia de producto —
  ya citado en tesis 15 solo por el resumen del efecto base). Las tres bloqueadas por el proxy en su
  URL directa (arxiv.org/hal.science, en.wikipedia.org/pressbooks.montgomerycollege.edu/
  onlinelibrary.wiley.com, ncbi.nlm.nih.gov/frontiersin.org); reconstruidas vía búsqueda dirigida
  (SSRN, ResearchGate, IDEAS/RePEc para F-164; iResearchNet, Businesstopia, Communication Theory.org,
  ERIC para F-125; ResearchGate, PhilPapers para F-175) que confirman detalle nuevo, no solo el
  resumen ya citado. Sumé las entradas 49, 50 y 51 de Intuición acumulada: (49) un trigger
  paramétrico más preciso reduce el basis risk pero no garantiza un contrato más eficiente si el
  residuo queda correlacionado con el índice de pérdida — acota tesis 4 sin bajarle la confianza;
  (50) antes de importar una teoría canónica como marco explicativo, verificar si una teoría rival
  ya la desplazó en una prueba de cabeza a cabeza — URT (base teórica del node de material visual)
  perdió esa prueba contra Predicted Outcome Value Theory (Sunnafrank), lo que sugiere que el
  mecanismo a optimizar en venta consultiva remota es señalizar valor esperado, no solo reducir
  incertidumbre; (51) el efecto ancla de una cifra headline no golpea parejo a la audiencia — se
  concentra en quien decide con presión de tiempo, baja confianza o menos conocimiento, acotando el
  criterio de riesgo/segmentación de tesis 15 sin bajarle la confianza. Ninguna tesis de negocio
  cambió de confianza numérica por esta corrida — es el mecanismo paralelo de intuición, no una
  revisión de evidencia sobre las tesis existentes, aunque las tres entradas de hoy sí acotan el
  alcance de tesis 4, 15 y (por conexión de node, no de tesis numerada) el marco del material visual
  de venta consultiva. Actualicé `research/lobo/fuentes_leidas_lobo.md` con las tres fuentes leídas
  hoy. Bitácora con 16 días de historial (2026-08-08 a hoy), dentro de la ventana de ~30 días — sin
  podar todavía.
- **2026-08-24** — Corrida diaria de refinamiento. Confirmé `main` al día (`git pull` trajo
  fast-forward 6324fc0→396f4cc, el commit de la corrida de ayer, working tree limpio) y verifiqué
  `research/fuentes/codice.md` por conteo directo: **468 filas, F-1 a F-468 sin huecos ni
  duplicados**, mismo tope exacto que procesó la corrida de ayer (2026-08-23) — **cero fuentes
  nuevas** registradas por `cronista`/`/trinidad`/`/seeker`/`/gossip`/`/marketer` desde entonces,
  undécimo día seguido sin cambios sustanciales en el ledger. Repasé las 25 tesis contra ese mismo
  tope: ninguna quedó desalineada con la evidencia vigente y no forcé ningún matiz solo por
  completar el paso — el último bloque "[Revisión...]" real sigue siendo el del 2026-08-12
  (mecanismo de `cronista`, cada ~3 días, ya lleva doce días sin correr; no lo disparo aquí porque
  es rutina de `cronista`, no de este proceso diario). Sí corrió la rutina diaria de intuición
  (decimonovena corrida desde el 2026-08-06): de 134 fuentes 🟢A confirmadas por conteo propio en el
  ledger, 51 ya tenían lectura profunda del Lobo — de las 83 restantes elegí 3 al azar puro: F-9
  (Adams, Hunt, Palmer & Zaliauskas 2021, RCT de divulgación financiera N≈124,000 — ya sostiene
  tesis 1, con revisión profunda de `cronista` del 2026-07-21 sobre el mecanismo, pero sin lectura a
  fondo propia del Lobo hasta hoy), F-329 (examiner design, línea de asesoría de enfermería VA — ya
  citado en documento externo del usuario solo por la cifra agregada de ahorro) y F-335 (Zheng et
  al. 2002, escala HITS de confianza en aseguradores — ya citada solo por sus cuatro componentes).
  Las tres bloqueadas por el proxy en su URL directa (sciencedirect.com ×2, pmc.ncbi.nlm.nih.gov,
  nber.org, web.mit.edu); reconstruidas vía búsqueda dirigida (NBER WP 25718, J-PAL, EconPapers para
  F-9; cobertura académica del examiner design y el marco de error simétrico entre enfermeras para
  F-329; PubMed, ResearchGate y el resumen del propio journal para F-335) que confirman detalle
  nuevo — la uniformidad del efecto nulo por edad/saldo en F-9, el marco de dos errores simétricos
  (sobre-refiere vs. sub-refiere) en F-329, y la escala final de 11 ítems con dos muestras de
  validación en F-335 — no solo el resumen ya citado. Sumé las entradas 52, 53 y 54 de Intuición
  acumulada: (52) un efecto nulo de divulgación parejo entre segmentos (no concentrado en ninguno)
  descarta "hace falta segmentar mejor" como arreglo — la corrección correcta es sobre la creencia
  previa, no el formato; acota tesis 1 con un criterio operacional que la revisión profunda de
  `cronista` no había registrado, sin bajarle la confianza; (53) un sistema de triaje/gatekeeping
  puede fallar en dos direcciones simétricas (sobre-cautela costosa, sobre-confianza peligrosa) —
  medir solo el ahorro de costo esconde la segunda, reforzando con evidencia de otro dominio (triaje
  humano) el mismo gate de seguridad que tesis 10 ya exige para el piloto farmacia+IA; (54) existe un
  instrumento validado y corto (HITS, 11 ítems, <10 min, dos muestras de validación) para medir
  confianza en un asegurador por sus cuatro componentes — operacionalizable en `lapuerta` o en
  cualquier encuesta futura en vez de una pregunta ad hoc de sí/no. Ninguna tesis de negocio cambió
  de confianza numérica por esta corrida — es el mecanismo paralelo de intuición, no una revisión de
  evidencia sobre las tesis existentes, aunque las tres entradas de hoy sí acotan el alcance de tesis
  1 y 10, y dan una herramienta operacional nueva sin tesis numerada asociada (F-335/HITS).
  Actualicé `research/lobo/fuentes_leidas_lobo.md` con las tres fuentes leídas hoy. Bitácora con 17
  días de historial (2026-08-08 a hoy), dentro de la ventana de ~30 días — sin podar todavía.
- **2026-08-25** — Corrida diaria de refinamiento. Confirmé `main` al día (`git pull` trajo
  fast-forward 6324fc0→4d6b7c5, el commit de la corrida de ayer, working tree limpio) y verifiqué
  `research/fuentes/codice.md` por conteo directo: **468 filas, F-1 a F-468 sin huecos**, mismo tope
  exacto que procesó la corrida de ayer (2026-08-24) — **cero fuentes nuevas** registradas por
  `cronista`/`/trinidad`/`/seeker`/`/gossip`/`/marketer` desde entonces, duodécimo día seguido sin
  cambios sustanciales en el ledger. Repasé las 25 tesis contra ese mismo tope: ninguna quedó
  desalineada con la evidencia vigente y no forcé ningún matiz solo por completar el paso — el último
  bloque "[Revisión...]" real sigue siendo el del 2026-08-12 (mecanismo de `cronista`, cada ~3 días,
  ya lleva trece días sin correr; no lo disparo aquí porque es rutina de `cronista`, no de este
  proceso diario). Sí corrió la rutina diaria de intuición (vigésima corrida desde el 2026-08-06): de
  134 fuentes 🟢A confirmadas por conteo propio en el ledger, 54 ya tenían lectura profunda del Lobo —
  de las 80 restantes elegí 3 al azar puro (`shuf` sobre la lista completa): F-237 (Hertenstein, Platt
  & Veryzer 2005, diseño industrial y desempeño financiero — ya citada en el node de diseño solo como
  evidencia base del vínculo diseño→desempeño), F-238 (2025, capacidad diseño-ingeniería vía patentes,
  1.659 firmas — ya citada como "la mejor evidencia disponible" del mismo node) y F-349 (ProPublica/
  Capitol Forum sobre EviCore — ya citada en documento externo del usuario solo por la narrativa
  general de conflicto de interés que refuerza tesis 23). Las dos primeras bloqueadas por el proxy en
  su URL directa (onlinelibrary.wiley.com, tandfonline.com); reconstruidas vía ResearchGate y
  cobertura académica que confirman detalle nuevo — la comparación intra-industria (no cruzada) del
  panel de 138 expertos en F-237, y la distinción entre efecto directo y efecto moderador (condicionado
  a cuánta innovación ya existe) en F-238. F-349 no tenía URL directa registrada en el ledger;
  reconstruida vía búsqueda dirigida que confirma el mecanismo operativo exacto: contratos que pagan
  más cuanto mayor la denegación, y un algoritmo interno ("the dial") que ex-empleados dicen se ajusta
  para cumplir metas de ahorro sin que el asegurador cliente lo sepa. Sumé las entradas 55, 56 y 57 de
  Intuición acumulada: (55) un estudio correlacional merece menos descuento de confianza cuando la
  comparación ya viene controlada por el confusor más obvio (aquí, industria) — matiza cómo leer una de
  las piezas base de tesis 21 sin bajarle la confianza; (56) un efecto "directo" y uno "moderador"
  sobre el mismo resultado no se acumulan igual — el moderador solo rinde si la otra variable (aquí,
  innovación) ya está presente en cantidad, útil para argumentar ROI de diseño según cuánto invierte ya
  la organización en I+D; (57) frente a un intermediario algorítmico cuyo contrato premia la métrica
  que él mismo reporta, la auditoría correcta pregunta qué palanca interna puede mover sin que el
  principal se entere y con qué frecuencia — agrega a tesis 10 un criterio de gobernanza concreto (quién
  controla el "dial") que su gate de validación clínica no cubría, y documenta con evidencia dura el
  incentivo financiero detrás del steering algorítmico que tesis 23 ya señalaba como riesgo de
  reactancia. Ninguna tesis de negocio cambió de confianza numérica por esta corrida — es el mecanismo
  paralelo de intuición, no una revisión de evidencia sobre las tesis existentes, aunque las tres
  entradas de hoy sí acotan el alcance de tesis 10, 21 y 23. Actualicé
  `research/lobo/fuentes_leidas_lobo.md` con las tres fuentes leídas hoy. Bitácora con 18 días de
  historial (2026-08-08 a hoy), dentro de la ventana de ~30 días — sin podar todavía.
- **2026-08-26** — Corrida diaria de refinamiento. Confirmé `main` al día (`git pull` trajo
  fast-forward de la corrida de ayer, working tree limpio) y verifiqué `research/fuentes/codice.md`
  por conteo directo: **468 filas, F-1 a F-468 sin huecos**, mismo tope exacto que procesó la corrida
  de ayer (2026-08-25) — **cero fuentes nuevas** registradas por `cronista`/`/trinidad`/`/seeker`/
  `/gossip`/`/marketer` desde entonces, decimotercer día seguido sin cambios sustanciales en el
  ledger. Repasé las 25 tesis contra ese mismo tope: ninguna quedó desalineada con la evidencia
  vigente y no forcé ningún matiz solo por completar el paso. Sí corrió la rutina diaria de intuición
  (vigesimoprimera corrida desde el 2026-08-06): de 136 fuentes 🟢A confirmadas por conteo propio en
  el ledger, 57 ya tenían lectura profunda del Lobo — de las 79 restantes elegí 3 al azar puro
  (`shuf`): F-63 (protocolo de validación mixto de Omaolo, JMIR Research Protocols — ya citada en el
  node de salud como plantilla de diseño de validación), F-178 (Guitart & Stremersch 2021, contenido
  informativo vs. emocional en TV, *JMR* — ya citada para matizar imagen aspiracional vs. bullets en
  material de venta) y F-340 (Sinaiko, Landrum & Chernew 2017, red por niveles, *Health Affairs* — ya
  citada en documento externo del usuario sobre steering de proveedor). Las tres bloqueadas por el
  proxy en su URL directa (ncbi.nlm.nih.gov, researchprotocols.org, journals.sagepub.com,
  healthaffairs.org, commonwealthfund.org); reconstruidas vía cobertura académica y periodística de
  búsqueda dirigida que confirma detalle nuevo no capturado en el resumen de una línea de cada una.
  Sumé las entradas 58, 59 y 60 de Intuición acumulada: (58) F-63 es el protocolo metodológico detrás
  de los números de Omaolo que ya sostenían tesis 10 (F-42) — agrega que la validación de seguridad de
  un triage necesita viñetas construidas a propósito para la cola de casos raros/agudos, no solo
  muestreo real, porque esa cola es justamente la que un muestreo real casi nunca captura; (59) F-178
  separa "qué mueve búsqueda" de "qué mueve venta" en contenido informativo vs. emocional, y ambos
  dependen del tier de precio del producto — matiza la recomendación de material visual de venta
  consultiva, que debe condicionarse al tier del producto y al objetivo de la pieza, no aplicarse
  parejo; (60) F-340 tiene un límite de mecanismo que el 5% de ahorro agregado no mostraba: el tiering
  de precio dirige bien a clientes nuevos sin relación establecida, pero no rompe relaciones ya
  existentes — acota cómo proyectar el ahorro esperado de cualquier palanca de tiering/derivación que
  el proyecto diseñe. Ninguna tesis de negocio cambió de confianza numérica por esta corrida — es el
  mecanismo paralelo de intuición, no una revisión de evidencia sobre las tesis existentes, aunque las
  tres entradas de hoy sí acotan el alcance de tesis 9, 10 y de la conexión de material visual de venta
  consultiva. Actualicé `research/lobo/fuentes_leidas_lobo.md` con las tres fuentes leídas hoy.
  Bitácora con 19 días de historial (2026-08-08 a hoy), dentro de la ventana de ~30 días — sin podar
  todavía.
- **2026-08-27** — Corrida diaria de refinamiento. Confirmé `main` al día (`git pull` trajo fast-forward
  6324fc0→e68ecd4, el commit de la corrida de ayer, working tree limpio) y verifiqué
  `research/fuentes/codice.md` por conteo directo: **468 filas, F-1 a F-468 sin huecos**, y **136 filas
  con rigor 🟢A** — mismo tope exacto que procesó la corrida de ayer (2026-08-26) — **cero fuentes
  nuevas** registradas por `cronista`/`/trinidad`/`/seeker`/`/gossip`/`/marketer` desde entonces,
  decimocuarto día seguido sin cambios sustanciales en el ledger. Repasé las 25 tesis contra ese mismo
  tope: ninguna quedó desalineada con la evidencia vigente y no forcé ningún matiz solo por completar el
  paso — el último bloque "[Revisión...]" real sigue siendo el del 2026-08-12 (mecanismo de `cronista`,
  cada ~3 días, ya lleva quince días sin correr; no lo disparo aquí porque es rutina de `cronista`, no de
  este proceso diario). Sí corrió la rutina diaria de intuición (vigesimosegunda corrida desde el
  2026-08-06): de 136 fuentes 🟢A confirmadas por conteo propio en el ledger, 60 ya tenían lectura
  profunda del Lobo — de las 76 restantes elegí 3 al azar puro (Python `random.sample`, sin `--seed`):
  F-154 (chatbot de seguros vía ML explicable + IPMA, MDPI *Electronics* 2025 — ya citado solo como
  "metodológicamente más sofisticado que un cuestionario simple"), F-108 (Direct Primary Care, *JGIM*
  2024 — ya citado solo por la cifra agregada de ahorro en Medicare) y F-225 (Alter & Oppenheimer 2009,
  fluidez de procesamiento — ya citado como sustento del Principio 1 del Playbook del Asesor). Las tres
  bloqueadas por el proxy en su URL directa (mdpi.com, link.springer.com/pubmed.ncbi.nlm.nih.gov,
  doi.org/journals.sagepub.com); reconstruidas vía búsqueda dirigida (ResearchGate para F-154 y F-225,
  PubMed/Concierge Medicine Today para F-108, más la literatura relacionada de los mismos autores —
  Alter, Oppenheimer, Epley & Eyre 2007, "Overcoming Intuition" — para el reverso de F-225) que
  confirman detalle nuevo, no solo el resumen ya citado. Sumé las entradas 61, 62 y 63 de Intuición
  acumulada: (61) el Importance-Performance Map Analysis separa qué atributo importa de cuál rinde mal
  hoy — en chatbots de seguros el cuadrante que justifica inversión es confianza e influencia social, no
  la utilidad percibida, que ya rinde bien; sin tesis numerada propia, conecta con tesis 9/10/23 y 18;
  (62) el ahorro de Direct Primary Care depende de que la membresía fija cambie el incentivo del médico
  (menos derivación cara), no de que el canal de acceso sea más barato — acota tesis 10 y 17 con un
  requisito de diseño para cualquier modelo de atención primaria alternativa del proyecto; (63) la
  fluidez de procesamiento tiene un reverso deliberado y documentado (dificultad metacognitiva activa
  escrutinio analítico, aunque no garantiza mejor decisión) — matiza tesis 1 y el Principio 1 del
  Playbook (tesis 18) con un límite de alcance que ninguna tenía: la claridad sirve para convertir, la
  fricción intencional sirve para proteger al cliente de una decisión apresurada, y son palancas
  distintas para objetivos distintos. Ninguna tesis de negocio cambió de confianza numérica por esta
  corrida — es el mecanismo paralelo de intuición, no una revisión de evidencia sobre las tesis
  existentes, aunque las tres entradas de hoy sí acotan el alcance de tesis 1, 9, 10, 17, 18 y 23.
  Actualicé `research/lobo/fuentes_leidas_lobo.md` con las tres fuentes leídas hoy. Bitácora con 20 días
  de historial (2026-08-08 a hoy), dentro de la ventana de ~30 días — sin podar todavía.
- **2026-08-28** — Corrida diaria de refinamiento. Confirmé `main` al día (`git pull` trajo fast-forward
  6324fc0→29b2246, el commit de la corrida de ayer, working tree limpio) y verifiqué
  `research/fuentes/codice.md` por conteo directo: **468 filas, F-1 a F-468 sin huecos** — mismo tope
  exacto que procesó la corrida de ayer (2026-08-27), **cero fuentes nuevas** registradas por `cronista`/
  `/trinidad`/`/seeker`/`/gossip`/`/marketer` desde entonces, decimoquinto día seguido sin cambios
  sustanciales en el ledger. Repasé las 25 tesis contra ese mismo tope: ninguna quedó desalineada con la
  evidencia vigente y no forcé ningún matiz solo por completar el paso — el último bloque
  "[Revisión...]" real sigue siendo el del 2026-08-12 (mecanismo de `cronista`, cada ~3 días, ya lleva
  dieciséis días sin correr; no lo disparo aquí porque es rutina de `cronista`, no de este proceso
  diario). Sí corrió la rutina diaria de intuición (vigesimotercera corrida desde el 2026-08-06): esta
  vez recalculé el conteo de fuentes 🟢A por conteo propio y directo sobre la columna de rigurosidad
  (no el resumen textual de filas previas, que mezclaba rigor primario con menciones secundarias de 🟢
  dentro del mismo texto) y encontré **134 filas con rigor primario 🟢A puro** (más 3 filas mixtas —
  F-149, F-457, F-466 — cuyo rigor principal no es A y que por eso excluí de la población elegible), de
  las cuales 63 ya tenían lectura profunda del Lobo — de las 71 restantes elegí 3 al azar puro (Python
  `random.sample`, sin `--seed`): F-43 (Harada et al. 2024, *JMIR Formative Research*, precisión de
  symptom-checker japonés — ya citado en tesis 10 solo por la cifra plana de 45.1% y, desde la revisión
  profunda de `cronista` del 2026-08-05, por el desglose 24.2%/14.5%), F-36 (factor dominante de
  automedicación no responsable en Perú, SciELO 2021 — ya citado en tesis 9 por el OR=29.06) y F-339
  (Mazurenko, Taylor & Menachemi 2022, *Medical Care Research and Review*, redes estrechas/por niveles —
  ya citado en tesis 23 como transferencia de mecanismo de redes de proveedores a steering de canal).
  Las tres bloqueadas por el proxy en su URL directa (ncbi.nlm.nih.gov, scielo.org.pe,
  journals.sagepub.com); reconstruidas vía búsqueda dirigida (JMIR Formative Research, Academia.edu/
  SciELO Preprints, y el repositorio institucional de IUPUI) que confirma detalle nuevo no capturado en
  el resumen de una línea de cada una, incluso para F-43 y F-36 pese a que ya tenían matiz de tesis
  propio — el ángulo de hoy es de heurística transferible, no de matiz de negocio puntual, como marca la
  regla del proceso. Sumé las entradas 64, 65 y 66 de Intuición acumulada: (64) un promedio de precisión
  estable en el tiempo no es evidencia de solidez si nadie separó los casos fáciles de los difíciles —
  F-43 confirma que "commonality" y "typicality" están asociadas de forma estadísticamente significativa
  a la precisión, el mecanismo formal detrás del dato ya conocido; (65) un odds ratio que multiplica por
  15-20x al resto de una tabla de regresión (aquí, OR=29 vs. 1.3-1.9) casi nunca es sesgo conductual
  gradual — es una regla de compuerta incumplida, y la intervención correcta es de proceso/política, no
  de nudge al consumidor; (66) un veredicto agregado de "sin efecto adverso sistemático" puede promediar
  un outcome negativo y saliente (tiempo de espera, en F-339) con otros neutrales — pedir el desglose por
  outcome antes de repetir el veredicto general de cualquier revisión sistemática. Ninguna tesis de
  negocio cambió de confianza numérica por esta corrida — es el mecanismo paralelo de intuición, no una
  revisión de evidencia sobre las tesis existentes, aunque las tres entradas de hoy sí acotan el alcance
  de tesis 9, 10 y 23. Actualicé `research/lobo/fuentes_leidas_lobo.md` con las tres fuentes leídas hoy.
  Bitácora con 21 días de historial (2026-08-08 a hoy), dentro de la ventana de ~30 días — sin podar
  todavía.
- **2026-08-29** — Corrida diaria de refinamiento. Confirmé `main` al día (`git pull` sin cambios,
  working tree limpio) y verifiqué `research/fuentes/codice.md` por conteo directo: **468 filas, F-1 a
  F-468 sin huecos** — mismo tope exacto que procesó la corrida de ayer (2026-08-28), **cero fuentes
  nuevas** registradas por `cronista`/`/trinidad`/`/seeker`/`/gossip`/`/marketer` desde entonces,
  decimosexto día seguido sin cambios sustanciales en el ledger. Repasé las 25 tesis contra ese mismo
  tope: ninguna quedó desalineada con la evidencia vigente y no forcé ningún matiz solo por completar
  el paso — el último bloque "[Revisión...]" real sigue siendo el del 2026-08-12 (mecanismo de
  `cronista`, cada ~3 días, ya lleva diecisiete días sin correr; no lo disparo aquí porque es rutina de
  `cronista`, no de este proceso diario). Sí corrió la rutina diaria de intuición (vigesimocuarta
  corrida desde el 2026-08-06): recalculé el conteo de filas con rigor primario 🟢A puro sobre la
  columna de rigurosidad (mismo método de la corrida de ayer, excluyendo las 3 filas mixtas F-149,
  F-457, F-466) y confirmé **134 filas**, de las cuales 66 ya tenían lectura profunda del Lobo — de las
  68 restantes elegí 3 al azar puro (Python `random.sample`, sin `--seed`): F-241 (Luguri &
  Strahilevitz 2021, *Journal of Legal Analysis*, dark patterns — ya citado solo en el node de
  tendencias-diseno-innovacion por las tres cifras agregadas de conversión), F-244 (Bansal et al. 2021,
  CHI, explicaciones de IA y desempeño complementario — ya citado en tesis 22 por el resumen de una
  línea "sin verificabilidad producen sobre-confianza") y F-341 (*Journal of Health Economics* 2018,
  disposición a pagar por continuidad de proveedor — ya citado en tesis 23 solo dentro de un rango
  agregado F-338 a F-341). Las tres bloqueadas por el proxy en su URL directa (academic.oup.com,
  dl.acm.org/researchgate.net/idl.cs.washington.edu, pubmed.ncbi.nlm.nih.gov/sciencedirect.com);
  reconstruidas vía búsqueda dirigida (SSRN/Chicago Unbound para F-241; NSF Public Access y Microsoft
  Research para F-244; IDEAS/RePEc, APPAM y CDC Stacks para F-341) que confirman detalle de mecanismo
  nuevo en las tres, no solo el resumen de una línea ya citado. Sumé las entradas 67, 68 y 69 de
  Intuición acumulada: (67) el backlash de un dark pattern depende del subtipo específico (leve vs.
  agresivo) y no de si existe manipulación en abstracto — los leves duplican conversión sin backlash
  medible pero castigan más a quien tiene menos educación, un criterio de auditoría nuevo para tesis 18
  (el playbook de ventas de RIMAC); (68) una explicación de IA puede subir la aceptación de la
  recomendación por igual acierte o falle la IA — inflar percepción de competencia, no calibrar
  confianza — y no superó al baseline barato de solo mostrar el score de confianza crudo, matiz de
  diseño nuevo para tesis 22; (69) la aversión a redes angostas de proveedores es casi binaria (¿el
  médico habitual queda adentro o afuera?), no una función continua del tamaño de la red — la variable
  de diseño más accionable que el cluster de evidencia de tesis 23 todavía no tenía. Ninguna tesis de
  negocio cambió de confianza numérica por esta corrida — es el mecanismo paralelo de intuición, no una
  revisión de evidencia sobre las tesis existentes, aunque las tres entradas de hoy sí acotan el alcance
  de tesis 18, 22 y 23. Actualicé `research/lobo/fuentes_leidas_lobo.md` con las tres fuentes leídas
  hoy. Bitácora con 22 días de historial (2026-08-08 a hoy), dentro de la ventana de ~30 días — sin
  podar todavía.
- **2026-08-30** — Corrida diaria de refinamiento. Confirmé `main` al día (`git pull` fast-forward
  5612e59→a1450e0, que trajo consigo el commit de ayer de esta opinión y de `fuentes_leidas_lobo.md`)
  y verifiqué `research/fuentes/codice.md` por conteo directo: **468 filas, F-1 a F-468 sin huecos** —
  mismo tope exacto que procesó la corrida de ayer (2026-08-29), **cero fuentes nuevas** registradas
  por `cronista`/`/trinidad`/`/seeker`/`/gossip`/`/marketer` desde entonces, decimoséptimo día
  seguido sin cambios sustanciales en el ledger. Repasé las 25 tesis contra ese mismo tope: ninguna
  quedó desalineada con la evidencia vigente y no forcé ningún matiz solo por completar el paso — el
  último bloque "[Revisión...]" real sigue siendo el del 2026-08-12 (mecanismo de `cronista`, cada ~3
  días, ya lleva dieciocho días sin correr; no lo disparo aquí porque es rutina de `cronista`, no de
  este proceso diario). Sí corrió la rutina diaria de intuición (vigesimoquinta corrida desde el
  2026-08-06): recalculé por script el conteo de filas con rigor primario 🟢A (columna de rigurosidad
  que **empieza** con 🟢, sin importar caveats secundarios después — mismo criterio que usó la corrida
  de ayer, que ya distinguía entre "mixto" F-149/F-457/F-466, con rigor primario no-A, de filas como
  F-257/F-333/F-429, con rigor primario A y solo un caveat secundario) y confirmé **134 filas**, de
  las cuales 69 ya tenían lectura profunda del Lobo — de las 65 restantes elegí 3 al azar puro
  (Python `random.sample`, sin `--seed`): F-221 (Kahneman & Tversky 1979, *Econometrica*, prospect
  theory — ya citado en tesis 18 solo por la cifra de aversión a la pérdida 2:1), F-59 (Mdege et al.
  2011, revisión metodológica del diseño stepped-wedge — ya citado en tesis 10 solo por el resumen de
  ventajas) y F-333 (Lewis et al. 2021, PLOS One, cumplimiento de NHS 111 — ya citado solo por la
  cifra agregada de £4.52M y 11% de no conformidad). Las tres bloqueadas por el proxy en su URL
  directa (jstor.org, ncbi.nlm.nih.gov, journals.plos.org); reconstruidas vía búsqueda dirigida que
  confirma detalle de mecanismo nuevo en las tres, no solo el resumen ya citado. Sumé las entradas 70,
  71 y 72 de Intuición acumulada: (70) el efecto certeza de la teoría fundacional explica por qué
  "cero deducible" se sobre-paga — eliminar el último tramo de riesgo residual vale
  desproporcionadamente más que reducirlo en la misma magnitud sin llegar a cero, hipótesis de
  pricing nueva para tesis 2/18; (71) la vulnerabilidad estructural específica (no genérica) de un
  piloto stepped-wedge es la confusión por tendencia temporal/secular — criterio de auditoría nuevo
  para cualquier piloto propio que use ese diseño (tesis 10); (72) el 11% de "incumplimiento" de NHS
  111 no era mayormente desobediencia: 88% de ese grupo llegó clasificado urgente y 37% terminó
  hospitalizado — evidencia empírica directa de la intuición 53 (un sistema de triaje falla en dos
  direcciones simétricas), criterio de validación nuevo para tesis 10. Ninguna tesis de negocio
  cambió de confianza numérica por esta corrida — es el mecanismo paralelo de intuición, no una
  revisión de evidencia sobre las tesis existentes, aunque las tres entradas de hoy sí acotan el
  alcance de tesis 2, 10 y 18. Actualicé `research/lobo/fuentes_leidas_lobo.md` con las tres fuentes
  leídas hoy. Bitácora con 23 días de historial (2026-08-08 a hoy), dentro de la ventana de ~30 días
  — sin podar todavía.
