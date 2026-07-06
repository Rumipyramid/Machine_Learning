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
que propone formalizar casi exactamente la mitad "humana" del modelo. Las tres pistas
**convergen** en que la necesidad y la infraestructura ya existen. **Divergen** en que la
evidencia empírica sobre la capa de IA de orientación es floja (precisión real ~45% en un
estudio, no 90%+), y el caso de negocio más parecido a este modelo (Babylon Health) colapsó
exactamente por sobreclamar ahí.

### 🔬 Pista empírica/teórica

- **Precisión real de symptom-checkers, no de laboratorio**: un symptom-checker de IA en un
  hospital comunitario en Japón tuvo solo **45.1%** de precisión diagnóstica en 3 años de uso
  real, sin mejora en el tiempo (F-43). En cambio, el instrumento finlandés **Omaolo** logró
  una validación formal robusta como **dispositivo médico auditado** (clase IIa, marcado CE)
  (F-42, F-63) — la diferencia es la rigurosidad de validación, no la tecnología en sí.
- **La literatura crítica advierte sobre la métrica misma**: "Accuracy is inaccurate" (F-44)
  argumenta que medir solo precisión diagnóstica es la métrica equivocada; lo que importa es
  el *outcome* de salud real del paciente.

| Fuente | Tipo de evidencia | Validez/Confiabilidad | Peso |
|---|---|---|---|
| SciELO — automedicación no responsable, Perú (F-36) | Peer-reviewed, Perú específico | ✅ contexto local directo | 🟢 Alto |
| Symptom checker Finlandia, Omaolo (F-42, F-63) | Estudio de validación de instrumento | ✅ dispositivo médico auditado | 🟢 Alto |
| Symptom checker Japón, 45.1% (F-43) | Observacional retrospectivo, 3 años | ⚠️ precisión moderada-baja, un solo hospital | 🟡 Medio |
| Perspectivas telemedicina Perú (F-40, F-41) | Peer-reviewed, contexto país | ✅ directamente aplicable | 🟢 Alto |
| Automedicación 68% vs. 20% (F-35, F-38) | Encuesta/estudio vía prensa | ⚠️ tensión entre fuentes, método no verificado | 🟡 Medio |

### 📱 Pista social/mediática — 🌡️ Circulando

- Un caso viral de cita de EsSalud asignada para **2026** generó indignación masiva y
  comentarios de casos similares o peores (F-45).
- Regiones con esperas **>90 días**: Lima, Arequipa, La Libertad, Piura, Lambayeque, Huánuco,
  Apurímac y Cusco (F-46) — el problema abarca Lima y provincias, no solo provincias.
- **Riesgo a vigilar**: 94% de médicos encuestados está preocupado por que sus pacientes usen
  IA para orientación médica — señal de resistencia del lado del proveedor, no solo del
  paciente.
- ⚠️ Limitación honesta: no se encontró discusión específica en foros/RRSS peruanos sobre
  "farmacia vs. médico" — se usó la señal social más cercana disponible (indignación con
  EsSalud), declarada como aproximación, no como equivalente exacto.

### 📈 Pista de negocio

- **Proyecto de Ley 08488/2024-CR** (en debate): farmacias privadas como puntos de atención
  primaria — adhesión voluntaria, farmacéutico licenciado obligatorio, medicamentos del stock
  SIS, el farmacéutico **monitorea y deriva** (no diagnostica), ~1,000 de 30,000+ boticas
  como alcance inicial (F-47). **Valida directamente** la mitad humana+delivery+derivación
  del modelo propuesto.
- **Plan Nacional de Telesalud 2026** (MINSA): Red Nacional conecta >2,000 establecimientos;
  plataforma **Teleatiendo** ya registra >3 millones de atenciones remotas (F-48).
- **Infraestructura de delivery ya existe a escala**: InkaFarma+Mifarma suman 2,245 farmacias
  (18% de boticas del país), delivery de 30-45 min operativo, ingresos S/.6,327M en 2022
  (F-49). No hay que construir la red — hay que integrarse a ella.
- ⚠️ **Precedente de negocio que colapsó**: **Babylon Health** (valuación pico ~US$4.2B)
  construyó esta misma arquitectura (triage IA → derivación) y quebró en 2023. El Lancet
  concluyó que su sistema "no ofreció evidencia convincente de desempeñarse mejor que
  médicos humanos... con posibilidad de desempeño significativamente peor" (F-50). La causa
  no fue "la IA no sirve" sino **sobreclamar sin validación clínica publicada**. Ada Health
  (misma categoría) sigue operando por mantener validación clínica peer-reviewed (F-51).
- Mercado de salud digital LatAm crece ~20% CAGR, pero Perú no es líder regional (Brasil/
  México/Chile sí) — oportunidad y a la vez falta de comparables locales (F-52).

### ⚖️ Síntesis

**Convergencia fuerte**: el modelo no inventa una necesidad ni una arquitectura nueva — formaliza
con IA algo que ya ocurre informalmente, que el regulador ya diseña por su cuenta (PL 08488) sin
la capa de IA, y para lo cual ya existe infraestructura de distribución (InkaFarma/Mifarma) y de
telemedicina estatal (Teleatiendo).

**Divergencia crítica**: la pieza específicamente nueva —la capa de IA de orientación— es la
menos madura empíricamente y tiene el precedente de negocio más cercano fallando por sobreclamar
desempeño sin validación (Babylon).

**Espacios de mejora identificados**:
1. No lanzar la IA sin estudio de validación de triage propio (sesgo conservador hacia
   sobre-derivar).
2. Apoyarse en el PL 08488 (IA como apoyo al farmacéutico, no sustituto).
3. Vender velocidad, no superioridad clínica (la razón real de la automedicación es tiempo,
   no desconfianza).
4. Transparencia sobre qué decide la IA y qué decide el humano, desde el día uno (mismo
   patrón de brecha actitud-conducta encontrado en la investigación de seguros — ver §5).
5. Canal de bajo ancho de banda / asistido para Sierra y Selva (no solo app/chat).
6. Aliarse con InkaFarma/Mifarma en vez de construir logística propia.

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
