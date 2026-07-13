---
name: calendario
description: >-
  Regla permanente (no requiere invocación explícita): cada vez que el usuario diga que
  hará algo en una fecha exacta o aproximada ("el jueves tengo...", "a mediados de agosto
  lanzo...", "en dos semanas entrego..."), pregúntale si quiere agendarlo en su Google
  Calendar y, si dice que sí, crea el evento con el MCP de Google Calendar. Cada compromiso
  agendado (o su intento) se registra también como nodo de conocimiento persistente en
  research/calendario/agenda.md. Dispárate en cualquier conversación de este repo, no solo
  cuando el usuario escriba /calendario — es una vigilancia de fondo, igual que la regla de
  registrar fuentes en cronista.
---

# calendario · Agendar compromisos con fecha + nodo de conocimiento

> Esta skill formaliza una instrucción permanente del usuario: toda mención de un plan con
> fecha (exacta o aproximada) dispara una pregunta de agendado. No es una skill que se invoque
> con un comando y punto — es una regla de fondo activa en cualquier sesión sobre este repo.

## 1. Detectar el disparador

Se dispara cuando el usuario **afirma** (no pregunta hipotética, no fecha de un tercero) que
hará/tendrá algo en un momento futuro identificable:
- Fecha exacta: "el 20 de agosto presento...", "el jueves tengo una reunión de...".
- Fecha aproximada: "a mediados de agosto...", "en unas dos semanas...", "el próximo mes...".

No se dispara para fechas puramente pasadas, hipotéticas ("si algún día hiciera..."), o de
otras personas/proyectos ajenos al usuario.

## 2. Preguntar (siempre, antes de crear nada)

Pregunta corto y directo, por ejemplo:
> "¿Quieres que agende esto en tu calendario?"

No crees el evento sin esta confirmación explícita. Si el usuario dice que no, no crees el
evento ni agregues fila al nodo — la conversación sigue normal.

## 3. Si confirma que sí

1. **Resuelve la fecha/hora:**
   - Fecha y hora exactas → úsalas tal cual.
   - Solo fecha (sin hora) → evento de todo el día (`allDay: true`).
   - Fecha aproximada → usa la mejor estimación (p. ej. "a mediados de agosto" → 15 de agosto)
     como evento de todo el día, y dilo explícitamente: "Lo agendo el 15 de agosto como fecha
     aproximada, ajústala cuando tengas el día exacto."
   - Zona horaria por defecto: `America/Lima`, salvo que el usuario indique otra.
2. **Crea el evento** con `mcp__Google_Calendar__create_event` (calendario primario salvo que
   el usuario pida otro — usa `mcp__Google_Calendar__list_calendars` si hay que resolver cuál).
   - `summary`: resumen corto de lo que el usuario dijo que hará.
   - `description`: opcionalmente el detalle tal como lo contó, más nota si la fecha es
     aproximada.
3. **Registra/actualiza** `research/calendario/agenda.md` (crea el archivo con la plantilla de
   abajo si no existe todavía): agrega una fila con fecha, compromiso, estado (`Agendado` o
   `Aproximada`), y el id/link del evento devuelto por `create_event`.
4. Si estás trabajando dentro de una sesión de este repo (no una consulta suelta), commitea el
   cambio a `research/calendario/agenda.md` igual que cualquier otro nodo del códice.

## 4. Mantenimiento del nodo

`research/calendario/agenda.md` es la única fuente de verdad local de qué se agendó desde
Claude Code — no reemplaza al Google Calendar real (que es la fuente de verdad del evento en
sí), sino que deja trazabilidad de la conversación que lo originó. Si el usuario después
cambia o cancela un compromiso, actualiza tanto el evento (`update_event`/`delete_event`) como
la fila correspondiente en el nodo (estado `Reagendado`/`Cancelado`).

## Plantilla del nodo (si hay que crearlo desde cero)

```markdown
# 📅 Calendario — Agenda de compromisos con fecha

> Nodo de conocimiento persistente: registra los compromisos con fecha (exacta o aproximada)
> que el usuario mencionó en conversación y confirmó agendar en su Google Calendar. Mantenido
> por el skill `calendario` cada vez que se confirma un agendado. Creado: AAAA-MM-DD.

## Compromisos agendados

| Fecha | Compromiso | Estado | Evento (Google Calendar) | Registrado |
|---|---|---|---|---|
```
