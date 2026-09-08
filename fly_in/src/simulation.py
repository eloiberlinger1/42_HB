from .objects import Graph


class SimulationEngine:

    def __init__(self, graph: Graph):

        for key, value in graph.zones.items():
            # print(f"{key} = {value}")
            pass
            # print()

    def run(self) -> None:
        t = 0

        # while (all drones not at end zone)
        while t != 10:
            t += 1
            print(f"Round : {t}")
            print("Something happens")
            print()
