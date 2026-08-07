# Arquitectura de Research Ops

> Descripción estructural del sistema de operaciones de investigación construido para el
> proyecto. Documento pensado para una audiencia externa: describe **capas y capacidades**,
> no herramientas ni implementación.
> 2026-08-05

---

## El problema que resuelve

La investigación aplicada en una organización suele fallar por las mismas cuatro razones,
ninguna de ellas técnica:

1. **El conocimiento no sobrevive.** Un hallazgo vive en un deck, en un hilo de chat o en la
   cabeza de quien investigó. Seis meses después nadie sabe de dónde salió una cifra.
2. **Todas las fuentes pesan igual.** Un paper con revisión por pares y un dato de un blog
   comercial terminan citados con la misma autoridad en la misma lámina.
3. **La evidencia se mezcla.** Un número de tracción en redes se usa para respaldar una
   afirmación causal; un caso de negocio se cita como si fuera un estudio.
4. **Nada obliga a buscar lo que contradice la tesis.** Se investiga hasta confirmar, no
   hasta poner a prueba.

La arquitectura que sigue está diseñada específicamente contra esos cuatro fallos. Cada capa
existe para cerrar uno de ellos.

---

## Vista general: seis capas y una capa de gobierno

```
                          ┌─────────────────────────────┐
   Evidencia externa ───▶ │  1 · ADQUISICIÓN            │  Tres registros paralelos
   (papers, mercado,      │     de evidencia            │  que nunca se mezclan
    conversación social)  └──────────────┬──────────────┘
                                         ▼
                          ┌─────────────────────────────┐
                          │  2 · CALIFICACIÓN Y          │  Toda fuente entra al registro
   Documentos internos ─▶ │     REGISTRO                 │  con grado de rigor explícito
   de la organización     └──────────────┬──────────────┘
                                         ▼
                          ┌─────────────────────────────┐
                          │  3 · CONSOLIDACIÓN           │  Un tema = una sola
                          │     del conocimiento         │  fuente de verdad
                          └──────────────┬──────────────┘
                                         ▼
                          ┌─────────────────────────────┐
                          │  4 · SIMULACIÓN              │  La audiencia, modelada
                          │     de audiencia             │  y calibrada contra dato real
                          └──────────────┬──────────────┘
                                         ▼
                          ┌─────────────────────────────┐
                          │  5 · CRITERIO acumulado      │  Tesis de negocio con
                          │     de negocio               │  confianza declarada
                          └──────────────┬──────────────┘
                                         ▼
                          ┌─────────────────────────────┐
                          │  6 · PRODUCCIÓN              │  Entregables que citan
                          │     de entregables           │  su origen
                          └─────────────────────────────┘

   ═══════════════════════ 0 · GOBIERNO ═══════════════════════
   Reglas transversales que mantienen la coherencia de todas las capas
```

**Escala actual del sistema:** 468 fuentes registradas y calificadas · 15 dominios de
conocimiento consolidados · 25 tesis de negocio vivas · un modelo de audiencia sintética
calibrado · ciclos de revisión automatizados.

---

## Capa 1 · Adquisición de evidencia

**Qué es.** El mecanismo por el que entra evidencia nueva al sistema. No es "buscar en
internet": es un protocolo con tres registros de evidencia que operan **en paralelo y sin
mezclarse**, porque cada uno mide una cosa distinta y se valida con un criterio distinto.

| Registro | Qué busca | Cómo se mide su validez |
|---|---|---|
| **Empírico / teórico** | Literatura académica, estudios, marcos conceptuales, teoría crítica | Rigor metodológico: diseño del estudio, tamaño de muestra, revisión por pares verificada (no asumida) |
| **Social / mediático** | Qué se dice en foros, redes, prensa, reseñas de consumidores | Frecuencia de cobertura y validación entre personas reales — no rigor académico |
| **De negocio** | Desempeño comercial y financiero publicado: resultados, participación de mercado, financiamiento | Que el resultado sea **publicado y verificable**, no opinión sobre cómo "parece" irle a alguien |

**Qué resuelve.** El fallo n.º 3: la mezcla de evidencia. Un dato de tracción social jamás
respalda una afirmación causal, y un caso de negocio nunca se presenta como estudio. Cuando
los tres registros **convergen**, eso se declara como señal fuerte. Cuando **divergen**, la
tensión se reporta tal cual — no se promedia ni se resuelve artificialmente.

**Capacidad distintiva: búsqueda adversarial obligatoria.** Antes de cerrar cualquier
veredicto, el protocolo exige buscar activamente lo que lo contradice: el fracaso además del
caso de éxito, la señal de problema además de la cifra favorable. Si no aparece nada
contrario, eso también se declara — "se buscó y no apareció" es una afirmación distinta y más
fuerte que el silencio.

**Capacidad distintiva: detección de eco de cita.** Antes de contar tres notas de prensa como
tres confirmaciones, se verifica si las tres citan el mismo comunicado original. Si es así,
es **una** fuente con tres altavoces, y se reporta como tal.

---

## Capa 2 · Calificación y registro de evidencia

**Qué es.** Un registro único y acumulativo donde **toda** fuente referenciable queda anotada
antes de poder ser citada. Cada entrada lleva: identificador estable, autoría, año, título,
resumen de lo que aporta, **grado de rigor en una escala explícita**, qué afirmación sustenta,
y la referencia original.

**El grado de rigor es la pieza central.** Cada fuente se califica en una escala de cinco
niveles — desde dato primario auditado (un estado financiero regulado, un ensayo aleatorizado
con revisión por pares) hasta cifra sin metodología verificable (un ranking viral, un
comunicado promocional). El grado viaja pegado a la fuente para siempre.

**Qué resuelve.** El fallo n.º 2: que todas las fuentes pesen igual. Cualquiera puede tomar
una cifra del sistema y ver, en el mismo renglón, **cuánto puede apoyarse en ella**. Una
afirmación sostenida por una fuente del nivel más bajo no es inutilizable — es utilizable
*con esa etiqueta encima*.

**Capacidades adicionales:**

- **Marcado de fuentes vetadas.** Una cifra que circula en la industria pero no tiene método
  verificable se registra explícitamente como "no usar", con la razón. Así no vuelve a
  colarse en un documento por la puerta de atrás.
- **Anotación de advertencias.** Una fuente puede entrar con salvedades pegadas: "la
  definición de esta métrica no es estándar y no es comparable con la de otros", "esta cifra
  se recuperó de forma indirecta, revalidar antes de publicar".
- **Índice temático.** Con cientos de fuentes, un índice agrupa rangos de identificadores por
  dominio, de modo que la búsqueda no dependa de recordar un número.
- **Custodia de documentos internos.** Los documentos primarios de la organización
  (materiales de campo, análisis internos, presentaciones) se preservan íntegros dentro del
  sistema, no solo se resumen — para que un análisis posterior pueda volver a la fuente en vez
  de al resumen de alguien.

---

## Capa 3 · Consolidación del conocimiento

**Qué es.** La capa donde la evidencia dispersa se convierte en conocimiento estructurado. Su
regla constitutiva es **un tema, una sola fuente de verdad**. Cuando llega evidencia nueva
sobre un tema que ya existe, se amplía el documento existente; no se crea uno paralelo.

**Estructura.** Un espacio plano de documentos temáticos —sin jerarquía de carpetas— más dos
mecanismos de navegación:

- Un **índice vivo** que registra qué documentos están vigentes, cuándo se actualizó cada uno
  y qué entregables dependen de cuáles.
- **Enlaces recíprocos** entre documentos: si A referencia a B, B referencia a A. La
  navegación la dan las relaciones declaradas, no la ubicación en un árbol de carpetas.

**Reglas de integridad:**

- **Las fuentes se citan por identificador**, nunca se copia la referencia completa. Corregir
  una fuente en el registro corrige automáticamente todo lo que la cita.
- **Se versiona solo por cambio de fundamento** — un cambio de premisa, de modelo o de
  alcance. Una ampliación incremental solo actualiza la fecha. Esto evita el ruido de
  versiones que no significan nada.
- **Nada se borra.** Si un documento queda obsoleto, se declara obsoleto; no desaparece.
- **Cada documento declara sus propias limitaciones**: qué registro de evidencia quedó débil,
  qué no se pudo verificar, qué queda fuera de alcance.

**Qué resuelve.** El fallo n.º 1: que el conocimiento no sobreviva. Un hallazgo de hace seis
meses sigue estando donde debe, con sus fuentes, su fecha y sus salvedades intactas.

---

## Capa 4 · Simulación de audiencia

**Qué es.** Un modelo de la población objetivo que permite generar cohortes sintéticas y
someterlas a preguntas antes de salir a campo. No es un generador de perfiles inventados: es
un modelo **calibrado**, cuyas distribuciones reproducen datos reales de fuentes oficiales y
de la propia base de evidencia del sistema.

**Qué permite hacer:**

- Generar una población con la composición exacta que interesa (rango etario, nivel
  socioeconómico, geografía, canal, etc.).
- Someterla a un cuestionario y obtener distribuciones de respuesta y cortes por segmento.
- **Estresar un guion de entrevista antes de campo**: descubrir en la simulación que una
  pregunta está mal formulada, que un filtro excluye al segmento equivocado o que hay una
  objeción predecible sin guionar — antes de gastar sesiones reales averiguándolo.

**Capacidades de integridad — lo que separa esto de inventar números:**

- **Reproducibilidad.** Cada ejecución se ancla a una semilla; la misma semilla produce
  exactamente la misma población. Cualquiera puede reproducir el ejercicio.
- **Validación contra realidad.** Existe un mecanismo que compara las distribuciones simuladas
  contra sus objetivos reales y falla si se desvían fuera de tolerancia. Si una regla de
  simulación produce un resultado fuera del rango documentado, se recalibra — y la
  recalibración queda registrada.
- **Distinción explícita entre dato y supuesto.** Cada variable declara si viene de un dato
  calibrado o de un supuesto razonado. Cuando una pregunta exige una variable que el modelo no
  tiene, se declara el sustituto usado y se marca como el eslabón débil del ejercicio.
- **Límite declarado.** El sistema afirma explícitamente que estos datos sirven para
  prototipar, explorar hipótesis y afinar instrumentos — **no** para sustituir investigación
  con personas reales ni para probar relaciones causales.

---

## Capa 5 · Criterio acumulado de negocio

**Qué es.** La capa que traduce evidencia en juicio. Mantiene un conjunto de **tesis de
negocio vivas** — afirmaciones sobre dónde hay oportunidad y dónde hay riesgo — cada una
atada a las fuentes que la sostienen y con un **nivel de confianza declarado**.

**Lo que la hace distinta de un documento de conclusiones:**

- **Separa dato de intuición.** Lo que se apoya en evidencia registrada se cita por
  identificador. Lo que es razonamiento propio sin fuente detrás va marcado como tal,
  explícitamente. Ambas cosas pueden ser útiles; confundirlas no.
- **Techos de confianza explícitos.** Una tesis puede llevar una restricción del tipo: "esta
  afirmación no sube de confianza media *por consistencia narrativa* — solo sube si aparece
  una fuente de rigor superior que la confirme". Impide que una idea se vuelva verdad por
  repetición.
- **Refinamiento periódico.** El criterio se revisa contra el registro de evidencia en ciclos
  regulares. Cuando entra evidencia nueva, las tesis se ajustan; cuando no entra nada, se
  declara "sin cambios sustanciales" en vez de fabricar un matiz para justificar la revisión.
- **Bitácora de decisiones.** Cada revisión deja registro de qué cambió y por qué —
  incluyendo cuando lo que cambió fue un error propio del sistema.

**Capacidad distintiva: el criterio puede corregirse a sí mismo.** En un caso documentado, el
ciclo de revisión estuvo leyendo una ubicación desactualizada del registro de evidencia y
reportó "sin novedad" durante siete revisiones consecutivas mientras la base real crecía. Al
detectarlo, la corrección quedó anotada en la bitácora como riesgo de proceso, no se borró.

---

## Capa 6 · Producción de entregables

**Qué es.** La capa de salida. Convierte conocimiento consolidado en documentos para consumo
humano: informes, presentaciones, resúmenes ejecutivos, materiales de campo.

**Reglas:**

- **Todo entregable declara sobre qué conocimiento se construyó**, con fecha de la versión
  usada.
- **Los entregables tienen estado.** Cuando cambia un documento de conocimiento del que
  dependen, quedan marcados como "requiere actualización". No hay entregables huérfanos
  circulando sin que nadie sepa si siguen siendo válidos.
- **Registro de audiencia y registro de precisión son distintos.** El mismo hallazgo puede
  producir una versión técnica completa —con todas las tablas, salvedades y trazabilidad— y
  una versión en lenguaje claro para audiencia no especialista. Ambas se derivan del mismo
  origen; ninguna es un resumen informal de la otra.

---

## Capa 0 · Gobierno (transversal)

Reglas que no pertenecen a ninguna capa porque sostienen todas:

**Trazabilidad completa.** Cualquier cifra en cualquier entregable se puede rastrear hasta su
fuente original y su grado de rigor. Sin excepciones.

**Incertidumbre explícita, nunca implícita.** El sistema está construido para hacer visible lo
que no sabe: grados de rigor en las fuentes, niveles de confianza en las tesis, marcas de
"supuesto" en el modelo de audiencia, secciones de limitaciones obligatorias en cada
documento.

**Las contradicciones se reportan, no se promedian.** Si la evidencia académica apunta a un
lado y la de negocio al otro, eso es un hallazgo, no un problema de redacción.

**Los vacíos se declaran.** "Se buscó y no se encontró evidencia" es un resultado que se
escribe, no un silencio. Igual que "esta pregunta no se pudo responder y por qué".

**Reproducibilidad.** Los ejercicios cuantitativos se anclan a semillas y sus scripts se
versionan junto con sus resultados.

**Memoria institucional por diseño.** El sistema está construido para que el conocimiento
sobreviva a la sesión, al proyecto y a la persona que investigó.

---

## Capacidades que emergen de la arquitectura

Ninguna de estas vive en una capa concreta: aparecen porque las capas están conectadas así.

| Capacidad | Qué permite en la práctica |
|---|---|
| **Investigación de 360° sin contaminación** | Ver un tema desde evidencia académica, conversación social y desempeño de negocio a la vez, manteniendo separado lo que cada una puede probar |
| **Validación externa de hallazgos internos** | Tomar un análisis interno de la organización y contrastarlo contra literatura y benchmarks externos para saber si es normal, excepcional o anómalo |
| **Prueba de instrumentos antes de campo** | Detectar problemas de un cuestionario o un filtro en simulación, antes de gastar sesiones reales |
| **Auditoría de afirmaciones heredadas** | Tomar un material ya en uso en la organización y verificar, afirmación por afirmación, cuáles tienen respaldo real y cuáles no |
| **Acumulación entre proyectos** | Un hallazgo levantado para un proyecto queda disponible y citable para el siguiente, con su rigor intacto |
| **Detección de deriva** | Cuando el modelo de audiencia se desvía de la realidad documentada, el sistema lo detecta y obliga a recalibrar |

---

## Lo que esta arquitectura no hace

Declarado explícitamente, porque un sistema que no dice sus límites no es confiable:

- **No sustituye investigación con personas reales.** La simulación de audiencia afina
  instrumentos y explora hipótesis; no reemplaza el campo.
- **No prueba causalidad.** Ninguna capa está diseñada para inferencia causal.
- **No mejora la calidad de la evidencia disponible.** Si sobre un tema solo existe evidencia
  débil, el sistema lo hará visible — pero no la vuelve fuerte.
- **No decide.** Produce criterio con confianza declarada; la decisión sigue siendo humana.

---

*Documento estructural. Describe capas y capacidades, no implementación.*
