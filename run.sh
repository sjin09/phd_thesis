#!/bin/bash

make clean
makeindex thesis.nlo -s nomencl.ist -o thesis.nls
make
ps2ascii thesis.pdf | wc -w
