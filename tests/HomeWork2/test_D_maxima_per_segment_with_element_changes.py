import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork2.D_maxima_per_segment_with_element_changes.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "5",
                "1 2 3 4 5",
                "5",
                "s 1 5",
                "u 3 10",
                "s 1 5",
                "u 2 12",
                "s 1 3",
            ],
            [5, 10, 12],
            id="example",
        ),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
