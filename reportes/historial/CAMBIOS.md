# 🕝 Historial de cambios del Beholder — últimos 15 días

> Generado por `registrar_cambio.py`. **No editar a mano.** El historial completo siempre queda en el git log.
> Retención: 15 días · Última actualización: 2026-07-04T03:29:58 · Cambios vigentes: 57

| Fecha/hora | Autor | Quest | Campo | Antes | Después | Tipo | Estado |
|---|---|---|---|---|---|---|---|
| 2026-07-04T03:29:58 | Alejandro | Gantt/Mascota | Estilo | Texto oscuro fuera de barras; mascota de colores saturados | Gantt 100% texto blanco sobre tema oscuro + nombres completos; mascota pastel con grano y trazos tenues | normal | aplicado |
| 2026-07-04T03:25:12 | Alejandro | Beholder | v1.6.0 | Gantt con tema por defecto; apertura sin mascota | Gantt de alto contraste + apertura con lema y mascota animada (assets/beholder.svg) | normal | aplicado |
| 2026-07-04T03:18:44 | Alejandro | Gantt | Formato | Barras con clave Q-n | Barras con nombre de la iniciativa + responsables (quién hace cada cosa) | normal | aplicado |
| 2026-07-04T03:13:38 | Alejandro | Beholder | Mejoras v1.5.0 | Validación manual; Excel aparte; sin digest/gantt/retro | beholder_tools.py (validar/digest/gantt/retro), Excel desde el tablero, dependencias, vencimientos, Issues por rojo | normal | aplicado |
| 2026-07-04T03:13:38 | Alejandro | Config | Vacaciones | — | Campo Vacaciones en el roster; capacidad 0 durante el periodo (regla 5) | normal | aplicado |
| 2026-07-04T03:13:38 | Beholder | Q-6/Q-7/Q-17 | Código rojo | In Progress con cierre 03/07 | 🚨 Vencidos: pendiente decisión del owner (entregado → Done, o mover fecha) | normal | aplicado |
| 2026-07-03T22:22:50 | Alejandro | Q-40/Q-42 | Estado | Diseñado (estado intermedio) | Done — el estado 'Diseñado' se elimina del tablero | normal | aplicado |
| 2026-07-03T22:20:09 | Alejandro | EPIC-9 | Épica | Backlog Q3 (previas), status 'Backlog del Chapter SD1' | Repositorio de iniciativas en Backlog; estado/status: solo 'Backlog' | normal | aplicado |
| 2026-07-03T21:53:44 | Alejandro | Economía | Regla de enteros | Se permitían medias monedas (1.5, 1.3) | Nadie puede tener media moneda; totales se redondean al múltiplo válido más cercano (empate: abajo) | normal | aplicado |
| 2026-07-03T21:53:44 | Alejandro | Q-37/Q-13/Q-24/Q-25 | Redistribución 50/50 | F4; F3; S5; S3 | F2·A2; F1·M1; S2·M2; S1·F1 — totales: A21, M21, S20, F19 (81 🪙) | normal | aplicado |
| 2026-07-03T21:53:44 | Alejandro | Q-2/Q-26 | Ajuste por regla de enteros | Q-2: 1.5·1.5 (3); Q-26: 1.3·1.3·1.3 (4) | Q-2: 1·1 (2); Q-26: 1·1·1 (3) | normal | aplicado |
| 2026-07-03T21:53:44 | Alejandro | Q-23 | Fecha de inicio | 09/07/2026 | 21/07/2026 — apaga código rojo de Stefanie (pico 11 → 8) | fecha | aprobada |
| 2026-07-03T21:53:44 | Alejandro | Q-5 | Fecha de inicio | 08/07/2026 | 09/07/2026 — pico de Alejandro dentro de la regla | fecha | aprobada |
| 2026-07-03T21:53:44 | Beholder | Alerta | Código rojo | 🚨 Stefanie pico 11 (09-17/07) | RESUELTO: redistribución + fecha Q-23 aprobada; todos los picos ≤ 8 | normal | aplicado |
| 2026-07-03T21:53:44 | Alejandro | Config | Nivel de expertise | — | Roster en beholder.config.md: Alejandro Senior; Melissa y Stefanie Semi senior; Felipe Junior (6 meses) | normal | aplicado |
| 2026-07-03T21:39:39 | Alejandro | Economía | Regla 50/50 | Repartos libres por iniciativa | Las monedas de una iniciativa se reparten siempre en partes iguales entre los involucrados | normal | aplicado |
| 2026-07-03T21:39:39 | Alejandro | Tablero | Columna nueva | — | Intervención conductual: descripción de la palanca de comportamiento de cada iniciativa | normal | aplicado |
| 2026-07-03T21:39:39 | Beholder | Alerta | Código rojo | — | 🚨 Stefanie pico 11 monedas simultáneas (09-17/07); acción propuesta: mover Q-23 al 21/07, pendiente de aprobación del owner | normal | aplicado |
| 2026-07-03T21:39:39 | Alejandro | Skill | Beholder v1.4.0 | Riesgos con severidad simple | Dimensionamiento probabilidad × impacto + códigos de alerta amarillo/rojo con disparadores y protocolo | normal | aplicado |
| 2026-07-03T21:23:23 | Alejandro | Tablero | Otros perfiles | Service Designer / Equipo de Product Designers | Service Design / Product Design; Q-28 pasa a Service Design | normal | aplicado |
| 2026-07-03T21:23:23 | Alejandro | Q-11 | Estado | Backlog (Plantillas primer contacto sin CUA, Felipe 2 🪙) | Eliminado del tablero | normal | aplicado |
| 2026-07-03T21:08:12 | Alejandro | Tablero | Formato monedas | Total + desglose: 4 🪙 (A:2 · F:2) | Una cifra por persona: 2 🪙 2 🪙 (orden de la columna BDs) | normal | aplicado |
| 2026-07-03T21:08:12 | Alejandro | Tablero | Columna nueva | — | Otros perfiles: Service Designer en todo excepto EPS/Backlog/Arquitectura; Product Designers solo en Q-38 | normal | aplicado |
| 2026-07-03T20:36:32 | Alejandro | Tablero | Columnas nuevas | Fechas dentro del status | Columnas fijas 'Fecha de inicio' y 'Fecha de cierre' en todas las tablas (skill v1.3.0) | normal | aplicado |
| 2026-07-03T20:22:27 | Alejandro | EPIC-2 | Épica | Guías resumidas y AMI Relanzamiento separadas (typo) | Fusionadas: AMI Relanzamiento contiene las guías resumidas (Q-16–Q-18); placeholder Q-19 eliminado | normal | aplicado |
| 2026-07-03T20:18:14 | Alejandro | EPIC-5 | Épica nueva | — | Spark: Vivo Pack (3 iniciativas; Stefanie, Melissa, Alejandro) | normal | aplicado |
| 2026-07-03T20:18:14 | Alejandro | EPIC-7 | Convenios | Backlog sin iniciativas | Activo: 3 iniciativas con fechas (20/07 → 21/08) | normal | aplicado |
| 2026-07-03T20:18:14 | Alejandro | EPIC-6 | Bienestar 360 | Done | Reabierto: status + seguimiento hasta 17/07 | normal | aplicado |
| 2026-07-03T20:18:14 | Alejandro | Q-38 | Ecosistema entendimiento | EPIC-2 Guías; Stef, Felipe, Alejandro | EPIC-8 Renovación EPS; Alejandro:2, Felipe:2 | normal | aplicado |
| 2026-07-03T20:18:01 | Alejandro | Tablero | Reestructura v2 | 22 quests / 10 épicas (roadmap) | 47 quests: épicas = proyectos BD, quests = iniciativas de la tabla final; claves renumeradas | normal | aplicado |
| 2026-07-03T20:18:01 | Alejandro | Economía | Fichas → Monedas | 8/10 fichas comprometidas por persona | Monedas = esfuerzo del trimestre; regla: máx. 8 simultáneas por persona | normal | aplicado |
| 2026-07-03T20:18:01 | Alejandro | Loyalty | Estado | In Progress (piloto/MVP) | Eliminado del tablero | normal | aplicado |
| 2026-07-03T20:18:01 | Alejandro | Todas | Fechas inicio/entrega | sin fechas | Fechas cargadas desde tabla final de iniciativas | fecha | aprobada |
| 2026-07-02T21:24:39 | Alejandro | Q-3 | Status del proyecto | Top 4 cuentas: 2/4 entregadas, 2/4 en revisión; ajustes y presentación final | Dra. Ana Gabriela Ramos (Dir. Médica Seguros Salud) ha escrito para revisar las guías para empresas | normal | aplicado |
| 2026-07-02T21:14:39 | Alejandro | Q-5 | Quest / Status | Mensajes de primer contacto; solo no clientes sin CUA | Estrategia de primer contacto; incluye clientes y no clientes con CUA, y no clientes sin CUA | normal | aplicado |
| 2026-07-02T21:08:38 | Alejandro | Q-7 | Status del proyecto | Asistencia a onboarding de FFVV actual; contenido listo, falta diseño instruccional | Modelo por competencias: calendarización, evaluación y reconocimientos | normal | aplicado |
| 2026-07-02T21:07:01 | Alejandro | Q-9 | Quest / Impacto | Kit de Social Selling; +leads/agendamientos; 15–25% conversión lead→cita | Playbook de Ventas FFVV Vida Individual; ↓ curva de aprendizaje del asesor; +conversión de venta | normal | aplicado |
| 2026-07-02T20:59:57 | Alejandro | Q-28 | Quest nuevo | — | Complemento digital para entendimiento y uso eficiente de seguros (In Progress, EPIC-2 Guías resumidas) | normal | aplicado |
| 2026-07-02T20:51:32 | Alejandro | Q-5 | Status del proyecto | Estrategia de primer contacto alineado a CUA (en definición → desbloqueándose) | Mesa con Legal, Cumplimiento, CUA y FFVV para definir estrategia viable de contacto a no clientes sin CUA | normal | aplicado |
| 2026-07-02T20:48:42 | Alejandro | Q-1 | Status del proyecto | Agencia devolvió 1ª guía diagramada (50%) | Planes AMI diseñados; pendiente check de Producto y equipo médico | normal | aplicado |
| 2026-07-02T20:48:42 | Alejandro | Q-4 | Status del proyecto | quick fix correo de conciliación (35%) | Priorizar conciliación facturas corporativas/gran empresa; sigue diseño nueva experiencia | normal | aplicado |
| 2026-07-02T20:41:34 | Alejandro | Q-16 | Estado | In Progress | Eliminado del tablero | normal | aplicado |
| 2026-07-02T20:41:33 | Alejandro | Q-20 | Estado | In Progress | Eliminado del tablero | normal | aplicado |
| 2026-07-02T20:41:32 | Alejandro | Q-19 | Estado | In Progress | Eliminado del tablero | normal | aplicado |
| 2026-07-02T20:41:31 | Alejandro | Q-27 | Estado | Backlog | Eliminado del tablero | normal | aplicado |
| 2026-06-25T13:56:51 | Alejandro | Q-1 | % Avance / Status | Diseño 1/4 (40%) | Agencia devolvió 1ª guía diagramada (50%) | normal | aplicado |
| 2026-06-25T13:56:51 | Stefanie | Q-10 | Status | cierre de playbook pendiente | playbook B360 entregado | normal | aplicado |
| 2026-06-25T13:56:51 | Stefanie | Q-4 | Status / Impacto | research 20% | quick fix correo de conciliación (35%) | normal | aplicado |
| 2026-06-25T02:40:54 | Stefanie | Q-27 | Quest nuevo | — | Emisión de póliza (Backlog, EPIC-4 Cobranzas) | normal | aplicado |
| 2026-06-23T21:56:31 | Stefanie | Stef | Fichas comprometidas | 11 (⛔ Inválido) | 8 (🟢 Óptimo) | normal | aplicado |
| 2026-06-23T21:56:27 | Stefanie | Q-1 | Behavioral designers | Stef, Felipe, Alejandro | Felipe, Alejandro | normal | aplicado |
| 2026-06-23T21:56:27 | Stefanie | Q-1 | Fichas | 8 | 5 | normal | aplicado |
| 2026-06-23T21:49:10 | Alejandro | Q-17/Q-18 | Iniciativa (matriz) | presentes (26) | retiradas (24) | normal | aplicado |
| 2026-06-23T21:24:22 | Stef | Q-17 | Estado | In Progress | Eliminado del tablero | normal | aplicado |
| 2026-06-23T21:24:22 | Stef | Q-18 | Estado | In Progress | Eliminado del tablero | normal | aplicado |
| 2026-06-23T13:48:08 | Alejandro | Q-3 | Estado | Done | In Review | normal | aplicado |
| 2026-06-23T13:48:08 | Alejandro | Q-6 | Equipo Behavioral Design | Alejandro | Meli, Alejandro | normal | aplicado |
