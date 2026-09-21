import sys
sys.path.append("../..")

from HomeWork2.I_maxima_per_segment_with_addition_on_segment import Solver, Node


ARRAY1 = [2, 4, 3, 1, 5]
SEGMENT_TREE_1_1 = [
    # глубина 0
    Node(5, 0),
    # глубина 1
    Node(4, 0),
    Node(5, 0),
    # глубина 2
    Node(4, 0),
    Node(3, 0),
    Node(5, 0),
    Node(float("-inf"), 0),
    # глубина 3
    Node(2, 0),
    Node(4, 0),
    Node(3, 0),
    Node(1, 0),
    Node(5, 0),
    Node(float("-inf"), 0),
    Node(float("-inf"), 0),
    Node(float("-inf"), 0),
]
SEGMENT_TREE_1_2 = [
    # глубина 0
    Node(104, 0),
    # глубина 1
    Node(104, 0),
    Node(5, 0),
    # глубина 2
    Node(104, 0),
    Node(3, 100),
    Node(5, 0),
    Node(float("-inf"), 0),
    # глубина 3
    Node(2, 0),
    Node(4, 100),
    Node(3, 0),
    Node(1, 0),
    Node(5, 0),
    Node(float("-inf"), 0),
    Node(float("-inf"), 0),
    Node(float("-inf"), 0),
]


def test_build_segment_tree():

    solver = Solver(array=ARRAY1)
    solver.build_segment_tree()

    assert solver.segment_tree == SEGMENT_TREE_1_1


def test_update():

    solver = Solver(array=ARRAY1)
    solver.build_segment_tree()
    solver.query(("a", 2, 4, 100))

    assert solver.segment_tree == SEGMENT_TREE_1_2


def test_get():

    solver = Solver(array=ARRAY1)
    solver.build_segment_tree()

    assert solver.query(("m", 1, 3)) == 4

    solver.query(("a", 2, 4, 100))

    assert solver.query(("m", 1, 3)) == 104
