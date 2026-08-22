# Análisis de los logs de AIDA — primera corrida

**Hallazgos sobre datos reales.** v1.3 · 2026-08-22

> **v1.3 — ⭐⭐⭐ §2.9: la primera medición contra el objetivo declarado**, no contra la calidad.
> **AIDA es más larga justo donde el asesor tiene menos tiempo**: 485 palabras de mediana en
> objeciones y 502 en speeches, contra 205 del corpus. Y **solo una de cada cuatro consultas se
> resuelve en un turno**.

> **v1.2 — ⭐⭐ §2.8: ya existe una batería de prueba corriendo contra AIDA**, con autor y con dos
> series distintas; una de ellas prueba exactamente dos de las tres funcionalidades del protocolo.
> Y **prueba de robustez de §2.1**: el hallazgo de inestabilidad **aguanta** que se le quite esa
> batería — 61,8% general y **69,6% en Vida**, que es la cifra que conviene llevar a la reunión.

> **v1.1 — ⭐⭐⭐ §2.7: verificación manual de contradicción.** Se confirmó, caso por caso, que AIDA
> entrega cifras incompatibles sobre el mismo producto, con un ejemplo que no requiere conocimiento
> de seguros para juzgarse. También se documentan **tres candidatos que se descartaron** porque AIDA
> era correcta.

Fuente: `aida_logs_19_08.csv`, entregado por el equipo de la capacidad.

---

## ⚠️ Advertencia de procedencia — leer antes que nada

> ✅ **Aclarado (2026-08-20).** El archivo se recibió primero descrito como *"el histórico de los
> últimos 3 meses"*; la definición posterior del diagnóstico lo describe como **"un período de 3 días
> de uso"**, que **sí coincide con el contenido**. La advertencia de abajo se conserva porque acota
> qué se puede afirmar, pero **ya no hay que leerla como una discrepancia sin resolver.**

**El archivo cubre un período corto, no un histórico largo.**

| | Declarado | Real en el archivo |
|---|---|---|
| **Periodo** | 3 meses | ⚠️ **2 días** — del 17-ago 16:49 al 19-ago 04:10 UTC |
| **Volumen** | ~90.000 consultas esperables *(a 30.000/mes)* | **3.606 registros** |

**Esto no invalida el análisis, pero acota fuerte lo que se puede afirmar:**

- ✅ **Sí se puede** describir cómo se comporta la herramienta y qué hay en su base.
- ⛔ **No se puede** hablar de tendencias, estacionalidad, ni de **qué preguntas se dejaron de
  hacer** — que era uno de los análisis más prometedores y **necesita la serie completa**.

🔴 **Acción: pedir igual el histórico completo.** Con 3 días alcanza para todo lo de este informe,
pero **la serie larga es la única vía para ver qué preguntas se dejaron de hacer** — y ese análisis
sigue siendo el de mayor probabilidad de dar un hallazgo que nadie más tiene.

⭐ **Nota (2026-08-20):** parte de ese hallazgo **se recuperó por otra vía** — cruzando lo que los
asesores declaran necesitar contra lo que efectivamente preguntan. Ver §3.4 de
`[[aida-diagnostico-cuatro-frentes]]`.

---

## 1. Qué contiene, una vez limpio

⚠️ **Primera limpieza necesaria:** hay una cuenta llamada `aida_service` con **651 consultas en 2
días**, todas la misma pregunta y todas en el ramo `otro`. **Es una cuenta de servicio o un chequeo
automático, no un asesor.** Contamina el 18% del volumen y **hay que excluirla de cualquier cifra**.

**Después de excluirla:**

| Métrica | Valor |
|---|---|
| Consultas (agente `ffvv`) | **2.697** |
| **Asesores distintos** | **274** en dos días |
| Sesiones | 501 |
| Consultas por asesor | mediana **6** · media 12 · máx. 113 |
| **Sesiones de un solo turno** | ⭐ **67,5%** |
| Reparto por ramo | **Vida 42%** · direct 21% · direct_coach 20% · Salud 7% · Vehicular 5% |

⭐ **Dato de contexto útil:** 274 asesores usándola en dos días es adopción real y amplia. El problema
del que habla este diagnóstico **no es que no la usen.**

⭐ **Y el 67,5% de sesiones de un solo turno merece atención:** pregunta y se va. Puede ser eficiencia
(resolvió a la primera) o abandono (no valió la pena insistir). **Los logs solos no distinguen** — se
resuelve cruzando con el rating y con el campo.

---

## 2. Los hallazgos que aguantan

### 2.1 ⭐⭐⭐ La misma pregunta no recupera siempre las mismas fuentes

**Es el hallazgo principal, y es una comparación directa sin interpretación de por medio.**

De las **66 preguntas formuladas 3 o más veces** en estos dos días:

| Hallazgo | Cifra |
|---|---|
| **No recuperaron siempre el mismo conjunto de fuentes** | ⭐ **68,2%** (45 de 66) |
| **Solo en Vida** | ⭐⭐ **75,9%** (22 de 29) |
| ⭐⭐ **A veces recuperaron fuentes y a veces NINGUNA** | **47%** (31 de 66) |
| Conjuntos distintos por pregunta | mediana 2 · **máximo 13** |

**Casos concretos:**

- *"6- speech para endosar crédito hipotecario"* — **14 veces preguntada, 13 conjuntos de fuentes
  distintos.** Prácticamente nunca leyó lo mismo dos veces.
- *"¿hay penalidades por cancelación anticipada?"* — **9 veces preguntada, 6 de ellas sin recuperar
  ninguna fuente.**
- *"2- brochure de vidacontigo"* — 12 veces: unas devuelve 2 documentos, otras 1, **dos veces
  ninguno.**

⭐ **Por qué esto importa más que cualquier medición de exactitud:** *la consistencia es la mejora #1
que piden los asesores*, y acá está su causa mecánica. **No es que AIDA "a veces se equivoque": es
que a la misma pregunta le entra material distinto cada vez.** Con material distinto, la respuesta
varía sin que nadie haya cambiado nada.

**Y es exactamente la firma de casi-duplicados en la base** que el diagnóstico venía planteando como
hipótesis principal. **Deja de ser hipótesis.**

> ### ✅ Prueba de robustez — el hallazgo aguanta que le quiten el caso más llamativo *(2026-08-22)*
>
> ⚠️ **Los dos ejemplos más vistosos —el speech de endoso repetido 14 veces y el brochure de Vida
> Contigo— no salen del uso orgánico: salen de una batería de prueba que corre una sola persona**
> (ver §2.8). Eso obliga a preguntar si el 68,2% es un artefacto de esa batería.
>
> **No lo es.** Recalculando con la misma medición, excluyendo por completo las consultas con
> prefijo numerado:
>
> | Corte | Preguntas 3+ veces | Inestables | Solo Vida |
> |---|---|---|---|
> | **Todo (como se reportó)** | 66 | **68,2%** | **75,9%** |
> | ⭐ **Sin la batería numerada** | 55 | **61,8%** | ⭐ **69,6%** |
> | Sin el usuario de la serie con guion | 56 | 62,5% | 69,6% |
>
> ⭐⭐ **Siete de cada diez preguntas de Vida repetidas por asesores reales no recuperan siempre las
> mismas fuentes.** El hallazgo baja unos puntos y no cambia de naturaleza.
>
> ⚠️ **Para la reunión conviene llevar la cifra sin la batería (61,8% · 69,6% en Vida)**, no la
> completa. Es más baja y **no tiene ningún flanco**: si alguien descubre después que dos de los
> ejemplos venían de una prueba interna, la cifra conservadora ya estaba puesta sobre la mesa.

### 2.2 ⭐⭐⭐ La base tiene varios documentos compitiendo por el mismo producto

Se citaron **199 documentos distintos** en 4.127 citas. Los documentos de producto llevan un código
numérico, y **agrupándolos por código aparece el problema con nombre y archivo**:

| Código | Documentos | Citas | Estado |
|---|---|---|---|
| **999993** | ⚠️ **4** — `VIDA_PLAN VIDA FLEXIBLE_080125.docx` · `Brochure Vida Flexible.pdf` · `Vida_Flexible_info.docx` · ⚠️⚠️ **`Condiciones Generales Vida Futuro Protegido Nuevo.pdf`** | 822 | 🔴 **El cuarto documento es de OTRO producto** — VFP archivado bajo el código de Vida Flexible |
| **999994** | ⚠️ **5** — tres de Inversión Global + condiciones generales + ⚠️ `Formatos.docx` | 440 | 🔴 Un documento genérico mezclado con los de producto |
| **999992** | ⚠️ **3** — `VIDA_Plan VIDA Contigo_080125.docx` · `Brochure Seguro de Vida Ahorro con Devolucion Feb2025.pdf` · `Vida_Contigo_info.docx` | 348 | ⭐ **Confirma que Vida Contigo y Ahorro con Devolución son el mismo producto** |
| **999998** | **2** — `Vida Ahorro Garantizado - Presentación de Producto.pdf` · `Seguro de Vida Ahorro Garantizado.pdf` | 442 | 🟡 Casi-duplicado clásico |

⭐⭐ **El código 999992 resuelve una discrepancia abierta del proyecto.** El Playbook lista **Vida
Contigo** y **VAG** como dos productos distintos con descripciones distintas. **La base los tiene bajo
el mismo código de producto.** Confirma que la matriz del repo tiene razón y **el Playbook está mal**
— el desfase está aguas arriba, en la fuente canónica, no en AIDA.

⚠️⚠️ **El código 999993 es un error de catálogo verificable**, con nombre de archivo: las
**Condiciones Generales de Vida Futuro Protegido** están archivadas bajo el código de **Plan Vida
Flexible**. Cuando un asesor pregunta por Vida Flexible, **puede recibir condiciones de otro
producto.** Es el tipo de error con riesgo de cumplimiento, no de calidad.

### 2.3 ⭐⭐ Contaminación cruzada entre ramos

El agente de la fuerza de venta está citando documentos que no son de su dominio:

| Documento | Citas |
|---|---|
| `Certificación en Salud_ Junio 2025.pdf` | 72 |
| `AGENDA_RIMAC.pdf` | 45 |
| `VEG001 CONDICIONES GENERALES DEL SEGURO VEHICULAR.docx` | 40 |
| `222324 SALUD RED MEDICA PLAN A_SET 2025_PLAN_BENEFICIOS.pdf` | 34 |
| `SALUD_Seguro de Asistencia Medica (AMI)_24062025.docx` | 31 |
| *(y ~10 documentos más de Salud, Vehicular y SOAT)* | |

⭐ **Es exactamente lo que la literatura marca como el error de arquitectura más caro:** fuentes
superpuestas entre dominios suben la alucinación y compiten con el documento correcto. **Y explica
por qué el ruteo falla.**

### 2.4 ⭐⭐ El ruteo es inestable, con datos

De las preguntas repetidas, **40,8% fueron clasificadas a más de un ramo distinto.**

El caso más claro: **"¿qué es un endoso?"** — preguntada **38 veces**, ruteada a **Vida, `direct` y
`general`**. La misma pregunta, tres caminos distintos, tres bases distintas.

⭐ **Confirma la capa D del diagnóstico**, que hasta ahora era una inferencia a partir del autorreporte
de la herramienta.

### 2.5 ⭐ El formato de la base es el que la evidencia dice que no funciona

De las 4.127 citas:

| Formato | Citas | % |
|---|---|---|
| `.docx` | 2.010 | 48,7% |
| **`.pdf`** | **1.978** | **47,9%** |
| **`.xlsx`** | **139** | **3,4%** |

⭐ **Más de la mitad de lo que AIDA lee está en formatos que degradan la recuperación** — y los
brochures en PDF están entre los más citados. Es la confirmación empírica, sobre el caso real, de lo
que el node de arquitectura sostenía con evidencia externa.

### 2.6 ⭐⭐ El rating positivo del 96% no significa lo que parece

| Métrica | Valor |
|---|---|
| Consultas calificadas | 74,7% |
| **Ratio positivo entre las calificadas** | **96,0%** |
| Negativas | **80** (2,2% del total) |

**Pero al mirar qué distingue a las 80 negativas, aparece la señal:**

| | Negativas | Base general | Diferencia |
|---|---|---|---|
| **Sin ninguna fuente citada** | **50,0%** | 23,7% | ⭐ **2,1×** |
| **Respuesta del tipo "no tengo esa información"** | **13,8%** | 2,2% | ⭐⭐ **6,3×** |

⭐⭐ **El asesor castiga exactamente cuando AIDA no recupera.** No castiga el estilo ni la longitud:
castiga la ausencia de fundamento. **Es la confirmación más limpia de que el problema es de capa A —
conocimiento— y viene de la conducta de los propios asesores, no de nuestra interpretación.**

**Y sobre qué tratan las negativas:** cobertura y exclusiones (17,5%), montos y tasas (12,5%), edad y
requisitos (13,8%) — ⭐ **casi la mitad son detalle técnico de producto, que es justamente lo que el
Playbook declara como "Pendiente".** La predicción falsable del diagnóstico se cumple.

⚠️ **Y lo más preocupante no está en las negativas, sino en lo que no se calificó.** Un cuarto de las
consultas no recibe rating, y **las respuestas sin fuente no siempre se califican mal**. El
instrumento de feedback **no detecta el problema de forma fiable** — sirve como señal, no como
medición.

---

## 2.7 ⭐⭐⭐ VERIFICADO: sí da información contradictoria sobre el mismo producto

> **Añadido el 2026-08-20 tras verificación manual dirigida.** La §5 de este documento retiraba una
> medición automática de discrepancia por no sobrevivir al escrutinio, y dejaba dicho que **afirmar
> contradicción requería revisión humana de una muestra**. Se hizo. **El resultado es afirmativo, y
> hay un caso que no necesita conocimiento de producto para juzgarse.**

### El caso definitivo — una sola respuesta, dos cifras incompatibles

**Pregunta de un asesor:** *"cuál es la prima mínima del seguro vida flex"*
**Fuentes que AIDA citó:** `999993. VIDA_PLAN VIDA FLEXIBLE_080125.docx` · `999993. Vida_Flexible_info.docx`

> La prima mínima para el seguro **Vida Flexible (Flexivida)** es la siguiente:
> * **Prima mínima mensual:** **$35 o S/ 180**.
> * **Monto mínimo para invertir:** **$35 o S/ 135**.

⭐⭐⭐ **El mismo `$35`, en renglones consecutivos de la misma respuesta, convertido a S/ 180 y a
S/ 135.**

**Por qué este caso es incontestable:** no hace falta saber nada de seguros de vida para juzgarlo, ni
decidir cuál de los dos atributos es cuál. **Si la cifra en dólares es la misma, la cifra en soles no
puede ser distinta.** O el `$35` está mal en una de las dos líneas, o una de las conversiones está
mal. **Es aritméticamente imposible que ambas sean correctas — y AIDA no lo detecta.**

⚠️ **Y es el número que el asesor le dice al cliente.** No es un detalle técnico interno: es el precio.

### El patrón, en todo el corpus

El mismo tipo de incoherencia aparece de forma sistemática. Barrido de **pares dólar↔sol dentro de una
misma frase** —una clase de afirmación que se puede juzgar sin conocimiento de producto—:

| Monto en USD | Conversiones distintas encontradas | Frecuencia | Atributo |
|---|---|---|---|
| **US$ 35** | ⚠️ **S/ 180 · S/ 135 · S/ 130** | 32 · 13 · 12 | Prima mínima |
| **US$ 50.000** | ⚠️ **S/ 180.000 · S/ 175.000** | 27 · 5 | Suma asegurada mínima de Vida Flexible |
| **US$ 3.000** | 🟡 **S/ 10.500 · S/ 10.000** | 38 · 1 | Suma asegurada de sepelio |

⭐ **Y los tres documentos del código 999993 aparecen citados tanto en las respuestas que dicen
S/ 180 como en las que dicen S/ 135.** No es que un documento diga una cosa y otro diga otra de forma
limpia: **el mismo conjunto de fuentes produce las dos cifras.** Eso apunta a que la incoherencia está
dentro del material, no solo entre documentos.

### ⚠️ Tres candidatos que se verificaron y se DESCARTARON

**Esto importa tanto como lo confirmado**, porque es lo que impide llevar una acusación falsa a una
reunión:

| Candidato | Parecía | Qué era realmente | Veredicto |
|---|---|---|---|
| **Edad de ingreso de Vida Flexible: 64 vs 74 años** | Contradicción directa | **64 es para el cónyuge, 74 para los padres**, en la cobertura de sepelio | ✅ **AIDA estaba bien** |
| **Carencia: "cero" vs 90 días vs 1 año** | Contradicción grave | Coberturas y productos distintos: cero en Temporal Total, 90 días en enfermedades graves de Vida Contigo, 1 año en la principal de Flexivida | ✅ **Sin contradicción probada** |
| **US$ 5.000 = S/ 15.000 vs S/ 16.000** | Conversión incoherente | **Productos distintos**: UltraCash vs un plan de Salud | ✅ **Descartado** |

⭐ **En los tres casos AIDA era más precisa de lo que sugería el análisis automático.** Es la razón por
la que la medición del 81% se retiró y por la que ésta se hizo a mano.

### Cómo enunciarlo sin exponerse

**Lo que se puede afirmar con total seguridad:**

> **AIDA entrega cifras incompatibles sobre el mismo producto.** El caso verificado: en una misma
> respuesta sobre la prima mínima de Vida Flexible, el mismo importe de $35 aparece convertido a
> S/ 180 y a S/ 135. Es aritméticamente imposible que las dos sean correctas, y el sistema no lo
> detecta. El patrón se repite en el corpus con la suma asegurada mínima.

**Lo que NO se debe afirmar:**

- ⛔ Que la mayoría de las respuestas se contradigan. **No está medido y probablemente no es cierto.**
- ⛔ Cuál de las dos cifras es la correcta. **Eso lo dice Producto, no el diagnóstico.**
- ⛔ Que sea intencional o negligencia de alguien. **Es un efecto de tener varios documentos por
  producto**, que es un problema de gobierno, no de personas.

---

## 2.8 ⭐⭐ Alguien ya está corriendo una batería de prueba contra AIDA *(hallazgo 2026-08-22)*

**No lo sabíamos, y cambia el plan de trabajo.** El 6,2% del volumen (166 consultas) llega con
**prefijo numerado** — no es la forma en que un asesor escribe una duda. Son **dos series
distintas**, y ninguna es uso real:

| Serie | Consultas | Usuarios | Ítems | Qué prueba | Sin cita |
|---|---|---|---|---|---|
| ⭐ **`N-` (guion)** | 113 | **1** — `yeni.prado` | **10**: 5 brochures + 5 speeches | ⭐⭐ **Exactamente las funcionalidades G-A y G-C del protocolo** | 3,5% |
| **`N.` (punto)** | 53 | **4** | **18**, todos los ramos | Batería de QA transversal — vehicular, salud, vida y corporativo | 22,6% |

**Los diez ítems de la serie con guion, cada uno corrido entre 9 y 14 veces en dos días:**
brochure de Flexivida · brochure de Vida Contigo · brochure de Inversión Global · brochure de
UltraCash · brochure de [Ahorro] Garantizada · speech para endosar crédito hipotecario · y **tres
speeches de Flexivida segmentados por edad** (20-30, 30-40, 40-50).

⭐⭐⭐ **Por qué esto importa más que la curiosidad:** el Banco G del protocolo fue diseñado para
probar las tres funcionalidades declaradas. **Dos de las tres ya tienen una batería corriendo, con
autor y con historial.** Pedir esas dos listas ahorra trabajo, evita duplicar y —lo más útil—
**demuestra que la práctica de medir AIDA ya existe dentro de la casa**, que es un argumento mejor
que llegar proponiéndola.

⚠️ **Y da una lectura de la repetición que no es la obvia:** que un mismo ítem se corra 14 veces en
dos días no es un asesor insistiendo, **es alguien probando**. Los ejemplos de inestabilidad más
llamativos de §2.1 salen de ahí — por eso está la prueba de robustez.

✅ **Lo que NO contamina:** la batería registró **138 calificaciones positivas y ninguna negativa**,
pero su efecto sobre el ratio es despreciable — **96,0% con ella, 95,7% sin ella.** El 96% no se
explica por esto.

**Qué preguntar, y a quién:** las dos listas completas, quién las diseñó y con qué criterio, si hay
resultados registrados en algún lado, y si la serie de 18 ítems es de un área de calidad. ⭐ **Es
además una vía de entrada distinta a la de la jefatura**, y con alguien que ya está haciendo el
mismo trabajo.

---

## 2.9 ⭐⭐⭐ Contra el objetivo declarado: AIDA es más larga justo donde el asesor tiene menos tiempo

> **Añadido el 2026-08-22.** Las secciones anteriores miden **calidad**. Ésta mide contra el
> **objetivo**: reducir el tiempo operativo del asesor **durante la venta**. Son dos mediciones sin
> interpretación de texto — largo de respuesta y turnos por sesión— y ninguna estaba hecha.
> *(Todas las cifras de esta sección excluyen la batería de prueba de §2.8.)*

### El largo de la respuesta, por tipo de consulta

| Tipo de consulta | n | **Mediana de palabras** | % de más de 200 palabras | Momento de uso |
|---|---|---|---|---|
| ⚠️ **Speech** | 187 | ⚠️ **502** | **90%** | 🟡 Preparando |
| ⚠️⚠️ **Objeción** | 19 | ⚠️⚠️ **485** | **84%** | 🔴 **En vivo** |
| ⚠️ **Explicar un concepto** | 55 | **387** | 78% | 🔴 **En vivo** |
| ⚠️ **Comparar opciones** | 115 | **260** | 74% | 🔴 **En vivo** |
| Dato de producto | 386 | 207 | 59% | 🔴 En vivo |
| Trámite | 264 | 207 | 63% | 🟢 Después |
| **Todo el corpus** | **2.531** | **205** | **53%** | |

⭐⭐⭐ **El hallazgo, en una frase: las tres categorías del momento en vivo son las que devuelven las
respuestas más largas.** Una objeción devuelve **485 palabras** — cerca de tres minutos de lectura,
**con el cliente esperando en el teléfono**. Un dato de producto devuelve 207.

⭐ **Y contradice el objetivo sin necesidad de juzgar el contenido.** Si el propósito es reducir el
tiempo operativo durante la venta, **devolver 485 palabras no reduce el trabajo: lo traslada** — el
asesor todavía tiene que leer, filtrar y traducir a algo decible. **Es la misma lógica que la cita
que hay que abrir**, aplicada al cuerpo de la respuesta.

**Solo el 16,3% de las respuestas baja de 80 palabras**, que es aproximadamente lo que se puede leer
en voz alta o escanear de un vistazo delante de alguien.

⚠️ **La fila de objeción se apoya en n=19.** El largo mediano es robusto para lo que se afirma
—orden de magnitud— pero **no se debe derivar de ahí ninguna tasa de calificación**: la base
calificada es demasiado chica.

### Los turnos por sesión

| | Sesiones | % |
|---|---|---|
| **1 turno — preguntó y listo** | 127 | **25,9%** |
| 2-3 turnos | 132 | 26,9% |
| 4-6 turnos | 117 | 23,9% |
| ⚠️ **7 o más** | 114 | **23,3%** |

**Mediana: 3 turnos. Máximo: 69.**

⚠️ **Este dato es ambiguo a propósito, y hay que decirlo así.** Más turnos pueden ser **una
conversación legítima** —el asesor profundiza sobre un caso— o **la herramienta obligando a
reformular**. El log no los distingue: no hay campo que diga si el turno siguiente es una pregunta
nueva o la misma dicha de otro modo.

⭐ **Es exactamente lo que la corrida manual tiene que desambiguar**, y por eso el campo *"¿tuviste
que repreguntar?"* pasa a ser obligatorio. **Solo una de cada cuatro consultas se resuelve en un
turno** — si la mayoría de los turnos extra resultan ser reformulaciones, el objetivo declarado está
peor de lo que cualquier medición de exactitud sugiere.

---

## 3. ⚠️ Lo que retracté durante el análisis

**Una medición intermedia daba "81% de discrepancia sustantiva entre respuestas a la misma pregunta".
No sobrevive a la verificación y no debe usarse.**

**Qué pasó:** el método comparaba las cifras con unidad (%, años, días) que aparecían en cada
respuesta. Al revisar los casos concretos, la mayor parte de esa "discrepancia" resultó ser
**variación en cuánto detalle menciona cada respuesta**, no contradicción entre datos — y en un caso
el patrón capturaba montos en soles como si fueran porcentajes.

⭐ **La versión que sí aguanta es la de §2.1** —inestabilidad de recuperación, 68,2%— porque **compara
un campo del log contra sí mismo, sin interpretar el texto.**

**Para afirmar contradicción de datos hacía falta revisión humana de una muestra.** ✅ **Se hizo, y el
resultado fue afirmativo — ver §2.7.** La contradicción existe y está verificada caso por caso; lo
que no existe es la cifra agregada de cuántas respuestas se contradicen. **Al miércoles va el caso,
no un porcentaje.**

---

## 4. Qué cambia en el plan

### 4.1 El banco sintético ya no hace falta

⭐ **Hay 2.697 preguntas reales.** El protocolo declaraba que el banco deducido de la matriz era
provisional y debía reemplazarse con preguntas de campo. **Ya se puede.**

**Las preguntas reales más frecuentes y más problemáticas pasan a ser el banco**, y las de control
diseñadas (producto inexistente, duplicado de tres nombres) se conservan.

### 4.2 La corrida manual cambia de propósito

**Ya no hace falta para descubrir si hay un problema — hace falta para caracterizarlo.** Se acorta y
se apunta:

| Qué | Antes | Ahora |
|---|---|---|
| Consistencia (Tanda 7) | 14 corridas en 4 días | ⭐ **Ya medida en los logs.** Solo confirmar 2-3 casos a mano |
| Banco de producto (Tandas 1-2) | Deducido de la matriz | **Reemplazado por las preguntas reales que fallaron** |
| Las 3 funcionalidades (Tanda 4) | Sin cambios | ⭐ **Sigue siendo necesaria** — los logs no dicen si el speech es plantilla |
| Latencia | Pendiente | ⚠️ **El log no trae tiempos.** Sigue haciendo falta cronometrar |

⚠️ **El archivo no incluye ninguna columna de duración.** La descomposición de los 9 segundos sigue
dependiendo de medirla a mano — y **conviene pedirla explícitamente** en el histórico completo.

### 4.3 Lo que ahora se puede llevar al miércoles con datos

1. **La misma pregunta no lee siempre lo mismo** — 68,2%, y 75,9% en Vida.
2. **Hay cuatro documentos bajo el código de Vida Flexible, y uno es de otro producto.**
3. **Documentos de Salud, Vehicular y la agenda corporativa alimentan al agente de venta de Vida.**
4. **La mitad de lo que lee está en PDF o Excel.**
5. **Los asesores castigan la falta de fuente 2 veces más, y el "no tengo esa información" 6 veces más.**
6. **274 asesores en dos días** — el problema no es de adopción.

⭐ **Ninguno de los seis requiere interpretación ni confrontar la palabra de nadie.** Salen del propio
sistema.

---

## 5. Qué pedir ahora

| # | Pedido | Por qué |
|---|---|---|
| 1 | 🔴 **El histórico completo de 3 meses**, con el rango declarado | Sin él no hay serie temporal ni análisis de preguntas abandonadas |
| 2 | ⭐ **Tiempos de respuesta por consulta**, si existen | Es la única vía para la descomposición de los 9 segundos a escala |
| 3 | **El inventario del SharePoint**, no solo lo citado | Los logs muestran los **199 documentos que se usaron**; no los que están y nunca se recuperan |
| 4 | **Qué es `aida_service`** y si debe estar en las métricas de adopción | Son 651 consultas en 2 días que **probablemente están infladas en el dashboard** |
| 5 | **El significado de los ramos `direct`, `otro` y `general`** | Son el 40% del volumen y no está claro si pasan por recuperación |

⚠️ **El punto 4 es delicado y conviene manejarlo con cuidado:** si esa cuenta está contando en los
30.000 mensuales, **la cifra de adopción que se reporta hacia arriba está inflada**. No es una
acusación —puede ser un monitoreo legítimo— pero **hay que saberlo antes de que alguien más lo
descubra.**

---

## Conexiones

- `[[diagnostico-copiloto-ai-asesor-vida-rimac]]` — las hipótesis que este análisis confirma o cierra.
- `[[aida-banco-preguntas-corrida]]` — el banco sintético que estos logs permiten reemplazar.
- `[[aida-roadmap-evaluacion]]` — el plan de corrida, que este análisis acorta.
- `[[arquitectura-conocimiento-agentes-copilot]]` — la evidencia externa sobre formatos, confirmada
  acá sobre el caso real.
