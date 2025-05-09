import sys
sys.path.append("../..")

import pytest
from pytest import param
from HomeWork1.F_backpack_max_cost_restoring import Item
from HomeWork1.F_backpack_max_cost_restoring import get_options_2d, solve


ITEMS1 = [Item(2, 7), Item(4, 2), Item(1, 5), Item(2, 1)]


def test_get_options():

    m = 6
    expected = [
        [(0, 0), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1)],
        [(0, 0), (-1, -1), (7, 1), (-1, -1), (-1, -1), (-1, -1), (-1, -1)],
        [(0, 0), (-1, -1), (7, 1), (-1, -1), (2, 2), (-1, -1), (9, 2)],
        [(0, 0), (5, 3), (7, 1), (12, 3), (2, 2), (7, 3), (9, 2)],
        [(0, 0), (5, 3), (7, 1), (12, 3), (8, 4), (13, 4), (9, 2)],
    ]

    assert get_options_2d(m, ITEMS1) == expected


@pytest.mark.parametrize(
    ("m", "items", "expected"),
    [
        param(6, ITEMS1, [4, 3, 1]),
    ],
)
def test_F_backpack_max_cost_restoring(m, items, expected):

    assert solve(m, items) == expected
