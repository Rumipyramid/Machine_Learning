#!/usr/bin/env python3
"""
pack-assets.py — Empaqueta los assets de marca Rimac para decks PORTABLES.

Por qué existe: design.md exige que el HTML entregado tenga 0 ocurrencias de
'./assets/' — fuentes e imágenes deben ir embebidas en base64 para que el deck
sea un único archivo que se mueva sin romperse (si no, rutas relativas → 404 →
las fuentes caen a Helvetica y las imágenes quedan rotas).

Qué hace:
  1. Fuentes: .ttf → woff2 → base64, y emite un bloque @font-face con data: URIs
     (~40KB por peso vs ~100KB del .ttf). BRSonoma (4 pesos) + Rimac Display.
  2. Imágenes: data: URI base64. La wave (PNG con alpha, ~1.6MB) → JPEG con matte
     blanco (~190KB, ≈8× más liviano) porque va sobre fondo blanco. El logo SVG se
     deja como SVG inline (no se toca).
  3. Escribe un .css y un .html de snippet listos para pegar en el <style>/<head>.

Uso:
    python scripts/pack-assets.py [--assets ./assets] [--out ./build] [--wave-jpeg]

Dependencias:
    pip install fonttools brotli Pillow
"""

import argparse
import base64
import io
import os
import sys

# ── Mapeo de nombre de archivo de fuente → (font-family, weight, style) ──────────
# Solo embebemos los pesos que el sistema usa de verdad (design.md §1.2):
# 400 cuerpo / 500 lead·footer / 700 sub-titulares·tier-tags / 800 titulares.
FONT_MAP = {
    "BRSonoma-Regular.ttf": ("BRSonoma", 400, "normal"),
    "BRSonoma-Medium.ttf":  ("BRSonoma", 500, "normal"),
    "BRSonoma-Bold.ttf":    ("BRSonoma", 700, "normal"),
    "BRSonoma-Black.ttf":   ("BRSonoma", 800, "normal"),
    "Rimac-Display.ttf":    ("Rimac Display", 800, "normal"),
}


def ttf_to_woff2_b64(ttf_path):
    """Convierte un .ttf a woff2 en memoria y devuelve el base64."""
    try:
        from fontTools.ttLib import TTFont
    except ImportError:
        sys.exit("Falta fontTools. Instalá: pip install fonttools brotli")
    try:
        import brotli  # noqa: F401  (lo necesita fontTools para flavor='woff2')
    except ImportError:
        sys.exit("Falta brotli (compresor woff2). Instalá: pip install brotli")

    font = TTFont(ttf_path)
    buf = io.BytesIO()
    font.flavor = "woff2"
    font.save(buf)
    return base64.b64encode(buf.getvalue()).decode("ascii")


def build_font_face_css(assets_dir):
    """Genera el bloque @font-face con las fuentes embebidas en base64."""
    fonts_dir = os.path.join(assets_dir, "fonts")
    if not os.path.isdir(fonts_dir):
        sys.exit(f"No encuentro la carpeta de fuentes: {fonts_dir}")

    blocks = []
    for filename, (family, weight, style) in FONT_MAP.items():
        path = os.path.join(fonts_dir, filename)
        if not os.path.exists(path):
            print(f"  ⚠  falta {filename} — se omite", file=sys.stderr)
            continue
        b64 = ttf_to_woff2_b64(path)
        blocks.append(
            f"@font-face{{font-family:'{family}';"
            f"src:url(data:font/woff2;base64,{b64}) format('woff2');"
            f"font-weight:{weight};font-style:{style};font-display:swap;}}"
        )
        print(f"  ✓ {filename:28s} → {family} {weight} ({len(b64)//1024}KB b64)")
    return "\n".join(blocks)


def image_to_data_uri(path, as_jpeg_matte=False, max_dim=1600, quality=85):
    """Devuelve un data: URI base64 de la imagen. Opcional: JPEG con matte blanco."""
    try:
        from PIL import Image
    except ImportError:
        sys.exit("Falta Pillow. Instalá: pip install Pillow")

    img = Image.open(path)
    if max_dim:
        img.thumbnail((max_dim, max_dim), Image.LANCZOS)

    buf = io.BytesIO()
    if as_jpeg_matte:
        # Aplana el alpha sobre blanco (la wave va sobre fondo blanco).
        if img.mode in ("RGBA", "LA", "P"):
            bg = Image.new("RGB", img.size, (255, 255, 255))
            rgba = img.convert("RGBA")
            bg.paste(rgba, mask=rgba.split()[-1])
            img = bg
        else:
            img = img.convert("RGB")
        img.save(buf, "JPEG", quality=quality)
        mime = "image/jpeg"
    else:
        img.save(buf, "PNG")
        mime = "image/png"

    b64 = base64.b64encode(buf.getvalue()).decode("ascii")
    return f"data:{mime};base64,{b64}", len(b64)


def main():
    ap = argparse.ArgumentParser(description="Empaqueta assets Rimac para decks portables.")
    ap.add_argument("--assets", default="./assets", help="Carpeta de assets (default ./assets)")
    ap.add_argument("--out", default="./build", help="Carpeta de salida (default ./build)")
    ap.add_argument("--wave-jpeg", action="store_true",
                    help="Embebe Wave-Soft como JPEG matte blanco (recomendado, ~8× más liviano)")
    args = ap.parse_args()

    os.makedirs(args.out, exist_ok=True)

    print("→ Fuentes (.ttf → woff2 → base64):")
    font_css = build_font_face_css(args.assets)

    css_path = os.path.join(args.out, "fonts-embedded.css")
    with open(css_path, "w") as f:
        f.write("/* Fuentes Rimac embebidas — pegar al inicio del <style>. */\n")
        f.write(font_css + "\n")
    print(f"→ Escrito: {css_path}")

    # Imágenes (opcional): emite un snippet con los data URIs para pegar.
    img_snippets = []
    wave = os.path.join(args.assets, "Wave-Soft.png")
    if os.path.exists(wave):
        uri, n = image_to_data_uri(wave, as_jpeg_matte=args.wave_jpeg)
        kind = "JPEG matte" if args.wave_jpeg else "PNG"
        print(f"  ✓ Wave-Soft ({kind}, {n//1024}KB b64)")
        img_snippets.append(f'<!-- wave de portada -->\n<img class="wave-bg" alt="" src="{uri}">')

    bg = os.path.join(args.assets, "Background.jpg")
    if os.path.exists(bg):
        uri, n = image_to_data_uri(bg, as_jpeg_matte=False)
        print(f"  ✓ Background ({n//1024}KB b64)")
        img_snippets.append(f'<!-- foto de portada -->\n<img alt="" src="{uri}">')

    if img_snippets:
        html_path = os.path.join(args.out, "images-embedded.html")
        with open(html_path, "w") as f:
            f.write("<!-- Imágenes Rimac embebidas — reemplazar el src de los <img> correspondientes. -->\n")
            f.write("\n\n".join(img_snippets) + "\n")
        print(f"→ Escrito: {html_path}")

    print("\n✅ Listo. Pegá fonts-embedded.css al inicio del <style> y usá los data URIs")
    print("   de images-embedded.html. Meta: 0 ocurrencias de './assets/' en el HTML final.")
    print("   (El logo Rimac va como SVG inline desde la constante LOGO_SVG — no se embebe acá.)")


if __name__ == "__main__":
    main()
