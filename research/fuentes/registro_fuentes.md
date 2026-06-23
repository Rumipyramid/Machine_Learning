# 📜 Registro de fuentes — Códice de evidencia

> Ledger persistente que mantiene el skill `cronista`. Cada fuente usada para
> crear o fundamentar contenido del proyecto se anota aquí: resumen breve,
> rigurosidad metodológica, autor y año. Fuente única de trazabilidad.
> Iniciado: 2026-06-22.

## Rúbrica de rigurosidad
| Nivel | Etiqueta | Criterio (resumen) |
|---|---|---|
| A | 🟢 Alta | Académico peer-reviewed, datos primarios, método y muestra explícitos. |
| B | 🔵 Sólida | Organismo oficial/regulador/intergubernamental con metodología documentada. |
| C | 🟡 Media | Consultora/industria con encuesta o método propio, no auditable. |
| D | 🟠 Baja | Prensa/blog/fuente secundaria que cita a otros sin método propio. |
| E | 🔴 Débil | Opinión sin metodología, sin origen verificable o anónima. |

## Fuentes registradas
| ID | Autor | Año | Fuente / Título | Rigurosidad | Resumen breve | Usado en / fundamenta | URL / referencia | Registrado |
|---|---|---|---|---|---|---|---|---|
| F-1 | SBS (Superintendencia de Banca, Seguros y AFP) | 2023 | Estudio sobre Conocimiento y Percepción de la Demanda de Seguros | 🔵 B — regulador oficial peruano, encuesta con metodología publicada | Tenencia ~4/10, SOAT conocido por 94%, confusión de "seguros" con salud pública (SIS/EsSalud). | Cifras de conocimiento y tenencia en `research/seguros_comportamiento_mundo_peru.md` §3.2. | https://www.sbs.gob.pe/Portals/4/jer/CIFRAS-ENCUESTA/2023/328-0922%20-%20Servicios%20de%20seguros%20-%20Informe%20de%20resultados.pdf | 2026-06-22 |
| F-2 | OECD | 2025 | Global Insurance Market Trends 2025 | 🔵 B — organismo intergubernamental, series estadísticas documentadas | Tendencias globales del mercado asegurador (penetración, primas, ramos) que sirven de marco comparativo. | Marco mundial en `research/seguros_comportamiento_mundo_peru.md` §1.1. | https://www.oecd.org/en/publications/global-insurance-market-trends-2025_0d11ecf4-en/full-report/component-3.html | 2026-06-22 |
| F-3 | Platteau, J.-P. et al. (vía ScienceDirect) | 2021 | Puzzles of insurance demand and its biases | 🟢 A — paper peer-reviewed con revisión de evidencia y método explícito | Sesgos conductuales (present bias, baja educación financiera) que deprimen la demanda de seguros. | Base conductual y selección de variables del generador de personas; `…md` §2. | https://www.sciencedirect.com/science/article/abs/pii/S2214635021000150 | 2026-06-22 |
| F-4 | Bain & Company | 2023 | Customer Behavior and Loyalty in Insurance (Global Edition) | 🟡 C — consultora; encuesta propia amplia (28,765 consumidores, 14 países) no auditable | ~80% de consumidores quiere criterios ESG integrados; comportamiento y lealtad por segmento. | Expectativas de valor en `research/seguros_comportamiento_mundo_peru.md` §1.4. | https://www.bain.com/insights/customer-behavior-and-loyalty-in-insurance-global-edition-2023/ | 2026-06-22 |
| F-5 | Infobae (cita a APESEG) | 2025 | Solo el 3% de los hogares peruanos cuenta con seguro contra sismos y desastres | 🟠 D — prensa que reporta cifra primaria de APESEG (fuente original = APESEG) | ~3.3% de hogares con seguro ante desastres en un país altamente sísmico. | Dato de subaseguramiento sísmico en `…md` §3.2. | https://www.infobae.com/peru/2025/03/04/solo-el-3-de-los-hogares-peruanos-cuenta-con-un-seguro-contra-sismos-y-desastres-naturales-alerta-apeseg/ | 2026-06-22 |
