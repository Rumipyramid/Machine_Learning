---
name: low-fi-slides
description: >-
  Convierte cualquier documento, tablero o conversación en una presentación wireframe
  de baja fidelidad (low-fi): analiza y sintetiza el material fuente en una secuencia
  de láminas (una idea por lámina, sin inventar datos) y las renderiza como un
  storyboard HTML autocontenido en la estética fija "blueprint" (grid de plano,
  recuadros punteados para assets pendientes, anotaciones monoespaciadas, un solo
  acento rojo de revisión), publicado como Artifact. Es el paso previo de revisión de
  contenido y estructura antes de invertir en una presentación final pulida (p. ej.
  con `presentaciones-rimac` o `rimac-slides`). Invócalo con /low-fi-slides o SIEMPRE
  que el usuario pida una presentación, deck, slides o láminas "low-fi", "lo-fi", "en
  wireframe", "en borrador"/"borrador visual", o quiera revisar la estructura de una
  presentación antes del diseño final.
---

# Low-fi Slides · storyboard wireframe para revisión de contenido

Estandariza cómo se responde a un pedido de presentación **low-fi**: siempre el mismo
recorrido (análisis → síntesis → storyboard), siempre la misma estética (no se
rediseña por proyecto — esa es la identidad del skill), siempre el mismo tipo de
entrega (Artifact, no archivo final del repo salvo que lo pidan).

## Recursos de esta skill

| Recurso | Qué es | Cuándo usarlo |
|---|---|---|
| `references/design.md` | El sistema de diseño completo (tokens, tipografía, componentes, reglas duras). **Es la fuente de verdad visual.** | Léelo siempre antes de construir el HTML — no reinventes la paleta ni la tipografía por proyecto. |
| `assets/template.html` | Esqueleto HTML con el CSS del sistema + un archetype de lámina por patrón (portada, spec-grid, secuencia, narrativa+tabla, stat-grid, placeholder de asset, cierre). | Punto de partida del build. Cópialo, instancia solo los archetypes que el contenido necesite, borra el resto. |

## Flujo de trabajo

### 1. Análisis y síntesis (el paso que no te puedes saltar)

No empieces por el HTML. Primero:

1. **Reúne el material fuente**: el documento, tablero o hilo de conversación que el
   usuario señale (o, si no señala nada, el documento/proyecto más reciente del que se
   viene hablando). Si el material fuente es ambiguo, pregunta cuál usar antes de
   sintetizar — no adivines de qué proyecto se trata.
2. **Encuentra el arco narrativo real** del contenido — no lo inventes, extráelo: suele
   ser algo como origen/contexto → problema → evidencia/diagnóstico → qué se construyó
   → qué sigue → cierre, pero sigue la estructura que el material fuente ya tenga (si
   el documento ya está numerado en secciones, esa numeración es tu punto de partida).
3. **Divide en láminas, una idea por lámina.** Una sección larga del documento fuente
   puede volverse 1–2 láminas; no fuerces todo el contenido de una sección en un solo
   frame. Si necesitas scroll interno para que quepa, son dos láminas.
4. **Decide el archetype de cada lámina** (ver tabla de `assets/template.html`):
   secuencia real → `.steps`; cifras duras → `.stat`; campos clave-valor → `.box`;
   tabla ya existente en la fuente → `table.wire`; imagen o gráfico final → `.placeholder`
   (nunca se embebe el asset final en un low-fi, salvo pedido explícito).
5. **No inventes nada.** Todo el copy sale del material fuente. Un dato que falta se
   omite o se marca `(por confirmar)`. Si el proyecto tiene una convención propia de no
   exponer códigos internos (p. ej. IDs de tablero) en material de cara a terceros,
   respétala también aquí.

### 2. Construir el storyboard

1. Copia `assets/template.html` como punto de partida.
2. Reemplaza cada `{{placeholder}}` con contenido real; borra los archetypes que no
   uses; duplica el que necesites repetir (p. ej. tres láminas `stat-grid` seguidas).
3. Actualiza `.rail` y `.tag` de cada lámina con la numeración final (`NN / total`) y
   la etiqueta corta de sección.
4. Sigue las reglas duras de `references/design.md` (self-contained, ambos temas,
   sin lorem ipsum, sin numeración de pasos si no hay secuencia real).
5. **Verifica visualmente antes de publicar** — no publiques sin confirmar que el HTML
   renderiza bien (proporciones 16:9, grillas que colapsan en mobile, ambos temas).

### 3. Publicar y entregar

1. Publica con el `Artifact` tool (favicon `📐`, título = nombre del proyecto +
   "— low-fi", descripción de una frase).
2. Cierra en el chat con: el link, un resumen de la secuencia de láminas (qué cubre
   cada una, en un renglón), y **el siguiente paso natural**: que el usuario valide
   contenido/estructura antes de pasar a una presentación final pulida.
3. **No commitees al repo por defecto** — es un artifact de revisión, no una fuente de
   verdad. Solo guárdalo como archivo del proyecto si el usuario lo pide explícitamente.

## Notas

- Este skill **no** sustituye a `presentaciones-rimac` ni a `rimac-slides` — es el paso
  anterior. Si el usuario ya validó el low-fi y quiere el deck final pulido, esa es la
  señal de pasar a esa otra skill (pregúntale antes de asumirlo).
- La estética "blueprint" es fija y no se negocia por proyecto — es lo que hace
  reconocible e inequívoco que "esto es un low-fi", no un diseño final a medio hacer.
