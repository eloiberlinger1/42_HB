from typing import List, Tuple

from ex0 import CreatureFactory, FireCreatureFactory, WaterCreatureFactory
from ex0.creature_base import Creature
from ex1 import (
    HealingCreatureFactory,
    TransformCreatureFactory,
)
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
)


def run_tournament(
    opponents: List[Tuple[CreatureFactory, BattleStrategy]],
) -> None:
    """
    takes a list of opponents (Factory, Strategy), and make them fight.
    """
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    fighters: List[Tuple[Creature, BattleStrategy]] = []

    for index, (factory, strategy) in enumerate(opponents):
        if isinstance(factory, FireCreatureFactory):
            name = "Flameling"
        elif isinstance(factory, WaterCreatureFactory):
            name = "Aquabub"
        elif isinstance(factory, HealingCreatureFactory):
            name = "Sproutling"
        else:
            name = "Shiftling"

        creature = factory.create_base_creature(name)
        fighters.append((creature, strategy))

    for i in range(len(fighters)):
        for j in range(i + 1, len(fighters)):
            c1, strat1 = fighters[i]
            c2, strat2 = fighters[j]

            print("* Battle *")
            c1.describe()
            print("VS.")
            c2.describe()
            print("now fight!")

            try:
                print(strat1.act(c1))
                print(strat2.act(c2))

            except ValueError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    flame_fact = FireCreatureFactory()
    water_fact = WaterCreatureFactory()
    heal_fact = HealingCreatureFactory()
    transfo_fact = TransformCreatureFactory()

    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print("Tournament (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    opponents_1 = [(flame_fact, normal), (heal_fact, defensive)]
    run_tournament(opponents_1)

    print("\n" + "=" * 40 + "\n")

    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    opponents_2 = [(flame_fact, aggressive), (heal_fact, defensive)]
    run_tournament(opponents_2)

    print("\n" + "=" * 40 + "\n")

    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    opponents_3 = [
        (water_fact, normal),
        (heal_fact, defensive),
        (transfo_fact, aggressive),
    ]
    run_tournament(opponents_3)
