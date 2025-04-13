import sys
sys.path.append("../..")

import pytest
from pytest import param
from HomeWork1.A_each_with_a_computer import solve


@pytest.mark.parametrize(
    ("groups", "classrooms", "expected"),
    [
        param([1], [2], (1, [1])),  # тест 1
        param([1], [1], (0, [0])),  # тест 2
        param([1, 2], [2, 3], (2, [1, 2])),  # тест 3
        param([1, 2, 3], [3, 4, 2], (3, [3, 1, 2])),  # тест 5
    ],
)
def test_A_each_with_a_computer(groups, classrooms, expected):

    assert solve(groups, classrooms) == expected
