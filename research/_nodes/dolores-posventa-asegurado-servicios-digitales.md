# Dolores del asegurado después de la compra: qué servicios digitales los resuelven y con qué evidencia

> Documento de investigación. Fuente persistente y versionada en el repositorio.
> Fecha de elaboración: 2026-10-28 · Última actualización: 2026-10-28 · Versión: v0.1 (exploratorio)
> Origen: pregunta de la persona usuaria: ¿qué otros terrenos se pueden digitalizar **una vez que la persona ya tiene el seguro** (agendar citas, historial médico, autorizaciones, reembolsos), con casos concretos y solo si hay respaldo confiable? Incluso si suena a largo plazo.
> Método de `/trinidad` (pistas empírica, social y de negocio, sin mezclar criterios). Fuentes nuevas registradas en `research/fuentes/codice.md` (F-1218 a F-1237). Complementa los nodes de ramos (`digitalizacion-ramos-vehicular-salud-microseguros`) y de embebidos.
> Solo fuentes públicas. **Todo se leyó por fragmentos de buscador (nivel N2)**: ninguna página se abrió completa. Donde el fragmento no mostraba una cifra, no la uso.
> **Pista social: no se pudo cubrir** (ver §5). No hay análisis interno de ninguna aseguradora en este documento.

---

## 0. Qué es y qué no es este documento

Hasta aquí el ciclo miró cómo se **vende** y se **paga** un seguro. Este node mira lo que pasa **después**: la persona ya tiene la póliza y le toca usarla. Ahí aparecen los dolores cotidianos: pedir una cita, saber qué cubre, pedir una autorización, cobrar un reembolso, tener a mano su historial, entender cuánto va a pagar.

No concluye qué construir. Ordena, por dolor, los **casos concretos** que existen, la **mejor evidencia disponible** y qué tan firme es. Sirve para decidir dónde vale la pena probar y dónde la evidencia todavía no alcanza.

## 1. En corto

1. **Los dolores de proceso, frecuentes y simples, tienen la evidencia más sólida y la adopción más masiva.** Los recordatorios de cita bajan la inasistencia de forma consistente (riesgo relativo de 0,75 en un metaanálisis, F-1229) y el NHS App de Inglaterra tiene 39 millones de usuarios registrados y 67,8 millones de recetas repetidas pedidas en 12 meses (F-1235). Es el terreno donde "digitalizar" tiene mejor respaldo.
2. **Los dolores de información (historial, notas, precios) mejoran la experiencia más de lo que mejoran la salud o el gasto.** Los portales mejoran la satisfacción, pero la evidencia de resultados clínicos es débil (F-1230). Una herramienta de precios no bajó el gasto: lo subió en US$ 59 y la usó 10% (F-1233). Los datos compartidos entre sistemas reducen pruebas repetidas solo con evidencia de baja calidad y se consultan en menos de 10% de los encuentros (F-1232).
3. **Los programas de bienestar con recompensas (el caso de Vitality) tienen evidencia a favor que viene del propio proveedor y evidencia independiente que no encuentra efecto.** El único ensayo aleatorizado grande (Illinois, unos 5.000 empleados) no halló efectos en gasto ni en salud tras más de dos años, y mostró que quienes participan ya gastaban menos antes (F-1218). Los estudios de Vitality son correlacionales y vinculados a Discovery (F-1219). **No encontré una evaluación independiente de Vitality.**
4. **La velocidad de reembolso y autorización es hoy una promesa de marca (Alan) y una obligación regulatoria (EE. UU.), pero no una medida pública en el Perú.** Alan dice que 90% de los reembolsos salen en un día, y otra nota dice 99%: las cifras no coinciden y son propias (F-1220). La norma de EE. UU. fija 72 horas para casos urgentes y 7 días para los demás (F-1234). **No hallé una medida pública de tiempo de reembolso en seguros de salud peruanos.**
5. **En el Perú existen los componentes, pero no hay una sola evaluación de su efecto.** Mapfre ofrece una clínica digital, chat médico, historia clínica electrónica y entrega de medicinas desde la app (F-1224); EsSalud tiene la app Mi Consulta para citas; el App Store de Rímac anuncia búsqueda de clínicas, gestión de reembolsos y asistencia vehicular (F-1224). No hallé datos de uso, resultados ni satisfacción de ninguno.
6. **Lo que más se parece a una "queja medida" en el Perú son los reclamos administrativos.** En el sector seguros hubo 8.248 reclamos ante Indecopi entre 2019 y 2022, y 87,8% ya se habían presentado a la aseguradora (F-1226). No sirven para saber qué parte es agendamiento, autorización o reembolso: eso no está abierto.

## 2. Mapa: dolor, casos, evidencia y lectura

La columna "Lectura" aplica la regla del ciclo (digital en los bordes, valor en el medio): ¿es una tarea frecuente y simple, hay capacidad física detrás, la persona puede usarla, se puede medir?

| Dolor | Casos concretos | Mejor evidencia | Nivel | Lectura |
|---|---|---|---|---|
| **Recordar y no faltar a la cita** | Recordatorios por SMS o llamada (ensayos en Kaiser Permanente, metaanálisis) | Metaanálisis de ensayos: inasistencia 15% vs. 21% (RR 0,75); varios recordatorios funcionan mejor que uno (F-1229) | 🔵 B | **Sí.** Evidencia más sólida. Barato, frecuente, medible |
| **Agendar la cita en línea** | Autoagendamiento en sistemas hospitalarios de EE. UU.; Mapfre Clínica Digital; EsSalud Mi Consulta; EPS Sura (web y WhatsApp) | Estudio de más de 134.000 visitas: quienes lo adoptan primero son más jóvenes, blancos y con seguro comercial; riesgo de ampliar brechas. Efecto en inasistencia: estudios pequeños y cifras de proveedores (F-1231) | 🟡 C | **Sí con condiciones.** Funciona si hay agenda real detrás y un canal asistido para quien no lo usa |
| **Hablar con el médico sin ir** | Mensajería segura de Kaiser Permanente; Ping An Good Doctor; Tsana en WhatsApp (nodes de ramos) | Kaiser: 35.423 adultos con diabetes o hipertensión; quien usó mensajería mejoró entre 2,0 y 6,5 puntos porcentuales en indicadores de control; diseño observacional (F-1221) | 🔵 B | **Probar.** Señal a favor, sin diseño causal |
| **Tener a mano mi historial** | NHS App (registros del médico de cabecera); OpenNotes (leer las notas del médico); Mapfre (historia clínica electrónica en app) | NHS: 20,8 millones de vistas de registros en un mes (F-1235). OpenNotes: 60% a 78% dice tomar mejor sus medicinas, pero es autoinforme y sin aleatorizar (F-1223). Intercambio de datos clínicos: evidencia de baja calidad de menos pruebas repetidas (F-1232) | 🔵 B / 🟡 C | **Sí, pero depende de que existan los datos conectados.** Es un problema de infraestructura y de alianzas con clínicas, no de app |
| **Pedir mis recetas y medicinas** | NHS App (recetas repetidas); Mapfre (entrega de medicinas) | NHS: 67,8 millones de recetas repetidas pedidas por la app en 12 meses (F-1235) | 🔵 B | **Sí.** Frecuente y simple. Es el uso más masivo del NHS App |
| **Saber cuánto voy a pagar** | Herramienta de precios de dos empleadores grandes de EE. UU. | La ofrecieron y la usó 10% en un año; el gasto ambulatorio subió US$ 59 (F-1233) | 🔵 B | **No como está.** Informar no basta si la persona no la usa o el precio no cambia su elección |
| **Entender qué cubre mi seguro** | Planes simplificados solo con copago (Humana, vía Penn); estudios de comprensión | Solo 14% entendía los cuatro conceptos básicos (deducible, copago, coseguro, máximo de bolsillo); con un plan solo de copagos hubo algo más de elecciones baratas (F-1225) | 🟡 C | **Probar con diseño del producto antes que con app.** Lo que se entiende es el copago |
| **Autorización previa de un procedimiento** | Norma de CMS en EE. UU. | 72 horas urgente y 7 días estándar desde 2026, con interfaces de datos desde 2027 (F-1234) | 🔵 B (norma) | **Sí donde hay regla y datos conectados.** En el Perú no hallé medida pública |
| **Cobrar un reembolso rápido** | Alan (Francia); Rímac anuncia "gestiona tus reembolsos" en su app | Alan: 90% en un día o 99% en un día, según la fuente; propio y sin auditar (F-1220). Rímac: solo el texto de la tienda de apps (F-1224) | 🔴 E / 🟠 D | **Plausible y valioso, sin evidencia independiente.** Hipótesis a medir en datos propios |
| **Seguir mi caso crónico** | Herramientas digitales para diabetes (Omada, Livongo, Virta y otras); navegación de atención (Navigate4Me) | Evaluación independiente (PHTI, 2024): beneficio clínico mínimo y de corto plazo, y mayor gasto; los proveedores objetan (F-1236). Navigate4Me: −14% hospitalizaciones por insuficiencia cardíaca, cifra de la propia empresa y sin grupo de control (F-1237) | 🔵 B / 🟠 D | **No hay base para prometer ahorro.** Probar con grupo de control |
| **Que me premien por cuidarme** | Vitality (Discovery), programas de bienestar de empleadores | Illinois: ensayo aleatorizado sin efecto en gasto ni salud (F-1218). Vitality: asociaciones con menos hospitalización, estudios vinculados a Discovery (F-1219) | 🟢 A / 🟡 C | **No como promesa de salud ni de ahorro.** Sí como herramienta de compromiso, si se mide aparte |

## 3. Casos concretos, uno por uno

Cada caso se separa por el tipo de evidencia. Las tres pistas no se mezclan.

### 3.1 Vitality (Discovery, Sudáfrica)

- **🔬 Empírica.** El estudio más citado (American Journal of Health Promotion, 2010) analizó a 948.974 afiliados de Discovery Health: los de alto compromiso (9,5% de la muestra) tuvieron menores costos de hospital, menos días de internación y menos ingresos que los no registrados (F-1219). Es **correlacional**: no distingue el efecto del programa de la selección de quienes ya eran más sanos. Hay además un estudio de cinco años con más de 300.000 afiliados que relaciona más visitas al gimnasio con menos hospitalizaciones; su cobertura viene de Discovery y de prensa. **No encontré una evaluación independiente ni un estudio de HealthyFood.**
- **Contraste independiente.** El ensayo aleatorizado de Illinois (Jones, Molitor y Reif, 2019) tampoco halló efectos en gasto médico, conductas, productividad ni salud autorreportada tras más de dos años, y mostró que los participantes gastaban menos antes de entrar (F-1218). Esto es **evidencia de otro programa, en otro país**: no prueba que Vitality falle, pero advierte que las asociaciones de Vitality pueden ser selección.
- **📈 Negocio.** No tengo cifras auditadas de Vitality en esta corrida. La literatura de negocio sobre Vitality (alianzas con aseguradoras en varios países) queda pendiente de leer.
- **Lectura.** Vitality es un caso de **compromiso con recompensas**, no una prueba de que el ahorro de salud exista. Es un buen caso para estudiar cómo se diseña el incentivo, y un mal caso para copiar su promesa de resultados.

### 3.2 NHS App (Inglaterra)

- **🔬 Empírica / oficial.** Datos de NHS England (diciembre de 2025): más de 39 millones de usuarios registrados; 70,5 millones de ingresos en octubre; 67,8 millones de recetas repetidas pedidas en 12 meses; 20,8 millones de vistas de registros del médico de cabecera y 6,6 millones de citas hospitalarias gestionadas en noviembre (F-1235). Son cifras de uso del propio servicio, no de resultados de salud.
- **Lectura.** Es un sistema público con identidad única y registros conectados. Su uso masivo se apoya en tareas frecuentes (receta, cita, ver el registro). **No es trasladable tal cual** a un seguro privado peruano, donde el registro vive en cada clínica.

### 3.3 Kaiser Permanente (EE. UU.)

- **🔬 Empírica.** Zhou y colegas (Health Affairs, 2010): entre 35.423 adultos con diabetes o hipertensión, el uso de mensajería segura con el médico se asoció con mejoras de 2,0 a 6,5 puntos porcentuales en indicadores de tamizaje y control (F-1221). Es observacional y las cifras las leí en cobertura de prensa.
- **Contexto.** Kaiser es a la vez aseguradora y prestadora, con historia clínica única. Eso **es lo que hace posible** el caso: la app solo conecta lo que ya está unido.

### 3.4 Alan (Francia)

- **📈 Negocio.** Más de 970.000 afiliados y 35.000 empresas; NPS de 66 (noviembre de 2025), frente a 70 en octubre de 2024 y 68 en abril de 2025; ingresos de más de 500 millones de euros en 2024, un 48% más (F-1220). Estas cifras son de su sitio y de una nota de prensa.
- **Dudas.** La promesa de reembolsos rápidos aparece como 90% en un día en una fuente y 99% en un día en otra. **No sé cuál es la correcta y ninguna es auditada.** Que el NPS baje entre tres mediciones (70, 68, 66) es un dato, no una explicación.
- **Lectura.** Alan es el ejemplo de **experiencia posventa como marca**: reembolso casi inmediato, app única. Sirve como hipótesis de lo que la gente valora, no como prueba de retención.

### 3.5 Ping An Good Doctor (China)

- **📈 Negocio.** Más de 14 millones de miembros del servicio de médico de familia a mediados de 2024, con calificación de cinco estrellas de más de 98% en consultas en línea, según la empresa; capacidad de atender hasta 4 millones de consultas por día con apoyo de IA (dato de 2025) (F-1222).
- **Dudas.** Las fuentes mezclan años, y la frecuencia de uso (5 veces por persona al año) aparece sin fecha. Son cifras de la empresa.
- **Lectura.** Muestra la integración de seguro, médico y servicio en un solo ecosistema. No dice si baja siniestros.

### 3.6 Oscar Health (EE. UU.)

- **📈 Negocio.** Cerró 2024 con unos 1,7 millones de afiliados, desde 1 millón un año antes; la dirección atribuye el crecimiento y la retención a la tecnología y la experiencia del afiliado; el índice de siniestralidad subió por ajustes de riesgo, no por uso (F-1227).
- **Lectura.** Es la afirmación de la empresa. **No hay evidencia independiente de que la experiencia digital cause la retención.**

### 3.7 Perú

- **📈 Negocio / documentos de empresa.** Mapfre lanzó su Clínica Digital en 2021 con autoevaluación de síntomas, videoconsulta y cita con especialista; sus planes de 2026 listan la app y el portal para historia clínica electrónica, medicinas a domicilio y chat médico (F-1224). EsSalud permite generar citas desde Mi Consulta en seis redes provinciales (F-1224). La app de Rímac anuncia búsqueda de clínicas, solicitud de asistencia vehicular, gestión de reembolsos y contenido de bienestar (F-1224).
- **Lo que no hallé.** Datos de uso, tiempos de reembolso, satisfacción o resultados de cualquiera de estas apps. Tampoco pude confirmar si hay seguimiento de siniestro o historial clínico en la app de Rímac más allá de lo que dice la ficha de la tienda.
- **Contexto institucional.** Los reclamos por coberturas de salud van a SUSALUD, no a la SBS; en seguros hubo 8.248 reclamos ante Indecopi entre 2019 y 2022 (F-1226); una ley uniformó en 15 días el plazo para atender reclamos de servicios financieros y de seguros (título de la norma, F-1226).
- **Comparación regional.** EPS Sura (Colombia) reporta que su sitio web concentra la mayor parte de las transacciones digitales (2,2 millones mensuales y 136 millones de visitas en 2024) y que WhatsApp también ofrece citas; a la vez, su informe de 2026 menciona quejas por retrasos en la asignación de citas (F-1228). Lo digital convive con el cuello de botella de la agenda real.

## 4. Pista de negocio: qué dice

- Las empresas muestran **uso masivo y satisfacción propia** (NHS App, Alan, Ping An, EPS Sura), no resultados de salud ni de costo.
- Donde hay evaluación independiente de herramientas con promesa de ahorro (diabetes digital, bienestar, precios), el resultado es **neutro o negativo en gasto** (F-1218, F-1233, F-1236). Los proveedores objetan con estudios propios y de plazo corto.
- Las cifras de velocidad (Alan) y de retención (Oscar) son **declaradas**.

## 5. Pista social: no se cubrió

Busqué quejas de asegurados en foros y redes en el Perú (reembolsos, autorizaciones, apps) y no encontré hilos útiles. Lo más cercano son registros administrativos (reclamos ante Indecopi y SBS) y notas de prensa sobre caídas de sistemas en Colombia (EPS Sura). **Eso no equivale a una pista social.** La conclusión de este node sobre qué duele más al asegurado peruano no está respaldada por voces directas. Para cubrirla haría falta acceso real a foros, reseñas de tiendas de apps y redes, o el uso de la biblioteca de reclamos de la SBS y Susalud.

## 6. Síntesis: dónde convergen y dónde no

- **Convergen** en que lo digital funciona mejor en tareas **frecuentes, simples y con capacidad física detrás** (recordatorio, receta repetida, cita). Aquí coinciden la evidencia (metaanálisis de recordatorios), el uso masivo (NHS App) y el negocio (EPS Sura, Mapfre).
- **Divergen** en los programas que prometen **cambiar conducta o bajar gasto**: las empresas muestran compromiso y asociaciones favorables; la evidencia independiente no encuentra efecto en gasto o salud. Tensión sin resolver: es probable que haya un valor de **experiencia y retención** que no se mide como ahorro.
- **Brecha de equidad.** Portales y autoagendamiento los usan primero personas más jóvenes, con más ingresos y con seguro comercial (F-1230, F-1231). En el Perú, donde el acceso digital es desigual, esto pesa más. Hace falta canal asistido.
- **Lo que mueve la aguja no es la app.** Lo que habilita el valor es que haya **datos conectados** (historial entre clínicas), **agenda real**, y **reglas de servicio** (plazos) que se puedan publicar y exigir. Eso ya aparecía en el ciclo: digital en los bordes, valor en el medio.

## 7. Hipótesis para probar con datos propios

| # | Hipótesis | Cómo probarla |
|---|---|---|
| PV1 | Dos o más recordatorios de cita (SMS o WhatsApp) bajan la inasistencia más que uno | Prueba aleatoria por clínica, midiendo inasistencia |
| PV2 | El autoagendamiento sube la inasistencia o la cancelación entre quienes agendan por canal digital (compromiso más bajo) | Comparar inasistencia y cancelación por canal de agendamiento |
| PV3 | Un canal asistido (llamada o WhatsApp con persona) cierra la brecha de uso entre personas mayores y jóvenes | Medir uso y resolución por edad antes y después |
| PV4 | Publicar el tiempo promedio de reembolso y autorización (compromiso verificable) sube la confianza más que un mensaje de marca | Prueba A/B de mensaje, con medición de confianza y renovación |
| PV5 | Ver el historial integrado (recetas, exámenes, citas) en un solo lugar reduce exámenes repetidos | Comparar exámenes repetidos entre usuarios con y sin historial integrado |
| PV6 | La barrera mayor del historial integrado en el Perú es la alianza con clínicas, no el desarrollo de la app | Entrevistas con clínicas y revisión de la norma de historia clínica electrónica |
| PV7 | Un incentivo de bienestar tipo Vitality atrae a quienes ya cuidan su salud y no mueve a quienes no | Comparar el perfil de ingreso y el cambio de conducta con grupo de control |
| PV8 | Un plan solo con copagos se entiende mejor que uno con deducible y se asocia con menos consultas postergadas | Comprensión medida con preguntas de verificación y datos de uso |
| PV9 | Mostrar el precio antes de elegir clínica sube la elección de opciones baratas solo si el costo de bolsillo varía de forma visible | Prueba A/B de información de costo de bolsillo en el buscador de clínicas |
| PV10 | La queja principal del asegurado peruano posventa es la autorización previa y no el reembolso | Clasificar los reclamos por tipo en la base de la aseguradora y en los registros públicos |

## 8. Limitaciones

- Todo es **N2**: fragmentos de buscador. Las cifras de portales, OpenNotes, Kaiser y la norma de EE. UU. vienen de resúmenes y prensa; no abrí los artículos originales. Para citar una cifra puntual hay que verificarla en el original.
- Varios autores y años no estaban visibles en los fragmentos (metaanálisis de recordatorios, revisiones de portales); los dejé sin nombre y con el enlace.
- **Pista social sin cubrir.** No sé qué dice la gente en redes sobre estos servicios en el Perú.
- Casi toda la evidencia es de **EE. UU., Reino Unido, Sudáfrica y China**, con sistemas de salud distintos del peruano. No hay estudio causal en seguros peruanos.
- No hallé evidencia pública de **uso o resultados** de las apps peruanas (Mapfre, Rímac, EsSalud, Sanna). Que no aparezcan no prueba que no existan datos internos.
- El énfasis en lo que no tiene respaldo **no significa que no haya oportunidad**: significa que la oportunidad está sin medir.

## Conexiones

- [[digitalizacion-ramos-vehicular-salud-microseguros|Digitalización por ramo]] — teleconsulta, triaje, farmacia, navegación y WhatsApp (§15): aquí se amplía a los dolores posventa.
- [[seguros-embebidos-insurance-as-a-service|Seguros embebidos e Insurance-as-a-Service]] — otros terrenos más allá del seguro (§10) y la diferencia entre distribuir y servir.
- [[digitalizacion-seguros-mercados-emergentes|Digitalización en seguros en mercados emergentes]] — defaults, automatización y qué se digitaliza en etapas.
- [[economia-conductual-seguros-literatura|Economía conductual de los seguros]] — comprensión del producto, atributos ocultos y por qué la gente compara poco.
- [[mecanismos-seguros-salud|Mecanismos de seguros de salud]] — Vitality, Kaiser, capitación y modelos que navegan la presión de costos.
- [[lealtad-gamificacion-recompensas-retail|Lealtad, gamificación y recompensas]] — qué efecto demostrado tienen los incentivos fuera del seguro.
- [[economia-plateada-seguros-peru-latam|Economía plateada]] — acceso digital de personas mayores y necesidad de canal asistido.
- [[conducta-humano-ia|Conducta humano-IA]] — confianza y descarga cognitiva en asistentes de salud.
- [[foresight-experiencia-futura-seguros-digitalizacion|Foresight de la experiencia futura]] — dónde vive la relación con la persona.
