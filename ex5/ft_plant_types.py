#!/usr/bin/env python3
"""
A modular garden simulation demonstrating class inheritance in Python.
It defines a base Plant class and specialized subclasses for Flowers,
Trees, and Vegetables, each with unique attributes and behaviors.
"""


class Plant:
    """Represent a plant"""
    def __init__(self, name: str, height: int, age: int) -> None:
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
        (to only change age set GPD values to 0)
        """
        height_before = self.height

        self.age += days_to_age
        self.grow(days_to_age * growth_per_day)

        return (self.height - height_before)


class Flower(Plant):
    """Represent a flower"""
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """init function, what did you expect ?"""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """
        Docstring for bloom

        :param self: Description
        """
        print(f"{self.name} is blooming beautifully!\n")

    def __str__(self) -> str:
        """
        print the plant informations
        """
        return (f"{self.name} (Flower): {self.height}cm, {self.age}"
                f" days, {self.color} color")


class Tree(Plant):
    """
    represent a tree
    """

    def __init__(self, name: str, h: int, a: int, trunk: int) -> None:
        """
        Docstring for __init__

        :param self: Description
        :param name: Description
        :type name: str
        :param h: Description
        :type h: int
        :param a: Description
        :type a: int
        :param trunk: Description
        :type trunk: int
        """
        super().__init__(name, h, a)
        self.trunk_diameter = trunk

    def produce_shade(self) -> int:
        """
        Docstring for produce_shade

        :param self: Description
        :return: Description
        :rtype: int
        """
        return int(self.height * 0.10 + self.trunk_diameter)

    def __str__(self) -> str:
        """
        Docstring for __str__

        :param self: Description
        :return: Description
        :rtype: str
        """
        return (f"{self.name} (Tree): {self.height}cm, {self.age} days, "
                f"{self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    """
    Docstring for Vegetable
    """

    def __init__(self, name: str, h: int, a: int, season: str) -> None:
        """
        Docstring for __init__

        :param self: self
        :param name: name of vegetable
        :type name: str
        :param h: height
        :type h: int
        :param a: age
        :type a: int
        :param season: season
        :type season: str
        """
        super().__init__(name, h, a)
        self.harvest_season = season
        self.nutritional_value = "Vitamin C"

    def __str__(self) -> str:
        """
        Docstring for __str__

        :param self: Description
        :return: Description
        :rtype: str
        """
        return (f"{self.name} (Vegetable): {self.height}cm, {self.age} days, "
                f"{self.harvest_season} harvest")


def main() -> None:
    """
    Docstring for main
    """
    print("=== Garden Plant Types ===\n")

    rose = Flower("Rose", 25, 30, "red")
    print(rose)
    rose.bloom()

    oak = Tree("Oak", 500, 1825, 50)
    print(oak)
    print(f"{oak.name} provide {oak.produce_shade()} square meters of shade\n")

    tomato = Vegetable("Tomato", 80, 90, "summer")
    print(tomato)
    print(f"{tomato.name} is rich in {tomato.nutritional_value}")


if __name__ == "__main__":
    """
    Run garden demo
    """
    main()
