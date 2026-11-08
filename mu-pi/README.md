# Mu en un Raspberry Pi

Mu vive en el Pi y se usa desde cualquier navegador de la casa (celular, laptop). Elige solo cómo responder en cada pregunta:

| Situación | Quién redacta | Calidad |
|---|---|---|
| Hay internet y clave de la API | Claude (Opus 5.5 por defecto), en dos pasos: plan y redacción | La versión completa |
| Sin internet, con modelo local instalado | Un modelo pequeño en el propio Pi (Llama 3.2 3B por defecto) | Más lento (1-3 minutos) y menos fino; puede citar mal |
| Sin internet y sin modelo local | Nadie: Mu muestra la evidencia ordenada | Fragmentos por nodo, fuentes por solidez, disputas, lecciones |

**Siempre funcionan, con o sin internet:** la búsqueda en el cerebro, la balanza del Criterio por reglas, el registro de temas y el "¿Te sirvió?". Se guardan en el Pi (`~/.local/share/mu-pi/`). El panel del cerebro está en `http://<pi>:8080/panel`.

## Qué necesitas

- Raspberry Pi 4 o 5 con Raspberry Pi OS de 64 bits. Sin modelo local basta con 2 GB de RAM.
- Para el modelo local: Pi 5 con 8 GB y unos 3 GB libres en la tarjeta.
- Una clave de la API de Anthropic (console.anthropic.com). Cada pregunta hace 3-4 llamadas con varios miles de palabras de evidencia cada una; mira el costo real de las primeras preguntas en la consola antes de usarlo mucho. Sonnet 5.5 sale más barato (`MU_MODELO=claude-sonnet-5-5`).

## Instalar

```bash
git clone --branch claude/funny-hamilton-ppedc4 https://github.com/Rumipyramid/Machine_Learning.git
sudo bash Machine_Learning/mu-pi/instalar.sh                 # sin modelo local
sudo bash Machine_Learning/mu-pi/instalar.sh --modelo-local  # con modelo local (baja ~2 GB)
```

Si el repositorio es privado, git pide tu usuario de GitHub y un token personal en vez de la contraseña.
El instalador pide la clave de la API y la guarda en `/etc/mu-pi.env` (solo la lee root y el servicio). Al terminar muestra la dirección, por ejemplo `http://192.168.1.20:8080`.

## Mantenerlo

- Cada noche a las 3:17, si hay internet, `actualizar.sh` trae lo nuevo del cerebro y regenera el corpus. A mano: `bash ~/Machine_Learning/mu-pi/actualizar.sh`.
- Cambiar la clave o el modelo: `sudo nano /etc/mu-pi.env` y luego `sudo systemctl restart mu`.
- Ver qué pasa: `systemctl status mu` · `journalctl -u mu -f` · `http://<pi>:8080/api/estado`.

## Seguridad

- La clave vive solo en el Pi. El navegador nunca la ve: el Pi hace de intermediario.
- Cualquiera conectado a tu wifi puede usar Mu, y con eso gastar tu clave. **No abras el puerto 8080 en el router.** Para usarlo fuera de casa, usa una VPN como Tailscale.
- Pon un tope de gasto mensual en la consola de Anthropic.

## Límites

- Los datos del Pi (consultas, temas, "¿Te sirvió?") están separados de los del artefacto de claude.ai. Tienen el mismo formato: `python3 research/grafo/impacto.py --db ~/.local/share/mu-pi` los cuenta, pero esa foto reemplaza a la del artefacto en `impacto.json`.
- El modelo local no razona como Claude. Úsalo para salir del paso, no para decisiones.
- Se probó en una computadora con servidores simulados de Anthropic y de Ollama: los tres modos, el registro y el panel. El instalador no se ha probado todavía en un Pi real.

## Archivos

- `servidor.py`: el servidor (solo Python estándar). Sirve la página, hace de puente con Claude u Ollama y guarda los datos.
- `shim.js`: conecta la página con el servidor del Pi.
- `instalar.sh` y `actualizar.sh`: instalación y actualización nocturna.
