#!/usr/bin/env python3
"""Debuxa a base da imaxe que se ve ao compartir a portada da web (1200x630, og:image).

A base leva o fixo: fondo, logo, nome, lema e enderezo. As portadas dos xogos póñaas Hugo
enriba ao compilar (layouts/partials/compartir.html), así que a imaxe vaise actualizando soa
con cada xogo novo. Só hai que volver executar isto se cambia o lema ou o logo:

  python3 ferramentas/compartir.py
  -> web/assets/compartir/base.png e web/assets/compartir/marco.png

Precisa Pillow e fontTools (para ler as fontes .woff2 da web)."""
import io, os, sys
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFilter, ImageFont

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTES = os.path.join(RAIZ, "web/static/fontes")
SAIDA = os.path.join(RAIZ, "web/assets/compartir")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from iconos import ICONAS, COR  # noqa: E402

LARGO, ALTO = 1200, 630
MARXE = 72
# as portadas: ata catro de 252x158 (16:10), na mesma fila; partials/compartir.html usa estas medidas
PORTADA_X, PORTADA_Y, PORTADA_W, PORTADA_H, PORTADA_OCO = MARXE, 392, 252, 158, 16

FONDO = (11, 18, 32)        # --fondo do tema escuro
TINTA = (236, 239, 244)
TENUE = (150, 161, 178)
ACENTO = (76, 180, 242)     # --acento do tema escuro


def fonte(nome, tamano, peso=None):
    """Le unha .woff2 da web; se é variable, fixa o peso."""
    f = TTFont(os.path.join(FONTES, nome))
    f.flavor = None
    datos = io.BytesIO()
    f.save(datos)
    datos.seek(0)
    letra = ImageFont.truetype(datos, tamano)
    if peso is not None:
        ejes = letra.get_variation_axes()
        letra.set_variation_by_axes([peso if e["name"] in (b"Weight", "Weight") else e["default"] for e in ejes])
    return letra


def base():
    im = Image.new("RGB", (LARGO, ALTO), FONDO)
    # brillo azul arriba á dereita, coma no heroe da web
    brillo = Image.new("RGB", (LARGO, ALTO), FONDO)
    d = ImageDraw.Draw(brillo)
    d.ellipse((620, -360, 1500, 300), fill=(16, 52, 86))
    brillo = brillo.filter(ImageFilter.GaussianBlur(120))
    im = Image.blend(im, brillo, 0.9)
    d = ImageDraw.Draw(im)
    # a grella de puntos do heroe, que se esvaece cara a abaixo
    for y in range(11, ALTO, 22):
        forza = max(0.0, 1 - y / (ALTO * 0.85))
        cor = tuple(int(FONDO[i] + (TINTA[i] - FONDO[i]) * 0.10 * forza) for i in range(3))
        for x in range(11, LARGO, 22):
            d.point((x, y), fill=cor)

    # logo (o mando en pixel art) e nome
    escala = 5
    grella = ICONAS["mando"]
    for y, fila in enumerate(grella):
        for x, letra in enumerate(fila):
            if letra in COR:
                cor = ACENTO if letra == "A" else (TINTA if letra == "W" else (8, 10, 14))
                d.rectangle((MARXE + x * escala, 66 + y * escala, MARXE + (x + 1) * escala - 1, 66 + (y + 1) * escala - 1), fill=cor)
    pixel = fonte("silkscreen-latin-400-normal.woff2", 30)
    x = MARXE + len(grella[0]) * escala + 22
    d.text((x, 74), "ENXEBRE ", font=pixel, fill=TINTA)
    d.text((x + d.textlength("ENXEBRE ", font=pixel), 74), "TRADUCIÓNS", font=pixel, fill=ACENTO)

    # o lema, en dúas liñas, co «o galego» resaltado coma na web
    titulo = fonte("bricolage-grotesque-latin-wght-normal.woff2", 80, peso=700)
    d.text((MARXE, 140), "Ti pos o xogo,", font=titulo, fill=TINTA)
    x = MARXE
    d.text((x, 228), "nós ", font=titulo, fill=TINTA)
    x += d.textlength("nós ", font=titulo)
    ancho = d.textlength("o galego", font=titulo)
    d.rectangle((x - 2, 290, x + ancho + 2, 318), fill=(19, 56, 88))
    d.text((x, 228), "o galego", font=titulo, fill=ACENTO)
    x += ancho
    d.text((x, 228), ".", font=titulo, fill=TINTA)

    texto = fonte("inter-latin-wght-normal.woff2", 25, peso=450)
    d.text((MARXE, 336), "Videoxogos traducidos ao galego, dos clásicos de consola aos de PC para Linux.", font=texto, fill=TENUE)
    pequena = fonte("silkscreen-latin-400-normal.woff2", 17)
    d.text((MARXE, 578), "enxebre-traducions.github.io", font=pequena, fill=TENUE)
    return im


def marco():
    """Vai enriba de cada portada: esquinas redondas (co fondo) e un bordo fino."""
    escala = 4
    w, h, raio = PORTADA_W * escala, PORTADA_H * escala, 12 * escala
    m = Image.new("RGBA", (w, h), FONDO + (255,))
    d = ImageDraw.Draw(m)
    d.rounded_rectangle((0, 0, w - 1, h - 1), radius=raio, fill=(0, 0, 0, 0), outline=(255, 255, 255, 46), width=2 * escala)
    return m.resize((PORTADA_W, PORTADA_H), Image.LANCZOS)


if __name__ == "__main__":
    os.makedirs(SAIDA, exist_ok=True)
    base().save(os.path.join(SAIDA, "base.png"), optimize=True)
    marco().save(os.path.join(SAIDA, "marco.png"), optimize=True)
    print("Feito:", os.path.relpath(SAIDA, RAIZ), "(base.png e marco.png)")
