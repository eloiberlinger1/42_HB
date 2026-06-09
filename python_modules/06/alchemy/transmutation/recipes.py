from alchemy.elements import create_air
import elements


def lead_to_gold():
    return (
        f"Recipe transmuting Lead to Gold: brew ’{create_air()}’ and "
        f"’created strength potion’ mixed with ’{elements.create_fire()}’"
    )