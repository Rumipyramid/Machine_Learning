# Matriz de variables para usuarios sintéticos — consumidores de seguros (Perú)

> Deriva de `research/seguros_comportamiento_mundo_peru.md`.
> Esquema machine-readable: `synthetic_user_schema.json` · Generador: `generate_synthetic_users.py`
> Fecha: 2026-06-21

Esta matriz convierte los hallazgos de la investigación en **variables, categorías y
distribuciones de probabilidad** para muestrear perfiles sintéticos de consumidores de seguros
peruanos. Cada celda marca su **origen**: `dato` (anclado en fuente citada) o `supuesto`
(estimación ilustrativa, ajustable).

---

## 1. Variables independientes (marginales)

| Variable | Categorías (probabilidad) | Origen |
|---|---|---|
| **generacion** | Gen Z 18-27 (0.22) · Millennial 28-43 (0.33) · Gen X 44-59 (0.25) · Boomer 60+ (0.20) | supuesto |
| **nse** (APEIM) | A (0.02) · B (0.11) · C (0.27) · D (0.26) · E (0.34) | supuesto |
| **region** | Lima Metro (0.33) · Resto Costa (0.25) · Sierra (0.30) · Selva (0.12) | supuesto |
| **educacion_financiera** | baja (0.50) · media (0.35) · alta (0.15) | supuesto* |
| **sesgo_presente** | alto (0.45) · medio (0.35) · bajo (0.20) | dato (predictor negativo de tenencia) |
| **canal_preferido** | directo/digital (0.35) · bancaseguros (0.30) · broker (0.25) · ninguno (0.10) | supuesto |

\* Consistente con la baja penetración y la confusión entre "seguro" y salud pública (SIS/EsSalud).

## 2. Variables condicionales

| Variable | Depende de | Lógica | Origen |
|---|---|---|---|
| **exposicion_riesgo_sismico** | region | Lima/Costa → mayoritariamente alta; Sierra/Selva → media/baja | dato (Perú sísmico) |
| **apertura_datos_ia** | generacion | Gen Z muy alta → Boomer baja | dato (Gen Z 87% confía en IA vs 75% Boomers) |
| **situacion_laboral** | nse | NSE alto → más formal_dependiente; NSE bajo → más informal | dato/supuesto (informalidad ~70%) |
| **cobertura_previsional** | situacion_laboral | formal → AFP/ONP; informal → ninguna (~60% sin pensión) | dato (8º retiro AFP 2025) |
| **tenencia_vehiculo** | region | Lima → más auto; Sierra/Selva → más moto/mototaxi; ~52% ninguno | dato (2/10 con seguro; 4/5 motos sin SOAT) |
| **acceso_digital** | region+nse+generacion | score → {alta/media/baja}; urbano/NSE alto/joven ↑ | dato (bancarización 59%; Yape/Plin) |
| **bancarizado** | nse+region+acceso_digital | prob. logística; marginal ≈ 0.59 | dato (~59% adultos en sist. financiero) |

> **v1.2 (2026-07-21):** se añadió `cobertura_previsional` (AFP/ONP/ninguna), driver de `tenencia_seguro`.
>
> **v1.1 (2026-07-06):** se añadieron `situacion_laboral`, `tenencia_vehiculo`, `acceso_digital` y
> `bancarizado` (reportes quincenales). Entran como drivers de `tenencia_seguro`
> (formal_dependiente +, bancarizado +, auto +, moto/informal −) y el split voluntario/obligatorio
> se inclina a obligatorio para formales (Vida Ley) y autos (SOAT). Marginales validadas tras la
> recalibración: any-seguro ≈ 0.41, desconfía ≈ 0.45, desastres ≈ 0.035, bancarizado ≈ 0.60.

## 3. Variables derivadas (modeladas)

| Variable | Modelo | Marginal objetivo | Origen |
|---|---|---|---|
| **confianza_aseguradora** | marginal + ajuste por canal (broker ↑ confianza) | desconfía 0.48 · neutral 0.29 · confía 0.23 | dato (SBS/APESEG) |
| **tenencia_seguro** | score logístico: NSE + edu. financiera + sesgo presente (−) + confianza | any-insurance ≈ 0.40 | dato (SBS ~4/10) |
| **seguro_desastres_naturales** | base 3.3% × NSE × exposición × tenencia | ≈ 0.033 | dato (APESEG) |
| **wtp_ratio** | gaussiana: no asegurado μ≈0.66 · asegurado μ≈1.05 | — | dato (literatura WTP) |

---

## 4. Relaciones / dependencias clave (resumen del grafo causal)

```
region ───────────────▶ exposicion_riesgo_sismico ─┐
generacion ───────────▶ apertura_datos_ia          │
canal_preferido ──────▶ confianza_aseguradora ──┐   │
nse ─────────────────┐                          │   │
educacion_financiera ┼─▶ tenencia_seguro ◀───────┘   │
sesgo_presente ──────┘          │                     │
                                ▼                     ▼
                     seguro_desastres_naturales ◀─────┘
                                │
                                ▼
                            wtp_ratio  (◀ tenencia)
```

Insights codificados:
- **El broker eleva la confianza** (intermediación) → +15 pp hacia "confía plena".
- **Sesgo del presente** reduce la tenencia (procrastinación: "lo contrato después").
- **NSE y educación financiera** son los principales empujes positivos de tenencia.
- **El seguro contra desastres es marginal** (~3.3%) incluso con alta exposición sísmica.
- **Los no asegurados subvaloran el riesgo**: WTP ≈ 2/3 del precio justo.

---

## 5. Cómo generar usuarios

```bash
# 5 perfiles en consola
python research/personas/generador/generate_synthetic_users.py --n 5 --seed 42

# 1000 perfiles a CSV reproducible
python research/personas/generador/generate_synthetic_users.py --n 1000 --out usuarios.csv --seed 42
```

Salida (columnas): `id, generacion, nse, region, educacion_financiera, sesgo_presente,
canal_preferido, situacion_laboral, cobertura_previsional, tenencia_vehiculo, acceso_digital,
bancarizado, exposicion_riesgo_sismico, apertura_datos_ia, confianza_aseguradora,
tenencia_seguro, seguro_desastres_naturales, wtp_ratio`.

Datasets generados en `datasets/`:
- `datasets/usuarios_sinteticos_ejemplo.csv` — 200 filas (ejemplo de referencia del generador).
- `datasets/muestra_22_usuarios.csv` — 22 filas (simulación de pregunta abierta).
- `datasets/grupo_nse_A.csv` — 10 filas (grupo NSE A, simulación de opinión RIMAC).

---

## 6. Perfiles arquetípicos (personas) derivados de la matriz

Tres arquetipos frecuentes que emergen de las distribuciones, útiles como anclas narrativas:

### 🟥 "El postergador desconfiado" (segmento mayoritario)
NSE D/E · educación financiera baja · **sesgo presente alto** · **desconfía** · canal directo/digital
o ninguno · **sin seguro** · WTP ≈ 0.6. *Barrera: precio + falta de información + procrastinación.*

### 🟨 "El protegido por obligación"
NSE C · educación media · canal bancaseguros · confianza neutral · **solo seguro obligatorio**
(SOAT / Vida Ley) · alta exposición sísmica pero **sin cobertura de desastres**. *Oportunidad de
upsell informado.*

### 🟩 "El asegurado confiado vía broker"
NSE A/B · educación financiera alta · **sesgo presente bajo** · canal **broker** · **confía plena**
· **seguro voluntario** (y a veces desastres) · WTP ≥ 1.0. *Segmento premium, fideliza con
servicio y claims ágiles.*

---

## 7. Advertencias de uso

- Varias marginales son **supuestos ilustrativos**; recalibrar con micro-datos reales (ENAHO,
  encuestas SBS, datos propios de la aseguradora) antes de usar en decisiones.
- Los **sesgos** de la matriz reflejan los de las fuentes (urbano-céntricas, 2023-2025).
- Datos sintéticos = **no representan personas reales**; aptos para prototipado, prueba de
  pipelines, balanceo de clases y simulación, no para inferencia causal.
