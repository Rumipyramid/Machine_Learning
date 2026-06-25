---
name: seeker
description: Investigar afirmaciones, claims o preguntas factuales con un enfoque riguroso que abarca simultáneamente fuentes empíricas (papers, datos cuantitativos, estudios históricos) y fuentes teóricas/críticas/humanísticas (filosofía, teoría literaria, estudios culturales, historia de las ideas, autores canónicos). Activar SIEMPRE que el usuario pida investigar, verificar, refutar o profundizar en una afirmación; cuando use formulaciones como "qué tan cierto es", "investiga si", "revisa críticamente", "busca fuentes sobre", "es verdad que"; o cuando un tema pueda tener tanto evidencia empírica como una discusión teórica subyacente que cambie su interpretación. Incluye revisión crítica de metodología en papers científicos, reporta inconsistencias metodológicas detectadas, prioriza fuentes de los últimos 5 años pero incorpora fuentes más antiguas cuando tengan valor canónico o metodológico, y usa citas inline en formato (Autor, año) junto a las afirmaciones fuerza.
---

# Investigación de Espectro Amplio

## Propósito

Investigar afirmaciones combinando dos registros que normalmente se trabajan por separado:

1. **Registro empírico**: papers, datos cuantitativos, estudios históricos con evidencia documental, bases de datos, estadísticas oficiales.
2. **Registro teórico/crítico**: filosofía, teoría literaria, estudios culturales, historia de las ideas, autores canónicos cuya tesis sobre un tema es relevante incluso cuando no aporta "datos" en sentido estricto.

La falla más común al investigar es buscar en un solo registro. Una afirmación sobre alfabetización europea, por ejemplo, tiene tanto datos cuantificables (tasas históricas, censos, estudios demográficos) como una literatura teórica robusta (Kittler sobre la voz materna en el sistema de inscripción de 1800; Chartier sobre la privatización de la lectura; Ariès sobre la infancia y la familia) que **cambia la interpretación de esos datos**. Ignorar cualquiera de los dos lados produce una respuesta cojeada que parece rigurosa pero deja un flanco abierto.

Este skill existe para evitar esa cojera.

## Cuándo activarse

Activar este skill cuando el usuario:

- Pida investigar, verificar o refutar una afirmación específica.
- Use formulaciones como "qué tan cierto es", "investiga si", "revisa críticamente", "busca fuentes sobre", "es verdad que", "verifica X".
- Mencione una idea o afirmación que circula sin atribución clara (mitos populares, "datos curiosos", afirmaciones virales).
- Pida una revisión rigurosa de un tema con peso académico.
- Pregunte por evidencia detrás de un claim que parece simple pero puede tener una dimensión teórica subyacente.
- Compare versiones contrapuestas de un fenómeno cultural, histórico, científico o social.

## Metodología

### Paso 1: Tipologizar el claim antes de buscar

Antes de cualquier búsqueda, identifica explícitamente qué tipo de afirmación es. Un solo enunciado suele tener varias capas; identifica todas:

- **Empírico-cuantitativo**: hay números, tasas, fechas verificables ("la alfabetización fue del X%", "el efecto fue de d=0.4").
- **Empírico-cualitativo**: hay un fenómeno histórico/social descrito sin números ("las madres enseñaban a leer a sus hijos").
- **Causal**: une dos cosas con relación causa-efecto ("esto pasó porque...").
- **Teórico/interpretativo**: hace una lectura conceptual de un fenómeno (a menudo no explícito en la formulación original del claim).

**Pista crítica**: si el claim incluye un componente que parece "demasiado interpretativo" o "pensado de cierta manera" o tiene un giro psicológico/cultural/libidinal fuerte, casi seguro proviene de un autor teórico específico. Su omisión es lo que hará fallar la búsqueda.

### Paso 2: Mapear los registros relevantes

Para cada capa del claim, identifica al menos:

1. **¿Qué disciplina(s) empírica(s) abordan esto?** (historia social, demografía, estadística, epidemiología, sociología cuantitativa, etc.)
2. **¿Qué disciplina(s) teórica(s) tienen una tesis relevante?** (teoría de medios, filosofía de la educación, estudios culturales, psicoanálisis aplicado, historia de las mentalidades, etc.)
3. **¿Hay autores canónicos cuyo trabajo es referencia obligada en este tema?** Incluso si no los cita el claim, su tesis suele estar implícita en cómo se formula.

Ejemplos de mapeos teóricos que se suelen omitir:
- Cualquier tema sobre lectura, escritura o alfabetización → Kittler, Chartier, Darnton, Ong, McLuhan.
- Cualquier tema sobre infancia o familia premoderna → Ariès, Stone, Pollock.
- Cualquier tema sobre disciplina, instituciones o cuerpo → Foucault, Goffman, Elias.
- Cualquier tema sobre prácticas cotidianas → De Certeau, Bourdieu.
- Cualquier tema sobre comunidades imaginadas, nacionalismo → Anderson, Hobsbawm.

### Paso 3: Búsquedas en paralelo, no en serie

Lanzar búsquedas en al menos dos registros simultáneamente:

- **Búsqueda 1**: datos empíricos del fenómeno (papers, estudios, bases de datos, estadísticas).
- **Búsqueda 2**: bibliografía teórica/crítica relevante (autores, libros canónicos, debates conceptuales).
- **Búsqueda 3 (opcional pero recomendada)**: historia de la formulación del claim mismo — ¿de dónde viene esta frase exacta? A veces busca por una palabra clave inusual del claim revela al autor original.

Si encuentras una palabra o giro inusual ("aura erótica", "envoltura aural", "asimetría de cierre"), búscala literalmente entre comillas: suele delatar al autor que la acuñó.

### Paso 4: Clasificación de tipo de evidencia

Antes de evaluar la calidad, clasifica **qué tipo de evidencia** aporta cada fuente. Un mismo paper puede aportar más de un tipo; identifica todos:

| Tipo | Qué es | Peso epistémico | Ejemplo |
|---|---|---|---|
| **Meta-análisis / revisión sistemática** | Síntesis cuantitativa de múltiples estudios con criterios de inclusión explícitos | 🟢 Máximo (si bien hecho) | Cochrane review, Campbell review |
| **RCT** | Experimento con asignación aleatoria y grupo control | 🟢 Alto para causalidad | Safetxt trial (Michie et al.) |
| **Cuasi-experimental** | Intervención sin aleatorización completa (pre-post, diferencias en diferencias, RDD) | 🔵 Medio-alto | Evaluaciones de política pública |
| **Observacional / correlacional** | Mide asociaciones sin manipular variables (transversal, longitudinal, cohorte) | 🟡 Medio — no permite inferencia causal | Willmott et al. 2021 (R² de COM-B) |
| **Cualitativo** | Entrevistas, etnografía, análisis temático, fenomenología | 🟡 Medio — aporta profundidad, no generalización | Focus groups sobre percepción de seguros |
| **Estudio de caso** | Análisis profundo de un caso o N pequeña sin control | 🟠 Bajo para generalizar, alto para generar hipótesis | Caso de implementación en una empresa |
| **Reporte de industria / encuesta** | Datos de consultora o gremio con método parcialmente documentado | 🟠 Variable — depende de transparencia metodológica | McKinsey, Bain, Swiss Re, APESEG |
| **Teórico / ensayo argumentativo** | Marco conceptual, teoría, filosofía — sin datos empíricos propios | ⚪ No aplica "evidencia" en sentido empírico, pero puede ser canónico | Shove (2010), Foucault (1975) |
| **Opinión / editorial / blog** | Juicio sin método ni datos primarios | 🔴 Mínimo | Posts corporativos, notas de prensa sin fuente |

**En la respuesta**, marca el tipo de cada fuente clave al menos una vez, p. ej.: `(Willmott et al., 2021 — observacional transversal, N=582)`. Esto le da al usuario calibración instantánea sobre qué puede y qué no puede concluir de esa fuente.

### Paso 5: Revisión crítica de metodología (papers empíricos)

Cuando una fuente sea un paper científico o un estudio empírico, evaluar críticamente:

- **Tamaño y selección de muestra**: ¿N suficiente para el efecto detectado? ¿muestreo representativo o de conveniencia?
- **Diseño**: experimental, cuasi-experimental, observacional, narrativo, estudio de caso. ¿Permite el diseño la inferencia causal que el paper hace?
- **Controles**: ¿hay variables de control plausibles? ¿hay grupo de comparación?
- **Operacionalización**: ¿cómo definen y miden la variable de interés? Este es un punto crítico — por ejemplo, la "alfabetización" se mide históricamente por capacidad de firmar, lo cual subestima sistemáticamente la capacidad de leer (especialmente entre mujeres).
- **Replicación y meta-análisis**: ¿el hallazgo se ha replicado independientemente? ¿hay revisión sistemática?
- **Conflictos de interés y sesgos**: financiación, posicionamiento ideológico explícito del autor o la revista.
- **Interpretación vs. dato**: ¿las conclusiones que extrae el paper son lo que el dato realmente sostiene, o sobreinterpretan? Distinguir entre el hallazgo y la narrativa que el autor construye sobre él.
- **Pre-registro y p-hacking**: ¿es un análisis confirmatorio o exploratorio? ¿declara hipótesis a priori?

**Reportar al usuario cualquier inconsistencia metodológica** detectada, aunque la fuente sea ampliamente citada. Es información valiosa para que el usuario calibre el peso del hallazgo. Decir "este paper se cita mucho pero su N=24 y no tiene grupo de control" es más útil que solo citar la conclusión.

### Paso 6: Evaluación de validez y confiabilidad de los datos

Cuando una fuente reporta datos cuantitativos (cifras, escalas, índices, effect sizes), evaluar **dos dimensiones ortogonales**:

#### A) Validez — ¿mide lo que dice medir?

| Tipo de validez | Pregunta clave | Señal de alerta |
|---|---|---|
| **De constructo** | ¿El instrumento captura realmente el concepto teórico? | Escalas tipo Likert de autopercepción usadas como proxy de conducta real (ej. "¿qué tan capaz se siente de…?" ≠ capacidad objetiva). |
| **Interna** | ¿La relación encontrada es causal o hay explicaciones alternativas? | Diseño transversal que afirma causalidad; variables confusoras no controladas; sesgo de selección. |
| **Externa** | ¿Los resultados son generalizables más allá de la muestra? | Muestra WEIRD (Western, Educated, Industrialized, Rich, Democratic); N de conveniencia (solo universitarios); un solo país/contexto. |
| **Ecológica** | ¿Lo medido en laboratorio o encuesta refleja lo que pasa en la vida real? | Conducta autorreportada vs. observada; intención declarada vs. comportamiento real (el intention-behaviour gap). |
| **De criterio** | ¿El instrumento predice un outcome externo relevante? | Un cuestionario de "motivación" que no predice la conducta que dice explicar. |

**Aplicación práctica:** cuando un estudio reporta R² alto pero usa medidas autorreportadas para predictor Y outcome (como Willmott 2021 con COM-B), la **validez de constructo** y la **validez ecológica** están comprometidas — el R² captura parcialmente varianza de método común, no solo relación real entre variables.

#### B) Confiabilidad — ¿los datos son consistentes y reproducibles?

| Tipo de confiabilidad | Pregunta clave | Señal de alerta |
|---|---|---|
| **Consistencia interna** | ¿Los ítems de una escala miden lo mismo? (α de Cronbach, ω de McDonald) | α < 0.70 en escalas clave; α inflado artificialmente por ítems redundantes. |
| **Test-retest** | ¿Si mides dos veces, obtienes lo mismo? | Sin reporte de estabilidad temporal; constructos volátiles (ej. "motivación") medidos una sola vez. |
| **Inter-evaluador** | ¿Distintos evaluadores coinciden? | Codificación cualitativa sin kappa de Cohen; clasificaciones sin doble ciego. |
| **Replicabilidad** | ¿Otros investigadores obtienen resultados similares? | Hallazgo único sin replicación; campos con crisis de replicación conocida (psicología social, priming). |

**Cómo reportarlo:** cuando la validez o confiabilidad de un dato sean relevantes para la fuerza del claim investigado, incluir una **nota de calibración** junto a la cita. Formato:

> `(Autor, año — ⚠️ validez ecológica baja: conducta autorreportada, no observada)`
>
> `(Autor, año — ⚠️ sin replicación independiente; α de escala no reportado)`
>
> `(Autor, año — ✅ RCT pre-registrado, N=4.400, outcome conductual objetivo)`

La nota de calibración **no reemplaza** la cita inline `(Autor, año)` — la complementa. Usarla en las fuentes que el usuario necesita calibrar para tomar una decisión, no en todas.

#### C) Tabla resumen de rigurosidad de datos (para respuestas con múltiples fuentes)

Cuando una investigación use **3 o más fuentes empíricas**, cerrar la sección de evidencia con una tabla resumen de rigurosidad:

| Fuente | Tipo de evidencia | N | Validez | Confiabilidad | Peso para el claim |
|---|---|---|---|---|---|
| Autor, año | RCT / observacional / etc. | N=… | ✅/⚠️/❌ + nota | ✅/⚠️/❌ + nota | 🟢 Alto / 🟡 Medio / 🔴 Bajo |

Esto le da al usuario una **vista de portafolio** de la evidencia: no todas las fuentes pesan igual, y la tabla lo hace explícito de un vistazo.

### Paso 7: Recencia con override de calidad

**Priorizar** fuentes de los últimos 5 años porque:
- Reflejan el estado actual del debate.
- Suelen integrar revisiones críticas de hallazgos anteriores.
- Tienen mejor metodología en promedio (estándares más altos, mayor consciencia de problemas de replicación).

**Pero incluir** fuentes más antiguas cuando:
- Son la referencia canónica del campo y no hay forma de hablar del tema sin ellas (Kittler 1985, Foucault 1975, Ariès 1960, etc.).
- Tienen rigor metodológico superior a alternativas recientes.
- Son la fuente primaria del dato (un censo histórico, un estudio fundacional, una encuesta original).
- Marcan un debate aún vigente que no se ha desplazado.

Cuando uses una fuente antigua, justifica brevemente por qué la incluiste. Ejemplo: "(Ariès, 1960) — referencia canónica e ineludible para la historia de la infancia en Occidente, aún en debate."

## Formato de respuesta

### Citas inline

Junto a **afirmaciones fuerza** —datos cuantitativos, causas atribuidas, tesis interpretativas relevantes, evaluaciones críticas— coloca la cita en formato `(Autor, año)`. Ejemplos:

- "La alfabetización inglesa pasó del 30% en 1641 al 47% en 1696 (Cressy, 1980)."
- "La Madre se constituye como agente primario de la socialización lingüística alrededor de 1800 (Kittler, 1985)."
- "El método fonético en la enseñanza de la lectura fue introducido por Stephani como reforma pedagógica bávara (Kittler, 1985)."

Citar solo afirmaciones fuerza. No saturar el texto con citas en cada frase descriptiva o de transición.

Si una afirmación combina varias fuentes que convergen, listarlas: `(Houston, 2011; Buringh & Van Zanden, 2009)`.

Si dos fuentes están en tensión, marcarlo explícitamente: `(Schenda, 1970, sostiene ~15%; cf. Houston, 2011, para una visión más alta en Inglaterra)`.

### Estructura recomendada para investigaciones de claims

Para respuestas a investigaciones de afirmaciones específicas, organizar en este orden:

1. **Veredicto inicial breve** (1-3 líneas): qué tan cierto es el claim en términos gruesos. No demorar el dictamen.
2. **Lo que sí está documentado**: hechos sólidos, con citas.
3. **Lo que es interpretación o teoría**: afirmaciones que dependen del autor que las formula. Atribuir explícitamente.
4. **Lo que no cuadra o es falso**: inconsistencias, errores empíricos, sobreinterpretaciones, anacronismos.
5. **De dónde puede venir el claim**: hipótesis sobre el origen de la confusión, si aplica (es frecuente que un claim viral mezcle un dato real con una capa interpretativa que lo distorsiona).
6. **Limitaciones de la búsqueda**: qué quedó pendiente, qué tipo de fuente no se pudo verificar, qué requeriría acceso a bases de datos no disponibles.

### Honestidad epistemológica

- Si una búsqueda no encontró algo, decirlo explícitamente. No inferir evidencia ausente.
- Distinguir entre "no documenté esto en esta búsqueda" y "esto no existe".
- Cuando una tesis es de un autor específico, atribuirla. No presentarla como "consenso histórico" ni como dato neutro.
- Cuando un debate sigue abierto, presentar las posiciones. No imponer una.
- Si el usuario señala una fuente que se pasó por alto (como ocurrió con Kittler en esta sesión), reconocer el error explícitamente, integrar la fuente, y revisar las conclusiones que dependían de ella.

## Anti-patrones a evitar

- **Buscar solo en un registro**: si el claim huele a teoría (giros interpretativos, vocabulario cultural, marcos psicológicos sofisticados), no quedarse solo en papers empíricos. Y viceversa.
- **Tomar Wikipedia como fuente única**: usarla como punto de entrada, no como respaldo final de afirmaciones fuerza. Seguir las referencias hasta las fuentes primarias.
- **Confundir frecuencia con verdad**: que un dato circule mucho no lo hace correcto. Los "datos" virales de tasas de alfabetización son ejemplo clásico.
- **Aceptar el framing del claim**: a veces el claim mismo está mal formulado o mezcla capas (un dato falso con una teoría real). Reformular en términos correctos antes de responder.
- **Suavizar para no contradecir al usuario**: si la afirmación es falsa, decirlo. La honestidad es más útil que el acomodo. El usuario está pidiendo investigación, no validación.
- **Citar de memoria sin verificar**: las citas en formato (Autor, año) deben corresponder a fuentes efectivamente consultadas o ampliamente conocidas. No inventar atribuciones para dar apariencia de rigor.
- **Sobre-extender la teoría**: si Kittler aplica para el 1800, no extenderlo automáticamente al siglo XV. Cada tesis tiene su período y su dominio de aplicación.

## Ejemplo de aplicación

**Claim del usuario**: "La alfabetización europea pasó del 5% al 95% entre los siglos XVII y XVIII porque las madres se encargaron de enseñar a leer a sus hijos."

**Paso 1 — Tipologización**:
- Capa A: empírico-cuantitativo (los porcentajes 5% y 95%).
- Capa B: causal (el "porque").
- Capa C: empírico-cualitativo (las madres enseñando).
- Capa D (sospechada): tesis teórica subyacente — el rol de la madre en la alfabetización es una formulación característica de teoría de medios continental.

**Paso 2 — Mapeo de registros**:
- Empírico: historia social de la lectura, demografía histórica → Houston, Cressy, Buringh & Van Zanden, Chartier, Darnton, Schenda.
- Teórico: teoría de medios, historia cultural → Kittler (sistema de inscripción de 1800), Ong (oralidad/escritura), McLuhan.
- Histórico-pedagógico: reformas educativas → Stephani, Pestalozzi.

**Paso 3 — Búsquedas paralelas**:
- Tasas históricas de alfabetización europea XVI-XIX.
- Pedagogía doméstica y rol de la madre en la enseñanza temprana.
- Tesis canónicas sobre la madre como agente alfabetizador (Kittler específicamente).
- Origen literal del claim (búsqueda de la formulación textual).

**Paso 4 — Resultado estructurado con citas**:
1. Veredicto: el claim es empíricamente falso en los porcentajes y simplifica una tesis teórica real.
2. Documentado: la alfabetización inglesa pasó del 30% (1641) al 62% (1800) (Houston, 2011); en Europa central llegaba al 15% hacia 1770 (Schenda, 1970); las dame schools y la enseñanza materna existieron (Ariès, 1960).
3. Teoría real: Kittler (1985) sí argumenta que la Madre se constituye como agente primario de alfabetización hacia 1800, con una carga libidinal vía Lacan, anclada en la reforma fonética de Stephani.
4. Lo falso: los porcentajes 5%/95% no existen en ninguna fuente; el siglo es 1800, no XVII→XVIII; la causalidad simple ignora la imprenta, la Reforma, las escuelas de caridad.
5. Origen del claim: probable mezcla de Kittler (mal recordado) + cifras infladas de origen viral.
6. Limitaciones: no se accedió al texto alemán original de Kittler ni a series cuantitativas de archivos parroquiales primarios.
