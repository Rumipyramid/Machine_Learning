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
rig = Counter(r["rigor"] for r in ledger.values())
hy = des["hyp"]; htot = sum(hy.values()); hres = htot - hy.get("abierta", 0)
cit_all = M["allc"] & set(ledger)
dcit = M["dcit"] & set(ledger)
orphans = sorted(M["in_range"] - M["dcit"])
fails = [(lbl, it) for lbl, it in audit if it]
n_checks = len(audit) + 2  # + discrepancias abiertas + entidades sin relaciones
sem_orph = len(set(ent) - {x for t in tri for x in (t["s"], t["o"])})
open_disc = len(est["discrepancias"])
checks_ok = len(audit) - len(fails) + (1 if open_disc == 0 else 0) + (1 if sem_orph == 0 else 0)
commit = sh("git", "rev-parse", "--short", "HEAD") if not SIN_GIT else "n/d"
branch = sh("git", "branch", "--show-current") if not SIN_GIT else "n/d"
today = dt.date.today().isoformat()


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
      cell(tens, "TENSIONES DECLARADAS", "contradice / refuta", False)]
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
code{background:var(--g3);padding:0 3px}
"""
HTML = f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>MU — panel del segundo cerebro</title><style>{CSS}</style></head><body>
<header><h1>MU</h1><p>segundo cerebro · {today}<br>rama {E(branch)} @ {E(commit)}<br>{len(ledger)} fuentes / {len(nodes)} nodes / {len(tri)} relaciones</p></header>
<section><h2>01 SALUD — ¿está sano?</h2><div class="g">{''.join(sal)}</div><div class="body"><div><h3>CHEQUEOS</h3><ul>{checklist}</ul></div><div><h3>PENDIENTES ACCIONABLES</h3><ul>{todo_html}</ul></div></div></section>
<section><h2>02 MADUREZ — ¿qué tan probado está?</h2><div class="g">{''.join(mad)}</div><div class="body"><div>{mad_charts}</div></div></section>
<section><h2>03 RIQUEZA — ¿cuánto hay?</h2><div class="g">{''.join(ri)}</div><div class="body"><div>{rig_chart}</div><div>{rel_chart}</div></div></section>
<section><h2>04 EVOLUCIÓN — ¿cómo creció?</h2><div class="body" style="grid-template-columns:1fr">{ev_ledger}{bar_sem}{notes}</div></section>
<section><h2>05 NODES — ¿dónde está el peso?</h2><div class="body" style="grid-template-columns:1fr"><table><tr><th>node</th><th>líneas</th><th>F-n</th><th>A/B</th><th>ent/sal</th><th></th></tr>{node_rows}</table></div></section>
<footer>Todo número sale de contar archivos (METRICAS.md). Citar ≠ validar. Impacto externo (uso por personas): NO medido. Regenerar: python research/grafo/mu.py</footer>
</body></html>"""
(H / "mu.html").write_text(HTML)

print(f"MU {today} | SALUD {checks_ok}/{n_checks} chequeos · {len(M['nonrecip'])} enlaces no recíprocos · {open_disc} discrepancias · {len(orphans)} huérfanos")
print(f"MADUREZ falsabilidad {pct(hres,htot)}% · autocorrección {pct(hy.get('refutada',0),hres)}% · reglas trazables {pct(des['rules_cited'],des['rules'])}% · A+B {pct(rig['A']+rig['B'],len(ledger))}% · relaciones leídas más allá de ficha {pct(lec['abstract']+lec['completa'],len(tri))}%")
print(f"RIQUEZA {len(ledger)} fuentes · {len(nodes)} nodes · {len(ent)} entidades · {len(tri)} relaciones · {conv} convergencias · {tens} tensiones · semántica {len(sem_f)}/{len(ledger)} ({pct(len(sem_f),len(ledger))}%)")
print("ALERTAS " + (" | ".join(re.sub(r'[*`]', '', l)[:60] + f" ({len(it)})" for l, it in fails) or "ninguna") + (f" | discrepancias ({open_disc})" if open_disc else ""))
print(f"panel: {H/'mu.html'}")
