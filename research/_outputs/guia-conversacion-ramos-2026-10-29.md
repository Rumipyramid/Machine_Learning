# Guía de conversación con los ramos

**Insumo para:** Gerencia de Digital, RIMAC · **Fecha:** 29-10-2026 · **Estado:** versión de trabajo 0.1
**Basada en:** `research/_nodes/valor-recurrencia-digital-seguros.md`, `research/_nodes/canal-servicio-siniestro-seguros.md`
y `research/_nodes/cliente-intermediado-bancaseguros-embebido.md`. Esta copia omite los datos propios de la compañía y
los documentos internos del equipo; la versión interna los trae en cada ficha.
Las fuentes se citan como (Autor, año) y con su número del registro de fuentes del proyecto (F-n). 🌐 marca contraste
fuera de LatAm; 📚, estudios canónicos anteriores a 2021.

---

## Para qué sirve esta guía

**No es una estrategia. Es la forma de abrir la conversación con cada ramo.** El benchmarking respondió qué sabemos
afuera. Lo que falta solo lo sabe cada ramo: su renovación, su cobranza, su margen y lo que hace su intermediario.

La guía propone tres pasos:

1. **Conversación con la gerente de Digital** (sección 1). Ella decide con qué ramos hablar, en qué orden y qué
   éxito se busca.
2. **Una conversación por ramo** (sección 3). Cada ficha tiene seis partes: lo que vemos en los datos, qué forma de
   valor aplica, evidencia externa, señales que pueden cambiar las reglas, preguntas que solo el ramo puede responder e
   hipótesis para probar juntos.
3. **Síntesis** (sección 4). Una plantilla para que cada conversación deje lo mismo y se pueda comparar.


---

## 1. Para la conversación con la gerente de Digital

Cinco preguntas que conviene cerrar con ella antes de citar a los ramos.

**1. ¿Qué cuenta como éxito digital?** Una meta de visitas mensuales premia entrar, no resolver. El seguro es de baja
frecuencia: un hábito necesita repetición frecuente en un contexto estable (Wood y Neal, 2007, F-888 📚). La propuesta
del benchmarking es medir **necesidades resueltas en el canal que mejor las resuelve** y su efecto en la renovación,
no sesiones.

**2. ¿Con qué ramos y en qué orden?** Propongo un criterio en vez de un orden fijo: empezar donde hay **mucho cliente
sin resolver en digital y una palanca cercana** que la compañía controla.

**3. ¿Qué dato pedimos antes de cada conversación?** La lista está en el Anexo A. El más importante es la
**permanencia**: renovación y persistencia por canal de origen y por uso digital. Sin ese dato no se puede decir si
lo digital retiene o solo atrae a quien ya se iba a quedar.

**4. ¿Quién es dueño de cada momento?** En varios ramos el cliente resuelve con otro: el banco, el empleador, el
corredor, la clínica o el taller. Antes de fijar metas por ramo conviene saber qué datos de ese tercero se pueden pedir
y bajo qué acuerdo.

**5. ¿Cómo se lleva la propuesta del equipo?**
Propuesta: las iniciativas que ya existan se llevan como hipótesis, no como decisiones. En la conversación con el ramo,
cada una se presenta como pregunta: "¿esto resuelve algo de tu cliente y cómo lo mediríamos?".

---

## 2. Lo que vale para todos los ramos

### 2.1 Tres hallazgos del benchmarking

- **Lo claro migra a digital y lo ambiguo llama.** En una aseguradora de salud de EE.UU., el portal bajó 29% las
  llamadas sobre información clara y subió las de pólizas y reclamos; en total, quien usaba el portal llamaba 14% más
  (Kumar y Telang, 2012, F-850 🌐 📚; cuasi experimento, leído por resumen).
- **El siniestro decide la permanencia, no el canal.** Tras un siniestro, la probabilidad de cambiar de aseguradora
  sube 35% en 180 días, aunque 94% esté satisfecho (LexisNexis, 2023, F-890 🌐). Lo que más predice la salida es el
  monto o la pérdida total (CCC, 2024, F-950 🌐).
- **El ancla explica la permanencia.** Hipoteca, empleo, crédito vehicular, billetera o corredor: el cliente llega y se
  queda por un tercero. Lo crítico es el momento en que el ancla se suelta (P3; Brockett y otros, 2008, F-852 📚: la
  primera cancelación predice la fuga del hogar).

### 2.2 Tres reglas de lectura para las conversaciones

1. **Separar selección de efecto.** Quien usa el app ya es distinto de quien no lo usa. Compararlos sin control
   exagera el valor del app. Hace falta grupo de control o despliegue escalonado (P1, Anexo C).
2. **Visitas no son resolución.** Una visita puede ser una búsqueda frustrada.
3. **Satisfacción no es permanencia.** 86% de quienes reclamaron estaba satisfecho y 41% de ellos probablemente
   cambiaría en un año (Accenture, 2014, F-892 🌐 📚).

### 2.3 Beneficios: ¿el cliente debería entrar al app por eso?

**La evidencia no respalda que más visitas a beneficios se conviertan en permanencia del seguro.** Hay tres razones.

- **La frecuencia diaria ya tiene dueño.** Yape tiene 15,9 millones de usuarios activos al mes (F-869). Interbank lleva
  los pagos a WhatsApp y Mibanco da créditos completos por ese canal (F-973). Competir por frecuencia es jugar en la
  cancha del banco. *Inferencia.*
- **El mecanismo de la lealtad en retail no existe en un seguro.** Los mensajes push subieron el gasto 14% y
  duplicaron el canje en un programa de sellos de supermercados de Indonesia, porque cada compra acerca al premio
  (Bies y otros, 2021, F-808 🌐; leído completo). En un seguro la prima es fija: no hay "comprar más". Lo que sí se
  trasladaría es el aumento del canje, que es costo. *Inferencia.*
- **Corregida la autoselección, el efecto casi desaparece.** El efecto real de un programa de lealtad es unas siete
  veces menor que el estimado sin corregir (Leenheer y otros, 2007, F-805 📚). Los programas de bienestar laboral
  seleccionan más de lo que transforman (Jones y otros, 2019, F-854; Song y Baicker, 2019, F-855 🌐).

**Lo que sí tiene respaldo o señal:** el beneficio ligado al trabajo del seguro. Prevención con efecto medido (la
retroalimentación telemática cambia la forma de manejar, F-442), adherencia del paciente crónico (Roebuck y otros,
2011, F-937 🌐 📚) o consumo diario que alimenta el producto (Cling Cling de Caser, España, F-982; sin cifras).
Betterfly, que llegó a Perú con un modelo de bienestar, salió en 2025 y hoy se define como plataforma para empresas por
suscripción que cubre todo el ecosistema de salud (F-964).


**Pregunta para cada ramo:** ¿qué beneficio de tu producto resuelve algo del riesgo asegurado, y cuál es solo tráfico?

### 2.4 Cobranza: la molestia de pagar pesa más que el monto

- En un mercado de salud subsidiado de EE.UU., dejar de pagar respondía más a la molestia de pagar que al precio: un
  plan que pasó de US$0 a US$3 al mes perdió 24% de sus afiliados en un mes (McIntyre y otros, 2021, F-962 🌐; working
  paper leído completo). Ese estudio no prueba el débito automático: prueba qué pasa por defecto cuando el cliente deja
  de pagar.
- En Perú, 38,4% de los reclamos de seguros ante Indecopi en 2023 fue por contratación o cargo indebido (PNUD, 2025,
  F-902). Un débito preseleccionado puede leerse así.
- **Señal:** la iniciación de pagos de TAPP (BCRP, piloto en diciembre de 2026, F-971) permitiría un pago recurrente
  autorizado una vez y revocable. En Brasil, pasar la cobranza de primas al pago instantáneo Pix redujo las demoras y
  bajas del pago con boleto (Microinsurance Network, F-986). *Hipótesis para Perú.*


---

## 3. Fichas por ramo

### 3.1 Vida individual

**Lo que vemos.**
La versión interna trae aquí cartera, digitalización por canal de venta, conversión de los flujos de venta y reclamos
de cobranza.

**Qué forma de valor aplica.** Retención (persistencia) y venta cruzada asistida. No costo de servir: la frecuencia
natural de necesidad es muy baja.

**Evidencia y casos.**
- 🌐 En India, la persistencia al mes 13 es 86% en venta en línea, 75% en corredores y 67% en agentes individuales;
  puede ser selección (F-956).
- En Perú, solo 20% compraría un seguro de forma digital (SBS y CAF, 2022, F-903).
- Porto Seguro (Brasil): 84% de su venta digital es venta cruzada a clientes existentes, y sus 45 mil corredores siguen
  siendo el motor (F-865).
- La percepción de canibalización del canal digital reduce el compromiso del agente, pero solo cuando hay pocas
  oportunidades de mercado (Sharma y Gassenheimer, 2009, F-924 📚).

**Señales.** Pago recurrente consentido por TAPP (F-971). Seguros de vida que se usan en vida (Bradesco Vida Viva,
F-905; sin cifras). Consumo diario que alimenta un seguro de ahorro (F-982).

**Preguntas para el ramo.**
1. ¿Cuál es la persistencia a 13 y 25 meses por canal de venta y por medio de pago?
2. ¿Qué hace el asesor al entregar la póliza, y se puede escribir como protocolo?
3. ¿De qué cartera hablamos cuando decimos "Vida Individual"?
4. ¿Dónde falla la cobranza: medio de pago, fecha, monto o aviso?
5. ¿Por qué Vida Endosable e Inversión Global no convierten en el app?

**Hipótesis para probar.**
- *Del benchmarking:* el app como canal híbrido en vida: trazar el lead hasta la póliza en vez de medir la venta 100%
  digital.

### 3.2 Vida por bancaseguros y worksite

**Lo que vemos.**
La versión interna trae aquí cartera, digitalización por rol (titular y dependiente) y la presencia del seguro en el
app del banco socio.

**Qué forma de valor aplica.** Alcance, con el riesgo de que la relación sea del banco o del empleador. El
intermediario es el dueño de la relación (Cummins y Doherty, 2006, F-180 📚).

**Evidencia y casos.**
- **Regulación peruana:** desde septiembre de 2025, las entidades deben ofrecer al menos un crédito de consumo que no
  exija desgravamen; en el hipotecario sigue siendo condición (Res. SBS 890-2025, F-952; leído por prensa).
- En Perú, 38,4% de los reclamos de seguros ante Indecopi en 2023 fue por contratación o cargo indebido (PNUD, 2025,
  F-902).
- Chile: la licitación obligatoria bajó el precio del desgravamen 62,1% (Coloma, 2019, F-904 📚).
- 🌐 Reino Unido: la venta inadecuada de seguros atados a créditos (PPI) terminó en devoluciones masivas (FCA, 2020,
  F-953).
- Brasil: 72% de clientes de bancos digitales dice querer ofertas de seguro en su app bancaria, ante una pregunta
  hipotética formulada por un proveedor (Cover Genius, 2021, F-987). Nubank llegó a 1,6% de penetración de seguros sobre
  su base en 2023 (F-863).
- 🌐 Worksite: en un caso de afiliación por autoservicio con descuento por planilla, la caída fue 45% mayor a la
  esperada (Society of Actuaries, 2014, F-958 📚).

**Señales.** Finanzas abiertas en Perú, en proyecto: bancos desde 2028 y seguros "desde 2029" según la prensa, sin
confirmar (F-970). Banking as a Service aprobado, sin aseguradoras (F-974). Seguros inclusivos por bancaseguros: más de
3 millones de pólizas de S/1 a S/30 en un competidor (F-966).

**Preguntas para el ramo.**
1. ¿Qué permite hoy el acuerdo con el banco sobre datos, consentimiento y presencia en su app?
2. ¿Qué pasa con el cliente cuando termina el crédito o deja el empleo? ¿Se le ofrece continuidad?
3. ¿Cuántos clientes eligieron el crédito sin desgravamen desde septiembre de 2025?
4. ¿Qué hace Recursos Humanos por el asegurado, y qué le falta?
5. ¿Tiene sentido activar al dependiente, que no paga ni eligió?

**Hipótesis para probar.**
- *Del benchmarking:* separar la meta digital por puerta de entrada y diseñar la salida del ancla: un aviso de
  continuidad cuando termina el crédito, probado con grupo de control.

### 3.3 SOAT y Vehicular

**Lo que vemos.**
La versión interna trae aquí cartera, digitalización, reparto del reporte de choque entre app y teléfono, y reclamos
por indemnización.

**Qué forma de valor aplica.** Confianza en el siniestro y prevención (telemática). En SOAT, el canal digital prueba que
sirve para vender, no que el cliente vuelva (P1).

**Evidencia y casos.**
- 🌐 El siniestro son dos momentos. Solo 9% reporta el siniestro por web o app, y la satisfacción es 33 puntos mayor
  entre quienes reciben el estado del siniestro en digital (J.D. Power, 2017, F-947 📚).
- 🌐 Entre quienes califican mal su experiencia digital de siniestro, 52% probablemente no renovará; entre quienes la
  califican excelente, 4% (J.D. Power, 2025, F-872).
- 🌐 Quienes piden asistencia vial por app tienen cerca de 30% menos probabilidad de calificar mal la experiencia; lo
  atribuyen a la ubicación exacta del teléfono (Agero, F-951; posible selección).
- La retroalimentación telemática redujo el exceso de velocidad entre 11% y 13% en un experimento aleatorizado nacional
  (F-442 🌐). Justos (Brasil) no renueva a cerca de 2% con peor nota de manejo (F-870).
- 42% compraría su seguro de auto en el concesionario (Accenture, 2023, F-905).

**Señales.** Suscripción mensual que premia al buen conductor desde el primer mes (Darwin Seguros, Brasil, F-965).
Reporte de choque armado en minutos por la telemetría del teléfono (F-960 🌐). Indemnización instantánea en siniestros
simples (Porto Seguro, F-865).

**Preguntas para el ramo.**
1. ¿El choque por teléfono es un fallo del canal o el diseño correcto? ¿Por qué el flujo solo opera de día?
2. ¿Qué parte del siniestro hacen el taller y el concesionario, y qué datos comparten?
3. ¿Cuál es la renovación del SOAT comprado en digital frente a otros canales?
4. ¿Por qué se concentran los reclamos en la asesoría para la indemnización del SOAT?
5. ¿Qué siguiente uso tiene sentido para alguien que compra una vez al año?

**Hipótesis para probar.**
- *Del benchmarking:* el aviso por teléfono y el seguimiento en digital, con avisos de estado probados con grupo de
  control.

### 3.4 Salud: EPS y AMI

**Lo que vemos.**
La versión interna trae aquí cartera y digitalización por rol (titular y dependiente) y el reparto entre app y
teléfono de reembolsos, buscador de clínicas y médico a domicilio.

**Qué forma de valor aplica.** Costo de servir (reembolsos), prevención en crónicos y confianza en la atención. Ojo: en
salud, el engagement selecciona buenos riesgos (P1).

**Evidencia y casos.**
- 🌐 En un plan de salud de EE.UU., quienes usaban el portal retenían 96,9% contra 90,5% de quienes no, en una cohorte
  emparejada; es observacional y del propio plan (Turley y otros, 2012, F-851 📚).
- 🌐 La telemedicina directa al consumidor aumenta el acceso pero no reduce el gasto (Ashwood y otros, 2017, F-934 📚).
- 🌐 La adherencia a la medicación en crónicos baja el uso y el costo total (Roebuck y otros, 2011, F-937 📚).
- 🌐 Alan (Francia) multiplicó por 2,3 sus usuarios diarios con un juego de salud; no ha medido el efecto en
  retención (F-859).
- Perú: Pacífico vende un seguro de salud en Yape y ofrece orientación médica por WhatsApp 24/7 en Tsana (F-938 a
  F-942).
- La compra de salud se negocia en el hogar (Davis, 1976, F-236 📚).

**Señales.** Plataformas para empresas que cubren todo el ecosistema de salud: seguro complementario, médicos,
farmacias y exámenes preventivos (Betterfly, F-964). WhatsApp como canal de atención (F-939).

**Preguntas para el ramo.**
1. ¿Qué resuelven el corredor y Recursos Humanos por el asegurado de EPS?
2. ¿Qué busca la gente cuando llama para encontrar una clínica, y por qué no lo encuentra en el app?
3. ¿Qué haría falta para que el médico a domicilio tenga flujo digital?
4. ¿Cuántos pacientes crónicos hay, cuánto gastan y qué programa tienen?
5. ¿Qué parte de la relación vive en la clínica y no en la aseguradora?

**Hipótesis para probar.**
- *Del benchmarking:* reemplazar la meta de adopción por resolución en el primer canal y costo por atención, empezando
  por el buscador de clínicas.

### 3.5 Generales y hogar

**Lo que vemos.**
La versión interna trae aquí cartera y digitalización.

**Qué forma de valor aplica.** Prevención y confianza en el siniestro, en especial ante eventos naturales.

**Evidencia y casos.** Es el ramo con menos evidencia externa sobre canal.
- En Perú, solo cerca de 3% de los hogares tiene seguro contra desastres, en un país sísmico (node de comportamiento y
  mercado de seguros).
- **El ancla en hogar es la hipoteca:** más de 90% de las viviendas aseguradas contra terremoto lo está porque el banco
  lo exige, y solo 12% mantiene el seguro al terminar de pagar (PNUD, 2025, F-902; dato del sector citado por prensa).
- 🌐 Lemonade, nativa digital, tiene una retención anual en dólares de 85%, afectada por no renovaciones deliberadas en
  hogar (F-857). Ser digital no garantiza retención.
- 🌐 Reino Unido: tras prohibir subir el precio a quien renueva por inercia, los precios de auto bajaron; en hogar no
  hubo relación (FCA, 2025, F-886).

**Señales.** Seguro paramétrico con reglamento propio en Perú: paga al superar un umbral, sin peritaje, pero solo lo
contratan entidades públicas o empresas para una colectividad (F-786). Los paramétricos con pago por celular protegen
consumo y activos en Kenia (F-792 🌐), con riesgo base alto (F-976 🌐). El Niño Costero 2026-27 hace urgente la
conversación (node de El Niño).

**Preguntas para el ramo.**
1. ¿Cuántas pólizas de hogar llegan por la hipoteca, y qué pasa cuando el crédito termina?
2. ¿Qué siniestros tiene el hogar y por dónde se avisan?
3. ¿Hay un tomador colectivo con quien probar un paramétrico (microfinanciera, gremio, municipio)?
4. ¿Qué es la cartera que queda fuera de la meta y por qué?

**Hipótesis para probar.**
- *Del benchmarking:* aviso preventivo ante El Niño a clientes de zonas expuestas, medido en siniestralidad y
  renovación contra un grupo sin aviso.

---

## 4. Qué se lleva de cada conversación

Una plantilla igual para todos los ramos, para poder comparar:

| Campo | Qué anotar |
|---|---|
| Forma de valor que el ramo prioriza | Una o dos de las cinco: costo de servir, retención, venta cruzada, prevención, confianza en el siniestro |
| Momento que más importa | Venta, entrega, pago, siniestro, renovación o salida del ancla |
| Quién es dueño de ese momento | La compañía, el banco, el empleador, el corredor, la clínica o el taller |
| Dato que existe y dato que falta | Sobre todo, permanencia por canal y por uso digital |
| Hipótesis elegida | Una sola, con su medida y su grupo de control |
| Qué necesita el ramo de Digital | Flujo, dato, acuerdo con un tercero o nada |

---

## Anexo A · Datos para pedir antes de cada conversación

La lista completa está en el informe P1 (Anexo D). Los cinco que más cambian la conversación:

1. **Renovación y persistencia** a 13 y 25 meses, por canal de origen, por medio de pago y por uso digital.
2. **Motivos de contacto por canal**, con volumen, para separar lo claro de lo ambiguo.
3. **Contactos por necesidad resuelta** y recontacto a 7 días, por flujo.
4. **Uso de cada beneficio** y su relación con la renovación.
5. **Qué gestiones solo se pueden hacer en un canal**, para saber cuánto del registro es obligatorio y no elegido.

Si un dato no existe, eso también es un hallazgo.

## Anexo B · Escala de evidencia

🟢 A revisión por pares · 🔵 B regulador u oficial · 🟡 C consultora o empresa · 🟠 D prensa o blog · 🔴 E opinión.

## Anexo C · Referencias con enlace

Cada fuente citada en el informe, con su número del registro de fuentes del proyecto. Los enlaces llevan a la fuente original o, si no estuvo accesible, al resumen o la cobertura desde donde se leyó. Los documentos internos se indican como tales.

- **F-180** · Cummins, J. D. & Doherty, N. A. (Journal of Risk and Insurance 73(3):359-396; DOI 10.1111/j.1539-6975.2006.00180.x) (2006). *The Economics of Insurance Intermediaries*. 🟢 A. [Ver fuente](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1539-6975.2006.00180.x)
- **F-236** · Davis, H. L. (1976). *Decision Making Within the Household (Journal of Consumer Research, 2(4):241-260)*. 🟢 A. [Ver fuente](https://academic.oup.com/jcr/article-abstract/2/4/241/1820423)
- **F-442** · Equipo de investigación en seguridad vial (autoría no capturada en detalle) (2026). *A national randomized field experiment testing the impact of simulated usage-based insurance programs on driver safety (*Accident Analysis & Prevention*)*. 🟢 A. [Ver fuente](https://www.sciencedirect.com/journal/accident-analysis-and-prevention · https://clinicaltrials.gov/study/NCT06101251)
- **F-786** · SBS — Resolución SBS N.° 02260-2026 (vía El Peruano, LP Derecho, Infomercado) (2026). *Reglamento de Seguros Paramétricos*. 🔵 B. [Ver fuente](https://elperuano.pe/noticia/304594-sbs-aprueba-reglamento-de-seguros-parametricos-para-su-funcionamiento-en-el-mercado-peruano · https://lpderecho.pe/reglamento-de-seguros-parametricos-resolucion-sbs-02260-2026/)
- **F-792** · Janzen, S. A. & Carter, M. R. (2019). *After the Drought: The Impact of Microinsurance on Consumption Smoothing and Asset Protection (American Journal of Agricultural Economics, 101(3):651-671)*. 🟢 A. [Ver fuente](https://ideas.repec.org/f/pja593.html)
- **F-805** · Leenheer, J.; van Heerde, H.; Bijmolt, T.; Smidts, A. (2007). *Do loyalty programs really enhance behavioral loyalty? An empirical analysis accounting for self-selecting members (Int. J. Res. Mark. 24(1):31-47)*. 🟢 A. [Ver fuente](https://repository.tilburguniversity.edu/items/3fc12a59-7823-4842-9792-de0262adaea7)
- **F-808** · Bies, S. M. T. A.; Bronnenberg, B. J. & Gijsbrechts, E. (International Journal of Research in Marketing 38(4):877-899; DOI 10.1016/j.ijresmar.2021.02.001) (2021). *How push messaging impacts consumer spending and reward redemption in store-loyalty programs*. 🟢 A. [Ver fuente](https://doi.org/10.1016/j.ijresmar.2021.02.001)
- **F-850** · Kumar, A. & Telang, R. (Information Systems Research 23(3-1):721-737) (2012). *Does the Web Reduce Customer Service Cost? Empirical Evidence from a Call Center*. 🟢 A. [Ver fuente](https://doi.org/10.1287/isre.1110.0390)
- **F-851** · Turley, M. et al. (American Journal of Managed Care) (2012). *Patient portal use and health plan membership retention (Kaiser Permanente Northwest, My Health Manager)*. 🟢 A. [Ver fuente](https://pmc.ncbi.nlm.nih.gov/articles/PMC4215918)
- **F-852** · Brockett, P. L.; Golden, L. L.; Guillen, M.; Nielsen, J. P.; Parner, J.; Pérez-Marín, A. M. (Journal of Risk and Insurance 75(3):713-737) (2008). *Survival Analysis of a Household Portfolio of Insurance Policies: How Much Time Do You Have to Stop Total Customer Defection?*. 🟢 A. [Ver fuente](https://ideas.repec.org/a/bla/jrinsu/v75y2008i3p713-737.html)
- **F-854** · Jones, D.; Molitor, D.; Reif, J. (Quarterly Journal of Economics 134(4):1747-1791) (2019). *What Do Workplace Wellness Programs Do? Evidence from the Illinois Workplace Wellness Study*. 🟢 A. [Ver fuente](https://econpapers.repec.org/RePEc:oup:qjecon:v:134:y:2019:i:4:p:1747-1791.)
- **F-855** · Song, Z. & Baicker, K. (JAMA) (2019). *Effect of a Workplace Wellness Program on Employee Health and Economic Outcomes: A Randomized Clinical Trial*. 🟢 A. [Ver fuente](https://hcp.hms.harvard.edu/publication/effect-workplace-wellness-program-employee-health-and-economic-outcomes-randomized)
- **F-857** · Lemonade, Inc. (Form 10-K FY2025 y cartas a accionistas 2025, SEC) (2026). *Form 10-K FY2025; Shareholder letters Q2-Q4 2025*. 🔵 B. [Ver fuente](https://www.sec.gov/Archives/edgar/data/1691421/000169142126000016/lmnd-20251231.htm)
- **F-859** · Alan (carta a accionistas Q2 2025) (2025). *Alan - 2025 Q2 Letter to Shareholders*. 🟠 D. [Ver fuente](https://alan.com/en/blog/discover-alan/a/alan-2025-q2-letter-to-shareholders)
- **F-863** · Nubank y Chubb (comunicados y prensa especializada) (2024). *Nubank and Chubb reach 2 million active insurance policies in Brazil*. 🟠 D. [Ver fuente](https://coverager.com/nubank-and-chubb-reach-2-million-active-insurance-policies-in-brazil/)
- **F-865** · Porto Seguro (presentación a inversionistas vía Quartr; release 1T25; CQCS) (2025). *Porto Seguro investor presentation; Release 1T25; entrevista a Patrícia Chacon (COO)*. 🟡 C. [Ver fuente](https://cqcs.com.br/noticia/patricia-chacon-coo-da-porto-seguro-revela-como-a-seguradora-esta-se-preparando-para-o-futuro/)
- **F-869** · Gestión; Perú Retail; El Comercio (cobertura de Yape, BCP) (2025-2026). *Yape: seguro de salud, venta de SOAT y resultados 2025*. 🟠 D. [Ver fuente](https://www.peru-retail.com/yape-se-consolida-como-gigante-financiero-con-1-8-millones-de-prestamos-mensuales/)
- **F-870** · Bloomberg Línea (Justos, Brasil) (2025). *Ribbit e Kaszek reforçam aposta na insurtech Justos com aporte de R$ 92 milhões*. 🟠 D. [Ver fuente](https://www.bloomberglinea.com.br/startups/ribbit-e-kaszek-reforcam-aposta-na-insurtech-justos-que-capta-r-92-milhoes/)
- **F-872** · J.D. Power (2025). *2025 U.S. Claims Digital Experience Study*. 🟡 C. [Ver fuente](https://www.jdpower.com/business/press-releases/2025-us-claims-digital-experience-study/)
- **F-886** · Financial Conduct Authority (Reino Unido) (2025). *Evaluation Paper 25/2: Our general insurance pricing practices (GIPP) remedies*. 🔵 B. [Ver fuente](https://www.fca.org.uk/publications/corporate-documents/evaluation-paper-25-2-general-insurance-pricing-practices-remedies)
- **F-888** · Wood, W. & Neal, D. T. (Psychological Review 114(4)) (2007). *A new look at habits and the habit-goal interface*. 🟢 A. [Ver fuente](https://dornsife.usc.edu/wendy-wood/wp-content/uploads/sites/183/2023/10/wood.neal_.2007psychrev_a_new_look_at_habits_and_the_interface_between_habits_and_goals.pdf)
- **F-890** · LexisNexis Risk Solutions (2023). *Moment of Truth: claims satisfaction and auto insurance switching (whitepaper)*. 🟡 C. [Ver fuente](https://www.claimsjournal.com/news/national/2023/06/08/317385.htm)
- **F-892** · Accenture (vía PropertyCasualty360) (2014). *Customer loyalty: it's more than just claims satisfaction*. 🟡 C. [Ver fuente](https://www.propertycasualty360.com/2014/11/01/customer-loyalty-its-more-than-just-claims-satisfaction/)
- **F-902** · Inga Falcón, P. (por encargo de la Oficina de Perú del PNUD y su Iniciativa de Seguros y Financiamiento de Riesgos) (2025). *Informe de diagnóstico de microseguros en el Perú (15 de diciembre de 2025)*. 🔵 B. PDF aportado por la usuaria; URL pública no verificada en esta sesión.
- **F-903** · SBS y CAF (citada vía el diagnóstico del PNUD, F-902) (2022). *Encuesta de Capacidades Financieras del Perú 2022 (resultados sobre seguros)*. 🔵 B. Cita secundaria en F-902; documento original no consultado.
- **F-904** · Coloma C., F. (Instituto de Economía, Pontificia Universidad Católica de Chile; ex Superintendente de Valores y Seguros) (2019). *Licitación de los seguros asociados a los créditos hipotecarios: algunos resultados y propuestas de mejoramiento (Documento de Política Pública)*. 🔵 B. PDF aportado por la usuaria (Documento de Política Pública, Instituto de Economía UC); URL pública no verificada.
- **F-905** · Saldanha, K. & Staehle, T. (Accenture) (2023). *Seeing the people behind the policies: Accenture's Global Insurance Consumer Study 2023*. 🟡 C. DOCX aportado por la usuaria; URL pública no verificada en esta sesión.
- **F-924** · Sharma, D. & Gassenheimer, J. B. (European Journal of Marketing 43(7/8):1076-1091) (2009). *Internet channel and perceived cannibalization: Scale development and validation in a personal selling context*. 🟢 A. [Ver fuente](https://doi.org/10.1108/03090560910961524)
- **F-934** · Ashwood, J. S.; Mehrotra, A.; Cowling, D.; Uscher-Pines, L. (Health Affairs 36(3):485-491; DOI 10.1377/hlthaff.2016.1130) (2017). *Direct-To-Consumer Telehealth May Increase Access To Care But Does Not Decrease Spending*. 🟢 A. [Ver fuente](https://www.rand.org/pubs/external_publications/EP67074.html)
- **F-937** · Roebuck, M. C.; Liberman, J. N.; Gemmill-Toyama, M.; Brennan, T. A. (Health Affairs 30(1):91-99) (2011). *Medication Adherence Leads To Lower Health Care Use And Costs Despite Increased Drug Spending*. 🟢 A. [Ver fuente](https://scholarhub.vn/publication/:slug/ef630f12-adfb-453e-8e75-a80a76b8da93)
- **F-938** · Trome y Diario Correo (publirreportajes sobre el seguro de salud de Pacífico vendido en Yape) (c. 2025-2026). *Atenciones médicas en línea con seguro de salud Yape*. 🟠 D. [Ver fuente](https://diariocorreo.pe/publireportaje/atenciones-medicas-en-linea-con-seguro-de-salud-yape-noticia/)
- **F-939** · Cortez Carpio, J. (líder de innovación y diseño, laboratorio de innovación La Cápsula de Pacífico Salud), publicación en LinkedIn; captura aportada por la usuaria (2026 (27 de agosto; año confirmado por la usuaria)). *¿Y si el mejor canal para una experiencia de salud no siempre es una app o una web? (orientación médica por WhatsApp en Tsana)*. 🔴 E. Captura de LinkedIn aportada por la usuaria (enlace acortado lnkd.in/d9WJzB8g).
- **F-942** · Gestión (entrevista a Guillermo Garrido-Lecca, CEO de Pacífico Salud) (2025). *Pacífico Salud explora zonas para expandir su red y afianza apuesta por diversificar segmentos (21 de julio de 2025)*. 🟠 D. Notas de la usuaria a partir de capturas de gestion.pe; URL no aportada.
- **F-947** · J.D. Power (vía Insurance-Canada y FenderBender) (2017). *2017 U.S. Auto Claims Satisfaction Study*. 🟡 C. [Ver fuente](https://insurance-canada.ca/2017/10/26/jd-power-auto-claims-satisfaction/)
- **F-950** · CCC Intelligent Solutions (vía Repairer Driven News) (2024). *Crash Course 2024 / estudio de experiencia del siniestro de auto (2.400 asegurados con siniestro propio)*. 🟡 C. [Ver fuente](https://www.repairerdrivennews.com/2024/10/08/ccc-customers-see-repair-process-as-single-cohesive-experience-between-repairers-insurers/)
- **F-951** · Agero (blog corporativo) (s.f. (c. 2020-2023)). *Consumer Insights: How Coverage Expectations and Request Channel Can Impact NPS*. 🟠 D. [Ver fuente](https://blog.agero.com/consumer-insights-how-coverage-expectations-and-request-channel-can-impact-nps)
- **F-952** · Superintendencia de Banca, Seguros y AFP (Resolución SBS N.° 00890-2025), vía Agencia Andina y diario El Peruano (2025). *Modificación de las normas sobre el seguro de desgravamen (publicada en marzo de 2025; vigente desde el 9 de septiembre de 2025)*. 🔵 B. [Ver fuente](https://andina.pe/agencia/noticia-entidades-financieras-deben-ofrecer-productos-crediticios-y-sin-seguro-desgravamen-1021963.aspx)
- **F-953** · Financial Conduct Authority (Reino Unido) (2020). *FCA publishes PPI complaints deadline final report (abril 2020) y datos mensuales de devoluciones de PPI*. 🔵 B. [Ver fuente](https://www.fca.org.uk/news/press-releases/fca-publishes-ppi-complaints-deadline-final-report)
- **F-956** · Cafemutual (prensa especializada), con datos del regulador de seguros de India (IRDAI) (s.f. (año de los datos no indicado)). *Products bought online show significantly higher persistency than those sold through agents*. 🟠 D. [Ver fuente](https://cafemutual.com/news/insurance/39099-products-bought-online-show-significantly-higher-persistency-than-those-sold-through-agents)
- **F-958** · Society of Actuaries (EE.UU.), boletín NewsDirect (2014). *Enrolling Voluntary Benefits Is Risky Business*. 🟡 C. [Ver fuente](https://www.soa.org/news-and-publications/newsletters/newsdirect/2014/september/ndn-2014-iss69-760oop/enrolling-voluntary-benefits-is-risky-business)
- **F-960** · Insurance Journal (sobre Cambridge Mobile Telematics, Claims Studio) (2020). *Accident Reports Now Ready Minutes After Crash on Smartphone, Says Telematics Firm*. 🟠 D. [Ver fuente](https://www.insurancejournal.com/news/national/2020/01/10/554252.htm)
- **F-962** · McIntyre, A. L.; Shepard, M. & Wagner, M. (NBER Working Paper 28630; preparado para AER Papers & Proceedings) (2021). *Can Automatic Retention Improve Health Insurance Market Outcomes?*. 🟡 C. [Ver fuente](https://www.nber.org/papers/w28630)
- **F-964** · Gestión (con declaraciones de Betterfly al Diario Financiero) (2025). *Chilena Betterfly cierra operación en Perú y cuatro países más: ¿cuál es la razón? (18 de marzo de 2025)*. 🟠 D. Nota aportada por la usuaria (recopilación de Gestión).
- **F-965** · Gestión (cobertura del Insurance Day 2025 de Apeseg) (2025). *Insurance Day 2025: historias reales que están transformando el sector asegurador (26 de mayo de 2025)*. 🟠 D. Nota aportada por la usuaria (recopilación de Gestión).
- **F-966** · Gestión (entrevista a Mónica Rivas, gerente de Bancaseguros y Ecosistemas Credicorp de Pacífico Seguros) (2024). *Pacífico Seguros: "Queremos llegar a millones de personas más con los seguros inclusivos" (19 de mayo de 2024)*. 🟠 D. Nota aportada por la usuaria (recopilación de Gestión).
- **F-970** · Superintendencia de Banca, Seguros y AFP — proyecto de Reglamento General del Sistema de Finanzas Abiertas (bloque I prepublicado con la Res. SBS N.° 02433-2026, 5 de octubre de 2026; bloque II el 19 de octubre), vía Gestión (21 de octubre de 2026), El Peruano y Cuatrecasas (2026). *Finanzas abiertas: datos de cuentas de ahorro podrán ser compartidos*. 🔵 B. [Ver fuente](https://elperuano.pe/noticia/307111-que-cambios-propone-la-sbs-para-las-finanzas-abiertas-revisa-el-proyecto-normativo)
- **F-971** · Banco Central de Reserva del Perú — TAPP, vía Gestión (2 de septiembre y 13 de octubre de 2026), Infobae y Cuatrecasas; Circular 0017-2026-BCRP (2026). *TAPP: plataforma pública de pagos inmediatos*. 🟠 D. [Ver fuente](https://gestion.pe/tu-dinero/bcrp-pronto-revolucionara-pagos-en-peru-con-masivo-sistema-como-funcionara-tapp-noticia/)
- **F-973** · Gestión (sobre Interbank, Mibanco, Caja Arequipa y Banco de la Nación) (2025-2026). *Plin WhatsApp: la apuesta de Interbank para pagar sin salir del chat (31 de octubre de 2025); Bancos y cajas empiezan a dar créditos y permitir pagos por WhatsApp (10 de febrero de 2026)*. 🟠 D. Nota aportada por la usuaria (recopilación de Gestión).
- **F-974** · Superintendencia de Banca, Seguros y AFP — Resolución SBS N.° 01747-2026, vía El Peruano y Cuatrecasas (2026). *Reglamento de Banking as a Service (publicado el 3 de julio de 2026)*. 🔵 B. [Ver fuente](https://elperuano.pe/noticia/299414-mas-competencia-y-nuevas-soluciones-sbs-publica-reglamento-para-banking-as-a-service)
- **F-976** · Jensen, N. D.; Barrett, C. B. & Mude, A. G. (American Journal of Agricultural Economics 98(5):1450-1469) (2016). *Index Insurance Quality and Basis Risk: Evidence from Northern Kenya*. 🟢 A. [Ver fuente](https://www.ilri.org/knowledge/publications/index-insurance-quality-and-basis-risk-evidence-northern-kenya)
- **F-982** · Caser Seguros (notas de prensa propias; Funds Society) (2019-2020). *Cling Cling: seguro de ahorro por consumo*. 🟡 C. [Ver fuente](https://www.caser.es/conocenos/actualidad/productos-y-servicios/caser-presenta-una-solucion-innovadora-de-ahorro-facil-y-por-consumo)
- **F-986** · Microinsurance Network (artículo de su sección de publicaciones; autoría individual no indicada) (s.f. (página vista el 2026-10-29; © 2026)). *Open insurance for inclusion: what will it really take?*. 🟡 C. [Ver fuente](https://microinsurancenetwork.org/posts/open-insurance-for-inclusion-what-will-it-really-take)
- **F-987** · Cover Genius (encuesta encargada a Momentive.ai, unidad de investigación de SurveyMonkey) (2021 (publicado el 30 de julio de 2021)). *The Embedded Insurance Report: Brazil*. 🟡 C. [Ver fuente](https://covergenius.com/resources/reports/embedded-insurance-brazil/)
