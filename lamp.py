from email import message
from message import Message
from state import State
from hsm import HSM

from brightness import Brightness

class Lamp (HSM):

    def enter (self):
        super ().enter ()

    def exit (self):
        super ().exit ()

## state OFF:
    def enter_OFF (self):
        self.send ('state', 'off', None)

    def exit_OFF (self):
        pass

    def handle_OFF (self, message):
        if message.port == 'pwr': 
            self.next ('on')
            return True
        else:
            self.unhandledMessage (message)
            return False
        
## state ON:
    def enter_ON (self):
        self.send ('state', 'on', None)

    def exit_ON (self):
        pass

    def handle_ON (self, message):
        if message.port == 'pwr': 
            self.next ('off')
            return True
        else:
            self.unhandledMessage (message)
            return False
        
## create new instance
    def __init__ (self, parent, instanceName):
        off = State (parent=parent, name='off', enter=self.enter_OFF, exit=self.exit_OFF, handle=self.handle_OFF, subMachineClass=None)
        on = State (parent=parent, name='on', enter=self.enter_ON, exit=self.exit_ON, handle=self.handle_ON, subMachineClass=None)
        stateList = [off, on]
        super ().__init__ (parent, instanceName, 
                           enter=None, exit=None,
                           defaultStateName='off', states=stateList)
