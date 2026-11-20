---
name: sintetizar
description: Sintetiza una transcripción (entrevista, reunión con cliente o sesión de trabajo) con rigor de investigación y deja el resultado en un documento PRIVADO, nunca en el repo. Invócalo con /sintetizar, o cuando el usuario suba, adjunte o pegue una transcripción y pida "sintetiza", "resume", "qué se dijo", "hallazgos de esta conversación".
---

# /sintetizar — transcripción → síntesis privada y rigurosa

La fuente es **solo la transcripción**. No agregues conocimiento externo ni del cerebro: contrastar con lo que ya
sabe el proyecto es un paso aparte (`/razonar-mu`) y solo si el usuario lo pide.

## Privacidad (regla fija)
El repo `Rumipyramid/Machine_Learning` es **público**. Nunca escribas en él la transcripción, su síntesis, cifras
internas ni nombres de personas. Tampoco la registres en el ledger (`research/fuentes/codice.md`), que es para
fuentes públicas. El destino es un documento privado de Claude Docs.

## Pasos
1. **Lee el archivo completo.** Si es `.docx`, extrae el texto con `python3 -I` y `zipfile` (lee `word/document.xml`),
   trabajando desde el scratchpad, no desde el repo. Avisa si el texto está cortado o trae errores de transcripción
   automática (cifras y nombres alterados).
2. **Pregunta solo lo que falte:** quién habla, fecha, tipo de sesión y para qué decisión sirve. Si ya se deduce, no preguntes.
3. **Escribe la síntesis** con esta estructura:
   - **Conclusión** en 3-4 frases.
   - **Cómo leer esta síntesis:** fuente, límites y qué es señal exploratoria.
   - **Lo dicho** (autorreporte, sin validar), agrupado por tema; usa tabla si son roles o atributos. Las cifras dudosas van "por confirmar".
   - **Inferencias:** tu lectura, rotulada como tal.
   - **Hipótesis a validar:** hipótesis, explicación alternativa y cómo validarla (método y con quién).
   - **Vacíos, contradicciones y pendientes**, incluido el material que la persona ofreció compartir.
4. **Guárdala** en un documento privado de Claude Docs (Artifact tipo Docs + conector) y entrega el link. Si la sesión
   no tiene el conector, dilo y deja la síntesis en el chat; no la guardes en ningún archivo del repo.
5. **Cierra** preguntando si quiere cruzarla con `/razonar-mu`. No lo hagas sola.

## Reglas de rigor
- Separa **dato observado, inferencia e hipótesis**; no presentes una inferencia como hallazgo.
- Distingue lo que la persona **dice** (actitudinal) de lo que **hace** (conductual) y señala sesgos de deseabilidad social y de encuadre.
- Una transcripción es señal exploratoria: no generalices. Marca qué voces faltan (corredor, cliente, usuario final, etc.).
- Separa la necesidad del usuario del deseo del negocio.
- No prejuzgues qué es fricción, causa o solución antes de la evidencia; ofrece explicaciones alternativas.
- No inventes cifras ni citas. Si citas, que sea textual de la transcripción.

## Redacción
Primero la conclusión, una idea por frase, frases cortas y autoexplicativas, sin códigos internos sin explicar
(`.claude/skills/mentes/REDACCION.md`). Escribe en español latinoamericano neutral.
