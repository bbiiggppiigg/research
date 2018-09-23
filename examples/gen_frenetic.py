#!/usr/bin/python
import pickle
def test_writetable(filename):
    with open(filename,'wb') as f:
        pickle.dump({'i1':'Port=5'},f)
    

def read_table(filename):
    with open(filename,'rb') as f:
        table =  pickle.load(f)
    return table
    
def fake_table():
    ret = dict()
    ret['i1'] = ('in','pkt.ipProto == 3')
    ret['i2'] = ('out','self.nib.occurred == True')
    ret['i3'] = ('out','SetPort(5)')
    return ret
def parse_strategy(filename):
    with open(filename) as f:
        lines = f.readlines()
        """
            When this for loop termiates
            i = index of line starts with orderedvarnames
        """
        
        for varname_index, line in enumerate(lines):
            if(line.startswith('.orderedvarnames')):
                break
        
        varnames = line.strip().split()[1:]
        label_map = varnames #zip( [i for i in range(len(varnames))],varnames)
        #print label_map
        """
            When this for loop termiates
            j = index of line starts with rootids
        """
 
        for root_index , line in enumerate(lines):
            if(line.startswith('.rootids')):
                break
        
        rootid = int(lines[root_index].strip().split()[1]) 
        graph = [0]
        for edge_index, line in enumerate(lines[root_index+2:]):
            if(line.startswith(".end")):
                break
            infos = map(lambda x : int(x) if x !='T' else 'T',line.strip().split())
            graph.append(infos[1:])
        return rootid,graph , label_map 
        
        #print rootid


get_sign = lambda x : (1,x) if x > 0 else (-1,-x) if x < 0 else (0,0)

def print_init(variables,table,numtabs):
    with open("skeleton/nib.py") as f:
        skeleton = f.read()
    ret = ""
    numtabs = 2
    for var in variables:
        if("'" in var or (var not in table)):
            continue
        ret += "\t"*numtabs + "self."+var+" = False\n"
                
    return skeleton%ret 

def print_import():
    with open("skeleton/import.py") as f:
        skeleton = f.read()
    return skeleton


def print_nibupdate(variables,table,numtabs):
    ret = ""
    for var in variables:
        if("'" in var or (var not in table)):
            continue
        ret += "\t"*numtabs + "if ( " + table[var][1] +" ) :\n" 
        ret += "\t"*(numtabs+1) + "self.nib."+var+" = True\n"
        ret += "\t"*numtabs +  "else :\n" 
        ret += "\t" *(numtabs+1) + "self.nib."+var+" = False\n\n"
        
    return ret 
def split_vars(stack,graph,label_map):
    primed = list()
    unprimed = list()
    for index in stack:
        sign,value = get_sign(index)
        varname = label_map[graph[value][1]]
        if("'" in varname):
            primed.append(index)
        else:
            unprimed.append(index)
    return primed,unprimed

def split_primed(stack,graph,label_map,table):
    inputs = list()
    outputs = list()
    for index in stack:
        sign,value = get_sign(index)
        varname = label_map[graph[value][1]][:-1]
        if(table[varname][0]=='in'):
            inputs.append(index)
        else:
            outputs.append(index)
    return inputs,outputs

isfirst = True
def pretty_print_sol(cond_list,input_cond_list,action_list,numtabs):
    global isfirst
    if(not isfirst):
        ret = "\t" *numtabs + "elif ( " + " and ".join(cond_list) +" ):\n"
    else:
        ret = "\t" *numtabs + "if ( " + " and ".join(cond_list) +" ):\n"
    ret +="\t" * (numtabs+1) + "if ( " + " and ".join(input_cond_list) + " ):\n"
    for action in action_list:
        if( "nib" in action ):
            ret += "\t" * (numtabs+2) + action + "\n"
        else:
            if( "not " in action):
                ret += "\t" * (numtabs+2) + "actions += []\n" 
            else:
                ret += "\t" * (numtabs+2) + "actions += " + action+"\n"
    isfirst = False
    print ret
    return ret

def print_sol(stack,graph,label_map):
    table = fake_table()
    primed,unprimed = split_vars(stack,graph,label_map)
    cond_list = list()
    
    action_list = list()
    for index in unprimed:
        sign,value = get_sign(index)
        varname = label_map[graph[value][1]]
        if(sign == -1):
            cond_list.append("( not self.nib."+varname+" )")
            #action_list.append( "self.nib."+varname+"= False")
        else:
            cond_list.append( "self.nib."+varname)
            #action_list.append( "self.nib."+varname+"= True")
    #conditions = " and ".join(cond_list)
    
    
    
    
    """
        Dealing with Primed Variables => NextState
    """
    
    
    inputs,outputs = split_primed(primed,graph,label_map,table)
    input_cond_list = []
    for index in inputs:
        sign,value = get_sign(index)
        varname = label_map[graph[value][1]][:-1]
        if(sign == -1):
            input_cond_list.append("( not "+table[varname][1]+" )")
            action_list.append( "self.nib."+varname+"= False")
        else:
            input_cond_list.append(table[varname][1])
            action_list.append( "self.nib."+varname+"= True")
    #input_conditions = " and ".join(input_cond_list) 
    for index in outputs:
        sign,value = get_sign(index)
        varname = label_map[graph[value][1]][:-1]
        if(sign == -1):
            action_list.append("( not "+table[varname][1]+" )")
            action_list.append( "self.nib."+varname+"= False")
        else:
            action_list.append(table[varname][1])
            action_list.append( "self.nib."+varname+"= True")
    pretty_print_sol(cond_list,input_cond_list,action_list,2)


def dfs(root, goal,graph,stack,label_map):
    #print root,graph[root]
    sign,value = get_sign(root) 
    #print sign,value, goal
    if(value == 1):
        if(sign == goal):
            print_sol(stack,graph,label_map)
        return 
    if(value ==0):
        raise Exception("dfs on 0-rooted tree")
    sub_goal = sign * goal
    stack.append(value)
    dfs(graph[value][2],sub_goal,graph,stack,label_map)
    del stack[-1]
    stack.append(-value)
    dfs(graph[value][3],sub_goal,graph,stack,label_map)
    del stack[-1]

def print_def():
    ret = ""
    with open("skeleton/app.py") as f:
        ret+= "\n"+f.read()
    ret += "\tdef packet_in(self,dpid,port_id,payload):\n"
    ret += "\t\tpkt = Packet.from_payload(dpid,port_id,payload)\n"
    ret += "\t\tactions = []\n"
    return ret

def print_pktout(numtabs):
    ret =  "\t"*numtabs + "print pkt\n"
    ret += "\t"*numtabs + "self.pkt_out( dpid, payload , actions) "
    return ret

def print_startup():
    print "\n"
    print "app = MyApp()"
    print "app.start_event_loop()"
rootid,graph,label_map = parse_strategy('atom/atom.symbolic')





def print_code():
    print print_import()
    print print_init(label_map,fake_table(),0)
    print print_def()
    dfs(rootid,1,graph,[],label_map)
    print "\t"*2 + "#Updating Internal State Variables "
    #print print_nibupdate(label_map,fake_table(),1)
    print print_pktout(2)
    print_startup()
print_code()
