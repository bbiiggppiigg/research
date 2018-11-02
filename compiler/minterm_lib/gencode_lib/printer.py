from gencode_lib.tables import DSs
from gencode_lib.helper import Helper, ImpossibleCondition


class SolutionTable(object):
    table = dict()
    terminate = 20
    @classmethod
    def insert(cls,stack):
        if(cls.terminate==0):
            return
        primed,unprimed,counter,flags = Helper.split_vars(stack)
        unprimed_in ,unprimed_out = Helper.split_io(unprimed)
        primed_in ,primed_out = Helper.split_io(primed)
        
        if (primed_out == frozenset()):
            return 
        table = cls.table
        
        setupin = (unprimed_in)
        setupout = (unprimed_out)
        setpin =  (primed_in)
        setpout =  (primed_out)
        try: 
            upin_str  =  Helper.interpret_stack(setupin)
            upout_str = Helper.interpret_stack(setupout)
            pin_str =  Helper.interpret_stack(setpin,True)
            counter_str = Helper.get_possible_counter(counter) 
        except ImpossibleCondition, e:
            #print "impossible condition",e
            return
            
        #cond_str_list = upin_str + upout_str + pin_str + counter_str
        cond_str_list = pin_str + counter_str
        if (len(cond_str_list)==0):
            return

        cond_str_set = set(cond_str_list)
        
        
        
        num_tabs = 2 
        actions = Helper.interpret_actions(setpout)
        action_str = "".join (map ( lambda action: "\t" *(num_tabs+1) + action+"\n"  , actions))
        if( Helper.goal_reached(flags)):
            action_str += "\t"*(num_tabs+1)+"self.nib.counter = (self.nib.counter + 1 ) %% %d\n"%DSs.state_counter_max
        if(action_str == ""):
            return
        superset = None
        for preds in table:
            if preds.issubset(cond_str_set):
                if cond_str_set.issubset(preds): # Same
                    if (action_str > table[preds]): # Replace if we have  more action associated with 
                        superset = preds
                        break
                    else:
                        pass
                else: # If we find a proper subset of the this condition set, we know its if branch is covered
                    return 
            elif cond_str_set.issubset(preds): # If our new condition is a subset of preds
                superset = preds
                break
        
       
        if (superset is not None):
            del table[superset]
 
        table[frozenset(cond_str_set)] = action_str 
        Helper.translate(list(setupin)+list(setupout)+list(setpin)+list(setpout))
   
        cls.terminate = cls.terminate - 1

    @classmethod
    def dump_native_solution(cls):
        print "dumping solution"
        isfirst = True
        ret = ""
        num_tabs = 2
        i= 0
        for predicates,action_str in cls.table.iteritems():
            #predicates = filter(lambda x : x != "", predicates)
            if(isfirst):
                cond_str = "\t"*num_tabs+"if(%s):\n" % (" and ".join(predicates))
            else:
                cond_str = "\t"*num_tabs+"elif(%s):\n" % (" and ".join(predicates))
            ret += (cond_str + action_str)
            isfirst = False         
            #i = i + 1
            #if ( i > cls.terminate):
            #    break
        return ret


class SolutionTable2(object):
    table = dict()

    @classmethod
    def insert(cls,stack):
        
        primed,unprimed,counter,flags = Helper.split_vars(stack)
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
            table[setupin][setupout][setpin] = (setpout,counter,flags) #list()
        #if (setpout not in table[setupin][setupout][setpin]):
        #    table[setupin][setupout][setpin].append(setpout)
    
"""
    @classmethod
    def dump_native_solution(cls):
        print "dumping solution"
        isfirst = True
        ret = ""
        
        num_tabs = 2
        for upin in cls.table:
            try: 
                upin_str  =  Helper.interpret_stack(upin)
                #print len(upin),upin_str
            except ImpossibleCondition, e:
                print e
                continue
            for upout in cls.table[upin]:
                try: 
                    upout_str = Helper.interpret_stack(upout)
                    #print len(upout),upout_str,upout
                except ImpossibleCondition, e:
                    print e
                    continue

                for pin in cls.table[upin][upout]:
                    try:
                        pin_str =  Helper.interpret_stack(pin,True)
                    except ImpossibleCondition, e:
                        print e
                        continue
                     
                    pout,counters,flags = cls.table[upin][upout][pin]
                    counter_str = Helper.get_possible_counter(counters) 
                    
                    if(len(upin_str + upout_str + pin_str+counter_str)==0):
                        continue
                    predicates = upin_str + upout_str + pin_str + counter_str
                    if(isfirst):
                        cond_str = "\t"*num_tabs+"if(%s):\n" % (" and ".join(predicates))
                    else:
                        cond_str = "\t"*num_tabs+"elif(%s):\n" % (" and ".join(predicates))
                     
                    
                    
                    actions = Helper.interpret_actions(pout)
                    action_str = "".join (map ( lambda action: "\t" *(num_tabs+1) + action+"\n"  , actions))
                    if( Helper.goal_reached(flags)):
                        action_str += "\t"*(num_tabs+1)+"self.nib.counter = (self.nib.counter + 1 ) %% %d\n"%DSs.state_counter_max
                    if(action_str == "" or cond_str ==""):
                        continue
                    ret += (cond_str + action_str)
                    isfirst = False
                    #ret += "\t"*num_tabs+"ACTIONS !! = %s\n "  % DSs.interpret_actions(pout)

        return ret
        pass
"""

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
        ret += "\t"*numtabs + "self."+var.name+" = 0\n"
    ret += "\t" * numtabs + "self.counter = 0\n"
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


