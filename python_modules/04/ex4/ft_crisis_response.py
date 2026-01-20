#!/usr/bin/env python3
"""
Docstring for ex4.ft_crisis_response
"""


def ft_crisis_response() -> None:
    """
    Docstring for ft_crisis_response
    """

    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print()

    file_name = "lost_archive.txt"
    try:
        print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
        with open(file_name) as file:
            content = file.read()
            print(f"{content}")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    print()

    file_name = "classified_data.txt"
    try:
        print("CRISIS ALERT: Attempting access to 'classified_data.txt'...")
        with open(file_name, "w") as file:
            file.write("restricted!")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    print("STATUS: Crisis handled, security maintained")

    print()

    file_name = "standard_archive.txt"
    try:
        print(f"ROUTINE ACCESS: Attempting access to '{file_name}.txt'...")
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"SUCCESS: Archive recovered - ``{content}''")
    except Exception as e:
        print(f"Error: {e}")
    print("STATUS: Normal operations resumed")

    print()
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    ft_crisis_response()
