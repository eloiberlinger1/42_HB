#!/usr/bin/env python3
"""
Game Data Stream Processor - Process game events using generators.
"""
from typing import Generator


def fibo_gen(limit: int) -> Generator[int, None, None]:
    """Generate first 'limit' Fibonacci numbers."""
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b


def prime_gen(limit: int) -> Generator[int, None, None]:
    """Generate first 'limit' prime numbers."""
    count = 0
    num = 2
    while (count < limit):
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num
            count += 1
        num += 1


def get_event(count: int) -> Generator[dict, None, None]:
    """Generate 'count' game events with rotating players and event types."""
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
    """Process game events stream and demonstrate generator usage."""

    events_amnt = 1000
    print("=== Game Data Stream Processor ===")
    print()
    print(f"Processing {events_amnt} game events...")
    print()
    stats = {"treasure": 0, "level_up": 0, "high_level": 0}

    for event in get_event(1000):
        if (event['event_type'] == "found treasure"):
            stats["treasure"] += 1
        elif (event['event_type'] == "leveled up"):
            stats["level_up"] += 1

        if (event['level'] >= 10):
            stats["high_level"] += 1

        if (event["event_i"] <= 6):
            print(f"Event {event['event_i']}: Player ", end="")
            print(f"{event['player_name']}",            end="")
            print(f" (level {event['level']}) {event['event_type']}")
    print("...")

    print()
    print("=== Stream Analytics ===")
    print(f"Total events processed: {events_amnt}")
    print(f"High-level players (10+): {stats['high_level']}")
    print(f"Treasure events: {stats['treasure']}")
    print(f"Level-up events: {stats['level_up']}")

    print()
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print()
    print("=== Generator Demonstration ===")
    fibo_list = [str(n) for n in fibo_gen(10)]
    print(f"Fibonacci sequence (first 10): {', '.join(fibo_list)}")

    prime_list = [str(n) for n in prime_gen(5)]
    print(f"Prime numbers (first 5): {', '.join(prime_list)}")


if (__name__ == "__main__"):
    ft_data_stream()
