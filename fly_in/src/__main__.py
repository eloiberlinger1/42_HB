import argparse
from pathlib import Path
from .parsing import MapParser, CLIParser


class Application:

    def __init__(self) -> None:

        self.path: Path = Path("maps/easy/01_linear_path.txt")

    def run(self) -> None:
        print("test")

        cli_parser = CLIParser()
        map = cli_parser.parse_input()

        map_parser = MapParser(map)
        print(map_parser.parse())

        self.parser = MapParser(self.path)

        print(self.parser.parse())


if __name__ == "__main__":
    app = Application()
    app.run()
