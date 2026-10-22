import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork1.D_backpack_max_weight.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["1 5968", "18"], 18, id="example"),
    ]
)
def test_main(lines, expected):
    assert main(lines) == expected
