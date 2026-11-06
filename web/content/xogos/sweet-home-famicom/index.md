---
title: "Sweet Home"
date: 2026-11-06
subtitulo: "O terror de Capcom que deu orixe a Resident Evil, traducido ao galego desde o guión xaponés orixinal."
sistema: "Famicom"
plataforma: "Famicom"
ano: 1989
compania: "Capcom"
xenero: "Rol e terror"
version: "0.9"
estado: "Completa"

probada: false
sen_probar: "Está traducida enteira e cada texto comprobouse automaticamente no xogo. Xogouse o comezo en ares e en Mesen e funciona ben, pero aínda ninguén a xogou enteira e falta probala na consola orixinal."

portada: "capturas/titulo-gl.png"
pixelada: true
# capturas que saen tamén no escaparate da portada da web (teñen que amosar o galego)
escaparate:
  - "capturas/mansion-gl.png"
lingua_orixinal: "xaponés"
comparacions:
  - nome: "Título"
    orixinal: "capturas/titulo-xp.png"
    galego: "capturas/titulo-gl.png"
  - nome: "A mansión"
    orixinal: "capturas/mansion-xp.png"
    galego: "capturas/mansion-gl.png"
  - nome: "Os frescos"
    orixinal: "capturas/frescos-xp.png"
    galego: "capturas/frescos-gl.png"
  - nome: "Akiko"
    orixinal: "capturas/akiko-xp.png"
    galego: "capturas/akiko-gl.png"
comparacions_nota: "Arrastra a liña para comparar co orixinal xaponés. Capturas sacadas do emulador co parche aplicado."
galeria:
  - imaxe: "capturas/fresco.png"
    texto: "Taguchi diante dun dos frescos de Ichiro Mamiya"
  - imaxe: "capturas/combate.png"
    texto: "Un combate: cada personaxe ten a súa vida e as súas ordes"

traducido:
  - "Os 466 textos do xogo, traducidos do xaponés: diálogos, notas, o diario de Ichiro, os frescos, o combate, a intro e o final"
  - "As respostas propias de cada personaxe e as variantes de home e de muller, que a versión inglesa recortara por falta de espazo"
  - "Os nomes dos 72 obxectos e dos 31 inimigos"
  - "Menús, pantalla de título, pantalla de nomes, fin da partida e créditos finais"

rom:
  nome: "Sweet Home (Japan).nes"
  nota: "A versión xaponesa orixinal, sen ningunha tradución. Vale tamén a copia coa cabeceira NES 2.0 de No-Intro (MD5 761c3fbbbd4ea29f19e28311a583de3a): no parcheador desta páxina ou co seu BPS."
  crc32: "40803BC5"
  md5: "49dd966e8a0e17bae16bc3d393c9d742"
  tamano: "262 160 bytes"

parcheador:
  parche: "parches/sweet-home-famicom/sweethome_galego.ips"
  extension: ".nes"
  # SHA-1 do contido da ROM sen a cabeceira iNES de 16 bytes: así vale
  # calquera cabeceira (iNES clásica ou NES 2.0) e mesmo sen cabeceira.
  # O IPS só cambia o byte 4 da cabeceira (256 → 512 KB de PRG).
  sha1_entrada: "a07bd0fdf7ba3a30fc4e40d50373cb77a9627eee"
  sha1_saida: "e0aeb18d16b83ce244b5a0fdf41c0a0a5b6ff75c"
  tamano_sen_cabeceira: 262144
  cabeceira: "4e45531a100012000000000000000000"
  saida: "Sweet Home (galego).nes"

descargas:
  - nome: "Parche BPS"
    nota: "Recomendado se parcheas á man: avisa se a ROM non é a boa"
    ficheiro: "parches/sweet-home-famicom/sweethome_galego.bps"
    destacada: true
  - nome: "Parche BPS (No-Intro)"
    nota: "O mesmo, para a copia coa cabeceira NES 2.0 de No-Intro"
    ficheiro: "parches/sweet-home-famicom/sweethome_galego_nointro.bps"
  - nome: "Parche IPS"
    nota: "Para aplicadores antigos. Non comproba nada"
    ficheiro: "parches/sweet-home-famicom/sweethome_galego.ips"
  - nome: "Paquete completo"
    nota: "Os tres parches e o LEME con instrucións (.zip)"
    url: "https://github.com/enxebre-traducions/enxebre-traducions.github.io/releases/download/sweet-home-famicom-v0.9/Sweet-Home-galego-v0.9.zip"

creditos:
  - ["Tradución", "Enxebre Traducións, con IA (Claude e Gemini)"]
  - ["Versión inglesa e motor", "The Siege e JMN (2016): a fonte latina e os nomes de lonxitude variable"]
  - ["Ferramentas", "[Wave](https://github.com/sewave) (Hextractor e a súa documentación) e o seu gráfico das vogais con til"]
---

Un equipo de televisión entra na mansión abandonada do pintor Ichiro Mamiya en busca dos seus frescos, e a casa non os deixa saír. Cinco personaxes, cada un cunha ferramenta propia, e ningunha segunda oportunidade: quen morre, non volve. Capcom fíxoo en 1989 a partir da película do mesmo nome e, anos despois, foi o punto de partida de Resident Evil.

Esta tradución parte do **guión xaponés**, non da versión inglesa. O xaponés ten moito máis texto: cada personaxe responde ao seu xeito e hai frases distintas para home e para muller, e en inglés todo iso recortárase por falta de espazo. Para que collese o galego enteiro, a ROM pasa de 256 a 512 KB, coma Dragon Warrior III e IV: a metade nova leva un segundo banco de texto. Probouse en ares e en Mesen, e debería ir en calquera emulador ou cartucho flash que soporte a placa SUROM do mapper 1.

As maiúsculas con til (É, Á, Ó, Í, Ú) debuxáronse para o galego. A tradución e o romhacking fixéronse con intelixencia artificial, e cada texto comprobouse automaticamente no propio xogo. Falta que alguén a xogue de principio a fin: se o fas, avísanos.
