# 📅 Calendario — Agenda de compromisos con fecha

> Nodo de conocimiento persistente: registra los compromisos con fecha (exacta o aproximada)
> que el usuario mencionó en conversación y confirmó agendar en su Google Calendar. No
> reemplaza al calendario real (que es la fuente de verdad del evento en sí) — deja
> trazabilidad de la conversación que originó cada agendado. Mantenido por el skill
> `calendario` (`.claude/skills/calendario/SKILL.md`) cada vez que el usuario confirma un
> agendado. Creado: 2026-07-13.

## Compromisos agendados

| Fecha | Compromiso | Estado | Evento (Google Calendar) | Registrado |
|---|---|---|---|---|
| _(vacío — se completa a medida que se confirman agendados)_ | | | | |

## Convenciones
- Fecha en formato `YYYY-MM-DD`; si es aproximada, se agenda con la mejor estimación y el
  estado queda como `Aproximada` hasta que el usuario confirme el día exacto.
- Estado: `Agendado` (evento creado con fecha exacta), `Aproximada` (evento creado con fecha
  estimada, pendiente de confirmar), `Reagendado`, `Cancelado`.
- La columna "Evento" guarda el id o link que devuelve `mcp__Google_Calendar__create_event`,
  para poder editarlo o borrarlo si el compromiso cambia.
