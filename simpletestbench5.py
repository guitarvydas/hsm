from connection import Connection
from net import Net
from container import Container

class SimpleTestBench5 (Container):
    def __init__ (self, parent, instanceName):
        super ().__init__ (parent, instanceName)
        self.children = []
        net2 = Net ('n2', [(self, 'power')])
        self.nets = [net2]
        conn1 = Connection (self, 'start', net2)
        self.connections = [conn1]

        self.initializeContainerDefault ()
