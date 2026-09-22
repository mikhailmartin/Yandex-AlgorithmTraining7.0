import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork3.A_count_of_ones import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["9"], 2, id="example1"),
        param(["0"], 0, id="custom1"),
        param(["1"], 1, id="custom2"),
        param(["2"], 1, id="custom3"),
        param(["3"], 2, id="custom4"),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
