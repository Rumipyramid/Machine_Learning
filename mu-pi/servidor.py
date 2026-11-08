#!/usr/bin/env python3
"""Mu en un Raspberry Pi: sirve "Pregúntale a Mu" en la red de la casa y conserva todo lo posible sin internet.

Tres modos, elegidos solos en cada pregunta:
  1. Con internet y clave de Anthropic → Claude redacta y razona (la versión más potente).
  2. Sin internet, con un modelo local (Ollama) instalado → el modelo local redacta (más lento y menos fino).
  3. Sin ninguno → Mu muestra la evidencia ordenada, sin redactar.
La búsqueda, el Criterio por reglas, el registro de temas y el "¿Te sirvió?" funcionan siempre: corren en el Pi.

La clave vive en el Pi (variable de entorno), nunca en el navegador. Solo stdlib.

Variables de entorno (todas opcionales):
  ANTHROPIC_API_KEY   clave de la API de Anthropic
  MU_MODELO           modelo de Claude (por defecto claude-opus-5-5)
  MU_OLLAMA           URL de Ollama (por defecto http://127.0.0.1:11434)
  MU_MODELO_LOCAL     modelo local de Ollama (por defecto llama3.2:3b)
  MU_PUERTO           puerto (por defecto 8080)
  MU_DATOS            carpeta de datos locales (por defecto ~/.local/share/mu-pi)
  MU_ANTHROPIC_URL    solo para pruebas: otra URL base de la API
"""
import http.client, json, os, socket, threading, time, uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

RAIZ = Path(__file__).resolve().parent.parent
PREG = RAIZ / "research/grafo/preguntar"
CLAVE = os.environ.get("ANTHROPIC_API_KEY", "").strip()
MODELO = os.environ.get("MU_MODELO", "claude-opus-5-5")
OLLAMA = os.environ.get("MU_OLLAMA", "http://127.0.0.1:11434").rstrip("/")
MODELO_LOCAL = os.environ.get("MU_MODELO_LOCAL", "llama3.2:3b")
PUERTO = int(os.environ.get("MU_PUERTO", "8080"))
DATOS = Path(os.environ.get("MU_DATOS", Path.home() / ".local/share/mu-pi"))
API = urlparse(os.environ.get("MU_ANTHROPIC_URL", "https://api.anthropic.com"))
COLECCIONES = {"consultas", "temas", "usos"}
_lock = threading.Lock()
_cache = {}


# ---------- ¿qué modelo hay? ----------
def _alcanzable(host, port, t=2.0):
    try:
        socket.create_connection((host, port), timeout=t).close()
        return True
    except OSError:
        return False


def estado():
    ahora = time.time()
    if _cache.get("t", 0) > ahora - 30:
        return _cache["e"]
    internet = _alcanzable(API.hostname, API.port or (443 if API.scheme == "https" else 80))
    o = urlparse(OLLAMA)
    local = _alcanzable(o.hostname, o.port or 11434, 0.5)
    modo = "claude" if (internet and CLAVE) else "local" if local else "ninguno"
    e = {"internet": internet, "clave": bool(CLAVE), "local": local, "modo": modo,
         "modelo": MODELO if modo == "claude" else MODELO_LOCAL if modo == "local" else ""}
    _cache.update(t=ahora, e=e)
    return e


# ---------- base de datos local: un JSON por documento (mismo formato que lee impacto.py --db) ----------
def _col(c):
    if c not in COLECCIONES:
        raise ValueError("colección desconocida")
    d = DATOS / c
    d.mkdir(parents=True, exist_ok=True)
    return d


def db(op, c, doc_id=None, data=None):
    d = _col(c)
    with _lock:
        if op == "list":
            return [{"id": p.stem, "data": json.loads(p.read_text(encoding="utf-8"))} for p in sorted(d.glob("*.json"))]
        if op == "add":
            doc_id = uuid.uuid4().hex[:20]
        p = d / f"{''.join(ch for ch in str(doc_id) if ch.isalnum() or ch in '_-')[:80]}.json"
        if op == "get":
            return {"exists": p.exists(), "data": json.loads(p.read_text(encoding="utf-8")) if p.exists() else None}
        if op in ("add", "set"):
            p.write_text(json.dumps(data or {}, ensure_ascii=False), encoding="utf-8")
            return {"id": p.stem}
        if op == "update":
            prev = json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}
            prev.update(data or {})
            p.write_text(json.dumps(prev, ensure_ascii=False), encoding="utf-8")
            return {"id": p.stem}
    raise ValueError("operación desconocida")


# ---------- la página ----------
SHIM = (Path(__file__).parent / "shim.js").read_text(encoding="utf-8")


def pagina():
    src = (PREG / "index.html").read_text(encoding="utf-8")
    for a, b in [("sampleChecked = true;", "sampleChecked = !!sample;"),
                 ('"Para que Mu redacte una respuesta, abre esta página en claude.ai con tu sesión iniciada."',
                  '"Sin internet y sin modelo local: Mu muestra la evidencia sin redactar."'),
                 ('sampling_disabled: "Claude no está disponible para esta cuenta. Mu solo puede mostrarte los fragmentos que encontró."',
                  'sampling_disabled: "No se pudo usar el modelo (sin internet, clave no válida o modelo local apagado). Mu muestra la evidencia sin redactar."')]:
        if a not in src:
            print(f"aviso: index.html cambió, no se encontró: {a[:50]}", flush=True)
        src = src.replace(a, b)
    return ('<!doctype html><html lang="es"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<script>{SHIM}</script></head><body>{src}</body></html>')


class H(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.0"  # cada respuesta cierra la conexión: permite pasar el stream tal cual

    def log_message(self, fmt, *a):
        pass

    def _enviar(self, code, cuerpo, tipo="application/json; charset=utf-8"):
        b = cuerpo if isinstance(cuerpo, bytes) else (cuerpo if isinstance(cuerpo, str) else json.dumps(cuerpo, ensure_ascii=False)).encode("utf-8")
        self.send_response(code)
        self.send_header("content-type", tipo)
        self.send_header("content-length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)

    def do_GET(self):
        ruta = urlparse(self.path).path
        if ruta in ("/", "/index.html"):
            return self._enviar(200, pagina(), "text/html; charset=utf-8")
        if ruta == "/mu-corpus.json":
            return self._enviar(200, (PREG / "mu-corpus.json").read_bytes())
        if ruta == "/panel":
            return self._enviar(200, (RAIZ / "research/grafo/mu.html").read_bytes(), "text/html; charset=utf-8")
        if ruta == "/api/estado":
            return self._enviar(200, estado())
        self._enviar(404, {"error": "no existe"})

    def do_POST(self):
        ruta = urlparse(self.path).path
        try:
            body = json.loads(self.rfile.read(int(self.headers.get("content-length", 0) or 0)) or b"{}")
        except ValueError:
            return self._enviar(400, {"code": "invalid_argument"})
        if ruta == "/api/db":
            try:
                return self._enviar(200, db(body.get("op"), body.get("col"), body.get("id"), body.get("data")))
            except ValueError as e:
                return self._enviar(400, {"code": "invalid_argument", "message": str(e)})
        if ruta == "/api/llm":
            e = estado()
            if e["modo"] == "claude":
                return self._claude(body)
            if e["modo"] == "local":
                return self._local(body)
            return self._enviar(503, {"code": "sampling_disabled", "message": "Sin internet y sin modelo local"})
        self._enviar(404, {"error": "no existe"})

    def _cabecera_stream(self):
        self.send_response(200)
        self.send_header("content-type", "text/event-stream; charset=utf-8")
        self.end_headers()

    def _claude(self, body):
        tier = body.get("tier")
        effort = "high" if tier == "complex" else "low" if tier == "quick" else "medium"
        req = {"model": MODELO, "max_tokens": 16000, "stream": True, "thinking": {"type": "adaptive"},
               "output_config": {"effort": effort}, "fallbacks": "default", "messages": body.get("messages", [])}
        Con = http.client.HTTPSConnection if API.scheme == "https" else http.client.HTTPConnection
        try:
            c = Con(API.hostname, API.port, timeout=600)
            c.request("POST", "/v1/messages", json.dumps(req), {
                "content-type": "application/json", "x-api-key": CLAVE, "anthropic-version": "2023-06-01",
                "anthropic-beta": "server-side-fallback-2026-07-01"})
            r = c.getresponse()
        except OSError:
            _cache.clear()
            return self._enviar(503, {"code": "sampling_disabled", "message": "Se perdió la conexión con la API"})
        if r.status != 200:
            det = r.read()[:300].decode("utf-8", "replace")
            code = "sampling_disabled" if r.status in (401, 403) else "rate_limited" if r.status == 429 else "api_error"
            return self._enviar(502, {"code": code, "message": f"La API respondió {r.status}: {det}"})
        self._cabecera_stream()
        try:
            while True:
                chunk = r.read1(8192) if hasattr(r, "read1") else r.read(8192)
                if not chunk:
                    break
                self.wfile.write(chunk)
                self.wfile.flush()
        except (BrokenPipeError, ConnectionResetError):
            pass

    def _local(self, body):
        o = urlparse(OLLAMA)
        msgs = [{"role": m.get("role", "user"), "content": str(m.get("content", ""))} for m in body.get("messages", [])]
        try:
            c = http.client.HTTPConnection(o.hostname, o.port or 11434, timeout=1800)
            c.request("POST", "/api/chat", json.dumps({"model": MODELO_LOCAL, "messages": msgs, "stream": True}),
                      {"content-type": "application/json"})
            r = c.getresponse()
        except OSError:
            _cache.clear()
            return self._enviar(503, {"code": "sampling_disabled", "message": "El modelo local no responde"})
        if r.status != 200:
            return self._enviar(502, {"code": "api_error", "message": f"El modelo local respondió {r.status}"})
        self._cabecera_stream()
        try:
            for linea in r:  # Ollama manda una línea JSON por trozo; se traduce al formato de eventos de Anthropic
                try:
                    ev = json.loads(linea)
                except ValueError:
                    continue
                t = (ev.get("message") or {}).get("content", "")
                if t:
                    d = {"type": "content_block_delta", "index": 0, "delta": {"type": "text_delta", "text": t}}
                    self.wfile.write(f"data: {json.dumps(d, ensure_ascii=False)}\n\n".encode("utf-8"))
                    self.wfile.flush()
                if ev.get("done"):
                    self.wfile.write(b'data: {"type":"message_delta","delta":{"stop_reason":"end_turn"}}\n\n')
                    break
        except (BrokenPipeError, ConnectionResetError):
            pass


def main():
    if not (PREG / "mu-corpus.json").exists():
        raise SystemExit("Falta el cerebro: corre primero python3 research/grafo/preguntar/build_corpus.py")
    DATOS.mkdir(parents=True, exist_ok=True)
    e = estado()
    print(f"Mu en http://0.0.0.0:{PUERTO} · modo ahora: {e['modo']} · datos en {DATOS}", flush=True)
    ThreadingHTTPServer(("0.0.0.0", PUERTO), H).serve_forever()


if __name__ == "__main__":
    main()
