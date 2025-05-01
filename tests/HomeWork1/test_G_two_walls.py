import sys
sys.path.append("../..")

import pytest
from pytest import param
from HomeWork1.G_two_walls import Solver


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

    solver = Solver(wall=wall)
    solver.build_options()

    assert solver.options == expected


@pytest.mark.parametrize(
    ("wall", "expected"),
    [
        param(WALL1, True),
        param(WALL2, False),
    ],
)
def test_has_solution(wall, expected):

    solver = Solver(wall=wall)
    solver.build_options()
    flag = solver.has_solution()

    print(solver.common_splits)

    assert flag == expected
