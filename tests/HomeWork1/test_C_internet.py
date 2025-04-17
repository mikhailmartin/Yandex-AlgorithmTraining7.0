import sys
sys.path.append("../..")

import pytest
from pytest import param
from HomeWork1.C_internet import solve


@pytest.mark.parametrize(
    ("m", "seconds", "expected"),
    [
        param(11, [1, 1, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 5),
    ],
)
def test_C_internet(m, seconds, expected):

    assert solve(m, seconds) == expected
