from abc import ABC, abstractmethod


class Creature(ABC):

    def __init__(self, name: str, creature_type: str) -> None:
        self.name: str = name
        self.creature_type: str = creature_type

    @abstractmethod
    def attack(self) -> str:
        """To be define more exactely for each creature"""
        pass

    def __str__(self):
        """To display a creature"""
        return f"{self.name} is a {self.creature_type} type Creature"
