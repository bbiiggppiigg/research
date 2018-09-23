#!/bin/bash
#./translate.py > tmp.structuredslugs
compiler.py $1 > $1.slugsin
#slugs fun.slugsin --symbolicStrategy test.sS
time slugs $1.slugsin --symbolicStrategy $1.sym
