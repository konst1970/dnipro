#
#             ####
#    ####### # I2 # ######
#    #        ####       #
#    #                   #
# ####                   #####
#    #                   #
#    #      #######      #  
#    #####  #  R1 # ######
#           #######
# 

from resistor import Resistor
from conductivity import Conductor
from current_source import CurrentSource
from voltage_source import VoltageSource
from circuit import Circuit


def run_test_circuit_1(name):
    R1 = Resistor('R1', [0, 1], 2) # 2 Ohm
    I2 = CurrentSource('I2', [0, 1], 1) # 1 Ampere

    test_circuit = Circuit()
    test_circuit.add_components([R1, I2])

    test_circuit.solve_DC() # DC

    # size = len(test_circuit.nodes)
    # print(size, "size")
    # im = test_circuit.A[0:size, 0:size]
    # print(im, "im")
    # am = (np.dot(im, im.T) > 0).astype(int)
    # np.fill_diagonal(am, 0)
    # print(am, "am")
    # graph = nx.from_numpy_matrix(am)
    # print(graph)
    # nx.draw_circular(graph,
    #      node_color='red',
    #      node_size=1000,
    #      with_labels=True,
    #      connectionstyle='arc3, rad = 0.5')
    # plt.show()

    test_circuit.print_matrix()
    test_circuit.print_results()
    test_circuit.print_graph()


if __name__ == '__main__':
    print("DNIPRO v.0.0.1 (c) 2021, all rights reserved")
    run_test_circuit_1("Test Circuit 1")
