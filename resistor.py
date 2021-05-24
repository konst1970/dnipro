from component import Component

class Resistor(Component):
    def __init__(self, name: str, nodes: list, resistance: float):
        self.name = name
        self.nodes = nodes
        self._args = resistance
        self.index = "Ohm"
    
    @property
    def args(self):
        return self._args
    
    @args.setter
    def args(self, resistance):
        self._args = resistance

    def add_OTM(self, circuit, step):
        # print ("R(", self.nodes[0], ",", self.nodes[1], ")=", self.args)
        # find my index in component list
        if step == None:
            step = 0

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

        # I
        circuit.A[len(circuit.components)+len(circuit.nodes)-1+ind,
                  len(circuit.components)+len(circuit.nodes)-1+ind] = 1
        # R(j)
        circuit.A[len(circuit.components)+len(circuit.nodes)-1+ind,
                 len(circuit.nodes)-1+ind] = -self._args
    
    def refresh_OTM(self, circuit, vector, step,):
        pass
    
    def add_HM10(self, circuit):
        i = self.nodes[0]
        j = self.nodes[1]

        if i > 0 and j > 0:
            circuit.A[i - 1, i - 1] += 1 / self._args
            circuit.A[i - 1, j - 1] += -1 / self._args
            circuit.A[j - 1, i - 1] += -1 / self._args
            circuit.A[j - 1, j - 1] += 1 / self._args
        elif i > 0 and j == 0:
            circuit.A[i - 1, i - 1] += 1 / self._args
        elif i == 0 and j > 0:
            circuit.A[j - 1, j - 1] += -1 / self._args


    def __str__(self):
        if self.name:
            return f"{self.name}"
        return f"{Resistor.__name__}"
