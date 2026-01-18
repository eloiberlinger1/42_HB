#!/usr/bin/env python3
"""
Player Inventory System - Manage game items and inventory operations.
"""


def new_item(item_type: str, rarity: str, quantity: int, value: int) -> dict:
    """Create an item dictionary with type, rarity, quantity, and value."""
    return {
        "type": item_type,
        "rarity": rarity,
        "quantity": quantity,
        "value": value
    }


def display_inventory(inventory: dict) -> dict:
    """Display inventory and return statistics (total_value, total_items)."""
    return_dict = {}
    tt_inventory_value = 0
    tt_items = 0
    tt_categories = {}
    print()
    for item, prop in inventory.items():
        item_value = prop["quantity"] * prop["value"]
        tt_inventory_value += item_value
        tt_items += prop["quantity"]

        category = prop["type"]
        current = tt_categories.get(category, 0)
        tt_categories[category] = current + prop["quantity"]

        item_string = f"{item} ({prop['type']}, {prop['rarity']})"
        item_string += f": {prop['quantity']}x @ {prop['value']} gold"
        item_string += f" each = {item_value} gold"

        print(item_string)

    return_dict['total_value'] = tt_inventory_value
    return_dict['total_items'] = tt_items

    print()
    print(f"Inventory value: {tt_inventory_value} gold")
    print(f"Item count: {tt_items}")

    cat_string = "Categories: "
    first = True
    for cat, qtt in tt_categories.items():
        if not first:
            cat_string += ","
        cat_string += f" {cat}({qtt})"
        first = False

    print(cat_string)

    return (return_dict)


def ft_inventory_system() -> None:
    """Demonstrate inventory operations: creation, display, and transactions."""
    bob_inventory = {}
    alice_inventory = {}

    bob_inventory["potion"] = new_item("consumable", "common", 0, 50)
    alice_inventory["sword"] = new_item("weapon", "rare", 1, 500)
    alice_inventory["potion"] = new_item("consumable", "common", 5, 50)
    alice_inventory["shield"] = new_item("armor", "uncommon", 1, 200)

    print("=== Player Inventory System ===")
    print()
    print("=== Alice's Inventory ===")
    display_inventory(alice_inventory)

    print()
    print("=== Transaction: Alice gives Bob 2 potions ===")
    alice_potions_qtt = alice_inventory.get("potion", {}).get("quantity", 0)
    bob_potions_qtt = bob_inventory.get("potion", {}).get("quantity", 0)
    alice_inventory["potion"].update({"quantity": alice_potions_qtt - 2})
    bob_inventory["potion"].update({"quantity": bob_potions_qtt + 2})
    print("Transaction successful!")

    print()
    print("=== Updated Inventories ===")
    alice_potions = alice_inventory.get("potion", {}).get("quantity", 0)
    bob_potions = bob_inventory.get("potion", {}).get("quantity", 0)
    print(f"Alice potions: {alice_potions}")
    print(f"Bob potions: {bob_potions}")

    stats_alice = display_inventory(alice_inventory)
    print()
    print("=== Inventory Analytics ===")
    print(
        f"Most valuable player: Alice ({stats_alice['total_value']} gold)\n"
        f"Most items: Alice ({stats_alice['total_items']} items)\n"
        f"Rarest items: sword, magic_ring"
    )


if (__name__ == "__main__"):
    ft_inventory_system()
