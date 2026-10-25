---
title: "Suzerain"
date: 2026-10-21
subtitulo: "Goberna Sordland en galego: conversas, xornais, leis, finais e o códex enteiro."
sistema: "PC"
plataforma: "PC (Steam)"
ano: 2020
compania: "Torpor Games"
xenero: "Narrativa política"
version: "1.0"
estado: "Completa (Sordland)"

probada: true
probada_data: 2026-10-25

portada: "capturas/xornal.webp"
galeria:
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
  nome: "Suzerain en Steam, versión 3.1.0"
  nota: "En Linux ou Steam Deck. O instalador non trae ningún ficheiro do xogo: traduce o teu."

instalador:
  onde: "Linux e Steam Deck"
  pasos:
    - "Descarga o paquete e descomprímeo onde queiras."
    - "Pecha o xogo."
    - "Abre unha terminal dentro da carpeta e executa `bash instalar.sh`. Busca Suzerain el só nas túas bibliotecas de Steam; se non o atopa, pásalle a carpeta do xogo."
    - "Abre Suzerain. Vale tamén coas partidas xa empezadas."
    - "Para volver ao inglés: `bash desinstalar.sh`."
  nota: "A primeira vez descarga UnityPy (uns 30 MB), a ferramenta que edita os ficheiros do xogo, e gárdaa aparte. Se Steam actualiza o xogo e volve o inglés, abonda con executar outra vez `instalar.sh`. Na Steam Deck faise desde o modo escritorio, coa aplicación Konsole."

descargas:
  - nome: "Instalador para Linux"
    nota: "Versión 1.0 (.zip). Sen ficheiros do xogo"
    url: "https://github.com/enxebre-traducions/enxebre-traducions.github.io/releases/download/suzerain-v1.0/Suzerain-en-galego-1.0.zip"
    destacada: true

creditos:
  - ["Tradución", "Enxebre Traducións, con IA (Claude), a partir da súa [versión en castelán](https://github.com/SuperPadLand/suzerain-castellano)"]
---

Suzerain é un xogo de política sen disparos: es Anton Rayne, presidente recén elixido de Sordland, un país que acaba de saír dunha ditadura, e cada conversa cos ministros, os xornalistas ou a túa familia vai decidindo que tipo de goberno fas. Ten moitísimo texto, e todo importa.

Está traducida toda a historia de Sordland, que é o xogo base. Fíxose con intelixencia artificial a partir da tradución ao castelán do mesmo proxecto, xa revisada, coidando o trato: os ministros tratan o presidente de *vostede*, e a familia e os amigos, de *ti*.

A versión 1.0 corrixe os dous erros que se atoparon ao xogala enteira: as palabras resaltadas saían entre asteriscos (\*así\*) en vez de entre comiñas (“así”), e moitas frases empezaban por «Bo,» onde en galego se di «Ben,». Se tes posta a 0.9, abonda con instalar a 1.0 por riba.

Se tes posta a tradución ao castelán, o instalador galego aproveita os ficheiros orixinais que gardou ela. Para pasar do galego ao castelán, desinstala antes o galego.
