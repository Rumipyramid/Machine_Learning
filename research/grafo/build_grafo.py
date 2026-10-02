#!/usr/bin/env python3
"""Grafologización del segundo cerebro (solo stdlib).

Lee la base de conocimiento (`research/_nodes`, `_outputs`, ledger `fuentes/codice.md`,
`lobo/`) y produce, de forma determinista y sin juicio de LLM:

  grafo.json       grafo completo (nodes, outputs, fuentes F-n, aristas tipadas)
  historial.jsonl  una instantánea por fecha (reconstruida desde git + ledger)
  ESTADO.md        reporte transparente: estado, evolución, enriquecimiento, auditoría
  grafo.html       visor autocontenido (sin dependencias externas)

Uso:  python research/grafo/build_grafo.py [--no-history]
Toda métrica se define en METRICAS.md; lo que NO mide está declarado en ESTADO.md §7.
"""
import json, re, subprocess, sys, datetime as dt
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
RES = HERE.parent
ROOT = RES.parent
DESIGN = "tendencias-diseno-innovacion"
# Rangos F-n que CLAUDE.md declara como cosecha de diseño/innovación (para medir huérfanos).
DESIGN_RANGES = [(237, 328, "diseño"), (380, 429, "diseño"), (430, 468, "innovación")]
RIGOR = {"🟢": "A", "🔵": "B", "🟡": "C", "🟠": "D", "🔴": "E"}
LEDGER_NAMES = ["research/fuentes/codice.md", "research/fuentes/registro_fuentes.md"]

FREF = re.compile(r"\bF-(\d+)\b")
WIKI = re.compile(r"\[\[([a-z0-9][a-z0-9-]*)(?:\|[^\]]*)?\]\]", re.S)


def git(*a):
    r = subprocess.run(["git", "-C", str(ROOT), *a], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


# ---------- parsers (aceptan texto, para servir también a instantáneas históricas) ----------
def parse_ledger(text):
    rows = {}
    for l in text.splitlines():
        m = re.match(r"\| F-(\d+) \|", l)
        if not m:
            continue
        c = [x.strip() for x in l.split("|")]
        rig = next((RIGOR[k] for k in RIGOR if k in c[5][:4]), "?") if len(c) > 5 else "?"
        rows[int(m.group(1))] = {
            "id": int(m.group(1)), "autor": c[2], "anio": c[3], "titulo": c[4][:140],
            "rigor": rig, "fecha": c[9] if len(c) > 9 else ""}
    return rows


def explicit_cites(text):
    """F-n individuales; los rangos 'F-a a F-b' no se expanden (no inflar citas)."""
    return {int(n) for n in FREF.findall(text)}


def parse_design(text):
    h = Counter()
    hyp = {}
    for l in text.splitlines():
        m = re.match(r"\|\s*\*\*H(\d+)\*\*\s*\|(.*?)\|(.*?)\|", l)
        if m:
            s = m.group(3)
            st = next((k for k in ("refutada", "respaldada", "parcial", "abierta") if k in s[:140]), "otra")
            hyp[int(m.group(1))] = st
            h[st] += 1
    rules = re.findall(r"^- \*\*(C\d+) —", text, re.M)
    rules_cited = 0
    for blk in re.split(r"(?m)^- \*\*C\d+ —", text)[1:]:
        if FREF.search(blk.split("\n- **")[0][:1500]):
            rules_cited += 1
    scale = Counter()
    sec = re.search(r"## 5\..*?(?=\n## 6\.)", text, re.S)
    if sec:
        for l in sec.group(0).splitlines():
            if l.startswith("| **"):
                for e in ("🟢", "🟡", "🔴", "⚔️"):
                    if e in l.split("|")[2][:12]:
                        scale[e] += 1
                        break
    iters = re.findall(r"(?m)^\| (\d+) \| (20\d\d-\d\d-\d\d) \|", text)
    return {"hyp": dict(h), "hyp_by_id": hyp, "rules": len(rules), "rules_cited": rules_cited,
            "scale": dict(scale), "iterations": len(iters), "lines": text.count("\n") + 1,
            "iter_dates": [d for _, d in iters]}


def graph_from(nodes_txt, outputs_txt):
    """nodes_txt/outputs_txt: {slug: texto}. Devuelve aristas wikilink y derivación."""
    slugs = set(nodes_txt)
    links = set()
    for a, t in nodes_txt.items():
        for b in WIKI.findall(t):
            if b in slugs and b != a:
                links.add((a, b))
    derive = set()
    for o, t in outputs_txt.items():
        for s in slugs:
            if s in t:
                derive.add((o, s))
    return links, derive


def components(names, und):
    seen, comps = set(), []
    for n in names:
        if n in seen:
            continue
        st, c = [n], set()
        while st:
            x = st.pop()
            if x in c:
                continue
            c.add(x)
            st += [y for y in und[x] if y not in c]
        seen |= c
        comps.append(c)
    return comps


# ---------- carga del estado actual ----------
def load_now():
    nodes = {p.stem: p.read_text() for p in sorted((RES / "_nodes").glob("*.md"))}
    outs = {p.name: p.read_text() for p in sorted((RES / "_outputs").glob("*")) if p.is_file()}
    ledger = parse_ledger((RES / "fuentes/codice.md").read_text())
    return nodes, outs, ledger


def lobo_state():
    p = RES / "lobo/fuentes_leidas_lobo.md"
    leidas = {int(n) for n in re.findall(r"(?m)^\| F-(\d+) \|", p.read_text())} if p.exists() else set()
    ops = (RES / "lobo/opinion_experto.md").read_text() if (RES / "lobo/opinion_experto.md").exists() else ""
    return {"fuentes_leidas": len(leidas), "leidas": leidas,
            "intuiciones": len(re.findall(r"(?m)^### \d+\. ", ops.split("## 🧠 Intuición acumulada")[-1].split("## 📔")[0])) if "## 🧠" in ops else 0,
            "tesis": len(re.findall(r"(?m)^### \d+\. ", ops.split("## 🎯")[1].split("## 💰")[0])) if "## 🎯" in ops else 0}


def alma_dates():
    out = {}
    for l in (RES / "alma.md").read_text().splitlines():
        m = re.match(r"\| `_nodes/([a-z0-9-]+)\.md` \|", l)
        if not m:
            continue
        c = [x.strip() for x in l.split("|")]
        d = next((x for x in c[2:] if re.fullmatch(r"\d{4}-\d\d-\d\d", x)), "n/d")
        v = next((re.search(r"v\d+(?:\.\d+)?", x).group(0) for x in c[3:] if re.search(r"v\d+(?:\.\d+)?", x)), "—")
        out[m.group(1)] = (d, v)
    return out


# ---------- historial ----------
def snapshot_at(commit):
    ls = git("ls-tree", "-r", "--name-only", commit, "research/_nodes", "research/_outputs") or ""
    names = ls.split()
    nodes = {Path(n).stem: git("show", f"{commit}:{n}") or "" for n in names if "/_nodes/" in n and n.endswith(".md")}
    outs = {Path(n).name: git("show", f"{commit}:{n}") or "" for n in names if "/_outputs/" in n}
    led_txt = next((t for t in (git("show", f"{commit}:{n}") for n in LEDGER_NAMES) if t), "")
    led = parse_ledger(led_txt)
    links, derive = graph_from(nodes, outs)
    d = parse_design(nodes.get(DESIGN, "")) if DESIGN in nodes else None
    cited = set()
    for t in nodes.values():
        cited |= explicit_cites(t)
    snap = {"fuentes": len(led), "rigor": dict(Counter(r["rigor"] for r in led.values())),
            "nodes": len(nodes), "outputs": len(outs), "wikilinks": len(links),
            "derivaciones": len(derive), "fuentes_citadas_en_nodes": len(cited & set(led))}
    if d:
        snap["diseno"] = {k: d[k] for k in ("hyp", "rules", "rules_cited", "scale", "iterations", "lines")}
        snap["diseno"]["cites"] = len(explicit_cites(nodes[DESIGN]) & set(led))
    return snap


def build_history():
    log = git("log", "--reverse", "--format=%H %ad", "--date=short", "--", "research") or ""
    byday = {}
    for l in log.splitlines():
        h, d = l.split()
        byday[d] = h  # último commit del día
    hist = []
    for d, h in sorted(byday.items()):
        s = snapshot_at(h)
        s.update(fecha=d, commit=h[:7], fuente="git")
        hist.append(s)
    return hist


def ledger_timeline(ledger):
    """Reconstrucción pre-git desde la columna fecha del ledger (acumulado de fuentes registradas)."""
    per = defaultdict(Counter)
    for r in ledger.values():
        if re.match(r"\d{4}-\d\d-\d\d", r["fecha"]):
            per[r["fecha"][:10]][r["rigor"]] += 1
    acc, out = 0, []
    for d in sorted(per):
        acc += sum(per[d].values())
        out.append({"fecha": d, "nuevas": sum(per[d].values()), "acumuladas": acc,
                    "AB": per[d]["A"] + per[d]["B"], "rigor": dict(per[d])})
    return out


# ---------- métricas ----------
def compute(nodes, outs, ledger):
    links, derive = graph_from(nodes, outs)
    names = sorted(nodes)
    und = {n: set() for n in names}
    for a, b in links:
        und[a].add(b); und[b].add(a)
    recip = [(a, b) for a, b in links if (b, a) in links]
    nonrecip = sorted((a, b) for a, b in links if (b, a) not in links)
    comps = components(names, und)
    cites = {n: explicit_cites(t) for n, t in nodes.items()}
    allc = set().union(*cites.values()) if cites else set()
    cnt = Counter(f for s in cites.values() for f in s)
    des = parse_design(nodes[DESIGN]) if DESIGN in nodes else None
    dcit = cites.get(DESIGN, set())
    in_range = {f for a, b, _ in DESIGN_RANGES for f in range(a, b + 1) if f in ledger}
    jacc = []
    for n in names:
        if n == DESIGN:
            continue
        u = dcit | cites[n]
        j = len(dcit & cites[n]) / len(u) if u else 0
        jacc.append({"node": n, "compartidas": len(dcit & cites[n]), "jaccard": round(j, 3),
                     "enlazado_dir": (DESIGN, n) in links or (n, DESIGN) in links})
    jacc.sort(key=lambda x: -x["compartidas"])
    ab = lambda S: sum(1 for f in S if ledger.get(f, {}).get("rigor") in "AB")
    return {
        "links": links, "derive": derive, "recip": recip, "nonrecip": nonrecip, "comps": comps,
        "cites": cites, "allc": allc, "cnt": cnt, "des": des, "dcit": dcit, "in_range": in_range,
        "jacc": jacc, "ab": ab, "und": und}


def pct(a, b):
    return f"{100*a/b:.0f}%" if b else "n/d"


def repo_first_date():
    ds = (git("log", "--format=%ad", "--date=short") or "").split()
    return min(ds) if ds else "n/d"


def git_dates(slug_path):
    out = git("log", "--format=%ad", "--date=short", "--", slug_path) or ""
    ds = out.split()
    return (ds[-1], ds[0], len(ds)) if ds else ("n/d", "n/d", 0)


def report(nodes, outs, ledger, M, hist, tl, lobo, alma):
    today = dt.date.today().isoformat()
    L = []
    w = L.append
    des, dcit = M["des"], M["dcit"]
    w(f"# 🕸️ Grafo del segundo cerebro — ESTADO\n\n*Generado: {today} por `research/grafo/build_grafo.py` "
      f"(determinista, sin LLM). No editar a mano: se regenera. Definiciones: `METRICAS.md`.*\n")
    w("> **Transparencia:** cada cifra de este reporte sale de contar archivos del repo. Lo que no se puede "
      "medir está listado en §7. Un número alto aquí significa *más material y mejor enlazado*, **no** que el "
      "conocimiento sea *verdadero* ni que haya tenido impacto fuera del repo.\n")
    # 1
    w("## 1. Estado actual (qué hay)\n")
    rig = Counter(r["rigor"] for r in ledger.values())
    w("| Capa | Cantidad | Detalle |\n|---|---|---|")
    w(f"| Nodes (`_nodes/`) | {len(nodes)} | {sum(t.count(chr(10))+1 for t in nodes.values()):,} líneas |")
    w(f"| Outputs (`_outputs/`) | {len(outs)} | derivan de nodes: {len({o for o,_ in M['derive']})} de {len(outs)} citan algún node |")
    w(f"| Fuentes en el ledger | {len(ledger)} | 🟢A {rig['A']} · 🔵B {rig['B']} · 🟡C {rig['C']} · 🟠D {rig['D']} · 🔴E {rig['E']} · otras/sin clasificar {len(ledger)-sum(rig[k] for k in 'ABCDE')} |")
    w(f"| Aristas wikilink (node→node) | {len(M['links'])} | recíprocas: {len(M['recip'])} de {len(M['links'])} ({pct(len(M['recip']),len(M['links']))}) |")
    w(f"| Fuentes citadas por ≥1 node | {len(M['allc'] & set(ledger))} de {len(ledger)} | {pct(len(M['allc'] & set(ledger)),len(ledger))} del ledger; **{len(ledger)-len(M['allc'] & set(ledger))} viven solo en el ledger** |")
    w(f"| Fuentes citadas por ≥2 nodes (transversales) | {sum(1 for f,c in M['cnt'].items() if c>=2 and f in ledger)} | evidencia reutilizada entre temas |")
    rel = RES / "grafo/relaciones/estado.json"
    if rel.exists():
        rj = json.loads(rel.read_text()); nf = len({f for b in rj["barridos"] for f in b["f_ids"]})
        nt = sum(1 for _ in (RES / "grafo/relaciones/triples.jsonl").open())
        w(f"| **Grafo semántico** (relaciones extraídas) | {nf} de {len(ledger)} fuentes ({pct(nf,len(ledger))}) | {nt} relaciones · {len(rj['barridos'])} barridos · detalle en `relaciones/RELACIONES.md` |")
    w(f"| Componentes conexas del grafo de nodes | {len(M['comps'])} | {'grafo conexo' if len(M['comps'])==1 else 'HAY islas: ' + '; '.join(sorted(','.join(sorted(c)) for c in M['comps'] if len(c)<len(nodes)))} |\n")
    # 2 diseño
    w("## 2. Segundo cerebro de DISEÑO (`tendencias-diseno-innovacion`)\n")
    if des:
        hy = des["hyp"]; tot = sum(hy.values()); res = tot - hy.get("abierta", 0)
        dab = M["ab"](dcit)
        w("| Indicador | Valor | Cómo leerlo |\n|---|---|---|")
        w(f"| Iteraciones de bitácora | {des['iterations']} ({', '.join(sorted(set(des['iter_dates'])))}) | cuántas veces se confrontó el node |")
        w(f"| Tamaño | {des['lines']:,} líneas | crecimiento ≠ calidad; ver trazabilidad |")
        w(f"| Fuentes citadas explícitamente | {len(dcit & set(ledger))} | F-n individuales dentro del node |")
        w(f"| …de rigor A/B | {dab} ({pct(dab,len(dcit & set(ledger)))}) | solidez de la base |")
        w(f"| Hipótesis vivas | {tot}: abierta {hy.get('abierta',0)} · parcial {hy.get('parcial',0)} · respaldada {hy.get('respaldada',0)} · refutada {hy.get('refutada',0)} | tablero §6 |")
        w(f"| **Falsabilidad ejercida** | {pct(res,tot)} ({res}/{tot}) | hipótesis que ya se movieron de `abierta` |")
        w(f"| **Tasa de autocorrección** | {pct(hy.get('refutada',0),res)} ({hy.get('refutada',0)}/{res}) | de las resueltas, cuántas se refutaron: 0% sostenido sería señal de confirmación sesgada |")
        w(f"| Reglas de criterio | {des['rules']} | §7 |")
        w(f"| **Trazabilidad de reglas** | {pct(des['rules_cited'],des['rules'])} ({des['rules_cited']}/{des['rules']}) | reglas con ≥1 F-n en su propio párrafo |")
        sc = des["scale"]
        w(f"| Escala de madurez §5 | 🟢 {sc.get('🟢',0)} · 🟡 {sc.get('🟡',0)} · 🔴 {sc.get('🔴',0)} · ⚔️ {sc.get('⚔️',0)} | dónde está el peso de la evidencia |")
        orphan = sorted(M["in_range"] - dcit)
        w(f"| **Huérfanos de cita** | {len(orphan)} de {len(M['in_range'])} ({pct(len(orphan),len(M['in_range']))}) | fuentes en los rangos de diseño/innovación (CLAUDE.md) registradas pero **sin cita individual** en el node (pueden estar en un rango 'F-a a F-b' o en otro node) |")
        elsewhere = [f for f in orphan if M["cnt"].get(f, 0) > 0]
        w(f"| …de ellos citados en otro node | {len(elsewhere)} | no están perdidos, solo fuera del node de diseño |\n")
        w("**Vecinos por evidencia compartida** (candidatos a conexión; ✅ = ya enlazado por wikilink):\n")
        w("| Node | F-n compartidas | Jaccard | Enlazado |\n|---|---|---|---|")
        for j in M["jacc"]:
            w(f"| `{j['node']}` | {j['compartidas']} | {j['jaccard']} | {'✅' if j['enlazado_dir'] else '❌ sin enlace'} |")
        w("")
    # 3 evolución
    w("## 3. Evolución\n")
    w("### 3.1 Enriquecimiento del ledger por fecha de registro (reconstruido, cubre desde el origen)\n")
    w("*Fuente: columna `fecha` del ledger. Es la fecha en que `cronista` registró cada F-n, no la fecha del estudio.*\n")
    w("| Fecha | Nuevas | Acumuladas | de ellas A/B | Barra |\n|---|---|---|---|---|")
    for r in tl:
        w(f"| {r['fecha']} | {r['nuevas']} | {r['acumuladas']} | {r['AB']} | {'█'*max(1,round(r['nuevas']/4))} |")
    w("\n### 3.2 Instantáneas por git (estado completo del grafo en cada día con commits)\n")
    w("*Fuente: `git show` de cada commit. **El clon es superficial (shallow)**: el historial verificable empieza en "
      f"{hist[0]['fecha'] if hist else 'n/d'}; antes de eso solo vale §3.1.*\n")
    w("| Fecha | Commit | Fuentes | Nodes | Outputs | Wikilinks | Fuentes citadas | Diseño: líneas | H abiertas | H resueltas | Reglas |\n|---|---|---|---|---|---|---|---|---|---|---|")
    last = None
    for s in hist:
        d = s.get("diseno") or {}
        hy = d.get("hyp", {}); op = hy.get("abierta", 0); rs = sum(hy.values()) - op
        key = (s["fuentes"], s["nodes"], s["outputs"], s["wikilinks"], d.get("lines"), op, d.get("rules"))
        if key == last:
            continue  # solo filas donde algo cambió
        last = key
        w(f"| {s['fecha']} | `{s['commit']}` | {s['fuentes']} | {s['nodes']} | {s['outputs']} | {s['wikilinks']} | {s['fuentes_citadas_en_nodes']} | {d.get('lines','–')} | {op if d else '–'} | {rs if d else '–'} | {d.get('rules','–')} |")
    w("\n*(Se omiten los días sin cambio en estas columnas.)*\n")
    # 4 impacto
    w("## 4. Métricas de impacto (definidas en `METRICAS.md`)\n")
    ab_all = rig["A"] + rig["B"]
    w("| Métrica | Valor | Qué dice | Qué NO dice |\n|---|---|---|---|")
    w(f"| M1 Base sólida (A+B / ledger) | {pct(ab_all,len(ledger))} | proporción de evidencia primaria/oficial | no que el hallazgo sea cierto |")
    w(f"| M2 Cobertura de citación | {pct(len(M['allc'] & set(ledger)),len(ledger))} | cuánto del ledger sostiene algún node | un node puede citar mal |")
    w(f"| M3 Reciprocidad de enlaces | {pct(len(M['recip']),len(M['links']))} | cumplimiento de la regla 5 de `alma.md` | calidad del enlace |")
    if des:
        w(f"| M4 Falsabilidad ejercida (diseño) | {pct(sum(des['hyp'].values())-des['hyp'].get('abierta',0), sum(des['hyp'].values()))} | el node confronta, no solo acumula | que las pruebas fueran rigurosas |")
        w(f"| M5 Trazabilidad de reglas (diseño) | {pct(des['rules_cited'],des['rules'])} | las reglas se apoyan en fuentes | que la fuente sea la correcta |")
        w(f"| M6 Integración (diseño↔resto) | {sum(1 for j in M['jacc'] if j['enlazado_dir'])}/{len(M['jacc'])} nodes enlazados; {sum(1 for j in M['jacc'] if j['compartidas']>0)} comparten evidencia | el diseño informa a los demás temas | uso real por personas |")
    w(f"| M7 Lectura profunda (Lobo) | {lobo['fuentes_leidas']} fuentes leídas a fondo = {pct(lobo['fuentes_leidas'],len(ledger))} del ledger; {lobo['intuiciones']} intuiciones | el cerebro se relee, no solo crece | que las intuiciones sean correctas |\n")
    # 5 salud
    w("## 5. Auditoría de integridad (fallas reales, sin maquillar)\n")
    issues = []
    dang = sorted((n, f) for n, s in M["cites"].items() for f in s if f not in ledger)
    issues.append(("F-n citadas en un node pero **ausentes del ledger**", dang))
    issues.append(("Wikilinks **no recíprocos** (viola regla 5)", [f"{a} → {b}" for a, b in M["nonrecip"]]))
    broken = sorted({(a, b) for a, t in nodes.items() for b in WIKI.findall(t) if b not in nodes and b != a})
    issues.append(("Wikilinks **rotos** (destino inexistente)", [f"{a} → {b}" for a, b in broken]))
    iso = [n for n in nodes if not M["und"][n]]
    issues.append(("Nodes **aislados** (sin enlaces)", iso))
    nl = [n for n in nodes if n not in alma]
    issues.append(("Nodes **ausentes** de la tabla de `alma.md`", nl))
    stale = []
    for n in nodes:
        if n in alma:
            gd = git_dates(f"research/_nodes/{n}.md")[1]
            if gd != "n/d" and gd > repo_first_date() and gd > alma[n][0]:
                stale.append(f"{n} (alma {alma[n][0]} < git {gd})")
    issues.append((f"Nodes **más nuevos que su fecha en `alma.md`** (solo se juzga si el último commit es posterior al inicio del historial visible, {repo_first_date()}; antes es indeterminable)", stale))
    outs_no = [o for o in outs if o not in {a for a, _ in M["derive"]}]
    issues.append(("Outputs que **no citan ningún node** (viola regla 4)", outs_no))
    for t, items in issues:
        w(f"- {'✅' if not items else '⚠️'} {t}: **{len(items)}**" + (" — " + ", ".join(map(str, items[:12])) + (" …" if len(items) > 12 else "") if items else ""))
    w("")
    # 6 nodes
    w("## 6. Tabla por node\n")
    w("| Node | Líneas | F-n citadas | A/B | Enlaces ent./sal. | Última modif. visible (git) | alma |\n|---|---|---|---|---|---|---|")
    for n in sorted(nodes, key=lambda x: -len(M["cites"][x])):
        s = {f for f in M["cites"][n] if f in ledger}
        ent = sum(1 for a, b in M["links"] if b == n); sal = sum(1 for a, b in M["links"] if a == n)
        fm = git_dates(f"research/_nodes/{n}.md")
        w(f"| `{n}` | {nodes[n].count(chr(10))+1} | {len(s)} | {M['ab'](s)} | {ent}/{sal} | {fm[1] if fm[1] > repo_first_date() else 'indeterminada (≤ ' + repo_first_date() + ', historial truncado)'} | {alma.get(n,('—','—'))[0]} {alma.get(n,('','—'))[1]} |")
    w("")
    # 7
    w("## 7. Límites declarados de esta medición\n")
    for x in [
        "**Historial git truncado:** el clon es superficial; las instantáneas (§3.2) empiezan en la fecha indicada. §3.1 reconstruye el ledger desde su columna `fecha`, que puede ser corregida a mano y no prueba *cuándo* se leyó la fuente.",
        "**Citar no es validar:** M2/M5 cuentan referencias `F-n`, no si la cita respalda la afirmación (eso lo audita el chequeo de eco de cita del propio node, no este script).",
        "**Rangos 'F-a a F-b' no se expanden:** si un node cita un rango, esas fuentes cuentan como huérfanas aquí. Es deliberado: un rango no es trazabilidad por afirmación.",
        "**Rigor A–E es el del ledger** (juicio de `cronista`), no re-evaluado aquí.",
        "**Hipótesis y reglas se leen por formato** (`| **Hn** |`, `- **Cn —`). Si el node cambia de formato, las métricas de diseño caerán a 0: tomarlo como alarma de parser, no como pérdida de conocimiento.",
        "**Sin métricas de uso externo:** no hay datos de quién lee, reutiliza ni decide con este cerebro. Impacto real = pendiente; lo único medible hoy es estructura, trazabilidad y autocorrección.",
        "**Wikilinks se cuentan en todo el texto del node**, no solo en `## Conexiones`.",
    ]:
        w(f"- {x}")
    w("\n---\n*Visor interactivo: `research/grafo/grafo.html` · grafo crudo: `grafo.json` · serie: `historial.jsonl`.*")
    return "\n".join(L) + "\n"


def export_graph(nodes, outs, ledger, M):
    G = {"nodes": [], "edges": []}
    for n, t in nodes.items():
        G["nodes"].append({"id": n, "type": "node", "lines": t.count("\n") + 1,
                           "cites": len(M["cites"][n] & set(ledger)), "design": n == DESIGN})
    for o in outs:
        G["nodes"].append({"id": o, "type": "output", "lines": 0, "cites": 0})
    for a, b in sorted(M["links"]):
        G["edges"].append({"s": a, "t": b, "k": "wikilink", "recip": (b, a) in M["links"]})
    for a, b in sorted(M["derive"]):
        G["edges"].append({"s": a, "t": b, "k": "deriva"})
    cited_by = defaultdict(list)
    for n, s in M["cites"].items():
        for f in s:
            if f in ledger:
                cited_by[f].append(n)
    for f, r in ledger.items():
        G["nodes"].append({"id": f"F-{f}", "type": "fuente", "rigor": r["rigor"], "titulo": r["titulo"],
                           "autor": r["autor"], "anio": r["anio"], "huerfana": f not in cited_by})
        for n in cited_by.get(f, []):
            G["edges"].append({"s": n, "t": f"F-{f}", "k": "cita"})
    return G


def main():
    nodes, outs, ledger = load_now()
    M = compute(nodes, outs, ledger)
    hist = [] if "--no-history" in sys.argv else build_history()
    if "--no-history" in sys.argv and (HERE / "historial.jsonl").exists():
        hist = [json.loads(l) for l in (HERE / "historial.jsonl").read_text().splitlines() if l]
    tl = ledger_timeline(ledger)
    lobo = lobo_state()
    alma = alma_dates()
    (HERE / "historial.jsonl").write_text("".join(json.dumps(s, ensure_ascii=False) + "\n" for s in hist))
    G = export_graph(nodes, outs, ledger, M)
    G["meta"] = {"generado": dt.date.today().isoformat(), "timeline": tl, "hist": hist,
                 "design": {k: v for k, v in (M["des"] or {}).items() if k != "hyp_by_id"}}
    (HERE / "grafo.json").write_text(json.dumps(G, ensure_ascii=False, indent=1))
    (HERE / "ESTADO.md").write_text(report(nodes, outs, ledger, M, hist, tl, lobo, alma))
    tpl = (HERE / "visor.template.html").read_text()
    (HERE / "grafo.html").write_text(tpl.replace("/*__DATA__*/null", json.dumps(G, ensure_ascii=False)))
    print(f"ok: {len(nodes)} nodes, {len(outs)} outputs, {len(ledger)} fuentes, {len(M['links'])} wikilinks, {len(hist)} instantáneas")


if __name__ == "__main__":
    main()
