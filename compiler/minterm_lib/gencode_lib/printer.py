from gencode_lib.tables import DSs
from gencode_lib.helper import Helper, ImpossibleCondition


class SolutionTable(object):
    table = dict()
    terminate = 2000
    case = 0
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
            
        cond_str_list = upin_str + upout_str + pin_str + counter_str
        #cond_str_list = pin_str + counter_str
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
        #action_str += "\t"*(num_tabs+1) + "print \"case\",%d\n"%cls.case
        cls.case+=1
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
        #Helper.translate(list(setupin)+list(setupout)+list(setpin)+list(setpout))
   
        cls.terminate = cls.terminate - 1
    @classmethod
    def naive_simplify(cls):
        table1 = dict()
        for predicates,action_str in cls.table.iteritems():
            if action_str not in table1:
                table1[action_str] = list()
            table1[action_str].append(predicates)
        cls.reverse_table = table1
        pass
    
    @classmethod
    def generate_solution(cls):
        print "dumping solution"
        isfirst = True
        ret = ""
        num_tabs = 2
        i= 0
        for action_str,predicate_list in cls.reverse_table.iteritems():
            predicate_strs = map(lambda predicates : "("+" and ".join(predicates)+")" ,predicate_list)
            join_predicate_str = "\n\t\t\tor ".join(predicate_strs)
            if(isfirst):
                cond_str = "\t"*num_tabs+"if(%s):\n" % join_predicate_str
            else:
                cond_str = "\t"*num_tabs+"elif(%s):\n" % join_predicate_str
            ret += (cond_str + action_str)
            isfirst = False         
        return ret


    @classmethod
    def dump_native_solution(cls):
        print "dumping solution"
        isfirst = True
        ret = ""
        num_tabs = 2
        i= 0
        for predicates,action_str in cls.table.iteritems():
            if(isfirst):
                cond_str = "\t"*num_tabs+"if(%s):\n" % (" and ".join(predicates))
            else:
                cond_str = "\t"*num_tabs+"elif(%s):\n" % (" and ".join(predicates))
            ret += (cond_str + action_str)
            isfirst = False         
        return ret


   

class Printer(object):
    @classmethod
    def setup(cls):
        SolutionTable.naive_simplify()
        cls.code = SolutionTable.generate_solution()
        #cls.code = SolutionTable.dump_native_solution()
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
    ret += Helper.get_prologue()+"\n"
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


