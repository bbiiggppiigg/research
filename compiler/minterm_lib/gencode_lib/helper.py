from tables import DSs
from variables import get_sign, MintermEncodingTable
class ImpossibleCondition(Exception):
    pass

class Helper:
    @classmethod
    def get_prologue(cls):
        table = DSs.minterm_table.table
        ret = { k : v for k,v in table.iteritems() if k.is_input } 
        ret_str = "\t\tnib=self.nib\n"
        for var,plist in ret.iteritems():
            is_first = True
            for enc , rep in enumerate(plist):
                if (is_first):
                    cond_str =  "\t\tif %s:\n" % rep.fr_predicate(True)
                else:
                    cond_str =  "\t\telif %s:\n" %rep.fr_predicate(True)
                action_str = "\t\t\t%s = %d\n"%(var,enc)
                is_first= False
                ret_str += (cond_str+action_str)


        """
        for var,plist in table.iteritems():
            if( not var.is_input):
                continue
            ret[var] = list()
            for encoding, rep in enumerate(plist):
                print (rep.fr_predicate(True),"%s = %d"%(var,encoding))
                ret.append( (rep.fr_predicate(True),"%s = %d"%(var,encoding)))
                    #print var,encoding,rep.fr_predicate(True)
        """
        return ret_str
    @classmethod
    def translate(cls,indices):
        ints,others = cls.split_int(indices)
        #print map (lambda x : ( "~" if get_sign(x)[0] < 0 else "")+DSs.names[x] , others)
        print cls.collect_bitmap(ints)

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
    def get_possible_counter(cls,indices):
        bit_map = dict()
        for index in indices:
            sign,value = get_sign(index)
            bit_index = int(DSs.names[index][5:])
            bit_map[bit_index] = sign
        ret = cls.backtracking(0,0,bit_map,DSs.state_counter_limit+1)
        ret = filter ( lambda x : x < DSs.state_counter_max, ret) 
        if ret == []:
            return []
        ret  = map (lambda x : "(nib.counter == %d)" % x, ret)
        ret = " or ".join(ret)
        #print ret
        return [ret]
        pass
    
    @classmethod
    def get_possible_minterms(cls,var_name,bit_map,oname = None):
        int_var = MintermEncodingTable.get(var_name)
        max_value = int_var.max_value
        num_bits = int_var.num_bits
        encodings = cls.backtracking(0,0,bit_map,num_bits) # A list of possible encodings for miterm 
        var = DSs.var_table[var_name]
        #print var_name,ret,max_value
        encodings = filter(lambda x : x <= max_value , encodings)
        #ret = filter(lambda x :  min_value <= x, ret)
        
        if (len(encodings) ==0 ):
            raise ImpossibleCondition(var_name)
        
        print "possible encodings = ",var_name,encodings
        #print var,ret ,max_value
        minterms = map (lambda x : DSs.minterm_table.table[var][x] , encodings) 
        #print "possible frenetic value " , var_name, map(lambda x : x.z3value, minterms)
        return minterms
    """
        Return All Possible Minterm Values for a given Input
    """
    
    @classmethod
    def get_minterm_string(cls,var_name,bit_map,is_prime= False):
        minterms = cls.get_possible_minterms(var_name,bit_map)
        if( is_prime ):
            ret = map(lambda x : x.fr_encoding(), minterms)
        else:
            ret = map(lambda x : x.fr_predicate(is_prime), minterms)
        ret = filter(lambda x : x != "" , ret)
        if (ret == []):
            return ""
        ret = " or ".join(ret)
        ret = "( %s )" % ret
        return ret
    @classmethod
    def goal_reached(cls,flags):
        if( DSs.state_counter_max==0 ):
            return False
        if (len(flags)!=1):
            return True
        return get_sign(flags[0])[0] > 0

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
        counters = filter (lambda x: x in DSs.state_counter,indices)
        flags = filter(lambda x: x in DSs.progress_flag,indices)
        return primed,unprimed,counters,flags

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
            ret.append(cls.get_possible_minterms(var_name,bitmap))
        return ret
    """
        For each variable, we need only one action assoicated with it
    """
    @classmethod
    def get_single_minterms(cls,indices):
        ret = []
        bitmaps = cls.collect_bitmap(indices)
        print bitmaps
        i = 0
        for var_name ,bitmap in bitmaps.iteritems():
            print  i
            i = i +1
            try:
                ret.append(cls.get_possible_minterms(var_name,bitmap)[:1])
            except ImpossibleCondition, e:
                continue
        return ret
    """
        For actions, we only need a single minterm representation
    """
    @classmethod
    def interpret_actions(cls,indices):
        ret = []
        intvars ,bitvars= cls.split_int(indices)
        minterms = cls.get_single_minterms(intvars) 
        for minterm in minterms:
            ret +=  map (lambda x : x.fr_action() , minterm )
        for minterm in minterms:
            ret +=  map (lambda x : x.fr_action_update() , minterm )
        
        for index in bitvars:
            sign,value = get_sign(index)
            var_name = DSs.label_map[DSs.graph[value][1]]
            if(sign >0):
                ret.append( "nib.%s = True " % var_name[:-1])
            else:
                ret.append( "nib.%s = False "%var_name[:-1])

        return ret
    """
        For each integer encodings, return the minterm strings
    """
    @classmethod
    def interpret_ints(cls,indices,isprime= False):
        ret = []
        bitmaps = cls.collect_bitmap(indices)
        print "int ",bitmaps  , indices
        for var_name,bitmap in bitmaps.iteritems():
            ret.append(cls.get_minterm_string(var_name,bitmap,isprime))
        ret = filter(lambda x : x!="", ret)
        return ret
        
    @classmethod
    def interpret_stack(cls,indices,isprime = False):
        ret = []
        #print map (lambda x : ( "~" if get_sign(x)[0] < 0 else "")+DSs.names[x] , indices)
        ints,others = cls.split_int(indices) 
        #print len(ints),len(others),len(indices)
        ret_ints = cls.interpret_ints(ints,isprime)
        for index in others:
            sign,value = get_sign(index)
            var_name = DSs.names[index]
            if(sign >0):
                ret.append( "nib.%s" % var_name)
            else:
                ret.append("(not nib.%s)"%var_name)

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
                    ret += "\t"* (num_tabs+1) + "%s\n" % (minterm.fr_action_update())
                    first_if = False
        return ret
                    




   
    pass


