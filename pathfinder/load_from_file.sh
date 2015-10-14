#!/bin/bash

# Partially sourced by @konsolebox at stackexchange
# http://unix.stackexchange.com/questions/149726/how-to-pass-each-line-of-a-text-file-as-an-argument-to-a-command

while IFS= read -r LINE; do
    python pathfinder.py "$LINE"
done < example_tables
