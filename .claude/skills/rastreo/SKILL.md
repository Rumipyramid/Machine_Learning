---
name: rastreo
description: Razona una búsqueda antes de hacerla y usa los recursos de búsqueda según ese razonamiento. Parte de la decisión que la búsqueda alimenta y de lo que el segundo cerebro ya sabe, convierte los huecos en preguntas buscables, decide para cada una qué evidencia la respondería, dónde está, con qué herramienta y cuánto esfuerzo merece, diseña desde el inicio la búsqueda en contra, fija cuándo parar y deja una bitácora para no repetir barridos. Entrega un plan de rastreo y lo ejecuta (o lo reparte entre seeker, gossiper, marketer, trinidad y contexto-peruano). Úsalo cuando el usuario invoque /rastreo, pida "planifica la búsqueda", "¿qué y dónde buscamos?", "investigación de fuentes secundarias", "busca con criterio", o como primer paso de /trinidad, /seeker, /gossip o /marketer cuando el tema es amplio o caro de investigar.
---

# /rastreo — razonar la búsqueda antes de buscar

## Qué es

`/criterio` es cómo el segundo cerebro juzga la evidencia que tiene. `/rastreo` es el mismo razonamiento puesto
**antes** de buscar: qué falta saber, qué evidencia lo resolvería, dónde vive y cuánto vale el esfuerzo de
encontrarla. Evita los dos errores más caros de una investigación: buscar lo que ya se sabe y buscar sin saber qué
decisión se quiere mover.

Los skills de búsqueda (`seeker`, `gossiper`, `marketer`, `trinidad`, `contexto-peruano`) siguen siendo los que
ejecutan cada registro con su propio método. `rastreo` decide **qué les toca a cada uno y con qué presupuesto**, y
mantiene la memoria de qué se buscó.

## El procedimiento

### 1. Encuadrar: la decisión y el umbral

Escribe, antes de cualquier búsqueda:
- **La decisión que alimenta** la búsqueda y **quién la toma**.
- **Qué respuesta cambiaría esa decisión.** Si ningún resultado posible la cambia, la búsqueda no vale la pena o
  está mal planteada: dilo.
- **El plazo**: para cuándo hace falta. Define cuánto se puede gastar.
- **El umbral de suficiencia**: qué tendría que encontrarse para dar la pregunta por respondida. Por ejemplo:
  "una estadística oficial reciente", "al menos dos estudios causales independientes", "el filing del último año".

### 2. Inventario interno: qué sabe ya el cerebro

Aplica el paso 2 de `/criterio` (consultar `research/alma.md`, el tema fuente de verdad, el registro de fuentes y
`python research/grafo/papisa.py --tema "<palabras clave>"`). Con eso, clasifica lo que ya hay:

| Lo que ya hay | Qué se hace |
|---|---|
| 🟢 Documentado, vigente y aplicable al contexto | **No se busca de nuevo.** Se cita. |
| 🟢 Documentado pero en otro país, sector o época | Se busca **solo la transferencia**: ¿hay evidencia local o reciente? |
| 🟡 Plausible, mal probado | Se busca la prueba que falta, con el diseño que la resolvería |
| ⚔️ Evidencia en conflicto | Se busca **lo que desempata**: un moderador, una réplica, la fuente primaria |
| 🔴 Hype o huérfano de cita | Se rastrea su origen solo si alguien lo usará en una decisión |
| Hipótesis abierta del tablero | Se intenta mover de estado: es la búsqueda de mayor valor |
| Nada | Pregunta nueva: va completa al paso 3 |

Revisa también la **bitácora de búsquedas** del tema (su sección de bitácora o de iteraciones): qué se buscó antes,
con qué términos y qué salió. Un barrido que ya dio cero tres veces con términos distintos no se repite igual: se
cambia de registro, de idioma o de tipo de fuente, o se reporta como propiedad del campo.

### 3. Descomponer en preguntas buscables

Convierte cada hueco en una pregunta que una búsqueda pueda responder. Para cada una decide:

- **Tipo de afirmación**: hecho o cifra, efecto causal, tendencia, benchmark de negocio, percepción social, norma,
  o validez de una medición.
- **La evidencia ideal** que la respondería (tabla del paso 3 de `/criterio`).
- **Dónde vive esa evidencia**: el mapa de `references/mapa-de-fuentes.md`.
- **El registro que la ejecuta**: académico (`seeker`), social (`gossiper`), negocio (`marketer`), dato oficial
  peruano (`contexto-peruano`) o una lectura directa.

### 4. Asignar recursos según el valor de la pregunta

No todas las preguntas merecen el mismo esfuerzo. Puntúa cada una en tres ejes, alto, medio o bajo:

- **Peso en la decisión**: cuánto movería la decisión una respuesta u otra.
- **Incertidumbre actual**: qué tan poco sabe hoy el cerebro.
- **Costo de equivocarse**: qué pasa si se decide con un supuesto falso.

| Prioridad | Cuándo | Recursos |
|---|---|---|
| **1 · A fondo** | Peso alto e incertidumbre alta | Búsqueda en paralelo en todos los registros que apliquen, búsqueda extendida, lectura de fuentes primarias completas, snowballing, búsqueda adversarial completa |
| **2 · Dirigida** | Peso alto con incertidumbre media, o peso medio con incertidumbre alta | Un registro principal, búsqueda estándar, lectura de las dos o tres fuentes clave, una consulta adversarial |
| **3 · Verificación** | Solo hace falta confirmar o actualizar un dato | Una o dos búsquedas estándar hacia la fuente oficial o primaria |
| **4 · No se busca** | Peso bajo, o ya está 🟢 y vigente | Se cita lo que hay, o se anota como supuesto declarado |

**Cómo se usan las herramientas:**

- **Búsqueda estándar por defecto.** Se usa la extendida solo cuando la estándar vuelve pobre, fuera de foco o
  desactualizada, o desde el inicio para hechos de nicho, eventos muy recientes, precios y disponibilidad, o
  investigación de varios pasos. Las búsquedas independientes de una misma ronda se lanzan juntas.
- **Leer la fuente, no el resultado de búsqueda.** Toda cifra que se vaya a usar en una decisión se lee en su fuente
  primaria (WebFetch o PDF). Si no se pudo abrir, se marca "leída solo por resumen" y baja un escalón de confianza.
- **Agentes en paralelo** solo cuando hay dos o más registros con preguntas de prioridad 1 o 2 (el caso de
  `/trinidad`). Para una sola pregunta dirigida, buscar directo es más barato que lanzar agentes.
- **Lo interno antes que lo externo**: el registro de fuentes y los temas del cerebro se consultan siempre primero
  (son gratis y ya están juzgados).
- **Conectores privados** (Drive, correo, calendario) solo si el usuario lo pide para esa búsqueda.

### 5. Diseñar las consultas, incluida la que busca lo contrario

Para cada pregunta de prioridad 1 a 3, escribe antes de ejecutar:

- **Consultas semilla**, con expansión de términos: sinónimos, el término técnico y el coloquial, y los idiomas que
  correspondan (español del Perú, inglés para la literatura, portugués para Brasil).
- **Operadores** cuando ayuden: `site:` (dominio oficial o de la revista), `filetype:pdf` (informes y memorias),
  año o rango de fechas, comillas para cifras exactas.
- **Rutas de ampliación**: snowballing hacia atrás (qué cita la mejor fuente) y hacia adelante (quién la cita
  después), y rastreo por autor o por institución.
- **La consulta adversarial**, decidida desde el inicio y no al final: "<idea> no funciona", "<idea> replication",
  "<idea> failed", "crítica <idea>", "<empresa> pérdidas", "<empresa> denuncia". Una búsqueda sin su contraparte no
  está completa.

### 6. Ejecutar con disciplina

- **Clasificar cada fuente al llegar**, con los dos ejes de `/criterio`: rigor A-E y madurez de la afirmación.
- **Rastrear toda cifra espectacular** hasta su origen antes de seguir (puede ser eco de cita o huérfana).
- **Adaptar el plan sobre la marcha**: si una pregunta se resuelve antes de lo previsto, su presupuesto pasa a otra;
  si aparece una pregunta nueva de prioridad 1, entra al plan.
- **Parar a tiempo.** Una pregunta se cierra cuando ocurre cualquiera de estas cosas:
  1. se alcanzó el umbral de suficiencia del paso 1;
  2. hay saturación: dos rondas seguidas sin una fuente primaria nueva;
  3. tres barridos distintos dieron cero: se reporta como propiedad del campo, no como fracaso;
  4. se gastó el presupuesto de su prioridad.
- **Si una herramienta falla** (no abre páginas, no devuelve redes sociales), se dice en el reporte y se usa la ruta
  alternativa del mapa. Nunca se rellena el hueco con suposiciones.

### 7. Cerrar el rastreo

1. **Juzgar lo encontrado con `/criterio`** (pasos 3 a 6): madurez de cada respuesta, divergencias y lo que no se sabe.
2. **Confrontar el tablero**: qué hipótesis cambiaron de estado.
3. **Escribir la bitácora** del rastreo en el tema correspondiente: fecha, preguntas, dónde se buscó, consultas
   clave, qué cambió y qué quedó pendiente, **incluidos los resultados nulos**. Si no hay tema, la bitácora va al
   final del reporte.
4. **Registrar las fuentes** con `cronista` y persistir los hallazgos según Many Brains.
5. **Responder** con la conclusión primero y, al final, qué buscar en la siguiente vuelta.

## El entregable: el plan de rastreo

Antes de ejecutar algo de prioridad 1, o cuando el usuario lo pide, se muestra el plan:

| # | Pregunta | Decisión que mueve | Ya sabemos (estado y fuentes) | Evidencia ideal | Dónde buscar | Registro y herramienta | Consultas semilla y adversarial | Prioridad | Se cierra cuando… |
|---|---|---|---|---|---|---|---|---|---|

Debajo: el umbral de suficiencia, el plazo, qué se deja fuera a propósito y por qué.

Si el usuario no pidió ver el plan y la búsqueda es de prioridad 2 o menor, se puede ejecutar directo y mostrar el
plan resumido junto con el resultado.

## Reglas invariables

- **No se busca lo que el cerebro ya sabe con suficiente solidez.** Se cita.
- **Toda búsqueda tiene su búsqueda en contra**, diseñada antes de empezar.
- **Toda búsqueda tiene un criterio de parada.** Buscar más no es más rigor.
- **El resultado nulo se registra** en la bitácora, con dónde y cómo se buscó.
- **Las herramientas que fallaron se declaran.** Una pista débil se reporta como débil.
- **Los temas de clientes o confidenciales no se escriben en el repositorio público**: el plan y los hallazgos
  aplicados van al proyecto privado correspondiente, y las fuentes al registro solo con temas genéricos.
