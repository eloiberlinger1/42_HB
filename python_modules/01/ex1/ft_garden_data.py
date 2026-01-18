#!/usr/bin/env python3
"""
This module provides a simple registry system for plants in a garden.
It defines a Plant class and a function to display plant data.
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


def garden_data():
    """Create and manage plants"""
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    rose.display_info()
    sunflower.display_info()
    cactus.display_info()


if __name__ == "__main__":
    garden_data()
