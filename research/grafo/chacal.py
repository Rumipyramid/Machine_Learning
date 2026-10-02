#!/usr/bin/env python3
"""/Chacal — auditor del segundo cerebro (solo stdlib).

  python research/grafo/chacal.py [--extractos]   perfil de evidencia de las 3 preguntas (determinista)
  python research/grafo/chacal.py guardar r.json  compone la nota en research/garaje/ con las respuestas de Mu y el veredicto

r.json = {"q1": {"respuesta": "...", "veredicto": "...", "apuntes": ["..."]}, "q2": {...}, "q3": {...},
          "global": {"veredicto": "...", "prioridades": ["..."]}}
"""
import json, re, sys, subprocess, datetime as dt
from collections import Counter
from pathlib import Path

H = Path(__file__).resolve().parent
RES = H.parent
G = RES / "garaje"
sys.path.insert(0, str(H))
import build_grafo as bg

R = json.loads((H / "chacal_rubrica.json").read_text())
today = dt.date.today()
nodes, outs, ledger = bg.load_now()
alma = bg.alma_dates()
REL = H / "relaciones"
tri = [json.loads(l) for l in (REL / "triples.jsonl").read_text().splitlines() if l]
est = json.loads((REL / "estado.json").read_text())
sem_f = {int(f[2:]) for b in est["barridos"] for f in b["f_ids"]}
lec = {}
for t in tri: lec.setdefault(int(t["f"][2:]), set()).add(t["lectura"])
resueltas = {r["triple"] for r in est.get("resoluciones", [])}
pct = lambda a, b: round(100 * a / b) if b else 0


def year(s):
    ys = [int(y) for y in re.findall(r"(?<!\d)(19\d\d|20\d\d)(?!\d)", s or "")]
    return max(ys) if ys else None


def perfil(q):
    ns = [n for n in q["nodes"] if n in nodes]
    cites = set()
    for n in ns: cites |= bg.explicit_cites(nodes[n])
    srcs = sorted(f for f in cites if f in ledger)
    rig = Counter(ledger[f]["rigor"] for f in srcs)
    ys = [year(ledger[f]["anio"]) for f in srcs]
    known = [y for y in ys if y]
    ages = []
    for n in ns:
        d = alma.get(n, ("n/d",))[0]
        try: ages.append((today - dt.date.fromisoformat(d)).days)
        except Exception: pass
    sem = [f for f in srcs if f in sem_f]
    deep = [f for f in sem if lec.get(f, {"ficha"}) - {"ficha"}]
    tens = [t for t in tri if t["p"] in ("contradice", "refuta") and int(t["f"][2:]) in srcs]
    tens_open = [t for t in tens if t["id"] not in resueltas]
    disc = [d for d in est["discrepancias"] if d.get("estado") != "cerrada" and int(d["f"][2:]) in srcs]
    regs = [dt.date.fromisoformat(ledger[f]["fecha"][:10]) for f in srcs if re.match(r"\d{4}-\d\d-\d\d", ledger[f]["fecha"])]
    ult = max(regs) if regs else None
    P = {"ultima_fuente": str(ult) if ult else None, "ultima_fuente_dias": (today - ult).days if ult else None,
         "edad_node_dias": max(ages) if ages else None, "nodes": ns, "nodes_faltantes": [n for n in q["nodes"] if n not in nodes],
         "lineas": sum(nodes[n].count("\n") + 1 for n in ns), "edad_node_max_dias": max(ages) if ages else None,
         "edad_node_min_dias": min(ages) if ages else None, "fuentes": len(srcs), "rigor": dict(rig),
         "ab_pct": pct(rig["A"] + rig["B"], len(srcs)), "anio_conocido": len(known),
         "recientes_pct": pct(sum(1 for y in known if y >= today.year - 1), len(known)),
         "anio_max": max(known) if known else None, "semantica_pct": pct(len(sem), len(srcs)),
         "leidas_pct": pct(len(deep), len(sem)), "tensiones": len(tens), "tensiones_abiertas": len(tens_open),
         "discrepancias_abiertas": len(disc), "abiertas": len(tens_open) + len(disc)}
    if "tendencias-diseno-innovacion" in ns:
        h = bg.parse_design(nodes["tendencias-diseno-innovacion"])["hyp"]; P["hipotesis"] = h
    return P


def semaforo(P):
    D = R["dimensiones"]; out = {}
    def ok(v, lim):
        for k, x in lim.items():
            if k.endswith("_min") and not (v[k[:-4]] is not None and v[k[:-4]] >= x): return False
            if k.endswith("_max") and not (v[k[:-4]] is not None and v[k[:-4]] <= x): return False
        return True
    m = dict(P); m["fuentes"] = P["fuentes"]
    for d, c in D.items():
        out[d] = "verde" if ok(m, c["verde"]) else ("amarillo" if ok(m, c["amarillo"]) else "rojo")
    if P["fuentes"] == 0: out = {d: "rojo" for d in D}
    if P["semantica_pct"] < 10 and out["contradicciones"] == "verde": out["contradicciones"] = "amarillo"
    return out


ICON = {"verde": "🟢", "amarillo": "🟡", "rojo": "🔴"}
perfiles = {q["id"]: perfil(q) for q in R["preguntas"]}
sems = {k: semaforo(p) for k, p in perfiles.items()}


def extracto(n, k=1100):
    t = nodes[n]; m = re.search(r"(?m)^## [^\n]*(Resumen|resumen|Hallazgos|Síntesis)[^\n]*\n", t)
    s = t[m.end():] if m else t.split("\n", 3)[-1]
    s = re.split(r"(?m)^## ", s)[0]
    return re.sub(r"\s+", " ", s)[:k]


if len(sys.argv) > 1 and sys.argv[1] == "guardar":
    ans = json.loads(Path(sys.argv[2]).read_text())
    G.mkdir(exist_ok=True)
    nivel = subprocess.run([sys.executable, str(H / "mu.py")], capture_output=True, text=True).stdout.splitlines()[0]
    commit = subprocess.run(["git", "-C", str(RES.parent), "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip()
    prev = [json.loads(l) for l in (G / "bitacora.jsonl").read_text().splitlines() if l] if (G / "bitacora.jsonl").exists() else []
    L = [f"# 🐺 Auditoría del Chacal — {today}", "",
         f"*Commit `{commit}` · {nivel} · rúbrica: `research/grafo/chacal_rubrica.json` (umbrales propuestos, editables).*", "",
         "> El Chacal le pregunta a Mu y mide con qué evidencia respondió. **Los semáforos son medidos; el veredicto es juicio del auditor y no los contradice.** "
         "Una respuesta fluida no es una respuesta respaldada.", ""]
    dims = list(R["dimensiones"])
    L += ["## Tablero", "", "| Pregunta | " + " | ".join(dims) + " |", "|---|" + "---|" * len(dims)]
    for q in R["preguntas"]:
        L.append(f"| {q['id'].upper()} — {q['texto'][:60]}… | " + " | ".join(ICON[sems[q['id']][d]] for d in dims) + " |")
    if prev:
        p0 = prev[-1]; ch = []
        for q in R["preguntas"]:
            for d in dims:
                a, b = p0["semaforos"].get(q["id"], {}).get(d), sems[q["id"]][d]
                if a and a != b: ch.append(f"{q['id'].upper()}·{d}: {ICON[a]}→{ICON[b]}")
        L += ["", f"**Cambios desde la auditoría del {p0['fecha']}:** " + ("; ".join(ch) if ch else "ninguno")]
    for q in R["preguntas"]:
        P, S, A = perfiles[q["id"]], sems[q["id"]], ans[q["id"]]
        L += ["", f"## {q['id'].upper()} — {q['texto']}", "", "### Respuesta de Mu", "", A["respuesta"], "", "### Perfil de evidencia (medido)", "",
              "| Dimensión | Semáforo | Medida |", "|---|---|---|",
              f"| cobertura | {ICON[S['cobertura']]} | {len(P['nodes'])} nodes ({P['lineas']:,} líneas), {P['fuentes']} fuentes citadas" + (f"; faltan: {', '.join(P['nodes_faltantes'])}" if P['nodes_faltantes'] else "") + " |",
              f"| vigencia | {ICON[S['vigencia']]} | node más viejo {P['edad_node_max_dias']} d (más nuevo {P['edad_node_min_dias']} d); última fuente registrada {P['ultima_fuente']} (hace {P['ultima_fuente_dias']} d); {P['recientes_pct']}% de las fuentes con año ≥ {today.year-1} (año conocido en {P['anio_conocido']}/{P['fuentes']}; máx. {P['anio_max']}) |",
              f"| solidez | {ICON[S['solidez']]} | A/B = {P['ab_pct']}% · rigor {dict(sorted(P['rigor'].items()))} |",
              f"| contradicciones | {ICON[S['contradicciones']]} | {P['tensiones_abiertas']} tensiones sin resolver (de {P['tensiones']}) + {P['discrepancias_abiertas']} discrepancias abiertas" + (" — **ciego**: <10% del corpus tiene relaciones extraídas" if P['semantica_pct'] < 10 else "") + " |",
              f"| profundidad | {ICON[S['profundidad']]} | {P['semantica_pct']}% de las fuentes con relaciones extraídas; {P['leidas_pct']}% de ellas leídas más allá de la ficha |"]
        if "hipotesis" in P: L.append(f"| hipótesis (diseño) | — | {P['hipotesis']} |")
        L += ["", "### Veredicto del Chacal", "", A["veredicto"], "", "### Apuntes", ""] + [f"- {x}" for x in A["apuntes"]]
    g = ans["global"]
    L += ["", "## Evaluación global del segundo cerebro", "", g["veredicto"], "", "### Prioridades (ordenadas)", ""] + [f"{i}. {x}" for i, x in enumerate(g["prioridades"], 1)]
    fn = G / f"{today}_auditoria.md"; n = 2
    while fn.exists(): fn = G / f"{today}_auditoria_{n}.md"; n += 1
    fn.write_text("\n".join(L) + "\n")
    with (G / "bitacora.jsonl").open("a") as fh:
        fh.write(json.dumps({"fecha": str(today), "archivo": fn.name, "commit": commit, "nivel": nivel, "semaforos": sems,
                             "metricas": {k: {x: v for x, v in p.items() if not isinstance(v, (list, dict))} for k, p in perfiles.items()}}, ensure_ascii=False) + "\n")
    rows = [json.loads(l) for l in (G / "bitacora.jsonl").read_text().splitlines() if l]
    idx = ["# 🚗 Garaje — índice de auditorías del Chacal", "", "| Fecha | Nota | " + " | ".join(q["id"].upper() for q in R["preguntas"]) + " |", "|---|---|" + "---|" * len(R["preguntas"])]
    for r in reversed(rows):
        idx.append(f"| {r['fecha']} | [{r['archivo']}]({r['archivo']}) | " + " | ".join("".join(ICON[v] for v in r["semaforos"][q["id"]].values()) for q in R["preguntas"]) + " |")
    idx += ["", "*Cada celda: 🟢🟡🔴 en el orden cobertura · vigencia · solidez · contradicciones · profundidad.*"]
    (G / "INDICE.md").write_text("\n".join(idx) + "\n")
    print("nota:", fn)
else:
    for q in R["preguntas"]:
        P, S = perfiles[q["id"]], sems[q["id"]]
        print(f"\n[{q['id']}] {q['texto']}\n  semáforos: " + " ".join(f"{d}={ICON[v]}" for d, v in S.items()))
        print("  " + json.dumps({k: v for k, v in P.items() if k != "nodes"}, ensure_ascii=False))
        if "--extractos" in sys.argv:
            for n in P["nodes"][:3]: print(f"  ▸ {n}: {extracto(n)}")
