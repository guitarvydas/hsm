from hsm import SubHSM

class Colour (SubHSM):

        
    def enter_YELLOW (self):
        self.send ('yellow', True, None)
        self.state = self.states ["yellow"]
    def exit_YELLOW (self):
        pass
    def handle_YELLOW (self, message):
        if ('colour' == message.port):
            self.next (self.states ["green"])
            return True
        elif self.state.contains ["handle"] (message):
            return True
        else:
            self.unhandledMessage (message, 'YELLOW')
        return False

    def enter_GREEN (self):
        self.send ('green', True, None)
        self.state = self.states ["green"]
    def exit_GREEN (self):
        pass
    def handle_GREEN (self, message):
        if ('colour' == message.port):
            self.next (self.states ["red"])
            return True
        elif self.state.contains ["handle"] (message):
            return True
        else:
            self.unhandledMessage (message, 'GREEN')
        return False

    def enter_RED (self):
        self.send ('red', True, None)
        self.state = self.states ["red"]
    def exit_RED (self):
        pass
    def handle_RED (self, message):
        if ('colour' == message.port):
            self.next (self.states ["yellow"])
            return True
        elif self.state.contains.handle (message):
            return True
        else:
            self.unhandledMessage (message, 'RED')
        return False

        

    def __init__ (self, parent, instanceName):
        super ().__init__ (parent, instanceName)
        y = {'name': 'yellow', 'enter': self.enter_YELLOW, 'exit': self.exit_YELLOW, 'handle': self.handle_YELLOW, 'contains': None}
        g = {'name': 'green', 'enter': self.enter_GREEN, 'exit': self.exit_GREEN, 'handle': self.handle_GREEN, 'contains': None}
        r = {'name': 'red', 'enter': self.enter_RED, 'exit': self.exit_RED, 'handle': self.handle_RED, 'contains': None}
        self.states = {'yellow': y, 'green': g, 'red': r }
        self.defaultState = y
        self.enterDefault ()

        
