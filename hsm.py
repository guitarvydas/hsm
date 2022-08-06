from leaf import Leaf
debugHSM = True
class HSM (Leaf):
    def __init__ (self, parent, instanceName):
        super ().__init__ (parent, instanceName)
    def __repr__ (self):
        return f'{self.name ()}:[{self.state["name"]}]'
    def enter (self):
        if debugHSM:
            print (f'entering {self}')
        self.state ["enter"] ()
    def enterDefault (self):
        self.state = self.defaultState
        self.enter ()
    def exit (self):
        if debugHSM:
            print (f'exiting {self}')
        if (self.state ["sub"]):
            self.state ["sub"].exit ()
        self.state ["exit"] ()
    def handle (self, message):
        if debugHSM:
            print (f'handling {self}...{message}')
        return self.state ["handle"] (message)

    def next (self, state):
        self.exit ()
        self.state = state
        self.enter ()
        
    # override abstract methods
    def reset (self):
        self.exit ()
        self.state = self.defaultState
        self.enter ()

class SubHSM (HSM):
    def __init__ (self, parent, instanceName):
        self.parent = parent
        self.instanceName = instanceName
        # inputq and outputq are those of parent HSM
    # external
    def run (self):
        raise Exception (f'run prohibited for SubHSM {self.name}')
    def step (self, message):
        raise Exception (f'step prohibitied for SubHSM {self.name}')
    def reset (self):
        raise Exception (f'reset prohibited for SubHSM {self.name}')
    def inject (self, message):
        raise Exception (f'inject prohibited for SubHSM {self.name}')
    def outputs (self):
        raise Exception (f'outputs prohibited for SubHSM {self.name}')
    def isReady (self):
        raise Exception (f'isReady prohibited for SubHSM {self.name}')
    def isBusy (self):
        raise Exception (f'isBusy prohibited for SubHSM {self.name}')
    #def name (self): <<inherited>>

    # internal
    def dequeueInput (self):
        raise Exception (f'dequeuInput prohibited for SubHSM {self.name}')
    def send (self, portname, data, causingMessage):
        sender = self.parent
        sender.send (portname, data, causingMessage)
    #def unhandledMessage (self, message): <<inherited>>
    
