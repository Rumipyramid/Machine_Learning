# Modelo de personas sintéticas (lapuerta)

> **Nodo nuevo, fuera del alcance formal declarado en `alma.md`** (que excluye
> `research/personas/` por ser "subsistema de código, ya estructurado en `CLAUDE.md`"). Se
> propone como excepción deliberada: la explicación *conceptual* del modelo no existía como un
> solo documento — vivía repartida entre `research/README.md`, `CLAUDE.md` y
> `matriz_usuarios_sinteticos.md`. El código, el esquema y los datos **no se mueven** de
> `research/personas/` — decenas de referencias por ruta fija (skills, GitHub Action, scripts)
> dependen de que sigan ahí. Este node cuenta la historia y cita dónde vive cada pieza activa.
> Última actualización: 2026-07-20.

## Qué es

Un generador de perfiles sintéticos de consumidores de seguros peruanos (solo stdlib de Python),
calibrado con datos reales — SBS 2023, APESEG, APEIM, BCRP/INEI, más los reportes quincenales de
`cerrajero` y los hallazgos de `/trinidad`. **v1.3, 20 variables**: 14
independientes/condicionales (generación, NSE, región, educación financiera, sesgo del presente,
canal, situación laboral, cobertura previsional, tenencia de vehículo, acceso digital,
bancarizado, trabajo en plataforma digital, exposición sísmica, apertura a datos/IA) + 6 modelos
derivados (confianza, disposición a compartir datos para pricing, tenencia de seguro, seguro de
desastres, WTP, propensión a microseguro).

Dos variables nuevas de v1.3 llegaron por **vías independientes** el mismo ciclo: `
trabajo_plataforma_digital` + `propension_microseguro` por el mecanismo de incorporación
automática de prioridad Alta (ver `CLAUDE.md` § Personas sintéticas), y
`disposicion_compartir_datos_pricing` por hallazgos de `/trinidad` sobre modelos de seguros
rentables — separa la confianza *abstracta* en IA de la disposición *conductual* real a
compartir datos para pricing UBI/telemetría (brecha actitud-conducta).

Marginales validadas: any-insurance ≈ 0.40, desconfía ≈ 0.46, desastres ≈ 0.035, bancarizado ≈
0.59, comparte datos pricing (alta) ≈ 0.15, trabajo en plataforma digital ≈ 0.07[^1].

## Dónde vive cada pieza (no se mueve de aquí)

| Pieza | Ruta |
|---|---|
| Esquema (fuente de verdad machine-readable) | `research/personas/generador/synthetic_user_schema.json` |
| Generador | `research/personas/generador/generate_synthetic_users.py` |
| Matriz legible + changelog de versiones | `research/personas/generador/matriz_usuarios_sinteticos.md` |
| Harness de validación | `research/personas/generador/validate.py` |
| Calibración con dato real (ENAHO → IPF) | `research/personas/datos_enaho/`, `enaho_loader.py`, `ipf.py` |
| Apps web (explorador por reglas + preguntas libres a Claude) | `research/personas/apps/` |
| Skill portátil (copia autocontenida para compartir) | `.claude/skills/lapuerta/` |

## Cómo se sigue alimentando

Cada ~15 días, `cerrajero` (a demanda) o el GitHub Action `fortalecimiento-modelo.yml`
(desatendido) investigan evidencia nueva y proponen variables candidatas en
`research/updates/`. Las de **prioridad Alta se aplican solas** al esquema/generador — con
recalibración empírica del intercepto y `validate.py --check` como gate; si falla, se revierte.
En el ciclo a demanda el cambio queda en la rama de trabajo; en el desatendido va a un **PR
aparte** (nunca push directo a main) porque ahí no hay nadie mirando la sesión en vivo. Las
propuestas Media/Baja quedan pendientes de revisión manual.

## Por qué importa

Es el activo diferencial que [[behavioral-design-estado-disciplina|behavioral design: estado de
la disciplina]] identifica en la frontera de "AI Behavioral Science": pocos equipos en la región
tienen simulación de consumidores calibrada con microdato nacional, no solo supuestos.

## Conexiones
- Calibrado con → [[seguros-comportamiento-mundo-peru|Comportamiento, percepción y valoración
  frente a seguros (Mundo vs. Perú)]] (SBS, APESEG, marginales)
- Posicionado por → [[behavioral-design-estado-disciplina|Behavioral design: estado de la
  disciplina y del mercado]] en la frontera de IA + usuarios sintéticos
- Patrón compartido con → [[tendencias-diseno-innovacion|Tendencias en diseño e innovación: qué tiene impacto
  real y qué es propuesta]]: su hipótesis H9 (los diseñadores declaran rechazo a la IA mientras la adoptan
  masivamente) es estructuralmente el mismo fenómeno que modela la variable
  `disposicion_compartir_datos_pricing` — desconfianza abstracta declarada ≠ conducta real.

[^1]: `research/personas/generador/matriz_usuarios_sinteticos.md` §2-3, notas v1.1-v1.3; medido
    con `validate.py --check`.
