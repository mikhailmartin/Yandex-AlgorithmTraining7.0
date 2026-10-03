import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork4.F_piggy_banks import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["4", "2", "1", "2", "4"], 2, id="example1"),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
