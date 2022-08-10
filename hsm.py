from component import Component

debugHSM = ''
class HSM (Component):
    def __init__ (self, parent, instanceName, enter, exit, defaultStateName, states):
        super ().__init__ (parent, instanceName)
        self._machineEnter = enter
        self._machineExit = exit
        self._state = None
        self._defaultStateName = defaultStateName
        self._states = states
        self.enterDefault ()
        
    def __repr__ (self):
        return f'{self.name ()}:[{self._state.baseName ()}]'

    def enter (self):
        print (f'entering {self.name ()}')
        if self._machineEnter:
            self._machineEnter ()
        self._state.enter ()

    def exit (self):
        print (f'exiting {self.name ()}')
        self._state.exit ()
        if self._machineExit:
            self._machineExit ()

    def enterDefault (self):
        self._state = self.lookupState (self._defaultStateName)
        self.enter ()

    def reset (self):
        self.exit ()
        self.enterDefault ()

    def handle (self):
        print (f'handling {self.name ()}')
        self._state.handle ()

    def next (self, nextState):
        self._state.exit ()
        self._state = nextState
        self.enter ()

    def run (self):
        while self.isBusy () or self.isReady ():
            self.step ()

    # a raw state machine always completes a step when handle() is called
    # and is never busy
    # (This is different for composite state machines, like Containers)
    def step (self):
        pass
    
    def isBusy (self):
        return False


# worker bees
    def lookupState (self, name):
        for state in self._states:
            if state.baseName () == name:
                return state
        raise Exception (f'internal error: State /{name}/ not found in {self.name ()}') 
