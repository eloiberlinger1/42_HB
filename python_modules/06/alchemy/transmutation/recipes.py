import alchemy
from ..potions import strength_potion


def lead_to_gold():
    return (
        f"Recipe transmuting Lead to Gold: brew ’{alchemy.elements.create_air()}’"
        f" and ’{strength_potion()}’"
    )
