# Valor de la recurrencia digital en seguros: por qué mecanismos la actividad digital se vuelve valor de negocio

> Documento de investigación. Fuente persistente y versionada en el repositorio.
> Fecha de elaboración: 2026-10-28 · Última actualización: 2026-10-28 · Versión: v1.0
> Origen: `/trinidad` (empírica como ancla, negocio como segundo pilar, social acotada al momento crítico).
> Pregunta: ¿por qué mecanismos la actividad digital (recurrencia en app o web) se convierte en valor de
> negocio en un seguro, quién lo ha demostrado y con qué evidencia?
> Contexto de uso: pregunta 1 del brief "Benchmarking: el valor de la recurrencia digital en seguros",
> insumo para la Gerencia de Digital de RIMAC. RIMAC está excluida como caso, fuente o benchmark.
> Alcance: seguros primero (Perú y LatAm); análogos de banca, salud y retail; EE.UU., Europa y Asia solo
> como contraste, marcados (🌐). Periodo 2021-2026; los estudios canónicos anteriores van marcados (📚).
> Fuentes registradas en `research/fuentes/codice.md`: F-847 a F-885, más F-25, F-180, F-183, F-186,
> F-353, F-376, F-442, F-638 y F-816 ya existentes.

---

## 0. Resumen ejecutivo

**La actividad digital crea valor cuando resuelve algo, no cuando genera visitas.** Las tres pistas
convergen en eso. Ninguna fuente encontrada muestra que la frecuencia de uso, por sí sola, produzca valor
en un seguro.

- **Costo de servir.** Es el mecanismo con mejor evidencia causal, y es de una aseguradora de salud. Un
  portal web bajó 29% las llamadas sobre información clara y fácil de encontrar. Subió las llamadas sobre
  información ambigua (pólizas, reclamos). En total, las llamadas subieron 14% (F-850). Digitalizar lo
  ambiguo puede costar más, no menos.
- **Retención.** En banca y planes de salud, quienes usan el canal digital se quedan más, incluso
  controlando la autoselección (F-847, F-851). En seguros no se encontró ningún estudio causal. Las cifras
  de las aseguradoras (Vitality, AIA, Oscar) son autorreportadas y no separan selección de efecto.
- **Venta cruzada.** Los usuarios digitales tienen más productos (F-848, F-849, F-862), pero es
  asociación. En LatAm, la "puerta de entrada" que vende seguros a escala es una app de alta frecuencia
  ajena: un banco digital o una billetera (F-863, F-864, F-869). No se encontró evidencia de que un
  producto propio de bajo ticket funcione como puerta.
- **Prevención.** Hay un experimento sólido de telemetría vehicular que cambia la forma de manejar
  (F-442). En salud, dos ensayos aleatorizados de programas de bienestar no encontraron efecto en el gasto
  médico (F-854, F-855). Los programas atraen a quien ya está sano. Su valor puede ser **selección de
  riesgo**, no prevención.
- **Confianza en el momento de verdad.** La calidad de la experiencia digital del siniestro se asocia
  fuertemente a la fuga (F-872). Pero entre los factores de satisfacción con el siniestro, la confianza
  pesa más y el canal digital pesa menos (F-874). La gente quiere una persona en lo complejo (F-183,
  F-882).

**Implicancia para la meta:** el MAU mide entrar, no resolver. Según el mecanismo que se elija, el
indicador correcto es otro, y en dos de los cinco casos un buen resultado **baja** la actividad.

---

## 1. Punto de partida: el seguro es un producto de baja frecuencia

El cliente típico interactúa con su aseguradora 1 o 2 veces al año; en banca, entre 10 y 20 veces más
(McKinsey, 2023, vía cita secundaria, F-876). Por eso la recurrencia no puede salir del seguro mismo.
Sale de servicios adyacentes (salud, asistencias, beneficios) o de plataformas ajenas de alta frecuencia.
Este dato encuadra todo lo que sigue.

---

## 2. 🔬 Pista empírica y teórica (ancla)

**Veredicto:** la evidencia causal existe para costo de servir (mixta) y para retención en industrias
análogas. No existe para retención en seguros. En prevención, la mejor evidencia es negativa.

### 2.1 Costo de servir

- 📚 **Aseguradora de salud, EE.UU.:** cuasi-experimento con diferencias en diferencias. Usar el portal
  subió 14% las llamadas. Bajaron 29% las de información clara y fácil de encontrar. Subieron las de
  información ambigua (Kumar y Telang, 2012, F-850).
- 📚 **Banco grande, EE.UU.:** quienes adoptan la banca online hacen más transacciones en total y usan
  *más* la sucursal y el call center. En el corto plazo, el cliente es menos rentable (Campbell y Frei,
  2010, F-847).
- **Banco cooperativo, Alemania:** con grupo de control emparejado, quienes adoptan la banca móvil
  reducen el uso del call center y de la sucursal (Becker et al., 2022, F-849).

**Lectura:** la sustitución de canal depende del tipo de tarea. Lo consultivo y claro migra. Lo ambiguo
o urgente genera contactos nuevos. Digitalizar no ahorra si la pantalla produce dudas que terminan en el
teléfono.

### 2.2 Retención y persistencia

- 📚 **Banca:** la adopción online se asocia a más retención a 1-3 años, aun controlando la autoselección
  (F-847).
- 📚 **Plan de salud (Kaiser Permanente):** con emparejamiento por propensión, quienes usaron el portal
  retuvieron 96,9% y quienes no, 90,5%. Es observacional, y el estudio es de la propia organización
  (Turley et al., 2012, F-851).
- **Seguros:** no se encontró ningún diseño causal. Lo que hay son encuestas transversales de intención
  (F-856, India) y cifras de empresa sin método (F-860, F-861).
- **Contraevidencia de selección:** en un ensayo aleatorizado, quienes se inscriben en programas de
  bienestar ya tenían menor gasto y mejores hábitos antes de empezar (Jones, Molitor y Reif, 2019, F-854).
  La misma lógica amenaza la tesis "el cliente digital es más fiel": quien adopta ya es distinto.
- 📚 **Hallazgo contraintuitivo en seguros:** la primera cancelación predice la fuga total del hogar. Los
  clientes con 3 o más pólizas fueron *más* propensos a irse por completo tras cancelar una (Brockett et
  al., 2008, F-852). Tener más productos no blinda por sí solo.

### 2.3 Venta cruzada

- 📚 Los adoptantes de banca online amplían su actividad y tienen más productos (Xue, Hitt y Chen, 2011,
  F-848). Los adoptantes de banca móvil compran más productos promovidos (F-849).
- En seguros no-vida, el número de contratos y el canal de acceso inicial influyen en cuánto tarda la
  segunda compra (F-853, Suiza, observacional).
- No se encontró evidencia académica de un producto obligatorio o de bajo ticket como puerta de entrada.

### 2.4 Siniestralidad y prevención

- **Auto (🟢 causal):** un experimento de campo nacional con seguro por uso simulado redujo la velocidad
  y las frenadas y aceleraciones bruscas (F-442). Mide conducta, no siniestros.
- 📚 **Salud (🟢 causal, negativo):** dos ensayos aleatorizados de bienestar laboral no encontraron
  efecto en gasto médico, salud clínica ni ausentismo (F-854, F-855).
- **Vitality:** reporta 4% menos siniestros con revisión actuarial declarada (F-353) y grandes caídas de
  mortalidad que no descartan autoselección (F-638).

**Lectura:** el valor del engagement en salud puede venir de atraer y retener a quien ya es buen riesgo.
Es un valor legítimo, pero es **selección**, no prevención, y se mide distinto.

### 2.5 Confianza en el momento de verdad

La pista académica no aportó estudios nuevos aquí. La evidencia es de negocio (§4) y social (§3).

### Tabla de rigor (pista empírica)

| Fuente | Rigor | Diseño | Industria | Período |
|---|---|---|---|---|
| F-850 Kumar y Telang | 🟢 A | Cuasi-experimento, dif-en-dif | Seguro de salud | 📚 2012 |
| F-847 Campbell y Frei | 🟢 A | Panel con control de selección | Banca | 📚 2010 |
| F-849 Becker et al. | 🟢 A | Dif-en-dif emparejado | Banca | 2022 |
| F-848 Xue, Hitt y Chen | 🟢 A | Panel | Banca | 📚 2011 |
| F-851 Turley et al. | 🟢 A (observacional) | Cohorte con propensión | Plan de salud | 📚 2012 |
| F-852 Brockett et al. | 🟢 A | Supervivencia | Seguros | 📚 2008 |
| F-853 Risks 2022 | 🟢 A | Supervivencia | Seguros | 2022 |
| F-854 Jones et al. | 🟢 A | Ensayo aleatorizado | Salud laboral | 📚 2019 |
| F-855 Song y Baicker | 🟢 A | Ensayo por conglomerados | Salud laboral | 📚 2019 |
| F-442 Seguro por uso | 🟢 A | Ensayo de campo | Auto | 2025-26 |
| F-856 Singh et al. | 🟡 C | Encuesta transversal | Seguro de vida | 2024 |

Todas las fuentes se leyeron por resumen; el texto completo no se consultó en esta sesión.

---

## 3. 📱 Pista social (acotada al momento crítico)

**Nivel de instalación:** 🌡️ tibio. Hay patrones claros pero poca conversación específica sobre apps de
seguros, y casi nada de Perú.

- **La gente quiere una persona en lo complejo.** Comentarios en Reddit: nadie imagina resolver un
  siniestro caro sin hablar con alguien; los bots resuelven lo simple y fallan en lo complejo (F-882,
  rigor E).
- 🌐 **La IA en el siniestro dispara desconfianza.** En 2021, Lemonade dijo que su IA leía "señales no
  verbales" en videos de reclamos. La reacción la acusó de discriminación y tuvo que retractarse (F-881).
- 🌐 **El cliente también se arma con IA.** Herramientas de IA para apelar rechazos se viralizaron en
  2024-2025 (F-885). Es una señal de que el siniestro puede volverse una disputa entre IAs.
- 🌐 **El chat que no ayuda termina en queja formal** (caso del defensor financiero británico, F-884).
- **Perú:** la fricción registrada está en la **resolución**, no en el canal. Indecopi recibió 8.248
  reclamos de seguros entre 2019 y 2022, y en 2025 sancionó demoras en indemnizaciones de SOAT y
  liquidaciones que no respetaban la póliza (F-883). No se encontró conversación social sobre apps de
  aseguradoras peruanas.

**Validación vs. amplificación:** el caso Lemonade tuvo cobertura convergente de prensa. Lo de Reddit
es anecdótico y llega por un blog de proveedor. Sirve como señal, no como medida.

---

## 4. 📈 Pista de negocio (segundo pilar)

**Veredicto:** abundan las cifras de asociación publicadas por las propias empresas. Hay pocas
auditadas. Ninguna separa el efecto del canal del tipo de cliente que lo usa.

### Perú

| Actor | Qué publica | Rigor | Aporta a |
|---|---|---|---|
| Pacífico Seguros | Más de 60% de consultas resueltas por autoservicio (chatbot y app); NPS +~50% en 3 años (2022) | 🟠 D (F-866) | Costo de servir |
| Interseguro | Venta digital de SOAT +66% y mejor renovación (2019, sin cifra de renovación); 580 mil clientes en canal digital (2022) | 🟡 C (F-867) | Venta, retención (débil) |
| La Positiva | Declara una plataforma digital en construcción; sin resultados | 🟠 D (F-868) | No aporta evidencia |
| Mapfre Perú | Nada verificable sobre resultados digitales | — | No aporta evidencia |
| Yape (análogo, billetera) | 15,9 M de usuarios activos mensuales; vende SOAT; seguro de salud con meta de 30 mil afiliados | 🟠 D (F-869) | Puerta de entrada ajena |

### LatAm

| Actor | Qué publica | Rigor | Aporta a |
|---|---|---|---|
| Porto Seguro (Brasil) | Meta: 84% de la venta digital es venta cruzada a clientes existentes; 71% de interacciones digitales; los corredores siguen siendo el motor | 🟡 C (F-865) | Venta cruzada, costo de servir |
| Nubank + Chubb (Brasil) | 2 M de pólizas; penetración de 1,6% de su base en 2023 | 🟠 D (F-863) | Puerta ajena: escala con baja conversión |
| Mercado Pago | 11 M de clientes con pólizas; venta por su propio corredor y asistente de IA | 🟠 D (F-864) | Puerta ajena, señal de IA |
| Justos (Brasil) | Siniestralidad −6 pp/año con telemetría y precio; 2% no renovados por mala nota | 🟠 D (F-870) | Prevención y selección |
| BBVA México (bancaseguros) | 76% de ventas digitales en unidades (2022), sin desglose de seguros | 🔵 B (F-879) | Contexto bancaseguros |
| Ecosistema insurtech | US$199 M de inversión en 2025; mortalidad de startups bajó de 13% a 8% | 🟡 C (F-878) | Señales |

### Contraste (🌐 no generalizar a Perú)

| Actor | Qué publica | Rigor | Aporta a |
|---|---|---|---|
| Lemonade | Retención en dólares de 85%: ser nativo digital no garantiza retención alta; más de 5% multiproducto aporta ~1/5 de la prima | 🔵 B (F-857) | Retención, venta cruzada |
| Vitality (Discovery, Reino Unido) | 39% a 67% menos caídas en miembros comprometidos, sin método de comparación | 🟠 D (F-860) | Retención (selección) |
| AIA | "Mejoras significativas" de persistencia, sin cifra | 🟠 D (F-861) | Retención |
| Ping An | 2,92 contratos por cliente; usuarios de salud con 1,6 veces más contratos (prensa) | 🔵 B / 🟠 D (F-862) | Venta cruzada (asociación) |
| Oscar Health | Atribuye retención a la plataforma y la IA, sin publicar tasa; pérdida de ~US$443 M en 2025 | 🟡 C (F-858) | Retención (sin dato) |
| Alan | Usuarios activos diarios ×2,3 con gamificación; usan 3 veces más los servicios; retención aún no medida | 🟠 D (F-859) | Prevención, recurrencia |
| Root | Ratio combinado 98,2% por precio y selección; la retención sigue siendo una incertidumbre declarada | 🔵 B (F-871) | Prevención y selección |
| J.D. Power (siniestros digitales) | Experiencia digital de siniestro mala: 52% en riesgo de fuga; excelente: 4% | 🟡 C (F-872) | Confianza |
| J.D. Power (siniestros auto) | Confianza es el factor 1 de 8; el canal digital, el 8 | 🟡 C (F-874) | Confianza |
| J.D. Power (salud digital) | Tras una mala experiencia, solo 27% vuelve a usar ese canal | 🟡 C (F-873) | Retención, confianza |
| Amica | Lidera la satisfacción sin ser digital primero | 🟡 C (F-880) | Contraste: lealtad por servicio |
| Proveedores de software | Dicen que se ahorra entre 30% y 40% del costo de servir. Registrado solo para advertir | 🔴 E (F-877) | No usar |

**Referentes sugeridos que no aportaron evidencia en esta pasada:** Mapfre Perú, La Positiva (solo
intención), Coalition, Zurich, AXA, Allianz y Allianz Direct, ZhongAn, Progressive y USAA. No se
forzaron. **Concesionarios con seguro vinculado:** solo apareció un caso de proveedor (Toyota Insurance
vía AWS, F-877, rigor E). No hay evidencia útil.

---

## 5. ⚖️ Síntesis: menú de teorías de valor

| Mecanismo | Indicador en vez del MAU | Mejor evidencia | Nivel | Qué implica |
|---|---|---|---|---|
| **Costo de servir** | Contactos por necesidad resuelta; resolución sin escalar a humano, por tipo de tarea | Aseguradora de salud: −29% de llamadas en lo claro, más llamadas en lo ambiguo (F-850) | 🟢 Causal, dirección mixta | Migrar primero lo claro. En lo ambiguo, rediseñar el contenido antes de digitalizar, o aceptar el teléfono |
| **Retención** | Renovación o persistencia en cohortes emparejadas | Banca y plan de salud: sí, con control de selección (F-847, F-851). Seguros: sin evidencia causal | 🔵 Plausible por analogía; ⚪ no demostrado en seguros | La tesis "el digital es más fiel" exige un diseño interno (cohortes emparejadas o despliegue escalonado). El benchmarking no la puede probar |
| **Venta cruzada** | Productos por cliente; lead a póliza; prima nueva de clientes existentes | Banca: los adoptantes tienen más productos (F-848, F-849). Porto: la venta digital es casi toda a clientes existentes (F-865) | 🟡 Asociación | Lo digital sirve para vender al que ya está. La puerta de entrada a escala la tienen apps ajenas de alta frecuencia |
| **Siniestralidad y prevención** | Siniestralidad por cohorte emparejada; separar selección de efecto | Auto: telemetría cambia conducta (F-442). Salud: los ensayos de bienestar no reducen gasto (F-854, F-855) | 🟢 en auto (conducta); 🔴 en salud (gasto) | En salud, el valor probable es atraer buenos riesgos. Medirlo como selección |
| **Confianza en el momento de verdad** | Tiempo a resolución; tasa de escalamiento digital a humano; resuelto al primer intento | Una mala experiencia digital de siniestro se asocia a fuga (F-872); confianza > canal (F-874); lo 100% digital falla en reclamos complejos (F-183) | 🟡 Asociación consistente entre fuentes | Diseñar el siniestro como híbrido. El indicador es resolver, no usar el app |

**Dónde convergen las tres pistas:** lo que importa es resolver, no la frecuencia. Lo académico lo muestra
en costo de servir. Lo de negocio, en siniestros. Lo social, en el pedido de una persona para lo complejo.

**Dónde divergen:**

- Las empresas reportan grandes beneficios de retención por engagement (Vitality, AIA, Oscar, Alan). La
  evidencia rigurosa muestra que esa diferencia puede ser selección.
- Los proveedores prometen ahorros de 30% a 40% del costo de servir. El único estudio causal en una
  aseguradora encontró más llamadas en total.

No se resuelve esa tensión: se reporta.

**La tensión con el MAU:** dos mecanismos (costo de servir y confianza) bajan la actividad cuando
funcionan. Un cliente que resolvió rápido no vuelve a entrar. Si la meta es el MAU, puede premiar la
fricción.

---

## 6. Banco de señales para el ejercicio de foresight

Separado de las prácticas probadas. Las señales todavía no tienen resultados.

**Prácticas probadas (con evidencia A o B):**

1. Lo claro migra a digital y lo ambiguo genera llamadas (F-850).
2. En banca, la adopción digital se asocia a retención aun controlando la selección (F-847).
3. La retroalimentación telemática cambia la forma de manejar (F-442).
4. Los programas de bienestar seleccionan más de lo que transforman (F-854, F-855).

**Señales emergentes:**

- **Agentes de IA que venden y atienden dentro de apps ajenas.** El asistente de Mercado Pago ofrece
  seguros (F-864); Oscar opera con "IA agéntica" (F-858).
- **El seguro como función de una billetera o banco de alta frecuencia.** Yape vende SOAT y salud
  (F-869); Nubank (F-863). En Perú, la relación diaria con el cliente la puede tener un tercero.
- **Disputa de IA contra IA en el siniestro:** el cliente usa IA para apelar (F-885).
- **Telemetría para no renovar.** Justos no renueva al 2% con peor nota (F-870). Es selección explícita,
  con riesgo reputacional.
- **Indemnización instantánea en siniestros simples** (Porto, celular en 48 h, F-865).
- **Gamificación de salud como motor de uso diario** (Alan Play, F-859), con la advertencia de selección.
- **Inversión insurtech en LatAm que se recupera en 2025, con más disciplina y menos mortalidad** (F-878).

Eje candidato para escenarios: **quién es dueño de la relación diaria con el cliente.** Puede ser la
aseguradora, el banco o la billetera, el empleador o corredor, o una interfaz de IA. Es una hipótesis
para el ejercicio, no un hallazgo.

---

## 7. Implicancias para las hipótesis del brief

- **"El cliente digital es más fiel".** El benchmarking no la confirma para seguros. Las analogías
  sugieren que puede ser cierta, y la selección sugiere que puede ser falsa. Solo se resuelve con data
  propia en cohortes emparejadas.
- **"Hace falta una llave de entrada para cada cartera".** No se encontró evidencia de que un producto
  propio de bajo ticket abra la puerta. Las puertas que funcionan a escala en LatAm son apps ajenas de alta
  frecuencia.
- **"La actividad la determina el producto, no el canal" y "la gente casi no interactúa con la propuesta
  de valor".** Son consistentes con la baja frecuencia estructural del seguro (F-876) y con que la
  recurrencia de los referentes venga de servicios adyacentes (Alan, Ping An, Vitality).
- **"El siniestro debería resolverse en digital".** La evidencia apunta a un modelo híbrido:
  - digital para iniciar el siniestro y seguir su estado;
  - una persona para lo complejo;
  - el indicador es el tiempo a resolución.

---

## 8. Limitaciones

- **Sin evidencia causal de Perú ni de LatAm en ningún mecanismo.** Todo lo regional es autorreportado.
- **Varios estudios académicos son anteriores a 2021.** Son canónicos y van marcados (📚). Sus contextos
  son EE.UU. y Europa.
- **Todo se leyó por resumen o resultado de búsqueda.** Los dominios `arxiv.org`, `pacifico.com.pe` y
  `quartr.com` no fueron accesibles desde la sesión. La Memoria Integrada 2025 de Pacífico queda
  pendiente.
- **La pista social es la más débil.** Sobre apps de aseguradoras peruanas no se encontró conversación.
- **Varias cifras de Porto Seguro son metas, no resultados.**
- **Las de Ping An que comparan usuarios con no usuarios vienen de prensa, no del filing.**

---

## Conexiones

- [[futuro-asesores-seguros-venta-digital|¿Desaparecerán los asesores de seguros?]] — la misma regla de
  complejidad: lo simple migra a digital y lo complejo pide persona. Aquí se extiende del canal de venta al
  servicio y al siniestro.
- [[venta-vida-digital-hibrida-latam|Venta de seguros de vida en LATAM]] — confirma que el digital puro
  directo no gana en LatAm. Este node agrega que la puerta digital a escala la tienen bancos digitales y
  billeteras (Nubank, Mercado Pago, Yape).
- [[mecanismos-seguros-salud|Mecanismos de seguros de salud]] — Vitality y la selección de riesgo. Aquí
  se suman dos ensayos aleatorizados que muestran que los programas de bienestar seleccionan más de lo que
  transforman.
- [[lealtad-gamificacion-recompensas-retail|Gamificación, recompensas y lealtad en retail]] — análogo de
  retail para la recurrencia; la membresía de pago (F-816) es el caso con efecto persistente.
- [[behavioral-design-estado-disciplina|Behavioral design: estado de la disciplina]] — la telemetría
  vehicular (F-442) como diseño conductual embebido en el producto.
- [[seguros-comportamiento-mundo-peru|Comportamiento y mercado de seguros, Mundo vs. Perú]] — la
  desconfianza y la baja frecuencia de interacción que encuadran por qué la recurrencia no sale del seguro
  mismo.
