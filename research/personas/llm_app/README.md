# Preguntas libres a usuarios sintéticos — respondidas por Claude

Hazle **cualquier pregunta** (no predeterminada) a la población sintética. **Claude responde con su
cerebro** (`claude-opus-4-8`), pero haciendo *role-play* de cada persona **según los parámetros que
construimos** (NSE, generación, región, educación financiera, sesgo del presente, canal, confianza,
tenencia, exposición sísmica, apertura a datos/IA, WTP — calibrados con SBS/APESEG/APEIM).

A diferencia del explorador por reglas (`../app/`), aquí las respuestas son texto libre en primera
persona, razonadas por el modelo a partir del perfil de cada persona.

## Cómo funciona

1. El backend muestrea N perfiles con el generador calibrado (`../generate_synthetic_users.py`).
2. Construye un prompt con el **codebook** de los parámetros + la pregunta + las personas en JSON.
3. Llama a Claude **una sola vez** con *structured outputs* (JSON schema): devuelve, validado,
   `quote` + `sentiment` (favorable/neutral/desfavorable) por persona, más `insights` ejecutivos.
4. El frontend dibuja la distribución de sentimiento, las respuestas (con los atributos de cada
   persona) y el panel de hallazgos.

## Requisitos y ejecución

```bash
cd research/personas/llm_app
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...     # tu clave de la API de Claude
python app.py                            # → http://localhost:5000/
```

Probar el prompt sin gastar tokens (no llama a la API):

```bash
python app.py --dry-run --n 5 --question "¿Comprarías un seguro por WhatsApp?"
```

## Archivos

| Archivo | Rol |
|---|---|
| `app.py` | Backend Flask: muestreo + prompt + llamada a Claude (structured outputs) + `/api/ask`. |
| `index.html` | Interfaz minimalista: pregunta libre, filtros de segmento, gráficos e insights. |
| `requirements.txt` | `anthropic`, `flask`. |

## Notas

- **Modelo:** `claude-opus-4-8` con *adaptive thinking* y `effort: medium`; salida restringida por
  JSON schema (no hace falta parsear texto a mano).
- **Tope de 25 personas** por consulta (latencia/costo); una sola llamada cubre todas.
- La clave de API vive **solo en el backend** (variable de entorno), nunca en el navegador.
- Datos sintéticos: personas inventadas calibradas a patrones reales; para prototipar y explorar
  hipótesis, no para sustituir una encuesta de mercado.
