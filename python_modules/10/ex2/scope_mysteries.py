from typing import Callable, Any


def mage_counter() -> Callable[[], int]:

    c = 0

    def result() -> int:
        nonlocal c
        c += 1
        return c

    return result


def spell_accumulator(initial_power: int) -> Callable[[int], int]:

    p = initial_power

    def result(to_add: int) -> int:
        nonlocal p
        p += to_add

        return p

    return result


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:

    def result(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return result


def memory_vault() -> dict[str, Any]:

    vault = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> Any:
        if key in vault:
            return vault[key]
        return "Memory not found"

    return {"store": store, "recall": recall}


def main() -> None:
    print("Testing mage counter...")

    counter = mage_counter()
    print(f"Counter call 1 : {counter()}")
    print(f"Counter call 2 : {counter()}")
    print(f"Counter call 3 : {counter()}")

    print("\nTesting spell accumulator...")
    base = 100
    accumulator = spell_accumulator(base)
    print(f"Base {base}, add 20 {accumulator(20)}")
    accumulator = spell_accumulator(100)
    print(f"Base {base}, add 30 {accumulator(30)}")

    print("\nTesting enchantment factory...")
    flaming_factory = enchantment_factory("Flaming")
    frozen_factory = enchantment_factory("Frozen")
    print(flaming_factory("Sword"))
    print(frozen_factory("Shield"))

    print("\nTesting memory vault...")
    vault_access = memory_vault()

    vault_access["store"]("secret", 42)
    print("Store 'secret' = 42")

    print(f"Recall 'secret' : {vault_access['recall']('secret')}")
    print(f"Recall 'unknown': {vault_access['recall']('unknown')}")


if __name__ == "__main__":
    main()
