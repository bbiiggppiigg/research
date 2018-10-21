#!/bin/bash
fname="simplest"
fname="block"
path="example/"$fname"/$fname"
#./compiler $path".txt" > $path".ast"
./minterm.py $path".decl" $path".ast" $path".structured_slugs" $path."db" > tmp
compiler.py $path".structured_slugs" > $path".slugs"  
slugs --symbolicStrategy $path."slugs"  $path."symbolic" > tmp
#slugs --explicitStrategy $path."slugs"  $path."explicit"
./gen_frenetic.py $path".db" $path".symbolic" $path."py" #> $path".py"
#compiler.py block.structured_slugs > block.slug
