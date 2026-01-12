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
        """Register a plant to the local collection."""
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        """Simulate a growth cycle for all registered plants."""
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(1)

    def generate_report(self) -> None:
        """make report for all gardens"""
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for p in self.plants:
            if isinstance(p, PrizeFlower):
                print(p)
            elif isinstance(p, FloweringPlant):
                print(f"{p.name}: {p.height}cm, {p.color} flowers (blooming)")
            else:
                print(f"{p.name}: {p.height}cm")
        print(f"Plants added: {len(self.plants)}")
        score = self.stats.calculate_points(self.plants)
        print(f"Garden score for {self.owner}: {score}")

    @staticmethod
    def validate_height(value: int) -> bool:
        """Utility function that doesn't require instance data."""
        return value >= 0

    @classmethod
    def create_garden_network(cls, owners: list[str]) -> list['GardenManager']:
        """Build a network of managers from a list of owners."""
        return [cls(name) for name in owners]


def main() -> None:
    """
    Docstring for main
    """
    print("=== Garden Management System Demo ===\n")
# Creating the network
    network = GardenManager.create_garden_network(["Alice", "Bob"])
    alice_garden = network[0]
    bob_garden = network[1]

    # Populate Alice's Garden
    alice_garden.add_plant(Plant("Oak Tree", 100))
    alice_garden.add_plant(FloweringPlant("Rose", 25, "red"))
    alice_garden.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))

    alice_garden.grow_all()
    alice_garden.generate_report()

    # Bob's Garden
    print("")
    bob_garden.add_plant(Plant("Bush", 90))
    bob_score = bob_garden.stats.calculate_points(bob_garden.plants)

    # Final Network Analytics [cite: 309]
    print(f"\nHeight validation test: {GardenManager.validate_height(10)}")
    print(f"Garden scores Alice: "
          f"{alice_garden.stats.calculate_points(alice_garden.plants)}, "
          f"Bob: {bob_score}")
    print(f"Total gardens managed: {GardenManager.total_gardens}")


if __name__ == "__main__":
    main()
