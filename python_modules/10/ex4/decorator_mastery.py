import functools
from typing import Callable, Any
import time


def spell_timer(func: Callable) -> Callable:

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Spell completed in {end_time - start_time:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable:

    def decorator(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = kwargs.get("power")

            if power is None and args:
                if len(args) >= 3 and hasattr(args[0], "cast_spell"):
                    power = args[2]
                else:
                    power = args[0]

            if power is not None and power >= min_power:
                return func(*args, **kwargs)

            return "Insufficient power for this spell"

        return wrapper

    return decorator


"""
def retry_spell(max_attempts: int) -> Callable:
    pass


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        pass

    def cast_spell(self, spell_name: str, power: int) -> str:
        pass
"""


@spell_timer
def fireball() -> str:
    time.sleep(0.067)
    return "Fireball cast!"


def main() -> None:
    print("\nTesting spell timer...")
    print(f"Result: {fireball()}\n\n")

    print("Testing retrying spell...")


if __name__ == "__main__":
    main()
