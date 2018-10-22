#!/bin/bash
fname="simplest"
#fname="block"
fname="liveness"
#fname="precedence"
path="example/"$fname"/$fname"

echo "Parsing Spec"
./compiler $path".txt" > $path".ast"
echo "Generating Structured Slugs"

./minterm.py $path".decl" $path".ast" $path".structured_slugs" $path."db" 
echo "End"
#compiler.py $path".structured_slugs" > $path".slugs"  
#echo "Generating Strategy"
#slugs --symbolicStrategy $path."slugs"  $path."symbolic" 
#slugs --explicitStrategy $path."slugs"  $path."explicit"
#echo "Generating Python" 
#./gen_frenetic.py $path".db" $path".symbolic" $path."py" #> $path".py"
