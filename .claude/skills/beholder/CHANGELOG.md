# Changelog — Beholder

Todas las versiones notables de este skill. Formato basado en
[Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/).

## [1.2.2] — 2026-06-23
### Cambiado
- Apertura simplificada: la pregunta obligatoria ahora **incluye el link al tablero** en el mismo
  mensaje y **ya no ofrece opciones A/B**.

## [1.2.1] — 2026-06-23
### Cambiado
- La apertura ahora ofrece **dos caminos** tras la pregunta obligatoria: **A) Contar qué pasó**
  (actualizar pendientes) o **B) Revisar el tablero de proyectos** (ver resumen + tablero por
  estado + link).

## [1.2.0] — 2026-06-23
### Añadido
- **Apertura obligatoria:** el Beholder inicia siempre con *"Has accedido al Beholder ¿Qué ha
  pasado últimamente con tus proyectos?"* y guía conversacionalmente al equipo para llenar pendientes.
- **Gobernanza de fechas:** los cambios de fecha proyectada generan una **alerta a todo el equipo**
  (`reportes/ALERTAS_FECHAS.md`) y **solo se aplican con aprobación del owner** (config en
  `reportes/beholder.config.md`). El resto de campos es de edición libre.
- **Repositorio de historial (15 días):** `reportes/historial/` con `registrar_cambio.py` (agrega
  entrada + purga >15 días + regenera `CAMBIOS.md`).

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
