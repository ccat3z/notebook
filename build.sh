#!/bin/sh

export OLD_PATH="$PATH"
export PATH="./bin:$PATH"

if [ -n "$1" ]; then
    FILES="$1"
    OUT="$(echo $1 | sed 's/\.[^\.]*$//')"
else
    FILES="$(ls *.md)"
    OUT="out"
fi

pandoc --pdf-engine=xelatex --pdf-engine-opt=-shell-escape --template template.tex --top-level-division=chapter --filter example.py --filter latexdivs.py --filter makeindex.py --data-dir . ${FILES} -o ${OUT}.pdf
