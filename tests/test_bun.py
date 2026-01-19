import pytest
from praktikum.bun import Bun

@pytest.mark.parametrize(
    "name, price",
    [
        ("Black bun", 100.0),
        ("White bun", 80.5),
        ("Space bun", 0.0),
    ]
)
def test_bun_getters_return_correct_values(name, price):
    bun = Bun(name, price)

    assert bun.get_name() == name
    assert bun.get_price() == price

