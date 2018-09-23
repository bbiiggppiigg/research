#!/bin/bash
#./translate.py > tmp.structuredslugs
compiler.py tmp2.structuredslugs > fun.slugsin
#slugs fun.slugsin --symbolicStrategy test.sS
time slugs fun.slugsin --explicitStrategy test.strat
