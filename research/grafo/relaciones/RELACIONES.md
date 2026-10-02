# 🧬 Grafo semántico del códice — RELACIONES

*Generado 2026-10-02 por `relaciones.py render`. No editar a mano. Cada relación vive en `triples.jsonl` con fuente F-n, apoyo, nivel de lectura y fuerza.*

> **Transparencia:** una relación aquí es lo que *una fuente dice*, no un hecho. `lectura=ficha` significa que solo se leyó el resumen del ledger; `abstract` que se leyó el resumen real de la fuente; `completa`, el texto íntegro. Un cruce entre fuentes es una *coincidencia de entidades*, no una prueba de que las fuentes sean compatibles.

## 1. Cobertura

| | |
|---|---|
| Fuentes procesadas | **13 de 468** (2.8%) |
| …del cerebro de diseño (citadas en el node) | 13 de 167 |
| …por rigor | A 12/134 · B 0/76 · C 1/100 · D 0/117 · E 0/28 |
| Barridos | 2 |
| Entidades | 54 |
| Relaciones | 49 |
| Nivel de lectura | ficha 32 · abstract 17 |
| Fuerza de las afirmaciones | observacional 16 · causal 16 · descriptiva 13 · teorica 4 |

## 2. Relaciones por tipo

| Relación | Clase | n |
|---|---|---|
| `aumenta` | efecto | 9 |
| `aplica_a` | estructura | 8 |
| `asocia_con` | efecto | 5 |
| `tiene_limite` | metodo | 4 |
| `modera` | efecto | 4 |
| `contradice` | evidencia | 4 |
| `reduce` | efecto | 4 |
| `mide` | metodo | 3 |
| `es_tipo_de` | estructura | 3 |
| `origina_en` | metodo | 3 |
| `respalda` | evidencia | 1 |
| `media` | efecto | 1 |

## 3. Convergencias: entidades sostenidas por ≥2 fuentes

| Entidad | Fuentes |
|---|---|
| Explicabilidad de la IA (explicaciones) | F-242, F-244, F-246 |
| Sobre-confianza en la IA | F-244, F-245, F-246 |
| Desempeño financiero de la firma (ROA, ROS, crecimiento) | F-237, F-238 |
| Diseño efectivo → mejor desempeño de la firma | F-237, F-238 |
| Firmas públicas de EE.UU. (n=1.659, 1980-2015) | F-237, F-238 |
| Susceptibilidad a dark patterns | F-241, F-251 |
| Menor educación → mayor susceptibilidad a patterns leves | F-241, F-251 |
| Design thinking | F-239, F-240 |
| El efecto del design thinking está totalmente mediado por empoderamiento | F-239, F-240 |
| Las explicaciones rara vez producen desempeño complementario | F-243, F-244 |
| Las explicaciones mejoran la decisión humano-IA | F-244, F-246 |

## 4. Tensiones declaradas (`contradice` / `refuta`)

- **Ingreso, educación y edad explican poco la susceptibilidad** —contradice→ **Menor educación → mayor susceptibilidad a patterns leves** (F-251, observacional): Abstract: evidencia débil de que ingreso, educación o edad afecten materialmente la susceptibilidad. Tensión posiblemente parcial: F-241 mira solo patterns leves; F-251 proxies en general.
- **Solo ~1/3 de las ideas mejora su métrica objetivo (1/3 negativo, 1/3 nulo)** —contradice→ **El diseño devuelve multiplicadores de retorno (p. ej. 100:1)** (F-262, teorica): Inferencia del node de diseño (reglas C2/C7), no del artículo, que trata de experimentación y no de diseño: si ~2/3 de las ideas bien diseñadas no mueven su métrica, un multiplicador universal es difícil de sostener.
- **Los mecanismos causales del design thinking no están establecidos** —contradice→ **El efecto del design thinking está totalmente mediado por empoderamiento** (F-240, teorica): Tensión posiblemente parcial, inferida de las fichas: F-239 propone una mediación en una muestra; F-240 dice que la base de mecanismos es débil en la literatura.
- **Las explicaciones rara vez producen desempeño complementario** —contradice→ **Las explicaciones mejoran la decisión humano-IA** (F-244, causal): No produjeron desempeño complementario humano-IA en el experimento (CHI 2021).

## 5. Hubs (entidades más conectadas)

| Entidad | Tipo | Grado | Fuentes |
|---|---|---|---|
| Diseño efectivo → mejor desempeño de la firma | afirmacion | 4 | 2 |
| Capacidad de diseño-ingeniería | constructo | 4 | 1 |
| Explicabilidad de la IA (explicaciones) | intervencion | 4 | 3 |
| Sobre-confianza en la IA | resultado | 4 | 3 |
| Firmas públicas de EE.UU. (n=1.659, 1980-2015) | poblacion | 3 | 2 |
| Dark patterns leves | intervencion | 3 | 1 |
| Dark patterns | concepto | 3 | 1 |
| Dark patterns agresivos | intervencion | 3 | 1 |
| Permanencia/aceptación de un plan dudoso | metrica | 3 | 1 |
| Susceptibilidad a dark patterns | resultado | 3 | 2 |

## 6. Discrepancias halladas contra el ledger (para `cronista`; no se corrigen aquí)

- **F-251** (2026-10-02): Ficha dice 'Varios, 2021'. La fuente es Zac, Huang, von Moltke, Decker & Ezrachi, *Behavioural Public Policy*, publicada online 3-feb-2025 (SSRN 2023). Además la ficha dice que 'la educación sí modera en los patterns leves'; el abstract solo dice evidencia débil de que ingreso/educación/edad importen y posible mayor vulnerabilidad en mayores. Posible mezcla con F-241. Revisar autor, año y esa frase.
- **F-241** (2026-10-02): Las cifras 11,3% / 25,8% / 41,9% no aparecen en el abstract consultado; sí 'más del doble' y 'casi cuatro veces' (consistentes: 2,3x y 3,7x). Falta confirmar con el texto completo.
- **F-262** (2026-10-02): La ficha mezcla '~1/3 de los experimentos mejora la métrica' (Microsoft, verificado) con '85-90% de fracaso en Bing, Google Ads, Netflix y Airbnb' (no verificado hoy). Son bases distintas; no deberían leerse como una sola cifra.
- **F-238** (2026-10-02): La autoría sigue sin verificarse tras buscar (revista, título y fecha de publicación online 19-ago-2025 confirmados).
- **F-239** (2026-10-02): La ficha dice 'Muestra estudiantil' y 'N=160 en 62 proyectos de innovación con empresas'; las dos descripciones conviven y conviene aclarar cuál es la muestra. No verificado.

## 7. Registro de barridos

| Fecha | Fuentes | Relaciones | Sin aporte | Notas |
|---|---|---|---|---|
| 2026-10-02 | F-237, F-238, F-241, F-251, F-262 | 28 | – | Primer lote (cerebro de diseño, 🟢A primero salvo F-262 🟡C por ser su contrapeso). Lectura vía WebSearch de abstracts; ningún texto completo. |
| 2026-10-02 | F-239, F-240, F-242, F-243, F-244, F-245, F-246, F-247 | 20 | – | Pase barato a nivel de FICHA (8 fuentes, sin búsqueda web) para ganar amplitud: grupos design thinking, XAI/sobre-confianza y UI adaptativa. Candidatas a lectura profunda: F-244/F-246 (tensión explica |

---
*Visor: `relaciones.html` · datos: `relaciones.json` · siguiente lote: `python research/grafo/relaciones/relaciones.py next`*
