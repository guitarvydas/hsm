from container import Container

class TestBench (Container):
    def __init__ (self, parent, instanceName):
        super ().__init__ (parent, instanceName)
        lamptester = LampTester (self, 'lamp tester')
        lamp = Lamp (self, 'lamp')
        self.children = [lamptester, lamp]
        net1 = Net ([lamptester, 'start'])
        net2 = Net ([lamp, 'pwr'])
        net3 = Net ([lamp, 'brightness'])
        net4 = Net ([lamp, 'colour'])
        self.nets = [net1, net2, net3, net4]
        conn1 = Connection (self, 'start', net1)
        conn2 = Connection (lamptester, 'pwr', net2)
        conn3 = Connection (lamptester, 'brightness', net3)
        conn4 = Connection (lamptester, 'colour', net4)
        self.connections = [conn1, conn2, conn3, conn4]

        self.initializeContainerDefault ()
