#!/usr/bin/env python3

def water_plants(plant_list):
    """Water plants"""
    try:
        print("Opening watering system")
        for p in plant_list:
            if (p is not None):
                print(f"Watering {p}")
            else:
                raise Exception()
    except Exception:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """Test watering system with valid and invalid inputs"""
    valid_plant_list = ["tomato", "dill", "coriander", "lettuce"]
    invalid_plant_list = ["Bombardino crocodilo", "Ballerino Cappuccino", None]

    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plants(valid_plant_list)
    print("Watering completed successfully!\n")
    print("Testing with error...")
    water_plants(invalid_plant_list)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
