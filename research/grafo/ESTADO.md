# 🕸️ Grafo del segundo cerebro — ESTADO

*Generado: 2026-10-26 por `research/grafo/build_grafo.py` (determinista, sin LLM). No editar a mano: se regenera. Definiciones: `METRICAS.md`.*

> **Transparencia:** cada cifra de este reporte sale de contar archivos del repo. Lo que no se puede medir está listado en §7. Un número alto aquí significa *más material y mejor enlazado*, **no** que el conocimiento sea *verdadero* ni que haya tenido impacto fuera del repo.

## 1. Estado actual (qué hay)

| Capa | Cantidad | Detalle |
|---|---|---|
| Nodes (`_nodes/`) | 30 | 9,530 líneas |
| Outputs (`_outputs/`) | 5 | derivan de nodes: 5 de 5 citan algún node |
| Fuentes en el ledger | 1064 | 🟢A 347 · 🔵B 195 · 🟡C 230 · 🟠D 234 · 🔴E 43 · otras/sin clasificar 15 |
| Aristas wikilink (node→node) | 230 | recíprocas: 230 de 230 (100%) |
| Fuentes citadas por ≥1 node | 1027 de 1064 | 97% del ledger; **37 viven solo en el ledger** |
| Fuentes citadas por ≥2 nodes (transversales) | 221 | evidencia reutilizada entre temas |
| **Grafo semántico** (relaciones extraídas) | 1064 de 1064 fuentes (100%) | 2323 relaciones · 126 barridos · detalle en `relaciones/RELACIONES.md` |
| Componentes conexas del grafo de nodes | 1 | grafo conexo |

## 2. Segundo cerebro de DISEÑO (`tendencias-diseno-innovacion` y sus nodos de dominio `diseno-*`, `innovacion-evidencia`)

| Indicador | Valor | Cómo leerlo |
|---|---|---|
| Iteraciones de bitácora | 9 (2026-07-26, 2026-07-29, 2026-08-02, 2026-10-02, 2026-10-12) | cuántas veces se confrontó el node |
| Tamaño | 1,124 líneas | crecimiento ≠ calidad; ver trazabilidad |
| Fuentes citadas explícitamente | 444 | F-n individuales dentro del node |
| …de rigor A/B | 229 (52%) | solidez de la base |
| Hipótesis vivas | 36: abierta 16 · parcial 14 · respaldada 2 · refutada 4 | tablero §6 |
| **Falsabilidad ejercida** | 56% (20/36) | hipótesis que ya se movieron de `abierta` |
| **Tasa de autocorrección** | 20% (4/20) | de las resueltas, cuántas se refutaron: 0% sostenido sería señal de confirmación sesgada |
| Reglas de criterio | 22 | §7 |
| **Trazabilidad de reglas** | 100% (22/22) | reglas con ≥1 F-n en su propio párrafo |
| Escala de madurez §5 | 🟢 16 · 🟡 10 · 🔴 15 · ⚔️ 4 | dónde está el peso de la evidencia |
| **Huérfanos de cita** | 8 de 181 (4%) | fuentes en los rangos de diseño/innovación (CLAUDE.md) registradas pero **sin cita individual** en el node (pueden estar en un rango 'F-a a F-b' o en otro node) |
| …de ellos citados en otro node | 0 | no están perdidos, solo fuera del node de diseño |

**Vecinos por evidencia compartida** (candidatos a conexión; ✅ = ya enlazado por wikilink):

| Node | F-n compartidas | Jaccard | Enlazado |
|---|---|---|---|
| `conducta-humano-ia` | 27 | 0.058 | ✅ |
| `proyecto-back-to-basics-ffvv-vida` | 19 | 0.041 | ✅ |
| `convergencia-psicologia-economia-ia` | 11 | 0.02 | ✅ |
| `fenomenos-psicologicos` | 10 | 0.018 | ✅ |
| `behavioral-design-estado-disciplina` | 9 | 0.02 | ✅ |
| `evaluacion-calidad-agentes-conversacionales-ia` | 8 | 0.018 | ✅ |
| `material-visual-venta-consultiva` | 8 | 0.018 | ✅ |
| `mecanismos-seguros-salud` | 7 | 0.014 | ✅ |
| `glosario-seguro-vida-peru` | 4 | 0.009 | ✅ |
| `seguros-comportamiento-mundo-peru` | 4 | 0.009 | ✅ |
| `transicion-venta-fria-a-opt-in` | 4 | 0.008 | ✅ |
| `glosario-seguro-salud-peru` | 3 | 0.007 | ✅ |
| `fenomeno-el-nino-impacto-personas` | 2 | 0.004 | ❌ sin enlace |
| `modelo-salud-ia-farmacias-peru` | 2 | 0.004 | ✅ |
| `conciencia-cuantica` | 0 | 0.0 | ❌ sin enlace |
| `futuro-asesores-seguros-venta-digital` | 0 | 0.0 | ✅ |
| `matriz-productos-vida-rimac` | 0 | 0.0 | ❌ sin enlace |
| `modelo-personas-sinteticas` | 0 | 0.0 | ✅ |
| `recomendaciones-acciones-2026` | 0 | 0.0 | ❌ sin enlace |
| `rentabilidad-modelos-seguros` | 0 | 0.0 | ❌ sin enlace |
| `venta-vida-digital-hibrida-latam` | 0 | 0.0 | ✅ |

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
| 2026-10-10 | 74 | 874 | 36 | ██████████████████ |
| 2026-10-11 | 5 | 879 | 0 | █ |
| 2026-10-12 | 97 | 976 | 43 | ████████████████████████ |
| 2026-10-25 | 88 | 1064 | 52 | ██████████████████████ |

### 3.2 Instantáneas por git (estado completo del grafo en cada día con commits)

*Fuente: `git show` de cada commit. **El clon es superficial (shallow)**: el historial verificable empieza en 2026-08-16; antes de eso solo vale §3.1.*

| Fecha | Commit | Fuentes | Nodes | Outputs | Wikilinks | Fuentes citadas | Diseño: líneas | H abiertas | H resueltas | Reglas |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-08-16 | `3acec5d` | 468 | 15 | 4 | 69 | 352 | 1800 | 19 | 12 | 22 |
| 2026-10-02 | `e32e8e5` | 515 | 16 | 4 | 84 | 404 | 1898 | 19 | 14 | 22 |
| 2026-10-03 | `d80e14b` | 645 | 17 | 4 | 96 | 540 | 2000 | 15 | 20 | 22 |
| 2026-10-04 | `b635cd4` | 740 | 18 | 4 | 110 | 636 | 2001 | 15 | 20 | 22 |
| 2026-10-06 | `944e196` | 528 | 16 | 4 | 84 | 423 | 1948 | 17 | 17 | 22 |
| 2026-10-07 | `7d6f508` | 800 | 19 | 5 | 116 | 694 | 2001 | 15 | 20 | 22 |
| 2026-10-08 | `686a858` | 740 | 18 | 4 | 110 | 636 | 2001 | 15 | 20 | 22 |
| 2026-10-09 | `de3c9ed` | 800 | 19 | 5 | 116 | 694 | 2001 | 15 | 20 | 22 |
| 2026-10-11 | `614bf74` | 879 | 20 | 5 | 142 | 770 | 2033 | 16 | 20 | 22 |
| 2026-10-12 | `90d0074` | 976 | 20 | 5 | 158 | 870 | 2215 | 16 | 20 | 22 |
| 2026-10-25 | `f258445` | 1064 | 30 | 5 | 230 | 1027 | 1124 | 16 | 20 | 22 |

*(Se omiten los días sin cambio en estas columnas.)*

## 4. Métricas de impacto (definidas en `METRICAS.md`)

| Métrica | Valor | Qué dice | Qué NO dice |
|---|---|---|---|
| M1 Base sólida (A+B / ledger) | 51% | proporción de evidencia primaria/oficial | no que el hallazgo sea cierto |
| M2 Cobertura de citación | 97% | cuánto del ledger sostiene algún node | un node puede citar mal |
| M3 Reciprocidad de enlaces | 100% | cumplimiento de la regla 5 de `alma.md` | calidad del enlace |
| M4 Falsabilidad ejercida (diseño) | 56% | el node confronta, no solo acumula | que las pruebas fueran rigurosas |
| M5 Trazabilidad de reglas (diseño) | 100% | las reglas se apoyan en fuentes | que la fuente sea la correcta |
| M6 Integración (diseño↔resto) | 16/21 nodes enlazados; 14 comparten evidencia | el diseño informa a los demás temas | uso real por personas |
| M7 Lectura profunda (Lobo) | 196 fuentes leídas a fondo = 18% del ledger; 195 intuiciones | el cerebro se relee, no solo crece | que las intuiciones sean correctas |
| M8 Uso externo (`impacto.json`) | 42 preguntas · 1 personas · 1 valoradas (100% útiles) · 0 decisiones | Mu se usa fuera del repo | que las decisiones fueran buenas (son autodeclaradas) |

## 5. Auditoría de integridad (fallas reales, sin maquillar)

- ✅ F-n citadas en un node pero **ausentes del ledger**: **0**
- ✅ Wikilinks **no recíprocos** (viola regla 5): **0**
- ✅ Wikilinks **rotos** (destino inexistente): **0**
- ✅ Nodes **aislados** (sin enlaces): **0**
- ✅ Nodes **ausentes** de la tabla de `alma.md`: **0**
- ✅ Nodes **más nuevos que su fecha en `alma.md`** (solo se juzga si el último commit es posterior al inicio del historial visible, 2026-08-16; antes es indeterminable): **0**
- ✅ Outputs que **no citan ningún node** (viola regla 4): **0**

## 6. Tabla por node

| Node | Líneas | F-n citadas | A/B | Enlaces ent./sal. | Última modif. visible (git) | alma |
|---|---|---|---|---|---|---|
| `tendencias-diseno-innovacion` | 1124 | 266 | 139 | 24/24 | 2026-10-25 | 2026-10-25 v4.1 |
| `diseno-producto-digital` | 781 | 148 | 60 | 5/5 | 2026-10-25 | 2026-10-25 v1.0 |
| `convergencia-psicologia-economia-ia` | 262 | 121 | 51 | 14/14 | 2026-10-25 | 2026-10-25 v1.0 |
| `fenomenos-psicologicos` | 561 | 115 | 112 | 10/10 | 2026-10-25 | 2026-10-25 v1.0 |
| `conciencia-cuantica` | 352 | 72 | 36 | 3/3 | 2026-10-10 | 2026-10-10 v1.0 |
| `fenomeno-el-nino-impacto-personas` | 413 | 59 | 32 | 6/6 | 2026-10-25 | 2026-10-25 v1.1 |
| `mecanismos-seguros-salud` | 358 | 57 | 35 | 12/12 | 2026-10-25 | 2026-10-25 v1.2 |
| `innovacion-evidencia` | 329 | 55 | 22 | 2/2 | 2026-10-25 | 2026-10-25 v1.0 |
| `conducta-humano-ia` | 167 | 51 | 32 | 11/11 | 2026-10-25 | 2026-10-25 v1.1 |
| `modelo-salud-ia-farmacias-peru` | 674 | 47 | 28 | 7/7 | 2026-10-25 | 2026-10-25 v1.0 |
| `diseno-servicios-politicas-salud` | 57 | 41 | 22 | 5/5 | 2026-10-25 | 2026-10-25 v1.0 |
| `proyecto-back-to-basics-ffvv-vida` | 940 | 34 | 30 | 15/15 | 2026-10-25 | 2026-10-25 v1.4 |
| `transicion-venta-fria-a-opt-in` | 415 | 31 | 12 | 5/5 | 2026-10-25 | 2026-10-25 v1.0 |
| `seguros-comportamiento-mundo-peru` | 356 | 30 | 14 | 20/20 | 2026-10-25 | 2026-10-25 v1.1 |
| `futuro-asesores-seguros-venta-digital` | 392 | 23 | 2 | 9/9 | 2026-10-25 | 2026-10-25 v1.0 |
| `rentabilidad-modelos-seguros` | 86 | 19 | 4 | 9/9 | 2026-10-25 | 2026-10-25 v1.0 |
| `evaluacion-calidad-agentes-conversacionales-ia` | 256 | 17 | 11 | 4/4 | 2026-10-04 | 2026-10-04 v1.0 |
| `material-visual-venta-consultiva` | 379 | 17 | 12 | 10/10 | 2026-10-12 | 2026-10-12 v1.1 |
| `diseno-espacios-ciudad` | 87 | 15 | 10 | 4/4 | 2026-10-25 | 2026-10-25 v1.0 |
| `diseno-estrategico-organizacional` | 56 | 15 | 7 | 3/3 | 2026-10-25 | 2026-10-25 v1.0 |
| `diseno-producto-fisico-industrial` | 52 | 15 | 10 | 4/4 | 2026-10-25 | 2026-10-25 v1.0 |
| `diseno-sostenibilidad-circularidad` | 58 | 15 | 7 | 4/4 | 2026-10-25 | 2026-10-25 v1.0 |
| `diseno-social-participativo` | 59 | 14 | 9 | 3/3 | 2026-10-25 | 2026-10-25 v1.0 |
| `behavioral-design-estado-disciplina` | 327 | 12 | 11 | 13/13 | 2026-10-25 | 2026-10-25 v1.1 |
| `recomendaciones-acciones-2026` | 72 | 10 | 1 | 3/3 | 2026-10-25 | 2026-10-25 v1.0 |
| `glosario-seguro-vida-peru` | 218 | 8 | 4 | 5/5 | 2026-10-11 | 2026-10-11 v1.0 |
| `venta-vida-digital-hibrida-latam` | 236 | 8 | 4 | 5/5 | 2026-10-25 | 2026-10-25 v1.0 |
| `glosario-seguro-salud-peru` | 198 | 6 | 5 | 6/6 | 2026-10-11 | 2026-10-11 v1.0 |
| `matriz-productos-vida-rimac` | 184 | 0 | 0 | 2/2 | indeterminada (≤ 2026-08-16, historial truncado) | 2026-07-26 v1.2 |
| `modelo-personas-sinteticas` | 81 | 0 | 0 | 7/7 | 2026-10-25 | 2026-10-25 v1.0 |

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
