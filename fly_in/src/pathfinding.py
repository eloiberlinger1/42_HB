from collections import deque
from typing import List, Optional, Set
from .objects import Graph, Path


class PathFinding:

    def __init__(self, graph):
        self.graph = graph

    def find_shortest_path(
        self, excluded_zones: Set[str] | None = None
    ) -> Optional[List[str]]:
        """
        Finds the shortest path using BFS.
        Ignores 'blocked' zones and already discovered paths
        """
        if excluded_zones is None:
            excluded_zones = set()
        start_zone = next(z for z in self.graph.zones.values() if z.is_start)
        end_zone = next(z for z in self.graph.zones.values() if z.is_end)

        queue: deque[tuple[str, List[str]]] = deque(
            [(start_zone.name, [start_zone.name])]
        )
        visited = {start_zone.name}

        while queue:
            current_name, path = queue.popleft()

            if current_name == end_zone.name:
                return path

            current_zone = self.graph.zones[current_name]

            for neighbor_name in current_zone.adjacent_zones.keys():
                neighbor = self.graph.zones[neighbor_name]

                # Ignore blocked and excluded zones
                if neighbor.zone_type == "blocked":
                    continue
                if neighbor_name in excluded_zones and not (
                    neighbor.is_start or neighbor.is_end
                ):
                    continue

                if neighbor_name not in visited:
                    visited.add(neighbor_name)
                    queue.append((neighbor_name, path + [neighbor_name]))

        return None

    def calculate_path_cost(self, nodes: List[str]) -> int:
        """
        Calculate required ticks for one drone to cross the path.
        """
        cost = 0
        for zone_name in nodes[1:]:
            zone = self.graph.zones[zone_name]
            cost += 2 if zone.zone_type == "restricted" else 1
        return cost

    def calculate_paths(self) -> List[Path]:
        """
        According to the Graph, calculate all possible paths
        """
        discovered_paths: List[Path] = []
        zone_usage: dict[str, int] = {name: 0 for name in self.graph.zones}
        excluded_zones: set[str] = set()

        while True:
            nodes = self.find_shortest_path(excluded_zones=excluded_zones)
            if not nodes:
                break

            cost = self.calculate_path_cost(nodes)
            path_obj = Path(nodes=nodes, turn_cost=cost)
            discovered_paths.append(path_obj)

            for zone_name in nodes:
                zone = self.graph.zones[zone_name]
                if zone.is_start or zone.is_end:
                    continue
                zone_usage[zone_name] += 1
                if zone_usage[zone_name] >= zone.max_drones:
                    excluded_zones.add(zone_name)

        discovered_paths.sort(key=lambda p: p.turn_cost)

        return discovered_paths
