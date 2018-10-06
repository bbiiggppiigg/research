from z3 import And , Not , Or 
from ast import IP , VarTable , isPredicate, isBinary, isUnary, isValue,Var
from ast import Integer, Boolean
from ast import  uop, Predicate, bop
from macro import Precedence, Invariant, Reaction 

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
    print ast_type , args
    if ast_type == "ip":
        return IP(args)
    elif ast_type == "int":
        return Integer(args)
    elif ast_type == "bool":
        return Boolean(args)
    return None


def gen_ast(expr):
    print "gen ast"
    ast_type, args = get_info(expr)
    print "type = ",ast_type, "args = ",args
    if (ast_type == "var"):
        return Var(args[0])
    elif(isPredicate(ast_type)):
        return Predicate(ast_type,gen_ast(args[0]),gen_ast(args[1]))
    elif(isBinary(ast_type)):
        return bop.create(ast_type,gen_ast(args[0]),gen_ast(args[1]))
    elif(isUnary(ast_type)):
        return uop.create(ast_type,gen_ast(args[0]))
    elif(isValue(ast_type)):
        return gen_const(ast_type,args[0])
    else:
        raise Exception ("Parsing Ast, get %s"%ast_type)

def parse_value(expr):
    print "Parse Value"
    print expr 
    print get_info(expr)
    expr = expr.strip()
    ast_type= expr.split()[0]
    value = expr[len(ast_type):]
    ret = None
    print "ast_type = " , ast_type
    if(ast_type == "Bool"):
        varname = value.strip()
        ret = VarTable.get(varname)
    if(ast_type == "Number"):
        ret = int(value)
    if(ast_type == "IP"):
        lparen = find_lparen(value)
        rparen = find_rparen(value)
        ip_str = value[lparen+1:rparen]
        ret = parse_ip(ip_str)
    return ret



# Used by the Z3 Solver subprocess;
def parse_expr(expr):
    print "QQ"
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

def get_predicates(ast):
    #ret = []
    return ast.get_predicates()
    """
    if(ast.__class__ == Predicate):
        ret += [ast]
    elif(ast.__class__ == BinOp):
        ret += get_predicates(ast.left)
        ret += get_predicates(ast.right)
    elif(ast.__class__ == UnaOp):
        ret += get_predicates(ast.term)

    return ret
    """



def parse_precedence(macro):
    print "parsing precedence"
    args = parse_args(macro)
    return Precedence(args[0],args[1])

def parse_invariant(macro):
    print "parsing invariant"
    args =  parse_args(macro)
    print args
    prop  = args[0]
    prop_ast = gen_ast(prop)#.nnf()
    predicates = get_predicates(prop_ast)
    return Invariant(prop_ast,predicates)

def parse_reaction(macro):
    print "parsing reaction"
    args = parse_args(macro)
    print args
    return Reaction(args[0],args[1],args[2])

def parse_macros(filename):
    ret = list()
    with open(filename) as f:
        macros = f.readlines()
        for macro in macros:
            #print macro.strip()
            if(str.startswith(macro,"invariant")):
                ret.append(parse_invariant(macro))
            #if(str.startswith(macro,"Justice")):
            #    print "parse_justice"
            if(str.startswith(macro,"reaction")):
                print "parse_reaction"
                ret.append(parse_reaction(macro))
            if(str.startswith(macro,"precedence")):
                print "parse_precedence"
                ret.append(parse_precedence(macro))
    return ret

