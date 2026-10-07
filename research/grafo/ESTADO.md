# 🕸️ Grafo del segundo cerebro — ESTADO

*Generado: 2026-10-07 por `research/grafo/build_grafo.py` (determinista, sin LLM). No editar a mano: se regenera. Definiciones: `METRICAS.md`.*

> **Transparencia:** cada cifra de este reporte sale de contar archivos del repo. Lo que no se puede medir está listado en §7. Un número alto aquí significa *más material y mejor enlazado*, **no** que el conocimiento sea *verdadero* ni que haya tenido impacto fuera del repo.

## 1. Estado actual (qué hay)

| Capa | Cantidad | Detalle |
|---|---|---|
| Nodes (`_nodes/`) | 17 | 7,274 líneas |
| Outputs (`_outputs/`) | 5 | derivan de nodes: 5 de 5 citan algún node |
| Fuentes en el ledger | 588 | 🟢A 163 · 🔵B 110 · 🟡C 126 · 🟠D 145 · 🔴E 29 · otras/sin clasificar 15 |
| Aristas wikilink (node→node) | 90 | recíprocas: 90 de 90 (100%) |
| Fuentes citadas por ≥1 node | 481 de 588 | 82% del ledger; **107 viven solo en el ledger** |
| Fuentes citadas por ≥2 nodes (transversales) | 74 | evidencia reutilizada entre temas |
| **Grafo semántico** (relaciones extraídas) | 155 de 588 fuentes (26%) | 256 relaciones · 17 barridos · detalle en `relaciones/RELACIONES.md` |
| Componentes conexas del grafo de nodes | 1 | grafo conexo |

## 2. Segundo cerebro de DISEÑO (`tendencias-diseno-innovacion`)

| Indicador | Valor | Cómo leerlo |
|---|---|---|
| Iteraciones de bitácora | 5 (2026-07-26, 2026-07-29, 2026-08-02, 2026-10-02) | cuántas veces se confrontó el node |
| Tamaño | 1,948 líneas | crecimiento ≠ calidad; ver trazabilidad |
| Fuentes citadas explícitamente | 259 | F-n individuales dentro del node |
| …de rigor A/B | 134 (52%) | solidez de la base |
| Hipótesis vivas | 34: abierta 17 · parcial 13 · respaldada 2 · refutada 1 | tablero §6 |
| **Falsabilidad ejercida** | 50% (17/34) | hipótesis que ya se movieron de `abierta` |
| **Tasa de autocorrección** | 6% (1/17) | de las resueltas, cuántas se refutaron: 0% sostenido sería señal de confirmación sesgada |
| Reglas de criterio | 22 | §7 |
| **Trazabilidad de reglas** | 100% (22/22) | reglas con ≥1 F-n en su propio párrafo |
| Escala de madurez §5 | 🟢 16 · 🟡 10 · 🔴 15 · ⚔️ 4 | dónde está el peso de la evidencia |
| **Huérfanos de cita** | 8 de 181 (4%) | fuentes en los rangos de diseño/innovación (CLAUDE.md) registradas pero **sin cita individual** en el node (pueden estar en un rango 'F-a a F-b' o en otro node) |
| …de ellos citados en otro node | 0 | no están perdidos, solo fuera del node de diseño |

**Vecinos por evidencia compartida** (candidatos a conexión; ✅ = ya enlazado por wikilink):

| Node | F-n compartidas | Jaccard | Enlazado |
|---|---|---|---|
| `conducta-humano-ia` | 24 | 0.089 | ✅ |
| `proyecto-back-to-basics-ffvv-vida` | 19 | 0.07 | ✅ |
| `evaluacion-calidad-agentes-conversacionales-ia` | 8 | 0.03 | ✅ |
| `material-visual-venta-consultiva` | 8 | 0.03 | ✅ |
| `mecanismos-seguros-salud` | 7 | 0.023 | ✅ |
| `behavioral-design-estado-disciplina` | 6 | 0.023 | ✅ |
| `glosario-seguro-vida-peru` | 4 | 0.015 | ❌ sin enlace |
| `transicion-venta-fria-a-opt-in` | 4 | 0.015 | ❌ sin enlace |
| `glosario-seguro-salud-peru` | 3 | 0.011 | ❌ sin enlace |
| `modelo-salud-ia-farmacias-peru` | 2 | 0.007 | ❌ sin enlace |
| `seguros-comportamiento-mundo-peru` | 2 | 0.007 | ✅ |
| `fenomeno-el-nino-impacto-personas` | 0 | 0.0 | ❌ sin enlace |
| `futuro-asesores-seguros-venta-digital` | 0 | 0.0 | ❌ sin enlace |
| `matriz-productos-vida-rimac` | 0 | 0.0 | ❌ sin enlace |
| `modelo-personas-sinteticas` | 0 | 0.0 | ✅ |
| `venta-vida-digital-hibrida-latam` | 0 | 0.0 | ❌ sin enlace |

## 3. Evolución

### 3.1 Enriquecimiento del ledger por fecha de registro (reconstruido, cubre desde el origen)

*Fuente: columna `fecha` del ledger. Es la fecha en que `cronista` registró cada F-n, no la fecha del estudio.*

| Fecha | Nuevas | Acumuladas | de ellas A/B | Barra |
|---|---|---|---|---|
| 2026-06-22 | 5 | 5 | 3 | █ |
| 2026-06-25 | 10 | 15 | 6 | ██ |
| 2026-07-06 | 62 | 77 | 32 | ████████████████ |
| 2026-07-10 | 41 | 118 | 25 | ██████████ |
| 2026-07-12 | 12 | 130 | 8 | ███ |
| 2026-07-13 | 9 | 139 | 7 | ██ |
| 2026-07-14 | 19 | 158 | 7 | █████ |
| 2026-07-15 | 13 | 171 | 9 | ███ |
| 2026-07-21 | 8 | 179 | 5 | ██ |
| 2026-07-22 | 28 | 207 | 8 | ███████ |
| 2026-07-23 | 12 | 219 | 3 | ███ |
| 2026-07-24 | 16 | 235 | 11 | ████ |
| 2026-07-25 | 1 | 236 | 1 | █ |
| 2026-07-26 | 92 | 328 | 30 | ███████████████████████ |
| 2026-07-27 | 51 | 379 | 24 | █████████████ |
| 2026-07-29 | 19 | 398 | 7 | █████ |
| 2026-08-02 | 70 | 468 | 24 | ██████████████████ |
| 2026-10-02 | 47 | 515 | 20 | ████████████ |
| 2026-10-03 | 13 | 528 | 10 | ███ |
| 2026-10-07 | 60 | 588 | 33 | ███████████████ |

### 3.2 Instantáneas por git (estado completo del grafo en cada día con commits)

*Fuente: `git show` de cada commit. **El clon es superficial (shallow)**: el historial verificable empieza en 2026-08-20; antes de eso solo vale §3.1.*

| Fecha | Commit | Fuentes | Nodes | Outputs | Wikilinks | Fuentes citadas | Diseño: líneas | H abiertas | H resueltas | Reglas |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-08-20 | `e8ba645` | 468 | 15 | 4 | 69 | 352 | 1800 | 19 | 12 | 22 |
| 2026-10-02 | `e32e8e5` | 515 | 16 | 4 | 84 | 404 | 1898 | 19 | 14 | 22 |
| 2026-10-03 | `0781a57` | 528 | 16 | 4 | 84 | 423 | 1948 | 17 | 17 | 22 |
| 2026-10-07 | `b4a8375` | 588 | 17 | 5 | 90 | 481 | 1948 | 17 | 17 | 22 |

*(Se omiten los días sin cambio en estas columnas.)*

## 4. Métricas de impacto (definidas en `METRICAS.md`)

| Métrica | Valor | Qué dice | Qué NO dice |
|---|---|---|---|
| M1 Base sólida (A+B / ledger) | 46% | proporción de evidencia primaria/oficial | no que el hallazgo sea cierto |
| M2 Cobertura de citación | 82% | cuánto del ledger sostiene algún node | un node puede citar mal |
| M3 Reciprocidad de enlaces | 100% | cumplimiento de la regla 5 de `alma.md` | calidad del enlace |
| M4 Falsabilidad ejercida (diseño) | 50% | el node confronta, no solo acumula | que las pruebas fueran rigurosas |
| M5 Trazabilidad de reglas (diseño) | 100% | las reglas se apoyan en fuentes | que la fuente sea la correcta |
| M6 Integración (diseño↔resto) | 8/16 nodes enlazados; 11 comparten evidencia | el diseño informa a los demás temas | uso real por personas |
| M7 Lectura profunda (Lobo) | 184 fuentes leídas a fondo = 31% del ledger; 183 intuiciones | el cerebro se relee, no solo crece | que las intuiciones sean correctas |

## 5. Auditoría de integridad (fallas reales, sin maquillar)

- ✅ F-n citadas en un node pero **ausentes del ledger**: **0**
- ✅ Wikilinks **no recíprocos** (viola regla 5): **0**
- ✅ Wikilinks **rotos** (destino inexistente): **0**
- ✅ Nodes **aislados** (sin enlaces): **0**
- ✅ Nodes **ausentes** de la tabla de `alma.md`: **0**
- ✅ Nodes **más nuevos que su fecha en `alma.md`** (solo se juzga si el último commit es posterior al inicio del historial visible, 2026-08-20; antes es indeterminable): **0**
- ✅ Outputs que **no citan ningún node** (viola regla 4): **0**

## 6. Tabla por node

| Node | Líneas | F-n citadas | A/B | Enlaces ent./sal. | Última modif. visible (git) | alma |
|---|---|---|---|---|---|---|
| `tendencias-diseno-innovacion` | 1948 | 259 | 134 | 8/8 | 2026-10-03 | 2026-10-03 v4.1 |
| `fenomeno-el-nino-impacto-personas` | 404 | 58 | 32 | 3/3 | 2026-10-07 | 2026-10-07 v1.1 |
| `mecanismos-seguros-salud` | 351 | 53 | 33 | 8/8 | 2026-10-02 | 2026-10-02 v1.2 |
| `conducta-humano-ia` | 139 | 35 | 25 | 5/5 | 2026-10-02 | 2026-10-02 v1.1 |
| `proyecto-back-to-basics-ffvv-vida` | 932 | 33 | 29 | 7/7 | indeterminada (≤ 2026-08-20, historial truncado) | 2026-07-27 v1.4 |
| `futuro-asesores-seguros-venta-digital` | 386 | 23 | 2 | 6/6 | indeterminada (≤ 2026-08-20, historial truncado) | 2026-07-27 v1.0 |
| `modelo-salud-ia-farmacias-peru` | 608 | 21 | 18 | 4/4 | 2026-10-07 | 2026-10-07 v1.0 |
| `transicion-venta-fria-a-opt-in` | 324 | 18 | 7 | 4/4 | 2026-10-02 | 2026-10-02 v1.0 |
| `material-visual-venta-consultiva` | 369 | 17 | 12 | 7/7 | 2026-10-02 | 2026-10-02 v1.1 |
| `seguros-comportamiento-mundo-peru` | 336 | 15 | 5 | 13/13 | 2026-10-07 | 2026-10-07 v1.1 |
| `evaluacion-calidad-agentes-conversacionales-ia` | 254 | 14 | 10 | 3/3 | 2026-10-02 | 2026-10-02 v1.0 |
| `behavioral-design-estado-disciplina` | 318 | 8 | 7 | 7/7 | 2026-10-02 | 2026-10-02 v1.1 |
| `glosario-seguro-vida-peru` | 216 | 8 | 4 | 3/3 | indeterminada (≤ 2026-08-20, historial truncado) | 2026-07-24 v1.0 |
| `venta-vida-digital-hibrida-latam` | 233 | 8 | 4 | 2/2 | indeterminada (≤ 2026-08-20, historial truncado) | 2026-07-27 v1.0 |
| `glosario-seguro-salud-peru` | 196 | 6 | 5 | 4/4 | indeterminada (≤ 2026-08-20, historial truncado) | 2026-07-21 v1.0 |
| `matriz-productos-vida-rimac` | 184 | 0 | 0 | 2/2 | indeterminada (≤ 2026-08-20, historial truncado) | 2026-07-26 v1.2 |
| `modelo-personas-sinteticas` | 76 | 0 | 0 | 4/4 | 2026-10-07 | 2026-10-07 v1.0 |

## 7. Límites declarados de esta medición

- **Historial git truncado:** el clon es superficial; las instantáneas (§3.2) empiezan en la fecha indicada. §3.1 reconstruye el ledger desde su columna `fecha`, que puede ser corregida a mano y no prueba *cuándo* se leyó la fuente.
- **Citar no es validar:** M2/M5 cuentan referencias `F-n`, no si la cita respalda la afirmación (eso lo audita el chequeo de eco de cita del propio node, no este script).
- **Rangos 'F-a a F-b' no se expanden:** si un node cita un rango, esas fuentes cuentan como huérfanas aquí. Es deliberado: un rango no es trazabilidad por afirmación.
- **Rigor A–E es el del ledger** (juicio de `cronista`), no re-evaluado aquí.
- **Hipótesis y reglas se leen por formato** (`| **Hn** |`, `- **Cn —`). Si el node cambia de formato, las métricas de diseño caerán a 0: tomarlo como alarma de parser, no como pérdida de conocimiento.
- **Sin métricas de uso externo:** no hay datos de quién lee, reutiliza ni decide con este cerebro. Impacto real = pendiente; lo único medible hoy es estructura, trazabilidad y autocorrección.
- **Wikilinks se cuentan en todo el texto del node**, no solo en `## Conexiones`.

---
*Visor interactivo: `research/grafo/grafo.html` · grafo crudo: `grafo.json` · serie: `historial.jsonl`.*
