import argparse
from pathlib import Path

from .parsing import MapParser, CLIParser
from .objects import Drone, Graph, Connection, Zone


class Application:

    def __init__(self) -> None:

        self.path: Path = Path("maps/easy/01_linear_path.txt")

    def _build_graph(self, raw_data):

        nb_drones = 0
        drones_list = []

        for key, value in raw_data.items():

            if key == "nb_drones":
                nb_drones = value
            elif key == "zones":
                zones = value
            elif key == "connections":
                connections = value
            else:
                raise ValueError("Unknown configuration key")

        # Extract and create zones
        for name, metadata in zones.items():

            if metadata.get("type_def") == "start_hub":
                start_zone = Zone(
                    name="start_hub",
                    x=metadata.get("x"),
                    y=metadata.get("y"),
                    max_drones=5,
                    color=metadata.get("metadata", None).get("color"),
                )

        # Extract and create drones
        for i in range(nb_drones):

            # position to be fetched
            drone = Drone(current_position="start_hub", drone_id=f"D_{value}")

            drones_list.append(drone)

        graph = Graph(nb_drones=nb_drones)

    def run(self) -> None:
        """
        Programm's main loop
        """

        # get user input for specific maps
        cli_parser = CLIParser()
        map = cli_parser.parse_input()

        # parse the file
        map_parser = MapParser(map)
        raw_data = map_parser.parse()

        # create business logic objects
        graph = self._build_graph(raw_data)


if __name__ == "__main__":
    app = Application()
    app.run()
