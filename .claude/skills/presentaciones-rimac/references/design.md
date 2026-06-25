---
version: alpha
name: Editorial Presentations
description: Sistema de presentaciones HTML editoriales sobrias del CoE de Diseño de Experiencias. Slides 16:9 fixed-stage, tipografía Manrope bold, acentos de gradiente cálido sobre fondos blancos y lavanda.

brand:
  team: CoE de Diseño de Experiencias
  organization: Rimac
  logo:
    src: ./06_assets/logo-rimac.svg
    width: 115px
    placement: footer-left

colors:
  primary: "#0B1620"
  secondary: "#6B7280"
  tertiary: "#F7052D"
  neutral: "#FFFFFF"
  accent-orange: "#FF7A00"
  accent-magenta: "#C8128B"
  bg-section: "#ECEEFC"
  bg-soft: "#F5F6FB"
  bg-viewport: "#F2F3F7"
  bg-warm-soft: "#FFF6EF"
  bg-cool-soft: "#F7F8FE"
  line: "#E5E7EB"
  text: "#1F2937"

gradients:
  hero: "linear-gradient(90deg, #FF7A00 0%, #F7052D 45%, #C8128B 100%)"
  soft: "linear-gradient(135deg, #FFEFE3 0%, #FCE4EC 100%)"

typography:
  cover-h1:
    fontFamily: Manrope
    fontSize: 116px
    fontWeight: 800
    lineHeight: 0.96
    letterSpacing: -0.04em
  section-h1:
    fontFamily: Manrope
    fontSize: 140px
    fontWeight: 800
    lineHeight: 0.95
    letterSpacing: -0.04em
  h2:
    fontFamily: Manrope
    fontSize: 64px
    fontWeight: 800
    lineHeight: 1.05
    letterSpacing: -0.025em
  h3:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.015em
  body-lead:
    fontFamily: Manrope
    fontSize: 26px
    fontWeight: 500
    lineHeight: 1.4
  body-md:
    fontFamily: Manrope
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.45
  body-sm:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.5
  eyebrow:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: 700
  tier-tag:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: 700
    letterSpacing: 0.05em
    textTransform: uppercase
  footer-tag:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: 500
    letterSpacing: 0.02em
  pagenum:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: 500
    letterSpacing: 0.04em

rounded:
  sm: 4px
  md: 14px
  lg: 18px
  pill: 999px

spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 32px
  xl: 56px
  2xl: 80px
  3xl: 100px

stage:
  width: 1920px
  height: 1080px
  aspectRatio: "16:9"
  scaling: uniform-transform
  background: "{colors.neutral}"

components:
  slide:
    backgroundColor: "{colors.neutral}"
    padding: "80px 100px 100px"
  slide-section:
    backgroundColor: "{colors.bg-section}"
    padding: "80px 100px 100px"
  card:
    backgroundColor: "{colors.bg-soft}"
    rounded: "{rounded.lg}"
    padding: "32px 32px 28px"
  card-warm:
    backgroundColor: "{colors.bg-warm-soft}"
    rounded: "{rounded.lg}"
    padding: "32px 32px 28px"
  card-cool:
    backgroundColor: "{colors.bg-section}"
    rounded: "{rounded.lg}"
    padding: "32px 32px 28px"
  callout:
    backgroundColor: "{colors.bg-section}"
    rounded: "{rounded.sm}"
    padding: "28px 36px"
    borderLeft: "6px solid {colors.tertiary}"
  pill:
    rounded: "{rounded.pill}"
    padding: "10px 18px"
    backgroundColor: "{colors.bg-soft}"
    typography: "{typography.body-sm}"
  pill-red:
    rounded: "{rounded.pill}"
    padding: "10px 18px"
    backgroundColor: "rgba(247,5,45,0.08)"
    textColor: "{colors.tertiary}"
  footer-tag:
    textColor: "{colors.secondary}"
    typography: "{typography.footer-tag}"
  pagenum:
    textColor: "{colors.secondary}"
    typography: "{typography.pagenum}"
---

## Overview

Sobriedad editorial con calidez selectiva. El sistema evoca una página impresa de broadsheet: tipografía generosa en peso pesado, páginas blancas tranquilas rotas ocasionalmente por una lavanda suave para los breaks de sección, y un único gradiente cálido-a-magenta aplicado quirúrgicamente sobre dos o tres palabras clave por título.

Audiencia: cualquiera. El mismo deck lee bien en un comité interno, en un foro público, o circulando como PDF. La estética es confiada sin ser comercial; estructurada sin ser corporativa.

Tono en slides: declarativo, oraciones completas, punto final en titulares. El gradiente es el único gesto decorativo del sistema — se usa para destacar una sola frase por slide. Todo lo demás retrocede para que ese gesto aterrice.

---

## Colors

- **Primary (`#0B1620`):** Tinta profunda para titulares, eyebrows y énfasis en tier-tags. No diluir.
- **Text (`#1F2937`):** Color de cuerpo. Un paso más suave que primary para que los párrafos largos se lean mejor.
- **Secondary (`#6B7280`):** Gris muteado para el tag del footer, page number, captions, placeholders "—" y anotaciones tipo `(touch)`.
- **Tertiary (`#F7052D`):** Rojo de marca. Usado para el logo Rimac, el borde de callout, acentos de tier-tag y celdas enfáticas en tablas. Nunca sobre titulares ni cuerpo.
- **Neutral (`#FFFFFF`):** Fondo de slide por defecto. El lienzo sobre el que aterriza la tipografía.
- **Accent Orange (`#FF7A00`):** Inicio del gradiente hero. Se usa standalone en curvas de gráficos y como borde izquierdo de cards warm.
- **Accent Magenta (`#C8128B`):** Fin del gradiente hero. Se usa standalone en bordes de cards cool.
- **Bg Section (`#ECEEFC`):** Fondo lavanda reservado para section dividers y slides que quieren alejarse del blanco sin ir a oscuro.
- **Bg Soft (`#F5F6FB`):** Fondo de card por defecto. Lo suficientemente suave para registrarse como contenedor sin competir con el contenido.
- **Bg Warm/Cool Soft (`#FFF6EF` / `#F7F8FE`):** Usados en celdas de tablas comparativas. Distinguen dos lados sin saturar.
- **Bg Viewport (`#F2F3F7`):** Color fuera del stage 1920×1080 cuando el navegador es más ancho o alto que 16:9. Tiene que ser neutro para no leerse como un marco.
- **Line (`#E5E7EB`):** Todos los bordes de tablas, divisores, separadores.

**Gradientes:**
- `gradients.hero` — aplicado vía `background-clip: text` a una sola frase por título. Nunca a un fill, nunca a un párrafo de cuerpo.
- `gradients.soft` — fill para cards warm y esquinas decorativas SVG.

---

## Typography

Familia única: **Manrope** (Google Fonts), weights 400–800. Sans humanista geométrico con el balance adecuado entre peso editorial en 800 y legibilidad en 400.

```html
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
```

**Racional de la escala** (a 1920 px de canvas):

- **Cover y section H1 son dominantes** (116–140 px). Consumen el slide. El letter-spacing negativo (-0.04em) los mantiene apretados, no airosos.
- **H2 de slide vive cerca de 64 px** pero puede oscilar 56–88 px según el largo del título. La grid lo permite — el wrapper slide-body lo centra limpio.
- **El cuerpo escala en tercios claros** — 26 (lead) / 22 (md) / 18 (sm). Sin micro-tweaks entre tamaños.
- **Eyebrow, tier-tag, footer-tag, pagenum comparten 14–18 px** y dependen de `letter-spacing` y `text-transform: uppercase` para jerarquía en lugar de tamaño.

**Negritas:** weight 800 para titulares; 700 para sub-titulares y tier-tags; 500 para footer/pagenum; 400 para cuerpo. Evitar 600 — enturbia el contraste.

**Gradient en texto:**

```css
.grad {
  background: linear-gradient(90deg, #FF7A00 0%, #F7052D 45%, #C8128B 100%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}
```

Aplicar a una frase por título (máx. 2–3 palabras consecutivas). Nunca a un título completo; nunca a texto de cuerpo.

---

## Layout

**Stage fijo de 1920×1080 px**, escalado uniformemente al viewport mediante `transform: scale()`. Esto fuerza 16:9 en cualquier pantalla sin reflujo del contenido.

Gotcha crítico: cuando el stage vive dentro de un contenedor `display: flex`, debe declarar `flex-shrink: 0` + `min-width/min-height` o el flex parent lo aplasta por debajo de 1920 px.

```css
.viewport {
  position: fixed; inset: 0;
  display: flex; align-items: center; justify-content: center;
  background: #F2F3F7;
}
.stage {
  width: 1920px; height: 1080px;
  min-width: 1920px; min-height: 1080px;
  flex-shrink: 0;
  position: relative;
  transform-origin: center center;
  background: #FFFFFF;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(11,22,32,0.12);
}
```

```js
function fit() {
  const sx = window.innerWidth / 1920;
  const sy = window.innerHeight / 1080;
  document.getElementById('stage').style.transform = `scale(${Math.min(sx, sy)})`;
}
window.addEventListener('resize', fit); fit();
```

**Padding del slide:** `80px 100px 100px` (top, sides, bottom). Los 100 px inferiores se reservan para el footer absoluto. Los 80 px superiores dejan espacio para el pagenum absoluto.

**Grids:**

- `two-col`: `1fr 1fr` con gap 80 px.
- `three-col`: `1fr 1fr 1fr` con gap 56 px.
- `four-col`: `repeat(4, 1fr)` con gap 36 px.
- `six-col`: `repeat(3, 1fr)` × 2 filas con gaps 40/60 px.

**Ningún grid lleva `flex: 1`.** Los grids se autoajustan a la card más alta. La centralización vertical entre título y footer la hace un wrapper `.slide-body` (ver Components).

**Escala de spacing** (usar tokens `spacing.*`):
- `xs 4 / sm 8 / md 16 / lg 32 / xl 56 / 2xl 80 / 3xl 100`.

---

## Elevation & Depth

El sistema es **casi plano**. La profundidad se transmite mediante capas tonales (slide blanco sobre divider de sección lavanda sobre viewport neutro), no con sombras.

La única sombra permitida:

```css
box-shadow: 0 20px 60px rgba(11,22,32,0.12);
```

Aplicada **solo** al stage para que el slide visualmente flote sobre el color del viewport. Dentro de los slides, cada card y tabla es plana; la profundidad viene del tono de fondo (`bg-soft`, `bg-section`, `bg-warm-soft`, `bg-cool-soft`).

Sin sombras en cards. Sin hover lift. Sin layered cards. Si hay que separar dos regiones, cambiar el tono de fondo o agregar un border 1 px `line`, no una sombra.

---

## Shapes

Mayormente suave, nunca pillow-y.

- **Cards: `rounded.lg` = 18 px.** Generoso pero no jugado.
- **Callouts: `rounded.sm` = 4 px** (rectangulares, con borde izquierdo de 6 px en `tertiary`).
- **Pills (tags, controles de nav): `rounded.pill` = 999 px.**
- **Tablas: 0 px** (esquinas duras).
- **Stage: 0 px** (la sombra resuelve la separación, no hace falta redondear).

No mezclar shapes redondeadas y sharp en una misma visualización a menos que sea intencional (ej. terminus en pill sobre un eje sharp en una timeline).

---

## Components

### slide-body (wrapper de centrado vertical)

Cada slide de contenido (no cover, no section divider, no panel-split) recibe un wrapper `.slide-body` inyectado al cargar. Toma todo lo que está entre el H2 y el footer/pagenum y usa `margin: auto 0` para centrar el bloque verticalmente.

```js
document.querySelectorAll('.slide').forEach(s => {
  if (s.classList.contains('cover') || s.classList.contains('section')) return;
  if (s.querySelector('.panel-split')) return;
  const title = s.querySelector('h2.h');
  if (!title) return;
  const wrapper = document.createElement('div');
  wrapper.className = 'slide-body';
  let cur = title.nextElementSibling;
  while (cur && !cur.classList.contains('pagenum') && !cur.classList.contains('footer')) {
    const node = cur;
    cur = cur.nextElementSibling;
    wrapper.appendChild(node);
  }
  title.after(wrapper);
});
```

```css
.slide-body { display: flex; flex-direction: column; margin: auto 0; width: 100%; }
```

### card

Token mapping:

```yaml
card:
  backgroundColor: "{colors.bg-soft}"
  rounded: "{rounded.lg}"
  padding: "32px 32px 28px"
```

Cada card lleva opcionalmente un `.tier-tag` (uppercase 14 px en tertiary), un `h4` (26 px 700) y body text (18 px). Variantes:

- `card-warm`: fondo `bg-warm-soft`, borde izquierdo `6px solid accent-orange`.
- `card-cool`: fondo `bg-section`, borde izquierdo `6px solid accent-magenta`.

### callout

```yaml
callout:
  backgroundColor: "{colors.bg-section}"
  rounded: "{rounded.sm}"
  padding: "28px 36px"
  borderLeft: "6px solid {colors.tertiary}"
```

Para pull-quotes, beats narrativos, framing importante. Body interior 22 px 500.

### num-list (lista numerada)

Grid de items donde cada uno tiene un numeral pequeño (18 px 500), un título bold (28 px 700), y una descripción (18 px 400) en una segunda fila. El elemento signature del sistema; reemplaza las listas con bullets clásicas en la mayoría de slides.

### pill / pill-red

Chips redondeados (radio 999 px). Pill es neutral (fondo `bg-soft`, texto ink). Pill-red lleva un tinte rojo transparente y texto tertiary — usado para estados activos o para etiquetar roles de actor.

### footer

```html
<div class="footer">
  <div class="logo"><svg>...</svg></div>
  <div class="sep"></div>
  <div class="tag">CoE de Diseño de Experiencias</div>
</div>
```

Absolutamente posicionado abajo-izquierda (`left: 100px; bottom: 50px`). Logo 115 px de ancho, separador de 1 px en gris, texto del footer-tag a la derecha. El SVG del logo se inyecta vía JS desde una constante única, no se duplica en el markup.

El `tag` es configurable por deck — típicamente `CoE de Diseño de Experiencias`, pero puede ajustarse a texto específico del proyecto cuando el deck representa un workstream particular.

### pagenum

Absolutamente posicionado arriba-derecha (`right: 100px; top: 60px`). Contenido dinámico seteado al cargar vía JS basado en el orden de slides — nunca hardcoded, así inserción/borrado de slides no rompe la numeración.

```js
slides.forEach((s, i) => {
  const p = s.querySelector('.pagenum');
  if (p) p.textContent = String(i + 1).padStart(2, '0') + ' / ' + String(total).padStart(2, '0');
});
```

---

## Do's and Don'ts

**Do:**
- Aplicar el gradiente a una frase por título — la frase que carga la tesis del slide.
- Cerrar cada título con punto. Es editorial, no casual.
- Setear el page number dinámicamente desde JS, nunca hardcoded.
- Inyectar el logo desde una constante SVG única; referenciarla en cada footer.
- Centrar contenido verticalmente usando el wrapper `.slide-body`.
- Mantener cards de igual altura dejando que el grid lo resuelva (sin `flex: 1`).
- Verificar 16:9 en al menos 3 viewports antes de entregar.
- Usar `{colors.tertiary}` para celdas enfáticas en tablas y para el borde izquierdo de callouts.
- Preferir `num-list` sobre listas con bullets para cualquier contenido tipo "N razones / N pasos".
- Si se incluyen íconos en cards, mantenerlos discretos (peso visual bajo) y con significado (categoría, estado, dirección).

**Don't:**
- No aplicar el gradiente a texto de cuerpo ni a títulos completos — pierde significado al sobreusarse.
- No usar `display: none` para cambiar de slide. Rompe el wrapper `.slide-body`. Usar `visibility + opacity + pointer-events`.
- No poner `flex: 1` en grids. Las cards se inflan y pierden densidad de card.
- No mezclar sombras de card, hover lifts o elevaciones en capas. El sistema es plano por diseño.
- No usar arrow-head markers (`marker-end`) en curvas SVG — algunos renderers producen artefactos feos. Usar un pequeño dot terminus en su lugar.
- No poner 6+ children dentro de una sola card. Partir en dos slides.
- No usar Inter, Roboto o system-ui como fallback. Manrope o nada — cargar de Google Fonts.
- No hardcodear page numbers como `12 / 25` — el JS los setea dinámicamente.
- No cambiar el logo de marca por deck. El logo Rimac es la marca del equipo; permanece a menos que el deck sea co-branded con un partner, en cuyo caso ambos logos conviven.

---

## Extra 1 · Slide templates (HTML)

Patrones de layout que se montan sobre los componentes. No son parte de la spec canónica de 8 secciones pero son necesarios para construir un deck real.

### Cover

```html
<section class="slide cover active">
  <div class="cover-eyebrow reveal">CONTEXTO · ETIQUETA SUPERIOR</div>
  <h1 class="reveal">Título principal con <span class="grad">palabra clave</span><br>en dos o tres líneas.</h1>
  <p class="sub reveal">Subtítulo con una o dos oraciones que describen el deck.</p>
  <div class="meta reveal">Documento de trabajo · v0.X<br>Fecha</div>
  <div class="footer">...</div>
</section>
```

### Section divider

```html
<section class="slide section">
  <div class="section-num reveal">01 — Parte uno</div>
  <h1 class="reveal">Título de la sección<br>en <span class="grad">dos líneas</span>.</h1>
  <p class="sublabel reveal">Frase de bajada explicando qué se cubre.</p>
  <div class="footer">...</div>
</section>
```

Background `bg-section`, `justify-content: center`, H1 a 140 px.

### Content (default)

```html
<section class="slide">
  <div class="eyebrow reveal">Etiqueta breve sobre el título</div>
  <h2 class="h reveal">Título con <span class="grad">énfasis</span> selectivo.</h2>
  <!-- todo lo siguiente se envuelve en .slide-body por JS -->
  <div class="two-col reveal">...</div>
  <div class="callout reveal">...opcional...</div>
  <div class="pagenum">XX / XX</div>
  <div class="footer">...</div>
</section>
```

### Panel-split (slide partido en dos planos)

```html
<section class="slide">
  <div class="panel-split">
    <div class="panel-left reveal">
      <div class="eyebrow">Etiqueta</div>
      <h2>Título principal con <span class="grad">énfasis</span>.</h2>
      <p>Cuerpo explicativo.</p>
    </div>
    <div class="panel-right reveal">
      <h2>Subtítulo de la derecha</h2>
      <div class="num-list">...</div>
    </div>
  </div>
</section>
```

El JS de slide-body excluye este slide automáticamente (detecta `.panel-split`).

---

## Extra 2 · Patrones de visualización

Patrones gráficos reutilizables con uso consistente de tokens.

### Tabla comparativa con flechas

Dos productos / dos enfoques a través de N filas. Grid `220px | 1fr | 56px | 1fr`. Flecha horizontal en cápsula sobre el lado A (beneficios transversales), flecha vertical SVG superpuesta entre los lados (escalonamiento). Backgrounds suaves de celda (`bg-warm-soft` / `bg-cool-soft`), no gradientes fuertes en headers.

### Curvas de activación

N curvas saliendo de un mismo punto de gatillo, cada una alcanzando una altura distinta. Curvas Bezier en colores escalonados desde `#FFC09F` (más baja) pasando por `accent-orange`, `tertiary`, hasta `accent-magenta` (más alta). Línea vertical punteada del gatillo en `tertiary`. Labels alineadas a la derecha con título + sub.

### Cost stack + return motors

Stack de costos (5 bandas en escala de grises `#6B7280 → #0B1620`) a la izquierda. 2 cards de motor a la derecha con headers en gradiente. Curvas suaves los conectan — **sin arrow-head markers**, solo un dot terminus pequeño. Lección aprendida a las malas: el render de `marker-end` SVG es inconsistente entre motores.

### Diagrama orbital

Nodo central + N nodos periféricos + 3 anillos concéntricos + spokes. Dots de acento en colores del gradiente en los puntos cardinales. Descripciones laterales que matchean la posición espacial de cada nodo y **no repiten el nombre del actor** — el nombre vive en el nodo del SVG.

### Dot grid

Grid N × M de círculos de 36 px coloreados por subgrupo. Leyenda debajo en cards con swatch + nombre + count + descripción breve.

### Venn (3 dimensiones)

3 círculos con `fill-opacity: 0.72` y `mix-blend-mode: multiply`. Labels centradas en el área exclusiva de cada círculo (no en intersecciones). Pill negro al centro para la palabra de síntesis.

### Timeline con ventanas

Eje horizontal, 3 rectángulos de banda coloreados marcando fases, 3 cards debajo con bordes izquierdos matching. Mapea outcomes a ventanas temporales.

---

## Extra 3 · Motion

```css
@keyframes riseIn {
  from { transform: translateY(24px); opacity: 0; }
  to   { transform: translateY(0); opacity: 1; }
}
.slide.active .reveal { animation: riseIn 0.7s cubic-bezier(0.22, 1, 0.36, 1) both; }
.slide.active .reveal:nth-child(1) { animation-delay: 0.05s; }
/* ... hasta :nth-child(6) a 0.55s */

@media (prefers-reduced-motion: reduce) {
  .slide.active .reveal { animation: none !important; }
  .slide { transition: none !important; }
}
```

Cada elemento visible en un slide fresco lleva clase `reveal`. Delays staggered en 0.05 / 0.15 / 0.25 / 0.35 / 0.45 / 0.55 s.

---

## Extra 4 · Navegación e interactividad

| Tecla | Acción |
|---|---|
| `→`, `Space`, `PageDown` | Siguiente slide |
| `←`, `PageUp` | Slide anterior |
| `Home` | Primera slide |
| `End` | Última slide |
| `E` | Toggle modo edición (contenteditable) |
| Touch swipe | Navegación en móvil |

UI de nav es una pill negra posicionada fuera del stage. No aparece en exports a PDF.

Modo edición flip `contentEditable` en titulares, párrafos, tablas y elementos clave.

---

## Extra 5 · Convenciones editoriales

**Estructura narrativa** (la cantidad varía por proyecto):
1. Cover
2. Mapa del documento
3. Pregunta o contexto abridor
4. Section divider 01
5. Bloque parte 01 (slides de contenido)
6. Section divider 02
7. Bloque parte 02
8. Section divider 03 — Cierre
9. Cierre / recomendaciones
10. Preguntas abiertas

Decks cortos pueden saltar los section dividers por completo.

**Lenguaje en titulares:** enunciados completos con punto final; gradiente en la palabra clave; evitar siglas.

**Lenguaje en cuerpos:** tono confiado pero no comercial; decimal con coma; rangos con guión-em (5–15); comillas curvas españolas en citas literales; negritas para subrayar el verbo o sustantivo clave.

---

## Extra 6 · Compatibilidad

Este DESIGN.md sigue la [especificación open-source de Google Stitch DESIGN.md](https://github.com/google-labs-code/design.md) (Apache 2.0, alpha). El YAML front matter es legible por máquina para cualquier agente que soporte la spec; el cuerpo Markdown es legible por humanos en cualquier editor.

Compatibilidad verificada con:

- Skill `frontend-slides` (Claude / Anthropic) — pasar este archivo como referencia de design al generar nuevos decks.
- Claude Code — referenciar desde `CLAUDE.md` como "Siga reglas visuales de `@DESIGN.md`".
- Cursor — incluir en `.cursor/rules/*.mdc`.
- Google Stitch — import directo (UI nativa).
- Cualquier LLM como contexto markdown plano.

Validación:

```
npx @google/design.md lint DESIGN.md
```

---

## Extra 7 · Checklist antes de entregar un deck

- [ ] Stage 16:9 verificado en 1920×1080, 1280×720 y 1024×768.
- [ ] `flex-shrink: 0` en `.stage`.
- [ ] Logo inyectado vía JS en cada footer (no duplicado en HTML).
- [ ] Pagenum dinámico — recuenta correcto tras inserción/borrado.
- [ ] Wrapper `.slide-body` centra contenido verticalmente.
- [ ] Cover, section dividers y panel-split excluidos del wrapper.
- [ ] Gradiente aplicado solo a frases clave (audit slide por slide).
- [ ] Manrope cargada (`<link>` a Google Fonts presente).
- [ ] Modo edición (`E`) funcional.
- [ ] Navegación con teclado + touch funciona.
- [ ] Sin `display: none` en slides.
- [ ] Sin `flex: 1` en grids.
- [ ] Versión y fecha de cover actualizadas.
- [ ] Footer-tag seteado apropiadamente para el contexto del deck.

---

## Extra 8 · Lo que falta para próximas iteraciones

- **Export a PDF** con animaciones congeladas (Playwright captura cada slide; falta empaquetar en un script reutilizable).
- **Modo presentador** con notas en pantalla secundaria.
- **Inserción de imágenes raster** dentro de slides (el sistema asume hoy contenido 100% vectorial / tipográfico).
- **Variantes oscuras** del tema (todos los slides asumen fondo claro).
- **Librería estandarizada de íconos** SVG inline (hoy los íconos se incrustan ad-hoc cuando se usan).

---

*Si el doc se desactualiza respecto al HTML que lo implementa, el código manda — actualizar este archivo para sincronizarlo.*
