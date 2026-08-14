# Arquitectura de base de conocimiento para agentes de Copilot (y agentes RAG en general)

> Node. Fuente de verdad de este tema: **cómo debe almacenarse la información para que un agente
> construido sobre Microsoft Copilot la consuma bien**, con la evidencia que lo respalda. Es la
> capa de **evidencia externa** — el estado y las decisiones internas del Copiloto AI de RIMAC
> viven en `_nodes/diagnostico-copiloto-ai-asesor-vida-rimac.md`, que consume este node.
>
> Fecha de elaboración: 2026-08-14 · Última actualización: 2026-08-14 · Versión: v1.1
> (v1.1, mismo día: agrega §8 — **uno o varios agentes**, y por qué consolidar bases de conocimiento
> es distinto de consolidar la interfaz. Cambio estructural: el node pasa de cubrir *cómo se escribe
> el contenido* a cubrir también *cómo se reparte entre agentes*, que es una decisión anterior.
> Fuentes nuevas: F-479, F-480.)
> Origen: investigación disparada por el diagnóstico del Copiloto AI del asesor de Vida (RIMAC),
> a pedido del usuario: "buscando evidencia o justificándome cuál es la forma correcta de
> almacenar información para que este agente copiloto consuma la información".
> Fuentes: F-469 a F-475, F-479 y F-480 del ledger de `cronista` (`research/fuentes/codice.md`).

---

## 0. Veredicto

Sí hay una forma correcta, está documentada por el propio fabricante, y **es casi exactamente lo
contrario de lo que un equipo comercial produce naturalmente.**

La respuesta corta, en una línea: **texto plano, corto, monotemático, estructurado por
encabezados, sin tablas, con un resumen al inicio, con dueño y fecha de revisión.**

La respuesta incómoda: el PPT bonito, el PDF con tablas de coberturas y el brochure diseñado
—los artefactos que más trabajo cuestan y mejor se ven ante un humano— son **los peores
insumos posibles para el agente**. No es una cuestión de prolijidad. Es que la información que
vive en la *disposición visual* de una lámina (columnas, cajas, jerarquía tipográfica, iconos)
no sobrevive a la extracción de texto: llega al agente como una lista de fragmentos sueltos sin
la relación que los hacía significar algo.

⚠️ **Fecha de caducidad declarada.** Todo lo que sigue describe el comportamiento de un producto
comercial que cambia rápido. Las cifras concretas (36.000 caracteres, 7 MB, 512 MB) hay que
**reverificarlas contra la documentación vigente antes de tomar una decisión de arquitectura**,
no citarlas de memoria dentro de seis meses. Lo que sí es estable es el principio, que además
está respaldado desde fuera del fabricante (§4).

---

## 1. El malentendido de origen

Casi todas las bases de conocimiento de agentes empresariales nacen del mismo movimiento:
*"tenemos una carpeta con todo lo del producto — conectémosla al agente."*

Ese movimiento asume que una **base documental para personas** y una **base de conocimiento para
un agente** son la misma cosa con distinto lector. No lo son:

| | Repositorio para personas | Base de conocimiento para un agente |
|---|---|---|
| **Unidad útil** | El documento completo | El **fragmento** recuperable (chunk) |
| **Navegación** | La persona busca, hojea, descarta, interpreta | El sistema recupera ~3-5 fragmentos y responde **solo con eso** |
| **Duplicados** | Molestos pero inofensivos — la persona elige el bueno | **Tóxicos** — el sistema no sabe cuál es el vigente y puede citar el viejo con total seguridad |
| **Documento vacío o de una línea** | Ruido visual ignorable | Contamina la recuperación y compite por espacio |
| **Formato visual (PPT, infografía)** | Aumenta la comprensión | **Destruye** información: lo que significaba la maqueta no llega |
| **Tabla** | La forma más clara de comparar | Se aplana en una cadena de valores desconectados |
| **Documento largo que cubre 6 temas** | Cómodo: todo en un lugar | Diluye: el fragmento correcto compite con cinco temas irrelevantes del mismo archivo |

La consecuencia práctica es que **migrar la carpeta al agente no es migrar: es reescribir.** Y es
un trabajo de contenido, no de TI.

---

## 2. Matriz de formatos — qué consume, qué degrada, qué es invisible

Según la documentación de producto (F-469, F-470, F-473):

| Formato | Estado | Qué pasa realmente |
|---|---|---|
| **Word (.docx)** | ✅ Soportado | El mejor de los formatos "de oficina": texto estructurado por estilos de encabezado. |
| **Texto/Markdown/HTML** | ✅ Óptimo como contenido | Máxima fidelidad de estructura. ⚠️ En Copilot Studio, **`.txt` y `.json` no se aceptan como archivo cargado** de base de conocimiento — el camino es página de SharePoint o `.docx`. |
| **Página de SharePoint** | ✅ Soportado y recomendado | Es el formato que el fabricante optimiza explícitamente (F-472). |
| **PDF (con texto real)** | ✅ Soportado | Único formato con **citas a nivel de página**; el resto degrada a cita a nivel de documento (F-469). |
| **PDF escaneado / basado en imagen** | ❌ **Invisible** | El agente **solo puede referenciar el título del archivo, no accede al contenido** (F-473). |
| **PowerPoint (.pptx)** | ⚠️ Soportado con pérdida severa | Se extrae el texto, con límite de caracteres. Se pierde la maqueta — que en un deck comercial **es** el contenido. |
| **Excel (.xlsx)** | ⚠️ Soportado con pérdida | Cae de lleno en el problema de tablas de §4. |
| **Imágenes sueltas (.jpg, .png)** | ❌ **No soportadas** como documento cargado | Solo se leen **embebidas en un PDF y anotadas con alt-text**. Una imagen sin descripción textual es invisible (F-469). |
| **Video / audio / ejecutables** | ❌ No soportados | Para multimedia **solo se indexa la metadata**, no el contenido (F-470). |
| **Archivos cifrados o con etiqueta de sensibilidad** | ❌ No soportados | Incluye protección por contraseña **y etiquetas de sensibilidad** (F-469) — trampa frecuente en corporativos, donde la etiqueta se aplica por política automática. |
| **Documentos vacíos o casi vacíos** | ⚠️ Bajo el umbral | Por debajo de ~4 KB degradan a cita a nivel de documento (F-470); además ocupan lugar en la recuperación sin aportar nada. |

### El modo de falla más peligroso

Ninguno de estos casos produce un error visible. **El agente no dice "no pude leer este PDF".**
Responde igual — con lo que sí encontró, que puede ser un documento viejo, un fragmento de otro
producto, o su propio conocimiento general. Desde afuera se ve como "el copiloto se inventó
algo"; desde adentro fue un archivo que nunca entró al índice.

---

## 3. Los tres techos — por qué un archivo "está ahí" y aun así no se puede responder sobre él

1. **Techo de tamaño por licenciamiento (F-470).** Con licencia de Microsoft 365 Copilot en el
   mismo tenant: hasta **200 MB**, y requiere tener activado *Tenant graph grounding with semantic
   search*. **Sin** esa licencia en el mismo tenant: la generación de respuestas solo puede usar
   archivos de SharePoint **menores a 7 MB**. La diferencia es de casi 30×, y **un deck comercial
   con imágenes pasa los 7 MB con facilidad.** Esta es la primera cosa a verificar en cualquier
   diagnóstico: bajo qué licencia opera el agente.
2. **Techo de longitud por archivo (F-471).** Máximo recomendado **36.000 caracteres (~15-20
   páginas)** por archivo; por encima, el fabricante recomienda **partirlo en archivos más
   cortos** para que el agente pueda recorrer el contenido completo.
3. **Techo de volumen total (F-471).** El conjunto de archivos relevantes referenciados debería
   mantenerse en **≤300 páginas**. ⭐ Esto es lo más contraintuitivo de todo el node: **más
   documentación no es mejor agente.** Pasado cierto punto, agregar documentos **degrada** las
   respuestas, porque cada documento nuevo es un competidor más por los pocos fragmentos que el
   sistema va a recuperar.

---

## 4. Las siete reglas de redacción

Estas son las reglas del propio fabricante (F-471, F-472), con el respaldo externo indicado.

1. **Sin tablas.** Literal: *"Copilot is currently unable to parse tables and other special
   formatting in SharePoint content"*, y recomienda **quitar las tablas y el formato especial**
   antes de exponer el contenido al agente (F-471). Una tabla de coberturas debe reescribirse
   como prosa con encabezados: *"### Cobertura por fallecimiento — Qué cubre: … · Suma asegurada:
   … · Exclusiones: …"*.
2. **Encabezados y viñetas por encima de tablas.** *"LLMs prefer well-structured, contextualized
   text over tables"* (F-471). El encabezado no es decoración: es la unidad por la que el sistema
   corta y recupera.
3. **Resumen conciso al inicio de cada documento.** Ayuda al modelo a entender tema, propósito y
   audiencia, y **a aterrizar la respuesta en la sección correcta** en vez de tomar información de
   la parte equivocada de un documento largo (F-471).
4. **Un documento, un tema.** Páginas *escaneables y monotemáticas* (F-472). Un documento que
   cubre seis temas se recupera mal para los seis.
5. **Corto.** ≤36.000 caracteres; partir lo que exceda (F-471, ver §3).
6. **Autosuficiencia del fragmento.** Cada sección debe poder leerse sola. Referencias como *"como
   se explicó arriba"* o *"ver la lámina anterior"* se rompen al trocear: el fragmento recuperado
   no lleva el "arriba" consigo.
7. **Nombres de archivo y títulos descriptivos.** El título es señal de recuperación, y para
   formatos degradados **es lo único que el sistema tiene** (F-473).

### Respaldo externo al fabricante

La regla 2 —estructurar explícitamente— no depende de creerle a Microsoft. Dos preprints
independientes convergen: el troceado **consciente de la estructura del documento** rinde mejor
en efectividad de recuperación *y* a menor costo computacional que las estrategias semántica y de
tamaño fijo (F-474), y las estrategias estructuralmente informadas **superan a las de tamaño fijo
siendo además más robustas** — menos sensibles al modelo de embedding usado (F-475).

⚠️ Ambos son **preprints sin revisión por pares y de dominio único**, registrados por convergencia
mutua y con el fabricante, no por autoridad propia. Lo que sostienen bien es la **dirección**
(estructurar mejora recuperación), no una magnitud.

⭐ El hallazgo de **robustez** de F-475 es el más valioso estratégicamente: estructurar bien el
contenido **protege el resultado aunque la plataforma cambie su motor por debajo.** Es la mejor
respuesta al riesgo de caducidad declarado en §0 — y el argumento para invertir en el contenido
antes que en la configuración del agente.

---

## 5. La capa que casi siempre se olvida: gobierno

El fabricante propone como **métrica de efectividad del propio Copilot la reducción de contenido
ROT** (Redundante, Obsoleto, Trivial) y la mejora de localizabilidad (F-472). Es decir: **limpiar
la base no es un prerrequisito del proyecto, es parte del proyecto y una de sus métricas.**

Lo que recomienda explícitamente (F-472):

- **Metadata consistente** por documento: tipo de documento, país/región, **dueño** y **fecha de
  revisión**. El fabricante afirma que la metadata rica y consistente mejora *"tanto la exactitud
  como la completitud"* de las respuestas, porque permite filtrar y priorizar lo vigente.
- **Term sets** reutilizables (tipo de documento, línea de producto, función), que además pueden
  usarse como variables en Copilot Studio.
- **Políticas de versionado, retención y revisión**, para que el agente se apoye en fuentes
  vigentes y autoritativas.
- **Arquitectura de información simple** y accesos bien gobernados.

El punto de fondo: **un duplicado desactualizado no es un archivo de más, es una respuesta
incorrecta esperando a ser recuperada.** Frente a dos versiones del mismo documento, el sistema no
tiene forma de saber cuál manda — salvo que la metadata se lo diga. Por eso "un dueño y una fecha
de revisión por documento" no es burocracia: es la única señal de vigencia que el agente puede
leer.

---

## 6. Protocolo de auditoría de una base existente

Orden recomendado para diagnosticar una base ya cargada (cada paso es barato y descarta una causa):

1. **Inventario con conteo por extensión y por peso.** Cuánto hay de cada formato de §2.
2. **Prueba del texto seleccionable.** Abrir cada PDF e intentar seleccionar texto. Si no se puede,
   es un PDF imagen: **el agente solo ve el título** (F-473). Esta prueba sola suele explicar una
   fracción grande de las quejas de "no encuentra la información".
3. **Prueba del techo de licencia.** Confirmar bajo qué licencia opera el agente y contar cuántos
   archivos superan el umbral que aplica — 7 MB o 200 MB (F-470).
4. **Detección de vacíos y casi-vacíos.** Todo lo que pese menos de ~4 KB (F-470).
5. **Detección de duplicados y casi-duplicados.** Especialmente versiones del mismo documento con
   nombres distintos: es la causa raíz de las **respuestas inconsistentes** (la misma pregunta
   contestada distinto en dos momentos), porque cada consulta puede recuperar una versión distinta.
6. **Detección de archivos cifrados o con etiqueta de sensibilidad** (F-469).
7. **Recién entonces**, medir la calidad de las respuestas con los instrumentos del node
   `[[evaluacion-calidad-agentes-conversacionales-ia]]` (faithfulness / context precision de RAGAS,
   F-151). Medir antes de limpiar solo confirma que está mal, sin decir por qué.

---

## 7. Qué NO dice esta evidencia

Honestidad sobre los límites, para que este node no se cite más fuerte de lo que es:

- **No dice que limpiar la base arregle el agente.** Dice que sin base limpia, el agente no puede
  funcionar bien. Es condición necesaria, no suficiente — las fallas de comportamiento e
  instrucciones son otra capa (ver §3 del node de diagnóstico).
- **No hay un estudio con muestra que cuantifique cuánto mejora la exactitud al reformatear una
  base corporativa.** No existe un "+X% por quitar las tablas". Lo que hay es documentación
  normativa del fabricante + dos preprints sobre troceado. **Cualquier cifra de mejora que aparezca
  en un blog de proveedor sobre esto debe tratarse como sospechosa de eco de cita** — la disciplina
  del proyecto sobre cadenas de eco (ver reglas C19-C22 en `[[tendencias-diseno-innovacion]]`)
  aplica de lleno a este mercado, que está saturado de proveedores de parsing vendiendo urgencia.
- **Ninguna fuente de Microsoft se leyó de primera mano**: `learn.microsoft.com` está bloqueado por
  el proxy de red del entorno; se reconstruyeron por búsqueda dirigida. Las dos afirmaciones más
  consecuentes —el límite de 36.000 caracteres y la incapacidad de parsear tablas— se verificaron
  con **dos pasadas independientes de redacción coincidente**, pero conviene confirmarlas contra la
  página viva antes de comprometer un rediseño grande.
- **No cubre Claude Projects ni otras plataformas.** Si el agente en cuestión no corre sobre
  Copilot, los principios de §1, §4 y §5 se transfieren (son propiedades de cómo funciona la
  recuperación, no del proveedor), pero **los límites numéricos de §2 y §3 no aplican.**

---

## 8. Uno o varios agentes — y qué significa "consolidar"

Decisión anterior a todo lo de arriba: **antes de escribir el contenido hay que decidir cuántas
bases habrá y cuántos agentes las consumirán.** Es donde se equivoca la intuición más común en
empresas — *"unifiquemos todo en un solo asistente para que la gente no tenga que aprender dónde
buscar"*.

Esa intuición es **correcta sobre la interfaz y equivocada sobre la recuperación**, y hay que
separarlas:

| Capa | Consolidar | Por qué |
|---|---|---|
| **Interfaz** — a cuántos lugares va el usuario | ✅ **Sí** | Menos superficies, menos carga cognitiva |
| **Recuperación** — cuántas bases hay detrás | ❌ **No** | Mezclar dominios degrada la exactitud (abajo) |

### Por qué mezclar dominios degrada la recuperación

- **Fabricante (F-479):** asignar a cada subagente **fuentes distintas y no superpuestas** — si dos
  buscan en la misma base, uno encuentra primero y el otro devuelve duplicados o se salta la
  búsqueda, sin aportar valor. Y **"multi-agente aporta valor solo cuando las fuentes son
  genuinamente distintas"**: con una sola fuente, **no dividir**.
- **Externo (F-480, preprint):** centralizar todos los documentos en un solo sistema RAG **agranda
  el espacio de recuperación y aumenta la evidencia irrelevante**; la señal-ruido cae cuando las
  bases no se separan por dominio. Particionar y rutear **reduce el ruido y la interferencia entre
  temas**, con mayor exactitud y **menor alucinación**.

⭐ Es coherente con el techo de ≤300 páginas de §3: **el problema de una base gigante no es de
almacenamiento, es de competencia entre fragmentos.** Cada documento irrelevante que entra al mismo
espacio de recuperación compite con el relevante. Consolidar bases es agrandar esa competencia.

### Los criterios del fabricante para separar (F-479)

Un dominio merece su propio agente/base cuando cumple alguno:

1. Tiene **expertise propio** (otro cuerpo de conocimiento, no un subtema del mismo).
2. Requiere **reglas de gobierno o control de acceso distintas** — el criterio más subestimado, y el
   que suele decidir en dominios regulados.
3. Es **reutilizable como servicio** por varios agentes principales.

Regla de arranque del propio fabricante: **empezar con un agente** y dividir solo cuando aparezca
una necesidad clara de modularidad o *"un límite que un solo agente no debería cruzar"*. No
sobre-arquitecturar al inicio.

### El patrón que satisface ambas capas

**Una puerta de entrada, varios dominios detrás:** el usuario habla con un solo agente, que rutea a
la base correcta. Está soportado explícitamente en Copilot Studio (orquestación multi-agente) — no
requiere desarrollo a medida.

⚠️ **Advertencia de secuencia:** poner una puerta única delante de bases cuya calidad no se ha
auditado **destruye la señal de diagnóstico** — el usuario deja de saber cuál dominio falló, y el
equipo pierde la capacidad de atribuir el error. **La auditoría (§6) va antes que la consolidación
de interfaz.**

---

## Conexiones

- [[diagnostico-copiloto-ai-asesor-vida-rimac]] — el caso que originó este node: el consumidor
  directo de estas reglas. Este node dice *cuál es la forma correcta*; ese node dice *qué está
  pasando hoy en RIMAC y qué hacer al respecto*.
- [[evaluacion-calidad-agentes-conversacionales-ia]] — cómo **medir** si el agente responde bien,
  una vez que la base está en condiciones. Los tres ejes que no hay que mezclar y las métricas RAG
  (RAGAS) son el instrumento del paso 7 del protocolo de §6.
- [[proyecto-back-to-basics-ffvv-vida]] — el proyecto marco. Su backlog ya nombraba "resolver la
  consistencia de respuestas del copiloto de IA" como prioridad de corto plazo; este node aporta el
  mecanismo causal candidato (§6, duplicados y casi-duplicados).
- [[material-visual-venta-consultiva]] — tensión productiva a tener presente: ese node documenta que
  el material visual **reduce la incertidumbre del cliente** en la venta consultiva. Este node
  documenta que el material visual **es ilegible para el agente**. No se contradicen: implican que
  el material visual y la base de conocimiento son **dos artefactos distintos con dos audiencias
  distintas**, y que producir uno no produce el otro.
