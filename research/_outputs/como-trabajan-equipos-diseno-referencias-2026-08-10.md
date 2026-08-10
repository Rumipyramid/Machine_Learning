# Cómo trabajan equipos de diseño con estos cuatro roles

### Referencias externas y peruanas para el modelo de trabajo del equipo

> Complemento de `revision-modelo-trabajo-diseno-2026-08-10.md`. Fecha: 2026-08-10.
> Roles considerados: **Product Designer · Service Designer · Behavioral Designer · UX Researcher**.
> Fuentes nuevas registradas en `research/fuentes/codice.md` como **F-483 a F-500**.
>
> ⚠️ **Limitación de lectura, declarada por adelantado.** 8 de las 18 fuentes de este barrido no
> pudieron leerse a texto completo por bloqueo de egreso del entorno (nngroup, behavioralscientist,
> mckinsey, gov.uk, gestion.pe, povertyactionlab, medium). Están reconstruidas desde resúmenes de
> buscador y marcadas como tales en el ledger. No es mala suerte: es una restricción estructural del
> entorno, ya registrada tres veces en el proyecto. Donde importa, lo digo en el punto.

---

## 0. El resumen en cinco líneas

1. **Ningún equipo de referencia organiza estos roles por artefacto.** Los que funcionan los
   separan por **unidad de análisis** y por **quién es dueño del resultado**.
2. **El benchmark de composición más citado es viejo y su propio autor advierte contra usarlo**:
   1 investigador : 5 diseñadores (F-483, dato de 2020).
3. **El tamaño del equipo no predice el impacto** — en la encuesta más grande que existe sobre el
   tema, hay equipos grandes en el nivel más bajo de madurez y equipos pequeños en el más alto (F-496).
4. **En Perú sí hay precedentes, y el más cercano al equipo es el CIX del BCP** — que declara casi
   exactamente el mismo set de roles (F-493). Pero ninguno publica resultados auditados.
5. **El mejor modelo de gobernanza de evidencia del país no es de diseño: es MineduLAB** (F-491).
   Y es el contraejemplo peruano al hallazgo más duro de la investigación anterior.

---

## 1. Los cuatro modos de organizar la función

Toda la literatura converge en las mismas tres formas, más una cuarta que casi nadie nombra pero
que es la más frecuente en la práctica.

| Modo | Cómo se ve | Qué resuelve bien | Dónde falla |
|---|---|---|---|
| **Centralizado** (CoE, laboratorio) | Un equipo único al que se le pide trabajo | Estándares, formación, consistencia, masa crítica de especialistas escasos | Distancia del contexto operativo; se vuelve cola de pedidos; **el conocimiento tácito se pierde en la entrega** |
| **Embebido** | Cada diseñador vive dentro de un equipo de producto o journey | Relevancia, velocidad, contexto | Suboptimización, inconsistencia entre equipos, especialistas aislados sin par con quien crecer |
| **Híbrido (hub + spokes)** | Núcleo central que gobierna método, sistema y estándares; ejecución en los equipos | Es a lo que converge casi todo el que pasa de la fase experimental | Requiere decidir explícitamente qué gobierna el hub — si no, reproduce los dos problemas a la vez |
| **Consultoría interna por proyecto** | Se contrata al equipo caso por caso | Bajo costo de arranque | **Es el modo donde el behavioral design se queda atrapado**: chispa, no llama sostenida (F-487) |

**El dato regional.** Mercado Libre es el ejemplo más claro de híbrido a escala: creó un equipo
central **"UX Core"** con el sistema de diseño *Andes* como infraestructura compartida, mientras la
organización opera descentralizada por país. Su equipo de UX se triplicó en una década (F-499).
⚠️ Es un *customer story* publicado por Figma — el proveedor contando la historia de su propio
producto. Vale como forma organizativa observada, no como evidencia de que funcione mejor.

**Una advertencia sobre el modo centralizado, que es el que el equipo tiene.** Circula una
afirmación de que las organizaciones con Centros de Excelencia de alta demanda rinden
significativamente peor que las descentralizadas, atribuida a los estudios DORA. **No pude
localizar la publicación DORA que lo respalda** (F-498). La registro con la advertencia explícita
de que tiene la forma exacta de la autoridad prestada que este proyecto ya documentó seis veces.
No la usen en un deck hasta verificarla contra el informe primario.

---

## 2. Los cuatro roles, según equipos que sí los tienen

### 2.1 El reparto de roles mejor documentado del mundo, y lo que le sobra a este equipo

El **Service Manual del gobierno británico** (F-489) es el estándar operativo de roles de diseño
con más kilometraje público: 10+ años, cientos de servicios, versionado a la vista de todos. Define
el equipo por roles con fronteras escritas: investigador de usuarios · diseñador de interacción ·
diseñador de servicio · diseñador de contenido · gestor de producto · gestor de entrega · **analista
de desempeño**.

⭐ **El hallazgo está en el último de la lista.** El estándar más maduro que existe incluye un rol
dedicado a **medir el desempeño del servicio después de lanzado** — y ese rol no está en este equipo,
ni en la mayoría de equipos de diseño corporativos.

Esto conecta directo con R1 y R4 del informe anterior. La pregunta "¿sirvió?" no se queda sin
responder por falta de voluntad: se queda sin responder porque **no es el trabajo de nadie en
particular**. En el estándar británico sí lo es.

### 2.2 Behavioral design: cómo se organizan los equipos que existen

Tres datos que reordenan las expectativas sobre este rol.

**Los equipos son diminutos.** 63% de los equipos de ciencias del comportamiento tiene entre 1 y 5
personas; 20% entre 6 y 10. Es habitual encontrar **una sola persona** designada como "la persona de
comportamiento" en una empresa global grande (F-486). Un equipo de behavioral design de una o dos
personas no es una versión incompleta de algo: **es la moda de la distribución**.

**La mayoría del trabajo no ocurre dentro de las organizaciones.** 55% de quienes hacen ciencias del
comportamiento aplicada son consultoras o contratistas; el resto tiene equipos embebidos en
departamentos existentes (F-486). Tener la función adentro ya es la opción minoritaria.

**Y hay una tesis fuerte sobre por qué eso importa.** ideas42 (F-487) lo formula así: *"la diferencia
entre insights conductuales ocasionales y un equipo de diseño conductual embebido es como la
diferencia entre una chispa y una llama sostenida."* ⚠️ Con el descuento obvio: ideas42 vende el
modelo embebido que recomienda. Pero dos de sus observaciones operativas se sostienen solas:

- **El patrón de arranque es empezar por un diseño que ya funcionó en otro lado** y escalar desde
  ahí hacia cambios más profundos. No empezar por lo original: empezar por lo replicado.
- **El factor de éxito declarado es respaldo en todos los niveles, de la dirección a la primera
  línea** — no solo patrocinio ejecutivo. Un equipo conductual con apoyo del directorio y sin apoyo
  del contact center no puede ejecutar.

Los dos modelos estructurales que la encuesta global identifica son: **unidad independiente que
reporta a un ejecutivo senior**, o **función distribuida embebida en equipos de producto**. La
tercera opción —consultoría interna caso por caso— es precisamente la que produce chispas.

### 2.3 UX Research: el rol bajo la mayor presión estructural del campo

Los números de la encuesta anual del sector (F-484) describen un cambio de fondo, no un ciclo:

| Indicador | 2020 | 2025 |
|---|---|---|
| Proporción "gente que investiga : investigadores dedicados" | **2 : 1** | **5 : 1** |
| Organizaciones con gente haciendo investigación sin ser investigadora | — | **71%** |
| Organizaciones que despidieron investigadores en el año | — | **21%** |
| Investigadores con mal pronóstico sobre el futuro de su disciplina | 23% | **49%** (+26 pts) |

**Cómo leerlo sin caer en la lectura fácil.** La conclusión apurada es "el rol se está muriendo".
La lectura más defendible es otra: **la ejecución de investigación se distribuyó y lo que quedó
escaso es el criterio**. Cuando cinco personas por investigador hacen estudios, el cuello de botella
deja de ser hacer estudios y pasa a ser garantizar que los estudios que se hacen valgan algo — qué
pregunta merece un estudio, qué método aguanta la decisión que se va a tomar, qué hallazgo no
resiste.

⚠️ **Y una fuente que hay que leer con máxima desconfianza.** El informe más citado sobre el recorte
de investigadores (F-485) lo publica una empresa que vende la herramienta de IA que ese mismo
informe presenta como sustituto del rol recortado. Es el conflicto de interés en su forma más pura.
No lo usen como evidencia de nada.

### 2.4 Service design: escalar la función es fácil, demostrarla no

El caso mejor documentado de escalamiento de diseño de servicios dentro de una organización grande
es el del gobierno británico (F-490): cuadruplicaron los diseñadores de servicio en GDS, la
estrategia de internalización abrió camino a **más de 800 diseñadores** contratados en el gobierno,
formaron **540 servidores públicos en 20 corridas del taller en 20 meses**, y montaron una serie de
eventos con **37 organizaciones y más de 3.000 participantes** en 2021.

⭐ **Miren la lista otra vez: todo lo medido es actividad.** Personas formadas, eventos corridos,
gente contratada. **Ni un solo resultado de servicio.** No es un descuido de este caso en
particular — es la regla **C7** del node de tendencias funcionando en vivo: no existe caso público
de rediseño con métricas de resultado auditadas, ni siquiera en el programa de diseño de servicios
más grande y mejor financiado del mundo occidental.

Es simultáneamente el mejor manual disponible de **cómo escalar la capacidad** y un ejemplo nulo de
**cómo demostrar el impacto**.

---

## 3. Perú: qué hay realmente

### 3.1 CIX del BCP — el análogo más cercano que existe en el país

El Centro de InnovaCXión del BCP opera como *tribu* con tres equipos interrelacionados
—**navegadores + diseño + innovación abierta**— y sus equipos multidisciplinarios se componen de
Design Research Team, Business Team y Technology Team (F-493).

⭐ Lo llamativo es la composición declarada del equipo de diseño:

> *design & behavioral researchers + service designers + user experience designers + user interface
> designers*

**Es casi exactamente el mismo set de roles de este equipo**, en el mismo país, en el mismo sector
financiero, montado hace años. Con una diferencia de nombre que no es menor: allí la figura es
**"behavioral researcher"** agrupada con "design researcher", no "behavioral designer" separado del
UX researcher. Volveré sobre eso en §5.

⚠️ **Dos advertencias.** No pude leer las fuentes a texto completo (bloqueo de egreso a `gestion.pe`);
esto viene de resúmenes. Y **no hay ningún resultado medido publicado** de ese arreglo — es una
descripción de estructura, no evidencia de que funcione.

### 3.2 La Victoria Lab y LaBentana — el modelo de laboratorio separado

La Victoria Lab es el laboratorio del grupo Intercorp, **activo desde 2014 y construido trabajando
con IDEO**; se le atribuyen Innova Schools, Interbank Explora y Cineplanet Chaplin. LaBentana es el
laboratorio de Interbank, formado por los equipos que trabajaron con IDEO entre 2012 y 2013 (F-494).

**Lo que este caso enseña es el modelo, no el resultado.** Es la forma "laboratorio separado del
negocio", que tiene una ventaja real (libertad para explorar) y un costo documentado (la distancia
del backstage operativo, F-476). Ninguno publica retorno auditado — consistente con lo que el
proyecto ya había registrado: **los labs peruanos siguen activos y ninguno reporta resultado**
(F-460).

### 3.3 MineduLAB — el mejor modelo de gobernanza de evidencia del país, y no es de diseño

Lanzado en abril de 2016 con MINEDU, J-PAL, IPA y GRADE. Combina el conocimiento de investigadores
con la experiencia operativa de funcionarios de política pública, y **evalúa rigurosamente antes de
escalar**. Ha diseñado, implementado y evaluado **14 innovaciones**, la mayoría ancladas en economía
del comportamiento — entre ellas "Expande tu Mente" (mentalidad de crecimiento en secundaria) y
programas de SMS a docentes (F-491).

⭐ **Es el contraejemplo peruano al hallazgo más duro del informe anterior.** F-469 mostraba que la
metodología más establecida para sistemas complejos casi nunca llega a la fase de evaluación.
MineduLAB sí llega, sistemáticamente, catorce veces, en el Estado peruano, con presupuesto público.

**Y lo que lo hace posible no es una metodología de diseño.** Es un arreglo de gobernanza: portafolio
acotado, criterio de entrada explícito, socio evaluador externo con estándar propio, y el compromiso
de evaluar *antes* de escalar. Exactamente lo que R6 del informe anterior señalaba como el punto
ciego, resuelto a 20 minutos de distancia en la misma ciudad.

Si hay un solo caso peruano que este equipo debería estudiar en detalle, es este — y no es de un
equipo de diseño.

### 3.4 BE OEFA — la otra unidad conductual peruana

Unidad de economía del comportamiento aplicada a fiscalización ambiental, con **cinco proyectos
ejecutados entre 2019 y 2020** (F-492).

Junto con MineduLAB deja un hecho que vale registrar: **el sector público peruano institucionalizó
ciencias del comportamiento antes que el sector privado peruano.** Es un dato útil para
contextualizar por qué el rol todavía se está definiendo dentro de una aseguradora.

### 3.5 El propio caso

RIMAC declara públicamente un **Centro de Excelencia en Diseño de Experiencia**, en una empresa de
más de 4.000 colaboradores (F-495). Lo registro por una razón práctica: **la figura ya es una promesa
pública, no solo un arreglo interno.** Al escribir el modelo de trabajo conviene tenerlo presente —
un CoE declarado hacia afuera crea expectativa sobre estándares y consistencia, no solo sobre
entrega.

### 3.6 El hallazgo negativo peruano

Aplicando **C7** — la ausencia también informa. Buscando específicamente casos peruanos de equipos
de diseño con estos roles y **resultados medidos publicados**, no encontré ninguno. Ni bancos, ni
aseguradoras, ni retail, ni labs. Tampoco encontré una encuesta de la comunidad de diseño peruana
que permita saber cuántos service designers o behavioral designers hay en el país.

Eso significa dos cosas a la vez: **no hay con quién compararse localmente**, y **el estándar local
a superar es bajísimo**. Publicar un solo caso con métrica auditada pondría a este equipo sin
competencia en el país.

---

## 4. Números de referencia, con su nivel de confianza

| Referencia | Cifra | Confianza | Cómo usarla |
|---|---|---|---|
| Investigador : diseñador (F-483) | **1 : 5** el más reportado (35%); 57% tiene al menos 1:20 | 🔵 B, **dato de 2020**, muestra autoseleccionada | Como orden de magnitud. **La propia NN/g advierte contra usar ratios como medida de madurez** |
| Tamaño de equipo conductual (F-486) | **63% tiene 1-5 personas** | 🔵 B | Para calibrar expectativas: un equipo conductual chico es lo normal, no lo insuficiente |
| Trabajo conductual hecho por consultoras (F-486) | **55%** | 🔵 B | Tener la función adentro ya es la opción minoritaria |
| Madurez de diseño (F-496, N=2.200) | N1 41% · N2 21% · N3 21% · N4 12% · **N5 5%** | 🟡 C, autorreporte, vendor | Como mapa de distribución, no como escalera a subir |
| Impacto en ingresos por nivel (F-496) | **92%** en N5 vs. **22%** en N1 lo reporta | 🟡 C — **es percepción autodeclarada, no impacto auditado** | ⚠️ No usar en un deck como prueba de ROI. Aplica C2 y C11 |
| Tamaño de equipo vs. impacto (F-496) | **No correlacionan** | 🟡 C | ⭐ El dato más útil de la tabla: crecer el equipo no es la palanca |
| Ambigüedad de rol → desempeño (F-497) | **ρ = −.21** | 🟢 A, meta-análisis | Ver §5 |
| Ambigüedad de rol → satisfacción (F-497) | **r = −.46** (conflicto de rol: −.48) | 🟢 A, meta-análisis | Ver §5 |

---

## 5. Solapamiento de roles — la evidencia

> Esta sección presenta **la evidencia sobre fronteras de rol**. La lectura sobre qué hacer con ella
> en este equipo se está discutiendo aparte, antes de proponer cualquier cambio.

### 5.1 Lo que dice la evidencia dura, incluido lo que va contra la recomendación fácil

El meta-análisis de referencia (F-497, 🟢A) encuentra que la ambigüedad de rol correlaciona **−.46
con satisfacción laboral** (y el conflicto de rol, −.48), pero que su relación con **desempeño es
modesta: ρ = −.21**.

⭐ **Calibración honesta, aplicando C1 y C2 a mi propia recomendación:** dejar fronteras de rol sin
definir daña sobre todo **cómo se siente el equipo trabajando**, y bastante menos **lo que el equipo
produce**. Eso justifica ordenar los roles —el efecto sobre satisfacción es grande y bien
establecido— y **desaconseja invertir esfuerzo desproporcionado** en un organigrama perfecto
esperando un salto de resultados. Prometer acumulación, no transformación, también aplica acá.

### 5.2 Cómo trazan la frontera los equipos que la tienen trazada

**Product ↔ Service.** La distinción que más se repite entre practicantes **no es de artefacto, es
de propiedad**: un equipo de producto involucra a otros equipos pero **termina siendo dueño de la
solución**; en diseño de servicios **la solución es co-propiedad de muchos equipos y todos tienen
que estar a bordo** (F-500). De ahí la práctica recomendada: acordar áreas de responsabilidad
explícitamente para no duplicar esfuerzo.

⭐ La consecuencia operativa: **trazar la frontera por quién es dueño del resultado, no por quién
dibuja el journey.** Si se traza por artefacto, se duplica de inmediato — los dos roles hacen mapas
de journey y los dos hacen flujos.

**El reparto institucional.** El estándar británico (F-489) separa por unidad de análisis y mantiene
roles distintos para investigación de usuarios, diseño de servicio, diseño de interacción y diseño
de contenido, **más un analista de desempeño**. Es el reparto más granular que existe y, aun así, la
función que casi nadie replica es la última.

**El precedente peruano usa otro corte.** El CIX del BCP agrupa **"design & behavioral researchers"**
como una sola familia de investigación, y separa service designers de UX y UI designers (F-493).
Es decir: el corte que hace el análogo peruano más cercano **no pasa entre "investigador" y
"conductual"** — pasa entre investigar y diseñar.

---

## 6. Qué se lleva este equipo de cada referencia

| Referencia | Qué aporta que el equipo no tenga hoy |
|---|---|
| **Service Manual británico** (F-489) | La existencia de un rol que **mide el servicio después de lanzado**. Es la respuesta institucional a R1 y R4 |
| **MineduLAB** (F-491) | El modelo de gobernanza que hace que la evaluación ocurra: portafolio acotado, criterio de entrada, evaluador externo, evaluar antes de escalar |
| **ideas42** (F-487) | El patrón de arranque conductual —empezar por lo que ya funcionó en otro lado— y el requisito de respaldo hasta la primera línea |
| **Encuesta global de equipos conductuales** (F-486) | La calibración de tamaño: un equipo conductual pequeño es la norma |
| **GDS / Martin Jordan** (F-490) | El mejor manual de escalamiento de capacidad, y la advertencia de que escalar capacidad no es demostrar impacto |
| **Mercado Libre** (F-499) | La forma híbrida hub + spokes a escala regional, con el sistema de diseño como infraestructura del hub |
| **InVision** (F-496) | Que crecer el equipo no es la palanca de impacto |
| **CIX BCP** (F-493) | El precedente local de que este set de roles ya convivió en una organización financiera peruana — y un corte de roles distinto al de este equipo |
| **El hallazgo negativo peruano** (§3.6) | Que el estándar local a superar es bajísimo, y que publicar un caso medido no tiene competencia |

---

## 7. Limitaciones

- **8 de 18 fuentes no se leyeron a texto completo** por bloqueo de egreso del entorno. Todas están
  marcadas en el ledger. Las más afectadas son las de mayor interés: NN/g, el Service Manual
  británico y las fuentes peruanas de `gestion.pe`.
- **El corpus peruano es todo 🟠D.** Blogs de negocio, perfiles institucionales y notas de prensa,
  sin método ni auditoría. Sirve para describir estructuras, **no** para afirmar que funcionan.
- **No existe evidencia comparativa causal entre modos organizativos.** No hay ningún estudio que
  compare equipos centralizados contra embebidos contra híbridos con resultado medido. Todo lo de §1
  es descripción de práctica, no evidencia de superioridad.
- **El benchmark de ratios es de 2020** y su emisor advierte contra usarlo como medida de madurez.
- **No encontré ninguna encuesta de la comunidad de diseño peruana** que permita dimensionar cuántos
  profesionales de cada rol hay en el país. Eso sigue sin dato.

---

## Conexiones

- [[metodologias-diseno-sistemas-complejos|Metodologías de diseño para sistemas complejos]] — este
  documento aporta el contraejemplo que le faltaba a su hallazgo central: **MineduLAB sí llega a la
  fase de evaluación**, y lo logra por gobernanza, no por método.
- [[tendencias-diseno-innovacion|Tendencias en diseño e innovación]] — el caso de GDS (F-490) es una
  confirmación nueva de **C7** en un dominio no barrido antes: el programa de diseño de servicios
  más grande de Occidente mide actividad y no resultado.
- [[behavioral-design-estado-disciplina|Behavioral design: estado de la disciplina]] — F-486, F-487
  y F-488 aportan por primera vez al node el ángulo **organizativo** del campo (tamaño de equipo,
  embebido vs. consultoría), que hasta ahora solo tenía el ángulo de evidencia y mercado.
