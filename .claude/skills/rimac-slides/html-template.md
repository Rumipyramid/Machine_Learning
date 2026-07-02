# Plantilla HTML (motor de render Rimac)

Arquitectura de referencia para generar decks. Todo deck es un **stage fijo 16:9**: los slides se autoran a 1920×1080 y el stage entero escala a la ventana.

> **Los valores de marca (color, tipografía, motion) que aparecen abajo son un reflejo de [design.md](design.md), la única ley.** Si design.md y este archivo difieren, **gana design.md**. No hardcodees valores: leé los tokens de design.md y volcálos al `:root`.

## Estructura HTML base

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Título de la presentación</title>

    <style>
        /* ===========================================
           FUENTES — @font-face LOCAL / BASE64 · OPCIÓN B (una familia por peso)
           BRSonoma y Rimac Display NO están en Google Fonts. Cada peso es SU PROPIA
           familia ('BRSonoma Bold', etc.) → se usa el archivo real horneado, nunca un
           peso sintético. NO se setea font-weight; font-synthesis:none (en html,body) lo
           refuerza. Para deck portable, embeber base64 (scripts/pack-assets.py). 0 './assets/'.
           =========================================== */
        @font-face{ font-family:'BRSonoma Regular'; src:url('./assets/fonts/BRSonoma-Regular.ttf') format('truetype'); font-display:swap; }
        @font-face{ font-family:'BRSonoma Medium';  src:url('./assets/fonts/BRSonoma-Medium.ttf')  format('truetype'); font-display:swap; }
        @font-face{ font-family:'BRSonoma Bold';    src:url('./assets/fonts/BRSonoma-Bold.ttf')    format('truetype'); font-display:swap; }
        @font-face{ font-family:'BRSonoma Black';   src:url('./assets/fonts/BRSonoma-Black.ttf')   format('truetype'); font-display:swap; }
        @font-face{ font-family:'Rimac Display';    src:url('./assets/fonts/Rimac-Display.ttf')    format('truetype'); font-display:swap; }
        /* Light y SemiBold están disponibles si una idea las pide (mismo patrón). */

        /* ===========================================
           VARIABLES CSS (TOKENS) — copiados de design.md
           Esta es la capa del MARCO (bloqueado). No inventar ni "variar para sorprender".
           =========================================== */
        :root {
            /* Colores Rimac (design.md §colors) */
            --primary:        #0B1620;   /* tinta de titulares / eyebrows */
            --text:           #1F2937;   /* cuerpo */
            --secondary:      #6B7280;   /* footer-tag, pagenum, captions */
            --tertiary:       #F7052D;   /* ROJO RIMAC — logo, acento puntual */
            --neutral:        #FFFFFF;   /* fondo de slide por defecto */
            --accent-orange:  #FF7A00;   /* inicio del gradiente */
            --accent-magenta: #C8128B;   /* fin del gradiente */
            --bg-section:     #ECEEFC;   /* lavanda — dividers / respiros */
            --bg-soft:        #F5F6FB;
            --bg-warm-soft:   #FFF6EF;
            --bg-cool-soft:   #F7F8FE;
            --bg-viewport:    #F2F3F7;   /* fuera del stage */
            --line:           #E5E7EB;

            /* Gradiente oficial (design.md §gradients) */
            --grad-hero: linear-gradient(90deg, #FF7A00 0%, #F7052D 45%, #C8128B 100%);
            --grad-soft: linear-gradient(135deg, #FFEFE3 0%, #FCE4EC 100%);

            /* Fondos del stage (Rimac) */
            --stage-bg: #F2F3F7;
            --slide-bg: #FFFFFF;

            /* Tipografía (design.md §typography) — Opción B: cada peso ES su familia.
               Titulares → 'BRSonoma Bold'; lead/footer → 'BRSonoma Medium'; dato → 'BRSonoma Black'. */
            --font-display: 'Rimac Display', sans-serif;   /* SOLO cover-title */
            --font-body: 'BRSonoma Regular', 'Helvetica Neue', Helvetica, Arial, sans-serif;

            /* Motion Rimac (design.md §motion) — RITMO BLOQUEADO */
            --ease-rimac: cubic-bezier(.22, 1, .36, 1);
            --reveal-duration: 0.75s;
        }

        /* Gradiente sobre texto (1 frase clave por slide, opcional) */
        .grad{ background:var(--grad-hero); -webkit-background-clip:text; background-clip:text; color:transparent; }

        /* ===========================================
           BASE
           =========================================== */
        * { margin: 0; padding: 0; box-sizing: border-box; }
        html, body { font-family: var(--font-body); font-synthesis: none; }

        /* --- PEGAR ACÁ EL CONTENIDO COMPLETO DE viewport-base.css --- */

        /* ===========================================
           ANIMACIONES — Motion Rimac
           Se disparan vía .visible en el slide activo.
           Token bloqueado: riseIn 0.75s cubic-bezier(.22,1,.36,1), stagger 0.05→0.55s.
           =========================================== */
        .reveal {
            opacity: 0;
            transform: translateY(28px);
            transition: opacity var(--reveal-duration) var(--ease-rimac),
                        transform var(--reveal-duration) var(--ease-rimac);
        }
        .slide.visible .reveal {
            opacity: 1;
            transform: translateY(0);
        }

        /* Stagger 0.05 → 0.55s (design.md §motion). El orden de entrada debe
           REVELAR el argumento (build-up por pasos), no ser un adorno mecánico. */
        .slide.visible .reveal:nth-child(1) { transition-delay: 0.05s; }
        .slide.visible .reveal:nth-child(2) { transition-delay: 0.15s; }
        .slide.visible .reveal:nth-child(3) { transition-delay: 0.25s; }
        .slide.visible .reveal:nth-child(4) { transition-delay: 0.35s; }
        .slide.visible .reveal:nth-child(5) { transition-delay: 0.45s; }
        .slide.visible .reveal:nth-child(6) { transition-delay: 0.55s; }
    </style>
</head>
<body>
    <div class="deck-viewport">
        <main class="deck-stage" id="deckStage">
            <section class="slide active">
                <!-- Composición de portada según design.md §slide-cover -->
            </section>
            <section class="slide">
                <!-- Slide de contenido: marco fijo + corazón libre (rúbrica), tokens Rimac -->
            </section>
            <!-- Más slides... -->
        </main>
    </div>

    <script>
        /* ===========================================
           CONTROLADOR DE PRESENTACIÓN
           =========================================== */
        class SlidePresentation {
            constructor() {
                this.slides = document.querySelectorAll('.slide');
                this.currentSlide = 0;
                this.stage = document.getElementById('deckStage');
                this.setupStageScale();
                this.setupKeyboardNav();
                this.setupTouchNav();
                this.setupPagenum();   // pagenum dinámico (design.md §pagenum) — nunca hardcodeado
                this.showSlide(0);
            }

            setupStageScale() {
                const scale = () => {
                    const factor = Math.min(window.innerWidth / 1920, window.innerHeight / 1080);
                    const x = (window.innerWidth - 1920 * factor) / 2;
                    const y = (window.innerHeight - 1080 * factor) / 2;
                    this.stage.style.transform = `translate(${x}px, ${y}px) scale(${factor})`;
                };
                scale();
                window.addEventListener('resize', scale);
            }

            setupKeyboardNav() { /* flechas ← →, espacio, Home/End */ }
            setupTouchNav()    { /* swipe táctil */ }
            setupPagenum()     { /* setear .pagenum de cada slide según su orden */ }

            showSlide(index) {
                this.currentSlide = Math.max(0, Math.min(index, this.slides.length - 1));
                this.slides.forEach((slide, i) => {
                    slide.classList.toggle('active', i === this.currentSlide);
                    slide.classList.toggle('visible', i === this.currentSlide);
                });
            }
        }
        new SlidePresentation();

        /* ===========================================
           LOGO RIMAC (constante SVG, design.md §Logo Rimac)
           Inyectado por JS desde una única constante — no duplicar en markup.
           Sobre fondo oscuro (excepción), usar la variante en negativo (blanco).
           =========================================== */
        // const LOGO_SVG = `<svg ...>`;  // ver design.md §Logo Rimac para el path completo
        // document.querySelectorAll('.footer .logo, .cover-logo').forEach(el => el.innerHTML = LOGO_SVG);
    </script>
</body>
</html>
```

## Features JavaScript requeridas

Toda presentación debe incluir:

1. **Clase SlidePresentation** — controlador con:
   - Navegación por teclado (flechas, espacio, Home/End).
   - Soporte touch/swipe.
   - **Sin barra de navegación visible** (design.md §pagenum): la nav pill ocupa espacio y se omite. Navegación por teclado + swipe.
   - **Pagenum dinámico** seteado por JS según el orden de slides — nunca hardcodeado.

2. **Escalado del stage** — comportamiento 16:9 fijo:
   - Todos los slides a 1920×1080 dentro de `.deck-stage`.
   - Escalar el stage entero con un solo transform.
   - Letterbox/pillarbox según haga falta; nunca reflowear por dispositivo.

3. **Logo Rimac inyectado** — desde la constante `LOGO_SVG` única (design.md §Logo Rimac) a `.footer .logo` y `.cover-logo`. El logo es **SVG inline rojo (#F7052D)**, no un PNG ni un recorte circular. Sobre fondo oscuro (excepción §Elevation & Depth), va en **negativo (blanco, `brand.logo.color-negative`)**.

4. **Edición inline** (incluida por defecto tras el borrador):
   - Botón toggle (oculto por defecto, revelado por hover-hotzone o tecla `E`).
   - Auto-guardado a localStorage.
   - Export/guardar archivo.
   - Ver "Implementación de edición inline".

## Implementación de edición inline

Afordancia liviana post-borrador. No preguntar por ella en el Q&A previo. Incluir por defecto salvo que el usuario pida un archivo bloqueado/solo-export.

**NO usar el selector CSS `~` para mostrar/ocultar por hover.** El enfoque CSS-only (`edit-hotzone:hover ~ .edit-toggle`) falla porque `pointer-events:none` en el botón rompe la cadena de hover.

**Enfoque requerido: hover por JS con timeout de 400ms.**

HTML:
```html
<div class="edit-hotzone"></div>
<button class="edit-toggle" id="editToggle" title="Modo edición (E)">✏️</button>
```

CSS (visibilidad por clases JS):
```css
.edit-hotzone { position: fixed; top: 0; left: 0; width: 80px; height: 80px; z-index: 10000; cursor: pointer; }
.edit-toggle  { opacity: 0; pointer-events: none; transition: opacity 0.3s ease; z-index: 10001; }
.edit-toggle.show, .edit-toggle.active { opacity: 1; pointer-events: auto; }
```

JS (cuatro métodos de interacción):
```javascript
// 1. Click en el botón
document.getElementById('editToggle').addEventListener('click', () => editor.toggleEditMode());

// 2. Hover del hotzone con gracia de 400ms
const hotzone = document.querySelector('.edit-hotzone');
const editToggle = document.getElementById('editToggle');
let hideTimeout = null;
hotzone.addEventListener('mouseenter', () => { clearTimeout(hideTimeout); editToggle.classList.add('show'); });
hotzone.addEventListener('mouseleave', () => { hideTimeout = setTimeout(() => { if (!editor.isActive) editToggle.classList.remove('show'); }, 400); });
editToggle.addEventListener('mouseenter', () => clearTimeout(hideTimeout));
editToggle.addEventListener('mouseleave', () => { hideTimeout = setTimeout(() => { if (!editor.isActive) editToggle.classList.remove('show'); }, 400); });

// 3. Click directo en el hotzone
hotzone.addEventListener('click', () => editor.toggleEditMode());

// 4. Tecla E (saltar si se está editando texto)
document.addEventListener('keydown', (e) => {
    if ((e.key === 'e' || e.key === 'E') && !e.target.getAttribute('contenteditable')) editor.toggleEditMode();
});
```

## Pipeline de imágenes (saltar si no hay imágenes)

Si el usuario eligió "sin imágenes", saltar. Si hay imágenes, procesarlas antes de generar el HTML.

**Dependencia:** `pip install Pillow`

```python
from PIL import Image

# Redimensionar (para imágenes pesadas que inflan el HTML)
def resize_max(input_path, output_path, max_dim=1600):
    img = Image.open(input_path)
    img.thumbnail((max_dim, max_dim), Image.LANCZOS)
    img.save(output_path, quality=85)
```

| Situación | Operación |
|---|---|
| Imagen > 1MB | `resize_max(max_dim=1600)` |
| Aspect ratio incorrecto | Crop manual con `img.crop()` |
| Wave de portada (PNG con alpha, sobre blanco) | Exportar JPEG con matte blanco (ver `scripts/pack-assets.py`) — ~8× más liviano |

Guardar imágenes procesadas con sufijo `_processed`. Nunca sobrescribir originales.

### Colocación de imágenes (estilo Rimac)

- **El logo es SVG inline**, no un `<img>` ni un recorte circular. Inyectarlo desde la constante `LOGO_SVG`.
- **Sin `box-shadow` en imágenes ni en tarjetas.** Rimac es "casi plano" (design.md §Elevation & Depth): la profundidad viene de capas tonales, no de sombras. La única sombra permitida es la del stage.
- **Esquinas redondeadas, no circulares.** La foto de portada usa `border-radius: 28px 28px 28px 0` (todas redondeadas excepto inferior-izquierda), design.md §slide-cover.
- Para deck portable, embeber imágenes como `data:` URI (ver `scripts/pack-assets.py`). 0 ocurrencias de `./assets/` en el archivo entregado.
- Nunca repetir la misma imagen en varios slides (salvo el logo).

```css
.slide-image { max-width: 100%; max-height: 100%; object-fit: contain; border-radius: 14px; }
```

---

## Calidad de código

**Comentarios:** cada sección con comentarios claros de qué hace y cómo modificarla.

**Accesibilidad:**
- HTML semántico (`<section>`, `<nav>`, `<main>`).
- Navegación por teclado completa.
- ARIA labels donde haga falta.
- Soporte `prefers-reduced-motion` (incluido en `viewport-base.css`).

## Estructura de archivos del deck generado

```
presentacion.html    # Autocontenido, todo CSS/JS inline; idealmente assets embebidos base64
```
