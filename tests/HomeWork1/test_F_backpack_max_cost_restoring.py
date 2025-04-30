import sys
sys.path.append("../..")

import pytest
from pytest import param
from HomeWork1.F_backpack_max_cost_restoring import get_options, solve


def test_get_options():

    m = 6
    items = [(2, 7), (4, 2), (1, 5), (2, 1)]
    expected = [
        [(0, 0), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1)],
        [(0, 0), (-1, -1), (7, 1), (-1, -1), (-1, -1), (-1, -1), (-1, -1)],
        [(0, 0), (-1, -1), (7, 1), (-1, -1), (2, 2), (-1, -1), (9, 2)],
        [(0, 0), (5, 3), (7, 1), (12, 3), (2, 2), (7, 3), (9, 2)],
        [(0, 0), (5, 3), (7, 1), (12, 3), (8, 4), (13, 4), (9, 2)],
    ]

    assert get_options(m, items) == expected


@pytest.mark.parametrize(
    ("m", "items", "expected"),
    [
        param(6, [(2, 7), (4, 2), (1, 5), (2, 1)], [1, 3, 4]),
    ],
)
def test_F_backpack_max_cost_restoring(m, items, expected):

    assert solve(m, items) == expected
