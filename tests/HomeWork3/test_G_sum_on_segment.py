import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork3.G_sum_on_segment import Solver, BinaryIndexedTree1D


def test_bit1d_init():
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected = [0, 1, 2, 6, 4, 9, 6, 28, 8, 17]
    bit1d = BinaryIndexedTree1D(arr)
    assert bit1d.tree == expected


@pytest.mark.parametrize(
    ("idx", "expected"),
    [
        param(0, 0),
        param(1, 1),
        param(2, 3),
        param(3, 6),
        param(4, 10),
        param(5, 15),
        param(6, 21),
        param(7, 28),
        param(8, 36),
        param(9, 45),
    ],
)
def test_bit1d__get(idx, expected):
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    bit1d = BinaryIndexedTree1D(arr)
    assert expected == bit1d._get(idx)


@pytest.mark.parametrize(
    ("edges", "expected"),
    [
        param((0, 0), 0, id="custom1"),
        param((1, 1), 1, id="custom2"),
        param((2, 2), 2, id="custom3"),
        param((3, 3), 3, id="custom4"),
        param((4, 4), 4, id="custom5"),
        param((8, 9), 17, id="custom6"),
    ],
)
def test_bit1d_get(edges, expected):
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    bit1d = BinaryIndexedTree1D(arr)
    assert expected == bit1d.get(*edges)


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "5 9",
                "A 2 2",
                "A 3 1",
                "A 4 2",
                "Q 1 1",
                "Q 2 2",
                "Q 3 3",
                "Q 4 4",
                "Q 5 5",
                "Q 1 5",
            ],
            [0, 2, 1, 2, 0, 5],
            id="example1",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
