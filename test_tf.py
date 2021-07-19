from random import randint

from resistor import Resistor
from current_source import CurrentSource
from circuit import Circuit


def create_circuit(m: int, n: int, source_value: int, resistor_value: int): # m - row, n -col
    node_list = [CurrentSource('I1', [0, 1], source_value)]

    for row in range(0, m-1, 1):
        for col in range(1, n, 1):
            a = col + row*n
            b = col + row*n + 1
            c = col + n*(row+1)
            # print(i, ' - ', i + 1)
            # print(i, ' - ', col + n*(row+1))
            node_list.append(Resistor(f'R{col + (row*n)+(row*m)+1}', [a, b], randint(1, resistor_value)))
            node_list.append(Resistor(f'R{col + (row+1)*m+(row*n)}', [a, c], randint(1, resistor_value)))
        
        # print(i+1, ' - ', col + n*(row+1)+1)
        node_list.append(Resistor(f'R{(row+1)*m+(row+1)*n+1}', [n + row*n, n + (row+1)*n], randint(1, resistor_value)))
    
    for col in range(0, n-1, 1):
        # print(m*(n-1) + col, ' - ', m*(n-1) + col + 1)
        node_list.append(Resistor(f'R{(m-1)*(2*n-1)+col+1+1}', [m*(n-1) + col,  m*(n-1) + col + 1],
                                  randint(1, resistor_value)))

    node_list.append(Resistor(f'R{(m-1)*n + (n-1)*m + 2}', [0, n+1], randint(1, resistor_value)))
    
    return node_list


def run_test_circuit_4(name):
    R1 = Resistor('R1', [1, 2], 1) # 1 Ohm
    R2 = Resistor('R2', [2, 0], 1) # 1 Ohm
    I3 = CurrentSource('I3', [1, 0], 1) # 1 Ampere
    R4 = Resistor('R4', [3, 2], 1) # 1 Ohm
    R5 = Resistor('R5', [4, 1], 1) # 1 Ohm
    R6 = Resistor('R6', [4, 0], 1) # 1 Ohm
    R7 = Resistor('R7', [3, 1], 1) # 1 Ohm

    test_circuit = Circuit(gpu=True)
    a = [R1, R2, I3, R4, R5, R6, R7]
    test_circuit.add_components(a)

    test_circuit.solve_DC() # DC
    test_circuit.print_results()


if __name__ == '__main__':
    print("DNIPRO v.0.0.1 (c) 2021, all rights reserved")
    node_l = create_circuit(49, 50, 1, 10)

    # circuit = Circuit(gpu=True)
    # circuit.add_components(node_l)

    # res = circuit.solve_DC() # DC
    # res_time = res['res_time']
    # print('GPU:', res_time)

    circuit = Circuit(gpu=False)
    circuit.add_components(node_l)

    res = circuit.solve_DC() # DC
    res_time = res['res_time']
    print('CPU:', res_time)
    print('CPU:', len(res['result']))
