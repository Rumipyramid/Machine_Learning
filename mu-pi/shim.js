// Puente del Raspberry Pi: hace las veces de window.claude contra el servidor local (/api/*).
(() => {
  const fallo = (code, message, text) => Object.assign(new Error(message), { code, message, text });
  const post = (ruta, cuerpo, signal) => fetch(ruta, { method: "POST", signal, headers: { "content-type": "application/json" }, body: JSON.stringify(cuerpo) });
  let ESTADO = { modo: "ninguno" };
  const refrescar = () => fetch("/api/estado").then(r => r.json()).then(e => { ESTADO = e; pintar(); }).catch(() => {});

  async function llamar(input, opts = {}) {
    const messages = (typeof input === "string" ? [{ role: "user", content: input }] : input)
      .map(t => ({ role: t.role === "assistant" ? "assistant" : "user", content: String(t.content) }));
    let res;
    try { res = await post("/api/llm", { messages, tier: opts.modelTier || "default" }, opts.signal); }
    catch (e) { if (e && e.name === "AbortError") throw fallo("cancelled", "Detenida"); throw fallo("sampling_disabled", "El Pi no responde"); }
    if (!res.ok) { const j = await res.json().catch(() => ({})); refrescar(); throw fallo(j.code || "api_error", j.message || "Error"); }
    const rd = res.body.getReader(), dec = new TextDecoder();
    let buf = "", text = "", stop = "";
    try {
      for (;;) {
        const { value, done } = await rd.read(); if (done) break;
        buf += dec.decode(value, { stream: true });
        let i;
        while ((i = buf.indexOf("\n")) >= 0) {
          const line = buf.slice(0, i).trim(); buf = buf.slice(i + 1);
          if (!line.startsWith("data:")) continue;
          let ev; try { ev = JSON.parse(line.slice(5)); } catch { continue; }
          if (ev.type === "content_block_delta" && ev.delta && ev.delta.type === "text_delta") {
            text += ev.delta.text; if (opts.onText) opts.onText({ text, delta: ev.delta.text });
          } else if (ev.type === "message_delta" && ev.delta && ev.delta.stop_reason) stop = ev.delta.stop_reason;
          else if (ev.type === "error") throw fallo("api_error", (ev.error && ev.error.message) || "Error de la API", text);
        }
      }
    } catch (e) {
      if (e && e.name === "AbortError") throw fallo("cancelled", "Detenida", text);
      throw e.code ? e : fallo("api_error", "Se cortó la conexión", text);
    }
    if (stop === "refusal" && !text) throw fallo("refused", "El modelo no quiso responder");
    return { text, truncated: stop === "max_tokens" };
  }
  const sample = (input, opts) => llamar(input, opts);
  sample.json = async (input, opts) => {
    const { text } = await llamar(input, opts);
    const t = text.replace(/```(?:json)?/g, ""), a = t.indexOf("{"), b = t.lastIndexOf("}");
    try { return JSON.parse(t.slice(a, b + 1)); } catch { throw fallo("invalid_json", "La respuesta no era JSON", text); }
  };
  sample.limits = async () => ({ tools: false, images: false });

  // Base de datos local: misma forma que la del artefacto (colecciones consultas, temas, usos).
  const oyentes = new Set(), avisar = () => setTimeout(() => oyentes.forEach(f => f()), 50);
  const api = (op, col, id, data) => post("/api/db", { op, col, id, data }).then(r => r.ok ? r.json() : Promise.reject(fallo("invalid_argument", "db")))
    .then(j => { if (op !== "list" && op !== "get") avisar(); return j; });
  function coleccion(col, filtros = [], orden = null, tope = 0) {
    const leer = async () => {
      let docs = (await api("list", col)).filter(d => filtros.every(([f, , v]) => d.data[f] === v));
      if (orden) docs.sort((a, b) => String(a.data[orden[0]]).localeCompare(String(b.data[orden[0]])) * (orden[1] === "desc" ? -1 : 1));
      if (tope) docs = docs.slice(0, tope);
      const ds = docs.map(d => ({ id: d.id, data: () => d.data }));
      return { docs: ds, size: ds.length };
    };
    return {
      where: (f, o, v) => coleccion(col, [...filtros, [f, o, v]], orden, tope),
      orderBy: (f, dir) => coleccion(col, filtros, [f, dir || "asc"], tope),
      limit: n => coleccion(col, filtros, orden, n),
      get: leer,
      onSnapshot(cb, err) { let vivo = true; const tic = () => vivo && leer().then(cb).catch(e => err && err(e)); oyentes.add(tic); tic(); const h = setInterval(tic, 15000); return () => { vivo = false; oyentes.delete(tic); clearInterval(h); }; },
      add: async data => ({ id: (await api("add", col, null, data)).id }),
      doc: id => ({
        get: async () => { const r = await api("get", col, id); return { exists: r.exists, data: () => r.data }; },
        set: data => api("set", col, id, data), update: data => api("update", col, id, data)
      })
    };
  }
  const DB = { collection: n => coleccion(n) };
  let uid = ""; try { uid = localStorage.getItem("mu-pi-uid") || ""; if (!uid) { uid = "u_pi_" + Math.random().toString(36).slice(2, 12); localStorage.setItem("mu-pi-uid", uid); } } catch { uid = "u_pi"; }
  const USER = { id: async () => uid, can: async () => true, isOwner: () => true, canEdit: () => true };

  window.claude = { use: async n => n === "db" ? DB : n === "user" ? USER : n === "sample" ? (await refrescar(), ESTADO.modo !== "ninguno" ? sample : null) : null };

  // Aviso de modo arriba de la página.
  function pintar() {
    let b = document.getElementById("mu-pi"); if (!b) return;
    const t = { claude: `Con internet: redacta Claude (${ESTADO.modelo}).`, local: `Sin internet: redacta el modelo local (${ESTADO.modelo}), más lento y menos fino.`, ninguno: "Sin internet y sin modelo local: Mu muestra la evidencia sin redactar." };
    b.textContent = "MU EN EL PI · " + (t[ESTADO.modo] || t.ninguno) + " · ";
    const a = document.createElement("a"); a.href = "/panel"; a.textContent = "panel del cerebro"; b.append(a);
  }
  addEventListener("DOMContentLoaded", () => {
    const b = document.createElement("p"); b.id = "mu-pi";
    b.style.cssText = "border:2px solid var(--fg,#000);padding:6px 10px;margin:8px 0;font-family:var(--mono,monospace);font-size:13px";
    document.body.prepend(b); refrescar(); setInterval(refrescar, 30000);
  });
})();
