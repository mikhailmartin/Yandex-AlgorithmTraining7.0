import sys
sys.path.append("../..")

import pytest
from pytest import param
from HomeWork1.I_elastic_rover import Product, Solver


PRODUCTS1 = [
    Product(1, 4, 1, 2),
    Product(2, 3, 1, 2),
    Product(3, 2, 1, 2),
]
PRODUCTS2 = [
    Product(1, 4, 1, 3),
    Product(2, 3, 1, 2),
    Product(3, 2, 1, 1),
]
PRODUCTS3 = [
    Product(1, 1000, 1_000_000, 0),
]
PRODUCTS4 = [
    Product(1, 1000, 1_000_000, 0),
]
PRODUCTS12 = [
    Product(1, 65, 861, 121),
    Product(2, 53, 532, 462),
    Product(3, 6, 611, 904),
    Product(4, 90, 158, 917),
    Product(5, 41, 462, 456),
    Product(6, 47, 961, 438),
    Product(7, 15, 101, 226),
    Product(8, 82, 374, 979),
    Product(9, 47, 15, 788),
    Product(10, 37, 497, 771),
]


@pytest.mark.parametrize(
    ("volume_rover", "products", "expected"),
    [
        param(7, PRODUCTS1, (3, [3, 2, 1])),  # тест 1
        param(7, PRODUCTS2, (2, [3, 2])),  # тест 2
        param(1000, PRODUCTS3, (1_000_000, [1])),  # тест 3
        param(999, PRODUCTS4, (0, [])),  # тест 4
        # param(95, PRODUCTS12, (, [])),  # тест 12
    ],
)
def test_solve(volume_rover, products, expected):

    solver = Solver(volume_rover, products)
    solver.solve()

    assert (solver.max_cost, solver.numbers) == expected
