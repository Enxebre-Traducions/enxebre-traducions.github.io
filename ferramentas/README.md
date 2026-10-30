# Ferramentas · Herramientas

Scripts do fluxo de traballo, pensados para xogos con **ocos de tamaño fixo**
(sen táboa de punteiros editable), que é o caso habitual nos proxectos de
[Hextractor](https://github.com/sewave/hextractor).

A idea de fondo: **cada liña traducida ten que medir exactamente os mesmos
bytes que a orixinal**. Con esa regra, un mapa `texto_orixe → texto_galego`
vale para todo o xogo e non hai que tocar nin un punteiro.

| Script | Que fai |
|---|---|
| `units.py` | Le e reconstrúe un `.ext` de Hextractor en unidades numeradas (round-trip exacto) |
| `chk.py` | Conta os bytes de cada cadea segundo a `.tbl` e valida os `#NNN` e os totais `\|NNN` do bloque |
| `fit.py` | Axusta a tradución igualando **cada liña de pantalla** ao ancho da orixinal, tocando só espazos de recheo |
| `buildmap.py` | Xunta os `map*.tsv`, aplica `fit` e escribe `map_fitted.tsv`; avisa do que non pode cadrar só |
| `render.py` | Debuxa texto cos tiles reais da ROM parcheada a un PNG (para revisar sen emulador) |
| `mkbps.py` | Xera un parche BPS con sumas CRC32 e comproba que reproduce a ROM destino |
| `applyips.py` | Aplica un parche IPS (útil para reconstruír a ROM base doutra tradución) |
| `iconos.py` | Debuxa en pixel art o icono da web (o mando coa bandeira) e escribe o logo e o favicon: `python3 ferramentas/iconos.py mando` |
| `compartir.py` | Debuxa a base da imaxe que se ve ao compartir a portada (fondo, logo e lema). As portadas dos xogos pónas Hugo enriba ao compilar, así que só hai que executalo se cambia o lema ou o logo |
| `escoller_xogo.sh` | A busca do xogo común a todos os instaladores de PC (só Linux): mira en Steam, Heroic, Lutris, Bottles, Wine e `~/Games`, pregunta en cal das copias e deixa escoller outra carpeta (busca dentro dela). Cada empaquetador métea tal cal no `instalar.sh`; as instrucións van na cabeceira |
| `videos_youtube.py` | Busca na canle de YouTube (o feed público, `[params.youtube]` de `web/hugo.toml`) o vídeo de cada xogo e pono na súa ficha (`video.youtube`, sección «En vídeo»). Vale se a descrición leva a ligazón á ficha ou se o título é «Turbo Review de <xogo>» coa plataforma da ficha. Execútao soa `.github/workflows/videos.yml` cada seis horas; `--probar` só di o que faría |

## Fluxo

```sh
python3 chk.py tr_xogo.ext xogo.tbl        # 0 problemas antes de empezar
TBL=xogo_gl.tbl python3 buildmap.py map1.tsv map2.tsv ...  # axusta lonxitudes
# ... inserir con Hextractor ...
python3 render.py parcheada.nes xogo_gl.tbl 0x2F910 proba.png "PREME START"  # revisión visual
python3 mkbps.py base.nes parcheada.nes parche.bps "descrición"
```

## Dúas trampas que xa custaron unha tarde

- **Ao recortar, nunca quitar un espazo solto entre dúas palabras**: pégaas
  ("Polassúas") e non se nota ata reextraer o texto da ROM. `fit.py` só toca
  recheos de dous ou máis espazos.
- Antes de traducir nada, **reinserir o `.ext` orixinal e comprobar que sae a
  ROM idéntica byte a byte**. Valida a ROM base, a táboa e os offsets nun
  minuto, e a partir de aí calquera fallo é da tradución.
