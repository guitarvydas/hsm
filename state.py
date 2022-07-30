class State:
    def __init__ (self, parent, name, fenter, fhandler, fexit):
        self.parent = parent
        self.name = name
        self.fenter = fenter
        self.fhandler = fhandler
        self.fexit = fexit
    def name (self):
        return f'[{self.parent.name ()}/{self.name}'
