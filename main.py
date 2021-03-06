import numpy

class Component():
    def __init__(self, nodes, args):
        self.nodes = nodes
        self.args = args

    def add(self, circuit): # must be overloaded in each component
        return 0

    def print(self):
        print(self.nodes)
        print(self.args)

class Resistor(Component):
    def __init__(self, i, j, resistance):
        self.nodes = [i,j]
        self.args = resistance

    def add(self, circuit):
        # print ("R(", self.nodes[0], ",", self.nodes[1], ")=", self.args)
        # find my index in component list
        ind = circuit.components.index (self)
        # print ("Index=", ind)

        i = self.nodes[0]
        j = self.nodes[1]

        if (i > 0):
          circuit.A[ind, i-1] = -1
          circuit.A[len(circuit.components)+i-1,len(circuit.nodes)+ind-1] = -1

        if (j > 0):
          circuit.A[ind, j-1] = 1
          circuit.A[len(circuit.components)+j-1,len(circuit.nodes)+ind-1] = 1

        circuit.A[ind, len(circuit.components)+len(circuit.nodes)-1+ind] = -1
        circuit.A[len(circuit.components)+len(circuit.nodes)-1+ind,
                  len(circuit.components)+len(circuit.nodes)-1+ind] = 1
        circuit.A[len(circuit.components)+len(circuit.nodes)-1+ind,
                 len(circuit.nodes)-1+ind] = -self.args



class VoltageSource(Component):
    def __init__(self, i, j, voltage):
        self.nodes = [i,j]
        self.args = voltage

class CurrentSource(Component):
    def __init__(self, i, j, current):
        self.nodes = [i,j]
        self.args = current

    def add(self, circuit):
        # print ("I(", self.nodes[0], ",", self.nodes[1], ")=", self.args)
        # find my index in component list
        ind = circuit.components.index (self)
        # print ("Index=", ind)

        i = self.nodes[0]
        j = self.nodes[1]

        if (i > 0):
          circuit.A[ind, i-1] = -1
          circuit.A[len(circuit.components)+i-1,len(circuit.nodes)+ind-1] = -1

        if (j > 0):
          circuit.A[ind, j-1] = 1
          circuit.A[len(circuit.components)+j-1,len(circuit.nodes)+ind-1] = 1

        circuit.A[ind, len(circuit.components)+len(circuit.nodes)-1+ind] = -1
        circuit.A[len(circuit.components)+len(circuit.nodes)-1+ind,
                 len(circuit.nodes)-1+ind] = -1
        circuit.b[len(circuit.components)+len(circuit.nodes)-1+ind] = -self.args


class Circuit():
    def __init__(self):
        self.nodes = []
        self.components = []
        self.A = numpy.zeros(shape=(1,1))
        self.b = numpy.zeros(shape=(1,1))
        self.x = numpy.zeros(shape=(1,1))
        self.size = 1

    def print(self):
        print(self.nodes)
        print(self.components)
        print(self.size)
        print(self.A)
        print(self.b)
        print(self.x)

    def add_component(self, component):
        self.components = self.components + [component]
        self.nodes = list(set(self.nodes) | set(component.nodes)) # add new nodes to list

    def add_components(self, component_list):
        for component in component_list:
            self.add_component(component)

    def calc_all_nodes_OTM(self):
        self.size = len(self.nodes)-1 + 2*len(self.components)
        self.A = numpy.zeros(shape=(self.size,self.size))
        self.b = numpy.zeros(shape=(self.size,1))
        self.x = numpy.zeros(shape=(self.size,1))

        for component in self.components:
            component.add(self)

    def solve(self):
        self.calc_all_nodes_OTM()
        self.x = numpy.linalg.solve(self.A, self.b)

def run_test_circuit(name):
    R1 = Resistor(0, 1, 2) # 2 Ohm
    R2 = Resistor(2, 1, 1) # 1 Ohm
    R3 = Resistor(0, 2, 1) # 1 Ohm
    I1 = CurrentSource(0, 1, 1) # 1 Amper

    # V1 = VoltageSource(0, 2, 1) # 1 Volt

    test_circuit = Circuit()
    test_circuit.add_components([R1, R2, R3, I1])

    test_circuit.solve()

    test_circuit.print()

if __name__ == '__main__':
    print("DNIPRO v.0.0.1 (c) 2021, all rights reserved")
    run_test_circuit("Test Circuit")
    
