# research/ — Investigación y modelo de personas sintéticas

Índice de la carpeta de investigación de seguros (Perú) y del modelo de usuarios sintéticos.

## Contenido

| Ruta | Qué es |
|---|---|
| [`seguros_comportamiento_mundo_peru.md`](seguros_comportamiento_mundo_peru.md) | Investigación base: comportamiento, percepción y valoración de seguros (Mundo vs. Perú), con fuentes. |
| [`instrucciones_claude_equipo_research.md`](instrucciones_claude_equipo_research.md) | Instrucciones base (transversales y anti-sesgo) para configurar a Claude como asistente del equipo de research/diseño. |
| [`personas/generador/`](personas/generador/) | **Fuente de verdad del modelo**: generador, esquema, matriz y dataset de ejemplo. |
| [`personas/laminas/`](personas/laminas/) | Lámina explicativa del sistema (script `build_lamina_detalle.py` + PNG). |
| [`personas/apps/reglas/`](personas/apps/reglas/) | App web autocontenida: preguntas por reglas (gráficos + insights), sin servidor. |
| [`personas/apps/llm/`](personas/apps/llm/) | App de preguntas libres respondidas por Claude (backend Flask + API). |
| [`updates/`](updates/) | Reportes quincenales de fortalecimiento + `generate_report.py` (usado por el Action). |

## Modelo de personas sintéticas — `personas/generador/`

- `generate_synthetic_users.py` — generador (solo stdlib).
  - `python research/personas/generador/generate_synthetic_users.py --n 1000 --out usuarios.csv --seed 42`
- `synthetic_user_schema.json` — distribuciones calibradas (editable; cada variable marca `dato`/`supuesto`).
- `matriz_usuarios_sinteticos.md` — matriz completa, grafo de dependencias y arquetipos.
- `usuarios_sinteticos_ejemplo.csv` — muestra de 200 perfiles.

> El skill **`/lapuerta`** (`.claude/skills/lapuerta/`) lleva una copia autocontenida de estos
> activos + el motor de simulación por reglas, para compartir sin depender del repo.

## Reportes quincenales — `updates/`

Generados a demanda con el skill **`/cerrajero`** o de forma desatendida por el GitHub Action
(`.github/workflows/fortalecimiento-modelo.yml`). El índice de reportes se mantiene en
[`CLAUDE.md`](../CLAUDE.md).

## Nota
Datos sintéticos: no representan personas reales. Para prototipado, exploración de hipótesis y
diseño de mensajes; no sustituyen una encuesta de mercado.
