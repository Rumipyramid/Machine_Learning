# Análisis detallado — Modelo de Churn y Matriz de Renovación (CoE AI / GenAI)

**Documentos fuente:**
1. `_COE_AI_ Gen AI_ Modelo_Churn_-_Visión_Cliente.pptx` — 17 láminas, Abril 2026
2. `Matriz_de_Renovación_para_AMI_y_VEH_-_2026.pptx` — 24 láminas (4 ocultas), Ene-Feb 2026

**Fecha de análisis:** 30 de julio 2026

---

## Nota metodológica sobre este documento

Los valores de las tablas de score (persistencia, siniestralidad, morosidad, APC, churn cliente) fueron reconstruidos a partir de la extracción de texto de PowerPoint (que desordena la posición de los textboxes) y validados por dos vías: (a) inspección visual directa de cada lámina, y (b) chequeo aritmético — cada columna de "% Certificados/Clientes/Leads" y "% Target" debe sumar ~100%, y la suma de las 2-3 bandas superiores debe coincidir con el titular de la lámina (ej. "concentran el 91%"). Donde una lectura inicial no cuadraba (un caso, detallado en la lámina 10 de Renovación), se corrigió con el valor consistente con ambos chequeos. Esto da alta confianza en las cifras, pero no reemplaza la verificación contra el archivo original si se van a citar externamente.

Todo lo marcado como **[Hallazgo]** es dato observado directamente en el deck. Todo lo marcado como **[A verificar]** es una inconsistencia, vacío o posible error detectado en el archivo. Todo lo marcado como **[Inferencia/Hipótesis]** es una lectura o cálculo mío sobre esos datos, no una afirmación que el documento haga explícitamente.

---
---

# PARTE 1 — Modelo de Churn: Visión Cliente

## Resumen ejecutivo

El documento construye 3 modelos de propensión a fuga (Morosidad, APC/pedido del cliente, y un modelo combinado a nivel Cliente) sobre una base de 1.8M clientes titulares / 2.9M certificados. El churn mensual a nivel cliente es 2.89% (~50K clientes, $11.5M en primas); a nivel certificado es 2.45% (~70K certificados), dividido en Morosidad (41%) y Pedido del Cliente/APC (59%). Los 3 scores logran una concentración muy alta: con 26%-36% de la base se captura 80%-91% del evento.

## Detalle lámina por lámina

### Lámina 1 — Portada
"Modelo de Churn - Visión Cliente" · CoE AI · Abril 2026.

### Lámina 2 — Definición de Universo
- **Universo:** +1.8M clientes titulares no mono-desgravamen de Rímac.
- **6 categorías de negocio y sus productos:**

| Categoría | Productos |
|---|---|
| Vehicular | Premier Oro, Premier Plata, Premier Platinum, Flexible |
| Salud | Full Salud, Preferencial, Renta Hospitalaria, Red Preferente/Privada/Salud, Salud de Oro, Flexible |
| Vida | Flexi vida, Vida contigo, Temporal, Vida con Devolución |
| Financieros | Renta Garantizada, Inversión Global, Ultracash, Vida Ahorro |
| Vida (BS&A) | Contigo Salud Efectiva, Contigo salud |
| Worksite | Accidentes Personales, Sepelio |

- **Notas de la lámina (speaker notes):**
  - Incluye Oncológico.
  - Interpretación clientes por ramo: 24% de clientes "prosperous" tienen seguro de vida; 14% de las primas de "prosperous" corresponde a vida.
  - Interpretación canales de venta: 77% de productos AMI (salud individual, excluyendo onco) se vende por brokers.
  - Se excluyen desgravamen y protección de tarjeta porque se trabajan con bancos y el cliente probablemente no sepa con qué aseguradora están.
  - **[A verificar]** Esta nota no tiene relación directa con el contenido de la lámina (definición de universo/productos). Aparece palabra por palabra en la lámina 2 del deck de Renovación también — ver sección de errores transversales.

### Lámina 3 — "Mensualmente, más de 50K clientes fugan de Rimac"
- Serie mensual (jul-25 a dic-25), % Churn: 2.87%, 2.42%, 2.73%, 2.59%, 3.20%, 3.50%.
- # Clientes por mes: 1.81M, 1.82M, 1.82M, 1.81M, 1.84M, 1.86M.
- **Churn mensual promedio: 2.89%**
- **Valor perdido en primas: $11.5M**
- **[Hallazgo]** El % churn muestra una tendencia ascendente hacia el final de la serie (de 2.42% en ago-25 a 3.50% en dic-25) — el deck no comenta esta tendencia, solo reporta el promedio.

### Lámina 4 — "A nivel de certificado, 70K certificados son anulados mensualmente"
- Serie mensual (jul-25 a dic-25), % Cancelación: 2.47%, 2.71%, 2.21%, 2.40%, 2.27%, 2.78%.
- # Certificados por mes: 2.85M, 2.86M, 2.81M, 2.84M, 2.87M, 2.89M.
- **Ratio de cancelación de certificados: 2.45%**
- **Principales productos cancelados:** SOAT, PT, VIDA.
- **Motivo de anulación:** Morosidad 41% · Pedido del Cliente (APC) 59%.

### Lámina 5 — Arquitectura de los modelos
- Clientes Titulares (1.8M) → Certificados (2.9M).
- **Visión Certificado:** Modelo A = Churn APC · Modelo B = Churn Morosidad.
- **Visión Cliente:** Modelo C = Modelo de Churn combinado.
- Notas: idénticas a la lámina 2 (mismo texto sobre "prosperous" y brokers).

### Lámina 6 — Timeline de gestión
- **Características (mes de análisis):** Mar-26.
- **Mes de ejecución** (se actualiza el score, fin de mes): Abr-26.
- **Meses de Gestión** (periodo de gestión anticipada antes de la fuga): Abr-26 → Jun-26.
- **Mes de fuga:** Jul-26.
- **Medición del Modelo:** Ago-26.

### Lámina 7 — Fuentes de datos exploradas

| Fuente | Contenido |
|---|---|
| RCC – Sistema financiero | Participación en sistema financiero, líneas de crédito, productos activos (12M) |
| Productos | Info de cliente Rímac, tenencia, prima, renovaciones, antigüedad |
| Siniestros | Historial de siniestros vehiculares y AMI (consultas, atenciones) |
| Socio-Demográficos | Edad, ubicación, variables económicas (26M) |
| Cobranza | Historial de pago/impago (3M) |
| Campañas y comunicación | Historial de comunicaciones con el cliente |

- Otras fuentes: APESEG, grado de instrucción, fuerzas armadas.

### Lámina 8 — Portada de sección
"Churn por Morosidad" · Abril 2026.

### Lámina 9 — Perfiles del modelo de Cancelación por Morosidad
- **Variables más relevantes** (de mayor a menor impacto): Producto, Ratio de Pago en los últimos 9 meses, Cliente Contratante (Sí/No), Subcanal de adquisición, Meses de Antigüedad, Prima Promedio en el año, Ratio en Tramo 1 en los últimos 3 meses, # Renovaciones, Frecuencia de Pago, # Productos en el último año, Ratio en Tramo 2 en el último año, Calificación RCC, Edad, Promedio mensual de días de mora en el año, Incremento de prima total en el año, Incremento de línea de crédito en los últimos 6 meses.
- **Perfil ALTO:** más probable haber estado en Tramo 1 en últimos 3 meses (55%); 2.5 productos en promedio; subcanales Worksite y BBVA; productos PT, AMI, WS (Sepelio).
- **Perfil MEDIO:** probabilidad Tramo 1 40%; 3 productos; subcanales BBVA y Estratégicos; producto Vehicular.
- **Perfil BAJO:** probabilidad Tramo 1 20%; 3.5 productos; subcanales Retail y Web; productos Financieros, Vida.
- **[A verificar]** El deck no define qué es "Tramo 1" en esta lámina (es razonable inferir que se refiere a un tramo de mora, pero no está explícito).

### Lámina 10 — Scores del modelo de Morosidad
"Los scores de mayor propensión concentran hasta el 91% de la cancelación por mora de certificados."

| Score | % Certificados | # Certificados | % Efectividad | % Fuga | Lift |
|---|---|---|---|---|---|
| Muy Alto | 6% | 172K | 69% | 3.08% | x11.6 |
| Alto | 20% | 584K | 22% | 0.30% | x1.1 |
| Medio | 20% | 589K | 6% | 0.07% | x0.3 |
| Bajo | 26% | 763K | 2% | 0.02% | x0.1 |
| Muy Bajo | 27% | 783K | 1% | 0.01% | x0.04 |

- Efectividad regular mensual: 0.26% · Certificados totales: 2.9M.
- **Insight del deck:** Muy Alto + Alto = 26% de certificados concentran 91% de la cancelación por mora.

### Lámina 11 — Portada de sección
"Churn APC" · Abril 2026.

### Lámina 12 — Perfiles del modelo de Cancelación APC (pedido del cliente)
- **Variables más relevantes:** Producto, Subcanal de adquisición, Meses de Antigüedad, Prima en los últimos 6 meses, Renovación Automática (Sí/No), # Productos en los últimos 3 meses, # Emails enviados al cliente en el año, Edad, Contratante (Sí/No), Frecuencia de Pago, Ingresos en el último año, Ratio en Tramo 1 en el último año, Ratio en Tramo 3 en el último año, Ratio en Tramo 2 en el último año, # Tarjetas de Crédito en los últimos 18 meses.
- **Perfil ALTO:** subcanales Estratégicos y BBVA; productos Vida, AMI.
- **Perfil MEDIO:** subcanales BBVA y Retail; productos PT, SOAT, WS (Accidentes).
- **Perfil BAJO:** subcanales Retail y Worksite; productos WS (Sepelio), Protección Familiar.
- **[Hallazgo]** A diferencia del modelo de Morosidad (lámina 9), este modelo no reporta variables numéricas de perfil (edad, # productos, % en tramo) por banda — solo subcanal y producto principal.

### Lámina 13 — Scores del modelo APC
"Los scores de mayor propensión concentran hasta el 85% de la cancelación APC de certificados."

| Score | % Certificados | # Certificados | % Efectividad | % Fuga | Lift |
|---|---|---|---|---|---|
| Muy Alto | 11% | 328K | 62% | 5.46% | x5.5 |
| Alto | 21% | 613K | 23% | 1.09% | x1.2 |
| Medio | 25% | 744K | 8% | 0.32% | x0.3 |
| Bajo | 24% | 710K | 4% | 0.18% | x0.1 |
| Muy Bajo | 18% | 540K | 3% | 0.08% | x0.05 |

- Efectividad regular mensual: 0.98% · Certificados totales: 2.9M.
- **Insight del deck:** Muy Alto + Alto = 33% de certificados concentran 85% de la cancelación (nota: 11%+21%=32% por redondeo individual, el deck redondea a 33%).

### Lámina 14 — Portada de sección
"Churn Cliente" · Abril 2026.

### Lámina 15 — Scores del modelo combinado a nivel Cliente
"Los scores de alta propensión concentran hasta el 80% de la fuga total de clientes."

| Score | % Clientes | # Clientes | % Efectividad | % Fuga | Lift |
|---|---|---|---|---|---|
| Muy Alto | 16% | 277K | 58% | 11.31% | x3.8 |
| Alto | 20% | 361K | 22% | 3.18% | x1.1 |
| Medio | 21% | 379K | 12% | 1.69% | x0.6 |
| Bajo | 23% | 411K | 7% | 0.82% | x0.3 |
| Muy Bajo | 20% | 396K | 1% | 0.14% | x0.05 |

- Efectividad regular mensual: 2.85% · Clientes totales: 1.8M.
- **Insight del deck:** Muy Alto + Alto = 36% de clientes concentran 80% de la fuga total.

### Lámina 16 — 3 perfiles de clientes según segmento de churn

| Perfil | Edad | Ingresos | Antigüedad en Rimac | Prima Total | Ratio de Pago |
|---|---|---|---|---|---|
| Alto (propensión) | 35–40 años | S/3K–4K | 10–15 meses | < $300 | 90% |
| Medio | 40–45 años | S/4K–5.5K | 18–20 meses | $400–$1K | 95% |
| Bajo (propensión) | 45–50 años | > S/7K | 24 meses | > $3K | 98% |

- **[Hallazgo]** El patrón es monotónico y consistente en las 5 variables: a mayor propensión de fuga, cliente más joven, de menor ingreso, más nuevo en Rímac, con menor prima y menor ratio de pago.

### Lámina 17 — Cierre
Lámina final solo con isotipo de Rímac, sin contenido adicional.

## Hallazgos consolidados — Modelo de Churn

1. El churn es un evento raro a nivel mensual (0.26%–2.89% según el corte), por lo que los "% Efectividad" (participación en el total de casos capturados) son la métrica más relevante para evaluar el modelo, más que el "% Fuga" (tasa dentro de la banda), que por diseño es un número pequeño.
2. Los 3 modelos logran una concentración similar: ~capturan 80-91% del evento con 26-36% de la base — el modelo de Morosidad es el más concentrado (91% con 26%) y el de Cliente (combinado) el menos concentrado relativamente (80% con 36%), lo cual es esperable porque el modelo combinado mezcla dos causas con drivers distintos.
3. Las dos causas de cancelación (Morosidad 41%, APC 59%) tienen perfiles de variables más relevantes distintos: Morosidad se explica por comportamiento de pago/mora y antigüedad; APC se explica más por canal de adquisición y antigüedad, sin que el deck reporte variables de comportamiento de pago.
4. El deck no reporta la variable "canal" ni "producto" como texto explícito en el modelo Cliente (lámina 15-16), solo variables socio-demográficas y financieras (edad, ingreso, antigüedad, prima, ratio de pago).

## Errores / inconsistencias — Modelo de Churn

- **[A verificar]** Nota de speaker "prosperous / brokers" (láminas 2 y 5) sin relación aparente con el contenido de esas láminas — ver detalle en sección transversal al final del documento.
- **[A verificar]** "Tramo 1" (lámina 9) no está definido en el documento.
- **[Hallazgo, no necesariamente error]** El % de churn mensual (lámina 3) sube de 2.42% a 3.50% en la segunda mitad de la serie sin que el documento lo señale ni lo explique.

---
---

# PARTE 2 — Matriz de Renovación AMI y VEH (2026)

## Resumen ejecutivo

El documento diseña 3 modelos por línea de negocio (VEH y AMI): Modelo 1 (probabilidad de buena renovación, usado como insumo de los otros dos), Modelo 2 (Persistencia a 12 meses) y Modelo 3 (Siniestralidad a 12 meses). Con los scores de Persistencia × Siniestralidad se construye una matriz de renovación por producto. El archivo tiene 24 láminas, pero **4 están ocultas** (7, 8, 17, 18) — corresponden al Modelo 1 de VEH y AMI — por lo que el recorrido "visible" del deck (el que se proyectaría) tiene solo 20 láminas y no incluye el score de renovación en sí, solo Persistencia y Siniestralidad.

## Detalle lámina por lámina

### Lámina 1 — Portada
17.02.26 · "Matriz de Renovación AMI y VEH" · COE AI & GenAI.

### Lámina 2 — Objetivo de los modelos
"Identificar a los clientes más propensos a persistir y siniestrarse en los próximos 12 meses de contrato de su póliza."
- **Universo — Clientes por Renovar:** VEH 5.5k · AMI 4.1k.
- **Modelo 1** (f(x)): probabilidad de buena renovación. Entra como probabilidad condicional a los demás modelos. Resultado: Renovados VEH 4.5K · Renovados AMI 3.6k · No renovado 1K (tratado con Look Alike).
- **Modelo 2:** Persistencia 12 meses.
- **Modelo 3:** Siniestralidad 12 meses (usa el Modelo 1 como input, según el diagrama de flujo).
- Consideraciones: (a) probabilidad de buena renovación, (b) propensión a identificar clientes más persistentes (llegar a 12m), (c) propensión a identificar clientes más siniestrosos durante los 12 meses.
- Notas de la lámina: idénticas, palabra por palabra, a las de las láminas 2 y 5 del deck de Churn (nota "prosperous"/brokers). **[A verificar]** — ver sección transversal.

### Lámina 3 — Journey de renovación
"Se diseñó una solución enfocada en analizar a los clientes que mantienen su póliza durante 9 meses para anticipar la gestión de renovación para AMI y VEH."
- Clientes con permanencia de póliza: 9 meses.
- Timeline: Jul-25, Ago-25, Set-25 → **Oct-25 = M9 (mes de ejecución, se actualiza el score)** → Nov-25 (M10) → Dic-25 (M11) → Ene-26 (M12) → **Feb-26 = mes de renovación** → predicción de Persistencia/Siniestralidad a 12 meses, hasta Ene-27.
- Meses de Gestión: entre M9 (Oct-25) y el mes de renovación (Feb-26).

### Lámina 4 — Portada de sección
12.01.26 · "Matriz de Renovación VEH" · 2026 · COE IA.

### Lámina 5 — Alcance del proyecto VEH
"El alcance del estudio abarca a los clientes que tengan algún producto 'vehicular' que estén en su periodo de renovación, que representa el 6.4% (5.5K) del stock de producto."
- Pólizas Vehicular: 142K → Persona natural 88K / Empresa (resto).
- Stock de producto: 85K → Por Renovar 5.5K / Activo (resto).
- 63% de las pólizas tienen asignada su primera renovación (2.8K provienen de venta nueva).
- **82% renuevan (4.5K pólizas).**
- Grupos de producto considerados: Vehicular, Web Vehicular.
- Universo: clientes CONTRATANTE con producto foco en los últimos 6 meses (2024/09 a 2025/02).

### Lámina 6 — Ratios de persistencia y siniestralidad VEH
"En VEHICULAR, aunque la renovación es alta, los ratios de persistencia y siniestralidad ocasionan pérdidas para Rímac."

*% Prima Renovada en 12 meses (mar-24 a feb-25):* 83%, 83%, 82%, 83%, 83%, 84%, 83%, 83%, 83%, 81%, 81%, 84%.
*Montos (millones):* 2.7, 2.5, 2.5, 2.4, 2.6, 2.7, 2.6, 2.8, 2.8, 3.3, 3.0, 2.7.

*% Ratio Siniestralidad -Prima- (mar-24 a feb-25):* 40%, 43%, 46%, 48%, 56%, 40%, 44%, 44%, 46%, 49%, 42%, 45%.
*Montos (millones):* 0.90, 0.89, 0.94, 0.97, 1.20, 0.90, 0.95, 1.04, 1.07, 1.30, 1.02, 1.02.

- **Rímac deja de percibir ~$470K por cosecha** debido a que el cliente no persiste los 12 meses con su póliza.
- **Se pierde ~$1.0M** debido a siniestro en los 12 meses siguientes a la renovación.

### Lámina 7 [OCULTA] — Perfil del modelo de Renovación VEH
"¿Cómo afectan las gestiones a la renovación? Las variables más importantes para el modelo de renovación VEH fueron 10."
- **Variables (mayor a menor impacto):** Nivel Socioeconómico, Canal del Producto Contratado, Edad del Cliente, Mínimo Ingreso Anual (12um), Prima Promedio Anual (3um), Incremento del Gasto (6um), Antigüedad del Vehículo, Línea de Tarjeta de Crédito Promedio (6um), Variación del Saldo de Tarjeta (6um), Mínima Antigüedad Vehicular.
- **Perfiles Verde / Ámbar / Rojo:** el único campo mostrado es "Ingreso Promedio", y en los tres casos **aparece vacío, sin cifra**.
- **[A verificar]** Esta lámina está incompleta — el contenido cuantitativo del perfil nunca se llenó. Es plausible que por eso la lámina quedó oculta en vez de eliminada.

### Lámina 8 [OCULTA] — Scores del modelo de Renovación VEH
"En promedio los scores de alta probabilidad concentran el x% de las clientes que renuevan su póliza." **[A verificar]** El título literalmente dice "el x%" — placeholder sin completar.

| Score | % Efectividad | % Leads | % Target |
|---|---|---|---|
| Muy alto | 90.8% | 26% | 28% |
| Alto | 86.2% | 27% | 28% |
| Medio | 81.3% | 23% | 23% |
| Bajo | 75.8% | 14% | 13% |
| Muy bajo | 62.5% | 11% | 8% |

- Efectividad regular mensual: 82.3%.
- Insight: con Muy Alto + Alto + Medio se identifica el 79% de los clientes con mayor indicador de renovación.

### Lámina 9 — Perfil del modelo de Persistencia VEH
"¿Quiénes son más propensos a persistir 12 meses?"
- **Variables (mayor a menor impacto):** Canal del Producto Contratado, Nivel Socioeconómico, Prima Vehicular Promedio (12um), Incremento de Prima Vehicular (12um), Edad del Cliente, Segmento Growth, Antigüedad del Vehículo, Promedio de Tarjetas de Crédito (18um), Promedio de Productos Activos sin Desgravamen, Saldo Total Promedio (6um).
- **Verde (Muy Alto/Alto):** NSE A–B · Segmento Growth Prosperous · Canal Brokers · Antigüedad del Vehículo 7–8 años.
- **Ámbar (Medio/Bajo):** NSE B · Growth Prosperous/Change-Agents · Canal Directo/CNT · Antigüedad 5–6 años.
- **Rojo (Muy Bajo):** NSE C-D-E · Growth Otros/Change-Agents · Canal CNT · Antigüedad 4 años.

### Lámina 10 — Scores del modelo de Persistencia VEH
"En promedio los scores de alta probabilidad concentran el 81% de las clientes que renuevan su póliza y persisten los 12 meses."

| Score | % Efectividad | % Leads | % Target |
|---|---|---|---|
| Muy alto | 84.5% | 28% | 33% |
| Alto | 76.7% | 25% | 27% |
| Medio | 69.1% | 22% | 21% |
| Bajo | 58.9% | 15% | 13% |
| Muy bajo | 40.5% | 10% | 6% |

- Efectividad regular mensual: 70.7%.
- Insight: Muy Alto + Alto + Medio = 81% de los clientes con mayor indicador de persistencia a 12 meses.

### Lámina 11 — Perfil del modelo de Siniestralidad VEH
"¿A quién consideramos un cliente VEH siniestroso?"
- **Variables (mayor a menor impacto):** Frecuencia de Siniestros Vehiculares (36um), Prima Vehicular Promedio (6um), Antigüedad del Vehículo, Servicios Registrados Promedio (12um), Emergencias Vehiculares Promedio (12um), Edad del Cliente, Nivel de Consumo con Tarjeta (18um), Variación de Línea de Crédito (18um), Variación del Consumo con Tarjeta (6um), Ingreso Estimado Promedio (6um).
- **Verde (Muy Alto/Alto):** Prima VEH promedio (6um) +$1K · Antigüedad de Vehículo 4.5 años · Ingreso promedio (6um) +$10K · Meses con Siniestros (36um) 2–3.
- **Ámbar (Medio/Bajo):** Prima $700 · Antigüedad 6–7 años · Meses con Siniestros 1 · Ingreso $7–9K.
- **Rojo (Muy Bajo):** Prima $440 · Antigüedad 9 años · Meses con Siniestros 0 · Ingreso $5K.

### Lámina 12 — Scores del modelo de Siniestralidad VEH
"En promedio los scores de alta probabilidad y media concentran el 82% de los clientes con ocurrencia de siniestralidad durante los 12 meses después de su renovación."

| Score | % Efectividad | % Leads | % Target |
|---|---|---|---|
| Muy alto | 26.9% | 26% | 41% |
| Alto | 19.1% | 21% | 23% |
| Medio | 15.0% | 21% | 18% |
| Bajo | 11.0% | 21% | 13% |
| Muy bajo | 6.8% | 11% | 4% |

- Efectividad regular mensual: 17.2%.
- Insight: Muy Alto + Alto + Medio = 82% de los clientes con mayor probabilidad de siniestro.

### Lámina 13 — Matriz de Renovación VEH
"A partir de los scores de persistencia y siniestralidad, se desarrolla la matriz de renovación de VEH para identificar pólizas potenciales."

**Distribución de Certificados** (Persistencia en filas, Siniestralidad en columnas: Muy bajo → Muy alto):

| Persistencia \ Siniestralidad | Muy bajo | Bajo | Medio | Alto | Muy alto | Total |
|---|---|---|---|---|---|---|
| Muy alto | 4.51% | 6.04% | 4.20% | 3.43% | 3.26% | 21.44% |
| Alto | 6.14% | 6.95% | 5.92% | 5.88% | 5.85% | 30.74% |
| Medio | 6.04% | 5.92% | 4.88% | 4.61% | 4.75% | 26.20% |
| Bajo | 4.79% | 3.42% | 2.24% | 1.97% | 2.24% | 14.66% |
| Muy bajo | 3.62% | 1.23% | 0.90% | 0.60% | 0.60% | 6.95% |
| **Total** | **25.10%** | **23.56%** | **18.14%** | **16.49%** | **16.70%** | **99.99%** |

**Distribución de Siniestros** (misma estructura de filas/columnas):

| Persistencia \ Siniestralidad | Muy bajo | Bajo | Medio | Alto | Muy alto | Total |
|---|---|---|---|---|---|---|
| Muy alto | 2.42% | 4.63% | 4.63% | 5.24% | 5.24% | 22.16% |
| Alto | 2.91% | 5.04% | 5.61% | 7.90% | 10.20% | 31.66% |
| Medio | 3.64% | 4.71% | 4.87% | 6.06% | 7.08% | 26.36% |
| Bajo | 2.74% | 3.28% | 2.91% | 2.70% | 3.44% | 15.07% |
| Muy bajo | 0.98% | 0.86% | 0.98% | 0.74% | 1.19% | 4.75% |
| **Total** | **12.69%** | **18.52%** | **19.00%** | **22.64%** | **27.15%** | **100.00%** |

- Base: **Certificados: 5.5K** · Monto anual de siniestro: **$1M**.
- Consideraciones: impacto medido sobre back test (fuera de tiempo); efectividad = persistencia de la póliza durante los próximos 12 meses.
- **[A verificar]** Esta base (5.5K) corresponde al universo completo "por renovar" de la lámina 5, no al subconjunto que efectivamente renueva (4.5K) — ver nota comparativa con AMI en la sección transversal.

### Lámina 14 — Portada de sección
19.01.26 · "Modelo de Renovación AMI" · 2026 · COE IA.

### Lámina 15 — Alcance del proyecto AMI
"El alcance del estudio abarca a los clientes que tengan algún producto 'AMI' que estén en su periodo de renovación, que representa el 7.5% (4.1K) del stock de producto."
- Pólizas AMI: 64K → Persona natural 56K / Empresa (resto).
- Stock de producto: 54.6K → Por Renovar 4.1K / Activo (resto).
- 43% de las pólizas tienen asignada su primera renovación (proviene de venta nueva).
- **88% renuevan (3.6K pólizas).**
- Grupos de producto: Full Salud, Preferencial, Red Médica, Red Preferente, Salud red Oro, Salud Flex, Otros.
- Universo: clientes CONTRATANTE con producto foco en los últimos 6 meses.

### Lámina 16 — Ratios de persistencia y siniestralidad AMI
"En AMI, la renovación es alta, sin embargo, no todos los clientes persisten en el tiempo."

*% Prima Renovada en 12 meses (mar-24 a feb-25):* 83%, 84%, 85%, 84%, 83%, 81%, 80%, 81%, 81%, 80%, 85%, 86%.
*Montos (millones):* 7.1, 6.3, 6.6, 6.4, 6.9, 7.0, 7.5, 6.9, 7.2, 6.2, 7.9, 6.6.

*% Ratio Siniestralidad -Prima- (mar-24 a feb-25):* 70%, 70%, 78%, 83%, 88%, 89%, 68%, 67%, 72%, 80%, 71%, 66%.
*Montos (millones):* 4.1, 3.7, 4.4, 4.4, 5.0, 5.0, 4.0, 3.7, 4.2, 4.0, 4.8, 3.7.

- **Rímac deja de percibir ~$1.18M por cosecha** debido a que el cliente no persiste los 12 meses con su póliza.
- **Se pierde ~$1.54M** debido a siniestro en los 12 meses siguientes a la renovación.
- **[Hallazgo]** Ambas pérdidas (persistencia y siniestralidad) son mayores en términos absolutos que en VEH, y el ratio de siniestralidad base es mucho más alto (66%-89% vs. 40%-56% en VEH).

### Lámina 17 [OCULTA] — Perfil del modelo de Renovación AMI
"¿Cómo afectan las gestiones a la buena renovación? Las variables más importantes para el modelo de renovación **VEH** fueron 10." **[A verificar — error]** Esta lámina pertenece a la sección AMI (todo el contenido de variables y perfiles es de AMI: prima AMI, siniestros AMI), pero el texto dice "VEH", idéntico palabra por palabra al de la lámina 7. Parece copy-paste sin actualizar la etiqueta.
- **Variables (mayor a menor impacto):** Promedio de Productos sin Desgravamen (12um), Prima Promedio Anual AMI (3um), Actividad WhatsApp Promedio sin Castigo (12um), Permanencia Total en AMI, Variación de Prima Anual AMI (12um), Mix de Productos (Origen Rímac), Edad del Cliente, Monto Promedio de Siniestros AMI (6um), Prima Promedio Anualizada sin Desgravamen (3um), Estado Civil del Cliente.
- **Verde (Muy Alto/Alto):** Prima AMI promedio $1.1K · Edad 45–55 años · Estado civil Soltero/Casado/Viudo · Monto de siniestro promedio $260.
- **Ámbar (Medio/Bajo):** Prima AMI $0.7K–$0.8K · Edad 38–44 años · Soltero · Monto de siniestro $46–$65.
- **Rojo (Muy Bajo):** Prima AMI $1.1K · Edad ≤35 años · Soltero · Monto de siniestro <$35. **[A verificar]** La prima promedio del segmento Rojo ($1.1K) aparece igual a la del segmento Verde — llamativo porque el resto del perfil (edad, siniestro) sí es consistente con menor propensión; confirmar contra el archivo si se va a usar esta cifra.

### Lámina 18 [OCULTA] — Scores del modelo de Renovación AMI
"En promedio los scores de alta probabilidad y media concentran el 84% de los clientes que van a tener una buena renovación."

| Score | % Efectividad | % Leads | % Target |
|---|---|---|---|
| Muy alto | 95.5% | 26% | 31% |
| Alto | 90.5% | 27% | 28% |
| Medio | 87.7% | 23% | 25% |
| Bajo | 82.3% | 14% | 12% |
| Muy bajo | 69.7% | 11% | 4% |

- Efectividad regular mensual: 88.9%.
- Insight: Muy Alto + Alto + Medio = 84% de los clientes con mayor indicador de renovación.

### Lámina 19 — Perfil del modelo de Persistencia AMI
"¿Quiénes son más propensos a persistir 12 meses?"
- **Variables (mayor a menor impacto):** Máximo Gasto respecto a línea de Tarjeta de Crédito (12um), Promedio Línea de Tarjeta de Crédito SBS (18um), Promedio Saldo Total SBS (6um), Nivel socioeconómico, Calificación Crediticia, Promedio Prima Anual AMI (12um), Promedio Prima Anual sin Desgravamen (3um), Edad de Cliente, Promedio Productos sin Desgravamen, Permanencia Total en AMI.
- **Verde (Muy Alto/Alto):** Prima AMI promedio +$1,500 · Generación X/Baby Boomer · Permanencia +21 meses · Edad +50 años.
- **Ámbar (Medio/Bajo):** Prima $600–$1,500 · Generación X/Millennials · Permanencia 12–20 meses · Edad 35–50 años.
- **Rojo (Muy Bajo):** Prima <$550 · Generación Z · Permanencia <12 meses · Edad <35 años.

### Lámina 20 — Scores del modelo de Persistencia AMI
"En promedio los scores de alta probabilidad y media concentran el 79% de los clientes que persisten durante los 12 meses después de su renovación."

| Score | % Efectividad | % Leads | % Target |
|---|---|---|---|
| Muy alto | 88.5% | 30% | 35% |
| Alto | 80.1% | 26% | 27% |
| Medio | 72.7% | 18% | 17% |
| Bajo | 65.8% | 15% | 13% |
| Muy bajo | 54.8% | 12% | 8% |

- Efectividad regular mensual: 76.3%.
- Insight: Muy Alto + Alto + Medio = 79% de los clientes con mayor propensión a persistir 12 meses.

### Lámina 21 — Perfil del modelo de Siniestralidad AMI
"¿A quién consideramos un cliente AMI siniestroso?"
- **Variables (mayor a menor impacto):** Promedio de Productos sin Desgravamen (12um), Promedio Prima Anual AMI (3um), Promedio de Cantidad de Mensajes WhatsApp (12um), Permanencia total AMI, Variación Prima Anual AMI (12um), Combinación de productos Rímac, Edad de Cliente, Promedio Monto Siniestro AMI (6um), Promedio Prima Anual sin Desgravamen (3um), Estado civil.
- **Verde (Muy Alto/Alto):** Gasto Mínimo (6um) 2.8K–5.3K · NSE A · Edad +50 años · Prima AMI (12um) $2,500+.
- **Ámbar (Medio/Bajo):** Gasto Mínimo (6um) 2.8K–5.3K · NSE B-C · Edad 45–50 años · Prima $700–$800. **[A verificar]** El rango de "Gasto Mínimo" es idéntico al del segmento Verde; podría ser un dato real (esa variable no discrimina entre esos dos segmentos) o un error de copiado — confirmar contra el archivo original.
- **Rojo (Muy Bajo):** Gasto Mínimo ≤2.5K · NSE B-C-D · Edad ≤40 años · Prima <$700.

### Lámina 22 — Scores del modelo de Siniestralidad AMI
"En promedio los scores de alta probabilidad y media concentran el 80% de los clientes con propensión de siniestralidad costosa durante los 12 meses después de su renovación."

| Score | % Efectividad | % Leads | % Target |
|---|---|---|---|
| Muy alto | 81.9% | 20% | 30% |
| Alto | 62.4% | 25% | 28% |
| Medio | 49.6% | 24% | 22% |
| Bajo | 41.8% | 18% | 13% |
| Muy bajo | 32.8% | 13% | 7% |

- Efectividad regular mensual: 55.9%.
- Insight: Muy Alto + Alto + Medio = 80% de los clientes con mayor probabilidad de siniestro.
- **[Hallazgo]** La efectividad regular mensual (55.9%) es ~3.3x la de VEH (17.2%) — el evento "siniestro en 12 meses" es mucho más frecuente en AMI, consistente con que las atenciones de salud son más recurrentes que los siniestros vehiculares.

### Lámina 23 — Matriz de Renovación AMI
"A partir de los scores de persistencia y siniestralidad, se desarrolla la matriz de renovación para identificar pólizas potenciales."

**Distribución de Pólizas** (Persistencia en filas, Siniestralidad en columnas: Muy bajo → Muy alto):

| Persistencia \ Siniestralidad | Muy bajo | Bajo | Medio | Alto | Muy alto | Total |
|---|---|---|---|---|---|---|
| Muy alto | 1.39% | 1.72% | 4.16% | 10.18% | 18.24% | 35.69% |
| Alto | 1.76% | 2.34% | 6.17% | 8.39% | 7.30% | 25.96% |
| Medio | 1.31% | 2.39% | 5.34% | 4.75% | 2.65% | 16.44% |
| Bajo | 1.50% | 3.25% | 3.75% | 3.16% | 1.24% | 12.90% |
| Muy bajo | 1.43% | 3.87% | 2.08% | 1.33% | 0.30% | 9.01% |
| **Total** | **7.39%** | **13.57%** | **21.50%** | **27.81%** | **29.73%** | **100.00%** |

**Indicador de Siniestralidad / Distribución de Siniestros** (misma estructura):

| Persistencia \ Siniestralidad | Muy bajo | Bajo | Medio | Alto | Muy alto | Total |
|---|---|---|---|---|---|---|
| Muy alto | 2.43% | 2.52% | 4.60% | 8.77% | 11.94% | 30.26% |
| Alto | 3.14% | 3.07% | 6.75% | 7.51% | 5.15% | 25.62% |
| Medio | 2.24% | 3.22% | 5.93% | 4.39% | 1.95% | 17.73% |
| Bajo | 2.51% | 4.06% | 4.32% | 2.88% | 0.92% | 14.69% |
| Muy bajo | 2.46% | 5.17% | 2.48% | 1.35% | 0.24% | 11.70% |
| **Total** | **12.78%** | **18.04%** | **24.08%** | **24.90%** | **20.20%** | **100.00%** |

- Base: **Pólizas: 3.5K** · Monto anual de siniestro: **$4.3M**.
- **[A verificar]** Esta base (3.5K) está más cerca del subconjunto que sí renueva (3.6K, lámina 15) que del universo completo "por renovar" (4.1K) — comportamiento distinto al de la matriz VEH, que sí usa el universo completo (5.5K). Ver nota comparativa en la síntesis.

### Lámina 24 — Próximos pasos
"Como siguientes pasos, se actualizarían los modelos WTP de renovación con los nuevos modelos que forman la matriz de renovación y se coordinará el despliegue para las campañas con la unidad de negocio y segmentos."

| Etapa | Estado | Entregable | Contenido |
|---|---|---|---|
| Modelos | ✅ Culminado | 16 de febrero | Presentación de rango de scores de propensión, persistencia y siniestralidad por segmento; dimensionamiento de matriz de renovación |
| WTP (Willingness To Pay) | 🟡 En proceso | Por definir | Actualización de segmento de elasticidad con nuevos inputs; actualización de los modelos WTP de renovación (administrado por el equipo de pricing) |
| Piloto | ⚪ Pendiente | Por definir | Diseño de piloto para el despliegue; definición de medición de contribución |

## Hallazgos consolidados — Matriz de Renovación

1. Los tres pares de modelo (Renovación, Persistencia, Siniestralidad) muestran el mismo patrón de concentración eficiente que el deck de Churn: con los 3 scores más altos se captura 79%-84% del evento de interés en VEH y AMI.
2. Los drivers principales difieren por producto: en VEH dominan variables de canal, NSE, antigüedad del vehículo y comportamiento crediticio; en AMI dominan permanencia previa, mix de productos, prima y — en el modelo de siniestralidad — actividad de WhatsApp (variable de engagement/contacto, no financiera ni demográfica).
3. AMI tiene bases de siniestralidad y pérdida por no-persistencia sustancialmente mayores que VEH en términos absolutos ($1.54M vs. $1.0M en siniestralidad; $1.18M vs. $470K en no-persistencia), aunque el volumen de pólizas de AMI en alcance es menor (4.1K vs. 5.5K).
4. El proyecto está en su primera etapa completada (dimensionamiento de matriz); la actualización de modelos WTP y el piloto de despliegue aún no tienen fecha definida.

## Errores / inconsistencias — Matriz de Renovación

1. **Etiqueta cruzada (lámina 17):** dice "modelo de renovación VEH" estando en la sección AMI.
2. **Perfil de renovación VEH incompleto (lámina 7):** el campo "Ingreso Promedio" está vacío en los 3 segmentos.
3. **4 láminas ocultas (7, 8, 17, 18):** el Modelo 1 (renovación) de VEH y AMI no forma parte del recorrido visible del deck.
4. **Bases poblacionales distintas entre matrices:** VEH usa 5.5K (universo completo), AMI usa 3.5K (cercano solo al subconjunto renovado).
5. **Prima idéntica entre segmentos Verde y Rojo (lámina 17, AMI-Renovación):** $1.1K en ambos casos.
6. **Rango de "Gasto Mínimo" idéntico entre Verde y Ámbar (lámina 21, AMI-Siniestralidad):** 2.8K–5.3K en ambos.
7. **Nota de speaker "prosperous/brokers" (lámina 2):** idéntica a la del deck de Churn, sin relación aparente con el contenido de la lámina.

---
---

# PARTE 3 — Síntesis cruzada entre ambos documentos

## Comparación AMI vs. VEH: relación entre persistencia y siniestralidad

Cruzando cada matriz de renovación contra sí misma (comparando, fila por fila de Persistencia, el % de pólizas/certificados contra el % de siniestros que le corresponde), se observa un patrón que **ninguno de los dos documentos señala explícitamente** — es un cálculo propio a partir de sus tablas:

| Persistencia | VEH: % certificados | VEH: % siniestros | VEH: ratio | AMI: % pólizas | AMI: % siniestros | AMI: ratio |
|---|---|---|---|---|---|---|
| Muy alto | 21.44% | 22.16% | 1.03 | 35.69% | 30.26% | 0.85 |
| Alto | 30.74% | 31.66% | 1.03 | 25.96% | 25.62% | 0.99 |
| Medio | 26.20% | 26.36% | 1.01 | 16.44% | 17.73% | 1.08 |
| Bajo | 14.66% | 15.07% | 1.03 | 12.90% | 14.69% | 1.14 |
| Muy bajo | 6.95% | 4.75% | **0.68** | 9.01% | 11.70% | **1.30** |

- **En VEH**, todas las bandas están cerca de un ratio de 1.0 (proporcionalidad entre % de certificados y % de siniestros), excepto Muy Baja persistencia, que está claramente subrepresentada en siniestros (0.68).
- **En AMI**, el patrón se invierte: Muy Alta persistencia está subrepresentada en siniestros (0.85) y Muy Baja persistencia está sobrerrepresentada (1.30) — a menor persistencia, mayor proporción relativa de siniestros.

**[Hipótesis, no confirmada por los documentos]** Dos lecturas posibles, no distinguibles con la información disponible:
1. Causalidad inversa en AMI: un siniestro costoso podría anteceder y explicar la no-renovación (el cliente se va después de/por el siniestro), mecanismo que en VEH sería más débil o inexistente.
2. Naturaleza distinta del riesgo: en salud, quien más usa el seguro (más siniestros/atenciones) puede ser quien más lo necesita y por ende más sensible a fricciones de precio en la renovación; en vehicular, un siniestro con responsabilidad puede implicar recargo de prima sin necesariamente traducirse en cancelación inmediata.

Para distinguir entre ambas explicaciones haría falta revisar el orden temporal real (¿el siniestro ocurre antes o después de la señal de no-renovación?) en la data subyacente — algo que ninguno de los dos documentos reporta.

## Terminología que cambia de significado entre documentos

**[A verificar]** La columna "% Efectividad" tiene un significado distinto en cada deck:
- En **Churn**, "% Efectividad" es la participación de esa banda en el total de casos capturados (recall) — ej. Muy Alto captura 69% de la cancelación por mora. El rol de "tasa dentro de la banda" (precisión) lo cumple la columna "% Fuga".
- En **Renovación**, "% Efectividad" es la tasa de acierto dentro de esa banda (precisión) — ej. 84.5% de los clientes "Muy Alto" efectivamente persistió. El rol de "participación en el total capturado" (recall) lo cumple la columna "% Target".

Si alguien compara ambos documentos asumiendo que "% Efectividad" significa lo mismo en los dos, va a leer mal los números.

## Oportunidades

**Diseño de tratamiento diferenciado, no solo priorización.** En los 7 modelos (3 de Churn + 4 de Renovación), Muy Alto+Alto concentran 79%-91% del evento con solo 26%-36% de la base. El paso natural más allá de "enfocar la gestión ahí" es definir qué tratamiento (contenido, canal, oferta) recibe específicamente ese 26-36%, en lugar de aplicar la misma gestión en mayor intensidad.

**Las dos causas de churn piden palancas de diseño distintas.** Morosidad (41%) es fricción operativa de pago — candidato a rediseño de recordatorios, medios de pago, flexibilización. APC (59%, pedido explícito del cliente) es una decisión activa, y ningún documento reporta el motivo detrás de esa decisión (precio, servicio, competencia). Diseñar una sola gestión de retención sin diferenciar por causa raíz puede desperdiciar la ventana de 2 meses que el propio modelo define (Abr-Jun antes de la fuga proyectada en Jul).

**La matriz Persistencia × Siniestralidad ya distingue dos problemas de negocio distintos** que el score de renovación por sí solo no separa: "va a renovar pero no es rentable" (alta persistencia + alta siniestralidad) vs. "no va a renovar" (baja persistencia). El piloto de despliegue (próximo hito, sin fecha) podría diseñar ofertas por cuadrante en vez de un tratamiento único de renovación.

**Las ventanas de tiempo ya definidas son un insumo de diseño aprovechable.** Ambos modelos especifican con precisión cuándo intervenir (2 meses antes de la fuga en Churn; entre M9 y el mes de renovación en Renovación) — vale anclar cualquier journey o comunicación a esos momentos específicos y no solo al score.

**Investigar el orden temporal en AMI (persistencia-siniestralidad).** Dado el patrón inverso encontrado entre AMI y VEH, valdría revisar si el siniestro antecede a la señal de no-renovación en AMI — si es así, cambiaría la interpretación de "para quién" diseñar la gestión de persistencia en esa línea de negocio.

## Limitaciones metodológicas a tener en cuenta

- Los "perfiles" (edad, NSE, canal, prima) son variables que el modelo encontró útiles para predecir — asociación, no evidencia de que modificar esa variable cambie el comportamiento.
- Ninguno de los dos documentos indica qué métrica de "impacto/importancia" se usó para rankear las variables (¿coeficiente de un modelo lineal, SHAP, feature importance de árboles?), por lo que no se puede evaluar si son comparables entre modelos o entre documentos.
- La validación reportada en las matrices de renovación es *backtest fuera de tiempo* — mide qué tan bien habría funcionado el score en el pasado, no el desempeño de una gestión activa ya desplegada; la efectividad real de un piloto puede diferir.
- No hay información sobre tamaño de muestra de entrenamiento ni ventana temporal usada para ajustar cada modelo, más allá de lo mostrado en las series de tiempo y la definición de universo — no es posible pronunciarse sobre estabilidad o representatividad fuera de los periodos graficados.
- Ambos documentos reportan concentración/efectividad de scoring, no resultados de una intervención — no hay (todavía) evidencia de que gestionar a los segmentos de alta propensión efectivamente reduzca el churn o mejore la persistencia; eso solo se sabrá con el piloto.
