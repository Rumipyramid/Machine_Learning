---
name: constructor-programa-academico
description: Diseña la estructura de un programa de formación para fuerza de ventas — desde un onboarding de 25 días hasta un taller táctico de 2 horas. Define qué bloques van, en qué orden, con qué duración, dónde ubicar checkpoints de mentoría, qué mecánicas de gamificación aplicar, y cómo evaluar si funcionó. No produce el contenido final de cada bloque (para eso usar material-capacitacion-ffvv una vez que la estructura está definida). Úsalo cuando la estructura del programa no esté ya decidida y haya que construirla desde cero.
---

# Constructor de Programa Académico

Decide el esqueleto de un programa de formación (desde un onboarding largo hasta un taller táctico de 2 horas): secuencia de bloques, checkpoints de mentoría, mecánicas de gamificación, y estrategia de evaluación. Es el paso previo a material-capacitacion-ffvv, que llena cada bloque ya definido con contenido real.

No usar este skill si la estructura ya está decidida (ej. si el usuario ya trae una lista de secciones armada) — en ese caso ir directo a material-capacitacion-ffvv para producir el contenido.

## Paso 0 — Investigación previa (antes de estructurar)

No construir la estructura solo con lógica propia — reunir respaldo de tres tipos, en este orden de esfuerzo:

1. **Data interna de onboardings anteriores** — preguntar explícitamente al usuario si tiene esta información disponible (qué bloques funcionaron, dónde hubo deserción o quejas, feedback de mentores previos) antes de asumir que no existe. Si el usuario confirma que no tiene o no sabe, continuar sin ella y decirlo explícito — no inventar un hallazgo interno.
2. **Evidencia académica sobre secuenciación instruccional** — apalancarse del skill `seeker` para esto: pasarle el claim específico sobre secuenciación (ej. "¿está validado que el orden conocimiento→habilidad→comportamiento mejora la retención en programas de formación laboral?") y usar su cruce de registro empírico + teórico como respaldo, en vez de reconstruir esa investigación dentro de este skill. Instrucción: consultar el skill ubicado en `.claude/skills/seeker/SKILL.md` y seguir su metodología completa para el claim que se necesite validar.
3. **Benchmarking de estructuras de onboarding en seguros/ventas** — buscar mejores prácticas de onboarding sin limitarse a Perú o LatAm; incluir aseguradoras y empresas de venta consultiva de cualquier país. Tratar como referencia, no como plantilla a copiar — el objetivo global del programa (Paso 1) manda sobre lo que hacen otros.

Si no hay tiempo o no aplica investigar a fondo para una estructura pequeña o iterativa, se puede saltar este paso — pero si se salta, decirlo explícito ("estructura basada en criterio del skill, sin benchmarking ni evidencia externa validada") para que quede claro que no tiene ese respaldo.

## Paso 1 — Definir los parámetros base

Antes de diseñar la secuencia, confirmar (preguntar si no está claro):
1. **Escala del programa** — no asumir que siempre son semanas o días. Puede ser un programa largo (15, 25, 30 días), un taller de un día, o una capacitación táctica de 2 horas. La escala cambia todo: un onboarding de 25 días tiene secuenciación por dependencia de contenido; un taller de 2 horas tiene un solo objetivo y va directo. Preguntar si no es evidente.
2. **Objetivo global del programa** — qué debe poder hacer el asesor al terminar (no solo qué debe saber).
3. **Público** — nuevo ingreso sin experiencia previa vs. asesor con experiencia en otro ramo (cambia cuánto tiempo dedicar a fundamentos vs. especialización).
4. **Contenido previo que ya existe** — preguntar explícitamente si hay capas que el participante ya cubrió en otro programa o que no aplican para esta capacitación específica. No asumir que siempre se empieza desde cero — en capacitaciones tácticas es común que los fundamentos ya estén cubiertos y se entre directo a un nivel específico.

## Paso 2 — Clasificar los bloques temáticos por objetivo

Igual que en material-capacitacion-ffvv, cada bloque temático (no el programa completo) se clasifica como:
- **Conocimiento** — normativa, producto, procesos.
- **Habilidad** — manejo de objeciones, discurso de venta, uso de herramientas.
- **Comportamiento** — hábitos sostenidos (ej. reportar actividad diaria, seguir protocolo de seguimiento).

Listar todos los bloques temáticos que debe cubrir el programa antes de ordenarlos.

## Paso 3 — Secuenciar en el eje temporal

Reglas de secuenciación — aplicar con flexibilidad según la escala del programa (Paso 1). En una capacitación táctica de 2 horas, varias de estas reglas no aplican; en un onboarding de 25 días, todas son relevantes:

1. **Dependencia de contenido (solo cuando aplica)** — un bloque de Habilidad que requiere conocimiento previo (ej. no se puede practicar manejo de objeciones de un producto que aún no se explicó) va después de su bloque de Conocimiento correspondiente. Pero si el contenido previo ya fue cubierto en otro programa o el participante ya lo domina (ver Paso 1, punto 4), la dependencia no existe y se puede entrar directo.
2. **Carga cognitiva decreciente al inicio** — en programas largos, los primeros días priorizan bloques de Conocimiento fundamental (lo que todo lo demás necesita), no todo mezclado desde el día 1. En capacitaciones tácticas cortas, este criterio no aplica — se va directo al objetivo.
3. **Bloques de Comportamiento al final o distribuidos, nunca al inicio** — un hábito no se instala antes de que exista la habilidad o el conocimiento que ese hábito debe sostener.
4. **Práctica transversal, no solo al cierre** — la práctica integrada (aplicar varios bloques juntos en un caso real) no se reserva solo para los últimos días. Distribuir momentos de práctica a lo largo del programa, especialmente después de bloques de Habilidad. El cierre sí debe incluir una práctica integradora final, pero no debe ser la única.

Si dos bloques no tienen dependencia clara entre sí, el orden es flexible — no forzar una secuencia rígida donde no la hay.

## Paso 4 — Ubicar checkpoints de mentoría

Los checkpoints de mentor no van a intervalos fijos automáticos (ej. "cada 5 días") — se ubican según la función que cumplen en ese punto del programa:

- **Después de un bloque de Habilidad** — el mentor da feedback sobre la práctica (ej. escuchar un roleplay grabado), no solo confirma que el contenido se vio.
- **Antes de un bloque de Comportamiento** — el mentor ayuda a plantear el compromiso o meta concreta que se espera sostener, para que el asesor no llegue al bloque sin haberlo procesado con alguien.
- **Al cierre de cada semana o tercio del programa** — checkpoint de consolidación general, para detectar si algo no está calzando antes de seguir avanzando.

Proponer la ubicación de checkpoints como parte de la estructura, no como una capa aparte que se agrega al final.

## Paso 5 — Gamificación (mecánicas de Octalysis en la estructura)

No es una capa decorativa que se agrega al final ("ponle puntos y badges") — las mecánicas de gamificación deben estar integradas en la estructura desde el diseño, conectadas al objetivo de cada bloque:

- **Bloques de Conocimiento** → mecánicas de progreso y descubrimiento (Core Drive 7: Unpredictability; Core Drive 2: Development & Accomplishment) — ej. desbloquear el siguiente nivel/módulo, quiz con feedback inmediato.
- **Bloques de Habilidad** → mecánicas de reto y feedback social (Core Drive 5: Social Influence; Core Drive 3: Empowerment) — ej. reto entre pares, roleplay evaluado por compañeros.
- **Bloques de Comportamiento** → mecánicas de compromiso y consistencia (Core Drive 4: Ownership; Core Drive 6: Scarcity) — ej. streak de días aplicando el hábito, compromiso público con el mentor.

En capacitaciones tácticas cortas (2 horas, taller de un día), la gamificación puede reducirse a una sola mecánica simple o no aplicar. No forzarla si la escala no la justifica.

## Paso 6 — Evaluación (cómo saber si el programa funcionó)

Definir antes de producir contenido — no como un paso final después de que todo está armado. La evaluación debe responder a tres niveles distintos:

1. **¿Se completó?** — métricas de asistencia/finalización. Necesario pero insuficiente por sí solo.
2. **¿Se aprendió?** — vinculado al tipo de objetivo de cada bloque:
   - Conocimiento → checkpoint de autoevaluación o quiz (ya cubierto en material-capacitacion-ffvv).
   - Habilidad → rúbrica de evaluación sobre práctica real (roleplay evaluado, caso resuelto).
   - Comportamiento → observación sostenida en el tiempo (no se puede medir en un solo momento).
3. **¿Generó impacto?** — indicadores que conectan el programa con resultados reales (ej. tasa de conversión, retención de clientes, tiempo a primera venta). Este nivel requiere definir el indicador y el baseline antes de arrancar el programa, no después.

Si no hay baseline disponible, decirlo explícito y proponer cómo establecerlo como parte del programa (ej. medir el indicador en la primera semana antes de la intervención).

## Output

Un esqueleto en texto plano: lista de bloques en orden, con su objetivo clasificado (conocimiento/habilidad/comportamiento), duración estimada, checkpoints de mentoría ubicados con su función explícita, mecánicas de gamificación propuestas por bloque, y estrategia de evaluación con sus tres niveles (completitud, aprendizaje, impacto). No contenido desarrollado — eso se produce después, bloque por bloque, con material-capacitacion-ffvv.

## Restricción

No producir el contenido de ningún bloque dentro de este skill, aunque sea tentador adelantarlo. Cerrar primero la estructura completa, validarla con el usuario, y solo después pasar a producir contenido con el otro skill.
