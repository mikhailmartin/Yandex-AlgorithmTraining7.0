import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork3.I_fixing_one_error import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            ["1", "01010"],
            "010010100",
            id="example1-part1",
        ),
        param(
            ["2", "010010101"],
            "01010",
            id="example1-part2",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
