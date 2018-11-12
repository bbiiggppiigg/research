from ast import StateVarTable

class Invariant:
    def __init__(self,prop_ast):
        self.prop_ast = prop_ast

    def collect_gr1(self):
        prop_str = self.prop_ast.gr1_repr()

        return  [],[prop_str],[] 

class Reaction:

    def collect_gr1(self):
        init =  [self.s.negate().gr1_repr()]
        s = self.s.gr1_repr()
        C = self.C.gr1_repr()
        B = self.B.gr1_repr()
        A = self.A.gr1_repr()
        trans = [
        "(%s | (%s & (!%s))) <-> X(%s)"%(A,s,C,s),
        "(%s -> %s)" % (s,B)
        ]
        """
        trans = [
                "(%s | (%s & (!%s))) <-> X(%s)"%(A,s,C,s),
                ]
        """
        return init, trans , []


    def __init__(self,A,B,C):

        self.A = A
        self.B = B
        self.C = C

        self.s = StateVarTable.create()



    #return [self.trigger,self.policy,self.terminate]

class Justice:

    def __init__(self,prop_ast):
        self.prop_ast = prop_ast

    def collect_gr1(self):
        #liveness = ["%s"%self.prop_ast.gr1_repr()]
        liveness_repr = self.prop_ast.gr1_repr()
        liveness = [liveness_repr]
        return [],[],liveness
class Precedence:

    def __init__(self,before_ast,after_ast):
        self.before_ast = before_ast
        self.after_ast = after_ast
        self.happened = StateVarTable.create()

    def collect_gr1(self):
        before_repr = self.before_ast.gr1_repr()
        after_repr = self.after_ast.gr1_repr()
        happen_repr = self.happened.gr1_repr()
       
        init = [("!(%s) & !(%s)"%(after_repr,happen_repr)) ]

        trans = [
                    "(!(%s) & !(%s)) -> X(!(%s))"%(happen_repr,before_repr,happen_repr),
                    "(%s) -> X(%s)"%(before_repr,happen_repr),
                    "!(%s) -> !(%s)"%(happen_repr,after_repr),
                    "(%s) -> X(%s)"%(happen_repr,happen_repr)
                    ]
                
        return init, trans , []



