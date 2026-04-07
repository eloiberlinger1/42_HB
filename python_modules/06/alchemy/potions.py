from .elements import create_fire, create_water, create_earth, create_air


def healing_potion():
    fire_result = create_fire()
    water_result = create_water()
    return f"Healing potion brewed with {fire_result} and {water_result}"


def strength_potion():
    earth_result = create_earth()
    fire_result = create_fire()
    return f"Strength potion brewed with {earth_result} and {fire_result}"


def invisibility_potion():
    air_result = create_air()
    water_result = create_water()
    return f"Invisibility potion brewed with {air_result} and {water_result}"


def wisdom_potion():
    mix = [create_fire(), create_water(), create_earth(), create_air()]
    result = mix[0]
    for i in mix[1:]:
        result += " and "+i
    return f"Healing potion brewed with: {result}"
