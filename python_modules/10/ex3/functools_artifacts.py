from typing import Any
from collections.abc import Callable
import functools
import operator


def spell_reducer(spells: list[int], operation: str) -> int:

    if not spells:
        return 0

    if operation == "add":
        return functools.reduce(operator.add, spells)
    elif operation == "multiply":
        return functools.reduce(operator.mul, spells)
    elif operation == "max":
        return functools.reduce(max, spells)
    elif operation == "min":
        return functools.reduce(min, spells)
    else:
        raise ValueError(f"Unknown operation: {operation}")


def partial_enchanter(
    base_enchantment: Callable[[int, str], str],
) -> dict[str, Callable[..., Any]]:
    """
    Allows to partially define an enchantement and let the
    user enter one or more parameters later when calling it
    """

    fire_enchant = functools.partial(base_enchantment, 50, "fire")
    ice_enchant = functools.partial(base_enchantment, 50, "ice")
    lightning_enchant = functools.partial(base_enchantment, 50, "lightning")

    return {
        "fire": fire_enchant,
        "ice": ice_enchant,
        "lightning": lightning_enchant,
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:

    if n < 0:
        raise ValueError("n doit être un entier positif ou nul.")
    if n == 0:
        return 0
    if n == 1:
        return 1

    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:

    @functools.singledispatch
    def _base_dispatcher(spell: Any) -> str:
        """
        Base function, and function which handles the unknown
        types
        """
        return "Unknown spell type"

    @_base_dispatcher.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @_base_dispatcher.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @_base_dispatcher.register(list)
    def _(spell: list[Any]) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return _base_dispatcher


def test_enchant(power: int, spell: str) -> str:
    return "enchangement result"


def main() -> None:
    """
    testing upper functions with demo data from the provided
    data_generator file from the subject
    """
    spell_powers = [26, 31, 11, 46, 39, 32]
    operations = ["add", "multiply", "max", "min"]
    fibonacci_tests = [18, 20, 13]

    print("\ntesting partial enchanter\n")
    result = partial_enchanter(test_enchant)
    print(f"Fire enchant is {result['fire']()}")

    print("\nTesting spell reducer...")
    print(spell_reducer(spell_powers, operations[1]))

    print("\n\nTesting memoized fibonacci...")
    fibonacci_tests = [18, 2004, 2000]
    for i in fibonacci_tests:
        print(f"Fib({i}): {memoized_fibonacci(i)}")

    print("\n\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher([1, 2, 3]))
    print(dispatcher(3.141592653589793238462643383279502884197169399375105820))


if __name__ == "__main__":
    main()
