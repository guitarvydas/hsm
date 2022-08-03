from hsm import HSM
from colour import Colour

class Brightness (HSM):

    def enter_DIM (self):
        self.state = self.states ["dim"]
        self.state ["contained"] = Colour (self, 'dim colour')
    def exit_DIM (self):
        pass
    def handle_DIM (self, message):
        if ('brightness' == message.port):
            self.next (self.states ["mid"])
            return True
        elif self.state ["contained"]["handle"] (message):
            return True
        else:
            self.unhandledMessage (message, 'DIM')
        return False

    def enter_MID (self):
        self.state = self.states ["mid"]
        self.state ["contained"] = Colour (self, 'mid colour')
    def exit_MID (self):
        pass
    def handle_MID (self, message):
        if ('brightness' == message.port):
            self.next (self.states ["high"])
            return True
        elif self.state ["contained"] ["handle"] (message):
            return True
        else:
            self.unhandledMessage (message, 'MID')
        return False

    def enter_HIGH (self):
        self.state = self.states ["high"]
        self.state.contained = Colour (self, 'high colour')
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
        d = {'name': 'dim', 'enter': self.enter_DIM, 'exit': self.exit_DIM, 'handle': self.handle_DIM, 'contained': None}
        m = {'name': 'mid', 'enter': self.enter_MID, 'exit': self.exit_MID, 'handle': self.handle_MID, 'contained': None}
        h = {'name': 'high', 'enter': self.enter_HIGH, 'exit': self.exit_HIGH, 'handle': self.handle_HIGH, 'contained': None}
        self.states = {'dim': d, 'mid': m, 'high': h}
        self.defaultState = d
        self.enterDefault ()
        
        
