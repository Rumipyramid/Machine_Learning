#!/usr/bin/env python3
"""
Proyecta el códice de evidencia a un grafo navegable en Obsidian.

No modifica `research/fuentes/codice.md`: lo lee. El códice sigue siendo la fuente
única de trazabilidad que mantiene el skill `cronista`; este script sólo genera una
proyección regenerable de él.

Qué produce
-----------
* `research/_grafo/fuentes/F-###.md` — una nota por fuente, con frontmatter
  (autor, año, rigor, eco de cita, huérfana) y enlaces a los nodes que fundamenta.
* Frontmatter en `research/_nodes/*.md` y `research/_outputs/*.md` — se inserta sólo
  si no existe; el cuerpo de esos archivos no se toca nunca.
* Tableros de consulta en `research/_grafo/` — con query de Dataview y, debajo, una
  tabla estática equivalente para quien no tenga el plugin instalado.
* Configuración de vault en `research/.obsidian/`.

Uso
---
    python3 research/_grafo/generar_grafo.py            # regenera todo
    python3 research/_grafo/generar_grafo.py --check    # sólo reporta, no escribe

Sólo stdlib, como el resto del tooling del proyecto.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path

RESEARCH = Path(__file__).resolve().parent.parent
CODICE = RESEARCH / "fuentes" / "codice.md"
NODES_DIR = RESEARCH / "_nodes"
OUTPUTS_DIR = RESEARCH / "_outputs"
GRAFO = RESEARCH / "_grafo"
FUENTES_OUT = GRAFO / "fuentes"
OBSIDIAN = RESEARCH / ".obsidian"

MARCA_A_GRADO = {"🟢": "A", "🔵": "B", "🟡": "C", "🟠": "D", "🔴": "E"}
GRADO_ORDEN = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "N/A": 5, "s/g": 6}

# Frases con las que el códice marca una fuente como no utilizable
# como afirmación fuerza.
RE_ECO = re.compile(
    r"eco de cita|huérfan[oa] de cita|autoridad prestada|cadena de cita"
    r"|no usar como afirmaci|NO debe usarse|no auditable",
    re.I,
)
RE_FILA = re.compile(r"^\|\s*F-\d+\s*\|")
RE_NODE_REF = re.compile(r"_nodes/([a-z0-9][a-z0-9\-]*)\.md")
RE_OUTPUT_REF = re.compile(r"_outputs/([a-z0-9][a-z0-9\-]*)\.md")
RE_FN = re.compile(r"\bF-(\d+)\b")
RE_HN = re.compile(r"\bH(\d{1,2})\b")
RE_CN = re.compile(r"\bC(\d{1,2})\b")

# Fila de la tabla de hipótesis:  | **H1** | enunciado | estado | prueba |
RE_HIP = re.compile(r"^\|\s*\*{0,2}(H\d{1,2})\*{0,2}\s*\|(.+)$")
# Viñeta de regla de criterio:    - **C1 — Título.** cuerpo…
RE_REGLA = re.compile(r"^\s*[-*]\s*\*\*(C\d{1,2})\s*[—–-]\s*(.+?)\*\*\s*(.*)$")
RE_ESTADO = re.compile(r"`(abierta|parcial|respaldada|refutada|degradada|contestada)`", re.I)

# Etiquetas de autoría que no son una entidad real y no merecen nota propia.
RE_AUTOR_GENERICO = re.compile(
    r"^(varios|varias|autor[ií]a no|autores no|desconocid|n/?d\b|s/?d\b"
    r"|no verificad|m[úu]ltiples|sin autor)", re.I)
# Un autor sólo se vuelve nodo del grafo si conecta al menos esta cantidad de
# fuentes; si no, sería una hoja suelta que ensucia el grafo sin aportar.
MIN_FUENTES_POR_AUTOR = 2


# --------------------------------------------------------------------------- #
# utilidades
# --------------------------------------------------------------------------- #
def yaml_str(value: str) -> str:
    """Cita un escalar YAML de forma segura."""
    return '"' + str(value).replace("\\", "\\\\").replace('"', '\\"') + '"'


def limpiar(celda: str) -> str:
    """Normaliza una celda de la tabla del códice a texto plano legible."""
    txt = celda.strip()
    txt = re.sub(r"<br\s*/?>", " ", txt)
    return re.sub(r"\s+", " ", txt).strip()


def normalizar_rigor(celda: str) -> tuple[str, str, str]:
    """(marca, grado, texto completo) a partir del campo de rigurosidad.

    Cubre los 17 casos que no siguen el patrón `emoji + letra` — «⚪ No aplica»,
    «🟡 Variable», «⚠️ No verificado», o los que abren con la crítica en vez del
    grado. Se toma la primera marca de color como grado principal.
    """
    texto = limpiar(celda)
    m = re.match(r"^(🟢|🔵|🟡|🟠|🔴)\s*([A-E](?:/[A-E])?)\b", texto)
    if m:
        return m.group(1), m.group(2).split("/")[0], texto
    if texto.startswith("⚪") or re.match(r"^⚪|No aplica", texto):
        return "⚪", "N/A", texto
    m = re.search(r"(🟢|🔵|🟡|🟠|🔴)", texto)
    if m:
        return m.group(1), MARCA_A_GRADO[m.group(1)], texto
    return "⚠️", "s/g", texto


def anio_numerico(texto: str) -> int | None:
    """Extrae un año comparable de campos como `2024-25` o `1984-2013` o `s.f.`."""
    anios = re.findall(r"\b(1[89]\d{2}|20\d{2})\b", texto)
    return int(anios[-1]) if anios else None


# --------------------------------------------------------------------------- #
# modelo
# --------------------------------------------------------------------------- #
@dataclass
class Fuente:
    id: str
    num: int
    autor: str
    anio_txt: str
    titulo: str
    rigor_texto: str
    marca: str
    grado: str
    resumen: str
    usado_en: str
    url: str
    registrado: str
    nodes: set[str] = field(default_factory=set)
    outputs: set[str] = field(default_factory=set)
    relacionadas: set[str] = field(default_factory=set)
    hipotesis: set[str] = field(default_factory=set)
    reglas: set[str] = field(default_factory=set)
    autor_slug: str = ""
    eco: bool = False

    @property
    def slug(self) -> str:
        return f"F-{self.num:03d}"

    @property
    def huerfana(self) -> bool:
        return not self.nodes and not self.outputs


def parsear_codice(texto: str) -> list[Fuente]:
    fuentes: list[Fuente] = []
    for linea in texto.split("\n"):
        if not RE_FILA.match(linea):
            continue
        celdas = [c.strip() for c in linea.strip().strip("|").split("|")]
        if len(celdas) != 9:
            print(f"  ⚠️  fila ignorada ({len(celdas)} celdas): {celdas[0]}")
            continue
        fid, autor, anio, titulo, rigor, resumen, usado, url, reg = celdas
        marca, grado, rigor_txt = normalizar_rigor(rigor)
        num = int(re.search(r"\d+", fid).group())
        f = Fuente(
            id=f"F-{num}",
            num=num,
            autor=limpiar(autor),
            anio_txt=limpiar(anio),
            titulo=limpiar(titulo),
            rigor_texto=rigor_txt,
            marca=marca,
            grado=grado,
            resumen=limpiar(resumen),
            usado_en=limpiar(usado),
            url=limpiar(url),
            registrado=limpiar(reg),
        )
        # Los nodes/outputs que la propia fila declara sustentar.
        f.nodes |= set(RE_NODE_REF.findall(usado))
        f.outputs |= set(RE_OUTPUT_REF.findall(usado))
        # Otras fuentes citadas dentro de la fila (complementa, choca con, deriva de).
        f.relacionadas |= {
            f"F-{n}" for n in RE_FN.findall(usado + " " + resumen)
        } - {f.id}
        # Hipótesis y reglas que la fila cita explícitamente. Se restringe al
        # campo «Usado en», que es donde el códice las referencia; buscarlas en
        # el resumen daría falsos positivos (C1 de una norma, H2 de una fórmula).
        f.hipotesis |= {f"H{n}" for n in RE_HN.findall(usado)}
        f.reglas |= {f"C{n}" for n in RE_CN.findall(usado)}
        f.eco = bool(RE_ECO.search(rigor + " " + resumen))
        fuentes.append(f)
    return fuentes


def titulo_de(path: Path) -> str:
    """Primer encabezado H1 del archivo; si no hay, el nombre del archivo."""
    for linea in path.read_text(encoding="utf8").split("\n")[:40]:
        if linea.startswith("# "):
            return linea[2:].strip()
    return path.stem


def meta_de_node(path: Path) -> dict[str, str]:
    """Versión y fecha del bloque de cita que abre cada node.

    Tolera el énfasis Markdown (`Versión: **v4.0 (iteración 4)**`) y prefiere
    «Última actualización» sobre «Fecha de elaboración» cuando el node trae ambas.
    """
    texto = path.read_text(encoding="utf8")
    if texto.startswith("---\n"):  # saltar frontmatter previo
        texto = texto.split("\n---\n", 1)[-1]
    cabeza = "\n".join(texto.split("\n")[:16])
    meta: dict[str, str] = {}

    m = re.search(r"Versi[óo]n:\s*\**\s*(v[\d.]+)", cabeza)
    if m:
        meta["version"] = m.group(1)

    m = re.search(r"(?:[ÚU]ltima actualizaci[óo]n|[Aa]ctualizad[oa])[^:\n]*:\s*\**\s*"
                  r"(\d{4}-\d{2}-\d{2})", cabeza)
    if not m:
        m = re.search(r"Fecha[^:\n]*:\s*\**\s*(\d{4}-\d{2}-\d{2})", cabeza)
    if m:
        meta["actualizado"] = m.group(1)
    return meta


# --------------------------------------------------------------------------- #
# entidades: hipótesis, reglas de criterio, autores
# --------------------------------------------------------------------------- #
@dataclass
class Entidad:
    id: str
    titulo: str
    cuerpo: str
    origen: str          # node donde vive
    estado: str = ""

    @property
    def slug(self) -> str:
        m = re.match(r"([A-Z])(\d+)", self.id)
        return f"{m.group(1)}{int(m.group(2)):02d}" if m else self.id


def sin_markdown(texto: str) -> str:
    """Quita énfasis y enlaces para usar el texto como título de nota."""
    txt = re.sub(r"\*{1,3}|`", "", texto)
    txt = re.sub(r"\[\[([^\]|]+)\|?[^\]]*\]\]", r"\1", txt)
    return re.sub(r"\s+", " ", txt).strip()


def parsear_entidades(nodes: list[Path]) -> tuple[dict[str, Entidad], dict[str, Entidad]]:
    """Extrae hipótesis (tabla) y reglas de criterio (viñetas) de los nodes."""
    hips: dict[str, Entidad] = {}
    reglas: dict[str, Entidad] = {}
    for path in nodes:
        for linea in path.read_text(encoding="utf8").split("\n"):
            m = RE_HIP.match(linea)
            if m:
                celdas = [c.strip() for c in m.group(2).strip().strip("|").split("|")]
                enunciado = limpiar(celdas[0]) if celdas else ""
                estado = ""
                for c in celdas[1:]:
                    e = RE_ESTADO.search(c)
                    if e:
                        estado = e.group(1).lower()
                        break
                hips[m.group(1)] = Entidad(
                    id=m.group(1), titulo=sin_markdown(enunciado)[:110],
                    cuerpo=" · ".join(limpiar(c) for c in celdas if c.strip()),
                    origen=path.stem, estado=estado)
                continue
        # Las reglas son viñetas que pueden envolverse en varias líneas (C18, C20
        # y C22 parten el título), así que se unen antes de intentar el match.
        for bloque in bloques_de_vineta(path.read_text(encoding="utf8")):
            m = RE_REGLA.match(bloque)
            if m:
                reglas[m.group(1)] = Entidad(
                    id=m.group(1), titulo=sin_markdown(m.group(2)).rstrip("."),
                    cuerpo=limpiar(m.group(3)), origen=path.stem)
    return hips, reglas


def bloques_de_vineta(texto: str) -> list[str]:
    """Une cada viñeta con sus líneas de continuación en un solo string."""
    bloques: list[str] = []
    actual: list[str] = []
    for linea in texto.split("\n"):
        if re.match(r"^\s*[-*]\s", linea):
            if actual:
                bloques.append(" ".join(actual))
            actual = [linea.rstrip()]
        elif actual and linea.strip() and not linea.startswith("#"):
            actual.append(linea.strip())          # continuación de la viñeta
        elif actual:
            bloques.append(" ".join(actual))
            actual = []
    if actual:
        bloques.append(" ".join(actual))
    return bloques


def slug_autor(nombre: str) -> str:
    """Nombre de archivo estable para un autor."""
    base = re.sub(r"\s*\([^)]*\)", "", nombre)          # quita paréntesis
    base = re.sub(r"[^\w\s&.\-]", "", base, flags=re.U).strip()
    base = re.sub(r"\s+", " ", base)
    return base[:60] or nombre[:60]


def nota_entidad(e: Entidad, tipo: str, fuentes: list[Fuente]) -> str:
    etiqueta = "hipótesis" if tipo == "hipotesis" else "regla"
    fm = ["---", f"tipo: {tipo}", f"id: {yaml_str(e.id)}",
          "aliases:", f"  - {yaml_str(e.id)}",
          f"titulo: {yaml_str(e.titulo)}"]
    if e.estado:
        fm.append(f"estado: {yaml_str(e.estado)}")
    fm += [f'vive_en: "[[{e.origen}]]"', f"fuentes: {len(fuentes)}",
           "tags:", f"  - {tipo}"]
    if e.estado:
        fm.append(f"  - estado/{e.estado}")
    fm.append("---")

    cuerpo = ["", f"# {e.id} · {e.titulo}", ""]
    if e.estado:
        cuerpo += [f"**Estado:** `{e.estado}`", ""]
    if e.cuerpo:
        cuerpo += [e.cuerpo, ""]
    cuerpo += [f"**Vive en:** [[{e.origen}]]", ""]

    if fuentes:
        cuerpo += [f"## Fuentes que tocan esta {etiqueta} ({len(fuentes)})", ""]
        cuerpo += [f"- [[{f.slug}]] — {f.marca} {f.grado} · {f.titulo[:78]}"
                   for f in sorted(fuentes, key=lambda x: (GRADO_ORDEN.get(x.grado, 9), x.num))]
        cuerpo.append("")
    else:
        cuerpo += ["> [!note] Sin fuente enlazada",
                   "> Ninguna fila del códice la cita en su columna «Usado en».", ""]

    cuerpo += ["---", "", "*Nota generada. Editar el node de origen y regenerar.*", ""]
    return "\n".join(fm + cuerpo)


def nota_autor(nombre: str, fuentes: list[Fuente]) -> str:
    c = Counter(f.grado for f in fuentes)
    ecos = [f for f in fuentes if f.eco]
    destinos = sorted({d for f in fuentes for d in (f.nodes | f.outputs)})
    fm = ["---", "tipo: autor", f"nombre: {yaml_str(nombre)}",
          f"fuentes: {len(fuentes)}",
          f"rigor_dominante: {yaml_str(min(c, key=lambda g: GRADO_ORDEN.get(g, 9)))}",
          f"con_eco_de_cita: {len(ecos)}", "tags:", "  - autor"]
    if ecos:
        fm.append("  - autor/con-eco-de-cita")
    fm.append("---")

    cuerpo = ["", f"# {nombre}", "",
              f"**{len(fuentes)} fuentes** en el códice · "
              + " · ".join(f"{g}: {c[g]}" for g in sorted(c, key=lambda g: GRADO_ORDEN.get(g, 9))),
              ""]
    if ecos:
        cuerpo += [f"> [!warning] {len(ecos)} de sus fuentes están marcadas como eco de cita",
                   "> " + ", ".join(f"[[{f.slug}]]" for f in ecos), ""]
    cuerpo += ["## Fuentes", ""]
    cuerpo += [f"- [[{f.slug}]] ({f.anio_txt}) — {f.marca} {f.grado} · {f.titulo[:76]}"
               for f in sorted(fuentes, key=lambda x: -(anio_numerico(x.anio_txt) or 0))]
    if destinos:
        cuerpo += ["", "## Aparece en", ""] + [f"- [[{d}]]" for d in destinos]
    cuerpo += ["", "---", "", "*Nota generada desde el códice.*", ""]
    return "\n".join(fm + cuerpo)


# --------------------------------------------------------------------------- #
# escritura
# --------------------------------------------------------------------------- #
def nota_fuente(f: Fuente) -> str:
    fm = [
        "---",
        "tipo: fuente",
        f"id: {yaml_str(f.id)}",
        "aliases:",
        f"  - {yaml_str(f.id)}",
        f"autor: {yaml_str(f.autor)}",
        f"anio_txt: {yaml_str(f.anio_txt)}",
    ]
    anio = anio_numerico(f.anio_txt)
    if anio:
        fm.append(f"anio: {anio}")
    fm += [
        f"rigor: {yaml_str(f.grado)}",
        f"rigor_marca: {yaml_str(f.marca)}",
        f"orden_rigor: {GRADO_ORDEN.get(f.grado, 9)}",
        f"eco_de_cita: {'true' if f.eco else 'false'}",
        f"huerfana: {'true' if f.huerfana else 'false'}",
    ]
    if f.url.startswith("http"):
        fm.append(f"url: {yaml_str(f.url)}")
    if f.registrado:
        fm.append(f"registrado: {yaml_str(f.registrado)}")

    destinos = sorted(f.nodes) + sorted(f.outputs)
    if destinos:
        fm.append("fundamenta:")
        fm += [f'  - "[[{d}]]"' for d in destinos]
    if f.autor_slug:
        fm.append(f'publicado_por: "[[{f.autor_slug}]]"')
    hips = sorted(f.hipotesis, key=lambda x: int(x[1:]))
    if hips:
        fm.append("hipotesis:")
        fm += [f'  - "[[{h}]]"' for h in hips]
    regs = sorted(f.reglas, key=lambda x: int(x[1:]))
    if regs:
        fm.append("reglas:")
        fm += [f'  - "[[{r}]]"' for r in regs]

    tags = ["fuente", f"rigor/{f.grado.replace('/', '-')}"]
    if f.eco:
        tags.append("eco-de-cita")
    if f.huerfana:
        tags.append("huerfana")
    fm.append("tags:")
    fm += [f"  - {t}" for t in tags]
    fm.append("---")

    cuerpo = [
        "",
        f"# {f.id} · {f.titulo}",
        "",
        f"**Autor:** {f.autor or '—'} · **Año:** {f.anio_txt or '—'}",
        "",
        f"**Rigurosidad:** {f.rigor_texto}",
        "",
        "## Resumen",
        "",
        f.resumen or "_Sin resumen registrado._",
        "",
    ]

    if destinos:
        cuerpo += ["## Fundamenta", ""]
        cuerpo += [f"- [[{d}]]" for d in destinos]
        cuerpo += ["", f"> {f.usado_en}", ""]
    else:
        cuerpo += [
            "## Fundamenta",
            "",
            "> [!warning] Fuente huérfana",
            "> Registrada en el códice pero sin node ni output que la cite.",
            "",
        ]

    if f.autor_slug:
        cuerpo += ["## Autor", "", f"- [[{f.autor_slug}]]", ""]

    if hips or regs:
        cuerpo += ["## Hipótesis y reglas que toca", ""]
        cuerpo += [f"- [[{h}]]" for h in hips]
        cuerpo += [f"- [[{r}]]" for r in regs]
        cuerpo.append("")

    vivas = sorted(f.relacionadas, key=lambda x: int(x.split("-")[1]))
    if vivas:
        cuerpo += ["## Relacionada con", ""]
        cuerpo += [f"- [[{r}]]" for r in vivas]
        cuerpo.append("")

    if f.eco:
        cuerpo += [
            "> [!danger] Marcada como eco de cita / autoridad prestada",
            "> El códice la registra explícitamente como no utilizable como afirmación fuerza.",
            "",
        ]

    if f.url:
        cuerpo += ["## Referencia", "", f.url, ""]

    cuerpo += ["---", "", "*Nota generada desde `research/fuentes/codice.md`. No editar a mano:*",
               "*los cambios se pierden al regenerar. Editar el códice.*", ""]

    return "\n".join(fm + cuerpo)


RE_FM_GENERADO = re.compile(r"^---\n(?:.*?\n)?tipo:\s*(?:node|output)\n.*?\n---\n\n?",
                            re.S)


def insertar_frontmatter(path: Path, campos: list[str], dry: bool) -> bool:
    """Escribe el frontmatter del script sin tocar nunca el cuerpo.

    Si ya hay un frontmatter generado por este script (lo delata `tipo: node` u
    `output`), se reemplaza para que los metadatos no queden viejos. Un frontmatter
    escrito a mano se respeta y no se toca.
    """
    texto = path.read_text(encoding="utf8")
    nuevo = "---\n" + "\n".join(campos) + "\n---\n\n"

    if texto.startswith("---\n"):
        m = RE_FM_GENERADO.match(texto)
        if not m:
            return False  # frontmatter propio del usuario: no tocar
        cuerpo = texto[m.end():]
        if m.group(0) == nuevo:
            return False  # ya está al día
        if not dry:
            path.write_text(nuevo + cuerpo, encoding="utf8")
        return True

    if not dry:
        path.write_text(nuevo + texto, encoding="utf8")
    return True


def tabla(cabeceras: list[str], filas: list[list[str]]) -> str:
    out = ["| " + " | ".join(cabeceras) + " |",
           "|" + "|".join("---" for _ in cabeceras) + "|"]
    out += ["| " + " | ".join(c.replace("|", "\\|") for c in fila) + " |" for fila in filas]
    return "\n".join(out)


# --------------------------------------------------------------------------- #
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="reporta el estado sin escribir nada")
    args = ap.parse_args()
    dry = args.check

    if not CODICE.exists():
        print(f"✕ no encuentro el códice en {CODICE}")
        return 1

    print(f"Leyendo {CODICE.relative_to(RESEARCH.parent)}…")
    fuentes = parsear_codice(CODICE.read_text(encoding="utf8"))
    por_id = {f.id: f for f in fuentes}
    print(f"  {len(fuentes)} fuentes")

    # --- aristas desde el cuerpo de nodes y outputs -------------------------- #
    nodes = sorted(NODES_DIR.glob("*.md"))
    outputs = sorted(OUTPUTS_DIR.glob("*.md"))
    citas_por_doc: dict[str, set[str]] = {}

    for path, destino in [(p, "node") for p in nodes] + [(p, "output") for p in outputs]:
        cuerpo = path.read_text(encoding="utf8")
        citadas = {f"F-{n}" for n in RE_FN.findall(cuerpo)}
        citas_por_doc[path.stem] = citadas
        for fid in citadas:
            f = por_id.get(fid)
            if f is None:
                continue
            (f.nodes if destino == "node" else f.outputs).add(path.stem)

    # Respaldo real de cada documento: unión de las citas inline con lo que el
    # códice declara en su columna «Usado en» (una fuente puede aparecer sólo en una).
    respaldo: dict[str, set[str]] = defaultdict(set)
    for f in fuentes:
        for d in f.nodes | f.outputs:
            respaldo[d].add(f.id)

    # --- entidades: hipótesis, reglas de criterio, autores ------------------ #
    hips, reglas = parsear_entidades(nodes)
    validos_h, validos_c = set(hips), set(reglas)
    for f in fuentes:  # descartar referencias a IDs que no existen
        f.hipotesis &= validos_h
        f.reglas &= validos_c

    por_autor: dict[str, list[Fuente]] = defaultdict(list)
    for f in fuentes:
        if f.autor and not RE_AUTOR_GENERICO.match(f.autor):
            por_autor[slug_autor(f.autor)].append(f)
    autores = {k: v for k, v in por_autor.items() if len(v) >= MIN_FUENTES_POR_AUTOR}
    for slug, fs in autores.items():
        for f in fs:
            f.autor_slug = slug

    fuentes_de_h = defaultdict(list)
    fuentes_de_c = defaultdict(list)
    for f in fuentes:
        for h in f.hipotesis:
            fuentes_de_h[h].append(f)
        for c in f.reglas:
            fuentes_de_c[c].append(f)

    print(f"  entidades: {len(hips)} hipótesis · {len(reglas)} reglas de criterio "
          f"· {len(autores)} autores con {MIN_FUENTES_POR_AUTOR}+ fuentes "
          f"(de {len(por_autor)} distintos)")

    huerfanas = [f for f in fuentes if f.huerfana]
    ecos = [f for f in fuentes if f.eco]
    rotas = sorted({fid for f in fuentes for fid in f.relacionadas if fid not in por_id})
    print(f"  {len(fuentes) - len(huerfanas)} conectadas · {len(huerfanas)} huérfanas "
          f"· {len(ecos)} marcadas eco de cita")
    if rotas:
        print(f"  ⚠️  referencias a IDs inexistentes: {', '.join(rotas)}")

    if dry:
        print("\n--check: no se escribió nada.")
        return 0

    # --- notas de fuente ----------------------------------------------------- #
    if FUENTES_OUT.exists():
        shutil.rmtree(FUENTES_OUT)
    FUENTES_OUT.mkdir(parents=True)
    for f in fuentes:
        (FUENTES_OUT / f"{f.slug}.md").write_text(nota_fuente(f), encoding="utf8")
    print(f"✓ {len(fuentes)} notas en {FUENTES_OUT.relative_to(RESEARCH.parent)}/")

    ENTIDADES = GRAFO / "entidades"
    if ENTIDADES.exists():
        shutil.rmtree(ENTIDADES)
    for sub in ("hipotesis", "reglas", "autores"):
        (ENTIDADES / sub).mkdir(parents=True)
    for hid, e in hips.items():
        (ENTIDADES / "hipotesis" / f"{e.slug}.md").write_text(
            nota_entidad(e, "hipotesis", fuentes_de_h.get(hid, [])), encoding="utf8")
    for cid, e in reglas.items():
        (ENTIDADES / "reglas" / f"{e.slug}.md").write_text(
            nota_entidad(e, "regla", fuentes_de_c.get(cid, [])), encoding="utf8")
    for slug, fs in autores.items():
        (ENTIDADES / "autores" / f"{slug}.md").write_text(
            nota_autor(fs[0].autor, fs), encoding="utf8")
    print(f"✓ {len(hips)} hipótesis + {len(reglas)} reglas + {len(autores)} autores "
          f"en {ENTIDADES.relative_to(RESEARCH.parent)}/")

    # --- frontmatter en nodes y outputs -------------------------------------- #
    tocados = 0
    for path in nodes:
        meta = meta_de_node(path)
        campos = ["tipo: node", f"titulo: {yaml_str(titulo_de(path))}"]
        if "version" in meta:
            campos.append(f"version: {yaml_str(meta['version'])}")
        if "actualizado" in meta:
            campos.append(f"actualizado: {yaml_str(meta['actualizado'])}")
        campos += [f"fuentes: {len(respaldo.get(path.stem, ()))}",
                   "tags:", "  - node"]
        tocados += insertar_frontmatter(path, campos, dry)
    for path in outputs:
        campos = ["tipo: output", f"titulo: {yaml_str(titulo_de(path))}",
                  f"fuentes: {len(respaldo.get(path.stem, ()))}",
                  "tags:", "  - output"]
        tocados += insertar_frontmatter(path, campos, dry)
    print(f"✓ frontmatter escrito en {tocados} archivos "
          f"({len(nodes)} nodes + {len(outputs)} outputs revisados)")

    # --- tableros ------------------------------------------------------------ #
    escribir_tableros(fuentes, nodes, outputs, hips, reglas, fuentes_de_h, autores)
    escribir_config()
    print(f"✓ tableros y configuración de vault en {GRAFO.relative_to(RESEARCH.parent)}/")
    print(f"\nAbrir en Obsidian: «Open folder as vault» → {RESEARCH}")
    return 0


def escribir_tableros(fuentes, nodes, outputs, hips, reglas, fuentes_de_h, autores) -> None:
    GRAFO.mkdir(exist_ok=True)
    dist = Counter(f.grado for f in fuentes)
    total = len(fuentes)
    huerfanas = sorted([f for f in fuentes if f.huerfana], key=lambda f: f.num)
    ecos = sorted([f for f in fuentes if f.eco], key=lambda f: f.num)

    por_node: dict[str, list] = defaultdict(list)
    for f in fuentes:
        for d in f.nodes | f.outputs:
            por_node[d].append(f)

    # 1 · Mapa ---------------------------------------------------------------- #
    filas = []
    for d in sorted(por_node, key=lambda k: -len(por_node[k])):
        fs = por_node[d]
        c = Counter(x.grado for x in fs)
        debiles = c["D"] + c["E"]
        filas.append([
            f"[[{d}]]", str(len(fs)),
            f"{c['A']}", f"{c['B']}", f"{c['C']}", f"{c['D']}", f"{c['E']}",
            f"{debiles * 100 // len(fs)}%",
        ])
    (GRAFO / "Mapa del códice.md").write_text(f"""---
tipo: tablero
titulo: "Mapa del códice"
tags:
  - tablero
---

# Mapa del códice

Proyección de `research/fuentes/codice.md` — **{total} fuentes**, {len(nodes)} nodes,
{len(outputs)} outputs. Regenerar con `python3 research/_grafo/generar_grafo.py`.

## Reparto por rigurosidad

{tabla(["Grado", "Fuentes", "% del total"],
       [[f"{g}", str(dist[g]), f"{dist[g] * 100 // total}%"]
        for g in sorted(dist, key=lambda x: GRADO_ORDEN.get(x, 9))])}

## Carga de evidencia por documento

Cuánta evidencia sostiene cada node/output y de qué calidad.
**% débil** = proporción en 🟠D + 🔴E.

{tabla(["Documento", "Fuentes", "🟢A", "🔵B", "🟡C", "🟠D", "🔴E", "% débil"], filas)}

## Puertas de entrada

- [[Tablero de hipótesis]] — las {len(hips)} hipótesis vivas y su estado
- [[Auditoría de rigor]] — qué se apoya en evidencia débil
- [[Fuentes huérfanas]] — registradas y nunca usadas
- [[Cadenas de eco de cita]] — cifras que no deben usarse como afirmación fuerza
- [[alma]] — mapa de nodes

## Entidades del grafo

| Tipo | Cuántas | Carpeta |
|---|---|---|
| Fuentes | {total} | `_grafo/fuentes/` |
| Hipótesis | {len(hips)} | `_grafo/entidades/hipotesis/` |
| Reglas de criterio | {len(reglas)} | `_grafo/entidades/reglas/` |
| Autores con 2+ fuentes | {len(autores)} | `_grafo/entidades/autores/` |
| Nodes | {len(nodes)} | `_nodes/` |
| Outputs | {len(outputs)} | `_outputs/` |
""", encoding="utf8")

    # 1b · Tablero de hipótesis ---------------------------------------------- #
    orden_estado = {"refutada": 0, "degradada": 1, "contestada": 2,
                    "parcial": 3, "abierta": 4, "respaldada": 5, "": 6}
    hs = sorted(hips.values(), key=lambda e: (orden_estado.get(e.estado, 9), int(e.id[1:])))
    conteo = Counter(e.estado or "sin estado" for e in hips.values())
    (GRAFO / "Tablero de hipótesis.md").write_text(f"""---
tipo: tablero
titulo: "Tablero de hipótesis"
tags:
  - tablero
---

# Tablero de hipótesis

Las **{len(hips)} hipótesis vivas** del proyecto, con la evidencia que cada una tiene
enganchada. Abre cualquiera para ver sus fuentes ordenadas por rigurosidad, o su grafo local
para ver con qué más se cruza.

{tabla(["Estado", "Hipótesis"],
       [[e, str(n)] for e, n in sorted(conteo.items(), key=lambda x: orden_estado.get(x[0], 9))])}

## Con Dataview

```dataview
TABLE WITHOUT ID file.link AS "Hipótesis", estado AS "Estado",
  fuentes AS "Fuentes", titulo AS "Enunciado"
FROM #hipotesis
SORT estado ASC
```

## Instantánea estática

{tabla(["Hipótesis", "Estado", "Fuentes", "Enunciado"],
       [[f"[[{e.slug}]]", e.estado or "—", str(len(fuentes_de_h.get(e.id, []))),
         e.titulo[:96]] for e in hs])}

## Reglas de criterio

{tabla(["Regla", "Título"],
       [[f"[[{e.slug}]]", e.titulo[:110]]
        for e in sorted(reglas.values(), key=lambda x: int(x.id[1:]))])}
""", encoding="utf8")

    # 2 · Auditoría de rigor -------------------------------------------------- #
    debiles = sorted([f for f in fuentes if f.grado in ("D", "E")],
                     key=lambda f: (f.grado, f.num))
    (GRAFO / "Auditoría de rigor.md").write_text(f"""---
tipo: tablero
titulo: "Auditoría de rigor"
tags:
  - tablero
---

# Auditoría de rigor

**{len(debiles)} de {total} fuentes ({len(debiles) * 100 // total}%) son 🟠D o 🔴E.**
No es un defecto en sí — `gossiper` y `marketer` producen ese registro por diseño — pero
sí es donde hay que mirar antes de convertir algo en afirmación fuerza.

## Con Dataview

```dataview
TABLE WITHOUT ID
  file.link AS "Fuente", autor AS "Autor", anio_txt AS "Año",
  rigor_marca + " " + rigor AS "Rigor", fundamenta AS "Fundamenta"
FROM #fuente
WHERE rigor = "D" OR rigor = "E"
SORT rigor ASC, anio DESC
```

Para auditar un node concreto, cambia el `WHERE`:

```dataview
TABLE WITHOUT ID file.link AS "Fuente", rigor_marca + " " + rigor AS "Rigor", autor
FROM #fuente
WHERE contains(string(fundamenta), "tendencias-diseno-innovacion")
SORT orden_rigor ASC
```

## Instantánea estática

{tabla(["Fuente", "Título", "Rigor", "Autor", "Año", "Fundamenta"],
       [[f"[[{f.slug}]]", f.titulo[:70], f"{f.marca} {f.grado}",
         f.autor[:34], f.anio_txt,
         ", ".join(f"[[{d}]]" for d in sorted(f.nodes | f.outputs)) or "—"]
        for f in debiles])}
""", encoding="utf8")

    # 3 · Huérfanas ----------------------------------------------------------- #
    (GRAFO / "Fuentes huérfanas.md").write_text(f"""---
tipo: tablero
titulo: "Fuentes huérfanas"
tags:
  - tablero
---

# Fuentes huérfanas

**{len(huerfanas)} de {total} fuentes ({len(huerfanas) * 100 // total}%)** están registradas
en el códice pero **ningún node ni output las cita**. O son evidencia que se buscó y no se
usó, o son citas que se perdieron al redactar. Vale la pena revisar cuáles de estas son
buenas y quedaron fuera: hay {sum(1 for f in huerfanas if f.grado == "A")} de rigor 🟢A entre ellas.

## Con Dataview

```dataview
TABLE WITHOUT ID
  file.link AS "Fuente", autor AS "Autor", anio_txt AS "Año",
  rigor_marca + " " + rigor AS "Rigor", registrado AS "Registrada"
FROM #fuente
WHERE huerfana = true
SORT orden_rigor ASC, anio DESC
```

## Instantánea estática

{tabla(["Fuente", "Título", "Rigor", "Autor", "Año", "Registrada"],
       [[f"[[{f.slug}]]", f.titulo[:70], f"{f.marca} {f.grado}",
         f.autor[:34], f.anio_txt, f.registrado] for f in huerfanas])}
""", encoding="utf8")

    # 4 · Eco de cita --------------------------------------------------------- #
    (GRAFO / "Cadenas de eco de cita.md").write_text(f"""---
tipo: tablero
titulo: "Cadenas de eco de cita"
tags:
  - tablero
---

# Cadenas de eco de cita

**{len(ecos)} fuentes** que el códice marca explícitamente como *eco de cita*, *huérfana de
cita*, *autoridad prestada* o *evidencia propietaria no auditable* — cifras que circulan con
muchos megáfonos y ninguna fuente primaria localizable. Registradas para no volver a caer,
**no para citarlas**.

Abre el **grafo local** de cualquiera de estas notas para ver la cadena completa: la sección
*Relacionada con* enlaza las fuentes que el propio códice cruza con ella.

## Con Dataview

```dataview
TABLE WITHOUT ID
  file.link AS "Fuente", autor AS "Autor", anio_txt AS "Año", fundamenta AS "Contamina a"
FROM #fuente
WHERE eco_de_cita = true
SORT anio DESC
```

## Instantánea estática

{tabla(["Fuente", "Título", "Rigor", "Autor", "Año", "Aparece en"],
       [[f"[[{f.slug}]]", f.titulo[:70], f"{f.marca} {f.grado}",
         f.autor[:30], f.anio_txt,
         ", ".join(f"[[{d}]]" for d in sorted(f.nodes | f.outputs)) or "—"]
        for f in ecos])}
""", encoding="utf8")

    (GRAFO / "README.md").write_text("""# `_grafo/` — proyección del códice a Obsidian

Todo lo que hay en `fuentes/` y en los tableros de esta carpeta es **generado**. La fuente
de verdad sigue siendo `research/fuentes/codice.md`, que mantiene el skill `cronista`.

```
python3 research/_grafo/generar_grafo.py           # regenerar
python3 research/_grafo/generar_grafo.py --check   # sólo reportar
```

**Nunca edites a mano las notas de `_grafo/fuentes/`** — se borran y se rehacen en cada
corrida. Para corregir una fuente, edita el códice y vuelve a generar.

## Abrir el vault

En Obsidian: *Open folder as vault* → apunta a `research/`. El vault incluye los nodes
reales con sus wikilinks, los outputs, y esta proyección del códice.

Los tableros traen la consulta de **Dataview** y, debajo, una tabla estática equivalente,
para que sirvan aunque no tengas el plugin instalado (Dataview es de comunidad y hay que
instalarlo desde *Settings → Community plugins*).

## Cómo se derivan las aristas

Una fuente enlaza a un node por dos vías, que se unen:

1. La columna *«Usado en / fundamenta»* de su fila en el códice.
2. Las menciones `F-n` en el cuerpo del node o del output.

Los nodes **no** se reescriben para convertir sus `F-n` en wikilinks: la arista la aporta la
nota de la fuente, y así los nodes siguen leyéndose igual fuera de Obsidian.
""", encoding="utf8")


def escribir_config() -> None:
    """Configuración mínima de vault: grafo coloreado por rigor."""
    OBSIDIAN.mkdir(exist_ok=True)
    (OBSIDIAN / "core-plugins.json").write_text(json.dumps({
        "file-explorer": True, "global-search": True, "switcher": True,
        "graph": True, "backlink": True, "outgoing-link": True,
        "tag-pane": True, "outline": True, "word-count": True,
    }, indent=2), encoding="utf8")
    (OBSIDIAN / "app.json").write_text(json.dumps({
        "attachmentFolderPath": "_grafo/adjuntos",
        "newLinkFormat": "shortest",
        "useMarkdownLinks": False,
        "alwaysUpdateLinks": True,
    }, indent=2), encoding="utf8")
    (OBSIDIAN / "graph.json").write_text(json.dumps({
        "collapse-filter": False, "search": "", "showTags": False,
        "showAttachments": False, "hideUnresolved": False, "showOrphans": True,
        "collapse-color-groups": False,
        "colorGroups": [
            {"query": "tag:#node", "color": {"a": 1, "rgb": 15844367}},
            {"query": "tag:#output", "color": {"a": 1, "rgb": 5431378}},
            {"query": "tag:#hipotesis", "color": {"a": 1, "rgb": 11621375}},
            {"query": "tag:#regla", "color": {"a": 1, "rgb": 16764082}},
            {"query": "tag:#autor", "color": {"a": 1, "rgb": 9868950}},
            {"query": "tag:#rigor/A", "color": {"a": 1, "rgb": 4437377}},
            {"query": "tag:#rigor/B", "color": {"a": 1, "rgb": 3576296}},
            {"query": "tag:#rigor/C", "color": {"a": 1, "rgb": 15453984}},
            {"query": "tag:#rigor/D", "color": {"a": 1, "rgb": 14503424}},
            {"query": "tag:#rigor/E", "color": {"a": 1, "rgb": 13959168}},
            {"query": "tag:#eco-de-cita", "color": {"a": 1, "rgb": 16711680}},
        ],
        "collapse-display": False, "showArrow": False, "textFadeMultiplier": -0.8,
        "nodeSizeMultiplier": 0.85, "lineSizeMultiplier": 0.6,
        "collapse-forces": False, "centerStrength": 0.4, "repelStrength": 12,
        "linkStrength": 0.6, "linkDistance": 180, "scale": 0.4,
    }, indent=2), encoding="utf8")


if __name__ == "__main__":
    sys.exit(main())
