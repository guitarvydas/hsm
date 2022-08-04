from leaf import Leaf
debugHSM = False
class HSM (Leaf):
    def __init__ (self, parent, instanceName):
        super ().__init__ (parent, instanceName)
    def __repr__ (self):
        return f'{self.name ()}:[{self.state["name"]}]'
    def enter (self):
        if debugHSM:
            print (f'entering {self}')
        self.state ["enter"] ()
    def enterDefault (self):
        self.state = self.defaultState
        self.enter ()
    def exit (self):
        if debugHSM:
            print (f'exiting {self}')
        if (self.state ["contains"]):
            self.state ["contains"].exit ()
        self.state ["exit"] ()
    def handle (self, message):
        if debugHSM:
            print (f'handling {self}...{message}')
        return self.state ["handle"] (message)

    def next (self, state):
        self.exit ()
        self.state = state
        self.enter ()
        
    # override abstract methods
    def reset (self):
        self.exit ()
        self.state = self.defaultState
        self.enter ()
        

    
