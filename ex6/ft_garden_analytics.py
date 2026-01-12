#!/usr/bin/env python3
"""
Creating a managment system for flowers.
"""


class Plant:
    """Represent a plant"""

    def __init__(self, name: str, height: int) -> None:
        """
        Init plant with height, height
        """
        self.name = name
        self.height = height

    def grow(self, cm: int) -> None:
        """
        Display plant info
        """
        self.height += cm
        print(f"{self.name} grew {cm}cm")


class FloweringPlant(Plant):
    """
    Plant that can flower
    """

    def __init__(self, name: str, height: int, color: str) -> None:
        """
        init flowering plant with height, name, color
        """
        super().__init__(name, height)
        self.color = color


class PrizeFlower(FloweringPlant):
    """
    Docstring for PrizeFlower
    """

    def __init__(self, name: str, h: int, color: str, points: int) -> None:
        """
        prize a flower
        """
        super().__init__(name, h, color)
        self.points = points

    def __str__(self):
        """
        dislpay prize flower informations
        """
        return (f"{self.name}: {self.height}cm, {self.color} flowers "
                f"(blooming), Prize points: {self.points}")


class GardenManager():
    """
    Docstring for GardenManager

    :var total_gardens: Description
    :vartype total_gardens: Literal[0]
    """

    total_gardens = 0

    class GardenStats:
        """
        Docstring for GardenStats
        """

        def calculate_points(self, plants: list[Plant]) -> int:
            """
            Docstring for calculate_points
            """
            points = 0
            for p in plants:
                if isinstance(p, PrizeFlower):
                    points += p.points * p.height
            return points

    def __init__(self, owner: str) -> None:
        """
        Docstring for __init__

        :param self: Description
        :param owner: Description
        :type owner: str
        """
        self.owner = owner
        self.plants: list[Plant] = []
        self.stats = self.GardenStats()
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant) -> None:
        """
        Docstring for add_plant

        :param self: Description
        :param plant: Description
        :type plant: Any
        """
        self.plants += plant
        print(f"Added {plant.name} to {self.owner}'s garden")


def main() -> None:
    """
    Docstring for main
    """
    print("=== Garden Management System Demo ===\n")

    alice_garden = GardenManager("Alice")

    p1 = Plant("Oak Tree", 100)
    p2 = FloweringPlant("Rose", 25, "red")
    p3 = PrizeFlower("Sunflower", 50, "yellow", 10)

    alice_garden.add_plant(p1)
    alice_garden.add_plant(p2)
    alice_garden.add_plant(p3)

    alice_garden.grow_all()
    alice_garden.generate_report()

    print(f"Height validation test: {GardenManager.validate_height(10)}")

    bob_garden = GardenManager("Bob")
    bob_garden.add_plant(Plant("Bush", 90))
    bob_score = bob_garden.stats.calculate_score(bob_garden.plants)

    print(f"Garden scores Alice: "
          f"{alice_garden.stats.calculate_score(alice_garden.plants)}, "
          f"Bob: {bob_score}")
    print(f"Total gardens managed: {GardenManager.total_gardens}")


if __name__ == "__main__":
    main()
