# Seguros embebidos e Insurance-as-a-Service: qué hay, qué se sabe y dónde está la oportunidad

> Documento de investigación. Fuente persistente y versionada en el repositorio.
> Fecha de elaboración: 2026-10-28 · Última actualización: 2026-10-28 · Versión: v0.1 (exploratorio)
> Origen: pregunta de la persona usuaria: *"¿qué hay de las Insurance-as-a-Service o Embedded Insurance?"*, dentro del ciclo de digitalización de seguros.
> Método de `/trinidad` sin la pista social. Fuentes nuevas registradas en `research/fuentes/codice.md` (F-1195 a F-1217); reutiliza F-882, F-896, F-897, F-900, F-998, F-1043, F-1116, F-1145, F-1178 y F-1189.
> Solo fuentes públicas. **Todo lo nuevo se leyó por fragmentos de buscador (nivel N2)**: los sitios no se abren desde la sesión. Las cifras de conversión y de tamaño son de proveedores y firmas de estudios de mercado.

---

## 0. Qué es y qué no es este documento

Un primer mapa de dos cosas relacionadas. **Seguro embebido** (*embedded insurance*) es una forma de distribución: el seguro se ofrece dentro de la compra, el pago o la app de otro negocio. **Insurance-as-a-Service** (seguro como servicio) es la infraestructura que lo hace posible: las APIs y plataformas que dejan a una empresa que no es aseguradora cotizar, emitir y cobrar una póliza sin construir nada de seguros. No es un ramo ni un tipo de póliza (F-1197).

**No concluye** qué producto lanzar ni cuánto vale el mercado. Separa lo que se sabe de lo que se afirma, y pone lado a lado la **evidencia de conversión** (casi toda de proveedores) y la **evidencia de valor para la persona** (casi toda de reguladores y de casos de reparación).

## 1. En corto

1. **El seguro embebido es una tendencia real, pero su evidencia de resultados es de proveedores.** Hay muchas cifras de conversión (de 2% a 4% contra 15% a 50%; "hasta 10 veces más"), pero ninguna es independiente y ninguna mide renovación, siniestros pagados ni quejas (F-1196).
2. **Las estimaciones de tamaño no son comparables:** de US$ 270.000 millones (solo Asia) a US$ 950.000 millones (global) a 2030, con definiciones distintas (F-1197).
3. **En el Perú, la forma embebida más grande ya existe y no es digital: es el seguro atado al crédito.** El informe del PNUD halló que 97,8% del microseguro se vende por entidades financieras, casi todo saldo deudor, con siniestralidad de 16,7% (F-882). Lo nuevo (billeteras, retail, viajes) es pequeño: Pacífico dice que los embebidos no llegan a 1% de su portafolio (F-1203).
4. **La historia de los seguros complementarios es una advertencia con datos.** En el Reino Unido, el regulador halló que quien compra un complemento compara menos, y que en un producto solo 10% de la prima volvía como siniestros (F-1199); el seguro de protección de pagos terminó en más de £38.000 millones de reparación (F-1200). La teoría explica por qué el ocultamiento persiste (F-1201).
5. **La oportunidad está en hacerlo con valor visible.** Las medidas que propuso el regulador (adhesión diferida, sin casillas premarcadas, publicar la siniestralidad) son también un diseño que puede **ganar confianza** frente a un sector donde 48% desconfía (node de comportamiento).
6. **Tres combinaciones parecen las más prometedoras en el Perú** (hipótesis): servicio más seguro dentro del chat o la billetera (lo que hace Pacífico con Tsana y Yape), seguros por evento de alta frecuencia (viaje, entradas, celular), y seguros paramétricos ligados a crédito o a un evento (con el marco nuevo de la SBS). Ninguna tiene prueba de efecto.

## 2. Cómo funciona

### 2.1 La cadena

| Pieza | Qué hace | Ejemplo |
|---|---|---|
| **Plataforma de distribución** | El negocio donde la persona ya compra o paga; muestra la oferta en el momento justo | Billetera, tienda, app de viajes, banco, aerolínea |
| **Aseguradora o MGA** | Pone la cobertura, el precio y la emisión. El MGA (agente administrador general) puede manejar a los socios sin cargar el riesgo, o retenerlo | Pacífico en Yape; Chubb con Falabella |
| **Capa de APIs (seguro como servicio)** | Conecta ambas: la plataforma envía datos, recibe la cotización al instante y, si la persona acepta, se emite y se cobra en el mismo flujo | Proveedores como Root, Qover, Boost; en el Perú, Insurama con Rímac |

Fuente: BCG y páginas de proveedores (F-1195). En EE. UU. se exige aseguradora autorizada, producto aprobado y licencia de distribución para la plataforma; en el Perú, ver §4.3.

### 2.2 Seis formas que conviene distinguir

| Forma | Cómo se ve | Caso |
|---|---|---|
| **Atado al crédito** | La póliza viene con el préstamo o la tarjeta (desgravamen, protección de tarjeta) | Saldo deudor en el Perú (F-882); desgravamen en Chile (F-1145) |
| **Complemento de una compra** | Se ofrece en el pago: dispositivo, garantía, viaje | Insurama con tiendas de dispositivos; RedBus y Ticketmaster (F-1203) |
| **En billetera o súper-app** | Seguro dentro de la app de pagos, cobrado de la misma cuenta | Yape con Pacífico (F-1116); Mercado Pago; GCash y Grab (F-896, F-897) |
| **Con un servicio** | El seguro entrega un servicio (teleconsulta, orientación) además de pagar | Seguro Salud Yape; Tsana (nodes de ramos y de digitalización) |
| **Paramétrico incluido** | Paga solo al ocurrir un evento medido, ligado a un insumo o crédito | Pula (África; F-900) y el marco peruano de 2026 (F-1204) |
| **Beneficio laboral** | El empleador lo da como beneficio | Betterfly (entró y habría salido del Perú; F-1203) |

## 3. Qué hay en el mundo y en América Latina

| Tema | Qué dicen las fuentes | Confianza |
|---|---|---|
| **Tamaño a 2030** | Asia: US$ 270.000 millones de primas (McKinsey); global: US$ 722.000 millones (InsTech London) y de US$ 210,9 a 950,6 mil millones (Mordor); comercio electrónico: ~US$ 22.000 millones en 2025 (Gallagher Re) | **Baja**: no son comparables (F-1197) |
| **Qué es** | Un modelo de distribución, no un ramo; cada firma cuenta productos distintos | Media |
| **Regional** | 250 insurtechs al cierre de 2023, 57% en Brasil y 18,4% en México; inversión de US$ 74,5 millones en 2023 frente a US$ 305,6 millones en 2021 (F-1198). Las finanzas embebidas de la región se estiman en US$ 9.630 millones o en US$ 35.400 a 38.800 millones según la firma | **Baja** (F-1198) |
| **Casos** | Mercado Libre (sistema cerrado de pagos, crédito y seguros), Mercado Pago con Cardif y Chubb, Nubank, Rappi con Chubb, Bys en Brasil | Anuncios, sin resultados (node de digitalización §16) |
| **Lo que no hay** | Primas embebidas de la región; datos de Pier, Justos o Falabella Seguros; renovación o siniestralidad de cualquier embebido | Ausencia confirmada |

## 4. Perú

### 4.1 Lo que existe

| Actor | Qué hace | Fuente y nivel |
|---|---|---|
| **Seguros atados al crédito** | 97,8% del microseguro se vende por entidades financieras, casi todo saldo deudor; siniestralidad de 16,7% frente a 40% regional | PNUD (F-882, N1) |
| **Pacífico en Yape** | Vida (S/ 5,99 al mes por S/ 10.000), salud con teleconsulta (S/ 9,90), celular (desde S/ 4,90), fraude (S/ 4,99), SOAT y emprendedores | F-1116 (N2) |
| **Pacífico en otros socios** | Accidentes para viajes terrestres (RedBus), no presentación (Ticketmaster); el BCP ofrece *Efectivo Protegido*. Pacífico dice que **los embebidos no llegan a 1% de su portafolio** | F-1203 (N2) |
| **Rímac** | Alianza con Grupo EFE (vida y salud en más de 200 tiendas, web y app) y con Insurama (protección de dispositivos con iShop y miStore de Xiaomi) | F-1203 (N2) |
| **Chubb y Falabella** | Seguro Falabella (hospitalización en dólares, vida, desgravamen) | F-1203 (N2) |
| **Corredor digital** | Ategia, con alianzas comerciales | F-1203 (N2) |
| **Interseguro** | Protección de tarjetas desde S/ 12,90 al mes (declarado) | F-1189 (N2) |
| **Insurtech** | Betterfly entró con Interseguro y habría salido tras tres años; Avla lanzó Iglú para hogares | F-1203 (N2) |

**Un matiz de precio.** El Celu Seguro de Pacífico aparece desde S/ 4,90 en Yape, pero una póliza de muestra de 2023-2024 fija S/ 38,90 al mes con renovación mensual automática. La prima parece depender del valor del equipo; no está confirmado.

### 4.2 Demanda declarada

Un estudio de BCG citado en Gestión dice que **43% de los peruanos** compraría un seguro integrado a otro producto o servicio, y cerca de **60%** de los jóvenes de ingreso medio-bajo (F-1203). Es **intención declarada**, de una consultora cuyo socio promueve el modelo en un evento del gremio, y las personas suelen decir más de lo que hacen. Sirve como pista, no como demanda.

### 4.3 Regulación

- La **venta por socios** se regula como **comercialización**: el comercializador es quien tiene un contrato con la aseguradora para facilitar la contratación; **los bancaseguros y las emisoras de dinero electrónico también lo son**. Los **seguros masivos**, simples y estandarizados, pueden venderse por comercializadores y bancaseguros. La aseguradora responde por la capacitación y la conducta (F-1204; leído por resúmenes).
- La **venta a distancia** se permitió y se facilitó con normas de 2017 y 2021; hay un proyecto de 2025 sobre ciberseguridad y un solo factor biométrico en el régimen simplificado (F-1204; F-1178).
- El **reglamento de banca como servicio** (Res. SBS 01747-2026) trata cuentas, créditos y pagos; la responsabilidad ante el cliente y la SBS recae en la entidad financiera. **No hallé que regule vender seguros dentro de apps bajo ese marco** (F-1189).
- Un proyecto de **seguros paramétricos** (mayo de 2026) modifica el reglamento de comercialización y los habilita por bancaseguros y sistemas a distancia (F-1204).
- **No confirmé** si una empresa no financiera (retail, servicios públicos, plataforma) puede ser comercializadora ni qué registro se exige.

## 5. Evidencia: conversión frente a valor para la persona

### 5.1 Conversión (lo que dicen los proveedores)

Se afirma que el seguro buscado aparte convierte 2% a 3% y que como complemento en el pago llega a 20% a 50%; que bien diseñado convierte 15% a 20% y mal diseñado 2% a 4%; que una aerolínea subió 400% su tasa de contratación; que un estudio de Swiss Re y KASKO halla hasta 10 veces más (F-1196). **Ninguna es independiente, ninguna mide qué pasa después** (renovación, siniestros pagados, quejas) y las cifras atribuidas a McKinsey y Deloitte no se pudieron verificar. Que **sea más fácil comprar** no prueba que **valga la pena comprar**: lo que se mide es la fricción, no la protección.

### 5.2 Valor para la persona (lo que dicen reguladores y casos)

| Evidencia | Qué muestra | Fuente |
|---|---|---|
| **Estudio de mercado del regulador británico (2014)** | En los complementos, quien compra compara menos, compara peor y es menos sensible al precio; ventaja del que vende en el punto de venta; en GAP solo **10% de la prima** volvía como siniestros | F-1199 |
| **Medidas propuestas** | Adhesión diferida (no cerrar la venta en el punto de venta del auto), **sin casillas premarcadas**, **publicar la siniestralidad**, mejorar la presencia en comparadores. El resultado final de las medidas no se confirmó | F-1199 |
| **Seguro de protección de pagos del Reino Unido** | Más de 32,4 millones de reclamos y más de **£38.000 millones** en reparación; el caso Plevin permitió reclamar comisiones superiores a 50% de la prima | F-1200 |
| **Chile, seguros atados al crédito** | Al pasar a licitación, los precios bajaron −62,1% en desgravamen y −34,3% en incendio y sismo en las primeras 105 licitaciones; la CMF halló en 2022 un rango de −4,11% a −77,34% en 20 licitaciones, con 3 alzas, y advierte que bajó el interés de las aseguradoras. El autor de Coloma aplicó la ley que evalúa (no es independiente) y "el precio bajó" no prueba que el deudor esté mejor | Coloma (F-1145, N1) |
| **Teoría** | El ocultamiento del precio de complementos puede persistir en equilibrio competitivo cuando hay consumidores miopes | F-1201 |
| **Supervisión europea** | Indicadores de valor por dinero, seguimiento de la protección de crédito y un marco de riesgos de distribución y punto de venta | F-1202 |
| **Perú, microseguro** | Siniestralidad de 16,7% (2024) y 18 productos con 0%; ambiguo: poco valor, productos nuevos o siniestros que no se registran | PNUD (F-882, N1) |

**Lectura (inferencia mía).** El problema no es que el seguro esté embebido, sino que **la persona que elige no es la que paga la comisión**, que el seguro **no se ve** hasta que falla y que la compra ocurre **donde se compara poco**. Si la plataforma cobra una comisión alta por vender, el incentivo es vender mucho y no vender bien. En los casos con datos (GAP, PPI, desgravamen), eso terminó con regulación y reparación. **En el Perú no hay publicada la siniestralidad ni la comisión de ningún producto embebido nuevo.**

## 6. Dónde está la oportunidad (hipótesis; ninguna con prueba en el Perú)

Ordenadas por cuán bien calzan con lo que ya se sabe y con las señales de mercado.

| # | Oportunidad | Por qué | Qué hay que cuidar |
|---|---|---|---|
| EM1 | **Servicio más seguro dentro del chat o la billetera**: orientación, teleconsulta o asistencia incluida, y el seguro como siguiente paso | Es lo que hacen Pacífico con Tsana y Yape (nodes de ramos §13 y §15); el valor se **ve** antes del siniestro | Evidencia de efecto ausente; costo de atender; escalamiento a humano |
| EM2 | **Seguro por evento de alta frecuencia** (viaje terrestre, entradas, celular, retiro de efectivo) con precio cobrado en la misma compra | Ya existe en pequeño (F-1203); el pago pequeño en el momento puede reducir la postergación | Que el siniestro sea fácil de reclamar; ver siniestralidad |
| EM3 | **Paramétrico ligado a crédito o a un evento** (clima, El Niño costero) | Marco nuevo de la SBS (F-1204); pago rápido y automático; Pula como referencia (F-900) | Riesgo de base (que el índice no coincida con la pérdida); educación del cliente |
| EM4 | **Trabajadores de plataformas** (reparto, transporte) con accidentes y salud dentro de la app | El modelo `lapuerta` ya modela el trabajo en plataforma digital (~7% de la población en el esquema) | Tipo de contrato del trabajador; quién paga |
| EM5 | **Seguro en retail con tarjeta propia**, vendido en tienda y por app | Alianzas de Rímac con Grupo EFE y de Chubb con Falabella (F-1203) | Venta presionada en tienda; la comisión (§5.2) |
| EM6 | **Embebido en salud con farmacia o red propia** (receta, medicinas) | Efecto medio de la farmacia en adherencia (nodes de ramos §8) | Costo y quién paga |
| EM7 | **Herramientas de seguro como servicio para aseguradoras medianas** (APIs, cobro por billetera, emisión) | Insurama con Rímac; reglamento de banca como servicio | No hallé una plataforma peruana propia |
| EM8 | **Embebido que gana confianza**: publicar siniestralidad, mostrar la comisión, cancelar en un paso, adhesión diferida | Son las medidas del regulador británico (F-1199) y responden a una desconfianza de 48% | Costo; puede bajar la conversión de corto plazo |

**Un diseño que combina la oportunidad con la lección.** Un embebido bien hecho sería: precio visible en el pago; sin casillas premarcadas; cancelación en un paso; **un siniestro pagado visible en la misma app** (hipótesis M3 y M4 del node de ramos); y la siniestralidad y la comisión publicadas. Eso es lo contrario del complemento oculto y convierte la lección del regulador en ventaja de confianza.

## 7. Riesgos y puntos ciegos

1. **Valor bajo disfrazado de conveniencia:** siniestralidad baja, comisiones altas, renovación automática que la persona olvida (el Celu Seguro se renueva cada mes).
2. **Quién tiene la relación:** la plataforma puede quedarse con el cliente y la aseguradora quedar como proveedor de cobertura; es el tema de la pregunta 6 del foresight.
3. **Responsabilidad ante un reclamo:** el cliente ve la marca del socio; la responsabilidad es de la aseguradora (F-1204). Hay que saber quién atiende y quién paga.
4. **Datos:** compartir datos entre la plataforma y la aseguradora (salud, ubicación, pagos) exige consentimiento y base legal; no verifiqué la ley de datos personales en esta ronda.
5. **Quienes menos comparan son los más expuestos:** poblaciones con poca educación financiera o poca conexión.
6. **Mercado pequeño hoy:** menos de 1% del portafolio de Pacífico; no se debe confundir la tendencia con el tamaño.
7. **Evidencia:** todo lo de conversión es de proveedores; el tamaño de mercado no concilia; no hay renovación ni siniestralidad publicadas; no hay estudio de campo de complementos en seguros.
8. **Lo que no se buscó:** Falabella, Ripley, Claro y Entel no aparecieron con embebidos en las fuentes; Mercado Libre y Rappi en el Perú, no hallé nada; la pista social; los costos reales de integración.

## 8. Preguntas que solo se cierran con datos propios

1. ¿Qué proporción de las pólizas vendidas por socios se renueva a 3 y 12 meses, frente a las vendidas por canal propio?
2. ¿Qué siniestralidad y qué tiempo de pago tiene cada producto embebido?
3. ¿Qué comisión o participación recibe cada socio y cómo cambia con la siniestralidad?
4. ¿Cuántas quejas y cancelaciones genera cada socio?
5. ¿Qué parte de quienes compran en el pago no sabía que lo había contratado?
6. ¿Qué embebidos atraen a quien no tenía seguro y cuáles solo reemplazan uno que ya tenía?

## 9. Límites

Todo lo nuevo es nivel N2 (fragmentos de buscador); no abrí ningún informe. La lista de casos de §10 la aportó la persona usuaria y se contrastó solo con fragmentos de buscador. El FCA, EIOPA y NBER se leyeron por extractos. Las cifras de conversión y tamaño son de proveedores y firmas de mercado. La pista social no se corrió. Las notas de Gestión que la persona usuaria está descargando pueden cambiar o precisar §4.

## 10. Otros terrenos: dónde se puede digitalizar y dónde no (más allá del seguro en sí)

Esta sección usa una lista de casos aportada por la persona usuaria (ejemplos de seguro como servicio y de banca como servicio fuera del seguro tradicional) y los contrasta con fragmentos de fuentes públicas. **Los casos se verificaron solo por fragmentos de buscador (N2); casi todo lo que dicen las empresas es autoinformado.** El foco es responder en qué terrenos conviene digitalizar y en cuáles no.

### 10.1 La regla que sale de los casos (inferencia mía)

Digitalizar rinde cuando se cumplen estas condiciones, ordenadas de más a menos importantes:

1. **El evento se mide con un dato externo y objetivo** (lluvia, vuelo, turno conectado, vulnerabilidad en una red). Entonces la cobertura se activa y se paga sola.
2. **No hace falta evaluar una pérdida con una persona** (peritaje, diagnóstico, discusión de un monto). Si hace falta, lo digital queda en los bordes: cotizar, pagar, avisar.
3. **El costo de la pérdida no lo fija un proveedor que el seguro no controla** (médicos, veterinarios). Si lo fija, la digitalización no baja el costo.
4. **La persona entiende qué compra y quién queda asegurado.**
5. **El riesgo de que el dato no coincida con la pérdida (riesgo de base) es bajo o corregible.**
6. **La comisión del socio no premia vender sin importar el valor** (§5).
7. **Hay evidencia independiente de resultados.** Casi nunca la hay.

### 10.2 Terreno por terreno

| Terreno | Casos de la lista | Qué se digitaliza bien | Qué no | Evidencia | En el Perú (fuentes públicas) | Veredicto |
|---|---|---|---|---|---|---|
| **Agro y clima (paramétrico)** | IBISA, Descartes | Activación por dato satelital y pago sin peritaje | El riesgo de base: que el índice no refleje la pérdida | Un ensayo en Kenia: el seguro con **fotos** subió la contratación frente al seguro índice (20% a 21%) y la confianza en 12 a 17 puntos; la demanda sube si se ven pagos (F-1209) | La Positiva lanzó uno ligado a El Niño en 2013; en 2017 su siniestralidad llegó a 125% y se anunciaron alzas; hay un seguro público catastrófico y un reglamento paramétrico de la SBS de 2026 (F-1217) | **Sí, con corrección del riesgo de base y con precio que resista un evento grande** |
| **Eventos y clima** | Sensible Weather, Companjon (no hallados); Beazley, REVO | Pago automático al cruzar un umbral de lluvia | Paga por el umbral, no por la pérdida; complementa al seguro tradicional | Descripciones de aseguradoras (F-1213) | No hallé oferta | **Sí, como complemento** |
| **Plataformas (repartidores, transporte)** | Qover con Deliveroo y Wolt | Cobertura que se activa al conectarse a la app | Quien trabaja en varias apps o fuera de ella | Solo del proveedor: tope de € 7.500 médicos, 90% de satisfacción autoinformada (F-1207) | No hallé producto vigente; Rappi anunció uno en 2020 y hubo reclamos sindicales por un seguro de accidentes (F-1217) | **Sí en la activación; falta saber qué queda fuera** |
| **Ciberseguridad para pymes** | Coalition, Cowbell | Escaneo continuo, alertas y respuesta; la prevención forma parte del producto | El pago de rescates y las exclusiones; que la pyme entienda | Cowbell: siniestralidad de 43% en 2022; Coalition: ~1,5% de asegurados con siniestro frente a ~6% del mercado, ambos de las propias empresas (F-1210) | Menos de 100 organizaciones con ciberseguro, según una consultora (F-1210) | **Sí; el valor está en la prevención, y hay un hueco grande de cobertura** |
| **Telecomunicaciones (micropagos con saldo prepago)** | Bima con Tigo y Airtel | Cobro de centavos con el saldo; alta masiva; pago por dinero móvil | Que la cobertura sea gratis condicionada al uso (puede ser un producto de fidelización más que de protección) | 500.000 suscriptores en Tanzania (2016); 50.000 reclamos por GHS 22 millones en Ghana (2020), de las empresas (F-1208) | No hallé caso en telcos peruanas | **Sí para llegar; falta medir el valor** |
| **Fintech, neobancos y súper-apps** | Chubb con Nubank, Rappi y Mercado Pago | Venta simple dentro de la app; cobro de la misma cuenta | La renovación y el siniestro no se muestran | Nubank Vida: 150.000 pólizas en el primer mes a ~US$ 2 al mes; antes, 20% tenía seguro de vida y 70% interés (F-1205) | Pacífico en Yape (F-1116, F-1203) | **Sí para productos simples; pedir renovación y siniestros** |
| **Viajes y retail con pago en cuotas** | Cover Genius con Booking y Ryanair; Klarna | Protección en el pago; pago de siniestros instantáneo (declarado) | **El costo de la protección sumado a las cuotas** es el complemento oculto que advirtió el regulador británico (§5.2) | Solo del proveedor (F-1206) | RedBus y Ticketmaster con Pacífico (F-1203) | **Sí, con precio visible y adhesión diferida** |
| **Movilidad y telemetría** | Tesla Insurance | Prima que se ajusta con la conducción | Que el puntaje prediga siniestros; el manejo de siniestros | Sin evidencia independiente; una publicación sectorial reporta pérdida técnica en 2024 y reguladores de California citaron demoras en siniestros (F-1214) | No hallé | **Cuidado: probar con grupo de control** |
| **Salud con servicio** | Sanitas Blua, Oscar con Holy Cross, Discovery Vitality | Teleconsulta, citas, autorizaciones sin papel | La capacidad, el costo médico y la continuidad (node de ramos §8) | Más de 3 millones de videoconsultas en Blua, sin resultados independientes (F-1215); Oscar cerró 2025 con siniestralidad de 87,4% (F-1170) | Tsana, Seguro Salud Yape | **Sí en los bordes; el servicio es lo que cuenta** |
| **Mascotas** | Fletch, Wrisk, FirstVet | Cita, teleconsulta veterinaria y copago en el punto de atención | **El costo lo fijan las veterinarias**, y suben; las quejas crecen | Reino Unido: 600 quejas en el primer trimestre de 2025 (+26%), 52% a favor del cliente (F-1211) | La Positiva (2020) y Mapfre; Rímac solo en una tesis (F-1211) | **Cuidado: digitalizar la cita no controla el costo** |
| **Alquiler (garantía)** | Rhino, The Guarantors | Cobro mensual junto con la renta | La persona no entiende que **asegura al propietario**; la cuota no se devuelve | Periodismo de investigación; algunas ciudades obligan a ofrecer alternativas al depósito (F-1212) | No hallé oferta | **Cuidado alto de conducta; solo con explicación clara** |
| **Asistencia B2B2C** | Mawdy (Mapfre) | Asistencias en el checkout de distribuidores | Sin datos de socios | Resultado de asistencia de Mapfre: de 207,2 a 256,0 millones de euros a nueve meses de 2025 (F-1216) | No hallé | **Sí; sin evidencia de resultados para el cliente** |

### 10.3 Dónde no (o no solo así)

- **Donde la pérdida se evalúa con una persona y el costo lo fija un tercero** (salud, mascotas, taller): lo digital ordena la entrada pero **no baja el costo**. Lo que decide es la red, el precio negociado y la capacidad.
- **Donde el producto confunde sobre quién está asegurado o qué se devuelve** (garantía de alquiler): digitalizar acelera una venta mal entendida.
- **Donde el dato no representa la pérdida** (paramétrico sin corrección de riesgo de base): se vende un seguro que no paga cuando se necesita, y la confianza se pierde.
- **Donde el socio vende sin que se vea el costo** (complementos en cuotas): es el patrón que el regulador británico y los casos de reparación mostraron (§5.2).
- **Donde no hay evidencia independiente de resultados** (casi todos los casos de esta tabla): se puede probar, pero no se debe escalar sin medir renovación, siniestros pagados y quejas.

### 10.4 Lo que esto dice sobre novedad en el Perú

- **El modelo de seguro embebido no es nuevo en el mercado peruano.** Existen la alianza de Rímac con Insurama (anunciada en febrero de 2024, con una expectativa de 20.000 a 25.000 clientes en su primer año en Perú y Chile) y con Grupo EFE, Pacífico con Yape, Chubb con Falabella y seguros de mascotas desde 2020 (F-1203, F-1217). Lo que no hay públicamente es **escala ni resultados**.
- **Lo que sí aparece nuevo, o poco explorado,** son los terrenos donde el dato decide: **paramétrico** (con reglamento de la SBS de 2026 y con un antecedente de pérdidas altas en 2017), **ciberseguro para pymes** (menos de 100 organizaciones aseguradas según una consultora), **plataformas** y **eventos**. Para el paramétrico, el contexto de El Niño costero 2026-2027 (node de El Niño) hace el tema urgente y el antecedente de 2013 hace el riesgo conocido.
- **La diferencia de fondo no está en "tener" un embebido, sino en cuatro decisiones:** quién tiene la relación con el cliente (la plataforma o la aseguradora), si se vende solo o con un servicio, si el precio y la comisión son visibles, y si se miden renovación y siniestros desde el primer día.

### 10.5 Hipótesis (para probar con datos propios)

| # | Hipótesis | Cómo probarla |
|---|---|---|
| EM9 | Un seguro paramétrico con corrección de riesgo de base (por ejemplo, con fotos o dato de campo) tiene más contratación y renovación que uno por índice puro | Comparar dos diseños con grupo de control |
| EM10 | El ciberseguro para pymes que incluye servicios de prevención reduce los siniestros respecto a uno sin ellos | Comparar frecuencia de siniestros por cohorte |
| EM11 | La cobertura por turno de plataformas deja sin proteger una parte relevante del tiempo de trabajo | Medir horas trabajadas conectado y no conectado |
| EM12 | En seguros de mascotas, la cita digital sube la asistencia a prevención pero no baja el costo del siniestro | Comparar costo por siniestro con y sin canal digital |
| EM13 | Un producto que se cobra con saldo o dinero móvil tiene más caducidad que uno con débito, si la persona no ve el valor | Comparar caducidad por esquema de cobro |
| EM14 | Mostrar el costo de la protección sumado a cuotas baja la contratación a corto plazo y sube la renovación | Prueba A/B de visibilidad del costo |

## Conexiones

- [[digitalizacion-seguros-mercados-emergentes|Digitalización en seguros en mercados emergentes]] — GCash, Grab, Pula, Mercado Pago, MetLife, estimaciones de tamaño y la pregunta de quién se queda con el valor.
- [[digitalizacion-ramos-vehicular-salud-microseguros|Digitalización por ramo]] — Seguro Salud Yape, Tsana, WhatsApp como señal (§15) y el microseguro atado al crédito.
- [[foresight-experiencia-futura-seguros-digitalizacion|Foresight de la experiencia futura de los seguros]] — "dónde vive la relación", finanzas abiertas, pagos del BCRP y banca como servicio.
- [[economia-conductual-seguros-literatura|Economía conductual de los seguros]] — sesgo del presente, atributos ocultos y por qué la gente compara poco.
- [[seguros-comportamiento-mundo-peru|Seguros: comportamiento y mercado, Mundo vs. Perú]] — desconfianza y brecha de protección.
- [[fenomeno-el-nino-impacto-personas|Impacto del Fenómeno El Niño en las personas]] — el paramétrico y el contexto de El Niño costero 2026-2027 (§10).
- [[conducta-humano-ia|Conducta humano-IA]] — IA que decide y venta conversacional dentro de una plataforma.
