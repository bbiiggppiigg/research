#!/usr/bin/python
from z3 import And , Not ,Solver, sat ,simplify
from parser import parse_macros
from ast import   Z3VarTable,PredicateTable, Bop
from lookup import LookupTable 


"""
1. _%d Token Generator for Reactive Pattern 

2. __%d Minterms token

"""


# A global variable for storing default input variable names to z3 variables mapping


input_vars = set(
        [ 'ethDst' , 'ethSrc', 'ethType', 'ip4Dst' , 'ip4Src' , 'ipProto' , 'port_id' ,
            #Switch
            #"TCPDstPort","TCPSrcPort","Vlan","VlanPcp"
            ])

def getInitSolver():
    #MAX_MAC = ((1<<48) -1)
    s = Solver()
    """
    def add_range(s,name,minv,maxv):
        var = Z3VarTable.getvar(name)
        s.add( minv <= Z3VarTable.get(var) )
        s.add( Z3VarTable.get(var) <= maxv )
    """
    #add_range(s,'ethDst',0,MAX_MAC)
    #add_range(s,'ethSrc',0,MAX_MAC)
    #add_range(s,'ipProto',1,255)
    return s


"""
Return a list of predicates appear in the AST

"""




class Minterm(object):
    def __init__(self,var,predicate_list,mid):
        self.var = var
        self.pred_list = predicate_list;
        self.id = mid
    def __repr__(self):
        return " && ".join( map( lambda x : x.__repr__() , self.pred_list))
    def gr1_repr(self):
        return "%s = %d"%(self.var,self.id)
    pass


class PredicateMintermMap(object):
    table = dict()

    @classmethod
    def insert_mapping(cls,predicate,minterm):
        if (predicate not in cls.table):
            cls.table[predicate] = list()
        cls.table[predicate].append(minterm)
    pass
    
    @classmethod
    def dump(cls):
        print "!!!!!!!!!!!!!! Dumping Mapping !!!!!!!!!!!!!!!!"
        for var in PredicateTable.table:
            if(var.ast_type == "bool"):
                continue
            for predicate in PredicateTable.table[var]:
                print "predicate =  %-*s, miterm = [%-*s]"%(5,predicate,5,(cls.table[predicate]))
        print "!!!!!!!!!!!!!! End Dumping Mapping !!!!!!!!!!!!"

class PerVarMinterm(object):

    def __init__(self,var):
        self.var = var
        self.minterms = list()


class MintermTable(object):
    table = dict()
     
    
    @classmethod 
    def insert(cls,var,predicates):
        if( var not in cls.table ):
            MintermTable.table[var] = list()
        new_id = len(MintermTable.table[var]) 
        minterm = Minterm(var,predicates,new_id)
        MintermTable.table[var].append(minterm)
        return minterm
    @classmethod
    def get_define(cls):
        inputs = []
        outputs = []
        for var in cls.table:
            if (var.is_input):
                inputs.append((var,len(cls.table[var])))
            else:
                outputs.append((var,len(cls.table[var])))
        return inputs,outputs
    
    @classmethod
    def dump(cls):
        print "!!! Dumping Minterm Table !!!"
        for var in cls.table:
            for minterm in cls.table[var]:
                print "%-*s       %-*s"%(10,var,20,minterm)
        print "!!! End of Dumping Minterm Table !!!"
    pass



"""
    Per_Var_Minterm is a dictionary that collects lists of encodings for each vars
    per_var_minterm = { ip4Src : [[0,1], [1,1] ]  ip4Dst = : [ [..], ... ] } 
"""


def gen_minterm(solver, var, predicates, depth , limit):
    
    if (solver.check() != sat):
        #print predicates
        return
    if (depth == limit):
        #print solver.model()
        #minterm = Minterm(predicates) 
        minterm = MintermTable.insert(var,predicates)
        for predicate in predicates:
            PredicateMintermMap.insert_mapping(predicate,minterm)

        return 

    
    pred = PredicateTable.table[var][depth]
   
    """
        Case by Case analysis
        a). pred not duplicate: Label 1 and Label 3 get executuede
        b). pred in predicates -> not pred not in predicates =>
            Label 2 and Label 3 get executed
        c). not pred in predicates -> pred not in predicates => # Label 1 and 4 get executed

    """
    if( pred not in predicates): # Label 1
        solver.push()
        solver.add( pred.toZ3())
        gen_minterm(solver,var, predicates + [pred] , depth+1 , limit)
        solver.pop()
    else: # Label 2
        gen_minterm(solver,var, predicates , depth+1 , limit)
    
    if (pred.negate() not in predicates):  # Label 3
        solver.push()
        solver.add( pred.negate().toZ3())
        gen_minterm(solver,var, predicates + [pred.negate()] , depth+1 , limit)
        solver.pop()
    else: #Label 4
        gen_minterm(solver,var, predicates , depth+1 , limit)
    



def conjuncts(a,b):
    return Bop.create("and",a,b)


def disjuncts(a,b):
    return Bop.create("or",a,b)


"""
    Returns a dictionary of list for each variable, contains the meaning of each minterm
    per_var_table {ip4Dst :  [And(ip4Dst==3,ip4Dst!=4), ... ] , ip4Src : [ And(...,...) ] }

"""


def collect_gr1(macros):
    inits = []
    trans = []
    lives = []
    for macro in macros:
        init , tran , live = macro.collect_gr1()
        inits += init
        trans += tran
        lives += live
    ret = "[ENV_INIT]\n"
    ret +="[SYS_INIT]\n"
    """
    for var in PredicateTable.table:
        if (not var.is_input):
            for pred in PredicateTable.table[var]:
                ret += "\n"+pred.gr1_repr() +"\n"

    """
    ret += "\n".join(inits)
    ret + "\n[ENV_TRANS]\n"
    ret +="\n[SYS_TRANS]\n"
    ret += "\n".join(trans)
    ret += "\n[ENV_LIVENESS]\n"
    ret +="\n[SYS_LIVENESS]\n"
    ret += "\n".join(lives)
    return ret


def write_gr1(macros,output_file):
    
    inputs, outputs = MintermTable.get_define() 
    spec = "[INPUT]\n"
    for inp in inputs:
        spec += "%s:0...%d\n"%(inp[0],inp[1])
    for var in Z3VarTable.z3table:
        if(var.is_input and var.ast_type == "bool"):
            spec += "%s\n"%var

    spec += "[OUTPUT]\n"
    for oup in outputs:
        spec += "%s:0...%d\n"%(oup[0],oup[1])
    for var in Z3VarTable.z3table:
        if( (not var.is_input) and var.ast_type == "bool"):
            spec += "%s\n"%var

   
    """
    for i in range(1,StateVar.LAST_ID+1):
        spec += "s%s\n"% i
    """
    spec += collect_gr1(macros)
    with open (output_file,"w") as f:

        f.write(spec)


def parse_declaration(filename):
    with open(filename) as f:
        lines = f.readlines()

    for line in lines:
        var_type, var_name = line.strip().split()
        if "=" in var_name:
            var_name, var_value = var_name.split("=")
            #print var_type, var_name , var_value 
        #else:
            #print var_type, var_name
        Z3VarTable.insert(var_name,var_type)



import sys
def usage():
    if len(sys.argv)  < 4:
        print "usage : check_dependency.py <declaration> <ast_filename> <structured_slugs_filename>"
        exit(-1)

def setup_vartable(declare_in):
    for var in input_vars:
        #print var
        Z3VarTable.insert(var,"int",True)
    Z3VarTable.insert("CONST_TRUE","bool",True)
    Z3VarTable.insert("CONST_FALSE","bool",True)

    parse_declaration(declare_in)
    
    variables = Z3VarTable.vartable
    for name in (variables):
        var = variables[name]


def generate_minterms():
    
    for var in PredicateTable.table:
        if(var.ast_type == "bool"):
            continue
        preds = PredicateTable.table[var]
        if(len(preds)==0):
            continue
        print "generating minterm for variable ",var
        s = getInitSolver()
        gen_minterm(s,var,[],0,len(preds))



def main():
    usage()
    declare_in = sys.argv[1] 
    ast_in = sys.argv[2]
    slug_out = sys.argv[3]

    setup_vartable(declare_in) 
    macros = parse_macros(ast_in)
    """
        1. Collect from each macro the expressions that we need to examine,
           so 1 for invaraints and justice, 2 for precedence and 3 for reaction
    """
    """
        After this step , all predicates are grouped by variable name in a global dictionary
        For example

        predicates[Port] = (Port = 5 , Port > 3 , Port < 4)
        predicates[SrcIP] = (SrcIP != 6 )

    """
    #collect_predicates(macros)
    #PredicateTable.dump()
    #Z3VarTable.dump()
    
    
    generate_minterms()
    MintermTable.dump()
    PredicateMintermMap.dump()
    """
    for var in PredicateTable.table:
        for predicate in PredicateTable.table[var]:
            print "predicate =" , predicate , "gr1_repr = ",predicate.gr1_repr()
    """
    write_gr1(macros,slug_out)
    
    dump_table = LookupTable()
    with open("test.db", "wb" ) as f:
        import pickle
        pickle.dump(dump_table,f)
main()

