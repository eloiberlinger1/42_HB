#!/usr/bin/env python3
"""
This module defines domain-specific error types such as
GardenError, PlantError, and WaterError
"""


class GardenError(Exception):
    """Docstring for GardenError"""
    pass


class PlantError(GardenError):
    """Exception raised for plant errors."""
    pass


class WaterError(GardenError):
    """Exception raised for water errors."""
    def __init__(self, message: str):
        """
        Docstring for __init__
        """
        super().__init__(message)


def test_custom_errors():
    """Demo of created Python exceptions"""
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as error_msg:
        print(f"Caught a PlantError: {error_msg}\n")

    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as error_msg:
        print(f"Caught a WaterError: {error_msg}\n")

    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato is wilting!")
    except GardenError as err_message:
        print(f"Caught a garden error: {err_message}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as err_message:
        print(f"Caught a garden error: {err_message}\n")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
