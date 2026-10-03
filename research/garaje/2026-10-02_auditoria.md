# 🐺 Auditoría del Chacal — 2026-10-02

*Commit `64d138c` · INTELIGENCIA N3/7 RELACIÓN → siguiente CRITERIO (63%) · rúbrica: `research/grafo/chacal_rubrica.json` (umbrales propuestos, editables).*

> El Chacal le pregunta a Mu y mide con qué evidencia respondió. **Los semáforos son medidos; el veredicto es juicio del auditor y no los contradice.** Una respuesta fluida no es una respuesta respaldada.

## Tablero

| Pregunta | cobertura | vigencia | solidez | contradicciones | profundidad |
|---|---|---|---|---|---|
| Q1 — ¿Qué es lo más relevante en la actualidad en el rubro del di… | 🟢 | 🟢 | 🟡 | 🔴 | 🟡 |
| Q2 — ¿Qué es lo más relevante en la actualidad de la investigació… | 🟡 | 🟡 | 🟢 | 🟡 | 🔴 |
| Q3 — ¿Qué es lo más relevante en seguros en la actualidad?… | 🟢 | 🟡 | 🟢 | 🟡 | 🔴 |

## Q1 — ¿Qué es lo más relevante en la actualidad en el rubro del diseño?

### Respuesta de Mu

**El diseño importa por su mecanismo, no por su multiplicador.** (1) El efecto es real, pequeño, acumulativo y mediado: F-237 y F-238 (desempeño de firmas, observacional) y F-262 (solo ~1/3 de los experimentos mejora su métrica). Las cifras estrella ($1→$100, McKinsey +32%/+56%) son correlacionales y no auditables. (2) El eje del gremio es IA × identidad profesional; la ansiedad supera la evidencia causal y hay incentivo comercial en ambos bandos (H10/H11). (3) Generative UI gana en preferencia (F-381, F-476) pero pierde en usabilidad funcional (F-382), consistencia (F-384) y fidelidad entre lo que dice y lo que implementa (F-475); falta el estudio de uso repetido (H3). (4) Negocio: Figma creció +48% en el Q2 y la acción no recuperó los US$33, pero por costo de IA sobre el margen (H13 respaldada en la letra, mecanismo en disputa → H32); Lovable sigue abierta (H14); las consultoras de diseño siguen en crisis (F-307), sin evidencia nueva este trimestre. (5) Productividad con IA: sin resolver; METR cambió su diseño y sus intervalos incluyen el cero (F-474).

### Perfil de evidencia (medido)

| Dimensión | Semáforo | Medida |
|---|---|---|
| cobertura | 🟢 | 2 nodes (2,211 líneas), 192 fuentes citadas |
| vigencia | 🟢 | node más viejo 0 d (más nuevo 0 d); última fuente registrada 2026-10-02 (hace 0 d); 74% de las fuentes con año ≥ 2025 (año conocido en 185/192; máx. 2026) |
| solidez | 🟡 | A/B = 36% · rigor {'?': 7, 'A': 39, 'B': 30, 'C': 47, 'D': 49, 'E': 20} |
| contradicciones | 🔴 | 0 tensiones sin resolver (de 8) + 3 discrepancias abiertas |
| profundidad | 🟡 | 26% de las fuentes con relaciones extraídas; 22% de ellas leídas más allá de la ficha |
| hipótesis (diseño) | — | {'abierta': 20, 'parcial': 7, 'respaldada': 4, 'refutada': 1, 'otra': 1} |

### Veredicto del Chacal

Es la respuesta mejor fundada del cerebro: 192 fuentes, node actualizado hoy y todas las tensiones del grafo con estado. Pero **el Chacal no la deja pasar limpia**. (a) Solo el 36% de las fuentes es A/B; 49 son D y 20 son E, y es justo donde viven las cifras de negocio (Figma, Lovable) que sostienen los puntos 4 y 5. (b) Las dos cifras bursátiles vienen de agregadores y resúmenes, no del 8-K abierto. (c) Hay 3 discrepancias del ledger abiertas (F-241, F-238, posible duplicado F-256/F-382) que tocan justo la evidencia del punto 3. (d) La pista social de la iteración 5 es casi inexistente: se afirma que la ansiedad del gremio 'se normaliza' sin una lectura reciente de foros. (e) Mu responde con seguridad sobre H13, pero la causa de la caída de la acción es lectura de prensa, no dato. Sobreafirmación moderada, no grave.

### Apuntes

- Solidez 🟡 (A/B 36%): las afirmaciones de negocio descansan sobre fuentes C/D/E; abrir el 8-K Q2 de Figma y el blog de METR completos.
- Contradicciones 🔴: F-256 y F-382 comparten título; F-241 sin cifras confirmadas; F-238 sin autoría. Sin cerrar estas tres, el punto 3 se apoya en fichas dudosas.
- Pista social débil: no hay lectura de Reddit/X de diseñadores desde julio; el punto 'el eje se normaliza' es heredado de la iteración 3, no confirmado en la iteración 5.
- Profundidad 🟡: 26% del corpus del tema tiene relaciones extraídas y solo 22% de ellas se leyeron más allá de la ficha; la 'tensión resuelta' de F-244/F-246 se resolvió con abstracts, no con los textos.
- Los 7 registros de rigor '?' del ledger en este tema no se pueden ponderar: faltan por clasificar.

## Q2 — ¿Qué es lo más relevante en la actualidad de la investigación y diseño conductual? (humano e IA)

### Respuesta de Mu

**El nudge promedio está en crisis; el valor se mudó a experimentar en el propio contexto, a diseñar a nivel de producto y a integrar IA.** (1) Tras corregir el sesgo de publicación, el efecto promedio de los nudges se debilita mucho (Mertens et al. 2022, F-16) y el campo se reconvirtió en megastudies, personalización y diseño estructural; el mercado sigue pagando (consultoras comprando boutiques conductuales, Vitality en 40+ mercados). (2) Fraude en el campo (caso Ariely/Gino): la conversación pública está dominada por el escándalo y por el giro a IA. (3) **Humano e IA**: la explicabilidad se asocia con la confianza solo de forma moderada (F-242); las explicaciones rara vez dan desempeño complementario (F-243, F-244) y ayudan solo cuando revisarlas ahorra esfuerzo, es decir en tareas difíciles (F-246); la fricción cognitiva reduce la sobre-confianza con costo en satisfacción (F-245); la personalización con IA puede reducir la compra por intrusividad percibida (F-254). (4) Brecha percepción-realidad con IA: −19% real vs. +20% percibido en devs expertos (F-257), pero solo ~1 punto en razonamiento lógico (F-401): la brecha existe, su tamaño depende de la tarea. (5) Evidencia causal en seguros: el UBI simulado (F-442) cambia la conducta de manejo, no demuestra efecto sobre siniestros ni precio.

### Perfil de evidencia (medido)

| Dimensión | Semáforo | Medida |
|---|---|---|
| cobertura | 🟡 | 4 nodes (967 líneas), 39 fuentes citadas |
| vigencia | 🟡 | node más viejo 79 d (más nuevo 0 d); última fuente registrada 2026-07-15 (hace 79 d); 38% de las fuentes con año ≥ 2025 (año conocido en 32/39; máx. 2026) |
| solidez | 🟢 | A/B = 59% · rigor {'?': 1, 'A': 20, 'B': 3, 'C': 5, 'D': 8, 'E': 2} |
| contradicciones | 🟡 | 0 tensiones sin resolver (de 0) + 0 discrepancias abiertas — **ciego**: <10% del corpus tiene relaciones extraídas |
| profundidad | 🔴 | 0% de las fuentes con relaciones extraídas; 0% de ellas leídas más allá de la ficha |

### Veredicto del Chacal

**Esta es la respuesta más frágil de las tres, y la menos justificada por el cerebro.** (a) El node conductual tiene 79 días y 39 fuentes; la evidencia 'humano e IA' más reciente (F-242 a F-246, F-254, F-401) **no vive en él sino en el node de diseño**: Mu tuvo que ensamblar la respuesta cruzando dos nodes, lo que revela que no existe un node de conducta humano-IA. (b) 0% de las fuentes de este tema tiene relaciones extraídas en el grafo: la 'ausencia de tensiones' no significa nada. (c) El punto 1 se apoya en un solo meta-análisis (F-16) y en un node de julio; el campo no se re-confrontó en 2 meses (no hay iteración conductual). (d) El punto 2 (fraude Ariely/Gino) está registrado como conversación, no se verificó el estado actual del caso. Mu responde con fluidez algo que el cerebro no actualizó: respuesta correcta en estructura, vieja en fecha.

### Apuntes

- Brecha estructural: crear/consolidar un node 'conducta humano-IA' que reúna F-242…F-246, F-254, F-257, F-401 y el node conductual; hoy el conocimiento está repartido y se pierde.
- Profundidad 🔴 (0% con relaciones): es el tema con menos grafo semántico, justo el que más cambia (IA × conducta). Candidato 1 para el siguiente barrido.
- Vigencia 🟡: última fuente del node conductual 2026-07-15 (79 días). Falta una iteración /trinidad conductual con mandato de confrontar, como la del node de diseño.
- Solidez 🟢 (A/B 59%): es el único tema donde la base es fuerte; el problema es la edad y la dispersión, no el rigor.
- El node 'evaluacion-calidad-agentes-conversacionales-ia' (v1.0, 2026-07-15) no incorpora C8/C11 del node de diseño pese a que la conexión está declarada: deuda de integración.

## Q3 — ¿Qué es lo más relevante en seguros en la actualidad?

### Respuesta de Mu

**El seguro es un mercado con baja penetración, poca confianza y una brecha de protección enorme, y los modelos que ganan integran la prestación y el cuidado.** (1) Perú: penetración ~2,08% del PBI (LatAm 3,2%, Chile >4,6%), confianza plena 23-25% y ~48% desconfía (causa #1: falta de información); ~4 de cada 10 tuvo seguro en 2 años; solo ~3,3% de hogares asegura contra desastres en un país sísmico; brecha de protección global ~US$1,8 billones. (2) Salud: el margen de la industria en EE.UU. es delgado (1,8% en el 1S de 2025, F-193) y la capitación con provisión propia (Kaiser, Optum) es el principio que gana; el entusiasmo de negocio (Discovery, ChenMed) supera a la evidencia académica independiente y parte del efecto financiero puede ser selección, no cambio de conducta. (3) Insurtech: la pregunta no es el signo sino la disciplina de suscripción (Root, combined ratio 91,4%, vs. Lemonade ~139%, F-449/F-450). (4) Canal y regulación: pasar de venta fría a opt-in casi nunca es voluntario y siempre contrae el volumen; la preferencia declarada por el recorrido híbrido en LatAm supera el 60%, pero la cifra de que 'duplica la retención' no se confirmó (F-376). (5) El PL 08488 del SIS está más cerca del modelo Singapur/NHS que del DPC estadounidense.

### Perfil de evidencia (medido)

| Dimensión | Semáforo | Medida |
|---|---|---|
| cobertura | 🟢 | 7 nodes (2,992 líneas), 131 fuentes citadas |
| vigencia | 🟡 | node más viejo 68 d (más nuevo 0 d); última fuente registrada 2026-08-02 (hace 61 d); 43% de las fuentes con año ≥ 2025 (año conocido en 112/131; máx. 2026) |
| solidez | 🟢 | A/B = 61% · rigor {'?': 4, 'A': 54, 'B': 26, 'C': 23, 'D': 21, 'E': 3} |
| contradicciones | 🟡 | 0 tensiones sin resolver (de 0) + 0 discrepancias abiertas — **ciego**: <10% del corpus tiene relaciones extraídas |
| profundidad | 🔴 | 1% de las fuentes con relaciones extraídas; 0% de ellas leídas más allá de la ficha |

### Veredicto del Chacal

**La más sólida por rigor (A/B 61%) y la más obsoleta por fecha: la última fuente registrada del tema es del 2 de agosto, hace 61 días.** (a) Mu responde 'en la actualidad' con evidencia de julio: no sabe qué publicaron las aseguradoras en el Q2/Q3, ni si cambió algo regulatorio en Perú. (b) Solo 1% de las fuentes de seguros tiene relaciones extraídas: el cerebro no puede ver contradicciones aquí, y las hay: **F-203 (Allianz) no coincide con el comunicado de resultados** (Vida y Salud: la ficha dice €2.400 M, +11,1%; las fuentes dicen ≈€1,35-1,4 mil M, −5,1%), hallazgo que vive solo en la bitácora de Lobo y no en el registro de discrepancias del ledger ni del grafo. (c) El punto 2 usa F-193 como contraste con Allianz, es decir, apoyado en una ficha que se sabe dudosa. (d) Los 4 nodes de seguros que Mu citó fueron 'actualizados' hoy por enlaces recíprocos, pero esa fecha de `alma.md` oculta que la evidencia es de hace 2 meses: la edad del node engaña, la fecha de la última fuente no.

### Apuntes

- Vigencia 🟡 engañosa: las fechas de alma.md de 4 nodes se movieron por ediciones estructurales (enlaces recíprocos); la medida honesta es la última fuente registrada (2026-08-02).
- Contradicciones 🟡 (ciego): <10% del corpus con relaciones; la discrepancia F-203 existe y no está registrada en estado.json. Acción: registrarla y reconciliar con el comunicado de Allianz.
- Profundidad 🔴 (1%): 131 fuentes de seguros, 1 con relaciones. Es el negocio central del proyecto y el tema con menor grafo semántico.
- Falta una iteración de actualidad en seguros: el proceso diario de Lobo lleva ~50 días sin fuentes nuevas en el ledger; está 'refinando' sin evidencia nueva.
- Un hallazgo regulatorio de Lobo (expediente propio de Rímac en 2025, F-70) no figura en los nodes que Mu citó: el cerebro sabe más de lo que el node de seguros dice.

## Evaluación global del segundo cerebro

El segundo cerebro es **bueno guardando, ordenando y citando; mediocre en actualidad y en profundidad; ciego a sus propias contradicciones fuera del tema de diseño.** Tiene estructura íntegra (8/9 chequeos, N3/7) y una base de evidencia razonable (A/B 45%), pero las tres respuestas muestran el mismo patrón: **fluidez por encima de respaldo**. Diseño es lo único auditado recientemente; conducta humano-IA está desactualizada y dispersa; seguros —el negocio central del proyecto— es rigurosamente sólido pero tiene 2 meses sin evidencia nueva y casi nada de grafo semántico. Los semáforos lo confirman: ninguna pregunta llega a verde en profundidad (0-26%), y la ausencia de tensiones medidas en conducta y seguros es ceguera del instrumento, no salud. El mayor riesgo no es un error de contenido sino una respuesta confiada de Mu sobre un mundo que cambió.

### Prioridades (ordenadas)

1. Seguros primero: una iteración /trinidad de actualidad (resultados Q2/Q3 de aseguradoras, regulación peruana, Allianz F-203) y registrar F-203 como discrepancia abierta.
2. Consolidar un node 'conducta humano-IA' (hoy repartido entre el node conductual y el de diseño) y re-confrontarlo con una iteración propia.
3. Extender el grafo semántico a seguros y conducta (hoy 1% y 0%): sin ello 'sin contradicciones' es un número vacío.
4. Cerrar las 3 discrepancias abiertas de diseño (F-241, F-238, duplicado F-256/F-382) con lectura de texto completo.
5. Cambiar la métrica de vigencia a 'última fuente registrada' como medida principal; la fecha de alma.md se mueve con ediciones estructurales y engaña.
