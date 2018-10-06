#!/usr/bin/python
from z3 import And , Not,Int ,Solver, sat ,simplify
from parser import parse_macros
from ast import bop,  VarTable
from lookup import LookupTable 


"""
1. _%d Token Generator for Reactive Pattern 

2. __%d Minterms token

"""


# A global variable for storing default input variable names to z3 variables mapping
variables = dict()

predicates = dict()

input_vars = set(
        [ 'ethDst' , 'ethSrc', 'ethType', 'ip4Dst' , 'ip4Src' , 'ipProto' , 'port_id' ,
            #Switch
            #"TCPDstPort","TCPSrcPort","Vlan","VlanPcp"
            ])


for input_var in input_vars:
    VarTable.insert(input_var,"int")
         



def getInitSolver():
    MAX_MAC = ((1<<48) -1)
    s = Solver()
    def add_range(s,var,minv,maxv):
        s.add( minv <= variables[var] )
        s.add( variables[var] <= maxv )

    add_range(s,'ethDst',0,MAX_MAC)
    add_range(s,'ethSrc',0,MAX_MAC)
    add_range(s,'ipProto',1,255)
    return s


"""
Return a list of predicates appear in the AST

"""



class StateVar:
    LAST_ID = 0
    def __init__(self,index = None):
        if(index is not None):
            self.id = index
        else:
            StateVar.LAST_ID+=1
            self.id = StateVar.LAST_ID
    def negate(self):
        return StateVar(-self.id)
    def gr1_repr(self):
        if(self.id > 0):
            return "(s%d)"%self.id
        else:
            return "(! s%d)"%(-self.id)


def check_sat(cond1,cond2):
    #print cond1, cond2
    s = getInitSolver()
    s = Solver()
    #s.add(cond1)
    s.add( And(cond1,cond2))
    if(s.check() ==  sat):
        return True
    return False



"""
    Per_Var_Minterm is a dictionary that collects lists of encodings for each vars
    per_var_minterm = { ip4Src : [[0,1], [1,1] ]  ip4Dst = : [ [..], ... ] } 
"""
per_var_minterms = dict()

def recurse_with_solver(solver,var,sofar,preds,depth,bitlist,minterms):
    ret = []
    if(depth == len(preds)):
        #print type(sofar),sofar
        sofar = simplify(sofar)
        print "minterm found" , sofar
        print "bitlist = ", bitlist

        minterm_id = len(per_var_minterms[var])
        per_var_minterms[var].append(bitlist)


        for i in range (len(bitlist)):
            b= bitlist[i]
            pred = preds[i]
            minterms[pred][b].append(minterm_id)

        return [sofar]
    solver.push()
    print "sofar = ", sofar, "preds =  " ,  preds[depth].toZ3(variables) , "depth = ",depth
    solver.add(preds[depth].toZ3(variables))
    if(solver.check()==sat):
        print "checking truth"
        ret += recurse_with_solver(
                solver,var,And(sofar,preds[depth].toZ3(variables))
                ,preds,depth+1,bitlist+[1],minterms
                )
    solver.pop()
    solver.push()
    solver.add( Not(preds[depth].toZ3(variables)))
    if(solver.check()==sat):
        print "checking false"
        ret +=  recurse_with_solver(
                solver,var,And(sofar,Not(preds[depth].toZ3(variables)))
                ,preds,depth+1,bitlist+[0],minterms
                )
    solver.pop()
    return ret





def conjuncts(a,b):
    return bop.create("and",a,b)


def disjuncts(a,b):
    return bop.create("or",a,b)


"""
    Returns a dictionary of list for each variable, contains the meaning of each minterm
    per_var_table {ip4Dst :  [And(ip4Dst==3,ip4Dst!=4), ... ] , ip4Src : [ And(...,...) ] }

"""


def get_minterm_table(per_var_minterms,predicates):
    per_var_table = dict()
    for var in per_var_minterms:
        per_var_table[var] = list()
        encodings  = per_var_minterms[var] 
        if(len(encodings)==0):
            continue
        for index, encoding in enumerate(encodings) :

            #print var,index,encodings

            minterm = reduce(conjuncts,[ predicates[var][bitindex] if bit ==0 else predicates[var][bitindex].negate() for bitindex,bit in enumerate(encoding)  ])
            per_var_table[var].append(minterm)
    return per_var_table


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
    for var in predicates:
        if( var not in input_vars):
            for pred in predicates[var]:
                ret += "\n"+pred.gr1_repr() +"\n"


    ret += "\n".join(inits)
    ret + "\n[ENV_TRANS]\n"
    ret +="\n[SYS_TRANS]\n"
    ret += "\n".join(trans)
    ret += "\n[ENV_LIVENESS]\n"
    ret +="\n[SYS_LIVENESS]\n"
    ret += "\n".join(lives)
    return ret


def write_gr1(macros,predicates,output_file):
    spec = "[INPUT]\n"
    for var in predicates:
        if( (var not in input_vars) ):
            continue
        for predicate in predicates[var]:
            spec += "i%s\n"% abs(predicate.id)
    spec += "[OUTPUT]\n"
    for var in predicates:
        if( (var in input_vars) ):
            continue
        for predicate in predicates[var]:
            spec += "o%s\n"% abs(predicate.id)

    for i in range(1,StateVar.LAST_ID+1):
        spec += "s%s\n"% i
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
            print var_type, var_name , var_value 
        else:
            print var_type, var_name
        VarTable.insert(var_name,var_type)


class Minterm():
    ID = 0
    def __init__(self,predicate_list):
        self.plist = predicate_list

def main():
    import sys


    if len(sys.argv)  < 4:
        print "usage : check_dependency.py <declaration> <ast_filename> <structured_slugs_filename>"
        exit(-1)
    else:
        #print sys.argv[1]

        for var in input_vars:
            variables[var] = Int(var)
            predicates[var] = list()
            per_var_minterms[var] = list() 

        declare_in = sys.argv[1] 
        parse_declaration(declare_in)
        ast_in = sys.argv[2]
        slug_out = sys.argv[3]
        
        macros = parse_macros(ast_in)
        """
            1. Collect from each macro the expressions that we need to examine,
               so 1 for invaraints and justice, 2 for precedence and 3 for reaction
        """
        for macro in macros:
            predicate_list = macro.getPredicates()
            #print len(preds),preds
            for predicate in predicate_list:
                #print "Original : ",pred
                #print "NNF : ", pred.nnf()
                if( predicate.var not in variables):
                    variables[predicate.var] = Int(predicate.var)
                    predicates[predicate.var] = list()
                    per_var_minterms[predicate.var] = list()
                predicates[predicate.var].append(predicate)
                #pred.toZ3(variables)

        """
            After this step , all predicates are grouped by variable name in a global dictionary
            For example

            predicates[Port] = (Port = 5 , Port > 3 , Port < 4)
            predicates[SrcIP] = (SrcIP != 6 )

        """
    
        minterms = dict()
        for var in predicates:
            preds = predicates[var]
            #if(len(preds)!=0):
            #    print "Available Predicats = ",predicates
            for pred in preds:
                minterms[pred] = list()
                minterms[pred].append(list())
                minterms[pred].append(list())
         
        for var in predicates:
            preds = predicates[var]
            print "var = ", var , "preds = ", preds
            if(len(preds)==0):
                continue
            s = getInitSolver()
            recurse_with_solver(s,var,And(True),preds,0,[],minterms)
            #for pred in predicates[var]:
                #print "negative mitnerms for predicate\n\t" ,pred , " len = ",len(minterms[pred][0])," = ",minterms[pred][0]
                #print ""
                #print "positive mitnerms for predicate\n\t" ,pred ,  " len = ",len(minterms[pred][1])," = ",minterms[pred][1]

        minterm_table = get_minterm_table(per_var_minterms,predicates)
        for var in predicates:
            print len(minterm_table[var]) ,len(per_var_minterms[var])

        rewrite_table = dict()
        for var in predicates:
            preds = predicates[var]
            if(len(preds)==0):
                continue
            print "\n\nvar = ", var 
            for pred in preds:
                #print minterms[pred][0]

                #print minterms[pred][1]
                #print len(minterm_table[var])
                """
                    For each predicate of the same var, replace them with the disjunctions of non-overlapping  atomic
                    propositions
                """
                rewrite_table [pred] = reduce(disjuncts,[ minterm_table[var][minterm_id] for minterm_id in minterms[pred][0]])

                #print "negative mitnerms for predicate\n\t" ,pred , " len = ",len(minterms[pred][0])," = ",minterms[pred][0]
                #print ""
                #print "positive mitnerms for predicate\n\t" ,pred ,  " len = ",len(minterms[pred][1])," = ",minterms[pred][1]
            for pred in predicates[var]:
                print "predicate = ", pred ," predicate id  = " ,pred.id
        for macro in macros:
            macro.rewrite(rewrite_table)
        write_gr1(macros,predicates,slug_out)
        
        dump_table = LookupTable(variables,input_vars,predicates)
        with open("test.db", "wb" ) as f:
            import pickle
            pickle.dump(dump_table,f)
        print dump_table
        #neg = minterms[var][0]
        #pos = minterms[var][1]
        #print "neg = ",neg
        #print "pos = ",pos
        #print macros[0].prop_ast
        #recurse_minterms(var,And(True),predicates[var],0,[])
        #print "var = ",var," num minterms = ",len(ret)
        #print "somtihng wrong"
        #compute_minterms(var,predicates[var])
main()

