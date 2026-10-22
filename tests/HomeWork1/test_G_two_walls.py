import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork1.G_two_walls.main import build_options, has_solution


WALL1 = [
    [(1, 1), (2, 2), (3, 3)]
]
OPTIONS1 = [
    [0, 1, 2, 2, 3, 3, 3]
]
WALL2 = [
    [(1, 3), (3, 3), (5, 3), (7, 3)],
    [(2, 4), (4, 4), (6, 4)],
]
OPTIONS2 = [
    [0, -1, -1, 1, -1, -1, 3, -1, -1, 5, -1, -1, 7],
    [0, -1, -1, -1, 2, -1, -1, -1, 4, -1, -1, -1, 6],
]

@pytest.mark.parametrize(
    ("wall", "expected"),
    [
        param(WALL1, OPTIONS1),
        param(WALL2, OPTIONS2)
    ],
)
def test_build_options(wall, expected):
    assert build_options(wall) == expected


@pytest.mark.parametrize(
    ("wall", "expected"),
    [
        param(WALL1, True),
        param(WALL2, False),
    ],
)
def test_has_solution(wall, expected):
    options = build_options(wall)
    common_splits = has_solution(options)
    assert bool(common_splits) == expected
