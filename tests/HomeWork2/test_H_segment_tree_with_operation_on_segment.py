import sys
sys.path.append("../..")

from HomeWork2.H_segment_tree_with_operation_on_segment import Solver


ARRAY1 = [2, 4, 3, 5, 2]
SEGMENT_TREE_1_1 = [
    0,
    0, 0,
    0, 0, 0, 0,
    2, 4, 3, 5, 2, 0, 0, 0,
]
SEGMENT_TREE_1_2 = [
    0,
    0, 0,
    10, 0, 0, 0,
    2, 4, 13, 5, 2, 0, 0, 0,
]


def test_build_segment_tree():

    solver = Solver(array=ARRAY1)
    solver.build_segment_tree()

    assert solver.segment_tree == SEGMENT_TREE_1_1


def test_update():

    solver = Solver(array=ARRAY1)
    solver.build_segment_tree()
    solver.query(("a", 1, 3, 10))

    assert solver.segment_tree == SEGMENT_TREE_1_2


def test_get():

    solver = Solver(array=ARRAY1)
    solver.build_segment_tree()
    solver.query(("a", 1, 3, 10))

    assert solver.query(("g", 1)) == 12
    assert solver.query(("g", 2)) == 14
    assert solver.query(("g", 3)) == 13
    assert solver.query(("g", 4)) == 5
    assert solver.query(("g", 5)) == 2
