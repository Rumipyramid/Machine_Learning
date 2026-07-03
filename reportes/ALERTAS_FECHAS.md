# 🚨 Alertas de cambio de fecha — pendientes de aprobación

> **Regla del Beholder:** todo cambio en una **fecha proyectada** genera una alerta para el equipo
> y **solo procede con la aprobación del owner**. Configuración en `reportes/beholder.config.md`.
> **Aprobador:** Alejandro (`Rumipyramid`).

| Fecha/hora | Quién pide | Quest | Fecha anterior | Fecha nueva | Motivo | Estado |
|---|---|---|---|---|---|---|
| 2026-07-03 | Beholder (propuesta) | Q-23 Diseño de piloto | Inicio 09/07/2026 | Inicio 21/07/2026 | Apagar código rojo: pico de Stefanie 11 → 8 monedas simultáneas | APROBADA (por Alejandro, 2026-07-03) |
| 2026-07-03 | Beholder (propuesta) | Q-5 UV Modelo de competencias | Inicio 08/07/2026 | Inicio 09/07/2026 | Bajar pico de Alejandro 8.5 → dentro de la regla de 8 | APROBADA (por Alejandro, 2026-07-03) |

---

### Cómo se usa
1. Cuando alguien pide cambiar una fecha, el Beholder **agrega una fila** aquí con estado
   `PENDIENTE DE APROBACIÓN` y **no** aplica el cambio.
2. El equipo se entera (este archivo + el commit/PR).
3. El **owner** responde `aprobado` → el Beholder aplica el cambio, marca la fila como
   `APROBADA (por Alejandro, AAAA-MM-DD)` y lo registra en `reportes/historial/`.
4. Si el owner lo rechaza, se marca `RECHAZADA` y la fecha queda como estaba.
