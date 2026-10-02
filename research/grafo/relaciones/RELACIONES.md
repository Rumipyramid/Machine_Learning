# 🧬 Grafo semántico del códice — RELACIONES

*Generado 2026-10-02 por `relaciones.py render`. No editar a mano. Cada relación vive en `triples.jsonl` con fuente F-n, apoyo, nivel de lectura y fuerza.*

> **Transparencia:** una relación aquí es lo que *una fuente dice*, no un hecho. `lectura=ficha` significa que solo se leyó el resumen del ledger; `abstract` que se leyó el resumen real de la fuente; `completa`, el texto íntegro. Un cruce entre fuentes es una *coincidencia de entidades*, no una prueba de que las fuentes sean compatibles.

## 1. Cobertura

| | |
|---|---|
| Fuentes procesadas | **5 de 468** (1.1%) |
| …del cerebro de diseño (citadas en el node) | 5 de 167 |
| …por rigor | A 4/134 · B 0/76 · C 1/100 · D 0/117 · E 0/28 |
| Barridos | 1 |
| Entidades | 30 |
| Relaciones | 28 |
| Nivel de lectura | abstract 17 · ficha 11 |
| Fuerza de las afirmaciones | descriptiva 11 · observacional 11 · causal 5 · teorica 1 |

## 2. Relaciones por tipo

| Relación | Clase | n |
|---|---|---|
| `aumenta` | efecto | 5 |
| `aplica_a` | estructura | 5 |
| `mide` | metodo | 3 |
| `tiene_limite` | metodo | 3 |
| `origina_en` | metodo | 3 |
| `asocia_con` | efecto | 2 |
| `modera` | efecto | 2 |
| `es_tipo_de` | estructura | 2 |
| `contradice` | evidencia | 2 |
| `respalda` | evidencia | 1 |

## 3. Convergencias: entidades sostenidas por ≥2 fuentes

| Entidad | Fuentes |
|---|---|
| Desempeño financiero de la firma (ROA, ROS, crecimiento) | F-237, F-238 |
| Diseño efectivo → mejor desempeño de la firma | F-237, F-238 |
| Firmas públicas de EE.UU. (n=1.659, 1980-2015) | F-237, F-238 |
| Susceptibilidad a dark patterns | F-241, F-251 |
| Menor educación → mayor susceptibilidad a patterns leves | F-241, F-251 |

## 4. Tensiones declaradas (`contradice` / `refuta`)

- **Ingreso, educación y edad explican poco la susceptibilidad** —contradice→ **Menor educación → mayor susceptibilidad a patterns leves** (F-251, observacional): Abstract: evidencia débil de que ingreso, educación o edad afecten materialmente la susceptibilidad. Tensión posiblemente parcial: F-241 mira solo patterns leves; F-251 proxies en general.
- **Solo ~1/3 de las ideas mejora su métrica objetivo (1/3 negativo, 1/3 nulo)** —contradice→ **El diseño devuelve multiplicadores de retorno (p. ej. 100:1)** (F-262, teorica): Inferencia del node de diseño (reglas C2/C7), no del artículo, que trata de experimentación y no de diseño: si ~2/3 de las ideas bien diseñadas no mueven su métrica, un multiplicador universal es difícil de sostener.

## 5. Hubs (entidades más conectadas)

| Entidad | Tipo | Grado | Fuentes |
|---|---|---|---|
| Diseño efectivo → mejor desempeño de la firma | afirmacion | 4 | 2 |
| Capacidad de diseño-ingeniería | constructo | 4 | 1 |
| Firmas públicas de EE.UU. (n=1.659, 1980-2015) | poblacion | 3 | 2 |
| Dark patterns leves | intervencion | 3 | 1 |
| Dark patterns | concepto | 3 | 1 |
| Dark patterns agresivos | intervencion | 3 | 1 |
| Permanencia/aceptación de un plan dudoso | metrica | 3 | 1 |
| Susceptibilidad a dark patterns | resultado | 3 | 2 |
| Solo ~1/3 de las ideas mejora su métrica objetivo (1/3 negativo, 1/3 nulo) | afirmacion | 3 | 1 |
| Plataforma de experimentación de Microsoft (ExP) | organizacion | 3 | 1 |

## 6. Discrepancias halladas contra el ledger (para `cronista`; no se corrigen aquí)

- **F-251** (2026-10-02): Ficha dice 'Varios, 2021'. La fuente es Zac, Huang, von Moltke, Decker & Ezrachi, *Behavioural Public Policy*, publicada online 3-feb-2025 (SSRN 2023). Además la ficha dice que 'la educación sí modera en los patterns leves'; el abstract solo dice evidencia débil de que ingreso/educación/edad importen y posible mayor vulnerabilidad en mayores. Posible mezcla con F-241. Revisar autor, año y esa frase.
- **F-241** (2026-10-02): Las cifras 11,3% / 25,8% / 41,9% no aparecen en el abstract consultado; sí 'más del doble' y 'casi cuatro veces' (consistentes: 2,3x y 3,7x). Falta confirmar con el texto completo.
- **F-262** (2026-10-02): La ficha mezcla '~1/3 de los experimentos mejora la métrica' (Microsoft, verificado) con '85-90% de fracaso en Bing, Google Ads, Netflix y Airbnb' (no verificado hoy). Son bases distintas; no deberían leerse como una sola cifra.
- **F-238** (2026-10-02): La autoría sigue sin verificarse tras buscar (revista, título y fecha de publicación online 19-ago-2025 confirmados).

## 7. Registro de barridos

| Fecha | Fuentes | Relaciones | Sin aporte | Notas |
|---|---|---|---|---|
| 2026-10-02 | F-237, F-238, F-241, F-251, F-262 | 28 | – | Primer lote (cerebro de diseño, 🟢A primero salvo F-262 🟡C por ser su contrapeso). Lectura vía WebSearch de abstracts; ningún texto completo. |

---
*Visor: `relaciones.html` · datos: `relaciones.json` · siguiente lote: `python research/grafo/relaciones/relaciones.py next`*
