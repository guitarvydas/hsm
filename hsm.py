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
        return f'{self._state.name ()}'

    def fullName (self):
        return f'{self.name ()}[{self._state.fullName ()}]'

    def enter (self):
        print (f'entering {self.fullName ()}')
        if self._machineEnter:
            self._machineEnter ()
        self._state.enter ()

    def exit (self):
        print (f'exiting {self.fullName ()}')
        self._state.exit ()
        if self._machineExit:
            self._machineExit ()

    def enterDefault (self):
        self._state = self.lookupState (self._defaultStateName)
        self.enter ()

    def reset (self):
        self.exit ()
        self.enterDefault ()

    def handle (self, message):
        print (f'handling {self.fullName ()}')
        self._state.handle (message)

    def next (self, nextStateName):
        self.exit ()
        self._state = self.lookupState (nextStateName)
        self.enter ()

    def run (self):
        while self.isBusy ():
            self.step ()
        while self.handleIfReady ():
            while self.isBusy ():
                self.step()


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
            if state.name () == name:
                return state
        raise Exception (f'internal error: State /{name}/ not found in {self.name ()}') 

    def handleIfReady (self):
        if self.isReady ():
            m = self.dequeueInput ();
            self.handle (m)
            return True
        else:
            return False
