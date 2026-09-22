import unittest
import sys
import os

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.objects import Zone, Connection, Graph
from src.pathfinding import PathFinding


class TestPathfindingPriority(unittest.TestCase):
    def test_priority_zones_preferred(self):
        # Create zones
        zone_A = Zone(name="A", x=0, y=0, is_start=True)
        zone_B = Zone(name="B", x=1, y=0)
        zone_C = Zone(name="C", x=2, y=0)

        zone_P1 = Zone(name="P1", x=0, y=1, zone_type="priority")
        zone_P2 = Zone(name="P2", x=1, y=1, zone_type="priority")
        zone_P3 = Zone(name="P3", x=2, y=1, zone_type="priority")
        zone_P4 = Zone(name="P4", x=3, y=1, zone_type="priority")

        zone_D = Zone(name="D", x=3, y=0, is_end=True)

        zones = {
            "A": zone_A,
            "B": zone_B,
            "C": zone_C,
            "P1": zone_P1,
            "P2": zone_P2,
            "P3": zone_P3,
            "P4": zone_P4,
            "D": zone_D,
        }

        # Helper to connect
        def connect(z1, z2):
            conn = Connection(zone1=z1, zone2=z2, max_link_capacity=1)
            z1.adjacent_zones[z2.name] = conn
            z2.adjacent_zones[z1.name] = conn

        # Path 1: Normal zones (3 hops to D)
        # A -> B -> C -> D
        # Cost: 10 + 10 + 10 = 30
        connect(zone_A, zone_B)
        connect(zone_B, zone_C)
        connect(zone_C, zone_D)

        # Path 2: Priority zones (5 hops to D)
        # A -> P1 -> P2 -> P3 -> P4 -> D
        # Cost: 1 + 1 + 1 + 1 + 10 = 14
        connect(zone_A, zone_P1)
        connect(zone_P1, zone_P2)
        connect(zone_P2, zone_P3)
        connect(zone_P3, zone_P4)
        connect(zone_P4, zone_D)

        graph = Graph(zones=zones, connections=[], drones=[])

        #          coût=10           coût=10           coût=10
        #    +---------------> [B] --------------> [C] --------------+
        #    |               (normal)            (normal)            |
        #    |                                                       |
        #    |                                                       v
        # [A] (départ)                                            [D] (arrivée, normal)
        #    |                                                       ^
        #    |   coût=1      coût=1      coût=1      coût=1          | coût=10
        #    +-------> [P1] -------> [P2] -------> [P3] -------> [P4]+
        #           (priority)    (priority)    (priority)    (priority)

        pf = PathFinding(graph)

        path = pf.find_shortest_path()

        # BFS would prefer A->B->C->D (fewer hops)
        # Dijkstra with weights should prefer the priority path
        self.assertEqual(path, ["A", "P1", "P2", "P3", "P4", "D"])


if __name__ == "__main__":
    unittest.main()
