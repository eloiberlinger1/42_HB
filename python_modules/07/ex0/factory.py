from .factory_base import AbstractCreatureFactory
from .creature_base import Creature
from .creatures import Flameling, Pyrodon, Aquabub, Torrential


class FireCreatureFactory(AbstractCreatureFactory):
    def create_base_creature(self, name: str) -> Creature:
        return Flameling(name)

    def create_evolved_creature(self, name: str) -> Creature:
        return Pyrodon(name)


class WaterCreatureFactory(AbstractCreatureFactory):
    def create_base_creature(self, name: str) -> Creature:
        return Aquabub(name)

    def create_evolved_creature(self, name: str) -> Creature:
        return Torrential(name)
