from typing import Callable, Any
import functools
import operator


def spell_reducer(spells: list[int], operation: str) -> int:

    if not spells:
        return 0

    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": lambda a, b: a if a > b else b,
        "min": lambda a, b: a if a < b else b,
    }

    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")

    return functools.reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    """
    Allows to partially define an enchantement and let the
    user enter one or more parameters later when calling it
    """

    fire_enchant = functools.partial(base_enchantment, 50, "fire")
    ice_enchant = functools.partial(base_enchantment, 50, "fire")
    lightning_enchant = functools.partial(base_enchantment, 50, "fire")

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

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


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
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return _base_dispatcher


def main() -> None:
    """
    testing upper functions with demo data from the provided
    data_generator file from the subject
    """
    spell_powers = [26, 31, 11, 46, 39, 32]
    operations = ["add", "multiply", "max", "min"]
    fibonacci_tests = [18, 20, 13]

    print("Testing spell reducer...")
    print(spell_reducer(spell_powers, operations[1]))

    print("\n\nTesting memoized fibonacci...")
    fibonacci_tests = [18, 20, 13]
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
