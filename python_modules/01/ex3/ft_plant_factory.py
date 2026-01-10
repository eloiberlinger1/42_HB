#!/usr/bin/env python3
"""
add text
"""


class Plant:
    """Represent a plant"""
    def __init__(self, name: str, height: int, age: int):
        """Initialize a plant with name height and age"""
        self.name = name
        self.height = height
        self.age = age
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")

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


def main():
    """
    Create 5 plants, make them grow
    """
    print("=== Plant Factory Output ===")
    plants = {
        "Margerite": Plant("Margerite", 5, 90),
        "Rose": Plant("Rose", 5, 90),
        "Lila": Plant("Lila", 5, 90),
        "Dandelion": Plant("Dandelion", 5, 90),
        "Cactus": Plant("Cactus", 5, 90)
    }

    print(f"Total plants created: {len(plants)}")


if __name__ == "__main__":
    main()
