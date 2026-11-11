# Gestión de colas en la atención presencial de aseguradoras: benchmarking

> Documento de investigación. Fuente persistente y versionada en el repositorio.
> Fecha de elaboración: 2026-11-11 · Última actualización: 2026-11-11 · Versión: v1.1
> Origen: `/seeker` (registro empírico + teórico/crítico). Fuentes F-847 a F-886.
> v1.1 (2026-11-11): se amplía el alcance a **la espera como espacio de awareness** (§10), a pedido
> del usuario, con prioridad en evidencia latinoamericana. F-873 a F-886.

---

## 0. Resumen ejecutivo

- **No existe un benchmark público y verificable de cómo las aseguradoras manejan sus colas
  presenciales.** Lo que publican las aseguradoras o sus proveedores son casos de marketing
  sin cifras auditables (F-859, F-860, F-862). El benchmark se arma con dos piezas: los
  modelos operativos que sí se observan en aseguradoras y en sectores vecinos (banca, salud,
  sector público), y la ciencia de colas, que es sólida y en buena parte experimental.
- **Se observan cinco modelos operativos**, que se combinan: (1) cita previa, (2) ticket con
  pantallas y monitoreo central, (3) recepción que deriva al canal remoto, (4) carril
  preferente obligatorio por ley y (5) tiempo máximo de espera fijado por norma. RIMAC usa
  el primero en su tienda de San Isidro (F-861). Ping An usa el tercero a escala (F-862, F-863).
- **La evidencia más fuerte dice cuatro cosas.** El cliente reacciona al largo de la fila que
  ve, más que al tiempo real de espera (F-850). La información de espera cambia el abandono
  según su magnitud y su frecuencia de actualización (F-851, un experimento aleatorio con 1,4
  millones de casos). Explicar la demora y mostrar el trabajo que se hace sube la valoración
  del servicio (F-849, F-854, F-855). Saltarse el orden de llegada choca con una norma social
  fuerte (F-848, F-856).
- **Hay dos advertencias.** Bajar el tiempo de espera a la mitad casi no movió la
  satisfacción en una aseguradora (F-864): el problema puede estar en la comunicación y no en
  la capacidad. Y la cita previa obligatoria excluye a los mayores; en España generó una
  protesta nacional (F-870, F-871).
- **Perú no fija un tiempo máximo de espera presencial.** Sí obliga a dar atención preferente
  (F-865), con multas aplicadas a bancos (F-866). La SBS exige al sistema financiero una
  alternativa de atención humana frente a los canales automatizados (F-867), pero esa norma
  no es la de seguros.

---

## 1. Tipologización de la pregunta

| Capa | Tipo | Qué se busca |
|---|---|---|
| Qué hacen las aseguradoras | Empírico-cualitativo (benchmark) | Modelos operativos documentados |
| Qué funciona | Causal | Efecto de cada palanca sobre abandono, percepción y satisfacción |
| Qué exige la norma | Normativo | Perú y referentes regionales |
| Qué significa hacer esperar | Teórico/crítico | Espera, poder y confianza |

---

## 2. Benchmark: modelos operativos observados

| Modelo | Quién lo usa (evidencia) | Qué resuelve | Riesgo |
|---|---|---|---|
| **1. Cita previa** (web, app o QR en puerta) | RIMAC, tienda de San Isidro: atención con reserva, lunes a viernes de 9:00 a 18:00 (F-861, prensa) · organismos públicos españoles como Muface | Aplana la demanda y permite preparar el caso antes | Excluye a quien no reserva o no usa medios digitales (§5) |
| **2. Híbrido: cita + ticket para quien llega sin cita** | Banco-aseguradora sueco con Qmatic desde 2017: el cliente con cita se registra en un kiosco, el que llega sin cita saca ticket y ve su turno en pantalla, y el personal gestiona la carga desde una app (F-859, caso de proveedor) | Combina previsibilidad con acceso libre | Sin cifras publicadas de resultado |
| **3. Ticket + pantallas + monitoreo central** | Adamjee Insurance (Pakistán, 34 sucursales): dispensador de tickets, pantallas por ventanilla y tablero central del desempeño de cada sucursal (F-860, caso de proveedor) | Visibilidad del turno y control desde la casa matriz | Sin cifras publicadas de resultado |
| **4. Derivación de la sucursal al canal remoto** | Ping An: antes había colas en unas sucursales y otras vacías; el sistema asigna un agente remoto según la ubicación del cliente (F-862, 2018). En 2026 su servicio exprés dice resolver 91% de las solicitudes sin humano (F-863, comunicado propio) | Saca de la fila los trámites que no necesitan presencia | Cifras autodeclaradas; no auditadas |
| **5. Carril preferente por ley** | Obligatorio en Perú para gestantes, niños, adultos mayores y personas con discapacidad (F-865) | Prioridad legítima y aceptada socialmente | Multa si no se cumple (F-866) |
| **6. Tiempo máximo legal** | Brasil: leyes municipales y estatales de 15 minutos en bancos (20 a 30 en días pico); autorregulación de Febraban en 20 y 30 minutos (F-868). Procon-MG multó con R$ 96 mil a una agencia de la Caixa por una espera de 22 minutos (F-869) | Pone un piso exigible | La fiscalización depende de denuncias; no se encontró ningún estudio que mida si las leyes redujeron la espera (§6) |

**Lectura del benchmark.** Los modelos 1 a 3 son de gestión del flujo y los venden los mismos
proveedores (Qmatic, Wavetec). El modelo 4 es el único que reduce la demanda presencial en vez
de ordenarla. Los modelos 5 y 6 vienen impuestos desde afuera.

---

## 3. Qué dice la evidencia sobre cada palanca

### 3.1 La fila que se ve pesa más que la espera real

Un estudio de un mostrador de delicatessen en un supermercado latinoamericano cruzó video
de la fila con datos de venta. Los clientes miran el largo de la fila y no corrigen lo
suficiente por la velocidad a la que avanza. Por encima de unas 5 personas, el efecto sobre la
compra es significativamente negativo. Solo 7% de la venta perdida se recuperó en otra parte
de la tienda (Lu, Musalem, Olivares y Schilkrut, 2013 — 🟢 peer-reviewed, *Management
Science*; observacional con datos de alta frecuencia; F-850).

**Implicancia.** El ticket o la fila virtual esconden el largo de la fila. Juntar varias filas en
una sola visible puede espantar más clientes aunque sea más eficiente.

### 3.2 Pero la fila única puede volver más lento al personal

En experimentos de comportamiento, una fila única servida por varias personas hizo más lento
el servicio que filas separadas con un responsable cada una. Los autores lo atribuyen a una
responsabilidad diluida. No ver el largo de la fila también hizo más lento al personal, salvo
con incentivos de desempeño (Shunko, Niederhoff y Rosokha, 2018 — 🟢 peer-reviewed,
*Management Science*; F-853). ⚠️ La réplica oficial de la revista confirmó la dirección del
efecto de la fila única, pero sin significancia estadística en la réplica principal.

**Tensión con §3.1.** Ocultar la fila ayuda al cliente y puede perjudicar la velocidad del
personal. Un tablero interno del largo de la fila, visible para el personal y no para el
cliente, resuelve ambas cosas. Esto es una inferencia, no un resultado probado.

### 3.3 La información de espera cambia el abandono

En un experimento aleatorio con 1.425.745 viajes en una plataforma de transporte, con la
espera real constante, tanto la magnitud del tiempo anunciado como la frecuencia de
actualización cambiaron el abandono (Yu, Zhang y Zhou, 2022 — 🟢 peer-reviewed,
*Management Science*; ✅ experimento de campo aleatorio, resultado conductual; F-851). En un
call center bancario israelí, por encima de 90 segundos de espera los clientes reaccionan con
aversión a la pérdida frente a lo anunciado (Yu, Allon y Bassamboo, 2021 — 🟢 peer-reviewed,
*Management Science*; observacional; F-852).

**Implicancia.** Anunciar un tiempo y luego superarlo se castiga más de lo que se premia
cumplirlo. La estimación debe ser realista y actualizarse.

### 3.4 Explicar la demora y mostrar el trabajo

Una demora explicada se percibe más corta que una sin explicación; importa poco si la
explicación culpa al cliente o al servicio (Seawright y Sampson, 2007 — ⚠️ revisión por pares
no verificada en esta búsqueda; experimento con video; F-849). Es una de las pocas pruebas
empíricas de los principios de Maister (F-847), que se citan mucho y se han probado poco.

Mostrar el trabajo que se hace sube el valor percibido del servicio, incluso con esperas más
largas (Buell y Norton, 2011 — 🟢 peer-reviewed, *Management Science*; experimentos de
laboratorio simulados; F-854). En campo, en servicios de comida, la transparencia operativa
subió 22,2% la calidad reportada y bajó 19,2% el tiempo de proceso (Buell, Kim y Tsay, 2017 —
🟢 peer-reviewed, *Management Science*; dos experimentos de campo y dos de laboratorio; F-855).

**Implicancia para una aseguradora.** Decir en qué etapa está el trámite (por ejemplo,
"revisando tu póliza" o "consultando con siniestros") es una palanca barata y respaldada.

### 3.5 El orden de llegada es una norma social fuerte

La justicia percibida de la fila importa tanto como su duración. Larson llamó *slips* y *skips*
a las veces en que alguien es atendido antes que uno habiendo llegado después (Larson, 1987 —
🟢 revista arbitrada, *Operations Research*, pero ensayo especulativo sin datos propios; F-848).
En un experimento de campo, la mayoría dejó pasar a un desconocido, pero casi nadie aceptó
dinero por hacerlo (Oberholzer-Gee, 2006 — 🟢 peer-reviewed, *Kyklos*; F-856).

**Implicancia.** Un carril preferente legal se acepta porque su criterio es visible y legítimo.
Un carril "VIP" por valor del cliente o la llamada de turnos con cita delante de quien espera
sin cita se perciben como saltos de fila, salvo que la regla se explique en pantalla.

---

## 4. Capa teórica: hacer esperar comunica poder

- **Schwartz (1974, 1975 — F-857).** La espera se reparte según el poder: espera más quien
  tiene menos. Es la referencia canónica de la sociología de la espera; se incluye pese a su
  antigüedad porque el debate actual parte de ella.
- **Auyero (2012 — F-858).** Etnografía de la espera de personas pobres ante el Estado
  argentino. Esperar enseña a ser "paciente" del Estado y no ciudadano; la espera produce
  sumisión. El autor la presenta como una dominación siempre parcial y negociada.

**Por qué importa para una aseguradora.** Quien va en persona a una aseguradora suele ir por
un siniestro, un reembolso rechazado o un reclamo, es decir, en un momento de dependencia.
Una espera larga y sin explicación confirma la desconfianza de base del mercado peruano (cerca
de 48% desconfía de las aseguradoras; ver el node de comportamiento en seguros). Esto es
interpretación teórica, no un resultado medido en seguros.

---

## 5. Contraevidencia buscada a propósito

1. **Reducir la espera no siempre mejora la satisfacción.** Una aseguradora bajó la espera de
   su línea telefónica de 40 a 20 segundos y la percepción de los clientes casi no cambió
   (McKinsey — 🟡 consultora; F-864). Es un canal telefónico, no presencial, y la consultora no
   publica el método. Aun así, es una advertencia directa: hay que contrastar las quejas con
   los datos reales de espera antes de invertir en capacidad.
2. **La cita previa obligatoria excluye.** En España, la campaña "Soy mayor, no idiota" (2022)
   reunió unas 600.000 firmas contra la banca sin atención presencial libre y llevó a las
   patronales bancarias a comprometer horarios y atención preferente para mayores (F-870,
   prensa). En el Reino Unido, uno de cada tres mayores de 75 años solo consigue cita con su
   médico de cabecera por vía digital, y algunos dejan de intentarlo (F-871, informe de una ONG,
   2026).
3. **Los principios de Maister casi no se han probado.** Solo se encontró una prueba directa
   del principio de "espera explicada" (F-849). No se encontró una réplica del principio de
   "tiempo ocupado se siente más corto".
4. **La fila única no es claramente mejor ni claramente peor.** Ver §3.1 y §3.2.

---

## 6. Normativa peruana y regional

- **Atención preferente.** La Ley 28683 obliga a entidades públicas y privadas que atienden al
  público a dar atención preferente a gestantes, niños, adultos mayores y personas con
  discapacidad. La multa no excede el 30% de la UIT según una versión del texto (F-865). Indecopi
  multó a un banco con 10 UIT en 2025 por este motivo (F-866; detalle tomado de un fragmento,
  no del texto completo).
- **Alternativa humana.** La Res. SBS 01741-2026 obliga a las entidades del sistema financiero
  que usan atención automatizada a ofrecer una alternativa de atención personal (F-867).
  ⚠️ Modifica el reglamento de conducta de mercado del **sistema financiero**; las aseguradoras
  tienen su propio reglamento. No se verificó si existe una exigencia equivalente para seguros.
- **Tiempo máximo.** No se encontró un tiempo máximo legal de espera presencial vigente en
  Perú. Circuló una propuesta de 30 minutos que además prohibía las colas en la vía pública; no
  se verificó su número ni su estado (F-872).
- **Referente regional.** Brasil tiene la "lei dos 15 minutos" para bancos (F-868, F-869). No se
  encontró ningún estudio que mida su efecto sobre la espera real.

---

## 7. Qué se puede llevar a una aseguradora peruana

Recomendaciones ordenadas por fuerza de la evidencia que las respalda:

1. **Mostrar un tiempo estimado realista y actualizado** (F-851, F-852). Respaldo alto.
2. **Explicar la demora y mostrar en qué etapa está el trámite** (F-849, F-854, F-855).
   Respaldo alto en otros sectores.
3. **Ocultar el largo de la fila al cliente con ticket o fila virtual y mostrárselo al
   personal** (F-850, F-853). Respaldo medio: dos resultados sólidos combinados por inferencia.
4. **Usar un modelo híbrido: cita para trámites complejos y ticket para quien llega sin cita**
   (F-859, F-870, F-871). Respaldo bajo en resultados, pero la cita obligatoria tiene riesgos
   documentados.
5. **Explicar en pantalla cualquier regla de prioridad distinta del orden de llegada** (F-848,
   F-856). Respaldo medio.
6. **Derivar al canal remoto lo que no necesita presencia, sin cerrarle la puerta al humano**
   (F-862, F-863, F-867). Respaldo bajo: cifras autodeclaradas.
7. **Antes de invertir en capacidad, cruzar las quejas con los datos de espera** (F-864).

---

## 8. Tabla de rigurosidad

| Fuente | Tipo | Revisión por pares | N | Validez | Confiabilidad | Peso |
|---|---|---|---|---|---|---|
| Yu, Zhang y Zhou 2022 (F-851) | Experimento de campo aleatorio | 🟢 *Management Science* | 1.425.745 viajes | ✅ conducta real; ⚠️ transporte, no seguros | ✅ | 🟢 Alto |
| Lu et al. 2013 (F-850) | Observacional, alta frecuencia | 🟢 *Management Science* | 1 tienda | ✅ conducta real; ⚠️ un solo local | ⚠️ sin réplica | 🟢 Alto |
| Yu, Allon y Bassamboo 2021 (F-852) | Observacional | 🟢 *Management Science* | Call center bancario | ✅ conducta real | ⚠️ | 🟡 Medio |
| Shunko et al. 2018 (F-853) | Experimento de laboratorio | 🟢 *Management Science* | Laboratorio | ⚠️ validez ecológica | ⚠️ réplica parcial | 🟡 Medio |
| Buell y Norton 2011 (F-854) | Experimentos simulados | 🟢 *Management Science* | 5 experimentos | ⚠️ simulación online | ✅ | 🟡 Medio |
| Buell, Kim y Tsay 2017 (F-855) | Campo + laboratorio | 🟢 *Management Science* | 4 estudios | ✅ campo | ✅ | 🟢 Alto |
| Seawright y Sampson 2007 (F-849) | Experimento con video | ⚠️ no verificada | — | ⚠️ percepción, no conducta | ⚠️ | 🟡 Medio |
| Oberholzer-Gee 2006 (F-856) | Experimento de campo | 🟢 *Kyklos* | No verificado | ✅ conducta real | ⚠️ | 🟡 Medio |
| Larson 1987 (F-848) · Maister 1985 (F-847) | Ensayo teórico | Larson 🟢 · Maister 🟡 capítulo | — | ⚪ | ⚪ | ⚪ Marco |
| Schwartz 1974-75 (F-857) · Auyero 2012 (F-858) | Teoría y etnografía | 🟢 / 🟡 libro académico | — | ⚪ | ⚪ | ⚪ Marco |
| Qmatic (F-859), Wavetec (F-860), Huawei (F-862) | Caso de proveedor | ⚪ no aplica | — | ❌ sin cifras | ❌ | 🔴 Bajo |
| Ping An 2026 (F-863) | Comunicado de empresa | ⚪ | — | ⚠️ autodeclarado | ❌ | 🔴 Bajo |
| McKinsey (F-864) | Reporte de consultora | ⚪ | — | ⚠️ canal telefónico | ❌ | 🟡 Medio como advertencia |
| Normas y sanciones (F-865 a F-869, F-872) | Normativa | ⚪ | — | ✅ | ✅ | 🔵 Referencia |

**Eco de cita.** F-859 y F-860 provienen del mismo agregador de casos de proveedores; no son
una confirmación independiente. Los blogs de proveedores que repiten "el 48% de los clientes
espera máximo 10 minutos" no se registraron como evidencia porque no tienen fuente primaria.

---

## 9. Limitaciones

- No se encontró información publicada de Pacífico, La Positiva, Mapfre Perú ni Interseguro
  sobre su gestión de colas presenciales. Llenar ese hueco requiere visita en campo (mystery
  shopping) o pedir los datos a cada empresa.
- Toda la evidencia experimental viene de otros sectores (transporte, comida, banca, salud).
  Ningún experimento se hizo en una oficina de seguros.
- No se leyó el texto completo de la Res. SBS 01741-2026, de la Ley 28683 vigente ni de la
  resolución de Indecopi contra el banco.
- No se encontró el reglamento de conducta de mercado del sistema de seguros para verificar si
  exige atención humana.

---

## 10. La espera como espacio de awareness (v1.1)

**Pregunta.** Cómo se aprovecha el tiempo de espera en la oficina para dar a conocer la marca,
los productos o información útil, con prioridad en estudios latinoamericanos.

### 10.1 Conclusión

- **No se encontró ningún estudio, latinoamericano o de otra región, que mida awareness durante la
  espera en una aseguradora.** La evidencia viene de salas de espera de salud, bancos y transporte.
- **La evidencia más sólida es de salud.** Las pantallas y videos en salas de espera suben un poco
  el conocimiento, casi no cambian la conducta y sí provocan preguntas al profesional (F-875,
  F-876). Para una aseguradora, el efecto útil sería ese último: que el cliente llegue a la
  ventanilla con una pregunta sobre un producto.
- **Quien espera está más receptivo.** En un estudio de campo con 66.473 personas en tránsito, la
  gente "cautiva" respondió más a la publicidad móvil, porque siente que le sobra tiempo (F-877).
- **Lo que hace agradable la espera pesa más que acortarla.** Mejorar el ambiente de espera calmó
  más el efecto negativo de esperar que reducir el tiempo real (F-874). Una pizarra de noticias en
  el lobby de un banco hizo la espera más llevadera y mejoró la evaluación del servicio (F-873).
- **En Latinoamérica la evidencia es de salud pública y es débil.** En Brasil, la "sala de espera"
  es una estrategia habitual de educación en salud del SUS, pero la evidencia es casi solo
  cualitativa (F-878). En México hay estudios del IMSS y de centros de salud con resultados de
  conocimiento, de diseño débil o no verificado (F-879, F-880). En Perú no se encontró ningún
  estudio de contenidos en sala de espera; una tesis peruana sí recomienda gestionar la
  experiencia en sala porque el tiempo real de espera se relaciona poco con la satisfacción
  (F-885).
- **Las cifras de recordación que circulan son de proveedores.** "52% de recordación en pantallas
  frente a 32% en TV", "75% recuerda un mensaje en hospitales" o "awareness de producto de 22% a
  45% en bancos" vienen de empresas que venden pantallas o de estudios que ellas encargaron
  (F-882, F-883, F-884). No sirven para decidir.

### 10.2 Evidencia por tipo de uso

| Uso del tiempo de espera | Mejor evidencia | Qué muestra | Solidez |
|---|---|---|---|
| **Educación (salud, finanzas)** | Revisión sistemática de 14 estudios en atención primaria (Berkhout y otros, 2018 — 🟢 peer-reviewed, *European Journal of General Practice*; F-875) | Ganancia pequeña de conocimiento, quizá no relevante; sin cambio robusto de conducta; los pacientes notan las pantallas y preguntan al médico | 🟢 Alta como revisión, pero estudios primarios de calidad baja o media |
| | Revisión integrativa de 33 estudios (Cass, Ball y Leveritt, 2016 — 🟢 peer-reviewed, *Australian Journal of Primary Health*; F-876) | Efecto positivo general en conocimiento, intención, uso de servicios y conducta; actitudes mixtas; pocos estudios de alta calidad | 🟡 Media |
| **Publicidad de marca o producto** | Estudio de campo sobre "audiencia cautiva" (*Journal of Advertising*, 2023 — 🟢 peer-reviewed; F-877) | Quien está obligado a esperar responde más a anuncios; lo explica la sensación de tener tiempo de sobra y el aburrimiento | 🟢 Alta, pero es publicidad móvil en transporte, no pantallas en oficina |
| | Pantallas en sucursales bancarias (proveedores; F-883) | Awareness y venta cruzada al alza, con cifras que no coinciden entre sí | 🔴 Baja |
| **Entretenimiento o información general** | Pizarra de noticias en el lobby de un banco de Boston (Katz, Larson y Larson, 1991; F-873) | Espera más llevadera y mejor evaluación del servicio, según quienes lo citan | 🟡 Media; no se leyó el original |
| **Ambiente de espera** | Pruyn y Smidts, 1998 (🟢 peer-reviewed, *International Journal of Research in Marketing*; F-874) | Mejorar el ambiente calma más que acortar la espera; el efecto de la TV es contradictorio según quién lo cita | 🟢 Alta |
| **Información del propio proceso** | Transparencia operativa (F-854, F-855; ver §3.4) | Mostrar el trabajo que se hace sube el valor percibido | 🟢 Alta |

### 10.3 Latinoamérica: lo que hay

| País | Estudio | Qué encontró | Solidez |
|---|---|---|---|
| Brasil | Revisión integrativa de 8 artículos sobre la sala de espera como espacio de educación en salud en el SUS (Quadros, Kosinski y Schmidt, 2017; F-878) | Consenso de que sirve para educar y crear vínculo; casi todo son relatos de experiencia, sin resultados medidos | 🟡 Baja-media |
| Brasil | Encuesta de industria sobre campañas en ambientes de salud (Meio & Mensagem; F-881) | 83% dice notar televisores en salas de espera o pasillos; 90% en clínicas. Mide exposición, no recordación | 🟠 Baja |
| México | Herramienta multimedia sobre diabetes que los pacientes del IMSS consultan en la sala de espera (*Cirugía y Cirujanos*, 2018; F-879) | El texto la llama ensayo aleatorizado y el título, cuasiexperimento; no se obtuvieron los resultados | ⚠️ No verificado |
| México | Intervención educativa de 15 minutos sobre infecciones respiratorias en la sala de espera de un centro de salud (revista de la UADY; F-880) | Subió el conocimiento; diseño cuasiexperimental sin aleatorización | 🟡 Baja-media |
| Perú | Tesis de la UPCH sobre tiempos de espera en consulta externa (F-885) | El tiempo real de espera se relaciona poco con la satisfacción; recomienda informar sobre demoras y gestionar la sala de espera | 🟡 Media (tesis) |
| Chile u otro país | Fila de un supermercado en una ciudad latinoamericana (Lu y otros, 2013; F-850) | No mide awareness: muestra que la fila visible cuesta ventas | 🟢 Alta, otro tema |

### 10.4 Contraevidencia buscada a propósito

1. **La TV en la sala de espera puede alargar la espera percibida.** Una revisión cita un estudio en
   una clínica donde quienes veían televisión percibieron una espera más larga y quedaron menos
   satisfechos; otra revisión dice que la TV en un hospital no cambió la experiencia (vía F-874).
   El resultado sigue abierto.
2. **Notar una pantalla no es comprar.** En una encuesta encargada por un proveedor, 84% dijo que
   las pantallas hacen pasar el tiempo más rápido, pero solo 40% dijo que eso lo haría preferir la
   tienda (F-886).
3. **El conocimiento sube poco y la conducta casi no cambia** (F-875). Si el objetivo es venta, la
   pantalla sola no basta; su valor está en abrir la conversación con el asesor.
4. **No se encontró ningún estudio que pruebe que la publicidad en la espera irrita.** Sí hay
   evidencia vecina: en anuncios de video, mostrar un temporizador baja la irritación, salvo si
   además hay un botón para saltar el anuncio (búsqueda de esta iteración, no registrada como
   fuente por falta de cita completa).

### 10.5 Qué se puede llevar a una aseguradora (inferencias, ordenadas por respaldo)

1. **Contenido que lleve a una pregunta, no solo a recordar la marca.** Por ejemplo: "¿Sabías que
   tu seguro vehicular cubre X? Pregúntale a tu asesor". Respaldo: el efecto más consistente en
   salud es que el paciente pregunta (F-875).
2. **Contenido ligado al motivo de la visita.** Quien viene por un siniestro o un reembolso está en
   un momento de dependencia y desconfianza (§4). Mostrar el estado y los pasos de su trámite
   (F-854, F-855) es más seguro que mostrarle un producto nuevo. Ofrecer otro producto en ese
   momento puede leerse como aprovecharse; esto es una inferencia, no un resultado medido.
3. **Mejorar el ambiente antes que llenar la pantalla de anuncios** (F-874, F-873).
4. **Medir con grupo de control.** No hay evidencia en seguros. Lo correcto es probar contenido A
   frente a contenido B por sucursal y semana, y medir preguntas al asesor, cotizaciones y
   abandono de la fila, no recordación declarada.

### 10.6 Limitaciones de esta ampliación

- No se leyeron a texto completo Katz y otros (1991), el estudio del IMSS ni el de la UADY.
- No se encontraron campañas documentadas de aseguradoras o bancos latinoamericanos (Sura,
  Bancolombia, BancoEstado, RIMAC, Pacífico) en sus salas de espera.
- Los buscadores de salud latinoamericanos (LILACS, SciELO) se consultaron solo a través de un
  buscador general.

---

## Conexiones

- [[seguros-comportamiento-mundo-peru|Comportamiento y percepción de seguros (Mundo vs. Perú)]]
  — la desconfianza de base del mercado peruano es el contexto en que la espera presencial se
  lee como señal de poder (§4).
- [[conducta-humano-ia|Conducta humano-IA]] — el modelo de derivación al canal remoto (§2,
  modelo 4) y la exigencia de una alternativa humana (§6) se cruzan con la confianza en
  sistemas automatizados.
- [[fenomenos-psicologicos|Fenómenos psicológicos y su estado de replicación]] — la aversión a
  la pérdida frente al tiempo anunciado (§3.3) y la regla del pico y el final aplican a la
  experiencia de espera.
- [[modelo-salud-ia-farmacias-peru|Modelo de triage IA + farmacias]] — el triage en la puerta
  y la derivación de casos son el mismo problema de enrutamiento de la demanda.
