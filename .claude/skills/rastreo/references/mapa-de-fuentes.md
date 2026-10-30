# Mapa de fuentes: dónde vive cada tipo de evidencia

*Referencia de `/rastreo`, paso 3. Para cada tipo de afirmación: dónde buscar primero, qué rigor suele tener (rúbrica A-E
de `cronista`), qué registro lo ejecuta y la ruta alternativa si la primera falla. Se amplía cuando una búsqueda real
encuentra una fuente mejor.*

## 1. Efecto causal: "¿X produce Y?"

| Dónde | Rigor típico | Notas |
|---|---|---|
| Metaanálisis y revisiones sistemáticas (Cochrane Library para salud; búsqueda "meta-analysis" + término en Google Scholar o Semantic Scholar) | A | Empezar aquí: dan el panorama y los moderadores |
| Ensayos aleatorizados y experimentos de campo (PubMed, revistas de marketing y economía, AEA RCT Registry) | A | Buscar si están preregistrados |
| Documentos de trabajo (NBER, SSRN, IZA) | A-, sin revisión por pares | Declarar que no son arbitrados |
| Réplicas y reportes registrados (OSF, Many Labs, Retraction Watch) | A | Imprescindible para efectos psicológicos |
| Literatura latinoamericana (SciELO, Redalyc) y tesis peruanas (repositorio ALICIA de CONCYTEC) | A a C | Ruta para la evidencia local; las tesis no suelen estar arbitradas |

**Registro:** `seeker`. **Consulta adversarial típica:** "<efecto> replication", "<efecto> null result", "<intervención>
no effect". **Si falla la lectura del texto completo:** buscar el preprint o la versión del autor; si no aparece, marcar
"leído solo por resumen".

## 2. Cifra o tamaño: "¿cuántos, cuánto?"

| Dónde | Rigor típico | Notas |
|---|---|---|
| INEI (ENAHO, ENDES, censos, PBI por departamento), datosabiertos.gob.pe | B | Fuente primaria del Perú; microdato disponible |
| BCRP (BCRPData, síntesis de actividad económica por región) | B | Series de tiempo regionales |
| Reguladores: SBS, SMV, SUSALUD, SUNAT, Produce | B | Estadísticas sectoriales y de empresas |
| Gremios: APESEG, APEIM (niveles socioeconómicos), cámaras de comercio | B a C | Método propio, a veces parcial |
| Consultoras e institutos de mercado: Ipsos Perú, Arellano, CPI, Kantar, Nielsen, Euromonitor | C | A menudo de pago; la prensa cita sus titulares |
| Multilaterales: Banco Mundial, BID, CEPAL, OCDE | B | Comparaciones entre países |

**Registro:** `contexto-peruano` para el Perú; `marketer` para tamaños de mercado. **Regla:** una cifra de prensa se
rastrea hasta el informe original antes de usarla. **Ruta alternativa:** si el informe es de pago, buscar la nota de
prensa del propio emisor (suele traer las cifras clave) y declararlo.

## 3. Tendencia: "¿está creciendo, cambiando?"

| Dónde | Rigor típico | Notas |
|---|---|---|
| Series oficiales (INEI, BCRP) | B | La mejor prueba de tendencia |
| Encuestas repetidas con la misma metodología (Ipsos, Kantar, Datum) | C | Comparar solo ediciones con el mismo método |
| Google Trends | D, solo como señal | Mide interés de búsqueda, no conducta |
| Reportes anuales del sector | C | Cuidado con el incentivo del emisor |

**Registro:** `marketer` o `contexto-peruano`. **Regla:** dos mediciones independientes o una serie; un pico no es
tendencia.

## 4. Benchmark de negocio: "¿cómo le va a esta empresa o a este modelo?"

| Dónde | Rigor típico | Notas |
|---|---|---|
| Filings y estados financieros auditados (SMV en el Perú, SEC, memorias anuales) | A-B | Lo único verificable de verdad |
| Hechos de importancia (SMV), notas de resultados trimestrales | B | |
| Prensa de negocios: Gestión, Semana Económica, El Comercio, Bloomberg Línea | D, con fuente citada | Vale por la fuente que cita |
| Bases de financiamiento: Crunchbase, LAVCA | C | Rondas y valuaciones, a menudo autorreportadas |
| Casos de escuelas de negocio (HBS, INCAE, Centrum, ESAN, Pacífico) | B-C | Útiles para el mecanismo; suelen ser favorables a la empresa |

**Registro:** `marketer`. **Consulta adversarial típica:** "<empresa> pérdidas", "<empresa> cierre", "<empresa>
despidos", "<empresa> Indecopi". **Regla:** un resultado autorreportado por el operador del modelo se marca como tal.

## 5. Percepción social: "¿qué dice la gente?"

| Dónde | Rigor típico | Notas |
|---|---|---|
| Reseñas de Google Maps de cada local | E, por volumen | Muy útil para retail y salud local; leer las de 1 y 5 estrellas |
| TikTok, Instagram, Facebook (páginas y grupos locales) | E | Donde está la conversación en el Perú, más que en X |
| Reddit (r/PERU, r/Lima) y foros | E | Tono más crítico; poco volumen en temas locales |
| Comentarios en medios | E | Sesgo hacia el enojo |
| Indecopi ("Mira a quién le compras", resoluciones de sanción) | B | Quejas y sanciones con registro oficial: lo más sólido de esta pista |

**Registro:** `gossiper`. **Regla:** contar validación (otros que confirman o desmienten), no solo volumen.
**Ruta alternativa:** si el buscador no devuelve redes, buscar reseñas y notas que las citen, y declarar que la pista
social quedó débil.

## 6. Norma: "¿qué está permitido, qué exige la ley?"

| Dónde | Rigor típico | Notas |
|---|---|---|
| Diario Oficial El Peruano (normas legales), SPIJ | B (texto primario) | Verificar que sea la versión vigente |
| Portales de reguladores en gob.pe (SUSALUD, SBS, Indecopi, Autoridad de Protección de Datos Personales) | B | Reglamentos, guías, resoluciones |
| Códigos de ética de colegios profesionales | B | Por ejemplo, el del Colegio Médico |
| Estudios de abogados, LP Derecho | D | Útiles para interpretar; no reemplazan el texto |

**Registro:** lectura directa. **Regla:** citar el artículo, no la nota que lo resume.

## 7. Validez de una medición: "¿esto mide lo que dice?"

| Dónde | Rigor típico | Notas |
|---|---|---|
| Estudios de validación del instrumento (búsqueda "<medida> validation", "<medida> reliability") | A | Para pruebas, escalas, biomarcadores, índices |
| Guías y posiciones de sociedades científicas | A-B | Por ejemplo, sociedades de cardiología para pruebas de riesgo |
| Críticas metodológicas publicadas | A | Buscar "<medida> criticism", "<medida> limitations" |

**Registro:** `seeker`. **Regla:** una medida comercial sin estudio de validación independiente se presenta como no
validada.

## Rutas generales cuando algo falla

- **La página no abre**: buscar el PDF directo, una versión archivada en web.archive.org, o la nota del propio emisor.
- **El dato está detrás de un muro de pago**: buscar el resumen ejecutivo gratuito o la nota de prensa del emisor, y
  declarar que no se leyó el informe completo.
- **No hay nada local**: usar la mejor evidencia de la región o del mundo, decir que no es local y anotarlo como
  hueco para la siguiente vuelta.
