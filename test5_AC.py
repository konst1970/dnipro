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
    I2 = CurrentSource('I1', [0, 1], 2, (2, 0.23, 0.1)) # 2 Ampere
    R1 = Resistor('R2', [1, 0], 10) # 1 Ohm
    C3 = Capacitor('C3', [1, 0], 1e-6, 0 ) # 1e-6 F # U_start = 0 argument

    test_circuit = Circuit()
    test_circuit.add_components([R1, I2, C3])

    # test_circuit.solve_DC() # DC
    res = test_circuit.solve_AC(0, 1e-4, 0.5e-7) # AC
    # print(res['result'])

    test_circuit.print_results()
    test_circuit.print_matrix()
    
    test_circuit.draw_plot(name, I2, res, 'I')
    test_circuit.draw_plot(name, R1, res, 'V')
    test_circuit.draw_plot(name, C3, res, 'I')

if __name__ == '__main__':
    print("DNIPRO v.0.0.1 (c) 2021, all rights reserved")
    run_test_circuit_5("Test Circuit 5")