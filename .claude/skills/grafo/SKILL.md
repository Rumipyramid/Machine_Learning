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
