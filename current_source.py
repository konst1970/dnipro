from component import Component

class CurrentSource(Component):
    def __init__(self, name: str, nodes: list, current: float):
        self.name = name
        self.nodes = nodes
        self._args = current
        self.index = "Ampere"
    
    @property
    def args(self):
        return self._args
    
    @args.setter
    def args(self, current):
        self._args = current

    def add_OTM(self, circuit, step=None):
        # print ("I(", self.nodes[0], ",", self.nodes[1], ")=", self.args)
        # find my index in component list
        if step == None:
            step = 0
        
        ind = circuit.components.index(self)
        # print ("Index=", ind)

        i = self.nodes[0]
        j = self.nodes[1]

        if (i > 0):
          circuit.A[ind, i-1] = 1
          circuit.A[len(circuit.components)+i-1,len(circuit.nodes)+ind-1] = 1

        if (j > 0):
          circuit.A[ind, j-1] = -1
          circuit.A[len(circuit.components)+j-1,len(circuit.nodes)+ind-1] = -1

        # -I
        circuit.A[ind, len(circuit.components)+len(circuit.nodes)-1+ind] = -1

        circuit.A[len(circuit.components)+len(circuit.nodes)-1+ind,
                 len(circuit.nodes)-1+ind] = 1

        circuit.b[len(circuit.components)+len(circuit.nodes)-1+ind] = self._args

    def refresh_OTM(self, circuit, vector, step, ):
        pass

    def add_HM10(self, circuit):
        i = self.nodes[0]
        j = self.nodes[1]

        if i > 0:
            circuit.b[i - 1] = -self._args
        if j > 0:
            circuit.b[j - 1] = self._args
    
    def __str__(self):
        if self.name:
            return f"{self.name}"
        return f"{CurrentSource.__name__}{self.id}"
