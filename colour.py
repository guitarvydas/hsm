from hsm import HSM

class Colour (HSM):

        
    def enter_YELLOW (self):
        self.state = self.states ["yellow"]
    def exit_YELLOW (self):
        pass
    def handle_YELLOW (self, message):
        if ('brightness' == message.port):
            self.next (self.states ["green"])
            return True
        elif self.state.contained ["handle"] (message):
            return True
        else:
            self.unhandledMessage (message, 'YELLOW')
        return False

    def enter_GREEN (self):
        self.state = self.states ["green"]
    def exit_GREEN (self):
        pass
    def handle_GREEN (self, message):
        if ('brightness' == message.port):
            self.next (self.states ["red"])
            return True
        elif self.state.contained ["handle"] (message):
            return True
        else:
            self.unhandledMessage (message, 'GREEN')
        return False

    def enter_RED (self):
        self.state = self.states ["red"]
    def exit_RED (self):
        pass
    def handle_RED (self, message):
        if ('brightness' == message.port):
            self.next (self.states ["yellow"])
            return True
        elif self.state.contained.handle (message):
            return True
        else:
            self.unhandledMessage (message, 'RED')
        return False

        

    def __init__ (self, parent, instanceName):
        super ().__init__ (parent, instanceName)
        y = {'name': 'yellow', 'enter': self.enter_YELLOW, 'exit': self.exit_YELLOW, 'handle': self.handle_YELLOW, 'contained': None}
        g = {'name': 'green', 'enter': self.enter_GREEN, 'exit': self.exit_GREEN, 'handle': self.handle_GREEN, 'contained': None}
        r = {'name': 'red', 'enter': self.enter_RED, 'exit': self.exit_RED, 'handle': self.handle_RED, 'contained': None}
        self.states = {'yellow': y, 'green': g, 'red': r }
        self.defaultState = y
        self.enter (y)

        
