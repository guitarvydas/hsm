from connection import Connection
from net import Net
from container import Container
from lamptester import LampTester

class MidTester4 (Container):
    def __init__ (self, parent, instanceName):
        super ().__init__ (parent, instanceName)
        lamptester = LampTester (self, 'lamptester')
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

class SimpleTestBench4 (Container):
    def __init__ (self, parent, instanceName):
        super ().__init__ (parent, instanceName)
        midtester = MidTester4 (self, 'midtester')
        self.children = [midtester]
        net101 = Net ('n101', [(midtester, 'start')])
        net102 = Net ('n102', [(self, 'power')])
        self.nets = [net101, net102]
        conn1 = Connection (self, 'start', net101)
        conn2 = Connection (midtester, 'pwr', net102)
        self.connections = [conn1, conn2]
        self.initializeContainerDefault ()
        
