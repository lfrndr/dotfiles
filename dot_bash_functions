function mcd() {
    mkdir -p -- "$1" &&
        cd -P -- "$1"
}

function gh() { history | grep -i "$1"; }

function cl() {
    DIR="$*"
    # if no DIR given, go home
    if [ $# -lt 1 ]; then
        DIR=$HOME
    fi
    builtin cd "${DIR}" &&
        # use your preferred ls command
        # ls -F --color=auto
        ls -alFh --color=auto
}
