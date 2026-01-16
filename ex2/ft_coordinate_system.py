#!/usr/bin/env python3
"""
Position tracker exercise
"""

import sys
import math


def main(cord: list[str]) -> None:
    """
    Docstring for main

    :param cord: List of coordinates in string format ["x,y,z", ...]
    """
    print("=== Game Coordinate System ===")
    print()
    p1 = (0, 0, 0)
    x1, y1, z1 = p1
    p2 = (5, 10, 5)
    x2, y2, z2 = p2
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

    print(
        f"Position created: {p2}\n"
        f"Distance between {p1} and {p2}: "
        f"{distance:.2f}\n"
    )

    if (not cord):
        cord = ["10,20,5", "abc,def,ghi"]

    for c in cord:
        try:
            parsed_c = c.split(',')
            x2 = int(parsed_c[0])
            y2 = int(parsed_c[1])
            z2 = int(parsed_c[2])

            p2 = (x2, y2, z2)
            distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
            print(
                f"Position created: {p2}\n"
                f"Distance between {p1} and {p2}: "
                f"{distance:.2f}\n"
            )

        except Exception as e:
            print(
                f'Parsing invalid coordinates: "{cord}"\n'
                f"Error parsing coordinates: {e}\n"
                f"Error details - Type: {type(e).__name__}, Args: {e.args}\n"
            )

    p3 = (6, 7, 5)
    x3, y3, z3 = p3
    print(
        "Unpacking demonstration:\n"
        f"Player at x={x3}, y={y3}, z={z3}\n"
        f"Coordinates: X={x3}, Y={y3}, Z={z3}"
    )


if __name__ == "__main__":
    main(sys.argv[1:])
