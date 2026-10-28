# Informe · Pregunta 1 del benchmarking: ¿para qué sirve la recurrencia digital en un seguro?

**Insumo para:** Gerencia de Digital, RIMAC · **Fecha:** 28-10-2026 · **Estado:** versión de trabajo
(el formato para la gerencia se define después)
**Basado en:** `research/_nodes/valor-recurrencia-digital-seguros.md` (v1.0, 2026-10-28). Las fuentes se
citan como (Autor, año) y con su número del registro de fuentes del proyecto (F-n).
**Alcance:**
- Seguros de Perú y LatAm primero.
- Banca, salud y retail como análogos.
- EE.UU., Europa y Asia solo como contraste (🌐), sin generalizar a Perú.
- Periodo 2021-2026. Los estudios canónicos anteriores van marcados con 📚.
- RIMAC está excluida como caso, fuente o benchmark.

---

## 1. Conclusión

**La actividad digital produce valor en un seguro cuando resuelve algo, no cuando genera visitas.** Las tres
pistas de investigación coinciden: la académica, la de resultados de negocio y la social. Ninguna fuente
encontrada muestra que la frecuencia de uso, por sí sola, genere valor.

**Consecuencia para la meta:** el MAU mide cuántos entran, no cuántos resuelven. Hay cinco formas en que lo
digital puede producir valor. Cada una pide un indicador distinto. **En dos de ellas, un buen resultado
baja la actividad**: un cliente que resolvió rápido no vuelve a entrar.

**Lo que la gerencia tiene que decidir:** cuál de las cinco formas de valor persigue el canal digital, y
por lo tanto qué indicador acompaña o reemplaza al MAU. Este informe no toma esa decisión. Entrega las
opciones y qué tan probada está cada una.

---

## 2. Menú de teorías de valor

| # | Teoría de valor | Indicador en vez del MAU | Mejor evidencia | Qué tan probada |
|---|---|---|---|---|
| 1 | **Costo de servir:** resolver en digital lo que hoy va al teléfono | Contactos por necesidad resuelta, separados por tipo de tarea | 📚 En una aseguradora de salud, el portal bajó 29% las llamadas sobre información clara y fácil de encontrar, pero subió 14% el total de llamadas, porque generó llamadas sobre información ambigua (Kumar y Telang, 2012, F-850) | 🟢 Causal, efecto en ambas direcciones |
| 2 | **Retención:** el cliente digital se queda más | Renovación o persistencia en cohortes emparejadas | 📚 En banca, adoptar lo digital se asocia a más retención aun controlando que adopta quien ya era fiel (Campbell y Frei, 2010, F-847). En un plan de salud, 96,9% contra 90,5% (Turley et al., 2012, F-851; observacional). **En seguros no hay ningún estudio causal** | 🔵 Plausible por analogía · ⚪ No demostrado en seguros |
| 3 | **Venta cruzada:** el cliente digital compra más productos | Productos por cliente; lead a póliza; prima nueva de clientes existentes | Los usuarios digitales tienen más productos en banca (Xue et al., 2011, F-848; Becker et al., 2022, F-849). La venta digital de Porto Seguro es casi toda a clientes que ya tiene: 84%, según su meta 2025 (F-865) | 🟡 Asociación |
| 4 | **Prevención:** lo digital cambia la conducta de riesgo | Siniestralidad por cohorte, separando selección de efecto | En auto, un experimento de campo con telemetría redujo velocidad y frenadas bruscas (F-442). En salud, dos ensayos aleatorizados de programas de bienestar no bajaron el gasto médico (Jones, Molitor y Reif, 2019, F-854; Song y Baicker, 2019, F-855) | 🟢 En auto (conducta) · 🔴 Negativa en salud (gasto) |
| 5 | **Confianza en el momento de verdad:** resolver bien el siniestro | Tiempo a resolución; tasa de escalamiento de digital a humano; resuelto al primer intento | 🌐 Con mala experiencia digital del siniestro, 52% está en riesgo de irse; con experiencia excelente, 4% (J.D. Power, 2025, F-872). La confianza es el factor más importante del siniestro y el canal digital el menos importante, entre ocho (J.D. Power, 2025, F-874) | 🟡 Asociación, consistente entre fuentes |

**Lectura:** solo la teoría 1 tiene evidencia causal en seguros, y su efecto va en las dos direcciones. La
teoría 2, que es la tesis central del canal ("el cliente digital es más fiel"), es la menos probada en
seguros.

---

## 3. Hallazgos por teoría de valor

### 3.1 Costo de servir: lo claro migra, lo ambiguo vuelve al teléfono

- **El estudio causal más directo es de una aseguradora de salud.** Usar el portal subió las llamadas 14% en
  total. Bajaron 29% las de información clara. Subieron las de información ambigua, como pólizas y reclamos
  (Kumar y Telang, 2012, F-850).
- **En banca pasa lo mismo.** Quienes adoptan la banca online hacen más transacciones en total y usan *más* el
  call center y la sucursal. En el corto plazo, el cliente se vuelve menos rentable (Campbell y Frei, 2010,
  F-847).
- **Un banco alemán muestra lo contrario.** Con un grupo de control emparejado, quienes adoptan la banca móvil
  usan *menos* el call center (Becker et al., 2022, F-849).
- **Perú:** Pacífico reporta que más de 60% de las consultas y solicitudes se resuelven por autoservicio (chatbot
  y app), según Forbes Perú (2022, F-866). Es una cifra de la empresa, sin método.
- **Proveedores de software:** prometen bajar entre 30% y 40% el costo de servir. No tienen método (F-877). No
  usar como dato.

**Implicancia:** antes de mover un flujo al canal digital, hay que preguntarse si su información es clara o
ambigua. En lo ambiguo, primero se rediseña el contenido; si no, el ahorro esperado se vuelve más llamadas.
Este patrón coincide con lo que muestra el diagnóstico interno de julio: lo digital gana en consultar y pierde
en gestionar y en lo urgente.

### 3.2 Retención: plausible en otras industrias, sin probar en seguros

- **Banca y salud:** la retención se mantiene más alta en usuarios digitales aun con controles de autoselección
  (F-847) o emparejamiento (F-851).
- **Seguros:** solo hay encuestas de intención (Singh et al., 2024, F-856, India) y cifras de las propias
  empresas sin método de comparación:
  - Vitality reporta entre 39% y 67% menos caídas de póliza en miembros comprometidos (F-860).
  - AIA habla de "mejoras significativas", sin cifra (F-861).
  - Oscar atribuye la retención a su plataforma, sin publicar la tasa (F-858).
- **🌐 Ser nativo digital no garantiza retención alta.** Lemonade retiene 85% de sus primas año a año, según su
  reporte anual auditado (F-857).
- **La amenaza principal es la selección.** En un ensayo aleatorizado, quienes se inscriben en programas de
  bienestar ya tenían menor gasto y mejores hábitos antes de empezar (Jones et al., 2019, F-854). La misma
  lógica aplica al cliente digital: quien adopta ya era distinto.
- 📚 **Tener más productos no blinda.** En una aseguradora europea, la primera cancelación predijo la fuga total
  del hogar. Los clientes con 3 o más pólizas fueron *más* propensos a irse del todo tras cancelar una
  (Brockett et al., 2008, F-852).

**Implicancia:** el benchmarking no puede probar la tesis "el cliente digital es más fiel". Solo se resuelve
con data propia: cohortes emparejadas o un despliegue escalonado.

### 3.3 Venta cruzada: la puerta de entrada a escala la tienen otros

- **Asociación, no efecto.** Los usuarios digitales tienen más productos en banca (F-848, F-849). 🌐 En Ping An,
  quienes usan su ecosistema de salud tienen 1,6 veces más contratos, según prensa (F-862).
- **Lo digital vende sobre todo al que ya es cliente.** Porto Seguro proyecta que 84% de su venta digital sea a
  clientes existentes. Sus 45 mil corredores siguen siendo el motor de la venta cruzada (F-865).
- **En LatAm, las apps de uso diario de otros venden seguros a escala:**
  - Nubank tiene 2 millones de pólizas, pero con baja penetración: 1,6% de su base en 2023 (F-863).
  - Mercado Pago tiene 11 millones de clientes con póliza (F-864).
  - Yape vende SOAT y lanzó un seguro de salud (F-869).
- **No se encontró evidencia de que un producto propio de bajo ticket, como el SOAT, funcione como puerta de
  entrada.** La venta digital de SOAT de Interseguro creció 66% en 2019. Su memoria también dice que mejoró la
  renovación, pero sin cifra (F-867).

**Implicancia:** si la apuesta es usar el SOAT como llave de entrada, hoy no hay evidencia que la respalde. Lo
que sí muestra la región es que la relación diaria con el cliente la puede tener una billetera o un banco.

### 3.4 Prevención: en auto cambia la conducta; en salud, el programa selecciona

- **Auto:** la retroalimentación telemática cambió la forma de manejar en un experimento de campo nacional
  (F-442). Midió conducta, no siniestros.
- **Brasil:** Justos reporta que su siniestralidad baja unos 6 puntos por año, y no renueva al 2% de clientes
  con peor nota de manejo. Atribuye la mejora a varios factores juntos: precio, suscripción y telemetría (F-870).
- **🌐 Root:** mejoró su ratio combinado a 98,2% por precio y selección de riesgo. La retención sigue siendo una
  incertidumbre declarada por la propia empresa (F-871).
- **Salud:** dos ensayos aleatorizados de programas de bienestar no encontraron efecto en gasto médico, salud
  clínica ni ausentismo (F-854, F-855).
  - Vitality reporta 4% menos siniestros, con una revisión actuarial que declara (F-353).
  - Alan duplicó sus usuarios activos diarios con gamificación y aún no mide el efecto en retención (F-859).

**Implicancia:** en salud, el valor más probable del engagement es atraer y retener buenos riesgos. Es un valor
legítimo, pero es **selección**, no prevención, y se mide distinto.

### 3.5 Confianza en el momento de verdad: el siniestro define la relación

- 🌐 **La experiencia digital del siniestro se asocia fuertemente a la fuga:** 52% en riesgo cuando es mala,
  contra 4% cuando es excelente (F-872).
- 🌐 **La confianza pesa más que el canal.** Bajar el tiempo de reparación de 22,3 a 19,3 días se asoció a +9
  puntos de satisfacción (F-874).
- 🌐 **Lo 100% digital falla en los reclamos complejos.** Más de 30% termina necesitando a una persona, y quien
  escala pierde 11 puntos de NPS (Bain, 2023, F-183).
- 🌐 **Satisfacción no es retención.** Tras un siniestro, la probabilidad de cambiarse de aseguradora sube 35%,
  aun entre clientes satisfechos (LexisNexis, 2023, F-890; dato de un proveedor).
- **Perú:** la fricción registrada está en la **resolución**, no en el canal. Indecopi recibió 8.248 reclamos de
  seguros entre 2019 y 2022. En 2025 sancionó demoras en indemnizaciones de SOAT y liquidaciones que no
  respetaban la póliza (F-883).

**Implicancia:** el siniestro se diseña como híbrido. Lo digital sirve para iniciarlo y seguir su estado; una
persona resuelve lo complejo. El indicador es el tiempo a resolución, no el uso del app.

---

## 4. Lectura conductual

La pregunta conductual no es "cómo hacemos que entren más". Es **qué conducta tiene que ocurrir para que haya
valor, y qué la frena**. Esta lectura agrega cuatro distinciones que el análisis de negocio no ve:

1. **Lealtad o inercia.** En seguros, cambiarse cuesta mucho, y por eso la gente se queda donde está (Handel,
   2013, F-889). El regulador británico prohibió cobrarle más a quien renueva por inercia. También documentó
   fricción puesta a propósito para retener, como exigir una llamada para cancelar (FCA, 2025, F-886). Si la
   meta de fidelidad no separa la elección activa de la renovación pasiva, premia la fricción para irse.
2. **Usar el app no es formar un hábito.** El hábito necesita frecuencia y un contexto estable (Wood y Neal,
   2007, F-888). Con una o dos interacciones al año (McKinsey, 2023, vía cita secundaria, F-876), un hábito en
   el app propia es improbable; esto es inferencia. La recurrencia se toma prestada de hábitos que ya existen
   (billetera, WhatsApp, banca) o de servicios cercanos de alta frecuencia.
3. **El siniestro es el pico de la relación.** La regla pico-final es uno de los efectos más robustos de la
   psicología: recordamos una experiencia por su peor o mejor momento y por cómo terminó. Por eso el cierre del
   siniestro (el pago, la explicación, el siguiente paso) pesa más que la cantidad de interacciones.
4. **Empujar decisiones cambia el riesgo de la cartera.**
   - Reducir la inercia empeoró la selección adversa en seguros de salud (Handel, 2013, F-889).
   - Quienes llegan cambiándose desde otra aseguradora siniestran el doble, con el mismo historial de manejo
     (estudio en Marketing Science, F-891).

   Todo empujón de adquisición o de cambio tiene un costo actuarial.

**Propuesta para las tres definiciones que hoy no existen:**

- **Fidelidad:** elegir quedarse teniendo alternativas, a diferencia de renovar por inercia.
- **Cliente digitalmente sano:** resuelve lo que necesita cuando lo necesita, sin fricción de más. No se mide
  por cuántas veces entra.
- **Cliente de alto valor:** suma el riesgo que trae, no solo la prima que paga.

**Herramienta para el ejercicio con los ramos:** una auditoría de fricciones por recorrido (Sunstein, 2022,
F-894). Usa la conversión de cada flujo y separa la fricción excesiva de la que protege al cliente.

---

## 5. Implicancias para las hipótesis del diagnóstico

| Hipótesis | Qué dice el benchmarking | Cómo se cierra |
|---|---|---|
| El cliente digital es más fiel | No confirmada para seguros. Las analogías dicen que puede ser cierta; la selección dice que puede ser falsa | Cohortes emparejadas o despliegue escalonado con data propia |
| Hace falta una llave de entrada para cada cartera | Sin evidencia de que un producto propio de bajo ticket abra la puerta. Las puertas que funcionan a escala son apps ajenas de alta frecuencia | Decidir si se compite por esa puerta o se aliña con quien la tiene (pregunta 3) |
| La actividad la determina el producto, no el canal | Consistente con la baja frecuencia estructural del seguro y con que la recurrencia de los referentes venga de servicios cercanos | Validar por ramo en el ejercicio con los ramos |
| La gente casi no interactúa con la propuesta de valor | Consistente con lo anterior | Igual que la anterior |
| El siniestro debería resolverse en digital | La evidencia apunta a un modelo híbrido: digital para iniciar y seguir, persona para lo complejo | Rol del canal por momento (pregunta 2) |

---

## 6. Lo que no se pudo responder

- **No hay evidencia causal de Perú ni de LatAm en ninguna de las cinco teorías.** Todo lo regional lo reportan
  las propias empresas.
- **No hay ningún estudio causal sobre retención digital en seguros.** El ensayo más cercano, sobre
  recordatorios y renovación automática en un seguro de salud de Ghana, está en curso y sin resultados (F-887).
- **Varios estudios académicos son anteriores a 2021.** Son canónicos y sus contextos son EE.UU. y Europa.
- **Todo se leyó por resumen.** Tres dominios estuvieron bloqueados desde el entorno de trabajo: `arxiv.org`,
  `pacifico.com.pe` y `quartr.com`. La Memoria Integrada 2025 de Pacífico queda pendiente.
- **La pista social es la más débil.** No se encontró conversación pública sobre apps de aseguradoras peruanas.
- **Varias cifras de Porto Seguro son metas, no resultados.** Las de Ping An que comparan usuarios con no
  usuarios vienen de prensa.

**Pendientes para la siguiente versión:**

- los PDFs y fuentes de la otra conversación;
- las memorias anuales completas de Perú y LatAm;
- la búsqueda de estudios causales de retención en seguros.

---

## Anexo A · Referentes revisados

| Referente | Bloque | Aportó a | Rigor de lo encontrado |
|---|---|---|---|
| Pacífico Seguros | Perú | Costo de servir | 🟠 D (F-866) |
| Interseguro | Perú | Venta digital de SOAT; renovación (débil) | 🟡 C (F-867) |
| La Positiva | Perú | **No aportó evidencia**: solo declara una plataforma en construcción | 🟠 D (F-868) |
| Mapfre Perú | Perú | **No aportó evidencia** | — |
| Yape (billetera, análogo) | Perú | Puerta de entrada ajena | 🟠 D (F-869) |
| Porto Seguro | LatAm | Venta cruzada, costo de servir, siniestro | 🟡 C (F-865) |
| Nubank + Chubb | LatAm | Puerta ajena: escala con baja conversión | 🟠 D (F-863) |
| Mercado Pago | LatAm | Puerta ajena; IA que vende seguros | 🟠 D (F-864) |
| Justos | LatAm | Prevención y selección | 🟠 D (F-870) |
| BBVA México | LatAm (bancaseguros) | Contexto, sin desglose de seguros | 🔵 B (F-879) |
| Lemonade | 🌐 Contraste | Retención, venta cruzada | 🔵 B (F-857) |
| Oscar Health | 🌐 Contraste | Retención (sin dato publicado) | 🟡 C (F-858) |
| Alan | 🌐 Contraste | Recurrencia, prevención | 🟠 D (F-859) |
| AIA / Vitality | 🌐 Contraste | Retención (con selección) | 🟠 D (F-860, F-861) |
| Ping An | 🌐 Contraste | Venta cruzada (asociación) | 🔵 B / 🟠 D (F-862) |
| Root | 🌐 Contraste | Prevención y selección | 🔵 B (F-871) |
| Amica | 🌐 Contraste | Lealtad sin ser digital primero | 🟡 C (F-880) |
| Zurich, AXA, Allianz y Allianz Direct, ZhongAn, Progressive, USAA, Coalition | 🌐 Extendidos | **No aportaron evidencia** a estas teorías en esta pasada; no se forzaron | — |
| Concesionarios con seguro vinculado | LatAm | **No aportaron evidencia**: solo un caso de proveedor sin método | 🔴 E (F-877) |

## Anexo B · Banco de señales (para el ejercicio de foresight con los ramos)

No es evidencia para decidir hoy. Es materia prima para pensar escenarios después de que la gerencia elija su
teoría de valor.

**Prácticas probadas** (evidencia A o B):

- lo claro migra a digital y lo ambiguo genera llamadas (F-850);
- en banca, lo digital se asocia a retención aun controlando la selección (F-847);
- la retroalimentación telemática cambia la forma de manejar (F-442);
- los programas de bienestar seleccionan más de lo que transforman (F-854, F-855);
- la retención por inercia es explotable y el regulador la puede prohibir (F-886).

**Señales emergentes** (sin resultados todavía):

- **Agentes de IA que venden y atienden dentro de apps ajenas:** Mercado Pago (F-864); Oscar opera con lo que
  llama "IA agéntica" (F-858).
- **El seguro como función de una billetera o banco de uso diario:** Yape (F-869), Nubank (F-863).
- **Una disputa de IA contra IA en el siniestro:** clientes que usan IA para apelar rechazos (F-885).
- **Telemetría para no renovar:** selección explícita, con riesgo reputacional (F-870).
- **Indemnización instantánea en siniestros simples** (Porto Seguro, F-865).
- **Gamificación de salud como motor de uso diario** (Alan, F-859).
- **Recuperación de la inversión insurtech en LatAm en 2025, con más disciplina** (F-878).

**Eje candidato para escenarios:** quién será dueño de la relación diaria con el cliente. Puede ser la
aseguradora, un banco o una billetera, el empleador o corredor, o una interfaz de IA. Es una hipótesis para el
ejercicio, no un hallazgo.

## Anexo C · Escala de evidencia usada

🟢 A: académico revisado por pares, con método y muestra explícitos · 🔵 B: regulador, organismo oficial o
reporte auditado · 🟡 C: consultora o industria con método propio no auditable · 🟠 D: prensa o cifra de la
propia empresa sin método · 🔴 E: opinión o marketing sin método. Detalle de cada fuente en
`research/fuentes/codice.md` (F-847 a F-894, más F-183, F-353 y F-442).
