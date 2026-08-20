# Diagnóstico de AIDA — la arquitectura de cuatro frentes

**Marco del diagnóstico + entrega del frente 3.** v1.0 · 2026-08-20
Definición de la arquitectura: Alejo, 2026-08-20.

---

## La arquitectura

El diagnóstico se organiza en cuatro frentes, cada uno con su método y su límite:

| # | Frente | Método | Qué responde | Estado |
|---|---|---|---|---|
| **1** | **Owners / creadores** | Entrevistas con owners · documentación interna · información externa y de redes | **Para qué fue creada** | 🟡 **Avanzado** — falta la capa externa |
| **2** | **Asesores (usuarios)** | Encuesta a grupo grande · mini etnografías con grupo pequeño | **Qué hacen con ella**, y con las IA de afuera | 🟡 **Parcial** — encuesta chica hecha, etnografías pendientes |
| **3** | **Cliente (usuario final)** | Análisis de casuística en el log | **Qué problemática del cliente tiene que resolver el asesor** | ✅ **ENTREGADO — ver §3** |
| **4** | **Auditoría de la herramienta** | Calidad de respuestas en el log · auditoría con otro LLM | **Cuál es su estándar y dónde falla** | 🟡 **Mitad hecha** — log analizado, LLM pendiente |

⭐ **Por qué esta arquitectura es correcta:** cada frente responde una pregunta que **ningún otro
puede responder**, y los cuatro se triangulan. La promesa (frente 1) se contrasta contra la conducta
(2), contra la necesidad real (3) y contra la capacidad medida (4). **Ninguno solo alcanza.**

---

## 1. Frente de los owners — qué falta

**Lo que ya existe:**
- ✅ **Entrevista con la PO** (Radille): objetivo declarado, dos AIDAs, arquitectura, medición,
  gobierno, y el proceso de solicitud de cambios.
- ✅ **Documentación interna de RIMAC** sobre el proyecto AIDA.
- ✅ **Auto-descripción de la herramienta** — lo que AIDA dice de sí misma.

**Lo que falta, y es lo nuevo de esta definición:**

| Pendiente | Por qué importa |
|---|---|
| ⭐ **Información externa y de redes sociales** | Si AIDA se comunicó hacia afuera —LinkedIn corporativo, prensa, premios, casos de proveedor— **esa es una declaración pública de propósito** que se puede contrastar contra lo que hace. Y es la única fuente que no controla nadie de adentro |
| **Entrevista con Emanuel, Will y Miguel** | La PO respondió por la capacidad. Falta la capa de **arquitectura y roadmap** — y **P15**, qué servicio de Google es exactamente |
| **El diagrama de arquitectura** | Existe. Radille lo mencionó. Acceso no confirmado |
| ⚠️ **Qué se espera que AIDA NO haga** | La PO declaró el objetivo, no el límite. **Sigue abierta** |

⭐ **Nota de método para la capa externa:** lo que se diga de AIDA hacia afuera hay que tratarlo como
**declaración de intención, no como evidencia de desempeño** — es exactamente la clase de fuente que
este proyecto viene marcando con descuento. Sirve para medir la brecha entre lo prometido y lo
entregado, no para probar que funciona.

---

## 2. Frente de los asesores — qué falta

**Lo que ya existe:** encuesta a 19 asesores · taller de objeciones (30 asistentes) · el kit de campo
listo para enviar · y ahora, **la conducta real de 274 asesores en los logs**.

**Lo que falta:**

| Pendiente | Nota |
|---|---|
| **Encuesta a un grupo grande** | ⭐ La de 19 sirve para tipificar, no para estimar. Herramienta disponible: **Wiser**, vía Dani. ⚠️ Los asesores tienen IA bloqueada en la computadora — **responden desde el teléfono** |
| **Mini etnografías** | 4-6 asesores. ⭐ Muestreo deliberado: **el que declaró no usarla nunca es la entrevista más informativa que existe** |
| ⭐ **Uso de IA de afuera** | ChatGPT y Gemini están confirmados por autorreporte. **Lo que falta es el cuándo y el para qué** — sobre todo si ocurre *durante* la conversación con el cliente |

⭐⭐ **Y ahora hay una pregunta nueva para este frente, que sale del frente 3** (§3.4): por qué el
manejo de objeciones es lo que más piden y casi nunca se lo preguntan a AIDA. **Es la pregunta de
campo más valiosa que existe hoy**, y solo se responde preguntándola.

---

# 3. ⭐ FRENTE DEL CLIENTE — entregado

**Método:** clasificación de las **2.697 consultas** del log (agente `ffvv`, excluida la cuenta de
servicio) según **qué problema del cliente hay detrás de cada pregunta**. La taxonomía se derivó
leyendo una muestra, no se impuso desde afuera.

⚠️ **Límite de esta inferencia, declarado:** el log dice **qué le pregunta el asesor a AIDA**, no qué
le pregunta el cliente al asesor. Es un **proxy**, y tiene un sesgo conocido: solo aparece lo que el
asesor decidió consultar. **Lo que resuelve solo, o le pregunta a otro, no está.** Aun así es la
aproximación más barata y más grande que existe hoy — 2.697 casos reales.

### 3.1 Qué tiene que resolver el asesor

| Problemática del cliente | Consultas | % |
|---|---|---|
| **Dato de producto** — qué es, qué incluye, cuánto cuesta | 541 | **20,1%** |
| **Cómo abordarlo** — el asesor necesita las palabras para entrar | 357 | **13,2%** |
| **¿Está cubierto mi caso?** — siniestro, enfermedad, accidente | 211 | 7,8% |
| *(continuaciones de conversación)* | 225 | 8,3% |
| **Trámite u operativa** — documentos, emisión, cobranza | 162 | 6,0% |
| ⭐ **Comparación entre opciones** | 111 | 4,1% |
| ⭐ **Riesgo de mercado y rentabilidad** | 97 | 3,6% |
| ⭐ **Flexibilidad — "¿y si cambio de idea?"** | 84 | 3,1% |
| **¿Encaja este cliente?** — edad, requisitos | 65 | 2,4% |
| **Explicar un concepto** | 47 | 1,7% |
| **Objeción o resistencia** | 31 | **1,1%** |
| *(sin clasificar)* | 766 | 28,4% |

### 3.2 ⭐⭐ Tres problemáticas del cliente que el proyecto no tenía mapeadas

**a) El cliente pregunta qué pasa si cambia de idea.** 84 consultas sobre **flexibilidad**, y son
notablemente concretas:

> *"¿A partir de cuándo se pueden desactivar las coberturas adicionales?"* · *"¿Desde qué mes se
> puede cambiar de beneficiarios?"* · *"¿Puedo retirar dinero sin perder la protección de vida?"* ·
> *"¿Puedo agregar cobertura de invalidez después de contratado?"* · ⭐ *"¿Si mi hijo no quiere ir a
> la universidad, pierdo mi dinero?"*

⭐ **No es una pregunta de cobertura: es una pregunta de arrepentimiento.** El cliente está evaluando
comprometerse a 15 o 20 años y quiere saber cuánto puede deshacer. **Es una objeción disfrazada de
consulta técnica**, y hoy nadie la está tratando como objeción.

**b) El cliente compara contra cosas que no son seguros.** 111 consultas de comparación, y el
contraste no siempre es entre productos RIMAC:

> *"¿Cuáles son las diferencias entre un seguro de vida, AFP, plazo fijo y ahorros en cuenta
> propia?"* · *"¿Cuál es mejor entre el AG o el Flexivida?"* · *"¿Por qué un Vida Ahorro Garantizado
> cotizado desde la web sale más barato que desde el journey?"*

⭐ **La competencia por el ahorro del cliente no es otra aseguradora: es el banco y la AFP.** Y la
última pregunta es peor: **el propio canal digital de RIMAC le está compitiendo el precio al asesor.**

**c) El cliente tiene miedo del mercado.** 97 consultas sobre rentabilidad y riesgo:

> *"¿Qué pasa si el mercado financiero cae en el plan Vida Flexible?"* · *"¿Existe una garantía
> mínima de capital en caso de caídas severas?"* · *"¿En qué se invierten los fondos del Flexivida?"*

⚠️ **Y acá hay un dato preocupante que sale del cruce con el frente 4: el 48,5% de estas respuestas
no cita ninguna fuente** — el peor porcentaje de todas las categorías. **Casi la mitad de lo que
AIDA dice sobre rentabilidad lo dice sin respaldo documental**, en productos de inversión, que es
donde un dato inventado tiene el máximo riesgo regulatorio.

### 3.3 ⭐⭐⭐ El patrón que ordena todo: AIDA responde lo declarativo y falla lo deliberativo

Cruzando la clasificación con la calificación de los asesores:

| Problemática | % calificaciones negativas | vs. base (4,0%) |
|---|---|---|
| ⚠️ **Explicar un concepto al cliente** | **10,3%** | **2,6×** |
| ⚠️ **Comparación entre opciones** | **9,2%** | **2,3×** |
| ⚠️ **Objeción o resistencia** | **8,7%** | **2,2×** |
| ⚠️ **¿Encaja este cliente?** | 7,7% | 1,9× |
| ⚠️ **Trámite u operativa** | 7,2% | 1,8× · **32,7% sin cita** |
| Dato de producto | 4,6% | 1,2× |
| Cómo abordar o contactar | 2,5% | 0,6× |
| ¿Está cubierto? / siniestro | 1,2% | 0,3× |
| **Flexibilidad — ¿y si cambio de idea?** | **0,0%** | ✅ |

⭐⭐⭐ **AIDA sabe decir qué es un producto. Falla cuando hay que comparar, explicar o persuadir** —
es decir, **cuando el asesor necesita ayuda para pensar con el cliente, no para recordar un dato.**

**Y eso choca de frente con la evidencia del proyecto:**
- Lo único con efecto verificado sobre desempeño **objetivo** es la **venta adaptativa** — leer al
  cliente y cambiar de camino en vivo.
- El tema **más pedido** por los asesores es **manejo de objeciones** (42%).
- El momento de **mayor necesidad declarada** es **el cierre**.

⭐ **AIDA es peor justamente donde más se la necesita.**

### 3.4 ⭐⭐⭐ La contradicción más informativa del análisis

> **El manejo de objeciones es el tema #1 que los asesores dicen necesitar (42% en la encuesta).
> Y es el 1,1% de lo que efectivamente le preguntan a AIDA.**

Esa brecha —de 42% declarado a 1,1% observado— **no puede explicarse por casualidad**. Tres
hipótesis, y las tres son accionables:

| Hipótesis | Cómo se comprueba |
|---|---|
| **1 · Ya aprendieron que no sirve para eso** | Es la 3ª categoría con peor calificación (8,7%). **Consistente con abandono selectivo** |
| **2 · Lo resuelven en ChatGPT o Gemini** | Preguntarlo directo en el campo — es la pregunta #1 del kit |
| **3 · No se les ocurre pedírselo** | Es el problema de la pantalla en blanco: nada le dice al asesor que puede pedir eso |

⭐⭐ **Y este es exactamente el hallazgo que dije que la telemetría no podía dar** —qué dejaron de
preguntar— **encontrado por otra vía: comparando lo declarado contra lo observado.** No hizo falta la
serie temporal larga; bastó cruzar la encuesta con el log.

**Las tres hipótesis se distinguen con una sola pregunta en campo**, y está en el kit:
> *"¿Hay algo que antes le preguntabas a AIDA y ya no? ¿Qué pasó?"*

### 3.5 Qué NO puede responder este frente

- ⛔ **Qué pregunta el cliente que el asesor nunca consulta.** El log solo ve lo que llegó a AIDA.
- ⛔ **Qué problemática pesa más en la decisión de compra.** Frecuencia de consulta ≠ importancia.
- ⛔ **Si el cliente quedó satisfecho.** No hay ningún dato del cliente en el log.
- ⚠️ **Y el 28,4% sin clasificar** es real: preguntas muy específicas de caso, continuaciones
  ambiguas y consultas de otros ramos. **No se fuerza a entrar en una categoría.**

---

## 4. Frente de la auditoría — mitad hecha

**✅ Lo hecho:** análisis completo del log — inestabilidad de recuperación (68,2%), duplicación de
documentos por producto, contaminación cruzada de ramos, formatos, patrón de calificaciones, y la
**contradicción de cifras verificada caso por caso**.

**🟡 Lo que falta:** la auditoría con otro LLM. El instrumento está listo (bancos F, G, H + protocolo
del juez con calibración κ≥0,60), y **el análisis del log lo mejora**: el banco sintético se
reemplaza por las preguntas reales, y ahora se sabe **dónde apuntar** — a las categorías con peor
calificación de §3.3, no a preguntas de producto genéricas.

⭐ **Reorientación que sale del frente 3:** la auditoría debe cargar el peso en **comparar, explicar y
manejar objeciones**, no en datos de cobertura, que es donde AIDA ya funciona bien.

---

## 5. Cómo se triangulan los cuatro

⭐ **El valor no está en cada frente por separado sino en los cruces.** Los que ya rindieron:

| Cruce | Qué produjo |
|---|---|
| **1 × 4** — promesa contra capacidad | El objetivo declarado es *consolidar y reducir tiempos*, y **ningún indicador del dashboard mide tiempo** |
| **2 × 3** — lo declarado contra lo observado | ⭐⭐ La brecha del 42% al 1,1% en objeciones (§3.4) |
| **3 × 4** — necesidad contra desempeño | ⭐⭐⭐ AIDA falla justo en lo deliberativo, que es donde está el valor verificado |
| **1 × 2** — para qué se creó contra cómo se usa | El uso está en la variable del asesor: **la adopción no mide utilidad** |

**Cruces todavía sin explotar:**
- **1 externo × 4** — lo que se dijo públicamente contra lo que la auditoría mide.
- **2 etnografía × 3** — ver si las problemáticas del log coinciden con las que el asesor enfrenta
  cuando nadie lo mira.

---

## 6. Lo que hay que hacer, en orden

| # | Acción | Frente | Cuándo |
|---|---|---|---|
| 1 | 🔴 **Pedir el histórico completo** con el rango declarado | 3 y 4 | Ya |
| 2 | **Correr la auditoría con LLM**, apuntada a comparar/explicar/objetar | 4 | Jue-lun |
| 3 | **Lanzar la encuesta grande** en Wiser | 2 | Vie |
| 4 | ⭐ **Preguntar por la brecha de objeciones** en las etnografías | 2 | Vie-lun |
| 5 | **Buscar la capa externa** — qué se dijo de AIDA hacia afuera | 1 | Lun |
| 6 | **Llevar P14 y P15 a la reunión** del miércoles | 1 | Mié |

---

## Conexiones

- `[[aida-analisis-logs-2026-08-20]]` — el análisis del que sale el frente 3 y la mitad del 4.
- `[[aida-kit-campo-asesores]]` — el instrumento del frente 2.
- `[[protocolo-interrogacion-aida-vida]]` — el instrumento del frente 4.
- `[[diagnostico-copiloto-ai-asesor-vida-rimac]]` — §19, la entrevista que cubre el frente 1.
- `[[aida-dossier-y-plan-faseado]]` — el dossier que este marco reorganiza.
