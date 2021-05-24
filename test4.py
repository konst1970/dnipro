# 
#                         ##########
#    ########## 1 ######  #   G1   # ######## 2
#    #          #         ##########          #
#    #          #                             #
#   ####      ######                        ######
#  # I1 #     #    #                        #    #
#   ####      # R1 #                        # R2 #
#    #        #    #                        #    #
#    #        ######                        ######
#    #          #                             #
#    #          #                             #
#    ########## 0 #############################
# 

from resistor import Resistor
from conductivity import Conductor
from current_source import CurrentSource
from voltage_source import VoltageSource
from circuit import Circuit

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def run_test_circuit_4(name):
    G1 = Conductor('G1', [1, 0], 0.5) # 0.5 1/Ohm
    R2 = Resistor('R2', [1, 2], 1) # 1 Ohm
    R3 = Resistor('R3', [2, 0], 1) # 1 Ohm
    I4 = CurrentSource('I4', [1, 0], 1) # 1 Ampere

    test_circuit = Circuit()
    test_circuit.add_components([G1, R2, R3, I4])

    test_circuit.solve_DC() # DC

    # test_circuit.print_components()
    # nodes = len(test_circuit.nodes)
    # comps = len(test_circuit.components)
    # print(nodes, "nodes")
    # print(comps, "comps")
    # im = test_circuit.A[:comps, :nodes-1]
    # print(im, "im")
    # am = (np.dot(im, im.T) > 0).astype(int)
    # print(am, "am")
    # graph = nx.from_numpy_matrix(am)
    # nx.draw_circular(graph,
    #      node_color='red',
    #      node_size=1000,
    #      with_labels=True,
    #      connectionstyle='arc2, rad = 0.5')
    # plt.show()

    test_circuit.print_matrix()
    # test_circuit.print_results()


if __name__ == '__main__':
    print("DNIPRO v.0.0.1 (c) 2021, all rights reserved")
    run_test_circuit_4("Test Circuit 4")
