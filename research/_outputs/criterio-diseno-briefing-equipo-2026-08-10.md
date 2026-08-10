# Criterio de diseño: qué sostiene, qué no, y qué hacer con eso

**Briefing para el equipo de diseño** · 2026-08-10
Construido sobre `_nodes/tendencias-diseno-innovacion.md` (v5.0, iteración 5).
Fuentes por ID en `research/fuentes/codice.md` (consultables con `/codice`).

> Esto no es un reporte de tendencias. Es el destilado de cinco corridas de investigación
> en una sola pregunta: **qué podemos afirmar en una sala sin que nos lo tumben**, y qué
> conviene dejar de decir.
>
> Está organizado por **la situación en la que estás**, no por tema. Salta a la que te toca.

---

## Resumen en cinco frases

1. **El diseño sí produce valor: es real, pequeño, acumulativo y mediado** — no transformacional. Cerca de 2/3 de los cambios bien diseñados no mueven la métrica que buscaban.
2. **Las cinco cifras estrella con que la industria vende diseño están rotas, y ninguna se retiró** — siguen circulando en paralelo. Si las usas, eres vulnerable en la sala.
3. **La IA no amenaza tu producto: amenaza tu margen.** Y en el día a día, la mayor parte del gasto en IA se va en corregir a la IA.
4. **La preferencia declarada y el desempeño real se separan justo donde duele**: prevención de errores, recuperación y ayuda.
5. **El contenido de tendencias en español no cita nada** (15 de 20 piezas), y cuando cita, importa el 100% de sus cifras de emisores con interés comercial.

---

## Situación 1 — Vas a sustentar el valor del diseño ante quien decide presupuesto

### Lo que sabemos

La afirmación "el diseño produce impacto de negocio" es **probablemente cierta y está mal
probada**. La evidencia sólida (econometría de firmas, experimentación online) dice algo mucho
más modesto que la retórica del gremio: el efecto es **real, pequeño, acumulativo y mediado**.

La distribución real de efectos es de **cola larga con moda cero**. Traducido: la mayoría de
tus cambios bien diseñados no van a mover su métrica objetivo, y eso es normal, no un fracaso.

### El problema: la lista negra

Cinco cifras sostienen casi todo el discurso de ROI del diseño. Las cinco se desmontaron.
**Ninguna se retiró de circulación** — el hallazgo de la iteración 3 fue que la industria no
corrige, **acumula**: las cinco siguen vivas en paralelo, cada una en su nicho.

| No digas esto | Por qué te lo tumban | Di esto en su lugar |
|---|---|---|
| "El diseño devuelve 100x lo invertido" (**$1 → $100**) | No hay estudio primario legible. En 2026 se describe como "el benchmark estándar" sin que nadie lo haya leído (F-423) | "Este cambio elimina 3 pasos del flujo y el retrabajo que generaban" |
| "Las empresas *design-centric* crecen **+32%/+56%**" (McKinsey) | Correlacional, de 2018, publicado por quien vende consultoría de diseño. En varias piezas circula mal fechado como "McKinsey 2026" (F-424) | "Medimos esta métrica antes y después, con este control" |
| "El índice de empresas de diseño rindió **+211%**" (DVI) | Índice construido mirando hacia atrás; sin edición nueva desde 2016; dos cifras históricas conflacionadas | *(sin reemplazo — no uses índices de este tipo)* |
| "Un design system ahorra **47% / 69% / 135%** de tiempo" | Un solo estudio, una sola empresa, sin replicación independiente tras cuatro barridos. Las calculadoras de 2026 siguen usando el 135% de 2022 (F-425) | "En nuestro equipo este componente ahorró N horas — aquí está la medición" |
| "**671%** de ROI" | No colapsa en una fuente mala: **no colapsa en ninguna** | *(sin reemplazo)* |

### Accionables

- **Argumenta por mecanismo, nunca por multiplicador.** "Quita N pasos, M errores y X horas de
  retrabajo" resiste a un CFO. "El diseño devuelve 100x" no sobrevive a la primera pregunta por
  la metodología.
- **Promete acumulación, no transformación.** La promesa honesta y defendible es *iterar y
  medir*, no *rediseñar y despegar*. Es además la única que puedes cumplir.
- **Regla de admisión a un entregable: si no puedes leer el estudio primario, la cifra no entra.**

---

## Situación 2 — Vas a trabajar con IA, o a justificar lo que cuesta

### Lo que sabemos

**El riesgo de la IA para una empresa de diseño no es que le reemplace el producto: es que le
coma el margen.** El caso de agosto de 2026 es limpio: Figma creció **48%**, batió ingresos y
utilidad, subió su guía anual — y la acción cayó **16,5%**. El detonante fue que su **costo de
inferencia subió 117%**, y que la compañía **regala inferencia en beta sin ingreso que la
compense** (F-469, F-470, F-471).

**Y en el día a día, el costo real de la IA es corregirla.** Desde marzo de 2026 Figma metra y
cobra créditos de IA, y por primera vez el fenómeno tiene precio en vez de anécdota: usuarios
reportan agotar US$120 en créditos, comprar US$240 más y quedarse sin ellos **con 10 días de mes
por delante**, y quemar **3.000+ créditos en una hora** arreglando lo que la IA rompió. La queja
que se repite: **la mayor parte del consumo se va en corregir salida mala o incompleta** (F-474).

**El dato contraintuitivo que cambia cómo se controla la calidad:** el escrutinio **decae con la
exposición**, no crece con la seniority. En 400 revisores y 11.429 revisiones, la tasa de
aprobación **sube 14,5 puntos** conforme se acumula exposición a salidas de IA (F-407). El riesgo
no es el junior que no sabe revisar: **es el veterano que ya se acostumbró.**

### Accionables

- **Presupuesta la corrección, no la generación.** El costo de una tarea con IA es el de la
  tarea **terminada bien**, no el del primer output.
- **Métrica que sí sirve: costo (o tiempo) por tarea *completada correctamente*, no por tarea
  iniciada.** La diferencia entre ambas *es* el impuesto de verificación.
- **En control de calidad de trabajo asistido por IA: rota revisores y siembra casos de
  control.** Si no lo haces, tu tasa de defectos detectados va a bajar sola y no vas a poder
  distinguir "el modelo mejoró" de "el revisor se acostumbró" — dos cosas opuestas.
- **Si pilotea IA en el equipo, segmenta por madurez del proceso que interviene.** Un piloto que
  promedia perfiles y contextos mide cero.

⚠️ **Honestidad sobre esto:** los testimonios de consumo son de foro, autoseleccionados. Prueban
que *existen* usuarios para quienes la corrección es la mayor parte del gasto y les duele en
dinero. **No** prueban que sea la mayoría del gasto del mercado — esa versión fuerte sigue sin
evidencia y no conviene afirmarla.

---

## Situación 3 — Vas a medir si un diseño funcionó

### Lo que sabemos

**La preferencia declarada y el desempeño real se separan sistemáticamente, y se separan justo
donde más duele.** El caso mejor documentado es la *generative UI* (interfaces que se arman solas
con IA): gana en preferencia declarada —hasta **72%**— y falla exactamente en **prevención de
errores, eficiencia de uso, recuperación y ayuda** (F-381, F-382). Además produce interfaces
distintas ante el mismo prompt incluso repitiendo la ejecución (F-384): la inconsistencia que
destruiría la aprendibilidad **ya está medida**.

**Un matiz que nos corrige a nosotros mismos:** habíamos apostado a que la brecha entre desempeño
objetivo y percibido sería de **≥20 puntos**. El mejor estudio disponible (peer-reviewed, N=452
con réplica) la mide en **~1 punto**: objetivo +3, autoestimación +4 (F-401). **Acertamos el
signo y fallamos la escala.** La brecha existe; no es un abismo.

### Accionables

- **Si mides satisfacción sin medir recuperación de error, estás midiendo la mitad optimista
  del fenómeno.** Vale para cualquier interfaz con IA, incluidos agentes conversacionales.
- **Mide sesión 1 contra sesión 5.** Todo lo que existe mide sesión única — y es justo ahí donde
  las interfaces generativas ganan.
- **No aceptes "a los usuarios les gustó más" como evidencia de que funciona mejor.** Son dos
  preguntas distintas y la literatura las separa.

---

## Situación 4 — Vas a citar una tendencia, un estudio o una cifra

### Lo que sabemos

El contenido de tendencias de diseño en español está peor de lo que parece. En una auditoría de
~20 piezas:

- **15 de 20 (75%) no citan ninguna fuente.** Afirman "el minimalismo sigue ganando fuerza" y ya.
- De las que sí citan, **13 de 13 (100%)** de las cifras vienen de emisores anglosajones con
  interés comercial directo. **Cero** piezas citaron un estudio con muestra propia en español o
  portugués. Y **tres cifras se atribuían a un Gartner que nunca las publicó** (F-408, F-418).

Y este mes aparecieron **dos trampas nuevas**, las más limpias que hemos documentado:

#### Trampa 1 — El calificador muere en el primer salto, y lo mata la universidad

> **Paper arbitrado:** "…el impacto de programas **simulados** de seguro basado en uso sobre la seguridad al conducir"
> **Nota de prensa de la misma universidad:** "**El seguro basado en uso mejora la seguridad al conducir**"

La palabra que hace honesto al hallazgo la borró **su propio autor institucional**, antes de que
la tocara ningún periodista, blog o consultora (F-479, F-480).

➜ **Cita el título del paper, nunca el titular de la nota de prensa.** Si solo tienes la nota,
asume que **ya se perdió algún calificador** y busca cuál.

#### Trampa 2 — La cifra exacta que no existe

Rastreamos una ronda de financiamiento. Los agregadores la reportan **cerrada**: "US$300M
levantados en 2026, valuación US$13.200M". Un resumen automático de IA llegó a afirmar que "la
ronda finalmente cerró por encima de esa cifra". **Ninguna ronda cerró.** La única real fue de
US$330M a US$6.600M, ocho meses antes; la de US$12.000M sigue en conversaciones (F-481, F-482,
F-483).

Esta cadena **no tiene un solo autor humano** en ningún eslabón: se fabrica entre agregación
automática y resumen por IA. Y viene con monto, año y valuación exactos — **la precisión aparente
es justamente lo que la hace creíble**.

➜ **La precisión no es señal de veracidad cuando no hay autor.**

### Accionable: cuatro preguntas antes de citar algo

Córrelas en orden. Si falla cualquiera, la cifra no entra al entregable.

1. **¿Quién gana si creo esto?** (descuento por incentivo del emisor — aplica también a quien
   *desmiente*: el que dice "el diseño no ha muerto" también vive de la audiencia)
2. **¿El emisor citado realmente lo publicó?** No preguntes si es débil; pregunta si **existe**.
3. **¿Llegué al primario?** Compañía, regulador o paper. **Nunca** un agregador ni un resumen de
   buscador. Sospecha en especial de **la cifra más redonda y más reciente**.
4. **¿El titular conserva los calificadores del original?**

---

## Lo que no sabemos, y no vamos a fingir que sí

- **No existe ni un solo estudio longitudinal de generative UI.** Cuatro barridos independientes
  con términos distintos, cero resultados. Todo lo que se afirme sobre aprendibilidad de
  interfaces generativas hoy es especulación — incluida la nuestra.
- **No hay replicación independiente del efecto de los design systems.** El campo
  **institucionalizó el mismo estudio** en vez de replicarlo.
- **No tenemos dato peruano de gobernanza de IA en diseño.** Cuatro iteraciones buscándolo, en
  blanco. Lo más cercano es Brasil (N=823): **60% usa IA en cuentas personales, 14% con
  capacitación de la empresa** (F-389). Si Perú se parece, **la intervención de mayor retorno es
  gobernanza, no capacitación en herramientas** — pero eso es una hipótesis, no un dato.
  ➜ Se resuelve con fuente primaria: una encuesta interna, no con más búsqueda.
- **Este briefing se construyó sin poder leer un solo texto completo.** Cinco corridas con
  bloqueos de red en los repositorios académicos y en los sitios de relaciones con inversionistas.
  Las cifras son reconstrucción a partir de coberturas concordantes. **Antes de llevar cualquiera
  a un entregable externo, revalídala contra el documento primario.**

---

## Una nota para el equipo

En la misma semana en que el mercado castigó a Figma por sus costos de IA, **su Chief Design
Officer amplió funciones y pasó a liderar producto** (F-473). Desde 2026 veníamos documentando lo
contrario —compresión del rol de diseño dentro de otras funciones— y este es **el primer caso
direccional inverso** que encontramos: diseño absorbiendo producto en vez de ser absorbido.

Un caso no es una tendencia, y la explicación es disputable. Pero vale conocerlo.

---

## Conexiones

- [[tendencias-diseno-innovacion|Tendencias en diseño e innovación]] — node fuente de este
  briefing: tablero de 33 hipótesis, 24 reglas de criterio y la bitácora de las cinco iteraciones.
  Lo que aquí se presenta como criterio cerrado, allí está con su estado, su evidencia y sus
  descuentos.
- [[behavioral-design-estado-disciplina|Behavioral design: estado de la disciplina]] — la misma
  estructura de problema en una disciplina vecina: una industria que sobrevendió su efecto
  promedio y se defiende mejor por mecanismo que por multiplicador.
- [[material-visual-venta-consultiva|Material visual en la venta consultiva]] — el caso aplicado
  de la Situación 3: qué material visual reduce incertidumbre de verdad y cuál solo lo parece.
- [[evaluacion-calidad-agentes-conversacionales-ia|Evaluación de calidad de agentes de IA]] — la
  Situación 2 y la 3 son directamente su instrumentación: medir por tarea completada
  correctamente, y no medir satisfacción sin medir recuperación de error.
