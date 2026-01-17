#!/usr/bin/env python3
"""
Archivment tracker exercise
"""


def ft_achievement_tracker() -> None:
    """
    Docstring for ft_archivment_tracker
    """

    alice = {"first_kill", "level_10", "level_50"}
    bob = {"explorer", "treasure_hunter", "boss_slayer", "collector"},
    charlie = {"perfectionist", "social_butterfly", "lone_wolf", "strategist"}

    print("=== Achievement Tracker System ===")

    print()
    all_achievements = alice.union(bob).union(charlie)
    print(
        f"All unique achievements: {all_achievements}\n"
        f"Total unique achievements: {len(all_achievements)}"
    )

    print()
    common_achievements = alice.intersection(bob).intersection(charlie)
    players = [('alice', alice), ('bob', bob), ('charlie', charlie)]
    rare_achievements = set()
    for achievement in all_achievements:
        count = 0
        for _, player_achievements in players:
            if achievement in player_achievements:
                count += 1
        if count == 1:
            rare_achievements = rare_achievements.union({achievement})

    print(
        f"Common to all players: {common_achievements}\n"
        f"Rare achievements (1 player): {rare_achievements}"
    )

    print()
    print(
        f"Alice vs Bob common: {alice.intersection(bob)}\n"
        f"Alice unique: {alice.difference(bob)}\n"
        f"Bob unique: {bob.difference(alice)}"
    )


if __name__ == "__main__":
    ft_achievement_tracker()
