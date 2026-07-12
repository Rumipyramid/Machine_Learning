# Modelo de cobertura de salud: triage con IA + farmacias + atención humana (Perú)

> Documento de investigación consolidado. Fuente persistente y versionada en el repositorio.
> Desarrollado con `/trinidad` (investigación de 360°) y `/seeker` (estrategias de testeo).
> Fecha de elaboración: 2026-07-06.
> Fuentes citadas indexadas en [`research/fuentes/registro_fuentes.md`](fuentes/registro_fuentes.md) (F-35 a F-66).

## 0. Propuesta evaluada

> ¿Podemos usar un modelo de cobertura en medicinas que funcione como un frente de atención
> primaria con IA para orientación inicial, que derive algunos casos a un backlog de aprobación
> de entrega de medicinas en farmacias cercanas, y atención humana para emergencias?

Arquitectura del modelo:

```
Usuario ──▶ Triage con IA (orientación primaria)
                  │
        ┌─────────┼──────────────────┐
        ▼         ▼                  ▼
   Caso leve   Caso ambiguo      Caso grave/emergencia
        │      (backlog de           │
        │      aprobación            ▼
        │      humana:          Atención humana
        │      farmacéutico)    inmediata
        ▼         │
   Kit de      ┌───┴───┐
   medicinas   │ aprueba│ deriva
   directo     ▼        ▼
        Delivery en   Atención
        farmacia      humana
        cercana
```

---

## 1. Pregunta base: ¿cómo gestiona su salud el peruano (Lima y provincias)?

### 1.1 La automedicación es la norma, no la excepción

- **68.21%** se automedica con antiinflamatorios, más común en 18-39 años (60.36%), con
  preferencia por marca (66.2%) sobre genérico (16.23%) (Blog USIL/Infobae, 2025 — F-35).
- **3 de cada 10 hogares** compra medicamentos sin receta; algo más frecuente en
  **provincias (36%)** que en Lima (32%); NSE E usa más el botiquín casero (9%) que NSE A/B (4%)
  (Kantar, vía Infobae 2024 — F-39).
- ⚠️ **Tensión entre fuentes**: un tercer dato reporta solo "1 de cada 5" peruanos (Infobae,
  2026 — F-38). Las tres cifras probablemente miden cosas distintas (clase de fármaco
  específica vs. automedicación general vs. nivel hogar/individuo). Tratar como **rango
  20-68%**, no como cifra cerrada.
- Factores asociados a la automedicación no responsable están documentados académicamente
  para población peruana (SciELO, 2021 — F-36, 🟢 peer-reviewed, contexto local directo).

### 1.2 La razón NO es principalmente desconfianza médica

Motivos para evitar al médico: ineficiencia del sistema de salud (**59.34%**), falta de
tiempo (**51.48%**), falta de dinero (**15.74%**), desconfianza en médicos (solo **7.21%**,
la menos citada) (F-38). **Implicación de diseño**: el modelo no compite contra la confianza
en el médico — compite contra la lentitud del sistema.

### 1.3 La fuente de orientación ya es informal y social

Familia/vecinos (**70.49%**), recetas previas (**64.26%**) y **opinión del técnico de
farmacia (22.95%)** son las principales fuentes de consejo para automedicarse (F-38). La
farmacia ya funciona como nodo de triage informal, documentado incluso en consultorios
adyacentes a farmacias durante la pandemia (SciELO Salud Pública — peer-reviewed).

### 1.4 El sistema formal falla en acceso, no solo en trato

- 35% no asiste a un centro de salud por demoras; 13% por distancia (más grave en zonas
  rurales) (F-38).
- **7 de cada 10 peruanos** que necesitaron atención médica en 2022 no la obtuvieron (MINSA,
  Plan Nacional de Telesalud 2026 — F-48).
- Telemedicina en Perú tiene barreras documentadas en 5 capas: tecnológicas, humano-sociales,
  psicosocial-antropológicas, de gobernanza y económicas (perspectivas peer-reviewed sobre
  Perú — F-40, F-41).

---

## 2. Reporte `/trinidad` 360° sobre el modelo propuesto

### Resumen ejecutivo

El peruano ya gestiona su salud así, solo que sin estructura: la farmacia ya es el frente de
atención primaria de facto, y **existe un proyecto de ley activo en el Congreso (08488/2024-CR)**
que propone formalizar casi exactamente la mitad "humana" del modelo (Infobae, 2026). Las tres
pistas **convergen** en que la necesidad y la infraestructura ya existen. **Divergen** en que la
evidencia empírica sobre la capa de IA de orientación es floja — precisión real ~45% en un
estudio, no 90%+ (PMC — estudio Japón, 2024) — y el caso de negocio más parecido a este modelo
(Babylon Health) colapsó exactamente por sobreclamar ahí (The Lancet, 2020).

Formato de cada afirmación de esta sección: **Afirmación** → *Evidencia* (dato/cita) →
**Rigurosidad** (1-5) → **Fuente** (Autor, año). La escala 1-5 traduce la rúbrica A-E de
`cronista` (`research/fuentes/registro_fuentes.md`): **5**=A (peer-reviewed/dato primario),
**4**=B (oficial/regulador), **3**=C (industria/consultora con método propio), **2**=D
(prensa/secundaria sin método propio), **1**=E (opinión sin método verificable).

### 🔬 Pista empírica/teórica

- **68.21% de peruanos se automedica con antiinflamatorios**, más común en 18-39 años
  (60.36%), con preferencia por marca (66.2%) sobre genérico (16.23%).
  *Evidencia:* estudio/encuesta reportado por blog universitario. **Rigurosidad: 2/5.**
  (Blog USIL/Infobae, 2025)
- **La automedicación no responsable en Perú tiene factores asociados documentados
  académicamente** (más allá de la anécdota).
  *Evidencia:* artículo peer-reviewed con metodología explícita, muestra y análisis propios.
  **Rigurosidad: 5/5.** (SciELO Perú, 2021)
- **~1 de cada 5 peruanos recurre a la automedicación**; los motivos dominantes son
  ineficiencia del sistema de salud (59.34%) y falta de tiempo (51.48%), muy por encima de
  la desconfianza médica (7.21%, la razón menos citada). ⚠️ En tensión con el dato anterior
  de 68.21% — probable diferencia de definición (fármaco específico vs. automedicación
  general).
  *Evidencia:* cifra de estudio/encuesta reportada por prensa, sin acceso al método completo.
  **Rigurosidad: 2/5.** (Infobae, 2026)
- **Un symptom-checker de IA en un hospital comunitario japonés tuvo solo 45.1% de precisión
  diagnóstica** en 3 años de uso real, sin mejora en el tiempo.
  *Evidencia:* estudio observacional retrospectivo, peer-reviewed. ⚠️ Validez externa baja
  (un solo hospital). **Rigurosidad: 5/5.** (PMC — estudio Japón, 2024)
- **El symptom-checker finlandés Omaolo logró una validación formal robusta como dispositivo
  médico auditado** (clase IIa, marcado CE) — la diferencia con el caso japonés es la
  rigurosidad de la validación, no la tecnología en sí.
  *Evidencia:* estudio de validación de instrumento + protocolo mixto de validación clínica,
  ambos peer-reviewed. **Rigurosidad: 5/5.** (PMC — estudio Omaolo, 2024; Protocolo Omaolo,
  2023)
- **Medir solo "precisión diagnóstica" es la métrica equivocada para evaluar chatbots
  médicos**; lo que importa es el *outcome* de salud real del paciente.
  *Evidencia:* artículo crítico/teórico peer-reviewed ("Accuracy is inaccurate").
  **Rigurosidad: 5/5.** (PMC — "Accuracy is inaccurate", 2024)
- **La telemedicina peruana enfrenta barreras en 5 capas**: tecnológicas, humano-sociales,
  psicosocial-antropológicas, de gobernanza y económicas.
  *Evidencia:* perspectiva de país peer-reviewed. **Rigurosidad: 5/5.**
  (PMC — perspectiva Perú, 2024)
- **Perú desarrolló telemedicina antes de la pandemia, lo que permitió un escalamiento rápido
  en 2020**; persiste la necesidad urgente de un sistema nacional de telesalud integrado.
  *Evidencia:* artículo peer-reviewed sobre origen e implementación de la telemedicina en
  Perú. **Rigurosidad: 5/5.** (PMC — Telemedicine in Peru, 2024)

| Fuente | Autor, año | Tipo de evidencia | Rigurosidad |
|---|---|---|---|
| Automedicación no responsable, Perú | SciELO Perú, 2021 | Peer-reviewed, Perú específico | 5/5 |
| Symptom checker Finlandia, Omaolo | PMC — estudio Omaolo, 2024 | Validación de instrumento | 5/5 |
| Symptom checker Japón, 45.1% | PMC — estudio Japón, 2024 | Observacional retrospectivo | 5/5 (⚠️ N=1 hospital) |
| Perspectivas telemedicina Perú | PMC — perspectiva Perú, 2024 | Peer-reviewed, contexto país | 5/5 |
| Automedicación 68% | Blog USIL/Infobae, 2025 | Encuesta vía prensa | 2/5 |
| Automedicación 20% | Infobae, 2026 | Encuesta vía prensa | 2/5 |

### 📱 Pista social/mediática — 🌡️ Circulando

- **Un caso viral de cita de EsSalud asignada para 2026 generó indignación masiva** y
  comentarios de usuarios compartiendo casos similares o peores.
  *Evidencia:* cobertura de prensa de un evento viral en redes sociales.
  **Rigurosidad: 2/5.** (El Popular/La República, 2025)
- **Ocho regiones tienen esperas mayores a 90 días** en especialidades de alta demanda: Lima,
  Arequipa, La Libertad, Piura, Lambayeque, Huánuco, Apurímac y Cusco — el problema abarca
  Lima y provincias, no solo provincias.
  *Evidencia:* informe técnico citado por prensa especializada, sin acceso directo al
  documento. **Rigurosidad: 2/5.** (RPP, 2025)
- **94% de médicos encuestados está preocupado por que sus pacientes usen IA para orientación
  médica** — señal de resistencia del lado del proveedor, no solo del paciente.
  *Evidencia:* encuesta de mayo 2025 citada dentro de una revisión académica, sin acceso
  directo a la encuesta primaria. ⚠️ **Rigurosidad: 3/5** (la revisión que la cita es
  peer-reviewed, pero la encuesta original no fue verificada de forma independiente).
  (encuesta médica, 2025, vía PMC — revisión, 2024)
- ⚠️ **Limitación honesta**: no se encontró discusión específica en foros/RRSS peruanos sobre
  "farmacia vs. médico" — se usó la señal social más cercana disponible (indignación viral
  con EsSalud) como aproximación, no como equivalente exacto de esa conversación específica.

### 📈 Pista de negocio

- **El Proyecto de Ley 08488/2024-CR propone que farmacias privadas se integren como puntos
  de atención primaria**: adhesión voluntaria, farmacéutico licenciado obligatorio,
  medicamentos del stock SIS, el farmacéutico monitorea y deriva (no diagnostica), ~1,000 de
  30,000+ boticas como alcance inicial. **Valida directamente** la mitad
  humana+delivery+derivación del modelo propuesto.
  *Evidencia:* cobertura de prensa de un proyecto de ley oficial en debate (fuente primaria =
  Congreso de la República, no accedida directamente). **Rigurosidad: 2/5.** (Infobae, 2026)
- **El Plan Nacional de Telesalud 2026 (MINSA) conecta más de 2,000 establecimientos**, y la
  plataforma Teleatiendo ya registra más de 3 millones de atenciones remotas.
  *Evidencia:* comunicado oficial del ente rector de salud (Resolución Ministerial
  293-2026/MINSA). **Rigurosidad: 4/5.** (MINSA, 2026)
- **InkaFarma+Mifarma ya operan 2,245 farmacias (18% de las boticas del país) con delivery de
  30-45 minutos**, e ingresos de S/.6,327M en 2022 — no hay que construir la red de
  distribución, hay que integrarse a ella.
  *Evidencia:* prensa especializada que reporta cifras de la propia empresa/grupo.
  **Rigurosidad: 2/5.** (Gestión/Peru Retail, 2024)
- **Babylon Health (triage con IA → derivación, valuación pico ~US$4.2B) colapsó en 2023**
  porque su sistema "no ofreció evidencia convincente de desempeñarse mejor que médicos
  humanos... con posibilidad de desempeño significativamente peor". La causa no fue "la IA
  no sirve" sino sobreclamar desempeño sin validación clínica publicada.
  *Evidencia:* evaluación publicada en una revista médica peer-reviewed (The Lancet), citada
  por prensa especializada en negocios. **Rigurosidad: 5/5.** (The Lancet, 2020)
- **Ada Health (misma categoría de producto que Babylon) sigue operando**, con foco en
  investigación clínica peer-reviewed y partnerships farmacéuticos (Novartis, Bayer, Pfizer)
  — el diferenciador de supervivencia es el rigor de validación, no la tecnología.
  *Evidencia:* artículo de reseña de industria sin metodología propia. **Rigurosidad: 2/5.**
  (IntuitionLabs, s.f.)
- **El mercado de salud digital de LatAm crece ~20% CAGR** (~USD 12.82B en 2024 → USD 66.4B
  en 2033), pero Brasil/México/Chile lideran la adopción regional — Perú no aparece como
  referente.
  *Evidencia:* informes de firmas de investigación de mercado, metodología propia no
  auditable. **Rigurosidad: 3/5.** (Grand View Research/Market Data Forecast, 2025)

### ⚖️ Síntesis

**Convergencia fuerte**: el modelo no inventa una necesidad ni una arquitectura nueva — formaliza
con IA algo que ya ocurre informalmente, que el regulador ya diseña por su cuenta (PL 08488;
Infobae, 2026) sin la capa de IA, y para lo cual ya existe infraestructura de distribución
(InkaFarma/Mifarma; Gestión/Peru Retail, 2024) y de telemedicina estatal (Teleatiendo; MINSA,
2026).

**Divergencia crítica**: la pieza específicamente nueva —la capa de IA de orientación— es la
menos madura empíricamente (PMC — estudio Japón, 2024) y tiene el precedente de negocio más
cercano fallando por sobreclamar desempeño sin validación (The Lancet, 2020, sobre Babylon).

**Espacios de mejora identificados**:
1. No lanzar la IA sin estudio de validación de triage propio (sesgo conservador hacia
   sobre-derivar) — lección directa del caso Babylon (The Lancet, 2020).
2. Apoyarse en el PL 08488 (IA como apoyo al farmacéutico, no sustituto) (Infobae, 2026).
3. Vender velocidad, no superioridad clínica — la razón real de la automedicación es tiempo
   (51.48%) e ineficiencia (59.34%), no desconfianza (7.21%) (Infobae, 2026).
4. Transparencia sobre qué decide la IA y qué decide el humano, desde el día uno (mismo
   patrón de brecha actitud-conducta encontrado en la investigación de seguros — ver §5).
5. Canal de bajo ancho de banda / asistido para Sierra y Selva, dadas las barreras de
   telemedicina peruana ya documentadas (PMC — perspectiva Perú, 2024).
6. Aliarse con InkaFarma/Mifarma en vez de construir logística propia (Gestión/Peru Retail,
   2024).

---

## 3. Preguntas de investigación para el piloto (framework RE-AIM)

Estructuradas con RE-AIM (Glasgow, Vogt & Boles, 1999 — F-53), más una capa de **seguridad
clínica** como gate previo y dos capas transversales (regulatorio, negocio).

### 3.0 Seguridad clínica (gate bloqueante)
1. ¿Cuál es la tasa de **falsos negativos** del triage (casos graves clasificados como leves)?
2. ¿Qué tan **conservador** es el sesgo de derivación (sobre-derivar vs. sub-derivar)?
3. ¿El contenido del **kit** (fármacos, dosis, contraindicaciones) es seguro considerando
   comorbilidades comunes que el triage inicial podría no capturar?
4. ¿Qué tasa de **eventos adversos o reconsulta** ocurre en 7-14 días vs. un grupo de
   comparación con atención tradicional?
5. ¿Cómo se **audita retrospectivamente** cada derivación (comité clínico, muestra semanal)?

### 3.1 Reach (alcance)
6. ¿Qué perfil de usuario usa efectivamente el flujo vs. el universo que lo necesita?
7. ¿Hay brecha sistemática por región (Lima vs. Sierra/Selva, `acceso_digital` bajo)?
8. ¿Qué proporción de la demanda de automedicación real el flujo logra formalizar?

### 3.2 Effectiveness (efectividad)
9. ¿El kit **resuelve** el episodio o solo lo pospone (reconsulta a 30 días)?
10. ¿El tiempo total del flujo es efectivamente más rápido que la alternativa (en horas, no
    cualitativamente)?
11. ¿Mejora algún **desenlace de salud medible**, o solo la percepción de conveniencia?

### 3.3 Adoption (adopción, ambos lados)
12. ¿Qué determina la aceptación real del kit sin ver a un médico (intención vs. conducta)?
13. ¿Qué tasa de **anulación** del farmacéutico sobre la sugerencia de la IA existe?
14. ¿Los usuarios **entienden** qué decide la IA y qué decide el humano?
15. ¿Hay resistencia del lado médico/farmacéutico al flujo?

### 3.4 Implementation (fidelidad de implementación)
16. ¿Cuánto tarda realmente la aprobación del backlog (SLA objetivo vs. real)?
17. ¿Qué tasa de **quiebre de stock** del kit ocurre en las farmacias aliadas?
18. ¿Qué proporción deriva a atención humana de emergencia, y cuál es el tiempo de respuesta?
19. ¿Se registra la **trazabilidad completa** (lote, historia clínica, aprobador) de forma
    consistente en la práctica real?

### 3.5 Maintenance (sostenibilidad)
20. ¿La precisión del triage se degrada o mejora con más uso?
21. ¿El costo por caso resuelto es sostenible al escalar?

### 3.6 Transversal — Regulatorio
22. ¿El flujo encaja dentro del marco del PL 08488 (monitorea/deriva, no diagnostica) o la IA
    excede ese rol legal?
23. ¿Quién es responsable legalmente si la IA clasifica mal un caso?

### 3.7 Transversal — Negocio
24. ¿Cuál es el **costo unitario real** por caso vs. una consulta tradicional evitada?
25. ¿El modelo de partnership con farmacias es económicamente viable a los volúmenes del piloto?

---

## 4. Estrategias de testeo (investigación `/seeker`)

Metodologías de validación con evidencia empírica/teórica de que funcionan, mapeadas contra
las 25 preguntas de investigación para maximizar cobertura con el menor número de estudios.

### E1 — Silent trial / shadow mode (fase 0, obligatoria primero)

Desplegar la IA en paralelo a la operación real sin que sus predicciones influyan en ninguna
decisión; se comparan contra el desenlace real o el juicio humano ciego. Roadmap de 3 etapas:
desarrollo exploratorio → **silent trial** → evaluación clínica prospectiva. Para modelos de
alto riesgo, correr mínimo **60-90 días** (variación estacional + fin de semana vs. entre
semana). No requiere consentimiento porque no influye en la atención (F-56, F-57 — 🟢 scoping
review + paper de framework, peer-reviewed).

**Resuelve**: RQ1, RQ2, RQ4 (parcial — el desenlace real solo se mide en la etapa 3 del
roadmap), RQ20 (si se repite periódicamente).

### E2 — Diseño híbrido efectividad-implementación tipo 2 (Curran)

Prueba la efectividad clínica y la viabilidad de implementación como **objetivos co-primarios
simultáneos**, en vez de secuenciales — acelera la traducción a la práctica real. Aplicado con
éxito en atención primaria (F-55, terapia breve tipo 2). Revisión metodológica que extiende el
framework (F-54).

**Resuelve**: RQ9, RQ10, RQ11, RQ16, RQ17, RQ18, RQ19.

### E3 — Diseño escalonado (stepped-wedge) por clusters de farmacias/regiones

Rollout secuencial y aleatorizado por cluster (distrito o cadena de farmacia): cada cluster
pasa de control (atención tradicional) a intervención (flujo con kit) en orden aleatorio hasta
que todos lo reciben. Permite inferencia causal sin negar el servicio a nadie permanentemente
— más aceptable en un contexto de servicio público de salud (F-58, F-59). ⚠️ **Riesgo
metodológico a declarar**: el diseño confunde por tiempo (el control siempre se mide antes
cronológicamente); requiere ajuste por tendencia temporal.

**Resuelve**: RQ6, RQ7 (al escalonar por región, genera comparación Lima vs. provincias de
forma natural), RQ9, RQ10, RQ11.

### E4 — Medición de sesgo de automatización con benchmark externo

Registrar cada vez que el farmacéutico aprueba, modifica o rechaza la sugerencia de la IA, y
comparar contra la tasa base documentada en sistemas clínicos: **5.2%-7%** de sesgo de
automatización (aceptar una sugerencia errónea) en radiología/patología (F-60); estudio
específico de sesgo de automatización en **soporte de decisión de prescripción** — análogo
directo al backlog farmacéutico (F-61).

**Resuelve**: RQ13, RQ2 (interpretación con denominador de comparación).

### E5 — Validación dual estilo FDA SaMD (técnica + clínica)

Separar explícitamente validación **técnica** (¿el software procesa datos con precisión y
reproducibilidad?) de validación **clínica** (¿el output es clínicamente significativo en el
contexto real?) — el error común es validar solo la primera (F-62). Usar el protocolo mixto
de validación de Omaolo (dispositivo médico clase IIa, marcado CE) como plantilla concreta
(F-63).

**Resuelve**: RQ1, RQ2, RQ22 (parcial — lógica trasladable aunque el marco peruano sea distinto).

### E6 — Medición conductual (logs) en paralelo al autorreporte

En vez de solo preguntar "¿confiarías en este flujo?", instrumentar el sistema para registrar
uso real (tasa de finalización, abandono, reconsulta) y comparar contra la intención declarada
en encuestas. Los datos de log son más válidos que el autorreporte para conducta real — el
autorreporte está sesgado por deseabilidad social y errores de memoria (F-65). Mismo patrón ya
usado para calibrar `disposicion_compartir_datos_pricing` en `lapuerta`.

**Resuelve**: RQ12, RQ14 (combinado con entrevista cualitativa).

### E7 — Marco CFIR para barreras/facilitadores de implementación

Mientras RE-AIM mide **si** funciona, CFIR explica **por qué** funciona o falla en 5 dominios:
características de la intervención, contexto externo/interno, características de los
individuos, proceso de implementación (F-64). Complementa a RE-AIM — práctica estándar
reciente en salud digital.

**Resuelve**: RQ7 (contexto externo/interno explica la brecha Sierra/Selva), RQ15
(características de los individuos explica resistencia médica), RQ16-RQ19.

### E8 — Micro-costing + estudio de tiempos y movimientos

Descomponer cada paso del flujo (triage IA, revisión farmacéutica, picking, entrega) en
actividades discretas, medir tiempo/recursos por observación directa, valorizar — método
estándar para costear intervenciones nuevas con alta variabilidad entre proveedores (F-66).
⚠️ La literatura reconoce que faltan guías estandarizadas del método — documentar con cuidado
para evitar heterogeneidad metodológica.

**Resuelve**: RQ16 (parcial), RQ24, RQ25.

### E9 — Formulario acotado antes de escalar (recomendación de diseño, no hallazgo de literatura)

Empezar el silent trial y el stepped-wedge con un formulario de kit muy acotado (2-3
condiciones de bajísimo riesgo) antes de expandir — reduce el "blast radius" de cualquier
falla del triage mientras se acumula evidencia real. Implicación práctica de combinar E1+E3+E5,
no una fuente citada aparte.

### Tabla de cobertura (estrategia → preguntas resueltas)

| Estrategia | RQs que resuelve |
|---|---|
| E1 Silent trial | 1, 2, 4 (parcial), 20 |
| E2 Híbrido tipo 2 | 9, 10, 11, 16, 17, 18, 19 |
| E3 Stepped-wedge | 6, 7, 9, 10, 11 |
| E4 Sesgo de automatización | 2, 13 |
| E5 Validación dual FDA-style | 1, 2, 22 (parcial) |
| E6 Logs vs. autorreporte | 12, 14 |
| E7 CFIR | 7, 15, 16, 17, 18, 19 |
| E8 Micro-costing | 16 (parcial), 24, 25 |
| E9 Formulario acotado | reduce riesgo global de E1+E3 |

### Brechas que NO resuelve ninguna estrategia de testeo (honestidad epistemológica)

- **RQ3** (seguridad del kit con comorbilidades): requiere panel de farmacólogos/protocolo de
  contraindicaciones y revisión de comité de ética/DIGEMID — no es un diseño de estudio
  poblacional.
- **RQ21** (sostenibilidad de precisión en el tiempo, a escala completa): excede el alcance de
  un "piloto" — requiere un programa de **vigilancia post-mercado** continuo, distinto de un
  testeo acotado.
- **RQ23** (responsabilidad legal): es un análisis legal/simulacro de casos con asesoría
  jurídica y DIGEMID/MINSA, no una metodología de investigación en salud.

No forzar una metodología de estudio donde lo que se necesita es un mecanismo distinto
(panel clínico, vigilancia continua, consulta legal) — declarar la brecha en vez de simular
cobertura que no existe.

---

## 5. Conexión con el modelo `lapuerta`

Este documento es la segunda vez que aparece el mismo patrón de diseño en esta línea de
investigación: la confianza abstracta en la IA no se traduce en aceptación real sin
transparencia específica sobre su rol. La primera vez apareció al investigar modelos de
seguros rentables (brecha actitud-conducta en telemática/UBI, caso Lemonade) y motivó la
variable `disposicion_compartir_datos_pricing` (v1.3) en
[`research/personas/generador/matriz_usuarios_sinteticos.md`](personas/generador/matriz_usuarios_sinteticos.md).
Aquí reaparece en salud (94% de médicos preocupados por el uso de IA médica por pacientes,
caso Babylon Health). Dos apariciones independientes del mismo principio lo convierten en un
principio de diseño transversal del proyecto, no una coincidencia puntual.

---

## 6. Limitaciones generales

- La cifra de automedicación varía fuertemente entre fuentes (20%-68%); no hay un dato único
  confiable.
- La pista social no encontró discusión específica en foros/RRSS peruanos sobre "farmacia vs.
  médico"; se usó la señal social más cercana disponible.
- Ninguna evidencia de precisión de symptom-checkers citada fue validada en población
  **peruana** específicamente (toda es de Finlandia/Japón/Portugal).
- No se accedió al texto completo del Proyecto de Ley 08488 ni a su estado de trámite más
  allá de marzo 2026 — verificar directamente en el portal del Congreso antes de decisiones
  de producto.
- Las estrategias de testeo (§4) están validadas en la literatura de salud digital global;
  ninguna fue aplicada específicamente a un flujo idéntico (triage IA + backlog farmacéutico +
  delivery) en Perú — son la mejor práctica disponible, no una garantía de que funcionen
  igual en este contexto.

---

## Conexiones

- [[mecanismos-seguros-salud|Mecanismos de seguros de salud]] — este node es el diseño concreto
  para Perú; ese node aporta el marco global de mecanismos (capitación, atención primaria,
  Singapur/NHS) que valida y matiza este diseño (ver su §3 y su síntesis §4).
- [[seguros-comportamiento-mundo-peru|Comportamiento y mercado global de seguros]] — §1.2-1.3 y
  §2 de ese node (confianza, sesgos conductuales) sustentan las decisiones de diseño de este
  documento.
- [[glosario-seguro-salud-peru|Glosario de seguro de salud en Perú]] — vocabulario base para la
  comunicación del flujo con usuarios finales.
