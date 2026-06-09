from alchemy.elements import create_air, create_earth
from elements import create_fire, create_water


def healing_potion():
    return f"Healing potion brewed with '{create_air()}' and '{create_earth()}'"


def strength_potion():
    return f"Strength potion brewed with '{create_fire()}' and '{create_water()}'"
