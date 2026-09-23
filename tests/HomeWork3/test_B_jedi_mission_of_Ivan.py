import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork3.B_jedi_mission_of_Ivan import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "3",
                "0 1 1",
                "1 0 1",
                "1 1 0",
            ],
            [1, 1, 1],
            id="example1",
        ),
        param(
            [
                "5",
                "0 0 1 1 1",
                "0 0 2 0 2",
                "1 2 0 1 3",
                "1 0 1 0 1",
                "1 2 3 1 0",
            ],
            [1, 2, 3, 1, 3],
            id="example2",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
