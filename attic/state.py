class State:
    def __init__ (self, parent, name, enter, exit, handle, subMachineClass):
        self.machine = parent
        self.name = name
        self.enterFunction = enter
        self.exitFunction = exit
        self.handleFunction = handle
        self.subMachineClass = subMachineClass
        self.subMachine = None

    def __repr__ (self):
        return self.name
    
    def enter (self):
        if self.subMachineClass:
            self.subMachine = self.subMachineClass (self, f'[{self.subMachineClass}]')
        self.enterFUnction ()
        
    def exit (self):
        self.subMachine.exit ()
        self.exitFUnction ()

    def handle (self, message):
        r = self.handleFUnction (self, m)
        return r

    ... tbd ...
