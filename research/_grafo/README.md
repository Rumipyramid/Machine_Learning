# `_grafo/` — proyección del códice a Obsidian

Todo lo que hay en `fuentes/` y en los tableros de esta carpeta es **generado**. La fuente
de verdad sigue siendo `research/fuentes/codice.md`, que mantiene el skill `cronista`.

```
python3 research/_grafo/generar_grafo.py           # regenerar
python3 research/_grafo/generar_grafo.py --check   # sólo reportar
```

**Nunca edites a mano las notas de `_grafo/fuentes/`** — se borran y se rehacen en cada
corrida. Para corregir una fuente, edita el códice y vuelve a generar.

## Cómo abrirlo (paso a paso)

1. Clona o actualiza el repo en tu máquina:
   `git clone https://github.com/Rumipyramid/Machine_Learning.git`
   (si ya lo tienes: `git pull`)
2. Descarga Obsidian de <https://obsidian.md> — gratis, no necesitas cuenta.
3. Ábrelo → **Open folder as vault** → elige la carpeta `research/` del repo.
   **Ojo: `research/`, no la raíz del repo.**
4. Al abrir dirá que el vault tiene configuración: acepta *Trust author and enable plugins*.
5. Empieza por `_grafo/Mapa del códice.md`.

Para ver el grafo: icono de las tres bolitas en la barra izquierda (*Graph view*).
Para ver el grafo de una nota sola: `Ctrl/Cmd+P` → *Open local graph*.

**Dataview es opcional.** Los tableros traen la consulta y, debajo, la tabla estática
equivalente. Si lo quieres: *Settings → Community plugins → Browse → Dataview → Install*.

## Qué hay en el grafo

| Tipo | Cuántos | Carpeta |
|---|---|---|
| `#fuente` | 542 | `fuentes/` |
| `#hipotesis` | 31 | `entidades/hipotesis/` |
| `#regla` | 22 | `entidades/reglas/` |
| `#autor` | 24 | `entidades/autores/` |
| `#node` | 18 | `../_nodes/` |
| `#output` | 10 | `../_outputs/` |

Los autores se crean sólo si tienen **2 o más fuentes**: con una sola serían hojas
colgando del grafo sin conectar nada. El umbral está en `MIN_FUENTES_POR_AUTOR`.

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
