from z3 import And

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


class AST():
    pass

class BinOp(AST):
    ast_type= None
    left = None
    right = None
    
    def __init__(self, ast_type ,left,right):
        self.ast_type= ast_type
        self.left = left
        self.right = right
        #debug(self)
    def __repr__(self):
        return " %s ( %s ) ( %s ) "%(self.ast_type,self.left,self.right) 

    
    def gr1_repr(self):
        fmt_str = "( (%s) %s (%s) )" 
        symbol = None
        if(self.ast_type == "And"):
            symbol = "&&"
        elif(self.ast_type == "Or"):
            symbol = "||"
        elif(self.ast_type == "Implies"):
            symbol = "->"
        elif(self.ast_type == "BImplies"):
            symbol = "<->"
        else:
            raise Exception("Hi")
        return fmt_str % (self.left.gr1_repr() , symbol ,self.right.gr1_repr()) 
    def rewrite(self,rewrite_table): 
        return BinOp(self.ast_type,self.left.rewrite(rewrite_table),self.right.rewrite(rewrite_table))
    
    def nnf(self):
        #print "something = ",self
        debug(self)
        return BinOp(self.ast_type,self.left.nnf(),self.right.nnf())
    def negate(self):
        ret = None 
        if (self.ast_type == "And"):
            ret = BinOp("Or",self.left.negate(),self.right.negate())
        elif (self.ast_type == "Or"):
            ret = BinOp("And",self.left.negate(),self.right.negate())
        elif (self.ast_type == "Implies"):
            
            #print "this branch, left negate = ",self.left.negate()
            ret = BinOp("And",dc(self.left),self.right.negate())

        elif (self.ast_type == "BImplies"):
            left = BinOp("And",dc(self.left),self.right.negate())
            right = BinOp("And",self.left.negate(),dc(self.right))
            ret = BinOp("Or",left,right)
        
        return ret

class UnaOp(AST):
    def gr1_repr(self):
        
        fmt_str = " ( %s (%s) ) "
        symbol = None
        if(self.ast_type == "Not"):
            symbol = "!"
        return fmt_str % (symbol,self.term.gr1_repr())
    def __init__(self,ast_type,term):
        self.ast_type= ast_type
        self.term = term

    def __repr__(self):
        return " %s ( %s ) "%(self.ast_type,self.term) 

    def rewrite(self,rewrite_table):
        try:
            return UnaOp(self.ast_type,self.term.rewrite(rewrite_table))
        except Exception,e:
            debug (e)
            return self
    def nnf(self):
        debug(self)
        if (self.ast_type == "Not"):
            try:
                self.term.negate().nnf()
                return self.term.nnf()
            except Exception,e:
                debug(e)
                return self
        else:
            return self.term.nnf()
    def negate(self):
        import copy
        if (self.ast_type == "Not"):
            return copy.deepcopy(self.term)
        elif(self.ast_type == "Next"):
            return copy.deepcopy(self)

class Predicate(AST):
    
    LAST_ID = 0
    compl_dict = {
            "Gt":"Leq","Geq":"Lt","Lt":"Geq","Leq":"Gt","Match":"NMatch","NMatch":"Match","Assign":"NAssign","NAssign":"Assign"
                }
    istr = "i%d"
    ostr = "o%d"
    def __hash__(self):
        return self.id
    
    def __eq__(self,other):
        return self.__repr__() == other.__repr__()
    
    def gr1_repr(self):
        index = self.id
        if(index > 0):
            return self.fmt_str%index
        else:
            return "!"+ self.fmt_str%(-index)
    def __init__(self,ast_type,left,right,input_vars,pid = None):
        self.input_vars = input_vars
        self.ast_type= ast_type
        self.left = left
        self.right = right
        self.var = self.left.term
        if(self.var not in input_vars):
            self.fmt_str = Predicate.ostr
        else:
            self.fmt_str = Predicate.istr
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
        if( isinstance(self.left,Value)):
            if(self.left.ast_type=="Bool"):
                var = variables[self.left.term]
                #print "var = ",var
                if (isinstance(self.right,Value)):          
                    if(isinstance(self.right.term,IP)):      # IP can only be matched, no comparison
                        ip_instance = self.right.term
                        ips = ip_instance.get_range()
                        if(ip_instance.masked):
                            return And(ips[0] <= var , var <= ips[1])
                        else:
                            return var == ips[0]
                        
                    else:                                    # Other type, Possibily Number
                        if(isinstance(self.right.term,int)):
                            if (self.ast_type == "Gt") :
                               return  var > self.right.term 
                            elif (self.ast_type == "Geq") :
                               return  var >= self.right.term 
                            elif (self.ast_type == "Lt") :
                               return  var < self.right.term 
                            elif (self.ast_type == "Leq") :
                                return  var <= self.right.term 
                            elif (self.ast_type == "Match"):
                                return  var == self.right.term
                            elif (self.ast_type == "NMatch"):
                                return  var != self.right.term
                            elif (self.ast_type == "NAssign"):
                                return  var != self.right.term
                            elif (self.ast_type == "Assign"):
                                return var ==  self.right.term
                            else:
                                print "Error!!"
                        #print "something else!!",self.right.term.__class__
                else:
                    return None
        else:
            print "Die!",self.right.__class__
    def __repr__(self):
        return " %s ( %s ) ( %s ) "%(self.ast_type,self.left,self.right) 
    def nnf(self):
        import copy
        return copy.deepcopy(self)
    
    def negate(self):
        new_type = Predicate.compl_dict[self.ast_type] 
        return Predicate(new_type,self.left,self.right,self.input_vars,-self.id)   
    
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

class IP:
    def __init__(self,ip_str):
        #print ip_str.strip().split()
        def parse_ip_string(ip_str):
            #print ip_str
            from parse import parse
            ip_type,ip_rest = ip_str.strip().split()
            if(ip_type != "Masked"):
                ip_rest += "/32"
                self.masked = False 
                
            format_string = "{n1:Num}.{n2:Num}.{n3:Num}.{n4:Num}/{mask:Num}" 
            res = parse(format_string,ip_rest,dict(Num=toN))
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
        self.address = "%d.%d.%d.%d"%(n1,n2,n3,n4)
        self.mask = res['mask']
        
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
    bops = ["And","Or","Implies","BImplies"]
    return ast_type in bops

def isUnary(ast_type):
    uops = ["Not","Next"]
    return ast_type in uops

def isValue(ast_type):
    values = ["Value","Bool","Number","IP"]
    return ast_type in values

def isPredicate(ast_type):
    pops = ["NAssign","Assign","NMatch","Match","Gt","Lt","Geq","Leq"]
    return ast_type in pops


def print_ast(ast):
    
    print "ast = ",ast
