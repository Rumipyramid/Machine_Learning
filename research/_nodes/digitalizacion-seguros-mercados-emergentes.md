# Digitalización de seguros en mercados emergentes: qué se digitaliza, qué intervenciones mueven la conducta, quién queda fuera y qué se puede transferir a Perú

> Documento de investigación. Fuente persistente y versionada en el repositorio.
> Fecha de elaboración: 2026-10-15 · Última actualización: 2026-10-15 · Versión: **v1.0**
> Origen: `/trinidad` (pista empírica/teórica + social/regulatoria + negocio), con el rol de *behavioral designer y researcher senior*, a pedido del usuario (aseguradora en Perú).
> Fuentes en `research/fuentes/codice.md`: **F-847 a F-902** (empírica F-847 a F-877 · social y regulación F-878 a F-884 · negocio F-885 a F-902). Reutiliza fuentes ya registradas: F-1, F-5, F-8, F-229, F-251, F-338, F-374, F-377, F-486, F-786, F-788, F-790, F-798, F-799, F-800.
> Pregunta permanente: **¿qué hace una aseguradora al digitalizarse que cambie de verdad lo que hace la gente (contratar, pagar, renovar, reclamar), para quién funciona, y qué de eso sirve en Perú?**
> Decisión que alimenta: diseño conductual y de producto de una aseguradora en Perú, con foco en lo accionable en Latinoamérica.

---

## 0. 🎯 Alcance, supuestos y cómo se leyó la evidencia

- **Ventana:** 2021-2026, salvo trabajos fundacionales. Los experimentos clave sobre seguro de lluvia son de 2008-2018 y van marcados **"fuera de ventana, canónico"**. Los hallazgos de 2021 en adelante son pocos y vienen sobre todo de reportes de industria.
- **Mercados comparables:** África subsahariana (Kenia, Ghana, Tanzania, Zimbabue), India, Sudeste Asiático (Filipinas, Indonesia), Centroamérica y Brasil, con Perú como destino.
- ⚠️ **Límite de lectura (importante).** En esta sesión no se pudo abrir ningún artículo ni página: las herramientas de descarga no tienen salida a internet (el proxy del entorno rechaza los dominios). Todo se leyó por **resúmenes y fragmentos de búsqueda**. Por eso hay cifras sin muestra ni intervalo, autores que no pude capturar y varios resultados que hay que confirmar antes de citarlos fuera de este repo. Cada ficha del ledger lo indica.
- ⚠️ **La búsqueda social no llegó a Reddit ni a X.** Devolvió prensa, foros antiguos y reguladores. La pista social mide menos de lo que el encargo pedía (ver §11).
- ⚠️ **"La hipótesis de edad" no estaba definida en el encargo.** Evalué esta formulación: *"la edad es la barrera principal de la digitalización de seguros: los mayores quedan fuera y los jóvenes adoptan"*. Si la hipótesis era otra, el §2 hay que rehacerlo.
- **Niveles de evidencia usados:** experimento aleatorizado (RCT) · cuasi-experimento · observacional · caso de negocio · reporte de industria · opinión. Cada vez que importa, se dice si la cifra la reporta la propia empresa o un tercero.
- **Sesgo de supervivencia:** casi todo lo publicado por empresas (GCash, Nubank, MicroEnsure, Pula, Azos) son casos que siguen vivos o que quieren mostrarse. Los fracasos aparecen poco: MicroEnsure dejó de operar sola, el programa gratuito de Econet se cerró por razones legales, Betterfly cerró en cinco países (ver [[venta-vida-digital-hibrida-latam]]).

---

## 1. ⚖️ Resumen ejecutivo

1. **Lo que más mueve la contratación no es el canal: es cuándo se paga, quién lo recomienda y si se ven pagos de siniestros.** Con la prima descontada en la cosecha, contrató 72% frente a 5% con prima adelantada (RCT en Kenia, F-847). La información que viaja por la red y por líderes de grupo sube la contratación (F-848, F-850). Los pagos recibidos, propios o ajenos, suben la demanda siguiente (F-849).
2. **La digitalización escaló el alcance, no la medición del uso.** Las cifras publicadas cuentan pólizas o personas cubiertas (GCash: 51,4 millones de pólizas; Nubank: 2 millones; MicroEnsure: más de 1 millón en Ghana y Tanzania). Ningún caso publica a la vez alcance, siniestros pagados y renovación. El único dato que enfrenta afiliación con vigencia (India, seguro de vida masivo) muestra que solo cerca de la mitad sigue activa (F-891, con reservas).
3. **Hipótesis de edad: matizada.** La brecha de uso de internet por edad es real en Perú (51,2% en mayores de 60 frente a 94-96% entre 19 y 40 años, F-869), pero la edad se confunde con acceso, alfabetización y confianza, y los estudios de contratación de seguro no muestran un efecto de edad consistente (F-864 frente a F-865). Detalle en §2.
4. **Cuando la venta digital escala, la fricción se mueve a la conducta de venta.** En India, las quejas por venta engañosa subieron 11,2% interanual (F-882) y el regulador multó a Policybazaar (F-884). En Perú, Indecopi sancionó a Pacífico por 1.395 llamadas sin consentimiento (F-878) y circulan estafas con SOAT falso (F-880).
5. **Lo accionable para Perú, en orden de impacto × facilidad:** (a) acompañamiento humano sobre el canal digital, (b) cobro atado al flujo de ingresos del cliente, (c) renovación asistida con experimentos en la base propia y (d) medir vigencia y uso real. Después, terceros confiables como canal. En vez de segmentar por edad, segmentar por necesidad de acompañamiento. Mapa en §10.
6. **Advertencia de alcance:** casi toda la evidencia aleatorizada es de seguro agrícola de índice y de diseño del contrato. No encontré ningún experimento publicado sobre canales digitales de seguros (WhatsApp, app, USSD) en un mercado emergente. La transferencia a vida, salud o auto es una hipótesis, no un hecho.

---

## 2. 🧓 Veredicto sobre la hipótesis de edad: **matizada**

**Formulación evaluada:** la edad es la barrera principal de la digitalización de seguros; los mayores quedan fuera y los jóvenes adoptan.

**Veredicto:** no se sostiene como causa principal y sí como señal. La edad funciona como marcador de tres cosas que sí tienen respaldo: acceso y uso del dispositivo, alfabetización digital y necesidad de ayuda. No encontré ningún estudio que pruebe la edad como moderadora de la adopción digital de seguros en un mercado emergente.

### 2.1 Lo que la respalda

| Evidencia | Qué dice | Tipo · quién reporta | Fuente |
|---|---|---|---|
| Uso de internet por edad, Perú, 3T 2025 | 60 años a más: 51,2% (47% un año antes). 19-24 años: 95,8%. 25-40: 94,2% | Encuesta oficial leída vía prensa | F-869 |
| Banca en línea por edad, Alemania | 78% a los 65-74 años, 35% desde los 75. Entre 16 y 64 años, 90-95% | Reporte de industria; banca, no seguros | F-876 |
| Análisis peruano | Banca, salud y servicios públicos pasan a plataformas que la mayoría de los mayores no domina | Opinión periodística | F-874 |
| Encuesta de un proveedor (EE.UU.) | 64% de los nacidos desde 1975 cree que el seguro debe comprarse en línea | Encuesta encargada por una insurtech; no es mercado emergente | F-875 |
| Dark patterns | Posible mayor vulnerabilidad de usuarios mayores; evidencia débil | Paper peer-reviewed | F-251 |

### 2.2 Lo que la contradice o la acota

| Evidencia | Qué dice | Tipo · quién reporta | Fuente |
|---|---|---|---|
| Brecha por país | En Mongolia ~90% de los mayores de 60 paga digitalmente a comercios; en Filipinas e Indonesia, cerca de cero | Encuesta del Banco Mundial (Findex 2025) vía blog | F-867 |
| Contratación de seguro de índice, edad | Etiopía (Borena): los hogares mayores compran menos. Kenia (Embu): los asegurados son mayores que los no asegurados | Observacionales; fragmentos | F-864, F-865 |
| Determinantes que sí se repiten | Confianza, liquidez, momento del pago, riesgo de base, redes y conocimiento del vendedor | RCT y observacionales | F-799, F-847, F-848, F-853 |
| Las intervenciones más eficaces no se diseñaron por edad | Pago en la cosecha, difusión por red, líderes de grupo | RCT | F-847, F-848, F-850 |
| Demografía en general | La segmentación demográfica (edad, ingreso, ocupación) explica poco de la conducta financiera | Paper peer-reviewed (2011) | F-229 |
| Los jóvenes también enfrentan barreras, de comprensión | Solo 1 de cada 4 jóvenes de 18-27 años (EE.UU.) puede definir deducible y copago | Encuesta de reguladores | F-8 |
| Lo que "ya tienen" los mayores peruanos | 94,4% de los mayores de 60 tiene algún seguro de salud; la lectura no distingue público de privado | Encuesta oficial vía prensa | F-870 |
| Moderación por edad en insurtech (Indonesia) | La edad modera algunas relaciones, sin dirección ni magnitud visibles | Fragmento; revista no verificada | F-866 |

### 2.3 Cómo leerlo para la decisión

- **La mitad de los mayores peruanos ya usa internet** y 98,6% de quienes usan mensajería usa WhatsApp (F-871, no desglosado por edad). La barrera no parece ser "los mayores no están en línea", sino quién los ayuda a decidir y a pagar. Esto es una inferencia mía; **no hay datos peruanos de seguros por edad** en lo que leí.
- **Segmentar por necesidad de acompañamiento y por flujo de ingresos, no por franja etaria.** Es lo que sostienen los RCT.
- ⚠️ **Un resultado que no uso.** El resumen de una lista de figuras de Findex 2025 dice que, entre titulares de cuenta, los jóvenes usan menos pagos digitales que los mayores. Va contra la intuición y no pude abrir la figura; queda para verificar (§12).
- **Cómo se probaría** (con datos propios): medir conversión y renovación por edad *condicionada* a uso previo de app y billetera. Si la edad deja de explicar nada, era un proxy. El modelo de usuarios sintéticos del proyecto ya tiene las variables de acceso digital y bancarización junto a generación (ver [[modelo-personas-sinteticas]]): la prueba equivalente es si generación aporta algo una vez controladas esas dos.

---

## 3. 📋 Tabla de casos

Convención de la columna *Evidencia*: **RCT** = experimento aleatorizado; **Cuasi** = cuasi-experimento; **Obs** = observacional; **Caso** = caso de negocio; **Ind.** = reporte de industria. Después de la barra va quién reporta: **3.º** = evaluado por terceros, **Emp.** = lo reporta la propia empresa. "n.d." = no disponible en lo que pude leer.

### 3.1 Seguros

| # | Caso · país | Qué digitalizó / canal | Población | Intervención | Mecanismo conductual | Resultado | Duración | Evidencia | Fuente |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Seguro de cosecha vía comprador · Kenia | **No fue digital**: prima descontada en la cosecha por el comprador | Pequeños agricultores de contrato | Pagar al cosechar vs adelantado | Sesgo del presente, liquidez, riesgo de contraparte | 72% vs 5%; más fuerte entre los más pobres; +21 puntos con un mes de gracia | n.d. | RCT / 3.º (fuera de ventana) | F-847 |
| 2 | Seguro de clima y redes · China | Sesiones presenciales | 5.335 hogares rurales | Información difundida por la red | Prueba social | Más contratación; mayor si los primeros informados son centrales | n.d. | RCT / 3.º | F-848 |
| 3 | Seguro de lluvia a grupos · Etiopía | Capacitación a líderes | Grupos de ayuda mutua | Líder entrena en compartir riesgo de base | Intermediario confiable | Mayor contratación (selección vs efecto directo, sin separar) | n.d. | RCT / 3.º | F-850 |
| 4 | Seguro de lluvia, educación y garantía · India | Campo | Hogares rurales | Invitación a educación financiera; garantía de devolución; pronósticos | Comprensión; aversión a la pérdida | +5,3 puntos (base 6,4%); garantía eficaz a ~US$43,62 por póliza extra; pronósticos sin efecto | n.d. | RCT / 3.º | F-851 |
| 5 | Seguro de lluvia y pagos · norte de Ghana | Campo | Agricultores | Ofrecer seguro; pagos | Confianza por experiencia | Más inversión; la demanda sube con pagos propios y de la red | Varios años | RCT / 3.º (doc. de trabajo) | F-849 |
| 6 | MicroEnsure con Airtel y Tigo · Ghana y Tanzania | Vida gratis embebida en la telco; inscripción voluntaria | Clientes móviles | Cobertura gratis; mejora de pago después | Costo cero, experiencia de reclamo | >1 millón cubiertos, 80% sin seguro previo; de ~30% inscritos, 80% pagaría mejora | n.d. | Caso / Emp.; sobrevivió como marca, no como empresa | F-885, F-886 |
| 7 | EcoSure · Zimbabue | Funerario cobrado de la billetera EcoCash | Suscriptores de Econet | Prima desde US$0,50 al mes | Pago pequeño y automático | 2 millones (2018) vs 1,2 millones (2020): notas que se contradicen | n.d. | Caso / prensa | F-888 |
| 8 | Ecolife (Econet) · Zimbabue | Seguro gratuito | Suscriptores | — | — | **Fracaso regulatorio**: cerrado en 2011; 1,6 millones perdieron la cobertura | — | Caso / prensa | F-888 |
| 9 | GCash GInsure · Filipinas | Mercado de seguros dentro de la super-app | Usuarios de la billetera | 48 productos; seguro gratis al comprar saldo | Embebido, bajo costo | 14,6 millones cubiertos y 51,4 millones de pólizas (1T 2025); sin siniestros ni renovación | n.d. | Caso / Emp. (comunicado replicado) | F-889 |
| 10 | Pula · Kenia y África | Seguro empaquetado con insumos y programas de gobierno | Pequeños agricultores | Cobertura automática al canjear fertilizante | Default por compra | 9,6 millones de agricultores en 22 países (sin fecha); sin siniestros | n.d. | Caso / institucional | F-890 |
| 11 | PMJJBY y PMSBY · India | Cuenta bancaria + débito automático | Titulares de cuenta | Prima de Rs 20 anuales (accidentes) | Inercia | 26,79 crore de beneficiarios vs 12,55 crore de pólizas activas (vida); reclamos liquidados 99,95% | n.d. | Ind. oficial / 3.º; cifras por confirmar | F-891 |
| 12 | Policybazaar · India | Mercado en línea + 380.000 asesores | Compradores de salud y vida | Digital y asesor | Confianza por asesor | +40% de primas; 62% de pólizas nuevas de salud desde ciudades de 2.º y 3.er nivel; multa de Rs 50 M del regulador | n.d. | Caso / Emp.; regulador | F-892, F-893, F-884 |
| 13 | Seguro de Salud Yape con Pacífico Salud · Perú | App de la billetera, teleconsulta | Usuarios de Yape | Microprima (S/9,90 al mes según publirreportaje) | Embebido | Meta de 30.000 afiliados en un año; **sin resultado hallado** | n.d. | Caso / Emp. (meta) | F-894 |
| 14 | Nu Vida con Chubb · Brasil | App del banco digital | Clientes de Nubank | Seguro en la app | Embebido | 2 millones de pólizas activas (jun-2024) | n.d. | Caso / Emp. | F-895 |
| 15 | Azos · Brasil | Suscripción digital sin examen, vendida por corredores | Clientes de vida | Digital + corredor | Confianza por intermediario | Duplicó facturación en 2025; más de 9.000 corredores socios | n.d. | Caso / Emp. y prensa | F-377 |
| 16 | ComparaOnline · Chile, Brasil, Colombia | Flujos de WhatsApp para calificar leads | Compradores de auto y viaje | Filtrar interés antes del vendedor | Menor fricción de respuesta | +18% de conversión a venta (según el proveedor) | n.d. | Ind. / Emp. (proveedor) | F-896 |
| 17 | MiCRO · Centroamérica | Paramétrico vía microfinancieras, sin reclamo | Clientes de microfinanzas | Pago automático por índice | Elimina el trámite | 171 mil pólizas, 52% mujeres | n.d. | Caso / Emp. | F-790 |
| 18 | Renovación del seguro nacional · Ghana | Recordatorio y renovación automática por celular | Afiliados | Protocolo de RCT | Olvido, inercia | Línea base: ~45% con el seguro vencido; **resultados no encontrados** | — | Protocolo / 3.º | F-862, F-877 |

### 3.2 Otras industrias (mismo esquema)

| # | Caso · país · industria | Qué digitalizó | Población | Intervención | Mecanismo | Resultado | Duración | Evidencia | Fuente |
|---|---|---|---|---|---|---|---|---|---|
| 19 | M-Pesa · Kenia · pagos | Dinero móvil | Hogares kenianos | Acceso a agentes | Costo de transacción | Dicen 194.000 hogares fuera de la pobreza; **disputado** | Largo plazo | Cuasi / 3.º, con crítica publicada | F-855, F-856 |
| 20 | Recordatorios de ahorro · tres bancos · finanzas | SMS | Titulares de cuentas de compromiso | Recordar meta e incentivo | Saliencia, atención | Suben el logro de la meta; el encuadre no importa; más recordatorios tardíos no suman | n.d. | RCT / 3.º | F-857 |
| 21 | Préstamo digital · México · fintech | Crédito 100% digital | Prestatarios | Demorar el desembolso | Reconsideración | Duplicar la demora (10 a 20 h) baja 21% el impago | n.d. | Cuasi (regresión discontinua) / 3.º | F-860 |
| 22 | Avaaj Otalo · India · agtech | Consejo agrícola por voz | 1.200 agricultores | Solo teléfono; teléfono + extensión; control | Confianza, baja alfabetización | Adopción de insumos recomendados; disposición a pagar < costo del piloto | n.d. | RCT / 3.º | F-858 |
| 23 | SMS y llamadas a padres · Botsuana · educación | SMS y llamadas | Familias | SMS solo vs SMS + llamada | Compromiso, contacto humano | +0,12 DE el combinado; SMS solo sin efecto | n.d. | RCT / 3.º | F-861 |
| 24 | M-KOPA · Kenia · energía y telecom | Pago por uso con apagado remoto | Hogares sin red | Apagado ante impago | Aversión a la pérdida | Dice impago bajo, sin tasa; 47.625 "clientes duros" sin pagar | n.d. | Caso / Emp. y prensa | F-902 |
| 25 | Microcrédito · seis países · microfinanzas | Crédito | Prestatarios | Seis RCT | Acceso a capital | Efectos positivos pero modestos; sin reducir la pobreza | n.d. | RCT / 3.º | F-859 |
| 26 | Afiliación a seguro de salud · India, Indonesia, Ghana | Inscripción | Hogares | Subsidios, ayuda al registro | Precio, trámite | Subsidios temporales suben afiliación; más de la mitad de quienes intentan inscribirse no lo logra | Mientras dura el subsidio | RCT / 3.º (sin abrir) | F-863 |

---

## 4. 🧩 Inventario de intervenciones (qué se aplicó, sobre qué mecanismo y con qué efecto)

Convención: ✅ cambió la conducta (se midió contratación, pago o renovación real) · 📊 solo movió una métrica (inscritos, pólizas emitidas, conversión del lead).

| Tipo | Intervención | Mecanismo | Momento del ciclo | Efecto reportado | Duración | Costo | ¿Conducta o métrica? | Fuente |
|---|---|---|---|---|---|---|---|---|
| **Nudge / recordatorio** | Recordatorio de meta de ahorro | Saliencia | Mantenimiento | Sube el logro de la meta; magnitud no leída | n.d. | Bajo (n.d.) | ✅ (ahorro) | F-857 |
| | Recordatorio y renovación automática del seguro de salud | Olvido, inercia | Renovación | **Sin resultados todavía** | — | n.d. | — | F-862 |
| | Flujos de WhatsApp para filtrar leads | Menos fricción de respuesta | Venta | +18% de conversión (proveedor) | n.d. | n.d. | 📊 | F-896 |
| **Arquitectura de decisión** | Pagar en la cosecha | Sesgo del presente + liquidez | Compra y pago | 72% vs 5%; +21 pts con un mes de gracia | n.d. | Requiere un tercero que descuente | ✅ | F-847 |
| | Cobertura gratis con inscripción voluntaria (freemium) | Costo cero | Alta | ~30% se inscribe; 80% de ellos pagaría una mejora (empresa) | n.d. | Lo paga la telco o el asegurador | 📊 (inscripción) | F-885 |
| | Débito automático | Inercia | Alta y renovación | 26,79 vs 12,55 crore (vigencia ≈ mitad) | Caduca | Bajo | ✅ afiliación · 📊 vigencia | F-891 |
| | Ayuda al registro | Trámite | Alta | Más intentos; >50% de quienes intentan no logra inscribirse | n.d. | n.d. | 📊 | F-863 |
| | Demora deliberada del desembolso (crédito) | Reconsideración | Desembolso | −21% de impago | n.d. | — | ✅ (otra industria) | F-860 |
| **Incentivo / recompensa** | Subsidio de prima | Precio | Alta | Sube afiliación y atrae perfiles de menor costo; contratación "decepcionante" sin subsidios grandes | Mientras dura | Alto | ✅ mientras dura | F-863, F-800 |
| | Garantía de devolución | Aversión a la pérdida | Alta | Eficaz | n.d. | ~US$43,62 por póliza adicional | ✅ | F-851 |
| | Seguro gratis al comprar saldo | Recompensa | Alta | Cobertura de hasta PHP 30.000 | n.d. | Lo cubre el asegurador | 📊 | F-889 |
| **Prueba social y confianza** | Difusión por red social | Prueba social | Compra | Más contratación; mayor con personas centrales | n.d. | Bajo | ✅ | F-848 |
| | Líderes de grupo capacitados | Intermediario confiable | Compra | Mayor contratación | n.d. | Bajo | ✅ | F-850 |
| | Pagos de siniestro propios y ajenos | Confianza por experiencia | Renovación | La demanda sube con pagos propios y de la red | Años siguientes | — | ✅ | F-849, F-852 |
| **Acompañamiento humano** | Asesores sobre una plataforma digital | Confianza por persona | Venta | 380.000 asesores; 62% de pólizas de salud nuevas fuera de las grandes ciudades | n.d. | n.d. | 📊 (empresa) | F-892, F-893 |
| | Corredores como canal de la tecnología | Confianza por persona | Venta | Azos duplica facturación con 9.000+ corredores | n.d. | n.d. | 📊 (empresa) | F-377 |
| | Llamada humana sumada al SMS | Contacto humano | Mantenimiento | SMS solo no funcionó; con llamada, +0,12 DE | n.d. | Bajo en costo por DE | ✅ (otra industria) | F-861 |
| **Educación** | Invitación a educación financiera | Comprensión | Alta | +5,3 pts (completaron: +8,1) | n.d. | n.d. | ✅ | F-851 |
| | Educación financiera modesta | Comprensión | Alta | **Sin efecto** | n.d. | — | ✅ | F-799 |
| | Educar primero a personas centrales | Difusión | Compra | Mayor difusión | n.d. | Bajo | ✅ | F-848 |
| **Producto o precio** | Reducir el riesgo de base | Confianza | Diseño | La demanda cae cuando el pago se aleja de la pérdida real | — | — | Obs. | F-853, F-849 |
| | Microprima en la billetera | Ticket bajo | Alta | US$0,50 al mes (funerario); PHP 30 por 30 días; S/9,90 al mes | n.d. | n.d. | 📊 | F-888, F-889, F-894 |
| | Pago automático por índice, sin reclamo | Sin trámite | Siniestro | 171 mil pólizas, US$6 M pagados en Guatemala | n.d. | n.d. | 📊 (empresa) | F-790 |
| | Empaquetar con insumos o crédito | Default por compra | Alta | Pula; mejoras en contratación (revisión) | n.d. | n.d. | 📊 | F-890, F-800 |

### 4.1 Qué cambió conducta y qué cambió solo la métrica

- **Cambiaron conducta, con control:** pago en la cosecha, difusión por red, líderes de grupo, pagos visibles, garantía de devolución, invitación a educación financiera (F-847, F-848, F-850, F-849, F-851).
- **Solo movieron una métrica (sin control ni medición de uso):** pólizas emitidas de GCash y Nubank, inscritos de MicroEnsure, la conversión de leads en WhatsApp, la meta de 30.000 afiliados de Yape (F-889, F-895, F-885, F-896, F-894).
- **No encontré ninguna fuente que mida descargas de una app de seguros frente a su uso real.** Es una laguna; no puedo decir cuánto pasa.
- **Hay una contradicción que no resuelvo:** la educación financiera subió la contratación 5,3 puntos en un diseño (F-851) y una educación modesta no tuvo efecto en otro (F-799). Los diseños difieren; no hay forma de saber desde estos resúmenes cuál pesa más.

---

## 5. 👥 Población: quién fue digitalizado y quién quedó fuera

| Dimensión | Lo que sé (Perú y comparables) | Cómo se adaptó y con qué resultado | Vacío |
|---|---|---|---|
| **Edad** | Perú: internet 51,2% en 60+ vs 94-96% de 19 a 40 años (F-869). Ver §2 | Sin adaptación por edad documentada en seguros | Sin dato de contratación digital por edad en Perú |
| **Alfabetización digital** | Audio y pictogramas ayudan a usuarios de baja alfabetización (vi un resumen sobre billeteras en Pakistán; no lo registré en el ledger) | Consejo por voz (India) funcionó para adoptar insumos (F-858) | No hay prueba en seguros |
| **Dispositivo y conectividad** | 31% de los adultos sin cuenta en países de ingreso bajo y medio no tiene teléfono (F-867). Perú: 98,6% de quienes usan mensajería usa WhatsApp (F-871) | Embebido en telco (MicroEnsure) o billetera (GCash, Yape) | Sin dato de propiedad de dispositivo por segmento en Perú |
| **Inclusión financiera** | Perú: cuentas 43% a 57% (2017-2021); cuentas por celular 3% a 14%; pagos digitales 34% a 49% (F-872). Billeteras con uso de 62,3% (F-871) | Seguro cobrado desde la billetera (F-888, F-889) | Cifras de 2021, anteriores al auge de billeteras |
| **Educación** | Los agricultores más educados cambiaron más su producción tras el seguro (F-852) | Educación financiera: efectos opuestos (F-851 vs F-799) | Sin efecto sobre contratación por nivel educativo |
| **Ingreso** | El pago en cosecha ayudó más a los más pobres (F-847); la contratación sube con riqueza (F-853) | Subsidios (F-863) | — |
| **Formalidad laboral** | Sin dato peruano verificado en esta sesión (una nota de Gestión hablaba de ~3 millones sin seguro de salud por informalidad; no la registré) | Pago atado al ingreso: solo en agricultura (F-847) | Falta el dato de informalidad por segmento |
| **Urbano / rural** | India: 62% de pólizas nuevas de salud desde 2.º y 3.er nivel (F-893, empresa) | Híbrido: ventas presenciales crecen (F-893) | Sin dato rural-urbano de seguros digitales en Perú |
| **Género** | América Latina: brecha de internet móvil ≈ −1% en 2024 (F-868, a confirmar); Asia del Sur 32%, África Subsahariana 29%. Mujeres ≈ 48-49% de asegurados de microseguros (F-873) | MiCRO: 52% mujeres (F-790) | En Perú el género no parece ser la barrera de acceso; la barrera sería otra (sin dato) |
| **Intermediarios** | Bancaseguros ≈ 37,65% del mercado peruano 2025, estimación de firma de mercado (F-900). Digital ≈ 7% de las ventas globales de Mapfre (F-901). En América Latina el microseguro usa más instituciones financieras (F-873) | Modelo híbrido: Azos, Policybazaar | No hallé la mezcla de canales por aseguradora en Perú |

### 5.1 Quién queda fuera y cuánto cuesta

- **Quedan fuera, con evidencia:** quienes no tienen cuenta ni teléfono (F-867), quienes dependen de ingresos irregulares (pago adelantado = 5%, F-847), y quienes tratan con intermediarios falsos (F-880).
- **Quedan fuera, por inferencia mía:** informales sin flujo regular, rurales sin conexión estable, mayores que no usan internet (48,8% de los 60+, F-869) y que no tienen quién los ayude.
- **Costo de la exclusión:** el microseguro cubre ~330 millones de personas en 36 países, 11,5% del potencial; el mercado estimado de US$41.400 M está alcanzado solo en 15% (F-873). En Perú, 2% de penetración y solo 3,3% de hogares con seguro de desastres (F-5).
- ⚠️ **Tensión de definiciones:** 94,4% de los mayores de 60 tiene "algún seguro de salud" (F-870) frente a "solo 7% de las familias peruanas tiene seguro de salud" (F-894). Casi seguro miden cosas distintas (público vs privado); no lo resuelvo.

---

## 6. 🔧 Brechas: dónde la digitalización resolvió la fricción y dónde la movió

| Etapa de la póliza | Fricción conductual | ¿Qué hizo la digitalización? | Evidencia |
|---|---|---|---|
| **Conocer y considerar** | Desconfianza; falta de información (causa nº 1 de desconfianza en Perú, F-1) | **Resolvió el alcance** (WhatsApp, billeteras). **Movió la confianza**: llamadas sin consentimiento, estafas con SOAT falso | F-878, F-880 |
| **Comprar** | Sesgo del presente; liquidez; carga cognitiva | Redujo el ticket con microprimas. **No tocó el momento del pago**, que es lo que movió 5% a 72% en el RCT | F-847, F-894 |
| **Entender** | Exclusiones que se descubren al siniestrar | **Sin evidencia de mejora.** La cobertura gratuita embebida no mide si el cliente sabe que la tiene. Indecopi ya sanciona a la aseguradora que no prueba que informó la exclusión | F-881, F-486, F-885 |
| **Pagar y cobrar** | Olvido; inercia | Débito automático logra afiliar pero la vigencia cae a cerca de la mitad (con reservas) | F-891 |
| **Siniestro** | Desconfianza en que paguen | El paramétrico elimina el trámite en catástrofe; en seguros comunes, Indecopi sigue multando por no pagar | F-790, F-879 |
| **Renovar** | Olvido; ver pagos | Sin resultado todavía de los recordatorios (protocolo en Ghana). Los pagos propios y ajenos sí sostienen la demanda | F-862, F-849 |
| **Retener** | Abandono | Las telcos reportan menos churn con seguro (dato de empresa antiguo) | F-887 |

**Resumen del patrón (inferencia mía a partir de lo anterior):** la digitalización abarató y acercó la venta. La fricción se desplazó a tres sitios: (1) la confianza en el vendedor, (2) la comprensión de lo comprado y (3) la vigencia. Nada de eso aparece en las métricas de alcance.

### 6.1 Oportunidades sin cubrir en LatAm, por segmento (hipótesis, no hallazgos)

- **Comerciantes y mypes con billetera:** cobro de la prima junto con la venta diaria. Falta probarlo.
- **Transportistas y mototaxistas (SOAT):** canal verificado y pagos visibles; el fraude con SOAT falso es un dolor reportado (F-880).
- **Agricultores del norte expuestos al Niño Costero:** paramétrico con pago a billetera. Ya hay reglamento (F-786) y antecedentes (F-798, F-790); ver [[fenomeno-el-nino-impacto-personas]].
- **Mujeres emprendedoras:** la brecha de acceso móvil en LatAm es cercana a cero (F-868), pero ninguna evidencia revisada prueba que ese sea el segmento con más retorno.
- **Personas que no resuelven solas (mayores o no):** acompañamiento humano sobre canal digital. Sin experimento de seguros que lo respalde.

---

## 7. 🌍 Otras industrias: mismo esquema

**Criterio de selección:** problemas análogos a seguros: confianza (M-Pesa, consejo agrícola), bajo uso (SMS), abandono y pago recurrente (ahorro, pago por uso, microcrédito), producto intangible (consejo, seguro) y baja alfabetización digital (voz). Los casos de las filas 19-26 de §3.2 los cubren.

| Industria | Qué enseña | Intervención | Población | Resultado | Fuente |
|---|---|---|---|---|---|
| Fintech y pagos | El dinero móvil escaló en Kenia, pero el efecto sobre la pobreza está en disputa. La fricción puede ser útil: demorar el desembolso redujo el impago | Acceso a agentes; demora del préstamo | Hogares; prestatarios en México | 194.000 hogares (disputado); −21% de impago | F-855, F-856, F-860 |
| Salud | Subsidios y trámites simples suben la afiliación; la ayuda al registro no basta; la renovación está en prueba | Subsidio; registro asistido; recordatorio | Hogares en India, Indonesia, Ghana | Afiliación sube mientras dura el subsidio | F-863, F-862 |
| Microfinanzas | Efectos modestos, no transformadores: calibrar expectativas | Crédito | Seis países | Positivo y pequeño | F-859 |
| Agtech | Un canal de voz puede generar confianza y adopción con baja alfabetización | Consejo por teléfono ± extensión | 1.200 agricultores | Adopción de insumos; costo > disposición a pagar en el piloto | F-858 |
| Educación | El SMS solo no basta; sumar contacto humano | SMS y llamadas | Familias en Botsuana | +0,12 DE; el SMS solo, sin efecto | F-861 |
| Telecom y energía | La telco como canal de seguro; el pago por uso funciona con apagado, que en seguros equivale a perder la cobertura | Seguro gratis; apagado | Clientes móviles | Cifras de empresa | F-885, F-902 |
| Retail | Solo hay un experimento fuerte de gamificación; sin evidencia causal en LatAm. Ver [[lealtad-gamificacion-recompensas-retail]] | — | — | — | — |
| Servicios públicos | La afiliación masiva por débito automático no equivale a vigencia | Esquemas estatales de India | Titulares de cuenta | ~Mitad activa (con reservas) | F-891 |

---

## 8. 🔁 Transferibilidad a Perú

Clasificación: **T** = transferible · **A** = transferible con adaptación · **N** = no transferible. Perú tiene billeteras de uso masivo (Yape, Plin), WhatsApp casi universal entre quienes usan mensajería (F-871) y un regulador que permite vender a distancia (F-898) y amplió el comercializador de microseguros a emisoras de dinero electrónico (F-899).

| Hallazgo | Qué lo hizo funcionar | ¿Existe en Perú? | Adaptación necesaria | Clase |
|---|---|---|---|---|
| Cobro atado al ingreso (72% vs 5%, F-847) | Un tercero con relación estable (el comprador) que descuenta; ingreso estacional | Agroexportadoras, cooperativas, plataformas de reparto y transporte, comerciantes con billetera | Definir quién descuenta; consentimiento expreso; no probado fuera de agricultura | **A** |
| Difusión por red y líderes de grupo (F-848, F-850) | Redes densas con líderes creíbles | Gremios, asociaciones de transportistas, mercados, grupos de WhatsApp | Canal WhatsApp; cuidado con el contacto no solicitado (Ley 32323, F-878) | **A** |
| Pagos visibles sostienen la demanda (F-849, F-852) | Siniestros que ocurren, se pagan rápido y se conocen | Norte del país con Niño Costero; SOAT | Datos y disparador; comunicar los pagos | **A** |
| Garantía de devolución (F-851) | Reduce el riesgo percibido | Aplicable | Costo de ~US$43,62 por póliza adicional; probar solo en segmento de alta desconfianza | **A** |
| Cobertura gratuita embebida (F-885) | Base cautiva de telco o billetera | Yape y telcos | Consentimiento (F-878); riesgo de cierre regulatorio (Ecolife, F-888) | **A** |
| Prima cobrada de la billetera (F-888, F-889) | Débito pequeño y automático | Yape, Plin | Consentimiento y tope de prima (F-899) | **A** |
| Débito automático estatal masivo (F-891) | Programa del Estado con prima casi simbólica | No como política | Solo se toma la lección: afiliar no es conservar | **N** (lección: sí) |
| Recordatorios (F-857, F-862) | Bajo costo; olvido como causa | Sí | Sin resultado en seguros: probar | **T** (a probar) |
| Voz para baja alfabetización (F-858) | Confianza y bajo esfuerzo | Notas de voz en WhatsApp | Contenido y lenguas (inferencia mía) | **A** |
| Contacto humano sobre el SMS (F-861) | Compromiso personal | Asesores, centros de contacto | Costo | **T** |
| Demorar el desembolso (F-860) | Reconsideración | — | Sin base en seguros; solo hipótesis | **A** (investigar) |
| M-Pesa y reducción de pobreza (F-855) | — | — | Disputado; no usar como argumento | **N** |
| Pago por uso con apagado remoto (F-902) | Pérdida inmediata del servicio | — | En seguros, apagar es perder cobertura: riesgo reputacional y regulatorio | **N** |
| Seguro de índice sin subsidios (F-800) | Subsidio grande y sostenido | Parcial | Contratación "decepcionante" sin subsidio | **N** si no hay subsidio |
| Expectativas modestas (F-859) | — | — | Calibrar metas de impacto | **T** |

---

## 9. 🧮 Matriz intervención × segmento

✅ evidencia directa (RCT en un segmento similar) · 🟡 evidencia indirecta (otra industria, o caso de empresa) · ❔ sin evidencia · ⛔ evidencia en contra.

| Intervención | Adulto urbano con billetera | Informal de ingreso diario | Agricultor / rural | Mayor de 60 poco digital | Mujer emprendedora | Cliente con asesor |
|---|---|---|---|---|---|---|
| Recordatorio / autorrenovación | 🟡 (ahorro, F-857) | ❔ | ❔ | ❔ | ❔ | 🟡 |
| Cobro atado al ingreso | ❔ | 🟡 (EcoSure, F-888) | ✅ (F-847) | ❔ | ❔ | ❔ |
| Prueba social, líder o red | ❔ | ❔ | ✅ (F-848, F-850) | ❔ | ❔ | ❔ |
| Pagos de siniestro visibles | ❔ | ❔ | ✅ (F-849, F-852) | ❔ | ❔ | ❔ |
| Cobertura gratis embebida | 🟡 (GCash, F-889) | 🟡 (F-885) | ❔ | ❔ | ❔ | ❔ |
| Acompañamiento humano sobre digital | ❔ | ❔ | 🟡 (F-858, efectos por brazo no leídos) | ❔ | ❔ | 🟡 (F-377, F-892) |
| Educación financiera | ❔ | ❔ | ✅ pero contradictoria (F-851 vs F-799) | ❔ | ❔ | ❔ |
| Voz / audio por WhatsApp | ❔ | ❔ | 🟡 (F-858) | ❔ | ❔ | ❔ |
| Paramétrico con pago automático | ❔ | ❔ | 🟡 (F-790, empresa) | ❔ | 🟡 (52% mujeres, F-790) | ❔ |

**Lectura:** casi toda la matriz está vacía. El segmento agricultor tiene la evidencia mejor; el de mayores de 60, ninguna. Ese vacío es el hallazgo: cualquier celda vacía que se decida llenar es, en rigor, un experimento.

---

## 10. 🗺️ Mapa de oportunidades (impacto vs facilidad en Perú)

Las puntuaciones (1-5) son **mi juicio, no una medición**. Impacto = cuánto movería contratación, vigencia o confianza si funciona. Facilidad = qué tan rápido se prueba hoy en Perú con lo que existe.

| Prioridad | Oportunidad | Impacto | Facilidad | Evidencia que la sostiene | Primer experimento | Medida de uso real |
|---|---|---|---|---|---|---|
| 1 | **Acompañamiento humano sobre el canal digital** para quienes no resuelven solos | 4 | 4 | Policybazaar y Azos (F-892, F-377); SMS más llamada (F-861); sin experimento de seguros | Asesor que cierra por WhatsApp contra autoservicio, en la misma población | Conversión y renovación; costo por póliza vigente |
| 2 | **Cobro atado al flujo de ingresos** (descuento al cobrar la venta, el viaje o la cosecha) | 5 | 3 | RCT en Kenia (F-847); EcoSure (F-888) | Piloto con un aliado que ya liquide ingresos al cliente | Contratación y vigencia a 90 días frente al cobro mensual fijo |
| 3 | **Renovación asistida**: recordatorio por WhatsApp y SMS más renovación automática por billetera, con consentimiento | 3 | 5 | Recordatorios en ahorro (F-857); olvido como causa de no renovar (F-877); sin resultados en seguros (F-862) | Cuatro brazos en la base propia: control, SMS, WhatsApp, autorrenovación | Renovación a 30 y 90 días, no aperturas |
| 4 | **Medir el uso real**: tablero con vigencia, siniestros pagados y comprensión, no pólizas emitidas | 3 | 5 | Todas las cifras de alcance carecen de uso (§4.1) | Medición retroactiva en la base | Vigencia a 12 meses; reclamos pagados |
| 5 | **Distribución con terceros confiables** (gremios, cooperativas, plataformas) | 4 | 3 | F-848, F-850; Pula (F-890) | Un gremio como aliado, con líder capacitado | Contratación por gremio y vigencia |
| 6 | **Canal verificado y antifraude** (SOAT, WhatsApp oficial) | 3 | 4 | F-880, F-878 | Número verificado y mensaje estándar | Quejas por fraude; confianza declarada |
| 7 | **Paramétrico con pago a billetera** en zonas del Niño Costero | 5 | 2 | Reglamento (F-786), antecedentes (F-798, F-790), pagos visibles (F-849) | Piloto con una caja o cooperativa del norte | Pagos realizados y renovación al año siguiente |
| 8 | **Mujeres emprendedoras** | 3 | 3 | Brecha móvil ≈ 0 (F-868); MiCRO (F-790) | Oferta de microseguro por la billetera | Contratación y siniestros por género |
| 9 | **Cobertura gratis embebida con puente a pago** | 3 | 2 | MicroEnsure (F-885); riesgos: Ecolife (F-888), consentimiento (F-878) | Solo con revisión legal previa | Conversión a pago y comprensión de la cobertura |

*Regla de orden: impacto × facilidad; a igual producto, gana el de mayor impacto.*

### 10.1 Hipótesis para probar (cada una con su resultado real)

- **E1.** ¿Un recordatorio por WhatsApp renueva más que uno por SMS, y más que no recordar? Resultado: renovación a 90 días.
- **E2.** ¿Cobrar al momento del ingreso del cliente sube la contratación frente a la cuota mensual fija? Resultado: contratación y vigencia a 90 días.
- **E3.** ¿Un asesor por WhatsApp supera al autoservicio en la misma población, y la diferencia depende de la edad? Resultado: conversión y renovación; separar el efecto de la edad del uso previo de app.
- **E4.** ¿El respaldo de un gremio o líder sube la contratación? Resultado: contratación por gremio.

---

## 11. 🧭 Las tres pistas, por separado, y su síntesis

### 11.1 🔬 Pista empírica

- **Qué sostiene:** los RCT sobre seguro de lluvia en India, Kenia, Ghana, China y Etiopía muestran que pesan la confianza, la liquidez, el momento del pago y las redes; el precio importa pero no basta (F-799, F-847, F-848, F-849, F-850, F-853).
- **Qué no sostiene:** nada de esto prueba el efecto de un canal digital. Es seguro agrícola de índice, casi todo de 2008-2018 (fuera de ventana). La transferencia a vida, salud o auto no está probada.
- **Contradicciones que no resuelvo:** (1) educación financiera: F-851 vs F-799; (2) M-Pesa y pobreza: F-855 vs F-856, donde los críticos son además adversarios declarados del microfinanciamiento; (3) edad y contratación de seguro de índice: F-864 vs F-865.

### 11.2 📱 Pista social y regulatoria

- **Qué encontré:** no pude ver conversación en Reddit ni en X. Lo que hay es regulador y prensa. En India, las quejas por venta engañosa crecen (+11,2% interanual, F-882); el regulador la califica "a nivel alarmante" (F-883) y multó a Policybazaar (F-884). En Perú: sanciones a Pacífico por llamadas sin consentimiento (F-878), multa a Mapfre por no pagar un SOAT (F-879), estafas con SOAT falso (F-880) y un foro de 2019 con una queja puntual sobre exclusiones descubiertas en el siniestro (F-881).
- **Nivel de instalación:** 💬 en Perú (conversación de nicho, empujada por el regulador); 🌡️ en India (cifra de quejas en alza). Es **validación institucional, no social**: no hay comentarios de personas que confirmen o desmientan.
- **No encontré** ninguna queja de clientes sobre seguros por dinero móvil en Kenia, Nigeria o Ghana.

### 11.3 💼 Pista de negocio

- **Qué sostiene:** el alcance es grande (GCash: 14,6 millones de personas; Policybazaar: +40% de primas y 59 millones de pólizas; Nubank y Chubb: 2 millones; Azos duplicó facturación) y los modelos que mejor funcionan **combinan digital con persona** (asesores en Policybazaar, corredores en Azos).
- **Qué no sostiene:** casi todo es autorreportado y sin uso, siniestros ni vigencia. En Perú no encontré cifras del canal digital por aseguradora; el único dato directo del segmento es una **meta** de 30.000 afiliados de Yape sin resultado (F-894). El CEO global de Mapfre dijo en 2022 que el canal digital es ~7% de sus ventas y complemento del asesor (F-901).
- **Sesgo de supervivencia:** MicroEnsure absorbida, Ecolife cerrada, Betterfly cerró en cinco países.

### 11.4 ⚖️ Síntesis (sin mezclar los criterios de validez)

- **Convergen:** (a) el canal digital amplía el alcance, no resuelve confianza ni liquidez; (b) la misma raíz, la confianza, aparece en el RCT (trust, F-799), en el regulador (venta engañosa, llamadas sin consentimiento) y en el negocio (los híbridos con persona).
- **Divergen, y no lo resuelvo:** el negocio muestra crecimiento (51,4 millones de pólizas, +40% de primas) mientras lo regulatorio muestra más quejas y lo empírico advierte que afiliar no es conservar. No se sabe si el crecimiento comprado es duradero.
- **Implicación para la pregunta original:** la oportunidad no está en "digitalizar más" sino en **diseñar el momento del pago, el respaldo de un tercero y el acompañamiento**, y en **medir vigencia y uso**.

---

## 12. 🕳️ Lagunas

- **Sin experimentos de canal digital en seguros** (app, WhatsApp, USSD) en un mercado emergente. Los RCT son de contrato y confianza.
- **Sin dato de contratación digital de seguros por edad en Perú.** Lo más cercano es uso de internet por edad (F-869) y seguro de salud por edad (F-870, sin distinguir público de privado).
- **USSD:** no encontré ninguna evidencia de seguros por USSD.
- **Mediación familiar:** no encontré evidencia de seguros contratados por un familiar en nombre de un mayor.
- **Mapfre, Sura, Bradesco y otras aseguradoras de la región:** sin cifras de canal digital ni WhatsApp.
- **Perú:** sin cifras por aseguradora del canal digital; sin resultado real de Yape-Pacífico; sin dato verificado de informalidad.
- **Duración de los efectos:** casi ninguna fuente la reporta. No puedo distinguir efecto corto de sostenido.
- **Por verificar:** (1) el resumen de Findex sobre jóvenes y mayores entre titulares de cuenta (§2.3); (2) los países de los tres bancos del experimento de recordatorios de ahorro (F-857): creo que uno estaba en Perú, pero no pude confirmarlo; (3) el comunicado exacto de la India sobre vigencia (F-891); (4) los resultados del protocolo de renovación en Ghana (F-862).
- **Las tres pistas no pesan igual:** la empírica es la más sólida; la social casi no existe como conversación; la de negocio es en su mayoría autorreportada.

---

## 13. 🧪 Implicaciones para el modelo `lapuerta`

El modelo de usuarios sintéticos ya incluye generación, acceso digital y bancarización. La conclusión del §2 sugiere probar si generación explica algo una vez controladas esas dos. Ningún cambio al esquema hasta que exista un dato propio que lo respalde (ver [[modelo-personas-sinteticas]]).

---

## 14. 📓 Bitácora

- **2026-10-15 · v1.0** — Creación. `/trinidad`; 56 fuentes (F-847 a F-902). Herramientas de descarga sin internet: todo vía resúmenes de búsqueda. Hipótesis de edad no definida en el encargo; se evaluó la formulación del §0.

---

## Limitaciones

- Lectura por **resúmenes**; sin acceso a los artículos completos. Varias atribuciones quedaron "no capturadas" en el ledger.
- La búsqueda solo ve resultados de EE.UU. y en español devolvió sobre todo prensa; no llegó a Reddit ni a X.
- La evidencia aleatorizada es de seguro agrícola de índice; las cifras de negocio son autorreportadas.
- Las puntuaciones del §10 son juicio mío.

## Conexiones

- [[venta-vida-digital-hibrida-latam|Venta de vida en LATAM: digital vs. híbrido vs. tradicional]] — los casos regionales (Azos, Betterfly, bancaseguros) que aquí se comparan con África y Asia.
- [[futuro-asesores-seguros-venta-digital|¿Desaparecerán los asesores?]] — el patrón de este node (los mejores modelos combinan digital y persona) coincide con esa tesis.
- [[seguros-comportamiento-mundo-peru|Comportamiento y mercado de seguros: Mundo vs. Perú]] — línea base de confianza, tenencia y barreras en Perú.
- [[behavioral-design-estado-disciplina|Behavioral design: estado de la disciplina]] — marco de qué intervenciones tienen respaldo y cuáles no.
- [[fenomeno-el-nino-impacto-personas|Impacto del Fenómeno El Niño]] — el paramétrico con pago a billetera (prioridad 7 del §10) viene de ese análisis.
- [[transicion-venta-fria-a-opt-in|De venta fría a opt-in]] — consentimiento y llamadas no solicitadas (Indecopi) que aquí aparecen como fricción movida.
- [[lealtad-gamificacion-recompensas-retail|Gamificación, recompensas y lealtad en retail]] — contraste: allí también hay una sola prueba fuerte y nada causal en LatAm.
- [[modelo-personas-sinteticas|Modelo de personas sintéticas (`lapuerta`)]] — las variables de generación, acceso digital y bancarización que el §2 sugiere probar.
- [[literatura-baja-digitalizacion-seguros-por-region|Qué dice la literatura sobre la baja digitalización de los seguros, por región]] — el mismo tema leído desde la literatura, de lo global a Perú.
- [[senales-insurtech-mundo|Señales del mundo insurtech]] — financiamiento, IA, seguros embebidos y regulación hoy.
