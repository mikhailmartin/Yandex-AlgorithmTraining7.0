import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork4.C_deque_with_error_protection import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "push_back 1",
                "back",
                "exit",
            ],
            ["ok", "1", "bye"],
            id="example1",
        ),
        param(
            [
                "size",
                "push_back 1",
                "size",
                "push_back 2",
                "size",
                "push_front 3",
                "size",
                "exit",
            ],
            ["0", "ok", "1", "ok", "2", "ok", "3", "bye"],
            id="example2",
        ),
        param(
            [
                "push_back 3",
                "push_front 14",
                "size",
                "clear",
                "push_front 1",
                "back",
                "push_back 2",
                "front",
                "pop_back",
                "size",
                "pop_front",
                "size",
                "exit",
            ],
            ["ok", "ok", "2", "ok", "ok", "1", "ok", "1", "2", "1", "1", "0", "bye"],
            id="example3",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
