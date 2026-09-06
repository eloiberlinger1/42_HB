from pathlib import Path
from .parser import Parser


class Main:

    def __init__(self):
        path = Path("maps/easy/01_linear_path.txt")
        self.parser = Parser(path)

    def run(self):
        print("test")
        print(self.parser.parse())


if __name__ == "__main__":
    main = Main()
    main.run()
