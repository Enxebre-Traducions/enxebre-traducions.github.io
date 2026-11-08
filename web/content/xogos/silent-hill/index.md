---
title: "Silent Hill"
date: 2026-11-07
lastmod: 2026-11-07
subtitulo: "Outeiro Silencioso: o clásico do terror de PlayStation, en galego e con voces."
sistema: "PS1"
# outros sistemas para os que tamén hai parche (saen na tarxeta e no filtro)
tamen_en: ["PC"]
plataforma: "PlayStation e PC (Linux)"
ano: 1999
compania: "Konami"
xenero: "Terror"
version: "0.9.2"
estado: "Completa, con dobraxe opcional"

probada: false
sen_probar: "Probouse só o comezo: ata saír do café despois de falar coa policía e vencer o primeiro monstro, e arranxáronse os fallos que saíron. Aínda non se probou ata o final."

portada: "capturas/titulo.png"
# capturas que saen tamén no escaparate da portada da web (teñen que amosar o galego)
escaparate:
  - "capturas/cheryl.png"
  - "capturas/inventario.png"
galeria:
  - imaxe: "capturas/cheryl.png"
    texto: "Harry ve a Cheryl entre a néboa, ao comezo da historia"
  - imaxe: "capturas/onde-estaras.png"
    texto: "As rúas baleiras de Silent Hill: os subtítulos van coa dobraxe galega"
  - imaxe: "capturas/inventario.png"
    texto: "O inventario: nomes, descricións e ordes en galego"
  - imaxe: "capturas/mapa.png"
    texto: "O mapa de Silent Hill vello, coas rúas traducidas"
  - imaxe: "capturas/gardar.png"
    texto: "Gardar partida, co tempo de xogo"
  - imaxe: "capturas/cargar.png"
    texto: "Cargar partida: os avisos da MEMORY CARD tamén en galego"

traducido:
  - "As voces, nos paquetes con dobraxe: unha dobraxe completa feita con IA, cunha voz galega para cada personaxe (Harry, Cybil, Kaufmann, Dahlia, Lisa e Cheryl)"
  - "Todos os diálogos e subtítulos, as notas, os libros e os quebracabezas"
  - "Os nomes e as descricións dos obxectos"
  - "Os menús: título, dificultade, inventario, opcións, gardar e cargar e a pantalla de resultados"
  - "A pantalla do título, os mapas coas notas de Harry, os consellos da pantalla de morte e os avisos da MEMORY CARD"
sen_traducir:
  - "A frase do comezo do vídeo de introdución"
  - "Os textos debuxados nas imaxes de documentos, notas e etiquetas, e os nomes das tendas"

rom:
  nome: "Silent Hill (USA), SLUS-00707, nun só ficheiro .bin"
  nota: "A versión americana, de 60 Hz. Na PlayStation, o parche aplícase sobre esta imaxe; no PC, é o disco que le o port. Ningún dos dous paquetes trae nada do xogo."
  crc32: "1D4A3FF7"
  md5: "b52500eea7d7d04a6a81b0efe88955e1"
  tamano: "616 494 480 bytes"

instalador:
  onde: "PC con Linux"
  pasos:
    - "Se aínda non tes o port de PC, descarga `SHPC-linux-x64.tar.gz` da [páxina de versións do port](https://github.com/SlickAmogus/silent-hill-decomp/releases/tag/realtime) e descomprímeo onde queiras (por exemplo, en `~/Games/Silent Hill PC`). Copia a túa imaxe `Silent Hill (USA).bin` dentro da súa carpeta `gamedata` e abre `SilentHillPC` unha vez para ver que arranca (precisa SDL2 e OpenAL, que case todas as distribucións traen de serie)."
    - "Escolle un dos dous paquetes de PC, **con dobraxe** ou **só textos**, e descomprímeo onde queiras."
    - "Pecha o xogo."
    - "Fai dobre clic en `instalar.sh` (se pregunta que facer, escolle *Executar*). Ábrese unha xanela de terminal onde só tes que ir respondendo: busca o port el só (~/Games e os sitios habituais) e pregúntache en cal das copias o pon; escribe o número e preme Intro. Se o tes noutro sitio, escolle «0» e indícalle a carpeta do port."
    - "Abre o xogo: xa sae en galego (e, co paquete con dobraxe, tamén con voces galegas). O idioma tamén se cambia en *Axustes*, na pantalla do título."
    - "Para volver ao inglés: dobre clic en `desinstalar.sh`."
  nota: "O instalador pon `language = gl` e `allow_loose_files = 1` no `config.cfg` do port (o segundo fai falta para a portada, as imaxes e as voces). Non precisa internet nin sudo. Para cambiar dun paquete ao outro, instala o novo por riba. Vale tamén a versión de Windows do port funcionando con Wine. Se o dobre clic abre o texto do ficheiro en vez de executalo (pasa en GNOME), fai clic dereito nel e escolle executalo como programa, ou abre unha terminal na carpeta e escribe `bash instalar.sh`."

descargas:
  - nome: "PlayStation, con dobraxe"
    nota: "Versión 0.9.2 (.zip, 33 MB). Parche xdelta: textos e voces"
    url: "https://github.com/enxebre-traducions/enxebre-traducions.github.io/releases/download/silent-hill-v0.9.2/Silent-Hill-en-galego-PS1-0.9.2.zip"
    destacada: true
  - nome: "PlayStation, só textos"
    nota: "Versión 0.9.2 (.zip, 2 MB). Voces orixinais en inglés"
    url: "https://github.com/enxebre-traducions/enxebre-traducions.github.io/releases/download/silent-hill-v0.9.2/Silent-Hill-en-galego-PS1-0.9.2-so-textos.zip"
  - nome: "PC (Linux), con dobraxe"
    nota: "Versión 0.9.2 (.zip, 49 MB). Instalador: textos e voces"
    url: "https://github.com/enxebre-traducions/enxebre-traducions.github.io/releases/download/silent-hill-v0.9.2/Silent-Hill-en-galego-PC-0.9.2.zip"
  - nome: "PC (Linux), só textos"
    nota: "Versión 0.9.2 (.zip, 900 KB). Voces orixinais en inglés"
    url: "https://github.com/enxebre-traducions/enxebre-traducions.github.io/releases/download/silent-hill-v0.9.2/Silent-Hill-en-galego-PC-0.9.2-so-textos.zip"

creditos:
  - ["Tradución", "Enxebre Traducións, con IA"]
  - ["Dobraxe", "Voces xeradas con IA"]

agradecementos:
  - "Á [descompilación de Silent Hill](https://github.com/shdecompilations/silent-hill-decomp): grazas a ela soubemos onde garda o xogo cada texto e que voz vai con cada subtítulo."
  - "Ao [port de PC de SlickAmogus](https://github.com/SlickAmogus/silent-hill-decomp), que permite xogalo en Linux e trae as ferramentas para os paquetes de idioma."
---

*Silent Hill* é o primeiro da saga: Harry Mason ten un accidente de coche á entrada dun pobo envolto en néboa e, cando esperta, a súa filla Cheryl desapareceu. Para atopala terá que percorrer as rúas baleiras, a escola e o hospital de Silent Hill.

Está traducido enteiro ao galego e tamén dobrado: cada personaxe fala coa súa propia voz galega, feita con IA, e os subtítulos van coas voces. Se prefires as voces orixinais, hai tamén paquetes só con textos: as voces quedan en inglés e todos os subtítulos en galego.

{{< audio src="mostra-dobraxe.mp3" texto="Mostra da dobraxe: Harry esperta no café e fala con Cybil, a policía." >}}

Hai dúas versións, cos mesmos textos: un parche para o disco de PlayStation e un instalador para o port de PC en Linux, e cada unha vén con dobraxe ou só con textos.

### Por que «Outeiro Silencioso»

A pantalla do título pon «Outeiro Silencioso», cun «Silent Hill» pequeno debaixo, porque nos fixo graza traducilo. É só iso: no resto do xogo o pobo chámase Silent Hill, como debe ser.

### Na PlayStation

Escolle o parche de PlayStation con dobraxe ou o de só textos: cada un leva o ficheiro `Silent-Hill-galego.xdelta`, o `.cue` e un LEME coas instrucións. Aplica o parche á túa imaxe `Silent Hill (USA).bin` cun parcheador de xdelta, como [Rom Patcher JS](https://www.marcrobledo.com/RomPatcher.js/) no navegador ou `xdelta3` na terminal, chama ao resultado `Silent Hill (galego).bin` e déixao na mesma carpeta ca o `.cue`. Funciona en emuladores, como DuckStation, e na consola con calquera sistema que lea imaxes .bin/.cue.

### No PC

O paquete de PC é para o port de Silent Hill feito a partir da descompilación do xogo de PlayStation, e precisa o teu disco americano. Os pasos para conseguir o port e instalar o galego están en «Como se instala», aquí debaixo.
