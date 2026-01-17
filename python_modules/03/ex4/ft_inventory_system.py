#!/usr/bin/env python3
"""
ex4.ft_inventory_system
"""


def new_item(item_type: str, rarity: str, quantity: int, value: int) -> dict:
    """Returns an item in the expected dict format"""
    return {
        "type": item_type,
        "rarity": rarity,
        "quantity": quantity,
        "value": value
    }


def display_inventory(inventory: dict) -> None:
    """
    Docstring for display_inventory
    """
    tt_inventory_value = 0
    tt_items = 0
    tt_categories = {}
    print()

    for item, prop in inventory:
        item_value = prop["quantity"] * prop["value"]
        tt_inventory_value += item_value
        tt_items += prop["quantity"]
        item_string = f"{item} ({prop['type']}, {prop['rarity']})"
        item_string += f": {prop['quantity']}x @ {prop['value']} gold"
        item_string += " each = {item_value} gold"

    print(item_string)
    print()
    print(f"Inventory value: {tt_inventory_value}")
    print(f"Item count: {tt_items}")

    cat_string = "Categories: "
    first = True
    for cat, qtt in tt_categories.items():
        if not first:
            cat_string += ","
        cat_string += f" {cat}({qtt})"
        first = False

    print(cat_string)


def ft_inventory_system():
    bob_inventory = {}
    alice_inventory = {}

    alice_inventory["potion"] = new_item("consumable", "common", 0, 50)

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


if (__name__ == "__main__"):
    ft_inventory_system()
