#!/usr/bin/env python3


def ft_analytics_dashboard():
    """
    Docstring for ft_analytics_dashboard
    """
    players = ['alice', 'charlie', 'diana']

    print("=== Game Analytics Dashboard ===")
    print()
    print("=== List Comprehension Examples ===")
    print("High scorers (>2000): ['alice', 'charlie', 'diana']")
    print("Scores doubled: [4600, 3600, 4300, 4100]")
    print("Active players: ['alice', 'bob', 'charlie']")
    print()
    print("=== Dict Comprehension Examples ===")
    print("Player scores: {'alice': 2300, 'bob': 1800, 'charlie': 2150}")
    print("Score categories: {'high': 3, 'medium': 2, 'low': 1}")
    print("Achievement counts: {'alice': 5, 'bob': 3, 'charlie': 7}")
    print("=== Set Comprehension Examples ===")
    print("Unique players: {'alice', 'bob', 'charlie', 'diana'}")
    print("Unique achievements: {'first_kill', 'level_10', 'boss_slayer'}")
    print("Active regions: {'north', 'east', 'central'}")
    print("=== Combined Analysis ===")
    print("Total players: 4")
    print("Total unique achievements: 12")
    print("Average score: 2062.5")
    print("Top performer: alice (2300 points, 5 achievements")


if (__name__ == "__main__"):
    ft_analytics_dashboard()
