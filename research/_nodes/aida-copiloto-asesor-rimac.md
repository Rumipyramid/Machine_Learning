# AIDA — el copiloto de IA de la fuerza de ventas de RIMAC

> Documento de investigación. Fuente persistente y versionada en el repositorio.
> Fecha de elaboración: 2026-08-12 · Versión: v1.0
> **Fuente de verdad** de lo que se sabe sobre AIDA. Hasta ahora el tema vivía disperso dentro de
> `proyecto-back-to-basics-ffvv-vida.md`; con tres cuerpos de evidencia propios ya justifica node.
> Insumos: encuesta a asesores (n=19), análisis auditado de logs (2.697 consultas) y el plan de
> exploratorio cualitativo. Fuentes registradas como F-537 a F-539.

---

## 0. Qué es AIDA y en qué estado está el conocimiento

AIDA es un prototipo de copiloto de IA construido sobre Claude, **de uso en vivo durante la
conversación real con el cliente** — no un simulador de práctica. Tiene dos superficies: *AIDA
Sales* (fuerza de ventas) y *AIDA Service*. Todo lo de este node es sobre **AIDA Sales**.

**El estado del conocimiento cambió de forma importante.** Hasta julio de 2026 lo único que había
era una encuesta declarativa de 19 asesores. Ahora hay **datos de conducta auditados sobre 2.697
consultas reales de 274 asesores**, y los dos cuerpos coinciden. Eso mueve varias afirmaciones de
"señal preliminar" a "hallazgo con respaldo".

**La conclusión de una línea, y las tres fuentes la sostienen:**

> **AIDA sabe lo que dice el folleto. No sabe cómo opera el negocio, y no enseña a vender.**

---

## 1. Las tres fuentes, y cuánto pesa cada una

| Fuente | Qué es | n | Naturaleza | Peso |
|---|---|---|---|---|
| **Encuesta a asesores** (F-537) | Declarativo, autorreporte | 19 de ~200+ | Lo que los asesores *dicen* | 🟠 Débil por muestra, valiosa por lo que dejó salir solo |
| **Análisis de logs AIDA Sales** (F-538) | Conductual, auditado | 2.697 consultas · 274 asesores · 2 días | Lo que los asesores *hacen* | 🔵 El cuerpo más fuerte que existe hoy |
| **Exploratorio cualitativo** (F-539) | Plan de investigación | 3 entrevistas + redes + logs | **Aún no ejecutado** | ⏳ Pendiente |

⭐ **La combinación importa más que cada una por separado.** La encuesta tiene un punto ciego
declarado: los logs solo registran lo que los asesores *siguen* preguntando; si dejaron de pedir
algo porque no funcionaba, no aparece. La encuesta cubre ese hueco. Y a la inversa: la encuesta es
n=19 y no puede cuantificar nada; los logs sí.

---

## 2. Lo que dice la encuesta (n=19)

| Hallazgo | Cifra |
|---|---|
| Dicen que AIDA es fácil o muy fácil de usar | **19 de 19 (100%)** — 12 dicen "muy fácil" |
| **No** se declaran satisfechos con AIDA | **11 de 19 (58%)** — 4 muy insatisfechos |
| Mencionaron ChatGPT, Gemini o Copilot **por iniciativa propia** | **10 de 19 (53%)** |
| Dicen que las herramientas ayudan poco a manejar objeciones y persuadir | **13 de 19 (68%)** |
| Piden manejo de objeciones como capacitación prioritaria | **8 de 19 (42%)** — el tema más votado |
| Señalan el cierre como el momento con menos apoyo | **8 de 19 (42%)** |

**Comparación de insatisfacción entre herramientas** (misma encuesta): AIDA 58% · Cotizador 26% ·
Salesforce 11% · Outlook 11%. AIDA es, por lejos, la peor evaluada del set.

Textuales de los insatisfechos: *"AIDA no apoya mucho con el producto Vida Ahorro Garantizado, no
da la información adecuada y se equivoca con otro producto"* · *"Da respuestas equivocadas"* ·
*"Porque contesta mal siempre"* · *"No tiene todo lo necesario para nuestra gestión"*.

⭐ **La disociación es el hallazgo, no las cifras sueltas: 100% dice que es fácil de usar y 58% no
está satisfecho.** La adopción no es el problema. La calidad de la respuesta sí.

⭐ **Y el dato del 53% pesa más de lo que parece, por el costo que revela.** Los asesores tienen la
IA externa **bloqueada en la computadora**: para usar ChatGPT tienen que sacar el teléfono en medio
de la jornada. Pagar ese costo teniendo una herramienta oficial a un clic significa que **la
calidad del otro lado compensa la fricción**. Nadie preguntó por IA externa en la encuesta: salió
solo, en una pregunta abierta.

---

## 3. Lo que dicen los logs — los cuatro hallazgos

**Base:** 2.697 consultas reales de AIDA Sales del **lunes 17 y martes 18 de agosto de 2026**, de
274 asesores, tras excluir 651 registros de una cuenta de pruebas y 258 de AIDA Service.
≈ **1.348 consultas por día.**

### H1 · En la práctica, AIDA es una herramienta de estudio de producto

| | |
|---|---|
| Consultas de producto | **2.269 de 2.697 (84%)** |
| Asesores que hicieron al menos una | **267 de 274 (97%)** |
| Consultas por asesor | 8,5 |

**El patrón de uso son sesiones de estudio, no consultas sueltas.** 80 sesiones de 10+ turnos, de
62 asesores, que concentran **1.327 consultas — el 49% de todo el tráfico**, con **duración mediana
de 35 minutos**. Dentro de esas sesiones la falla es 5,8%, *mejor* que el promedio general.

⭐ **Casi la mitad del uso de AIDA son personas dedicándole media hora seguida a prepararse sobre un
producto. Y ahí funciona.**

**Y dentro de la misma sesión, la calidad se degrada al acercarse a la venta:** rentabilidad falla
2,6% · coberturas 3,1% · definiciones del oficio 8,8% · **contratación y emisión 12,2%**. Es la
misma persona, en la misma sesión.

**Adopción:** 86% de los asesores vuelve después de la primera consulta; 82 asesores hicieron entre
10 y 29 consultas y generan casi la mitad del volumen. No depende de un grupo pequeño de
entusiastas. ⚠️ **No se conoce el denominador**: 274 usaron AIDA, de cuántos en total no se sabe.

### H2 · En Vida falla en precio y en cómo se emite

Base: 1.522 consultas de producto en Vida · 235 asesores · **6,0% de falla general**.

De ocho temas, solo tres se distinguen del promedio (intervalos de Wilson 95%):

| Tema | Consultas | Fallas | Rango 95% | |
|---|---|---|---|---|
| Rentabilidad, retiros e inversión | 290 | 9 | 1,6 – 5,8% | ✅ **mejor** |
| **Precio, prima y montos** | **121** | **15** | **7,7 – 19,4%** | ❌ **peor** |
| **Contratación y emisión** | **44** | **6** | **6,4 – 26,7%** | ❌ **peor** |

Los otros cinco (beneficiarios, edades/plazos, coberturas, condiciones, definiciones) son
indistinguibles entre sí y del promedio.

**Preguntas de precio que no pudo responder** — ninguna es exótica:

> *"¿Cuál es la prima mínima de Vida Contigo?"*
> *"¿Cuál es el monto mínimo para incrementar la suma asegurada en Vida Ahorro Garantizado?"*
> *"¿De cuánto es la cobertura mínima de suma asegurada en el Vida Ahorro Garantizado soles?"*
> *"¿La condromalasia genera sobreprima en un seguro de vida Temporal Total?"*
> *"¿Cuál es el procedimiento para solicitar un cambio de suma asegurada?"*

**El mecanismo, y es la parte importante:**

- **Rentabilidad casi no falla porque no sale de documentos** — sale de una herramienta conectada
  que consulta valores reales de portafolio. **Cuando AIDA tiene un dato vivo, acierta.**
- **El precio falla porque no es un dato de ficha**: depende de scoring del cliente, autonomías
  comerciales, tarifas por edad y suma asegurada, sobreprimas por condición médica.
- **La contratación falla por lo mismo**: requisitos de suscripción, cuándo va a evaluación manual,
  qué exámenes pide, quién los paga.

**La confirmación documental es la pieza más fuerte del análisis.** Sobre 95 documentos distintos y
6.165 citas en respuestas de Vida:

| Tipo de documento | % de las citas |
|---|---|
| Fichas de producto y brochures | **77%** |
| Condiciones generales (contrato) | 9,6% |
| **Reglas de operación / procedimientos** | **3,4%** |

⭐ **Los dos temas que fallan son exactamente los que no tienen documentos.** No es un problema de
inteligencia artificial.

### H3 · Hay dos grupos de productos, y la diferencia es la documentación

| Producto | Consultas | Fallas | Tasa | Rango 95% | Documentos citados |
|---|---|---|---|---|---|
| Vida Flexible | 561 | 17 | **3,0%** | 1,9 – 4,8% | 7 |
| Vida Temporal Total | 27 | 1 | 3,7% | 0,7 – 18,3% | 1 |
| Inversión Global / Ultracash | 287 | 11 | **3,8%** | 2,2 – 6,7% | 10 |
| Vida Contigo / con Devolución | 191 | 16 | **8,4%** | 5,2 – 13,2% | 4 |
| Vida Ahorro Garantizado | 233 | 21 | **9,0%** | 6,0 – 13,4% | 2 |
| Desgravamen / hipotecario | 82 | 9 | **11,0%** | 5,9 – 19,6% | — |
| Renta Garantizada | 129 | 16 | **12,4%** | 7,8 – 19,2% | **1** |

De 21 pares posibles, **5 no se solapan**, y los cinco van en la misma dirección: Vida Flexible es
mejor que Vida Contigo, VAG, Desgravamen y Renta Garantizada; e Inversión Global es mejor que Renta
Garantizada.

⭐ **El tipo de documento importa tanto como la cantidad.** Vida Flexible tiene siete que incluyen
ficha, brochure, condiciones generales e información complementaria. **Renta Garantizada tiene un
brochure — material de venta, no de consulta técnica — y es el que más falla.** VAG tiene dos, ambos
comerciales: ni condiciones generales ni procedimientos, y por eso no responde exclusiones ni
penalidades por retiro.

### H4 · El uso comercial es ancho pero poco profundo

| | Consultas | Asesores | Consultas por asesor |
|---|---|---|---|
| Producto | 2.269 | 267 (97%) | **8,5** |
| **Comercial** | 428 (15,9%) | 116 (**42%**) | **3,7** |

**La recurrencia revela el problema:**

| Tipo de pedido | Asesores | Preguntaron 1 sola vez | Media |
|---|---|---|---|
| Producto | 267 | **18%** | 8,5 |
| *"Escríbeme una pieza"* (speech, correo) | 85 | 32% | 4,0 |
| **"Enséñame a vender"** (objeciones, cómo) | **50** | **66%** | **1,8** |

⭐ **Cincuenta asesores le pidieron a AIDA que les enseñara a vender. Treinta y tres no volvieron a
intentarlo.**

**Los dos pedidos no fallan igual:** redactar una pieza falla 4,7% —*mejor* que producto (6,7%)—
mientras que enseñar a vender falla **8,9%** y el filtro de seguridad lo bloquea **4,4%**, siete
veces más que en producto.

**Y hay un clasificador interno que manda mal casi la mitad de esos pedidos:**

| | Consultas | Fallas |
|---|---|---|
| Clasificador acertó (camino de coaching) | 51 | **2 — 3,9%** |
| Clasificador falló (camino de producto) | 39 | **6 — 15,4%** |

**El 43% de los pedidos de venta se procesan por el camino equivocado**, y ahí la falla se
multiplica por cuatro. El asesor no ve la bifurcación ni la puede forzar. ⚠️ La interpretación del
campo `coach_mode` **hay que confirmarla con el equipo técnico**.

**El formato tampoco calza con el momento de uso:** respuesta comercial **483 palabras** vs. 188 de
producto. Es material para estudiar, no munición para una llamada en vivo — que es justo donde la
encuesta dice que necesitan apoyo. Ver §6: la literatura predice este modo de falla y trae el
remedio probado.

---

## 4. El exploratorio cualitativo (pendiente de ejecución)

Diseño de tres métodos que se triangulan entre sí: **entrevistas de incidente crítico** a 3 perfiles
(el que declaró "nunca", un usuario intensivo, y alguien que resuelve por fuera), **análisis de
contenido en redes** de asesores propios y de la competencia buscando rastro de IA, y el **análisis
de logs** (ya ejecutado, §3).

**Su objetivo específico #3 es el que más importa para el roadmap:** *identificar la necesidad raíz
detrás de las consultas, para evaluar si un agente conversacional es realmente la forma correcta de
resolverla, o si la necesidad tiene otra forma.* Es la única pieza del expediente que se permite
cuestionar el formato mismo.

Dos decisiones de diseño que vale conservar: el **Bloque 1 indaga la necesidad-raíz antes de nombrar
ninguna herramienta**, y el **ejercicio en vivo** pide al asesor resolver un caso con ChatGPT o
Gemini en su propio celular mientras se observa qué escribe y si el resultado lo convence. Eso
último es lo más cerca que se puede estar de medir la comparación real contra la alternativa.

---

## 5. Convergencias y tensiones entre las tres fuentes

### Convergen, y con fuerza

| Afirmación | Encuesta | Logs |
|---|---|---|
| **La adopción no es el problema** | 100% dice fácil de usar | 86% vuelve tras la primera consulta; 97% usa producto |
| **La calidad sí lo es** | 58% no satisfecho | 6,0% de falla general en Vida, con picos de 12-19% |
| **Falla donde se vende** | 68% dice que ayudan poco con objeciones; 42% pide objeciones; 42% señala el cierre | 66% de abandono en "enséñame a vender"; falla 8,9% y bloqueo 4,4% |
| **VAG es un caso conocido** | Citado por nombre en un textual | 9,0% de falla, 2 documentos, ambos comerciales |
| **Ya hay sustituto** | 53% menciona ChatGPT/Gemini solo | *(los logs no pueden verlo — punto ciego declarado)* |

### La convergencia que no es obvia, y es la más útil

⭐ **La encuesta confirma H1 por omisión.** Ningún asesor menciona la información de producto como
necesidad insatisfecha. Es el uso más grande de la herramienta —84% del tráfico— **y nadie se queja
de él, porque funciona.** Un silencio que confirma es más difícil de conseguir que una cifra.

### Tensiones y cosas que el expediente no resuelve

**1 · Vida Temporal Total contradice la tesis de H3 y se declara como excepción.** Un solo documento
y 3,7% de falla, cuando la tesis diría que debería fallar mucho. El documento lo atribuye a la
muestra (27 consultas, rango 0,7 – 18,3%), y es razonable. **Pero hay una segunda explicación que no
se menciona y es testeable:** Temporal Total es el producto más simple del portafolio —temporal
puro, sin ahorro, sin devolución, sin rescate— así que probablemente **no recibe las preguntas
difíciles**, no que las responda bien. Se comprueba comparando la distribución de temas por
producto: si a Temporal Total casi no le preguntan de precio ni de contratación, la excepción se
disuelve.

**2 · La ventana es de dos días y son lunes y martes.** Alcanza para demostrar que los problemas
existen; no alcanza para saber su frecuencia, y **no cubre cierre de mes, campaña ni fin de
semana** — momentos donde la mezcla de consultas es plausiblemente distinta (más presión de cierre,
más pedido comercial).

**3 · El propio análisis declara que sus intervalos son optimistas.** Wilson asume observaciones
independientes y los turnos de una conversación no lo son: las 91 fallas de Vida están en 60
asesores y 64 sesiones, y los cinco asesores con más fallas concentran el 23%. **Los rangos reales
son más anchos**, y el par más ajustado —Inversión Global vs Renta Garantizada— podría no
sobrevivir a una corrección por agrupamiento. Está bien declarado; hay que repetirlo al presentar.

**4 · El detector de falla es conservador y solo ve fallas totales.** No detecta **fallas
parciales** — respuestas que contestan algo pero no lo que se preguntó. **Las tasas reportadas son
un piso.** ⚠️ Esto conecta con un hallazgo del proyecto en otro frente: en la evaluación del agente
de salud de la web, el defecto dominante **no fue la alucinación sino la omisión** — responder
correctamente sin dar el dato que se tenía. Si AIDA tiene el mismo patrón, el problema medido está
sistemáticamente subestimado.

---

## 6. ⭐ Cruce con la literatura de copilotos de ventas

Este cruce no está en los tres documentos y cambia la lectura del Hallazgo 4.

**Luo, Qin, Fang y Qu (2021)** — *Journal of Marketing*, experimentos de campo aleatorizados con
agentes de ventas reales (F-540). El beneficio de un coach de IA **no se reparte parejo**: sigue una
**U invertida**. Los agentes de rendimiento **medio** son los que más ganan. Los de **abajo** ganan
poco, y el mecanismo medido es **sobrecarga de información**. Los de **arriba** ganan poco por
**aversión a la IA**.

⭐ **Y el remedio está probado experimentalmente: en un segundo experimento restringieron el nivel de
feedback del coach y el desempeño de los agentes de abajo mejoró significativamente.**

**Por qué esto importa acá.** El H4 observa que las respuestas comerciales de AIDA son **483
palabras contra 188 de producto**, y lo interpreta como un problema de formato para el momento de
uso. La literatura dice algo más preciso y más accionable: **483 palabras de coaching es
literalmente el mecanismo de sobrecarga de información que produce el abandono medido.** Los dos
hallazgos, obtenidos de forma independiente, describen lo mismo.

**La implicación operativa invierte el instinto:** ante el 66% de abandono, la reacción natural es
mejorar y enriquecer la respuesta de coaching. **El experimento dice lo contrario — hay que darle
menos, no más.**

**Brynjolfsson, Li y Raymond (2025)** — *Quarterly Journal of Economics*, 5.172 agentes de soporte
(F-541): +15% de productividad promedio, con las ganancias concentradas en los **menos
experimentados**, mientras los más experimentados tienen ganancias pequeñas en velocidad y
**pequeñas caídas en calidad**.

⚠️ **Los dos estudios divergen sobre dónde caen las ganancias** —abajo en soporte, en el medio en
ventas— y **no hay que promediarlos**: la tarea es distinta (soporte tiene respuesta correcta
recuperable; la venta es relacional y requiere criterio). Pero coinciden en algo que sí conviene
llevarse: **los top performers no ganan, y pueden perder calidad.**

**La pregunta que falta responder con la data que ya existe:** nadie ha segmentado el uso de AIDA
por desempeño comercial del asesor. Es cruzable —274 asesores identificados— y decidiría a quién
apuntar el roadmap. Hoy el promedio está tapando tres comportamientos distintos.

---

## 7. ⭐ Cruce con la matriz de productos Vida — la misma laguna, por dos caminos

Esta es la triangulación más concreta del expediente, y es verificable celda por celda.

El **anexo de fichas de producto** construido desde `Matriz_productos_VIDA_FINAL.xlsx` excluyó
41 de 70 parámetros por falta de dato. Entre los que le faltan **específicamente a Vida Ahorro
Garantizado** está **«Suma asegurada mínima»**.

Y entre las preguntas que el H2 documenta como **no respondidas por AIDA** está, textual:

> *"¿De cuánto es la cobertura mínima de suma asegurada en el Vida Ahorro Garantizado soles?"*

⭐ **Es el mismo dato.** Un análisis de logs de conversaciones reales y una auditoría de la matriz de
producto, hechos con métodos completamente independientes, **señalan el mismo hueco en el mismo
producto**. Eso convierte una recomendación genérica ("falta documentación") en una tarea concreta:
llenar esa celda.

El patrón se repite más allá de ese caso. El H3 dice que VAG *"no responde las exclusiones ni las
penalidades por retiro"*; el anexo excluyó, para VAG, las carencias de enfermedades graves, dispensa
de primas y renta hospitalaria, además de tipos de riesgo. **Los dos análisis describen el mismo
producto con los mismos vacíos.**

**Implicación:** la lista de 41 parámetros incompletos del anexo **es, en parte, la agenda de
carga documental que H2 y H3 piden** — no dos pendientes distintos.

---

## 8. ⭐ Cruce con el brief de arquitectura del agente de clientes

AIDA (interno, para asesores) y el asistente de la app (externo, para clientes) son productos
distintos con **el mismo modo de falla**, y por lo tanto buena parte del brief de arquitectura
aplica tal cual.

| Hallazgo en AIDA | Recomendación equivalente del brief |
|---|---|
| 77% de las citas son folletos, 3,4% reglas de operación | **A2 · Condicionados y procedimientos como fuente consultable** |
| Falla en prima mínima, suma asegurada mínima, sobreprimas | **A3 · Tabla de datos autorizados** |
| El clasificador manda 43% de los pedidos por el camino equivocado | **C1 · Separar las reglas, y hacer visible el criterio** |
| El filtro de seguridad bloquea 7× más en pedidos comerciales | **C2 · Un motivo distinto por cada negativa** — hoy no se puede medir el sobre-bloqueo |
| Rentabilidad casi no falla porque sale de herramienta conectada | **B1 · El dato vivo por herramienta, no por documento** |
| El detector solo ve fallas totales, no parciales | **I2 · Medir también lo que el agente calla** |

⭐ **El caso de rentabilidad es la prueba más limpia de toda la tesis del brief.** Es el único tema
de Vida donde AIDA está claramente mejor que el promedio, y la razón es que **no consulta un
documento: consulta una herramienta con valores reales**. Es exactamente el argumento de que el
problema no está en el modelo sino en la capa de conocimiento — y acá está medido, adentro, con
datos propios.

---

## 9. Preguntas abiertas

1. **¿Cuál es el denominador de adopción?** 274 asesores usaron AIDA en dos días; de cuántos en
   total, no se sabe. Sin eso no se puede afirmar nada sobre penetración.
2. **¿Renta Garantizada tiene documentos cargados que AIDA nunca recupera?** Si los tiene, el
   problema no es de contenido sino de recuperación, **y la solución es completamente distinta**.
   Es lo primero que hay que verificar al abrir la base.
3. **¿Qué es exactamente `coach_mode`?** Cómo decide, y si el asesor puede forzarlo. Sin eso, el
   hallazgo del clasificador es una inferencia razonable pero no confirmada.
4. **¿Cómo se distribuye el uso por desempeño comercial del asesor?** (§6). Es la pregunta con mejor
   relación valor/esfuerzo del expediente: la data ya existe.
5. **¿A Temporal Total le preguntan cosas difíciles?** (§5, tensión 1). Resuelve si su baja falla es
   robustez o simplicidad.
6. **¿Cuántas fallas parciales hay?** Requiere revisión manual de una muestra. Define cuánto se está
   subestimando el problema.

---

## 10. Limitaciones del expediente completo

- **Dos días de datos** (lunes 17 y martes 18 de agosto de 2026), sin cierre de mes ni campaña.
- **Encuesta de 19 sobre 200+**, y autoseleccionada.
- **El exploratorio cualitativo no se ha ejecutado** — es un plan.
- **Intervalos optimistas** por agrupamiento, declarado por el propio análisis.
- **El detector de falla es un piso**, no una medida.
- **No hay contrafactual.** No se sabe qué tan bien resolvería un asesor sin AIDA la misma consulta,
  ni qué tan bien la resuelve ChatGPT — que es la comparación que los asesores ya están haciendo
  todos los días con su celular. El ejercicio en vivo del exploratorio es lo único diseñado para
  cerrar ese hueco.

---

## Conexiones

- [[proyecto-back-to-basics-ffvv-vida|Proyecto Back to Basics — FFVV Vida Individual]] — AIDA vivía
  descrito ahí; este node pasa a ser la fuente de verdad del tema y aquel conserva el encuadre
  estratégico (por qué se propuso un copiloto, el Plan Piloto de 10 asesores, la corrección sobre
  práctica vs. producción).
- [[matriz-productos-vida-rimac|Matriz de productos Vida RIMAC]] — §7: los vacíos de la matriz y las
  fallas de AIDA señalan las mismas celdas en los mismos productos.
- [[capacidades-asistente-ia-aseguradora|Capacidades de un asistente de IA in-app]] — §8: mismo modo
  de falla en el agente de clientes; el brief de arquitectura aplica en buena parte a AIDA.
- [[evaluacion-calidad-agentes-conversacionales-ia|Evaluación de calidad de agentes conversacionales]]
  — el marco para medir a AIDA de forma continua, y la fuente de la distinción entre falla total y
  falla parcial que §5 identifica como el sesgo del detector actual.
- [[futuro-asesores-seguros-venta-digital|¿Desaparecerán los asesores de seguros?]] — AIDA es la
  apuesta concreta por "potenciar al asesor" en vez de reemplazarlo; §6 trae la evidencia de campo
  sobre si eso funciona y con quiénes.
