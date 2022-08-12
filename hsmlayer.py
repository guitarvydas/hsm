from hsm import HSM

class HSMLayer (HSM):
    ## An HSMLayer is a part of a larger HSM
    ## An HSMLayer is mostly an HSM, except for the Component fields
    ##  (i.e. an HSMLayer is sync, whereas an HSM is async
    ##   ; an HSMLayer is a piece of an async HSM)
    ## Send () in an HSMLayer refers to the outer HSM wrapper
    ## There's probably a more efficient way to structure HSMLayer, but that's a future consideration
    ## The catch is that Send () cannot be implemented blindly using CALL/RETURN (as would
    ##  happen in a standard class-based approach)
    ## Likewise, name () cannot invoke Component/name and must bottom-out here
    
    def __init__ (self, tophsm, layerName, enter, exit, defaultStateName, states):
        super ().__init__ (None, '', enter, exit, defaultStateName, states)
        self._topHSM = tophsm
        self._layerName = layerName
        self._parent = None
        self._instanceName = ''
        self._inputq = None
        self._outputq = None
        
    def send (self, portname, data, causingMessage):
        self._topHSM.send (portname, data, causingMessage)

    def name (self):
        return self._layerName
