class nib(object):
    allow = False
    counter = 0
    def __init__(self):
        self.allow = False
    def flip(self):
        self.counter = (self.counter+1)%8
        self.allow = False if self.counter < 2 else True
 
