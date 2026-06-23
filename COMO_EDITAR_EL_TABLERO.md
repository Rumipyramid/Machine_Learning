# ✏️ Cómo editar el tablero Beholder

Guía rápida para el equipo. El tablero vive en este repo:
- **Tablero (Markdown):** [`TABLERO_BEHOLDER.md`](TABLERO_BEHOLDER.md)
- **Matriz de status (Excel):** [`reportes/Status_Proyectos_Behavioral_Design.xlsx`](reportes/Status_Proyectos_Behavioral_Design.xlsx)
- **Skill que lo genera:** [`.claude/skills/beholder/`](.claude/skills/beholder/)

Hay dos formas de editarlo. La **Opción A (desde Claude)** es la más cómoda.

---

## ✅ Antes de empezar (una sola vez)
1. Tener una **cuenta de Claude con Claude Code** (plan Pro o Max, o estar en un plan Team).
2. Ser **colaborador de este repo con permiso “Write”** (pídeselo a la dueña del repo).

---

## 🅰️ Opción A — Editar desde Claude (recomendado)

Como el skill **Beholder** ya está dentro del repo, el comando `/beholder` se carga solo. No instalas nada.

1. Entra a **https://claude.ai/code** e inicia sesión.
2. **Conecta tu GitHub** y da acceso al repo `Rumipyramid/Machine_Learning`.
3. **Abre una sesión** eligiendo el repo `Rumipyramid/Machine_Learning` y la rama **`main`**.
4. Escríbele a Claude en lenguaje normal lo que quieres cambiar. Ejemplos:
   - `/beholder cambia el estado de Q-6 (Loyalty) a In Review y el avance a 80%`
   - `/beholder agrega un riesgo a Q-4: "demora del área de Finanzas", severidad media`
   - `/beholder marca Q-3 como Done`
5. Claude edita `TABLERO_BEHOLDER.md`, hace **commit y push** y te deja el link.
6. **Cuando termines, escribe `/actualizar`** para subir tus cambios a `main` y que todo el equipo
   los vea. (También trae lo último de los demás antes de publicar.)

> 💡 Cada sesión de Claude trabaja en **su propia rama**. Tus cambios recién aparecen para el resto
> cuando llegan a `main` — eso es justo lo que hace `/actualizar`.

---

## 🅱️ Opción B — Editar directo en GitHub (sin Claude)

Para cambios chiquitos al **tablero Markdown**:
1. Abre [`TABLERO_BEHOLDER.md`](TABLERO_BEHOLDER.md) en GitHub.
2. Clic en el **lápiz ✏️** (Edit).
3. Edita el texto.
4. Abajo, **“Commit changes”** (Guardar) — escribe en una línea qué cambiaste.

---

## 🔄 Publicar tus cambios: `/actualizar`
Cuando termines de editar, escribe **`/actualizar`**. Ese comando:
1. Guarda tus cambios, 2) trae lo último de `main` (lo de tus compañeros), 3) **fusiona tus cambios
a `main`** y 4) te deja el link. Así todos ven tu actualización.

> Las **fechas** siguen necesitando aprobación del owner: `/actualizar` no las publica sin aprobar.

## 🤝 Para no pisarse entre varios
- Cada quien trabaja en **su propia rama** (su sesión de Claude). Al terminar, **`/actualizar`**
  lleva lo tuyo a `main` y trae lo de los demás. Así queda registro y nadie sobrescribe a otro.
- Si dos editaron lo mismo, `/actualizar` avisa del choque y lo resuelven antes de publicar.

---

## 📊 Sobre el Excel
GitHub **no** edita archivos `.xlsx` en el navegador. Dos caminos:
- **A)** Pídele a Claude que lo **regenere** (el generador está en `reportes/generar_matriz_status.py`).
- **B)** Descárgalo → edítalo en Excel → vuelve a subirlo (reemplazar).

Recomendación: llevar el status del día a día en el **tablero Markdown** (más fácil de editar entre
varios) y regenerar el Excel cuando haga falta compartirlo.

---

## 📌 Recordatorios del Beholder
- Cada colaborador tiene **10 fichas** = 8 comprometibles en quests + 2 de reserva (overhead).
- Estados de capacidad: ⚪ holgura (<8) · 🟢 óptimo (8) · 🔴 sobreasignado (9–10) · ⛔ inválido (>10).
- Más detalle en el [README del skill](.claude/skills/beholder/README.md).
