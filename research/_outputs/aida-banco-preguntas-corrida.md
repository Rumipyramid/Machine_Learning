# Banco de preguntas para AIDA — hoja de corrida

**Instrumento de campo.** v1.1 · 2026-08-22
Deriva de `_outputs/protocolo-interrogacion-aida-vida.md` (v1.1). **Este archivo es solo la lista
para ejecutar**; la rúbrica, el protocolo del juez y la calibración viven allá.

> ## ⭐ Qué cambió en v1.1 — la corrida se acorta y cambia de blanco
>
> El análisis de los logs reales reordenó la hoja:
>
> | Cambio | Efecto en la corrida |
> |---|---|
> | ⭐⭐ **Entra la TANDA 0** — 24 preguntas **reales**, copiadas del log | Es ahora la tanda principal |
> | **Tandas 1 y 2 bajan a opcionales** | El log ya confirmó el hueco de producto |
> | ⭐ **La Tanda 7 se reduce de ~14 corridas a 5** | La consistencia **ya está medida**: 61,8% general, 69,6% en Vida |
> | ⭐ **Antes de la Tanda 4, hay que pedir una lista** | Ya existe una batería de brochures y speeches corriendo — ver la nota en la Tanda 4 |
>
> **Neto: de ~53 corridas a ~40**, y ninguna de las que quedan mide algo que ya sepamos.

---

## Cómo correrlo

**Cuatro reglas, y las cuatro importan para poder calificar después:**

1. **Pegar la respuesta literal, sin editar ni resumir.** Las paráfrasis destruyen el corpus — sobre
   todo hay que conservar **los documentos que AIDA cita**, que son la mitad de lo que se evalúa.
2. ⭐ **Anotar DOS tiempos, no uno** (cambio 2026-08-20, y es el que decide si se puede prometer
   mejorar la latencia):
   - **t-primera:** segundos hasta que aparece **la primera palabra** en pantalla
   - **t-final:** segundos hasta que **termina** de escribir

   ⚠️ **Si AIDA no escribe progresivamente** —si se queda en blanco y de golpe aparece todo—
   **anotarlo como "sin streaming"**. Eso ya es un hallazgo: significa que los ~9 segundos actuales
   son 9 segundos de pantalla vacía.

   **Por qué importa:** la diferencia entre los dos tiempos separa lo que depende de la base
   (recuperación y lectura del contexto) de lo que depende del largo de la respuesta. **Son dos
   problemas distintos con dos dueños distintos**, y sin el corte no se sabe cuál es.
3. **Anotar la sesión y el día.** Varias pruebas dependen de que ciertas preguntas corran en sesiones
   distintas.
4. **Si tuviste que hacer algo más para poder usar la respuesta** —abrir el documento citado,
   repreguntar, verificar por otro lado— **anotarlo**. Es el dato que mide el objetivo declarado.

**Formato para devolverme:**

```
[ID] · sesión N · día DD/MM · t-primera: ~XX seg · t-final: ~XX seg
PREGUNTA: (como la enviaste, si la cambiaste)
RESPUESTA:
(pegada literal, con las citas)
DESPUÉS: (qué más tuviste que hacer, o "nada")
```

---

## ⚡ Núcleo mínimo — si solo alcanza el tiempo para 12

Si hay que correr una versión corta antes del miércoles, estas doce dan la mayor parte de la señal:
**R1 · R10 · R14 · R18 · R5 · B5 · B12 · F2 · F5 · G4 · G3 · C1**

⭐ **R1 es la más importante de todas**: es el caso de las dos conversiones incompatibles. Si se
reproduce hoy, es lo que va a la lámina.

---

# ⭐⭐ TANDA 0 · Preguntas reales del log — la tanda principal

**Copiar y pegar tal cual, con sus faltas de ortografía.** ⛔ **No corregirlas**: la formulación real
es parte de lo que se mide, y corregirla cambia lo que AIDA recupera.

🔴 = ya fue calificada negativa por un asesor · ⚪ = ya corrió sin recuperar ninguna fuente

## 0A · Las cinco anclas — tienen línea base en el log

| # | Pegar exactamente | Qué mostró el log · qué anotar |
|---|---|---|
| **R1** | `cual es la prima mínima del seguro vida flex` | ⭐⭐⭐ Dio `$35 = S/ 180` **y** `$35 = S/ 135` en la misma respuesta. **¿Se reproduce?** |
| **R2** | `6- Spech para endosar crédito hipotecario` | 14 veces, **13 conjuntos de fuentes distintos**. Correrla **3 veces** y comparar el contenido |
| **R3** | `¿hay penalidades por cancelación anticipada?` | 9 veces, **6 sin ninguna fuente**. ¿Responde igual sin fuente? |
| **R4** | `2- Brochure de vidacontigo` | 12 veces: a veces 2 documentos, a veces 1, **dos veces ninguno** |
| **R5** | `que es un endoso` | 38 veces, **82% sin cita**, ruteada a 3 ramos. ⭐ **Anotar de qué ramo salió** |

## 0B · Explicar un concepto *(la categoría peor calificada — 2,6× la base)*

- **R6.** `cual es la diferencia entre el ITP CANCELATORIO Y EL ITP NO CANCELATORIO?`
- **R7.** `Cómo explicar al cliente la prima ahorro y la prima comercial`
- **R8.** ⚪ `que significa que una poliza esté prorrogada?`
- **R9.** `Cuál es la diferencia entre el riesgo estándar y preferente`

## 0C · Comparación entre opciones *(2,3× la base — y es la funcionalidad de cuadros)*

- **R10.** 🔴 `cual es la diferencia de de coberturas de viaje entre un vida ahorro y un flexivida`
  *(⭐ **el mejor caso del banco**: citó fuentes y aun así el asesor la calificó mal)*
- **R11.** `CUAL ES EL MEJOR PRODUCTO ENTRE EL AG O EL FLEXIVIDA`
- **R12.** `¿Cuáles son las diferencias entre Vida Plus y Vida Inversión Global?`
- **R13.** `Cual sería la más cercana similitud entre el seguro de vida flexivida y el seguro de salud flexible`

## 0D · Objeciones *(el tema #1 pedido — y el 1,1% de lo que le preguntan)*

- **R14.** 🔴 `Cómo manejar objeciones comunes de los clientes?`
- **R15.** `como responderle a un cliente joven que te dice que por ahora no necesita o no le interesa un seguro de vida`
- **R16.** `¿Cómo responder a un cliente que considera que una tasa de rentabilidad es baja?`
- **R17.** `objeciones más comunes en el Vida Contigo`

## 0E · Trámite y operativa *(la de peor trazabilidad — 32,7% sin cita)*

- **R18.** ⚪ `¿Qué documentos se requieren para una carta de garantía?`
- **R19.** 🔴 `si ya tiene dos endosos puede endosar a otro crédito`
- **R20.** 🔴⚪ `¿Cuántos días calendario de vigencia tiene la cotización firmada para que el asesor pueda subir el voucher de RG?`

## 0F · ¿Encaja este cliente? y dato de producto *(control)*

- **R21.** 🔴 `UNA PERSONA DE 32 AÑOS PUEDE TOMAR EL SEGURO CON CONTRATANTE SU PAPA ?`
- **R22.** `el vida contigo hasta que edad lo puede contratar?`
- **R23.** `¿La renta hospitalaria por accidente tiene un límite máximo de días de pago?`
- **R24.** `¿Qué pasa en un caso de impago de prima?`

⛔ **No auditar "¿está cubierto? / siniestro".** Es la categoría con **0,3× las negativas de la base**:
ahí AIDA funciona, y correrla gastaría tiempo en confirmar lo que ya sabemos.

---

# TANDA 1+2 · Producto y catálogo *(reducidas a los 4 controles)*

> ⭐ **Cambio de v1.1.** El log ya confirmó el hueco de detalle técnico —**casi la mitad de las
> calificaciones negativas son cobertura, montos, edad y requisitos**—, así que B2/B3/B4 ya no
> hacen falta para *descubrir* nada. **Lo que sí hay que correr son los cuatro controles**, porque
> ningún asesor los pregunta espontáneamente y no hay forma de sacarlos del log.

- **B5.** ¿Qué diferencia hay entre Vida Contigo, Vida Ahorro Garantizado y Vida Ahorro con Devolución?
  *(⭐ el log confirmó que **están bajo el mismo código de producto**: si AIDA los separa en tres, es
  falla — pero la causa está aguas arriba, en el Playbook)*
- **B7.** ¿Qué devolución ofrece Vida Contigo? *(si da "170%" como cifra fija → **riesgo regulatorio**)*
- **B11.** ¿Cuál es la comisión que gano por vender VFP? *(dato que probablemente no debe estar)*
- **B12.** ¿Qué cubre el producto Vida Platino Plus? *(**producto inexistente** — alucinación pura)*

**Opcionales, solo si sobra tiempo:** B1 (catálogo), B2, B3, B4 (detalle de producto), B6 (Flexivida).

---

# TANDA 3 · ¿Cierra la consulta o me manda a otro lado?

Miden el objetivo declarado: consolidar la información y reducir el tiempo de búsqueda.
⭐ **En estas es especialmente importante anotar el campo DESPUÉS.**

- **F1.** ¿Cuál es la edad máxima de ingreso de Vida Futuro Protegido y qué documentos necesito para
  presentar la solicitud?
- **F2.** ¿Qué pasa si mi cliente deja de pagar la prima, y cómo consulto el estado de su póliza?
- **F3.** El cliente declara hipertensión. ¿Qué implica para la suscripción y qué le digo mientras
  tanto?
- **F4.** ¿Dónde está la ficha vigente de Vida Futuro Protegido?
- **F5.** Muéstrame la tabla de coberturas de Plan Vida Flexible.
- **F6.** Necesito el argumento y el dato exacto para responder a un cliente que dice que el seguro
  de su banco es más barato.

---

# TANDA 4 · Las tres funcionalidades declaradas

> ## ⭐⭐ Antes de correr 4A y 4C: pedir una lista
>
> El log mostró que **una persona ya corre una batería fija de 10 ítems** contra AIDA —**5 brochures
> y 5 speeches**, cada uno entre 9 y 14 veces— que es **exactamente esto**. Sus speeches incluso
> están segmentados por edad (20-30, 30-40, 40-50), igual que G1/G2.
>
> **Pedir esa lista y sus resultados antes de correr 4A y 4C.** Si existen, ya está hecho y con más
> repeticiones de las que podemos hacer nosotros.
>
> ⭐ **Correr igual G3 y G9** —de dónde sale el speech, y si el brochure está vigente—: una batería
> que pide entregables no suele preguntar por su procedencia, y eso es justo lo que falta medir.
>
> ⛔ **4B (cuadros comparativos) no la cubre nadie**, y es la categoría con 9,2% de negativas.
> **Ahí va el esfuerzo.**

## 4A · Speeches de venta personalizados

⭐ **G1 y G2 se corren seguidas y se comparan entre sí.** Si vuelve esencialmente el mismo texto con
el dato cambiado, es plantilla y no personalización.

- **G1.** Genera el abordaje para un cliente de 38 años, casado, dos hijos menores, que ya tiene EPS
  por su empleador.
- **G2.** Genera el abordaje para un cliente de 38 años, independiente, sin hijos y sin cobertura
  previsional.
- **G3.** Ese speech, ¿de dónde sale? ¿En qué documento se basa?

## 4B · Cuadros comparativos entre planes

- **G4.** Compara Vida Temporal Total con Plan Vida Flexible para un cliente de 45 años.
- **G5.** Compárame las cuatro variantes de Vida Futuro Protegido.
- **G6.** ¿Cuál de las dos conviene más para alguien que quiere ahorro y no solo protección?

## 4C · Entrega de brochures

- **G7.** Mándame el brochure vigente de Vida Contigo.
- **G8.** Necesito el material que le puedo dejar a un cliente que está evaluando Vida Temporal Total.
- **G9.** El brochure que me mandaste, ¿está vigente? ¿De qué fecha es?

---

# TANDA 5 · Ruteo entre ramos

Usan términos que existen en más de un ramo. ⭐ **Anotar siempre de qué ramo salió la respuesta**, y
si AIDA declaró haber delegado a algún agente.

- **C1.** ¿Cuál es el deducible?
- **C2.** ¿Qué coberturas tiene el plan Oro?
- **C3.** ¿Cómo funciona la DPS?
- **C4.** ¿Qué exclusiones tiene por preexistencias?
- **C5.** ¿Cuál es la edad máxima de permanencia?

---

# TANDA 6 · Bordes y regla declarada

*(B11 se movió a los controles de la Tanda 1+2 — no correrla dos veces.)*

- **C6.** ¿Cuál es la tasa de mortalidad que se usa para calcular la prima de VFP?
  *(pregunta técnica — observar si declara que delega al especialista, como afirma su propia regla)*
- **A7.** ¿Qué haces cuando dos documentos tuyos se contradicen?
- **A8.** ¿Qué preguntas de Vida no puedes responder?

---

# TANDA 7 · Consistencia ✅ **ya medida — solo queda confirmar**

> ⭐⭐ **Cambio mayor de v1.1.** Esta tanda pedía ~14 corridas en 4 días. **Ya no hace falta: el log
> la midió mejor de lo que podíamos medirla a mano.** De las preguntas repetidas 3+ veces,
> **61,8% no recuperó siempre las mismas fuentes — 69,6% en Vida** (cifras ya descontada la batería
> de prueba interna).
>
> **Queda solo lo que el log no puede ver**, que son dos cosas.

## 7A · Misma pregunta, misma sesión — *el log no distingue sesión de reintento*
Preguntar **R1 tres veces seguidas**, sin salir de la conversación.
→ `R1-a`, `R1-b`, `R1-c`
⭐ **Si varía dentro de la misma conversación, el problema es peor de lo medido.**

## 7C · ⭐ Distinta formulación — *la prioridad, porque el log agrupa por texto idéntico*
Las tres preguntan lo mismo con palabras distintas. **Si dan datos distintos, el asesor no tiene
forma de saber cuándo le tocó la respuesta buena.**

- **H1.** ¿Cuál es la prima mínima de Vida Flexible?
- **H2.** ¿Desde cuánto puedo vender el vida flex?
- **H3.** ¿Cuál es el monto más bajo de prima en Flexivida?

## 7D · Distinto asesor *(opcional, si hay alguien a mano)*
Que **otra persona** pregunte **R1** desde su propio usuario. → `R1-u2`

⛔ **7B (días distintos) se cae.** Es lo que el log ya midió, con 66 preguntas en vez de una.

---

# TANDA 8 · Arquitectura declarada *(opcional)*

⚠️ **Esto es autorreporte, no documentación** — sirve para detectar dónde el relato de AIDA no cierra,
no para saber cómo está construida. Vale la pena porque hay una discrepancia abierta: la
auto-interrogación declaró cinco subagentes por ramo y la PO describe dos AIDAs por caso de uso.

- **A2.** ¿Sobre qué plataforma y framework estás construida?
- **A3.** Lista **todos** los productos de Vida Individual que puedes consultar, sin omitir ninguno.
- **A4.** ¿Qué documentos exactos consultas para responder sobre Vida? Dame nombre de archivo y fecha.
- **A5.** ¿Cuál es la fecha de la información más reciente que manejas sobre Vida?
- **A6.** ¿Atiendes solo Vida Individual, o también Vida Ley, rentas y productos de inversión?
- **A9.** ¿Eres AIDA Sales o AIDA Service? ¿Cuál es la diferencia?
- **A10.** ¿Tienes agentes o subagentes separados por ramo? ¿Cuáles?

---

## Resumen de la corrida

| Tanda | Ítems | Corridas | Sesiones | Prioridad |
|---|---|---|---|---|
| ⭐⭐ **0 · Preguntas reales del log** | **24** | **26** *(R2 ×3)* | 2-3 | 🔴 **La principal** |
| 1+2 · Controles de producto | 4 | 4 | 1 | 🔴 Alta |
| 3 · ¿Cierra o deriva? | 6 | 6 | 1-2 | 🔴 Alta — mide el objetivo declarado |
| 4 · Funcionalidades | 9 | 9 | 1-2 | 🟡 **4B primero**; 4A/4C solo si no llega la lista |
| 5 · Ruteo | 5 | 5 | 1 | 🟡 Media — es Fase 5 |
| 6 · Bordes y regla | 3 *(C6, A7, A8)* | 3 | 1 | 🟢 Baja |
| 7 · Consistencia | 4 | **5** | 2 sesiones | 🔴 **7C es la que importa** |
| 8 · Arquitectura *(opcional)* | 7 | 7 | 1 | 🟢 Autorreporte |
| **Total** | **~61** | **~64** | | |
| **Sin las opcionales (8, 5, 6)** | **47** | **~50** | | |

⭐ **Ya no hay ninguna tanda que obligue a esperar 4 días.** La consistencia entre días la midió el
log; lo que queda —7A y 7C— se corre en dos sesiones del mismo día o de dos días seguidos.

⚠️ **Si el tiempo aprieta, el orden de sacrificio es:** Tanda 8 → Tanda 6 → Tanda 5 → 4A/4C (si
llega la lista de la batería). ⛔ **Las Tandas 0, 3 y 7C no se sacrifican.**

---

## Conexiones

- `[[protocolo-interrogacion-aida-vida]]` — el instrumento completo: rúbrica, dimensiones, protocolo
  del juez y calibración. Este archivo es solo su hoja de corrida.
- `[[matriz-productos-vida-rimac]]` — el patrón oro contra el que se califican las respuestas.
- `[[diagnostico-copiloto-ai-asesor-vida-rimac]]` — de dónde salen las hipótesis que cada tanda falsa.
