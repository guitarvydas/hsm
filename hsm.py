from component import Component
class HSM (Component):
    def __init__ (self, parent, instanceName):
        super ().__init__ (parent, instanceName)
    def enter (self):
        self.state = self.default
        self.state.enter ()
    def exit (self):
        self.state.exit ()
    def handle (self, message):
        self.state.handle (message)
    # override abstract methods
    def reset (self):
        self.exit ()
        self.enter ()
        

    
