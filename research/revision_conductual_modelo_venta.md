# 🧠 Revisión conductual — Modelo de venta basado en motivaciones

> Revisión de las secciones del modelo que invocan **sesgos o frameworks de la
> economía/ciencia del comportamiento**, acotadas a lo **mejor respaldado por la
> literatura**. Cada bloque es un **reemplazo drop-in** para el documento original
> (`Modelo_de_venta_basado_en_motivaciones.md`): se indica qué sección sustituye.
> Derivado de investigación `/seeker` (2026-06-30). Fuentes nuevas: F-16 a F-25 en
> `research/fuentes/registro_fuentes.md`.

## Criterio aplicado

1. **Un sesgo o framework solo entra si (a) está bien respaldado y (b) justifica una decisión concreta de diseño.** Nombrar un mecanismo que nunca se usa ("teatro conductual") resta credibilidad a los sólidos.
2. **Se retiran los mecanismos contestados o mal aplicados al caso de seguros** (loss aversion como driver de protección, optimism bias, endowment effect, sunk cost como motor de cambio).
3. **Se agrega el mejor respaldado y más relevante para el sub-aseguramiento**, que el documento omitía: *present bias / inercia*.

| Elemento | Antes | Después |
|---|---|---|
| Sesgos en §2.3 | 9 (varios decorativos/contestados) | 4 operacionalizados + nota de lo retirado |
| Loss aversion (§2.3, §4.2-M01) | "motor de la protección" | Retirado como motor; reemplazado por responsabilidad/regret anticipado |
| Optimism bias (§2.3) | listado | Retirado (artefacto metodológico) |
| Endowment + sunk cost (§4.2-M04) | "tres sesgos operan" | Retirados; status quo + reencuadre de recuperación |
| COM-B (§2.3) | "una acción ocurre únicamente cuando…" | Marco diagnóstico, no ley causal |
| Behavioral Life-Cycle (§2.1) | sustento de la "curva de 4 etapas" | Reetiquetado: la curva es ciclo de vida; lo conductual es mental accounting |
| JTBD (§2.2) | "justifica exactamente 4 motivaciones" | Lente de diseño; no predice el número |

---

## ▸ Reemplaza el sub-bloque de §2.1 — "El sustento teórico detrás del marco"

**El sustento conductual de la curva — y su límite.** Conviene separar dos cosas
que es fácil confundir. Que las necesidades financieras cambien por **etapa de vida**
es una segmentación por ciclo de vida (en la tradición de la hipótesis del ciclo de
vida de Modigliani y de la segmentación comercial), no un hallazgo de economía
conductual. Lo que sí aporta la economía conductual es un mecanismo más fino: el
**mental accounting** (Thaler) —y su extensión, la *Behavioral Life-Cycle Hypothesis*
de Shefrin y Thaler (1988)— muestra que las personas no administran todo su dinero
con la misma lógica, sino que crean **cuentas mentales separadas** para el presente,
el mediano plazo y el futuro, cada una con su propia tolerancia al riesgo y
sensibilidad al precio.

Esa es la parte que explica por qué un cliente en etapa de creación de patrimonio
responde a propuestas que combinan retorno visible con protección: opera
simultáneamente con una cuenta mental de acumulación activa y una de protección ante
el shock. No hace falta atribuir la curva de cuatro etapas a Shefrin y Thaler —basta
con el mental accounting, que es el mecanismo efectivamente respaldado.

> _Nota de calibración (SDT, sub-bloque previo de §2.1):_ la Teoría de la
> Autodeterminación es una de las teorías mejor respaldadas en psicología de la
> motivación. La lectura de que las estrategias financieras informales satisfacen
> autonomía, competencia y vinculación es una **interpretación plausible**, no un
> dato medido en esta investigación; se usa como lente explicativa, no como evidencia
> de que esas estrategias sean eficientes.

---

## ▸ Reemplaza la introducción de §2.2 y la sección "Por qué este framework justifica exactamente cuatro motivaciones"

**La lógica central (con su estatus correcto).** Jobs to Be Done es un **marco de
diseño y marketing** popularizado por Clayton Christensen. Su premisa es que los
clientes no compran productos —contratan soluciones para hacer un trabajo que
necesitan resolver—, y que lo que determina la elección no es el atributo técnico
sino qué tan bien el producto hace ese trabajo.

> _Nota de calibración:_ JTBD es una lente organizadora útil, **no una teoría
> conductual con validación empírica**. Su taxonomía de trabajos "funcionales,
> emocionales y sociales" es una convención práctica sin base experimental
> establecida (Klement). Lo usamos para estructurar la conversación de venta, no como
> evidencia científica con el mismo peso que, por ejemplo, el mental accounting.

**Por qué cada motivación necesita una propuesta distinta** (reemplaza el título
anterior). Las cuatro motivaciones no son variaciones del mismo job: cada una activa
un mecanismo distinto, requiere un idioma distinto y deriva en un producto distinto.
JTBD **no predice cuántas** motivaciones debe haber —eso lo determinan el portafolio
y el momento de vida (sección anterior)—. Lo que JTBD aporta es el criterio para no
colapsar trabajos distintos en una sola conversación: si dos motivaciones se
resuelven con el mismo producto y el mismo idioma, son el mismo job operacional (como
ocurre con "sostener lo que construí", que colapsa en protección).

---

## ▸ Reemplaza por completo §2.3 — "Behavioral economics" y "COM-B"

### 2.3 Economía conductual

La economía conductual explica por qué dos clientes con necesidades similares toman
decisiones distintas frente a la misma propuesta. La evidencia muestra que las
decisiones financieras están influidas por el contexto, el encuadre y un puñado de
sesgos sistemáticos.

Para mantener el modelo anclado a lo **mejor respaldado por la evidencia y relevante
para seguros**, trabajamos con cuatro mecanismos —y cada uno justifica una decisión
concreta de diseño, no aparece como adorno:

- **Present bias e inercia.** Las personas sobrevaloran el costo presente (la prima de
  hoy) frente a un beneficio futuro y difuso (la protección), y por defecto no actúan.
  Es el mecanismo mejor documentado del sub-aseguramiento (Platteau et al., 2021).
  _Decisión que justifica:_ por qué el punto de entrada es el momento de vida —no el
  perfil— y por qué el Paso 1 minimiza la fricción: cada barrera adicional convierte la
  inercia en abandono.
- **Mental accounting** (Thaler). Las personas asignan el dinero a "cuentas mentales"
  distintas (gasto, ahorro, inversión) y evalúan cada decisión según la cuenta en que
  la ubican. _Decisión que justifica:_ presentar el producto como "ahorro con
  protección incluida" —no como "prima"— activa la cuenta de inversión y cambia la
  evaluación del precio (motivación de crecimiento).
- **Status quo bias / inercia de cambio** (Samuelson & Zeckhauser, 1988). Hay una
  tendencia fuerte a mantener la situación actual aunque exista una opción mejor, por
  el esfuerzo y la incertidumbre del cambio. Es de los sesgos más robustos en
  decisiones de seguros y pensiones. _Decisión que justifica:_ el endoso requiere hacer
  **visible la comparación**, porque el cliente no cambia por iniciativa propia
  (motivación de recuperación).
- **Anchoring.** La primera cifra de referencia condiciona de forma desproporcionada
  las evaluaciones posteriores. _Decisión que justifica:_ en el dimensionamiento
  (Paso 2), el primer monto que ve el cliente —el objetivo, no la prima— ancla la
  conversación hacia "cuánto quiere llegar a tener", no hacia "cuánto cuesta".

> _Nota metodológica sobre lo que dejamos fuera:_ versiones anteriores listaban
> también loss aversion, optimism bias, endowment effect, goal-gradient y social proof.
> Los acotamos por rigor: la forma fuerte de **loss aversion** no está bien respaldada
> (Gal & Rucker, 2018) y, en seguros, predice más bien sub-aseguramiento (Gottlieb,
> 2012); el **optimism bias** medido por método comparativo es en parte un artefacto
> estadístico (Harris & Hahn, 2011); el **endowment effect** es frágil y depende del
> procedimiento experimental (Plott & Zeiler, 2005). El **goal-gradient** es real pero
> modesto (Kivetz et al., 2006): puede mencionarse al mostrar progreso, sin colgarle
> peso. Un sesgo que no cambia una decisión de diseño no aporta.

### COM-B: la motivación no basta

El modelo **COM-B** (Michie et al.) es un **marco diagnóstico** útil: ayuda a ver que,
además de la motivación, una acción se vuelve más probable cuando coinciden tres
condiciones:

- **Capability:** el cliente sabe qué decide y cómo, y puede actuar con confianza.
- **Opportunity:** el entorno, el canal y el momento facilitan la acción.
- **Motivation:** existe una razón suficiente, racional y emocional, para actuar.

> _Nota de calibración:_ COM-B organiza el diagnóstico, pero **no es un modelo
> predictivo validado**. Su validez predictiva es moderada y se mide casi siempre
> sobre conducta **autorreportada** (Howlett et al., 2019; Willmott et al., 2021,
> R²≈0.23–0.31). Lo usamos para diagnosticar barreras, no como ley causal: la
> convergencia de los tres factores hace la acción **más probable, no inevitable**.

Aplicado a las cuatro motivaciones, COM-B sugiere una barrera dominante distinta:

- **Protección** — barrera de *capability*: el cliente siente la necesidad pero no sabe
  cuánto cubrir ni cómo elegir. El perfilador guía el dimensionamiento en el idioma de
  su vida, sin jerga.
- **Crecimiento** — barrera de *motivation* reflectiva: no tiene claro que el seguro
  puede ser vehículo de acumulación. El framing (objetivos y retornos, no primas)
  trabaja esa barrera.
- **Meta** — barrera de *opportunity*: tiene la meta clara pero no el momento ni el
  canal. El canal digital está disponible cuando el cliente piensa en su meta.
- **Endoso** — barrera de *status quo* dentro de la *motivation*, combinada con baja
  *capability* sobre qué tiene contratado: no cambia porque no entiende bien qué tiene
  y cambiar parece más complicado que quedarse.

---

## ▸ Reemplaza "Qué evidencia la respalda" de §4.2 · Motivación 01

_Qué evidencia la respalda:_ Liebenberg et al. (2012) demostraron que eventos de vida
concretos —matrimonio, nacimiento de un hijo— predicen la demanda de seguro con
consistencia estadística. LIMRA–Bain (2025) encontró que el 39% de los prospectos
reconoció su necesidad a raíz de un evento de vida específico. El **motor psicológico**
de esta motivación es la **responsabilidad hacia personas concretas que dependen del
cliente** y la **simulación del escenario** en que él falta —no la *loss aversion* en
sentido técnico—: en seguros la aversión a la pérdida es un predictor ambiguo y puede
incluso favorecer el sub-aseguramiento (Gottlieb, 2012; Platteau et al., 2021). Lo que
activa es el deseo de no dejar a los suyos vulnerables, anclado en el regret
anticipado.

---

## ▸ Reemplaza "Qué evidencia la respalda" de §4.2 · Motivación 04

_Qué evidencia la respalda:_ El mecanismo dominante es el **status quo bias / inercia**
(Samuelson & Zeckhauser, 1988): el cliente no cambia el desgravamen por iniciativa
propia aunque exista una opción mejor —necesita que alguien le haga **visible la
comparación**—. Sobre eso opera un **reencuadre de recuperación**: presentar la
propuesta como "lo que ya pagas, finalmente se queda contigo" en lugar de "cambia tu
seguro".

> _Nota de calibración:_ versiones previas atribuían esta motivación a *sunk cost* y
> *endowment effect*. Los retiramos: el sunk cost explica por qué la gente **se queda**
> en lo que ya pagó (opera contra el cambio, no a favor), y el endowment effect es un
> efecto frágil y mal ajustado a este caso (Plott & Zeiler, 2005). El reencuadre de
> recuperación es una palanca de comunicación legítima; no necesita el respaldo de un
> sesgo para funcionar.

---

*Fuentes nuevas registradas en `research/fuentes/registro_fuentes.md` (F-16 a F-25).
Revisión bajo protocolo `/seeker`, 2026-06-30.*
