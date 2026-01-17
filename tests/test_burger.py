from praktikum.burger import Burger


def test_set_buns_sets_bun(bun):
    burger = Burger()
    burger.set_buns(bun)

    assert burger.bun == bun


def test_add_ingredient_adds_item(sauce):
    burger = Burger()
    burger.add_ingredient(sauce)

    assert len(burger.ingredients) == 1
    assert burger.ingredients[0] == sauce
