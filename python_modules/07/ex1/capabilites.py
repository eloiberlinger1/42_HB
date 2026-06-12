import ex0
from abc import ABC, abstractmethod


class HealCapability(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def heal(self):  # add target ?
        print("heals itself for a small amount")


class TransformCapability(ABC):
    def __init__(self):
        pass


class HealingCreatureFactory(ex0.CreatureFactory):
    def __init__(self):
        pass
    