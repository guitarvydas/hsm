from hsm import HSM
from colour import Colour

class Brightness (HSM):

    def enter_DIM (self):
        self.state = self.states ["dim"]
    def exit_DIM (self):
        pass
    def handle_DIM (self, message):
        if ('brightness' == message.port):
            self.next (self.states ["mid"])
            return True
        elif self.state.contained ["handle"] (message):
            return True
        else:
            self.unhandledMessage (message, 'DIM')
        return False

    def enter_MID (self):
        self.state = self.states ["mid"]
    def exit_MID (self):
        pass
    def handle_MID (self, message):
        if ('brightness' == message.port):
            self.next (self.states ["high"])
            return True
        elif self.state.contained ["handle"] (message):
            return True
        else:
            self.unhandledMessage (message, 'MID')
        return False

    def enter_HIGH (self):
        self.state = self.states ["high"]
    def exit_HIGH (self):
        pass
    def handle_HIGH (self, message):
        if ('brightness' == message.port):
            self.next (self.states ["dim"])
            return True
        elif self.state.contained ["handle"] (message):
            return True
        else:
            self.unhandledMessage (message, 'HIGH')
        return False



    def __init__ (self, parent, instanceName):
        super ().__init__ (parent, instanceName)
        d = {'name': 'dim', 'enter': self.enter_DIM, 'exit': self.exit_DIM, 'handle': self.handle_DIM, 'contained': Colour (self, 'dim colour')}
        m = {'name': 'mid', 'enter': self.enter_MID, 'exit': self.exit_MID, 'handle': self.handle_MID, 'contained': Colour (self, 'mid colour')}
        h = {'name': 'high', 'enter': self.enter_HIGH, 'exit': self.exit_HIGH, 'handle': self.handle_HIGH, 'contained': Colour (self, 'high colour')}
        self.states = {'dim': d, 'mid': m, 'high': h}
        self.defaultState = d
        self.enter (d)
        
        
