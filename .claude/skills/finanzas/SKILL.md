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
| Datos nuevos del mes (sueldo, gastos, cuotas) | Agrega filas al CSV del mes, corre `resumen`, actualiza `estado.md` |
| "cuándo salgo de la deuda", "cuánto me cuesta" | `python finanzas.py deuda --saldo N --cuota N --tcea ...` |
| "y si sigo así" | `python finanzas.py proyeccion --mes AAAA-MM --saldo N --cuota N` |
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
3. **Ninguna tasa se inventa.** La TCEA sale del estado de cuenta del usuario. Mientras
   no esté, se muestran escenarios (`--tcea 0 40 60 90`) etiquetados como rango de
   referencia, nunca como su tasa.
4. **El déficit se carga a la tarjeta.** Al proyectar, un mes que cierra en negativo
   suma ese déficit a la deuda — es lo que pasa en la práctica. Proyectar con el
   déficit "cubierto por arte de magia" da un plan que no se cumple.
5. **Los supuestos se escriben** en §4 de `estado.md`, con lo que se interpretó y qué
   dato lo confirmaría.
6. **No se editan meses cerrados.** Dato nuevo de un mes pasado = fila nueva con `nota`.
7. **Sin datos bancarios.** Ni números de tarjeta, ni cuentas, ni credenciales — solo
   montos y saldos.

## Tono

Directo y sin condescendencia. Los números se dicen completos, incluso cuando el mes
cierra mal: el valor del sistema es que el usuario vea la situación real, no una
versión amable. Nada de sermones sobre gastar menos — el usuario sabe lo que gasta;
lo que necesita es la aritmética y la consecuencia.

Esto es contabilidad personal, **no asesoría financiera regulada**. No recomiendes
productos financieros específicos ni instrumentos de inversión.
