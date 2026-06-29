---
name: presentaciones-rimac
description: >-
  Crea presentaciones, decks, slides o diapositivas con el sistema de diseño
  "Editorial Presentations" del CoE de Diseño de Experiencias de Rimac: HTML 16:9
  (stage de 1920×1080), tipografía Manrope, estética editorial sobria con un único
  gradiente cálido como acento, y exportación a PDF vectorial. Usa esta skill
  SIEMPRE que el usuario quiera crear, armar, diseñar, maquetar o exportar una
  presentación, deck, slides, diapositivas o "ppt" — especialmente si menciona
  Rimac o el CoE de Diseño de Experiencias — aunque no nombre la skill
  explícitamente. También aplica para convertir un texto, guion o documento en un
  deck con esta identidad visual.
---

# Presentaciones Rimac · Editorial Presentations

Sistema para producir presentaciones HTML que respetan la identidad visual del CoE
de Diseño de Experiencias de Rimac, y exportarlas a PDF vectorial de alta fidelidad.

## Recursos de esta skill

| Recurso | Qué es | Cuándo usarlo |
|---|---|---|
| `references/design.md` | El sistema de diseño completo (colores, tipografía, componentes, do's & don'ts). **Es la fuente de verdad.** | **Léelo SIEMPRE antes de construir.** Contiene el detalle que este SKILL.md solo resume. |
| `assets/logo-rimac.svg` | El logo oficial de Rimac en vectorial. | Se inyecta en el footer de cada slide. |
| `scripts/export_pdf.js` | El exportador HTML → PDF (Playwright + pdf-lib). | Para generar el PDF final. |

## Flujo de trabajo

1. **Lee `references/design.md`.** No saltes este paso: define los tokens exactos
   (colores, escala tipográfica, spacing, componentes) y las reglas editoriales.
   Este SKILL.md resume lo crítico, pero el design.md manda.
2. **Construye el HTML** de la presentación partiendo del esqueleto de más abajo,
   creando un `<section class="slide">` por diapositiva.
3. **Verifica visualmente** antes de exportar (abre el HTML o toma una captura).
4. **Exporta a PDF** con `scripts/export_pdf.js` (ver sección *Exportar*).

## Reglas de diseño esenciales (resumen — el detalle vive en design.md)

- **Tipografía:** Manrope (Google Fonts), pesos 400–800. Nunca uses Inter/Roboto/system-ui como fallback. Títulos en 800, subtítulos/tags en 700, footer/pagenum en 500, cuerpo en 400. Evita el peso 600.
- **Color:** lienzo blanco; lavanda `#ECEEFC` solo para section dividers. Tinta `#0B1620` para titulares. Rojo de marca `#F7052D` solo para logo, borde de callouts y celdas enfáticas — nunca sobre titulares ni cuerpo.
- **El gradiente cálido** (`#FF7A00 → #F7052D → #C8128B`) es el único gesto decorativo: aplícalo con `background-clip:text` a **una sola frase clave por título** (2–3 palabras). Nunca a un título completo ni al cuerpo.
- **Casi plano:** sin sombras salvo la del stage. La profundidad viene del tono de fondo de las cards (`#F5F6FB`, `#ECEEFC`, etc.), no de sombras ni hover.
- **Titulares:** enunciados completos, con punto final. Tono confiado, no comercial.
- **Cards de igual altura:** deja que el grid lo resuelva; nunca uses `flex:1` en grids.

> Para componentes (cards, callouts, num-list, tablas comparativas, diagramas) y
> los templates de slide (cover, section divider, content, panel-split), consulta
> las secciones *Components*, *Extra 1* y *Extra 2* de `references/design.md`.

## Esqueleto HTML base (compatible con el exportador)

El exportador necesita tres cosas en el HTML: un `#stage`, elementos `.slide`, y una
función global `window.show(idx)`. Este esqueleto las incluye. Pártelo y rellena los
slides; ajusta estilos según design.md.

```html
<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  :root{
    --ink:#0B1620; --text:#1F2937; --muted:#6B7280; --red:#F7052D;
    --bg-section:#ECEEFC; --bg-soft:#F5F6FB; --line:#E5E7EB;
  }
  *{margin:0;padding:0;box-sizing:border-box}
  body{font-family:'Manrope',sans-serif;color:var(--text)}
  .viewport{position:fixed;inset:0;display:flex;align-items:center;justify-content:center;background:#F2F3F7}
  .stage{width:1920px;height:1080px;min-width:1920px;min-height:1080px;flex-shrink:0;
         position:relative;transform-origin:center center;background:#fff;overflow:hidden;
         box-shadow:0 20px 60px rgba(11,22,32,.12)}
  .slide{position:absolute;inset:0;padding:80px 100px 100px;
         visibility:hidden;opacity:0;pointer-events:none;transition:opacity .35s}
  .slide.active{visibility:visible;opacity:1;pointer-events:auto}
  .slide.section{background:var(--bg-section);display:flex;flex-direction:column;justify-content:center}
  h1{font-size:116px;font-weight:800;line-height:.96;letter-spacing:-.04em;color:var(--ink)}
  h2.h{font-size:64px;font-weight:800;line-height:1.05;letter-spacing:-.025em;color:var(--ink)}
  .eyebrow{font-size:18px;font-weight:700;letter-spacing:.02em;color:var(--ink);margin-bottom:24px}
  p.sub{font-size:26px;font-weight:500;line-height:1.4;margin-top:32px;max-width:1100px}
  .grad{background:linear-gradient(90deg,#FF7A00 0%,#F7052D 45%,#C8128B 100%);
        -webkit-background-clip:text;background-clip:text;color:transparent}
  .footer{position:absolute;left:100px;bottom:50px;display:flex;align-items:center;gap:16px}
  .footer .logo svg{width:115px;height:auto;display:block}
  .footer .sep{width:1px;height:20px;background:var(--muted);opacity:.4}
  .footer .tag{font-size:14px;font-weight:500;letter-spacing:.02em;color:var(--muted)}
  .pagenum{position:absolute;right:100px;top:60px;font-size:14px;font-weight:500;
           letter-spacing:.04em;color:var(--muted)}
  .nav-controls{position:fixed;bottom:20px;left:50%;transform:translateX(-50%);
                display:flex;gap:8px;background:var(--ink);color:#fff;
                padding:10px 18px;border-radius:999px;font-size:14px;z-index:99}
</style>
</head>
<body>
<div class="viewport">
  <div class="stage" id="stage">

    <!-- COVER -->
    <section class="slide cover active">
      <div class="eyebrow">CONTEXTO · ETIQUETA SUPERIOR</div>
      <h1>Título principal con <span class="grad">palabra clave</span><br>en dos o tres líneas.</h1>
      <p class="sub">Subtítulo con una o dos oraciones que describen el deck.</p>
      <div class="footer"></div>
    </section>

    <!-- CONTENT -->
    <section class="slide">
      <div class="eyebrow">Etiqueta breve</div>
      <h2 class="h">Título con <span class="grad">énfasis</span> selectivo.</h2>
      <!-- contenido: cards, callouts, num-list, tablas (ver design.md) -->
      <div class="pagenum"></div>
      <div class="footer"></div>
    </section>

  </div>
</div>

<div class="nav-controls">← / → para navegar · E para editar</div>

<script>
  /* Logo oficial: pega aquí el contenido de assets/logo-rimac.svg */
  const LOGO_SVG = `__PEGAR_SVG_DEL_LOGO__`;

  /* Inyecta logo + separador + tag en cada footer (no duplicar en el HTML) */
  document.querySelectorAll('.footer').forEach(f => {
    f.innerHTML =
      `<div class="logo">${LOGO_SVG}</div>` +
      `<div class="sep"></div>` +
      `<div class="tag">CoE de Diseño de Experiencias</div>`;
  });

  const slides = Array.from(document.querySelectorAll('.slide'));
  const total = slides.length;

  /* Numeración dinámica (nunca hardcodear) */
  slides.forEach((s, i) => {
    const p = s.querySelector('.pagenum');
    if (p) p.textContent = String(i+1).padStart(2,'0') + ' / ' + String(total).padStart(2,'0');
  });

  /* window.show(idx): el exportador lo llama por cada slide.
     Usa visibility+opacity+pointer-events (nunca display:none). */
  let cur = 0;
  window.show = (idx) => {
    cur = Math.max(0, Math.min(total-1, idx));
    slides.forEach((s, i) => s.classList.toggle('active', i === cur));
  };

  /* Escalado uniforme a 16:9 en pantalla (el exportador lo fija a scale(1)) */
  window.fit = () => {
    const s = document.getElementById('stage');
    const k = Math.min(window.innerWidth/1920, window.innerHeight/1080);
    if (s) s.style.transform = `scale(${k})`;
  };
  window.addEventListener('resize', fit); fit();

  /* Navegación con teclado */
  addEventListener('keydown', e => {
    if (['ArrowRight',' ','PageDown'].includes(e.key)) show(cur+1);
    if (['ArrowLeft','PageUp'].includes(e.key)) show(cur-1);
    if (e.key === 'Home') show(0);
    if (e.key === 'End') show(total-1);
  });
  show(0);
</script>
</body>
</html>
```

**Nota sobre el logo:** sustituye `__PEGAR_SVG_DEL_LOGO__` por el contenido literal de
`assets/logo-rimac.svg` (todo el bloque `<svg>…</svg>`). El logo es vectorial, así que
se mantiene nítido en el PDF.

## Exportar a PDF

El exportador usa un navegador Chromium (vía Playwright) para "imprimir" cada slide y
unirlos en un PDF.

**No hace falta instalar nada a mano:** la primera vez que se ejecuta, el script instala
solo sus dependencias (Playwright + pdf-lib + el navegador Chromium, que queda en caché
para las siguientes veces). Solo córrelo:

```bash
node ~/.claude/skills/presentaciones-rimac/scripts/export_pdf.js  entrada.html  salida.pdf
```

- El HTML debe tener `#stage`, elementos `.slide` y `window.show(idx)` (el esqueleto ya los trae).
- El script convierte el texto en gradiente a imagen nítida (resuelve un bug de Chromium) y deja todo lo demás vectorial. No modifiques esa parte salvo que sepas lo que haces.

## Checklist antes de entregar

- [ ] `references/design.md` leído y aplicado.
- [ ] Manrope cargada vía `<link>` de Google Fonts.
- [ ] Gradiente solo en una frase clave por título (auditar slide por slide).
- [ ] Logo inyectado vía JS en cada footer (no duplicado en el HTML).
- [ ] Pagenum dinámico (no hardcodeado).
- [ ] Sin sombras de card ni `flex:1` en grids.
- [ ] Titulares con punto final.
- [ ] PDF exportado y revisado visualmente.
