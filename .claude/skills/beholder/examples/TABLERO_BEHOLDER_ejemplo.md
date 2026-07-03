# 🐉 Tablero Beholder — Onboarding 2.0

> Ejemplo de salida del skill **Beholder** con datos ficticios. Muestra los cuatro estados de
> capacidad (⚪/🟢/🔴/⛔ — aquí se ven 🟢 y 🔴), un quest con riesgo alto 🚩 y el libro mayor
> reconciliado.

**Estado del proyecto:** WIP  ·  **Ciclo/Sprint:** Sprint 7  ·  **Fecha:** 2026-06-22

## 📊 Resumen
| Métrica | Valor |
|---|---|
| Épicas | 2 |
| Quests | 4 |
| Colaboradores | 2 |
| Fichas comprometidas / capacidad | 17 / 16 |
| Quests con riesgo alto 🚩 | 1 |
| Alertas de capacidad (sobreasignados 🔴) | 1 |

## 🗂️ Tablero por estado
> Columnas estilo Jira. Cada quest aparece bajo su estado actual.

| Backlog | To Do | In Progress | In Review | Done |
|---|---|---|---|---|
| — | Q-2 · Email de bienvenida | Q-1 · Rediseñar registro 🚩 | Q-4 · Panel de analítica | — |
| | | Q-3 · Checklist primeros pasos | | |

## 📋 Épicas y quests (detalle)

### EPIC-1 · Flujo de bienvenida
Reducir la fricción del primer ingreso y activar al usuario en el día 1.

| Clave | Quest | Estado | Status del proyecto | Fecha de inicio | Fecha de cierre | Fichas | Behavioral designers | Riesgos | Impacto |
|---|---|---|---|---|---|---|---|---|---|
| Q-1 | Rediseñar pantalla de registro | In Progress | Maqueta lista; pendiente revisión de Legal | 15/06/2026 | 03/07/2026 | 8 🎟️ | Mara, Cassian | Dependencia con Legal 🚩 | −20% abandono en registro |
| Q-2 | Email de bienvenida conductual | To Do | Copy en borrador; falta setup de dominio | 06/07/2026 | 10/07/2026 | 3 🎟️ | Mara | Deliverability / spam | +10% activación en D1 |

### EPIC-2 · Activación
Llevar al usuario a su primer "momento de valor" en la semana 1.

| Clave | Quest | Estado | Status del proyecto | Fecha de inicio | Fecha de cierre | Fichas | Behavioral designers | Riesgos | Impacto |
|---|---|---|---|---|---|---|---|---|---|
| Q-3 | Checklist de primeros pasos | In Progress | 3 de 5 pasos instrumentados | 22/06/2026 | 08/07/2026 | 4 🎟️ | Cassian | — | +8% retención semana 1 |
| Q-4 | Panel de analítica de onboarding | In Review | Dashboard armado; validando datos por paso | 10/06/2026 | — | 2 🎟️ | Cassian | Datos incompletos por paso | Visibilidad de drop-off por paso |

## 🎟️ Libro mayor de fichas (capacidad del equipo)
> Regla: 8 de 10 fichas comprometidas. Las 2 restantes son reserva de overhead.

| Colaborador | Comprometidas (de 8) | Reserva (de 2) | Estado | Desglose por quest |
|---|---|---|---|---|
| Mara | 8 | 2 | 🟢 Óptimo | Q-1: 5, Q-2: 3 |
| Cassian | 9 | 1 | 🔴 Sobreasignado | Q-1: 3, Q-3: 4, Q-4: 2 |

**Alertas de capacidad:** (solo sobreasignados/inválidos; la holgura no genera alerta)
- 🔴 **Cassian: 9 comprometidas.** Usa 1 ficha de su reserva → le queda medio tanque para
  overhead (coordinación, contexto, imprevistos). **Ajuste sugerido:** mover 1 ficha de Q-4
  (In Review, casi cerrado) a la reserva → vuelve a 8 🟢 Óptimo.

## 🚩 Registro de riesgos
| Clave | Quest | Riesgo | Severidad | Mitigación sugerida |
|---|---|---|---|---|
| Q-1 | Rediseñar pantalla de registro | Dependencia con Legal para textos/consentimiento | Alta | Cerrar revisión legal en sprint actual; preparar versión sin campos sensibles como plan B |
| Q-2 | Email de bienvenida conductual | Deliverability / caer en spam | Media | Calentar dominio; pruebas A/B de asunto; validar SPF/DKIM |
| Q-4 | Panel de analítica de onboarding | Datos incompletos por paso | Media | Instrumentar eventos faltantes antes de publicar el panel |

## 📈 Impacto
| Clave | Quest | Impacto esperado |
|---|---|---|
| Q-1 | Rediseñar pantalla de registro | −20% abandono en registro |
| Q-2 | Email de bienvenida conductual | +10% activación en D1 |
| Q-3 | Checklist de primeros pasos | +8% retención semana 1 |
| Q-4 | Panel de analítica de onboarding | Visibilidad de drop-off por paso |
