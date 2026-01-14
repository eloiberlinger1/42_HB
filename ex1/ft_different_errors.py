#!/usr/bin/env python3

def garden_operations(value: str):
    """
    Allows to test different errors with value
    """
    if (value == "ValueError"):
        try:
            intvalue = int("abc")
            print(str(intvalue))
        except ValueError:
            print("Caught ValueError: invalid literal for int()")

    elif (value == "ZeroDivisionError"):
        try:
            result = 42 / 0
            print(result)
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero")

    elif (value == "FileNotFoundError"):
        try:
            open("none.txt")
        except FileNotFoundError:
            print("Caught FileNotFoundError: No such file")

    elif (value == "KeyError"):
        try:
            plants = {"Rose", "Tree"}
            value = plants["none"]
        except KeyError:
            print("Caught KeyError: 'missing\_plant'")

    elif (value == "multiple"):
        try:
            num = int("abc")
            print(str(num))
        except (ValueError, ZeroDivisionError, KeyError):
            print("Caught an error, but program continues!")


def test_error_types():
    """Testing errors"""
    print("=== Garden Error Types Demo\n ===")
    print("Testing ValueError...")
    garden_operations("ValueError")

    print("Testing ZeroDivisionError...")
    garden_operations("ZeroDivisionError")

    print("Testing FileNotFoundError...")
    garden_operations("FileNotFoundError")

    print("Testing KeyError...")
    garden_operations("KeyError")

    print("Testing multiple errors together...")
    garden_operations("multiple")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
