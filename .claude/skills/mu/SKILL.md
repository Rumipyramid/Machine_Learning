---
name: mu
description: Panel brutalista del segundo cerebro con indicadores numéricos y gráficos de SALUD (integridad), MADUREZ (qué tan probado), RIQUEZA (cuánto hay) y EVOLUCIÓN. Invócalo con /mu (o /Mu), o cuando pidan "el panel", "dashboard del cerebro", "indicadores de salud/madurez/riqueza", "cómo está el cerebro hoy".
---

# /mu — panel del segundo cerebro

Eficiencia: **no leas archivos grandes**; el script hace todo y el panel es HTML autocontenido.

1. Ejecuta desde la raíz del repo: `python research/grafo/mu.py` (solo stdlib, ~3 s). Imprime 4 líneas de resumen
   (SALUD / MADUREZ / RIQUEZA / ALERTAS) y escribe `research/grafo/mu.html`.
2. Si hay `SendUserFile`, envía `research/grafo/mu.html` con `display: "render"` para que el usuario vea el panel.
3. Responde en ≤6 líneas: los números clave tal cual salen del script y las 2-3 alertas más accionables. **No suavices**
   las fallas (rojo = requiere atención) y recuerda el límite: citar ≠ validar; el uso externo no se mide.
4. No edites nodes, ledger ni `alma.md` desde esta skill. Si el usuario quiere actuar sobre una alerta, propón el
   siguiente comando (`relaciones.py next --mejorar`, corregir enlace no recíproco, etc.) y pregunta.

## Identidad visual (regla del usuario, 2026-10-03)
**Todo lo que se pida "de Mu"** (panel, guías, one-pagers, láminas, decks, reportes visuales) usa la identidad
de `IDENTIDAD.md` de esta carpeta: blanco/negro + un solo naranja de alerta (`#ff3b00`), Impact + monoespaciada,
esquinas rectas, reglas de 8px, secciones numeradas con barra invertida y señalética ✓/✗. Partir de
`mu-base.css` (mismos tokens y clases del panel). No inventar otra paleta ni otro estilo para piezas de Mu.

Indicadores (definiciones en `research/grafo/METRICAS.md`; titulares = cifras crudas, sin índices compuestos inventados):
- **00 INTELIGENCIA:** nivel N0-N7 (escalera de criterios en `niveles.json`; umbrales propuestos, editables) y qué falta para el siguiente.
- **01 SALUD:** chequeos de integridad OK/total, enlaces no recíprocos, discrepancias ledger↔fuente, huérfanos de cita, fuentes sin node.
- **02 MADUREZ:** falsabilidad ejercida, autocorrección, reglas trazables, base A+B, relaciones leídas más allá de ficha, lectura profunda (Lobo).
- **03 RIQUEZA:** fuentes, nodes, enlaces, fuentes del node de diseño, cobertura del grafo semántico, entidades, convergencias, tensiones.
- **04 EVOLUCIÓN:** ledger por fecha de registro (el historial git está truncado) y barridos semánticos. **05 NODES:** peso por node.
- **06 TEMAS:** qué sabe el cerebro de cada node: subgrafo semántico (relaciones cuya fuente cita el node o un
  output derivado), cobertura, convergencias y tensiones; mapa radial SVG (sin JS) para nodes con ≥10 relaciones,
  primero los de la última fecha de `alma.md`. Si un tema nuevo no aparece aquí, falta su barrido semántico
  (`/grafo`, modo semántico), no un cambio en Mu.
