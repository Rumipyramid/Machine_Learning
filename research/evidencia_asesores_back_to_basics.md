# Evidencia primaria de asesores — Back to Basics (Q3 2026)

Registro de dos piezas de evidencia primaria recolectadas por el equipo, usadas para calibrar el
backlog de Back to Basics (`TABLERO_BEHOLDER.md`, EPIC-1) y la presentación del proyecto
(`reportes/presentacion_back_to_basics.md`).

## 1. Encuesta a asesores sobre herramientas (n=19)

Encuesta mixta (cuantitativa + abierta) a 19 asesores de la FFVV sobre las herramientas que usan
en su día a día. Archivo fuente: `Herramientas_para_asesores119.xlsx`.

### Uso de herramientas (frecuencia auto-reportada)
| Herramienta | "Siempre" | "Nunca" | Lectura |
|---|---|---|---|
| Salesforce | 16/19 | 0/19 | Herramienta troncal, uso casi universal |
| WhatsApp | 14/19 | 0/19 | Canal de contacto dominante |
| Email | 11/19 | 0/19 | Uso alto, más variable que Salesforce/WhatsApp |
| AIDA | 7/19 | 1/19 | Uso alto pero con **quejas de calidad de información** (ver abajo) |
| Excel | 10/19 | 1/19 | Uso alto — varios asesores arman sus propias tablas cuando otra herramienta falla |
| Cartillas de producto | 4/19 | 4/19 | Uso mixto |
| CartaPlan | 1/19 | **7/19** | Adopción baja — mayoría "nunca" o "rara vez" |
| Ticker | 1/19 | **9/19** | Adopción muy baja — mayoría "nunca" o "rara vez" |

### Satisfacción general
- Promedio de "cuánto te ayudan las herramientas de RIMAC" (escala 0–10): **8.05/10** — alto en
  el agregado.
- **Paradoja de la satisfacción agregada**: el promedio alto convive con fricciones concretas y
  repetidas en las respuestas abiertas — el mismo patrón que ya documenta el proyecto en otros
  frentes (una cifra agregada satisfactoria no implica ausencia de dolor específico y accionable).
- Ayuda de las herramientas para que el cliente entienda el producto: 8/19 "bastante", 8/19
  "regular", 3/19 "poco".
- Ayuda de las herramientas para manejar objeciones y persuadir: 6/19 "bastante", 9/19 "regular",
  4/19 "poco" — **peor calificada que la comprensión de producto**, consistente con el hallazgo
  de abajo.

### El hallazgo más accionable: manejo de objeciones + cierre son el mismo dolor
- **Tema de capacitación más pedido**: "Manejo de objeciones" — 8/19 (42%), muy por encima de
  "Conocimiento de producto" (4/19) y "Conocimiento de los clientes" (4/19).
- **Momento de la venta donde piden más apoyo**: "cierre" (o variantes: "al cierre", "en el
  cierre", "momento del cierre") — ~7-8/19 (~40%) de las respuestas abiertas. El resto se reparte
  entre objeciones, prospección e "siempre".
- **Lectura conjunta**: el asesor no pide más información de producto — pide ayuda para manejar
  la conversación en el momento en que el cliente objeta, justo antes de cerrar. Es un problema de
  habilidad conversacional, no de conocimiento declarativo.

### Herramienta que más se pide mejorar (empate a 4/19 cada una)
- **AIDA** — con motivo explícito y repetido: *"no da la información adecuada y se equivoca con
  otro producto"*, *"no brinda información correcta"*, *"no contesta bien casi nunca"*, *"no tiene
  toda lo necesario para nuestra gestión"*. Evidencia concreta que respalda directamente el
  backlog de evolucionar AIDA de piloto a herramienta funcional (ver EPIC-1 del tablero).
- **Recursos visuales** (cartillas, flyers) — piden brochures digitales y plantillas listas,
  algunos mencionan que hoy tienen que crear sus propios materiales.
- **Cotizador** — piden poder usarlo sin registro/autorización previa y con más ejemplos.

### Otros hallazgos con valor de diagnóstico
- Un asesor señala explícitamente una falla de onboarding: *"no enseñan bien a usar el salesforce
  en las capacitaciones del inicio... tenemos que aprender en marcha"* — evidencia directa para
  reforzar Universidad Vida — Onboarding.
- Varios asesores mencionan usar herramientas no oficiales (ChatGPT, Gemini) para compensar
  huecos de AIDA o del cotizador — señal de que la necesidad ya se resuelve informalmente cuando
  la herramienta oficial no alcanza.

## 2. Taller de Manejo de Objeciones (CoE Experience Design) — resultados completos

Taller orientado a fortalecer las capacidades de gestión de objeciones en la interacción con
clientes, reportado por CoE Experience Design.

### Métricas
| Indicador | Resultado |
|---|---|
| Satisfacción con el contenido | 99.33% |
| Desempeño del speaker | 98.67% |
| NPS (recomendación) | **96.67** |
| Asistencia | 83.33% (30 de 36 invitados) |

### Qué generó el valor (drivers)
1. **Aprendizaje basado en casuística real** — principal driver de valor; facilita la aplicación
   directa en la gestión con clientes.
2. **Uso de Copilot como herramienta diferenciadora** — potencia la calidad de las respuestas y
   la creatividad en el manejo de objeciones. **Casi con certeza es AIDA** (el "copiloto" de IA
   que el equipo co-diseñó en Q-13, con el mismo patrón de role-play + feedback + puntaje) — el
   nombre "Copilot" en el reporte de CoE Experience Design probablemente es coloquial, no el
   producto de Microsoft.
3. **Metodología práctica y dinámica** — interacción, práctica y feedback fortalecen habilidades
   críticas del rol.

### Oportunidades de mejora identificadas
1. Ampliar la práctica y diversidad de casos: incorporar role play, videos y más escenarios.
2. Ajustar el uso de Copilot/AIDA: mejorar la consistencia en evaluaciones y el alineamiento con
   lineamientos internos — **el mismo problema de calidad de información que ya reportan los
   asesores en la encuesta de arriba** (AIDA "da respuestas equivocadas", "no brinda información
   correcta"). Dos fuentes independientes apuntando al mismo defecto concreto.
3. Optimizar logística: duración, horarios y espacios dedicados a práctica.

### Relación con el tablero
- El tema (manejo de objeciones), el mecanismo (role-play + feedback + IA) y el hallazgo de
  calidad de información de la IA coinciden con **Q-13 (Co-diseño AIDA Skill Trainer)** en tres
  puntos independientes — la evidencia para que sea el mismo piloto (o su primera corrida real)
  es ahora fuerte, no solo una coincidencia temática. Sigue pendiente confirmar con el equipo si
  se fusiona el registro de Q-69 dentro de Q-13 o se mantienen separados (el taller lo organizó
  CoE Experience Design, no está claro si fue 100% el mismo entregable o una ejecución conjunta).
- La oportunidad de mejora #2 (consistencia de Copilot/AIDA) es el mismo hallazgo que ya
  respalda Q-64 (AIDA: de piloto a herramienta funcional) — ahora con evidencia de una ejecución
  real, no solo de la encuesta.

## Cómo se usa esta evidencia

- Registrada como quests `Done` en `TABLERO_BEHOLDER.md` (EPIC-1) para trazabilidad de impacto.
- Respalda directamente 3 iniciativas ya en el backlog: evolución de AIDA (mejorar calidad de
  información), potenciamiento del entrenamiento (manejo de objeciones como tema prioritario) y
  materiales visuales/transversalización (recursos visuales pedidos).
- No es evidencia externa citable (no aplica la rúbrica A–E del ledger de `cronista`) — es
  investigación primaria propia del equipo, registrada aquí como conocimiento del proyecto.
