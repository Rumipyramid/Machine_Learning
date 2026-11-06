# Cómo avisar que un proveedor sale de la red de salud y llevar al asegurado al nuevo

> Documento de investigación. Fuente persistente y versionada en el repositorio.
> Fecha de elaboración: 2026-11-06 · Última actualización: 2026-11-06 · Versión: **v1.0**
> Origen: `/seeker` (registro empírico + teórico), pedido del usuario.
> Fuentes en `research/fuentes/codice.md`: **F-847 a F-880** (normativa F-847 a F-862 y F-876 · empírica F-863 a F-874 y F-878 · casos F-875 y F-877 · teoría F-879 y F-880). Se apoya también en F-117, F-118 (contacto comercial en Perú), F-221, F-223 y F-724 (aversión a la pérdida).
> Pregunta: **¿cómo comunican las aseguradoras de salud la salida de una clínica o centro de imágenes de su red, y qué hace que el asegurado se atienda en el proveedor nuevo?**
> Decisión que alimenta: diseñar la comunicación que migre pacientes de un centro de imágenes a otro.

---

## 0. Alcance y límites de lectura

- **Qué cubre:** aseguradoras privadas de salud y planes gestionados. Perú (EPS, aseguradoras, IAFAS), Chile (isapres), Colombia, EE.UU. (Medicare Advantage y planes comerciales) y Reino Unido.
- ⚠️ **Límite fuerte.** En esta sesión no se pudo abrir ninguna página completa. Los dominios de la SBS, de gob.pe, de la Superintendencia de Salud de Chile y del CFR estaban bloqueados por la red. Todo se leyó por **fragmentos del buscador**. Las cifras de plazos peruanos deben verificarse en el texto oficial antes de usarse con un cliente o un regulador.
- ⚠️ **No apareció ningún comunicado público de una aseguradora peruana** anunciando la salida de una clínica o un centro de imágenes. En Perú este aviso parece viajar por canales privados (correo al afiliado, área de RR. HH. del empleador, corredor). Lo que se dice aquí sobre la práctica peruana es inferencia a partir de contratos y de la norma.
- No se hizo búsqueda social (Reddit, X, foros). Eso le toca a `/gossip`.

---

## 1. Conclusión

1. **El aviso es obligatorio y tiene plazo en todos los mercados revisados, pero el plazo varía.** Perú: entre 15 días hábiles y 30 a 45 días calendario según la norma y el producto (por verificar). EE.UU.: 30 días, y 45 días con llamada telefónica cuando sale un médico de cabecera o de salud mental. Chile: correo y web, más ajuste del plan.
2. **El mejor estándar no es avisar, es dar continuidad.** EE.UU. protege 90 días a quien está en tratamiento (F-858). Chile obliga a reembolsar si el prestador ya no cobra por convenio (F-860). Avisar sin un puente para el tratamiento en curso genera la mayor parte de las quejas.
3. **En imágenes, quien decide dónde se hace el examen es el médico que deriva, no el paciente.** Su peso supera al del precio y al de la cercanía (F-867). Una campaña al asegurado sin cambiar la orden médica rinde poco.
4. **Las imágenes son el servicio más fácil de mover.** Los pacientes las ven como intercambiables (F-865). El contacto previo al examen con una alternativa concreta funcionó en Anthem (F-863).
5. **Lo que más se pierde al cambiar de centro son los estudios previos.** Si el médico ve las imágenes anteriores, baja 25% la probabilidad de repetir el examen (F-869). Garantizar ese traspaso es parte del mensaje, no un detalle técnico.
6. **Los errores de comunicación más dañinos son tres:** cartas confusas sobre disputas que aún no terminan (F-871), el corte sin puente (F-870, F-861) y culpar al prestador en público (F-862).

---

## 2. Marco regulatorio

### 2.1 Perú

| Norma | Qué exige | Solidez de la lectura |
|---|---|---|
| Ley 29946, Ley del Contrato de Seguro, art. 30 (F-848) | El contratante debe ser informado de los cambios propuestos durante la vigencia y puede aceptarlos o no. Por conocimiento general: 30 días para decidir y, si no acepta, rige lo pactado hasta el fin de la vigencia. | Texto literal no verificado |
| SBS, cláusulas abusivas (F-847) | La red de clínicas es un aspecto relevante del contrato. La aseguradora no puede cambiarla libremente: debe informar al contratante y seguir el art. 30. | Fragmento de documento oficial |
| SBS, Res. 4143-2019, conducta de mercado en seguros (F-849) | La modificación durante la vigencia solo procede en supuestos acotados. En casos aprobados aparece el aviso de 45 días calendario. | No se confirmó si aplica a cambios de red |
| SUSALUD, Res. 066-2020 y 069-2021 (F-851) | Cambios en cobertura, beneficios o red de prestadores: aviso escrito con 15 días hábiles; vale una comunicación de fecha cierta. | Fragmentos incompletos; verificar ámbito |
| SUSALUD, Res. 004-2020, cláusulas mínimas IAFAS-IPRESS (F-850) | Aviso de modificaciones con al menos 30 días antes de su vigencia, salvo casos excepcionales. Los contratos se registran en SITECON en 15 días hábiles. | No queda claro si el aviso es al afiliado o entre las partes |
| Ley 29414 y D.S. 027-2015-SA (F-853) | Derecho del usuario a ser informado de forma adecuada y oportuna ante toda IAFAS e IPRESS. | Marco general, sin artículo específico de red |
| D.S. 002-2019-SA, reclamos (F-854) | Reclamo primero ante la IAFAS; sin respuesta en 30 días o insatisfactoria, a SUSALUD. | Guías secundarias |
| Contacto comercial (F-117, F-118) | Indecopi sanciona llamadas comerciales no consentidas. | Relevante si la llamada de redirección "ofrece" algo |

**Lectura práctica para Perú.** Hay dos reguladores según el producto. Si es una póliza de seguro (SBS), el cambio de red se trata como modificación del contrato. Si es una EPS o un plan de IAFAS (SUSALUD), el aviso al afiliado es escrito y con plazo. El dato que falta confirmar es cuál plazo aplica a cada caso. Mientras tanto, lo prudente es **usar el plazo más largo (45 días) y documentar la fecha cierta de entrega**.

**Una zona gris útil.** Si la llamada solo informa un cambio en el contrato vigente, no es venta. Si ofrece un beneficio para cambiar de centro, podría leerse como contacto comercial. Conviene que la llamada sea de servicio y que el incentivo viaje por escrito.

### 2.2 Referentes externos

| Mercado | Regla | Fuente |
|---|---|---|
| EE.UU., Medicare Advantage | Aviso escrito a los pacientes habituales del proveedor (atendidos en los últimos 3 meses; 3 años en atención primaria y salud mental). 45 días antes para atención primaria y salud mental, con al menos un intento de llamada; 30 días para el resto. | F-855 |
| EE.UU., modelo de carta de CMS | Se nombra como "terminación". Campo obligatorio: cómo pedir que siga el tratamiento en curso. Se entrega una lista de alternativas de la red. | F-856 |
| EE.UU., No Surprises Act | Quien está en tratamiento grave, embarazo, hospitalización o cirugía programada conserva condiciones de red hasta 90 días desde el aviso. La ley no aclara quién avisa a quién. | F-858, F-859 |
| EE.UU., propuesta 2027 | Incluir en el aviso el derecho a cambiar de plan. Estado incierto. | F-857 |
| Chile, Circular IF/N° 413 (2022) | Reembolso si el prestador deja de cobrar por convenio. Se puede reemplazar al prestador en el plan. Hay que decirle a la persona cómo seguir accediendo. Se reporta al regulador en 10 días hábiles. | F-860 |
| Colombia (proyecto) | Información de red actualizada y difundida por medios masivos en cada cambio. | F-876 |

---

## 3. Canales y momentos

| Canal | Quién lo usa | Para qué sirve |
|---|---|---|
| **Carta o correo personalizado** | Todos. Es el canal que la norma reconoce (fecha cierta en Perú, aviso escrito en EE.UU.) | Prueba legal del aviso |
| **Llamada telefónica** | Obligatoria en EE.UU. para médico de cabecera y salud mental (F-855) | Llegar a quien no lee; resolver dudas en el momento |
| **Web y buscador de red** | Chile (F-861), Reino Unido (F-875), Perú en anexos PDF (F-877) | Consulta, no aviso. Nadie entra a buscar un cambio que no sabe que ocurrió |
| **Médico que deriva** | Anthem 2017: lista de centros alternativos entregada al médico (F-864) | El canal con más poder en imágenes (F-867) |
| **Corredor o RR. HH.** | Reino Unido avisó a asesores (F-875); en Perú las EPS se gestionan vía empleador | Canal real en seguros colectivos |
| **Punto de atención del prestador** | Implícito en los conflictos chilenos: el afiliado se entera en ventanilla cuando no le emiten el bono (F-861) | El peor momento para enterarse |

**Momentos.** Hay tres: el aviso previo (30 a 45 días), el momento de la orden médica (cuando se decide el centro) y el día del examen. El aviso previo cumple la ley. **El momento de la orden es el que mueve la conducta** (F-863, F-867).

**A quién avisar.** El estándar estadounidense no avisa a toda la cartera: avisa a quien usó el proveedor hace poco (F-855). Chile avisó a quienes tenían a la clínica como preferente (F-861). Segmentar por uso reciente reduce ruido y miedo innecesario.

---

## 4. El mensaje: cómo se nombra y qué tono se usa

**Lo documentado:**
- El regulador estadounidense usa una palabra directa: **"terminación"** del proveedor (F-856). No se halló en ninguna norma un eufemismo como "mejora de red".
- En las disputas, las cartas culpan a la otra parte. En 2026 Cigna escribió que la red hospitalaria "exige precios más altos que el promedio" (F-870). En Chile, la clínica culpó a la isapre (F-862). **Cada lado cuenta su versión y el paciente queda en medio.**
- Las cartas sobre una salida "posible" confunden. Anthem reconoció que su carta "lamentablemente creó confusión" (F-871).

**Lo que no se encontró:** evidencia de qué nombre del cambio funciona mejor ("salida de red", "nuevo proveedor", "mejora de red"). No hay experimentos publicados sobre esa variable. Lo que sigue es inferencia.

**Capa teórica (interpretación).**
- **Inercia o sesgo del statu quo** (F-879): el asegurado prefiere su centro habitual aunque cueste más. El aviso pide un esfuerzo activo; si el camino nuevo no es más fácil que el viejo, gana el viejo.
- **Aversión a la pérdida** (F-221, F-223; replicada con matices, F-724): el asegurado lee el cambio como la pérdida de algo que tenía. Encuadrarlo como "mejora" cuando se percibe pérdida se lee como maquillaje y erosiona confianza. La aversión es mayor en personas mayores y en lo que el cliente conoce poco.
- **Inferencia:** el tono que mejor resiste es **decir el cambio con claridad y poner el énfasis en lo que se conserva** (cobertura, médico, estudios previos, citas ya agendadas). Llamarlo "mejora" solo es honesto si el asegurado gana algo concreto y verificable (menos espera, más cerca, entrega de resultados más rápida).

---

## 5. Redirección: qué hace que el asegurado vaya al centro nuevo

| Palanca | Evidencia | Solidez |
|---|---|---|
| **Contacto antes del examen con una alternativa concreta** | Anthem llamaba al afiliado antes de la resonancia si había un centro al menos US$400 más barato. Bajó el costo y forzó a la competencia a bajar precios (F-863). | 🟢 Cuasi-experimental, peer-reviewed |
| **Actuar sobre el médico que deriva** | Pesa más que el copago o la residencia del paciente. Menos de 1% compara precios; en promedio se pasan de largo 6 centros más baratos (F-867). | 🟢 Observacional, peer-reviewed |
| **Incentivo en dinero** | Éxito modesto, mayor en imágenes; solo ~8% usa la herramienta (F-865). | 🟢 Observacional, peer-reviewed |
| **Precio de referencia (copago mayor fuera)** | −13% en precio por examen de imágenes, pero el efecto se desvaneció con el tiempo (F-866). | 🟡 Resumen académico |
| **Obligación (preaprobación)** | Anthem 2017 exigió autorización para imágenes en hospitales y dio al médico la lista de centros. Funciona, con costo reputacional (F-864). | 🟠 Prensa |
| **Agendamiento en línea, buenas calificaciones, cercanía y poca espera** | Lo que más valoran los pacientes al elegir un centro de imágenes, junto con la recomendación de su médico (F-868). | 🟢 Preferencia declarada |
| **Traspaso de estudios previos** | Si el médico ve las imágenes anteriores, baja 25% la repetición de exámenes (F-869). | 🟢 Observacional, peer-reviewed |
| **Lista de alternativas de la red** | Exigida por CMS en el aviso (F-856). | 🔵 Norma |
| **Puente para quien está en tratamiento** | 90 días con condiciones de red en EE.UU. (F-858); reembolso en Chile (F-860). | 🔵 Norma |

**Qué no se encontró:** estudios sobre agendamiento asistido por la aseguradora como palanca de cambio, ni sobre beneficios no monetarios (resultados más rápidos, traslado). Son hipótesis razonables, sin prueba publicada.

---

## 6. Fricciones y reacciones

- **El corte sin puente es la fricción mayor.** En Chile, el afiliado pasó de pagar un copago a pagar todo y pedir reembolso de un día para otro (F-861, F-862). En EE.UU., pacientes quedaron "corriendo" tras cortes abruptos (F-870).
- **La continuidad se rompe y no se recupera sola.** Cuando el médico habitual queda fuera de red, las visitas de seguimiento caen y las de paciente nuevo no compensan (F-872, preliminar).
- **Las cartas sobre lo que "podría" pasar asustan más de lo que informan.** El caso Anthem es explícito (F-871). KFF cuenta más de 650 hospitales en disputas públicas desde 2021; en muchas el contrato se renovó tras las cartas (F-870).
- **El daño no es parejo.** Los cierres de planes en Medicare Advantage afectan más a beneficiarios afroamericanos (F-874). Las redes de salud mental se perciben inadecuadas el doble que las médicas (F-878). Los pacientes en tratamiento, mayores o con enfermedad crónica son los más expuestos.
- **La rotación es normal, no excepcional.** La red típica cambia poco en neto, pero algunas rotan mucho (F-873). Un proceso de aviso estandarizado vale más que una campaña por caso.
- **Teoría (Hirschman, F-880).** Ante un deterioro, el cliente reclama o se va. Si el aviso no abre un canal claro de voz (a quién llamar, cómo pedir excepción), la reacción se va al reclamo formal ante SUSALUD (F-854) o a no renovar el seguro.

---

## 7. Casos concretos

| Caso | Qué pasó | Lección |
|---|---|---|
| **Indisa y Banmédica/Vida Tres, Chile 2022** (F-861) | Clínica avisa al regulador el 17-nov; corta bonos el 23-nov; la isapre envía correo a quienes tenían la clínica como preferente y publica en web; se reanuda el 1-dic. | Avisar solo a los afectados está bien. Seis días entre aviso y corte no alcanzan. |
| **Indisa y Cruz Blanca, Chile 2023** (F-862) | El afiliado paga todo y luego pide reembolso. La clínica comunica culpando a la isapre. | Si la aseguradora no cuenta primero, cuenta el prestador. |
| **Circular 413, Chile 2022** (F-860) | El regulador reacciona a las denuncias con reembolso obligatorio y reemplazo del prestador en el plan. | Las quejas producen norma. El costo de comunicar mal termina en regulación. |
| **Anthem y CommonSpirit, EE.UU.** (F-871) | Carta confusa; la aseguradora pide disculpas y promete reescribirla. | Probar la carta con asegurados antes de enviarla. |
| **Anthem, programa de resonancias 2014** (F-863) | Llamada previa al examen con una alternativa concreta más barata. | Buen ejemplo de redirección en imágenes. |
| **Anthem, preaprobación 2017** (F-864) | Obligación y lista de centros entregada al médico. | Funciona, pero genera rechazo. |
| **Bupa y BMI, Reino Unido 2011** (F-875) | Se avisa a miembros y asesores; algunos hospitales vuelven tras revisión. | El corredor es canal de aviso. |

**No se halló ningún caso peruano documentado en público.**

---

## 8. Qué aplica al Perú

- **Aplica directo:** aviso escrito con fecha cierta, plazo (asumir 45 días hasta verificar), derecho del contratante a rechazar el cambio en pólizas SBS, ruta de reclamos ante SUSALUD.
- **Aplica con adaptación:** el estándar estadounidense de avisar solo a quienes usaron el centro en los últimos meses, sumar una llamada y una lista de alternativas. En Perú no es obligatorio, pero reduce reclamos.
- **Aplica con cuidado:** la llamada de redirección. Si ofrece un beneficio, podría leerse como contacto comercial (F-117, F-118).
- **Contexto peruano que amplifica el riesgo:** la desconfianza en seguros es alta (cerca de la mitad desconfía; la causa principal es la falta de información; ver [[seguros-comportamiento-mundo-peru]]). Un aviso confuso confirma esa sospecha.
- **Contexto que juega a favor:** la red de imágenes en Lima ya incluye varios centros grandes (F-877). El paciente tiene alternativas reales; el problema es de costumbre y de orden médica, no de oferta.
- **Seguros colectivos (EPS):** el empleador y el corredor son canales obligados. El afiliado suele no leer el correo de la aseguradora.

---

## 9. Patrones comunes y aprendizajes para migrar pacientes de un centro de imágenes a otro

**Patrones que se repiten en todos los mercados:**
1. Aviso escrito con plazo, documentado.
2. Aviso solo a quien usó el proveedor hace poco.
3. Lista de alternativas concretas.
4. Puente para quien está en tratamiento.
5. Canal para pedir excepciones.

**Aprendizajes accionables (cada uno con su base):**

| # | Acción | Por qué |
|---|---|---|
| 1 | **Segmentar.** Avisar a quien se hizo un estudio en el centro saliente en los últimos 3 a 12 meses, y priorizar a quien tiene un control programado (oncología, embarazo, seguimiento de lesiones). | Estándar de EE.UU. (F-855); el daño se concentra en quien está en tratamiento (F-858, F-872). |
| 2 | **Avisar con 45 días, por escrito y con fecha cierta; sumar SMS o WhatsApp y una llamada a los prioritarios.** | Plazo más largo de la norma peruana (F-849); llamada obligatoria en EE.UU. para los casos sensibles (F-855). |
| 3 | **Decir el cambio sin eufemismo y abrir con lo que se conserva.** Ejemplo: "Desde el 15 de enero, el Centro X deja de estar en tu red. Tu cobertura no cambia. Te ayudamos a pasar al Centro Y con tus estudios anteriores." | Inercia y aversión a la pérdida (F-879, F-221, F-724); las cartas confusas generan quejas (F-871). |
| 4 | **Dar un solo centro recomendado, no una lista larga**, elegido por cercanía al domicilio o al centro anterior, con dirección, horario y tiempo de espera. Dejar la lista completa como respaldo. | Lo que valoran los pacientes: cercanía, espera, calificación (F-868); una alternativa concreta funcionó en Anthem (F-863). |
| 5 | **Garantizar y comunicar el traspaso de imágenes y reportes previos.** Mejor aún: que el centro nuevo los tenga cargados antes de la primera cita. | Evita repetir exámenes (F-869) y elimina la pérdida más concreta que siente el paciente. |
| 6 | **Agendamiento asistido en el mismo mensaje:** botón o enlace para reservar, o llamada para agendar. | El agendamiento en línea pesa en la elección (F-868). Su efecto en la migración no está probado: medirlo. |
| 7 | **Trabajar con los médicos que derivan.** Enviarles el cambio y el centro sugerido; actualizar las órdenes y los sistemas de derivación de las clínicas de la red. | El médico pesa más que el precio o la cercanía (F-867); Anthem lo usó (F-864). |
| 8 | **Puente para los que están en tratamiento.** Mantener condiciones de red por 60 a 90 días, o reembolsar, para quienes tienen un control ya iniciado. | Estándar de EE.UU. y Chile (F-858, F-860). |
| 9 | **Incentivo solo si hace falta, y por escrito.** Por ejemplo, copago cero o resultados prioritarios en el primer estudio en el centro nuevo. | Efecto modesto (F-865) y se desvanece (F-866); por teléfono roza el contacto comercial (F-117). |
| 10 | **Abrir un canal de voz explícito:** un número, un nombre, un plazo para pedir excepción. | Sin voz, la reacción es reclamo o salida (F-880, F-854). |
| 11 | **Coordinar el relato con el centro saliente**, o al menos llegar primero. | Si no, el prestador cuenta su versión (F-862). |
| 12 | **No avisar de cortes que todavía no son seguros**, o decir con claridad que es una posibilidad, la fecha de decisión y qué pasa en cada escenario. | Las cartas sobre lo "posible" confunden (F-871, F-870). |

**Qué medir.** Proporción de estudios del segmento hechos en el centro nuevo a 30, 60 y 90 días; reclamos al libro de la aseguradora y a SUSALUD; exámenes repetidos por falta de estudios previos; renovación de la póliza o del plan.

**Experimento sugerido.** Asignar al azar a los afectados entre carta estándar y paquete completo (carta + centro único recomendado + agendamiento asistido + estudios previos transferidos). Comparar la migración a 60 días y los reclamos. Si el volumen lo permite, una tercera rama con incentivo.

---

## 10. Contraevidencia buscada

- **Se buscó a propósito evidencia de que redirigir no funciona o se revierte.** Se encontró: el efecto del precio de referencia en imágenes **se desvaneció** (F-866); solo ~8% usa las herramientas de comparación (F-865); los pacientes pasan de largo centros más baratos aunque paguen más (F-867). Lectura: las palancas al paciente son débiles; las palancas al médico y al proceso son más fuertes.
- **Se buscó evidencia de que el aviso anticipado reduce reclamos o pérdida de clientes.** No se encontró ningún estudio que lo mida. El supuesto de que más anticipación da mejor resultado es razonable pero no probado.
- **Se buscó un estudio de confianza o satisfacción tras la salida de un proveedor.** No se encontró. Lo más cercano es la caída de visitas de seguimiento (F-872, preliminar).
- **Se buscó un caso peruano público.** No se encontró.

---

## 11. Limitaciones

- Ninguna página se abrió completa; todo viene de fragmentos del buscador.
- Los plazos peruanos (15 días hábiles, 30 o 45 días calendario) vienen de normas distintas y no se pudo confirmar cuál rige cada producto. **Verificar en El Peruano y en el texto consolidado de la SBS antes de usar.**
- Varias fichas tienen autores no verificados (F-863, F-865, F-868, F-874, F-878).
- La evidencia de redirección viene de EE.UU. con incentivos de precio. En Perú el asegurado de EPS suele pagar un copago fijo; la palanca del precio pesa menos y la de conveniencia pesa más.
- No hay evidencia publicada sobre el nombre o el tono del mensaje.

---

## 12. Tabla de rigurosidad

| Fuente | Tipo | Peer review | Validez | Peso para la decisión |
|---|---|---|---|---|
| F-863 Anthem resonancias (2014) | Cuasi-experimental | 🟢 Health Affairs | ⚠️ EE.UU., incentivo de precio | 🟢 Alto para redirección en imágenes |
| F-867 Chernew et al. (2018/2021) | Observacional, claims | 🟢 versión publicada (el NBER no) | ✅ conducta observada | 🟢 Alto: el médico decide |
| F-865 Whaley et al. (2019) | Observacional con comparación | 🟢 Health Affairs | ⚠️ autoselección en quién usa la herramienta | 🟡 Medio |
| F-866 Berkeley (2017) | Resumen de estudio con comparación | ⚠️ origen no verificado | ⚠️ un solo empleador | 🟡 Medio |
| F-868 PLOS ONE (2025) | Elección discreta | 🟢 | ⚠️ preferencia declarada, no conducta | 🟡 Medio |
| F-869 Vest et al. (2015) | Observacional | 🟢 AJMC | ⚠️ una región; no mide cambio de centro | 🟢 Alto para el traspaso de estudios |
| F-872 Berkeley CEGA | Preliminar | 🔴 sin arbitraje | ⚠️ | 🔴 Bajo |
| F-874, F-878 JAMA | Transversal, encuesta | 🟢 | ⚠️ miden otra cosa (cierres de plan, percepción) | 🟡 Contexto |
| F-847 a F-861, F-876 | Normativa | ⚪ no aplica | ⚠️ leída por fragmentos | 🟢 Alto para lo obligatorio, por verificar |
| F-862, F-864, F-870, F-871, F-875 | Prensa | ⚪ no aplica | ⚠️ casos | 🟡 Ilustran fricciones |

**Eco de cita.** Las notas sobre Indisa (F-861 y F-862) comparten origen en el mismo conflicto. Los plazos de Medicare Advantage (F-855) vienen de tres planes que resumen la misma regla: cuentan como una sola fuente.

---

## 13. Preguntas abiertas

| # | Pregunta | Cómo responderla |
|---|---|---|
| CR1 | ¿Qué plazo exacto rige el aviso de cambio de red en EPS y en pólizas SBS de salud? | Leer el texto oficial de las normas F-848 a F-851; consultar a legal. |
| CR2 | ¿El centro único recomendado migra más pacientes que la lista completa? | A/B en el próximo cambio de red. |
| CR3 | ¿El agendamiento asistido y el traspaso de estudios previos suben la migración a 60 días? | Experimento de §9. |
| CR4 | ¿Cuánto pesa el médico que deriva en Perú? | Analizar órdenes por médico y centro en los datos de la aseguradora. |
| CR5 | ¿Qué nombre del cambio genera menos reclamos? | Prueba de mensajes con usuarios sintéticos (`/lapuerta`) como filtro y luego con asegurados reales. |

---

## Conexiones

- [[glosario-seguro-salud-peru|Glosario de seguro de salud en Perú]] — define "red de prestadores", "crédito" y "reembolso", las palabras que el aviso de cambio tiene que usar bien.
- [[mecanismos-seguros-salud|Mecanismos de seguros de salud]] — las redes cerradas y la dirección del paciente hacia proveedores más baratos son mecanismos de costo que este node mira desde la comunicación.
- [[seguros-comportamiento-mundo-peru|Comportamiento y mercado de seguros (Mundo vs. Perú)]] — la desconfianza por falta de información en Perú es el riesgo de fondo de un aviso mal hecho.
- [[fenomenos-psicologicos|Fenómenos psicológicos clásicos]] — estado de replicación de la aversión a la pérdida (§5.4), base del encuadre del mensaje.
- [[material-visual-venta-consultiva|Material visual en la venta consultiva]] — la regla de reducir opciones y dar una recomendación clara se aplica al centro alternativo.
- [[transicion-venta-fria-a-opt-in|Transición de venta fría a opt-in]] — marco legal peruano del contacto comercial, que limita la llamada de redirección si ofrece un incentivo.
