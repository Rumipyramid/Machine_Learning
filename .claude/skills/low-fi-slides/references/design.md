# Sistema de diseño — Low-fi Slides ("blueprint")

Fuente de verdad visual del skill. El `SKILL.md` resume el flujo; esto define los
tokens y componentes exactos. Léelo siempre antes de construir el HTML.

## Por qué esta estética (no es decorativa, es funcional)

Un low-fi es una revisión de **contenido y estructura**, no de diseño final. La
estética "blueprint" (plano técnico + anotación de diseñador) comunica eso mismo con
honestidad: recuadros punteados en vez de imágenes finales, tipografía monoespaciada
para las anotaciones (como una nota al margen de un redline), un solo acento rojo que
funciona como "tinta de revisión". Nadie confunde esto con el deck final — esa es la
función.

## Tokens de color

Paleta fija (no rediseñar por proyecto; es la identidad del skill, no del contenido).

| Token | Claro | Oscuro | Uso |
|---|---|---|---|
| `--paper` | `#eef1f4` | `#10151b` | Fondo de página |
| `--grid` | `#ccd6de` | `#232c35` | Líneas finas del grid de plano (cada 16px) |
| `--grid-major` | `#b4c1cb` | `#2c3742` | Líneas mayores del grid (cada 96px), bordes de tablas/boxes |
| `--ink` | `#1c232c` | `#e9edf1` | Texto principal, borde de frame |
| `--ink-soft` | `#52606d` | `#9aa7b4` | Texto secundario |
| `--ink-faint` | `#7c8895` | `#6c7883` | Anotaciones, numeración, footers |
| `--card` | `#ffffff` | `#161d25` | Fondo de cada lámina |
| `--accent` | `#cf4520` | `#ff8a5c` | Único color de acento — "tinta de revisión" |
| `--placeholder` / `--placeholder-bg` | `#8b98a6` / `#e3e8ec` | `#4c5863` / `#1b232b` | Recuadros de assets pendientes |

Implementar con custom properties en `:root`, redefinir bajo
`@media (prefers-color-scheme: dark)` y de nuevo bajo `:root[data-theme="dark"]` /
`:root[data-theme="light"]` (el toggle del viewer debe ganar en ambas direcciones).
Nunca un color hardcodeado fuera de los tokens.

## Tipografía (tres roles, sin webfonts)

Este skill **no** embebe tipografías (a propósito: un low-fi usa fuentes del sistema,
es parte de la honestidad "no es el diseño final"). Tres roles:

1. **Cuerpo / títulos de lámina** — stack de sistema: `-apple-system, "Segoe UI",
   Roboto, Helvetica, Arial, sans-serif`. Títulos con `text-wrap: balance`.
2. **Anotación / dato / spec** — monoespaciada: `"SF Mono", "IBM Plex Mono", Menlo,
   Consolas, monospace`. Úsala para: numeración de lámina, eyebrows, labels de boxes,
   headers de tabla, números grandes de stat-callouts (con
   `font-variant-numeric: tabular-nums`). Es la voz "de spec sheet", no la voz de
   contenido.
3. Nunca mezclar los dos roles dentro del mismo bloque de texto.

## Layout — storyboard de scroll vertical

- Página = grid de plano de fondo (`background-image` con `linear-gradient` repetido,
  16px fino + 96px mayor), no una imagen.
- Cada lámina es un `.frame` con `aspect-ratio: 16 / 9`, borde sólido de 1.5px
  (`--frame`), fondo `--card`, y **crop marks** en dos esquinas opuestas (pseudo-
  elementos `::before/::after` con dos bordes).
- Antes de cada `.frame` va un `.rail`: numeración `NN / total` + línea + etiqueta corta
  de sección — es la referencia de "en qué lámina estoy" del storyboard.
- `max-width: 1100px` centrado. Una lámina por fila (scroll vertical), no carrusel.
- Cierre de página: una línea `.endnote` monoespaciada con el origen del contenido
  (de qué documento/fuente viene) — nunca dejar el low-fi sin decir de dónde salió el
  contenido.

## Componentes

| Componente | Cuándo usarlo |
|---|---|
| `.eyebrow` | Referencia a la sección/§ del documento fuente, arriba del título de lámina |
| `.tag` | Esquina superior derecha del frame — nombre corto de la lámina |
| `.box` (`.label` + `.val`) | Un dato/campo con su etiqueta — para specs, definiciones, resúmenes de tabla clave-valor |
| `.stat` (`.n` + `.l`) | Una cifra dura con su lectura — SOLO para números reales del material fuente, nunca inventados |
| `.callout` | Un hallazgo o síntesis que merece destacarse — borde de acento, no relleno |
| `.steps` / `.step` | Una secuencia **real** (proceso, línea de tiempo, orden causal) — línea punteada vertical + marcador. No usar numeración si el contenido no es realmente secuencial (ver regla en SKILL.md) |
| `table.wire` | Tablas simples, ruled, sin zebra-stripe ni color — cuando el material fuente ya trae una tabla |
| `.placeholder` | Recuadro punteado con hatch diagonal (`repeating-linear-gradient`) — donde iría un asset final (imagen, gráfico) que **no** se embebe en el low-fi. Lleva label mono con el nombre del archivo real si existe |
| `.grid2` / `.grid3` / `.grid6` | Grillas de `.box`/`.stat` — colapsan a 1 columna bajo 720px |
| `.split` | Layout de dos columnas asimétrico (1.1fr / 0.9fr) — para narrativa + tabla o narrativa + placeholder juntos |

## Reglas duras

- **Una idea por lámina.** Si un componente no cabe sin scroll interno forzado, es
  señal de que son dos láminas, no una.
- **Nunca lorem ipsum.** Todo el copy sale del material fuente (documento, tablero,
  conversación). Si un dato no existe, se omite o se marca `(por confirmar)` — no se
  inventa.
- **Numeración de pasos solo si hay secuencia real** (proceso, orden causal, línea de
  tiempo). Contenido categórico (seis entregables sin orden entre sí) va en grid de
  `.box`, no en `.steps`.
- **Los assets finales (imágenes, gráficos ya elaborados) van como `.placeholder`**,
  no embebidos — el low-fi valida estructura y contenido, no el asset en sí. Excepción:
  si el usuario pide explícitamente ver el asset real dentro del low-fi.
- **Self-contained**: todo el CSS inline en el HTML, sin `<link>` externos, sin
  dependencias de red (hereda las reglas del Artifact tool).
- **Ambos temas** (claro/oscuro) siempre definidos vía tokens — nunca un solo tema.
