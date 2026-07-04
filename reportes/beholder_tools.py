#!/usr/bin/env python3
"""Herramientas del Beholder. Fuente de verdad: TABLERO_BEHOLDER.md + reportes/beholder.config.md.

Uso:
  python reportes/beholder_tools.py validar   # picos, vacaciones, vencidos, sin programar (exit 1 si hay rojo)
  python reportes/beholder_tools.py digest    # escribe reportes/DIGEST.md (semana pasada + semana próxima)
  python reportes/beholder_tools.py gantt     # regenera la sección Gantt (mermaid) del tablero
  python reportes/beholder_tools.py retro     # monedas estimadas vs. días invertidos (calibración)
"""
import csv
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TABLERO = ROOT / "TABLERO_BEHOLDER.md"
CONFIG = ROOT / "reportes" / "beholder.config.md"
CAMBIOS = ROOT / "reportes" / "historial" / "CAMBIOS.csv"
DIGEST = ROOT / "reportes" / "DIGEST.md"
REGLA_MAX_SIMULTANEAS = 8


def parse_fecha(s):
    m = re.match(r"(\d{2})/(\d{2})/(\d{4})", s.strip())
    return date(int(m.group(3)), int(m.group(2)), int(m.group(1))) if m else None


def parse_tablero():
    """Lee las tablas de detalle del tablero (12 columnas) y devuelve la lista de quests."""
    quests, epica = [], None
    for line in TABLERO.read_text(encoding="utf-8").splitlines():
        m = re.match(r"### (EPIC-\d+) · (.+)", line)
        if m:
            epica = {"id": m.group(1), "nombre": m.group(2).strip()}
            continue
        if not line.startswith("| Q-"):
            continue
        c = [x.strip() for x in line.split("|")[1:-1]]
        if len(c) != 12:  # otras tablas (dependencias, riesgos, impacto) no calzan
            continue
        (clave, nombre, estado, status, interv, f_ini, f_fin,
         monedas_s, bds_s, perfiles, riesgos, impacto) = c
        coins = [float(x) for x in re.findall(r"([\d.]+)\s*🪙", monedas_s)]
        bds = ([b.strip() for b in bds_s.split(",")]
               if bds_s not in ("—", "Todos", "(por confirmar)") else [])
        monedas = dict(zip(bds, coins)) if bds and len(bds) == len(coins) else {}
        dias_m = re.search(r"\((\d+) días?\)", status)
        quests.append(dict(
            clave=clave, nombre=re.sub(r"\*\*", "", nombre), epica=epica,
            estado=estado, status=status, intervencion=interv,
            inicio=parse_fecha(f_ini), cierre=parse_fecha(f_fin),
            monedas=monedas, monedas_total=sum(coins), bds=bds_s,
            perfiles=perfiles, riesgos=riesgos, impacto=impacto,
            dias=int(dias_m.group(1)) if dias_m else None,
        ))
    return quests


def parse_roster():
    """Roster de la config: {nombre: {nivel, vacaciones: [(ini, fin), ...]}}."""
    roster, en_tabla = {}, False
    for line in CONFIG.read_text(encoding="utf-8").splitlines():
        if line.startswith("### Equipo"):
            en_tabla = True
            continue
        if en_tabla and line.startswith("### "):
            break
        if en_tabla and line.startswith("|") and "Miembro" not in line and "---" not in line:
            c = [x.strip() for x in line.split("|")[1:-1]]
            if len(c) < 4:
                continue
            vac = [(parse_fecha(m.group(1)), parse_fecha(m.group(2)))
                   for m in re.finditer(
                       r"(\d{2}/\d{2}/\d{4})\s*(?:a|–|-)\s*(\d{2}/\d{2}/\d{4})", c[2])]
            roster[c[0]] = dict(nivel=c[1].replace("*", ""), vacaciones=vac)
    return roster


def cargas_diarias(quests):
    """{persona: {fecha: monedas simultáneas}} sumando iniciativas cuyas fechas se solapan."""
    cargas = {}
    for q in quests:
        if not (q["inicio"] and q["cierre"] and q["monedas"]):
            continue
        d = q["inicio"]
        while d <= q["cierre"]:
            for p, n in q["monedas"].items():
                cargas.setdefault(p, {})
                cargas[p][d] = cargas[p].get(d, 0) + n
            d += timedelta(days=1)
    return cargas


def evaluar(hoy=None):
    """Evalúa reglas y devuelve (rojos, amarillos, picos)."""
    hoy = hoy or date.today()
    quests, roster = parse_tablero(), parse_roster()
    rojos, amarillos, picos = [], [], {}

    cargas = cargas_diarias(quests)
    for p, dias in sorted(cargas.items()):
        pico = max(dias.values())
        dias_pico = sorted(d for d, v in dias.items() if v == pico)
        picos[p] = (pico, dias_pico[0], dias_pico[-1])
        if pico > REGLA_MAX_SIMULTANEAS:
            rojos.append(f"{p} viola la regla de capacidad: pico {pico:g} 🪙 "
                         f"({dias_pico[0]:%d/%m}–{dias_pico[-1]:%d/%m}) > {REGLA_MAX_SIMULTANEAS}")

    for p, info in roster.items():
        for vi, vf in info["vacaciones"]:
            if vf < hoy:
                continue
            for q in quests:
                if (q["monedas"].get(p) and q["inicio"] and q["cierre"]
                        and q["inicio"] <= vf and vi <= q["cierre"]):
                    rojos.append(f"{p} tiene {q['clave']} agendado durante sus vacaciones "
                                 f"({vi:%d/%m}–{vf:%d/%m}); capacidad en vacaciones = 0")

    for q in quests:
        if q["cierre"] and q["cierre"] < hoy and q["estado"] != "Done":
            rojos.append(f"{q['clave']} venció el {q['cierre']:%d/%m} y sigue en {q['estado']} "
                         "(¿se entregó o se mueve la fecha con aprobación del owner?)")
        if q["monedas_total"] > 0 and not q["inicio"] and q["estado"] != "Done":
            amarillos.append(f"{q['clave']} tiene {q['monedas_total']:g} 🪙 asignadas sin programar")
        if q["cierre"] and q["estado"] == "To Do" and hoy <= q["cierre"] <= hoy + timedelta(days=7) \
                and q["inicio"] and q["inicio"] < hoy:
            amarillos.append(f"{q['clave']} entrega en ≤7 días ({q['cierre']:%d/%m}) y sigue en To Do")
    return rojos, amarillos, picos


def cmd_validar():
    rojos, amarillos, picos = evaluar()
    print("== Picos de concurrencia (regla: ≤ %d 🪙 simultáneas) ==" % REGLA_MAX_SIMULTANEAS)
    for p, (pico, d1, d2) in sorted(picos.items(), key=lambda kv: -kv[1][0]):
        marca = ("⛔" if pico > REGLA_MAX_SIMULTANEAS
                 else "🟡 al límite" if pico == REGLA_MAX_SIMULTANEAS else "🟢")
        print(f"  {p}: {pico:g} 🪙 ({d1:%d/%m} → {d2:%d/%m}) {marca}")
    print("\n== 🚨 Códigos rojos ==")
    print("\n".join(f"  🚨 {r}" for r in rojos) if rojos else "  (ninguno)")
    print("\n== ⚠️ Códigos amarillos ==")
    print("\n".join(f"  ⚠️ {a}" for a in amarillos) if amarillos else "  (ninguno)")
    if rojos:
        print("\nRESULTADO: HAY CÓDIGO ROJO — corregir antes de publicar.")
        sys.exit(1)
    print("\nRESULTADO: OK para publicar.")


def cmd_digest():
    hoy = date.today()
    quests = parse_tablero()
    rojos, amarillos, picos = evaluar()

    recientes = []
    if CAMBIOS.exists():
        with open(CAMBIOS, encoding="utf-8") as f:
            for fila in csv.DictReader(f):
                if datetime.fromisoformat(fila["timestamp"]).date() >= hoy - timedelta(days=7):
                    recientes.append(fila)

    prox_entregas = sorted((q for q in quests if q["cierre"] and q["estado"] != "Done"
                            and hoy <= q["cierre"] <= hoy + timedelta(days=7)),
                           key=lambda q: q["cierre"])
    prox_inicios = sorted((q for q in quests if q["inicio"]
                           and hoy < q["inicio"] <= hoy + timedelta(days=7)),
                          key=lambda q: q["inicio"])

    L = [f"# 📰 Digest Beholder — semana del {hoy:%d/%m/%Y}", ""]
    L += ["## 🚨 Códigos activos"]
    L += [f"- 🚨 {r}" for r in rojos] + [f"- ⚠️ {a}" for a in amarillos] or ["- 🟢 Sin códigos."]
    if not (rojos or amarillos):
        L += ["- 🟢 Sin códigos."]
    L += ["", "## 📦 Entregas de los próximos 7 días"]
    L += [f"- **{q['clave']}** {q['nombre']} — cierra **{q['cierre']:%d/%m}** ({q['bds']})"
          for q in prox_entregas] or ["- (ninguna)"]
    L += ["", "## 🚀 Inicios de los próximos 7 días"]
    L += [f"- **{q['clave']}** {q['nombre']} — arranca **{q['inicio']:%d/%m}** ({q['bds']})"
          for q in prox_inicios] or ["- (ninguno)"]
    L += ["", "## 🪙 Picos de la semana (capacidad)"]
    L += [f"- {p}: pico {pico:g} 🪙 ({d1:%d/%m}–{d2:%d/%m})"
          for p, (pico, d1, d2) in sorted(picos.items(), key=lambda kv: -kv[1][0])]
    L += ["", f"## 📝 Cambios de los últimos 7 días ({len(recientes)})"]
    L += [f"- {f['timestamp'][:10]} · **{f['autor']}** · {f['clave']} · {f['campo']}: "
          f"{f['antes']} → {f['despues']}" for f in recientes] or ["- (sin cambios)"]
    L += ["", "---", "*Generado con `python reportes/beholder_tools.py digest`.*", ""]
    DIGEST.write_text("\n".join(L), encoding="utf-8")
    print(f"Digest escrito en {DIGEST.relative_to(ROOT)} "
          f"({len(recientes)} cambios, {len(prox_entregas)} entregas próximas).")


def cmd_gantt():
    quests = parse_tablero()
    L = ["```mermaid", "gantt", "  dateFormat YYYY-MM-DD", "  axisFormat %d/%m",
         "  title Roadmap Q3-2026 — Behavioral Design"]
    epica_actual = None
    for q in quests:
        if not (q["inicio"] and q["cierre"]):
            continue
        if q["epica"]["id"] != epica_actual:
            epica_actual = q["epica"]["id"]
            L.append(f"  section {q['epica']['nombre'][:28]}")
        tags = []
        if "🚩" in q["riesgos"]:
            tags.append("crit")
        if q["estado"] == "Done":
            tags.append("done")
        elif q["estado"] == "In Progress":
            tags.append("active")
        tag = (", ".join(tags) + ", ") if tags else ""
        nombre = q["nombre"].replace(":", " —")[:40]
        fin = q["cierre"] + timedelta(days=1)  # mermaid trata el fin como exclusivo
        L.append(f"  {q['clave']} {nombre} :{tag}{q['inicio']:%Y-%m-%d}, {fin:%Y-%m-%d}")
    L.append("```")
    texto = TABLERO.read_text(encoding="utf-8")
    nuevo = re.sub(r"(<!-- GANTT:START -->).*?(<!-- GANTT:END -->)",
                   lambda m: m.group(1) + "\n" + "\n".join(L) + "\n" + m.group(2),
                   texto, flags=re.S)
    if nuevo == texto and "<!-- GANTT:START -->" not in texto:
        print("No encontré los marcadores <!-- GANTT:START/END --> en el tablero.")
        sys.exit(1)
    TABLERO.write_text(nuevo, encoding="utf-8")
    print(f"Gantt regenerado en el tablero ({sum(1 for q in quests if q['inicio'])} barras).")


def cmd_retro():
    quests = [q for q in parse_tablero() if q["dias"] and q["monedas_total"] > 0]
    print("== Retro de estimaciones: monedas vs. días invertidos ==")
    print(f"{'Clave':7} {'🪙':>5} {'días':>5} {'🪙/día':>7}  Iniciativa")
    filas = sorted(quests, key=lambda q: -(q["monedas_total"] / q["dias"]))
    for q in filas:
        ratio = q["monedas_total"] / q["dias"]
        marca = " ⚠️ revisar" if ratio >= 1.5 or ratio <= 0.15 else ""
        print(f"{q['clave']:7} {q['monedas_total']:5g} {q['dias']:5d} {ratio:7.2f}  "
              f"{q['nombre'][:48]}{marca}")
    if filas:
        media = sum(q["monedas_total"] / q["dias"] for q in filas) / len(filas)
        print(f"\nRatio medio del equipo: {media:.2f} 🪙/día. "
              "Al cierre del Q3, comparar contra días reales para calibrar el Q4.")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    {"validar": cmd_validar, "digest": cmd_digest,
     "gantt": cmd_gantt, "retro": cmd_retro}.get(cmd, lambda: print(__doc__))()
