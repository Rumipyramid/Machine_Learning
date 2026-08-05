# Guía de preguntas — Estudio de triaje digital + kit · 200 usuarios sintéticos (`lapuerta`)

> Simulación de la *Guía de preguntas* (facilitadores) sobre una población sintética de
> **200 peruanos de 18 a 65 años, NSE A, B y C**, generada con el modelo `lapuerta`
> (semilla 42, reproducible).
> Fecha: 2026-08-05 · Proyecto `Rumipyramid/Machine_Learning`.
> Script: `simulate_guia_triaje.py` · CSV con los 200 perfiles y sus respuestas:
> `guia_triaje_200_usuarios.csv`.

---

## ⚠️ Lo primero: qué se pudo y qué no se pudo responder

**El prototipo no es alcanzable desde este entorno.** `https://vivo-triaje.vercel.app`
devuelve **403 al CONNECT** en el gateway de red del entorno — es una **denegación de
política**, no un fallo transitorio ni un problema del sitio (el mismo gateway bloquea otros
dominios externos; se verificó con `curl` directo y con el endpoint de estado del proxy).
Intenté además cargarlo con navegador headless y con fetch, con el mismo resultado.

Por lo tanto apliqué tu instrucción de respaldo: **se responden solo las preguntas de la guía
que no requieren haber usado el prototipo ni el kit físico.**

| Sección de la guía | ¿Respondida? | Motivo |
|---|---|---|
| PARTE 1 — Screener (WhatsApp) | ✅ Sí | No requiere prototipo |
| Para conocerte (edad, seguro, para quién) | ✅ Sí | No requiere prototipo |
| Punto de partida (último malestar, por qué, medicamentos) | ✅ Sí | Conducta pasada, no requiere prototipo |
| **Sobre el asistente digital** (5 preguntas) | ❌ **No** | Requiere usar el prototipo |
| **Sobre el kit** (3 preguntas) | ❌ **No** | Requiere el kit físico (además marcado "activado a partir del jueves") |
| Si a las 24-48h no mejoras, ¿qué harías? | ✅ Sí | Hipotético de escalamiento, no requiere prototipo |
| Cierre (solución ideal) | ✅ Sí | Aspiracional, no requiere prototipo |

**De las 16 preguntas sustantivas de la guía, se respondieron 8; quedaron sin responder las 8
de evaluación de UX del prototipo y del kit.** Al final del informe está la lista exacta.

**Cómo destrabarlo:** si me pegas el flujo del prototipo (pantallas, textos, qué pregunta,
qué recomienda al ingresar "resfrío + dolor de garganta sin fiebre alta"), o exportas el
recorrido a texto/capturas, puedo correr también las 8 preguntas restantes sobre estos mismos
200 perfiles.

---

## 0. Nota metodológica (leer antes de usar las cifras)

**Qué es esto y qué no es.** `lapuerta` genera perfiles sintéticos cuyas *marginales*
reproducen datos reales del consumidor peruano de seguros (SBS, APESEG, APEIM, ENAHO). Sirve
para **prototipar, explorar hipótesis y estresar un guion de entrevista antes de campo** — no
sustituye entrevistas reales ni prueba relaciones causales. Ninguna de estas 200 personas
existe.

**Tres decisiones declaradas que afectan la lectura:**

1. **El screener de WhatsApp es un supuesto, no un dato.** El modelo `lapuerta` no tiene
   variable "usa WhatsApp". La derivé de `acceso_digital` (alta → 0.97 · media → 0.85 ·
   baja → 0.45). Es la pieza más débil de esta simulación; en campo real el screener
   probablemente filtre distinto.
2. **El techo de 65 años se impuso truncando.** El modelo define su cohorte mayor como
   "Boomer 60+" sin techo superior; para respetar tu rango 18-65 asigné a esa cohorte edades
   de 60 a 65. Eso hace que el tramo 60-65 esté **sobrerrepresentado** frente a la población
   real de esa edad exacta.
3. **El reparto de aseguradoras es invención razonada, no market share.** No hay dato de
   participación de mercado de salud privada verificado en el ledger del proyecto, así que la
   distribución entre RIMAC / Pacífico / Mapfre / La Positiva / Sanitas **no debe citarse**.

**Calibración de la sección de conducta.** Las proporciones de "Punto de partida" no las
inventé: están ancladas en la investigación propia del proyecto
(`research/_nodes/modelo-salud-ia-farmacias-peru.md` §1.1-§1.4, fuentes F-35, F-36, F-38,
F-39, F-48). Una primera versión de las reglas produjo 80.3% de automedicación —**fuera** del
rango documentado (20-68%) y con segmentos saturados en 100%— así que comprimí los
coeficientes y amplié el ruido hasta que la marginal cayera dentro del rango. El resultado
final (63.6%) sí está dentro. Dejo constancia porque el número inicial habría sido engañoso.

---

## 1. Composición de la muestra (200 perfiles)

| Dimensión | Distribución |
|---|---|
| **NSE** | C = 132 · B = 60 · A = 8 |
| **Generación** | Gen X (44-59) = 61 · Millennial (28-43) = 53 · Boomer (60-65) = 53 · Gen Z (18-27) = 33 |
| **Región** | Lima Metropolitana = 70 · Sierra = 59 · Resto Costa = 45 · Selva = 26 |
| **Situación laboral** | Formal dependiente = 90 · Independiente/microemprendedor = 58 · Informal = 52 |
| **Tenencia de seguro** | Ninguno = 78 · Solo obligatorio = 66 · Voluntario = 56 |
| **Confianza en aseguradoras** | Desconfía = 98 · Neutral = 55 · Confía plenamente = 47 |
| **Acceso digital** | Alta = 94 · Media = 85 · Baja = 21 |
| **Educación financiera** | Baja = 103 · Media = 70 · Alta = 27 |
| **Edad** | min 18 · mediana 47 · max 65 |

> **Ojo con NSE A (n=8).** La muestra refleja la distribución real de NSE en Perú, donde A es
> una fracción pequeña. Con n=8, **cualquier porcentaje de NSE A en este informe es
> estadísticamente inútil** — lo reporto para completitud, no para decidir.

---

## 2. PARTE 1 — Screener

**¿Sueles usar WhatsApp para comunicarte en tu día a día?**

| Respuesta | % | n |
|---|---|---|
| ✅ Sí — continúa la sesión | 86.5% | 173 |
| ❌ No — queda fuera del estudio | 13.5% | 27 |

**Muestra elegible para la guía principal: 173 de 200.** Todo lo que sigue se calcula sobre
esos 173.

**Lectura para el equipo:** el screener de WhatsApp descarta ~1 de cada 7. Los descartados se
concentran en `acceso_digital` baja, que a su vez correlaciona con NSE C, mayor edad y
regiones fuera de Lima. **Ese filtro no es neutral: está sacando del estudio justamente al
segmento con más fricción de acceso al sistema formal de salud** — que es, plausiblemente, a
quien más le serviría el servicio. Vale decidirlo a conciencia, no por defecto.

---

## 3. PARTE 2 — Para conocerte (n=173)

**¿Cuántos años tienes?**

| Tramo | % | n |
|---|---|---|
| 44-59 | 30.1% | 52 |
| 28-43 | 27.2% | 47 |
| 60-65 | 24.3% | 42 |
| 18-27 | 18.5% | 32 |

**¿Tienes algún seguro de salud privado?**

| Respuesta | % | n |
|---|---|---|
| No | 87.9% | 152 |
| Sí | 12.1% | 21 |

*(El reparto por aseguradora entre esos 21 es supuesto — ver nota metodológica. No citar.)*

**Cuando buscas ayuda para un malestar, ¿es para ti o también para otros?**

| Respuesta | % | n |
|---|---|---|
| Solo para mí | 43.4% | 75 |
| También para hijos y/o un adulto mayor | 18.5% | 32 |
| También para mis hijos | 18.5% | 32 |
| También para mi pareja | 15.0% | 26 |
| También para otros en casa | 4.6% | 8 |

**Lectura:** **56.6% busca ayuda también para terceros**, no solo para sí mismo. Si el
asistente digital está diseñado en primera persona ("¿qué síntomas *tienes*?"), está
desalineado con la mayoría de los casos de uso. Un flujo que no permita declarar "es para mi
hijo / para mi mamá" pierde a más de la mitad de la demanda real desde la primera pantalla —
y en un producto de salud eso además cambia la recomendación (dosis pediátrica, interacciones
en adulto mayor).

---

## 4. Punto de partida — La última vez que te sentiste mal, ¿cómo lo resolviste?

| Respuesta | % | n |
|---|---|---|
| Fui a la farmacia y pedí algo sin receta | 32.9% | 57 |
| Me automediqué con lo que tenía en casa | 30.6% | 53 |
| Consulté a un familiar/conocido con criterio médico | 26.6% | 46 |
| Fui a una consulta médica formal | 9.8% | 17 |

> ### **63.6% resolvió sin ver a un médico** (110 de 173)
> Dentro del rango 20-68% documentado en `modelo-salud-ia-farmacias-peru.md` §1.1.

**¿Por qué lo abordaste así?**

| Motivo dominante | % | n |
|---|---|---|
| El sistema es lento / sacar cita toma mucho | 37.0% | 64 |
| No tenía tiempo | 20.8% | 36 |
| Era algo leve, no ameritaba médico | 16.2% | 28 |
| Por el costo | 9.8% | 17 |
| Era serio / tengo cobertura y la uso | 9.8% | 17 |
| No confío mucho en la atención médica | 6.4% | 11 |

**Este es el hallazgo más accionable de toda la simulación**, y replica el patrón que el
proyecto ya tenía documentado (F-38): **la desconfianza en el médico es el motivo *menos*
citado (6.4%)**. La gente no se automedica porque desconfíe de la medicina — se automedica
porque **el sistema formal es lento (37.0%) y no tiene tiempo (20.8%)**: 57.8% combinado, un
problema de *acceso*, no de *credibilidad*.

**Implicación de posicionamiento:** el asistente digital **no compite contra el médico**.
Compite contra **la cola, la cita a 3 semanas y el trámite**. Todo el mensaje de producto
debería vender *velocidad y resolución*, no *superioridad clínica* — un claim de "tan bueno
como un médico" ataca un problema que el usuario no tiene y activa un escrutinio que no
necesita (riesgo ya señalado en la tesis 10 de El Lobo, caso Babylon Health).

**¿Cómo hiciste con los medicamentos?**

| Fuente de la decisión | % | n |
|---|---|---|
| Me guie por consejo de familia/conocidos | 40.5% | 70 |
| Le pregunté al técnico de la farmacia | 20.8% | 36 |
| Reusé una receta anterior | 16.8% | 29 |
| Lo pedí por nombre, ya sabía cuál | 12.1% | 21 |
| Con receta del médico | 9.8% | 17 |

| Preferencia | % | n |
|---|---|---|
| Prefiero la marca conocida | 68.2% | 118 |
| Genérico está bien | 18.5% | 32 |
| Me da igual | 13.3% | 23 |

**Dos lecturas para el diseño del kit y de las recomendaciones:**

1. **El consejo ya es social, no profesional** (40.5% familia/conocidos + 20.8% técnico de
   farmacia = 61.3%). El asistente digital no entra a un vacío: entra a **competir con la
   cuñada y con el técnico del mostrador**, que son gratis, inmediatos y tienen confianza
   ganada. La barrera no es tecnológica.
2. **68.2% prefiere marca sobre genérico.** Si el kit trae genéricos por costo, hay una
   objeción predecible que conviene tener guionada antes de campo — no descubrirla en la
   sesión 12.

---

## 5. Si a las 24-48 horas no mejoras, ¿qué harías?

| Respuesta | % | n |
|---|---|---|
| Vuelvo a la farmacia por algo más fuerte | 36.4% | 63 |
| Espero un poco más a ver si pasa | 30.1% | 52 |
| Teleconsulta, si viene incluida | 24.9% | 43 |
| Voy al médico / clínica | 8.7% | 15 |

**🚨 Alerta de seguridad clínica — el hallazgo más incómodo del ejercicio.** Ante una falta de
mejora a 24-48h, **66.5% escala mal o no escala**: vuelve a la farmacia a subir la dosis
(36.4%) o simplemente espera (30.1%). Solo **8.7% va al médico**.

Esto significa que **el escalamiento no puede quedar librado a la iniciativa del usuario**. Si
el servicio no *empuja* activamente la derivación a las 48h (mensaje proactivo por WhatsApp,
que es justamente el canal del screener), el diseño está contando con un comportamiento que
2 de cada 3 personas no van a tener. Es el mismo patrón que el proyecto ya documentó para el
canal digital en seguros (`research/_nodes/futuro-asesores-seguros-venta-digital.md`): el
punto de falla no está en la entrada, está en el momento en que algo no sale bien.

**El dato optimista:** 24.9% sí tomaría una teleconsulta **"si viene incluida"** — la
condicional importa. La teleconsulta es la ruta de escalamiento con más tracción potencial,
pero solo si no aparece como un costo nuevo en el peor momento.

---

## 6. Cierre — ¿Cómo debería ser la solución ideal?

| Respuesta | % | n |
|---|---|---|
| Que un profesional me confirme antes de tomar algo | 32.4% | 56 |
| Digital, pero con un humano disponible si lo necesito | 24.9% | 43 |
| Rápida y digital, sin tener que hablar con nadie | 22.0% | 38 |
| Prefiero atención presencial | 20.8% | 36 |

**57.3% quiere validación humana en el circuito** (32.4% que confirme un profesional + 24.9%
digital con humano disponible). Solo **22.0% quiere un flujo 100% digital sin hablar con
nadie**.

Converge con lo que el proyecto ya encontró en otros canales: el modelo que gana no es el
digital puro ni el presencial puro — es el **híbrido con humano accesible**. La pregunta de
diseño no es *"¿cómo evitamos al humano?"* sino *"¿en qué momento exacto aparece, y cuánto
cuesta que aparezca?"*.

---

## 7. Cortes por segmento — % que resolvió sin médico

**Por NSE**

| NSE | n | % sin médico |
|---|---|---|
| C | 111 | 79.3% |
| B | 54 | 40.7% |
| A | 8 | 0.0% ⚠️ n insuficiente |

El gradiente por NSE es el más fuerte de todos: **NSE C se automedica casi el doble que
NSE B**. El caso de uso es sustancialmente más urgente en C.

**Por situación laboral**

| Situación | n | % sin médico |
|---|---|---|
| Informal | 41 | 92.7% |
| Independiente / microemprendedor | 49 | 69.4% |
| Formal dependiente | 83 | 45.8% |

Aún más marcado que NSE: **quien no tiene empleo formal casi nunca ve a un médico** por un
malestar leve. Tiene lógica — no hay licencia médica que lo cubra, y cada hora en una cola es
ingreso perdido. Es, de lejos, el segmento con mayor dolor y mayor disposición esperable.

**Por región**

| Región | n | % sin médico |
|---|---|---|
| Resto Costa | 41 | 78.0% |
| Sierra | 49 | 65.3% |
| Selva | 16 | 62.5% |
| Lima Metropolitana | 67 | 53.7% |

Consistente con el dato documentado de que en provincias la compra sin receta es más frecuente
que en Lima (36% vs. 32%).

**Por generación**

| Generación | n | % sin médico |
|---|---|---|
| Boomer (60-65) | 42 | 69.0% |
| Gen X (44-59) | 52 | 65.4% |
| Millennial (28-43) | 47 | 61.7% |
| Gen Z (18-27) | 32 | 56.2% |

Diferencias menores — **la generación es el peor predictor de los cuatro cortes**. Segmentar
esta propuesta por edad sería un error; NSE y formalidad laboral discriminan mucho más.

---

## 8. Las 8 preguntas que quedaron sin responder

Requieren interacción con el prototipo o con el kit físico:

**Sobre el asistente digital**
1. Sobre la experiencia general, ¿qué te pareció? ¿Por qué?
2. ¿Qué tan fácil te resultó? Poco / algo / muy fácil. ¿Por qué?
3. ¿Qué te gustó y qué no te gustó? ¿Por qué?
4. Sobre las recomendaciones que te mostró: ¿por qué elegiste esa? / ¿por qué no elegiste alguna?
5. ¿Qué mejorarías?

**Sobre el kit**
6. ¿Qué te pareció? ¿Por qué?
7. ¿Qué te gustó y qué no te gustó? ¿Por qué?
8. ¿Qué mejorarías?

**Por qué no las respondí en vez de improvisarlas:** simular una reacción de UX a un prototipo
que no pude ver sería inventar el hallazgo más importante del estudio. Las preguntas de arriba
son precisamente las que justifican hacer campo; fabricarlas destruiría el valor del ejercicio.

---

## 9. Qué haría con esto antes de salir a campo

1. **Revisar el screener de WhatsApp.** Filtra a ~13.5%, concentrado justo en el perfil de
   mayor fricción de acceso. Si la decisión es deliberada, perfecto; si es heredada del canal
   técnico, vale reconsiderarla.
2. **Agregar al guion la pregunta "¿para quién?" desde el inicio.** 56.6% busca ayuda para
   terceros; conviene saber si el prototipo lo soporta antes de que un participante choque
   con eso en vivo.
3. **Guionar la objeción marca vs. genérico** del kit (68.2% prefiere marca).
4. **Sondear el escalamiento explícitamente**, no solo preguntarlo. Con 66.5% escalando mal,
   vale contrastar lo que dicen que harían con lo que hacen — es el punto de mayor riesgo
   clínico y de mayor valor de diseño.
5. **No vender precisión clínica.** El motivo real es tiempo y lentitud del sistema (57.8%),
   no desconfianza médica (6.4%). El posicionamiento debería ser velocidad.

---

## 10. Limitaciones

- **Datos sintéticos.** Ninguna de las 200 personas existe. Sirve para afinar el guion y
  anticipar objeciones; **no** reemplaza las entrevistas reales ni prueba causalidad.
- **8 de 16 preguntas sin responder** por bloqueo de red al prototipo.
- **El screener de WhatsApp es el eslabón más débil** — supuesto derivado de `acceso_digital`.
- **NSE A (n=8) no es interpretable.** Tampoco Selva (n=16, n=26 antes del screener).
- **El reparto de aseguradoras es invención**, no market share verificado.
- **El tramo 60-65 está sobrerrepresentado** por el truncamiento del cohorte "60+".
- Las respuestas son **categóricas por reglas**, no verbatims: dan distribución y dirección,
  no el matiz cualitativo que sí daría una entrevista real.

---

*Generado con el skill `lapuerta` (semilla 42, reproducible). Script y CSV con los 200
perfiles y sus respuestas individuales disponibles. Calibración de conducta anclada en
`research/_nodes/modelo-salud-ia-farmacias-peru.md` (fuentes F-35, F-36, F-38, F-39, F-48 del
ledger `research/fuentes/codice.md`).*
