from component import Component

debugHSM = ''
class HSM (Component):
    def __init__ (self, parent, instanceName, defaultStateName, states):
        super ().__init__ (parent, instanceName)
        self.state = None
        self.defaultStateName = defaultStateName
        self.states = states
        
    def __repr__ (self):
        return f'{self.name ()}:[{self.state["name"]}]'

    def enter (self):
        print (f'entering {self.name ()}')
        self.enter ()
        self.state.enter ()

    def exit (self):
        print (f'exiting {self.name ()}')
        self.state.exit ()
        self.exit ()

    def enterDefault (self):
        self.state = self.lookupState (self.defaultStateName)
        self.enter ()

    def reset (self):
        self.exit ()
        self.enterDefault ()

    def handle (self):
        print (f'handling {self.name ()}')
        self.state.handle ()

    def next (self, nextState):
        self.state.exit ()
        self.state = nextState
        self.enter ()


# worker bees
    def lookupState (self, name):
        for state in self.states:
            if state.name == name:
                return state
        raise Exception (f'internal error: State /{name}/ not found in {self.name ()}') 
