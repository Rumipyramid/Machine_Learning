# Inventario de intervenciones: qué cambió la adopción y la conducta

**Insumo para:** Gerencia de Digital, RIMAC · **Fecha:** 29-10-2026 · **Estado:** versión de trabajo 0.1
**Basado en:** `research/_nodes/intervenciones-adopcion-conducta.md` y los nodes del benchmarking. Esta copia omite
los ejemplos con datos propios de la compañía.

**Cómo leer las cifras.** Cada intervención lleva su fuente (F-n) y su rigor: 🟢 A revisión por pares, 🔵 B oficial,
🟡 C consultora, empresa o working paper, 🟠 D prensa, 🔴 E opinión o eco de cita. **(R)** marca las cifras leídas solo
en resúmenes de búsqueda, sin abrir el texto. 🌐 marca contraste fuera de América Latina; 📚, estudios anteriores
a 2021.

**Cómo leer la población.** Cada fila describe a quién se aplicó (ingreso, zona, país, tamaño de muestra). No se
fijó un segmento único: la columna de transferibilidad (sección 6) dice qué tan cerca está del cliente peruano.

---

## Conclusión

1. **Cuándo y cómo se cobra pesa más que el mensaje.** Cobrar el seguro en la cosecha, cuando hay liquidez, llevó la
   contratación de 5% a 72% en Kenia (F-988, 🟢 A, R). Pagar y renovar por el celular se asocia a 17,4 puntos más de
   renovación en el seguro nacional de salud de Ghana, sobre todo en informales (F-1031, 🟢 A, observacional, R). Dejar de pagar responde más a la molestia de pagar que al monto
   (F-962, 🟡 C). Un periodo de gracia en microcrédito subió las ganancias, pero triplicó el no pago (F-998, 🟢 A, R).
2. **Acceso no es uso.** Seguros y cuentas gratis o subsidiados se adoptan y se abandonan: en Nicaragua, menos de 10%
   seguía afiliado al año de vencer el subsidio (F-989, R); en Kenia, el afiliado mediano no usó su seguro gratis
   (F-991, R); en Chile, solo 3% usó con regularidad una cuenta gratuita (F-1002, R).
3. **Ver un siniestro pagado sostiene la recompra.** En India, que cobre un vecino pesa casi como cobrar uno mismo
   (F-990, 🟢 A, R). En China, un amigo informado sube la contratación como bajar 13% la prima (F-993, R). En México,
   el valor del microseguro de vida fue la rapidez del pago (F-896, 🟡 C).
4. **Los recordatorios funcionan, pero poco, y depende de quién habla.** Suben el ahorro 6% (incluye Perú, F-994, R)
   y la puntualidad de pago entre 7% y 9% (F-997, R). En Filipinas, el SMS solo funcionó con el nombre de un asesor
   conocido (F-999, R). En Colombia, la visita personal superó a la carta (F-1020, R). El efecto decae entre mensajes
   (F-1022, R).
5. **La conducta cambia cuando el producto devuelve información útil.** La telemetría con retroalimentación redujo el
   exceso de velocidad entre 11% y 13%, y el efecto se sostuvo tras la intervención (F-442, 🟢 A). Poder revisar el
   saldo construyó confianza y ahorro en México (F-1001, R).
6. **Muchas métricas que se celebran no prueban conducta.** Descargas, afiliaciones automáticas, usuarios diarios y
   millones de pólizas embebidas son métricas de alcance. Pocas fuentes publican uso, permanencia o siniestralidad
   (sección 4).

---

## 1. Qué digitalizan los referentes y por qué canal

Cada celda trae un ejemplo con fuente. "Sin evidencia" significa que no se encontró un caso documentado.

| Momento | App propia | WhatsApp o chat | Agente digital o IA | Embebido en otro | SMS o USSD |
|---|---|---|---|---|---|
| **Venta** | Venta cruzada a clientes existentes (Porto Seguro, F-865) | Pólizas simples vendidas por WhatsApp (MetLife con Klimber, F-965) | Asistente de IA que ofrece seguros (Mercado Pago, F-954) | Seguro al comprar un brasier, un pasaje o una entrada (F-965, F-967); billeteras (F-863, F-954) | Compra por código USSD (Turaco con Airtel, F-981) |
| **Onboarding** | Sin evidencia de efecto | Sin evidencia | Sin evidencia | Afiliación por defecto: ~90% de adopción, pero muchos no saben que están cubiertos (F-1027) | Sin evidencia |
| **Cobranza** | Débito automático: 26% de los asegurados peruanos (F-903) | Pagos en el chat (Plin, F-973) | Sin evidencia | Prima descontada en la cosecha (F-988) o en planilla (F-958) | Prima por dinero móvil (M-Pesa, F-980); Pix en Brasil (F-986) |
| **Siniestro** | Indemnización instantánea en siniestros simples (Porto, F-865) | Reclamos por WhatsApp (Turaco, F-981) | Telemetría que arma el reporte de choque (F-960) | Paramétrico: paga sin aviso del cliente (F-980, F-786) | Pago por dinero móvil (F-980, F-981) |
| **Renovación** | No renovar a malos conductores por telemetría (Justos, F-870) | Sin evidencia | Sin evidencia | Sin evidencia | Recordatorio y renovación automática en curso (Ghana, F-887) |
| **Servicio** | Portal de reembolsos y consultas (F-850, F-851) | Orientación médica 24/7 (Pacífico, F-939) | Chat de urgencias virtuales (Oscar, F-858) | Sin evidencia | Sin evidencia |

**Lectura.** La venta y la cobranza son los momentos más digitalizados por terceros. El onboarding es el vacío más
grande: no se encontró ningún experimento publicado, y la cifra que circula atribuida a LIMRA es un eco de cita
(F-1028, 🔴 E).

---

## 2. Para qué lo hacen: objetivo declarado contra resultado medido

| Caso | Objetivo declarado | Resultado medido y publicado | Brecha |
|---|---|---|---|
| Seguro embebido en LatAm (Klimber, Leonisa, Mercado Pago) | Inclusión y penetración | Millones de asegurados (F-965, F-985, F-954) | Sin siniestralidad, renovación ni uso posterior |
| Turaco (África) | Protección a quien no tiene seguro | 1,5 millones de asegurados; pagos en menos de 3 días (F-981) | Sin siniestralidad ni renovación |
| Seguros inclusivos de un competidor peruano | Inclusión y resiliencia | Más de 3 millones de pólizas; S/141 millones pagados en 68 mil casos (F-966) | Sin renovación ni uso |
| Alan Play (Francia) | Retención y venta cruzada | Usuarios diarios ×2,3 (F-859) | Retención no medida |
| Betterfly en Perú | Crecimiento de doble dígito | Salida del país en 2025 (F-964, F-372) | Fracaso documentado |
| Seguro abierto en Brasil | Competencia y elección | Menos de 10.000 consentimientos activos tras cinco años (F-983) | Fracaso de adopción |
| Bima Sugam (India) | "El UPI de los seguros" | Sin cifras; cinco plazos incumplidos (F-975) | Sin resultado |
| Afiliación automática al SIS (Perú) | Cobertura universal | Más de 20 millones de asegurados (F-1012) | Sin datos de uso |
| Yape con DNI (Perú) | Inclusión financiera | 1,3 millones incluidos según la empresa (F-1006); dos millones de primeros créditos formales y cerca de 18 millones de usuarios, según el CEO de Credicorp (F-1036) | En 2022, 19% tenía billetera y solo 12% pagaba con ella; el acceso lleva tres años estancado por conectividad y educación financiera (F-1036) |
| Pix (Brasil) | Digitalizar pagos e incluir | Adopción de 91,7% (67,8% en hogares de menor ingreso) (F-1004) | Sin efecto causal probado en el bienestar de los más pobres |
| M-Pesa (Kenia) | Inclusión | Se asocia a la salida de la pobreza de 2% de los hogares (F-1000) | Cifra discutida |

**Patrón.** El objetivo declarado casi siempre es inclusión o penetración. Lo que se publica es alcance. Lo que se mide
con rigor (uso, permanencia, bienestar) aparece casi solo en estudios académicos, y muchas veces es nulo o pequeño.

---

## 3. Inventario de intervenciones

Columnas: a quién se aplicó · momento y tipo · mecanismo que buscaba activar · efecto y duración · costo · si cambió
conducta real · rigor y fuente.

### 3.1 Seguros

| Intervención y población | Momento · tipo | Mecanismo | Efecto y duración | Costo | ¿Conducta real? | Rigor · fuente |
|---|---|---|---|---|---|---|
| Telemetría con retroalimentación y microincentivo · 1.449 conductores, EE.UU. 🌐 | Uso · producto | Retroalimentación y meta | Exceso de velocidad −11% a −13%; frenado brusco −16% a −21%; **se sostuvo** tras la intervención | Incentivo de US$100 | Sí, manejo medido | 🟢 A · F-442 |
| Cobrar la prima en la cosecha · agricultores por contrato, Kenia | Adquisición y pago · producto | Liquidez y sesgo del presente | Contratación 72% contra 5% (R); una temporada | No publicado | Sí, prima cobrada | 🟢 A · F-988 |
| Pasar al plan gratis a quien deja de pagar · bajos ingresos, EE.UU. 🌐 | Pago · opción por defecto | Inercia y molestia de pagar | Retuvo 14% al año; más jóvenes y sanos | No publicado | Sí, permanencia sin pago | 🟡 C · F-962 |
| Subsidio temporal a la prima · informales urbanos, Nicaragua 📚 | Adquisición y renovación · precio | Precio | 20% se afilió; **menos de 10% seguía** al año de vencer (R) | No publicado | No sostenida | 🟢 A · F-989 |
| Seguro de salud gratis por un año · 789 informales, Kenia | Onboarding y uso · precio | Quitar la barrera de precio | El afiliado mediano **no lo usó** (R) | Una póliza anual | No | 🟢 A · F-991 |
| Ayuda para registrarse más subsidio de un año · ~6.000 hogares, Indonesia | Adquisición · acompañamiento y precio | Fricción y precio | 30% de afiliación; más de la mitad no logró registrarse (R) | No publicado | Sí, parcial | 🟢 A · F-1011 |
| Haber visto pagar un siniestro · hogares rurales, India | Siniestro y recompra · experiencia | Experiencia reciente y aprendizaje social | El pago al vecino pesa casi como el propio; decae (R) | No aplica | Sí, recompra | 🟢 A · F-990 |
| Amigo capacitado sobre el seguro · 5.300 hogares, China | Adquisición · prueba social | Información por redes | Como bajar 13% la prima (R) | No publicado | Sí, contratación | 🟢 A · F-993 |
| Cupones de descuento contra educación · pastores, Etiopía 📚 | Adquisición · precio contra información | Precio contra conocimiento | Cupones suben la compra de forma duradera; educación sube el conocimiento, **no** la compra (R) | No publicado | Sí (cupones); no (educación) | 🟢 A · F-977 |
| Pago rápido y justo · microseguro de vida, México 📚 | Siniestro · operativo | Confianza | 17 horas de procesamiento; pago a los 9 días; el pago esperado servía de garantía para pedir prestado | No publicado | Valor percibido, sin medir permanencia | 🟡 C · F-896 |
| Pagar y renovar por USSD con dinero móvil · seguro nacional de salud, Ghana | Pago y renovación · canal | Menos fricción para pagar | Renovación +17,4 puntos frente a pagar en oficina; más en informales (R) | No publicado | Sí, renovación (observacional: puede haber selección) | 🟢 A · F-1031 |
| Pix en la cobranza de primas · Brasil | Pago · infraestructura | Menos fricción que el boleto | Menos demoras y bajas, sin cifra | No publicado | Sin medir | 🟡 C · F-986 |
| Afiliación por defecto en microseguro móvil | Onboarding · opción por defecto | Inercia | ~90% de adopción; muchos no saben que están cubiertos (R) | No publicado | **No**: métrica de alcance | 🟡 C · F-1027 |
| Avisar el estado del siniestro en digital · EE.UU. 🌐 📚 | Siniestro · operativo | Reducir la incertidumbre | +33 puntos de satisfacción (asociación) | No publicado | Satisfacción, no permanencia | 🟡 C · F-947 |
| Siniestro 100% digital · EE.UU. 🌐 | Siniestro · canal | Autoservicio | Falla 39% en hogar y 33% en auto; quien termina con una persona califica 11 puntos peor | No publicado | Fracaso documentado | 🟡 C · F-183 |
| Programas de bienestar laboral · EE.UU. 🌐 | Uso · prevención | Hábitos e incentivo | Sin efecto en gasto ni salud; **seleccionan** a quien ya estaba sano | No publicado | No | 🟢 A · F-854, F-855 |
| Juego de salud en el app (Alan Play) · Francia 🌐 | Uso · gamificación | Hábito | Usuarios diarios ×2,3; retención no medida | No publicado | **No probada**: métrica de uso | 🟠 D · F-859 |
| Pasos de comprensión en la compra de vida · EE.UU. 🌐 | Venta · simplificación | Comprensión | Mejoran el recorrido de compra (experimentos de industria) | No publicado | Intención y comprensión | 🟡 C · F-22 |
| Prohibir subir el precio a quien renueva por inercia · Reino Unido 🌐 | Renovación · regulación | Corregir la inercia explotada | Bajó la práctica y los precios de auto; sin efecto en hogar | Costo de cumplimiento | Sí, precios | 🔵 B · F-886 |
| Licitación obligatoria del seguro del crédito · Chile 📚 | Venta · regulación | Competencia | Desgravamen −62,1% | No publicado | Sí, precio pagado | 🔵 B · F-904 |
| Prima pagada por el Estado en paramétricos · Kenia y México | Adquisición · modelo | Quitar la barrera de compra | Escala que la venta voluntaria no logra; en México, más siembra e ingreso tras el pago | Presupuesto público | Sí | 🔵 B, 🟡 C · F-979, F-984 |

### 3.2 Microfinanzas y ahorro

| Intervención y población | Momento · tipo | Mecanismo | Efecto y duración | Costo | ¿Conducta real? | Rigor · fuente |
|---|---|---|---|---|---|---|
| Recordatorios mensuales de ahorro · Bolivia, **Perú** y Filipinas | Uso · nudge | Atención limitada | Ahorro +6% (R) | No publicado | Sí | 🟢 A · F-994 |
| Cuenta de ahorro con compromiso · Filipinas 📚 | Adquisición y uso · arquitectura | Sesgo del presente | La abrió 28%; saldo +81 puntos a 12 meses (R) | No publicado | Sí | 🟢 A · F-995 |
| Grupos con metas públicas y SMS · 2.687 clientes de microcrédito, **Chile** | Uso · prueba social | Compromiso público | Depósitos ×3,7; una tasa más alta **no** tuvo efecto (R) | No publicado | Sí | 🟢 A · F-996 |
| SMS contra incentivo para pagar el crédito · 1.121 prestatarios, Uganda | Pago · nudge e incentivo | Olvido contra precio | Pago a tiempo +7% a 9%; el SMS rindió como bajar 25% el costo (R) | Muy bajo | Sí | 🟡 C · F-997 |
| Periodo de gracia de dos meses · 845 clientas, India | Pago · producto | Liquidez | Ganancias +30%; **incumplimiento de 2% a 7%** (R) | No publicado | Sí, con efecto adverso | 🟢 A · F-998 |
| SMS con el nombre del asesor · Filipinas | Pago · mensajero | Relación personal | Solo funcionó con el nombre del asesor conocido: impagos −41% (R) | Muy bajo | Sí, condicionada | 🟡 C · F-999 |

### 3.3 Pagos, billeteras y banca

| Intervención y población | Momento · tipo | Mecanismo | Efecto y duración | Costo | ¿Conducta real? | Rigor · fuente |
|---|---|---|---|---|---|---|
| Dinero móvil con red de agentes (M-Pesa) · Kenia 📚 | Adopción · modelo | Menor costo de transacción | Salida de la pobreza de 2% de los hogares (R; discutida) | No publicado | Sí | 🟢 A · F-1000 |
| Tarjeta de débito para la transferencia social · **México** | Uso · operativo | Acceso y verificación del saldo | Ahorro adicional de 2% del ingreso a 2 años (R) | No publicado | Sí | 🟢 A · F-1001 |
| Cuenta bancaria gratuita · Malawi, Uganda y **Chile** | Adquisición · precio | Quitar el costo | Uso regular: 17%, 10% y 3%; **sin efecto** en ahorro (R) | Comisiones subsidiadas | No | 🟡 C · F-1002 |
| Sueldo depositado en cuenta · 3.136 obreros, Bangladesh | Onboarding y uso · operativo | Aprender usando | Aprendieron a usar la cuenta y evitar cobros abusivos (R, sin cifra) | No publicado | Sí | 🟡 C · F-1003 |
| Terminales de pago en tiendas pequeñas · **México** | Adopción · red | Externalidad de red | Adopción de tarjeta de los demás +21% (R) | No publicado | Sí | 🟢 A · F-1005 |
| SMS para reactivar billeteras inactivas · Kenia | Abandono · nudge | Recordar | **Sin efecto** (piloto sin control) | Bajo | No | 🟡 C · F-1026 |
| Banca en línea · EE.UU. 🌐 📚 | Uso · canal | Autoservicio | Más retención controlando selección; más transacciones totales | No publicado | Sí | 🟢 A · F-847 |
| Revelar al inicio que se habla con un bot · ~6.000 clientes de servicios financieros, Asia | Venta · IA conversacional | Sesgo contra las máquinas | Compra −79,7% frente a no revelarlo; revelarlo tarde atenúa el efecto (R) | No aplica | Sí, compra | 🟢 A · F-1034 |
| Comunicación más clara sobre la cuenta · 124.000 ahorristas, Reino Unido 🌐 | Uso · información | Atención | Casi nadie cambió de cuenta (R) | No publicado | **No** cambió conducta | 🟢 A · F-1033 |

### 3.4 Retail y lealtad

| Intervención y población | Momento · tipo | Mecanismo | Efecto y duración | Costo | ¿Conducta real? | Rigor · fuente |
|---|---|---|---|---|---|---|
| Insignias y tablas de posiciones · centro comercial, Asia | Uso · gamificación | Logro y comparación | Ventas +21% a +23%; **se sostuvo** al retirarlo; el cupón (+31,7%) se desvaneció | No publicado | Sí | 🟢 A · F-807 |
| Mensajes push en un programa de sellos · 46.504 miembros, Indonesia | Uso · nudge | Acercar el premio | Gasto +14%; canje ×2; cada mensaje suma menos | No publicado | Sí, pero el canje es costo | 🟢 A · F-808 |
| Programa de lealtad corregido por autoselección · Países Bajos 📚 | Uso · incentivo | Recompensa | Efecto real 7 veces menor que el ingenuo | No publicado | Poco | 🟢 A · F-805 |
| Seguir usando el app de la marca · programa internacional de lealtad | Uso · canal | Recencia | Gasto +19% a +48% en tres meses si se sigue usando; quien deja de usarla compra menos (R) | No aplica | Sí; la descarga sola no | 🟢 A · F-1035 |

### 3.5 Salud

| Intervención y población | Momento · tipo | Mecanismo | Efecto y duración | Costo | ¿Conducta real? | Rigor · fuente |
|---|---|---|---|---|---|---|
| SMS semanales de adherencia · 431 adultos, Kenia rural 📚 | Uso · nudge | Recordar | 53% contra 40% con adherencia alta a 48 semanas (R) | No publicado | Sí | 🟢 A · F-1007 |
| Promotores que viven de vender productos · aldeas, Uganda | Prevención · acompañamiento y modelo | Visitas, educación y acceso | Mortalidad infantil −27% en 3 años (R) | US$68 por año de vida | Sí | 🟢 A · F-1008 |
| Servicio confiable más un incentivo pequeño · 134 aldeas, India 📚 | Uso repetido · operativo e incentivo | Postergación | Vacunación completa 39% contra 18% y 6% (R) | US$28 contra US$56 por niño | Sí | 🟢 A · F-1009 |
| SMS de vacunación · **Guatemala** | Uso · nudge | Recordar | Mejor puntualidad (42% contra 31%); **sin efecto** en completar (R) | No publicado | Parcial | 🟢 A · F-1010 |
| Afiliación automática al SIS · **Perú** | Adquisición · opción por defecto | Inercia | 2,5 millones de afiliados nuevos (R) | No publicado | **Sin datos de uso** | 🟠 D · F-1012 |

### 3.6 Educación

| Intervención y población | Momento · tipo | Mecanismo | Efecto y duración | Costo | ¿Conducta real? | Rigor · fuente |
|---|---|---|---|---|---|---|
| SMS frecuentes a padres · colegios de bajos ingresos, **Chile** | Uso · información | Cerrar la brecha de información | Matemáticas +0,08 a 0,09 DE; asistencia mínima +4,5 a 4,7 puntos; 18 meses (R) | Bajo | Sí | 🟢 A · F-1013 |
| Videos sobre lo que rinde estudiar · **Perú** (MineduLAB) | Permanencia · información | Corregir creencias | Deserción −18% (R); escalado a 500.000 alumnos | No publicado | Sí | 🔵 B · F-1014 |
| SMS a alumnos en la pandemia · 18.256 alumnos, **Brasil** | Permanencia · nudge | Encuadre de ganancia | Riesgo de deserción −20% a −26% (R); solo si llegaba al celular del alumno | No publicado | Sí | 🟢 A · F-1015 |
| SMS más llamadas de tutoría · Botsuana | Uso · acompañamiento | Práctica con contacto humano | +0,12 DE (R) | 0,89 DE por US$100 | Sí | 🟢 A · F-1016 |
| Nudges y coaching a universitarios 🌐 | Uso · nudge | Planificación | **Sin efecto** académico (R) | No publicado | No | 🟡 C · F-1017 |

### 3.7 Impuestos y servicios públicos

| Intervención y población | Momento · tipo | Mecanismo | Efecto y duración | Costo | ¿Conducta real? | Rigor · fuente |
|---|---|---|---|---|---|---|
| Norma social en el impuesto predial · **Perú** | Pago · prueba social | Cuántos vecinos pagan | Efectos mezclados; el recordatorio simple funcionó (R, sin cifra) | No publicado | Sí, mezclado | 🟡 C · F-1018 |
| Carta disuasiva contra carta de equidad · **Argentina** | Pago · nudge | Sanción contra reciprocidad | Disuasiva +4 puntos; equidad **sin efecto** (R) | No publicado | Sí | 🟢 A · F-1019 |
| Mismo mensaje por visita, carta o correo · **Colombia** | Cobranza · canal | Contacto personal | La visita supera a la carta y al correo (R, sin cifra) | No publicado | Sí | 🟢 A · F-1020 |
| Medidor eléctrico prepago · Sudáfrica | Pago · modelo de pago | Precio visible, sin deuda | Consumo −13% a −14%; mejor recaudo con los más pobres (R) | No publicado | Sí | 🟢 A · F-1021 |
| Factura con comparación social · EE.UU. 🌐 📚 | Uso · prueba social | Comparación con vecinos | Consumo −2%; decae entre cartas y vuelve con cada una (R) | Bajo | Sí | 🟢 A · F-1022 |
| Comparación con el barrio en agua · **Costa Rica** | Uso · prueba social | Comparación cercana | −4,9% en dos meses; la comparación con toda la ciudad no fue significativa (R) | No publicado | Sí, corto plazo | 🟢 A · F-1024 |
| SMS a responsables de mantenimiento escolar · **Perú** | Cumplimiento · nudge | Recordar | Incumplimiento −15% (R); escalado nacional | No publicado | Sí | 🔵 B · F-1025 |

---

## 4. Conducta real contra métrica superficial

**Cambiaron conducta medida** (pago, uso, permanencia, manejo, aprendizaje): la telemetría (F-442), el cobro en la
cosecha (F-988), los recordatorios de ahorro y pago (F-994, F-997), el compromiso de ahorro (F-995), la tarjeta de
débito (F-1001), la adherencia (F-1007), los promotores de salud (F-1008), los SMS a padres (F-1013) y el prepago
(F-1021).

**Movieron una métrica de alcance, no de conducta:**
- afiliación automática sin uso medido (SIS, F-1012; microseguro móvil, F-1027);
- usuarios diarios sin retención medida (Alan, F-859);
- millones de pólizas embebidas sin renovación publicada (F-965, F-985, F-954);
- cuentas abiertas que no se usan (F-1002);
- satisfacción sin permanencia (F-947, F-890).

**Engañan si no se separa la selección:** los programas de bienestar (F-854) y de lealtad (F-805) parecen funcionar
porque se inscribe quien ya se iba a portar bien. Pocos usan los servicios de prevención de su aseguradora aunque digan
quererlos: entre 2,1% y 4,3% según el país (Bain, 2023, F-4).


---

## 5. Qué funcionó, qué no y por qué

**Funcionó cuando:**
- **se cambió el momento o la forma de cobrar**, no el mensaje (F-988, F-1021, F-986);
- **el producto devolvió información útil y verificable** al cliente (F-442, F-1001);
- **el mensajero era una persona conocida** o el contacto era personal (F-999, F-1020, F-1008);
- **el servicio era confiable** antes de empujar la demanda (F-1009: el incentivo funcionó sobre campamentos que sí
  abrían);
- **la recompensa estaba en la propia conducta** que se buscaba (F-807 sostuvo el efecto; el cupón no).

**No funcionó o salió mal cuando:**
- **se regaló el acceso sin acompañar el uso** (F-989, F-991, F-1002);
- **se forzó lo complejo al autoservicio** (siniestro 100% digital, F-183);
- **se confió en el mensaje sin servicio detrás** (bienestar laboral, F-854; reactivación por SMS, F-1026);
- **se dio flexibilidad sin control** (gracia en microcrédito, F-998);
- **se construyó infraestructura sin un beneficio inmediato para el cliente** (seguro abierto en Brasil, F-983; Bima
  Sugam, F-975).

**Fracasos documentados:** Betterfly salió de Perú y de otros cuatro países (F-964, F-372); la venta de vida 100% en
línea cayó 33,6% en una década en Corea (F-185); el seguro abierto de Brasil no consigue consentimientos (F-983); los
seguros de salud subsidiados en Nicaragua e Indonesia no retuvieron (F-989, F-1011).

---

## 6. Transferibilidad a Perú y vacíos

**Más transferible** (América Latina, bajos ingresos, mismo problema): recordatorios de ahorro con un brazo en Perú
(F-994); grupos de ahorro en Chile (F-996); tarjeta de débito en México (F-1001); SMS a padres en Chile (F-1013);
MineduLAB y mantenimiento escolar en Perú (F-1014, F-1025); impuestos en Perú, Argentina y Colombia (F-1018 a F-1020).

**Transferible con cuidado** (otro continente, mismo mecanismo): cobro en la cosecha (F-988), recompra por pagos
visibles (F-990), mensajero conocido (F-999), prepago (F-1021).

**Contraste** (EE.UU. y Europa): telemetría (F-442), retención automática (F-962), bienestar laboral (F-854),
comparación social en energía (F-1022). Sirven para el mecanismo, no para el tamaño del efecto.

**Vacíos que siguen abiertos:**
- **Onboarding en seguros:** ningún experimento publicado.
- **Recordatorios de pago de prima en América Latina:** ningún experimento; el de Ghana aún no publica resultados
  (F-887).
- **Yape, Plin y Pix:** sin evaluación independiente sobre usuarios de bajos ingresos.
- **WhatsApp, telecomunicaciones prepago y USSD:** nada utilizable con método.
- **Costos:** casi nunca se publican.
- **Lectura:** casi todas las cifras de las secciones 3.2 a 3.7 vienen de resúmenes de búsqueda. Para citarlas en un
  documento final conviene abrir el texto (dominios hoy bloqueados en la red de la sesión).

## Anexo B · Escala de evidencia

🟢 A revisión por pares · 🔵 B regulador u oficial · 🟡 C consultora, empresa o working paper · 🟠 D prensa o blog ·
🔴 E opinión o eco de cita.

## Anexo C · Referencias con enlace

Cada fuente citada en el informe, con su número del registro de fuentes del proyecto. Los enlaces llevan a la fuente original o, si no estuvo accesible, al resumen o la cobertura desde donde se leyó. Los documentos internos se indican como tales.

- **F-4** · Bain & Company (2023). *Customer Behavior and Loyalty in Insurance (Global Edition)*. 🟡 C. [Ver fuente](https://www.bain.com/insights/customer-behavior-and-loyalty-in-insurance-global-edition-2023/)
- **F-22** · RGA / Society of Actuaries (2024-25). *Behavioral Science and Insurance: The value of improved comprehension*. 🟡 C. [Ver fuente](https://www.rgare.com/knowledge-center/article/behavioral-science-and-life-insurance--the-value-of-improved-comprehension-in-the-customer-journey)
- **F-183** · Bain & Company, con datos de NPS Prism (2023). *Insurers Have a Digital Dilemma: Complex Claims*. 🟡 C. [Ver fuente](https://www.bain.com/insights/insurers-have-digital-dilemma-complex-claims-snap-chart/)
- **F-185** · The Korea Times (2025). *Life insurers still favor face-to-face sales in digital era*. 🟠 D. [Ver fuente](https://www.koreatimes.co.kr/business/banking-finance/20250206/life-insurers-still-favor-face-to-face-sales-in-digital-era)
- **F-372** · AméricaEconomía, BioBioChile, El Dínamo, Emol (cobertura convergente) (2025). *Betterfly (Chile) despide personal y cierra operaciones en cinco países*. 🟡 C. [Ver fuente](https://www.americaeconomia.com/en/node/290934 · https://www.biobiochile.cl/noticias/economia/negocios-y-empresas/2025/03/14/la-empresa-chilena-betterfly-aplica-despidos-y-determina-cerrar-sus-operaciones-en-cinco-paises.shtml)
- **F-442** · Equipo de investigación en seguridad vial (autoría no capturada en detalle) (2026). *A national randomized field experiment testing the impact of simulated usage-based insurance programs on driver safety (*Accident Analysis & Prevention*)*. 🟢 A. [Ver fuente](https://www.sciencedirect.com/journal/accident-analysis-and-prevention · https://clinicaltrials.gov/study/NCT06101251)
- **F-786** · SBS — Resolución SBS N.° 02260-2026 (vía El Peruano, LP Derecho, Infomercado) (2026). *Reglamento de Seguros Paramétricos*. 🔵 B. [Ver fuente](https://elperuano.pe/noticia/304594-sbs-aprueba-reglamento-de-seguros-parametricos-para-su-funcionamiento-en-el-mercado-peruano · https://lpderecho.pe/reglamento-de-seguros-parametricos-resolucion-sbs-02260-2026/)
- **F-805** · Leenheer, J.; van Heerde, H.; Bijmolt, T.; Smidts, A. (2007). *Do loyalty programs really enhance behavioral loyalty? An empirical analysis accounting for self-selecting members (Int. J. Res. Mark. 24(1):31-47)*. 🟢 A. [Ver fuente](https://repository.tilburguniversity.edu/items/3fc12a59-7823-4842-9792-de0262adaea7)
- **F-807** · Ho, Y.-J.; Liu, S.; Wang, L. (2023). *Fun Shopping: A Randomized Field Experiment on Gamification (Inf. Syst. Res. 34(2):766-785; DOI 10.1287/isre.2022.1147)*. 🟢 A. [Ver fuente](https://pubsonline.informs.org/doi/fpi/10.1287/isre.2022.1147)
- **F-808** · Bies, S. M. T. A.; Bronnenberg, B. J. & Gijsbrechts, E. (International Journal of Research in Marketing 38(4):877-899; DOI 10.1016/j.ijresmar.2021.02.001) (2021). *How push messaging impacts consumer spending and reward redemption in store-loyalty programs*. 🟢 A. [Ver fuente](https://doi.org/10.1016/j.ijresmar.2021.02.001)
- **F-847** · Campbell, D. & Frei, F. (Management Science 56(1):4-24) (2010). *Cost Structure, Customer Profitability, and Retention Implications of Self-Service Distribution Channels*. 🟢 A. [Ver fuente](https://pubsonline.informs.org/doi/10.1287/mnsc.1090.1132)
- **F-850** · Kumar, A. & Telang, R. (Information Systems Research 23(3-1):721-737) (2012). *Does the Web Reduce Customer Service Cost? Empirical Evidence from a Call Center*. 🟢 A. [Ver fuente](https://doi.org/10.1287/isre.1110.0390)
- **F-851** · Turley, M. et al. (American Journal of Managed Care) (2012). *Patient portal use and health plan membership retention (Kaiser Permanente Northwest, My Health Manager)*. 🟢 A. [Ver fuente](https://pmc.ncbi.nlm.nih.gov/articles/PMC4215918)
- **F-854** · Jones, D.; Molitor, D.; Reif, J. (Quarterly Journal of Economics 134(4):1747-1791) (2019). *What Do Workplace Wellness Programs Do? Evidence from the Illinois Workplace Wellness Study*. 🟢 A. [Ver fuente](https://econpapers.repec.org/RePEc:oup:qjecon:v:134:y:2019:i:4:p:1747-1791.)
- **F-855** · Song, Z. & Baicker, K. (JAMA) (2019). *Effect of a Workplace Wellness Program on Employee Health and Economic Outcomes: A Randomized Clinical Trial*. 🟢 A. [Ver fuente](https://hcp.hms.harvard.edu/publication/effect-workplace-wellness-program-employee-health-and-economic-outcomes-randomized)
- **F-858** · Oscar Health, Inc. (Form 10-K FY2025; llamadas de resultados 1T25 y 1T26) (2026). *Form 10-K FY2025; earnings calls*. 🟡 C. [Ver fuente](https://www.sec.gov/Archives/edgar/data/1568651/000156865126000011/oscr-20251231.htm)
- **F-859** · Alan (carta a accionistas Q2 2025) (2025). *Alan - 2025 Q2 Letter to Shareholders*. 🟠 D. [Ver fuente](https://alan.com/en/blog/discover-alan/a/alan-2025-q2-letter-to-shareholders)
- **F-863** · Nubank y Chubb (comunicados y prensa especializada) (2024). *Nubank and Chubb reach 2 million active insurance policies in Brazil*. 🟠 D. [Ver fuente](https://coverager.com/nubank-and-chubb-reach-2-million-active-insurance-policies-in-brazil/)
- **F-865** · Porto Seguro (presentación a inversionistas vía Quartr; release 1T25; CQCS) (2025). *Porto Seguro investor presentation; Release 1T25; entrevista a Patrícia Chacon (COO)*. 🟡 C. [Ver fuente](https://cqcs.com.br/noticia/patricia-chacon-coo-da-porto-seguro-revela-como-a-seguradora-esta-se-preparando-para-o-futuro/)
- **F-870** · Bloomberg Línea (Justos, Brasil) (2025). *Ribbit e Kaszek reforçam aposta na insurtech Justos com aporte de R$ 92 milhões*. 🟠 D. [Ver fuente](https://www.bloomberglinea.com.br/startups/ribbit-e-kaszek-reforcam-aposta-na-insurtech-justos-que-capta-r-92-milhoes/)
- **F-886** · Financial Conduct Authority (Reino Unido) (2025). *Evaluation Paper 25/2: Our general insurance pricing practices (GIPP) remedies*. 🔵 B. [Ver fuente](https://www.fca.org.uk/publications/corporate-documents/evaluation-paper-25-2-general-insurance-pricing-practices-remedies)
- **F-887** · Autores del protocolo ReachUHC (Trials, BMC; medRxiv) (2025). *ReachUHC: a randomized controlled trial of a mobile phone-based reminder and automatic renewal intervention to increase health insurance renewal rates in Kumasi, Ghana*. 🔵 B. [Ver fuente](https://link.springer.com/article/10.1186/s13063-025-09360-1)
- **F-890** · LexisNexis Risk Solutions (2023). *Moment of Truth: claims satisfaction and auto insurance switching (whitepaper)*. 🟡 C. [Ver fuente](https://www.claimsjournal.com/news/national/2023/06/08/317385.htm)
- **F-896** · Poulton, D. & Magnoni, B. (MicroInsurance Centre, proyecto MILK) (2013). *MILK Brief #16: 'Doing the Math' – Life Microinsurance in Mexico (Compartamos Banco)*. 🟡 C. [Ver fuente](https://microinsurancecentre.milliman.com/en/insight/milk-brief-16-doing-the-math-life-microinsurance-in-mexico)
- **F-903** · SBS y CAF (citada vía el diagnóstico del PNUD, F-902) (2022). *Encuesta de Capacidades Financieras del Perú 2022 (resultados sobre seguros)*. 🔵 B. Cita secundaria en F-902; documento original no consultado.
- **F-904** · Coloma C., F. (Instituto de Economía, Pontificia Universidad Católica de Chile; ex Superintendente de Valores y Seguros) (2019). *Licitación de los seguros asociados a los créditos hipotecarios: algunos resultados y propuestas de mejoramiento (Documento de Política Pública)*. 🔵 B. PDF aportado por la usuaria (Documento de Política Pública, Instituto de Economía UC); URL pública no verificada.
- **F-939** · Cortez Carpio, J. (líder de innovación y diseño, laboratorio de innovación La Cápsula de Pacífico Salud), publicación en LinkedIn; captura aportada por la usuaria (2026 (27 de agosto; año confirmado por la usuaria)). *¿Y si el mejor canal para una experiencia de salud no siempre es una app o una web? (orientación médica por WhatsApp en Tsana)*. 🔴 E. Captura de LinkedIn aportada por la usuaria (enlace acortado lnkd.in/d9WJzB8g).
- **F-947** · J.D. Power (vía Insurance-Canada y FenderBender) (2017). *2017 U.S. Auto Claims Satisfaction Study*. 🟡 C. [Ver fuente](https://insurance-canada.ca/2017/10/26/jd-power-auto-claims-satisfaction/)
- **F-954** · Let's Money y Latam Fintech (prensa especializada), con datos de Mercado Pago (2026). *Mercado Pago expande su oferta de seguros con IA y llega a 11 millones de clientes en Brasil (julio 2026)*. 🟠 D. [Ver fuente](https://www.letsmoney.com.br/noticias/mercado-pago-11-mi-clientes-seguros/)
- **F-958** · Society of Actuaries (EE.UU.), boletín NewsDirect (2014). *Enrolling Voluntary Benefits Is Risky Business*. 🟡 C. [Ver fuente](https://www.soa.org/news-and-publications/newsletters/newsdirect/2014/september/ndn-2014-iss69-760oop/enrolling-voluntary-benefits-is-risky-business)
- **F-960** · Insurance Journal (sobre Cambridge Mobile Telematics, Claims Studio) (2020). *Accident Reports Now Ready Minutes After Crash on Smartphone, Says Telematics Firm*. 🟠 D. [Ver fuente](https://www.insurancejournal.com/news/national/2020/01/10/554252.htm)
- **F-962** · McIntyre, A. L.; Shepard, M. & Wagner, M. (NBER Working Paper 28630; preparado para AER Papers & Proceedings) (2021). *Can Automatic Retention Improve Health Insurance Market Outcomes?*. 🟡 C. [Ver fuente](https://www.nber.org/papers/w28630)
- **F-964** · Gestión (con declaraciones de Betterfly al Diario Financiero) (2025). *Chilena Betterfly cierra operación en Perú y cuatro países más: ¿cuál es la razón? (18 de marzo de 2025)*. 🟠 D. Nota aportada por la usuaria (recopilación de Gestión).
- **F-965** · Gestión (cobertura del Insurance Day 2025 de Apeseg) (2025). *Insurance Day 2025: historias reales que están transformando el sector asegurador (26 de mayo de 2025)*. 🟠 D. Nota aportada por la usuaria (recopilación de Gestión).
- **F-966** · Gestión (entrevista a Mónica Rivas, gerente de Bancaseguros y Ecosistemas Credicorp de Pacífico Seguros) (2024). *Pacífico Seguros: "Queremos llegar a millones de personas más con los seguros inclusivos" (19 de mayo de 2024)*. 🟠 D. Nota aportada por la usuaria (recopilación de Gestión).
- **F-967** · Gestión (con declaraciones de María José Alfaro, gerente de embebidos e innovación de Pacífico Seguros) (2026). *Lanzan seguros desde S/3 para protección en viajes, ¿qué peligros cubren? (22 de abril de 2026)*. 🟠 D. Nota aportada por la usuaria (recopilación de Gestión).
- **F-973** · Gestión (sobre Interbank, Mibanco, Caja Arequipa y Banco de la Nación) (2025-2026). *Plin WhatsApp: la apuesta de Interbank para pagar sin salir del chat (31 de octubre de 2025); Bancos y cajas empiezan a dar créditos y permitir pagos por WhatsApp (10 de febrero de 2026)*. 🟠 D. Nota aportada por la usuaria (recopilación de Gestión).
- **F-975** · Prensa india y aseguradoras (Business Today, Reinsurance Asia, Tata AIA) (2025-2026). *Bima Sugam: mercado digital único de seguros del regulador indio IRDAI*. 🟠 D. [Ver fuente](https://www.businesstoday.in/personal-finance/insurance/story/irdai-announces-bima-sugam-portal-launch-first-phase-expected-in-december-494470-2025-09-17)
- **F-977** · Takahashi, K.; Ikegami, M.; Sheahan, M. & Barrett, C. B. (World Development 78:324-340) (2016). *Experimental evidence on the drivers of index-based livestock insurance demand in Southern Ethiopia*. 🟢 A. [Ver fuente](https://repo.mel.cgiar.org/handle/20.500.11766/4688)
- **F-979** · ILRI y Gobierno de Kenia (nota de 2019); Swiss Re (informe 2017); Artemis (2017-2019). *Kenya Livestock Insurance Program (KLIP)*. 🔵 B. [Ver fuente](https://www.ilri.org/news/kenya-government-declares-pay-out-ksh87-million-cushion-6000-pastoralists-effects-drought)
- **F-980** · ACRE Africa / Kilimo Salama (brief de IFC y Syngenta; 3ie; prensa) (2012-2016). *Seguro agrícola por índice climático con pago por M-Pesa*. 🟡 C. [Ver fuente](https://www.3ieimpact.org/evidence-hub/publications/other-evaluations/formative-evaluation-increasing-uptake-acre-hakika)
- **F-981** · Turaco (sitio propio) y prensa tecnológica africana (Disrupt Africa, NextBillion, Insurtech Insights) (2020-2026). *Turaco: microseguro embebido de salud y vida en Kenia, Uganda, Nigeria y otros países*. 🟠 D. [Ver fuente](https://www.insurtechinsights.com/kenyan-insurtech-turaco-passes-one-million-customers-insured-milestone/)
- **F-983** · Susep (Brasil), vía LetsMoney (republica Valor Econômico) y The Paypers (2024-2026). *Open Insurance en Brasil: transacciones, consentimientos y estado del sistema*. 🟠 D. [Ver fuente](https://www.letsmoney.com.br/noticias/open-insurance-menos-10-mil-consentimentos/)
- **F-984** · de Janvry, A.; Ramírez Ritchie, E. & Sadoulet, E. (World Bank Policy Research Working Paper 7715) (2016). *Weather Index Insurance and Shock Coping: Evidence from Mexico's CADENA Program*. 🟡 C. [Ver fuente](https://openknowledge.worldbank.org/handle/10986/24632)
- **F-985** · Prensa regional (Corresponsables, Bloomberg Línea, Expansión, Pulzo) (2023-2026). *Seguros dentro de billeteras y "sponsors" en LatAm: Klimber con MetLife, Mercado Pago México, Nequi Colombia*. 🟠 D. [Ver fuente](https://www.corresponsables.com/arg/actualidad/klimber-expande-su-operacion-a-uruguay-y-colombia-y-celebra-15-millones-de-asegurados-en-america-latina)
- **F-986** · Microinsurance Network (artículo de su sección de publicaciones; autoría individual no indicada) (s.f. (página vista el 2026-10-29; © 2026)). *Open insurance for inclusion: what will it really take?*. 🟡 C. [Ver fuente](https://microinsurancenetwork.org/posts/open-insurance-for-inclusion-what-will-it-really-take)
- **F-988** · Casaburi, L. & Willis, J. (American Economic Review 108(12):3778-3813) (2018). *Time versus State in Insurance: Experimental Evidence from Contract Farming in Kenya*. 🟢 A. [Ver fuente](https://econpapers.repec.org/RePEc:aea:aecrev:v:108:y:2018:i:12:p:3778-3813)
- **F-989** · Thornton, R. L.; Hatt, L. E.; Field, E. M.; Islam, M.; Solís Diaz, F. & González, M. A. (Health Economics 19(S1):181-206) (2010). *Social security health insurance for the informal sector in Nicaragua: a randomized evaluation*. 🟢 A. [Ver fuente](https://econpapers.repec.org/RePEc:wly:hlthec:v:19:y:2010:i:s1:p:181-206)
- **F-990** · Cole, S.; Stein, D. & Tobacman, J. (American Economic Review: Papers & Proceedings 104(5):284-290) (2014). *Dynamics of Demand for Index Insurance: Evidence from a Long-Run Field Experiment*. 🟢 A. [Ver fuente](https://econpapers.repec.org/RePEc:aea:aecrev:v:104:y:2014:i:5:p:284-90)
- **F-991** · Haushofer, J.; Chemin, M.; Jang, C. & Abraham, J. (Journal of Development Economics) (2020). *Economic and psychological effects of health insurance and cash transfers: Evidence from a randomized experiment in Kenya*. 🟢 A. [Ver fuente](https://jrpabraham.github.io/assets/Haushofer_JDE_2020.pdf)
- **F-993** · Cai, J.; de Janvry, A. & Sadoulet, E. (American Economic Journal: Applied Economics) (2015). *Social Networks and the Decision to Insure*. 🟢 A. [Ver fuente](https://www.povertyactionlab.org/evaluation/social-networks-and-decision-insure-china?lang=es)
- **F-994** · Karlan, D.; McConnell, M.; Mullainathan, S. & Zinman, J. (Management Science 62(12)) (2016). *Getting to the Top of Mind: How Reminders Increase Saving*. 🟢 A. [Ver fuente](https://causalclaims.trfetzer.com/paper/w16205.html)
- **F-995** · Ashraf, N.; Karlan, D. & Yin, W. (Quarterly Journal of Economics 121(2)) (2006). *Tying Odysseus to the Mast: Evidence from a Commitment Savings Product in the Philippines*. 🟢 A. [Ver fuente](https://microfinancegateway.org/paper/2005/09/tying-odysseus-mast-evidence-commitment-savings-product-philippines)
- **F-996** · Kast, F.; Meier, S. & Pomeranz, D. (Journal of Development Economics 133:275-294) (2018). *Saving more in groups: Field experimental evidence from Chile*. 🟢 A. [Ver fuente](https://econpapers.repec.org/RePEc:eee:deveco:v:133:y:2018:i:c:p:275-294)
- **F-997** · Cadena, X. & Schoar, A. (NBER Working Paper 17020) (2011). *Remembering to Pay? Reminders vs. Financial Incentives for Loan Payments*. 🟡 C. [Ver fuente](https://www.nber.org/papers/w17020)
- **F-998** · Field, E.; Pande, R.; Papp, J. & Rigol, N. (American Economic Review 103(6):2196-2226) (2013). *Does the Classic Microfinance Model Discourage Entrepreneurship Among the Poor?*. 🟢 A. [Ver fuente](https://econpapers.repec.org/RePEc:aea:aecrev:v:103:y:2013:i:6:p:2196-2226)
- **F-999** · Karlan, D.; Morten, M. & Zinman, J. (registro AEA RCT; publicación no verificada) (s.f.). *A Personal Touch in Text Messaging: microcrédito en Filipinas*. 🟡 C. [Ver fuente](https://www.socialscienceregistry.org/trials/1853)
- **F-1000** · Suri, T. & Jack, W. (Science 354) (2016). *The long-run poverty and gender impacts of mobile money*. 🟢 A. [Ver fuente](https://sciencedaily.com/releases/2016/12/161208151920.htm)
- **F-1001** · Bachas, P.; Gertler, P.; Higgins, S. & Seira, E. (Journal of Finance 76(4):1913-1957) (2021). *How Debit Cards Enable the Poor to Save More*. 🟢 A. [Ver fuente](https://econpapers.repec.org/RePEc:bla:jfinan:v:76:y:2021:i:4:p:1913-1957)
- **F-1002** · Dupas, P.; Karlan, D.; Robinson, J. & Ubfal, D. (NBER Working Paper 22463) (2016). *Banking the Unbanked? Evidence from Three Countries*. 🟡 C. [Ver fuente](https://nber.org/system/files/working_papers/w22463/w22463.pdf)
- **F-1003** · Breza, E.; Kanz, M. & Klapper, L. (NBER Working Paper 28249) (2020). *Learning to Navigate a New Financial Technology: Evidence from Payroll Accounts*. 🟡 C. [Ver fuente](https://econpapers.repec.org/RePEc:nbr:nberwo:28249)
- **F-1004** · Sarkisyan, S. (working paper de conferencia); tesis de Princeton (2026) y de la Universidade de São Paulo (2025); policy brief sobre adopción (2023-2026). *Evidencia sobre Pix, el pago instantáneo público de Brasil*. 🟠 D. [Ver fuente](https://afajof.org/management/viewp.php?n=23408)
- **F-1005** · Higgins, S. (American Economic Review 114(11):3469-3512) (2024). *Financial Technology Adoption: Network Externalities of Cashless Payments in Mexico*. 🟢 A. [Ver fuente](https://econpapers.repec.org/RePEc:aea:aecrev:v:114:y:2024:i:11:p:3469-3512)
- **F-1006** · BCP (vía RPP) e Ipsos para Credicorp (vía La Cámara) (2022-2024). *Yape con DNI y uso de billeteras en Perú*. 🟡 C. [Ver fuente](https://rpp.pe/campanas/valor-compartido/yape-con-dni-es-reconocido-por-permitir-que-mas-de-1-millon-de-peruanos-accedan-al-sistema-financiero-por-primera-vez-noticia-1376668)
- **F-1007** · Pop-Eleches, C.; Thirumurthy, H.; et al. (AIDS 25(6)) (2011). *Mobile phone technologies improve adherence to antiretroviral treatment in a resource-limited setting*. 🟢 A. [Ver fuente](https://pmc.ncbi.nlm.nih.gov/articles/PMC3718389)
- **F-1008** · Björkman Nyqvist, M.; Guariso, A.; Svensson, J. & Yanagizawa-Drott, D. (AEJ: Applied Economics 11(3)) (2019). *Reducing Child Mortality in the Last Mile: Experimental Evidence on Community Health Promoters in Uganda*. 🟢 A. [Ver fuente](https://es.poverty-action.org/sites/default/files/2023-04/Reducing%20Child%20Mortality%20in%20the%20Last%20Mile%20Experimental%20Evidence%20on%20Community%20Health%20Promoters%20in%20Uganda%20-%20AEJ.pdf)
- **F-1009** · Banerjee, A. V.; Duflo, E.; Glennerster, R. & Kothari, D. (BMJ 340) (2010). *Improving immunisation coverage in rural India: clustered randomised controlled evaluation of immunisation campaigns with and without incentives*. 🟢 A. [Ver fuente](https://www.povertyactionlab.org/evaluation/improving-immunization-rates-through-regular-camps-and-incentives-india)
- **F-1010** · Autores no verificados (artículo indexado en TechNet-21) (s.f.). *SMS text message reminders to improve infant vaccination coverage in Guatemala*. 🟢 A. [Ver fuente](https://www.technet-21.org/en/resources/journal-article/sms-text-message-reminders-to-improve-infant-vaccination-coverage-in-guatemala-a-pilot-randomized-controlled-trial)
- **F-1011** · Banerjee, A.; Finkelstein, A.; Hanna, R.; Olken, B. A.; Ornaghi, A. & Sumarto, S. (American Economic Review 111(9):3035-3063) (2021). *The Challenges of Universal Health Insurance in Developing Countries: Experimental Evidence from Indonesia's National Health Insurance*. 🟢 A. [Ver fuente](https://econpapers.repec.org/RePEc:aea:aecrev:v:111:y:2021:i:9:p:3035-63)
- **F-1012** · Agencia Andina (sobre el Seguro Integral de Salud) (2020). *SIS superó los 20 millones de asegurados en 2019 (afiliación automática por el Decreto de Urgencia 017-2019)*. 🟠 D. [Ver fuente](https://andina.pe/agencia/noticia-sis-supero-20-millones-asegurados-el-2019-780682.aspx)
- **F-1013** · Berlinski, S.; Busso, M.; Dinkelman, T. & Martínez, C. (Journal of Human Resources; NBER Working Paper 28581) (2021). *Reducing Parent-School Information Gaps and Improving Education Outcomes: Evidence from High-Frequency Text Messages*. 🟢 A. [Ver fuente](https://www.nber.org/system/files/working_papers/w28581/w28581.pdf)
- **F-1014** · Ministerio de Educación del Perú (MineduLAB), con IPA y J-PAL (2019). *Decidiendo para un futuro mejor (policy brief)*. 🔵 B. [Ver fuente](https://www.minedu.gob.pe/minedulab/pdf/pb-decidiendo-para-un-futuro-mejor-final-2019.pdf)
- **F-1015** · Lichand, G. & Christen, J. (npj Science of Learning) (2024). *Behavioral nudges to prevent student dropouts in the pandemic (Goiás, Brasil)*. 🟢 A. [Ver fuente](https://www.nature.com/articles/s41539-024-00235-9.pdf)
- **F-1016** · Angrist, N.; Bergman, P. & Matsheng, M. (Nature Human Behaviour) (2022). *Experimental evidence on learning using low-tech when school is out*. 🟢 A. [Ver fuente](https://conference.iza.org/conference_files/covid_2021/angrist_n30860.pdf)
- **F-1017** · Oreopoulos, P. & Petronijevic, U. (IZA Discussion Paper 12460) (2019). *The Remarkable Unresponsiveness of College Students to Nudging and What We Can Learn from It*. 🟡 C. [Ver fuente](https://docs.iza.org/dp12460.pdf)
- **F-1018** · Del Carpio, L. (GRADE, documento de investigación 73) (2014). *Are the Neighbors Cheating? Evidence from a Social Norm Experiment on Property Taxes in Peru*. 🟡 C. [Ver fuente](https://www.grade.org.pe/wp-content/uploads/DI73.pdf)
- **F-1019** · Castro, L. & Scartascini, C. (Journal of Economic Behavior & Organization 116:65-82) (2015). *Tax compliance and enforcement in the pampas: Evidence from a field experiment*. 🟢 A. [Ver fuente](https://econpapers.repec.org/RePEc:eee:jeborg:v:116:y:2015:i:c:p:65-82)
- **F-1020** · Ortega, D. & Scartascini, C. (Journal of Economic Behavior & Organization 170:286-300) (2020). *Don't blame the messenger: the delivery method of a message matters*. 🟢 A. [Ver fuente](https://econpapers.repec.org/RePEc:eee:jeborg:v:170:y:2020:i:c:p:286-300)
- **F-1021** · Jack, B. K. & Smith, G. (AEJ: Applied Economics) (2020). *Charging Ahead: Prepaid Metering, Electricity Use, and Utility Revenue*. 🟢 A. [Ver fuente](https://www.aeaweb.org/doi/10.1257/app.20180155)
- **F-1022** · Allcott, H. (Journal of Public Economics, 2011); Allcott, H. & Rogers, T. (American Economic Review, 2014) (2011-2014). *Social Norms and Energy Conservation; The Short-Run and Long-Run Effects of Behavioral Interventions*. 🟢 A. [Ver fuente](https://ceepr.mit.edu/workingpaper/social-norms-and-energy-conservation)
- **F-1024** · Autores no verificados (World Bank Economic Review 34(2):444-463) (2020). *Experimento de comparación social y planificación del consumo de agua en Belén, Costa Rica*. 🟢 A. [Ver fuente](https://econpapers.repec.org/RePEc:oup:wbecrv:v:34:y:2020:i:2:p:444-463)
- **F-1025** · Innovations for Poverty Action (con Pronied y MineduLAB) (s.f.). *Improving School Maintenance with Text Message Alerts in Peru*. 🔵 B. [Ver fuente](https://poverty-action.org/impact/improving-school-maintenance-with-text-message-alerts-peru)
- **F-1026** · CGAP (blog sobre KPOSB, Kenia) (2015). *Understanding Customer Inactivity with Customer Data in Kenya*. 🟡 C. [Ver fuente](https://www.cgap.org/blog/understanding-customer-inactivity-with-customer-data-kenya)
- **F-1027** · Microinsurance Network (artículo sobre microseguro móvil) (s.f.). *From connectivity to coverage via collaboration: revisiting mobile microinsurance*. 🟡 C. [Ver fuente](https://microinsurancenetwork.org/posts/from-connectivity-to-coverage-via-collaboration-revisiting-mobile-microinsurance)
- **F-1028** · Blogs de proveedores de software de seguros (atribuido a LIMRA) (s.f.). *«El onboarding estructurado reduce 20-35% la caducidad del primer año»*. 🔴 E. Sin URL primaria (cifra repetida en blogs de proveedores).
- **F-1031** · Nsiah-Boateng, E. y otros (BMC Health Services Research; DOI 10.1186/s12913-023-09236-7) (2023). *Effect of mobile phone-based health insurance contribution payment system on retention of coverage in the National Health Insurance Scheme in Ghana*. 🟢 A. [Ver fuente](https://link.springer.com/10.1186/s12913-023-09236-7)
- **F-1033** · Adams, P.; Hunt, S.; Palmer, C. & Zaliauskas, R. (Journal of Financial Economics 141(1):122-147) (2021). *Testing the Effectiveness of Consumer Financial Disclosure: Experimental Evidence from Savings Accounts*. 🟢 A. [Ver fuente](https://econpapers.repec.org/RePEc:eee:jfinec:v:141:y:2021:i:1:p:122-147)
- **F-1034** · Luo, X.; Tong, S.; Fang, Z. & Qu, Z. (Marketing Science 38(6):937-947; DOI 10.1287/mksc.2019.1192) (2019). *Frontiers: Machines vs. Humans: The Impact of Artificial Intelligence Chatbot Disclosure on Customer Purchases*. 🟢 A. [Ver fuente](https://econpapers.repec.org/RePEc:inm:ormksc:v:38:y:2019:i:6:p:937-947)
- **F-1035** · Kim, S. J.; Wang, R. J.-H. & Malthouse, E. C. (Journal of Interactive Marketing 31:28-41; DOI 10.1016/j.intmar.2015.05.004) (2015). *The Effects of Adopting and Using a Brand's Mobile Application on Customers' Subsequent Purchase Behavior*. 🟢 A. [Ver fuente](https://ideas.repec.org/a/eee/joinma/v31y2015icp28-41.html)
- **F-1036** · Villar(s), P. (El Comercio), entrevista a Gianfranco Ferrari, CEO de Credicorp (2026 (fecha no visible en el recorte; posterior a la publicación del Índice de Inclusión Financiera 2026, de octubre de 2026)). *«Estoy convencido de que TAPP, del BCR, ayudará a ganarle la batalla al efectivo»*. 🟠 D. Recorte de El Comercio aportado por la usuaria (adjunto 35 en el repositorio privado); sin enlace.
