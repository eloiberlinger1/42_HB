#!/usr/bin/env python3
"""

"""


class SecurePlant:
    """Represent a plant"""
    def __init__(self, name: str, height: int, age: int):
        """Initialize a plant with name height and age"""
        self.name = name
        self._height = 0
        self._age = 0

        self.set_height(height)
        self.set_age(age)

        print(f"Plant created: {self.name}")

    def set_height(self, height: int) -> None:
        """Set the height of plant"""
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = height

    def set_age(self, age: int) -> None:
        """
        Change age of plant
        """
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
        else:
            self._age = age

    def get_height(self) -> int:
        """
        return plant height
        """
        return (self._height)

    def get_age(self) -> int:
        """
        return plant age
        """
        return (self._age)

    def __str__(self):
        """Display plant informations"""
        return f"{self.name} ({self._height}cm, {self._age} days)"


def main():
    """
    demonstrate secure plant class
    """
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 25, 30)
    print(f"Height updated: {rose.get_height()}cm [OK]")
    print(f"Age updated: {rose.get_age()} days [OK]\n")
    rose.set_height(-5)
    print(f"\nCurrent plant: {rose}")


if __name__ == "__main__":
    main()
