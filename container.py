from component import Component

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
    def step:
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
        workDone = self.stepAnyChild ()
        while workDone:
            workDone = self.stepAnyChild ()
        ## end doWhile...
    def isBusy (self):
        for child in self.children:
            if isBusy (child):
                return True
        return False
    def reset (self):
        for child in self.children:
            child.reset ()

    # internal
    def stepAnyChild (self):
        for child in self.children:
            childActed = child.step ()
            if childActed:
                return True
        return False
            
    def noop (self):
        pass
    
