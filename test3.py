# 
#                         ##########
#    ########## 1 ######  #   R1   # ######## 2
#    #          #         ##########          #
#    #          #                             #
#   ####      ######                        ######
#  # V4 #     #    #                        #    #
#   ####      # R2 #                        # R3 #
#    #        #    #                        #    #
#    #        ######                        ######
#    #          #                             #
#    #          #                             #
#    ########## 0 #############################
# 

from resistor import Resistor
from current_source import CurrentSource
from voltage_source import VoltageSource
from circuit import Circuit



def run_test_circuit_3(name):
    R1 = Resistor('R1', [1, 0], 2) # 2 Ohm
    R2 = Resistor('R2', [1, 2], 1) # 1 Ohm
    R3 = Resistor('R3', [2, 0], 1) # 1 Ohm
    V4 = VoltageSource('V4', [1, 0], 1) # 1 Volt

    test_circuit = Circuit()
    test_circuit.add_components([R1, R2, R3, V4])
    

    test_circuit.solve_DC() # DC

    test_circuit.print_matrix()
    test_circuit.print_results()
    test_circuit.print_graph()

if __name__ == '__main__':
    print("DNIPRO v.0.0.1 (c) 2021, all rights reserved")
    run_test_circuit_3("Test Circuit 3")
