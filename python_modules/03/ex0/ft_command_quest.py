#!/usr/bin/env python3
"""
Command Quest - Process and display command-line arguments.
"""

import sys


def main() -> None:
    """Display program name and all command-line arguments."""
    print("=== Command Quest ===")
    print(f"Program name: {str(sys.argv[0])}")
    print(f"Arguments received: {str(len(sys.argv) - 1)}")

    if (len(sys.argv) == 1):
        print("No arguments provided!")
    else:
        for i in range(1, len(sys.argv)):
            print(f"Argument {str(i)}: {sys.argv[i]}")
    print(f"Total arguments: {str(len(sys.argv))}\n")


if __name__ == "__main__":
    main()
