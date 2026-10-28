# Auditoría de acceso a fuentes y lista de notas de Gestión por abrir

> Fecha: 2026-10-28 · Estado: documento de trabajo. Cubre el ciclo de digitalización de seguros (nodes `digitalizacion-seguros-mercados-emergentes`, `digitalizacion-ramos-vehicular-salud-microseguros`, `foresight-experiencia-futura-seguros-digitalizacion`, `economia-plateada-seguros-peru-latam`, `hipotesis-digitalizacion-seguros-evidencia-publica`, `economia-conductual-seguros-literatura`).
> Solo fuentes públicas. Los enlaces de la parte 2 son los que devolvió el buscador; **no los abrí**.

---

## Parte 1. Qué pude leer y qué no

### 1.1 Lo que se puede comprobar en el registro de la sesión

| Hecho | Cifra |
|---|---|
| Intentos de abrir una página web con la herramienta de lectura de páginas | **35** |
| Intentos que funcionaron | **0** (todos fallaron porque el dominio no resuelve desde la sesión) |
| Búsquedas web realizadas | ~370; devuelven títulos, enlaces y un resumen del buscador |
| Archivos que la persona usuaria subió y yo leí | 18 (lista abajo) |
| Fichas del ledger registradas en esta sesión (F-847 a F-1187) | 341 |

**Consecuencia.** Todo lo que no vino de un archivo subido se apoya en un **resumen de buscador** o en un titular. Los nodes lo decían ("lectura por extractos"), pero no siempre con la claridad de que *ninguna* página web se abrió.

### 1.2 Qué leí desde archivos

"Parte pertinente" significa que leí lo que se usa (resumen, introducción, resultados, limitaciones o los pasajes buscados), no página por página, salvo que se indique.

| Archivo aportado | Qué leí |
|---|---|
| Diagnóstico de microseguros en el Perú (PNUD) | Resumen ejecutivo, mercado, percepción y recomendaciones |
| McKinsey, *Global Insurance Report 2023* (América Latina) | Pasajes sobre consumidores, digital y Perú |
| Coloma, documento de la Universidad Católica (Chile, licitación de seguros) | Resumen ejecutivo y búsqueda de cifras |
| Milliman, *MILK Brief 16* (microseguro de vida en México) | La mayor parte |
| Informe del Índice de Inclusión Financiera 2026 (Credicorp) | Partes pertinentes |
| Accenture, *People Before Policies* (PDF y docx) | Partes pertinentes |
| Capgemini, *World Property & Casualty Insurance Report 2024* (PDF y docx) | Partes pertinentes |
| Folleto de seguros en Latinoamérica (Deloitte) | Completo |
| Artículo de economía conductual en seguros (Universidad de Lima, docx) | Completo; citas verificadas |
| Pérez-Llorca, *Actualidad Iberoamericana de Seguros*, T3 2026 (docx) | Partes pertinentes |
| Desk research de canales digitales (deck PDF) | Pertinentes; cada cifra verificada o marcada |
| Wallace y colaboradores, *npj Digital Medicine* 2022 | Resumen, introducción y resultados |
| Mafi y colaboradores, *JAMA Network Open* 2026 | Resumen, introducción, limitaciones |
| Aihara, Kawachi y Sommers, *JMIR* 2025 | Resumen, introducción |
| Nota de política de Stanford HAI, febrero de 2026 | Primeras páginas y búsqueda de cifras |
| Ficha de CHBRP (California), julio de 2026 | Completa (una página) |
| Preprint de arXiv 2605.23465 | Resumen e introducción |
| Estudio interno de exploración (confidencial) | Leído fuera del repositorio; **nada se versionó** |

**Corrección de mi parte.** En el mensaje anterior dije que había leído "completos" los seis PDFs de salud. Solo la ficha de CHBRP se leyó entera. Los demás los leí en sus partes pertinentes. Ya corregí esa palabra en el ledger y en el node.

### 1.3 Qué hay detrás de cada tipo de fuente

| Nivel de lectura | Qué es | Fichas aproximadas | Cómo tratar la cifra |
|---|---|---|---|
| **N1. Leído en un archivo** | PDF o docx subido | hasta ~30 fichas mencionan estos documentos o a sus autores; **no todas sus cifras vienen del archivo** (algunas citan al mismo autor a través de prensa) | Se puede citar con su página; verificar el resto del documento si la decisión es grande |
| **N2. Fragmento de buscador o nota de prensa** | Resumen del buscador de un artículo, informe o estudio | el resto, unas ~300 fichas (según una clasificación por palabras clave, ~160 lo dicen en la ficha y **~160 no indican cómo se leyeron**; por defecto es este nivel). El conteo es aproximado | Tomar como **pista**, no como dato; abrir la fuente antes de citar |
| **N3. Solo titular** | Titular de una lista de noticias | 6 fichas | No usar la cifra |

**Hallazgo sobre el ledger.** La ficha no tiene una columna que diga cuánto se leyó. La rúbrica A a E mide el tipo de fuente, no mi nivel de acceso. Propongo agregar una columna "Nivel de lectura (N1, N2, N3)". No la agrego sin tu autorización porque cambia la estructura del ledger.

### 1.4 Errores que ya detecté y corregí en este ciclo

1. Plin por WhatsApp: "7.000 afiliados" y "2,7 millones de activos" no se pudieron reproducir; los retiré.
2. "90% de banca móvil" era de México, no del Perú.
3. McKinsey "25.000 personas en 7 países": no localizable; reemplazado por McKinsey y LIMRA 2022.
4. Chile: la baja de primas de la licitación no era −59,53% sino −62,1% (desgravamen) y −34,3% (incendio y sismo).
5. El 63% de la lámina era de Capgemini, no de Accenture.
6. IIF Credicorp "49% a 40%": era el porcentaje que no usó ningún producto financiero en el mes.
7. "Leído completo" estaba sobrestimado para PNUD, McKinsey, Coloma, IIF y Accenture.
8. El "microseguro de S/ 4,90" era un ejemplo (Celu Seguro de Pacífico en Yape), no un microseguro legal.
9. JAMA Network Open es de **2026**, no 2025, y los autores no leen su resultado como "sustitución".
10. El artículo de JMIR es un estudio de Japón (gasto total −1,0%), no una revisión.
11. Wallace: no confirmé el "78,6% de subtriaje".
12. Stanford HAI: la cifra de la AMA (61%) y el caso Cigna no están en la nota.
13. CHBRP es de California; el 26,3% de Medicare y los datos de ASPE no están ahí.
14. El preprint de arXiv es un banco de pruebas con viñetas sintéticas; lo de Babylon y Kenia es de segunda mano.
15. Dije "leí completos" los seis PDFs: era sobrestimado.

### 1.5 Qué considero sólido y qué no (por tema)

| Tema | Sólido (N1, con método) | Frágil (N2 o N3) |
|---|---|---|
| Microseguros en el Perú | PNUD: 5,8 millones de asegurados, siniestralidad de 16,7%, 97,8% por entidades financieras | Penetración de la oferta digital |
| Microseguro de vida en México | Milliman (MILK Brief 16) | Casos de Zambia y otros países |
| Telemedicina y gasto | Mafi (EE. UU., nulo) y Aihara (Japón, −1,0%) | Estudio de 2017 de telemedicina directa; "25 de 31" de una revisión citada |
| Triaje automático | Wallace (10 estudios) | Preprint de Kenia y Ruanda; quioscos de urgencias |
| IA en seguros de salud | Nota de HAI (84% de aseguradores usan IA) | AMA y Cigna |
| Brecha digital en telesalud | CHBRP (California) | Medicare 26,3%, ASPE, RAND |
| Recordatorios de cita | Cochrane (leída por resumen) | Aplicación a seguros: hipótesis |
| Vida, ahorro e inversión | Nada propio leído en archivo | **Todo**: LIMRA, persistencia en India, Anagol, D'Acunto, SOA, caducidad |
| Open banking en el Perú | Pérez-Llorca T3 2026 (docx) | Gestión, BCRP, SBS: fragmentos |
| Pacífico Salud, Yape, Sanna | Nada | **Todo**: fragmentos de Gestión, declaraciones de la empresa |
| SOAT y vehicular | Nada propio leído en archivo | **Todo**: gremio y prensa |

**Lectura honesta.** Los hallazgos de microseguros, telemedicina, triaje, IA en seguros de salud y brecha digital descansan sobre al menos un documento leído. **Vida, ahorro e inversión, SOAT y vehicular, Pacífico Salud, Yape y open banking descansan sobre fragmentos.** Con esas áreas hay que ser más cautos al decidir.

### 1.6 Cómo cerrar el hueco

1. **Subir o pegar** las fuentes de la parte 2 en lotes, empezando por las de prioridad 1.
2. Si quieres que yo abra páginas, agregar los dominios en la configuración de red del entorno (menú del entorno, *Edit*, *Allowed domains*). Para Gestión no basta: tiene muro de pago.
3. **Documentos de pago o de acceso restringido que valdría la pena subir** (PDF o copia): Cochrane CD007458 (recordatorios), Anagol, Cole y Sarkar, D'Acunto, Prabhala y Rossi, Martinez 2018, Graetz 2024, informe de la SOA sobre suscripción acelerada.
4. Con tu autorización, agregar la columna de nivel de lectura al ledger y marcar N1/N2/N3 en las fichas de este ciclo.

---

## Parte 2. Notas de Gestión que conviene abrir

**Cómo estructurarlo.** Pega cada nota con este encabezado, en lotes de hasta 5 y en el orden de prioridad:

```
G-xx · fecha de publicación · titular · URL
[cuerpo del artículo, tal cual]
```

Si prefieres PDF, imprime la nota desde tu sesión de suscriptor (Imprimir, Guardar como PDF) y súbela con el nombre `G-xx.pdf`. La fecha de publicación es lo más importante: varias notas que devolvió el buscador son de 2019 a 2023 y las cifras pueden estar vencidas.

**Prioridad.** 1 = cambia una conclusión o valida una cifra clave. 2 = contexto útil. 3 = antigua, publirreportaje o de baja utilidad.

### A. Salud (aseguradoras, clínicas, telemedicina, EsSalud)

| ID | Pri. | Titular | Qué resuelve | URL |
|---|---|---|---|---|
| G-01 | 1 | Yape espera afiliar a su seguro de salud a 30,000 usuarios en su primer año | Meta, precio, cobertura y fecha del Seguro Salud Yape; cifra de 17 millones de usuarios | https://gestion.pe/economia/empresas/yape-espera-afiliar-a-su-seguro-de-salud-a-30000-usuarios-en-su-primer-ano-noticia/ |
| G-02 | 1 | Pacífico Salud triplica su inversión en innovación: los proyectos en carpeta con Sanna y clínicas | 3% frente a 1% de los ingresos; Tsana con 90.000 suscriptores; qué mide cada cifra | https://gestion.pe/economia/empresas/pacifico-salud-triplica-su-inversion-en-innovacion-los-proyectos-en-carpeta-con-sanna-y-clinicas-noticia/ |
| G-03 | 1 | Pacífico Salud: las nuevas zonas que expandirá su red de clínicas y los segmentos a los que apunta | Meta de 12 millones; "50% virtual"; piloto de bajo costo en Lima Norte | https://gestion.pe/economia/empresas/pacifico-salud-las-nuevas-zonas-expandira-su-red-de-clinicas-y-los-segmentos-a-los-que-apunta-noticia/ |
| G-04 | 3 | Pacífico Salud proyecta culminar en 2027 la ampliación de SANNA Clínica San Borja (publirreportaje) | Inversión de US$ 35 millones; camas | https://gestion.pe/publirreportaje/pacifico-salud-proyecta-culminar-en-2027-la-ampliacion-de-sanna-clinica-san-borja-tras-inversion-de-us35-millones-noticia/ |
| G-05 | 1 | Telemedicina en el Perú: ¿cuáles son las especialidades más demandadas por los pacientes? | Qué se consulta por telemedicina; origen de la cifra | https://gestion.pe/economia/empresas/telemedicina-en-el-peru-cuales-son-las-especialidades-mas-demandadas-por-los-pacientes-noticia/ |
| G-06 | 2 | Telemedicina, el reto de atender la salud a través de apps y videollamadas | Barreras de adopción | https://gestion.pe/tendencias/telemedicina-el-reto-de-atender-la-salud-a-traves-de-apps-y-videollamadas-noticia/ |
| G-07 | 2 | Mapfre Perú: los planes de expansión de la aseguradora (Clínica Digital) | Si la Clínica Digital sigue y con qué uso | https://gestion.pe/economia/empresas/mapfre-peru-los-planes-de-expansion-de-la-aseguradora-para-el-2023-aseguradoras-polizas-noticia/ |
| G-08 | 2 | La expansión de Sanna con centros médicos y la estrategia digital detrás | Qué hace la estrategia digital de Sanna | https://gestion.pe/economia/empresas/la-expansion-de-sanna-con-centros-medicos-y-la-estrategia-digital-detras-empresas-salud-privada-centros-medicos-noticia/ |
| G-09 | 2 | Sanna expandirá centros médicos accesibles y evalúa proyecto en Arequipa | Segmentos de menor ingreso | https://gestion.pe/economia/empresas/sanna-expandira-centros-medicos-accesibles-y-evalua-proyecto-en-arequipa-noticia/ |
| G-10 | 2 | Pacífico Salud en 2025: con la mayor inversión en últimos dos años para nuevas sedes | Contexto de inversión | https://gestion.pe/economia/empresas/pacifico-salud-en-2025-con-la-mayor-inversion-en-ultimos-dos-anos-para-nuevas-sedes-clinicas-salud-provincias-lima-san-juan-de-lurigancho-san-borja-lima-norte-noticia/ |
| G-11 | 1 | Aplicativo EsSalud para sacar citas: ¿cómo ayuda a reducir colas? | Qué hace la app y desde cuándo | https://gestion.pe/peru/aplicativo-essalud-para-sacar-citas-como-ayuda-a-reducir-colas-y-que-servicios-ofrece-app-essalud-mi-consulta-tramites-noticia/ |
| G-12 | 1 | INEI: se eleva el tiempo para programar una cita médica en los centros de salud pública | Esperas medidas (10,4 días en 2019, 25,2 en 2025, según un fragmento) | https://gestion.pe/economia/inei-se-eleva-el-tiempo-para-programar-una-cita-medica-en-los-centros-de-salud-publica-noticia/ |
| G-13 | 2 | EsSalud: déficit de caja sería cercano a S/ 2,000 millones | Presión financiera del seguro social | https://gestion.pe/economia/essalud-deficit-llegaria-a-s-2000-millones-en-2026-noticia/ |
| G-14 | 2 | Envejecimiento acelerado en Perú pone "en jaque" a EsSalud | Vínculo con economía plateada | https://gestion.pe/economia/envejecimiento-acelerado-en-peru-pone-en-jaque-a-essalud-que-riesgos-aparecen-noticia/ |
| G-15 | 1 | Peruanos afiliados al SIS, EsSalud y seguros privados: INEI reporta crecimiento | **Cobertura real de seguro privado** (reconcilia 3%, 4,5%, 13% y 18% de fuentes distintas) | https://gestion.pe/peru/peruanos-afiliados-al-sis-essalud-y-seguros-privados-inei-reporta-crecimiento-noticia/ |
| G-16 | 2 | La salud como negocio: el papel de provincias y el "ticket" limeño por consulta | Precio por consulta y presencia de seguros | https://gestion.pe/economia/empresas/tras-el-negocio-de-la-salud-presencia-seguros-y-costos-de-la-oferta-privada-y-publica-noticia/ |
| G-17 | 2 | Se recupera número de asegurados a EPS tras disminuir en el 2020 | Tamaño de las EPS | https://gestion.pe/economia/se-recupera-numero-de-asegurados-a-entidades-prestadoras-de-salud-tras-disminuir-en-el-2020-noticia/ |
| G-18 | 2 | Costo de atención en EPS podría elevarse, ¿cuál sería el detonante? | Presión de costos | https://gestion.pe/economia/mercados/costo-de-atencion-en-eps-podria-elevarse-cual-seria-el-detonante-noticia/ |
| G-19 | 3 | Indecopi da luz verde a compra del Grupo Credicorp con Empresas Banmédica | Integración vertical | https://gestion.pe/economia/empresas/indecopi-da-luz-verde-a-compra-del-grupo-credicorp-con-empresas-banmedica-pacifico-salud-banco-de-credito-grupo-credito-noticia/ |

### B. Farmacias y datos de salud

| ID | Pri. | Titular | Qué resuelve | URL |
|---|---|---|---|---|
| G-20 | 2 | Gobierno alerta "hackeo" a Inkafarma: datos de más de 3 millones de clientes se habrían filtrado | Riesgo de datos si se integran farmacia y seguro | https://gestion.pe/peru/gobierno-alerta-hackeo-a-inkafarma-datos-de-mas-de-3-millones-de-clientes-se-habrian-filtrado-noticia/ |
| G-21 | 3 | Intercorp lanza Mifarma Prime | Estrategia de formatos; **no** trata seguros | https://gestion.pe/g-de-gestion/mifarma-prime-esta-es-la-nueva-propuesta-de-intercorp-con-su-cadena-de-farmacias-noticia/ |

*No hallé nota de Gestión sobre convenios entre cadenas de farmacias y aseguradoras. Si la conoces, pásala.*

### C. Insurtech y canales digitales

| ID | Pri. | Titular | Qué resuelve | URL |
|---|---|---|---|---|
| G-22 | 1 | Interseguro: "Hemos lanzado un seguro vehicular 100% digital…" | Baja de 30% del SOAT por canal directo (declaración de la empresa) | https://gestion.pe/economia/interseguro-hemos-lanzado-un-seguro-vehicular-100-digital-que-nos-permite-trasladar-eficiencias-al-consumidor-noticia/ |
| G-23 | 2 | Mónica García: "WhatsApp es más efectivo que Messenger en la venta de seguros" | Evidencia sobre WhatsApp en venta (Rímac) | https://gestion.pe/tu-dinero/finanzas-personales/monica-garcia-whatsapp-es-mas-efectivo-que-messenger-en-la-venta-de-seguros-noticia/ |
| G-24 | 2 | Insurtechs: el futuro del sector seguros | Panorama (puede ser antiguo) | https://gestion.pe/panelg/fotos-insurtechs-hacia-donde-va-futuro-sector-seguros-2209598 |
| G-25 | 2 | Sector seguros: a la caza del cliente digital | Cifras de venta en línea (21% de pólizas; 67% prefiere buscar en línea) | https://gestion.pe/panelg/fotos-sector-seguros-caza-nuevo-cliente-digital-2209754 |
| G-26 | 3 | Avla lanza insurtech para asegurar viviendas | Caso Iglú | https://gestion.pe/economia/empresas/avla-lanza-insurtech-para-asegurar-viviendas-noticia/ |
| G-27 | 2 | Betterfly llega al Perú: la estrategia y los planes de la insurtech | Caso de entrada y salida; **busca también la nota de su salida** (no tengo su enlace) | https://gestion.pe/economia/empresas/los-planes-de-la-insurtech-betterfly-en-el-peru-noticia/ |
| G-28 | 3 | Insurance Day 2025 (publirreportaje) | Tendencias declaradas por el sector | https://gestion.pe/publirreportaje/insurance-day-2025-historias-reales-que-estan-transformando-el-sector-asegurador-noticia/ |
| G-29 | 2 | La ambición de Yape que puede desbloquear a estas empresas clave | Estrategia de Yape | https://gestion.pe/tu-dinero/la-ambicion-de-yape-que-puede-desbloquear-a-estas-empresas-clave-noticia/ |
| G-30 | 2 | Dos millones de trabajadores podrán recibir sueldo en billeteras sin Yape | Ley de pago de sueldos en billeteras | https://gestion.pe/tu-dinero/dos-millones-de-trabajadores-podran-recibir-sueldo-en-billeteras-sin-yape-que-opciones-tienen-noticia/ |
| G-31 | 2 | Pacífico Seguros comunica exposición de base de datos de SOAT | Incidente de seguridad (0,5% de clientes) | https://gestion.pe/tu-dinero/pacifico-seguros-comunica-exposicion-de-base-de-datos-de-soat-noticia/ |
| G-32 | 2 | Pacífico Seguros: "Queremos llegar a millones de personas más con los seguros inclusivos" | Estrategia de seguros inclusivos | https://especial.gestion.pe/comunidadesg/2024/04/19/pacifico-seguros-queremos-llegar-a-millones-de-personas-mas-con-los-seguros-inclusivos-y-ser-un-pais-mas-resiliente/ |

### D. Open banking, finanzas abiertas, pagos y BaaS

| ID | Pri. | Titular | Qué resuelve | URL |
|---|---|---|---|---|
| G-33 | 1 | Finanzas abiertas: SBS publica proyecto con primer bloque de normas | Alcance, fechas y si incluye seguros | https://gestion.pe/economia/empresas/finanzas-abiertas-sbs-publica-proyecto-con-primer-bloque-de-normas-noticia/ |
| G-34 | 1 | Open banking: BCRP próximo a dar luz verde a "iniciadores de pagos" | Fecha del reglamento y de TAPP | https://gestion.pe/tu-dinero/open-banking-bcrp-proximo-a-dar-luz-verde-a-iniciadores-de-pagos-sepultaran-a-tarjetas-de-credito-noticia/ |
| G-35 | 1 | Pagos en segundos y menores precios: la revolución de iniciación de pagos que busca el BCRP | Cómo funcionaría el pago iniciado | https://gestion.pe/tu-dinero/pagos-en-segundos-y-menores-precios-la-revolucion-de-iniciacion-de-pagos-que-busca-el-bcrp-noticia/ |
| G-36 | 1 | Open finance: SBS conforma departamento para implementarlo | Hoja de ruta | https://gestion.pe/tu-dinero/open-finance-sbs-conforma-departamento-para-implementarlo-cual-sera-su-primera-tarea-noticia/ |
| G-37 | 2 | SBS adelanta lineamientos para sistema de finanzas abiertas en Perú | Lineamientos previos | https://gestion.pe/tu-dinero/sbs-adelanta-lineamientos-para-sistema-de-finanzas-abiertas-en-peru-noticia/ |
| G-38 | 2 | Datos de su cuenta de ahorro podrán ser compartidos por su banco: ¿a quiénes? | Consentimiento y terceros | https://gestion.pe/tu-dinero/datos-de-su-cuenta-de-ahorro-podran-ser-compartidos-por-su-banco-a-quienes-noticia/ |
| G-39 | 2 | Perú alista open banking pero en camino tortuoso: los fracasos más sonados | Riesgos y casos fallidos | https://gestion.pe/tu-dinero/peru-alista-open-banking-pero-en-camino-tortuoso-los-fracasos-mas-sonados-noticia/ |
| G-40 | 3 | Open Finance: el cambio que viene para el sistema financiero peruano (opinión) | Opinión | https://gestion.pe/opinion/open-finance-el-cambio-que-viene-para-el-sistema-financiero-peruano-noticia/ |
| G-41 | 3 | María y el celular: el potencial de las finanzas abiertas para la inclusión (opinión) | Inclusión | https://gestion.pe/opinion/maria-y-el-celular-el-potencial-de-las-finanzas-abiertas-para-la-inclusion-noticia/ |
| G-42 | 1 | SBS reglamenta el modelo Banking as a Service, ¿qué viene para el sistema financiero? | Fecha de vigencia y responsabilidad | https://gestion.pe/tu-dinero/sbs-reglamenta-el-modelo-banking-as-a-service-que-viene-para-el-sistema-financiero-noticia/ |
| G-43 | 2 | Personas podrán contratar productos bancarios en bigtech, telcos y fintech, ¿cobrarán? | Qué se podría vender en apps ajenas | https://gestion.pe/tu-dinero/personas-podran-contratar-productos-bancarios-en-bigtech-telcos-y-fintech-cobraran-noticia/ |
| G-44 | 3 | ¿Compras y créditos directos desde una app? Los rubros que se beneficiarán con el BaaS | Rubros | https://gestion.pe/tu-dinero/compras-y-creditos-directos-desde-una-app-los-rubros-que-se-beneficiaran-con-el-baas-en-peru-noticia/ |

### E. Regulación de la venta digital de seguros y de la IA

| ID | Pri. | Titular | Qué resuelve | URL |
|---|---|---|---|---|
| G-45 | 1 | SBS plantea cambios de ciberseguridad en venta digital de seguros | Biometría y régimen simplificado; si se aprobó | https://gestion.pe/tu-dinero/finanzas-personales/sbs-plantea-cambios-de-ciberseguridad-en-la-venta-digital-de-seguros-que-propone-noticia/ |
| G-46 | 1 | Perú ya tiene reglamento de IA: ¿tu empresa opera bajo riesgos "altos" o "indebidos"? | Decreto Supremo 115-2025-PCM y salud como riesgo alto | https://gestion.pe/economia/peru-ya-tiene-reglamento-de-ia-tu-empresa-opera-bajo-riesgos-altos-o-indebidos-noticia/ |
| G-47 | 2 | Tras la Ley de IA, el país mira al sector financiero: ¿qué falta para una Ley Fintech? | Vacíos para seguros | https://gestion.pe/economia/tras-la-ley-de-ia-el-pais-mira-al-sector-financiero-que-falta-para-una-ley-fintech-noticia/ |
| G-48 | 2 | SBS permitirá comercializar más seguros de forma online | Qué seguros se pueden vender en línea | https://gestion.pe/economia/sbs-permitira-comercializar-mas-seguros-de-forma-online-noticia/ |
| G-49 | 2 | SBS cambia reglamentación para facilitar venta no presencial de seguros | Reglas de venta a distancia | https://gestion.pe/economia/sbs-cambia-reglamentacion-para-facilitar-venta-no-presencial-de-seguros-noticia/ |
| G-50 | 2 | SBS alista plan para seguros baratos y ágiles, ¿qué peligros acechan a peruanos? | Régimen simplificado y riesgos | https://gestion.pe/tu-dinero/sbs-alista-plan-para-seguros-baratos-y-agiles-que-peligros-acechan-a-peruanos-noticia/ |
| G-51 | 2 | SBS reglamentó los seguros paramétricos | Resolución SBS 02260-2026 | https://gestion.pe/economia/empresas/sbs-reglamento-los-seguros-parametricos-como-funcionara-este-nuevo-tipo-de-cobertura-noticia/ |

### F. Vida, ahorro, inversión, rentas y Vida Ley

| ID | Pri. | Titular | Qué resuelve | URL |
|---|---|---|---|---|
| G-52 | 1 | Seguros de vida inversión crecen 64%, ¿por qué toman plazos m…? (23-mar-2026) | Periodo y base del 64%. **No tengo el enlace**: búscala por el titular en https://gestion.pe/noticias/seguro-de-vida/ | https://gestion.pe/noticias/seguro-de-vida/ |
| G-53 | 1 | ¿Se acelerarán jubilaciones en AFP? Seguros de vida y rentas vitalicias crecerán muy rápido | Vida +18% a abril; efecto del retiro de AFP | https://gestion.pe/tu-dinero/se-aceleraran-jubilaciones-en-afp-seguros-de-vida-y-rentas-vitalicias-creceran-muy-rapido-noticia/ |
| G-54 | 1 | Seguros de vida (Interseguro): tres razones por las que apuesta por estas pólizas | 90% de primas en vida frente a 55% de la industria (declarado) | https://gestion.pe/economia/empresas/seguros-de-vida-interseguro-tres-razones-por-las-que-apuesta-por-estas-polizas-noticia/ |
| G-55 | 1 | Seguros: productos Vida Devolución y renta particular ya superan a los tradicionales | Peso de ahorro y devolución | https://gestion.pe/g-de-gestion/seguros-productos-vida-devolucion-y-renta-particular-ya-superan-a-los-tradicionales-interseguro-mapfre-beneficios-intereses-tasas-g-de-gestion-noticia/ |
| G-56 | 1 | Seguros por partida doble: la devolución puede llegar al 200% de las primas pagadas | Costos y penalidades de rescate | https://gestion.pe/economia/mercados/seguros-por-partida-doble-la-devolucion-puede-llegar-al-200-de-las-primas-pagadas-seguros-de-vida-seguros-con-devolucion-aseguradoras-rimac-pacifico-la-positiva-g-de-gestion-noticia/ |
| G-57 | 2 | Retiro del 95% de AFP: ¿efectivo o pensión de por vida? | Decisión renta frente a efectivo | https://gestion.pe/tu-dinero/retiro-del-95-de-afp-llego-el-dia-de-decidir-llevarse-en-efectivo-o-pension-de-por-vida-noticia/ |
| G-58 | 2 | Seguros de vida: tres de cada cuatro familias que perdieron a alguien no tenía una póliza (APESEG) | Brecha de protección de vida | https://gestion.pe/tu-dinero/seguros-de-vida-tres-de-cada-cuatro-familias-que-perdieron-a-alguien-no-tenia-una-poliza-apeseg-aseguradoras-noticia/ |
| G-59 | 2 | Se duplican seguros de vida que otorgan renta mensual | Rentas privadas | https://gestion.pe/tu-dinero/se-duplican-seguros-de-vida-que-otorgan-renta-mensual-noticia/ |
| G-60 | 2 | Seguros de vida para trabajadores: obligatorio desde qué momento | Vida Ley | https://gestion.pe/tu-dinero/finanzas-personales/seguros-de-vida-para-trabajadores-obligatorio-desde-que-momento-noticia/ |

### G. SOAT y vehicular

| ID | Pri. | Titular | Qué resuelve | URL |
|---|---|---|---|---|
| G-61 | 1 | SOAT: clave en un país de pistas peligrosas, ¿qué tanto ha bajado su costo en 24 años? | Cumplimiento de motos (20% a 30%), SOAT digital desde 2017 | https://gestion.pe/g-de-gestion/reportaje/soat-clave-en-un-pais-de-pistas-peligrosas-que-tanto-ha-bajado-su-costo-en-24-anos-noticia/ |
| G-62 | 2 | Sujetos venden a través de Facebook falsos SOAT a motociclistas | Fraude del canal | https://gestion.pe/peru/elcomercio-lima-sucesos-facebook-sujetos-venden-falsos-soat-motociclistas-evadir-controles-policia-nndc-275011-noticia/ |
| G-63 | 2 | SOAT: compara cuál es el seguro más conveniente con una herramienta de la SBS | Comparador | https://gestion.pe/mix/mi-bolsillo/soat-compara-cual-es-el-seguro-mas-conveniente-con-una-herramienta-de-la-sbs-seguro-obligatorio-de-accidentes-de-transito-noticia/ |

### H. Mercado general y microseguros

| ID | Pri. | Titular | Qué resuelve | URL |
|---|---|---|---|---|
| G-64 | 1 | Ganancias bajan en la mitad de las compañías de seguros: ¿cuánto gana la suya? | Primas del primer semestre de 2026 (+1,1%, S/ 9.451 millones) y utilidades; reconcilia el dato "a revisar" de penetración | https://gestion.pe/tu-dinero/ganancias-bajan-en-la-mitad-de-las-companias-de-seguros-cuanto-gana-la-suya-noticia/ |
| G-65 | 1 | Seguros en Perú: ¿en qué indemnizaron más a clientes y qué puede venir? | Primas del primer trimestre de 2026 (APESEG) | https://gestion.pe/tu-dinero/seguros-en-peru-en-que-indemnizaron-mas-a-clientes-y-que-puede-venir-noticia/ |
| G-66 | 2 | ¿Dólar culpable?: caen utilidades de empresas de seguros luego de 2 años | Resultados de 2025 | https://gestion.pe/tu-dinero/dolar-culpable-caen-utilidades-de-empresas-de-seguros-luego-de-2-anos-noticia/ |
| G-67 | 2 | SBS actualiza el reglamento de pólizas de microseguros | Tope de prima y canales | https://gestion.pe/tu-dinero/finanzas-personales/sbs-actualiza-el-reglamento-de-polizas-de-microseguros-seguros-noticia/ |
| G-68 | 2 | Inclusión financiera en los seguros: ¿cómo integrarla dentro de una estrategia ESG? | Asegurados en microseguros a diciembre de 2022 | https://especial.gestion.pe/comunidadesg/2023/05/19/inclusion-financiera-en-los-seguros-como-integrarla-dentro-de-una-estrategia-esg/ |

### Lo que pediría primero (14 notas)

G-01, G-02, G-03, G-05, G-11, G-12, G-15, G-33, G-34, G-42, G-52, G-53, G-64 y G-45. Con ellas se verifican la oferta de salud digital de Pacífico y Yape, el contexto de EsSalud, el seguro privado real, el calendario de finanzas abiertas y pagos, el crecimiento de vida con inversión y la cifra de primas de 2026.

### Qué no encontré en Gestión (y habría que buscar por otro lado)

- Nota sobre convenios entre cadenas de farmacias y aseguradoras.
- Cifras oficiales de la SBS de vida con ahorro e inversión por producto.
- Nota sobre la salida de Betterfly del Perú.
- Reglas de idoneidad de la SBS para vida con inversión.
