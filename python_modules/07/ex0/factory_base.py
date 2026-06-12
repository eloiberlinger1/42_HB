from abc import ABC, abstractmethod
from .creature_base import Creature


class CreatureFactory(ABC):

    @abstractmethod
    def create_base_creature(self, name: str) -> Creature:
        """Return level 1 creature."""
        pass

    @abstractmethod
    def create_evolved_creature(self, name: str) -> Creature:
        """Returns evolved creature."""
        pass
