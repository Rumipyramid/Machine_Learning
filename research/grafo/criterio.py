#!/usr/bin/env python3
"""La balanza del Criterio: cuánto respaldo tiene una respuesta de Mu para la pregunta que se le hizo (solo stdlib).

Herramienta determinista del **Criterio de Mu** (`.claude/skills/criterio/`). No redacta ni opina: pesa.
Dada la pregunta y la primera respuesta, calcula con reglas fijas:

  1. QUÉ CITÓ    fuentes citadas que existen, códigos inventados, rigor y profundidad de lectura de lo citado
  2. QUÉ ESTIRÓ  frases con cifras o palabras absolutas sin ninguna fuente al lado
  3. QUÉ HAY     lo que el cerebro tiene sobre la pregunta: fuentes, hipótesis, desacuerdos abiertos, lecciones
                 (heurísticas) de El Lobo y temas del backlog de Mu sin buena respuesta
  4. RELEVANCIA  si cada fuente citada estudia lo mismo que se pregunta: directa · cercana · lejana (regla en relevancia())
  5. EL NIVEL    firme · parcial · solo heurística · sin base (regla en NIVELES, más abajo)
  6. EL CAMINO   pasos concretos para poder responder bien la pregunta

El nivel es un techo: quien redacte el criterio puede bajarlo, nunca subirlo.

Uso:  python research/grafo/criterio.py --pregunta "…" --respuesta archivo.md [--json]
      (con --respuesta - lee la respuesta desde la entrada estándar)
"""
import argparse, datetime as dt, json, math, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "preguntar"))
import build_corpus as bc  # noqa: E402
import papisa  # noqa: E402  (mismo filtro por palabras clave: raices + puntaje)

NIVELES = {
    "firme": "Firme: la respuesta se apoya en 3 o más fuentes del registro, al menos la mitad de rigor A o B y al menos 2 directamente relevantes para la pregunta, sin códigos inventados, sin desacuerdos abiertos sobre lo citado y con a lo más una afirmación fuerte sin fuente.",
    "parcial": "Parcial: hay respaldo, pero incompleto (pocas fuentes, fuentes débiles, desacuerdos abiertos o la respuesta no usó lo que el cerebro tiene).",
    "heuristica": "Solo heurística: el cerebro no tiene fuentes sobre esto; solo lecciones de criterio del equipo. Se puede ofrecer como intuición declarada, nunca como respuesta.",
    "sin_base": "Sin base: el cerebro no tiene fuentes, lecciones ni hipótesis sobre esto. Lo honesto es decir que no hay respuesta.",
}
ABSOLUTAS = r"\b(siempre|nunca|todos|todas|ninguno|ninguna|demuestra|demostrado|probado|comprobado|garantiza|sin duda|causa|provoca|elimina|definitivamente)\b"
# palabras que no identifican un tema: no bastan para que una lección del equipo "toque" la pregunta
GENERICAS = {w[:6] for w in "mejor mejores peor peores bueno buena buenos buenas malo mala mayor menor forma formas manera maneras hacer hago puede pueden podemos debe deben debo deberia quiero saber cosa cosas algo cual cuales funciona funcionan sirve sirven conviene vale".split()}
# Relevancia: contextos que, si la pregunta los nombra, la fuente también debe tratar (pregunta, fuente, herramienta)
CONTEXTOS = [
    ("Perú", r"per[uú]|peruan|\blima\b|lime[ñn]|latinoam|latam", r"per[uú]|peruan|\blima\b|latinoam|latam|am[eé]rica latina|\bsbs\b|apeseg|\binei\b|bcrp|enaho", "/contexto-peruano"),
    ("seguros", r"segur[oa]s?\b|asegur|p[oó]liza|siniestr|insur", r"segur[oa]s?\b|asegur|p[oó]liza|insur|siniestr|actuar", "/seeker o /marketer"),
    ("salud", r"salud|m[eé]dic|cl[ií]nic|farmac|hospital|paciente", r"salud|m[eé]dic|cl[ií]nic|farmac|hospital|paciente|health", "/seeker"),
    ("inteligencia artificial", r"\bia\b|inteligencia artificial|\bllms?\b|chatbot|\bai\b|modelos? de lenguaje", r"\bia\b|inteligencia artificial|\bllms?\b|chatbot|\bai\b|language model|algoritm|machine learning|agente", "/seeker"),
    ("diseño", r"dise[ñn]o|\bux\b|interfaz|experiencia de usuario", r"dise[ñn]|design|\bux\b|interfa|usabil", "/seeker"),
]
PRESENTE = r"\bhoy\b|actual|reciente|[uú]ltim[oa]s?\b|tendencia|20[2-9]\d"
PISTAS = [  # (palabras de la pregunta, herramienta del equipo, para qué)
    (r"mercado|empresa|startup|ingreso|venta|precio|inversi|rentab|ronda|competidor|negocio", "/marketer", "resultados de negocio publicados y verificables"),
    (r"redes|opina|percep|viral|tiktok|reputaci|qué se dice|rumor", "/gossip", "qué se dice en redes y prensa, medido por cobertura"),
    (r"per[uú]|peruan|inei|sbs|bcrp|apeseg|lima|lime[ñn]|cu[aá]nt[oa]s|porcentaje|cifra", "/contexto-peruano", "el dato oficial peruano (INEI, SBS, BCRP)"),
]


def oraciones(texto):
    partes = re.split(r"(?<=[.!?])\s+|\n+", texto)
    return [p.strip(" -•*") for p in partes if len(p.strip(" -•*")) > 25]


def relevancia(f, pregunta, claves5, anio):
    """Qué tan directamente una fuente estudia lo que se pregunta. Es un techo: quien redacta puede bajarlo, nunca subirlo.
    directa: comparte el tema (al menos la mitad de las palabras clave, mínimo 2) y todos los contextos que nombra la pregunta,
             con datos vigentes si la pregunta es sobre el presente.
    cercana: comparte parte del tema, pero le falta un contexto o los datos tienen más de 5 años.
    lejana : no comparte el tema; solo coincide en palabras sueltas o en nada."""
    texto = f"{f['titulo']} {f['resumen']}"
    r = {w[:5] for w in papisa.raices(texto)}
    hall = len(claves5 & r)
    tema = bool(claves5) and hall >= min(2, len(claves5)) and hall >= len(claves5) / 2
    falta = [c for c, pq, pf, _ in CONTEXTOS if re.search(pq, pregunta, re.I) and not re.search(pf, texto, re.I)]
    antigua = bool(re.search(PRESENTE, pregunta, re.I)) and f.get("y") and f["y"] < anio - 5
    motivo = []
    if falta:
        motivo.append("no trata " + " ni ".join(falta))
    if antigua:
        motivo.append(f"sus datos son de {f['y']}")
    if tema and not motivo:
        return "directa", ""
    if tema or hall:
        return "cercana", "; ".join(motivo) or "trata solo parte del tema"
    return "lejana", "no estudia lo que se pregunta"


def balanza(pregunta, respuesta):
    fuentes = {f["id"]: f for f in bc.ledger_rows()}
    tens, _ = bc.grafo(list(fuentes.values()))
    citadas = list(dict.fromkeys(re.findall(r"\bF-\d{1,4}\b", respuesta)))
    validas = [c for c in citadas if c in fuentes]
    inventadas = [c for c in citadas if c not in fuentes]
    ab = [c for c in validas if fuentes[c]["rig"] in ("A", "B")]
    debiles = [c for c in validas if fuentes[c]["rig"] in ("D", "E")]
    a_medias = [c for c in validas if not fuentes[c]["deep"]]
    disp = [t for t in tens if t["abierta"] and t["f"] in set(validas)]
    claves5 = {w[:5] for w in papisa.raices(pregunta)} - {g[:5] for g in GENERICAS}
    anio = dt.date.today().year
    relev = {c: relevancia(fuentes[c], pregunta, claves5, anio) for c in validas}
    directas = [c for c in validas if relev[c][0] == "directa"]
    cercanas = [c for c in validas if relev[c][0] == "cercana"]
    lejanas = [c for c in validas if relev[c][0] == "lejana"]
    pertinentes = directas + cercanas
    if not validas:
        rel_global = "sin fuentes citadas"
    elif len(directas) >= 2 or (directas and len(directas) >= len(validas) / 2):
        rel_global = "alta"
    elif pertinentes:
        rel_global = "media"
    else:
        rel_global = "baja"

    sin_fuente = []
    for o in oraciones(respuesta):
        if o.lower().startswith("lo que mu no sabe"):
            continue
        if not re.search(r"F-\d", o) and (re.search(r"\d", o) or re.search(ABSOLUTAS, o, re.I)):
            sin_fuente.append(o[:220])

    L = papisa.libro(pregunta, validas, top=8)  # lo que el cerebro tiene sobre la pregunta (sin mirar la respuesta)
    claves = papisa.raices(pregunta)
    claves_tema = claves - GENERICAS
    intu = [i for i in bc.mago_mesa()["intuiciones"] if papisa.puntaje(claves_tema, i["titulo"], i["texto"]) > 0]
    rel = L["totales"]["relevantes"]

    if not pertinentes and rel == 0 and not intu:  # una fuente lejana no cuenta como base
        nivel = "sin_base"
    elif not pertinentes and rel == 0:
        nivel = "heuristica"
    elif (len(validas) >= 3 and len(ab) >= math.ceil(len(validas) / 2) and len(directas) >= 2
          and not disp and not inventadas and len(sin_fuente) <= 1):
        nivel = "firme"
    else:
        nivel = "parcial"

    camino = []
    if inventadas:
        camino.append(f"Corregir la respuesta: cita {', '.join(inventadas)}{', que no existe' if len(inventadas) == 1 else ', que no existen'} en el registro de fuentes.")
    if lejanas:
        camino.append(f"Retirar o reemplazar {', '.join(lejanas[:3])}: no estudia{'n' if len(lejanas) > 1 else ''} lo que se pregunta.")
    if validas and not directas:
        ctx = [c for c in CONTEXTOS if any(c[0] in relev[v][1] for v in pertinentes)]
        if ctx:
            camino.append(f"Buscar evidencia sobre {ctx[0][0]} con {ctx[0][3]}: las fuentes citadas estudian otro contexto.")
    viejas = [c for c in pertinentes if "sus datos son de" in relev[c][1]]
    if viejas:
        camino.append(f"Actualizar {', '.join(viejas[:3])}: sus datos tienen más de 5 años y la pregunta es sobre el presente.")
    if nivel in ("sin_base", "heuristica"):
        extra = [f"{h} ({para})" for pat, h, para in PISTAS if re.search(pat, pregunta, re.I)]
        camino.append(f"Investigar el tema como conocimiento nuevo con /trinidad (evidencia académica, social y de negocio a la vez)"
                      + (f"; o, si basta una arista, {' o '.join(extra)}" if extra else "; si solo hace falta la evidencia académica, /seeker") + ".")
        camino.append("Si la pregunta se repite sin respuesta, el protocolo de Mu la marcará sola para investigarla.")
    if L["libro"] and nivel != "sin_base":
        fs = [f"{f['id']} ({f['rigor']})" for f in L["libro"][:3]]
        camino.append(f"Usar lo que el cerebro ya tiene y la respuesta no citó: {', '.join(fs)}.")
    if sin_fuente:
        camino.append(f"Respaldar o retirar {len(sin_fuente)} afirmación(es) con cifras o palabras absolutas que no citan fuente.")
    if validas and len(debiles) > len(validas) / 2:
        camino.append(f"Buscar la fuente primaria detrás de {', '.join(debiles[:3])}: hoy son notas de prensa u opiniones.")
    if a_medias:
        camino.append(f"Leer a fondo {', '.join(a_medias[:3])}: solo se leyó su resumen o no pasó por el análisis de relaciones.")
    for t in disp[:1]:
        camino.append(f"Resolver el desacuerdo abierto de {t['f']} (\"{t['s']}\" {t['p']} \"{t['o']}\") antes de afirmar en esa dirección.")
    for h in L["vivo"][:1]:
        if h["prueba"]:
            camino.append(f"Correr la prueba pendiente de la idea {h['id']}: {h['prueba'][:160]}")

    return {"pregunta": pregunta, "nivel": nivel, "nivel_txt": NIVELES[nivel],
            "citadas": {"validas": validas, "inventadas": inventadas, "ab": ab, "debiles": debiles, "a_medias": a_medias},
            "relevancia": {"global": rel_global, "directas": directas, "cercanas": cercanas, "lejanas": lejanas,
                           "detalle": {c: {"grado": g, "motivo": m} for c, (g, m) in relev.items()}},
            "disputas": [{"f": t["f"], "s": t["s"], "p": t["p"], "o": t["o"], "estado": t["estado"]} for t in disp],
            "sin_fuente": sin_fuente[:6],
            "cerebro": {"fuentes_relevantes": rel, "fuentes_AB": L["totales"]["no_citadas_AB"], "no_citadas": L["libro"][:5],
                        "hipotesis": L["vivo"][:4], "lecciones": [{"n": i["n"], "titulo": i["titulo"], "texto": i["texto"][:300]} for i in intu[:4]],
                        "backlog": [b for b in L["velo"]["backlog"] if b["toca"]][:3]},
            "camino": camino[:5]}


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--pregunta", required=True)
    ap.add_argument("--respuesta", required=True, help="archivo con la primera respuesta, o - para leerla de stdin")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    resp = sys.stdin.read() if a.respuesta == "-" else Path(a.respuesta).read_text(encoding="utf-8")
    B = balanza(a.pregunta, resp)
    if a.json:
        print(json.dumps(B, ensure_ascii=False, indent=1)); return
    C, K = B["citadas"], B["cerebro"]
    print(f"# Balanza del Criterio — {a.pregunta}\n")
    print(f"**Nivel (techo): {B['nivel'].upper()}** — {B['nivel_txt']}\n")
    print(f"## 1. Qué citó la respuesta\n- válidas: {', '.join(C['validas']) or 'ninguna'} · A-B: {len(C['ab'])} · D-E: {len(C['debiles'])} · leídas solo en resumen: {len(C['a_medias'])}")
    if C["inventadas"]:
        print(f"- ⚠️ códigos que NO existen en el registro: {', '.join(C['inventadas'])}")
    RV = B["relevancia"]
    print(f"- relevancia para la pregunta: {RV['global'].upper()} (directas {len(RV['directas'])} · cercanas {len(RV['cercanas'])} · lejanas {len(RV['lejanas'])})")
    for c, d in RV["detalle"].items():
        print(f"  - {c}: {d['grado']}{' — ' + d['motivo'] if d['motivo'] else ''}")
    for d in B["disputas"]:
        print(f"- desacuerdo abierto sobre {d['f']}: \"{d['s']}\" {d['p']} \"{d['o']}\" ({d['estado']})")
    print(f"\n## 2. Qué estiró (frases con cifras o palabras absolutas sin fuente al lado): {len(B['sin_fuente'])}")
    for s in B["sin_fuente"]:
        print(f"- {s}")
    print(f"\n## 3. Qué tiene el cerebro sobre la pregunta\n- {K['fuentes_relevantes']} fuentes tocan el tema ({K['fuentes_AB']} de rigor A-B no citadas)")
    for f in K["no_citadas"]:
        print(f"  - {f['id']} ({f['rigor']}, {f['anio']}) {f['titulo'][:110]} · {f['lectura']}")
    for h in K["hipotesis"]:
        print(f"- idea en prueba {h['id']} [{h['estado']}]: {h['texto'][:150]}")
    for i in K["lecciones"]:
        print(f"- lección del equipo (heurística, no evidencia): {i['titulo']}")
    for b in K["backlog"]:
        print(f"- ya preguntado a Mu sin buena respuesta: {b['tema']} (✗ {b['sin']} · ~ {b['parcial']})")
    print("\n## 4. Camino para responder")
    for i, c in enumerate(B["camino"], 1):
        print(f"{i}. {c}")
    if not B["camino"]:
        print("- (nada urgente: la respuesta está bien apoyada)")


if __name__ == "__main__":
    main()
