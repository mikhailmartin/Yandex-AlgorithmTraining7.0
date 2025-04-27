import sys
sys.path.append("../..")

import pytest
from pytest import param
from HomeWork1.E_backpack_max_cost import solve


@pytest.mark.parametrize(
    ("m", "items", "expected"),
    [
        param(597, [(18, 16)], 16),  # тест 1
        param(789, [(45, 51), (44, 41)], 92),  # тест 2
    ],
)
def test_E_backpack_max_cost(m, items, expected):

    assert solve(m, items) == expected
