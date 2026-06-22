#!/usr/bin/env bash
#
# Empaqueta el skill Beholder como un repositorio Git independiente, listo para
# publicar en GitHub. NO modifica este repo: copia la carpeta del skill a un
# destino nuevo, inicializa git y deja el primer commit hecho.
#
# Uso:
#   scripts/publish_beholder_standalone.sh [destino]
# Ejemplo:
#   scripts/publish_beholder_standalone.sh ~/beholder
#
# Como la raíz del repo standalone es el contenido de la carpeta del skill,
# luego se puede instalar con:
#   git clone <url> ~/.claude/skills/beholder
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$REPO_ROOT/.claude/skills/beholder"
DEST="${1:-$REPO_ROOT/dist/beholder}"

if [ ! -f "$SRC/SKILL.md" ]; then
  echo "No encuentro el skill en: $SRC" >&2
  exit 1
fi
if [ -e "$DEST" ]; then
  echo "El destino ya existe: $DEST (bórralo o elige otro)" >&2
  exit 1
fi

mkdir -p "$DEST"
# Copia el contenido del skill (incluye archivos ocultos como .gitignore)
cp -a "$SRC/." "$DEST/"

cd "$DEST"
git init -q
git add .
git commit -q -m "Initial commit: Beholder skill (Jira-style board + token economy)"

echo "✅ Repo standalone listo en: $DEST"
echo ""
echo "Siguientes pasos:"
echo "  1) Crea un repositorio vacío en GitHub (p. ej. 'beholder')."
echo "  2) git -C \"$DEST\" remote add origin git@github.com:<owner>/beholder.git"
echo "  3) git -C \"$DEST\" branch -M main && git -C \"$DEST\" push -u origin main"
echo ""
echo "Instalación desde el repo publicado:"
echo "  git clone https://github.com/<owner>/beholder ~/.claude/skills/beholder"
