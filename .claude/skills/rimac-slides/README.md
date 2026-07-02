# rimac-slides

Skill de Claude Code que genera **presentaciones HTML 16:9 on-brand de Rimac**, regidas por un único `design.md`. Es un fork de [frontend-slides](https://github.com/zarazhangrui/frontend-slides) del que conserva el **motor de render** (stage fijo, animaciones, edición inline, export PDF/Vercel, conversión PPT) y al que se le **quitó todo el menú de estilos**: acá no se elige un "vibe", hay **una sola marca**.

## Filosofía: tres capas

| Capa | Estado | Quién la define |
|---|---|---|
| **Marco** | 🔒 Bloqueado (uniforme) | Título (franja superior, color/tipografía/voz fijos), footer + branding, paleta, estética plano-seria, stage y motion — `design.md`, no se toca "para variar" |
| **Una idea por slide** | 🔒 Regla de contenido | Cada slide transmite un único mensaje, sintetizado en el título (voz corporativa de síntesis, sin punto final) |
| **Corazón** | 🆓 Libre — aquí vive la calidad | Cómo se **visualiza** la idea (texto / mixto / diagrama / dato / visual), con animación y recursos gráficos a medida |

> La consistencia la garantizan los **tokens** y el **marco** de `design.md`. La variedad no es de formato sino de **calidad**: marcos repetidos están bien; lo que no se repite es un corazón genérico cuando la idea pedía más (Principio de variedad — `design.md`).

## La única ley: `design.md`

[`design.md`](design.md) es la **fuente de verdad única** de todo lo visual — vive en este repo y es el archivo que se edita para actualizar la marca (junto con los `assets/`). El skill lo lee **completo y siempre** antes de generar; no hay nada hardcodeado en el motor que haya que perseguir. Cuando se actualiza `design.md` y se sube, el equipo recibe la nueva versión con `/plugin marketplace update` (ver abajo).

## Estructura

```
rimac-slides/
├── SKILL.md              ← el skill (orquestador)
├── design.md            ← la única ley de diseño (3 capas: marco + una idea + corazón)
├── viewport-base.css    ← motor: stage fijo 16:9 (incluir entero en cada deck)
├── html-template.md     ← motor: arquitectura HTML + controlador JS + edición inline
├── animation-patterns.md← registro de Motion Rimac + técnicas de animación
├── assets/              ← fuentes (BRSonoma, Rimac Display), logo SVG, wave, background
├── scripts/
│   ├── pack-assets.py   ← empaqueta fuentes/imágenes en base64 (deck portable)
│   ├── extract-pptx.py  ← conversión PPT → contenido
│   ├── deploy.sh        ← deploy a Vercel
│   └── export-pdf.sh    ← export a PDF
└── examples/
    ├── proof-rimac.html ← golden-sample de la marca (referencia, NO plantilla)
    └── lab-vanilla.html ← referencia de técnica de corazones animados (single-file embebido)
```

## Cómo acceder (para el equipo)

> **Prerrequisito:** este repo es **privado**. Pedile al dueño (`jlatorree`) que te agregue como **colaborador** en GitHub (*Settings → Collaborators*). Sin eso no vas a poder clonar ni instalar.

### Opción A — Claude Code, plugin privado (recomendado)
Este mismo repo es a la vez **marketplace privado** y plugin. Desde la terminal:
```
/plugin marketplace add jlatorree/rimac-slides
/plugin install rimac-slides@rimac-coe
```
Para recibir actualizaciones cuando cambie la marca: `/plugin marketplace update rimac-coe`.

### Opción B — Claude Cowork (la app)
Cowork instala desde un archivo **`.plugin`** (no usa el marketplace de GitHub). Descargá `rimac-slides.plugin` desde la pestaña **Releases** del repo y, en Cowork: **Customize → Plugins → Upload** → elegí el archivo. Para actualizar, te pasan un `.plugin` nuevo y lo volvés a subir.

### Opción C — Skill suelto (sin plugin)
Cloná el repo y copiá esta carpeta a `~/.claude/skills/rimac-slides/`. Funciona como skill, pero **sin actualización automática** (hay que re-copiar en cada cambio).

## Deck portable (importante)

Un deck que se comparte solo (sin la carpeta `assets/`) debe llevar **fuentes e imágenes embebidas en base64** — si no, las rutas `./assets/` dan 404 al moverlo y las fuentes caen a Helvetica. Corré:
```
pip install fonttools brotli Pillow
python scripts/pack-assets.py --assets ./assets --out ./build --wave-jpeg
```
y pegá la salida en el `<style>`/`<head>`. Meta: **0 ocurrencias de `./assets/`** en el HTML entregado. `examples/lab-vanilla.html` es un ejemplo ya embebido de referencia.

## Licencia

El **código y los archivos de skill** (SKILL.md, design.md, scripts, templates) son MIT (motor base heredado de frontend-slides). **Las fuentes de marca incluidas en `assets/fonts/` — BR Sonoma y Rimac Display — son propietarias y NO están bajo MIT**: se distribuyen acá solo para uso interno de Rimac bajo su propia licencia. Por eso este repo es **privado**: no redistribuir las fuentes fuera de Rimac.

## Crédito

Motor base: **frontend-slides** de [Zara Zhang](https://github.com/zarazhangrui/frontend-slides) (MIT). Capa de marca Rimac: CoE Diseño Estratégico.
