from ex0 import CreatureFactory
import ex0.factory as factory


flame_fact = factory.FireCreatureFactory()
aqua_fact = factory.WaterCreatureFactory()


def initiate_creature(
    factory: CreatureFactory,
    basename: str,
    evolvedname: str
) -> None:
    print("Testing factory")
    creature = factory.create_base_creature(basename)
    print(f"{creature.attack()}")
    creature = factory.create_evolved_creature(evolvedname)
    print(f"{creature.attack()}")
    print()


initiate_creature(flame_fact, "Flameling", "Pyrodon")
initiate_creature(aqua_fact, "Aquabub", "Torragon")


def make_them_fight(
        factory1: CreatureFactory,
        factory2: CreatureFactory
) -> None:
    print("Testing battle")
    flameling = factory1.create_base_creature("flameling")
    print("vs.")
    aquabub = factory1.create_base_creature("aquabub")
    flameling.attack()
    aquabub.attack()


make_them_fight(flame_fact, aqua_fact)
