class Transition:
    def __init__ (self, state, port, function, nextStateName, nextStateEntryFunction, nextStateExitFunction):
        self.state = state
        self.port = port
        self.function = function
        self.nextStateName = nextStateName
        self.nextStateEntryFunction = nextStateEntryFunction
        self.nextStateExitFunction = nextStateExitFunction
    def isNoChange (self):
        return (self.next == None or self.next = '.')
