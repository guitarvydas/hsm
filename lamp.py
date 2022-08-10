from message import Message
from state import State
from hsm import HSM

class Lamp (HSM):

    def __repr__ (self):
        return f'Lamp[{self.name ()}:{self.state["name"]}]'

    def enter (self):
        super ().enter ()

    def exit (self):
        super ().exit ()

## state OFF:
    def enter_OFF (self):
        super ().enter ()

    def exit_OFF (self):
        super ().exit ()

    def handle_OFF (self, message):
        super ().handle (message)
        if message.port == 'pwr': 
            self.next ('on')
            return True
        elif self.delegate (message):
            return True
        else:
            self.unhandledMessage (message)
            return False
        
## state ON:
    def enter_ON (self):
        super ().enter ()

    def exit_ON (self):
        super ().exit ()

    def handle_ON (self, message):
        super ().handle (message)
        if message.port == 'pwr': 
            self.next ('off')
            return True
        elif self.delegate (message):
            return True
        else:
            self.unhandledMessage (message)
            return False
        
## create new instance
    def __init__ (self, parent, instanceName):
        off = State (parent=parent, name='off', enter=self.enter_OFF, exit=self.exit_OFF, handle=self.handle_OFF, subMachineClass=None)
        on = State (parent=parent, name='on', enter=self.enter_ON, exit=self.exit_ON, handle=self.handle_ON, subMachineClass=None)
        stateList = [off, on]
        super ().__init__ (parent, instanceName, defaultStateName='off', states=stateList)
