import sys
sys.path.append("../..")

from HomeWork2.F_nearest_larger_number_on_right import Solver


ARRAY1 = [1, 2, 3, 4]


def test1():

    solver = Solver(array=ARRAY1)

    solver.build_segment_tree()
    assert solver.segment_tree == [4, 2, 4, 1, 2, 3, 4]

    solver.u_query(2, 3)
    assert solver.segment_tree == [4, 3, 4, 1, 3, 3, 4]
