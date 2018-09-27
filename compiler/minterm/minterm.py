#!/usr/bin/python
from z3 import And, Or , Not,Int , Solver, sat ,simplify
from parser import find_lparen, find_rparen , parse_args, parse_ip ,get_ip ,get_info,is_ip
from ast import *
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


        #minterms[var] = list()
    #minterms[var].append(list())
    #minterms[var].append(list())

     

MAX_MAC = ((1<<48) -1)


def parse_value(expr):
    expr = expr.strip()
    ast_type= expr.split()[0]
    value = expr[len(ast_type):]
    ret = None
    print "ast_type = " , ast_type
    if(ast_type == "Bool"):
        ret = variables[value.strip()]
    if(ast_type == "Number"):
        ret = int(value)
    if(ast_type == "IP"):
        lparen = find_lparen(value)
        rparen = find_rparen(value)
        ip_str = value[lparen+1:rparen]
        ret = parse_ip(ip_str)
    return ret

def getInitSolver():
    s = Solver()
    def add_range(s,var,minv,maxv):
        s.add( minv <= variables[var] )
        s.add( variables[var] <= maxv )

    add_range(s,'ethDst',0,MAX_MAC)
    add_range(s,'ethSrc',0,MAX_MAC)
    add_range(s,'ipProto',1,255)
    return s


def gen_value(value_string):
    ast_type, args = get_info(expr)
    if(ast_type == "Number"):
        return int(args[0])
    elif (ast_type == "Bool"):
        return args[0]
    elif (ast_type == "IP"):
        return IP(args[0])


"""
Return a list of predicates appear in the AST

"""

def get_predicates(ast):
    ret = []
    if(ast.__class__ == Predicate):
        ret += [ast]
    elif(ast.__class__ == BinOp):
        ret += get_predicates(ast.left)
        ret += get_predicates(ast.right)
    elif(ast.__class__ == UnaOp):
        ret += get_predicates(ast.term)

    return ret


"""
Recursively Generate AST from input expression string expr

"""

def gen_ast(expr):
    ast_type, args = get_info(expr)
    print ast_type
    if(isPredicate(ast_type)):
        return Predicate(ast_type,gen_ast(args[0]),gen_ast(args[1]),input_vars)
    elif(isBinary(ast_type)):
        return BinOp(ast_type,gen_ast(args[0]),gen_ast(args[1]))
    elif(isUnary(ast_type)):
        return UnaOp(ast_type,gen_ast(args[0]))
    elif(isValue(ast_type)):
        value_type, value_args = get_info(args[0])

        if(value_type != "IP"):
            #print "value_type = ",value_type
            value_type, value_args = value_type.split()

            if(value_type == "Bool"):
                return Value(value_type,value_args)
            elif(value_type == "Number"):
                return Value (value_type,int(value_args))

        elif(value_type == "IP"):
            return Value (value_type,IP(value_args[0]))
    else:
        print "parsing something",ast_type



def parse_expr(expr):
    ast_type, args = get_info(expr)
    print "ast_type = ",ast_type," args = ",args,"\n"
    if(ast_type=="Value"):
        return parse_value(args[0]) 
    else:
        if(ast_type == 'And'):
            return And(parse_expr(args[0]),parse_expr(args[1]))
        elif(ast_type == "BImplies"):
            return (parse_expr(args[0]) == parse_expr(args[1]))
        elif(ast_type == "Or"):
            return Or(parse_expr(args[0]),parse_expr(args[1]))
        elif(ast_type == "Not"):
            return Not(parse_expr(args[0]))
        elif(ast_type == "Match"):
            if(is_ip(args[1])):
                print "do something !"
                left = parse_expr(args[0])
                ips =  get_ip(args[1])
                return And(left <= ips[0] , left >= ips[1])
            else:
                return(parse_expr(args[0])==parse_expr(args[1]))
        elif(ast_type == "NMatch"):
            if(is_ip(args[1])):
                print "do something !"
                left = parse_expr(args[0])
                ips =  get_ip(args[1])
                return Not(And(left <= ips[0] , left >= ips[1]))
            else:
                return(parse_expr(args[0])!=parse_expr(args[1]))
        
        elif(ast_type == "Assign"):
            if(is_ip(args[1])):
                print "do something !"
                left = parse_expr(args[0])
                ips =  get_ip(args[1])
                return And(left <= ips[0] , left >= ips[1])
            else:
                print "Find Assignment !!!, transalte into predicate"
                
                print (parse_expr(args[0])==parse_expr(args[1]))
                return(parse_expr(args[0])==parse_expr(args[1]))
        else:
            print "Un Supported Z3 !!"
            exit(-1)


class Invariant:
    prop = None
    ast = None
    predicates = None
    def __init__(self,prop):
        self.prop = prop
        #print "Prop = ",prop
        self.prop_ast = gen_ast(prop).nnf()
        #print "Original = ",self.prop_ast
        #print "NNF      = ",self.prop_ast.nnf()
        #self.prop_ast = self.prop_ast.nnf()
        self.predicates = get_predicates(self.prop_ast)
        print_ast(self.prop_ast) 

    def rewrite(self,rewrite_table):
        self.prop_ast = self.prop_ast.rewrite(rewrite_table)

    def collect_gr1(self):
        prop_str = self.prop_ast.gr1_repr()

        return  [],[prop_str],[] 
    def getPredicates(self):
        return self.predicates

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


class Reaction:

    def collect_gr1(self):
        init =  [self.triggered.negate().gr1_repr()]
        triggered = self.triggered.gr1_repr()
        terminate = self.terminate_ast.gr1_repr()
        policy =self.policy_ast.gr1_repr()
        trigger = self.trigger_ast.gr1_repr()
        trans = [
                "(%s | (%s & !%s)) <-> X(%s)"%(trigger,triggered,terminate,triggered),
                "(%s)->(%s)"%(triggered,policy),
                ]
        return init, trans , []


    def __init__(self,trigger,policy,terminate):
        self.trigger = trigger
        self.policy = policy
        self.terminate = terminate

        self.trigger_ast = gen_ast(self.trigger).nnf()
        self.policy_ast = gen_ast(self.policy).nnf()
        self.terminate_ast = gen_ast(self.terminate).nnf()

        self.predicates = reduce(lambda a,b : a+b ,map( get_predicates, [self.trigger_ast,self.policy_ast,self.terminate_ast] ))
        self.triggered = StateVar()
        print self.predicates

    def rewrite(self,rewrite_table):
        self.trigger_ast = self.trigger_ast.rewrite(rewrite_table)
        self.policy_ast = self.policy_ast.rewrite(rewrite_table)
        self.terminater_ast = self.terminate_ast.rewrite(rewrite_table)

    def toGR1(self):
        ret = dict()
        ret["init"]="!"+self.triggered;
        ret["trans"]=(
                [
                    "(%s | (%s & !%s)) <-> X(%s)"%(self.trigger,self.triggered,self.terminate,self.triggered),
                    "%s->%s"%(self.triggered,self.policy),
                    ]
                )
        return ret

    def toZ3(self):
        return [parse_expr(self.trigger),parse_expr(self.policy),parse_expr(self.terminate)]

    def getPredicates(self):
        return self.predicates
    #return [self.trigger,self.policy,self.terminate]

class Justice:

    def __init__(self,prop):
        self.prop = prop

    def toGR1(self):
        ret = dict()
        ret["liveness"]=self.prop
        return ret
    def toZ3(self):
        return [parse_expr(self.prop)]
    def getPredicates(self):
        return [self.prop]

class Precedence:

    def __init__(self,before,after):
        self.before = before
        self.after = after
        self.happened = before+"ed"

    def toGR1(self):
        ret = dict()
        ret["init"]= ("!%s & !%s"%(self.after,self.happened)) 
        ret["trans"]=(
                [
                    "(!%s & !%s) -> X(!%s)"%(self.happened,self.after,self.happened),
                    "%s -> X(%s)"%(self.before,self.happened),
                    "!%s -> !%s"%(self.happened,self.after),
                    "%s -> X(%s)"%(self.happened,self.happened)
                    ]
                )
        return ret

    def toZ3(self):
        return [parse_expr(self.before),parse_expr(self.after)]
    def getPredicates(self):
        return [self.before,self.after]




def parse_precedence(macro):
    print "parsing precedence"
    #inner = macro[lpar1+1:rpar1]
    args = parse_args(macro)
    #print args
    return Precedence(args[0],args[1])
#print macro
    #print inner
    #parse_expr(inner)



def parse_invariant(macro):
    print "parsing invariant"
    args =  parse_args(macro)
    #print "args=  ",macro
    #print args
    return Invariant(args[0])
#print macro
    #print inner
    #parse_expr(inner)

def parse_reaction(macro):
    print "parsing reaction"
    args = parse_args(macro)
    print args
    return Reaction(args[0],args[1],args[2])

def generate_macros(filename):
    ret = list()
    with open(filename) as f:
        macros = f.readlines()
        for macro in macros:
            #print macro.strip()
            if(str.startswith(macro,"Invariant")):
                ret.append(parse_invariant(macro))
            #if(str.startswith(macro,"Justice")):
            #    print "parse_justice"
            if(str.startswith(macro,"Reaction")):
                print "parse_reaction"
                ret.append(parse_reaction(macro))
            if(str.startswith(macro,"Precedence")):
                print "parse_precedence"
                ret.append(parse_precedence(macro))
    return ret


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
    return BinOp("And",a,b)


def disjuncts(a,b):
    return BinOp("Or",a,b)


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
                ret += "\n"+pred.gr1_repr()


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

def main():
    import sys


    if len(sys.argv)  < 3:
        print "usage : check_dependency.py <ast_filename> <structured_slugs_filename>"
        exit(-1)
    else:
        #print sys.argv[1]

        for var in input_vars:
            variables[var] = Int(var)
            predicates[var] = list()
            per_var_minterms[var] = list() 


        macros = generate_macros(sys.argv[1])
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
        write_gr1(macros,predicates,sys.argv[2])
        
        dump_table = LookupTable(variables,input_vars,predicates)
        with open("test.db", "wb" ) as f:
            import pickle
            pickle.dump(dump_table,f)
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

