#!/usr/bin/env python3
"""Genera el reporte quincenal de fortalecimiento del modelo `lapuerta`.

Usa la API de Claude (claude-opus-4-8) con la herramienta de búsqueda web para
investigar datos/evidencia recientes y proponer cómo incorporar nuevas variables
al modelo de usuarios sintéticos de seguros (Perú). Escribe el reporte en
`research/updates/AAAA-MM-DD_fortalecimiento_modelo.md` y lo indexa en el códice
(`CLAUDE.md`).

Además, aplica automáticamente al esquema/generador cualquier variable candidata que
el reporte marque Prioridad: Alta (ver `apply_alta_proposals`): un segundo llamado a la
API reescribe `synthetic_user_schema.json`, `generate_synthetic_users.py` y
`matriz_usuarios_sinteticos.md`; el intercepto de variables booleanas nuevas se
recalibra empíricamente (barrido/bisección local, sin depender de que el modelo lo
acierte a la primera) y el resultado se valida con `validate.py --check`. Si algo
falla o la respuesta no viene completa, se revierte todo y la variable queda como
propuesta sin aplicar (no rompe el reporte ni el códice).

Pensado para correr dentro de un GitHub Action (cron). Requiere ANTHROPIC_API_KEY.

Uso:
  python research/updates/generate_report.py            # genera (llama a la API)
  python research/updates/generate_report.py --dry-run  # arma el prompt sin llamar
"""
from __future__ import annotations

import argparse
import datetime as dt
import importlib.util
import json
import os
import random
import re
import subprocess
import sys

MODEL = "claude-opus-4-8"
ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
UPDATES_DIR = os.path.join(ROOT, "research", "updates")
CODEX = os.path.join(ROOT, "CLAUDE.md")
START = "<!-- LAPUERTA_REPORTS_START -->"
END = "<!-- LAPUERTA_REPORTS_END -->"

GENERADOR_DIR = os.path.join(ROOT, "research", "personas", "generador")
SCHEMA_PATH = os.path.join(GENERADOR_DIR, "synthetic_user_schema.json")
GENERATOR_PATH = os.path.join(GENERADOR_DIR, "generate_synthetic_users.py")
MATRIZ_PATH = os.path.join(GENERADOR_DIR, "matriz_usuarios_sinteticos.md")
VALIDATE_PATH = os.path.join(GENERADOR_DIR, "validate.py")
APPLY_FILES = {
    "schema.json": SCHEMA_PATH,
    "generate_synthetic_users.py": GENERATOR_PATH,
    "matriz_usuarios_sinteticos.md": MATRIZ_PATH,
}

VARIABLES_ACTUALES_FALLBACK = (
    "generacion, nse, region, educacion_financiera, sesgo_presente, canal_preferido, "
    "situacion_laboral, cobertura_previsional, tenencia_vehiculo, acceso_digital, bancarizado, "
    "trabajo_plataforma_digital, exposicion_riesgo_sismico, apertura_datos_ia, "
    "confianza_aseguradora, tenencia_seguro, seguro_desastres_naturales, wtp_ratio, "
    "propension_microseguro"
)
# Candidatas Media/Baja ya propuestas pero NO aplicadas (solo Alta se aplica sola; ver
# "Pendientes de incorporar" en matriz_usuarios_sinteticos.md, que es la fuente viva de esto).
YA_PROPUESTAS = (
    "enfermedad_cronica, tenencia_vivienda, recibe_remesas, dependientes_hogar, genero, "
    "vulnerabilidad_economica, nivel_endeudamiento, canal_preferido (recalibracion a "
    "condicional de generacion)"
)


def variables_actuales() -> str:
    """Lee las variables YA en el esquema en vivo (no una lista fija que se desactualiza)."""
    try:
        with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
            schema = json.load(f)
        names = list(schema.get("variables", {})) + list(schema.get("modelos_derivados", {}))
        return ", ".join(names) if names else VARIABLES_ACTUALES_FALLBACK
    except Exception:
        return VARIABLES_ACTUALES_FALLBACK

SYSTEM = """\
Eres analista de investigación del modelo de usuarios sintéticos de seguros del Perú
("lapuerta"). Tu trabajo quincenal: buscar datos y evidencia RECIENTES (últimos ~6 meses)
que permitan fortalecer el modelo, y proponer cómo incorporarlos como variables.

Usa la herramienta de búsqueda web para encontrar fuentes verificables (INEI, BCRP, SBS,
APESEG, APEIM, MAPFRE, OECD, prensa especializada, literatura). Prioriza cifras concretas
con su fuente. No inventes datos; si no encuentras evidencia nueva fuerte para algo, dilo.

Entrega SOLO un reporte en Markdown en español, con esta estructura exacta:
1. Encabezado con fecha y "Próxima revisión" (+15 días).
2. Resumen ejecutivo (3-6 viñetas con la evidencia más fuerte y su cifra).
3. Tabla: variable candidata | evidencia/dato | fuente | cómo incorporarla | prioridad | origen(dato/supuesto).
4. Detalle por variable (definición, evidencia, incorporación: distribución/dependencias/efecto).
5. Cambios propuestos al esquema (snippets JSON ilustrativos) + nota de re-validación.
6. Fuentes (lista de URLs).
Marca cada propuesta como `dato` (anclado en fuente) o `supuesto`. Evita repetir variables
que ya existen o ya fueron propuestas; busca ángulos NUEVOS o recalibraciones con cifras frescas.
"""


def build_user_prompt(today: str, nxt: str) -> str:
    return f"""\
Fecha de hoy: {today}. Próxima revisión: {nxt}.

Variables YA en el modelo: {variables_actuales()}.
Variables YA propuestas en reportes previos (no repetir salvo recalibración con cifra nueva):
{YA_PROPUESTAS}.

Marginales objetivo actuales (no romper): tiene seguro ≈ 0.40, desconfía ≈ 0.48,
seguro de desastres ≈ 0.033.

Investiga evidencia reciente sobre comportamiento, percepción y demanda de seguros en Perú
(y LatAm como referencia) y produce el reporte en Markdown según la estructura indicada.
Cierra con la línea: "*Generado por el ciclo quincenal de fortalecimiento del modelo `lapuerta`.*"
"""


def call_claude(system: str, user: str) -> str:
    import anthropic

    client = anthropic.Anthropic()
    web_search = {"type": "web_search_20260209", "name": "web_search", "max_uses": 8}
    messages = [{"role": "user", "content": user}]
    for _ in range(6):  # tolera varios pause_turn del bucle de búsqueda server-side
        resp = client.messages.create(
            model=MODEL,
            max_tokens=8000,
            thinking={"type": "adaptive"},
            output_config={"effort": "medium"},
            system=system,
            tools=[web_search],
            messages=messages,
        )
        if resp.stop_reason == "refusal":
            raise RuntimeError("El modelo rechazó la solicitud.")
        if resp.stop_reason == "pause_turn":
            messages.append({"role": "assistant", "content": resp.content})
            continue
        break
    text = "".join(b.text for b in resp.content if getattr(b, "type", None) == "text")
    if not text.strip():
        raise RuntimeError("Respuesta vacía del modelo.")
    return text.strip()


ALTA_ROW_RE = re.compile(
    r"^\|\s*\d+\s*\|\s*`?([a-zA-Z_][a-zA-Z0-9_]*)`?[^|]*\|.*\|\s*\*{0,2}alta\*{0,2}\s*\|",
    re.MULTILINE | re.IGNORECASE,
)


def find_alta_variables(report_text: str) -> list[str]:
    """Extrae nombres de variables candidatas marcadas Prioridad=Alta en la tabla del reporte
    (columna final antes de 'origen'). 'Media-Alta' NO matchea (no es Alta pura)."""
    names: list[str] = []
    for m in ALTA_ROW_RE.finditer(report_text):
        name = m.group(1)
        if name not in names:
            names.append(name)
    return names


APPLY_SYSTEM = """\
Eres ingeniero de software del generador de usuarios sintéticos de seguros del Perú ("lapuerta").
Tu tarea: aplicar al código las variables candidatas de PRIORIDAD ALTA de un reporte quincenal que
ya fue redactado, siguiendo EXACTAMENTE los patrones de código ya existentes en los tres archivos
que te paso completos a continuación.

Reglas:
- Aplica SOLO variables marcadas Prioridad: Alta en la tabla del reporte. Ignora Media/Baja.
- No toques nada de las variables ya existentes, salvo agregar la(s) nueva(s) al final de su
  sección correspondiente.
- Sigue el patrón de nombres: `sample_<variable>(rng, schema, ...)` en
  generate_synthetic_users.py, wireada en generate_user() en orden de dependencia (después de
  que sus inputs ya estén calculados), y agregada al dict de retorno.
- En el esquema JSON: variables independientes/condicionales van en "variables"; variables
  derivadas de otras ya calculadas (como confianza_aseguradora o tenencia_seguro) van en
  "modelos_derivados".
- Si la variable es booleana con un intercepto logístico (patrón `score.intercepto` +
  `rng.random() < sigmoid(score)`), el efecto de mezcla sobre subgrupos heterogéneos casi
  siempre da una marginal poblacional MÁS ALTA que sigmoid(intercepto) solo — no necesitas
  acertar el intercepto exacto, quien te llama lo recalibra empíricamente después con un
  barrido automático. Usa el intercepto propuesto en el reporte como punto de partida.
- Actualiza matriz_usuarios_sinteticos.md: agrega la variable a la tabla correspondiente (§2 si
  es condicional, §3 si es derivada) y una nota de versión nueva (formato de las notas
  v1.1/v1.2 ya presentes: qué se añadió, de dónde viene, marginal esperada).
- NO cambies meta.version ni meta.fecha del JSON (los ajusta el script después).
- NO agregues nada de variables Media/Baja aunque el reporte las liste.

Devuelve SOLO tres bloques con el contenido COMPLETO y final de cada archivo (nunca un diff ni
un resumen — el archivo entero, listo para sobrescribir), en este formato exacto:

```FILE:schema.json
{...contenido JSON completo...}
```

```FILE:generate_synthetic_users.py
#!/usr/bin/env python3
...contenido completo del archivo...
```

```FILE:matriz_usuarios_sinteticos.md
# ...contenido completo del archivo...
```

Después de los tres bloques, en líneas aparte, para CADA variable nueva que sea booleana y tenga
una marginal objetivo declarada en el reporte (ej. "~6-8%"), agrega una línea:
CHECK: <nombre_variable> <bajo>-<alto>
(ejemplo: "CHECK: trabajo_plataforma_digital 0.06-0.08", con el bajo/alto como fracción 0-1).
Si una variable nueva no es booleana, o no tiene marginal objetivo declarada, no emitas línea
CHECK para ella.
"""


def build_apply_prompt(report_text: str, alta_vars: list[str]) -> str:
    parts = [f"Variables de prioridad Alta a aplicar: {', '.join(alta_vars)}.\n\n",
             "=== REPORTE ===\n", report_text, "\n\n"]
    for label, path in APPLY_FILES.items():
        with open(path, "r", encoding="utf-8") as f:
            parts.append(f"=== ARCHIVO ACTUAL: {label} ===\n{f.read()}\n\n")
    return "".join(parts)


def call_claude_text(system: str, user: str) -> str:
    import anthropic

    client = anthropic.Anthropic()
    resp = client.messages.create(
        model=MODEL,
        max_tokens=32000,
        thinking={"type": "adaptive"},
        output_config={"effort": "medium"},
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    if resp.stop_reason == "refusal":
        raise RuntimeError("El modelo rechazó la solicitud de aplicar cambios.")
    text = "".join(b.text for b in resp.content if getattr(b, "type", None) == "text")
    if not text.strip():
        raise RuntimeError("Respuesta vacía del modelo (aplicar Alta).")
    return text.strip()


FILE_BLOCK_RE = re.compile(r"```FILE:([^\n`]+)\n(.*?)```", re.DOTALL)
CHECK_RE = re.compile(r"^CHECK:\s*(\S+)\s+([\d.]+)\s*-\s*([\d.]+)\s*$", re.MULTILINE)


def parse_apply_response(text: str) -> tuple[dict[str, str], list[tuple[str, float, float]]]:
    files = {m.group(1).strip(): m.group(2) for m in FILE_BLOCK_RE.finditer(text)}
    checks = [(name, float(lo), float(hi)) for name, lo, hi in CHECK_RE.findall(text)]
    return files, checks


def _measure_marginal(var_name: str) -> float | None:
    """Recarga generate_synthetic_users.py desde disco y mide la tasa de True de un campo
    booleano sobre 20k usuarios (semilla fija: el resto de campos queda igual entre corridas,
    solo cambia el intercepto que se está barriendo, asi que el barrido es determinista)."""
    spec = importlib.util.spec_from_file_location("synthgen_fresh", GENERATOR_PATH)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    schema = mod.load_schema()
    rng = random.Random(42)
    users = [mod.generate_user(rng, schema, i) for i in range(20000)]
    if not users or var_name not in users[0] or not isinstance(users[0][var_name], bool):
        return None
    return sum(1 for u in users if u[var_name]) / len(users)


def _find_intercept_path(schema: dict, var_name: str) -> list[str] | None:
    for section in ("variables", "modelos_derivados"):
        node = schema.get(section, {}).get(var_name)
        if node and "score" in node and "intercepto" in node["score"]:
            return [section, var_name, "score", "intercepto"]
    return None


def _recalibrate_intercept(var_name: str, target_lo: float, target_hi: float) -> str:
    """Bisección sobre el intercepto hasta que la marginal empírica caiga en [lo, hi].
    Monótono por construcción (sigmoid(score) crece con el intercepto), así que la bisección
    converge; si no converge exacto en 16 pasos, deja el valor más cercano encontrado.
    Devuelve una nota legible para el changelog, o '' si no hizo falta tocar nada."""
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        schema = json.load(f)
    path = _find_intercept_path(schema, var_name)
    if not path:
        return ""

    def node_at(s: dict):
        n = s
        for key in path[:-1]:
            n = n[key]
        return n

    original = node_at(schema)[path[-1]]

    def set_intercept(value: float):
        s = schema
        node_at(s)[path[-1]] = value
        with open(SCHEMA_PATH, "w", encoding="utf-8") as f:
            json.dump(s, f, ensure_ascii=False, indent=2)
        return _measure_marginal(var_name)

    marg = _measure_marginal(var_name)
    if marg is None or target_lo <= marg <= target_hi:
        return ""

    target_mid = (target_lo + target_hi) / 2
    lo_x, hi_x = original - 4.0, original + 4.0
    best_x, best_marg = original, marg
    for _ in range(16):
        mid_x = (lo_x + hi_x) / 2
        m = set_intercept(mid_x)
        if m is None:
            break
        if abs(m - target_mid) < abs(best_marg - target_mid):
            best_x, best_marg = mid_x, m
        if target_lo <= m <= target_hi:
            best_x, best_marg = mid_x, m
            break
        if m > target_hi:
            hi_x = mid_x
        else:
            lo_x = mid_x

    set_intercept(best_x)
    ok = target_lo <= best_marg <= target_hi
    return (f"intercepto de `{var_name}` recalibrado automáticamente de {original} a "
            f"{best_x:.2f} (el propuesto daba {marg:.3f} de marginal; objetivo "
            f"[{target_lo},{target_hi}]; {'alcanzado' if ok else 'más cercano posible'}: "
            f"{best_marg:.3f})")


def apply_alta_proposals(report_text: str) -> list[str]:
    """Si el reporte tiene variables de Prioridad: Alta, las aplica al esquema/generador/matriz,
    recalibra sus interceptos empíricamente y corre validate.py --check. Si algo falla o la
    respuesta viene incompleta, revierte los 3 archivos y no aplica nada. Devuelve la lista de
    variables efectivamente aplicadas (para el mensaje de commit y el resumen)."""
    alta_vars = find_alta_variables(report_text)
    if not alta_vars:
        return []
    print(f"[i] Candidatas de prioridad Alta detectadas: {', '.join(alta_vars)}", file=sys.stderr)

    backups = {}
    for path in APPLY_FILES.values():
        with open(path, "r", encoding="utf-8") as f:
            backups[path] = f.read()

    def restore():
        for path, content in backups.items():
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

    try:
        resp = call_claude_text(APPLY_SYSTEM, build_apply_prompt(report_text, alta_vars))
        files, checks = parse_apply_response(resp)
        if not set(APPLY_FILES).issubset(files):
            print(f"[!] apply_alta_proposals: respuesta incompleta ({sorted(files)}); "
                  f"se descarta.", file=sys.stderr)
            return []
        for label, path in APPLY_FILES.items():
            with open(path, "w", encoding="utf-8") as f:
                f.write(files[label])
    except Exception as e:
        print(f"[!] apply_alta_proposals: {e}. Se descarta la aplicación automática.",
              file=sys.stderr)
        restore()
        return []

    try:
        for name, lo, hi in checks:
            note = _recalibrate_intercept(name, lo, hi)
            if note:
                print(f"[i] {note}", file=sys.stderr)

        check = subprocess.run(
            [sys.executable, VALIDATE_PATH, "--check", "--n", "20000", "--seed", "42"],
            capture_output=True, text=True, cwd=GENERADOR_DIR,
        )
        if check.returncode != 0:
            print("[!] validate.py --check FALLÓ tras aplicar Alta; se revierte todo.",
                  file=sys.stderr)
            print(check.stdout[-3000:], file=sys.stderr)
            restore()
            return []
    except Exception as e:
        print(f"[!] apply_alta_proposals: error validando ({e}); se revierte.", file=sys.stderr)
        restore()
        return []

    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        schema = json.load(f)
    try:
        major, minor = schema["meta"]["version"].split(".")
        schema["meta"]["version"] = f"{major}.{int(minor) + 1}"
    except Exception:
        pass
    schema["meta"]["fecha"] = dt.date.today().isoformat()
    with open(SCHEMA_PATH, "w", encoding="utf-8") as f:
        json.dump(schema, f, ensure_ascii=False, indent=2)

    print(f"[i] Aplicado y validado: {', '.join(alta_vars)}", file=sys.stderr)
    return alta_vars


def update_codex(date_str: str, rel_path: str) -> None:
    if not os.path.exists(CODEX):
        return
    with open(CODEX, "r", encoding="utf-8") as f:
        content = f.read()
    entry = f"- {date_str} — `{rel_path}`"
    if START in content and END in content:
        if entry in content:
            return
        content = content.replace(START, f"{START}\n{entry}", 1)
    else:  # crear la sección si no existe
        block = (
            "\n### 📌 Reportes quincenales (fortalecimiento del modelo)\n"
            f"Índice de reportes (auto-actualizado):\n{START}\n{entry}\n{END}\n"
        )
        content = content.rstrip() + "\n" + block
    with open(CODEX, "w", encoding="utf-8") as f:
        f.write(content)


def main(argv=None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args(argv)

    today = dt.date.today()
    nxt = today + dt.timedelta(days=15)
    today_s, nxt_s = today.isoformat(), nxt.isoformat()
    system, user = SYSTEM, build_user_prompt(today_s, nxt_s)

    if args.dry_run:
        print(f"[dry-run] modelo={MODEL}")
        print(f"[dry-run] system chars={len(system)}  user chars={len(user)}")
        print(f"[dry-run] escribiría research/updates/{today_s}_fortalecimiento_modelo.md")
        return 0

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERROR: falta ANTHROPIC_API_KEY", file=sys.stderr)
        return 2

    report = call_claude(system, user)
    os.makedirs(UPDATES_DIR, exist_ok=True)
    fname = f"{today_s}_fortalecimiento_modelo.md"
    out = os.path.join(UPDATES_DIR, fname)
    with open(out, "w", encoding="utf-8") as f:
        f.write(report + "\n")
    update_codex(today_s, f"research/updates/{fname}")

    applied = apply_alta_proposals(report)
    if applied:
        print(f"Aplicadas automáticamente al esquema (validado): {', '.join(applied)}")
    else:
        print("Sin variables de prioridad Alta aplicadas automáticamente en este ciclo.")

    print(f"OK → {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
