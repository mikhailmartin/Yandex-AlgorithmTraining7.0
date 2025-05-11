import sys
sys.path.append("../..")

import pytest
from pytest import param
from HomeWork2.A_number_of_maxima_per_segment import build_sparse_table, query


ARRAY1 = [7, 1, 2, 4, 2, 3, 1]
ARRAY3 = [
    2, 2, 2, 1, 6, 6, 4, 10, 3, 6, 3, 10, 1, 10, 3, 4, 9, 10, 8, 10, 8, 5, 7, 6, 5, 8,
    1, 10, 7, 9, 5, 1, 2, 8, 4, 2, 5, 2, 9, 1, 3, 8, 10, 1, 10, 7, 4, 8, 8, 8, 6, 3, 10,
    2, 1, 9, 8, 1, 1, 5, 7, 1, 9, 2, 6, 9, 9, 3, 4, 4, 4, 6, 9, 9, 6, 4, 7, 2, 8, 5, 9,
    9, 6, 8, 8, 8, 4, 8, 1, 4, 3, 6, 8, 2, 4, 7, 9, 4, 4, 1,
]
QUERIES3 = [
    (26, 38),
    (13, 83),
    (53, 74),
    (14, 46),
    (64, 67),
    (12, 30),
    (17, 52),
    (7, 52),
    (30, 43),
    (19, 77),
    (8, 90),
    (24, 29),
    (52, 90),
    (3, 40),
    (37, 58),
    (10, 39),
    (2, 47),
    (9, 80),
    (15, 69),
    (24, 81),
    (56, 63),
    (9, 51),
    (23, 44),
    (92, 95),
    (13, 97),
    (1, 8),
    (39, 48),
    (19, 26),
    (44, 70),
    (9, 87),
    (3, 92),
    (86, 100),
    (18, 32),
    (65, 89),
    (5, 45),
    (11, 79),
    (83, 100),
    (27, 59),
    (10, 30),
    (23, 70),
    (48, 54),
    (43, 50),
    (54, 92),
    (23, 55),
    (60, 69),
    (26, 44),
    (9, 41),
    (15, 15),
    (74, 80),
    (20, 31),
    (42, 70),
    (22, 36),
    (86, 94),
    (5, 72),
    (54, 77),
    (15, 63),
    (45, 55),
    (21, 55),
    (22, 91),
    (48, 62),
    (3, 46),
    (9, 31),
    (40, 52),
    (6, 81),
    (1, 97),
    (36, 83),
    (1, 33),
    (27, 67),
    (23, 29),
    (6, 85),
    (72, 90),
    (20, 82),
    (37, 84),
    (73, 82),
    (71, 81),
    (23, 80),
    (37, 73),
    (20, 22),
    (44, 53),
    (16, 75),
    (68, 72),
    (6, 96),
    (13, 72),
    (22, 77),
    (42, 59),
    (46, 68),
    (48, 80),
    (11, 86),
    (7, 8),
    (27, 49),
    (23, 72),
    (2, 51),
    (11, 80),
    (33, 78),
    (21, 55),
    (46, 100),
    (18, 40),
    (1, 50),
    (79, 80),
    (8, 37),
]


def test_build_sparse_table():

    sparse_table, depths = build_sparse_table(ARRAY1)
    expected_sparse_table = [
        [(0, 0)] + [(num, 1) for num in ARRAY1],
        [(0, 0), (7, 1), (2, 1), (4, 1), (4, 1), (3, 1), (3, 1)],
        [(0, 0), (7, 1), (4, 1), (4, 1), (4, 1)],
    ]
    expected_depths = [-1, 0, 1, 1, 2, 2, 2, 2]

    assert sparse_table == expected_sparse_table
    assert depths == expected_depths


def test_query():

    sparse_table, depths = build_sparse_table(ARRAY3)
    for left, right in QUERIES3:

        array = [0] + ARRAY3
        max_true = max(array[left: right+1])
        count_true = array[left: right+1].count(max_true)

        max_pred, count_pred = query(sparse_table, depths, left, right)

        print(f"{left=}, {right=}, {max_true=}, {count_true=}, {max_pred=}, {count_pred=}")

        assert (max_pred, count_pred) == (max_true, count_true)
