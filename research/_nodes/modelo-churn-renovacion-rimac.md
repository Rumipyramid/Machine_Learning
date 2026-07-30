# Modelo de Churn y Matriz de Renovación de RIMAC (AMI/VEH): hallazgos internos + validación externa

> Documento de investigación. Fuente persistente y versionada en el repositorio.
> Fecha de elaboración: 2026-07-30 · Versión: v1.0
> Origen: análisis de documento interno (usuario) + `/trinidad` — investigación de 360°
> Fuente primaria: `research/_fuentes_internas/Analisis_Detallado_Churn_Renovacion.md`
> (análisis detallado de 2 decks internos de RIMAC: Modelo de Churn - Visión Cliente,
> abril 2026; Matriz de Renovación AMI y VEH, ene-feb 2026)
> Fuentes de validación externa registradas en `research/fuentes/codice.md` (F-388 a F-392).

---

## 0. Resumen ejecutivo (TL;DR)

RIMAC tiene, hoy, capacidad interna de modelado de propensión a fuga (churn) y de
renovación (persistencia + siniestralidad) que **supera con holgura los benchmarks
publicados de la industria** en eficiencia de concentración: captura 79-91% del evento con
solo 26-36% de la base, contra un estándar académico publicado de ~90% de captura
necesitando ~50% de la base. La pregunta relevante ya no es si el modelo funciona — es si
el tratamiento que reciben esos segmentos ya identificados está diseñado con la misma
sofisticación que el score que los identifica. El hallazgo más importante no es técnico:
es que la cancelación **voluntaria** (pedido del cliente, 59% del total) supera a la
**involuntaria** (morosidad, 41%), es consistente con una tendencia de industria más
amplia (documentada externamente), y ningún documento interno reporta la causa raíz de esa
decisión — precio, servicio o competencia. Ese es el vacío de mayor valor de negocio.

---

## 1. Hallazgos internos (fuente: documento persistido en `_fuentes_internas/`)

**Modelo de Churn (visión cliente):** 3 modelos sobre 1.8M clientes / 2.9M certificados.
Churn mensual a nivel cliente: 2.89% (~50K clientes, $11.5M en primas); a nivel
certificado: 2.45% (~70K certificados), con Morosidad 41% y Pedido del Cliente (APC) 59%
como causas. Los 3 scores concentran 80-91% del evento con 26-36% de la base.

**Matriz de Renovación (AMI y VEH):** 4 modelos por línea (Renovación, Persistencia,
Siniestralidad). VEH: 82% de pólizas renuevan (universo 5.5K); pérdida de ~$470K/cosecha
por no-persistencia y ~$1.0M por siniestralidad. AMI: 88% renuevan (universo 4.1K); pérdida
mayor en términos absolutos (~$1.18M por no-persistencia, ~$1.54M por siniestralidad) pese
a un universo menor, con ratio de siniestralidad base mucho más alto (66-89% vs. 40-56% en
VEH).

**Patrón cruzado no señalado por ningún documento fuente** (cálculo propio del análisis):
cruzando persistencia contra siniestralidad relativa, VEH muestra proporcionalidad
consistente (ratio ~1.0 en casi todas las bandas, con Muy Baja persistencia
*subrepresentada* en siniestros, 0.68); AMI muestra el patrón **inverso** — Muy Baja
persistencia está *sobrerrepresentada* en siniestros (ratio 1.30), Muy Alta persistencia
subrepresentada (0.85).

**Calidad de dato — señales de gobierno de datos a atender:** terminología de "% Efectividad"
significa cosas distintas en cada deck (recall en Churn, precisión en Renovación); 4 láminas
ocultas del deck de Renovación (el score de Renovación en sí no está en el recorrido visible);
al menos 3 inconsistencias puntuales detectadas (etiqueta cruzada VEH/AMI, campo vacío,
valores idénticos entre segmentos Verde/Rojo donde no deberían serlo).

## 2. 🔬 Validación externa — pista empírica/teórica

**¿Es buena la concentración del modelo?** Un benchmark académico reciente de modelos de
churn (MDPI, revista arbitrada) reporta lift de ~1.9-3.01x en el decil superior como
desempeño esperado/mejor-caso publicado, con las 5 bandas superiores (50% de la base)
capturando ~90% de los churners (F-388, 🟢A). **Los modelos de RIMAC necesitan solo 26-36%
de la base para el mismo 79-91% de captura**, y el score "Muy Alto" de Morosidad tiene lift
x11.6 — muy por encima del x3.01 reportado como mejor caso en la literatura. Esto no es una
comparación 1:1 perfecta (datasets distintos), pero la brecha es demasiado grande para ser
ruido: la capacidad predictiva interna de RIMAC es, direccionalmente, sustancialmente mejor
que el estándar publicado.

**¿Por qué se invierte el patrón persistencia-siniestralidad entre AMI y VEH?** La
literatura de selección adversa dinámica en seguros de salud (Geneva Risk and Insurance
Review, F-390, 🟢A) documenta que las decisiones de lapso/reinstalación están sujetas a
selección adversa: quienes dan de baja su póliza tenían, antes de eso, una experiencia de
siniestros **distinta** de quienes permanecen. El mismo mecanismo general aparece en seguros
de cuidado a largo plazo (F-391, 🔵B): las personas de menor riesgo son las que más lapsan,
dejando un pool remanente más enfermo. **Divergencia señalada explícitamente, no forzada:**
el dato de RIMAC es *predictivo* (dos scores separados sobre clientes que aún no decidieron,
no una medición retrospectiva de quién efectivamente lapsó), por lo que la dirección exacta
del mecanismo no se puede confirmar 1:1 contra esta literatura — pero es el marco teórico más
cercano disponible, y sugiere que el patrón inverso de AMI no es ruido, es la firma esperable
de selección adversa dinámica operando en una línea de salud, algo que estructuralmente no
aplica igual en un producto de riesgo físico como VEH.

**¿La ventana de gestión anticipada tiene respaldo?** Una fuente agregadora que cita un
hallazgo de revista académica (tratar con cautela, F-392, 🟡C) reporta que 68% de quienes
cancelan una suscripción/póliza ya tomaron la decisión 30-90 días antes del evento —
consistente en dirección con el diseño de ambos modelos de RIMAC (Churn: ventana de gestión
Abr-Jun antes de fuga proyectada en Jul; Renovación: M9 hasta el mes de renovación, ~4 meses).

## 3. 📈 Validación externa — pista de negocio

La cancelación voluntaria (APC, 59% en el dato de RIMAC) superando a la involuntaria
(morosidad, 41%) **no es una anomalía** — es consistente con una tendencia de industria más
amplia y reciente: ~29% de asegurados en EE.UU. cambiaron de aseguradora en 2025 (presión de
precio acumulada), y 60% cambiaría por mejor personalización/experiencia, no por precio más
bajo — incluso 30% de clientes "satisfechos" declara intención de cambiar en los próximos 3
meses (F-389, 🟡C, prensa especializada citando encuestas de industria). **Implicación
directa:** si esta tendencia también aplica en Perú, el 59% de APC de RIMAC probablemente no
es un problema homogéneo — mezcla precio, servicio y competencia en proporciones que ningún
documento interno reporta todavía.

## 4. 📱 Pista social/mediática

Esta pista se omite explícitamente para este tema: no hay una dimensión de percepción
pública/social directamente aplicable a un modelo analítico interno de RIMAC (no es un
producto, marca o controversia con circulación social propia) — forzarla sería inventar
evidencia irrelevante. La pista social sí aplica, y ya está cubierta, en los nodes que tratan
la experiencia de cliente y confianza de RIMAC en general (ver Conexiones).

## 5. ⚖️ Síntesis

**Convergencia:** las tres validaciones externas apuntan en la misma dirección — el enfoque
técnico de RIMAC (scoring de alta concentración, ventanas de gestión anticipada) está
alineado o por encima del estándar de industria; el patrón de causas de cancelación
(voluntaria > involuntaria) es consistente con lo que está pasando en el sector globalmente,
no un artefacto local; y el patrón inverso AMI/VEH tiene un marco teórico plausible
(selección adversa dinámica), aunque no una confirmación exacta por diferencia de diseño del
dato (predictivo vs. retrospectivo).

**Lo que la validación externa no puede resolver — porque el documento interno no lo mide:**
la causa raíz del 59% de cancelación voluntaria (precio vs. servicio vs. competencia). Es el
mayor vacío de valor de negocio identificado en este cruce: RIMAC tiene el "quién" con
precisión (el score) pero no el "por qué" (la causa), y la literatura de industria sugiere que
mezclar ambas causas en una sola gestión de retención desperdicia la ventana ya bien diseñada.

## 6. Limitaciones

- La comparación de lift/concentración (§2) usa un benchmark académico de dataset(s)
  distinto(s) al de RIMAC — dirección robusta, no comparación controlada exacta.
- F-390/F-391 dan el marco teórico más cercano encontrado para el patrón AMI/VEH, pero el
  dato de RIMAC es predictivo, no retrospectivo — la divergencia se declara, no se resuelve.
- F-392 es una cifra de cautela (agregador citando revista académica sin verificación directa
  de la fuente primaria en esta sesión).
- No se investigó específicamente el mercado peruano de switching/cancelación de seguros —
  la validación de industria (§3) es mayormente de EE.UU.

---

## Conexiones

- [[futuro-asesores-seguros-venta-digital|¿Desaparecerán los asesores de seguros?]] — ese
  node documenta que el punto de falla más agudo de lo 100%-digital es el reclamo, no la
  venta; este node aporta el paralelo en retención: RIMAC ya tiene el score, el vacío es el
  tratamiento diferenciado por causa, no la tecnología de detección.
- `research/lobo/opinion_experto.md` — tesis 21 traduce estos hallazgos a oportunidades y
  riesgos de negocio concretos para RIMAC.
