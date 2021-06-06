from math import sin
from component import Component

class CurrentSource(Component):
    def __init__(self, name: str, nodes: list, current: float, ac_current=None):
        self.name = name
        self.nodes = nodes
        self._args = current
        self.index = "Ampere"
        if ac_current:
            self.ac_current = ac_current
        else:
            self.ac_current = 0
    
    @property
    def args(self):
        return self._args
    
    @args.setter
    def args(self, current):
        self._args = current
    
    def time_func(self, start, step, iter):
        if self.ac_current == 0:
            return None
        if len(self.ac_current) == 3: # I = I0 * sin(w*t + phi)
            i = self.ac_current[0]
            w = self.ac_current[1]
            phi = self.ac_current[2]
            t = start + (step * iter)
            return i * sin(w*t + phi) 
        if len(self.ac_current) == 2: # I = I0 * t0, if t0 >= t => t0 = 1, else t0 = 0
            st = self.ac_current[1]
            t = start + (step * iter)
            if t >= st:
                return self.ac_current[0]
            else:
                return 0

    def add_OTM(self, circuit, start=None, step=None, iter=None):
        # print ("I(", self.nodes[0], ",", self.nodes[1], ")=", self.args)
        # find my index in component list
        if step == None:
            step = 0
        
        components_len = len(circuit.components)
        nodes_len = len(circuit.nodes)
        ind = circuit.components.index(self)
        # print ("Index=", ind)

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

        circuit.A[components_len+nodes_len-1+ind, nodes_len-1+ind] = 1

        if self.time_func(start, step, iter) == None:
            circuit.b[components_len+nodes_len-1+ind] = self._args
        else:
            circuit.b[components_len+nodes_len-1+ind] = self.time_func(start, step, iter)

    def refresh_OTM(self, circuit, vector, start, step, iter):
        components_len = len(circuit.components)
        nodes_len = len(circuit.nodes)
        ind = circuit.components.index(self)
        res = 0

        if self.ac_current == 0:
            res = 0
        elif len(self.ac_current) == 3: # I = I0 * sin(w*t + phi)
            i = self.ac_current[0]
            w = self.ac_current[1]
            phi = self.ac_current[2]
            t = start + (step * iter)
            res = i * sin(w*t + phi)
        elif len(self.ac_current) == 2: # I = I0 * t0, if t0 >= t => t0 = 1, else t0 = 0
            st = self.ac_current[1]
            t = start + (step * iter)
            if t >= st:
                res = self.ac_current[0]

        circuit.b[components_len+nodes_len-1+ind] = res

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
