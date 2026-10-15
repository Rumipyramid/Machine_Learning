# Digitalización de adultos de 50+ en contextos de baja digitalización (Latinoamérica, África, Asia)

> Documento de investigación. Fuente persistente y versionada en el repositorio.
> Fecha de elaboración: 2026-10-15 · Última actualización: 2026-10-15 · Versión: **v1.0**
> Origen: `/trinidad` (pista empírica + social/mediática + negocio/programas), a pedido del usuario.
> Fuentes en `research/fuentes/codice.md`: **F-802 a F-825** (todas nuevas).
> Pregunta permanente: **¿qué intervenciones de digitalización para mayores de 50 años en contextos
> poco digitalizados dieron resultados medibles, cuáles no, y qué tan sólida es la evidencia?**

---

## 0. 🎯 Alcance y cómo se leyó la evidencia

- **Población:** 50+; se aceptan cortes de 55+, 60+ y 65+ y se señala cuál usó cada estudio.
- **Geografía:** Latinoamérica, África (subsahariana y del norte), Asia (sur, sudeste, este). Periodo 2021-2026.
- **Qué cuenta como "favorable":** mejora medible en adopción, uso sostenido, autonomía o habilidades. Satisfacción o
  intención de uso = evidencia débil.
- **Regla de significancia:** si lo recuperado no trae p, IC o tamaño de efecto, se escribe "no reporta (en lo
  recuperado)". No se infiere.
- ⚠️ **Limitación de método de esta corrida:** solo pude leer **resúmenes y fragmentos devueltos por la búsqueda**.
  El acceso a los textos completos falló (la herramienta de descarga no resolvió el dominio), así que la mayoría de los
  p-valores, tamaños de efecto y n no se pudieron verificar. Donde falta un dato, está marcado.
- ⚠️ **Pista social:** no se buscó directamente en X, Reddit ni TikTok. La cobertura de esta pista es solo
  prensa y comunicados. Está declarado abajo.

---

## 1. Resumen ejecutivo (5 líneas)

1. **La evidencia rigurosa es casi inexistente**: encontré **un solo ECR con adultos mayores** en un país de ingreso medio (Brasil, 60+), y mide depresión, no habilidades digitales.
2. Las demás intervenciones de habilidades son **cuasi-experimentales o pre-post pequeñas** (n=10 a n=84), y varias en contextos urbanos o con participantes ya digitalizados.
3. Donde hay mejora medible (Tailandia, Corea, Singapur), es en **habilidades a corto plazo** (hasta 1 mes). **No encontré uso sostenido a 3, 6 o 12 meses** en ningún estudio.
4. La contraevidencia más fuerte no es un ensayo nulo sino **daño por diseño**: en India, los pagos y pensiones digitales excluyen a mayores por fallas biométricas (4-5% en un piloto de Karnataka, según prensa).
5. Vacíos grandes: **África sin ningún estudio específico de 50+**, Perú y México casi sin evaluación, y **ningún dato de retención de fintech o telecom por edad**.

**Convergencia entre pistas:** las tres coinciden en lo mismo: se capacita a muchas personas (producto) y casi nadie mide qué ocurre después (resultado).

---

## 2. 🔬 Pista empírica

### 2.1 Tabla de estudios

| Intervención | País (región) | Población (edad) | Diseño y n | Resultado | Significancia | Tipo de evidencia |
|---|---|---|---|---|---|---|
| Mensajes de texto de 6 semanas (psicoeducación + activación conductual) vs. un mensaje (F-802) | Brasil (LatAm) | 60+ con depresión, atención primaria | ECR, n=603 (298 / 305) | Mejoró la depresión: 42,4% vs. 32,2% a 3 meses. **No mide habilidad ni uso digital.** | OR ajustado 1,57; IC 95% 1,07-2,29; p=0,019. Diferencia absoluta ≈10 puntos porcentuales | Empírica fuerte (resultado en salud, no en digitalización) |
| 6 talleres de smartphone y tablet (F-804) | Tailandia (Sudeste asiático), urbano | 60+ | Cuasi-experimental, n=84; medición pre, post y a 1 mes (MDPQ-16) | Mejora de competencia con el dispositivo, mantenida a 1 mes | Resumen: "P<.000". Tamaño de efecto: no reporta (en lo recuperado). Control: no verificado | Empírica moderada |
| Educación en alfabetización digital (F-805) | Corea del Sur (Asia este), rural | 65+ | Cuasi-experimental, diferencias en diferencias; n no recuperado | Más uso de smartphone y grabación de video que el control; cognición β=1,305 | Uso: "significativo" (estadístico no recuperado). Cognición: p=0,05 | Empírica moderada. **Corea no es contexto de baja digitalización** |
| Programa en 4 áreas: formar a trabajadores de salud, generar demanda en mayores y cuidadores, participación social (F-811) | Tailandia | Corte etario no recuperado | Cuasi-experimental, 158 tratados vs. 157 control | Más acceso y uso del "libro digital de salud del mayor" que el control; satisfacción alta | "Significativamente" (estadístico no recuperado) | Empírica débil-moderada. Revista nacional, solo resumen leído |
| Curso de smartphone de 2 semanas, 6 clases remotas (F-809) | México | Mujeres 55-70, con estudios superiores y smartphone propio | Cualitativo, n=10 | Mejora promedio de 37% en competencias (15% WhatsApp, 69% botón de pánico) | No reporta | Débil. Muestra ya digitalizada |
| Aprendizaje abuelos-nietos, 3 meses (F-806) | China (Asia este), rural | Edad no recuperada | Cualitativo, 10 parejas | Mejoras reportadas en conocimiento y habilidades | No reporta | Débil |
| Curso en programa comunitario (F-823) | Colombia | Edad no recuperada | Pre-experimental sin control, n=15 | Pre-post en uso de redes sociales | No reporta | Débil. URL del estudio no verificada |
| Una sesión de entrenamiento en apps (banca, pagos, salud) (F-825) | India | Edad no recuperada | Un brazo, n=42; año probablemente 2020 | 70% usó las apps de forma independiente | No reporta | Débil. Posiblemente fuera del periodo |
| Programa de alfabetización digital con smartphone y datos entregados (F-807) | Singapur | 55+, bajo nivel socioeconómico | No aleatorizado con grupo de espera, n=138 | Mejora significativa en alfabetización digital | p y tamaño de efecto: no recuperados | Empírica moderada. **País de ingreso alto: comparador, no alcance** |
| Programa de capacitación en dinero móvil + SMS recordatorio (F-810) | Malawi (África subsahariana) | **Sin restricción de edad** | Experimento aleatorizado en grupos de ahorro | +5 pp (conocimiento), +3 pp (uso), +4 pp (inclusión financiera) | "Significativo" según resumen; p/IC no recuperados | Empírica moderada. **No es evidencia de 50+**; fuera de periodo (2020) |
| App de teleasistencia, 14 semanas (F-808) | Brasil (Ribeirão Preto, según búsqueda) | 60+ | ECR piloto, n=21 | Mide alfabetización en salud; resultado no recuperado | No recuperada | Piloto; sin resultado verificable |
| Programa de apps para actividades diarias (F-803) | India (Karnataka) | 60-75, ya usan smartphone | ECR por conglomerados, protocolo | **Sin resultados publicados** | — | Protocolo |

### 2.2 Con resultados favorables

- **Habilidades digitales a corto plazo**, en cuasi-experimentos de Tailandia (F-804), Corea (F-805) y Singapur (F-807). Es la señal más consistente, pero con diseños sin aleatorización y en contextos más digitalizados que el que pide el tema.
- **Acceso y uso de una herramienta digital de salud** apoyado por trabajadores de salud locales (Tailandia, F-811). La magnitud no se pudo verificar.
- **Salud entregada por canal de baja tecnología** (SMS en Brasil, F-802): efecto estadísticamente significativo y de tamaño práctico relevante en depresión. Prueba que un canal simple llega a mayores de 60 en un entorno de bajos recursos, no que se mejoró su autonomía digital.
- **Revisión de alcance** (F-819): hay ECR en Sudáfrica, Brasil y Turquía en depresión y soledad de mayores, con resultados "prometedores". Es un mapa, no una estimación de efecto.

### 2.3 Sin resultados o con resultados negativos o ambiguos

- **No hallé ningún ensayo con resultado nulo en digitalización de mayores de PBMI.** Eso es más probable que sea sesgo de publicación y falta de ensayos que evidencia de que todo funciona.
- **Dentro de los estudios favorables hay matices:** en Tailandia, quienes tienen 70+ y menor educación puntúan más bajo (F-804); en Corea, el efecto en cognición está en el límite (p=0,05, F-805); en India, los autores del piloto piden seguimiento porque una sola sesión no garantiza sostenimiento (F-825).
- **Revisión sistemática de servicios preventivos** (F-820): 24 estudios de 11 países, mejoras "modestas y mixtas". No verifiqué cuántos eran de PBMI.
- **ECR en India (F-803) sin resultados publicados**, y piloto de teleasistencia en Brasil (F-808) sin resultado recuperado: no se pueden clasificar como favorables ni nulos.
- **Daño por diseño** (no es una intervención de capacitación, pero es contraevidencia sobre digitalizar a mayores): ver §3.

### 2.4 Patrones de diseño (hipótesis, no conclusiones)

Ningún estudio comparó componentes entre sí, así que esto es lo que **se repite** en los casos con mejora, no lo que se demostró que causa la mejora:

1. **Varias sesiones estructuradas**, no una sola (6 talleres en Tailandia; 12 sesiones en un ensayo registrado sin país verificado, NCT07693582, sin resultados).
2. **Práctica con el dispositivo propio o entregado.** Singapur lo entregó junto con datos (F-807); México lo exigió como criterio (F-809).
3. **Intermediarios cercanos y de confianza:** trabajadores de salud (F-811), nietos (F-806), grupos de ahorro (F-810).
4. **Canal simple:** SMS en Brasil (F-802), sin app ni habilidades previas.
5. **Refuerzo posterior:** recordatorios por SMS (F-810); los autores indios piden sesiones de seguimiento (F-825).
6. **Los más viejos y de menor escolaridad se rezagan** (F-804): el mismo programa no basta para todos.

---

## 3. 📱 Pista social y mediática

**Cobertura buscada:** prensa y comunicados oficiales. **No se buscó directamente en redes** (X, Reddit, TikTok).
Validez medida por frecuencia de cobertura y validación social, no por rigor.

- 🔥 **India — exclusión por autenticación biométrica.** Reportajes de The Wire (F-814) y Deccan Herald (F-815) documentan a pensionistas de edad avanzada sin pensión ni raciones por huellas desgastadas o escáneres que no leen. Cifras de prensa: 4-5% de fallas de autenticación en un piloto de Udupi; ~1,3 millones de pensiones canceladas en Rajasthan en 2023-24 por muerte o migración, con muchos casos mal clasificados. **Tono: crítico.** Son cifras de prensa y casos individuales, no un conteo auditado.
- 🌡️ **Colombia y otros países de LatAm — cursos de celular para mayores.** Notas oficiales (F-821, F-822) cuentan personas formadas (150, 108) y testimonios. **Tono: positivo, promocional.** No miden resultados.
- 🧊 **África, Perú, Brasil, Indonesia, Vietnam, Bangladesh:** no apareció cobertura específica en esta búsqueda.

**Validación vs. amplificación:** la cobertura crítica de India tiene casos detallados y verificables caso por caso; la positiva de LatAm es comunicación institucional.

---

## 4. 📈 Pista de negocio y programas

- **Pensión 65 (Perú, F-816):** pago bimestral de S/350 vía Banco de la Nación a más de 824.000 beneficiarios; más de 700.000 con tarjeta de débito; el Midis capacita en uso de tarjeta y clave. **No hay dato de uso de billeteras digitales ni de uso sostenido.**
- **Libro de salud digital del mayor (Tailandia, F-812):** ~9,35 millones de mayores registrados y ~441.000 voluntarios, según un documento oficial. Son **registros**, no usuarios activos; no hay retención a 3, 6 o 12 meses.
- **India (F-813):** las transferencias del gobierno son una puerta de entrada a pagos digitales, pero el acceso móvil barato, la interoperabilidad y nuevas interfaces sostienen el uso. Sin desglose por edad.
- **África subsahariana (F-818):** dinero móvil en 28% de adultos (2022). Sin cifras para 60+ en lo recuperado.
- **Intención de adopción de Yape en mayores de Lima (F-817):** la facilidad de uso percibida es la variable más ligada a la intención. Es intención, no uso.
- **Fintech y telecom:** **No tengo una fuente verificada** de usuarios activos ni retención a 3, 6 y 12 meses de mayores de 50 en Paytm, PhonePe, M-Pesa, GCash, Yape u operadores móviles. Busqué programas de Google/Paytm/Safaricom y no devolvió nada específico.

---

## 5. ⚖️ Síntesis

- **Convergen** en dos puntos: (1) hay muchos programas que cuentan personas capacitadas y pocos que miden uso posterior; (2) los mayores quedan excluidos cuando el servicio supone habilidades o biometría que no tienen.
- **Divergen** en tono: la prensa de LatAm celebra los cursos; la de India documenta daño. No hay evidencia empírica que arbitre entre ambas, porque los cursos no se evaluaron con control y la exclusión india no es una intervención evaluada.
- **Implicancia para la pregunta original:** hoy no se puede afirmar con rigor qué intervención "funciona" para adultos de 50+ poco digitalizados en estas regiones. Lo que hay es una señal consistente de mejora de habilidades a corto plazo en estudios pequeños, y una señal consistente de que diseñar el servicio sin tener en cuenta a los mayores los excluye.

---

## 6. Limitaciones y vacíos

- **Método:** solo resúmenes; sin textos completos. p, IC, n y tamaños de efecto, faltan en la mayoría.
- **África:** ningún estudio específico de 50+. El único experimento africano hallado (Malawi, F-810) no restringe edad y es de 2020.
- **Latinoamérica:** el único ECR (F-802) no mide digitalización. Perú y México casi no tienen evaluaciones; Brasil, solo piloto (F-808).
- **Asia:** mejor cubierta en Tailandia y Corea (esta última no es baja digitalización). Sin evidencia en Vietnam, Bangladesh, Nepal ni Indonesia (solo menciones sin resultados). Filipinas: programa CLICK con mejora reportada en resumen de congreso, sin n ni estadística, no registrado.
- **Edades:** los de 50-59 casi no aparecen: los cortes son 55+, 60+ y 65+. Los 75+ solo se ven como subgrupo rezagado (F-804).
- **Uso sostenido:** ningún estudio mide 3, 6 o 12 meses. El máximo hallado fue 1 mes.
- **Autoselección:** varios participantes ya tenían smartphone o estudios superiores (México, India), lo que sobreestima el efecto en poblaciones de baja digitalización.
- **No exploré** literatura en chino, árabe, francés ni portugués fuera de lo que devolvió la búsqueda; puede haber estudios no indexados.
- **Siguientes pasos:** ClinicalTrials.gov, AEA RCT Registry, CTRI y ChiCTR; Global Findex microdatos por edad; textos completos de F-804, F-805, F-807, F-811.

---

## Conexiones

- [[conducta-humano-ia|Conducta humano-IA]] — la confianza y la descarga cognitiva importan si la digitalización pasa por asistentes de IA para mayores; hoy sin evidencia en este grupo.
- [[seguros-comportamiento-mundo-peru|Comportamiento y mercado global de seguros (Mundo vs. Perú)]] — la barrera de desconfianza y baja educación financiera se cruza con la exclusión digital de mayores.
- [[modelo-salud-ia-farmacias-peru|Modelo de triage IA + farmacias (Perú)]] — un canal simple (SMS, voz) con mayores de 60 tiene evidencia de efecto en salud (F-802); relevante para el diseño del triage.
- [[modelo-personas-sinteticas|Modelo de personas sintéticas (`lapuerta`)]] — el generador cubre acceso digital pero no distingue por edad dentro de 50+; no se propone cambio sin datos por edad.
