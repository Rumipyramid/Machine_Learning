# Informe · Pregunta 1 del benchmarking: ¿para qué sirve la recurrencia digital en un seguro?

**Insumo para:** Gerencia de Digital, RIMAC · **Fecha:** 28-10-2026 · **Estado:** versión de trabajo 7
(integra quince documentos aportados por la usuaria y doce papers verificados a partir de ellos; ocho documentos
internos del equipo se omiten de esta copia; el formato para la gerencia se define después)
**Basado en:** `research/_nodes/valor-recurrencia-digital-seguros.md` (v1.1, 2026-10-28). Las fuentes se
citan como (Autor, año) y con su número del registro de fuentes del proyecto (F-n).
**Alcance:**
- Seguros de Perú y LatAm primero.
- Banca, salud y retail como análogos.
- EE.UU., Europa y Asia solo como contraste (🌐), sin generalizar a Perú.
- Periodo 2021-2026. Los estudios canónicos anteriores van marcados con 📚.
- RIMAC está excluida como caso, fuente o benchmark.

**Cómo leer las marcas:** 📎 señala lo que entró o cambió con los documentos aportados. Así se ve en qué secciones
repercutieron. La §7 resume ese cambio teoría por teoría. 🔧 señala lo que se agregó en la versión 7 para aterrizar el
informe: qué significa cada teoría, cómo se mide, ejemplos y qué decisión ayuda a tomar.

**Mapa rápido para decidir:** la §2.1 explica cada forma de valor con ejemplos; la §3.1 muestra qué tarea conviene en
qué canal; la §4.1 traduce la lectura conductual en reglas de decisión; la §5 ordena las decisiones de la gerencia; el
Anexo C explica los métodos de medición con ejemplos; el Anexo D lista los datos que hay que pedir a los ramos.

---

## 1. Conclusión

**La actividad digital produce valor en un seguro cuando resuelve algo, no cuando genera visitas.** Las tres
pistas de investigación coinciden: la académica, la de resultados de negocio y la social. Ninguna fuente
encontrada muestra que la frecuencia de uso, por sí sola, genere valor.

**Consecuencia para la meta:** el MAU mide cuántos entran, no cuántos resuelven. Hay cinco formas en que lo
digital puede producir valor. Cada una pide un indicador distinto. **En dos de ellas, un buen resultado
baja la actividad**: un cliente que resolvió rápido no vuelve a entrar.

📎 **Lo que agregaron los documentos aportados.** No cambiaron la conclusión; la anclaron en Perú y le sumaron
cuatro matices:

1. **La confianza en el momento de verdad es la forma de valor con más respaldo en Perú.** Antes descansaba en
   encuestas de EE.UU. Ahora la sostienen datos peruanos de reclamos, microseguros y desconfianza, y un caso de
   México. En Perú el problema está en cumplir y pagar, no en el canal.
2. **La puerta de entrada ajena vende, pero no retiene ni basta.** La billetera diaria no subió la tenencia de
   seguros. La puerta cobra comisiones altas y genera reclamos por cobros no consentidos. Cuando se acaba la
   relación que ancla el seguro, el seguro se va.
3. **Los canales conviven por función, no por atraso.** La gente busca en línea y contrata con una persona. Los
   canales caros sobreviven por lo que resuelven. "Todo digital" puede ser la meta equivocada, no solo una meta
   difícil.
4. **Digitalizar lo que ya se vende es defensa, no ventaja.** Si todos agregan el mismo canal, todos cargan el costo
   y nadie gana posición.

🔧 **Una voz del sector coincide.** En una entrevista, el CEO de Credicorp dijo que lo digital "es un medio, no un fin";
que Yape nació para resolver dos problemas a la vez, mejorar la experiencia del cliente y reducir el costo de servirle;
que los productos financieros son hoy commodities; y que los canales (agencias, personas e IA) van a convivir según la
importancia de la decisión. Es una opinión, no evidencia (F-932, 🔴 E), pero calza con cuatro hallazgos de este
informe (§3.8).

**Lo que la gerencia tiene que decidir:** cuál de las cinco formas de valor persigue el canal digital, y
por lo tanto qué indicador acompaña o reemplaza al MAU. Este informe no toma esa decisión. Entrega las
opciones y qué tan probada está cada una. 📎 Como inferencia, no como hallazgo: la evidencia acumulada favorece
dos candidatas para Perú. Una es la confianza en el momento de verdad, medida con tiempo a resolución y reclamos
escalados. La otra es el costo de servir, limitado a las tareas de información clara.

---

## 2. Menú de teorías de valor

| # | Teoría de valor | Indicador en vez del MAU | Mejor evidencia | 📎 Respaldo en Perú y LatAm | Qué tan probada |
|---|---|---|---|---|---|
| 1 | **Costo de servir:** resolver en digital lo que hoy va al teléfono | Contactos por necesidad resuelta, separados por tipo de tarea | 📚 En una aseguradora de salud, el portal bajó 29% las llamadas sobre información clara y fácil de encontrar, pero subió 14% el total de llamadas, porque generó llamadas sobre información ambigua (Kumar y Telang, 2012, F-850) | Solo cifras de empresa (Pacífico: más de 60% de consultas por autoservicio, F-866). 📎 🌐 En Francia, entre 75% y 90% de las contrataciones termina por teléfono aun con opción en línea (F-921) | 🟢 Causal, efecto en ambas direcciones |
| 2 | **Retención:** el cliente digital se queda más | Renovación o persistencia en cohortes emparejadas | 📚 En banca, adoptar lo digital se asocia a más retención aun controlando que adopta quien ya era fiel (Campbell y Frei, 2010, F-847). En un plan de salud, 96,9% contra 90,5% (Turley et al., 2012, F-851; observacional). **En seguros no hay ningún estudio causal** | 📎 Ningún estudio de retención. Sí motivos de fuga que no dependen del canal: en Perú, solo 12% mantiene el seguro de terremoto al terminar el crédito (F-902); en México, 47% lo pierde al cambiar de trabajo (F-898) | 🔵 Plausible por analogía · ⚪ No demostrado en seguros |
| 3 | **Venta cruzada:** el cliente digital compra más productos | Productos por cliente; lead a póliza; prima nueva de clientes existentes | Los usuarios digitales tienen más productos en banca (Xue et al., 2011, F-848; Becker et al., 2022, F-849). La venta digital de Porto Seguro es casi toda a clientes que ya tiene: 84%, según su meta 2025 (F-865) | Puertas ajenas venden a escala (F-863, F-864, F-869). 📎 Pero la tenencia no sube con la billetera (F-906), la puerta cobra comisiones cercanas a 50% (F-902) y 38,4% de los reclamos de seguros ante Indecopi en 2023 fue por contratación o cargo indebido (F-902) | 🟡 Asociación |
| 4 | **Prevención:** lo digital cambia la conducta de riesgo | Siniestralidad por cohorte, separando selección de efecto | En auto, un experimento de campo con telemetría redujo velocidad y frenadas bruscas (F-442). En salud, dos ensayos aleatorizados de programas de bienestar no bajaron el gasto médico (Jones, Molitor y Reif, 2019, F-854; Song y Baicker, 2019, F-855) | Solo un dato de empresa en Brasil (Justos, F-870) | 🟢 En auto (conducta) · 🔴 Negativa en salud (gasto) |
| 5 | **Confianza en el momento de verdad:** resolver bien el siniestro | Tiempo a resolución; tasa de escalamiento de digital a humano; resuelto al primer intento; 📎 reclamos que escalan | 🌐 Con mala experiencia digital del siniestro, 52% está en riesgo de irse; con experiencia excelente, 4% (J.D. Power, 2025, F-872). La confianza es el factor más importante del siniestro y el canal digital el menos importante, entre ocho (J.D. Power, 2025, F-874) | 📎 La más respaldada: en México, pago en 9 días que evitó deuda cara (F-896); en Perú, los microseguros devuelven 16,7% de la prima (F-902), 47% de quienes desconfían dice que no cumplen (F-903) y los reclamos que escalan subieron de 61,6 a 141 por cada mil (F-902) | 🟡 Asociación · 📎 la más consistente y la única con evidencia peruana de varios tipos |

**Lectura:** solo la teoría 1 tiene evidencia causal en seguros, y su efecto va en las dos direcciones. La
teoría 2, que es la tesis central del canal ("el cliente digital es más fiel"), es la menos probada en
seguros. 📎 La teoría 5 sigue siendo asociación, pero es la única que acumula evidencia peruana de varios tipos.

### 2.1 🔧 Qué significa cada teoría, con ejemplos

Cada teoría es una respuesta distinta a la pregunta "¿para qué queremos que el cliente use el canal digital?". Elegir
una cambia qué se construye, qué se mide y qué se considera éxito. Cada ejemplo es una situación construida para
explicar la teoría, pero cada uno descansa en una fuente: la línea **Sustento** dice cuál, y qué tan sólida es.

**1. Costo de servir: que resolver le cueste menos a la compañía.**

- **Qué es.** Lo digital crea valor si atiende una necesidad que hoy cuesta más por otro canal (una llamada, una visita,
  un correo que alguien procesa a mano).
- **Cómo produce valor.** Un pedido resuelto en el app cuesta menos que el mismo pedido en el call center. Pero solo si
  el pedido no vuelve por otro canal.
- **Ejemplo.** Un asegurado de salud quiere saber en qué va su reembolso. Si el app muestra "en revisión, pago estimado
  el jueves, no falta ningún documento", no llama. Si solo dice "en proceso", llama dos veces.
- **Sustento.** En una aseguradora de salud de EE.UU., el portal web bajó 29% las llamadas sobre información clara y subió
  las llamadas sobre información ambigua, como pólizas y reclamos (Kumar y Telang, 2012, F-850; 🟢 A, causal).
- **Qué decisión informa.** Qué flujos mover primero a digital y cuáles rediseñar antes de moverlos.
- **Cómo se mide.** Con **contactos por necesidad resuelta**: cuántas veces tuvo que contactar el cliente, por cualquier
  canal, para resolver una necesidad. Ejemplos de necesidad: "cobrar un reembolso", "obtener la carta de garantía",
  "reportar un choque y tener el auto reparado", "descargar la constancia del SOAT", "cambiar la tarjeta de cobro". Si un
  reembolso generó una carga en el app, dos llamadas de "¿en qué va?" y un chat, son cuatro contactos para una
  necesidad. La meta es bajar ese número, no subir las visitas al app. Indicadores derivados: tasa de recontacto a 7
  días, contactos de "¿en qué va mi trámite?" por caso y porcentaje resuelto sin intervención humana (detalle en el
  Anexo C).
- **Trampa.** Contar como éxito las sesiones del app. El cliente que entra cinco veces a revisar su reembolso no es un
  cliente comprometido: es un cliente que no sabe qué está pasando.

**2. Retención: que el cliente se quede más tiempo.**

- **Qué es.** Lo digital crea valor si hace que el cliente renueve o mantenga su póliza más que si no lo usara.
- **Cómo produce valor.** Cada año que el cliente se queda aporta prima sin costo de adquisición.
- **Ejemplo.** Dos clientes de vehicular. Uno usa el app y renueva; el otro no la usa y se va. La pregunta es si el app
  *causó* la renovación o si el que la usa ya era el tipo de cliente que renueva.
- **Sustento.** En banca, la adopción digital se asoció a más retención aun controlando la autoselección (Campbell y
  Frei, 2010, F-847; 🟢 A). Pero en un ensayo con sorteo, quienes eligieron participar en un programa ya eran distintos
  antes de empezar, y el programa no cambió su permanencia (Jones et al., 2019, F-854; 🟢 A).
- **Qué decisión informa.** Cuánto invertir en el app como herramienta de fidelización.
- **Cómo se mide.** Con **renovación** (porcentaje que renueva al vencer la póliza) o **persistencia** (porcentaje de
  pólizas que siguen vigentes a los 13 y 25 meses, la medida usual en vida). Para saber si lo digital la causa, se
  compara contra **cohortes emparejadas** o con un **despliegue escalonado** (explicados en el Anexo C).
- **Trampa.** Comparar usuarios y no usuarios del app y atribuir la diferencia al app. Quien adopta lo digital ya era
  distinto antes de adoptarlo (§3.2).

**3. Venta cruzada: que el cliente compre más productos.**

- **Qué es.** Lo digital crea valor si un cliente que lo usa termina comprando otro seguro.
- **Cómo produce valor.** Vender a quien ya es cliente cuesta menos que conseguir uno nuevo.
- **Ejemplo.** Quien compra el SOAT en línea recibe, en el momento correcto, una oferta de vehicular o de salud. O una
  billetera ofrece un seguro a quien paga con ella todos los días.
- **Sustento.** Interseguro hizo crecer 66% su venta digital de SOAT en 2019, sin cifra publicada de venta cruzada
  (F-867; 🟡 C). Nubank llegó a 2 millones de pólizas vendidas en su app de uso diario, pero solo a 1,6% de su base
  (F-863; 🟠 D), y en Perú la billetera diaria no subió la tenencia de seguros (F-906; 🔵 B).
- **Qué decisión informa.** Si construir una puerta de entrada propia (como el SOAT) o aliarse con quien ya tiene la
  relación diaria (un banco, una billetera, un empleador).
- **Cómo se mide.** Productos por cliente; tasa de conversión de oferta a póliza; prima nueva que viene de clientes
  existentes; y, para saber si es efecto, la misma comparación contra un grupo de control.
- **Trampa.** Ver que los clientes digitales tienen más productos y concluir que lo digital los vendió. Puede ser al
  revés: quien ya tiene varios productos usa más el app.

**4. Prevención: que el cliente tenga menos siniestros.**

- **Qué es.** Lo digital crea valor si cambia la conducta de riesgo: manejar mejor, hacerse chequeos, cuidar la casa.
- **Cómo produce valor.** Menos siniestros o siniestros más baratos bajan el costo de la cartera.
- **Ejemplo.** Un programa de manejo con puntaje en el app; un programa de bienestar con retos de pasos.
- **Sustento.** En un experimento de campo nacional, la retroalimentación telemática redujo la velocidad y las frenadas
  bruscas (F-442; 🟢 A). Dos ensayos de bienestar laboral no bajaron el gasto médico (F-854, F-855; 🟢 A).
- **Qué decisión informa.** Si invertir en programas de engagement y bienestar, y cómo evaluarlos.
- **Cómo se mide.** Con **siniestralidad por cohorte, separando selección de efecto**. "Siniestralidad" es cuánto se
  paga en siniestros frente a la prima. "Por cohorte" significa comparar grupos que entraron en el mismo momento.
  "Separar selección de efecto" significa distinguir si el grupo siniestra menos *porque el programa lo cambió* (efecto)
  o *porque los que se inscriben ya eran de menor riesgo* (selección). El ejemplo más claro es el de un ensayo de
  bienestar laboral: los que se inscribieron gastaban 24% menos en salud *antes* de empezar; una comparación simple decía
  que el programa ahorraba US$104 al mes por persona; el ensayo con grupo de control mostró que no ahorraba nada (Jones,
  Molitor y Reif, 2019, F-854; detalle en §3.4 y en el Anexo C).
- **Trampa.** Presentar como prevención lo que es selección. La selección también vale (atrae buenos riesgos), pero se
  mide distinto y tiene otro costo: puede trasladar el costo a los clientes más pobres o enfermos.

**5. Confianza en el momento de verdad: que el cliente sienta que el seguro cumplió.**

- **Qué es.** Lo digital crea valor si ayuda a que el siniestro, el reembolso o la atención se resuelvan rápido, claro y
  con justicia.
- **Cómo produce valor.** El cliente decide si se queda, recomienda o reclama según cómo le fue cuando lo necesitó.
- **Ejemplo.** Tras un choque, el cliente reporta por el canal que prefiera, ve en todo momento en qué va su caso y sabe
  qué falta; si hay rechazo, recibe una explicación que entiende y una persona a quien preguntar.
- **Sustento.** Con una mala experiencia digital del siniestro, 52% de los clientes está en riesgo de irse; con una
  excelente, 4% (J.D. Power, 2025, F-872; 🟡 C, EE.UU.). En México, un pago de seguro de vida en 9 días evitó a las
  familias endeudarse caro (F-896; 🟡 C). En Perú, los reclamos de seguros que escalan a Indecopi o la SBS subieron de
  61,6 a 141 por cada mil entre 2018 y 2024 (F-902; 🔵 B).
- **Qué decisión informa.** Dónde poner la inversión digital en el siniestro y dónde poner personas.
- **Cómo se mide.** Tiempo desde el aviso hasta la resolución; porcentaje resuelto al primer intento; porcentaje que
  escala de digital a humano sin haberlo planificado; reclamos ante la compañía, y los que escalan a Indecopi o la SBS.
- **Trampa.** Medir solo el porcentaje de siniestros reportados por el app. Un reporte digital que termina en tres
  llamadas y un reclamo no es un éxito.

---

## 3. Hallazgos por teoría de valor

### 3.1 Costo de servir: lo claro migra, lo ambiguo vuelve al teléfono

- **El estudio causal más directo es de una aseguradora de salud.** Usar el portal subió las llamadas 14% en
  total. Bajaron 29% las de información clara. Subieron las de información ambigua, como pólizas y reclamos
  (Kumar y Telang, 2012, F-850).
- 🔧 **En banca pasó algo parecido, y vale la pena entenderlo bien.** Campbell y Frei siguieron a 100.000 clientes de un
  banco grande de EE.UU. durante 30 meses (2010, F-847; detalle verificado con el resumen editorial de la revista,
  Gorman, 2010, F-931). Quienes empezaron a usar la banca online:
  - usaron *menos* el cajero y la respuesta automática por teléfono, los canales baratos;
  - usaron *más* la sucursal y el call center, los canales caros. Los autores lo atribuyen, como hipótesis, a que les
    costaba entender y usar el canal nuevo;
  - hicieron más transacciones en total, porque cada una les costaba menos esfuerzo; por eso el costo promedio por
    cliente subió;
  - dejaron 11% menos de utilidad por cliente el primer año, por más costo y por menos comisiones cobradas.

  A cambio, el banco ganó satisfacción, retención a uno y tres años, y participación de mercado. Los autores controlan
  que quien adopta ya era distinto. La lección del editor de la revista: el beneficio principal del canal en línea es
  atraer y retener clientes, más que hacer más rentables a los que ya están. **Para un seguro:** lanzar un canal digital
  puede *subir* los contactos al principio. Si la meta es costo, hay que medir contactos por necesidad, no adopción.
- **Un banco alemán muestra lo contrario.** Con un grupo de control emparejado, quienes adoptan la banca móvil
  usan *menos* el call center (Becker et al., 2022, F-849).
- **Perú:** Pacífico reporta que más de 60% de las consultas y solicitudes se resuelven por autoservicio (chatbot
  y app), según Forbes Perú (2022, F-866). Es una cifra de la empresa, sin método.
- 📎 🌐 **Ofrecer el canal no traslada la tarea.** En Francia, la mayoría termina de contratar por teléfono aunque
  pueda hacerlo en línea (detalle en §3.6).
- **LatAm:** una aseguradora sin nombre desvía 30% de sus siniestros a una vía rápida por reglas, y otras pasaron la
  mayoría de sus siniestros de salud a digital con más satisfacción y menos costo, según McKinsey (2023, F-900), sin
  cifras verificables.
- **Proveedores de software:** prometen bajar entre 30% y 40% el costo de servir. No tienen método (F-877). No
  usar como dato.

**Implicancia:** antes de mover un flujo al canal digital, hay que preguntarse si su información es clara o
ambigua. En lo ambiguo, primero se rediseña el contenido; si no, el ahorro esperado se vuelve más llamadas.
Este patrón coincide con lo que muestra el diagnóstico interno de julio: lo digital gana en consultar y pierde
en gestionar y en lo urgente. 📎 La meta no es mover todo a digital. Es que cada tarea se resuelva en el canal que
mejor la resuelve, y medir la resolutividad por canal.

**🔧 Qué tarea conviene en qué canal: ejemplos.** La regla de fondo sale de la evidencia: lo claro y repetible migra a
digital; lo ambiguo, emocional o de alto monto necesita una persona, con lo digital acompañando. La tabla es una
propuesta para discutir con los ramos, no un hallazgo.

| Tipo de tarea | Ejemplos | Canal que mejor resuelve | Cómo saber si funciona | Evidencia detrás |
|---|---|---|---|---|
| Información clara y transaccional | Descargar la póliza o la constancia del SOAT; pagar la prima; cambiar la tarjeta; ver el estado de un reembolso; ubicar una clínica de la red | Autoservicio digital | Porcentaje resuelto sin ningún contacto posterior en 7 días | Lo claro migra y baja las llamadas (F-850) |
| Seguimiento de un trámite en curso | "¿En qué va mi reembolso?", "¿cuándo me pagan?", "¿mi auto ya está en el taller?" | Digital proactivo: avisar antes de que el cliente pregunte | Llamadas de "¿en qué va?" por caso | El seguimiento visible devuelve control; la ambigüedad genera llamadas (F-850) |
| Información ambigua o con consecuencias | "¿Esto me cubre?", preexistencias, deducibles, por qué rechazaron un reembolso | Digital con explicación en lenguaje claro y salida a una persona a un clic | Tasa de recontacto y de escalamiento | Lo ambiguo vuelve al teléfono (F-850); 30% de los reclamos complejos termina en una persona (F-183) |
| Siniestro simple y de bajo monto | Choque leve, rotura de lunas, reembolso de una consulta | Digital de punta a punta, con reglas de pago rápido | Tiempo hasta el pago; porcentaje pagado sin intervención | Vía rápida para siniestros simples (F-865, F-900) |
| Siniestro grave o de alta carga emocional | Hospitalización, fallecimiento, pérdida total, robo con violencia | Persona que acompaña, con lo digital para documentos y seguimiento | Tiempo a resolución; reclamos; satisfacción al cierre | La confianza pesa más que el canal (F-874); el pago rápido y justo crea valor (F-896) |
| Decisión de compra compleja | Elegir un seguro de salud o de vida | Buscar en línea y cerrar con una persona | Conversión de cotización en línea a póliza con asesor | La gente busca en línea y compra con una persona (F-918, F-900); solo 20% en Perú compraría digital (F-903) |
| Cancelación | Dar de baja una póliza | Digital y sin fricción artificial, con una oferta de retención opcional | Tiempo para cancelar; quejas | El regulador británico sancionó la fricción para retener (F-886) |

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
- 📎 **El estudio de India sobre seguros de vida, leído completo, es el ejemplo típico de esta evidencia débil**
  (Singh, Panigrahi y Shekhar, 2024, F-856). Mide la retención como actitud ("siento lealtad", "estoy dispuesto
  a seguir") y no como renovación real. Su muestra es de usuarios digitales diarios, 67% de ingreso alto y 97%
  urbana.
- 📎 **🌐 "No lo usé" es una razón para irse.** En una encuesta representativa del Reino Unido, 40% canceló o
  considera cancelar su seguro privado de salud. La razón más citada después del precio fue "no lo usé tanto como
  esperaba" (27%), y es la primera entre 18 y 34 años (Graphite Digital, 2025, F-895). Es intención declarada, y la
  autora vende experiencia digital.
- 📎 **🌐 Al irse, pesa más el precio que lo digital.** 27% de asegurados cambió de aseguradora en dos años, sobre todo
  por precio (60%) y cobertura (53%) (Capgemini, 2024, F-901; encuesta de una consultora).
- 📎 **Cuando se acaba el ancla, se va el seguro.** En Perú, más del 90% de las viviendas aseguradas contra terremoto
  lo están porque el banco lo exige con el crédito hipotecario. Al terminar de pagar, solo 12% mantiene el seguro
  (representantes del sector citados por prensa, vía el diagnóstico del PNUD, F-902; cita secundaria). En México, 47%
  de quienes dejaron de tener seguro lo atribuye a un cambio de trabajo (Treo, c. 2021, F-898, con datos de la ENIF
  2018). Ese tipo de fuga no la resuelve ningún canal.

  🔧 **Qué es un "ancla".** Es la relación externa al seguro que lo mantiene vigente sin que el cliente lo decida cada
  año. Cuando el ancla se acaba, el seguro queda expuesto. Las anclas más comunes:

  | Ancla | Qué seguros sostiene | Qué pasa cuando se acaba | Evidencia |
  |---|---|---|---|
  | Crédito hipotecario | Desgravamen; incendio y terremoto de la vivienda | Al terminar de pagar, solo 12% mantiene el seguro de terremoto | F-902 (cita secundaria) |
  | Empleo | Salud (EPS, planes colectivos), vida ley, seguros del empleador | Al cambiar de trabajo, 47% de quienes dejaron de tener seguro en México lo perdió | F-898 |
  | Crédito o financiamiento del vehículo | Seguro vehicular exigido por el banco o vendido con el auto | Al terminar el crédito, el cliente decide solo por primera vez | El ancla existe: 42% compraría su seguro en el concesionario (F-905). Qué pasa al terminar el crédito: sin dato; es inferencia por analogía con el seguro de terremoto (F-902) |
  | Microcrédito | Microseguro de vida o de desgravamen | Se sostiene mientras dura el crédito, pagado al ritmo de la cuota | F-896, F-897 |
  | Cuenta, tarjeta o billetera | Seguros masivos vendidos por el banco o la billetera | Depende del banco; la billetera no subió la tenencia por sí sola | F-906 |
  | La clínica (en salud) | Planes y seguros de salud | Si el cliente puede atenderse en su clínica sin el seguro, el seguro sobra | Hipótesis |
  | El corredor | Cartera del segmento de mayor ingreso | Si el corredor se cambia de aseguradora, puede llevarse al cliente | Hipótesis |

  **Para decidir:** identificar el ancla de cada cartera y diseñar el momento en que se suelta (el último pago del
  crédito, la salida del empleo, el fin del financiamiento) como un momento de elección, con una oferta de continuidad.
- **La amenaza principal es la selección.** En un ensayo aleatorizado, quienes se inscriben en programas de
  bienestar ya tenían menor gasto y mejores hábitos antes de empezar (Jones et al., 2019, F-854). La misma
  lógica aplica al cliente digital: quien adopta ya era distinto. 🔧 El mismo ensayo midió retención y no encontró
  efecto a 30 meses: el programa no hizo que los empleados se quedaran más (leído completo; F-854).
- 📚 **Tener más productos no blinda.** En una aseguradora europea, la primera cancelación predijo la fuga total
  del hogar. Los clientes con 3 o más pólizas fueron *más* propensos a irse del todo tras cancelar una
  (Brockett et al., 2008, F-852).

**Implicancia:** el benchmarking no puede probar la tesis "el cliente digital es más fiel". Solo se resuelve
con data propia: cohortes emparejadas o un despliegue escalonado. 📎 Los motivos de fuga que sí están documentados
son precio, no uso, promesa incumplida y fin de la relación que anclaba el seguro. Ninguno depende de cuántas veces
se entra al app.

### 3.3 Venta cruzada: la puerta de entrada a escala la tienen otros

- **Asociación, no efecto.** Los usuarios digitales tienen más productos en banca (F-848, F-849). 🌐 En Ping An,
  quienes usan su ecosistema de salud tienen 1,6 veces más contratos, según prensa (F-862).
- **Lo digital vende sobre todo al que ya es cliente.** Porto Seguro proyecta que 84% de su venta digital sea a
  clientes existentes. Sus 45 mil corredores siguen siendo el motor de la venta cruzada (F-865).
- **En LatAm, las apps de uso diario de otros venden seguros a escala:**
  - Nubank tiene 2 millones de pólizas, pero con baja penetración: 1,6% de su base en 2023 (F-863).
  - Mercado Pago tiene 11 millones de clientes con póliza (F-864).
  - Yape vende SOAT y lanzó un seguro de salud (F-869).
- 📎 **La puerta de entrada funciona en un caso de LatAm, pero por defecto y anclada a una relación frecuente.** En
  México, un microcrédito incluía cobertura de vida automática, y cerca de la mitad de los clientes compró módulos
  voluntarios (Poulton y Magnoni, 2013, F-896). En un ensayo aleatorizado con esos clientes, al quitar la
  cobertura automática la gente compró más por su cuenta, pero terminó menos protegida (Zimmerman et al., 2013,
  F-897). La relación era semanal (el pago del crédito) y no fue digital.
- 📎 **La puerta ajena cobra peaje.** En Perú, los microseguros llegan 97,8% por bancos y microfinancieras, con
  comisiones cercanas a 50% (Inga Falcón para el PNUD, 2025, F-902). En Chile, obligar a los bancos a licitar el
  seguro atado al crédito hipotecario bajó el desgravamen 62% (Coloma, 2019, F-904). La puerta por defecto funciona,
  pero sin competencia encarece el seguro.
- 📎 **La puerta por defecto genera reclamos si el consentimiento no es claro.** De 56.311 reclamos de seguros ante
  Indecopi en 2023, 38,4% fue por contratación o cargo indebido, y 33,7% se resolvió a favor del consumidor (F-902,
  con datos de Indecopi).
- 📎 **Tener la puerta no basta.** En LatAm, la billetera móvil pasó de 11% a 49% de la población en cinco años y se usa
  a diario, pero la tenencia de seguros privados no creció; Perú tiene la más baja de la región (13%) pese a su alto
  uso de billetera (Banco de Ideas Credicorp e Ipsos, 2026, F-906; encuesta probabilística, 5.031 casos en Perú; 🔵 B). El
  seguro no se suma solo a los hábitos diarios.
- 📎 **El momento de compra funciona como puerta.** 42% compraría su seguro de auto en el concesionario, frente a 32% en
  2018 (Accenture, 2023, F-905; intención declarada).
- 📎 **En Perú, la venta 100% digital tiene techo.** Solo 20% compraría un seguro de forma digital; el canal presencial
  domina (encuesta SBS-CAF 2022, vía F-903). En LatAm, 67% empieza a buscar seguro de vida en línea, pero compra con
  una persona (McKinsey, 2023, F-900).
- 🔧 **El SOAT se vende bien en digital, pero no hay evidencia de que abra la puerta a otra cosa.** Hay que separar dos
  preguntas:
  - *¿Se puede vender el SOAT en digital?* Sí. La venta digital de SOAT de Interseguro creció 66% en 2019 (F-867). Es
    digitalización de una venta que ya existía.
  - *¿Comprar el SOAT en digital lleva al cliente a algo más?* Es decir, a comprar otro seguro (vehicular, salud,
    hogar), a volver a usar el canal durante el año o a renovar más. No se encontró ninguna cifra que lo muestre. La
    memoria de Interseguro dice que mejoró la renovación, sin dar el número (F-867). Las razones para dudar: el SOAT es
    obligatorio, de precio regulado y de compra anual; se compra para cumplir, no por una relación con la marca.

  **Mi punto:** el éxito del SOAT digital prueba que el canal sirve para vender un producto simple. No prueba que ese
  cliente se convierta en un cliente digital recurrente o en un comprador de otros productos. Esa es la apuesta que
  habría que medir con datos propios: de los compradores digitales de SOAT, cuántos compran otro seguro en 12 meses,
  contra un grupo comparable que lo compró por otro canal.

**Implicancia:** si la apuesta es usar el SOAT como llave de entrada, hoy no hay evidencia que la respalde. Lo
que sí muestra la región es que la relación diaria con el cliente la puede tener una billetera o un banco. 📎 Esa
puerta vende, pero no retiene por sí sola, cobra peaje y exige consentimiento claro. La pregunta deja de ser "tener
una puerta" y pasa a ser con quién y en qué condiciones (pregunta 3).

### 3.4 Prevención: en auto cambia la conducta; en salud, el programa selecciona

- **Auto:** la retroalimentación telemática cambió la forma de manejar en un experimento de campo nacional
  (F-442). Midió conducta, no siniestros.
- **Brasil:** Justos reporta que su siniestralidad baja unos 6 puntos por año, y no renueva al 2% de clientes
  con peor nota de manejo. Atribuye la mejora a varios factores juntos: precio, suscripción y telemetría (F-870).
- **🌐 Root:** mejoró su ratio combinado a 98,2% por precio y selección de riesgo. La retención sigue siendo una
  incertidumbre declarada por la propia empresa (F-871).
- **Salud:** dos ensayos aleatorizados de programas de bienestar no encontraron efecto en gasto médico, salud
  clínica ni ausentismo (F-854, F-855).
- 🔧 **Por qué el ensayo de Illinois es la mejor lección de medición del informe** (Jones, Molitor y Reif, 2019, F-854;
  leído completo). Invitaron a 12.459 empleados; 4.834 se inscribieron; 3.300 fueron sorteados al programa y 1.534 a un
  grupo de control.
  - **Antes de empezar**, quienes participaron gastaban US$115 menos al mes en salud que quienes no participaron.
  - **Una comparación simple** entre participantes y no participantes, aun ajustando por muchas variables, decía que el
    programa bajaba el gasto en US$104 al mes. Es el tipo de cifra que publican las empresas.
  - **El sorteo** mostró que el programa no bajaba el gasto: la diferencia era de quién se inscribía, no de lo que el
    programa hacía.
  - **Lo único que cambió** fue que más gente se hizo chequeos (+4 puntos).
  - **Quienes no participaron** eran más a menudo del cuartil de salario más bajo: un incentivo ligado al programa
    traslada costo a los más pobres y enfermos.

  **Para un seguro:** cualquier cifra del tipo "los usuarios del app siniestran X% menos" o "renuevan X% más" tiene este
  problema hasta que se demuestre lo contrario.
  - Vitality reporta 4% menos siniestros, con una revisión actuarial que declara (F-353).
  - Alan duplicó sus usuarios activos diarios con gamificación y aún no mide el efecto en retención (F-859).

**Implicancia:** en salud, el valor más probable del engagement es atraer y retener buenos riesgos. Es un valor
legítimo, pero es **selección**, no prevención, y se mide distinto.

🔧 **Qué significa "selección" aquí, en simple.** Un programa de bienestar (retos de pasos, puntos por ir al gimnasio)
atrae sobre todo a quien ya se cuida. Si esas personas siniestran menos, no es porque el programa las cambió: ya eran
así. Para la aseguradora eso igual puede valer, porque atrae y retiene clientes de menor riesgo. Pero tiene dos costos:
no baja el gasto de quienes más gastan, y si el programa da descuentos, los pagan de hecho los que no participan, que
suelen ser de menor ingreso y peor salud (F-854). Por eso se mide distinto: no como "cuánto bajó la siniestralidad del
programa", sino como "qué tipo de cliente atrajo y retuvo".

### 3.4.1 🔧 Salud en el día a día: cuando la frecuencia es real

Hay una diferencia importante entre los programas de bienestar y el uso cotidiano de un seguro de salud. Un paciente
crónico, una familia con niños o alguien en tratamiento sí tiene necesidades frecuentes: consultar, renovar recetas,
tomar medicación, seguir un reembolso. Ahí la recurrencia no hay que inventarla. La evidencia sobre esos usos es
distinta, y más alentadora en algunos casos:

| Uso cotidiano | Qué dice la evidencia | Qué tan sólida | Teoría de valor |
|---|---|---|---|
| Recordatorios de medicación por mensaje de texto | En 16 ensayos aleatorizados con 2.742 pacientes crónicos, los recordatorios duplicaron la probabilidad de tomar bien la medicación (razón de momios 2,11); si la adherencia base es 50%, sube a cerca de 68% (Thakkar et al., 2016, F-933). Ojo: ensayos cortos y adherencia casi siempre autorreportada | 🟢 A, causal sobre la adherencia | Prevención en crónicos |
| Que la adherencia baje el costo | En 135.008 pacientes con enfermedades cardiovasculares crónicas, la buena adherencia subió el gasto en medicinas, pero bajó más el de hospitalización y emergencias (Roebuck et al., 2011, F-937). Estudio de una administradora de beneficios farmacéuticos, con datos observacionales | 🟢 A, asociación con método fuerte | Prevención en crónicos |
| Reposición de medicamentos a domicilio | En pacientes con diabetes de Kaiser, recibir la medicación por envío se asoció a 7 u 8 puntos más de adherencia (Duru et al., 2010, F-936). Observacional: quien elige el envío puede ser distinto | 🟢 A, asociación | Prevención en crónicos y costo de servir |
| Mensajería segura con el médico | En Kaiser, quienes usaban el portal con mensajes al médico tuvieron entre 6,7% y 9,7% menos consultas presenciales al año (Zhou et al., 2007, F-935). Cohorte observacional | 🟢 A, asociación | Costo de servir |
| Teleconsulta directa al paciente | Solo 12% de las teleconsultas reemplazó una consulta presencial; 88% fue uso nuevo. El gasto neto subió US$45 por usuario al año (Ashwood et al., 2017, F-934) | 🟢 A, observacional con datos de reclamos | Advierte contra la teoría de costo: la teleconsulta puede subir el gasto |
| Teleconsulta o atención por WhatsApp en LatAm | Solo se encontraron pilotos y experiencias descriptivas: videoconsultas por WhatsApp en un hospital de Brasil (factibilidad) y teledermatología entre médicos en Chile, con 41% de concordancia diagnóstica. No se encontró ningún ensayo aleatorizado con pacientes en la región. Hay advertencias de privacidad por ser una plataforma no clínica | Señal, sin evidencia de resultados | Por definir |
| Seguimiento de reembolsos y trámites | Lo claro migra y baja llamadas; lo ambiguo las sube (F-850) | 🟢 A, causal | Costo de servir |

**🔧 Perú: Pacífico Salud ya está probando esta estrategia.** Es el caso peruano más cercano a lo que discute esta
sección. Todo lo que sigue son declaraciones de la empresa en prensa o redes, sin resultados auditados:

- **Un seguro de salud dentro de Yape.** Lanzado en junio de 2025 con Yape: S/9,90, teleconsultas ilimitadas de
  medicina general y pediatría por videollamada desde el app de Yape para el titular y hasta tres familiares, receta,
  orientación telefónica 24 horas y S/500 si hay hospitalización. Apunta a personas sin seguro de los niveles C, D y E.
  Meta: 30.000 asegurados el primer año, sobre una base de 17 millones de usuarios de Yape (Gestión, 2025, F-940;
  también F-938).
- **Telemedicina propia (Tsana).** Teleconsultas, recetas válidas en cualquier farmacia y órdenes de análisis. Unos
  80.000 clientes en menos de un año, según el CEO de Pacífico Salud en julio de 2025 (F-942). En octubre de 2025, más de
  90.000 suscriptores y más de 1.000 atenciones al mes (F-941).
- **Orientación médica por WhatsApp.** El equipo de innovación de Pacífico Salud lanzó orientación médica 24/7 por
  WhatsApp con médicos reales, para resolver malestares cotidianos y decidir si algo requiere emergencia. También
  diseñó experiencias de gestión de citas y de búsqueda de medicamentos por ese canal. La responsable lo resume así:
  "diseñar una buena conversación también es diseñar un buen servicio" (publicación en LinkedIn de su líder de
  innovación y diseño, con menos de tres meses de operación al publicarse, F-939).
- **La lógica declarada por la empresa:** mucha gente se automedica o va directo a la farmacia, así que un médico a
  precio accesible, virtual o presencial, puede ser la puerta a quienes no tienen seguro privado. Su segmento de menor
  ticket empezó con seguros indemnizatorios, que superan el medio millón de asegurados (F-942).

**Lo que este caso sí y no dice.**

- *Sí dice* que un competidor peruano está apostando por la frecuencia real en salud (consultas cotidianas, recetas,
  citas, medicamentos) y por WhatsApp como canal, no solo por el app.
- *No dice* cuántos usan el servicio de forma recurrente, si renuevan o si pasan a productos de mayor valor. Las notas no
  reportan retención ni conversión.
- *Una cifra para mirar con cuidado.* Si los más de 90.000 suscriptores generan algo más de 1.000 atenciones al mes, el
  uso mensual rondaría 1% de los suscriptores (cálculo propio). Sería un uso bajo incluso para telemedicina barata, en
  línea con el "no lo usé". Pero las dos cifras pueden medir cosas distintas, y la de clientes no coincide entre notas
  (80.000 en julio, más de 90.000 suscriptores en octubre): no es una conclusión, es una pregunta para la gerencia.

**Qué cambia para la decisión.**

- **Separar dos públicos.** Para el asegurado sano, el engagement selecciona. Para el asegurado crónico, hay evidencia
  de que acompañar la medicación cambia la conducta, y una asociación fuerte con menor costo. Si la gerencia quiere
  recurrencia en salud, el lugar con más respaldo es el paciente crónico, no el reto de pasos.
- **La teleconsulta no ahorra por sí sola.** Atiende demanda que antes no se atendía. Puede valer por acceso y
  satisfacción, pero si la meta es costo, hay que medir sustitución: cuántas teleconsultas evitaron una consulta
  presencial o una emergencia.
- **El canal puede ser WhatsApp o el app; lo que tiene evidencia es la función** (recordar, reponer, responder), no la
  plataforma. Un piloto por WhatsApp debería medirse con grupo de control, porque en la región no hay estudios de
  resultados.

### 3.5 Confianza en el momento de verdad: el siniestro define la relación

- 🌐 **La experiencia digital del siniestro se asocia fuertemente a la fuga:** 52% en riesgo cuando es mala,
  contra 4% cuando es excelente (F-872).
- 🌐 **La confianza pesa más que el canal.** Bajar el tiempo de reparación de 22,3 a 19,3 días se asoció a +9
  puntos de satisfacción (F-874).
- 🌐 **Lo 100% digital falla en los reclamos complejos.** Más de 30% termina necesitando a una persona, y quien
  escala pierde 11 puntos de NPS (Bain, 2023, F-183).
- 🌐 **Satisfacción no es retención.** Tras un siniestro, la probabilidad de cambiarse de aseguradora sube 35%,
  aun entre clientes satisfechos (LexisNexis, 2023, F-890; dato de un proveedor).
- 📎 **LatAm: el valor está en la rapidez y la justicia del pago.** En un microseguro de vida en México, el pago
  llegó en promedio 9 días después de la muerte. Las familias lo usaron como garantía para pedir prestado sin
  interés a su red, y evitaron deuda cara o vender activos. Después del siniestro, todos los asegurados dijeron que
  fue buena decisión (Poulton y Magnoni, 2013, F-896). La muestra es pequeña (32 familias aseguradas y 36 no
  aseguradas) y no aleatoria.
- 📎 **Perú: el problema está en pagar, no en el canal.** Los microseguros devuelven en siniestros solo 16,7% de la
  prima (en LatAm ronda 40%); 18 productos no pagaron ningún siniestro en 2024; reclamar exige documentos que no
  existen en zonas remotas (F-902). De quienes desconfían de las aseguradoras, 47% dice que no cumplen lo ofrecido
  (F-903). En un ranking de experiencia de cliente de 2022, los seguros quedaron últimos de 20 industrias (F-900).
- 📎 **Perú: los reclamos bajan, pero los que escalan suben.** Los reclamos de seguros por cada 10.000 pólizas bajaron de
  16 (2018) a 8,9 (2024). Los que escalan a Indecopi o a la SBS por una respuesta insatisfactoria subieron de 61,6 a
  141 por cada mil reclamos (MEF, 2025, vía F-902). Lo que no se resuelve bien a la primera, escala.
- **Perú:** la fricción registrada está en la **resolución**, no en el canal. Indecopi recibió 8.248 reclamos de
  seguros entre 2019 y 2022. En 2025 sancionó demoras en indemnizaciones de SOAT y liquidaciones que no
  respetaban la póliza (F-883).
- 📎 **Perú: la norma deja abierto el tiempo del siniestro.** La aseguradora tiene 30 días desde la documentación
  completa para responder, pero puede pedir información adicional en los primeros 20 días sin un límite expreso de
  veces (Pérez-Llorca, 2026, F-907).
- 📎 **El lenguaje en el momento del siniestro mueve conducta y costo.** Una aseguradora alemana rediseñó el lenguaje de
  sus agentes con ciencias del comportamiento: la aceptación de su red de talleres superó 30% y, al escalarlo, la
  siniestralidad bajó 2% (caso citado por Beway, F-909; cifras no verificadas en el original).
- 📎 **🌐 21% de quienes consideran dejar su seguro de salud cita la dificultad para reclamar** (Graphite Digital,
  2025, F-895; intención declarada).

**Implicancia:** el siniestro se diseña como híbrido. Lo digital sirve para iniciarlo y seguir su estado; una
persona resuelve lo complejo. El indicador es el tiempo a resolución, no el uso del app. 📎 En Perú, esta es la
teoría con más respaldo, y su indicador natural incluye los reclamos que escalan.

### 3.6 📎 Transversal: lo digital convive con lo asistido

Esta sección es nueva. La sostienen papers que verificamos a partir de la revisión de literatura aportada.

🔧 **La idea en una frase:** cada canal es bueno para algo distinto, y por eso los canales no se reemplazan entre sí; se
reparten el trabajo. Hay cinco mecanismos que lo explican:

1. **Un canal sirve para buscar y otro para cerrar.** El canal digital es bueno para comparar precios a cualquier hora;
   la persona es buena para resolver dudas y dar seguridad antes de firmar. El cliente usa los dos en secuencia
   ("research shopping", Verhoef, Neslin y Vroomen, 2007, F-918).
2. **El canal digital retiene poco hasta la compra.** En internet el cliente abandona con un clic; en una conversación con
   una persona, el proceso tiende a terminar (F-918).
3. **Los canales se potencian entre sí.** Usar uno da información o confianza para usar el otro (F-918). Por eso un buen
   canal digital puede *aumentar* las conversaciones con asesores, como pasó en banca (F-847).
4. **El canal caro sobrevive porque resuelve algo que el barato no.** En vida en España, el banco es el canal más
   eficiente en costo, pero agentes y corredores siguen existiendo porque dan mejor producto, más servicio y defienden
   al cliente frente a la compañía (Rubio-Misas, 2022, F-923).
5. **Agregar el canal que todos agregan no da ventaja.** Si todas las aseguradoras abren el mismo canal, todas cargan el
   costo y ninguna gana posición (Neslin et al., 2006, F-917, según la revisión aportada); los incumbentes tienden a
   usar lo digital para defenderse, no para crear productos nuevos (Holland y Kavuri, 2024, F-922).

**Qué significa para las decisiones:**

- **Diseñar el traspaso entre canales,** no solo cada canal. Cuando un cliente pasa del app al asesor, el asesor debe ver
  lo que el cliente ya hizo. Repetir información es la señal de que el recorrido digital terminó antes que la
  necesidad.
- **Medir el recorrido, no el canal.** Un indicador por canal premia al canal; un indicador por necesidad resuelta
  premia al cliente.
- **Cuidar el costo interno.** Si los asesores sienten que el canal digital les quita ventas, se comprometen menos, sobre
  todo cuando el mercado ofrece pocas oportunidades (F-924). El diseño de comisiones importa tanto como el diseño de
  pantallas.

- 📚 **La gente busca en un canal y compra en otro.** Se llama "research shopping": un canal sirve para buscar, otro
  para cerrar, y el canal digital retiene poco al cliente hasta la compra (Verhoef, Neslin y Vroomen, 2007, F-918).
  Calza con lo que se ve en la región: 67% busca seguro de vida en línea y compra con una persona (F-900).
- 📚 🌐 **Ofrecer el canal no traslada la tarea.** En Francia, entre 75% y 90% de las contrataciones directas termina por
  teléfono aunque exista la opción de terminar en línea (Dalla Pozza y Texier, 2014, F-921; cifra tomada de la revisión
  aportada, no verificada en el texto).
- 🌐 **Los canales caros sobreviven por lo que resuelven.** En vida en España, el canal bancario es más eficiente en
  costos, pero agentes y corredores compensan con calidad de producto, más servicio y mejor manejo del conflicto de
  intereses. No hay un sistema de distribución óptimo único (Rubio-Misas, 2022, F-923).
- 🌐 **Digitalizar lo que ya se vende es defensa.** Los incumbentes usan la tecnología para defender su posición; los
  nuevos entrantes, para crear productos (Holland y Kavuri, 2024, F-922; siete casos). 📚 Agregar un canal que todos
  agregan funciona como un dilema del prisionero: todos cargan el costo y nadie gana posición (Neslin et al., 2006,
  F-917, según la revisión aportada).
- 📚 **El MAU es una métrica de gerente de canal.** Muchas organizaciones siguen organizadas por gerentes que optimizan su
  propio canal, y esa es la barrera a la integración (Verhoef, Kannan e Inman, 2015, F-919, según la revisión aportada).
  Inferencia nuestra: un indicador de uso del app premia al canal, no al cliente que resolvió.
- 📚 **Digitizar, digitalizar y transformar no son lo mismo.** Pasar un certificado a PDF es digitizar. Automatizar la
  venta del SOAT es digitalizar un proceso que ya existía. Cambiar cómo se crea valor es transformar (Verhoef et al.,
  2021, F-920). La pregunta "para qué digitalizamos" exige decir en cuál de las tres se está.
- 📚 **Mover tareas al canal digital tiene un costo interno.** Los agentes de seguros que sienten que internet les
  quita ventas se comprometen menos, pero solo cuando el mercado ofrece pocas oportunidades (Sharma y Gassenheimer,
  2009, F-924; 511 agentes).

**Implicancia:** la pregunta útil no es cuánto se digitaliza, sino qué tarea va a qué canal y con qué indicador. Eso
es la pregunta 2. "Salud 100% digital" o "todo al app" pueden ser metas equivocadas, no solo metas difíciles.

---

### 3.8 🔧 Comoditización, agentes de IA y alcance: lo que agrega la visión de un líder del sector

**Qué es esta sección.** Una entrevista al CEO de Credicorp, en notas tomadas por la usuaria (F-932). Es opinión de un
ejecutivo con interés en el tema: rigor 🔴 E. Se usa porque plantea tres riesgos que la evidencia del informe no había
nombrado, y se contrasta cada idea con lo que ya sabemos.

| Idea de la entrevista | Qué dice la evidencia del informe | Qué agrega para decidir |
|---|---|---|
| "Lo digital es un medio para mejorar algo de los clientes, no un fin" | Coincide con la conclusión central: la actividad crea valor cuando resuelve algo (§1) | Refuerza que la meta no puede ser el uso del canal |
| Yape se aprobó porque prometía dos cosas medibles: mejor experiencia y menor costo de servir. Su competencia no era otro banco, sino el efectivo | Son las teorías 1 y 5 de este informe. Yape vende SOAT y salud (F-869) | **Definir contra qué conducta compite el canal.** Para Yape fue el efectivo. Para un seguro podría ser la llamada al call center, el "guardadito", la red familiar o la clínica (§4) |
| Los productos son commodities; la diferencia está en la propuesta de valor y la experiencia | Si todos agregan el mismo canal, nadie gana posición (F-917); los incumbentes digitalizan para defenderse (F-922) | Digitalizar el trámite básico es condición para competir, no ventaja. La ventaja está en resolver mejor el momento de verdad |
| Con agentes de IA que comparan por el cliente, "ya no importa quién tenga el mejor app": la relación emocional puede desaparecer | La gente ya acepta que una IA cotice (46%), menos que presente un siniestro (22%) (F-916); revelar que es un bot baja la compra (F-912) | **Inferencia nuestra:** si parte de la renovación se sostiene en inercia (F-889), un agente que compara y cambia por el cliente la elimina. Las carteras retenidas por inercia son las más expuestas; las retenidas por buen servicio en el siniestro, las menos |
| Agencias, personas e IA van a convivir; la hipoteca necesita una persona, el celular se compra en línea | Coincide con la convivencia de canales por función (§3.6): se busca en línea y se cierra con una persona (F-918) | Asignar canal según el peso de la decisión y la carga emocional (tabla de §3.1) |
| La confianza se construye de a poco y se destruye rápido; hay que equilibrar "pro-agente" y "anti-agente" | Una mala experiencia del siniestro multiplica el riesgo de fuga (F-872); la aversión a la IA baja si la persona puede corregir el resultado (F-915) | Introducir IA con confirmación humana en los pasos sensibles (hipótesis 5 de §4) |
| La penetración financiera es baja, ligada a informalidad y nivel socioeconómico; llegar a esos clientes es caro | Perú tiene la tenencia de seguros privados más baja de la región, 13% (F-906); los microseguros llegan 97,8% por bancos, con comisiones cercanas a 50% (F-902); el mercado se orienta a segmentos de mayor ingreso, alcanzables por canales digitales (F-902) | **Posible sexta forma de valor: alcance.** Usar lo digital para llegar con costo bajo a quien hoy no es rentable atender. 🔧 En Perú, Pacífico Salud lo está intentando: seguro de salud de S/9,90 en Yape, telemedicina propia con unos 80.000 a 90.000 suscriptores y orientación médica por WhatsApp (F-940, F-941, F-942, F-939). Son declaraciones de la empresa, sin datos de uso recurrente, retención ni conversión. Aún no hay evidencia de que funcione como negocio. Es materia de la pregunta 3 |
| Gestionar las apuestas como un portafolio de inversiones: una base segura y apuestas pequeñas de alta incertidumbre para "tocar el agua" | No es un hallazgo; es un criterio de gestión | Ordenar las decisiones de §5.1 como portafolio (ver decisión 8) |

**Lo que no se debe concluir.** La entrevista no prueba que los agentes de IA vayan a comoditizar los seguros ni cuándo.
Es una señal para el ejercicio de foresight (Anexo B), no una tendencia medida.

## 4. Lectura conductual

La pregunta conductual no es "cómo hacemos que entren más". Es **qué conducta tiene que ocurrir para que haya
valor, y qué la frena**. Esta lectura agrega distinciones que el análisis de negocio no ve:

1. **Lealtad o inercia.** 🔧 Dicho simple: un cliente que se queda no es necesariamente un cliente leal.
   - **Lealtad** es quedarse *por elección*: el cliente sabe que tiene alternativas, las consideró y prefirió quedarse.
   - **Inercia** es quedarse *porque cambiarse cuesta*: no revisó, la renovación fue automática, comparar da pereza,
     teme perder coberturas o no sabe cómo irse.

   En seguros, la inercia es grande: en un seguro de salud en EE.UU., la gente se quedó en planes que le costaban más
   solo por no cambiarse (Handel, 2013, F-889). En el Reino Unido, las aseguradoras cobraban más a quien renovaba sin
   mirar, y ponían fricción para cancelar, como exigir una llamada; el regulador lo prohibió (FCA, 2025, F-886).

   **Por qué importa para la meta digital:** un buen canal digital hace más fácil comparar, entender y cancelar. Si la
   renovación actual se sostiene en inercia, un mejor canal puede *bajar* la renovación en el corto plazo, y una meta de
   "fidelidad" que no distinga ambas cosas castigaría el buen diseño. **Señales para distinguirlas:** renovación
   automática sin ninguna interacción (probable inercia); renovación después de una subida de prima sin reclamo
   (inercia o lealtad, hay que preguntar); cliente que cotizó con otros y se quedó (lealtad); cliente que cambió
   coberturas al renovar (elección activa).
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
5. 📎 **La cobertura por defecto pesa más que el mensaje.** En el ensayo de microseguro en México, quitar la
   cobertura automática redujo la protección total, y los mensajes emocionales o factuales no cambiaron la compra
   (Zimmerman et al., 2013, F-897). Lo que viene incluido define cuánto queda protegido. Pero el defecto también se
   presta para cobrar de más, y ahí interviene el regulador: en Chile, licitar el seguro atado al crédito bajó el
   precio del desgravamen 62% (F-904). 📎 Y el defecto no crea lealtad: cuando termina el crédito, 12% mantiene el
   seguro de terremoto (F-902).
6. 📎 **La seguridad pesa en el canal.** 35% de la región teme hacer transacciones digitales (F-906). En México, la
   desconfianza en la banca móvil aparece en casi todos los perfiles estudiados (F-898).

### 4.1 🔧 Cómo usar la lectura conductual para decidir

La lectura conductual sirve para tres cosas concretas: evitar indicadores que premian lo equivocado, elegir dónde
invertir y anticipar efectos no buscados. Cada fila es una regla de decisión.

| Si la gerencia está por decidir… | La lectura conductual dice… | Entonces… |
|---|---|---|
| Medir la fidelidad con la tasa de renovación | Parte de la renovación es inercia, no elección (F-889, 🟢 A; F-886, 🔵 B) | Separar renovación activa de pasiva antes de fijar metas; no premiar la fricción para irse |
| Invertir en funciones para que el cliente "entre más" al app | Con una o dos necesidades al año no se forma un hábito en un app propia (el hábito necesita frecuencia y contexto estable, F-888, 🟢 A; frecuencia del seguro, F-876, 🟠 D) | Llevar el servicio a donde ya hay hábito (WhatsApp, billetera, banca, la clínica) en vez de pelear por la frecuencia |
| Repartir la inversión del siniestro | El cliente recuerda el peor momento y el final (regla pico-final; estado de replicación en el registro de fenómenos psicológicos del proyecto); el siniestro pesa en la fuga (F-872, F-890) | Invertir primero en el cierre: pago, explicación del resultado y siguiente paso |
| Lanzar campañas para atraer clientes de otras aseguradoras | Quien llega cambiándose siniestró el doble con el mismo historial (F-891, 🔵 B, nota de prensa de la revista); reducir la inercia empeoró la selección adversa (F-889, 🟢 A) | Revisar el efecto actuarial de toda campaña de adquisición o de cambio |
| Incluir coberturas por defecto en una puerta de entrada | El defecto es la palanca más fuerte (meta-análisis, d=0,68, F-913, 🟢 A; ensayo en México, F-897, 🔵 B), pero sin consentimiento claro genera reclamos: 38,4% de los reclamos de seguros en Indecopi (F-902, 🔵 B) | Usar defectos con aviso claro y salida fácil; medir reclamos por cargo indebido |
| Forzar el uso del app | 35% de la región teme hacer transacciones digitales (F-906, 🔵 B); solo 20% en Perú compraría un seguro de forma digital (F-903, 🔵 B) | Ofrecer el canal digital como opción, no como obligación; mantener una vía segura y conocida |
| Lanzar un programa de puntos o niveles | Los programas atraen a quien ya está sano (F-854, 🟢 A); que un beneficio que baja se vive como pérdida es aversión a la pérdida, una inferencia aplicada a este diseño | Medirlo como selección y no como prevención; probarlo con un grupo de control antes de escalar |

**Hipótesis conductuales para el trabajo de campo.** El estudio mexicano de inclusión financiera y las voces de
practitioners no son evidencia, pero abren mecanismos que coinciden con otras fuentes. Valen como hipótesis:

1. 📎 **La red familiar y el "guardadito" compiten con el seguro.** Ante un golpe, la gente recurre primero a familia,
   ahorros y recorte de gastos. Es la hipótesis más respaldada: coinciden cinco fuentes (F-896, F-898, F-903, F-906,
   F-908), y en Perú la red pesa más que en cualquier otro país de la región (F-906). Implica diseñar el seguro como
   complemento de la red, no como su reemplazo.
2. 📎 **El cobro debe seguir el ritmo del ingreso.** Quien cobra por semana tiene menos seguros (F-898); el microseguro
   mexicano se pagaba cada semana junto al crédito (F-896).
3. 📎 **El dependiente o el adulto mayor poco digital se alcanza a través de un familiar** (F-898). Se conecta con la
   baja digitalización de dependientes del diagnóstico interno.
4. 📎 **La fricción pequeña acumulada empuja a irse sin una decisión consciente**, y la confianza se gana cuando algo
   falla (F-899). Coincide con la fuga tras siniestro (F-890, F-872).
5. 📎 **Delegar en una IA exige confirmar en cada paso sensible** para sentir control (F-899). **Esta hipótesis ya tiene
   respaldo experimental:** revelar que era un bot antes de conversar bajó la compra más de 79,7% (Luo et al., 2019,
   F-912); la gente resiste la IA porque cree que no considera lo que la hace única (Longoni et al., 2019, F-914); la
   aversión baja si puede modificar el resultado (Dietvorst et al., 2018, F-915); y la comodidad cae de cotizar (46%)
   a presentar un siniestro por mí (22%) (F-916). Ojo: ocultar al bot sube la venta, pero choca con la transparencia
   que exige la regulación de IA (F-907).
6. 📎 **El momento de vida pesa más que la edad**, y conviene ofrecer cuando el riesgo se siente cerca (F-899, F-909),
   como al comprar un auto (F-905).
7. 📎 **La confianza se construye usando el producto** (F-898); completar la primera tarea genera confianza (F-895).

Sobre los defaults: un meta-análisis de 58 estudios halló un efecto considerable (d=0,68) de las opciones por
defecto (Jachimowicz et al., 2019, F-913), mientras que el efecto promedio de los nudges en general desaparece al
corregir el sesgo de publicación (Maier et al., 2022, F-17).

**Propuesta para las tres definiciones que hoy no existen:**

- **Fidelidad:** elegir quedarse teniendo alternativas, a diferencia de renovar por inercia.
- **Cliente digitalmente sano:** resuelve lo que necesita cuando lo necesita, sin fricción de más. No se mide
  por cuántas veces entra. 📎 Puede resolver por medio de su corredor o de otro canal y seguir siendo sano.
- **Cliente de alto valor:** suma el riesgo que trae, no solo la prima que paga.

🔧 **Las tres definiciones, aterrizadas.** Los umbrales son puntos de partida para discutir con los ramos, no estándares.

| Definición | Cómo se calcula | Datos que necesita | Ejemplo | Sustento |
|---|---|---|---|---|
| **Fidelidad activa** | Porcentaje de renovaciones en las que hubo un momento de elección: el cliente abrió el aviso de vencimiento, comparó o cotizó, cambió coberturas o confirmó la renovación. El resto se cuenta como **renovación pasiva** | Tipo de renovación (automática o activa); interacciones en los 60 días previos al vencimiento; cambios de prima y de coberturas; cotizaciones | Cliente con débito automático que no abrió ningún aviso y renovó: pasiva. Cliente que recibió una prima más alta, comparó y renovó: activa | La inercia es grande en seguros (F-889, 🟢 A) y el regulador británico separó a quien renueva sin mirar (F-886, 🔵 B) |
| **Cliente digitalmente sano** | Porcentaje de las necesidades del cliente en 12 meses que se resolvieron dentro del plazo prometido, al primer intento y sin recontacto en 7 días, por cualquier canal (incluido su corredor) | Registro de casos o necesidades por cliente, con canal, fechas de inicio y cierre, y recontactos | Cliente con dos reembolsos pagados a tiempo sin llamar y una constancia descargada: sano, aunque solo haya entrado tres veces al app. Cliente que entró 40 veces y llamó seis por el mismo reembolso: no sano | Usar más el portal puede subir las llamadas (F-850, 🟢 A); en banca, el adoptante digital usó más los canales caros (F-847, F-931) |
| **Cliente de alto valor** | Margen esperado del cliente: prima, menos siniestralidad esperada, menos costo de servir, menos comisión; más el potencial de otros productos y menos el riesgo de fuga | Prima y siniestralidad por póliza; costo de servir por canal (sale de la teoría 1); comisión; productos; renovaciones | Dos clientes con la misma prima: el que siniestra poco, resuelve solo y renueva activamente vale más que el que siniestra mucho y genera muchos contactos | El riesgo que trae el cliente cambia el valor de la cartera (F-891, F-889); el costo de servir varía por canal (F-847) |

**Herramienta para el ejercicio con los ramos:** una auditoría de fricciones por recorrido (Sunstein, 2022,
F-894). Usa la conversión de cada flujo y separa la fricción excesiva de la que protege al cliente.

---

## 5. Implicancias para las hipótesis del diagnóstico

### 5.1 🔧 Las decisiones que tiene que tomar la gerencia

Cada fila es una decisión. Se indica qué dice la evidencia, qué dato propio la cierra y cómo conseguirlo. El orden
sugiere una secuencia: primero el indicador, luego dónde invertir.

| # | Decisión | Opciones | Qué dice la evidencia | Qué dato propio la cierra | Cómo y en cuánto tiempo |
|---|---|---|---|---|---|
| 1 | Qué indicador acompaña o reemplaza al MAU | MAU; contactos por necesidad resuelta; renovación activa; tiempo a resolución del siniestro | El MAU no tiene relación probada con valor; en dos teorías el buen resultado baja la actividad | Contactos por necesidad y tiempo a resolución por flujo | Medición con datos que ya existen en call center y siniestros; semanas |
| 2 | Qué flujos mover primero a digital | Todos; los más usados; los de información clara | Lo claro migra y baja llamadas; lo ambiguo las sube (F-850) | Motivos de contacto clasificados en claros y ambiguos, y su volumen | Análisis de motivos de contacto del call center; semanas |
| 3 | Qué hacer con el siniestro | Todo digital; todo humano; híbrido por tipo de siniestro | Híbrido: digital para iniciar y seguir; persona para lo complejo (F-183, F-874) | Tiempo a resolución y reclamos por tipo de siniestro y canal | Corte de datos por ramo; piloto de vía rápida en siniestros simples |
| 4 | Cómo usar el app para retener | Invertir para "enganchar"; invertir en cumplir; no invertir | No hay prueba causal en seguros; los motivos de fuga no dependen del canal | Efecto del app en renovación | Despliegue escalonado de una función de renovación; 12 meses (Anexo C) |
| 5 | Puerta de entrada | Producto propio (SOAT); alianza con banco, billetera o empleador | La puerta ajena vende pero no retiene sin ancla, cobra peaje y genera reclamos sin consentimiento claro | Renovación de clientes por canal de origen; reclamos por canal | Datos de cartera por canal de venta; pregunta 3 |
| 6 | Programas de bienestar o puntos | Lanzar; no lanzar; piloto controlado | Seleccionan más de lo que previenen (F-854, F-855) | Siniestralidad de inscritos antes y después, contra un control | Piloto con sorteo o despliegue escalonado; 12 a 24 meses |
| 7 | Meta de "salud 100% digital" | Mantenerla; reemplazarla por una meta por tarea | Los canales conviven por función (§3.6) | Qué tareas de salud se resuelven bien en digital | Mapa de tareas por canal con el ramo salud (pregunta 2) |
| 8 | Cómo repartir la inversión digital | Apostar todo a una teoría; repartir como portafolio | Solo la teoría 1 tiene evidencia causal; la 5 es la más respaldada en Perú; el resto no está probado en seguros (§2) | El resultado de los pilotos de las decisiones 4 y 6 | Propuesta: una base en lo probado (flujos claros y siniestro híbrido), apuestas medianas con medición (renovación activa, puerta aliada) y apuestas pequeñas para aprender (agentes de IA, finanzas abiertas), cada una con un criterio para escalar o cerrar. Criterio tomado de la entrevista al CEO de Credicorp (F-932, 🔴 E), no de evidencia |

### 5.2 Las hipótesis del diagnóstico

| Hipótesis | Qué dice el benchmarking | Cómo se cierra |
|---|---|---|
| El cliente digital es más fiel | No confirmada para seguros. Las analogías dicen que puede ser cierta; la selección dice que puede ser falsa. 📎 Los motivos de fuga documentados (precio, no uso, promesa incumplida, fin del ancla) no dependen del canal | 🔧 Con datos propios, de dos formas (Anexo C). **Cohortes emparejadas:** comparar la renovación de clientes que adoptaron el app con la de clientes que no lo hicieron pero eran iguales antes (mismo producto, antigüedad, prima, canal de venta, siniestros y renovaciones previas). **Despliegue escalonado:** lanzar una función por oleadas a grupos elegidos al azar y comparar los que la recibieron primero con los que aún no |
| Hace falta una llave de entrada para cada cartera | Sin evidencia de que un producto propio de bajo ticket y uso anual abra la puerta. Funciona cuando la cobertura viene por defecto y anclada a una relación frecuente (microcrédito semanal en México, F-896 y F-897) o a una app ajena de uso diario. 📎 Pero esa puerta no retiene sin el ancla (F-902), no basta por sí sola (F-906) y genera reclamos si el consentimiento no es claro (F-902) | Decidir si se compite por esa puerta o se alía con quien la tiene, y en qué condiciones (pregunta 3) |
| Un canal digital ahorra costo por sí mismo | 📎 No por sí mismo: lo ambiguo vuelve al teléfono (F-850) y ofrecer el canal no traslada la tarea (F-921) | Medir resolutividad por canal y flujo |
| La actividad la determina el producto, no el canal | Consistente con la baja frecuencia estructural del seguro y con que la recurrencia de los referentes venga de servicios cercanos | 🔧 Con los datos del Anexo D: frecuencia natural de necesidad por producto y motivos de contacto por canal |
| La gente casi no interactúa con la propuesta de valor | Consistente con lo anterior | 🔧 Con los datos del Anexo D: tasa de uso de cada beneficio, tiempo hasta el primer uso y relación entre uso y renovación |
| El siniestro debería resolverse en digital | La evidencia apunta a un modelo híbrido: digital para iniciar y seguir, persona para lo complejo. 📎 En Perú, lo que falla es resolver y pagar, y lo mal resuelto escala (F-902, F-903) | Rol del canal por momento (pregunta 2) |
| 📎 Implícita en la meta: más uso del app es mejor | No: en dos teorías, el buen resultado baja la actividad; y en el segmento que delega en su corredor, poca actividad propia no significa poco valor | Reemplazar o acompañar el MAU con el indicador de la teoría elegida |
| 📎 Implícita: el objetivo es llevar todo (o salud) a 100% digital | La evidencia dice que los canales conviven por función: la gente busca en línea y cierra con una persona (F-918); en Francia, 75% a 90% termina por teléfono aun pudiendo hacerlo en línea (F-921); los canales caros sobreviven por lo que resuelven (F-923). Detalle en §3.6 | Definir qué tarea va a qué canal con la tabla de §3.1 (pregunta 2) |

---

## 6. Lo que no se pudo responder

- **No hay evidencia causal de Perú ni de LatAm en ninguna de las cinco teorías.** Lo regional son datos de
  empresas, encuestas, registros de reclamos y un caso mexicano. 📎 El único ensayo aleatorizado regional (México) es
  sobre la cobertura por defecto, no sobre lo digital.
- **No hay ningún estudio causal sobre retención digital en seguros.** El ensayo más cercano, sobre
  recordatorios y renovación automática en un seguro de salud de Ghana, está en curso y sin resultados (F-887).
- **Varios estudios académicos son anteriores a 2021.** Son canónicos y sus contextos son EE.UU. y Europa.
- 📎 **Cómo se leyó cada fuente.** Lo encontrado en la web (papers, reportes anuales, prensa) se leyó por su resumen,
  la página del editor o la cobertura de prensa; no se abrió el texto completo de la mayoría, y tres dominios
  estuvieron bloqueados desde el entorno de trabajo (`arxiv.org`, `pacifico.com.pe` y `quartr.com`). Los documentos
  aportados se leyeron completos, con tres excepciones: del diagnóstico del PNUD no se leyó el capítulo de riesgo de
  desastres (fuera de alcance); del boletín de Pérez-Llorca, solo las secciones de IA y de Perú (el resto son otros
  países); y del documento de Coloma, solo el resumen ejecutivo (se leerá completo para la pregunta 3). Cada ficha del
  registro de fuentes indica cómo se leyó.
- 📎 **Dos fuentes piden cuidado.** El artículo de la Universidad de Lima atribuye a estudios clásicos cifras que no
  parecen corresponderles; no se usan (F-908). La cifra francesa de contratación por teléfono viene de una revisión
  y no se verificó en el texto (F-921).
- **La pista social es la más débil.** No se encontró conversación pública sobre apps de aseguradoras peruanas.
- **Varias cifras de Porto Seguro son metas, no resultados.** Las de Ping An que comparan usuarios con no
  usuarios vienen de prensa.

**Pendientes para la siguiente versión:**

- 📎 abrir el texto completo de los cinco papers que más pesan en las conclusiones: Kumar y Telang (F-850), Campbell y
  Frei (F-847), Jones et al. (F-854), Handel (F-889) y Dalla Pozza y Texier (F-921);
- el resto del blog de Beway: el dominio `blog.beway.com` está bloqueado desde el entorno de trabajo (se leyó un
  artículo aportado por la usuaria);
- las memorias anuales completas de Perú y LatAm;
- la búsqueda de estudios causales de retención en seguros;
- 📎 para la pregunta 3: la cifra de McKinsey sobre el peso de bancaseguros en LatAm, que no se pudo verificar.

---

## 7. 📎 Cómo cambió el informe con los documentos aportados

### 7.1 Por teoría de valor

La versión 1 se armó solo con búsqueda web. Esta tabla compara aquella lectura con la actual.

| Teoría | Versión 1 (solo búsqueda web) | Versión 6 (con los documentos) | Qué lo movió | ¿Cambia lo que se recomienda? |
|---|---|---|---|---|
| 1. Costo de servir | Causal en ambas direcciones (EE.UU.); en Perú, solo una cifra de empresa | Igual nivel. Se suma que ofrecer el canal no traslada la tarea y que los canales caros sobreviven por lo que resuelven | Dalla Pozza y Texier (F-921), Rubio-Misas (F-923) | **Sí, matiza.** La meta pasa de "mover a digital" a "resolver cada tarea en el canal que mejor la resuelve" |
| 2. Retención | No demostrada en seguros; plausible por analogía con banca y salud | Sigue sin demostrarse. Ahora se conocen los motivos de fuga, y ninguno depende del canal | PNUD (F-902), Treo (F-898), Capgemini (F-901), Graphite (F-895) | **Sí.** La fidelidad se juega en valor percibido y en cumplir, no en uso; la meta debe separar renovación pasiva de elección |
| 3. Venta cruzada | Asociación; las puertas ajenas venden a escala | Asociación. La puerta ajena vende, pero no basta, cobra peaje, genera reclamos y no retiene sin el ancla | Credicorp (F-906), PNUD (F-902), Coloma (F-904), MILK México (F-896, F-897) | **Sí.** La pregunta pasa de "tener una puerta" a "con quién y en qué condiciones" (pregunta 3) |
| 4. Prevención | En auto cambia la conducta; en salud no baja el gasto | Igual. | Sin cambios de fondo en esta copia | No |
| 5. Confianza en el momento de verdad | Asociación con encuestas de EE.UU. | Asociación, pero la más consistente y con evidencia peruana de varios tipos | PNUD (F-902), SBS-CAF (F-903), Pérez-Llorca (F-907), MILK México (F-896) | **Sí.** Pasa a ser la candidata con más respaldo para Perú |
| Transversal (nueva) | No existía | Los canales conviven por función; digitalizar lo existente es defensa | Papers F-917 a F-924 | **Sí.** Abre la pregunta 2 con una hipótesis: "todo digital" puede ser la meta equivocada |

### 7.2 Por sección

- **§1 Conclusión:** la tesis central no cambió. Se agregaron cuatro matices y una inferencia rotulada sobre las dos
  teorías con más respaldo en Perú.
- **§2 Menú:** nueva columna con el respaldo en Perú y LatAm; la teoría 5 se marca como la más consistente.
- **§3 Hallazgos:** cada teoría suma evidencia peruana o latinoamericana; se agrega la §3.6 sobre convivencia de
  canales.
- **§4 Lectura conductual:** se agregan el defecto que no crea lealtad, el peso de la seguridad en el canal.
- **§5 Implicancias:** se actualizan cuatro hipótesis y se agregan dos que la meta de MAU da por supuestas.
- **§6:** se corrige "todo se leyó por resumen", que era inexacto, y se detalla cómo se leyó cada fuente.
- 🔧 **Versión 7, para aterrizar:** §2.1 (qué significa cada teoría, con ejemplos y cómo se mide); §3.1 (detalle del
  caso bancario y tabla de qué tarea va a qué canal); §3.2 (qué es un ancla); §3.4 (el ensayo de bienestar leído
  completo); §3.6 (los cinco mecanismos de convivencia de canales); §4 (lealtad e inercia explicadas, reglas de
  decisión y definiciones operativas); §5.1 (decisiones de la gerencia); Anexos C y D.
- 🔧 **Versión 7.1:** cada ejemplo tiene ahora una línea de sustento con su fuente y su rigor; nueva §3.8 con la
  entrevista al CEO de Credicorp (comoditización, agentes de IA, alcance y portafolio de apuestas); decisión 8 en §5.1.
- 🔧 **Versión 7.2:** aclaración del SOAT como puerta de entrada (§3.3); qué significa "selección" en salud y nueva
  §3.4.1 sobre el uso cotidiano del seguro de salud (medicación, reposición, mensajería, teleconsulta, WhatsApp).
- 🔧 **Versión 7.3:** el caso de Pacífico Salud (seguro en Yape, telemedicina propia y orientación médica por WhatsApp)
  en §3.4.1, §3.8 y Anexos A y B; corrige que no se había encontrado información pública sobre WhatsApp.

### 7.3 Veredicto por documento

| Documento | ¿Robustece lo que ya teníamos? |
|---|---|
| Estudio de India sobre seguros de vida (F-856) | **No.** Leído completo, confirma que es evidencia débil: mide actitud, no renovación, con una muestra sesgada a usuarios digitales de ingreso alto |
| Whitepaper sobre apps de seguros de salud (F-895). ⚠️ El archivo venía rotulado como J.D. Power, pero es de Graphite Digital, una agencia | **Parcial.** Suma el "no lo usé" como razón de fuga y confirma el siniestro y la sobrecarga de información como puntos críticos. Intención declarada, con conflicto de interés |
| Microseguro de vida en México (F-896) y su ensayo aleatorizado (F-897) | **Sí.** Da evidencia de LatAm para la confianza en el momento de verdad y para la cobertura por defecto. Matiza la puerta de entrada: funciona por defecto y anclada a una relación frecuente |
| Estudio de inclusión financiera en México (F-898) | **No para esta pregunta.** Sí aporta que parte de la fuga es estructural (cambio de trabajo), que los adultos mayores se alcanzan mejor por intermediarios y que la desconfianza en la banca móvil es casi general |
| Luo 2019, Jachimowicz 2019, Longoni 2019, Dietvorst 2018 (F-912 a F-915) | **Sí.** Respaldo experimental para la hipótesis de control al delegar en IA y para la fuerza de los defaults |
| Índice de Inclusión Financiera de Credicorp 2026 (F-906) | **Sí, y matiza la puerta ajena.** La billetera se volvió diaria, pero los seguros no crecieron; Perú tiene la tenencia más baja (13%). Leído completo: su método es una encuesta probabilística con 5.031 casos en Perú |
| Estudio global de consumidores de Accenture 2023 (F-905) | **Parcial.** El concesionario como puerta (42%) y la rapidez del siniestro como valor. Intención declarada |
| Artículo de la Universidad de Lima (F-908) | **Parcial y con cuidado.** Suma una fuente peruana a la hipótesis de la red familiar. Sin diseño causal; varias cifras que atribuye a estudios clásicos no se usan |
| Boletín legal de Pérez-Llorca 3T 2026 (F-907) | **Para señales y la pregunta 2:** reglamento peruano de IA y plazos del siniestro con una puerta abierta |
| Artículo de Beway sobre seguro marítimo (F-909) | **Parcial.** El lenguaje conductual en el siniestro mueve conducta y costo (caso de segunda mano) |
| Diagnóstico de microseguros en el Perú para el PNUD (F-902) y encuesta SBS-CAF 2022 (F-903) | **Sí, el más fuerte para Perú.** Solo 20% compraría digital; la puerta ajena cobra comisiones cercanas a 50%; los siniestros devuelven poco valor; los reclamos que escalan subieron; 38,4% de los reclamos ante Indecopi fue por cargo indebido; solo 12% mantiene el seguro de terremoto al terminar el crédito |
| Reporte de McKinsey sobre seguros en LatAm (F-900) | **Parcial.** Búsqueda en línea y compra con persona; seguros últimos en experiencia en Perú. Casos sin cifras verificables |
| 🔧 Texto completo del ensayo de bienestar de Illinois (F-854) y resumen editorial de Campbell y Frei (F-931) | **Sí, y aclara el método.** El ensayo muestra con cifras cómo una comparación simple confunde selección con efecto, y que no hubo efecto en retención. El resumen confirma el detalle del caso bancario: sube el uso de canales caros y baja la utilidad por cliente el primer año, pero sube la retención |
| Licitación de seguros hipotecarios en Chile (F-904) | **Sí, para la puerta por defecto** (y para la pregunta 3): sin competencia, el seguro atado cobra de más |
| Informe mundial de seguros generales de Capgemini (F-901) | **Débil.** Al irse, pesa más el precio que lo digital |
| Voces de practitioners de Flat 101 (F-899) | **No valida; muestra que la idea ya circula** en el sector. Coincide con la evidencia sobre el siniestro y el escalamiento a una persona |
| Ocho papers sobre estrategia de canales (F-917 a F-924), verificados a partir de una revisión de literatura aportada | **Sí.** Dan el marco de convivencia de canales (§3.6). El efecto de canibalización sobre los agentes es menor de lo que la revisión decía: solo aparece en mercados con pocas oportunidades |

---

## Anexo A · Referentes revisados

| Referente | Bloque | Aportó a | Rigor de lo encontrado |
|---|---|---|---|
| Pacífico Seguros | Perú | Costo de servir | 🟠 D (F-866) |
| 🔧 Pacífico Salud | Perú | Alcance y salud en el día a día: seguro en Yape, telemedicina propia, orientación por WhatsApp | 🟠 D / 🔴 E (F-938 a F-942) |
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
- la retención por inercia es explotable y el regulador la puede prohibir (F-886);
- 📎 los canales de distribución conviven porque cada uno resuelve algo distinto (F-923).

**Señales emergentes** (sin resultados todavía):

- **Agentes de IA que venden y atienden dentro de apps ajenas:** Mercado Pago (F-864); Oscar opera con lo que
  llama "IA agéntica" (F-858).
- **El seguro como función de una billetera o banco de uso diario:** Yape (F-869), Nubank (F-863).
- **Una disputa de IA contra IA en el siniestro:** clientes que usan IA para apelar rechazos (F-885).
- **Telemetría para no renovar:** selección explícita, con riesgo reputacional (F-870).
- **Indemnización instantánea en siniestros simples** (Porto Seguro, F-865).
- **Gamificación de salud como motor de uso diario** (Alan, F-859).
- **Recuperación de la inversión insurtech en LatAm en 2025, con más disciplina** (F-878).
- 📎 **Bancos que compiten por "custodiar el permiso para actuar"** de agentes de IA que ejecutan con confirmaciones
  (practitioners de Flat 101, F-899; opinión).
- 📎 **Finanzas abiertas en la agenda regulatoria peruana y "seguro abierto" en Brasil** (F-900, F-902).
- 📎 **Seguros paramétricos en desarrollo en Perú**, aún sin oferta (F-902).
- 📎 **Reglamento peruano de IA por niveles de riesgo (sept-2025)**, que alcanzará a la tarificación y los siniestros con
  IA (F-907).
- 📎 **Seguros de vida que se usan en vida y cambian con la etapa** (Bradesco Vida Viva, F-905), sin cifras.
- 📎 **La frontera de la delegación en IA:** se acepta que cotice o informe, no que presente un siniestro o cancele por
  uno (F-916). Medirla en Perú es un vacío.
- 📎 **Hubs de salud con valor diario como respuesta al "no lo usé"** (F-895; propuesta de una agencia, sin
  resultados).

**🔧 Señales de la entrevista al CEO de Credicorp (F-932; opinión):**

- **Agentes de IA que compran por el cliente** y eligen por precio o beneficios: la relación con la marca podría
  desaparecer.
- **Un "funcionario" de IA para 18 millones de peruanos** que hoy no tienen quién los asesore.
- **Definir al competidor como una conducta** (el efectivo, en el caso de Yape), no como otra empresa.
- **Apuestas pequeñas que fracasan varias veces antes de funcionar**, como Yape en su origen.

**🔧 Señales de Pacífico Salud (F-939 a F-942; declaraciones de la empresa):**

- **Orientación médica por WhatsApp 24/7** con médicos reales, y gestión de citas y búsqueda de medicamentos por el mismo
  canal.
- **Ecosistema de seguro, telemedicina y prestación propia** para segmentos de bajo ticket, con inversión en nuevas sedes
  en zonas desatendidas de Lima y regiones.
- **El seguro como puerta de entrada a la atención,** no al revés: un médico accesible para quien hoy se automedica.

**Eje candidato para escenarios:** quién será dueño de la relación diaria con el cliente. Puede ser la
aseguradora, un banco o una billetera, el empleador o corredor, o una interfaz de IA. Es una hipótesis para el
ejercicio, no un hallazgo.

## Anexo C · 🔧 Métodos de medición, explicados con ejemplos

**Contactos por necesidad resuelta.** Se define primero la necesidad ("cobrar un reembolso"), con su inicio y su
cierre. Luego se cuentan todos los contactos del cliente sobre esa necesidad, por cualquier canal: llamadas, chats,
correos, visitas, mensajes al corredor. Se divide entre las necesidades cerradas. *Ejemplo:* 1.000 reembolsos pagados
en un mes que generaron 2.600 contactos dan 2,6 contactos por reembolso. Si tras rediseñar el seguimiento en el app
baja a 1,4, el canal ahorró costo, aunque las visitas al app no hayan cambiado.

**Tasa de recontacto.** Porcentaje de casos en que el cliente vuelve a contactar por lo mismo dentro de 7 días después
de que se dio por resuelto. Mide si de verdad se resolvió.

**Renovación y persistencia.** Renovación: de las pólizas que vencen en un periodo, qué porcentaje se renueva.
Persistencia: de las pólizas emitidas en un mes, qué porcentaje sigue vigente 13 y 25 meses después. Se usa en
productos de pago continuo, como vida.

**Cohortes emparejadas.** Sirve para estimar el efecto de algo que el cliente elige usar, como el app. Se toma a los
clientes que adoptaron el app en un periodo y se busca, para cada uno, un "gemelo" que no lo adoptó pero que antes era
igual en lo que importa: mismo producto, antigüedad, prima, canal de venta, región, siniestros y renovaciones previas.
Luego se compara la renovación de ambos grupos en los 12 meses siguientes. *Límite:* solo empareja lo que se puede
medir. El ensayo de bienestar de Illinois mostró que, aun con muchos controles, la comparación seguía confundiendo
selección con efecto (F-854). Por eso es un primer paso, no la prueba final.

**Despliegue escalonado.** Es la forma práctica de tener un grupo de control sin negarle nada a nadie para siempre. Se
lanza una función (por ejemplo, el aviso de renovación con comparación de coberturas en el app) por oleadas: un mes a un
grupo de clientes elegido al azar, el mes siguiente a otro, y así. Mientras tanto, los que aún no la reciben sirven de
comparación. *Ejemplo:* si los que recibieron el aviso en la primera oleada renuevan 3 puntos más que los que todavía no
lo tienen, y la diferencia se repite en cada oleada, es un efecto del aviso, no de quién lo usa.

**Separar selección de efecto.** Selección: el grupo es distinto porque se eligió solo (los sanos se inscriben en el
programa de bienestar; los clientes ordenados usan el app). Efecto: el grupo cambió por lo que hicimos. *Cómo
distinguirlos:* (1) mirar al grupo *antes* de la intervención: si ya era distinto, hay selección; (2) comparar contra un
grupo de control sorteado o escalonado; (3) desconfiar de cifras que comparan usuarios con no usuarios sin control. En
Illinois, los participantes gastaban US$115 menos al mes *antes* de empezar; la comparación simple atribuía al programa
un ahorro de US$104; el sorteo mostró que no había ahorro (F-854).

**Siniestralidad por cohorte.** Siniestros pagados entre prima ganada, calculados para un grupo que entró en el mismo
periodo (por ejemplo, los que se inscribieron en el programa de manejo en enero) y seguido en el tiempo. Se compara con
su propia siniestralidad antes de entrar y con un grupo de control.

## Anexo D · 🔧 Insumos para el ejercicio con los ramos

Para validar dos hipótesis del diagnóstico ("la actividad la determina el producto, no el canal" y "la gente casi no
interactúa con la propuesta de valor") y para elegir la teoría de valor, conviene pedir a cada ramo estos datos. Si un
dato no existe, que no exista también es un hallazgo.

| Dato | Para qué sirve | Cómo se lee |
|---|---|---|
| Frecuencia natural de necesidad por producto: siniestros por póliza al año; atenciones al año en salud; consultas por póliza | Saber cuántas veces al año el producto le da al cliente una razón para interactuar | Si un producto genera una necesidad al año, una meta de uso mensual no tiene sentido |
| Motivos de contacto por canal, con volumen (call center, app, web, WhatsApp, oficinas, corredor) | Ver qué buscan los clientes y dónde | Separar motivos claros (migran a digital) de ambiguos (necesitan rediseño o persona) |
| Contactos por necesidad y recontacto a 7 días, por flujo | Medir resolutividad | Los flujos con más recontacto son los primeros candidatos a rediseño |
| Porcentaje de clientes sin ninguna interacción en 12 meses, por producto | Dimensionar el silencio normal del seguro | Un silencio alto con renovación alta sugiere inercia; con renovación baja, falta de valor percibido |
| Tasa de uso de cada beneficio de la propuesta de valor (por ejemplo, médico a domicilio, chequeo preventivo, asistencia vehicular) | Saber si la propuesta de valor se usa | Beneficios que casi nadie usa no generan recurrencia ni valor percibido |
| Tiempo desde la compra hasta el primer uso de un beneficio o servicio | Ver si el cliente "estrena" su seguro | Un primer uso temprano puede ser el momento de confianza (hipótesis 7 de §4) |
| Renovación según uso de beneficios y según adopción del app, con las variables de emparejamiento del Anexo C | Primera lectura de retención | Si la diferencia desaparece al emparejar, era selección |
| Canal de origen de cada póliza (directo, corredor, banco, empleador, concesionario) y su renovación | Identificar el ancla de cada cartera | Las carteras que dependen de un ancla necesitan un diseño para el momento en que el ancla se suelta |
| Tiempo a resolución de siniestros y reclamos, por tipo y canal; reclamos que escalan a Indecopi o la SBS | Medir la teoría 5 | Ubicar dónde se rompe la confianza |
| Costo por contacto por canal | Convertir resolutividad en dinero | Permite calcular el costo de servir de cada cliente (definición de cliente de alto valor) |

## Anexo E · Escala de evidencia usada

🟢 A: académico revisado por pares, con método y muestra explícitos · 🔵 B: regulador, organismo oficial o
reporte auditado · 🟡 C: consultora o industria con método propio no auditable · 🟠 D: prensa o cifra de la
propia empresa sin método · 🔴 E: opinión o marketing sin método. Detalle de cada fuente en
`research/fuentes/codice.md` (F-847 a F-942, más F-17, F-183, F-353 y F-442; F-910, F-911 y F-925 a F-930 están
reservados para documentos internos que no se publican aquí). Enlaces en el Anexo F.

## Anexo F · Referencias con enlace

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
- **F-906** · Banco de Ideas Credicorp, con Ipsos (Rojas, P.; Wiener, L.; Pinedo, S.; Zamora, C.; Sánchez, L.) (2026). *Índice de Inclusión Financiera de Credicorp 2026: un vínculo más digital (octubre 2026)*. 🔵 B. DOCX aportado por la usuaria; URL pública no verificada en esta sesión.
- **F-907** · Pérez-Llorca (equipos de Seguros y Reaseguros de Colombia, España, México, Portugal y Perú) (2026). *Actualidad Iberoamericana de Seguros, tercer trimestre 2026*. 🟡 C. DOCX aportado por la usuaria; URL pública no verificada en esta sesión.
- **F-908** · Enríquez Quicaño, J. B.; Alvarado Mesa, M. F.; Romero Valdivia, M. S. (Desafíos: Economía y Empresa n.° 8, Universidad de Lima, pp. 11-38; DOI 10.26439/ddee2026.n008.7940) (2025). *Aplicación de la economía conductual en el mercado de los seguros*. 🟡 C. [Ver fuente](https://doi.org/10.26439/ddee2026.n008.7940) · Documento aportado por la usuaria.
- **F-909** · Beway, en colaboración con la Asociación Latinoamericana de Suscriptores Marítimos (autoría individual no indicada) (s.f. (c. 2025-2026)). *Cerrar la brecha de aseguramiento marítimo en América Latina: una mirada desde las ciencias del comportamiento*. 🟠 D. Archivo de la usuaria: articulo-bewAY-_Brecha-aseguramiento-maritimo.md (blog.beway.com, dominio bloqueado desde la sesión).
- **F-912** · Luo, X.; Tong, S.; Fang, Z.; Qu, Z. (Marketing Science 38(6):937-947; DOI 10.1287/mksc.2019.1192) (2019). *Frontiers: Machines vs. Humans: The Impact of Artificial Intelligence Chatbot Disclosure on Customer Purchases*. 🟢 A. [Ver fuente](https://econpapers.repec.org/RePEc:inm:ormksc:v:38:y:2019:i:6:p:937-947)
- **F-913** · Jachimowicz, J. M.; Duncan, S.; Weber, E. U.; Johnson, E. J. (Behavioural Public Policy 3(2):159-186; DOI 10.1017/bpp.2019.25) (2019). *When and why defaults influence decisions: a meta-analysis of default effects*. 🟢 A. [Ver fuente](https://econpapers.repec.org/RePEc:cup:bpubpo:v:3:y:2019:i:02:p:159-186_00)
- **F-914** · Longoni, C.; Bonezzi, A.; Morewedge, C. K. (Journal of Consumer Research) (2019). *Resistance to Medical Artificial Intelligence*. 🟢 A. [Ver fuente](https://www.scinapse.io/papers/2942858056)
- **F-915** · Dietvorst, B. J.; Simmons, J. P.; Massey, C. (Management Science 64(3)) (2018). *Overcoming Algorithm Aversion: People Will Use Imperfect Algorithms If They Can (Even Slightly) Modify Them*. 🟢 A. [Ver fuente](https://pubsonline.informs.org/doi/10.1287/mnsc.2016.2643)
- **F-916** · Insurity (cita secundaria) (2026). *Encuesta a consumidores de EE.UU. sobre comodidad con la IA en seguros*. 🟠 D. Cita secundaria; fuente original no consultada.
- **F-917** · Neslin, S. A.; Grewal, D.; Leghorn, R.; Shankar, V.; Teerling, M. L.; Thomas, J. S.; Verhoef, P. C. (Journal of Service Research 9(2):95-112) (2006). *Challenges and Opportunities in Multichannel Customer Management*. 🟢 A. [Ver fuente](https://doi.org/10.1177/1094670506293559)
- **F-918** · Verhoef, P. C.; Neslin, S. A.; Vroomen, B. (International Journal of Research in Marketing 24(2):129-148) (2007). *Multichannel customer management: Understanding the research-shopper phenomenon*. 🟢 A. [Ver fuente](https://doi.org/10.1016/j.ijresmar.2006.11.002)
- **F-919** · Verhoef, P. C.; Kannan, P. K.; Inman, J. J. (Journal of Retailing 91(2):174-181) (2015). *From Multi-Channel Retailing to Omni-Channel Retailing: Introduction to the Special Issue on Multi-Channel Retailing*. 🟢 A. [Ver fuente](https://doi.org/10.1016/j.jretai.2015.02.005)
- **F-920** · Verhoef, P. C.; Broekhuizen, T.; Bart, Y.; Bhattacharya, A.; Dong, J. Q.; Fabian, N.; Haenlein, M. (Journal of Business Research 122:889-901) (2021). *Digital transformation: A multidisciplinary reflection and research agenda*. 🟢 A. [Ver fuente](https://doi.org/10.1016/j.jbusres.2019.09.022)
- **F-921** · Dalla Pozza, I. & Texier, L. (Journal of Applied Business Research 30(3):863-868; versión previa IPAG Working Paper 2014-059) (2014). *Managing Multichannel Strategies in the Service Sector: The Example of the French Insurance Industry*. 🟢 A. [Ver fuente](https://clutejournals.com/index.php/JABR/article/view/8571)
- **F-922** · Holland, C. P. & Kavuri, A. S. (The Geneva Papers on Risk and Insurance – Issues and Practice 50(1); DOI 10.1057/s41288-024-00341-0) (2024). *Insurtech strategies: a comparison of incumbent insurance firms with new entrants*. 🟢 A. [Ver fuente](https://link.springer.com/10.1057/s41288-024-00341-0)
- **F-923** · Rubio-Misas, M. (International Journal of Bank Marketing 40(4):724-745; DOI 10.1108/IJBM-04-2021-0129) (2022). *Bancassurance and the coexistence of multiple insurance distribution channels*. 🟢 A. [Ver fuente](https://doi.org/10.1108/IJBM-04-2021-0129)
- **F-924** · Sharma, D. & Gassenheimer, J. B. (European Journal of Marketing 43(7/8):1076-1091) (2009). *Internet channel and perceived cannibalization: Scale development and validation in a personal selling context*. 🟢 A. [Ver fuente](https://doi.org/10.1108/03090560910961524)
- **F-931** · Gorman, M. F. (Management Science 56(1):iv-vii; DOI 10.1287/mnsc.1090.1132) (2010). *Management Insights (resumen editorial de los artículos del número, incluido Campbell y Frei, 2010)*. 🟢 A. [Ver fuente](https://doi.org/10.1287/mnsc.1090.1132)
- **F-932** · Gianfranco Ferrari, CEO de Credicorp (entrevista; notas tomadas por la usuaria) (2026). *Entrevista sobre transformación digital, IA y estrategia en servicios financieros (notas)*. 🔴 E. Notas de la usuaria; entrevista pública sin enlace aportado.
- **F-933** · Thakkar, J.; Kurup, R.; Laba, T.-L.; et al. (JAMA Internal Medicine 176(3):340-349; DOI 10.1001/jamainternmed.2015.7667) (2016). *Mobile Telephone Text Messaging for Medication Adherence in Chronic Disease: A Meta-analysis*. 🟢 A. [Ver fuente](https://doi.org/10.1001/jamainternmed.2015.7667)
- **F-934** · Ashwood, J. S.; Mehrotra, A.; Cowling, D.; Uscher-Pines, L. (Health Affairs 36(3):485-491; DOI 10.1377/hlthaff.2016.1130) (2017). *Direct-To-Consumer Telehealth May Increase Access To Care But Does Not Decrease Spending*. 🟢 A. [Ver fuente](https://www.rand.org/pubs/external_publications/EP67074.html)
- **F-935** · Zhou, Y. Y.; Garrido, T.; Chin, H. L.; Wiesenthal, A. M.; Liang, L. L. (American Journal of Managed Care 13(7):418-424) (2007). *Patient Access to an Electronic Health Record With Secure Messaging: Impact on Primary Care Utilization*. 🟢 A. [Ver fuente](https://www.ajmc.com/journals/issue/2007/2007-07-vol13-n7/jul07-2509p418-424)
- **F-936** · Duru, O. K.; Schmittdiel, J. A.; Dyer, W. T.; et al. (American Journal of Managed Care 16(1):33-40) (2010). *Mail-Order Pharmacy Use and Adherence to Diabetes-Related Medications*. 🟢 A. [Ver fuente](https://californiahealthline.org/morning-breakout/kaiser-study-finds-access-to-mailorder-pharmacies)
- **F-937** · Roebuck, M. C.; Liberman, J. N.; Gemmill-Toyama, M.; Brennan, T. A. (Health Affairs 30(1):91-99) (2011). *Medication Adherence Leads To Lower Health Care Use And Costs Despite Increased Drug Spending*. 🟢 A. [Ver fuente](https://scholarhub.vn/publication/:slug/ef630f12-adfb-453e-8e75-a80a76b8da93)
- **F-938** · Trome y Diario Correo (publirreportajes sobre el seguro de salud de Pacífico vendido en Yape) (c. 2025-2026). *Atenciones médicas en línea con seguro de salud Yape*. 🟠 D. [Ver fuente](https://diariocorreo.pe/publireportaje/atenciones-medicas-en-linea-con-seguro-de-salud-yape-noticia/)
- **F-939** · Cortez Carpio, J. (líder de innovación y diseño, laboratorio de innovación La Cápsula de Pacífico Salud), publicación en LinkedIn; captura aportada por la usuaria (c. 2025 (27 de agosto; año no visible en la captura)). *¿Y si el mejor canal para una experiencia de salud no siempre es una app o una web? (orientación médica por WhatsApp en Tsana)*. 🔴 E. Captura de LinkedIn aportada por la usuaria (enlace acortado lnkd.in/d9WJzB8g).
- **F-940** · Gestión (entrevista a José Enrique Deza, subgerente de Productos Masivos de Pacífico Salud); notas parafraseadas por la usuaria (2025). *Yape espera afiliar a su seguro de salud a 30.000 usuarios en su primer año (26 de junio de 2025)*. 🟠 D. Notas de la usuaria a partir de capturas de gestion.pe; URL no aportada.
- **F-941** · Gestión (redacción) (2025). *Pacífico Salud: inversión en innovación e infraestructura (20 de octubre de 2025; título truncado en la captura)*. 🟠 D. Notas de la usuaria a partir de capturas de gestion.pe; URL no aportada.
- **F-942** · Gestión (entrevista a Guillermo Garrido-Lecca, CEO de Pacífico Salud) (2025). *Pacífico Salud explora zonas para expandir su red y afianza apuesta por diversificar segmentos (21 de julio de 2025)*. 🟠 D. Notas de la usuaria a partir de capturas de gestion.pe; URL no aportada.
