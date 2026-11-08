#!/usr/bin/env bash
# Instala Mu en un Raspberry Pi (Raspberry Pi OS de 64 bits). Se corre una vez, con sudo.
#   sudo bash instalar.sh                 # Mu con Claude cuando hay internet; evidencia sin redactar cuando no
#   sudo bash instalar.sh --modelo-local  # además instala Ollama y un modelo local para redactar sin internet
# Se puede volver a correr: no borra datos ni la clave.
set -euo pipefail

REPO_URL="${MU_REPO_URL:-https://github.com/Rumipyramid/Machine_Learning.git}"
RAMA="${MU_RAMA:-claude/funny-hamilton-ppedc4}"
USUARIO="${SUDO_USER:-pi}"
CASA="$(getent passwd "$USUARIO" | cut -d: -f6)"
DESTINO="${MU_DESTINO:-$CASA/Machine_Learning}"
MODELO_LOCAL="${MU_MODELO_LOCAL:-llama3.2:3b}"
ENV=/etc/mu-pi.env

[ "$(id -u)" -eq 0 ] || { echo "Córrelo con sudo: sudo bash instalar.sh"; exit 1; }

echo "1/5 · Paquetes del sistema"
apt-get update -qq && apt-get install -y -qq git python3 curl >/dev/null

echo "2/5 · El repositorio en $DESTINO"
if [ -d "$DESTINO/.git" ]; then
  sudo -u "$USUARIO" git -C "$DESTINO" pull --ff-only
else
  # Si el repositorio es privado, git pedirá usuario y un token personal de GitHub (no la contraseña).
  sudo -u "$USUARIO" git clone --branch "$RAMA" --depth 1 "$REPO_URL" "$DESTINO"
fi

echo "3/5 · El cerebro (corpus de búsqueda y panel)"
sudo -u "$USUARIO" python3 "$DESTINO/research/grafo/preguntar/build_corpus.py"
sudo -u "$USUARIO" python3 "$DESTINO/research/grafo/mu.py" >/dev/null || echo "   (el panel no se pudo generar; Mu funciona igual)"

echo "4/5 · Configuración en $ENV"
if [ ! -f "$ENV" ]; then
  read -r -s -p "   Clave de la API de Anthropic (Enter para dejarla vacía y ponerla después): " CLAVE; echo
  umask 077
  cat > "$ENV" <<EOF
# Configuración de Mu. Solo la lee root y el servicio. Nunca la subas a ningún repositorio.
ANTHROPIC_API_KEY=$CLAVE
MU_MODELO=claude-opus-5-5
MU_MODELO_LOCAL=$MODELO_LOCAL
MU_PUERTO=8080
MU_DATOS=$CASA/.local/share/mu-pi
EOF
  chmod 600 "$ENV"
else
  echo "   Ya existe; no se toca. Para cambiar la clave: sudo nano $ENV && sudo systemctl restart mu"
fi

if [ "${1:-}" = "--modelo-local" ]; then
  echo "   · Modelo local: Ollama + $MODELO_LOCAL (baja unos 2 GB; tarda)"
  command -v ollama >/dev/null || curl -fsSL https://ollama.com/install.sh | sh
  systemctl enable --now ollama
  sleep 3
  ollama pull "$MODELO_LOCAL"
fi

echo "5/5 · Servicio y actualización nocturna"
cat > /etc/systemd/system/mu.service <<EOF
[Unit]
Description=Mu, el segundo cerebro, en la red de la casa
After=network-online.target
Wants=network-online.target

[Service]
User=$USUARIO
EnvironmentFile=$ENV
ExecStart=/usr/bin/python3 $DESTINO/mu-pi/servidor.py
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF
systemctl daemon-reload
systemctl enable mu >/dev/null 2>&1
systemctl restart mu

cat > /etc/cron.d/mu-actualizar <<EOF
# Cada noche a las 3:17 trae lo nuevo del cerebro si hay internet (si no, no hace nada).
17 3 * * * $USUARIO bash $DESTINO/mu-pi/actualizar.sh >> $CASA/.local/share/mu-pi/actualizar.log 2>&1
EOF
sudo -u "$USUARIO" mkdir -p "$CASA/.local/share/mu-pi"

IP="$(hostname -I | awk '{print $1}')"
echo
echo "Listo. Abre en cualquier navegador de la casa:  http://$IP:8080   (o http://$(hostname).local:8080)"
echo "Estado del servicio:  systemctl status mu    ·    Registro:  journalctl -u mu -f"
