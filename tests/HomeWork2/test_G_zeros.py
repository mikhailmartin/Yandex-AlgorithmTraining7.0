import sys
sys.path.append("../..")

from HomeWork2.G_zeros import Solver, Node, Filler


ARRAY_1 = [328, 0, 0, 0, 0]
SEGMENT_TREE_1_1 = [
    # глубина 0
    Node(4, 0, 4, False),
    # глубина 1
    Node(3, 0, 3, False),
    Node(1, 1, 1, True),
    # глубина 2
    Node(1, 0, 1, False),
    Node(2, 2, 2, True),
    Node(1, 1, 1, True),
    Filler(0, 0, 0, False),
    # глубина 3
    Node(0, 0, 0, False),
    Node(1, 1, 1, True),
    Node(1, 1, 1, True),
    Node(1, 1, 1, True),
    Node(1, 1, 1, True),
    Filler(0, 0, 0, False),
    Filler(0, 0, 0, False),
    Filler(0, 0, 0, False),
]


def test1():

    solver = Solver(array=ARRAY_1)

    solver.build_segment_tree()
    assert solver.segment_tree == SEGMENT_TREE_1_1
