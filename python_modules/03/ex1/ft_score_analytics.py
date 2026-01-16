#!/usr/bin/env python3
"""
getting and interpreting input and args
"""

import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    if (len(sys.argv) == 1):
        errormsg = "No scores provided. Usage: python3 ft_score_a"
        errormsg += "nalytics.py <score1> <score2> ..."
        print(errormsg)
        return

    user_i = []
    for i in sys.argv[1:]:
        try:
            user_i.append(int(i))
        except ValueError:
            print("Only numeric values please")
    print(f"Scores proceed: {str(user_i)}")
    print(f"Total players: {len(user_i)}")
    print(f"Total score: {sum(user_i)}")


if __name__ == "__main__":
    main()
