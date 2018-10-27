from variables import VarTable
def parse_variables(variables):
    ret = []
    for variable in variables:
        tmp = variable
        
        if ("'" in variable):
            tmp = tmp[:-1] 
       
       # if ("_jx_b" in tmp):
            #tmp = "_jx_b@"+tmp[5:]
            #print tmp
            #exit(-1)
        #    continue
        if ("@0" in variable):
            var_name,values = tmp.split("@")
            zero,min_value,max_value=values.split(".")
            VarTable.insert_or_create( var_name ,(min_value,max_value))     
            tmp = var_name+"@0" 
        elif("@" not in variable):
            VarTable.insert_or_create(tmp)
        else: # @ in variable but not @0
            var_name,values = tmp.split("@")
            VarTable.record_bits(var_name,values)

        if("'" in variable):
            tmp = tmp+"'"
        
        ret.append(tmp)
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
        #label_map = varnames #zip( [i for i in range(len(varnames))],varnames)
        #print label_map
        label_map = parse_variables(varnames)
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


