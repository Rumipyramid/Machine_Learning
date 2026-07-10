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

Cuando se invoque, ejecuta estos pasos de principio a fin:

## 1. Investigar (búsqueda web)
Busca evidencia/datos **recientes (~últimos 6 meses)** sobre comportamiento, percepción y
demanda de seguros en **Perú** (y LatAm como referencia). Prioriza fuentes verificables con
cifras concretas: **INEI, BCRP, SBS, APESEG, APEIM, MAPFRE, OECD**, prensa especializada y
literatura. Haz 3–5 búsquedas con ángulos distintos. **No inventes datos**; si no hay evidencia
nueva fuerte para algo, dilo.

**Evita repetir** variables que ya existen o ya fueron propuestas:
- Ya en el modelo: `generacion, nse, region, educacion_financiera, sesgo_presente,
  canal_preferido, exposicion_riesgo_sismico, apertura_datos_ia, confianza_aseguradora,
  tenencia_seguro, seguro_desastres_naturales, wtp_ratio`.
- Ya propuestas (revisar último reporte en `research/updates/`): `acceso_digital,
  situacion_laboral, bancarizado, experiencia_siniestro, conciencia_riesgo_climatico,
  cobertura_salud_publica, influencia_social`.
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

## 3. Indexar en el códice
Edita `CLAUDE.md`: inserta la nueva entrada **arriba** del bloque gestionado, entre los
marcadores (más reciente primero):
```
<!-- LAPUERTA_REPORTS_START -->
- AAAA-MM-DD — `research/updates/AAAA-MM-DD_fortalecimiento_modelo.md`
... (entradas previas) ...
<!-- LAPUERTA_REPORTS_END -->
```

## 4. Commitear y subir
Haz commit del reporte nuevo + `CLAUDE.md` y push a la rama de trabajo actual
(mensaje: `Reporte quincenal de fortalecimiento del modelo (AAAA-MM-DD)`).

## 5. Resumir al usuario
Muestra en el chat el **resumen ejecutivo** y las 2–3 variables candidatas de mayor prioridad,
con la ruta del archivo creado.

## Notas
- Si ya existe un reporte con la fecha de hoy, **actualízalo** en vez de duplicarlo.
- Mantén el mismo formato/tono del primer reporte (`research/updates/2026-06-21_fortalecimiento_modelo.md`)
  como referencia de calidad.
- Las propuestas son de diseño; recordar que deben recalibrarse con micro-datos (ENAHO/ENDES)
  antes de usarse en decisiones reales.
