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
    R1 = Resistor(1, [1, 0], 4) # 2 Ohm
    R2 = Resistor(2, [1, 2], 1) # 1 Ohm
    R3 = Resistor(3, [2, 0], 1) # 1 Ohm
    V4 = VoltageSource(4, [1, 0], 1) # 1 Volt

    test_circuit = Circuit()
    test_circuit.add_components([R1, R2, R3, V4])

    test_circuit.solve_DC('HM10')

    test_circuit.print()