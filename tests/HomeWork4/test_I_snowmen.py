import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork4.I_snowmen import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "8",
                "0 1",
                "1 5",
                "2 4",
                "3 2",
                "4 3",
                "5 0",
                "6 6",
                "1 0",
            ],
            74,
            id="example1",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
