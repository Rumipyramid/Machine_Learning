---
name: trinidad
description: Invocar simultáneamente los tres buscadores de espectro amplio del proyecto — `seeker` (empírico/teórico), `gossiper` (social/mediático) y `marketer` (negocio/benchmarks) — sobre un mismo tema, para obtener una investigación de 360° que cubra evidencia académica, percepción social y desempeño de negocio a la vez. Activar SIEMPRE que el usuario invoque /trinidad, o pida una investigación "completa", "desde todos los ángulos", "académica + social + de negocio" sobre un tema, empresa, producto, persona o afirmación. No reemplaza a los tres skills individuales — los orquesta en paralelo y consolida sus resultados en un solo reporte, registrando todas las fuentes en el ledger de `cronista`.
---

# Trinidad — Investigación de 360°

## Propósito

Correr los tres registros de búsqueda del proyecto sobre el **mismo tema, en paralelo**,
y consolidar sus resultados en un solo reporte sin que se contaminen entre sí: evidencia
empírica no se mezcla con rumor social, y un benchmark de negocio no se confunde con
teoría. `trinidad` no reemplaza a `seeker`, `gossiper` ni `marketer` — es la orquesta que
los hace tocar juntos cuando el usuario quiere ver un tema desde los tres ángulos a la vez.

## Cuándo activarse

Activar este skill cuando el usuario:

- Invoque `/trinidad`.
- Pida una investigación "completa", "de 360°", "desde todos los ángulos", "académica +
  social + de negocio" sobre un tema, empresa, producto, persona o afirmación.
- Quiera evaluar algo (una startup, un rumor corporativo, un producto viral) cubriendo a
  la vez: qué dice la evidencia (`seeker`), qué se dice en redes/prensa (`gossiper`), y
  cómo le va en negocio (`marketer`).

Si el usuario solo quiere una de las tres pistas, usa el skill individual correspondiente
en vez de `trinidad` — no fuerces las tres cuando solo una aplica.

## Metodología

### Paso 1: Tipologizar el tema una sola vez, para las tres pistas

Antes de lanzar ninguna búsqueda, identifica en una sola pasada qué aristas tiene el tema
para cada registro:

- ¿Hay una afirmación empírica o teórica de fondo? → pista `seeker`.
- ¿Hay circulación social/mediática (rumor, controversia, percepción pública)? → pista
  `gossiper`.
- ¿Hay una dimensión de negocio (empresa, producto, métrica comercial)? → pista
  `marketer`.

No todos los temas requieren las tres por igual. Si una pista claramente no aplica (p. ej.
un tema sin ninguna empresa involucrada, sin componente de negocio), dilo explícitamente
en el reporte final y omite esa pista en vez de forzarla con evidencia irrelevante.

### Paso 2: Lanzar las tres búsquedas en paralelo

Ejecuta las tres metodologías **simultáneamente, no en serie** (lanza las búsquedas en
paralelo cuando la herramienta lo permita, en vez de esperar a que termine una para
empezar la siguiente):

- **Pista empírica/teórica**: aplica la metodología completa de `seeker`
  (`.claude/skills/seeker/SKILL.md`) — tipologizar capas del claim, mapear registros
  empírico/teórico, buscar en paralelo, clasificar tipo de evidencia, evaluar validez y
  confiabilidad.
- **Pista social/mediática**: aplica la metodología completa de `gossiper`
  (`.claude/skills/gossiper/SKILL.md`) — mapear plataformas (X/Twitter, Reddit, TikTok,
  foros, comentarios de noticias), buscar cobertura y reacción, medir frecuencia y
  validación social.
- **Pista de negocio**: aplica la metodología completa de `marketer`
  (`.claude/skills/marketer/SKILL.md`) — mapear fuentes de negocio (filings, bases de
  venture, informes de mercado, prensa especializada), buscar métricas, clasificar tipo
  de evidencia, evaluar comparabilidad.

Cada pista conserva su **propio criterio de validez** — nunca promedies ni mezcles rigor
académico con validación social ni con evidencia de negocio: son ejes distintos que miden
cosas distintas.

### Paso 3: Consolidar sin contaminar

Al armar el reporte final, mantén las tres pistas **visualmente separadas**. Nunca uses
una fuente de una pista para respaldar la conclusión de otra: no uses volumen de tuits
como evidencia de validez académica; no uses un paper para inferir tracción social; no
uses una ronda de financiamiento como prueba de que un rumor es cierto.

Si las tres pistas **convergen** en una misma conclusión, dilo explícitamente — es una
señal fuerte. Si **divergen** (ej. evidencia empírica débil pero mucha tracción social, o
buen desempeño de negocio pero percepción social negativa), señala la tensión: no la
resuelvas artificialmente ni promedies las conclusiones.

### Paso 4: Reporte consolidado

Estructura recomendada:

1. **Resumen ejecutivo** (3-5 líneas): qué dice cada pista en una frase, y si convergen
   o divergen entre sí.
2. **🔬 Pista empírica/teórica** — formato de `seeker`: veredicto, lo documentado, lo
   teórico/interpretativo, tabla de rigurosidad si hay 3+ fuentes.
3. **📱 Pista social/mediática** — formato de `gossiper`: nivel de instalación social
   (🔥/🌡️/💬/🧊), tono dominante, validación vs. amplificación.
4. **📈 Pista de negocio** — formato de `marketer`: métricas encontradas, tipo de
   evidencia, vigencia y comparabilidad.
5. **⚖️ Síntesis**: dónde convergen las tres pistas, dónde divergen, y qué implica eso
   para la pregunta original del usuario.
6. **Limitaciones**: qué pista quedó más débil por falta de fuentes, qué no se pudo
   verificar en ninguna de las tres.

Si una pista se omitió por no aplicar (Paso 1), decláralo en el resumen ejecutivo en vez
de dejar la sección vacía sin explicación.

### Paso 5: Registro consolidado en el cronista

Al terminar, registra en el ledger de `cronista` (`research/fuentes/registro_fuentes.md`)
todas las fuentes usadas en las tres pistas, con la misma rúbrica A-E de siempre:

- Deduplica contra el ledger existente antes de escribir (por URL o Autor+Año+Título).
- En el **Resumen breve** de cada fuente, indica de qué pista viene (empírica / social /
  negocio) para que quede trazable qué parte del reporte consolidado sustenta.
- Es normal que las tres pistas produzcan fuentes de rigor muy distinto en la misma
  investigación (un paper A junto a un hilo de Reddit E) — regístralas todas, cada una
  con su nivel real, sin forzar equivalencia.

## Anti-patrones a evitar

- **Correr las tres búsquedas en serie** cuando podrían ir en paralelo — pierde tiempo y
  no aporta rigor adicional.
- **Mezclar los criterios de validez** de las tres pistas en un solo puntaje o veredicto
  único ("esto tiene 7/10 de verdad" no significa nada si mezcla rigor + viralidad + ROI).
- **Omitir una pista sin decirlo**: el usuario debe saber explícitamente si faltó
  investigar la dimensión de negocio, por ejemplo, no asumir que no aplicaba.
- **Forzar una pista que no aplica** al tema — si no hay ninguna dimensión de negocio,
  no inventar una solo para completar las tres secciones.
- **Resolver divergencias artificialmente**: si las pistas están en tensión (buena
  evidencia empírica pero mala percepción social), reportar la tensión tal cual, no
  promediarla en una conclusión falsamente armoniosa.
