from resistor import Resistor
from conductivity import Conductor
from capacitor import Capacitor
from current_source import CurrentSource
from voltage_source import VoltageSource
from circuit import Circuit

import math

def run_test_circuit_5(name):
    I1 = VoltageSource('I1', [1, 0], math.sin(2)) # 2 Ampere
    R2 = Resistor('R2', [1, 0], 1) # 1 Ohm
    C3 = Capacitor('C3', [1, 0], 0.01, 1) # 1 F # U_start = 0.1 argument

    test_circuit = Circuit()
    test_circuit.add_components([I1, R2, C3])

    # test_circuit.solve_DC() # DC
    test_circuit.solve_AC(1, 0.1)


if __name__ == '__main__':
    print("DNIPRO v.0.0.1 (c) 2021, all rights reserved")
    run_test_circuit_5("Test Circuit 5")