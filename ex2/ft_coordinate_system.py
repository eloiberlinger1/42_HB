#!/usr/bin/env python3
"""
Position tracker exercise
"""

import sys
import math


def main(cord: list[str]) -> None:
    print("=== Game Coordinate System ===")
    print()
    # unpack position
    p1 = (0, 0, 0)
    x1, y1, z1 = p1
    p2 = (5, 2, 6)
    x2, y2, z2 = p2
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

    print(
        f"Position created: {p2}\n"
        f"Distance between {p1} and {p2}: "
        f"{distance:.2f}\n"
    )


if __name__ == "__main__":
    main(sys.argv[1:])
