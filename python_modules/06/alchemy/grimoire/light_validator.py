from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:

    allowed: list[str] = light_spell_allowed_ingredients()

    ingredients_min = ingredients.lower()

    for i in allowed:
        if (i in ingredients_min):
            return f"{ingredients} VALID"
    
    return f"{ingredients} INVALID"
