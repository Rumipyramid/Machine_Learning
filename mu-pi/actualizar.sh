#!/usr/bin/env bash
# Trae lo nuevo del cerebro y regenera el corpus y el panel. Sin internet no hace nada y Mu sigue con lo que tiene.
# Lo corre el cron cada noche; también se puede correr a mano:  bash mu-pi/actualizar.sh
set -uo pipefail
RAIZ="$(cd "$(dirname "$0")/.." && pwd)"
echo "== $(date '+%F %T') =="
if ! git -C "$RAIZ" pull --ff-only -q; then
  echo "Sin internet o sin acceso al repositorio: se mantiene el cerebro actual."
  exit 0
fi
python3 "$RAIZ/research/grafo/preguntar/build_corpus.py" || { echo "Falló el corpus: se mantiene el anterior."; exit 0; }
python3 "$RAIZ/research/grafo/mu.py" >/dev/null 2>&1 || echo "El panel no se regeneró."
echo "Cerebro al día: $(git -C "$RAIZ" log -1 --format='%h · %cs · %s')"
# El servidor lee el corpus en cada pedido: no hace falta reiniciarlo.
