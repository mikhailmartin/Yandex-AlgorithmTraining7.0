import sys
sys.path.append("../..")

import pytest
from pytest import param
from HomeWork1.D_backpack_max_weight import solve


@pytest.mark.parametrize(
    ("m", "weights", "expected"),
    [
        param(5968, [18], 18),  # тест 1
    ]
)
def test_D_backpack_max_weight(m, weights, expected):

    assert solve(m, weights) == expected
