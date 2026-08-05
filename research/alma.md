# 00 — Hub de investigación (research/) — Rumipyramid/Machine_Learning

*Mapa maestro de los documentos de conocimiento del proyecto. Última actualización: 2026-08-05.*

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
| `_nodes/modelo-salud-ia-farmacias-peru.md` | Modelo de triage con IA + farmacias + atención humana (Perú): investigación, RE-AIM, estrategias de testeo | 2026-08-05 | v1.0 (revisión profunda de F-36/F-40/F-41/F-42 (2026-07-29): factor dominante de automedicación OR=29, ventana de adopción de telesalud, safety vs. exact-match en Omaolo; revisión profunda de F-43/F-44/F-50/F-53/F-54 (2026-08-05): por qué falla el symptom-checker japonés (enfermedad rara + presentación atípica, sin curva de aprendizaje), el argumento relacional de por qué precisión≠outcome, el defecto metodológico exacto de Babylon (datos de médicos simulando pacientes, no usuarios legos reales), y dos correcciones de cita/autoría — F-53 apuntaba en realidad a Holtrop et al. 2021 (13 malentendidos de RE-AIM + evolución a PRISM), F-54 es de Garner 2022, no "Kirchner", con la extensión DIeSEL) |
| `_nodes/mecanismos-seguros-salud.md` | Mecanismos de seguros de salud: presión demográfica/costo, balance financiero/rentabilidad global (incl. contraste Europa/Asia/Perú-Latam), y modelos que la navegan (global, comparativo) | 2026-07-22 | v1.2 (amplía con contraste regional del balance financiero) |
| `_nodes/material-visual-venta-consultiva.md` | Material visual en la venta consultiva: qué reduce la incertidumbre y facilita la elección (empírico + negocio + regulatorio; pista social sin cobertura) | 2026-07-21 | v1.1 (amplía con anclaje/regulatorio/confianza; aplicada a flyers Vida Ahorro) |
| `_nodes/transicion-venta-fria-a-opt-in.md` | Cómo transicionan las organizaciones de venta fría a venta opt-in (seguros y sectores análogos): disparadores, impacto en volumen, tácticas puente | 2026-07-14 | v1.0 |
| `_nodes/evaluacion-calidad-agentes-conversacionales-ia.md` | Escalas y frameworks para medir la calidad de un agente/chatbot de IA (usabilidad, métricas técnicas RAG, específicos de banca/seguros) | 2026-07-15 | v1.0 |
| `_nodes/behavioral-design-estado-disciplina.md` | Estado del behavioral design como disciplina/mercado + checklist para ser los mejores (seguros/Rimac) | 2026-07-29 | v1.1 (revisión profunda de F-23: UBI es RCT preregistrado con efecto sostenido en seguimiento, pero valida feedback+incentivo, no pricing dinámico real) |
| `_nodes/modelo-personas-sinteticas.md` | Cómo funciona y se calibra el modelo `lapuerta` (20 variables, v1.3) — excepción declarada de alcance, no mueve el código | 2026-07-20 | v1.0 |
| `_nodes/futuro-asesores-seguros-venta-digital.md` | ¿Desaparecerán los asesores de seguros? Automatización, venta 100% digital y el rol del intermediario (empírico + social + negocio); §3.7 amplía con casos de éxito comercial verificable en venta de vida 100% digital (Ethos, Bowtie) | 2026-07-27 | v1.0 (amplía §3.7, sin bump — afina la tesis, no la cambia) |
| `_nodes/proyecto-back-to-basics-ffvv-vida.md` | Proyecto Back to Basics — FFVV Vida Individual (RIMAC): conocimiento construido — Modelo de Experiencia de Venta Vida (deck al VP, Dx1-Dx3), mapa sistémico AS IS (9 frentes / 4 hallazgos operativos), estrategias de contacto (DS 016), playbook del asesor, encuesta a 19 asesores + Taller de Manejo de Objeciones, Universidad Vida, backlog Espejo/Transformación (ramo AMI), cruce con evidencia/tesis del Lobo, Plan Piloto de validación (10 asesores) | 2026-07-27 | v1.4 (deck low-fi para Milagros: origen del pedido, regla metodológica, hallazgos previos, evidencia McKinsey nueva, datos primarios de diagnóstico, alcance nuevo AMI, Felipe como colaborador no listado antes) |
| `_nodes/matriz-productos-vida-rimac.md` | Matriz de productos Vida RIMAC: catálogo de 3(+1) productos reales (VFP, Plan Vida Flexible, Vida Contigo, Vida Temporal Total), coberturas/addons, trazabilidad de fuentes y niveles de confianza — VCD digital/Endosable digital pendientes, no confirmados | 2026-07-26 | v1.2 |
| `_nodes/glosario-seguro-vida-peru.md` | Glosario de seguro de vida en lenguaje claro — FAQ de cliente (investigación `/trinidad`: pista empírica + social + negocio) para completar el Playbook del Asesor | 2026-07-24 | v1.0 |
| `_nodes/tendencias-diseno-innovacion.md` | **Node acumulativo** — Tendencias en **diseño e innovación**: qué tiene impacto tangible demostrado y qué es propuesta sin respaldo. 🎨 Diseño (producto/UX, IA, design systems, servicio, visual) + 💡 innovación (gestión de la innovación, innovation labs, difusión, ROI, insurtech). ⚠️ **Alcance ampliado y node renombrado el 2026-08-02** (antes `tendencias-diseno.md`; ver §0). Escala de madurez de evidencia, tablero de **31 hipótesis vivas**, **22 reglas de criterio** destiladas y bitácora de iteraciones | 2026-08-02 | **v4.0 (iteración 4)** — 💡 **apertura del dominio de innovación y prueba de transferencia de la tesis**: el vínculo I+D→desempeño es real, pequeño y mediado igual que diseño→desempeño (F-430); 4 cadenas de eco nuevas con la misma anatomía; y un defecto **peor** que el eco — el **huérfano de cita** (F-444: las cifras de fracaso del dominio no colapsan en *ninguna* fuente) → regla **C22**. ⭐ Con dos puntos donde innovación **supera** a diseño: se autocorrige sola (F-431/F-432 desmienten el mito del "80-95% de productos que fracasan" con 83.719 SKU reales) y aporta **el único RCT preregistrado de todo el node, y es de seguros** (F-442, UBI/telemática, N=1.449). La crisis del modelo se replica pero **le ocurre a otro eslabón**: muere la función interna (labs, CVC), sobrevive el proveedor externo fusionándose (H28). 5 hipótesis nuevas (H27-H31). F-430 a F-468. · *v3.0 (iteración 3)* — **la iteración en que el node se auditó a sí mismo**: el *impuesto de verificación* que la iter. 2 celebró **no tiene fuente primaria rastreable** (6.ª cadena de eco, y la primera propia) → **H19 degradada**; **H20 `respaldada`** con 13/13 (100%) de cifras hispanohablantes de emisores anglosajones interesados, tres atribuidas a un Gartner que nunca las publicó; **H5, H10, H11, H15 → `parcial`**; **H22 reformulada** (la industria no rota cifras, las acumula); desmentido oficial de MercadoLibre vuelve contestado el caso testigo de la iter. 2. 4 hipótesis nuevas (H23-H26), 3 reglas nuevas (C19-C21), 2 corregidas (C16, C17). F-399 a F-429 |
| `_nodes/venta-vida-digital-hibrida-latam.md` | Venta de seguros de vida en LATAM (Brasil, Chile, Colombia; excluye Perú): modelo digital vs. híbrido vs. tradicional y cómo performa cada uno — extensión regional de `futuro-asesores-seguros-venta-digital.md` | 2026-07-27 | v1.0 |

---

## Outputs activos

| Output | Construido sobre (nodes) | Última actualización | Estado |
|---|---|---|---|
| `_outputs/back-to-basics-presentacion-milagros-2026-07-23.md` — afirmaciones fortalecidas + estructura de deck para presentar Back to Basics (FFVV Vida Individual) | `transicion-venta-fria-a-opt-in`, `behavioral-design-estado-disciplina`, `material-visual-venta-consultiva`, `futuro-asesores-seguros-venta-digital`, `seguros-comportamiento-mundo-peru` | 2026-07-23 | al día |
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
