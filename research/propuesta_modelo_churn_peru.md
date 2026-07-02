# 🤖 Propuesta de modelo — churn y renovación de seguros en Perú

> Propuesta técnica de modelado, apoyada **solo en la evidencia de mayor rigurosidad**
> (fuentes 🟢 A y 🔵 B del ledger). Desagrega por NSE / perfil **únicamente donde el
> mecanismo de churn cambia**, siguiendo un principio de parsimonia. Consolida el hilo
> `/seeker` (ver `research/prediccion_renovacion_churn_seguros.md`). Elaborado 2026-07-01.

## Principio rector: parsimonia con base en el mecanismo

No se segmenta por etiqueta (NSE) porque sí. Se segmenta **solo cuando el proceso
generador del dato difiere**. La evidencia de alta rigurosidad muestra que en Perú/
LatAm hay **un corte de mecanismo real** —caída involuntaria por impago vs. decisión
activa— que sí justifica separar; la mayoría de las demás distinciones se capturan
mejor con **features e interacciones**, no con modelos separados.

> Regla operativa: **desagregar un modelo solo si una prueba de heterogeneidad muestra
> que un modelo único con interacciones no captura la diferencia.** (Ver §7.)

---

## 1. La decisión de diseño #1 — ¿qué es "churn" en Perú?

"Churn" no es un solo evento. La evidencia de mayor rigurosidad obliga a **dos targets
distintos**, porque tienen causa, predictores e intervención diferentes:

| Target | Qué es | Por qué separado (evidencia 🟢/🔵) |
|---|---|---|
| **A. Lapse involuntario** | La póliza cae por **impago** (cobro fallido / no pago), sin decisión activa | En mercados emergentes la restricción de **liquidez** es determinante de dropout (Eling et al., 2014 — F-39); informalidad e ingreso volátil → shock de ingreso (EFH: Outreville, 1990 — F-38) |
| **B. No-renovación / rescate voluntario** | El cliente **decide** no renovar o rescatar | Gobernado por **precio en la renovación** (Guelman & Guillén, 2014 — F-35) y, en vida, por tasas/reemplazo (lapse Lasso, 2022 — F-37) |

**Esto no es opcional:** modelar A y B como un solo evento mezcla dos procesos y hace
al modelo inaccionable (la intervención de A es operativa; la de B, comercial).

---

## 2. Arquitectura propuesta

```
                        ┌─────────────────────────────┐
                        │  Evento de baja de póliza    │
                        └──────────────┬──────────────┘
                          ┌────────────┴────────────┐
                          ▼                          ▼
                 A. Lapse involuntario       B. Baja voluntaria
                 (predice impago)            (predice no-renovación/rescate)
                          │                          │
          ┌───────────────┼──────────┐     ┌─────────┼──────────┐
          ▼               ▼          ▼     ▼         ▼          ▼
        Vida            Auto       Salud  Vida      Auto       Salud
```

- **Corte primario: tipo de evento (A vs. B).** Justificado por mecanismo (arriba).
- **Corte secundario: ramo.** La economía del producto difiere (auto elástico al
  precio; vida gobernada por duración/EFH; salud por red/elegibilidad). Se implementa
  como **modelos por ramo** o un modelo con **fuertes interacciones ramo × feature**;
  decidir con datos (§7).
- **NSE / perfil: como feature, no como modelo separado** — salvo que la prueba de
  heterogeneidad lo exija (§6).

---

## 3. Unidad de análisis y horizonte

- **Unidad:** póliza × ventana temporal (panel mensual). Permite capturar dinámica de
  pago y cambios de estado.
- **Enfoque dual:**
  - **Supervivencia (time-to-event):** modela el *tiempo hasta* la baja — natural para
    el efecto de **tenure/duración temprana** (lapse más alto en los primeros 1–2 años;
    F-37) y para censura.
  - **Clasificación en ventana:** probabilidad de baja en los próximos *k* meses (p. ej.
    60–90 días pre-renovación para B; horizonte corto rodante para A) — para accionar.
- Recomendación: **modelo de supervivencia** (Cox con regularización / survival GBM)
  como base + **clasificador de ventana** (gradient boosting) para operación.

---

## 4. Features — solo señales de alta rigurosidad

Agrupadas y marcadas según a qué target sirven (A = involuntario, B = voluntario).

| Grupo | Features | Sirve a | Respaldo |
|---|---|---|---|
| **Pago** | Método (débito automático vs. manual), frecuencia, atrasos previos, cobros fallidos, días de mora | **A** (crítico) | Eling 2014 (F-39); liquidez/timing |
| **Precio/renovación** | Cambio de prima en renovación (Δ%), competitividad, historial de ajustes | **B** (crítico) | Guelman & Guillén 2014 (F-35) |
| **Póliza** | Tenure/duración, ramo, producto, **crédito-atado (desgravamen)**, suma asegurada, modo de pago de la prima | A y B | Lapse Lasso 2022 (F-37) |
| **Cliente** | Edad, NSE/APEIM (proxy), formalidad del ingreso, bancarización, zona | A y B | APEIM 2024 (F-41); SBS 2023 (F-1) |
| **Relación** | Canal (**broker vs. directo**), siniestro reciente y su resolución/satisfacción, engagement | A y B | SBS 2023 (F-1): confianza sube con broker |
| **Macro** | Desempleo/inflación regional (para EFH en vida) | A y B (vida) | Outreville 1990 (F-38); S&P 2024 (F-40) |
| **Sesgo/estructura** | Present bias/inercia (proxies conductuales), **flag structural break desgravamen** | A y B | Platteau et al. 2021 (F-3) |

> **Definición del target — cuidado (F-1):** el 70% en Perú confunde "seguro" con
> SIS/EsSalud. La variable objetivo debe aislar **seguro privado voluntario** vs.
> **crédito-atado** vs. **público**. Un target mal definido invalida todo el modelo.

---

## 5. Cómo entra NSE / perfil (y por qué no como modelo separado por defecto)

La evidencia de alta rigurosidad **no da coeficientes de churn por NSE en Perú** — no
existen públicos. Lo que sí está fundamentado es que **el peso del mecanismo cambia**:

- **NSE bajo / informal / pago manual / crédito-atado →** domina el **lapse
  involuntario** (liquidez; F-39, F-38).
- **NSE A/B / formal / débito automático →** domina la **baja voluntaria** (precio/
  servicio; F-35), como en mercados maduros (APEIM 2024 confirma bancarización casi
  universal en A/B — F-41).

**Implicación de diseño (clave para "solo si es necesario"):** ese corte se captura
mejor con **variables operativas observables** (método de pago, formalidad, producto
crédito-atado) que con la **etiqueta NSE**. El perfil de riesgo de impago **es** el
método de pago + formalidad, no el NSE per se. Por eso:

1. NSE entra como **feature** (y como proxy de las anteriores cuando falten).
2. El **perfil operativo** ("pago automático + formal" vs. "pago manual + informal")
   es el segmentador más accionable, y ya está implícito en el corte A/B.
3. **Modelos separados por NSE solo si** la prueba de heterogeneidad (§7) lo justifica.

---

## 6. Cuándo desagregar (regla explícita)

Desagregar (entrenar modelos separados) **solo si** se cumple:

- El **tamaño de muestra** por segmento es suficiente (no sacrificar potencia), **y**
- Una prueba de **heterogeneidad de efectos** (interacciones significativas, o mejora
  de PR-AUC out-of-time del modelo segmentado vs. el único con interacciones) es
  material.

Si no → **un modelo con interacciones** (segmento × features). Esto evita la
proliferación de modelos frágiles y honra la parsimonia. El corte **A vs. B** y
**por ramo** casi seguro lo justifican; **por NSE**, probablemente no (mejor como
feature) — validar.

---

## 7. Método y algoritmos

- **Base interpretable:** Cox regularizado (elastic net) / regresión logística con
  regularización → transparencia y coeficientes.
- **Producción:** **gradient boosting** (XGBoost/LightGBM) o survival GBM →
  rendimiento y no-linealidades.
- **Desbalance** (el churn es raro): **class weights / focal loss**, y evaluar con
  **PR-AUC**, no accuracy (ver §8).
- **Explicabilidad:** SHAP para traducir score → causa → acción.
- **Heterogeneidad:** interacciones explícitas + validación segmentada (§6).

---

## 8. Métricas de evaluación

- **PR-AUC / recall @ top-decil** (no accuracy — con clases desbalanceadas la accuracy
  engaña; ver nota de rigor).
- **AUC-ROC** como secundaria.
- **Calibración** (curva de calibración / Brier) — crítica si el score alimenta
  decisiones de precio.
- **Lift por decil** — cuánta baja concentra el top del score (para priorizar acción).
- **Métricas de negocio:** caja/prima retenida, no solo métricas estadísticas.

---

## 9. Del score a la acción (dos rutas, según target)

| Target | Intervención | Lógica |
|---|---|---|
| **A. Lapse involuntario** | **Operativa**: migrar a débito automático, ajustar fecha de cobro a liquidez, recordatorios, recuperación de cobro fallido | La palanca #1 del masivo peruano **no es el precio, es asegurar el pago** (F-39) |
| **B. Baja voluntaria** | **Comercial**: retención por valor/precio, contacto pre-renovación, refuerzo del broker, mejora de experiencia de siniestro | Precio y servicio gobiernan la decisión (F-35, F-1) |

- **Uplift modeling** (no solo propensión): actuar sobre quienes la intervención
  *cambia*, no sobre quienes caerían/renovarían igual. Evita gastar retención en
  falsos positivos.

---

## 10. Riesgos, sesgos y validación

- **Fairness / discriminación:** NSE y proxies de crédito pueden inducir sesgo; auditar
  y cumplir normativa SBS. Evitar penalizar por condición socioeconómica.
- **Data leakage:** no usar variables posteriores al evento (p. ej. gestión de
  cobranza ya iniciada).
- **Structural break del desgravamen (F-44):** la serie histórica cruza el cambio
  normativo → segmentar antes/después o incluir el flag; no entrenar a ciegas sobre la
  transición.
- **Validación out-of-time** (no solo out-of-sample) — el churn es sensible al ciclo
  macro (F-40).
- **Definición del target** (F-1): revalidar que no mezcla SIS/EsSalud/crédito-atado.

---

## 11. Roadmap por fases

1. **Fase 0 — Datos y target.** Definir con precisión los dos eventos (A/B), armar el
   panel póliza×mes, marcar el structural break, auditar calidad del target.
2. **Fase 1 — MVP por target × ramo prioritario.** Base interpretable + GBM; PR-AUC,
   calibración, SHAP. Empezar por el ramo/segmento de mayor prima en riesgo.
3. **Fase 2 — Heterogeneidad.** Probar si desagregar por NSE/perfil aporta sobre
   interacciones; decidir con datos (§6).
4. **Fase 3 — Uplift + operación.** Pasar de propensión a uplift; conectar score →
   intervención (A operativa, B comercial); medir caja/prima retenida.
5. **Fase 4 — Monitoreo.** Drift, recalibración, y re-evaluación del structural break.

---

## 12. Nota de rigor

- **Solo se usó evidencia 🟢 A / 🔵 B** para las decisiones de diseño: Eling 2014
  (F-39), Outreville 1990 (F-38), Guelman & Guillén 2014 (F-35), lapse Lasso 2022
  (F-37), SBS 2023 (F-1), APEIM 2024 (F-41), S&P 2024 (F-40), Platteau et al. 2021
  (F-3). Los datos de menor rigurosidad (Mordor 🟡C — F-43; Arellano 🟠D — F-42;
  prensa desgravamen 🟠D — F-44) se usan **solo como contexto direccional**, no para
  fundamentar el diseño.
- **No hay coeficientes de churn medidos en Perú:** la arquitectura se justifica por
  **mecanismo**, no por effect sizes locales. Los pesos reales salen de la data de
  RIMAC al entrenar.
- **Effect sizes foráneos** (p. ej. Meyers 2019 en salud US — F-36) **no se trasladan**
  como parámetros; se usan solo para justificar *qué variables incluir*.
- La recomendación de **no desagregar por NSE por defecto** es una decisión de
  parsimonia: sujeta a la prueba de heterogeneidad con datos reales (§6).

---

*Propuesta de modelado del hilo `/seeker` sobre churn en seguros. 2026-07-01.
Datos de entrenamiento requeridos: panel de pólizas RIMAC con estados de pago,
renovaciones, siniestros, canal y atributos de cliente.*
