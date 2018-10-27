#!/usr/bin/python
import sys
from gencode_lib.parser import parse_strategy
from gencode_lib.variables import DSs
from gencode_lib.printer import Printer, SolutionTable

get_sign = lambda x : (1,x) if x > 0 else (-1,-x) if x < 0 else (0,0)

def dfs(root, goal,stack):
    
    #print root,graph[root]
    sign,value = get_sign(root) 
    #print sign,value, goal
    if(value == 1):
        if(sign == goal):
            print stack,len(stack)
            SolutionTable.insert(stack)
        else:
            pass
        return 
    if(value ==0):
        raise Exception("dfs on 0-rooted tree")
    sub_goal = sign * goal
    stack.append(value)
    dfs(DSs.graph[value][2],sub_goal,stack)
    del stack[-1]
    stack.append(-value)
    dfs(DSs.graph[value][3],sub_goal,stack)
    del stack[-1]


def usage():
    if ( len(sys.argv) < 4):
        print "Usage : ./gen_frenetic.py table_filename symbolic_strategy output_filename"
        exit(-1)


def gen_frenetic(db,strategy,code):
    
    rootid,graph,label_map = parse_strategy(strategy)
    
    DSs.setup(db,graph,label_map)   
    dfs(rootid,1,[])
    
    Printer.print_code(code)
    return True
    #print print_nibupdate(label_map,fake_table(),1)
    #print print_pktout(2)
    #print_startup()

if __name__ == "__main__":
    import sys
    usage()
    db = sys.argv[1]
    strategy = sys.argv[2]
    code = sys.argv[3]
    gen_frenetic(db,strategy,code)
#print_code()

