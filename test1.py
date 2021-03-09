#
#             ####
#    ####### # I1 # ######
#    #        ####       #
#    #                   #
# ####                   #####
#    #                   #
#    #      #######      #  
#    #####  #     # ######
#           #######
# 

from resistor import Resistor
from conductivity import Conductor
from current_source import CurrentSource
from voltage_source import VoltageSource
from circuit import Circuit

def run_test_circuit_1(name):
    R1 = Resistor(1, 0, 1, 2) # 2 Ohm
    I1 = CurrentSource(1, 0, 1, 1) # 1 Ampere

    test_circuit = Circuit()
    test_circuit.add_components([R1, I1])

    test_circuit.solve_DC() # DC

    test_circuit.print()


if __name__ == '__main__':
    print("DNIPRO v.0.0.1 (c) 2021, all rights reserved")
    run_test_circuit_1("Test Circuit 1")
