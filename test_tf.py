from resistor import Resistor
from current_source import CurrentSource
from circuit import Circuit


def run_test_circuit_4(name):
    R1 = Resistor('R1', [1, 2], 1) # 1 Ohm
    R2 = Resistor('R2', [2, 0], 1) # 1 Ohm
    I3 = CurrentSource('I3', [1, 0], 1) # 1 Ampere
    R4 = Resistor('R4', [3, 2], 1) # 1 Ohm
    R5 = Resistor('R5', [4, 1], 1) # 1 Ohm
    R6 = Resistor('R6', [4, 0], 1) # 1 Ohm
    R7 = Resistor('R7', [3, 1], 1) # 1 Ohm

    test_circuit = Circuit(gpu=True)
    test_circuit.add_components([R1, R2, I3, R4, R5, R6, R7])

    
    test_circuit.solve_DC() # DC
    test_circuit.print_results()


if __name__ == '__main__':
    print("DNIPRO v.0.0.1 (c) 2021, all rights reserved")
    run_test_circuit_4("Test Circuit 4")
