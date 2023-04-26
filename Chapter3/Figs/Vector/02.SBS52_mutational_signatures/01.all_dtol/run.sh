#!/bin/bash

while read line
do
    python /Users/sl666/Github/himut/scripts/dump_mutational_spectrum.py -i $line.tsv --sample DTOL_$line -o $line.pdf
done < input.fofn
