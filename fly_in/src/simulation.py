from collections import deque
from typing import List, Optional, Set

from .objects import Graph, Path


class SimulationEngine:

    def __init__(self, graph: Graph) -> None:

        self.graph = graph

    def _find_shortest_path(
        self, excluded_zones: Set[str] = None
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

    def _calculate_path_cost(self, nodes: List[str]) -> int:
        """
        Calculate required ticks for one drone to cross the path.
        """
        cost = 0
        for zone_name in nodes[1:]:
            zone = self.graph.zones[zone_name]
            cost += 2 if zone.zone_type == "restricted" else 1
        return cost

    def _calculate_paths(self) -> List[Path]:
        """
        According to the Graph, calculate all possible paths
        """
        discovered_paths: List[Path] = []
        zone_usage: dict[str, int] = {name: 0 for name in self.graph.zones}
        excluded_zones: set[str] = set()

        while True:
            nodes = self._find_shortest_path(excluded_zones=excluded_zones)
            if not nodes:
                break

            cost = self._calculate_path_cost(nodes)
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

    def _dispatch_drones(self, paths: List[Path]) -> None:
        """
        Assign drones to the best path
        """

        path_counts = []
        for i in range(len(paths)):
            path_counts.append(0)

        for drone in self.graph.drones:
            best_index = min(
                range(len(paths)), key=lambda i: paths[i].turn_cost + path_counts[i]
            )
            drone.path = paths[best_index].nodes
            drone.path_index = 0
            path_counts[best_index] += 1

    def _get_zone_occupancy(self) -> dict[str, int]:
        """Count how many drones actually occupy the zone"""
        occupancy: dict[str, int] = {name: 0 for name in self.graph.zones}
        for d in self.graph.drones:
            if d.state not in ["ARRIVED", "IN_TRANSIT"] and d.current_position:
                occupancy[d.current_position] += 1
        return occupancy

    def step(self) -> List[str]:
        """
        Run one tick of the simulation
        Returns the list of movements
        """
        moves_result: List[str] = []
        occupancy = self._get_zone_occupancy()

        link_traffic: dict[tuple[str, str], int] = {}

        for drone in self.graph.drones:
            if drone.state == "IN_TRANSIT":
                drone.turns_remaining -= 1
                if drone.turns_remaining == 0:
                    target_zone_name = drone.path[drone.path_index]
                    drone.current_position = target_zone_name
                    drone.state = "WAITING"
                    occupancy[target_zone_name] += 1
                    moves_result.append(f"{drone.drone_id}-{target_zone_name}")

        active_drones = [
            d
            for d in self.graph.drones
            if d.state != "ARRIVED" and d.state != "IN_TRANSIT"
        ]

        # Sort waiting drones from the most advanced to the less advanced
        active_drones.sort(key=lambda d: d.path_index, reverse=True)

        for drone in active_drones:
            if drone.path_index + 1 >= len(drone.path):
                continue

            current_zone_name = drone.path[drone.path_index]
            target_zone_name = drone.path[drone.path_index + 1]
            target_zone = self.graph.zones[target_zone_name]

            # sort the zones to avoid collision if another goes in opposite direction
            link_key = tuple(sorted([current_zone_name, target_zone_name]))
            conn = self.graph.zones[current_zone_name].adjacent_zones[target_zone_name]
            current_link_usage = link_traffic.get(link_key, 0)

            if current_link_usage >= conn.max_link_capacity:
                continue

            is_target_end = target_zone.is_end
            if (
                not is_target_end
                and occupancy[target_zone_name] >= target_zone.max_drones
            ):
                # zone is full
                continue

            link_traffic[link_key] = current_link_usage + 1

            if not self.graph.zones[current_zone_name].is_start:
                occupancy[current_zone_name] -= 1

            drone.path_index += 1

            if target_zone.zone_type == "restricted":
                drone.state = "IN_TRANSIT"
                drone.turns_remaining = 1
                conn_name = f"{current_zone_name}-{target_zone_name}"
                moves_result.append(f"{drone.drone_id}-{conn_name}")

            else:
                drone.current_position = target_zone_name
                if is_target_end:
                    drone.state = "ARRIVED"
                else:
                    occupancy[target_zone_name] += 1
                moves_result.append(f"{drone.drone_id}-{target_zone_name}")

        return moves_result

    def run(self) -> None:
        """
        Run the simulation.
        -> Will call step() unltil all drones are not in state ARRIVED.
        """
        print(f"Starting simulation for {self.graph.nb_drones} drones")

        paths = self._calculate_paths()
        if not paths:
            print("No valid path found.")
            return
        self._dispatch_drones(paths)
        turn_count = 0
        while any(d.state != "ARRIVED" for d in self.graph.drones):
            turn_count += 1
            moves = self.step()
            if moves:
                print(" ".join(moves))

        print(f"\nFinished simulation in {turn_count} turns.")
