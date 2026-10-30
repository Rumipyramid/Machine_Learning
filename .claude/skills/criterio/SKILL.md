---
name: criterio
description: El sistema de razonamiento del segundo cerebro (Mu) empaquetado como método. Antes de responder una pregunta o apoyar una decisión con evidencia, consulta lo que el cerebro ya sabe, clasifica cada afirmación en dos ejes (rigor de la fuente y madurez de la afirmación), la pasa por los filtros de juicio que el cerebro destiló de sus iteraciones (trazabilidad, incentivo del emisor, qué se midió, magnitud, agregados, transferencia, mecanismo), audita hacia adentro y responde con la conclusión primero y lo que no sabe a la vista. Úsalo cuando el usuario invoque /criterio, pida "razónalo con el cerebro", "¿qué tan sólido es esto?", "¿podemos apoyarnos en este dato?", "evalúa esta afirmación", o cuando otro skill (trinidad, seeker, rastreo, chacal) necesite juzgar evidencia con el mismo estándar del proyecto.
---

# /criterio — cómo razona el segundo cerebro

## Qué es

El segundo cerebro no solo guarda fuentes: tiene una forma de pensar. Está repartida en varios lugares que
crecieron por separado:

- la **rúbrica de rigor A-E** del registro de fuentes (`.claude/skills/cronista/SKILL.md`);
- la **escala de madurez** de las afirmaciones, el **tablero de hipótesis** y las **reglas de criterio** del tema de
  tendencias (`research/_nodes/tendencias-diseno-innovacion.md`, §5, §6 y §7);
- los **estados de replicación** de los fenómenos psicológicos (`research/_nodes/fenomenos-psicologicos.md`);
- las **lecciones de juicio** de El Lobo (`research/lobo/opinion_experto.md`, sección "Intuición acumulada");
- los **semáforos** del auditor (`research/grafo/chacal_rubrica.json`).

Este skill junta esas piezas en un solo procedimiento. No las reemplaza: ellas siguen siendo la fuente de verdad y
siguen creciendo. `references/reglas.md` es el índice consolidado de los filtros de juicio, con su origen.

**Qué no es.** No es una búsqueda (para eso están `/rastreo`, `/seeker`, `/gossip`, `/marketer` y `/trinidad`). No
es una mente arquetípica (`/mentes`), que relee una respuesta ya dada y es opcional. `criterio` es el razonamiento
que debe ocurrir **siempre** que el cerebro responde con evidencia.

## El procedimiento

### 1. Encuadrar: qué decisión alimenta

Antes de razonar, escribe en una línea:
- **La pregunta**, en palabras del usuario.
- **La decisión que alimenta**: qué hará alguien distinto según la respuesta. Si no hay decisión, dilo: la respuesta
  será descriptiva y el estándar de prueba puede ser más bajo.
- **El tipo de afirmación** que hace falta: un hecho o cifra, un efecto causal, una tendencia, un benchmark de
  negocio, una percepción social o una norma. Cada tipo se prueba con evidencia distinta (ver paso 3).

### 2. Consultar lo que el cerebro ya sabe, antes que nada

En este orden, y sin buscar afuera todavía:

1. `research/alma.md`: qué tema es la fuente de verdad de la pregunta.
2. Ese tema (`research/_nodes/<tema>.md`): su resumen, su escala de madurez y su tablero de hipótesis.
3. El registro de fuentes (`research/fuentes/codice.md`, o `/codice`): qué fuentes hay y con qué rigor.
4. Lo que el cerebro sabe y suele callar:
   `python research/grafo/papisa.py --tema "<palabras clave>"` (fuentes no citadas, hipótesis vivas, disputas,
   lecturas a medias, temas sin cobertura).
5. Si la respuesta usa un efecto psicológico clásico: su estado en `research/_nodes/fenomenos-psicologicos.md`.
   **Ningún efecto clásico se cita sin su estado.**
6. Las lecciones de juicio de El Lobo que toquen el tema (buscar por palabra clave en "Intuición acumulada").

**Regla: confrontar antes que buscar novedad.** Si el cerebro ya tiene una hipótesis abierta sobre la pregunta, la
respuesta empieza por decir qué pasa con esa hipótesis. Mover una hipótesis de estado vale más que sumar un
hallazgo nuevo.

### 3. Clasificar cada afirmación en dos ejes que no se mezclan

| Eje | Qué mide | Escala |
|---|---|---|
| **Rigor de la fuente** | Qué tan sólido es el método con que se produjo el dato | A revisado por pares o datos primarios · B oficial o regulador · C consultora o industria · D prensa o blog que cita a otros · E opinión sin método |
| **Madurez de la afirmación** | Qué tan probada está la idea, sumando todas las fuentes | 🟢 documentada · 🟡 plausible, mal probada · 🔴 hype, refutada o sin respaldo · ⚔️ evidencia en conflicto |

Para efectos psicológicos se usa la escala de replicación: 🟢 robusto · 🔵 replicado con matices · 🟡 mixto ·
🟠 en disputa · 🔴 no replicado.

Además, para cada afirmación anota tres cosas:
- **Qué se midió**: preferencia declarada, desempeño o consecuencia real. No son intercambiables.
- **Fuerza**: descriptiva, observacional (asociación), causal o teórica.
- **Profundidad de lectura**: solo el resumen del registro, el resumen real de la fuente o la fuente completa.

Una fuente A puede sostener una afirmación 🔴 (un buen estudio que refuta) y diez fuentes D pueden sostener una
afirmación que sigue siendo 🟡. Por eso los ejes no se promedian.

**Qué evidencia prueba cada tipo de afirmación:**

| Tipo | La evidencia que la prueba | La que no alcanza |
|---|---|---|
| Efecto causal | Experimento aleatorizado, cuasi-experimento creíble, metaanálisis con moderadores | Correlación, caso de éxito, encuesta de satisfacción |
| Cifra o tamaño | Estadística oficial con método, filing auditado | Cifra repetida por prensa sin fuente primaria |
| Tendencia | Serie de tiempo, varias mediciones independientes | Un pico de conversación, una encuesta del vendedor |
| Benchmark de negocio | Resultados publicados y verificables | Autorreporte del operador sin auditoría |
| Percepción social | Volumen y validación de comentarios reales, sostenidos | Una nota viral, cuentas con incentivo |
| Norma | Texto de la norma vigente | Interpretación de un blog |

### 4. Pasar por los filtros de juicio

Aplica las familias de `references/reglas.md` que correspondan. Las que más se olvidan:

1. **Trazabilidad.** Ante una cifra espectacular, rastrear la fuente primaria antes de usarla. Varias citas que
   terminan en una sola fuente son una sola fuente (eco de cita). Una cifra sin ninguna fuente localizable es un
   huérfano de cita: no se usa.
2. **Incentivo del emisor.** Descontar a quien gana si la afirmación es cierta, y en los dos bandos: el que alarma y
   el que desmiente también pueden vender algo.
3. **Qué se midió.** Gustar no es funcionar, y funcionar no es producir la consecuencia que importa.
4. **Magnitud y forma.** La curva antes que el signo. Sin réplica, asumir que el efecto real es cerca de la mitad
   del original.
5. **Agregados que esconden.** Un promedio estable o un "sin efecto" general puede esconder un extremo que empeora.
6. **Transferencia.** Lo probado en otro país, sector o escala no se traslada solo. Si no hay evidencia en el Perú o
   Latinoamérica, dilo.
7. **Mecanismo antes que multiplicador.** Argumentar por qué funciona algo, no con un retorno de "100 a 1".

### 5. Auditar hacia adentro

Antes de cerrar, toma **el hallazgo que más te satisfizo** —el que resolvía la tensión o confirmaba lo que se
esperaba— y rastréalo con el mismo rigor con que desmontas las cifras ajenas. El cerebro ya encontró así hallazgos
propios que no tenían fuente primaria. Si hay tiempo y la decisión lo amerita, haz una búsqueda adversarial
explícita: la mejor evidencia en contra de la conclusión.

### 6. Juzgar la propia respuesta

Califica la respuesta con los cinco semáforos del auditor, en palabras:

| Dimensión | Pregunta |
|---|---|
| Cobertura | ¿Hay suficientes temas y fuentes del cerebro para responder? |
| Vigencia | ¿Lo que se usa es reciente para la velocidad del tema? |
| Solidez | ¿Qué parte se apoya en fuentes A o B? |
| Contradicciones | ¿Hay tensiones abiertas que tocan la respuesta? |
| Profundidad | ¿Las fuentes clave se leyeron más allá del resumen? |

Si dos o más están en rojo, la respuesta lo dice al principio, no al final.

### 7. Responder

- **Primero la conclusión**, con su madurez dicha en palabras ("está documentado", "es plausible pero mal
  probado", "la evidencia está en conflicto").
- **Cada afirmación con su fuente contada**: qué encontró, quién, cuándo y qué tan sólida es; el código `F-n` al
  final.
- **Las divergencias se reportan, no se resuelven a la fuerza.** Si la evidencia académica y la de negocio apuntan a
  lados distintos, esa tensión es parte de la respuesta.
- **Lo que no se sabe va a la vista**: qué falta, qué cambiaría la decisión y cómo se averiguaría.
- Redacción según `.claude/skills/mentes/REDACCION.md`: nada que solo el sistema conozca.

### 8. Qué hacer con lo aprendido

| Si apareció… | Va a… |
|---|---|
| Una fuente nueva | El registro de fuentes, vía `cronista`, con su rigor |
| Un hallazgo que vale retener | El tema correspondiente en `research/_nodes/` (Many Brains) |
| Una apuesta comprobable | El tablero de hipótesis del tema, con "cómo se falsa" |
| Una regla de juicio | Solo si sobrevivió a una búsqueda adversarial o a dos iteraciones: a las reglas del tema o a las lecciones de El Lobo, y se agrega a `references/reglas.md` |
| Una pregunta sin cobertura | El backlog de temas de Mu |

## Reglas invariables

- **Nunca una cifra sin fuente ni un efecto sin estado.**
- **Los dos ejes no se promedian**: rigor de la fuente y madurez de la afirmación son cosas distintas.
- **El hallazgo negativo es un hallazgo.** Tres búsquedas bien hechas sin resultado dicen algo del campo.
- **`criterio` no edita el registro ni los temas por su cuenta**: propone; lo que se guarda sigue las reglas de
  `cronista`, Many Brains y `CLAUDE.md`.
