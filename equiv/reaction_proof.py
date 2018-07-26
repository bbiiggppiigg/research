#!/usr/bin/python3
import spot
from functools import reduce

ltl = spot.formula("G(trigger -> X(policy  W (!trigger & terminate & callback)))")
GR1 = (
[
"!triggered",
"G((trigger | (triggered & !terminate))<-> X(triggered))",
"G(triggered -> policy)",
"G((!trigger & terminate ) -> callback)"
])
translated_gr1 = (reduce(lambda x,y : spot.product(x,y) ,map(spot.translate,map(spot.formula,GR1))))
ltl_n = spot.formula.Not(ltl).translate()
ans = spot.product(translated_gr1,ltl_n)
print (ans.is_empty())
print (ans.accepting_word())







