// Corre la página real de "Pregúntale a Mu" sin conexión y devuelve, por pregunta, lo que Mu recupera
// (nodos, fuentes) y el prompt exacto que enviaría a Claude. Lo llama examen.py; no se usa solo.
// Uso: node recuperar.cjs <preguntas.json> <salida.json>
// Requiere Playwright (en el entorno en la nube vive en /opt/node22/lib/node_modules/playwright).
const fs = require('fs'), path = require('path'), http = require('http');
let pw;
try { pw = require('playwright'); } catch { pw = require('/opt/node22/lib/node_modules/playwright'); }
const DIR = path.join(__dirname, '..', 'preguntar');
const [, , inPath, outPath] = process.argv;
const qs = JSON.parse(fs.readFileSync(inPath, 'utf8')).preguntas;

// La página se sirve tal cual; solo se expone retrieve() para leer lo recuperado.
const html = fs.readFileSync(path.join(DIR, 'index.html'), 'utf8').replace(
  '  function retrieve(q) {',
  '  window.__retrieve = q => retrieve(ampliarDiseno(ampliarIA(q)));\n  function retrieve(q) {');
if (!html.includes('window.__retrieve')) { console.error('no se encontró retrieve() en index.html'); process.exit(2); }

// Sustituto de window.claude: base en memoria y un sample que registra el prompt y responde vacío.
const MOCK = `(() => {
  const store = {}; const col = n => (store[n] = store[n] || new Map());
  function coll(name) { return { orderBy() { return this }, limit() { return this }, where() { return this },
    onSnapshot(cb) { setTimeout(() => cb({ docs: [], size: 0 }), 0); return () => {} },
    async get() { return { docs: [], size: 0 } }, async add(d) { const id = 'c' + col(name).size; col(name).set(id, d); return { id } },
    doc(id) { return { async get() { return { exists: false, data: () => null } }, async set() {}, async update() {} } } } }
  const sample = async (inp, o) => { const s = typeof inp === 'string' ? inp : JSON.stringify(inp);
    window.__calls = (window.__calls || []).concat([s]); const t = 'Respuesta de prueba.';
    if (o && o.onText) o.onText({ text: t, delta: t }); return { text: t, truncated: false } };
  // El paso de planificación se registra aparte y devuelve un plan marcador: examen.py lo reemplaza por el plan real.
  sample.json = async (inp) => { const s = typeof inp === 'string' ? inp : JSON.stringify(inp);
    if (/razonamiento interno de Mu/.test(s)) { window.__plans = (window.__plans || []).concat([s]);
      return { tipo: 'MARCADOR', criterio: 'MARCADOR', afirmaciones: [{ idea: 'PLAN_MARCADOR', fuentes: [] }], conclusion: 'MARCADOR' }; }
    return { tema_id: 'examen', tema: 'examen', cubierto: 'no', node: '' }; };
  sample.limits = async () => ({ tools: false });
  window.claude = { use: async n => n === 'db' ? { collection: coll } : n === 'user' ? { id: async () => 'u_examen', can: async () => true } : n === 'sample' ? sample : null };
})();`;

(async () => {
  const srv = http.createServer((q, r) => {
    const name = q.url === '/' ? 'index.html' : decodeURIComponent(q.url.slice(1));
    if (name === 'index.html') { r.writeHead(200, { 'content-type': 'text/html; charset=utf-8' }); return r.end(html); }
    const p = path.join(DIR, name);
    if (!p.startsWith(DIR) || !fs.existsSync(p)) { r.writeHead(404); return r.end(); }
    r.writeHead(200, { 'content-type': 'application/json; charset=utf-8' }); r.end(fs.readFileSync(p));
  }).listen(0);
  const port = srv.address().port;
  const launch = fs.existsSync('/opt/pw-browsers/chromium') ? { executablePath: '/opt/pw-browsers/chromium' } : {};
  let b;
  try { b = await pw.chromium.launch(); } catch { b = await pw.chromium.launch(launch); }
  const pg = await b.newPage(); const errs = []; pg.on('pageerror', e => errs.push(e.message));
  await pg.addInitScript({ content: MOCK });
  await pg.goto(`http://localhost:${port}/`);
  await pg.waitForFunction(() => !document.querySelector('#go').disabled, { timeout: 90000 });
  const out = [];
  for (const q of qs) {
    const r = await pg.evaluate(t => { const r = window.__retrieve(t);
      return { nodos: [...new Set(r.nodes.map(c => c.node))], secciones: r.nodes.map(c => c.node + ' § ' + c.seccion),
               fuentes: r.fuentes.map(f => f.id) }; }, q.pregunta);
    // Cada pregunta en una página nueva: sin historial de la pregunta anterior.
    await pg.goto(`http://localhost:${port}/`);
    await pg.waitForFunction(() => !document.querySelector('#go').disabled, { timeout: 90000 });
    await pg.evaluate(() => { window.__calls = []; window.__plans = [] });
    await pg.fill('#qbox', q.pregunta); await pg.click('#go');
    await pg.waitForFunction(() => (window.__calls || []).length > 0, { timeout: 30000 }).catch(() => {});
    const prompt = await pg.evaluate(() => (window.__calls || [])[0] || '');
    const plan_prompt = await pg.evaluate(() => (window.__plans || [])[0] || '');
    out.push({ id: q.id, ...r, prompt, plan_prompt });
    await pg.waitForFunction(() => !document.querySelector('#go').disabled, { timeout: 60000 }).catch(() => {});
  }
  fs.writeFileSync(outPath, JSON.stringify({ errores_pagina: errs, resultados: out }, null, 1));
  await b.close(); srv.close();
})().catch(e => { console.error(e); process.exit(1); });
