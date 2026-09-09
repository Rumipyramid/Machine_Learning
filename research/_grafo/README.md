# `_grafo/` — proyección del códice a Obsidian

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
