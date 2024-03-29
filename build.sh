#!/bin/sh

NOTE_ROOT=$(realpath "$(dirname "$0")")
export PATH="$NOTE_ROOT/bin:$PATH"

if [ -n "$1" ]; then
    FILES="$1"
    META_DOC="00-meta.md"
    if [ "$1" != "$META_DOC" ] && [ -f "$META_DOC" ]; then
        FILES="$META_DOC $1"
    fi
    OUT="$(echo "$1" | sed 's/\.[^\.]*$//')"
else
    FILES="$(ls ./*.md)"
    OUT="out"
fi

pandoc \
    --pdf-engine=xelatex \
    --pdf-engine-opt=-shell-escape \
    --template "$NOTE_ROOT/template.tex" \
    --top-level-division=chapter \
    --filter center.py \
    --filter example.py \
    --filter latexdivs.py \
    --filter makeindex.py \
    --filter python.py \
    --filter plantuml.py \
    --data-dir "$NOTE_ROOT" \
    ${FILES} -o "${OUT}.pdf"
