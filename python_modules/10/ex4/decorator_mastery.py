import functools
import time
from typing import Any, Callable


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
                elif len(args) > 0:
                    power = args[0]

            if power is not None and power >= min_power:
                return func(*args, **kwargs)

            return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:

    def decorator(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:

            for attempt in range(1, max_attempts + 1):

                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying {attempt}/{max_attempts}")

            return f"Spell casting failed after {max_attempts} attempts"
     
        return wrapper

    return decorator



"""


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


@retry_spell(3)
def spell_test(i: int) -> None:
    
    if (i == -1):
        raise ValueError("Waaaaaaagh spelled !")
    else:
        print("It worked")


def main() -> None:
    print("\nTesting spell timer...")
    print(f"Result: {fireball()}\n\n")

    decorator_config = power_validator(10)
    # cast_spell = decorator_config()
    # testing to implement

    print("Testing retrying spell...")
    retry_result = spell_test(-1)
    print(f"Result: {retry_result}\n")



if __name__ == "__main__":
    main()
