# Machine_Learning

Repositorio de proyectos de Machine Learning y **bóveda de conocimiento** del proyecto.
Este README es el mapa de entrada; el códice persistente vive en [`CLAUDE.md`](CLAUDE.md).

## Mapa de la bóveda

| Carpeta / archivo | Qué hay |
|---|---|
| [`CLAUDE.md`](CLAUDE.md) | **Códice**: índice y memoria del proyecto (lo carga Claude al iniciar). |
| [`research/`](research/) | Investigación y modelo de personas sintéticas (ver su [README](research/README.md)). |
| [`.claude/skills/`](.claude/skills/) | Skills compartibles: **`/lapuerta`** (generar/simular) y **`/cerrajero`** (reporte quincenal). |
| [`.github/workflows/`](.github/workflows/) | Action programado que genera el reporte quincenal del modelo. |
| `Proyecto_ML_1.ipynb` | Notebook de ML. |
| `Self driving car/` | Proyecto de simulación de auto autónomo. |

## Líneas de trabajo

### 🔬 Investigación de seguros (Perú)
Comportamiento, percepción y valoración de seguros (Mundo vs. Perú), con un **modelo de
usuarios sintéticos** calibrado a datos reales (SBS, APESEG, APEIM). Incluye matriz de
variables, generador, láminas explicativas y apps web. → [`research/`](research/)

### 🧩 Skills
- **`/lapuerta`** — genera y consulta usuarios sintéticos de seguros; simula respuestas
  (por reglas o con LLM). Autocontenido y compartible.
- **`/cerrajero`** — ejecuta a demanda la actualización quincenal del modelo (investiga,
  redacta el reporte y lo indexa en el códice).

### 🚗 Self driving car
Simulación con red neuronal (`Self driving car/`).

## Convenciones
- Artefactos generados (CSV de muestra, ZIP, `__pycache__`, `dist/`) **no** se versionan.
- La fuente de verdad del modelo está en `research/personas/generador/`; el skill `lapuerta`
  lleva su propia copia autocontenida para compartir.
