import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork4.D_switching_between_windows import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "6",
                "Run Mozilla Firefox",
                "Run Free Pascal",
                "Alt+Tab",
                "Run Miranda IM",
                "Alt+Tab+Tab",
                "Alt+Tab+Tab+Tab",
            ],
            [
                "Mozilla Firefox",
                "Free Pascal",
                "Mozilla Firefox",
                "Miranda IM",
                "Free Pascal",
                "Free Pascal",
            ],
            id="example1",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
