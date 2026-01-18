#!/usr/bin/env python3


def ft_analytics_dashboard():
    """
    Docstring for ft_analytics_dashboard
    """
    players = [
        "alice",
        "bob",
        "charlie",
        "diana",
        "eve",
        "frank"
    ]
    characterisis = ["level", "kills", "deaths"]
    players_stats = {p: {c: 0 for c in characterisis} for p in players}

    # Define example values
    players_stats["alice"]["level"] = 20
    players_stats["charlie"]["level"] = 25
    players_stats["eve"]["level"] = 2
    players_stats["alice"]["kills"] = 540
    players_stats["charlie"]["kills"] = 225
    players_stats["eve"]["kills"] = 28

    print("=== Game Analytics Dashboard ===")
    print()
    print("=== List Comprehension Examples ===")

    high_level_p = [p for p in players_stats if players_stats[p]['level'] > 10]
    print(f"High level players (>10): {high_level_p}")

    kills_not_doubled = [stat['kills'] for stat in players_stats.values()]
    kills_doubled = [stat['kills'] * 2 for stat in players_stats.values()]
    print(f"Kills not doubled: {kills_not_doubled}")
    print(f"Kills doubled: {kills_doubled}")

    active_p = [p for p in players_stats if players_stats[p]['level'] > 0]
    print(f"Active players: {active_p}")

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
