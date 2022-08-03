from component import Component

class Colour (Component):

        
    def enter_YELLOW (self, e):
        self.state = self.states.off
        self.state.enter ()
    def exit_YELLOW (self, e):
        self.state.exit ()
    def handle_YELLOW (self, message, e):
        if ('brightness' == message.port):
            self.next (self.states.green)
            return True
        elif self.state.contained.handle (message):
            return True
        else:
            self.unhandledMessage (message, 'YELLOW', e)
        return False

    def enter_GREEN (self, e):
        self.state = self.states.off
        self.state.enter ()
    def exit_GREEN (self, e):
        self.state.exit ()
    def handle_GREEN (self, message, e):
        if ('brightness' == message.port):
            self.next (self.states.red)
            return True
        elif self.state.contained.handle (message):
            return True
        else:
            self.unhandledMessage (message, 'GREEN', e)
        return False

    def enter_RED (self, e):
        self.state = self.states.on
    def exit_RED (self, e):
        pass
    def handle_RED (self, message, e):
        if ('brightness' == message.port):
            self.next (self.states.yellow)
            return True
        elif self.state.contained.handle (message):
            return True
        else:
            self.unhandledMessage (message, 'RED', e)
        return False

    def enter (self):
        self.state = self.default
        self.state.enter ()
    def exit (self):
        self.state.exit ()
    def handle (self, message):
        self.state.handle (message)

    # override abstract methods
    def reset (self):
        self.exit ()
        self.enter ()
        
        

    def __init__ (self, parent, instanceName):
        super ().__init__ (parent, instanceName)
        y = {'enter': self.enter_YELLOW, 'exit': self.exit_YELLOW, 'handle': self.handle_YELLOW, 'contained': None}
        g = {'enter': self.enter_GREEN, 'exit': self.exit_GREEN, 'handle': self.handle_GREEN, 'contained': None}
        r = {'enter': self.enter_RED, 'exit': self.exit_RED, 'handle': self.handle_RED, 'contained': None}
        self.states = {'yellow': y, 'green': g, 'red': r }
        self.defaultState = y
        self.state = y

        
