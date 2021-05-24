from resistor import Resistor
from conductivity import Conductor
from capacitor import Capacitor
from inductor import Inductor
from current_source import CurrentSource
from voltage_source import VoltageSource
from circuit import Circuit

def run_test_circuit_6(name):
    I1 = CurrentSource('I1', [1, 0], 2) # 2 Ampere
    R2 = Resistor('R2', [1, 0], 1) # 1 Ohm
    # R3 = Resistor('R3', [1, 0], 2) # 1 Ohm
    L3 = Inductor('L3', [1, 0], 0.01, 1) # 1 H # I_start = 0.1

    test_circuit = Circuit()
    test_circuit.add_components([I1, R2, L3])

    # test_circuit.solve_DC() # DC
    # test_circuit.solve_DC()
    test_circuit.solve_AC(1, 0.1)


if __name__ == '__main__':
    print("DNIPRO v.0.0.1 (c) 2021, all rights reserved")
    run_test_circuit_6("Test Circuit 6")