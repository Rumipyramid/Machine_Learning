---
name: rimac-slides
description: Genera presentaciones HTML 16:9 on-brand del CoE Diseño Estratégico de Rimac, regidas por un único design.md de tres capas (marco bloqueado + una idea por slide + corazón libre). Úsalo cuando el usuario quiera armar una presentación, un deck, slides para una charla/pitch interno, o convertir un PPT a HTML con la identidad Rimac. NO hay descubrimiento de estilos: hay una sola marca y design.md la define entera.
---

# Rimac Slides

Genera presentaciones HTML sin dependencias, ricas en animación, que corren enteras en el navegador — **siempre en la identidad Rimac**. La marca no se elige ni se descubre: vive en [design.md](design.md), la única ley de diseño. El skill **diseña la composición** de cada slide a medida; **no rellena un catálogo de moldes**.

## Principios rectores

1. **Cero dependencias** — Un único archivo HTML con CSS/JS inline. Sin npm, sin build.
2. **Mostrar, no contar** — Antes de generar el deck completo, previsualiza **la marca aplicada** en un slide de muestra para que el usuario confirme. (No es un menú de estilos: es la misma marca, vista una vez.)
3. **Distinción por calidad, no por formato** — Nada de "AI slop". La distinción NO viene de cambiar fuente/color/tema (bloqueados) ni de forzar un layout distinto por slide, sino de **la calidad con que el corazón de cada slide explica su idea**. Marcos repetidos están bien; lo que no se repite es la pereza. Ver §Estética.
4. **Brand-Locked Source** — `design.md` es la única ley de diseño. **Léelo completo y SIEMPRE** antes de generar. No existen índices de estilo, presets ni plantillas que descubrir. Si dudás de un color, una fuente, un tamaño o un gesto de movimiento, la respuesta está en `design.md` — nunca la inventes.
5. **Stage fijo 16:9 (NO NEGOCIABLE)** — Todo deck usa un lienzo de 1920×1080 escalado como un todo al viewport. Los slides se mantienen 16:9 en cualquier pantalla, incluido el teléfono. Nunca reflowear el contenido para que entre en el dispositivo.

## Estética: variedad = calidad del corazón, no novedad de formato

Tendés a converger hacia salidas genéricas y "on distribution" — el aspecto "AI slop". Acá el antídoto **no** es elegir tipografías o paletas nuevas (la marca Rimac está bloqueada en `design.md`) **ni forzar un layout distinto por slide**. El antídoto es **elevar la calidad con que el corazón de cada slide explica su idea**. La marca trabaja en **tres capas** (design.md §Overview):

- **Marco (bloqueado)** → título en la franja superior, footer + branding siempre, paleta disciplinada, estética plano-seria, stage y motion. Viene de `design.md`; **marcos repetidos están bien** — la uniformidad da marca.
- **Una idea por slide** → cada slide transmite **un único mensaje**, sintetizado en el título (voz corporativa de síntesis, **sin punto final**, no creativo-publicitario). Si hay dos ideas, son dos slides.
- **El corazón (libre)** → acá vive la calidad. Elegí el tratamiento por la **naturaleza de la idea** (rúbrica, design.md §El corazón del slide): texto-líder / mixto / diagrama / dato / visual. **Nunca default-ear a viñetas.** El visual **explica, no decora**. **Animá para revelar el argumento** (build-up por pasos), anclado en el token de motion (`riseIn`, stagger), respetando `prefers-reduced-motion`.

Evitá los clichés de AI slop que **además** contradicen Rimac: hero genérico, glassmorphism gratuito, sombras sin propósito (Rimac es "casi plano"), y sobre todo el **corazón perezoso** (texto + viñetas cuando la idea pedía una visualización). Ver §Guardarraíles anti-slop.

> Regla mental: la pregunta por slide **no** es "¿se ve distinto al anterior?" sino **"¿esta es la mejor manera de explicar esta idea?"**. La consistencia la garantizan los tokens y el marco; tu trabajo es la calidad del corazón.

**Técnica del corazón:** SVG/CSS/WAAPI permitidos para visualizaciones que **expliquen** (no decoren); Canvas solo como último recurso (raster: borroso al escalar, fuera del PDF y del editor inline, exige cargar la fuente a mano). Preferí **vanilla JS** sobre frameworks; si usás uno, inlinéalo (cero-dependencia, sin CDN). Toda animación con el **easing** de marca (`cubic-bezier(.22,1,.36,1)`); la duración se adapta al gesto. Respetá `prefers-reduced-motion` (en WAAPI, chequealo en JS). Verificá en screenshots. **La animación degrada con gracia:** un solo deck — construí cada corazón animado con el **estado final legible sin JS** + `prefers-reduced-motion` → el mismo archivo sirve estático (PDF/impresión) y animado (en vivo); el gate es **por slide vía rúbrica**, no una fase global de "animar al final". Confiabilidad para compartir = **embeber** (single-file, base64), no des-animar. Referencia de técnica de corazones animados: [examples/lab-vanilla.html](examples/lab-vanilla.html).

## Reglas del stage fijo

Invariantes que aplican a TODO slide de TODO deck:

- Todo deck tiene un wrapper de viewport que llena la ventana del navegador.
- Todo slide se autora dentro de un stage fijo de 1920×1080.
- El stage escala uniformemente para entrar en el viewport. Puede hacer letterbox/pillarbox; **nunca** re-layout del contenido.
- No usar breakpoints responsive para reacomodar el contenido del slide en teléfonos.
- Usar medidas internas fijas a tamaño de diseño 1920×1080.
- La visibilidad del slide se controla con `.active` / `.visible` vía `visibility`, `opacity` y `pointer-events` (ver [viewport-base.css](viewport-base.css)). **Nunca `display:none` / `display:block`** para conmutar slides — clases de layout posteriores (`.slide-content{display:flex}`) lo sobrescriben y muestran todos los slides a la vez.
- Usar `clamp()` solo para UI fuera del stage, o para previews pequeños donde un stage completo no es práctico.
- Incluir soporte `prefers-reduced-motion`.
- Nunca negar funciones CSS directamente (`-clamp()`, `-min()`, `-max()` se ignoran en silencio) — usar `calc(-1 * clamp(...))`.

**Al generar, leé `viewport-base.css` e incluí su contenido completo en cada presentación.**

### Modos de densidad de contenido

Preguntá al usuario si es principalmente un deck de **lectura** o de **exposición**, y diseñá según la respuesta:

| Modo | Para | Comportamiento de diseño |
| --- | --- | --- |
| **Baja densidad / orador** | Charlas, keynote, explicación en vivo | Una idea por slide, tipo grande, jerarquía fuerte, mucho aire, 1–3 elementos/ideas máx, más slides si hace falta |
| **Alta densidad / lectura** | Reportes, handouts, revisión async, docs internos | Slides autocontenidos, grillas/tablas/anotaciones estructuradas, 4–8 elementos o 4–6 tarjetas cuando sea legible (viñetas: último recurso, no el primero), spacing más ajustado pero intencional |

Límites base siempre: sin scroll, sin overflow, sin paneles solapados, sin texto por debajo de un tamaño cómodo de lectura. Si el contenido excede el modo, **dividí en más slides** en vez de encoger hasta apretar.

---

## Fase 0: Detectar modo

Determiná qué quiere el usuario:

- **Modo A: Nueva presentación** — Crear desde cero. Ir a Fase 1.
- **Modo B: Conversión PPT** — Convertir un .pptx. Ir a Fase 4.
- **Modo C: Mejora** — Mejorar un HTML existente. Leerlo, entenderlo, mejorar. Seguir las reglas de modificación de abajo.

### Modo C: Reglas de modificación

Al mejorar presentaciones existentes, el ajuste al stage fijo es el riesgo mayor:

1. **Antes de añadir contenido:** contar elementos existentes, chequear contra límites de densidad.
2. **Añadir imágenes:** que entren en el lienzo 1920×1080. Si el slide ya está lleno, dividir en dos.
3. **Añadir texto:** máx. 4–6 elementos por slide (viñetas solo si la idea lo pide; nunca por defecto). ¿Excede? Dividir en slides de continuación.
4. **Tras CUALQUIER cambio, verificar:** el stage sigue 16:9, ningún texto desborda su tarjeta, ningún panel se solapa, y los screenshots se ven bien a 1280×720 y en un viewport de teléfono.
5. **Reorganizar proactivamente:** si los cambios van a causar overflow, dividir automáticamente e informar al usuario. No esperar a que lo pidan.

---

## Fase 1: Descubrimiento de contenido (nuevas presentaciones)

**Hacé TODAS las preguntas juntas** para que el usuario complete todo de una. Si el entorno tiene una UI estructurada de preguntas, usala; si no, una sola mensaje conciso con opciones numeradas:

1. **Propósito** — ¿Para qué es? Pitch / Enseñanza-tutorial / Charla / Presentación interna.
2. **Largo** — ¿Cuántos slides aprox.? Corto 5–10 / Medio 10–20 / Largo 20+.
3. **Contenido** — ¿Tenés el contenido listo? Todo listo / Notas sueltas / Solo el tema.
4. **Densidad** — ¿Qué tan denso? Baja densidad / orador · Alta densidad / lectura.

**No preguntes por la edición inline en esta fase.** Se incluye por defecto tras el borrador, salvo que el usuario pida un archivo bloqueado/solo-export.

Recordá la densidad elegida: afecta cantidad de slides, escala tipográfica, texto por slide y ritmo.

Si el usuario tiene contenido, pedile que lo comparta.

### Paso 1.2: Evaluación de imágenes (si las hay)

Si no hay imágenes → saltar a Fase 2.

Si el usuario da una carpeta de imágenes:

1. **Escanear** — listar archivos (.png, .jpg, .svg, .webp…).
2. **Inspeccionar cada una** — usar la capacidad de comprensión de imágenes. Si no está disponible, usar nombres/metadata y preguntar solo si hace falta.
3. **Evaluar** — para cada una: qué muestra, USABLE o NO (con motivo), qué concepto representa, colores dominantes. Recordá que las fotos en slides de contenido son válidas y deseables para variedad (design.md, capa libre).
4. **Co-diseñar el outline** — las imágenes curadas informan la estructura junto con el texto. Diseñar alrededor de ambos desde el inicio.
5. **Confirmar el outline** con la UI estructurada: "¿Este outline e imágenes se ven bien?" Looks good / Ajustar imágenes / Ajustar outline.

> **Logo y marca:** el logo, las fuentes, los colores y todos los elementos bloqueados **provienen de `design.md` y sus assets** (`assets/logo-rimac.svg` inline, fuentes en `assets/fonts/`). No se generan variantes de marca ni se embebe el logo en "opciones de estilo": hay una sola marca.

---

## Fase 2: Brand Preview (confirmación de marca)

Esta fase reemplaza al viejo "descubrimiento de estilos". **No hay 3 opciones, ni presets, ni wildcard, ni elección de vibe.** Hay una marca: Rimac.

### Paso 2.0: Cargar la marca y previsualizarla

1. **Leé [design.md](design.md) completo.** Es la única ley de diseño: tokens (front matter machine-readable = marco bloqueado) + prosa (la rúbrica del corazón, Principio de variedad, checklist). Internalizá el modelo de **3 capas** (marco / una idea por slide / corazón), color, tipografía (Opción B: una familia por peso), **voz del título** (corporativa de síntesis, sin punto final), portada, footer, logo y el token de motion.
2. **Generá UN slide de muestra** fiel a la capa bloqueada (la portada, o un slide representativo del contenido del usuario) para que confirme que la marca se ve correcta — fuentes que cargan de verdad, logo, footer, gradiente/rojo como acento. Guardalo en `.rimac-slides/preview/` y abrilo.
3. Preguntá: "¿La marca se ve correcta para arrancar?" Sí, generá / Ajustá algo puntual.

### Reglas de higiene del preview (NO NEGOCIABLES)

- El preview debe verse como un primer slide real del deck del usuario, no como una tarjeta de diagnóstico.
- **Nunca** renderizar texto interno de workflow en un slide: nada de "preview", "generado desde", "template", "preset", "Opción A/B/C", nombres de archivo, rutas o etiquetas de proceso.
- Si el slide necesita chrome, usá solo chrome real del deck: título, sección, fecha, autor, organización, número de página, o una frase genuina del material del usuario.
- Antes de abrir el preview, inspeccioná el texto visible y corregí si aparece cualquier metadata interna.

---

## Fase 3: Generar presentación

Generá el deck completo con el contenido de Fase 1 (texto, o texto + imágenes curadas) y la marca de `design.md`.

**Antes de generar, leé estos archivos de soporte:**

- [design.md](design.md) — **la única ley de diseño.** Releela: tokens (marco bloqueado) + la rúbrica del corazón, Principio de variedad y semillas de composición (capa libre). Es la fuente de verdad de TODO lo visual.
- [viewport-base.css](viewport-base.css) — CSS obligatorio del stage fijo (incluir completo en el `<style>`).
- [html-template.md](html-template.md) — arquitectura HTML, controlador JS, edición inline. Los valores del `:root` y de `.reveal` deben venir de los tokens de `design.md`.
- [animation-patterns.md](animation-patterns.md) — registro de motion Rimac y técnicas de animación on-brand.

**Tratá `design.md` como la receta única:**

- Preservá sus fuentes, paleta, vocabulario decorativo, ritmo de spacing y gramática de componentes = **capa bloqueada**. Cópiala tal cual.
- **Diseñá el corazón de cada slide a medida** = **capa libre**, eligiendo el tratamiento por la **naturaleza de la idea** (rúbrica, design.md §El corazón del slide): texto-líder / mixto / diagrama / dato / visual. **Una idea por slide.** **Nunca default-ear a viñetas** (último recurso, no el primero). El visual **explica, no decora**. Marcos repetidos están bien (Principio de variedad: **calidad, no formato**); lo que no se repite es un corazón genérico cuando la idea pedía una visualización.
- Generá todo como **stage fijo 1920×1080** escalado uniformemente. Traducí cualquier proporción a coordenadas del stage 1920×1080; no dejes reflow responsive.
- Single-file autocontenido. Aplicá la densidad elegida. No dejes que la alta densidad degenere en clutter: si un slide desborda, dividilo o rediseñalo.

**Requisitos clave:**

- Un único archivo HTML autocontenido, todo CSS/JS inline.
- Incluí el contenido COMPLETO de `viewport-base.css` en el `<style>`.
- **Fuentes vía `@font-face` local / base64** desde `assets/fonts/` — **BRSonoma NO está en Google Fonts**, jamás cargarla de ahí (caería a Helvetica). Para un deck portable, embebé en base64 (ver `scripts/pack-assets.py` y design.md §Notas técnicas).
- Comentarios detallados explicando cada sección, con bloques `/* === NOMBRE === */`.
- Verificá overflow de contenido y solape de paneles en screenshots renderizados, no solo `scrollHeight`.

---

## Fase 4: Conversión PPT

Al convertir PowerPoint:

1. **Extraer contenido** — `python scripts/extract-pptx.py <input.pptx> <output_dir>` (instalar `pip install python-pptx` si hace falta).
2. **Confirmar con el usuario** — presentar títulos, resúmenes y conteo de imágenes extraídos.
3. **Aplicar la marca Rimac** — ir a Fase 2 (Brand Preview) para cargar `design.md`. **No hay selección de estilo:** el contenido entra, la marca Rimac sale. La conversión re-renderiza el contenido on-brand; no es una fotocopia visual del PPT.
4. **Generar HTML** — convertir preservando todo el texto, imágenes (de assets/), orden de slides y notas del orador (como comentarios HTML).

---

## Fase 5: Entrega

1. **Limpiar** — borrar `.rimac-slides/preview/` si existe.
2. **Abrir** — `open [archivo].html` en el navegador.
3. **Resumir** — decir al usuario:
   - Ubicación del archivo, marca (Rimac · design.md), cantidad de slides.
   - Navegación: flechas, espacio, swipe/tap.
   - Qué es customizable: la **composición** (layout de cada slide). La **marca está bloqueada** por `design.md` — color, tipografía, logo, motion no se editan "para variar".
   - Edición inline disponible: hover esquina superior-izquierda o tecla `E`, click en cualquier texto, Ctrl+S para guardar.
   - Ofrecer acciones post-borrador: pedir revisiones, editar texto en el navegador, exportar/compartir.
   - Si el deck **anima corazones**, verificar que el **fallback estático** (reduced-motion / PDF) también rinde — el mismo archivo debe leerse bien quieto, no solo en vivo.

---

## Fase 6: Compartir y exportar (opcional)

Tras la entrega, **preguntá:** "¿Querés compartir esta presentación? Puedo desplegarla a una URL en vivo (funciona en cualquier dispositivo, incluido el teléfono) o exportarla a PDF."

- **Desplegar a URL** (`bash scripts/deploy.sh <ruta>`) — link compartible vía Vercel. Verificá que todas las imágenes carguen en la URL desplegada; preferí deploy de carpeta cuando haya muchos assets.
- **Exportar a PDF** (`bash scripts/export-pdf.sh <ruta-html> [salida.pdf]`) — snapshot estático vía Playwright. Las animaciones se reemplazan por su estado final. **Recordatorio Rimac:** el gradiente `background-clip:text` NO renderiza en PDF — para export, las frases que llevarían gradiente caen a color sólido `tertiary` (#F7052D). Ver design.md §Notas técnicas.
- Si el PDF supera ~10MB, ofrecer recomprimir con `--compact` (1280×720).

Si el usuario declina, parar acá.

---

## Guardarraíles anti-slop (rescatados, agnósticos de marca)

Refuerzan "el skill DISEÑA, no rellena moldes". Aplican **además** de la marca de design.md:

**Fuentes a evitar como display:** Inter, Roboto, Arial, fuentes de sistema. *(En Rimac la display es Rimac Display para portada y BRSonoma para todo lo demás — vienen de design.md.)*

**Colores a evitar:** `#6366f1` (índigo genérico), gradientes morados sobre blanco. *(La paleta Rimac está en design.md; el único gradiente oficial es `hero` naranja→rojo→magenta.)*

**Layouts a evitar:** todo centrado, hero sections genéricas, grillas de tarjetas idénticas.

**Decoraciones a evitar:** ilustraciones realistas, glassmorphism gratuito, sombras sin propósito. *(Rimac es "casi plano": la única sombra permitida es la del stage; sin hover-lift, sin cards elevadas, sin tilt 3D.)*

**Gotcha CSS — negar funciones:** `right: -clamp(...)` se ignora en silencio (sin error de consola). Usar siempre `right: calc(-1 * clamp(...))`.

---

## Archivos de soporte

| Archivo | Propósito | Cuándo leer |
| --- | --- | --- |
| [design.md](design.md) | **La única ley de diseño** — 3 capas: marco bloqueado (tokens) + una idea por slide + corazón libre (la rúbrica, Principio de variedad) | **Siempre y completo** antes de generar (Fase 2 y 3) |
| [viewport-base.css](viewport-base.css) | CSS obligatorio del stage fijo — copiar entero en cada deck | Fase 3 (generación) |
| [html-template.md](html-template.md) | Estructura HTML, controlador JS, edición inline | Fase 3 (generación) |
| [animation-patterns.md](animation-patterns.md) | Registro de motion Rimac y técnicas de animación | Fase 3 (generación) |
| [scripts/pack-assets.py](scripts/pack-assets.py) | Empaqueta fuentes (.ttf→woff2 base64) e imágenes para decks portables | Fase 3/5 (deck portable) |
| [scripts/extract-pptx.py](scripts/extract-pptx.py) | Extracción de contenido de PPT | Fase 4 (conversión) |
| [scripts/deploy.sh](scripts/deploy.sh) | Deploy a Vercel para compartir | Fase 6 |
| [scripts/export-pdf.sh](scripts/export-pdf.sh) | Export a PDF | Fase 6 |
| [examples/proof-rimac.html](examples/proof-rimac.html) | Golden-sample de la marca aplicada — **referencia visual, NO plantilla a copiar** | Consulta de QA de marca |
| [examples/lab-vanilla.html](examples/lab-vanilla.html) | Referencia de **técnica de corazones animados** (count-up, loop, build-up palabra-x-palabra, ciclo activate/deactivate) + receta single-file embebido (fuentes base64, 0 deps, degradación con `prefers-reduced-motion`) — **referencia de técnica, NO plantilla** | Al animar un corazón (Fase 3) |
