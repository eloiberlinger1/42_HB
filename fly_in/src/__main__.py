from pathlib import Path

from .parsing import MapParser, CLIParser
from .objects import Drone, Graph, Connection, Zone
from .simulation import SimulationEngine

from typing import Dict, Any


class Application:

    def __init__(self) -> None:
        """
        Initialize the Application class
        """
        self.path: Path = Path("maps/easy/01_linear_path.txt")

    def _build_graph(self, raw_data: Dict[str, Any]) -> Graph:

        nb_drones = raw_data.get("nb_drones", 0)
        raw_zones = raw_data.get("zones", {})
        raw_connections = raw_data.get("connections", [])

        zones_dict: Dict[str, Zone] = {}
        start_zone_name = None

        # 1. Instanciation of zones
        for name, zone_info in raw_zones.items():
            type_def = zone_info.get("type_def")
            is_start = type_def == "start_hub"
            is_end = type_def == "end_hub"

            if is_start:
                start_zone_name = name

            meta = zone_info.get("metadata", {})
            zone_type = meta.get("zone", "normal")

            raw_max_drones = meta.get("max_drones")
            max_drones = int(raw_max_drones) if raw_max_drones is not None else 1
            color = meta.get("color")

            zone = Zone(
                name=name,
                x=zone_info.get("x"),
                y=zone_info.get("y"),
                zone_type=zone_type,
                max_drones=max_drones,
                color=color,
                is_start=is_start,
                is_end=is_end,
            )

            zones_dict[name] = zone

        if not start_zone_name and nb_drones > 0:
            raise ValueError("start_hub not found in the input file")

        # 2. Instanciation of connexions
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

            zones_dict[z1_name].adjacent_zones[z2_name] = connection
            zones_dict[z2_name].adjacent_zones[z1_name] = connection

            connections_list.append(connection)

        # 3. Instanciation of drones
        drones_list = []
        for i in range(nb_drones):
            drone = Drone(drone_id=f"D{i+1}", current_position=start_zone_name)
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
        print("Fly-In       eberling\n\n")

        # get user input for specific maps
        try:
            cli_parser = CLIParser()
            map_file = cli_parser.parse_input()

        except Exception as e:
            print(f"Error during treatment of user input see below : \n\n {e}")

        # parse the file
        try:
            map_parser = MapParser(map_file)
            raw_data = map_parser.parse()

        except Exception as e:
            print(f"Error during parsing of map file see below : \n\n {e}")
            exit()

        # create business logic objects
        try:
            graph = self._build_graph(raw_data)
        except Exception as e:
            print(f"Error during instanciation of the Graph. See below \n\n {e}")
            exit()

        print(graph)

        engine = SimulationEngine(graph)
        engine.run()


if __name__ == "__main__":
    app = Application()
    app.run()
