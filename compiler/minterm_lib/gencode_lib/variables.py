import dill

get_sign = lambda x : (1,x) if x > 0 else (-1,-x) if x < 0 else (0,0)

class Helper:
    @classmethod
    def backtracking(cls,index,value,bit_map,limit):
        if(index == limit):
            return [value]
        if (index in bit_map):
            if ( bit_map[index] > 0 ):
                return cls.backtracking (index+1,value | (1 << index),bit_map,limit)
            else:
                return cls.backtracking (index+1,value ,bit_map,limit)
        else:
            case0 = cls.backtracking (index+1,value,bit_map,limit)
            case1 = cls.backtracking (index+1,value | (1 << index),bit_map,limit)
            return case0 + case1
        pass
       
    @classmethod
    def get_possible_minterms(cls,var_name,bit_map):
        int_var = VarTable.get(var_name)
        max_value = int_var.max_value
        num_bits = int_var.num_bits
        ret = cls.backtracking(0,0,bit_map,num_bits)
        
        var = DSs.var_table[var_name]
        ret = filter(lambda x : x <= max_value , ret)
        #print var,ret ,max_value
        ret = map (lambda x : DSs.minterm_table.table[var][x] , ret) 
        return ret 
    """
        Return All Possible Minterm Values for a given Input
    """
    
    @classmethod
    def get_minterm_string(cls,var_name,bit_map,is_prime= False):
        minterms = cls.get_possible_minterms(var_name,bit_map)
        ret = map(lambda x : x.fr_predicate(is_prime), minterms)
        ret = filter(lambda x : x != "" , ret)
        if (ret == []):
            return ""
        ret = " or ".join(ret)
        ret = "( %s )" % ret
        return ret
    
    @classmethod
    def split_int(cls,indices):
        ints = filter(lambda x : x in DSs.ints , indices)
        others = filter(lambda x : x in DSs.bools , indices)
        return ints,others
   
    @classmethod
    def collect_bitmap(cls,indices):
        bitmap = dict()
        for index in indices:
            sign,value = get_sign(index)
            var_name  = DSs.names[index]
            #print var_name
            bit_index = DSs.bit_dict[index]
            if(var_name not in bitmap):
                bitmap[var_name] = dict()
            bitmap[var_name][bit_index] = sign 
        return bitmap
        
    @classmethod
    def split_vars(cls,indices):
        primed = filter(lambda x : x in DSs.primes , indices)
        unprimed  = filter(lambda x : x in DSs.originals , indices)
        return primed,unprimed

    @classmethod
    def split_io(cls,indices):
        inputs = filter (lambda x : DSs.is_input(x) , indices)
        outputs = filter(lambda x : not DSs.is_input(x) , indices)
        return frozenset(inputs),frozenset(outputs)

    @classmethod
    def get_minterms(cls,indices):
        ret = []
        bitmaps = cls.collect_bitmap(indices)
        for var_name, bitmap in bitmaps.iteritems():
            ret.append(Helper.get_possible_minterms(var_name,bitmap))
        return ret

    @classmethod
    def get_single_minterms(cls,indices):
        ret = []
        bitmaps = cls.collect_bitmap(indices)
        
        for var_name ,bitmap in bitmaps.iteritems():
            ret.append(Helper.get_possible_minterms(var_name,bitmap)[:1])
        return ret

    @classmethod
    def interpret_actions(cls,indices):
        ret = []
        intvars ,bitvars= cls.split_int(indices)
        minterms = cls.get_single_minterms(intvars) 
        
        for minterm in minterms:
            ret +=  map (lambda x : x.fr_action() , minterm )
        for minterm in minterms:
            ret +=  map (lambda x : x.fr_update() , minterm )
        
        for index in bitvars:
            sign,value = get_sign(index)
            var_name = DSs.label_map[DSs.graph[value][1]]
            if(sign >0):
                ret.append( "self.nib.%s = True " % var_name[:-1])
            else:
                ret.append( "self.nib.%s = False "%var_name[:-1])

        return ret
    
    @classmethod
    def interpret_ints(cls,indices,isprime= False):
        ret = []
        bitmaps = cls.collect_bitmap(indices)
        for var_name,bitmap in bitmaps.iteritems():
            ret.append(Helper.get_minterm_string(var_name,bitmap,isprime))
        ret = filter(lambda x : x!="", ret)
        return ret
        
    @classmethod
    def interpret_stack(cls,indices,isprime = False):
        ret = []
        ints,others = cls.split_int(indices) 
        print len(ints),len(others),len(indices)
        ret_ints = cls.interpret_ints(ints,isprime)
        for index in others:
            sign,value = get_sign(index)
            var_name = DSs.names[index]
            if(sign >0):
                ret.append( "self.nib.%s" % var_name)
            else:
                ret.append("(not self.nib.%s)"%var_name)

        return ret+ret_ints
        pass

    """
        Generate Update String for Primed Inputs
        Updates fro Primed Ouptputs should be generated with each action
    """

    @classmethod
    def get_updates(cls):
        minterms = DSs.minterm_table.table
        num_tabs = 2
        ret = ""
        
        
        for var,per_var_minterm in minterms.iteritems():
            first_if = True
            for minterm in per_var_minterm:
                if (minterm.fr_predicate(True) != ""):
                    if(first_if):
                        ret += "\t"* num_tabs + "if (%s):\n" % (minterm.fr_predicate(True))
                    else:
                        ret += "\t"* num_tabs + "elif (%s):\n" % (minterm.fr_predicate(True))
                    ret += "\t"* (num_tabs+1) + "%s\n" % (minterm.fr_update())
                    first_if = False
        return ret
                    




   
    pass

class DSs(object):
    inputs = set()
    outputs = set()
    primes = set()
    originals = set()
    ints = set()
    bools = set()
    names = dict()
    bit_dict = dict() 
     
    @classmethod
    def setup(cls,filename,graph,label_map):
        #VarTable.dump()
        with open(filename,'r') as f:
            cls.var_table = dill.load(f)
            cls.minterm_table = dill.load(f)
            #cls.minterm_table.dump()
            cls.statevar_table = dill.load(f)
            for name in cls.var_table:
                print name , cls.var_table[name].ast_type , cls.var_table[name].init_value
            #print cls.var_table.items()
            #print cls.statevar_table
            #exit(-1)
        for name,var in cls.var_table.iteritems():
            if var.ast_type != "bool" and var in cls.minterm_table.table:
                VarTable.refine_max(
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
                pass
            elif(var_name=="strat_type"):
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

class Var(object):
    pass

class CounterVar(Var):
    var_typr = "counter"
    def __init__(self,max_value):
        self.name = "_jx_b"
        self.min_value = 0
        self.max_value = max_value

class IntVar(Var):
    var_type = "int"
    def __init__(self,name,min_value,max_value):
        self.name = name
        self.min_value = int(min_value)
        self.max_value = int(max_value)
        self.num_bits = 0
    def refine_max(self,value):
        if( value < self.max_value):
            self.max_value = value
    
    def increase_max(self,value):
        if ( value  > self.max_value):
            self.max_value = value
    
    def set_bit(self,num_bits):
        if( num_bits > self.num_bits):
            self.num_bits = num_bits
    def __repr__(self):
        return "%s %s = %d...%d , num_bits = %d " % (self.var_type, self.name , self.min_value ,
                self.max_value,self.num_bits)
    pass

class BoolVar(Var):
    var_type = "bool"
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return "%s %s"%(self.var_type, self.name)
    pass

class VarTable(object):
    table = dict()
    @classmethod
    def insert_or_create(cls,name,min_max = None):
        if ( name in cls.table):
            return cls.table[name]
        if(min_max is not None):
            ret = IntVar(name,min_max[0],min_max[1])
        else:
            ret = BoolVar(name)
        cls.table[name] = ret
        return ret
        pass
    @classmethod
    def refine_max(cls,name,value):
        if ( name not in cls.table):
            return 
        #print "refining variable ",name,value
        cls.table[name].refine_max(value)
    @classmethod
    def increase_max(cls,name,vlaue):
        if (name not in cls.table):
            return 
        cls.table[name].increase_max(value)
    @classmethod
    def get(cls,name):
        if ( name in cls.table):
            return cls.table[name]
        else:
            raise Exception("Unknown Variable %s"%name)
        pass
    @classmethod
    def record_bits(cls,var_name, bit_index):
        if ( var_name not in cls.table):
            raise Exception ("Setting bit for Non-Present Int : %s"%var_name)
        if(cls.table[var_name].var_type != "int"):
            raise Exception ("Setting bit for Non Int Type : %s" % cls.table[var_name].var_type)
        cls.table[var_name].set_bit(int(bit_index)+1)
    @classmethod
    def dump(cls):
        table = cls.table
        for name in table:
            var = table[name]
            print "dumping ",var , type(var)

