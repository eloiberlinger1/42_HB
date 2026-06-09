from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str):
    allowed = dark_spell_allowed_ingredients()
    if (ingredients in allowed):
        return "VALID"
    else:
        return "INVALID"
