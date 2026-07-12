# 00 — Hub de investigación (research/) — Rumipyramid/Machine_Learning

*Mapa maestro de los documentos de conocimiento del proyecto. Última actualización: 2026-07-10.*

Este archivo es el **índice vivo** de `research/`: la vista **global** de qué está vigente y qué
deriva de qué. Como `_nodes/` es plano (sin carpetas por tema), la navegación no la dan las
carpetas: la dan este `_hub.md` y la vista **local** de cada node, en su sección
`## Conexiones`.

> **Alcance de este hub**: cubre el conocimiento de investigación de `research/` (seguros, salud,
> Perú). **No** cubre `research/personas/` (subsistema de código del generador de personas
> sintéticas — schema JSON + matriz + scripts, ya estructurado y referenciado en `CLAUDE.md`) ni
> `research/updates/` (reportes quincenales, ya estructurado y auto-indexado en `CLAUDE.md`).

---

## Reglas de gestión (las cinco consignas)

**1. Una fuente de verdad por tema.** Cada tema es un solo node en `_nodes/`. No se duplica
contenido entre nodes.

**2. Versionado solo por cambio estructural.** La versión sube solo ante un cambio de fundamento
(premisa, modelo, arquitectura, alcance). Lo incremental solo actualiza la fecha.

**3. Hub como mapa.** Este archivo es el único lugar donde se ve qué nodes están vigentes, cuándo
se actualizaron y qué output deriva de cuáles.

**4. Los outputs citan sus nodes-fuente.** "Basado en `node.md` (versión del YYYY-MM-DD)" + citas
por afirmación cuando corresponda.

**5. Conexiones explícitas y recíprocas en wikilinks.** Cada node cierra con `## Conexiones`
(`[[...]]`, con alias). Si A enlaza a B, B enlaza a A.

---

## Estructura de carpetas

| Ruta | Contenido |
|---|---|
| `_hub.md` | Este índice vivo (raíz de `research/`) |
| `_nodes/` | Todo el conocimiento, plano, un `.md` por tema (kebab-case) |
| `fuentes/registro_fuentes.md` | Ledger de `cronista` — bibliografía compartida de todos los nodes, citada por ID (`F-n`). No se movió a `_nodes/` porque `cronista` referencia esta ruta en su propio SKILL.md y en las 116+ filas existentes. |
| `personas/` | Subsistema de código del modelo de personas sintéticas (`lapuerta`) — fuera del alcance de este hub, ver `CLAUDE.md` |
| `updates/` | Reportes quincenales de fortalecimiento del modelo — fuera del alcance de este hub, ver `CLAUDE.md` |

`_nodes/` es plano: nada de subcarpetas por tema.

---

## Nodes vigentes

| Documento | Tema | Última actualización | Versión |
|---|---|---|---|
| `_nodes/seguros-comportamiento-mundo-peru.md` | Comportamiento, percepción y mercado global de seguros (Mundo vs. Perú) | 2026-07-10 | v1.1 |
| `_nodes/glosario-seguro-salud-peru.md` | Glosario de términos de seguro de salud en lenguaje claro (Perú) | 2026-06-25 | v1.0 |
| `_nodes/modelo-salud-ia-farmacias-peru.md` | Modelo de triage con IA + farmacias + atención humana (Perú): investigación, RE-AIM, estrategias de testeo | 2026-07-06 | v1.0 |
| `_nodes/mecanismos-seguros-salud.md` | Mecanismos de seguros de salud: presión demográfica/costo, y modelos que la navegan (global, comparativo) | 2026-07-10 | v1.0 |

---

## Outputs activos

| Output | Construido sobre (nodes) | Última actualización | Estado |
|---|---|---|---|
| _(vacío — aún no se ha generado ningún output formal desde los nodes)_ | | | |

> **Estado**: `al día` o `requiere refresh`.

---

## Documentos pendientes de crear

- _(vacío)_

---

## Bibliografía compartida

`fuentes/registro_fuentes.md` (ledger de `cronista`, mantenido por ese skill) — 116+ fuentes
(F-1...) citadas por ID desde cualquier node. Reglas de uso desde este hub:

- Cada node cita fuentes por ID (`F-n`) en vez de repetir la referencia completa.
- Al crear/actualizar un node con evidencia nueva, registrar la fuente en el ledger primero
  (skill `cronista`), luego citarla por ID en el node.

---

## Cómo se mantiene este hub

`/seeker` y `/trinidad` escriben directamente a `_nodes/` al terminar una investigación (ver regla
en `CLAUDE.md`), no solo responden en el chat. El agente mantiene este hub en cada sesión:
actualiza fechas/versiones al tocar nodes, agrega filas nuevas al crear/mover/renombrar, y
actualiza la fecha de cabecera con cada cambio.
