#!/usr/bin/env python3
"""
Player Score Analytics - Calculate statistics from numeric scores.
"""

import sys


def main() -> None:
    """Process scores from command-line and display statistics."""
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
    print(f"Total players: {str(len(user_i))}")
    print(f"Total score: {str(sum(user_i))}")
    print(f"Average score: {str(sum(user_i)/len(user_i))}")
    print(f"High score: {str(max(user_i))}")
    print(f"Low score: {str(min(user_i))}")
    print(f"Score range: {str(max(user_i)-min(user_i))}")


if __name__ == "__main__":
    main()
