from resistor import Resistor
from inductor import Inductor
from voltage_source import VoltageSource
from circuit import Circuit

def run_test_circuit_6(name):
    I1 = VoltageSource('I1', [1, 0], 2, (2, 0.1, 0.1)) # 2 Ampere
    R2 = Resistor('R2', [1, 0], 1) # 1 Ohm
    L3 = Inductor('L3', [1, 0], 0.01, 1) # 1 H # I_start = 0.1

    test_circuit = Circuit(gpu=True)
    test_circuit.add_components([I1, R2, L3])


    res = test_circuit.solve_AC(0, 1, 0.1)
    test_circuit.print_results()
    test_circuit.draw_result(name, L3, res, 'V')


if __name__ == '__main__':
    print("DNIPRO v.0.0.1 (c) 2021, all rights reserved")
    run_test_circuit_6("Test Circuit 6")