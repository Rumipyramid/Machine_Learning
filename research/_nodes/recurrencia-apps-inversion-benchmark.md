# Recurrencia y persistencia en inversión y seguros de vida: qué la produce y qué solo parece producirla

> Documento de investigación. Fuente persistente y versionada en el repositorio.
> Fecha de elaboración: 2026-11-01 · Última actualización: 2026-11-02 · Versión: **v2.0** (ampliación de alcance: protección de crédito, vida con ahorro y competidores)
> Origen: `/trinidad` (pista empírica + social + negocio), rol *behavioral designer researcher*.
> Fuentes en `research/fuentes/codice.md`: **F-847 a F-923** (v1.0: F-847 a F-873 · v2.0: F-874 a F-923; incluye una lámina interna, F-908).
> Pregunta permanente: **¿qué hace que una persona vuelva a aportar a una inversión (y no solo a abrir la app), y qué evidencia independiente lo respalda?** Desde v2.0 incluye también: **¿qué mantiene el dinero aportando hasta la meta en seguros de vida y protección de crédito, y qué papel juega la digitalización?**
> ⚠️ **Decisión que alimenta: no definida.** Se asumió benchmarking para el diseño de recurrencia en inversión y seguros de vida con ahorro. Si hay decisión concreta, volver a §6.

---

## 0. 🎯 Alcance y cómo se leyó la evidencia

- **"Recurrencia" tiene tres significados y se confunden.** (a) *Visita*: abrir la app. (b) *Operación*: comprar y vender seguido. (c) *Aporte*: poner dinero de forma periódica. Un seguro de vida con ahorro depende de (c). Casi toda la evidencia sobre "engagement" mide (a) o (b).
- **Cobertura.** Perú: Trii, Tyba, Hapi (se asumió que "Happ" es Hapi), apps de BCP, BBVA e Interbank, fondos mutuos. Mundo: Robinhood, Nubank, Revolut, Acorns, Betterment, Vitality. Quedaron **sin datos útiles**: Vanguard, Fidelity, AFP, bancos globales distintos de Nubank y Revolut.
- **Herramienta de lectura:** solo resúmenes de búsqueda, con resultados centrados en EE.UU. No se abrió ningún artículo ni filing completo. Las atribuciones dudosas están marcadas en el ledger.

## 1. ⚖️ Resumen ejecutivo

1. **No hay ningún dato público de retención ni de aporte sostenido para las apps peruanas.** Ni Trii, ni Tyba, ni Hapi, ni los bancos lo publican. Todo lo que circula es tamaño (usuarios, montos) y es de la propia empresa (F-862 a F-865, F-867).
2. **La evidencia causal más sólida favorece la automatización, no el juego.** Inscripción automática y ahorro con compromiso mueven aportes en estudios con revisión de pares (F-850, F-853). El juego y las alertas mueven más bien la *frecuencia de operación*, con efecto pequeño y daño probable (F-847, F-848).
3. **Esa evidencia viene de pensiones en EE.UU. y de un banco filipino.** No se probó en apps de inversión de LatAm. Además, una revisión oficial califica de baja la evidencia causal de los defaults (F-852).
4. **Más actividad en la app no equivale a más valor.** Robinhood perdió 13% de usuarios activos mensuales mientras subían activos e ingreso por usuario (F-860). Y un experimento con >50.000 clientes subió el compromiso 23% sin mover la inversión real (F-854, de autores y revista no verificados).
5. **En Perú el mercado crece (490.012 partícipes, +17% en 2025, F-866), pero el crecimiento es de acceso, no de recurrencia demostrada.** Las apps abren la puerta (montos mínimos desde S/ 20); lo que se hace después no se mide en público.

## 2. 🔬 Pista empírica/teórica (rigor académico)

### 2.1 Lo que sí tiene respaldo causal: automatizar y comprometer
| Mecanismo | Resultado | Fuente | Límite principal |
|---|---|---|---|
| Inscripción automática (default) | Participación ~20% → ~90% de inmediato, >98% a 36 meses | F-850 (🟢A) | Una empresa; muchos se quedan en la tasa baja por defecto |
| Aporte que sube con cada aumento de sueldo | Mecanismo propuesto y probado en pocas empresas | F-851 (🟢A, leído vía espejos) | Cifras sin verificar en el original |
| Cuenta de ahorro con compromiso | Toma 28%; saldo +42% a 6 meses, +82% a 1 año | F-853 (🟢A, aleatorizado) | Un banco en Filipinas; solo 28% la toma |
| Revisión de la calidad de la evidencia | Baja evidencia causal; casi sin datos de ahorro total | F-852 (🔵B) | Revisión de agencia, 2016 |

**Interpretación (inferencia mía, no hallazgo):** quien se queda en el default no necesariamente "recurre"; solo no se va. Para un producto de inversión eso puede ser retención real, o puede ser inercia que se rompe al primer sobresalto.

### 2.2 Juego, notificaciones y atención: suben la operación, no la calidad
- Los usuarios de Robinhood operan más sobre lo que capta atención; sus compras masivas predijeron retornos bajos (F-847, 🟢A).
- En un experimento aleatorizado, la gamificación hedónica subió el volumen ~5%. Del contraste entre plataformas, ~70% es autoselección y ~30% efecto del juego. Atrae más a quien sabe menos (F-848, 🟢A, plataforma simulada).
- Un ensayo del regulador de Ontario (2.430 personas) vio lo mismo con puntos de valor casi nulo (F-849, 🔵B).
- **Límite que aplica a las tres:** todas miden *operar más*. Ninguna mide *aportar de forma sostenida*, que es lo que importa en vida con ahorro.

### 2.3 Normas sociales y pares: atención sin acción
- La información de pares subió el compromiso inicial 23% sin efecto detectable en la inversión (F-854, 🟡C).
- Mostrar el ahorro de compañeros elevó la intención y algunos pasos en un banco holandés (F-855, 🟡C).
- Ambos son de revista y autores sin verificar; tomarlos como **señal exploratoria**.

### 2.4 Contraevidencia buscada
No encontré ningún experimento de campo que muestre que **metas, rachas o notificaciones** aumenten el aporte sostenido en una app de inversión. La búsqueda dio cero resultados directos; es un vacío, no una refutación.

## 3. 📱 Pista social/mediática

**Nivel de instalación social: 🧊 en Perú, 🌡️ en EE.UU. (solo por el caso Robinhood).** La búsqueda no devolvió hilos de Reddit ni de X sobre Trii, Tyba o Hapi (la herramienta ve sobre todo resultados de EE.UU.), así que **no puedo decir qué opina la gente de esas apps**.

- **EE.UU.:** el caso de mayor ruido es el de Robinhood. En 2024 pagó US$7,5M a Massachusetts y dejó el confeti por frecuencia de operación, las notificaciones a listas "más populares" y rasgos de juego de azar (F-856, 🟡C). Robinhood niega que su app sea gamificada. Es un acuerdo, no una sentencia.
- **Perú:** reseñas de blogs describen funciones, sin quejas ni sentimiento medido (F-857, 🟠D). Una encuesta de Tyba dice que 44% usa redes como principal fuente de educación financiera (F-858, 🟡C, encargada por quien vende) y Andina recoge opiniones de economistas: apps y redes explicarían la entrada de jóvenes (F-859, 🟠D).
- **Validación vs. amplificación:** lo de Perú es amplificación de notas de prensa y de empresa; no hay validación de usuarios.

## 4. 📈 Pista de negocio

**Tipo de evidencia:** filings (F-860, F-861), prensa con cifras corporativas (F-862, F-864, F-867), páginas de producto (F-865, F-872), cifras oficiales por prensa (F-866). **Ninguna da retención ni aporte sostenido.**

| Caso | Qué reporta | Qué NO reporta |
|---|---|---|
| **Robinhood** (F-860) | 27,0M de clientes con fondos; 4,18M en Gold (~15,5%); activos mensuales 13,0M vs 14,9M; ingreso por usuario US$171 | Retención por cohorte |
| **Nubank** (F-861) | 36,2M clientes activos en inversión (2T 2025); actividad mensual 83% | Recurrencia de aporte; Cajitas |
| **Revolut** (F-871) | Aporte recurrente promedio ~€47/mes en Rumania | Cuántos mantienen el plan |
| **Acorns** (F-868) | >50% usaba inversión recurrente (2017, dicho por un ejecutivo) | Denominador, período, churn |
| **Betterment** (F-869) | Precio más bajo si aporta ≥US$200/mes o tiene ≥US$24.000 | Efecto en retención |
| **Vitality** (F-870, y F-25, F-638 ya en el códice) | Caducidad de pólizas 15% a 47% menor (internas) | Control de selección |
| **Trii Perú** (F-862, F-863) | ~50% de operaciones de la BVL; 95% de cuentas nuevas 2024; usuarios 600.000 a 1M según fuente | Usuarios que siguen operando |
| **Tyba Perú** (F-864, F-865) | 216.000 usuarios y S/ 131M (fin 2023); aporte automático desde S/ 20 | Cuántos lo activan y lo mantienen |
| **Hapi** (F-867) | Medio millón de clientes (región), US$4,3M levantados | Retención; cifras 2026 |
| **BCP, BBVA, Interbank** (F-872) | Mínimos S/ 20, S/ 100; BBVA con suscripción programada; Interbank exige perfilamiento | Uso real |
| **Mercado peruano** (F-866) | 490.012 partícipes, +17,39%; patrimonio +21,77% | Corte por edad o canal |

**Cálculo propio (inferencia):** S/ 131M ÷ 216.000 usuarios ≈ **S/ 600 por usuario** en Tyba a fines de 2023. Es un promedio que mezcla inscritos y activos; sugiere tickets pequeños, no recurrencia.

**Comparabilidad:** baja. Cada empresa define "usuario activo" distinto, las fechas van de 2017 a 2026 y las cifras de Trii se contradicen entre fuentes.

## 5. ⚖️ Síntesis (sin mezclar los criterios de validez)

- **Convergencia débil:** las tres pistas apuntan a que **abrir la puerta es fácil (apps, montos desde S/ 20) y lo difícil, y no medido, es el segundo y tercer aporte.** Empírica y negocio coinciden en que lo único con respaldo para sostener aportes es la **automatización con compromiso**; negocio la ofrece (Tyba, BBVA, Betterment) sin publicar si funciona.
- **Divergencia:** la **gamificación** es lo que más usa y celebra el negocio (confeti, rachas, Gold), y es lo que menos respaldo tiene como motor de aporte; lo que sí demuestra la evidencia es que sube operación y atrae a quien sabe menos. La pista social en EE.UU. la trata como problema regulatorio.
- **Explicaciones alternativas al crecimiento peruano** (no descartadas): mayor acceso por las apps, contenido en redes, rendimientos de fondos mutuos que superaron al plazo fijo en 2024 (titular de Andina, no revisado) y distribución vía banco (BCP→Tyba, alianza con Yape). Ninguna prueba recurrencia.
- **Seguros de vida con ahorro:** la caducidad menor de Vitality es la única cifra de persistencia que encontré, y es interna y con selección probable (F-870). Perú tiene norma de transparencia (F-873) pero no publica persistencia.

## 6. 🧪 Hipótesis para testear (no son hallazgos)

1. **Aporte automático atado a un evento de ingreso** (sueldo, gratificación, CTS): ¿sube el aporte sostenido a 6 y 12 meses frente a un recordatorio? Respaldo indirecto en F-850, F-851; no probado en Perú.
2. **Compromiso con meta bloqueada** (tipo F-853) en un producto peruano: ¿qué fracción lo elige y cuánto dura? Probar con gente de bajo y alto sesgo del presente.
3. **Fricción de perfilamiento:** ¿abandona más quien debe pasar el cuestionario de perfil (BBVA, Interbank) que quien entra directo (BCP, Trii)? Hoy es conjetura mía.
4. **Juego vs. sin juego en aporte**, no en operación: nadie lo midió; un A/B daría el primer dato.
5. **Medir lo que falta:** pedir a los actores (si hay acceso) retención de aporte a 3, 6 y 12 meses por cohorte, con definición de "activo" explícita.
6. **Métrica de 'cuenta principal' propia:** medir qué porcentaje de clientes tiene el aporte atado a su sueldo o a un débito vinculado a su ingreso, por cohorte, como hacen Chime y Monzo con el depósito directo (§8.11). Es una métrica, no una intervención; sirve para ver si el aporte sostenido se concentra ahí.
7. **Bolsillo de emergencia dentro del producto de ahorro o vida:** ¿una opción de pausa o rescate parcial reduce la caducidad por liquidez sin bajar el aporte promedio? Respaldo indirecto en F-919 y F-878; no probado en Perú (§8.12).

## 7. 🕳️ Vacíos

- Retención y aporte sostenido en Trii, Tyba, Hapi y apps bancarias peruanas.
- Persistencia (mes 13, 25) de seguros de vida con ahorro en Perú.
- Sentimiento real de usuarios peruanos (Reddit, X, reseñas de tienda): no se pudo ver.
- Bancos globales, Vanguard, Fidelity, AFP y fondos de inversión: sin datos útiles en esta pasada.
- Si los defaults de F-850 funcionan igual con ingresos informales e inestables, típicos en Perú.
- **v2.0:** tasa de conversión al terminar un préstamo; resultados posteriores a sep-2025 del desgravamen opcional; ingreso a la app por día de cobro; efecto de la facilidad de cancelar sobre la caducidad; persistencia (mes 13, 25) de vida con ahorro en Perú.

## 8. 🔭 Ampliación v2.0 (2026-11-01): ocho preguntas sobre persistencia y digitalización

> **Por qué se amplió.** La pregunta cambió de "qué hace volver a la app" a "qué mantiene el dinero aportando hasta la meta, y qué papel juega la digitalización". Cubre protección de crédito (desgravamen), seguro de vida con ahorro y fondos/apps de inversión. Fuentes nuevas: F-874 a F-907 (empírica F-874 a F-880, F-882, F-891, F-903 a F-905 · social/regulatoria F-883 a F-885, F-888 · negocio F-881, F-886, F-887, F-889, F-890, F-892 a F-902, F-906, F-907).
> **Estado de cada respuesta:** 🟢 respondida con evidencia razonable · 🟡 parcial · ⚪ sin evidencia hallada.

### 8.1 Protección de crédito: ¿dónde se gana o se pierde al cliente? — 🟡 parcial
- **Perú.** La prima va dentro de la cuota y se calcula sobre el saldo, así que baja con la deuda (F-889). Desde el 9-sep-2025 el seguro solo puede ser condición en hipotecas de vivienda; las entidades deben ofrecer crédito sin seguro, informar las comisiones que reciben y no cobrar comisión por póliza endosada (F-887). Un experto dice que buena parte de la prima termina como comisión al banco (F-888, opinión).
- **Lectura (inferencia mía).** Con el cobro atado a la cuota, el riesgo no es el olvido. Los puntos de pérdida son (a) quién coloca el seguro al originar el crédito y (b) la posibilidad de cambiar de póliza (F-890).
- **Fuera de Perú.** España y Portugal permiten póliza propia; la barrera práctica sería el descuento de tasa atado a la póliza del banco (F-886, contenido de corredores). En Portugal la retención se volvió difícil tras 2009 (F-891, estudio sin verificar). Irlanda habla de "brecha de cambio" por inercia (F-885).
- **Lo que no hay:** ningún dato cuantitativo de cuánto cliente se pierde en cada punto.

### 8.2 Conversión cuando termina el préstamo — ⚪ sin evidencia
- No hallé ninguna tasa de conversión publicada.
- Hallé lo contrario: casos de ombudsman en Reino Unido e Irlanda donde la póliza siguió cobrándose años después de pagar la hipoteca, y se ordenó devolver primas (F-884). **Cualquier estrategia de conversión necesita consentimiento explícito**; la continuación silenciosa es un riesgo regulatorio y de reputación.
- Algunas pólizas están diseñadas para continuar tras el préstamo (F-884, caso CommBank).

### 8.3 Efecto de que el desgravamen sea opcional — ⚪ sin resultados
- No hay datos posteriores a septiembre de 2025 sobre contratación, tasas ni balances (F-887). Hay proyecciones de prensa: alza de tasas en créditos sin seguro, sobre todo para adultos mayores, y ahorros para los deudores (F-887, titulares sin verificar).
- Es un **experimento natural en curso**: las estadísticas de la SBS antes y después serían la vía de dato.

### 8.4 Por qué se deja de pagar — 🟡 parcial
- **Voluntaria por liquidez: respaldada.** Choques como nacimiento o divorcio suben el rescate (F-878). El desempleo se asocia a mayor caducidad (F-879). Una revisión dice que la literatura apoya sobre todo la hipótesis del fondo de emergencia; la de tasas de interés tiene menos respaldo; en pólizas tradicionales alemanas no hay evidencia de ninguna y en las ligadas a fondos hay más (F-880).
- **Involuntaria: sin dato de seguros.** En suscripciones, ~50% del abandono involuntario viene de tarjetas rechazadas (encuesta a ejecutivos) y proveedores dan 20-40% del total (F-900). No es seguros ni Perú.
- **Cuando cae el canal de cobro, cae la póliza.** En un caso de microseguros solo 14% de ~10.000 pólizas seguía activa dos años después, porque los clientes dejaron de pedir préstamos (F-883). Es una lección de diseño del cobro, no un promedio.
- **Perú: nada.** Ni causas ni mes de caída.

### 8.5 Qué sostiene la persistencia (evidencia) — 🟡 débil
- Todo son cifras de proveedores o internas, sin grupo de control: Vitality y AIA solo dan cifras internas (F-870) y Discovery no publica persistencia en sus resultados (F-897), un SMS el día de la renovación bajó cancelaciones 52%, usuarios de portal cancelan 12% menos (observacional) (F-899), una alerta temprana redujo caducidad 22% (F-892).
- Referencia de mercado: caducidad de la industria en EE.UU. 5,6% en 2025 vs 7,0% en 2024 (F-898).
- **La mejor prueba pendiente** es el ensayo de Ghana con recordatorios y renovación automática por dinero móvil (F-882); aún sin resultados.

### 8.6 Segmentos por ritmo de uso y qué necesita cada uno — 🟡 parcial
- La heterogeneidad existe en operaciones: los activos son un tercio (F-903), 41% operó un solo día en Italia (F-904) y en Colombia los más activos rinden peor (F-905).
- **Ojo con la intuición de que mirar mucho daña:** con ingresos a la cuenta, más atención se asoció a mejor desempeño en un corredor de EE.UU. (F-877, no generalizable). Y el ingreso baja tras caídas del mercado (F-875).
- Los recordatorios suben el ahorro sobre todo cuando apuntan a un gasto concreto (F-876).
- **La hipótesis de que el cliente promedio entra a la app el día de cobro no la encontré probada ni refutada.** Es medible con datos propios.

### 8.7 Qué hacen Nubank, Vitality, Revolut, XTB y otros — 🟡 parcial
| Actor | Qué hace (publicado) | Qué no publica |
|---|---|---|
| **Nubank** | Depósitos recurrentes en Caixinhas desde 2022, con aviso previo y pausa (F-894); Nubank Vida con Chubb, contratación en <1 min, ~560 mil pólizas en 2023 (F-893); 36,2 M de clientes activos en inversión (F-861) | % con aporte recurrente; caducidad del seguro |
| **Vitality (Discovery)** | Recompensas por conducta; mortalidad 57% menor en estatus Gold/Diamond (F-897) | Persistencia por cohorte; control de selección |
| **Revolut** | Planes de ETF desde €1 y robo-advisor con recurrentes desde €10 (F-896); aporte medio ~€47 en Rumania (F-871) | Retención del plan |
| **XTB** | 864 mil clientes nuevos en 2025 (F-901); ingreso por cliente activo de 7.400 a 1.800 PLN y solo 7% de nuevos en CFD (F-902) | Retención; clientes activos |
| **Trade Republic** | Planes de ahorro desde €1 (F-895) | Clientes con plan; aporte medio |
| **Yape (Perú)** | ~15,9 M activos mensuales y 54,5 transacciones al mes por activo (F-906) | Desglose por función |
| **BCP/tyba (Perú)** | Aporte automático y fondos desde S/ 20 (F-865, F-907) | Uso real |

**Patrón (inferencia):** ninguno publica retención de aporte. Todos construyen la recurrencia **por diseño** (aporte programado, aviso previo, pausa) y la montan sobre un hábito existente (cuenta, pagos). XTB sugiere que el negocio de operar mucho rinde cada vez menos por cliente.

### 8.8 ¿Digitalizar facilita irse? — ⚪ sin evidencia rigurosa
- No hallé estudio alguno sobre facilidad de cancelar y abandono, ni en seguros ni en suscripciones.
- Lo cercano: el cobro desde saldo móvil sostiene la persistencia pero el cliente puede no saber que está inscrito (F-881); un SMS el día de renovación redujo cancelaciones (F-899, proveedor); y los ombudsman tratan la continuidad silenciosa como problema (F-884). Muestran que el momento de decidir existe y se puede intervenir, no que digitalizar suba o baje la caducidad.
- **La hipótesis sigue abierta.**

### 8.9 Síntesis de la ampliación (pistas separadas)
- **🔬 Empírica:** lo mejor respaldado es que los choques de liquidez explican rescates y que defaults y automatización sostienen el aporte (F-850, F-878). Más funciones no tienen respaldo causal y pueden empeorar la satisfacción (F-874). Atención y operación no son lo mismo (F-875, F-877).
- **📱 Social/regulatoria:** lo más sólido son los ombudsman extranjeros sobre cobros que continúan tras el préstamo (F-884). Sobre usuarios peruanos no hay foros ni quejas accesibles con esta herramienta.
- **💼 Negocio:** crecimiento y tamaño en todos los competidores, sin retención de aporte ni caducidad. Las cifras de persistencia que existen son de proveedores (F-899, F-892).
- **Convergencia débil:** nadie demuestra que digitalizar sostenga el aporte; lo que sí aparece repetido es automatizar con aviso previo y pausa. **Divergencia:** los proveedores reportan reducciones grandes de caducidad que la evidencia independiente no corrobora.

### 8.10 Implicaciones para RIMAC (hipótesis, no hallazgos)
1. **Desgravamen:** la palanca competitiva está en la originación y en la experiencia al reclamar, no en el engagement. Vigilar el efecto del cambio normativo con las estadísticas de la SBS.
2. **Vida con ahorro:** primero diagnosticar por qué cae el cliente (liquidez vs. cobro fallido). Si domina la liquidez, evaluar una opción de pausa o rescate parcial; no está probada.
3. **Inversión:** aporte programado atado al ingreso, con aviso antes del cargo y pausa fácil (patrón de Nubank); probarlo contra un grupo de control y medir aporte a 3, 6 y 12 meses.
4. **Conversión al terminar un préstamo:** solo con consentimiento explícito.

### 8.11 Cinco patrones fintech (lámina interna): qué hay de evidencia detrás — 🟡 parcial

> Fuente: lámina de una investigación interna, sin autor ni método indicados (F-908). Etiqueta cinco apps con un patrón de diseño y afirma que son "transferibles a seguros". La lámina no trae ninguna cifra de efecto; esta sección contrasta cada patrón con lo que se halló. Fuentes: F-909 a F-914.

| Patrón de la lámina | App | Qué se halló | Estado |
|---|---|---|---|
| **Prioriza** (productos sugeridos) | Revolut | Planes recurrentes y robo-advisor publicados, sin retención (F-896, F-871) | Sin evidencia de efecto |
| **Reorganiza** (lista de inicio 0/6) | N26 | N26 no publica métricas de inicio ni retención (F-913); no busqué estudios de listas de inicio | Sin evidencia hallada |
| **Transparenta** (desglose de comisión) | Wise | Bajó su comisión media a 53 puntos base y más de 70% de clientes nuevos llega por recomendación (F-914): correlación, no efecto probado. En Perú la SBS ya obliga a informar las comisiones del desgravamen (F-887) | Parcial: ya es norma en un caso |
| **Adapta** (subir de nivel) | Chime | La empresa dice que su nivel Prime mejora la retención de quienes ya tienen depósito directo (F-910); sin grupo de control. El ingreso por miembro crece con la antigüedad (F-910), lo que puede ser supervivencia | Sin evidencia independiente |
| **Experimenta** (sorteo y recompensas) | Monzo | Double Payday sortea el doble del sueldo de 10 clientes al mes desde dic-2025 (F-912); sin datos de uso ni efecto. El juego en inversión sube la operación, no el aporte (F-848) | Sin evidencia de efecto |

**Lo más útil de estas cinco empresas no es ninguno de los cinco patrones.** Chime, Monzo y N26 miden la misma cosa: **qué porcentaje de sus clientes tiene el sueldo depositado ahí** ("cuenta principal"). Chime lo define con un depósito directo de al menos US$200 al mes o 15 compras (F-909); Monzo reporta 33% de clientes y 49% de activos mensuales (F-911); N26 dice buscar que el sueldo llegue a su cuenta (F-913). Es la métrica que eligieron, no evidencia causal, pero coincide con la hipótesis de que el hábito se ancla en el ingreso (§6, hipótesis 1 y 6).

**Lectura (inferencia mía):** los patrones de la lámina son analogías de diseño razonables, pero ninguna de las cinco empresas publica retención, así que "transferible a seguros" es una hipótesis, no un resultado.

### 8.12 Ahorro: qué dice la literatura conductual (2026-11-02) — 🟡 parcial

> Fuentes nuevas: F-915 a F-922. Ya estaban en este node la inscripción automática (F-850), el ahorro con compromiso (F-853), los recordatorios (F-876) y la revisión de calidad de la evidencia (F-852).

| Mecanismo | Qué se halló | Fuente | Límite principal |
|---|---|---|---|
| **Automatizar el aporte** | Con inscripción automática, la participación pasó de ~20% a ~90% (F-850). En Dinamarca, ~85% de la gente es "pasiva": no responde a subsidios y su ahorro sube con contribuciones automáticas; US$1 de subsidio sube el ahorro total 1 centavo (F-915). | F-850, F-915 (🟢A) | Pensiones en EE.UU. y Dinamarca; nada en América Latina |
| **El efecto se erosiona** | ~20% del ahorro creado se compensa con más deuda (F-916). A mediano y largo plazo la dinámica reduce el efecto de la inscripción y de la escalada automáticas (F-917). Choukhmane halla más riqueza a los 65 (>12%) con poco desplazamiento, pero ganancias de corto plazo que se desvanecen (F-918). | F-916, F-917, F-918 (🟡C) | Documentos de trabajo; los estudios no coinciden en cuánto sobrevive |
| **Aporte que sube con el sueldo** (Save More Tomorrow) | Diseño: se compromete hoy un aumento del aporte con cada futuro aumento de sueldo (F-851). CLEAR califica de baja la evidencia causal (F-922). Las cifras que circulan no coinciden entre fuentes y **no pude verificar ninguna**. | F-851 (🟢A), F-922 (🔵B) | Pocas empresas; sin grupo de control claro |
| **Compromiso (dinero bloqueado hasta la meta)** | Saldo +82% a un año con una cuenta con compromiso; solo 28% la toma (F-853). Revisión general en F-920, sin tamaños de efecto leídos. | F-853 (🟢A), F-920 (🔵B) | Un banco en Filipinas |
| **Ahorro para salud en mercados emergentes** | Un lugar seguro para guardar subió el ahorro para salud 66%. La cuenta reservada a emergencias de salud fue muy valorada. Quienes tienen sesgo de presente (~16%) no usaron el dispositivo sin restricción de retiro. El uso siguió alto tres años después (F-919). | F-919 (🟢A) | 771 personas en zonas rurales de Kenia |
| **Teoría de la liquidez** | Los activos ilíquidos funcionan como compromiso; añadir liquidez puede bajar el ahorro y el bienestar (F-921). | F-921 (🟢A, modelo) | Es un modelo, no una prueba de campo |
| **Recordatorios** | Suben el ahorro sobre todo cuando apuntan a un gasto concreto (F-876). | F-876 (🟢A) | Sin tamaños de efecto leídos |

**Lectura (inferencia mía):**
- **Lo que mueve el ahorro es quitar decisiones repetidas y limitar las salidas**, no dar más información ni más funciones. Eso refuerza lo ya visto: automatizar con aviso y pausa.
- **La digitalización tiene una tensión de fondo.** La teoría (F-921) sugiere que facilitar el retiro puede bajar el ahorro. No hay prueba de campo, pero apunta a la pregunta abierta de 8.8.
- **Compromiso con válvula de emergencia.** En Kenia, la cuenta reservada a emergencias fue muy valorada (F-919). Es una pista para una opción de pausa o rescate parcial dentro de un producto de ahorro (8.10, punto 2). Es hipótesis, no resultado.
- **No asumir que lo automático asegura el aporte a 12-24 meses.** Los estudios recientes muestran erosión (F-916 a F-918).
- **No hay evidencia peruana** y casi ninguna de América Latina.

**No verifiqué:** otras piezas conocidas de la literatura (por ejemplo O'Donoghue y Rabin sobre procrastinación, o la teoría de miopía ante pérdidas) y las cifras originales de Save More Tomorrow. Todo se leyó por resúmenes.

### 8.13 Hexágono de la Salud Financiera: un mapa de necesidades, no evidencia — 🟠

> Fuente: F-923, material divulgativo de la consultora Beway (cinco de seis vértices). **No amplía el alcance ni responde ninguna de las ocho preguntas con evidencia.** Sirve para ubicar qué necesidad cubre cada producto.

| Vértice | Qué propone | Dónde toca las preguntas |
|---|---|---|
| **1. Administración diaria** | Presupuesto, bolsillos, débito automático, tarjetas prepago | Refuerza automatizar y separar el dinero (8.12); aporte atado al ingreso (hipótesis 1 y 6) |
| **2. Resiliencia financiera** | Fondo de emergencia de 3 a 6 meses de ingresos, en cuenta separada; los seguros como parte de la protección | Caducidad por liquidez (8.4) y bolsillo de emergencia (hipótesis 7). **Tensión (inferencia mía):** si el cliente no tiene un fondo propio, un producto de vida con ahorro puede terminar usándose como tal, y el rescate por liquidez es previsible |
| **3. Metas a corto y medio plazo** | Metas SMART y ahorro periódico dentro del presupuesto | Recordatorios con un gasto concreto (F-876). Que fijar metas claras ayude a ahorrar **no tiene respaldo experimental en lo que leí** |
| **4. Flexibilidad financiera** | Liquidez para aprovechar oportunidades, en activos de bajo riesgo | Tensión con la teoría de la liquidez (F-921): liquidez evita decisiones impulsivas pero puede bajar el ahorro. Se concilia (inferencia) separando cubetas: liquidez para emergencias y oportunidades, dinero comprometido para metas y largo plazo |
| **5. La inversión** | Inflación, interés compuesto y control emocional ante caídas | Días malos (F-875) y 8.6. La aritmética del ejemplo cuadra, pero asume 5% real sin fuente |

**Lectura (inferencia mía):** el hexágono ayuda a ubicar cada producto en una cubeta: resiliencia para el seguro, metas y largo plazo para ahorro e inversión. No cambia las preguntas. El vértice 6 no se recibió.

---

## 9. 📓 Bitácora

- **2026-11-02** — Se añade §8.13: el Hexágono de la Salud Financiera (F-923) como mapa de necesidades; sin evidencia de efecto y sin ampliar el alcance. Incremental.
- **2026-11-02** — Se añade §8.12 con la literatura conductual de ahorro (F-915 a F-922): automatización, erosión de los defaults, compromiso, ahorro para salud en Kenia y teoría de la liquidez. Incremental.
- **2026-11-02** — Se añade §8.11 con cinco patrones fintech de una lámina interna (F-908) contrastados con Chime, Monzo, N26, Wise y Revolut (F-909 a F-914). Cambio incremental; la versión sigue en v2.0.
- **2026-11-01 · v2.0** — Ampliación de alcance (cambio estructural): las ocho preguntas de §8; 34 fuentes nuevas (F-874 a F-907). Competidores: Nubank, Vitality, Revolut, XTB, Trade Republic, Yape. Lectura por resúmenes de búsqueda.
- **2026-11-01 · v1.0** — Creación. `/trinidad`; 27 fuentes (F-847 a F-873). Búsqueda sin acceso a textos completos; todo por resúmenes.

---

## Limitaciones

- La pista **social** quedó la más débil: sin foros ni redes de Perú.
- La pista **de negocio** es abundante pero toda es cifra de empresa; ninguna sirve para inferir retención.
- Varias fuentes empíricas (F-851, F-854, F-855) tienen autores o revista sin verificar; no apoyar decisiones en sus cifras sin abrir el original.
- Las cifras de Trii se contradicen entre fuentes y no se resolvió cuál es la correcta.
- **v2.0:** las cuatro preguntas sobre desgravamen (8.1 a 8.3) y persistencia (8.4, 8.5) quedaron sin dato peruano; la norma de la SBS se leyó solo vía prensa y consultora. Los estudios de Portugal, China y Alemania tienen autor o revista sin verificar. Ninguno de los competidores publica retención de aporte. De las cinco apps de la lámina interna, no se buscó evidencia de efecto de las listas de inicio ni de los cambios de nivel (§8.11). Las cifras originales de Save More Tomorrow no se pudieron verificar (§8.12).

## Conexiones

- [[lealtad-gamificacion-recompensas-retail|Gamificación, recompensas y lealtad en retail]] — mismo problema en retail: poca evidencia causal de que el juego mueva conducta sostenida.
- [[behavioral-design-estado-disciplina|Behavioral design: estado de la disciplina y del mercado]] — crisis del nudge: los efectos de defaults y avisos suelen ser menores fuera del estudio original.
- [[fenomenos-psicologicos|Fenómenos psicológicos clásicos]] — estado de replicación del sesgo del presente, que sustenta el ahorro con compromiso.
- [[matriz-productos-vida-rimac|Matriz de productos Vida RIMAC]] — productos de vida con ahorro donde la persistencia de aporte es el indicador clave.
- [[mecanismos-seguros-salud|Mecanismos de seguros de salud]] — Vitality como caso de recompensa y caducidad, con la misma salvedad de selección.
- [[seguros-comportamiento-mundo-peru|Seguros: comportamiento y mercado, Mundo vs. Perú]] — baja confianza y educación financiera como contexto del aporte.
- [[glosario-seguro-vida-peru|Glosario de seguro de vida en lenguaje claro]] — términos de caducidad, rescate y desgravamen para leer esta evidencia.
