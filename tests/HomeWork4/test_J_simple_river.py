import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork4.J_simple_river import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "4",
                "3 5 5 4",
                "5",
                "1 1",
                "2 1",
                "1 3",
                "2 2",
                "1 3",
            ],
            [75, 105, 73, 101, 83, 113],
            id="example1",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
