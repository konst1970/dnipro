# 
#                         ##########
#    ########## 1 ######  #   G3   # ######## 2
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
from circuit import Circuit


def run_test_circuit_4(name):
    G2 = Conductor('G2', [1, 0], 0.25) # 0.5 1/Ohm
    R1 = Resistor('R1', [1, 2], 1) # 2 Ohm
    R3 = Resistor('R3', [2, 0], 5) # 4 Ohm
    I4 = CurrentSource('I4', [0, 1], 2) # 0.5 Ampere

    test_circuit = Circuit()
    test_circuit.add_components([R1, G2, R3, I4])

    test_circuit.solve_DC() # DC

    test_circuit.print_matrix()
    test_circuit.print_results()


if __name__ == '__main__':
    print("DNIPRO v.0.0.1 (c) 2021, all rights reserved")
    run_test_circuit_4("Test Circuit 4")
