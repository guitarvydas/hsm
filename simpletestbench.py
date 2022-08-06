from connection import Connection
from net import Net
from container import Container
from lamptester import LampTester
from lamp import Lamp

class SimpleTestBench (Container):
    def __init__ (self, parent, instanceName):
        super ().__init__ (parent, instanceName)
        lamptester = LampTester (self, '❲lamp tester❳')
        self.children = [lamptester]
        net1 = Net ('n1', [(lamptester, 'start')])
        net2 = Net ('n2', [(self, 'power')])
        self.nets = [net1, net2]
        conn1 = Connection (self, 'start', net1)
        conn2 = Connection (lamptester, 'pwr', net2)
        conn3 = Connection (lamptester, 'brightness', None)
        conn4 = Connection (lamptester, 'colour', None)
        self.connections = [conn1, conn2, conn3, conn4]

        self.initializeContainerDefault ()