import os
import sys

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork3.E_points_on_plane import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["3 4", "5 23"], (7, 18), id="example1"),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
