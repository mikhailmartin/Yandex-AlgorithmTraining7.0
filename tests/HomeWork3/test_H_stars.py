import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork3.H_stars import Solver, BinaryIndexedTree2D


def test_bit2d_init():
    matrix = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
    ]
    expected = [0, 1, 2, 3, 8, 7,6, 13, 8]
    bit2d = BinaryIndexedTree2D.from_matrix(matrix)
    assert bit2d.tree == expected


@pytest.mark.parametrize(
    ("edges", "expected"),
    [
        param((0, 0, 0, 0), 0),
        param((2, 2, 2, 2), 8),
        param((1, 1, 2, 2), 24),
    ],
)
def test_bit2d_get(edges, expected):
    matrix = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
    ]
    bit2d = BinaryIndexedTree2D.from_matrix(matrix)
    assert bit2d.get(*edges) == expected


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "2",
                "2 1 1 1 1 1 1",
                "1 0 0 0 1",
                "1 0 1 0 3",
                "2 0 0 0 0 0 0",
                "2 0 0 0 0 1 0",
                "1 0 1 0 -2",
                "2 0 0 0 1 1 1",
                "3",
            ],
            [0, 1, 4, 2],
            id="example1",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
