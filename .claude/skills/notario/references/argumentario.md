# Argumentario: por qué el diseño conductual crece cuando una empresa acelera lo digital

> Banco de argumentos reutilizable de `/notario`. Solo conocimiento del cerebro (nodes y ledger);
> **nada personal**. Cada argumento trae su fuente (`F-n` en `research/fuentes/codice.md`) y su
> solidez. Última revisión: 2026-11-08.
>
> Regla de uso: nunca se presenta un argumento sin su contraargumento más fuerte (sección B).
> Quien escucha ya lo tiene en la cabeza; mejor nombrarlo primero.

## A. Argumentos a favor

**A1. Lo digital es donde los efectos chicos se vuelven rentables.**
Los experimentos conductuales a escala en gobiernos (más de 120 ensayos, más de 20 millones de
personas) mueven la conducta unos 1,4 puntos porcentuales: poco por persona, casi gratis por persona
(DellaVigna y Linos, 2022, F-21, 🟢). Ese cálculo solo cierra con poblaciones grandes y costo marginal
bajo. Eso es exactamente un canal digital. *Frase:* "lo digital le da el denominador; la disciplina le
da el numerador".

**A2. Lo digital abarata el experimento, y experimentar es el oficio.**
El estándar actual del campo es probar decenas de variantes a la vez en la propia población. Un
megaestudio probó 54 programas digitales con 61.293 personas reales; el mejor no fue un recordatorio
genérico sino un microincentivo en el momento de recaída, a ~US$0,75 por persona al mes
(Milkman et al., 2021, F-20, 🟢). Sin alguien que diseñe hipótesis conductuales, una plataforma
digital solo prueba colores de botón.

**A3. Las decisiones de mayor efecto se toman al construir el producto digital.**
En salud y finanzas, las intervenciones de mayor efecto son los valores por defecto y la reducción
de esfuerzo (Mertens et al., 2022, F-16, 🟢; el promedio general está en disputa, ver B1). La teoría
más citada de la década dice lo mismo: el valor está en cambiar la estructura del producto, no en
retocar el mensaje (Chater y Loewenstein, 2022, F-19, 🟢). Los defaults, los pasos y las fricciones
de un flujo digital se deciden en los proyectos digitales. Si la disciplina no está ahí, esas
decisiones se toman igual, pero sin criterio conductual.

**A4. Informar no basta; diseñar sí.**
Un ensayo de campo con ~124.000 clientes en Reino Unido mostró que una divulgación clara mejora la
comprensión pero casi no cambia la conducta (Adams et al., 2021, F-9, 🟢). Digitalizar un formulario
o una póliza sin rediseñar la decisión reproduce el mismo resultado: más información, misma conducta.

**A5. En seguros ya hay evidencia de que el diseño embebido en el producto funciona.**
Un ensayo nacional preregistrado (1.449 conductores) con retroalimentación y microincentivos tipo
seguro por uso redujo el exceso de velocidad 11-13% y las frenadas bruscas 16-21%, y la mejora se
sostuvo tras la intervención (F-442, 🟢; mide conducta de manejo, no siniestros ni precio). Ensayos de
industria muestran que video y simplificación mejoran la compra de seguros de vida (RGA/SOA, F-22, 🟡).

**A6. La IA conversacional mueve a las personas, y alguien tiene que medir hacia dónde.**
Un estudio en *Science* con 11 modelos y 2.405 personas mostró que la IA complaciente aumenta la
dependencia y la gente la prefiere igual (Cheng et al., 2026, F-488, 🟢). Lo que las personas dicen de
la IA diverge de lo que pasa con su juicio y su desempeño en cinco literaturas distintas (node
`conducta-humano-ia`, regla "medir conducta, no autoinformes"). Cada asistente, copiloto o bot de un
plan digital necesita evaluación conductual, no solo satisfacción. Ver también el node
`evaluacion-calidad-agentes-conversacionales-ia`.

**A7. Las empresas que se toman en serio lo conductual lo internalizan.**
McKinsey documenta unidades conductuales corporativas con efectos como +10% de retención y menos
fraude, y define el estándar: traducir conducta a valor con pruebas A/B permanentes (F-26, 🟡
consultora). Las grandes consultoras compraron o se aliaron con firmas conductuales en 2024-2025
(node `behavioral-design-estado-disciplina`, 🟠 informes de mercado).

**A8. La integridad es un diferencial comercial.**
Tras los escándalos de fraude del campo (F-24, 🔵), un equipo que dice "nuestros efectos vienen de
nuestros propios experimentos, con datos verificables" se distingue de quien vende hallazgos de
segunda mano.

## B. Contraargumentos fuertes y cómo responderlos

**B1. "El nudge no funciona: el efecto promedio es cero."**
Es cierto para el promedio publicado: corregido el sesgo de publicación, el efecto agregado cae de
d=0,27 a prácticamente cero (Maier et al., 2022, F-17, 🟢; Hu et al., 2025, F-18, 🟢).
*Respuesta:* por eso la disciplina ya no vende catálogo; vende experimentos propios con control y
KPI declarados antes. El promedio es cero porque mezcla lo que funciona con lo que no; el trabajo
es encontrar qué funciona aquí (A2).

**B2. "Las consultoras conductuales se están achicando."**
Mind Gym, consultora de cambio conductual cotizada en Londres, cayó 14% y luego 23% en ingresos con
pérdidas (F-629, 🔵). *Respuesta:* se contrae la consultoría genérica de cursos y talleres; crece la
capacidad interna ligada a producto (A7). Es un argumento para tener el equipo dentro, junto a
producto, no para no tenerlo.

**B3. "UX y research ya cubren esto."**
*Respuesta:* UX optimiza que algo se pueda usar; la disciplina conductual diseña qué decide la persona
y mide si cambió su conducta (A3, A4). Se complementan. Conviene mostrarlo con un caso donde el
flujo era usable y aun así la conducta no cambió.

**B4. "Sus impactos son estimaciones."**
Suele ser verdad y hay que reconocerlo. *Respuesta:* separar lo medido de lo estimado, poner primero
lo medido y comprometer una medición con grupo de control en cada proyecto digital del próximo año.

**B5. "Los usuarios sintéticos no reemplazan a personas reales."**
Una consultora encontró respuestas sintéticas "significativamente distintas" de las humanas
(F-627, 🟡). *Respuesta:* se usan para filtrar hipótesis antes del experimento real, no para
reemplazarlo (node `convergencia-psicologia-economia-ia` §6).

## C. Cómo armar el argumento en una conversación

1. Empezar por el objetivo del otro (los proyectos digitales del próximo año), no por la disciplina.
2. Un dato medido propio > tres estudios externos > diez estimaciones.
3. Nombrar B1 antes de que lo nombren.
4. Cerrar con una propuesta concreta y barata: un proyecto digital con experimento y KPI declarado,
   en un plazo corto.
