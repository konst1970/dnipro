from component import Component

class CurrentSource(Component):
    def __init__(self, _id, i, j, current):
        self.id = _id
        self.nodes = [i,j]
        self._args = current
    
    @property
    def args(self):
        return self._args
    
    @args.setter
    def args(self, current):
        self._args = current

    def add_OTM(self, circuit):
        # print ("I(", self.nodes[0], ",", self.nodes[1], ")=", self.args)
        # find my index in component list
        ind = circuit.components.index(self)
        # print ("Index=", ind)

        i = self.nodes[0]
        j = self.nodes[1]

        if (i > 0):
          circuit.A[ind, i-1] = -1
          circuit.A[len(circuit.components)+i-1,len(circuit.nodes)+ind-1] = -1

        if (j > 0):
          circuit.A[ind, j-1] = 1
          circuit.A[len(circuit.components)+j-1,len(circuit.nodes)+ind-1] = 1

        # -I
        circuit.A[ind, len(circuit.components)+len(circuit.nodes)-1+ind] = -1
        circuit.A[len(circuit.components)+len(circuit.nodes)-1+ind,
                 len(circuit.nodes)-1+ind] = 1
        circuit.b[len(circuit.components)+len(circuit.nodes)-1+ind] = self._args
    
    def __str__(self):
        return f"{CurrentSource.__name__}{self.id}"
