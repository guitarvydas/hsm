from hsm import SubHSM
from colour import Colour

class Brightness (SubHSM):

    def enter_DIM (self):
        self.send ('state', 'dim', None)
        self.state = self.states ["dim"]
        self.state ["sub"] = Colour (self, 'dim')
    def exit_DIM (self):
        self.send ('state', 'x-dim', None)
    def handle_DIM (self, message):
        if ('brightness' == message.port):
            self.next (self.states ["mid"])
            return True
        elif self.state ["sub"].handle (message):
            return True
        else:
            self.unhandledMessage (message)
        return False

    def enter_MID (self):
        self.send ('state', 'mid', None)
        self.state = self.states ["mid"]
        self.state ["sub"] = Colour (self, 'mid')
    def exit_MID (self):
        self.send ('state', 'x-mid', None)
    def handle_MID (self, message):
        if ('brightness' == message.port):
            self.next (self.states ["high"])
            return True
        elif self.state ["sub"].handle (message):
            return True
        else:
            self.unhandledMessage (message)
        return False

    def enter_HIGH (self):
        self.send ('state', 'high', None)
        self.state = self.states ["high"]
        self.state.sub = Colour (self, 'high')
    def exit_HIGH (self):
        self.send ('state', 'x-high', None)
    def handle_HIGH (self, message):
        if ('brightness' == message.port):
            self.next (self.states ["dim"])
            return True
        elif self.state ["sub"].handle (message):
            return True
        else:
            self.unhandledMessage (message)
        return False



    def __init__ (self, parent, instanceName):
        super ().__init__ (parent, instanceName)
        d = {'name': 'dim', 'enter': self.enter_DIM, 'exit': self.exit_DIM, 'handle': self.handle_DIM, 'sub': None}
        m = {'name': 'mid', 'enter': self.enter_MID, 'exit': self.exit_MID, 'handle': self.handle_MID, 'sub': None}
        h = {'name': 'high', 'enter': self.enter_HIGH, 'exit': self.exit_HIGH, 'handle': self.handle_HIGH, 'sub': None}
        self.states = {'dim': d, 'mid': m, 'high': h}
        self.defaultState = d
        self.enterDefault ()
        
        
