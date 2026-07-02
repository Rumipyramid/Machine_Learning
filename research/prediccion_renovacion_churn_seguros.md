# 📉 Predicción de renovación y churn en seguros — síntesis

> Informe que consolida los hallazgos sobre **qué variables predicen renovación vs.
> churn** en seguros, desagregado en cinco niveles: **transversal → ramo → región →
> Perú → NSE**. Elaborado bajo protocolo `/seeker` (2026-07-01). Fuentes en
> `research/fuentes/registro_fuentes.md` (F-35 a F-44) y en
> `research/seguros_comportamiento_mundo_peru.md`.

## Resumen ejecutivo (TL;DR)

1. **No hay un set único de predictores: el mecanismo del churn cambia por ramo.** En P&C (auto/hogar) domina el **precio en la renovación**; en salud, **premium + red/elegibilidad**; en vida no es "churn" sino **lapse** (shock financiero, tasas, duración temprana).
2. **La distinción de fondo es churn activo vs. caída involuntaria (impago).** En mercados maduros y NSE altos domina la decisión activa (shopping); en LatAm masivo domina el impago.
3. **LatAm amplifica predictores estructurales:** liquidez/informalidad, confianza y fricción de pago pesan más que en mercados maduros.
4. **En Perú casi no hay data pública de persistencia;** lo que se sabe es contexto estructural que apunta a **caída involuntaria** como mecanismo dominante en el masivo, con un quiebre reciente: el desgravamen dejó de ser obligatorio.
5. **NSE A/B (≈12% de hogares) concentran el mercado direccionable del seguro voluntario** y su churn se comporta como el de mercados maduros (activo), no como el masivo.

---

## 1. La distinción de fondo: churn activo vs. caída involuntaria

| | Churn activo | Caída involuntaria (lapse por impago) |
|---|---|---|
| Qué pasa | El cliente cotiza y decide irse | El cliente deja de pagar (no "decide") |
| Predictores | Precio, servicio, competencia, siniestro | Método de pago, atrasos, shock de liquidez |
| Intervención | Competitiva (precio, valor, experiencia) | Operativa (recuperar el pago, flexibilizar) |
| Dónde domina | Mercados maduros, NSE A/B | LatAm masivo, NSE bajos, informalidad |

> Modelar ambos como una sola cosa es el error más común: el mismo % de churn puede tener causa raíz opuesta.

---

## 2. Predictores transversales (aplican a casi todos los ramos)

Ordenados por consistencia en la evidencia:

- **Cambio de precio en la renovación (rate change)** — el más fuerte y consistente en P&C (curvas de elasticidad precio-renovación; Guelman & Guillén, 2014).
- **Antigüedad / duración (tenure)** — churn alto al inicio y decreciente; en auto, "acantilado" en 18–24 meses.
- **Número de pólizas / bundling** — multi-línea reduce churn de forma marcada.
- **Experiencia de siniestros** — un siniestro, y sobre todo su **insatisfacción/rechazo**, sube el churn.
- **Método y frecuencia de pago** — débito automático y pago anual reducen churn.
- **Canal y relación con asesor/broker** — la intermediación con asesoría retiene más.
- **Satisfacción/NPS, engagement digital, eventos de vida y cambios de elegibilidad.**
- **Edad del asegurado** (jóvenes rotan más) y scores de riesgo como proxies.

> Calibración: la mayoría de estudios ML de churn corren sobre **datos de una sola aseguradora** → validez externa limitada; la importancia relativa es contextual. Lo más robusto entre estudios: **precio y tenure**.

### Zoom: cómo predice la experiencia de siniestro (lo mejor respaldado)

El siniestro es el predictor con más matices. Lo que la evidencia de mayor rigurosidad sostiene:

1. **En promedio, tener un siniestro eleva la probabilidad de no renovar.** Documentado con regresión logística sobre datos reales de aseguradora (Guillén, Parner, Densgsoe & Pérez-Marín, 2003 — 🟢A). Mecanismo doble: la fricción del proceso y la **anticipación del aumento de prima** por experience rating/bonus-malus.
2. **El efecto es condicional, no automático.** La revisión sistemática de cancelación en no-vida (Geneva Papers, 2020 — 🟢A) muestra que la dirección y magnitud **varían según el contexto y el diseño del estudio**: el "tuvo siniestro" binario es un mal predictor aislado.
3. **Lo que de verdad dispara el churn es el *resultado* del siniestro:** rechazo, demora o mala resolución. La evidencia cuantificada aquí es de industria (Accenture: de los insatisfechos con su último siniestro, ~30% cambió de aseguradora y ~47% lo consideraba — 🟡C, encuesta propia), pero es consistente entre encuestas y con el mecanismo de confianza.
4. **Un siniestro bien resuelto puede *retener*** ("momento de la verdad"): el cliente que fue bien atendido en el momento de estrés muestra lealtad igual o mayor que quien nunca usó el seguro (evidencia de industria — 🟡C; sin cuantificación académica robusta).
5. **Efecto contagio en el hogar — el hallazgo riguroso más accionable:** con análisis de supervivencia sobre un portafolio de hogares, Brockett, Golden, Guillén, Nielsen, Parner & Pérez-Marín (2008, *Journal of Risk and Insurance* — 🟢A) muestran que **cuando un cliente cancela una póliza, la probabilidad de que cancele las demás del hogar sube fuertemente y la deserción total ocurre en una ventana corta**. Un siniestro mal manejado no arriesga una póliza: arriesga al cliente completo, y hay poco tiempo para reaccionar.

**Implicación de modelado:** no usar `siniestro_reciente` binario como única señal. Operacionalizar el **resultado** (pagado/rechazado), el **tiempo de resolución**, la **satisfacción** (si existe), el **Δprima posterior al siniestro**, y un **flag de cancelación reciente de otra póliza del mismo cliente/hogar** (señal de contagio, ventana corta). Estas variables ya están recogidas en `research/features_modelo_churn_peru.md` (grupo 5).

---

## 3. Desagregado por ramo

### 🚗 Auto (P&C personal)
El más elástico al precio y "shoppeable". **#1:** competitividad del precio / magnitud del aumento; shopping. Además: tenure (acantilado 18–24m), siniestro reciente, bundling con hogar, telemática/UBI (retiene a buenos conductores), credit score. La retención de auto personal cayó ~3.2% en 2024 (EE.UU.); el churn ya se predice a mitad de vigencia.

### 🏠 Hogar / Propiedad
**Bundling es el predictor dominante** (el hogar ancla el paquete; monoline rota más). Luego: rate change, tenure, siniestros grandes/rechazados. Prima vía escrow hipotecario → más pegajosa.

### 🏥 Salud
Mezcla decisión activa y **cambios de elegibilidad**. **Premium:** en Medicare Advantage, **+US$100/mes ≈ +33.9 pp de probabilidad de cambiar de plan** (Meyers et al., 2019). **Red** (perder prestador) y **calidad**: plan **5 estrellas ≈ −30.1 pp de desafiliación**. ~20% de la población con seguro comercial cambia de cobertura al año, sobre todo por empleo/elegibilidad. La disrupción administrativa (romper la re-inscripción automática) dispara el switching.

### 🧬 Vida
No es churn de shopping, es **lapse/surrender**:
- **Hipótesis del fondo de emergencia (EFH):** shocks de ingreso/desempleo ↑ caída. La más respaldada.
- **Hipótesis de tasa de interés (IRH):** tasas ↑ → rescatan para reinvertir (productos rate-sensitive). Evidencia mixta.
- **Hipótesis de reemplazo (PRH):** aparece un producto mejor.
- **Duración temprana** (primeros 1–2 años el lapse es mayor), **canal** (venta con asesor persiste mejor), **modo de pago**, **face amount**, **edad**, **prima/ingreso**, **tipo de producto** (term vs. permanente).

### 🏢 Comercial / B2B
**Relación con el broker es el predictor dominante.** Luego: precio y ciclo de mercado (hard vs. soft), experiencia de siniestros y servicio, cambios de riesgo, tamaño de cuenta (las grandes se re-cotizan cada renovación).

| Ramo | Predictor dominante | Otros fuertes | Naturaleza |
|---|---|---|---|
| Auto | Cambio de precio | Tenure, siniestro, bundling, telemática | Shopping activo |
| Hogar | Bundling | Rate change, tenure, siniestros grandes | Shopping / no-renovación |
| Salud | Premium + red/elegibilidad | Star rating, empleo, disrupción admin. | Decisión + elegibilidad |
| Vida | Shock financiero (EFH) / tasas (IRH) | Duración temprana, canal, accesibilidad | Lapse / surrender |
| Comercial | Relación con broker | Precio/ciclo, siniestros, tamaño | Re-cotización intermediada |

---

## 4. Desagregado por región

Las diferencias son **estructurales — de la economía, no del producto**. LatAm amplifica:

| Predictor | Mercados maduros | LatAm |
|---|---|---|
| Precio / rate change | 🔴 Dominante (auto/hogar) | 🟠 Fuerte, vía **accesibilidad** |
| Liquidez / timing de pago | 🟡 Menor | 🔴 **Dominante** (informalidad) |
| Confianza institucional | 🟡 Se da por sentada | 🔴 **Predictor activo** |
| Método de pago / bancarización | 🟠 Relevante | 🔴 **Más fuerte** (caída por impago) |
| Tasa de interés (lapse vida) | 🟠 IRH relevante | 🟡 Menor (domina EFH) |
| Shock de empleo/ingreso (EFH) | 🟡 Moderado | 🔴 **Amplificado** |
| Atadura a crédito/banco | 🟡 Parcial | 🟠 **Alta** (desgravamen, bancassurance) |

- **Liquidez e informalidad** (el amplificador #1): la restricción no es "no tienen dinero" sino no tener fondos disponibles al momento de pagar (Eling et al., 2014; CGAP). El **timing/flexibilidad del pago** es palanca de retención más potente que en mercados maduros.
- **Confianza:** en microseguros emergentes está entre los principales determinantes de dropout.
- **Macro** (inflación, FX, desempleo): eleva lapse y rescates, sobre todo en productos con ahorro (S&P, 2024).

---

## 5. Perú en detalle

> Honestidad: **no hay tasas públicas de persistencia/lapse de Perú**. Lo siguiente es contexto estructural + tu investigación base + extrapolación de mercados emergentes.

- **Fricción de pago → churn mayormente involuntario.** Solo ~38% de adultos con cuenta bancaria (Mordor; nota: Arellano reporta ~65% "bancarizado", definición más amplia) e informalidad **>73%** → el débito automático no está disponible para la mayoría → **caída por impago**, no decisión.
- **Informalidad e ingresos volátiles → EFH amplificada.**
- **Quiebre regulatorio:** el **desgravamen dejó de ser obligatorio** en casi todos los créditos (salvo hipotecas). Como mucha "tenencia" era crédito-atada, esto vuelve real la decisión de opt-out → tratar como *structural break* en cualquier serie.
- **Desconfianza (~48%)** con la falta de información como causa #1; la confianza **sube con el broker** → canal como predictor de retención.
- **Confusión conceptual:** 70% asocia "seguros" con salud pública (SIS/EsSalud) → contamina la variable objetivo.
- **Sesgos:** present bias e inercia; la inercia retiene al inscrito pero produce la caída silenciosa por impago (doble filo).
- **Asequibilidad:** penetración ~2.08% del PBI, WTP ≈ 2/3 del precio justo.
- **Mezcla de producto:** obligatorios (SOAT 94% conocido, Vida Ley) vs. voluntarios (~23% vehicular voluntario).

---

## 6. NSE A y B en Perú

- **Tamaño:** nacional NSE **A 1.2% + B 10.6% ≈ 12%** de hogares (APEIM 2024); mucho mayor en Lima. Ingreso **AB ≈ S/ 8,117/mes** vs. nacional S/ 3,348.
- **Son el mercado direccionable del seguro voluntario** (Vida Individual, salud privada, vehicular voluntario): ingreso, bancarización casi universal, formalidad.
- **Su churn es activo, no pasivo:** con autopay disponible y sin restricción de liquidez, **no caen por impago** — deciden. Predictores tipo mercado maduro: **precio/competitividad de renovación, servicio y siniestro, bundling, relación con asesor**.
- **Palanca de retención distinta al masivo:** valor percibido, experiencia y precio (no "asegurar el pago").
- **Menos confusión SIS/EsSalud** (más propensos a EPS/privado) → variable objetivo más limpia.
- Coincide con el segmento del **perfilador / modelo de venta** ("creación de patrimonio"): A/B y C1 alto.

> ⚠️ APEIM reporta "AB" agrupado (el A gana bastante más que el B) y clasifica por gasto, no por riqueza líquida; sesgo urbano/Lima. Separar A de B si el modelo lo permite.

---

## 7. Implicaciones para el modelado (accionable)

1. **Separa dos modelos/targets:** *caída involuntaria (impago)* vs. *churn activo*. En Perú masivo domina el primero; en A/B el segundo.
2. **Señales de impago** (método de pago, atrasos, fallos de cobro) para el involuntario; **precio/servicio/shopping** para el activo.
3. **Define bien el target** (evita confusión SIS/EsSalud/crédito-atado).
4. **Canal/broker como feature de retención**, no solo de adquisición.
5. **Marca el corte del desgravamen** como variable estructural.
6. **Ajusta por ramo:** un modelo por ramo (o interacciones fuertes), no uno global.
7. **Métricas:** con churn desbalanceado, mirar recall/AUC, no accuracy.
8. **Palanca #1 en el masivo peruano no es el precio: es facilitar y asegurar el pago.**

### Tabla maestra de predictores

| Predictor | Aplica a | Fuerza | ¿Accionable? |
|---|---|---|---|
| Cambio de precio renovación | Auto, hogar, salud, comercial | 🔴 Alta | Parcial (tiene costo) |
| Método/timing de pago | Todos (crítico LatAm) | 🔴 Alta (involuntario) | ✅ Sí |
| Tenure / duración temprana | Todos | 🔴 Alta | ❌ No (pero segmentable) |
| Bundling / n° pólizas | Auto, hogar | 🔴 Alta | ✅ Sí (cross-sell) |
| Siniestro (y satisfacción) | Todos | 🟠 Media-alta | ✅ Sí (experiencia) |
| Canal / relación broker | Todos (fuerte en Perú) | 🟠 Media-alta | ✅ Sí |
| Shock ingreso/empleo (EFH) | Vida, salud (LatAm) | 🟠 Media | ❌ No (mitigable con flexibilidad) |
| Confianza / información | Todos (fuerte en Perú) | 🟠 Media | ✅ Sí |
| Tasa de interés (IRH) | Vida ahorro | 🟡 Baja-media | ❌ No |
| Red/elegibilidad | Salud | 🔴 Alta | Parcial |

---

## 8. Nota de rigor (limitaciones)

- **Effect sizes de salud** (+33.9pp, −30.1pp) son de contextos US (Medicare Advantage) — **no trasladar directo a Perú**; sirven como dirección/magnitud relativa.
- **Estudios ML de churn** reportan accuracy alta (90%+) sobre datos de una aseguradora, con **desbalance de clases** que la infla — mirar recall/AUC. Correlación, no causalidad.
- **Hipótesis de lapse en vida** (EFH/IRH/PRH): soporte **mixto** según mercado/período; EFH la más consistente.
- **Perú:** sin tasas públicas de persistencia; inferencias estructurales, no coeficientes medidos. La data real la tiene RIMAC/SBS.
- **Cifras de mercado** (2.08%, 48%, 38%/65% bancarización, 73% informalidad, APEIM) de reguladores/gremios/consultoras — verificar contra el original antes de citar.
- **NSE "AB" agrupado** y basado en gasto: aproximación, no renta líquida.

---

*Síntesis del hilo de investigación `/seeker` sobre churn en seguros. 2026-07-01.*
