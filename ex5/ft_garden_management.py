#!/usr/bin/env python3
"""
This module implements a comprehensive Garden Management System
"""


class GardenError(Exception):
    """Basic GardenError"""
    pass


class PlantError(GardenError):
    """Plant specific error class"""
    pass


class WaterError(GardenError):
    """Watter repated errors"""
    pass


class Plant():
    """
    Docstring for Plant
    """
    def __init__(self, name, water_level=5, sunlight=8):
        """
        Docstring for __init__
        """
        if not name:
            raise ValueError("Plant name cannot be empty!")
        self.name = name
        self.water_level = water_level
        self.sunlight = sunlight


class GardenManager():
    """
    Docstring for GardenManager
    """
    def __init__(self):
        """
        Docstring for __init__
        """
        self.plants = []

    def add_plant(self, p: Plant):
        """Docstring for addplant funciton"""
        try:
            if not isinstance(p, Plant):
                raise PlantError("Invalid Plant object!")
            self.plants.append(p)
            print(f"Added {p.name} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self):
        """
        Docstring for water_plants
        """
        print("Opening watering system")
        try:
            if not self.plants:
                raise WaterError("Not enough water in tank")
            for p in self.plants:
                print(f"Watering {p.name}")
                print("Success")
        except WaterError as e:
            print(f"Caught GardenError: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self):
        """Check the health of garden"""
        for plant in self.plants:
            try:
                if plant.water_level > 10:
                    error_content = f"Water level {plant.water_level}"
                    error_content += " is too high (max 10)"
                    raise ValueError(error_content)
                print_content = f"{plant.name}: healthy (water:"
                print_content += f"{plant.water_level}, sun: {plant.sunlight})"
                print(print_content)
            except ValueError as e:
                print(f"Error checking {plant.name}: {e}")


def test_garden_management():
    """
    Testing the GardenManagment classes.
    """
    print("=== Garden Management System ===")
    gm = GardenManager()

    # Test add plant
    gm.add_plant(Plant("tomato"))
    gm.add_plant(Plant("lettuce", water_level=15))

    # test watering (finally)
    gm.water_plants()

    # Test health
    print("Checking plant health...")
    gm.check_health()

    print("Garden management system test complete! ")


if __name__ == "__main__":
    test_garden_management()
