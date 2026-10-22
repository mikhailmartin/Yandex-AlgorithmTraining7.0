import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork1.F_backpack_max_cost_restoring.main import Item
from HomeWork1.F_backpack_max_cost_restoring.main import main, get_options_2d


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
    ("lines", "expected"),
    [
        param(["4 6", "2 4 1 2", "7 2 5 1"], [4, 3, 1], id="example"),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
