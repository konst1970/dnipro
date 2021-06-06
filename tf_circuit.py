from utility import create_array

import numpy
import tensorflow as tf

from component import Component

import networkx as nx
import matplotlib.pyplot as plt

class Circuit():
    def __init__(self):
        self.nodes = []
        self.components = []
        self.I = []
        self.A = []
        self.b = []
        self.x = []
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

    def calc_all_nodes_OTM(self, start=None, step=None, iter=None):
        nodes_len = len(self.nodes)
        components_len = len(self.components)
        self.size = 2*components_len + nodes_len - 1 
        self.I = create_array(nodes_len, components_len)
        self.A = create_array(self.size, self.size)
        self.b = create_array(self.size)
        self.x = create_array(self.size)

        for i, component in enumerate(self.components):
            component.add_OTM(self, start, step, iter)
            self.I[component.nodes[0]][i] = 1
            self.I[component.nodes[1]][i] = -1
    
    def calc_all_nodes_HM10(self):
        num = 0
        nodes_len = len(self.nodes)
        components_len = len(self.components)
        for component in self.components:
            if str(component).find('V') > -1 or str(component).find('L') > -1:
                num = num + 1
        
        self.size = nodes_len + num - 1
        self.A = create_array(self.size, self.size)
        self.b = create_array(self.size)
        self.x = create_array(self.size)

        for component in self.components:
            component.add_HM10(self)

    def solve_DC(self, model='OTM'):
        if model == 'OTM':
            self.calc_all_nodes_OTM()
        elif model == 'HM10':
            self.calc_all_nodes_HM10()
        self.A = tf.constant(self.A, dtype = tf.float32)
        self.b = tf.constant(self.b, shape = (self.size, 1), dtype = tf.float32)
        self.x = tf.linalg.solve(self.A, self.b)
        self.print_results(model)

        return {
            'type': 'ac',
            'result': self.x
        }
    
    def solve_AC(self, start, stop, step):
        result = []
        time_points = []
        
        self.calc_all_nodes_OTM(start, step, 0)
        self.x = numpy.linalg.solve(self.A, self.b)
        result.append(self.x)
        time_points.append(start)


        iter = int((stop - start) // step + 1) - 1

        for i in range(1, iter+1):
            b2 = self.b
            b1 = create_array(self.size)
            for component in self.components:
                component.refresh_OTM(self, b1, start, step, i+1)
            # print(b1, "b1")
            self.b = numpy.add(b2, b1)
            # print(self.b, 'b')
            self.x = numpy.linalg.solve(self.A, self.b)
            self.b = b2
            result.append(self.x)
            time_points.append(start + (i+1)*step)

        return {
            'type': 'ac',
            'start': start,
            'stop': stop,
            'time_points': time_points,
            'result': result
        }

    def draw_result(self, name, elem, analysis_result, param='V'):
        plt.suptitle = name

        time_points = analysis_result['time_points']

        elem_index = self.components.index(elem)
        elem_points = []
        if param == 'V':
            for el in analysis_result['result']:
                elem_points.append(el[len(self.nodes)+len(self.components)+elem_index-1][0])
            # elem_points.append(el[0][0])
        elif param == 'I':
            for el in analysis_result['result']:
                elem_points.append(el[len(self.nodes)+elem_index-1][0])

        print(elem_points, 'elem')
        plt.ylabel(f'{param}({str(elem)})')
        plt.xlabel('time')
        start = elem_points[0]
        stop = elem_points[1]

        # plt.axis([analysis_result['start'], analysis_result['stop'], start, stop])

        plt.plot(time_points, elem_points)
        plt.show()

        
    def print_components(self):
        lst = []
        for comp in self.components:
            lst.append(str(comp))
        print("elements -> ", lst)

    def print_results(self, model='OTM'):
        nodes = len(self.nodes)
        comps = len(self.components)
        for i in range(nodes - 1):
            print(f"\u03C6{i + 1} = {self.x[i]} Volt")        
        if model == 'OTM':
            for i, comp in enumerate(self.components):
                print(f"{str(comp)} = {comp.args} {comp.index}")
                print(f"I{i + 1} = {self.x[nodes + i - 1]} Ampere | "
                      f"V{i + 1} = {self.x[nodes + comps + i - 1]} Volt")
        

    def result_vector(self):
        return self.x
    
    # def print_matrix(self):
    #     line = ''
    #     # A = numpy.array2string(self.A).split('\n')
    #     for i in range(self.size):
    #         line = f"{A[i]}   {self.x[i:i+1][0]}   {self.b[i:i+1][0]}"
    #         if i == self.size//2:
    #             line = f"{A[i]} * {self.x[i:i+1][0]} = {self.b[i:i+1][0]}"
    #         print(line)
       
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
