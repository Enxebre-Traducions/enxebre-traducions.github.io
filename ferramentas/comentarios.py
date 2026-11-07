#!/usr/bin/env python3
"""Le os comentarios das fichas (giscus → GitHub Discussions) e escribe web/data/comentarios.json.

Coa portada vese o que se comenta sen entrar en cada ficha: a sección «Últimos comentarios»
e o contador de cada tarxeta saen deste ficheiro. Cada ficha ten o seu fío na categoría de
[params.giscus] (web/hugo.toml), titulado co nome da ficha (ou co `comentarios:` dela).

Execútao a acción .github/workflows/web.yml antes de compilar, tamén cada vez que alguén
comenta. A man (colle o token de `gh` se non hai GH_TOKEN):

  python3 ferramentas/comentarios.py
  python3 ferramentas/comentarios.py --probar   # só amosa o que escribiría

Se GitHub non responde, avisa e non escribe nada: a web compílase igual, sen comentarios.
"""
import json, os, subprocess, sys, tomllib, urllib.request

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEB = os.path.join(RAIZ, "web")
SAIDA = os.path.join(WEB, "data", "comentarios.json")
ULTIMOS = 6        # cantos saen na portada
EXTRACTO = 180     # letras de cada comentario na portada

CONSULTA = """
query($dono: String!, $repo: String!, $categoria: ID!, $despois: String) {
  repository(owner: $dono, name: $repo) {
    discussions(first: 25, after: $despois, categoryId: $categoria) {
      pageInfo { hasNextPage endCursor }
      nodes {
        title
        comments(first: 100) {
          nodes {
            ...comentario
            replies(first: 100) { nodes { ...comentario } }
          }
        }
      }
    }
  }
}
fragment comentario on DiscussionComment {
  createdAt isMinimized deletedAt bodyText
  author { login }
}
"""


def token():
    for nome in ("GH_TOKEN", "GITHUB_TOKEN"):
        if os.environ.get(nome):
            return os.environ[nome]
    try:
        return subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return ""


def preguntar(clave, variables):
    peticion = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": CONSULTA, "variables": variables}).encode(),
        headers={"Authorization": f"bearer {clave}", "Content-Type": "application/json",
                 "User-Agent": "enxebre-traducions-comentarios"})
    with urllib.request.urlopen(peticion, timeout=30) as resposta:
        datos = json.load(resposta)
    if datos.get("errors"):
        raise RuntimeError("; ".join(e.get("message", "?") for e in datos["errors"]))
    return datos["data"]["repository"]["discussions"]


def extracto(texto):
    texto = " ".join(texto.split())
    if len(texto) <= EXTRACTO:
        return texto
    corte = texto[:EXTRACTO].rsplit(" ", 1)[0]
    return corte.rstrip(".,;:–-") + "…"


def main():
    with open(os.path.join(WEB, "hugo.toml"), "rb") as f:
        giscus = tomllib.load(f)["params"]["giscus"]
    dono, repo = giscus["repo"].split("/")
    clave = token()
    if not clave:
        print("Aviso: sen token de GitHub (GH_TOKEN ou `gh auth login`); non leo os comentarios.")
        return

    fios, todos, despois = {}, [], None
    try:
        while True:
            paxina = preguntar(clave, {"dono": dono, "repo": repo,
                                       "categoria": giscus["categoriaId"], "despois": despois})
            for fio in paxina["nodes"]:
                comentarios = []
                for c in fio["comments"]["nodes"]:
                    comentarios.append((c, False))
                    comentarios += [(r, True) for r in c["replies"]["nodes"]]
                vivos = [(c, r) for c, r in comentarios if not c["isMinimized"] and not c["deletedAt"]]
                if not vivos:
                    continue
                fios[fio["title"]] = {"total": len(vivos), "ultimo": max(c["createdAt"] for c, _ in vivos)}
                todos += [{"fio": fio["title"],
                           "autor": (c["author"] or {}).get("login", "alguén"),
                           "data": c["createdAt"],
                           "resposta": r,
                           "texto": extracto(c["bodyText"])} for c, r in vivos]
            if not paxina["pageInfo"]["hasNextPage"]:
                break
            despois = paxina["pageInfo"]["endCursor"]
    except Exception as e:  # rede, token sen permiso, GitHub caído…
        print(f"Aviso: non puiden ler os comentarios ({e}); a web vai sen eles.")
        return

    todos.sort(key=lambda c: c["data"], reverse=True)
    resultado = {"fios": fios, "ultimos": todos[:ULTIMOS]}
    texto = json.dumps(resultado, ensure_ascii=False, indent=2) + "\n"
    if "--probar" in sys.argv:
        print(texto, end="")
        return
    os.makedirs(os.path.dirname(SAIDA), exist_ok=True)
    with open(SAIDA, "w", encoding="utf-8") as f:
        f.write(texto)
    print(f"{sum(f['total'] for f in fios.values())} comentarios en {len(fios)} fichas → {os.path.relpath(SAIDA, RAIZ)}")


if __name__ == "__main__":
    main()
