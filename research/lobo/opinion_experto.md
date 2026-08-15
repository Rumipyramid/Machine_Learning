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
- **2026-07-27** — Corrida diaria de refinamiento. El ledger creció de F-235 a F-328 desde la
  última corrida (2026-07-26): investigación `/trinidad` de 360° sobre tendencias de diseño (node
  nuevo `_nodes/tendencias-diseno-innovacion.md`, 92 fuentes) — **cambio sustancial**. Es el node menos
  centrado en seguros de los que ha entrado al ledger hasta hoy (cubre producto/UX, IA, design
  systems, consultoras de diseño, mercado laboral del gremio), así que filtré con criterio de
  negocio qué de ahí es accionable para Rimac en vez de sumarlo todo: tomé solo lo que el propio
  node ya marca como "aplicable directamente al contexto Rimac/seguros" o que conecta con tesis ya
  vigentes de esta opinión. Sumé tesis 21 (el ROI del diseño que sostenga cualquier caso de negocio
  interno —incluido el deck al VP de Back to Basics, tesis 18— debe argumentarse por mecanismo, no
  por multiplicador; las 4 cifras de ROI de diseño más citadas globalmente no tienen fuente
  primaria auditable) y tesis 22 (la personalización con IA puede reducir conversión, no
  aumentarla, cuando el dato es sensible y la privacidad está saliente — conecta directo con tesis
  7/UBI y tesis 13/divulgación progresiva; el mecanismo que sí calibra confianza es
  verificabilidad, no explicabilidad genérica). Añadí un matiz al riesgo ya existente sobre el
  agente conversacional de Rimac (agregar explicabilidad sin verificabilidad puede generar
  sobre-confianza, no calibrarla) y 3 riesgos/2 oportunidades nuevos espejando ambas tesis. Ninguna
  tesis 1-20 requirió ajuste de confianza — el ledger nuevo las toca solo por conexión razonada
  (tesis 7, 13), no por evidencia directa nueva sobre seguros/salud/Perú. *Nota aparte, no ledger:*
  el node `proyecto-back-to-basics-ffvv-vida.md` (documentación interna del proyecto, no evidencia
  externa de `cronista`) registra que el lineamiento de CUA pasó de "vigente" a "definitivo" el
  2026-07-25: RIMAC cerró por completo el contacto en frío sin consentimiento (Estrategias 2 y 3
  quedan inválidas por definición, no por falta de validación de Compliance) y formalizó un
  mecanismo de tarjeta+QR para la única vía que queda (Estrategia 4). No lo convertí en tesis nueva
  por no ser evidencia externa citable con F-n, pero es la validación interna más fuerte posible de
  tesis 8 (riesgo regulatorio de contacto no consentido) y tesis 16 (el asesor se redistribuye
  hacia canales de consentimiento, no desaparece) — la registro aquí como instinto/contexto de
  proyecto, no como fuente nueva del ledger. Bitácora con 16 días de historial (2026-07-12 a hoy),
  dentro de la ventana de ~30 días — sin podar todavía.
- **2026-07-27 (segunda corrida del día)** — Corrida diaria de refinamiento disparada por segunda
  vez en la misma fecha. Confirmé `main` actualizado (HEAD ya en `e304055`, sin fast-forward
  pendiente) y leí `codice.md` completo: sigue tope en F-328, idéntico al que ya procesó la corrida
  de hoy más temprano (mismo día, commit anterior) — **sin cambios sustanciales** en evidencia, cero
  fuentes nuevas entre una corrida y otra. Repasé las 22 tesis contra ese mismo tope: ninguna quedó
  desalineada, y no forcé ninguna conexión nueva entre tesis solo por completar el paso — la corrida
  anterior de hoy mismo ya agotó las conexiones razonables disponibles (tesis 21, 22, y el matiz
  sobre el agente conversacional de Rimac). Próximo salto de tesis/confianza sigue condicionado a
  que `/trinidad`, `/seeker`, `/gossip`, `/marketer` o `cronista` registren fuentes nuevas en el
  ledger. Bitácora con 16 días de historial (2026-07-12 a hoy), dentro de la ventana de ~30 días —
  sin podar todavía.
- **2026-07-28** — Corrida diaria de refinamiento. Confirmé `main` actualizado (fast-forward
  78584ad→b3fa77b) y leí `codice.md` completo: sigue tope en F-328, idéntico al de las dos
  corridas de ayer (2026-07-27) — **sin cambios sustanciales** en evidencia, cero fuentes nuevas
  desde entonces. Repasé las 22 tesis contra ese mismo tope: ninguna quedó desalineada con el
  ledger vigente. No forcé ninguna conexión nueva entre tesis solo por completar el paso — las dos
  corridas de ayer ya agotaron las conexiones razonables disponibles entre tesis 7, 13, 21 y 22.
  Próximo salto de tesis/confianza sigue condicionado a que `/trinidad`, `/seeker`, `/gossip`,
  `/marketer` o `cronista` registren fuentes nuevas en el ledger. Bitácora con 17 días de
  historial (2026-07-12 a hoy), dentro de la ventana de ~30 días — sin podar todavía.
- **2026-07-29** — Corrida diaria de refinamiento. Confirmé `main` actualizado (fast-forward
  78584ad→c76a3bf) y leí `codice.md` completo: el ledger creció de F-328 a F-379 desde la última
  corrida (2026-07-28) — **cambio sustancial**, 51 fuentes nuevas en tres clusters: (1) un documento
  externo del usuario sobre steering conductual hacia atención primaria/triaje remoto (F-329 a
  F-358, sin node propio en este repo — cruzado directamente contra esta opinión), (2) ampliación de
  `_nodes/futuro-asesores-seguros-venta-digital.md` con los casos Ethos y Bowtie a mayor detalle más
  tres citas del deck interno "Back to Basics" (F-359 a F-371), y (3) node nuevo
  `_nodes/venta-vida-digital-hibrida-latam.md` sobre venta de vida en Brasil/Chile/Colombia (F-372 a
  F-379). Sumé tesis 23 (el steering hacia canal más barato ahorra costo real, pero es el mecanismo
  con la reactancia más fuerte documentada del sector cuando se percibe como interés del pagador —
  con matiz que refuta el supuesto de que opt-out convierte mejor que opt-in, F-357). Amplié tesis 16
  con el detalle de Ethos/Bowtie (ninguno es "cero humano" real) y, sobre todo, con el dato LATAM —
  más transferible a Perú que Corea/China: Azos (Brasil) crece vía 9,000+ corredores, no D2C;
  bancaseguros controla hasta 80% de la distribución de vida en Brasil; Betterfly (Chile) cerró
  operaciones en 5 países. Añadí un matiz a tesis 10: el colapso de Babylon lo gatilló el pagador
  (Centene no renovó), no el paciente — validar precisión clínica no basta si el caso de negocio no
  convence a quien firma el contrato. Sumé 2 oportunidades y 3 riesgos nuevos reflejando tesis 23 y
  el refuerzo LATAM de tesis 16. Ninguna tesis 1-22 requirió ajuste de confianza a la baja — toda la
  evidencia nueva refuerza o matiza tesis ya vigentes, ninguna las contradice. Bitácora con 18 días
  de historial (2026-07-12 a hoy), dentro de la ventana de ~30 días — sin podar todavía.
- **2026-07-29 (revisión profunda, tercera corrida del día)** — Rutina de revisión profunda
  (cada ~3 días): no busca fuentes nuevas en la web, relee a fondo 5 fuentes 🟢A que el ledger
  ya tenía registradas pero solo con el resumen de una línea de `cronista` — las primeras 🟢A
  aún sin lectura profunda, en orden de ID (F-23, F-36, F-40, F-41, F-42; F-3 a F-21 ya se
  habían releído en corridas anteriores del 2026-07-21/22, registradas en
  `research/fuentes/revision_profunda.md`). Ninguna tesis cambió de dirección; las cinco
  matizaron tesis ya vigentes con detalle que el resumen breve no dejaba ver: **tesis 7** (F-23,
  UBI) — el RCT es preregistrado (N=1,449, NCT06101251, 4 brazos, 12 semanas) y el efecto se
  sostuvo en seguimiento posterior a la intervención, pero lo validado es feedback+incentivo
  ("UBI simulado"), no pricing dinámico real — separa el mecanismo conductual del vehículo
  comercial. **Tesis 9** (F-36, F-40, F-41, farmacia+telesalud Perú) — el factor de riesgo
  dominante de automedicación no responsable es que el dispensador no pide receta (OR=29,
  muy por encima de cualquier otro factor), lo que convierte "corregir esa práctica" en
  objetivo de diseño explícito, no efecto colateral; y el crecimiento de telesalud peruana
  cayó tras el pico pandémico — ventana de oportunidad de corto plazo, no tendencia asegurada.
  **Tesis 10** (F-42, Omaolo Finlandia) — el contraejemplo positivo a Babylon separa
  explícitamente seguridad (97.6%) de coincidencia exacta con el humano (53.7%): el gate de un
  triage IA debe fijarse en la primera métrica, no en la segunda. Actualicé `revision_profunda.md`
  con las 5 fuentes de este ciclo y enriquecí los nodes `modelo-salud-ia-farmacias-peru.md` y
  `behavioral-design-estado-disciplina.md` en Many Brains con el mismo detalle, sin mover ni
  reestructurar nada. Bitácora con 18 días de historial (2026-07-12 a hoy) — sin podar todavía.
- **2026-07-30** — Corrida diaria de refinamiento. Confirmé `main` actualizado (fast-forward
  78584ad→ef3a2a3) y leí `codice.md` completo: el ledger creció de F-379 a F-398 desde la última
  corrida (2026-07-29) — **cambio sustancial** en volumen, pero el crecimiento entero es la
  iteración 2 de un solo node (`_nodes/tendencias-diseno-innovacion.md`), que ya venía marcado como el menos
  centrado en seguros de todos los que ha recibido esta opinión (mismo criterio de filtro que
  apliqué el 2026-07-27). Integré con criterio de negocio solo lo transferible a Rimac/seguros, no
  el lote completo: sumé tesis 24 (generative UI — interfaces que la IA genera dinámicamente ya
  tienen evidencia real de que suben la preferencia declarada pero fallan específicamente en
  soporte y consistencia entre sesiones, F-380 a F-386; caución directa para cualquier interfaz
  dinámica que Rimac evalúe para su agente conversacional o un configurador/simulador). Amplié
  tesis 21 con una quinta cadena de eco de cita en design systems ("135% de ROI" es una calculadora
  de 2022, no un estudio medido, F-397) y con un caso paralelo fuera de diseño: el "impuesto de
  verificación" en desarrollo asistido por IA (F-388, preprint sin revisión por pares) — mismo
  principio de tesis 21 ("argumentar por mecanismo, no por multiplicador"), ahora aplicable
  también a cualquier cifra de productividad con IA sobre las propias herramientas del proyecto
  (`lapuerta`, `cerrajero`, el agente conversacional). Sumé dos riesgos nuevos: shadow AI sin
  gobierno de dato corporativo (60% de adopción sin lineamiento en el dato brasileño más reciente,
  F-389 — superficie de fuga de dato regulada por LPDP para cualquier equipo de una aseguradora,
  no solo tema de productividad) y el precedente de MercadoLibre desvinculando 119 roles de UX en
  LatAm citando integración con IA (F-391 — decisión corporativa ya documentada en la región, no
  apuesta especulativa). Filtré explícitamente sin integrar: F-387 (revisión de diseño público del
  gobierno UK, sin conexión directa a seguros), F-390/F-392 (circulación del meme "AI slop" en
  español y cifra agregada de despidos tech con atribución autodeclarada — mismo descuento ya
  aplicado a F-282/F-283 en la iteración 1), F-393 a F-395 (estado gremial del service design,
  incluida su comunidad en Lima — señal social sin puente de negocio directo a Rimac hoy), F-396
  (ya absorbida como refuerzo de tesis 21, no tesis propia), y F-398 (cotización de Figma en bolsa
  — sin conexión de negocio con el proyecto). Ninguna tesis 1-23 requirió ajuste de confianza a la
  baja — la evidencia nueva no las toca, es un node distinto. Bitácora con 19 días de historial
  (2026-07-12 a hoy), dentro de la ventana de ~30 días — sin podar todavía.
- **2026-07-31** — Corrida diaria de refinamiento. Confirmé `main` actualizado (sin cambios
  pendientes) y leí `codice.md` completo: sigue tope en F-398, idéntico al que ya procesó la
  corrida de ayer (2026-07-30) — **sin cambios sustanciales** en evidencia, cero fuentes nuevas
  registradas por `cronista`/`/trinidad`/`/seeker`/`/gossip`/`/marketer` en las últimas 24h.
  Repasé las 24 tesis contra ese mismo tope: ninguna quedó desalineada con el ledger vigente, y no
  forcé ninguna conexión nueva entre tesis solo por completar el paso — la corrida de ayer ya
  agotó las conexiones razonables disponibles (tesis 21/generative UI, shadow AI, MercadoLibre).
  Próximo salto de tesis/confianza sigue condicionado a que alguna de las skills de investigación
  registre fuentes nuevas en el ledger, o a que la próxima revisión profunda (cada ~3 días, la
  última corrió el 2026-07-29 sobre F-23/F-36/F-40/F-41/F-42) encuentre un matiz de mecanismo al
  leer a fondo una fuente ya citada solo por su resumen. Bitácora con 20 días de historial
  (2026-07-12 a hoy), dentro de la ventana de ~30 días — sin podar todavía.
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
- **2026-08-07** — Corrida diaria de refinamiento. Confirmé `main` actualizado (ya en el commit del
  2026-08-06) y leí `codice.md` completo: sigue tope exacto en F-468 (F-1 a F-468 sin huecos),
  idéntico al que ya procesó la corrida de ayer (2026-08-06) — **sin cambios sustanciales** en
  evidencia, cero fuentes nuevas registradas por `cronista`/`/trinidad`/`/seeker`/`/gossip`/
  `/marketer` en las últimas 24h. Repasé las 25 tesis contra ese mismo tope: ninguna quedó
  desalineada con el ledger vigente, y no forcé ninguna conexión de tesis nueva solo por completar
  el paso. La última revisión profunda (rutina de `cronista`, cada ~3 días, última el 2026-08-05) no
  vence hoy. Sí corrió la rutina diaria de intuición (segunda corrida desde que se creó el
  2026-08-06): seleccioné al azar 3 fuentes 🟢A adicionales sin lectura previa del Lobo — F-6
  (Loewenstein 2013, ya citada en tesis 2), F-53 (Holtrop et al. 2021 RE-AIM, ya citada en tesis 9 y
  ya releída por la revisión profunda de `cronista` el 2026-08-05 desde otro ángulo) y F-230 (Deci &
  Ryan 2000, ya citada en tesis 19) — y sumé las entradas 4, 5 y 6 de Intuición acumulada: (4) la
  incomprensión puede anular el uso de un beneficio ya gratuito, no solo empeorar la elección entre
  pagados (matiza tesis 2 sin cambiar su confianza); (5) buscar la literatura de
  "malentendidos/clarificaciones" de cualquier framework con nombre propio antes de adoptarlo, no
  solo el paper fundacional (heurística de proceso, sin tocar confianza de tesis 9/21); (6) un
  incentivo económico contingente puede socavar la motivación de quien ya actuaba por convicción
  propia (efecto de socavamiento, Deci/Koestner/Ryan 1999) — matiza el diseño de incentivos de tesis
  7 y 19 sin cambiar su confianza, es instinto razonado sobre teoría, no dato de campo peruano.
  Actualicé `research/lobo/fuentes_leidas_lobo.md` con las tres fuentes leídas hoy. Bitácora con 26
  días de historial (2026-07-12 a hoy), dentro de la ventana de ~30 días — sin podar todavía.
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
