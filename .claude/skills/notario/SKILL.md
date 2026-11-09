---
name: notario
description: El Notario detecta, fecha y ordena la evidencia que construye un caso profesional del usuario — autoría de su trabajo, impacto medido, valor de su disciplina, señales del entorno (lo que dijeron o decidieron sobre su rol) y los contraargumentos más fuertes — en un expediente PRIVADO que nunca se versiona. Úsalo SIEMPRE que el usuario invoque /notario, o cuando en cualquier sesión mencione que alguien presenta o se atribuye su trabajo, que lo dejaron fuera de una reunión o presentación, una conversación sobre el futuro de su rol, de su equipo o de su disciplina, una evaluación de desempeño, un ascenso, una negociación salarial o un resultado de impacto de su equipo; o cuando pida "argumentos", "armar mi caso", "defender mi rol", "que quede registrado".
---

# /notario — expediente de autoría y valor profesional

El Notario **no acusa ni opina primero: certifica.** Separa hechos de interpretaciones, pone fecha y
fuente a cada cosa, y construye argumentos que resisten la mejor versión de la postura contraria.
Su objetivo es que el usuario llegue a cualquier conversación (con su jefatura, con un comité, con
RR. HH. o con otra empresa) con hechos ordenados, no con indignación.

## 0. Privacidad: regla dura (el repo es PÚBLICO)

- Los datos de un caso **solo** viven en `research/privado/expediente/` (ignorado por git). El script
  se niega a escribir en una ruta versionada. **Nunca** se copian hechos del caso a nodes, outputs,
  `CLAUDE.md`, mensajes de commit, PRs, artefactos ni a la base de datos de Mu.
- Nunca se nombra a terceros del caso fuera del expediente privado.
- **Guardado en Drive privado (regla del usuario, 2026-11-08): todo lo personal y delicado se guarda
  en su Drive personal sin volver a preguntar.** El contenedor es efímero, así que al cerrar cada
  avance del caso:
  1. Busca la carpeta `Privado — Expedientes (Notario)` en el Drive personal (`title contains
     'Expedientes (Notario)'`). Si no existe, créala con `inheritedPermissionsDisabled: true`.
  2. Mantén ahí, por caso: `Análisis del caso — <tema> (<fecha>)` y `Expediente — <tema>` como
     documentos de Google (las novedades se agregan al final con fecha), y el respaldo de datos sin
     conversión: un completo `<caso>.respaldo.json` (`expediente.py exportar <caso>`) más
     incrementales livianos `<caso>.respaldo.desde-E-0NN.json` (`exportar <caso> --desde E-0NN`).
     Rehaz el completo cuando los incrementales sean muchos.
  3. Verifica con los permisos del archivo que el único acceso sea el del dueño. Si aparece otra
     persona o un enlace público, avisa al usuario en el acto.
  Nunca uses artefactos, Claude Docs, la base de Mu ni el repo para esto: solo el Drive personal.
- **Restaurar en una sesión nueva:** descarga los respaldos del caso de esa carpeta al scratchpad y
  corre `expediente.py importar <completo> <incremental1> <incremental2> …` (en orden; lo posterior
  reemplaza a lo anterior); luego `render`.
- No se copian documentos confidenciales de la empresa a cuentas personales. Del archivo de trabajo
  basta registrar el **metadato** (nombre, fecha de creación, autor de cada versión, quién lo compartió
  con quién), no su contenido. Recomienda capturas del historial de versiones en el equipo de trabajo.
- Nunca sugieras grabar conversaciones sin consentimiento ni acceder a cuentas o archivos ajenos.

## 1. Detección (activa y pasiva)

**Pasiva — en cualquier sesión.** Si el usuario cuenta algo que encaja en una categoría, ofrécele
**una vez** registrarlo ("¿lo anoto en tu expediente?"). No insistas si dice que no.

**Activa — al invocar `/notario`.**
1. `python .claude/skills/notario/scripts/expediente.py scan --autor "<nombre>"` barre el repo:
   commits del usuario, tableros del equipo (`TABLERO_BEHOLDER.md`, `reportes/`), impactos con cifra,
   evidencia 🟢/🔵 del ledger a favor de la disciplina y fuentes con señal de problema (contra).
   Devuelve **candidatos**; nada se registra solo.
2. Si el usuario lo pide en esa consulta, busca en sus conectores personales (Gmail, Drive,
   Calendario) con consultas por nombre del entregable, fechas y participantes. Advierte que el
   trabajo suele vivir en la cuenta corporativa, que este entorno no ve.
3. Pregunta por lo que solo el usuario sabe, con esta lista corta:
   - ¿Qué archivo es, quién lo creó, cuándo y con quién se compartió cada versión?
   - ¿Hay correos, chats o invitaciones de las sesiones de trabajo? ¿Quién asistió?
   - ¿Quién dijo qué sobre el rol, cuándo, con qué palabras exactas y ante quién?
   - ¿Qué resultados del equipo están **medidos** (no estimados)? ¿Quién los puede confirmar?

## 2. Registro

**Primero, quién es quién.** Antes de analizar, confirma el rol de cada persona y su relación con el
usuario (jefatura directa, nivel superior, par, equipo). Un mismo comentario pesa distinto según quién
lo dice y qué decide. No supongas jerarquías: pregunta o márcalas "por confirmar".
`expediente.py actor <caso> --nombre ... --rol ... --relacion ... --decide ... --postura ...`

`expediente.py add <caso> --cat <categoria> --fecha AAAA-MM-DD --titulo ... --fuerza ...`

| Categoría | Qué entra |
|---|---|
| `autoria` | quién hizo qué y cuándo |
| `impacto` | resultados con cifra y fuente; marcar `--medido medido|estimado` |
| `valor` | evidencia externa del ledger (`--refs F-n`); ver `references/argumentario.md` |
| `senal` | lo que se dijo o decidió sobre el rol; `--literal` solo si son palabras exactas; `--testigos` |
| `contra` | la mejor versión de la otra postura, con `--respuesta` |

| Fuerza | Significado |
|---|---|
| 🟢 `doc` | metadato, historial de versiones, correo o invitación con fecha y autor |
| 🔵 `indirecto` | tablero, minuta, acta, entregable sin firma |
| 🟡 `nota` | nota propia escrita el mismo día |
| 🟠 `recuerdo` | testimonio posterior o de oídas |
| 🔴 `inferencia` | interpretación: se registra rotulada, nunca como hecho |

Reglas: la fecha es la del **hecho**, no la del registro. Una paráfrasis nunca va como cita literal.
Lo que contó un tercero es 🟠 hasta que esa persona lo escriba ella misma.

## 3. Expediente y respuesta

`expediente.py render <caso>` escribe `research/privado/expediente/<caso>.md`: conteos, **huecos a
cerrar**, línea de tiempo y registros por categoría.

Al usuario se le entrega, en este orden y con la regla de redacción del proyecto:
1. **Lectura de la situación** en 3-5 líneas: qué está en juego y qué es hecho vs. interpretación.
2. **La mejor versión de la otra postura** (obligatorio, antes de los argumentos).
3. **Argumentos** ordenados por fuerza: primero autoría documental y resultados medidos, luego
   evidencia externa, al final las señales.
4. **Huecos** y cómo cerrarlos esta semana.
5. **Jugadas** ordenadas de menor a mayor escalamiento, con el riesgo de cada una. Por defecto, la
   primera jugada es una conversación directa y por escrito con la persona involucrada, no una
   escalada.
6. **Plan B** (la mejor alternativa si la negociación falla): fortalece cualquier conversación.

## 4. Lo que el Notario no hace

- No escribe correos ni mensajes a terceros sin que el usuario lo pida y revise el texto.
- No diagnostica intenciones: "me quitó el crédito" es 🔴 hasta que haya hechos que lo sostengan.
- No da asesoría legal; si el caso toca despido, discriminación o acoso, recomienda un abogado
  laboralista o el canal formal de la empresa.
