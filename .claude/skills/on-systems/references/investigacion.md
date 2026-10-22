# Investigación: cómo enriquecer cada bloque con evidencia

La consigna es **suficiencia, no exhaustividad**. El objetivo no es saber todo sobre el sistema: es saber lo justo para poder dar el paso siguiente con fundamento. Un exceso de información satura y retrasa la decisión.

Antes de buscar cualquier cosa, la pregunta es siempre la misma: **¿qué decisión depende de este dato, y qué haría distinto según cómo salga?** Si la respuesta es "nada", no lo busques.

---

## 1. Acordar el modo, en el Paso 0

Tres modos, y el usuario elige. Puede cambiar entre bloques.

| Modo | Cuándo conviene | Qué haces |
|---|---|---|
| **Búsqueda directa** | Datos públicos y verificables: cómo funciona el sistema en otros lugares, qué se ha publicado sobre intervenciones parecidas, series de tiempo disponibles, marco regulatorio. | Buscas con tu herramienta y traes el hallazgo con fuente. |
| **Prompt de deep research** | Hace falta profundidad, o cobertura de literatura académica o de fuentes cerradas. | Le entregas el prompt armado. Ver sección 3. |
| **El usuario aporta** | Todo lo interno: historia real del sistema, qué se intentó antes, cómo se decide de verdad, qué se mide, qué piensan los actores. | Le pides lo que necesitas y trabajas con eso. |

En este dominio el tercer modo pesa más que en otros: **la mayor parte de la evidencia que importa está adentro del sistema y no es pública**. Lo que sí conviene buscar afuera son las series de tiempo, los casos comparables y las evaluaciones de intervenciones parecidas.

Durante el proceso, **cuando falte un dato buscable y su ausencia bloquee un análisis, búscalo sin preguntar.** Preguntar por cada dato interrumpe el hilo. Lo que sí se pregunta es cuando el dato es interno y solo el usuario lo tiene.

---

## 2. Qué buscar en cada bloque

Cada línea es lo mínimo que hace falta, no una lista completa.

**`comportamiento`.** Series de datos reales de las variables que importan, lo más largas que se pueda conseguir. Es el bloque donde la búsqueda más rinde, porque la memoria de la gente sobre el comportamiento pasado es sistemáticamente poco confiable: juran que algo viene bajando cuando lo que subió fue la variabilidad. Busca también **qué se intentó antes y qué pasó después de cada intento**, que casi nunca está documentado en un solo lugar y es lo más revelador del bloque.

**`estructura`.** Sistemas parecidos y qué comportamiento produjeron. Como los sistemas con estructuras de retroalimentación similares producen comportamientos similares, un caso análogo bien elegido vale más que diez datos sueltos. También: cuáles son los retrasos reales de los procesos involucrados, que suelen estar documentados aunque nadie los mire.

**`actores`.** Qué han declarado públicamente los actores relevantes. Cómo se decide formalmente y quién firma. Historial de conducta de cada actor frente a cambios anteriores: **el pasado de un actor predice mucho mejor que la especulación sobre su racionalidad.**

**`apalancamiento`.** Evaluaciones de intervenciones comparables en otros sistemas. Qué se hizo, en qué punto de la lista de Meadows caía, y qué pasó. Acá la literatura de evaluación de políticas y de programas es sorprendentemente útil incluso para problemas organizacionales.

**`indicadores`.** Qué se mide hoy en el sistema, con qué frecuencia y quién lo ve. Y qué mide gente comparable, que ayuda a detectar la trampa de perseguir la meta equivocada.

---

## 3. Prompts de deep research

Tu trabajo es entregar un prompt que produzca un resultado accionable, no un ensayo.

**Primero decide cuántos.** La regla: **un research por pregunta de decisión.** Recomiéndale al usuario partirlo cuando las preguntas exigen tipos de fuente distintos, cubren sistemas o geografías distintas, o cuando una depende del resultado de otra, en cuyo caso van en secuencia.

Mantenlo en uno solo cuando comparten fuentes y contexto, y partirlas obligaría a repetir el mismo trabajo de fondo.

Dile siempre cuántos recomiendas, por qué, y en qué orden si van en secuencia.

**Estructura del prompt.** Adáptalo; esto es el esqueleto:

```
CONTEXTO
[Qué sistema es, en qué ámbito, qué decisión está sobre la mesa.
Dos o tres frases. Sin esto, el research devuelve generalidades.]

PREGUNTA CENTRAL
[Una sola, la que la decisión necesita responder.]

PREGUNTAS ESPECÍFICAS
1. [...]
2. [...]
3. [...]
[Entre tres y seis. Cada una con respuesta verificable, no interpretativa.]

FUENTES SUGERIDAS
[Nombra las que sabes que existen para este ámbito: literatura de
evaluación, informes sectoriales, reguladores, bases de datos
estadísticas, prensa especializada. Si no conoces las de este
ámbito, dilo en vez de inventar nombres.]

CRITERIOS DE CALIDAD
- Cada dato con su fuente y su fecha.
- Distinguir dato reportado de estimación, y estimación de opinión.
- Cuando las fuentes se contradigan, presentar ambas y decir cuál
  es más confiable y por qué.
- Cuando un dato no exista o no sea público, decirlo explícitamente
  en vez de aproximarlo.
- Para intervenciones comparables: reportar qué se hizo, en qué
  contexto, y qué pasó después, incluidos los efectos no buscados.
- Priorizar los últimos [N] años.

FORMATO DE ENTREGA
[Qué quieres de vuelta: una tabla comparativa, una serie de tiempo
con su fuente, una lista de casos con evidencia por punto. El
formato determina si el resultado se puede usar o hay que
reprocesarlo.]
```

Cuando el usuario vuelva con el resultado, tu trabajo no es aceptarlo: es leerlo con el criterio de la sección 4 y marcar qué entra como dato verificado y qué queda como supuesto.

---

## 4. Cómo se trata la evidencia

**Todo lo que entra al documento está marcado.** Dos categorías, sin tercera:

- **Dato verificado**, con fuente y fecha.
- **Supuesto**, con la prueba que lo volvería verificable, quién la corre y para cuándo.

**Cuando un dato no existe, dilo.** Un vacío nombrado es información útil: le dice al usuario dónde está ciego. Un número inventado o estimado sin base es peor que no tener nada.

**Cuando dos fuentes se contradigan**, investiga cuál es más confiable (quién la produjo, con qué método, con qué incentivo, de cuándo es) y explica por qué elegiste una. Registra que hubo contradicción: es información sobre la calidad del terreno.

**No inventes nada**: ni cifras, ni nombres de fuentes, ni citas, ni estudios. Si necesitas un número para que un razonamiento cierre y no lo tienes, escribe el razonamiento con el número como incógnita y márcalo como lo que falta averiguar.

### Las tres marcas de una flecha

Por qué una flecha se marca como cualquier otra afirmación está en `SKILL.md`. Acá van las tres marcas, que es lo que hace falta en el momento de dibujar:

| Marca | Qué significa | Cómo entra a `evidencia.md` |
|---|---|---|
| **Observada** | Hay datos o testimonio directo de que al mover A se movió B. | Dato verificado, con fuente y fecha. |
| **Inferida** | Se deduce de cómo funciona el sistema, con el razonamiento explícito. | **Supuesto**, con el razonamiento escrito y la observación que lo confirmaría. |
| **Supuesta** | Alguien cree que es así y todavía no se verificó. | Supuesto, con la prueba que lo resolvería. |

La fila del medio es la que hay que respetar: **una flecha inferida es un supuesto, no un dato verificado.** Un razonamiento bien construido sobre cómo debería funcionar el sistema sigue siendo una hipótesis sobre el sistema real, y tratarlo como verificado es exactamente la forma en que un error entra al piso de la cadena de inferencia sin que nadie lo note.

Un mapa donde todas las flechas son supuestas no es un diagnóstico: es una hipótesis, y hay que decirlo así antes de que alguien tome decisiones con él.

**La prueba más barata para una flecha dudosa** casi siempre es preguntarle a quien está en ese punto del sistema. Cuando el usuario supone cómo ve las cosas un actor, la prueba es hablar con ese actor, y suele tomar quince minutos.

### Distinguir correlación de causalidad, en voz alta

En este dominio la confusión es especialmente fácil porque los diagramas invitan a dibujar flechas. Cuando dos variables se mueven juntas, hay al menos cuatro explicaciones: A causa B, B causa A, un tercer factor causa las dos, o es coincidencia. **La segunda es la que más se olvida y es la que el pensamiento sistémico existe para recuperar**, porque casi siempre resulta que hay un ciclo y ambas cosas son verdad.

Cuando propongas una flecha, di cuál de las cuatro estás afirmando y por qué descartas las otras. Si no puedes, es una flecha supuesta.
