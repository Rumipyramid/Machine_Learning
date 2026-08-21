# 💰 Estado financiero — Alejandro

*Foto vigente: **agosto 2026**. Última actualización: 2026-08-21.*

Fuente de verdad del seguimiento de finanzas personales. Los montos vienen de
`movimientos/AAAA-MM.csv` y `deuda.csv`; los cálculos, de `finanzas.py`. Si un número
de este documento no sale de correr el script, es un supuesto y está marcado como tal.

---

## 1. Cómo cierra agosto

| | Monto | Nota |
|---|---:|---|
| Ingresos | **S/ 6,700** | Sueldo 6,500 + cochera 200 |
| Gastos fijos | **S/ 2,610** | Alquiler, mantenimiento, cámara, terapia, IA |
| Gastos variables | **S/ 0** | ⚠️ No hay ninguno registrado — ver §5 |
| Servicio de deuda | **S/ 4,200** | Cuota TC 3,000 + adelanto 1,200 |
| **Balance del mes** | **S/ -110** | |

```
python finanzas.py resumen --mes 2026-08
```

### Lo que dice esta foto

**El mes cierra en rojo por S/ 110 — y eso es antes de comer.** El presupuesto no
registra alimentación, transporte, servicios (luz, agua, internet) ni celular. Lo
que hoy aparece como un déficit chico es en realidad el piso de un déficit mayor.

**63% de los ingresos se va en servicio de deuda** (4,200 de 6,700). La referencia
habitual de sostenibilidad está por debajo de 30%. Los gastos fijos, en cambio, están
sanos: 39% de los ingresos, dentro de rango. El problema no es el tren de vida —
es la deuda.

**La cuota de 3,000 está calibrada por encima de la capacidad de pago.** Descontando
fijos y el adelanto, quedan S/ 2,890 para la tarjeta. La cuota es 3,000. Faltan 110,
más todo lo que cuesten los huecos del §6.

---

## 2. Deuda

| Acreedor | Instrumento | Saldo | Pago agosto | TCEA |
|---|---|---:|---:|---:|
| Banco | Tarjeta de crédito | S/ 10,000 | 3,000 | ❓ por confirmar |
| Empleador | Adelanto de sueldo | ❓ por confirmar | 1,200 | 0% |

La deuda total **no es 10,000**: es 10,000 más el saldo pendiente del adelanto, que
todavía no está registrado.

### Cuánto cuesta la tarjeta según la tasa

Pagando 3,000/mes y **sin volver a usar la tarjeta**:

| TCEA | Meses | Total pagado | Intereses |
|---:|---:|---:|---:|
| 0% (referencia) | 4 | S/ 10,000 | S/ 0 |
| 40% | 4 | S/ 10,665 | S/ 665 |
| 60% | 4 | S/ 10,958 | S/ 958 |
| 90% | 4 | S/ 11,360 | S/ 1,360 |

```
python finanzas.py deuda --saldo 10000 --cuota 3000 --tcea 0 40 60 90
```

Estas cuatro tasas son un rango de referencia, no tu tasa. **La TCEA real está en tu
estado de cuenta** y hay que registrarla en `deuda.csv`: entre 40% y 90% hay S/ 700 de
diferencia en cuatro meses.

### El escenario que sí importa

El cuadro de arriba asume que la tarjeta no se vuelve a usar. Pero si el mes cierra
en -110 y no hay ahorro, ese déficit se paga con la tarjeta. Y si los huecos del §3
suman, digamos, 1,500 al mes, el déficit real es de ~1,610:

| Escenario (TCEA 60%) | Meses hasta saldar | Total desembolsado | De eso, intereses |
|---|---:|---:|---:|
| Sin consumo nuevo | 4 | S/ 10,958 | S/ 958 |
| Con déficit de 110/mes cargado a la TC | 4 | S/ 11,425 | S/ 985 |
| Con déficit de 1,610/mes cargado a la TC | **9** | S/ 26,520 | **S/ 2,030** |

El "total desembolsado" incluye el consumo nuevo que se fue cargando (en el tercer
escenario, 9 × 1,610 = S/ 14,490 de gasto real de vida). La columna que mide el costo
de la deuda es la de intereses: pasar de 4 a 9 meses **duplica** lo que le pagas al
banco por el mismo saldo inicial.

```
python finanzas.py deuda --saldo 10000 --cuota 3000 --tcea 60 --consumo-nuevo 1610
```

Esta es la trampa de fondo: **pagar 3,000 al mes no baja la deuda si el mes cierra en
negativo y el hueco lo cubre la misma tarjeta.** Se paga mucho y el saldo no se mueve.
Cerrar el déficit mensual vale más que subir la cuota.

---

## 3. Calendario de ingresos irregulares

Eventos ya conocidos, en `calendario.csv`. No son parte de la estructura mensual: entran
solo en el mes que corresponde.

| Mes | Concepto | Monto | Estado |
|---|---|---:|---|
| 2026-11 | Retiro de CTS | S/ 4,500 | estimado |
| 2026-12 | Gratificación | S/ 6,500 | estimado |

**La gratificación probablemente sea mayor que 6,500.** Se calcula sobre el sueldo **bruto**,
no descuenta AFP/ONP, y la Ley 30334 agrega una bonificación extraordinaria (~9% si estás en
EsSalud, ~6.75% con EPS). Como los 6,500 del §1 están registrados como sueldo *neto*, el
depósito de diciembre puede ser bastante más alto. Vale confirmarlo con planilla: es el
número más grande del trimestre y está estimado a la baja.

---

## 4. Runway agosto → marzo

Proyección mes a mes con el calendario aplicado. Modela lo que pasa de verdad cuando el mes
no alcanza: la cuota se paga igual, pero el faltante vuelve a la tarjeta.

```
python finanzas.py proyeccion --mes 2026-08 --saldo 10000 --cuota 3000 \
    --tcea 60 --meses 8 --variables 1500 --otros-deuda-hasta 2026-08
```

### Hallazgo 1 — la tarjeta muere sola, con o sin CTS

Con una cuota de 3,000 la tarjeta se cancela en **noviembre o diciembre en prácticamente todo
el rango de escenarios** (gasto variable de 0 a 3,000/mes). El CTS y la gratificación no son
lo que te saca de la deuda: la cuota mensual ya lo hace.

Y el corolario incómodo: aplicar el CTS + la gratificación a la tarjeta en vez de dejarlos en
caja cambia el resultado final en **S/ 66** sobre ocho meses (19,312 vs. 19,246). Es
indiferente. La razón es el calendario: para cuando llega el dinero, ya casi no queda saldo
que amortizar.

### Hallazgo 2 — lo que decide todo es el gasto variable, no los extraordinarios

Misma cuota, mismo CTS, misma gratificación. Solo cambia lo que gastas al mes en comida,
transporte y servicios:

| Gasto variable | TC en cero | Caja acumulada a marzo |
|---:|---|---:|
| S/ 0 | 2026-11 | S/ 31,549 |
| S/ 1,000 | 2026-11 | S/ 23,424 |
| S/ 1,500 | 2026-11 | S/ 19,312 |
| S/ 2,000 | 2026-11 | S/ 15,189 |
| S/ 3,000 | 2026-12 | S/ 6,786 |

**Un rango de S/ 25,000 según un dato que todavía no está medido.** Los 11,000 de CTS +
gratificación son menos de la mitad de lo que está en juego en esa columna.

### Hallazgo 3 — el escenario donde nada de esto alcanza

Si el adelanto de 1,200 **se repite todos los meses** y el gasto variable ronda los 2,500:

| Mes | Pago a la TC | Saldo TC |
|---|---:|---:|
| 2026-08 | 3,000 | 10,009 |
| 2026-09 | 3,000 | 10,019 |
| 2026-10 | 3,000 | 10,029 |

Tres meses, S/ 9,000 pagados, y el saldo **sube**. Todo se va en intereses y en el déficit que
vuelve a la tarjeta. En ese escenario el CTS y la gratificación entran completos y se
evaporan: llegas a marzo con S/ 2,299 de caja. Si además el gasto variable llega a 3,000, la
tarjeta **no se cancela nunca**, ni con los 11,000 encima.

### La prueba de octubre

No hace falta esperar a diciembre para saber en qué escenario estás. **Al cerrar octubre, mira
el saldo de la tarjeta:**

- Debajo de S/ 5,000 → vas por el camino bueno, la cuota está funcionando.
- Cerca de S/ 10,000 → estás en el hallazgo 3: la cuota es teatro y el problema es el déficit
  mensual, no la deuda.

### Qué hacer con el CTS

Si la tarjeta se cancela sola en noviembre, **retirar el CTS para pagarla no tiene sentido**:
llega cuando ya no hay casi nada que amortizar, y ahorra 66 soles. El CTS es tu seguro de
desempleo, gana interés donde está, y sacarlo para que se quede parado en una cuenta al 0%
es perder por los dos lados.

El orden que se desprende de los números:

1. **No retires el CTS todavía.** Decidilo en noviembre, con el saldo real de octubre en la
   mano. Si estás en el escenario del hallazgo 3, ahí sí sirve — y mucho.
2. **La gratificación de diciembre es la que construye el colchón**, no el CTS. Es el único
   ingreso del año lo bastante grande para crear un fondo de emergencia sin tocar la
   indemnización.
3. **El colchón es lo que impide volver a la tarjeta.** Un mes que cierra en cero y sin
   reserva es exactamente lo que produjo los 10,000 actuales. Salir de la deuda sin construir
   la reserva es repetir el ciclo con otra fecha.

---

## 5. Patrimonio

Activos en `patrimonio.csv`, ordenados por qué tan rápido se convierten en plata.

| Activo | Liquidez | Valor | Nota |
|---|---|---:|---|
| Caja Arequipa | inmediata | S/ 700 | |
| ETFs y acciones | días | S/ 1,125 | US$ 300 |
| S&P 500 | días | S/ 1,125 | US$ 300 |
| Pokémon TCG | baja | S/ 790 | valuación incierta; el precio de venta real suele ser menor |
| Cámara profesional | baja | S/ 4,000 | herramienta de trabajo, todavía en cuotas |
| **Total activos** | | **S/ 7,740** | |
| Pasivos registrados | | S/ 10,000 | + adelanto y cuotas de cámara sin confirmar |
| **Patrimonio neto** | | **S/ -2,260** | es un **techo**: faltan pasivos por registrar |

```
python finanzas.py patrimonio --tcea 60 --colchon 700
```

### El número que importa no es el patrimonio, es el runway

Tu colchón líquido inmediato son S/ 700. Tus gastos fijos son S/ 2,610 al mes. Eso son
**ocho días** de cobertura. Contando ETFs y acciones (que se liquidan en días), sube a
**34 días**.

Esa es la fragilidad real. Un mes que cierra en cero, sin reserva y con una tarjeta
disponible es exactamente la máquina que produjo los 10,000 actuales.

### ¿Liquidar las inversiones para pagar la tarjeta?

La lógica de tasa valla dice que sí, y fuerte: tu deuda cuesta ~60% anual, y ningún ETF
rinde eso. Mantener S/ 2,250 invertidos mientras existe la deuda cuesta ~S/ 90 al mes.

Pero al correrlo contra el calendario real, el beneficio se achica mucho:

| Escenario | Sin liquidar (caja a marzo) | Liquidando 2,250 | Ganancia neta |
|---|---:|---:|---:|
| Realista (variables 1,500) | S/ 19,312 | S/ 21,943 | **S/ 381** |
| Pesimista (variables 2,500) | S/ 2,299 | S/ 5,035 | **S/ 486** |

*(Ganancia neta = diferencia de caja menos los 2,250 que dejas de tener invertidos.)*

La razón es la misma que con el CTS: la tarjeta se muere en noviembre/diciembre de todas
formas, así que el interés que evitas solo corre tres o cuatro meses.

**Veredicto: no liquides.** Ganar S/ 400 a cambio de pasar de 34 días de runway a 8, en la
situación exacta donde un imprevisto vuelve a la tarjeta al 60%, es un mal cambio. Los
S/ 400 se pierden en un solo mes malo.

Lo que sí conviene es **dejar de llamarlos inversión**: hasta que la tarjeta esté en cero y
el colchón construido, esos S/ 2,250 son tu fondo de emergencia, no tu cartera. No se tocan
para gastar, y no se aportan más hasta que la deuda muera.

*(Si igual decides liquidar, verifica antes el costo tributario de la ganancia de capital y
las comisiones de salida del bróker — pueden comerse buena parte de los S/ 400.)*

### La cámara

S/ 4,000 de valor: **52% de todo tu patrimonio en un solo activo ilíquido que además todavía
estás pagando.** Los 420/mes son el tercer gasto fijo más grande, después del alquiler y del
mantenimiento, y equivalen al 6% de tu ingreso.

Eso no la hace un problema — la hace la línea que más cambia según un dato que no tengo:
**¿genera ingresos?** Si es herramienta de trabajo que factura, es un activo productivo y la
cuota se paga sola. Si no, es la línea más discrecional de un presupuesto que cierra en rojo.

---

## 6. Lo que falta para que el modelo sea real

Cuatro datos cambian materialmente el diagnóstico. En orden de impacto:

1. **Gastos variables del mes** — alimentación, transporte, servicios, celular. Es el
   hueco más grande: define si el déficit real es de 110 o de 2,000.
2. **TCEA de la tarjeta** — está en el estado de cuenta. Define cuánto de los 3,000
   mensuales es pago real y cuánto es interés.
3. **Saldo pendiente del adelanto** — si quedan más cuotas de 1,200, el alivio de
   agosto no llega cuando se piensa.
4. **Cuotas que faltan de la cámara** — 420/mes que en algún momento se liberan. Saber
   cuándo permite planificar.

A eso se suman dos del calendario (§3): el **monto real de la gratificación** (posiblemente
mayor que 6,500) y el **saldo exacto del CTS**. Y dos del patrimonio (§5): **cuántas cuotas
faltan de la cámara** —que es un pasivo sin registrar contra un activo de 4,000— y si la
cámara **genera ingresos**.

Mientras esos datos no estén, los números de este documento son un piso, no un retrato.

---

## 7. Supuestos vigentes

Se registran para poder corregirlos, no porque estén verificados:

- **Moneda:** soles (S/).
- **"Adelanto -1,200"** se interpreta como descuento en planilla que repaga un adelanto
  ya cobrado — o sea, servicio de deuda, no gasto. Por eso el sueldo entra completo
  (6,500) y el adelanto sale como egreso.
- **"Cochera +200"** se interpreta como ingreso por alquiler de una cochera propia.
- **"Cámara -420"** se interpreta como cuota mensual de un financiamiento, no compra única.
- **"IA -240"** se interpreta como suscripciones mensuales de herramientas.
- **El saldo TC de 10,000** se asume anterior al pago de agosto; el saldo de cierre
  proyectado (7,000) asume cero consumo nuevo en el mes.
- **Tipo de cambio S/ 3.75 por USD**, asumido. Los US$ 600 valen S/ 2,250 a esa tasa; el
  tipo de cambio real del día está en el BCRP y se pasa con `--tc`.
- **Los S/ 790 de Pokémon TCG** son valuación de mercado, no precio de venta. Los
  coleccionables se venden con descuento y con demora: como reserva de emergencia, no cuentan.
- **La cámara vale S/ 4,000** hoy; los equipos se deprecian, así que es un techo, no un piso.
- **Los US$ 300 en ETFs y los US$ 300 en S&P** se tratan como dos posiciones separadas
  (US$ 600 en total), según cómo fueron reportados.

---

## 8. Bitácora

Una entrada por mes, al cerrar. Formato: qué pasó, qué cambió respecto al mes anterior,
qué decisión se tomó.

### 2026-08 (c) — Entra el patrimonio

Se registran los activos: S/ 700 en Caja Arequipa, US$ 600 entre ETFs/acciones y S&P,
S/ 790 en Pokémon TCG y una cámara de S/ 4,000. Nuevo `patrimonio.csv` y comando
`patrimonio`.

Patrimonio neto **negativo: S/ -2,260**, y es un techo porque faltan pasivos por registrar
(adelanto, cuotas de la cámara). El dato operativo es otro: el colchón líquido inmediato
cubre **ocho días** de gastos fijos.

Se evaluó liquidar los US$ 600 contra la tarjeta. Ganancia neta S/ 381 (escenario realista)
a S/ 486 (pesimista) — poco, porque la tarjeta muere en noviembre/diciembre igual. Decisión:
**no liquidar**; se reclasifican como fondo de emergencia en vez de cartera de inversión.

### 2026-08 (b) — Entran CTS y gratificación al modelo

Se registran dos ingresos irregulares conocidos: CTS de 4,500 retirable en noviembre y
gratificación de un sueldo en diciembre. Se agrega `calendario.csv` y la proyección pasa a
ser calendario-aware.

Resultado que cambia el plan: **la tarjeta se cancela en noviembre/diciembre con o sin esos
11,000**, y aplicarlos a la deuda en vez de a caja cambia el resultado en 66 soles. La
decisión relevante no es cómo usar los extraordinarios sino cuánto se gasta al mes: entre
gastar 0 y 3,000 de variable hay 25,000 soles de diferencia en la caja de marzo. Decisión
tomada: **no retirar el CTS por ahora**, reevaluar en noviembre con el saldo real de octubre.

### 2026-08 — Mes 1: línea base

Primera foto del sistema. Balance -110 con el presupuesto incompleto. Servicio de deuda
en 63% de ingresos, fijos en 39%. Deuda TC de 10,000 con cuota de 3,000 y TCEA sin
confirmar. Pendiente: registrar gastos variables, TCEA, saldo del adelanto y cuotas
restantes de la cámara.

---

## Ver también

- [`research/yopersona/perfil.md`](../research/yopersona/perfil.md) — perfil profesional del
  usuario: el ingreso laboral que sostiene este presupuesto.

> Nota: `finanzas/` está **fuera** del hub Many Brains (`research/alma.md`) — es un registro
> operativo, no un node de investigación. Por eso este enlace es un link plano y no un
> wikilink recíproco.
