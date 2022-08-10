from fifo import FIFO
from message import Message

class Component:
    def __init__ (self, parent, name):
        self.parent = parent
        self.instanceName = name
        self.inputq = FIFO ()
        self.outputq = FIFO ()

    # external to-be-implemented in descendent
    def run (self):
        raise Exception (f'run must be overridden for {self.name}')
    def step (self, message):
        raise Exception (f'step must be overridden for {self.name}')
    def inject (self, message):
        self.inputq.enqueue (message)
    def isBusy (self):
        raise Exception ("isBusy not overridden")

    # external
    def outputs (self):
        # return a dictionary of FIFOs, one FIFO per output port
        resultdict = {}
        for message in self._outputq.asDeque ():
            if (not (message.port in resultdict)):
                resultdict [message.port] = FIFO ()
            resultdict [message.port].enqueue (message.data)
        self.clearOutputs ()
        resultdict2 = {}
        for key in resultdict:
            fifo = resultdict [key]
            resultdict2 [key] = fifo.asDeque ()
        return resultdict2
    def isReady (self):
        return (not self.inputq.isEmpty ())
    def name (self):
        if (None == self.parent):
            return self.instanceName
        else:
            return f'{self.parent.name ()}/{self.instanceName}'


    # internal
    def clearOutputs (self):
        self.outputq = FIFO ()

    def enqueueInput (self, message):
        self.inputq.enqueue (message)
        
    def enqueueOutput (self, message):
        self.outputq.enqueue (message)
        

    def dequeueInput (self):
        return self.inputq.dequeue ()
    def dequeueOutput (self):
        return self.outputq.dequeue ()
    
