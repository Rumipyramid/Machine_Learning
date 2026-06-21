/* =============================================================================
 * Motor de usuarios sintéticos de seguros (Perú)
 * - Genera perfiles calibrados (port JS del schema en synthetic_user_schema.json)
 * - Simula respuestas a preguntas según el perfil de cada persona
 * - Genera hallazgos / insights con redacción ejecutiva
 * Sin dependencias. Usable en navegador (window.SynthEngine) y en Node (require).
 * ========================================================================== */
(function (root) {
  "use strict";

  // ---- Paleta de categorías ----
  var C = {
    green: "#2e8b57", teal: "#138a8a", amber: "#cf7a1f",
    red: "#b23a48", gray: "#8a9099", blue: "#2e5aac"
  };

  // ---- RNG reproducible (mulberry32) ----
  function mulberry32(seed) {
    var a = seed >>> 0;
    return function () {
      a |= 0; a = (a + 0x6D2B79F5) | 0;
      var t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  function gauss(rng, mean, sd) {
    var u = 1 - rng(), v = rng();
    return mean + sd * Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v);
  }
  function pick(rng, dist) {
    var r = rng(), acc = 0, keys = Object.keys(dist);
    for (var i = 0; i < keys.length; i++) { acc += dist[keys[i]]; if (r < acc) return keys[i]; }
    return keys[keys.length - 1];
  }
  function sigmoid(x) { return 1 / (1 + Math.exp(-x)); }

  // ---- Distribuciones (calibradas con SBS 2023, APESEG, APEIM) ----
  var M = {
    generacion: { "Gen Z (18-27)": .22, "Millennial (28-43)": .33, "Gen X (44-59)": .25, "Boomer (60+)": .20 },
    nse: { A: .02, B: .11, C: .27, D: .26, E: .34 },
    region: { "Lima Metro": .33, "Resto Costa": .25, "Sierra": .30, "Selva": .12 },
    educacion: { baja: .50, media: .35, alta: .15 },
    sesgo: { alto: .45, medio: .35, bajo: .20 },
    canal: { "Directo/Digital": .35, "Bancaseguros": .30, "Broker": .25, "Ninguno": .10 }
  };
  var EXPO = {
    "Lima Metro": { alta: .85, media: .13, baja: .02 },
    "Resto Costa": { alta: .70, media: .25, baja: .05 },
    "Sierra": { alta: .40, media: .45, baja: .15 },
    "Selva": { alta: .20, media: .45, baja: .35 }
  };
  var APERTURA = {
    "Gen Z (18-27)": { alta: .55, media: .32, baja: .13 },
    "Millennial (28-43)": { alta: .45, media: .35, baja: .20 },
    "Gen X (44-59)": { alta: .32, media: .40, baja: .28 },
    "Boomer (60+)": { alta: .22, media: .40, baja: .38 }
  };
  var DRV = {
    nse: { A: 1.6, B: 1.0, C: 0.2, D: -0.4, E: -0.9 },
    edu: { alta: 0.9, media: 0.2, baja: -0.5 },
    sesgo: { alto: -0.7, medio: -0.1, bajo: 0.5 },
    conf: { confia: 0.6, neutral: 0.0, desconfia: -0.5 },
    intercepto: 0.25
  };
  var P_VOL = { A: .75, B: .60, C: .40, D: .25, E: .15 };

  function makeUser(rng, idx) {
    var generacion = pick(rng, M.generacion);
    var nse = pick(rng, M.nse);
    var region = pick(rng, M.region);
    var edu = pick(rng, M.educacion);
    var sesgo = pick(rng, M.sesgo);
    var canal = pick(rng, M.canal);
    var exposicion = pick(rng, EXPO[region]);
    var apertura = pick(rng, APERTURA[generacion]);

    // confianza (marginal + ajuste por canal)
    var cd = { desconfia: .48, neutral: .29, confia: .23 };
    if (canal === "Broker") { cd.confia += .15; cd.desconfia = Math.max(.01, cd.desconfia - .15); }
    else if (canal === "Directo/Digital") { cd.confia = Math.max(.01, cd.confia - .03); cd.desconfia += .03; }
    var confianza = pick(rng, cd);

    // tenencia (score logístico)
    var score = DRV.intercepto + DRV.nse[nse] + DRV.edu[edu] + DRV.sesgo[sesgo] + DRV.conf[confianza];
    var tenencia;
    if (rng() >= sigmoid(score)) tenencia = "ninguno";
    else tenencia = (rng() < P_VOL[nse]) ? "voluntario" : "obligatorio";

    // seguro desastres
    var base = .033, mult = 1;
    mult *= ({ A: 4, B: 2.5, C: 1, D: .4, E: .2 })[nse];
    mult *= ({ alta: 1.4, media: 1, baja: .6 })[exposicion];
    mult *= ({ voluntario: 3, obligatorio: .8, ninguno: .1 })[tenencia];
    var desastres = rng() < Math.min(.95, base * mult);

    // WTP
    var wtp = tenencia === "ninguno" ? gauss(rng, .66, .18) : gauss(rng, 1.05, .20);
    wtp = Math.max(0, Math.round(wtp * 1000) / 1000);

    return {
      id: "u" + idx, generacion: generacion, nse: nse, region: region,
      educacion: edu, sesgo: sesgo, canal: canal, exposicion: exposicion,
      apertura: apertura, confianza: confianza, tenencia: tenencia,
      desastres: desastres, wtp: wtp
    };
  }

  function generate(n, seed) {
    var rng = mulberry32(seed | 0), out = [];
    for (var i = 0; i < n; i++) out.push(makeUser(rng, i));
    return out;
  }

  // ---- Preguntas ----
  var QUESTIONS = {
    confianza: {
      label: "¿Confías en las aseguradoras?",
      cats: [
        { key: "confia", label: "Confío", color: C.green },
        { key: "neutral", label: "Neutral", color: C.gray },
        { key: "desconfia", label: "Desconfío", color: C.red }
      ],
      favorable: "confia",
      answer: function (u) { return u.confianza; },
      lens: "La confianza sube con la intermediación de un corredor y con mayor educación financiera; la falta de información es el principal motor de la desconfianza.",
      reco: "Priorizar transparencia y educación: explicar coberturas en lenguaje claro y apoyar el canal broker para los segmentos más escépticos."
    },
    contratar: {
      label: "¿Contratarías un seguro hoy?",
      cats: [
        { key: "si", label: "Sí", color: C.green },
        { key: "condiciones", label: "Sí, con condiciones", color: C.amber },
        { key: "no", label: "No", color: C.red }
      ],
      favorable: "si",
      answer: function (u) {
        if (u.tenencia === "voluntario") return "si";
        var s = 0;
        s += ({ confia: 2, neutral: 0, desconfia: -1.5 })[u.confianza];
        s += ({ A: 1.5, B: 1.5, C: 0.3, D: -0.5, E: -1 })[u.nse];
        s += ({ alto: -1.2, medio: -0.3, bajo: 0.5 })[u.sesgo];
        s += ({ alta: 0.8, media: 0.2, baja: -0.4 })[u.educacion];
        if (s >= 1.5) return "si";
        if (s >= -0.6) return "condiciones";
        return "no";
      },
      lens: "El cortoplacismo (“lo veré después”) y el precio frenan la compra en NSE bajos; la confianza y la educación financiera la impulsan.",
      reco: "Activar a los “indecisos con condiciones” con precio claro, pagos flexibles y pruebas de siniestros pagados a tiempo."
    },
    tenencia: {
      label: "¿Tienes algún seguro actualmente?",
      cats: [
        { key: "voluntario", label: "Seguro voluntario", color: C.green },
        { key: "obligatorio", label: "Solo obligatorio", color: C.teal },
        { key: "ninguno", label: "Ninguno", color: C.gray }
      ],
      favorable: "voluntario",
      answer: function (u) { return u.tenencia; },
      lens: "Cerca de 4 de cada 10 peruanos tiene o tuvo seguro; la tenencia voluntaria se concentra en NSE altos y personas con baja procrastinación.",
      reco: "Diseñar productos de entrada (microseguros) para convertir a quienes hoy solo tienen cobertura obligatoria."
    },
    marca: {
      label: "¿Qué piensas de {brand}?",
      needsBrand: true,
      cats: [
        { key: "positiva", label: "Positiva", color: C.green },
        { key: "neutral", label: "Neutral / evalúa", color: C.amber },
        { key: "critica", label: "Crítica", color: C.red }
      ],
      favorable: "positiva",
      answer: function (u) {
        var s = 0;
        s += ({ confia: 2, neutral: 0, desconfia: -2 })[u.confianza];
        s += ({ voluntario: 1, obligatorio: 0, ninguno: -0.5 })[u.tenencia];
        s += ({ "Broker": 1, "Bancaseguros": 0.7, "Directo/Digital": -0.3, "Ninguno": -0.5 })[u.canal];
        if (s >= 1.5) return "positiva";
        if (s >= -0.6) return "neutral";
        return "critica";
      },
      lens: "El reconocimiento de marca rara vez se traduce en confianza automática: el factor decisivo es la rapidez y transparencia del siniestro.",
      reco: "Convertir el reconocimiento en confianza con garantías de servicio (tiempos de pago) y reforzar la atención en provincias."
    },
    datos_ia: {
      label: "¿Compartirías tus datos con una aseguradora que use IA?",
      cats: [
        { key: "alta", label: "Sí, sin problema", color: C.green },
        { key: "media", label: "Con reservas", color: C.amber },
        { key: "baja", label: "No", color: C.red }
      ],
      favorable: "alta",
      answer: function (u) { return u.apertura; },
      lens: "La apertura a compartir datos y a la IA es marcadamente generacional: alta en Gen Z y mucho menor en Boomers.",
      reco: "Apalancar canales digitales con IA en segmentos jóvenes y reforzar garantías de privacidad para los mayores."
    }
  };

  // ---- Filtros y agregaciones ----
  function applyFilters(users, f) {
    f = f || {};
    return users.filter(function (u) {
      return (!f.nse || !f.nse.length || f.nse.indexOf(u.nse) >= 0)
        && (!f.generacion || !f.generacion.length || f.generacion.indexOf(u.generacion) >= 0)
        && (!f.region || !f.region.length || f.region.indexOf(u.region) >= 0)
        && (!f.canal || !f.canal.length || f.canal.indexOf(u.canal) >= 0);
    });
  }

  function tally(users, q, brand) {
    var counts = {}; q.cats.forEach(function (c) { counts[c.key] = 0; });
    users.forEach(function (u) { counts[q.answer(u, brand)]++; });
    var n = users.length || 1;
    return q.cats.map(function (c) {
      return { key: c.key, label: c.label, color: c.color, value: counts[c.key], pct: Math.round(1000 * counts[c.key] / n) / 10 };
    });
  }

  var DIM = { nse: ["A", "B", "C", "D", "E"], generacion: Object.keys(M.generacion), region: Object.keys(M.region), canal: Object.keys(M.canal) };
  function dimKey(dim) { return dim; } // user field name matches

  function breakdown(users, q, dim, brand) {
    var field = dimKey(dim);
    var levels = DIM[dim];
    return levels.map(function (lv) {
      var sub = users.filter(function (u) { return u[field] === lv; });
      var t = tally(sub, q, brand);
      return { level: lv, n: sub.length, cats: t };
    }).filter(function (r) { return r.n > 0; });
  }

  // ---- Generación de hallazgos / insights (tono ejecutivo) ----
  function favPct(users, q, brand) {
    if (!users.length) return 0;
    var f = 0; users.forEach(function (u) { if (q.answer(u, brand) === q.favorable) f++; });
    return Math.round(1000 * f / users.length) / 10;
  }

  function insights(users, q, brand, filtersDesc) {
    var n = users.length;
    var t = tally(users, q, brand).slice().sort(function (a, b) { return b.value - a.value; });
    var dom = t[0];
    var favLabel = q.cats.filter(function (c) { return c.key === q.favorable; })[0].label;
    var fp = favPct(users, q, brand);

    // variación por NSE
    var byNse = DIM.nse.map(function (lv) {
      var sub = users.filter(function (u) { return u.nse === lv; });
      return { lv: lv, n: sub.length, fp: favPct(sub, q, brand) };
    }).filter(function (r) { return r.n >= Math.max(3, n * 0.02); });
    byNse.sort(function (a, b) { return b.fp - a.fp; });

    // variación por generación
    var byGen = DIM.generacion.map(function (lv) {
      var sub = users.filter(function (u) { return u.generacion === lv; });
      return { lv: lv, n: sub.length, fp: favPct(sub, q, brand) };
    }).filter(function (r) { return r.n >= Math.max(3, n * 0.02); });
    byGen.sort(function (a, b) { return b.fp - a.fp; });

    var label = q.label.replace("{brand}", brand || "la marca");
    var headline = "Sobre “" + label + "”, la postura predominante es “" + dom.label +
      "” con " + dom.pct + "% de las " + n + " respuestas" + (filtersDesc ? " (" + filtersDesc + ")" : "") + ".";

    var bullets = [];
    bullets.push("Respuesta favorable (“" + favLabel + "”): " + fp + "% del grupo.");
    if (byNse.length >= 2) {
      var bestN = byNse[0], worstN = byNse[byNse.length - 1];
      bullets.push("Por nivel socioeconómico, el NSE " + bestN.lv + " es el más favorable (" + bestN.fp +
        "% “" + favLabel + "”) frente al NSE " + worstN.lv + " (" + worstN.fp + "%).");
    }
    if (byGen.length >= 2 && Math.abs(byGen[0].fp - byGen[byGen.length - 1].fp) >= 8) {
      var bestG = byGen[0], worstG = byGen[byGen.length - 1];
      bullets.push("Brecha generacional: " + bestG.lv + " lidera (" + bestG.fp + "%) y " +
        worstG.lv + " es el más bajo (" + worstG.fp + "%).");
    }
    var avgWtp = users.reduce(function (s, u) { return s + u.wtp; }, 0) / (n || 1);
    bullets.push("Disposición a pagar promedio: " + (Math.round(avgWtp * 100) / 100) +
      "× del precio justo (1.0 = precio técnico del riesgo).");
    bullets.push(q.lens);

    return { headline: headline, bullets: bullets, recommendation: q.reco, dominant: dom, favPct: fp };
  }

  var api = {
    palette: C, M: M, DIM: DIM, QUESTIONS: QUESTIONS,
    generate: generate, applyFilters: applyFilters, tally: tally,
    breakdown: breakdown, insights: insights, favPct: favPct
  };

  if (typeof module !== "undefined" && module.exports) module.exports = api;
  root.SynthEngine = api;
})(typeof window !== "undefined" ? window : globalThis);
