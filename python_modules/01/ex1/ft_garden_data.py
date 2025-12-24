#!/usr/bin/env python3

class Plant:
    """Represent a plant"""
    def __init__(self, name: str, height: int, age: int):
        """Initialize a plant with name height and age"""
        self.name = ""
        self.height = 0
        self.age = 0

    def display_info(self):
        """Display plant informations"""
        print(f"Name : {self.name}")
        print(f"Name : {self.height}cm")
        print(f"Age : {self.age}")


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
