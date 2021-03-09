import numpy
from component import Component

class Circuit():
    def __init__(self):
        self.nodes = []
        self.components = []
        self.A = numpy.zeros(shape=(1,1))
        self.b = numpy.zeros(shape=(1,1))
        self.x = numpy.zeros(shape=(1,1))
        self.size = 1

    def print(self):
        print(f"node -> {self.nodes}")
        self.print_components()
        print(f"size = {self.size}")
        self.print_matrix()
        print(f"x = {self.x}")

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
            component.add_OTM(self)

    def solve_DC(self):
        self.calc_all_nodes_OTM()
        self.x = numpy.linalg.solve(self.A, self.b)
    
    def print_components(self):
        lst = []
        for comp in self.components:
            lst.append(str(comp))
        print("elements -> ", lst)
    
    def print_matrix(self):
        line = ''
        for i in range(self.size):
            line = f"{numpy.array2string((self.A[i, :]), sign='+')}   {numpy.array2string((self.x[i, :]), sign='+')}   {numpy.array2string((self.b[i, :]), sign='+')}"

            if i == self.size // 2:
                line = f"{numpy.array2string((self.A[i, :]), sign='+')} * {numpy.array2string((self.x[i, :]), sign='+')} = {numpy.array2string((self.b[i, :]), sign='+')}" 
            
            print(line)