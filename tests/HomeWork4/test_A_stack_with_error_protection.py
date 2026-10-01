import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork4.A_stack_with_error_protection import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "push 1",
                "back",
                "exit",
            ],
            ["ok", "1", "bye"],
            id="example1",
        ),
        param(
            [
                "size",
                "push 1",
                "size",
                "push 2",
                "size",
                "push 3",
                "size",
                "exit",
            ],
            ["0", "ok", "1", "ok", "2", "ok", "3", "bye"],
            id="example2",
        ),
        param(
            [
                "push 3",
                "push 14",
                "size",
                "clear",
                "push 1",
                "back",
                "push 2",
                "back",
                "pop",
                "size",
                "pop",
                "size",
                "exit",
            ],
            ["ok", "ok", "2", "ok", "ok", "1", "ok", "2", "2", "1", "1", "0", "bye"],
            id="example3",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
