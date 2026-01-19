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
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by Data Archivist trainee"
    ]
    try:
        file = open(file_name, "w")
        print("Storage unit created successfully...")
        print()

        print("Inscribing preservation data...")
        for e in entries:
            print(e)
            file.write(e)

        print("SECURE PRESERVATION:")
        print("[CLASSIFIED] New security protocols archived")
        print("Vault automatically sealed upon completion")
        file.close()
    except Exception:
        print("Failed to create storage unit")


if __name__ == "__main__":
    ft_archive_creation()
