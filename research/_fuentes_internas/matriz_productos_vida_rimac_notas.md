# Matriz de productos Vida RIMAC — Notas y catálogo de coberturas

Documentación complementaria a `matriz_productos_vida_rimac.csv`. Última actualización: a partir de 6 documentos fuente (3 decks internos + 3 fichas comerciales vigentes).

## 1. Alcance y estado

**Confirmado con el usuario:** lo que en un inicio parecían 5 productos distintos son en realidad **3 productos reales**, con nombres comerciales que varían según la pieza:

| Producto | Nombres detectados | Variantes en la matriz |
|---|---|---|
| Vida Futuro Protegido | VFP | 4 filas (Plan 35, Plan 65, Plus 35, Plus 65) |
| Plan Vida Flexible | Plan Vida Flexible / Vida Ahorro Flexible (VAF) / Vida Inversión Flexible (VIF) | 1 fila |
| Producto dotal 170% | Vida Contigo / Vida Ahorro Garantizado / Vida Ahorro con Devolución | 1 fila |

Hay un **cuarto producto, Vida Temporal Total** (protección pura, sin ahorro/devolución), que ya cuenta con ficha comercial propia. Confirma características cualitativas (moneda, plazos, endoso, coberturas), pero aún no tiene cifras de edad de ingreso/permanencia, prima mínima ni suma asegurada — esos campos siguen marcados "PENDIENTE" en la matriz.

## 2. Trazabilidad de fuentes

| Documento | Tipo | Vigencia | Producto(s) que documenta |
|---|---|---|---|
| `Productos_VUL.pptx` | Capacitación interna | 2023 | Vida Futuro Protegido (VFP) |
| `Flexivida_-_Producto.pptx` | Comercial/capacitación | Marzo 2022 | Plan Vida Flexible |
| `Seguro_de_Vida_Flexible_2.pdf` | Ficha comercial | Vigente desde 01/01/2025 | Plan Vida Flexible |
| `Lanzamiento_Vida_Contigo_170_Devolución.pptx` | Repricing/lanzamiento | Junio 2023 | Vida Contigo (tabla de devolución por plazo/edad/moneda) |
| `Seguro_de_Vida_Contigo_2__1___1_.pdf` | Ficha comercial | Vigente desde 01/01/2025 | Vida Contigo |
| `Seguro_de_Vida_Ahorro_Garantizado.pdf` | Ficha comercial | Vigente desde 01/01/2025 | Vida Ahorro Garantizado |
| `Brochure_Temporal_Total_1__1_.pdf` | Ficha comercial | Vigente desde 01/01/2025 | Vida Temporal Total |

## 3. Catálogo de coberturas / addons

Estas coberturas se repiten entre productos con reglas propias por producto — de ahí que se documenten aparte en vez de ser columnas de la matriz principal.

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

**Nota de rigor:** las edades y carencias de esta tabla salen del deck `Flexivida_-_Producto.pptx` (2022) para las coberturas compartidas — no se confirmó si estas reglas exactas siguen vigentes en 2025 para Plan Vida Flexible ni si aplican igual a VFP y Vida Contigo. Tratar como referencia, no como condicionado vigente.

## 4. Preguntas abiertas / pendientes

- **Vida Temporal Total**: ya tiene ficha propia (`Brochure_Temporal_Total_1__1_.pdf`), que confirma moneda, plazos, endoso y las 4 coberturas. Sigue sin edad de ingreso/permanencia, prima mínima ni suma asegurada — la ficha es comercial resumida, no el condicionado. Si se necesita para la matriz completa, hay que pedir el condicionado o la ficha técnica interna.
- **Depósitos extraordinarios en Plan Vida Flexible**: dos versiones del mismo deck 2022 dan cifras distintas ("4 veces al año hasta $500,000" vs. "ilimitadamente") — no resuelto.
- **Devolución de Vida Contigo**: el 170% es un headline de marketing (2025); la tabla de repricing 2023 muestra que el % real varía bastante según plazo/edad/moneda (rango observado: ~100%–172%). No se debe usar "170%" como cifra fija en análisis comparativos sin la tabla completa.
- **Riesgo de suscripción, prima mínima y frecuencia de pago de Vida Contigo**: no especificados en ninguna de las 3 fuentes recibidas.
- **Correspondencia Plan Vida Flexible ↔ VAF/VIF**: confirmada por el usuario a nivel de producto, pero no verificada línea por línea contra el condicionado — si hay dudas puntuales de una regla específica, validar con Producto/Actuarial.

## 5. Nivel de confianza por producto

- **VFP — Alta**: una sola fuente (deck de capacitación 2023), datos internamente consistentes.
- **Plan Vida Flexible — Media-alta**: 3 fuentes con datos compatibles entre sí (2022 y 2025), pero con la duda de depósitos extraordinarios sin resolver.
- **Vida Contigo (3 nombres) — Media**: consolidación de 3 nombres comerciales confirmada por el usuario; el detalle exacto de coberturas varía levemente entre fichas.
- **Vida Temporal Total — Media**: tiene ficha propia y confirma características cualitativas, pero le faltan las cifras duras (edad, montos, prima) que sí tienen los demás productos.
