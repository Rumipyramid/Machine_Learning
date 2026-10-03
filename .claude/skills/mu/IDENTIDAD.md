# MU — identidad visual

Fuente de verdad del estilo de **todo lo que sea de Mu**: el panel (`research/grafo/mu.html`), guías, one-pagers,
láminas, decks o cualquier pieza que se pida "de Mu". Se fijó el 2026-10-03 a pedido del usuario, tomando como
base el panel brutalista generado por `research/grafo/mu.py`. Si una pieza de Mu no sigue esto, está mal.

**Idea de marca:** un instrumento de medición, no un folleto. Mu muestra cifras crudas, dice lo que falla sin
suavizarlo y deja ver la estructura. La estética es **brutalista e industrial**: tinta, rejilla, bloques y un solo
color de alerta.

## 1. Color

Tres tintas y un acento. Nada de degradados, sombras ni transparencias decorativas.

| Token | Claro | Oscuro | Uso |
|---|---|---|---|
| `--bg` | `#fff` | `#000` | fondo |
| `--fg` | `#000` | `#fff` | tinta: texto, bordes, barras de sección |
| `--acc` | `#ff3b00` | `#ff5a26` | **solo** alerta, falla, lo que requiere acción, o el dato que hay que mirar primero |
| `--g2` | `#666` | `#999` | texto secundario, notas |
| `--g3` | `#bbb` | `#444` | rellenos neutros, estados inactivos, fondos de `code` |

- El naranja es escaso: si todo es naranja, nada lo es. Sobre naranja siempre va texto **negro** (`#000`), en
  ambos modos.
- Modo oscuro con `@media (prefers-color-scheme: dark)`, invirtiendo tinta y fondo.

## 2. Tipografía

| Rol | Fuente | Forma |
|---|---|---|
| Titular / marca | `Impact, 'Arial Black', sans-serif`, peso 900 | `MU` gigante (`clamp(56px,14vw,128px)`), interlineado .85, tracking −.04em |
| Barras de sección (`h2`) | Impact 900, 20px, tracking .04em | texto invertido (fondo tinta, letra fondo) |
| Cifra héroe | Impact 900, 44px (tarjeta) a 110px (nivel) | el número manda; la unidad va chica y gris (`N5<span>/7</span>`) |
| Cuerpo | `ui-monospace, Menlo, Consolas, monospace`, 14px/1.35 | todo lo demás es monoespaciado |
| Rótulos | mono 700, 12px, MAYÚSCULAS | etiquetas de tarjeta, `h3`, cabeceras de tabla |
| Notas | mono 11px, gris `--g2` | límites, fuentes, advertencias de método |

Sin fuentes web: solo fuentes del sistema (la pieza debe funcionar sin red).

## 3. Forma y retícula

- **Esquinas rectas siempre** (`border-radius: 0`).
- **Reglas gruesas:** 8px de tinta separan secciones y cierran la cabecera; 2px enmarcan tarjetas y celdas;
  4px enmarcan el bloque héroe.
- Las tarjetas se **tocan**: bordes de 2px solapados (`margin:-1px 0 0 -1px`) forman una rejilla continua, sin
  aire entre celdas.
- Rejilla fluida: `repeat(auto-fit, minmax(200px,1fr))` para tarjetas, `minmax(300px,1fr)` para bloques de texto.
  En pantallas de celular todo cae a una columna; nunca hay scroll horizontal.
- Márgenes laterales de 16px.

## 4. Señalética

| Señal | Forma | Significado |
|---|---|---|
| Numeración de sección | `00`, `01`, `02`… delante del título en la barra invertida | orden de lectura; el título lleva la pregunta: `00 INTELIGENCIA — ¿qué nivel tiene?` |
| `✓` / `✗` | en tablas y listas de criterios | cumple / no cumple |
| Lista de estado | barra izquierda de 8px: tinta = ok, naranja = falla, gris = neutro | estado de cada ítem sin depender del color solo (hay `✓`/`✗`) |
| Tarjeta en alerta | fondo naranja completo, texto negro | métrica que requiere atención |
| Bloque de nivel | `N5/7` + rótulo naranja invertido (`AUTOCORRECCIÓN`) + definición en una línea | dónde está Mu en su escalera |
| Barras SVG | rectángulos planos tinta / gris / naranja, sin ejes decorativos | magnitud, nunca ilustración |
| `code` | fondo gris `--g3` | comandos y rutas |
| Botón | bloque de tinta, Impact en mayúsculas, flecha `↗`; al pasar o enfocar se vuelve naranja | abre algo más (p. ej. `VER ARQUITECTURA ↗`) |
| Ventana emergente | `popover` nativo (sin JS), marco de 8px, barra de título invertida fija arriba, botón `CERRAR ✗` | detalle que no cabe en la página; ver `research/grafo/mu_guia.html` |
| Diagrama de capas | bloques apilados con número en columna de tinta, flechas de tinta con rótulo gris entre capas, la capa de auditoría con número en naranja | arquitectura o flujo; HTML, no imagen, para que se lea en el celular |

## 5. Voz

- Cifras crudas primero, interpretación después. Sin índices compuestos inventados.
- Las fallas se dicen sin suavizar; los límites del método van en nota gris al pie (*"citar ≠ validar; el uso
  externo no se mide"*).
- Rótulos en MAYÚSCULAS, frases cortas, español claro (regla del usuario del 2026-10-03: nada de jerga sin explicar).

## 6. Cómo aplicarlo

- HTML **autocontenido**: un solo archivo con el `<style>` dentro, sin JS salvo que la pieza lo necesite, sin
  recursos externos.
- Copiar la hoja base de `.claude/skills/mu/mu-base.css` (los mismos tokens y clases del panel) al `<style>` de la
  pieza nueva y construir encima.
- Estructura mínima: `header` con `MU` gigante + línea de contexto en mayúsculas → secciones numeradas con barra
  invertida → `footer` con fecha, fuente de los datos y límites.
- Si el pedido es otro formato (PDF, deck, lámina), se trasladan los mismos tokens: fondo blanco o negro, tinta,
  un acento naranja, Impact + monoespaciada, esquinas rectas, reglas gruesas.
