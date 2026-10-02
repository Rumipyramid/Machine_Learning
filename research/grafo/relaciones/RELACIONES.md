# 🧬 Grafo semántico del códice — RELACIONES

*Generado 2026-10-02 por `relaciones.py render`. No editar a mano. Cada relación vive en `triples.jsonl` con fuente F-n, apoyo, nivel de lectura y fuerza.*

> **Transparencia:** una relación aquí es lo que *una fuente dice*, no un hecho. `lectura=ficha` significa que solo se leyó el resumen del ledger; `abstract` que se leyó el resumen real de la fuente; `completa`, el texto íntegro. Un cruce entre fuentes es una *coincidencia de entidades*, no una prueba de que las fuentes sean compatibles.

## 1. Cobertura

| | |
|---|---|
| Fuentes procesadas | **21 de 476** (4.4%) |
| …del cerebro de diseño (citadas en el node) | 21 de 175 |
| …por rigor | A 12/134 · B 2/78 · C 5/104 · D 1/118 · E 1/29 |
| Barridos | 4 |
| Entidades | 83 |
| Relaciones | 71 |
| Nivel de lectura | ficha 42 · abstract 29 |
| Fuerza de las afirmaciones | descriptiva 24 · observacional 20 · causal 20 · teorica 7 |

## 2. Relaciones por tipo

| Relación | Clase | n |
|---|---|---|
| `aplica_a` | estructura | 12 |
| `aumenta` | efecto | 11 |
| `asocia_con` | efecto | 10 |
| `tiene_limite` | metodo | 9 |
| `contradice` | evidencia | 6 |
| `reduce` | efecto | 6 |
| `modera` | efecto | 5 |
| `origina_en` | metodo | 4 |
| `mide` | metodo | 3 |
| `es_tipo_de` | estructura | 3 |
| `respalda` | evidencia | 1 |
| `media` | efecto | 1 |

## 3. Convergencias: entidades sostenidas por ≥2 fuentes

| Entidad | Fuentes |
|---|---|
| Explicabilidad de la IA (explicaciones) | F-242, F-244, F-246 |
| Sobre-confianza en la IA | F-244, F-245, F-246 |
| Generative UI (interfaces generadas por LLM) | F-247, F-475, F-476 |
| Desempeño financiero de la firma (ROA, ROS, crecimiento) | F-237, F-238 |
| Diseño efectivo → mejor desempeño de la firma | F-237, F-238 |
| Firmas públicas de EE.UU. (n=1.659, 1980-2015) | F-237, F-238 |
| Susceptibilidad a dark patterns | F-241, F-251 |
| Menor educación → mayor susceptibilidad a patterns leves | F-241, F-251 |
| Design thinking | F-239, F-240 |
| El efecto del design thinking está totalmente mediado por empoderamiento | F-239, F-240 |
| Las explicaciones rara vez producen desempeño complementario | F-243, F-244 |
| Las explicaciones mejoran la decisión humano-IA | F-244, F-246 |
| ARR de Lovable | F-471, F-472 |
| El ARR de vibe coding no retiene (H14) | F-472, F-473 |
| Churn y cohortes no publicados | F-472, F-473 |
| Generative UI gana en usabilidad percibida | F-475, F-476 |

## 4. Tensiones declaradas (`contradice` / `refuta`)

- **Ingreso, educación y edad explican poco la susceptibilidad** —contradice→ **Menor educación → mayor susceptibilidad a patterns leves** (F-251, observacional) · **estado: alcance_distinto**
  - Abstract: evidencia débil de que ingreso, educación o edad afecten materialmente la susceptibilidad. Tensión posiblemente parcial: F-241 mira solo patterns leves; F-251 proxies en general.
  - *Resolución (2026-10-02):* No es refutación: F-241 (abstract) halla que los menos educados fueron más susceptibles a patterns leves en un experimento de EE.UU.; F-251 (abstract) halla solo evidencia débil de que ingreso, educación o edad importen en general. Distinto alcance y fuerza. Pendiente: texto completo de F-251 para ver el coeficiente de educación.
- **Solo ~1/3 de las ideas mejora su métrica objetivo (1/3 negativo, 1/3 nulo)** —contradice→ **El diseño devuelve multiplicadores de retorno (p. ej. 100:1)** (F-262, teorica) · **estado: inferencia_del_node**
  - Inferencia del node de diseño (reglas C2/C7), no del artículo, que trata de experimentación y no de diseño: si ~2/3 de las ideas bien diseñadas no mueven su métrica, un multiplicador universal es difícil de sostener.
  - *Resolución (2026-10-02):* No hay tensión entre fuentes: el artículo trata de experimentación, no de diseño. La contradicción con los multiplicadores es una inferencia del node (C2/C7) y debe presentarse así.
- **Los mecanismos causales del design thinking no están establecidos** —contradice→ **El efecto del design thinking está totalmente mediado por empoderamiento** (F-240, teorica) · **estado: alcance_distinto**
  - Tensión posiblemente parcial, inferida de las fichas: F-239 propone una mediación en una muestra; F-240 dice que la base de mecanismos es débil en la literatura.
  - *Resolución (2026-10-02):* Compatibles: F-239 prueba una mediación en una sola muestra (160 estudiantes, 62 proyectos); F-240 es una revisión que dice que los mecanismos no están establecidos en general. Una mediación en un estudio no establece el mecanismo; F-240 no se leyó más allá de la ficha.
- **Las explicaciones rara vez producen desempeño complementario** —contradice→ **Las explicaciones mejoran la decisión humano-IA** (F-244, causal) · **estado: reconciliada**
  - No produjeron desempeño complementario humano-IA en el experimento (CHI 2021).
  - *Resolución (2026-10-02):* El moderador es el costo-beneficio de involucrarse (dificultad de la tarea). F-244: tareas de sentido común, sin ventaja de las explicaciones frente a mostrar la confianza. F-246: las explicaciones reducen la sobre-confianza solo en la tarea difícil de un laberinto. Resultados distintos (precisión de equipo vs. sobre-confianza) y tareas distintas, no una contradicción.
- **La IA cobra un impuesto de margen a las herramientas de diseño (H32)** —contradice→ **El mercado descuenta disrupción de IA sobre la demanda (H13)** (F-470, teorica) · **estado: mecanismo_en_disputa**
  - Explicación alternativa del mecanismo (no del resultado): la caída se atribuye al costo de IA sobre el margen, no a una pérdida de demanda. La atribución es lectura de prensa.
  - *Resolución (2026-10-02):* No contradice el resultado de H13 (se cumplió), sino su mecanismo: costo de IA sobre el margen vs. descuento por disrupción de la demanda. Se resuelve con el margen bruto del Q3 (nov-2026); hoy la atribución es lectura de prensa.
- **La justificación de diseño generada no coincide con lo implementado** —contradice→ **Generative UI gana en usabilidad percibida** (F-475, teorica) · **estado: alcance_distinto**
  - Tensión de alcance, no de resultado: F-475 mide fidelidad de implementación; F-476 mide usabilidad percibida en una sesión.
  - *Resolución (2026-10-02):* Miden cosas distintas: fidelidad entre justificación e implementación (F-475, preprint) vs. usabilidad percibida en sesión única (F-476, emisor interesado). Ninguna prueba uso repetido; se mantiene H33 abierta.

## 5. Hubs (entidades más conectadas)

| Entidad | Tipo | Grado | Fuentes |
|---|---|---|---|
| Susceptibilidad a dark patterns | resultado | 5 | 2 |
| Diseño efectivo → mejor desempeño de la firma | afirmacion | 4 | 2 |
| Capacidad de diseño-ingeniería | constructo | 4 | 1 |
| El efecto del design thinking está totalmente mediado por empoderamiento | afirmacion | 4 | 2 |
| Explicabilidad de la IA (explicaciones) | intervencion | 4 | 3 |
| Sobre-confianza en la IA | resultado | 4 | 3 |
| Las explicaciones mejoran la decisión humano-IA | afirmacion | 4 | 2 |
| Firmas públicas de EE.UU. (n=1.659, 1980-2015) | poblacion | 3 | 2 |
| Dark patterns leves | intervencion | 3 | 1 |
| Dark patterns | concepto | 3 | 1 |

## 6. Discrepancias halladas contra el ledger (para `cronista`; no se corrigen aquí)

- ✅ **F-251** (2026-10-02, cerrada): Ficha dice 'Varios, 2021'. La fuente es Zac, Huang, von Moltke, Decker & Ezrachi, *Behavioural Public Policy*, publicada online 3-feb-2025 (SSRN 2023). Además la ficha dice que 'la educación sí modera en los patterns leves'; el abstract solo dice evidencia débil de que ingreso/educación/edad importen y posible mayor vulnerabilidad en mayores. Posible mezcla con F-241. Revisar autor, año y esa frase.
  - *Resolución:* Cerrada: autores y año corregidos en el ledger el 2026-10-02.
- ⚠️ **F-241** (2026-10-02, abierta): Las cifras 11,3% / 25,8% / 41,9% no aparecen en el abstract consultado; sí 'más del doble' y 'casi cuatro veces' (consistentes: 2,3x y 3,7x). Falta confirmar con el texto completo. Actualización 2026-10-02: la afirmación de que los menos educados fueron más susceptibles a patterns leves SÍ figura en el abstract; las cifras exactas siguen sin confirmarse.
- ✅ **F-262** (2026-10-02, cerrada): La ficha mezcla '~1/3 de los experimentos mejora la métrica' (Microsoft, verificado) con '85-90% de fracaso en Bing, Google Ads, Netflix y Airbnb' (no verificado hoy). Son bases distintas; no deberían leerse como una sola cifra.
  - *Resolución:* Cerrada con matiz: el 85-90% se confirma en resúmenes de materiales de Kohavi (Bing ~85%, Google Ads/Netflix ~90%, Airbnb ~92%; Microsoft ~66-70%). Son organizaciones distintas, no una cifra única. El texto de HBR sigue sin abrirse.
- ⚠️ **F-238** (2026-10-02, abierta): La autoría sigue sin verificarse tras buscar (revista, título y fecha de publicación online 19-ago-2025 confirmados).
- ✅ **F-239** (2026-10-02, cerrada): La ficha dice 'Muestra estudiantil' y 'N=160 en 62 proyectos de innovación con empresas'; las dos descripciones conviven y conviene aclarar cuál es la muestra. No verificado.
  - *Resolución:* Cerrada: la muestra es de 160 estudiantes en 62 proyectos de innovación para empresas; las dos descripciones de la ficha eran compatibles.

## 7. Registro de barridos

| Fecha | Fuentes | Relaciones | Sin aporte | Notas |
|---|---|---|---|---|
| 2026-10-02 | F-237, F-238, F-241, F-251, F-262 | 28 | – | Primer lote (cerebro de diseño, 🟢A primero salvo F-262 🟡C por ser su contrapeso). Lectura vía WebSearch de abstracts; ningún texto completo. |
| 2026-10-02 | F-239, F-240, F-242, F-243, F-244, F-245, F-246, F-247 | 20 | – | Pase barato a nivel de FICHA (8 fuentes, sin búsqueda web) para ganar amplitud: grupos design thinking, XAI/sobre-confianza y UI adaptativa. Candidatas a lectura profunda: F-244/F-246 (tensión explica |
| 2026-10-02 | F-239, F-241, F-244, F-246, F-251, F-262 | 8 | – | Lote de resolución de contradicciones: lectura dirigida de abstracts de las fuentes en tensión. |
| 2026-10-02 | F-469, F-470, F-471, F-472, F-473, F-474, F-475, F-476 | 14 | – | Pase sobre las 8 fuentes de la iteración 5 de /trinidad (diseño e innovación). Nivel: abstract en las académicas/METR; ficha en empresa, prensa y blogs. |

---
*Visor: `relaciones.html` · datos: `relaciones.json` · siguiente lote: `python research/grafo/relaciones/relaciones.py next`*
