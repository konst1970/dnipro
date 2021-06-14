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
from current_source import CurrentSource
from circuit import Circuit


def run_test_circuit_sweep(name):
    G2 = Conductor('G2', [0, 1], 0.25) # 0.5 1/Ohm
    # R2 = Resistor('R2', [0, 1], 0.25) # 0.5 1/Ohm
    R1 = Resistor('R1', [1, 2], 1) # 2 Ohm
    R3 = Resistor('R3', [2, 0], 5) # 4 Ohm
    I4 = CurrentSource('I4', [0, 1], 2) # 0.5 Ampere

    test_circuit = Circuit()
    test_circuit.add_components([R1, G2, R3, I4])
    
    res = test_circuit.solve_DC_sweep(I4, 2, 8, 1) # DC
    print(res['result'])

    test_circuit.draw_VA_plot('VA', I4, res)

if __name__ == '__main__':
    print("DNIPRO v.0.0.1 (c) 2021, all rights reserved")
    run_test_circuit_sweep("Test Circuit sweep")
