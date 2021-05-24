import numpy
from component import Component

import networkx as nx
import matplotlib.pyplot as plt

class Circuit():
    def __init__(self):
        self.nodes = []
        self.components = []
        self.I = numpy.zeros(shape=(1,1))
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

    def calc_all_nodes_OTM(self, step=None):
        self.size = len(self.nodes)-1 + 2*len(self.components)
        self.I = numpy.zeros(shape=(len(self.nodes), len(self.components)))
        self.A = numpy.zeros(shape=(self.size,self.size))
        self.b = numpy.zeros(shape=(self.size,1))
        self.x = numpy.zeros(shape=(self.size,1))

        for i, component in enumerate(self.components):
            print(str(component))
            component.add_OTM(circuit=self, step=step)
            self.I[component.nodes[0], i] = 1
            self.I[component.nodes[1], i] = -1
    
    def calc_all_nodes_HM10(self):
        num = 0
        for component in self.components:
            if str(component).find('V') > -1 or str(component).find('L') > -1:
                num = num + 1
        
        self.size = len(self.nodes) + num - 1
        self.A = numpy.zeros(shape=(self.size, self.size))
        self.b = numpy.zeros(shape=(self.size, 1))
        self.x = numpy.zeros(shape=(self.size, 1))

        for component in self.components:
            component.add_HM10(self)

    def solve_DC(self, model='OTM'):
        if model == 'OTM':
            self.calc_all_nodes_OTM()
        elif model == 'HM10':
            self.calc_all_nodes_HM10()
        self.x = numpy.linalg.solve(self.A, self.b)
        self.print_results(model)
    
    def solve_AC(self, time, step):
        result = []
        
        self.calc_all_nodes_OTM(step)
        self.x = numpy.linalg.solve(self.A, self.b)
        result.append(self.x)

        iter = int(time // step + 1) - 1

        for i in range(iter):
            b1 = numpy.zeros(shape=(self.size, 1))
            for component in self.components:
                component.refresh_OTM(self, b1, step,)
            
            self.b = numpy.add(self.b, b1)
            self.x = numpy.linalg.solve(self.A, self.b)
            result.append(self.x)
        
        print(result)

    def print_components(self):
        lst = []
        for comp in self.components:
            lst.append(str(comp))
        print("elements -> ", lst)

    def print_results(self, model='OTM'):
        nodes = len(self.nodes)
        comps = len(self.components)
        for i in range(nodes - 1):
            print(f"\u03C6{i + 1} = {self.x[i][0]} Volt")        
        if model == 'OTM':
            for i, comp in enumerate(self.components):
                print(f"{str(comp)} = {comp.args} {comp.index}")
                print(f"I{i + 1} = {self.x[nodes + i - 1][0]} Ampere | "
                      f"V{i + 1} = {self.x[nodes + comps + i - 1][0]} Volt")
        

    def result_vector(self):
        return self.x
    
    def print_matrix(self):
        line = ''
        A = numpy.array2string(self.A).split('\n')
        for i in range(self.size):
            line = f"{A[i]}   {self.x[i:i+1][0]}   {self.b[i:i+1][0]}"
            if i == self.size//2:
                line = f"{A[i]} * {self.x[i:i+1][0]} = {self.b[i:i+1][0]}"
            print(line)
       
    def print_graph(self):
        edges = []
        G=nx.MultiGraph()
        G.add_nodes_from(self.nodes)
        for i, arr in enumerate(self.I.T):
            a = list(arr).index(-1)
            b = list(arr).index(1)
            edges.append((a, b))
        G.add_edges_from(edges)
        pos = nx.spring_layout(G)
        nx.draw_networkx(G, pos, with_labels=True, node_color = 'r', node_size = 300, alpha = 1)
        ax = plt.gca()
        for e in G.edges:
            # print(e)
            ax.annotate("",
                        xy=pos[e[0]], xycoords='data',
                        xytext=pos[e[1]], textcoords='data',
                        arrowprops=dict(arrowstyle="-", color="0.5",
                                        shrinkA=10, shrinkB=10,
                                        patchA=None, patchB=None,
                                        connectionstyle="arc3,rad=rrr".replace('rrr',str(0.3*e[2])
                                        ),
                                        ),
                        )
        labels = {edge: str(self.components[i]) for i, edge in enumerate(edges)}
        # print(labels)
        # print(edges)
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels,font_color='red', label_pos=0.3, verticalalignment='bottom')

        plt.axis('off')
            
        plt.show()
