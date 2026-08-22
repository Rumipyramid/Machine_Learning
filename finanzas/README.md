# finanzas/ — Seguimiento de finanzas personales

Sistema mínimo para llevar las finanzas mes a mes: datos en CSV, cálculos en un script
sin dependencias, e interpretación en un documento vivo.

| Archivo | Qué es |
|---|---|
| `estado.md` | **Documento principal.** Foto vigente, deuda, supuestos y bitácora mensual |
| `movimientos/AAAA-MM.csv` | Movimientos del mes — fuente de verdad de los montos |
| `deuda.csv` | Saldos por acreedor, mes a mes, con su tasa y su estado (vigente/cancelado) |
| `calendario.csv` | Ingresos/egresos irregulares ya conocidos (CTS, gratificación, bonos) |
| `patrimonio.csv` | Activos, con su liquidez y qué tan confiable es la valuación |
| `finanzas.py` | Calculadora (solo stdlib) |

## Uso

```bash
cd finanzas

# Cómo cierra el mes
python finanzas.py resumen --mes 2026-08

# Cuánto cuesta la deuda a distintas tasas
python finanzas.py deuda --saldo 10000 --cuota 3000 --tcea 0 40 60 90

# ...y si el déficit se sigue cargando a la tarjeta
python finanzas.py deuda --saldo 10000 --cuota 3000 --tcea 60 --consumo-nuevo 1610

# Activos, pasivos, patrimonio neto y tasa valla
python finanzas.py patrimonio --tcea 60 --colchon 700

# Qué pasa si este mes se repite (aplica calendario.csv en su mes)
python finanzas.py proyeccion --mes 2026-08 --saldo 10000 --cuota 3000 --tcea 60 --meses 8 \
    --variables 1500 --otros-deuda-hasta 2026-08
```

Flags útiles de `proyeccion`:

- `--variables N` — gasto variable mensual asumido, para tapar el hueco del presupuesto y ver
  el escenario honesto. Correr con varios valores es la mejor forma de ver qué está en juego.
- `--otros-deuda-hasta AAAA-MM` — último mes en que se paga el servicio de deuda que no es la
  cuota de la tarjeta (p. ej. un adelanto de sueldo). Sin esto, se asume que se repite siempre.
- `--extraordinario deuda|caja` — si el CTS y la gratificación se aplican a la deuda o quedan
  en caja. Comparar ambos es cómo se decide qué hacer con ellos.

`patrimonio` acepta `--tc` (tipo de cambio USD→PEN, default 3.75 — verificar en BCRP),
`--tcea` y `--colchon` (monto líquido que se reserva como fondo de emergencia antes de
calcular cuánto es aplicable a la deuda).

Los demás comandos aceptan `--json` para uso programático.

## Formato de los CSV

`calendario.csv` usa las mismas columnas que los movimientos, pero sus filas son eventos de un
mes futuro concreto: no se repiten y solo los lee `proyeccion`.

`patrimonio.csv` clasifica cada activo por `liquidez` (`inmediata` · `dias` · `baja`) y por
`confianza_valuacion` (`alta` · `media` · `baja`). Las dos columnas existen porque un activo
ilíquido o mal valuado **no es colchón de emergencia**, por más que sume en el total.

### `movimientos/AAAA-MM.csv`

```csv
mes,concepto,categoria,tipo,monto,estado,nota
2026-08,Sueldo,trabajo,ingreso,6500,confirmado,Sueldo neto mensual
2026-08,Alquiler,vivienda,fijo,-1250,confirmado,
```

- **`monto` va firmado:** ingresos en positivo, egresos en negativo. El script valida
  que el archivo cuadre solo.
- **`tipo`** ∈ `ingreso` · `fijo` · `variable` · `deuda`. Es lo que separa "vivir" de
  "pagar deuda", que es la distinción que manda todo el análisis.
- **`estado`** ∈ `confirmado` · `estimado`. Los estimados se marcan con `~` en el
  resumen para no confundir un dato con una suposición.
- **`categoria`** tiene un valor **reservado: `tarjeta_credito`**, que marca cuál de los pagos
  de deuda es la cuota de la tarjeta. Sin esa marca, `proyeccion` no puede separar lo que
  amortiza la tarjeta de lo que no (adelantos, cuotas sin intereses) y proyectar con una cuota
  distinta a la registrada da resultados falsos. El script avisa si falta.
- El resto de `categoria` es libre, pero el script vigila cuatro categorías base —
  `alimentacion`, `transporte`, `servicios`, `comunicaciones`— y avisa si el mes no
  tiene ninguna. Un mes sin comida registrada no está completo, está incompleto.

## Convenciones

1. **Un CSV por mes.** No se editan meses cerrados: si aparece un dato nuevo de un mes
   pasado, se agrega como fila con su `nota` explicando de dónde salió.
2. **Lo irregular va al calendario, no a la estructura.** CTS, gratificaciones y bonos son
   eventos de un mes, no parte del mes tipo. Meterlos en un CSV mensual infla el promedio y
   hace creer que hay holgura donde no la hay.
3. **Los supuestos se escriben.** Todo lo que se interpretó (y no se verificó) va al §4
   de `estado.md`. Un supuesto escrito se puede corregir; uno implícito, no.
4. **El runway manda sobre el patrimonio neto.** Un patrimonio positivo con dos días de
   liquidez es más frágil que uno negativo con tres meses de reserva. El número que se mira
   primero es cuántos días de gasto fijo cubre lo líquido.
5. **El script manda sobre el documento.** Si un número de `estado.md` no sale de correr
   `finanzas.py`, es un supuesto y va marcado como tal.
6. **Nada de datos de identificación bancaria** en este directorio: ni números de tarjeta,
   ni cuentas, ni credenciales. Solo montos y saldos.
