class Component():
    def __init__(self, nodes, args):
        self.nodes = nodes
        self.args = args

    def add(self, circuit): # must be overloaded in each component
        return 0

    def print(self):
        print(self.nodes)
        print(self.args)
