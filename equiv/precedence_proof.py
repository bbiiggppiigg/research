#!/usr/bin/python3
import spot
precede= spot.formula(" ((F after) -> ( (!after) U ((!after) & before) ))")
gr1 = spot.formula(" (!before & !s & !after) & G( (!s & !before)->X(!s) ) &G(before->X(s))  & G((!s)->(!after)) & G(s->X(s))")

def implies(f,g):
    a_f = f.translate()
    a_ng = spot.formula.Not(g).translate()
    return spot.product(a_f,a_ng)

r1= (implies(precede,gr1))
print (r1.is_empty())
print (r1.accepting_word())

r2= (implies(gr1,precede))
print (r2.is_empty())
print (r2.accepting_word())






