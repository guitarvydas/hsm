from email import message
from message import Message
from state import State
from hsmlayer import HSMLayer

class Brightness (HSMLayer):

    def enter (self):
        super ().enter ()

    def exit (self):
        super ().exit ()

## state DIM:
    def enter_DIM (self):
        self.send ('state', '<dim>', None)

    def exit_DIM (self):
        self.send ('state', '</dim>', None)

    def handle_DIM (self, message):
        if message.port == 'brightness': 
            self.next ('mid')
            return True
        else:
            return False
        
## state MID:
    def enter_MID (self):
        self.send ('state', '<mid>', None)

    def exit_MID (self):
        self.send ('state', '</mid>', None)

    def handle_MID (self, message):
        if message.port == 'brightness': 
            self.next ('high')
            return True
        else:
            return False
        
## state HIGH:
    def enter_HIGH (self):
        self.send ('state', '<high>', None)

    def exit_HIGH (self):
        self.send ('state', '</high>', None)

    def handle_HIGH (self, message):
        if message.port == 'brightness': 
            self.next ('dim')
            return True
        else:
            return False
        
## create new instance
    def __init__ (self, tophsm, layerName):
        dim = State (machine=self, name='dim', enter=self.enter_DIM, exit=self.exit_DIM, handle=self.handle_DIM, subMachineClass=None)
        mid = State (machine=self, name='mid', enter=self.enter_MID, exit=self.exit_MID, handle=self.handle_MID, subMachineClass=None)
        high = State (machine=self, name='high', enter=self.enter_HIGH, exit=self.exit_HIGH, handle=self.handle_HIGH, subMachineClass=None)
        stateList = [dim, mid, high]
        super ().__init__ (tophsm, layerName, 
                           enter=None, exit=None,
                           defaultStateName='dim', states=stateList)
