#!/usr/bin/env bash
#
# Activa "mi Claude" en una máquina/cuenta de Claude Code nueva (laptop
# corporativa, laptop personal, sandbox en la nube) sin tener que recordar ni
# retipear a mano los pasos manuales cada vez:
#
#   /plugin marketplace add Rumipyramid/Machine_Learning
#   /plugin install rumipyramid-skills@rumipyramid-machine-learning
#
# El repo es público, así que esto solo jala definiciones de skills (texto
# público en GitHub) — no requiere ni expone credenciales personales, y es
# seguro de correr también en una cuenta corporativa.
#
# Idempotente: si el marketplace o el plugin ya están, no hace nada.
#
# Uso:
#   scripts/bootstrap_claude_code.sh

set -euo pipefail

MARKETPLACE="rumipyramid-machine-learning"
MARKETPLACE_SOURCE="Rumipyramid/Machine_Learning"
PLUGIN="rumipyramid-skills"

if ! command -v claude >/dev/null 2>&1; then
  echo "Error: no encuentro el CLI 'claude' en el PATH. Instala Claude Code primero." >&2
  exit 1
fi

if claude plugin marketplace list --json 2>/dev/null | jq -e --arg name "$MARKETPLACE" \
  'any(.[]; .name == $name)' >/dev/null 2>&1; then
  echo "Marketplace '$MARKETPLACE' ya está agregado."
else
  echo "Agregando marketplace '$MARKETPLACE_SOURCE'..."
  claude plugin marketplace add "$MARKETPLACE_SOURCE"
fi

if claude plugin list --json 2>/dev/null | jq -e --arg name "$PLUGIN" \
  'any(.[]; .name == $name)' >/dev/null 2>&1; then
  echo "Plugin '$PLUGIN' ya está instalado."
else
  echo "Instalando plugin '$PLUGIN@$MARKETPLACE'..."
  claude plugin install "$PLUGIN@$MARKETPLACE"
fi

echo "Listo. Skills disponibles: /seeker /gossip /marketer /trinidad /lapuerta /beholder /actualizar /cronista /codice /many-brains /rimac-slides /presentaciones-rimac /cerrajero /contexto-peruano"
