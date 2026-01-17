import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.bun import Bun


@pytest.fixture
def sauce():
    return Ingredient("Sauce", INGREDIENT_TYPE_SAUCE, 100)


@pytest.fixture
def filling():
    return Ingredient("Filling", INGREDIENT_TYPE_FILLING, 200)


@pytest.fixture
def bun():
    return Bun("Black bun", 100)



