#!/usr/bin/env python3
"""
Archivment tracker exercise
 & => .intersection()
 - => .difference()
 | => .union()
"""


def ft_achievement_tracker() -> None:
    """
    Docstring for ft_archivment_tracker
    """

    alice = {"first_kill", "level_10", "boss_slayer", "level_50"}
    bob = {"explorer", "boss_slayer", "level_10"}
    charlie = {"level_10", "lone_wolf", "strategist"}

    print("=== Achievement Tracker System ===")

    print()
    all_achievements = alice | bob | charlie
    print(
        f"All unique achievements: {all_achievements}\n"
        f"Total unique achievements: {len(all_achievements)}"
    )

    print()
    common_achievements = alice & bob & charlie
    players = [('alice', alice), ('bob', bob), ('charlie', charlie)]
    rare_achievements = set()
    for achievement in all_achievements:
        count = 0
        for _, player_achievements in players:
            if achievement in player_achievements:
                count += 1
        if count == 1:
            rare_achievements = rare_achievements | {achievement}

    print(
        f"Common to all players: {common_achievements}\n"
        f"Rare achievements (1 player): {rare_achievements}"
    )

    print()
    print(
        f"Alice vs Bob common: {alice & bob}\n"
        f"Alice unique: {alice - bob}\n"
        f"Bob unique: {bob - alice}"
    )


if __name__ == "__main__":
    ft_achievement_tracker()
