---
name: actualizar
description: >-
  Publica en la rama main los cambios del miembro del equipo, para que todos los
  vean. Úsalo SIEMPRE que el usuario invoque /actualizar, o cuando pida "subir a
  main", "actualizar el main", "publicar mis cambios", "que el equipo vea mis
  cambios" o "sincronizar con main". Toma la rama de trabajo actual, la pone al
  día con main, la fusiona a main y confirma con el link.
---

# 🔄 /actualizar — Publicar cambios a `main`

Deja los cambios del miembro en la rama **`main`**, que es la que todo el equipo ve. Pensado para
que cualquiera del equipo lo use **sin saber de git**: tú haces los pasos por dentro y le explicas
el resultado en simple.

## Qué hace, paso a paso

Trabaja sobre la **rama actual** de la sesión (cada sesión de Claude tiene la suya).

1. **Guardar lo pendiente.** Si hay cambios sin commitear, `git add -A` y commitea con un mensaje
   claro (si el usuario no da uno, resúmelo tú: *"Actualiza tablero: …"*). Si **no hay nada nuevo**
   (ni cambios sin commitear ni commits por delante de `main`), dile *"No hay nada nuevo que
   publicar"* y termina.
2. **Ponerse al día con `main`** (evita conflictos y trae lo de otros):
   ```bash
   git fetch origin
   git merge origin/main          # trae lo último de main a tu rama
   ```
   Si hay **conflicto**, **no sigas**: explica en simple qué archivo chocó y resuélvelo con el
   usuario (o pide ayuda). Nunca publiques a medias.
3. **Publicar a `main`.** Sube tu rama y fusiónala:
   ```bash
   git push -u origin <rama-actual>
   ```
   Luego crea un **PR** de tu rama → `main` y **fusiónalo** (con las herramientas de GitHub). Si la
   fusión automática está bloqueada por protección de rama, dilo claro y pide al **owner** que
   apruebe/fusione.
4. **Confirmar.** Avisa que listo y entrega el **link a `main`** (y al archivo que cambió). Recuerda
   que su sesión **sigue en su rama**; los demás verán el cambio en `main` al refrescar (o con un
   `/actualizar` que primero trae lo de `main`).

## Reglas (gobernanza del Beholder)

- `/actualizar` **no salta** la regla de fechas: los cambios de **fecha proyectada** siguen
  necesitando aprobación del owner (ver `reportes/beholder.config.md` y `reportes/ALERTAS_FECHAS.md`).
  Si se intenta publicar una fecha sin aprobar, déjala en alerta — no la apliques.
- Si el tablero (`TABLERO_BEHOLDER.md`) y la matriz (`reportes/Status_Proyectos_Behavioral_Design.xlsx`)
  quedaron desalineados, avísalo (o regenera el Excel) antes de cerrar.
- Reintenta `push`/`fetch` ante errores de red (2s, 4s, 8s, 16s).

## Mensaje de cierre (ejemplo)

> ✅ Listo, tus cambios ya están en **main** y el equipo los verá al refrescar.
> 🔗 main: `https://github.com/<owner>/<repo>/tree/main`
> (Tu sesión sigue en tu rama; para traer lo último de otros, usa `/actualizar` de nuevo o abre una
> sesión nueva.)
