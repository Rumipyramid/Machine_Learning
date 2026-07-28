#!/usr/bin/env python3
"""Posiciones planetarias aproximadas para una fecha/hora, geocéntricas y tropicales.

Pensado para Lima, Perú (UTC-5, 12°02'S 77°02'W) — configurable por CLI.
Solo stdlib: implementa elementos keplerianos aproximados de la JPL
("Keplerian Elements for Approximate Positions of the Major Planets", válidos
1800-2050) para Mercurio..Plutón, la fórmula de baja precisión del Astronomical
Almanac para la Luna, el nodo lunar medio, y Ascendente/Medio Cielo por tiempo
sidéreo local.

Precisión esperada: planetas ~0.1° (exteriores algo más), Luna ~0.3°, Sol ~0.01°.
Suficiente para signo, casa (signos enteros) y aspectos con orbe amplio; NO es
una efeméride de precisión. Si un cuerpo cae a menos de 1° de un cambio de signo
el script lo advierte explícitamente.

Uso:
  python astro.py                      # ahora, hora de Lima
  python astro.py --fecha 2026-07-28 --hora 19:30
  python astro.py --json
  python astro.py --lat -12.0464 --lon -77.0428 --tz -5
"""

from __future__ import annotations

import argparse
import json
import math
from datetime import datetime, timedelta, timezone

RAD = math.pi / 180.0

SIGNOS = ["Aries", "Tauro", "Géminis", "Cáncer", "Leo", "Virgo",
          "Libra", "Escorpio", "Sagitario", "Capricornio", "Acuario", "Piscis"]
ELEMENTO = {"Aries": "Fuego", "Leo": "Fuego", "Sagitario": "Fuego",
            "Tauro": "Tierra", "Virgo": "Tierra", "Capricornio": "Tierra",
            "Géminis": "Aire", "Libra": "Aire", "Acuario": "Aire",
            "Cáncer": "Agua", "Escorpio": "Agua", "Piscis": "Agua"}
MODALIDAD = {"Aries": "Cardinal", "Cáncer": "Cardinal", "Libra": "Cardinal", "Capricornio": "Cardinal",
             "Tauro": "Fijo", "Leo": "Fijo", "Escorpio": "Fijo", "Acuario": "Fijo",
             "Géminis": "Mutable", "Virgo": "Mutable", "Sagitario": "Mutable", "Piscis": "Mutable"}

CASAS_SIGNIFICADO = {
    1: "identidad, cuerpo, cómo apareces", 2: "recursos, dinero propio, valor",
    3: "entorno cercano, palabra, aprendizaje", 4: "casa, origen, raíz, familia",
    5: "creación, juego, hijos, deseo", 6: "trabajo cotidiano, salud, servicio",
    7: "pareja, socios, el otro", 8: "crisis, recursos compartidos, muerte y transformación",
    9: "sentido, viajes, estudio mayor, creencias", 10: "vocación, carrera, exposición pública",
    11: "amigos, redes, proyectos colectivos", 12: "inconsciente, retiro, lo que opera oculto",
}

# a, e, I, L, long.peri, long.node  +  tasas por siglo juliano (JPL, 1800-2050)
PLANETAS = {
    "Mercurio": ((0.38709927, 0.20563593, 7.00497902, 252.25032350, 77.45779628, 48.33076593),
                 (0.00000037, 0.00001906, -0.00594749, 149472.67411175, 0.16047689, -0.12534081)),
    "Venus":    ((0.72333566, 0.00677672, 3.39467605, 181.97909950, 131.60246718, 76.67984255),
                 (0.00000390, -0.00004107, -0.00078890, 58517.81538729, 0.00268329, -0.27769418)),
    "Tierra":   ((1.00000261, 0.01671123, -0.00001531, 100.46457166, 102.93768193, 0.0),
                 (0.00000562, -0.00004392, -0.01294668, 35999.37244981, 0.32327364, 0.0)),
    "Marte":    ((1.52371034, 0.09339410, 1.84969142, -4.55343205, -23.94362959, 49.55953891),
                 (0.00001847, 0.00007882, -0.00813131, 19140.30268499, 0.44441088, -0.29257343)),
    "Júpiter":  ((5.20288700, 0.04838624, 1.30439695, 34.39644051, 14.72847983, 100.47390909),
                 (-0.00011607, -0.00013253, -0.00183714, 3034.74612775, 0.21252668, 0.20469106)),
    "Saturno":  ((9.53667594, 0.05386179, 2.48599187, 49.95424423, 92.59887831, 113.66242448),
                 (-0.00125060, -0.00050991, 0.00193609, 1222.49362201, -0.41897216, -0.28867794)),
    "Urano":    ((19.18916464, 0.04725744, 0.77263783, 313.23810451, 170.95427630, 74.01692503),
                 (-0.00196176, -0.00004397, -0.00242939, 428.48202785, 0.40805281, 0.04240589)),
    "Neptuno":  ((30.06992276, 0.00859048, 1.77004347, -55.12002969, 44.96476227, 131.78422574),
                 (0.00026291, 0.00005105, 0.00035372, 218.45945325, -0.32241464, -0.00508664)),
    "Plutón":   ((39.48211675, 0.24882730, 17.14001206, 238.92903833, 224.06891629, 110.30393684),
                 (-0.00031596, 0.00005170, 0.00004818, 145.20780515, -0.04062942, -0.01183482)),
}

REGENCIAS = {
    "Sol": "Leo", "Luna": "Cáncer", "Mercurio": "Géminis y Virgo", "Venus": "Tauro y Libra",
    "Marte": "Aries (y Escorpio en tradición)", "Júpiter": "Sagitario (y Piscis en tradición)",
    "Saturno": "Capricornio (y Acuario en tradición)", "Urano": "Acuario (moderna)",
    "Neptuno": "Piscis (moderna)", "Plutón": "Escorpio (moderna)",
}

ASPECTOS = [("Conjunción", 0.0, 8.0), ("Sextil", 60.0, 4.0), ("Cuadratura", 90.0, 6.0),
            ("Trígono", 120.0, 6.0), ("Oposición", 180.0, 8.0)]
LUMINARIAS = ("Sol", "Luna")


def norm360(x: float) -> float:
    return x % 360.0


def julian_day(dt_utc: datetime) -> float:
    y, m = dt_utc.year, dt_utc.month
    d = (dt_utc.day + dt_utc.hour / 24 + dt_utc.minute / 1440
         + dt_utc.second / 86400)
    if m <= 2:
        y -= 1
        m += 12
    a = y // 100
    b = 2 - a + a // 4
    return math.floor(365.25 * (y + 4716)) + math.floor(30.6001 * (m + 1)) + d + b - 1524.5


def _kepler(M: float, e: float) -> float:
    """Resuelve la ecuación de Kepler. M en grados, devuelve E en grados."""
    M = ((M + 180) % 360) - 180
    E = M + (180 / math.pi) * e * math.sin(M * RAD)
    for _ in range(60):
        dM = M - (E - (180 / math.pi) * e * math.sin(E * RAD))
        dE = dM / (1 - e * math.cos(E * RAD))
        E += dE
        if abs(dE) < 1e-9:
            break
    return E


def heliocentrico(nombre: str, T: float) -> tuple[float, float, float]:
    (a0, e0, I0, L0, w0, O0), (da, de, dI, dL, dw, dO) = PLANETAS[nombre]
    a = a0 + da * T
    e = e0 + de * T
    I = (I0 + dI * T) * RAD
    L = L0 + dL * T
    w = w0 + dw * T           # longitud del perihelio
    O = (O0 + dO * T) * RAD   # longitud del nodo ascendente
    E = _kepler(L - w, e) * RAD
    # coordenadas en el plano orbital
    xp = a * (math.cos(E) - e)
    yp = a * math.sqrt(1 - e * e) * math.sin(E)
    argp = (w - (O0 + dO * T)) * RAD  # argumento del perihelio
    cw, sw = math.cos(argp), math.sin(argp)
    cO, sO = math.cos(O), math.sin(O)
    cI, sI = math.cos(I), math.sin(I)
    x = (cw * cO - sw * sO * cI) * xp + (-sw * cO - cw * sO * cI) * yp
    y = (cw * sO + sw * cO * cI) * xp + (-sw * sO + cw * cO * cI) * yp
    z = (sw * sI) * xp + (cw * sI) * yp
    return x, y, z


def precesion(T: float) -> float:
    """De longitud eclíptica J2000 a eclíptica de la fecha (precesión general)."""
    return 1.396971 * T + 0.0003086 * T * T


def longitud_planeta(nombre: str, jd: float) -> float:
    T = (jd - 2451545.0) / 36525.0
    xe, ye, ze = heliocentrico("Tierra", T)
    if nombre == "Sol":
        x, y = -xe, -ye
    else:
        xp, yp, zp = heliocentrico(nombre, T)
        x, y = xp - xe, yp - ye
    return norm360(math.degrees(math.atan2(y, x)) + precesion(T))


def longitud_luna(jd: float) -> float:
    """Fórmula de baja precisión del Astronomical Almanac (~0.3°). Ya es de la fecha."""
    T = (jd - 2451545.0) / 36525.0
    lam = (218.32 + 481267.8813 * T
           + 6.29 * math.sin((134.9 + 477198.85 * T) * RAD)
           - 1.27 * math.sin((259.2 - 413335.38 * T) * RAD)
           + 0.66 * math.sin((235.7 + 890534.23 * T) * RAD)
           + 0.21 * math.sin((269.9 + 954397.70 * T) * RAD)
           - 0.19 * math.sin((357.5 + 35999.05 * T) * RAD)
           - 0.11 * math.sin((186.6 + 966404.05 * T) * RAD))
    return norm360(lam)


def nodo_lunar_medio(jd: float) -> float:
    T = (jd - 2451545.0) / 36525.0
    return norm360(125.0445479 - 1934.1362891 * T + 0.0020754 * T * T)


def obliquidad(jd: float) -> float:
    T = (jd - 2451545.0) / 36525.0
    return 23.439291 - 0.0130042 * T - 1.64e-7 * T * T


def gmst(jd: float) -> float:
    T = (jd - 2451545.0) / 36525.0
    return norm360(280.46061837 + 360.98564736629 * (jd - 2451545.0)
                   + 0.000387933 * T * T - T ** 3 / 38710000.0)


def asc_mc(jd: float, lat: float, lon: float) -> tuple[float, float]:
    lst = norm360(gmst(jd) + lon)          # lon este positiva
    eps = obliquidad(jd) * RAD
    t = lst * RAD
    mc = norm360(math.degrees(math.atan2(math.sin(t), math.cos(t) * math.cos(eps))))
    asc = math.degrees(math.atan2(
        math.cos(t),
        -(math.sin(t) * math.cos(eps) + math.tan(lat * RAD) * math.sin(eps))))
    asc = norm360(asc)
    if not (0 < norm360(asc - mc) < 180):   # el Asc va delante del MC
        asc = norm360(asc + 180)
    return asc, mc


def a_signo(lon: float) -> dict:
    lon = norm360(lon)
    i = int(lon // 30)
    grado = lon - i * 30
    signo = SIGNOS[i]
    return {
        "longitud": round(lon, 3),
        "signo": signo,
        "grado": round(grado, 2),
        "posicion": f"{int(grado)}°{int((grado % 1) * 60):02d}' {signo}",
        "elemento": ELEMENTO[signo],
        "modalidad": MODALIDAD[signo],
        "cerca_de_cambio_de_signo": grado < 1.0 or grado > 29.0,
    }


def fase_lunar(jd: float) -> dict:
    d = norm360(longitud_luna(jd) - longitud_planeta("Sol", jd))
    nombres = [(22.5, "Luna nueva"), (67.5, "Creciente iluminante"), (112.5, "Cuarto creciente"),
               (157.5, "Gibosa creciente"), (202.5, "Luna llena"), (247.5, "Gibosa menguante"),
               (292.5, "Cuarto menguante"), (337.5, "Balsámica (menguante final)"), (360.1, "Luna nueva")]
    nombre = next(n for lim, n in nombres if d < lim)
    return {
        "elongacion_sol_luna": round(d, 2),
        "fase": nombre,
        "iluminacion_pct": round(50 * (1 - math.cos(d * RAD)), 1),
        "ciclo": "creciente (siembra, apertura)" if d < 180 else "menguante (cosecha, soltar)",
    }


def aspectos(cuerpos: dict) -> list[dict]:
    out = []
    nombres = list(cuerpos)
    for i, a in enumerate(nombres):
        for b in nombres[i + 1:]:
            sep = abs(cuerpos[a]["longitud"] - cuerpos[b]["longitud"]) % 360
            if sep > 180:
                sep = 360 - sep
            for nom, ang, orbe in ASPECTOS:
                permitido = orbe + (2 if a in LUMINARIAS or b in LUMINARIAS else 0)
                if abs(sep - ang) <= permitido:
                    out.append({
                        "cuerpos": [a, b],
                        "aspecto": nom,
                        "separacion": round(sep, 2),
                        "orbe": round(abs(sep - ang), 2),
                        "exacto": abs(sep - ang) < 1.0,
                    })
                    break
    return sorted(out, key=lambda x: x["orbe"])


def carta(dt_local: datetime, tz: float, lat: float, lon: float) -> dict:
    dt_utc = dt_local - timedelta(hours=tz)
    jd = julian_day(dt_utc)

    cuerpos: dict[str, dict] = {}
    for nombre in ["Sol", "Luna", "Mercurio", "Venus", "Marte", "Júpiter",
                   "Saturno", "Urano", "Neptuno", "Plutón"]:
        if nombre == "Luna":
            lon_hoy, lon_man = longitud_luna(jd), longitud_luna(jd + 1)
        else:
            lon_hoy, lon_man = longitud_planeta(nombre, jd), longitud_planeta(nombre, jd + 1)
        delta = ((lon_man - lon_hoy + 180) % 360) - 180
        d = a_signo(lon_hoy)
        d["retrogrado"] = delta < 0
        d["velocidad_grados_dia"] = round(delta, 4)
        d["rige"] = REGENCIAS[nombre]
        cuerpos[nombre] = d

    nodo = a_signo(nodo_lunar_medio(jd))
    asc_l, mc_l = asc_mc(jd, lat, lon)
    asc, mc = a_signo(asc_l), a_signo(mc_l)

    # casas por signos enteros a partir del signo del Ascendente
    i_asc = SIGNOS.index(asc["signo"])
    casas = []
    for n in range(1, 13):
        signo = SIGNOS[(i_asc + n - 1) % 12]
        ocupantes = [c for c, v in cuerpos.items() if v["signo"] == signo]
        casas.append({"casa": n, "signo": signo, "asunto": CASAS_SIGNIFICADO[n], "ocupantes": ocupantes})

    for nombre, v in cuerpos.items():
        v["casa"] = (SIGNOS.index(v["signo"]) - i_asc) % 12 + 1

    avisos = [f"{c} está a menos de 1° de cambiar de signo ({v['posicion']}): "
              f"verificar con efeméride si el matiz importa."
              for c, v in cuerpos.items() if v["cerca_de_cambio_de_signo"]]

    return {
        "sistema": "Astrología tropical (posiciones aproximadas calculadas en local)",
        "momento": {
            "local": dt_local.strftime("%Y-%m-%d %H:%M"),
            "utc": dt_utc.strftime("%Y-%m-%d %H:%M"),
            "tz": f"UTC{tz:+g}",
            "lat": lat, "lon": lon,
            "jd": round(jd, 5),
        },
        "cuerpos": cuerpos,
        "nodo_lunar_norte": nodo,
        "ascendente": asc,
        "medio_cielo": mc,
        "casas": casas,
        "fase_lunar": fase_lunar(jd),
        "aspectos": aspectos(cuerpos),
        "retrogrados": [c for c, v in cuerpos.items() if v["retrogrado"]],
        "balance_elementos": {e: sum(1 for v in cuerpos.values() if v["elemento"] == e)
                              for e in ("Fuego", "Tierra", "Aire", "Agua")},
        "balance_modalidades": {m: sum(1 for v in cuerpos.values() if v["modalidad"] == m)
                                for m in ("Cardinal", "Fijo", "Mutable")},
        "avisos_de_precision": avisos,
        "nota_metodo": ("Cálculo propio con elementos keplerianos JPL (planetas), fórmula de baja "
                        "precisión del Astronomical Almanac (Luna) y nodo lunar medio. Error típico "
                        "≤0.3°; casas por signos enteros desde el Ascendente."),
    }


def a_markdown(c: dict) -> str:
    m = c["momento"]
    L = ["## Cielo del momento — astrología tropical", "",
         f"*{m['local']} (hora local, {m['tz']}) · lat {m['lat']}, lon {m['lon']} · JD {m['jd']}*", "",
         "| Cuerpo | Posición | Casa | Estado |", "|---|---|---|---|"]
    for nombre, v in c["cuerpos"].items():
        estado = "℞ retrógrado" if v["retrogrado"] else "directo"
        L.append(f"| {nombre} | {v['posicion']} | {v['casa']} | {estado} |")
    L += ["",
          f"**Ascendente:** {c['ascendente']['posicion']} · **Medio Cielo:** {c['medio_cielo']['posicion']} "
          f"· **Nodo Norte:** {c['nodo_lunar_norte']['posicion']}",
          f"**Luna:** {c['fase_lunar']['fase']} ({c['fase_lunar']['iluminacion_pct']}% iluminada), "
          f"ciclo {c['fase_lunar']['ciclo']}",
          f"**Retrógrados:** {', '.join(c['retrogrados']) or 'ninguno'}",
          f"**Elementos:** " + " · ".join(f"{k} {v}" for k, v in c["balance_elementos"].items()),
          f"**Modalidades:** " + " · ".join(f"{k} {v}" for k, v in c["balance_modalidades"].items()),
          "", "**Aspectos (orbe ascendente):**"]
    for a in c["aspectos"][:12]:
        ex = " ·exacto" if a["exacto"] else ""
        L.append(f"- {a['cuerpos'][0]} {a['aspecto']} {a['cuerpos'][1]} "
                 f"(orbe {a['orbe']}°{ex})")
    if not c["aspectos"]:
        L.append("- (sin aspectos dentro de orbe)")
    L += ["", "**Casas (signos enteros):**"]
    for h in c["casas"]:
        occ = f" — {', '.join(h['ocupantes'])}" if h["ocupantes"] else ""
        L.append(f"- {h['casa']} en {h['signo']} ({h['asunto']}){occ}")
    if c["avisos_de_precision"]:
        L += ["", "**Avisos de precisión:**"] + [f"- {a}" for a in c["avisos_de_precision"]]
    L += ["", f"*Método:* {c['nota_metodo']}"]
    return "\n".join(L)


def main() -> None:
    ap = argparse.ArgumentParser(description="Cielo del momento (aprox.) para una ubicación")
    ap.add_argument("--fecha", help="AAAA-MM-DD (hora local); por defecto hoy")
    ap.add_argument("--hora", help="HH:MM (hora local); por defecto ahora")
    ap.add_argument("--lat", type=float, default=-12.0464, help="latitud (Lima por defecto)")
    ap.add_argument("--lon", type=float, default=-77.0428, help="longitud, este positiva (Lima por defecto)")
    ap.add_argument("--tz", type=float, default=-5.0, help="huso horario (Lima = -5)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    ahora_local = datetime.now(timezone.utc).replace(tzinfo=None) + timedelta(hours=a.tz)
    if a.fecha:
        y, mo, d = (int(x) for x in a.fecha.split("-"))
        ahora_local = ahora_local.replace(year=y, month=mo, day=d)
    if a.hora:
        h, mi = (int(x) for x in a.hora.split(":"))
        ahora_local = ahora_local.replace(hour=h, minute=mi, second=0, microsecond=0)

    c = carta(ahora_local, a.tz, a.lat, a.lon)
    print(json.dumps(c, ensure_ascii=False, indent=2) if a.json else a_markdown(c))


if __name__ == "__main__":
    main()
