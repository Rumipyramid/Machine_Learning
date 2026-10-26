# Digitalización en seguros (LatAm y mercados emergentes): qué se digitaliza, qué cambia la conducta y dónde hay oportunidades

> Documento de investigación. Fuente persistente y versionada en el repositorio.
> Fecha de elaboración: 2026-10-26 · Última actualización: 2026-10-26 · Versión: **v1.0**
> Origen: `/trinidad` (pista empírica + social + negocio), rol *behavioral designer / UX researcher* de una aseguradora peruana.
> Fuentes en `research/fuentes/codice.md`: **F-847 a F-940** (nuevas). Se reutilizan además F-1, F-3, F-4, F-9, F-25, F-70, F-117, F-180, F-182, F-183, F-353, F-362 a F-379, F-442, F-485, F-486, F-504 a F-507, F-529 y F-805 a F-808.
> Pregunta permanente: **¿cómo y para qué se digitalizan las aseguradoras, qué intervenciones cambian la conducta real (y cuáles solo mueven una métrica), sobre quiénes, y qué es transferible a Perú?**
> Decisión que alimenta: **base estructural de una estrategia digital** (no solo táctica) y tres definiciones basales: cliente digitalmente sano, fidelidad y cliente de alto valor.

---

## 0. Alcance, método y límites de lectura

- **Qué cubre.** Seguros (vida, salud, vehicular/SOAT, patrimoniales, microseguros) en Perú, LatAm, India, Sudeste Asiático y África; y analogías de pagos, banca, crédito digital, educación, telecomunicaciones y servicios públicos. Ventana preferente: 2021-2026; los clásicos van marcados.
- **Hipótesis de edad.** El texto del encargo que se reenvió **omitió** el párrafo de la hipótesis, pero el formato de salida y las reglas de evidencia la siguen pidiendo. Se evaluó la formulación original: *"los usuarios de mayor edad presentan un rechazo natural a la digitalización de seguros debido a brechas tecnológicas, prefiriendo siempre el canal humano, independientemente del diseño de la interfaz"*.
- ⚠️ **Todo se leyó por resúmenes y fragmentos de búsqueda.** En esta sesión no se pudo abrir ninguna página ni PDF (la descarga directa devolvió error de red). Por eso hay cifras sin intervalo ni tamaño de muestra, y varios títulos quedaron marcados "no verificado" en el ledger. **Nada de lo de abajo debe citarse hacia fuera sin abrir el original.**
- ⚠️ **La pista social es la más débil.** No se llegó a Reddit, X ni TikTok (la búsqueda no devolvió hilos). Se usó prensa de consumo, resoluciones y denuncias, y encuestas de percepción. Mide percepción institucional, no validación social de las apps.
- ⚠️ **Pista "datos internos" sin cubrir.** No hubo acceso a datos de la aseguradora. Las tres definiciones basales (§F) son **criterios y fórmulas propuestos**, no valores; los umbrales deben salir de esos datos.
- ⚠️ **No se probaron las apps de la competencia.** El mapa de oferta local (§3, fila de competencia) se arma con descripciones públicas de tiendas de apps, memorias y prensa. Hace falta una auditoría de uso real (§G).
- **Cómo se etiqueta la evidencia.** *RCT* (experimento aleatorizado), *cuasi-experimento*, *observacional*, *caso de negocio*, *reporte de industria*, *opinión*. **PR** = lo reporta la propia empresa; **tercero** = lo evalúa alguien independiente. **⚠️S** = riesgo de sesgo de supervivencia (solo se publican casos exitosos).

---

## 1. Resumen ejecutivo

1. **La compra cambia por quién avala y cuándo se cobra, no por la interfaz.** Dos RCT arbitrados (agro, India y Kenia): el aval de un tercero local de confianza subió **40%** la probabilidad de compra (F-847) y cobrar la prima a la cosecha llevó la compra de **5% a 72%** (F-848). Es transferible con adaptación; **no existe un RCT equivalente en vida, salud o SOAT en LatAm**.
2. **Lo digital mueve la renovación donde el obstáculo es el olvido y la fricción de pago.** Ghana: **+17,4 puntos** con pago y recordatorios por celular (cuasi-experimento, N=57.993, F-856), con más efecto en informales. El RCT que lo confirmaría (F-857) aún no tiene resultados.
3. **"Digital reduce el churn" no está demostrado.** En India lo online persiste más (71% vs 43-51% al mes 61, F-870); en Australia ~40% de las pólizas directas caducan el primer año (F-871). **No hay dato público de persistencia por canal en Perú ni en LatAm.** Lo que sí acompaña a quedarse es tener más de un producto (F-873, F-874), con la selección como explicación alternativa.
4. **Bancaseguros: el activo es la confianza en el banco; la responsabilidad ante un problema es difusa.** 72% se quedaría más tiempo en su banco si compra un seguro allí y 9 de 10 no asegurados lo contrataría con su banco (encuesta de consultora, F-903). **Ningún estudio mide a quién culpa el cliente**; la evidencia indirecta apunta a "un solo problema, dos responsables" (§A.3).
5. **Hipótesis de edad: matizada.** La preferencia por un humano es real en reclamos y en compras complejas, pero no es "natural", ni "siempre", ni independiente del diseño: depende de geografía, ingreso, confianza, miedo a estafas y de si hay alguien que asista (§2).
6. **El digital que ya funciona en Perú es el de producto estandarizado y obligatorio.** SOAT: 9 de cada 10 se emite digital (2022, F-891), con riesgo de suplantación (F-892). Fuera de SOAT, la compra online sigue siendo "reducida" (F-920) y la apuesta embebida más visible (Salud Yape) se fijó **30.000 afiliados sobre ~17 millones de usuarios (0,18%)**, sin resultados publicados (F-913).
7. **El techo real de la digitalización es el segmento formal y urbano.** 70,7% de informalidad (F-878); 23,4% de hogares rurales con internet (F-876); solo 11,8% de independientes con seguro social (F-879). Para el resto el diseño debe ser **asistido** (agente, familiar, tienda), no "menos digital".
8. **En el siniestro la fricción se mueve, no desaparece.** Los reclamos 100% digitales fallan 33-39% y quien escala a un humano califica peor (NPS −11, F-183); solo 22% de las actualizaciones digitales son adecuadas (F-909). Hay que diseñar **"digital con humano a un toque"** y medir recontacto.
9. **No transferible tal cual:** educación financiera como palanca única (F-847, F-852, F-862), productos o cuentas gratis (solo 3% usó la cuenta gratis en Chile, F-861) y métricas de adopción nominal (CoDi: 21,8 M de cuentas, <2,5 M pagaron, F-896).
10. **Las tres definiciones basales se arman con eventos y cohortes, no con frecuencia de uso** (§F): resolución verificada sin recontacto; renovación activa y conducta tras el siniestro; y valor esperado ajustado por la respuesta a la intervención, no por el tamaño de la cuenta.

---

## 2. Veredicto de la hipótesis de edad: **matizada**

**Confianza: baja a moderada.** No encontré ningún estudio que pruebe la hipótesis tal como está escrita. La parte *"independientemente del diseño de la interfaz"* **no tiene prueba directa a favor ni en contra** en seguros.

| | Qué dice la evidencia | Nivel · pista · fuente |
|---|---|---|
| **A favor** | 59% de los boomers prefiere hablar con una persona antes que un proceso totalmente digital; solo 7% ve el autoservicio como ideal; ~28% dice haber evitado reclamar por frustración con plataformas digitales | Reporte de industria (encuesta de proveedor, EE.UU./Canadá), PR · F-898 |
| **A favor** | En Brasil, al cierre de 2021 usaba Pix el 37% de los mayores frente a 71% de la población, y eran el blanco principal de estafas | Encuesta del gremio bancario vía prensa · F-894; los 60+ eran 4,1% de usuarios con 14,6% de población · F-895 |
| **A favor** | En Perú usa internet 47% de los de 60+ (urbano 56,8%; rural 14,6%), frente a 82% de la población de 6+ | Estadística oficial vía prensa · F-877, F-876 |
| **A favor** | El reclamo es el momento donde todos quieren a una persona: 90% de todas las edades dice que lo humano importa; solo 45% confía en la IA para presentar un reclamo | Reportes de industria · F-899, F-901 |
| **En contra** | La edad predijo mal la preferencia de canal; 32% de los de 18-24 prefería cotizar en persona; en reclamos el call center era el canal principal en **todas** las edades | Reporte de industria (EE.UU., 2013, antiguo) · F-900 |
| **En contra** | Los mayores de 65 fueron **los menos** dispuestos a pagar más por intervención humana (31%) | Reporte de industria (Reino Unido) · F-899 |
| **En contra** | Pensión 65: mayores en pobreza extrema cobran con tarjeta de débito (>700.000) y **33.674 usan a un tercero autorizado** (un familiar cobra por ellos). El canal bancario se adopta cuando hay beneficio claro y alguien asiste | Prensa que cita a entidades públicas (caso observacional) · F-880 |
| **En contra** | En un estudio en Lima, la facilidad de uso percibida fue la variable más ligada a adoptar Yape entre mayores: depende del diseño | Tesis, solo Lima · F-882 |
| **En contra** | Un portal de inscripción a Medicare reporta 22% de inscripciones online en 4T-2018 y 27% en 2019 entre mayores de 65 (aunque admite que algunos siempre necesitarán un agente) | Caso de negocio, PR, ⚠️S · F-935 |
| **Alternativas que explican lo mismo** | Educación, ingreso y zona (dentro de los mayores, la brecha urbano-rural es enorme, 56,8% vs 14,6%, y la geografía podría pesar tanto o más que la edad: inferencia); miedo a estafas (los mayores son el blanco principal de golpes en Pix, F-894); y soporte disponible (los allegados ayudan a los mayores con la banca, a veces compartiendo claves, F-866, F-867) | Observacional |
| **Sin resultados todavía** | Dos ensayos de capacitación bancaria a mayores (Alemania, N=333; Bangladesh, N=484) | F-868, F-869 |

**Lectura.** Lo que sostiene la evidencia es una versión más acotada: *los mayores prefieren un humano en el reclamo y en decisiones complejas, y adoptan canales digitales cuando el beneficio es claro, el uso es simple y hay alguien de confianza que asista*. Dos advertencias: (1) casi todo lo que apoya la hipótesis viene de encuestas de proveedores en EE.UU., Canadá y Reino Unido, no de LatAm; (2) **no hay evidencia de seguros en adultos mayores de LatAm**; la mejor señal peruana (Pensión 65) no es un seguro.

**Contradicciones entre fuentes (no resueltas).** Una encuesta dice que los mayores quieren más humano (F-898) y otra que son los que menos pagarían por más humano (F-899): miden cosas distintas (preferencia vs. disposición a pagar), en países distintos y con proveedores con interés. Tampoco coinciden las dos notas del INEI sobre mayores que usan internet (47% vs 44,9%, F-877).

---

## 3. Tabla de casos conductuales y estratégicos

Columnas: Empresa o programa · País e industria · Qué digitalizó · Población · Intervención · Mecanismo conductual · Resultado y duración · Nivel de evidencia y fuente. **Fila 31** resume los casos ya documentados en otros nodes (Ethos, Bowtie, Azos, Betterfly, Lemonade, Vitality).

| # | Programa | País · industria | Qué digitalizó | Población | Intervención | Mecanismo | Resultado y duración | Evidencia · fuente |
|---|---|---|---|---|---|---|---|---|
| 1 | Seguro de lluvia indexado | India · agro | Venta | Hogares rurales (Andhra Pradesh, Gujarat) | Aval de un agente local de confianza; descuentos; módulo educativo | Confianza delegada; precio | Compra de 5-10%. Aval: **+40%** de probabilidad de compra. −10% de precio → +10-12% de compra. Educación: poco efecto. Una temporada | RCT, arbitrado, tercero · F-847 |
| 2 | Seguro con prima a la cosecha | Kenia · agro | Cobro | Pequeños productores de caña | La compradora descuenta la prima a la cosecha | Descuento hiperbólico; liquidez | **72% vs 5%**; pagar un mes después: +21 pp. Un ciclo | RCT, arbitrado, tercero · F-848 |
| 3 | Sesiones de información sobre seguro de clima | China · agro | Venta | 5.335 hogares | Sesión intensiva; difusión por amigos | Conocimiento y red social | **+43%** de compra; un amigo informado ≈ bajar 13% la prima | RCT, arbitrado, tercero · F-849 |
| 4 | Seguro indexado (siete años) | India · agro | Renovación | Hogares del experimento | Observación de pagos propios y de vecinos | Disponibilidad; experiencia | La demanda sube tras un pago propio o vecino; el efecto vecinal se diluye | Panel de RCT, arbitrado · F-850 |
| 5 | Microseguro de vida con reembolso sin siniestro | **Perú** · rural | Venta y recompra | Beneficiarios del programa Juntos | Devolver parte de la prima si no hay siniestro | Aversión a perder la prima; confianza | Confianza ↑; tamaño no leído | Experimento de campo, documento de trabajo · F-853 |
| 6 | Microseguro de vida (Compartamos) | México · microfinanzas | Venta | 8.700 prestatarios | Quitar el subsidio; mensaje financiero vs. emocional | Precio; encuadre | Sin subsidio ↓ cobertura; mensajes sin efecto promedio | RCT, documento de trabajo · F-855 |
| 7 | Microseguro agrícola con crédito | Colombia · agro | Venta | Prestatarios agrícolas | Junto al crédito vs. después | Agrupación | Sin efecto en la compra total; bajo entendimiento del producto | RCT, arbitrado · F-854 |
| 8 | Seguro de salud nacional (NHIS) | Ghana · salud pública | Renovación | 57.993 afiliados | Pago por USSD/dinero móvil; SMS 1 mes y 2 semanas antes | Olvido, procrastinación | **+17,4 pp** de renovación; mayor en informales; un año | Cuasi-experimento, arbitrado, tercero · F-856. RCT sin resultados · F-857 |
| 9 | Freemium Tigo–MicroEnsure–Bima | Ghana, Tanzania · telco | Venta | Clientes prepago | Vida gratis ligada al gasto en minutos | Reciprocidad; fidelización del operador | >1 M cubiertos, 80% sin seguro previo; **churn sin cifra** | PR de ONG y operador · F-925, F-926 · ⚠️S |
| 10 | Linda Jamii | Kenia · M-Pesa | Cobro | Hogares | Plan de salud con cuotas por M-Pesa | Fraccionamiento | Meta 1 M en 2 años; 36.000 (otra fuente: 22.000); **cerrado en 2015** | Prensa · F-927 · fracaso documentado |
| 11 | MeBanbɔ (Hollard) | Ghana · USSD | Venta | Sin seguro previo | Micro-primas (GHS 2-50) con *269# | Ticket bajo; baja fricción | "Ha funcionado bien" (ejecutivo); sin persistencia | PR · F-928 · ⚠️S |
| 12 | Policybazaar | India · plataforma | Venta asistida | Ciudades de nivel 2 y 3 | Tiendas físicas y call center | "Reaseguro" presencial | Lo offline ≈30% de ventas en Bengala Occidental; utilidad del T2 FY26: ₹135 crore | PR y resultados · F-929, F-930 · ⚠️S |
| 13 | ZhongAn | China · aseguradora digital | Todo el ciclo | Ecosistemas de plataformas | Producto embebido | Conveniencia | 2025: primas RMB35,7 mil M; ratio combinado 95,8%; consumo −10,6%, salud +22,7% | Aviso a la bolsa · F-931 · ⚠️S |
| 14 | Previsul (Caixa) | Brasil · vida | Cotización | Vida individual | Bot en WhatsApp y Messenger; cotiza con la fecha de nacimiento | Baja fricción | **Sin resultados** | PR · F-933 |
| 15 | Tuio (Mapfre) | España · distribución | Venta | Digital | Asistente de IA | Conveniencia | >20% de clientes nuevos (autorreporte) | PR · F-932 · ⚠️S |
| 16 | **SOAT digital** | **Perú** · obligatorio | Venta | Dueños de vehículos | Compra en la web de la aseguradora; póliza registrada en APESEG | Estandarización; verificación | **9 de 10** digitales (2022); ~2.000 taxistas con SOAT falso | Gremio vía prensa · F-891, F-892 |
| 17 | Pacífico en Yape; Salud Yape | **Perú** · billetera | Cobro y venta | ~16 M usuarios activos | Pago de primas en "Yapear servicios"; plan desde S/9,90 con teleconsulta | Baja fricción; confianza en la billetera | **Meta 30.000 afiliados** (0,18%); sin resultados. Pacífico reporta 3,3 M clientes con seguros inclusivos (<S/40) en BCP, Mibanco y Yape | Autorreporte y prensa · F-912, F-913, F-915 · ⚠️S |
| 18 | Vida "100% online" con devolución | **Perú** · vida temporal | Venta | Urbano | Devuelve todo lo pagado si no hay siniestro | Aversión a perder la prima | Sin evaluación | Página comercial · F-922 |
| 19 | App Rímac; App Mapfre; Mi Espacio y VERA (Pacífico) | **Perú** · todos los ramos | Servicio y siniestro | Clientes | Asistencia vehicular, reembolsos, SOAT, pólizas, WhatsApp con autenticación; ruleta mensual (Rímac) | Conveniencia; recompensa variable | App Rímac: ~4,7/5 con ~23.000 calificaciones (iOS Perú). Uso real y resolución: **sin dato** | Fichas de tienda, PR · F-916 a F-919 |
| 20 | Pensión 65 | **Perú** · transferencias | Cobro | Mayores en pobreza extrema | Tarjeta de débito; tercero autorizado; pagadores móviles | Asistencia y confianza en familiares | >700.000 con tarjeta; 33.674 vía tercero | Entidad vía prensa · F-880 |
| 21 | Inscripción online a Medicare | EE.UU. · salud | Venta | Mayores de 65 | Plataforma de comparación | — | 22% online (4T-2018), 27% (2019) | PR · F-935 · ⚠️S |
| 22 | Recordatorios de ahorro | Filipinas, Bolivia, **Perú** · banca | Ahorro | Titulares con cuenta de meta | SMS (Filipinas, Bolivia) o carta (Perú) | Atención limitada | **+6%** de ahorro; +3 pp de meta; recordatorios repetidos sin efecto extra | RCT, arbitrado · F-859 |
| 23 | M-Pesa | Kenia · pagos | Pagos y ahorro | Hogares | Dinero móvil + red de agentes | Menor costo de enviar y ahorrar | ~2% de hogares fuera de la pobreza; más en mujeres | Cuasi-experimento, arbitrado · F-863 |
| 24 | Cuentas de ahorro gratuitas | Uganda, Malawi, **Chile** · banca | Cuentas | Sin cuenta | Cuenta sin costo | Acceso | 17%, 10% y **3%** con ≥5 depósitos; sin efecto en bienestar | RCT · F-861 |
| 25 | Crédito digital | Malawi · crédito | Crédito | Usuarios de una telco | Préstamo digital; educación por teléfono | Información | Conocimiento ↑; repago puntual no; **mora ↑** | RCT y regresión discontinua, arbitrado · F-862 |
| 26 | Educación financiera (meta-análisis) | 33 países | — | — | — | Conocimiento | Efectos medios positivos en 76 RCT | Meta-análisis, arbitrado · F-860 |
| 27 | CoDi | México · pagos QR | Pagos | Todos | Obligación a los bancos | — | 21,8 M cuentas validadas; **<2,5 M pagaron** | Opinión periodística · F-896 · fracaso |
| 28 | Pix | Brasil · pagos | Pagos | Todos | Banco central | — | 60+: 37% vs 71% (2021) | Encuesta vía prensa · F-894, F-895 |
| 29 | Intervenciones psicológicas breves | Educación en línea | Cursos | Estudiantes de países menos desarrollados | Mensajes de identidad social | Amenaza de identidad | Mejoran persistencia; "no hay bala de plata" | Experimentos de campo · F-864 |
| 30 | Elección activa de plan | EE.UU. · salud | Selección de plan | Empleados | Forzar la elección | Inercia | Mejora si los precios son fijos; **empeora la selección adversa** si se ajustan | Datos reales y modelo, arbitrado · F-858 |
| 31 | Ethos, Bowtie, Azos, Betterfly, Lemonade, Vitality | EE.UU., Hong Kong, Brasil, Chile | Varios | — | — | — | Ver los nodes de asesores y de vida en LatAm; Vitality: autorreporte (F-25) y un RCT de feedback con incentivo (F-442) | F-362 a F-379, F-25, F-353, F-442 |

**Competencia local, lo que se sabe (§3 del encargo, nivel micro).** Cuota de primas a junio de 2025: Rímac 27,4%, Pacífico 22,6%, Mapfre 13,5%, La Positiva 12,0% (F-911). Digital declarado:
- **Pacífico:** asistente VERA por web y WhatsApp con autenticación (F-916), app con siniestros, EPS y cartas de garantía (F-917), pago de primas en Yape y plan de salud en Yape (F-913, F-915), 3,3 M de clientes en seguros inclusivos (F-912).
- **Rímac:** app con clínicas, asistencia vehicular, reembolsos, programa de bienestar y ruleta (F-918); líder histórico de SOAT digital (F-923).
- **Mapfre:** app con asistencia vehicular, SOAT en 4 pasos y pólizas (F-919); el canal digital era ~7% de las ventas globales (2022) y en Perú la compra online era "reducida" (F-920); ratio combinado de Perú 102,4% en el 1T 2026 (F-505).
- **Banca:** Interseguro/Interbank: bancaseguros +98% en optativos (2023) y +18,9% (2025), vida "100% online" con devolución de prima (F-921, F-922); BCP: multa de Indecopi por fallas en seguros (F-889). **No se halló** información de La Positiva, Scotiabank ni BBVA.
- **Lo que no se pudo medir:** ventas digitales por aseguradora en 2025, resolución de siniestros en app, calidad real de cada experiencia (§G).

---

## 4. Matriz intervención × segmento

Leyenda: ✅ evidencia directa en seguros o microseguros (RCT o cuasi) · 🟨 evidencia indirecta (otra industria, encuesta o PR) · ⬜ sin evidencia (hipótesis) · ⚠️ riesgo documentado. **La mayoría de las celdas son 🟨 o ⬜: la matriz es un mapa de dónde probar, no un resultado.**

| Intervención | Joven urbano formal | Adulto 45-64 urbano formal | Mayor 65+ | Independiente o informal urbano con billetera | Rural o baja conectividad | Cliente de banco (bancaseguros) |
|---|---|---|---|---|---|---|
| **Aval de un tercero de confianza** (asesor, banco, agente local) | ⬜ | ⬜ | 🟨 familiar como aval (F-867, F-880) | ✅ en agro (F-847) | ✅ F-847; sesión con red F-849 | 🟨 72% / 9 de 10 (F-903) |
| **Cobro alineado al flujo de ingreso** (diferido, fraccionado, micro-prima) | ⬜ | ⬜ | ⬜ | ✅ en agro (F-848); 🟨 USSD (F-928) | ✅ F-848 | ⬜ |
| **Recordatorio + pago en un toque** | 🟨 (F-859) | 🟨 | ⬜ | ✅ Ghana, mayor en informales (F-856) | 🟨 carta en Perú (F-859) | 🟨 |
| **Reembolso sin siniestro** | ⬜ (F-922 sin evaluar) | ⬜ | ⬜ | 🟨 (F-853) | 🟨 (F-853) | ⬜ |
| **Sesión asistida o grupal con red social** | ⬜ | ⬜ | ⬜ | 🟨 | ✅ F-849 | ⬜ |
| **Cobertura gratuita ligada a otro servicio** | ⬜ | ⬜ | ⬜ | 🟨 alcance, sin conversión a pago (F-925) | 🟨 ⚠️ Linda Jamii (F-927) | ⬜ |
| **Renovación automática o elección por defecto** | ⬜ | ⚠️ selección adversa (F-858); cobros no pedidos (F-888, F-890) | ⚠️ | ⬜ | ⬜ | ⚠️ desgravamen (F-888) |
| **Asistente conversacional (WhatsApp/IA) con relevo humano** | 🟨 (F-932, F-933 PR) | ⬜ | ⚠️ 59% prefiere persona (F-898); 45% confía en IA para reclamar (F-901) | ⬜ | ⬜ | ⬜ ⚠️ escalar mal baja el NPS 11 puntos (F-183) |
| **Canal asistido** (tienda, call center, delegado autorizado) | ⬜ | 🟨 | 🟨 Pensión 65 (F-880); eHealth reconoce agente (F-935) | 🟨 | 🟨 Policybazaar (F-929) | 🟨 |
| **Siniestro digital de punta a punta con estado visible** | 🟨 mayor satisfacción (F-909) | 🟨 (F-909) | ⚠️ ~28% evitó reclamar (F-898) | ⬜ | ⬜ | ⬜ |

**Lectura.** Donde hay evidencia directa, es de **seguro agrícola indexado** (India, Kenia, China): se parece a vida o SOAT en el problema de confianza y liquidez, pero no en el riesgo ni en el pagador. Los segmentos "joven" y "adulto formal" casi no tienen evidencia propia en seguros: se asumen cómodos con lo digital, y eso **también es una hipótesis**.

---

## 5. Mapa de oportunidades priorizado

Impacto y facilidad son **juicios de diseño sobre la evidencia disponible**, no estimaciones cuantitativas. Evidencia: ✅ directa · 🟨 indirecta · ⬜ solo hipótesis.

### 5.1 Matriz impacto × facilidad (Perú)

| | **Facilidad alta** | **Facilidad media** | **Facilidad baja** |
|---|---|---|---|
| **Impacto alto** | **O1** Renovación y cobro por billetera con recordatorio · **O3** Aval del canal que ya tiene confianza | **O2** Prima alineada al ingreso del independiente · **O4** Siniestro con estado visible y humano a un toque · **O9** Segundo producto temprano · **O12** Medición por cohortes y canal | **O13** "Una sola puerta" de reclamo en bancaseguros |
| **Impacto medio** | **O5** Frontera de producto (qué va 100% digital) · **O7** Antifraude visible | **O6** Delegado autorizado para mayores · **O8** Devolución de prima, probada | **O11** Canal asistido rural |
| **Impacto bajo o incierto** | — | **O10** Seguro embebido en plataformas no financieras | — |

### 5.2 Detalle

| # | Oportunidad | Qué se hace | Evidencia | Por qué en Perú | Primer experimento (conducta real, no clics) | Riesgo |
|---|---|---|---|---|---|---|
| **O1** | Renovación y cobro por billetera | Recordatorio previo con enlace de pago en un toque (Yape/Plin) en seguros de ticket bajo o mensuales | 🟨 Ghana +17,4 pp cuasi (F-856); recordatorios +6% (F-859); un RCT en curso (F-857) | 52% hace pagos digitales; 42% tiene dinero móvil (F-875); Pacífico ya cobra en Yape (F-915) | RCT: recordatorio a 30 y 15 días **con** vs. **sin** enlace de pago; resultado: renovación a 90 días | Recordatorios repetidos no suman (F-859); cuidar spam (F-70, F-117) |
| **O2** | Prima alineada al ingreso | Cobro quincenal o ligado a ventas por QR para independientes | ✅ en agro (F-848); ⬜ en Perú | 70,7% de informalidad (F-878); microseguro con tope de S/30 al mes (F-883) | Dos brazos: mensual vs. quincenal con débito en billetera; resultado: pagos consecutivos | Necesita un pagador o canal que descuente; el cobro fraccionado encarece el costo operativo |
| **O3** | Aval del canal con confianza | Que el mensaje, el enlace o el QR lleve el nombre del asesor, el corredor o el banco que ya conoce el cliente | ✅ aval +40% (F-847); 🟨 72% (F-903) | En Perú la confianza sube con el corredor (nodes de comportamiento y de asesores) | A/B: el mismo mensaje enviado "por tu asesor X" vs. "por la aseguradora"; resultado: compra pagada | Responsabilidad difusa si algo falla (O13) |
| **O4** | Siniestro digital con humano a un toque | Estado del trámite siempre visible; botón "hablar con una persona" que conserva el contexto | 🟨 satisfacción mayor digital (F-909); fallas 33-39% y NPS −11 al escalar (F-183) | La falta de idoneidad del servicio concentra los reclamos ante Indecopi (F-888) | Medir recontacto a 14 días y reapertura, por tipo de siniestro | "Contención" inflada si se cuenta al que se rinde (F-910, opinión) |
| **O5** | Frontera de producto | Mantener 100% digital lo estandarizado y obligatorio (SOAT, viaje, accidentes, microseguros); en vida y salud complejos, digital asistido | ✅ SOAT 9/10 digital (F-891); Bain: 92% investiga, 25% compra 100% digital (F-182) | Ya está pasando; falta ordenarlo como política | Auditar qué productos hoy se fuerzan a digital sin que el cliente complete | — |
| **O6** | Delegado autorizado | Familiar o cuidador con permisos limitados (pagar, consultar, avisar un siniestro) con consentimiento del titular | 🟨 Pensión 65 con tercero (F-880); estudios de delegados (F-866) | Mayores con apoyo familiar; 27,8% de hogares con jefe de 60+ (F-877) | Piloto en renovación y aviso de siniestro; medir completitud | Compartir claves es la práctica actual y es un riesgo (F-866); datos personales |
| **O7** | Antifraude visible | Verificación de póliza con un toque; sello de canal oficial; aviso de suplantación | 🟨 ~2.000 taxistas afectados (F-892); mayores, blanco de estafas (F-894) | La compra digital crece al ritmo del fraude | Medir intención de compra y abandono con y sin verificación visible | Muestra el problema; ahuyenta si se exagera |
| **O8** | Devolución de prima | Probar si "te devolvemos lo pagado" sube compra y persistencia más de lo que cuesta | 🟨 confianza ↑ (F-853); ya existe en Interseguro (F-922) sin evaluación | La desconfianza nace de pagar y "no recibir nada" | Dos productos casi iguales, con y sin devolución; resultado: conversión y persistencia a 13 meses | Costo esperado alto; puede atraer a quien no se queda |
| **O9** | Segundo producto temprano | Ofrecer un microseguro complementario en los primeros 90 días | 🟨 retención 95% vs 83% con más productos (F-874); permanencia mayor con más productos (F-873) | Pacífico ya tiene 3,3 M con inclusivos (F-912) | Aleatorizar la oferta del segundo producto; medir persistencia del primero a 12 meses | La asociación puede ser selección, no causa |
| **O10** | Embebido en plataformas no financieras | Seguro en el flujo de compra o de movilidad | ⬜ (attach rates no verificados) | Plataformas con base grande | Piloto pequeño con medición de pago recurrente | Linda Jamii y Salud Yape: alcance no es compra (F-927, F-913) |
| **O11** | Canal asistido en zonas rurales | Agente, bodega o tienda que asiste una compra con billetera o USSD | 🟨 Policybazaar (F-929); Hollard USSD (F-928); ✅ agro con sesiones (F-849) | 23,4% de hogares rurales con internet; 88,4% de usuarios rurales accede por celular (F-876) | Piloto con agente de confianza; comparar con autoservicio | Costo por póliza; autoreporte de éxitos |
| **O12** | Sistema de medición | Experimentos con uplift y cohortes por canal desde el primer día | — | La mayor laguna es dato propio de persistencia y recontacto | Crear el panel de cohortes (§F) | Medir "clics" en vez de conducta |
| **O13** | "Una sola puerta" en bancaseguros | El banco canaliza y muestra el estado; la aseguradora resuelve | 🟨 Argentina ya canaliza el reclamo por el banco (F-905); sanciones y reclamos separados (F-889, F-890) | Desgravamen y cobros indebidos concentran quejas (F-888) | Medir tiempo de resolución y reclamos repetidos | Requiere acuerdo con bancos |

### 5.3 Principios estructurales para la estrategia (inferencia a partir de lo anterior)

1. **Digitalizar el evento, no al cliente.** En productos de pocos toques el éxito se mide cuando ocurre un evento (compra, renovación, siniestro), no con frecuencia de uso.
2. **Segmentar por quién avala y cómo entra el dinero** antes que por edad.
3. **"Digital con humano a un toque"** como estándar de diseño, con costo y NPS medidos del escalamiento.
4. **Experimentar antes de forzar.** Ninguna migración forzada sin un grupo de control y una medida de abandono inducido.
5. **Cuidar la responsabilidad en canales intermediados** (banco, asesor, plataforma): un reclamo debe tener un dueño visible.
6. **Antifraude como parte del producto**, no como aviso legal.
7. **Medir conducta y persistencia por cohortes y canal desde el día uno**, porque hoy el mercado no tiene dato público.

---

## 6. Lagunas de información

1. **Persistencia o caducidad por canal (digital vs. asesor vs. banco) en Perú y LatAm:** no hay dato público; solo India, Australia y Reino Unido, con resultados opuestos (F-870, F-871, F-872).
2. **A quién culpa el cliente de bancaseguros en un siniestro (banco o aseguradora):** ningún estudio; solo normas y casos (F-905, F-906, F-889).
3. **Abandono de onboarding en seguros en LatAm:** ninguna fuente primaria. La cifra "70% abandona" que circula viene de un blog sin fuente (F-893) y **se descartó**.
4. **Ventas digitales por aseguradora en Perú 2025** (Rímac, Pacífico, Mapfre, La Positiva): no se hallaron; solo cifras antiguas (F-920, F-923) o parciales (F-921).
5. **Funcionalidades reales de los competidores:** no se probaron las apps; no se halló información de La Positiva ni de bancos distintos de Interbank. Un dato que circula sobre el rating de las apps de seguros (3,7) frente a las de banca (4,5) **no se pudo verificar** y no se usa.
6. **Resultados de Salud Yape** más allá de la meta (F-913), y qué parte de los seguros inclusivos de Pacífico se vende por Yape (F-912).
7. **Microseguros en Perú, cifras 2024-2025:** no se hallaron; el diagnóstico del PNUD de marzo de 2026 aparece listado pero no se leyó.
8. **Encuesta SBS 2023 por edad y canal:** no se pudo abrir. Además, una nota dice "3 de cada 10" tienen seguro (F-885) y el ledger ya traía "~4 de cada 10" (F-1): **contradicción sin reconciliar**.
9. **Mayores y seguros en LatAm:** no hay evidencia. Tampoco el corte por edad del Global Findex 2025 para Perú (F-875).
10. **Pista social:** sin Reddit, X ni TikTok. Un caso viral hallado (Rímac y la novia, F-897) es campaña de marca, no validación de la oferta digital.
11. **Educación financiera:** el meta-análisis (F-860) y los RCT de seguros y crédito (F-847, F-852, F-862) no coinciden; no se pudo explicar la diferencia (¿contenido, población, resultado medido?).
12. **Estudios no verificados:** una reseña de Science sobre asesoría agrícola digital (Fabregas, Kremer y Schilbach, 2019) **no se pudo confirmar** y no se usa; tampoco el "94% de recompra" atribuido a Dixon et al. (F-865).
13. **Ensayos sin resultados:** ReachUHC (F-857), Banking for Boomers (F-868), THRIFT (F-869).
14. **Sesgo de supervivencia:** dominan los casos con éxito publicado (Policybazaar, ZhongAn, Azos, Tuio, Tigo). Los fracasos hallados son pocos (Linda Jamii, Betterfly, CoDi); casi seguro hay más sin documentar.
15. **Transferencia desde agro:** la evidencia causal más fuerte es de seguro agrícola indexado; no se sabe cuánto se traslada a vida, salud o SOAT.
16. **Sudeste Asiático y embebido:** no hay tasas de adjunción verificables (Gojek, Grab); lo hallado es un panel de demostración sin fuente.
17. **Idioma y lenguas originarias, plan de datos limitado y dispositivo compartido:** posibles barreras, sin evidencia hallada.
18. **Datos internos de la aseguradora:** sin acceso; las tres definiciones basales quedan como criterios.

---

## 7. Ledger de fuentes

**Cómo leer.** El ledger completo (resumen de cada fuente, caveats y rigor detallado) está en `research/fuentes/codice.md`, filas F-847 a F-940. Aquí solo va la referencia. **Todas se leyeron por resumen de búsqueda; ninguna se abrió completa.** Rigor A-E según la rúbrica del ledger.

**Fuentes ya existentes en el ledger que este node reutiliza:** F-1 (SBS 2023), F-3 (sesgos y educación financiera), F-4, F-182, F-183 (Bain), F-9 y F-6 (comprensión y divulgación), F-25 y F-353 (Vitality), F-70 y F-117 (Indecopi, spam), F-180 (Cummins y Doherty), F-362 a F-379 (Ethos, Bowtie, Azos, Betterfly, Mapfre, McKinsey), F-442 (RCT de seguro por uso), F-482, F-485, F-486, F-504 a F-507, F-529 y F-805 a F-808.

### 🔬 Pista empírica y datos oficiales (41)
- **F-847** · Cole, S.; Giné, X.; Tobacman, J.; Topalova, P.; Townsend, R.; Vickery, J. (2013). *Barriers to Household Risk Management: Evidence from India (American Economic Journal: Applied Economics 5(1))*. 🟢 A. <https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr373.html>
- **F-848** · Casaburi, L. & Willis, J. (2018). *Time vs. State in Insurance: Experimental Evidence from Contract Farming in Kenya (American Economic Review)*. 🟢 A. <https://www.atai-research.org/wp-content/uploads/2017/08/aer.20171526.pdf>
- **F-849** · Cai, J.; de Janvry, A.; Sadoulet, E. (2015). *Social Networks and the Decision to Insure (American Economic Journal: Applied Economics 7(2):81-108)*. 🟢 A. <https://www.povertyactionlab.org/media/file-research-paper/social-networks-and-decision-insure>
- **F-850** · Cole, S.; Stein, D.; Tobacman, J. (2014). *Dynamics of Demand for Index Insurance: Evidence from a Long-Run Field Experiment (American Economic Review: Papers & Proceedings 104(5):284-290)*. 🟢 A. <https://ideas.repec.org/a/aea/aecrev/v104y2014i5p284-90.html>
- **F-851** · Cai, H.; Chen, Y.; Fang, H.; Zhou, L. (s.f. (NBER w15396; la versión publicada es posterior y no se verificó)). *Microinsurance, Trust and Economic Development: Evidence from a Randomized Natural Field Experiment*. 🟢 A. <https://nber.org/system/files/working_papers/w15396/w15396.pdf>
- **F-852** · Dercon, S.; Gunning, J. W.; Zeitlin, A. (s.f. (documento de trabajo, conferencia NBER)). *The demand for insurance under limited trust: Evidence from a field experiment in Kenya*. 🟡 C. <https://conference.nber.org/conf_papers/f81607/f81607.pdf>
- **F-853** · Galarza, F. & Outes, I. (Universidad del Pacífico) (2016). *Do you want some cash-back? Assessing the demand for a no-claim rebate life-insurance product (documento de trabajo DD/16-04)*. 🟡 C. <https://ideas.repec.org/p/pai/wpaper/16-04.html>
- **F-854** · Bauchet, J.; Damon, A.; Larsen, A. (2017). *RCT de microseguro agrícola ofrecido junto con la solicitud de crédito o por separado, Colombia (Journal of Development Effectiveness 9(4):443-461; título exacto no verificado)*. 🟢 A. <https://ideas.repec.org/a/taf/jdevef/v9y2017i4p443-461.html>
- **F-855** · Bauchet, J. (2012). *Experimento con 8.700 prestatarios de Compartamos sobre precio e información en microseguro de vida (México) — documento de trabajo*. 🟡 C. <https://www.financialaccess.org/publications-index/tag/Mexico>
- **F-856** · Nsiah-Boateng, E. y colegas (2023). *Effect of mobile phone-based health insurance contribution payment system on retention of coverage in the National Health Insurance Scheme in Ghana (BMC Health Services Research)*. 🟢 A. <https://doaj.org/article/98c2d97968f14405be3b04da48cdf9ba>
- **F-857** · Equipo ReachUHC (Kumasi, Ghana) (2024-2025). *ReachUHC: protocolo de un RCT de recordatorios por celular y renovación automática (medRxiv 2024; Trials)*. 🟡 C. <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12720431/>
- **F-858** · Handel, B. (2013). *Adverse Selection and Inertia in Health Insurance Markets: When Nudging Hurts (American Economic Review 103(7))*. 🟢 A. <https://www.nber.org/papers/w17459>
- **F-859** · Karlan, D.; McConnell, M.; Mullainathan, S.; Zinman, J. (2016). *Getting to the Top of Mind: How Reminders Increase Saving (Management Science 62(12):3393-3411)*. 🟢 A. <https://img.nber.org/papers/w16205>
- **F-860** · Kaiser, T.; Lusardi, A.; Menkhoff, L.; Urban, C. (2022). *Financial education affects financial knowledge and downstream behaviors (Journal of Financial Economics 145(2A); NBER w27057)*. 🟢 A. <https://www.nber.org/papers/w27057.pdf>
- **F-861** · Dupas, P.; Karlan, D.; Robinson, J.; Ubfal, D. (2016-2018 (NBER w22463; la versión publicada se asume posterior, no se verificó)). *Banking the Unbanked? Evidence from Three Countries*. 🟢 A. <https://nber.org/system/files/working_papers/w22463/w22463.pdf>
- **F-862** · Brailovskaya, V.; Dupas, P.; Robinson, J. (2024). *Is Digital Credit Filling a Hole or Digging a Hole? Evidence from Malawi (The Economic Journal 134(658):457-484)*. 🟢 A. <https://ideas.repec.org/a/oup/econjl/v134y2024i658p457-484..html>
- **F-863** · Suri, T. & Jack, W. (2016). *The long-run poverty and gender impacts of mobile money (Science 354(6317):1288-1292)*. 🟢 A. <https://www.findevgateway.org/paper/2016/12/long-run-poverty-and-gender-impacts-mobile-money>
- **F-864** · Kizilcec, R.; Saltarelli, A.; Reich, J.; Cohen, G. (2017). *Closing global achievement gaps in MOOCs (Science 355:251-252)*. 🟢 A. <https://news.mit.edu/2017/small-interventions-big-effects-closing-mooc-achievement-gap-0131>
- **F-865** · Dixon, M.; Freeman, K.; Toman, N. (2010). *Stop Trying to Delight Your Customers (Harvard Business Review, jul-2010)*. 🟡 C. <https://store.hbr.org/product/stop-trying-to-delight-your-customers/R1007L?searchid=0>
- **F-866** · Manitoba HCI Lab (CHI 2022) y Soubutts, E. y colegas (UCL, CHI 2025) (2022 y 2025). *Unofficial proxies: how close others help older adults with banking / Navigating Technology Support for Older Adults' Banking Activities with Close Others*. 🟡 C. <https://hci.cs.umanitoba.ca/publications/details/unofficial-proxies-how-close-others-help-older-adults-with-banking>
- **F-867** · Universidad de Jyväskylä (tesis de maestría) (2024). *Exploring the factors influencing UPI adoption among senior citizens in India*. 🟡 C. <https://jyx.jyu.fi/jyx/Record/jyx_123456789_95943>
- **F-868** · Universidad de Mainz (documento de discusión 2505) (2025). *Banking for Boomers (RCT con 333 clientes de una caja de ahorros alemana)*. 🟡 C. <https://download.uni-mainz.de/RePEc/pdf/Discussion_Paper_2505.pdf>
- **F-869** · Registro de ensayos (NCT05510687), THRIFT Bangladesh (s.f.). *Ensayo aleatorizado: lentes de lectura + capacitación en banca móvil a beneficiarios mayores de pensiones*. 🔵 B. <https://tundraspace.com/directory/studies/nct05510687>
- **F-870** · IRDAI (regulador de seguros de India) vía Café Mutual (s.f.). *Products bought online show significantly higher persistency than those sold through agents*. 🟠 D. <https://cafemutual.com/news/insurance/39099-products-bought-online-show-significantly-higher-persistency-than-those-sold-through-agents>
- **F-871** · Plan For Life (vía Riskinfo, Australia) (2015). *Direct Insurance Sales Fall*. 🟠 D. <https://riskinfo.com.au/news/2015/04/30/direct-insurance-sales-fall>
- **F-872** · FSA (regulador del Reino Unido) vía Professional Adviser (s.f. (antigua)). *FSA finds product lapse rates lower among IFAs*. 🟠 D. <https://professionaladviser.com/news/2243495/fsa-product-lapse-rates-lower-ifas>
- **F-873** · Universidad EAFIT (repositorio; datos de una aseguradora latinoamericana) (2020). *Customer churn prediction in insurance industries: a multiproduct approach*. 🟡 C. <https://repository.eafit.edu.co/items/5b1924c0-c24a-47de-8317-b0ca300f415d>
- **F-875** · Banco Mundial Global Findex 2025, vía IEP (Instituto de Estudios Peruanos) (2025). *Perú 2024: cuentas, dinero móvil y pagos digitales (documento Ge080925_16)*. 🔵 B. <https://iep.org.pe/wp-content/uploads/2025/09/Ge080925_16.pdf>
- **F-876** · INEI (vía El Peruano) (2026). *Estadísticas de las TIC en los hogares, IV trimestre 2025*. 🔵 B. <https://elperuano.pe/noticia/292141-lima-metropolitana-el-984-de-hogares-conto-con-telefonia-movil-durante-cuarto-trimestre-de-2025>
- **F-877** · INEI (vía Forbes Perú) (2024). *Sube a 47% el porcentaje de personas mayores de 60 años que usan internet*. 🔵 B. <https://forbes.pe/tecnologia/2024-10-01/sube-a-47-el-porcentaje-de-personas-mayores-de-60-anos-que-usan-internet-en-peru/>
- **F-878** · INEI (vía Infomercado y Expreso) (2025-2026). *Informalidad laboral en el Perú: 70,7% de la población ocupada en 2025*. 🔵 B. <https://infomercado.pe/informalidad-laboral-en-peru-llega-al-70-segun-el-inei/>
- **F-879** · Horizonte Laboral (vía La República) (2025). *El EsSalud que hereda Fujimori: indicadores*. 🟠 D. <https://www.larepublica.co/globoeconomia/el-essalud-que-hereda-fujimori-los-indicadores-que-enfrentan-los-pacientes-en-peru-4449874>
- **F-880** · Midis / Banco de la Nación (vía La República y Caretas) (2026). *Pensión 65: pago a más de 824.000 adultos mayores*. 🟠 D. <https://larepublica.pe/sociedad/2026/08/03/ya-empezo-el-pago-de-pension-65-a-mas-de-824000-adultos-mayores-asi-puedes-cobrar-en-agosto-el-subsidio-de-s350-del-estado-147039>
- **F-881** · EsSalud (2026). *Boletín de Telesalud, enero 2026*. 🔵 B. <https://cdn.www.gob.pe/uploads/document/file/9493036/7715225-boletin-de-telesalud-enero-2026.pdf>
- **F-882** · PUCP (tesis) (s.f.). *Uso de billeteras digitales en la generación de adultos mayores de Lima Metropolitana*. 🟡 C. <https://tesis.pucp.edu.pe/repositorio//handle/20.500.12404/22999>
- **F-883** · SBS (Res. 01438-2024), vía Andina y Gestión (2024). *SBS modificó el Reglamento de Pólizas de Microseguros*. 🔵 B. <https://andina.pe/agencia/noticia-sbs-modifico-reglamento-polizas-microseguros-982868.aspx>
- **F-884** · SBS (vía Andina) (2016 (dato); nota posterior). *¿Cuántos peruanos y mypes tienen un microseguro en el Perú?*. 🔵 B. <https://andina.pe/ingles/noticia-cuantos-peruanos-y-mypes-tienen-un-microseguro-el-peru-688889.aspx>
- **F-885** · Perú21 (cita a la SBS) (2024). *Las nuevas alternativas para vivir seguros*. 🟠 D. <https://peru21.pe/economia/las-nuevas-alternativas-para-vivir-seguros/>
- **F-886** · BID (s.f.). *Research Insights: How Can Digital Payments Drive Financial Inclusion in Latin America and the Caribbean*. 🔵 B. <https://publications.iadb.org/publications/english/document/Research-Insights-How-Can-Digital-Payments-Drive-Financial-Inclusion-in-Latin-America-and-the-Caribbean.pdf>
- **F-902** · de Andrés-Sánchez, J. & Gené-Albesa, J. (2024). *Aceptación de chatbots por asegurados (Humanities & Social Sciences Communications)*. 🟢 A. <https://doaj.org/article/90ae44fac45f4aceb6c8200df5cd99c8>
- **F-908** · Autores no verificados (revista ILR vol. 7 n.º 2, Universidad Islámica Internacional de Islamabad; nombre completo de la revista no verificado) (2024). *Artículo sobre bancaseguros y venta indebida en Pakistán (título exacto no verificado)*. 🟡 C. <https://iiu.edu.pk/wp-content/uploads/2024/05/ILR-Vol-7-Issue-2-Article-1-210524.pdf>

### 📱 Pista social y mediática (12)
- **F-887** · Edelman (2026). *Edelman Trust Barometer 2026 — Perú (Top 10)*. 🟡 C. <https://www.edelman.com/sites/g/files/aatuss191/files/lat/2026-03/ETB%202026_Top10%20PER%20ESP.pdf>
- **F-888** · Andina / Infomercado / Congreso de la República (Comisión de Defensa del Consumidor) (2022). *Indecopi impuso 1.408 sanciones a 26 empresas del sector Seguros; conversatorio sobre desgravamen*. 🟠 D. <https://andina.pe/agencia/noticia-indecopi-impuso-1408-sanciones-a-26-empresas-del-sector-seguros-896401.aspx>
- **F-889** · Expreso (s.f. (año no verificado)). *Indecopi sanciona a BCP por fallas en seguros; también hay irregularidades en seguridad digital*. 🟠 D. <https://www.expreso.com.pe/economia/indecopi-sanciona-a-bcp-por-fallas-en-seguros-tambien-hay-irregularidades-en-seguridad-digital-spc-noticia/1227671/>
- **F-890** · La República (2023). *Denuncian que Caja Piura y Mapfre buscan no pagar seguro de desgravamen*. 🟠 D. <https://larepublica.pe/economia/2023/10/29/denuncian-que-caja-piura-y-mapfre-buscan-no-pagar-seguro-de-desgravamen-2020653>
- **F-892** · APESEG (vía Andina y Panamericana) (2022). *¿Estás a punto de adquirir un SOAT? Conoce cómo evitar estafas*. 🟠 D. <https://andina.pe/agencia/noticia-estas-a-punto-adquirir-un-soat-conoce-como-evitar-estafas-908262.aspx>
- **F-893** · Sovos (proveedor de cumplimiento) con cita a la Asociación Fintech del Perú (s.f.). *Onboarding en servicios financieros: los errores que cuestan clientes*. 🔴 E. <https://sovos.com/es/blog/iva/onboarding-servicios-financieros-errores-soluciones/>
- **F-894** · Tecnoblog (cita el Radar Febraban) (2021). *Idosos têm menor confiança no Pix e são maior alvo de golpes financeiros*. 🟠 D. <https://tecnoblog.net/noticias/idosos-tem-menor-confianca-no-pix-e-sao-maior-alvo-de-golpes-financeiros/>
- **F-896** · DPL News (2025). *¿Por qué fracasó CoDi?*. 🟠 D. <https://dplnews.com/por-que-fracaso-codi-pagos-qr-mexico/>
- **F-897** · Mercado Negro (2023 (inferido)). *Novia se queda varada en Larcomar: así fue la campaña de Rímac Seguros*. 🟠 D. <https://www.mercadonegro.pe/publicidad/novia-se-queda-varada-en-larcomar-asi-fue-la-campana-de-rimac-seguros/>
- **F-905** · SSN (Superintendencia de Seguros de la Nación, Argentina) (2021). *Resolución 822/2021*. 🔵 B. <https://100seguro.com.ar/wp-content/uploads/2021/12/RES_SSN_822_2021-1.pdf>
- **F-906** · Insurance Business Asia (2025-2026). *Joint liability ruling puts India's bancassurance distribution under scrutiny*. 🟠 D. <https://www.insurancebusinessmag.com/asia/news/breaking-news/joint-liability-ruling-puts-indias-bancassurance-distribution-under-scrutiny-589202.aspx>
- **F-907** · VietnamNet (2025). *Investigation into bancassurance's wrongdoings*. 🟠 D. <https://vietnamnet.vn/en/investigation-into-bancassurance-s-wrongdoings-to-conclude-by-end-of-july-pm-2171581.html>

### 💼 Pista de negocio e industria (41)
- **F-874** · J.D. Power (vía Insurance Canada) (2009 (y estudios afines 2007-2012)). *Customer retention is critical for insurance carriers*. 🟡 C. <https://insurance-canada.ca/2009/04/22/j-d-power-and-associates-reports-customer-retention-is-critical-for-insurance-carriers-particularly-among-those-customers-potentially-impacted-by-challenging-economic-conditions/>
- **F-891** · APESEG (vía Andina) (2022). *Nueve de cada diez SOAT emitidos son digitales*. 🟠 D. <https://andina.pe/agencia/noticia-apeseg-nueve-cada-diez-soat-emitidos-son-digitales-898358.aspx>
- **F-895** · Capco (con datos del Banco Central de Brasil) (2021). *PIX no Brasil*. 🟡 C. <https://www.capco.com/-/media/CapcoMedia/Subfolder-Unsorted/Capco-2/PDFs/PIX-No-Brasil.ashx>
- **F-898** · Insurity (proveedor de software; encuesta propia) (2025). *Digital Experience Index: digital fatigue among Baby Boomers*. 🟡 C. <https://www.businesswire.com/news/home/20250724865185/en>
- **F-899** · KPMG Reino Unido (2026). *Consumers want humans managing insurance claims*. 🟡 C. <https://kpmg.com/uk/en/media/press-releases/2026/04/consumers-want-humans-managing-insurance-claims.html>
- **F-900** · Accenture (vía Canadian Underwriter e Insurance Canada) (2013). *Customers' age not necessarily best indication of how they want insurance quotes*. 🟡 C. <https://www.canadianunderwriter.ca/insurance/customers-age-not-necessarily-best-indication-of-how-they-want-insurance-quotes-survey>
- **F-901** · Hi Marley (vía Insurance Business) (2026). *Insurers are bullish on AI, but policyholders want a human on standby*. 🟡 C. <https://www.insurancebusinessmag.com/ca/news/cyber/insurers-are-bullish-on-ai-but-policyholders-want-a-human-on-standby--study-591160.aspx>
- **F-903** · McKinsey (Encuesta de Bancaseguros Latinoamericano), vía Portafolio (s.f. (año de la encuesta no verificado)). *Bancaseguros para reducir brechas*. 🟡 C. <https://www.portafolio.co/opinion/analisis/bancaseguros-para-reducir-brechas-618345>
- **F-904** · McKinsey (2025). *Informe Global de Seguros 2025: en busca del crecimiento en América Latina (versión en español)*. 🟡 C. <https://www.mckinsey.com/locations/south-america/latam/hispanoamerica-en-potencia/informe-global-de-seguros-2025-en-busca-del-crecimiento-en-america-latina/es-CL>
- **F-909** · J.D. Power (2021-2025). *US Claims Digital Experience Study (varias ediciones)*. 🟡 C. <https://www.insurancebusinessmag.com/us/news/claims/digitalonly-claims-journey-delivers-highest-satisfaction-j-d--power-finds-560443.aspx>
- **F-910** · CustomerThink (blog de experiencia de cliente) (s.f.). *Beware of Silent Sufferers! First Contact and Digital Containment Rates are Worse than You Think*. 🔴 E. <https://customerthink.com/?p=1072782>
- **F-911** · PCR (Pacific Credit Rating) (2025). *Perú: Sector Seguros*. 🟡 C. <https://ww3.ratingspcr.com/peru-sector-seguros/>
- **F-912** · Credicorp (resultados 1T25 y cobertura de la llamada del 4T25) (2025-2026). *Resultados: Pacífico, seguros inclusivos y Yape*. 🔵 B. <https://finance.yahoo.com/news/credicorp-q4-earnings-call-highlights-162218758.html>
- **F-913** · Descubre / Gestión (2025). *Yape lanzará seguro de salud con Pacífico Salud para 30.000 usuarios*. 🟠 D. <https://www.descubre.vc/noticia/yape-lanzar-seguro-de-salud-con-pac-fico-salud-para-30-000-usuarios-2025-06-24>
- **F-914** · Diario Correo / Trome (publirreportaje) (2025). *Atenciones médicas en línea con Seguro de Salud Yape*. 🔴 E. <https://diariocorreo.pe/publireportaje/atenciones-medicas-en-linea-con-seguro-de-salud-yape-noticia/>
- **F-915** · Revista Economía (s.f.). *Pacífico: ahora puedes pagar tus seguros por Yape*. 🟠 D. <https://www.revistaeconomia.com/pacifico-ahora-puedes-pagar-tus-seguros-por-yape/>
- **F-916** · Pacífico Seguros (s.f.). *Términos y condiciones del asistente virtual VERA*. 🟠 D. <https://www.pacifico.com.pe/documents/28730/209427323/tyc+vera.pdf/1821cc3b-281c-2f65-cbc4-244e17a795e9>
- **F-917** · Apple App Store (ficha de 'Mi Espacio Pacífico') (s.f.). *Mi Espacio Pacífico*. 🟠 D. <https://apps.apple.com/us/app/-/id1469237859>
- **F-918** · Apple App Store Perú (ficha de 'App Rímac') (s.f.). *App Rímac*. 🟠 D. <https://apps.apple.com/pe/app/app-rimac/id602975058>
- **F-919** · Google Play (ficha de 'App Mapfre Perú') (s.f.). *App Mapfre Perú*. 🟠 D. <https://play.google.com/store/apps/details?id=com.mapfreperu.appmapfre&hl=en_US>
- **F-920** · Forbes Perú (entrevista al CEO global de Mapfre) y Gestión (2022). *CEO global de Mapfre: asegurar las cosechas...; los nuevos tipos de seguro por los que apuesta Mapfre*. 🟠 D. <https://forbes.pe/editors-pick/2022-08-16/ceo-global-de-mapfre-asegurar-las-cosechas-contra-las-consecuencias-del-cambio-climatico-es-una-necesidad/>
- **F-921** · Interseguro (memorias anuales 2023 y 2025) y Forbes Perú (2022-2026). *Memoria Anual 2025; Memoria 2023; 'Interseguro proyecta crecimiento de doble dígito y mayores ventas en su canal digital'*. 🟡 C. <https://www.interseguro.pe/wp-content/uploads/2026/04/Memoria-Anual-2025-Revisado-EY-VF.18.03.26.pdf>
- **F-922** · Interseguro (s.f.). *Seguro de vida Interbank (página comercial)*. 🟠 D. <https://www.interseguro.pe/seguro-de-vida/interbank/>
- **F-923** · Mercado Negro y Rímac (reporte de sostenibilidad 2018) (2018-2019). *Rímac en SOAT digital y marketing digital*. 🟠 D. <https://www.mercadonegro.pe/digital/rimac-seguros-se-corona-como-anunciante-del-ano-en-los-premios-iab-mixx-2019>
- **F-924** · Chubb Perú (s.f.). *Formato de solicitud (Chubb Studio)*. 🟠 D. <https://chubb.com/content/dam/chubb-sites/chubb/latam/pe-es/pdfs/chubb-studio-solicitud.pdf>
- **F-925** · GSMA Mobile for Development y Opportunity International (2012-2013). *Tigo, Bima and MicroEnsure bring a 'Freemium' model to mobile insurance (Ghana)*. 🟠 D. <https://www.gsma.com/mobilefordevelopment/country/ghana/tigo-bima-and-microensure-bring-a-freemium-model-to-mobile-insurance/>
- **F-926** · CGAP (s.f.). *Can Phones Drive Insurance Markets? Initial Results From Ghana*. 🔵 B. <https://cgap.org/node/2224>
- **F-927** · Business Daily Africa / Standard Media / NextBillion (2014-2015). *Linda Jamii (Safaricom, Britam y Changamka)*. 🟠 D. <https://www.businessdailyafrica.com/bd/corporate/companies/safaricom-s-linda-jamii-cover-to-now-target-smes--2071408>
- **F-928** · Hollard Ghana y Citi Newsroom (2022-2024). *Hollard Life MeBanbɔ ya está disponible en MTN MoMo*. 🟠 D. <https://www.hollard.com.gh/media-centre/press-releases/hollard-life-mebanbo-is-now-available-on-mtn-momo>
- **F-929** · Business Standard, BusinessWorld y prensa de negocios india (2025). *Policybazaar reporta 60% de crecimiento offline en Bengala Occidental; tiendas físicas*. 🟠 D. <https://www.business-standard.com/amp/industry/news/policybazaar-reports-60-offline-growth-in-west-bengal-insurance-sales-125091000964_1.html>
- **F-930** · Medianama, Entrackr, Inc42 (resultados de PB Fintech) (2025-2026). *PB Fintech: resultados del año fiscal 2026*. 🟠 D. <https://www.medianama.com/2025/10/223-policybazaar-pb-fintech-165-yoy-profit-q2fy26-135-cr-insurance-premiums/>
- **F-931** · ZhongAn Online (aviso a la bolsa de Hong Kong) (2026). *Resultados anuales 2025*. 🔵 B. <https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0319/2026031900592.pdf>
- **F-932** · Fintech Global / La República (2026). *Mapfre adquiere 38,9% de la insurtech Tuio*. 🟠 D. <https://fintech.global/2026/07/31/mapfre-acquires-38-9-stake-in-insurtech-tuio/>
- **F-933** · Baguete y Revista Apólice (2020). *Previsul vende online con O2OBOTS*. 🟠 D. <https://www.baguete.com.br/noticias/previsul-vende-on-line-com-o2obots>
- **F-934** · Cover (Sudáfrica) (2026). *Metropolitan closes the coverage gap with a new No-Lapse Funeral Growth Plan*. 🟠 D. <https://www.cover.co.za/news/metropolitan-closes-the-coverage-gap-for-millions-of-south-africans-with-new-no-lapse-funeral-growth-plan>
- **F-935** · Fierce Healthcare (cita a eHealth) y memoria anual 2019 de eHealth (2019-2020). *eHealth's online Medicare enrollment up 69% in Q4 2018*. 🟡 C. <https://www.fiercehealthcare.com/payer/online-medicare-enrollment-up-69-q4-2018>
- **F-936** · GSMA Mobile for Development (s.f.). *Growing agri insurance: ACRE Africa's experience of innovative partnerships*. 🟡 C. <https://www.gsma.com/mobilefordevelopment/africa/growing-agri-insurance-acre-africas-experience-of-innovative-partnerships/>
- **F-937** · InfoMoney (datos de la Susep) (2024). *Open Insurance: 16,5 millones de transacciones (sep-2023 a sep-2024)*. 🟠 D. <https://www.infomoney.com.br/?p=2632217>
- **F-938** · CNseg (vía Monitor Mercantil) (s.f. (año no claro)). *Cancelamento do seguro de vida atinge mínima histórica*. 🟠 D. <https://monitormercantil.com.br/cancelamento-do-seguro-de-vida-atinge-minima-historica-em-agosto/>
- **F-939** · Chubb Latinoamérica (blog) (s.f.). *Comercialización de seguros: múltiples canales*. 🟠 D. <https://www.chubb.com/latammarketing/bloglatam/comercializacion-de-seguros-multiples-canales.html>
- **F-940** · Portafolio (Colombia) (2017). *Los microseguros cubren al 8,1% de la población latina*. 🟠 D. <https://www.portafolio.co/economia/finanzas/los-microseguros-cubren-al-8-1-de-la-poblacion-latina-516287>

---

# ANEXOS ANALÍTICOS (respuestas por pregunta)

## A. Estrategia de digitalización: qué, por qué canal y para qué

### A.1 Qué se digitaliza y cómo (nivel macro y meso)

| Etapa | Canales vistos | Objetivo declarado | Resultado medido | Brecha entre ambos | Fuentes |
|---|---|---|---|---|---|
| **Venta** | App, web, WhatsApp, embebido en billeteras o plataformas, corredores digitales, asistentes de IA | Inclusión y penetración | Crecimiento de la plataforma o del canal (Policybazaar, ZhongAn, Azos); en Perú, **penetración estable en 2,0-2,1%** (F-507) | Escala del canal ≠ más gente asegurada | F-929, F-931, F-507, F-377 |
| **Cobro y renovación** | Dinero móvil, USSD, SMS, billetera | Reducir caducidad | Ghana +17,4 pp (cuasi) | Es de las pocas medidas con control | F-856 |
| **Siniestro** | App, WhatsApp, asistente | Rapidez y satisfacción | Satisfacción mayor si todo es digital (EE.UU.); fallas de 33-39% y NPS −11 al escalar | La satisfacción promedia a quien completa; la falla mide a quien no | F-909, F-183 |
| **Servicio** | Asistentes, apps | Reducir llamadas | Sin dato público en Perú | — | F-916, F-917 |
| **Cobranza masiva por banco** | Débito automático | Escala | Reclamos por cobros indebidos y desafiliación pendiente | La cobranza se digitalizó; el consentimiento no | F-888 |

**Distribución en LatAm.** Corredores y agentes concentran 60-65% de las primas y bancaseguros hasta 80% en vida y pensiones en Brasil (F-375, F-904). El financiamiento insurtech de la región fue USD 199 M en 2025 (F-374). En Perú, los microseguros son pequeños frente al mercado (S/126 M de primas en 2022 contra S/24.034 M de primas netas totales en 2025; años distintos, **menos de 1%**, cálculo propio aproximado; F-884, F-482).

**Fracasos documentados.** Linda Jamii (Kenia): meta de 1 M, 36.000 y cierre en un año (F-927). Betterfly (Chile): cierre en cinco países (F-372). CoDi (México): adopción nominal sin uso (F-896). Bestow y Singlife: ver el node de asesores. Salud Yape aún no tiene resultados que permitan juzgarlo (F-913).

### A.2 "Pocos toques" y usuario digitalmente saludable (macro)

- **No se busca un usuario que entre cada día.** En productos de pocos toques la señal es la resolución eficiente cuando ocurre un evento. Los indicadores de volumen de app (descargas, usuarios activos) no miden eso;
- **Valor sin invadir.** En Perú la invasión tiene costo legal: multas de hasta 450 UIT por llamadas comerciales sin consentimiento y un proceso a Pacífico por llamadas de spam (F-70, F-117). Eso empuja a monetizar con **consentimiento y eventos** (vencimiento, siniestro, cambio de vida), no con frecuencia. Vitality es el modelo de enganche más citado, pero sus cifras son autorreporte (F-25); la mejor prueba causal disponible es un RCT de feedback con incentivo que valida el mecanismo, no el negocio (F-442, F-353).

### A.3 Fricciones de confianza y bancaseguros (meso)

- **Confianza.** En Perú, ~48% desconfía de las aseguradoras y la causa principal es la falta de información (node de comportamiento). La confianza institucional subió a 45% en 2026 y sigue en zona de desconfianza; las empresas son lo más confiable (57%) (F-887).
- **Qué se sabe de bancaseguros.** (1) El cliente asocia el seguro al banco: 72% se quedaría más en su banco si compra allí un seguro (F-903). (2) Quien compra por bancaseguros lo hace por la relación con la sucursal (Pakistán, F-908). (3) La responsabilidad ante el cliente es compartida en la práctica: en Perú Indecopi sanciona al banco aparte (F-889), India ordenó un reembolso conjunto (F-906), Argentina hace que el reclamo pase por el banco como tomador (F-905), y en Perú el desgravamen concentra denuncias contra bancos y aseguradoras a la vez (F-888, F-890). (4) **Lo que no se sabe:** si el cliente culpa al banco o a la aseguradora. Es una laguna, no un hallazgo.
- **Fidelidad.** No hay literatura regional que pruebe que digitalizar reduzca el churn. La retención depende de la duración estructural del producto (SOAT anual vs. vida a 15 años) y de la experiencia de pago de siniestros (F-850): quien ve un pago recompra más.

## B. Inventario de intervenciones (mecanismo, momento, efecto, duración, costo, conducta real o métrica superficial)

| # | Intervención | Mecanismo | Momento | Efecto reportado | Duración | Costo conocido | ¿Conducta real? | Fuentes |
|---|---|---|---|---|---|---|---|---|
| 1 | Aval de tercero local | Confianza delegada | Venta | +40% de probabilidad de compra | Una temporada | Comisión del tercero (~25% a corredores según un blog de una aseguradora) | Sí (compra pagada) | F-847, F-939 |
| 2 | Prima descontada a la cosecha | Descuento hiperbólico; liquidez | Cobro | 72% vs 5% | Un ciclo | Riesgo de contraparte; requiere un pagador | Sí | F-848 |
| 3 | Sesión intensiva con red social | Difusión de conocimiento | Venta | +43% de compra | Dos rondas | Costo de sesiones (n.d.) | Sí | F-849 |
| 4 | Rebaja o subsidio de precio | Precio | Venta | −10% de precio → +10-12% de compra; quitar subsidio ↓ cobertura | Corto | Directo | Sí, pero se paga | F-847, F-855 |
| 5 | Módulo de educación financiera | Conocimiento | Previo | Poco efecto en seguros; positivo en promedio general; en crédito digital sube conocimiento y mora | — | n.d. | Mixto | F-847, F-852, F-860, F-862 |
| 6 | Pago visible a la comunidad | Disponibilidad; prueba social | Renovación | Demanda ↑ tras pago propio o vecino; se diluye | Años | Costo del siniestro | Sí | F-850 |
| 7 | Devolución sin siniestro | Aversión a perder la prima | Venta, recompra | Confianza ↑; tamaño n.d. | n.d. | Alto (devolución esperada) | No probado | F-853, F-922 |
| 8 | Pago y renovación por celular con SMS | Fricción de pago; olvido | Renovación | +17,4 pp | Un año | Bajo (SMS, USSD) | Sí (registro administrativo) | F-856 |
| 9 | Recordatorio | Atención limitada | Pago, ahorro | +6% de ahorro; +3 pp de meta | Corto; repetidos no suman | Bajo | Sí | F-859 |
| 10 | Cobertura gratuita ligada a otro servicio | Reciprocidad; fidelización del operador | Venta | >1 M cubiertos (PR); churn sin cifra | n.d. | Absorbido por el operador | **Superficial hasta medir conversión a pago** | F-925, F-926 |
| 11 | Seguro embebido en billetera | Baja fricción | Venta | Meta 30.000 de ~17 M; sin resultados | n.d. | n.d. | Sin evidencia | F-913 |
| 12 | Asistente conversacional | Menor fricción de acceso | Venta, servicio | >20% de clientes nuevos de Tuio (PR); baja aceptación en encuestas | n.d. | n.d. | Parcial | F-932, F-901, F-902 |
| 13 | Canal físico o asistido | "Reaseguro" presencial | Venta | Lo offline ≈30% de ventas en una región (PR) | Años | Alto | Sí, ⚠️S | F-929 |
| 14 | Verificación y antifraude | Seguridad percibida | Venta | SOAT 9/10 digital con fraude documentado | — | n.d. | Parcial | F-891, F-892 |
| 15 | Reclamo digital con estado visible | Carga cognitiva; ansiedad | Siniestro | Satisfacción ↑; fallas de 33-39%; NPS −11 si escala | — | n.d. | Parcial | F-909, F-183 |
| 16 | Delegado autorizado | Confianza en la familia | Servicio | 33.674 usan tercero en Pensión 65 | — | n.d. | Sí (cobro) | F-880, F-866 |
| 17 | Gamificación (ruleta mensual en app) | Recompensa variable | Engagement | El único experimento fuerte de gamificación en retail dio +21% que sobrevivió al retiro; en LatAm no hay evidencia causal | — | n.d. | Incierto | F-918, F-807 |
| 18 | Capacitación a mayores | Autoeficacia | Post-venta | Sin resultados | — | n.d. | Sin evidencia | F-868, F-869 |

**Qué cambió conducta real y qué solo una métrica superficial.** Cambiaron conducta con control: aval, calendario de pago, sesión con red, recordatorio (todas de compra o ahorro; en seguros, Ghana en renovación). Métricas superficiales que conviene no usar como éxito: personas cubiertas por seguros gratis (F-925), cuentas validadas (F-896), pólizas emitidas por canal sin pago posterior, metas anunciadas (F-913) y descargas.

## C. Población y segmentación

### C.1 Quién quedó dentro y quién fuera (Perú, orden de magnitud)

| Criterio | Dato | Fuente |
|---|---|---|
| Informalidad laboral | 70,7% (rural 94,8%; jóvenes 84,8%) | F-878 |
| Internet por área (6+) | Lima 90,3% · resto urbano 84,4% · **rural 59,6%** | F-876 |
| Hogares con internet | Lima 78,2% · **rural 23,4%** | F-876 |
| Uso de internet en 60+ | 47% (urbano 56,8%, rural 14,6%) | F-877 |
| Cuenta financiera; pagos digitales | 59%; 52% (2024) | F-875 |
| Independientes con seguro social | 11,8% | F-879 |
| Microseguros: usuarios | 4,87 M en 2016, 64% por bancaseguros | F-884 |

**Techo real (método propuesto, no cifra).** Estimar con datos propios la intersección: clientes potenciales con (cuenta o billetera) ∩ (celular con datos) ∩ (ingreso suficiente para la prima) ∩ (disposición a comprar sin asistencia). Los datos públicos dan los márgenes, no la intersección, y no se pudo calcular aquí.

### C.2 Más allá de las variables obvias (clústeres y barreras emergentes; evidencia indirecta)

- **Quién paga no es quién usa** (familiar que cobra, empresa que descuenta la prima): Pensión 65 con tercero (F-880), prima a la cosecha (F-848).
- **Flujo de ingreso irregular** vs. salario formal: el momento del cobro cambia la compra (F-848).
- **Experiencia previa de pago** propia o del vecino (F-850).
- **Relación con quien avala** (corredor, banco, familiar, agente local): F-847, F-903.
- **Miedo a estafas y suplantación**, sobre todo en mayores (F-894, F-892).
- **Cliente "heredado" de un banco que no sabe que tiene el seguro** (cobros indebidos y desafiliación pendiente): F-888, F-890.
- **Obligatorio vs. voluntario:** SOAT se digitalizó por ser obligatorio y estandarizado, no por afinidad digital (F-891).
- **Sin evidencia hallada:** lengua originaria, plan de datos limitado, dispositivo compartido.

### C.3 Cómo se adaptaron las intervenciones por segmento

- **Rural, informal:** pago diferido o fraccionado (F-848), sesiones con red (F-849), USSD y micro-primas (F-928). Resultado con control: solo agro.
- **Mayor:** tarjeta con tercero autorizado (F-880) y canal bancario asistido; delegados informales con riesgos (F-866).
- **Ciudades de nivel 2 y 3:** tiendas físicas y call center (F-929).
- **Cliente de banco:** venta cruzada a la base (F-903); sus costos de reputación aparecen en Indecopi (F-889).

### C.4 Qué segmentos se excluyen y cuánto cuesta

Se excluyen sistemáticamente quienes no tienen cuenta (41%), el rural y el informal con ingreso irregular. **El costo de esa exclusión no se pudo cuantificar con fuentes públicas** (laguna 15 y 18). Lo que sí se observa: Ghana mostró el mayor efecto del canal móvil justo en informales (F-856), así que excluirlos por defecto podría dejar fuera donde el digital más ayuda. Es una inferencia, no un resultado.

## D. Fricciones en el ciclo de vida y dónde lo digital resolvió o solo movió

| Etapa | Fricción conductual | Evidencia | ¿Resolvió o movió? |
|---|---|---|---|
| Descubrimiento | Falta de información; desconfianza | 92% investiga online, 25% compra 100% digital (F-182); causa #1 de desconfianza en Perú | Resolvió acceso a información; **no la confianza**: la desconfianza pasa a "¿quién está detrás?" (fraude, F-892) |
| Cotización | Carga cognitiva; comparar | >90% compara varias cotizaciones (F-904) | Resolvió comparabilidad; probablemente intensifica la competencia por precio (hipótesis) |
| Contratación | Declaración de salud con riesgo de nulidad; exclusiones poco claras | Formato con declaración jurada (F-924); Indecopi: la aseguradora debe acreditar que el asegurado conoció la exclusión (F-486) | Lo digital permite **dejar rastro** de que se informó (oportunidad); no resuelve la comprensión (F-9, F-6) |
| Pago | Sesgo del presente; liquidez | Pago a la cosecha 72% vs 5% (F-848) | Billetera mueve el cobro, no cambia el calendario del ingreso informal |
| Renovación | Olvido, agenda, procrastinación | 19,8%, 17,9% y 15,6% como razones (F-857) | Resolvió parcialmente: +17,4 pp (F-856) |
| Siniestro | Ansiedad; falta de estado | Fallas 33-39% (F-183); actualizaciones adecuadas 22% (F-909) | **Movió** la fricción al escalamiento y a las llamadas de estado |
| Reclamo o disputa | Desconfianza en la decisión | 8.248 reclamos, 87,8% ya presentados a la aseguradora (F-888) | Lo digital no cambia la decisión; sí puede mejorar la trazabilidad |
| Cobros no pedidos | Inercia; débito automático | Desgravamen, desafiliación pendiente (F-888, F-890) | La cobranza se digitalizó; el consentimiento no |

**Oportunidades no cubiertas por segmento** (síntesis; ver §5 para prioridad): independiente informal (O2, O1), rural (O11), mayor (O6, O7), cliente de banco (O3, O13), cliente nuevo (O9, O8), todos (O4, O12).

## E. Cross-industry y transferibilidad

| Industria | Hallazgo | Qué condiciones lo hicieron funcionar | ¿Existen en Perú/LatAm? | Qué adaptar | **Transferibilidad** |
|---|---|---|---|---|---|
| Banca y ahorro | Recordatorios con meta e incentivo: +6% de ahorro (F-859) | Meta explícita; mensaje con razón concreta; **un** recordatorio basta | Sí, incluso se probó en Perú | Vincular a una razón concreta (qué protege la póliza) y a un pago en un toque | **Transferible con adaptación** |
| Seguro agrícola | Pago a la cosecha: 5% → 72% (F-848) | Un pagador que descuenta la prima; producto ligado a un contrato | Parcial: informales sin pagador único | Cobro ligado a flujo (ventas por QR, plataformas) | **Transferible con adaptación** |
| Seguro agrícola | Aval de un tercero local: +40% (F-847) | Tercero con confianza previa en la comunidad | Sí (corredores, bancos, bodegueros) | Evitar conflicto de incentivos; trazar responsabilidad | **Transferible** |
| Seguro agrícola | Sesión con red: +43% (F-849) | Redes densas de aldea; difusión de conocimiento | Parcial (rural sí; urbano disperso) | Grupos de gremios, mercados, apps de transporte | **Transferible con adaptación** |
| Educación financiera | Efecto medio positivo en 76 RCT (F-860); nulo para comprar seguros (F-847, F-852); en crédito digital sube conocimiento y mora (F-862) | Depende del contenido y de la conducta medida | Sí | Úsese como complemento; nunca como única palanca | **No transferible como palanca única** |
| Banca básica | Cuentas gratis: 3% con ≥5 depósitos en Chile (F-861) | — | Sí (Chile es LatAm) | Acceso ≠ uso: el costo no era el cuello de botella | **No transferible** (lección de medición) |
| Pagos móviles | M-Pesa (F-863): efecto vía agentes y ahorro | Red densa de agentes; dinero móvil como puerta | Yape/Plin: hay red y uso (16 M activos, 66 transacciones al mes, F-912) | Usar las vías de pago, no copiar el modelo | **Transferible con adaptación** |
| Pagos QR | CoDi: adopción nominal sin uso (F-896) | Obligación sin incentivo | Es LatAm | Medir uso, no cuentas | **Lección de medición, transferible** |
| Pagos instantáneos | Pix: los mayores adoptan menos y son blanco de estafas (F-894, F-895) | Confianza y seguridad percibida | Mismo patrón esperado en Perú (hipótesis) | Antifraude visible y soporte | **Transferible con adaptación** |
| Crédito digital | Condiciones poco entendidas, mora (F-862) | Fricción mínima + términos opacos | Sí | En seguros, equivale a exclusiones poco claras: "explicar más no basta" (node de comportamiento) | **Transferible como advertencia** |
| Telecomunicaciones | Cobertura gratuita ligada al gasto: alcance sin churn medido (F-925); Linda Jamii cerró (F-927) | Operador interesado en fidelizar; datos de gasto | No se halló en Perú | Probar conversión a pago, no cobertura | **Transferible con adaptación** (evidencia débil, ⚠️S) |
| Servicios públicos | Pensión 65: tarjeta con tercero autorizado (F-880) | Beneficio claro; apoyo familiar; red del Banco de la Nación | Sí | Consentimiento y permisos del titular | **Transferible con adaptación** |
| Salud | Telemedicina de EsSalud: 1,6 M atenciones (F-881) | Impulso institucional | Sí | Soporte para mayores; sin dato por edad | **Transferible con adaptación** (sin evidencia de adopción) |
| Retail y lealtad | Un solo experimento fuerte de gamificación (+21% que persiste, F-807); sin evidencia en LatAm | Contexto de un centro comercial asiático | Parcial | Probar antes de escalar (ruleta mensual de Rímac, F-918) | **Transferible con adaptación** (evidencia débil) |
| Educación en línea | Intervenciones breves ayudan, "no hay bala de plata" (F-864) | Barrera específica del estudiante | Sí | Elegir según la barrera | **Transferible con adaptación** |
| Salud (seguros) | Empujar a elegir activamente puede empeorar la selección adversa (F-858) | Precios que se ajustan al riesgo | En salud privada, sí | Evaluar el efecto en el pool antes de forzar | **Transferible como advertencia** |

## F. Criterios para las tres definiciones basales

> Son **criterios y fórmulas propuestos** (inferencia de diseño), no hallazgos. Los umbrales los fijan los datos internos.

### F.1 Cliente digitalmente sano

**Principio.** Un cliente sano resuelve lo que necesita cuando ocurre un evento, con poco esfuerzo, sin tener que volver por otro canal. No es quien abre la app más veces.

| Métrica | Qué mide | Cómo evitar que sea una métrica superficial | Soporte |
|---|---|---|---|
| **Resolución digital verificada** | % de eventos (siniestro, endoso, consulta, pago) cerrados en digital **sin recontacto en otro canal a 7-14 días** | Contar como "no contenido" a quien abandona; un blog sugiere que 40% reportado puede ser 18-24% real (hipótesis, F-910) | F-909 |
| **Esfuerzo percibido por evento** (Customer Effort Score) | Qué tan fácil fue resolver | Medir por evento, no global; predice lealtad mejor que satisfacción o NPS en centros de contacto B2C (no es seguros ni LatAm) | F-865 |
| **Completitud sin fricción** | % que llega de inicio a póliza emitida (compra) o a número de siniestro (aviso), por paso | Reportar abandono por paso, no solo el total | — |
| **Escalamiento planificado vs. forzado** | % que pasa a un humano por diseño vs. por falla | El forzado debe medirse con NPS aparte (−11 al escalar mal) | F-183 |
| **Activación temprana** | Uso del canal digital en los primeros 30-90 días | Es un predictor, no un resultado | — |
| **Por qué no descargas ni usuarios activos** | No dicen si se resolvió algo | — | F-909 (solo 41% de los digitalmente comprometidos usa web o app para avisar el siniestro) |

### F.2 Fidelidad

**Principio.** En un mercado de baja confianza, renovar por inercia no es fidelidad: hay que separar la renovación **activa** de la **pasiva** y poner el centro en la conducta tras el siniestro.

| Señal (de más débil a más fuerte) | Definición operativa | Soporte |
|---|---|---|
| Renovación pasiva (débito automático, cobro por defecto) | Se mantiene sin acción del cliente | La inercia es alta (F-858); riesgo de cobros no pedidos (F-888, F-890). **No contarla como fidelidad** |
| Persistencia por cohortes y canal | Pólizas vigentes a 13, 25 y 61 meses, por canal de origen | Sin dato público; India vs. Australia opuestos (F-870, F-871) |
| Pago sin recordatorio | Paga a tiempo sin empuje | F-856, F-859 |
| Más de un producto | Segunda póliza en 12 meses | Asociación con retención (F-873, F-874); posible selección |
| **Conducta tras el siniestro** | Renueva después de reclamar; recontrata tras un pago | La demanda sube tras un pago propio o vecino (F-850) |
| Referidos | Trae a otra persona | — |
| NPS (actitud) | Solo como complemento | No decide solo (F-865) |

**Según la duración del producto.** SOAT (un año): recompra sin lapso de cobertura y sin intermediario; vida (15 años): persistencia a 13, 25 y 61 meses; salud: renovación más uso. **Hipótesis que debe probarse, no darse por cierta:** que digitalizar eleva la persistencia (no hay estudio regional que lo demuestre).

### F.3 Cliente de alto valor y a quién conviene empujar hacia lo digital

**Principio.** Que un cliente valga mucho no dice si conviene empujarlo a lo digital. Hay que decidir por el **cambio esperado en valor** que produce la intervención.

**Variables para el valor:**
1. **Margen técnico esperado** por ramo y cohorte (un ramo con ratio combinado >100% no es "alto valor" aunque venda mucho: Mapfre Perú, 102,4% en el 1T 2026, F-505).
2. **Persistencia esperada** (por cohorte, canal y producto).
3. **Potencial de segundo producto** (F-873, F-874).
4. **Costo de adquirir y de servir por canal** (comisión de corredor ~25% según un blog, F-939; costo de servicio por canal es dato interno).
5. **Riesgo de pérdida** del cliente si se le fuerza a un canal que no domina.

**Regla de decisión propuesta** (estimada con experimentos, no con tasas de adopción observadas, que están sesgadas por autoselección):

> Empujar a digital si **ΔVAN = p(adopta) × (costo de servir humano − costo de servir digital) × horizonte + Δ persistencia × margen − costo de la intervención − p(abandono inducido) × LTV > 0**

- Se estima con un **modelo de uplift** a partir de un experimento aleatorizado.
- Penalizar el **escalamiento mal ejecutado** (−11 puntos de NPS, F-183).
- En productos complejos y de alto valor (vida individual) el canal humano se mantiene; ver el node de asesores.

| Cuadrante | Valor del cliente | Respuesta esperada al digital | Qué hacer |
|---|---|---|---|
| Alto · alta | Alto | Alta | Incentivar y facilitar |
| Alto · baja | Alto | Baja | Mantener canal asistido; digital como complemento |
| Bajo · alta | Bajo | Alta | Autoservicio por defecto |
| Bajo · baja | Bajo | Baja | Canal masivo asistido de bajo costo (agente, delegado) |

## G. Hipótesis para probar (sin resolver)

| # | Hipótesis | Cómo probarla | Resultado de conducta |
|---|---|---|---|
| DS1 | El aval del canal conocido sube la compra más que cualquier cambio de interfaz en vida y SOAT | A/B de remitente (asesor/banco vs. aseguradora) | Compra pagada |
| DS2 | Cobro alineado al ingreso eleva persistencia en independientes | Dos brazos de calendario | Pagos consecutivos a 6 meses |
| DS3 | Recordatorio con pago en un toque eleva la renovación en ticket bajo | RCT (replica Ghana en Perú) | Renovación a 90 días |
| DS4 | Digital no reduce la persistencia frente al asesor una vez controlada la selección | Cohortes por canal con emparejamiento o asignación aleatoria | Persistencia a 13 y 25 meses |
| DS5 | En bancaseguros el cliente atribuye el problema a ambos; una "puerta única" baja reclamos repetidos | Medición previa y posterior | Tiempo de resolución y reclamos repetidos |
| DS6 | Un delegado autorizado eleva la completitud de trámites en mayores | Piloto con consentimiento | Trámites completados |
| DS7 | La devolución de prima sube la persistencia más de lo que cuesta | Dos productos comparables | Persistencia y margen |
| DS8 | El estado visible del siniestro reduce llamadas sin bajar la satisfacción | A/B sobre el aviso de estado | Recontacto a 14 días |
| DS9 | Auditoría de uso real de apps de competidores (Rímac, Pacífico, Mapfre, La Positiva, bancos) | Pruebas de tareas con 8-10 personas por app, incluyendo mayores | Tareas completadas, errores, tiempo |

---

## Conexiones

- [[venta-vida-digital-hibrida-latam|Venta de seguros de vida en LATAM]] — el caso de Azos (tecnología distribuida a través de corredores) y el de Betterfly; aquí se amplía a todos los ramos y a mercados emergentes de otras regiones.
- [[futuro-asesores-seguros-venta-digital|¿Desaparecerán los asesores de seguros?]] — marco causal del intermediario (Cummins y Doherty, F-180) y casos de Ethos y Bowtie; este node suma la evidencia de aval, calendario de pago y renovación digital.
- [[seguros-comportamiento-mundo-peru|Comportamiento, percepción y valoración frente a seguros]] — confianza, falta de información y datos de penetración; aquí se contradice el "~4 de cada 10" con una nota que dice "3 de cada 10" (F-885).
- [[transicion-venta-fria-a-opt-in|Transición de venta fría a venta opt-in]] — el consentimiento como base legal de la monetización sin spam (F-70, F-117).
- [[behavioral-design-estado-disciplina|Behavioral design: estado de la disciplina]] — crisis del nudge promedio; por eso aquí se priorizan intervenciones estructurales (aval, calendario de pago) sobre mensajes.
- [[lealtad-gamificacion-recompensas-retail|Gamificación, recompensas y lealtad en retail]] — evidencia limitada de gamificación (F-807) para evaluar la ruleta mensual de la app de Rímac.
- [[conducta-humano-ia|Conducta humano-IA]] — adulación y confianza en la IA; aquí, la aceptación baja de chatbots para reclamar (F-901, F-902).
- [[evaluacion-calidad-agentes-conversacionales-ia|Evaluación de calidad de agentes conversacionales de IA]] — cómo medir un asistente de WhatsApp antes de escalarlo.
- [[material-visual-venta-consultiva|Material visual en la venta consultiva]] — cómo reducir la incertidumbre en la explicación previa de exclusiones.
- [[mecanismos-seguros-salud|Mecanismos de seguros de salud]] — advertencia sobre inercia y selección adversa al empujar la elección (F-858).
- [[fenomeno-el-nino-impacto-personas|Fenómeno El Niño: impacto en la vida de las personas]] — seguros paramétricos y confianza tras un pago.
- [[modelo-personas-sinteticas|Modelo de personas sintéticas (lapuerta)]] — las variables "quién avala" y "calendario de ingreso" no están en el esquema actual (v1.3); candidatas a evaluar con `/cerrajero`.
