from email import message
from message import Message
from state import State
from hsmlayer import HSMLayer

class Colour (HSMLayer):

    def enter (self):
        super ().enter ()

    def exit (self):
        super ().exit ()

## state YELLOW:
    def enter_YELLOW (self):
        self.send ('state', '<yellow>', None)

    def exit_YELLOW (self):
        self.send ('state', '</yellow>', None)

    def handle_YELLOW (self, message):
        if message.port == 'colour': 
            self.next ('green')
            return True
        else:
            return False
        
## state GREEN:
    def enter_GREEN (self):
        self.send ('state', '<green>', None)

    def exit_GREEN (self):
        self.send ('state', '</green>', None)

    def handle_GREEN (self, message):
        if message.port == 'brightness': 
            self.next ('red')
            return True
        else:
            return False
        
## state RED:
    def enter_RED (self):
        self.send ('state', '<red>', None)

    def exit_RED (self):
        self.send ('state', '</red>', None)

    def handle_RED (self, message):
        if message.port == 'brightness': 
            self.next ('yellow')
            return True
        else:
            return False
        
## create new instance
    def __init__ (self, tophsm, layerName):
        yellow = State (machine=self, name='yellow', enter=self.enter_YELLOW, exit=self.exit_YELLOW, handle=self.handle_YELLOW, subMachineClass=None)
        green = State (machine=self, name='green', enter=self.enter_GREEN, exit=self.exit_GREEN, handle=self.handle_GREEN, subMachineClass=None)
        red = State (machine=self, name='red', enter=self.enter_RED, exit=self.exit_RED, handle=self.handle_RED, subMachineClass=None)
        stateList = [yellow, green, red]
        super ().__init__ (tophsm, layerName, 
                           enter=None, exit=None,
                           defaultStateName='yellow', states=stateList)
