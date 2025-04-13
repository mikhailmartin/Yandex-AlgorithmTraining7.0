import sys
sys.path.append("../..")

import pytest
from pytest import param
from HomeWork1.B_no_more_no_less import solve


@pytest.mark.parametrize(
    ("test_sample", "expected"),
    [
        # тест 1
        param([1, 3, 3, 3, 2], (3, [1, 3, 1])),
        param([1, 9, 8, 7, 6, 7, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9], (3, [1, 6, 9])),
        param([7, 2, 3, 4, 3, 2, 7], (3, [2, 3, 2])),
        # тест 2
        param([1, 1, 9, 2, 9, 9, 9, 5, 8], (4, [1, 1, 2, 5])),
        param([10, 9, 9, 10, 3, 4, 1, 8, 2, 7], (5, [4, 2, 1, 2, 1])),
    ],
)
def test_B_no_more_no_less(test_sample, expected):

    assert solve(test_sample) == expected
