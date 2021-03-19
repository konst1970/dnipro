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
    
    def calc_all_nodes_HM10(self):
        num = 0
        for component in self.components:
            if str(component).find('Voltage') > -1 or str(component).find('Inductor') > -1:
                num = num + 1
        
        self.size = len(self.nodes) + num - 1
        self.A = numpy.zeros(shape=(self.size, self.size))
        self.b = numpy.zeros(shape=(self.size, 1))
        self.x = numpy.zeros(shape=(self.size, 1))

        for component in self.components:
            component.add_HM10(self)
    
    def calc_nodes_HM5(self, tree: list, cord: list):
        self.A = numpy.zeros(shape=(len(self.components), len(self.nodes) - 1))
        B = numpy.zeros(shape=(len(cord), len(tree)))
        D = numpy.zeros(shape=(len(tree), len(cord)))

        T_ones = numpy.ones(len(tree), len(tree))
        L_ones = numpy.ones(len(cord), len(cord))

        for component in self.components:
            component.add_HM5(self)
        
        At = []
        for i in tree:
            At.append(self.A[i - 1, :])
        At = numpy.array(At).transpose()
        minus_At_ob = numpy.subtract(numpy.zeros(shape=(len(tree), len(tree))), numpy.linalg.inv(At))
        Al = []
        for i in cord:
            Al.append(self.A[i - 1, :])
        Al = numpy.array(Al).transpose()

        B = numpy.matmul(minus_At_ob, Al).transpose()
        D =  numpy.subtract(numpy.zeros(shape=(len(tree), len(tree))), B).transpose()
        
        print(self.A, 'a')
        print(At, 'at')
        print(minus_At_ob, 'atob')
        print(Al, 'al')
        print(B, 'B')
        print(D, 'D')


    def solve_DC(self, model='OTM'):
        if model == 'OTM':
            self.calc_all_nodes_OTM()
        elif model == 'HM10':
            self.calc_all_nodes_HM10()
        print(self.A)
        print(self.b)
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
