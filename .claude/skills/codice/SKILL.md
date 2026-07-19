---
name: codice
description: >-
  El Códice es la ventana de lectura del ledger de evidencia del proyecto
  (`research/fuentes/codice.md`, mantenido por el skill `cronista`). Úsalo
  SIEMPRE que el usuario invoque /codice, o pida ver, consultar, buscar o
  listar fuentes ya registradas — "qué fuentes tenemos sobre X", "muéstrame
  el códice", "busca F-45", "qué dijo tal autor", "cuántas fuentes A tenemos",
  "qué respalda este node". No registra fuentes nuevas (eso lo hace
  `cronista` automáticamente) — `codice` solo lee, filtra y resume lo que ya
  está en el ledger.
---

# 📜 Códice — Consulta del ledger de fuentes

## Propósito

`cronista` **escribe** al ledger (`research/fuentes/codice.md`) cada vez que se usa
evidencia referenciable en el proyecto. `codice` es el otro lado de esa misma moneda:
el punto de invocación explícito para **leer** ese ledger — buscar, filtrar, resumir —
sin tener que abrir el archivo a mano ni hacer Ctrl+F sobre 170+ filas.

No dupliques la lógica de `cronista` aquí: `codice` nunca agrega ni edita filas del
ledger. Si mientras consultas detectas una fuente sin registrar o un dato desactualizado,
señálaselo al usuario y déjale la corrección a `cronista` (o dispáralo tú mismo si el
contexto lo amerita, pero como una acción aparte, no como parte de responder la consulta).

## Cuándo activarse

- El usuario invoca `/codice`.
- Pide ver, buscar, filtrar o listar fuentes ya registradas: "muéstrame el códice",
  "busca F-45", "qué fuentes tenemos sobre seguros paramétricos", "qué dijo Swiss Re",
  "cuántas fuentes de rigurosidad A tenemos", "qué respalda tal afirmación del node X".
- Quiere un panorama del estado del ledger: cuántas fuentes hay, distribución por
  rigurosidad, qué nodes tienen más/menos evidencia, fuentes registradas recientemente.
- Necesita verificar si una fuente ya está registrada antes de citarla (deduplicación
  manual, fuera del flujo automático de `cronista`).

No lo actives para registrar una fuente nueva (`cronista`) ni para investigar un tema
desde cero (`seeker`/`gossiper`/`marketer`/`trinidad`) — `codice` opera solo sobre lo que
ya está en el ledger.

## Dónde vive el ledger

`research/fuentes/codice.md` — archivo único, mantenido por `cronista`. Estructura:
cabecera + rúbrica de rigurosidad A-E + índice temático por node + tabla de fuentes
(`ID | Autor | Año | Fuente/Título | Rigurosidad | Resumen breve | Usado en/fundamenta |
URL/referencia | Registrado`).

Si el archivo no existe todavía, dilo explícitamente — significa que `cronista` no ha
registrado ninguna fuente aún, no es un error de `codice`.

## Tipos de consulta

### 1. Búsqueda puntual (por ID, autor o palabra clave)

- **Por ID** (`F-45`, "la fuente 45"): devuelve la fila completa.
- **Por autor/organismo** ("qué dijo Swiss Re", "fuentes de McKinsey"): busca coincidencias
  en el campo Autor, devuelve todas las filas que matcheen.
- **Por palabra clave/tema** ("fuentes sobre seguros paramétricos"): busca en Resumen breve
  y Fuente/Título; si el índice temático del ledger ya mapea el tema a un rango de `F-n`,
  úsalo primero en vez de recorrer toda la tabla.

Responde con una tabla filtrada (mismas columnas relevantes), no con el archivo completo.

### 2. Consulta por node / "qué respalda esto"

Cuando el usuario pregunta qué fuentes sostienen un node de `research/_nodes/`, cruza el
índice temático del ledger con la cabecera del node (que suele declarar su propio rango
de `F-n`, ej. "Fuentes registradas en `research/fuentes/codice.md` (F-16 a F-27)"). Si el
rango declarado en el node y lo que hay realmente en el ledger no coinciden, repórtalo
como inconsistencia — es señal de que el node quedó desactualizado o de un renumerado
pendiente de reflejar (como el reconciliado F-16–F-27 → F-160–F-171 de este proyecto).

### 3. Consulta agregada / panorama del ledger

- **Distribución por rigurosidad**: cuenta filas por nivel A-E, o filtra solo las de un
  nivel ("qué fuentes E tenemos" — útil para detectar dónde el proyecto se apoya en
  evidencia débil).
- **Distribución por node/tema**: usa el índice temático del ledger para mostrar cuántas
  fuentes respalda cada node.
- **Recencia**: fuentes con fecha `Registrado` más reciente, o filtradas por año de
  publicación.
- **Origen (qué skill las trajo)**: el campo Resumen breve suele indicar la pista de
  origen cuando viene de `trinidad` ("Pista social de /trinidad...", "Pista de negocio...")
  — útil para responder "qué encontró gossiper sobre X" separado de lo que encontró seeker.

Para cualquier agregación, trabaja sobre la tabla real del archivo — no estimes ni
redondees cifras sin haberlas contado.

## Formato de respuesta

- **Consulta puntual**: tabla con las filas que matchean, columnas relevantes a la
  pregunta (no siempre las 9 columnas completas — si preguntan solo por el resumen y la
  rigurosidad, no satures con URL y fecha de registro).
- **Consulta agregada**: cifra o tabla resumen + una línea de interpretación si hay algo
  notable (ej. "80% de las fuentes de este node son C o D — evidencia de industria, poca
  académica").
- **Sin resultados**: dilo explícitamente ("no encontré ninguna fuente que mencione X en
  el ledger actual") — no inventes una fuente para completar la respuesta ni asumas que
  existe porque "debería".

## Anti-patrones a evitar

- **Registrar fuentes nuevas desde aquí** — esa es la responsabilidad de `cronista`, no
  de `codice`. Si el usuario quiere agregar algo, indícaselo y deja que `cronista` se
  dispare (o invócalo tú, pero como paso separado y explícito).
- **Devolver el archivo completo cuando piden algo puntual** — filtra siempre a lo que se
  pidió.
- **Inventar una fuente o su contenido** si no aparece en el ledger — la honestidad
  epistemológica del resto del códice (`seeker`, `gossiper`, `marketer`) aplica igual
  aquí: "no está registrada" es una respuesta válida y preferible a adivinar.
- **Ignorar inconsistencias** entre lo que un node declara citar y lo que el ledger
  realmente contiene — repórtalas, no las suavices.
