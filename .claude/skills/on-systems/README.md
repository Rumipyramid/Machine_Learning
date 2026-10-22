# on-systems

Skill de [Claude Code](https://claude.com/claude-code) que actúa como socio de pensamiento sistémico. Co-construye con el usuario, en español y una decisión a la vez, el análisis y la intervención en un sistema complejo, combinando el repertorio de métodos de Christian Baron (*Methods for Systems Thinking*), la dinámica de Donella Meadows (*Thinking in Systems*) y los arquetipos y modelos mentales de Peter Senge (*The Fifth Discipline*).

Sirve para el problema que vuelve. Ese que ya se intentó resolver dos o tres veces, que mejora un rato y reaparece, y donde la sensación es que cada arreglo genera el siguiente problema.

## Cómo procede el skill

**Propone, el usuario decide.** En cada elección: explica en lenguaje llano qué se decide y por qué importa, pregunta lo que solo el usuario sabe, propone opciones con su razonamiento y una recomendación, espera la decisión, y recién entonces la registra y avanza.

**Nunca propone un framework sin explicar por qué ese.** Es una guía, no un dispensador de plantillas. Cada método viene con la razón por la que se propone ese y no otro, y las siglas van siempre desplegadas la primera vez.

Toda sesión arranca con un **Paso 0 obligatorio**: diagnóstico de la situación y una ruta de trabajo acordada explícitamente antes de tocar cualquier framework.

Y una diferencia importante con otros skills de marco: **este dominio no es una secuencia obligatoria**. Baron organiza sus métodos para que uno entre por donde su situación lo pide y se mueva hacia adelante y hacia atrás. El Paso 0 diagnostica y propone un punto de entrada, no un temario. Los bloques que la ruta no toca quedan marcados como fuera de alcance, con su razón registrada, y no bloquean la compilación del documento final.

## Qué frameworks maneja

**De Christian Baron**, como columna vertebral operativa:

- **La estructura 5M**: Motivate, Meet, Map, Make, Manage. Cinco categorías de trabajo con un criterio de selección, no un proceso lineal.
- **Los cinco criterios de selección de método**: tipo de problema (relojes y nubes, de Popper), propósito, personas, recursos y evidencia.
- **El catálogo de 65+ métodos**, distinguiendo los que el skill puede conducir en conversación de los que necesitan una sala y un grupo.

**De Donella Meadows**, como núcleo dinámico:

- **Stocks y flujos**, ciclos de retroalimentación reforzadores y balanceadores, retrasos, no linealidad, dominancia cambiante.
- **Resiliencia, autoorganización y jerarquía**, y por qué las tres se sacrifican sin darse cuenta.
- **Racionalidad acotada**: por qué cambiar a la persona en una posición casi nunca cambia el resultado.
- **Los doce puntos de apalancamiento**, con el razonamiento de por qué cada uno está donde está, y las advertencias sobre dirección y resistencia.

**De Peter Senge**, acotado a tres aportes:

- **Los diez arquetipos de sistemas**, cada uno con su síntoma de alerta temprana y dónde está el apalancamiento, reconciliados con las ocho trampas de Meadows.
- **Los tres niveles de explicación**: eventos, patrones y estructura, y la postura que produce cada uno.
- **Las cuatro herramientas de modelos mentales**: Espoused Theory frente a Theory-in-Use, Leaps of Abstraction, The Left-Hand Column, y Balancing Inquiry and Advocacy.

**De la tradición crítica**, incrustado donde corresponde en vez de como sección aparte: el Boundary Critique de Ulrich y Midgley y las doce preguntas de Critical Systems Heuristics (CSH) en el bloque de frontera; CATWOE (Customers, Actors, Transformation, Worldview, Owners, Environmental constraints) de Checkland en el de actores.

El skill usa las **versiones vigentes** de los marcos, no las publicadas primero. Cynefin va con el dominio aporético y las zonas liminales que Snowden incorporó desde 2021, no con los cinco dominios clásicos. La Certainty/Agreement Matrix se usa solo como aparato de conversación, porque Stacey mismo la repudió. Y los puntos de apalancamiento incluyen el agrupamiento en cuatro dominios de Abson y colegas (2017), atribuido a ellos y no a Meadows.

## Estructura del proyecto

```
on-systems/
├── SKILL.md                          proceso, Paso 0, bloques, cierre y verificación
└── references/
    ├── conceptos.md                  el núcleo dinámico
    ├── arquetipos.md                 los diez patrones que se repiten
    ├── apalancamiento.md             los doce puntos y dónde intervenir
    ├── metodos.md                    el catálogo 5M y cómo elegir
    ├── frontera-y-perspectivas.md    frontera, actores y modelos mentales
    ├── investigacion.md              protocolo de evidencia y deep research
    └── entregable.md                 arquitectura del entregable modular
```

`SKILL.md` mantiene el proceso liviano y apunta a la referencia que corresponde a cada bloque. Ningún archivo copia contenido de los libros fuente: son síntesis y reformulación propia, con citas puntuales atribuidas.

## Cómo estructura el entregable

En vez de un documento monolítico que crece sin control, el skill construye el análisis en secciones separadas dentro de la carpeta de trabajo del usuario, una por cada módulo que hay que decidir. Estos son los diez, más dos anexos, con lo mínimo de cada uno; el detalle completo y el criterio de calidad de cada sección viven en `references/entregable.md`:

- **Propósito.** Por qué intervenir y qué se busca, incluida la pregunta de quién se beneficia del statu quo.
- **Frontera.** Qué queda dentro y fuera del sistema, y la crítica de esa elección.
- **Actores.** Quiénes son, cuánto poder tienen, y cómo se ve el sistema desde donde está cada uno.
- **Comportamiento.** La historia del sistema en el tiempo, antes de teorizar su estructura.
- **Estructura.** El mapa causal: ciclos, retrasos y el arquetipo si aparece uno.
- **Modelos mentales.** Los supuestos que hacen parecer razonable la estructura actual.
- **Apalancamiento.** Dónde intervenir, con la dirección explícita en que se empuja.
- **Intervenciones.** Qué se prueba, a qué escala y en qué plazo.
- **Riesgos.** Consecuencias no buscadas de las intervenciones elegidas.
- **Indicadores.** Qué se mira, con qué frecuencia, y qué gatillaría revisar el análisis.
- **Métodos aplicados** *(anexo)*. Qué método se usó en cada bloque y por qué.
- **Arquetipos identificados** *(anexo)*. Cada arquetipo con la evidencia que lo sostiene.

Esos doce módulos viven junto a un índice y a tres registros transversales:

```
[carpeta de trabajo]/
├── index.md                     mapa de estado y dependencias entre secciones
├── inbox/                       para dejar contexto o resultados de talleres, se procesa y se vacía
├── secciones/                   los doce módulos, cada uno con su frontmatter de estado
├── evidencia.md                 cada dato marcado como verificado o como supuesto
├── bitacora-de-decisiones.md    registro cronológico, append-only
├── lecciones.md                 correcciones del usuario convertidas en reglas
└── intervencion-sistemica.md    el documento final, compilado solo al cerrar
```

Cada sección lleva un frontmatter (`estado`, `version`, `depende_de`) que la ubica en un grafo de dependencias declarado en un solo lugar. Antes de escribir cualquier sección, el skill relee de qué depende y qué depende de ella para detectar contradicciones y alertarlas **antes** de escribir.

### Las cuatro flechas de retorno

El grafo no es una cadena sino un ciclo: cuatro dependencias corren hacia atrás, cada una con su disparador. **Apalancamiento → frontera**, cuando la palanca principal queda fuera del encuadre. **Modelos mentales → propósito**, cuando el propósito revelado no es el declarado. **Riesgos → intervenciones**, cuando una consecuencia mata o cambia lo propuesto. **Indicadores → comportamiento**, cuando el sistema se movió distinto de lo previsto. El disparador y la fuente de cada una están en `references/entregable.md`.

### Los métodos que necesitan una sala

Buena parte del repertorio de Baron son dinámicas presenciales que un skill de conversación no puede conducir. El circuito es de ida y vuelta: el skill recomienda el taller con su brief, dice qué tiene que volver y en qué forma, y procesa el resultado por el `inbox/`. Si no hay tiempo o equipo, **avanza igual**: co-construye el bloque con lo que el usuario sí sabe, marcando esa parte como supuesto y no como dato verificado.

## Instalación

**A nivel de proyecto** (disponible solo en el repo donde lo instalas):

```bash
git clone https://github.com/jlatorree/on-systems.git .claude/skills/on-systems
```

**A nivel global** (disponible en cualquier proyecto):

```bash
git clone https://github.com/jlatorree/on-systems.git ~/.claude/skills/on-systems
```

Para actualizar a la última versión, entra a la carpeta del skill instalado y corre `git pull`.

## Uso

El skill dispara cuando el usuario quiere entender por qué un problema se repite pese a los intentos de resolverlo; mapear un sistema, sus actores y sus dinámicas; decidir dónde intervenir para que el cambio dure; anticipar consecuencias no deseadas; diagnosticar por qué una solución no pega o genera resistencia; o hacer seguimiento y adaptar una intervención en curso. Aplica aunque no mencione "sistema", "pensamiento sistémico" ni ningún framework.

## Fuentes

- Christian Baron, *Methods for Systems Thinking: 65+ Practical Approaches for Exploring Systems, Perspectives, and Complexity* (Routledge, 2026).
- Donella H. Meadows, *Thinking in Systems: A Primer*, editado por Diana Wright (Chelsea Green, 2008).
- Peter M. Senge, *The Fifth Discipline: The Art and Practice of the Learning Organization*, edición revisada (Currency, 2006).

Y para las versiones vigentes de los marcos que los libros presentan en versiones anteriores:

- David J. Abson et al., ["Leverage points for sustainability transformation"](https://link.springer.com/article/10.1007/s13280-016-0800-y) (*Ambio*, 2017), para el agrupamiento de los doce puntos en cuatro dominios.
- Gerald Midgley, ["The Systemic Intervention Approach"](https://www.scienceopen.com/hosted-document?doi=10.54120/jost.000050) (*Journal of Systems Thinking*, 2023), para el Boundary Critique como punto de partida.
- Dave Snowden, [Cynefin St David's Day 2021](https://thecynefin.co/cynefin-st-davids-day-2021-1-of-3/), para el dominio aporético y las zonas liminales.
- Peter Senge, Hal Hamilton y John Kania, ["The Dawn of System Leadership"](https://ssir.org/pdf/Winter_2015_The_Dawn_of_System_Leadership.pdf) (*Stanford Social Innovation Review*, 2015), para la versión condensada del marco de Senge posterior a la edición de 2006.

Este repositorio no incluye los libros fuente ni reproduce su texto: contiene una síntesis y reformulación original con fines de referencia operativa.
