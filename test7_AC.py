#      
#                   ####
#    ############# # I1 # #######
#    #              ####        #
#    #                          #
#    #     ##########     # #   #
#    ##### #   R2   # ### # # ### 
#    #     ##########     # #   #
#    #                     C4   #  
#    #     /\   /\              #
#    #    / \  / \              #
#    ### /   \/   \ #############
#             L3
#


from resistor import Resistor
from inductor import Inductor
from capacitor import Capacitor
from current_source import CurrentSource
from circuit import Circuit

def run_test_circuit_7(name):
    I1 = CurrentSource('I1', [2, 0], 2, (2, 0.2, 0.1)) # 2 Ampere
    R2 = Resistor('R2', [1, 0], 1) # 1 Ohm
    L3 = Inductor('L3', [2, 0], 0.01, ) # 0.01 H # I_start = 0.
    C4 = Capacitor('C4', [1, 2], 0.00001) # 0.00001 F #U_start = 0.

    test_circuit = Circuit()
    test_circuit.add_components([I1, R2, L3, C4])


    res = test_circuit.solve_AC(0, 0.001, 0.000002)
    
    test_circuit.print_results()
    test_circuit.draw_plot(name, I1, res, 'I')
    test_circuit.draw_plot(name, R2, res, 'V')
    test_circuit.draw_plot(name, L3, res, 'V')
    test_circuit.draw_plot(name, C4, res, 'I')


if __name__ == '__main__':
    print("DNIPRO v.0.0.1 (c) 2021, all rights reserved")
    run_test_circuit_7("Test Circuit 7")