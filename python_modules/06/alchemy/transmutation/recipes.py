import alchemy
from ..potions import strength_potion
from elements import create_fire


def lead_to_gold():
    return (
        "Recipe transmuting Lead to Gold: "
        f"brew ’{alchemy.elements.create_air()}’"
        f" and ’{strength_potion()}’ mixed with ’{create_fire()}’"
    )
