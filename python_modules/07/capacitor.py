from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex0 import CreatureFactory


heal_fact = HealingCreatureFactory()
transfo_fact = TransformCreatureFactory()


def initiate_creatures(
    factory: CreatureFactory,
    basename: str,
    evolvedname: str
) -> None:
    """
    ??? Ici faire une condition pour voir si c'est un appel depuis une usine Healing ou Transform ????
    """
    print("Testing Creature with healing capability")
    print("base:")
    c = factory.create_base_creature(basename)
    c.attack()
    c.heal()
    print("evolved:")
    factory.create_evolved_creature(evolvedname)


initiate_creatures(heal_fact, "Sproutling", "Bloomelle")
initiate_creatures(transfo_fact, "Shiftling", "Morphagon")
