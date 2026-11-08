#!/usr/bin/env python3
"""Mu de bolsillo: un solo archivo HTML que funciona sin internet y, cuando hay conexión, redacta con un modelo.

Toma la página de "Pregúntale a Mu" (index.html) sin duplicarla y le hace tres cambios:
  1. Mete el cerebro (mu-corpus.json) dentro del archivo, así no descarga nada.
  2. Reemplaza la conexión de claude.ai por una llamada directa a la API de Anthropic con la clave del usuario,
     guardada solo en su navegador. Sin conexión o sin clave, Mu muestra la evidencia ordenada, sin redactar.
  3. Agrega un panel "Modelo" para guardar la clave y elegir el modelo.

Uso: python research/grafo/preguntar/build_bolsillo.py   (después de build_corpus.py)
Salida: research/grafo/preguntar/mu-bolsillo.html (no se versiona: pesa lo mismo que el corpus).
"""
import json
from pathlib import Path

H = Path(__file__).resolve().parent
OUT = H / "mu-bolsillo.html"

SHIM = r"""
<script>
// Puente local: hace las veces de window.claude. Solo existe en el Mu de bolsillo.
(() => {
  const K = "mu-bolsillo-clave", M = "mu-bolsillo-modelo";
  const leer = k => { try { return localStorage.getItem(k) || ""; } catch { return ""; } };
  window.__muLocal = { K, M, leer };
  const fallo = (code, message, text) => Object.assign(new Error(message), { code, message, text });
  async function llamar(input, opts = {}) {
    const clave = leer(K), modelo = leer(M) || "claude-opus-5-5";
    if (!clave) throw fallo("sampling_disabled", "Falta la clave de la API");
    const messages = (typeof input === "string" ? [{ role: "user", content: input }] : input)
      .map(t => ({ role: t.role === "assistant" ? "assistant" : "user", content: String(t.content) }));
    const effort = opts.modelTier === "complex" ? "high" : opts.modelTier === "quick" ? "low" : "medium";
    let res;
    try {
      res = await fetch("https://api.anthropic.com/v1/messages", {
        method: "POST", signal: opts.signal,
        headers: { "content-type": "application/json", "x-api-key": clave, "anthropic-version": "2023-06-01",
                   "anthropic-beta": "server-side-fallback-2026-07-01", "anthropic-dangerous-direct-browser-access": "true" },
        body: JSON.stringify({ model: modelo, max_tokens: 16000, stream: true, thinking: { type: "adaptive" },
                               output_config: { effort }, fallbacks: "default", messages })
      });
    } catch (e) {
      if (e && e.name === "AbortError") throw fallo("cancelled", "Detenida");
      throw fallo("sampling_disabled", "Sin conexión con la API");
    }
    if (!res.ok) {
      const det = await res.text().catch(() => "");
      if (res.status === 401 || res.status === 403) throw fallo("sampling_disabled", "La clave no es válida");
      if (res.status === 429) throw fallo("rate_limited", "Demasiadas consultas seguidas");
      throw fallo("api_error", `La API respondió ${res.status}: ${det.slice(0, 200)}`);
    }
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
  const listo = () => navigator.onLine && !!leer(K);
  window.claude = { use: async n => n === "sample" && listo() ? sample : null };

  // El cerebro viaja dentro del archivo.
  const f0 = window.fetch.bind(window);
  window.fetch = (u, o) => String(u) === "mu-corpus.json"
    ? Promise.resolve(new Response(document.getElementById("mu-corpus-inline").textContent, { headers: { "content-type": "application/json" } }))
    : f0(u, o);

  // Panel "Modelo": clave (solo en este navegador) y modelo.
  addEventListener("DOMContentLoaded", () => {
    const p = document.createElement("details"); p.id = "mu-local";
    p.innerHTML = `<summary>MODELO</summary>
      <p>Sin internet, Mu muestra la evidencia sin redactar. Con internet y una clave de la API de Anthropic, redacta y razona.
      La clave se guarda solo en este navegador.</p>
      <label>Clave de la API <input id="mu-k" type="password" autocomplete="off" placeholder="sk-ant-…"></label>
      <label>Modelo <select id="mu-m"><option value="claude-opus-5-5">Claude Opus 5.5 (el más capaz)</option>
        <option value="claude-sonnet-5-5">Claude Sonnet 5.5 (más barato)</option></select></label>
      <button type="button" id="mu-g">Guardar</button> <button type="button" id="mu-b">Borrar clave</button>
      <p id="mu-e"></p>`;
    document.body.prepend(p);
    const $ = id => document.getElementById(id), escribir = (k, v) => { try { v ? localStorage.setItem(k, v) : localStorage.removeItem(k); } catch {} };
    const estado = () => { $("mu-e").textContent = (navigator.onLine ? "En línea" : "Sin conexión") + " · " + (leer(K) ? "clave guardada" : "sin clave") + " · " + (navigator.onLine && leer(K) ? "Mu redacta con " + ($("mu-m").selectedOptions[0] || {}).text : "Mu muestra la evidencia sin redactar"); };
    $("mu-m").value = leer(M) || "claude-opus-5-5";
    $("mu-g").onclick = () => { if ($("mu-k").value.trim()) escribir(K, $("mu-k").value.trim()); escribir(M, $("mu-m").value); $("mu-k").value = ""; estado(); };
    $("mu-b").onclick = () => { escribir(K, ""); estado(); };
    addEventListener("online", estado); addEventListener("offline", estado); estado();
  });
})();
</script>
<style>
#mu-local{border:2px solid var(--fg,#000);padding:6px 10px;margin:8px 0;font-family:var(--mono,monospace);font-size:13px}
#mu-local summary{cursor:pointer;font-family:var(--display,Impact,sans-serif);letter-spacing:.05em}
#mu-local label{display:block;margin:6px 0}#mu-local input,#mu-local select{width:100%;max-width:420px;font:inherit;padding:4px;border:2px solid var(--fg,#000);border-radius:0}
#mu-local button{font:inherit;padding:4px 10px;border:2px solid var(--fg,#000);background:var(--bg,#fff);color:var(--fg,#000);border-radius:0;cursor:pointer}
#mu-e{color:var(--acc,#ff3b00)}
</style>
"""

CAMBIOS = [
    # Si no había modelo, volver a mirar en la próxima pregunta (por si volvió la conexión o se guardó la clave).
    ("sampleChecked = true;", "sampleChecked = !!sample;"),
    ('"Para que Mu redacte una respuesta, abre esta página en claude.ai con tu sesión iniciada."',
     '"Sin conexión o sin clave de la API: Mu muestra la evidencia sin redactar. Para respuestas redactadas, conéctate y guarda tu clave en MODELO."'),
    ('sampling_disabled: "Claude no está disponible para esta cuenta. Mu solo puede mostrarte los fragmentos que encontró."',
     'sampling_disabled: "No se pudo usar el modelo (sin conexión o clave no válida). Mu muestra la evidencia sin redactar."'),
]


def main():
    page = (H / "index.html").read_text(encoding="utf-8")
    for a, b in CAMBIOS:
        if a not in page:
            raise SystemExit(f"no se encontró en index.html: {a[:60]}")
        page = page.replace(a, b)
    corpus = (H / "mu-corpus.json").read_text(encoding="utf-8").replace("</", "<\\/")
    html = ('<!doctype html><html lang="es"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<script type="application/json" id="mu-corpus-inline">{corpus}</script>{SHIM}</head><body>'
            f'{page}</body></html>')
    OUT.write_text(html, encoding="utf-8")
    print(f"ok: {OUT.relative_to(H.parent.parent.parent)} · {OUT.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
