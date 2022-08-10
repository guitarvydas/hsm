from leaf import Leaf
from container import Container

debugHSM = ''
class HSM (Leaf):
    def __init__ (self, parent, instanceName):
        super ().__init__ (parent, instanceName)
    def __repr__ (self):
        return f'{self.name ()}:[{self.state["name"]}]'

    def enter (self):
        self.enter ()
        self.state.enter ()

    def exit (self):
        self.state.exit ()
        self.exit ()

    def enterDefault (self):
        self.state = self.defaultState
        self.enter ()

    def reset (self):
        self.exit ()
        self.enterDefault ()

    def handle (self):
        self.state.handle ()

    def next (self, nextState):
        self.state.exit ()
        self.state = nextState
        self.enter ()

    def send (self, port, data):
        


enter machine:
  funcall machine entry
  enter state

exit machine:
  exit state
  funcall machine entry
pp
    def enter (self):
        if (debugHSM and debugHSM == 'full'):
            print (f'entering {self}')
        self.state ["enter"] ()
    def enterDefault (self):
        self.state = self.defaultState
        self.enter ()
    def exit (self):
        if (debugHSM and debugHSM == 'full'):
            print (f'exiting {self}')
        if (self.state ["sub"]):
            self.state ["sub"].exit ()
        self.state ["exit"] ()
    def handle (self, message):
        kind = 'Leaf'
        if isinstance (self, Container):
            kind = 'Container'
        if (debugHSM):
            print (f'handling HSM {kind} {self}...{message}')
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

    def delegate (self, message):
        if (self.state ["sub"]):
            return self.state ["sub"].handle (message)
        else:
            return False

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
        raise Exception (f'dequeueInput prohibited for SubHSM {self.name}')
    def send (self, portname, data, causingMessage):
        sender = self.parent
        sender.send (portname, data, causingMessage)
    #def unhandledMessage (self, message): <<inherited>>
    
