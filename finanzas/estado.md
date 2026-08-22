# 💰 Estado financiero — Alejandro

*Foto vigente: **agosto 2026**. Última actualización: 2026-08-21.*

Fuente de verdad del seguimiento de finanzas personales. Los montos vienen de
`movimientos/AAAA-MM.csv` y `deuda.csv`; los cálculos, de `finanzas.py`. Si un número
de este documento no sale de correr el script, es un supuesto y está marcado como tal.

---

---

---

## 📅 El martes 25 — cómo repartir el sueldo

*El mínimo de la tarjeta en agosto es **S/ 2,500**. Eso no es negociable y cambia el reparto:
la cuota deja de ser la variable de ajuste y pasa a ser un dato fijo.*

```
python finanzas.py reparto --mes 2026-08 --reserva 1200 --minimo 2500
```

| | | |
|---|---:|---|
| **1. Entra** | **S/ 6,700** | sueldo 6,500 + cochera 200 |
| **2. Sale sí o sí** | **S/ 3,810** | alquiler 1,250 · préstamo 1,200 · cámara 420 · terapia 360 · mantenimiento 340 · IA 240 |
| Disponible | S/ 2,890 | |
| **3. Mínimo de la tarjeta** | **S/ 2,500** | piso del estado de cuenta |
| **Queda para vivir** | **S/ 390** | ← el problema |

**Agosto tiene un hueco de S/ 810.** Vivir un mes con 390 no es un plan de austeridad, es
imposible. La plata tiene que salir de algún lado, y la única pregunta buena es de dónde.

### De dónde salen los 810

Comparando por lo que te deja en el bolsillo a diciembre —contando el activo que consumes,
no solo la caja—:

| Opción | Caja a diciembre | + queda en Caja Arequipa | Total |
|---|---:|---:|---:|
| **A.** Caja Arequipa 700 + recortar 110 de vida | S/ 9,527 | S/ 0 | **S/ 9,527** |
| **B.** Cargar los 810 a la tarjeta | S/ 8,585 | S/ 700 | **S/ 9,285** |
| **C.** Pausar suscripciones IA un mes (240) + caja 570 | S/ 9,527 | S/ 130 | **S/ 9,657** |

**La opción B es la peor**, y por más de lo que parece: los 810 no cuestan un mes de interés
(S/ 32), cuestan cuatro —se quedan en el saldo hasta diciembre— y encima pierden el periodo de
gracia por ser consumo sobre saldo vigente. Diferencia contra A: **S/ 242**.

**Vender ETFs para esto tampoco:** te deja igual que A pero con comisiones y posible costo
tributario encima, y desarma la única reserva de días que tienes.

### Lo recomendado

**Opción C si puedes; si no, la A.** La diferencia entre las dos es chica (S/ 130) pero C es
la única que crea margen en vez de moverlo: los S/ 240 de suscripciones de IA son la **única
línea fija con juego real** en todo el presupuesto —el alquiler, el mantenimiento, la cámara y
la terapia no se tocan— y basta pausarlas un mes. Si son herramienta de trabajo que factura,
descártalo y anda por la A.

### En concreto, el martes

1. **Paga los S/ 2,500** a la tarjeta. Es el piso, no hay decisión que tomar ahí.
2. **Saca S/ 570 de Caja Arequipa** (o 700 si no pausas la IA) y **sepáralos con el resto de la
   plata de vida el mismo día**, físicamente.
3. **Vive con S/ 1,200** (o 1,090 en la opción A) hasta el próximo sueldo.
4. **Anota cada gasto desde el martes.** Este mes es el que define todo lo demás.

### Setiembre repone lo que agosto gasta

El préstamo muere con este pago y liberas 1,200/mes. Lo primero de setiembre es **devolver los
700 a Caja Arequipa**, antes de subir la cuota de la tarjeta.

Sí, es plata al 0% mientras debes al 60%. **Cuesta S/ 82 en total.** Por 82 soles, tener
colchón desde setiembre en vez de diciembre es una compra obvia: quedarte cuatro meses sin
liquidez es exactamente la condición que fabricó los 10,000 que estás pagando.

| Cierre de | A la tarjeta | Saldo tarjeta |
|---|---:|---:|
| Agosto | S/ 2,500 (mínimo) | S/ 7,899 |
| Setiembre | S/ 2,190 + 700 al colchón | S/ 6,025 |
| Octubre | S/ 2,890 | S/ 3,376 |
| Noviembre | S/ 2,890 | S/ 620 |
| Diciembre | S/ 645 | **S/ 0** |

Cierras diciembre con la tarjeta en cero y **S/ 9,445 de caja** — 3.6 meses de gastos fijos,
por encima del objetivo de 3. Diciembre sigue en verde, y ahora con el colchón repuesto desde
setiembre en vez de aparecer recién con la gratificación.

### ⚠️ El mínimo de 2,500 merece una mirada

**Es el 25% del saldo.** Para un mínimo revolvente es alto: lo habitual está bastante por
debajo. Lo más probable es que incluya **cuotas de compras hechas en cuotas**, que son
contractuales y no se pueden bajar.

Si es así, es buena noticia: significaría que una parte de los 10,000 está en cuotas **sin
intereses**, y entonces la tasa efectiva de tu deuda es menor que el 60% que venimos asumiendo
y los intereses proyectados están sobreestimados. Pídele al banco el desglose del saldo entre
revolvente y cuotas — es la misma llamada en la que preguntas la TCEA.

## 🩺 Diagnóstico vigente y plan a diciembre

*Corrido el 2026-08-22. Actualizado con el adelanto y la cámara confirmados: las dos
incógnitas grandes están cerradas y el escenario es el bueno.*

### El diagnóstico en tres frases

**No estás en crisis, estás sin instrumentos.** Tus gastos fijos son el 39% de tus ingresos
—sano— y el 63% que se fue en deuda es un pico de un solo mes, no una estructura: el adelanto
era único y ya está cancelado. La tarjeta se cancela sola en diciembre.

**Tu problema no es la deuda, es la falta de colchón.** S/ 700 líquidos contra S/ 2,610 de
gastos fijos son ocho días. Eso es lo que convierte cualquier imprevisto en saldo de tarjeta,
y es la máquina que fabricó los 10,000.

**Y estás volando a ciegas en la única variable que todavía decide el resultado.** El gasto
variable no está medido, y es lo único que separa terminar diciembre con 3.3 meses de colchón
o con 0.8.

### Qué significa "llegar en verde"

1. **Tarjeta en cero** al cerrar diciembre.
2. **Ningún mes rebotando** — que la cuota salga del sueldo, no de la misma tarjeta.
3. **Colchón de al menos 3 meses** de gastos fijos: S/ 7,830.

Con el adelanto cancelado, las tres son alcanzables **sin tocar el CTS**.

### Cuánto puedes gastar

Desde setiembre tu capacidad mensual es `6,700 − 2,610 − variable = 4,090 − variable`.
Sin retirar el CTS:

| Gasto variable | Cuota sostenible | Caja a diciembre | Colchón |
|---:|---:|---:|---:|
| S/ 800 | S/ 3,290 | S/ 10,714 | 4.1 meses |
| S/ 1,200 | S/ 2,890 | S/ 8,585 | **3.3 meses** ✅ |
| S/ 1,600 | S/ 2,490 | S/ 6,418 | 2.5 meses |
| S/ 2,000 | S/ 2,090 | S/ 4,252 | 1.6 meses |
| S/ 2,400 | S/ 1,690 | S/ 2,086 | 0.8 meses |

**Hasta S/ 2,750/mes de gasto variable, la tarjeta igual llega a cero en diciembre.** El
margen es cómodo; lo que se estrecha rápido es el colchón.

### El camino base, mes a mes

Variable 1,200 · cuota 2,890 · sin tocar el CTS:

| Cierre de | Saldo tarjeta | Caja |
|---|---:|---:|
| Agosto | S/ 8,709 | 0 |
| Setiembre | S/ 6,167 | 0 |
| **Octubre** | **S/ 3,524** | 0 |
| Noviembre | S/ 774 | 0 |
| Diciembre | **S/ 0** | **S/ 8,585** |

---

### Consejo 1 — Ponle techo de S/ 1,200 al gasto variable, y mídelo desde el 1 de setiembre

Es la palanca más grande y la única enteramente bajo tu control: entre gastar 1,200 y 2,400 al
mes hay **S/ 6,499** de diferencia en la caja de diciembre. Más que el CTS entero.

Con 1,200 cierras diciembre con 3.3 meses de colchón sin tocar nada más. Y hoy es el único
número grande del modelo que sigue siendo una adivinanza: el presupuesto tiene un agujero de
cuatro categorías (comida, transporte, servicios, comunicaciones) y todo lo demás ya está
confirmado.

No hace falta app: anota 30 días todo lo que salga y no sea fijo. **Setiembre es el mes de
medir**, y con el dato real recalibramos el techo.

### Consejo 2 — Los S/ 1,200 que se liberan en setiembre van a la tarjeta el día de pago

El adelanto era único y ya se pagó. Eso significa que en setiembre te "aparecen" 1,200 que en
agosto no tenías — y ese es exactamente el dinero que suele desaparecer sin que nadie decida
gastarlo. Absorbido en el estilo de vida, es la diferencia entre 3.3 y 0.8 meses de colchón.

Lo concreto: la cuota de setiembre sube a **S/ 2,890**, y sale **el día que entra el sueldo**,
antes de cualquier otro gasto. No al final del mes con lo que sobre — al final del mes nunca
sobra. Es la mecánica que hace que el consejo 1 se cumpla solo, en vez de depender de aguantar
treinta días.

La misma regla aplica cuando termine la cámara: son otros 420 que se liberan y que ya tienen
destino.

### Consejo 3 — La gratificación de diciembre va íntegra al colchón

En el camino base llegas a diciembre con S/ 8,585, y **prácticamente todo eso es la
gratificación**: setiembre, octubre y noviembre se van completos en matar la tarjeta.

Diciembre es el peor mes del año para tener 6,500 disponibles y ninguna regla. Si se va en
consumo, terminas con la tarjeta en cero y cero colchón — el mismo estado en que empezó este
año, con otra fecha. Decide **hoy** cuánto es colchón y cuánto es gasto de fin de año, no el
15 de diciembre.

Y confirma el monto real con planilla: la gratificación se calcula sobre el bruto, no descuenta
AFP/ONP y lleva bonificación extraordinaria (~9%), así que probablemente sea más de 6,500.

---

### La única verificación que queda

**¿Cuál es la TCEA real de la tarjeta?** Está en tu estado de cuenta. Entre 40% y 90% hay
S/ 873 de intereses de aquí a diciembre. Es el último dato del modelo que sigue siendo un
supuesto.

*(La verificación del doble conteo quedó cerrada: la cámara se compró directo a un amigo, no
pasa por la tarjeta.)*

### La regla de la cuota

Paga lo que sale de esta resta, recalculada cada mes:

```
cuota = 6,700 − 2,610 − gasto variable
```

Pagar más no acelera nada: la diferencia vuelve a la tarjeta el mismo mes (lo corrimos, el
resultado final es idéntico) y solo produce la ilusión de avanzar. Pagar menos es peor:
acumulas efectivo al 0% mientras debes al 60%.

### La prueba de octubre

Al cerrar octubre, el saldo de la tarjeta debería estar cerca de **S/ 3,500**. Si está por
encima de **S/ 5,000**, el gasto variable se salió del techo y ahí se reevalúa el CTS —que
hasta entonces no se toca.

## 1. Cómo cierra agosto

*Actualizado el 2026-08-22 con la cuota corregida a 1,690 y la reserva de vida registrada.*

| | Monto | Nota |
|---|---:|---|
| Ingresos | **S/ 6,700** | Sueldo 6,500 + cochera 200 |
| Gastos fijos | **S/ 2,610** | Alquiler, mantenimiento, cámara, terapia, IA |
| Gastos variables | **S/ 1,200** | ⚠️ Reserva estimada, sin desglosar — ver §6 |
| Servicio de deuda | **S/ 2,890** | Cuota TC 1,690 + préstamo 1,200 |
| **Balance del mes** | **S/ 0** | |

```
python finanzas.py resumen --mes 2026-08
```

### Lo que dice esta foto

**Agosto cuadra exacto, en cero, y solo porque la cuota bajó a lo que aguanta el mes.** Con
los 3,000 originales el mes cerraba en −1,310 y esa diferencia se pagaba con la misma tarjeta.
Cero no es holgura: es no tener margen para nada imprevisto.

**43% de los ingresos se va en servicio de deuda** (2,890 de 6,700). La referencia de
sostenibilidad está debajo de 30%, pero es un pico de un solo mes: el préstamo de 1,200 muere
con este pago. Los gastos fijos están sanos en 39%.

**El número frágil de esta foto es la reserva de 1,200**, que es un supuesto mío y no un dato
tuyo. Si vivir te cuesta 1,600, el mes cierra en −400 y la cuota real era 1,290. Por eso
setiembre es el mes de medir.

## 2. Deuda

| Acreedor | Instrumento | Saldo | Pago agosto | TCEA |
|---|---|---:|---:|---:|
| Banco | Tarjeta de crédito | S/ 10,000 | 3,000 | ❓ por confirmar |
| Empleador | Adelanto de sueldo | ❓ por confirmar | 1,200 | 0% |
| Financiera/tienda | Cuotas cámara | ❓ por confirmar | 420 | **0%** |

La deuda total **no es 10,000**: es 10,000 más el saldo del adelanto más las cuotas que
falten de la cámara, ninguno de los dos registrado todavía.

### Orden de ataque

Tienes deuda a dos precios muy distintos y eso ordena todo:

1. **Tarjeta de crédito** — tasa sin confirmar, asumir alta. Aquí va cada sol excedente.
2. **Adelanto de sueldo** — 0%. Solo el descuento, nunca adelantar.
3. **Cuotas de la cámara** — 0%. Solo la cuota, nunca adelantar.

**Una deuda al 0% no se adelanta jamás mientras exista una cara.** Es el único
financiamiento gratis que tienes; adelantarlo es regalarlo y quedarte pagando 60% en otro
lado. Si alguna vez te sobra plata, va íntegra a la tarjeta.

### ⚠️ Verificar: posible doble conteo

Si la cámara se compró **en cuotas sin intereses con la misma tarjeta de crédito** (que es
como suele venderse en Perú), entonces su saldo pendiente **ya está dentro de los 10,000** y
el modelo lo está contando dos veces: una en la línea "Cámara -420" y otra dentro de la
deuda de la tarjeta.

Eso cambiaría dos cosas: el balance de agosto mejoraría en 420, y una parte de esos 10,000
estaría al 0% y no a la tasa de la tarjeta, con lo que los intereses proyectados están
sobreestimados. Vale confirmarlo en el estado de cuenta antes de seguir proyectando.

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

Costó **S/ 3,000 en cuotas sin intereses**, a 420/mes. Eso son **unas 7 cuotas** (3,000 ÷ 420
= 7.1), así que la línea **se termina sola** — falta saber cuántas ya pagaste para poner la
fecha. Cuando termine, son 420/mes que se liberan.

Dos cosas que corrige este dato:

**No es una deuda cara, es la más barata que tienes.** Al 0%, los 420 no son costo
financiero: son amortización de algo que ya compraste. En el orden de ataque va al final
(§2), y adelantarla sería un error.

**Y por lo tanto no es "la línea más discrecional" que llamé antes.** La plata ya está
comprometida, el financiamiento es gratis y el plazo se acaba pronto. La única pregunta que
queda viva es hacia adelante: **¿la cámara genera ingresos?** Si factura, es un activo
productivo. Si no, sigue siendo un costo hundido con fecha de vencimiento — no una fuga que
convenga cortar hoy.

**Sobre la valuación:** declaraste S/ 4,000 y costó S/ 3,000. Puede ser que valga más de lo
que pagaste, pero el equipo fotográfico usado normalmente se revende **por debajo** del
costo. Como reserva de emergencia conviene mirarla al costo o menos:

| Cámara valuada en | Total activos | Patrimonio neto |
|---:|---:|---:|
| S/ 4,000 (declarado) | S/ 7,740 | S/ -2,260 |
| S/ 3,000 (costo) | S/ 6,740 | S/ -3,260 |

Y en los dos casos falta restar el adelanto y las cuotas que queden — el neto real es peor.

---

## 6. Lo que falta para que el modelo sea real

Cuatro datos cambian materialmente el diagnóstico. En orden de impacto:

1. **Gastos variables del mes** — alimentación, transporte, servicios, celular. Es el
   hueco más grande y, tras cerrar el adelanto y la cámara, **el único que queda abierto de
   los grandes**: define si diciembre cierra con 3.3 meses de colchón o con 0.8.
2. **TCEA de la tarjeta** — está en el estado de cuenta. Define cuánto de los 3,000
   mensuales es pago real y cuánto es interés.
3. ~~**Saldo pendiente del adelanto**~~ — **cerrado:** fue único y quedó cancelado en agosto.
4. **Cuotas que faltan de la cámara** — 420/mes que en algún momento se liberan. Saber
   cuándo permite planificar.

A eso se suman dos del calendario (§3): el **monto real de la gratificación** (posiblemente
mayor que 6,500) y el **saldo exacto del CTS**. Y una del patrimonio (§5): **cuántas cuotas faltan
de la cámara** (de ~7 totales), que fija cuándo se liberan los 420. La verificación del doble
conteo quedó **cerrada en negativo**: la cámara se compró directo a un amigo y no pasa por la
tarjeta.

Mientras esos datos no estén, los números de este documento son un piso, no un retrato.

---

## 7. Supuestos vigentes

Se registran para poder corregirlos, no porque estén verificados:

- **Moneda:** soles (S/).
- ~~**"Adelanto -1,200"** se interpreta como descuento en planilla~~ → **CONFIRMADO
  (2026-08-22):** adelanto único de 1,200, repagado íntegro en agosto. No se repite. Desde
  setiembre libera 1,200/mes de ingreso disponible.
- **"Cochera +200"** se interpreta como ingreso por alquiler de una cochera propia.
- ~~**"Cámara -420"** se interpreta como cuota mensual de un financiamiento~~ → **CONFIRMADO
  (2026-08-22):** Fujifilm X-T30 III comprada directo a un amigo por S/ 3,000 sin intereses,
  en cuotas de 420. **No pasa por la tarjeta**, así que no hay doble conteo.
- **"IA -240"** se interpreta como suscripciones mensuales de herramientas.
- **El saldo TC de 10,000** se asume anterior al pago de agosto. El saldo de cierre
  proyectado pasa a **S/ 8,709** con la cuota corregida de 1,690 y cero consumo nuevo.
- **El pago mínimo de 2,500 se toma como dato duro** del estado de cuenta. Queda por confirmar
  si es un mínimo revolvente o incluye cuotas de compras en cuotas (ver §del martes).
- **La reserva de vida de S/ 1,200/mes es un supuesto**, no un dato medido. Es el número que
  hay que confirmar en setiembre; todo el plan se recalibra con él.
- **El sueldo entra el martes 25/08** y cubre hasta el siguiente pago (≈25/09), así que la
  reserva de vida es de un mes completo, no de los días que restan de agosto.
- **Tipo de cambio S/ 3.75 por USD**, asumido. Los US$ 600 valen S/ 2,250 a esa tasa; el
  tipo de cambio real del día está en el BCRP y se pasa con `--tc`.
- **Los S/ 790 de Pokémon TCG** son valuación de mercado, no precio de venta. Los
  coleccionables se venden con descuento y con demora: como reserva de emergencia, no cuentan.
- **La cámara vale S/ 4,000** según lo declarado, contra un costo de S/ 3,000 en cuotas sin
  intereses. Los equipos usados se revenden por debajo del costo, así que los 4,000 son un
  techo optimista para efectos de liquidez.
- **La cámara son ~7 cuotas de 420** (3,000 ÷ 420 = 7.1), asumiendo que los 420 cubren solo
  la cámara y no incluyen accesorios u otros cargos.
- **Los US$ 300 en ETFs y los US$ 300 en S&P** se tratan como dos posiciones separadas
  (US$ 600 en total), según cómo fueron reportados.

---

## 8. Bitácora

Una entrada por mes, al cerrar. Formato: qué pasó, qué cambió respecto al mes anterior,
qué decisión se tomó.

### 2026-08 (h) — El mínimo de la tarjeta es 2,500

Dato nuevo: el pago mínimo de agosto es S/ 2,500, no elegible. Con eso la cuota deja de ser la
variable de ajuste y agosto queda con **S/ 390 para vivir un mes: un hueco de S/ 810**.

Evaluadas tres salidas por su efecto neto a diciembre (contando el activo consumido, no solo
la caja): pausar la IA un mes + 570 de Caja Arequipa (9,657) > Caja Arequipa 700 + recortar 110
(9,527) > cargar los 810 a la tarjeta (9,285). Cargar a la tarjeta es la peor por 242: los 810
se quedan cuatro meses en el saldo, no uno, y pierden el periodo de gracia.

Decidido: pagar el mínimo, cubrir el hueco con ahorros (y con la pausa de IA si es viable), y
**reponer los 700 en setiembre antes de subir la cuota** — cuesta S/ 82 en total y devuelve el
colchón cuatro meses antes.

Se abre una verificación con potencial de buena noticia: un mínimo de 25% del saldo es alto
para un revolvente, y probablemente incluya cuotas de compras en cuotas. Si parte de los 10,000
está en cuotas sin intereses, la tasa efectiva es menor que el 60% supuesto.

`finanzas.py` gana la categoría reservada `ahorro`: un retiro de ahorros financia el mes pero
no es ingreso, y si entra al denominador los ratios mienten — un mes malo se ve sano por haber
vaciado la cuenta.

### 2026-08 (g) — Plan del día de pago

El sueldo de agosto entra el martes 25 y de ahí salen el préstamo (el adelanto de 1,200, ya
desembolsado y gastado) más todo lo listado al inicio. Reparto: entran 6,700, sale sí o sí
3,810, se apartan 1,200 para vivir, y **quedan 1,690 para la tarjeta — no 3,000**.

Verificado que las dos rutas dan el mismo saldo al 31/08 (S/ 8,709): pagar 3,000 y vivir con
la tarjeta, o pagar 1,690 y vivir en efectivo. La segunda es estrictamente mejor porque el
consumo nuevo sobre saldo vigente pierde el periodo de gracia.

Nuevo comando `reparto`: dado el mes y la reserva de vida, imprime el orden de asignación del
sueldo y avisa cuando la cuota registrada excede lo que aguanta el mes.

### 2026-08 (f) — Se cierran el adelanto y la cámara

Confirmado: el adelanto fue **uno solo** de 1,200, repagado íntegro en agosto — no se repite.
Y la cámara es una **Fujifilm X-T30 III comprada directo a un amigo** por 3,000 sin intereses,
así que **no pasa por la tarjeta y no hay doble conteo** (esa verificación se cierra en
negativo: no había los +2,234 que podía haber).

Con eso el árbol de escenarios colapsa a la rama buena: desde setiembre se liberan 1,200/mes,
la capacidad sube a `4,090 − variable`, y llegar en verde a diciembre —tarjeta en cero, sin
rebotes, 3 meses de colchón— es alcanzable **sin tocar el CTS** con cualquier gasto variable
hasta 1,200. El umbral para que la tarjeta igual llegue a cero es 2,750/mes.

El consejo 2 se reemplaza: "matar el adelanto" ya está hecho, y pasa a ser **proteger los
1,200 liberados** — cuota de 2,890 el día de pago, antes de que el dinero se absorba.

`deuda.csv` gana una columna `estado` (vigente/cancelado) para que un pasivo saldado deje de
sumar en el patrimonio neto.

### 2026-08 (e) — Diagnóstico y plan a diciembre

Se corre el diagnóstico completo y se fija el plan. Llegar en verde a diciembre (tarjeta en
cero + sin rebotes + 3 meses de colchón) es alcanzable en casi toda la grilla de escenarios.

Tres palancas, en orden de impacto sobre la caja de diciembre: techo de 1,200 al gasto
variable (+6,499), matar el adelanto (+5,096) y destinar la gratificación al colchón (es
prácticamente toda la caja de diciembre). El CTS queda en reserva condicional: solo se activa
si en octubre el adelanto sigue y el gasto variable pasa de 1,800.

**Bug encontrado y corregido en `finanzas.py`:** `proyectar` derivaba el otro servicio de
deuda restando la cuota del total registrado, así que al proyectar con una cuota distinta de
la del mes base reasignaba en silencio la diferencia al adelanto. Con `--cuota 1290` el
adelanto pasaba a 2,910 y la proyección quedaba inservible. Ahora se lee del dato: la cuota
de la tarjeta se identifica por la categoría reservada `tarjeta_credito`. Los barridos de
escenarios de esta entrada se rehicieron sobre el modelo corregido.

### 2026-08 (d) — La cámara es deuda al 0%

Dato nuevo: la cámara costó S/ 3,000 en cuotas **sin intereses**, no 4,000. Eso la convierte
en la deuda más barata del balance y define un orden de ataque explícito: tarjeta primero,
0% al final y nunca adelantado.

Corrige la lectura anterior de la cámara como "la línea más discrecional": al 0% y con ~7
cuotas totales, es un costo hundido con fecha de vencimiento, no una fuga. Se libera 420/mes
cuando termine — falta saber cuántas cuotas van.

Se abre una verificación: si la compra se hizo en cuotas con la misma tarjeta, su saldo ya
está dentro de los 10,000 y el modelo lo cuenta dos veces.

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
