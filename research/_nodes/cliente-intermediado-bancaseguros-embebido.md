# Cliente intermediado: cuando el cliente llega por el banco, la billetera, el empleador o el corredor

> Documento de investigación. Fuente persistente y versionada en el repositorio.
> Fecha de elaboración: 2026-10-29 · Última actualización: 2026-10-29 (§3.1 señales de embebido, paramétrico y finanzas abiertas) · Versión: v1.0
> Origen: pregunta 3 del brief "Benchmarking: el valor de la recurrencia digital en seguros" (sobre todo
> investigación de negocio; lo académico solo para la teoría del intermediario). Insumo para la Gerencia de
> Digital de RIMAC; RIMAC está excluida como caso, fuente o benchmark.
> Pregunta: ¿qué cambia para la estrategia digital cuando el dueño de la relación es otro?
> Alcance: Perú y LatAm primero; Reino Unido, India, EE.UU. y Australia como contraste (🌐).
> Fuentes registradas en `research/fuentes/codice.md`: F-952 a F-958, más F-180, F-181, F-375, F-851, F-900,
> F-902, F-904 (lectura ampliada el 2026-10-29), F-905, F-906, F-923, F-924 y F-940 ya existentes.
> Output derivado: `research/_outputs/informe-canal-e-intermediarios-p2-p3-2026-10-29.md` (Parte B).

---

## 0. Resumen

**Cuando el cliente es de otro, el dueño de la relación es el intermediario.** La aseguradora tiene contacto
directo en dos momentos: el siniestro y el fin del vínculo (cuando termina el crédito o el empleo).

- **Teoría.** El intermediario reduce asimetrías de información y costos de búsqueda; no desaparece por la
  tecnología (F-180, 🟢 A). Los canales caros sobreviven si aportan servicio o mejor manejo de conflictos (F-923).
- **Banco.** Escala porque cobra con la cuota, pero con comisiones altas sin competencia (27% a 37% de la prima en
  Chile antes de licitar; la licitación bajó el desgravamen 62%, F-904), bajo uso del seguro (siniestralidad de
  16,7% en microseguros peruanos, F-902) y reclamos (38,4% por cargo indebido en Indecopi, F-902; PPI en el Reino
  Unido, F-953). Solo 12% mantiene el seguro de terremoto al terminar el crédito (F-902).
- **Regulación peruana.** Desde septiembre de 2025, al menos un crédito de consumo sin desgravamen obligatorio
  (F-952). En el hipotecario sigue siendo condición.
- **Billetera.** Escala la venta (11 millones con póliza en Mercado Pago Brasil, F-954), pero no hay cifras públicas
  de retención. En Perú, 13% tiene seguro privado pese al uso diario de billeteras (F-906).
- **Empleador.** Hay dos clientes: Recursos Humanos decide y el trabajador usa. La afiliación y la rotación
  determinan la caída de pólizas (F-958).
- **Corredor.** Concentra la mayor parte de la prima no vida en la región (F-900, F-375) y aporta en el siniestro
  masivo (F-904); su riesgo está en lo simple (F-181).

## 1. Quién controla cada momento

| Momento | Banco | Billetera | Empleador | Corredor |
|---|---|---|---|---|
| Elegir | El banco | El cliente, en un clic | Recursos Humanos | El corredor recomienda |
| Cobrar | Con la cuota | La billetera | La planilla | Aseguradora o corredor |
| Servicio | Aseguradora | Aseguradora, a veces dentro de la plataforma | Aseguradora y Recursos Humanos | El corredor filtra |
| Siniestro | Aseguradora (en desgravamen cobra el banco) | Aseguradora | Aseguradora | El corredor pelea el caso |
| Fin del vínculo | Termina el crédito | Baja en un clic | Termina el empleo | El corredor cambia de aseguradora |

Síntesis de la evidencia de este node, no un dato.

## 2. Evidencia por puerta

| Puerta | Hallazgo | Fuente | Rigor |
|---|---|---|---|
| Banco · Chile | Licitación obligatoria desde 2012: desgravamen −62,1%, incendio y sismo −34,3%; corredores ligados al banco siguen cobrando más | F-904 | 🔵 B |
| Banco · Perú | Microseguros: 97,8% por bancos y microfinancieras, comisiones 28%-60%, siniestralidad 16,7% | F-902 | 🔵 B |
| Banco · Perú | Desgravamen opcional en al menos un crédito de consumo desde 2025 | F-952 | 🔵 B |
| Banco · Reino Unido 🌐 | PPI: más de £38.000 millones devueltos, 32,4 millones de reclamos | F-953 | 🔵 B |
| Banco · India 🌐 | Persistencia mixta según el corte (65,4% contra 60,2%; 73% al mes 13 frente a 86% en línea) | F-956, F-957 | 🟠 D |
| Banco · España 🌐 | El canal bancario baja costos; los canales conviven por función | F-923 | 🟢 A |
| Región | Bancaseguros y afinidad: 25%-30% de la prima en 2023; en no vida bajaron a 15%-20% | F-375 | 🔵 B |
| Billetera · Brasil | Mercado Pago: 11 millones con póliza; un banco digital vendió más de un millón de pólizas de vida en ~18 meses | F-954, F-900 | 🟠 D, 🟡 C |
| Billetera · Perú | Seguro de salud en Yape con meta de 30.000 afiliados (0,18% de la base) | F-940 | 🟠 D |
| Embebido 🌐 | 42% compraría el seguro de auto en el concesionario; proyección de 18% de la prima australiana en 2033 | F-905, F-955 | 🟡 C |
| Empleador 🌐 | Afiliación por autoservicio: caída 45% mayor a la esperada | F-958 | 🟡 C |
| Corredor | 50%-80% de la prima no vida en LatAm; más de US$15.000 millones en comisiones de baja complejidad expuestas a la IA en EE.UU. | F-900, F-181 | 🟡 C |

## 3. Hipótesis vivas

| Código | Hipótesis | Estado | Cómo probarla |
|---|---|---|---|
| CI1 | Un aviso de continuidad al terminar el crédito retiene más que el 12% actual | 🟠 Sin evidencia directa; inferida de F-902 | Piloto con grupo de control en créditos que vencen en un trimestre |
| CI2 | Mezclar clientes intermediados en la meta de digitalización esconde la adopción real | 🔵 Aritmética; depende de la composición de la cartera | Separar la métrica por puerta de entrada y por titular contra dependiente |
| CI3 | El seguro embebido retiene menos que el elegido | 🟠 Sin datos públicos | Cohortes por canal de origen con renovación a 12 y 24 meses |
| CI4 | Con el desgravamen de consumo opcional, sube la caída de ese producto | 🟡 Plausible por F-952 | Comparar la contratación antes y después del 9 de septiembre de 2025 |

### 3.1 Señales para la conversación con los ramos (2026-10-29)

- **El seguro embebido escala por volumen declarado, no por resultados publicados.** MetLife con Klimber
  (F-985), Leonisa con BNP Paribas Cardif (F-965) y Turaco (F-981) reportan millones de asegurados, sin
  siniestralidad ni renovación. En Perú, el embebido pesa menos de 1% de la cartera de Pacífico (F-967).
- **El paramétrico peruano exige un tomador colectivo** (F-786). Es otra forma de intermediación: el
  cliente final llega por una microfinanciera, un gremio o el Estado.
- **El banco ya no es el único dueño posible de los rieles.** Finanzas abiertas (F-970, en proyecto) y TAPP
  (F-971) abren pagos y datos a terceros; Banking as a Service no incluye aseguradoras (F-974). En Brasil,
  el seguro abierto no encontró demanda (F-983).

## 4. Vacíos

- Reparto público de primas por canal en Perú.
- Retención o persistencia por canal en América Latina.
- Retención del seguro embebido en la región.
- Una licitación peruana de seguros atados al crédito.
- El texto completo de la Resolución SBS 890-2025 (leída por prensa oficial).

## Conexiones

- [[futuro-asesores-seguros-venta-digital|¿Desaparecerán los asesores de seguros?]] — trae la teoría del
  intermediario (F-180). Ese node mira la venta; este, qué pasa después con el cliente intermediado.
- [[venta-vida-digital-hibrida-latam|Venta de seguros de vida en LATAM]] — bancos digitales y billeteras como
  puerta de venta en Brasil, Chile y Colombia.
- [[valor-recurrencia-digital-seguros|Valor de la recurrencia digital en seguros]] — pregunta 1. Allí, las anclas
  (hipoteca, empleo, crédito, billetera) explican la permanencia; aquí, quién controla cada momento.
- [[canal-servicio-siniestro-seguros|Rol del canal en el servicio y el siniestro]] — pregunta 2. El siniestro es el
  momento de contacto directo con el cliente intermediado.
- [[transicion-venta-fria-a-opt-in|Transición de venta fría a opt-in]] — la venta en la puerta del crédito y sus
  reclamos (cargo indebido, PPI) son el mismo problema de consentimiento.
- [[fenomeno-el-nino-impacto-personas|Fenómeno El Niño: impacto en las personas]] — el seguro paramétrico (F-786, F-792)
  llega a las personas a través de un tomador colectivo: otra forma de cliente intermediado.
