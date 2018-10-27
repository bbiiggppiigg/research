from ast import StateVarTable

class Invariant:
    def __init__(self,prop_ast):
        self.prop_ast = prop_ast

    def collect_gr1(self):
        prop_str = self.prop_ast.gr1_repr()

        return  [],[prop_str],[] 

class Reaction:

    def collect_gr1(self):
        init =  [self.triggered.negate().gr1_repr()]
        triggered = self.triggered.gr1_repr()
        terminate = self.terminate_ast.gr1_repr()
        policy =self.policy_ast.gr1_repr()
        trigger = self.trigger_ast.gr1_repr()
        trans = [
                "(%s | (%s & !(%s))) <-> X(%s)"%(trigger,triggered,terminate,triggered),
                "(%s)->(%s)"%(triggered,policy),
                ]
        return init, trans , []


    def __init__(self,trigger_ast,policy_ast,terminate_ast):

        self.trigger_ast = trigger_ast
        self.policy_ast = policy_ast
        self.terminate_ast = terminate_ast

        self.triggered = StateVarTable.create()



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



