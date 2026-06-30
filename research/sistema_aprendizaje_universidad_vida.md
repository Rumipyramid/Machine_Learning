# 🎓 Sistema de aprendizaje para asesores — "Universidad Vida"

> Diseño de un sistema de aprendizaje para formar asesores de Vida Individual
> (egresados recién contratados), basado en lo **mejor respaldado por la ciencia
> del aprendizaje y la conductual**. Acota frameworks populares sin evidencia.
> Derivado de investigación `/seeker` (2026-06-30). Fuentes: F-26 a F-34 en
> `research/fuentes/registro_fuentes.md`. Se ancla al modelo de venta de 4 pasos
> (ver `research/revision_conductual_modelo_venta.md`).

## El problema, bien diagnosticado

La experiencia de aprendizaje está **fragmentada** (materiales, capacitaciones y
onboarding no conversan) y **sin seguimiento** (se capacita, pero no se sabe si
aprenden ni si aplican). Agregar evaluaciones + calendario + recompensas es
necesario, pero **insuficiente por sí solo**, y una de esas piezas mal ejecutada
(recompensas) puede ser contraproducente.

El problema de fondo son **dos cosas**:

1. **Coherencia** → se resuelve con un **modelo de competencias** único que ordene
   todo lo que ya existe en Universidad Vida.
2. **Transferencia** (que lo aprendido se aplique en el puesto) → y aquí está el
   hallazgo central: **lo que más predice la aplicación NO es la capacitación, es el
   entorno posterior, sobre todo el jefe directo.** El clima de transferencia
   (r≈.27) y el apoyo social (r≈.21) son los predictores más fuertes; y para una
   venta consultiva —una *open skill*— ese factor pesa **más** que para habilidades
   cerradas (Blume et al., 2010).

> **Implicación de diseño:** el sistema debe construirse alrededor de la
> transferencia y la coherencia, no alrededor de los contenidos. Si se agregan las
> tres piezas pero no se diseña el rol del líder/coach y la oportunidad de aplicar,
> se reproduce el mismo fracaso con mejor tablero.

---

## Arquitectura: 5 capas

### Capa 0 · Columna vertebral: modelo de competencias

Antes que calendario o evaluaciones, definir **qué sabe y qué hace** un buen asesor,
atado al perfilador de 4 pasos (motivaciones → dimensionamiento → perfil financiero
→ propuesta).

- Redactar el **modelo de competencias** (conocimiento + conducta observable por
  paso del modelo de venta).
- **Mapear todo el contenido actual de Universidad Vida** contra esas competencias:
  revela solapes, vacíos y la secuencia correcta.
- Definir **una sola ruta de aprendiz** (onboarding → fundamentos → práctica aplicada
  → certificación → desarrollo continuo) que referencie ese mapa.

Esto es lo que hace que onboarding, materiales y capacitaciones dejen de estar
fragmentados: todos apuntan al mismo mapa. Sin esta capa, el resto son parches.

### Capa 1 · Calendario: espaciado y por cohortes

- **Cohortes de ingreso** (encaja con contratar tandas de egresados): habilita
  aprendizaje entre pares y socialización temprana.
- **Distribuir en el tiempo, no concentrar.** El *spacing effect* es de los hallazgos
  más robustos del campo: el mismo contenido distribuido en semanas se retiene mucho
  más que un bootcamp intensivo (Cepeda et al., 2006). Un curso concentrado se olvida.
- **Intercalar** producto con conversación de venta, en ciclos cortos:
  *aprende → practica → aplica con cliente real → reflexiona → siguiente*.
- **Onboarding las primeras semanas** centrado en conexión y claridad de rol
  (mentor/buddy, expectativas explícitas), no solo en contenido: la adaptación
  temprana del recién ingresado predice retención y desempeño (investigación de
  socialización organizacional, Bauer, 2010).

### Capa 2 · Evaluaciones: dos funciones distintas

**(a) Evaluación COMO aprendizaje (formativa).** Quizzes frecuentes, de baja apuesta
y **espaciados**: el acto de recuperar de memoria *es* lo que fija el aprendizaje
(*testing effect*, g≈0.61 frente a solo releer; Adesope et al., 2017). Formatos
mixtos (opción múltiple + respuesta corta) rinden más.

**(b) Compuertas de maestría (competency-based).** Avanzar por **demostrar la
competencia**, no por horas-asiento. No se pasa a "cotización" sin dominar
"perfilamiento".

**(c) Medir la APLICACIÓN en el puesto (Nivel 3) — la pieza que hoy falta.** No
asumir que "le gustó" o "aprobó el quiz" significa "lo aplica": los niveles de
Kirkpatrick **no están causalmente encadenados ni correlacionan** entre sí (Alliger
& Janak, 1989); la satisfacción con el curso casi no predice el desempeño en el
puesto. Medir la conducta directamente:

- role-plays grabados contra rúbrica,
- escucha de llamadas / revisión de grabaciones,
- acompañamientos (ride-alongs),
- checklist del jefe sobre si efectivamente corre los 4 pasos.

Ese es el **indicador adelantado** real de que la formación funciona.

**Cuidado con el feedback.** Mejora el desempeño en promedio (d≈0.41) **pero ~1 de
cada 3 intervenciones lo empeora** —sobre todo cuando apunta a la persona ("eres
bueno/malo") en vez de a la tarea (Kluger & DeNisi, 1996). Hay que **entrenar a los
coaches** para dar feedback específico contra la rúbrica, no juicios al ego.

### Capa 3 · Crecimiento / recompensa: escalera de competencias, no puntos

- **El motivador más fuerte y seguro es una carrera por niveles visible y con
  consecuencias reales:** *Asesor en formación → Certificado → Senior → Mentor*, cada
  nivel con criterios claros y beneficios reales (mejores leads, autonomía,
  compensación). Activa **competencia y autonomía** (Teoría de la Autodeterminación)
  sin los riesgos de los premios.
- **Ojo con las recompensas extrínsecas.** Premios tangibles, esperados y
  contingentes al desempeño **socavan la motivación intrínseca** (d≈ −0.28 a −0.40;
  Deci, Koestner & Ryan, 1999). Si "aprender" se vuelve "ganar puntos/premios", se
  erosiona el interés genuino. Usar recompensas para tareas genuinamente aburridas de
  compliance; usar **reconocimiento** para la maestría.
- **Si se gamifica, con cuidado.** El efecto es **pequeño** y, para resultados
  motivacionales/conductuales, **inestable** (cognitivo g≈0.49, motivacional g≈0.36,
  conductual g≈0.25; Sailer & Homner, 2020). Ayuda: narrativa y **combinar competencia
  con colaboración** (metas de cohorte). Falla: rankings puros (desmotivan al fondo de
  la tabla).

### Capa 4 · El líder como reforzador (la capa que casi todos olvidan)

Dado que el clima de transferencia y el apoyo social son los predictores #1 (Blume
et al., 2010), el sistema debe **diseñar explícitamente el rol del jefe**:

- cadencia de coaching 1:1 con el asesor en formación,
- **crear oportunidades de aplicar de inmediato** lo recién visto,
- reforzar la conducta correcta contra la rúbrica.

La responsabilidad del jefe sobre la transferencia debe ser **parte del sistema**
(con sus propios indicadores), no un extra opcional.

### Capa 5 · Medir si el sistema funciona (no asumirlo)

- **Indicadores adelantados:** tasa de maestría, puntajes de role-play, % de
  aplicación observada en llamadas.
- **Indicadores rezagados:** tiempo a productividad (ramp), ventas tempranas por
  tenencia, **retención de asesores**.
- Donde se pueda, **comparar cohortes** (piloto vs. control). El error clásico de L&D
  es declarar éxito por "asistencia y satisfacción".

---

## Lo respaldado vs. lo que NO hay que forzar

| Usar (respaldado) | Evitar / no forzar |
|---|---|
| Espaciamiento + recuperación (quizzes) como motor (Cepeda 2006; Adesope 2017) | **70-20-10** como arquitectura: cifras inventadas, sin base empírica; viene de autorreporte retrospectivo de ejecutivos (origen Lombardo & Eichinger; crítica Kajewski & Madsen 2012) |
| Medir **conducta en el puesto** (Nivel 3) | Tratar **Kirkpatrick** como cadena causal o usar reacción/quiz como proxy de aplicación (Alliger & Janak 1989) |
| **Clima de transferencia + coaching del jefe** como palanca central (Blume 2010) | **Estilos de aprendizaje** ("visual/auditivo"): mito sin evidencia (Pashler et al. 2008) — no segmentar por ahí |
| **Escalera de competencias** (autonomía/competencia, SDT) | **Gamificación ingenua** (puntos/rankings) como motor motivacional (Sailer & Homner 2020) |
| Feedback **enfocado en la tarea**, contra rúbrica | Recompensas extrínsecas que erosionan el interés (Deci et al. 1999); feedback al ego (Kluger & DeNisi 1996) |

---

## Nota de rigor (honestidad epistémica)

La mayoría de estos hallazgos provienen de educación y formación corporativa general;
**hay menos RCTs específicos de fuerza de ventas de seguros**. Los effect sizes son
trasladables con prudencia, no garantías. Los más sólidos y trasladables:
espaciamiento, recuperación, clima de transferencia y el riesgo de las recompensas
extrínsecas. El más "blando": la magnitud exacta de la gamificación. Por eso la
Capa 5 (medir el propio sistema) no es opcional.

---

## Siguientes artefactos posibles

- **Mapa de competencias** del asesor, atado a los 4 pasos del perfilador.
- **Calendario de cohorte espaciado** de ejemplo (p. ej., 12 semanas).
- **Rúbrica de role-play / escucha de llamadas** (instrumento de Nivel 3).
- **Modelo de coaching del líder** (cadencia + guía de feedback task-focused).

---

*Fuentes registradas en `research/fuentes/registro_fuentes.md` (F-26 a F-34).
Diseño bajo protocolo `/seeker`, 2026-06-30.*
