#!/usr/bin/env python3
"""
This module defines the Plant class and simulates its growth cycle.
It tracks the evolution of a plant's height and age over a given
period through the ft_plant_growth function.
"""


class Plant:
    """Represent a plant"""
    def __init__(self, name: str, height: int, age: int):
        """Initialize a plant with name height and age"""
        self.name = name
        self.height = height
        self.age = age

    def display_info(self):
        """Display plant informations"""
        print(f"{self.name} : {self.height}, {self.age} days old")

    def grow(self, growth_value: int) -> None:
        """Make plant grow"""
        self.height += growth_value

    def age_plant(self, days_to_age: int, growth_per_day: int = 1) -> int:
        """
        Make the plant older and grow it.
        (to only change age set GPDV to 0)
        """
        height_before = self.height

        self.age += days_to_age
        self.grow(days_to_age * growth_per_day)

        return (self.height - height_before)


def ft_plant_growth():
    """
    Create a plant, make it grow and display related info
    """
    my_plant = Plant("Margerite", 5, 90)
    growth_per_day = 1
    days_passed = 1
    days_to_pass = 6

    print(f"=== Day {days_passed} ===")
    print(f"{my_plant.name}: {my_plant.height}cm, {my_plant.age} days old")

    growth = my_plant.age_plant(days_to_pass, growth_per_day)
    days_passed = days_to_pass

    print(f"=== Day {days_passed} ===")
    print(f"{my_plant.name}: {my_plant.height}cm, {my_plant.age} days old")
    print(f"Growth this week: +{growth}cm")


if __name__ == "__main__":
    ft_plant_growth()
