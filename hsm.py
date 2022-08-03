from component import Component
class HSM (Component):
    def __init__ (self, parent, instanceName):
        super ().__init__ (parent, instanceName)
    def enter (self, state):
        self.state = state
        print (f'{self.name ()} entering {state["name"]}')
        state["enter"] ()
    def exit (self):
        print (f'{self.name ()} exiting {self.state["name"]}')
        self.state.exit ()
    def handle (self, message):
        print (f'{self.name ()} handling {self.state["name"]}')
        self.state.handle (message)
    # override abstract methods
    def reset (self):
        self.exit ()
        self.enter ()
        

    
