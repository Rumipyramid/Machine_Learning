# Changelog — Beholder

Todas las versiones notables de este skill. Formato basado en
[Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/).

## [1.6.0] — 2026-07-04
### Añadido
- **Apertura con mascota y lema:** el Beholder abre cada sesión con el banner ASCII del ojo con
  alas y la frase *«Beauty is in the eye of the beholder»*; la versión animada
  (`assets/beholder.svg` — parpadea, aletea y flota) queda embebida en la cabecera del tablero.
### Cambiado
- **Gantt con tema de alto contraste:** franjas de sección claras, texto oscuro fuera de las
  barras y texto blanco dentro (barras azules; activas ámbar, done gris, críticas rojas) para
  que ninguna letra se pierda contra el fondo.

## [1.5.0] — 2026-07-04
### Añadido
- **Caja de herramientas** (`reportes/beholder_tools.py`): `validar` (picos de concurrencia,
  vacaciones, vencidos, monedas sin programar — exit 1 si hay rojo, obligatorio antes de
  publicar), `digest` (resumen semanal → `DIGEST.md`), `gantt` (Gantt Mermaid embebido en el
  tablero) y `retro` (monedas vs. días para calibrar estimaciones).
- **Excel desde el tablero:** `generar_matriz_status.py` ahora lee `TABLERO_BEHOLDER.md` como
  única fuente de verdad — se acabó la desincronización.
- **Chequeo de vencimientos al abrir sesión** (¿se entregó o movemos la fecha?), **modo
  `/beholder resumen`**, sección **🔗 Dependencias** con evaluación de efecto dominó ante
  cambios de fecha, e **Issues de GitHub por código rojo**.
- **Vacaciones en el roster** de la config: capacidad 0 durante el periodo; trabajo agendado
  en vacaciones dispara 🚨 código rojo (lo detecta el validador).

## [1.4.1] — 2026-07-03
### Añadido
- **Roster con nivel de expertise** en la config del despliegue (`beholder.config.md`): el
  Beholder lo registra en el Paso 2 y lo usa en propuestas de distribución de carga (el junior
  no lleva solo entregables críticos; los seniors acompañan lo crítico).
- Config: **reglas de la economía local** (esfuerzo del trimestre, ≤ 8 simultáneas, reparto
  igualitario 50/50 y **solo monedas enteras** — sin medias monedas).

## [1.4.0] — 2026-07-03
### Añadido
- **Dimensionamiento de riesgos y códigos de alerta:** matriz probabilidad × impacto que asigna
  🚨 **código rojo** / ⚠️ **código amarillo** / 🟢 verde a cada riesgo, con disparadores
  automáticos (⛔ capacidad, ruta crítica bloqueada, fecha controlada vencida o sin aprobación,
  🔴 sobreasignación, monedas sin programar, entregas próximas sin avance). Protocolo: sección
  **"Alertas activas"** después del Resumen, anuncio de códigos al abrir sesión, y registro +
  push inmediato de todo código rojo. Una mitigación activa baja el código un nivel.
- Registro de riesgos con columnas **Probabilidad | Impacto | Código** (reemplaza "Severidad").

## [1.3.0] — 2026-07-03
### Añadido
- Columnas obligatorias **"Fecha de inicio"** y **"Fecha de cierre"** en todas las tablas de
  detalle del tablero (`dd/mm/aaaa`; `—` si el quest no está programado). Son los campos
  controlados de la gobernanza: cambiarlas requiere aprobación del owner. Plantilla y ejemplo
  actualizados.

## [1.2.2] — 2026-06-23
### Cambiado
- Apertura simplificada: la pregunta obligatoria ahora **incluye el link al tablero** en el mismo
  mensaje y **ya no ofrece opciones A/B**.

## [1.2.3] — 2026-06-25
### Añadido
- Nueva columna **"Status del proyecto"** en las tablas de detalle del tablero (el status
  descriptivo, distinto del `Estado` Jira). Plantilla y ejemplo actualizados.

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
