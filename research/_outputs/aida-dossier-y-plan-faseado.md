# AIDA — Dossier completo y plan de intervención faseado

**Documento de consolidación.** v2.0 · 2026-08-20

> ⭐⭐ **v2.0 — entrevista con la PO de AIDA.** Radille, dueña de las funcionalidades asociadas a la
> FFVV, respondió sobre objetivos, alcance, medición y gobierno. **Resuelve cinco preguntas abiertas y
> confirma tres hipótesis centrales del diagnóstico desde la propia capacidad.** Lo esencial:
> el objetivo declarado es **uno** (consolidar información y reducir tiempo de búsqueda), **el uso de
> AIDA está en la variable del asesor**, **es RAG puro** sobre SharePoint, **el feedback negativo ya
> está trazado a documentación desactualizada**, **no hay roadmap** y los cambios entran por solicitud
> del negocio con captura de valor — pero ⭐ **cargar base de conocimiento es el camino barato y ya
> hay un canal abierto**. Detalle completo en §19 del node.
CoE Diseño Estratégico · Behavioral Design · RIMAC Seguros

> **Qué es este documento.** Reúne en un solo lugar todo lo que el proyecto sabe sobre **AIDA** —el
> copiloto de IA del asesor de Vida— y la **propuesta de intervención por fases**. Está pensado para
> leerse de corrido por alguien que llega nuevo al tema, y para consultarse por partes por alguien
> que ya está dentro.
>
> **Qué NO es.** No es la fuente de verdad. Los nodes lo siguen siendo, y ante cualquier discrepancia
> mandan ellos:
> - `_nodes/diagnostico-copiloto-ai-asesor-vida-rimac.md` (v2.2) — estado interno y decisiones
> - `_nodes/arquitectura-conocimiento-agentes-copilot.md` (v1.3) — evidencia externa
> - `_outputs/release-1-base-conocimiento-aida.md` (v2.2) — el Release 1 ejecutable
> - `_outputs/protocolo-interrogacion-aida-vida.md` (v0.4) — el instrumento de diagnóstico
>
> **Nivel de certeza.** Cada afirmación viene marcada: ✅ confirmado · 🟡 probable, con evidencia
> parcial · ⚠️ hipótesis o autorreporte · ⛔ descartado. **Nada aquí es dato de campo cerrado** — la
> auditoría estructurada y el shadowing están en curso.

---

## Índice

**Parte I · Qué es AIDA**
1. Identidad, plataforma y alcance
2. Lo que AIDA **no** es
3. Las tres funciones declaradas y el estado real de cada una
4. Dónde vive AIDA: los seis frentes del asesor
5. Los agentes desplegados y los prototipos existentes
6. Lo que sabemos del uso real

**Parte II · El diagnóstico**
7. La taxonomía de fallas y la prueba que las separa
8. La biblioteca: qué hay y por qué rompe
9. Por qué ordenar rinde más que reentrenar
10. La contradicción está aguas arriba
11. La barrera de actualización de producto
12. Qué debe hacer el asesor, y qué de eso está verificado
13. Las restricciones duras

**Parte III · El plan faseado**
14. Vista general y regla de secuencia
15. Fase 1 · Release 1 — cerrar la brecha de la promesa
16. Fase 2 · Extender a los demás ramos
17. Fase 3 · Mejorar el motor
18. Fase 4 · Entrenamiento, casuística y prototipos
19. Fase 5 · Arquitectura de agentes
20. En paralelo · Recuperar a quien ya se fue
21. Lo que el plan **no** arregla

**Parte IV · Cómo se mide**
22. Los instrumentos de diagnóstico
23. El diseño de validación

**Parte V · Estado abierto**
24. Preguntas abiertas P1–P15
25. Insumos y evidencia
26. Limitaciones

---

# Parte I · Qué es AIDA

## 1. Identidad, plataforma y alcance

| Atributo | Estado |
|---|---|
| **Qué es** | Copiloto conversacional de IA para la fuerza de ventas. ✅ **Ya desplegado en producción** |
| **Nombre interno** | "AIDA FFVV" |
| **Plataforma** | ✅ **Google.** No es Microsoft Copilot |
| **Alcance** | ✅ **Multi-ramo, un agente por ramo.** Vida es uno de varios |
| **Dueño** | ⚠️ Tiene PO declarada; el gobierno completo (quién decide qué) sin mapear — **P7** |
| **Medición previa** | ⚠️ Sin confirmar que exista telemetría accesible — **P4/P5** |
| **Sandbox** | ⛔ **No existe.** Ninguna funcionalidad nueva se puede testear dentro de AIDA |

### 1.1 La corrección de plataforma, y por qué importa tanto

Durante buena parte del proyecto se asumió que AIDA estaba construida sobre **Microsoft Copilot**.
Ese supuesto venía del brief inicial y condicionó el diagnóstico entero.

**La primera señal en contra la dio la propia herramienta:** al auto-interrogarla declaró la función
`transfer_to_agent`, que es de **Google ADK**, no de Copilot Studio. En su momento se registró como
hipótesis y se suspendieron los límites técnicos de Copilot.

✅ **Confirmado en la reunión con la jefatura (agosto 2026): AIDA corre sobre Google.**

**Consecuencias, y son de fondo:**

| Qué | Antes | Ahora |
|---|---|---|
| Techo de 36.000 caracteres por archivo | Vigente | ⛔ **No aplica** |
| Techo de 7 MB / 200 MB por licencia | Vigente | ⛔ **No aplica** |
| Presupuesto de recuperación ≤300 páginas | Vigente | ⛔ **No aplica** |
| Reglas de formato y redacción (un tema por documento, sin tablas, troceado por encabezado) | Vigentes | ✅ **Siguen vigentes** |
| Capacidad de inferencia esperada | Baja (por supuesto) | ⚠️ **Desconocida, probablemente mayor** — hay que medirla |

⭐ **La distinción crítica:** los **números** eran de Microsoft y cayeron. Las **reglas** no son de
Microsoft — son propiedades de cómo funciona la recuperación aumentada, sostenidas por evidencia
arbitrada independiente del fabricante (ICCV, ACL, ICLR, SIGIR, EMNLP). Esas se sostienen intactas.

⚠️ **Advertencia de método que deja este episodio:** el supuesto "es Copilot, luego infiere poco"
estuvo silenciosamente condicionando qué se le pedía a la herramienta. **La capacidad de inferencia
ahora se mide, no se supone.** Es parte de lo que justifica el bloque de auditoría con LLM.

⚠️ **Y una revisión pendiente que este documento hace explícita:** la evaluación de formato del
Playbook (§8.3 más abajo) se construyó contra el techo de 36.000 caracteres. **Ese criterio ya no
aplica.** La recomendación de partir por bloque y des-tabular **sobrevive por otras razones** —un
tema por documento, calidad del fragmento recuperado, competencia entre documentos— pero el umbral
numérico específico hay que recalcularlo contra los límites reales del servicio Google, que todavía
no conocemos (**P15**).

### 1.2 Contexto organizacional

RIMAC tiene un **partnership con Google**, y está evaluando —de forma tentativa y no cerrada— llevar
la ofimática completa de la organización a Google. Ese análisis lo conduce Miguel Portugal.

⭐ **Consecuencia estratégica:** el trabajo sobre AIDA **rema a favor** de una dirección que la
organización ya está considerando, no en contra. Es un argumento útil frente a los dueños de la
capacidad, y conviene usarlo como tal.

---

## 2. Lo que AIDA **no** es

⚠️ **Esta distinción se confundió dentro del propio repositorio hasta el 2026-08-14 y hay que
sostenerla activamente.**

| | **AIDA** | **El prototipo del Plan Piloto** |
|---|---|---|
| Plataforma | Google | Claude |
| Estado | ✅ Desplegada en producción, en manos de la FFVV | Prototipo, no desplegado |
| Alcance | Multi-ramo corporativo | Vida, para el piloto |
| Dueño | Área de la capacidad | CoE Diseño Estratégico |
| Qué diagnostica este proyecto | ✅ **Esta** | ❌ No |

**Por qué importa operativamente:** el indicador del Plan Piloto *"consultas sin respuesta
satisfactoria y temas más consultados"* **mide el prototipo, no AIDA.** Usarlo como corpus de fallas
de AIDA es un error de atribución que el repositorio ya cometió una vez.

⭐ **Y hay una oportunidad escondida en esta distinción.** Hoy el prototipo se lee como una
herramienta que compite con AIDA. **No debería competir: dado que no hay sandbox, es el único banco
de pruebas disponible.** Ver §18.4.

---

## 3. Las tres funciones declaradas y el estado real de cada una

> ⭐⭐ **ACTUALIZADO (v2.0) — ahora hay una tercera fuente, y es la mejor: la PO.** Lo que sigue
> mantiene la estructura de tres funciones porque así estaba levantada de documentación, pero
> **la dueña de la capacidad declara un objetivo, no tres.** Ver §3.0.

## 3.0 ✅ El objetivo declarado por la PO — la vara real

Preguntada directamente, Radille confirmó textualmente:

> *"¿Podríamos decir que fue para un tema de **consolidación de información** para el asesor y
> **reducir tiempos de búsqueda**?"* — **"Ese fue el objetivo."**

**Y tres funcionalidades concretas de AIDA Sales:**
1. **Genera speeches de venta personalizados**
2. **Genera cuadros comparativos entre planes**
3. **Comparte los brochures** cargados, para que el asesor no los busque en distintos lugares

⭐⭐ **Esto reordena la lectura de la brecha.** Lo que el diagnóstico trataba como *una de tres
promesas* —centralizar el conocimiento— **es LA promesa**. Las otras dos son funcionalidades a su
servicio. La brecha es más seria de lo que estaba presentada, y a la vez **más fácil de conversar**:
ataca exactamente lo que la capacidad se propuso hacer.

⭐ **También resuelve P13 al revés de como se planteó.** La hipótesis era que AIDA nació para *soporte
comercial*. **No: nació para consolidación.** El soporte comercial se construyó encima.

**Y hay dos AIDAs, no una:**

| | **AIDA Service** | **AIDA Sales** |
|---|---|---|
| **Para** | Central de Consultas | **FFVV**, BI Pro, Hub, piloto canal BIF |
| **Qué hace** | Procedimientos, consulta por DNI del cliente | Información de producto para la venta |
| **Arquitectura** | La misma en ambas | La misma |
| **Base de conocimiento** | Independiente, no conversan | Independiente, no conversan |

⚠️ **La PO no confirmó los cinco subagentes por ramo** que la auto-interrogación declaró. Describe
segmentación por **caso de uso y canal**. No se contradicen necesariamente, pero **el autorreporte
queda sin confirmar** — se resuelve con el diagrama de arquitectura, no preguntándole a AIDA (**P16**).

---

## 3.1 Las tres funciones como estaban levantadas

Salen de dos fuentes que tienen una virtud específica: permiten evaluar la herramienta **sin
confrontar la palabra de ninguna persona**.

1. **La documentación de RIMAC** sobre el proyecto AIDA.
2. **Lo que la propia herramienta responde** cuando se le pregunta para qué sirve.

| # | Función declarada | Estado real | Detalle |
|---|---|---|---|
| **1** | Centralizar el conocimiento y los recursos del asesor | 🔴 **Sin avance sustantivo** | El conocimiento sigue viviendo en el cartapacio, en la capa y en el onboarding. En recursos, **Sales Coach no está integrado de ninguna forma** |
| **2** | Dar soporte comercial | 🟡 **Parcial** | La función existe: se le dieron lógicas para construir mensajes recomendados a partir de una base. **El problema no es la función — es el material del que los construye** |
| **3** | Consultar información oficial y actualizada de producto | 🟡 **Arquitectura sí, contenido no** | Existe la consulta a un repositorio documental. La información no está seteada en la forma que el agente puede leer |

### 3.1 La hipótesis sobre el origen del desalineamiento

⚠️ **Hipótesis de la jefatura (P13), no dato:** AIDA **nació para la función 2** —soporte comercial—
y las otras dos se le agregaron después.

El argumento es de coherencia de diseño: si las tres hubieran sido premisa desde el inicio, la
orquestación y el gobierno del conocimiento serían otros. Lo que se observa —una capa de soporte
comercial funcionando sobre un repositorio sin gobierno— es más consistente con una función original
que creció que con tres funciones diseñadas juntas.

**Por qué importa:** decide si el diagnóstico está midiendo contra una promesa real o contra una
promesa retrospectiva. No cambia qué hay que arreglar; cambia cómo se conversa.

### 3.2 ⚠️ El riesgo epistémico de usar la auto-descripción como vara

Es elegante políticamente, pero **es autorreporte**. Un modelo al que se le pregunta por su propósito
produce una narración plausible —leyendo su prompt de sistema, o reconstruyendo un patrón genérico—
y **no distingue entre ambas al responder**.

**Mitigación:** la documentación manda, la auto-descripción corrobora.

⭐ **Y si divergen, esa divergencia es un hallazgo gratis** —la herramienta no sabe para qué es— que
sigue sin confrontar a nadie.

---

## 4. Dónde vive AIDA: los seis frentes del asesor

El asesor de Vida opera hoy en seis frentes simultáneos:

| # | Frente | Qué hace ahí | ¿Es IA? |
|---|---|---|---|
| 1 | **Salesforce** | Registra información de gestión | No |
| 2 | **AIDA** | Consulta y soporte durante la venta | ✅ Sí |
| 3 | **Material físico** | Cartapacio, fichas, folletos para el cliente | No |
| 4 | **Agente de suscripción** | Apoyo en procesos de suscripción | ✅ Sí |
| 5 | **Sales Coach** | Entrenamiento en fases iniciales | ✅ Sí |
| 6 | **Jefatura** | Feedback directo | No |

**El lineamiento del diagnóstico sistémico:** el modelo de venta debe desplegarse **multimodalmente**
(en todos los frentes), y **el copiloto debe concentrar la mayoría de las funciones front** del
asesor.

### 4.1 Las tres capas que hay que separar para no romper nada

La palabra "multimodal" y el mandato "concentrar" parecen contradecirse. No lo hacen si se separan
tres capas distintas:

| Capa | Decisión | Por qué |
|---|---|---|
| **Distribución del modelo de venta** | **Multimodal** — vive en selección, entrenamiento, pautas, sistemas del canal y el copiloto | Es un modelo de referencia transversal: una fuente canónica, N instanciaciones |
| **Interfaz del asesor** | **Consolidar** — una sola puerta de entrada | Reduce la carga cognitiva de saber cuál herramienta usar para qué |
| **Bases de conocimiento** | ⛔ **NO consolidar** | Juntarlas empeora las respuestas — ver §8.2 |

**Qué se consolida y qué no, frente por frente:**

| Frente | Decisión | Razón |
|---|---|---|
| AIDA | **Es la puerta** | Ya es la superficie conversacional en producción |
| Agente de suscripción | **Detrás de la puerta**, base separada | Dominio y gobierno distintos; mezclarlo sube el riesgo donde el error es más caro |
| Sales Coach | **Detrás de la puerta**, modo separado | Práctica y producción son modos distintos (ver §18) |
| Salesforce | **Se consolida la interacción, no el sistema** | Que el copiloto registre por el asesor; el CRM sigue siendo el sistema de registro |
| Material físico | **No se absorbe** | Otra audiencia: el cliente |
| Feedback de jefatura | **No se absorbe** | Su valor no es informacional |

### 4.2 ⚠️ Dos advertencias de secuencia

**1 · La puerta única sobre bases rotas empeora el diagnóstico.** Si se pone un orquestador delante
de agentes cuya calidad no se auditó, el asesor deja de saber **cuál** falló — y se pierde la señal
que hoy sí existe ("AIDA no contesta bien"). **La auditoría va antes que cualquier consolidación de
interfaz.**

**2 · El entrenamiento no sobrevive al contacto con una herramienta rota.** El asesor nuevo se
entrena en Sales Coach y después trabaja en AIDA. Pero el mayor efecto de un copiloto se da
precisamente en los novatos (+34%, F-476): **la herramienta de la que más depende un asesor nuevo es
la de producción, no la de entrenamiento.** Si AIDA falla, el novato aprende un modelo que después no
puede ejecutar. **Arreglar AIDA es precondición para que el valor de Sales Coach se materialice.**

---

## 5. Los agentes desplegados y los prototipos existentes

### 5.1 Lo que AIDA declara ser

⚠️ **Autorreporte, no inspección de configuración.** Hipótesis a triangular.

Un **Coordinador Principal** con **cinco subagentes**: `SaludAgent`, `VehicularAgent`,
`VidaFinancieroAgent`, `GeneralOpsAgent`, `SalesCoachAgent`. Tres lógicas declaradas —clasificación y
enrutamiento, modo coach con contexto, y **reglas operativas estrictas que le prohíben responder de
memoria en temas técnicos**— y una función de delegación, `transfer_to_agent`.

**Cinco hallazgos, dos de los cuales cambiaron el diagnóstico:**

**H1 · AIDA no es el copiloto de Vida: es multi-ramo.** Solo 1 de 5 subagentes es Vida.
⭐ Esto convierte **el error de ruteo entre ramos en candidato principal** de la queja "no da la
información adecuada": una respuesta correcta del ramo equivocado es, para el asesor,
indistinguible de un error de conocimiento.

**H2 · La arquitectura recomendada ya existe.** Coordinador + subagentes por dominio con fuentes
separadas es exactamente el patrón que la literatura recomienda. ⭐ **El arreglo no es construir el
ruteo — el ruteo existe. Lo que falta es medir si acierta.**

**H3 · Los productos que AIDA nombra no coinciden con el portafolio vigente.** Declara "Flexivida,
Inversión Global, Renta Garantizada, UltraCash"; la matriz vigente desde 01/01/2025 tiene **VFP, Plan
Vida Flexible, Vida Contigo/VAG y Vida Temporal Total**.
> ⚠️ **Corrección importante:** la primera lectura fue que AIDA estaba anclada a material de 2022.
> **Falso, o al menos injusto: el propio Playbook —la fuente canónica— también dice "Flexivida".**
> Es más probable que **AIDA esté reproduciendo fielmente su fuente**. El desfase existe, pero está
> **aguas arriba**. Mueve la responsabilidad del agente al catálogo.

**H4 · `transfer_to_agent` es de Google ADK.** ✅ Confirmado después. Ver §1.1.

**H5 · `SalesCoachAgent` vive dentro de AIDA**, pero Sales Coach figura como frente separado en el
mapa de seis. O son dos cosas homónimas, o el mapa se corrige. ⚠️ Sin resolver.

### 5.2 Los dos prototipos de Behavioral Design

✅ **El equipo ya construyó 2 prototipos.**

**Prototipo A — práctica agéntica de objeciones (sobre Copilot).** El asesor practica con **casos
ficticios de objeciones**, recibe consejos y **es puntuado**. Incluye la capacidad de guardar los
puntajes, **reportarlos a la jefatura** y **retroalimentar a AIDA**.

**Prototipo B — ⚠️ sin confirmar (P11).** El brief dice "2 prototipos" y describe uno. Se asume que
el segundo es el prototipo sobre Claude del Plan Piloto, **pero no está verificado**. Si es un tercer
artefacto distinto, hay un inventario incompleto de lo que el equipo ya construyó.

⭐ **Consecuencia inmediata:** dado que **no hay sandbox en AIDA**, estos prototipos dejan de ser
curiosidades y pasan a ser **la única infraestructura de prueba de funcionalidad que existe.**

---

## 6. Lo que sabemos del uso real

Fuentes: encuesta a 19 asesores, taller de manejo de objeciones (36 invitados / 30 asistentes), y la
lectura del equipo.

### 6.1 ⭐ El hallazgo más filoso: uso alto y utilidad baja, a la vez

**La mayoría de asesores declara que usa AIDA. La mayoría declara que no le resulta útil.**

Las dos cosas solo conviven de forma estable si **el uso no lo está moviendo la utilidad**.

⭐⭐⭐ **CONFIRMADO POR LA PO (v2.0). Ya no es inferencia.** Preguntada si el uso estaba incentivado:

> **"Están en su business, en su variable."**

**El uso de AIDA está dentro de la retribución variable del asesor.** Y el criterio de éxito
declarado de la capacidad es, textualmente, *"la cantidad de consultas, el promedio de consultas
diarias y la actividad"* — **la métrica de adopción**.

⭐ **Consecuencia, y hay que decirla con cuidado porque es delicada:** la cifra de adopción **no puede
leerse como señal de valor** — no porque nadie haya hecho trampa, sino **por construcción del
indicador**. Un asesor que consulta AIDA porque está en su variable produce el mismo número que uno
que la consulta porque le sirve. **El indicador no distingue, y no fue diseñado para distinguir.**

⭐ **La lectura constructiva, que es la que va a la conversación:** la medición no está mal hecha.
**Mide adopción, y adopción no es utilidad** — y hoy no existe ningún indicador que mida lo segundo.
Ese es el hueco, y llenarlo es barato.

**La línea base real, para dimensionar:**

| Dato | Valor |
|---|---|
| Despliegue de AIDA Sales | **Mayo de 2025** — más de un año en producción |
| Estado | Volumen estable tras crecimiento sostenido |
| Volumen | **>30.000 consultas mensuales** |
| Promedio por asesor | **3 a 3,5 consultas diarias** |

### 6.2 Conducta compensatoria confirmada

Los propios asesores reportan usar **ChatGPT y Gemini** por fuera para *"qué respondo en este caso"*
y *"cómo manejo esta objeción"* — **exactamente la función que AIDA declara como propia**.

⭐ **La lectura correcta no es negativa: la demanda existe y ya está probada.** No hay que crear el
hábito. Hay que darle una herramienta que lo merezca — y que además responda con la estrategia de
RIMAC y no con la de un modelo genérico.

⭐ **Y hay un uso metodológico:** esas conversaciones son, en la práctica, **el registro de lo que
AIDA no les resolvió**. Preguntarle a un asesor *"¿qué le preguntas a ChatGPT que no le preguntas a
AIDA?"* es probablemente la pregunta más eficiente de todo el proyecto.

### 6.3 El resto de los datos de campo

| Dato | Valor |
|---|---|
| **Mejora más pedida** | **La consistencia de las respuestas** |
| **Capacidad peor calificada** | **Manejo de objeciones** — referido a los recursos que se le dan al asesor, no a AIDA |
| **Suficiencia de información para objeciones** | **Solo 6 asesores** de 19 consideran que reciben información suficiente |
| **Tema más pedido** | Manejo de objeciones (42%) |
| **Momento de mayor necesidad** | El cierre (~40%) |
| **Driver de valor del taller** | Casuística real + práctica con feedback |
| **Uso de AIDA** | "Siempre" 7/19 · **"Nunca" 1/19** |
| **Dónde ven la mayor oportunidad** | ⭐ **En AIDA** — no la dieron por perdida |
| ⭐⭐ **Patrón de uso por antigüedad** | **Confirmado por la PO:** *"los que tienen mayor uso son asesores nuevos; los que tienen menos uso son antiguos o más expertos"* |

⭐⭐ **El patrón por antigüedad confirma F-476 en población propia de RIMAC.** Brynjolfsson midió +34%
en novatos y efecto mínimo en expertos; el uso de AIDA reproduce esa distribución. Y ahorra trabajo:
§12.1 proponía reanalizar la encuesta cortando por antigüedad — **la PO ya tiene el dato**.

⚠️ **Precisión que hay que sostener:** esto confirma el patrón de **uso**, no el de **efecto**. Que
los novatos la usen más no prueba que les rinda más, aunque es consistente. **La estratificación por
antigüedad en el diseño de validación sigue siendo obligatoria.**

⭐ **Nota de muestreo:** el asesor que **nunca** la usa es la entrevista más informativa que existe.
Decidió que no valía la pena y puede decir exactamente por qué. Una sola conversación con esa persona
probablemente rinde más que cinco con usuarios satisfechos.

---

# Parte II · El diagnóstico

## 7. La taxonomía de fallas y la prueba que las separa

**Este es el aporte central del diagnóstico y el mayor riesgo del proyecto si se salta.**

"Fallas graves en el output" no es un diagnóstico: es un síntoma que puede venir de **cuatro capas
distintas**, que se arreglan con equipos, presupuestos y plazos distintos.

| Capa | Qué falla | Cómo se ve en el output | Cómo se confirma | Quién lo arregla |
|---|---|---|---|---|
| **A · Conocimiento** | El dato correcto no está, no es legible, está duplicado o desactualizado | Inventa datos · da información de otro producto · dice "no tengo esa información" sobre algo que sí está · **responde distinto a la misma pregunta en dos momentos** | Auditoría de base + *context precision/recall* | Contenido / Producto |
| **B · Instrucciones** | Tiene el dato pero se comporta mal: tono, longitud, no sigue el modelo de venta | Correcto pero inútil · da precio cuando debía redirigir con una pregunta | Mismo dato, distinta instrucción → ¿cambia? | Diseño / CoE |
| **C · Plataforma** | Techos duros del producto | Ignora documentos · trunca · no cita | Verificación técnica | TI / Arquitectura |
| **D · Ruteo** ⭐ | **Delega al subagente equivocado** | **Respuesta correcta del ramo equivocado** — el asesor la lee como dato falso | Preguntas con términos que existen en varios ramos | Clasificador |

⭐ **Por qué la capa D merece existir aparte:** una falla de ruteo **se ve idéntica a una falla de
conocimiento** desde afuera, pero se arregla en un lugar completamente distinto. Sin separarla, un
proyecto de limpieza de contenido podría no mover la aguja en nada.

### 7.1 La prueba que separa A de B, y cuesta una tarde

Tomar 20 preguntas reales de asesores. Para cada una, **pegar manualmente el fragmento correcto de la
fuente** en el prompt y volver a preguntar.

- Con el fragmento pegado **responde bien** → la información existe y **no la encuentra**: **capa A**,
  se arregla con contenido.
- Con el fragmento pegado **sigue respondiendo mal** → **capa B**, y ninguna limpieza de la base lo va
  a resolver.

⭐ **El síntoma de inconsistencia tiene una firma causal muy específica:** la misma pregunta contestada
distinto en dos momentos apunta a **duplicados o casi-duplicados en la base** — versiones distintas
del mismo documento, de las que cada consulta recupera una. Es la hipótesis principal a falsar, y es
consistente con una base cargada por acumulación a lo largo del tiempo.

### 7.2 ⭐ La tercera lectura, que es la más probable

Hay una lectura mejor que "capa A" o "capa B", y la trajo el research interno de Behavioral Design:

> AIDA **ya tiene la regla correcta** — su lógica le prohíbe responder de memoria en temas técnicos y
> la obliga a delegar al especialista. Esa es exactamente la mitigación que recomienda la literatura.
> **El problema no es la regla: es que hoy no se puede cumplir**, porque cuando el especialista sale a
> buscar encuentra contenido contradictorio, vacío o ilegible — y en ese vacío el modelo cae de vuelta
> en la memoria.
>
> **Ordenar el repositorio no es el plan B. Es lo que hace cumplible la regla que AIDA ya tiene.**

Es una **falla de capa A disfrazada de capa B**. Se distingue con la prueba del fragmento pegado.

---

## 8. La biblioteca: qué hay y por qué rompe

### 8.1 El malentendido de origen

Casi todas las bases de conocimiento de agentes empresariales nacen del mismo movimiento: *"tenemos
una carpeta con todo lo del producto — conectémosla al agente"*. Ese movimiento asume que una base
documental **para personas** y una base **para un agente** son la misma cosa con distinto lector.

| | Repositorio para personas | Base para un agente |
|---|---|---|
| **Unidad útil** | El documento completo | El **fragmento** recuperable |
| **Navegación** | La persona busca, hojea, descarta, interpreta | El sistema recupera ~3-5 fragmentos y responde **solo con eso** |
| **Duplicados** | Molestos pero inofensivos | **Tóxicos** — no sabe cuál es el vigente y puede citar el viejo con total seguridad |
| **Documento vacío** | Ruido visual ignorable | Contamina la recuperación y compite por espacio |
| **Formato visual (PPT)** | Aumenta la comprensión | **Destruye** información: lo que significaba la maqueta no llega |
| **Tabla** | La forma más clara de comparar | Se aplana en una cadena de valores desconectados |
| **Documento largo, 6 temas** | Cómodo | Diluye: el fragmento correcto compite con cinco temas irrelevantes del mismo archivo |

⭐ **Consecuencia: migrar la carpeta al agente no es migrar, es reescribir.** Y es trabajo de
contenido, no de TI.

### 8.2 Qué hay hoy en el repositorio de AIDA

**El catálogo de producto no cierra:**
- Un producto **figura dos veces con nombres distintos**
- Otro producto **vigente no aparece**
- Uno **conserva el nombre que tenía en 2022**
- **Conviven versiones distintas** del mismo material

**Y junto a eso:** archivos vacíos, plantillas sin contenido, láminas donde la información vive en el
diseño, PDFs y PPTs cargados tal cual.

### 8.3 El Playbook del Asesor como fuente canónica: evaluación

El **Playbook del Asesor** (versión 2026-08-14, 100.173 caracteres, 1.743 líneas) es el modelo de
venta Vida y la fuente canónica declarada.

**Veredicto:** el contenido es sólido y la estructura es mejor de lo esperado, pero **el documento que
debe resolver las contradicciones contiene contradicciones**, y no es consumible por un agente en su
forma actual.

**a) ⭐ La contradicción está dentro de la fuente canónica**

| Playbook | Matriz vigente (fichas desde 01/01/2025) | Estado |
|---|---|---|
| Temporal Total | Vida Temporal Total | ✅ Coincide |
| **Vida Contigo** + **VAG** *(dos filas, descripciones distintas)* | Vida Contigo = VAG = **un solo producto** | 🔴 **El playbook duplica un producto** |
| **Flexivida** | Nombre vigente: **Plan Vida Flexible** | 🔴 Nombre desactualizado (es el del PPT de 2022) |
| VCD digital · Endosable digital | No confirmados como productos distintos | ⚠️ |
| *(ausente)* | **Vida Futuro Protegido (VFP)**, con 4 variantes | 🔴 **Producto vigente que el playbook no menciona** |

⭐⭐ **Esto demuestra con nombres concretos lo que el diagnóstico venía planteando como hipótesis: la
inconsistencia del agente es la inconsistencia de la organización, reflejada.**

**b) El playbook no contiene los datos que el asesor más consulta.** Lo declara el propio documento:
*"Detalle técnico de cada producto (Pendiente) — coberturas exactas, exclusiones, tiempos de espera,
edades de contratación... depende del equipo de Producto."*

⭐ **Esto produce una predicción falsable y valiosa.** Si la base de Vida de AIDA deriva del playbook,
**no tiene ningún dato de cobertura, exclusión ni carencia**. Las preguntas B2-B4 del protocolo
deberían fallar. **Los dos resultados posibles son ambos hallazgos:**
- **Si fallan** → el hueco es de contenido, no de recuperación. Se arregla trayendo la matriz.
- **Si AIDA las responde con seguridad** → está tomando datos de **una fuente que nadie declaró**.
  Eso es una fuente no gobernada, y es más grave.

**c) Formato:** 🟢 ya es markdown, jerarquía limpia, cero imágenes. 🔴 **29 tablas**, varias en el
contenido más crítico. 🟡 cinco bloques temáticos en un solo archivo.

> ⚠️ **Corrección de este documento (2026-08-19):** la evaluación original medía el playbook contra
> el techo de **36.000 caracteres de Copilot**. **Ese criterio ya no aplica** — AIDA corre sobre
> Google. Lo que **sí sobrevive** y sigue justificando partirlo: **un tema por documento** y la
> calidad del fragmento recuperado. El umbral numérico se recalcula cuando se resuelva P15.

**Tamaños por bloque** (útil para el corte, independiente del techo):

| Bloque | Caracteres |
|---|---|
| Portada + journey | 5.349 |
| 1 · Quiénes somos | 13.701 |
| **2 · Qué vendes** | **5.396** |
| 3 · Que te encuentren | 27.063 |
| **4 · La asesoría** | **34.390** |
| 5 · Después del sí | 3.838 |
| Apéndice | **133** 🔴 documento prácticamente vacío |
| Índice de Confianza Profesional | 7.685 |

⚠️ **Dato incómodo:** el Bloque 2 (Qué vendes) es el bloque sustantivo **más pequeño** — 5.396
caracteres, contra 27.063 de social selling. **El conocimiento de producto, que es lo que se le
pregunta a AIDA, es la parte más delgada del playbook.**

**d) ⭐ Las tablas están justo donde más duele.** La *"Guía rápida: qué hay detrás de cada objeción"*
—tres columnas: lo que dice el cliente / qué puede haber detrás / estrategia sugerida— es
probablemente **el fragmento más valioso de todo el playbook**, y está en el formato que peor
sobrevive. Aplanada, quedan tres listas sueltas.

**Reescritura recomendada** — una entrada por objeción, autosuficiente:

> `##### Objeción: "Está muy caro"`
> **Qué puede haber detrás:** no tiene puntos de referencia.
> **Estrategias:** Punto de referencia · Tu ingreso es tu mayor activo.
> **Cómo suena:** …

**e) El playbook es dos artefactos en uno.** Contiene el modelo de venta (normativo, transversal) y
además contenido de otra naturaleza: el Índice de Confianza Profesional (autodiagnóstico personal), el
Apéndice administrativo (certificación, incentivos, remuneración) y buena parte del social selling
(cómo tomarse la foto, cómo vestirse). Para un humano está bien reunido. **Para el agente es ruido que
compite por el presupuesto de recuperación.** ⭐ **La derivación hacia la base debe seleccionar, no
solo reformatear.**

**f) Ocho vacíos declarados.** El documento lista lo pendiente: detalle técnico de producto y glosario
(Producto), perfil de cliente objetivo (Estrategia de Clientes), gestión de referidos e indicadores,
certificación, incentivos, esquema remunerativo, y **estrategia de contacto inicial CUA — "depende de
Alejo"**, que sigue pendiente en el documento. **Estos ocho vacíos son el backlog de contenido del
agente**: son las preguntas que AIDA **no puede** responder bien hoy porque la respuesta no existe en
ninguna fuente canónica.

**g) Lo que está bien y no hay que romper.** El modelo de 4 pasos y el manejo de objeciones son
contenido de calidad, con procedimiento, ejemplo dialogado y estrategias codificadas — y la
codificación ya es compatible con recuperación por fragmento. Tiene **28 fuentes citadas con
DOI/enlace**, varias de primer nivel. La lógica de match motivación ↔ perfil financiero → producto
está clara y bien construida. ⚠️ Ninguna de las 28 fuentes está registrada en el códice del proyecto.

---

## 9. Por qué ordenar rinde más que reentrenar

> ⭐⭐⭐ **CERRADO POR LA PO (v2.0) — no era una disyuntiva.** Preguntada si el modelo fue entrenado
> con la información:
>
> *"El modelo lee la documentación de SharePoint. **El modelo no genera data, extrae.** No genera
> ningún tipo de información. Lo que hace es **interpretar la base de conocimientos**, identificar qué
> se está consultando y sobre esa información responde. Inclusive **en la respuesta te pone los
> documentos de referencia** sobre los cuales se basó."*
>
> **Es RAG puro. No hay nada que reentrenar.** La calidad de la respuesta es **función directa** de la
> calidad del SharePoint — y AIDA **ya cita sus fuentes**, que era una de las recomendaciones de
> diseño del proyecto.
>
> ⭐ **Esto valida la tesis central del Release 1 desde la dueña de la capacidad, no desde el CoE.**
> Lo que sigue es la evidencia externa que decía lo mismo, y que ahora sirve para dimensionar cuánto
> se gana, no para discutir si se gana.

La pregunta natural de presupuesto: *si AIDA aprendió de una base desordenada, ¿alcanza con arreglar
la base o hay que reentrenarla?*

**La respuesta está medida** (F-490, F-492 — EMNLP 2024). Sobre conocimiento fuera del entrenamiento:

| Enfoque | Resultado |
|---|---|
| Modelo base | 0,481 |
| **Reentrenado** | 0,504 — **prácticamente nada, y en otro modelo empeoró** |
| Reentrenado + documento al responder | 0,830 |
| ⭐ **Solo darle el documento al responder** | **0,875 — el mejor resultado y el más barato** |

⭐ **Añadir reentrenamiento restó.** Y un segundo paper agrega que entrenar con hechos nuevos
**aumenta linealmente la tendencia a inventar**.

**La cuantificación de las palancas de formato:**

| Palanca | Efecto medido | Rigor |
|---|---|---|
| Conversión estructurada vs. extracción plana | 86,2% → **94,1%**; en preguntas con tablas, **33 puntos** de brecha | 🔵 revista arbitrada, 1.706 páginas |
| Calidad del conversor | Recuperación 63,5 → **44,8** con conversor mediocre | 🟢 ICCV 2025, 8.561 documentos |
| Presentaciones vs. texto | Brecha de **26 puntos** vs. 6 — **3 a 6× peor** | 🟢 ACL / ICLR / AAAI |
| Crecer el corpus sin separar por dominio | Precisión de 75% a **menos de 40%** | Preprint 2026 |

⚠️ **Advertencia de fuente que hay que sostener:** la cifra ancla que circula en el research interno
—*"la precisión cae 79,5% → 24,2% con documentos contradictorios"*— **tiene un problema de cita
abierto** (F-489). El arXiv citado resuelve a un paper distinto, cuyo mecanismo es conflicto
contexto-memoria, no contradicción entre documentos del corpus. **El fenómeno se sostiene por
literatura adyacente; la magnitud y su atribución hay que reverificarlas antes de que esa cifra entre
a un comité.** El orden de prioridades no cambia: se sostiene igual en F-490, F-491 y F-492.

---

## 10. La contradicción está aguas arriba

**El mandato del copiloto incluye una tarea que ningún copiloto puede cumplir.** Se le pide reducir la
carga de "leer información que a veces puede ser contradictoria".

⭐ **Pero un copiloto no puede arbitrar contradicciones — solo puede ocultarlas.** Cuando dos fuentes
dicen cosas distintas, el sistema recupera una de las dos y responde con seguridad. El asesor deja de
ver la contradicción, pero la contradicción sigue ahí, y ahora es invisible.

**Consecuencia:** la inconsistencia reportada de AIDA **puede ser la inconsistencia de la organización,
reflejada**. §8.3 lo demuestra con nombres de producto concretos.

**Quién resuelve la contradicción:** ✅ **el modelo de venta es la fuente canónica** — el único
material de consulta para todos los frentes multimodales. Ese es el diseño correcto. **El problema es
que hoy la fuente canónica contiene las contradicciones que debía resolver.**

⭐ **De ahí sale la secuencia del Release 1:** se abre cerrando el catálogo, porque cualquier base
derivada de una fuente contradictoria hereda el error.

---

## 11. La barrera de actualización de producto

**Barrera sistémica declarada:** el negocio no tiene una forma ágil de actualizar la información de
producto.

### 11.1 Parte del retraso es irreducible

Hay que separar dos capas que hoy están acopladas sólo porque viven en los mismos documentos:

| Capa | Naturaleza | ¿Acelerable? |
|---|---|---|
| **Piso regulatorio (SBS)** | Aprobación de condiciones, notas técnicas, pólizas | ⛔ **No** — es tiempo de regulador |
| **Capa comercial** | Argumentos, materiales, guías, parámetros de venta | ✅ **Sí** |

⭐ **Conviene medir el reparto antes de atacarlo.** Si el 80% del retraso es regulatorio, un proyecto
de agilidad sobre la capa comercial promete algo que no puede entregar.

### 11.2 ⭐ La dirección de la traducción está invertida

Hoy: documentos ejecutivos → alguien los interpreta → matriz de producto (si existe).

La práctica establecida invierte el flujo:

> **La matriz es la fuente; los documentos ejecutivos se generan desde ella.** Se autora una vez en
> forma estructurada y se publica a N canales.

Es la regla de **"una fuente canónica, N instanciaciones"** aplicada al dato de producto. **La matriz
debe ser fuente, no destino.**

⭐ **RIMAC ya tiene un prototipo de esto:** `matriz-productos-vida-rimac` — catálogo con coberturas,
add-ons, **trazabilidad de fuentes y niveles de confianza**. Se construyó a mano para otro fin, pero
**es la especificación de la matriz que se necesita**, incluida la parte que los proveedores no traen
de fábrica: decir de dónde salió cada dato y cuánto se confía en él. No hay que diseñarla desde cero
— hay que decidir si se promueve a fuente canónica, con dueño y cadencia.

⚠️ **Advertencia de evidencia, y es fuerte (F-483):** se buscó específicamente evidencia de
aceleración por configuradores de producto y **12 de 12 fuentes encontradas en dos búsquedas
independientes eran proveedores** que venden la solución que la cifra justifica. **Ninguna de esas
cifras entra al proyecto.**

### 11.3 La condición de gobernanza

Marcada por la jefatura como **condición, no deseo**:

> *"Si le vamos a dar un Excel, puede terminar pasando lo mismo... necesitamos que **Productos se
> comprometa** a tener por lo menos un flujo de actualización."*

⭐ **Sin eso, la promesa de información vigente no tiene sentido.** Se puede dejar el catálogo
impecable una vez; si nada impide que mañana se suba un PPT sin dueño ni fecha, la base se vuelve a
ensuciar. **El Release 1 debe dejar dueño y cadencia declarados o tiene fecha de vencimiento.**

---

## 12. Qué debe hacer el asesor, y qué de eso está verificado

### 12.1 El copiloto no rinde igual para todos

**F-476** (Brynjolfsson, Li & Raymond, *QJE* 2025 — 🟢A, 5.179 agentes, despliegue escalonado,
desempeño objetivo):

- **+14% de productividad en promedio**
- ⭐ **+34% en trabajadores novatos y de baja calificación**
- **Impacto mínimo en los experimentados**
- **Mecanismo declarado: la IA difunde las mejores prácticas de los trabajadores más capaces**
- Efectos secundarios: mejora el sentimiento del cliente y **la retención de empleados**

**Tres implicaciones directas:**

1. **El copiloto se diseña para el asesor nuevo, no para el promedio.** El +14% es un artefacto
   estadístico de dos poblaciones distintas; diseñar contra el promedio es diseñar contra nadie.
2. **La adopción actual hay que releerla por antigüedad.** Reanalizar la encuesta cortando por
   antigüedad es **trabajo de una tarde sobre datos ya levantados**.
3. **El mecanismo dice qué cargar:** si el efecto viene de difundir las prácticas de los mejores, el
   activo más valioso **no es el catálogo de producto** — es **cómo resuelven los mejores asesores las
   conversaciones difíciles**. Eso hoy no está escrito en ninguna parte.

⚠️ **Descuento honesto:** el estudio es de soporte al cliente, no de venta consultiva de vida.
**Dirección sólida, magnitud a validar en población propia.**

### 12.2 Qué conducta está verificada contra desempeño real

**F-477** (Franke & Park, *JMR* 2006 — 🟢A, meta-análisis de 155 muestras, **>31.000 vendedores**):

| Constructo | Autorreportado | Evaluado por el jefe | **Objetivo** |
|---|---|---|---|
| **Venta adaptativa** (cambiar la conducta durante la interacción según lo que el cliente muestra) | ✅ sube | ✅ sube | ✅ **sube** |
| **Orientación al cliente** (disposición general a poner al cliente primero) | ✅ sube | — | ❌ **no** |

⭐ **La asimetría es el hallazgo: la conducta situacional se paga en desempeño real; la actitud
declarada solo se paga en la autopercepción del vendedor.** Y la dirección causal probada va
**adaptación → orientación** (adaptarse construye la orientación, no al revés), lo que invierte el
orden de muchos programas de formación comercial: **no se entrena la actitud esperando que produzca
conducta, se entrena la conducta.**

### 12.3 ⭐ La convergencia que ordena la prioridad

Tres fuentes independientes apuntan al mismo punto del journey:

- **La evidencia** dice que lo que se paga es la **adaptación en vivo** (F-477).
- **Los asesores** dicen que lo que más necesitan es **manejo de objeciones** (42%) y que el momento
  de mayor necesidad es **el cierre** (~40%).
- **El taller** confirma que lo que valoran es **casuística real** + práctica con feedback.

**Manejo de objeciones en el cierre es venta adaptativa**: es el momento donde el asesor tiene que leer
una señal del cliente y cambiar de camino en tiempo real.

**El criterio de priorización de capacidades que sale de ahí:**

| Prioridad | Capacidad | Por qué |
|---|---|---|
| **1** | Apoyo a la **adaptación en vivo**: qué responder ante esta objeción, con este cliente, ahora | Único constructo con efecto verificado sobre desempeño **objetivo** + es lo que los asesores piden + es el momento declarado de mayor necesidad |
| **2** | **Casuística real** de los mejores asesores, recuperable por situación | Es el mecanismo por el que la IA produce el efecto + driver de valor #1 del taller |
| **3** | **Datos duros de producto**, exactos y trazables | Condición de no-daño: es donde una falla es riesgo de cumplimiento. **No es el diferencial** — la encuesta dice que el asesor no pide más información de producto |
| **4** | Contenido de actitud, valores, identidad de marca | Efecto verificado solo sobre desempeño **autorreportado**. No cargarlo como prioridad |

⚠️ **Nota de disciplina:** este mercado está saturado de cifras tipo *"los vendedores pierden el 30%
de su tiempo buscando información"*, casi siempre emitidas por proveedores de sales enablement y sin
fuente primaria rastreable (F-481). **Ninguna entra al proyecto sin rastrear el origen.**

---

## 13. Las restricciones duras

| # | Restricción | Consecuencia |
|---|---|---|
| **R1** | ⛔ **No hay sandbox de AIDA** | No se puede crear una funcionalidad y dársela a 10 asesores. **Mata el A/B de funcionalidad nueva.** Los prototipos son la única vía |
| **R2** | **AIDA es multi-ramo** | El alcance se acota a Vida — y eso **regala la serie de comparación** para la validación |
| **R3** | ⚠️ **Sin medición previa confirmada** | Si no hay telemetría accesible, la línea base hay que construirla, no recuperarla |
| **R4** | **El catálogo canónico está contradictorio** | Bloqueante: cualquier base derivada hereda el error |
| **R5** | ⚠️ **Deuda de credibilidad con los asesores** | Ya opinaron dos veces (19 encuestados, 30 en taller). Si no ven que sirvió, **dejan de responder** |
| **R6** | **Sin presupuesto asignado** | Todo lo de fase 1 debe ser cambio de contenido, no desarrollo |
| **R7** | ⛔ **No hay roadmap de mejora de AIDA** | Los cambios entran solo por **solicitud del negocio + captura de valor + "fricción de la demanda"**. Nadie está planificando mejoras hoy |
| **R8** | ⚠️ **En esta organización, capacidad ES presupuesto** | Los recursos del equipo de IA son **staffeables**: no están asignados al BAU y **los paga el negocio que los solicita**. Corrige el supuesto de "solo requiere capacidad" |
| **R9** | ⭐ **Pero cargar base de conocimiento es el camino barato** | Declarado por la PO como *"lo más sencillo"*, sin presupuesto ni staffing — **y ya hay un canal abierto y operando** |

### 13.1 ⭐⭐ Los dos caminos, y por qué esta es la distinción táctica más importante del plan

La PO describió, sin que se lo preguntaran, que hay **dos vías con costos radicalmente distintos**:

| Camino | Qué incluye | Costo | Proceso |
|---|---|---|---|
| ⭐ **Carga de base de conocimiento** | Documentos nuevos, corregidos o reformateados en el SharePoint | **"Lo más sencillo."** Sin presupuesto ni staffing | ⭐ **Canal ya abierto**: mesas de trabajo de los jueves, con Jaime — donde ya se está centralizando el manual y los catálogos de beneficios a través de AIDA |
| **Cambio de capacidad** | Funcionalidad nueva, cambios de lógica, interfaz | Presupuesto + recursos staffeables | Solicitud del negocio → captura de valor → fricción de la demanda → desarrollo |

⭐⭐⭐ **Consecuencia: no hay que crear un proceso para el Release 1. Hay que sumarse a uno que ya está
funcionando.** Ver §15.2 para la clasificación de los seis arreglos contra esta división.

---

# Parte III · El plan faseado

## 14. Vista general y regla de secuencia

| Fase | Qué hace | Requisito de entrada | Necesita presupuesto |
|---|---|---|---|
| **1 · Release 1** | Cerrar la brecha entre la promesa y lo que AIDA entrega, acotado a Vida | Ninguno — **arranca ya** | ❌ No |
| **2 · Extensión** | El mismo método en Salud y Vehicular | Que la Etapa 3 de la Fase 1 haya **mostrado mejora medida** | ❌ No |
| **3 · Motor** | Técnicas de recuperación: reordenador, cita forzada, descripción de láminas | Que el diagnóstico muestre que **la falla que queda es de recuperación**, no de contenido | ✅ Sí — es cambio técnico |
| **4 · Capacidades** | Evaluar los prototipos existentes y decidir qué se promueve | Diagnóstico de **uso y potencial** | ✅ Sí |
| **5 · Arquitectura** | Ruteo entre ramos y relación entre los agentes | ⛔ **Bloqueante: resolver P15** (qué es exactamente "Google") | ✅ Sí |
| **∥ Paralelo** | Que la mejora llegue a quien ya se fue | Ninguno — corre con la Fase 1 | ❌ No |

### 14.1 ⭐ La regla que ordena todo

**Cada fase depende de que la anterior haya dejado una medición.** No de que haya terminado — de que
haya **medido**. Sin eso, la fase siguiente propaga algo que nadie sabe si funciona.

### 14.2 La dependencia que no cambia

⚠️ **Todo el plan se apoya en que AIDA responda bien.** Un agente que entrena sobre una base
contradictoria enseña la contradicción, y la enseña con más eficacia que un documento. Un orquestador
delante de bases rotas esconde cuál falló. **El Release 1 va primero, siempre.**

---

## 15. Fase 1 · Release 1 — cerrar la brecha de la promesa

**Promesa del Release 1, en una frase:**

> **Que cuando un asesor de Vida le pregunte a AIDA algo de producto o de venta, la respuesta sea
> correcta, vigente y citable — o que AIDA diga que no lo sabe.**

No es "que AIDA funcione bien". Es un alcance acotado y verificable: **un dominio (Vida), un cuerpo
canónico, y una medición del antes y el después.**

### 15.1 Las tres etapas

| Etapa | Qué incluye |
|---|---|
| **1 · Diagnóstico de la herramienta** | Encuestas y **shadowing** con asesores → banco de preguntas reales → evaluación asistida con LLM (usabilidad, error, exactitud) → **medición de tiempo** |
| **2 · Intervención** | Los seis arreglos. Objetivo declarado: **menos errores y consulta más rápida** |
| **3 · Testeo** | Prueba 1 contra línea base (sin asesores, es la compuerta) → Prueba 2 con asesores |

⭐ **La velocidad como segundo objetivo.** No requiere trabajo aparte —sale del mismo movimiento:
menos documentos compitiendo y archivos más cortos hacen que el agente encuentre antes— pero **hay que
cronometrarla en la Etapa 1**, o después no se puede demostrar.

### 15.2 Los seis arreglos

> ⭐⭐ **ACTUALIZADO (v2.0).** El proyecto venía diciendo *"no requieren inversión, solo capacidad"*.
> **Eso es impreciso en esta organización: capacidad ES presupuesto** (R8). Lo que sí es gratis es
> **la carga de base de conocimiento** — y ahí caen cuatro de los seis.

**Clasificación por camino** (ver §13.1):

| # | Arreglo | Camino | Costo |
|---|---|---|---|
| **1** | Cerrar el catálogo de producto | ⭐ **Carga de base** | Canal abierto |
| **2** | Cargar el modelo de venta | ⭐ **Carga de base** | Canal abierto |
| **3** | Sacar del índice lo que no debe responder | ⭐ **Carga de base** (bajas) | Canal abierto |
| **4** | Convertir láminas en cuadros | ⭐ **Carga de base** | Canal abierto |
| **5** | Evaluar la consistencia de las respuestas | 🟡 **Mixto** — el banco lo corre el CoE; instrumentarlo *dentro* de AIDA sí es capacidad | Parcial |
| **6** | Que la pantalla no arranque en blanco | 🔴 **Capacidad** — solicitud + captura de valor + presupuesto | Requiere business case |

⭐⭐ **Cuatro de los seis —los que sostienen la promesa del Release 1— son gratis y por un canal que ya
opera.** El arreglo 6 es el que necesita el business case, y es justamente donde el proyecto tiene el
argumento más fuerte: decide si la mejora **llega** a quien ya abandonó la herramienta (§20).

**Detalle de cada arreglo:**

| # | Arreglo | Detalle | Estado |
|---|---|---|---|
| **1** | **Cerrar el catálogo de producto** | Una sola versión vigente por producto, con dueño y fecha. Resolver con Producto: ¿VAG y Vida Contigo son uno o dos? ¿Flexivida o Plan Vida Flexible? ¿Dónde está VFP? | 🔴 **Bloqueante de todo lo demás** |
| **2** | **Cargar el modelo de venta** | El Playbook partido por bloque, des-tabulado, sin las partes que solo funcionan como gráfico, y **seleccionando** qué entra (no el autodiagnóstico ni el apéndice) | Depende de 1 |
| **3** | **Sacar del índice lo que no debe responder** | Archivos vacíos, plantillas, versiones superadas. Compiten con la respuesta correcta | Independiente |
| **4** | **Convertir las láminas en cuadros** | Lo que hoy vive en el diseño de una diapositiva pasa a texto recuperable. Empezar por objeciones, que es el de mayor demanda | Independiente |
| **5** | **Evaluar la consistencia de las respuestas** | Banco de control permanente + la metodología de jueces por área (§22.3) | Se monta en Etapa 1 |
| **6** | **Que la pantalla no arranque en blanco** | Hoy AIDA se presenta y no dice qué se le puede pedir. Es la puerta de la recuperación de desertores | Independiente |

### 15.3 El entregable cero: el inventario

Antes de tocar nada, **saber qué hay**: cuántos archivos, de qué tipo, cuáles están vacíos, cuáles
duplicados, cuál es la fecha de cada uno y quién es su dueño.

Sin inventario no se puede dimensionar el trabajo ni demostrar que se hizo. **Es también la línea base
del "antes".**

### 15.4 ⭐ Por qué el catálogo es bloqueante y no un paso más

Mientras el catálogo canónico esté mal, **cualquier base derivada de él hereda el error**. Cargar el
playbook antes de cerrar el catálogo es cargar las contradicciones en formato limpio — que es peor,
porque las vuelve más difíciles de detectar.

**Es trabajo de días y desbloquea todo lo demás.**

---

## 16. Fase 2 · Extender a los demás ramos

Salud y Vehicular con el método ya probado en Vida.

**Requisito de entrada:** que la Etapa 3 del Release 1 haya **mostrado mejora medida en Vida**. Si no
la mostró, extender el método es propagar algo que no sabemos que funciona.

⚠️ **Costo específico de esta fase:** al extender, **se pierde la serie de comparación natural** (§23.3).
Por eso la medición de Vida tiene que quedar **cerrada antes**, no en paralelo.

---

## 17. Fase 3 · Mejorar el motor

Las técnicas de recuperación que el Release 1 deja fuera **por ser cambio técnico y no de contenido**:

| Técnica | Qué aporta |
|---|---|
| **Reordenador + cita forzada con fragmento textual** | La mejor relación costo-beneficio de las técnicas disponibles. Y ataca directamente el modo de falla dominante (§21.1) |
| **Descripción multimodal de láminas** | Recupera los diagramas sin rehacerlos |
| **Recuperación visual de página** | La opción más cara, y **rinde menos en español que en inglés**. Solo si el diagnóstico muestra que la falla es visual |

**Requisito de entrada:** que la Etapa 1 haya mostrado que **la falla que queda es de recuperación y
no de contenido** — son capas distintas (A vs. C) y se arreglan distinto.

---

## 18. Fase 4 · Entrenamiento, casuística y prototipos

> ⚠️ **Esta fase está deliberadamente fuera de la fase 1.** Dos razones, ambas explícitas: requiere
> otro nivel de desarrollo, y **la literatura no sostiene que el asesor tenga que entrenar a través de
> su copiloto** — fue una idea que vino de la propuesta de la herramienta, no de la necesidad
> levantada. Lo que sigue es **el expediente para cuando se decida entrar**, no una propuesta activa.

### 18.1 Lo que ya existe

Behavioral Design **ya construyó 2 prototipos** (§5.2). La fase deja de ser *"prototipar capacidades"*
y pasa a ser **"evaluar los prototipos que existen y decidir cuáles se promueven"** — más barato y más
rápido de lo que estaba planteado.

### 18.2 Las tres capacidades candidatas

| Capacidad | Por qué es candidata | Estado |
|---|---|---|
| **Entrenar habilidades de venta** | Interés declarado del equipo; y es **el mecanismo de captura** de la casuística | ✅ Prototipo construido |
| **Casuística de los mejores asesores, recuperable por situación** | El conocimiento que gana ventas vive en conversaciones, no en documentos — por eso ninguna base lo tiene | Se **produce** desde la práctica |
| **Registro asistido** | El asesor registra en Salesforce lo que ya le contó a AIDA. La duplicación más visible de los seis frentes | Sin prototipar. ⚠️ Cruza a otro dueño |

### 18.3 ⭐ El proceso de captura, y sus dos riesgos

**El proceso propuesto:** *AIDA captura las mejores respuestas durante el entrenamiento con AIDA.*

**Por qué es la mejor idea del bloque:** el problema de la casuística nunca fue *quererla* — fue
**adquirirla**. Pedirle a alguien que la escriba falla dos veces: no lo hace, y si lo hace escribe la
versión declarada, no la que ejecuta. **La práctica la produce como subproducto de algo que el asesor
ya tiene razón para hacer.**

**Pero el mecanismo validado no funciona exactamente así:**

| | Brynjolfsson, Li & Raymond (2025) | La propuesta |
|---|---|---|
| **Qué se capturó** | Conversaciones **reales con clientes** | Respuestas de **práctica** sobre casos ficticios |
| **Cómo se definió "la mejor"** | Por el **desenlace**: el caso se resolvió, sobreponderando a los agentes con mejor desempeño real | Por el **puntaje que AIDA misma asigna** |

**Riesgo 1 · La práctica no es la conducta.** Lo que un asesor dice cuando lo puntúan es lo que
**cree** correcto, no lo que hace frente al cliente. No es fatal, pero hay que nombrarlo: el corpus
resultante es de práctica **declarada**.

**Riesgo 2 · ⭐ El bucle cerrado, y este sí es serio.** Si AIDA puntúa, selecciona las respuestas mejor
puntuadas y después enseña ese corpus, **nada externo corrige nunca la rúbrica**. La rúbrica pasa a ser
la definición operativa de "vender bien" y deriva libre de si efectivamente vende. **Es el mismo
problema de una fuente que se valida a sí misma, reproducido un nivel más arriba.**

### 18.4 ⭐ El arreglo: separar la captura de la etiqueta

**No hay que renunciar a la idea. Hay que anclar el bucle a una señal de afuera.**

- **La captura sigue igual** — durante la práctica, que es lo barato y lo que funciona.
- **La etiqueta viene de afuera:** qué respuestas entran al corpus canónico lo decide el **desempeño
  real** del asesor (conversión, persistencia de la póliza), **no su puntaje de práctica**.
- ⭐ **Y no cuesta trabajo extra:** esa señal de desenlace **ya hay que levantarla** para la Etapa 3 del
  Release 1. Es el mismo dato, usado dos veces.

**Beneficio secundario:** si la casuística de los mejores-por-resultado rinde distinto que la de los
mejores-por-rúbrica, **eso mismo es un hallazgo** — dice si la rúbrica mide lo que importa.

### 18.5 ⚠️ El reporte a la jefatura puede invertir el signo de todo lo demás

Es la pieza más barata de implementar y la más fácil de equivocar, **porque parece una función
gratis**. No lo es.

- **Kluger & DeNisi (1996)** — 607 tamaños de efecto, 23.663 observaciones. El feedback mejora el
  desempeño en promedio (**d = 0,41**), pero ⭐ **más de un tercio de las intervenciones de feedback lo
  empeoró**. El moderador es **hacia dónde dirige la atención**: el feedback sobre **la tarea** ayuda;
  sobre **la persona** perjudica. Un puntaje que llega a tu jefe es, por construcción, sobre la persona.
- **Efecto de segundo orden propio de este diseño:** si el puntaje es evaluativo, el asesor deja de
  usar la práctica para fallar barato y empieza a usarla para puntuar bien. ⭐ **Eso contamina justamente
  el corpus que se quiere construir.** Las dos funcionalidades se atacan entre sí.

**Recomendación — es decisión de diseño, no técnica:**

| Destinatario | Qué ve | Por qué |
|---|---|---|
| **El asesor** | Su puntaje, su progreso, todo | Feedback de tarea, es el que funciona |
| **La jefatura** | **Agregado y por tema, no por persona** — *"en tu equipo la objeción de precio es la debilidad"* | Accionable sin convertir la práctica en examen |
| **Individual a jefatura** | Solo si se decide después, declarado, **con el corpus ya construido** | Evita contaminar la captura cuando más importa |

Si el negocio igual quiere reporte individual —decisión legítima—, entonces como mínimo **conservar un
modo de práctica que no puntúe ni reporte**, para que siga existiendo un lugar donde fallar.

### 18.6 Qué esperar del entrenamiento, honestamente

| Hallazgo | Implicación |
|---|---|
| La práctica simulada rinde **igual que practicar con una persona real** (27 ECAs, 1.480 participantes — F-497) | ⭐ **El valor no es que enseñe mejor. Es la disponibilidad y el costo** — se practica un martes a las 11 de la noche sin agendar a nadie. Ese argumento es suficiente y defendible; el de "enseña mejor" no |
| Contra ninguna instrucción el efecto es grande; contra instrucción activa cae a **0,30–0,66** (F-498) | Si ya hay role-play con la jefatura, el delta es modesto. **Cuál es el caso hay que levantarlo, no suponerlo** |
| ⚠️ En **profesiones**, la práctica deliberada explica **menos del 1% de la varianza** de desempeño — la categoría más débil de cinco (F-496) | **No se puede vender el entrenamiento como la palanca de productividad.** Lo que sí sostiene la evidencia es la **captura de casuística**, que es un argumento de conocimiento, no de aprendizaje |

### 18.7 ⚠️ La colisión con Sales Coach

**Sales Coach ya entrena.** Si AIDA adquiere capacidad de entrenamiento, hay **dos agentes que
enseñan** — y dos agentes que enseñan sin fuente común es exactamente la falla que este proyecto está
diagnosticando en los documentos, reproducida un nivel más arriba.

**P12 — ¿El prototipo de práctica reemplaza a Sales Coach, lo reemplaza en parte, o es un cuarto
agente?** Las tres son defendibles. **La que no es defendible es no decidirlo**, porque el resultado
por omisión son dos agentes enseñando modelos de venta que nadie garantizó que coincidan.

### 18.8 El orden correcto de esta fase

1. **Inventariar los 2 prototipos** (P11) — qué hace cada uno, sobre qué corre, quién lo tiene.
2. **Decidir la señal de etiqueta** antes de capturar nada (§18.4) — un corpus construido con la
   etiqueta equivocada hay que rehacerlo entero.
3. **Decidir el destinatario del puntaje** antes de la primera corrida (§18.5), por la misma razón.
4. **Resolver P12** antes de que existan dos agentes que enseñan.

---

## 19. Fase 5 · Arquitectura de agentes

Dos problemas que ninguna limpieza de contenido resuelve:

- **El ruteo entre ramos** — que una pregunta ambigua llegue al subagente correcto (capa D).
- **La relación entre los tres agentes desplegados** — AIDA, suscripción, Sales Coach. El agente coach
  es el único que necesita contexto de otro agente, y la literatura marca ese patrón como el más frágil.

**Y la decisión de fondo que conviene tomar aquí y no antes:** ⭐ **consolidar la puerta de entrada del
asesor, sin consolidar las bases de conocimiento** (§4.1). Juntar todo en una sola base empeora las
respuestas — crecer el corpus sin separarlo por dominio llevó la precisión de 75% a menos de 40%.

⛔ **Requisito de entrada bloqueante: resolver P15** — qué es exactamente el servicio Google sobre el
que corre AIDA. Sin eso, cualquier decisión de arquitectura se toma sobre un supuesto no verificado, y
ya sabemos lo que pasa cuando eso ocurre.

---

## 20. En paralelo · Recuperar a quien ya se fue

**No espera a ninguna fase.** Corre junto con la Etapa 2 del Release 1.

**El problema:** llegar a AIDA no es la dificultad — los asesores saben dónde está. ⭐ **Lo que hay al
llegar es una pantalla en blanco:** ningún botón, ningún caso de uso, ningún ejemplo, nada que le diga
al asesor qué puede pedirle.

**Por qué esto puede anular todo el trabajo:**

- ⭐ **El asesor que ya dejó de usar AIDA no va a volver a comprobar si mejoró.** Está documentado desde
  2015 (Dietvorst, Simmons & Massey): tras ver fallar a una herramienta automatizada, la gente la
  abandona **incluso cuando pasa a ser mejor que la alternativa**, y no la reevalúa por su cuenta.
- El meta-análisis de adopción (88 estudios, King & He 2006) da la jerarquía: la **utilidad percibida**
  predice el uso más que la facilidad de uso — la calidad **sí** es la palanca mayor. Pero la facilidad
  también predice la utilidad percibida: ⭐ **la pantalla en blanco no compite con la calidad, la
  oculta.** El asesor no puede percibir que AIDA mejoró si nunca llega a formular la pregunta que se lo
  mostraría.
  ⚠️ *Los coeficientes específicos que circulan de este paper provienen del research interno; se
  verificó el paper y su muestra, no esos coeficientes.*
- El caso análogo más parecido —ensayo del gobierno australiano con Copilot, más de 2.000 personas con
  acceso garantizado— tuvo **86% que quería seguir usándolo y solo un tercio usándolo a diario**, con
  dos barreras declaradas que no eran de acceso: **no saber cómo pedir** e **identificar casos de uso
  relevantes**.

⭐ **Consecuencia para el alcance:** el Release 1 necesita **una pieza mínima de reintroducción** —
aunque sean tres ejemplos de qué preguntarle y un aviso de que cambió. No es el rediseño del front,
que es conversación aparte. **Es lo mínimo para que la mejora llegue a quien ya se fue**, que es
justamente la población que se quiere recuperar.

**Una idea adicional que salió de la jefatura y vale la pena retener:** personalizar la entrada según
el **contexto de uso** del asesor (momento del día, actividad en curso), no solo según el tema. Es el
patrón que ya usan las herramientas de IA de consumo, y es un quick win de bajo costo.

---

## 21. Lo que el plan **no** arregla

Decirlo antes, no después.

### 21.1 La invención residual no desaparece

Herramientas comerciales con recuperación sobre documentos oficiales **y citas reales** siguen
inventando entre **17% y 33%** (F-493), y el modo de falla dominante es **citar un documento auténtico
y afirmar falsamente que dice lo que no dice**.

⚠️ **Y hay un agravante conductual: mostrar citas sube la confianza del usuario incluso cuando las
citas son falsas.**

⭐ **De ahí el criterio de diseño: no basta con el enlace — fragmento textual y fecha de vigencia
visibles**, y medir si la cita *sustenta* la respuesta, no si existe. **El banco de control no es un
entregable de proyecto: es permanente.**

### 21.2 El resto

- **El ruteo entre ramos sigue igual** hasta la Fase 5. Una pregunta ambigua puede seguir yendo al
  especialista equivocado — y eso se ve, desde el asesor, idéntico a un dato falso.
- **No resuelve el gobierno de la actualización** por sí solo. Si nada impide que mañana se suba un PPT
  sin dueño ni fecha, la base se vuelve a ensuciar. **El Release 1 debe dejar dueño y cadencia
  declarados o tiene fecha de vencimiento.**
- **No prueba que el modelo de venta funcione.** Prueba que la herramienta que lo vehicula mejoró. Son
  dos cosas distintas y conviene no confundirlas ante un comité.
- **No cubre las integraciones con Salesforce.** Fueron declaradas viables por el área, pero **cruzan a
  otro dueño** — se mapean, no se proponen, hasta que esa puerta se abra formalmente.

---

# Parte IV · Cómo se mide

## 22. Los instrumentos de diagnóstico

### 22.1 Los tres artefactos de exploración

| Artefacto | Qué hace | Estado |
|---|---|---|
| **Auditoría de la herramienta** | Estresarla, evaluar la calidad de sus respuestas con método estructurado | Instrumento listo, **sin correr** |
| **Reporte del asesor** | Encuesta + **shadowing**, con foco en cómo y para qué usan las herramientas de afuera | Encuesta hecha (19); **shadowing pendiente** |
| **Registro de fallos técnicos** | Tiempos, inconsistencias, de forma sistemática | ⚠️ **Hoy no existe** |

⭐ **Un cuarto artefacto cambió de dueño.** La lista de *"qué debería y qué no debería ser AIDA"* **no
sale del diagnóstico** — lo tienen que declarar los **dueños de la capacidad**. Deja de ser entregable
y pasa a ser **la pregunta que se lleva a la reunión** (P14).

**Herramienta de campo:** Wiser, incluida su modalidad cuantitativa.
⚠️ **Restricción operativa:** los asesores tienen la IA bloqueada en la computadora — **responden desde
el teléfono**.

### 22.2 Los cuatro bloques del protocolo

| Bloque | Qué mide | Estado |
|---|---|---|
| **A · Auto-interrogación** | Qué declara AIDA sobre sí misma (A1–A10) | ✅ Primera corrida hecha (§5.1) |
| **B · Calidad contra la matriz** | Exactitud sobre datos de producto, con la matriz como patrón oro | ⚠️ **Banco provisional** — ver §22.4 |
| **C · Ruteo entre ramos** | Preguntas con términos que existen en varios ramos | Sin correr |
| **D · Claude como auditor** | Evaluación asistida por LLM con rúbrica y **calibración humana obligatoria** | Sin correr |

⭐ **Correr B2-B4 temprano.** Distinguen hueco de contenido de fuente no gobernada (§8.3b), y es la
prueba más informativa por unidad de esfuerzo disponible hoy.

### 22.3 ⭐ Bloque E · Metodología de jueces por área

**Aporte nuevo, y llena un hueco real.** Preguntarle a **Experiencia, Negocio y Marketing** qué
*debería* responder AIDA ante una pregunta dada, y usar eso como referencia contra la respuesta real.

**Por qué es un aporte y no una variante:** el protocolo usa la **matriz de producto** como patrón oro,
y eso solo sirve para la capa de **dato de producto**. Esto abre patrón oro para la capa de **mensaje**
—cómo hablarle al cliente—, que no tenía ninguno.

⭐ **Y tiene un segundo efecto que vale más que el primero:** si las tres áreas responden distinto, **la
inconsistencia no es de AIDA — es de la organización**, y queda medida. Es la tesis de §10 convertida
en instrumento.

### 22.4 ⭐ El campo alimenta el protocolo, no lo sigue

El banco de preguntas del Bloque B se construyó **deduciéndolo de la matriz de productos** — son
preguntas verificables, pero **sintéticas**: son las que *deberían* hacerse, no las que los asesores
*hacen*.

Un banco sintético mide lo que a nosotros nos parece importante. Un banco derivado del campo mide **lo
que realmente rompe la venta**. **El trabajo de campo va antes o en paralelo a la corrida del
protocolo, no después** — y su salida principal es el banco de preguntas real.

Se conservan las preguntas de control (producto inexistente, duplicado de tres nombres, cifra con
riesgo regulatorio) porque **esas sí tienen que ser diseñadas**.

### 22.5 Cómo preguntarle al asesor: incidentes, no opiniones

⚠️ **Preguntar "¿te ayuda AIDA?" produce una evaluación, y las evaluaciones autorreportadas de
herramientas de IA están sistemáticamente desalineadas de la conducta real.** El proyecto tiene la
evidencia dura: **METR (2025)** — desarrolladores fueron **19% más lentos** con IA mientras estimaban
ser **20% más rápidos**: una brecha de ~39 puntos entre percepción y desempeño.

La corrección tiene nombre: **técnica del incidente crítico** (Flanagan, 1954). Se pide **el último
caso concreto en que ocurrió**, con contexto, conducta y consecuencia.

| ❌ En vez de preguntar | ✅ Preguntar |
|---|---|
| ¿AIDA te da buena información? | Cuéntame **la última vez** que le preguntaste algo y la respuesta no te sirvió. ¿Qué preguntaste? ¿Qué te dijo? ¿Qué hiciste después? |
| ¿Confías en AIDA? | ¿Cuándo fue **la última vez** que verificaste una respuesta suya por otro lado? ¿Con qué la verificaste? |
| ¿Usas ChatGPT? | ¿Cuál fue **lo último** que le preguntaste a ChatGPT o Gemini para el trabajo? ¿Por qué a esa y no a AIDA? |
| ¿Te falta información? | ⭐ ¿Hay algo que **antes le preguntabas y ya no**? ¿Qué pasó? |
| ¿Encuentras información contradictoria? | Cuéntame **la última vez** que dos fuentes de RIMAC te dijeron cosas distintas. ¿Cuáles eran? ¿A cuál le hiciste caso? |

⭐ **La última fila es doble:** produce insumo sobre las contradicciones **y** revela el criterio informal
que el asesor usa para arbitrar — que hoy es la única regla de resolución que existe.

### 22.6 Qué solo entrega el campo

1. **Qué le preguntan a ChatGPT/Gemini que no le preguntan a AIDA.** El mapa del hueco sin auditar un
   solo archivo.
2. ⭐ **Qué dejaron de preguntar.** El hallazgo más importante y el más invisible: después de suficientes
   malas respuestas, la gente deja de hacer categorías enteras de pregunta. **La telemetría tiene un
   problema de supervivencia — no puede mostrar una pregunta que nunca se hizo.**
3. **Qué hacen cuando sospechan que la respuesta está mal.** Conducta de rodeo, invisible en logs.
4. **En qué momento del flujo consultan y por qué ahí.** Los timestamps dan la hora, no la situación.
5. **Qué contradicciones han vivido en carne propia.** El asesor es el punto donde todas las
   instanciaciones del modelo se encuentran — **sabe dónde están porque las sufre.**
6. **La carga emocional.** El mandato del copiloto la nombra. No hay telemetría que la mida.

### 22.7 Muestreo y shadowing

**Volumen sugerido:** 8-12 entrevistas de incidente crítico (~45 min) + shadowing de 4-6 asesores. Lo
suficiente para **saturar los modos de falla**, no para estimar frecuencias — la frecuencia sale de la
telemetría y del protocolo.

**A quién:**
- ⭐ **El que no la usa nunca** (1/19) — la entrevista más informativa que existe.
- **Usuarios intensivos** (del grupo de 7) — hay que saber qué **no** romper.
- **Por antigüedad, obligatorio** — novatos y expertos usan la herramienta distinto y el efecto se
  concentra en los primeros. Sin este corte, el campo describe un asesor promedio que no existe.
- **Lima y provincias** — provincia por videollamada.

**Qué mirar en el shadowing, que la entrevista no da:**
- **El momento exacto de la consulta** — ¿antes, durante o después de hablar con el cliente?
- ⭐ **El salto entre herramientas** — la secuencia real: AIDA → Salesforce → WhatsApp → ChatGPT →
  material físico. **Ahí está la carga que el copiloto debería absorber, y se ve, no se recuerda.**
- **Qué hace con la respuesta** — ¿la copia, la reformula, la descarta, la verifica?
- **Cuánto tarda** en obtener algo usable, y cuántos intentos hace.
- **Qué no consulta** aunque le habría servido.

### 22.8 ⚠️ Dos riesgos del campo

**1 · Ser observado cambia la conducta.** Un asesor acompañado va a usar AIDA más de lo habitual. **El
shadowing sobreestima el uso.** Mitigación: triangular con telemetría, decir explícitamente que no se
evalúa a la persona sino a la herramienta, y **no compartir los registros individuales con jefaturas**.

**2 · ⭐ Deuda de credibilidad — el riesgo relacional, y es el más serio.** Los asesores **ya opinaron
dos veces**. Si se les vuelve a preguntar y no ven que lo anterior sirvió de algo, **el costo no es que
respondan mal: es que dejen de responder**, y eso cierra la única fuente de las seis preguntas de §22.6.

**Obligación que se sigue:** abrir cada entrevista contando **qué produjo lo que dijeron antes** — que
su queja está documentada, que originó este proyecto, y qué se está haciendo. No es cortesía: **es la
condición para que la segunda ronda tenga la calidad de la primera.**

---

## 23. El diseño de validación

### 23.1 ⭐ Son dos experimentos, no uno

Confundirlos es el error más caro disponible, porque hace gastar el capital político de la fuerza de
venta en una prueba que podía hacerse sin ella.

| | **Experimento 1 · La herramienta** | **Experimento 2 · El asesor** |
|---|---|---|
| **Pregunta** | ¿Los fixes mejoraron las respuestas? | ¿La mejor herramienta cambia el desempeño? |
| **Necesita asesores** | **No** | Sí |
| **Duración** | Días | Semanas o meses |
| **Ruido** | Muy bajo — banco fijo | Alto — estacionalidad, campañas, cartera, ánimo |
| **Qué aísla** | El efecto del fix, limpio | El efecto del fix **más** todo lo demás |
| **Costo** | Bajo | Alto, y consume goodwill de la FFVV |

⭐ **El Experimento 1 es la compuerta del 2.** Si la calidad de respuesta no se mueve en el mismo banco
de preguntas, **no hay nada que testear con asesores** — y se evita quemar la disposición de la fuerza
de venta en un piloto que nunca iba a mostrar nada.

### 23.2 Experimento 1 — la re-corrida

- **Mismo banco de preguntas, mismo juez, misma rúbrica, misma calibración** que la línea base.
- **Comparación pareada pregunta por pregunta** (antes → después). ⭐ Esto da **alta potencia
  estadística con pocos ítems**, porque cada pregunta es su propio control.
- **Aísla el mecanismo:** como el banco está fijo, un cambio de puntaje es atribuible al fix y no a
  variación de asesores o de mercado.

⚠️ **Advertencia:** una prueba así **no es un casillero que se marca una vez** — vale mientras la
población de uso no cambie. Si el banco deja de parecerse a lo que los asesores preguntan, deja de
medir lo que importa.

### 23.3 Experimento 2 — qué diseño es posible

⛔ **Dado que no hay sandbox, el A/B por asignación individual dentro de AIDA no es posible.**

| Diseño | Viable | Nota |
|---|---|---|
| A/B de **funcionalidad nueva** en AIDA | ⛔ **No** | No hay forma de aislar un grupo |
| A/B por **equipos o canales** | 🟡 Solo si la intervención puede acotarse a un canal | Depende de la arquitectura |
| ⭐ **Serie temporal interrumpida** | ✅ **Sí** | Es el diseño recomendado |

⭐ **El "full con puntos de corte" tiene nombre: serie temporal interrumpida.** Es el diseño
cuasi-experimental más fuerte disponible cuando no se puede aleatorizar. **Requiere varios puntos de
medición antes y después, no dos fotos.**

⭐⭐ **Y su debilidad —que algo más pudo cambiar en el mismo periodo— se resuelve con algo que ya
tenemos gratis:** como el Release 1 se acota a Vida, **Salud y Vehicular siguen con la base vieja y
funcionan como serie de comparación natural.** Si Vida mejora y los otros ramos no, el efecto es de la
intervención. Es la variante *comparativa* del diseño, y no cuesta montar nada.

⚠️ **Esa serie de comparación se pierde en la Fase 2.** Por eso la medición de Vida tiene que cerrarse
antes de extender.

### 23.4 Qué medir — tres niveles que no se mezclan

1. **Éxito de tarea** — ¿resolvió lo que el asesor necesitaba?
2. **Percepción del asesor** — ¿se sintió útil, claro, confiable? (escalas validadas: **BUS-11** es la
   más cercana al caso; **CUQ** tiene un factor específico de *manejo de errores*)
3. **Corrección objetiva** — ¿lo que dijo es fiel a la fuente real? (*faithfulness* para alucinación,
   *context precision/recall* para calidad de recuperación)

⭐ **El eje 3 es el que responde "¿tiene fallas graves?" con un número defendible ante un comité**, y el
que distingue capa A de capa B.

**Y un cuarto que la reestructuración agregó: el tiempo.** Hay que cronometrarlo en la Etapa 1 o después
no se puede demostrar.

### 23.5 Dos condiciones no negociables

- ⭐ **Estratificar por antigüedad desde el diseño** — el efecto se concentra en novatos (+34%); sin el
  corte, un efecto real puede leerse como nulo.
- ⭐ **La conversión no es desenlace primario** — el ciclo de venta de Vida excede la ventana de
  medición. Usarla como métrica principal es diseñar para no encontrar nada.

**Preregistrar antes de correr:** hipótesis, desenlace primario, cortes y criterio de éxito, escritos
antes de ver los datos.

### 23.6 El formato del corpus de fallas

Una fila por falla observada:

`pregunta del asesor · respuesta del agente · respuesta correcta · fuente donde vivía la respuesta ·
capa (A/B/C/D) · severidad · ¿es de producto regulado?`

Dos campos merecen justificación:
- ⭐ **"Fuente donde vivía la respuesta"** convierte el corpus en un **mapa de huecos de la base**. Sin
  él, la lista no dice qué arreglar.
- ⭐ **"¿Es de producto regulado?"** separa la falla cosmética de la falla con riesgo: un error sobre
  coberturas, exclusiones o precio dicho a un cliente **no es un problema de calidad, es un problema de
  cumplimiento.**

---

# Parte V · Estado abierto

## 24. Preguntas abiertas

| # | Pregunta | Estado | Por qué importa |
|---|---|---|---|
| **P1** | ¿Cuál es la herramienta objeto del diagnóstico? | ✅ **Resuelta** | AIDA, desplegada. No el prototipo Claude |
| **P2** | Licenciamiento y sus techos | ⛔ **Obsoleta** | Era una pregunta sobre Copilot. Reemplazada por P15 |
| **P4** | ¿Existe telemetría de AIDA accesible? | ✅ **RESUELTA** | **Sí, y ya se solicitó.** Los logs traen todas las preguntas, las respuestas y el feedback +/−. Es el corpus de fallas ideal. **Descarta pedirle registro manual a los asesores** |
| **P5** | ¿Existe medición previa / línea base? | ✅ **RESUELTA** | **Sí, sólida.** Desplegada desde mayo 2025, dashboards activos, >30.000 consultas/mes. Más de un año de serie temporal |
| **P6** | ¿Los agentes comparten base de conocimiento? | 🟡 **Parcial** | **AIDA Service y AIDA Sales tienen bases independientes que no conversan** (✅ el patrón correcto). Dentro de Sales, estructura de carpetas por ramo — falta confirmar si hay subagentes |
| **P7** | ¿Quién es dueño de cada agente? | 🔴 **Abierta** | Determina si "una puerta de entrada" es problema técnico u organizacional |
| **P8** | ¿El modelo de venta contiene o referencia los datos de producto? | ✅ **Resuelta** | Los **referencia** sin contenerlos — confirmado por el propio playbook |
| **P9** | ¿Sobre qué framework corre AIDA? | ✅ **RESUELTA** | **Google, no Copilot.** Los límites numéricos de Copilot quedan descartados |
| **P10** | ¿Cuál es "el modelo SHUNK"? | 🔴 **Abierta** | Marco de evaluación nombrado por Alejo, **no identificado**. Candidatos descartados: Shackel (1991), BUS-11/BUS-15/CUQ. ⚠️ **No se aplica por aproximación** |
| **P11** | ¿Cuál es el segundo prototipo de Behavioral Design? | 🔴 **Abierta** | Si es un tercer artefacto, el inventario está incompleto |
| **P12** | ¿El prototipo de práctica reemplaza a Sales Coach? | 🔴 **Abierta** | Por omisión quedan dos agentes enseñando modelos que nadie garantizó que coincidan |
| **P16** | ¿AIDA Sales tiene subagentes por ramo adentro? | 🔴 **Abierta** | La auto-interrogación declaró cinco; la PO describe segmentación por caso de uso. **Se resuelve con el diagrama, no preguntándole a AIDA** |
| **P17** | ¿Qué es la "metodología de fricción de la demanda"? | 🔴 **Abierta** | Es el filtro por el que pasa cualquier solicitud. ⭐ **Conocerla es saber cómo se escribe una solicitud que pasa** |
| **P18** | ¿Qué proporción del feedback negativo es capa A? | 🔴 **Abierta** | La PO dice que "está más en relación a" documentación desactualizada. **Los logs deberían cuantificarlo** — primera pregunta a hacerles |
| **P19** | ¿Cómo se entra a las mesas de trabajo de los jueves? | 🔴 **Abierta** | ⭐⭐ Es el canal barato ya abierto. **Probablemente la pregunta operativa más rentable del proyecto** |
| **P13** | ¿AIDA nació para "soporte comercial"? | ✅ **RESUELTA — al revés** | **No: nació para consolidar información y reducir tiempo de búsqueda.** El soporte comercial se construyó encima |
| **P14** | ¿Cuál es el objetivo declarado según sus dueños? | ✅ **RESUELTA** | **Consolidar información y reducir tiempo de búsqueda.** ⚠️ Lo que **no** debe hacer sigue sin declararse — queda como pregunta viva |
| **P15** | ⛔⛔ ¿Qué servicio de Google indexa un **SharePoint** de Microsoft, y con qué límites? | 🔴 **Abierta y PRECISADA** | ⭐ **La PO declara que la base vive en SharePoint**, aunque la jefatura declaró que el motor es Google. Probablemente compatible (motor Google + repositorio SharePoint) pero **sin confirmar**. Algunos límites de SharePoint podrían sí aplicar. **Bloqueante de la Fase 5.** Existe un diagrama de arquitectura — pedirlo |

---

## 25. Insumos y evidencia

### 25.1 Primarios — internos de RIMAC

| # | Insumo | Nota |
|---|---|---|
| 1 | **Playbook del Asesor** (2026-08-14) — modelo de venta Vida, 5 bloques | Fuente canónica declarada. ⚠️ Contiene 8 pendientes y las discrepancias de catálogo de §8.3 |
| 2 | **Matriz de productos Vida RIMAC**, de fichas vigentes desde 2025-01-01 | Patrón oro para calificar exactitud |
| 3 | **Encuesta a 19 asesores** (2026) | Uso, satisfacción, temas más pedidos, conducta compensatoria |
| 4 | **Taller de Manejo de Objeciones** (36 invitados / 30 asistentes, 2026) | Drivers de valor y mejoras pedidas |
| 5 | **Auto-interrogación de AIDA** (2026-08-14) | ⚠️ **Autorreporte** — hipótesis a triangular |
| 6 | **Plan Piloto · Modelo de Experiencia de Venta Vida** (julio 2026) | ⚠️ Estado histórico; sus indicadores miden el **prototipo Claude** |
| 7 | **Mapa sistémico AS IS y diagnóstico Dx1-Dx3** (2026) | Origen del mapa de 6 frentes |
| 8 | **«La biblioteca de AIDA»** — research de Behavioral Design (agosto 2026) | Aporta la cuantificación de §9. ⚠️ Su cifra ancla tiene problema de cita abierto (F-489) y **no se usa** |
| 9 | **Reunión con la jefatura** (agosto 2026) | Resuelve P9, declara la ausencia de sandbox, fija el encuadre |

### 25.2 Secundarios — evidencia externa, por rigor

| # | Fuente | ID |
|---|---|---|
| 1 | **Brynjolfsson, Li & Raymond (2025)**, *QJE* 140(2) — 5.179 agentes, despliegue escalonado | F-476 |
| 2 | **Franke & Park (2006)**, *JMR* 43(4) — 155 muestras, >31.000 vendedores | F-477 |
| 3 | **Dietvorst, Simmons & Massey (2015)**, *JEP: General* 144(1), 114-126 | F-494 |
| 4 | **Kluger & DeNisi (1996)**, *Psychological Bulletin* 119(2) — 607 tamaños de efecto | F-495 |
| 5 | **Macnamara, Hambrick & Oswald (2014)**, *Psychological Science* 25(8) — 88 estudios | F-496 |
| 6 | **JMIR (2024)** 26:e56195 — 27 ECAs / 1.480 participantes · **Cook et al. (2011-2012)**, *JAMA* | F-497, F-498 |
| 7 | **Ovadia et al. (2024)** · **Gekhman et al. (2024)**, *EMNLP* | F-490, F-491 |
| 8 | **Zheng et al. (2023)**, MT-Bench, *NeurIPS* · **Liu et al. (2023)**, G-Eval, *EMNLP* | F-159, F-158 |
| 9 | **Magesh et al. (2025)**, Stanford RegLab · **Ding et al. (2025)**, *AAAI* | F-493 |
| 10 | **Flanagan (1954)**, *Psychological Bulletin* 51(4) | F-485 |
| 11 | **King & He (2006)**, *Information & Management* 44(1) — 88 estudios. ⚠️ **Coeficientes específicos no verificados** | F-492 |
| 12 | **Lopez Bernal et al. (2018)** · **Hemming & Taljaard (2020)**, *IJE* | F-487, F-486 |
| 13 | **OHR-Bench** (ICCV 2025) · **REAL-MM-RAG** (ACL 2025) · **ColPali** (ICLR 2025) · **«The Power of Noise»** (SIGIR 2024) | F-469 a F-475 |
| 14 | **METR (2025)** — brecha percepción-desempeño. ⚠️ Preprint | F-488 |

### 25.3 ⚠️ Lo que quedó deliberadamente fuera

Cuatro familias de cifras que circulan en este mercado **no entraron** por no tener fuente primaria
rastreable. Quedan registradas como trampas:

| Cifra | Por qué no entra | ID |
|---|---|---|
| Adopción de metodologías de venta | Las cifras disponibles vienen de vendors de *sales enablement* | F-481 |
| Aceleración por configuradores de producto | **12 de 12 fuentes** son del proveedor que vende el configurador | F-483 |
| Retorno de gestión de datos maestros (MDM) | Mecanismo real, cifra de vendor, alta tasa de fracaso de implementación | F-484 |
| «79,5% → 24,2%» por documentos contradictorios | El arXiv citado resuelve a otro paper, con otro mecanismo | F-489 |

---

## 26. Limitaciones

- ⚠️ **El diagnóstico no está ejecutado.** La auditoría estructurada, el shadowing y el registro de
  fallos técnicos **están pendientes**. Todo lo que este documento presenta como "lo que encontramos"
  es lectura preliminar de fuentes existentes, no resultado de campo cerrado.
- ⚠️ **Nunca se ha inspeccionado la configuración de AIDA.** Toda la sección de arquitectura es
  autorreporte de la herramienta más deducción. No hay inspección técnica.
- ⚠️ **F-476 es de soporte al cliente, no de venta consultiva de vida.** Dirección sólida, **magnitud a
  validar en población propia**.
- ⚠️ **Los datos de campo provienen de una muestra chica** (19 encuestados, 30 asistentes al taller) y
  sin cortes por antigüedad todavía aplicados.
- ⚠️ **El umbral de formato del Playbook (§8.3c) hay que recalcularlo** contra los límites reales del
  servicio Google. La recomendación de partir y des-tabular sobrevive; el número no.
- ⚠️ **Los coeficientes de King & He citados en §20** provienen del research interno; se verificó el
  paper y su muestra, no esos coeficientes.
- ⚠️ **P10 sin resolver.** "El modelo SHUNK" se incorpora al plan de evaluación en cuanto se confirme
  cuál es. **No se aplica por aproximación.**

---

## Conexiones

- `[[diagnostico-copiloto-ai-asesor-vida-rimac]]` — el node que es fuente de verdad del estado interno
  y de las decisiones. Este documento lo consolida; ese node manda.
- `[[arquitectura-conocimiento-agentes-copilot]]` — la evidencia externa sobre cómo almacenar el
  conocimiento. ⛔ Su parte específica de Copilot **ya no aplica** a AIDA.
- `[[proyecto-back-to-basics-ffvv-vida]]` — el proyecto marco. De ahí vienen el modelo de venta, la
  encuesta y el taller.
- `[[matriz-productos-vida-rimac]]` — el catálogo que la base debe representar correctamente, y la
  especificación de la matriz que §11.2 propone promover a fuente canónica.
- `[[evaluacion-calidad-agentes-conversacionales-ia]]` — los tres ejes de medición y las escalas.
- `[[modelo-salud-ia-farmacias-peru]]` — de donde salen las estrategias de testeo reutilizadas en §23.
- `[[futuro-asesores-seguros-venta-digital]]` — el marco de por qué potenciar al asesor humano en vez
  de reemplazarlo.
