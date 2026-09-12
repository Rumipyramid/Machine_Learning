# Plan para construir la Visión y Estrategia de Canales Digitales — Rimac Seguros

> **Output** del hub de investigación. Construido el **2026-09-11** (viernes) para la sesión de
> diseño del **lunes 14-sep** con los dos service designers, y para dar rol y forma a la
> **reunión de todo el canal del jueves 17-sep**.
>
> **Actualizado el 2026-09-11 (noche)**: confirmaciones del usuario incorporadas — RIMAC, JTBD,
> alcance con postventa y siniestros, César y Jonathan, el CEO no asiste al jueves, el entregable
> es un documento con soluciones ejecutables, Luciana ya es Gerente del canal de la App, y **no
> existe plan estratégico RIMAC 2026-2028**. Ver §0.5 ④, §2.5 y §5.5.
>
> Integra tres marcos: **Jobs to be Done** (eje de demanda), **modelo por componentes** (eje de
> oferta) y **The Cone Framework** de Romano Theunissen — *The Futures Cone Reimagined*, Journal
> of Futures Studies, 2026 (F-469) — como **arquitectura del proceso completo**.
>
> ⚠️ Escribí *Rimac* donde dictaste *"Rimax"* (asumo transcripción de voz). Si es deliberado,
> reemplázalo en todo el documento.

---

## 0. Lectura del encargo (lo primero que hay que decir en voz alta)

El CEO **no pidió una estrategia digital**. Pidió **claridad**. Son cosas distintas y confundirlas
es la trampa del encargo.

El síntoma que describe — *"me traen soluciones sin una estrategia"* — no se cura con un documento
de estrategia. Se cura con **un criterio de decisión compartido y auditable** que permita, frente
a cualquier iniciativa que le llegue, decir *esto sí, esto no, esto todavía no, y esta es la
razón*. Hoy ese criterio no existe o no es público; por eso toda solución que llega parece
igualmente defendible y ninguna se puede rechazar sin política de por medio.

De ahí se derivan **tres** entregables, no uno:

| Lo que se pide | Lo que realmente resuelve el dolor | Horizonte |
|---|---|---|
| "Visión de canales digitales" | Una **declaración de futuro preferido** (1 frase + 3 principios) que haga que las decisiones de hoy sumen entre sí | Largo plazo |
| "Estrategia" | Un **criterio de priorización explícito** aplicable a cualquier solicitud entrante | Permanente |
| "Corto plazo" | Una **cartera secuenciada de activaciones** (qué componente, en qué ramo, primero) | 2 trimestres |

> 🎯 **Prueba de éxito del plan**: al final, el CEO debería poder tomar **tres solicitudes reales
> que ya estén en su bandeja** y clasificarlas él mismo con el criterio, sin que tú estés en la
> sala. Si eso no se puede hacer, produjimos un marco bonito y no resolvimos nada.

---

## 0.5. Lo que ya existe, y qué clase de cosa es cada una

> Incorporado el **2026-09-11 (tarde)** tras la conversación con Milly. Fuente: reporte verbal del
> usuario, no documento — todo lo de esta sección debe confirmarse el lunes.

La pregunta era: *¿cuál es la estrategia del equipo del App de Luciana, y qué parte de la
estrategia de RIMAC le pega al ecosistema digital?* La respuesta de Milly: **no hay ninguna de las
dos.**

Eso no es un vacío de información: **es el hallazgo que valida el encargo del CEO.** No estás
llegando tarde a una estrategia existente — estás a tiempo para escribir la primera. Dilo así el
lunes: cambia el tono de todo el proyecto, de *"ponernos al día"* a *"redactar el original"*.

Lo que sí hay son **cinco definiciones** construidas para 2026. No son la misma clase de cosa, y
tratarlas como si lo fueran es lo que produce la confusión:

| Definición 2026 | Qué clase de cosa es realmente | Qué decide | Qué hacer con ella |
|---|---|---|---|
| Que la estrategia **involucre a todos los canales** | **Alcance** | Nada por sí sola, pero confirma que la matriz es multicanal y no solo app | Se adopta como restricción de diseño |
| **Interconexión de BBDD · interoperabilidad · modularidad** | **Capacidades habilitantes** (medios) | Qué *se puede* construir, no qué *conviene* construir | Alimentan el inventario de componentes transversales (§3.3) |
| **Personalización / campos dinámicos** — *"cuánto pagas hoy y cuánto el próximo mes"* | **Un job real, enunciado como feature** | Es demanda, no arquitectura | Entra al Jobs Studio tal cual: ya es casi una job story |
| **Super app** con conexión a clínicas, back y front | **Apuesta de arquitectura de negocio** | Compromete años y presupuesto | ⚠️ La única que es una decisión estratégica grande. **Debe pasar por el cono en la E4**, no entrar como premisa |
| **Valor directo: ventas + reducción de gasto operativo vía autogestión — no MAU** | **Norte de valor** | ✅ Lo más cercano a una estrategia que tienen, y es bueno | Se adopta como **ancla del criterio de priorización** |

### Tres lecturas que cambian el plan

**① El hueco exacto está entre la fila 5 y la fila 4.** Nadie ha demostrado que la super app sea el
camino más corto a *más ventas y menos gasto operativo*. Hay un norte de valor declarado y una
apuesta de arquitectura grande, y **ninguna evidencia que los conecte**. Ese hueco es,
literalmente, el trabajo de las seis semanas. Y es la forma menos confrontativa de plantearlo: no
se cuestiona la super app, se pregunta por el puente.

**② El norte del canal ya ganó por ti la batalla que yo anticipaba.** En §3.3 advertí que si
"digital" se lee solo como venta, la estrategia nace coja. **No hace falta dar esa pelea**:
*reducción de gasto operativo vía autogestión* **es** las capas 4 y 5 del modelo de componentes
—servicio, postventa, momento de verdad—. Luciana y Simeón ya la ganaron. Consecuencia operativa
inmediata: **el top-10 de motivos de contacto del contact center deja de ser "un proxy barato" y
pasa a ser el dato #1 del proyecto** — es la medida directa del gasto operativo digitalizable, o
sea, de la métrica que el propio canal declaró como norte.

**③ Las definiciones no son un obstáculo: son el escenario "proyectado".** En el Cono actualizado,
*proyectado* = los pronósticos institucionales formales. **Ya tienes el proyectado escrito y con
dueño.** Eso te ahorra trabajo en la Etapa 4 y, sobre todo, te permite ubicar la super app sin
confrontar a nadie: no la cuestionas, la clasificas junto a los demás escenarios y dejas que la
pregunta *¿preferido por quién, bajo qué condiciones?* haga el trabajo.

**④ No existe un plan estratégico RIMAC 2026-2028.** *(Confirmado el 11-sep. Era una pregunta
abierta; ahora es un hecho, y es el más pesado de los cuatro.)* Tres consecuencias:

- **Explica el pedido del CEO mejor de lo que parecía.** No es que no le cuenten lo que hacen: es
  que **no hay de dónde colgarlo**. Cualquier iniciativa que le llegue es igual de defendible
  porque no existe un marco corporativo contra el cual contrastarla. Su pedido de claridad está
  bien fundado.
- **Le agrega trabajo a la Etapa 3.** El Triángulo de Futuros esperaba poder derivar los *empujes*
  y el *jalón* de un plan corporativo. Hay que construirlos: los empujes desde mercado, regulación
  y tecnología; el jalón desde el propio taller. **Prevé 3.5 h para el 1-oct, no 3.**
- **Sube el listón y el riesgo.** El entregable del 22-oct va a ser, de facto, **el documento
  estratégico más concreto que tenga la compañía sobre digital**. Es una oportunidad grande y
  también un peso. Conviene decirlo en voz alta el lunes — y es el argumento para pedir 20 minutos
  del CEO a mitad de camino (§5.5).

### ⚠️ La pregunta de alcance, que es la más importante que queda abierta

Tres círculos posibles, y no está claro cuál es el encargo:

| Círculo | Quién lo encarna | Tamaño |
|---|---|---|
| **La App** | Luciana — Gerente del canal de la App | El más chico |
| **Todo el canal digital** | Simeón — subgerente de todo el canal digital, y quien agendó el jueves | Intermedio |
| **Todos los canales** | La definición 2026 dice literalmente "que involucre a todos los canales" | El más grande |

Son tres tamaños de proyecto distintos, y cambian la matriz, la lista de invitados del jueves y el
destinatario del documento. **Resuélvelo el lunes, antes que cualquier otra cosa.** Si no hay
respuesta clara, la respuesta por defecto debería ser **todo el canal digital** —el alcance de
Simeón, que es quien convocó— y declararlo explícitamente en la primera página del documento.

### Lo que sigue abierto

- **La lista completa de ramos y qué agrupa PNC** — sigue sin respuesta; sin eso la matriz no tiene
  columnas definidas.
- **Línea base** de las dos métricas del norte: ventas por canal digital y costo operativo por
  transacción. Sin línea base, "valor directo" no es medible y el criterio queda cojo en su factor
  más importante.

### Mapa de actores

| Quién | Rol | Qué necesita de esto |
|---|---|---|
| **CEO** | Pidió claridad. **No asiste al jueves ni a ninguna de las cinco sesiones** | Un criterio que pueda aplicar solo, y una visión en una frase |
| **Luciana** | **Gerente del canal de la App** | Que la estrategia exista y sea suya, no impuesta desde el CoE. **Es quien puede ratificar el contrato de proceso en la sala** (§5.5) |
| **Simeón** | Subgerente del canal digital, bajo Luciana. **Agendó el evento del jueves.** Lleva el seguimiento de capacidades | Que el trabajo se conecte con el inventario de capacidades que él ya lleva, no que lo duplique |
| **Milly** | Pone el plazo: algo en 2-3 sprints | Un entregable por sprint, no un informe al final |
| **César** | Service designer — propuso **JTBD** | Dueño del eje de demanda; facilita la E4 |
| **Jonathan** | Service designer — propuso el **modelo por componentes** | Dueño del eje de oferta; facilita la E3 |
| **Product designer** *(por asignar)* | Entra en el Sprint 1 en el track de evidencia. Dueño del **cómo se hace real y qué cuesta** | Una frontera escrita con Jonathan, y la regla de cero pantallas propuestas antes del 8-oct (§6.1) |
| **Tú (CoE de Experiencia)** | Dueño del **método**, no de la ejecución | Que la Etapa 5 asigne dueños por apuesta para no quedar como cuello de botella |

> ⚠️ **Simeón agendó el jueves, y eso cambia la política de la reunión.** No es tu reunión: es de
> él. Tres consecuencias:
>
> **(1) Hay que alinearlo antes del jueves**, idealmente el lunes mismo. Si él espera un
> levantamiento de capacidades y tú corres *Recruit or Repel* sin avisarle, quemas la relación con
> el dueño operativo del canal justo al empezar.
>
> **(2) Es el dueño natural del eje de componentes.** Ya está a cargo del seguimiento de
> capacidades. El modelo por componentes **no hay que vendérselo: hay que conectarlo con lo que él
> ya está haciendo.** Pregúntale por su inventario actual *antes* de construir uno nuevo — si ya
> existe, te ahorras una semana del Sprint 1 y le das autoría.
>
> **(3)** *Corrección del 11-sep:* no hay transición de roles pendiente — **Luciana ya es Gerente
> del canal de la App**. Lo que sí queda es la asimetría de alcances entre ella y Simeón, que es la
> pregunta de alcance de más arriba.

---

## 1. Arquitectura: cómo se integran los tres marcos (y por qué no compiten)

Los dos service designers te dieron recomendaciones que **parecen alternativas y no lo son**: cada
una cubre un eje distinto. El Cone Framework aporta el tercero — y además aporta **la secuencia**.

```
        THE CONE FRAMEWORK (Theunissen, 2026)  ──  la SECUENCIA del proceso
        E1 presente → E2 pasado → E3 presente analítico → E4 futuros → E5 compromiso
                                        │
                 ┌──────────────────────┴──────────────────────┐
                 ▼                                             ▼
        JOBS TO BE DONE                              MODELO POR COMPONENTES
        ¿para quién / para qué?    ──►  MATRIZ  ◄──  ¿con qué capacidad?
        eje DEMANDA                  Job × Componente          eje OFERTA
                                  ponderada por VOLUMETRÍA
                                             │
                                             ▼
                          CARTERA con dueños, renuncias y señales
```

- **Eje demanda — Jobs to be Done.** Unidad: *el job del cliente*, no el producto ni el ramo.
  Responde **dónde atacar primero** sin que la respuesta sea "el ramo cuyo gerente grita más".
  Un mismo job (*"quiero saber si esto me cubre antes de pagar"*) cruza Salud, Vehicular y Vida
  — y eso es lo que hace que una inversión digital rinda en varios ramos a la vez.
- **Eje oferta — modelo por componentes.** Unidad: *la capacidad digital reutilizable*. Responde
  **qué activar primero**, con evidencia de volumetría.
- **Secuencia y profundidad — Cone Framework.** Responde **en qué orden hacer las preguntas** para
  que la visión no sea una extrapolación del presente disfrazada de ambición. Su aporte central:
  el presente no se levanta, **se construye**; y el proceso no cierra en posibilidad sino en
  responsabilidad.

### 1.1 Lo que aporta cada marco que los otros no pueden dar

| | JTBD | Componentes | Cone Framework |
|---|---|---|---|
| Evita | Priorizar por política interna | Comprar soluciones no reutilizables | Confundir visión con extrapolación |
| Falla si va solo | Insights sin capacidad de ejecutar | Roadmap de TI sin cliente | Inspiración sin cartera |
| Pregunta que hace | ¿Qué progreso busca la persona? | ¿Qué pieza lo habilita y ya existe? | ¿Desde qué presente y qué memoria estamos imaginando, y quién responde? |

---

## 2. El plan: seis semanas sobre la cadencia de los jueves

Fechas ancladas a hoy (viernes **11-sep-2026**). Cada jueves es una etapa del Cone Framework.

| # | Cuándo | Etapa / bloque | Quiénes | Entregable |
|---|---|---|---|---|
| **S0** | **Lun 14-sep** | Diseño del plan | Tú + 2 service designers | Plan acordado, rol del jueves, reparto de facilitación |
| **S1** | **Jue 17-sep · 90 min** | 🫀 **Etapa 1 — Descubrir el presente** | **Todo el canal** | Verdad afectiva del canal + contrato de proceso + dueños de datos |
| — | 18-sep → 1-oct | Volumetría + inventario de componentes + Jobs Studio | Tú + SDs + datos/TI | Tablero de volumetría · inventario de capacidades · mapa de jobs |
| **S2** | **Jue 24-sep · 3 h** | 🕰️ **Etapa 2 — Entender el pasado** | Núcleo representativo | Línea de tiempo con los cinco pasados del canal digital |
| **S3** | **Jue 1-oct · 3 h** | ⚖️ **Etapa 3 — Entender el presente** | Núcleo representativo | Triángulo de Futuros: empujes, pesos, jalones — con la volumetría encima |
| **S4** | **Jue 8-oct · 4 h** | 🔭 **Etapa 4 — Imaginar futuros** | Núcleo representativo | Escenarios CPSM + clasificación en el Cono + futuro preferido |
| **S5** | **Jue 15-oct · 4 h** | 🤝 **Etapa 5 — Volver al presente** | Núcleo + decisores | Backcasting, cartera, dueños, renuncias y señales de falsación |
| **—** | ~22-oct | Presentación al CEO | — | Visión (1 frase + 3 principios) + criterio + cartera H1 |

> ⚠️ **Regla de oro**: ninguna de estas seis semanas produce soluciones. Producen el criterio para
> elegirlas. Si en la semana 2 alguien ya está diseñando pantallas, el plan falló y reprodujimos
> el problema que el CEO reportó.

> 🔻 **Trade-off que hay que declarar el lunes.** Theunissen reporta que las sesiones más potentes
> se hacen en **dos días seguidos**, y advierte que estirar la Etapa 5 rompe energía y cohesión.
> Aquí estiramos a cinco semanas. **A favor**: las Etapas 1-2 son emocionalmente densas y él mismo
> recomienda no apurarlas; y necesitamos la volumetría entre la E1 y la E3. **En contra**: se
> pierde continuidad. **Mitigación**: mismo núcleo en las cuatro sesiones (no rotativo), 5 min de
> recapitulación al abrir cada una, y un muro compartido que sobreviva entre sesiones.
> Alternativa si el calendario lo permite: fusionar **E4+E5 en un offsite de dos días** (8 y 9 de
> octubre). Es la versión más fiel al marco y la que yo recomendaría pelear.

---

## 2.5. El plan en sprints — la pregunta de Milly

Milly quiere tener algo en **2-3 sprints**. Buena noticia: **encaja casi exacto**, si son sprints
de dos semanas arrancando el lunes 14.

| Sprint | Fechas | Qué contiene | Entregable al cierre |
|---|---|---|---|
| **1** | 15 → 26 sep | E1 (17-sep) · E2 (24-sep) · volumetría e inventario · **auditoría de interfaz** | Presente construido · inventario de componentes con estado · **diagnóstico de por qué lo que existe no se usa** · mitos listados para falsar · **línea base de las dos métricas del norte** |
| **2** | 29 sep → 10 oct | E3 (1-oct) · E4 (8-oct) | **Criterio con pesos · matriz Job × Componente priorizada · futuro preferido · escenarios clasificados (incluida la super app)** |
| **3** | 13 → 24 oct | E5 (15-oct) · **checkpoint con el CEO** (§5.5) · presentación (~22-oct) | **El documento de dos partes**: Parte A (visión + criterio con pesos) y Parte B (3 soluciones especificadas para ejecutar, con alcance, métrica, dueño y dependencias) |

> ✂️ **Si Milly solo tiene dos sprints, el corte es el 10 de octubre.** Al cierre del Sprint 2 ya
> hay con qué decidir: criterio, matriz priorizada y futuro preferido. Lo que falta después es el
> backcasting y la asignación de dueños — importante, pero ya no bloquea la toma de decisiones.

### Resuelto: qué es «algo» — un documento con soluciones para ejecutar

Milly lo aclaró. Eso cierra la ambigüedad y cambia dos cosas.

**① El Track B se cae como estaba planteado.** No hace falta tener algo corriendo al cierre del
Sprint 3. Pero deja una regla, más abajo.

**② Sube la resolución del entregable final.** El plan entregaba «cartera de 3 apuestas con
dueños». Eso no alcanza: *soluciones para ejecutar* significa que un equipo debe poder tomar el
documento y empezar. Hay que llegar a **alcance, métrica, dueño, dependencias de capacidad y un
primer corte de qué se construye**, por cada una de las tres.

> ⚠️ **Y hay una trampa que hay que nombrar en voz alta el lunes.** «Un documento con soluciones
> para ejecutar» está a un paso de ser exactamente lo que el CEO reportó como problema:
> *soluciones*. La única diferencia es que estas vienen **con el criterio que las justifica, y el
> criterio manda sobre ellas.**

Por eso el entregable es **un documento de dos partes**:

| | **Parte A — Por qué** | **Parte B — Qué** |
|---|---|---|
| Contenido | La visión (1 frase + 3 principios) y el criterio de priorización con sus pesos | Las 3 soluciones especificadas para ejecutar |
| Orden | Se escribe primero | **Se deriva de A — cada solución muestra su score** |
| Uso posterior | Cualquier iniciativa futura pasa por aquí | Se ejecuta y se mide contra el norte del canal |

> 🔒 **La regla que protege todo el trabajo, y va en la primera página del documento:** si alguien
> extrae la Parte B y la circula sola, reprodujimos el problema que el CEO reportó. La Parte B sin
> la Parte A es una lista de soluciones más.

**Regla para las tres soluciones:** al menos una debe salir de la categoría `Existe pero no se usa`
— ejecutable en el sprint siguiente, sin arquitectura nueva y sin comprometer la decisión de super
app. Es la que le da a Milly algo que se mueve de inmediato y compra credibilidad para las otras
dos.


---

## 3. Los instrumentos de evidencia (alimentan la Etapa 3)

### 3.1 Volumetría: qué pedir, a quién, en qué formato

Arranca **el viernes 18 o el lunes 21**: es lo único con dependencia externa (datos, TI, contact
center) y lo que más tarda.

**Por cada ramo × componente, 12 meses, granularidad mensual:**

1. **Tráfico y entrada** — sesiones únicas por origen (orgánico, paid, app, WhatsApp, link de
   asesor, IVR-a-digital).
2. **Embudo por paso** — intentos iniciados vs. completados en cada componente
   (cotizar → seleccionar → datos → pago → emisión). *El paso donde se cae la gente es la
   evidencia de fricción más barata que existe.*
3. **Volumen digitalizable no digital** — transacciones que hoy pasan por teléfono, agencia o
   asesor y que técnicamente ya podrían ser digitales: cotización, emisión, pago,
   endoso/modificación, renovación, aviso de siniestro, constancias.
4. ⭐ **Top 10 motivos de contacto al contact center** por ramo, con volumen y AHT. **Este es el
   dato #1 del proyecto, no el cuarto.** Desde que el canal declaró que su norte es *reducir el
   gasto operativo vía autogestión* (§0.5), este dato dejó de ser un proxy barato de "job no
   resuelto" y pasó a ser **la medición directa de la métrica que el canal eligió como norte**.
   Pídelo primero y persíguelo tú mismo.
5. **Contactabilidad** — % de la base con dato digital válido **y consentimiento vigente**
   (conecta con `_nodes/transicion-venta-fria-a-opt-in.md`).
6. **Costo por transacción por canal** — aunque sea estimado. Sin esto no hay caso de negocio.
7. **Estado de la capacidad** — ¿el componente existe, existe a medias, o no existe?

**Regla de decisión** — acuérdenla el lunes, **antes** de ver los datos, para que el criterio no
se acomode al resultado:

> 🔑 *El primer componente que se activa no es el más grande ni el más nuevo: es donde coinciden
> **volumen alto + fricción alta + capacidad ya instalada**. Lo grande sin capacidad es un
> proyecto; lo nuevo sin volumen es una apuesta de horizonte largo.*

**Plan B si la volumetría no existe o está federada por ramo** (probable): no se detiene el plan.
(a) Top motivos de contacto, (b) estimación acordada por cada gerente de ramo en **una sola**
sesión de 90 min, con rangos y nivel de confianza declarado, (c) la incertidumbre se marca en la
matriz en vez de esconderse. **Un número con intervalo declarado decide mejor que un número falso
con dos decimales.**

---

### 3.2 Jobs Studio — el eje de demanda

> 📌 **Asumo que "job studion" = Jobs to be Done** (posiblemente *job stories*, que es su artefacto
> de escritura). Si tu service designer se refería a otra cosa, corrígelo el lunes: el plan sigue
> funcionando, solo cambia el contenido de este bloque.

**Formato del job** — progreso que la persona busca, no funcionalidad ni producto:

```
Cuando [situación],
quiero [progreso buscado],
para poder [resultado esperado].
```

Ejemplos en clave seguros, escritos a propósito de forma transversal a ramos:

- *Cuando me pasa algo y no sé si estoy cubierto, quiero confirmarlo en menos de un minuto, para
  poder decidir qué hacer sin llamar a nadie.*
- *Cuando me toca renovar, quiero entender qué cambió y por qué subió, para poder aceptar sin
  sentir que me están viendo la cara.*
- *Cuando estoy comparando, quiero saber qué NO cubre, para poder confiar en lo que sí.*

**Por qué esto resuelve tu problema de ramos.** Tienes (por confirmar el lunes — la lista que
dictaste vino incompleta):

| Ramo | Nota |
|---|---|
| Salud | |
| Vehicular | |
| Vida | |
| PNC / P&C masivos | ⚠️ confirmar qué agrupa exactamente y si es vista de canal o de producto |
| B2B / Empresas | Job del corredor ≠ job del cliente final. Doble sujeto. |
| Financieros / Bancaseguros | Canal de terceros — restricciones propias |

Si priorizas **por ramo**, la decisión es política. Si priorizas **por job**, aparecen dos clases
de oportunidad y las dos son defendibles ante el CEO:

- **Jobs transversales** (el mismo job en 4+ ramos) → justifican inversión en un componente
  **compartido**. Es el argumento más fuerte que vas a tener: *una inversión, cinco ramos*.
- **Jobs críticos de un solo ramo** → justifican una activación **focalizada** y rápida.

**Cómo levantarlo, en orden de costo creciente:**

1. **Evidencia que ya existe (costo casi cero).** Top motivos de contact center, reclamos,
   búsquedas del sitio, logs de chat, y los nodes que este repo ya tiene:
   `_nodes/seguros-comportamiento-mundo-peru.md` (desconfianza ~48%, causa #1 falta de
   información), `_nodes/glosario-seguro-salud-peru.md` y `_nodes/glosario-seguro-vida-peru.md`
   (*el vocabulario donde la gente se pierde **es** el job no resuelto*),
   `_nodes/material-visual-venta-consultiva.md`.
2. **Barrido sintético para hipótesis (horas, no semanas).** `/lapuerta` con `--seed 42` para
   estresar hipótesis de job por NSE / generación / acceso digital **antes** de gastar entrevistas
   reales. ⚠️ Sirve para **priorizar dónde mirar**, no como evidencia de cliente.
3. **Entrevistas reales dirigidas.** 5-6 por ramo prioritario, con guion de *switch interview*
   (qué hizo antes, qué lo empujó, qué lo frenó). Solo en los 2-3 ramos donde la volumetría ya
   mostró masa.

**Priorización dentro del eje de demanda** (escala 1-5 por job):

`Oportunidad = Importancia + (Importancia − Satisfacción)`

Alta importancia + baja satisfacción = frente de ataque. Alta importancia + **alta** satisfacción
= **lo que no hay que tocar** — y decirlo explícitamente también es estrategia.

---

### 3.3 Modelo por componentes — el eje de oferta

**Qué es un componente.** Una capacidad digital **reutilizable entre ramos**, con dueño, métrica y
estado de madurez. No es una pantalla, no es un proyecto, no es un canal.

**Taxonomía propuesta** (punto de partida para el lunes). Cinco capas, porque la capa donde vive
el componente cambia quién debe ser su dueño:

| Capa | Componentes típicos | Pregunta que responde |
|---|---|---|
| **1. Captación** | Landings, comparador, paid/orgánico, referidos, link de asesor | ¿Cómo llega? |
| **2. Decisión** | Cotizador, simulador, explicador de coberturas/exclusiones, asistente conversacional | ¿Cómo entiende y elige? |
| **3. Contratación** | Onboarding, validación de identidad, suscripción/declaración de salud, pago, emisión | ¿Cómo compra? |
| **4. Servicio y postventa** | Autoservicio de póliza, endosos, cobranza, renovación, constancias, red de prestadores | ¿Cómo convive con el producto? |
| **5. Momento de verdad** | Aviso y seguimiento de siniestro, reembolsos, autorizaciones, asistencia | ¿Qué pasa cuando lo necesita? |
| **Transversales** | Identidad/cuenta única, datos y consentimiento, CRM y contactabilidad, notificaciones, medición | Habilitan a todas las anteriores |

**Estado de cada componente** (una línea por componente × ramo):

`No existe` · `Existe parcial` · `Existe pero no se usa` · `Existe y rinde`

> ⚡ **"Existe pero no se usa" es la categoría más rentable del inventario** y la que nadie
> levanta: volumen y capacidad ya pagada, con fricción de adopción. Es la activación más barata
> que vas a encontrar, y da las victorias tempranas que compran credibilidad para las apuestas
> largas.

> ✅ **Confirmado el 11-sep: el alcance incluye postventa y siniestros.** Esa era la batalla que
> anticipaba dar el jueves, y ya no hay que darla — las capas 4 y 5 están dentro por definición, y
> además son donde vive el norte del canal (autogestión y gasto operativo). **Consecuencia
> práctica: la matriz debe tener al menos tanta densidad en las capas 4-5 como en las 1-3.** Si al
> cerrar el Sprint 1 el inventario está cargado solo hacia venta, el levantamiento falló y hay que
> volver a pedirlo.

---

### 3.4 La matriz y el criterio de priorización

**La matriz.** Filas = jobs priorizados. Columnas = componentes. Cada celda marcada = apuesta
candidata, coloreada por volumetría.

**El scoring.** Cinco factores, 1-5 cada uno, con peso. Esto es lo que el CEO se lleva y usa solo:

| Factor | Peso | Qué mide | De dónde sale |
|---|---|---|---|
| **Volumen** | 25 % | Masa de transacciones o contactos afectados | Volumetría (§3.1) |
| **Fricción** | 25 % | Importancia − satisfacción del job | Jobs Studio (§3.2) |
| **Valor económico** | 20 % | **Ventas incrementales + gasto operativo evitado** — el norte declarado del canal (§0.5). MAU y engagement **no cuentan** | Finanzas + costo por transacción + contact center |
| **Capacidad instalada** | 15 % | Qué tan cerca está de poder activarse | Inventario de componentes (§3.3) |
| **Coherencia con el futuro preferido** | 15 % | ¿Construye la visión o solo parcha? | Etapa 4 (§4) |

> 🧠 **El quinto factor es el que convierte un backlog en una estrategia.** Sin él, el scoring
> premia siempre lo urgente y barato, y en dos años tienes cincuenta parches coherentes con nada.
> Es la respuesta técnica exacta al dolor que reportó el CEO. Defiéndelo cuando alguien proponga
> quitarlo por "subjetivo": es el único factor que mira más allá del trimestre.

**Regla de corte de la cartera de corto plazo:** máximo **3 apuestas activas**. Más de tres y
vuelves al problema original con otro nombre.

> 🚫 **Regla de descarte, derivada del norte del canal.** Toda iniciativa cuyo único beneficio
> prometido sea MAU, engagement, descargas o "presencia digital" **no entra al scoring**. No se
> puntúa bajo: no se puntúa. El canal ya declaró que su valor es ventas y gasto operativo; esta
> regla solo hace cumplir esa declaración — y es la más fácil de defender ante cualquiera, porque
> no la inventaste tú.

---

## 4. The Cone Framework (Theunissen, JFS 2026) — la columna vertebral del proceso

### 4.1 Qué dice el marco, y por qué es exactamente el que necesitas

Theunissen **no rechaza el Cono de Futuros: lo reubica**. Su tesis es que el Cono nunca fue un
método — es un *andamio relacional y epistémico* (una ayuda cognitiva) que solo cobra sentido
después del trabajo duro. Usado como punto de partida, "aplana la complejidad en vez de revelarla"
y se convierte en un gesto decorativo. Su corrección tiene cinco piezas que te sirven directamente:

1. **El Cono es el punto medio, no el de entrada.** Se ubica *entre sensemaking y estrategia, entre
   imaginación y decisión*. → Justifica que el foresight ocurra en la **semana 4** y no el primer
   día, y que el jueves 17 **no** sea un taller de futuros.
2. **El presente no es un dato, es un resultado.** La base del cono se **co-construye** mediante
   reflexión, diálogo y pluralidad. → Le da estatus metodológico a tu contrapropuesta: el jueves
   no "levanta información", **construye el presente**.
3. **El proceso cierra en responsabilidad, no en posibilidad.** El ciclo se cierra *no con
   predicción sino con rendición de cuentas*. → Es el antídoto contra el taller de visión que
   produce entusiasmo y cero decisiones.
4. **Empieza por la emoción, no por las tendencias.** El orden epistémico del marco es
   deliberado: afecto → memoria → análisis → imaginación → compromiso. Lo analítico llega
   **tercero**, no primero. → Tu terreno. Eres behavioral designer; este marco está construido
   sobre tu disciplina, no sobre planeamiento estratégico.
5. **Pluralidad de pasados y presentes.** Rechaza el "ahora" único y el pasado único. El presente
   es una **zona**, no un punto; y hay cinco pasados (dominante, ignorado, olvidado, cultural,
   mítico). → En una aseguradora con ramos federados, esto no es filosofía: es literalmente que
   Salud, Vehicular y B2B **no viven el mismo presente**, y una estrategia que asume uno solo
   fracasa en los otros cuatro.

**El Cono actualizado** que propone (para la Etapa 4) suma al modelo clásico: un **Cono del
Pasado** con los cinco pasados; un **presente plural** como zona; **trayectorias no lineales**
(bucles, recursividad); **fronteras porosas** (línea punteada: lo implausible puede volverse
posible); y siete tipologías de escenario:

`Preposterous (disparatado)` · `Posible` · `Plausible` · `Probable` · `Proyectado` · `Preferido` · `Indeseable`

> 📎 **Proyectado** = los pronósticos institucionales formales (el plan estratégico vigente, el
> presupuesto 2027, el roadmap ya aprobado). **Indeseable** = trayectorias éticamente
> preocupantes. Que ambas categorías existan es lo que te permite poner sobre la mesa, sin
> confrontación, tanto lo que la empresa ya prometió como lo que nadie quiere decir en voz alta.

### 4.2 Las cinco etapas, aplicadas a Canales Digitales Rimac

| Etapa | Actividad del marco | Modo de aprendizaje | Traducción a tu caso | Cuándo |
|---|---|---|---|---|
| **1. Descubrir el presente** | **Recruit or Repel** | Afectivo / narrativo | La verdad emocional del canal digital: qué dirías para atraer a alguien y qué para espantarlo | **Jue 17-sep**, todo el canal |
| **2. Entender el pasado** | **Líneas de tiempo** (5 pasados) | Histórico-crítico | La historia real de lo digital en Rimac: lo oficial, lo ignorado, lo olvidado, lo cultural, y los mitos | **Jue 24-sep** |
| **3. Entender el presente** | **Triángulo de Futuros** (Inayatullah) | Analítico | Empujes (mercado, regulación, IA), pesos (legado, ramos federados, sistemas), jalón (la visión que atrae). **Aquí entran volumetría y jobs** | **Jue 1-oct** |
| **4. Imaginar futuros** | **CPSM** + el Cono | Imaginativo / ético | Cinco escenarios de canal digital, luego clasificados en el Cono. **Aquí entran las soluciones que ya le llevaron al CEO** | **Jue 8-oct** |
| **5. Volver al presente** | **Backcasting** + compromisos | Estratégico / normativo | Cartera, dueños, renuncias, señales de falsación | **Jue 15-oct** |

**Notas de ejecución por etapa:**

- **E1 — Recruit or Repel.** La pregunta original es: *si estuvieras en una reunión de ex
  compañeros y te encontraras con alguien a quien querrías reclutar (o ahuyentar) de esta
  organización, ¿qué le dirías?* Acotada a tu caso: **"…alguien que está evaluando entrar a
  canales digitales de Rimac"**. Las respuestas se agrupan y discuten **no por su exactitud sino
  por su verdad afectiva**. Esto *es* tu toma de temperatura — con respaldo teórico (Weick,
  sensemaking; Milojević, foresight emocional) y mucho mejor instrumento que una encuesta de
  madurez.
- **E2 — Los cinco pasados del canal digital.** Dominante: la narrativa oficial de la
  transformación digital. Ignorado: las iniciativas que se mataron y todos saben cuáles fueron.
  Olvidado: lo que recuerda la FFVV o el contact center y nunca entró a un PPT. Cultural: cómo se
  hacen las cosas por ramo. Mítico: *"el peruano no compra seguros online"*. ⚠️ Theunissen
  advierte que **E1 y E2 son emocionalmente intensas** — aparecen desilusión, duelo institucional
  y verdades incómodas. Planifica pausas y descompresión; apurarlas contamina las etapas
  siguientes.
- **E3 — Triángulo de Futuros.** Es la primera vez que entra lo analítico, **y es a propósito**.
  Los mitos que capturaste en E2 son literalmente los **pesos del pasado** del triángulo, y aquí
  se confrontan contra la volumetría. Ese choque —creencia contra dato— es el momento en que el
  proceso se gana la autoridad para proponer una visión.
- **E4 — CPSM y el Cono.** Theunissen reporta que **CPSM funciona mejor** que las matrices 2×2 o
  los arquetipos de Dator, porque se encadena naturalmente con el Triángulo. Sus cinco
  progresiones: **Mejor caso · Peor caso · Adaptativo · Regresión · Cambio marginal**. Solo
  *después* de tener los escenarios se introduce el Cono y se clasifican. ⭐ **Las cinco
  definiciones de 2026 (§0.5) entran aquí como el escenario "proyectado" —ya está escrito y tiene
  dueño— y la super app se clasifica junto al resto en lugar de discutirse como premisa.** La clasificación **va a
  generar resistencia** (a nadie le gusta que su escenario favorito quede en "plausible"), y eso
  es deseable: se maneja replanteando la clasificación **como indagación, no como juicio** — *¿preferido
  por quién? ¿indeseable para quién? ¿bajo qué condiciones?* Theunissen reporta que ahí aparece la
  conversación más rica de todo el proceso.
- **E5 — Backcasting.** Desde el futuro preferido hacia atrás: qué condiciones, decisiones y
  compromisos hacen falta. Aquí nacen la cartera, los dueños, **lo que se deja de hacer** y las
  señales que falsarían cada apuesta.

### 4.3 Tres advertencias del autor que aplican directo a tu situación

1. **Tu jefa va a pedir ver el marco completo antes.** Theunissen dice que es lo normal y que la
   solución **no** es negarse: comparte una **versión visual simplificada, omitiendo las etiquetas
   tipológicas** ("plausible", "disparatado", "pasado ignorado"). Preséntalo como **agenda
   gráfica**. No daña la experiencia y compra el permiso.
2. **No lo llames "Cono de Futuros" con los participantes.** El marco está diseñado para recorrer
   el Cono **sin nombrarlo**. Preséntalo como *"ordenar nuestras apuestas por horizonte"*. Nombrarlo
   invita a que alguien lo trate como plantilla — el error exacto que el paper denuncia.
3. **La representatividad del grupo define el techo del resultado.** Theunissen es explícito:
   un grupo homogéneo produce resultados homogéneamente sesgados, y preguntar *"¿quién no está en
   la sala?"* **no sirve de mucho** — puede incluso marginar más. Lo que sirve es **componer el
   grupo para que espeje la diversidad real de la institución**. 👉 Consecuencia concreta: el
   núcleo de las etapas 2-5 **no se arma con voluntarios**. Se arma a propósito con los seis
   ramos + asesor/FFVV + contact center + suscripción + siniestros + TI. Y el jueves 17 es la sala
   más representativa que vas a tener en todo el proceso: por eso no se puede gastar en levantar
   requerimientos.

---

## 5. La reunión del jueves 17-sep — Etapa 1, diseñada

### 5.1 El reto, dicho con precisión

Tu contrapropuesta a tu jefa es correcta, y ahora tiene un argumento más fuerte que "prefiero
tomar temperatura":

> **Un levantamiento de necesidades en una reunión de todo el canal produce una lista de deseos.
> Y una lista de deseos es exactamente "soluciones sin estrategia" — el problema que el CEO
> reportó — solo que ahora con cincuenta firmantes y expectativa de cumplimiento.**

Tres riesgos concretos, por si necesitas defenderlo:

1. **Riesgo de producto**: obtienes soluciones ya formuladas ("necesitamos un chatbot"), no jobs.
   Preguntar por necesidades a un grupo grande garantiza respuestas en formato solución.
2. **Riesgo de expectativa**: si alguien pone su pedido en un papel, asume que entró a la cartera.
   Lo que no salga después se lee como traición, y quemas el capital político de octubre.
3. **Riesgo de oportunidad**: es la sala más representativa que vas a tener (advertencia 3 de
   §4.3). Gastarla en datos que el contact center te da en un CSV es un mal negocio.

**Y el jueves sí tiene un rol crítico y no negociable**: es la **Etapa 1** del marco — donde se
co-construye el presente y donde el proceso obtiene legitimidad. Sin el jueves, en octubre
presentas una estrategia que le cayó del cielo al canal.

### 5.1-bis Antes del jueves: alinear con Simeón

**El evento lo agendó Simeón, no tú.** Todo lo de §5 se cae si él llega el jueves esperando otra
cosa. Conversación corta, el lunes o martes, con tres puntos:

1. **Reconocer que la reunión es suya** y pedirle que abra él el encuadre — no tú.
2. **Preguntarle por su inventario de capacidades antes de construir uno.** Él ya lleva ese
   seguimiento; si existe, el eje de componentes arranca con su material y con su autoría.
3. **Mostrarle la agenda gráfica** (§4.3, advertencia 1) y ser explícito en que el jueves **no**
   levanta requerimientos ni capacidades — eso viene después y con su data, no con post-its.

> Si Simeón necesita salir del jueves con algo de capacidades para su propio seguimiento, el campo
> 5 del artefacto (*¿quién tiene el dato?*) se lo da sin romper la Etapa 1. Ofrécelo así.

### 5.2 Los tres objetivos (y un no-objetivo)

| | |
|---|---|
| ✅ **O1 — Verdad afectiva** | Cómo se vive hoy el canal digital: orgullo, vergüenza, frustración, lo que nadie dice en un comité |
| ✅ **O2 — Mitos en circulación** | Capturar las creencias compartidas sobre lo digital, **sin discutirlas** (insumo del pasado mítico de E2 y de los pesos de E3) |
| ✅ **O3 — Contrato de proceso** | Presentar el plan (como agenda gráfica, §4.3) y acordar que **desde hoy ninguna iniciativa entra sin pasar por el criterio** |
| ❌ **No-objetivo** | Levantar requerimientos, recoger iniciativas o comprometer entregables |

> 🎁 **O3 es el objetivo oculto y el más valioso.** Convierte a la audiencia de *demandante de
> soluciones* en *co-constructor del criterio*. Es el cambio de rol que resuelve el problema del
> CEO de forma estructural, no puntual.

### 5.3 Agenda — 90 minutos

| Min | Bloque | Cómo | Sale con |
|---|---|---|---|
| **0-10** | **Encuadre** | Nombras el encargo del CEO tal cual y dices la frase: *"hoy no venimos a recoger pedidos, venimos a construir el punto de partida"*. Muestras la agenda gráfica de las 6 semanas. | Expectativa alineada |
| **10-40** | 🫀 **Recruit or Repel** | Individual y en silencio, 5 min: *"Te encuentras a alguien que está evaluando entrar a canales digitales de Rimac. (a) ¿Qué le dices para convencerlo? (b) ¿Qué le dices para espantarlo?"* Luego en mesas de 5-6, se comparte y se eligen las 3 frases más ciertas de cada lado. Plenario: se leen. **No se corrige a nadie.** | Frases textuales, atraer y espantar |
| **40-60** | 🔗 **Agrupar la verdad afectiva** | En plenario, agrupas los "repel" en 4-6 temas y les pones nombre **con las palabras de ellos**, no con vocabulario de consultoría. Pregunta de cierre por tema: *"¿desde cuándo es así?"* — no se responde ahora, se anota. | 4-6 temas nombrados + semillas para E2 |
| **60-75** | 🌫️ **"Todos sabemos que…"** | Anónimo, post-its: *"Completa: 'Todos sabemos que en seguros, digitalmente, ____'"*. Se leen en voz alta **sin discutir ninguna**. Anuncias: *"estas son las creencias que vamos a poner a prueba contra los datos, y les traemos el resultado el 1 de octubre"*. | 8-12 mitos etiquetados |
| **75-88** | 🤝 **Contrato** | Presentas el criterio en construcción (los 5 factores, **sin pesos todavía**) y el calendario. Pides dos cosas: **quién tiene cada dato de volumetría**, y **confirmas nominalmente el núcleo** de las etapas 2-5 (ya elegido por representatividad, no por voluntariado). | Dueños de dato + núcleo confirmado |
| **88-90** | **Cierre** | Qué reciben y cuándo: síntesis el lunes 21; la confrontación mito-vs-dato el 1-oct; la cartera el 15-oct. | Compromiso de devolución |

### 5.4 El artefacto del jueves (lo que tu jefa pedía, reconvertido)

Tu jefa pidió un artefacto de levantamiento. **Dáselo — pero que levante lo correcto.** Una
plantilla de una página, individual:

```
┌──────────────────────────────────────────────────────────────┐
│  RAMO / SUB-CANAL: ______________      (sin nombre, opcional)│
├──────────────────────────────────────────────────────────────┤
│  1. RECLUTAR — "Éntrale, porque acá…"                        │
│     _______________________________________________________  │
│  2. AHUYENTAR — "No te metas, porque acá…"                   │
│     _______________________________________________________  │
│  3. ¿DESDE CUÁNDO ES ASÍ?  (un año, un hito, un nombre)       │
│     _______________________________________________________  │
│  4. "TODOS SABEMOS QUE…"  (la creencia del canal)            │
│     _______________________________________________________  │
│  5. ¿QUIÉN TIENE EL DATO?  (volumetría, sistema, persona)     │
│     _______________________________________________________  │
│  6. 🅿️ PARKING — la solución que ibas a proponer              │
│     _______________________________________________________  │
└──────────────────────────────────────────────────────────────┘
```

> 🅿️ **El campo 6 es deliberado.** La gente *necesita* soltar su solución; si no le das dónde, la
> mete en los otros campos y te contamina la Etapa 1. Dándole un lugar explícito y prometiendo que
> **entrará al ejercicio de horizontes en la Etapa 4** (donde se clasifica, no se descarta),
> consigues las dos cosas: material limpio y nadie ignorado. Es diseño conductual aplicado a tu
> propio proceso — y es tu terreno.
>
> 💡 El campo 3 es el puente a la Etapa 2: cada respuesta es una entrada de la línea de tiempo.

### 5.5 El CEO no está en la sala — dos cosas que resolver

Confirmado: al jueves va **gerencia para abajo, sin CEO**. Y tampoco participa de ninguna de las
cinco sesiones.

**Lo bueno, y no es menor:** sin el CEO en la sala, *Recruit or Repel* funciona mucho mejor. La
verdad afectiva se dice cuando el jefe máximo no está. Es una ventaja real para la Etapa 1.

**(1) El contrato de proceso (O3) necesita a Luciana.** El acuerdo de que *"desde hoy ninguna
iniciativa entra sin pasar por el criterio"* **no lo puedes declarar tú**: eres del CoE, no del
canal. Necesitas que **Luciana lo diga en la sala**, o que lo respalde explícitamente. Pídeselo
antes del jueves, junto con la alineación con Simeón (§5.1-bis).

**(2) El destinatario final no participa de ninguna sesión.** Riesgo real: llegar el 22-oct con
algo que no se parece a lo que el CEO tenía en la cabeza, después de seis semanas y sin margen para
corregir.

> 🎯 **Antídoto: un checkpoint de 20 minutos con el CEO al cierre del Sprint 2** (semana del
> 13-oct), cuando ya existan el criterio y el futuro preferido pero **antes** de especificar las
> soluciones. No es para pedir permiso: es para verificar que **el criterio le sirve para decidir**.
> Si le sirve, la Parte B se escribe sola. Si no, corriges con dos semanas de margen en vez de
> cero. Y ahora tienes el argumento para pedirlo: **no existe plan estratégico corporativo**
> (§0.5 ④), así que este documento va a ser la referencia de la compañía sobre digital.

**Táctica para la franqueza con Luciana presente.** La agenda ya la protege: escritura individual
en silencio antes del plenario (min 10-40) y post-its anónimos (min 60-75). **Mantén esos dos
formatos exactamente como están** — son lo que permite que se diga lo incómodo con la gerente en la
sala.

---

## 6. La sesión del lunes 14-sep con César y Jonathan

**2 h. Objetivo: salir con el plan firmado y el jueves diseñado.** No es para explorar marcos, es
para cerrar decisiones.

| Min | Tema | Decisión que debe salir |
|---|---|---|
| 0-15 | **Encuadre del encargo** (§0) | Acuerdo en que el entregable es *criterio + visión + cartera*, no un documento de estrategia |
| 15-35 | **Integración de los tres marcos** (§1) | Acuerdo en que JTBD y componentes son **ejes de la misma matriz**, y el Cone Framework es **la secuencia**. *Momento delicado: cada SD trae su recomendación. El encuadre "ejes complementarios + secuencia" evita que sea una competencia entre ellos.* |
| 35-50 | **Unidad de análisis** | Definición cerrada de qué es un job y qué es un componente en Rimac; taxonomía ajustada (§3.3) |
| 50-65 | **Criterio de priorización** (§3.4) | Los 5 factores y **sus pesos, acordados antes de ver datos** |
| 65-85 | **Diseño del jueves** (§5) | Agenda, artefacto, y quién facilita qué. Ensayar en voz alta el enunciado de *Recruit or Repel* |
| 85-100 | **Composición del núcleo** (§4.3, adv. 3) | Lista nominal de 10-14 personas que espejen la institución — **antes** del jueves |
| 100-110 | **Volumetría** (§3.1) | Lista de pedidos de datos, a quién, quién los persigue |
| 110-120 | **Calendario y el offsite** | ¿Se pelea el offsite de 2 días para E4+E5 (8-9 oct)? Dueño de cada entregable |

### Reparto de facilitación — César y Jonathan

Confirmado el 11-sep: **Jonathan propuso el modelo por componentes y César el JTBD.** El reparto
sale solo de ahí — **cada uno facilita el eje que propuso**, y tú el marco que los integra. Es lo
que desactiva la competencia entre marcos: no compiten porque cada uno tiene su eje y ninguno
tiene el todo.

| Sesión | Facilita | Por qué |
|---|---|---|
| **E1 · 17-sep** | **Tú** | Es afectiva y narrativa: es tu disciplina |
| **E2 · 24-sep** | Tú + **Jonathan** | Las líneas de tiempo cruzan memoria y capacidad |
| **E3 · 1-oct** | **Jonathan** (propuso componentes) | Es la sesión analítica y la que usa la volumetría |
| **E4 · 8-oct** | **César** (propuso JTBD) | Escenarios, imaginación y clasificación |
| **E5 · 15-oct** | Tú + **Simeón** | Compromisos y dueños: necesita al canal, no al CoE |

### 6.1 El product designer: dónde entra y con qué frontera

**Entra en el Sprint 1, desde el 18-sep, en el track de evidencia — no en el de talleres.** Cuatro
aportes, en orden de valor:

1. **Es el dueño natural de la Parte B del entregable.** Especificar tres soluciones al nivel que un
   equipo pueda ejecutarlas es diseño de producto, no de servicio. César y Jonathan llevan hasta
   *qué apostar*; el PD lleva hasta *qué se construye*. Sin él, la Parte B queda vaga y el pedido de
   Milly falla.
2. **Cierra el hueco del inventario de componentes.** `Existe pero no se usa` es una categoría, no
   un diagnóstico — y la razón casi siempre es de interfaz: enterrado a tres taps, nombrado con un
   término interno, punto de entrada en otra parte. El PD la convierte en causa, justo donde tiene
   que salir al menos una de las tres soluciones (§2.5).
3. **Traduce "campos dinámicos" de feature a producto.** Contrato de datos, estados (¿y si no hay
   cifra del próximo mes? ¿y si cambió por un siniestro?), errores, y viabilidad con la
   interoperabilidad actual. Es el puente entre las capacidades habilitantes y el job (§0.5).
4. **Hace clasificables los escenarios de la E4.** Tres pantallas toscas vuelven juzgable un futuro
   que en abstracto no lo es. **Props de escenario, deliberadamente feos — no propuestas.**

**Por qué en el Sprint 1 y no en el 3.** Un PD que llega al final a especificar, sin haber estado
en el proceso, produce specs desconectadas del criterio. Entrando con un entregable de
**diagnóstico**, la Parte B se escribe sola.

> ⚠️ **El riesgo: que empiece a diseñar.** No es defecto personal, es el reflejo de la disciplina —
> y es lo que hundiría la regla de oro de §2. **Antídoto:** su entregable del Sprint 1 es una
> **auditoría de interfaz** (diagnóstico, no propuesta), y una regla escrita — **cero pantallas
> propuestas antes del 8-oct**, y ahí solo como props de escenario.

**El reparto queda sin solapes:**

| Quién | Pregunta que responde | Unidad |
|---|---|---|
| **César** | ¿Qué progreso busca la persona? | job |
| **Jonathan** | ¿Qué capacidad lo habilita? | componente |
| **Product designer** | ¿Cómo se hace real y qué cuesta? | producto |
| **Tú** | ¿Por qué esto y no aquello? | criterio |

Esa frontera es el punto: **si el PD entra sin ella, colisiona con Jonathan en componentes**, los
dos mirando la misma capacidad desde ángulos que se pisan.

**Preguntas que hay que resolver el lunes y no después:**

1. ⚠️ **¿Cuál es el alcance real — la App, todo el canal digital, o todos los canales?** (§0.5).
   Es la primera, y cambia el tamaño de todo lo demás.
2. ¿Cuál es la **lista completa de ramos** y qué agrupa "PNC"? Sin eso la matriz no tiene columnas.
3. ¿Qué iniciativas **ya están comprometidas y presupuestadas** para 2027? → son el escenario
   **"proyectado"** de la Etapa 4, y el criterio tiene que poder convivir con ellas
4. ¿Quién decide finalmente — el CEO, un comité, tu jefa? → determina el formato del entregable
5. ¿Hay **restricción de tecnología o proveedor** ya tomada? → limita qué componentes son
   activables en el corto plazo
6. ¿Los dos service designers **facilitan** las etapas 2-5 o solo diseñan? → afecta tu carga y el
   riesgo de cuello de botella
7. ¿Hay **línea base** de ventas digitales y costo operativo por transacción? Sin eso, el factor de
   valor económico no es calculable
8. ¿Quién es el dueño formal de la **decisión de super app** — Luciana, el CEO, TI? → determina si
   la E4 puede realmente clasificarla o solo comentarla
9. ¿Validan César y Jonathan las siete decisiones del borrador low-fi? → ver output de validación

---

## 7. Riesgos del plan y antídotos

| Riesgo | Señal temprana | Antídoto |
|---|---|---|
| El jueves se convierte en lista de deseos | En el minuto 30 la gente propone soluciones | El "parking" explícito (§5.4) + facilitación firme |
| E1/E2 se desbordan emocionalmente | Silencio incómodo, o una persona monopoliza el dolor | Advertencia del autor: pausas, escritura individual antes de plenario, no apurar |
| La clasificación de la E4 se vuelve pelea | "Ese escenario no es *solo* plausible" | Replantear como indagación: *¿preferido por quién? ¿bajo qué condiciones?* |
| "Digital" se lee solo como venta | Nadie menciona siniestros ni renovación | Forzar las capas 4-5 en la taxonomía desde el lunes |
| La volumetría no existe o está federada | A los 5 días nadie responde el pedido de datos | Plan B de §3.1: estimaciones con rango declarado |
| Producimos un modelo elegante que nadie usa | El criterio nunca se aplica a un caso real | **Prueba de fuego**: aplicar el scoring en vivo a 3 solicitudes reales pendientes, delante del comité |
| Pérdida de cohesión por estirar a 5 semanas | Cae la asistencia del núcleo en la 3.ª sesión | Mismo núcleo, recap de 5 min, muro persistente; o el offsite E4+E5 |
| El núcleo termina siendo homogéneo | Solo van los "digitales" y los entusiastas | Composición nominal por representatividad (§4.3, adv. 3), no por invitación abierta |
| El CEO no participa de ninguna sesión y el 22-oct no reconoce su pedido | Nadie ha validado el criterio con él | Checkpoint de 20 min al cierre del Sprint 2 (§5.5) |
| Alguien circula la Parte B sin la Parte A | «Pásame solo las tres soluciones» | La regla en la primera página del documento (§2.5) |
| El alcance real nunca se define | Se habla de «la app» y de «todos los canales» en la misma frase | Decidirlo el lunes; por defecto, todo el canal digital, declarado por escrito |
| Simeón llega al jueves esperando otra reunión | No respondió o no confirmó el encuadre | Alineación previa obligatoria (§5.1-bis) — es su evento |
| La super app se blinda como premisa no discutible | «Eso ya está decidido» antes de la E4 | Clasificarla, no cuestionarla; y pedir el puente de evidencia hacia ventas y gasto operativo (§0.5 ①) |
| El plan se lee como seis semanas de talleres | Milly pregunta «¿y qué entregamos?» | Track B con sus tres condiciones (§2.5) |
| Duplicamos el inventario de capacidades de Simeón | Dos listas de componentes en circulación | Preguntar primero, construir después |
| Tú quedas como cuello de botella | Todo pasa por ti | Etapa 5: dueño por apuesta, no dueño del plan |

---

## 8. Lo que puedes mandarle a tu jefa hoy o el lunes temprano

> *"Sobre el pedido del CEO: creo que lo que está pidiendo no es un documento de estrategia sino
> un criterio para decidir — algo que le permita mirar cualquier iniciativa que le llegue y saber
> por qué sí o por qué no. Propongo un proceso de seis semanas que produce tres cosas: (1) una
> visión de canal digital en una frase con tres principios, (2) un criterio de priorización
> explícito que cualquiera pueda aplicar, y (3) una cartera de tres activaciones para los próximos
> dos trimestres, priorizada con volumetría real.*
>
> *La reunión del jueves entra como el arranque del proceso: no como levantamiento de
> requerimientos —que nos daría una lista de deseos y reproduciría justo el problema que el CEO
> reporta— sino como la construcción del punto de partida común y el acuerdo de que, de aquí en
> adelante, ninguna iniciativa entra sin pasar por el criterio. Salimos del jueves con la lectura
> real de cómo se vive hoy el canal, las creencias que estamos dando por ciertas, los dueños de
> los datos que necesitamos, y el grupo confirmado para las siguientes sesiones. El método está
> tomado de un marco publicado de foresight participativo; te lo detallo el lunes después de la
> sesión con los service designers."*

---

## 9. Pendientes

### ✅ Resuelto el 11-sep

RIMAC (no Rimax) · «job studion» = Jobs to be Done · el alcance incluye postventa y siniestros ·
los service designers son César y Jonathan · el CEO no asiste al jueves (gerencia para abajo) ·
«algo en 2-3 sprints» = un documento con soluciones para ejecutar · Luciana ya es Gerente del canal
de la App · **no existe plan estratégico RIMAC 2026-2028**.

### Abierto — para el lunes

- [ ] ⚠️ **Definir el alcance**: ¿la App, todo el canal digital, o todos los canales? (§0.5)
- [ ] **Lista completa de ramos** y qué agrupa PNC
- [ ] **Alinear con Simeón antes del jueves** y pedirle su inventario de capacidades
- [ ] **Pedirle a Luciana que ratifique el contrato de proceso en la sala** (§5.5)
- [ ] Gestionar el **checkpoint de 20 min con el CEO** para la semana del 13-oct
- [ ] Conseguir línea base de ventas digitales y costo operativo por transacción
- [ ] Definir quién es el dueño formal de la decisión de super app
- [ ] **Nombrar al product designer** y confirmar capacidad desde el 18-sep. Si no hay nadie hasta
      octubre, entraría solo a la E4 y a la Parte B, y se pierde la auditoría de interfaz del Sprint 1
- [ ] Decidir si se pelea el offsite de dos días para las etapas 4 y 5

---

## Fuentes

- **F-469** — Theunissen, R. (2026). *The Futures Cone Reimagined: A Framework for Critical and
  Plural Futures Thinking*. Journal of Futures Studies. Texto completo leído. Marco de las cinco
  etapas, el Cono actualizado, las siete tipologías y las lecciones de facilitación de §4.
  Referencias internas citadas por el autor y usadas aquí: Voros (2003, 2017), Gall et al. (2022),
  Inayatullah (Triángulo de Futuros, 2023), Milojević (CPSM 2005; foresight emocional 2024),
  Weick (sensemaking, 1995), Robinson (backcasting, 1990), Dator (arquetipos), Escobar (2020),
  Sardar (2010), Christophilopoulos (2021), Terry et al. (2024).

## Conexiones

- [[futuro-asesores-seguros-venta-digital]] — el filo plural: qué futuro asumimos para el asesor
- [[venta-vida-digital-hibrida-latam]] — evidencia regional de modelos digital vs. híbrido
- [[seguros-comportamiento-mundo-peru]] — desconfianza, barreras y penetración: insumo del presente
- [[transicion-venta-fria-a-opt-in]] — contactabilidad y consentimiento como componente transversal
- [[material-visual-venta-consultiva]] — reducción de incertidumbre en la capa de decisión
- [[modelo-personas-sinteticas]] — `/lapuerta` como barrido previo de hipótesis de jobs
- [[behavioral-design-estado-disciplina]] — por qué el orden afecto→memoria→análisis es tu terreno

---

## Output derivado

- `_outputs/validacion-estrategia-canales-digitales-lowfi-2026-09-11.html` — borrador low-fi en
  blanco y negro con **siete decisiones a validar**, para César y Jonathan antes de la sesión del
  lunes. Es una destilación de este plan, no una fuente nueva: si una decisión cambia allí, este
  documento se actualiza.
