import dill

get_sign = lambda x : (1,x) if x > 0 else (-1,-x) if x < 0 else (0,0)


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



"""
    This class is a lookup table from a variable to its minterm encoding
    name:str -> var:Var
"""
class MintermEncodingTable(object):
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

