from message import Message
from fifo import FIFO

class Component:
    def __init__ (self, parent, instanceName):
        self.parent = parent
        self.instanceName = instanceName
        self.inputq = FIFO ()
        self.outputq = FIFO ()

    # external
    def run (self):
        raise Exception (f'run must be overridden for {self.name}')
    def step (self, message):
        raise Exception (f'step must be overridden for {self.name}')
    def reset (self):
        raise Exception (f'reset must be overridden for {self.name}')
    def inject (self, message):
        self.inputq.enqueue (message)
    def outputs (self):
        # return a dictionary of FIFOs, one FIFO per output port
        resultdict = {}
        for message in self.outputq.asList ():
            if (not (message.port in resultdict)):
                resultdict [message.port] = FIFO ()
            resultdict [message.port].enqueue (message.data)
        self.outputq = FIFO () # discard outputq
        return resultdict
    def isReady (self):
        return (not self.inputq.isEmpty ())
    def isBusy (self):
        raise Exception ("isBusy not overridden")
    def name (self):
        if (None == self.parent):
            return self.instanceName
        else:
            return f'{self.parent.name ()}/{self.instanceName}'

    # internal
    def dequeueInput (self):
        return self.inputq.dequeue ()
    def send (self, portname, data, causingMessage):
        trail = [causingMessage, causingMessage.trail]
        m = Message (self, portname, data, trail)
        m.updateState ('output')
        self.outputq.enqueue (m)
    def handleNonMatchingMessage (self, message):
        # normal: just drop the message
        # but, in this POC, raise an error
        print ()
        print (f'unhandled message {message} for {self.hierarchicalName ()}')
        exit ()
