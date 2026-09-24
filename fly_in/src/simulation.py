import sys
from collections import deque
from typing import List, Optional, Set

from .colors import get_color, RESET
from .objects import Graph, Path
from .pathfinding import PathFinding


class SimulationEngine:

    def __init__(self, graph: Graph) -> None:

        self.graph = graph
        self.pathfinding = PathFinding(graph)

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
            if d.state == "ARRIVED":
                continue
            if d.state == "WAITING_RESTRICTED" and d.turns_remaining > 0:
                continue
            if d.current_position:
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
            if drone.state == "WAITING_RESTRICTED":
                if drone.turns_remaining > 0:
                    u = drone.path[drone.path_index - 1]
                    v = drone.path[drone.path_index]
                    link_key = (u, v) if u <= v else (v, u)
                    link_traffic[link_key] = link_traffic.get(link_key, 0) + 1

        for drone in self.graph.drones:
            if drone.state == "WAITING_RESTRICTED":
                if drone.turns_remaining == 0:
                    drone.state = "WAITING"
                else:
                    drone.turns_remaining -= 1

        active_drones = [
            d
            for d in self.graph.drones
            if d.state not in ("ARRIVED", "WAITING_RESTRICTED")
        ]

        # Sort waiting drones from the most advanced to the less advanced
        active_drones.sort(key=lambda d: d.path_index, reverse=True)

        for drone in active_drones:
            if drone.path_index + 1 >= len(drone.path):
                continue

            current_zone_name = drone.path[drone.path_index]
            target_zone_name = drone.path[drone.path_index + 1]
            target_zone = self.graph.zones[target_zone_name]

            # sort the zones to avoid collision
            # link_key = tuple(sorted([current_zone_name, target_zone_name]))
            link_key = (
                (current_zone_name, target_zone_name)
                if current_zone_name <= target_zone_name
                else (target_zone_name, current_zone_name)
            )
            zone = self.graph.zones[current_zone_name]
            conn = zone.adjacent_zones[target_zone_name]
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
                drone.state = "WAITING_RESTRICTED"
                drone.turns_remaining = 1
                drone.current_position = target_zone_name
                if is_target_end:
                    drone.state = "ARRIVED"

                color = get_color(target_zone.color)
                move_str = f"{drone.drone_id}-{target_zone_name}"
                if color:
                    moves_result.append(f"{color}{move_str}{RESET}")
                else:
                    moves_result.append(f"{move_str}")

            else:
                drone.current_position = target_zone_name
                if is_target_end:
                    drone.state = "ARRIVED"
                else:
                    occupancy[target_zone_name] += 1

                color = get_color(target_zone.color)
                move_str = f"{drone.drone_id}-{target_zone_name}"
                if color:
                    moves_result.append(f"{color}{move_str}{RESET}")
                else:
                    moves_result.append(f"{move_str}")

        return moves_result

    def run(self) -> None:
        """
        Run the simulation.
        -> Will call step() unltil all drones are not in state ARRIVED.
        """
        print(f"Starting simulation for {self.graph.nb_drones} drones")

        paths = self.pathfinding.calculate_paths()
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
