from component import Component
from connection import Connection
from net import Net
from message import Message

# A Container is slightly different from a Leaf in that
# Containers are composed of other Components, which ultimately boils down to Leaves
#  (in hierarchical pieces)
# A Container processes messages by delegating work to its child Components
# Containers do this delegation in a series of steps.
# Stepping must be done in a breadth-first manner, since one child might wake
#  another child up.
# A Container isn't finished working until all of innards have finished working.  This
#  means that a Container needs to wait until all internal messages have been processed
#  to completion (breadth-first, since one internal step might create new internal messages
#  all of which need to be processed to completion).

class Container (Component):
    def step (self):
        # delegate step to all children, if any of them did any work, return True
        workDone = self.stepAnyChild ()
        if workDone:
            return True
        # else all children have finished working and have not needed to be
        #  stepped, so, is there another input to be processed?
        # a Container isBusy() if any of its Children isBusy(), we must not consume another input
        #  until all Children are quiescent
        if self.isReady ():
            m = self.dequeueInput ()
            self.handle (m)
            return True
        return False
    def run (self):
        # finish processing one input to completion, don't consume the next input
        ## doWhile...
        if self.isReady ():
            m = self.dequeueInput ()
            self.handle (m)
        workDone = self.stepAnyChild ()
        while workDone:
            workDone = self.stepAnyChild ()
        ## end doWhile...
    def isBusy (self):
        for child in self.children:
            if child.isBusy ():
                return True
        return False
    def reset (self):
        for child in self.children:
            child.reset ()

    # internal
    def handle (self, message):
        net = self.findNet (self, message.port)
        self.route (message, net)
        
    def stepAnyChild (self):
        for child in self.children:
            childActed = child.step ()
            if childActed:
                self.routeChildOutputs (child)
                return True
        return False
            
    def enter (self):
        self.state = self.states ["default"]

    def noop (self):
        pass

    def findNet (self, instance, portname):
        # lookup instance/portname in connections and return the corresponding net
        for connection in self.connections:
            if connection.hasSender (instance, portname):
                return connection.net ()
        raise Exception (f'internal error: no connection for {instance.name ()}/{portname}')
            
    def route (self, message, net):
        if net:
            receiverList = net.receiverList ()
            for receiverTuple in receiverList:
                receiver = receiverTuple [0]
                port = receiverTuple [1]
                # Copy on write...
                m = Message (message.sender, port, message.value (), message.trail) 
                if (receiver == self):
                    m.updateState ('output')
                    receiver.enqueueOutput (m)
                else:
                    m.updateState ('input')
                    receiver.enqueueInput (m)

    def routeChildOutputs (self, child):
        outputs = child.outputQueue ().asDeque ()
        child.clearOutputs ()
        for message in outputs:
            net = self.findNet (child, message.port)
            self.route (message, net)

    def initializeContainerDefault (self):
        default = {'name': 'default', 'enter': self.noop, 'exit': self.noop, 'handle': self.handle, 'sub': None}
        self.states = { 'default': default }
        self.defaultState = default
        self.enter ()
    
