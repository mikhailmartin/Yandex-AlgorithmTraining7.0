import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork1.C_internet.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "11",
                "1 1 10 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1",
            ],
            5,
            id="example",
        ),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
