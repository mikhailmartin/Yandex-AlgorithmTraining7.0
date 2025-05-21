import sys
sys.path.append("../..")

from HomeWork2.D_maxima_per_segment_with_element_changes import Solver


ARRAY1 = [1, 2, 3, 4, 5]


def test1():

    solver = Solver(array=ARRAY1)

    solver.build_segment_tree()
    assert solver.segment_tree == [5, 4, 5, 2, 4, 5, float("-inf"), 1, 2, 3, 4, 5, float("-inf"), float("-inf"), float("-inf")]

    maxima = solver.s_query(
        left_segment_border=1-1,
        right_segment_border=5-1,
        node_index=0,
        left_node_border=0,
        right_node_border=solver.shift,
    )
    assert maxima == 5

    solver.u_query(number=3, value=10)
    assert solver.segment_tree == [10, 10, 5, 2, 10, 5, float("-inf"), 1, 2, 10, 4, 5, float("-inf"), float("-inf"), float("-inf")]
