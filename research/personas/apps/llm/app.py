#!/usr/bin/env python3
"""
Backend de preguntas libres a usuarios sintéticos, respondidas por Claude.

Flujo:
  1. Muestrea N perfiles con el generador calibrado (research/personas/generate_synthetic_users.py).
  2. Construye un prompt que le pide a Claude hacer role-play de cada persona ante la
     pregunta libre del usuario, en español peruano y coherente con sus atributos.
  3. Usa structured outputs (JSON schema) para recibir, validado: respuesta + sentimiento
     por persona, más hallazgos/insights ejecutivos.
  4. Sirve la interfaz (index.html) y expone POST /api/ask.

Requisitos: pip install -r requirements.txt   y   export ANTHROPIC_API_KEY=...
Ejecutar:   python app.py   →   http://localhost:5000/

Modelo: claude-opus-4-8 (structured outputs + adaptive thinking).
"""
from __future__ import annotations

import importlib.util
import json
import os
import random

from flask import Flask, jsonify, request, send_from_directory

APP_DIR = os.path.dirname(os.path.abspath(__file__))
GEN_PATH = os.path.normpath(os.path.join(APP_DIR, "..", "..", "generador", "generate_synthetic_users.py"))

# --- Cargar el generador calibrado como módulo ---
_spec = importlib.util.spec_from_file_location("synthgen", GEN_PATH)
synthgen = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(synthgen)
_SCHEMA = synthgen.load_schema()

MODEL = "claude-opus-4-8"
MAX_N = 25  # tope de personas por consulta (latencia/costo)

FIELD_MAP = {  # filtro -> campo del usuario
    "nse": "nse",
    "generacion": "generacion",
    "region": "region",
    "canal": "canal_preferido",
}

SYSTEM_PROMPT = """\
Eres un simulador de investigación de mercado. Recibes un conjunto de PERSONAS SINTÉTICAS
(consumidores peruanos de seguros, generadas a partir de distribuciones calibradas con datos
reales de SBS, APESEG y APEIM) y una PREGUNTA. Debes responder la pregunta EN PRIMERA PERSONA
por cada persona, como si fueran personas reales siendo entrevistadas.

Codebook de atributos de cada persona:
- generacion: Gen_Z_18_27, Millennial_28_43, Gen_X_44_59, Boomer_60_mas.
- nse: nivel socioeconómico A (alto) a E (bajo).
- region: Lima_Metropolitana, Resto_Costa, Sierra, Selva.
- educacion_financiera: baja | media | alta.
- sesgo_presente: alto = muy cortoplacista/procrastinador; bajo = planifica a futuro.
- canal_preferido: directo_digital | bancaseguros | broker_corredor | ninguno.
- exposicion_riesgo_sismico: alta | media | baja.
- apertura_datos_ia: disposición a compartir datos / confiar en IA (alta|media|baja).
- confianza_aseguradora: confia_plena | neutral | desconfia.
- tenencia_seguro: voluntario | obligatorio (solo SOAT/Vida Ley) | ninguno.
- seguro_desastres_naturales: true/false (cobertura ante sismos).
- wtp_ratio: disposición a pagar como fracción del precio justo (1.0 = precio técnico).

Reglas:
1. Responde en ESPAÑOL PERUANO, natural y coloquial cuando corresponda al perfil.
2. Cada respuesta debe ser COHERENTE con los atributos: un desconfia + sesgo alto + NSE bajo
   suena distinto a un confia_plena + NSE A con seguro voluntario.
3. Cada "quote" tiene 1 a 3 oraciones, en primera persona.
4. Clasifica el "sentiment" de cada respuesta FRENTE A LA PREGUNTA:
   favorable | neutral | desfavorable.
5. Devuelve EXACTAMENTE una respuesta por cada persona recibida, usando su "id".
6. En "insights" redacta con tono de experto en presentaciones: un "headline" (1 frase con la
   cifra clave), 3-5 "findings" con patrones y porcentajes aproximados, y una "recommendation"
   accionable. Conecta los hallazgos con los drivers reales (confianza, información, precio,
   sesgo del presente, canal broker).

Recuerda: son personas inventadas; el objetivo es prototipar y explorar hipótesis, no sustituir
una encuesta real.
"""

RESULT_SCHEMA = {
    "type": "object",
    "properties": {
        "responses": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "sentiment": {"type": "string", "enum": ["favorable", "neutral", "desfavorable"]},
                    "quote": {"type": "string"},
                },
                "required": ["id", "sentiment", "quote"],
                "additionalProperties": False,
            },
        },
        "insights": {
            "type": "object",
            "properties": {
                "headline": {"type": "string"},
                "findings": {"type": "array", "items": {"type": "string"}},
                "recommendation": {"type": "string"},
            },
            "required": ["headline", "findings", "recommendation"],
            "additionalProperties": False,
        },
    },
    "required": ["responses", "insights"],
    "additionalProperties": False,
}

PERSONA_FIELDS = [
    "id", "generacion", "nse", "region", "educacion_financiera", "sesgo_presente",
    "canal_preferido", "exposicion_riesgo_sismico", "apertura_datos_ia",
    "confianza_aseguradora", "tenencia_seguro", "seguro_desastres_naturales", "wtp_ratio",
]


def sample_users(n: int, seed: int, filters: dict) -> list[dict]:
    """Muestrea n usuarios que cumplan los filtros (oversampling si hace falta)."""
    n = max(1, min(int(n), MAX_N))
    rng = random.Random(int(seed))
    out, i, guard = [], 0, 0
    active = {FIELD_MAP[k]: set(v) for k, v in (filters or {}).items() if v}
    while len(out) < n and guard < 200_000:
        u = synthgen.generate_user(rng, _SCHEMA, i)
        i += 1
        guard += 1
        if all(u[field] in vals for field, vals in active.items()):
            u["id"] = f"p{len(out):02d}"
            out.append({k: u[k] for k in PERSONA_FIELDS})
    return out


def build_messages(question: str, users: list[dict]):
    user_msg = (
        f"PREGUNTA:\n{question.strip()}\n\n"
        f"PERSONAS ({len(users)}):\n"
        + json.dumps(users, ensure_ascii=False)
    )
    system = [{"type": "text", "text": SYSTEM_PROMPT, "cache_control": {"type": "ephemeral"}}]
    return system, [{"role": "user", "content": user_msg}]


def ask_claude(question: str, users: list[dict]) -> dict:
    import anthropic

    client = anthropic.Anthropic()  # lee ANTHROPIC_API_KEY del entorno
    system, messages = build_messages(question, users)
    resp = client.messages.create(
        model=MODEL,
        max_tokens=16000,
        thinking={"type": "adaptive"},
        output_config={"format": {"type": "json_schema", "schema": RESULT_SCHEMA}, "effort": "medium"},
        system=system,
        messages=messages,
    )
    if resp.stop_reason == "refusal":
        raise RuntimeError("El modelo rechazó la solicitud por motivos de seguridad.")
    if resp.stop_reason == "max_tokens":
        raise RuntimeError("Respuesta incompleta (max_tokens). Reduce el número de personas.")
    text = next((b.text for b in resp.content if b.type == "text"), None)
    if not text:
        raise RuntimeError("Respuesta vacía del modelo.")
    return json.loads(text)


# --- Flask ---
app = Flask(__name__, static_folder=None)


@app.route("/")
def index():
    return send_from_directory(APP_DIR, "index.html")


@app.route("/api/ask", methods=["POST"])
def api_ask():
    body = request.get_json(force=True) or {}
    question = (body.get("question") or "").strip()
    if not question:
        return jsonify({"error": "Falta la pregunta."}), 400
    if not os.environ.get("ANTHROPIC_API_KEY"):
        return jsonify({"error": "Configura ANTHROPIC_API_KEY en el entorno para usar el cerebro de Claude."}), 503

    users = sample_users(body.get("n", 12), body.get("seed", 42), body.get("filters", {}))
    if not users:
        return jsonify({"error": "Ningún usuario cumple esos filtros. Amplía la muestra o relaja los segmentos."}), 200
    try:
        result = ask_claude(question, users)
    except Exception as e:  # noqa: BLE001
        return jsonify({"error": f"{type(e).__name__}: {e}"}), 502
    return jsonify({"question": question, "model": MODEL, "users": users, "result": result})


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Construye el prompt sin llamar a la API")
    parser.add_argument("--question", default="¿Por qué contratarías o no un seguro hoy?")
    parser.add_argument("--n", type=int, default=5)
    parser.add_argument("--port", type=int, default=5000)
    args = parser.parse_args()

    if args.dry_run:
        users = sample_users(args.n, 42, {})
        system, messages = build_messages(args.question, users)
        print(f"Usuarios: {len(users)}")
        print(f"System chars: {len(system[0]['text'])}")
        print(f"User msg chars: {len(messages[0]['content'])}")
        print("--- primeras 2 personas ---")
        print(json.dumps(users[:2], ensure_ascii=False, indent=2))
    else:
        app.run(host="0.0.0.0", port=args.port, debug=False)
