---
name: cerrajero
description: >-
  Invocado con /cerrajero. Barre incrementalmente, en grupos de 5, las fuentes de máximo
  rigor (🟢A "verde") ya registradas en el códice de cronista (research/fuentes/codice.md),
  con memoria persistente entre invocaciones para no revisar dos veces el mismo estudio.
  Evalúa si cada fuente del grupo sugiere una variable nueva o una recalibración para el
  modelo de usuarios sintéticos ("lapuerta"), y siempre cierra preguntándole al usuario si
  quiere aplicar los hallazgos al modelo — nunca aplica solo. Invócalo con /cerrajero o
  cuando se pida "barrer el códice", "revisar la literatura verde" o "seguir con el
  siguiente grupo de fuentes para el modelo".
---

# cerrajero · Barrido incremental de literatura verde para el modelo `lapuerta`

> Invocación: **`/cerrajero`**.
>
> **Mecanismo (2026-07-23):** este skill ya no busca evidencia nueva en la web — relee,
> en grupos de 5, la literatura de rigor **🟢A** que otras investigaciones del proyecto
> (`/seeker`, `/trinidad`, etc.) ya registraron en el códice de `cronista`
> (`research/fuentes/codice.md`), evaluando si algo de eso implica una variable nueva o una
> recalibración para el modelo `lapuerta` que no se haya aplicado todavía. Mantiene memoria
> persistente entre invocaciones (no repite estudios ya barridos) y **nunca aplica cambios
> por su cuenta**: siempre termina preguntándole al usuario si quiere actualizar el modelo.
>
> **Divergencia con la versión desatendida:** el GitHub Action
> `.github/workflows/fortalecimiento-modelo.yml` (`research/updates/generate_report.py`)
> **no se modificó** junto con este skill — sigue haciendo búsqueda web de evidencia nueva
> de forma automática y aplicando sola la prioridad Alta (con PR aparte para revisión). Las
> dos versiones de "fortalecimiento del modelo" ahora usan mecanismos distintos: `/cerrajero`
> relee literatura ya vetada del proyecto; el Action busca evidencia nueva en internet. Avisar
> al usuario si en algún momento se quiere alinear ambas.

Cuando se invoque, ejecuta estos pasos de principio a fin:

## 1. Armar el siguiente grupo de 5

1. Lee `research/fuentes/codice.md` y filtra las filas cuya columna de Rigurosidad empiece
   con **🟢 A** ("verde"), en el orden en que aparecen (orden ascendente de `F-n`).
2. Lee (o crea si no existe) `research/updates/cerrajero_barrido_estado.json` — la memoria
   persistente del barrido. Si no existe, créalo con `f_ids_barridos_total: []` y `barridos: []`.
3. Descarta de la lista de 🟢A los `F-n` que ya estén en `f_ids_barridos_total`.
4. Toma los siguientes **5** IDs no barridos (los primeros 5 la primera vez que se invoque
   el skill). Si quedan menos de 5, toma los que queden.
5. Si no queda ninguno sin barrer: informa al usuario que ya se revisó toda la literatura
   🟢A del códice al menos una vez, y pregúntale si quiere **reiniciar el ciclo** (útil porque
   el códice sigue creciendo con cada investigación nueva). No reinicies sin confirmación —
   termina aquí si no la da.

## 2. Revisar cada una de las 5 fuentes

Para cada fuente del grupo, relee su fila completa (resumen, autor/año, "usado en/fundamenta")
y evalúa explícitamente contra el modelo `lapuerta` — lee `variables`/`modelos_derivados` de
`research/personas/generador/synthetic_user_schema.json` **en el momento** (no una lista fija)
más la tabla "Pendientes de incorporar" de `matriz_usuarios_sinteticos.md`, igual que hacía
este skill antes para no proponer duplicados. Clasifica cada fuente en una de tres:

- **(a) Variable candidata nueva** — la evidencia sugiere una dimensión que el esquema no
  captura todavía.
- **(b) Recalibración** — la evidencia afina/corrige una variable o distribución ya existente.
- **(c) Sin relación con el modelo de personas** — la fuente fundamenta otro node del proyecto
  (glosario, behavioral design, salud, etc.) pero no aporta nada al generador. **Es un
  resultado legítimo y esperado para buena parte del barrido — no fuerces una relación que
  no existe.**

## 3. Registrar el barrido en la memoria

Actualiza `research/updates/cerrajero_barrido_estado.json`: agrega una entrada al array
`barridos` con `fecha` (hoy), `f_ids` (los 5 de este grupo) y un `hallazgo` de una línea por
fuente (a/b/c + qué implica). Agrega esos mismos `F-n` a `f_ids_barridos_total`.

## 4. Redactar hallazgos (solo si hubo candidatas)

Si el grupo produjo al menos una candidata (a) o (b), crea/actualiza
`research/updates/AAAA-MM-DD_barrido_verde_cerrajero.md` (fecha de hoy; si ya existe uno de
hoy, amplíalo) con: resumen ejecutivo, tabla `variable candidata | evidencia (F-n) | cómo
incorporarla | tipo (nueva/recalibración) | prioridad`, y detalle por variable (definición,
evidencia, snippet JSON ilustrativo si aplica). Cita las fuentes por `F-n`, no repitas el
texto completo del códice. Si el grupo no produjo ninguna candidata, no crees archivo —
repórtalo solo en el chat.

## 5. Preguntar al usuario (el entregable central de este skill)

Cierra **siempre** con una pregunta explícita — nunca apliques nada sin que el usuario
responda que sí, sin importar cuán clara parezca la evidencia:

- Si hubo candidatas: resume cada una en una línea y pregunta *"¿Quieres que actualice el
  modelo de personas sintéticas con [estos hallazgos / esta variable]?"*
- Si no hubo candidatas: dilo con honestidad ("este grupo no aportó nada nuevo al modelo —
  ya estaba cubierto por `sesgo_presente`/`educacion_financiera`/etc., o fundamenta otro
  node") y pregunta si quiere continuar de una vez con el siguiente grupo de 5 o dejarlo
  para otra sesión.

## 6. Aplicar (solo si el usuario confirma que sí)

Si el usuario confirma, aplica cada candidata con la misma disciplina que este skill ya
usaba para prioridad Alta:
1. Agrégala a `synthetic_user_schema.json` (`variables` si es independiente/condicional,
   `modelos_derivados` si es derivada).
2. Agrega su función `sample_*` a `generate_synthetic_users.py` y su llamada en
   `generate_user()` (en orden de dependencia), más el campo en el dict de salida.
3. Genera una muestra grande (`--n 20000 --seed 42`) y **mide** la marginal resultante contra
   el objetivo de la evidencia — ajusta el intercepto empíricamente si se desvía (no confíes
   en el snippet sin medir).
4. Corre `python research/personas/generador/validate.py --check`.
   - Si **falla**: revierte los cambios de esquema/generador para esa variable y déjala en
     "Pendientes de incorporar" de `matriz_usuarios_sinteticos.md` con nota "⚠️ intentó
     aplicarse vía /cerrajero (barrido AAAA-MM-DD) sobre F-n, no pasó validate.py --check".
   - Si **pasa**: consérvala.
5. Actualiza `matriz_usuarios_sinteticos.md` (mueve la variable a su tabla, nota de versión
   `v1.N (fecha)` con la marginal medida y cualquier recalibración de intercepto).
6. Sube `meta.version` (+0.1) y `meta.fecha` en el esquema.
7. Indexa en `CLAUDE.md`: si se aplicó alguna variable, actualiza la línea "Variables (N,
   esquema v1.N)" y "Marginales validadas" del bloque de personas sintéticas.

Si el usuario dice que no (o "todavía no"), no toques nada del modelo — el barrido ya quedó
registrado en la memoria de todos modos (paso 3), así que la próxima invocación sigue con el
siguiente grupo sin volver a preguntar por estas mismas fuentes.

## 7. Commitear y subir

Commitea siempre `research/updates/cerrajero_barrido_estado.json` (y el reporte de hallazgos
si se creó) — el barrido en sí es progreso que no debe repetirse, independientemente de si el
usuario aplicó algo. Si además se aplicó una variable (paso 6), súmala al mismo commit o haz
uno inmediatamente después con `synthetic_user_schema.json`, `generate_synthetic_users.py`,
`matriz_usuarios_sinteticos.md` y `CLAUDE.md`. Push a la rama de trabajo actual.

## Notas

- El orden de barrido es por `F-n` ascendente (orden de registro en el códice), no por fecha
  de publicación del estudio ni por tema.
- Las fuentes 🟢A nuevas que se agreguen al códice más adelante (por cualquier skill de
  investigación) quedan automáticamente en la cola de "no barridas" — el barrido las alcanza
  en su turno según su `F-n`.
- Este skill nunca decide solo por prioridad — a diferencia de la versión anterior (que
  aplicaba Alta automáticamente), ahora **toda aplicación pasa por confirmación explícita del
  usuario**, porque el barrido revisita literatura ya usada para otros fines, no evidencia
  nueva dedicada al modelo.
