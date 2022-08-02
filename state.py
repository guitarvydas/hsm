class State:
    def __init__ (self, parent, name, fenter, transitions, fexit):
        self.parent = parent
        self.name = name
        self.fenter = fenter
        self.transitions = transitions
        self.fexit = fexit
    def name (self):
        return f'[{self.parent.name ()}/{self.name}'
