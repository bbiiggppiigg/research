from z3 import And , Int , Bool, Or
def disjuncts (a,b):
    return Bop.create(a,b)

class PredicateTable:
    table = dict()
    @classmethod
    def get(cls,pred):
        try:
            return PredicateTable.table[pred.var][pred]
        except:
            raise Exception ("Unknown Predicate : %s "%pred)
        pass
    
    @classmethod
    def insert(cls,ast_type,var,value):
        #print "doing insertion", type(value)
        if (var not in PredicateTable.table):
            PredicateTable.table[var] = list()
        
        for pred in PredicateTable.table[var]:
            if(pred.ast_type == ast_type and pred.var == var and pred.value == value):
                return pred
        pred= Predicate.create(ast_type,var,value)
        PredicateTable.table[var].append(pred)
        #print "return value = ",pred
        return pred 
        pass

    @classmethod
    def insert_negation(cls,ast_type,var,value,pid):
        for pred in cls.table[var]:
            if(pred.ast_type == ast_type and pred.var == var and pred.value == value):
                return pred
        pred= Predicate.create(ast_type,var,value,-pid)
        cls.table[var].append(pred)
        #print "return value = ",pred
        return pred 
        pass



    @classmethod
    def get_all(cls):
        ret = list()
        for var in PredicateTable.table:
            for predicate in PredicateTable.table[var]:
                ret.append(predicate)
        return ret

    @classmethod
    def dump(cls):
        print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        print "Printing              Predicates"
        print "================================"
        for var in cls.table:
            for predicate in cls.table[var]:
                print "%-*s        %-*s"%(10,var,10,predicate)
        print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" 



class Z3VarTable:
    z3table = dict()
    vartable= dict()
    @classmethod
    def get(cls,var):
        try:
            return Z3VarTable.z3table[var]
        except :
            raise Exception ("unknown variable %s"%var)
    @classmethod
    def insert(cls,name,typeinfo,is_input = False, init_value = None ):
        if ( name in cls.vartable):
            return cls.vartable[name]
        var = Var(name,typeinfo,is_input , init_value)
        cls.vartable[name]=var
        
        if(typeinfo == "bool"):
            Z3VarTable.z3table[var] = Bool(name)
        else:
            Z3VarTable.z3table[var] = Int(name)
        
        return var
    @classmethod
    def getvar(cls,name,assign = False):
        if( assign and Z3VarTable.vartable[name].is_input):
            name += "_out"
        return Z3VarTable.vartable[name]
   
   
    @classmethod
    def dump(cls):
        print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        print "Printing              Predicates"
        print "================================"
        for var in cls.z3table:
                print "%-*s"%(10,var),var.is_input
        print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" 

    pass

def debug(s):
    """
    print "Debuging ========================"
    print s
    print "Endding  ========================" 
    """
    return 


def dc(x):
    import copy
    return copy.deepcopy(x)

class BExpr(object):
    pass


class StateVarTable(object):
    table = dict()
    @classmethod
    def insert(cls,state_var):
        cls.table[state_var.id] = state_var
        return state_var
    @classmethod
    def create(cls):
        return cls.insert(StateVar())
        pass 
    @classmethod
    def create_negate(cls,state_var):
        if ( -state_var.id in cls.table):
            return cls.table[-state_var.id]
        ret = StateVar(- state_var.id)
        return cls.insert(ret)
    pass

class StateVar:
    LAST_ID = 0
    def __init__(self,index = None):
        if(index is not None):
            self.id = index
        else:
            StateVar.LAST_ID+=1
            self.id = StateVar.LAST_ID
    def negate(self):
        return StateVarTable.create_negate(self)
    
    def gr1_repr(self):
        if(self.id > 0):
            return "s%d"%self.id
        else:
            return "!(s%d)"%(-self.id)



class BoolExpr(BExpr):
    def __init__(self,name):
        self.name = name
        pass
    def __repr__(self):
        return self.name

    def __eq__(self,other):
        return self.name == other.name

    def __hash__(self):
        return self.name.__hash__()
  

    def gr1_repr(self):
        return self.__repr__()


class Var(object):
    def __init__(self,name,ast_type,is_input=False, init_value = None):
        self.name = name
        self.ast_type = ast_type
        self.is_input = is_input
        self.init_value  = init_value
    
    def __repr__(self):
        return self.name
    
    def __eq__(self,other):
        return self.name == other.name

    def __hash__(self):
        return self.name.__hash__()
  

    def gr1_repr(self):
        return self.__repr__()

class Predicate(BExpr):
    LAST_ID = 0
    builtin_predicate = dict()
    
    builtin_predicate['ethDst']=" pkt.ethDst  %s %s "
    builtin_predicate['ethSrc']=" pkt.ethSrc %s %s"
    builtin_predicate['ethType']="pkt.ethType %s %s"

    builtin_predicate['ip4Src']="pkt.ip4Src %s %s"
    builtin_predicate['ip4Dst']="pkt.ip4Dst %s %s"

    builtin_predicate['port_id']="port_id %s  %s"

    builtin_predicate['ipProto']="pkt.ipProto %s %s"

    
    def __init__(self,ast_type,var,value,pid = None):
        self.ast_type = ast_type
        self.var = var
        self.value = value
        if(pid is not None):
            self.id = -pid
        else:
           Predicate.LAST_ID +=1
           self.id = Predicate.LAST_ID
    def __repr__(self):
        return " %s (%s) (%s) " % (self.ast_type, self.var , self.value)

    def get_predicates(self):
        return [self]
    def __hash__(self):
        return self.id
    
    def __eq__(self,other):
        return self.__repr__() == other.__repr__()
    
    def gr1_repr(self):
        from minterm import PredicateMintermMap
        ret = reduce(disjuncts,PredicateMintermMap.table[self])
        return ret.gr1_repr()

   
    def rewrite(self,rewrite_table):
        return rewrite_table[self]
  
    def nnf(self):
        import copy
        return copy.deepcopy(self)
    
    def negate(self):
        compl_dict = {
                "gt":Bleq,"geq":Blt,"lt":Bgeq,"leq":Bgt,"match":Bnmatch,"nmatch":Bmatch,"assign":Bnassign,"nassign":Bassign }
        #print self.ast_type, type(self.ast_type)
        return PredicateTable.insert_negation(compl_dict[self.ast_type].ast_type,self.var,self.value,self.id)
        #return compl_dict[self.ast_type](self.var,self.value,self.id)   

    def fr_predicate(self):
        
        var = self.var
        if(var.name in self.builtin_predicate):
            return self.builtin_predicate[var.name]%(self.symbol,self.value)
    
    @classmethod
    def create(cls,ast_type,var,value,pid = None):
        reflect = {"gt":Bgt,"lt":Blt,"geq":Bgeq,"leq":Bleq,"match":Bmatch,"nmatch":Bnmatch,"assign":Bassign,"nassign":Bnassign} 
        return reflect[ast_type](var,value,pid)


    
class Bgt(Predicate):
    ast_type = "gt"
    symbol = ">"
    def __init__(self,var,value,pid = None):
        super(Bgt,self).__init__("gt",var,value, pid)

    def toZ3(self):
        return (Z3VarTable.get(self.var) > self.value.value)

class Blt(Predicate):

    symbol = "<"
    ast_type = "lt"
    def __init__(self,var,value, pid = None ):
        super(Blt,self).__init__("le",var,value, pid  )
    
    def toZ3(self):
        return (Z3VarTable.get(self.var) < self.value.value)



class Bgeq(Predicate):
    ast_type = "geq"
    symbol = ">="
    def __init__(self,var,value, pid = None ):
        super(Bgeq,self).__init__("geq",var,value, pid  )
    
    def toZ3(self):
        return (Z3VarTable.get(self.var) >= self.value.value)


class Bleq(Predicate):
    ast_type = "leq"
    symbol = "<="
    def __init__(self,var,value, pid = None ):
        super(Bleq,self).__init__("leq",var,value,pid)
    
    def toZ3(self):
        return (Z3VarTable.get(self.var) <= self.value.value)


class Bassign(Predicate):
    ast_type = "assign"
    symbol = "="
    def __init__(self,var,value, pid = None ):
        super(Bassign,self).__init__("assign",var,value,pid)
    
    def toZ3(self):
        var = Z3VarTable.get(self.var)
        if ( isinstance(self.value, IP)):
            ips = self.value.get_range()
            return And(var >= ips[0] , var <= ips[1]) 
        return (var == self.value.value)
        
    def gr1_repr(self):
        if(self.var.ast_type == "bool"):
            if(self.value.value == "TRUE"):
                return "(%s)"%self.var
            else:
                return "!%s"%self.var
            return "(%s = %s)"%(self.var,self.value)
        else:
            return super(Bassign,self).gr1_repr()

class Bmatch(Predicate):
    symbol = "=="
    ast_type = "match"
    def __init__(self,var,value, pid = None ):
        super(Bmatch,self).__init__("match",var,value,pid)
    
    def toZ3(self):
        var = Z3VarTable.get(self.var)
        if ( isinstance(self.value, IP)):
            ips = self.value.get_range()
            return And(var >= ips[0] , var <= ips[1]) 
        
        print "qq ",self ,"type = ",self.value
        return (var == self.value.value)
    def gr1_repr(self):
        if(self.var.ast_type == "bool"):
            if(self.value.value == "TRUE"):
                return "(%s)"%self.var
            else:
                return "!%s"%self.var
 
            return "(%s = %s)"%(self.var,self.value)
        else:
            return super(Bmatch,self).gr1_repr()



class Bnassign(Predicate):
    ast_type = "nassign"
    symbol = "!="
    def __init__(self,var,value, pid = None ):
        super(Bnassign,self).__init__("nassign",var,value,pid)
    
    def toZ3(self):
        var = Z3VarTable.get(self.var)
        if ( isinstance(self.value, IP)):
            ips = self.value.get_range()
            return Or(var < ips[0] , var > ips[1]) 

        return (var != self.value.value)
    def gr1_repr(self):
        if(self.var.ast_type == "bool"):
            return "(%s != %s)"%(self.var,self.value)
        else:
            return super(Bnassign,self).gr1_repr()



class Bnmatch(Predicate):
    ast_type = "nmatch"
    symbol = "!="
    def __init__(self,var,value, pid = None ):
        super(Bnmatch,self).__init__("nmatch",var,value,pid)
    
    def toZ3(self):
        var = Z3VarTable.get(self.var)
        if ( isinstance(self.value, IP)):
            ips = self.value.get_range()
            return Or(var < ips[0] , var > ips[1]) 

        return (var != self.value.value)
    def gr1_repr(self):
        if(self.var.ast_type == "bool"):
            return "(%s != %s)"%(self.var,self.value)
        else:
            return super(Bnmatch,self).gr1_repr()



class Bop(BExpr):
        
    def __init__(self,ast_type,e1,e2):
        self.ast_type = ast_type
        self.left = e1
        self.right = e2
    
    def get_predicates(self):
        ret = []
        ret += self.left.get_predicates()
        ret += self.right.get_predicates()
        return ret 
    def __repr__ (self):
        return "%s (%s) (%s)" % (self.ast_type, self.left , self.right)

    def gr1_repr(self):
        lookup = {"and":"&&", "or" : "||" , "implies" : "->" , "bimplies" : "<->"}
        return "( (%s) %s (%s) )"%(self.left.gr1_repr(),lookup[self.ast_type],self.right.gr1_repr())

    def nnf(self):    
        
        reflect = {"and":Band,"or":Bor,"implies":Bimplies,"bimplies":Bbimplies}
        return reflect[self.ast_type](self.left.nnf(),self.right.nnf())


    def rewrite(self,table): 
        
        reflect = {"and":Band,"or":Bor,"implies":Bimplies,"bimplies":Bbimplies}
        return reflect[self.ast_type](self.left.rewrite(table),self.right.rewrite(table))

    @classmethod
    def create(cls,ast_type,e1,e2):
        reflect = {"and":Band,"or":Bor,"implies":Bimplies,"bimplies":Bbimplies}
        return reflect[ast_type](e1,e2)

class Band(Bop):
    def __init__(self,e1,e2): 
        super(Band,self).__init__("and",e1,e2)
    
    def negate(self):
        return Bor(self.left.negate(),self.right.negate())    
class Bor(Bop):
    def __init__(self,e1,e2): 
        super (Bor,self).__init__("or",e1,e2)
 
    def negate(self):
        return Band(self.left.negate(),self.right.negate())
class Bimplies(Bop):
    def __init__(self,e1,e2): 
        super(Bimplies,self).__init__("implies",e1,e2)
    def negate(self):
        return Band(dc(self.left),self.right.negate())
class Bbimplies(Bop):
    def __init__(self,e1,e2): 
        super(Bbimplies,self).__init__("bimplies",e1,e2)
        
    def negate(self):
        left =  Band(dc(self.left),self.right.negate())
        right =  Band(self.left.negate(),dc(self.right))
        return Bor(left,right)



class Uop(object):
        
    def __init__(self,ast_type,e1):
        self.ast_type = ast_type
        self.left = e1
    
    def get_predicates(self):
        ret = []
        ret += self.left.get_predicates()
        return ret 
    def __repr__ (self):
        return "%s (%s)" % (self.ast_type, self.left )

    def gr1_repr(self):
        lookup = {"next":"X", "not" : "!"}
        return "( %s(%s) )"%(lookup[self.ast_type],self.left.gr1_repr())

    def nnf(self):    
        
        reflect = {"next":Unext}
        if ( self.ast_type == "not" ) :
            return self.left.negate().nnf()
        else:
            return reflect[self.ast_type](self.left.nnf())


    def rewrite(self,table): 
        
        reflect = {"next":Unext,"not":Unot}
        return reflect[self.ast_type](self.left.rewrite(table))

    @classmethod
    def create(cls,ast_type,e1):
        reflect = {"next":Unext,"not":Unot}
        return reflect[ast_type](e1)


class Unext(Uop):
    def __init__(self,e):
        super(Unext,self).__init__("next",e)
    def negate(self):

        return dc(self.left.negate())

    pass

class Unot(Uop):
    def __init__(self,e):
        super(Unot,self).__init__("not",e)
    
    def negate(self):
        return dc(self.left)
    pass



"""
    Left hand side of the predicate must be a single var value 
"""

class Constant:
    const_type= "const"
    pass

class Integer(Constant):
    const_type = "int"
    def __init__(self,value):
        self.value = value
    def __repr__(self):
        return self.value
    
    def __eq__(self,other):
        return (self.value == other.value)
    
    def __neq__(self,other):
        return not(self.__eq__(other))


class Boolean(Constant):
    const_type = "bool"
    def __init__(self,value):
        self.value = value

    def __repr__(self):
        return str.upper(self.value)
    
    def __eq__(self,other):
        return (self.value == other.value)
    
    def __neq__(self,other):
        return not(self.__eq__(other))

    def gr1_repr(self):
        if( self.value == "false"):
            return "FALSE"
        else:
            return "TRUE"
class IP(Constant):
    const_type = "IP" 
    format_string = "{n1:Num}.{n2:Num}.{n3:Num}.{n4:Num}/{mask:Num}" 
    def __init__(self,ip_str):
        def toN(text):
            return int(text)

       #print ip_str.strip().split()
        def parse_ip_string(ip_str):
            #print ip_str
            from parse import parse
               
            res = parse(IP.format_string,ip_str,dict(Num=toN))
            return res
        
        def ip_to_range(n1,n2,n3,n4,mask=32):
            ip_value = n1 * (256**3) + n2 * (256**2) + n3 * (256) + n4
            back_mask = (( 1 << (32-mask))-1) & 0xffffffff
            front_mask = (0xffffffff -(back_mask & 0xffffffff))
        
            min_value = ip_value & front_mask
            max_value = ip_value | back_mask
            
            return min_value ,max_value 
        self.masked = True 
        res = parse_ip_string(ip_str)
        n1 = res['n1'] 
        n2 = res['n2'] 
        n3 = res['n3'] 
        n4 = res['n4'] 
        
        self.mask = res['mask']
        self.masked = (self.mask!=32)
        
        self.address = "%d.%d.%d.%d"%(n1,n2,n3,n4)
        
        self.min_value,self.max_value = ip_to_range(n1,n2,n3,n4,self.mask)
        #print self.address

    def __repr__(self):
        ret = self.address
        if(self.masked):
            ret += ("/%d"%(self.mask))
        return '"'+ret+'"'

    def get_range(self):
        return self.min_value,self.max_value

    def __eq__(self,other):
        return (self.address == other.address) and (self.mask == other.mask)
    def __neq__(self,other):
        return not(self.__eq__(other))

def isBinary(ast_type):
    bops = ["and","or","implies","bimplies"]
    return ast_type in bops

def isUnary(ast_type):
    uops = ["not","next"]
    return ast_type in uops

def isValue(ast_type):
    values = ["value","bool","int","ip"]
    return ast_type in values

def isAssign(ast_type):
    assigns = ["nassign","assign"]
    return ast_type in assigns
def isPredicate(ast_type):
    pops = ["nassign","assign","match","nmatch","gt","lt","geq","leq"]
    return ast_type in pops


def print_ast(ast):
    
    print "ast = ",ast
