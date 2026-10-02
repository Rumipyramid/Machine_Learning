# 🕸️ Grafo del segundo cerebro — ESTADO

*Generado: 2026-10-02 por `research/grafo/build_grafo.py` (determinista, sin LLM). No editar a mano: se regenera. Definiciones: `METRICAS.md`.*

> **Transparencia:** cada cifra de este reporte sale de contar archivos del repo. Lo que no se puede medir está listado en §7. Un número alto aquí significa *más material y mejor enlazado*, **no** que el conocimiento sea *verdadero* ni que haya tenido impacto fuera del repo.

## 1. Estado actual (qué hay)

| Capa | Cantidad | Detalle |
|---|---|---|
| Nodes (`_nodes/`) | 15 | 6,582 líneas |
| Outputs (`_outputs/`) | 4 | derivan de nodes: 4 de 4 citan algún node |
| Fuentes en el ledger | 476 | 🟢A 134 · 🔵B 78 · 🟡C 104 · 🟠D 118 · 🔴E 29 · otras/sin clasificar 13 |
| Aristas wikilink (node→node) | 74 | recíprocas: 74 de 74 (100%) |
| Fuentes citadas por ≥1 node | 360 de 476 | 76% del ledger; **116 viven solo en el ledger** |
| Fuentes citadas por ≥2 nodes (transversales) | 15 | evidencia reutilizada entre temas |
| **Grafo semántico** (relaciones extraídas) | 21 de 476 fuentes (4%) | 71 relaciones · 4 barridos · detalle en `relaciones/RELACIONES.md` |
| Componentes conexas del grafo de nodes | 1 | grafo conexo |

## 2. Segundo cerebro de DISEÑO (`tendencias-diseno-innovacion`)

| Indicador | Valor | Cómo leerlo |
|---|---|---|
| Iteraciones de bitácora | 5 (2026-07-26, 2026-07-29, 2026-08-02, 2026-10-02) | cuántas veces se confrontó el node |
| Tamaño | 1,842 líneas | crecimiento ≠ calidad; ver trazabilidad |
| Fuentes citadas explícitamente | 175 | F-n individuales dentro del node |
| …de rigor A/B | 57 (33%) | solidez de la base |
| Hipótesis vivas | 33: abierta 20 · parcial 7 · respaldada 4 · refutada 1 | tablero §6 |
| **Falsabilidad ejercida** | 39% (13/33) | hipótesis que ya se movieron de `abierta` |
| **Tasa de autocorrección** | 8% (1/13) | de las resueltas, cuántas se refutaron: 0% sostenido sería señal de confirmación sesgada |
| Reglas de criterio | 22 | §7 |
| **Trazabilidad de reglas** | 23% (5/22) | reglas con ≥1 F-n en su propio párrafo |
| Escala de madurez §5 | 🟢 16 · 🟡 10 · 🔴 15 · ⚔️ 4 | dónde está el peso de la evidencia |
| **Huérfanos de cita** | 14 de 181 (8%) | fuentes en los rangos de diseño/innovación (CLAUDE.md) registradas pero **sin cita individual** en el node (pueden estar en un rango 'F-a a F-b' o en otro node) |
| …de ellos citados en otro node | 0 | no están perdidos, solo fuera del node de diseño |

**Vecinos por evidencia compartida** (candidatos a conexión; ✅ = ya enlazado por wikilink):

| Node | F-n compartidas | Jaccard | Enlazado |
|---|---|---|---|
| `mecanismos-seguros-salud` | 2 | 0.009 | ✅ |
| `behavioral-design-estado-disciplina` | 0 | 0.0 | ✅ |
| `evaluacion-calidad-agentes-conversacionales-ia` | 0 | 0.0 | ✅ |
| `futuro-asesores-seguros-venta-digital` | 0 | 0.0 | ❌ sin enlace |
| `glosario-seguro-salud-peru` | 0 | 0.0 | ❌ sin enlace |
| `glosario-seguro-vida-peru` | 0 | 0.0 | ❌ sin enlace |
| `material-visual-venta-consultiva` | 0 | 0.0 | ✅ |
| `matriz-productos-vida-rimac` | 0 | 0.0 | ❌ sin enlace |
| `modelo-personas-sinteticas` | 0 | 0.0 | ✅ |
| `modelo-salud-ia-farmacias-peru` | 0 | 0.0 | ❌ sin enlace |
| `proyecto-back-to-basics-ffvv-vida` | 0 | 0.0 | ✅ |
| `seguros-comportamiento-mundo-peru` | 0 | 0.0 | ✅ |
| `transicion-venta-fria-a-opt-in` | 0 | 0.0 | ❌ sin enlace |
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
| 2026-10-02 | 8 | 476 | 2 | ██ |

### 3.2 Instantáneas por git (estado completo del grafo en cada día con commits)

*Fuente: `git show` de cada commit. **El clon es superficial (shallow)**: el historial verificable empieza en 2026-08-13; antes de eso solo vale §3.1.*

| Fecha | Commit | Fuentes | Nodes | Outputs | Wikilinks | Fuentes citadas | Diseño: líneas | H abiertas | H resueltas | Reglas |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-08-13 | `8a90dc2` | 468 | 15 | 4 | 69 | 352 | 1800 | 19 | 12 | 22 |

*(Se omiten los días sin cambio en estas columnas.)*

## 4. Métricas de impacto (definidas en `METRICAS.md`)

| Métrica | Valor | Qué dice | Qué NO dice |
|---|---|---|---|
| M1 Base sólida (A+B / ledger) | 45% | proporción de evidencia primaria/oficial | no que el hallazgo sea cierto |
| M2 Cobertura de citación | 76% | cuánto del ledger sostiene algún node | un node puede citar mal |
| M3 Reciprocidad de enlaces | 100% | cumplimiento de la regla 5 de `alma.md` | calidad del enlace |
| M4 Falsabilidad ejercida (diseño) | 39% | el node confronta, no solo acumula | que las pruebas fueran rigurosas |
| M5 Trazabilidad de reglas (diseño) | 23% | las reglas se apoyan en fuentes | que la fuente sea la correcta |
| M6 Integración (diseño↔resto) | 7/14 nodes enlazados; 1 comparten evidencia | el diseño informa a los demás temas | uso real por personas |
| M7 Lectura profunda (Lobo) | 169 fuentes leídas a fondo = 36% del ledger; 168 intuiciones | el cerebro se relee, no solo crece | que las intuiciones sean correctas |

## 5. Auditoría de integridad (fallas reales, sin maquillar)

- ✅ F-n citadas en un node pero **ausentes del ledger**: **0**
- ✅ Wikilinks **no recíprocos** (viola regla 5): **0**
- ✅ Wikilinks **rotos** (destino inexistente): **0**
- ✅ Nodes **aislados** (sin enlaces): **0**
- ✅ Nodes **ausentes** de la tabla de `alma.md`: **0**
- ✅ Nodes **más nuevos que su fecha en `alma.md`** (solo se juzga si el último commit es posterior al inicio del historial visible, 2026-08-13; antes es indeterminable): **0**
- ✅ Outputs que **no citan ningún node** (viola regla 4): **0**

## 6. Tabla por node

| Node | Líneas | F-n citadas | A/B | Enlaces ent./sal. | Última modif. visible (git) | alma |
|---|---|---|---|---|---|---|
| `tendencias-diseno-innovacion` | 1842 | 175 | 57 | 7/7 | 2026-10-02 | 2026-10-02 v4.1 |
| `mecanismos-seguros-salud` | 332 | 45 | 27 | 7/7 | 2026-10-02 | 2026-10-02 v1.2 |
| `proyecto-back-to-basics-ffvv-vida` | 932 | 33 | 29 | 7/7 | indeterminada (≤ 2026-08-13, historial truncado) | 2026-07-27 v1.4 |
| `futuro-asesores-seguros-venta-digital` | 386 | 23 | 2 | 6/6 | indeterminada (≤ 2026-08-13, historial truncado) | 2026-07-27 v1.0 |
| `modelo-salud-ia-farmacias-peru` | 605 | 21 | 18 | 3/3 | indeterminada (≤ 2026-08-13, historial truncado) | 2026-08-12 v1.0 |
| `transicion-venta-fria-a-opt-in` | 324 | 18 | 7 | 4/4 | 2026-10-02 | 2026-10-02 v1.0 |
| `material-visual-venta-consultiva` | 369 | 17 | 12 | 7/7 | 2026-10-02 | 2026-10-02 v1.1 |
| `evaluacion-calidad-agentes-conversacionales-ia` | 253 | 13 | 9 | 2/2 | indeterminada (≤ 2026-08-13, historial truncado) | 2026-07-15 v1.0 |
| `behavioral-design-estado-disciplina` | 317 | 8 | 7 | 6/6 | indeterminada (≤ 2026-08-13, historial truncado) | 2026-07-29 v1.1 |
| `glosario-seguro-vida-peru` | 216 | 8 | 4 | 3/3 | indeterminada (≤ 2026-08-13, historial truncado) | 2026-07-24 v1.0 |
| `venta-vida-digital-hibrida-latam` | 233 | 8 | 4 | 2/2 | indeterminada (≤ 2026-08-13, historial truncado) | 2026-07-27 v1.0 |
| `glosario-seguro-salud-peru` | 196 | 6 | 5 | 4/4 | indeterminada (≤ 2026-08-13, historial truncado) | 2026-07-21 v1.0 |
| `seguros-comportamiento-mundo-peru` | 320 | 3 | 1 | 11/11 | 2026-10-02 | 2026-10-02 v1.1 |
| `matriz-productos-vida-rimac` | 184 | 0 | 0 | 2/2 | indeterminada (≤ 2026-08-13, historial truncado) | 2026-07-26 v1.2 |
| `modelo-personas-sinteticas` | 73 | 0 | 0 | 3/3 | indeterminada (≤ 2026-08-13, historial truncado) | 2026-07-20 v1.0 |

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
