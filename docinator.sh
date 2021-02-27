#!/bin/sh

echo "Running pandoc"
pandoc -f markdown ./markdown/title.md ./markdown/content/*.md -o markdown.pdf
