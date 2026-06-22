# 🐉 Beholder — Tablero de proyecto estilo Jira con economía de fichas

Skill de [Claude Code](https://claude.com/claude-code) que toma el estado de un proyecto
—nuevo o en curso (WIP)— y lo ordena en un **tablero estilo Jira escrito en Markdown**,
administrando además una **economía de fichas** que mantiene honesta la capacidad real de
cada colaborador.

El Beholder es el "ojo supervisor": entrevista corto y adaptativo → renderiza un tablero
con resumen, columnas por estado, épicas/quests, **libro mayor de fichas**, registro de
riesgos e impacto.

---

## 📂 Estructura del skill

```
beholder/
├── SKILL.md                          # Definición del skill (frontmatter + instrucciones)
├── README.md                         # Este archivo
├── CHANGELOG.md                      # Historial de versiones
└── examples/
    └── TABLERO_BEHOLDER_ejemplo.md   # Ejemplo de salida completo (datos ficticios)
```

`SKILL.md` es el único archivo que Claude Code necesita para cargar el skill. El resto es
documentación y ejemplos para que sea fácil de entender e instalar desde GitHub.

---

## 🚀 Instalación

El skill es una carpeta dentro de `.claude/skills/`. Para usarlo en otro repositorio o de
forma global, copia la carpeta `beholder/` completa:

**Por proyecto** (solo este repo):
```bash
mkdir -p tu-repo/.claude/skills
cp -r .claude/skills/beholder tu-repo/.claude/skills/
```

**Global** (todas tus sesiones):
```bash
mkdir -p ~/.claude/skills
cp -r .claude/skills/beholder ~/.claude/skills/
```

**Desde el repo independiente** (si lo publicas como repo propio, ver más abajo):
```bash
git clone https://github.com/<owner>/beholder ~/.claude/skills/beholder
```

Luego **recarga / reinicia Claude Code** para que registre el skill. En una sesión nueva ya
queda disponible automáticamente.

> Requisito mínimo: que el archivo `SKILL.md` con su frontmatter (`name`, `description`) esté
> presente. Los demás archivos son opcionales.

---

## 🕹️ Uso

Invócalo explícitamente:

```
/beholder
```

O simplemente describe en qué anda un proyecto: el skill se dispara **aunque no digas
"Jira" ni "tablero"** cuando hablas de épicas, quests, fichas, capacidad del equipo,
behavioral designers, riesgos o impacto, o cuando pegas notas sueltas (nuevas o WIP) y
quieres estructurarlas.

El Beholder conduce una **entrevista corta** (¿nuevo o WIP? → cabecera → roster → épicas →
quests con desglose de fichas → reconciliación) y luego **renderiza el tablero**, lo guarda
(sugiere `TABLERO_BEHOLDER.md`) y **cierra con un link funcional al archivo**.

---

## 🎟️ La economía de fichas (8/2)

Cada colaborador tiene **10 fichas** = su capacidad total. La regla de oro: **8 comprometidas
en quests + 2 de reserva** para overhead (correos, material, contexto, imprevistos).

| Fichas comprometidas | Estado | Lectura |
|---|---|---|
| **< 8** | ⚪ Con holgura | Informativo: se registra, no es alerta. |
| **= 8** | 🟢 Óptimo | Capacidad completa, reserva intacta. |
| **9–10** | 🔴 Sobreasignado | Consume reserva de overhead → **alerta** + propuesta de ajuste. |
| **> 10** | ⛔ Inválido | Imposible; **se corrige antes de cerrar** el tablero. |

La holgura solo se informa; el sobreasignado se marca con alerta; el inválido bloquea el
cierre.

---

## ✅ Campos obligatorios por quest

Antes de cerrar el tablero, cada quest debe tener: **Épica · Quest · Fichas asignadas (con
desglose por colaborador) · Behavioral designers · Riesgos · Impacto.** El `Estado` lo
agrega el skill (asume `To Do` si no se indica).

---

## 📄 Qué produce

Un tablero Markdown con: resumen, columnas Jira (`Backlog/To Do/In Progress/In Review/Done`),
detalle de épicas y quests, **libro mayor de fichas** con alertas de capacidad, registro de
riesgos e impacto. Mira un ejemplo completo en
[`examples/TABLERO_BEHOLDER_ejemplo.md`](examples/TABLERO_BEHOLDER_ejemplo.md).

---

## 🔧 Compatibilidad

- Claude Code (CLI, web, desktop, IDE). El skill es 100% Markdown/instrucciones: no requiere
  dependencias ni red.
- El entregable es Markdown legible, no una exportación real de Jira.

## 📦 Publicar como repositorio independiente

La raíz del repo standalone **es** el contenido de esta carpeta (`SKILL.md`, `README.md`,
`CHANGELOG.md`, `LICENSE`, `examples/`). Por eso, al publicarlo, se instala con un simple
`git clone <url> ~/.claude/skills/beholder`.

Desde el repo contenedor hay un script que lo empaqueta e inicializa git automáticamente:

```bash
scripts/publish_beholder_standalone.sh ~/beholder
# luego: crear repo vacío en GitHub, agregar remote y push
```

O a mano: copia el contenido de `.claude/skills/beholder/` a una carpeta nueva, `git init`,
commit y push a un repo llamado `beholder`.

## 📌 Versión y licencia

Versión actual: ver [`CHANGELOG.md`](CHANGELOG.md). Licencia: [MIT](LICENSE).
