import os
import sys

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork3.D_fun_game import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["1"], 1, id="example1"),
        param(["11"], 14, id="custom1"),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
