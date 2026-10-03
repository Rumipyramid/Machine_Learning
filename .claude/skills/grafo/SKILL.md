---
name: grafo
description: Grafologiza la base de conocimiento (nodes, outputs, ledger F-n) y reporta con total transparencia estado, evolución y enriquecimiento del segundo cerebro de diseño. Invócalo con /grafo o cuando pidan "estado del cerebro", "métricas del segundo cerebro", "grafo de conocimiento", "cómo ha evolucionado el node de diseño" o "qué tan enriquecido está".
---

# /grafo — grafo y métricas del segundo cerebro

1. Ejecuta `python research/grafo/build_grafo.py` desde la raíz del repo (solo stdlib; ~5 s).
2. Lee `research/grafo/ESTADO.md` y resume al usuario: estado (§1-2), evolución (§3), métricas M1-M7 (§4),
   fallas de integridad (§5). **Reporta las fallas ⚠️ tal cual y los límites de §7**; no los suavices.
3. Definiciones y fórmulas: `research/grafo/METRICAS.md`. Visor: `research/grafo/grafo.html`.
4. No edites nodes, ledger ni `alma.md` desde esta skill; si hay fallas, proponlas como siguiente paso y pregunta.
5. Tras cada corrida de `/trinidad` o del proceso diario de Lobo, regenerar deja la serie histórica al día.

## Modo semántico — revisar el códice de a poco y extraer relaciones

Grafo de entidades y relaciones con evidencia, en `research/grafo/relaciones/` (memoria en `estado.json`,
datos en `triples.jsonl` y `entidades.json`, vocabulario CERRADO en `vocabulario.json`).

1. `python research/grafo/relaciones/relaciones.py next -n 5` → siguiente lote (prioriza fuentes del cerebro de
   diseño, luego rigor A→E, luego ID). Cinco por lote, igual que `cerrajero`.
2. **Lee cada fuente más allá de la ficha** (WebSearch/WebFetch del abstract o texto). Si solo leíste la ficha,
   la relación lleva `lectura: "ficha"`; nunca la presentes como leída a fondo.
3. Escribe `lote_NNN.json` (entidades + relaciones, cada una con `f`, `apoyo` ≤300 car., `lectura`, `fuerza`).
   Reutiliza ids de entidad existentes (revisa `entidades.json`) para que las fuentes converjan en el mismo nodo.
4. `... relaciones.py add lote_NNN.json` (el validador rechaza relaciones fuera del vocabulario, fuentes
   inexistentes, apoyos vacíos o fuentes sin relaciones ni nota `sin_aporte`) → `check` → `render`.
5. **Discrepancias contra el ledger** (autor, año, cifras) van en `discrepancias` del lote y se reportan al
   usuario; **no** se corrigen el ledger ni los nodes sin pedirlo (eso es de `cronista`).
6. Cierra cada lote diciendo cobertura (X de 468), qué convergió, qué tensiones aparecieron y qué no se pudo
   verificar. Pide permiso antes de proponer relaciones nuevas al vocabulario.

### Dos pasadas (eficiencia de tokens)
- **Pase de amplitud (barato):** lotes de ~8 fuentes a nivel `ficha`, sin búsqueda web; cada relación queda marcada `lectura: "ficha"`.
- **Pase de profundidad (selectivo):** `relaciones.py next --mejorar` lista lo procesado solo a nivel ficha; léelo (abstract/texto) y
  reemplaza con un lote nuevo `abstract`/`completa`. Prioriza fuentes que están en tensión (`contradice`) o con discrepancias abiertas.
- Las correcciones al ledger solo se aplican si la discrepancia se verificó en la fuente y el usuario lo autorizó; se anota la corrección en la propia ficha.
- **Autorización permanente para datos bibliográficos (regla del usuario, 2026-10-03).** Cuando una ficha tiene
  **autor, año, revista, volumen o DOI** faltantes o mal registrados (p. ej. la revista o el repositorio como autor,
  "autores no individualizados", "s.f.") y el dato correcto se **verificó contra el resumen oficial o la página
  del editor**, se corrige **sin preguntar**: se anota "⚠️ corregido AAAA-MM-DD (autoría verificada contra el
  resumen oficial)" en la ficha, la discrepancia se registra en el lote **ya cerrada** con su `resolucion`, y se
  informa al usuario al cierre del lote.
  - **No cubre** (sigue pidiendo permiso): cambios de **cifras, hallazgos, conclusiones, rigor (A-E) o URL**,
    ni datos bibliográficos que no se pudieron verificar (esos quedan como discrepancia abierta).
  - Si la corrección de autoría afecta lo que un node atribuye a esa fuente, el node también requiere permiso.
