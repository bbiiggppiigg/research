#!/bin/bash
fname="block"
path="example/"$fname"/$fname"
./compiler $path".txt" > $path".ast"
./minterm.py $path".ast" 
compiler.py $path".structured_slugs" > $path".slugs"
#compiler.py block.structured_slugs > block.slug
