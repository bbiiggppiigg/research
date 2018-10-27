from gencode_lib.variables import DSs, Helper

class SolutionTable(object):
    table = dict()

    @classmethod
    def insert(cls,stack):
        
        primed,unprimed = Helper.split_vars(stack)
        unprimed_in ,unprimed_out = Helper.split_io(unprimed)
        primed_in ,primed_out = Helper.split_io(primed)
 
        if (primed_out == frozenset()):
            return 
        table = cls.table
        setupin = (unprimed_in)
        setupout = (unprimed_out)
        setpin =  (primed_in)
        setpout =  (primed_out)
        if( setupin  not in table):
           cls.table[setupin] = dict() 
        if( setupout  not in table[setupin]):
            table[setupin][setupout] = dict()
        if( setpin  not in table[setupin][setupout]):
            table[setupin][setupout][setpin] = setpout #list()
        #if (setpout not in table[setupin][setupout][setpin]):
        #    table[setupin][setupout][setpin].append(setpout)
    

    @classmethod
    def dump_native_solution(cls):
        print "dumping solution"
        isfirst = True
        ret = ""
        for upin in cls.table:
                
            num_tabs = 2
            
            upin_str  =  Helper.interpret_stack(upin)
            
            for upout in cls.table[upin]:
                
                upout_str = Helper.interpret_stack(upout)
                
                for pin in cls.table[upin][upout]:
                    pin_str =  Helper.interpret_stack(pin,True)
                    if(len(upin_str + upout_str + pin_str)==0):
                        continue
                    predicates = upin_str + upout_str + pin_str
                    if(isfirst):
                        cond_str = "\t"*num_tabs+"if(%s):\n" % (" and ".join(predicates))
                    else:
                        cond_str = "\t"*num_tabs+"elif(%s):\n" % (" and ".join(predicates))
                    
                    #isfirst = False
                    
                    pout = cls.table[upin][upout][pin]
                    actions = Helper.interpret_actions(pout)
                    action_str = "".join (map ( lambda action: "\t" *(num_tabs+1) + action+"\n"  , actions))
                    if(action_str == "" or cond_str ==""):
                        continue
                    ret += (cond_str + action_str)
                    isfirst = False
                    #ret += "\t"*num_tabs+"ACTIONS !! = %s\n "  % DSs.interpret_actions(pout)

        return ret
        pass


class Printer(object):
    @classmethod
    def setup(cls):
        cls.code = SolutionTable.dump_native_solution()
        cls.state_vars = map(lambda x : "s"+str(x) ,  filter (lambda x : x > 0 , DSs.statevar_table.keys()))
        #print cls.state_vars
        cls.minterm_vars = []
        #for var , minterm_list  in DSs.minterm_table.table.iteritems():
        #    cls.minterm_vars +=  map (lambda x :  var.name + str(x.id), minterm_list )
        for var in DSs.minterm_table.table:
            cls.minterm_vars.append(var)
        #print cls.minterm_vars
        cls.bool_vars = map (lambda x : x[0] , filter(lambda x : x[1].ast_type == "bool", DSs.var_table.items() ))
        #print cls.bool_vars
        #exit(-1)
        
    
    @classmethod 
    def print_code(cls,filename):
        cls.setup()
        ret = get_import_str()
        ret += get_init_str(cls.state_vars, cls.bool_vars, cls.minterm_vars)
        ret += get_def_str()
        ret += cls.code
        ret += Helper.get_updates()
        ret += get_pktout_str(2)
        ret += get_startup_str() 
        with open(filename,"w") as f :
            f.write(ret)
        #print ret

        pass
    pass


    
def get_init_str(state_vars, bool_vars , miterm_vars):
    with open("skeleton/nib.py") as f:
        skeleton = f.read().replace("    ","\t")

    ret = ""
    numtabs = 2
    #for var in variables:
        #if("'" in var or (var not in table)):
        #    continue
    for var in state_vars  + bool_vars :
        ret += "\t"*numtabs + "self."+var+" = False\n"
    for var in miterm_vars:
        ret += "\t"*numtabs + "self."+var.name+" = -1\n"
    return skeleton%ret 

def get_import_str():
    with open("skeleton/import.py") as f:
        skeleton = f.read().replace("    ","\t")

    return skeleton

def get_def_str():
    ret = ""
    with open("skeleton/app.py") as f:
        ret+= "\n"+f.read().replace("    ","\t")
    ret += "\tdef packet_in(self,dpid,port_id,payload):\n"
    ret += "\t\tpkt = Packet.from_payload(dpid,port_id,payload)\n"
    ret += "\t\tactions = []\n"
    return ret

def get_pktout_str(numtabs):
    ret =  "\t"*numtabs + "print pkt\n"
    ret +=  "\t"*numtabs + "print actions\n"
    ret += "\t"*numtabs + "self.pkt_out( dpid, payload , actions) "
    return ret

def get_startup_str():
    ret =  "\n"
    ret += "app = MyApp()\n"
    ret += "app.start_event_loop()\n"
    return ret


