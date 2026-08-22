---
name: finanzas
description: >-
  Lleva las finanzas personales del usuario mes a mes: registra ingresos, gastos y
  deudas en `finanzas/`, calcula cómo cierra el mes, cuánto cuesta realmente la deuda
  y qué pasa si el escenario se repite. Úsalo SIEMPRE que el usuario invoque
  /finanzas, o cuando pegue su sueldo, gastos, cuotas, deudas o "status" del mes;
  cuando pregunte cómo va, si le alcanza, cuánto le queda, si puede pagar algo, en
  cuánto tiempo sale de una deuda, o si conviene subir o bajar una cuota; cuando
  mencione tarjeta de crédito, TCEA, alquiler, adelanto de sueldo o presupuesto.
  Dispárate aunque no diga "finanzas": si el usuario está poniendo números de su
  plata sobre la mesa, esto aplica.
---

# finanzas · Seguimiento de finanzas personales

> Invocación: **`/finanzas`**. Fuente de verdad: `finanzas/estado.md`.

Sistema de seguimiento mensual: datos en CSV, cálculos en `finanzas/finanzas.py`
(solo stdlib), interpretación en `finanzas/estado.md`.

## Primero, lee el estado

Antes de responder nada, lee `finanzas/estado.md`: trae la foto vigente, la deuda,
**los supuestos abiertos** y la bitácora. Nunca reconstruyas el panorama de memoria ni
desde el chat — el mes cerrado manda.

## Qué hacer según lo que pida el usuario

| Pide | Haz |
|---|---|
| "cómo voy", "cómo cierra el mes" | `python finanzas.py resumen --mes AAAA-MM` |
| "me pagan el martes", "cuánto abono", "cómo reparto el sueldo" | `python finanzas.py reparto --mes AAAA-MM --reserva N --minimo N` |
| Datos nuevos del mes (sueldo, gastos, cuotas) | Agrega filas al CSV del mes, corre `resumen`, actualiza `estado.md` |
| "cuándo salgo de la deuda", "cuánto me cuesta" | `python finanzas.py deuda --saldo N --cuota N --tcea ...` |
| "y si sigo así" | `python finanzas.py proyeccion --mes AAAA-MM --saldo N --cuota N --variables N` |
| Menciona ahorros, inversiones, ETFs, un bien de valor | Agrégalo a `patrimonio.csv` y corre `patrimonio` |
| "cuánto tengo", "cuánto valgo", "me conviene vender X" | `python finanzas.py patrimonio --tcea N --colchon N` |
| Menciona CTS, gratificación, bono, utilidades | Agrégalo a `calendario.csv` en su mes y **vuelve a proyectar** — puede cambiar el plan |
| "¿puedo pagar X?" | Compara contra la **brecha** del resumen, no contra el sueldo |
| Cerrar el mes | Nueva entrada en la Bitácora (§5) + nuevo CSV para el mes siguiente |

## Reglas de la casa

1. **Ingresos completos, deuda aparte.** El sueldo entra íntegro como `ingreso`; los
   descuentos que repagan algo ya cobrado (adelantos, préstamos de planilla) salen como
   `tipo=deuda`. Netear el sueldo esconde el servicio de deuda, que es justo el número
   que importa.
2. **Cero no es lo mismo que vacío.** Si una categoría base no está registrada, es un
   **hueco**, no un gasto de cero. El script lo marca — no lo silencies ni lo estimes
   sin decir que lo estimaste (`estado=estimado`).
3. **Las deudas se atacan de la tasa más cara a la más barata, sin excepción.** Una deuda al
   0% (cuotas sin intereses, adelanto de planilla) **nunca** se adelanta mientras exista una
   cara: es financiamiento gratis y adelantarlo es regalarlo. Registra la `tcea` de cada
   pasivo en `deuda.csv` — sin eso no hay orden de ataque posible.
4. **Cuidado con el doble conteo.** Una compra en cuotas hecha con la tarjeta ya está dentro
   del saldo de la tarjeta. Si además figura como gasto mensual propio, está contada dos
   veces y los intereses proyectados quedan inflados. Verifícalo antes de proyectar.
5. **La cuota de la tarjeta se marca con la categoría reservada `tarjeta_credito`** en el CSV
   del mes. Sin esa marca, `proyeccion` no distingue lo que amortiza la tarjeta de lo que no,
   y cualquier `--cuota` distinta de la registrada da números falsos.
6. **El día de pago se reparte en orden: no negociable → reserva de vida → tarjeta.** Nunca al
   revés. Fijar primero la cuota y vivir con lo que sobre es exactamente cómo se termina
   financiando la comida con la tarjeta. Si el gasto de vida no está medido, se registra como
   `reserva_vida` con `estado=estimado`: cuadra el mes sin fingir que el dato existe.
7. **Ni un retiro de ahorros ni un préstamo son ingreso.** Van como `tipo=ingreso` con
   categoría `ahorro` o `prestamo_recibido` para que el mes cuadre, pero quedan fuera del
   denominador de los ratios y el resumen lo advierte. Un mes malo no puede verse sano por
   haber vaciado la cuenta o pedido prestado.
8. **Un adelanto o préstamo puente se compara contra las demás fuentes a igual nivel de vida**,
   por la liquidez al final del horizonte — no por su tasa suelta. Y se pide **solo lo que se
   necesita**: cada sol de más cuesta interés y aprieta el mes siguiente, que es cuando se
   devuelve. Si se recomienda uno, va con su **condición de salida** explícita: qué lo
   justifica una vez y qué señal indicaría que dejó de ser puente y se volvió mecanismo.
9. **El pago mínimo de la tarjeta es un piso, no una opción.** Si la cuota sostenible cae por
   debajo del mínimo, el mínimo manda y el hueco se cubre por otro lado — y ahí se comparan las
   fuentes por su efecto **neto** a fin del horizonte, contando el activo que se consume, no
   solo la caja que queda.
10. **La cuota correcta es la sostenible**, no la más alta posible:
   `cuota = ingresos − fijos − variables − otros pagos de deuda`. Pagar más solo hace que la
   diferencia rebote a la tarjeta el mismo mes (resultado final idéntico, con la ilusión de
   avanzar); pagar menos acumula efectivo al 0% mientras se debe al 60%.
11. **Una deuda saldada se marca `cancelado` en `deuda.csv`, no se borra.** Deja de sumar al
   patrimonio neto y al orden de ataque, pero la fila queda como historial.
12. **Ninguna tasa se inventa.** La TCEA sale del estado de cuenta del usuario. Mientras
   no esté, se muestran escenarios (`--tcea 0 40 60 90`) etiquetados como rango de
   referencia, nunca como su tasa.
13. **El déficit se carga a la tarjeta.** Al proyectar, un mes que cierra en negativo
   suma ese déficit a la deuda — es lo que pasa en la práctica. Proyectar con el
   déficit "cubierto por arte de magia" da un plan que no se cumple.
14. **Lo irregular va a `calendario.csv`, no al CSV mensual.** CTS, gratificaciones, bonos y
   utilidades son eventos de un mes. Mezclarlos con la estructura mensual infla el promedio y
   simula una holgura que no existe.
15. **Antes de recomendar qué hacer con un ingreso extraordinario, corre los dos destinos**
   (`--extraordinario deuda` y `--extraordinario caja`) y compara. Si la diferencia es chica,
   dilo: significa que la decisión no es esa, y seguir tratándola como importante distrae del
   número que sí manda.
16. **Antes de recomendar liquidar un activo para pagar deuda, corre las dos proyecciones**
   (`--saldo` con y sin el activo aplicado) y resta lo que el usuario deja de tener. La tasa
   valla sola exagera el beneficio: si la deuda muere en pocos meses, el interés evitado
   corre solo esos meses. Y contrasta siempre contra el **runway** — cuántos días de gasto
   fijo cubre lo líquido. Quedarse sin colchón para ahorrar intereses reconstruye la deuda.
17. **Corre la sensibilidad al gasto variable** (`--variables` con varios valores) antes de dar
   un diagnóstico. Casi siempre pesa más que los extraordinarios, y sin eso el consejo apunta
   al lugar equivocado.
18. **Los supuestos se escriben** en §7 de `estado.md`, con lo que se interpretó y qué
   dato lo confirmaría.
19. **No se editan meses cerrados.** Dato nuevo de un mes pasado = fila nueva con `nota`.
20. **Sin datos bancarios.** Ni números de tarjeta, ni cuentas, ni credenciales — solo
   montos y saldos.

## Tono

Directo y sin condescendencia. Los números se dicen completos, incluso cuando el mes
cierra mal: el valor del sistema es que el usuario vea la situación real, no una
versión amable. Nada de sermones sobre gastar menos — el usuario sabe lo que gasta;
lo que necesita es la aritmética y la consecuencia.

Esto es contabilidad personal, **no asesoría financiera regulada**. No recomiendes
productos financieros específicos ni instrumentos de inversión.
