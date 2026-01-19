import pytest
from unittest.mock import patch

from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.mark.parametrize(
    "method_name, fake_data, expected_class",
    [
        ("available_buns", [Bun("Fake bun 1", 111), Bun("Fake bun 2", 222)], Bun),
        (
            "available_ingredients",
            [
                Ingredient("Fake sauce", INGREDIENT_TYPE_SAUCE, 10),
                Ingredient("Fake filling", INGREDIENT_TYPE_FILLING, 20),
            ],
            Ingredient,
        ),
    ],
)
def test_database_methods_with_mock_and_parametrize(method_name, fake_data, expected_class):
    # Мокаем нужный метод базы
    with patch.object(Database, method_name, return_value=fake_data):
        db = Database()

        # Достаём метод по имени и вызываем
        result = getattr(db, method_name)()

    # Проверки
    assert isinstance(result, list)
    assert len(result) > 0
    assert all(isinstance(item, expected_class) for item in result)

