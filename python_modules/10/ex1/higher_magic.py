#! /usr/local/bin/python3

from typing import Callable

Spell = Callable[[str, int], str]


def spell_combiner(
    spell1: Spell, spell2: Spell
) -> Callable[[str, int], tuple[str, str]]:

    def result(target: str, power: int) -> tuple[str, str]:
        return ((spell1(target, power)), (spell2(target, power)))

    return result


def power_amplifier(base_spell: Spell, multiplier: int) -> Spell:

    def result(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return result


def conditional_caster(
    condition: Callable[[str, int], bool], spell: Spell
) -> Spell:

    def result(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"

    return result


def spell_sequence(
    spells: list[Spell],
) -> Callable[[str, int], list[str]]:

    def result(target: str, power: int) -> list[str]:
        results = []
        for f in spells:
            results.append(f(target, power))

        return results

    return result


def main() -> None:
    print("Testing spell combiner...")

    test_values = [11, 25, 17]
    test_targets = ["Dragon", "Goblin", "Wizard", "Knight"]

    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    comb_spell_result = spell_combiner(fireball, heal)
    spell_output = comb_spell_result(test_targets[0], test_values[0])
    print(f"Combined spell result: {spell_output[0]}, {spell_output[1]}\n")

    print("Testing power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original power 10 description -> {fireball('Dragon', 10)}")
    print(f"Amplified power 10 description -> {mega_fireball('Dragon', 10)}")


if __name__ == "__main__":
    main()
