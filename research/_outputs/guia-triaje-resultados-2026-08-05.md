# Guía de preguntas — Resultados · 200 usuarios sintéticos

> Simulación de la *Guía de preguntas* (estudio de triaje digital) sobre **200 peruanos
> sintéticos de 18 a 65 años, NSE A, B y C**, generados con el modelo `lapuerta`
> (semilla 42, reproducible).
> Screener de WhatsApp: **173 elegibles** de 200. Todos los porcentajes se calculan sobre 173.
> 2026-08-05 · Proyecto `Rumipyramid/Machine_Learning`

---

## Los tres hallazgos que mueven decisiones

**1. El competidor no es el médico — es la cola.**
63.6% resolvió su último malestar sin ver a un médico. El motivo dominante es que el sistema
es lento (37.0%) y que no hay tiempo (20.8%). La desconfianza en la atención médica es el
motivo **menos** citado: 6.4%. El posicionamiento debería vender velocidad, no superioridad
clínica.

**2. Ante una falta de mejora, 2 de cada 3 escalan mal.**
Si a las 24-48h no mejoran, 36.4% vuelve a la farmacia por algo más fuerte y 30.1%
simplemente espera. Solo 8.7% va al médico. El escalamiento no puede quedar librado a la
iniciativa del usuario.

**3. La mayoría no busca ayuda solo para sí misma.**
56.6% busca también para hijos, pareja o un adulto mayor. Un flujo diseñado en primera
persona queda desalineado con la mayoría de los casos de uso desde la primera pantalla.

---

## Composición de la muestra (200 perfiles)

| Dimensión | Distribución |
|---|---|
| NSE | C = 132 · B = 60 · A = 8 |
| Generación | Gen X (44-59) = 61 · Millennial (28-43) = 53 · Boomer (60-65) = 53 · Gen Z (18-27) = 33 |
| Región | Lima Metropolitana = 70 · Sierra = 59 · Resto Costa = 45 · Selva = 26 |
| Situación laboral | Formal dependiente = 90 · Independiente = 58 · Informal = 52 |
| Tenencia de seguro | Ninguno = 78 · Solo obligatorio = 66 · Voluntario = 56 |
| Confianza en aseguradoras | Desconfía = 98 · Neutral = 55 · Confía plenamente = 47 |
| Acceso digital | Alta = 94 · Media = 85 · Baja = 21 |
| Educación financiera | Baja = 103 · Media = 70 · Alta = 27 |
| Edad | min 18 · mediana 47 · max 65 |

---

## PARTE 1 — Screener

### ¿Sueles usar WhatsApp para comunicarte en tu día a día?

| Respuesta | % | n |
|---|---|---|
| ✅ Sí — continúa la sesión | 86.5% | 173 |
| ❌ No — queda fuera del estudio | 13.5% | 27 |

**Lectura.** El screener descarta ~1 de cada 7, y los descartados se concentran en acceso
digital bajo — que correlaciona con NSE C, mayor edad y regiones fuera de Lima. El filtro no
es neutral: saca del estudio justamente al segmento con más fricción de acceso al sistema
formal de salud, que es plausiblemente a quien más le serviría el servicio.

---

## PARTE 2 — Para conocerte (n = 173)

### ¿Cuántos años tienes?

| Tramo | % | n |
|---|---|---|
| 44-59 | 30.1% | 52 |
| 28-43 | 27.2% | 47 |
| 60-65 | 24.3% | 42 |
| 18-27 | 18.5% | 32 |

### ¿Tienes algún seguro de salud privado?

| Respuesta | % | n |
|---|---|---|
| No | 87.9% | 152 |
| Sí | 12.1% | 21 |

*(La marca de aseguradora entre esos 21 quedó fuera de este informe: no hay dato de
participación de mercado verificado para respaldarla.)*

### Cuando buscas ayuda para un malestar, ¿es para ti o también para otros?

| Respuesta | % | n |
|---|---|---|
| Solo para mí | 43.4% | 75 |
| También para hijos y/o un adulto mayor | 18.5% | 32 |
| También para mis hijos | 18.5% | 32 |
| También para mi pareja | 15.0% | 26 |
| También para otros en casa | 4.6% | 8 |

**Lectura.** **56.6% busca ayuda también para terceros.** En un producto de salud esto no es
un detalle de copy: cambia la recomendación misma (dosis pediátrica, interacciones en adulto
mayor). Si el asistente no permite declarar "es para mi hijo / para mi mamá", pierde más de
la mitad de la demanda real y arriesga recomendar sobre el perfil equivocado.

---

## Punto de partida — La última vez que te sentiste mal, ¿cómo lo resolviste?

| Respuesta | % | n |
|---|---|---|
| Fui a la farmacia y pedí algo sin receta | 32.9% | 57 |
| Me automediqué con lo que tenía en casa | 30.6% | 53 |
| Consulté a un familiar/conocido con criterio médico | 26.6% | 46 |
| Fui a una consulta médica formal | 9.8% | 17 |

> ### **63.6% resolvió sin ver a un médico** (110 de 173)

### ¿Por qué lo abordaste así?

| Motivo dominante | % | n |
|---|---|---|
| El sistema es lento / sacar cita toma mucho | 37.0% | 64 |
| No tenía tiempo | 20.8% | 36 |
| Era algo leve, no ameritaba médico | 16.2% | 28 |
| Por el costo | 9.8% | 17 |
| Era serio / tengo cobertura y la uso | 9.8% | 17 |
| No confío mucho en la atención médica | 6.4% | 11 |

**Lectura — el hallazgo más accionable del estudio.** La desconfianza médica es el motivo
menos citado. La gente no se automedica porque dude de la medicina: se automedica porque
**el sistema formal es lento (37.0%) y no tiene tiempo (20.8%)** — 57.8% combinado. Es un
problema de **acceso**, no de **credibilidad**.

Consecuencia directa para el producto: el asistente no compite contra el médico, compite
contra la cola y la cita a tres semanas. Un claim de "tan bueno como un médico" ataca un
problema que el usuario no tiene, y abre un escrutinio clínico que el producto no necesita.

### ¿Cómo hiciste con los medicamentos?

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

**Lectura.** El consejo ya es social, no profesional: 61.3% se guía por familia/conocidos o
por el técnico del mostrador. El asistente digital no entra a un vacío — entra a competir con
alguien gratis, inmediato y con confianza ya ganada. Y con 68.2% prefiriendo marca sobre
genérico, si el kit trae genéricos por costo hay una objeción predecible que conviene tener
guionada antes de campo.

---

## Si a las 24-48 horas no mejoras, ¿qué harías?

| Respuesta | % | n |
|---|---|---|
| Vuelvo a la farmacia por algo más fuerte | 36.4% | 63 |
| Espero un poco más a ver si pasa | 30.1% | 52 |
| Teleconsulta, si viene incluida | 24.9% | 43 |
| Voy al médico / clínica | 8.7% | 15 |

**Lectura — alerta de seguridad clínica.** **66.5% escala mal o no escala**: sube la dosis por
cuenta propia o espera. Solo 8.7% va al médico.

Si el servicio no *empuja* activamente la derivación a las 48h — por ejemplo con un mensaje
proactivo por WhatsApp, que es justamente el canal del screener — el diseño está contando con
un comportamiento que 2 de cada 3 personas no van a tener.

El dato aprovechable: 24.9% sí tomaría una teleconsulta, pero **"si viene incluida"**. La
condicional importa: es la ruta de escalamiento con más tracción, siempre que no aparezca
como un costo nuevo en el peor momento.

---

## Cierre — ¿Cómo debería ser la solución ideal?

| Respuesta | % | n |
|---|---|---|
| Que un profesional me confirme antes de tomar algo | 32.4% | 56 |
| Digital, pero con un humano disponible si lo necesito | 24.9% | 43 |
| Rápida y digital, sin tener que hablar con nadie | 22.0% | 38 |
| Prefiero atención presencial | 20.8% | 36 |

**Lectura.** **57.3% quiere validación humana en el circuito**; solo 22.0% quiere un flujo
100% digital sin hablar con nadie. La pregunta de diseño no es *"¿cómo evitamos al humano?"*
sino *"¿en qué momento exacto aparece, y cuánto cuesta que aparezca?"*.

---

## Cortes por segmento — % que resolvió sin médico

### Por situación laboral — el corte más discriminante

| Situación | n | % sin médico |
|---|---|---|
| Informal | 41 | 92.7% |
| Independiente / microemprendedor | 49 | 69.4% |
| Formal dependiente | 83 | 45.8% |

Quien no tiene empleo formal casi nunca ve a un médico por un malestar leve. Tiene lógica: no
hay licencia médica que lo cubra y cada hora en una cola es ingreso perdido. Es el segmento
con mayor dolor y mayor disposición esperable.

### Por NSE

| NSE | n | % sin médico |
|---|---|---|
| C | 111 | 79.3% |
| B | 54 | 40.7% |
| A | 8 | — *(n insuficiente, no interpretable)* |

NSE C se automedica casi el doble que NSE B.

### Por región

| Región | n | % sin médico |
|---|---|---|
| Resto Costa | 41 | 78.0% |
| Sierra | 49 | 65.3% |
| Selva | 16 | 62.5% |
| Lima Metropolitana | 67 | 53.7% |

### Por generación

| Generación | n | % sin médico |
|---|---|---|
| Boomer (60-65) | 42 | 69.0% |
| Gen X (44-59) | 52 | 65.4% |
| Millennial (28-43) | 47 | 61.7% |
| Gen Z (18-27) | 32 | 56.2% |

**La generación es el peor predictor de los cuatro cortes.** Segmentar esta propuesta por edad
sería un error: formalidad laboral y NSE discriminan mucho más.

---

## Qué haría con esto antes de salir a campo

1. **Revisar el screener de WhatsApp** — filtra a 13.5%, concentrado justo en el perfil de
   mayor fricción de acceso.
2. **Agregar "¿para quién?" al inicio del guion** — 56.6% busca ayuda para terceros; conviene
   saber si el prototipo lo soporta antes de que un participante choque con eso en vivo.
3. **Guionar la objeción marca vs. genérico** del kit (68.2% prefiere marca).
4. **Sondear el escalamiento, no solo preguntarlo** — con 66.5% escalando mal, vale contrastar
   lo que dicen que harían contra lo que hacen. Es el punto de mayor riesgo clínico.
5. **No vender precisión clínica** — el motivo real es tiempo y lentitud (57.8%), no
   desconfianza médica (6.4%).

---

## Cómo leer estas cifras

- **Son datos sintéticos.** Ninguna de las 200 personas existe. `lapuerta` genera perfiles
  cuyas marginales reproducen datos reales del consumidor peruano (SBS, APESEG, APEIM,
  ENAHO). Sirve para **afinar el guion y anticipar objeciones antes de campo** — no sustituye
  las entrevistas reales ni prueba causalidad.
- **La sección de conducta está calibrada**, no inventada: las proporciones de "Punto de
  partida" están ancladas en la investigación propia del proyecto
  (`research/_nodes/modelo-salud-ia-farmacias-peru.md`, fuentes F-35, F-36, F-38, F-39, F-48).
  El 63.6% de automedicación cae dentro del rango documentado de 20-68%.
- **El screener de WhatsApp es el eslabón más débil:** el modelo no tiene esa variable, la
  derivé de `acceso_digital`. Es supuesto, no dato.
- **NSE A (n=8) y Selva (n=16) no son interpretables** por tamaño de muestra.
- **El tramo 60-65 está sobrerrepresentado**: el modelo define su cohorte mayor como "60+" sin
  techo, y la trunqué para respetar el rango 18-65 del estudio.
- Las respuestas son **categóricas por reglas**, no verbatims: dan distribución y dirección,
  no el matiz cualitativo de una entrevista real.

---

*Generado con el skill `lapuerta` (semilla 42, reproducible). CSV con los 200 perfiles y sus
respuestas individuales: `research/personas/datasets/guia_triaje_200_usuarios_2026-08-05.csv`.*
