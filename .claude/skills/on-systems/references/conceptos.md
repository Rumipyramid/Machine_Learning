# Conceptos: el núcleo dinámico

Fuentes: Donella Meadows, *Thinking in Systems: A Primer* (Chelsea Green, 2008); Peter Senge, *The Fifth Discipline*, edición revisada (Currency, 2006); Christian Baron, *Methods for Systems Thinking* (Routledge, 2026).

Este archivo es el vocabulario común del skill y la profundidad de los bloques `comportamiento` y `estructura`. Los métodos que operacionalizan estos conceptos están en `metodos.md`; los patrones que forman están en `arquetipos.md`.

Índice:
1. [La tesis: la estructura genera el comportamiento](#1-la-tesis-la-estructura-genera-el-comportamiento)
2. [Qué es un sistema](#2-qué-es-un-sistema)
3. [Stocks y flujos](#3-stocks-y-flujos)
4. [Retroalimentación](#4-retroalimentación)
5. [Retrasos](#5-retrasos)
6. [No linealidad, límites y emergencia](#6-no-linealidad-límites-y-emergencia)
7. [Por qué los sistemas funcionan: resiliencia, autoorganización, jerarquía](#7-por-qué-los-sistemas-funcionan-resiliencia-autoorganización-jerarquía)
8. [Racionalidad acotada](#8-racionalidad-acotada)
9. [El bloque `comportamiento`: levantar el comportamiento en el tiempo](#9-el-bloque-comportamiento-levantar-el-comportamiento-en-el-tiempo)
10. [El bloque `estructura`: construir el mapa](#10-el-bloque-estructura-construir-el-mapa)

---

## 1. La tesis: la estructura genera el comportamiento

Meadows enseña con un Slinky, ese resorte largo que rebota. Lo sostiene con una mano, lo suelta con la otra, y el resorte oscila. Pregunta qué lo hizo oscilar. La respuesta obvia es "tu mano". Entonces repite el gesto con la caja en la que venía el Slinky, y la caja no hace nada.

**Lo que hace oscilar está dentro del resorte.** La mano solo libera un comportamiento que ya estaba latente en la estructura. Esa es la idea central de todo el marco: **el sistema causa, en gran medida, su propio comportamiento.** Un evento externo puede desencadenarlo, pero el mismo evento aplicado a otro sistema produce otra cosa.

Consecuencias que hay que decir en voz alta con el usuario, porque son incómodas:

- Los líderes políticos no causan las recesiones; los altibajos son inherentes a la estructura de la economía de mercado.
- Los competidores rara vez causan que una empresa pierda participación de mercado. Están ahí para recoger la ventaja, pero la empresa que pierde crea sus pérdidas al menos en parte con sus propias políticas.

### Los tres niveles de explicación

De Senge, y es la herramienta más rentable de todo el marco para una conversación. Cada nivel es igualmente cierto y produce una postura distinta:

| Nivel | Pregunta que responde | Postura que produce |
|---|---|---|
| **Eventos** | ¿Quién hizo qué a quién? | Reactiva |
| **Patrones de comportamiento** | ¿Qué viene pasando en el tiempo? | Responsiva |
| **Estructura sistémica** | ¿Qué causa esos patrones? | **Generativa** |

Las explicaciones de eventos son las dominantes en la cultura contemporánea, y por eso predomina la gestión reactiva. Solo las estructurales abordan las causas en un nivel donde el patrón se puede cambiar.

Cuando el usuario explique su problema en nivel de eventos, no lo corrijas. Devuélvele la misma historia un nivel más abajo y pregúntale si se reconoce. El movimiento es más convincente que la lección.

El Iceberg de Baron agrega una cuarta capa debajo, los modelos mentales, que se trabaja en el bloque `modelos-mentales` (`frontera-y-perspectivas.md`).

### Complejidad de detalle y complejidad dinámica

Distinción de Senge que evita el error más común del pensamiento sistémico aplicado.

- **Complejidad de detalle**: muchas variables. Armar un mueble con instrucciones largas, hacer el inventario de una tienda.
- **Complejidad dinámica**: causa y efecto son sutiles y los efectos de las intervenciones en el tiempo no son obvios. Hay complejidad dinámica cuando la misma acción tiene efectos muy distintos en el corto y en el largo plazo, o efectos distintos acá que allá.

**El apalancamiento real está en entender la complejidad dinámica.** Para mucha gente, pensamiento sistémico significa combatir complejidad con complejidad: modelos con miles de variables. Eso es lo contrario del pensamiento sistémico. Un mapa con cuarenta nodos distrae de ver los patrones; uno con ocho bien elegidos los revela.

---

## 2. Qué es un sistema

Un sistema es **un conjunto interconectado de elementos organizado coherentemente de manera que logra algo**. Tres cosas: elementos, interconexiones, y una función o propósito.

Prueba rápida para saber si estás mirando un sistema o un montón de cosas: ¿puedes identificar partes? ¿las partes se afectan entre sí? ¿juntas producen un efecto distinto del de cada una por separado? ¿ese comportamiento persiste en circunstancias variadas?

### La jerarquía de importancia

Cámbialos uno por uno mentalmente y verás cuál pesa:

- **Cambiar elementos** suele tener el menor efecto. Cambia todos los jugadores de un equipo de fútbol y sigue siendo un equipo de fútbol.
- **Cambiar interconexiones** altera mucho el sistema. Cambia las reglas del fútbol por las del básquetbol y es otro juego con los mismos jugadores.
- **Cambiar el propósito lo cambia todo**, aunque elementos e interconexiones queden iguales.

Y el propósito es la parte menos obvia de las tres. De ahí sale la mitad del valor de este skill.

### El propósito declarado y el propósito revelado

**El propósito se deduce del comportamiento, no de la retórica.** Si una rana gira a la derecha y caza una mosca, gira a la izquierda y caza una mosca, y gira hacia atrás y caza una mosca, su propósito no tiene que ver con girar: tiene que ver con cazar moscas.

Si un gobierno proclama interés en proteger el ambiente pero asigna poco dinero y poco esfuerzo, la protección ambiental no es, de hecho, su propósito. Si un hospital declara la salud de la comunidad pero su conducta prioriza sistemáticamente el ingreso sobre el cuidado, su propósito efectivo es el ingreso.

**Cómo se usa esto en conversación sin acusar a nadie:** no digas "el propósito real de tu organización es X". Pregunta "si alguien de afuera solo mirara qué se aprueba, qué se premia y qué se posterga, ¿qué diría que este sistema está tratando de lograr?". La brecha entre esa respuesta y el propósito declarado es casi siempre el hallazgo más valioso del análisis, y le pertenece al usuario, no a ti.

Ojo con los subpropósitos: uno de los aspectos más frustrantes de los sistemas es que los propósitos de las subunidades pueden sumar un comportamiento global que nadie quiere. Cuando la meta de un subsistema domina a costa de la del sistema total, eso se llama **suboptimización**.

---

## 3. Stocks y flujos

**Stock**: una acumulación de material o información construida en el tiempo. Es lo que puedes ver, sentir, contar o medir en un momento dado. Un stock es la memoria de la historia de flujos cambiantes del sistema. No tiene que ser físico: la confianza acumulada, la reputación y la deuda técnica son stocks.

**Flujo**: lo que llena o vacía el stock.

### Los principios de la bañera

Simples y sorprendentemente poco usados:

- Si la suma de entradas supera la de salidas, el stock sube.
- Si la de salidas supera la de entradas, el stock baja.
- Si son iguales, hay equilibrio dinámico: el nivel no cambia aunque el agua siga corriendo.
- **Un stock se puede aumentar bajando su salida, no solo subiendo su entrada.** La mente humana se fija más en los stocks que en los flujos, y dentro de los flujos, más en las entradas que en las salidas. Un avance en eficiencia energética equivale, en su efecto sobre el stock de petróleo disponible, a descubrir un yacimiento nuevo. Una empresa puede aumentar su dotación contratando más o bajando la rotación, y las dos rutas cuestan cosas muy distintas.
- **Los stocks cambian lentamente aunque los flujos cambien de golpe.** Por eso actúan como retrasos, amortiguadores y fuentes de inercia. Y por eso también dan margen de maniobra: dan tiempo para experimentar y corregir.
- **Los stocks permiten que la entrada y la salida se desacoplen.** Sería imposible operar una petrolera si la gasolina tuviera que producirse exactamente al ritmo en que los autos la queman.

**Cómo usarlo con el usuario:** cuando alguien describe un problema en términos de flujo ("estamos contratando poco"), pregunta por el stock ("¿cuánta gente hay y cuánta se va?"). Casi siempre aparece que el problema estaba en la salida y nadie la estaba mirando.

---

## 4. Retroalimentación

Un ciclo de retroalimentación (feedback loop) se forma cuando los cambios en un stock afectan a los flujos que entran o salen de ese mismo stock.

**Ciclo balanceador (B)**: estabilizador, busca meta. Se opone a cualquier dirección de cambio que se le imponga. Es fuente de estabilidad **y también de resistencia al cambio**. El termostato es el ejemplo canónico.

**Ciclo reforzador (R)**: amplifica. Cada acción empuja al sistema más en la misma dirección. Produce crecimiento exponencial o colapso desbocado. Aparece donde un stock tiene la capacidad de reproducirse a sí mismo.

Atajo útil: **el tiempo de duplicación de un stock que crece exponencialmente es aproximadamente 70 dividido por la tasa de crecimiento expresada en porcentaje.** Al 7% anual, diez años.

### Las metas implícitas

Lo que hace difíciles los ciclos balanceadores en la práctica es que **sus metas suelen ser implícitas y nadie reconoce que el ciclo existe**.

El caso de Senge: un amigo suyo trataba de reducir el agotamiento en su empresa de capacitación. Escribió memos, acortó la jornada, llegó a cerrar las oficinas más temprano. Todo se compensó: ignoraron los memos, desobedecieron los horarios y se llevaron el trabajo a la casa. La razón era una norma no escrita que decía que los que de verdad se comprometían trabajaban setenta horas a la semana. Norma que él mismo había establecido con su propio ejemplo.

**De ahí la regla más útil sobre resistencia:** siempre que hay resistencia al cambio, puedes contar con que hay uno o más procesos balanceadores ocultos. La resistencia no es caprichosa ni misteriosa; casi siempre nace de amenazas a normas tradicionales, y esas normas suelen estar entretejidas con relaciones de poder establecidas. En vez de empujar más fuerte, busca la fuente.

### Dominancia cambiante

Los comportamientos complejos suelen aparecer cuando **la fuerza relativa de los ciclos cambia** y primero domina uno y después otro. Un stock gobernado por un reforzador y un balanceador crece exponencialmente si el reforzador domina, decae si domina el balanceador, y se estabiliza si están parejos.

Y un principio que hace mucho trabajo: **sistemas con estructuras de retroalimentación parecidas producen comportamientos parecidos, aunque por fuera se vean completamente distintos.** Una población y una economía industrial son el mismo animal: un stock con un ciclo reforzador de crecimiento y uno balanceador de muerte. Esto es lo que hace posible que los arquetipos existan.

---

## 5. Retrasos

Un retraso (delay) es la brecha de tiempo entre una acción y su efecto visible. Son la fuente principal de sorpresa en los sistemas.

**Un retraso en un ciclo balanceador vuelve probable que el sistema oscile.**

### El caso que hay que contar

Meadows modela un concesionario de autos con tres retrasos realistas: de percepción (promedia las ventas de cinco días antes de decidir), de respuesta (corrige un tercio de la brecha por vez) y de entrega (cinco días de la fábrica). La demanda sube 10% una sola vez. El resultado son oscilaciones fuertes en el inventario.

La dueña, que es inteligente, decide reaccionar más rápido: acorta su percepción de cinco días a dos. **Las oscilaciones empeoran.** Acorta su tiempo de respuesta de tres días a dos. **Empeoran mucho más.** Lo que funciona es lo contrario: alargar la respuesta de tres a seis días amortigua las oscilaciones y el sistema encuentra su equilibrio.

Meadows llama a esto **"alta palanca, dirección equivocada"**: alguien encuentra intuitivamente una palanca que de verdad tiene fuerza, y la empuja al revés. Es uno de los errores más caros que existen y hay que buscarlo activamente en el bloque `apalancamiento`.

### Reglas prácticas

- Regla de Forrester para estimar: pregunta a todos en el sistema cuánto creen que dura el retraso, haz tu mejor estimación, y **multiplica por tres**.
- "Toma dos aspirinas y espera": cuenta lo que ya pediste y todavía no llegó antes de pedir más. Del Beer Game de Senge, donde la demanda del consumidor sube una sola vez y queda plana, y aun así todo el sistema entra en crisis por los retrasos.
- La información que entrega un ciclo **solo puede afectar el comportamiento futuro**. No puede corregir la conducta que produjo la retroalimentación actual. Por eso siempre habrá retraso.
- Un ciclo balanceador que mantiene un stock **tiene que fijar su meta compensando los procesos de vaciado**. Si quieres 18 grados en la pieza, el termostato va un poco más arriba, porque el calor se escapa mientras el horno lo repone.

---

## 6. No linealidad, límites y emergencia

**No linealidad**: la causa no produce un efecto proporcional. Importa sobre todo por una razón de segundo orden: **la no linealidad cambia la fuerza relativa de los ciclos** y puede voltear un sistema de un modo de comportamiento a otro.

**Ley del mínimo (von Liebig)**: en cualquier momento, **el insumo más importante para un sistema es el que más lo limita**. No sirve echar más nitrógeno si lo que falta es fósforo.

**Capas de límites**: la comprensión real no viene de identificar cuál es el factor limitante hoy, sino de ver que **el crecimiento cambia cuál es el limitante**. La interacción entre lo que crece y su límite es dinámica. Modelo de crecimiento corporativo de Forrester: contratas vendedores excelentes, generan más pedidos de los que la fábrica produce, expandes la fábrica, contratas gente apurado y sin entrenar, cae la calidad, inviertes en formación, mejora la calidad, llueven pedidos y ahora se atasca el sistema de registro. Y así.

Y el que hay que decir en voz alta cuando alguien plantea crecer indefinidamente: **siempre habrá límites al crecimiento; pueden ser autoimpuestos o los impondrá el sistema.**

**Emergencia**: patrones que surgen de la interacción y que ninguna parte contiene por sí sola. La conciencia no está en una neurona. El tráfico no está en un conductor. Explica por qué las intervenciones a nivel de componente muchas veces no funcionan.

---

## 7. Por qué los sistemas funcionan: resiliencia, autoorganización, jerarquía

Estas tres se sacrifican con facilidad porque no se ven, y perderlas es caro.

**Resiliencia**: capacidad de recuperarse tras una perturbación. Surge de una estructura rica de muchos ciclos de retroalimentación que operan por mecanismos distintos, en escalas de tiempo distintas y con redundancia, uno entrando cuando otro falla.

No es lo mismo que estabilidad estática: un sistema resiliente puede ser muy dinámico, y las oscilaciones pueden ser justamente la condición normal que la resiliencia restaura. Meadows la piensa como **una meseta sobre la cual el sistema puede jugar**: al perder resiliencia la meseta se encoge, los muros se vuelven más rígidos, y el sistema termina operando al filo. La pérdida llega como sorpresa porque el sistema estaba mirando su juego y no su espacio de juego. Un día hace algo que ha hecho cien veces y se cae.

La resiliencia se sacrifica todo el tiempo por productividad o estabilidad, que sí se ven. El inventario justo a tiempo bajó costos y volvió el sistema vulnerable a cualquier interrupción de combustible, tráfico o mano de obra.

**Autoorganización**: capacidad de crear estructura nueva, aprender, diversificarse. Es la forma más fuerte de resiliencia, porque un sistema que puede evolucionar sobrevive casi a cualquier cambio cambiándose a sí mismo. Surge de reglas simples. Requiere libertad, experimentación y cierto desorden, y por eso asusta a las estructuras de poder: fomentarla se siente como perder el control.

**Jerarquía**: subsistemas dentro de sistemas. Existe por una razón funcional, no decorativa: reduce la cantidad de información que cada parte tiene que seguir. La fábula de los relojeros Hora y Tempus: los sistemas complejos solo evolucionan desde sistemas simples si hay **formas intermedias estables**.

El principio que casi siempre está roto en las organizaciones: **las jerarquías evolucionan de abajo hacia arriba, y el propósito de las capas superiores es servir a las inferiores.** Cuando eso se olvida aparecen los dos males gemelos, la suboptimización y el exceso de control central.

---

## 8. Racionalidad acotada

De Herbert Simon, y es la idea que le quita el moralismo a todo el marco.

**La gente toma decisiones razonables con la información que tiene**, que es incompleta, tardía y sesgada hacia lo cercano. No somos optimizadores omniscientes sino satisfacedores: buscamos algo suficientemente bueno y seguimos.

La consecuencia operativa es fuerte: **sacar a un individuo de una posición de racionalidad acotada y poner a otro rara vez cambia algo.** Dentro de los límites de lo que esa persona puede ver y saber desde ese lugar del sistema, su conducta es razonable. Culpar al individuo casi nunca ayuda a producir un resultado mejor.

Lo que sí cambia las cosas es rediseñar la información, los incentivos, las metas y las restricciones que llegan a esa posición.

**El caso de los medidores holandeses**, que vale más que cualquier argumento: en un barrio cerca de Ámsterdam, casas idénticas, unas con el medidor eléctrico en el sótano y otras en el recibidor. Durante la crisis del petróleo se descubrió que las del recibidor consumían **un tercio menos**. Mismo precio, familias parecidas. La única diferencia era que la ruedita giraba donde la gente pasaba varias veces al día.

Ese es el modelo de una intervención sistémica buena: no cambió a la gente, cambió dónde llegaba la información.

Senge llega al mismo lugar por otra puerta con su ley 11: **no hay culpa**. Tú y el "otro" son parte de un mismo sistema.

**Cómo se usa esto cuando el usuario está enojado con alguien:** no lo contradigas. Pregúntale qué ve esa persona desde donde está sentada, qué la premian por hacer y qué información le llega y cuándo. Nueve de cada diez veces la conducta que parecía incompetencia o mala fe se vuelve legible, y ahí aparece la intervención real.

---

## 9. El bloque `comportamiento`: levantar el comportamiento en el tiempo

Este bloque va **antes** de dibujar estructura. La primera de las quince pautas de Meadows es "toma el pulso del sistema": antes de perturbarlo de cualquier manera, mira cómo se comporta.

Qué hacer, en orden:

1. **Pide la historia.** Qué viene pasando, desde cuándo, qué se intentó y qué pasó después de cada intento. Pregunta a quien lleve tiempo en el sistema.
2. **Consigue o construye datos en el tiempo.** Un Behaviour Over Time Graph (BOTG) es un gráfico simple de una variable contra el tiempo. Lo que importa es **la forma de la curva y los puntos donde cambia de dirección**, no la precisión de los números.
3. **Elige variables que puedan subir y bajar.** "Carga de trabajo del equipo" sirve; "el equipo" no. Incluye intangibles: la confianza, la moral y la reputación se grafican igual.
4. **Grafica varias juntas.** Lo interesante es cómo varían unas respecto de otras y con qué desfase. Ese desfase es un retraso y suele ser el hallazgo.
5. **Proyecta.** Si nada cambia, ¿hacia dónde va esta curva? Esa pregunta suele producir más movimiento que cualquier diagnóstico.

**Por qué esto importa tanto:** empezar por el comportamiento obliga a mirar hechos en vez de teorías, y evita el error más común, que es definir el problema por la ausencia de la solución favorita de alguien. "El problema es que necesitamos más gente" no es un problema, es una solución disfrazada. Meadows lo dice sin rodeos: la gente jura que la lluvia está bajando y al mirar los datos resulta que lo que subió fue la variabilidad.

---

## 10. El bloque `estructura`: construir el mapa

Con la historia en la mano, recién ahora se dibuja. La herramienta central es el Causal Loop Diagram (CLD), un mapa de relaciones de causa y efecto en círculo.

Cómo se hace bien:

1. **Acuerda la frontera primero.** Qué está dentro y qué fuera del mapa. Si no se hizo el bloque `frontera`, hazlo mínimamente acá (`frontera-y-perspectivas.md`).
2. **Variables específicas y modificables.** "Carga de trabajo del estudiante", no "estudiantes". Cada variable tiene que poder subir y bajar.
3. **Flechas de causalidad, no de correlación.** Cada flecha va marcada (`investigacion.md`).
4. **Signo en cada flecha.** Más (+) si las dos variables se mueven en la misma dirección, menos (-) si se mueven en direcciones opuestas.
5. **Cierra los ciclos y etiquétalos.** R para reforzador, B para balanceador. Un mapa sin ciclos cerrados no es un CLD, es un diagrama de causas.
6. **Marca los retrasos** sobre las flechas donde el efecto tarda. Al leer el diagrama en voz alta, agrega la palabra "eventualmente" al cruzar un retraso.
7. **Busca el arquetipo.** Con los ciclos a la vista, compara la estructura con los patrones conocidos (`arquetipos.md`). Encontrar el arquetipo es lo que convierte un dibujo en un diagnóstico, porque cada arquetipo ya trae dicho dónde está el apalancamiento.

**Poda sin culpa.** Si el mapa pasa de diez o doce variables, casi siempre es señal de que se están mezclando varias historias. Sepáralas o elige. Un diagrama que nadie puede contar en voz alta en dos minutos no le sirve a nadie.

**Alternativas al CLD según la situación**, todas en `metodos.md`: el Iceberg cuando lo que falta es bajar de eventos a estructura y modelos mentales; Connected Circles cuando hay muchas variables y todavía no se sabe cuáles importan; el Paper Computer de Vester cuando hace falta distinguir cuáles son palanca y cuáles son indicador; stocks y flujos cuando el problema es de acumulación y no de causalidad; el Viable System Model (VSM) cuando el problema es de estructura organizacional y no de dinámica.
