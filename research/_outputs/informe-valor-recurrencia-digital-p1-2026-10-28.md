# Informe · Pregunta 1 del benchmarking: ¿para qué sirve la recurrencia digital en un seguro?

**Insumo para:** Gerencia de Digital, RIMAC · **Fecha:** 28-10-2026 · **Estado:** versión de trabajo 5 (incorpora
quince documentos aportados por la usuaria y cuatro papers verificados; dos documentos internos del equipo se omiten de esta copia)
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
- **LatAm:** una aseguradora sin nombre desvía 30% de sus siniestros a una vía rápida por reglas, y otras pasaron la
  mayoría de sus siniestros de salud a digital con más satisfacción y menos costo, según McKinsey (2023, F-900), sin
  cifras verificables.
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
- **El estudio de India sobre seguros de vida, leído completo, es el ejemplo típico de esta evidencia débil**
  (Singh, Panigrahi y Shekhar, 2024, F-856). Mide la retención como actitud ("siento lealtad", "estoy dispuesto
  a seguir") y no como renovación real. Su muestra es de usuarios digitales diarios, 67% de ingreso alto y 97%
  urbana.
- **🌐 "No lo usé" es una razón para irse.** En una encuesta representativa del Reino Unido, 40% canceló o
  considera cancelar su seguro privado de salud. La razón más citada después del precio fue "no lo usé tanto como
  esperaba" (27%), y es la primera entre 18 y 34 años (Graphite Digital, 2025, F-895). Es intención declarada, y la
  autora vende experiencia digital. Confirma el problema de valor percibido en productos de baja frecuencia.
- **🌐 Al irse, pesa más el precio que lo digital.** 27% de asegurados cambió de aseguradora en dos años, sobre todo
  por precio (60%) y cobertura (53%) (Capgemini, 2024, F-901; encuesta de una consultora).
- **Parte de la fuga es estructural.** En México, 47% de quienes dejaron de tener seguro lo atribuye a un cambio
  de trabajo (Treo, c. 2021, F-898, con datos de la ENIF 2018). Ese tipo de fuga no la resuelve ningún canal.
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
- **La puerta de entrada funciona en un caso de LatAm, pero por defecto y anclada a una relación frecuente.** En
  México, un microcrédito incluía cobertura de vida automática, y cerca de la mitad de los clientes compró módulos
  voluntarios (Poulton y Magnoni, 2013, F-896). En un ensayo aleatorizado con esos clientes, al quitar la
  cobertura automática la gente compró más por su cuenta, pero terminó menos protegida (Zimmerman et al., 2013,
  F-897). La relación era semanal (el pago del crédito) y no fue digital.
- **La puerta ajena cobra peaje.** En Perú, los microseguros llegan 97,8% por bancos y microfinancieras, con comisiones
  cercanas a 50% (Inga Falcón para el PNUD, 2025, F-902). En Chile, obligar a los bancos a licitar el seguro atado
  al crédito hipotecario bajó el desgravamen 62% (Coloma, 2019, F-904). La puerta por defecto funciona, pero sin
  competencia encarece el seguro.
- **Tener la puerta no basta.** En LatAm, la billetera móvil pasó de 11% a 49% de la población en cinco años y se usa
  a diario, pero la tenencia de seguros privados no creció; Perú tiene la más baja de la región (13%) pese a su alto
  uso de billetera (Banco de Ideas Credicorp e Ipsos, 2026, F-906). El seguro no se suma solo a los hábitos diarios.
- **El momento de compra funciona como puerta.** 42% compraría su seguro de auto en el concesionario, frente a 32% en
  2018 (Accenture, 2023, F-905; intención declarada).
- **En Perú, la venta 100% digital tiene techo.** Solo 20% compraría un seguro de forma digital; el canal presencial
  domina (encuesta SBS-CAF 2022, vía F-903). En LatAm, 67% empieza a buscar seguro de vida en línea, pero compra con
  una persona (McKinsey, 2023, F-900).
- **No se encontró evidencia de que un producto propio de bajo ticket y frecuencia anual, como el SOAT, funcione
  como puerta de entrada.** La venta digital de SOAT de Interseguro creció 66% en 2019. Su memoria también dice que mejoró la
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
- **LatAm: el valor está en la rapidez y la justicia del pago.** En un microseguro de vida en México, el pago
  llegó en promedio 9 días después de la muerte. Las familias lo usaron como garantía para pedir prestado sin
  interés a su red, y evitaron deuda cara o vender activos. Después del siniestro, todos los asegurados dijeron que
  fue buena decisión (Poulton y Magnoni, 2013, F-896). La muestra es pequeña (32 familias aseguradas y 36 no
  aseguradas) y no aleatoria.
- **Perú: la norma deja abierto el tiempo del siniestro.** La aseguradora tiene 30 días desde la documentación completa
  para responder, pero puede pedir información adicional en los primeros 20 días sin un límite expreso de veces
  (Pérez-Llorca, 2026, F-907).
- **El lenguaje en el momento del siniestro mueve conducta y costo.** Una aseguradora alemana rediseñó el lenguaje de
  sus agentes con ciencias del comportamiento: la aceptación de su red de talleres superó 30% y, al escalarlo, la
  siniestralidad bajó 2% (caso citado por Beway, F-909; cifras no verificadas en el original).
- **Perú: el problema está en pagar, no en el canal.** Los microseguros devuelven en siniestros solo 16,7% de la
  prima (en LatAm ronda 40%); 18 productos no pagaron ningún siniestro en 2024; reclamar exige documentos que no
  existen en zonas remotas (F-902). De quienes desconfían de las aseguradoras, 47% dice que no cumplen lo ofrecido
  (F-903). En un ranking de experiencia de cliente de 2022, los seguros quedaron últimos de 20 industrias (F-900).
- **🌐 21% de quienes consideran dejar su seguro de salud cita la dificultad para reclamar** (Graphite Digital,
  2025, F-895; intención declarada).
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
5. **La cobertura por defecto pesa más que el mensaje.** En el ensayo de microseguro en México, quitar la
   cobertura automática redujo la protección total, y los mensajes emocionales o factuales no cambiaron la compra
   (Zimmerman et al., 2013, F-897). Lo que viene incluido define cuánto queda protegido. Pero el defecto también se
   presta para cobrar de más, y ahí interviene el regulador: en Chile, licitar el seguro atado al crédito bajó el
   precio del desgravamen 62% (F-904).

**Hipótesis conductuales para el trabajo de campo.** El estudio mexicano de inclusión financiera y las voces de
practitioners no son evidencia, pero abren mecanismos que coinciden con otras fuentes. Valen como hipótesis:

1. **La red familiar y el "guardadito" compiten con el seguro.** Ante un golpe, la gente recurre primero a familia,
   ahorros y recorte de gastos. Es la hipótesis más respaldada: coinciden cinco fuentes (F-896, F-898, F-903, F-906,
   F-908). Implica diseñar el seguro como complemento de la red, no como su reemplazo.
2. **El cobro debe seguir el ritmo del ingreso.** Quien cobra por semana tiene menos seguros (F-898); el microseguro
   mexicano se pagaba cada semana junto al crédito (F-896).
3. **El dependiente o el adulto mayor poco digital se alcanza a través de un familiar** (F-898). Se conecta con la
   baja digitalización de dependientes del diagnóstico interno.
4. **La fricción pequeña acumulada empuja a irse sin una decisión consciente**, y la confianza se gana cuando algo
   falla (F-899). Coincide con la fuga tras siniestro (F-890, F-872).
5. **Delegar en una IA exige confirmar en cada paso sensible** para sentir control (F-899). **Esta hipótesis ya tiene
   respaldo experimental:** revelar que era un bot antes de conversar bajó la compra más de 79,7% (Luo et al., 2019,
   F-912); la gente resiste la IA porque cree que no considera lo que la hace única (Longoni et al., 2019, F-914); la
   aversión baja si puede modificar el resultado (Dietvorst et al., 2018, F-915); y la comodidad cae de cotizar (46%)
   a presentar un siniestro por mí (22%) (F-916). Ojo: ocultar al bot sube la venta, pero choca con la transparencia
   que exige la regulación de IA (F-907).
6. **El momento de vida pesa más que la edad**, y conviene ofrecer cuando el riesgo se siente cerca (F-899, F-909),
   como al comprar un auto (F-905).
7. **La confianza se construye usando el producto** (F-898); completar la primera tarea genera confianza (F-895).

Sobre los defaults: un meta-análisis de 58 estudios halló un efecto considerable (d=0,68) de las opciones por
defecto (Jachimowicz et al., 2019, F-913), mientras que el efecto promedio de los nudges en general desaparece al
corregir el sesgo de publicación (Maier et al., 2022, F-17).

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
| Hace falta una llave de entrada para cada cartera | Sin evidencia de que un producto propio de bajo ticket y uso anual abra la puerta. Funciona cuando la cobertura viene por defecto y anclada a una relación frecuente (microcrédito semanal en México, F-896 y F-897) o a una app ajena de uso diario | Decidir si se compite por esa puerta o se aliña con quien la tiene (pregunta 3) |
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

- el resto de los documentos de la otra conversación (ya se incorporaron quince documentos y cuatro papers: ver §7);
- el resto del blog de Beway: el dominio `blog.beway.com` está bloqueado desde el entorno de trabajo (se leyó un artículo aportado por la usuaria);
- las memorias anuales completas de Perú y LatAm;
- la búsqueda de estudios causales de retención en seguros.

---

## 7. Qué cambió con los documentos aportados

| Documento | ¿Robustece lo que ya teníamos? |
|---|---|
| Estudio de India sobre seguros de vida (F-856) | **No.** Leído completo, confirma que es evidencia débil: mide actitud, no renovación, con una muestra sesgada a usuarios digitales de ingreso alto |
| Whitepaper sobre apps de seguros de salud (F-895). ⚠️ El archivo venía rotulado como J.D. Power, pero es de Graphite Digital, una agencia | **Parcial.** Suma el "no lo usé" como razón de fuga y confirma el siniestro y la sobrecarga de información como puntos críticos. Intención declarada, con conflicto de interés |
| Microseguro de vida en México (F-896) y su ensayo aleatorizado (F-897) | **Sí.** Da evidencia de LatAm para la confianza en el momento de verdad y para la cobertura por defecto. Matiza la puerta de entrada: funciona por defecto y anclada a una relación frecuente |
| Estudio de inclusión financiera en México (F-898) | **No para esta pregunta.** Sí aporta que parte de la fuga es estructural (cambio de trabajo) y que los adultos mayores se alcanzan mejor por intermediarios |
| Luo 2019, Jachimowicz 2019, Longoni 2019, Dietvorst 2018 (F-912 a F-915) | **Sí.** Respaldo experimental para la hipótesis de control al delegar en IA y para la fuerza de los defaults |
| Índice de Inclusión Financiera de Credicorp 2026 (F-906) | **Sí, y matiza la puerta ajena.** La billetera se volvió diaria, pero los seguros no crecieron; Perú tiene la tenencia más baja (13%) |
| Estudio global de consumidores de Accenture 2023 (F-905) | **Parcial.** El concesionario como puerta (42%) y la rapidez del siniestro como valor. Intención declarada |
| Artículo de la Universidad de Lima (F-908) | **Parcial.** Suma una fuente peruana a la hipótesis de la red familiar. Sin diseño causal |
| Boletín legal de Pérez-Llorca 3T 2026 (F-907) | **Para señales y la pregunta 2:** reglamento peruano de IA y plazos del siniestro con una puerta abierta |
| Artículo de Beway sobre seguro marítimo (F-909) | **Parcial.** El lenguaje conductual en el siniestro mueve conducta y costo (caso de segunda mano) |
| Diagnóstico de microseguros en el Perú para el PNUD (F-902) y encuesta SBS-CAF 2022 (F-903) | **Sí, el más fuerte para Perú.** Solo 20% compraría digital; la puerta ajena cobra comisiones cercanas a 50%; los siniestros devuelven poco valor. Refuerza que el problema está en pagar, no en el canal |
| Reporte de McKinsey sobre seguros en LatAm (F-900) | **Parcial.** Búsqueda en línea y compra con persona; seguros últimos en experiencia en Perú. Casos sin cifras verificables |
| Licitación de seguros hipotecarios en Chile (F-904) | **Sí, para la puerta por defecto** (y para la pregunta 3): sin competencia, el seguro atado cobra de más |
| Informe mundial de seguros generales de Capgemini (F-901) | **Débil.** Al irse, pesa más el precio que lo digital |
| Voces de practitioners de Flat 101 (F-899) | **No valida; muestra que la idea ya circula** en el sector. Coincide con la evidencia sobre el siniestro y el escalamiento a una persona |

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
- **Bancos que compiten por "custodiar el permiso para actuar"** de agentes de IA que ejecutan con confirmaciones
  (practitioners de Flat 101, F-899; opinión).
- **Finanzas abiertas en la agenda regulatoria peruana y "seguro abierto" en Brasil** (F-900, F-902).
- **Seguros paramétricos en desarrollo en Perú**, aún sin oferta (F-902).
- **Reglamento peruano de IA por niveles de riesgo (sept-2025)**, que alcanzará a la tarificación y los siniestros con
  IA (F-907).
- **Seguros de vida que se usan en vida y cambian con la etapa** (Bradesco Vida Viva, F-905), sin cifras.
- **La frontera de la delegación en IA:** se acepta que cotice o informe, no que presente un siniestro o cancele por
  uno (F-916). Medirla en Perú es un vacío.
- **Hubs de salud con valor diario como respuesta al "no lo usé"** (F-895; propuesta de una agencia, sin
  resultados).

**Eje candidato para escenarios:** quién será dueño de la relación diaria con el cliente. Puede ser la
aseguradora, un banco o una billetera, el empleador o corredor, o una interfaz de IA. Es una hipótesis para el
ejercicio, no un hallazgo.

## Anexo C · Escala de evidencia usada

🟢 A: académico revisado por pares, con método y muestra explícitos · 🔵 B: regulador, organismo oficial o
reporte auditado · 🟡 C: consultora o industria con método propio no auditable · 🟠 D: prensa o cifra de la
propia empresa sin método · 🔴 E: opinión o marketing sin método. Detalle de cada fuente en
`research/fuentes/codice.md` (F-847 a F-916, más F-183, F-353 y F-442). Enlaces en el Anexo D.

## Anexo D · Referencias con enlace

Cada fuente citada en el informe, con su número del registro de fuentes del proyecto. Los enlaces llevan a la fuente original o, si no estuvo accesible, al resumen o la cobertura desde donde se leyó. Los documentos aportados por la usuaria se indican como tales.

- **F-17** · Maier, M. et al. (2022). *No evidence for nudging after adjusting for publication bias (PNAS)*. 🟢 A. [Ver fuente](https://www.pnas.org/doi/10.1073/pnas.2200300119)
- **F-183** · Bain & Company, con datos de NPS Prism (2023). *Insurers Have a Digital Dilemma: Complex Claims*. 🟡 C. [Ver fuente](https://www.bain.com/insights/insurers-have-digital-dilemma-complex-claims-snap-chart/)
- **F-353** · Vitality Group; validación actuarial de Arbital Health (2024). *Vitality Impact Study*. 🔵 B. [Ver fuente](https://vitalitygroup.com/insights/independent-actuaries-confirm-methodology-in-vitalitys-impact-study/)
- **F-442** · Equipo de investigación en seguridad vial (autoría no capturada en detalle) (2026). *A national randomized field experiment testing the impact of simulated usage-based insurance programs on driver safety (Accident Analysis & Prevention)*. 🟢 A. [Ver registro del ensayo](https://clinicaltrials.gov/study/NCT06101251) · [Ver revista](https://www.sciencedirect.com/journal/accident-analysis-and-prevention)
- **F-847** · Campbell, D. & Frei, F. (Management Science 56(1):4-24) (2010). *Cost Structure, Customer Profitability, and Retention Implications of Self-Service Distribution Channels*. 🟢 A. [Ver fuente](https://pubsonline.informs.org/doi/10.1287/mnsc.1090.1132)
- **F-848** · Xue, M.; Hitt, L. M.; Chen, P. (Management Science 57(2):291-307) (2011). *Determinants and Outcomes of Internet Banking Adoption*. 🟢 A. [Ver fuente](https://doi.org/10.1287/mnsc.1100.1187)
- **F-849** · Becker, Stolper & Walter (Zeitschrift für das gesamte Genossenschaftswesen 72(4):234-267) (2022). *The Impact of Mobile Banking Adoption on Retail Banking in Germany*. 🟢 A. [Ver fuente](https://doi.org/10.1515/zfgg-2022-0019)
- **F-850** · Kumar, A. & Telang, R. (Information Systems Research 23(3-1):721-737) (2012). *Does the Web Reduce Customer Service Cost? Empirical Evidence from a Call Center*. 🟢 A. [Ver fuente](https://doi.org/10.1287/isre.1110.0390)
- **F-851** · Turley, M. et al. (American Journal of Managed Care) (2012). *Patient portal use and health plan membership retention (Kaiser Permanente Northwest, My Health Manager)*. 🟢 A. [Ver fuente](https://pmc.ncbi.nlm.nih.gov/articles/PMC4215918)
- **F-852** · Brockett, P. L.; Golden, L. L.; Guillen, M.; Nielsen, J. P.; Parner, J.; Pérez-Marín, A. M. (Journal of Risk and Insurance 75(3):713-737) (2008). *Survival Analysis of a Household Portfolio of Insurance Policies: How Much Time Do You Have to Stop Total Customer Defection?*. 🟢 A. [Ver fuente](https://ideas.repec.org/a/bla/jrinsu/v75y2008i3p713-737.html)
- **F-854** · Jones, D.; Molitor, D.; Reif, J. (Quarterly Journal of Economics 134(4):1747-1791) (2019). *What Do Workplace Wellness Programs Do? Evidence from the Illinois Workplace Wellness Study*. 🟢 A. [Ver fuente](https://econpapers.repec.org/RePEc:oup:qjecon:v:134:y:2019:i:4:p:1747-1791.)
- **F-855** · Song, Z. & Baicker, K. (JAMA) (2019). *Effect of a Workplace Wellness Program on Employee Health and Economic Outcomes: A Randomized Clinical Trial*. 🟢 A. [Ver fuente](https://hcp.hms.harvard.edu/publication/effect-workplace-wellness-program-employee-health-and-economic-outcomes-randomized)
- **F-856** · Singh, N.; Panigrahi, R.; Shekhar, R. (Indian Journal of Marketing 54(7):68-82; DOI 10.17010/ijom/2024/v54/i7/174017) (2024). *Fostering Digital Engagement and Customer Retention in Indian Insurance: An Empirical Study*. 🟡 C. [Ver fuente](https://indianjournalofmarketing.com/index.php/ijom/article/view/174017) · Documento aportado por la usuaria.
- **F-857** · Lemonade, Inc. (Form 10-K FY2025 y cartas a accionistas 2025, SEC) (2026). *Form 10-K FY2025; Shareholder letters Q2-Q4 2025*. 🔵 B. [Ver fuente](https://www.sec.gov/Archives/edgar/data/1691421/000169142126000016/lmnd-20251231.htm)
- **F-858** · Oscar Health, Inc. (Form 10-K FY2025; llamadas de resultados 1T25 y 1T26) (2026). *Form 10-K FY2025; earnings calls*. 🟡 C. [Ver fuente](https://www.sec.gov/Archives/edgar/data/1568651/000156865126000011/oscr-20251231.htm)
- **F-859** · Alan (carta a accionistas Q2 2025) (2025). *Alan - 2025 Q2 Letter to Shareholders*. 🟠 D. [Ver fuente](https://alan.com/en/blog/discover-alan/a/alan-2025-q2-letter-to-shareholders)
- **F-860** · Vitality UK (materiales para asesores) / Discovery Life (presentaciones a inversionistas); SOA 2019 (2018-2025). *Vitality lapse-by-status claims (2023 Life claims and benefits report; adviser campaign pages; SOA 2019 Annual Meeting session 041)*. 🟠 D. [Ver fuente](https://adviser.vitality.co.uk/campaigns/live-longer-with-vitality)
- **F-861** · AIA New Zealand (vía Insurance Business NZ) (s.f.). *"Advisers are crucial" in AIA NZ initiative*. 🟠 D. [Ver fuente](https://www.insurancebusinessmag.com/nz/news/breaking-news/advisers-are-crucial-in-aia-nz-initiative-423895.aspx)
- **F-862** · Ping An Insurance (resultados anuales 2024, HKEX) y comunicados de prensa (2025). *2024 Annual Results announcement*. 🔵 B. [Ver fuente](https://www1.hkexnews.hk/listedco/listconews/sehk/2025/0319/2025031900856.pdf)
- **F-863** · Nubank y Chubb (comunicados y prensa especializada) (2024). *Nubank and Chubb reach 2 million active insurance policies in Brazil*. 🟠 D. [Ver fuente](https://coverager.com/nubank-and-chubb-reach-2-million-active-insurance-policies-in-brazil/)
- **F-864** · Mercado Pago (vía LatamFintech; El Cronista) (2025). *Mercado Pago acelera su estrategia en seguros en Brasil con cuatro nuevos productos impulsados por IA*. 🟠 D. [Ver fuente](https://www.latamfintech.co/articles/mercado-pago-acelera-su-estrategia-en-seguros-en-brasil-con-cuatro-nuevos-productos-impulsados-por-ia)
- **F-865** · Porto Seguro (presentación a inversionistas vía Quartr; release 1T25; CQCS) (2025). *Porto Seguro investor presentation; Release 1T25; entrevista a Patrícia Chacon (COO)*. 🟡 C. [Ver fuente](https://cqcs.com.br/noticia/patricia-chacon-coo-da-porto-seguro-revela-como-a-seguradora-esta-se-preparando-para-o-futuro/)
- **F-866** · Forbes Perú (entrevista a Pacífico Seguros) (2022). *Pacífico Seguros: iniciamos con solo 4 productos digitales y ahora ya tenemos más de 18*. 🟠 D. [Ver fuente](https://forbes.pe/negocios/2022-11-03/pacifico-seguros-iniciamos-con-solo-4-productos-digitales-y-ahora-ya-tenemos-mas-de-18/)
- **F-867** · Interseguro (memorias anuales 2019 y 2022) (2019-2023). *Memoria Anual 2019; Memoria Anual 2022*. 🟡 C. [Ver fuente](https://www.interseguro.pe/memoria/2022.pdf)
- **F-868** · La Positiva Seguros (vía Cámara de Comercio Canadá-Perú) (2024). *La Positiva Seguros and its commitment to simplicity, positivism and generation of trust*. 🟠 D. [Ver fuente](https://canadaperu.org/en/noticia/la-positiva-seguros-and-its-commitment-simplicity-positivism-and-generation-trust)
- **F-869** · Gestión; Perú Retail; El Comercio (cobertura de Yape, BCP) (2025-2026). *Yape: seguro de salud, venta de SOAT y resultados 2025*. 🟠 D. [Ver fuente](https://www.peru-retail.com/yape-se-consolida-como-gigante-financiero-con-1-8-millones-de-prestamos-mensuales/)
- **F-870** · Bloomberg Línea (Justos, Brasil) (2025). *Ribbit e Kaszek reforçam aposta na insurtech Justos com aporte de R$ 92 milhões*. 🟠 D. [Ver fuente](https://www.bloomberglinea.com.br/startups/ribbit-e-kaszek-reforcam-aposta-na-insurtech-justos-que-capta-r-92-milhoes/)
- **F-871** · Root, Inc. (resultados 2025; llamada 4T25) (2026). *Root Q4 2025 earnings*. 🔵 B. [Ver fuente](https://www.fool.com/earnings/call-transcripts/2026/02/25/root-root-q4-2025-earnings-call-transcript)
- **F-872** · J.D. Power (2025). *2025 U.S. Claims Digital Experience Study*. 🟡 C. [Ver fuente](https://www.jdpower.com/business/press-releases/2025-us-claims-digital-experience-study/)
- **F-874** · J.D. Power (2025). *2025 U.S. Auto Claims Satisfaction Study*. 🟡 C. [Ver fuente](https://www.jdpower.com/business/press-releases/2025-us-auto-claims-satisfaction-study)
- **F-876** · McKinsey (2023, 'Elevating customer experience'), citado por artículo académico serbio (2023). *Frecuencia de interacción en seguros vs. banca*. 🟠 D. [Ver fuente](https://phaidrabg.bg.ac.rs/open/o:35874)
- **F-877** · Airkit (BusinessWire); AWS (Toyota Insurance); HCLTech (casos de proveedores) (2021-2025). *Casos de proveedores sobre deflexión de llamadas en aseguradoras*. 🔴 E. [Ver fuente](https://aws.amazon.com/blogs/contact-center/how-toyota-insurance-cut-customer-service-costs-and-achieved-self-service-with-amazon-connect)
- **F-878** · Finnovista (vía FF News; MAPFRE Insights) (2026). *LatAm insurtech sector closes 2025 with 530 companies and US$200 million in funding*. 🟡 C. [Ver fuente](https://ffnews.com/newsarticle/insurtech/latam-insurtech-sector-closes-2025-with-530-companies-and-us200-million-in-funding/)
- **F-879** · BBVA México (Reporte Trimestral 1T22) (2022). *Reporte Trimestral BBVA México 1T22*. 🔵 B. [Ver fuente](https://investors.bbva.mx/wp-content/uploads/2022/04/Reporte-Trimestral-BBVA-México-1T22.pdf)
- **F-880** · J.D. Power (2025 U.S. Home Insurance Study) y Amica (comunicado 2026) (2025-2026). *Amica: primer lugar en satisfacción en hogar e inquilinos (2025) y en auto Nueva Inglaterra (2026)*. 🟡 C. [Ver fuente](https://www.businesswire.com/news/home/20250916810246/en)
- **F-883** · Andina (citando a Indecopi); resoluciones de Indecopi 2025 (2022-2025). *Indecopi impuso 1.408 sanciones a 26 empresas del sector Seguros; sanciones 2025 por demoras en indemnización*. 🔵 B. [Ver fuente](https://andina.pe/agencia/noticia-indecopi-impuso-1408-sanciones-a-26-empresas-del-sector-seguros-896401.aspx)
- **F-885** · InsuranceNewsNet (cobertura) (2025). *AI vs. AI: Patients deploy bots to battle health insurers that deny care*. 🟠 D. [Ver fuente](https://insurancenewsnet.com/oarticle/ai-vs-ai-patients-deploy-bots-to-battle-health-insurers-that-deny-care-8)
- **F-886** · Financial Conduct Authority (Reino Unido) (2025). *Evaluation Paper 25/2: Our general insurance pricing practices (GIPP) remedies*. 🔵 B. [Ver fuente](https://www.fca.org.uk/publications/corporate-documents/evaluation-paper-25-2-general-insurance-pricing-practices-remedies)
- **F-887** · Autores del protocolo ReachUHC (Trials, BMC; medRxiv) (2025). *ReachUHC: a randomized controlled trial of a mobile phone-based reminder and automatic renewal intervention to increase health insurance renewal rates in Kumasi, Ghana*. 🔵 B. [Ver fuente](https://link.springer.com/article/10.1186/s13063-025-09360-1)
- **F-888** · Wood, W. & Neal, D. T. (Psychological Review 114(4)) (2007). *A new look at habits and the habit-goal interface*. 🟢 A. [Ver fuente](https://dornsife.usc.edu/wendy-wood/wp-content/uploads/sites/183/2023/10/wood.neal_.2007psychrev_a_new_look_at_habits_and_the_interface_between_habits_and_goals.pdf)
- **F-889** · Handel, B. R. (American Economic Review 103(7):2643-2682) (2013). *Adverse Selection and Inertia in Health Insurance Markets: When Nudging Hurts*. 🟢 A. [Ver fuente](https://econpapers.repec.org/RePEc:aea:aecrev:v:103:y:2013:i:7:p:2643-82)
- **F-890** · LexisNexis Risk Solutions (2023). *Moment of Truth: claims satisfaction and auto insurance switching (whitepaper)*. 🟡 C. [Ver fuente](https://www.claimsjournal.com/news/national/2023/06/08/317385.htm)
- **F-891** · INFORMS (nota de prensa sobre artículo en Marketing Science; autores no verificados) (s.f.). *Insurance companies: want to steal your competitors' customers? New research says it may cost you*. 🔵 B. [Ver fuente](https://www.informs.org/News-Room/INFORMS-Releases/News-Releases/Insurance-companies-want-to-steal-your-competitors-customers-New-research-says-it-may-cost-you)
- **F-894** · Sunstein, C. R. (Behavioural Public Policy 6(4):654-673) (2022). *Sludge Audits*. 🟢 A. [Ver fuente](https://www.cambridge.org/core/journals/behavioural-public-policy/article/abs/sludge-audits/12A7E338984CE8807CC1E078EC4F13A7)
- **F-895** · Graphite Digital (encuesta de Opinium por encargo) (2025). *Redefining digital experience in health insurance: strategic priorities for a changing market*. 🟡 C. [Ver fuente](https://graphitedigital.com) · Documento aportado por la usuaria.
- **F-896** · Poulton, D. & Magnoni, B. (MicroInsurance Centre, proyecto MILK) (2013). *MILK Brief #16: 'Doing the Math' – Life Microinsurance in Mexico (Compartamos Banco)*. 🟡 C. [Ver fuente](https://microinsurancecentre.milliman.com/en/insight/milk-brief-16-doing-the-math-life-microinsurance-in-mexico) · Documento aportado por la usuaria.
- **F-897** · Zimmerman, E.; Bauchet, J.; Magnoni, B.; Poulton, D. (MicroInsurance Centre, proyecto MILK); trabajo relacionado de Bauchet (8.700 prestatarios) (2013). *Protecting those left behind: an experimental study of life microinsurance purchase decisions of Compartamos Banco's borrowers*. 🔵 B. [Ver fuente](https://microinsurancecentre.milliman.com/en/insight/milk-rct-protecting-those-left-behind-an-experimental-study-of-life-microinsurance-purchase-decision)
- **F-898** · Martínez Gutiérrez, A. L. (coord.); Hindriks, P.; Reséndiz Ruiz, C.; Santos Ochoa, J. (por encargo de Treo) (c. 2021 (año no visible en el documento)). *El camino a la tranquilidad financiera: oportunidades para la disrupción de las finanzas personales en México. Estudio completo*. 🟡 C. [Ver fuente](https://treo.mx) · Documento aportado por la usuaria.
- **F-899** · Flat 101 (Vanessa Ballesteros Abad y Ricardo Tayar López; posts de LinkedIn resumidos por Claude a partir de capturas de la usuaria) — cuentan como una sola fuente de origen (2025-2026). *Voces de practitioners de behavioral design sobre confianza, fricción, delegación a IA y segmentación por situación*. 🔴 E. Archivo de la usuaria: voces-practitioners.md (posts de LinkedIn, sin URL individual).
- **F-900** · Craddock, C.; Marchi, R.; Morales, J.; Spak, S.; Waisser, S. (McKinsey & Company) (2023). *Reporte Global de Seguros 2023: Capturando la siguiente ola de crecimiento en América Latina (septiembre 2023)*. 🟡 C. PDF aportado por la usuaria (versión en español); URL pública no verificada en esta sesión.
- **F-901** · Capgemini Research Institute for Financial Services (2024). *World Property and Casualty Insurance Report 2024: Become an underwriting trailblazer*. 🟡 C. DOCX aportado por la usuaria; URL pública no verificada en esta sesión.
- **F-902** · Inga Falcón, P. (por encargo de la Oficina de Perú del PNUD y su Iniciativa de Seguros y Financiamiento de Riesgos) (2025). *Informe de diagnóstico de microseguros en el Perú (15 de diciembre de 2025)*. 🔵 B. PDF aportado por la usuaria; URL pública no verificada en esta sesión.
- **F-903** · SBS y CAF (citada vía el diagnóstico del PNUD, F-902) (2022). *Encuesta de Capacidades Financieras del Perú 2022 (resultados sobre seguros)*. 🔵 B. Cita secundaria en F-902; documento original no consultado.
- **F-904** · Coloma C., F. (Instituto de Economía, Pontificia Universidad Católica de Chile; ex Superintendente de Valores y Seguros) (2019). *Licitación de los seguros asociados a los créditos hipotecarios: algunos resultados y propuestas de mejoramiento (Documento de Política Pública)*. 🔵 B. PDF aportado por la usuaria (Documento de Política Pública, Instituto de Economía UC); URL pública no verificada.
- **F-905** · Saldanha, K. & Staehle, T. (Accenture) (2023). *Seeing the people behind the policies: Accenture's Global Insurance Consumer Study 2023*. 🟡 C. DOCX aportado por la usuaria; URL pública no verificada en esta sesión.
- **F-906** · Banco de Ideas Credicorp, con Ipsos (Rojas, P.; Wiener, L.; Pinedo, S.; Zamora, C.; Sánchez, L.) (2026). *Índice de Inclusión Financiera de Credicorp 2026: un vínculo más digital (octubre 2026)*. 🟡 C. DOCX aportado por la usuaria; URL pública no verificada en esta sesión.
- **F-907** · Pérez-Llorca (equipos de Seguros y Reaseguros de Colombia, España, México, Portugal y Perú) (2026). *Actualidad Iberoamericana de Seguros, tercer trimestre 2026*. 🟡 C. DOCX aportado por la usuaria; URL pública no verificada en esta sesión.
- **F-908** · Enríquez Quicaño, J. B.; Alvarado Mesa, M. F.; Romero Valdivia, M. S. (Desafíos: Economía y Empresa n.° 8, Universidad de Lima, pp. 11-38; DOI 10.26439/ddee2026.n008.7940) (2025). *Aplicación de la economía conductual en el mercado de los seguros*. 🟡 C. [Ver fuente](https://doi.org/10.26439/ddee2026.n008.7940) · Documento aportado por la usuaria.
- **F-909** · Beway, en colaboración con la Asociación Latinoamericana de Suscriptores Marítimos (autoría individual no indicada) (s.f. (c. 2025-2026)). *Cerrar la brecha de aseguramiento marítimo en América Latina: una mirada desde las ciencias del comportamiento*. 🟠 D. Archivo de la usuaria: articulo-bewAY-_Brecha-aseguramiento-maritimo.md (blog.beway.com, dominio bloqueado desde la sesión).
- **F-912** · Luo, X.; Tong, S.; Fang, Z.; Qu, Z. (Marketing Science 38(6):937-947; DOI 10.1287/mksc.2019.1192) (2019). *Frontiers: Machines vs. Humans: The Impact of Artificial Intelligence Chatbot Disclosure on Customer Purchases*. 🟢 A. [Ver fuente](https://econpapers.repec.org/RePEc:inm:ormksc:v:38:y:2019:i:6:p:937-947)
- **F-913** · Jachimowicz, J. M.; Duncan, S.; Weber, E. U.; Johnson, E. J. (Behavioural Public Policy 3(2):159-186; DOI 10.1017/bpp.2019.25) (2019). *When and why defaults influence decisions: a meta-analysis of default effects*. 🟢 A. [Ver fuente](https://econpapers.repec.org/RePEc:cup:bpubpo:v:3:y:2019:i:02:p:159-186_00)
- **F-914** · Longoni, C.; Bonezzi, A.; Morewedge, C. K. (Journal of Consumer Research) (2019). *Resistance to Medical Artificial Intelligence*. 🟢 A. [Ver fuente](https://www.scinapse.io/papers/2942858056)
- **F-915** · Dietvorst, B. J.; Simmons, J. P.; Massey, C. (Management Science 64(3)) (2018). *Overcoming Algorithm Aversion: People Will Use Imperfect Algorithms If They Can (Even Slightly) Modify Them*. 🟢 A. [Ver fuente](https://pubsonline.informs.org/doi/10.1287/mnsc.2016.2643)
- **F-916** · Insurity (cita secundaria) (2026). *Encuesta a consumidores de EE.UU. sobre comodidad con la IA en seguros*. 🟠 D. Cita secundaria; fuente original no consultada.
