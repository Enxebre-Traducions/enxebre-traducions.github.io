---
title: "Suzerain"
date: 2026-10-21
subtitulo: "Goberna Sordland en galego: conversas, xornais, leis, finais e o códex enteiro."
sistema: "PC"
plataforma: "PC (Linux)"
ano: 2020
compania: "Torpor Games"
xenero: "Narrativa política"
version: "1.0.1"
estado: "Completa (Sordland)"

probada: true
probada_data: 2026-10-25

portada: "capturas/menu.webp"
galeria:
  - imaxe: "capturas/menu-enteiro.webp"
    texto: "O menú principal, en galego"
  - imaxe: "capturas/xornal.webp"
    texto: "O xornal da mañá, en galego"
  - imaxe: "capturas/conversa.webp"
    texto: "Unha conversa no despacho presidencial"
  - imaxe: "capturas/mapa.webp"
    texto: "O menú dunha cidade no mapa. A primeira e a última opción veñen do código do xogo e quedan en inglés"

traducido:
  - "Toda a historia de Sordland: o prólogo, os once turnos, os epílogos e os nove finais da xubilación"
  - "Xornais, informes, diario, decisións, decretos e leis"
  - "O códex enteiro, as políticas e as situacións"
  - "A interface: menús, mapa, paneis do goberno e da Asemblea, e os cargos dos personaxes"
sen_traducir:
  - "O DLC *Kingdom of Rizia*: traducimos só o xogo base, Sordland, porque o DLC non o temos e non o poderiamos probar"
  - "Uns poucos rótulos e avisos que escribe o propio programa do xogo, como «Open City Information», «Read the report.» ou «Are you sure…?»: non están nos ficheiros de texto que traduce o instalador, senón dentro do código, e cambialos obrigaría a modificar o programa, co risco de rompelo"
  - "As etiquetas da personalización do presidente (*Hair*, *Attire*, *Background*…): o xogo xéraas no código a partir dunha lista interna, así que pasa o mesmo"
  - "Os nomes das etnias e relixións nas fichas das cidades do mapa (*Sordish*, *Bludish*, *Agno-Sordish*…): o xogo úsaos por dentro como identificadores e, se se traducen, a partida bloquéase ao comezar a primeira quenda"

rom:
  nome: "Suzerain 3.1.0, probada coa versión de Steam"
  nota: "En Linux ou Steam Deck, co xogo funcionando con Proton, Wine, Heroic, Lutris ou Bottles. O instalador recoñece a versión de Steam coa que se probou; con calquera outra copia (doutra tenda, como GOG, ou doutra versión) avisa e pregunta antes de tocar nada, porque iso aínda non o probou ninguén. Non trae ningún ficheiro do xogo: traduce o teu."

instalador:
  onde: "Linux e Steam Deck"
  pasos:
    - "Descarga o paquete e descomprímeo onde queiras."
    - "Pecha o xogo."
    - "Fai dobre clic en `instalar.sh` (se pregunta que facer, escolle *Executar*). Ábrese unha xanela de terminal onde só tes que ir respondendo: busca Suzerain el só (Steam, Heroic, Lutris, Bottles, Wine…) e pregúntache en cal das copias o pon; escribe o número e preme Intro. Se o tes noutro sitio, escolle «0» e indícalle a carpeta; vale tamén unha que a conteña, como o disco onde o gardas."
    - "Abre Suzerain. Vale tamén coas partidas xa empezadas."
    - "Para volver ao inglés: dobre clic en `desinstalar.sh`."
  nota: "A primeira vez descarga UnityPy (uns 30 MB), a ferramenta que edita os ficheiros do xogo, e gárdaa aparte. Se o xogo se actualiza e volve o inglés, abonda con executar outra vez `instalar.sh`. Na Steam Deck faise desde o modo escritorio. Se o dobre clic abre o texto do ficheiro en vez de executalo (pasa en GNOME), fai clic dereito nel e escolle executalo como programa, ou abre unha terminal na carpeta e escribe `bash instalar.sh`."

descargas:
  - nome: "Instalador para Linux"
    nota: "Versión 1.0.1 (.zip). Sen ficheiros do xogo"
    url: "https://github.com/enxebre-traducions/enxebre-traducions.github.io/releases/download/suzerain-v1.0.1/Suzerain-en-galego-1.0.1.zip"
    destacada: true

creditos:
  - ["Tradución", "Enxebre Traducións, con IA (Claude), a partir da súa [versión en castelán](https://github.com/SuperPadLand/suzerain-castellano)"]
---

Suzerain é un xogo de política sen disparos: es Anton Rayne, presidente recén elixido de Sordland, un país que acaba de saír dunha ditadura, e cada conversa cos ministros, os xornalistas ou a túa familia vai decidindo que tipo de goberno fas. Ten moitísimo texto, e todo importa.

Está traducida toda a historia de Sordland, que é o xogo base. Fíxose con intelixencia artificial a partir da tradución ao castelán do mesmo proxecto, xa revisada, coidando o trato: os ministros tratan o presidente de *vostede*, e a familia e os amigos, de *ti*.

A versión 1.0 corrixe os dous erros que se atoparon ao xogala enteira: as palabras resaltadas saían entre asteriscos (\*así\*) en vez de entre comiñas (“así”), e moitas frases empezaban por «Bo,» onde en galego se di «Ben,». Se tes posta a 0.9, abonda con instalar a 1.0 por riba.

A 1.0.1 trae a mesma tradución cun instalador novo: xa non fai falta que o xogo sexa de Steam, porque o busca tamén en Heroic, Lutris, Bottles e Wine, e deixa escoller calquera outra carpeta. Se a copia non é a versión coa que se probou, avisa e pregunta antes. Se tes posta a 1.0, non tes que facer nada.

Se tes posta a tradución ao castelán, o instalador galego aproveita os ficheiros orixinais que gardou ela. Para pasar do galego ao castelán, desinstala antes o galego.
