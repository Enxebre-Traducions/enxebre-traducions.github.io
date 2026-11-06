---
title: "P.T. (Silent Hills)"
date: 2026-11-01
lastmod: 2026-11-01
subtitulo: "O corredor máis temido dos videoxogos, en galego: subtítulos, menú, o final e, se queres, tamén as voces."
sistema: "PC"
plataforma: "PC (Linux)"
ano: 2014
compania: "Kojima Productions"
xenero: "Terror"
version: "1.0"
estado: "Completa, con dobraxe opcional"

probada: true
probada_data: 2026-11-01

portada: "capturas/silent-hills.png"
# a portada (o logo do final) non leva texto en galego: no escaparate da web saen só estas
escaparate_sen_portada: true
escaparate:
  - "capturas/radio-vermella.png"
  - "capturas/corredor.png"
galeria:
  - imaxe: "capturas/corredor.png"
    texto: "A radio conta o crime mentres percorres o corredor"
  - imaxe: "capturas/radio-vermella.png"
    texto: "O corredor en vermello: a radio segue falando, en galego"
  - imaxe: "capturas/opcions.png"
    texto: "O menú de opcións, co galego na lista de subtítulos"
  - imaxe: "capturas/silent-hills.png"
    texto: "O final: P.T. era o avance de Silent Hills"

traducido:
  - "Todos os subtítulos: a radio, o feto do lavabo, a bolsa de papel, a voz do final e as mensaxes escritas que aparecen polo camiño"
  - "O menú de opcións e os avisos do xogo"
  - "As imaxes de texto do final, co inglés borrado e o galego escrito coa letra do propio xogo"
  - "Co paquete da dobraxe, as voces: o locutor da radio (tamén o do teléfono), o feto, a bolsa de papel e a voz do final"
sen_traducir:
  - "Nos menús quedan algúns restos en castelán"
  - "O título «OPTIONS» do menú de opcións, que xa vén en inglés en todos os idiomas do xogo"
  - "A radio en sueco e os murmurios: no orixinal non teñen subtítulos en ningún idioma, e tamén na dobraxe quedan como estaban"

rom:
  nome: "P.T., probada co port de PC 1.0.8 e os datos da versión americana de PS4"
  nota: "Este P.T. é o [port de PC de LoreanXavier](https://github.com/LoreanXavier/pt-pc), que le os datos da túa propia copia do xogo de PS4. O paquete non trae nin o port nin o xogo: precisas telos instalados. O instalador recoñece os datos americanos (CUSA01127), cos que se probou; cos europeos ou cos xaponeses avisa e pregunta antes de tocar nada, porque iso aínda non o probou ninguén."

instalador:
  onde: "Linux"
  pasos:
    - "Escolle un dos dous paquetes, **con dobraxe** ou **só textos**, e descomprímeo onde queiras."
    - "Pecha o xogo."
    - "Fai dobre clic en `instalar.sh` (se pregunta que facer, escolle *Executar*). Ábrese unha xanela de terminal onde só tes que ir respondendo: busca o port de P.T. el só (~/Games, Heroic, Lutris, Bottles…) e pregúntache en cal das copias o pon; escribe o número e preme Intro. Se o tes noutro sitio, escolle «0» e indícalle a carpeta do port (onde está o programa `pt`); vale tamén unha que a conteña, como o disco onde o gardas."
    - "Abre o xogo e, no menú de opcións, escolle **Galego** en *Subtítulos*."
    - "Para volver ao inglés: dobre clic en `desinstalar.sh`."
  nota: "O galego ocupa o sitio do castelán: na lista de subtítulos sae «Galego» onde poñía «Español». Coa dobraxe, as voces soan en galego escollas o idioma que escollas. Para apagalo sen desinstalalo, nos axustes de PC do port: *Gráficos > Mods*. Para cambiar dun paquete ao outro, instala o novo por riba. Tamén se pode poñer a man: copia a carpeta `pt-galego` dentro da carpeta `mods` do port. Se o dobre clic abre o texto do ficheiro en vez de executalo (pasa en GNOME), fai clic dereito nel e escolle executalo como programa, ou abre unha terminal na carpeta e escribe `bash instalar.sh`."

descargas:
  - nome: "Con dobraxe galega"
    nota: "Versión 1.0 (.zip, 138 MB). Subtítulos, menú, final e voces"
    url: "https://github.com/enxebre-traducions/enxebre-traducions.github.io/releases/download/pt-silent-hills-v1.0/PT-en-galego-1.0-dobraxe.zip"
    destacada: true
  - nome: "Só textos"
    nota: "Versión 1.0 (.zip, 130 KB). Voces orixinais en inglés"
    url: "https://github.com/enxebre-traducions/enxebre-traducions.github.io/releases/download/pt-silent-hills-v1.0/PT-en-galego-1.0.zip"

creditos:
  - ["Tradución", "Enxebre Traducións, con IA"]
  - ["Dobraxe", "Voces xeradas con IA"]

# Atopouno ferramentas/videos_youtube.py
video:
  youtube: "y7xJh0X9kXo"
---

P.T. apareceu en 2014 na PlayStation 4 como un xogo de terror gratuíto dun estudo que ninguén coñecía: un corredor, unha radio e unha porta que sempre te devolve ao comezo. Quen chegaba ao final descubría que era o avance xogable de *Silent Hills*, de Hideo Kojima e Guillermo del Toro. O xogo cancelouse e Konami retirou P.T. da tenda en 2015, pero aquel corredor quedou na memoria de todos. Hoxe pódese xogar en PC grazas ao port de LoreanXavier, que le os datos da túa propia copia de PS4.

Hai dous paquetes. O de **só textos** pon en galego os subtítulos, o menú e as imaxes do final, e deixa as voces en inglés. O **con dobraxe** fai o mesmo e, ademais, o locutor da radio, o feto do lavabo, a bolsa de papel e a voz do final falan en galego. As voces fixéronse con intelixencia artificial, escoitáronse unha a unha cun recoñecedor de voz para comprobar que se entende todo e levan o mesmo son ca as orixinais: a radio soa a radio, e a voz do final sae polos mesmos altofalantes ca no xogo.

{{< audio src="mostra-dobraxe.mp3" texto="Mostra da dobraxe: o comezo do noticiario da radio, a bolsa de papel e o feto." >}}

Os subtítulos do paquete con dobraxe van ao ritmo das voces galegas; os do de só textos, ao das inglesas.
