from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:

    allowed: list[str] = dark_spell_allowed_ingredients()

    ingredients_min = ingredients.lower()

    for i in allowed:
        if (i in ingredients_min):
            return f"{ingredients} VALID"
    
    return f"{ingredients} INVALID"
