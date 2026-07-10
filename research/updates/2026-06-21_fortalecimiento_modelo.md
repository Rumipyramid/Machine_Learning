# Reporte quincenal — Fortalecimiento del modelo de usuarios sintéticos (seguros · Perú)

- **Fecha:** 2026-06-21
- **Próxima revisión:** 2026-07-06 (ciclo de 15 días)
- **Alcance:** buscar datos/evidencia recientes que permitan **añadir o recalibrar variables**
  del generador (`.claude/skills/lapuerta/`) y proponer **cómo incorporarlas**.
- **Método:** búsqueda web de fuentes 2024–2026 (INEI, BCRP, SBS, MAPFRE, INEI/ENAHO, prensa
  especializada, literatura). Cada propuesta marca su `origen` (`dato` vs `supuesto`).

> Las propuestas son sugerencias de diseño; antes de adoptarlas en decisiones reales, recalibrar
> con micro-datos (ENAHO/ENDES) y validar marginales.

---

## Resumen ejecutivo

La evidencia reciente apunta a **cinco palancas** que hoy el modelo no captura y que explican
buena parte de la tenencia/intención de seguro en Perú:

1. **Acceso digital y billeteras móviles** (Yape/Plin) — habilitador clave de canal y microseguros.
2. **Situación laboral / informalidad** — define quién accede a Vida Ley y a bancaseguros.
3. **Bancarización** — puerta de entrada a la venta de seguros (bancaseguros).
4. **Experiencia previa con siniestros** — el predictor de confianza más fuerte tras la información.
5. **Conciencia de riesgo climático** (no solo sísmico) — impulsa microseguros paramétricos (IoT +300%).

Marginales reales útiles encontradas: **bancarización ≈ 59%** de adultos (urbano 61% vs rural 37%;
educación universitaria 86.5% vs primaria 33.3%); insurtech LatAm **+117%** de inversión en 2025
con Perú entre los 3 polos; **67%** prefiere experiencias "phygital"; microseguros agrícolas IoT
**+300%** de adopción.

---

## Tabla de variables candidatas

| # | Variable candidata | Evidencia / dato | Fuente | Cómo incorporarla (resumen) | Prioridad | Origen |
|---|---|---|---|---|---|---|
| 1 | `acceso_digital` | Bancarización 59%; urbano 61% / rural 37%; Yape/Plin masivos | BCRP, INEI, BBVA | Variable condicional de `region`+`nse`+`generacion`; alimenta `canal_preferido` y `apertura_datos_ia` | Alta | dato |
| 2 | `situacion_laboral` | Informalidad laboral ~70%; Vida Ley solo asalariados formales; microseguros a microemprendedores | SBS, MAPFRE | Nueva marginal; condiciona `tenencia_seguro` (obligatorio) y acceso a microseguro | Alta | dato/supuesto |
| 3 | `bancarizado` | 59% en el sistema financiero; bancaseguros depende de tener cuenta/crédito | BCRP, SBS | Booleano derivado de `nse`+`region`+`acceso_digital`; habilita canal `bancaseguros` | Alta | dato |
| 4 | `experiencia_siniestro` | La rapidez/transparencia del siniestro es el driver de confianza nº1 | EY, Bain, SBS | Nueva marginal {positiva/negativa/ninguna}; entra al modelo de `confianza` y `tenencia` | Media-Alta | dato |
| 5 | `conciencia_riesgo_climatico` | Microseguros paramétricos IoT +300%; riesgo de inundación/Niño además del sísmico | MAPFRE | Condicional de `region`+`exposicion`; impulsa `seguro_desastres` y `wtp_ratio` | Media | dato/supuesto |
| 6 | `cobertura_salud_publica` | SIS/EsSalud muy extendidos; afectan necesidad percibida de seguro privado | SBS/SIS | Marginal {SIS/EsSalud/ninguna}; modula intención de seguro de salud privado | Media | dato |
| 7 | `influencia_social` | 67% prefiere "phygital"; recomendación/boca a boca pesa en compra | Insurtech LatAm | Marginal {alta/baja}; pequeño empujón a intención de compra | Baja | supuesto |

---

## Detalle y propuesta de incorporación

### 1) `acceso_digital`  (alta / media / baja) — **Alta prioridad**
- **Evidencia:** 59% de adultos bancarizados; fuerte brecha urbano (61%) vs rural (37%) y por
  educación (universitaria 86.5% vs primaria 33.3%). Yape/Plin transformaron el pago móvil.
- **Incorporación:** tabla condicional de `region` × `nse` (× `generacion` para el sesgo joven).
  - Efectos: ↑ probabilidad de `canal_preferido = directo_digital`; ↑ `apertura_datos_ia`;
    habilita microseguros on-demand (ver variable 5).
- **Validación:** marginal global de "acceso digital alto" ≈ 55–60% urbano.

### 2) `situacion_laboral`  (formal_dependiente / independiente_microemprendedor / informal) — **Alta**
- **Evidencia:** Vida Ley es obligatorio solo para asalariados con +4 años; microseguros nuevos
  apuntan a microemprendedores formales con cuenta y pago digital; informalidad ~70%.
- **Incorporación:** nueva marginal. Condiciona `tenencia_seguro`:
  - `formal_dependiente` → mayor prob. de `solo_obligatorio` (Vida Ley) y de bancaseguros.
  - `independiente_microemprendedor` → objetivo de microseguro voluntario.
  - `informal` → menor tenencia; canal directo/ninguno.

### 3) `bancarizado`  (booleano) — **Alta**
- **Evidencia:** 59% en el sistema financiero; el canal bancaseguros requiere relación bancaria.
- **Incorporación:** derivado de `nse` + `region` + `acceso_digital`. Si `False`, baja fuerte la
  probabilidad de `canal_preferido = bancaseguros` y de tenencia voluntaria vía banco.

### 4) `experiencia_siniestro`  (positiva / negativa / ninguna) — **Media-Alta**
- **Evidencia:** el factor más correlacionado con confianza (tras "información") es la
  rapidez/transparencia del siniestro (EY, Bain). En el modelo actual la confianza es marginal fija.
- **Incorporación:** nueva marginal; entra como término en el ajuste de `confianza` y como driver
  positivo/negativo en el score de `tenencia`:
  - `positiva` → +confianza, +tenencia; `negativa` → −−confianza, −tenencia.

### 5) `conciencia_riesgo_climatico`  (alta / media / baja) — **Media**
- **Evidencia:** microseguros paramétricos con IoT crecieron +300%; el riesgo no es solo sísmico
  (inundaciones, Niño costero). Hoy solo modelamos `exposicion_riesgo_sismico`.
- **Incorporación:** condicional de `region` + `exposicion_riesgo_sismico`. Multiplica al alza la
  probabilidad de `seguro_desastres_naturales` y sube `wtp_ratio` para coberturas paramétricas.

### 6) `cobertura_salud_publica`  (SIS / EsSalud / ninguna) — **Media**
- **Evidencia:** SIS (~97% conocimiento) y EsSalud (~93%) muy extendidos; reducen la necesidad
  percibida de seguro de salud privado.
- **Incorporación:** marginal condicionada por `situacion_laboral` (EsSalud ligado a empleo formal)
  y `nse`. Modula una futura intención de "seguro de salud privado".

### 7) `influencia_social`  (alta / baja) — **Baja**
- **Evidencia:** 67% prefiere experiencias "phygital"; recomendación pesa en adopción.
- **Incorporación:** pequeño empujón (+/−) a la intención en `simulate_rules.py` (pregunta `contratar`).

---

## Cambios propuestos al esquema (`synthetic_user_schema.json`)

Bosquejo (ilustrativo) para las dos de mayor prioridad:

```jsonc
// nuevas marginales
"situacion_laboral": {
  "origen": "dato/supuesto",
  "categorias": { "formal_dependiente": 0.30, "independiente_microemprendedor": 0.25, "informal": 0.45 }
},
// condicional: acceso digital depende de región y NSE (resumen)
"acceso_digital": {
  "origen": "dato", "condicional_de": ["region", "nse"],
  "nota": "alto≈55-60% urbano; mucho menor en rural y NSE D/E"
}
```

Y nuevos términos en los modelos derivados:

```jsonc
"confianza_aseguradora": {
  "ajuste_por_experiencia": { "positiva": "+0.6 a confia", "negativa": "-0.7 a confia", "ninguna": "0" }
},
"tenencia_seguro": {
  "drivers": { "situacion_laboral": { "formal_dependiente": 0.6, "independiente_microemprendedor": 0.1, "informal": -0.6 },
               "bancarizado_true": 0.4, "experiencia_positiva": 0.5 }
}
```

> Tras editar el esquema, **re-validar** que las marginales clave sigan cerca de la realidad
> (`tiene seguro ≈ 0.40`, `desconfía ≈ 0.48`, `desastres ≈ 0.033`) y que las nuevas no rompan
> esos objetivos.

---

## Cómo se incorporaría en el flujo
1. Añadir las marginales/condicionales nuevas a `scripts/synthetic_user_schema.json`.
2. Ampliar `generate_synthetic_users.py` para muestrear las nuevas variables (en orden de dependencia).
3. Sumar los nuevos términos a los modelos de `confianza` y `tenencia`.
4. Recalibrar interceptos para mantener las marginales objetivo.
5. Actualizar el codebook en `SKILL.md` y la lámina.

---

## Fuentes
- INEI — Brechas de la inclusión financiera digital en Perú: https://www.inei.gob.pe/media/MenuRecursivo/investigaciones/brecha.pdf
- BCRP — Digitalización e inclusión financiera (Moneda 197): https://www.bcrp.gob.pe/docs/Publicaciones/Revista-Moneda/moneda-197/moneda-197-02.pdf
- SBS — Inclusión financiera: https://www.sbs.gob.pe/inclusion
- BBVA — Bancarización en Perú (billeteras móviles y jóvenes): https://www.bbva.com/es/pe/sostenibilidad/bancarizacion-en-peru-billeteras-moviles-y-jovenes-marcan-el-rumbo-pero-la-inclusion-financiera-sigue-siendo-un-desafio/
- MAPFRE — Insurtech LatAm cierra 2025 (+financiación): https://www.mapfre.com.pe/notas-de-prensa/sector-insurtech-latinoamericano-cierra-2025-mas-530-insurtech-200-millones-dolares-financiacion/
- MAPFRE — Microseguros para emprendedores en Perú: https://www.mapfre.com/en/communicate/sustainability-communicate/entrepreneurs-peru-microinsurance/
- El Español/Invertia — Inversión insurtech LatAm +117% en 2025: https://www.elespanol.com/invertia/disruptores-americas/20260216/inversion-ecosistema-insurtech-latinoamerica-crece-alcanza-millones-euros/1003744121114_0.html
- Determinantes de cobertura de salud (mujeres, ENDES 2017): https://link.springer.com/article/10.1186/s12939-020-01310-4

---

*Generado por el ciclo quincenal de fortalecimiento del modelo `lapuerta`.*
