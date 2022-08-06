from connection import Connection
from net import Net
from container import Container
from lamptester import LampTester
from lamp import Lamp

class TestBench (Container):
    def __init__ (self, parent, instanceName):
        super ().__init__ (parent, instanceName)
        lamptester = LampTester (self, 'lamptester')
        lamp = Lamp (self, 'lamp')
        self.children = [lamptester, lamp]
        net1 = Net ('n1', [(lamptester, 'start')])
        net2 = Net ('n2', [(lamp, 'pwr')])
        net3 = Net ('n3', [(lamp, 'brightness')])
        net4 = Net ('n4', [(lamp, 'colour')])
        net5 = Net ('n5', [(self, 'lampstate')])
        self.nets = [net1, net2, net3, net4, net5]
        conn1 = Connection (self, 'start', net1)
        conn2 = Connection (lamptester, 'pwr', net2)
        conn3 = Connection (lamptester, 'brightness', net3)
        conn4 = Connection (lamptester, 'colour', net4)
        conn5 = Connection (lamp, 'state', net5)
        self.connections = [conn1, conn2, conn3, conn4, conn5]

        self.initializeContainerDefault ()
