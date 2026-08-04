# Cobranza de seguros con clientes empresariales (B2B / corporativo)

> Node. Investigación `/trinidad` (2026-08-04): cómo se opera la cobranza de primas de
> seguros cuando el cliente es una empresa (no persona natural) — proceso, marco legal
> peruano, tecnología/automatización, tercerización, y qué tan instalado está el tema
> socialmente. Fuentes indexadas en `fuentes/codice.md` (F-469 a F-479).
>
> Fecha de elaboración: 2026-08-04 · Última actualización: 2026-08-04 · Versión: v1.0

---

## Resumen ejecutivo

Las tres pistas **no convergen porque cubren preguntas distintas** que sí encajan entre
sí: la pista empírica/regulatoria explica el **marco** (cómo debe operar la cobranza en
Perú), la pista de negocio muestra **hacia dónde se mueve la operación** (automatización
con IA, fuera de Perú por ahora), y la pista social confirma que este es un tema de
**back-office silencioso** — no hay percepción pública, quejas virales ni debate sobre
cobranza B2B de seguros. Eso no es una laguna de búsqueda: es una señal en sí misma (ver
§3).

## 🔬 Pista empírica / regulatoria

**Veredicto**: en Perú, la cobranza de primas empresariales opera bajo un marco legal
explícito (Ley 29946, Ley del Contrato de Seguro) que define un mecanismo estándar de
mora → suspensión → resolución, ejecutado en la práctica por la aseguradora y el
**corredor de seguros** (el intermediario obligado en el segmento corporativo/"high
commercial").

- **Marco legal de la mora**: el incumplimiento de pago de la prima produce la
  **suspensión automática de cobertura** transcurridos 30 días desde el vencimiento
  (salvo plazo adicional pactado). Durante la suspensión, el asegurador no responde por
  siniestros ocurridos. El asegurador debe **comunicar de forma fehaciente** el
  incumplimiento y el plazo para pagar antes de la suspensión (Ley 29946, Ley del
  Contrato de Seguro, Perú — F-469, 🔵 B). Si no se regulariza, el contrato se considera
  **resuelto** a los 30 días de comunicada por escrito esa decisión; la rehabilitación
  posterior aplica solo hacia el futuro y exige el pago total de lo vencido.
- **Estructura de la prima comercial**: la Resolución SBS 1840-2022 establece que la
  prima comercial = prima pura de riesgo + gastos de gestión (emisión, costos operativos,
  gestión continua del contrato) — la cobranza es, regulatoriamente, parte de ese costo
  de gestión que se traslada al cliente (F-470, 🔵 B).
- **Rol del corredor en el segmento empresarial**: en el segmento "High Commercial", la
  gestión integral del cliente corporativo —consultoría de riesgos, suscripción,
  **cobranza de primas**, siniestros, fidelización— recae en gran medida en el corredor
  de seguros, no directamente en la aseguradora; el corredor no puede recibir dinero
  directamente del asegurado por ley, lo que estructura cómo fluye el pago (aseguradora
  ↔ corredor ↔ empresa) (F-471, 🟡 C — descripción de práctica de mercado, sin fuente
  académica peer-reviewed que la sistematice).
- **Comparación internacional (fuera de Perú, registro genérico B2B)**: en mercados
  anglosajones, la cobranza de primas comerciales sigue un proceso escalonado estándar
  (llamadas y cartas → negociación de plan de pago → derivación a agencia de cobranza
  especializada → acción legal), con líneas de crédito típicas de 30/60/90 días entre
  broker y asegurador (F-472, 🟠 D — fuente de industria/blog sin metodología propia,
  pero describe una práctica ampliamente replicada en el sector).

**Lo que no se encontró**: ningún estudio académico peer-reviewed específico sobre
cobranza de seguros B2B (a diferencia de, por ejemplo, la literatura sobre riesgo moral o
selección adversa que sí es robusta en este proyecto — ver `mecanismos-seguros-salud.md`).
Es un tema operativo/regulatorio, no uno con tradición de investigación académica propia.

## 📱 Pista social / mediática

**Nivel de instalación social: 🧊 Sin tracción.**

Se buscó activamente cobertura noticiosa, quejas en redes (X/Twitter, Reddit, LinkedIn),
y reclamos públicos contra aseguradoras peruanas (Rimac, Pacífico) específicamente sobre
cobranza o facturación a clientes empresariales — no apareció ninguna discusión pública
identificable. Lo único que aparece es material institucional (manuales de facturación
electrónica de Rimac, canal de libro de reclamaciones genérico) y menciones tangenciales
de que Rimac debe responder reclamos en 15 días hábiles (F-473, ⚪ institucional, sin
relación directa al tema).

**Contraevidencia buscada activamente** (Paso 10 de `gossiper`): se buscó explícitamente
"queja/reclamo de cobranza de seguros empresariales" en español e inglés, en redes y
foros — no apareció ni el rumor ni el desmentido. Esto es consistente con la naturaleza
del tema: la cobranza B2B de seguros es una relación contractual entre empresas y
corredores/aseguradoras, gestionada por áreas de administración/finanzas, no un punto de
fricción que genere ruido público como sí lo generan, por ejemplo, el rechazo de
siniestros de salud (ver `_nodes/futuro-asesores-seguros-venta-digital.md`,
`mecanismos-seguros-salud.md`).

**Limitación explícita**: esto no descarta que existan quejas internas, en grupos
cerrados de LinkedIn, o en canales B2B no indexados por buscadores generales — solo que
no hay evidencia pública accesible de ellas.

## 📈 Pista de negocio

**Veredicto**: la frontera de innovación en cobranza de seguros B2B está en
**automatización con agentes de IA**, liderada por insurtechs fuera de Perú (México,
Argentina, Reino Unido) — no se encontró un jugador equivalente operando específicamente
en el mercado peruano.

- **Primo** (México/Buenos Aires): insurtech fundada por ex-consultores de BCG y talento
  técnico de Brubank/MercadoPago; automatiza cobranza, comisiones y conciliación de
  primas con agentes de IA — **gestiona USD 150M en primas con ~70% de automatización**
  operativa. Modelo de pricing atípico: cobra por resultado logrado, no por licencia (si
  el cliente no ve impacto, Primo no cobra). Cerró ronda seed en abril 2025 con Latitud y
  Better Tomorrow Ventures (F-474, 🟠 D — cobertura de prensa especializada que reporta
  cifras self-reported de la empresa, sin filing auditado; tratar el 70%/USD150M como
  cifra de marketing, no auditada).
- **Diesta** (Reino Unido): SaaS B2B enfocado en digitalizar y automatizar el
  procesamiento de pagos de primas entre aseguradoras — cerró semilla de USD 3.8-4M en
  octubre 2024 (liderada por FinTech Collective, con Commerce Ventures, Restive Ventures
  y SixThirty), tras un pre-seed de USD 2M. Su tesis de mercado: cada pago original de
  prima se mueve **siete veces** a través de sistemas anticuados antes de completarse —
  la ineficiencia que están vendiendo resolver (F-475, 🟠 D — múltiples notas de prensa
  especializada citando el mismo comunicado de la ronda; cuenta como una sola fuente
  primaria, no como triangulación independiente — eco de cita).
- **Mercado insurtech regional más amplio**: entre agosto 2025 y julio 2026 el
  financiamiento insurtech global alcanzó ~USD 1.67B, con ronda mediana de USD 30M
  (F-476, 🟡 C — agregador de funding rounds, metodología de conteo no auditable
  externamente) — contexto de que la categoría "pagos/cobranza B2B de seguros" es un nicho
  activo dentro de un mercado insurtech más amplio, no un boom aislado.
- **No se encontró** un insurtech de cobranza específicamente peruano o con operación
  confirmada en Perú — el hueco de mercado local está, por ahora, sin cubrir por un
  jugador especializado identificable.

**Contraevidencia buscada** (Paso 10 de `marketer`): se buscó activamente evidencia de
fracaso o problemas en este nicho (quiebras, downgrades) — no apareció nada verificable,
pero la categoría es reciente (rondas de 2024-2025) y aún no ha pasado por un ciclo
completo de maduración donde ese tipo de señal normalmente aparece.

## ⚖️ Síntesis

- **Perú específicamente**: la cobranza empresarial de seguros está fuertemente
  **normada** (suspensión a 30 días, comunicación fehaciente obligatoria, resolución de
  contrato) y operativamente **delegada en gran parte al corredor** en el segmento
  corporativo — no se encontró evidencia de que esté "digitalizada" o "automatizada" de
  forma sistemática en el mercado local; los ejemplos de automatización con IA
  encontrados operan en México, Argentina y Reino Unido, no en Perú.
- **Sin tensión entre pistas** en el sentido de "divergencia" — más bien **tres niveles
  de resolución distintos** sobre el mismo proceso: la ley define las reglas del juego,
  el negocio muestra hacia dónde evoluciona la tecnología que podría aplicarse a ese
  proceso, y lo social confirma que es una fricción de back-office sin ruido público —
  coherente con que el pagador es una empresa (con área administrativa dedicada) y no un
  consumidor individual con reacción emocional/pública ante el cobro.
- **Implicación para el proyecto**: si en algún momento se explora una oferta de
  cobranza/pago B2B para seguros empresariales en Perú (p. ej. para RIMAC empresas), el
  espacio competitivo local parece abierto — los jugadores identificados (Primo, Diesta)
  no operan aquí — pero el diseño debe respetar el marco de suspensión a 30 días de la
  Ley 29946, no solo optimizar cobranza como problema de UX/tecnología.

## Limitaciones

- Pista social: ausencia de tracción no equivale a ausencia de fricción real — solo a
  ausencia de fricción **visible públicamente**; no se tuvo acceso a foros cerrados de
  administradores/finanzas de empresas peruanas donde sí podría discutirse.
- Pista de negocio: las cifras de Primo (USD 150M gestionados, 70% automatización) son
  self-reported vía prensa, no verificadas contra un filing o auditoría independiente.
- No se encontró literatura académica peer-reviewed específica sobre cobranza de seguros
  B2B — el tema vive en normativa y prensa de industria, no en investigación académica.
- No se pudo confirmar si algún corredor o aseguradora peruana (Rimac, Pacífico,
  Interseguro) ya usa herramientas de automatización de cobranza tipo Primo/Diesta
  internamente — no hay comunicación pública al respecto.

## Conexiones

- [[mecanismos-seguros-salud]] — mecanismos de balance financiero y presión de costo de
  las aseguradoras, del que la cobranza efectiva es un componente operativo.
- [[matriz-productos-vida-rimac]] — catálogo de productos donde podría aplicarse un
  proceso de cobranza corporativa equivalente en el ramo Vida.
- [[futuro-asesores-seguros-venta-digital]] — contraste: la venta digital sí genera
  tracción social/mediática visible; la cobranza B2B, no — refuerza que la visibilidad
  pública depende de si el interlocutor es un consumidor individual o una empresa.
