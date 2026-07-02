#! /usr/local/bin/python3
from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:

    return sorted(artifacts, key=lambda par: par["power"], reverse=True)


def power_filter(
    mages: list[dict[str, Any]], min_power: int
) -> list[dict[str, Any]]:

    return list(filter(lambda p: p["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda p: ("* " + p + " *"), spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    max_mage = max(mages, key=lambda p: p["power"])
    min_mage = min(mages, key=lambda p: p["power"])
    total_power = sum(m["power"] for m in mages)
    avg_power = round(total_power / len(mages), 2)

    return {
        "max_power": max_mage["power"],
        "min_power": min_mage["power"],
        "avg_power": avg_power,
    }


def main() -> None:
    """
    Testing defined functions with data from the data generator
    """
    mages = [  # noqa: F841
        {"name": "Sage", "power": 56, "element": "shadow"},
        {"name": "Phoenix", "power": 86, "element": "ice"},
        {"name": "Storm", "power": 53, "element": "light"},
        {"name": "Storm", "power": 89, "element": "earth"},
        {"name": "Nova", "power": 80, "element": "shadow"},
    ]
    artifacts = [  # noqa: F841
        {"name": "Light Prism", "power": 74, "type": "weapon"},
        {"name": "Light Prism", "power": 65, "type": "armor"},
        {"name": "Water Chalice", "power": 89, "type": "accessory"},
        {"name": "Lightning Rod", "power": 61, "type": "weapon"},
    ]

    spells = ["darkness", "flash", "tsunami", "heal"]  # noqa: F841

    print("\nTesting artifact sorter...")

    result = artifact_sorter(artifacts)

    print(
        f"{result[0].get('name')} "
        f"({result[0].get('power')} power) comes before"
        f" {result[1].get('name')} "
        f"({result[1].get('power')} power)\n"
    )

    print("Testing spell transformer...")
    for i in spell_transformer(spells):
        print(i + " ", end="")

    print()


if __name__ == "__main__":
    main()
