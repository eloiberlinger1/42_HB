from .objects import Graph


class Simulation:
    def __init__(self, graph: Graph):
        self.graph = graph
        print(self.graph)

    def run(self):
        print("")
