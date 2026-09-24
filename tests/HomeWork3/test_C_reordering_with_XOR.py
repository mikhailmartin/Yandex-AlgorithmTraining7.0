import os
import sys
from functools import reduce
from operator import xor

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork3.C_reordering_with_XOR import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "3",
                "7 10 11",
            ],
            True,
            id="example1",
        ),
        param(
            [
                "3",
                "7 10 3",
            ],
            False,
            id="example2",
        ),
        param(
            [
                "2",
                "1 2"
            ],
            True,
            id="custom1",
        ),
        param(
            [
                "2",
                "1 3"
            ],
            False,
            id="custom2",
        ),
        param(
            [
                "4",
                "1 2 4 28"
            ],
            True,
            id="custom3",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    ok, nums = solver.solve()
    assert ok == expected
    if ok:
        assert (reduce(xor, nums) == 0) == expected
