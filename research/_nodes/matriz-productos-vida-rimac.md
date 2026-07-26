# Matriz de productos Vida RIMAC — catálogo y coberturas

> Node. Fuente de verdad de este tema: catálogo de productos de Seguro de Vida Individual de
> RIMAC (qué existe, qué coberturas trae cada uno, con qué nivel de confianza y de qué fuente),
> más el trabajo de reconciliación de nombres comerciales duplicados. Complementa al node del
> proyecto Back to Basics (ver Conexiones) — ese node documenta el modelo de venta y el estado
> del proyecto; este node documenta el producto que se vende.
>
> Fecha de elaboración: 2026-07-24 · Última actualización: 2026-07-26 · Versión: v1.1
> (v1.0: catálogo inicial, "3(+1) productos reales" a partir de consolidar 5 nombres comerciales
> — Vida Contigo y Vida Ahorro Garantizado se trataban como el mismo producto dotal 170% con
> nombres distintos, y VFP figuraba como producto activo con confianza Alta.
> v1.1 (2026-07-26, confirmado por el usuario) corrige la premisa: **los productos finales son 6**
> — Vida Contigo y Vida Ahorro Garantizado son productos distintos, no el mismo producto con dos
> nombres; VFP queda fuera del catálogo activo (descontinuado); se agregan VCD digital y
> Endosable digital como productos finales aún sin caracterizar. Cambio estructural — reordena la
> tabla de §1, la trazabilidad de fuentes de §2, el catálogo de coberturas de §3 y los niveles de
> confianza de §6.)
> Fuentes: documento interno "Matriz de productos Vida RIMAC — Notas y catálogo de coberturas"
> (complementario a `matriz_productos_vida_rimac.csv`, ninguno de los dos vive en este
> repositorio), consolidado a partir de 6 documentos fuente internos (3 decks de
> capacitación/lanzamiento + 3 fichas comerciales vigentes desde 01/01/2025); corrección de
> alcance v1.1 confirmada directamente por el usuario en sesión (2026-07-26), sin documento fuente
> nuevo.

---

## 1. Alcance — 6 productos finales

**Los productos finales de Vida Individual son 6** (confirmado por el usuario, 2026-07-26 —
sustituye el conteo "3(+1)" de v1.0 de este node):

| Producto | Nombres detectados | Estado de caracterización |
|---|---|---|
| Plan Vida Flexible | Plan Vida Flexible / Vida Ahorro Flexible (VAF) / Vida Inversión Flexible (VIF) | Caracterizado (1 fila en la matriz fuente) |
| Vida Contigo | Vida Contigo / Vida Ahorro con Devolución | Caracterizado (1 fila en la matriz fuente) |
| Vida Ahorro Garantizado | Vida Ahorro Garantizado | Caracterizado (ficha comercial propia, §2) |
| Vida Temporal Total | Vida Temporal Total | Caracterizado cualitativamente; sin cifras duras (edad, prima, suma asegurada) — ver §5 |
| VCD digital | VCD digital | **Pendiente de caracterizar** — sin ficha ni fuente propia todavía |
| Endosable digital | Endosable digital | **Pendiente de caracterizar** — sin ficha ni fuente propia todavía |

**VFP (Vida Futuro Protegido) queda fuera del catálogo activo — descontinuado** (confirmado por
el usuario, 2026-07-26). Se conserva como referencia histórica en §2 (trazabilidad) y §3
(catálogo de coberturas, donde varias coberturas compartidas estaban documentadas también para
VFP) porque esas fuentes ya estaban consolidadas en v1.0 de este node, pero **no tratar a VFP
como parte de la oferta comercial vigente** en ningún material nuevo.

**Nota sobre la consolidación anterior:** v1.0 de este node trataba a Vida Contigo y Vida Ahorro
Garantizado como el mismo "producto dotal 170%" con nombres distintos, apoyado en que ambas
fichas comerciales (§2) documentan una cobertura de sobrevivencia/devolución similar. Esa lectura
queda corregida: son dos productos distintos con ficha comercial propia cada uno.

## 2. Trazabilidad de fuentes

| Documento | Tipo | Vigencia | Producto(s) que documenta |
|---|---|---|---|
| `Productos_VUL.pptx` | Capacitación interna | 2023 | Vida Futuro Protegido (VFP) — **descontinuado, ver §1**; se conserva la fila por trazabilidad histórica |
| `Flexivida_-_Producto.pptx` | Comercial/capacitación | Marzo 2022 | Plan Vida Flexible |
| `Seguro_de_Vida_Flexible_2.pdf` | Ficha comercial | Vigente desde 01/01/2025 | Plan Vida Flexible |
| `Lanzamiento_Vida_Contigo_170_Devolución.pptx` | Repricing/lanzamiento | Junio 2023 | Vida Contigo (tabla de devolución por plazo/edad/moneda) |
| `Seguro_de_Vida_Contigo_2__1___1_.pdf` | Ficha comercial | Vigente desde 01/01/2025 | Vida Contigo |
| `Seguro_de_Vida_Ahorro_Garantizado.pdf` | Ficha comercial | Vigente desde 01/01/2025 | Vida Ahorro Garantizado |
| `Brochure_Temporal_Total_1__1_.pdf` | Ficha comercial | Vigente desde 01/01/2025 | Vida Temporal Total |
| *(sin documento fuente todavía)* | — | — | VCD digital — **pendiente**, ver §5 |
| *(sin documento fuente todavía)* | — | — | Endosable digital — **pendiente**, ver §5 |

Ninguno de estos documentos vive en este repositorio ni es fuente externa citable por `cronista`
— son documentación comercial/interna de RIMAC, mismo tratamiento que los documentos fuente del
node [[proyecto-back-to-basics-ffvv-vida|Proyecto Back to Basics — FFVV Vida Individual]].

## 3. Catálogo de coberturas / addons

**Nota (2026-07-26):** la columna "Presente en" de esta tabla sigue listando a VFP tal como se
consolidó en v1.0 de este node, porque la fuente (`Flexivida_-_Producto.pptx`) documentaba las
coberturas compartidas citando a VFP junto con Plan Vida Flexible y Vida Contigo. **VFP está
descontinuado (§1)** — al usar esta tabla para un material nuevo, leer esas menciones como
referencia histórica de qué cobertura existía en el producto descontinuado, no como parte de la
oferta vigente.

Estas coberturas se repiten entre productos con reglas propias por producto — de ahí que se
documenten aparte en vez de ser columnas de una matriz única:

| Cobertura | Qué cubre | Edad ingreso | Edad permanencia | Monto / % | Carencia | Presente en |
|---|---|---|---|---|---|---|
| Fallecimiento (principal) | Muerte natural o accidental | Según producto | Según producto | Mín. $50,000 (VFP) / desde $3K (Vida Contigo) | Ninguna | VFP, Plan Vida Flexible, Vida Contigo |
| IAFA (Indemnización Adicional por Fallecimiento Accidental) | Monto extra si el fallecimiento es por accidente | — | 64 años y 364 días | = SA fallecimiento, mín. $50,000 | Ninguna | VFP, Plan Vida Flexible |
| Enfermedades Graves (EG) | Infarto, derrame, bypass, cáncer, trasplante, insuficiencia renal | 18–59a364d | 64a364d | 50% capital, máx. $50,000 (VFP) / 25–50%, máx. $50,000 (Plan Vida Flexible) | 180 días | VFP, Plan Vida Flexible, Vida Contigo |
| ITP 2/3 (Invalidez Total y Permanente) | Pérdida ≥2/3 capacidad de trabajo por enfermedad o accidente | 18–59a364d | 64a364d | = SA fallecimiento, mín. $50,000 | 6 meses | VFP, Plan Vida Flexible, Vida Contigo (variante cancelatoria) |
| PEI (Pérdida de Existencia Independiente) | Incapacidad para 3+ de 6 actividades básicas diarias | 18–59a364d | 74a364d | SA $50,000 | 6 meses (no aplica en accidente) | VFP, Plan Vida Flexible |
| DPP (Dispensa de Pago de Primas) | Exonera primas si el titular queda incapacitado | 18–59a364d | 64a364d | — | 1 año | Plan Vida Flexible, Vida Contigo |
| Renta Hospitalaria por Accidente | Indemnización por día de hospitalización, hasta 30 días | 18–64a364d (hijos 0–24a364d) | 64a364d (hijos 24a364d) | Según SA contratada | Activa desde 24h hospitalizado | Plan Vida Flexible, Vida Contigo |
| Indemnización por Cirugía | Indemnización por intervención quirúrgica | 18–64a364d | 74a364d | Según SA contratada | 60 días (no aplica accidente) | Plan Vida Flexible |
| Asistencia de Sepelio | Cobertura de sepelio a titular y familiares | 18–64a364d (hijos 0–27a364d) | 94a364d (hijos 27a364d) | Según plan (Plus/Full) | 30 días | Plan Vida Flexible |
| Desempleo Involuntario | Indemnización por despido involuntario | 18–64a184d | 64a364d | Según SA | 60 días | Plan Vida Flexible |
| Sobrevivencia / Devolución | Pago del % de devolución elegido si se llega al final de la vigencia | — | Depende del plazo | % elegido al contratar (hasta 170%) | — | Vida Contigo (es la cobertura definitoria del producto) |
| Asistencias (American Assist / Vida Platinum) | Servicios de salud, hogar, veterinaria, descuentos | — | — | — | — | VFP (American Assist) · Vida Contigo (Vida Platinum) |
| Dental (COA) | Cobertura dental | — | — | — | 30 días de carencia, cobertura x 11 meses | VFP (solo 1er año) |

**Nota de rigor:** las edades y carencias de esta tabla salen del deck `Flexivida_-_Producto.pptx`
(2022) para las coberturas compartidas — no se confirmó si estas reglas exactas siguen vigentes
en 2025 para Plan Vida Flexible ni si aplican igual a VFP y Vida Contigo. Tratar como referencia,
no como condicionado vigente.

## 4. Caveat operativo — no usar "170%" como cifra fija

**El 170% es un headline de marketing (2025).** La tabla de repricing 2023
(`Lanzamiento_Vida_Contigo_170_Devolución.pptx`) muestra que el porcentaje real de devolución de
Vida Contigo varía bastante según plazo, edad y moneda — rango observado ~100%–172%. **No usar
"170%" como cifra fija en análisis comparativos, materiales de venta o presentaciones sin la
tabla completa de repricing.** Esto es relevante directamente para cualquier material que el
proyecto Back to Basics produzca citando este producto (ver Conexiones) — incluida cualquier
lámina o deck ya construido que use "170%" como cifra puntual.

## 5. Preguntas abiertas / pendientes

- **VCD digital y Endosable digital**: confirmados como 2 de los 6 productos finales (§1,
  2026-07-26), pero **sin ninguna fuente ni ficha todavía** — no hay coberturas, montos, edades ni
  condiciones documentadas. Máxima prioridad de levantamiento si el proyecto necesita citarlos en
  cualquier material dirigido al asesor o al cliente.
- **Vida Temporal Total**: tiene ficha propia (`Brochure_Temporal_Total_1__1_.pdf`), que confirma
  moneda, plazos, endoso y las 4 coberturas. Sigue sin edad de ingreso/permanencia, prima mínima
  ni suma asegurada — la ficha es comercial resumida, no el condicionado. Si se necesita para la
  matriz completa, hay que pedir el condicionado o la ficha técnica interna.
- **Vida Ahorro Garantizado**: tiene ficha propia (`Seguro_de_Vida_Ahorro_Garantizado.pdf`), antes
  tratada como el mismo producto que Vida Contigo (v1.0 de este node) — separados en v1.1 (§1).
  No se re-auditó el detalle de coberturas de su ficha de forma independiente de Vida Contigo;
  pendiente si se necesita el detalle línea por línea.
- **Depósitos extraordinarios en Plan Vida Flexible**: dos versiones del mismo deck 2022 dan
  cifras distintas ("4 veces al año hasta $500,000" vs. "ilimitadamente") — no resuelto.
- **Riesgo de suscripción, prima mínima y frecuencia de pago de Vida Contigo**: no especificados
  en ninguna de las 3 fuentes recibidas.
- **Correspondencia Plan Vida Flexible ↔ VAF/VIF**: confirmada por el usuario a nivel de
  producto, pero no verificada línea por línea contra el condicionado — si hay dudas puntuales de
  una regla específica, validar con Producto/Actuarial.

## 6. Nivel de confianza por producto

- **Plan Vida Flexible — Media-alta**: 3 fuentes con datos compatibles entre sí (2022 y 2025),
  pero con la duda de depósitos extraordinarios sin resolver.
- **Vida Contigo — Media**: 2 fuentes (repricing 2023 + ficha 2025) con datos compatibles.
- **Vida Ahorro Garantizado — Media**: tiene ficha propia (2025); no se auditó su detalle de forma
  tan profunda como Vida Contigo, al haberse tratado como el mismo producto hasta v1.0.
- **Vida Temporal Total — Media**: tiene ficha propia y confirma características cualitativas,
  pero le faltan las cifras duras (edad, montos, prima) que sí tienen los demás productos.
- **VCD digital — Sin caracterizar**: ningún dato disponible todavía (§5).
- **Endosable digital — Sin caracterizar**: ningún dato disponible todavía (§5).
- **VFP — Descontinuado (§1)**: ya no forma parte del catálogo activo; su confianza histórica
  (Alta, una sola fuente internamente consistente) queda solo como referencia por si se necesita
  material retrospectivo.

---

## Limitaciones

- Este node consolida un documento interno de RIMAC (no público, subido directamente a la sesión
  el 2026-07-24) — no es investigación con fuentes externas nuevas; no se registraron filas
  nuevas en `research/fuentes/codice.md` porque ninguna de las fuentes citadas aquí es evidencia
  externa citable (son documentación comercial/interna propia de RIMAC).
- Los documentos fuente (`Productos_VUL.pptx`, `Flexivida_-_Producto.pptx`, las fichas
  comerciales, `matriz_productos_vida_rimac.csv`) **no viven en este repositorio** — este node
  resume su contenido relevante, no los reemplaza como fuente primaria.
- Vida Temporal Total tiene la confianza más baja entre los productos con ficha propia por falta
  de cifras duras — no tratar sus datos cualitativos como equivalentes en completitud a los de
  Plan Vida Flexible.
- VCD digital y Endosable digital son productos finales confirmados (§1) pero sin ninguna
  caracterización todavía — no inventar coberturas, montos ni condiciones para ellos en ningún
  material derivado de este node.
- El caveat del §4 (no usar "170%" como cifra fija) aplica retroactivamente a cualquier material
  ya construido por el proyecto que haya citado esa cifra sin la tabla completa — no se auditó en
  este node si algún material existente (p. ej. el deck del proyecto Back to Basics) incurre en
  esto; queda como verificación pendiente si se necesita.

---

## Conexiones

- [[proyecto-back-to-basics-ffvv-vida|Proyecto Back to Basics — FFVV Vida Individual (RIMAC)]] —
  este catálogo de producto es insumo directo del Bloque 4 del Playbook del Asesor (§4 de ese
  node, "venta consultiva de 4 pasos" — motivación → dimensionamiento → perfil financiero →
  propuesta) y del ejercicio de dimensionamiento del Plan Piloto (§8 de ese node, Casos C y D) —
  ambos requieren saber qué cubre y cuánto cuesta cada producto real, no solo el modelo de
  conversación. Los 6 productos finales de §1 (Plan Vida Flexible, Vida Contigo, Vida Temporal
  Total, Vida Ahorro Garantizado, VCD digital, Endosable digital) son los que debe reflejar
  cualquier mención de catálogo en ese node.
- [[glosario-seguro-vida-peru|Glosario de seguro de vida en lenguaje claro]] — glosario de
  cliente que deliberadamente no cubre el detalle técnico de coberturas (IAFA, EG, ITP,
  PEI, DPP); ese detalle vive en el §3 de este node.
