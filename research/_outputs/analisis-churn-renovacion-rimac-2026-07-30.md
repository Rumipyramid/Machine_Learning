# Modelo de Churn y Matriz de Renovación RIMAC — Análisis, validación con literatura, alertas y recomendaciones por ramo

> Informe basado en el documento interno `Análisis detallado — Modelo de Churn y Matriz de
> Renovación (CoE AI / GenAI)` (análisis de 2 decks: Modelo de Churn - Visión Cliente, abril
> 2026; Matriz de Renovación AMI y VEH, ene-feb 2026), cruzado con validación externa
> (`/trinidad`) e incorporado al Lobo (`research/lobo/opinion_experto.md`, tesis 21).
> Persistido en `research/_fuentes_internas/Analisis_Detallado_Churn_Renovacion.md` y
> `research/_nodes/modelo-churn-renovacion-rimac.md` (v1.0) del proyecto
> `Rumipyramid/Machine_Learning`. Fuentes de validación externa: F-388 a F-392 en
> `research/fuentes/codice.md`.
> Fecha: 2026-07-30.

---

## Resumen ejecutivo

RIMAC tiene, hoy, tres modelos de churn (Morosidad, APC, Cliente combinado) y cuatro
modelos de renovación (Persistencia y Siniestralidad, en VEH y AMI) que **concentran el
evento de interés con una eficiencia por encima del benchmark académico publicado**: capturan
79-91% del evento con solo 26-36% de la base, mientras la literatura reporta ~90% de captura
necesitando ~50% de la base en el mejor de los casos documentados. La capacidad técnica de
detección no es el cuello de botella. Los dos vacíos de mayor valor de negocio están en otro
lugar: (1) nadie mide la **causa raíz** de la cancelación voluntaria (59% del churn de
certificado, más grande que la morosidad), y (2) el patrón inverso entre persistencia y
siniestralidad en AMI vs. VEH tiene una explicación teórica plausible en la literatura de
selección adversa, pero no está confirmado con el dato disponible — es predictivo, no
retrospectivo.

---

## 1. Ramo transversal — Churn Cliente/Certificado (Morosidad + APC)

### Diagnóstico interno
Universo de 1.8M clientes / 2.9M certificados. Churn mensual a nivel cliente: 2.89%
(~50K clientes, $11.5M en primas); a nivel certificado: 2.45% (~70K certificados). La causa
se reparte en **Morosidad 41%** y **Pedido del Cliente / APC 59%** — la cancelación
voluntaria es mayoría. Los 3 scores (Morosidad, APC, Cliente combinado) concentran 80-91%
del evento con 26-36% de la base; el de Morosidad es el más eficiente (91% con 26%, lift
x11.6 en la banda "Muy Alto"). Los perfiles de cada causa tienen drivers distintos:
Morosidad se explica por comportamiento de pago/mora y antigüedad; APC se explica más por
canal de adquisición y producto, sin variables de comportamiento de pago reportadas. El
patrón demográfico del churn cliente es monotónico: a mayor propensión, cliente más joven,
menor ingreso, más nuevo en Rímac, menor prima, menor ratio de pago.

### Validación con literatura
- **Calidad del modelo:** un benchmark académico reciente de modelos de churn (revista
  arbitrada, F-388, 🟢A) reporta lift de ~1.9-3.01x en el decil superior como
  estándar/mejor-caso publicado, con 50% de la base necesaria para ~90% de captura. Los
  modelos de RIMAC necesitan **26-36%** de la base para el mismo resultado, y el lift x11.6
  del score "Muy Alto" de Morosidad triplica el mejor caso publicado (x3.01). La brecha es
  demasiado grande para ser ruido de comparación entre datasets distintos.
- **¿Es normal que la cancelación voluntaria supere a la morosidad?** Sí — es consistente
  con una tendencia de industria documentada externamente (F-389, 🟡C): ~29% de asegurados
  en EE.UU. cambió de aseguradora en 2025 por presión de precio acumulada, y 60% cambiaría
  por mejor personalización/servicio, no por precio más bajo. El 59% de APC de RIMAC no es
  una anomalía local, es la manifestación de una fuerza de industria más amplia.
- **Ventana de gestión anticipada (Abr-Jun antes de fuga proyectada en Jul):** consistente
  en dirección con evidencia (F-392, 🟡C, tratar con cautela) de que ~68% de quienes
  cancelan una póliza/suscripción ya tomaron la decisión 30-90 días antes del evento.

### 🚨 Alertas
- **Vacío de dato más caro del análisis: ningún documento reporta la causa raíz del 59% de
  APC** (¿precio, servicio, competencia?). Sin esa variable, cualquier gestión de retención
  sobre ese 59% dispara "a ciegas" sobre la mayoría del churn.
- El deck no reporta "canal" ni "producto" como variable explícita del modelo Cliente
  combinado (láminas 15-16) — solo variables socio-demográficas/financieras.
- Nota de speaker "prosperous/brokers" (láminas 2 y 5) no tiene relación aparente con el
  contenido de esas láminas — posible remanente de otro documento, no invalida el modelo
  pero conviene limpiarlo antes de compartir el deck externamente.
- El % de churn mensual sube de 2.42% (ago-25) a 3.50% (dic-25) sin que el documento lo
  señale ni lo explique — vale monitorear si es estacionalidad o tendencia real.

### ✅ Recomendaciones
1. **Instrumentar causa raíz de la cancelación voluntaria** (encuesta de salida corta, o
   modelo de clasificación de motivo) antes de diseñar cualquier oferta de retención masiva
   sobre el segmento APC — es el mayor ROI marginal identificado en todo el análisis.
2. **Diseñar tratamiento diferenciado por causa, no un solo flujo de retención.** Morosidad
   (fricción operativa) pide recordatorios/medios de pago/flexibilización; APC (decisión
   activa) pide entender y responder al motivo real antes de ofrecer un descuento genérico.
3. **Anclar cualquier journey de retención a la ventana Abr-Jun ya validada por el modelo**
   (y externamente consistente con el patrón de decisión 30-90 días) en vez de una campaña
   de intensidad pareja todo el año.

---

## 2. Ramo VEH (Vehicular)

### Diagnóstico interno
Universo "por renovar": 5.5K pólizas (6.4% del stock de 85K). 82% renueva (4.5K). Pese a
renovación alta, persistencia y siniestralidad a 12 meses generan pérdida: ~$470K/cosecha
por no-persistencia, ~$1.0M por siniestralidad. Modelo de Persistencia: 81% de captura con
las 3 bandas superiores (drivers: canal, NSE, prima, antigüedad del vehículo). Modelo de
Siniestralidad: 82% de captura (drivers: frecuencia de siniestros previos, prima, antigüedad
del vehículo, ingreso). En la matriz Persistencia × Siniestralidad, **todas las bandas están
cerca de proporcionalidad 1:1** entre % de certificados y % de siniestros, excepto Muy Baja
persistencia, que está *subrepresentada* en siniestros (ratio 0.68).

### Validación con literatura
El patrón de proporcionalidad ~1.0 en casi toda la matriz VEH es consistente con lo
esperable en un riesgo físico/vehicular: la propensión a persistir y la propensión a
siniestrarse responden a mecanismos mayormente independientes (comportamiento de pago y
canal, por un lado; exposición y hábito de manejo, por otro), sin el mecanismo de selección
por anticipación de uso que sí opera en salud (ver Ramo AMI). No se encontró literatura que
prediga específicamente el patrón de subrepresentación en Muy Baja persistencia — se
reporta como observación propia del documento interno, no como hallazgo con respaldo externo
directo.

### 🚨 Alertas
- **Lámina 7 (perfil del modelo de Renovación VEH) está incompleta**: el campo "Ingreso
  Promedio" aparece vacío en los tres segmentos (Verde/Ámbar/Rojo) — posible causa de por
  qué la lámina quedó oculta en el deck en vez de corregida.
- **Lámina 8 tiene un título con placeholder sin completar** ("concentran el x% de las
  clientes...") — señal de que el Modelo 1 de Renovación (VEH) no llegó a un estado
  final documentado, aunque si se usa en producción según el diagrama de flujo.
- La base de la matriz (5.5K) es el universo completo "por renovar", no el subconjunto que
  efectivamente renueva (4.5K) — comparar esta cifra con AMI (que sí usa el subconjunto
  renovado) sin ajustar puede llevar a conclusiones erróneas sobre el tamaño relativo del
  problema entre ramos.

### ✅ Recomendaciones
1. Completar el perfil cuantitativo de la lámina 7 (Ingreso Promedio) antes de usar ese
   modelo para segmentar campañas — hoy no es accionable sin esa cifra.
2. Dado que persistencia y siniestralidad son casi independientes en VEH (salvo el extremo
   de Muy Baja persistencia), **los dos problemas pueden tratarse con palancas separadas**:
   retención centrada en canal/NSE/antigüedad del vehículo; control de siniestralidad
   centrado en historial de siniestros y prima. No hace falta una oferta combinada única
   por cuadrante como sí se justifica en AMI (ver abajo).
3. Investigar puntualmente el segmento Muy Baja persistencia (subrepresentado en siniestros,
   0.68) — podría ser el segmento de menor lealtad pero también de menor riesgo real, un
   perfil distinto al que la intuición de "cliente que se va = cliente problemático" sugiere.

---

## 3. Ramo AMI (Salud individual)

### Diagnóstico interno
Universo "por renovar": 4.1K pólizas (7.5% del stock de 54.6K). 88% renueva (3.6K). Las
pérdidas son mayores que VEH en términos absolutos pese a menor volumen: ~$1.18M/cosecha por
no-persistencia (vs. $470K en VEH), ~$1.54M por siniestralidad (vs. $1.0M en VEH); el ratio
de siniestralidad base es mucho más alto (66-89% vs. 40-56% en VEH). Modelo de Persistencia:
79% de captura (drivers: uso de tarjeta de crédito, NSE, calificación crediticia, prima,
permanencia previa). Modelo de Siniestralidad: 80% de captura, con **actividad de WhatsApp**
como driver relevante — variable de engagement/contacto, no financiera ni demográfica, única
en todo el análisis. La efectividad regular mensual de este modelo (55.9%) es ~3.3x la de
VEH (17.2%), consistente con que las atenciones de salud son más recurrentes que los
siniestros vehiculares. **Hallazgo central de este ramo:** en la matriz cruzada, Muy Baja
persistencia está *sobrerrepresentada* en siniestros (ratio 1.30) — patrón inverso al de VEH.

### Validación con literatura
Este es el hallazgo con la validación externa más directa y, a la vez, la más matizada del
análisis. La literatura de selección adversa dinámica en seguros de salud (Geneva Risk and
Insurance Review, 2026, F-390, 🟢A) documenta que las decisiones de lapso/reinstalación
están sujetas a selección adversa: la experiencia de siniestros de quienes lapsan es
sistemáticamente distinta de quienes permanecen. El mismo mecanismo general aparece en
seguros de cuidado a largo plazo (F-391, 🔵B): las personas de menor riesgo son las que más
lapsan, dejando un pool remanente más enfermo. **Esto da un marco teórico sólido para *por
qué* AMI se comporta distinto de VEH** (el seguro de salud es un producto de uso recurrente,
donde la decisión de renovar está más ligada a la necesidad/costo percibido de seguir
usándolo que en un seguro de riesgo físico como VEH) — pero **no confirma la dirección
exacta** encontrada en RIMAC: el dato de RIMAC es *predictivo* (dos scores separados sobre
clientes que aún no decidieron), no una medición retrospectiva de quién efectivamente hizo
lapso. Se reporta como la hipótesis mejor sustentada, no como hallazgo cerrado.

### 🚨 Alertas
- **Lámina 17 tiene una etiqueta cruzada real:** dice "modelo de renovación VEH" con todo el
  contenido siendo de AMI (prima AMI, siniestros AMI) — copy-paste sin actualizar, mismo
  texto palabra por palabra que la lámina 7 de VEH.
- **Prima idéntica ($1.1K) entre los segmentos Verde y Rojo** del perfil de Renovación AMI
  (lámina 17) — llamativo porque el resto del perfil (edad, siniestro) sí es consistente con
  menor propensión en Rojo; confirmar contra el archivo original antes de usar esa cifra.
- **Rango de "Gasto Mínimo" idéntico (2.8K-5.3K) entre Verde y Ámbar** del perfil de
  Siniestralidad AMI (lámina 21) — podría ser un dato real (la variable no discrimina entre
  esos dos segmentos) o un error de copiado.
- La base de la matriz de renovación AMI (3.5K) está más cerca del subconjunto que sí
  renueva (3.6K) que del universo completo "por renovar" (4.1K) — comportamiento distinto al
  de VEH (que sí usa el universo completo). No comparar ambas matrices en tamaño absoluto sin
  ajustar por esta diferencia de base.

### ✅ Recomendaciones
1. **Investigar el orden temporal real** (¿el siniestro ocurre antes o después de la señal
   de no-renovación en la data subyacente?) — es la única forma de confirmar si el mecanismo
   es selección adversa (el cliente que más usa el seguro es más sensible a la fricción de
   renovarlo) o causalidad inversa (un siniestro costoso empuja directamente a no renovar).
   La respuesta cambia qué "para quién" diseñar la gestión de persistencia en este ramo.
2. **Diseñar oferta específica para el cuadrante "alta siniestralidad + baja persistencia"**
   — es el segmento de mayor pérdida potencial doble (se va y cuesta caro mientras se queda),
   y la matriz ya lo aísla sin que exista todavía una jugada propuesta para él.
3. **Investigar "actividad de WhatsApp" como palanca, no solo como predictor.** Es la única
   variable de engagement (no financiera/demográfica) que aparece entre los 10 drivers
   principales de siniestralidad AMI — vale entender si el canal de contacto en sí mismo es
   accionable (más o mejor contacto reduce fricción) antes de tratarlo solo como señal
   pasiva de scoring.
4. Corregir la etiqueta cruzada de la lámina 17 y verificar las dos cifras duplicadas
   (Verde/Rojo en prima; Verde/Ámbar en gasto mínimo) contra el archivo original antes de
   usar el deck para una decisión de negocio o presentarlo fuera del equipo que lo construyó.

---

## 4. Alertas transversales de gobernanza de datos

- **"% Efectividad" significa cosas opuestas en cada deck.** En Churn es *recall*
  (participación de la banda en el total capturado); en Renovación es *precisión* (tasa de
  acierto dentro de la banda). Compararlos como si fueran el mismo indicador lleva a leer
  mal los números.
- **4 láminas del deck de Renovación están ocultas** (7, 8, 17, 18) — el Modelo 1
  (probabilidad de buena renovación) de VEH y AMI no forma parte del recorrido visible,
  aunque sí se usa como input de los otros dos modelos según el diagrama de flujo.
- **Ambos documentos validan con backtest fuera de tiempo, no con una intervención real.**
  Es la limitación más importante del conjunto: mide qué tan bien habría funcionado el score
  en el pasado, no el efecto de gestionar activamente a un segmento. El "Piloto" (próximo
  hito del roadmap, sin fecha) es lo único que puede confirmar si la concentración eficiente
  del modelo se traduce en menos churn real.

---

## 5. Tabla resumen — recomendaciones priorizadas

| # | Ramo | Recomendación | Por qué es prioritaria |
|---|---|---|---|
| 1 | Transversal | Instrumentar causa raíz del 59% de cancelación voluntaria (APC) | Mayor volumen de churn, cero visibilidad de motivo hoy |
| 2 | AMI | Investigar orden temporal siniestro↔no-renovación | Determina si el mecanismo es selección adversa o causalidad inversa — cambia el diseño de la intervención |
| 3 | AMI | Diseñar oferta para cuadrante alta-siniestralidad/baja-persistencia | Mayor pérdida potencial doble ya identificado y sin jugada propuesta |
| 4 | Transversal | Tratamiento diferenciado por causa (Morosidad vs. APC), no un flujo único | Evita desperdiciar la ventana de gestión ya bien diseñada |
| 5 | VEH | Completar perfil cuantitativo de la lámina 7 (Ingreso Promedio) | Modelo no accionable para segmentación sin esa cifra |
| 6 | Transversal | Unificar/documentar significado de "% Efectividad" entre decks | Riesgo de decisión de negocio basada en una lectura cruzada incorrecta |
| 7 | AMI | Corregir etiqueta cruzada y verificar cifras duplicadas (lám. 17, 21) | Riesgo de credibilidad si el deck circula fuera del equipo sin corregir |

---

## Limitaciones

- La comparación de lift/concentración usa un benchmark académico de dataset(s) distinto(s)
  al de RIMAC — dirección robusta, no comparación controlada exacta.
- La validación teórica del patrón AMI/VEH (selección adversa dinámica) es el marco más
  cercano encontrado, no una confirmación causal — el dato de RIMAC es predictivo, la
  literatura citada es mayormente retrospectiva.
- No se investigó específicamente el mercado peruano de switching/cancelación de seguros —
  la validación de industria sobre cancelación voluntaria es mayormente de EE.UU.
- Ninguna recomendación de este informe reemplaza la verificación de las cifras exactas
  contra los archivos PowerPoint originales antes de usarlas en un documento externo o una
  decisión de negocio formal.

---

*Fuente completa y versionada: `research/_nodes/modelo-churn-renovacion-rimac.md` (v1.0) y
`research/lobo/opinion_experto.md` (tesis 21). Documento primario:
`research/_fuentes_internas/Analisis_Detallado_Churn_Renovacion.md`. Fuentes de validación
externa F-388 a F-392 en `research/fuentes/codice.md`.*
