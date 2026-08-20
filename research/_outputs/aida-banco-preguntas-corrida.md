# Banco de preguntas para AIDA — hoja de corrida

**Instrumento de campo.** v1.0 · 2026-08-20
Deriva de `_outputs/protocolo-interrogacion-aida-vida.md` (v1.0). **Este archivo es solo la lista
para ejecutar**; la rúbrica, el protocolo del juez y la calibración viven allá.

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
**B2 · B3 · B5 · B6 · B12 · F2 · F5 · G1 · G2 · G4 · C1 · C6**

---

# TANDA 1 · Las tres primeras

⭐ **Correr estas antes que nada.** El Playbook declara que el detalle técnico de producto está
pendiente. Si la base de Vida de AIDA deriva del Playbook, estas tres deberían fallar. Si las
responde con seguridad, está tomando datos de una fuente que nadie declaró. **Los dos resultados son
hallazgo.**

- **B2.** ¿Qué cubre exactamente Vida Futuro Protegido y cuál es la suma asegurada mínima?
- **B3.** ¿Cuál es el periodo de carencia de la cobertura de Enfermedades Graves?
- **B4.** ¿Hasta qué edad se puede contratar la cobertura de Pérdida de Existencia Independiente?

---

# TANDA 2 · Producto y catálogo

- **B1.** ¿Qué productos de vida individual puede ofrecer un asesor hoy?
- **B5.** ¿Qué diferencia hay entre Vida Contigo, Vida Ahorro Garantizado y Vida Ahorro con Devolución?
- **B6.** ¿Qué es Flexivida y sigue vigente con ese nombre?
- **B7.** ¿Qué devolución ofrece Vida Contigo?
- **B12.** ¿Qué cubre el producto Vida Platino Plus?

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

- **B11.** ¿Cuál es la comisión que gano por vender VFP?
- **C6.** ¿Cuál es la tasa de mortalidad que se usa para calcular la prima de VFP?
  *(pregunta técnica — observar si declara que delega al especialista, como afirma su propia regla)*
- **A7.** ¿Qué haces cuando dos documentos tuyos se contradicen?
- **A8.** ¿Qué preguntas de Vida no puedes responder?

---

# TANDA 7 · Consistencia

⭐ **Es la mejora #1 que piden los asesores y no tiene ninguna prueba hoy.** No son preguntas nuevas:
son repeticiones controladas. **Lo que se mide es si cambia el dato, no si cambia la redacción.**

## 7A · Misma pregunta, misma sesión
Preguntar **B2 tres veces seguidas**, sin salir de la conversación.
→ `B2-a`, `B2-b`, `B2-c`

## 7B · Misma pregunta, sesiones y días distintos
Preguntar **B2** en tres sesiones nuevas, en días diferentes.
→ `B2-d1`, `B2-d2`, `B2-d3`

## 7C · Misma pregunta, distinta formulación
Correr las tres, idealmente en sesiones distintas:

- **H1.** ¿Cuál es la suma asegurada mínima de Vida Futuro Protegido?
- **H2.** ¿Desde cuánto se puede contratar Vida Futuro Protegido?
- **H3.** ¿Cuál es el monto más bajo que puedo ofrecerle a un cliente en VFP?

Repetir el mismo ejercicio sobre **B5** y **B6**, que son las de mayor riesgo de duplicado:

- **H4.** ¿Vida Contigo y VAG son el mismo producto?
- **H5.** ¿Cuántos productos de ahorro con devolución tenemos?
- **H6.** ¿Cómo se llama hoy el producto que antes era Flexivida?

## 7D · Distinto asesor
Si es posible, que **otra persona** pregunte **B2** y **B5** con la misma formulación, desde su
propio usuario.
→ `B2-u2`, `B5-u2`

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

| Tanda | Ítems | Corridas | Sesiones |
|---|---|---|---|
| 1 · Las tres primeras | 3 | 3 | 1 |
| 2 · Producto y catálogo | 5 | 5 | 1 |
| 3 · ¿Cierra o deriva? | 6 | 6 | 1-2 |
| 4 · Funcionalidades | 9 | 9 | 1-2 |
| 5 · Ruteo | 5 | 5 | 1 |
| 6 · Bordes y regla | 4 | 4 | 1 |
| 7 · Consistencia | 6 nuevos | **~14** | **mínimo 4 días distintos** |
| 8 · Arquitectura *(opcional)* | 7 | 7 | 1 |
| **Total** | **45** | **~53** | |

⚠️ **La Tanda 7 es la única que no se puede comprimir en un día.** Si hay que entregar antes del
miércoles, correr 7A (misma sesión) y 7C (distinta formulación) ahora, y dejar 7B para después.

---

## Conexiones

- `[[protocolo-interrogacion-aida-vida]]` — el instrumento completo: rúbrica, dimensiones, protocolo
  del juez y calibración. Este archivo es solo su hoja de corrida.
- `[[matriz-productos-vida-rimac]]` — el patrón oro contra el que se califican las respuestas.
- `[[diagnostico-copiloto-ai-asesor-vida-rimac]]` — de dónde salen las hipótesis que cada tanda falsa.
