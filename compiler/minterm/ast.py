from z3 import And , Int , Bool


class VarTable:
    table = dict()
    @classmethod
    def get(cls,name):
        try:
            return VarTable.table[name]
        except :
            raise Exception ("unknown variable %s"%name)
    @classmethod
    def insert(cls,name,typeinfo):
        if(typeinfo == "bool"):
            VarTable.table[name] = Bool(name)
        else:
            VarTable.table[name] = Int(name)

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

class Expr:
    pass
class Var(Expr):
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return self.name

   

class AST(Expr):
    pass


class predicate:
    def __init__(self,ast_type,var,value):
        self.ast_type = ast_type
        self.var = var
        self.value = value
    def __repr__(self):
        return " %s (%s) (%s) " % (self.ast_type, self.var , self.value)
    pass


class bge(predicate):
    def __init__(self,var,value):
        super("ge",var,value)

class ble(predicate):
    def __init__(self,var,value):
        super("le",var,value)
class bgeq(predicate):
    def __init__(self,var,value):
        super("geq",var,value)

class bleq(predicate):
    def __init__(self,var,value):
        super("leq",var,value)

class bassign(predicate):
    def __init__(self,var,value):
        super("assign",var,value)
class bmatch(predicate):
    def __init__(self,var,value):
        super("match",var,value)

class bnassign(predicate):
    def __init__(self,var,value):
        super("nassign",var,value)
class bnmatch(predicate):
    def __init__(self,var,value):
        super("nmatch",var,value)

class bop(object):
        
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
        
        reflect = {"and":band,"or":bor,"implies":bimplies,"bimplies":bbimplies}
        return reflect[self.ast_type](self.left.nnf(),self.right.nnf())


    def rewrite(self,table): 
        
        reflect = {"and":band,"or":bor,"implies":bimplies,"bimplies":bbimplies}
        return reflect[self.ast_type](self.left.rewrite(table),self.right.rewrite(table))

    @classmethod
    def create(cls,ast_type,e1,e2):
        reflect = {"and":band,"or":bor,"implies":bimplies,"bimplies":bbimplies}
        return reflect[ast_type](e1,e2)

class band(bop):
    def __init__(self,e1,e2): 
        super(band,self).__init__("and",e1,e2)
    
    def negate(self):
        return bor(self.left.negate(),self.right.negate())    
class bor(bop):
    def __init__(self,e1,e2): 
        super (bor,self).__init__("or",e1,e2)
 
    def negate(self):
        return band(self.left.negate(),self.right.negate())
class bimplies(bop):
    def __init__(self,e1,e2): 
        super(bimplies,self).__init__("implies",e1,e2)
    def negate(self):
        return band(dc(self.left),self.right.negate())
class bbimplies(bop):
    def __init__(self,e1,e2): 
        super(bbimplies,self).__init__("bimplies",e1,e2)
        
    def negate(self):
        left =  band(dc(self.left),self.right.negate())
        right =  band(self.left.negate(),dc(self.right))
        return bor(left,right)



class uop(object):
        
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
        
        reflect = {"next":unext}
        if ( self.ast_type == "not" ) :
            return self.left.negate().nnf()
        else:
            return reflect[self.ast_type](self.left.nnf())


    def rewrite(self,table): 
        
        reflect = {"next":unext,"not":unot}
        return reflect[self.ast_type](self.left.rewrite(table))

    @classmethod
    def create(cls,ast_type,e1):
        reflect = {"next":unext,"not":unot}
        return reflect[ast_type](e1)


class unext(uop):
    def __init__(self,e):
        super(unext,self).__init__("next",e)
    def negate(self):

        return dc(self.left.negate())

    pass

class unot(uop):
    def __init__(self,e):
        super(unot,self).__init__("not",e)
    
    def negate(self):
        return dc(self.left)
    pass



"""
    Left hand side of the predicate must be a single var value 
"""

class Predicate(AST):
    
    LAST_ID = 0
    compl_dict = {
            "gt":"leq","geq":"lt","lt":"geq","leq":"gt","match":"nmatch","nmatch":"match","assign":"nassign","Nnassign":"assign"
                }

    def get_predicates(self):
        return [self]
    def __hash__(self):
        return self.id
    
    def __eq__(self,other):
        return self.__repr__() == other.__repr__()
    
    def gr1_repr(self):
        return "%d"%self.id
    
    def __init__(self,ast_type,left,right,pid = None):
        self.ast_type= ast_type
        self.left = left
        self.right = right
        self.var = self.left.name
        if(pid is not None):
            self.id = pid
        else:
            self.id = Predicate.LAST_ID +1
            Predicate.LAST_ID += 1
    
    def rewrite(self,rewrite_table):
        if(self in rewrite_table):
            return rewrite_table[self]
        else:
            print "Die !!!"

    def toZ3(self,variables):
        left = self.left
        right = self.right
        ast_type = self.ast_type
        var = VarTable.get(left.name)
        if (isinstance(right,IP)):
            if(ast_type not in ["assign","nassign","match","nmatch"]):
                raise Exception ("Unsupported Predicate Type for IP : %s "%ast_type)
            ips = right.get_range()
            if(ips[0] == ips[1]):
                return And(var == ips[0])
            else:
                return And(ips[0] <= var , var <= ips[1])
            pass
        elif(isinstance(right,Integer) or isinstance(right,Boolean)):
            if (ast_type == "gt") :
               return  And(var > right.value)
            elif (ast_type == "geq") :
               return  And(var >= right.value )
            elif (ast_type == "lt") :
               return  And(var < right.value )
            elif (ast_type == "leq") :
                return  And(var <= right.value)
            elif (ast_type == "match"):
                return  And(var == right.value)
            elif (ast_type == "nmatch"):
                return  And(var != right.value)
            elif (ast_type == "nassign"):
                return  And(var != right.value)
            elif (ast_type == "assign"):
                return And(var ==  right.value)
            else:
                raise Exception("Unsupported ast type for value: %s "%ast_type)
        else:
        
            raise Exception("Unsupported ast type for value: %s "%ast_type)
    
    def __repr__(self):
        return " %s ( %s ) ( %s ) "%(self.ast_type,self.left,self.right) 
    
    def nnf(self):
        import copy
        return copy.deepcopy(self)
    
    def negate(self):
        new_type = Predicate.compl_dict[self.ast_type] 
        return Predicate(new_type,self.left,self.right,-self.id)   

class Value(AST):

    def __init__(self,ast_type,term):
        self.ast_type= ast_type
        self.term = term
    def __repr__(self):
        return " %s ( %s )  "%(self.ast_type,self.term) 
   
    def gr1_repr(self):
        return self.term

    def rewrite(self,_):
        return self

    def nnf(self):
        return self

def toN(text):
    return int(text)


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
        return self.value
    
    def __eq__(self,other):
        return (self.value == other.value)
    
    def __neq__(self,other):
        return not(self.__eq__(other))

class IP(Constant):
    const_type = "IP" 
    format_string = "{n1:Num}.{n2:Num}.{n3:Num}.{n4:Num}/{mask:Num}" 
    def __init__(self,ip_str):
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

def isPredicate(ast_type):
    pops = ["nassign","assign","match","nmatch","gt","lt","geq","leq"]
    return ast_type in pops


def print_ast(ast):
    
    print "ast = ",ast
