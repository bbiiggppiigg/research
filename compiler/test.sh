#!/bin/bash
fname="simplest"
#fname="block"
path="example/"$fname"/$fname"
./compiler $path".txt" > $path".ast"
./minterm.py $path".decl" $path".ast" $path".structured_slugs" 
#compiler.py $path".structured_slugs" > $path".slugs"
#slugs --symbolicStrategy $path."slugs"  $path."symbolic"
#./gen_frenetic.py $path".symbolic" > $path".py"
#compiler.py block.structured_slugs > block.slug
