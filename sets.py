from sets_categories_data import (ALCOHOLS)


def clean_ingredients(dish_name, dish_ingredients):
    set_ingredients = set(dish_ingredients)
    return dish_name, set_ingredients


def check_drinks(drink_name, drink_ingredients):
    set_ingredients = set(drink_ingredients)
    if len(set_ingredients.intersection(ALCOHOLS))>0:
        return f"{drink_name} Cocktail"
    else:
        return f"{drink_name} Mocktail"

