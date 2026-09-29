from typing import Dict, List, Optional, Tuple
from collections import defaultdict

from .objects import Graph, Zone, Drone


class ReservationTable:
    def __init__(self, graph):
        self.map_data = graph
        self.zone_usage = {}
        self.connection_usage = {}

    def is_zone_available(self):
        return False

    def is_connection_available(self):
        return False

    def reserve_path(self):
        pass


class Pathfinding:

    def __init__(self, graph):
        self.graph = graph
        self.res_table = ReservationTable(graph)

    def resolve_graph(self):
        pass
