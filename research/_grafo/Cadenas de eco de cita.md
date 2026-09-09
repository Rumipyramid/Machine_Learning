---
tipo: tablero
titulo: "Cadenas de eco de cita"
tags:
  - tablero
---

# Cadenas de eco de cita

**32 fuentes** que el códice marca explícitamente como *eco de cita*, *huérfana de
cita*, *autoridad prestada* o *evidencia propietaria no auditable* — cifras que circulan con
muchos megáfonos y ninguna fuente primaria localizable. Registradas para no volver a caer,
**no para citarlas**.

Abre el **grafo local** de cualquiera de estas notas para ver la cadena completa: la sección
*Relacionada con* enlaza las fuentes que el propio códice cruza con ella.

## Con Dataview

```dataview
TABLE WITHOUT ID
  file.link AS "Fuente", autor AS "Autor", anio_txt AS "Año", fundamenta AS "Contamina a"
FROM #fuente
WHERE eco_de_cita = true
SORT anio DESC
```

## Instantánea estática

| Fuente | Título | Rigor | Autor | Año | Aparece en |
|---|---|---|---|---|---|
| [[F-004]] | Customer Behavior and Loyalty in Insurance (Global Edition) | 🟡 C | Bain & Company | 2023 | [[seguros-comportamiento-mundo-peru]] |
| [[F-028]] | Embedded Insurance Market Report 2026 | 🟡 C | Research and Markets | 2026 | — |
| [[F-052]] | Latin America Digital Health / Telehealth Market Size reports | 🟡 C | Grand View Research / Market D | 2025 | — |
| [[F-161]] | P/C Insurance Market Profitability Improves in 2024; Expected to Conti | 🟡 C | Triple-I & Milliman | 2025 | — |
| [[F-170]] | Global Insurance Report 2025: Searching for profitable growth in comme | 🟡 C | McKinsey & Company | 2025 | — |
| [[F-181]] | $15 billion of the insurance industry is at risk from AI, BofA says | 🟡 C | BofA Global Research (vía Fort | 2026 | [[futuro-asesores-seguros-venta-digital]] |
| [[F-182]] | Insurance Agent Digital Shake-up | 🟡 C | Bain & Company | s.f. | [[futuro-asesores-seguros-venta-digital]] |
| [[F-183]] | Insurers Have a Digital Dilemma: Complex Claims | 🟡 C | Bain & Company | s.f. | [[futuro-asesores-seguros-venta-digital]] |
| [[F-195]] | Analyzing Financial Trends Of Health Insurance In Q1 2025 | 🟡 C | Oliver Wyman | 2025 | [[mecanismos-seguros-salud]] |
| [[F-231]] | Searching for Simplicity: Improving Customer Comprehension in Life Ins | 🔵 B | SOA Research Institute & RGA ( | 2024 | [[glosario-seguro-vida-peru]] |
| [[F-234]] | La declaración del riesgo/salud en el seguro de vida: consecuencias de | 🟠 D | Múltiples (Almacén de Derecho, | Vigente 2026 | [[glosario-seguro-vida-peru]] |
| [[F-266]] | The Business Value of Design (McKinsey Design Index) | 🟡 C | McKinsey & Company | 2018 | [[tendencias-diseno-innovacion]] |
| [[F-268]] | The Six Steps For Justifying Better UX | 🟡 C | Forrester Research (Hogan, S.  | 2016 | [[tendencias-diseno-innovacion]] |
| [[F-281]] | State of UX 2026 | 🟡 C | Nielsen Norman Group | 2026 | [[tendencias-diseno-innovacion]] |
| [[F-315]] | Creative Software Market Size & Share Report | 🟡 C | Grand View Research (y otros v | 2024-2026 | [[tendencias-diseno-innovacion]] |
| [[F-327]] | "Los design systems dan 671% de ROI (Forrester)" | 🔴 E | Blogs de agencia y posts de Li | 2024-2026 | [[tendencias-diseno-innovacion]] |
| [[F-332]] | Medical Mutual Nurse Triage Case Study | 🟠 D | Conduit Health Partners | s.f. | — |
| [[F-346]] | Política de "ER evitable" de Anthem — backlash y reversión | 🟡 C | NPR, AARP, Fierce Healthcare,  | 2018-2019 | — |
| [[F-354]] | How a remote nurse-first triage model reduces benefits spend for emplo | 🟠 D | Patient Safety & Quality Healt | s.f. | — |
| [[F-367]] | Singlife taps MUFG loan / Singapore Life financials | 🟡 C | Insurance Business Magazine /  | 2023-2026 | [[futuro-asesores-seguros-venta-digital]] |
| [[F-372]] | Betterfly (Chile) despide personal y cierra operaciones en cinco paíse | 🟡 C | AméricaEconomía, BioBioChile,  | 2025 | [[venta-vida-digital-hibrida-latam]] |
| [[F-377]] | Azos dobra faturamento em 2025 / Azos capta R$170 mi em Série B / A Jo | 🟡 C | Revista Segurador Brasil, Bloo | 2025 | [[venta-vida-digital-hibrida-latam]] |
| [[F-397]] | One Formula To Rule Them All: The ROI Of A Design System | 🔴 E | Smashing Magazine | 2022 | [[tendencias-diseno-innovacion]] |
| [[F-404]] | Why Sr. Devs Are Actually Less Productive with AI Copilot — DZone | 🔴 E | Autoría no declarada (blog sin | 2025 | [[tendencias-diseno-innovacion]] |
| [[F-406]] | Telemetría de +10.000 desarrolladores / 1.255 equipos | 🟡 C | Faros AI (vendor de analítica  | 2025 | [[tendencias-diseno-innovacion]] |
| [[F-408]] | Descubre cómo evoluciona el UX/UI en 2026 | 🔴 E | IEM Business School (iembs.com | 2026 | [[tendencias-diseno-innovacion]] |
| [[F-411]] | Las tendencias de diseño gráfico más interesantes para 2026 · Canva pr | 🔴 E | The Power Business School (the | 2025-2026 | [[tendencias-diseno-innovacion]] |
| [[F-444]] | "El 90% de los innovation labs corporativos fracasa" · "El 70-90% del  | 🔴 E | Blogs de consultoría y platafo | 2016-2026 | [[tendencias-diseno-innovacion]] |
| [[F-458]] | Ecosistema insurtech LatAm: 536 startups (2025) → 576 (1S 2026, +14%); | 🟠 D | MAPFRE Perú, El Ecosistema Sta | 2025-2026 | [[tendencias-diseno-innovacion]] |
| [[F-482]] | Why 70% of Transformations Miss the Mark / gobernanza en programas de  | 🟡 C | BCG Platinion / McKinsey (vía  | 2023-2024 | [[metodologias-diseno-sistemas-complejos]], [[revision-modelo-trabajo-diseno-2026-08-10]] |
| [[F-498]] | Problems with the Center of Excellence Model | 🟠 D | ZeroBlockers (blog) atribuyend | 2024-2025 | [[como-trabajan-equipos-diseno-referencias-2026-08-10]] |
| [[F-525]] | Stop Trying to Delight Your Customers / The Effortless Experience | 🟡 C | Dixon, M., Freeman, K. & Toman | 2010-2026 | [[capacidades-asistente-ia-aseguradora]] |
