"""Iconos en pixel art para Enxebre Traducións: cada un é unha grella de letras -> cores.

O da web é «mando» (o mando coa franxa azul da bandeira, escollido o 25-10-2026); os outros
quedan como alternativas. Uso: python3 ferramentas/iconos.py mando
  -> web/layouts/partials/logo.html (azul coa cor de acento do tema) e web/static/favicon.svg (cores fixas)."""
import os, sys

# cor fixa (favicon) e, se a hai, variable CSS para o logo da cabeceira
COR = {
    "A": ("#0a6fb4", "var(--acento)"),   # azul da bandeira / da web
    "D": ("#075a93", "var(--acento-forte)"),
    "W": ("#ffffff", None),
    "K": ("#15171c", None),              # contorno
    "R": ("#c4472b", None),              # polbo (pementón)
    "r": ("#8f2f1c", None),
    "G": ("#8b93a1", None),              # gris cartucho / pedra
    "g": ("#b8bec8", None),
    "T": ("#b5532e", None),              # tella
    "t": ("#7e3a20", None),
    "S": ("#d9c7a3", None),              # madeira / pedra clara
    "s": ("#a8916a", None),
}

def bocadillo():
    w, h = 16, 14
    g = [["." for _ in range(w)] for _ in range(h)]
    top, bot = 0, 10                      # bordos do globo
    for x in range(1, w - 1):
        g[top][x] = "K"; g[bot][x] = "K"
    for y in range(top + 1, bot):
        g[y][0] = "K"; g[y][w - 1] = "K"
        for x in range(1, w - 1):
            g[y][x] = "W"
    # banda azul de esquina a esquina, como na bandeira
    ih, iw = bot - top - 1, w - 2
    for y in range(ih):
        c = (y + 0.5) * iw / ih
        for x in range(iw):
            if abs((x + 0.5) - c) < 2.4:
                g[top + 1 + y][1 + x] = "A"
    # rabiño
    for (x, y, c) in [(3, 10, "W"), (4, 10, "W"), (2, 11, "K"), (3, 11, "W"), (4, 11, "K"), (2, 12, "K"), (3, 12, "K"), (1, 13, "K")]:
        g[y][x] = c
    g[13][1] = "."
    g[12][2] = "K"; g[12][3] = "K"
    return ["".join(r) for r in g]

ICONAS = {
    "polbo": [
        "................",
        ".....KKKKKK.....",
        "...KKRRRRRRKK...",
        "..KRRRRRRRRRRK..",
        "..KRRRRRRRRRRK..",
        ".KRRWWRRRRWWRRK.",
        ".KRRWKRRRRWKRRK.",
        ".KRRRRRRRRRRRRK.",
        "..KRRRRrrRRRRK..",
        ".KRRRRRRRRRRRRK.",
        "KRRKRRKRRKRRKRRK",
        "KRKKRKKRRKKRKKRK",
        "KRK.KRKKKKRK.KRK",
        ".KRK.KRK.KRK.KRK",
        "..KK..KK..KK..K.",
        "................",
    ],
    "bocadillo": bocadillo(),
    "mando": [
        "..KKKK....KKKK..",
        ".KWWWWKKKKWWWWK.",
        "KWWKWAAWWWWWKWWK",
        "KWKKKWAAWWWKWKWK",
        "KWWKWWWAAWWWKWWK",
        "KWWWWWWWAAWWWWWK",
        "KWWWWKKKKKKWWWWK",
        ".KWWK......KWWK.",
        "..KK........KK..",
    ],
    "horreo": [
        ".K................K.",
        "KTTTTTTTTTTTTTTTTTTK",
        "KTTTTTTTTTTTTTTTTTTK",
        "KttttttttttttttttttK",
        ".KSsSsSsSsSsSsSsSsK.",
        ".KSsSsSsSsSsSsSsSsK.",
        ".KSsSsSsSsSsSsSsSsK.",
        ".KSsSsSsSsSsSsSsSsK.",
        ".KKKKKKKKKKKKKKKKKK.",
        ".KGGGGK......KGGGGK.",
        "..KKKK........KKKK..",
        "...KGK........KGK...",
        "...KGK........KGK...",
        "..KKKKK......KKKKK..",
    ],
}

def svg(nome, tema=False, clase=None):
    g = ICONAS[nome]
    h, w = len(g), max(len(r) for r in g)
    rects = []
    for y, fila in enumerate(g):
        x = 0
        while x < len(fila):
            c = fila[x]
            if c == ".":
                x += 1; continue
            x2 = x
            while x2 < len(fila) and fila[x2] == c:
                x2 += 1
            fixa, var = COR[c]
            cor = var if (tema and var) else fixa
            rects.append(f'<rect x="{x}" y="{y}" width="{x2 - x}" height="1" fill="{cor}"/>')
            x = x2
    attr = f' class="{clase}" aria-hidden="true"' if clase else ' xmlns="http://www.w3.org/2000/svg"'
    return f'<svg{attr} viewBox="0 0 {w} {h}" shape-rendering="crispEdges">' + "".join(rects) + "</svg>"

def favicon(nome):
    """O favicon vai nun lenzo cadrado, co icono centrado."""
    g = ICONAS[nome]
    h, w = len(g), len(g[0])
    lado = max(w, h)
    s = svg(nome)
    return s.replace(f'viewBox="0 0 {w} {h}"', f'viewBox="{-((lado - w) // 2)} {-((lado - h) // 2)} {lado} {lado}"')


if __name__ == "__main__":
    nome = sys.argv[1] if len(sys.argv) > 1 else "mando"
    web = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "web")
    logo = svg(nome, tema=True, clase="logo-icona")
    open(os.path.join(web, "layouts", "partials", "logo.html"), "w", encoding="utf-8").write(logo + "\n")
    open(os.path.join(web, "static", "favicon.svg"), "w", encoding="utf-8").write(favicon(nome) + "\n")
    print(f"{nome}: {len(ICONAS[nome][0])}x{len(ICONAS[nome])} píxeles -> logo.html e favicon.svg")
