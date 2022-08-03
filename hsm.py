from leaf import Leaf
class HSM (Leaf):
    def __init__ (self, parent, instanceName):
        super ().__init__ (parent, instanceName)
    def enter (self):
        print (f'{self.name ()} entering {self.state["name"]}')
        self.state ["enter"] ()
    def enterDefault (self):
        self.state = self.defaultState
        self.enter ()
    def exit (self):
        print (f'{self.name ()} exiting {self.state["name"]}')
        self.state ["exit"] ()
    def handle (self, message):
        print (f'{self.name ()} handling {self.state["name"]}')
        self.state ["handle"] (message)

    def next (self, state):
        self.exit ()
        self.state = state
        self.enter ()
        
    # override abstract methods
    def reset (self):
        self.exit ()
        self.state = self.defaultState
        self.enter ()
        

    
