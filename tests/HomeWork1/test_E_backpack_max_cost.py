import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork1.E_backpack_max_cost.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["1 597", "18", "16"], 16, id="example1"),
        param(["2 789", "45 44", "51 41"], 92, id="example2"),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
