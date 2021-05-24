class Component:
    def __init__(self, _id: int, nodes: list, args: float, index: str):
        self.id = _id
        self.nodes = nodes
        self.args = args
        self.index = index

    def __str__(self):
        return f"{Component.__name__}{self.id}"

    def add(self, circuit): # must be overloaded in each component
        return 0

    def print(self):
        print(self.nodes)
        print(self.args)
