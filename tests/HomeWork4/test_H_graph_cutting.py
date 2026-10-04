import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork4.H_graph_cutting import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "3 3 7",
                "1 2",
                "2 3",
                "3 1",
                "ask 3 3",
                "cut 1 2",
                "ask 1 2",
                "cut 1 3",
                "ask 2 1",
                "cut 2 3",
                "ask 3 1",
            ],
            [
                "YES",
                "YES",
                "NO",
                "NO",
            ],
            id="example1",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
