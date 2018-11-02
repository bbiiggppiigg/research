import dill
from variables import MintermEncodingTable
class DSs(object):
    inputs = set()
    outputs = set()
    primes = set()
    originals = set()
    ints = set()
    bools = set()
    names = dict()
    bit_dict = dict() 
    state_counter = set()
    progress_flag = set()
    state_counter_limit = 0
    @classmethod
    def setup(cls,filename,graph,label_map):
        #MintermEncodingTable.dump()
        with open(filename,'r') as f:
            cls.var_table = dill.load(f)
            cls.minterm_table = dill.load(f)
            cls.minterm_table.dump()
            cls.statevar_table = dill.load(f)
            cls.state_counter_max = dill.load(f)
            #for name in cls.var_table:
            #    print name , cls.var_table[name].ast_type , cls.var_table[name].init_value
            #print cls.var_table.items()
            #print cls.statevar_table
            #exit(-1)
        for name,var in cls.var_table.iteritems():
            if var.ast_type != "bool" and var.min_max is not None:
                min_value, max_value = var.min_max
                #exit(-1)
            if var.ast_type != "bool" and var in cls.minterm_table.table:
                MintermEncodingTable.refine_max(
                        name,
                        len(cls.minterm_table.table[var])-1
                        )


        cls.graph =graph
        cls.label_map = label_map
        #print graph
        for i in range(1,len(graph)):
            var_name = label_map[graph[i][1]]
            #print var_name 
            if("'" in var_name ):
                cls.primes.add(i)
                cls.primes.add(-i)
                var_name = var_name.split("'")[0]
            else:
                cls.originals.add(i)
                cls.originals.add(-i)
             
            
            if( "@" in var_name):
                #print var_name
                var_name,bit_index = var_name.split("@")
                cls.bit_dict[i] = int(bit_index)
                cls.bit_dict[-i] = int(bit_index)
                cls.ints.add(i)
                cls.ints.add(-i)
            elif("_jx_b" in var_name):
                bit_index = int(var_name[5:])
                if( bit_index > cls.state_counter_limit ):
                    cls.state_counter_limit = bit_index
                cls.state_counter.add(i)
                cls.state_counter.add(-i)
                cls.names[i] = var_name
                cls.names[-i] = var_name
                continue 
                pass
            elif(var_name=="strat_type"):
                cls.progress_flag.add(i)
                cls.progress_flag.add(-i)
                cls.names[i] = var_name
                cls.names[-i] = var_name
                continue
                pass
            else:
                cls.bools.add(i)
                cls.bools.add(-i)
            
           
            
            if(var_name in cls.var_table and cls.var_table[var_name].is_input):
                cls.inputs.add(i)
                cls.inputs.add(-i)
            else:
                cls.outputs.add(i)
                cls.outputs.add(-i)
            
            cls.names[i] = var_name
            cls.names[-i] = var_name
            if "_out" in var_name:
                print "qq",var_name
                exit(-1)
    @classmethod
    def is_input(cls,index):
        return index in cls.inputs


