import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork1.B_no_more_no_less.main import solve


@pytest.mark.parametrize(
    ("test_sample", "expected"),
    [
        # пример 1
        param([1, 3, 3, 3, 2], (3, [1, 3, 1])),
        param([1, 9, 8, 7, 6, 7, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9], (3, [1, 6, 9])),
        param([7, 2, 3, 4, 3, 2, 7], (3, [2, 3, 2])),
        # пример 2
        param([1, 1, 9, 2, 9, 9, 9, 5, 8], (4, [1, 1, 2, 5])),
        param([10, 9, 9, 10, 3, 4, 1, 8, 2, 7], (5, [4, 2, 1, 2, 1])),
    ],
)
def test_solve(test_sample, expected):
    assert solve(test_sample) == expected
