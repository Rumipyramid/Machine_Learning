# CLAUDE.md — Codex de conocimiento del proyecto

Bóveda persistente que Claude Code carga al iniciar cualquier sesión sobre
`Rumipyramid/Machine_Learning`. Índice único de qué hay, dónde está y cómo se usa.

## 🗺️ Mapa de archivos

| Ruta | Qué es | Uso / notas |
|---|---|---|
| `Proyecto_ML_1.ipynb` | Notebook principal de ML | Origen Colab |
| `Self driving car/` | Simulación de auto autónomo (Pygame + red neuronal) | Entrada: `self driving car.py`; config en `config_file.txt` |
| `research/seguros_comportamiento_mundo_peru.md` | Investigación base: comportamiento/percepción de seguros (Mundo vs. Perú) | Fuentes OECD, McKinsey, EY, Bain, Swiss Re, APESEG, SBS… |
| `research/glosario_seguro_salud_peru.md` | Glosario de seguro de salud en Perú en lenguaje claro (definición + ejemplo + malentendido típico) | Derivado de investigación /seeker; alineado a glosario SBS |
| `research/revision_conductual_modelo_venta.md` | Revisión conductual del modelo de venta RIMAC: secciones corregidas con sesgos/frameworks acotados a lo respaldado por evidencia | Reemplazos drop-in para el doc original; fuentes F-16..F-25 |
| `research/sistema_aprendizaje_universidad_vida.md` | Diseño de sistema de aprendizaje para asesores (Universidad Vida): 5 capas basadas en ciencia del aprendizaje (transferencia, espaciamiento, evaluación, motivación) | Acota frameworks sin evidencia (70-20-10, estilos); fuentes F-26..F-34 |
| `research/mapa_competencias_asesor.md` | Mapa de competencias del asesor (Capa 0): dominios C1–C7 atados a los 4 pasos del perfilador, niveles de maestría N1–N4 y matriz de cobertura | Base para compuertas de maestría, escalera de crecimiento y evaluación Nivel 3 |
| `research/calendario_cohorte_12_semanas.md` | Calendario de cohorte de 12 semanas (Capa 1): secuencia C1→C6 espaciada, recuperación, bucle de aplicación y compuertas de maestría hasta certificación N2 | Plantilla adaptable; cadencia de quizzes/role-plays/coaching |
| `research/personas/matriz_usuarios_sinteticos.md` | Matriz legible: variables, distribuciones, grafo causal, arquetipos | Deriva de la investigación base |
| `research/personas/synthetic_user_schema.json` | Esquema machine-readable de la matriz | Lo consume el generador |
| `research/personas/generate_synthetic_users.py` | Generador de perfiles sintéticos (solo stdlib) | `python … --n 1000 --out usuarios.csv --seed 42` |
| `research/personas/datasets/usuarios_sinteticos_ejemplo.csv` | 200 filas — ejemplo de referencia del generador | — |
| `research/personas/datasets/muestra_22_usuarios.csv` | 22 filas — simulación de pregunta abierta | — |
| `research/personas/datasets/grupo_nse_A.csv` | 10 filas — grupo NSE A (simulación de opinión RIMAC) | — |
| `research/fuentes/registro_fuentes.md` | Ledger de evidencia: resumen breve, rigurosidad metodológica, autor y año por fuente | Lo mantiene el skill `cronista` (trazabilidad de fuentes) |
| `.claude/skills/cronista/SKILL.md` | Skill `cronista`: archivero de fuentes del códice | Se dispara al usar evidencia referenciable para crear/fundamentar |
| `.claude/skills/seeker/SKILL.md` | Skill `seeker`: investigación de espectro amplio | Se invoca con `/seeker` tras preguntas de investigación; cruza registros empíricos y teóricos |

## 📊 Datos clave — seguros (Perú vs. Mundo)

- **Penetración:** Perú ~**2.08%** del PBI · LatAm 3.2% · Chile 4.6%. CAGR ~12% (2026-2031).
- **Confianza:** plena ~**23-25%**; ~**48% desconfía** (causa #1: falta de información).
  Global cross-industria ~39%. El **broker eleva la confianza** (intermediación).
- **Tenencia:** ~**4/10** tiene/tuvo seguro en 2 años. SOAT conocido por **94%**.
- **Desastres naturales:** solo ~**3.3% de hogares** asegurados, en país altamente sísmico.
- **Brecha de protección global:** ~**US$1.8 billones**; 60% de pérdidas por catástrofe (2024) sin asegurar.
- **Barreras:** precio, desconfianza, baja educación financiera, **sesgos** (present bias, inercia).

## 🧑‍🤝‍🧑 Personas sintéticas — parámetros del generador

- **Variables:** generación, NSE (APEIM), región, educación financiera, sesgo del presente,
  canal, exposición sísmica, apertura a datos/IA, confianza, tenencia, seguro de desastres, WTP ratio.
- **Marginales objetivo validadas:** any-insurance ≈ **0.40-0.43** · desconfía ≈ **0.45-0.48** ·
  desastres ≈ **0.033**. Origen de cada celda marcado como `dato` o `supuesto` en el esquema.
- **Generar:** `python research/personas/generate_synthetic_users.py --n 1000 --out usuarios.csv --seed 42`
- ⚠️ Datos sintéticos: prototipado/balanceo/simulación, **no** inferencia causal ni personas reales.

## 🧭 Convenciones

- Investigación → `research/`. · Activos de personas sintéticas → `research/personas/`.
- Salidas/datasets generados → `research/personas/datasets/`.
- Spec (`schema.json`) y matriz legible (`.md`) se mantienen sincronizados con el generador.
- **Evidencia → `cronista`:** toda fuente referenciable usada para crear o fundamentar
  se registra en `research/fuentes/registro_fuentes.md` (resumen, rigurosidad, autor, año).

---
*Investigación recopilada 2026-06-21 · codex reorganizado 2026-06-22.*
