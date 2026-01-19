#!/usr/bin/env python3
"""
Docstring for ex0.ft_ancient_text
"""


def ft_ancient_text() -> None:
    """
    Docstring for ft_ancient_text
    """
    file_path = "ancient_fragment.txt"
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print()
    print(f"Accessing Storage Vault: {file_path}")
    try:
        file = open(file_path)
        print("Connection established")

        print("RECOVERED DATA:")
        print(file.read())
        file.close()

    except Exception:
        print("ERROR: Storage vault not found.")

    print()
    print("Data recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    ft_ancient_text()
