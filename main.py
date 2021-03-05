
class Component():
    def __init__(self, nodes, args):
        self.nodes = nodes
        self.args = args

    def print(self):
        print(self.nodes)
        print(self.args)

class Resistor(Component):
    def __init__(self, i, j, resistance):
        self.nodes = [i,j]
        self.args = resistance

class VoltageSource(Component):
    def __init__(self, i, j, voltage):
        self.nodes = [i,j]
        self.args = voltage

class CurrentSource(Component):
    def __init__(self, i, j, current):
        self.nodes = [i,j]
        self.args = current

def print_circuit(name):
    R1 = Resistor(0, 1, 100) # 100 Ohm
    V1 = VoltageSource(1, 2, 1) # 1 Volt
    I1 = CurrentSource(0, 1, 1) # 1 Amper
    R1.print()
    V1.print()
    I1.print()


if __name__ == '__main__':
    print("DNIPRO v.0.0.1 (c) 2020, all rights reserved")
    print_circuit("Test Circuit")


