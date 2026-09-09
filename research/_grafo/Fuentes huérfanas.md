---
tipo: tablero
titulo: "Fuentes huérfanas"
tags:
  - tablero
---

# Fuentes huérfanas

**92 de 542 fuentes (16%)** están registradas
en el códice pero **ningún node ni output las cita**. O son evidencia que se buscó y no se
usó, o son citas que se perdieron al redactar. Vale la pena revisar cuáles de estas son
buenas y quedaron fuera: hay 23 de rigor 🟢A entre ellas.

## Con Dataview

```dataview
TABLE WITHOUT ID
  file.link AS "Fuente", autor AS "Autor", anio_txt AS "Año",
  rigor_marca + " " + rigor AS "Rigor", registrado AS "Registrada"
FROM #fuente
WHERE huerfana = true
SORT orden_rigor ASC, anio DESC
```

## Instantánea estática

| Fuente | Título | Rigor | Autor | Año | Registrada |
|---|---|---|---|---|---|
| [[F-005]] | Solo el 3% de los hogares peruanos cuenta con seguro contra sismos y d | 🟠 D | Infobae (cita a APESEG) | 2025 | 2026-06-22 |
| [[F-008]] | Only About 1 in 4 Gen Z Adults Can Define 'Deductible' and 'Co-Pay' | 🟡 C | NAIC (National Association of Insu | 2024 | 2026-06-25 |
| [[F-014]] | Named Perils vs. All Risks Explained in Plain English | 🟠 D | Insurance Training Center | s.f. | 2026-06-25 |
| [[F-028]] | Embedded Insurance Market Report 2026 | 🟡 C | Research and Markets | 2026 | 2026-07-06 |
| [[F-030]] | Hippo 'Off to a Fast Start' With Reversal of Q1 Loss a Year Ago | 🟠 D | Insurance Journal | 2026 | 2026-07-06 |
| [[F-031]] | Lemonade, Root earnings show insurtechs can scale | 🟠 D | Insurance Journal / eMarketer | 2026 | 2026-07-06 |
| [[F-032]] | Swiss Re delivers record Group net income of USD 4.8 billion in 2025 / | 🔵 B | Swiss Re | 2026 | 2026-07-06 |
| [[F-033]] | Media release FY2025 results / 2026-2030 targets | 🔵 B | Munich Re | 2026 | 2026-07-06 |
| [[F-034]] | Big Four European reinsurers post record ROE in 2025, 2026 outlook wea | 🟠 D | Intelligent Insurer | 2026 | 2026-07-06 |
| [[F-037]] | Usuarios de farmacias y boticas (cap. 4, publicación INEI) | 🔵 B | INEI (Instituto Nacional de Estadí | s.f. | 2026-07-06 |
| [[F-042]] | Triage Accuracy and the Safety of User-Initiated Symptom Assessment Wi | 🟢 A | NCBI/PMC (estudio Finlandia, Omaol | 2024 | 2026-07-06 |
| [[F-043]] | Longitudinal Changes in Diagnostic Accuracy of a Differential Diagnosi | 🟢 A | NCBI/PMC (estudio Japón) | 2024 | 2026-07-06 |
| [[F-044]] | Accuracy is inaccurate: Why a focus on diagnostic accuracy for medical | 🟢 A | NCBI/PMC | 2024 | 2026-07-06 |
| [[F-045]] | Peruano se indigna al ver su cita en EsSalud para 2026 | 🟠 D | El Popular / La República (cobertu | 2025 | 2026-07-06 |
| [[F-046]] | Citas médicas en EsSalud cada vez demoran más: informe técnico alerta  | 🟠 D | RPP | 2025 | 2026-07-06 |
| [[F-047]] | Farmacias privadas podrían sumarse al sistema de salud en Perú: Proyec | 🟠 D | Infobae | 2026 | 2026-07-06 |
| [[F-049]] | Inkafarma: "Con Mifarma tendríamos 2,245 farmacias y el 18% de las bot | 🟠 D | Gestión / Peru Retail (datos de In | 2024 | 2026-07-06 |
| [[F-050]] | Evaluación de Babylon Health's Diagnostic and Triage System | 🟢 A | The Lancet (vía TechCrunch/The Wee | 2020 | 2026-07-06 |
| [[F-051]] | Healthcare Chatbot Platforms: A Guide & Comparison | 🟠 D | IntuitionLabs (reseña de industria | s.f. | 2026-07-06 |
| [[F-052]] | Latin America Digital Health / Telehealth Market Size reports | 🟡 C | Grand View Research / Market Data  | 2025 | 2026-07-06 |
| [[F-067]] | Ley N° 29733 — Ley de Protección de Datos Personales | 🔵 B | Congreso de la República del Perú | 2011 | 2026-07-06 |
| [[F-068]] | Nuevo reglamento de Protección de Datos Personales refuerza el consent | 🔵 B | MINJUS (Ministerio de Justicia y D | 2025 | 2026-07-06 |
| [[F-071]] | Nuevo reglamento de datos busca acabar con llamadas spam pero experto  | 🟠 D | Infobae | 2025 | 2026-07-06 |
| [[F-072]] | El consentimiento en el nuevo reglamento de Protección de Datos Person | 🟡 C | Estudio Ugaz Zegarra (firma legal) | 2025 | 2026-07-06 |
| [[F-073]] | Registro "Gracias... no insista" quedó obsoleto | 🟠 D | ConNuestroPeru.com / PeruWeek (his | 2018 | 2026-07-06 |
| [[F-074]] | Guías de email marketing legal en Perú bajo Ley 29733 | 🟠 D | Mailpro / Yumayus (agencias de mar | s.f./2024 | 2026-07-06 |
| [[F-075]] | Estrategias de captación de clientes en farmacias (punto de venta, fid | 🟠 D | Increnta / Asefarma (agencias de m | s.f. | 2026-07-06 |
| [[F-076]] | Datos personales y el envío de publicidad sin consentimiento a través  | 🟡 C | Manrique, M. & Proaño, G. (IUS360  | s.f. | 2026-07-06 |
| [[F-077]] | Data Protection in Peru: Overview | 🟡 C | Multilaw / Niubox Legal (guías com | 2023 | 2026-07-06 |
| [[F-079]] | Allianz Global Insurance Report 2025/2026 | ⚪ N/A | Allianz Research | 2025 | 2026-07-10 |
| [[F-080]] | Top international insurance markets / Global insurance market share by | 🔵 B | NAIC / Statista (agregando datos O | 2024-2025 | 2026-07-10 |
| [[F-081]] | Insurance NPS Benchmarks 2025 | 🟠 D | CustomerGauge / QuestionPro (agreg | 2025 | 2026-07-10 |
| [[F-082]] | Equilibrium in Competitive Insurance Markets: An Essay on the Economic | 🟢 A | Rothschild, M. & Stiglitz, J. | 1976 | 2026-07-10 |
| [[F-083]] | Uncertainty and the Welfare Economics of Medical Care (The American Ec | 🟢 A | Arrow, K.J. | 1963 | 2026-07-10 |
| [[F-084]] | Insurance and Behavioral Economics: Improving Decisions in the Most Mi | 🟡 C | Kunreuther, H. (con Pauly, McMorro | 1984-2013 | 2026-07-10 |
| [[F-093]] | Risk Pooling: How Health Insurance in the Individual Market Works | 🟡 C | American Academy of Actuaries (Act | s.f. | 2026-07-10 |
| [[F-095]] | Market Design in Regulated Health Insurance Markets: Risk Adjustment v | 🔴 E | Tebaldi, P. (NBER Working Paper w3 | 2024 | 2026-07-10 |
| [[F-101]] | The Singapore Model | 🟡 C | AEI (American Enterprise Institute | s.f. | 2026-07-10 |
| [[F-132]] | Insurance Marketing Coalition Limited v. Federal Communications Commis | 🔵 B | US Court of Appeals, 11th Circuit | 2025 | 2026-07-14 |
| [[F-146]] | Designing for UX Trust: Security, Privacy & Transparency | 🟠 D | Think Design / MoldStud (blogs de  | s.f. | 2026-07-14 |
| [[F-160]] | U.S. P/C Insurers Post Biggest Q1 Underwriting Profit in 25 Years | 🟠 D | AM Best (vía Carrier Management) | 2026 | 2026-07-06 |
| [[F-161]] | P/C Insurance Market Profitability Improves in 2024; Expected to Conti | 🟡 C | Triple-I & Milliman | 2025 | 2026-07-06 |
| [[F-162]] | Bibliometric review of telematics-based automobile insurance | 🟢 A | ScienceDirect (revisión bibliométr | 2023 | 2026-07-06 |
| [[F-163]] | The Growth of Parametric Insurance | 🟡 C | Cappelletti, A. (Society of Actuar | 2026 | 2026-07-06 |
| [[F-164]] | On the design of optimal parametric insurance (The Geneva Risk and Ins | 🟢 A | Louaas, A. & Picard, P. | 2026 | 2026-07-06 |
| [[F-165]] | Triggers paramétricos y reducción de costos de siniestros | 🟠 D | Swiss Re Institute (citado vía Ins | 2026 | 2026-07-06 |
| [[F-166]] | UK insurers warned privacy concerns are stalling telematics pricing ad | 🟠 D | Insurance Business Mag (UK) | 2026 | 2026-07-06 |
| [[F-167]] | Telematics and Trust: How Usage-Based Insurance Is Transforming Auto C | 🟠 D | Carrier Management | 2026 | 2026-07-06 |
| [[F-168]] | Lemonade backtracks AI comments after accusations of discrimination | 🟠 D | Forbes / Claims Journal (cobertura | 2021 | 2026-07-06 |
| [[F-169]] | US P&C industry sees decade-high performance in 2025 | 🟡 C | AM Best (vía Reinsurance News) | 2026 | 2026-07-06 |
| [[F-170]] | Global Insurance Report 2025: Searching for profitable growth in comme | 🟡 C | McKinsey & Company | 2025 | 2026-07-06 |
| [[F-171]] | Commercial Insurance Market Performance Data: 2025 metrics | 🟡 C | Datos agregados de industria (AM B | 2025 | 2026-07-06 |
| [[F-208]] | 9 Best Stocks To Buy Now For July 2026 / Best Stocks to Buy Now for Ju | 🟠 D | Forbes / Zacks | 2026 | 2026-07-23 |
| [[F-209]] | My Top Ranked Stock to Buy Right Now in July (2026) / Best Stocks to B | 🟠 D | The Motley Fool | 2026-07-03 | 2026-07-23 |
| [[F-210]] | Trending Stocks — July 2026 / WallStreetBets Stocks — Most Mentioned T | 🟡 C | AltIndex | 2026-07 | 2026-07-23 |
| [[F-211]] | Best Performing Stocks in July 2026 - Monthly Gainers | 🟡 C | StockTitan | 2026-07 | 2026-07-23 |
| [[F-212]] | 'Yet another way in which 2026 is looking like 1999' / Investors grow  | 🟠 D | Fortune / eciks.org | 2026-06-08 y 2026-07 | 2026-07-23 |
| [[F-213]] | Acciones peruanas para invertir en la BVL: análisis y perspectivas 202 | 🟠 D | Rankia Perú / trii.pe | 2026 | 2026-07-23 |
| [[F-214]] | SAB LOCALES COMPARTEN SUS TOP PICKS PARA LA BVL EN EL 2026 | 🟠 D | Borsista.com (compilación de casas | 2026 | 2026-07-23 |
| [[F-215]] | Bolsa de Valores de Lima: Ganancias de empresas rompen marca histórica | 🟠 D | Gestión.pe | 2026 | 2026-07-23 |
| [[F-216]] | El precio del cobre en perspectiva geopolítica | 🟡 C | UBS (citado en Rumbo Minero) | 2026 | 2026-07-23 |
| [[F-217]] | Acciones con potencial para invertir en julio de 2026: análisis comple | 🔵 B | BCRP (citado en Rankia Perú) | 2026 | 2026-07-23 |
| [[F-329]] | Tele-triage, care substitution, and health: Evidence from quasi-random | 🟢 A | Autor no confirmado (bloqueo de ac | s.f. | 2026-07-27 |
| [[F-330]] | Medical advice lines offering on-demand access to providers reduced em | 🟢 A | Tran, Rose, Suzuki, Urech, Vashi | 2023 | 2026-07-27 |
| [[F-331]] | Triaging and Referring In Adjacent General and Emergency Departments ( | 🟢 A | Autores del TRIAGE trial | s.f. | 2026-07-27 |
| [[F-332]] | Medical Mutual Nurse Triage Case Study | 🟠 D | Conduit Health Partners | s.f. | 2026-07-27 |
| [[F-333]] | Patient compliance with NHS 111 advice | 🟢 A | Revisión rápida de evidencia, vía  | s.f. | 2026-07-27 |
| [[F-334]] | Do consumers perceive and trust health insurers within a system of man | 🟢 A | Autores no especificados en el res | s.f. | 2026-07-27 |
| [[F-335]] | A Measure of Trust in Insurers (Health Services Research) | 🟢 A | Zheng, B. et al. | ~2002 | 2026-07-27 |
| [[F-336]] | Exploring Trust in Health Insurers: Insights from Enrollees' Perceptio | 🟡 B | van der Hulst, F.J.P.; Huijgen, S. | 2025 | 2026-07-27 |
| [[F-337]] | The role of autonomy and reactance for nudging — Experimentally compar | 🟢 A | Bruns, H. & Perino, G. | 2023 | 2026-07-27 |
| [[F-338]] | How Do Consumers Interact with Digital Expert Advice? Experimental Evi | 🟢 A | Bundorf, M.K.; Polyakova, M.; Tai- | 2024 | 2026-07-27 |
| [[F-339]] | The Impact of Narrow and Tiered Networks on Costs, Access, Quality, an | 🟢 A | Mazurenko, O.; Taylor, E.; Menache | 2022 | 2026-07-27 |
| [[F-340]] | Enrollment In A Health Plan With A Tiered Provider Network Decreased M | 🟢 A | Sinaiko, A.D.; Landrum, M.B.; Cher | 2017 | 2026-07-27 |
| [[F-341]] | Estudio en Journal of Health Economics sobre disposición a pagar por c | 🟢 A | Autores no especificados en el res | 2018 | 2026-07-27 |
| [[F-342]] | Encuesta de autorización previa (prior authorization) — pacientes, emp | 🟠 C | American Medical Association (AMA) | 2024-2025 | 2026-07-27 |
| [[F-343]] | Denegaciones algorítmicas de Cigna (300,000 reclamos en 2 meses, 1.2 s | 🟡 C | AAPC / KFF / Bloomberg Law (múltip | 2025 | 2026-07-27 |
| [[F-344]] | Reacción social al asesinato del CEO de UnitedHealthcare (dic. 2024) — | 🟡 C | CNN Business, NBC News, ABC7, NPR  | 2024 | 2026-07-27 |
| [[F-345]] | Anthem revierte política de límite de tiempo de anestesia tras presión | 🔵 B | NBC News, Healthcare Brew, oficina | 2024 | 2026-07-27 |
| [[F-346]] | Política de "ER evitable" de Anthem — backlash y reversión | 🟡 C | NPR, AARP, Fierce Healthcare, Heal | 2018-2019 | 2026-07-27 |
| [[F-347]] | Quejas recurrentes sobre 98point6: deriva a urgent care sin tratar, co | 🟠 D | Reviews de usuarios vía Trustpilot | s.f. | 2026-07-27 |
| [[F-348]] | Quejas sobre Included Health/Doctor On Demand: negativa a recetar, pub | 🟠 D | Reviews de usuarios vía BBB / Trus | s.f. | 2026-07-27 |
| [[F-349]] | Investigación sobre EviCore ("the dial") — algoritmo ajustable de aseg | 🟢 A | ProPublica | 2023-2024 | 2026-07-27 |
| [[F-350]] | Plan "virtual-first" de Priority Health — ~5,000 inscritos, 60% de enc | 🟠 D | KFF Health News, BusinessWire | 2020-2021 | 2026-07-27 |
| [[F-351]] | Formulario 10-K, año fiscal 2024 (SEC) | 🟡 C | Oscar Health | 2024 | 2026-07-27 |
| [[F-352]] | What Are The Potential Savings From Steering Patients To Lower-Priced  | 🟢 A | Desai, S.; Hatfield, L.A.; Hicks,  | ~2016 | 2026-07-27 |
| [[F-353]] | Vitality Impact Study | 🔵 B | Vitality Group; validación actuari | 2024 | 2026-07-27 |
| [[F-354]] | How a remote nurse-first triage model reduces benefits spend for emplo | 🟠 D | Patient Safety & Quality Healthcar | s.f. | 2026-07-27 |
| [[F-355]] | Patient and Parent Experience with Pediatric Care Providers During the | 🟢 A | Gotthardt, C.J.; Haynes, S.C.; Mur | 2024 | 2026-07-27 |
| [[F-356]] | Healthcare NPS Benchmarks: 31 Scores + Industry Guide | 🔵 B | CustomerGauge | 2025 | 2026-07-27 |
| [[F-357]] | Ensayo aleatorizado de framing opt-out vs. opt-in en monitoreo remoto  | 🟢 A | Mehta, S.J. et al. | 2025 | 2026-07-27 |
| [[F-358]] | Colapso financiero de Babylon Health — pérdidas de $212-274M en 2022,  | 🟡 C | TechCrunch, Hospitalogy, Healthcar | 2023 | 2026-07-27 |
