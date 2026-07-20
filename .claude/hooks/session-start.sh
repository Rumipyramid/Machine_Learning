#!/bin/bash
set -euo pipefail

cd "$CLAUDE_PROJECT_DIR"

if [ ! -d .claude/skills ]; then
  exit 0
fi

DIRTY="$(git status --porcelain -- .claude/skills/ 2>/dev/null || true)"

if [ -n "$DIRTY" ]; then
  echo "⚠️  Hay cambios sin commitear en .claude/skills/:"
  echo "$DIRTY"
  echo ""
  echo "Si creaste o modificaste una skill en esta sesión, antes de cerrarla:"
  echo "  1. Commitea .claude/skills/<nombre>/SKILL.md (nunca debe quedar solo en el historial de la conversación)."
  echo "  2. Corre: /plugin marketplace update rumipyramid-machine-learning"
  echo "     para que quede disponible de inmediato en cualquier otra máquina/cuenta."
fi
