# Rol del canal en el servicio y el siniestro de un seguro

> Documento de investigación. Fuente persistente y versionada en el repositorio.
> Fecha de elaboración: 2026-10-29 · Última actualización: 2026-10-29 · Versión: v1.0
> Origen: pregunta 2 del brief "Benchmarking: el valor de la recurrencia digital en seguros" (académica +
> negocio; lo social solo para el siniestro). Insumo para la Gerencia de Digital de RIMAC; RIMAC está excluida
> como caso, fuente o benchmark.
> Pregunta: ¿qué rol cumple cada canal según el momento y el producto, sobre todo en el servicio y el siniestro?
> Alcance: seguros de Perú y LatAm primero; análogos de banca y servicios; EE.UU., Europa y Asia como contraste (🌐).
> Fuentes registradas en `research/fuentes/codice.md`: F-945 a F-951, F-959 y F-960 (F-944 reservado: datos
> internos, solo en el repositorio privado), más F-183, F-850, F-872, F-890, F-892, F-900, F-902, F-903, F-907,
> F-913, F-916 y F-918 ya existentes.
> Output derivado: `research/_outputs/informe-canal-e-intermediarios-p2-p3-2026-10-29.md` (Parte A).

---

## 0. Resumen

**El canal que gana depende de cuán clara, urgente y emocional es la gestión, no del producto.**

- **Lo claro migra; lo ambiguo llama.** Un portal web bajó 29% las llamadas sobre información clara y las subió
  sobre información ambigua (F-850, 🟢 A, causal).
- **El siniestro son dos momentos.** Avisar es urgente: el teléfono domina y quien avisa en digital no queda más
  satisfecho (F-947, 🟡 C, 🌐). Seguir el caso es repetitivo: recibir el estado por app se asocia a más satisfacción,
  pero solo un tercio lo recibe (F-947, F-872, 🌐).
- **El siniestro decide la permanencia, no el canal.** Tras un siniestro, cambiar de aseguradora es 35% más
  probable aunque 94% diga estar satisfecho; pesan la demora, el monto y la complejidad (F-890, F-892, F-950, 🌐).
- **Implicancia.** Tres metas en vez de una: migrar lo claro, acompañar lo ambiguo (persona al frente, digital
  para seguir) y no forzar lo urgente.

## 1. Marco

| Idea | Fuente | Rigor | Uso |
|---|---|---|---|
| Incertidumbre contra equivocidad: lo equívoco pide medios ricos | Daft y Lengel, 1986 (F-945) | 🟢 A, canónico; analogía fuera de su dominio | Predice que "¿me cubre?" irá al teléfono |
| Información clara migra; ambigua genera llamadas | Kumar y Telang, 2012 (F-850) | 🟢 A, causal | Aclarar antes de digitalizar |
| El autoservicio se juzga por si resuelve; si falla, se culpa a la empresa | Meuter et al., 2000 (F-946) | 🟢 A, canónico | Un flujo cortado es peor que ninguno |
| Buscar en un canal, cerrar en otro | Verhoef et al., 2007 (F-918) | 🟢 A, análogo de retail | Medir secuencias, no canales ganadores |
| Para solicitudes complejas, 34% prefiere tienda y 33% teléfono; correo 7% | Verint, 2016 (F-949) | 🟡 C, 🌐 | Confirma el patrón fuera de seguros |

## 2. Rol del canal por momento

| Momento | Rol | Evidencia clave |
|---|---|---|
| Consultar póliza, pagar, reembolso claro | Digital o automático | F-850, F-903, F-913, F-900 |
| Trámites y cambios de póliza | Se inicia en digital, lo cierra una persona | F-916 (aceptación de la IA cae a 16% al cancelar o renovar) |
| Avisar el siniestro | Teléfono o persona; digital para lo simple | F-947 (9% avisa en digital; −16 puntos), F-948 (44% teléfono, 10,5% app) |
| Seguir el siniestro | Digital proactivo | F-947 (+33 puntos con estado por app), F-872 |
| Siniestro complejo | Persona con apoyo digital | F-183 (falla 33% a 39% del siniestro 100% digital) |
| Urgencias (grúa, auxilio, médico) | Lo que despache más rápido; app si da ubicación exacta | F-951 (proveedor, sin método) |
| Renovación y baja | Sin evidencia pública sobre el canal | F-913 (efecto de la opción por defecto, indirecto) |

## 3. Siniestro: permanencia y voz del cliente

- **Permanencia.** F-890 (35% más probabilidad de cambio en 180 días), F-892 (86% satisfecho y 41% cambiaría),
  F-950 (17% cambió; pesan pérdida total con crédito, lesiones y primer siniestro). Todas de proveedores y de EE.UU.
- **Voz del cliente peruano.** El registro social rindió poco: solo categorías de reclamo (demora, monto, rechazo,
  plazo; F-959). El escalamiento a Indecopi o la SBS subió de 61,6 a 141 por cada 1.000 reclamos (F-902).
- **Regla de plazo.** 30 días desde la documentación completa para aceptar o rechazar sin ajustador; el silencio
  equivale a aceptación (F-907).
- **Pista sin evidencia.** Detección automática de choques por telemetría del teléfono (F-960, anuncio de proveedor).

## 4. Hipótesis vivas

| Código | Hipótesis | Estado | Cómo probarla |
|---|---|---|---|
| CS1 | El seguimiento proactivo del siniestro sube la satisfacción y baja las llamadas | 🟡 Asociación en EE.UU. (F-947, F-872) | Avisos de estado a la mitad de los siniestros de un mes, con grupo de control |
| CS2 | El aviso del choque por app no mejora la experiencia | 🟡 Una encuesta de 2017 (F-947) | Comparar satisfacción y tiempo a resolución por canal de aviso, ajustando por complejidad |
| CS3 | Una consulta "clara" con baja migración esconde una pregunta equívoca | 🔵 Inferida de F-850 y F-945 | Clasificar las llamadas de esa gestión por motivo real |
| CS4 | El canal del aviso pesa menos en la permanencia que la demora y el monto | 🟡 Proveedores (F-890, F-950) | Modelo de fuga tras siniestro con canal, tiempo y monto |

## 5. Vacíos

- Ningún estudio con grupo de control sobre el canal del siniestro en América Latina.
- Ninguna cifra pública de reparto de canales por gestión de otra aseguradora peruana.
- Conversación social peruana sobre el canal del siniestro.
- No se verificó si la SBS exige poder resolver el contrato por el mismo medio por el que se contrató.

## Conexiones

- [[valor-recurrencia-digital-seguros|Valor de la recurrencia digital en seguros]] — pregunta 1 del mismo
  benchmarking. Allí, el costo de servir y la confianza en el siniestro son teorías de valor; aquí se baja a qué
  canal sirve en cada momento.
- [[cliente-intermediado-bancaseguros-embebido|Cliente intermediado: banco, billetera, empleador y corredor]] —
  pregunta 3. Para el cliente intermediado, el siniestro es el principal momento de contacto directo.
- [[futuro-asesores-seguros-venta-digital|¿Desaparecerán los asesores de seguros?]] — la misma regla de
  complejidad, aplicada a la venta. Aquí se extiende al servicio y al siniestro.
- [[evaluacion-calidad-agentes-conversacionales-ia|Evaluación de agentes conversacionales de IA]] — si el
  seguimiento o el aviso se automatizan con un agente, cómo medir su calidad.
- [[intervenciones-adopcion-conducta|Intervenciones que cambiaron (o no) la adopción y la conducta]] — ver pagar un
  siniestro sostiene la recompra (F-990, F-896).
