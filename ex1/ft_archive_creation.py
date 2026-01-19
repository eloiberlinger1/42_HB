#!/usr/bin/env python3
"""
Docstring for ex1.ft_archive_creation
"""


def ft_archive_creation() -> None:
    """
    Docstring for ft_archive_creation
    """
    file_name = "new_discovery.txt"
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print("Initializing new storage unit: ")
    entries = [
        "[ENTRY 001] New quantum algorithm discovered\n",
        "[ENTRY 002] Efficiency increased by 347%\n",
        "[ENTRY 003] Archived by Data Archivist trainee\n"
    ]
    try:
        with open(file_name, "w") as file:
            print("Storage unit created successfully...")
            print()

            print("Inscribing preservation data...")
            for e in entries:
                print(e, end="")
                file.write(e)

            print()
            print("SECURE PRESERVATION:")
            print("[CLASSIFIED] New security protocols archived")
            print("Vault automatically sealed upon completion")
            file.close()
            print(f"Archive '{file_name}' ready for long-term preservation.")
    except Exception:
        print("Failed to create storage unit")


if __name__ == "__main__":
    ft_archive_creation()
