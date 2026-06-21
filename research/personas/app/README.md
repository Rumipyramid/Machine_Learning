# Explorador de Usuarios Sintéticos · Seguros Perú

Interfaz web minimalista para **hacer preguntas a una población sintética** de consumidores de
seguros (Perú) y obtener **gráficos de distribución, desglose por segmento e insights redactados**.

## Cómo abrirla

- **Opción A (un solo archivo):** abre `explorador_standalone.html` con doble clic en cualquier
  navegador. No requiere internet ni servidor.
- **Opción B (modular):** abre `index.html` (carga `engine.js` desde la misma carpeta). Si tu
  navegador bloquea scripts locales, sirve la carpeta:
  `python -m http.server` y entra a `http://localhost:8000/`.

## Qué hace

1. **Elige una pregunta** (confianza, intención de compra, tenencia, opinión de una marca,
   apertura a datos/IA).
2. **Filtra el segmento** (NSE, generación, región, canal) y define tamaño de muestra + semilla.
3. Pulsa **“Preguntar a los usuarios”** y obtén:
   - Distribución de respuestas (barras).
   - Desglose por segmento (barras apiladas, dimensión seleccionable).
   - **Hallazgos & insights** con lectura ejecutiva y una recomendación.

## Archivos

| Archivo | Rol |
|---|---|
| `engine.js` | Motor: generación de perfiles, simulación de respuestas, insights. Testeable en Node. |
| `index.html` | Interfaz (carga `engine.js`). |
| `explorador_standalone.html` | App en un único archivo (engine embebido). |
| `build_standalone.js` | Reconstruye el standalone: `node build_standalone.js`. |

El motor reusa las distribuciones de `../synthetic_user_schema.json` (SBS 2023, APESEG, APEIM).

> **Datos sintéticos:** no representan personas reales. Para prototipado, exploración de hipótesis
> y diseño de mensajes; no sustituyen una encuesta de mercado.
