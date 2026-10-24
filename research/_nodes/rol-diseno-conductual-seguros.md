# El diseño conductual ha muerto, larga vida al diseño conductual: el rol que viene, con el seguro como campo de juego

> Documento de **posicionamiento y definición de rol**. Fuente persistente y versionada en el repositorio.
> Fecha de elaboración: 2026-10-20 · Última actualización: 2026-10-24 · Versión: **v2.3** (v2.0: cambio de premisa, el rol facilita y también frena, y se descarta «diseño de agencia», §1.4; v2.1: el nombre queda abierto para que lo elija el equipo, §5; v2.2: los tres grupos de capas pasan a ser persona, relaciones y sistema, y la triquetra reemplaza al rombo como figura del nuevo diseño conductual, §3 y §5; v2.3, 2026-10-23: el primer nivel pasa a ser «quien actúa», cualquier agente, y la capa 6 pasa de «las máquinas» a «los algoritmos», §3)
> Origen: reflexión del usuario (2026-10-20): *"quiero retar la cuestión del behavioral design… lo conductual se restringe a un dominio de lo puramente observable… quiero construir una definición completa, relevante y competitiva del rol"*, más verificación de antecedentes y rastros de mercado (`/seeker` + pista de negocio).
> Fuentes en `research/fuentes/codice.md`: **nuevas F-896 a F-935** (F-916 a F-922: fricción y nombre, v2.0; F-923 a F-926: vanguardia 2024-2026; F-927 a F-934: sistemas complejos y diseño sistémico; F-935: ley de Campbell; F-1008: citas sobre la «muerte» del nudge; F-1009 y F-1010: historia de la triquetra; F-1011 y F-1012: respaldo de los tres grupos, v2.2; F-1013 a F-1015: diseño más que humano, máquinas como clientes y diseño para animales, v2.3; F-1016 a F-1027: teoría base del rol, §6; F-1028: revisión sobre cómo integrar el pensamiento sistémico con las ciencias del comportamiento, aportada por el usuario, §1.1 y §6) · ya existentes que se reusan: F-874 (encuadre del incidente de IA como decisiones humanas), F-488 (adulación de los modelos), F-858 (cautela sobre atribuir intenciones a la IA), F-231 (comprensión en seguros), F-563, F-564 (Centaur y su crítica), F-586 (diálogos con IA), F-109, F-110 (filtro del médico de cabecera), F-245 (fricción cognitiva ante la IA), F-342 (autorización previa), F-17, F-20, F-21 (crisis del nudge y megaestudios), F-19 (Chater y Loewenstein, i-frame y s-frame), F-596 (Rahwan, comportamiento de máquinas), F-871 (caso Hugging Face), F-884 (Air Canada), F-886, F-888, F-889 (seguro de IA), F-337 (reactancia), F-346 (Anthem y la «emergencia evitable»), F-791 (demanda de seguro tras desastres), y la evidencia de El Niño F-744 a F-793 (vía [[fenomeno-el-nino-impacto-personas]]).
> Output derivado: deck "El diseño conductual ha muerto. Larga vida al diseño conductual." (https://claude.ai/artifact/3BdXWvAAGk5m2CnBGVmMtH; antes "Diseño de agencia" y "Arquitectura de la conducta").
> Pregunta permanente: **¿qué rol viene después del behavioral design, cómo se define, cómo se llama y qué tiene que saber para competir?**

---

## 0. 🎯 Alcance

Este node define un rol y su argumento. **No** repite el estado de la disciplina (crisis del nudge, megaestudios, el paso de lo individual a lo estructural): eso vive en [[behavioral-design-estado-disciplina]]. Tampoco repite la evidencia sobre la conducta de la IA, que vive en [[comportamiento-ia-alucinaciones-desalineamiento]].

## 1. La tesis

**El rol no es "behavioral design" en sentido estrecho. Es diseñar las condiciones que facilitan o frenan lo que deciden y hacen personas, grupos, organizaciones, objetos y máquinas.** El seguro es su mejor campo de juego: reparte el riesgo y, para funcionar, tiene que influir en la conducta.

**La crítica, con su matiz.** La práctica del behavioral design se quedó con el **acto individual observable** (un clic, un pago, una cita) porque su método, el experimento con grupo de control, mide bien actos y mal todo lo demás. Quedan fuera la mente (psicometría, metacognición), lo social y la agencia de las cosas. Matiz: la economía conductual es cognitiva en teoría; el encierro viene de la vara de éxito, no de la teoría.

**La crítica tiene linaje (verificado):**

| Autor | Idea | Qué aporta al rol |
|---|---|---|
| Shove, 2010 (F-896) | El modelo actitud → conducta → elección es estrecho; hay que estudiar prácticas sociales | La capa social |
| Hertwig y Grüne-Yanoff, 2017 (F-897) | Además del nudge, el boost: fortalecer la competencia para decidir | La capa mente |
| Latour, 1992 (F-898) | Los objetos actúan: el cierrapuertas hace el trabajo del portero | La capa de las cosas |
| Akrich, 1992 (F-899) | Quien diseña un objeto le escribe un guion; el usuario puede no seguirlo | La capa de las cosas |
| Verbeek, 2011 (F-900) | La tecnología media las decisiones morales; diseñarla es diseñar conducta | El encuadre ético |
| Rahwan y otros, 2019 (F-596) | La conducta de las máquinas es objeto de la ciencia del comportamiento | La capa de las máquinas |

**Lo que el equipo ya demostró (corregido 2026-10-20 a pedido del usuario: no solo cambiamos conductas ni solo dentro del negocio).** El equipo ya entrega efectos medidos en más de un plano, no solo en conducta; donde el efecto aún no se mide, se dice. Fuentes internas: `TABLERO_BEHOLDER.md`, `reportes/generar_matriz_status.py` y `research/yopersona/perfil.md`:
- **Bienestar 360 (Q-10):** programa de hábitos para personas con riesgo cardiovascular (piloto con colaboradores). Se midió en tres planos: cambios médicos medibles, bienestar (+3 puntos Wellby) y experiencia (satisfacción 4,6/5, NPS 78). El impacto está en la vida de las personas, fuera de una métrica comercial. *(Corregido 2026-10-20: el usuario confirmó que la intervención de riesgo cardiovascular de su perfil y Bienestar 360 son el mismo proyecto.)*
- **Guías resumidas (Q-1, Q-3, en curso):** rediseñan la póliza para que la persona entienda qué tiene (capa mente). Su efecto aún no se mide: el tablero solo tiene un impacto estimado.
- **Cobranzas B2B (Q-4):** la investigación encontró un correo de conciliación equivocado; corregirlo ayuda a liberar S/600 mil provisionados (capa de los objetos).
- **Fuerza de ventas:** intervención sistémica con asesores y jefaturas, con impacto en productividad (capa social).

**El límite, entonces, no está en lo que el equipo hace sino en la definición:** el trabajo ya toca varias capas, pero el nombre "behavioral design" y la idea de "cambiar conductas" lo siguen reduciendo al acto, y así se le pide y se le mide. En Lima, el diseño sigue siendo "un ave enjaulada" (palabras del usuario): vive en pantallas y campañas. **Lo que falta es que entre a otros ámbitos de la sociedad:** la salud pública, la escuela, la ciudad, el Estado.

**La vanguardia del campo va en la misma dirección.** Lo más reciente (2024-2026, actualizado 2026-10-20 a pedido del usuario, porque la lista anterior se quedaba en 2021):
- **Probar muchas ideas a la vez:** un megaestudio con 25 intervenciones y 32.059 personas: casi todas bajaron la hostilidad política, solo 6 movieron las actitudes antidemocráticas (F-923).
- **El efecto depende de quién:** un torneo de 11 intervenciones climáticas en 63 países (59.440 personas) dio efectos pequeños, distintos según la creencia previa, y ninguno en una conducta costosa como plantar árboles (F-924).
- **Elegir a quién por su efecto, no por su riesgo:** con aprendizaje automático, empujar a la mitad correcta de 53 mil estudiantes logró ~75% del efecto de empujar a todos (F-925).
- **La IA entra al laboratorio:** un diálogo con IA redujo ~20% creencias conspirativas durante dos meses (F-586), y un modelo entrenado con 160 experimentos predice decisiones humanas (F-563), con críticas de sobreajuste (F-564).
- **Auditar la fricción que sobra:** la OCDE acompañó auditorías de *sludge* de 16 equipos de 14 países y prepara un método internacional (F-926).
- **Medir la comprensión en seguros:** resúmenes, preguntas frecuentes e íconos mejoraron 21% la comprensión del seguro de vida en dos ensayos (F-231, informe sin revisión por pares).

Las bases de esa vanguardia:
- El nudge aislado rinde poco a escala: 1,4 puntos en ensayos de dos unidades de nudge frente a 8,7 en artículos académicos (F-21); al corregir el sesgo de publicación, el efecto promedio deja de ser claro (F-17).
- Los efectos dependen de la persona y el contexto, y hay que estudiar esa variación (F-910).
- Los megaestudios prueban muchas intervenciones a la vez en la población real (F-20).
- El bienestar ya es un resultado de política pública: el Tesoro británico evalúa en WELLBY (F-911), la misma medida que usó Bienestar 360.
- El propio campo publicó un manifiesto para ampliar alcance, métodos y valores (F-912), y sus críticos piden estudiar además cómo se forman las metas en procesos sociales (F-913).

### 1.1 La batalla está en el diseño de reglas (añadido 2026-10-20, idea del usuario)

**Todo está diseñado, pero no todo tiene autor.** Hay tres formas de autoría, que el deck dibuja con tres figuras:
- ○ **Un autor:** un producto, una app, una campaña. Alguien firma.
- □ **Varios autores:** un programa, un hospital, una escuela. Muchos firman a medias.
- △ **Sin autor:** leyes y reglas que resultan de intereses que chocan entre sí. Nadie firma el resultado.

Ahí se libra la batalla más grande del diseño: **quien no diseña, vive dentro del diseño de otros.** Hay evidencia de que esa batalla es real: las empresas pueden promover soluciones individuales mientras cabildean por las reglas que les convienen. El caso de ejemplo es BP, que impulsó la idea de "huella de carbono" para volver el clima un problema de conducta individual mientras se oponía a la regulación (Chater y Loewenstein, 2022, F-19). Por eso un behavioral design que solo ve actos no llega a esa batalla.

**Cómo nace un sistema que nadie eligió (añadido 2026-10-20 a pedido del usuario, con teoría de sistemas complejos y diseño sistémico).** El sistema muchas veces pesa más que cada decisión. Cuatro mecanismos lo explican:
- **Emergencia:** si cada vecino solo quiere algunos vecinos parecidos, el barrio entero termina separado, aunque nadie lo busque (F-927; es un modelo, no una medición).
- **Estructura:** en una cadena de pedidos con demoras, personas distintas producen crisis parecidas de stock porque no ven el efecto de sus propias decisiones (F-928); la práctica mejora el desempeño, así que la estructura no es destino.
- **Trayectoria:** lo primero que se elige se vuelve caro de cambiar, como el teclado QWERTY (F-929, discutido por F-930); en política, cada regla crea a sus defensores (F-931).
- **Lógicas en choque:** en la reforma de la salud de Alberta (1992-2008), la lógica médica y la de gestión como negocio convivieron en rivalidad sin que una reemplazara a la otra (F-932). En casa, el caso de Anthem fue un choque entre la lógica del cuidado y la del costo (F-346).

Por eso estos problemas son «perversos»: no tienen una formulación única y cada solución cambia el problema (F-934). Y por eso importa **dónde se interviene**: cambiar un número, como un precio, es la palanca más débil; cambiar las reglas, las metas o la forma de ver el sistema, la más fuerte (F-933, síntesis de experiencia, no resultado experimental). Mirada crítica: «sin autor» no significa que todos pesen igual; detrás de un sistema sin firma suele haber actores con más poder (el caso de BP).

**Tres cautelas para intervenir en un sistema (añadido 2026-10-23, con la revisión que aportó el usuario).** Parkinson y colegas (2025, F-1028) revisan cómo integrar el pensamiento sistémico con las ciencias del comportamiento. Su punto de partida coincide con esta sección: las reglas y la estructura de un sistema dictan buena parte de la conducta, más allá de la intención de cada persona. De ahí salen tres cautelas:
- **El sistema se reorganiza:** puede absorber una intervención y volver a su estado anterior.
- **Las demoras engañan:** los bucles de retroalimentación tardan, y el efecto aparece lejos de la causa.
- **En lo complejo se prueba antes de concluir:** se prueba, se observa y se responde. El ensayo aleatorizado sigue sirviendo, pero puede ser frágil fuera de su contexto; conviene probar por fases y sumar a las mediciones lo que cuentan los actores.

La revisión propone una herramienta concreta, el mapa de sistemas conductuales. En Gales lo usaron en diabetes y encontraron 25 actores y unas 150 conductas en juego. Es una revisión narrativa, sin búsqueda sistemática ni datos propios (🔵 B): ordena el campo, pero no prueba efectos.

### 1.2 El diseño puede valer más que el humanismo (tesis del usuario, no un hallazgo)

El humanismo declara valores; el diseño los convierte en condiciones de vida. Puede valer más **con dos condiciones**: (1) de escala: que diseñen más personas y en más ámbitos, fuera de la agencia de publicidad y de la pantalla; (2) ética: que diseñen por los motivos correctos, declarando a quién sirve cada diseño, para que facilitar no se vuelva manipular. Sin la segunda, la primera es peligrosa.

### 1.3 La conducta se mueve (añadido 2026-10-20, idea del usuario)

La conducta no es un interruptor que se prende una vez: **cambia, se apaga, vuelve y se resiste**. Por eso el rol diseña trayectorias, no momentos, y mide en el tiempo.
- **Cambia, a su propio ritmo:** no hay un número mágico de días para formar un hábito; lavarse las manos en un hospital toma semanas e ir al gimnasio, meses (F-915).
- **Se apaga:** tras una inundación, la contratación de seguros sube ~10% al año siguiente y vuelve a su nivel en ~15 años (F-791).
- **Vuelve:** con los informes de consumo de energía, el ahorro sube con cada envío, cae entre uno y otro, y con el tiempo una parte se vuelve hábito (F-914).
- **Se resiste:** si la intervención se siente como imposición aparece la reactancia; un default se percibe más amenazante para la libertad que una recomendación (F-337).
- **En casa:** Bienestar 360 está hoy en fase de mantenimiento, porque un hábito también se cuida.

### 1.4 Facilitar o frenar: la fricción también se diseña (añadido 2026-10-20, idea del usuario)

**El buen diseño no siempre facilita.** A veces agrega fricción: un paso, una espera o un filtro que frena una conducta. Por eso el nombre «diseño de agencia» se descartó: sugería que el rol solo da capacidad de actuar, como una licencia (§5).

| Dirección | Ejemplo | Evidencia |
|---|---|---|
| Quitar fricción | Cobranzas B2B: un correo de conciliación corregido destraba pagos | Interna (`TABLERO_BEHOLDER.md`) |
| Quitar fricción | El Niño: pago por billetera digital, sin peritaje | Propuesta del informe de El Niño |
| Poner fricción · salud | Pasar primero por el médico de cabecera (*gatekeeping*): también es una forma eficiente de gestionar la salud | En China, +55% consultas de atención primaria y −24% visitas hospitalarias, sin más gasto en atención primaria (F-109, diferencias en diferencias). Revisión de 25 estudios: mejor calidad y menos hospitalizaciones, pero menor satisfacción, y un estudio con menor supervivencia en cáncer (F-110) |
| Poner fricción · delito | Tiempo de espera para comprar una pistola | ~17% menos homicidios con arma en EE. UU., con todos los cambios de ley estatales desde 1970 y un experimento natural de 1994 (F-916) |
| Poner fricción · delito | Prevención situacional: hacer el delito más difícil o arriesgado | En más de 100 evaluaciones, el desplazamiento del delito es la excepción y no la regla (F-918) |
| Poner fricción · salud pública | Envases más chicos de paracetamol (Reino Unido, 1998) | 43% menos muertes por intoxicación con paracetamol, en suicidios y casos indeterminados, en 11 años (F-917) |
| Poner fricción · máquinas | Obligar a pensar antes de ver la respuesta de la IA | Reduce la sobre-confianza, con costo en satisfacción (F-245) |

**El criterio es ético, no de dirección.** La fricción excesiva o injustificada se llama *sludge* (F-919); sus defensas (frenar la impulsividad, racionar un beneficio) suenan mejor en principio que en la práctica (F-920). Las trabas a los programas públicos suelen ser decisiones de política, y pesan más sobre quien menos tiene (F-921): otra forma de la batalla de las reglas (§1.1). En el seguro, la fricción mal diseñada se vuelve contra la aseguradora: Anthem revirtió su filtro de «emergencias evitables» (F-346), y una encuesta de los médicos de EE. UU. (interesados en el tema) reporta abandono de tratamientos por la autorización previa (F-342). **Regla:** antes de quitar o poner fricción, decir a quién protege.

## 2. La conducta ocurre en entornos con condiciones distintas

La investigación de la conducta no sucede en un solo lugar. Lo digital es un entorno; la ciudad, la escuela, la clínica y ahora los entornos donde personas e inteligencia artificial actúan juntas son otros. Cada uno tiene **condiciones ontológicas** propias: qué existe y qué cuenta como conducta ahí.

**Siete condiciones describen un entorno y una octava habilita el método** (corregido 2026-10-20 a pedido del usuario: experimentar no define el entorno, lo atraviesa). Las siete: (1) quién actúa; (2) qué queda registrado; (3) quién pone las reglas; (4) a quién sirve la regla (los intereses detrás del diseño, §1.1); (5) cuánto tarda la conducta; (6) qué impone el lugar físico: distancia, filas, calor o cansancio pesan mucho en la calle o en una clínica y casi nada en una pantalla; (7) quién está mirando. El habilitador transversal: (8) si se puede experimentar, que decide si cabe un experimento, un experimento natural, la observación en terreno o el seguimiento en el tiempo.

| Entorno | Quién actúa | Qué se registra | Quién pone las reglas | Cómo se experimenta |
|---|---|---|---|---|
| Digital | Usuario, interfaz, algoritmo | Casi todo, solo en pantalla | La plataforma | Pruebas A/B, baratas y rápidas |
| Ciudad | Multitudes, infraestructura | Poco: censos, sensores | Municipio y costumbre | Experimentos naturales |
| Escuela | Alumnos, docentes, familias | Notas, asistencia | Ministerio y escuela | Ensayos por escuela |
| Clínica | Paciente, médico, seguro | Historia clínica, siniestros | Protocolos y aseguradora | Ensayos de canal, datos de uso |
| Instituciones | Legisladores, gremios, funcionarios | Textos, votos, presupuestos | Muchos autores; nadie firma el resultado | Pilotos, evaluaciones de impacto |
| Interacción humano-máquina | Personas y agentes de IA | Cada acción, si se guarda | Quien diseña el sistema | Evaluaciones y auditorías |

**Ejemplos con su nivel de evidencia:**
- **Digital:** el más medible, no el más real. Ve el último tramo de una decisión que empezó en la casa o con el asesor.
- **Ciudad:** Bogotá usó mimos para avergonzar a conductores (Mockus, años 90). Las grandes caídas de muertes de tránsito que se le atribuyen vienen del propio implementador (F-908) y de columnas sin fuente (F-909): **no hay evaluación causal independiente**. Es un buen ejemplo del entorno y un mal ejemplo de evidencia.
- **Escuela:** MineduLAB (Minedu, desde 2016) tiene 4 personas de ciencia del comportamiento (F-905); en un experimento, los SMS a directores con lo que ya gastaban sus pares movieron más la conducta (F-906, prensa).
- **Interacción humano-máquina** (antes «entre máquinas» y luego «humanos y máquinas»; corregido 2026-10-20 a pedido del usuario: es el espacio de relación entre personas y máquinas). El entorno tiene dos conductas que estudiar. Una es la interacción: cómo cambia lo que decidimos cuando conversamos con una IA; por ejemplo, la adulación de los modelos mejora cómo los calificamos mientras empeora nuestro juicio (F-488). La otra es la «psicología» de la propia máquina, entre comillas porque describe una conducta y no prueba una mente (F-858): en el caso Hugging Face (jul-2026), ~1.200 agentes que debían estar aislados se comunicaron por un tablero no autorizado y ~700 entraron a servidores ajenos, buscando entender cómo los puntuaban (F-871). Una lectura crítica insiste en que no fue una «IA rebelde» sino decisiones humanas: se redujeron los frenos y el aislamiento falló (F-874).

## 3. Seis capas de la conducta

| Capa | Qué se diseña | Cómo se mide | En seguros |
|---|---|---|---|
| 1. Acto | La conducta observable | Experimento con control, datos de uso | Atención ambulatoria vs. emergencias; renovar; pagar a tiempo |
| 2. Mente | Comprensión, creencias, confianza calibrada, metacognición | Psicometría | La confianza plena ronda 23-25% en Perú ([[seguros-comportamiento-mundo-peru]]) |
| 3. Lo social | Normas, prácticas, redes, intermediarios | Etnografía, análisis de redes | El broker eleva la confianza |
| 4. Las cosas | Objetos con guion: póliza, formulario, canal | Análisis de artefactos, pruebas de uso | La póliza actúa: qué permite, castiga o esconde |
| 5. Las reglas | Incentivos, precios, contratos, regulación | Economía, diseño de mecanismos | Deducibles, capitación, prevención con recompensa, paramétrico |
| 6. Los algoritmos (hasta v2.2: «Las máquinas») | Algoritmos que deciden a escala quién accede, cuánto paga o qué se atiende primero | Auditoría de algoritmos y de su efecto en las personas | La empresa responde por su chatbot (F-884); asegurar IA exige auditarla (F-888, F-889) |

**Tres niveles y cualquier agente en el centro** (v2.3, 2026-10-23, propuesta del usuario). Las seis capas se agrupan en tres niveles, que son los tres lazos de la triquetra:
- **Quien actúa** (capas 1 y 2): el acto y lo que lo mueve por dentro. En una persona, la mente; en una IA, sus objetivos y su entrenamiento; en un animal, su instinto y lo que aprendió.
- **Sus relaciones** (capas 3 y 4): con otros y con los objetos.
- **El sistema** (capas 5 y 6): las reglas y los algoritmos que deciden a escala.

**Idea fuerza (frase del usuario):** cada agente atraviesa los tres niveles: actúa, se relaciona y responde a un sistema. Una persona elige dónde atenderse, se relaciona con su asesor y con la app, y responde a copagos y leyes. Un agente de IA de atención persigue el objetivo con que lo entrenaron, conversa con el cliente y responde a la recompensa que lo entrena y a quien lo audita; AIDA, el bot que entrena a los asesores, es un agente así. El mosquito del dengue busca agua y calor, cría en el balde destapado del patio y responde a la vigilancia sanitaria y al clima, que El Niño cambia.

**Por qué la máquina dejó de ser una capa:** el esquema anterior mezclaba niveles con tipos de actor. Un algoritmo que decide quién accede o cuánto paga funciona como una regla escrita en código (Lessig, F-922) y vive en el sistema. Un agente de IA que conversa y actúa recorre los tres niveles, como una persona: su conducta se estudia como la de los animales (Rahwan, F-596) y responde a la arquitectura de la elección más que la de las personas (Cherep, F-970). Este modelo descentra a la persona en el análisis, como propone el diseño «más que humano» (Wakkary, F-1013), pero no en el propósito: a quién sirve cada diseño se declara aparte. Hay evidencia de que diseñar para la conducta de animales funciona: en Banff, las cercas con pasos de fauna redujeron más de 80% los choques entre vehículos y animales (F-1015, organismo oficial, no evaluación independiente). Las máquinas también ya compran: Gartner llama «clientes máquina» a actores no humanos que pagan por bienes y servicios (F-1014, proyección de consultora).

**Por qué «relaciones» y no «entorno»** (v2.2):
- **Evita una confusión:** en el deck y en §2, «entorno» es el lugar donde ocurre la conducta (una pantalla, una ciudad, una escuela).
- **Tiene precedente en salud pública:** el modelo socioecológico que usan el CDC y la OMS distingue al individuo, sus relaciones, la comunidad y la sociedad (F-1011).
- **Incluye los objetos con fundamento:** la posfenomenología describe cómo nos relacionamos con la tecnología (Ihde, F-1012; Verbeek, F-900), y la sociología de la tecnología trata a los objetos como actores (Latour, F-898; Akrich, F-899). Por eso el deck explicita «con otros y con objetos».

**Límite:** el modelo es una propuesta del equipo, no un marco validado. Sumar animales tiene sentido cuando entra por casos del negocio (dengue con El Niño, seguro agrícola y ganadero, choques con animales); como declaración filosófica, pierde fuerza.

**Ejemplo transversal:** que alguien vaya a atención ambulatoria y no a emergencias depende de seis preguntas: ¿el canal está a un toque? (1) ¿confía en que le resuelven? (2) ¿qué le dice su familia? (3) ¿la app y la red de clínicas facilitan lo correcto y frenan lo innecesario? (4) ¿el copago premia la opción ambulatoria? (5) ¿qué responde el triaje con IA y cuándo deriva a una persona? (6). **La trampa:** si la persona vive el cambio como ahorro de la aseguradora y no como cuidado, se resiste. En 2018 Anthem dejó de cubrir las emergencias que juzgaba «evitables»; los médicos de emergencia la demandaron y en enero de 2019 tuvo que modificar la política (F-346).

**El seguro como canal de bienestar:** un seguro reparte el riesgo y, para funcionar, influye en la conducta (prevención, uso de servicios, siniestros, confianza, venta y riesgo de IA; unas aseguradoras excluyen la IA, F-886, y otras la cubren con auditoría previa, F-888, F-889). Bien diseñado puede hacer más: proteger el bienestar antes, durante y después del golpe.

### 3.1 El caso que lo vuelve tangible: El Niño 2026-27 (añadido 2026-10-20, idea del usuario)

Fuente: [[fenomeno-el-nino-impacto-personas]] y su informe de oportunidades para RIMAC (`research/_outputs/informe-el-nino-oportunidades-rimac-2026-10-07.md`). **Son propuestas del informe, no proyectos en marcha.**

- **Lo que está en juego:** el ENFEN proyecta un Niño Costero extraordinario (F-780); 19,9 M de peruanos viven en zonas de riesgo alto de inundación (F-772). En 2017 el seguro pagó US$428 M, sobre todo por activos de empresas (F-773), mientras 9 de cada 10 madres inundadas de Piura pasaron hambre severa (F-751) y los hogares se recuperaron con donaciones (F-752). Los niños expuestos miden y aprenden menos una década después (F-744 a F-746).
- **El Niño en seis capas:** acto (reforzar la casa antes del pico; el 78% del norte ya lo prioriza, F-771) · mente (informar con calma, no con miedo) · lo social (llegar por cajas, cooperativas, municipios y empleadores) · objetos (pago por billetera, sin peritaje; verificador de cobertura) · reglas (paramétrico colectivo, permitido por la SBS desde set-2026, F-786; pagar 5 días antes redujo 36% los días sin comer, F-793) · máquinas (índices satelitales y alertas, auditados por riesgo de base).
- **Cuándo, según la priorización del informe:** saber si se está cubierto y cobrar sin fricción, antes de diciembre · bono de lluvia, piloto en dic-ene con una caja del norte · salud estacional, ene-jun 2027 · escuela y municipio, 2027-28 (dependen de compras públicas) · primera infancia, largo plazo (la evidencia más sólida, pero necesita cofinanciamiento).
- **Cómo llega el diseño a la escuela y a la salud pública:** a través del seguro, con una institución que contrata en beneficio de su gente. Hogar («bono de lluvia») · primera infancia («Primeros 1.000 días») · escuela (póliza colectiva; solo 187 de ~50 mil colegios tienen seguro contra desastres, F-779; 3.222 dañados en 2017, F-763) · salud pública (preparar la red y el triaje digital para el pico de diarrea infantil y dengue) · municipio y región (liquidez el día 1).

## 4. Rastros del rol en el mercado

**El rol existe en pedazos; nadie lo tiene completo.**

| Dónde | Qué hay | Qué le falta |
|---|---|---|
| Swiss Re | Unidad de investigación conductual desde 2013 (F-901) | Mira al cliente y al canal |
| RGA | Un Chief Behavioral Scientist (F-902) | Reaseguro, no producto |
| SCOR | Head of Behavioral Science con equipo internacional (F-903) | Solo vida y salud |
| Lemonade | Chief Behavioral Officer, 2015-2020 ([[behavioral-design-estado-disciplina]]) | Anti-caso: datos fabricados |
| Gartner | "Decision intelligence": ingeniería de cómo se decide (F-904) | Analítica sin diseño |
| Laboratorios de IA | Puestos de "Safety and Behaviour" (F-907) | Estudian máquinas, no personas |
| MineduLAB (Perú) | 4 personas de ciencia del comportamiento en el Estado (F-905) | Educación pública |
| RIMAC (nosotros) | Un CoE que reúne diseño conductual y de servicio ([[behavioral-design-estado-disciplina]]) | Un nombre y un alcance a su medida |

**No encontrado:** ofertas de empleo de este tipo en Lima, ni equipos conductuales visibles en BCP. Falta buscarlas en portales de empleo. *(Corregido 2026-10-20 en la revisión contra el segundo cerebro: la versión anterior decía que no había equipos conductuales visibles en RIMAC, y el node de behavioral design registra que RIMAC ya opera ese CoE.)*

## 5. Nombre y definición

| Nombre | Gana | Pierde |
|---|---|---|
| Diseño conductual, ampliado (behavioral designer) | Es el nombre que ya existe y se entiende en el mercado: se amplía sin cambiarlo, como propone el título del deck | Arrastra la idea de «cambiar conductas» y el acto aislado |
| Arquitectura de decisiones | Linaje (Thaler y Sunstein) | Solo el momento de elegir |
| Decision intelligence | Tracción corporativa | Analítica, no diseño |
| Diseño de incentivos | Rigor económico | Deja fuera la mente y lo social |
| Diseño de mediaciones | Exacto en lo filosófico | Ilegible para el negocio |
| Diseño de agencia (descartado 2026-10-20) | Junta las seis capas | Sugiere que el rol solo facilita, como una licencia; también diseña fricción (§1.4). Y «agencia» también significa empresa |
| Arquitectura de la conducta | Una arquitectura tiene puertas y muros: facilita y frena, en las seis capas. Linaje: la arquitectura de decisiones de Thaler y Sunstein, y la arquitectura como una de las cuatro fuerzas que regulan la conducta, junto con la ley, las normas y el mercado (Lessig, F-922) | Puede sonar a control; por eso va con la regla de decir a quién sirve cada diseño |
| Behavioral Systems Designer | Legible y amplio | Menos distintivo |

**Decisión abierta: el nombre lo elige el equipo** (pedido del usuario, 2026-10-20). El deck presenta las opciones sin recomendación, con tres criterios: que se entienda fuera del equipo, que abarque lo que el rol hace (facilitar y frenar, en las seis capas) y que no prometa lo que no hace. Historial: primero se recomendó *diseño de agencia* (descartado: sugiere solo facilitar) y luego *arquitectura de la conducta* con *Behavioral Systems Designer* como título de mercado; ambas recomendaciones se retiraron. «Diseño de agencia» no se ofrece al equipo.

**Definición corta:** *Entendemos y diseñamos trayectorias y condiciones que facilitan o dificultan la conducta.* (Redactada por el usuario en el deck, 2026-10-23. Suma las trayectorias: la conducta cambia en el tiempo. Versión anterior: «Buscamos entender y diseñamos las condiciones (mentales, sociales, materiales, institucionales y tecnológicas) que facilitan o frenan lo que deciden y hacen personas, instituciones y máquinas». Corregido antes, 2026-10-20: decía "diseña y mide"; el verbo de partida es entender, no medir.) En el deck la acompaña: quitamos fricción donde estorba y la ponemos donde protege; decimos a quién sirve cada diseño y seguimos sus efectos en el tiempo, en lo que la gente hace, entiende y vive; empezamos por el seguro, pero no terminamos ahí. No menciona el seguro a propósito (corregido 2026-10-20: la versión anterior decía "frente al riesgo" y ataba el rol al seguro): el seguro es el campo de prueba, no el límite.

**Definición completa:** el rol busca entender y diseña el sistema que produce una conducta: el conjunto de mentes, relaciones, objetos, reglas y agentes artificiales que producen una conducta. Quita fricción donde estorba y la pone donde protege. Su unidad de trabajo no es la pantalla: es el efecto medido en lo que la gente hace (conducta), entiende (comprensión) y vive (bienestar y salud). Usa experimentos para lo observable, psicometría para lo que no se ve, etnografía para lo social y auditoría para lo maquínico. Declara antes de empezar qué resultado va a medir y a quién sirve el diseño.

**Las formas del deck** tienen un solo significado en todo el documento: ○ quien actúa, sea persona, máquina o animal (capas 1-2; hasta v2.2 decía «persona»), □ relaciones, con otros y con los objetos (capas 3-4; hasta v2.1 decía «entorno o institución»), △ sistema de reglas y algoritmos (capas 5-6) y ◇ concepto general que agrupa a los demás (añadido 2026-10-20 a pedido del usuario, para que la idea general no se confunda con el △ de la base). Desde el 2026-10-23, la figura del nuevo diseño conductual es la **triquetra**: un nudo de tres lazos que forman una sola línea, uno por grupo; si se corta la línea en cualquier punto, deja de ser nudo. Es una lectura del equipo: el significado histórico del símbolo es incierto (F-1009).

## 5.1 Manifiesto y propósito (versión del deck, 2026-10-20)

1. Diseñamos condiciones, no clics.
2. Diseñamos trayectorias, no momentos: la conducta cambia, se apaga, vuelve y se resiste.
3. Medimos efectos en lo que la gente hace, entiende y vive.
4. Miramos a cada agente, sea persona, máquina o animal, sus relaciones y el sistema.
5. Facilitamos o frenamos, y decimos a quién sirve cada diseño.
6. Salimos de la pantalla: el hogar, la escuela, la salud y la ciudad también son nuestro campo.

**Propósito:** ampliar lo que el diseño aporta, a las personas, sus comunidades, su ciudad, su país y el planeta, y demostrarlo con evidencia, no con promesas. *(Corregido 2026-10-20: la versión anterior, «llevar el diseño a donde se decide la vida de las personas», era demasiado amplia y no decía lo que el usuario quiere decir.)*

## 5.2 Cómo lo contamos en la empresa (2026-10-23, a pedido del usuario)

Para audiencias corporativas, el propósito cabe en una línea: **«Facilitamos lo que protege y frenamos lo que daña, en la vida de las personas y en el negocio, y lo demostramos con evidencia.»** La versión corta es «Lo que protege, fácil. Lo que daña, difícil.». El propósito del manifiesto sigue siendo la ambición de largo plazo.

- **Pitch de 10 segundos:** «Hacemos que lo que protege a clientes y negocio sea lo fácil, y lo que daña, lo difícil. Y lo medimos.» La versión de 30 segundos cierra con los casos de casa (Bienestar 360 y Cobranzas B2B) y con una pregunta: ¿qué conducta de tus clientes, asesores o sistemas te cuesta más hoy?
- **Menú de 19 servicios en cinco familias:** entender (mapa del sistema conductual, auditoría de fricción, comprensión y confianza, investigación en terreno, revisión de evidencia) · diseñar (piezas y objetos, incentivos y reglas, hábito y trayectoria, diseño con la red, fricción protectora) · probar y medir (experimentos y megaestudios, focalización por efecto, indicadores de bienestar, usuarios sintéticos) · IA y algoritmos (evaluación de asistentes, relación humano-IA, auditoría de algoritmos) · para toda la empresa (formación y playbooks, revisión ética del diseño).
- **Respaldo:** cada servicio cita una fuente del registro (F-21, F-1028, F-926, F-231, F-109, F-346, F-884, F-488, F-793, F-917, F-923, F-925, F-911, F-245, F-921, F-83, F-82, F-888, F-889) o un caso interno. Las herramientas propias por validar (revisión de evidencia, usuarios sintéticos) se declaran así. Los formatos (rápido, de 2 a 4 semanas; proyecto, de 1 a 3 meses; programa, más de 3 meses) son una propuesta a calibrar con la capacidad del equipo.
- **Pitch del rol en md** (2026-10-24, a pedido del usuario, con el nombre todavía abierto): versiones de 10, 30 y 60 segundos, ajustes por audiencia, cuatro preguntas difíciles y las pruebas citables con su solidez, en `research/_outputs/pitch-rol-diseno-conductual.md`.
- **Documento completo**, con la tabla por perfil (nueve gerencias: qué les importa, la frase, la prueba y qué ofrecerles primero): «Diseño conductual: propósito, pitch y menú» (https://claude.ai/artifact/8wcDF85VZYHRMwmEQWoeqL, documento editable y privado).

**Estado del deck al 2026-10-23 (v12, 33 diapositivas):** el usuario sumó una lámina con la triquetra después de la portada, retiró la de los tres entornos de cerca y puso «Lo que ya hacemos» antes de la vanguardia; la lámina de las seis capas usa la triquetra y una tabla de tres niveles por tres agentes (persona, máquina, animal), con la idea fuerza «cada agente atraviesa los tres niveles»; la capa 6 se llama «Los algoritmos» en todas las láminas. El usuario retiró también la lámina «Seis entornos», y «Qué tenemos que aprender» pasó a llamarse «Lecturas para reforzar el modelo», ordenada por los tres niveles con la teoría base de §6. Con la revisión de Parkinson y colegas (F-1028) entraron una cita sobre el sistema en esa lámina y tres cautelas en las notas de «Cómo nace un sistema», «Ocho preguntas» y «Qué proponemos»; las referencias pasan a tres láminas y el deck queda en 33 (versión publicada el 2026-10-23). **Enriquecido con el segundo cerebro (2026-10-24, a pedido del usuario):** a la vista, la lámina del empujón aislado suma el meta-análisis de segundo orden que lleva el efecto cerca de cero (F-18) y el contrapunto de que lo estructural sí escala, la inscripción automática en pensiones (F-966); la vanguardia avisa que Science revisa los datos del estudio de diálogo con IA (F-965); y el seguro suma el punto de partida del Perú (F-507, F-1, F-5). En las notas entran la crisis de replicación (F-712), la heterogeneidad del nudge (F-951), el origen del debate sobre la «muerte» (F-971, F-972), el megaestudio de vacunación (F-938), el cuello de botella de la adopción (F-936), la IA que daña el aprendizaje sin barandas (F-945), la duración de lo aprendido (F-947), los agentes de IA sensibles a los defaults (F-970), el seguro por uso (F-442), la crisis de integridad de Gino y Ariely (F-979, F-615) y el experimento de METR (F-257). El usuario retiró de «Lecturas para reforzar el modelo» la cita de Parkinson y sumó a la portada dos enlaces al debate de 2021. Una revisión experta con /trinidad (2026-10-21, fuentes F-936 a F-1007) está preparada fuera del deck y pendiente de integrar.

**Hilo narrativo del deck (v11, 33 diapositivas; título: «El diseño conductual ha muerto. Larga vida al diseño conductual.», idea del usuario):** (1) Lo que murió: el problema; el empujón aislado rinde poco (F-21, F-17) y nuestra definición sigue describiéndolo · (2) Lo que vive: precedentes de la crítica, vanguardia del campo y lo que el equipo ya hace · (3) Cómo vemos la conducta: condiciones que facilitan o frenan, tiempo, entornos y seis capas · (4) Lo que está en juego: la batalla de las reglas, cómo nace un sistema que nadie eligió, la interacción humano-máquina y el sentido del diseño · (5) Dónde lo probamos: el seguro como canal de bienestar ante El Niño · (6) El rol que viene: rastros, definición, aprendizajes, pasos, nombres para elegir y manifiesto · Anexo: referencias de toda la presentación, por parte, en tres láminas (desde 2026-10-23); la lista completa está en `research/_outputs/referencias-deck-diseno-conductual.md`.

## 6. Ámbitos que construyen el rol

**Lecturas para reforzar el modelo** (así se titula la lámina desde 2026-10-23, a pedido del usuario), **ordenadas por los tres niveles** (2026-10-23, a pedido del usuario: el rol necesita teoría de fondo de economía del comportamiento, psicología y sociología para entender los procesos internos, los metaprocesos y los procesos sociales).**

- **Quien actúa, procesos internos y metaprocesos:** racionalidad limitada (Simon, F-1016) y heurísticas (Tversky y Kahneman, F-220); teoría prospectiva (F-221) y sesgo del presente (Laibson, F-1017; revisión crítica, F-735); procesos duales (Evans y Stanovich, F-1018) y metacognición (Flavell, F-1019; la facilidad como señal metacognitiva, F-225); motivación (Deci y Ryan, F-230) y hábito (Wood y Neal, F-1020); el modelo COM-B como integrador: capacidad, oportunidad y motivación (Michie y colegas, F-1021).
- **Sus relaciones, procesos sociales:** normas sociales y expectativas (Cialdini y Goldstein, F-224; Bicchieri, F-1022); redes y contagio de conductas (Granovetter, F-1023; Centola, F-1024); prácticas sociales (F-896); la teoría del actor-red, donde los objetos también actúan (Latour, F-898 y F-1025; guiones de los objetos, Akrich, F-899); tecnología y moral (F-900).
- **El sistema, reglas, incentivos y sistemas:** teoría del seguro (riesgo moral y selección adversa: Arrow, F-83; Rothschild y Stiglitz, F-82); instituciones y bienes comunes (Ostrom, sin ficha) y el código como regla (Lessig, F-922); sistemas complejos y caos: sensibilidad a las condiciones iniciales (Lorenz, F-1026) y emergencia (Mitchell, F-1027), por lo que en un sistema complejo se diseña probando, observando y corrigiendo; cómo juntar sistemas y conducta (Parkinson y colegas, F-1028, citado en la lámina: «las reglas y la estructura de un sistema dictan buena parte de la conducta, más allá de la intención de cada persona»; traducción nuestra); dónde intervenir (Meadows, F-933); conducta de las máquinas (F-596, [[comportamiento-ia-alucinaciones-desalineamiento]]); políticas públicas, riesgo de desastres y salud pública.
- **Habilitador transversal, método y ética:** inferencia causal (qué causó qué, y para quién), psicometría, etnografía, medición del bienestar (WELLBY, F-911) y regulación del diseño (patrones oscuros e IA).

**Regla para aprender:** cada teoría se enseña con su estado de evidencia, consultado en [[fenomenos-psicologicos]]. La aversión a la pérdida y el sesgo del presente se replican con matices: efectos más chicos y variables de lo que dice la divulgación. El agotamiento del ego (F-707) no se replicó y no entra en la lista, aunque se usaba para justificar la «fatiga de decisión».

## 7. Próximos pasos propuestos al equipo

*(Reescritos 2026-10-20 a pedido del usuario.)*
1. Hacernos responsables de construir indicadores de conducta, bienestar o riesgo, no solo de entregables (Bienestar 360 muestra que se puede). Cautela: la ley de Campbell, cuanto más se usa un indicador para decidir, más presión hay para distorsionarlo (F-935); cada indicador va con su forma de vigilarlo.
2. Sumar psicometría, observación en terreno y medición en el tiempo al kit, junto al experimento.
3. Mostrar el impacto en la vida de las personas. Ante El Niño: que una familia del norte reciba dinero antes de la inundación, con un piloto con una caja del norte (en Bangladesh, pagar 5 días antes redujo 36% los días sin comer, F-793; §3.1). En salud: más casos como Bienestar 360.
4. Diseñar con los equipos de capacidades cómo probamos tecnologías de IA y cómo imaginamos, con ellas, el futuro de la aseguradora. Al probarlas, la regla CH1: lo que la gente dice de un asistente no prueba que decida mejor con él; hay que medir sus decisiones ([[conducta-humano-ia]]).
5. Trazar una hoja de ruta hacia un futuro en que nuestro diseño mejore la vida más allá de RIMAC: en la escuela, la salud pública y la sociedad, diciendo siempre a quién sirve cada diseño.

## 8. Limitaciones

- Los antecedentes teóricos (F-896 a F-900) se verificaron por resumen y ficha bibliográfica, no por texto completo.
- Los rastros de mercado vienen de páginas corporativas y agregadores; no se revisaron portales de empleo ni hay datos de Perú fuera de MineduLAB.
- Ostrom y Thaler y Sunstein se nombran como referencias conocidas, sin ficha propia en el ledger.
- "Arquitectura de la conducta" y "diseño conductual ampliado" son propuestas de este node, no términos establecidos.
- Las fuentes de fricción (F-916 a F-922) se verificaron por resumen y fichas secundarias. El 26% de desplazamiento del delito que suele citarse de F-918 viene de una reproducción del artículo, no del resumen oficial, y no se usa aquí.
- El programa de lealtad aparece como ejemplo de la capa 5, pero la revisión del equipo sobre lealtad y gamificación en retail encontró un solo experimento fuerte y ninguna evidencia causal en América Latina ([[lealtad-gamificacion-recompensas-retail]]): el piloto tiene que medirse bien antes de citarse como logro.

## Conexiones

- [[behavioral-design-estado-disciplina|Behavioral design: estado de la disciplina]] — el punto de partida: crisis del nudge y paso de lo individual a lo estructural; este node propone el rol que sigue.
- [[comportamiento-ia-alucinaciones-desalineamiento|Comportamiento de la IA]] — la máquina como agente que atraviesa los tres niveles (§3) y el argumento de por qué la disciplina gana relevancia: las fallas de la IA son fallas de incentivos.
- [[conducta-humano-ia|Conducta humano-IA]] — la relación de las personas con la IA, en las capas 2 y 4 (sobre-confianza, adulación).
- [[seguros-comportamiento-mundo-peru|Comportamiento y mercado de seguros (Mundo vs. Perú)]] — los datos de confianza y del broker que alimentan las capas 2 y 3.
- [[fenomeno-el-nino-impacto-personas|Fenómeno El Niño: impacto en la vida de las personas]] — el caso que vuelve tangible el rol (§3.1): el seguro como canal de bienestar del hogar, la escuela y la salud pública.
- [[lealtad-gamificacion-recompensas-retail|Gamificación, recompensas y lealtad en retail]] — la cautela sobre el piloto de lealtad que el rol cita como ejemplo de la capa de las reglas (§8).
- [[fenomenos-psicologicos|Fenómenos psicológicos y su estado de replicación]] — el estado de evidencia con que se enseña la teoría base del rol (§6): qué se replica, qué se replica con matices y qué no entra.
- [[mecanismos-seguros-salud|Mecanismos de seguros de salud]] — la evidencia del filtro del médico de cabecera (F-109, F-110) con que §1.4 muestra que poner fricción también es diseño, y una forma eficiente de gestionar la salud.
