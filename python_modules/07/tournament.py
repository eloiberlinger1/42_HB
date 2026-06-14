from typing import List, Tuple

from ex1 import (
    HealingCreatureFactory,
    TransformCreatureFactory,
    HealCapability,
    TransformCapability
)
from ex0 import (
    CreatureFactory,
    FireCreatureFactory,
    WaterCreatureFactory
)
import ex2

def run_tournament(opponents: List[Tuple[CreatureFactory, BattleStrategy]])

heal_fact = HealingCreatureFactory()
transfo_fact = TransformCreatureFactory()
flame_fact = FireCreatureFactory()
water_fact = WaterCreatureFactory()

print("Tournament 0 (basic)")


print("[ (Flameling+Normal), (Healing+Defensive) ]")

print("*** Tournament ***")
print("2 opponents involved")

print("* Battle *")

f = flame_fact.create_evolved_creature("test flame")
print("vs.")
h = heal_fact.create_evolved_creature("test heal")

print("now fight!")

