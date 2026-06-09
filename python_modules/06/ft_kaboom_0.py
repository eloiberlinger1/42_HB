import alchemy.grimoire as grimoire

print("=== Kaboom 0 ===")
print("Using grimoire module directly")
ingredient = "Earth, wind and fire"
print(
    "Testing record light spell: Spell recorded: Fantasy"
    f" ({ingredient} -"
    f" {grimoire.light_validator.validate_ingredients(ingredient)})"
)
