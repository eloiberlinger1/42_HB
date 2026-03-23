#!/usr/bin/env python3

import alchemy

def ft_sacred_scroll():
    print("=== Sacred Scroll Mastery ===")
    print("\nTesting direct module access:")
    for i in dir(alchemy):
        attr = getattr(alchemy, i)
        if (callable(attr)):
            print(f"alchemy.elements.{i}, {attr()}")


if __name__ == "__main__":
    ft_sacred_scroll()

