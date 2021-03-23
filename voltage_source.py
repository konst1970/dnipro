from component import Component

class VoltageSource(Component):
    def __init__(self, name: str, nodes, voltage):
        self.name = name
        self.nodes = nodes
        self._args = voltage
    
    @property
    def args(self):
        return self._args
    
    @args.setter
    def args(self, voltage):
        self._args = voltage
    
    def add_OTM(self, circuit):
        ind = circuit.components.index(self)

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
                 len(circuit.components)+len(circuit.nodes)-1+ind] = 1
        circuit.b[len(circuit.components)+len(circuit.nodes)-1+ind] = self._args

    def add_HM10(self, circuit):
        ind = circuit.components.index(self)

        i = self.nodes[0]
        j = self.nodes[1]

        # if i > 0 and j > 0:
        #     circuit.A[ind - 1, i - 1] = 1
        #     circuit.A[ind - 1, j - 1] = -1
        # elif i > 0 and j == 0:
        #     circuit.A[ind - 1, i - 1] = 1
        # elif i == 0 and j > 0:
        #     circuit.A[ind - 1, j - 1] = -1

        if i > 0:
            circuit.A[ind - 1, i - 1] = 1
            circuit.A[i - 1, ind - 1] = 1
        
        if j > 0:
            circuit.A[ind - 1, j - 1] = -1
            circuit.A[j - 1, ind - 1] = -1
        
        circuit.b[ind - 1] = self._args

    def __str__(self):
        if self.name:
            return f"{self.name}"
        return f"{VoltageSource.__name__}{self.id}"
