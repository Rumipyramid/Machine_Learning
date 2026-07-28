#!/usr/bin/env python3
"""Tirada simulada de Tarot de Marsella con clave junguiana (solo stdlib).

Baraja las 78 cartas (22 mayores + 56 menores con nomenclatura marsellesa) y
reparte una tirada. Los menores se componen en el momento: número × palo, según
la numerología marsellesa, con la función psíquica junguiana del palo.

Uso:
  python tarot.py                       # tirada de 3, markdown
  python tarot.py --tirada cruz --json
  python tarot.py --tirada arbol
  python tarot.py --solo-mayores        # baraja solo los 22 arcanos mayores
  python tarot.py --invertidas          # permite cartas invertidas (no es canon marsellés)
  python tarot.py --seed 42             # reproducible (solo para pruebas)
"""

from __future__ import annotations

import argparse
import json
import os
import random
from pathlib import Path

REF = Path(__file__).resolve().parent.parent / "references" / "tarot_marsella.json"
PALOS = ("Bastos", "Copas", "Espadas", "Oros")
FIGURAS = ("Valet", "Caballero", "Reina", "Rey")
ROMANOS = {
    0: "sin número", 1: "I", 2: "II", 3: "III", 4: "IIII", 5: "V", 6: "VI", 7: "VII",
    8: "VIII", 9: "VIIII", 10: "X", 11: "XI", 12: "XII", 13: "XIII",
    14: "XIIII", 15: "XV", 16: "XVI", 17: "XVII", 18: "XVIII", 19: "XVIIII",
    20: "XX", 21: "XXI",
}


def _rng(seed: int | None) -> random.Random:
    if seed is not None:
        return random.Random(seed)
    return random.Random(int.from_bytes(os.urandom(16), "big"))


def mazo(solo_mayores: bool = False) -> list[tuple]:
    cartas = [("mayor", n) for n in range(22)]
    if not solo_mayores:
        for palo in PALOS:
            for n in range(1, 11):
                cartas.append(("menor", (n, palo)))
            for f in FIGURAS:
                cartas.append(("figura", (f, palo)))
    return cartas


def describe(carta: tuple, ref: dict, invertida: bool) -> dict:
    tipo, dato = carta
    d = {"tipo": tipo, "invertida": invertida}
    if tipo == "mayor":
        m = ref["mayores"][str(dato)]
        d.update(
            numero=dato,
            romano=ROMANOS[dato],
            nombre=f"{ROMANOS[dato]} · {m['nombre']}" if dato else m["nombre"],
            carta=m["nombre"],
            arquetipo=m["arquetipo"],
            eje=m["eje"],
            luz=m["luz"],
            sombra=m["sombra"],
            individuacion=m["individuacion"],
        )
    elif tipo == "menor":
        n, palo = dato
        p = ref["palos"][palo]
        d.update(
            nombre=f"{n} de {palo}",
            carta=f"{n} de {palo}",
            palo=palo,
            numero=n,
            elemento=p["elemento"],
            funcion_jung=p["funcion_jung"],
            ambito=p["ambito"],
            numerologia=ref["numeros"][str(n)],
            lectura=f"{ref['numeros'][str(n)]} Aplicado a {p['ambito']} (función {p['funcion_jung']}, {p['elemento']}).",
        )
    else:
        fig, palo = dato
        f = ref["figuras"][fig]
        p = ref["palos"][palo]
        d.update(
            nombre=f"{fig} de {palo}",
            carta=f"{fig} de {palo}",
            palo=palo,
            figura=fig,
            elemento=p["elemento"],
            funcion_jung=p["funcion_jung"],
            ambito=p["ambito"],
            rol=f["rol"],
            movimiento=f["movimiento"],
            lectura=f"{f['rol'].capitalize()}: {f['movimiento']}. Aplicado a {p['ambito']}. "
                    f"Clave junguiana: {f['jung']} (función {p['funcion_jung']}).",
        )
    if invertida:
        d["nota_inversion"] = ("Carta invertida: en clave junguiana léela como contenido reprimido o "
                               "no integrado — la energía existe pero opera desde la sombra.")
    return d


def tirada(nombre_tirada: str = "tres", solo_mayores: bool = False,
           invertidas: bool = False, seed: int | None = None) -> dict:
    ref = json.loads(REF.read_text(encoding="utf-8"))
    posiciones = ref["tiradas"][nombre_tirada]
    rng = _rng(seed)
    baraja = mazo(solo_mayores)
    rng.shuffle(baraja)
    sacadas = baraja[: len(posiciones)]

    cartas = []
    for pos, c in zip(posiciones, sacadas):
        inv = invertidas and rng.random() < 0.5
        d = describe(c, ref, inv)
        d["posicion"] = pos
        cartas.append(d)

    mayores = sum(1 for c in cartas if c["tipo"] == "mayor")
    palos = [c.get("palo") for c in cartas if c.get("palo")]
    # solo hay dominante si un palo se repite y no está empatado con otro
    conteo = {p: palos.count(p) for p in set(palos)}
    dominante = None
    if conteo:
        top = max(conteo.values())
        empatados = [p for p, c in conteo.items() if c == top]
        dominante = empatados[0] if top > 1 and len(empatados) == 1 else None

    return {
        "sistema": "Tarot de Marsella (marco junguiano)",
        "tirada": nombre_tirada,
        "mazo": "solo arcanos mayores (22)" if solo_mayores else "78 cartas",
        "inversiones": invertidas,
        "cartas": cartas,
        "dinamica": {
            "arcanos_mayores": mayores,
            "proporcion_mayores": f"{mayores}/{len(cartas)}",
            "palo_dominante": dominante,
            "nota": ("Muchos mayores = el asunto toca material arquetípico/colectivo, no solo biográfico. "
                     "Predominio de un palo = una función psíquica está cargando el proceso; "
                     "el palo ausente suele señalar la función inferior (lo no atendido)."),
            "palos_ausentes": [p for p in PALOS if p not in palos],
        },
    }


def a_markdown(t: dict) -> str:
    L = [f"## Tarot de Marsella — tirada simulada ({t['tirada']})", "",
         f"*Mazo:* {t['mazo']}{' · con inversiones' if t['inversiones'] else ''}", ""]
    for i, c in enumerate(t["cartas"], 1):
        inv = " (invertida)" if c["invertida"] else ""
        L.append(f"**{i}. {c['posicion']} → {c['nombre']}{inv}**")
        if c["tipo"] == "mayor":
            L.append(f"- Arquetipo: {c['arquetipo']}")
            L.append(f"- Eje: {c['eje']}")
            L.append(f"- Luz: {c['luz']}")
            L.append(f"- Sombra: {c['sombra']}")
            L.append(f"- Individuación: {c['individuacion']}")
        else:
            L.append(f"- Palo: {c['palo']} · {c['elemento']} · función {c['funcion_jung']}")
            L.append(f"- Lectura: {c['lectura']}")
        if c["invertida"]:
            L.append(f"- {c['nota_inversion']}")
        L.append("")
    d = t["dinamica"]
    L.append(f"*Dinámica de la tirada:* {d['proporcion_mayores']} arcanos mayores · "
             f"palo dominante: {d['palo_dominante'] or '—'} · "
             f"palos ausentes: {', '.join(d['palos_ausentes']) or 'ninguno'}")
    L.append(f"*Nota:* {d['nota']}")
    return "\n".join(L)


def main() -> None:
    ref_tiradas = json.loads(REF.read_text(encoding="utf-8"))["tiradas"]
    ap = argparse.ArgumentParser(description="Tirada simulada de Tarot de Marsella")
    ap.add_argument("--tirada", choices=tuple(ref_tiradas), default="tres")
    ap.add_argument("--solo-mayores", action="store_true")
    ap.add_argument("--invertidas", action="store_true")
    ap.add_argument("--seed", type=int, default=None)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    t = tirada(a.tirada, a.solo_mayores, a.invertidas, a.seed)
    print(json.dumps(t, ensure_ascii=False, indent=2) if a.json else a_markdown(t))


if __name__ == "__main__":
    main()
