class State:
    def __init__ (self, parent, name, enter, exit, handle, subMachineClass):
        self._machine = parent
        self._name = name
        self._enter = enter
        self._exit = exit
        self._handle = handle
        self._subMachineClass = subMachineClass
        self._subMachine = None

    def __repr__ (self):
        return self.name
    
    def enter (self):
        if self._subMachineClass:
            self._subMachine = self._subMachineClass (self, f'[{self._subMachineClass}]')
        self._enter ()
        
    def exit (self):
        if self._subMachine:
            self._subMachine.exit ()
        self._exit ()

    def handle (self, message):
        r = self._handleFunction (self, message)
        return r

    def baseName (self):
        return self._name
