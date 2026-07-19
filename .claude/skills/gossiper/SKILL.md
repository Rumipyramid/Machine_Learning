---
name: gossiper
description: Investigar qué se dice sobre un tema, rumor, evento, marca o persona en espacios sociales — X/Twitter, Reddit, foros, TikTok, comentarios de noticias — con el mismo ancho de banda de búsqueda que `seeker` pero restringido al registro social/mediático informal. Activar SIEMPRE que el usuario pida "qué se dice de", "busca rumores/chismes sobre", "qué opina la gente en redes sobre", "revisa reddit/twitter sobre", "hay ruido sobre X", o quiera medir percepción pública, sentimiento o viralidad. El grado de validez aquí NO es rigor académico sino la FRECUENCIA/CANTIDAD de cobertura y el volumen y tono de la validación de comentarios de personas reales. Complementa a `seeker` (que cubre lo empírico/teórico) cubriendo el chisme, la noticia viral y la reacción social. Las fuentes usadas se registran también en el ledger de `cronista`.
---

# Gossiper — Investigación de Espectro Social

## Propósito

Investigar qué está circulando **socialmente** sobre un tema — no si es verdad en sentido
académico, sino **cuánto y cómo** se está hablando de él. Usa el mismo mecanismo de ancho
de banda de búsqueda que `seeker` (búsquedas paralelas, tipologización previa, clasificación
de fuentes, tabla resumen), pero aplicado a un registro distinto: noticias virales,
publicaciones en redes sociales y comentarios/validación de personas reales, no papers
ni teoría.

`seeker` responde "¿qué tan cierto es esto?". `gossiper` responde **"¿qué tan instalado
está esto socialmente, y qué dice la gente al respecto?"**. Son preguntas distintas y no
deben confundirse: un rumor puede estar altamente instalado (mucha cobertura, mucho
comentario) y ser falso; o puede ser cierto y tener nula tracción social. `gossiper` mide
lo primero, no lo segundo.

## Cuándo activarse

Activar este skill cuando el usuario:

- Pida "qué se dice de X", "busca chismes/rumores sobre X", "qué opina la gente de X".
- Pida revisar específicamente Reddit, X/Twitter, TikTok, foros o comentarios de noticias.
- Quiera medir sentimiento, percepción pública, viralidad o "ruido" sobre un tema, marca,
  persona o evento.
- Pregunte si algo "es tendencia", si "se está hablando de eso", o quiera rastrear el
  origen de un rumor.
- Necesite distinguir entre un tema con tracción real (muchas fuentes independientes,
  validación cruzada) y un rumor aislado (una sola fuente, sin confirmación).

No activarlo cuando el usuario pida evidencia académica/teórica (eso es `seeker`) o
evidencia de desempeño de negocio (eso es `marketer`).

## Metodología

### Paso 1: Tipologizar el tema antes de buscar

Antes de buscar, identifica qué tipo de fenómeno social es:

- **Evento noticioso reciente**: algo ocurrió y se está cubriendo (hecho verificable, con
  cobertura de medios establecidos).
- **Rumor/chisme sin fuente clara**: circula pero nadie apunta a un origen verificable.
- **Percepción de marca/persona/producto**: no es un evento puntual sino una opinión
  agregada que se acumula en el tiempo.
- **Controversia o polémica**: hay bandos, hay debate activo, hay validación Y rechazo
  simultáneos.
- **Tendencia/meme**: viralidad por formato o humor, no por contenido factual — el
  "tema" es secundario al fenómeno de difusión mismo.

### Paso 2: Mapear las plataformas relevantes

Para cada tema, identifica qué plataformas son la fuente primaria de la conversación:

- **X/Twitter**: reacción instantánea, opinión pública en caliente, buena para rastrear
  el momento en que algo "explotó".
- **Reddit**: hilos largos y elaborados, comunidades de nicho (útil para validar si un
  tema tiene tracción en una audiencia específica, no solo genérica); revisar el tamaño
  y moderación del subreddit, no solo el contenido del hilo.
- **TikTok/Instagram**: formato viral, audiencia joven, difusión por remix/duetos más que
  por argumento.
- **Foros especializados**: comunidades de nicho con memoria larga (buenas para rastrear
  el origen de un rumor).
- **Comentarios de artículos de noticias**: reacción de audiencia general, distinguir
  medio serio (con firma, corrección, línea editorial) de tabloide/agregador.

### Paso 3: Búsquedas en paralelo

Lanza búsquedas simultáneas en al menos estos frentes:

- **Búsqueda 1 — Cobertura noticiosa**: cuántos medios distintos cubren el tema, desde
  cuándo, cómo evolucionó la cobertura en el tiempo.
- **Búsqueda 2 — Contenido en RRSS**: qué se dice literalmente, hashtags asociados,
  hilos principales, cuentas que originaron o amplificaron.
- **Búsqueda 3 — Reacción/comentarios**: validación, desmentidos, debate en las
  respuestas/comentarios — no solo el post original.
- **Búsqueda 4 (opcional) — Origen del rumor**: rastrear la primera mención verificable;
  buscar la frase exacta entre comillas suele delatar el post/cuenta originaria.

### Paso 4: Clasificación de tipo de fuente social

Antes de evaluar cuánta tracción tiene un tema, clasifica **qué tipo de fuente** aporta
cada pieza. Una misma búsqueda puede traer varios tipos; identifícalos todos:

| Tipo | Qué es | Peso para "instalación social" | Ejemplo |
|---|---|---|---|
| **Medio de prensa establecido** | Firma, línea editorial, corrección de errores | 🟢 Alto — confirma que trascendió lo puramente social | Reuters, El Comercio, medios con desk de verificación |
| **Medio digital / agregador** | Republica o resume sin reporteo propio | 🔵 Medio — cuenta como cobertura pero no como fuente primaria | Portales que repostean notas de otros |
| **Cuenta verificada / figura pública** | Identidad confirmada, trayectoria | 🔵 Medio-alto si tiene expertise en el tema | Periodista, especialista, autoridad reconocida en el nicho |
| **Comunidad grande y moderada** | Subreddit/foro con miles de miembros activos y reglas de moderación | 🟡 Medio — valida que hay una audiencia de nicho involucrada | r/... con historial y moderación activa |
| **Hilo viral de cuenta anónima** | Mucho engagement, sin trayectoria verificable | 🟠 Bajo para veracidad, alto para "instalación" | Post con miles de RT sin autor identificable |
| **Comentario aislado / cuenta nueva** | Sin trayectoria, posible bot o cuenta creada ad hoc | 🔴 Mínimo — señal de alerta de amplificación artificial | Cuentas sin historial que repiten el mismo mensaje |

### Paso 5: La métrica de validez propia — Frecuencia y Validación Social

A diferencia de `seeker` (que pesa rigor metodológico), aquí la validez de la evidencia
se mide con dos ejes:

**A) Frecuencia**: cuántas piezas *independientes* (no republicaciones de la misma nota)
mencionan el tema en una ventana temporal razonable (últimos 7/30 días según el caso).
Cuenta medios y cuentas distintas, no menciones totales — 500 retweets del mismo post
cuentan como una sola fuente, no 500.

**B) Validación social**: no solo cuánto engagement hay, sino **de qué tipo**. Distingue:
- Comentarios que **confirman** el hecho (testigos, capturas, fuentes propias).
- Comentarios que **desmienten** o cuestionan.
- Comentarios que solo **amplifican sin aportar** (compartir, reaccionar, sin validar
  nada).
- Señales de **amplificación artificial**: ráfaga de cuentas nuevas repitiendo el mismo
  texto, patrones de bot, coordinación sospechosa — repórtalo si lo detectas.

Con ambos ejes, clasifica el nivel de instalación social:

| Nivel | Etiqueta | Criterio |
|---|---|---|
| 🔥 **Instalado** | Múltiples medios + validación mayoritaria | 10+ fuentes independientes en <7 días, comentarios en su mayoría confirmatorios |
| 🌡️ **Circulando** | Cobertura moderada, validación mixta | Varias fuentes, pero con desmentidos o dudas activas |
| 💬 **Rumor aislado** | Poca cobertura, sin confirmación externa | 1-2 fuentes o un solo hilo, sin corroboración independiente |
| 🧊 **Sin tracción** | Fuente única, no verificable | Una sola mención, cuenta sin trayectoria, sin eco |

### Paso 6: Tabla resumen (cuando haya 3+ fuentes)

| Fuente/plataforma | Tipo | Fecha | Validación (confirma/desmiente/amplifica) | Nivel |
|---|---|---|---|---|
| Ej. Reddit r/…, hilo de u/… | Comunidad grande | YYYY-MM-DD | Mayoría confirma, 2 desmentidos | 🌡️ Circulando |

### Paso 7: Recencia estricta

A diferencia de `seeker`, aquí **no aplica** el override de calidad por fuentes canónicas
antiguas: lo social decae rápido. Prioriza:
- Ventanas cortas (días/semanas, no años) salvo que el usuario pida evolución histórica.
- Marca siempre la fecha del último dato consultado: *"esto es de hace X días y puede
  haber cambiado"*.
- Si el tema tiene más de unas semanas, verifica si sigue activo o ya se apagó — no
  reportes como "instalado" algo que se apagó hace tiempo.

## Formato de respuesta

### Veredicto inicial (1-3 líneas)

Responde **primero** el nivel de instalación social (🔥/🌡️/💬/🧊) y, **por separado y
explícitamente marcado**, si hay señales de que el contenido de fondo sea verdadero o
falso (si esto se puede determinar con lo encontrado). Nunca fusionar ambos juicios en
uno solo — decir "esto es viral" no es decir "esto es cierto".

### Estructura recomendada

1. **Nivel de instalación social** con la etiqueta y justificación breve.
2. **Qué dice la cobertura noticiosa** (si existe), con fuentes.
3. **Qué dice la conversación social**: tono dominante, principales posturas, presencia
   de debate o consenso.
4. **Validación vs. amplificación**: qué proporción de la reacción confirma/desmiente vs.
   solo comparte.
5. **Origen probable** (si se pudo rastrear) y evolución temporal.
6. **Señales de alerta**: amplificación artificial, churnalism (muchas "noticias" que son
   la misma nota republicada), cuentas sospechosas.
7. **Limitaciones**: qué plataformas no se pudieron revisar, qué quedó sin verificar.

### Citas inline

Formato: `(Plataforma, autor/medio, fecha)`. Ejemplos:

- "El tema acumula cobertura en al menos 8 medios distintos desde el 2 de julio
  (El Comercio, 2026-07-02; RPP, 2026-07-03)."
- "El hilo original en Reddit generó validación cruzada de usuarios que se identifican
  como testigos (r/Peru, hilo de u/ejemplo, 2026-07-01)."

## Anti-patrones a evitar

- **Confundir viralidad con veracidad**: que algo tenga mucha cobertura o mucho comentario
  no lo hace cierto. Repórtalo como "instalado", no como "verificado".
- **Tomar un solo hilo o cuenta como representativo** del consenso social — verifica que
  haya múltiples fuentes independientes antes de hablar de "consenso".
- **Ignorar amplificación artificial**: si el patrón de cuentas sugiere coordinación o
  bots, decirlo explícitamente en vez de contarlo como validación orgánica.
- **Confundir churnalism con cobertura real**: muchas "noticias" pueden ser la misma nota
  de agencia republicada por decenas de portales sin reporteo propio — cuenta fuentes
  *independientes*, no republicaciones.
- **Mezclar el juicio de instalación con el juicio de verdad** — son ejes distintos y
  deben reportarse por separado.

## Registro en el cronista

Al terminar una investigación de `gossiper`, registra las fuentes usadas en el ledger de
`cronista` (`research/fuentes/codice.md`), igual que haría cualquier otro skill
que se apoye en evidencia externa:

- La mayoría de las fuentes de `gossiper` caerán en los niveles **D** (prensa/blogs sin
  método propio) o **E** (redes sociales, foros, opinión sin metodología) de la rúbrica
  de rigurosidad de `cronista` — eso es esperado y correcto, no un defecto: `gossiper`
  no busca rigor académico sino tracción social.
- En el campo **Resumen breve**, incluye el dato de frecuencia/validación que motivó el
  registro (p. ej. *"8 medios cubrieron el rumor en 5 días; comentarios de Reddit en su
  mayoría lo desmienten"*), para que quien lea el ledger después entienda por qué se
  registró una fuente de rigor bajo.
- Si el mismo rumor/tema ya tiene entradas previas en el ledger, deduplica y actualiza
  el campo *Usado en / fundamenta* en vez de crear filas nuevas.
