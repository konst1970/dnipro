from component import Component

class VoltageSource(Component):
    def __init__(self, i, j, voltage):
        self.nodes = [i,j]
        self.args = voltage