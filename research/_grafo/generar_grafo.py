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
    escribir_tableros(fuentes, nodes, outputs)
    escribir_config()
    print(f"✓ tableros y configuración de vault en {GRAFO.relative_to(RESEARCH.parent)}/")
    print(f"\nAbrir en Obsidian: «Open folder as vault» → {RESEARCH}")
    return 0


def escribir_tableros(fuentes, nodes, outputs) -> None:
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

- [[Auditoría de rigor]] — qué se apoya en evidencia débil
- [[Fuentes huérfanas]] — registradas y nunca usadas
- [[Cadenas de eco de cita]] — cifras que no deben usarse como afirmación fuerza
- [[alma|alma — mapa de nodes]]
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
