# Reporte quincenal — Fortalecimiento del modelo de usuarios sintéticos (seguros · Perú)

- **Fecha:** 2026-07-06
- **Próxima revisión:** 2026-07-21 (ciclo de 15 días)
- **Alcance:** buscar evidencia nueva para **añadir/recalibrar variables** del generador
  (`research/personas/generador/` y skill `lapuerta`) y proponer **cómo incorporarlas**.
- **Método:** búsqueda web de fuentes 2024–2026 (SBS, Gestión, PUCP, INEI, Infobae, UDEP, Banco
  Mundial, OECD). Cada propuesta marca su `origen` (`dato`/`supuesto`). Se evitaron variables ya
  existentes o propuestas en el reporte del 2026-06-21.

---

## Resumen ejecutivo
- **Vehículo importa, y mucho:** solo **2 de cada 10 vehículos** tienen seguro voluntario; el SOAT
  cubre ~**90%** de autos pero **4 de cada 5 motos NO** tienen SOAT, y las motos tienen una
  siniestralidad **5–7×** mayor (≈7% vs ≈1% en autos). El tipo de vehículo es un predictor fuerte
  de tenencia y riesgo que hoy no modelamos.
- **Salud y enfermedad crónica:** el gasto de bolsillo en salud está fuertemente asociado a
  **enfermedad crónica**, ingreso y educación; empuja la demanda de seguro privado/EPS.
- **Brecha de género:** mujeres con cuenta **59%** (2 pp bajo hombres) pero solo **22%** en
  inclusión financiera avanzada vs **30%** hombres (brecha 8 pp); peores condiciones de crédito.
- **Vulnerabilidad económica:** Perú tiene más vulnerabilidad que pobreza; los hogares vulnerables
  recurren a familia/prestamistas informales en vez de ahorro/seguro formal.

---

## Tabla de variables candidatas (nuevas)

| # | Variable | Evidencia / dato | Fuente | Cómo incorporarla | Prioridad | Origen |
|---|---|---|---|---|---|---|
| 1 | `tenencia_vehiculo` | 2/10 con seguro voluntario; autos ~90% SOAT, motos 4/5 sin SOAT; moto 7% vs auto 1% siniestralidad | Gestión, amovernos | Marginal condicionada por región (más motos en Sierra/Selva/Costa); define obligatoriedad/cumplimiento SOAT y riesgo | Alta | dato |
| 2 | `enfermedad_cronica` | Gasto de bolsillo ↑ con enfermedad crónica; asociado a ingreso/educación | PUCP, AIS | Booleano condicionado por `generacion`; sube intención de seguro de salud privado y `wtp_ratio` | Media-Alta | dato |
| 3 | `genero` | Mujeres 59% cuenta (−2 pp); 22% inclusión avanzada vs 30% hombres; 55% billetera | INEI, Infobae, UDEP | Marginal ~50/50; modula `acceso_digital`, `bancarizado` y condiciones; eje de equidad | Media | dato |
| 4 | `vulnerabilidad_economica` | Más vulnerabilidad que pobreza; hogares vulnerables usan buffers informales | Banco Mundial, OECD | Condicionada por `nse`; alta → ↓ tenencia, ↑ peso del sesgo del presente, ↓ WTP | Media | dato/supuesto |
| 5 | `nivel_endeudamiento` | El monitoreo de hogares evalúa endeudamiento (bajó a dic-2024) | SBS (IESF 2025) | {alto/medio/bajo}; alto → ↓ capacidad/WTP, ↑ sensibilidad a precio | Baja | supuesto |

---

## Detalle y propuesta de incorporación

### 1) `tenencia_vehiculo`  (ninguno / auto / moto_mototaxi) — **Alta**
- **Evidencia:** del parque, solo **2/10** tiene seguro voluntario; SOAT en autos ~**90%**, pero
  en motos solo ~**1 de 5** lo tiene; siniestralidad moto **~7%** vs auto **~1%**. El mototaxismo
  informal concentra siniestros.
- **Incorporación:** marginal condicionada por `region` (mayor proporción de moto/mototaxi fuera de
  Lima). Efectos:
  - Define la base de **tenencia obligatoria** (SOAT) y su **cumplimiento** (auto alto, moto bajo).
  - `moto_mototaxi` → mayor exposición/riesgo → mayor necesidad pero menor cumplimiento (informalidad).
  - Conecta con un futuro producto **seguro vehicular voluntario** (hoy raro: 2/10).

### 2) `enfermedad_cronica`  (sí / no) — **Media-Alta**
- **Evidencia:** la presencia de enfermedad crónica/discapacidad **aumenta** el gasto de bolsillo en
  salud; asociado a ingreso y educación. El SIS/EsSalud no eliminan ese gasto.
- **Incorporación:** booleano condicionado por `generacion` (mayor en Gen X/Boomer). Efectos:
  - ↑ intención de **seguro de salud privado/EPS** y ↑ `wtp_ratio` para coberturas de salud.
  - Interactúa con `cobertura_salud_publica` (propuesta previa).

### 3) `genero`  (mujer / hombre) — **Media**
- **Evidencia:** cuenta 59% mujeres (−2 pp vs hombres); **22%** inclusión avanzada (vs 30%);
  **55%** con billetera digital; emprendedoras reciben montos menores y tasas más altas.
- **Incorporación:** marginal ~50/50. Modula a la baja (leve) `acceso_digital`, `bancarizado` y la
  intención en niveles avanzados; habilita **análisis de equidad de género** de la cartera.

### 4) `vulnerabilidad_economica`  (alta / media / baja) — **Media**
- **Evidencia:** Perú con más vulnerabilidad que pobreza; los hogares vulnerables recurren a
  **familia/prestamistas informales** y reducen consumo ante crisis, en vez de ahorro/seguro formal.
- **Incorporación:** condicionada por `nse`. Efectos: alta → ↓ `tenencia`, refuerza el efecto del
  `sesgo_presente`, ↓ `wtp_ratio`. Buen proxy de "capacidad de absorber shocks".

### 5) `nivel_endeudamiento`  (alto / medio / bajo) — **Baja**
- **Evidencia:** el sistema monitorea el endeudamiento de hogares (bajó hacia dic-2024).
- **Incorporación:** {alto/medio/bajo}; alto → ↓ capacidad de pago/WTP y ↑ sensibilidad a precio.

---

## Cambios propuestos al esquema (`synthetic_user_schema.json`)

```jsonc
// nuevas marginales / condicionales (bosquejo)
"genero": { "origen": "dato", "categorias": { "mujer": 0.50, "hombre": 0.50 } },
"tenencia_vehiculo": {
  "origen": "dato", "condicional_de": "region",
  "nota": "ninguno mayoritario; moto_mototaxi más frecuente fuera de Lima"
},
"enfermedad_cronica": {
  "origen": "dato", "condicional_de": "generacion",
  "nota": "mayor prevalencia en Gen X / Boomer"
},
"vulnerabilidad_economica": { "origen": "dato/supuesto", "condicional_de": "nse" }
```

```jsonc
// nuevos términos en modelos derivados
"tenencia_seguro": {
  "drivers": {
    "tenencia_vehiculo": { "auto": 0.5, "moto_mototaxi": -0.2, "ninguno": 0.0 },
    "vulnerabilidad_alta": -0.5
  }
},
"wtp_ratio": {
  "ajustes": { "enfermedad_cronica_si": "+0.10", "vulnerabilidad_alta": "-0.12" }
}
```

> **Re-validar** tras incorporar: mantener marginales objetivo (tiene seguro ≈ 0.40,
> desconfía ≈ 0.48, seguro de desastres ≈ 0.033) y revisar que `genero`/`vulnerabilidad` no
> sesguen la tenencia global fuera de rango.

---

## Cómo se incorporaría en el flujo
1. Añadir marginales/condicionales a `research/personas/generador/synthetic_user_schema.json`.
2. Ampliar `generate_synthetic_users.py` para muestrear las nuevas variables (respetando dependencias).
3. Sumar los términos a los modelos de `tenencia` y `wtp`; agregar intención de "seguro de salud privado".
4. Recalibrar interceptos para sostener las marginales objetivo.
5. Actualizar codebook (`SKILL.md`) y lámina.

---

## Fuentes
- Gestión — SOAT: 4 de cada 5 motos sin seguro: https://gestion.pe/tu-dinero/soat-cuatro-de-cada-5-motos-no-tiene-seguro-a-que-se-debe-sbs-accidentes-de-transito-aseguradoras-motocicletas-noticia/
- Gestión — Dos de cada 10 vehículos con seguro: https://gestion.pe/mix/mi-bolsillo/dos-de-cada-10-vehiculos-cuentan-con-seguro-cuatro-mitos-sobre-la-cobertura-vehicular-i-seguro-vehicular-i-soat-i-mitos-noticia/
- amovernos — Por qué el SOAT de moto es tan caro (siniestralidad/informalidad): https://amovernos.com/por-que-el-soat-de-moto-es-tan-caro-en-el-peru-la-combinacion-de-riesgo-informalidad-y-numeros-en-rojo/
- PUCP — Determinantes del gasto de bolsillo en salud en el Perú: https://departamento-economia.pucp.edu.pe/documentos-de-trabajo/determinantes-del-gasto-de-bolsillo-en-salud-en-el-peru
- AIS Perú — El catastrófico gasto de bolsillo en salud: https://aisperu.org.pe/el-catastrofico-gasto-de-bolsillo-en-salud/
- Infobae — 22% de mujeres en inclusión financiera avanzada: https://www.infobae.com/peru/2025/03/23/el-22-de-las-mujeres-peruanas-alcanza-un-nivel-avanzado-de-inclusion-financiera/
- UDEP — Persisten desigualdades en acceso financiero de mujeres: https://www.udep.edu.pe/hoy/2025/05/persisten-desigualdades-en-acceso-financiero-de-mujeres-segun-reportes-del-2024/
- Banco Mundial (vía La República) — pobreza y vulnerabilidad en Perú: https://larepublica.pe/economia/2025/12/05/peru-sigue-rezagado-en-reduccion-de-pobreza-y-vulnerabilidad-segun-informe-delbancomundial-hnews-41573
- OECD — Social protection e informalidad en Perú (2025): https://www.oecd.org/en/publications/2025/10/expanding-social-protection-and-addressing-informality-in-latin-america_9a502cb3/full-report/towards-universal-social-protection-in-peru-challenges-and-possibilities_5b4ede08.html
- SBS — Informe de Estabilidad del Sistema Financiero (mayo 2025): https://www.sbs.gob.pe/Portals/0/IESF-2025-1A.pdf

---

*Generado por el ciclo quincenal de fortalecimiento del modelo `lapuerta`.*
