#!/usr/bin/python3
import spot
from functools import reduce

ltl = spot.formula("((F after) -> ((!after) U (!after) & before))")
GR1 = (
[
"!after & !happened", 
"G( (!happened & !after) -> X(!happened))",
"G( before -> X(happened))",
"G(!happened->!after)",
"G(happened -> X(happened))"
])
translated_gr1 = (reduce(lambda x,y : spot.product(x,y) ,map(spot.translate,map(spot.formula,GR1))))
ltl_n = spot.formula.Not(ltl).translate()
ans = spot.product(translated_gr1,ltl_n)
print (ans.is_empty())
print (ans.accepting_word())







