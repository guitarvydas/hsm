from brightness import Brightness
from hsm import HSM

class Lamp (HSM):

    def enter_OFF (self):
        self.send ('state', 'off', None)
        self.state = self.states ["off"]
    def exit_OFF (self):
        self.send ('state', 'x-off', None)
    def handle_OFF (self, message):
        if ('pwr' == message.port):
            self.next (self.states ["on"])
            return True
        else:
            self.unhandledMessage (message)
        return False

    def enter_ON (self):
        self.send ('state', 'on', None)
        self.state = self.states ["on"]
        self.state ["sub"] = Brightness (self, 'brightness')
    def exit_ON (self):
        self.send ('state', 'x-on', None)
        pass
    def handle_ON (self, message):
        if ('pwr' == message.port):
            self.send ('power', True, message)
            self.next (self.states ["off"])
            return True
        elif self.state ["sub"].handle (message):
            return True
        else:
            self.unhandledMessage (message)
        return False


    def __init__ (self, parent, instanceName):
        super ().__init__ (parent, instanceName)
        off = {'name': 'off', 'enter': self.enter_OFF, 'exit': self.exit_OFF, 'handle': self.handle_OFF, 'sub': None}
        on = {'name' : 'on', 'enter': self.enter_ON, 'exit': self.exit_ON, 'handle': self.handle_ON, 'sub': None}
        self.states = { 'off': off, 'on' : on }
        self.defaultState = off
        self.enterDefault ()
        
