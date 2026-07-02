import functools
import time
from typing import Any, Callable, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def spell_timer(func: F) -> F:

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Spell completed in {end_time - start_time:.3f} seconds")
        return result

    return wrapper  # type: ignore[return-value]


def power_validator(min_power: int) -> Callable[[F], F]:

    def decorator(func: F) -> F:

        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = kwargs.get("power")

            if power is None and args:
                if len(args) >= 3 and hasattr(args[0], "cast_spell"):
                    power = args[2]
                elif len(args) > 0:
                    power = args[0]

            if power is not None and power >= min_power:
                return func(*args, **kwargs)

            return "Insufficient power for this spell"

        return wrapper  # type: ignore[return-value]

    return decorator


def retry_spell(max_attempts: int) -> Callable[[F], F]:

    def decorator(func: F) -> F:

        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:

            for attempt in range(1, max_attempts + 1):

                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying {attempt}/{max_attempts}")

            return (
                f"Spell casting failed after {max_attempts} attempts"
                "\nWaaaaaaagh spelled !"
            )

        return wrapper  # type: ignore[return-value]

    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        alpha_spaces_only = all(
            char.isalpha() or char.isspace() for char in name
        )
        if len(name) >= 3 and alpha_spaces_only:
            return True
        return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    time.sleep(0.067)
    return "Fireball cast!"


@retry_spell(3)
def spell_test(i: int) -> None | str:

    if i == 2:
        return str(i)

    raise ValueError()


"""
@power_validator(10)
def test_spell(power: int, cast_spell: str, target: str) -> None:
    print("Spell done and checked with power validator !")
"""


def main() -> None:
    print("\nTesting spell timer...")
    print(f"Result: {fireball()}\n\n")

    # print("Testing power validator:")
    # print(test_spell(5, "fire", "dragon"))

    print("\nTesting retrying spell...")
    retry_result = spell_test(1)
    print(retry_result)

    test_powers = [14, 9, 20, 26]
    spell_names = ["heal", "tsunami", "flash", "earthquake"]
    mage_names = ["Casey", "Pho_enix", "Nova", "Kai", "Storm", "Ash"]

    print("\n\nTesting MageGuild...")
    mg_inst = MageGuild()

    print(mg_inst.validate_mage_name(mage_names[0]))
    print(mg_inst.validate_mage_name(mage_names[1]))
    print(mg_inst.cast_spell(spell_names[0], test_powers[0]))
    print(mg_inst.cast_spell(spell_names[1], test_powers[1]))

    print()


if __name__ == "__main__":
    main()
