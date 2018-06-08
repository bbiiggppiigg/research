#!/usr/bin/python

class IntVar():
    def __init__(self,name,min_value,max_value):
        self.name = name
        self.min_value = min_value
        self.max_value = max_value
        if(min_value <0):
            self.min_value -= min_value
            self.max_value -= min_value

    def __repr__(self):
        return self.name
        #return "IntVar name : %s, range (%d,%d)" % (self.name,self.min_value,self.max_value)
    def __def__(self):
        return "%s:%d...%d"%(self.name,self.min_value,self.max_value)

class BoolVar():
    def __init__(self,name):
        self.name = name
    
    def __repr__(self):
        return self.name
        #return "BoolVar name : %s"%(self.name)

    def __def__(self):
        return self.__repr__()

class GR1():
    def __init__(self,inputs,outputs,env_init,sys_init,env_trans,sys_trans,env_live,sys_live):
        self.inputs = inputs
        self.outputs = outputs
        self.env_trans = env_trans
        self.sys_trans = sys_trans
        self.env_init = env_init
        self.sys_init = sys_init

    def __repr__(self):
        input_section = "[INPUT]\n"
        for inp in self.inputs:
            input_section += inp.__def__() +"\n"
        output_section = "[OUTPUT]\n"
        for oup in self.outputs:
            output_section += oup.__def__() +"\n"
        sys_init_section = "[SYS_INIT]\n"
        for ini in self.sys_init:
            sys_init_section += ini+"\n"
        sys_trans_section = "[SYS_TRANS]\n"
        for tran in self.sys_trans:
            sys_trans_section += tran+"\n"
            
        """
        print input_section
        print output_section
        print sys_init_section
        print sys_trans_section
        """
        return (
                
        input_section+"\n"+
        output_section+"\n"+
        sys_init_section+"\n"+
        sys_trans_section
                )

def Globally(something):
    return "G( %s )"%something
def Implies(pre,post):
    return " %s -> %s "%(pre,post)
def Or(*args):
    return "("+"|".join(str(arg) for arg in args)+")"
def And(*args):
    return "("+" && ".join(str(arg) for arg in args)+")"
def Next(something):
    return "X(%s)"%something

tmp  = (" src_mac = 1 * in_port = 0 "," forward=1 ", "dst_mac=1 "," out_port=0 ")
src_mac = IntVar('src_mac',-2147483648,2147483647)
in_port = IntVar('in_port',0,128)
match_history = BoolVar('match')

match2 = BoolVar('match2')
match3 = BoolVar('match3')
forward = BoolVar('forward')
dst_mac = IntVar('dst_mac',-2147486348,2147483647)
out_port = IntVar('out_port',0,128)
inputs = [src_mac,in_port]
outputs = [dst_mac,out_port,forward,match_history,match2,match3]

#def __init__(self,inputs,outputs,env_init,sys_init,env_trans,sys_trans,env_live,sys_live):

sys_init = [ "!match","!match2","!match3"]
"""
sys_trans = (
        
        [ 
        Implies(And("src_mac = 0","in_port = 1"),And("forward'",Next("match"))),
        Implies("match",Next("match")),
        Implies("match",Next(Implies("dst_mac=0","out_port=1"))),
        Implies(And("src_mac = 2147483647","in_port = 1"),And("forward'",Next("match2"))),
        Implies("match2",Next("match2")),
        Implies("match2",Next(Implies("dst_mac=2147483647","out_port=1"))),
        Implies(And("src_mac = 2147483647","in_port = 2"),And("forward'",Next("match3"))),
        Implies("match3",Next("match3")),
        Implies("match3",Next(Implies("dst_mac=2147483647","out_port=2")))
        ])
#
"""
sys_trans = (
        
        [ 
        Implies(And("src_mac = 0","in_port = 1"),And("forward'",Next("match"))),
        Implies("match",Next("match")),
        Implies("match",Next(Implies("dst_mac=0","out_port=1"))),
        ])
#print sys_trans
print GR1(inputs,outputs,None,sys_init,None,sys_trans,None,None)
"""

G ( match -> action && G[ new_match -> new_action ])

G match -> action && memory
G memory -> X ( memory )
G memory -> X (new_match -> new_action)


"""
def reaction(match,action,new_match,new_action):
    ret = Globally(
            Implies(
                match,And(
                    action,
                    Next(
                        Globally(
                            Implies(
                                new_match,
                                new_action
                                )
                            )
                        )
                    )
                )
            )
    print ret
    return ret



"""
def create(inputs,outputs):
    input_str = ".inputs "+" ".join(inp for inp in inputs)
    output_str = ".outputs "+" ".join(oup for oup in outputs)
    print input_str
    print output_str
    return input_str,output_str

def create_file(filename):
    with open("%s.ltl"%filename,"w") as f:
        tmp  = reaction(" src_mac=1 * in_port=0 "," forward=1 ", "dst_mac=1 "," out_port=0 ")
        f.write(tmp)
    with open("%s.part"%filename,"w") as f:
        inputs = ["src_mac","dst_mac","in_port"];
        outputs = ["forward","out_port"];
        tmp,tmp2 = create(inputs,outputs)
        f.write(tmp+"\n")
        f.write(tmp2+"\n")
create_file("hello1")
"""
