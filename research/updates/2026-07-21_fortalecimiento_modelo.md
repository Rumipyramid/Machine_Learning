# Reporte quincenal — Fortalecimiento del modelo de usuarios sintéticos (seguros · Perú)

- **Fecha:** 2026-07-21
- **Próxima revisión:** 2026-08-05 (ciclo de 15 días)
- **Alcance:** evidencia nueva para **añadir/recalibrar variables** del generador
  (`research/personas/generador/` y skill `lapuerta`, v1.1) y proponer **cómo incorporarlas**.
- **Método:** búsqueda web 2025–2026 (BID/Infobae, Mivivienda/Banco Mundial, SBS, BCRP/MEF).
  Cada propuesta marca su `origen`. Se evitaron variables ya existentes o propuestas
  (v1.0/v1.1 y reportes 2026-06-21 / 2026-07-06).

---

## Resumen ejecutivo
- 💸 **Remesas estructurales:** en 2025 Perú escaló en el ranking regional de remesas (BID) — son
  ingreso estructural de millones de hogares; los receptores son foco natural de **microseguros y
  ahorro** ligados a esos flujos.
- 🏠 **Déficit habitacional ~1.9 millones** (587k cuantitativo + **1.3M cualitativo** = viviendas
  con carencias/informales). La **tenencia y formalidad de la vivienda** define quién es asegurable
  en hogar/desastres (hoy solo 3.3% de hogares con cobertura sísmica).
- 👴 **Octavo retiro AFP (2025, Ley 32445, hasta 4 UIT ≈ S/ 21,400):** erosiona el ahorro
  previsional y deja una **brecha de protección en la vejez**; señal fuerte de cortoplacismo y de
  necesidad de **seguro de vida/renta** como sustituto.

---

## Tabla de variables candidatas (nuevas)

| # | Variable | Evidencia / dato | Fuente | Cómo incorporarla | Prioridad | Origen |
|---|---|---|---|---|---|---|
| 1 | `cobertura_previsional` | 8º retiro AFP 2025 (4 UIT); informalidad ~70% sin pensión | SBS, La República | Condicional de `situacion_laboral`; `ninguna` → brecha vejez → ↑ necesidad de vida/renta | Alta | dato |
| 2 | `tenencia_vivienda` | Déficit 1.9M (1.3M cualitativo/informal) | Mivivienda, Banco Mundial | Condicional de `nse`; propietario_formal habilita hogar/desastres; informal = poco asegurable | Media-Alta | dato |
| 3 | `recibe_remesas` | Perú gran receptor en 2025 (ranking BID) | BID/Infobae, MEF | Marginal (booleano); receptor → +bancarización, leve ↑ tenencia/WTP, canal digital | Media | dato |
| 4 | `dependientes_hogar` | Núcleo de la demanda de vida/salud | (proxy ENAHO/ENDES) | {0 / 1-2 / 3+}; ↑ dependientes → ↑ intención de seguro de vida y WTP | Baja | supuesto |

---

## Detalle y propuesta de incorporación

### 1) `cobertura_previsional`  (AFP / ONP / ninguna) — **Alta**
- **Evidencia:** el 8º retiro AFP (Ley 32445, hasta **4 UIT ≈ S/ 21,400**, oct-2025) y la SBS
  adoptando medidas extraordinarias muestran un sistema previsional debilitado; con informalidad
  ~70%, gran parte de la población **no tiene pensión**.
- **Incorporación:** marginal condicionada por `situacion_laboral`:
  - `formal_dependiente` → mayoría **AFP/ONP**; `informal` → mayoría **ninguna**.
  - Efectos: `ninguna` → **brecha de protección en la vejez** → ↑ necesidad (no acción, por sesgo)
    de **seguro de vida / renta**; haber retirado AFP refuerza `sesgo_presente`. Conecta con un
    futuro producto de **ahorro-previsión voluntario**.

### 2) `tenencia_vivienda`  (propietario_formal / propietario_informal / alquila / cedida) — **Media-Alta**
- **Evidencia:** déficit habitacional **1.9M** de viviendas, de las cuales **1.3M** son déficit
  cualitativo (carencias/informalidad). Mucha propiedad **sin título formal**.
- **Incorporación:** condicional de `nse`. Efectos:
  - `propietario_formal` → base para **seguro de hogar y de desastres** → ↑ `seguro_desastres` y `wtp`.
  - `propietario_informal`/`cedida` → vivienda poco asegurable (sin título) → ↓ cobertura.
  - `alquila` → menor seguro de inmueble, posible seguro de contenido.

### 3) `recibe_remesas`  (sí / no) — **Media**
- **Evidencia:** en 2025 Perú ascendió en el ranking regional de remesas (BID); son ingreso
  estructural de millones de hogares y un canal recomendado para **microseguros y ahorro**.
- **Incorporación:** marginal booleana (calibrar con % de hogares receptores). Efectos: receptor →
  +bancarización, ingreso adicional → leve ↑ `tenencia`/`wtp`; afinidad con canal **digital/bancaseguros**.

### 4) `dependientes_hogar`  (0 / 1-2 / 3+) — **Baja**
- **Evidencia:** la presencia de dependientes es el núcleo de la demanda de **seguro de vida y de
  salud** (protección del proveedor del hogar).
- **Incorporación:** {0/1-2/3+}; ↑ dependientes → ↑ intención de vida y ↑ `wtp`. (Recalibrar con ENAHO/ENDES.)

---

## Cambios propuestos al esquema (`synthetic_user_schema.json`)

```jsonc
"cobertura_previsional": {
  "origen": "dato", "condicional_de": "situacion_laboral",
  "tabla": {
    "formal_dependiente": {"AFP": 0.6, "ONP": 0.3, "ninguna": 0.1},
    "independiente_microemprendedor": {"AFP": 0.25, "ONP": 0.1, "ninguna": 0.65},
    "informal": {"AFP": 0.1, "ONP": 0.05, "ninguna": 0.85}
  }
},
"tenencia_vivienda": { "origen": "dato", "condicional_de": "nse" },
"recibe_remesas": { "origen": "dato", "categorias": {"si": 0.12, "no": 0.88} }
```

```jsonc
// nuevos términos
"tenencia_seguro": { "drivers": {
  "cobertura_previsional": {"AFP": 0.2, "ONP": 0.0, "ninguna": -0.2},
  "recibe_remesas": {"si": 0.2, "no": 0.0}
}},
"seguro_desastres_naturales": { "ajuste_por_vivienda": {
  "propietario_formal": "x2.0", "propietario_informal": "x0.6", "alquila": "x0.4", "cedida": "x0.3"
}},
"wtp_ratio": { "ajustes": {"dependientes_3plus": "+0.08", "recibe_remesas_si": "+0.05"} }
```

> **Re-validar** tras incorporar: mantener marginales objetivo (tiene seguro ≈ 0.40,
> desconfía ≈ 0.48, desastres ≈ 0.033) y recalibrar interceptos; cuidar que `tenencia_vivienda`
> no infle el seguro de desastres por encima de ~3.3%.

---

## Cómo se incorporaría en el flujo
1. Añadir marginales/condicionales a `synthetic_user_schema.json` (en orden de dependencia:
   `cobertura_previsional` tras `situacion_laboral`; `tenencia_vivienda` tras `nse`).
2. Ampliar `generate_synthetic_users.py` y sumar términos a `tenencia`, `seguro_desastres` y `wtp`.
3. Recalibrar interceptos; re-validar marginales.
4. Actualizar codebook (`SKILL.md`), matriz y lámina.

---

## Fuentes
- Infobae / BID — Perú escala en remesas en 2025: https://www.infobae.com/peru/2025/11/26/bid-estos-son-los-paises-que-mas-remesas-recibiran-en-2025-y-peru-supera-a-la-gigante-brasil-en-que-lugar-quedo/
- MEF — Estrategia Nacional de Inclusión Financiera (remesas e inclusión): https://www.mef.gob.pe/contenidos/archivos-descarga/ENIF.pdf
- Mivivienda — Dinámica del déficit habitacional en el Perú: https://www.mivivienda.com.pe/PortalCMS/archivos/documentos/DinamicadeDeficitHabitacionalenelPeru.pdf
- Banco Mundial — La vivienda en el Perú: https://documents1.worldbank.org/curated/en/214201645586293949/pdf/Housing-in-Peru-An-Instrument-for-Inclusive-and-Resilient-Economic-Recovery.pdf
- La República — Retiro AFP 2025: SBS adopta medidas extraordinarias (8ª liberación): https://larepublica.pe/economia/2025/11/15/retiro-afp-sbs-adopta-medidas-extraordinarias-para-mitigar-impactos-de-octava-liberacion-de-fondos-hnews-320250
- Infobae — Retiro AFP 2025 (hasta 4 UIT): https://www.infobae.com/peru/2025/09/18/retiro-afp-2025-paso-a-paso-para-conocer-el-dinero-al-que-puedo-acceder-de-mi-cuenta-de-fondo-de-pensiones/

---

*Generado por el ciclo quincenal de fortalecimiento del modelo `lapuerta`.*
