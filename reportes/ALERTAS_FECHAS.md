# 🚨 Alertas de cambio de fecha — pendientes de aprobación

> **Regla del Beholder:** todo cambio en una **fecha proyectada** genera una alerta para el equipo
> y **solo procede con la aprobación del owner**. Configuración en `reportes/beholder.config.md`.
> **Aprobador:** Alejandro (`Rumipyramid`).

| Fecha/hora | Quién pide | Quest | Fecha anterior | Fecha nueva | Motivo | Estado |
|---|---|---|---|---|---|---|
| — | — | — | — | — | — | (sin alertas pendientes) |

---

### Cómo se usa
1. Cuando alguien pide cambiar una fecha, el Beholder **agrega una fila** aquí con estado
   `PENDIENTE DE APROBACIÓN` y **no** aplica el cambio.
2. El equipo se entera (este archivo + el commit/PR).
3. El **owner** responde `aprobado` → el Beholder aplica el cambio, marca la fila como
   `APROBADA (por Alejandro, AAAA-MM-DD)` y lo registra en `reportes/historial/`.
4. Si el owner lo rechaza, se marca `RECHAZADA` y la fecha queda como estaba.
