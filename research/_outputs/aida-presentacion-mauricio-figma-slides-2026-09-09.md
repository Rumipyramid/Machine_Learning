<!--
=============================================================================
AIDA · "El copiloto que el piloto no puede soltar"
Presentación ejecutiva para Mauricio (VP de Canales) — FORMATO FIGMA SLIDES
=============================================================================

CÓMO USAR ESTE ARCHIVO EN FIGMA SLIDES
--------------------------------------
1. Abre Figma Slides > archivo nuevo (16:9).
2. Copia todo el contenido de este archivo DESDE la línea del primer separador
   "---" hacia abajo, y pégalo en el canvas de Figma Slides (Cmd/Ctrl+V).
   Alternativa: usa un plugin de importación de Markdown ("Markdown to Slides",
   "Docs to Slides") apuntando a este .md.
3. Figma crea una lámina por bloque separado por "---".

CONVENCIONES DE ESTE ARCHIVO (mapeo a los placeholders de Figma Slides)
-----------------------------------------------------------------------
  ---            → separador de lámina (una lámina por bloque)
  `KICKER`       → etiqueta superior, mono (JetBrains Mono, 14px, acento rojo)
  # Texto        → Título de la lámina (Fraunces, serif)
  ## Texto       → Subtítulo / bajada (Inter)
  ### Texto      → encabezado de bloque dentro de la lámina
  **99%**        → cifra protagonista (una sola por lámina de hallazgo)
  - viñeta       → cuerpo (Inter)
  > cita         → verbatim de asesor (Fraunces itálica + atribución mono)
  <!-- ... -->   → notas de dirección de arte y de orador. NO se importan a
                   Figma (son comentarios HTML, invisibles al pegar). Si tu vía
                   de importación sí las muestra, bórralas con buscar/reemplazar
                   del patrón <!-- ... -->.

SISTEMA DE DISEÑO (configurar una vez en el tema del archivo de Figma Slides)
-----------------------------------------------------------------------------
  Fondo papel cálido   #F2F3F7
  Tinta                #03050F
  Acento (único)       #EF3340
  Títulos              Fraunces
  Cuerpo               Inter
  Kickers/cifras/tags  JetBrains Mono
  Sin degradés, sin sombras, sin iconografía decorativa.
  Máximo UNA cifra protagonista por lámina de hallazgo.

DIFERENCIAS FRENTE AL DOCUMENTO FUENTE (deliberadas, por el medio)
------------------------------------------------------------------
  · Figma Slides no tiene elemento de tabla: todas las tablas del documento se
    convirtieron en bloques de viñetas o en pares "columna izquierda /
    columna derecha", que sí se maquetan nativo.
  · Las láminas con tabla larga se dividieron para respetar el criterio de
    densidad ejecutiva: 5a → 4 láminas · 7 (mapa de soluciones) → 4 láminas.
  · Numeración original entre corchetes al final de cada título de nota, para
    poder rastrear cada lámina de vuelta al documento fuente.
  · No se cambió, redondeó ni inventó ningún dato, verbatim ni veredicto.

ESTRUCTURA: 29 láminas + 1 de respaldo (no proyectar).

PROCEDENCIA
-----------
Output del hub de investigación. Node relacionado:
[[proyecto-back-to-basics-ffvv-vida]] (capa de estado y decisiones internas de
RIMAC, donde vive la descripción de AIDA como copiloto en conversación real).
Contenido de origen: diagnóstico AIDA ya validado + documento fuente del usuario
`DX-AIDA-presentacion-final-GenAI.md` (no versionado en este repo).
Fecha: 2026-09-09.
=============================================================================
-->

---

`BEHAVIORAL DESIGN · COE DE EXPERIENCIA`

# AIDA: el copiloto que el piloto no puede soltar

## Diagnóstico de AIDA en la venta de Vida — y el camino para que se gane el asiento

Presentado a Mauricio · VP de Canales

<!--
LÁMINA 1 · Carátula [fuente: Lámina 1]
ARTE: silueta de un auto de carrera visto desde dentro de la cabina — dos
asientos, piloto y copiloto, ambos con casco. El piloto con las manos en el
volante; el copiloto sosteniendo un mapa/tablet. Alto contraste (tinta sobre
papel o inverso), sin gradientes, línea gruesa, estilo blueprint técnico — no
ilustración realista. El acento rojo marca ÚNICAMENTE al copiloto: es la pieza
que se está evaluando.
LAYOUT: título a sangre en la mitad inferior izquierda; ilustración ocupando el
tercio derecho o el fondo completo al 15% de opacidad.
-->

---

`CONTEXTO`

# Un piloto no suelta el volante por un copiloto en el que no confía

### La falla que abrió la exploración

[IMAGEN — captura real del chat con AIDA]

Se le preguntó: *"¿qué productos tenemos hoy en la cartera de vida?"*
La respuesta **omitió Vida Ahorro Garantizado**, uno de los productos centrales del ramo.

Esta fue la primera señal, dentro de la intervención **Back to Basics: Venta Vida**, de que valía la pena preguntarse si AIDA está cumpliendo lo que prometió.

<!--
LÁMINA 2 · Contexto, parte 1 de 2 [fuente: Lámina 2, columna izquierda]
ARTE: lámina a dos columnas. Izquierda: la captura real del chat, encuadrada
con borde de 2px tinta, sin sombra, con un subrayado rojo sobre la omisión.
Derecha: espacio en blanco deliberado — la lámina siguiente carga las promesas.
Se separó en dos láminas porque en proyección la captura necesita tamaño real
para leerse, y compartir espacio con tres bloques de cita la vuelve ilegible.
-->

---

`CONTEXTO`

# Las tres promesas con las que se construyó AIDA

### Promesa primaria
Reducir el tiempo de gestión del asesor.

### Promesa secundaria 1
Acortar la curva de aprendizaje de los asesores nuevos.

### Promesa secundaria 2
Mejorar la experiencia de venta — y con eso, el NPS, la conversión, la recomendación y la renovación.

▸ Todo lo que sigue en esta presentación mide a AIDA contra estas tres promesas, no contra una opinión.

<!--
LÁMINA 3 · Contexto, parte 2 de 2 [fuente: Lámina 2, columna derecha]
ARTE: tres bloques apilados, cada uno con filete rojo de 4px a la izquierda
(componente "quote block" del sistema). La numeración de promesa en mono,
pequeña, sobre cada bloque. La línea "▸" al pie, en mono, tamaño cuerpo, sin
recuadro — es la regla de lectura de todo el deck.
NOTA DE ORADOR: dejar esta lámina proyectada mientras se enuncia la agenda; es
la vara de medición y conviene que quede fijada antes de entrar al método.
-->

---

`OBJETIVO DE ESTA REUNIÓN`

# Qué necesitamos decidir hoy

Alinear contigo el diagnóstico de AIDA — con evidencia, no con percepción — y salir de esta reunión con una decisión sobre el camino a seguir: **aceptar el POC de un proveedor externo, o evolucionar AIDA con capacidad propia ya construida.**

<!--
LÁMINA 4 · Objetivo [fuente: Lámina 3, primera mitad]
ARTE: lámina de una sola idea. Título grande, párrafo único a 2/3 de ancho, el
resto en blanco. Las dos opciones de la última frase van en negrita tinta, sin
color — el rojo se reserva para la lámina 23, donde la decisión se presenta.
Se separó de la agenda porque el objetivo es la única frase que Mauricio debe
retener de esta sección.
-->

---

`OBJETIVO DE ESTA REUNIÓN`

# Agenda

1. **Metodología** — cómo llegamos a estas conclusiones
2. **Las oportunidades** — 4 capacidades donde hay una brecha entre lo que AIDA hace y lo que podría hacer
3. **Veredicto** — las tres promesas, evaluadas
4. **Mapa de soluciones** — todo lo identificado, ordenado por esfuerzo
5. **Opciones de siguientes pasos** — la decisión que te traemos
6. **Demo** — te presentamos Maveric
7. **Cierre** — los indicadores de productividad a los que apuntamos

<!--
LÁMINA 5 · Agenda [fuente: Lámina 3, segunda mitad]
ARTE: sin gráfico. Bloques con número en mono grande (rojo) + título en
Fraunces + descripción en Inter gris tinta al 60%. Sin iconografía. Mismo
tratamiento de "índice" ya usado en el resto del deck.
-->

---

`CÓMO LLEGAMOS AQUÍ`

# Ninguna conclusión descansa en un solo método

## Seis frentes de evidencia independientes, que se cruzan entre sí. Donde dos o más llegan al mismo hallazgo por caminos separados, ese hallazgo deja de ser una opinión.

- **Encuesta a asesores** — 19 asesores · qué dicen que necesitan
- **Auditoría documental con Claude como juez** — 46 preguntas verificadas contra el documento fuente real · qué tan correcto es el dato, verificado, no supuesto
- **Entrevistas de incidentes críticos** — 4 asesores de Vida e Inversiones · qué hacen en la práctica, no solo qué dicen
- **Logs reales de uso (AIDA Sales)** — 3.606 consultas · 1.266 sesiones · 341 usuarios · 3 días · comportamiento real, a escala
- **Entrevista a la dueña del producto (PO)** — 1 entrevista · arquitectura técnica real y qué mide hoy el tablero
- **Dashboard de adopción** — 242.785 consultas · 167 días · 50 jefaturas · el panorama completo de uso en toda la fuerza de ventas

▸ Este es el mismo rigor metodológico que ya se presentó al equipo de Gen AI — aquí lo resumimos porque el foco de hoy es la decisión, no el método.

<!--
LÁMINA 6 · Metodología [fuente: Lámina 4]
GRÁFICO: seis chips horizontales tipo "termómetro de muestra" — un ícono simple
(línea, 1.5px, tinta) + la cifra de alcance de cada frente, en UNA sola fila
bajo el subtítulo, con el nombre del frente debajo en mono 12px. Formato más
ejecutivo que la tabla completa del deck técnico. Si la fila de seis no respira,
usar dos filas de tres — nunca una tabla.
DESTACAR: el chip de "Auditoría documental" en acento rojo — es el frente que
sostiene la lámina 8-11 y el único que verifica corrección, no percepción.
-->

---

# Detectamos oportunidades en 4 capacidades de AIDA

Back to Basics no busca apagar AIDA — busca identificar, con evidencia, dónde deja valor sobre la mesa. Encontramos brechas concretas en cuatro capacidades: **qué cubre hoy, y qué podría cubrir si cerrara esas brechas.**

- **Consulta** — Falla, y ya no hay confianza
- **Entrenamiento** — Los asesores senior ya no la utilizan
- **Gestión** — El dashboard no registra reducción del tiempo de gestión ni impacto en la productividad
- **Generación de contenido** — Los asesores usan ChatGPT, Gemini y Copilot para esto; AIDA no se usa

<!--
LÁMINA 7 · Transición a oportunidades [fuente: Lámina 5]
ARTE: un asesor de venta (silueta, sin rostro identificable) sentado frente a
una pantalla o celular, con un ícono simple de IA (chip o burbuja de chat)
superpuesto — mismo tratamiento blueprint que la carátula, sin fotografía
realista. Ilustración a la derecha o de fondo al 12%.
LAYOUT: las cuatro capacidades como lista numerada 01-04 en mono; el nombre de
la capacidad en Fraunces y el hallazgo en Inter, misma línea, separados por un
filete vertical rojo de 2px.
-->

---

`OPORTUNIDAD 1 DE 4 · CONSULTA`

# Falla, y ya no hay confianza

## En un contraste directo, la auditoría documental encontró que AIDA **acierta en el dato simple y falla en el tema que decide la venta**.

El error no se reparte parejo: se concentra en los temas de mayor consulta y mayor impacto comercial.

<!--
LÁMINA 8 · Consulta, apertura [fuente: Lámina 5a, cifra protagonista]
ARTE: lámina de una sola idea, sin datos. El contraste "acierta en lo simple /
falla en lo que decide" se compone tipográficamente: la primera mitad en tinta,
la segunda en acento rojo. Sirve de portada de las tres láminas siguientes.
-->

---

`OPORTUNIDAD 1 DE 4 · CONSULTA`

# Dónde falla: los temas de alta consulta

## Cruce de cuánto se consulta con qué tan bien responde AIDA

**Datos atómicos / de existencia** *(prima mínima, "¿está cubierto?")*
Consulta: muy alta · **✓ CONFIABLE** — Acierta: es su terreno fuerte, los 4 controles de respuesta conocida pasaron.

**Rentabilidad / devolución** *(seguros de inversión)*
Consulta: muy alta · **✕ CUMPLIMIENTO** — 21,12% de fuente fantasma y "170% gratis y ganancia" → mis-selling: ningún portafolio garantiza rentabilidad.

**Identidad de producto** *(VAG / RG / Devolución 200)*
Consulta: alta · **✕ CRÍTICO** — Mezcla productos distintos; el material se contradice y AIDA lo propaga en vez de señalarlo.

**Coberturas: ¿a quién cubre?** *(titular vs. familia)*
Consulta: media · **✕ CRÍTICO** — Infló la cobertura: marcó familia como cubierta en 7 de 9 filas donde la ficha limita al titular.

<!--
LÁMINA 9 · Consulta, mapa de fallas 1 de 2 [fuente: Lámina 5a, filas 1-4]
GRÁFICO: esta lista ES el gráfico. Cada fila con (a) una barra corta horizontal
de "cuánto se consulta" a la izquierda, escala fija de 4 pasos
(muy alta / alta / media / baja), y (b) un chip de estado a la derecha:
  ✕ CRÍTICO y ✕ CUMPLIMIENTO → fondo tinta + texto papel
  ✓ CONFIABLE               → solo contorno tinta, sin relleno
  ◐ BRECHA                  → medio tono
FUENTE AL PIE (mono 11px): "Auditoría documental con Claude, 46 preguntas
verificadas contra el documento fuente real; volumen de consulta según logs,
ramo Vida, n=1.139."
Se dividió en dos láminas: 9 filas en proyección ejecutiva no se leen. El corte
es por volumen de consulta (alta arriba, baja abajo), que es además el orden en
que conviene narrarlo.
-->

---

`OPORTUNIDAD 1 DE 4 · CONSULTA`

# Dónde falla: los temas de baja consulta — y el peor de todos

**Cotización / precio** *(antes de cerrar)*
Consulta: baja · **✕ CRÍTICO** — 12,4% de falla medida. No compara ni alerta límites de negocio.

**Edades: ingreso / permanencia** *(edad máxima por producto)*
Consulta: baja · **✕ CRÍTICO** — Confunde edad de ingreso con edad de permanencia (auditoría + asesores).

**Suscripción / riesgo** *(preferente vs. estándar)*
Consulta: baja · **✕ CRÍTICO** — Clasificó a un hipertenso como "preferente" cuando el procedimiento dice estándar/agravado.

**Emisión / trámite** *(el momento del cierre)*
Consulta: baja · **✕ CRÍTICO — EL PEOR TEMA** — 13,6% de falla medida. El error llega cuando cuesta más caro.

**Objeciones / cierre** *(la necesidad #1 declarada)*
Consulta: 0,6% pedido · **◐ BRECHA** — Casi no se le pide (0,6%) aunque el 42% lo necesita: se resuelve por fuera con ChatGPT/Copilot.

<!--
LÁMINA 10 · Consulta, mapa de fallas 2 de 2 [fuente: Lámina 5a, filas 5-9]
GRÁFICO: mismo tratamiento que la lámina 9 — continuidad visual exacta, misma
posición de barras y chips, para que se lea como una sola tabla partida.
DESTACAR: "Emisión / trámite" con el chip en acento rojo sólido (único uso de
rojo relleno del bloque) — es el peor tema medido y el que decide el cierre.
La fila "Objeciones / cierre" anticipa la lámina 15-16: al narrarla, señalarla
como puente.
-->

---

`OPORTUNIDAD 1 DE 4 · CONSULTA`

# Por qué ya no hay confianza: el mecanismo detrás de la tabla

- AIDA es exacta cuando el dato es atómico y vive en un documento limpio. Se cae —con la misma seguridad y sin avisar— cuando el dato es ambiguo o requiere síntesis. **De los 9 temas, solo 1 sale "Confiable".**
- Casos verificados documento por documento: citó una fuente financiera que no existe; declinó dar un dato que sí tenía citado minutos antes; dio el mismo error en 4 de 7 preguntas idénticas y no en las otras 3.
- **3 de 4 asesores entrevistados** describen, sin haber visto la auditoría, los mismos tres errores que la auditoría encontró por su lado: confusión de edades, uso del dato equivocado con la fuente correcta al lado, confusión entre productos.
- El error no se reparte parejo: se concentra justo en los temas de mayor volumen (**Rentabilidad, 39,4% de la demanda**) y de mayor impacto en el cierre (**Emisión/trámite, el peor tema medido**).

> "Confianza... un 50%... me confunde más que me ayuda."
> — Asesora, ~1 año en Rimac

<!--
LÁMINA 11 · Consulta, mecanismo [fuente: Lámina 5a, bloque final]
ARTE: cuerpo a la izquierda (2/3), verbatim a la derecha (1/3) en el componente
de cita: Fraunces itálica 32px, filete rojo de 4px arriba, atribución en mono.
NOTA DE ORADOR: el tercer punto es el que cierra la discusión sobre si esto es
percepción o hecho — dos métodos independientes, mismo hallazgo. Es el argumento
metodológico de la lámina 6 aplicado a un caso concreto.
-->

---

`OPORTUNIDAD 2 DE 4 · ENTRENAMIENTO`

# Los asesores senior ya no la utilizan

## El uso de AIDA **decae de forma continua** desde el primer mes del asesor en la compañía — no se estabiliza, sigue cayendo.

### Por qué pasa, verificado contra la fuente
- AIDA responde bien las preguntas de un solo dato — una cobertura, un requisito, una definición. Es el terreno de un asesor nuevo.
- Falla más en lo que un asesor experimentado necesita: casos límite, comparaciones, síntesis entre documentos que se contradicen.
- Es decir: cuanto más avanza el asesor en su curva de aprendizaje, más se corre hacia el terreno exacto donde AIDA es frágil.

> "Hoy en día te conozco ya al revés, el derecho del producto... yo creo que ya no recurro mucho a ella."
> — Asesora, ~1 año en Rimac

▸ Esta no es una falla de adopción — es un límite estructural de lo que AIDA sabe hacer bien hoy. Y es exactamente lo que el modo Entrenar (mapa de soluciones) está diseñado para resolver.

<!--
LÁMINA 12 · Entrenamiento [fuente: Lámina 5b]
GRÁFICO: curva de decaimiento simple. Eje X = "mes 0 → 6-8 meses → 1 año+".
Eje Y = "uso de AIDA (alto → bajo)". UNA sola línea descendente, 3px tinta, sin
ejes numéricos exactos, sin grilla.
⚠️ OBLIGATORIO — nota al pie del gráfico, mono 11px:
   "Patrón cualitativo confirmado en entrevistas, no serie medida."
   Sin esa nota se sobre-representa la precisión del dato. No negociable.
LAYOUT: gráfico arriba a la derecha, ocupando 40% del ancho; el bloque "por qué
pasa" abajo a la izquierda; verbatim al pie.
-->

---

`OPORTUNIDAD 3 DE 4 · GESTIÓN`

# El dashboard no registra reducción del tiempo de gestión ni impacto en la productividad

## De los **cinco indicadores** del dashboard actual de AIDA —consultas, promedio diario, actividad, ratio de feedback, margen de error— **ninguno mide tiempo ni productividad.**

No existe hoy un número para sostener ni para desmentir la promesa primaria de AIDA, ni para saber si AIDA hace al asesor más productivo.

<!--
LÁMINA 13 · Gestión, la ausencia [fuente: Lámina 5c, primera mitad]
GRÁFICO: cinco chips en fila, uno por indicador del dashboard actual, cada uno
con una "X" superpuesta en acento rojo y la etiqueta "no mide tiempo" debajo en
mono 11px. Visual simple y contundente, sin datos numéricos — el punto ES la
ausencia. Los chips en gris al 40% para que la X roja sea lo único que salta.
-->

---

`OPORTUNIDAD 3 DE 4 · GESTIÓN`

# Y el indicador que sí existe mide lo contrario de lo que parece

## 👎 134 palabras · 👍 207 palabras

Las respuestas con feedback **negativo son más cortas** (134 palabras de mediana) que las que reciben feedback **positivo** (207 palabras de mediana) — lo opuesto de lo esperable si el problema fuera "demasiado larga".

- El **34% de las calificaciones negativas** son, directamente, respuestas de "no tengo esa información": el asesor castiga el fracaso visible y premia la respuesta larga y de aspecto completo, así esa respuesta larga sea la que esconde el dato riesgoso.
- **Consecuencia:** el **96% de aprobación** que muestra el dashboard hoy no puede detectar ninguno de los problemas de este diagnóstico, porque viven precisamente dentro de las respuestas que el sistema de feedback recompensa.

<!--
LÁMINA 14 · Gestión, el feedback engañoso [fuente: Lámina 5c, segunda mitad]
GRÁFICO: dos barras horizontales simples, 👎 134 palabras / 👍 207 palabras,
misma escala, la de 👍 visiblemente más larga. Etiqueta bajo el par, en mono:
"el feedback premia lo que se ve completo, no lo que es correcto".
DESTACAR: el "96%" en cifra grande al pie, tachado o con el filete rojo del
componente de alerta — es el número que Mauricio probablemente ya vio y del que
esta lámina lo tiene que despegar.
NOTA DE ORADOR: esta es la lámina que desarma el argumento "pero el dashboard
dice que está bien". Es la contraparte exacta de la lámina 28 (indicadores).
-->

---

`OPORTUNIDAD 4 DE 4 · GENERACIÓN DE CONTENIDO`

# Los asesores ya resuelven esto — pero no con AIDA

## 42% ≠ 0,6%

- **42%** dice que manejar objeciones es su necesidad #1 *(encuesta a 19 asesores)*
- **0,6%** de lo que realmente le pide a AIDA es sobre objeciones *(logs, 3.606 consultas)*

La misma necesidad, medida por dos métodos distintos, con una brecha de **70x** entre lo que se declara y lo que se hace. Es la brecha más grande de todo el diagnóstico.

<!--
LÁMINA 15 · Generación de contenido, la brecha [fuente: Lámina 5d, cifra]
GRÁFICO: dos cifras grandes, lado a lado (Fraunces 180px), con "≠" o una flecha
entre ellas. El "42%" en tinta, el "0,6%" en acento rojo. Debajo de cada una, su
fuente en mono 12px. El "70x" al pie, más pequeño, en mono.
Es el contraste visual más fuerte de toda la presentación — no meter nada más en
esta lámina.
-->

---

`OPORTUNIDAD 4 DE 4 · GENERACIÓN DE CONTENIDO`

# Los asesores ya dividieron el trabajo — y ya eligieron qué herramienta va en cada lado

### AIDA
**Para qué se usa:** validación técnica — coberturas, exclusiones, edades, documentos oficiales.
**Resultado:** es la única que conoce los datos reales de RIMAC.

### ChatGPT / Gemini / Copilot
**Para qué se usa:** generación de contenido — speeches, guiones, flyers, prospección.
**Resultado:** no conoce esos datos — pero es rápida, corta y usable en el momento.

> "Aida sería conocimiento, y Copilot, inteligencia."
> — Asesora, ~1 año en Rimac

▸ No es que el asesor no necesite ayuda para generar contenido comercial — es que dejó de pedírsela a AIDA porque aprendió que ahí no se la resuelve, y ya resolvió el problema por fuera, sin que nadie se lo pidiera.

<!--
LÁMINA 16 · Generación de contenido, el reparto [fuente: Lámina 5d, tabla]
LAYOUT: dos columnas verticales de igual ancho separadas por un filete tinta de
1px — la tabla original girada 90°, que es como se maqueta nativo en Figma
Slides. Encabezado de cada columna en Fraunces; "Para qué se usa" y "Resultado"
como etiquetas mono 11px dentro de cada columna.
El verbatim cruza el ancho completo, debajo de las dos columnas — funciona como
el resumen de las dos.
-->

---

`EL VEREDICTO`

# Las tres promesas, evaluadas

### ✕ Reducir el tiempo de gestión *(primaria)* — NO SE CUMPLE
La desconfianza obliga a verificar cada respuesta con un jefe, un compañero o el documento fuente — eso anula cualquier ahorro. Y no existe una métrica de tiempo para probarlo o desmentirlo.

### ◐ Acortar la curva de aprendizaje *(secundaria)* — A MEDIAS
Ayuda al inicio, pero decae con la experiencia — y mientras dura, deja al asesor junior expuesto a errores que no puede detectar a tiempo.

### ✕ Mejorar la experiencia de venta *(secundaria)* — NO SE CUMPLE
El formato de AIDA no sirve en el momento en vivo frente al cliente (10–20 seg de espera, 200–500 palabras de respuesta), y esa necesidad comercial ya se resuelve con otra herramienta.

<!--
LÁMINA 17 · Veredicto [fuente: Lámina 6, tabla]
ARTE: marca visual GRANDE ✕ / ◐ a la izquierda de cada bloque (72px): las dos ✕
en acento rojo, la ◐ en gris tinta al 50%. El veredicto en mono mayúsculas a la
derecha del título de cada promesa.
Sin recuadros ni fondos — tres bloques separados solo por filete tinta 1px.
NOTA DE ORADOR: es el punto de bisagra del deck. Todo lo anterior es evidencia;
todo lo que sigue es qué hacemos. Pausa aquí.
-->

---

`EL VEREDICTO`

# Los riesgos que están detrás del veredicto — y que hoy nadie está vigilando

### Riesgo de cumplimiento
En un speech de venta, una cifra de rentabilidad prudente ("hasta 170%") se convierte en una promesa sin matiz ("tu seguro te salió gratis y encima ganaste dinero") — contradiciendo un documento propio de RIMAC que afirma que ningún portafolio de inversión ofrece rentabilidad garantizada.

### Riesgo de gobierno de datos
Hay datos personales completos de una clienta real —nombre, DNI, dirección, teléfono, número de póliza— dentro de la base de conocimiento que usa AIDA. **Ninguna métrica actual lo detecta.**

### Riesgo de error silencioso
El asesor no puede notar el error de AIDA hasta que ya ocurrió, porque su prioridad frente al cliente es no mostrar duda — un error con la misma seguridad que un acierto es, en la práctica, indistinguible para el asesor en el momento.

<!--
LÁMINA 18 · Riesgos [fuente: Lámina 6, bloque de riesgos]
ARTE: componente "alert" del sistema, a lámina completa — fondo tinta (#03050F),
texto papel (#F2F3F7), borde rojo grueso (8px) a la izquierda. Es la ÚNICA
lámina en negativo de todo el deck: el cambio de fondo hace el trabajo de
señalar gravedad sin necesidad de iconografía de alarma.
Se separó de la lámina 17 porque el veredicto y los riesgos compiten por
atención si comparten lámina, y el riesgo de gobierno de datos es el único punto
del deck con consecuencia regulatoria inmediata.
-->

---

`QUÉ HACEMOS`

# Una pirámide, tres momentos, todas las soluciones identificadas

### Cómo leer las próximas tres láminas
La pirámide tiene tres niveles: **Cimiento** (base, más ancha — arreglar lo que ya existe), **Hábito** (medio — que confíen y vuelvan a usarla) y **Retorno** (arriba, más angosto — que el valor se pueda medir). Dos soluciones no dependen de la secuencia y pueden arrancar hoy mismo: están marcadas **▶ YA**.

### Leyenda de esfuerzo *(propuesta, a validar contigo)*
**●** Bajo — accionable en semanas, sin dependencias técnicas grandes · **●●** Medio — requiere coordinación entre áreas o desarrollo moderado · **●●●** Alto — requiere desarrollo técnico o cambio de producto significativo.

### Leyenda de owner *(propuesta, a validar contigo)*
**Canales** — decisiones de negocio, contenido comercial y priorización · **Producto / Gen AI** — desarrollo técnico de AIDA · **Learning** — capacitación y refuerzo de contenidos · **CoE Diseño y Experiencia** — Behavioral Design + Service Design · **Calidad / EDA** — auditoría de riesgos · **Mantenimiento** — limpieza y seguridad de datos.
Varias soluciones tienen más de un owner porque requieren trabajo conjunto — el primero listado es quien lidera.

<!--
LÁMINA 19 · Mapa de soluciones, cómo leer [fuente: Lámina 7, encabezado]
ARTE: la pirámide como forma visual real (tres franjas horizontales apiladas de
ancho decreciente: Cimiento la más ancha abajo, Retorno la más angosta arriba)
a la derecha, VACÍA, solo con los nombres de los tres niveles. Las leyendas a la
izquierda. Las tres láminas siguientes rellenan una franja cada una, con la
pirámide siempre presente en la misma posición y el nivel activo en tinta y los
otros dos al 20% — así se ve el avance sin repetir la explicación.
-->

---

`QUÉ HACEMOS · NIVEL 1`

# 🔺🔺🔺 Cimiento — que el contenido esté bien

## La base: nada de lo demás funciona sobre una base todavía rota.

- **▶ YA — Automatizar la auditoría de calidad con un modelo de IA** (Claude, o alternativamente Copilot) y bajar hallazgos y preguntas frecuentes al equipo de Learning · **●** Bajo · *CoE Diseño y Experiencia + Learning*
- Definir los activos de conocimiento de Vida (playbook, manual de objeciones, matriz de productos) · **●●** Medio · *Canales + Producto / Gen AI*
- Detectar duplicados o contradicciones *(ya en marcha, usando el modelo auditor validado desde 2023)* · **●** Bajo · *Producto / Gen AI*
- Definir la jerarquía de fuentes (ej. el condicionado manda sobre el material de marketing) · **●** Bajo · *Canales*
- Designar un dueño de negocio por cada activo *(hay precedente: el subagente "Susi" en suscripción)* · **●●** Medio · *Canales*
- Consolidar: un documento por producto, sin duplicados, en texto legible · **●●●** Alto · *Canales + Producto / Gen AI*
- Bajar lineamientos formales de carga de documentos · **●** Bajo · *Producto / Gen AI*
- Depurar los datos personales de clientes expuestos en la base · **●●** Medio · *Producto / Gen AI + Mantenimiento*
- Clasificar el contexto de cada consulta (estudio vs. gestión en vivo) · **●●●** Alto · *Producto / Gen AI*
- Capturar y estandarizar las "inferencias" de intención detrás de cada consulta · **●●●** Alto · *Producto / Gen AI*
- Agregar alertas automáticas de baja confianza · **●●●** Alto · *Producto / Gen AI*

<!--
LÁMINA 20 · Cimiento [fuente: Lámina 7, tabla Cimiento]
GRÁFICO: pirámide a la derecha con la franja INFERIOR activa. Los ítems como
chips pequeños dentro de la franja, coloreados por esfuerzo (escala de gris a
rojo: ● gris claro, ●● gris medio, ●●● rojo). Cada chip lleva su owner en mono
10px debajo del texto.
DESTACAR: el ítem "▶ YA" con borde rojo sólido de 2px, para que salte a la vista
sin leer el detalle.
NOTA DE ORADOR: el ítem de depurar datos personales es el que cierra el riesgo
de gobierno de datos de la lámina 18 — nombrarlo así al pasar.
Es la lámina de mayor densidad del bloque; si en proyección no respira, partir
en "Cimiento — contenido" (ítems 1-7) y "Cimiento — sistema" (ítems 8-11).
-->

---

`QUÉ HACEMOS · NIVEL 2`

# 🔺🔺 Hábito — que la usen y recuperen la confianza

## Depende de que Cimiento esté avanzado: usar AIDA sobre una base todavía rota reproduce el problema.

- **▶ YA — Reforzar los contenidos de mayor error y consulta** (rentabilidad, coberturas, endoso), vía Learning · **●** Bajo · *Learning*
- **Relanzamiento integrado desde el inicio a la campaña de motivación comercial Escuadrón RIMAC** — no como un anuncio técnico de mejoras, sino dentro de la narrativa que el canal ya usa para motivarse, explicando qué se corrigió · **●●** Medio · *Canales + CoE Diseño y Experiencia + Learning*
- Cargar a AIDA el manual de objeciones *(ya se está armando)* · **●** Bajo · *Canales + Producto / Gen AI*
- Habilitar el modo Entrenar además de Consultar *(ya existe un prototipo — falta formalizarlo como subagente "AIDA Learning")* · **●●●** Alto · *CoE Diseño y Experiencia + Producto / Gen AI + Learning*
- Medir KPIs de frecuencia, recurrencia y evolución de uso · **●●** Medio · *Producto / Gen AI + CoE Diseño y Experiencia*

<!--
LÁMINA 21 · Hábito [fuente: Lámina 7, tabla Hábito]
GRÁFICO: pirámide a la derecha con la franja MEDIA activa; Cimiento abajo al 20%
pero ya con sus chips visibles en gris (señal de "esto ya lo vimos").
DESTACAR: el ítem "▶ YA" con borde rojo sólido; el ítem de relanzamiento con un
marcador discreto que lo conecte con la lámina 26 (Maveric) — es el mismo
movimiento, contado dos veces desde ángulos distintos.
-->

---

`QUÉ HACEMOS · NIVEL 3`

# 🔺 Retorno — que el impacto se vea y se defienda

## Depende de que Hábito esté instalado: no se puede medir el impacto de algo que nadie usa todavía con confianza.

- Medir tiempo de gestión, tasa de error y nivel de riesgo (antes/después) · **●●** Medio · *CoE Diseño y Experiencia + Producto / Gen AI*
- Consolidar el aprendizaje medido por el modo Entrenar en un indicador de impacto real · **●●** Medio · *Learning + CoE Diseño y Experiencia*
- Medir calidad de venta: persistencia, referidos, NPS · **●●** Medio · *Canales + CoE Diseño y Experiencia*
- Sistematizar auditorías periódicas del modelo *(ya en marcha, parcial — falta ampliar el mandato del equipo de Calidad/EDA)* · **●●** Medio · *Calidad / EDA*

*Nota: la sección "Más allá" del roadmap completo (modo tipo Copilot abierto, memoria de largo plazo, "one front" tipo Copilot M365) queda deliberadamente fuera de esta pirámide — son apuestas grandes que esperan a que Hábito esté instalado, y no compiten por foco en esta conversación.*

<!--
LÁMINA 22 · Retorno [fuente: Lámina 7, tabla Retorno + nota de cierre]
GRÁFICO: pirámide completa, con la franja SUPERIOR activa y las dos de abajo ya
llenas en gris — la lámina donde por fin se ve la pirámide entera. Es el cierre
visual del bloque.
La nota "Más allá" al pie, en Inter itálica 14px, gris tinta al 55%: está para
que Mauricio sepa que existe y que se decidió no traerla, no para discutirla.
-->

---

`LA DECISIÓN DE HOY`

# Dos caminos, no uno solo

### POC — Overlap
Aceptar el piloto (POC) del proveedor externo, entregándole datos internos de RIMAC para que la herramienta funcione.

### Evolucionar AIDA
Cerrar las brechas de Cimiento y, según el alcance elegido, sumar nuevas capacidades sobre la base ya construida internamente.

- **Opción i — Solo cimientos:** evolucionar AIDA únicamente hasta cerrar las brechas de Cimiento (gobierno de contenido, consolidación, jerarquía de fuentes).
- **Opción ii — Cimientos + nuevas capacidades:** evolucionar AIDA hasta dotarla de nuevas capacidades, en un entorno de prueba controlado, sobre un **prototipo ya funcional** creado por Behavioral Design y Service Design.

<!--
LÁMINA 23 · Dos caminos [fuente: Lámina 8, primera parte]
GRÁFICO: NO una tabla comparativa fría. Layout de "dos caminos" con bifurcación
visual — una línea que entra por la izquierda y se separa en dos, cada rama con
un ícono simple (línea 1.5px) y 2-3 palabras clave. La rama "Evolucionar AIDA"
se subdivide otra vez en i / ii.
El acento rojo marca la bifurcación misma, no una de las dos ramas — la lámina
plantea la decisión, no la resuelve visualmente.
-->

---

`LA DECISIÓN DE HOY`

# Qué cambia entre un camino y el otro

### Dato que entrega RIMAC
**POC — Overlap:** datos internos y de clientes al proveedor externo.
**Evolucionar AIDA:** ninguno sale de la compañía — todo el desarrollo es interno.

### Punto de partida
**POC — Overlap:** herramienta de terceros, sin historial de uso ni de errores en RIMAC.
**Evolucionar AIDA:** ya existe evidencia acumulada (este diagnóstico) y un prototipo funcional corriendo.

## La pregunta detrás de esta decisión: ¿la brecha de AIDA es una razón para reemplazarla por un proveedor externo, o para terminar de construir lo que Behavioral Design y Service Design ya empezaron a validar internamente?

▸ Lo que viene a continuación es exactamente ese prototipo — para que la decisión no sea sobre una promesa, sino sobre algo que ya puedes ver funcionando.

<!--
LÁMINA 24 · Dos caminos, el contraste [fuente: Lámina 8, filas de comparación]
LAYOUT: dos criterios × dos columnas, maquetado como bloques, no como tabla.
La pregunta de cierre en Fraunces grande, cruzando el ancho completo, sobre
fondo papel — es la frase con la que conviene dejar la lámina proyectada
mientras se abre la demo.
NOTA: la tabla comparativa completa del documento fuente sirve como handout
impreso, no necesariamente como lámina proyectada.
-->

---

# Te presentamos Maveric

## El prototipo que Behavioral Design y Service Design ya construyeron — para mostrar, no para prometer.

<!--
LÁMINA 25 · Transición Maveric [fuente: Lámina 9, título y lead]
ARTE: siluetas de aviones de combate en formación (referencia directa a Top Gun)
de fondo, en tratamiento blueprint/línea — mismo lenguaje visual que la carátula
(auto de carrera), ahora escalado a aviación: el copiloto que demostró que puede
volar. Título grande, centrado, "Maveric" en el tratamiento de "concletter" que
ya usa el resto del deck (letra grande, acento rojo).
Es la lámina más "de aire" del deck: solo título y lead, nada más.
-->

---

`SUGERENCIA ESTRATÉGICA · A VALIDAR CONTIGO`

# Por qué "Maveric" y no un nombre corporativo más

Relanzar el copiloto bajo el nombre **Maveric**, alineado a la nueva estrategia de motivación comercial **Escuadrón RIMAC** — que ya usa call signs, insignias y el resto del universo Top Gun para movilizar y motivar a la fuerza de ventas.

- No es solo un nombre nuevo para la misma herramienta: es **sumar el copiloto a una narrativa que el canal ya reconoce** y con la que ya se identifica.
- La alternativa es lanzar una capacidad más con un nombre corporativo genérico que **compite por atención contra AIDA**.
- El relanzamiento del nivel Hábito (lámina 21) puede apalancarse directamente en esta narrativa ya instalada, en vez de construir una nueva desde cero.

<!--
LÁMINA 26 · La propuesta de nombre [fuente: Lámina 9, bloque estratégico]
ARTE: mismo fondo blueprint de aviones que la lámina 25, pero al 10% de opacidad
para dejar leer el cuerpo. La insignia/call sign de Escuadrón RIMAC, si existe
como asset, va arriba a la derecha.
⚠️ Marcar visiblemente el kicker "A VALIDAR CONTIGO" — es propuesta del equipo,
no hallazgo del diagnóstico, y la distinción tiene que ser evidente en pantalla.
Se separó de la lámina 25 para que la transición respire y el argumento de
nombre se discuta con la cabeza fría, no encima del impacto visual.
-->

---

`DEMO EN VIVO`

# Una sola solución para tres casos de uso

- **a. Consulta** *(no es foco de este prototipo, por temas de seguridad de la información)*
- **b. Selección y Entrenamiento**
- **c. Dashboard de gestión**

<!--
LÁMINA 27 · Demo [fuente: Lámina 10]
GRÁFICO: tres tarjetas horizontales, una por caso de uso, solo el nombre + ícono
simple — SIN descripción. Es la lámina "ancla" antes de la demo interactiva: el
detalle de cada caso se explica en vivo, no en la lámina.
La tarjeta "Consulta" en tono atenuado/gris para señalar visualmente que no es
foco; las otras dos con el tratamiento normal en tinta/papel.
⚠️ PENDIENTE DE CONTENIDO: reemplazar por capturas o mockups reales del
prototipo Maveric cuando estén disponibles (ver lámina de respaldo).
NOTA DE ORADOR: dejar esta lámina proyectada al salir a la demo; volver a ella
al terminar cada caso de uso.
-->

---

`A QUÉ LE APUNTAMOS`

# Los indicadores de productividad a los que esperamos pegarle

## Esta es la vara con la que se va a medir cualquiera de los dos caminos — no una lista aparte de aspiraciones.

### 1. Ramp-up de asesores
Que los asesores junior empiecen a vender más rápido — que la curva de aprendizaje (promesa secundaria 1) se acorte en la práctica, medida en tiempo hasta el primer nivel de productividad esperado.

### 2. Buena venta como entendimiento de los parámetros básicos del producto
Traducido en un indicador concreto: **reducción de reclamos**. Si el asesor entiende bien coberturas, exclusiones y condiciones desde la consulta o el entrenamiento, eso se ve después en menos reclamos por mala venta o mala explicación.

### 3. Buena venta como resultado comercial
Mayor conversión por asesor, mayor recomendación y mayor renovación — el mismo trío que ya nombra la promesa secundaria 2, ahora como los indicadores contra los que se va a evaluar el impacto real de Cimiento, Hábito y Retorno.

▸ Ninguno de estos tres indicadores existe hoy en el dashboard de AIDA — es, literalmente, lo que la etapa Retorno del mapa de soluciones está diseñada para instalar.

<!--
LÁMINA 28 · Cierre, indicadores [fuente: Lámina 11]
GRÁFICO: tres columnas simples tipo "de dónde venimos → qué medimos", cada una
con un ícono de línea (reloj para ramp-up, escudo/documento para reclamos,
flecha ascendente para conversión/recomendación/renovación).
SIN CIFRAS, a propósito: hoy no existe la línea base — el dashboard actual no
mide nada de esto (lámina 13). Esta lámina es la contraparte visual exacta de
la 13: allá cinco chips con X, aquí tres columnas con contenido pero sin número.
La ausencia de cifra aquí es el argumento, no una omisión.
-->

---

`CIERRE`

# La decisión que te dejamos

## ¿Aceptamos el POC del proveedor externo, o terminamos de construir lo que ya está funcionando adentro?

AIDA no falla por falta de adopción. Falla en el terreno exacto donde el asesor la necesita: el dato que decide la venta. Eso se arregla con contenido, hábito y medición — en ese orden — y ya hay un prototipo que lo demuestra.

<!--
LÁMINA 29 · Cierre [lámina nueva, no está en el documento fuente]
ARTE: vuelve la ilustración de la carátula (cabina, piloto y copiloto), ahora
con el copiloto en rojo pleno en lugar de solo delineado — el arco visual se
cierra: el copiloto se ganó el asiento.
Propuesta del equipo: el documento fuente termina en la lámina de indicadores,
que es un cierre técnico. Una reunión de decisión conviene cerrarla con la
pregunta de decisión en pantalla. Quitar si prefieres cerrar en la 28.
-->

---

`RESPALDO · NO PROYECTAR`

# Vacíos de contenido a completar antes del deck final

- **Proveedor del POC:** el nombre real detrás de "Overlap" y cualquier condición conocida del piloto — costo, plazo, alcance de datos solicitados. *(Lámina 23-24)*
- **Prototipo Maveric:** capturas o mockups reales para reemplazar las descripciones funcionales. *(Lámina 27)*
- **Validación de esfuerzo y owners:** los niveles ●/●●/●●● y los owners (Canales, Producto/Gen AI, Learning, CoE Diseño y Experiencia, Calidad/EDA, Mantenimiento) se asignaron con criterio propio a partir de la naturaleza de cada ítem — **no están confirmados con las áreas dueñas**. *(Láminas 19-22)*

### Procedencia del contenido
Todo el resto —hallazgos, cifras, verbatims, veredicto— proviene del diagnóstico ya validado: encuesta a 19 asesores, auditoría documental con Claude sobre 46 preguntas, entrevistas a 4 asesores, logs reales de 3.606 consultas, entrevista a la PO y dashboard de adopción de 242.785 consultas. **No se inventó ni se redondeó ningún dato.**
Contenido propuesto para esta versión y marcado como tal: niveles de esfuerzo y owners del mapa de soluciones, encuadre de "Maveric", y la lámina 29 de cierre.

<!--
LÁMINA 30 · Respaldo [fuente: Notas de cierre del documento]
Borrar antes de presentar, o dejarla al final del archivo de Figma fuera del
rango de proyección (Figma Slides permite ocultar láminas: clic derecho >
Hide slide). Sirve como checklist de producción del deck.
-->
