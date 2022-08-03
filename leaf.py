from component import Component

class Leaf (Component):
    def __init__ (self, parent, instanceName):
        super ().__init__(parent, instanceName)
    def isBusy (self):
        return False

    # override abstract methods
    def step (self):
        # return True if any work has been done, else False
        # Leaf finishes processing a message completely, hence,
        # can be stepped if there is anything in the input queue
        # (Containers need to worry about stepping their children, but Leaves don't worry about stepping Children - this is a Leaf)
        if self.isReady ():
            m = self.dequeueInput ()
            self.handle (m)
            return True
        return False
