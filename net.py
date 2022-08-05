class Net:
    def __init__ (self, name, receiverList):
        self.name = name
        self.receivers = receiverList
    def __repr__ (self):
        return f'<net {self.name} {self.receivers}>'
    def receiverList (self):
        return self.receivers
