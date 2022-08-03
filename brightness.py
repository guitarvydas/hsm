from hsm import HSM
from colour import Colour

class Brightness (HSM):

    def enter_DIM (self, e):
        self.state = self.states.off
        self.state.enter ()
    def exit_DIM (self, e):
        self.state.exit ()
    def handle_DIM (self, message, e):
        if ('brightness' == message.port):
            self.next (self.states.mid)
            return True
        elif self.state.contained.handle (message):
            return True
        else:
            self.unhandledMessage (message, 'DIM', e)
        return False

    def enter_MID (self, e):
        self.state = self.states.off
        self.state.enter ()
    def exit_MID (self, e):
        self.state.exit ()
    def handle_MID (self, message, e):
        if ('brightness' == message.port):
            self.next (self.states.high)
            return True
        elif self.state.contained.handle (message):
            return True
        else:
            self.unhandledMessage (message, 'MID', e)
        return False

    def enter_HIGH (self, e):
        self.state = self.states.on
    def exit_HIGH (self, e):
        pass
    def handle_HIGH (self, message, e):
        if ('brightness' == message.port):
            self.next (self.states.dim)
            return True
        elif self.state.contained.handle (message):
            return True
        else:
            self.unhandledMessage (message, 'HIGH', e)
        return False



    def __init__ (self, parent, instanceName):
        super ().__init__ (parent, instanceName)
        d = {'enter': self.enter_DIM, 'exit': self.exit_DIM, 'handle': self.handle_DIM, 'contained': Colour (self, 'dim colour')}
        m = {'enter': self.enter_MID, 'exit': self.exit_MID, 'handle': self.handle_MID, 'contained': Colour (self, 'mid colour')}
        h = {'enter': self.enter_HIGH, 'exit': self.exit_HIGH, 'handle': self.handle_HIGH, 'contained': Colour (self, 'high colour')}
        self.states = {'dim': d, 'mid': m, 'high': h}
        self.defaultState = d
        self.state = d
        
        
