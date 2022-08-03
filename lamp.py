from component import Component
from brightness import Brightness

class Lamp (Component):

    def __init__ (self, parent, instanceName):
        super ().__init__ (parent, instanceName)
        self.states.off = {enter: enter_OFF, exit: exit_OFF, handle = handle_OFF, contained: None}
        self.states.on = {enter: enter_ON, exit: exit_ON, handle = handle_ON, contained: Brightness ()}
        self.defaultstate = self.states.off
        self.state = self.defaultstate
        
    def enter_OFF (self, e):
        self.state = self.states.off
        self.state.enter ()
    def exit_OFF (self, e):
        self.state.exit ()
    def handle_OFF (self, message, e):
        if ('pwr' == message.port):
            self.next (self.states.on)
            return True
        else:
            self.unhandledMessage (message, 'OFF', e)
        return False

    def enter_ON (self, e):
        self.state = self.states.on
    def exit_ON (self, e):
        pass
    def handle_ON (self, message, e):
        if ('pwr' == message.port):
            self.next (self.states.off)
            return True
        elif self.state.contained.handle (message, e.contained):
            return True
        else:
            self.unhandledMessage (message, 'ON', e)
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
        
        
