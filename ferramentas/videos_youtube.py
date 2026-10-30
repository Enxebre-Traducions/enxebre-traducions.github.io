#!/usr/bin/env python3
"""Busca na canle de YouTube os vídeos dos xogos da web e pono na súa ficha (video.youtube).

Le o feed público da canle (os últimos 15 vídeos, sen claves; a canle está en
[params.youtube] de web/hugo.toml). Un vídeo é dun xogo se:
  1. a descrición leva a ligazón á súa ficha (enxebre-traducions.github.io/xogos/<ficha>), ou
  2. o título empeza por «Turbo Review de <título do xogo>» e, se leva plataformas entre
     parénteses, unha delas é o `sistema` da ficha (así «Castlevania (PS1)» non cae na de NES).

Só toca as fichas que aínda non teñen `video:`. Para que unha ficha non colla nunca vídeo,
pon `video: false`. Execútao soa a acción .github/workflows/videos.yml; a man:

  python3 ferramentas/videos_youtube.py            # escribe nas fichas
  python3 ferramentas/videos_youtube.py --probar   # só di o que faría
  python3 ferramentas/videos_youtube.py --feed feed.xml --probar
"""
import glob, os, re, sys, tomllib, unicodedata, urllib.request
import xml.etree.ElementTree as ET

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEB = os.path.join(RAIZ, "web")
NS = {"a": "http://www.w3.org/2005/Atom", "yt": "http://www.youtube.com/xml/schemas/2015",
      "m": "http://search.yahoo.com/mrss/"}


def normal(texto):
    """Minúsculas, sen tiles e só letras e números separados por un espazo."""
    texto = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode().lower()
    return " ".join(re.sub(r"[^a-z0-9]+", " ", texto).split())


def campo(fronte, nome):
    m = re.search(rf'^{nome}:\s*"?(.*?)"?\s*$', fronte, re.M)
    return m.group(1) if m else ""


def fichas():
    for ruta in sorted(glob.glob(os.path.join(WEB, "content/xogos/*/index.md"))):
        texto = open(ruta, encoding="utf-8").read()
        fronte = texto.split("\n---", 1)[0]
        yield {"ruta": ruta, "texto": texto, "slug": os.path.basename(os.path.dirname(ruta)),
               "titulo": campo(fronte, "title"), "sistema": campo(fronte, "sistema"),
               "ten_video": re.search(r"^video:", fronte, re.M) is not None}


def vale_polo_titulo(titulo_video, ficha):
    inicio = re.match(r"\s*turbo review\b(?:\s+de\b)?\s*:?\s*", titulo_video, re.I)
    if not inicio:
        return False
    # o nome do xogo remata nun «:», nun «(», nun « - » ou ao final; proban todos porque o
    # propio nome pode levar «:» («Penumbra: Overture»), pero ten que coincidir enteiro
    # («Castlevania III» non é «Castlevania»)
    resto = titulo_video[inicio.end():]
    cortes = [c.start() for c in re.finditer(r"\s*(?::|\(|\s[-–—|]\s)", resto)] + [len(resto)]
    if not any(normal(resto[:c]) == normal(ficha["titulo"]) for c in cortes):
        return False
    plataformas = [normal(p) for grupo in re.findall(r"\(([^)]*)\)", titulo_video)
                   for p in re.split(r"[,/]", grupo)]
    sistema = normal(ficha["sistema"])
    return not plataformas or any(f" {sistema} " in f" {p} " for p in plataformas)


def main():
    probar = "--probar" in sys.argv
    with open(os.path.join(WEB, "hugo.toml"), "rb") as f:
        canle = tomllib.load(f)["params"]["youtube"]["id"]
    if "--feed" in sys.argv:
        xml = open(sys.argv[sys.argv.index("--feed") + 1], "rb").read()
    else:
        url = f"https://www.youtube.com/feeds/videos.xml?channel_id={canle}"
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                xml = r.read()
        except Exception as e:
            # YouTube falla ás veces: xa se mirará na próxima volta
            print(f"Non se puido ler o feed ({e}); non se cambia nada.")
            return
    videos = []
    for e in ET.fromstring(xml).findall("a:entry", NS):
        videos.append({"id": e.find("yt:videoId", NS).text, "titulo": e.find("a:title", NS).text or "",
                       "descricion": e.find("m:group/m:description", NS).text or ""})

    for ficha in fichas():
        if ficha["ten_video"]:
            continue
        ligazon = re.compile(rf"enxebre-traducions\.github\.io/xogos/{re.escape(ficha['slug'])}(/|\b)", re.I)
        atopado = next((v for v in videos if ligazon.search(v["descricion"])), None) \
            or next((v for v in videos if vale_polo_titulo(v["titulo"], ficha)), None)
        if not atopado:
            continue
        print(f"{ficha['slug']}: {atopado['id']} «{atopado['titulo']}»")
        if probar:
            continue
        # o bloque vai ao final do front matter, antes do «---» que o pecha
        cabeza, resto = ficha["texto"].split("\n---", 1)
        bloque = f'\n\n# Atopouno ferramentas/videos_youtube.py\nvideo:\n  youtube: "{atopado["id"]}"'
        with open(ficha["ruta"], "w", encoding="utf-8") as f:
            f.write(cabeza.rstrip("\n") + bloque + "\n---" + resto)


if __name__ == "__main__":
    main()
