# 🐺 Auditoría del Chacal — 2026-10-03

*Commit `fb522d1` · INTELIGENCIA N3/7 RELACIÓN → siguiente CRITERIO (89%) · rúbrica: `research/grafo/chacal_rubrica.json` (umbrales propuestos, editables).*

> El Chacal le pregunta a Mu y mide con qué evidencia respondió. **Los semáforos son medidos; el veredicto es juicio del auditor y no los contradice.** Una respuesta fluida no es una respuesta respaldada.

## Tablero

| Pregunta | cobertura | vigencia | solidez | contradicciones | profundidad |
|---|---|---|---|---|---|
| Q1 — ¿Qué es lo más relevante en la actualidad en el rubro del di… | 🟢 | 🟢 | 🟡 | 🔴 | 🟡 |
| Q2 — ¿Qué es lo más relevante en la actualidad de la investigació… | 🟢 | 🟡 | 🟢 | 🟡 | 🟡 |
| Q3 — ¿Qué es lo más relevante en seguros en la actualidad?… | 🟢 | 🟡 | 🟢 | 🟡 | 🔴 |

**Cambios desde la auditoría del 2026-10-02:** ninguno

## Q1 — ¿Qué es lo más relevante en la actualidad en el rubro del diseño?

### Respuesta de Mu

**El diseño importa por su mecanismo, no por su multiplicador, y el oficio está bajo presión de la IA en tareas de producción.** (1) El efecto del diseño es real, pequeño, acumulativo y mediado: F-237, F-238 y F-514 (desempeño de firmas, observacional), F-262 y F-21 (a escala el efecto se encoge: ~8,7 pp en papers vs. ~1,4 pp). Las cifras estrella ($1→$100, McKinsey +32%/+56%) son correlacionales y no auditables (C1, C3, C17). (2) **Corrección reciente:** hay evidencia causal de caída de demanda en tareas de producción de imagen (−17% de publicaciones en una plataforma freelance; F-521, versión de conferencia), mientras el BLS proyecta +2% de empleo de diseñadores gráficos (F-308); la adopción es heterogénea (F-522) y exposición de la OIT no es pérdida de empleo (F-515): hay que segmentar (H34). (3) Generative UI gana en preferencia (F-381, F-476) pero pierde frente a una línea base humana en carga cognitiva (F-513), en usabilidad funcional (F-382), en consistencia (F-384) y en fidelidad entre lo que dice y lo que implementa (F-475); falta el estudio de uso repetido (H3, H33). (4) Humano-IA: las combinaciones rinden peor que lo mejor de cada parte, salvo en tareas de creación (F-516); los indicadores visuales de confianza amplifican el acuerdo con errores (F-520). (5) Negocio: Figma +48% y la acción no recuperó los US$33, por costo de IA sobre el margen (H13 respaldada en la letra; mecanismo en disputa, H32); Lovable sigue abierta (H14); Lemonade mejoró su siniestralidad pero sigue con pérdida neta y Root es rentable sin crecer (H29 parcial). **Lo que Mu no sabe:** no hay lectura reciente de la pista social; H6 y H7 sin evidencia nueva.

### Perfil de evidencia (medido)

| Dimensión | Semáforo | Medida |
|---|---|---|
| cobertura | 🟢 | 2 nodes (2,282 líneas), 225 fuentes citadas |
| vigencia | 🟢 | node más viejo 1 d (más nuevo 0 d); última fuente registrada 2026-10-03 (hace 0 d); 72% de las fuentes con año ≥ 2025 (año conocido en 218/225; máx. 2026) |
| solidez | 🟡 | A/B = 44% · rigor {'?': 7, 'A': 55, 'B': 44, 'C': 49, 'D': 50, 'E': 20} |
| contradicciones | 🔴 | 1 tensiones sin resolver (de 9) + 2 discrepancias abiertas |
| profundidad | 🟡 | 24% de las fuentes con relaciones extraídas; 25% de ellas leídas más allá de la ficha |
| hipótesis (diseño) | — | {'abierta': 20, 'parcial': 8, 'respaldada': 4, 'refutada': 1, 'otra': 1} |

### Veredicto del Chacal

**Mejor respaldada que nunca (A/B 36%→44%), pero contradicciones pasa a 🔴 por una corrección del propio instrumento:** el Chacal contaba como 'resuelta' cualquier tensión con un estado, incluso 'en disputa'; ahora cuenta como abierta la del mecanismo de Figma (H13/H32) y, junto con las discrepancias de F-241 y F-238, suma 3. Además, el punto 2 corrige una tesis central del node y descansa en **una sola fuente causal leída solo en su versión de conferencia**; el punto 5 sigue apoyado en filings leídos vía resúmenes.

### Apuntes

- Abrir F-521 (la versión de revista) antes de reescribir la tesis social del node: es la corrección más importante y la menos verificada.
- Cerrar F-241 y F-238 o declararlas permanentes: con el acceso bloqueado, siguen contando en rojo.
- Pista social sin lectura reciente; lo único que hay es un hilo de X (F-473) y prensa.

## Q2 — ¿Qué es lo más relevante en la actualidad de la investigación y diseño conductual? (humano e IA)

### Respuesta de Mu

**La IA no solo asiste: mueve el juicio y la conducta de las personas, y lo que la gente prefiere de ella diverge de cómo decide.** (1) **Adulación:** una sola interacción con una IA aduladora aumenta 25%-62% la convicción de tener razón y reduce 10%-28% la disposición a asumir responsabilidad, y los usuarios la califican mejor (F-488; preprint preregistrado, N=2.405); ya salió del laboratorio: retiro de GPT-4o en 4 días (F-495) y litigios y cartas de fiscales (F-496, alegaciones, no fallos). (2) **Persuasión:** real pero pequeña por conversación (F-489, Science; F-490); si se concentra en personas susceptibles está **en disputa** (F-491, preprint, vs. F-499, PNAS: el microtargeting no aporta ventaja). (3) **Explicaciones y confianza:** aportan una ganancia pequeña sobre la sola predicción (F-498), no limitada a tareas difíciles; la explicabilidad se asocia con la confianza de forma solo moderada (F-242); la fricción cognitiva reduce la sobre-confianza con costo de aceptación (F-245, F-502, regla CH2); los indicadores visuales de confianza amplifican el acuerdo con errores (F-520). (4) **Brecha percepción-realidad:** −19% real vs. +20% percibido en devs expertos (F-257), con METR en revisión (F-474), y ~1 punto en razonamiento lógico (F-401); medir conducta, no autoinformes (regla CH1). (5) **Combinaciones humano-IA:** peores que lo mejor de cada parte en promedio; ganan solo en creación (F-516). (6) **Descarga cognitiva:** asociada a menos pensamiento crítico solo por autorreporte u observación (F-492, F-493). (7) **Oficio:** el nudge promedio está en crisis (F-16 a F-18) y el efecto a escala cae a ~1,4 pp (F-21). **Mu no sabe:** nada de seguros aplicado a esto (HC6 es extrapolación) y la pista social es un caso (GPT-4o).

### Perfil de evidencia (medido)

| Dimensión | Semáforo | Medida |
|---|---|---|
| cobertura | 🟢 | 5 nodes (1,108 líneas), 66 fuentes citadas |
| vigencia | 🟡 | node más viejo 75 d (más nuevo 1 d); última fuente registrada 2026-10-02 (hace 1 d); 58% de las fuentes con año ≥ 2025 (año conocido en 59/66; máx. 2026) |
| solidez | 🟢 | A/B = 62% · rigor {'?': 1, 'A': 34, 'B': 7, 'C': 12, 'D': 10, 'E': 2} |
| contradicciones | 🟡 | 1 tensiones sin resolver (de 3) + 0 discrepancias abiertas |
| profundidad | 🟡 | 45% de las fuentes con relaciones extraídas; 33% de ellas leídas más allá de la ficha |

### Veredicto del Chacal

**La respuesta que más mejoró** (cobertura 🟢, contradicciones 🟢→🟡 solo por el cambio de instrumento: la persuasión concentrada en susceptibles sigue en disputa y ahora cuenta). Pero la regla CH1/CH2 salió de una búsqueda adversarial hecha sobre **resúmenes**, el titular (adulación) sigue en un preprint, y vigencia está en 🟡 porque el node conductual original (75 días) nunca se re-confrontó: se agregó un node nuevo encima, no se actualizó el viejo.

### Apuntes

- Leer a texto completo F-488, F-491 y F-499: la disputa de persuasión no se resuelve sin eso.
- Re-confrontar el node behavioral-design (75 días): el node nuevo lo supera en actualidad y lo contradice en parte (nudge a escala).
- HC6 (aplicación a seguros) sigue sin un solo estudio; es la pregunta de negocio pendiente.

## Q3 — ¿Qué es lo más relevante en seguros en la actualidad?

### Respuesta de Mu

**Seguros en Perú: mercado de baja penetración y poca confianza que parece estar desacelerando, con presión regulatoria sobre el reclamo y la explicación previa.** (1) **Mercado:** primas netas S/24.034 M a dic-2025 (+8,3%); penetración estable en 2,0%-2,1% del PBI (2,06% a set-2025, F-507; las cifras de 2,01% y ~2,08% son compatibles); confianza plena 23-25% y ~48% desconfía; ~4 de cada 10 tuvo seguro en 2 años. (2) **Alerta sin verificar:** una nota de prensa reporta que el sistema creció solo +1,1% en el 1S 2026 (S/9.451 M) frente a la expectativa de +8%-9% (F-506, fecha y cifras sin confirmar). (3) **Aseguradoras:** Rímac, utilidad neta −40% en el 2T 2026 (F-504); Mapfre Perú, ratio combinado de 102,4% en el 1T (F-505); sin datos del 2T de Pacífico ni Interseguro. (4) **Regulación:** Res. SBS 01923-2026 amplió las infracciones (rechazo de cobertura sin fundamento o fuera de plazo, F-484); Indecopi sancionó a Pacífico (F-485) y a una aseguradora que no acreditó haber explicado las exclusiones (F-486). (5) **PL 08488:** registrado en 2024 (F-508), estado actual no verificado. (6) **Salud en EE.UU.:** el 1,8% de 2025 fue un valle: UnitedHealth bajó su ratio de costo médico a 86,7% en el 2T 2026 (F-198) y la industria ganó US$14,8 mil M de suscripción en el 1T (F-480): un trimestre y una aseguradora, no tendencia confirmada. (7) **Insurtech:** Root, combined ratio de 92,1% sin crecer (F-481); Lemonade, loss ratio de 60% pero pérdida neta (F-509). (8) **Global:** primas reales +1,3% en 2026 (F-487); Allianz Vida y Salud creció 10% en el 2T (F-477) y la cifra antigua de F-203 se corrigió (F-478). **Mu no sabe:** estadísticas oficiales de la SBS al 2T, resultados de Pacífico e Interseguro, y el estado del PL 08488.

### Perfil de evidencia (medido)

| Dimensión | Semáforo | Medida |
|---|---|---|
| cobertura | 🟢 | 7 nodes (3,024 líneas), 149 fuentes citadas |
| vigencia | 🟡 | node más viejo 69 d (más nuevo 1 d); última fuente registrada 2026-10-02 (hace 1 d); 51% de las fuentes con año ≥ 2025 (año conocido en 130/149; máx. 2026) |
| solidez | 🟢 | A/B = 60% · rigor {'?': 4, 'A': 55, 'B': 34, 'C': 32, 'D': 21, 'E': 3} |
| contradicciones | 🟡 | 1 tensiones sin resolver (de 5) + 0 discrepancias abiertas |
| profundidad | 🔴 | 21% de las fuentes con relaciones extraídas; 9% de ellas leídas más allá de la ficha |

### Veredicto del Chacal

**Más completa y más actual (hoy: última fuente), pero la contradicción más importante del tema está sin resolver.** El semáforo de contradicciones pasa a 🟡 porque el +1,1% vs. +8-9% (F-506) sigue en 'sin verificar' y el instrumento antes la daba por resuelta. Profundidad 🔴: solo el 9% de las fuentes con relaciones se leyó más allá de la ficha. Los puntos 3 y 4 vienen de agregadores y prensa; los nodes de seguros no tocados llegan a 69 días.

### Apuntes

- Conseguir la estadística de la SBS al 2T 2026: el dato del +1,1% cambia la tesis del mercado y hoy se sostiene con una nota de prensa.
- Profundidad 🔴: 21% de las fuentes de seguros en el grafo, 9% leídas más allá de la ficha; es el tema de mayor riesgo con la lectura más superficial.
- Nodes de seguros sin tocar (matriz de productos, venta digital LATAM, glosarios) siguen en 🟡 de vigencia por su edad.

## Evaluación global del segundo cerebro

**El cerebro avanzó en actualidad y en respaldo, y el auditor se volvió más severo con razón.** En esta ronda hubo lectura nueva (10 fuentes A/B, una corrección a una tesis social, seguros de Perú, Lemonade) y el instrumento del Chacal corrigió su propia indulgencia: ya no cuenta como 'resuelta' una tensión 'en disputa' o 'sin verificar'. Resultado: **tres contradicciones relevantes quedaron al descubierto** (mecanismo de Figma, persuasión concentrada y +1,1% del mercado peruano). El patrón de fondo no cambió: **se agrega material más rápido de lo que se lee y se verifica**; casi todo lo nuevo viene de resúmenes de búsqueda y las fuentes que más cambian conclusiones (F-521, F-506) son las menos verificadas.

### Prioridades (ordenadas)

1. Verificar con la fuente primaria las dos afirmaciones que más cambian el cuadro: F-521 (caída causal de demanda) y F-506 (+1,1% del mercado peruano).
2. Resolver o declarar permanentes las 3 discrepancias/tensiones abiertas de diseño (F-241, F-238, mecanismo de Figma H13/H32).
3. Re-confrontar el node behavioral-design (75 días) y los nodes de seguros no tocados (hasta 69 días).
4. Leer a texto completo F-488, F-491 y F-499 para cerrar la disputa de persuasión.
5. Seguir subiendo la proporción de fuentes A/B en el node de diseño (43%→50%) con lectura real, no con citas de relleno.
