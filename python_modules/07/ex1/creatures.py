from ex0.creature_base import Creature
from .capabilites import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Grass")

    def describe(self) -> None:
        return super().describe()

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self) -> str:
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Grass/Fairy")

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount"

    def describe(self) -> None:
        return super().describe()
    

class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Normal")
        self.transformed = False

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} returns to normal."

    def attack(self) -> str:
        if (self.transformed):
            return f"{self.name} performs a boosted strike!"
        else:
            return f"{self.name} attacks normally."

    def describe(self) -> None:
        return super().describe()


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Normal/Dragon")
        self.transformed = False

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} stabilizes its form."

    def attack(self) -> str:
        if (self.transformed):
            return f"{self.name} unleashes a devastating morph strike!"
        else:
            return f"{self.name} attacks normally."

    def describe(self) -> None:
        return super().describe()
