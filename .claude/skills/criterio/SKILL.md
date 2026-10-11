---
name: criterio
description: El Criterio de Mu — razona la primera respuesta de Mu frente a la pregunta que se le hizo, con reglas conservadoras. Pesa cuánto respaldo tiene (firme · parcial · solo heurística · sin base), separa lo que se sostiene de lo que se estiró, admite cuando el cerebro no tiene respuesta y propone un camino para responderla. Va SIEMPRE después de una primera respuesta de Mu (en "Pregúntale a Mu" corre solo); úsalo también cuando el usuario invoque /criterio o pida "¿esa respuesta se sostiene?", "¿qué tan seguro es esto?", "razona la respuesta", "¿Mu de verdad sabe esto?".
---

# /criterio — ¿la respuesta de Mu responde de verdad la pregunta?

El **Criterio** es la parte del segundo cerebro que, después de que Mu responde, se detiene a pensar **antes de que
la respuesta se use**. No vuelve a responder ni agrega datos: **pesa** la respuesta frente a la pregunta y dice,
con reglas fijas y sin adornos, cuánto de ella se sostiene, qué se estiró, qué no se sabe y cómo se podría llegar a
saberlo.

Su virtud es la **prudencia**: donde no hay conocimiento, ni lecciones o heurísticas asentadas del equipo, el Criterio
lo dice en voz alta ("Mu no tiene una respuesta para esto todavía") en lugar de forzar una.

## 1. Cuándo actúa

1. **Siempre, después de una primera respuesta de Mu.** A diferencia de las mentes (`/mentes`, opcionales), el
   Criterio es parte del flujo normal:
   - En **"Pregúntale a Mu"** (artefacto) corre solo, debajo de cada respuesta, en el bloque **⚖️ CRITERIO**.
   - En una **sesión de Claude Code**, cuando se responde una pregunta dirigida a Mu o a lo que sabe el cerebro, la
     respuesta se cierra con el bloque del Criterio (en línea o con el subagente `criterio`).
   - **A pedido** (`/criterio`), sobre la última respuesta sustantiva de la conversación.
2. No actúa sobre respuestas que no son de conocimiento (saludos, órdenes de mantenimiento, reportes de rutinas).
3. Va **rotulado** (`⚖️ Criterio de Mu`) y separado de la respuesta: nunca se mezcla con ella ni la reemplaza.

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
3. **El nivel es un techo.** Quien redacta el Criterio puede **bajarlo** (si lee que una fuente citada no dice lo que
   la respuesta afirma), **nunca subirlo**:

   | Nivel | Regla fija | Qué puede decir el Criterio |
   |---|---|---|
   | 🟢 **Firme** | ≥3 fuentes válidas, al menos la mitad de rigor A o B, sin códigos inventados, sin desacuerdos abiertos sobre lo citado y a lo más 1 afirmación fuerte sin fuente | Que la respuesta se sostiene, con sus límites |
   | 🟡 **Parcial** | Hay alguna fuente o el cerebro tiene material, pero no alcanza lo anterior | Qué parte se sostiene y cuál no; la respuesta prudente se limita a la parte sostenida |
   | 🟠 **Solo heurística** | Ninguna fuente sobre el tema, pero sí lecciones de criterio del equipo | Puede ofrecer la lección **como intuición declarada** ("el equipo ha aprendido que…; no es evidencia"), nunca como respuesta |
   | 🔴 **Sin base** | Ni fuentes, ni lecciones, ni ideas en prueba sobre el tema | Que **Mu no tiene una respuesta** para esto todavía. Punto. Sin rellenar con conocimiento general |

4. **Contrastar lo esencial.** Para las 1-3 afirmaciones centrales de la respuesta, abre la ficha de la fuente citada
   en `research/fuentes/codice.md` y verifica que **dice eso**. Si no lo dice, es "estirado" y el nivel baja.
5. **Efectos psicológicos.** Si la respuesta se apoya en uno, revisa su estado en
   `research/_nodes/fenomenos-psicologicos.md`: si no se ha logrado replicar (🔴) o está en disputa (🟠), no sirve de base.
6. **Redactar** con el formato de §3 y el manual `.claude/skills/mentes/REDACCION.md`.

## 3. Formato (lo que se entrega)

```
⚖️ Criterio de Mu · ¿la respuesta responde la pregunta?

**Veredicto:** Responde · Responde en parte · No puede responder con lo que sabe — y por qué, en una frase.
**Respaldo:** 🟢 firme · 🟡 parcial · 🟠 solo heurística · 🔴 sin base (el nivel de la balanza, o más bajo).

**Lo que se sostiene** (solo si hay algo)
- **La afirmación, corta.** En qué se apoya, contado con palabras: qué encontró la fuente, quién, cuándo, qué tan sólida es [F-n].

**Lo que se estiró** (solo si hay algo)
- **La frase de la respuesta que va más allá de su evidencia.** Por qué no se sostiene y cómo debería decirse.

**Lo que Mu no sabe**
- La parte de la pregunta que queda sin respuesta, y si eso cambia la decisión.

**Respuesta prudente:** lo máximo que se puede afirmar honestamente, en 1-3 frases. Si el nivel es "sin base":
"Mu no tiene una respuesta para esto todavía." Si es "solo heurística": la lección, rotulada como intuición.

**Camino para responderla**
1. El paso más útil, con verbo y con la herramienta del equipo que corresponde (investigar con `/trinidad`, `/seeker`,
   `/marketer`, `/gossip` o `/contexto-peruano`; leer a fondo una fuente; correr una prueba; preguntar a una persona).
2. …(2 a 4 pasos)
```

Extensión: 120-300 palabras. Sin títulos ni tablas dentro del bloque.

## 4. Reglas duras

- **No inventa.** Solo usa fuentes, ideas y lecciones que aparecen en la balanza o en el registro. Nunca un código
  `F-n` que no exista.
- **No rellena con conocimiento general.** Si el cerebro no lo tiene, el Criterio no lo "completa" con lo que sabe el
  modelo: dice que no está y propone cómo conseguirlo.
- **No fuerza.** Una respuesta parcial no se maquilla de firme; una heurística no se presenta como hallazgo; una
  coincidencia de palabras no es evidencia.
- **Conservador, pero no paralizante.** Siempre deja algo accionable: la respuesta prudente y el camino. "No sabemos"
  nunca es el final: es el comienzo del camino.
- **Hecho, inferencia, intuición:** con esas palabras (regla del proyecto).
- **Solo lee.** No edita nodes, registro ni grafo. Lo que valga guardar (un hueco a investigar), lo propone.
- **Backlog de Mu:** el Criterio no cuenta como consulta nueva. En el artefacto, su nivel se guarda junto a la consulta
  (campo `criterio`) y un nivel "sin base" cuenta como pregunta **sin cobertura** para el protocolo de temas.

## 5. Diferencia con lo que ya existe

| Pieza | Qué mira | Cuándo |
|---|---|---|
| Semáforos de la respuesta (artefacto) | Métricas de las fuentes citadas (cantidad, vigencia, solidez, desacuerdos, profundidad) | Siempre, instantáneo |
| **⚖️ Criterio** | **Si la respuesta responde la pregunta** con lo que el cerebro sabe; qué se estiró; respuesta prudente; camino | **Siempre, después de la respuesta** |
| 🎩 El Mago / 📖 La Papisa (`/mentes`) | Conexiones no hechas / lo que se calló | Opcional, a pedido |
| `/chacal` | Auditoría del cerebro entero con 3 preguntas fijas | Periódico, a pedido |
