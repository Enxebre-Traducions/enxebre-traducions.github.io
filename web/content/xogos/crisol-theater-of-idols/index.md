---
title: "Crisol: Theater of Idols"
date: 2026-11-08
lastmod: 2026-11-14
subtitulo: "O terror de Hispania, en galego: textos, menús, o logotipo e, se queres, tamén as voces."
sistema: "PC"
plataforma: "PC (Linux)"
ano: 2026
compania: "Vermila Studios"
xenero: "Acción e terror"
version: "1.0.1"
estado: "Completa, con dobraxe opcional"

probada: true
probada_data: 2026-11-08
probada_texto: "Unha persoa xogou a versión 1.0 coa tradución e a dobraxe postas, sen atopar textos rotos nin letras raras. A actualización 1.0.1 (tres pequenas correccións) aínda non se probou no xogo, pero debería funcionar igual."

portada: "capturas/logo.png"
# capturas que saen tamén no escaparate da portada da web (teñen que amosar o galego)
escaparate:
  - "capturas/menu.png"
  - "capturas/mediodia.png"
galeria:
  - imaxe: "capturas/menu.png"
    texto: "O menú principal, co logotipo en galego: «Teatro de Ídolos»"
  - imaxe: "capturas/dificultade.png"
    texto: "A escolla de dificultade"
  - imaxe: "capturas/mediodia.png"
    texto: "A primeira chamada de Mediodía polo transmisor"
  - imaxe: "capturas/cartel.png"
    texto: "Os carteis da cidade levan o seu subtítulo en galego ao miralos"
  - imaxe: "capturas/arroyo.png"
    texto: "O padre Arroyo e Gabriel discuten polo transmisor"
  - imaxe: "capturas/se-busca.png"
    texto: "Os solari comentan os carteis de «Se busca»"
  - imaxe: "capturas/dolores.png"
    texto: "Dolores á espreita nas rúas de Tormentosa"

traducido:
  - "As voces, no paquete con dobraxe: unha dobraxe completa feita con IA, na que cada personaxe fala coa súa voz e as frases van ao ritmo das bocas"
  - "Todos os diálogos e subtítulos"
  - "Os menús, as opcións, a dificultade e os consellos"
  - "Os documentos, o diario e os obxectos"
  - "O logotipo do menú principal, «Teatro de Ídolos», feito coas letras do orixinal"
  - "No menú de idioma, «Galego» onde antes poñía «Español»"
# o título da lista (por defecto «Que queda en inglés»)
sen_traducir_titulo: "Que queda en castelán"
sen_traducir:
  - "Os carteis e letreiros debuxados no escenario e a cita de Calderón do comezo, que quedan en castelán. Os carteis, ao miralos, levan o seu subtítulo en galego"

rom:
  nome: "Crisol: Theater of Idols, probada coa versión de Steam"
  nota: "En Linux, co xogo de Windows funcionando con Proton, Wine, Heroic, Lutris ou Bottles. O instalador recoñece a versión de Steam coa que se fixo e se probou a tradución; se a túa copia é doutra, por exemplo porque o xogo se actualizou despois, avisa e pregunta antes de tocar nada. O paquete non trae o xogo: precisas telo instalado."

instalador:
  onde: "Linux"
  pasos:
    - "Escolle un dos dous paquetes, **con dobraxe** ou **só textos**, e descomprímeo onde queiras."
    - "Pecha o xogo."
    - "Fai dobre clic en `instalar.sh` (se pregunta que facer, escolle *Executar*). Ábrese unha xanela de terminal onde só tes que ir respondendo: busca o xogo el só (Steam, Heroic, Lutris, Bottles, Wine, ~/Games…) e pregúntache en cal das copias o pon; escribe o número e preme Intro. Se o tes noutro sitio, escolle «0» e indícalle a carpeta do xogo; vale tamén unha que a conteña, como o disco onde o gardas."
    - "Abre o xogo e, en *Opcións > Idioma*, escolle **Galego** en *Idioma de visualización*. Co paquete con dobraxe, escolle tamén **Galego** en *Idioma das voces*."
    - "Para volver ao castelán: dobre clic en `desinstalar.sh`."
  nota: "O galego ocupa o sitio do castelán: no menú de idioma, todo o que era «Español» pasa a chamarse «Galego». Por iso, co paquete só con textos, «Galego» en *Idioma das voces* son as voces castelás de sempre (as inglesas seguen como estaban). Para cambiar dun paquete ao outro, instala o novo por riba. Tamén se pode poñer a man: copia os tres ficheiros da carpeta `datos` en `CRToiPrototype/Content/Paks`, dentro da carpeta do xogo. Se o dobre clic abre o texto do ficheiro en vez de executalo (pasa en GNOME), fai clic dereito nel e escolle executalo como programa, ou abre unha terminal na carpeta e escribe `bash instalar.sh`."

descargas:
  - nome: "Con dobraxe galega"
    nota: "Versión 1.0.1 (.zip, 114 MB). Textos, menús, logotipo e voces. Coas últimas correccións, sen probar aínda no xogo"
    url: "https://github.com/enxebre-traducions/enxebre-traducions.github.io/releases/download/crisol-theater-of-idols-v1.0.1/Crisol-en-galego-1.0.1.zip"
    destacada: true
  - nome: "Só textos"
    nota: "Versión 1.0.1 (.zip, 600 KB). Voces orixinais en inglés ou castelán. Coas últimas correccións, sen probar aínda no xogo"
    url: "https://github.com/enxebre-traducions/enxebre-traducions.github.io/releases/download/crisol-theater-of-idols-v1.0.1/Crisol-en-galego-1.0.1-so-textos.zip"
  - nome: "Con dobraxe galega (versión 1.0)"
    nota: "Versión 1.0 (.zip, 114 MB). A probada por humanos, sen as correccións da 1.0.1"
    url: "https://github.com/enxebre-traducions/enxebre-traducions.github.io/releases/download/crisol-theater-of-idols-v1.0/Crisol-en-galego-1.0.zip"
  - nome: "Só textos (versión 1.0)"
    nota: "Versión 1.0 (.zip, 600 KB). A probada por humanos, sen as correccións da 1.0.1"
    url: "https://github.com/enxebre-traducions/enxebre-traducions.github.io/releases/download/crisol-theater-of-idols-v1.0/Crisol-en-galego-1.0-so-textos.zip"

creditos:
  - ["Tradución", "Enxebre Traducións, con IA"]
  - ["Dobraxe", "Voces xeradas con IA"]
---

*Crisol: Theater of Idols* é un xogo de acción e terror en primeira persoa ambientado en Hispania, unha versión retorcida de España. Es Gabriel, un soldado que usa o seu propio sangue como munición, e tes que abrirte camiño por Tormentosa.

Hai dous paquetes. O **con dobraxe** pon en galego os textos, os menús e o logotipo e, ademais, todas as voces: cada personaxe fala coa súa propia voz galega, feita con IA, e as frases axustáronse unha a unha para que caian onde se moven as bocas dos personaxes. O de **só textos** fai o mesmo pero deixa as voces como no xogo, en inglés ou en castelán.

{{< audio src="mostra-dobraxe.mp3" texto="Mostra da dobraxe: o comezo do xogo, a Carpideira e a primeira chamada de Mediodía." >}}

### Novidades da 1.0.1

- A primeira páxina do diario de Marta saía en inglés. Era un fallo do propio xogo, que en castelán fai o mesmo; agora sae en galego.
- Nunha frase de Gabriel, a IA lía «home» coma se fose inglés.
- Unha oración que no xogo orixinal reza un grupo agora tamén a reza un grupo: unha voz diante e o coro detrás.

Estas correccións aínda non se probaron no xogo, pero son pequenas e deberían funcionar igual. Se prefires a versión probada por humanos, a 1.0 segue nas descargas.

