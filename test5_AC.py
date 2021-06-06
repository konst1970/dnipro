#      
#            ####
#    ###### # I1 # #######
#    #       ####        #
#    #                   #
#    #     ##########    #
#    ##### #   R2   # #### 
#    #     ##########    #
#    #                   #
#    #       #  #        #
#    ####### #  # ########
#            #  #
#             C3
#

from resistor import Resistor
from conductivity import Conductor
from capacitor import Capacitor
from current_source import CurrentSource
from circuit import Circuit


def run_test_circuit_5(name):
    I1 = CurrentSource('I1', [0, 1], 2, (1, 0.5)) # 2 Ampere
    R2 = Resistor('R2', [1, 0], 10) # 1 Ohm
    C3 = Capacitor('C3', [1, 0], 0.1, 0.) # 1 F # U_start = 0.1 argument

    test_circuit = Circuit(gpu=True)
    test_circuit.add_components([I1, R2, C3])

    # test_circuit.solve_DC() # DC
    res = test_circuit.solve_AC(0, 2, 0.1)
    print(res['result'])

    test_circuit.print_results()
    test_circuit.draw_result(name, I1, res, 'V')
    test_circuit.draw_result(name, C3, res, 'V')

if __name__ == '__main__':
    print("DNIPRO v.0.0.1 (c) 2021, all rights reserved")
    run_test_circuit_5("Test Circuit 5")