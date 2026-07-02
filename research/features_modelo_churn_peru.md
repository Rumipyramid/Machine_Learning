# 🧱 Lista de features — modelo de churn/renovación Perú

> Operacionalización de la propuesta (`research/propuesta_modelo_churn_peru.md`).
> Cada feature: **variable · cálculo · fuente de dato · target al que sirve · tipo**.
> Target: **A** = lapse involuntario (impago) · **B** = baja voluntaria · **A/B** = ambos.
> Elaborado 2026-07-01.

## Convenciones
- **Fuente de dato**: sistema origen genérico (ajustar a los sistemas reales de RIMAC).
- **Ventana**: la mayoría se calcula a fecha de corte del panel (póliza × mes).
- ⚠️ = requiere control de *data leakage* (no usar información posterior al evento).

---

## 1. Señales de pago  → target **A** (crítico)

| Variable | Cálculo | Fuente | Target | Tipo |
|---|---|---|---|---|
| `metodo_pago` | Débito automático / tarjeta / manual / caja | Cobranzas / facturación | A | Categórica |
| `es_debito_automatico` | 1 si método = débito automático | Cobranzas | A | Binaria |
| `n_cobros_fallidos_3m` / `_6m` | Conteo de cobros rechazados en ventana | Cobranzas | A | Numérica |
| `dias_mora_actual` | Días desde el último vencimiento impago | Cuentas por cobrar | A | Numérica ⚠️ |
| `n_atrasos_12m` | Veces con pago fuera de fecha en 12m | Cobranzas | A | Numérica |
| `frecuencia_pago` | Mensual / trimestral / anual | Póliza | A/B | Categórica |
| `ratio_prima_ingreso` | Prima / ingreso estimado del cliente | Póliza + cliente | A | Numérica |

## 2. Precio / renovación  → target **B** (crítico)

| Variable | Cálculo | Fuente | Target | Tipo |
|---|---|---|---|---|
| `delta_prima_renovacion_pct` | (Prima nueva − prima previa) / prima previa | Suscripción | B | Numérica |
| `n_ajustes_prima_24m` | Cambios de prima en 24m | Suscripción | B | Numérica |
| `competitividad_precio` | Prima vs. referencia de mercado del ramo | Pricing / mercado | B | Numérica |
| `dias_a_renovacion` | Días hasta la fecha de renovación | Póliza | B | Numérica |

## 3. Póliza  → target **A/B**

| Variable | Cálculo | Fuente | Target | Tipo |
|---|---|---|---|---|
| `tenure_meses` | Meses desde emisión | Póliza | A/B | Numérica |
| `duracion_temprana` | 1 si tenure ≤ 24 meses | Póliza | B (vida) | Binaria |
| `ramo` | Vida / auto / hogar / salud / … | Póliza | A/B | Categórica |
| `producto` | Código de producto | Póliza | A/B | Categórica |
| `es_credito_atado` | 1 si es desgravamen / ligado a crédito | Póliza | A/B | Binaria |
| `suma_asegurada` | Monto de cobertura | Póliza | A/B | Numérica |
| `flag_post_desgravamen` | 1 si el periodo es posterior al cambio normativo | Regla temporal | A/B | Binaria |

## 4. Cliente  → target **A/B**

| Variable | Cálculo | Fuente | Target | Tipo |
|---|---|---|---|---|
| `edad` | Edad a la fecha de corte | Cliente / RENIEC | A/B | Numérica |
| `nse_apeim` | Nivel socioeconómico (proxy si falta) | Cliente / geo-APEIM | A/B | Categórica |
| `formalidad_ingreso` | Formal / informal / mixto | Cliente / scoring | A | Categórica |
| `es_bancarizado` | 1 si tiene cuenta/banca | Cliente / bureau | A | Binaria |
| `zona` / `region` | Ubicación (para macro y sismo) | Cliente | A/B | Categórica |
| `n_polizas_cliente` | Conteo de pólizas activas (bundling) | Cliente | A/B | Numérica |

## 5. Relación y servicio  → target **A/B**

| Variable | Cálculo | Fuente | Target | Tipo |
|---|---|---|---|---|
| `canal` | Broker / bancassurance / directo / digital | Comercial | A/B | Categórica |
| `tiene_broker` | 1 si intermediado por corredor | Comercial | A/B | Binaria |
| `siniestro_reciente` | 1 si hubo siniestro en 12m | Siniestros | A/B | Binaria |
| `satisfaccion_siniestro` | Resultado/satisfacción del último siniestro | Siniestros / NPS | A/B | Ordinal |
| `siniestro_rechazado` | 1 si último siniestro fue rechazado | Siniestros | A/B | Binaria ⚠️ |
| `engagement_digital` | Logins/app en ventana | Digital | A/B | Numérica |

## 6. Macro / contexto  → target **A/B (vida/salud)**

| Variable | Cálculo | Fuente | Target | Tipo |
|---|---|---|---|---|
| `desempleo_regional` | Tasa de desempleo de la región (rezago) | INEI / BCRP | A (EFH) | Numérica |
| `inflacion` | Variación de precios (rezago) | INEI / BCRP | A/B | Numérica |
| `tasa_interes` | Tasa de referencia (para IRH en vida-ahorro) | BCRP | B (vida) | Numérica |

## 7. Conductual / estructura  → target **A/B**

| Variable | Cálculo | Fuente | Target | Tipo |
|---|---|---|---|---|
| `proxy_present_bias` | Señales de cortoplacismo (p. ej. patrón de pago tardío) | Derivada | A/B | Numérica |
| `antiguedad_relacion` | Meses como cliente (no como póliza) | Cliente | A/B | Numérica |

---

## Notas de construcción

- **Target A vs. B:** definir el evento de baja y **etiquetar su causa** (impago vs.
  decisión) — es la base de los dos modelos. Sin esta etiqueta, no hay propuesta.
- **Definición del objetivo (F-1):** aislar seguro privado voluntario de crédito-atado
  y de SIS/EsSalud; el 70% en Perú confunde el concepto.
- **Leakage (⚠️):** `dias_mora_actual`, `siniestro_rechazado` y toda variable de gestión
  de cobranza deben cortarse **antes** del inicio del proceso que predice el evento.
- **NSE como feature, no como partición** (salvo prueba de heterogeneidad): el impago lo
  predicen mejor `metodo_pago` + `formalidad_ingreso` + `es_credito_atado`.
- **`flag_post_desgravamen`:** marca el *structural break*; imprescindible en series que
  cruzan el cambio normativo.

---

*Operacionalización del hilo `/seeker` sobre churn en seguros. 2026-07-01.*
