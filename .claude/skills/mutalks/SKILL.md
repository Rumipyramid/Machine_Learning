---
name: mutalks
description: Abre el front "Pregúntale a Mu", la página donde se le hacen preguntas al segundo cerebro (artefacto https://claude.ai/artifact/3564MJATLFeuP7soFwpPSm). Antes de abrirlo verifica que el corpus publicado esté al día con los nodes y el ledger; si no, lo regenera y lo republica. Úsalo SIEMPRE que el usuario invoque /mutalks, o pida "abrir Pregúntale a Mu", "quiero preguntarle al cerebro", "hablar con Mu" o "el front de preguntas".
---

# /mutalks: abrir "Pregúntale a Mu"

El front de preguntas al cerebro es un **artefacto privado** de claude.ai:

- **URL:** https://claude.ai/artifact/3564MJATLFeuP7soFwpPSm
- **Página:** `research/grafo/preguntar/index.html` (se publica como `index.html`).
- **Corpus:** `mu-corpus.json`, generado por `research/grafo/preguntar/build_corpus.py`. No se versiona
  (está en `.gitignore`); solo vive como archivo publicado del artefacto.
- **Capacidades declaradas:** `db`, `sample`, `user`. Al republicar, **omite `capabilities`** para conservarlas.
  La base `db` guarda el backlog de temas y el instrumento de impacto (N7): **nunca la borres ni la reescribas**
  desde esta skill.

## Pasos

1. **Regenerar el corpus** desde la raíz del repo:
   `python research/grafo/mu.py >/dev/null && python research/grafo/preguntar/build_corpus.py`.
   El corpus incluye el estado del panel, así que conviene regenerar Mu primero.
2. **Comparar con lo publicado.** Lee el artefacto con `Artifact` `action: "read"` y `path: "mu-corpus.json"` y
   compara el número de fuentes y de fragmentos de nodes (`fuentes`, `nodes`) y la fecha `generado` con el corpus
   local. Si la página local `index.html` cambió respecto de la publicada, también hay que republicarla.
3. **Si está desactualizado, republicar.** Lee el artefacto **sin `path`** (requisito para republicar) y publica con
   `url` = la del artefacto, `file_path` = `research/grafo/preguntar/index.html` y
   `files` = `{"mu-corpus.json": "research/grafo/preguntar/mu-corpus.json"}`, **sin** `capabilities` ni `icon`.
   Si la publicación choca con una versión más nueva (por ejemplo, un cambio guardado desde la página), vuelve a
   leerla y publica encima de esa versión; nunca uses `force`.
4. **Abrir el front** con `Artifact` `action: "open"` y la URL.
5. **Responder en 2-3 líneas:** el link, si el corpus estaba al día o se republicó (fuentes, nodes y fecha antes →
   después), y un recordatorio: las respuestas citan F-n del ledger y el botón "¿Te sirvió?" alimenta el N7 de Mu.

## Reglas

- No edites nodes, ledger ni `alma.md` desde esta skill.
- Si el artefacto no se puede leer ni publicar (sin permiso de escritura, refusal o red), ábrelo igual y avisa
  que el corpus puede estar desactualizado, con la fecha `generado` que muestra.
- Esta skill no reemplaza a `/mu` (el panel de indicadores): `/mutalks` es para conversar con el cerebro y `/mu`
  para medirlo.
