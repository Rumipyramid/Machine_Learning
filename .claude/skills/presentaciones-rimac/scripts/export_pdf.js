/**
 * export_pdf.js — Exportador de presentaciones HTML a PDF
 * Sistema "Editorial Presentations" · CoE de Diseño de Experiencias · Rimac
 *
 * USO:
 *   node export_pdf.js <entrada.html> <salida.pdf>
 *
 * REQUISITOS (instalar una sola vez, dentro de la carpeta del proyecto):
 *   npm install playwright pdf-lib
 *   npx playwright install chromium
 *
 * El HTML de entrada debe seguir el sistema design.md:
 *   - Un stage de 1920×1080 con elementos .slide
 *   - Una función global window.show(idx) que activa el slide número idx
 *     (la plantilla base ya la incluye)
 *
 * ── Fix de texto en gradiente (heredado del script original v6) ──────────
 * El motor de PDF de Chromium ignora la máscara de recorte de glifos cuando
 * se usa fill="url(#gradient)" en <text> SVG: rellena todo el bounding box en
 * vez de las letras. No se arregla vía atributos SVG (es un bug de Chromium).
 *
 * Solución: renderizar el texto en gradiente a un Canvas a 2× devicePixelRatio
 * y reemplazar cada span .grad / .stat .n por un <img> inline nítido.
 * Canvas fillText() recorta el gradiente correctamente a las letras.
 * Todo lo demás (títulos, cuerpo, logo SVG, formas) permanece vectorial.
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

/* ── Auto-instala las dependencias la primera vez, si faltan ───────────────
   Así el exportador funciona en cualquier máquina o carpeta, sin pasos manuales. */
function ensureDeps() {
  try { require.resolve('playwright'); require.resolve('pdf-lib'); return; }
  catch (_) { /* faltan; las instalamos abajo */ }
  const dir = path.join(__dirname, '..'); // carpeta de la skill (tiene package.json)
  console.log('Primera vez: instalando lo que necesita el exportador (Playwright + pdf-lib)…');
  execSync('npm install', { cwd: dir, stdio: 'inherit' });
  const pw = path.join(dir, 'node_modules', '.bin', 'playwright');
  execSync(`"${pw}" install chromium`, { cwd: dir, stdio: 'inherit' });
  console.log('Dependencias listas ✓');
}
ensureDeps();

const { chromium } = require('playwright');
const { PDFDocument } = require('pdf-lib');

/* ── Rutas por argumento (en vez de hardcodeadas) ──────────────────────── */
const HTML_PATH = process.argv[2];
const PDF_OUT   = process.argv[3];

if (!HTML_PATH || !PDF_OUT) {
  console.error('Uso: node export_pdf.js <entrada.html> <salida.pdf>');
  process.exit(1);
}

const HTML_ABS = path.resolve(HTML_PATH);
if (!fs.existsSync(HTML_ABS)) {
  console.error(`No se encontró el archivo HTML: ${HTML_ABS}`);
  process.exit(1);
}

/* ── CLIENT: reemplaza spans de texto en gradiente por imágenes de canvas ── */
async function clientConvertGradientToCanvas() {
  const DPR = 2; // calidad retina

  /* Esperar a que las fuentes web estén cargadas en el motor del navegador */
  await document.fonts.ready;

  const candidates = Array.from(document.querySelectorAll('.grad, .stat .n'));

  for (const el of candidates) {
    const cs  = getComputedStyle(el);
    const box = el.getBoundingClientRect();
    if (box.width < 1 || box.height < 1) continue;

    const text = el.textContent.trim();
    if (!text) continue;

    const fsize = parseFloat(cs.fontSize);

    /* Detección multilínea: si el alto del bounding-rect supera 1.5× el
       line-height, el texto en gradiente envuelve en varias líneas. Canvas no
       puede envolver — reemplazarlo produciría un bloque de ancho fijo que
       rompe el flujo inline del título. Fallback: usar el primer stop sólido. */
    const lineH = parseFloat(cs.lineHeight) || fsize * 1.2;
    if (box.height > lineH * 1.5) {
      el.style.setProperty('background',             'none',    'important');
      el.style.setProperty('-webkit-background-clip','unset',   'important');
      el.style.setProperty('background-clip',        'unset',   'important');
      el.style.setProperty('color',                  '#FF7A00', 'important');
      continue;
    }
    const fweight = cs.fontWeight;
    const ffam    = cs.fontFamily.replace(/"/g, '').split(',')[0].trim();
    const lspac   = cs.letterSpacing !== 'normal' ? cs.letterSpacing : '0px';
    const w       = box.width;
    const h       = box.height;

    /* Parsear los stops del gradiente desde el backgroundImage computado */
    const bgImg = cs.backgroundImage;
    let gradStops = [
      { pos: 0,    color: '#FF7A00' },
      { pos: 0.45, color: '#F7052D' },
      { pos: 1,    color: '#C8128B' },
    ];
    const colorMatch = bgImg.match(/(#[0-9a-fA-F]{3,8}|rgba?\([^)]+\))/g);
    if (colorMatch && colorMatch.length >= 2) {
      gradStops = colorMatch.map((c, i, arr) => ({
        pos: i / (arr.length - 1),
        color: c,
      }));
    }

    /* Canvas de alta densidad */
    const canvas = document.createElement('canvas');
    canvas.width  = Math.ceil(w * DPR);
    canvas.height = Math.ceil(h * DPR);
    const ctx = canvas.getContext('2d');
    ctx.scale(DPR, DPR);

    ctx.font = `${fweight} ${fsize}px ${ffam}`;
    if ('letterSpacing' in ctx) ctx.letterSpacing = lspac;
    ctx.textBaseline = 'alphabetic';

    const m = ctx.measureText(text);
    const halfLeading = Math.max(0, (h - fsize) / 2);
    const baseline = halfLeading + (m.actualBoundingBoxAscent || fsize * 0.78);

    const grad = ctx.createLinearGradient(0, 0, w, 0);
    gradStops.forEach(s => grad.addColorStop(s.pos, s.color));

    ctx.fillStyle = grad;
    ctx.fillText(text, 0, baseline);

    /* Si al span le sigue un nodo de texto que empieza con ".", Chromium lo
       renderiza como un glifo diminuto mal ubicado tras el <img>. Fix: absorber
       el punto DENTRO del canvas, en color de tinta, como un solo elemento. */
    const nextSib = el.nextSibling;
    const hasTrailingDot =
      nextSib &&
      nextSib.nodeType === Node.TEXT_NODE &&
      nextSib.textContent.trimStart().charAt(0) === '.';

    const inkColor = getComputedStyle(el.parentElement).color || '#0B1620';

    const dotWidth = hasTrailingDot ? ctx.measureText('.').width + 2 : 0;
    const totalW = w + dotWidth;

    const finalCanvas = document.createElement('canvas');
    finalCanvas.width  = Math.ceil(totalW * DPR);
    finalCanvas.height = Math.ceil(h * DPR);
    const fctx = finalCanvas.getContext('2d');
    fctx.scale(DPR, DPR);
    fctx.font = `${fweight} ${fsize}px ${ffam}`;
    if ('letterSpacing' in fctx) fctx.letterSpacing = lspac;
    fctx.textBaseline = 'alphabetic';

    fctx.fillStyle = grad;
    fctx.fillText(text, 0, baseline);

    if (hasTrailingDot) {
      fctx.fillStyle = inkColor;
      fctx.fillText('.', w, baseline);
      nextSib.textContent = nextSib.textContent.replace(/^(\s*)\./, '$1');
    }

    const vaOffset = -(h - baseline);

    const dataUrl = finalCanvas.toDataURL('image/png');
    const img = document.createElement('img');
    img.src = dataUrl;
    img.style.cssText = [
      'display:inline-block',
      `width:${totalW}px`,
      `height:${h}px`,
      `vertical-align:${vaOffset.toFixed(2)}px`,
      'image-rendering:crisp-edges',
      'pointer-events:none',
    ].join(';');
    img.width  = Math.ceil(totalW);
    img.height = Math.ceil(h);
    img.alt = text + (hasTrailingDot ? '.' : '');

    el.replaceWith(img);
  }
}

/* ── MAIN ────────────────────────────────────────────────────────────── */
(async () => {
  console.log(`Abriendo: ${HTML_ABS}`);
  const browser = await chromium.launch({ args: ['--font-render-hinting=none'] });
  const page    = await browser.newPage();

  await page.setViewportSize({ width: 1920, height: 1080 });
  await page.goto('file://' + encodeURI(HTML_ABS), { waitUntil: 'networkidle' });
  await page.waitForTimeout(1800); // margen para que carguen las Google Fonts

  await page.evaluate(() => {
    window.fit = () => {
      const s = document.getElementById('stage');
      if (s) s.style.transform = 'scale(1)';
    };
    window.fit();
    document.querySelectorAll('.nav-controls, .edit-badge').forEach(el => el.style.display = 'none');
  });

  /* Convertir spans de gradiente → imágenes de canvas */
  await page.evaluate(clientConvertGradientToCanvas);
  await page.evaluate(() => window.fit && window.fit());

  /* CSS de impresión: fuerza el layout a 1920×1080 sin márgenes */
  await page.addStyleTag({ content: `
    @page { size: 1920px 1080px; margin: 0; }
    @media print {
      *, *::before, *::after {
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
      }
      html, body {
        width: 1920px !important; min-width: 1920px !important;
        overflow: visible !important;
        margin: 0 !important; padding: 0 !important;
        background: white !important;
      }
      .viewport {
        position: static !important;
        width: 1920px !important; height: 1080px !important;
        display: block !important; overflow: hidden !important;
        background: transparent !important;
      }
      .stage {
        transform: none !important; box-shadow: none !important;
        width: 1920px !important; height: 1080px !important;
        position: relative !important; overflow: hidden !important;
      }
      .nav-controls, .edit-badge { display: none !important; }
    }
  ` });

  const totalSlides = await page.evaluate(() =>
    document.querySelectorAll('.slide').length
  );
  console.log(`Total de slides: ${totalSlides}`);

  const allPdfBytes = [];

  for (let i = 0; i < totalSlides; i++) {
    await page.evaluate((idx) => { window.show(idx); }, i);
    await page.waitForTimeout(400);

    const bytes = await page.pdf({
      preferCSSPageSize: true,
      printBackground:   true,
      margin: { top: '0', right: '0', bottom: '0', left: '0' },
    });
    allPdfBytes.push(bytes);

    process.stdout.write(`  ✓ slide ${i + 1}/${totalSlides}\r`);
  }

  console.log('\nTodos los slides capturados. Uniendo…');
  await browser.close();

  const merged = await PDFDocument.create();
  for (const bytes of allPdfBytes) {
    const doc   = await PDFDocument.load(bytes);
    const pages = await merged.copyPages(doc, doc.getPageIndices());
    pages.forEach(p => merged.addPage(p));
  }

  const out = await merged.save();
  fs.writeFileSync(PDF_OUT, out);
  console.log(`Listo ✓  →  ${PDF_OUT}  (${(out.length / 1024 / 1024).toFixed(1)} MB)`);
})();
