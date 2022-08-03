from component import Component
from colour import Colour

class Brightness (Component):

    def __init__ (self, parent, instanceName):
        super ().__init__ (parent, instanceName)
        self.states.yellow = {enter: enter_YELLOW, exit: exit_YELLOW, handle = handle_YELLOW, contained: Colour ()}
        self.states.green = {enter: enter_GREEN, exit: exit_GREEN, handle = handle_GREEN, contained: Colour ()}
        self.states.red = {enter: enter_RED, exit: exit_RED, handle = handle_RED, contained: Colour ()}
        self.defaultState = self.states.yellow
        self.state = self.defaultState

        
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
        
        
