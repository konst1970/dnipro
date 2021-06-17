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
from conductivity import Conductor
from voltage_source import VoltageSource
from circuit import Circuit

if __name__ == '__main__':
    R1 = Resistor('R1', [1, 0], 2) # 2 Ohm
    R2 = Resistor('R2', [1, 2], 1) # 1 Ohm
    R3 = Resistor('R3', [2, 0], 1) # 1 Ohm
    V4 = VoltageSource('V4', [1, 0], 1) # 1 Volt

    test_circuit = Circuit()
    test_circuit.add_components([R1, R2, R3, V4])

    test_circuit.solve_DC('HM10')

    test_circuit.print_matrix()
    test_circuit.print_results('HM10')
    # test_circuit.print()