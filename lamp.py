from component import Component

class Lamp (Component):
    self.enter = None
    self.exit = None
    self.handle = None
    def enter_OFF (self, e):
        self.enter = enter_OFF
        self.exit = exit_OFF
        self.handle = handle_OFF
    def exit_OFF (self, e):
        pass
    def handle_OFF (self, message, e):
        if ('pwr' == message.port):
            self.next (enter_ON, handle_ON, exit_ON)
            self.send ('success', True)
        else:
            self.unhandledMessage (message, 'OFF', e)
        self.send ('success', False)

    def enter_ON (self, e):
        s = self.lookupState ('ON')
        self.on.brightness = Brightness ()
        self.enter = enter_ON
        self.exit = exit_ON
        self.handle = handle_ON
    def exit_ON (self, e):
        pass
    def handle_ON (self, message, e):
        if ('pwr' == message.port):
            self.next (enter_OFF, handle_OFF, exit_OFF)
            self.send ('success', True)
        elif self.on.brightness.handle (message, e.child):
            self.send ('success', True)
        else:
            self.unhandledMessage (message, 'ON', e)
        self.send ('success', False)

    self.default_ENTER = enter_OFF

    def enter (self):
        self.machineHandle = self.default_ENTER
        self.machineHandle ()
    def exit (self):
        self.machineExit ()
    def handle (self, message):
        self.machineHandle (message)
