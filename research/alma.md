# 00 — Hub de investigación (research/) — Rumipyramid/Machine_Learning

*Mapa maestro de los documentos de conocimiento del proyecto. Última actualización: 2026-08-18.*

Este archivo es el **índice vivo** de `research/`: la vista **global** de qué está vigente y qué
deriva de qué. Como `_nodes/` es plano (sin carpetas por tema), la navegación no la dan las
carpetas: la dan este `alma.md` y la vista **local** de cada node, en su sección
`## Conexiones`.

> **Alcance de este hub**: cubre el conocimiento de investigación de `research/` (seguros, salud,
> Perú). **No** cubre `research/personas/` (subsistema de código del generador de personas
> sintéticas — schema JSON + matriz + scripts, ya estructurado y referenciado en `CLAUDE.md`) ni
> `research/updates/` (reportes quincenales, ya estructurado y auto-indexado en `CLAUDE.md`) —
> con una excepción declarada: `_nodes/modelo-personas-sinteticas.md` cuenta la historia
> *conceptual* del modelo (que no vivía en un solo doc) sin mover ni duplicar el código/schema,
> que sigue exactamente donde estaba.

---

## Reglas de gestión (las cinco consignas)

**1. Una fuente de verdad por tema.** Cada tema es un solo node en `_nodes/`. No se duplica
contenido entre nodes.

**2. Versionado solo por cambio estructural.** La versión sube solo ante un cambio de fundamento
(premisa, modelo, arquitectura, alcance). Lo incremental solo actualiza la fecha.

**3. Hub como mapa.** Este archivo es el único lugar donde se ve qué nodes están vigentes, cuándo
se actualizaron y qué output deriva de cuáles.

**4. Los outputs citan sus nodes-fuente.** "Basado en `node.md` (versión del YYYY-MM-DD)" + citas
por afirmación cuando corresponda.

**5. Conexiones explícitas y recíprocas en wikilinks.** Cada node cierra con `## Conexiones`
(`[[...]]`, con alias). Si A enlaza a B, B enlaza a A.

---

## Estructura de carpetas

| Ruta | Contenido |
|---|---|
| `alma.md` | Este índice vivo (raíz de `research/`) |
| `_nodes/` | Todo el conocimiento, plano, un `.md` por tema (kebab-case) |
| `fuentes/codice.md` | Ledger de `cronista` (se consulta con `/codice`) — bibliografía compartida de todos los nodes, citada por ID (`F-n`). No se movió a `_nodes/` porque `cronista` referencia esta ruta en su propio SKILL.md y en las 235+ filas existentes. |
| `personas/` | Subsistema de código del modelo de personas sintéticas (`lapuerta`) — fuera del alcance de este hub, ver `CLAUDE.md` |
| `updates/` | Reportes quincenales de fortalecimiento del modelo — fuera del alcance de este hub, ver `CLAUDE.md` |
| `lobo/opinion_experto.md` | Opinión de negocio acumulada del skill `lobo`, refinada diariamente contra el ledger de `cronista` — subsistema con su propia lógica de confianza/tope, fuera del alcance de este hub, ver `CLAUDE.md` |
| `yopersona/perfil.md` | Perfil profesional del usuario (CV) — fuente de verdad para cartas de presentación y asesoría de carrera, fuera del alcance de este hub, ver `CLAUDE.md` |

`_nodes/` es plano: nada de subcarpetas por tema.

---

## Nodes vigentes

| Documento | Tema | Última actualización | Versión |
|---|---|---|---|
| `_nodes/seguros-comportamiento-mundo-peru.md` | Comportamiento, percepción y mercado global de seguros (Mundo vs. Perú) | 2026-07-21 | v1.1 |
| `_nodes/glosario-seguro-salud-peru.md` | Glosario de términos de seguro de salud en lenguaje claro (Perú) | 2026-07-21 | v1.0 |
| `_nodes/modelo-salud-ia-farmacias-peru.md` | Modelo de triage con IA + farmacias + atención humana (Perú): investigación, RE-AIM, estrategias de testeo — **su §4 se reutilizó el 2026-08-14 como base del diseño de validación del copiloto AIDA**, ver `diagnostico-copiloto-ai-asesor-vida-rimac` §12 | 2026-08-12 | v1.0 (revisión profunda de F-36/F-40/F-41/F-42 (2026-07-29): factor dominante de automedicación OR=29, ventana de adopción de telesalud, safety vs. exact-match en Omaolo; revisión profunda de F-43/F-44/F-50/F-53/F-54 (2026-08-05): por qué falla el symptom-checker japonés, el argumento relacional de por qué precisión≠outcome, el defecto metodológico exacto de Babylon, y dos correcciones de cita/autoría — F-53→Holtrop et al. 2021, F-54→Garner 2022; revisión profunda de F-55/F-56/F-57/F-58/F-59 (2026-08-12, §4 estrategias de testeo): E1 silent trial sin guías formales todavía y caso de colapso de AUC 0.90→0.50 por distribution shift; E2 resultados reales del ejemplo de Curran tipo 2 (Cully et al. 2017: 50% vs 32.8% de respuesta, efecto modesto y desigual por subgrupo) + corrección de autoría F-55 (Cully, no "Bauer"); E3 el stepped-wedge está en mayor riesgo de sesgo que el paralelo-CRT según Hemming & Taljaard y su ventaja ética es objeto de controversia académica activa (Kotz et al. 2012 vs. Mdege et al. 2011) — tres URLs bloqueadas por el proxy de red del entorno, reconstruido vía búsqueda dirigida) |
| `_nodes/mecanismos-seguros-salud.md` | Mecanismos de seguros de salud: presión demográfica/costo, balance financiero/rentabilidad global (incl. contraste Europa/Asia/Perú-Latam), y modelos que la navegan (global, comparativo) | 2026-07-22 | v1.2 (amplía con contraste regional del balance financiero) |
| `_nodes/material-visual-venta-consultiva.md` | Material visual en la venta consultiva: qué reduce la incertidumbre y facilita la elección (empírico + negocio + regulatorio; pista social sin cobertura) | 2026-07-21 | v1.1 (amplía con anclaje/regulatorio/confianza; aplicada a flyers Vida Ahorro) |
| `_nodes/transicion-venta-fria-a-opt-in.md` | Cómo transicionan las organizaciones de venta fría a venta opt-in (seguros y sectores análogos): disparadores, impacto en volumen, tácticas puente | 2026-07-14 | v1.0 |
| `_nodes/evaluacion-calidad-agentes-conversacionales-ia.md` | Escalas y frameworks para medir la calidad de un agente/chatbot de IA (usabilidad, métricas técnicas RAG, específicos de banca/seguros); §6 actualiza el **método de juez LLM al estado 2026** — el sesgo de estilo resulta dominante y el de posición marginal, y la calibración humana pasa a ser obligatoria | 2026-08-14 | v1.1 |
| `_nodes/behavioral-design-estado-disciplina.md` | Estado del behavioral design como disciplina/mercado + checklist para ser los mejores (seguros/Rimac) | 2026-07-29 | v1.1 (revisión profunda de F-23: UBI es RCT preregistrado con efecto sostenido en seguimiento, pero valida feedback+incentivo, no pricing dinámico real) |
| `_nodes/modelo-personas-sinteticas.md` | Cómo funciona y se calibra el modelo `lapuerta` (20 variables, v1.3) — excepción declarada de alcance, no mueve el código | 2026-07-20 | v1.0 |
| `_nodes/futuro-asesores-seguros-venta-digital.md` | ¿Desaparecerán los asesores de seguros? Automatización, venta 100% digital y el rol del intermediario (empírico + social + negocio); §3.7 amplía con casos de éxito comercial verificable en venta de vida 100% digital (Ethos, Bowtie) | 2026-07-27 | v1.0 (amplía §3.7, sin bump — afina la tesis, no la cambia) |
| `_nodes/proyecto-back-to-basics-ffvv-vida.md` | Proyecto Back to Basics — FFVV Vida Individual (RIMAC): conocimiento construido — Modelo de Experiencia de Venta Vida (deck al VP, Dx1-Dx3), mapa sistémico AS IS (9 frentes / 4 hallazgos operativos), estrategias de contacto (DS 016), playbook del asesor, encuesta a 19 asesores + Taller de Manejo de Objeciones, Universidad Vida, backlog Espejo/Transformación (ramo AMI), cruce con evidencia/tesis del Lobo, Plan Piloto de validación (10 asesores) | 2026-08-14 | **v1.6** (§1.1 declara qué clase de objeto es el Modelo de Venta: **modelo de referencia transversal** — normativo, transversal y **generativo** (emite requerimientos de producto cuando no hay match) —, sus **4 frentes de instanciación** y la regla de **una fuente canónica, N instanciaciones**. v1.5 — desconflación de AIDA y el prototipo del piloto: AIDA es la herramienta **de Copilot ya desplegada**, el prototipo sobre **Claude** es el del Plan Piloto — corrige un error que v1.2 había introducido y propagado a §2 y §8; el Plan Piloto además cambió, §8 pasa a ser histórico. v1.4 — deck low-fi para Milagros: origen del pedido, regla metodológica, hallazgos previos, evidencia McKinsey nueva, datos primarios de diagnóstico, alcance nuevo AMI, Felipe como colaborador no listado antes) |
| `_nodes/matriz-productos-vida-rimac.md` | Matriz de productos Vida RIMAC: catálogo de 3(+1) productos reales (VFP, Plan Vida Flexible, Vida Contigo, Vida Temporal Total), coberturas/addons, trazabilidad de fuentes y niveles de confianza — VCD digital/Endosable digital pendientes, no confirmados | 2026-07-26 | v1.2 |
| `_nodes/glosario-seguro-vida-peru.md` | Glosario de seguro de vida en lenguaje claro — FAQ de cliente (investigación `/trinidad`: pista empírica + social + negocio) para completar el Playbook del Asesor | 2026-07-24 | v1.0 |
| `_nodes/tendencias-diseno-innovacion.md` | **Node acumulativo** — Tendencias en **diseño e innovación**: qué tiene impacto tangible demostrado y qué es propuesta sin respaldo. 🎨 Diseño (producto/UX, IA, design systems, servicio, visual) + 💡 innovación (gestión de la innovación, innovation labs, difusión, ROI, insurtech). ⚠️ **Alcance ampliado y node renombrado el 2026-08-02** (antes `tendencias-diseno.md`; ver §0). Escala de madurez de evidencia, tablero de **31 hipótesis vivas**, **22 reglas de criterio** destiladas y bitácora de iteraciones | 2026-08-02 | **v4.0 (iteración 4)** — 💡 **apertura del dominio de innovación y prueba de transferencia de la tesis**: el vínculo I+D→desempeño es real, pequeño y mediado igual que diseño→desempeño (F-430); 4 cadenas de eco nuevas con la misma anatomía; y un defecto **peor** que el eco — el **huérfano de cita** (F-444: las cifras de fracaso del dominio no colapsan en *ninguna* fuente) → regla **C22**. ⭐ Con dos puntos donde innovación **supera** a diseño: se autocorrige sola (F-431/F-432 desmienten el mito del "80-95% de productos que fracasan" con 83.719 SKU reales) y aporta **el único RCT preregistrado de todo el node, y es de seguros** (F-442, UBI/telemática, N=1.449). La crisis del modelo se replica pero **le ocurre a otro eslabón**: muere la función interna (labs, CVC), sobrevive el proveedor externo fusionándose (H28). 5 hipótesis nuevas (H27-H31). F-430 a F-468. · *v3.0 (iteración 3)* — **la iteración en que el node se auditó a sí mismo**: el *impuesto de verificación* que la iter. 2 celebró **no tiene fuente primaria rastreable** (6.ª cadena de eco, y la primera propia) → **H19 degradada**; **H20 `respaldada`** con 13/13 (100%) de cifras hispanohablantes de emisores anglosajones interesados, tres atribuidas a un Gartner que nunca las publicó; **H5, H10, H11, H15 → `parcial`**; **H22 reformulada** (la industria no rota cifras, las acumula); desmentido oficial de MercadoLibre vuelve contestado el caso testigo de la iter. 2. 4 hipótesis nuevas (H23-H26), 3 reglas nuevas (C19-C21), 2 corregidas (C16, C17). F-399 a F-429 |
| `_nodes/venta-vida-digital-hibrida-latam.md` | Venta de seguros de vida en LATAM (Brasil, Chile, Colombia; excluye Perú): modelo digital vs. híbrido vs. tradicional y cómo performa cada uno — extensión regional de `futuro-asesores-seguros-venta-digital.md` | 2026-07-27 | v1.0 |
| `_nodes/diagnostico-copiloto-ai-asesor-vida-rimac.md` | Diagnóstico del Copiloto AI del asesor de Vida (RIMAC) — proyecto **asociado** a Back to Basics: brief ordenado en 4 frentes, taxonomía de 3 capas de falla (conocimiento / instrucciones / plataforma) con la prueba que las separa, protocolo para documentar fallas sobre los instrumentos ya existentes, criterio de priorización de capacidades del copiloto respaldado por evidencia (F-476 a F-478), 10 preguntas abiertas y plan de trabajo | 2026-08-14 | **v2.0** (§16 fija la **estructura definitiva del Release 1 en tres etapas** — diagnóstico de la herramienta · intervención · testeo —, suma la **velocidad** como segundo objetivo y nombra el "full con puntos de corte" como **serie temporal interrumpida**, cuya serie de control ya existe gratis en los ramos no intervenidos. Abre P10, el "modelo SHUNK" sin identificar. v1.9 (§15 integra el research de Felipe y produce el Release 1. v1.8 (§14 **evaluación del Playbook del Asesor** como fuente canónica: contiene las contradicciones que debía resolver — duplica Vida Contigo/VAG, omite VFP, usa el nombre desactualizado "Flexivida" —, lo que **corrige H3**: AIDA probablemente reproduce el playbook en vez de estar anclada a 2022. Confirma P8 y produce una predicción falsable sobre B2-B4. v1.7 (§12 diseño de validación de los fixes: **dos experimentos, no uno**, con la re-corrida del banco como compuerta, estratificación por antigüedad obligatoria y escalonado con su controversia declarada; §13 **trabajo de campo con asesores**: el campo alimenta el banco de preguntas en vez de seguirlo, se pregunta por incidentes concretos y no por opiniones (F-488 sobre F-257), y se nombra lo que ninguna telemetría cubre — **qué dejaron de preguntar**. v1.5 (§11 auto-interrogación de AIDA: es **multi-ramo, no de Vida**; el ruteo que se iba a recomendar **ya existe**; productos declarados que no coinciden con el portafolio vigente; ⚠️ **`transfer_to_agent` es de Google ADK** — los límites de Copilot quedan en suspenso hasta confirmar; nueva **capa D · Ruteo** en la taxonomía. v1.4 (§9.2 corregida — **el modelo de venta ES la fuente canónica**, la base de AIDA debe ser una derivación suya, no una carpeta; §10 **barrera de actualización de producto**: piso regulatorio SBS irreducible vs. capa comercial acelerable, hoy acopladas, y la dirección de traducción invertida — la matriz debe ser fuente, no destino. v1.3: §9 **la contradicción aguas arriba**: un copiloto no arbitra fuentes que se contradicen, las oculta — la inconsistencia reportada de AIDA puede ser la de la organización reflejada; agrega el paso F2b de detección de contradicciones y corrige la lectura estrecha de "multimodal" de v1.2. v1.2: §2.1 mapa real de **6 frentes** del asesor y **3 agentes de IA ya desplegados** — AIDA, suscripción, Sales Coach —, lo que reancla el diagnóstico de Dx3 a **Dx2**; §8 nueva: resuelve si el copiloto debe concentrar todos los frentes separando distribución / interfaz / recuperación. v1.1: fija AIDA (Copilot, desplegada) como objeto y corrige la fuente de insumos de F1, que v1.0 había asignado al prototipo de Claude) |
| `_nodes/arquitectura-conocimiento-agentes-copilot.md` | Cómo debe almacenarse la información para que un agente de Copilot la consuma: matriz de formatos (qué consume, qué degrada, qué es invisible), los tres techos (licencia 7 MB vs. 200 MB, 36.000 caracteres por archivo, ≤300 páginas totales), 7 reglas de redacción — **sin tablas**, encabezados, un tema por documento —, capa de gobierno/ROT y protocolo de auditoría de 7 pasos; §8 **uno o varios agentes** — consolidar la interfaz sí, consolidar las bases no; **§7 corregido: la cuantificación que declaraba inexistente sí existe** (F-490 a F-492). Evidencia F-469 a F-475, F-479, F-480, F-489 a F-494 | 2026-08-14 | v1.2 |

---

## Outputs activos

| Output | Construido sobre (nodes) | Última actualización | Estado |
|---|---|---|---|
| `_outputs/back-to-basics-presentacion-milagros-2026-07-23.md` — afirmaciones fortalecidas + estructura de deck para presentar Back to Basics (FFVV Vida Individual) | `transicion-venta-fria-a-opt-in`, `behavioral-design-estado-disciplina`, `material-visual-venta-consultiva`, `futuro-asesores-seguros-venta-digital`, `seguros-comportamiento-mundo-peru` | 2026-07-23 | al día |
| `_outputs/estrategia-diagnostico-aida-2026-08-14.html` — **estrategia consolidada de diagnóstico de AIDA** (v2.0, publicada también como artifact compartible): objeto y alcance, los **4 niveles de confianza de la evidencia** (verificado / declarado / deducido / hipótesis), la **cadena causal de 5 eslabones a falsar** con su prueba cada uno, la **taxonomía de 4 capas de falla** incl. la capa D · Ruteo, los 4 frentes con estado, la secuencia en 4 fases con compuertas, **§07 el trabajo de campo con asesores** (incidente crítico en vez de opiniones; el campo alimenta el banco de preguntas, no lo sigue) · **§09 el diseño de validación de los fixes** (dos experimentos, no uno; estratificación por antigüedad obligatoria; escalonado con su controversia declarada), y los riesgos de la propia estrategia | `diagnostico-copiloto-ai-asesor-vida-rimac` (v1.5), `arquitectura-conocimiento-agentes-copilot` (v1.1), `evaluacion-calidad-agentes-conversacionales-ia` (v1.1), `matriz-productos-vida-rimac`, `proyecto-back-to-basics-ffvv-vida` (v1.6) | 2026-08-14 | al día |
| `_outputs/aida-dossier-y-plan-faseado.md` — **dossier completo de AIDA + plan de intervención faseado** (v2.0). Documento de consolidación en 26 secciones: qué es AIDA (plataforma, alcance, las 3 funciones declaradas y su estado real, los 6 frentes, los agentes y los 2 prototipos) · el diagnóstico (taxonomía de 4 capas, la biblioteca, la evaluación del Playbook, por qué ordenar rinde más que reentrenar, la contradicción aguas arriba, la barrera de producto, qué debe hacer el asesor, las 6 restricciones duras) · **el plan en 5 fases + 1 paralela** con requisito de entrada por fase · los instrumentos y el diseño de validación · P1-P15 · insumos con las 4 cifras excluidas. ⚠️ **No es fuente de verdad** — la consolida desde los nodes, que mandan ante discrepancia. ⭐ Corrige que la evaluación de formato del Playbook estaba medida contra un techo de Copilot que ya no aplica | consolida `diagnostico-copiloto-ai-asesor-vida-rimac` (v2.2), `arquitectura-conocimiento-agentes-copilot` (v1.3), `_outputs/release-1-base-conocimiento-aida.md` (v2.2) y `_outputs/protocolo-interrogacion-aida-vida.md` (v0.4) | 2026-08-19 | al día |
| `_outputs/presentacion-aida-owners-2026-08-19.html` — **presentación para los dueños de la capacidad** (Emanuel, Will, Miguel Portugal), 11 slides on-brand del CoE. Estructura fijada por la jefatura: de dónde venimos · **las 3 funciones que AIDA declara** (documentación + auto-descripción, para no confrontar a la PO) · los 3 instrumentos de verificación · **la brecha función por función** · la adopción que no mide utilidad · la conducta compensatoria · la biblioteca como causa · los 6 arreglos · **el pedido: co-crear la matriz de priorización** · las 3 cosas que se piden de vuelta. ⚠️ Auditoría estructurada y shadowing en curso: las láminas 5 y 6 se cierran con esos resultados | deriva de `diagnostico-copiloto-ai-asesor-vida-rimac` §18 y `_outputs/release-1-base-conocimiento-aida.md` | 2026-08-19 | al día |
| `_outputs/release-1-aida-presentable-2026-08-14.html` — **versión presentable del Release 1** (v3, publicada como artifact compartible `0bb009a6`): el mismo alcance en lenguaje llano, pensada para leerse en una reunión con Producto, TI o dirección de canal. **v3 (2026-08-18)** agrega citación **(Autor, año)** en línea, la sección **Insumos** (primarios internos + secundarios externos, con lo que quedó deliberadamente fuera), **las fases siguientes** —incluida la Fase 4 de **prototipado de capacidades**— y reformula *qué queda afuera* como **qué no entra ahora y adónde va**. La versión extendida en `.md` sigue siendo la fuente de verdad | deriva de `_outputs/release-1-base-conocimiento-aida.md` | 2026-08-18 | al día |
| `_outputs/release-1-base-conocimiento-aida.md` — **Release 1 de las intervenciones en AIDA (Vida)**, v2.1 **en tres etapas** (diagnóstico con asesores + evaluación asistida por LLM · intervención en la base · testeo contra línea base o A/B): alcance ejecutable en 5 entregables (resolver el catálogo · sacar del índice lo que no debe responder · cargar el cuerpo canónico derivado · reescribir los cuadros más consultados · banco de control con medición del antes), inventario como entregable cero, qué va a fases siguientes, el riesgo de adopción que puede anularlo entero, y lo que no arregla. Integra el research de Felipe con el diagnóstico. **v2.1 (2026-08-18)**: §5 reformulado como **qué no entra ahora y adónde va** (cada diferido con destino), **§5.1 las fases siguientes** (Fase 2 extensión · Fase 3 motor · **Fase 4 prototipar capacidades antes de construirlas**, que le da rol al prototipo Claude como banco de prototipado · Fase 5 arquitectura de agentes · paralelo de reintroducción) y **§9 Insumos** con la trazabilidad completa | `diagnostico-copiloto-ai-asesor-vida-rimac` (v1.9), `arquitectura-conocimiento-agentes-copilot` (v1.2), `matriz-productos-vida-rimac`, Playbook y research de Felipe en `_fuentes_internas/` | 2026-08-18 | al día |
| `_outputs/protocolo-interrogacion-aida-vida.md` — instrumento de diagnóstico de AIDA (ramo Vida): auto-interrogación de arquitectura, banco de preguntas de calidad calificado contra la matriz de productos, y pruebas de ruteo entre ramos. **v0.2** agrega el **Bloque D — Claude como auditor** con el método de juez LLM (Zheng et al. 2023 / G-Eval, F-159/F-156) actualizado a 2026 (F-485 a F-487): calificación guiada por referencia contra la matriz, mitigación del sesgo de estilo (el dominante), y calibración humana obligatoria con κ de Cohen por criterio | `diagnostico-copiloto-ai-asesor-vida-rimac`, `evaluacion-calidad-agentes-conversacionales-ia`, `matriz-productos-vida-rimac`, `arquitectura-conocimiento-agentes-copilot` | 2026-08-14 | al día |
| `_outputs/guia-triaje-200-usuarios-sinteticos-2026-08-05.md` — simulación de la "Guía de preguntas" (estudio de triaje digital + kit) sobre 200 usuarios sintéticos `lapuerta` (18-65, NSE A/B/C). ⚠️ Parcial: 8 de 16 preguntas quedaron sin responder porque el prototipo no fue alcanzable desde el entorno | `modelo-salud-ia-farmacias-peru`, `modelo-personas-sinteticas`, `futuro-asesores-seguros-venta-digital` | 2026-08-05 | al día |

> **Estado**: `al día` o `requiere refresh`.

---

## Documentos pendientes de crear

- _(vacío)_

---

## Bibliografía compartida

`fuentes/codice.md` (ledger de `cronista`, mantenido por ese skill; se consulta con el skill
`/codice`) — 235+ fuentes (F-1...) citadas por ID desde cualquier node. Reglas de uso desde
este hub:

- Cada node cita fuentes por ID (`F-n`) en vez de repetir la referencia completa.
- Al crear/actualizar un node con evidencia nueva, registrar la fuente en el ledger primero
  (skill `cronista`), luego citarla por ID en el node.

**Nota de reconciliación (2026-07-17):** el PR de esta rama divergió de `main` — `main` nunca
recibió la migración a Many Brains y avanzó en paralelo (skill `lobo`, `yopersona`, skill
`contexto-peruano`, marketplace de plugins, e investigación propia de behavioral design con
IDs F-16 a F-27 del ledger). Al reconciliar: los flat files que `main` mantenía
(`seguros_comportamiento_mundo_peru.md`, `glosario_seguro_salud_peru.md`) eran superset-subset
exactos de los nodes ya migrados — se descartaron sin pérdida de contenido.
`behavioral_design_360.md` era investigación nueva y real — se migró como
`_nodes/behavioral-design-estado-disciplina.md`, conservando sus IDs F-16 a F-27 sin cambio.
Los IDs F-16 a F-27 que esta rama había asignado a otra investigación (rentabilidad P/C,
telemática, seguros paramétricos) se renumeraron a F-160 a F-171 para no chocar — ver ledger.

**Segunda reconciliación (2026-07-20):** `main` siguió evolucionando el layout viejo en
paralelo tras la primera reconciliación (nunca recibió el merge, sigue sin `alma.md`/`_nodes/`).
El ledger (renombrado `registro_fuentes.md`→`codice.md` el 2026-07-19) solo recibió cambios
cosméticos de `main` (formato `[[wikilink]]`, sin filas nuevas) — se conservó la versión de esta
rama, ya migrada. De paso se corrigió una referencia obsoleta que había quedado de la primera
reconciliación: F-16 a F-27 en `codice.md` seguían apuntando a `research/behavioral_design_360.md`
(ruta pre-migración) en vez de `research/_nodes/behavioral-design-estado-disciplina.md`.

---

## Cómo se mantiene este hub

`/seeker` y `/trinidad` escriben directamente a `_nodes/` al terminar una investigación (ver regla
en `CLAUDE.md`), no solo responden en el chat. El agente mantiene este hub en cada sesión:
actualiza fechas/versiones al tocar nodes, agrega filas nuevas al crear/mover/renombrar, y
actualiza la fecha de cabecera con cada cambio.
