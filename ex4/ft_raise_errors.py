#!/usr/bin/env python3
"""
This module implements robust health monitoring for individual plants.
"""


def check_plant_health(plant_name, water_level, sunlight_hours):
    """Raise an error in case of invalid values"""
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too high (max 12)")
    if sunlight_hours < 2:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too low (min 2)")
    print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks():
    """test errors with vaid / invalid values"""
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    try:
        check_plant_health("tomato", 5, 6)
    except ValueError as exc:
        print(f"Error: {exc}")
    print()
    print("Testing empty plant name...")
    try:
        check_plant_health("", 5, 6)
    except ValueError as exc:
        print(f"Error: {exc}")
    print()
    print("Testing bad water level...")
    try:
        check_plant_health("tomato", 15, 6)
    except ValueError as exc:
        print(f"Error: {exc}")
    print()
    print("Testing bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except ValueError as exc:
        print(f"Error: {exc}")
    print()
    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
