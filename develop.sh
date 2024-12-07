#!/usr/bin/env bash

program="$1"
infile="${2:-sample.in}"

echo -e "${program}\n${infile}\ndata.in" | entr -ncrs "echo -e '\n${infile}:' && pypy3 ${program} < ${infile} && echo -e '\ndata.in:' && pypy3 ${program} < data.in"
