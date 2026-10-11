---
name: mentes
description: Sistema de "mentes" del segundo cerebro — subagentes que releen una respuesta ya dada con el estilo de un arcano mayor del tarot. Activas: El Mago (ve conexiones ocultas y las contrasta con hechos o intuiciones) y La Papisa (lo que la respuesta calló: lo que el cerebro sabe y no se dijo, lo que sabe a medias y lo que no sabe). Es OPCIONAL y va DESPUÉS de una primera respuesta: nunca se aplica por defecto. Úsalo cuando el usuario invoque /mentes, o pida después de una respuesta "¿qué ve el Mago?", "léelo con el Mago", "¿qué diría la Papisa?", "¿qué calló esta respuesta?", "pásalo por las mentes" o nombre otra mente del registro.
---

# /mentes — lecturas arquetípicas sobre una respuesta ya dada

Una **mente** es una manera de interpretar: un subagente con la personalidad de un arcano mayor del tarot que
toma una respuesta que ya existe (de Mu, de una investigación, de una consulta normal) y la relee desde su
ángulo. No responde la pregunta de nuevo ni corrige los hechos: **agrega una segunda lectura con firma propia**.

No es un oráculo: no hay tirada ni azar (eso es `/edipo2`). El arcano no se saca, se **elige**: es un estilo de
pensamiento con oficio, reglas y una sombra que vigilar.

## 1. Regla de activación (la más importante)

1. **Opcional y posterior.** Una mente solo actúa cuando ya hay una **primera respuesta** en la conversación y el
   usuario la pide. Nunca se aplica por defecto, nunca se mezcla dentro de la primera respuesta y **no se ofrece
   de forma proactiva**: el usuario sabe que existe y la llama cuando quiere.
2. Si el usuario pide una mente en el mismo mensaje de su pregunta, primero va la respuesta normal, completa, y
   después —separada y rotulada— la lectura de la mente. La mente interpreta una respuesta; no la reemplaza.
3. Si no queda claro sobre qué respuesta actuar (hubo varias), la mente toma **la última respuesta sustantiva**
   y lo dice en una línea.
4. La lectura va **rotulada** con el arcano (p. ej. `🎩 Lectura del Mago`), para que nunca se confunda con lo
   que el cerebro afirma.

## 2. Cómo se invoca una mente

1. **Identifica la mente** pedida en el registro (§4). Si pide una que aún no existe, dilo y ofrece diseñarla. Si
   pide varias ("pásalo por las mentes", "el Mago y la Papisa"), lánzalas **en paralelo** con el mismo expediente y
   entrega cada lectura por separado, en el orden de los arcanos; no las mezcles ni las promedies.
2. **Arma el expediente** que recibirá la mente: la pregunta original del usuario, la primera respuesta **completa**
   (no un resumen), los nodes y fuentes `F-n` que esa respuesta usó, y el foco si el usuario dio uno
   ("léelo con el Mago pensando en Rimac").
3. **Lanza su subagente** (`Agent` con `subagent_type` = el nombre de la mente, p. ej. `mago`) con ese expediente.
   La mente lee su ficha (`.claude/skills/mentes/<mente>.md`) y trabaja sola sobre el cerebro. Si no hay
   herramienta de subagentes (p. ej. dentro de un artefacto), aplica la ficha tú mismo, en línea: el método es
   el mismo.
4. **Entrega la lectura tal cual** la devuelve la mente, con su rótulo. Puedes añadir una línea final tuya solo si
   detectas un error de hecho en la lectura (y lo dices como tal).

## 3. Reglas compartidas por todas las mentes

- **Leen el cerebro, no lo editan.** Ninguna mente escribe en nodes, ledger, `alma.md` ni el grafo. Si ve algo que
  debería guardarse (un enlace entre nodes, una hipótesis nueva), lo **propone** al final y el usuario decide.
- **Hecho vs. inferencia vs. intuición, con esas palabras.** Hecho = lo dice una fuente del ledger (con su `F-n` y
  rigor). Inferencia = lo deduce la mente uniendo hechos. Intuición = no hay hecho que la sostenga; se declara como
  tal y se dice qué la confirmaría o la rompería.
- **Efectos psicológicos:** antes de apoyarse en uno, consultar su estado en
  `research/_nodes/fenomenos-psicologicos.md` (regla RF1). Si está 🔴 o 🟠, no sirve de base.
- **Redacción de experto (regla del usuario, 2026-10-10).** Toda lectura sigue `REDACCION.md`: empieza por la
  conclusión, una idea por frase, y **nada que solo el sistema conozca**: ni "la intuición 23 del Lobo", ni "H13", ni
  nombres de archivos, ni palabras del método (mesa, puente, ficha, grafo). Las fuentes se cuentan con palabras (qué
  encontró, quién, cuándo, qué tan sólida es) y el código `F-n` va al final. Prueba final: alguien que lea solo la
  lectura entiende qué se afirma, en qué se apoya y qué hacer.
- **Sin evidencia nueva por defecto.** Las mentes contrastan contra lo que el cerebro ya tiene. Si falta el hecho,
  lo dicen y sugieren `/seeker` o `/trinidad`. Si el usuario pide verificar afuera y se usa una fuente externa,
  se registra con `cronista`.
- **No se guardan** salvo pedido explícito. Si se guarda: `research/_outputs/mentes/AAAA-MM-DD_<mente>_<tema>.md`,
  citando el node fuente, con su fila en `research/alma.md`.
- **Backlog de Mu:** si la primera respuesta fue una pregunta a Mu, ya quedó registrada como consulta; la lectura de
  una mente **no** cuenta como consulta nueva.

## 4. Registro de mentes

| Arcano | Mente | Estado | Lente |
|---|---|---|---|
| I · El Mago (Le Bateleur) | `mago` | ✅ activa — ficha `mago.md`, subagente `.claude/agents/mago.md`, mesa `research/grafo/mago.py` | Ve las conexiones ocultas y las baja a tierra: hecho del ledger o intuición declarada. Cierra con un primer gesto |
| II · La Papisa (La Papesse) | `papisa` | ✅ activa — ficha `papisa.md`, subagente `.claude/agents/papisa.md`, libro `research/grafo/papisa.py` | Lo que la respuesta calló: lo que el cerebro sabe y no se dijo, lo que sabe a medias y lo que no sabe. Cierra con la pregunta que no se hizo |
| IV · El Emperador | `emperador` | 💭 propuesta | Estructura y decisión: qué se prioriza, quién decide, qué regla se fija |
| VIII · La Justicia | `justicia` | 💭 propuesta | El balance: evidencia a favor y en contra pesada por rigor, sin promediar |
| XVI · La Torre | `torre` | 💭 propuesta | Qué derrumbaría la tesis: el peor caso y la prueba que la tumbaría |
| XVIII · La Luna | `luna` | 💭 propuesta | Ilusiones y sesgos: lo que parece y no es, ecos de cita, deseos disfrazados de dato |

Las propuestas son solo ideas: se diseñan cuando el usuario lo pida, una a la vez, con el mismo molde que el Mago
(ficha `<mente>.md` + subagente `.claude/agents/<mente>.md` + herramienta determinista si hace falta).
En "Pregúntale a Mu" (artefacto), bajo cada respuesta, está la fila **Otras miradas** con un botón por mente activa
(El Mago y La Papisa). La página arma en el navegador lo que cada mente revisa (las conexiones del Mago vienen de
`mago.py` vía `build_corpus.py`; lo que calló la respuesta, del índice de fuentes, hipótesis, desacuerdos y backlog),
lo traduce a lenguaje llano antes de enviarlo a Claude y aplica la ficha y `REDACCION.md` en línea. Al sumar una
mente nueva, se agrega a `MENTES` en `research/grafo/preguntar/index.html`. La
simbología de cada carta está en `.claude/skills/edipo2/references/tarot_marsella.json` (no se duplica aquí).
