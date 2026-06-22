# Changelog — Beholder

Todas las versiones notables de este skill. Formato basado en
[Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/).

## [1.1.1] — 2026-06-22
### Añadido
- **Empaquetado para GitHub:** `README.md`, `CHANGELOG.md`, ejemplo en `examples/`,
  `LICENSE` (MIT) y `.gitignore`.
- Guía y script (`publish_beholder_standalone.sh`) para publicar el skill como repositorio
  independiente, instalable con `git clone <url> ~/.claude/skills/beholder`.

## [1.1.0] — 2026-06-22
### Añadido
- **Entrega de link funcional obligatoria.** El render ahora siempre guarda el tablero en un
  archivo y cierra con un link que abre de verdad el `.md` (URL de GitHub al blob en la rama,
  link a *Files changed* del PR, o archivo adjunto), porque una ruta de archivo no es clicable
  fuera de la terminal.
- Nota de robustez: "el entregable no está completo si el usuario no puede abrir el tablero
  con un clic".

## [1.0.0] — 2026-06-22
### Añadido
- Versión inicial del skill **Beholder**.
- Entrevista adaptativa (nuevo / WIP) y render del tablero estilo Jira en Markdown.
- **Economía de fichas 8/2** con validación de capacidad por colaborador
  (⚪ holgura · 🟢 óptimo · 🔴 sobreasignado · ⛔ inválido) y libro mayor reconciliado.
- Mapeo a conceptos de Jira (épicas → Epic, quests → Story, fichas → story points,
  behavioral designers → assignees, riesgos → flags 🚩).
- Plantilla de salida fija: resumen, tablero por estado, detalle de épicas/quests,
  libro mayor de fichas, registro de riesgos e impacto.
