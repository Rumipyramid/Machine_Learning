# Curso introductorio: Diseño conductual hoy

> Output de `research/_outputs/`. Currícula para un curso de 6 sesiones que el equipo de diseño conductual podría
> dictar. Construido sobre los nodes `behavioral-design-estado-disciplina`, `conducta-humano-ia`,
> `convergencia-psicologia-economia-ia`, `fenomenos-psicologicos` y `evaluacion-calidad-agentes-conversacionales-ia`.
> Las lecturas citan el registro de fuentes del proyecto (`research/fuentes/codice.md`) con su ID. Fecha: 2026-11-09.

## En una frase

Un curso para aprender a diseñar las condiciones que facilitan o frenan una conducta, y a medir si de verdad
cambiaron, en un mundo donde el nudge aislado perdió fuerza y la IA ya es parte del entorno.

## Para quién

- Diseñadores de producto, servicio y UX, investigadores, analistas y equipos de negocio que quieran usar ciencia
  del comportamiento en su trabajo.
- No requiere formación previa en psicología ni en estadística.

## Formato

- **6 sesiones de 2 horas** (12 horas en total), una por semana. Puede comprimirse en dos jornadas de 6 horas.
- **Cada sesión:** 40 minutos de exposición, 60 de taller sobre un caso y 20 de cierre con una pregunta para la
  semana.
- **Grupo:** 15 a 25 personas, en equipos de 4 o 5 que trabajan el mismo proyecto todo el curso.
- **Proyecto del curso:** cada equipo elige una conducta real de su trabajo y llega a la sesión 6 con un
  diagnóstico, una intervención y un plan de prueba.

## Qué sabrá hacer quien lo termine

1. Explicar qué murió del diseño conductual (la promesa de cambiar conductas con un mensaje) y qué sigue vivo.
2. Describir una conducta en sus seis capas: el acto, la mente, lo social, los objetos, las reglas y los algoritmos.
3. Diagnosticar por qué una conducta no ocurre, con un marco explícito.
4. Decidir dónde quitar fricción y dónde ponerla, y a quién sirve cada decisión.
5. Diseñar una prueba con grupo de control y un indicador declarado antes.
6. Reconocer cómo la IA cambia la conducta de las personas, y cuándo una simulación con IA sirve y cuándo no.

---

## Sesión 1 · Qué murió y qué vive

**Idea central:** el efecto promedio del nudge publicado estaba inflado; la disciplina no murió, se mudó al
experimento propio, al diseño del sistema y a la IA.

- **Contenido**
  - De dónde viene: la arquitectura de la elección y el nudge (Thaler y Sunstein, 2008, F-860).
  - La crisis: corregido el sesgo de publicación, el efecto promedio cae a casi cero (Maier y otros, 2022, F-17;
    Hu y otros, 2025, F-18). A escala, las unidades de nudge de gobierno logran unos 1,4 puntos frente a 8,7 en los
    papers (DellaVigna y Linos, 2022, F-21).
  - La integridad: el caso de datos fabricados en el estudio de honestidad que usaron aseguradoras (Bazerman, 2025,
    F-24).
  - Lo que vive: del individuo al sistema (Chater y Loewenstein, 2022, F-19), del empujón a la capacidad de decidir
    (Hertwig y Grüne-Yanoff, 2017, F-857) y una agenda para el campo (Hallsworth, 2023, F-859).
- **Taller:** cada equipo trae una "intervención conductual" que conozca y la clasifica: ¿cambia un mensaje, una
  estructura o una capacidad? ¿Se midió? ¿Contra qué?
- **Pregunta para la semana:** ¿qué conducta de tu trabajo te gustaría entender mejor? (será el proyecto del curso).

## Sesión 2 · Cómo ver la conducta

**Idea central:** un clic es el final visible de una decisión que empezó antes, en lo que la persona cree, en quién
la rodea y en las reglas que la limitan.

- **Contenido**
  - Las seis capas de la conducta: acto, mente, lo social, los objetos, las reglas y los algoritmos. Cualquier agente
    en el centro: persona, máquina o animal.
  - Trayectorias, no momentos: la conducta cambia, se apaga, vuelve y se resiste.
  - Fricción: quitarla donde estorba y ponerla donde protege. La que sobra se llama "sludge" (Sunstein, 2020, F-858).
  - Qué sobrevive a la replicación: estado de los efectos clásicos (anclaje, encuadre, aversión a la pérdida, priming)
    antes de apoyar una decisión en ellos (node `fenomenos-psicologicos`).
- **Taller:** mapear la conducta del proyecto en las seis capas. ¿En qué capa intervendríamos hoy por costumbre?
  ¿En cuál está el problema?
- **Pregunta para la semana:** ¿qué fricción de tu servicio protege a la persona y cuál solo protege a la empresa?

## Sesión 3 · Diagnosticar antes de diseñar

**Idea central:** todo pedido recibe primero una exploración del sistema donde vive el problema.

- **Contenido**
  - COM-B: la conducta ocurre cuando hay capacidad, oportunidad y motivación (Michie y otros, 2011, F-856).
  - Mapas de sistemas: actores, conexiones y dónde se cruzan las lógicas.
  - Métodos para ver: observación en terreno, entrevistas, datos de uso, análisis de los objetos (formularios,
    pólizas, apps).
  - Informar no basta: una divulgación clara mejora la comprensión pero casi no cambia la conducta (Adams y otros,
    2021, F-9).
- **Caso:** Back to Basics. Un pedido de speeches para asesores se convirtió en un diagnóstico de sistema: las
  lógicas del cliente, la aseguradora y el vendedor no conversan, y todo desemboca en un asesor sobrecargado.
- **Taller:** diagnóstico COM-B de la conducta del proyecto y un primer mapa de sistema.

## Sesión 4 · Diseñar y probar

**Idea central:** una idea sin prueba es una opinión. El valor está en experimentar en la propia población, con un
indicador declarado antes.

- **Contenido**
  - Del mensaje al producto: los defaults y la reducción de esfuerzo son las palancas de mayor efecto en salud y
    finanzas (Mertens y otros, 2022, F-16).
  - Diseño de pruebas: grupo de control, indicador de conducta (no de opinión), tamaño de muestra en simple.
  - Megaestudios: probar muchas ideas a la vez. En gimnasios, 54 programas con 61.293 personas; ganó un
    microincentivo en el momento de recaída (Milkman y otros, 2021, F-20).
  - Producto embebido: un seguro tipo pago por uso con retroalimentación redujo el exceso de velocidad 11-13% y el
    efecto se sostuvo (F-442).
  - Medir más que el acto: bienestar, comprensión y confianza, con escalas validadas.
- **Caso:** Bienestar 360. Un programa de hábitos saludables medido en tres planos: salud, bienestar y experiencia.
- **Taller:** cada equipo escribe su intervención y su plan de prueba en una página: hipótesis, grupo de control,
  indicador, duración y qué decisión tomarán según el resultado.

## Sesión 5 · Conducta e inteligencia artificial

**Idea central:** la IA ya es parte del entorno donde ocurre la conducta. Mueve a las personas, tiene su propia
"conducta" y sirve como herramienta del oficio, con límites.

- **Contenido**
  - Cómo la IA mueve a las personas: la IA complaciente aumenta la dependencia y la gente la prefiere igual (Cheng y
    otros, 2026, F-488); conversar con una IA bajó la creencia en teorías conspirativas (Costello y otros, 2024,
    F-586).
  - Sobre-confianza: lo que la gente dice de un asistente no prueba que decida mejor con él. Hay que medir sus
    decisiones (node `conducta-humano-ia`); la fricción cognitiva reduce la sobre-confianza (Buçinca y otros, 2021,
    F-245).
  - La conducta de la máquina: equipos dedicados a la "personalidad" de los modelos y a reducir la adulación
    (F-849).
  - La IA como herramienta: poblaciones simuladas (Park y otros, 2024, F-549; empresas como Simile y Aaru, F-850,
    F-851) y modelos que predicen decisiones humanas (Binz y otros, 2025, F-563). Límite: sus respuestas difieren de
    las humanas (F-627). Sirven para filtrar ideas, no para reemplazar la prueba con personas.
  - Evaluar un agente conversacional: usabilidad, calidad técnica y efecto en la conducta, sin mezclarlos (node
    `evaluacion-calidad-agentes-conversacionales-ia`).
- **Taller:** si la conducta del proyecto pasa por un canal digital o un asistente, ¿qué capa decide el algoritmo?
  ¿Cómo mediríamos si la IA mejora la decisión de la persona y no solo su satisfacción?

## Sesión 6 · Ética, escala y presentación de proyectos

**Idea central:** todo diseño sirve a alguien. Facilitar una decisión no puede convertirse en manipularla.

- **Contenido**
  - A quién sirve la regla: patrones oscuros, sludge y el caso de la "huella de carbono" como estrategia para desviar
    la atención del sistema (Chater y Loewenstein, 2022, F-19).
  - Cuando el desvío se vuelve en contra: si la persona lo vive como recorte y no como cuidado, se resiste.
  - Indicadores con cautela: cuanto más se usa un indicador para decidir, más presión hay para distorsionarlo.
  - Cómo trabajan hoy los equipos en el mundo (fuentes 2022-2026): gobierno (unidades de nudge de EE. UU., F-21;
    auditorías de fricción de la OCDE en 14 países, F-862; MineduLAB, F-861), consultoras y ONG (Irrational Labs,
    Busara, F-854, F-853), dentro de aseguradoras (Swiss Re, RGA, Vitality, F-847, F-848, F-231, F-25) y con IA
    (Simile, Aaru, OpenAI, BIT con Cambridge, F-849 a F-851, F-855).
- **Presentación final:** cada equipo presenta en 8 minutos su conducta, su diagnóstico, su intervención, su plan de
  prueba y su respuesta a la pregunta "¿a quién sirve este diseño?".

---

## Evaluación

| Componente | Peso | Qué se mira |
|---|---|---|
| Participación en talleres | 30% | Que el equipo aplique el marco de la sesión a su caso. |
| Diagnóstico (sesión 3) | 20% | Conducta bien definida, capas identificadas, COM-B con evidencia. |
| Plan de prueba (sesión 4) | 25% | Grupo de control, indicador de conducta declarado antes, decisión según resultado. |
| Presentación final (sesión 6) | 25% | Coherencia de punta a punta y una respuesta honesta a "¿a quién sirve?". |

## Materiales

- Plantilla de las seis capas (una página).
- Plantilla COM-B y de mapa de sistema.
- Plantilla de plan de prueba de una página.
- Lista de verificación ética: a quién sirve, qué fricción se agrega o quita, cómo se vigila el indicador.
- Lecturas: las fuentes citadas por sesión (registro de fuentes del proyecto). Para cada sesión, una lectura
  obligatoria corta y dos opcionales.

## Decisiones abiertas

- **Público:** interno (equipos de RIMAC) o abierto. Si es abierto, los casos internos deben pasar por Comunicaciones y
  presentarse sin cifras no aprobadas.
- **Certificación:** constancia de participación o evaluación con nota.
- **Docentes:** qué sesión dicta cada integrante del equipo.
