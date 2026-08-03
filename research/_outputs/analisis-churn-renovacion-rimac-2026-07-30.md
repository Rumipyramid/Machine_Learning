# Modelo de Churn y Matriz de Renovación RIMAC — Análisis detallado, validación con literatura, alertas y recomendaciones por ramo

> Informe basado en el documento interno `Análisis detallado — Modelo de Churn y Matriz de
> Renovación (CoE AI / GenAI)` (análisis de 2 decks: *Modelo de Churn - Visión Cliente*, abril
> 2026, 17 láminas; *Matriz de Renovación AMI y VEH*, ene-feb 2026, 24 láminas, 4 ocultas),
> cruzado con validación externa (`/trinidad`) e incorporado a la opinión de negocio de El
> Lobo (`research/lobo/opinion_experto.md`, tesis 21).
> Persistido en `research/_fuentes_internas/Analisis_Detallado_Churn_Renovacion.md` y
> `research/_nodes/modelo-churn-renovacion-rimac.md` (v1.0) del proyecto
> `Rumipyramid/Machine_Learning`. Fuentes de validación externa: F-388 a F-392 en
> `research/fuentes/codice.md`.
> Versión ampliada (más detalle y tablas completas) — 2026-07-30.

---

## 0. Cómo leer este informe — glosario de términos usados en ambos decks

Antes de los números: los dos decks originales usan las mismas palabras con significados
**distintos**. Si no se lee esta sección primero, es fácil comparar mal un modelo contra otro.

| Término | En el deck de **Churn** | En el deck de **Renovación** |
|---|---|---|
| **% Efectividad** | *Recall*: qué % del total de casos de fuga que ocurrieron en el mes está capturado dentro de esa banda de score. Ej.: la banda "Muy Alto" de Morosidad captura 69% de toda la cancelación por mora del mes. | *Precisión*: qué % de los clientes de esa banda efectivamente tuvo el resultado esperado. Ej.: 84.5% de los clientes "Muy Alto" de Persistencia VEH efectivamente persistió 12 meses. |
| **% Fuga** | *Precisión* (tasa dentro de la banda) — el rol que en Renovación cumple "% Efectividad". | No existe esta columna en Renovación. |
| **% Target** | No existe esta columna en Churn. | *Recall* — el rol que en Churn cumple "% Efectividad". |
| **Lift** | Cuántas veces más frecuente es el evento en esa banda comparado con la tasa promedio de toda la base. Un lift de x11.6 significa que esa banda tiene una tasa de fuga 11.6 veces mayor que el promedio general. | No se reporta como columna explícita en las tablas de Renovación (aunque el concepto aplica igual). |
| **Concentración / captura** | Qué % del total del evento (fuga, siniestro, no-renovación) queda "capturado" sumando las bandas de score más altas. Es la métrica central de todo el análisis: con poca base (26-36%) se captura casi todo el evento (79-91%). | Igual. |

**Por qué importa:** un lector que compare "% Efectividad" de un score de Churn contra uno de
Renovación, asumiendo que mide lo mismo, va a sacar una conclusión equivocada — en un deck es
"cuánto del problema total resuelvo apuntando aquí", en el otro es "qué tan seguro estoy de
acertar dentro de este grupo". Son preguntas de negocio distintas.

---

## 1. Resumen ejecutivo

RIMAC tiene, hoy, **tres modelos de churn** (Morosidad, APC/Pedido del Cliente, y un modelo
combinado a nivel Cliente) y **cuatro modelos de renovación** (Persistencia y Siniestralidad,
cada uno en VEH y AMI), más un quinto modelo de Renovación propiamente dicho (Modelo 1) que
existe pero no forma parte del recorrido visible del deck. En total, 7 modelos con score
visible que **concentran el evento de interés con una eficiencia por encima del benchmark
académico publicado**: capturan 79-91% del evento con solo 26-36% de la base, mientras la
literatura especializada reporta que el mejor caso documentado necesita ~50% de la base para
llegar a ~90% de captura (ver §5). La capacidad técnica de detección **no es el cuello de
botella** de esta operación.

Los dos vacíos de mayor valor de negocio están en otro lugar, y ninguno es técnico:

1. **Nadie mide la causa raíz de la cancelación voluntaria** — el 59% del churn de
   certificado (más grande que la morosidad, 41%) es una decisión activa del cliente, y
   ningún documento interno distingue si es por precio, por servicio o por competencia.
2. **El patrón inverso entre persistencia y siniestralidad en AMI vs. VEH** tiene una
   explicación teórica plausible en la literatura de selección adversa dinámica de seguros
   de salud — pero no está confirmado con el dato disponible, porque el score de RIMAC es
   *predictivo* (sobre clientes que aún no decidieron), no una medición retrospectiva de
   quién efectivamente se fue.

Este informe desarrolla ambos puntos, además de un tercer eje — alertas de calidad y
gobernanza de dato encontradas en los propios decks — y cierra con una tabla de
recomendaciones priorizadas por ramo de negocio.

---

## 2. Ramo transversal — Churn Cliente/Certificado (Morosidad + APC)

### 2.1 Qué mide el modelo y sobre qué base

El universo son **+1.8 millones de clientes titulares** no mono-desgravamen de Rímac, que en
conjunto tienen **2.9 millones de certificados** (un cliente puede tener varios certificados,
de distintos productos/ramos). Rímac construyó 3 modelos sobre esta base:

- **Modelo A — Churn APC** (a nivel certificado): probabilidad de que el cliente pida
  cancelar por decisión propia.
- **Modelo B — Churn Morosidad** (a nivel certificado): probabilidad de cancelación por
  impago.
- **Modelo C — Churn combinado** (a nivel Cliente): probabilidad de que el cliente completo
  (no un certificado puntual) fugue de Rímac.

**Timeline de gestión del modelo** (lámina 6): el mes de análisis (características que
alimentan el score) es marzo; el score se actualiza y ejecuta a fin de abril; el periodo de
**gestión anticipada** corre de abril a junio; el mes de fuga proyectada es julio; y el
modelo se mide en agosto contra lo efectivamente ocurrido. Es decir, Rímac diseñó
deliberadamente una ventana de **2-3 meses de anticipación** antes de que el cliente
efectivamente se vaya — no es un modelo reactivo.

**Fuentes de datos que alimentan el modelo** (lámina 7): sistema financiero/RCC (líneas de
crédito, productos activos — 12M de registros), productos internos de Rímac (tenencia,
prima, renovaciones, antigüedad), historial de siniestros (vehiculares y AMI), variables
socio-demográficas (26M de registros), historial de cobranza (3M de registros), historial de
campañas/comunicación, más fuentes externas (APESEG, grado de instrucción, fuerzas armadas).

### 2.2 La magnitud del problema

| Nivel | Evento mensual promedio | Volumen | Impacto |
|---|---|---|---|
| **Cliente** | Churn 2.89% | ~50.000 clientes/mes | $11.5M en primas perdidas |
| **Certificado** | Cancelación 2.45% | ~70.000 certificados/mes | Productos más cancelados: SOAT, PT (Protección/Personal accidental), VIDA |

La serie mensual de churn a nivel cliente (jul-25 a dic-25) es: 2.87%, 2.42%, 2.73%, 2.59%,
3.20%, 3.50%. **El documento reporta el promedio (2.89%) pero no comenta la tendencia
ascendente** de la segunda mitad del año (de 2.42% en agosto a 3.50% en diciembre) — vale la
pena que el equipo de negocio revise si es estacionalidad (fin de año) o una tendencia real
que se está acelerando.

**Por causa de cancelación de certificado:** Morosidad 41% · Pedido del Cliente (APC) 59%.
La cancelación voluntaria es, por sí sola, mayoría absoluta del problema.

### 2.3 Los tres scores, con el detalle completo

**Modelo de Morosidad** — "los scores de mayor propensión concentran hasta el 91% de la
cancelación por mora de certificados":

| Score | % Certificados | # Certificados | % Efectividad (recall) | % Fuga (precisión) | Lift |
|---|---|---|---|---|---|
| Muy Alto | 6% | 172K | 69% | 3.08% | x11.6 |
| Alto | 20% | 584K | 22% | 0.30% | x1.1 |
| Medio | 20% | 589K | 6% | 0.07% | x0.3 |
| Bajo | 26% | 763K | 2% | 0.02% | x0.1 |
| Muy Bajo | 27% | 783K | 1% | 0.01% | x0.04 |

*Lectura:* con solo el 6% de certificados más riesgosos, Rímac ya captura el 69% de toda la
cancelación por mora del mes. Sumando "Alto" (20% adicional), la concentración sube a 91%
con 26% de la base — el modelo más eficiente de los tres.

**Variables más relevantes de Morosidad** (de mayor a menor impacto): Producto, Ratio de
Pago en los últimos 9 meses, si es Cliente Contratante, Subcanal de adquisición, Meses de
Antigüedad, Prima Promedio anual, Ratio en Tramo 1 en los últimos 3 meses (nota: el deck no
define "Tramo 1" explícitamente — es razonable inferir que es un tramo de mora, pero no está
confirmado), # Renovaciones, Frecuencia de Pago, # Productos, Ratio en Tramo 2, Calificación
RCC, Edad, promedio de días de mora, incremento de prima, incremento de línea de crédito.

**Perfiles de Morosidad:** el perfil ALTO tiene 55% de probabilidad de haber estado en Tramo
1 en los últimos 3 meses, 2.5 productos en promedio, subcanales Worksite/BBVA, productos
PT/AMI/WS-Sepelio. El perfil BAJO es lo opuesto: 20% de probabilidad de Tramo 1, 3.5
productos, subcanales Retail/Web, productos Financieros/Vida.

**Modelo de Churn APC** — "los scores de mayor propensión concentran hasta el 85% de la
cancelación APC de certificados":

| Score | % Certificados | # Certificados | % Efectividad (recall) | % Fuga (precisión) | Lift |
|---|---|---|---|---|---|
| Muy Alto | 11% | 328K | 62% | 5.46% | x5.5 |
| Alto | 21% | 613K | 23% | 1.09% | x1.2 |
| Medio | 25% | 744K | 8% | 0.32% | x0.3 |
| Bajo | 24% | 710K | 4% | 0.18% | x0.1 |
| Muy Bajo | 18% | 540K | 3% | 0.08% | x0.05 |

*Lectura:* Muy Alto + Alto = 33% de certificados (el deck redondea 11%+21%=32% a 33%)
concentran 85% de la cancelación voluntaria.

**Variables más relevantes de APC:** Producto, Subcanal de adquisición, Meses de Antigüedad,
Prima en los últimos 6 meses, si tiene Renovación Automática activada, # Productos en los
últimos 3 meses, # Emails enviados en el año, Edad, si es Contratante, Frecuencia de Pago,
Ingresos, Ratios en Tramo 1/2/3, # Tarjetas de Crédito. **A diferencia de Morosidad, este
modelo no reporta variables numéricas de perfil por banda** (edad, # productos, % en
tramo) — solo subcanal y producto principal: perfil ALTO en subcanales Estratégicos/BBVA con
productos Vida/AMI; perfil BAJO en Retail/Worksite con productos WS-Sepelio/Protección
Familiar.

**Modelo de Churn Cliente (combinado)** — "los scores de alta propensión concentran hasta el
80% de la fuga total de clientes":

| Score | % Clientes | # Clientes | % Efectividad (recall) | % Fuga (precisión) | Lift |
|---|---|---|---|---|---|
| Muy Alto | 16% | 277K | 58% | 11.31% | x3.8 |
| Alto | 20% | 361K | 22% | 3.18% | x1.1 |
| Medio | 21% | 379K | 12% | 1.69% | x0.6 |
| Bajo | 23% | 411K | 7% | 0.82% | x0.3 |
| Muy Bajo | 20% | 396K | 1% | 0.14% | x0.05 |

Este modelo, al mezclar dos causas con drivers distintos (morosidad + APC), es el **menos
concentrado relativamente** de los tres (80% con 36% de base) — esperable, no un defecto.

**Los 3 perfiles de cliente por segmento de churn** (lámina 16) muestran un patrón
**monotónico y consistente en las 5 variables a la vez**:

| Perfil | Edad | Ingresos | Antigüedad en Rímac | Prima Total | Ratio de Pago |
|---|---|---|---|---|---|
| Alto (propensión a fuga) | 35–40 años | S/3K–4K | 10–15 meses | < $300 | 90% |
| Medio | 40–45 años | S/4K–5.5K | 18–20 meses | $400–$1K | 95% |
| Bajo (propensión a fuga) | 45–50 años | > S/7K | 24 meses | > $3K | 98% |

A mayor propensión de fuga: cliente más joven, de menor ingreso, más nuevo en Rímac, con
menor prima total y menor ratio de pago histórico — las 5 variables se mueven juntas, sin
ninguna excepción, lo que da confianza en que el modelo capturó un patrón real y no ruido.

### 2.4 Validación con literatura externa

**¿Es buena la eficiencia de concentración de estos 3 modelos?** Un benchmark académico
reciente de modelos de churn, publicado en una revista arbitrada (F-388, 🟢A — MDPI,
*Information*, 2025), evalúa modelos de machine learning/deep learning sobre datasets reales
de seguros y telecom. Reporta que un **lift de ~1.9-3.01x en el decil superior** (el 10% de
clientes de mayor riesgo) es el desempeño esperado/mejor-caso publicado en la literatura, y
que se necesitan las **5 bandas superiores (50% de la base) para capturar ~90%** de los
churners. Comparado con esto: el score "Muy Alto" de Morosidad de RIMAC tiene **lift x11.6**
— casi 4 veces el mejor caso publicado (x3.01) — y los 3 modelos de RIMAC necesitan solo
26-36% de la base para el mismo ~90% de captura que la literatura logra con 50%. No es una
comparación controlada perfecta (los datasets son distintos), pero la brecha es demasiado
grande para explicarse solo por diferencias metodológicas.

**¿Es normal que la cancelación voluntaria (59%) supere a la morosidad (41%)?** Sí. Evidencia
de industria reciente (F-389, 🟡C — cobertura especializada de seguros, 2025-2026) muestra que
~29% de los asegurados en EE.UU. cambió de aseguradora en 2025, impulsado principalmente por
presión de precio acumulada tras varios años de alzas; y que **60% de los clientes cambiaría
por mejor personalización/experiencia de servicio, no por un precio más bajo** — incluso 30%
de los clientes que se declaran "satisfechos" tiene intención de cambiar en los próximos 3
meses. El 59% de APC de RIMAC no es una anomalía local: es la manifestación de una fuerza de
industria más amplia y, según esta evidencia, creciente.

**¿La ventana de gestión anticipada (2-3 meses antes de la fuga) tiene respaldo?** Una fuente
que cita un hallazgo de revista académica (F-392, 🟡C — tratar con cautela, no se verificó
contra la fuente primaria en esta sesión) reporta que **68% de quienes cancelan una
suscripción o póliza ya tomaron esa decisión entre 30 y 90 días antes** del evento de
cancelación efectivo. La ventana de Rímac (score en abril, gestión abril-junio, fuga
proyectada en julio) cae justo dentro de ese rango — el diseño temporal del modelo está bien
calibrado según esta evidencia, aunque la cifra exacta (68%) debe tratarse como direccional.

### 2.5 🚨 Alertas de este ramo

1. **El vacío de dato más caro de todo el análisis: ningún documento reporta la causa raíz
   del 59% de APC.** No se sabe si el cliente se va por precio, por mal servicio, porque
   encontró una oferta de la competencia, o por una combinación. Sin esa variable, cualquier
   campaña de retención sobre ese 59% dispara "a ciegas" sobre la mayoría del problema.
2. El modelo Cliente combinado (láminas 15-16) **no reporta "canal" ni "producto" como
   variable explícita** — solo variables socio-demográficas y financieras. Puede ser una
   omisión de la lámina resumen (no necesariamente del modelo real), pero conviene
   confirmarlo.
3. La nota de speaker "prosperous/brokers" que aparece en las láminas 2 y 5 **no tiene
   relación aparente con el contenido de esas láminas** (definición de universo, arquitectura
   de modelos) — y aparece palabra por palabra también en el deck de Renovación. Es probable
   que sea un remanente de otro documento/presentación pegado por error. No invalida el
   modelo, pero conviene limpiarlo antes de compartir el deck fuera del equipo que lo hizo.
4. El churn mensual sube de 2.42% a 3.50% en la segunda mitad de la serie observada, sin que
   el deck lo señale — vale monitorear si continúa en los meses siguientes.

### 2.6 ✅ Recomendaciones de este ramo

1. **Instrumentar la causa raíz de la cancelación voluntaria.** La forma más rápida es una
   encuesta de salida corta (2-3 preguntas) en el flujo de cancelación; la forma más
   escalable es un modelo de clasificación de motivo entrenado sobre el histórico de
   interacciones (llamadas, chats, emails) previo a la cancelación. Es, con la evidencia
   disponible, el mayor ROI marginal de todo este análisis — el "quién" ya está resuelto, el
   "por qué" no.
2. **Diseñar tratamiento diferenciado por causa, no un único flujo de retención.** Morosidad
   es fricción operativa (candidato: recordatorios mejor diseñados, más medios de pago,
   flexibilización de fecha de cobro); APC es una decisión activa que exige entender y
   responder al motivo real antes de ofrecer un descuento genérico que puede no atacar la
   causa verdadera.
3. **Anclar cualquier journey de retención a la ventana abril-junio** ya validada por el
   modelo (y externamente consistente con el patrón de decisión 30-90 días antes del evento)
   — no diluir el esfuerzo en una campaña de intensidad pareja todo el año.

---

## 3. Ramo VEH (Vehicular)

### 3.1 Alcance y magnitud

El estudio de Renovación VEH cubre a los clientes con producto "vehicular" en periodo de
renovación: **6.4% del stock de producto (5.5K pólizas)**, sobre un total de 142K pólizas
vehiculares (88K de persona natural) y un stock de 85K pólizas. De ese universo de 5.5K por
renovar, **63% tiene asignada su primera renovación** (2.8K provienen de venta nueva
reciente) y **82% efectivamente renueva (4.5K pólizas)**.

**Journey de renovación** (lámina 3, compartido con AMI): Rímac analiza a los clientes que
llevan 9 meses con su póliza (M9) para anticipar la gestión — el score se actualiza en M9,
la ventana de gestión corre de M9 hasta el mes de renovación (M12), y el modelo predice
persistencia/siniestralidad a 12 meses **después** de esa renovación (hasta 13 meses hacia
adelante desde M9).

Pese a que la renovación es alta (82%), persistencia y siniestralidad a 12 meses generan
pérdida real:

| Métrica | Valor | Detalle |
|---|---|---|
| % Prima renovada a 12 meses (mar-24 a feb-25) | 81-84% mensual | Montos: $2.4M-$3.3M/mes |
| Pérdida por no-persistencia | **~$470K por cosecha** | Cliente renueva pero no llega a los 12 meses |
| % Ratio de siniestralidad sobre prima (mismo periodo) | 40-56% mensual | Montos: $0.89M-$1.30M/mes |
| Pérdida por siniestralidad | **~$1.0M** | Siniestros en los 12 meses posteriores a la renovación |

### 3.2 Los 3 modelos VEH, con el detalle completo

**Modelo 1 — Renovación VEH** (lámina 8, **oculta en el deck**): "en promedio los scores de
alta probabilidad concentran el [x]% de las clientes que renuevan su póliza" — el título
literalmente quedó con un placeholder "x%" sin completar.

| Score | % Efectividad (precisión) | % Leads | % Target (recall) |
|---|---|---|---|
| Muy alto | 90.8% | 26% | 28% |
| Alto | 86.2% | 27% | 28% |
| Medio | 81.3% | 23% | 23% |
| Bajo | 75.8% | 14% | 13% |
| Muy bajo | 62.5% | 11% | 8% |

Muy Alto + Alto + Medio = 79% de los clientes con mayor indicador de renovación, con
efectividad regular mensual de 82.3%. El perfil de este modelo (lámina 7, también oculta)
lista 10 variables (Nivel Socioeconómico, Canal, Edad, Ingreso Mínimo Anual, Prima
Promedio, Incremento de Gasto, Antigüedad del Vehículo, Línea de Tarjeta de Crédito,
Variación de Saldo, Mínima Antigüedad Vehicular) — pero **el campo cuantitativo "Ingreso
Promedio" aparece vacío en los tres segmentos (Verde/Ámbar/Rojo)**, sin ninguna cifra. Es
razonable que por eso ambas láminas quedaron ocultas en vez de eliminadas: el contenido
existe pero no se completó.

**Modelo 2 — Persistencia VEH** — "en promedio los scores de alta probabilidad concentran el
81% de las clientes que renuevan su póliza y persisten los 12 meses":

| Score | % Efectividad (precisión) | % Leads | % Target (recall) |
|---|---|---|---|
| Muy alto | 84.5% | 28% | 33% |
| Alto | 76.7% | 25% | 27% |
| Medio | 69.1% | 22% | 21% |
| Bajo | 58.9% | 15% | 13% |
| Muy bajo | 40.5% | 10% | 6% |

Efectividad regular mensual: 70.7%. **Variables:** Canal del Producto Contratado (la de
mayor impacto), Nivel Socioeconómico, Prima Vehicular Promedio, Incremento de Prima,
Edad, Segmento Growth, Antigüedad del Vehículo, Tarjetas de Crédito, # Productos activos,
Saldo Total. **Perfiles:** Verde (Muy Alto/Alto) = NSE A-B, segmento Growth "Prosperous",
canal Brokers, vehículo de 7-8 años. Rojo (Muy Bajo) = NSE C-D-E, canal CNT (Centro de
Negocios/Telefónico), vehículo de 4 años.

**Modelo 3 — Siniestralidad VEH** — "en promedio los scores de alta probabilidad y media
concentran el 82% de los clientes con ocurrencia de siniestralidad durante los 12 meses
después de su renovación":

| Score | % Efectividad (precisión) | % Leads | % Target (recall) |
|---|---|---|---|
| Muy alto | 26.9% | 26% | 41% |
| Alto | 19.1% | 21% | 23% |
| Medio | 15.0% | 21% | 18% |
| Bajo | 11.0% | 21% | 13% |
| Muy bajo | 6.8% | 11% | 4% |

Efectividad regular mensual: 17.2% — nótese que estos porcentajes de "% Efectividad" son
bajos comparados con Persistencia porque el siniestro es, en sí mismo, un evento poco
frecuente incluso en la banda de mayor riesgo (26.9% de precisión en "Muy alto" significa
que, de cada 100 clientes en esa banda, ~27 efectivamente tiene un siniestro en 12 meses —
alto respecto al resto de bandas, pero lejos de una certeza). **Variables:** Frecuencia de
Siniestros previos (la de mayor impacto), Prima Vehicular, Antigüedad del Vehículo,
Servicios/Emergencias registradas, Edad, variables de tarjeta de crédito, Ingreso. **Perfil
Verde** (mayor riesgo de siniestro): prima +$1K, vehículo de 4.5 años (más nuevo), ingreso
+$10K, 2-3 meses con siniestros en los últimos 36 meses. **Perfil Rojo** (menor riesgo):
prima $440, vehículo de 9 años, 0 meses con siniestros, ingreso $5K.

### 3.3 La matriz de Renovación VEH (Persistencia × Siniestralidad)

Con los dos scores (Persistencia y Siniestralidad) cruzados, Rímac construye una matriz de 25
celdas sobre una base de **5.5K certificados** y **$1M de monto anual de siniestro**:

**Distribución de certificados** (% del total en cada combinación de bandas):

| Persistencia \ Siniestralidad | Muy bajo | Bajo | Medio | Alto | Muy alto | **Total fila** |
|---|---|---|---|---|---|---|
| Muy alto | 4.51% | 6.04% | 4.20% | 3.43% | 3.26% | **21.44%** |
| Alto | 6.14% | 6.95% | 5.92% | 5.88% | 5.85% | **30.74%** |
| Medio | 6.04% | 5.92% | 4.88% | 4.61% | 4.75% | **26.20%** |
| Bajo | 4.79% | 3.42% | 2.24% | 1.97% | 2.24% | **14.66%** |
| Muy bajo | 3.62% | 1.23% | 0.90% | 0.60% | 0.60% | **6.95%** |
| **Total columna** | **25.10%** | **23.56%** | **18.14%** | **16.49%** | **16.70%** | 99.99% |

**Distribución de siniestros** (misma estructura — qué % de los siniestros reales cae en
cada celda):

| Persistencia \ Siniestralidad | Muy bajo | Bajo | Medio | Alto | Muy alto | **Total fila** |
|---|---|---|---|---|---|---|
| Muy alto | 2.42% | 4.63% | 4.63% | 5.24% | 5.24% | **22.16%** |
| Alto | 2.91% | 5.04% | 5.61% | 7.90% | 10.20% | **31.66%** |
| Medio | 3.64% | 4.71% | 4.87% | 6.06% | 7.08% | **26.36%** |
| Bajo | 2.74% | 3.28% | 2.91% | 2.70% | 3.44% | **15.07%** |
| Muy bajo | 0.98% | 0.86% | 0.98% | 0.74% | 1.19% | **4.75%** |
| **Total columna** | **12.69%** | **18.52%** | **19.00%** | **22.64%** | **27.15%** | 100.00% |

**⚠️ Nota de base:** esta matriz usa como base los **5.5K certificados del universo completo
"por renovar"**, no el subconjunto de 4.5K que efectivamente renueva — importante al
comparar tamaños con AMI (ver §4.3).

### 3.4 El patrón persistencia-siniestralidad en VEH (cálculo propio, no está en el deck)

Comparando, fila por fila de Persistencia, el % de certificados contra el % de siniestros
que le corresponde:

| Persistencia | % certificados | % siniestros | **Ratio (siniestros/certificados)** |
|---|---|---|---|
| Muy alto | 21.44% | 22.16% | 1.03 |
| Alto | 30.74% | 31.66% | 1.03 |
| Medio | 26.20% | 26.36% | 1.01 |
| Bajo | 14.66% | 15.07% | 1.03 |
| Muy bajo | 6.95% | 4.75% | **0.68** |

**Casi todas las bandas están cerca de un ratio de 1.0** — es decir, el % de certificados y
el % de siniestros que le corresponde son casi proporcionales, sin importar si la
persistencia predicha es alta o baja. La única excepción es "Muy baja persistencia", que
está claramente **subrepresentada** en siniestros (ratio 0.68): ese grupo tiene menos
siniestros de los que su tamaño relativo haría esperar.

### 3.5 Validación con literatura

El patrón de proporcionalidad ~1.0 en casi toda la matriz VEH es consistente con lo esperable
en un seguro de riesgo físico: la propensión a persistir (que depende de canal, precio,
comportamiento crediticio) y la propensión a siniestrarse (que depende de exposición y hábito
de manejo) responden a mecanismos **mayormente independientes** entre sí. No se encontró en
esta ronda de investigación literatura que prediga específicamente por qué el segmento de Muy
Baja persistencia queda subrepresentado en siniestros — se reporta como observación propia
del análisis interno, sin respaldo externo directo todavía.

### 3.6 🚨 Alertas de este ramo

1. **El perfil cuantitativo del modelo de Renovación VEH (lámina 7) está incompleto** — el
   campo "Ingreso Promedio" aparece vacío en los tres segmentos. Es plausible que sea la
   causa de que la lámina haya quedado oculta en vez de corregida.
2. **El título de la lámina 8 (scores de Renovación VEH) tiene un placeholder sin completar**
   ("concentran el x% de las clientes...") — señal adicional de que este modelo específico
   no llegó a un estado de documentación final, aunque si se use en producción según el
   diagrama de flujo del deck.
3. **La base de la matriz (5.5K) es el universo completo, no el subconjunto renovado** —
   comparar el tamaño de esta matriz contra la de AMI sin ajustar por esta diferencia de
   base lleva a una lectura incorrecta de la magnitud relativa del problema entre ramos (ver
   §4.3).

### 3.7 ✅ Recomendaciones de este ramo

1. **Completar el perfil cuantitativo de la lámina 7** (cifra de Ingreso Promedio por
   segmento) antes de usar ese modelo para segmentar campañas — hoy no es accionable sin
   esa cifra específica.
2. **Tratar persistencia y siniestralidad con palancas separadas en VEH**, dado que son
   casi independientes entre sí (salvo el extremo de Muy Baja persistencia): retención
   centrada en canal/NSE/antigüedad del vehículo; control de siniestralidad centrado en
   historial de siniestros y prima. A diferencia de AMI, **no hace falta necesariamente una
   oferta combinada por cuadrante** — el problema no está tan entrelazado.
3. **Investigar puntualmente el segmento de Muy Baja persistencia** (subrepresentado en
   siniestros, ratio 0.68) — podría tratarse del segmento de menor lealtad pero también de
   menor riesgo real, un perfil distinto al que la intuición de "cliente que se va = cliente
   problemático" sugeriría a primera vista.

---

## 4. Ramo AMI (Salud individual)

### 4.1 Alcance y magnitud

El estudio de Renovación AMI cubre a los clientes con producto "AMI" en periodo de
renovación: **7.5% del stock de producto (4.1K pólizas)**, sobre un total de 64K pólizas AMI
(56K de persona natural) y un stock de 54.6K pólizas. **43% tiene asignada su primera
renovación** (proviene de venta nueva) y **88% efectivamente renueva (3.6K pólizas)** — una
tasa de renovación aún más alta que VEH (82%).

Pese a esa renovación alta, las pérdidas de AMI son **mayores que VEH en términos absolutos,
pese a un universo menor**:

| Métrica | VEH | AMI | Diferencia |
|---|---|---|---|
| Universo "por renovar" | 5.5K | 4.1K | AMI es 25% menor en volumen |
| % que renueva | 82% | 88% | AMI renueva más |
| % Ratio de siniestralidad sobre prima | 40-56% mensual | **66-89% mensual** | AMI mucho más alto |
| Pérdida por no-persistencia | ~$470K/cosecha | **~$1.18M/cosecha** | AMI es 2.5x mayor |
| Pérdida por siniestralidad | ~$1.0M | **~$1.54M** | AMI es 1.5x mayor |

El ratio de siniestralidad base de AMI (66-89% mensual, montos de $3.7M-$5.0M/mes) es
estructuralmente más alto que VEH — consistente con que el seguro de salud cubre eventos
mucho más recurrentes (consultas, atenciones) que un seguro vehicular.

### 4.2 Los 3 modelos AMI, con el detalle completo

**Modelo 1 — Renovación AMI** (lámina 18, **oculta en el deck**): "en promedio los scores de
alta probabilidad y media concentran el 84% de los clientes que van a tener una buena
renovación":

| Score | % Efectividad (precisión) | % Leads | % Target (recall) |
|---|---|---|---|
| Muy alto | 95.5% | 26% | 31% |
| Alto | 90.5% | 27% | 28% |
| Medio | 87.7% | 23% | 25% |
| Bajo | 82.3% | 14% | 12% |
| Muy bajo | 69.7% | 11% | 4% |

Efectividad regular mensual: 88.9% — más alta que VEH (82.3%), consistente con la mayor tasa
de renovación general de AMI. **⚠️ La lámina 17 (perfil de este modelo, también oculta) tiene
un error de etiqueta real:** el título dice "las variables más importantes para el modelo de
renovación **VEH** fueron 10", pero todo el contenido (prima AMI, siniestros AMI) es de AMI —
es el mismo texto, palabra por palabra, que la lámina 7 de VEH, sin actualizar la etiqueta
(copy-paste sin corregir). **Variables:** Promedio de Productos sin Desgravamen, Prima
Promedio Anual AMI, Actividad de WhatsApp sin castigo, Permanencia Total en AMI, Variación de
Prima, Mix de Productos, Edad, Monto de Siniestros AMI, Prima Anualizada, Estado Civil.
**Perfiles:** Verde = prima AMI $1.1K, edad 45-55 años, monto de siniestro promedio $260.
Ámbar = prima $0.7-0.8K, edad 38-44, siniestro $46-65. **Rojo = prima $1.1K** (⚠️ idéntica a
Verde — ver alertas), edad ≤35, siniestro <$35.

**Modelo 2 — Persistencia AMI** — "en promedio los scores de alta probabilidad y media
concentran el 79% de los clientes que persisten durante los 12 meses después de su
renovación":

| Score | % Efectividad (precisión) | % Leads | % Target (recall) |
|---|---|---|---|
| Muy alto | 88.5% | 30% | 35% |
| Alto | 80.1% | 26% | 27% |
| Medio | 72.7% | 18% | 17% |
| Bajo | 65.8% | 15% | 13% |
| Muy bajo | 54.8% | 12% | 8% |

Efectividad regular mensual: 76.3%. **Variables:** Máximo Gasto vs. línea de Tarjeta de
Crédito (la de mayor impacto), Línea SBS, Saldo Total SBS, Nivel Socioeconómico,
Calificación Crediticia, Prima Anual AMI, Prima sin Desgravamen, Edad, # Productos,
Permanencia Total en AMI — **un modelo dominado por variables financieras/crediticias, más
que por comportamiento de uso del seguro**. **Perfiles:** Verde = prima +$1,500, Generación
X/Baby Boomer, permanencia +21 meses, edad +50. Rojo = prima <$550, Generación Z,
permanencia <12 meses, edad <35.

**Modelo 3 — Siniestralidad AMI** — "en promedio los scores de alta probabilidad y media
concentran el 80% de los clientes con propensión de siniestralidad costosa durante los 12
meses después de su renovación":

| Score | % Efectividad (precisión) | % Leads | % Target (recall) |
|---|---|---|---|
| Muy alto | 81.9% | 20% | 30% |
| Alto | 62.4% | 25% | 28% |
| Medio | 49.6% | 24% | 22% |
| Bajo | 41.8% | 18% | 13% |
| Muy bajo | 32.8% | 13% | 7% |

Efectividad regular mensual: **55.9%** — aproximadamente **3.3 veces la de VEH (17.2%)**: el
evento "siniestro en los 12 meses siguientes" es mucho más frecuente en AMI, consistente con
que las atenciones de salud son recurrentes por naturaleza (consultas, chequeos, tratamientos)
mientras que un siniestro vehicular es un evento más esporádico. **Variables:** Promedio de
Productos sin Desgravamen, Prima Anual AMI, **Promedio de mensajes de WhatsApp** (única
variable de engagement/contacto en todo el análisis, no financiera ni demográfica),
Permanencia Total, Variación de Prima, Mix de Productos, Edad, Monto de Siniestros, Prima sin
Desgravamen, Estado Civil. **Perfiles:** Verde (mayor riesgo) = Gasto Mínimo 2.8K-5.3K, NSE
A, edad +50, prima AMI $2,500+. Ámbar = mismo rango de Gasto Mínimo que Verde (⚠️ ver
alertas), NSE B-C, edad 45-50, prima $700-800. Rojo (menor riesgo) = Gasto Mínimo ≤2.5K, NSE
B-C-D, edad ≤40, prima <$700.

### 4.3 La matriz de Renovación AMI (Persistencia × Siniestralidad)

Base: **3.5K pólizas** (⚠️ ver nota de base más abajo) y **$4.3M de monto anual de
siniestro** — más de 4 veces el monto de VEH ($1M) pese a que la base de pólizas es menor.

**Distribución de pólizas:**

| Persistencia \ Siniestralidad | Muy bajo | Bajo | Medio | Alto | Muy alto | **Total fila** |
|---|---|---|---|---|---|---|
| Muy alto | 1.39% | 1.72% | 4.16% | 10.18% | 18.24% | **35.69%** |
| Alto | 1.76% | 2.34% | 6.17% | 8.39% | 7.30% | **25.96%** |
| Medio | 1.31% | 2.39% | 5.34% | 4.75% | 2.65% | **16.44%** |
| Bajo | 1.50% | 3.25% | 3.75% | 3.16% | 1.24% | **12.90%** |
| Muy bajo | 1.43% | 3.87% | 2.08% | 1.33% | 0.30% | **9.01%** |
| **Total columna** | **7.39%** | **13.57%** | **21.50%** | **27.81%** | **29.73%** | 100.00% |

**Distribución de siniestros:**

| Persistencia \ Siniestralidad | Muy bajo | Bajo | Medio | Alto | Muy alto | **Total fila** |
|---|---|---|---|---|---|---|
| Muy alto | 2.43% | 2.52% | 4.60% | 8.77% | 11.94% | **30.26%** |
| Alto | 3.14% | 3.07% | 6.75% | 7.51% | 5.15% | **25.62%** |
| Medio | 2.24% | 3.22% | 5.93% | 4.39% | 1.95% | **17.73%** |
| Bajo | 2.51% | 4.06% | 4.32% | 2.88% | 0.92% | **14.69%** |
| Muy bajo | 2.46% | 5.17% | 2.48% | 1.35% | 0.24% | **11.70%** |
| **Total columna** | **12.78%** | **18.04%** | **24.08%** | **24.90%** | **20.20%** | 100.00% |

**⚠️ Nota de base importante:** esta matriz usa 3.5K como base, una cifra **más cercana al
subconjunto que sí renueva (3.6K)** que al universo completo "por renovar" (4.1K) — un
comportamiento **distinto** al de la matriz VEH, que sí usa su universo completo (5.5K, no el
subconjunto renovado de 4.5K). Esto significa que las dos matrices no son directamente
comparables en magnitud sin ajustar primero por esta diferencia de definición de base.

### 4.4 El patrón persistencia-siniestralidad en AMI — el hallazgo central de este ramo

| Persistencia | % pólizas | % siniestros | **Ratio (siniestros/pólizas)** |
|---|---|---|---|
| Muy alto | 35.69% | 30.26% | 0.85 |
| Alto | 25.96% | 25.62% | 0.99 |
| Medio | 16.44% | 17.73% | 1.08 |
| Bajo | 12.90% | 14.69% | 1.14 |
| Muy bajo | 9.01% | 11.70% | **1.30** |

**El patrón se invierte respecto a VEH.** En vez de proporcionalidad ~1.0 en casi todas las
bandas (como en VEH), AMI muestra una tendencia **continua y monotónica**: a mayor
persistencia predicha, menos siniestros de los que el tamaño haría esperar (Muy Alta
persistencia: ratio 0.85); a menor persistencia predicha, más siniestros de los esperados
(Muy Baja persistencia: ratio 1.30). No es un solo extremo aislado como en VEH — es una
tendencia que corre a lo largo de las 5 bandas.

**Dos lecturas posibles, no distinguibles con la información disponible en el deck:**

1. **Causalidad inversa:** un siniestro costoso podría anteceder y explicar la no-renovación
   — el cliente se va *después de* o *por causa de* un siniestro (ej.: disputa con la
   cobertura, aumento de prima post-siniestro, mala experiencia en la atención).
2. **Selección por necesidad/uso:** en salud, quien más usa el seguro (más
   siniestros/atenciones) puede ser también quien más sensible es a la fricción de precio o
   condiciones al momento de renovar — no porque el siniestro "cause" la salida, sino porque
   ambas cosas (usar mucho el seguro y ser sensible a su costo de renovación) covarían en el
   mismo tipo de cliente.

Distinguir entre ambas requeriría revisar el **orden temporal real** (¿el siniestro ocurre
antes o después de la señal de no-renovación?) en la data subyacente — algo que ninguno de
los dos documentos fuente reporta.

### 4.5 Validación con literatura externa

Este es el hallazgo con la validación externa **más directa y, a la vez, la más matizada**
de todo el análisis.

La literatura de **selección adversa dinámica** en seguros de salud (F-390, 🟢A — *The
Geneva Risk and Insurance Review*, 2026, revista académica especializada en economía del
seguro) documenta que las decisiones de lapso y reinstalación de pólizas de salud están
sujetas a selección adversa: las pólizas que terminan en lapso (no renovación) tenían, antes
de eso, una experiencia de siniestros **sistemáticamente distinta** de las pólizas que
permanecen vigentes; y las pólizas que se reinstalan después de un lapso tienen mayor
probabilidad de siniestro posterior que las que nunca interrumpieron su cobertura. El mismo
mecanismo general —las personas de menor riesgo son las que más abandonan su cobertura,
dejando un pool remanente más enfermo— aparece documentado también en seguros de cuidado a
largo plazo (F-391, 🔵B, *ScienceDirect*).

**Por qué esto da un marco teórico sólido para *por qué* AMI se comporta distinto de VEH:**
el seguro de salud es un producto de uso recurrente, donde la decisión de renovar está
estructuralmente más ligada a la necesidad/costo percibido de seguir usándolo (¿estoy
tratándome algo ahora mismo? ¿me sale más barato buscar otra alternativa?) que en un seguro
de riesgo físico como el vehicular, donde persistir o no tiene poca relación con cuánto se
ha usado el auto.

**Por qué esto NO confirma la dirección exacta encontrada en RIMAC, y hay que decirlo con
esa precisión:** el dato de RIMAC es ***predictivo*** — dos scores separados (Persistencia y
Siniestralidad) calculados sobre clientes que **todavía no han decidido** si renovar o no —
mientras que la literatura citada mide, en su mayoría, la experiencia de siniestros
***retrospectiva*** de clientes que **ya** lapsaron o se reinstalaron. Son preguntas de
investigación relacionadas pero no idénticas. La lectura correcta es: la literatura da el
marco teórico *más cercano encontrado* para explicar por qué el mecanismo se invierte entre
salud y vehicular — no una confirmación causal cerrada del patrón exacto de RIMAC.

### 4.6 🚨 Alertas de este ramo

1. **Etiqueta cruzada confirmada (lámina 17):** el título dice "modelo de renovación VEH"
   estando enteramente en la sección AMI, con contenido 100% de AMI — copy-paste de la
   lámina 7 sin actualizar la etiqueta.
2. **Prima idéntica ($1.1K) entre los segmentos Verde y Rojo** del perfil de Renovación AMI
   (lámina 17) — llamativo porque el resto del perfil de cada segmento (edad, monto de
   siniestro) sí es consistente con menor propensión en Rojo. Puede ser un dato real (esa
   variable específica no discrimina entre esos dos extremos) o un error de copiado —
   **confirmar contra el archivo original antes de usar esta cifra en cualquier decisión**.
3. **Rango de "Gasto Mínimo" idéntico (2.8K-5.3K) entre Verde y Ámbar** del perfil de
   Siniestralidad AMI (lámina 21) — misma ambigüedad: podría ser correcto (la variable no
   discrimina esos dos segmentos) o un error.
4. **La base de la matriz de renovación (3.5K) usa una definición distinta a la de VEH** —
   cercana al subconjunto renovado (3.6K), no al universo completo (4.1K). No comparar el
   tamaño de ambas matrices sin ajustar por esta diferencia.

### 4.7 ✅ Recomendaciones de este ramo

1. **Investigar el orden temporal real entre siniestro y señal de no-renovación** en la data
   subyacente. Es la única forma de confirmar si el mecanismo dominante es selección por
   necesidad/uso o causalidad inversa (el siniestro empuja directamente a no renovar) — la
   respuesta cambia el diseño de la intervención: si es selección por uso, la retención debe
   enfocarse en el costo/valor percibido del seguro; si es causalidad inversa, debe enfocarse
   en la experiencia del proceso de siniestro (rapidez, transparencia, trato).
2. **Diseñar una oferta específica para el cuadrante "alta siniestralidad + baja
   persistencia"** — combinando las tablas de §4.3, ese cuadrante concentra una proporción
   desproporcionada de pérdida potencial doble (el cliente se va Y cuesta caro mientras se
   queda), y la matriz ya lo aísla con precisión sin que exista todavía una jugada de negocio
   propuesta para él específicamente.
3. **Investigar la actividad de WhatsApp como palanca posible, no solo como variable
   pasiva de scoring.** Es la única variable de engagement/contacto (no financiera ni
   demográfica) que aparece entre los 10 drivers principales del modelo de Siniestralidad
   AMI — vale entender si el canal de contacto en sí mismo es accionable (más o mejor
   contacto podría reducir fricción de renovación) antes de tratarlo solo como una señal que
   el modelo predice mas no puede modificar.
4. **Corregir la etiqueta cruzada de la lámina 17 y verificar las dos cifras duplicadas**
   (prima Verde/Rojo en Renovación; gasto mínimo Verde/Ámbar en Siniestralidad) contra el
   archivo original antes de usar el deck para una decisión de negocio o de presentarlo fuera
   del equipo que lo construyó.

---

## 5. Alertas transversales de gobernanza de datos (aplican a ambos ramos)

1. **"% Efectividad" significa cosas opuestas en cada deck** (ver glosario, §0). En Churn es
   *recall*; en Renovación es *precisión*. Es el riesgo de lectura más silencioso de todo el
   análisis porque el nombre de la columna es idéntico en ambos documentos.
2. **4 de las 24 láminas del deck de Renovación están ocultas** (7, 8, 17, 18) — el Modelo 1
   (probabilidad de buena renovación) de VEH y de AMI, en su totalidad, no forma parte del
   recorrido "visible" que se proyectaría en una presentación, aunque sí se usa como insumo
   de los otros dos modelos según el propio diagrama de flujo del deck (lámina 2).
3. **La nota de speaker "prosperous/brokers" se repite, idéntica, en ambos decks** en
   láminas sin relación aparente con su contenido — indicio de una plantilla o slide maestro
   reutilizado sin revisar el contenido de las notas.
4. **Ambos documentos validan con *backtest fuera de tiempo*, no con una intervención real
   ya desplegada.** Es la limitación más importante de todo el conjunto: mide qué tan bien
   *habría funcionado* el score sobre datos históricos, no el efecto real de gestionar
   activamente a un segmento hoy. El "Piloto" (próximo hito del roadmap de Renovación, sin
   fecha definida todavía) es lo único que puede confirmar si la altísima concentración de
   estos modelos efectivamente se traduce en menos churn o mejor persistencia una vez que se
   actúa sobre ella.
5. Ninguno de los dos documentos indica qué método se usó para rankear la "importancia" de
   las variables (¿coeficiente de un modelo lineal, SHAP, feature importance de árboles?) —
   sin saberlo, no se puede comparar el peso de una variable entre un modelo y otro con
   precisión.

---

## 6. Tabla resumen — recomendaciones priorizadas

| # | Ramo | Recomendación | Por qué es prioritaria |
|---|---|---|---|
| 1 | Transversal | Instrumentar causa raíz del 59% de cancelación voluntaria (APC) | Mayor volumen de churn de todo el análisis, cero visibilidad de motivo hoy |
| 2 | AMI | Investigar orden temporal siniestro ↔ no-renovación | Determina si el mecanismo es selección por uso o causalidad inversa — cambia el diseño completo de la intervención |
| 3 | AMI | Diseñar oferta para el cuadrante alta-siniestralidad / baja-persistencia | Mayor pérdida potencial doble ya identificada por la matriz, sin jugada propuesta todavía |
| 4 | Transversal | Tratamiento diferenciado por causa (Morosidad vs. APC), no un flujo único | Evita desperdiciar la ventana de gestión de 2-3 meses ya bien diseñada |
| 5 | VEH | Completar el perfil cuantitativo de la lámina 7 (Ingreso Promedio) | El modelo de Renovación VEH no es accionable para segmentación sin esa cifra |
| 6 | Transversal | Unificar/documentar el significado de "% Efectividad" entre ambos decks | Riesgo silencioso de decisión de negocio basada en una lectura cruzada incorrecta |
| 7 | AMI | Corregir la etiqueta cruzada de la lámina 17 y verificar las 2 cifras duplicadas | Riesgo de credibilidad si el deck circula fuera del equipo sin corregir |
| 8 | AMI | Investigar "actividad de WhatsApp" como palanca accionable | Única variable de engagement entre los principales drivers — oportunidad no explorada |
| 9 | VEH | Revisar el segmento de Muy Baja persistencia (subrepresentado en siniestros) | Perfil de negocio potencialmente distinto al que la intuición sugiere |

---

## 7. Limitaciones de este informe

- La comparación de lift/concentración (§2.4) usa un benchmark académico construido sobre
  datasets distintos a los de RIMAC (seguros/telecom internacionales, no necesariamente
  peruanos) — la dirección de la comparación es robusta, pero no es una comparación
  controlada exacta entre metodologías idénticas.
- La validación teórica del patrón AMI/VEH (§4.5, selección adversa dinámica) es el marco
  más cercano encontrado en la literatura, no una confirmación causal — el dato de RIMAC es
  predictivo, la literatura citada es mayormente retrospectiva. Se reporta como hipótesis
  mejor sustentada, no como hallazgo cerrado.
- No se investigó específicamente el mercado peruano de switching/cancelación de seguros —
  la validación de industria sobre cancelación voluntaria (§2.4) es mayormente de EE.UU.
- Ninguna recomendación de este informe reemplaza la verificación de las cifras exactas
  contra los archivos PowerPoint originales antes de usarlas en un documento externo o una
  decisión de negocio formal — varias cifras puntuales quedaron marcadas explícitamente como
  "a verificar" a lo largo del análisis.

---

*Fuente completa y versionada: `research/_nodes/modelo-churn-renovacion-rimac.md` (v1.0) y
`research/lobo/opinion_experto.md` (tesis 21). Documento primario:
`research/_fuentes_internas/Analisis_Detallado_Churn_Renovacion.md`. Fuentes de validación
externa F-388 a F-392 en `research/fuentes/codice.md`.*
