import heapq
from typing import List, Optional, Set
from .objects import Path, Dict


class PathFinding:

    def __init__(self, graph):
        self.graph = graph
        self.start_zone = next(
            (z for z in self.graph.zones.values() if z.is_start), None
        )
        self.end_zone = next((z for z in self.graph.zones.values() if z.is_end), None)

    def _get_zone_traversal_cost(self, zone):
        if zone.zone_type == "priority":
            return 1
        return 10

    def find_shortest_path(
        self,
        excluded_zones: Set[str] | None = None,
        zone_penalties: Dict[str, float] | None = None
    ) -> Optional[List[str]]:
        """
        Finds the shortest path using Djikstra.
        Ignores 'blocked' zones and already discovered paths
        """
        excluded = excluded_zones or set()

        start_zone = self.start_zone
        end_zone = self.end_zone

        if not start_zone or not end_zone:
            return None
        if start_zone.zone_type == "blocked" or end_zone.zone_type == "blocked":
            return None
        if start_zone.name == end_zone.name:
            return [start_zone.name]

        queue: List[tuple[float, str]] = [(0.0, start_zone.name)]
        distances: Dict[str, float] = {start_zone.name: 0.0}
        came_from: Dict[str, Optional[str]] = {start_zone.name: None}

        # Djikstra implementation
        while queue:
            current_cost, current_name = heapq.heappop(queue)

            if current_name == end_zone.name:
                return self._reconstruct_path(came_from, end_zone.name)

            if current_cost > distances[current_name]:
                continue

            current_zone = self.graph.zones[current_name]

            for neighbor_name in current_zone.adjacent_zones.keys():
                neighbor = self.graph.zones[neighbor_name]

                # Ignore blocked and excluded zones
                if neighbor.zone_type == "blocked":
                    continue
                if neighbor_name in excluded:
                    continue

                step_cost = self._get_zone_traversal_cost(neighbor)
                if zone_penalties:
                    step_cost += zone_penalties.get(neighbor_name, 0.0)
                new_cost = current_cost + step_cost

                if new_cost < distances.get(neighbor_name, float("inf")):
                    distances[neighbor_name] = new_cost
                    came_from[neighbor_name] = current_name
                    heapq.heappush(queue, (new_cost, neighbor_name))

        return None

    def _reconstruct_path(
        self, came_from: Dict[str, Optional[str]], end_name: str
    ) -> List[str]:
        path = []
        curr: Optional[str] = end_name
        while curr is not None:
            path.append(curr)
            curr = came_from[curr]
        path.reverse()
        return path

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
        zone_penalties: dict[str, float] = {}
        seen_paths: set[tuple[str, ...]] = set()

        # Limit number of paths to avoid infinite loops when not excluding zones
        max_paths = max(10, len(self.graph.drones) * 2)
        for _ in range(max_paths):
            nodes = self.find_shortest_path(
                excluded_zones=excluded_zones,
                zone_penalties=zone_penalties
            )
            if not nodes:
                break

            path_tuple = tuple(nodes)
            if path_tuple not in seen_paths:
                seen_paths.add(path_tuple)
                cost = self.calculate_path_cost(nodes)
                path_obj = Path(nodes=nodes, turn_cost=cost)
                discovered_paths.append(path_obj)

            for zone_name in nodes:
                zone = self.graph.zones[zone_name]
                if zone.is_start or zone.is_end:
                    continue
                zone_usage[zone_name] += 1
                zone_penalties[zone_name] = zone_penalties.get(zone_name, 0.0) + 1.0
                if zone_usage[zone_name] >= zone.max_drones:
                    pass # We only rely on zone_penalties to encourage path diversity

        discovered_paths.sort(key=lambda p: p.turn_cost)

        return discovered_paths
