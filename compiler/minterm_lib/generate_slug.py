#!/usr/bin/python
from z3 import Solver, sat
from parser import parse_macros
from ast import   Z3VarTable,PredicateTable, StateVarTable
from minterm import generate_minterms , MintermTable

import dill

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
    return ret, len(lives)


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
    gr1_code, lives = collect_gr1(macros)
    spec += gr1_code 
    with open (output_file,"w") as f:

        f.write(spec)
    return lives

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



import sys
def usage():
    if len(sys.argv)  < 5:
        print "usage : check_dependency.py <declaration> <ast_filename> <structured_slugs_filename> <table_filename>"
        exit(-1)

def setup_vartable(declare_in):
    for var in [ 'ethDst' , 'ethSrc', 'ethType',  'ipProto' ]:
        #print var
        Z3VarTable.insert(var,"int",True)
        Z3VarTable.insert(var+"_out","int")
    
    Z3VarTable.insert("ip4Src","ip",True)
    Z3VarTable.insert("ip4Src_out","ip")
    Z3VarTable.insert("ip4Dst","ip",True)
    Z3VarTable.insert("ip4Dst_out","ip")
    
    
    
    Z3VarTable.insert('port_id',"int",True)
    #Z3VarTable.insert("CONST_TRUE","bool",True)
    #Z3VarTable.insert("CONST_FALSE","bool",True)

    parse_declaration(declare_in)
    
    variables = Z3VarTable.vartable
    for name in (variables):
        var = variables[name]




def generate_slugs(declare_in, ast_in , slug_out , table_out):
    setup_vartable(declare_in) 
    macros = parse_macros(ast_in)
    """
        1. Collect from each macro the expressions that we need to examine,
           so 1 for invaraints and justice, 2 for precedence and 3 for reaction
    """
        
    generate_minterms()
    """
    for var in PredicateTable.table:
        for predicate in PredicateTable.table[var]:
            print "predicate =" , predicate , "gr1_repr = ",predicate.gr1_repr()
    """
    lives = write_gr1(macros,slug_out)
    print "number of liveness properties = ",lives
    #Z3VarTable.dump()
    var_table = Z3VarTable.vartable
    #minterm_table = MintermTable()
        
    #MintermTable.dump()
    #exit(-1)
    with open(table_out, "w" ) as f:
        dill.dump(var_table,f)
        dill.dump(MintermTable,f)
        dill.dump(StateVarTable.table,f)
    
        
    print "END OF MINTEMRM"
    return True

if __name__ == "__main__":
    usage()
    declare_in = sys.argv[1] 
    ast_in = sys.argv[2]
    slug_out = sys.argv[3]
    table_out = sys.argv[4]
    generate_slugs(declare_in,ast_in,slug_out,table_out)
