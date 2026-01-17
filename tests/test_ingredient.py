import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import IngredientTypes


@pytest.mark.parametrize(
    "type_, name, price",
    [
        (IngredientTypes.SAUCE, "Spicy sauce", 50.0),
        (IngredientTypes.FILLING, "Meat", 200.0),
    ]
)
def test_ingredient_getters(type_, name, price):
    ing = Ingredient(type_, name, price)

    assert ing.get_type() == type_
    assert ing.get_name() == name
    assert ing.get_price() == price
