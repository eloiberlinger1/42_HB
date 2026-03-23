#!/usr/bin/env python3

import alchemy


def ft_sacred_scroll() -> None:

    print("=== Sacred Scroll Mastery ===")
    print("\nTesting direct module access:")

    # for i in dir(alchemy):
    #     attr = getattr(alchemy, i)
    #     if (callable(attr)):
    #         print(f"alchemy.elements.{i}, {attr()}")

    print(
        f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}\n"
        f"alchemy.elements.create_water(): {alchemy.elements.create_water()}\n"
        f"alchemy.elements.create_earth(): {alchemy.elements.create_earth()}\n"
        f"alchemy.elements.create_air(): {alchemy.elements.create_air()}\n"
    )

    print("Testing package-level access (controlled by __init__.py):")

    print(
        f"alchemy.create_fire(): {alchemy.create_fire()}\n"
        f"alchemy.create_water(): {alchemy.create_water()}\n"
        "alchemy.create_earth(): ", end=""
    )
    try:
        print(f"{alchemy.create_earth()}")
    except AttributeError:
        print("AttributeError - not exposed")
    print("alchemy.create_air(): ", end="")
    try:
        print(f"{alchemy.create_air()}")
    except AttributeError:
        print("AttributeError - not exposed")

    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    ft_sacred_scroll()
