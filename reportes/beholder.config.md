# ⚙️ Configuración del Beholder (este despliegue)

> El skill lee este archivo al iniciar para saber quién aprueba y dónde guardar alertas e historial.

- **Owner / aprobador de fechas:** **Alejandro (GitHub: `Rumipyramid`)** — alejandrorv89@gmail.com
- **Tablero:** `TABLERO_BEHOLDER.md`
- **Matriz (Excel):** `reportes/Status_Proyectos_Behavioral_Design.xlsx`
- **Alertas de fecha:** `reportes/ALERTAS_FECHAS.md`
- **Repositorio de historial (15 días):** `reportes/historial/` (`CAMBIOS.md` + `CAMBIOS.csv`)
- **Retención del historial:** **15 días**

### Equipo y nivel de expertise
> El Beholder usa este roster al proponer distribuciones de carga: el junior no lleva solo
> entregables críticos ni la mayor carga total; los seniors acompañan lo crítico.

| Miembro | Nivel de expertise | Vacaciones | Nota |
|---|---|---|---|
| Alejandro | **Senior** | — | Owner del tablero y aprobador de fechas |
| Melissa | **Semi senior** | — | — |
| Stefanie | **Semi senior** | — | — |
| Felipe | **Junior** | — | 6 meses en el equipo |

> **Vacaciones:** formato `dd/mm/aaaa a dd/mm/aaaa` (varios periodos separados por `;`).
> Durante las vacaciones la capacidad es **0 monedas**: cualquier iniciativa agendada en ese
> periodo dispara **🚨 código rojo** (lo detecta `python reportes/beholder_tools.py validar`).

### Reglas de la economía local (monedas 🪙 — Q3-2026)
1. Las monedas miden el **esfuerzo del trimestre** por persona.
2. **Concurrencia:** nadie usa más de **8 monedas al mismo tiempo** (suma de iniciativas cuyas fechas se solapan).
3. **Reparto igualitario:** las monedas de una iniciativa se dividen **en partes iguales** entre los involucrados (50/50, 33/33/33).
4. **Solo enteros:** nadie puede tener **media moneda** asignada. Si el total de la iniciativa no divide en enteros, se redondea al múltiplo válido más cercano (en empate, hacia abajo, para no inflar esfuerzo).
5. **Vacaciones = capacidad 0:** no se agenda trabajo a nadie durante sus vacaciones (registradas en el roster de arriba); si ocurre, es 🚨 código rojo.

### Herramientas del despliegue
- `python reportes/beholder_tools.py validar` — picos, vacaciones, vencidos y monedas sin programar; **exit 1 si hay código rojo** (correr antes de publicar a main).
- `python reportes/beholder_tools.py digest` — digest semanal → `reportes/DIGEST.md`.
- `python reportes/beholder_tools.py gantt` — regenera el Gantt (Mermaid) dentro del tablero.
- `python reportes/beholder_tools.py retro` — monedas vs. días invertidos (calibración de estimaciones).
- `python reportes/generar_matriz_status.py` — regenera el Excel **desde el tablero** (única fuente de verdad).

### Campos controlados (requieren aprobación del owner)
- Fechas proyectadas: **Fecha de entrega**, fecha de cierre, sprint asignado, hitos.

### Campos de edición libre (se aplican directo, pero se registran en el historial)
- Estado, % Avance, Status (detalle), Riesgos, Impacto, Intervención de diseño de conducta,
  Equipo Behavioral Design (owners), Stakeholder, Fichas, Objetivo, Prioridad.

> Para cambiar el aprobador o la retención, edita este archivo.
