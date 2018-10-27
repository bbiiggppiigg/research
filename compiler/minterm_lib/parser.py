from ast import IP , Z3VarTable , isPredicate, isBinary, isUnary, isValue, isAssign
from ast import Integer, Boolean
from ast import  Uop, PredicateTable, Bop
from macro import Precedence, Invariant, Reaction  , Justice

def ip_to_range(n1,n2,n3,n4,mask=32):
    ip_value = (n1 * (256**3) + n2 * (256**2)  + n3 * (256**1) + n4 ) & 0xffffffff
    #print "mask = ",mask
    rest_mask = ((1<<(32-mask)) - 1) & 0xffffffff
    front_mask = (0xffffffff - rest_mask & 0xffffffff)

    #print '{0:b}'.format(rest_mask),len( '{0:b}'.format(rest_mask)),rest_mask
    #print '{0:b}'.format(front_mask),len( '{0:b}'.format(front_mask)),front_mask


    minimum =  ip_value & front_mask
    maximum = ip_value | rest_mask
    return [minimum,maximum]


def is_ip(expr):
    if(expr.strip().split()[0]!="Value"):
        return False
    args = parse_args(expr)
    return ("IP"==args[0].strip().split()[0])

def get_ip(expr):
    args = parse_args(expr)
    ip_str = parse_args(args[0])
    return parse_ip(ip_str[0])



def find_rparen(expr):
    level =0 
    for i in range(len(expr)):
        c = expr[i]
        if(c=='(') :
            level += 1
        if(c==')') :
            level -= 1
            if(level==0):
                return i
    return -1

def find_lparen(expr):
    return expr.find("(")

def parse_ip(ip_str):
    ip_str = ip_str.strip()
    ip_type,ip = ip_str.split()
    n1,n2,n3,last = ip.split(".")
    if(len(last.split("/"))>1):
        n4,mask = last.split("/")
    else:
        n4 = last
        mask = 32
    return ip_to_range(int(n1),int(n2),int(n3),int(n4),int(mask))


def get_info(expr):
    expr = expr.strip()
    ast_type = expr.split("(")[0].strip()
    args_string = expr[len(ast_type)-1:]
    args = parse_args(args_string)
    return ast_type,args


def parse_args(expr):
    nexpr = expr
    ret = []
    while(find_lparen(nexpr) != -1):
        lpar = find_lparen(nexpr)
        rpar = find_rparen(nexpr)
        arg = nexpr[lpar+1:rpar]
        ret.append(arg)
        nexpr = nexpr[rpar+1:]
    #print len(ret),ret;
    return ret

"""
Recursively Generate AST from input expression string expr

"""

def gen_const(ast_type,args):
    #print "gen const , ast_type = ",ast_type , "args = ", args
    if ast_type == "ip":
        return IP(args)
    elif ast_type == "int":
        return Integer(args)
    elif ast_type == "bool":
        return Boolean(args)
    return None



def gen_ast(expr,assign = False):
    #print "gen ast"
    ast_type, args = get_info(expr)
    #if(assign):
    #    print "assign",ast_type , args
 
    #print "gen_ast type = ",ast_type, "args = ",args
    if (ast_type == "var"):
        return Z3VarTable.getvar(args[0],assign)
    elif (ast_type == "bool_expr"):
        return Z3VarTable.getvar(args[0],assign)
    elif (isAssign(ast_type)):
        return PredicateTable.insert(ast_type,gen_ast(args[0],True),gen_ast(args[1]))
    elif(isPredicate(ast_type)):
        #print "inserting predicate"  
        return PredicateTable.insert(ast_type,gen_ast(args[0]),gen_ast(args[1]))
        #return Predicate.create(ast_type,gen_ast(args[0]),gen_ast(args[1]))
    elif(isBinary(ast_type)):
        return Bop.create(ast_type,gen_ast(args[0]),gen_ast(args[1]))
    elif(isUnary(ast_type)):
        return Uop.create(ast_type,gen_ast(args[0]))
    elif(isValue(ast_type)):
        return gen_const(ast_type,args[0])
    else:
        raise Exception ("Parsing Ast, get %s"%ast_type)




def parse_precedence(macro):
    #print "parsing precedence"
    args = parse_args(macro)
    before_ast = gen_ast(args[0])
    after_ast  = gen_ast(args[1])
    
    return Precedence(before_ast,after_ast)

def parse_invariant(macro):
    #print "parsing invariant"
    args =  parse_args(macro)
    #print args
    prop  = args[0]
    prop_ast = gen_ast(prop)#.nnf()
    return Invariant(prop_ast)

def parse_justice(macro):
    #print "parsing invariant"
    args =  parse_args(macro)
    #print args
    prop  = args[0]
    prop_ast = gen_ast(prop)#.nnf()
    return Justice(prop_ast)


def parse_reaction(macro):
    #print "parsing reaction"
    args = parse_args(macro)
    trigger = args[0]
    policy = args[1]
    terminate = args[2]
    trigger_ast = gen_ast(trigger)
    policy_ast = gen_ast(policy)
    terminate_ast = gen_ast(terminate)
    return Reaction(trigger_ast,policy_ast,terminate_ast)

def parse_macros(filename):
    ret = list()
    with open(filename) as f:
        macros = f.readlines()
        for macro in macros:
            #print macro.strip()
            if(str.startswith(macro,"invariant")):
                ret.append(parse_invariant(macro))
            if(str.startswith(macro,"justice")):
                ret.append(parse_justice(macro))
 
            if(str.startswith(macro,"reaction")):
                print "parse_reaction"
                ret.append(parse_reaction(macro))
            if(str.startswith(macro,"precedence")):
                print "parse_precedence"
                ret.append(parse_precedence(macro))
    return ret

