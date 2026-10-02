import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork4.E_weak_link import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["5", "4 5 5 2 3"], [3, 0, 0, 1, 2], id="example1"),
        param(["5", "5 1 3 1 5"], [0, 1, 2, 1, 0], id="example2"),
        param(["3", "6 6 6"], [0, 0, 0], id="example3"),
        param(["4", "6 5 5 6"], [0, 0, 0, 0], id="example4"),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
