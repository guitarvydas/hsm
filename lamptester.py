from hsm import HSM

class LampTester (HSM):

    def enter_DEFAULT (self):
        self.state = self.states ["default"]
    def exit_DEFAULT (self):
        raise Exception (f'internal error: leaving default prohibited {self.name}')
    def handle_DEFAULT (self, message):
        if ('start' == message.port):
            self.send ('pwr', True, None)
            #self.send ('brightness', True, None)
            #self.send ('colour', True, None)
            return True
        else:
            self.unhandledMessage (message)
        return False

    def __init__ (self, parent, instanceName):
        super ().__init__ (parent, instanceName)
        default = {'name': 'default', 'enter': self.enter_DEFAULT, 'exit': self.exit_DEFAULT, 'handle': self.handle_DEFAULT, 'contains': None}
        self.states = { 'default': default }
        self.defaultState = default
        self.enterDefault ()
        
