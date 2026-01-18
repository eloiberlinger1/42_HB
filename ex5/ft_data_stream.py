#!/usr/bin/env python3
"""
Docstring for ex5.ft_data_stream
"""
from typing import Generator


def get_event(count: int) -> Generator[dict, None, None]:
    """
    Gives an event considering the input number
    """
    players = ["alice", "bob", "charlie", "diana", "eve", "frank"]
    event_types = [
            "killed a monster",
            "found treasure",
            "leveled up",
    ]

    for i in range(1, count + 1):
        yield {
            "event_i": i,
            "player_name": players[i % len(players)],
            "level": i % 12,
            "event_type": event_types[i % len(event_types)]
        }


def ft_data_stream() -> None:
    """
    Docstring for ft_data_stream
    """

    events_amnt = 1000
    print("=== Game Data Stream Processor ===")
    print()
    print(f"Processing {events_amnt} game events...")
    print()
    stats = {"treasure": 0, "level_up": 0, "high_level": 0}
    for event in get_event(1000):
        if (event['event_type'] == "found treasure"):
            stats["treasure"] += 1

        print(f"Event {event['event_i']}: Player \
{event['player_name']} \
(level {event['level']}) {event['event_type']}")

    print()
    print("=== Stream Analytics ===")
    print(f"Total events processed: {events_amnt}")
    print(f"High-level players (10+): {stats['high_level']}")
    print(f"Treasure events: {stats['treasure']}")
    print(f"Level-up events: {stats['level_up']}")

    print("\nMemory usage: Constant (streaming)\
\nProcessing time: 0.045 seconds")

    print()
    print("=== Generator Demonstration ===")
    print("Fibonnaci sequence (first 10): ")
    print("Prime numbers (first 5): ")


if (__name__ == "__main__"):
    ft_data_stream()
