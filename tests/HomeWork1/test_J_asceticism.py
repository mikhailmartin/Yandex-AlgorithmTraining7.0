import sys
sys.path.append("../..")

import pytest
from pytest import param
from HomeWork1.J_asceticism import Solver


EVENTS1 = [
    ("Cappuccino", 25),
    ("Car", 5),
    ("Food", 4),
    ("Apartment", 1),
    ("Shopping", 7),
]


@pytest.mark.parametrize(
    ("spiritual_power", "events", "max_materiality", "expected"),
    [
        param(3, EVENTS1, 25, (4, 9, set(["Apartment", "Car", "Food", "Shopping"]))),
    ],
)
def test_solve(spiritual_power, events, max_materiality, expected):

    solver = Solver(spiritual_power, events, max_materiality)
    solver.solve()

    assert (solver.k, solver.t, set(solver.reject_event_names)) == expected
