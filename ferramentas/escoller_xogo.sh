# >>> escoller_xogo: común a todos os instaladores de Enxebre Traducións
# A copia boa está en enxebre-traducions/ferramentas/escoller_xogo.sh. Cada empaquetador métea tal cal
# no instalar.sh do xogo, e o desinstalar.sh lea de alí (entre estas dúas liñas de marca).
#
# Antes de usala, o instalador define:
#   XOGO_NOME     nome para as mensaxes                     («Suzerain»)
#   XOGO_STEAM    carpeta dentro de steamapps/common        («Suzerain»)
#   XOGO_MARCA    ruta que leva o xogo, relativa á súa carpeta, para buscalo con find
#                 («Suzerain_Data», «config/English.lang»)
#   e_o_xogo DIR  función: correcta se DIR é de verdade a carpeta do xogo
# Xusto despois do bloque (fóra das marcas, para que o desinstalador non o colla):
#              xogo_abrir_terminal "$AQUI/instalar.sh" "$@"
# e despois:  XOGO="$(escoller_xogo "${1:-}")" || fallo "..."
# Para preguntar antes de seguir (por exemplo, se a copia non é a versión probada):
#              xogo_confirmar "Instalar igualmente? Escribe s e preme Intro: " || fallo "..."
#
# Sen argumento busca en Steam, Heroic (GOG, Epic, Amazon e os engadidos a man), o lanzador de Epic,
# Lutris, Bottles, Wine, itch e ~/Games, e deixa escoller entre o atopado ou outra carpeta (cunha xanela
# se hai escritorio). Se a carpeta escollida non é a do xogo, búscao dentro: vale o disco ou o prefixo.
# As preguntas van á terminal (stderr); por stdout só sae a carpeta escollida.

_xogo_dentro() {  # _xogo_dentro DIR FONDO ORIXE: «carpeta<TAB>orixe» por cada copia en DIR ata FONDO niveis
    local dir="$1" fondo="$2" orixe="$3" atopado barras i
    if [ ! -d "$dir" ]; then return 0; fi
    if e_o_xogo "$dir"; then printf '%s\t%s\n' "$dir" "$orixe"; return 0; fi
    barras="${XOGO_MARCA//[^\/]/}"
    while IFS= read -r -d '' atopado; do
        for ((i = 0; i <= ${#barras}; i++)); do atopado="${atopado%/*}"; done
        if e_o_xogo "$atopado"; then printf '%s\t%s\n' "$atopado" "$orixe"; fi
    done < <(find "$dir" -maxdepth $((fondo + ${#barras} + 1)) \
                \( -path '*/drive_c/windows' -o -path '*/steamapps/compatdata' -o -path '*/steamapps/shadercache' \
                   -o -name .git -o -name node_modules \) -prune \
                -o -ipath "*/$XOGO_MARCA" -print0 2>/dev/null)
}

_xogo_candidatos() {  # as copias que hai nos sitios habituais
    local raiz lib f ruta
    # Steam (tamén Flatpak e Snap) e as súas outras bibliotecas
    for raiz in "$HOME/.local/share/Steam" "$HOME/.steam/steam" "$HOME/.steam/root" \
                "$HOME/.var/app/com.valvesoftware.Steam/.local/share/Steam" \
                "$HOME/snap/steam/common/.local/share/Steam"; do
        if [ ! -d "$raiz/steamapps" ]; then continue; fi
        while IFS= read -r lib; do
            if e_o_xogo "$lib/steamapps/common/$XOGO_STEAM"; then
                printf '%s\tSteam\n' "$lib/steamapps/common/$XOGO_STEAM"
            fi
        done < <(echo "$raiz"
                 if [ -f "$raiz/steamapps/libraryfolders.vdf" ]; then
                     sed -n 's/^[[:space:]]*"path"[[:space:]]*"\(.*\)"[[:space:]]*$/\1/p' "$raiz/steamapps/libraryfolders.vdf"
                 fi)
    done
    # Heroic e o lanzador de Epic: as rutas de instalación dos seus JSON
    for f in "$HOME"/.config/heroic/{gog_store,legendaryConfig/legendary,nile_config/nile}/installed.json \
             "$HOME"/.config/heroic/sideload_apps/library.json \
             "$HOME"/.var/app/com.heroicgameslauncher.hgl/config/heroic/{gog_store,legendaryConfig/legendary,nile_config/nile}/installed.json \
             "$HOME"/.var/app/com.heroicgameslauncher.hgl/config/heroic/sideload_apps/library.json \
             "$HOME"/.local/share/com.epicgames.eglv2/installations.jsonl; do
        if [ ! -f "$f" ]; then continue; fi
        case "$f" in *eglv2*) orixe=Epic ;; *) orixe=Heroic ;; esac
        while IFS= read -r ruta; do
            _xogo_dentro "$ruta" 1 "$orixe"
        done < <(grep -o '"\(install_path\|folder_name\|path\|installLocation\)"[[:space:]]*:[[:space:]]*"/[^"]*"' "$f" |
                 sed 's/^[^:]*:[[:space:]]*"\(.*\)"$/\1/')
    done
    # Lutris: o executable ou o prefixo de cada xogo
    for f in "$HOME"/.local/share/lutris/games/*.yml "$HOME"/.config/lutris/games/*.yml \
             "$HOME"/.var/app/net.lutris.Lutris/data/lutris/games/*.yml; do
        if [ ! -f "$f" ]; then continue; fi
        while IFS= read -r ruta; do
            ruta="${ruta%\"}"; ruta="${ruta#\"}"; ruta="${ruta%\'}"; ruta="${ruta#\'}"
            if [ -f "$ruta" ]; then ruta="${ruta%/*}"; fi
            _xogo_dentro "$ruta" 5 Lutris
        done < <(sed -n 's/^[[:space:]]*\(exe\|prefix\|working_dir\|game_path\):[[:space:]]*\(.*\/.*\)$/\2/p' "$f")
    done
    # prefixos de Bottles e de Wine, a aplicación de itch e as carpetas de xogos de sempre
    for ruta in "$HOME"/.local/share/bottles/bottles/*/drive_c \
                "$HOME"/.var/app/com.usebottles.bottles/data/bottles/bottles/*/drive_c; do
        _xogo_dentro "$ruta" 4 Bottles
    done
    _xogo_dentro "$HOME/.wine/drive_c" 4 Wine
    _xogo_dentro "$HOME/.config/itch/apps" 2 itch
    for ruta in "$HOME/Games" "$HOME/games" "$HOME/Xogos" "$HOME/Juegos"; do
        _xogo_dentro "$ruta" 4 "~/${ruta##*/}"
    done
}

_xogo_ler() {  # _xogo_ler VARIABLE PREGUNTA: le unha liña da terminal; falla se non hai terminal
    local _resposta
    IFS= read -r -e -p "$2" _resposta || return 1
    printf -v "$1" '%s' "$_resposta"
}

xogo_abrir_terminal() {  # xogo_abrir_terminal GUION [ARGUMENTOS]: se o abriron con dobre clic (sen terminal),
                         # volve abrir o guion nunha xanela de terminal, que espera un Intro antes de pecharse
    local t msg
    local -a orde=()
    if [ -n "${ENXEBRE_XANELA:-}" ]; then
        trap 'echo; echo "Preme Intro para pechar esta xanela."; read -r _ || true' EXIT
        return 0
    fi
    if [ -t 0 ] || [ -t 1 ] || [ -t 2 ] || [ -z "${WAYLAND_DISPLAY:-}${DISPLAY:-}" ]; then return 0; fi
    case "${XDG_CURRENT_DESKTOP:-}" in
        *KDE*) orde=(konsole) ;;
        *GNOME*) orde=(kgx ptyxis gnome-terminal) ;;
        *XFCE*) orde=(xfce4-terminal) ;;
        *MATE*) orde=(mate-terminal) ;;
        *LXQt*) orde=(qterminal) ;;
    esac
    orde+=(xdg-terminal-exec x-terminal-emulator konsole kgx ptyxis gnome-terminal xfce4-terminal
           mate-terminal qterminal terminator alacritty kitty foot wezterm xterm)
    for t in "${orde[@]}"; do
        if ! command -v "$t" >/dev/null 2>&1; then continue; fi
        case "$t" in
            xdg-terminal-exec | kitty | foot) exec "$t" env ENXEBRE_XANELA=1 bash "$@" ;;
            kgx | ptyxis | gnome-terminal) exec "$t" -- env ENXEBRE_XANELA=1 bash "$@" ;;
            xfce4-terminal | mate-terminal | terminator) exec "$t" -x env ENXEBRE_XANELA=1 bash "$@" ;;
            wezterm) exec "$t" start -- env ENXEBRE_XANELA=1 bash "$@" ;;
            *) exec "$t" -e env ENXEBRE_XANELA=1 bash "$@" ;;
        esac
    done
    # sen ningunha terminal, polo menos que se vexa o porqué
    msg="Non atopo ningunha terminal. Abre unha nesta carpeta e escribe: bash ${1##*/}"
    kdialog --error "$msg" 2>/dev/null || zenity --error --text="$msg" 2>/dev/null || true
    exit 1
}

xogo_confirmar() {  # xogo_confirmar PREGUNTA: correcta só se responde «s»; sen terminal, non
    local resposta=""
    _xogo_ler resposta "$1" || return 1
    resposta="${resposta//[[:space:]]/}"
    case "${resposta,,}" in s | si | sí) return 0 ;; *) return 1 ;; esac
}

_xogo_elixir() {  # _xogo_elixir CARPETAS ORIXES: menú numerado, co 0 para outra carpeta
    local -n _carpetas="$1" _orixes="$2"
    local i n resposta ver
    echo >&2
    echo "Atopei $XOGO_NOME en:" >&2
    for i in "${!_carpetas[@]}"; do
        # a carpeta persoal como ~, que se le mellor
        ver="${_carpetas[$i]/#"$HOME"\//\~/}"
        if [ -n "${_orixes[$i]}" ]; then
            printf '  %d) %s   [%s]\n' $((i + 1)) "$ver" "${_orixes[$i]}" >&2
        else
            printf '  %d) %s\n' $((i + 1)) "$ver" >&2
        fi
    done
    echo "  0) Está noutra carpeta" >&2
    while :; do
        if ! _xogo_ler resposta "Escribe o número e preme Intro [1]: "; then
            # sen terminal só se segue se non hai dúbida
            if [ ${#_carpetas[@]} -eq 1 ]; then printf '%s\n' "${_carpetas[0]}"; return 0; fi
            echo "Hai máis dunha copia e non hai terminal onde preguntar cal." >&2
            return 1
        fi
        resposta="${resposta//[[:space:]]/}"
        if [ -z "$resposta" ]; then resposta=1; fi
        if [[ "$resposta" =~ ^[0-9]+$ ]]; then
            n=$((10#$resposta))
            if [ "$n" -eq 0 ]; then _xogo_outra; return; fi
            if [ "$n" -le ${#_carpetas[@]} ]; then printf '%s\n' "${_carpetas[$((n - 1))]}"; return 0; fi
        fi
        echo "Escribe un número do 0 ao ${#_carpetas[@]}." >&2
    done
}

_xogo_buscar_en() {  # _xogo_buscar_en DIR: o xogo en DIR ou dentro del
    local dir="$1" atopado orixe
    local -a atopados=() orixes=()
    # o que deixa unha terminal ao arrastrar unha carpeta: espazos, comiñas ou file://
    dir="${dir#"${dir%%[![:space:]]*}"}"; dir="${dir%"${dir##*[![:space:]]}"}"
    case "$dir" in \'*\' | \"*\") dir="${dir:1:${#dir}-2}" ;; esac
    if [[ "$dir" == file://* ]]; then dir="${dir#file://}"; dir="$(printf '%b' "${dir//%/\\x}")"; fi
    if [[ "$dir" == "~" || "$dir" == "~/"* ]]; then dir="$HOME${dir:1}"; fi
    if [ "$dir" != / ]; then dir="${dir%/}"; fi
    if [ -z "$dir" ]; then echo "Non escolliches ningunha carpeta." >&2; return 1; fi
    if [ ! -d "$dir" ]; then echo "Non existe a carpeta «$dir»." >&2; return 1; fi
    if e_o_xogo "$dir"; then printf '%s\n' "$dir"; return 0; fi
    echo "Buscando $XOGO_NOME dentro de «$dir»..." >&2
    while IFS=$'\t' read -r atopado orixe; do
        atopados+=("$atopado"); orixes+=("")
    done < <(_xogo_dentro "$dir" 6 "")
    case ${#atopados[@]} in
        0) echo "Non atopo $XOGO_NOME dentro de «$dir»." >&2; return 1 ;;
        1) printf '%s\n' "${atopados[0]}" ;;
        *) _xogo_elixir atopados orixes ;;
    esac
}

_xogo_outra() {  # pide a carpeta (cunha xanela se pode) e busca o xogo nela
    local dir=""
    echo >&2
    echo "Escolle a carpeta onde está $XOGO_NOME." >&2
    echo "Vale tamén unha que a conteña, como un disco ou un prefixo de Wine: xa o busco eu dentro." >&2
    if [ -n "${WAYLAND_DISPLAY:-}${DISPLAY:-}" ]; then
        if command -v kdialog >/dev/null 2>&1 && [[ "${XDG_CURRENT_DESKTOP:-}" == *KDE* ]]; then
            dir="$(kdialog --title "Onde está $XOGO_NOME?" --getexistingdirectory "$HOME" 2>/dev/null)" || dir=""
        elif command -v zenity >/dev/null 2>&1; then
            dir="$(zenity --file-selection --directory --title="Onde está $XOGO_NOME?" --filename="$HOME/" 2>/dev/null)" || dir=""
        elif command -v kdialog >/dev/null 2>&1; then
            dir="$(kdialog --title "Onde está $XOGO_NOME?" --getexistingdirectory "$HOME" 2>/dev/null)" || dir=""
        fi
    fi
    if [ -z "$dir" ]; then
        if ! _xogo_ler dir "Escribe a carpeta (ou arrástraa aquí) e preme Intro; baleiro para saír: "; then
            echo "Non hai terminal onde preguntar." >&2
            return 1
        fi
    fi
    _xogo_buscar_en "$dir"
}

escoller_xogo() {  # escoller_xogo [CARPETA]: escribe a carpeta do xogo
    local dir orixe real
    local -a atopados=() orixes=()
    local -A visto=()
    if [ -n "${1:-}" ]; then _xogo_buscar_en "$1"; return; fi
    echo "Buscando $XOGO_NOME (Steam, Heroic, Lutris, Bottles, Wine, ~/Games...)" >&2
    while IFS=$'\t' read -r dir orixe; do
        real="$(realpath -m -- "$dir")"
        if [ -z "${visto[$real]:-}" ]; then
            visto[$real]=1; atopados+=("$dir"); orixes+=("$orixe")
        fi
    done < <(_xogo_candidatos)
    if [ ${#atopados[@]} -eq 0 ]; then
        echo "Non o atopei nos sitios habituais." >&2
        _xogo_outra
        return
    fi
    _xogo_elixir atopados orixes
}
# <<< escoller_xogo
