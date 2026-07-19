---
name: cerrajero
description: >-
  Ejecuta a demanda, dentro de la sesión, la actualización quincenal del modelo de
  usuarios sintéticos de seguros ("lapuerta"): investiga evidencia/datos recientes con
  búsqueda web, redacta un reporte en Markdown con propuestas para incorporar nuevas
  variables, lo guarda en research/updates/, lo indexa en el códice (CLAUDE.md) y lo
  commitea. Invócalo con /cerrajero o cuando se pida "actualizar/fortalecer el modelo",
  "generar el reporte quincenal" o "buscar evidencia nueva para el modelo de seguros".
---

# cerrajero · Actualización quincenal del modelo `lapuerta`

> Invocación: **`/cerrajero`**. Es la versión **a demanda** (la corre Claude en la sesión,
> con su propia búsqueda web — no necesita API key) del GitHub Action
> `.github/workflows/fortalecimiento-modelo.yml`, que es la versión **desatendida**.
>
> Diferencia importante en el paso 3 (aplicar Alta): esta versión a demanda deja el cambio en
> la rama de trabajo actual de la sesión (igual que el resto de tus ediciones — la revisión
> humana ocurre cuando esa rama se publica a main, p. ej. con `/actualizar`). La versión
> desatendida en cambio **nunca pushea el cambio de esquema directo a main**: lo manda a un
> PR aparte (`lapuerta/alta-auto-AAAA-MM-DD`) para que alguien lo revise antes de mergear,
> porque ahí no hay nadie mirando la sesión en vivo.

Cuando se invoque, ejecuta estos pasos de principio a fin:

## 1. Investigar (búsqueda web)
Busca evidencia/datos **recientes (~últimos 6 meses)** sobre comportamiento, percepción y
demanda de seguros en **Perú** (y LatAm como referencia). Prioriza fuentes verificables con
cifras concretas: **INEI, BCRP, SBS, APESEG, APEIM, MAPFRE, OECD**, prensa especializada y
literatura. Haz 3–5 búsquedas con ángulos distintos. **No inventes datos**; si no hay evidencia
nueva fuerte para algo, dilo.

**Evita repetir** variables que ya existen o ya fueron propuestas:
- Ya en el modelo: lee las claves de `variables` y `modelos_derivados` en
  `research/personas/generador/synthetic_user_schema.json` **en el momento** (no uses una lista
  fija — el esquema cambia cada vez que este skill aplica una propuesta de prioridad Alta).
- Ya propuestas pero aún sin aplicar (Media/Baja, pendientes de revisión manual): tabla
  "Pendientes de incorporar" en `research/personas/generador/matriz_usuarios_sinteticos.md`.
- Busca **ángulos nuevos** o **recalibraciones** con cifras frescas.

## 2. Redactar el reporte
Crea `research/updates/AAAA-MM-DD_fortalecimiento_modelo.md` (fecha de hoy) con esta estructura:
1. Encabezado: fecha + "Próxima revisión" (+15 días) + alcance/método.
2. **Resumen ejecutivo** (3–6 viñetas con la evidencia más fuerte y su cifra).
3. **Tabla**: variable candidata | evidencia/dato | fuente | cómo incorporarla | prioridad | origen.
4. **Detalle por variable**: definición, evidencia, incorporación (distribución/dependencias/efecto).
5. **Cambios propuestos al esquema** (`synthetic_user_schema.json`): snippets JSON ilustrativos
   + nota de re-validación (no romper: tiene seguro ≈ 0.40, desconfía ≈ 0.48, desastres ≈ 0.033).
6. **Fuentes** (lista de URLs).

Marca cada propuesta como `dato` (anclado en fuente) o `supuesto`. Cierra con:
`*Generado por el ciclo quincenal de fortalecimiento del modelo `lapuerta`.*`

## 3. Aplicar automáticamente las propuestas de prioridad Alta
Para **cada** variable candidata marcada **Prioridad: Alta** en la tabla del reporte recién creado:
1. Agrégala a `research/personas/generador/synthetic_user_schema.json` (a `variables` si es
   independiente/condicional, a `modelos_derivados` si es derivada), usando el snippet JSON del
   reporte como punto de partida.
2. Agrega su función `sample_*` a `generate_synthetic_users.py` y su llamada en `generate_user()`
   (en orden de dependencia), y el campo correspondiente al dict de salida.
3. Genera una muestra grande (`--n 20000 --seed 42`) y **mide** la marginal resultante de la
   variable nueva contra el objetivo que declara el reporte. La mezcla logística sobre subgrupos
   suele desviar el resultado del snippet propuesto (p. ej. un intercepto pensado para ~7% puede
   dar ~15% si hay un subsegmento con score alto) — si se desvía, ajusta el intercepto
   empíricamente (barrido de valores) hasta acercarla al objetivo. No confíes en el snippet sin medir.
4. Corre `python research/personas/generador/validate.py --check`.
   - Si **falla**: revierte los cambios de esquema/generador para esa variable, y déjala en la
     tabla "Pendientes de incorporar" de `matriz_usuarios_sinteticos.md` con una nota
     "⚠️ intentó aplicarse automáticamente el AAAA-MM-DD, no pasó validate.py --check".
   - Si **pasa**: consérvala.
5. Actualiza `matriz_usuarios_sinteticos.md`: mueve la variable a su tabla correspondiente (§2 si
   es condicional, §3 si es derivada) y agrega una nota de versión (`v1.N (fecha)`) con lo que se
   validó, siguiendo el formato de las notas v1.1/v1.2/v1.3 existentes (incluye la marginal medida
   y cualquier recalibración de intercepto que hiciste en el paso 3).
6. Sube `meta.version` (+0.1) y `meta.fecha` (hoy) en el esquema.

Las propuestas de prioridad Media/Baja **no** se aplican solas: quedan en "Pendientes de
incorporar" para revisión manual del usuario.

## 4. Indexar en el códice
Edita `CLAUDE.md`: inserta la nueva entrada **arriba** del bloque gestionado, entre los
marcadores (más reciente primero):
```
<!-- LAPUERTA_REPORTS_START -->
- AAAA-MM-DD — `research/updates/AAAA-MM-DD_fortalecimiento_modelo.md`
... (entradas previas) ...
<!-- LAPUERTA_REPORTS_END -->
```
Si el paso 3 aplicó alguna variable, actualiza también la línea "Variables (N, esquema v1.N)" y
"Marginales validadas" del bloque de personas sintéticas en `CLAUDE.md`.

## 5. Commitear y subir
Haz commit de todo lo que haya cambiado — reporte nuevo + `CLAUDE.md` siempre; además
`synthetic_user_schema.json`, `generate_synthetic_users.py` y `matriz_usuarios_sinteticos.md` si
el paso 3 aplicó alguna variable — y push a la rama de trabajo actual (mensaje: `Reporte
quincenal de fortalecimiento del modelo (AAAA-MM-DD)`, + una línea extra si se aplicaron Altas).

## 6. Resumir al usuario
Muestra en el chat el **resumen ejecutivo**, las 2–3 variables candidatas de mayor prioridad, la
ruta del archivo creado, y **qué se aplicó automáticamente** (variable, marginal validada) vs qué
quedó pendiente de revisión manual (y por qué, si algo falló validate.py).

## Notas
- Si ya existe un reporte con la fecha de hoy, **actualízalo** en vez de duplicarlo.
- Mantén el mismo formato/tono del primer reporte (`research/updates/2026-06-21_fortalecimiento_modelo.md`)
  como referencia de calidad.
- Las propuestas Media/Baja son de diseño; recordar que deben recalibrarse con micro-datos
  (ENAHO/ENDES) y revisión humana antes de aplicarse.
- La incorporación automática (paso 3) solo alcanza a prioridad Alta, y siempre está condicionada
  a que `validate.py --check` pase — es una red de seguridad, no una garantía de que la propuesta
  sea correcta; sigue siendo evidencia de un solo reporte, no una recalibración con micro-datos.
