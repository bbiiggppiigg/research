#!/usr/bin/python
import sys




# Get all possible jxb stage by bruteforceing all unset values
import copy
inputs = list()
outputs = list()


inits = list()

max_goal_num = -1
def getAllStage(stage_num,jxb_set_list):
    set_list = copy.deepcopy(jxb_set_list)
    ret = set()
    if 1 not in set_list:
        #print "adding to set",stage_num
        ret.add(stage_num)
        return ret
    for i in range(len(set_list)):
        if (set_list[i]==0):
            continue
        num1 = stage_num
        set_list[i]=0
        ret= ret.union(getAllStage(num1,set_list))
        
        num2 = stage_num | (1 << i)
        ret = ret.union(getAllStage(num2,set_list))
        #print num1,num2
    return ret 

"""
Return the list of all possible goal numbers by bruteforcing all possible assignments to _jxb_variables

"""
def getStage(jxb_list):
    jxb_len = max_jxb_len
    jxb_set_list = [1] * jxb_len
    #print jxb_list
    
    #print jxb_set_list
    stage_num = 0
    for jxb in jxb_list:
        bit_string_index = jxb.find('_jx_b')+len('_jx_b')
        #sys.stdout.write(jxb[bit_string_index:])
        bit_index = int(jxb[bit_string_index:])
        if('~' not in jxb):
            stage_num |= (1<<bit_index) 
        #print bit_index
        jxb_set_list[bit_index]=0
        #print jxb_set_list
    currentStages =  getAllStage(stage_num,jxb_set_list)
    #print currentStages


    return currentStages


aggr_cond = dict()

def interpret():
    global max_goal_num
    def aggr_ints(ll):
        return True

    def split_vars(list_of_vars):
        reti = list()
        reto = list()
        rets = list()
        for var in list_of_vars:
            tmp = var.split("@")[0]
            if("~" in tmp):
                tmp = tmp[1:]
            if("'" in tmp):
                tmp=tmp[:-1]
            
            #print "after split",tmp
            #if(tmp in intnodes):
            #    print "intnodes ",var
            if(tmp in inputs):
                reti.append(var)
            elif(tmp in outputs):
                reto.append(var)
            else:
                rets.append(var)
        return reti,reto,rets

    isprime = lambda c : '\'' in c
    current = list()
    onestep = list()
    currstage = list()
    #currstate = list()
    
    #print stack
    for node in stack:
        label = id_var_map[labeling[abs(node)]]
        #print node,labeling[abs(node)]
        #if(label.startswith("strat_type")):
        #    print "found"
#            exit(-1)

        if(node<0):
            label = "~"+label
        if(isprime(label)):
            onestep.append(label)

        else:
            if("_jx_b" in label):
                currstage.append(label)
            #elif ("strat" in label):
            #    print label
            #    exit(-1)
            #    currstate.append(label)
            else:
                current.append(label)
    possible_goal_num = getStage(currstage)
    #print currstage,nextstage
    #print currstate
    
    """
        ci , co , cs are the unprimed version of input / output / state variables
        oi,  oo , os are the   primed version of input / output / state variables
        
        The State Transition is driven by 2^X -> 2^Y -> 2^X' -> 2^Y'
        
         

    """
    ci,co,cs = split_vars(current)
    oi,oo,os = split_vars(onestep)
    #if(len(cs)!=0):
    #    print "QQ",cs
    #    exit(-1)
    if(len(os)!=0):
        print "QQQ",os
        print inputs
        print outputs
        exit(-1)
    
    #print "Under condition " + " or ".join(map(lambda x: str(x),list(currentCond))) 
    #print "Input : "+ " ".join(ci)+", Output : "+" ".join(co) +" => "
    #print "Input : "+ " ".join(oi)+", Output : "+" ".join(oo)
    #print possible_goal_num
    #print cs
    #exit(-1)
    if(len(cs)==0):
        reached = 1

    elif( ("~" in  cs[0])):
        reached = -1
    else:
        reached = 1
    
    for goal_num in possible_goal_num:
        if(goal_num > max_goal_num):
            max_goal_num = goal_num
        
        if goal_num not in aggr_cond:
            aggr_cond[goal_num]=dict()    
        if reached not in aggr_cond[goal_num]:
            aggr_cond[goal_num][reached]=list()
        aggr_cond[goal_num][reached].append((ci,co,oi,oo))

    # Debug Only
    """
    if(len(oi)>0):
        print "ya hallo!"
        for inp in oi:
            cp = inp[:-1]
            if(cp not in ci):
                print "Buggy!!!! cant find ",cp," in ",ci
                #exit(-1)
    
    """

    #print current,"=>",onestep

    #exit(-1)
stack = list()
def dfs(root,complement):
    def sign(x):
        if x > 0: return 1
        if x < 0: return -1
        return 0


    nroot = abs(root)
    if(nroot == 1):
        if(root==complement):
            #print stack,root,complement
            interpret()
        return
    if(root ==0 ):
        print "QQQQ"
        exit(-1)
    #print complement   
    complement *= sign(root)
    stack.append(nroot)
    dfs(nodeinfo[nroot][0],complement)
    del stack[-1]
    stack.append(nroot*-1)
    dfs(nodeinfo[nroot][1],complement)
    del stack[-1]


# Recording the tree structure of the given BDD
# nodeinfo[rootid] return a list of two elements, 
# the id of left child (then) and right child (else)
nodeinfo = dict()

labeling = dict()
var_id_map = dict()
id_var_map = dict()
max_jxb_len = -1
rootid = -1
# runtime stack for tracking paths that can reach 1

intnodes = dict()



def init():
    def usage():
        if len(sys.argv) != 3:
            print ("usage : ./parse.py spec filename")
            exit(-1)


    def parse_intnode(label):
        import re
        m = re.match(r'(\w+)@0.(\d+).(\d+)',label)
        var_name,min_value,max_value = m.groups()
        return var_name,min_value,max_value

    def parse_spec(filename):
        with open(filename) as f:
            lines = f.readlines()
            line_it = 0
            line = lines[line_it]
            while(line_it < len(lines)):
                line_it+=1
                line = lines[line_it-1]
                if(line.startswith("[INPUT]")):
                    break
            line = lines[line_it] 
            while(not line.startswith("[OUTPUT]")):
                
                ## BUG ##
                if(line.strip()!=""):
                    inputs.append(line.strip().split(":")[0])
                
                line_it+=1
                line = lines[line_it]
                #print inputs 
            line_it+=1
            line = lines[line_it]
            while(not line.startswith("[")):
                #print line.strip().split(":")[0]
                if(line.strip()!=""):
                    outputs.append(line.strip().split(":")[0])
                line_it+=1
                line = lines[line_it]
                #print outputs
            if(line.startswith("[ENV_INIT]")):
                line_it+=1
                line = lines[line_it]
                while(not line.startswith("[")):
                    if(line.strip()!=""):
                        line = line.strip()
                        if("=" in line):
                            #var_name , value = line.split("=")
                            inits.append(line+";")
                        else:
                            fmt_str = "%s = %d;"
                            if("!" in line):
                                inits.append(fmt_str%(line[1:],0))
                            else:
                                inits.append(fmt_str%(line,1))

#                        print line
                    line_it+=1
                    line = lines[line_it]
            if(line.startswith("[SYS_INIT]")):
                line_it+=1
                line = lines[line_it]
                while(not line.startswith("[")):
                    if(line.strip()!=""):
                        line = line.strip()
                        if("=" in line):
                            #var_name , value = line.split("=")
                            #sys_init[var_name] = value
                            inits.append(line+";")
                        else:
                           fmt_str = "%s = %d;"
                           if("!" in line):
                               inits.append(fmt_str%(line[1:],0))
                           else:
                               inits.append(fmt_str%(line,1))

 #                       print line
                    line_it+=1
                    line = lines[line_it]
            #exit(-1)


    global var_id_map
    global id_var_map
    global max_jxb_len
    global rootid
    usage()
    parse_spec(sys.argv[1])
    filename = sys.argv[2]
     
    with open(filename) as f:
        lines = f.readlines()
        i = 0
        while(i < len(lines)):
            line = lines[i]
            if(line[0]=='#'):
                i+=1
                continue
            #if(line.startswith(".nnodes")):
            #    nnodes = int(line.strip().split()[1])
            if(line.startswith(".orderedvarnames")):
                variables = line.strip().split()[1:]
                #print variables 
                for var_id  in range(len(variables)):
                    if '@0.' in variables[var_id]:
                        var_name,min_value,max_value = parse_intnode(variables[var_id])
                        intnodes[var_name]=  (min_value,max_value) 
                        var_name+='@0'
                        
                        if("'" in variables[var_id]):
                            var_name+="'"
                        variables[var_id]=var_name
                        
                        #print var_name
                is_output = set()
                for var in variables:
                    if "'" in var:
                        is_output.add(var[:-1])
                #print is_output
                ids = list( x for x in range(len(variables )))
                #print ids
                var_id_map = dict(
                        zip(variables,ids
                        )
                    )
                id_var_map = dict(
                        zip(ids,variables)
                        ) 
             
                max_jxb_len = sum(1 for var in variables if "_jx_b" in var)
            if(line.startswith(".rootids")):
                rootid = int(line.strip().split()[1])
            
            if(line.startswith(".nodes")):
                break
            i+=1
        i = i +1;
        while(i<len(lines)):
            line = lines[i]
            if(line.startswith(".end")):
                break
            infos = map(lambda x : int(x) if x!='T' else 'T' , line.strip().split())
            
            labeling[infos[0]]=infos[1]
            nodeinfo[infos[0]] = infos[3:]
            #print infos
            i+=1


def output_result():
    def parse_clause(clauses):
        
        clauses = list(clauses)
        if clauses == []:
            #print "QQ"
            return "True"
 
        ret = list()
        for cl in clauses:
            if(len(cl.split("@"))>1):
                var_name,bit_index = cl.split("@")
                if("'" in cl):
                    var_name = var_name+"_primed"
                    bit_index = bit_index[:-1]
                if("~" in cl): # use bit and do remove all other bits
                    var_name = var_name[1:]
                    new_cl = " ( %s & ~(1 << %s ))" % (var_name,bit_index)
                else:
                    new_cl = " ( %s | ~(1 << %s ))" % (var_name,bit_index)
                ret.append(new_cl)
                #print "  (1 << %s ) "%(bit_index)
            else:
                var_name = cl
                if("'" in cl):
                    var_name = var_name[:-1]+"_primed"
                if("~" in cl):
                    var_name = "!"+var_name[1:]
                ret.append(var_name)
       #exit(-1)
        return  " && ".join(ret)
    
    def generate_variables(): 
        ret = list()
        ret.append("#define MAX_GOAL %d\n"%(max_goal_num+1))
        ret.append("int state; ")
        ret.append("int goal = 0;")
        for inp in inputs:
            if(inp in intnodes):
                ret_str = "int %s, %s_primed; "%(inp,inp)
                ret.append(ret_str)
            else:
                ret.append("bool %s , %s_primed ;"%(inp,inp))
        for oup in outputs:
            if(oup in intnodes):
            
                ret.append("int %s  ;"%(oup))
            else:
        
                ret.append("bool %s  ;"%(oup))
        return ret
    
        
    print "\n".join(generate_variables())
    print " int main() { "
    
    print "\n".join(inits) 
    print "switch(state){"
    
    for goal_num in aggr_cond:
        case_str = "\tcase "+str(goal_num)+": {"
        print case_str
        for reached in aggr_cond[goal_num]:
            #print reached
            #if(reached == -1):
            #    case_str += "//Moving towards goal : #"+str(goal_num)
            #else:
            #    case_str += "//Goal #"+str(goal_num)+" reached !"
            #print case_str
            #print len(aggr_cond[cond])
            
            state_strategy_map = dict()
            
            for strategy in aggr_cond[goal_num][reached]:
                prev_input,prev_output,next_input,next_output = strategy
                if(tuple(prev_input+prev_output) not in state_strategy_map):
                    state_strategy_map[tuple(prev_input+prev_output)] = dict()
                if( tuple(next_input) not in state_strategy_map[tuple(prev_input+prev_output)]):
                    state_strategy_map[tuple(prev_input+prev_output)][tuple(next_input)] = list()
                state_strategy_map[tuple(prev_input+prev_output)][tuple(next_input)].append((next_output))
                #break
                #print strategy
           
            """
                Iterate Through all possible combination of prev_input , prev_output, next_inpu
                and through away unncessary permissive strategies
            """
            for sys_state in state_strategy_map:
                for next_input in state_strategy_map[sys_state]:
                    primed_output = state_strategy_map[sys_state][next_input][0]
                    print "\t\tif ( "+ parse_clause(sys_state+next_input)+") {"
                    print "\t\t\tif ( "+parse_clause(next_input)+") {"
                    for assign in primed_output:
                        assign = assign[:-1]
                        if( len(assign.split("@")) > 1):
                            var_name , bit_index = assign.split("@")
                            if("~" in var_name):
                                print "\t\t\t\t %s &= (~(1 << %s ));"%(var_name[1:],bit_index);
                            else:
                                print "\t\t\t\t %s |= ( (1 << %s ));"%(var_name,bit_index);
                        else: 
                            if("~" in assign):
                                print "\t\t\t\t",assign[1:],"=0;";
                            else:
                                print "\t\t\t\t",assign,"=1;";
                    if(reached == 1):
                        print "\t\t\t\tgoal = ( goal + 1 ) % MAX_GOAL ;"
                    print "\t\t\t\tbreak;"
                    print "\t\t\t}"
                    print "\t\t}"

        print "}"
    print "}"
    print "return 0;"
    print "}"
if __name__=="__main__":
    init()
    #print labeling
    #print id_var_map
    #print var_id_map
    dfs(rootid,1)
    output_result()
    

#dfs(rootid,1)
#print isprime('g')



