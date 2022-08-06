from connection import Connection
from net import Net
from container import Container
from lamptester import LampTester

class SimpleTestBench2 (Container):
    def __init__ (self, parent, instanceName):
        super ().__init__ (parent, instanceName)
        lamptester = LampTester (self, 'lamptester')
        self.children = [lamptester]
        net1 = Net ('n1', [(lamptester, 'start')])
        net2 = Net ('n2', [(self, 'power')])
        net4 = Net ('n4', [(self, 'colour')])
        self.nets = [net1, net2, net4]
        conn1 = Connection (self, 'start', net1)
        conn2 = Connection (lamptester, 'pwr', net2)
        conn3 = Connection (lamptester, 'brightness', None)
        conn4 = Connection (lamptester, 'colour', net4)
        self.connections = [conn1, conn2, conn3, conn4]

        self.initializeContainerDefault ()