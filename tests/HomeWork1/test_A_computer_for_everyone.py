import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork1.A_computer_for_everyone import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["1 1", "1", "2"], (1, [1]), id="example1"),
        param(["1 1", "1", "1"], (0, [0]), id="example2"),
        param(["2 2", "1 2", "2 3"], (2, [1, 2]), id="test3"),
        param(["3 3", "1 2 3", "3 4 2"], (3, [3, 1, 2]), id="test5"),
    ],
)
def test_solve(lines, expected):
    assert main(lines) == expected
