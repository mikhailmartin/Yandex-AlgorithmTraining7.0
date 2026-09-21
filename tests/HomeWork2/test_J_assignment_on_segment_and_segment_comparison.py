import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork2.J_assignment_on_segment_and_segment_comparison import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "5",
                "1 2 1 2 1",
                "4",
                "1 2 4 2",
                "0 3 5 2",
                "1 1 3 2",
                "1 2 3 3",
            ],
            ["+", "-", "+"],
            id="example1",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
