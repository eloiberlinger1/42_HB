#!/usr/bin/env python3
"""
Game Analytics Dashboard - Demonstrate list, dict, and set comprehensions.
"""


def ft_analytics_dashboard() -> None:
    """Display player statistics using comprehensions and analytics."""
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
    players_stats["diana"]["kills"] = 2863

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
    p_scores = {key: stats['level'] for key, stats in players_stats.items()}
    print(f"Player scores: {p_scores}")

    print()
    print("=== Set Comprehension Examples ===")
    p_set = {p for p, s in players_stats.items() if (s['kills'] == 0)}
    print(f"Peacefull players (0 kills): {p_set}")
    print()
    print("=== Combined Analysis ===")
    print(f"Total players: {str((len(players)))}")
    total_kills = sum(stats['kills'] for stats in players_stats.values())
    print(f"Total kills: {str(total_kills)}")
    average_kills = str(total_kills / len(players))
    print(f"Average kills: {average_kills}")
    tp_name = max(players_stats, key=lambda p: players_stats[p]['kills'])
    top_player = {
        'name': tp_name,
        'kills': players_stats[tp_name]['kills'],
        'deaths': players_stats[tp_name]['deaths'],
    }
    print("Top performer: alice (2300 points, 5 achievements")
    print(f"Top performer: {top_player['name']} ",              end="")
    print(f"{top_player['kills']} kills, {top_player['deaths']} deaths")


if (__name__ == "__main__"):
    ft_analytics_dashboard()
