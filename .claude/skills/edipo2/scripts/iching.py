#!/usr/bin/env python3
"""Tirada simulada de I Ching (solo stdlib).

Genera 6 líneas de abajo hacia arriba, identifica el hexagrama en la secuencia
King Wen, sus líneas mutantes y el hexagrama resultante.

Métodos:
  - yarrow  (default): probabilidades del método de los tallos de milenrama
              6 = 1/16, 7 = 5/16, 8 = 7/16, 9 = 3/16
  - monedas: método de las tres monedas
              6 = 1/8, 7 = 3/8, 8 = 3/8, 9 = 1/8

Uso:
  python iching.py                 # tirada nueva, salida markdown
  python iching.py --json          # salida JSON
  python iching.py --metodo monedas
  python iching.py --seed 42       # reproducible (solo para pruebas)
"""

from __future__ import annotations

import argparse
import json
import os
import random
from pathlib import Path

REF = Path(__file__).resolve().parent.parent / "references" / "hexagramas.json"

# Tabla King Wen: fila = trigrama inferior, columna = trigrama superior.
# Orden de trigramas: Qián(111) Zhèn(100) Kǎn(010) Gèn(001) Kūn(000) Xùn(011) Lí(101) Duì(110)
_ORDEN = ["111", "100", "010", "001", "000", "011", "101", "110"]
_TABLA = [
    [1, 34, 5, 26, 11, 9, 14, 43],    # inferior Qián
    [25, 51, 3, 27, 24, 42, 21, 17],  # inferior Zhèn
    [6, 40, 29, 4, 7, 59, 64, 47],    # inferior Kǎn
    [33, 62, 39, 52, 15, 53, 56, 31], # inferior Gèn
    [12, 16, 8, 23, 2, 20, 35, 45],   # inferior Kūn
    [44, 32, 48, 18, 46, 57, 50, 28], # inferior Xùn
    [13, 55, 63, 22, 36, 37, 30, 49], # inferior Lí
    [10, 54, 60, 41, 19, 61, 38, 58], # inferior Duì
]

SIMBOLO = {6: "---x---", 7: "-------", 8: "--- ---", 9: "---o---"}
NOMBRE_LINEA = {
    6: "yin mutante (viejo)",
    7: "yang fijo (joven)",
    8: "yin fijo (joven)",
    9: "yang mutante (viejo)",
}


def _rng(seed: int | None) -> random.Random:
    if seed is not None:
        return random.Random(seed)
    # entropía del sistema: cada ejecución es una tirada distinta
    return random.Random(int.from_bytes(os.urandom(16), "big"))


def tirar_linea(rng: random.Random, metodo: str) -> int:
    if metodo == "monedas":
        # cara = 3, sello = 2; suma de tres monedas
        return sum(rng.choice((2, 3)) for _ in range(3))
    # yarrow
    x = rng.random()
    if x < 1 / 16:
        return 6
    if x < 1 / 16 + 5 / 16:
        return 7
    if x < 1 / 16 + 5 / 16 + 7 / 16:
        return 8
    return 9


def bits(lineas: list[int], mutadas: bool = False) -> str:
    """Devuelve los 6 bits de abajo hacia arriba ('1' = yang)."""
    out = []
    for v in lineas:
        if mutadas:
            v = {6: 7, 9: 8, 7: 7, 8: 8}[v]
        out.append("1" if v in (7, 9) else "0")
    return "".join(out)


def numero_king_wen(b: str) -> int:
    inferior = b[0:3]   # líneas 1-3, de abajo hacia arriba
    superior = b[3:6]   # líneas 4-6
    return _TABLA[_ORDEN.index(inferior)][_ORDEN.index(superior)]


def regla_de_lectura(mutantes: list[int], n_prim: int, n_res: int) -> str:
    k = len(mutantes)
    if k == 0:
        return ("Sin líneas mutantes: se lee solo el dictamen y la imagen del hexagrama. "
                "La situación es estable, no está en tránsito.")
    if k == 1:
        return (f"Una línea mutante ({mutantes[0]}ª): es el eje de la respuesta. "
                f"El hexagrama {n_res} muestra hacia dónde tiende.")
    if k == 2:
        return (f"Dos líneas mutantes ({', '.join(str(m) for m in mutantes)}ª): pesa más la superior, "
                f"pero se leen ambas como tensión entre dos movimientos.")
    if k == 3:
        return (f"Tres líneas mutantes ({', '.join(str(m) for m in mutantes)}ª): la del medio orienta; "
                f"el hexagrama resultante {n_res} pesa tanto como el primario.")
    if k in (4, 5):
        return (f"{k} líneas mutantes: la situación se está dando vuelta. Se lee sobre todo el hexagrama "
                f"resultante ({n_res}) y, dentro del primario, las líneas que NO mutan.")
    return ("Las seis líneas mutan: caso especial. Se lee el hexagrama resultante y, si el primario es "
            "1 o 2, su línea de uso adicional ('todas las líneas').")


def tirada(metodo: str = "yarrow", seed: int | None = None) -> dict:
    rng = _rng(seed)
    lineas = [tirar_linea(rng, metodo) for _ in range(6)]
    b_prim = bits(lineas)
    b_res = bits(lineas, mutadas=True)
    n_prim = numero_king_wen(b_prim)
    n_res = numero_king_wen(b_res)
    mutantes = [i + 1 for i, v in enumerate(lineas) if v in (6, 9)]

    ref = json.loads(REF.read_text(encoding="utf-8"))
    hexs, trigs, pos = ref["hexagramas"], ref["trigramas"], ref["posiciones"]

    def describe(n: int, b: str) -> dict:
        d = dict(hexs[str(n)])
        d["numero"] = n
        d["binario_abajo_arriba"] = b
        d["trigrama_inferior"] = trigs[b[0:3]]
        d["trigrama_superior"] = trigs[b[3:6]]
        return d

    return {
        "sistema": "I Ching",
        "metodo": metodo,
        "lineas": [
            {
                "posicion": i + 1,
                "valor": v,
                "tipo": NOMBRE_LINEA[v],
                "simbolo": SIMBOLO[v],
                "muta": v in (6, 9),
                "sentido_de_la_posicion": pos[str(i + 1)],
            }
            for i, v in enumerate(lineas)
        ],
        "hexagrama_primario": describe(n_prim, b_prim),
        "lineas_mutantes": mutantes,
        "hexagrama_resultante": describe(n_res, b_res) if mutantes else None,
        "regla_de_lectura": regla_de_lectura(mutantes, n_prim, n_res),
    }


def a_markdown(t: dict) -> str:
    p = t["hexagrama_primario"]
    L = ["## I Ching — tirada simulada", "", f"*Método:* {t['metodo']}", "", "```"]
    for ln in reversed(t["lineas"]):  # se dibuja de arriba hacia abajo
        marca = "  ←muta" if ln["muta"] else ""
        L.append(f"{ln['posicion']}  {ln['simbolo']}  ({ln['valor']}){marca}")
    L += ["```", ""]
    L.append(f"**Hexagrama primario {p['numero']} · {p['chino']} {p['pinyin']} — {p['nombre']}**")
    L.append(f"- Trigramas: {p['trigrama_superior']['imagen']} sobre {p['trigrama_inferior']['imagen']} "
             f"({p['trigrama_superior']['nombre']} / {p['trigrama_inferior']['nombre']})")
    L.append(f"- Clave: {p['clave']}")
    L.append(f"- Dictamen: {p['dictamen']}")
    L.append(f"- Imagen: {p['imagen']}")
    L.append("")
    if t["lineas_mutantes"]:
        L.append(f"**Líneas mutantes:** {', '.join(str(m) for m in t['lineas_mutantes'])}")
        for m in t["lineas_mutantes"]:
            ln = t["lineas"][m - 1]
            L.append(f"- Línea {m} ({ln['tipo']}): {ln['sentido_de_la_posicion']}")
        r = t["hexagrama_resultante"]
        L.append("")
        L.append(f"**Hexagrama resultante {r['numero']} · {r['chino']} {r['pinyin']} — {r['nombre']}**")
        L.append(f"- Clave: {r['clave']}")
        L.append(f"- Dictamen: {r['dictamen']}")
    else:
        L.append("**Sin líneas mutantes.**")
    L += ["", f"*Regla de lectura:* {t['regla_de_lectura']}"]
    return "\n".join(L)


def main() -> None:
    ap = argparse.ArgumentParser(description="Tirada simulada de I Ching")
    ap.add_argument("--metodo", choices=("yarrow", "monedas"), default="yarrow")
    ap.add_argument("--seed", type=int, default=None, help="solo para pruebas reproducibles")
    ap.add_argument("--json", action="store_true", help="salida JSON en vez de markdown")
    a = ap.parse_args()
    t = tirada(a.metodo, a.seed)
    print(json.dumps(t, ensure_ascii=False, indent=2) if a.json else a_markdown(t))


if __name__ == "__main__":
    main()
