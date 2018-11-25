#!/usr/bin/python
from z3 import Solver, sat , And, Not
from parser import parse_macros
from ast import   Z3VarTable,PredicateTable, StateVarTable
from flag import DEBUG

"""
1. _%d Token Generator for Reactive Pattern 

2. __%d Minterms token

"""


# A global variable for storing default input variable names to z3 variables mapping


#DEBUG = False        
#DEBUG = True 

def getInitSolver(var):
    s = Solver()
    if ( var.min_max is not None):
        print "adding min_max for ",var
        min_value, max_value = var.min_max
        z3var = Z3VarTable.get(var)
        s.add(min_value <= z3var )
        s.add( z3var <= max_value)
    return s


"""
Return a list of predicates appear in the AST

"""
class ActionTable(object):
    pass


import ipaddress
class Minterm(object):
    builtin_action = dict()
    builtin_action['ethDst']="SetEthDst(%s)"
    builtin_action['ethSrc']="SetEthSrc(%s)"
    builtin_action['ethType']="SetEthType(%s)"
    builtin_action['ip4Src']="SetIP4Src(%s)"
    builtin_action['ip4Dst']="SetIP4Dst(%s)"
    builtin_action['Port']="SetPort (%s)"
    builtin_action['ipProto']="SetIPProto(%s)" 

    builtin_predicate = dict()

    builtin_predicate['ethDst']=" pkt.ethDst  == %s "
    builtin_predicate['ethSrc']=" pkt.ethSrc == %s"

    builtin_predicate['ip4Src']="pkt.ip4Src == %s"
    builtin_predicate['ip4Dst']="pkt.ip4Dst == %s"

    builtin_predicate['port_id']="port_id ==  %s"

    builtin_predicate['ipProto']="pkt.ipProto == %s"



  
    def __init__(self,var,predicate_list,mid,some_value):
        self.var = var
        self.pred_list = predicate_list;
        self.id = mid
        if (self.var.ast_type == "bool"):
            self.z3value = some_value
        elif(var.ast_type == "ip"):
            self.z3value = '"%s"'%( ipaddress.IPv4Address(some_value.as_long()))
        else:
            self.z3value = some_value.as_long()

    def __repr__(self):
        return " && ".join( map( lambda x : x.__repr__() , self.pred_list))
    def gr1_repr(self):
        return "%s = %d"%(self.var,self.id)
    def fr_encoding(self):
        #if (isprime):
        return "%s == %d"%(self.var.name,self.id)
        assert(False)
        #return "self.nib.%s%d"%(self.var.name,self.id)

    def fr_predicate(self,isprime = False):
        # TODO DEBUG
        if(DEBUG):
            if (isprime):
                return "%s%d"%(self.var.name,self.id)
            return "nib.%s%d"%(self.var.name,self.id)
            
        if ( isprime) :
            if( self.var.name in self.builtin_predicate):
                ret =  " and ".join(map (lambda x : x.fr_predicate() , self.pred_list))
                ret = "(%s)"%ret
                return ret
            else:
                # TODO : Not sure what to deal with this situation
                return ""
                #return "self.nib.%s%d"%(self.var.name,self.id)
                pass
        else:
            return "nib.%s == %d"%(self.var.name,self.id)

    def fr_action_update(self):
        return "nib.%s = %d" % (self.var.name,self.id)
    
    def fr_update(self):
        return "nib.%s = %s" % (self.var.name,self.z3value)
    
    def fr_action(self):
        name = self.var.name
        value = self.z3value
        if(name in self.builtin_action):
            
            action =  self.builtin_action[name]%(value)
            if(DEBUG):
                action =  self.builtin_action[name]%(self.id) #TODO DEBUG
            return "actions += [%s]"%action
        return "nib.%s = %s " % ( name ,value)

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


# Indexed by var
class MintermTable(object):
    table = dict()
     
    
    @classmethod 
    def insert(cls,var,predicates,some_value):
        if( var not in cls.table ):
            MintermTable.table[var] = list()
        new_id = len(MintermTable.table[var]) 
        minterm = Minterm(var,predicates,new_id,some_value)
        cls.table[var].append(minterm)
        return minterm
    @classmethod
    def get_define(cls):
        inputs = []
        outputs = []
        for var in cls.table:
            if (var.is_input):
                inputs.append((var,len(cls.table[var])-1))
            else:
                outputs.append((var,len(cls.table[var])-1))
        return inputs,outputs
    
    @classmethod
    def dump(cls):
        print "!!! Dumping Minterm Table !!!"
        for var in cls.table:
            for minterm in cls.table[var]:
                print "%-*s       %-*s  %-*s"%(10,var,20,minterm,20,minterm.z3value)
        print "!!! End of Dumping Minterm Table !!!"
    pass


def check_implies(a,b):
    s = Solver()
    s.add(And(a,Not(b)))
    if(s.check() == sat):
        return False
    return True

"""
    Per_Var_Minterm is a dictionary that collects lists of encodings for each vars
    per_var_minterm = { ip4Src : [[0,1], [1,1] ]  ip4Dst = : [ [..], ... ] } 
"""


def gen_minterm2(solver, sofar ,var, predicates, depth , limit):
    
    if (solver.check() != sat):
        #print predicates
        return
    if (depth == limit):
        #print solver.model()
        #minterm = Minterm(predicates) 
        minterm = MintermTable.insert(var,predicates,solver.model()[Z3VarTable.get(var)])
        for predicate in predicates:
            PredicateMintermMap.insert_mapping(predicate,minterm)

        return 

    
    pred = PredicateTable.table[var][depth]
    predz3 = pred.toZ3()
    negpred = pred.negate()
    negpredz3 = negpred.toZ3()
    """
        Case by Case analysis
        a). pred not duplicate: Label 1 and Label 3 get executuede
        b). pred in predicates -> not pred not in predicates =>
            Label 2 and Label 3 get executed
        c). not pred in predicates -> pred not in predicates => # Label 1 and 4 get executed

    """
    if( pred not in predicates): # Label 1
        if ( check_implies(sofar,predz3)):
            #print sofar, predz3
            gen_minterm2(solver,sofar,var, predicates , depth+1 , limit)
        elif (check_implies(predz3,sofar)):
            print "swapping for ",var,predz3,sofar
            newsolver = getInitSolver(var)
            newsolver.add(predz3)
            gen_minterm2(newsolver,predz3,var, [pred] , depth+1 , limit)
        else:
            solver.push()
            solver.add(predz3)
            gen_minterm2(solver,And(sofar, predz3) ,var, predicates + [pred] , depth+1 , limit)
            solver.pop()
    else: # Label 2
        gen_minterm2(solver,sofar,var, predicates , depth+1 , limit)
    
    if (negpred not in predicates):  # Label 3
        if ( check_implies(sofar,negpredz3)):
            #print sofar, predz3
            gen_minterm2(solver,sofar,var, predicates , depth+1 , limit)
        elif (check_implies(negpredz3,sofar)):
            print "swapping for ",var,predz3,sofar
            newsolver = getInitSolver(var)
            newsolver.add(negpredz3)
            gen_minterm2(newsolver,negpredz3,var, [negpred] , depth+1 , limit)
        else:
            solver.push()
            solver.add( negpredz3)
            gen_minterm2(solver,And(sofar,negpredz3) ,var, predicates + [negpred] , depth+1 , limit)
            solver.pop()
    else: #Label 4
        gen_minterm2(solver,sofar,var, predicates , depth+1 , limit)
 

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
        minterm = MintermTable.insert(var,predicates,solver.model()[Z3VarTable.get(var)])
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
    



#def conjuncts(a,b):
#    return Bop.create("and",a,b)




"""
    Returns a dictionary of list for each variable, contains the meaning of each minterm
    per_var_table {ip4Dst :  [And(ip4Dst==3,ip4Dst!=4), ... ] , ip4Src : [ And(...,...) ] }

"""


def collect_gr1(macros):
    print "calling collect gr1"
    inits = []
    trans = []
    lives = []
    for macro in macros:
        
        init , tran , live = macro.collect_gr1()
        #print macro
        inits += init
        trans += tran
        lives += live
    ret = "[ENV_INIT]\n"
    ret +="[SYS_INIT]\n"
    ret += "\n".join(inits)
    ret += "\n[ENV_TRANS]\n"
    #ret += "CONST_TRUE\n"
    #ret += "!CONST_FALSE\n"
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
    print "Getting Value from StateVarTable"
    print StateVarTable.table
    for sid in StateVarTable.table:
        if(sid >0):
            spec += "%s\n"%StateVarTable.table[sid].gr1_repr()

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
            Z3VarTable.insert(var_name,var_type, is_input = False , init_value = var_value )
            #print var_type, var_name , var_value 
        else:
            #print var_type, var_name
            Z3VarTable.insert(var_name,var_type, is_input = False )



def generate_minterms():
    for var in PredicateTable.table:
        if(var.ast_type == "bool"):
            continue
        preds = PredicateTable.table[var]
        if(len(preds)==0):
            continue
        print "generating minterm for variable ",var
        s = getInitSolver(var)
        gen_minterm2(s,And(True),var,[],0,len(preds))



