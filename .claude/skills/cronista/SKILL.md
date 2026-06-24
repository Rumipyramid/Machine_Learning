---
name: cronista
description: >-
  El Cronista es el archivero del códice: cada vez que usas evidencia
  referenciable para crear o fundamentar algo, anota esa fuente en un ledger
  persistente con su resumen breve, una calificación de rigurosidad
  metodológica, autor y año. Úsalo SIEMPRE que cites o te apoyes en una fuente
  externa —papers, estudios, reportes de industria, estadísticas oficiales,
  encuestas, libros, normativa, datasets o páginas web— para afirmar un dato,
  sustentar una investigación, parametrizar un modelo, calibrar un supuesto o
  justificar una decisión; cuando agregues una cifra o hallazgo que venga de
  afuera; cuando menciones a un autor u organismo y un año; o cuando el usuario
  hable de fuentes, bibliografía, citas, referencias, evidencia o rigurosidad.
  Dispárate aunque el usuario no diga "fuente": si lo que escribes se apoya en
  algo referenciable, el Cronista lo registra.
---

# 📜 El Cronista — Registro de evidencia del códice

El Cronista es el archivero que acompaña al códice. Cada vez que usas **evidencia
referenciable** para **crear** (una investigación, un dato, un esquema, un modelo)
o para **fundamentar** (un supuesto, una decisión, una afirmación), el Cronista
deja constancia de esa fuente en un **ledger persistente y versionado**, para que
el conocimiento del proyecto nunca quede sin trazabilidad.

Tu trabajo cuando este skill se dispara es **registrar cada fuente que usaste**, no
solo citarla en el texto. Una fuente sin entrada en el ledger es conocimiento que
se pierde.

---

## Dónde vive el ledger

| | |
|---|---|
| **Archivo único** | `research/fuentes/registro_fuentes.md` |
| **Rol** | "El espacio del códice" donde se acumulan los resúmenes de fuentes. |
| **Indexado en** | `CLAUDE.md` (mapa de archivos). |

Si el archivo no existe, **créalo** con la cabecera, la rúbrica de rigurosidad y la
tabla vacía (ver *Plantilla del ledger* abajo) antes de añadir la primera entrada.
Nunca disperses fuentes en otros archivos: el ledger es la fuente única de verdad.

---

## Qué se registra por cada fuente (el contrato de campos)

Toda entrada del ledger tiene **estos campos obligatorios**:

| Campo | Qué es | Regla |
|---|---|---|
| **ID** | Clave corta `F-n` | Correlativo; nunca se reusa ni se renumera. |
| **Autor** | Persona(s) u organismo que produjo la fuente | Si no hay autor personal, usa el organismo/medio editor. Si se desconoce, `Anónimo`. |
| **Año** | Año de publicación de la fuente | Si no hay fecha, `s.f.`. Si es serie/actualización, el año de la edición citada. |
| **Fuente / Título** | Nombre del documento, estudio o página | Lo más específico posible (no solo el dominio). |
| **Rigurosidad** | Calificación metodológica `A`–`E` (ver rúbrica) | Siempre asignada, con una justificación de una línea. |
| **Resumen breve** | 1–2 frases: qué dice y por qué es relevante | Conciso; no copies abstracts largos. |
| **Usado en / fundamenta** | Dónde y para qué la usaste en el proyecto | Ej. "dato de penetración 2.08% en `seguros_…md`". |
| **URL / referencia** | Enlace o cita completa | Si es offline (libro/PDF local), pon la cita bibliográfica. |
| **Registrado** | Fecha `YYYY-MM-DD` en que se anotó | Usa la fecha de hoy. |

---

## Rúbrica de rigurosidad metodológica

Califica el **método con que se produjo el dato**, no el tipo de fuente ni el
prestigio de la marca. Para ubicar el nivel, lee estas **señales**: ¿datos
primarios o reempaquetados?, ¿muestra/tamaño declarados?, ¿metodología
transparente y replicable?, ¿revisión por pares?, ¿qué tan vigente es el dato
(año)? Asigna el nivel y, si quieres afinar, añade un **modificador `+` / `−`**
dentro del nivel. Justifica siempre en una línea.

| Nivel | Etiqueta | El método cumple… | Ejemplos típicos |
|---|---|---|---|
| **A** | 🟢 Alta | Datos primarios + **revisión por pares** + muestra y metodología explícitas y replicables. | Papers indexados con DOI (ScienceDirect, Springer, MDPI). |
| **B** | 🔵 Sólida | Datos primarios u oficiales con metodología documentada y trazable, **sin** revisión por pares. | Reguladores/organismos: SBS, APESEG, OECD, EIOPA. |
| **C** | 🟡 Media | Estudio propio (encuesta/análisis) con muestra o método declarados pero **no auditables** por terceros. | Consultoras/reaseguradoras: McKinsey, Bain, EY, Swiss Re. |
| **D** | 🟠 Baja | **Sin método propio**: reempaqueta o cita datos de terceros. | Prensa (Infobae), blogs corporativos, agregadores de mercado. |
| **E** | 🔴 Débil | **Sin método ni origen verificable**: opinión, anónimo o fecha desconocida. | Posts de opinión, foros, afirmaciones sin respaldo. |

**Modificadores** (opcionales, para afinar dentro del nivel):
- `+` cuando hay una señal extra de rigor (p. ej. muestra grande y transparente:
  *Bain con 28,765 encuestados en 14 países → C+*).
- `−` cuando una señal resta (dato viejo, tras *paywall*, posible conflicto de
  interés, muestra opaca).

Reglas de la rúbrica:
- La calificación es del **método, no del tipo de fuente ni del prestigio**: un
  regulador con metodología floja puede bajar a C, y una consultora con muestra
  enorme y transparente puede subir a C+.
- **Primario > secundario.** Si una fuente secundaria (D) cita un dato primario
  fuerte, registra de ser posible la **fuente primaria**; si solo tienes la
  secundaria, déjala en D y anota en el resumen quién es la fuente original.
- **Vigencia:** distingue el año de *publicación* del año de los *datos*. Un
  informe nuevo con datos viejos merece un `−`.
- Ante la duda entre dos niveles, **baja medio escalón** y explica por qué.

---

## Flujo cuando el skill se dispara

1. **Detecta la evidencia usada.** Recorre lo que acabas de escribir/crear e
   identifica cada fuente referenciable en la que te apoyaste (papers, reportes,
   estadísticas, normas, datasets, páginas web, resultados de búsqueda).
2. **Abre o crea el ledger** (`research/fuentes/registro_fuentes.md`).
3. **Deduplica.** Antes de añadir, busca si la fuente ya existe (por URL, o por
   `Autor + Año + Título`):
   - **Si ya existe:** no dupliques. Actualiza su campo *Usado en / fundamenta*
     agregando el nuevo contexto, y corrige datos si tienes mejor información.
   - **Si es nueva:** asígnale el siguiente `F-n` y crea la fila.
4. **Rellena los campos obligatorios**, calificando la rigurosidad con la rúbrica
   y su justificación de una línea.
5. **Guarda** el ledger y, en tu respuesta al usuario, menciona brevemente qué
   fuentes registraste (p. ej. *"Registré 2 fuentes en el ledger: F-12 (SBS 2023, B)
   y F-13 (Bain 2023, C)."*).

No conviertas esto en una entrevista: trabaja con lo que tienes. Si falta un dato
obligatorio (p. ej. el año), usa la convención (`s.f.`) y sigue.

---

## Plantilla del ledger

Cuando crees el archivo por primera vez, úsalo exactamente con esta estructura:

```markdown
# 📜 Registro de fuentes — Códice de evidencia

> Ledger persistente que mantiene el skill `cronista`. Cada fuente usada para
> crear o fundamentar contenido del proyecto se anota aquí: resumen breve,
> rigurosidad metodológica, autor y año. Fuente única de trazabilidad.

## Rúbrica de rigurosidad
> Califica el método, no el tipo de fuente. Modificadores opcionales `+`/`−` afinan dentro del nivel.

| Nivel | Etiqueta | El método cumple… |
|---|---|---|
| A | 🟢 Alta | Datos primarios + revisión por pares + muestra y metodología replicables. |
| B | 🔵 Sólida | Datos primarios u oficiales con metodología documentada y trazable, sin revisión por pares. |
| C | 🟡 Media | Estudio propio con muestra/método declarados pero no auditables por terceros. |
| D | 🟠 Baja | Sin método propio: reempaqueta o cita datos de terceros. |
| E | 🔴 Débil | Sin método ni origen verificable: opinión, anónimo o fecha desconocida. |

## Fuentes registradas
| ID | Autor | Año | Fuente / Título | Rigurosidad | Resumen breve | Usado en / fundamenta | URL / referencia | Registrado |
|---|---|---|---|---|---|---|---|---|
| F-1 | … | … | … | 🟢 A — {justificación} | … | … | … | YYYY-MM-DD |
```

---

## Notas de estilo y robustez

- **Escribe en español**, como el resto del códice.
- **No inventes fuentes ni datos.** Si no recuerdas el autor o el año exactos, usa
  `Anónimo` / `s.f.` antes que adivinar. El ledger debe ser confiable.
- **Resúmenes cortos**: 1–2 frases. El ledger es un índice, no un repositorio de
  textos completos.
- **Cada fuente, una sola fila.** La trazabilidad se mantiene con dedup, no con
  filas repetidas.
- **Siempre califica la rigurosidad**, aun cuando sea baja. Una fuente D o E
  registrada y marcada como tal es más útil que un dato sin origen.
- Mantén el ledger **sincronizado con `CLAUDE.md`**: si el archivo cambia de ruta,
  actualiza el mapa de archivos del códice.
