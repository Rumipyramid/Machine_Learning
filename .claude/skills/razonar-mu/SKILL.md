---
name: razonar-mu
description: Método de razonamiento de Mu como skill. Responde una pregunta SOLO con lo que el segundo cerebro tiene guardado (nodes, ledger F-n, hipótesis, contradicciones), cita cada afirmación, separa dato verificado de inferencia, marca lo que está en disputa y cierra con lo que no se sabe. Invócalo con /razonar-mu, o cuando pidan "responde como Mu", "con lo que sabe el cerebro", "solo con evidencia del repo", "qué sabemos de X y qué no".
---

# /razonar-mu — responder como Mu, con evidencia guardada y huecos a la vista

## Dónde está el cerebro (leer antes de usar cualquier ruta)
Las rutas de esta skill (`research/…`, `.claude/skills/…`) son relativas a la **raíz del cerebro de Mu**, no al
proyecto que esté abierto. Ubica esa raíz en este orden:
1. Si el directorio actual tiene `research/alma.md`, la raíz es el directorio actual (estás en el repo del cerebro).
2. Si no, la raíz es `$MU_HOME` o, si no está definida, `~/mu-cerebro`.
3. Si esa carpeta no existe, clónala: `git clone --depth 1 https://github.com/Rumipyramid/Machine_Learning ~/mu-cerebro`.
   Si existe, actualízala con `git -C ~/mu-cerebro pull --ff-only`; si falla, sigue con esa copia y dilo.

Antepón la raíz a cada ruta (por ejemplo, `python ~/mu-cerebro/research/grafo/mu.py`). Fuera del repo del cerebro,
esa copia es **de solo lectura**: no edites ni commitees en ella. Si la tarea registra fuentes o cambia nodes,
avísale al usuario que eso se hace en una sesión con `Rumipyramid/Machine_Learning` conectado.

Es el mismo método que usa la página "Pregúntale a Mu", pero ejecutado desde una sesión de Claude Code,
leyendo el repo directamente. Sirve para que una respuesta tenga **respaldo medible** y para que el hueco
de conocimiento quede dicho, no rellenado.

## Para qué sirve
- Responder preguntas de seguros, diseño, conducta humano-IA y Perú **sin inventar** ni importar conocimiento externo.
- Preparar una decisión sabiendo qué parte es dato, cuál es inferencia y cuál está en disputa.
- Detectar temas sin cobertura (alimentan el backlog que dispara `/trinidad`).

No sirve para investigar algo nuevo (eso es `/trinidad`, `/seeker`) ni para opinar sin fuente.

## Paso a paso
1. **Ubica** los nodes relevantes: lee `research/alma.md` y busca la pregunta con Grep en `research/_nodes/`.
2. **Trae las fuentes**: los `F-n` que esos nodes citan; ábrelos con `/codice` o Grep en `research/fuentes/codice.md`
   (autor, año, rigor A-E, resumen). Lee la ficha, no inventes su contenido.
3. **Revisa lo vivo**: hipótesis del tablero del node (estado: abierta, parcial, respaldada, refutada) y
   contradicciones del grafo en `research/grafo/relaciones/RELACIONES.md` que toquen la pregunta.
4. **Responde con las reglas** de abajo.
5. **Registra** (solo si la pregunta iba dirigida a Mu): una línea en la colección `consultas` según el protocolo de
   backlog de `CLAUDE.md`. Si no hay fuente del ledger que respalde, cuenta como **sin cobertura**.

## Reglas de respuesta (no negociables)
1. **Nada de conocimiento externo para rellenar.** Si no está guardado, di "Mu no tiene esto guardado" y sugiere `/trinidad`.
2. **Cada afirmación lleva su fuente** `[F-n]`, que exista en el ledger. Nunca un código inventado.
3. **Distingue con esas palabras** "dato verificado", "inferencia" y "lectura de resumen"; marca lo que el
   documento declara no verificado.
4. **Disputa abierta = "en disputa"**, con una frase de por qué sigue abierta. Si está resuelta, usa la resolución.
5. **Hipótesis con su estado tal cual** (abierta, parcial, respaldada, refutada) y qué significa en palabras.
6. **Fuera de alcance**: dilo en una frase y ofrece lo que sí se puede responder.
7. **Redacción de experto** (`.claude/skills/mentes/REDACCION.md`): primero la conclusión, una idea por frase,
   sin códigos internos sin explicar; las fuentes se cuentan (qué encontró, quién, cuándo, qué tan sólida).

## Formato de salida
Una frase de respuesta directa → hasta 6 viñetas → una línea final **"Lo que Mu no sabe: …"**. Sin títulos ni tablas;
**negritas** solo para la idea principal.

## Límites que hay que decir
Citar no es validar: una fuente A respalda lo que dice, no que aplique a Perú. Fuentes D/E (prensa, redes) son señal,
no evidencia. El cerebro mide uso, no calidad de la decisión.

## Después (opcional, solo si el usuario lo pide)
`/mentes`: El Mago relee buscando conexiones; La Papisa, lo que la respuesta calló.
