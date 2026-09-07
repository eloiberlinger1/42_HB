import argparse
from pathlib import Path

from .parsing import MapParser, CLIParser
from .objects import Drone, Graph, Connection, Zone

from typing import Dict


class Application:

    def __init__(self) -> None:

        self.path: Path = Path("maps/easy/01_linear_path.txt")

    def _build_graph(self, raw_data):

        nb_drones = raw_data.get("nb_drones", 0)
        raw_zones = raw_data.get("zones", {})
        raw_connections = raw_data.get("connections", [])

        zones_dict: Dict[str, Zone] = {}
        start_zone_name = None

        # 1. Instanciation des zones
        for name, metadata in raw_zones.items():
            is_start = metadata.get("type_def") == "start_hub"
            if is_start:
                start_zone_name = name

            zone = Zone(
                name=name,
                x=metadata.get("x"),
                y=metadata.get("y"),
                zone_type=metadata.get("zone_type", "normal"),
                max_drones=metadata.get("max_drones", 1),
                color=metadata.get("color"),
                is_start=is_start,
                is_end=metadata.get("is_end", False),
            )
            zones_dict[name] = zone

        if not start_zone_name and nb_drones > 0:
            raise ValueError("start_hub not found in the input file")

        # 2. Instanciation des connexions
        connections_list = []
        for conn_data in raw_connections:
            z1_name = conn_data.get("from")
            z2_name = conn_data.get("to")

            if z1_name not in zones_dict or z2_name not in zones_dict:
                raise KeyError(
                    f"Trying to bound two not existing zones {z1_name} -> {z2_name}"
                )

            connection = Connection(
                zone1=zones_dict[z1_name],
                zone2=zones_dict[z2_name],
                max_link_capacity=conn_data.get("max_link_capacity", 1),
            )
            connections_list.append(connection)

        # 3. Instanciation des drones
        drones_list = []
        for i in range(nb_drones):
            drone = Drone(drone_id=f"D_{i}", current_position=start_zone_name)
            drones_list.append(drone)

        return Graph(
            nb_drones=nb_drones,
            zones=zones_dict,
            connections=connections_list,
            drones=drones_list,
        )

    def run(self) -> None:
        """
        Programm's main loop
        """

        print(24 * "\n")

        # get user input for specific maps
        cli_parser = CLIParser()
        map = cli_parser.parse_input()

        # parse the file
        map_parser = MapParser(map)
        raw_data = map_parser.parse()

        # create business logic objects
        graph = self._build_graph(raw_data)

        print(graph)


if __name__ == "__main__":
    app = Application()
    app.run()
