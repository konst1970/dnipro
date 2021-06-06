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

    def add_OTM(self, circuit, start=None, step=None, iter=None):
        # print ("R(", self.nodes[0], ",", self.nodes[1], ")=", self.args)
        # find my index in component list
        if step == None:
            step = 0

        components_len = len(circuit.components)
        nodes_len = len(circuit.nodes)
        ind = circuit.components.index(self)

        i = self.nodes[0]
        j = self.nodes[1]

        if (i > 0):
          circuit.A[ind, i-1] = 1
          circuit.A[components_len+i-1, nodes_len+ind-1] = 1

        if (j > 0):
          circuit.A[ind, j-1] = -1
          circuit.A[components_len+j-1, nodes_len+ind-1] = -1

        # -I
        circuit.A[ind, components_len+nodes_len-1+ind] = -1

        # I
        circuit.A[components_len+nodes_len-1+ind, components_len+nodes_len-1+ind] = 1
        # R(j)
        circuit.A[components_len+nodes_len-1+ind, nodes_len-1+ind] = -self._args
    
    def refresh_OTM(self, circuit, vector, start, step, iter):
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
