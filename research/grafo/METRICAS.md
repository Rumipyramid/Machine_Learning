# Métricas del grafo — definiciones (contrato de transparencia)

Todo se calcula con `python research/grafo/build_grafo.py` leyendo solo archivos del repo. Sin LLM, sin
estimaciones: si una cifra no sale de contar algo, no está aquí. Resultado actual: `ESTADO.md`.

## Qué es el grafo
- **Vértices:** nodes (`_nodes/*.md`), outputs (`_outputs/*`), fuentes (filas `F-n` de `fuentes/codice.md`).
- **Aristas:** `wikilink` (`[[slug|alias]]` entre nodes) · `deriva` (un output menciona el slug de un node) ·
  `cita` (un node contiene el token `F-n`).

## Métricas
| ID | Fórmula | Qué dice | Qué NO dice |
|---|---|---|---|
| M1 Base sólida | fuentes A+B / fuentes del ledger | peso de evidencia primaria/oficial | veracidad del hallazgo |
| M2 Cobertura de citación | F-n citadas por ≥1 node / ledger | cuánto del ledger sostiene conocimiento | que la cita respalde la afirmación |
| M3 Reciprocidad | wikilinks A→B con B→A / wikilinks | cumplimiento de la regla 5 de `alma.md` | calidad del enlace |
| M4 Falsabilidad ejercida (diseño) | hipótesis ≠ `abierta` / total (§6 del node) | el node confronta, no solo acumula | rigor de las pruebas |
| M4b Autocorrección (diseño) | `refutada` / resueltas | 0% sostenido = sospecha de sesgo de confirmación | que un % alto sea bueno |
| M5 Trazabilidad de reglas (diseño) | reglas `Cn` con ≥1 F-n en su párrafo / reglas | reglas con base explícita | que la base sea correcta |
| M6 Integración (diseño↔resto) | nodes enlazados al de diseño; F-n compartidas (Jaccard) | si el cerebro de diseño informa a los demás | uso real por personas |
| M7 Lectura profunda | fuentes en `lobo/fuentes_leidas_lobo.md` / ledger | el cerebro se relee, no solo crece | exactitud de las intuiciones |
| Huérfanos de cita | F-n dentro de los rangos de diseño/innovación (CLAUDE.md) sin cita individual en el node | cosecha no integrada | pérdida (pueden estar en un rango "F-a a F-b") |

## Evolución
- **§3.1 (ledger):** acumulado por la columna `fecha` del ledger. Cubre todo el origen; es fecha de registro.
- **§3.2 (git):** instantánea completa por día con commits (`historial.jsonl`). **Clon superficial:** el historial
  verificable empieza donde lo indique el reporte. Cada ejecución regenera la serie desde git, así que al
  traer historial completo (`git fetch --unshallow`) la serie se amplía sola.

## Auditoría de integridad (§5)
F-n inexistentes en el ledger · wikilinks no recíprocos / rotos · nodes aislados · nodes fuera de `alma.md` ·
`alma.md` desactualizada · outputs que no citan node. Se reportan como fallas, no se corrigen solas.

## Reglas del sistema
1. Determinista: misma entrada → mismo reporte (salvo fecha).
2. Nunca edita nodes, ledger ni `alma.md`; solo escribe en `research/grafo/`.
3. Lo no medible se declara en `ESTADO.md` §7. Impacto externo (uso por personas) hoy **no se mide**.
4. Si cambia el formato de tablero de hipótesis/reglas del node de diseño, las M4/M5 caen a 0: es alarma de parser.

## Nivel de inteligencia (panel `/mu`, sección 00)
Escalera de 7 niveles (`niveles.json`): MEMORIA → ORDEN → RELACIÓN → CRITERIO → AUTOCORRECCIÓN → PROFUNDIDAD → IMPACTO.
- **Regla:** se sube de nivel solo si se cumplen **todos** los criterios de ese nivel y de los anteriores; no hay puntaje compuesto ni pesos.
- **Umbrales:** propuestos por el autor (juicio, no norma); se editan en `niveles.json` y el panel los lee.
- **Qué significa:** madurez estructural y metodológica del repositorio (íntegro, conectado, con criterio, autocorregido, leído a fondo). **No** mide verdad del contenido ni capacidad cognitiva.
- **N7 (IMPACTO)** exige medir uso/decisiones de personas; hoy no hay instrumento, así que no es alcanzable.
