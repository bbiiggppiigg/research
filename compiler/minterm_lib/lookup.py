from ast import Z3VarTable, PredicateTable
class LookupTable():
    
    def __init__(self):
        #self.variables = variables 
        self.vars = [var for var in Z3VarTable.z3table]
        self.predicates = PredicateTable.get_all()

    def __repr__(self):
        return "vars = %s , predicates = %s "%(self.vars ,self.predicates)

    def is_input(self,varname):
        tmp = varname.split("'")[0]
        tmp = tmp.split("@")[0]
        for var in self.vars:
            if(var.name == tmp):
                return var.is_input
        return False
