#
#             ####
#    ####### # V2 # #######
#    #        ####        #
#    #                    #
# ####                    #####
#    #                    #
#    #      ########      #  
#    #####  #  R1  # ######
#           ########
# 

from resistor import Resistor
from conductivity import Conductor
from voltage_source import VoltageSource
from circuit import Circuit

def run_test_circuit_2(name):
    R1 = Resistor('R1', [0, 1], 5) # 5 Ohm
    V2 = VoltageSource('V2', [0, 1], 1) # 1 Volt

    test_circuit = Circuit()
    test_circuit.add_components([R1, V2])

    test_circuit.solve_DC() # DC

    test_circuit.print_matrix()
    test_circuit.print_results()


if __name__ == '__main__':
    print("DNIPRO v.0.0.1 (c) 2021, all rights reserved")
    run_test_circuit_2("Test Circuit 2")