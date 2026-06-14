from ex0.creature_base import Creature
from ex1 import HealCapability, TransformCapability
from abc import ABC, abstractmethod


class BattleStrategy(ABC):

    def __init__(self) -> None:
        self.valid = True
        pass

    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> str:
        return creature.attack()


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise ValueError(f"Invalid Creature '{creature.name}' for this aggressive strategy")
        
        assert isinstance(creature, TransformCapability)
        res = []
        res.append(creature.transform())
        res.append(creature.attack())
        res.append(creature.revert())

        return "\n".join(res)


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise ValueError(f"Invalid Creature '{creature.name}' for this defensive strategy")
        
        assert isinstance(creature, HealCapability)
        res = []
        res.append(creature.attack())
        res.append(creature.heal())

        return "\n".join(res)
