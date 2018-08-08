#!/usr/bin/python
from z3 import *


variables = dict()
variables['pkt_in'] = Bool('pkt_in')
variables['pkt_out'] = Bool('pkt_out')

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


def is_ip(expr):
    if(expr.strip().split()[0]!="Value"):
        return False
    args = parse_args(expr)
    return ("IP"==args[0].strip().split()[0])

def get_ip(expr):
    args = parse_args(expr)
    ip_str = parse_args(args[0])
    return parse_ip(ip_str[0])

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
        print "QQQQ = ",value
        lparen = find_lparen(value)
        rparen = find_rparen(value)
        ip_str = value[lparen+1:rparen]
        ret = parse_ip(ip_str)
    return ret
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

def gr1_expr(expr):
    expr = expr.strip()
    print "expr = ",expr
    ast_type = expr.split("(")[0].strip()
    args_string = expr[len(ast_type)-1:]
    print (len(args_string))
    args = parse_args(args_string)
    print "ast_type = ",ast_type," args = ",args,"\n"
    if(ast_type=="Value"):
        return parse_value(args[0]) 
    else:
        if(ast_type == 'And'):
            return "(%s) & (%s)"%(gr1_expr(args[0]),gr1_expr(args[1]))
        if(ast_type == "BImplies"):
            return "(%s) <-> (%s)"%(gr1_expr(args[0]) , gr1_expr(args[1]))
        if(ast_type == "Or"):
            return "(%s) | (%s)"%(gr1_expr(args[0]),gr1_expr(args[1]))
        if(ast_type == "Not"):
            return "!(%s)"%(gr1_expr(args[0]))
        if(ast_type == "Equal"):
            if(is_ip(args[1])):
                print "do something !"
                left = gr1_expr(args[0])
                ips =  get_ip(args[1])
                return "(%d <= %s) & (%s <= %d)" % (left,ips[0],left,ips[1])
            else:
                return "(%s) = (%s)"%(gr1_expr(args[0]),gr1_expr(args[1]))
 

def parse_expr(expr):
    expr = expr.strip()
    print "expr = ",expr
    ast_type = expr.split("(")[0].strip()
    args_string = expr[len(ast_type)-1:]
    print (len(args_string))
    args = parse_args(args_string)
    print "ast_type = ",ast_type," args = ",args,"\n"
    if(ast_type=="Value"):
        return parse_value(args[0]) 
    else:
        if(ast_type == 'And'):
            return And(parse_expr(args[0]),parse_expr(args[1]))
        if(ast_type == "BImplies"):
            return (parse_expr(args[0]) == parse_expr(args[1]))
        if(ast_type == "Or"):
            return And(parse_expr(args[0]),parse_expr(args[1]))
        if(ast_type == "Not"):
            return Not(parse_expr(args[0]))
        if(ast_type == "Equal"):
            if(is_ip(args[1])):
                print "do something !"
                left = parse_expr(args[0])
                ips =  get_ip(args[1])
                return And(left <= ips[0] , left >= ips[1])
            else:
                return(parse_expr(args[0])==parse_expr(args[1]))
        

class Invariant:
    def __init__(self,prop):
        self.prop = prop
    def toGR1(self):
        ret = dict()
        ret["trans"]= gr1_expr( self.prop)
        return ret

    def toZ3(self):
        return parse_expr(self.prop)

class Reaction:

    def __init__(self,trigger,policy,terminate):
        self.trigger = trigger
        self.policy = policy
        self.terminate = terminate
        self.triggered = trigger+"ed"

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

class Justice:

    def __init__(self,prop):
        self.prop = prop

    def toGR1(self):
        ret = dict()
        ret["liveness"]=self.prop
        return ret
    def toZ3(self):
        return [parse_expr(self.prop)]

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

def parse_ast(filename):
    ret = list()
    with open(filename) as f:
        macros = f.readlines()
        for macro in macros:
            #print macro.strip()
            if(str.startswith(macro,"Invariant")):
                ret.append(parse_invariant(macro))
            if(str.startswith(macro,"Justice")):
                print "parse_justice"
            if(str.startswith(macro,"Reaction")):
                print "parse_reaction"
                ret.append(parse_reaction(macro))
            if(str.startswith(macro,"Precedence")):
                print "parse_precedence"
                ret.append(parse_precedence(macro))
    return ret

import sys
def main():
    if len(sys.argv)  < 2:
        print "usage : check_dependency.py <ast_filename>"
        exit(-1)
    else:
        #print sys.argv[1]
        macros = parse_ast(sys.argv[1])
        for macro in macros:
            print macro
            print macro.toZ3()

if len(sys.argv)  < 2:
    print "usage : check_dependency.py <ast_filename>"
    exit(-1)
else:
    #print sys.argv[1]
    macros = parse_ast(sys.argv[1])
    for macro in macros:
        print macro
        print macro.toZ3()

#main()

