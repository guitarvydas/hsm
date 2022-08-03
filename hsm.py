from leaf import Leaf
class HSM (Leaf):
    def __init__ (self, parent, instanceName):
        super ().__init__ (parent, instanceName)
    def enter (self, state):
        self.state = state
        print (f'{self.name ()} entering {state["name"]}')
        state["enter"] ()
    def exit (self):
        print (f'{self.name ()} exiting {self.state["name"]}')
        self.state ["exit"] ()
    def handle (self, message):
        print (f'{self.name ()} handling {self.state["name"]}')
        self.state ["handle"] (message)

    def next (self, state):
        self.exit ()
        state ["enter"] ()
        
    # override abstract methods
    def reset (self):
        self.state ["exit"] ()
        self.state ["enter"] ()
        

    
