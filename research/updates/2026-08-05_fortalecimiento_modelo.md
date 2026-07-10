# Reporte quincenal — Fortalecimiento del modelo de usuarios sintéticos (seguros · Perú)

- **Fecha:** 2026-08-05
- **Próxima revisión:** 2026-08-20 (ciclo de 15 días)
- **Alcance:** evidencia nueva para **añadir/recalibrar variables** del generador
  (`research/personas/generador/` y skill `lapuerta`, v1.2) y proponer **cómo incorporarlas**.
- **Método:** búsqueda web 2025–2026 (Mordor Intelligence, BID Invest, MAPFRE, Bloomberg Línea,
  Congreso/Pandape, APESEG/SBS). Cada propuesta marca su `origen`. Se evitaron variables ya
  existentes o propuestas (v1.0–v1.2 y reportes 2026-06-21 / 2026-07-06 / 2026-07-21).

---

## Resumen ejecutivo
- 🛵 **Economía de plataformas sin protección:** ~**113 mil repartidores/socios** y ~2 millones de
  usuarios operan en apps (Rappi, PedidosYa, etc.) **sin seguro de salud, pensión ni accidentes**;
  hay un proyecto en el Congreso para reconocerles beneficios. Es un sub-segmento masivo, joven y
  digital, con brecha de protección **aguda y específica** → foco natural de microseguro de
  accidentes/salud *on-demand*.
- 🧩 **Microseguros = la frontera de crecimiento:** salud y microseguros son los espacios
  "no explotados"; encajan con personas de **ingreso variable, alta informalidad y baja tolerancia
  a primas altas** pero con clara necesidad de protección (MAPFRE ya lanzó microseguros para
  pequeños emprendedores). El modelo hoy no distingue *quién es receptivo a una prima baja*.
- 📱 **El canal digital directo se acelera:** bancaseguros aún pesa **37.65%** del mercado (2025),
  pero los canales **directo online + insurtech** proyectan **+12.31% CAGR** a 2031, con crecimiento
  de dos dígitos en altas online entre **menores de 40**. El `canal_preferido` debería inclinarse
  por generación, no ser plano.
- 📉 **Contexto de penetración (recalibración):** mercado ~**USD 7.84 mil M** en 2026 (+~8–9% anual),
  penetración estancada en **2.0–2.1% del PBI**; **No-Vida = 78%** del mercado (empuje de obligatorios).
  Solo **~11%** tiene seguro de salud y **<20%** seguro de vida → confirma marginales bajas del modelo.

---

## Tabla de variables candidatas (nuevas)

| # | Variable | Evidencia / dato | Fuente | Cómo incorporarla | Prioridad | Origen |
|---|---|---|---|---|---|---|
| 1 | `trabajo_plataforma_digital` | ~113k repartidores/socios, 2M usuarios; sin salud/pensión/accidentes; proyecto de ley en curso | Bloomberg Línea, Pandape, Ideele | Booleano condicional de `situacion_laboral`+`generacion`+`acceso_digital`; ↑ afinidad microseguro/digital, brecha de accidentes | **Alta** | dato |
| 2 | `propension_microseguro` | Microseguros = espacio real para ingreso variable, informalidad alta y baja tolerancia a prima | Mordor, BID Invest, MAPFRE | Derivada {alta/media/baja} de `nse`+`situacion_laboral`+`acceso_digital`+`sesgo_presente`; abre vía de protección aun si `tenencia=ninguno` | **Alta** | dato/supuesto |
| 3 | `canal_preferido` (recalibrar) | Bancaseguros 37.65% (2025); directo+insurtech +12.31% CAGR; altas online ↑ en <40 | Mordor Intelligence | Volver `canal_preferido` **condicional de `generacion`** (jóvenes → directo_digital) | Media | dato |
| 4 | Marginales de salud/vida (recalibrar) | Seguro de salud ~11%; vida <20%; No-Vida 78% del mercado | Mordor Intelligence | Ajuste fino de targets de tenencia por ramo (no nueva variable) | Baja | dato |

---

## Detalle y propuesta de incorporación

### 1) `trabajo_plataforma_digital`  (sí / no) — **Alta**
- **Evidencia:** las apps de movilidad/delivery mueven ~**2 millones de usuarios**, **~113 mil**
  repartidores/socios y ~10 mil aliados. Al operar como autónomos, **no tienen contrato, seguro de
  salud, pensión ni cobertura de accidentes**; hay un proyecto aprobado en comisión del Congreso
  para reconocerles beneficios (régimen tipo D.L. 728). Colombia aprobó algo similar en 2025.
- **Por qué es nueva:** `situacion_laboral` distingue formal/independiente/informal, pero **no
  captura** este sub-segmento con un perfil único: joven, urbano, alto `acceso_digital`, exposición
  física a accidentes y **brecha de protección crítica**. Es el cliente arquetípico del microseguro
  *on-demand* y de accidentes personales.
- **Incorporación:** booleano condicional de `situacion_laboral` (sobre todo
  `independiente_microemprendedor` e `informal`) + `generacion` (Gen Z/Millennial) + `acceso_digital`
  (alta). Efectos: ↑ `propension_microseguro`, ↑ necesidad de **accidentes/salud**, afinidad
  **canal directo_digital**; no mueve por sí solo la tenencia voluntaria tradicional.

### 2) `propension_microseguro`  (alta / media / baja) — **Alta**
- **Evidencia:** salud y **microseguros** son señalados como la frontera de crecimiento no explotada;
  encajan con poblaciones de **ingreso variable, informalidad alta y baja tolerancia a primas
  elevadas** pero con necesidad real de protección. MAPFRE ya comercializa microseguros para
  pequeños emprendedores; el ecosistema fintech (>230 startups) experimenta con coberturas
  paramétricas y onboarding 100% digital.
- **Por qué es nueva:** el modelo decide hoy entre `voluntario / solo_obligatorio / ninguno`, pero
  un "ninguno" en seguro tradicional puede ser un **"sí" a un microseguro de S/ 5–15/mes**. Esta
  variable abre esa vía y permite simular el potencial de productos de bajo costo.
- **Incorporación:** variable **derivada** {alta/media/baja} por score:
  - ↑ con `nse` C/D (ingreso bajo-medio pero existente), `situacion_laboral` informal/independiente,
    `acceso_digital` alta, `trabajo_plataforma_digital`=sí, `apertura_datos_ia` alta.
  - ↓ con `sesgo_presente` alto y `nse` E extremo (capacidad de pago casi nula).
  - Efecto: define un mercado direccionable de microseguro **independiente** de `tenencia_seguro`.

### 3) `canal_preferido` → condicional de `generacion` — **Media (recalibración)**
- **Evidencia:** **bancaseguros 37.65%** del mercado (2025); **directo online + insurtech** con
  **+12.31% CAGR** proyectado a 2031 y **crecimiento de dos dígitos en altas online entre <40**.
- **Incorporación:** convertir `canal_preferido` de marginal plana a **tabla condicional de
  `generacion`**: Gen Z/Millennial → más `directo_digital`; Gen X/Boomer → más `bancaseguros`/`broker`.
  Mantener la mezcla agregada cercana a la actual para no romper `confianza` (broker ↑).

### 4) Recalibración de marginales por ramo — **Baja**
- **Evidencia:** seguro de **salud ~11%**, **vida <20%**, **No-Vida = 78%** del mercado (peso de
  obligatorios: vehicular, Vida Ley). Penetración macro **2.0–2.1% del PBI**, mercado ~USD 7.84 mil M.
- **Incorporación:** no es variable nueva; es un **chequeo de calibración**: el split
  voluntario/obligatorio del modelo ya refleja el dominio de obligatorios; verificar que la tenencia
  voluntaria de salud/vida no quede sobre-representada frente a estos techos.

---

## Cambios propuestos al esquema (`synthetic_user_schema.json`)

```jsonc
// 1) nueva variable condicional
"trabajo_plataforma_digital": {
  "origen": "dato", "condicional_de": ["situacion_laboral", "generacion", "acceso_digital"],
  "score": {
    "situacion_laboral": {"informal": 0.6, "independiente_microemprendedor": 0.8, "formal_dependiente": -1.5},
    "generacion": {"Gen_Z_18_27": 0.8, "Millennial_28_43": 0.5, "Gen_X_44_59": -0.4, "Boomer_60_mas": -1.5},
    "acceso_digital": {"alta": 0.6, "media": 0.0, "baja": -1.0},
    "intercepto": -2.2   // marginal objetivo ~6-8% de la población adulta
  }
}
```

```jsonc
// 2) nueva variable derivada (mercado de microseguro)
"propension_microseguro": {
  "origen": "dato/supuesto", "salida": ["alta", "media", "baja"],
  "score": {
    "nse": {"A": -0.3, "B": 0.0, "C": 0.5, "D": 0.4, "E": -0.2},
    "situacion_laboral": {"informal": 0.5, "independiente_microemprendedor": 0.4, "formal_dependiente": -0.2},
    "acceso_digital": {"alta": 0.5, "media": 0.1, "baja": -0.5},
    "trabajo_plataforma_digital": {"true": 0.6, "false": 0.0},
    "sesgo_presente": {"alto": -0.4, "medio": 0.0, "bajo": 0.3},
    "intercepto": -0.1, "umbral_alta": 0.6, "umbral_media": -0.3
  }
}
```

```jsonc
// 3) canal_preferido recalibrado a condicional de generacion (sustituye la marginal plana)
"canal_preferido": {
  "origen": "supuesto", "condicional_de": "generacion",
  "tabla": {
    "Gen_Z_18_27":      {"directo_digital": 0.50, "bancaseguros": 0.25, "broker_corredor": 0.15, "ninguno": 0.10},
    "Millennial_28_43": {"directo_digital": 0.42, "bancaseguros": 0.30, "broker_corredor": 0.20, "ninguno": 0.08},
    "Gen_X_44_59":      {"directo_digital": 0.28, "bancaseguros": 0.32, "broker_corredor": 0.30, "ninguno": 0.10},
    "Boomer_60_mas":    {"directo_digital": 0.18, "bancaseguros": 0.30, "broker_corredor": 0.38, "ninguno": 0.14}
  }
}
```

> **Re-validar** tras incorporar: mantener marginales objetivo (tiene seguro ≈ 0.40,
> desconfía ≈ 0.48, desastres ≈ 0.033) y, en el agregado, la mezcla de canal cercana a la v1.2
> (directo ~0.35 / banca ~0.30 / broker ~0.25 / ninguno ~0.10) para no alterar `confianza_aseguradora`.
> `propension_microseguro` y `trabajo_plataforma_digital` **no** deben empujar la tenencia
> tradicional; abren un eje paralelo de producto de bajo costo.

---

## Cómo se incorporaría en el flujo
1. Añadir al esquema en orden de dependencia: `trabajo_plataforma_digital` (tras `situacion_laboral`,
   `generacion` y `acceso_digital`), luego `propension_microseguro` (derivada al final).
2. Reemplazar la marginal plana de `canal_preferido` por la tabla condicional de `generacion`.
3. Ampliar `generate_synthetic_users.py` (dos `sample_*` nuevas + lectura de tabla de canal).
4. Re-validar marginales y la mezcla de canal; actualizar codebook (`SKILL.md`), matriz y lámina.

---

## Fuentes
- Mordor Intelligence — Mercado de Seguros de Vida y No Vida de Perú (tamaño, canales, microseguros): https://www.mordorintelligence.com/industry-reports/life-non-life-insurance-market-in-peru
- BID Invest — Microseguros: la nueva frontera de la resiliencia financiera en ALC: https://idbinvest.org/en/blog/digital-economy/microinsurance-new-frontier-financial-resilience-latin-america-and-caribbean
- MAPFRE — Microseguros para pequeños emprendedores en Perú: https://www.mapfre.com/en/communicate/sustainability-communicate/entrepreneurs-peru-microinsurance/
- Bloomberg Línea — Avanza regulación laboral en apps de delivery en Perú: https://www.bloomberglinea.com/latinoamerica/peru/avanza-regulacion-laboral-en-apps-de-delivery-en-peru-que-pasa-en-otros-paises/
- Pandape — Oportunidades y retos de la Gig Economy en el Perú: https://www.pandape.com/blog/gig-economy/
- Revista Ideele — ¿Cómo es trabajar para una app en el Perú?: https://www.revistaideele.com/2022/09/02/plataformas-y-empleo-como-es-trabajar-para-una-app-en-el-peru/
- APESEG — Estadísticas de los seguros: https://www.apeseg.org.pe/estadisticas/

---

*Generado por el ciclo quincenal de fortalecimiento del modelo `lapuerta`.*
