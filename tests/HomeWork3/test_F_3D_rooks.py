import os
import sys

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork3.F_3D_rooks import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "2 2",
                "1 1 1",
                "2 2 2",
            ],
            (True, (1, 1, 1)),
            id="example1",
        ),
        param(
            [
                "2 2",
                "1 1 1",
                "1 1 2",
            ],
            (False, (2, 2, 1)),
            id="example2"
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
