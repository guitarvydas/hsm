from connection import Connection
from net import Net
from container import Container
from lamptester import LampTester
from lamp import Lamp

class TestBench (Container):
    def __init__ (self, parent, instanceName):
        super ().__init__ (parent, instanceName)
        lamptester = LampTester (self, '❲lamp tester❳')
        lamp = Lamp (self, 'lamp')
        self.children = [lamptester, lamp]
        net1 = Net ('n1', [(lamptester, 'start')])
        net2 = Net ('n2', [(lamp, 'pwr')])
        net3 = Net ('n3', [(lamp, 'brightness')])
        net4 = Net ('n4', [(lamp, 'colour')])
        net5 = Net ('n5', [(lamptester, 'power')])
        net6 = Net ('n6', [(lamptester, 'colour')])
        self.nets = [net1, net2, net3, net4, net5, net6]
        conn1 = Connection (self, 'start', net1)
        conn2 = Connection (lamptester, 'pwr', net2)
        conn3 = Connection (lamptester, 'brightness', net3)
        conn4 = Connection (lamptester, 'colour', net4)
        conn5 = Connection (lamp, 'power', net5)
        conn6 = Connection (lamp, 'colour', net6)
        self.connections = [conn1, conn2, conn3, conn4, conn5, conn6]

        self.initializeContainerDefault ()
