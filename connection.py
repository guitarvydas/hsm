class Connection:
    def __init__ (self, instance, portname, net):
        self.instance = instance
        self.port = portname
        self.netref = net

    def net (self):
        return self.netref

    def hasSender (self, instance, portname):
        return (self.instance == instance an self.port == portname)
