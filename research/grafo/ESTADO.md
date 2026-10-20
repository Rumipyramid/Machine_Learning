# 🕸️ Grafo del segundo cerebro — ESTADO

*Generado: 2026-10-20 por `research/grafo/build_grafo.py` (determinista, sin LLM). No editar a mano: se regenera. Definiciones: `METRICAS.md`.*

> **Transparencia:** cada cifra de este reporte sale de contar archivos del repo. Lo que no se puede medir está listado en §7. Un número alto aquí significa *más material y mejor enlazado*, **no** que el conocimiento sea *verdadero* ni que haya tenido impacto fuera del repo.

## 1. Estado actual (qué hay)

| Capa | Cantidad | Detalle |
|---|---|---|
| Nodes (`_nodes/`) | 21 | 8,722 líneas |
| Outputs (`_outputs/`) | 5 | derivan de nodes: 5 de 5 citan algún node |
| Fuentes en el ledger | 891 | 🟢A 311 · 🔵B 136 · 🟡C 203 · 🟠D 189 · 🔴E 37 · otras/sin clasificar 15 |
| Aristas wikilink (node→node) | 140 | recíprocas: 140 de 140 (100%) |
| Fuentes citadas por ≥1 node | 785 de 891 | 88% del ledger; **106 viven solo en el ledger** |
| Fuentes citadas por ≥2 nodes (transversales) | 104 | evidencia reutilizada entre temas |
| **Grafo semántico** (relaciones extraídas) | 479 de 891 fuentes (54%) | 797 relaciones · 61 barridos · detalle en `relaciones/RELACIONES.md` |
| Componentes conexas del grafo de nodes | 1 | grafo conexo |

## 2. Segundo cerebro de DISEÑO (`tendencias-diseno-innovacion`)

| Indicador | Valor | Cómo leerlo |
|---|---|---|
| Iteraciones de bitácora | 5 (2026-07-26, 2026-07-29, 2026-08-02, 2026-10-02) | cuántas veces se confrontó el node |
| Tamaño | 2,002 líneas | crecimiento ≠ calidad; ver trazabilidad |
| Fuentes citadas explícitamente | 274 | F-n individuales dentro del node |
| …de rigor A/B | 140 (51%) | solidez de la base |
| Hipótesis vivas | 35: abierta 15 · parcial 14 · respaldada 2 · refutada 4 | tablero §6 |
| **Falsabilidad ejercida** | 57% (20/35) | hipótesis que ya se movieron de `abierta` |
| **Tasa de autocorrección** | 20% (4/20) | de las resueltas, cuántas se refutaron: 0% sostenido sería señal de confirmación sesgada |
| Reglas de criterio | 22 | §7 |
| **Trazabilidad de reglas** | 100% (22/22) | reglas con ≥1 F-n en su propio párrafo |
| Escala de madurez §5 | 🟢 16 · 🟡 10 · 🔴 15 · ⚔️ 4 | dónde está el peso de la evidencia |
| **Huérfanos de cita** | 8 de 181 (4%) | fuentes en los rangos de diseño/innovación (CLAUDE.md) registradas pero **sin cita individual** en el node (pueden estar en un rango 'F-a a F-b' o en otro node) |
| …de ellos citados en otro node | 0 | no están perdidos, solo fuera del node de diseño |

**Vecinos por evidencia compartida** (candidatos a conexión; ✅ = ya enlazado por wikilink):

| Node | F-n compartidas | Jaccard | Enlazado |
|---|---|---|---|
| `conducta-humano-ia` | 24 | 0.082 | ✅ |
| `proyecto-back-to-basics-ffvv-vida` | 19 | 0.066 | ✅ |
| `convergencia-psicologia-economia-ia` | 9 | 0.024 | ✅ |
| `fenomenos-psicologicos` | 9 | 0.024 | ✅ |
| `evaluacion-calidad-agentes-conversacionales-ia` | 8 | 0.028 | ✅ |
| `material-visual-venta-consultiva` | 8 | 0.028 | ✅ |
| `mecanismos-seguros-salud` | 7 | 0.022 | ✅ |
| `behavioral-design-estado-disciplina` | 6 | 0.022 | ✅ |
| `glosario-seguro-vida-peru` | 4 | 0.014 | ❌ sin enlace |
| `seguros-comportamiento-mundo-peru` | 4 | 0.014 | ✅ |
| `transicion-venta-fria-a-opt-in` | 4 | 0.014 | ❌ sin enlace |
| `glosario-seguro-salud-peru` | 3 | 0.011 | ❌ sin enlace |
| `modelo-salud-ia-farmacias-peru` | 2 | 0.007 | ❌ sin enlace |
| `riesgo-proteccion-seguros-sectores-populares-peru` | 1 | 0.003 | ❌ sin enlace |
| `fenomeno-el-nino-impacto-personas` | 0 | 0.0 | ❌ sin enlace |
| `futuro-asesores-seguros-venta-digital` | 0 | 0.0 | ❌ sin enlace |
| `lealtad-gamificacion-recompensas-retail` | 0 | 0.0 | ✅ |
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
| 2026-07-06 | 62 | 77 | 31 | ████████████████ |
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
| 2026-07-26 | 92 | 328 | 29 | ███████████████████████ |
| 2026-07-27 | 51 | 379 | 24 | █████████████ |
| 2026-07-29 | 19 | 398 | 7 | █████ |
| 2026-08-02 | 70 | 468 | 24 | ██████████████████ |
| 2026-10-02 | 47 | 515 | 20 | ████████████ |
| 2026-10-03 | 130 | 645 | 56 | ████████████████████████████████ |
| 2026-10-04 | 95 | 740 | 94 | ████████████████████████ |
| 2026-10-07 | 60 | 800 | 33 | ███████████████ |
| 2026-10-15 | 45 | 845 | 17 | ███████████ |
| 2026-10-20 | 46 | 891 | 19 | ████████████ |

### 3.2 Instantáneas por git (estado completo del grafo en cada día con commits)

*Fuente: `git show` de cada commit. **El clon es superficial (shallow)**: el historial verificable empieza en 2026-09-08; antes de eso solo vale §3.1.*

| Fecha | Commit | Fuentes | Nodes | Outputs | Wikilinks | Fuentes citadas | Diseño: líneas | H abiertas | H resueltas | Reglas |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-09-08 | `2937e16` | 468 | 15 | 4 | 69 | 352 | 1800 | 19 | 12 | 22 |
| 2026-10-02 | `e32e8e5` | 515 | 16 | 4 | 84 | 404 | 1898 | 19 | 14 | 22 |
| 2026-10-03 | `d80e14b` | 645 | 17 | 4 | 96 | 540 | 2000 | 15 | 20 | 22 |
| 2026-10-04 | `b635cd4` | 740 | 18 | 4 | 110 | 636 | 2001 | 15 | 20 | 22 |
| 2026-10-06 | `944e196` | 528 | 16 | 4 | 84 | 423 | 1948 | 17 | 17 | 22 |
| 2026-10-07 | `7d6f508` | 800 | 19 | 5 | 116 | 694 | 2001 | 15 | 20 | 22 |
| 2026-10-15 | `d2adac5` | 845 | 20 | 5 | 124 | 738 | 2002 | 15 | 20 | 22 |
| 2026-10-20 | `f3ff934` | 884 | 21 | 5 | 140 | 778 | 2002 | 15 | 20 | 22 |

*(Se omiten los días sin cambio en estas columnas.)*

## 4. Métricas de impacto (definidas en `METRICAS.md`)

| Métrica | Valor | Qué dice | Qué NO dice |
|---|---|---|---|
| M1 Base sólida (A+B / ledger) | 50% | proporción de evidencia primaria/oficial | no que el hallazgo sea cierto |
| M2 Cobertura de citación | 88% | cuánto del ledger sostiene algún node | un node puede citar mal |
| M3 Reciprocidad de enlaces | 100% | cumplimiento de la regla 5 de `alma.md` | calidad del enlace |
| M4 Falsabilidad ejercida (diseño) | 57% | el node confronta, no solo acumula | que las pruebas fueran rigurosas |
| M5 Trazabilidad de reglas (diseño) | 100% | las reglas se apoyan en fuentes | que la fuente sea la correcta |
| M6 Integración (diseño↔resto) | 11/20 nodes enlazados; 14 comparten evidencia | el diseño informa a los demás temas | uso real por personas |
| M7 Lectura profunda (Lobo) | 223 fuentes leídas a fondo = 25% del ledger; 222 intuiciones | el cerebro se relee, no solo crece | que las intuiciones sean correctas |
| M8 Uso externo (`impacto.json`) | 7 preguntas · 1 personas · 0 valoradas (0% útiles) · 0 decisiones | Mu se usa fuera del repo | que las decisiones fueran buenas (son autodeclaradas) |

## 5. Auditoría de integridad (fallas reales, sin maquillar)

- ✅ F-n citadas en un node pero **ausentes del ledger**: **0**
- ✅ Wikilinks **no recíprocos** (viola regla 5): **0**
- ✅ Wikilinks **rotos** (destino inexistente): **0**
- ✅ Nodes **aislados** (sin enlaces): **0**
- ✅ Nodes **ausentes** de la tabla de `alma.md`: **0**
- ⚠️ Nodes **más nuevos que su fecha en `alma.md`** (solo se juzga si el último commit es posterior al inicio del historial visible, 2026-09-08; antes es indeterminable): **11** — behavioral-design-estado-disciplina (alma 2026-10-04 < git 2026-10-15), fenomeno-el-nino-impacto-personas (alma 2026-10-07 < git 2026-10-20), fenomenos-psicologicos (alma 2026-10-04 < git 2026-10-20), futuro-asesores-seguros-venta-digital (alma 2026-10-04 < git 2026-10-20), glosario-seguro-salud-peru (alma 2026-07-21 < git 2026-10-20), material-visual-venta-consultiva (alma 2026-10-04 < git 2026-10-20), mecanismos-seguros-salud (alma 2026-10-04 < git 2026-10-15), modelo-personas-sinteticas (alma 2026-10-07 < git 2026-10-20), modelo-salud-ia-farmacias-peru (alma 2026-10-07 < git 2026-10-20), seguros-comportamiento-mundo-peru (alma 2026-10-07 < git 2026-10-20), tendencias-diseno-innovacion (alma 2026-10-04 < git 2026-10-15)
- ✅ Outputs que **no citan ningún node** (viola regla 4): **0**

## 6. Tabla por node

| Node | Líneas | F-n citadas | A/B | Enlaces ent./sal. | Última modif. visible (git) | alma |
|---|---|---|---|---|---|---|
| `tendencias-diseno-innovacion` | 2002 | 274 | 140 | 11/11 | 2026-10-15 | 2026-10-04 v4.1 |
| `convergencia-psicologia-economia-ia` | 245 | 115 | 49 | 7/7 | 2026-10-04 | 2026-10-04 v1.0 |
| `fenomenos-psicologicos` | 549 | 107 | 104 | 9/9 | 2026-10-20 | 2026-10-04 v1.0 |
| `fenomeno-el-nino-impacto-personas` | 405 | 58 | 32 | 4/4 | 2026-10-20 | 2026-10-07 v1.1 |
| `mecanismos-seguros-salud` | 355 | 53 | 33 | 9/9 | 2026-10-15 | 2026-10-04 v1.2 |
| `riesgo-proteccion-seguros-sectores-populares-peru` | 286 | 50 | 20 | 8/8 | 2026-10-20 | 2026-10-20 v1.0 |
| `lealtad-gamificacion-recompensas-retail` | 222 | 44 | 17 | 4/4 | 2026-10-15 | 2026-10-15 v1.0 |
| `conducta-humano-ia` | 142 | 41 | 28 | 7/7 | 2026-10-04 | 2026-10-04 v1.1 |
| `proyecto-back-to-basics-ffvv-vida` | 976 | 33 | 29 | 7/7 | 2026-10-12 | 2026-10-12 v1.4 |
| `modelo-salud-ia-farmacias-peru` | 618 | 24 | 18 | 5/5 | 2026-10-20 | 2026-10-07 v1.0 |
| `futuro-asesores-seguros-venta-digital` | 390 | 23 | 2 | 7/7 | 2026-10-20 | 2026-10-04 v1.0 |
| `seguros-comportamiento-mundo-peru` | 341 | 23 | 12 | 16/16 | 2026-10-20 | 2026-10-07 v1.1 |
| `material-visual-venta-consultiva` | 378 | 18 | 12 | 9/9 | 2026-10-20 | 2026-10-04 v1.1 |
| `transicion-venta-fria-a-opt-in` | 325 | 18 | 7 | 4/4 | 2026-10-04 | 2026-10-04 v1.0 |
| `evaluacion-calidad-agentes-conversacionales-ia` | 256 | 17 | 11 | 4/4 | 2026-10-04 | 2026-10-04 v1.0 |
| `behavioral-design-estado-disciplina` | 321 | 10 | 9 | 10/10 | 2026-10-15 | 2026-10-04 v1.1 |
| `glosario-seguro-vida-peru` | 216 | 8 | 4 | 3/3 | indeterminada (≤ 2026-09-08, historial truncado) | 2026-07-24 v1.0 |
| `venta-vida-digital-hibrida-latam` | 233 | 8 | 4 | 2/2 | 2026-10-04 | 2026-10-04 v1.0 |
| `glosario-seguro-salud-peru` | 197 | 6 | 5 | 5/5 | 2026-10-20 | 2026-07-21 v1.0 |
| `matriz-productos-vida-rimac` | 184 | 0 | 0 | 2/2 | indeterminada (≤ 2026-09-08, historial truncado) | 2026-07-26 v1.2 |
| `modelo-personas-sinteticas` | 81 | 0 | 0 | 7/7 | 2026-10-20 | 2026-10-07 v1.0 |

## 7. Límites declarados de esta medición

- **Historial git truncado:** el clon es superficial; las instantáneas (§3.2) empiezan en la fecha indicada. §3.1 reconstruye el ledger desde su columna `fecha`, que puede ser corregida a mano y no prueba *cuándo* se leyó la fuente.
- **Citar no es validar:** M2/M5 cuentan referencias `F-n`, no si la cita respalda la afirmación (eso lo audita el chequeo de eco de cita del propio node, no este script).
- **Rangos 'F-a a F-b' no se expanden:** si un node cita un rango, esas fuentes cuentan como huérfanas aquí. Es deliberado: un rango no es trazabilidad por afirmación.
- **Rigor A–E es el del ledger** (juicio de `cronista`), no re-evaluado aquí.
- **Hipótesis y reglas se leen por formato** (`| **Hn** |`, `- **Cn —`). Si el node cambia de formato, las métricas de diseño caerán a 0: tomarlo como alarma de parser, no como pérdida de conocimiento.
- **Uso externo, medición joven y autodeclarada:** desde 2026-10-04 `impacto.json` cuenta preguntas reales a Mu, valoraciones ¿te sirvió? y decisiones que las personas dicen haber tomado con Mu (artefacto + `impacto_manual.jsonl`). Prueba uso, no que la decisión fuera buena; solo mide a quien usa el artefacto o lo declara.
- **Wikilinks se cuentan en todo el texto del node**, no solo en `## Conexiones`.

---
*Visor interactivo: `research/grafo/grafo.html` · grafo crudo: `grafo.json` · serie: `historial.jsonl`.*
