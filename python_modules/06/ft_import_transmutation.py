#!/usr/bin/env python3

import elements
from elements import create_water
from alchemy.potions import wisdom_potion as heal, strength_potion
from elements import create_earth, create_fire


def ft_import_transmutation() -> None:
    """Testing the transmutation"""
    try:
        print("=== Import Transmutation Mastery ===")
        print()
        print("Method 1 - Full module import:")
        print("alchemy.elements.create_fire(): "
              f"{elements.create_fire()}")
        print()
        print("Method 2 - Specific function import:")
        print(f"create_water(): {create_water()}")
        print()
        print("Method 3 - Aliased import:")
        print(f"heal(): {heal()}")
        print()
        print("Method 4 - Multiple imports:")
        print(f"create_earth(): {create_earth()}")
        print(f"create_fire(): {create_fire()}")
        print(f"strength_potion(): {strength_potion()}")
        print()
        print("All import transmutation methods mastered!")
    except Exception as e:
        print(f"error : {e}")


if __name__ == "__main__":
    ft_import_transmutation()
