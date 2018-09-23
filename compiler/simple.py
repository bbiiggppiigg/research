#!/usr/bin/python

class Invariant:
    def __init__(self,prop):
        self.prop = prop
    def toGR1(self):
        ret = dict()
        ret["trans"]=self.prop
        return ret

class Reaction:

    def __init__(self,trigger,policy,terminate,callback):
        self.trigger = trigger
        self.policy = policy
        self.terminate = terminate
        self.callback = callback
        self.triggered = trigger+"ed"

    def toGR1(self):
        ret = dict()
        ret["init"]="!"+self.triggered;
        ret["trans"]=(
        [
            "(%s | (%s & !%s)) <-> X(%s)"%(self.trigger,self.triggered,self.terminate,self.triggered),
            "%s->%s"%(self.triggered,self.policy),
            "(!%s & %s) -> %s "%(self.trigger,self.terminate,self.callback),
        ]
        )
        return ret

class Justice:

    def __init__(self,prop):
        self.prop = prop
    
    def toGR1(self):
        ret = dict()
        ret["liveness"]=self.prop
        return ret

class Precedence:

    def __init__(self,before,after):
        self.before = before
        self.after = after
        self.happened = before+"ed"
    
    def toGR1(self):
        ret = dict()
        ret["init"]= ("!%s & !%s"%(self.after,self.happened)) 
        ret["trans"]=(
        [
            "(!%s & !%s) -> X(!%s)"%(self.happened,self.after,self.happened),
            "%s -> X(%s)"%(self.before,self.happened),
            "!%s -> !%s"%(self.happened,self.after),
            "%s -> X(%s)"%(self.happened,self.happened)
        ]
        )
        return ret

x = Invariant("src_ip=3")
y = Reaction("infect","drop","cure","hello")
z = Precedence("me","you")
w = Justice("Dead")
print x.toGR1()
print y.toGR1()
print z.toGR1()
print w.toGR1()
