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

def run_test_circuit_4(name):
    G1 = Conductor('G1', [1, 0], 0.5) # 0.5 1/Ohm
    R2 = Resistor('R2', [1, 2], 1) # 1 Ohm
    R3 = Resistor('R3', [2, 0], 1) # 1 Ohm
    I4 = CurrentSource('I4', [1, 0], 1) # 1 Ampere

    test_circuit = Circuit()
    test_circuit.add_components([G1, R2, R3, I4])

    test_circuit.solve_DC() # DC

    test_circuit.print()


if __name__ == '__main__':
    print("DNIPRO v.0.0.1 (c) 2021, all rights reserved")
    run_test_circuit_4("Test Circuit 4")
