import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork4.G_islands import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "4 5",
                "1 2",
                "1 3",
                "2 3",
                "3 4",
                "4 1",
            ],
            4,
            id="example1",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
