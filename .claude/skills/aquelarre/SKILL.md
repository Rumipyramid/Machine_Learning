---
name: aquelarre
description: Investigación de escritorio de 360° sobre un caso, lugar, leyenda o fenómeno paranormal, como base para escribir crónicas periodísticas. Corre en paralelo tres pistas que no se mezclan — 📜 Archivo (hemerotecas, expedientes, documentos de época), 🗣️ Voces (testimonios, folclor, foros, redes, TV) y 🔬 Escéptica (psicología anomalística, ciencia, investigación escéptica, explicaciones alternativas) — y deja un expediente del caso en `cronicas/expedientes/`, con cada fuente registrada en el grimorio (`cronicas/grimorio.md`). Activar SIEMPRE que el usuario invoque /aquelarre, o pida investigar, documentar o preparar una crónica sobre un caso paranormal, una casa embrujada, una aparición, un ovni, una leyenda urbana, un milagro, una maldición, un fantasma o cualquier relato sobrenatural, aunque no nombre el skill.
---

# Aquelarre — Investigación de escritorio para crónicas paranormales

## Propósito

El aquelarre es la versión de `/trinidad` para el oficio de cronista de lo paranormal. Junta
tres pistas sobre el mismo caso, las corre en paralelo y las consolida sin contaminarlas.

La pregunta de fondo **no es "¿es real el fantasma?"**. Es la pregunta del periodista:
**¿qué pasó, quién lo cuenta, desde cuándo, con qué pruebas, y qué explicaciones compiten?**
Lo sobrenatural se documenta como relato y como fenómeno social. No se afirma como hecho ni
se ridiculiza: se rastrea.

| Pista | Responde | Su criterio de validez |
|---|---|---|
| 📜 **Archivo** | ¿Qué consta por escrito, cuándo y dónde? | **Cercanía al hecho** (P1-P5): qué tan cerca en tiempo y origen está el documento del suceso. |
| 🗣️ **Voces** | ¿Quién lo cuenta, cómo cambió el relato, cuánto circula? | **Cadena de transmisión**: testigo directo identificado ≫ "le pasó a un amigo de un amigo"; más variantes datadas, más instalación social. |
| 🔬 **Escéptica** | ¿Qué explicaciones naturales hay y qué tan probadas están? | **Rigor metodológico** A-E (la misma rúbrica del códice). |

Los tres criterios miden cosas distintas. Nunca se promedian.

## Cuándo activarse

- El usuario invoca `/aquelarre` (con un caso, un lugar o una pregunta).
- Pide investigar o "documentar" un caso paranormal para una crónica, un reportaje o un guion.
- Pide rastrear el origen de una leyenda urbana o de un relato sobrenatural.

Si solo quiere una pista (p. ej. "¿qué explica la parálisis del sueño?"), usa solo esa pista y
dilo. Si la pregunta es puramente científica y no hay caso, `/seeker` basta.

## Metodología

### Paso 0: Revisar lo que ya existe

Antes de buscar, lee `cronicas/README.md` y busca el caso en `cronicas/expedientes/` y en
`cronicas/grimorio.md`. Si ya hay expediente, **amplíalo**: una fuente de verdad por caso.
Para la pista escéptica, consulta también `research/_nodes/fenomenos-psicologicos.md`
(estado de replicación de efectos psicológicos): si un efecto ya está marcado como no
replicado, no lo uses como explicación fuerte.

### Paso 1: Tipologizar el caso una sola vez

Identifica en una pasada qué es y qué necesita cada pista:

- **Tipo de caso**: lugar embrujado · aparición o entidad · ovni / luces · milagro o
  imagen religiosa · maldición o brujería · criatura (críptido) · posesión · predicción o
  vidente · leyenda urbana sin lugar fijo.
- **Núcleo verificable**: qué partes del relato *podrían* constar en un registro (un crimen,
  un incendio, una muerte, un dueño de la casa, una fecha, una nota de prensa, un expediente
  policial o judicial).
- **Época y geografía**: define qué archivos existen para ese periodo y lugar (Archivo
  General de la Nación, archivo arzobispal, procesos de la Inquisición de Lima, hemeroteca
  de la Biblioteca Nacional, registros públicos, diarios de época).
- **Hipótesis sobrenatural tal como se cuenta** y **2-4 hipótesis naturales candidatas**
  (psicológica, ambiental, histórica, fraude, error de percepción, malentendido, marketing).

### Paso 2: Lanzar las tres pistas en paralelo

Las tres pistas usan el mismo mecanismo de ancho de banda de `/seeker` y `/gossip`:
búsquedas simultáneas con expansión de términos (español, inglés, quechua si aplica;
variantes del nombre del lugar; nombres antiguos de calles), snowballing, rastreo por
autor/medio, clasificación de fuentes, chequeo de eco de cita y búsqueda adversarial.

#### 📜 Pista Archivo

- **Qué buscar**: prensa de época (hemerotecas digitalizadas, Google News Archive, archivos de
  diarios), expedientes policiales o judiciales publicados, partidas, catastro, actas
  municipales, documentos coloniales, fotografías con procedencia, libros de historia local.
- **Primera aparición datada**: el dato más valioso del expediente. ¿Cuál es el documento
  más antiguo que menciona el relato sobrenatural? Distínguelo del documento más antiguo que
  menciona el hecho real (la casa, la muerte, el incendio). La distancia entre ambas fechas
  suele contar la historia.
- **Contrastar el núcleo verificable**: ¿existió la persona? ¿ocurrió el crimen en esa fecha?
  ¿el edificio tenía ese uso? Cada dato queda como ✅ consta · ❌ contradicho · ❔ sin rastro.
- **Escala de cercanía al hecho** (se registra en el grimorio):

| Nivel | Qué es |
|---|---|
| **P1** | Documento primario contemporáneo al hecho: expediente, acta, partida, foto o grabación original con procedencia. |
| **P2** | Prensa de la época, o testimonio registrado poco después del hecho. |
| **P3** | Testimonio de primera mano, identificado, recogido después (entrevista, libro, documental). |
| **P4** | Recopilación o relato de segunda mano: libro de leyendas, programa de TV, nota retrospectiva. |
| **P5** | "Le pasó a un amigo de un amigo", anónimo o viral sin origen rastreable. |

#### 🗣️ Pista Voces

Aplica la metodología de `/gossip` (`.claude/skills/gossiper/SKILL.md`) adaptada:

- **Dónde**: Reddit (r/Paranormal, r/Peru, r/HighStrangeness, r/Glitch_in_the_Matrix), foros
  de misterio, YouTube y TikTok (canales de terror y "visitas nocturnas"), programas de TV,
  podcasts, comentarios de noticias, libros de leyendas, etnografías y estudios de folclor
  (p. ej. tradición oral andina y amazónica).
- **Árbol de variantes**: lista las versiones del relato con su fecha y medio. Qué elementos
  se agregan con el tiempo (nombres, muertes, cifras) y quién los agregó. Una leyenda que
  gana detalles con los años es un hallazgo, no un estorbo.
- **Testigos**: clasifica cada testimonio por cadena de transmisión (directo identificado,
  directo anónimo, indirecto, FOAF). No aceptes un testimonio como directo si solo lo cita
  un tercero.
- **Instalación social**: usa la escala de `/gossip` (🔥 alta · 🌡️ media · 💬 nicho · 🧊 nula)
  y marca si hay un pico atribuible a un medio, un programa o un video viral.
- **Ojo con el churnalism**: veinte notas que repiten el mismo reportaje de TV son una
  sola fuente.

#### 🔬 Pista Escéptica

Aplica la metodología de `/seeker` (`.claude/skills/seeker/SKILL.md`) a cada hipótesis
natural del Paso 1:

- **Fuentes**: psicología anomalística (parálisis del sueño, pareidolia, infrasonido,
  monóxido de carbono, sugestión, memoria reconstructiva, contagio social), física y
  geología del lugar, historia, investigaciones escépticas publicadas (Skeptical Inquirer,
  CSI, investigadores con método declarado) y parapsicología académica con su crítica.
- **Ajuste al caso**: una explicación general no basta. Di qué tan bien encaja con los
  detalles concretos del relato y qué detalles no explica.
- **Rigor A-E** con la rúbrica del códice; reporta revisión por pares y réplicas.
- **Búsqueda adversarial en ambos sentidos**: busca también lo que la explicación escéptica
  no logra explicar. El escepticismo flojo es tan mala crónica como la credulidad.

### Paso 3: Consolidar sin contaminar

- Nunca uses la viralidad como prueba de que ocurrió, ni un paper general como prueba de que
  en *este* caso fue eso.
- Si las tres pistas convergen (p. ej. el crimen nunca consta, la leyenda nace en un programa
  de TV de 1990 y el patrón calza con contagio social), dilo: es una conclusión fuerte.
- Si divergen (el hecho real consta, pero ninguna explicación natural encaja con lo que
  relatan varios testigos directos), reporta la tensión tal cual.

### Paso 4: Estado del caso

Cierra con un estado, nunca con "real / falso":

| Estado | Significa |
|---|---|
| 📂 **Documentado** | El núcleo del relato consta en registros cercanos al hecho; lo sobrenatural sigue siendo relato. |
| 🕯️ **Leyenda sin rastro** | No hay documento que respalde el núcleo; vive solo en la transmisión oral o mediática. |
| 🔦 **Explicación probable** | Una explicación natural encaja con los detalles y tiene buena evidencia. |
| 🧨 **Desmentido** | Hay evidencia directa de fraude, invención o error (el "hecho" no ocurrió, el autor lo admitió). |
| 🌀 **Abierto** | Testimonios directos y consistentes sin explicación que encaje. Se dice así, sin dramatizar. |

### Paso 5: Expediente del caso

Escribe o amplía `cronicas/expedientes/<caso-en-kebab-case>.md` siguiendo
`cronicas/expedientes/_plantilla.md`. Cita las fuentes por ID (`G-n`) del grimorio, no
completas. Actualiza la tabla de expedientes de `cronicas/README.md` (fecha, estado, versión).

El expediente no es la crónica. Es la mesa de trabajo: la crónica se escribe después, en
`cronicas/borradores/`, solo cuando el usuario la pida.

### Paso 6: Preparar el trabajo de campo

La investigación de escritorio termina en una lista accionable:

- Archivos que conviene visitar en persona (qué buscar, en qué fondo, qué fechas).
- Personas a entrevistar (por rol: vecino antiguo, guardián, historiador local, autor del
  primer reportaje), nunca con datos privados de contacto.
- Preguntas que solo el campo puede responder.
- Escenas posibles para la crónica (lugares, horas, objetos con carga narrativa).

### Paso 7: Registro en el grimorio

Registra todas las fuentes en `cronicas/grimorio.md` según el contrato del skill
`/grimorio` (`.claude/skills/grimorio/SKILL.md`): deduplica, asigna el siguiente `G-n`,
califica rigor A-E y, si la fuente es sobre el caso, su cercanía al hecho P1-P5. Indica la
pista de origen (archivo / voces / escéptica) en el resumen.

Las fuentes paranormales **no van al códice** (`research/fuentes/codice.md`): ese ledger
alimenta a Mu, al grafo y a las métricas del segundo cerebro de seguros y diseño. Excepción:
una fuente científica que sirva a ambos mundos (p. ej. un paper de psicología) puede estar en
los dos; en el grimorio se anota su `F-n` en la columna de referencia.

## Formato del reporte

1. **Resumen** (3-5 líneas): qué dice cada pista y el estado del caso.
2. **🧭 Línea de tiempo**: hecho real (si existe) → primera aparición del relato → hitos de
   difusión → hoy.
3. **📜 Archivo**: núcleo verificable (✅/❌/❔), documentos con su P1-P5.
4. **🗣️ Voces**: árbol de variantes, testigos por cadena, instalación social.
5. **🔬 Escéptica**: cada hipótesis natural con su rigor y su ajuste al caso.
6. **⚖️ Síntesis y estado del caso.**
7. **🎒 Para el campo**: archivos, entrevistas, preguntas, escenas.
8. **Límites**: qué no se pudo verificar desde el escritorio.

## Ética del cronista

- **Personas privadas**: no publiques nombres, direcciones ni datos de testigos o vecinos
  privados que no se expusieron ellos mismos. En el expediente se describen por rol.
- **Muertes reales**: muchas leyendas se apoyan en tragedias verdaderas. Las víctimas y sus
  familias se tratan con respeto; no se inventan detalles de su muerte para ganar efecto.
- **Lugares habitados**: si la casa "embrujada" es hoy una vivienda, no publiques la
  dirección exacta sin pensarlo: atrae visitas e intrusiones.
- **Salud mental y menores**: un relato de posesión o de visiones puede ser un cuadro clínico.
  No se diagnostica ni se expone a menores.
- **Nada se inventa**: ni fuentes, ni citas, ni testimonios. Si un dato no se encontró, el
  expediente dice "sin rastro". La crónica puede tener atmósfera; los hechos no se adornan.

## Anti-patrones

- Tratar la repetición del relato como prueba de que ocurrió.
- Cerrar el caso con una explicación de manual que no encaja con los detalles.
- Contar como independientes veinte notas que copian el mismo programa de TV.
- Omitir una pista sin decirlo.
- Escribir la crónica sin expediente: el estilo no reemplaza la investigación.
