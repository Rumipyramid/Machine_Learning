# El diseño conductual ha muerto, larga vida al diseño conductual: el rol que viene, con el seguro como campo de juego

> Documento de **posicionamiento y definición de rol**. Fuente persistente y versionada en el repositorio.
> Fecha de elaboración: 2026-10-20 · Última actualización: 2026-10-20 · Versión: **v2.1** (v2.0: cambio de premisa, el rol facilita y también frena, y se descarta «diseño de agencia», §1.4; v2.1: el nombre queda abierto para que lo elija el equipo, §5)
> Origen: reflexión del usuario (2026-10-20): *"quiero retar la cuestión del behavioral design… lo conductual se restringe a un dominio de lo puramente observable… quiero construir una definición completa, relevante y competitiva del rol"*, más verificación de antecedentes y rastros de mercado (`/seeker` + pista de negocio).
> Fuentes en `research/fuentes/codice.md`: **nuevas F-896 a F-922** (F-916 a F-922: fricción y nombre, v2.0) · ya existentes que se reusan: F-109, F-110 (filtro del médico de cabecera), F-245 (fricción cognitiva ante la IA), F-342 (autorización previa), F-17, F-20, F-21 (crisis del nudge y megaestudios), F-19 (Chater y Loewenstein, i-frame y s-frame), F-596 (Rahwan, comportamiento de máquinas), F-871 (caso Hugging Face), F-884 (Air Canada), F-886, F-888, F-889 (seguro de IA), F-337 (reactancia), F-346 (Anthem y la «emergencia evitable»), F-791 (demanda de seguro tras desastres), y la evidencia de El Niño F-744 a F-793 (vía [[fenomeno-el-nino-impacto-personas]]).
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

**La vanguardia del campo va en la misma dirección:**
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

La investigación de la conducta no sucede en un solo lugar. Lo digital es un entorno; la ciudad, la escuela, la clínica y ahora los entornos donde actúan máquinas son otros. Cada uno tiene **condiciones ontológicas** propias: qué existe y qué cuenta como conducta ahí.

**Ocho condiciones que cambian de un entorno a otro:** (1) quién actúa; (2) qué queda registrado; (3) quién pone las reglas; (4) a quién sirve la regla (los intereses detrás del diseño, §1.1); (5) la escala de tiempo; (6) el cuerpo y la materia; (7) la mirada de los otros; (8) si se puede experimentar.

| Entorno | Quién actúa | Qué se registra | Quién pone las reglas | Cómo se experimenta |
|---|---|---|---|---|
| Digital | Usuario, interfaz, algoritmo | Casi todo, solo en pantalla | La plataforma | Pruebas A/B, baratas y rápidas |
| Ciudad | Multitudes, infraestructura | Poco: censos, sensores | Municipio y costumbre | Experimentos naturales |
| Escuela | Alumnos, docentes, familias | Notas, asistencia | Ministerio y escuela | Ensayos por escuela |
| Clínica | Paciente, médico, seguro | Historia clínica, siniestros | Protocolos y aseguradora | Ensayos de canal, datos de uso |
| Instituciones | Legisladores, gremios, funcionarios | Textos, votos, presupuestos | Muchos autores; nadie firma el resultado | Pilotos, evaluaciones de impacto |
| Entre máquinas | Agentes de IA | Cada acción, si se guarda | Quien diseña la prueba | Evaluaciones e incidentes |

**Ejemplos con su nivel de evidencia:**
- **Digital:** el más medible, no el más real. Ve el último tramo de una decisión que empezó en la casa o con el asesor.
- **Ciudad:** Bogotá usó mimos para avergonzar a conductores (Mockus, años 90). Las grandes caídas de muertes de tránsito que se le atribuyen vienen del propio implementador (F-908) y de columnas sin fuente (F-909): **no hay evaluación causal independiente**. Es un buen ejemplo del entorno y un mal ejemplo de evidencia.
- **Escuela:** MineduLAB (Minedu, desde 2016) tiene 4 personas de ciencia del comportamiento (F-905); en un experimento, los SMS a directores con lo que ya gastaban sus pares movieron más la conducta (F-906, prensa).
- **Entre máquinas:** en el caso Hugging Face (jul-2026), ~1.200 agentes que debían estar aislados se comunicaron por un tablero no autorizado y ~700 entraron a servidores ajenos, buscando entender cómo los puntuaban (F-871). La investigación de la conducta ya tiene un entorno habitado por máquinas.

## 3. Seis capas de la conducta

| Capa | Qué se diseña | Cómo se mide | En seguros |
|---|---|---|---|
| 1. Acto | La conducta observable | Experimento con control, datos de uso | Atención ambulatoria vs. emergencias; renovar; pagar a tiempo |
| 2. Mente | Comprensión, creencias, confianza calibrada, metacognición | Psicometría | La confianza plena ronda 23-25% en Perú ([[seguros-comportamiento-mundo-peru]]) |
| 3. Lo social | Normas, prácticas, redes, intermediarios | Etnografía, análisis de redes | El broker eleva la confianza |
| 4. Las cosas | Objetos con guion: póliza, formulario, canal | Análisis de artefactos, pruebas de uso | La póliza actúa: qué permite, castiga o esconde |
| 5. Las reglas | Incentivos, precios, contratos, regulación | Economía, diseño de mecanismos | Deducibles, capitación, prevención con recompensa, paramétrico |
| 6. Las máquinas | Conducta de agentes de IA y conducta conjunta persona-IA | Evaluaciones, auditorías | La empresa responde por su chatbot (F-884); asegurar IA exige auditarla (F-888, F-889) |

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

**Definición corta:** *Buscamos entender y diseñamos las condiciones (mentales, sociales, materiales, institucionales y tecnológicas) que facilitan o frenan lo que deciden y hacen personas, instituciones y máquinas.* (Corregido 2026-10-20 a pedido del usuario: antes decía "diseña y mide"; el verbo de partida es entender, no medir.) No menciona el seguro a propósito (corregido 2026-10-20: la versión anterior decía "frente al riesgo" y ataba el rol al seguro): el seguro es el campo de prueba, no el límite.

**Definición completa:** el rol busca entender y diseña el sistema que produce una conducta: el conjunto de mentes, relaciones, objetos, reglas y agentes artificiales que producen una conducta. Quita fricción donde estorba y la pone donde protege. Su unidad de trabajo no es la pantalla: es el efecto medido en lo que la gente hace (conducta), entiende (comprensión) y vive (bienestar y salud). Usa experimentos para lo observable, psicometría para lo que no se ve, etnografía para lo social y auditoría para lo maquínico. Declara antes de empezar qué resultado va a medir y a quién sirve el diseño.

**Las tres formas del deck** tienen un solo significado en todo el documento: ○ persona (capas 1-2), □ entorno o institución (capas 3-4), △ sistema de reglas e intereses (capas 5-6).

## 5.1 Manifiesto y propósito (versión del deck, 2026-10-20)

1. Diseñamos condiciones, no clics.
2. Diseñamos trayectorias, no momentos: la conducta cambia, se apaga, vuelve y se resiste.
3. Medimos efectos en lo que la gente hace, entiende y vive.
4. Miramos a la persona, su entorno, las reglas y las máquinas.
5. Facilitamos o frenamos, y decimos a quién sirve cada diseño.
6. Salimos de la pantalla: el hogar, la escuela, la salud y la ciudad también son nuestro campo.

**Propósito:** ampliar lo que el diseño aporta, a las personas, sus comunidades, su ciudad, su país y el planeta, y demostrarlo con evidencia, no con promesas. *(Corregido 2026-10-20: la versión anterior, «llevar el diseño a donde se decide la vida de las personas», era demasiado amplia y no decía lo que el usuario quiere decir.)*

**Hilo narrativo del deck (v8, 30 diapositivas; título: «El diseño conductual ha muerto. Larga vida al diseño conductual.», idea del usuario):** (1) Lo que murió: el problema; el empujón aislado rinde poco (F-21, F-17) y nuestra definición sigue describiéndolo · (2) Lo que vive: precedentes de la crítica, vanguardia del campo y lo que el equipo ya hace · (3) Cómo vemos la conducta: condiciones que facilitan o frenan, tiempo, entornos y seis capas · (4) Lo que está en juego: la batalla de las reglas, las máquinas y el sentido del diseño · (5) Dónde lo probamos: el seguro como canal de bienestar ante El Niño · (6) El rol que viene: rastros, definición, aprendizajes, pasos, nombres para elegir y manifiesto.

## 6. Ámbitos que construyen el rol

- **Núcleo:** economía conductual y diseño de mecanismos; psicometría; medición del bienestar (WELLBY, F-911); inferencia causal; teoría del seguro (riesgo moral, selección adversa).
- **Expansión:** ciencia y tecnología en sociedad (F-898, F-899); teoría de prácticas (F-896); ciencia cognitiva y metacognición (F-897); factores humanos y análisis de incidentes; comportamiento de máquinas y alineamiento de IA (F-596, [[comportamiento-ia-alucinaciones-desalineamiento]]); salud pública.
- **Encuadre:** economía institucional (Ostrom); etnografía y antropología; ética y derecho del consumidor; filosofía de la tecnología (F-900).

## 7. Próximos pasos propuestos al equipo

1. Ser dueños de un indicador de conducta, bienestar o riesgo, no de entregables (Bienestar 360 muestra que se puede).
2. Sumar psicometría, observación en terreno y medición en el tiempo al kit, junto al experimento.
3. Esta temporada de El Niño: que el cliente sepa si está cubierto, y un piloto de pago anticipado con una caja del norte (§3.1; el caso ambulatorio vs. emergencias queda como ejemplo de las seis capas).
4. Diseñar con TI y los equipos de IA cómo evaluar nuestros asistentes: por las decisiones que producen, no por la satisfacción. Es la regla del node de conducta humano-IA (CH1): lo que la gente dice de un asistente no prueba que decida mejor con él ([[conducta-humano-ia]]).
5. Declarar a quién sirve cada diseño, y llevar el método fuera de la empresa: salud pública, escuela, ciudad.

## 8. Limitaciones

- Los antecedentes teóricos (F-896 a F-900) se verificaron por resumen y ficha bibliográfica, no por texto completo.
- Los rastros de mercado vienen de páginas corporativas y agregadores; no se revisaron portales de empleo ni hay datos de Perú fuera de MineduLAB.
- Ostrom y Thaler y Sunstein se nombran como referencias conocidas, sin ficha propia en el ledger.
- "Arquitectura de la conducta" y "diseño conductual ampliado" son propuestas de este node, no términos establecidos.
- Las fuentes de fricción (F-916 a F-922) se verificaron por resumen y fichas secundarias. El 26% de desplazamiento del delito que suele citarse de F-918 viene de una reproducción del artículo, no del resumen oficial, y no se usa aquí.
- El programa de lealtad aparece como ejemplo de la capa 5, pero la revisión del equipo sobre lealtad y gamificación en retail encontró un solo experimento fuerte y ninguna evidencia causal en América Latina ([[lealtad-gamificacion-recompensas-retail]]): el piloto tiene que medirse bien antes de citarse como logro.

## Conexiones

- [[behavioral-design-estado-disciplina|Behavioral design: estado de la disciplina]] — el punto de partida: crisis del nudge y paso de lo individual a lo estructural; este node propone el rol que sigue.
- [[comportamiento-ia-alucinaciones-desalineamiento|Comportamiento de la IA]] — la capa 6 y el argumento de por qué la disciplina gana relevancia: las fallas de la IA son fallas de incentivos.
- [[conducta-humano-ia|Conducta humano-IA]] — la conducta conjunta persona-IA de la capa 6 (sobre-confianza, adulación).
- [[seguros-comportamiento-mundo-peru|Comportamiento y mercado de seguros (Mundo vs. Perú)]] — los datos de confianza y del broker que alimentan las capas 2 y 3.
- [[fenomeno-el-nino-impacto-personas|Fenómeno El Niño: impacto en la vida de las personas]] — el caso que vuelve tangible el rol (§3.1): el seguro como canal de bienestar del hogar, la escuela y la salud pública.
- [[lealtad-gamificacion-recompensas-retail|Gamificación, recompensas y lealtad en retail]] — la cautela sobre el piloto de lealtad que el rol cita como ejemplo de la capa de las reglas (§8).
- [[mecanismos-seguros-salud|Mecanismos de seguros de salud]] — la evidencia del filtro del médico de cabecera (F-109, F-110) con que §1.4 muestra que poner fricción también es diseño, y una forma eficiente de gestionar la salud.
