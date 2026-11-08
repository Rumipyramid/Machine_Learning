#!/usr/bin/env python3
"""Expediente privado de autoría, impacto y valor profesional (skill /notario).

Solo stdlib. Guarda hechos fechados en un JSONL y los convierte en un expediente
legible (línea de tiempo, argumentos por categoría, huecos y contraargumentos).

Regla dura de privacidad: el expediente SOLO se escribe en una ruta que git
ignore (por defecto `research/privado/`). Si la ruta quedaría versionada, el
script se niega a escribir. El repo puede ser público.

Uso:
  expediente.py init  <caso>
  expediente.py add   <caso> --cat autoria --fecha 2026-10-20 --titulo "..." \
                      --detalle "..." --fuente "..." --fuerza doc [--literal] \
                      [--testigos "A,B"] [--medido medido|estimado] [--refs "F-21,TABLERO:76"] \
                      [--respuesta "..."]   (solo para --cat contra)
  expediente.py list  <caso> [--cat X]
  expediente.py render <caso>              -> research/privado/expediente/<caso>.md
  expediente.py scan  [--autor "Nombre"] [--max 8] [--json]
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]  # raíz del repo
BASE = ROOT / "research" / "privado" / "expediente"

CATS = {
    "autoria": "Autoría — quién hizo qué y cuándo",
    "impacto": "Impacto — resultados con cifra y fuente",
    "valor": "Valor de la disciplina — evidencia externa",
    "senal": "Señales del entorno — lo que se dijo o decidió",
    "contra": "Contraargumentos — la mejor versión de la otra postura",
}
FUERZA = {
    "doc": ("🟢", "documental directa: metadato, historial de versiones, correo o invitación con fecha y autor"),
    "indirecto": ("🔵", "documental indirecta: tablero, minuta, acta, entregable sin firma"),
    "nota": ("🟡", "nota propia escrita el mismo día del hecho"),
    "recuerdo": ("🟠", "testimonio posterior o de oídas"),
    "inferencia": ("🔴", "interpretación: no es un hecho, es una lectura"),
}


# ---------------------------------------------------------------- privacidad
def ensure_private(path: Path) -> None:
    """Aborta si `path` no está ignorado por git (evita filtrar el caso a un repo público)."""
    try:
        r = subprocess.run(
            ["git", "-C", str(ROOT), "check-ignore", "-q", str(path)],
            capture_output=True,
        )
    except FileNotFoundError:
        print("⚠️  git no disponible: no puedo verificar que la ruta sea privada.", file=sys.stderr)
        return
    if r.returncode == 1:
        sys.exit(
            f"⛔ {path.relative_to(ROOT)} NO está en .gitignore. El expediente no se escribe en "
            "rutas versionadas. Agrega `research/privado/` al .gitignore."
        )
    if r.returncode not in (0, 1):  # 128 = no es repo git
        print("⚠️  No es un repo git: no puedo verificar privacidad.", file=sys.stderr)
    tracked = subprocess.run(
        ["git", "-C", str(ROOT), "ls-files", "--error-unmatch", str(path)],
        capture_output=True,
    )
    if tracked.returncode == 0:
        sys.exit(f"⛔ {path} ya está versionado en git. Sácalo con `git rm --cached` antes de seguir.")


def case_path(caso: str) -> Path:
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]{1,60}", caso):
        sys.exit("El nombre del caso va en kebab-case: minúsculas, números y guiones.")
    return BASE / f"{caso}.jsonl"


def load(caso: str) -> list[dict]:
    p = case_path(caso)
    if not p.exists():
        return []
    return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]


# ---------------------------------------------------------------- comandos
def cmd_init(a):
    p = case_path(a.caso)
    ensure_private(p)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.touch(exist_ok=True)
    print(f"Expediente listo: {p.relative_to(ROOT)} (privado, ignorado por git)")


def cmd_add(a):
    p = case_path(a.caso)
    ensure_private(p)
    p.parent.mkdir(parents=True, exist_ok=True)
    if a.cat not in CATS:
        sys.exit(f"Categoría inválida. Usa una de: {', '.join(CATS)}")
    if a.fuerza not in FUERZA:
        sys.exit(f"Fuerza inválida. Usa una de: {', '.join(FUERZA)}")
    try:
        dt.date.fromisoformat(a.fecha)
    except ValueError:
        sys.exit("--fecha debe ser AAAA-MM-DD (fecha del hecho, no del registro).")
    items = load(a.caso)
    entry = {
        "id": f"E-{len(items) + 1:03d}",
        "fecha_hecho": a.fecha,
        "fecha_registro": dt.date.today().isoformat(),
        "cat": a.cat,
        "titulo": a.titulo,
        "detalle": a.detalle or "",
        "fuente": a.fuente or "",
        "fuerza": a.fuerza,
        "literal": bool(a.literal),
        "testigos": [t.strip() for t in (a.testigos or "").split(",") if t.strip()],
        "medido": a.medido or "",
        "refs": [r.strip() for r in (a.refs or "").split(",") if r.strip()],
        "respuesta": a.respuesta or "",
    }
    with p.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    print(f"{entry['id']} registrado ({CATS[a.cat].split(' —')[0]}, {FUERZA[a.fuerza][0]}).")


def _line(e: dict) -> str:
    icon = FUERZA.get(e["fuerza"], ("?",))[0]
    extra = []
    if e.get("literal"):
        extra.append("cita literal")
    if e.get("medido"):
        extra.append(e["medido"])
    if e.get("testigos"):
        extra.append("testigos: " + ", ".join(e["testigos"]))
    tail = f" _({'; '.join(extra)})_" if extra else ""
    s = f"- {icon} **{e['fecha_hecho']} · {e['titulo']}** ({e['id']}){tail}"
    if e.get("detalle"):
        s += f"\n  {e['detalle']}"
    if e.get("fuente"):
        s += f"\n  Dónde se verifica: {e['fuente']}"
    if e.get("refs"):
        s += f"\n  Referencias: {', '.join(e['refs'])}"
    if e["cat"] == "contra":
        s += f"\n  Respuesta: {e['respuesta'] or '⚠️ SIN RESPUESTA TODAVÍA'}"
    return s


def actors_path(caso: str) -> Path:
    return BASE / f"{caso}.actores.json"


def load_actors(caso: str) -> list[dict]:
    p = actors_path(caso)
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else []


def cmd_actor(a):
    """Registra o actualiza a una persona del caso: rol, relación con el usuario y postura conocida."""
    p = actors_path(a.caso)
    ensure_private(p)
    p.parent.mkdir(parents=True, exist_ok=True)
    actors = [x for x in load_actors(a.caso) if x["nombre"] != a.nombre]
    actors.append({"nombre": a.nombre, "rol": a.rol or "", "relacion": a.relacion or "",
                   "postura": a.postura or "desconocida", "decide": a.decide or ""})
    p.write_text(json.dumps(actors, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Actor registrado: {a.nombre} ({a.rol}).")


def cmd_list(a):
    for e in load(a.caso):
        if a.cat and e["cat"] != a.cat:
            continue
        print(_line(e))


def gaps(items: list[dict]) -> list[str]:
    out = []
    by = {c: [e for e in items if e["cat"] == c] for c in CATS}
    if not any(e["fuerza"] == "doc" for e in by["autoria"]):
        out.append("Autoría sin prueba documental directa (🟢). Busca el historial de versiones del archivo, "
                   "el correo o la invitación con la que se compartió el borrador, y anota fecha y autor.")
    debiles = [e["id"] for e in by["senal"] if e["fuerza"] in ("recuerdo", "inferencia")]
    if debiles:
        out.append(f"Señales solo de oídas o recuerdo ({', '.join(debiles)}). Pide a quien estuvo presente que "
                   "escriba hoy una nota fechada con lo que se dijo (palabras exactas si las recuerda).")
    pendientes = [e["id"] for e in items if "PENDIENTE" in e.get("fuente", "")]
    if pendientes:
        out.append(f"Registros con fuente pendiente de conseguir: {', '.join(pendientes)}.")
    imp = by["impacto"]
    if imp and not any(e.get("medido") == "medido" for e in imp):
        out.append("Todo el impacto es estimado. Un solo resultado medido pesa más que diez proyecciones.")
    if not imp:
        out.append("No hay impacto registrado. Corre `scan` y revisa el tablero del equipo.")
    if not by["valor"]:
        out.append("Falta evidencia externa sobre el valor de la disciplina. Revisa references/argumentario.md.")
    sin_resp = [e["id"] for e in by["contra"] if not e.get("respuesta")]
    if not by["contra"]:
        out.append("No hay contraargumentos. Un caso sin la mejor versión de la otra postura no está listo.")
    elif sin_resp:
        out.append(f"Contraargumentos sin respuesta: {', '.join(sin_resp)}.")
    if sum(e["fuerza"] == "inferencia" for e in items) > len(items) / 2 and items:
        out.append("Más de la mitad del expediente son interpretaciones. Conviértelas en hechos o descártalas.")
    return out


def cmd_render(a):
    items = load(a.caso)
    out = BASE / f"{a.caso}.md"
    ensure_private(out)
    hoy = dt.date.today().isoformat()
    L = [f"# Expediente: {a.caso}", "",
         f"> Privado. Generado {hoy} por `/notario`. No se versiona. {len(items)} registros.", ""]
    actors = load_actors(a.caso)
    if actors:
        L += ["## Quién es quién", "", "| Persona | Rol | Relación con el usuario | Qué decide | Postura conocida |",
              "|---|---|---|---|---|"]
        L += [f"| {x['nombre']} | {x['rol']} | {x['relacion']} | {x['decide']} | {x['postura']} |" for x in actors]
        L.append("")
    L += ["## Escala de fuerza", ""] + [f"- {v[0]} {v[1]}" for v in FUERZA.values()] + [""]
    L += ["## Conteo", "", "| Categoría | Registros | 🟢 | 🔵 | 🟡 | 🟠 | 🔴 |", "|---|---|---|---|---|---|---|"]
    for c, name in CATS.items():
        sub = [e for e in items if e["cat"] == c]
        L.append(f"| {name.split(' —')[0]} | {len(sub)} | " +
                 " | ".join(str(sum(e['fuerza'] == k for e in sub)) for k in FUERZA) + " |")
    L += ["", "## Huecos a cerrar", ""] + ([f"- {g}" for g in gaps(items)] or ["- Ninguno detectado."])
    L += ["", "## Línea de tiempo (hechos del caso; sin evidencia externa ni contraargumentos)", ""]
    L += [f"- {e['fecha_hecho']} · {FUERZA[e['fuerza']][0]} {e['titulo']} ({e['id']}, {e['cat']})"
          for e in sorted(items, key=lambda x: x["fecha_hecho"]) if e["cat"] in ("autoria", "impacto", "senal")]
    for c, name in CATS.items():
        sub = sorted([e for e in items if e["cat"] == c], key=lambda x: x["fecha_hecho"])
        L += ["", f"## {name}", ""] + ([_line(e) for e in sub] or ["_(vacío)_"])
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"Expediente escrito en {out.relative_to(ROOT)}")


# ---------------------------------------------------------------- detección
SCAN = {
    "impacto": (
        ["TABLERO_BEHOLDER.md", "reportes", "research/_outputs"],
        r"(NPS\s*\d|CSAT|Wellby|S/\s?[\d.,]+\s?[kKmM]?|\+\d+\s?(pp|%|ptos)|retenci[oó]n|ahorro|liberaci[oó]n)",
    ),
    "valor": (
        ["research/fuentes/codice.md"],
        r"(?=.*(🟢 A|🔵 B))(?=.*(conductual|behavioral|nudge|megastud|experiment|RCT|comprensi[oó]n|adopci[oó]n|conversi[oó]n))",
    ),
    "contra": (
        ["research/fuentes/codice.md"],
        r"(se[ñn]al de problema|contracci[oó]n|no evidence|sin efecto|efecto (promedio )?(nulo|cero)|d=0\.0)",
    ),
}


def _grep(paths: list[str], pattern: str, limit: int, must: str | None = None) -> list[dict]:
    rx, mrx = re.compile(pattern, re.I), re.compile(must, re.I) if must else None
    hits = []
    for rel in paths:
        base = ROOT / rel
        files = [base] if base.is_file() else sorted(base.rglob("*.md")) if base.exists() else []
        for f in files:
            if "privado" in f.parts:
                continue
            for n, line in enumerate(f.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
                if rx.search(line) and (mrx is None or mrx.search(line)):
                    hits.append({"archivo": f"{f.relative_to(ROOT)}:{n}", "texto": line.strip()[:240]})
                    if len(hits) >= limit:
                        return hits
    return hits


def cmd_scan(a):
    res = {}
    if a.autor:
        log = subprocess.run(
            ["git", "-C", str(ROOT), "log", f"--author={a.autor}", "--date=short",
             "--format=%ad · %an · %s", f"-{a.max}"],
            capture_output=True, text=True,
        ).stdout.strip().splitlines()
        res["autoria (git)"] = [{"archivo": "git log", "texto": l} for l in log]
        res["autoria (tableros)"] = _grep(["TABLERO_BEHOLDER.md", "reportes"], re.escape(a.autor.split()[0]), a.max)
        res["impacto (con el autor)"] = _grep(SCAN["impacto"][0], SCAN["impacto"][1], a.max, must=re.escape(a.autor.split()[0]))
    for cat, (paths, pat) in SCAN.items():
        res[cat] = _grep(paths, pat, a.max)
    if a.json:
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return
    print("Candidatos detectados (no se registra nada solo; confirma cada uno con `add`).\n")
    for k, v in res.items():
        print(f"## {k} ({len(v)})")
        for h in v:
            print(f"- {h['archivo']} — {h['texto']}")
        print()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    s = sp.add_parser("init"); s.add_argument("caso"); s.set_defaults(f=cmd_init)
    s = sp.add_parser("add"); s.add_argument("caso")
    s.add_argument("--cat", required=True); s.add_argument("--fecha", required=True)
    s.add_argument("--titulo", required=True); s.add_argument("--detalle"); s.add_argument("--fuente")
    s.add_argument("--fuerza", required=True); s.add_argument("--literal", action="store_true")
    s.add_argument("--testigos"); s.add_argument("--medido", choices=["medido", "estimado"])
    s.add_argument("--refs"); s.add_argument("--respuesta"); s.set_defaults(f=cmd_add)
    s = sp.add_parser("actor"); s.add_argument("caso"); s.add_argument("--nombre", required=True)
    s.add_argument("--rol"); s.add_argument("--relacion"); s.add_argument("--postura"); s.add_argument("--decide")
    s.set_defaults(f=cmd_actor)
    s = sp.add_parser("list"); s.add_argument("caso"); s.add_argument("--cat"); s.set_defaults(f=cmd_list)
    s = sp.add_parser("render"); s.add_argument("caso"); s.set_defaults(f=cmd_render)
    s = sp.add_parser("scan"); s.add_argument("--autor"); s.add_argument("--max", type=int, default=8)
    s.add_argument("--json", action="store_true"); s.set_defaults(f=cmd_scan)
    a = ap.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
