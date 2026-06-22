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

> 💡 Pídele que trabaje en **tu propia rama** y abra un **PR** si quieres revisión antes de fusionar.

---

## 🅱️ Opción B — Editar directo en GitHub (sin Claude)

Para cambios chiquitos al **tablero Markdown**:
1. Abre [`TABLERO_BEHOLDER.md`](TABLERO_BEHOLDER.md) en GitHub.
2. Clic en el **lápiz ✏️** (Edit).
3. Edita el texto.
4. Abajo, **“Commit changes”** (Guardar) — escribe en una línea qué cambiaste.

---

## 🤝 Para no pisarse entre varios
- Lo más seguro: cada quien trabaja en **su propia rama** y abre un **PR** para fusionar a `main`.
  Así queda registro y nadie sobrescribe a otro.
- Si el equipo es chico y está coordinado, también pueden editar `main` directo.

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
