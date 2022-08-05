from connection import Connection
from net import Net
from container import Container
from lamptester import LampTester
from lamp import Lamp

class SimpleTestBench (Container):
    def __init__ (self, parent, instanceName):
        super ().__init__ (parent, instanceName)
        lamptester = LampTester (self, 'lamp tester')
        self.children = [lamptester]
        net1 = Net ('n1', [(lamptester, 'start')])
        net2 = Net ('n2', [(lamptester, 'pwr')])
        self.nets = [net1, net2]
        conn1 = Connection (self, 'start', net1)
        conn2 = Connection (lamptester, 'pwr', net2)
        self.connections = [conn1, conn2]

        self.initializeContainerDefault ()
