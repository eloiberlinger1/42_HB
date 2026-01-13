#!/usr/bin/env python3

def check_temperature(temp_str: str) -> int:
    """
    Docstring for check_temperature

    :param input: Temperature of temperature to check
    :type input: str => (int)
    """
    try:
        print(f"Testing temperature: {temp_str}")
        input = int(temp_str)
        if (input < 0):
            print(f"Error: {temp_str}°C is too cold for plants (min 0°C)")
        elif (input > 40):
            print(f"Error: {temp_str}°C is too hot for plants (max 40°C)")
        else:
            return (input)

    except ValueError:
        print(f"Error: {temp_str} is not a valid number")


def test_temperature_input():
    """
    test_temperature_input
    """
    print("=== Garden Temperature Checker ===\n")
    if (check_temperature("25") is not None):
        print("Temperature 25°C is perfect for plants!")
    print("")
    check_temperature("abc")
    print("")
    check_temperature("100")
    print("")
    check_temperature("-50")
    print("")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
