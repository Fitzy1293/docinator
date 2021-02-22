#!/bin/env bash

echo "Creating out.md"
time (python3 cat_doc.py && pandoc out.md -t pdf -o out.pdf && echo 'ALL GOOD!!!!!')
