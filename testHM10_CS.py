# 
#                         ##########
#    ########## 1 ######  #   R1   # ######## 2
#    #          #         ##########          #
#    #          #                             #
#   ####      ######                        ######
#  # I4 #     #    #                        #    #
#   ####      # R2 #                        # R3 #
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

if __name__ == '__main__':
    R1 = Resistor('R1', [1, 0], 2) # 2 Ohm
    R2 = Resistor('R2', [1, 2], 1) # 1 Ohm
    R3 = Resistor('R3', [2, 0], 1) # 1 Ohm
    I4 = CurrentSource('I4', [1, 0], 1) # 1 Ampere

    test_circuit = Circuit()
    test_circuit.add_components([R1, R2, R3, I4])

    test_circuit.solve_DC('HM10')

    test_circuit.print_matrix()
    test_circuit.print_results('HM10')
    # test_circuit.print()