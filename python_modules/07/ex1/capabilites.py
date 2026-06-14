from ex0 import CreatureFactory
from ex0.creature_base import Creature

from abc import ABC, abstractmethod


class HealCapability(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def heal(self) -> str:
        pass


class TransformCapability(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class HealingCreatureFactory(CreatureFactory):

    def __init__(self) -> None:
        pass

    def create_base_creature(self, name: str) -> Creature:
        from .creatures import Sproutling
        return Sproutling(name)

    def create_evolved_creature(self, name: str) -> Creature:
        from .creatures import Bloomelle
        return Bloomelle(name)


class TransformCreatureFactory(CreatureFactory):

    def __init__(self) -> None:
        pass

    def create_base_creature(self, name: str) -> Creature:
        from .creatures import Shiftling
        return Shiftling(name)

    def create_evolved_creature(self, name: str) -> Creature:
        from .creatures import Morphagon
        return Morphagon(name)
