---
tipo: tablero
titulo: "Auditoría de rigor"
tags:
  - tablero
---

# Auditoría de rigor

**163 de 542 fuentes (30%) son 🟠D o 🔴E.**
No es un defecto en sí — `gossiper` y `marketer` producen ese registro por diseño — pero
sí es donde hay que mirar antes de convertir algo en afirmación fuerza.

## Con Dataview

```dataview
TABLE WITHOUT ID
  file.link AS "Fuente", autor AS "Autor", anio_txt AS "Año",
  rigor_marca + " " + rigor AS "Rigor", fundamenta AS "Fundamenta"
FROM #fuente
WHERE rigor = "D" OR rigor = "E"
SORT rigor ASC, anio DESC
```

Para auditar un node concreto, cambia el `WHERE`:

```dataview
TABLE WITHOUT ID file.link AS "Fuente", rigor_marca + " " + rigor AS "Rigor", autor
FROM #fuente
WHERE contains(string(fundamenta), "tendencias-diseno-innovacion")
SORT orden_rigor ASC
```

## Instantánea estática

| Fuente | Título | Rigor | Autor | Año | Fundamenta |
|---|---|---|---|---|---|
| [[F-005]] | Solo el 3% de los hogares peruanos cuenta con seguro contra sismos y d | 🟠 D | Infobae (cita a APESEG) | 2025 | — |
| [[F-014]] | Named Perils vs. All Risks Explained in Plain English | 🟠 D | Insurance Training Center | s.f. | — |
| [[F-015]] | Encuesta "solo el 9% entiende términos básicos de seguro" | 🟠 D | UnitedHealth (vía resultados de bú | s.f. | [[glosario-seguro-salud-peru]] |
| [[F-025]] | Shared-value insurance: resultados del modelo Vitality | 🟠 D | Vitality Group / Discovery | 2025 | [[behavioral-design-estado-disciplina]] |
| [[F-030]] | Hippo 'Off to a Fast Start' With Reversal of Q1 Loss a Year Ago | 🟠 D | Insurance Journal | 2026 | — |
| [[F-031]] | Lemonade, Root earnings show insurtechs can scale | 🟠 D | Insurance Journal / eMarketer | 2026 | — |
| [[F-034]] | Big Four European reinsurers post record ROE in 2025, 2026 outlook wea | 🟠 D | Intelligent Insurer | 2026 | — |
| [[F-035]] | Estudio revela que el 68.21% de los peruanos se automedica con antiinf | 🟠 D | Blog USIL / Infobae (cita estudio) | 2025 | [[guia-triaje-200-usuarios-sinteticos-2026-08-05]], [[guia-triaje-resultados-2026-08-05]], [[modelo-salud-ia-farmacias-peru]] |
| [[F-038]] | Uno de cada cinco peruanos recurre a la automedicación | 🟠 D | Infobae (cita estudio/encuesta) | 2026 | [[guia-triaje-200-usuarios-sinteticos-2026-08-05]], [[guia-triaje-resultados-2026-08-05]], [[modelo-salud-ia-farmacias-peru]] |
| [[F-039]] | Automedicación descontrolada en Perú: 3 de cada 10 hogares compran med | 🟠 D | Infobae (cita a Kantar) | 2024 | [[guia-triaje-200-usuarios-sinteticos-2026-08-05]], [[guia-triaje-resultados-2026-08-05]], [[modelo-salud-ia-farmacias-peru]] |
| [[F-045]] | Peruano se indigna al ver su cita en EsSalud para 2026 | 🟠 D | El Popular / La República (cobertu | 2025 | — |
| [[F-046]] | Citas médicas en EsSalud cada vez demoran más: informe técnico alerta  | 🟠 D | RPP | 2025 | — |
| [[F-047]] | Farmacias privadas podrían sumarse al sistema de salud en Perú: Proyec | 🟠 D | Infobae | 2026 | — |
| [[F-049]] | Inkafarma: "Con Mifarma tendríamos 2,245 farmacias y el 18% de las bot | 🟠 D | Gestión / Peru Retail (datos de In | 2024 | — |
| [[F-051]] | Healthcare Chatbot Platforms: A Guide & Comparison | 🟠 D | IntuitionLabs (reseña de industria | s.f. | — |
| [[F-071]] | Nuevo reglamento de datos busca acabar con llamadas spam pero experto  | 🟠 D | Infobae | 2025 | — |
| [[F-073]] | Registro "Gracias... no insista" quedó obsoleto | 🟠 D | ConNuestroPeru.com / PeruWeek (his | 2018 | — |
| [[F-074]] | Guías de email marketing legal en Perú bajo Ley 29733 | 🟠 D | Mailpro / Yumayus (agencias de mar | s.f./2024 | — |
| [[F-075]] | Estrategias de captación de clientes en farmacias (punto de venta, fid | 🟠 D | Increnta / Asefarma (agencias de m | s.f. | — |
| [[F-081]] | Insurance NPS Benchmarks 2025 | 🟠 D | CustomerGauge / QuestionPro (agreg | 2025 | — |
| [[F-085]] | Compulsory motor third-party liability insurance — comparativa por paí | 🟠 D | The Zebra / European Commission /  | 2020-2024 | [[seguros-comportamiento-mundo-peru]] |
| [[F-086]] | Estadísticas de esperanza de vida y envejecimiento global | 🟠 D | Worldmetrics.org / Sogevity (agreg | 2026 | [[mecanismos-seguros-salud]] |
| [[F-113]] | CVS closes $10.6B acquisition of Oak Street Health | 🟠 D | Fierce Healthcare / Healthcare Div | 2023 | [[mecanismos-seguros-salud]] |
| [[F-126]] | Pricing Page Psychology 2026: A SaaS Decision Framework | 🟠 D | Digital Applied (blog de agencia/c | 2026 | [[material-visual-venta-consultiva]] |
| [[F-127]] | Comparativas Highspot vs. Seismic vs. Showpad — sales enablement | 🟠 D | Highspot / Seismic / diversos comp | 2026 | [[material-visual-venta-consultiva]] |
| [[F-129]] | Resúmenes derivados del caso HBS sobre la transición de HubSpot de out | 🟠 D | Fuentes secundarias (Medium, UKEss | s.f. | [[transicion-venta-fria-a-opt-in]] |
| [[F-130]] | Alineación de modelos de incentivos con objetivos estratégicos y creci | 🟠 D | Bain & Company (citado vía blogs d | s.f. | [[transicion-venta-fria-a-opt-in]] |
| [[F-133]] | Assurance IQ TCPA Settlement — Lessons Learned | 🟠 D | CompliancePoint / National Law Rev | 2024-2025 | [[transicion-venta-fria-a-opt-in]] |
| [[F-134]] | 35 Biggest TCPA Lawsuits Ever | 🟠 D | Leadshook (blog legal/marketing, a | 2025 | [[transicion-venta-fria-a-opt-in]] |
| [[F-136]] | Cambios de State Farm, Allstate y ascenso de Progressive por venta dir | 🟠 D | Insurance Business Magazine / Live | 2026 | [[transicion-venta-fria-a-opt-in]] |
| [[F-139]] | Why Cold Calling is Dead: The Shift to Relationship-Based Selling | 🟠 D | New Sales Expert (blog de práctica | s.f. | [[transicion-venta-fria-a-opt-in]] |
| [[F-140]] | Consent-Based Marketing: Turning Privacy into Business Growth | 🟠 D | Seers AI (blog de proveedor de ges | s.f. | [[transicion-venta-fria-a-opt-in]] |
| [[F-146]] | Designing for UX Trust: Security, Privacy & Transparency | 🟠 D | Think Design / MoldStud (blogs de  | s.f. | — |
| [[F-155]] | AI Customer Service Benchmark 2026 / AI Customer Support Resolution Ra | 🟠 D | Aissist.io / Notch.cx (blogs de pr | 2026 | [[evaluacion-calidad-agentes-conversacionales-ia]] |
| [[F-160]] | U.S. P/C Insurers Post Biggest Q1 Underwriting Profit in 25 Years | 🟠 D | AM Best (vía Carrier Management) | 2026 | — |
| [[F-165]] | Triggers paramétricos y reducción de costos de siniestros | 🟠 D | Swiss Re Institute (citado vía Ins | 2026 | — |
| [[F-166]] | UK insurers warned privacy concerns are stalling telematics pricing ad | 🟠 D | Insurance Business Mag (UK) | 2026 | — |
| [[F-167]] | Telematics and Trust: How Usage-Based Insurance Is Transforming Auto C | 🟠 D | Carrier Management | 2026 | — |
| [[F-168]] | Lemonade backtracks AI comments after accusations of discrimination | 🟠 D | Forbes / Claims Journal (cobertura | 2021 | — |
| [[F-174]] | BBVA es multado por publicidad engañosa: campaña 'Preaprobado para ti' | 🟠 D | Infobae | 2025 | [[material-visual-venta-consultiva]] |
| [[F-177]] | The trust gap: why incomplete product information is crushing conversi | 🟠 D | Retail Times | s.f. | [[material-visual-venta-consultiva]] |
| [[F-179]] | How lifestyle content can significantly increase your ecommerce conver | 🟠 D | Creatively Squared (blog de agenci | s.f. | [[material-visual-venta-consultiva]] |
| [[F-185]] | Life insurers still favor face-to-face sales in digital era | 🟠 D | The Korea Times | 2025 | [[futuro-asesores-seguros-venta-digital]] |
| [[F-186]] | Digital Insurance Grown 20 Times but Traditional Channels Still Domina | 🟠 D | Fintech Hong Kong (vía informe KPM | s.f. | [[futuro-asesores-seguros-venta-digital]] |
| [[F-187]] | Killing of UnitedHealthcare CEO prompts flurry of stories on social me | 🟠 D | CNN Business | 2024 | [[futuro-asesores-seguros-venta-digital]] |
| [[F-188]] | How patients are using AI to fight back against denied insurance claim | 🟠 D | PBS NewsHour | s.f. | [[futuro-asesores-seguros-venta-digital]] |
| [[F-189]] | Lemonade's Improving Loss Ratio Is the Real Story | 🟠 D | The Motley Fool (cobertura de resu | 2026 | [[futuro-asesores-seguros-venta-digital]], [[proyecto-back-to-basics-ffvv-vida]] |
| [[F-196]] | Global Insurance Growth Slows To 1.3% In 2026 As Fragmentation Reshape | 🟠 D | Risk & Insurance (prensa especiali | 2026 | [[mecanismos-seguros-salud]] |
| [[F-201]] | GLP-1s, Specialty Spend, and a 9% Cost Surge: Why Employers Must Rethi | 🟠 D | MedCity News | 2026 | [[mecanismos-seguros-salud]] |
| [[F-204]] | Bupa group profit down to £725m but premiums push up UK insurance and  | 🟠 D | Health & Protection (prensa especi | 2026 | [[mecanismos-seguros-salud]] |
| [[F-205]] | Niva Bupa closes March 2026 quarter with 67% profit jump | 🟠 D | Insurance Business Asia (prensa es | 2026 | [[mecanismos-seguros-salud]] |
| [[F-208]] | 9 Best Stocks To Buy Now For July 2026 / Best Stocks to Buy Now for Ju | 🟠 D | Forbes / Zacks | 2026 | — |
| [[F-209]] | My Top Ranked Stock to Buy Right Now in July (2026) / Best Stocks to B | 🟠 D | The Motley Fool | 2026-07-03 | — |
| [[F-212]] | 'Yet another way in which 2026 is looking like 1999' / Investors grow  | 🟠 D | Fortune / eciks.org | 2026-06-08 y 2026-07 | — |
| [[F-213]] | Acciones peruanas para invertir en la BVL: análisis y perspectivas 202 | 🟠 D | Rankia Perú / trii.pe | 2026 | — |
| [[F-214]] | SAB LOCALES COMPARTEN SUS TOP PICKS PARA LA BVL EN EL 2026 | 🟠 D | Borsista.com (compilación de casas | 2026 | — |
| [[F-215]] | Bolsa de Valores de Lima: Ganancias de empresas rompen marca histórica | 🟠 D | Gestión.pe | 2026 | — |
| [[F-233]] | Comprensión de las pólizas y falta de confianza, principales dificulta | 🟠 D | SegurosNews | 2025-2026 (fecha exacta no verificada) | [[glosario-seguro-vida-peru]] |
| [[F-234]] | La declaración del riesgo/salud en el seguro de vida: consecuencias de | 🟠 D | Múltiples (Almacén de Derecho, Map | Vigente 2026 | [[glosario-seguro-vida-peru]] |
| [[F-273]] | Critical Analysis: Why McKinsey's "The Business Value of Design" Misst | 🟠 D | Mauro Usability Science | 2023 | [[tendencias-diseno-innovacion]] |
| [[F-283]] | AI is now the leading reason companies give for cutting jobs | 🟠 D | CNBC / Challenger, Gray & Christma | 2026 | [[tendencias-diseno-innovacion]] |
| [[F-287]] | Vol. XXXII: The Slop Rebellion | 🟠 D | Eidos Design (Substack) | 2026 | [[tendencias-diseno-innovacion]] |
| [[F-288]] | Anti-AI Crafting: The $50 Million Handmade Rebellion | 🟠 D | Sykes, G. (Landor), vía Design Mag | 2026 | [[tendencias-diseno-innovacion]] |
| [[F-290]] | Apple is tweaking its controversial Liquid Glass design | 🟠 D | TechCrunch | 2026 | [[tendencias-diseno-innovacion]] |
| [[F-291]] | 'Tinted' control in iOS 26.1 beta 4 tones down Liquid Glass | 🟠 D | Gulf News | 2025-2026 | [[tendencias-diseno-innovacion]] |
| [[F-292]] | Cómo cambia Liquid Glass en iOS 27 — slider de transparencia | 🟠 D | MacRumors / 9to5Mac | 2026 | [[tendencias-diseno-innovacion]] |
| [[F-294]] | Lovable review · Figma Make vs Lovable | 🟠 D | Superblocks / Bonanza Studios | 2026 | [[tendencias-diseno-innovacion]] |
| [[F-295]] | Canva Unveils 2026 Design Trends: 'Imperfect by Design' | 🟠 D | Canva (vía Businesswire) | 2025 | [[tendencias-diseno-innovacion]] |
| [[F-296]] | ChatGPT Images 2.0 has people declaring the death of graphic design... | 🟠 D | Creative Bloq | 2026 | [[tendencias-diseno-innovacion]] |
| [[F-297]] | Retro & brutalist UI field guide 2026 | 🟠 D | Setproduct / Fireart | 2026 | [[tendencias-diseno-innovacion]] |
| [[F-302]] | 5by5: el futuro del service design · contratos que citan "Service Desi | 🟠 D | Service Design Network / ITJobsWat | 2026 | [[tendencias-diseno-innovacion]] |
| [[F-316]] | IDEO invented 'human-centered design.' Can it survive an AI world? | 🟠 D | Fortune | 2026 | [[tendencias-diseno-innovacion]] |
| [[F-317]] | Design giant IDEO cuts a third of staff and closes offices | 🟠 D | Fast Company (Wilson, M.) | 2023 | [[tendencias-diseno-innovacion]] |
| [[F-318]] | Anthropic launches Claude Design, challenges Figma | 🟠 D | VentureBeat | 2026 | [[tendencias-diseno-innovacion]] |
| [[F-319]] | Design tech's hot mess: Claude Design vs. Adobe, Canva, Figma | 🟠 D | Fast Company | 2026 | [[tendencias-diseno-innovacion]] |
| [[F-320]] | Lovable reportedly in talks to double its valuation to $13.2B | 🟠 D | TechCrunch (Temkin, M.) | 2026 | [[tendencias-diseno-innovacion]] |
| [[F-321]] | Lovable raises $330M to power the age of the builder | 🟠 D | Lovable | 2025 | [[tendencias-diseno-innovacion]] |
| [[F-322]] | Perfiles de Framer / Webflow / Bolt.new / Vercel | 🟠 D | Sacra | 2025-2026 | [[tendencias-diseno-innovacion]] |
| [[F-323]] | Canva delays IPO until 2027 as it beds down Canva AI 2.0 | 🟠 D | Capital Brief | 2026 | [[tendencias-diseno-innovacion]] |
| [[F-324]] | Canva gets to $4B in revenue as LLM referral traffic rises | 🟠 D | TechCrunch | 2026 | [[tendencias-diseno-innovacion]] |
| [[F-325]] | Accenture Song absorbed into new Reinvention Services line | 🟠 D | Consultancy.uk | 2026 | [[tendencias-diseno-innovacion]] |
| [[F-326]] | Cobertura de la caída de la acción de Figma (FIG) | 🟠 D | Parameter / TIKR / TradingKey | 2026 | [[tendencias-diseno-innovacion]] |
| [[F-328]] | The Total Economic Impact™ of InVision | 🟠 D | Forrester Consulting (comisionado  | 2019 | [[tendencias-diseno-innovacion]] |
| [[F-332]] | Medical Mutual Nurse Triage Case Study | 🟠 D | Conduit Health Partners | s.f. | — |
| [[F-347]] | Quejas recurrentes sobre 98point6: deriva a urgent care sin tratar, co | 🟠 D | Reviews de usuarios vía Trustpilot | s.f. | — |
| [[F-348]] | Quejas sobre Included Health/Doctor On Demand: negativa a recetar, pub | 🟠 D | Reviews de usuarios vía BBB / Trus | s.f. | — |
| [[F-350]] | Plan "virtual-first" de Priority Health — ~5,000 inscritos, 60% de enc | 🟠 D | KFF Health News, BusinessWire | 2020-2021 | — |
| [[F-354]] | How a remote nurse-first triage model reduces benefits spend for emplo | 🟠 D | Patient Safety & Quality Healthcar | s.f. | — |
| [[F-361]] | Trayectoria de loss ratio de Lemonade: 166% (2017) → 86% (2019) → ~90% | 🟠 D | Fuente no especificada en el deck  | 2017-2022 | [[proyecto-back-to-basics-ffvv-vida]] |
| [[F-363]] | Ethos IPO tests 2026 market as insurtech rivals crumble | 🟠 D | TechBuzz AI / IPOScoop (cobertura  | 2026 | [[futuro-asesores-seguros-venta-digital]] |
| [[F-365]] | Bowtie: From Startup To Top 10 Life Insurer in Just 5 Years / Hong Kon | 🟠 D | PR Newswire / InsurTech Digital (c | 2025 | [[futuro-asesores-seguros-venta-digital]] |
| [[F-369]] | Life Insurance Industry Trends 2026: From Record Sales to a Generation | 🟠 D | actuary.info (agregación de tenden | 2026 | [[futuro-asesores-seguros-venta-digital]] |
| [[F-371]] | "Bowtie: From Startup To Top 10 Life Insurer in Just 5 Years" / "Bowti | 🟠 D | Bowtie (blog propio, comunicado) + | 2023-2026 | [[futuro-asesores-seguros-venta-digital]] |
| [[F-373]] | El nuevo modelo de negocio de Betterfly / Betterfly (Wikipedia) | 🟠 D | Endeavor Hub, Wikipedia (ES), Mark | s.f. | [[venta-vida-digital-hibrida-latam]] |
| [[F-390]] | Basura visual: la IA omnipresente que está desatando una corriente est | 🟠 D | Xataka (España) | 2026 | [[tendencias-diseno-innovacion]] |
| [[F-392]] | Las tecnológicas concretaron más de 45.000 despidos en lo que va de 20 | 🟠 D | Ámbito, FayerWayer, Bloomberg Líne | 2026 | [[tendencias-diseno-innovacion]] |
| [[F-393]] | Service Design: What's Next? | 🟠 D | Aricò, M. (Design Mavericks) | 2025-2026 | [[tendencias-diseno-innovacion]] |
| [[F-394]] | Service Design Lima — Jam Lima 2026 · Cafecito SDL "El Diseño en evolu | 🟠 D | Service Design Lima (comunidad) | 2017-2026 | [[tendencias-diseno-innovacion]] |
| [[F-395]] | Service Design Global Conference 2026 (Alemania + online, 28-30 oct) · | 🟠 D | Service Design Network (SDN) | 2026 | [[tendencias-diseno-innovacion]] |
| [[F-410]] | AI in Design 2026: la profesión cambió en doce meses | 🟠 D | Evidencia Creativa (blog, España), | 2026 | [[tendencias-diseno-innovacion]] |
| [[F-412]] | Figma Config 2026 (23-25 jun, San Francisco, +8.000 asistentes) | 🟠 D | Blog Trazos, UXCristopher, Qubika, | 2026 | [[tendencias-diseno-innovacion]] |
| [[F-414]] | Hilo sobre escasez de empleos junior en diseño | 🟠 D | Blind (teamblind.com) — comentario | 2026 | [[tendencias-diseno-innovacion]] |
| [[F-417]] | Confianza y adopción de IA en España, may-2026 | 🟠 D | El Dinamo, El Ecosistema Startup,  | 2026 | [[tendencias-diseno-innovacion]] |
| [[F-422]] | Crecimiento de R/GA: +30% H2'25 vs. H1'25; **+25% YoY en Q1 2026** | 🟠 D | R/GA (autorreportado), vía MMM-Onl | 2026 | [[tendencias-diseno-innovacion]] |
| [[F-423]] | 40+ Key UX Stats for 2026 | 🟠 D | Maze (maze.co) | 2026 | [[tendencias-diseno-innovacion]] |
| [[F-424]] | Improve Customer Experience with UX Investments that Increase ROI | 🟠 D | Interaction Design Foundation (IxD | recirculado 2026 | [[tendencias-diseno-innovacion]] |
| [[F-425]] | How to Measure Design System ROI in 2026 | 🟠 D | figr.design (vendor de gestión de  | 2026 | [[tendencias-diseno-innovacion]] |
| [[F-438]] | Managing Your Innovation Portfolio (*Harvard Business Review*) — orige | 🟠 D | Nagji, B. & Tuff, G. (Monitor Grou | 2012 | [[tendencias-diseno-innovacion]] |
| [[F-439]] | The Innovation Commitment — "8 esenciales de la innovación" y el "2,4x | 🟠 D | McKinsey & Company | ~2023 | [[tendencias-diseno-innovacion]] |
| [[F-455]] | Revenue FY2025 US$14,4B (+7% YoY, 22.º año consecutivo de crecimiento) | 🟠 D | Boston Consulting Group (comunicad | 2024-2026 | [[tendencias-diseno-innovacion]] |
| [[F-458]] | Ecosistema insurtech LatAm: 536 startups (2025) → 576 (1S 2026, +14%); | 🟠 D | MAPFRE Perú, El Ecosistema Startup | 2025-2026 | [[tendencias-diseno-innovacion]] |
| [[F-460]] | Labs de innovación corporativos peruanos activos (BCP **CIX**, Pacífic | 🟠 D | Forbes Perú (entrevista a BCP, 202 | 2022-2025 | [[como-trabajan-equipos-diseno-referencias-2026-08-10]], [[tendencias-diseno-innovacion]] |
| [[F-462]] | "In Defense of Innovation Theater" (nov-2025) y su reamplificación (di | 🟠 D | Mile Zero (consultora de innovació | 2025 | [[tendencias-diseno-innovacion]] |
| [[F-463]] | Medio + eventos sobre innovación corporativa, con membresías desde US$ | 🟠 D | InnoLead (innovationleader.com) | 2024-2026 | [[tendencias-diseno-innovacion]] |
| [[F-464]] | "El teatro de la innovación" en español | 🟠 D | El Español (dic-2020), Forbes Méxi | 2020-2026 | [[tendencias-diseno-innovacion]] |
| [[F-472]] | Cynefin Domains / críticas a la validación empírica del marco | 🟠 D | Cynefin.io + literatura de crítica | 2024-2025 | [[metodologias-diseno-sistemas-complejos]], [[revision-modelo-trabajo-diseno-2026-08-10]] |
| [[F-477]] | "Why Design Thinking is bullshit" / "Design Thinking and the Theater o | 🟠 D | Jen, N. (Pentagram, vía It's Nice  | 2018-2021 | [[metodologias-diseno-sistemas-complejos]] |
| [[F-478]] | Is Design Thinking Still Relevant For Product Design In 2026? | 🟠 D | UX Army / hilos de practicantes (a | 2026 | [[metodologias-diseno-sistemas-complejos]] |
| [[F-485]] | The 2026 State of Customer Research Hiring: Why Teams Cut Researchers  | 🟠 D | Perspective AI | 2026 | [[como-trabajan-equipos-diseno-referencias-2026-08-10]] |
| [[F-493]] | El estilo del Centro de Innovación CIX BCP / Estructura del Centro de  | 🟠 D | Centro de InnovaCXión BCP (CIX), v | 2018-2019 | [[como-trabajan-equipos-diseno-referencias-2026-08-10]] |
| [[F-494]] | Laboratorios de innovación corporativos peruanos | 🟠 D | La Victoria Lab (grupo Intercorp)  | 2012-2026 | [[como-trabajan-equipos-diseno-referencias-2026-08-10]] |
| [[F-495]] | Centro de Excelencia (CoE) en Diseño de Experiencia | 🟠 D | RIMAC Seguros (perfiles institucio | 2025-2026 | [[como-trabajan-equipos-diseno-referencias-2026-08-10]] |
| [[F-498]] | Problems with the Center of Excellence Model | 🟠 D | ZeroBlockers (blog) atribuyendo el | 2024-2025 | [[como-trabajan-equipos-diseno-referencias-2026-08-10]] |
| [[F-499]] | How Mercado Libre Scales Design Across Latin America with Figma | 🟠 D | Figma (customer story sobre Mercad | 2025-2026 | [[como-trabajan-equipos-diseno-referencias-2026-08-10]] |
| [[F-500]] | Product Designer vs. Service Designer + Service designers and product  | 🟠 D | Miro (centro de recursos) + litera | 2021-2026 | [[como-trabajan-equipos-diseno-referencias-2026-08-10]] |
| [[F-506]] | Unidad de investigación conductual de la reaseguradora | 🟠 D | Swiss Re — Behavioural Research Un | 2013-2026 | [[analisis-final-modelo-trabajo-diseno-2026-08-10]] |
| [[F-507]] | La mayor escalada documentada de una función de diseño dentro de una e | 🟠 D | IBM Design — vía Adobe blog, Inc., | 2012-2017 | [[analisis-final-modelo-trabajo-diseno-2026-08-10]] |
| [[F-508]] | Organización de diseño de Nubank | 🟠 D | Nubank — blog de ingeniería "Build | 2022-2026 | [[analisis-final-modelo-trabajo-diseno-2026-08-10]] |
| [[F-509]] | Descripción institucional de la práctica de diseño del gobierno de Sin | 🟠 D | GovTech Singapur — Design Practice | 2023-2026 | [[analisis-final-modelo-trabajo-diseno-2026-08-10]] |
| [[F-520]] | Chatbot manipulado para "vender" una camioneta en US$1 como "oferta le | 🟠 D | Cobertura del incidente del conces | 2023-2026 | [[capacidades-asistente-ia-aseguradora]] |
| [[F-521]] | Sentimiento público sobre chatbots de atención en banca y seguros | 🟠 D | Prensa de consumo y agregadores de | 2023-2026 | [[capacidades-asistente-ia-aseguradora]] |
| [[F-522]] | Métricas de uso del asistente virtual Erica | 🟠 D | Bank of America — comunicados de p | 2024-2026 | [[capacidades-asistente-ia-aseguradora]] |
| [[F-524]] | Automatización de siniestros con AI Jim y cotización con Maya | 🟠 D | Lemonade — vía agregadores de caso | 2023-2026 | [[capacidades-asistente-ia-aseguradora]] |
| [[F-528]] | Fallas reportadas del symptom checker de Babylon | 🟠 D | Alegaciones públicas sobre el veri | 2018-2022 | [[capacidades-asistente-ia-aseguradora]] |
| [[F-537]] | Hallazgos AIDA — Encuesta a asesores (n=19) | 🟠 D | CoE de Diseño, RIMAC — encuesta a  | 2026 | [[aida-copiloto-asesor-rimac]], [[aida-historia-completa-post-owners-2026-08-19]], [[aida-objetivo-vs-diagnostico-2026-08-12]] |
| [[F-095]] | Market Design in Regulated Health Insurance Markets: Risk Adjustment v | 🔴 E | Tebaldi, P. (NBER Working Paper w3 | 2024 | — |
| [[F-099]] | "Largest behavior change study on physical activity" — Vitality + Appl | 🔴 E | Vitality Group (autopublicado) | s.f. | [[mecanismos-seguros-salud]] |
| [[F-116]] | Advancing Access to Healthcare Through Value-Based Primary Care / blog | 🔴 E | ChenMed (autopublicado, blog corpo | s.f. | [[mecanismos-seguros-salud]] |
| [[F-137]] | Hilos "New to Life Insurance....Tired of Cold Calling" y "Call Relucta | 🔴 E | Insurance-Forums.com (foro de ases | s.f. | [[back-to-basics-presentacion-milagros-2026-07-23]], [[transicion-venta-fria-a-opt-in]] |
| [[F-149]] | Chatbot Usability Questionnaire (CUQ) — "Towards Validating a Chatbot  | 🔴 E | Ulster University (tesis doctoral, | 2019/2023 | [[evaluacion-calidad-agentes-conversacionales-ia]] |
| [[F-227]] | The 10X Rule: The Only Difference Between Success and Failure (libro d | 🔴 E | Cardone, G. | 2011 | [[proyecto-back-to-basics-ffvv-vida]] |
| [[F-235]] | "¿Vale la pena contratar/pagar un seguro de vida?" (patrón recurrente  | 🔴 E | Quora (hispanohablante, múltiples  | Vigente 2026 | [[glosario-seguro-vida-peru]] |
| [[F-279]] | UX/UI Design Trends 2026 (reportes de tendencias de fabricantes de her | 🔴 E | UXPin, Envato, Stan.vision y otros | 2026 | [[tendencias-diseno-innovacion]] |
| [[F-286]] | Manifiesto SLOPLESS (X / LinkedIn / slopless.design) | 🔴 E | Malewicz, M. | 2025-2026 | [[tendencias-diseno-innovacion]] |
| [[F-289]] | "Steve Jobs would have fired everyone" — captura del Control Center de | 🔴 E | @Greggertruck (X), vía Notebookche | 2025 | [[tendencias-diseno-innovacion]] |
| [[F-293]] | Hilos de feedback sobre Figma Make / Config | 🔴 E | Foro oficial de Figma (usuarios) | 2025-2026 | [[tendencias-diseno-innovacion]] |
| [[F-299]] | Respuestas a Jakob Nielsen ("la IA invalidará el proceso manual de dis | 🔴 E | Agory / UX Collective / Bootcamp ( | 2026 | [[tendencias-diseno-innovacion]] |
| [[F-300]] | The mirage of UX Design's demise keeps coming back | 🔴 E | Berumen Castro, L. (UX Collective) | 2026 | [[tendencias-diseno-innovacion]] |
| [[F-301]] | Nobody knows what a designer is right now | 🔴 E | Tocker, L. (Substack) | 2026 | [[tendencias-diseno-innovacion]] |
| [[F-327]] | "Los design systems dan 671% de ROI (Forrester)" | 🔴 E | Blogs de agencia y posts de Linked | 2024-2026 | [[tendencias-diseno-innovacion]] |
| [[F-397]] | One Formula To Rule Them All: The ROI Of A Design System | 🔴 E | Smashing Magazine | 2022 | [[tendencias-diseno-innovacion]] |
| [[F-404]] | Why Sr. Devs Are Actually Less Productive with AI Copilot — DZone | 🔴 E | Autoría no declarada (blog sin arb | 2025 | [[tendencias-diseno-innovacion]] |
| [[F-408]] | Descubre cómo evoluciona el UX/UI en 2026 | 🔴 E | IEM Business School (iembs.com), c | 2026 | [[tendencias-diseno-innovacion]] |
| [[F-409]] | Tendencias UX/UI 2026: Diseño web y app que convierte | 🔴 E | Doonamis (agencia de desarrollo we | 2026 | [[tendencias-diseno-innovacion]] |
| [[F-411]] | Las tendencias de diseño gráfico más interesantes para 2026 · Canva pr | 🔴 E | The Power Business School (thepowe | 2025-2026 | [[tendencias-diseno-innovacion]] |
| [[F-413]] | UX 2026: despidos, IA y la pregunta incómoda… ¿tocó volverse generalis | 🔴 E | Podcast UX Friends, Ep. 93 | 2026 | [[tendencias-diseno-innovacion]] |
| [[F-415]] | Muestra del ciclo "UX is dead / el diseño ha muerto" (n≈8 piezas, may- | 🔴 E | Medium (Design Bootcamp, Muzli), S | 2026 | [[tendencias-diseno-innovacion]] |
| [[F-440]] | Ten Types of Innovation | 🔴 E | Doblin / Keeley, L. (hoy Deloitte  | s/f (marco vigente) | [[tendencias-diseno-innovacion]] |
| [[F-444]] | "El 90% de los innovation labs corporativos fracasa" · "El 70-90% del  | 🔴 E | Blogs de consultoría y plataformas | 2016-2026 | [[tendencias-diseno-innovacion]] |
| [[F-445]] | "Cooper: 24% de éxito con procesos ad hoc vs. 63-78% con Stage-Gate" | 🔴 E | Stage-Gate International y Cora Sy | ~2017 | [[tendencias-diseno-innovacion]] |
| [[F-453]] | "Innovation Premium" — base del ranking *World's Most Innovative Compa | 🔴 E | Forbes / HOLT (Credit Suisse) — pá | 2011-2012 | [[tendencias-diseno-innovacion]] |
| [[F-459]] | Mercado de *innovation management software*: US$1,25B (2024) → US$3,5B | 🔴 E | Reportes de mercado agregados (ope | 2024-2026 | [[tendencias-diseno-innovacion]] |
| [[F-468]] | Hilo sobre despidos e innovación en *big tech* | 🔴 E | Blind (teamblind.com) | s/f | [[revision-modelo-trabajo-diseno-2026-08-10]], [[tendencias-diseno-innovacion]] |
