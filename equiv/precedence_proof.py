#!/usr/bin/python3
import spot
precede= spot.formula(" ((F p) -> ( (!p) U ((!p) & e) ))")
gr1 = spot.formula(" (!e & !s & !p) & G( (!s & !e)->X(!s) ) &G(e->X(s))  & G((!s)->(!p)) & G(s->X(s))")

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






