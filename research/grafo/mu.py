#!/usr/bin/env python3
"""/Mu — panel brutalista del segundo cerebro (solo stdlib). Escribe research/grafo/mu.html e imprime un resumen.

Cada número sale de contar archivos (ver METRICAS.md). Sin índices compuestos inventados: titulares = cifras crudas.
Uso: python research/grafo/mu.py [--sin-git]
"""
import json, re, sys, subprocess, datetime as dt
from collections import Counter, defaultdict
from html import escape as E
from pathlib import Path

H = Path(__file__).resolve().parent
sys.path.insert(0, str(H))
import build_grafo as bg

REL = H / "relaciones"
SIN_GIT = "--sin-git" in sys.argv


def sh(*a):
    r = subprocess.run(a, capture_output=True, text=True, cwd=H)
    return r.stdout.strip() if r.returncode == 0 else "n/d"


def pct(a, b):
    return round(100 * a / b) if b else 0


# ---------- datos ----------
nodes, outs, ledger = bg.load_now()
M = bg.compute(nodes, outs, ledger)
alma = bg.alma_dates()
lobo = bg.lobo_state()
tl = bg.ledger_timeline(ledger)
des = M["des"] or {"hyp": {}, "rules": 0, "rules_cited": 0, "scale": {}, "iterations": 0, "lines": 0}
audit = bg.audit(nodes, outs, ledger, M, alma)

tri = [json.loads(l) for l in (REL / "triples.jsonl").read_text().splitlines() if l] if (REL / "triples.jsonl").exists() else []
ent = json.loads((REL / "entidades.json").read_text()) if (REL / "entidades.json").exists() else {}
est = json.loads((REL / "estado.json").read_text()) if (REL / "estado.json").exists() else {"barridos": [], "discrepancias": []}
sem_f = {f for b in est["barridos"] for f in b["f_ids"]}
src_by_ent = defaultdict(set)
for t in tri:
    src_by_ent[t["s"]].add(t["f"]); src_by_ent[t["o"]].add(t["f"])
conv = sum(1 for s in src_by_ent.values() if len(s) >= 2)
lec = Counter(t["lectura"] for t in tri)
tens = sum(1 for t in tri if t["p"] in ("contradice", "refuta"))
_res = {r["triple"]: r["estado"] for r in est.get("resoluciones", [])}
tens_open = sum(1 for t in tri if t["p"] in ("contradice", "refuta") and t["id"] not in _res)
tens_real = sum(1 for t in tri if t["p"] in ("contradice", "refuta") and _res.get(t["id"]) == "alcance_distinto")
rig = Counter(r["rigor"] for r in ledger.values())
hy = des["hyp"]; htot = sum(hy.values()); hres = htot - hy.get("abierta", 0)
cit_all = M["allc"] & set(ledger)
dcit = M["dcit"] & set(ledger)
orphans = sorted(M["in_range"] - M["dcit"])
fails = [(lbl, it) for lbl, it in audit if it]
n_checks = len(audit) + 2  # + discrepancias abiertas + entidades sin relaciones
sem_orph = len(set(ent) - {x for t in tri for x in (t["s"], t["o"])})
open_disc = sum(1 for d in est["discrepancias"] if d.get("estado") != "cerrada")
checks_ok = len(audit) - len(fails) + (1 if open_disc == 0 else 0) + (1 if sem_orph == 0 else 0)
commit = sh("git", "rev-parse", "--short", "HEAD") if not SIN_GIT else "n/d"
branch = sh("git", "branch", "--show-current") if not SIN_GIT else "n/d"
today = dt.date.today().isoformat()


# ---------- nivel de inteligencia ----------
NIV = json.loads((H / "niveles.json").read_text())["niveles"]
VAL = {"fuentes": len(ledger), "nodes": len(nodes), "citadas_pct": pct(len(cit_all), len(ledger)),
       "fallas_integridad": len(fails), "reciprocidad_pct": pct(len(M["recip"]), len(M["links"])),
       "cobertura_sem_pct": pct(len(sem_f), len(ledger)), "entidades": len(ent), "convergencias": conv,
       "reglas_trazables_pct": pct(des["rules_cited"], des["rules"]), "falsabilidad_pct": pct(hres, htot),
       "base_diseno_ab_pct": pct(M["ab"](dcit), len(dcit)), "autocorreccion_pct": pct(hy.get("refutada", 0), hres),
       "tensiones_resueltas_pct": pct(sum(1 for t in tri if t["p"] in ("contradice", "refuta") and t["id"] in {r["triple"] for r in est.get("resoluciones", [])}), tens),
       "discrepancias_abiertas": open_disc,
       "leidas_pct": pct(lec["abstract"] + lec["completa"], len(tri)), "uso_externo_medido": 0}


def crit_ok(c):
    v = VAL[c["id"]]
    return v >= c["min"] if "min" in c else v <= c["max"]


def crit_prog(c):  # 0..1
    v = VAL[c["id"]]
    if "min" in c: return min(1, v / c["min"]) if c["min"] else 1
    return 1 if v <= c["max"] else 0


for lv in NIV:
    lv["ok"] = all(crit_ok(c) for c in lv["criterios"])
    lv["prog"] = sum(crit_prog(c) for c in lv["criterios"]) / len(lv["criterios"])
nivel = 0
for lv in NIV:
    if lv["ok"]: nivel += 1
    else: break
sig = NIV[nivel] if nivel < len(NIV) else None
nombre_nivel = NIV[nivel - 1]["nombre"] if nivel else "ARCHIVO"

# ---------- SVG ----------
def bars(items, w=460, rowh=20, label_w=150, maxv=None, accent=None):
    """items: [(label, value, shade 0-1 | None, texto_derecha)]"""
    maxv = maxv or max([v for _, v, *_ in items] + [1])
    h = rowh * len(items) + 4
    o = [f'<svg viewBox="0 0 {w} {h}" role="img">']
    for i, it in enumerate(items):
        lab, v = it[0], it[1]
        txt = it[3] if len(it) > 3 else str(v)
        y = i * rowh + 2
        bw = (w - label_w - 60) * v / maxv
        cls = "acc" if accent and lab in accent else "fg"
        o.append(f'<text x="0" y="{y+14}" class="t">{E(lab[:22])}</text>'
                 f'<rect x="{label_w}" y="{y+2}" width="{max(bw,1):.1f}" height="{rowh-6}" class="{cls}"/>'
                 f'<text x="{label_w+bw+5:.1f}" y="{y+14}" class="t b">{E(txt)}</text>')
    o.append("</svg>")
    return "".join(o)


def stack(parts, w=460, h=26):
    tot = sum(v for _, v, _ in parts) or 1
    x, o = 0, [f'<svg viewBox="0 0 {w} {h+16}" role="img">']
    for lab, v, cls in parts:
        bw = w * v / tot
        if v:
            o.append(f'<rect x="{x:.1f}" y="0" width="{bw:.1f}" height="{h}" class="{cls}"/>')
            if bw > 22:
                o.append(f'<text x="{x+4:.1f}" y="{h-8}" class="t b inv">{v}</text>')
        x += bw
    leg, lx = [], 0
    for lab, v, cls in parts:
        leg.append(f'<text x="{lx}" y="{h+13}" class="t s">{E(lab)} {v}</text>'); lx += 18 + 6.2 * (len(lab) + len(str(v)) + 1)
    return "".join(o) + "".join(leg) + "</svg>"


def cols(series, w=900, h=130):
    mx = max([v for _, v in series] + [1]); n = len(series); bw = (w - 10) / n
    o = [f'<svg viewBox="0 0 {w} {h+30}" role="img">']
    for i, (lab, v) in enumerate(series):
        bh = (h - 16) * v / mx
        o.append(f'<rect x="{5+i*bw+2:.1f}" y="{h-bh:.1f}" width="{bw-4:.1f}" height="{bh:.1f}" class="fg"/>'
                 f'<text x="{5+i*bw+bw/2:.1f}" y="{h-bh-3:.1f}" class="t s" text-anchor="middle">{v}</text>'
                 f'<text x="{5+i*bw+bw/2:.1f}" y="{h+12}" class="t s" text-anchor="middle">{lab[5:]}</text>')
    o.append("</svg>")
    return "".join(o)


def cell(big, label, sub="", warn=False):
    return f'<div class="c{" w" if warn else ""}"><div class="big">{big}</div><div class="lab">{E(label)}</div><div class="sub">{E(sub)}</div></div>'


def escalera(w=720, h=230):
    bw = w / len(NIV)
    o = [f'<svg viewBox="0 0 {w} {h+52}" role="img">']
    for i, lv in enumerate(NIV):
        bh = 50 + (h - 50) * (i + 1) / len(NIV)
        x, y = i * bw + 4, h - bh
        o.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw-8:.1f}" height="{bh:.1f}" fill="none" stroke="var(--fg)" stroke-width="3"/>')
        if i < nivel:
            o.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw-8:.1f}" height="{bh:.1f}" class="fg"/>')
        elif i == nivel:
            fh = bh * lv["prog"]
            o.append(f'<rect x="{x:.1f}" y="{h-fh:.1f}" width="{bw-8:.1f}" height="{fh:.1f}" class="acc"/>')
        pc = f'{round(lv["prog"]*100)}%'
        col = "inv" if i < nivel else ""
        o.append(f'<text x="{x+8:.1f}" y="{y+24:.1f}" class="t b {col}" font-size="20">N{lv["n"]}</text>')
        if i >= nivel:
            o.append(f'<text x="{x+bw/2-4:.1f}" y="{y+bh-8:.1f}" class="t b" font-size="15" text-anchor="middle" fill="var(--fg)" style="paint-order:stroke;stroke:var(--bg);stroke-width:4px">{pc}</text>')
        nm = {"AUTOCORRECCIÓN": "AUTOCORREC."}.get(lv["nombre"], lv["nombre"])
        o.append(f'<text x="{x+bw/2-4:.1f}" y="{h+20}" class="t b" font-size="12" text-anchor="middle">{E(nm)}</text>')
        o.append(f'<text x="{x+bw/2-4:.1f}" y="{h+38}" class="t" font-size="12" text-anchor="middle">{"✓ " if i < nivel else ""}{pc}</text>')
    o.append("</svg>")
    return "".join(o)


def fmtv(c):
    v = VAL[c["id"]]
    if c["id"] == "uso_externo_medido": return "NO MEDIDO"
    return f"{v} / {'≥' + str(c['min']) if 'min' in c else '≤' + str(c['max'])}"


crit_rows = ""
for lv in NIV:
    state = "LOGRADO" if (lv["ok"] and lv["n"] <= nivel) else ("SIGUIENTE" if lv["n"] == nivel + 1 else "BLOQUEADO")
    for j, c in enumerate(lv["criterios"]):
        ok = crit_ok(c)
        lab = f"N{lv['n']} {lv['nombre']}" if j == 0 else ""
        crit_rows += (f'<tr class="{"" if ok else "ko"}"><td>{lab}</td>'
                      f'<td>{state if j == 0 else ""}</td><td>{E(c["label"])}</td><td class="r">{E(fmtv(c))}</td><td>{"✓" if ok else "✗"}</td>'
                      f'<td><svg viewBox="0 0 100 10"><rect width="{100*crit_prog(c):.0f}" height="10" class="fg"/></svg></td></tr>')
falta = ""
if sig:
    falta = "<ul>" + "".join(f'<li class="ko"><b>✗</b> {E(c["label"])}: {E(fmtv(c))}</li>' for c in sig["criterios"] if not crit_ok(c)) + "</ul>"

# ---------- secciones ----------
sal = [cell(f"{checks_ok}/{n_checks}", "CHEQUEOS OK", "integridad, ver lista", checks_ok < n_checks),
       cell(len(M["nonrecip"]), "ENLACES NO RECÍPROCOS", f"de {len(M['links'])}", bool(M["nonrecip"])),
       cell(f"{pct(len(M['recip']),len(M['links']))}%", "RECIPROCIDAD", "regla 5 de alma.md", len(M["recip"]) < len(M["links"])),
       cell(open_disc, "DISCREPANCIAS ABIERTAS", "ledger vs fuente", open_disc > 0),
       cell(len(orphans), "HUÉRFANOS DE CITA", f"de {len(M['in_range'])} en rangos de diseño", len(orphans) > 0),
       cell(len(ledger) - len(cit_all), "FUENTES SIN NODE", f"{pct(len(ledger)-len(cit_all),len(ledger))}% del ledger", False)]
checklist = "".join(f'<li class="{"ko" if it else "ok"}"><b>{"✗" if it else "✓"}</b> {E(re.sub(r"[*`]", "", l))}'
                    f'{": " + str(len(it)) if it else ""}</li>' for l, it in audit)
checklist += f'<li class="{"ko" if open_disc else "ok"}"><b>{"✗" if open_disc else "✓"}</b> Discrepancias ledger↔fuente abiertas{": " + str(open_disc) if open_disc else ""}</li>'
checklist += f'<li class="{"ko" if sem_orph else "ok"}"><b>{"✗" if sem_orph else "✓"}</b> Entidades semánticas sin relaciones{": " + str(sem_orph) if sem_orph else ""}</li>'

mad = [cell(f"{pct(hres,htot)}%", "FALSABILIDAD EJERCIDA", f"{hres}/{htot} hipótesis movidas", False),
       cell(f"{pct(hy.get('refutada',0),hres)}%", "AUTOCORRECCIÓN", f"{hy.get('refutada',0)} refutadas de {hres} resueltas", hy.get("refutada", 0) == 0),
       cell(f"{pct(des['rules_cited'],des['rules'])}%", "REGLAS TRAZABLES", f"{des['rules_cited']}/{des['rules']} con F-n", des["rules_cited"] < des["rules"] / 2),
       cell(f"{pct(rig['A']+rig['B'],len(ledger))}%", "BASE SÓLIDA A+B", f"{rig['A']+rig['B']} de {len(ledger)} fuentes", False),
       cell(f"{pct(lec['abstract']+lec['completa'],len(tri))}%", "RELACIONES LEÍDAS", f"{lec['abstract']+lec['completa']}/{len(tri)} más allá de la ficha", lec["ficha"] > len(tri) / 2),
       cell(f"{pct(lobo['fuentes_leidas'],len(ledger))}%", "LECTURA PROFUNDA (LOBO)", f"{lobo['fuentes_leidas']} fuentes · {lobo['intuiciones']} intuiciones", False)]
sc = des["scale"]
mad_charts = ("<h3>ESCALA DE MADUREZ DE EVIDENCIA (§5 del node de diseño)</h3>" +
              stack([("documentado", sc.get("🟢", 0), "g1"), ("plausible", sc.get("🟡", 0), "g2"), ("hype/contradicho", sc.get("🔴", 0), "acc"), ("conflicto", sc.get("⚔️", 0), "g3")]) +
              "<h3>HIPÓTESIS (§6)</h3>" +
              stack([("abierta", hy.get("abierta", 0), "g3"), ("parcial", hy.get("parcial", 0), "g2"), ("respaldada", hy.get("respaldada", 0), "g1"), ("refutada", hy.get("refutada", 0), "acc")]) +
              "<h3>NIVEL DE LECTURA DE LAS RELACIONES</h3>" +
              stack([("ficha", lec["ficha"], "g3"), ("abstract", lec["abstract"], "g2"), ("completa", lec["completa"], "g1")]))

ri = [cell(len(ledger), "FUENTES EN EL LEDGER", f"{len(cit_all)} citadas por algún node", False),
      cell(len(nodes), "NODES", f"{sum(t.count(chr(10))+1 for t in nodes.values()):,} líneas · {len(outs)} outputs", False),
      cell(len(M["links"]), "ENLACES NODE→NODE", f"{len(M['comps'])} componente(s)", False),
      cell(len(dcit), "FUENTES EN EL NODE DE DISEÑO", f"{pct(M['ab'](dcit),len(dcit))}% A/B", False),
      cell(f"{len(sem_f)}", "FUENTES CON RELACIONES", f"{pct(len(sem_f),len(ledger))}% del ledger (grafo semántico)", len(sem_f) < len(ledger) / 10),
      cell(len(ent), "ENTIDADES", f"{len(tri)} relaciones", False),
      cell(conv, "CONVERGENCIAS", "entidades sostenidas por ≥2 fuentes", False),
      cell(tens, "TENSIONES DECLARADAS", f"{tens_open} sin resolver · {tens_real} de alcance distinto · {tens-tens_open-tens_real} reconciliadas/inferencia", tens_open > 0)]
rig_chart = "<h3>FUENTES POR RIGOR</h3>" + bars([(f"{k} {n}", rig[k], None, f"{rig[k]} ({pct(rig[k],len(ledger))}%)") for k, n in zip("ABCDE", ["verde", "azul", "amarillo", "naranja", "rojo"])], accent={"E rojo"}) if False else \
    "<h3>FUENTES POR RIGOR (A = máximo)</h3>" + bars([(f"{k}", rig[k], None, f"{rig[k]}  {pct(rig[k],len(ledger))}%") for k in "ABCDE"], label_w=30)
rel_cnt = Counter(t["p"] for t in tri)
rel_chart = "<h3>RELACIONES POR TIPO</h3>" + (bars([(p, n, None, str(n)) for p, n in rel_cnt.most_common()], label_w=100) if rel_cnt else "<p>—</p>")

ev_ledger = "<h3>LEDGER: FUENTES NUEVAS POR FECHA DE REGISTRO</h3>" + cols([(r["fecha"], r["nuevas"]) for r in tl])
bar_sem = ""
if est["barridos"]:
    bar_sem = "<h3>BARRIDOS SEMÁNTICOS</h3><table>" + "".join(
        f'<tr><td>{b["fecha"]}</td><td>{len(b["f_ids"])} fuentes</td><td>{b["triples"]} relaciones</td><td>{E(", ".join(b["f_ids"]))}</td></tr>' for b in est["barridos"]) + "</table>"
notes = "<p class='n'>Serie git: clon superficial; antes de la primera fecha visible solo vale la columna <code>fecha</code> del ledger (fecha de registro, no de lectura).</p>"

top = sorted(nodes, key=lambda n: -len(M["cites"][n] & set(ledger)))
node_rows = "".join(
    f'<tr><td>{"■ " if n == bg.DESIGN else ""}{E(n)}</td><td class="r">{nodes[n].count(chr(10))+1}</td><td class="r">{len(M["cites"][n] & set(ledger))}</td>'
    f'<td class="r">{pct(M["ab"](M["cites"][n] & set(ledger)), len(M["cites"][n] & set(ledger)))}%</td>'
    f'<td class="r">{sum(1 for a,b in M["links"] if b==n)}/{sum(1 for a,b in M["links"] if a==n)}</td>'
    f'<td><svg viewBox="0 0 100 10"><rect width="{min(100, 100*len(M["cites"][n] & set(ledger))/max(1,len(M["cites"][top[0]] & set(ledger))))}" height="10" class="fg"/></svg></td></tr>'
    for n in top)

# ---------- 06 temas: qué sabe cada node (subgrafo semántico) ----------
import math
ENT_N = lambda e: ent.get(e, {}).get("nombre", e)


def node_fs(n):  # F-n citadas por el node + por los outputs que derivan de él
    fs = {f"F-{i}" for i in M["cites"][n] & set(ledger)}
    for o, src in M["derive"]:
        if src == n and isinstance(outs.get(o), str):
            fs |= set(re.findall(r"F-\d+", outs[o]))
    return fs


def mapa(ts, w=900, h=420, k=13):
    """Mapa radial sin JS: centro = entidad de mayor grado; aristas entre las k entidades más conectadas."""
    deg = Counter()
    for t in ts:
        deg[t["s"]] += 1; deg[t["o"]] += 1
    top = [e for e, _ in deg.most_common(k)]
    if len(top) < 3:
        return "<p class='n'>Subgrafo demasiado pequeño para dibujar.</p>"
    cx, cy = w / 2, h / 2
    rx, ry = w / 2 - 225, h / 2 - 40  # deja ~210 px por lado para las etiquetas
    pos = {top[0]: (cx, cy)}
    for i, e in enumerate(top[1:]):
        a = 2 * math.pi * i / (len(top) - 1) - math.pi / 2
        pos[e] = (cx + rx * math.cos(a), cy + ry * math.sin(a))
    srcs = defaultdict(set)
    for t in ts:
        srcs[t["s"]].add(t["f"]); srcs[t["o"]].add(t["f"])
    pairs = defaultdict(lambda: [0, False])
    for t in ts:
        if t["s"] in pos and t["o"] in pos and t["s"] != t["o"]:
            p = pairs[tuple(sorted((t["s"], t["o"])))]
            p[0] += 1; p[1] = p[1] or t["p"] in ("contradice", "refuta")
    o = [f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="mapa del subgrafo">']
    for (a, b), (n, tension) in pairs.items():
        (x1, y1), (x2, y2) = pos[a], pos[b]
        dash = ";stroke-dasharray:6 4" if tension else ""
        col = "--acc" if tension else "--fg"
        o.append(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" '
                 f'style="stroke:var({col});stroke-width:{min(5, 1 + n)}{dash}"/>')
    for e, (x, y) in pos.items():
        rad = 5 + 2.2 * min(8, len(srcs[e]))
        o.append(f'<rect x="{x-rad:.0f}" y="{y-rad:.0f}" width="{2*rad:.0f}" height="{2*rad:.0f}" class="{"acc" if e == top[0] else "fg"}"/>')
        anchor = "middle" if abs(x - cx) < 20 else ("start" if x > cx else "end")
        dx = 0 if anchor == "middle" else (rad + 4 if anchor == "start" else -rad - 4)
        dy = rad + 12 if anchor == "middle" and y >= cy else (-rad - 4 if anchor == "middle" else 4)
        lab = ENT_N(e)
        lab = lab if len(lab) <= 30 else lab[:29] + "…"
        o.append(f'<text x="{x+dx:.0f}" y="{y+dy:.0f}" text-anchor="{anchor}" class="t{" b" if e == top[0] else ""}">{E(lab)}</text>')
    o.append("</svg>")
    return "".join(o)


tema_rows, tema_cards = "", ""
_last = max((d for d, _ in alma.values() if d), default="")
recent = {n for n, (d, _) in alma.items() if d and d == _last}
temas = []
for n in nodes:
    fs = node_fs(n)
    ts = [t for t in tri if t["f"] in fs]
    es = {x for t in ts for x in (t["s"], t["o"])}
    sb = defaultdict(set)
    for t in ts:
        sb[t["s"]].add(t["f"]); sb[t["o"]].add(t["f"])
    temas.append((n, fs, ts, es, sb))
temas.sort(key=lambda x: (x[0] not in recent, -len(x[2])))
for n, fs, ts, es, sb in temas:
    cov = len(fs & sem_f)
    tn = [t for t in ts if t["p"] in ("contradice", "refuta")]
    tema_rows += (f'<tr><td>{"● " if n in recent else ""}{E(n)}</td><td class="r">{len(fs)}</td><td class="r">{cov} ({pct(cov, len(fs))}%)</td>'
                  f'<td class="r">{len(ts)}</td><td class="r">{len(es)}</td><td class="r">{sum(1 for s in sb.values() if len(s) >= 2)}</td>'
                  f'<td class="r">{len(tn)}</td><td><svg viewBox="0 0 100 10"><rect width="{pct(cov, len(fs))}" height="10" class="fg"/></svg></td></tr>')
    if len(ts) >= 10:
        convs = sorted(((e, s) for e, s in sb.items() if len(s) >= 2), key=lambda x: -len(x[1]))[:6]
        conv_html = "".join(f"<li><b>{len(s)}</b> {E(ENT_N(e))} <span class='sub'>({E(', '.join(sorted(s, key=lambda f: int(f[2:]))[:6]))}{'…' if len(s) > 6 else ''})</span></li>" for e, s in convs) or "<li>—</li>"
        tens_html = "".join(f"<li class='ko'>{E(ENT_N(t['s']))} ⟷ {E(ENT_N(t['o']))} <span class='sub'>({t['f']})</span></li>" for t in tn[:4]) or "<li class='ok'>sin tensiones declaradas</li>"
        lec_n = Counter(t["lectura"] for t in ts)
        tema_cards += (f'<div class="tema"><h3>{"● ÚLTIMO INGRESO · " if n in recent else ""}{E(n)} — {len(ts)} relaciones · {len(es)} entidades · '
                       f'lectura: {lec_n["ficha"]} ficha / {lec_n["abstract"] + lec_n["completa"]} abstract+</h3>{mapa(ts)}'
                       f'<div class="body" style="padding:0"><div><h3>CONVERGENCIAS (≥2 FUENTES)</h3><ul>{conv_html}</ul></div>'
                       f'<div><h3>TENSIONES</h3><ul>{tens_html}</ul></div></div></div>')
temas_html = (f'<div class="body" style="grid-template-columns:1fr"><table><tr><th>node (● = última actualización en alma.md)</th><th>F-n</th><th>con relaciones</th>'
              f'<th>relaciones</th><th>entidades</th><th>converg.</th><th>tensiones</th><th></th></tr>{tema_rows}</table>'
              f'<p class="n">Subgrafo de un node = relaciones del grafo semántico cuya fuente cita el node o un output derivado de él. '
              f'Mapa: centro naranja = entidad más conectada; tamaño = n.º de fuentes; línea gruesa = varias relaciones; naranja punteada = tensión. '
              f'Se dibujan solo nodes con ≥10 relaciones. Una relación es lo que una fuente dice, no un hecho.</p></div>'
              f'<div class="body" style="grid-template-columns:1fr">{tema_cards}</div>')

# pendientes (accionables, derivados de lo medido)
todo = []
for a, b in M["nonrecip"][:6]:
    todo.append(f"Enlace no recíproco: {a} → {b} (falta la vuelta en {b})")
for o in [o for o in outs if o not in {a for a, _ in M["derive"]}]:
    todo.append(f"Output sin node-fuente: {o}")
for d in est["discrepancias"][:6]:
    todo.append(f"{d['f']}: {d['detalle'][:130]}…")
if lec["ficha"]:
    todo.append(f"{lec['ficha']} relaciones solo a nivel ficha → <code>relaciones.py next --mejorar</code>")
nxt = len(ledger) - len(sem_f)
todo.append(f"{nxt} fuentes sin procesar en el grafo semántico → <code>relaciones.py next -n 8</code>")
todo_html = "".join(f"<li>{t if '<code>' in t else E(t)}</li>" for t in todo)

CSS = """
:root{--bg:#fff;--fg:#000;--acc:#ff3b00;--g1:#000;--g2:#666;--g3:#bbb}
@media(prefers-color-scheme:dark){:root{--bg:#000;--fg:#fff;--acc:#ff5a26;--g1:#fff;--g2:#999;--g3:#444}}
*{box-sizing:border-box;border-radius:0}
body{margin:0;background:var(--bg);color:var(--fg);font:14px/1.35 ui-monospace,Menlo,Consolas,monospace}
header{border-bottom:8px solid var(--fg);padding:12px 16px;display:flex;flex-wrap:wrap;align-items:baseline;gap:8px 24px}
h1{font:900 clamp(56px,14vw,128px)/.85 Impact,'Arial Black',sans-serif;margin:0;letter-spacing:-.04em}
header p{margin:0;font-size:12px;text-transform:uppercase}
section{border-bottom:8px solid var(--fg);padding:0}
h2{margin:0;padding:6px 16px;background:var(--fg);color:var(--bg);font:900 20px Impact,'Arial Black',sans-serif;letter-spacing:.04em}
h3{margin:14px 0 4px;font-size:12px;text-transform:uppercase;border-bottom:2px solid var(--fg)}
.g{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr))}
.c{border:2px solid var(--fg);margin:-1px 0 0 -1px;padding:10px 12px}
.c.w{background:var(--acc);color:#000}.c.w .lab,.c.w .sub{color:#000}
.big{font:900 44px/1 Impact,'Arial Black',sans-serif}
.lab{font-weight:700;font-size:12px;text-transform:uppercase;margin-top:4px}.sub{font-size:11px;color:var(--g2)}
.body{padding:8px 16px 16px;display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:0 28px}
svg{width:100%;height:auto;display:block}
.fg,.g1{fill:var(--g1)}.g2{fill:var(--g2)}.g3{fill:var(--g3)}.acc{fill:var(--acc)}
.t{font:11px ui-monospace,monospace;fill:var(--fg)}.t.b{font-weight:700}.t.s{font-size:10px}.inv{fill:var(--bg)}
table{width:100%;border-collapse:collapse;font-size:12px}td,th{border:2px solid var(--fg);padding:3px 6px;text-align:left}td.r{text-align:right}
th{background:var(--fg);color:var(--bg);text-transform:uppercase;font-size:11px}
ul{margin:6px 0;padding:0;list-style:none}li{border-left:8px solid var(--g3);padding:2px 8px;margin:3px 0;font-size:12px}
li.ko{border-color:var(--acc)}li.ok{border-color:var(--fg)}li b{display:inline-block;width:1.2em}
p.n,footer{font-size:11px;color:var(--g2);padding:8px 16px}footer{border-top:2px solid var(--fg)}
tr.ko td{background:transparent}tr.ko td:nth-child(5){color:var(--acc);font-weight:900}
.nv{border:4px solid var(--fg);padding:10px 14px}.big2{font:900 110px/0.9 Impact,'Arial Black',sans-serif}.big2 span{font-size:36px;color:var(--g2)}
.lab2{font:900 26px Impact,'Arial Black',sans-serif;letter-spacing:.04em;background:var(--acc);color:#000;display:inline-block;padding:0 8px;margin-top:6px}
.hero{grid-template-columns:300px minmax(0,1fr)!important;align-items:start}@media(max-width:720px){.hero{grid-template-columns:minmax(0,1fr)!important}.big2{font-size:84px}}
code{background:var(--g3);padding:0 3px}
.tema{border:4px solid var(--fg);margin:8px 0;padding:0 10px 10px}.tema svg{max-width:900px;margin:0 auto}
"""
HTML = f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>MU — panel del segundo cerebro</title><style>{CSS}</style></head><body>
<header><h1>MU</h1><p>segundo cerebro · {today}<br>rama {E(branch)} @ {E(commit)}<br>{len(ledger)} fuentes / {len(nodes)} nodes / {len(tri)} relaciones</p></header>
<section><h2>00 INTELIGENCIA — ¿qué nivel tiene?</h2><div class="body hero"><div class="nv"><div class="big2">N{nivel}<span>/{len(NIV)}</span></div><div class="lab2">{nombre_nivel}</div><div class="sub">{E(NIV[nivel-1]["def"] if nivel else "Sin criterios cumplidos")}</div></div><div>{escalera()}<div style="margin-top:10px"><h3>PARA SUBIR A N{nivel+1 if sig else nivel}{(" — " + sig["nombre"]) if sig else ""}</h3>{falta}<p class="n">Escalera: se sube solo con TODOS los criterios del nivel. Umbrales propuestos (juicio del autor), editables en niveles.json. N7 exige medir uso externo, hoy sin instrumento: no es alcanzable aún.</p></div></div></div><div class="body" style="grid-template-columns:1fr"><table><tr><th>nivel</th><th>estado</th><th>criterio</th><th>valor / umbral</th><th></th><th></th></tr>{crit_rows}</table></div></section>
<section><h2>01 SALUD — ¿está sano?</h2><div class="g">{''.join(sal)}</div><div class="body"><div><h3>CHEQUEOS</h3><ul>{checklist}</ul></div><div><h3>PENDIENTES ACCIONABLES</h3><ul>{todo_html}</ul></div></div></section>
<section><h2>02 MADUREZ — ¿qué tan probado está?</h2><div class="g">{''.join(mad)}</div><div class="body"><div>{mad_charts}</div></div></section>
<section><h2>03 RIQUEZA — ¿cuánto hay?</h2><div class="g">{''.join(ri)}</div><div class="body"><div>{rig_chart}</div><div>{rel_chart}</div></div></section>
<section><h2>04 EVOLUCIÓN — ¿cómo creció?</h2><div class="body" style="grid-template-columns:1fr">{ev_ledger}{bar_sem}{notes}</div></section>
<section><h2>05 NODES — ¿dónde está el peso?</h2><div class="body" style="grid-template-columns:1fr"><table><tr><th>node</th><th>líneas</th><th>F-n</th><th>A/B</th><th>ent/sal</th><th></th></tr>{node_rows}</table></div></section>
<section><h2>06 TEMAS — ¿qué sabe de cada tema?</h2>{temas_html}</section>
<footer>Todo número sale de contar archivos (METRICAS.md). Citar ≠ validar. Impacto externo (uso por personas): NO medido. Regenerar: python research/grafo/mu.py</footer>
</body></html>"""
(H / "mu.html").write_text(HTML)

print(f"INTELIGENCIA N{nivel}/{len(NIV)} {nombre_nivel}" + (f" → siguiente {sig['nombre']} ({round(sig['prog']*100)}%)" if sig else ""))
print(f"MU {today} | SALUD {checks_ok}/{n_checks} chequeos · {len(M['nonrecip'])} enlaces no recíprocos · {open_disc} discrepancias · {len(orphans)} huérfanos")
print(f"MADUREZ falsabilidad {pct(hres,htot)}% · autocorrección {pct(hy.get('refutada',0),hres)}% · reglas trazables {pct(des['rules_cited'],des['rules'])}% · A+B {pct(rig['A']+rig['B'],len(ledger))}% · relaciones leídas más allá de ficha {pct(lec['abstract']+lec['completa'],len(tri))}%")
print(f"RIQUEZA {len(ledger)} fuentes · {len(nodes)} nodes · {len(ent)} entidades · {len(tri)} relaciones · {conv} convergencias · {tens} tensiones · semántica {len(sem_f)}/{len(ledger)} ({pct(len(sem_f),len(ledger))}%)")
print("ALERTAS " + (" | ".join(re.sub(r'[*`]', '', l)[:60] + f" ({len(it)})" for l, it in fails) or "ninguna") + (f" | discrepancias ({open_disc})" if open_disc else ""))
print(f"panel: {H/'mu.html'}")
