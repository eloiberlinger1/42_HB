from ex1 import (
    HealingCreatureFactory,
    TransformCreatureFactory,
    HealCapability,
    TransformCapability
)
from ex0 import CreatureFactory


heal_fact = HealingCreatureFactory()
transfo_fact = TransformCreatureFactory()


def initiate_creatures(
    factory: CreatureFactory,
    basename: str,
    evolved_name: str
) -> None:
    print("Testing Creature with healing capability")
    print("base:")
    c = factory.create_base_creature(basename)
    c.describe()
    print(c.attack())
    if (isinstance(c, HealCapability)):
        print(c.heal())
    elif (isinstance(c, TransformCapability)):
        print(c.transform())
        print(c.attack())
        print(c.revert())

    print("evolved:")
    c = factory.create_evolved_creature(evolved_name)
    print(c.attack())
    if (isinstance(c, HealCapability)):
        print(c.heal())
    elif (isinstance(c, TransformCapability)):
        print(c.transform())
        print(c.attack())
        print(c.revert())


initiate_creatures(heal_fact, "Sproutling", "Bloomelle")
initiate_creatures(transfo_fact, "Shiftling", "Morphagon")
