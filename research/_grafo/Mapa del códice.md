---
tipo: tablero
titulo: "Mapa del códice"
tags:
  - tablero
---

# Mapa del códice

Proyección de `research/fuentes/codice.md` — **542 fuentes**, 18 nodes,
10 outputs. Regenerar con `python3 research/_grafo/generar_grafo.py`.

## Reparto por rigurosidad

| Grado | Fuentes | % del total |
|---|---|---|
| A | 147 | 27% |
| B | 107 | 19% |
| C | 112 | 20% |
| D | 135 | 24% |
| E | 28 | 5% |
| N/A | 10 | 1% |
| s/g | 3 | 0% |

## Carga de evidencia por documento

Cuánta evidencia sostiene cada node/output y de qué calidad.
**% débil** = proporción en 🟠D + 🔴E.

| Documento | Fuentes | 🟢A | 🔵B | 🟡C | 🟠D | 🔴E | % débil |
|---|---|---|---|---|---|---|---|
| [[tendencias-diseno-innovacion]] | 181 | 37 | 29 | 42 | 45 | 21 | 36% |
| [[mecanismos-seguros-salud]] | 43 | 15 | 11 | 7 | 6 | 2 | 18% |
| [[proyecto-back-to-basics-ffvv-vida]] | 33 | 21 | 8 | 1 | 2 | 1 | 9% |
| [[futuro-asesores-seguros-venta-digital]] | 25 | 3 | 1 | 11 | 9 | 0 | 36% |
| [[capacidades-asistente-ia-aseguradora]] | 24 | 3 | 11 | 5 | 5 | 0 | 20% |
| [[modelo-salud-ia-farmacias-peru]] | 21 | 16 | 2 | 0 | 3 | 0 | 14% |
| [[como-trabajan-equipos-diseno-referencias-2026-08-10]] | 21 | 2 | 6 | 5 | 8 | 0 | 38% |
| [[transicion-venta-fria-a-opt-in]] | 18 | 4 | 3 | 3 | 7 | 1 | 44% |
| [[material-visual-venta-consultiva]] | 17 | 9 | 3 | 0 | 5 | 0 | 29% |
| [[back-to-basics-presentacion-milagros-2026-07-23]] | 15 | 8 | 5 | 0 | 0 | 1 | 6% |
| [[metodologias-diseno-sistemas-complejos]] | 14 | 2 | 6 | 3 | 3 | 0 | 21% |
| [[evaluacion-calidad-agentes-conversacionales-ia]] | 13 | 9 | 0 | 1 | 1 | 1 | 15% |
| [[behavioral-design-estado-disciplina]] | 12 | 7 | 1 | 3 | 1 | 0 | 8% |
| [[revision-modelo-trabajo-diseno-2026-08-10]] | 11 | 3 | 3 | 3 | 1 | 1 | 18% |
| [[analisis-final-modelo-trabajo-diseno-2026-08-10]] | 10 | 1 | 3 | 2 | 4 | 0 | 40% |
| [[glosario-seguro-vida-peru]] | 8 | 3 | 1 | 1 | 2 | 1 | 37% |
| [[venta-vida-digital-hibrida-latam]] | 8 | 0 | 4 | 3 | 1 | 0 | 12% |
| [[glosario-seguro-salud-peru]] | 7 | 3 | 2 | 1 | 1 | 0 | 14% |
| [[seguros-comportamiento-mundo-peru]] | 6 | 1 | 2 | 1 | 1 | 0 | 16% |
| [[aida-copiloto-asesor-rimac]] | 6 | 2 | 2 | 1 | 1 | 0 | 16% |
| [[guia-triaje-resultados-2026-08-05]] | 5 | 1 | 1 | 0 | 3 | 0 | 60% |
| [[guia-triaje-200-usuarios-sinteticos-2026-08-05]] | 5 | 1 | 1 | 0 | 3 | 0 | 60% |
| [[zoom-c4-contenido-clinico-2026-08-12]] | 4 | 1 | 1 | 2 | 0 | 0 | 0% |
| [[aida-historia-completa-post-owners-2026-08-19]] | 3 | 1 | 1 | 0 | 1 | 0 | 33% |
| [[aida-objetivo-vs-diagnostico-2026-08-12]] | 2 | 1 | 0 | 0 | 1 | 0 | 50% |

## Puertas de entrada

- [[Tablero de hipótesis]] — las 31 hipótesis vivas y su estado
- [[Auditoría de rigor]] — qué se apoya en evidencia débil
- [[Fuentes huérfanas]] — registradas y nunca usadas
- [[Cadenas de eco de cita]] — cifras que no deben usarse como afirmación fuerza
- [[alma]] — mapa de nodes

## Entidades del grafo

| Tipo | Cuántas | Carpeta |
|---|---|---|
| Fuentes | 542 | `_grafo/fuentes/` |
| Hipótesis | 31 | `_grafo/entidades/hipotesis/` |
| Reglas de criterio | 22 | `_grafo/entidades/reglas/` |
| Autores con 2+ fuentes | 24 | `_grafo/entidades/autores/` |
| Nodes | 18 | `_nodes/` |
| Outputs | 10 | `_outputs/` |
