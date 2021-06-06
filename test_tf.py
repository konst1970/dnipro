from resistor import Resistor
from current_source import CurrentSource
from circuit import Circuit


def run_test_circuit_4(name):
    R2 = Resistor('R2', [1, 2], 1) # 1 Ohm
    R3 = Resistor('R3', [2, 0], 1) # 1 Ohm
    I4 = CurrentSource('I4', [1, 0], 1) # 1 Ampere
    R5 = Resistor('R5', [3, 2], 1) # 1 Ohm
    R6 = Resistor('R6', [4, 1], 1) # 1 Ohm
    R7 = Resistor('R7', [4, 0], 1) # 1 Ohm
    R8 = Resistor('R8', [3, 1], 1) # 1 Ohm

    test_circuit = Circuit(gpu=True)
    test_circuit.add_components([R2, R3, I4, R5, R6, R7, R8])

    
    test_circuit.solve_DC() # DC


if __name__ == '__main__':
    print("DNIPRO v.0.0.1 (c) 2021, all rights reserved")
    run_test_circuit_4("Test Circuit 4")
