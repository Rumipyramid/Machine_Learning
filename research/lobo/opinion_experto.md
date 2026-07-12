# 🐺 El Lobo — Opinión de negocio acumulada

> No vengo a resumir papers. Vengo a decir dónde hay plata, dónde se quema plata,
> y qué jugada haría yo con lo que el `cronista` ya verificó. Cada tesis carga su
> evidencia (F-n del ledger `research/fuentes/registro_fuentes.md`) y un nivel de
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
el conocimiento, no la conversión. Si el negocio mide éxito de un glosario en
ventas, está midiendo la métrica equivocada.
- **Evidencia:** F-9 (🟢A, RCT N≈124,000), F-10 (🟢A, síntesis canónica)
- **Confianza:** Alta
- **Actualizado:** 2026-07-12

### 2. El coaseguro variable es el cuello de botella de comprensión #1 en seguros de salud
Dos estudios (uno con dos encuestas representativas EE.UU., otro con encuesta
nacional del regulador de salud) coinciden: el coaseguro es el término peor
entendido, y quien tiene un plan con coaseguro/tarifas variables subestima sus
costos reales por un margen mucho mayor que quien tiene deducible fijo. Esto no es
un problema de comunicación — es un problema de diseño de producto.
- **Evidencia:** F-6 (🟢A, Loewenstein et al. 2013), F-7 (🔵B, KFF 2017)
- **Confianza:** Alta
- **Actualizado:** 2026-07-12

### 3. El problema de comprensión es estructural, no generacional — no lo resuelve "educar a los jóvenes"
Solo ~1 de cada 4 adultos Gen Z en EE.UU. puede definir deducible o copago. Cruzado
con la tesis 1 y 2, el patrón es consistente: ni la generación más "nativa digital"
entiende los términos base, y aunque los entendiera, eso no predice que compre.
Cualquier estrategia que apueste a "la próxima generación va a entender mejor" no
tiene sustento.
- **Evidencia:** F-8 (🟡C, NAIC 2024 — nota de asociación, método no detallado)
- **Confianza:** Media (una sola fuente C; consistente con F-6/F-7 pero no del
  mismo rigor)
- **Actualizado:** 2026-07-12

### 4. La brecha de aseguramiento sísmico en Perú es una categoría de producto casi vacía
Solo ~3.3% de los hogares peruanos tiene seguro contra sismos/desastres en un país
de altísima exposición sísmica. El dato circula vía prensa citando a APESEG (el
gremio del sector — incentivo a dramatizar la brecha para pedir regulación
favorable), no vía fuente primaria auditada directamente.
- **Evidencia:** F-5 (🟠D, Infobae vía APESEG)
- **Confianza:** Media — la dirección del hallazgo (brecha enorme) es creíble y
  consistente con la baja penetración general del mercado peruano, pero el número
  exacto no está verificado en fuente primaria. Antes de dimensionar un caso de
  negocio con el 3.3%, pedir el dato directo de APESEG/SBS.
- **Actualizado:** 2026-07-12

### 5. ESG como diferenciador de marca: aplica al consumidor global premium, no está probado en Perú
Bain reporta que ~80% de consumidores globales quiere criterios ESG integrados en
sus seguros. Es una encuesta propia de consultora (no auditable) y de alcance
global — extrapolarla al consumidor peruano medio (con problemas de tenencia
básica, no de diferenciación ESG) es **instinto**, no dato.
- **Evidencia:** F-4 (🟡C, Bain & Company 2023, alcance global)
- **Confianza:** Baja para el mercado peruano específicamente
- **Actualizado:** 2026-07-12

## 💰 Oportunidades

- **Producto paramétrico de bajo costo contra sismos.** Categoría con ~96.7% de
  hogares sin cobertura (tesis 4) en un país donde SOAT —un seguro obligatorio de
  bajo entendimiento y alto conocimiento (94%, F-1)— ya probó que la distribución
  masiva funciona cuando el producto es simple y el precio es bajo. Jugada:
  bundling o cross-sell sobre la base de SOAT, no venta desde cero.
- **Rediseñar el producto, no el glosario.** Si el coaseguro variable es el
  problema (tesis 2) y la divulgación no cambia conducta (tesis 1), la jugada de
  mayor ROI es lanzar variantes con deducible fijo y simuladores de costo en el
  punto de venta — no otro explicador. Esto convierte un hallazgo académico en
  ventaja de producto frente a competidores que siguen invirtiendo en "educar".
- **Distribución por bróker/intermediario para superar desconfianza.** *Instinto,
  no ledger-backed todavía*: en mercados de baja confianza institucional, la
  intermediación humana suele convertir mejor que el canal digital directo. Vale
  la pena que `seeker` o `marketer` busquen evidencia dura (tasa de conversión
  bróker vs. digital en Perú) antes de apostarle presupuesto.

## ⚠️ Riesgos

- **Quemar presupuesto de marketing en "educación financiera" esperando ventas.**
  Es el error más respaldado por evidencia del ledger (tesis 1, dos fuentes A). Si
  el objetivo real es conversión, ese presupuesto rinde más en simplificación de
  producto o en el canal de bróker.
- **Lanzar producto Gen Z con coaseguro variable pensando que "ya van a entender".**
  Tesis 2 + 3 combinadas: ni el consumidor promedio ni el más joven entienden el
  coaseguro. Ese diseño produce fricción, quejas y probable lapse/churn temprano.
- **Dimensionar un caso de negocio de seguros de desastres con el 3.3% sin
  verificar la fuente primaria.** Es un número de gremio (APESEG) vía prensa (D),
  no auditado. Usarlo para levantar capital o justificar inversión sin
  confirmación directa es un riesgo de credibilidad si el número no resiste
  escrutinio.
- **F-15 sigue marcada "NO USAR" en el ledger** (cifra de UnitedHealth sin método
  verificable, ~9% entiende términos básicos). Cuidado con que se cuele en algún
  deck o caso de negocio — no tiene respaldo.

## 📔 Bitácora

- **2026-07-12** — Primera creación de la opinión. Revisé las 15 fuentes del
  ledger (`registro_fuentes.md`, F-1 a F-15). Construí 5 tesis iniciales: (1)
  la divulgación no convierte, (2) el coaseguro es el cuello de botella de
  comprensión, (3) el problema es estructural/no generacional, (4) la brecha
  sísmica peruana es una categoría casi vacía, (5) ESG es palanca global, no
  probada en Perú. Marqué 3 oportunidades y 4 riesgos, incluyendo la advertencia
  de no usar F-15. Sin entradas previas contra las cuales comparar — este es el
  punto de partida.
