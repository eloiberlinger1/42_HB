from .creature_base import Creature


class Flameling(Creature):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Fire")

    def describe(self) -> None:
        return super().describe()

    def attack(self) -> str:
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Fire/Flying")

    def attack(self) -> str:
        return f"{self.name} uses Flamethrower!"

    def describe(self) -> None:
        return super().describe()


class Aquabub(Creature):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Water")

    def attack(self) -> str:
        return f"{self.name} uses Water Gun!"

    def describe(self) -> None:
        return super().describe()


class Torrential(Creature):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Water")

    def attack(self) -> str:
        return f"{self.name} uses Hydro Pump!"

    def describe(self) -> None:
        return super().describe()
