#!/usr/bin/python
import sys




# Get all possible jxb stage by bruteforceing all unset values
import copy
inputs = list()
outputs = list()
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


def interpret():
    def aggr_ints(ll):
        return True

    def split_vars(ll):
        reti = list()
        reto = list()
        rets = list()
        for l in ll:
            r = l
            if("~" in r):
                r = r[1:]
            if("'" in r):
                r=r[:-1]
            if(r in intnodes):
                print "intnodes ",l
            if(r.split("@")[0] in inputs):
                reti.append(l)
            elif(r.split("@")[0] in outputs):
                reto.append(l)
            else:
                rets.append(l)
        return reti,reto,rets

    isprime = lambda c : '\'' in c
    current = list()
    onestep = list()
    currstage = list()
    #currstate = list()
    
    print stack
    for node in stack:
        label = id_var_map[labeling[abs(node)]]
        print node,labeling[abs(node)]
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
    currentCond = getStage(currstage)
    #print currstage,nextstage
    #print currstate
    ci,co,cs = split_vars(current)
    oi,oo,os = split_vars(onestep)
    print "Under condition " + " or ".join(map(lambda x: str(x),list(currentCond))) 
    print "Input : "+ " ".join(ci)+", Output : "+" ".join(co) +" => "
    print "Input : "+ " ".join(oi)+", Output : "+" ".join(oo)
    if(len(oi)>0):
        print "ya hallo!"
        for inp in oi:
            cp = inp[:-1]
            if(cp not in ci):
                print "Buggy!!!! cant find ",cp," in ",ci
                #exit(-1)
    print current,"=>",onestep
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
                #print line.strip()
                inputs.append(line.strip())
                line_it+=1
                line = lines[line_it]
            
            line_it+=1
            line = lines[line_it]
            while(not line.startswith("[")):
                #print line.strip().split(":")[0]
                outputs.append(line.strip().split(":")[0])
                line_it+=1
                line = lines[line_it]
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
                print variables 
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


if __name__=="__main__":
    init()
    #print labeling
    #print id_var_map
    #print var_id_map
    dfs(rootid,1)

#dfs(rootid,1)
#print isprime('g')



