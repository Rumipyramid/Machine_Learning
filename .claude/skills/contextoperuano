---
name: contexto-peruano
description: Busca y sintetiza data pública peruana y regional (INEI, SBS, BCRP, APESEG, BID, Banco Mundial) para fundamentar contexto socioeconómico o benchmarking sectorial en cualquier proyecto. Úsalo siempre que se necesite fundamentar una afirmación sobre la realidad peruana (nivel educativo, acceso digital, penetración de seguros, comportamiento de consumo financiero, indicadores demográficos o macroeconómicos) con dato verificable, en vez de asumirla, generalizarla o citarla de memoria. Se activa también cuando el usuario menciona INEI, SBS, BCRP, APESEG, BID, o pide "dato oficial", "cifra verificada", "benchmarking del sector" o "contexto peruano".
---

# Contexto Peruano

Skill de investigación con fuentes fijas para fundamentar afirmaciones sobre la realidad socioeconómica y sectorial peruana con datos públicos verificables. No analiza data propia del usuario — busca y sintetiza data ya publicada por fuentes oficiales.

## Cuándo se activa

Cuando se necesita fundamentar una afirmación sobre la realidad peruana (nivel educativo, acceso digital, penetración de seguros, comportamiento de consumo financiero, indicadores demográficos o macroeconómicos) con dato verificable, en vez de asumirla o generalizarla.

## Paso 1 — Validación obligatoria antes de buscar

No se ejecuta ninguna búsqueda hasta confirmar estos 4 elementos. Si falta alguno (excepto año), preguntar antes de buscar — nunca asumir ni lanzar una búsqueda genérica con un pedido incompleto:

1. **Variable exacta** — no "acceso digital" sino "penetración de internet móvil" o "uso de WhatsApp Business en pymes". Si el pedido es ambiguo, preguntar cuál específicamente antes de buscar.
2. **Corte** — región, NSE, edad, urbano/rural. Si no se especifica, confirmar si se quiere el dato agregado nacional o preguntar el corte deseado.
3. **Año o rango** — si no se especifica, usar el más reciente disponible y declararlo explícito en la respuesta. Este es el único de los 4 con default razonable; no requiere pregunta.
4. **Propósito** — para qué se va a usar el dato (qué documento, qué sección, qué decisión). Si no se especifica, preguntar — determina qué tan preciso o genérico debe ser el dato y qué fuente priorizar.

Ejemplo de pedido bien formado: "Necesito penetración de smartphone en Lima Metropolitana, segmentado por NSE, dato más reciente disponible — es para fundamentar la sección de WhatsApp Business del playbook."

Ejemplo de pedido ambiguo que requiere preguntar antes de buscar: "Dame data de tecnología en Perú."

## Paso 2 — Fuentes priorizadas, en este orden

1. **INEI** (censos, ENAHO, encuestas especializadas) — prioridad para datos locales, regionales, por NSE.
2. **SBS** — indicadores del sistema financiero y de seguros.
3. **BCRP** — indicadores macroeconómicos.
4. **APESEG / gremios sectoriales** — benchmarking de seguros específicamente.
5. **BID** — estudios sectoriales y de comportamiento del consumidor en LatAm, útil especialmente para inclusión financiera y seguros.
6. **Banco Mundial (World Bank Open Data)** — series históricas o comparación entre países, cuando las fuentes anteriores no tienen el corte o la serie necesaria.
7. **Fuentes secundarias** — solo si ninguna de las anteriores tiene el dato, marcado explícito como tal.

No saltar directamente a fuentes secundarias o genéricas por comodidad de búsqueda: agotar las fuentes oficiales en orden antes de bajar en la lista.

## Paso 3 — Estándar de evidencia

- **Link directo** a la fuente oficial en cada dato.
- Si no hay link directo al dato puntual (tableros interactivos, PDFs sin URL fija), dar el link al reporte o tablero más específico posible.
- **Nombre exacto de la fuente/reporte** siempre incluido (ej. "INEI - Encuesta Nacional de Hogares (ENAHO) 2024, módulo de Educación"), para que el usuario pueda ubicarla manualmente si el link se rompe.
- **Año de publicación explícito** — la data de INEI/SBS puede tener 1-3 años de rezago respecto al momento de la consulta; esto debe decirse siempre, no darse por sobreentendido.
- Diferenciar claramente entre dato duro (medido) y estimación/proyección.

## Paso 4 — Nota de calibración por fuente

No toda cifra pesa igual aunque venga de fuente oficial. Junto a la cita, agregar una nota breve de calibración cuando sea relevante para que el usuario sepa qué tan sólido es el dato:

- **Registro administrativo** (SBS, censos INEI) — cobertura total o casi total, mayor solidez. Ej.: `(SBS, 2025 — registro administrativo, cobertura total del sistema)`.
- **Encuesta por muestreo** (ENAHO, encuestas especializadas de INEI) — sujeta a error muestral, puede ser poco confiable en cortes finos (regiones con N bajo). Ej.: `(INEI, ENAHO 2024 — encuesta por muestreo, N regional puede ser bajo fuera de Lima)`.
- **Reporte de gremio/industria** (APESEG y similares) — metodología no siempre transparente o auditable externamente. Ej.: `(APESEG, 2024 — reporte de gremio, verificar metodología si el dato es crítico para la decisión)`.
- **Estudio o serie de organismo multilateral** (BID, Banco Mundial) — generalmente sólido, pero puede usar definiciones distintas a las de fuentes peruanas (ej. "acceso financiero" definido distinto por BID vs. SBS); señalar si hay riesgo de comparar peras con manzanas.

No es necesario poner la nota en cada dato citado — usarla cuando el usuario vaya a tomar una decisión o afirmación fuerte con ese dato, no en menciones de paso.

## Paso 5 — Tabla resumen cuando hay múltiples fuentes

Si una respuesta cita 3 o más fuentes distintas, cerrar con una tabla corta:

| Fuente | Tipo | Año | Nota de confiabilidad |
|---|---|---|---|
| INEI, ENAHO | Encuesta por muestreo | 2024 | N bajo fuera de Lima |
| SBS | Registro administrativo | 2025 | Cobertura total |
| APESEG | Reporte de gremio | 2024 | Verificar metodología |

Esto le da al usuario una vista rápida de qué tan sólida es cada pieza de evidencia antes de usarla en un documento formal.

## Restricciones

- No generalizar con data de otro país si no se encuentra el dato específico de Perú. Declarar explícitamente que no está disponible y ofrecer el proxy más cercano (ej. dato regional LatAm del BID o Banco Mundial), marcado como tal.
- No acceder a contenido detrás de login o captcha.
- No inventar cifras aproximadas bajo ninguna circunstancia, ni siquiera como "estimación razonable".

## Output

Texto plano con: el dato, la fuente (nombre + link), el año, y una nota breve de cómo se conecta al proyecto o pregunta que lo originó. No es un reporte aislado — se integra al documento o diagnóstico que lo solicitó, sin encabezados ni estructura de informe formal salvo que el usuario lo pida.
