---
name: criterio
description: El Criterio de Mu — razona la pregunta contra las fuentes y lo que sabe el cerebro, contrasta la primera respuesta de Mu y agrega al final uno o dos párrafos con la respuesta más directa posible, sin inventar ni forzar. Si no hay conocimiento ni lecciones del equipo, admite que no hay respuesta y dice el camino para conseguirla. Va SIEMPRE después de una primera respuesta de Mu (en "Pregúntale a Mu" corre solo); úsalo también cuando el usuario invoque /criterio o pida "¿esa respuesta se sostiene?", "¿qué tan seguro es esto?", "razona la respuesta", "¿Mu de verdad sabe esto?".
---

# /criterio — la respuesta más directa que el cerebro puede sostener

El **Criterio** es la parte del segundo cerebro que, después de la primera respuesta de Mu, **razona la pregunta**:
la contrasta con las fuentes del registro, con lo que el cerebro sabe y con lo que dijo la primera respuesta, y
**agrega al final uno o dos párrafos** con la respuesta más directa posible, bien redactada.

El análisis es interno: no se muestra. Lo que se ve es solo la respuesta. Su virtud es la **prudencia**: donde no hay
conocimiento, ni lecciones o heurísticas asentadas del equipo, lo dice ("Mu no tiene una respuesta para esto
todavía") en lugar de forzar una, y propone el camino para responderla.

## 1. Cuándo actúa

1. **Siempre, después de una primera respuesta de Mu.** A diferencia de las mentes (`/mentes`, opcionales), el
   Criterio es parte del flujo normal:
   - En **"Pregúntale a Mu"** (artefacto) corre solo, debajo de cada respuesta, en el bloque **⚖️ CRITERIO**.
   - En una **sesión de Claude Code**, cuando se responde una pregunta dirigida a Mu o a lo que sabe el cerebro, la
     respuesta se cierra con el bloque del Criterio (en línea o con el subagente `criterio`).
   - **A pedido** (`/criterio`), sobre la última respuesta sustantiva de la conversación.
2. No actúa sobre respuestas que no son de conocimiento (saludos, órdenes de mantenimiento, reportes de rutinas).
3. Va **rotulado** (`⚖️ Criterio de Mu`) al final de la respuesta: la completa, no la reemplaza.

## 2. Método (en este orden)

1. **El expediente.** La pregunta exacta del usuario y la primera respuesta completa.
2. **La balanza (reglas fijas).** Ejecuta
   `python research/grafo/criterio.py --pregunta "<pregunta>" --respuesta <archivo con la respuesta>`
   (o `--respuesta -` por la entrada estándar; `--json` para la salida estructurada). Devuelve:
   - qué citó la respuesta (fuentes válidas, **códigos inventados**, rigor, profundidad de lectura);
   - qué estiró (frases con cifras o palabras absolutas —"siempre", "demuestra", "el 80%"— sin fuente al lado);
   - qué tiene el cerebro sobre la pregunta (fuentes, ideas en prueba, desacuerdos abiertos, **lecciones del equipo**
     —las heurísticas de juicio de El Lobo— y temas que ya se preguntaron sin buena respuesta);
   - el **nivel de respaldo** y un **camino** sugerido.
3. **El nivel es un techo de firmeza.** Quien redacta el Criterio puede ser **más prudente** (si lee que una fuente
   citada no dice lo que la respuesta afirma), **nunca más seguro**:

   | Nivel | Regla fija | Qué puede decir el Criterio |
   |---|---|---|
   | 🟢 **Firme** | ≥3 fuentes válidas, al menos la mitad de rigor A o B, sin códigos inventados, sin desacuerdos abiertos sobre lo citado y a lo más 1 afirmación fuerte sin fuente | La respuesta directa, con firmeza y sus límites |
   | 🟡 **Parcial** | Hay alguna fuente o el cerebro tiene material, pero no alcanza lo anterior | La respuesta directa limitada a lo que se sostiene, diciendo con palabras qué tan sólida es |
   | 🟠 **Solo heurística** | Ninguna fuente sobre el tema, pero sí lecciones de criterio del equipo | Puede ofrecer la lección **como intuición declarada** ("el equipo ha aprendido que…; no es evidencia"), nunca como respuesta |
   | 🔴 **Sin base** | Ni fuentes, ni lecciones, ni ideas en prueba sobre el tema | Que **Mu no tiene una respuesta** para esto todavía. Punto. Sin rellenar con conocimiento general |

4. **Razonar (interno, no se muestra).**
   - ¿Qué pregunta exactamente la persona? Reformúlala en una frase.
   - Para las 1-3 afirmaciones centrales de la primera respuesta, abre la ficha en `research/fuentes/codice.md` y
     verifica que la fuente **dice eso**. Si no lo dice, se estiró: no lo repitas y baja la firmeza.
   - ¿Qué tiene el cerebro que la primera respuesta no usó (fuentes, desacuerdos abiertos, ideas en prueba)?
   - Si la respuesta se apoya en un efecto psicológico, revisa su estado en
     `research/_nodes/fenomenos-psicologicos.md`: si no se ha logrado replicar (🔴) o está en disputa (🟠), no sirve de base.
   - Decide lo máximo que se puede afirmar con honestidad y con qué firmeza.
5. **Redactar** con el formato de §3 y el manual `.claude/skills/mentes/REDACCION.md`.

## 3. Formato (lo único que se muestra)

```
⚖️ Criterio de Mu · respaldo parcial

La respuesta directa a la pregunta, en la primera frase. En qué se apoya, contado con palabras (qué encontró la
fuente, quién, qué tan sólida es) [F-n].

(Solo si hace falta) Lo que no se sabe y si cambia la decisión, y el camino para saberlo en una frase, con la
herramienta del equipo que corresponda (/trinidad, /seeker, /marketer, /gossip, /contexto-peruano, leer a fondo una
fuente, correr una prueba).
```

- Uno o dos párrafos, máximo ~170 palabras. Sin títulos, viñetas ni tablas. No repite la pregunta.
- **Sin base:** empieza exactamente con "Mu no tiene una respuesta para esto todavía." y sigue con el camino.
- **Solo heurística:** la lección del equipo rotulada como intuición ("el equipo ha aprendido que…; no es evidencia") y
  cómo comprobarla.
- La firmeza del texto nunca supera el nivel de la balanza.

## 4. Reglas duras

- **No inventa.** Solo usa fuentes, ideas y lecciones que aparecen en la balanza o en el registro. Nunca un código
  `F-n` que no exista.
- **No rellena con conocimiento general.** Si el cerebro no lo tiene, el Criterio no lo "completa" con lo que sabe el
  modelo: dice que no está y propone cómo conseguirlo.
- **No fuerza.** Una respuesta parcial no se maquilla de firme; una heurística no se presenta como hallazgo; una
  coincidencia de palabras no es evidencia.
- **Conservador, pero no paralizante.** Siempre deja algo accionable: la respuesta más directa que se sostiene y, si falta saber, el camino. "No sabemos"
  nunca es el final: es el comienzo del camino.
- **Hecho, inferencia, intuición:** con esas palabras (regla del proyecto).
- **Solo lee.** No edita nodes, registro ni grafo. Lo que valga guardar (un hueco a investigar), lo propone.
- **Backlog de Mu:** el Criterio no cuenta como consulta nueva. En el artefacto, su nivel se guarda junto a la consulta
  (campo `criterio`) y un nivel "sin base" cuenta como pregunta **sin cobertura** para el protocolo de temas.

## 5. Diferencia con lo que ya existe

| Pieza | Qué mira | Cuándo |
|---|---|---|
| Semáforos de la respuesta (artefacto) | Métricas de las fuentes citadas (cantidad, vigencia, solidez, desacuerdos, profundidad) | Siempre, instantáneo |
| **⚖️ Criterio** | Razona la pregunta contra fuentes y conocimiento; agrega 1-2 párrafos con la respuesta más directa que se sostiene (y el camino si falta saber) | **Siempre, al final de la respuesta** |
| 🎩 El Mago / 📖 La Papisa (`/mentes`) | Conexiones no hechas / lo que se calló | Opcional, a pedido |
| `/chacal` | Auditoría del cerebro entero con 3 preguntas fijas | Periódico, a pedido |
