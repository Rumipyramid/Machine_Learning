# Recurrencia en apps de inversión: qué la produce y qué solo parece producirla

> Documento de investigación. Fuente persistente y versionada en el repositorio.
> Fecha de elaboración: 2026-11-01 · Última actualización: 2026-11-01 · Versión: **v1.0**
> Origen: `/trinidad` (pista empírica + social + negocio), rol *behavioral designer researcher*.
> Fuentes en `research/fuentes/codice.md`: **F-847 a F-873** (empírica F-847 a F-855 · social F-856 a F-859 · negocio F-860 a F-873).
> Pregunta permanente: **¿qué hace que una persona vuelva a aportar a una inversión (y no solo a abrir la app), y qué evidencia independiente lo respalda?**
> ⚠️ **Decisión que alimenta: no definida.** Se asumió benchmarking para el diseño de recurrencia en inversión y seguros de vida con ahorro. Si hay decisión concreta, volver a §6.

---

## 0. 🎯 Alcance y cómo se leyó la evidencia

- **"Recurrencia" tiene tres significados y se confunden.** (a) *Visita*: abrir la app. (b) *Operación*: comprar y vender seguido. (c) *Aporte*: poner dinero de forma periódica. Un seguro de vida con ahorro depende de (c). Casi toda la evidencia sobre "engagement" mide (a) o (b).
- **Cobertura.** Perú: Trii, Tyba, Hapi (se asumió que "Happ" es Hapi), apps de BCP, BBVA e Interbank, fondos mutuos. Mundo: Robinhood, Nubank, Revolut, Acorns, Betterment, Vitality. Quedaron **sin datos útiles**: Vanguard, Fidelity, AFP, bancos globales distintos de Nubank y Revolut.
- **Herramienta de lectura:** solo resúmenes de búsqueda, con resultados centrados en EE.UU. No se abrió ningún artículo ni filing completo. Las atribuciones dudosas están marcadas en el ledger.

## 1. ⚖️ Resumen ejecutivo

1. **No hay ningún dato público de retención ni de aporte sostenido para las apps peruanas.** Ni Trii, ni Tyba, ni Hapi, ni los bancos lo publican. Todo lo que circula es tamaño (usuarios, montos) y es de la propia empresa (F-862 a F-865, F-867).
2. **La evidencia causal más sólida favorece la automatización, no el juego.** Inscripción automática y ahorro con compromiso mueven aportes en estudios con revisión de pares (F-850, F-853). El juego y las alertas mueven más bien la *frecuencia de operación*, con efecto pequeño y daño probable (F-847, F-848).
3. **Esa evidencia viene de pensiones en EE.UU. y de un banco filipino.** No se probó en apps de inversión de LatAm. Además, una revisión oficial califica de baja la evidencia causal de los defaults (F-852).
4. **Más actividad en la app no equivale a más valor.** Robinhood perdió 13% de usuarios activos mensuales mientras subían activos e ingreso por usuario (F-860). Y un experimento con >50.000 clientes subió el compromiso 23% sin mover la inversión real (F-854, de autores y revista no verificados).
5. **En Perú el mercado crece (490.012 partícipes, +17% en 2025, F-866), pero el crecimiento es de acceso, no de recurrencia demostrada.** Las apps abren la puerta (montos mínimos desde S/ 20); lo que se hace después no se mide en público.

## 2. 🔬 Pista empírica/teórica (rigor académico)

### 2.1 Lo que sí tiene respaldo causal: automatizar y comprometer
| Mecanismo | Resultado | Fuente | Límite principal |
|---|---|---|---|
| Inscripción automática (default) | Participación ~20% → ~90% de inmediato, >98% a 36 meses | F-850 (🟢A) | Una empresa; muchos se quedan en la tasa baja por defecto |
| Aporte que sube con cada aumento de sueldo | Mecanismo propuesto y probado en pocas empresas | F-851 (🟢A, leído vía espejos) | Cifras sin verificar en el original |
| Cuenta de ahorro con compromiso | Toma 28%; saldo +42% a 6 meses, +82% a 1 año | F-853 (🟢A, aleatorizado) | Un banco en Filipinas; solo 28% la toma |
| Revisión de la calidad de la evidencia | Baja evidencia causal; casi sin datos de ahorro total | F-852 (🔵B) | Revisión de agencia, 2016 |

**Interpretación (inferencia mía, no hallazgo):** quien se queda en el default no necesariamente "recurre"; solo no se va. Para un producto de inversión eso puede ser retención real, o puede ser inercia que se rompe al primer sobresalto.

### 2.2 Juego, notificaciones y atención: suben la operación, no la calidad
- Los usuarios de Robinhood operan más sobre lo que capta atención; sus compras masivas predijeron retornos bajos (F-847, 🟢A).
- En un experimento aleatorizado, la gamificación hedónica subió el volumen ~5%. Del contraste entre plataformas, ~70% es autoselección y ~30% efecto del juego. Atrae más a quien sabe menos (F-848, 🟢A, plataforma simulada).
- Un ensayo del regulador de Ontario (2.430 personas) vio lo mismo con puntos de valor casi nulo (F-849, 🔵B).
- **Límite que aplica a las tres:** todas miden *operar más*. Ninguna mide *aportar de forma sostenida*, que es lo que importa en vida con ahorro.

### 2.3 Normas sociales y pares: atención sin acción
- La información de pares subió el compromiso inicial 23% sin efecto detectable en la inversión (F-854, 🟡C).
- Mostrar el ahorro de compañeros elevó la intención y algunos pasos en un banco holandés (F-855, 🟡C).
- Ambos son de revista y autores sin verificar; tomarlos como **señal exploratoria**.

### 2.4 Contraevidencia buscada
No encontré ningún experimento de campo que muestre que **metas, rachas o notificaciones** aumenten el aporte sostenido en una app de inversión. La búsqueda dio cero resultados directos; es un vacío, no una refutación.

## 3. 📱 Pista social/mediática

**Nivel de instalación social: 🧊 en Perú, 🌡️ en EE.UU. (solo por el caso Robinhood).** La búsqueda no devolvió hilos de Reddit ni de X sobre Trii, Tyba o Hapi (la herramienta ve sobre todo resultados de EE.UU.), así que **no puedo decir qué opina la gente de esas apps**.

- **EE.UU.:** el caso de mayor ruido es el de Robinhood. En 2024 pagó US$7,5M a Massachusetts y dejó el confeti por frecuencia de operación, las notificaciones a listas "más populares" y rasgos de juego de azar (F-856, 🟡C). Robinhood niega que su app sea gamificada. Es un acuerdo, no una sentencia.
- **Perú:** reseñas de blogs describen funciones, sin quejas ni sentimiento medido (F-857, 🟠D). Una encuesta de Tyba dice que 44% usa redes como principal fuente de educación financiera (F-858, 🟡C, encargada por quien vende) y Andina recoge opiniones de economistas: apps y redes explicarían la entrada de jóvenes (F-859, 🟠D).
- **Validación vs. amplificación:** lo de Perú es amplificación de notas de prensa y de empresa; no hay validación de usuarios.

## 4. 📈 Pista de negocio

**Tipo de evidencia:** filings (F-860, F-861), prensa con cifras corporativas (F-862, F-864, F-867), páginas de producto (F-865, F-872), cifras oficiales por prensa (F-866). **Ninguna da retención ni aporte sostenido.**

| Caso | Qué reporta | Qué NO reporta |
|---|---|---|
| **Robinhood** (F-860) | 27,0M de clientes con fondos; 4,18M en Gold (~15,5%); activos mensuales 13,0M vs 14,9M; ingreso por usuario US$171 | Retención por cohorte |
| **Nubank** (F-861) | 36,2M clientes activos en inversión (2T 2025); actividad mensual 83% | Recurrencia de aporte; Cajitas |
| **Revolut** (F-871) | Aporte recurrente promedio ~€47/mes en Rumania | Cuántos mantienen el plan |
| **Acorns** (F-868) | >50% usaba inversión recurrente (2017, dicho por un ejecutivo) | Denominador, período, churn |
| **Betterment** (F-869) | Precio más bajo si aporta ≥US$200/mes o tiene ≥US$24.000 | Efecto en retención |
| **Vitality** (F-870, y F-25, F-638 ya en el códice) | Caducidad de pólizas 15% a 47% menor (internas) | Control de selección |
| **Trii Perú** (F-862, F-863) | ~50% de operaciones de la BVL; 95% de cuentas nuevas 2024; usuarios 600.000 a 1M según fuente | Usuarios que siguen operando |
| **Tyba Perú** (F-864, F-865) | 216.000 usuarios y S/ 131M (fin 2023); aporte automático desde S/ 20 | Cuántos lo activan y lo mantienen |
| **Hapi** (F-867) | Medio millón de clientes (región), US$4,3M levantados | Retención; cifras 2026 |
| **BCP, BBVA, Interbank** (F-872) | Mínimos S/ 20, S/ 100; BBVA con suscripción programada; Interbank exige perfilamiento | Uso real |
| **Mercado peruano** (F-866) | 490.012 partícipes, +17,39%; patrimonio +21,77% | Corte por edad o canal |

**Cálculo propio (inferencia):** S/ 131M ÷ 216.000 usuarios ≈ **S/ 600 por usuario** en Tyba a fines de 2023. Es un promedio que mezcla inscritos y activos; sugiere tickets pequeños, no recurrencia.

**Comparabilidad:** baja. Cada empresa define "usuario activo" distinto, las fechas van de 2017 a 2026 y las cifras de Trii se contradicen entre fuentes.

## 5. ⚖️ Síntesis (sin mezclar los criterios de validez)

- **Convergencia débil:** las tres pistas apuntan a que **abrir la puerta es fácil (apps, montos desde S/ 20) y lo difícil, y no medido, es el segundo y tercer aporte.** Empírica y negocio coinciden en que lo único con respaldo para sostener aportes es la **automatización con compromiso**; negocio la ofrece (Tyba, BBVA, Betterment) sin publicar si funciona.
- **Divergencia:** la **gamificación** es lo que más usa y celebra el negocio (confeti, rachas, Gold), y es lo que menos respaldo tiene como motor de aporte; lo que sí demuestra la evidencia es que sube operación y atrae a quien sabe menos. La pista social en EE.UU. la trata como problema regulatorio.
- **Explicaciones alternativas al crecimiento peruano** (no descartadas): mayor acceso por las apps, contenido en redes, rendimientos de fondos mutuos que superaron al plazo fijo en 2024 (titular de Andina, no revisado) y distribución vía banco (BCP→Tyba, alianza con Yape). Ninguna prueba recurrencia.
- **Seguros de vida con ahorro:** la caducidad menor de Vitality es la única cifra de persistencia que encontré, y es interna y con selección probable (F-870). Perú tiene norma de transparencia (F-873) pero no publica persistencia.

## 6. 🧪 Hipótesis para testear (no son hallazgos)

1. **Aporte automático atado a un evento de ingreso** (sueldo, gratificación, CTS): ¿sube el aporte sostenido a 6 y 12 meses frente a un recordatorio? Respaldo indirecto en F-850, F-851; no probado en Perú.
2. **Compromiso con meta bloqueada** (tipo F-853) en un producto peruano: ¿qué fracción lo elige y cuánto dura? Probar con gente de bajo y alto sesgo del presente.
3. **Fricción de perfilamiento:** ¿abandona más quien debe pasar el cuestionario de perfil (BBVA, Interbank) que quien entra directo (BCP, Trii)? Hoy es conjetura mía.
4. **Juego vs. sin juego en aporte**, no en operación: nadie lo midió; un A/B daría el primer dato.
5. **Medir lo que falta:** pedir a los actores (si hay acceso) retención de aporte a 3, 6 y 12 meses por cohorte, con definición de "activo" explícita.

## 7. 🕳️ Vacíos

- Retención y aporte sostenido en Trii, Tyba, Hapi y apps bancarias peruanas.
- Persistencia (mes 13, 25) de seguros de vida con ahorro en Perú.
- Sentimiento real de usuarios peruanos (Reddit, X, reseñas de tienda): no se pudo ver.
- Bancos globales, Vanguard, Fidelity, AFP y fondos de inversión: sin datos útiles en esta pasada.
- Si los defaults de F-850 funcionan igual con ingresos informales e inestables, típicos en Perú.

## 8. 📓 Bitácora

- **2026-11-01 · v1.0** — Creación. `/trinidad`; 27 fuentes (F-847 a F-873). Búsqueda sin acceso a textos completos; todo por resúmenes.

---

## Limitaciones

- La pista **social** quedó la más débil: sin foros ni redes de Perú.
- La pista **de negocio** es abundante pero toda es cifra de empresa; ninguna sirve para inferir retención.
- Varias fuentes empíricas (F-851, F-854, F-855) tienen autores o revista sin verificar; no apoyar decisiones en sus cifras sin abrir el original.
- Las cifras de Trii se contradicen entre fuentes y no se resolvió cuál es la correcta.

## Conexiones

- [[lealtad-gamificacion-recompensas-retail|Gamificación, recompensas y lealtad en retail]] — mismo problema en retail: poca evidencia causal de que el juego mueva conducta sostenida.
- [[behavioral-design-estado-disciplina|Behavioral design: estado de la disciplina y del mercado]] — crisis del nudge: los efectos de defaults y avisos suelen ser menores fuera del estudio original.
- [[fenomenos-psicologicos|Fenómenos psicológicos clásicos]] — estado de replicación del sesgo del presente, que sustenta el ahorro con compromiso.
- [[matriz-productos-vida-rimac|Matriz de productos Vida RIMAC]] — productos de vida con ahorro donde la persistencia de aporte es el indicador clave.
- [[mecanismos-seguros-salud|Mecanismos de seguros de salud]] — Vitality como caso de recompensa y caducidad, con la misma salvedad de selección.
- [[seguros-comportamiento-mundo-peru|Seguros: comportamiento y mercado, Mundo vs. Perú]] — baja confianza y educación financiera como contexto del aporte.
