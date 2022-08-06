from connection import Connection
from net import Net
from container import Container
from lamptester import LampTester

class SimpleTestBench3 (Container):
    def __init__ (self, parent, instanceName):
        super ().__init__ (parent, instanceName)
        lamptesterA = LampTester (self, 'lamptesterA')
        lamptesterB = LampTester (self, 'lamptesterB')
        self.children = [lamptesterA, lamptesterB]
        net1 = Net ('n1', [(lamptesterA, 'start')])
        net2 = Net ('n2', [(lamptesterB, 'start')])
        net3 = Net ('n3', [(self, 'power')])
        self.nets = [net1, net2, net3]
        conn1 = Connection (self, 'start', net1)
        conn2 = Connection (lamptesterA, 'pwr', net2)
        conn3 = Connection (lamptesterA, 'brightness', None)
        conn4 = Connection (lamptesterA, 'colour', None)
        conn12 = Connection (lamptesterB, 'pwr', net3)
        conn13 = Connection (lamptesterB, 'brightness', None)
        conn14 = Connection (lamptesterB, 'colour', None)
        self.connections = [conn1, conn2, conn3, conn4, conn12, conn13, conn14]

        self.initializeContainerDefault ()
